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

« Palette Ficolia — contrôle-html.zip » (racine du dépôt, déposé le 01/11 ; une seule planche, `D-Accent.dc.html`) : « Garde là dans le dépot mais ne l'affiche pas sur l'artefact » (02/11). Il reste dans le dépôt, hors de `prototype/sources/`, et n'est pas publié sur le canevas.

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
- **La fiche s'ouvre aussi depuis le menu** (porteuse, 02/11 : « OUI », à « J'en fais un lien ? »). Dans « Bonnes pratiques par thème », la ligne « Toilette des seins » était marquée « à écrire » sans être un lien ; elle mène désormais à la fiche, comme « Crevasses ». La fiche reste un texte provisoire, et c'est la fiche elle-même qui le dit.
- **Source à vérifier** : l'ANAES 2002 est ancienne, sans grade et au conditionnel (`L-77`). Il faut vérifier, avant toute publication publique, qu'aucun texte plus récent de la HAS ne la remplace (`T-606`, `T-581`).
- **Le texte final** revient au toxicologue et à la porteuse.

## 02/11, fin de matinée

Les commits `23c0a20` et `a3c25f0` sont datés à tort « 03/11 » dans leur message : c'était le 02/11.

| Choix | Ses mots | Commit |
| --- | --- | --- |
| Piste (a) de la question du type reliée (décision 184) : 12 scanners (résultat simulé « Produit reconnu, type suggéré (piste a) ») et 5 écrans de recherche (lien de prototype sous celui de l'option (b)) ; l'option (b) reste | « ok pour tout » | `23c0a20` |
| « Mettre à jour » mène à « Après la mise à jour », pour le prototype ; la note dit que le vrai bouton ouvre le magasin d'applications | « ok pour tout » | `23c0a20` |
| « Accepter » (ouverture et accueil, 4 planches) mène à la demande de caméra (`T-232`) | « ok pour tout » | `23c0a20` |
| Étape 8 : lancée dès que le registre v6.9 est dans le dépôt | « on le lance des que le regstre v6.9 est dans le dépot » | — |
| Tenue du slogan : **2 s**, validée (« 3s c'est trop long ») ; la porteuse a changé le réglage par défaut de `E1-Ouverture-Arbre` sur la page, rapatrié dans le dépôt (R3). Les trois autres planches au même réglage (`-Reduit`, `E1-Accueil-Bienvenue`, `-Conditions`) restent à 3 s : question posée. Règle la question 10 du 31/10 et le fil `778d3ee5` de l'ancien canevas | « slogan 2s c'est validé, 3s c'est trop long. changement fait manuellemnt » (commentaire sur la page, 02/11) | voir le commit de ce rapatriement |
| Police du logo : 29LT Riwaya Informal, sous licence ; gardée pour le prototype ; une police gratuite à trouver pour le lancement. Complète `T-636` et `T-558` (à inscrire). Aucun fichier de la police dans le dépôt ni sur le canevas (vérifié) | « la police est sous-licence : 29lt riwaya informal / Pour l'instant sur le prototype on garde celle-ci, mais je vais devoir en chercher une gratuite. » (fil `0940e8c9`) | — |
| Mentions de la ligne allaitement et leurs explications à reformuler : propositions dans les fils (deux pistes pour les cases, explications nouvelles), choix attendu ; rien n'est posé | « Toutes les mentions sont à reformuler car elles ne sont toujours pas clair pour un user tiers. » ; « Les explications aux mentions sont aussi à reformuler car pas comprise du premier coup par un user tiers. » (fils `111f9ffa`, `8b340b1d`) | — |
| « Rechercher · aucun résultat » : la figue de l'état « produit inconnu » (la cagette vide, image fixe validée le 12/10) en filigrane sous le message, décorative, sans animation ; réglage « ton chaud » (par défaut), « couleurs atténuées », « aucun » ; seule `E2-Recherche-Aucun` (version 37) | « image en arrière plan en filigrane de la figue : soit celle décidée en image fixe de la figue qui n'a pas trouvé le produit ou (en attendant) le logo en filigrane » (fil `99641baa`) | `f8ffb55` |
| Verdict « à actualiser » : « les données » expliqué (le verdict enregistré sur le téléphone, `D-91`, `T-511`), deux formulations proposées ; choix attendu | « "Les données" c'est à dire ? la liste INCI ou les études scientifique ? » (fil `a5b20715`) | — |
| Encadré « réévalué » : durée non fixée au registre (`D-282`) ; trois possibilités proposées, la première recommandée ; choix attendu | « Durée d'afficage de cet encadré ? apparaît seulement une fois à la première consultation ? » (fil `19560b13`) | — |
| Dépôt public et données de la personne extérieure : sans objet, la porteuse a eu l'autorisation | « on s'en fiche. j'ai eu l'autorisation. » | — |
| Forme du test hors cible : un lien à envoyer, le prototype comme une application téléchargée, navigation libre et un menu des chemins critiques à tester | « j'avais imaginé un lien à envoyer avec le prototype comme s'ils avaient téléchargé l'application. navigation libre + menu ou on peut séléctionner des chemins critiques qu'on veut tester absolument. » | — |
| Recrutement du test hors cible fait : cinq personnes, 2 hommes et 3 femmes (`PR-2.2`) | « C'est fait : 2 hommes, 3 femmes hors cible » | — |
| Version de test : une page HTML plein écran, avec la possibilité de laisser des commentaires ; le menu des chemins critiques est visible des testeurs ; la liste des chemins est en réflexion | « non pas un artéfact à part, une page hmtl plein écran c'est possible ? + possibilité de mettre des commentaires » ; « oui » (menu visible) ; « je réflechis » (chemins) | — |
| La porteuse vérifie elle-même que les commentaires de l'ancien canevas sont tous traités | « je dois aussi vérifier les commentaires sur l'original si tout a été traité » | — |

**Limites** :
- Dans la recherche, la piste (a) ne paraît que si le réglage « catalogue » est sur « … option (b) » : c'est ce réglage qui montre les produits reconnus avec la question du type. Le nom du réglage ne le dit pas.
- Les 3 planches marquées « À SUPPRIMER » (`E3-Scan-Avant`, `E6-APropos`, `E6-BonnesPratiques`) restent : leur suppression attend un accord explicite.
- Contrôle des liens du 02/11 : il lit les liens écrits dans les sources. Il ne dit pas si un retour mène au bon écran.

## Contrôle R3 du 02/11 : ce qu'il vérifie, et ce qu'il ne vérifie pas

La liste des fichiers du canevas donne leurs tailles, pas leurs empreintes. Les 190 planches ont été comparées **par la taille** (après réécriture des ressources en `/_blob/`). L'index `canvas.json` a été **lu en entier** puis comparé par son contenu.

Une modification de même longueur, par exemple un mot remplacé par un autre de même taille, échapperait à une comparaison par la taille. Avant de remplacer une planche, il vaut mieux lire sa version en ligne (empreinte sha256) que se fier à la taille. Ce n'a pas été fait le 02/11 pour `EA-Verdict-Gel`, dont seule la taille a été comparée avant la publication de la version 30.
