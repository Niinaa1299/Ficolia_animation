#!/usr/bin/env python3
"""Vérifie les liens et les boutons des planches du prototype, sans rien modifier.

Usage, depuis la racine du dépôt :
    python3 -I outils/verifier-liens.py [dossier-des-planches]
Par défaut : prototype/sources/project/.

Ce que le rapport donne :
1. les liens vers une planche absente (href="X.dc.html", ou 'X.dc.html' dans le code des planches) ;
2. les planches absentes de canvas.json, et les entrées de canvas.json sans fichier ;
3. par page du canevas, les planches qu'aucun lien n'atteint : souvent des variantes figées d'un état, des
   comparaisons ou des traces, à regarder une à une avant de conclure à un chaînon manquant ;
4. les planches sans aucun lien sortant ;
5. la barre d'onglets : les planches dont les cibles diffèrent des quatre onglets attendus ;
6. les boutons sans action (sans sc-camel-on-click), hors boutons grisés (aria-disabled), par libellé ;
7. les gestionnaires appelés par un bouton mais absents du code de la planche (hors boucles item.*, h.*).

Écrit le 02/11/2026 à partir de la vérification des liens faite ce jour-là (décision 197).

Limites : c'est une lecture des sources, pas un parcours. Elle ne dit pas si un lien mène au bon écran, ni ce
que fait un gestionnaire. Une planche « que rien n'atteint » peut être atteinte par un réglage, comme les états
d'un même gabarit.
"""
import collections, glob, json, os, re, sys

TAB = {"E1-Scan.dc.html", "E2-Recherche.dc.html", "E5-Historique.dc.html", "E6-Menu.dc.html"}


def libelle(tag, contenu):
    m = re.search(r'aria-label="([^"]*)"', tag)
    if m:
        return m.group(1)
    t = re.sub(r"<[^>]+>", " ", contenu)
    return re.sub(r"\s+", " ", t).strip()[:60]


def main():
    dossier = sys.argv[1] if len(sys.argv) > 1 else "prototype/sources/project"
    fichiers = sorted(glob.glob(os.path.join(dossier, "*.dc.html")))
    noms = {os.path.basename(f) for f in fichiers}
    index = json.load(open(os.path.join(dossier, "canvas.json"), encoding="utf-8"))
    planches = index["boards"]
    sortants, entrants = {}, collections.defaultdict(set)
    absents = collections.defaultdict(set)
    sans_action = collections.defaultdict(set)
    gest_absents = collections.defaultdict(set)
    onglets = {}
    for f in fichiers:
        n = os.path.basename(f)
        s = open(f, encoding="utf-8").read()
        script = s[s.find("data-dc-script"):]
        cibles = set(re.findall(r'href="([^"#{]+?\.dc\.html)"', s)) | set(re.findall(r"'([A-Za-z0-9-]+\.dc\.html)'", s))
        sortants[n] = cibles
        for c in cibles:
            entrants[c].add(n)
            if c not in noms:
                absents[c].add(n)
        for m in re.finditer(r"(<button\b[^>]*>)(.*?)</button>", s, re.S):
            tag, contenu = m.group(1), m.group(2)
            if "sc-camel-on-click" not in tag:
                if 'aria-disabled="true"' not in tag:
                    sans_action[libelle(tag, contenu)].add(n[:-8])
            else:
                h = re.search(r'sc-camel-on-click="\{\{\s*([A-Za-z_$][\w$]*)', tag)
                if h and h.group(1) not in ("item", "h") and not re.search(r"\b" + re.escape(h.group(1)) + r"\b", script):
                    gest_absents[(libelle(tag, contenu), h.group(1))].add(n[:-8])
        nav = re.search(r'<nav aria-label="Navigation principale".*?</nav>', s, re.S)
        if nav:
            t = set(re.findall(r'href="([^"]+)"', nav.group(0)))
            if not t <= TAB | {"E5-Historique-Reevalue.dc.html", "E5-Historique-Reevalues.dc.html", "E5-Historique-Evalue.dc.html"} or not TAB <= t:
                onglets[n[:-8]] = sorted(x[:-8] if x.endswith(".dc.html") else x for x in t)

    print(f"{len(fichiers)} planches lues dans {dossier}\n")
    print("1. Liens vers une planche absente :", "aucun" if not absents else "")
    for c, d in sorted(absents.items()):
        print(f"   {c} ← {sorted(x[:-8] for x in d)}")
    print("\n2. Planches hors de canvas.json :", sorted(noms - set(planches)) or "aucune")
    print("   Entrées de canvas.json sans fichier :", sorted(set(planches) - noms) or "aucune")
    print("\n3. Planches qu'aucun lien n'atteint, par page :")
    pages = collections.defaultdict(list)
    for n, b in planches.items():
        pages[b.get("page", "?")].append(n)
    for p, ns in pages.items():
        o = sorted(x[:-8] for x in ns if x in noms and not entrants.get(x))
        if o:
            print(f"   {p} ({len(o)}) : {', '.join(o)}")
    print("\n4. Planches sans aucun lien sortant :", sorted(n[:-8] for n, c in sortants.items() if not c) or "aucune")
    print("\n5. Barres d'onglets incomplètes ou inattendues :", "aucune" if not onglets else "")
    for n, t in sorted(onglets.items()):
        print(f"   {n} : {t}")
    print("\n6. Boutons sans action (hors grisés), par libellé :", "aucun" if not sans_action else "")
    for k, v in sorted(sans_action.items(), key=lambda x: -len(x[1])):
        print(f"   {len(v):3d} × « {k} » ; ex. {sorted(v)[:3]}")
    print("\n7. Gestionnaires introuvables dans le code de la planche :", "aucun" if not gest_absents else "")
    for (k, h), v in sorted(gest_absents.items()):
        print(f"   {h} (« {k} ») : {sorted(v)[:3]}")


if __name__ == "__main__":
    main()
