"""Construit la page de l'artifact « Ficolia · Récit de la figue » à partir des maquettes.

Usage : python3 outils/apercu.py <sortie.html>   (depuis la racine du dépôt)

L'artifact enveloppe lui-même la page (doctype, <html>, <head>, <body>). Chaque maquette
est montée dans sa propre zone isolée (Shadow DOM) : ses styles et ses identifiants ne
débordent pas sur les autres. Son script reçoit cette zone comme racine (ROOT) au lieu
du document. En tête, l'avancement des écrans du récit (FICOLIA_DESIGN.md §2) ; on passe
d'une maquette à l'autre par leur nom.
"""
import re
import sys

TITRE = "Ficolia · Récit de la figue"

# Les écrans du périmètre, dans l'ordre du brief : (nom, état, libellé, (ancre, maquette) ou None).
ECRANS = [
    ("Ouverture", "validee", "validée", None),
    ("Accueil, trois écrans", "a-venir", "à venir", None),
    ("Formulaire envoyé", "maquette", "maquette", ("formulaire", "maquettes/formulaire-envoye.html")),
    ("Connexion insuffisante ou absente", "maquette", "maquette", ("connexion", "maquettes/connexion-insuffisante.html")),
    ("Mise à jour obligatoire", "maquette", "maquette", ("mise-a-jour", "maquettes/mise-a-jour-obligatoire.html")),
    ("Délai de connexion", "a-venir", "à venir", None),
    ("Produit inconnu", "maquette", "maquette", ("inconnu", "maquettes/produit-inconnu.html")),
    ("Service indisponible", "maquette", "maquette", ("service", "maquettes/service-indisponible.html")),
]
DEFAUT = "service"  # l'écran affiché à l'ouverture : le dernier travaillé

POLICE = "'Atkinson Hyperlegible Next','Atkinson Hyperlegible',system-ui,sans-serif"

STYLE_PAGE = """
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--page);color:var(--page-texte);font-family:%(police)s;-webkit-tap-highlight-color:transparent}
.hote[hidden]{display:none}
.recit{padding-block:20px 0;padding-inline:16px}
.recit-in{max-width:840px;margin:0 auto;display:flex;flex-direction:column;gap:10px}
.recit-sur{margin:0;font-size:13px;font-weight:700;letter-spacing:.04em;color:var(--page-texte-2)}
.recit-etapes{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:6px}
.recit-etapes li>*{display:flex;align-items:center;gap:8px;min-height:36px;padding:0 12px;border-radius:999px;border:1px solid var(--page-trait);background:var(--surface);font-size:14px;color:var(--page-texte-2);text-decoration:none}
.recit-etapes li>*::before{content:"";width:8px;height:8px;border-radius:50%%;border:1.5px solid currentColor;flex:none}
.recit-etapes li[data-etat="validee"]>*::before{background:currentColor}
.recit-etapes a{color:var(--page-texte);cursor:pointer;transition:border-color 160ms ease,background-color 160ms ease}
.recit-etapes a::before{background:var(--choix);border-color:var(--choix)!important}
.recit-etapes a[aria-current="page"]{border-color:var(--choix);background:var(--choix);color:var(--choix-texte);font-weight:700}
.recit-etapes a[aria-current="page"]::before{background:var(--choix-texte);border-color:var(--choix-texte)!important}
.recit-etapes a[aria-current="page"] small{color:var(--choix-texte)}
.recit-etapes a:focus-visible{outline:2px solid var(--choix);outline-offset:2px}
@media (hover:hover) and (pointer:fine){.recit-etapes a:not([aria-current="page"]):hover{border-color:var(--choix)}}
.recit-etapes small{font-size:12px;font-weight:400;color:var(--page-texte-2)}
@media (max-width:760px){
  .recit-etapes{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
  .recit-etapes::-webkit-scrollbar{display:none}
  .recit-etapes li{flex:none}
}
""" % {"police": POLICE}


def extraire(chemin):
    with open(chemin, encoding="utf-8") as f:
        src = f.read()
    style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
    corps = src.split("<body>", 1)[1].split("</body>", 1)[0]
    script = re.search(r"<script>(.*?)</script>", corps, re.S).group(1)
    balisage = re.sub(r"<script>.*?</script>", "", corps, flags=re.S).strip()
    racine = re.search(r":root\{(.*?)\n\}", style, re.S).group(1)
    jetons = dict(re.findall(r"(--[\w-]+):([^;]+);", racine))
    sombre = re.search(r"(@media \(prefers-color-scheme:dark\)\{.*?\}\n\}\n:root\[data-theme=\"dark\"\]\{.*?\})", style, re.S).group(1)
    # La fonction de la maquette, appelée plus tard avec la zone isolée comme racine.
    script, n = re.subn(r"\}\)\(window\.__ficoliaRacine \|\| document\);[^\n]*\s*$", "})", script)
    assert n == 1, chemin
    assert "</script" not in script
    return {"style": style, "balisage": balisage, "script": script.strip(), "jetons": jetons, "sombre": sombre}


def entete():
    items = []
    for nom, etat, libelle, maquette in ECRANS:
        if maquette:
            ancre = maquette[0]
            items.append(f'<li data-etat="{etat}"><a href="#{ancre}" data-ecran="{ancre}"><span>{nom}</span><small>{libelle}</small></a></li>')
        else:
            items.append(f'<li data-etat="{etat}"><span><span>{nom}</span><small>{libelle}</small></span></li>')
    return (
        '<header class="recit"><div class="recit-in">'
        '<p class="recit-sur">Ficolia · le récit de la figue</p>'
        f'<nav aria-label="Écrans du récit"><ol class="recit-etapes">{"".join(items)}</ol></nav></div></header>'
    )


def construire():
    maquettes = [(m[0], extraire(m[1])) for _, _, _, m in ECRANS if m]
    jetons = {}
    for _, m in maquettes:
        jetons.update(m["jetons"])
    racine = ":root{\n" + "".join(f"  {k}:{v};\n" for k, v in jetons.items()) + "}\n"
    morceaux = [
        f"<title>{TITRE}</title>",
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;700&amp;display=swap" rel="stylesheet">',
        "<style>\n" + racine + maquettes[0][1]["sombre"] + "\n" + STYLE_PAGE + "</style>",
        entete(),
    ]
    for ancre, m in maquettes:
        hote_style = f":host{{display:block;color:var(--page-texte);font-family:{POLICE}}}\n"
        morceaux.append(f'<div class="hote" id="hote-{ancre}" hidden></div>')
        morceaux.append(f'<template id="tpl-{ancre}"><style>{hote_style}{m["style"]}</style>{m["balisage"]}</template>')
        morceaux.append(f"<script>\n(window.__ficoliaEcrans = window.__ficoliaEcrans || {{}})['{ancre}'] = {m['script']};\n</script>")
    ancres = [a for a, _ in maquettes]
    morceaux.append("""<script>
document.documentElement.lang = "fr";
(() => {
  const ancres = %(ancres)s, defaut = '%(defaut)s', montees = new Set();
  function montrer(ancre) {
    if (!ancres.includes(ancre)) ancre = defaut;
    for (const a of ancres) document.getElementById('hote-' + a).hidden = a !== ancre;
    for (const lien of document.querySelectorAll('.recit-etapes a')) {
      if (lien.dataset.ecran === ancre) lien.setAttribute('aria-current', 'page');
      else lien.removeAttribute('aria-current');
    }
    if (!montees.has(ancre)) {
      montees.add(ancre);
      const racine = document.getElementById('hote-' + ancre).attachShadow({ mode: 'open' });
      racine.appendChild(document.getElementById('tpl-' + ancre).content.cloneNode(true));
      window.__ficoliaEcrans[ancre](racine);
    }
    // Sur téléphone, la rangée défile : on la centre sur l'écran affiché.
    const rangee = document.querySelector('.recit-etapes');
    const courant = rangee.querySelector('[aria-current="page"]');
    if (courant) rangee.scrollLeft = courant.parentElement.offsetLeft - (rangee.clientWidth - courant.offsetWidth) / 2;
  }
  window.addEventListener('hashchange', () => montrer(location.hash.slice(1)));
  montrer(location.hash.slice(1));
})();
</script>""" % {"ancres": repr(ancres), "defaut": DEFAUT})
    return "\n".join(morceaux) + "\n"


if __name__ == "__main__":
    sortie = sys.argv[1]
    page = construire()
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(page)
    print("ok", sortie, len(page))
