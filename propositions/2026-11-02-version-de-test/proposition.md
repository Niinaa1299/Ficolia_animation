# La version de test du prototype : proposition du 02/11 (rien n'est construit)

Pour le test hors cible (`PR-2`, protocole du 20/10 : cinq personnes hors cible, aucune donnée de santé, tâches et critères fixés d'avance). Tâche 2.8 de `prototype/A-FAIRE.md`.

## Ce que la porteuse a demandé (02/11)

- « j'avais imaginé un lien à envoyer avec le prototype comme s'ils avaient téléchargé l'application. navigation libre + menu ou on peut séléctionner des chemins critiques qu'on veut tester absolument. »
- « non pas un artéfact à part, une page hmtl plein écran c'est possible ? + possibilité de mettre des commentaires »
- Le menu des chemins est visible des testeurs : « oui ».
- La liste des chemins : « je réflechis ».
- Recrutement : « C'est fait : 2 hommes, 3 femmes hors cible » (`PR-2.2`).

## Ce que Claude propose

- **Une page web plein écran, publiée sur claude.ai.** Ce n'est pas un canevas : pas de planches ni d'outils, seulement l'application. Sur un téléphone, elle occupe tout l'écran. Sur claude.ai, toute page publiée par Claude s'appelle un « artefact » : c'est le sens du mot dans la proposition du 02/11, qui a prêté à confusion.
- **Construite par un script à partir des sources du dépôt** (`prototype/sources/project/`) : le script copie les planches, masque les étiquettes de prototype et écrit la page d'accueil avec le menu. Après chaque changement de planche, on relance le script, et la version de test suit. Le canevas de travail n'est pas touché.
- **Le départ** (proposition, à confirmer) : le premier lancement (l'ouverture, puis l'accueil), comme si l'application venait d'être téléchargée ; puis navigation libre par les liens entre écrans.
- **Le menu « Parcours »**, visible des testeurs : un bouton discret, toujours au même endroit, qui lance les chemins critiques.
- **Les commentaires** : sur chaque écran, un bouton « Commenter cet écran » ouvre la boîte de commentaires de claude.ai. Le commentaire est rattaché à l'écran affiché. Claude les lit ensuite (outil `ArtifactComments`) et en fait la synthèse écran par écran.
- **Les étiquettes de prototype masquées** : « Texte provisoire », « [Prototype : … ] ». 169 planches sur 191 ont déjà un réglage « Statuts des textes » qui les masque. 93 planches contiennent des mentions « [Prototype : … ] », dont une partie n'est pas couverte par ce réglage ; certaines servent à naviguer (scans simulés) et devront être remplacées par le menu.

## Chemins critiques proposés (provisoires, la porteuse choisit)

1. Le premier lancement : ouverture, accueil, conditions, demande de caméra.
2. Scanner un produit évalué (le lait corps) : écran produit, verdict grossesse, ingrédients.
3. La ligne allaitement du même produit : verdict, cases « À savoir », explications.
4. Un soin des mamelons : le renvoi « Crevasses ».
5. Un gel douche : le lien vers « Toilette des seins ».
6. Une recherche par nom, puis une recherche sans résultat.
7. Un produit inconnu : la figue, puis la contribution photo.
8. Sans connexion : un verdict gardé, puis un verdict à actualiser.
9. Un produit réévalué, depuis l'historique.
10. Signaler une erreur.

## Ce qui a été vérifié, et comment le faire

- **Le moteur des planches tourne hors du canevas.** `outils/runtime/support.js` charge React et Babel depuis `cdn.jsdelivr.net` s'ils manquent, service autorisé pour les pages publiées. Le rendu local (`outils/rendre.mjs`) le fait déjà. À confirmer sur un premier essai publié.
- **Les commentaires** : la capacité `comments` déclarée en `{"composer_only": true}` ouvre la boîte de commentaires de claude.ai sans demander de consentement, et la page reste partageable. La forme complète, `{}`, rend la page interne à l'organisation : à éviter. Le bouton doit s'ancrer sur un élément qui porte le nom de l'écran affiché, pour savoir de quel écran parle chaque commentaire.
- **Les images et les vidéos** se publient comme fichiers de la page. Ne pas employer la capacité `assets`, qui rend la page interne à l'organisation. Les adresses `/_blob/` du canevas ne valent que pour le canevas.
- **Le partage** se règle depuis le menu « Partager » de la page, en lecture seule (aucun droit d'écriture hors de l'organisation, R4). **Non vérifié** : si un lien peut s'ouvrir et permettre de commenter sans compte claude.ai. À voir sur une première version privée. Repli : la porteuse note les remarques pendant la séance.

## Limites

- Un vrai scan est impossible : chaque chemin choisit le produit « scanné ».
- Chaque planche garde son propre état : les états (sans connexion, réévalué…) ne se déclenchent pas seuls, on y entre par le menu.
- Les vidéos alourdissent le premier chargement.
- La version ne sera prête pour les tests qu'avec les phrases sous le verdict (`CT-1`, tâches 2.1 à 2.6) et les mentions reformulées (tâche 2.5a).

## Étapes, après l'accord de la porteuse

1. Écrire le script d'assemblage (dans `outils/`), d'abord avec les chemins provisoires.
2. Publier une première version **privée** ; vérifier le moteur, les liens, les vidéos et le bouton de commentaire.
3. Montrer des captures à la porteuse (R6).
4. Remplacer les chemins par les siens ; refaire après les phrases (`CT-1`) et les mentions.
5. La porteuse règle le partage et envoie le lien.
