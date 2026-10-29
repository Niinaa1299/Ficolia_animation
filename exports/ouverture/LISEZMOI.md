# L'ouverture et l'accueil, prêts pour le prototype

Exportés le 29/10 par `outils/exporter-ouverture.mjs`, depuis la maquette `maquettes/ouverture-arbre.html`, avec les choix de la porteuse :
- la révélation du logo, puis « l'arbre et la figue », en gros plan puis recul ;
- le vert pâle accroché au pré (`recul3`, 29/10) ;
- l'accueil 2/2, piste A, la lecture sous le figuier (29/10).

**Les vidéos et les images ne portent aucun texte.** Tous les textes sont du HTML posé par-dessus. On les change sans refaire l'export.

## Les fichiers

| Fichier | Ce que c'est |
| --- | --- |
| `ouverture.mp4`, `ouverture.webm` | 10 s : la révélation, puis l'arbre et la figue, jusqu'à l'image fixe de l'accueil 1/2. |
| `accueil-2_piste-a.mp4`, `accueil-2_piste-a.webm` | 4,4 s : après « Continuer », l'accueil 2/2, piste A. Sa première image est, au pixel près, la dernière de l'ouverture : le passage d'une vidéo à l'autre ne se voit pas. |
| `revelation_derniere-image.png` | Le logo seul, détouré (fond transparent) : la fin de la révélation, pour « réduire les animations ». |
| `accueil-1_derniere-image.png`, `accueil-2_piste-a_derniere-image.png` | Les images fixes du 1/2 et du 2/2. Ce sont, au pixel près, les dernières images des vidéos, mouvement réduit compris. Elles servent à « réduire les animations » et à « Retour ». |
| `ouverture.html` | La page de référence : les vidéos, et tous les textes par-dessus, aux instants de la maquette. Elle s'ouvre dans un navigateur, à côté des autres fichiers. |
| `exports.json` | Pour chaque vidéo : durée, taille, poids, et le réglage de la maquette d'où elle vient. |

Format commun :
- plein écran, 390 × 844 points, en ×2 (780 × 1688 px) ;
- 60 images par seconde ;
- couleurs en BT.709, écrites dans les fichiers.

Le mp4 (H.264) se lit sur les téléphones et dans Safari, Chrome, Edge et Firefox. La webm (VP9) le remplace dans les navigateurs qui ne lisent pas le H.264, dont le Chromium des essais automatiques.

## Changer un texte

Dans `ouverture.html`, tout est dans le bloc « LES TEXTES : à modifier ici ». Dans le prototype, c'est le même HTML, recopié dans la planche.

- **L'accroche** : une ligne par paragraphe ; la seconde paraît 0,3 s après la première. Elle est centrée sous le logo, à 377,7 points du haut. Chacune de ses deux lignes fait environ 270 px, pour 390 de large.
- **Les textes de l'accueil** sont posés sur le vert pâle.
  - Au 1/2, le bloc commence à 476 points du haut, et à 396 au 2/2.
  - S'ils s'allongent ou s'agrandissent, ils défilent, et les boutons restent en bas (cap §2). C'est vérifié pour un texte agrandi ×1,3 et ×2, et pour un texte long au 2/2.
- **Les étiquettes « statut »** (pointillés) disent où en est chaque texte. Elles se masquent par `?statuts=off`.
- **Règles** : les règles de texte du projet s'appliquent (`design/textes.md`, brief §3 et §4). Tout texte nouveau est marqué « Proposition », et certains textes passent par la juriste.

Les textes posés le 29/10 sont ceux de la maquette, mot pour mot, sauf l'accroche :

| Où | Texte | Statut |
| --- | --- | --- |
| Accroche | « Continuer à prendre soin de soi, / sans vérifier ses flacons dix fois. » | Celle du prototype (décision 132 de la porteuse, 12/10), texte provisoire. Elle remplace « Vos cosmétiques, en toute sérénité. », écartée le 12/10. Voir les limites. |
| 1/2 | « Bienvenue sur Ficolia » | Titre : proposition (22/10) |
| 1/2 | « [L’objectif de Ficolia, en une phrase : à écrire] » | À écrire (cap §4) |
| 1/2 | « Ce n’est pas un avis médical. Pour toute question de santé, adressez-vous à un professionnel de santé. » | Le rappel général (`D-114` C8), en attente de la juriste |
| 2/2 | « Conditions d’utilisation » ; « Pour utiliser Ficolia, il faut en accepter les conditions d’utilisation. » ; « [Limites essentielles, en mots simples — en attente de la juriste] » ; « Lire les conditions d'utilisation » ; « Politique de confidentialité » ; « Conditions d'utilisation — version du [date] » | Ceux du prototype (05/10), provisoires ; la juriste (`T-557`) |
| Boutons | « Continuer », « Accepter », « Retour » (pour les lecteurs d'écran) | « Accepter » est acté |

## Les instants, pour la planche

En millisecondes depuis le début de chaque vidéo. Deux courbes :
- **douce** : `cubic-bezier(.37,0,.63,1)` ;
- **révélation** : `cubic-bezier(.25,.6,.35,1)`.

| Texte | Paraît | S'en va |
| --- | --- | --- |
| Accroche, 1re ligne | 3500 → 4050 : fondu, et monte de 7,94 px (révélation) | 4600 → 5050 : fondu (douce) ; elle descend aussi de 40 px, de 4550 à 5450 (douce) |
| Accroche, 2e ligne | 3800 → 4350 (révélation) | avec la 1re |
| Texte du 1/2 | 7950 → 8450 : fondu, et monte de 8 px (douce) | au 2/2, 0 → 300 : fondu (douce) |
| Points et « Continuer » | 8000 → 8450 : fondu (douce) | au 2/2, 0 → 300 |
| Texte du 2/2 | 1500 → 2000 après « Continuer » : fondu, et monte de 8 px (douce) | — |
| Points, « Accepter », « Retour » | 1550 → 2000 : fondu (douce) | — |

« Continuer » est entier à 8,41 s. Le texte et les boutons sont invisibles, donc impossibles à toucher, tant qu'ils n'ont pas commencé à paraître.

**Mouvement réduit.** Que des fondus linéaires, sans aucun déplacement, comme dans la maquette.
- **Ouverture, 2,1 s**
  1. Le logo seul et l'accroche paraissent de 0 à 600.
  2. Ils s'effacent de 1500 à 1800, pendant que l'image fixe du 1/2 paraît, de 1500 à 2100.
  3. Le texte du 1/2 et « Continuer » paraissent de 1800 à 2100.
- **2/2, 1,2 s**
  1. Le texte du 1/2 s'efface (0 → 300).
  2. L'image du 1/2 s'efface (300 → 600).
  3. L'image du 2/2 paraît (600 → 900).
  4. Le texte, « Accepter » et « Retour » paraissent (900 → 1200).

## L'intégrer au prototype

D'après la note de reprise du prototype (21/10, §6), qui fait foi pour le canevas « Ficolia — Prototype ». C'est à faire dans la discussion du prototype, avec la porteuse.

1. **Déposer les sept fichiers dans la réserve du canevas** : les deux mp4, les deux webm et les trois png, par une publication avec `asset: true`. Un chemin relatif ne s'affiche pas dans ce type de canevas. Chaque fichier reçoit une adresse `/_blob/<identifiant>`, à recopier telle quelle dans les balises `<source>`, `<img>` et dans `poster`.
2. **Reprendre l'élément `.ecran` de `ouverture.html` dans une planche**, avec son CSS : les vidéos, les images, les textes. L'enchaînement 1/2 → 2/2 → « Retour » partage un état : il tient sur une seule planche (note, « Un état par planche »).
3. **La logique de la planche**, sur le modèle du script de la page :
   - lancer la vidéo au montage, sauf si le téléphone demande de réduire les animations ;
   - « Continuer » montre et lance la vidéo du 2/2 ;
   - « Retour » montre l'image fixe du 1/2 ;
   - « Accepter » mène au scanner (`E1-Scan`).
4. **Les textes attendent la vidéo** (classe `attente`) et se recalent sur son horloge. Sans cela, une vidéo lente à démarrer laisserait paraître le texte avant la figue.
5. Cette ouverture remplacerait, sur le canevas :
   - « Ouverture · animation, lue une fois » et « Ouverture · image fixe » (la révélation seule) ;
   - les six planches de l'accueil en trois écrans, d'avant le cap du 17/10 (deux écrans).

   À trancher avec la porteuse.

## Vérifié le 29/10

- **Les textes de la page suivent ceux de la maquette.** À 27 instants de l'ouverture et du 2/2, même opacité (écart 0,000) et même place (0,1 px au plus). Pour l'accroche, seuls l'instant et la place sont comparés, puisque son texte a changé.
- **Images entières, page contre maquette, en ×2**
  - écart moyen de 0,1 à 1,6 niveau sur 255 ;
  - jusqu'à 3,7 sur 255 pendant la descente dans le feuillage (6 à 7,75 s), où la compression touche le bord des traits. Ce n'est pas visible, même au grossissement ×2.
  - En mouvement réduit, l'écart moyen est de 1,3 au plus.
- **Vidéos décodées contre les images d'origine** : écart moyen de 0,75 (ouverture) et 1,2 (2/2) sur 255. Pas de bandes dans les dégradés du ciel ni du vert pâle.
- **Lecture réelle**
  - Les textes suivent la vidéo à deux images près.
  - Le passage au 2/2 se fait sans saut ni éclair.
  - Au 2/2, le focus passe au titre des conditions une fois le texte paru ; « Retour » le rend à « Continuer ».
  - Avant 7,95 s, « Continuer » n'est pas touchable.
  - La console n'affiche aucune erreur.
- **Les six états** (`exports/animations/`, 12/10) : leurs maquettes n'ont pas changé, et leur dernière image refaite le 29/10 est identique, au pixel près, à celle de l'export.

## Limites

- **Le mp4 n'a pas été lu dans un navigateur.** Celui des essais ne lit pas le H.264 : le mp4 a été vérifié décodé par ffmpeg, et la webm dans Chromium. Il reste à le regarder sur un iPhone et un Android, et dans Safari, où les couleurs n'ont pas été vérifiées.
- **L'accroche.**
  - Son texte est celui de la décision 132 du prototype. La réserve de Claude du 12/10 tient toujours : « sans vérifier ses flacons dix fois » peut se lire comme la promesse de ne plus avoir à vérifier. Or le brief §4 (« Aucune promesse ») et le dossier (§4.3, règle 5 ; `T-533`) l'écartent. C'est à la porteuse et à la juriste de trancher.
  - Sa police est Atkinson Hyperlegible Next, comme sur le canevas (décision 131, à valider). Le brief (§5) disait Nunito, à confirmer.
- **La révélation** est celle de la maquette, redessinée aux couleurs de la marque, comme sur le canevas (décision 132 : « la palette de la marque prime sur les couleurs du fichier »).
- **« Continuer » à 8,41 s** : c'est un écart au cap §1 (« Le lancement doit être immédiat »), à tracer au registre. Il s'ajoute aux 5 s de la révélation sans « Passer » (`PASSATION.md` §3).
- **Les polices** se chargent depuis Google Fonts. Hors réseau, une police de secours les remplace.
- **Une vidéo ne se retouche pas.** Pour changer l'animation elle-même, il faut changer la maquette, puis refaire l'export.
- **Le mode « instant figé »** (`?t=`) sert aux captures. Dans un navigateur sans écran, la toute première image d'une vidéo peut tarder d'une seconde à s'afficher : faire une première capture pour rien.

## Refaire l'export

Depuis la racine du dépôt, avec Playwright (Chromium) et ffmpeg (libx264, libvpx-vp9) :

```
NODE_PATH=<dossier où Playwright est installé> node outils/exporter-ouverture.mjs exports/ouverture
```

L'export prend environ trois minutes. Le mp4 ressort identique octet pour octet ; la webm peut différer de quelques octets (encodage en parallèle), sans changer l'image. `ouverture.html` et ce fichier ne sont pas touchés.
