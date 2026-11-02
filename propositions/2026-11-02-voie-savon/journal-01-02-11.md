# Journal des 01 et 02/11 : ce que la porteuse a tranché

Séance de reprise sur le canevas de travail « ficolia - prototype_vTravail » (https://claude.ai/artifact/FB6cC6xawyir9Y1QwCYosb). Ce journal reprend les choix de la porteuse, avec le commit qui les applique. Les numéros de décision (218 et suivants) restent à attribuer dans la note de reprise : ce journal n'en donne pas.

## Choix appliqués

| Choix | Ses mots | Date | Commit |
| --- | --- | --- | --- |
| Le canevas neuf devient le canevas de travail ; l'ancien reste une archive | « ok maintenant cet artéfact est notre canevas de travail » | 01/11 | `e70aa19`, `e50b70a` |
| Planches non reprises : les 8 anciennes de l'étape 1, et Main, A à D | « non on ne les reprend pas » | 01/11 | — |
| Cases de la ligne allaitement en largeur partagée par défaut | (31/10) | 01/11 | `217fea9` |
| L'idée 5 « à plat » sur les 10 listes d'ingrédients vivantes | « parfait » | 01/11 | `6caac47` |
| « Réessayer » ramène à l'écran d'où l'on vient ; « Accès à la caméra » marqué comme action du téléphone | « ok » | 01/11 | `f77b5fa` |
| Bandeau grisé avec son motif quand le verdict n'est pas établi | « reporter dans un bandeau grisée "évaluation incomplète" et si il y a d'autres types d'évaluation partielle inscrire le bon motif » | 01/11 | `478bd19` |
| Décision 217 appliquée : la ligne allaitement dans le parcours principal (étapes 1, 2, 5), recherche comprise | « go », puis « ok » | 01/11 | `092aafd` |
| Écart minimal de 24 px avant « Ce n'est pas ce produit » ; l'arc dans Fondations et Polices | « go » | 01/11 | `79a1011`, `8e237e3` |
| L'ouverture et l'accueil en deux écrans (4 planches) | « 1et 2 OK » | 02/11 | `47089e6` |
| Écrans produit défilants en texte agrandi, barre d'onglets fixe en bas (`T-220`) | « oui traite le », puis « 1et 2 OK » | 02/11 | `0cfec0c` |
| Renvoi « Crevasses » : **première lecture** (voir ci-dessous) | « ok » | 02/11 | aucun : c'est le comportement du prototype |
| Troisième voie du savon publiée, pour le test hors cible (voir ci-dessous) | « ok » | 02/11 | `4259d83`, `78a5c92` |

Modification faite par la porteuse sur la page, rapatriée (R3) : la page « Étape 1 — sans animation » s'appelle « Étape 1 » (`37a99a1`, 02/11).

## Le renvoi « Crevasses » : première lecture

Le renvoi s'affiche sur un soin des mamelons (produit à l'attribut) qui n'est pas vert, dont l'évaluation est incomplète, ou qui porte une mention (`D-214`, étape 7). Une condition compte comme une mention (décision 170). Un soin des mamelons vert et parfumé reçoit donc le renvoi, parce que le parfum est une condition.

- C'est le seul cas où les deux lectures divergent. L'autre lecture s'appuie sur `D-272` (l'élément ② n'est pas une mention) ; elle n'aurait pas montré le renvoi sur ce produit.
- `O-65`, cité par la proposition PR-1.5, n'est pas dans le registre v6.7 du dépôt : le fichier du 30/10 reste introuvable. À relire quand il revient.
- À tracer au registre, dans la discussion de méthodologie.

## La troisième voie du savon (PR-1.6)

**Publié le 02/11** (versions 30 et 31 du canevas) :
- `E6-Fiche-ToiletteSeins` (nouvelle planche, étape 6, troisième rangée) : la phrase de la condition savon validée le 17/10, « Selon les recommandations professionnelles, la douche habituelle suffit : nettoyer les mamelons avant ou après une tétée complique inutilement l'allaitement. », source « ANAES, 2002 · [référence à vérifier] », le rappel général et des sections à rédiger. Texte provisoire, pour le test hors cible.
- `EA-Verdict-Gel` : un nettoyant **vert ou jaune** renvoie à cette fiche, sous la même forme que le renvoi « Crevasses » (le petit rond sur la photo par défaut). Jamais sur « Évaluation incomplète », ni sur l'orange ou le rouge. Le renvoi « Crevasses » est inchangé ; les deux ne se rencontrent pas, un nettoyant n'ayant pas l'attribut.

**Sur quels produits** :
- *Dans l'application* : les nettoyants de la condition savon (`D-262` ; `D-266`, groupe 12). Ce sont le gel douche, le savon solide corps, le produit moussant pour le bain, le gommage corps et le savon liquide. Leur sont rattachés : le savon liquide pour le corps et l'huile de douche, ainsi que le produit 2 en 1 cheveux et corps (`T-495`), qui vont au gel douche ; les sels et huiles de bain, qui vont au produit moussant ; le savon solide pour les mains, qui va au savon solide corps. Exclus : le lavant intime, les nettoyants et gommages visage, l'eau micellaire, les démaquillants, le shampoing et les lingettes nettoyantes corps.
- *Dans le prototype* : un seul produit porte ce profil, le « Gel douche surgras » de l'étude de la ligne allaitement. Seule la planche `EA-Verdict-Gel` montre donc le renvoi. Le parcours principal (le lait corps) ne le montre jamais.

**Limites, à ne pas perdre de vue** :
- **Tension avec la décision 168**, maintenue par la 183. Le 17/10, la porteuse a écrit que la condition savon « n'a rien à faire ici […] meme pas en pop up ». Un lien sur le verdict revient en partie sur ce choix. Son « ok » du 02/11 porte sur la publication pour le test hors cible, et la 168 n'est pas annulée pour autant. À trancher après le test.
- **Écart au registre** : `D-262`, `D-265` et `D-266` gardent la condition savon sur le verdict, alors que le prototype l'a remplacée par un lien vers une fiche. À réviser dans la discussion de méthodologie, avec `T-605`.
- **Le lien ne vit que sur `EA-Verdict-Gel`.** Les autres planches du même gabarit (`EA-Verdict-Gel-Source`, `EA-Verdict-Lait-*`, `EA-Verdict-Baume-*`, `E*-Allaitement`…) n'ont pas reçu la logique. Si l'on y choisit « Gel douche surgras » dans les réglages, le renvoi n'y paraît pas. Rien de faux ne s'affiche, mais c'est incomplet. À étendre si le test le retient.
- **La fiche ne s'ouvre pas depuis le menu.** Dans « Bonnes pratiques par thème », la ligne « Toilette des seins » existe, marquée « à écrire », mais ce n'est pas un lien. La flèche de retour de la fiche ramène pourtant à cette liste. Faut-il faire de cette ligne un lien ? Question posée à la porteuse.
- **Source à vérifier** : l'ANAES 2002 est ancienne, sans grade et au conditionnel (`L-77`). Il faut vérifier, avant toute publication publique, qu'aucun texte plus récent de la HAS ne la remplace (`T-606`, `T-581`).
- **Le texte final** revient au toxicologue et à la porteuse.

## Contrôle R3 du 02/11 : ce qu'il vérifie, et ce qu'il ne vérifie pas

La liste des fichiers du canevas donne leurs tailles, pas leurs empreintes. Les 190 planches ont été comparées **par la taille** (après réécriture des ressources en `/_blob/`). L'index `canvas.json` a été **lu en entier** puis comparé par son contenu.

Une modification de même longueur, par exemple un mot remplacé par un autre de même taille, échapperait à une comparaison par la taille. Avant de remplacer une planche, il vaut mieux lire sa version en ligne (empreinte sha256) que se fier à la taille. Ce n'a pas été fait le 02/11 pour `EA-Verdict-Gel`, dont seule la taille a été comparée avant la publication de la version 30.
