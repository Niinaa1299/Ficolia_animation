#!/usr/bin/env python3
"""Prépare la publication des planches dans le canevas : copie les sources qui référencent une ressource
(assets/<empreinte>.<ext>) en remplaçant chaque chemin relatif par l'adresse /_blob/… de la réserve du
canevas (prototype/sources/blobs.json). Les sources du dépôt ne sont pas modifiées.

Usage, depuis la racine du dépôt :
    python3 -I outils/preparer-publication.py <dossier-de-sortie> [source.dc.html ...]
Sans source nommée : toutes les planches de prototype/sources/project/ qui référencent une ressource.

Pourquoi : le canevas n'affiche pas un chemin relatif (note de reprise du 21/10, §6 ; constaté de nouveau le
01/11 : les vidéos restaient invisibles), alors que le rendu local (outils/rendre.mjs) en a besoin.

Écrit <sortie>/project/<Nom>.dc.html pour chaque planche concernée, et affiche la liste. Une ressource absente
de blobs.json arrête le script : il faut la téléverser d'abord et compléter la table.
"""
import glob, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(RACINE, "prototype", "sources")


def main():
    if len(sys.argv) < 2:
        sys.exit("usage : preparer-publication.py <dossier-de-sortie> [source.dc.html ...]")
    sortie = os.path.abspath(sys.argv[1])
    table = json.load(open(os.path.join(SOURCES, "blobs.json"), encoding="utf-8"))["ressources"]
    fichiers = sys.argv[2:] or sorted(glob.glob(os.path.join(SOURCES, "project", "*.dc.html")))
    os.makedirs(os.path.join(sortie, "project"), exist_ok=True)
    faits, manquantes = [], set()
    for f in fichiers:
        src = open(f, encoding="utf-8").read()
        refs = set(re.findall(r'(?<![\w/])assets/([0-9a-f]{12}\.[a-z0-9]+)', src))
        if not refs:
            continue
        for r in refs:
            if r in table:
                src = src.replace("assets/" + r, table[r])
            else:
                manquantes.add(r)
        dest = os.path.join(sortie, "project", os.path.basename(f))
        open(dest, "w", encoding="utf-8").write(src)
        faits.append(dest)
    if manquantes:
        sys.exit("ressources absentes de blobs.json, à téléverser d'abord : " + ", ".join(sorted(manquantes)))
    print(f"{len(faits)} planche(s) préparée(s) dans {sortie}")
    for d in faits:
        print(d)


if __name__ == "__main__":
    main()
