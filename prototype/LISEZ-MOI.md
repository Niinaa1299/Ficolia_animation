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
| `sources/project/canvas.json` | Un index composé par le déballage : une page du canevas par export, les planches en rangées (les positions d'origine ne sont pas dans l'export). |
| `sources/project/assets/` | Les ressources téléversées (images, vidéos) que les exports emballent, nommées par empreinte ; les planches les référencent en chemin relatif. |
| `sources/noms.json` | La table titre d'écran → nom de fichier. **Déduite**, à confirmer sur le canevas. |
| `sources/RAPPORT-<page>.md` | Le rapport de chaque déballage : vérifications planche par planche, écarts, limites. |
| `captures/<page>/*.png` | Les écrans rendus localement depuis les sources reconstituées (échelle 2). |
| `../outils/deballer-export.py` | Le déballage. |
| `../outils/rendre.mjs` | Le rendu local d'une source, avec le moteur du canevas. |
| `../outils/runtime/` | Le moteur (`support.js`, c'est-à-dire dc-runtime) et React, extraits de l'export. Servent au rendu local seulement ; ne se publient pas dans un canevas, qui a le sien. |

## Ce que contient un export

L'export « page par page » est une page HTML unique qui emballe (gzip + base64, bloc `__bundler/manifest`) une page par planche. Chaque page de planche emballe à son tour le moteur, React, la police utilisée, les ressources téléversées qu'elle affiche, et **la source de la planche telle que le canevas la stocke**, à trois remplacements près, que le déballage inverse :

1. `<script src="./support.js"></script>` renommé vers un identifiant aléatoire ;
2. la feuille Google Fonts (`<link css2>`) incorporée en `@font-face`, et la police emballée ;
3. chaque ressource téléversée (`/_blob/…` sur le canevas) remplacée par un identifiant, son contenu emballé. Le déballage l'extrait sous `project/assets/` et la référence en chemin relatif ; l'identifiant `/_blob/` d'origine est perdu, ce qui ne change rien pour un canevas neuf.

Le reste est repris tel quel : balisage `<x-dc>`, trous `{{…}}`, boucles `sc-for`/`sc-if`, réglages `data-props`, SVG en ligne, liens de prototype entre planches (par nom de fichier d'origine).

## Déballer un nouvel export

Depuis la racine du dépôt :

```
python3 -I outils/deballer-export.py "prototype/exports/<date> <page>.html" --page <nom-court>
```

Avec `--titre "<nom de la page>"` pour nommer la page dans le canevas. Rejouer un export remplace sa page dans l'index sans toucher aux autres. Puis compléter `sources/noms.json` pour les titres que le rapport signale « pas dans noms.json », et relancer. Pour vérifier le rendu :

```
node outils/rendre.mjs prototype/captures/<nom-court> prototype/sources/project/*.dc.html
```

## Vérifications faites le 31/10 (5 pages, 74 planches)

- Pages déballées : étape 1 sans animation (16), étape 2 (12), étape 6 (16), étape 7 (5), ligne allaitement (25). Sans écart : chaque source a sa ligne `support.js`, son `<x-dc>` et son bloc `data-dc-script` ; aucun identifiant d'export restant ; 3 ressources extraites (la vidéo « la figue s'incline », mp4 et webm, et sa dernière image, partagées par les quatre écrans « Nous écrire »).
- Rendu local des 74 sources reconstituées sans erreur de page. Pour l'étape 1, comparé pixel à pixel aux captures de l'export (même moteur, échelle 2) : 0 % de pixels franchement différents (écart > 128/255) sur chaque écran ; 1 à 3 % d'écarts faibles (> 40/255), dus à l'anticrénelage, la capture de l'export passant par une iframe décalée d'un demi-pixel.
- Un lien cassé constaté dans les sources (donc sur le canevas) : les écrans produit et ingrédients de la ligne allaitement pointent vers `EA-Verdict-Lait`, planche écartée et retirée depuis ; la vérification globale des liens (décision 197) est encore à faire.

## Limites, à ne pas perdre de vue

- **Les noms de fichiers sont déduits** des titres et des liens entre planches. Le bandeau de chaque planche, sur le canevas, permet de les confirmer.
- **La disposition, les pages et les notes du canevas** ne sont pas dans l'export : `canvas.json` est une recomposition. L'archive du 22/10 (remise à la porteuse, hors dépôt) porte l'index d'alors.
- **Le `<link>` Google Fonts** est reconstitué à partir des `@font-face` ; l'original n'est pas dans l'export.
- **Les ressources téléversées** sont dans l'export et extraites, mais sous un nouveau nom (empreinte) et en chemin relatif : l'identifiant `/_blob/` du canevas d'origine n'est pas récupérable.
- **Les commentaires et l'historique des versions** restent sur le canevas.
- **Aucune comparaison octet par octet avec le canevas** n'est possible.
- Le rendu local est une reconstitution : il sert à vérifier une modification, pas à remplacer le canevas.

## Rapporter dans un canevas

Les fichiers de `sources/project/` sont au format du canevas et se publient tels quels dans un canevas neuf (`project/<Nom>.dc.html`, `project/assets/…` et `project/canvas.json`). Le moteur n'a pas à être publié : chaque canevas a le sien. Le canevas prend le titre écrit dans `canvas.json`.

Fait le 31/10 : les 74 planches sont publiées dans le canevas neuf https://claude.ai/artifact/FB6cC6xawyir9Y1QwCYosb, que Claude Code lit et modifie (vérifié).
