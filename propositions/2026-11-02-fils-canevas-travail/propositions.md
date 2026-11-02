# Fils du canevas de travail, 02/11 : ce qui est proposé, ce qui attend la porteuse

Canevas : « ficolia - prototype_vTravail », https://claude.ai/artifact/FB6cC6xawyir9Y1QwCYosb. Le 02/11, la porteuse y a ouvert sept fils, tous envoyés à Claude. Claude a répondu dans chacun ; aucun n'est fermé, car la porteuse les ferme après lecture. Ce fichier garde le texte exact des propositions, pour qu'une autre session puisse les appliquer sans relire les fils.

Tous les textes nouveaux ci-dessous sont des **propositions** (`FICOLIA_DESIGN.md`, §3.5 ; `design/textes.md`, §4) : rien n'est posé sur les planches avant le choix de la porteuse. Ils respectent les règles de texte : aucune consigne (« évitez »…), aucun « vous », aucun mot interdit (« sûr », « sans danger »…), aucune date, aucune promesse ; « un bébé » plutôt que « le bébé », qui suppose un bébé né (`D-114` C1).

## Vue d'ensemble

| Fil | Planche | Demande de la porteuse | État |
| --- | --- | --- | --- |
| `b2bd2428` | `E1-Ouverture-Arbre` | « slogan 2s c'est validé, 3s c'est trop long. changement fait manuellemnt » | **fait** : rapatrié (R3, commit `10ac429`). Question : passer aussi à 2 s les trois autres planches au même réglage ? |
| `0940e8c9` | `E1-Ouverture-Arbre` | « la police est sous-licence : 29lt riwaya informal / Pour l'instant sur le prototype on garde celle-ci, mais je vais devoir en chercher une gratuite. » | **noté** : aucun fichier de la police dans le dépôt ni sur le canevas ; à inscrire au registre (`T-636`, `T-558`) |
| `111f9ffa` | `EA-Verdict-Baume-Jaune` | « Toutes les mentions sont à reformuler car elles ne sont toujours pas clair pour un user tiers. » | **choix attendu** : piste A ou B (§1) |
| `8b340b1d` | `EA-Ingredients-Spray-Mention` (trace du 17/10) | « Les explications aux mentions sont aussi à reformuler car pas comprise du premier coup par un user tiers. » | **choix attendu** : explications du §2, et deux points à trancher |
| `99641baa` | `E2-Recherche-Aucun` | « image en arrière plan en filigrane de la figue : soit celle décidée en image fixe de la figue qui n'a pas trouvé le produit ou (en attendant) le logo en filigrane » | **fait** : version 37, commit `f8ffb55`. Choix attendu : la version de l'image ; le report sur les quatre autres planches de recherche (§3) |
| `a5b20715` | `E3-Verdict-ActualiserHorsLigne` | « "Les données" c'est à dire ? la liste INCI ou les études scientifique ? » | **choix attendu** : formulation A ou B (§4) |
| `19560b13` | `E5-Verdict-Reevalue` | « Durée d'afficage de cet encadré ? apparaît seulement une fois à la première consultation ? » | **choix attendu** : possibilité 1, 2 ou 3 (§5) |

## 1. Les mentions de la ligne allaitement (fil `111f9ffa`)

Les six mentions actuelles (décision 215, textes provisoires, `T-604`) : « Tétée · évaluée », « Tétée · évaluation incomplète », « Mamelon et aréole · non évalués », « Inhalation du produit par le bébé · non évaluée », « Contact avec la peau du bébé · non évalué », « Parfum · produit parfumé ».

Ce qui gêne sans doute un tiers : le couple « sujet · état » avec « évaluée / non évalué », qui ne dit pas ce que cela change ; et « le bébé ».

**Piste A : on garde les cases « sujet · état », avec des mots courants.**
1. Produit présent à la tétée · pris en compte
2. Produit présent à la tétée · évaluation incomplète
3. Sur le mamelon ou l'aréole · pas pris en compte
4. Ce qu'un bébé respire · pas pris en compte
5. Ce qui passe sur la peau d'un bébé · pas pris en compte
6. Parfum · présent

**Piste B : une phrase entière par case, sans état à part.**
1. La tétée est prise en compte.
2. Pour la tétée, l'évaluation est incomplète.
3. Ce verdict ne vaut pas sur le mamelon ni sur l'aréole.
4. Ce qu'un bébé respire n'est pas pris en compte.
5. Ce qui passe sur la peau d'un bébé n'est pas pris en compte.
6. Ce produit contient du parfum.

Le titre « À savoir sur ce verdict » peut rester.

**Où les poser, une fois choisies** : les 13 planches de verdict qui portent ces mentions, `E1-Allaitement`, `E2-Allaitement`, `E5-Allaitement`, `E5-Allaitement-Reevalue`, `EA-Verdict-Baume-Incomplet`, `-Baume-Jaune`, `-Baume-Vert`, `-Baume-ZoneIncomplete`, `-Gel`, `-Gel-Source`, `-Lait-Orange`, `-Lait-Sous`, `-Spray` ; la phrase du parfum figure aussi dans 29 planches, listes d'ingrédients comprises. Le code de ces textes est dans la logique des planches (tableau `els`, champs `titre`, `sujet`, `etat`, `texte`). Les traces du 17/10 restent telles quelles, comme témoins. Captures avant publication.

## 2. Les explications des mentions (fil `8b340b1d`)

Elles remplacent celles du fil `111f9ffa`, restées trop proches des textes actuels. Toutes suivent le même modèle : d'abord la situation concrète, en mots courants, puis ce que le verdict en fait.

1. Produit présent à la tétée, pris en compte (soin des mamelons) : « Ce produit s'applique aussi sur le mamelon. Ce verdict tient compte de ce qui peut en rester au moment de la tétée. »
2. Même cas, évaluation incomplète : « Ce produit s'applique aussi sur le mamelon. Pour au moins un de ses ingrédients, ce verdict ne peut pas dire ce qu'il en est au moment de la tétée. »
3. Mamelon et aréole, pas pris en compte (soins du corps) : « Ce verdict ne vaut que si le produit n'est mis ni sur le mamelon ni sur l'aréole. Sur ces zones, un bébé qui tète peut en avaler un peu : ce cas n'a pas été jugé. »
4. Ce qu'un bébé respire : « Un bébé qui se trouve tout près peut respirer un peu de ce produit. Ce verdict n'en tient pas compte. »
5. Ce qui passe sur la peau d'un bébé : « Un bébé porté contre une peau où ce produit a été mis peut en recevoir un peu sur sa propre peau. Ce verdict n'en tient pas compte. »
6. Parfum : « Ce produit contient du parfum. Or un nouveau-né se repère à l'odeur pour trouver le sein. » (même source). Variante plus explicite : ajouter « Un parfum peut couvrir cette odeur. »

**Points à trancher** :
- En 3, « peut en avaler un peu » et la variante du 6 disent le pourquoi. C'est plus clair, mais ce sont des affirmations à faire relire par la toxicologue, comme tous ces textes (`T-604`).
- En 3, « ne vaut que si… » décrit une condition, pas une consigne. Se lit-il comme une consigne ?

## 3. Le filigrane « aucun résultat » (fil `99641baa`)

**Fait** (version 37, commit `f8ffb55`) sur `E2-Recherche-Aucun` : l'image fixe validée le 12/10 de l'état « produit inconnu » (la figue et la cagette vide, `assets/eb8e2e06607c.png`, identique à `exports/animations/produit-inconnu_cagette-vide_derniere-image.png`), sous le message, centrée, décorative (masquée aux lecteurs d'écran), sans animation. Le logo n'a pas été nécessaire.

Réglage « Aucun résultat : figue en filigrane » : « Ton chaud (proposition, 02/11) » par défaut (gris chaud, proche du filigrane beige de l'état « champ vide »), « Couleurs atténuées » (les teintes de la figue, très pâles), « Aucun ».

**Choix attendu** : la version à garder ; et le report, avec la retouche du 29/10 (message centré), sur les quatre autres planches du gabarit de recherche (`E2-Recherche`, `E2-Recherche-Resultats`, `E2-Produit`, `E5-Recherche-HorsLigne`).

## 4. « Les données » du verdict à actualiser (fil `a5b20715`)

**Ce que c'est** (`D-91`, `D-92`, `T-511`) : le verdict tel qu'il a été enregistré sur le téléphone lors de sa dernière mise à jour. Ficolia garde sur le téléphone les verdicts consultés et ceux de son catalogue, pour fonctionner sans réseau. Entre-temps, la composition du produit ou l'évaluation de ses ingrédients a pu changer. Au-delà d'un certain âge sans mise à jour, Ficolia n'affiche plus le niveau : « verdict à actualiser ». Le seuil n'est pas fixé (`T-242`).

Textes actuels : « Les données de ce verdict sont trop anciennes pour être affichées. Il s'affichera dès qu'elles seront mises à jour. » ; sans connexion : « Pas de connexion : les données seront mises à jour dès que la connexion reviendra. »

**A** : « Ce verdict est enregistré sur ce téléphone depuis trop longtemps pour être affiché : il doit d'abord être mis à jour. » ; sans connexion : « Pas de connexion : la mise à jour se fera quand le téléphone sera connecté. »

**B** : « Depuis la dernière mise à jour de ce téléphone, l'évaluation de ce produit a pu changer. Ce verdict s'affichera une fois mis à jour. » ; sans connexion : la même ligne qu'en A.

A dit la cause sans entrer dans le détail. B dit pourquoi c'est important, mais « a pu changer » peut inquiéter un peu plus.

**Où les poser** : la phrase principale est sur 9 planches (`E3-Verdict-Actualiser`, `-ActualiserHorsLigne`, `-Incomplet`, `-Rappel`, `-TypeNonPrecise`, `E3-Ingredients-Actualiser`, `-Incomplet`, `-TypeNonPrecise`, `E5-Verdict-Reevalue`) ; la ligne « Pas de connexion » sur 6.

## 5. La durée de l'encadré « réévalué » (fil `19560b13`)

Rien ne la fixe : `D-282` dit où l'encadré apparaît et ce qu'il ne dit pas (ni ancien niveau, ni date, ni cause) ; la décision 200 (30/10) note la proposition de Claude, « première ouverture seulement », à confirmer. Dans le prototype, l'encadré ne disparaît jamais : la planche est figée sur l'état « réévalué ».

1. À la première ouverture du verdict après la réévaluation, puis plus jamais. **Recommandée** : discret, sans geste de plus ; la trace durable reste l'étiquette « Réévalué » de l'historique. Risque : un verdict ouvert sans être lu fait manquer l'encadré.
2. Jusqu'à ce qu'on le ferme, avec une croix : plus sûr, mais un geste et une cible de 44 px de plus.
3. Pendant un nombre de jours fixé : déconseillé, délai arbitraire et règle invisible pour l'utilisatrice.

Une fois le choix fait : l'inscrire comme décision et mettre à jour la note de la planche.
