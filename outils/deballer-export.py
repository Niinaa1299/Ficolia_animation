#!/usr/bin/env python3
"""Déballe un export HTML « modifiable » d'une page du canevas Design (claude.ai) et reconstitue les
sources des planches (.dc.html) telles que le canevas les stocke.

Usage, depuis la racine du dépôt :
    python3 -I outils/deballer-export.py <export.html> [--page <nom-court>] [--dest prototype/sources]

Ce que fait l'export du canevas (constaté sur l'export du 31/10/2026) :
  - une page unique, avec un manifeste (« __bundler/manifest ») qui emballe une page HTML par planche,
    compressée (gzip + base64), et un gabarit qui donne le titre de chaque planche ;
  - chaque page de planche est elle-même un paquet : son gabarit (« __bundler/template ») est la SOURCE
    de la planche, à deux remplacements près :
      1. la ligne <script src="./support.js"></script> est renommée vers un identifiant aléatoire
         (le moteur dc-runtime est emballé sous cet identifiant, avec React) ;
      2. la feuille Google Fonts (<link css2>) est incorporée sous forme de règles @font-face dans le
         <helmet><style>, et la police effectivement utilisée est emballée sous un identifiant.
  Ce script inverse ces deux remplacements. Tout le reste de la source est repris tel quel.

Ce qu'il produit :
  <dest>/project/<Nom>.dc.html    une source par planche, nommée d'après <dest>/noms.json
  <dest>/project/canvas.json      un index composé ici (disposition en rangées : les positions d'origine
                                  ne sont PAS dans l'export)
  outils/runtime/                 le moteur (support.js = dc-runtime) et React, extraits de l'export,
                                  pour le rendu local (voir outils/rendre.mjs)
  <dest>/RAPPORT-<page>.md        le rapport de déballage : vérifications par planche, écarts, limites

Limites connues :
  - Les positions, pages et notes du canevas d'origine ne sont pas dans l'export : canvas.json est recomposé.
  - Le <link> Google Fonts est reconstitué à partir des @font-face trouvés (familles, graisses, styles) :
    c'est la forme attendue par le canevas (cf. design/reference/revelation-logo.dc.html du zip du brief),
    mais l'ordre des paramètres et display=swap sont une hypothèse.
  - Les images téléversées (/_blob/…) ne seraient pas dans l'export ; le rapport les signalerait.
  - Aucune comparaison avec le canevas n'est possible : le serveur refuse d'en servir les fichiers.
"""
import argparse, base64, datetime, gzip, html, json, os, re, unicodedata
from collections import OrderedDict

MARQUE_RUNTIME = "// GENERATED from dc-runtime"
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def bloc(kind, src):
    m = re.search(r'<script type="__bundler/' + kind + r'">\s*(.*?)\s*</script>', src, re.S)
    return m.group(1) if m else None


def decode(entry):
    raw = base64.b64decode(entry["data"])
    return gzip.decompress(raw) if entry.get("compressed") else raw


def slug(titre):
    s = unicodedata.normalize("NFKD", titre).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    return s[:60] or "Planche"


def lien_google_fonts(style_css):
    """Reconstitue le <link css2> à partir des @font-face. Retourne (html, familles), ou (None, []) si le
    bloc contient autre chose que des @font-face et des commentaires."""
    reste = re.sub(r"/\*.*?\*/", "", style_css, flags=re.S)
    reste = re.sub(r"@font-face\s*\{[^}]*\}", "", reste, flags=re.S).strip()
    if reste:
        return None, []
    fam = OrderedDict()
    for f in re.findall(r"@font-face\s*\{([^}]*)\}", style_css, flags=re.S):
        name = re.search(r"font-family:\s*'([^']+)'", f)
        w = re.search(r"font-weight:\s*(\d+)", f)
        st = re.search(r"font-style:\s*(\w+)", f)
        if name:
            fam.setdefault(name.group(1), set()).add((1 if st and st.group(1) == "italic" else 0, int(w.group(1)) if w else 400))
    if not fam:
        return None, []
    parts = []
    for name, axes in fam.items():
        q = name.replace(" ", "+")
        if any(i for i, _ in axes):
            q += ":ital,wght@" + ";".join(f"{i},{w}" for i, w in sorted(axes))
        else:
            q += ":wght@" + ";".join(str(w) for _, w in sorted(axes))
        parts.append("family=" + q)
    href = "https://fonts.googleapis.com/css2?" + "&amp;".join(parts) + "&amp;display=swap"
    out = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
           '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">\n'
           f'<link href="{href}" rel="stylesheet">')
    return out, list(fam.keys())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--page", default=None, help="nom court de la page exportée (pour le rapport)")
    ap.add_argument("--dest", default=os.path.join(RACINE, "prototype", "sources"))
    a = ap.parse_args()
    dest = os.path.abspath(a.dest)
    noms_path = os.path.join(dest, "noms.json")
    noms = {k: v for k, v in json.load(open(noms_path, encoding="utf-8")).items() if not k.startswith("_")} if os.path.exists(noms_path) else {}
    page_id = a.page or slug(os.path.splitext(os.path.basename(a.export))[0])

    src = open(a.export, encoding="utf-8").read()
    manifest = json.loads(bloc("manifest", src))
    ordre = json.loads(bloc("page_order", src) or "[]")
    gabarit = json.loads(bloc("template", src))
    titres = {u: html.unescape(t) for t, u in re.findall(r'<h2>(.*?)</h2><iframe src="about:blank#([0-9a-f-]+)"', gabarit)}
    m = re.search(r"<title>(.*?)</title>", gabarit)
    titre_canevas = html.unescape(m.group(1)) if m else "Canevas"

    os.makedirs(os.path.join(dest, "project"), exist_ok=True)
    runtime_dir = os.path.join(RACINE, "outils", "runtime")
    os.makedirs(runtime_dir, exist_ok=True)

    rapport = [f"# Rapport de déballage — {page_id}", "",
               f"Export : `{os.path.basename(a.export)}` · déballé le {datetime.date.today().isoformat()} · canevas « {titre_canevas} »", "",
               f"Planches dans l'export : {len(ordre)} (manifeste : {len(manifest)} entrées).", "",
               "| # | Titre dans l'export | Fichier produit | Nom | Taille | support.js | x-dc | dc-script | $preview | trous | liens | images téléversées | identifiants restants |",
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    boards, order, ecarts, runtime_ok, fam_txt = OrderedDict(), [], [], False, "—"
    x = y = 0
    for i, u in enumerate(ordre, 1):
        page = decode(manifest[u]).decode("utf-8")
        man2 = json.loads(bloc("manifest", page))
        ext2 = json.loads(bloc("ext_resources", page) or "[]")
        source = json.loads(bloc("template", page))
        titre = titres.get(u, f"Planche {i}")

        # 1. le moteur, remis à sa place
        rt = [k for k, v in man2.items() if "javascript" in v["mime"] and decode(v)[:40].decode("utf-8", "replace").startswith(MARQUE_RUNTIME)]
        if rt:
            if not runtime_ok:
                open(os.path.join(runtime_dir, "support.js"), "wb").write(decode(man2[rt[0]]))
                for e in ext2:
                    if e["uuid"] in man2:
                        open(os.path.join(runtime_dir, os.path.basename(e["id"])), "wb").write(decode(man2[e["uuid"]]))
                runtime_ok = True
            source, n = re.subn(r'<script src="' + re.escape(rt[0]) + r'"></script>', '<script src="./support.js"></script>', source)
            if n != 1:
                ecarts.append(f"{titre} : ligne support.js non retrouvée ({n} remplacement)")
        else:
            ecarts.append(f"{titre} : moteur dc-runtime absent du paquet")

        # 2. les polices, rendues au <link> Google Fonts
        m = re.search(r"(<helmet>\s*<style>)(.*?)(</style>)", source, re.S)
        if m and "@font-face" in m.group(2):
            link, fams = lien_google_fonts(m.group(2))
            if link:
                source = source[:m.start()] + "<helmet>\n" + link + source[m.end():]
                fam_txt = ", ".join(fams)
            else:
                ecarts.append(f"{titre} : bloc @font-face mêlé à d'autres règles, laissé tel quel")

        # 3. le nom de fichier
        nom = noms.get(titre)
        if not nom:
            nom = slug(titre)
            ecarts.append(f"{titre} : pas dans noms.json, nommé {nom}")
        fichier = nom + ".dc.html"
        open(os.path.join(dest, "project", fichier), "w", encoding="utf-8").write(source)

        # 4. les vérifications
        uuids = sorted(set(re.findall(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", source)))
        props = re.search(r"data-props=\"(.*?)\"", source, re.S) or re.search(r"data-props='(.*?)'", source, re.S)
        prev = None
        if props:
            try:
                prev = json.loads(html.unescape(props.group(1))).get("$preview")
            except json.JSONDecodeError:
                ecarts.append(f"{titre} : data-props illisible")
        w, h = (prev or {}).get("width", 390), (prev or {}).get("height", 844)
        trous = len(set(re.findall(r"\{\{[^}]+\}\}", source)))
        liens = sorted(set(re.findall(r'href="([^"]*\.dc\.html)"', source)))
        blobs = len(re.findall(r"/_blob/", source))
        if blobs:
            ecarts.append(f"{titre} : {blobs} référence(s) à une image téléversée, absente de l'export")
        if uuids:
            ecarts.append(f"{titre} : identifiants d'export restants : {uuids}")
        rapport.append(f"| {i} | {titre} | `{fichier}` | {'table' if titre in noms else 'construit'} | {len(source.encode())} o | "
                       f"{'oui' if './support.js' in source else 'NON'} | {'oui' if '<x-dc>' in source else 'NON'} | {'oui' if 'data-dc-script' in source else 'NON'} | "
                       f"{w}×{h} | {trous} | {len(liens)} | {blobs} | {len(uuids)} |")

        boards[fichier] = {"x": x, "y": y, "w": w, "h": h, "title": titre}
        order.append(fichier)
        x += w + 80
        if i % 8 == 0:
            x, y = 0, y + h + 120

    index = {"v": 3, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
             "title": titre_canevas, "launch": {"view": "canvas"}, "pages": [], "boards": boards, "order": order, "notes": {}, "designSystems": []}
    with open(os.path.join(dest, "project", "canvas.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=1)

    rapport += ["", f"Polices reconstituées en `<link>` Google Fonts : {fam_txt}.", "",
                "## Écarts et points à vérifier", ""] + ([f"- {e}" for e in ecarts] or ["- Aucun écart relevé."]) + ["",
                "## Limites", "",
                "- Les positions, pages et notes du canevas d'origine ne sont pas dans l'export : `canvas.json` dispose les planches en rangées de 8, dans l'ordre de l'export.",
                "- Les noms de fichiers viennent de `noms.json` (déduits, à confirmer sur le canevas).",
                "- Le `<link>` Google Fonts est reconstitué (familles et graisses lues dans les `@font-face`) ; l'original n'est pas dans l'export.",
                "- Aucune comparaison octet par octet avec le canevas n'est possible : le serveur refuse d'en servir les fichiers."]
    with open(os.path.join(dest, f"RAPPORT-{page_id}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(rapport) + "\n")
    print("\n".join(rapport))


if __name__ == "__main__":
    main()
