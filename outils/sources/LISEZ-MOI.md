# Sources des maquettes assemblées et des artéfacts

Ces dossiers contiennent ce qui fabrique `maquettes/ouverture-arbre.html`, `site/proposition.html` et `site/maquette.html`. Relancés depuis le dépôt, les trois assembleurs redonnent ces trois fichiers à l'octet près (vérifié le 22/10).

Les fichiers assemblés ne sont pas faits pour être retouchés à la main : le prochain assemblage les écraserait. On modifie le gabarit, puis on assemble.

## Ce qu'il y a

| Fichier | Rôle |
| --- | --- |
| `donnees.json` | Les tracés : la figue du symbole (`FIG`), le logotype manuscrit (`LOGO`) et les traits de la révélation (`REV`). Partagé par les trois gabarits. |
| `arbre/gabarit.html` | Le gabarit de l'ouverture « l'arbre et la figue » (page, panneau de réglages, moteur d'animation). Les marques `/*@FIG@*/`, `/*@LOGO@*/`, `/*@REV@*/` reçoivent les tracés. |
| `arbre/assembler.py` | Injecte `donnees.json` dans le gabarit. |
| `site/gabarit-proposition.html` + `site/assembler.py` | Le dossier du site vitrine. |
| `site/maquette/gabarit.html` + `site/maquette/assembler.py` | La maquette animée du site vitrine. |
| `nom/ficolia-porteuse.png` + `nom/tracer.py` | Le nom en toutes lettres (porteuse, 22/10) : son image du mot complet, et le script qui en vectorise le « o » dans le repère du logo et mesure le rapprochement de « lia ». Le résultat est recopié à la main dans `arbre/gabarit.html` (`LETTRE_O`, `LIA_LETTRES`, `LOGO_C_LETTRES`). Le script demande `pillow`, `numpy` et `potracer` (`pip install potracer==0.0.4`, de préférence dans un environnement à part). |

## Assembler

Depuis la racine du dépôt. Les deux assembleurs du site relisent aussi les textes contre les mots interdits (`design/textes.md` §2) : ils ont besoin de `textes.md` et de `figue-symbole.svg`, qui sont dans le zip du brief. On les extrait dans un dossier vide, ici `ENTREES`.

```
mkdir ENTREES
unzip -j Ficolia_contexte_Claude_Code_09_10_2026.zip \
  'ficolia-claude-code/design/textes.md' 'ficolia-claude-code/design/assets/figue-symbole.svg' -d ENTREES

# L'ouverture : la maquette
python3 -I outils/sources/arbre/assembler.py outils/sources/arbre/gabarit.html \
  outils/sources/donnees.json maquettes/ouverture-arbre.html

# Le dossier du site : le fragment à publier, puis le document complet (site/proposition.html)
python3 -I outils/sources/site/assembler.py outils/sources/site/gabarit-proposition.html \
  outils/sources/donnees.json ENTREES/figue-symbole.svg ENTREES/textes.md \
  proposition-fragment.html site/proposition.html

# La maquette animée du site : le fragment à publier, puis le document complet (site/maquette.html)
python3 -I outils/sources/site/maquette/assembler.py outils/sources/site/maquette/gabarit.html \
  outils/sources/donnees.json ENTREES/textes.md maquette-fragment.html site/maquette.html

# L'aperçu « Récit de la figue » : tous les écrans dans une page (voir outils/apercu.py)
python3 -I outils/apercu.py apercu.html
```

## Publier

- Pour un artéfact, on publie le **fragment** (`proposition-fragment.html`, `maquette-fragment.html`, `apercu.html`) : l'outil Artifact l'enveloppe lui-même. Les fichiers « document » sont faits pour s'ouvrir tels quels dans un navigateur.
- La maquette du site charge ses images en `captures/<nom>.webp` : à la publication, on les joint avec `files`, par exemple `{"captures/scanner.webp": "site/captures/scanner.webp"}`, une entrée par image.
- Publié depuis un autre compte, un artéfact reçoit une nouvelle adresse, sauf si ce compte a reçu le droit de le modifier (partage en écriture) : il se met alors à jour à son adresse d'origine. C'est le cas du récit de la figue depuis le 22/10 (version 24).

## L'ouverture, par l'adresse

La maquette de l'ouverture se règle par l'adresse, ce qui permet aussi de figer un instant pour une capture :

| Réglage | Valeurs | Par défaut |
| --- | --- | --- |
| `bas` | `pale`, `profond`, `pale-bis`, `profond-bis`, `blanc` | `pale-bis` |
| `transition` (versions bis seulement) | `recul3` (son choix, retouché le 29/10 : le vert pâle du bas accroché au pré, il ne paraît qu'avec lui ; le texte et « Continuer » une fois la figue posée), `recul2` (son choix du 22/10 : gros plan, puis recul, tout se dévoile dans l'ordre, sans nom en haut), `recul`, `saut`, `brume`, `soleil`, `mouvement`, `bis` | `recul3` |
| `nom` (versions bis seulement, sauf `recul3` et `recul2`, qui n'ont plus de nom en haut) | `lettres` : « Ficolia » en toutes lettres en haut du paysage (22/10) ; `figue` : le logo avec la figue à la place du « o », pour mémoire | `lettres` |
| `ecran` (avec `recul3` ou `recul2` seulement) | `1` : l'accueil 1/2 ; `2` : l'accueil 2/2, les conditions (22/10), où mène aussi « Continuer » | `1` |
| `piste2` | le 2/2 : `a`, la lecture sous le figuier (son choix, 29/10) ; `b`, l'étal au bord du pré, pour mémoire | `a` |
| `mouvement` | `normal`, `reduit` | le réglage du téléphone |
| `notes` | `off` masque les notes du prototype | affichées |
| `t` | un instant figé, en millisecondes | lecture |
| `place`, `descente`, `decor` | choix du 18/10, gardés pour mémoire | `b`, `a`, `a` |

Les versions `pale` et `profond` (sans bis) restent identiques à leur état du 20/10.

## Exporter pour le prototype : `exports/`

Les animations validées sortent en vidéos et en images, sans aucun texte : les textes restent du HTML, dans les écrans du prototype. L'index de tout ce qui est exporté est dans `exports/LISEZMOI.md`.

| Script | Ce qu'il exporte |
| --- | --- |
| `outils/exporter-animations.mjs` | Les six états (12/10), seule l'illustration, dans `exports/animations/`. |
| `outils/exporter-ouverture.mjs` | L'ouverture et l'accueil (29/10), en plein écran, dans `exports/ouverture/`. La page de référence `ouverture.html`, écrite à la main, n'est pas touchée : elle pose les textes par-dessus, et ses instants sont ceux de la maquette. |

Les deux demandent Playwright (`NODE_PATH=<dossier de Playwright>`) et ffmpeg ; voir le `LISEZMOI.md` de chaque dossier.

## Vérifier : `outils/verification/`

Des scripts Playwright (Chromium) qui servent à regarder le résultat. Ils cherchent Playwright dans `/opt/node22/lib/node_modules/playwright` : remplacer ce chemin par celui de l'installation.

| Script | Ce qu'il fait |
| --- | --- |
| `frames.mjs <maquette> <dossier> <requête>…` | Une image de l'écran par requête, par exemple `"t=5200&notes=off&transition=recul"`. |
| `figzoom.mjs <maquette> <image.png> <requête>…` | La figue en gros plan, pour chaque requête. |
| `vitesse.mjs <maquette> <transition>…` | La vitesse de la vue image par image : pics et à-coups, pour juger de la fluidité. |
| `vitesse-detail.mjs <maquette> <transition> <de> <à>` | Le détail image par image autour d'un instant. |
| `arrivee.mjs <maquette> <transition>…` | Quand le texte et « Continuer » arrivent, et ce que dure l'animation avec eux (moins de 5 s : WCAG 2.2.2). |
| `bas-ecran.mjs <maquette> "<réglages>" [de] [à] [pas]` | Le bas de l'écran instant par instant : la ligne du pré, le haut du vert pâle et du fondu de l'herbe, la part de l'écran qu'ils couvrent, le texte. Signale tout bord visible du vert pâle. |
| `hub-arbre3.mjs <aperçu> <préfixe>` | L'ouverture dans l'aperçu : passage d'une transition à l'autre, fin, erreurs. |
| `export-textes.mjs <maquette> <page exportée>` | Les textes de `exports/ouverture/ouverture.html` contre ceux de la maquette, à 27 instants : opacité et place. |
| `export-lecture.mjs <page exportée>` | La page exportée en vraie lecture : les textes suivent la vidéo ; « Continuer », « Retour », focus ; mouvement réduit. |
| `site-maquette.mjs`, `site-dossier.mjs` | Parcours de la maquette et du dossier du site : erreurs, débordements, images. |
| `proto-captures.mjs` | Photographie les écrans du prototype (canevas de conception) pour les captures du site. |

Les autres scripts sont des outils des étapes précédentes (`hub-*.mjs` par écran, `video.mjs`, `trace.mjs`, `zoom.mjs`, `geo_*`…), gardés pour mémoire. Certains visent des écrans ou des réglages qui ont changé : `hub-arbre.mjs` cherche par exemple le bouton « Passer », supprimé de l'ouverture le 20/10.
