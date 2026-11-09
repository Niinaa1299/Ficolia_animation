# Prototype Ficolia : les sources des écrans, hors du canevas

Note du 31/10/2026. Ce dossier reconstitue, dans le dépôt, les sources des écrans du canevas « Ficolia — Prototype » (claude.ai, type Design), à partir des exports « HTML modifiable, page par page » que la porteuse fait depuis la page du canevas.

## État au 02/11 (à lire d'abord ; la suite décrit la reconstitution du 31/10)

- **Le canevas de travail** est « ficolia - prototype_vTravail », https://claude.ai/artifact/FB6cC6xawyir9Y1QwCYosb (voir `CLAUDE.md`, règles R1 à R6). L'ancien canevas est une archive.
- **Toutes les planches sont reprises** : 190 sur le canevas comme dans `sources/project/`. Il n'en manque aucune, sauf celles que la porteuse a décidé de ne pas reprendre (les 8 anciennes de l'étape 1, et Main, A à D).
- **L'index `sources/project/canvas.json` est celui du canevas.** Il a été relu en ligne et enregistré à l'octet près le 02/11 (R3). Ce n'est plus une recomposition : dispositions, titres et noms de pages sont ceux de la page.
- **Le lien cassé vers `EA-Verdict-Lait`** est réparé depuis le 01/11 (`ec3ac5d`). Le 02/11, aucun lien de planche ne pointe vers une planche absente.
- **Les ressources** (vidéos, images) sont dans la réserve du canevas. `sources/blobs.json` donne leurs adresses, et `../outils/preparer-publication.py` réécrit les chemins `assets/…` en `/_blob/…` pour la publication.
- **Lire et publier depuis Claude Code** passe par l'outil intégré « Artifact » (l'ancien serveur `claude-artifacts` n'est plus branché) :
  - lister les fichiers : `action: list`, `scope: files`, `url` du canevas. La liste donne les **tailles**, pas les empreintes ;
  - lire un ou plusieurs fichiers : `action: read`, `url`, `path` ou `paths`, `out_dir` dans le dossier de travail. La lecture donne l'empreinte sha256 ;
  - publier : `url`, `root: <dépôt>/prototype/sources` (ou le dossier de `preparer-publication.py`), `file_path` (chemin **absolu** d'un des fichiers), `files: {"project/X": "project/X"}`. L'outil refuse de publier sur une version qu'on n'a pas lue : faire d'abord un `read`.
- **Ce que vaut le contrôle R3** : comparer les tailles de la liste repère les retouches de la porteuse, sauf celles qui ne changent pas la longueur d'un fichier. Avant de remplacer une planche, lire sa version en ligne et comparer son contenu (fait depuis le 02/11, après une publication du 02/11 qui ne l'avait pas fait : voir `propositions/2026-11-02-voie-savon/journal-01-02-11.md`).
- **Deux outils ajoutés le 02/11** : `../outils/rendre-reglage.mjs` rend une planche avec un réglage imposé et liste les liens présents à l'écran (variables `CLIC` et `CAPTURE`) ; `../outils/verifier-liens.py` vérifie les liens et les boutons de toutes les planches (liens vers une planche absente, planches que rien n'atteint, barre d'onglets, boutons sans action). Mode d'emploi en tête de chaque fichier.
- **Le plan du prototype** (05/11, décision 273) : la planche `E0-Plan`, point de départ du test de navigation, mène à toutes les autres. Elle est écrite par `../outils/plan-du-prototype.py`, qui refuse d'écrire si une planche de `canvas.json` n'est dans aucune rubrique : **toute planche nouvelle s'ajoute à une rubrique du script, puis on le relance** (et on republie `E0-Plan` et `canvas.json`). Le canevas n'a pas de retour « à l'écran précédent » : chaque retour est un lien vers une planche fixe, sauf ceux du signalement : « Retour au verdict » relit le dernier verdict touché, « Retour au produit » le dernier écran produit touché, dans la mémoire de session (décisions 275 et 276 ; un verdict nouveau qui mène au signalement reçoit les lignes `ficolia-verdict` au début de `renderVals()`, un écran produit nouveau qui mène à « Ce n'est pas ce produit », les lignes `ficolia-produit`). La prise en main du premier lancement suit la même mémoire (clé `ficolia-tuto`, décision 277). Limites connues : journal du 05/11, « relier les écrans ».
- **Les commentaires** restent sur l'ancien canevas ; le canevas de travail n'en a pas hérité. Ses fichiers sont illisibles depuis Claude Code, mais ses fils de commentaires se lisent (outil « ArtifactComments », `action: read`, vérifié le 02/11 : 139 fils, dont 30 ouverts ; inventaire dans `propositions/2026-11-02-commentaires-ancien-canevas/fils-ancien-canevas.md`). Répondre ou fermer un fil demande l'accord de la porteuse (R6).

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
- Un lien cassé constaté dans les sources (donc sur le canevas) : les écrans produit et ingrédients de la ligne allaitement pointent vers `EA-Verdict-Lait`, planche écartée et retirée depuis (réparé le 01/11) ; la vérification globale des liens (décision 197) est encore à faire.

## Limites, à ne pas perdre de vue

- **Les noms de fichiers sont déduits** des titres et des liens entre planches. Le bandeau de chaque planche, sur le canevas, permet de les confirmer.
- **La disposition, les pages et les notes du canevas** ne sont pas dans l'export : `canvas.json` était une recomposition (31/10). Depuis le 02/11, c'est l'index relu sur le canevas de travail. L'archive du 22/10 (remise à la porteuse, hors dépôt) porte l'index d'alors.
- **Le `<link>` Google Fonts** est reconstitué à partir des `@font-face` ; l'original n'est pas dans l'export.
- **Les ressources téléversées** sont dans l'export et extraites, mais sous un nouveau nom (empreinte) et en chemin relatif : l'identifiant `/_blob/` du canevas d'origine n'est pas récupérable.
- **Les commentaires et l'historique des versions** restent sur le canevas.
- **Aucune comparaison octet par octet avec le canevas** n'était possible le 31/10. Depuis le 01/11, l'outil « Artifact » lit les fichiers du canevas de travail (voir « État au 02/11 »).
- Le rendu local est une reconstitution : il sert à vérifier une modification, pas à remplacer le canevas.

## Rapporter dans un canevas

Les fichiers de `sources/project/` sont au format du canevas et se publient tels quels dans un canevas neuf (`project/<Nom>.dc.html`, `project/assets/…` et `project/canvas.json`). Le moteur n'a pas à être publié : chaque canevas a le sien. Le canevas prend le titre écrit dans `canvas.json`.

Fait le 31/10 : les 74 planches sont publiées dans le canevas neuf https://claude.ai/artifact/FB6cC6xawyir9Y1QwCYosb, que Claude Code lit et modifie (vérifié).
