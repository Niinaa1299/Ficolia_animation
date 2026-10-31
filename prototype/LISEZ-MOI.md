# Prototype Ficolia : les sources des écrans, hors du canevas

Note du 31/10/2026. Ce dossier reconstitue, dans le dépôt, les sources des écrans du canevas « Ficolia — Prototype » (claude.ai, type Design), à partir des exports « HTML modifiable, page par page » que la porteuse fait depuis la page du canevas.

## Pourquoi

Depuis le 31/10, aucune session Claude Code ne peut lire ni modifier les fichiers du canevas : le serveur d'artefacts refuse tout canevas « dans lequel quelqu'un hors de l'organisation a écrit », et c'est le cas ici depuis la passation du 22/10 (un compte d'une autre organisation a publié les versions 280 à 342 ; voir `Ficolia — note de reprise, complément du 31-10.md`, branche `claude/relaxed-noether-g2fdj1`, §1). Dupliquer le canevas depuis sa page hérite de ce refus (vérifié le 31/10). L'outil « Artifact » qui passait outre est coupé depuis le 31/10.

Le seul chemin qui reste : les exports de la page, qui contiennent la source exacte de chaque planche (voir « Ce que contient un export »).

## Ce qu'il y a ici

| Chemin | Contenu |
| --- | --- |
| `exports/` | Les exports bruts, tels que déposés par la porteuse, datés. Ne pas modifier. |
| `sources/project/*.dc.html` | Les sources des planches, reconstituées, nommées comme dans le canevas. C'est ce qui se modifie. |
| `sources/project/canvas.json` | Un index composé par le déballage (disposition en rangées : les positions d'origine ne sont pas dans l'export). |
| `sources/noms.json` | La table titre d'écran → nom de fichier. **Déduite**, à confirmer sur le canevas. |
| `sources/RAPPORT-<page>.md` | Le rapport de chaque déballage : vérifications planche par planche, écarts, limites. |
| `captures/<page>/*.png` | Les écrans rendus localement depuis les sources reconstituées (échelle 2). |
| `../outils/deballer-export.py` | Le déballage. |
| `../outils/rendre.mjs` | Le rendu local d'une source, avec le moteur du canevas. |
| `../outils/runtime/` | Le moteur (`support.js`, c'est-à-dire dc-runtime) et React, extraits de l'export. Servent au rendu local seulement ; ne se publient pas dans un canevas, qui a le sien. |

## Ce que contient un export

L'export « page par page » est une page HTML unique qui emballe (gzip + base64, bloc `__bundler/manifest`) une page par planche. Chaque page de planche emballe à son tour le moteur, React, la police utilisée, et **la source de la planche telle que le canevas la stocke**, à deux remplacements près, que le déballage inverse :

1. `<script src="./support.js"></script>` renommé vers un identifiant aléatoire ;
2. la feuille Google Fonts (`<link css2>`) incorporée en `@font-face`, et la police emballée.

Le reste est repris tel quel : balisage `<x-dc>`, trous `{{…}}`, boucles `sc-for`/`sc-if`, réglages `data-props`, SVG en ligne, liens de prototype entre planches (par nom de fichier d'origine).

## Déballer un nouvel export

Depuis la racine du dépôt :

```
python3 -I outils/deballer-export.py "prototype/exports/<date> <page>.html" --page <nom-court>
```

Puis compléter `sources/noms.json` pour les titres que le rapport signale « pas dans noms.json », et relancer. Pour vérifier le rendu :

```
node outils/rendre.mjs prototype/captures/<nom-court> prototype/sources/project/*.dc.html
```

## Vérifications faites le 31/10 (page « étape 1 sans anim », 16 planches)

- Déballage sans écart : 16 sources, chacune avec sa ligne `support.js`, son `<x-dc>` et son bloc `data-dc-script` ; aucune image téléversée ; aucun identifiant d'export restant (`sources/RAPPORT-etape-1.md`).
- Rendu local des 16 sources reconstituées, comparé pixel à pixel aux captures de l'export (même moteur, échelle 2) : 0 % de pixels franchement différents (écart > 128/255) sur chaque écran ; 1 à 3 % d'écarts faibles (> 40/255), dus à l'anticrénelage, la capture de l'export passant par une iframe décalée d'un demi-pixel.

## Limites, à ne pas perdre de vue

- **Les noms de fichiers sont déduits** des titres et des liens entre planches. Le bandeau de chaque planche, sur le canevas, permet de les confirmer.
- **La disposition, les pages et les notes du canevas** ne sont pas dans l'export : `canvas.json` est une recomposition. L'archive du 22/10 (remise à la porteuse, hors dépôt) porte l'index d'alors.
- **Le `<link>` Google Fonts** est reconstitué à partir des `@font-face` ; l'original n'est pas dans l'export.
- **Les images et polices téléversées** (`/_blob/…`) ne seraient pas dans l'export ; aucune n'a été rencontrée dans cette page.
- **Les commentaires et l'historique des versions** restent sur le canevas.
- **Aucune comparaison octet par octet avec le canevas** n'est possible.
- Le rendu local est une reconstitution : il sert à vérifier une modification, pas à remplacer le canevas.

## Rapporter dans un canevas

Les fichiers de `sources/project/` sont au format du canevas et se publient tels quels dans un canevas neuf (`project/<Nom>.dc.html` et `project/canvas.json`). Le moteur n'a pas à être publié : chaque canevas a le sien.
