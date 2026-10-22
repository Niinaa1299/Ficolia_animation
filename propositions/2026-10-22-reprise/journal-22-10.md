# Prototype Ficolia — séance du 22/10/2026

Branche `claude/relaxed-noether-g2fdj1`, partie de `main` (5fd02f2). Le registre v6.7 (`main`) fait foi. Le travail précédent est sur `claude/ecstatic-lamport-qjpucd` (non modifiée) ; les animations sont sur `claude/compassionate-shannon-qu70ot` (non modifiée).

## 1. Relecture, avant toute modification

- **Accès** : le compte de cette session est propriétaire du canevas (https://claude.ai/artifact/EuTtpHhP8LubH91j4wpsVw). Il peut publier, répondre aux fils envoyés à Claude et les clore, avec l'approbation de la porteuse.
- **Version en ligne** : 1792536570-62b1, celle que décrit la note de reprise du 21/10. 12 pages, 193 planches, 70 notes, 7 planches « À SUPPRIMER », ouverture sur « Ligne allaitement (étude) » : conformes au §1 de la note.
- **Note de reprise sur `main`** (`Ficolia — note de reprise.md`) : même contenu que celle de la branche précédente ; seules la mise en forme, le sommaire et les échappements diffèrent.
- **Fils de commentaires** : voir `fils-ouverts.md`, dans ce dossier.

## 2. Copie complète du canevas (avant la première modification)

- Version 1792536570-62b1 : 194 fichiers `project/` (index et 193 planches) et les 49 fichiers de la réserve (39 appelés par les planches, 10 que rien n'appelle), vérifiés contre les empreintes du service ; manifeste sha256 et LISEZ-MOI.
- Archive `copie-canevas-2026-10-22-v1792536570-62b1.tar.gz` (15,6 Mo, sha256 `d7d612864883d6f471ab938c517be8ac7a01325fd7018a298c706ec3eaff7f44`), remise à la porteuse, qui la garde en local. Le Drive n'a pas pu servir : l'outil exige le contenu entier dans l'appel, trop gros pour 15,6 Mo.
- Ni les commentaires ni l'historique des versions ne sont dans la copie. Elle n'est pas versée au dépôt (public).

## 3. Registre v6.7 et canevas : écarts relevés

La note du 21/10 était écrite d'après la v6.5. Lecture ciblée des entrées qui touchent les écrans, pas du registre entier.

1. **`D-104`, phrase 2 du volet grossesse** (modifiée le 22/10, à titre provisoire : « … un signal modéré pour la grossesse. ») : l'ancienne phrase est sur 24 planches de verdict, le lexique et deux planches de l'étape 0. **Non reportée** (porteuse, 22/10 : « les phrases ne sont pas arrêtées même cette nouvelle phrase est provisoire » ; `T-609`).
2. **Textes de la ligne allaitement validés le 20/10** (`D-256` à `D-260`, `D-275`, `D-161`) : absents de l'étude du 17/10. **Alignés le 22/10** (§4).
3. **Savon** : `D-262` garde l'élément ⑥ (vert et jaune ; revue du 19/10, « ok » le 20/10) ; la décision 168 (17/10) l'a retiré du verdict. Conflit soumis à la porteuse (22/10).
4. **`D-273` contre `cap-onboarding.md` §2** : le registre garde la rubrique de l'onboarding où `D-273` place le signal poitrine ; l'accueil en deux écrans du 17/10 n'y est pas tracé. En attente de la décision de la porteuse ; l'accueil du canevas n'est pas touché.
5. `D-280` : accord exprès de la porteuse le 21/10 (« Soin des mamelons » dans la question du type) ; ferme la décision 47.

## 4. Publication du 22/10 : version 344 (1792666413-082a)

Demande : « 4. Oui » (aligner l'étude sur le registre, étiquette « Contact rapproché » comprise).

- **Planches** : les 17 verdicts et les 5 listes d'ingrédients de l'étude allaitement ; le lexique (`E6-Methode-Lexique`, groupe allaitement). **Index** : titre de `EA-Ingredients-Spray-Mention` (« la mention « contact rapproché » … ») ; un paragraphe daté du 22/10 ajouté à la note « formesEA » de la page allaitement (les textes du 17/10 qu'elle consigne restent).
- **Textes** (registre, 20/10) : ① « Zone de tétée non évaluée : cette évaluation ne tient pas compte d'une application sur le mamelon ou l'aréole. » ; ② « Zone de tétée évaluée : cette évaluation tient compte du produit présent au moment de la tétée. », et « Zone de tétée : évaluation incomplète. Au moins un ingrédient n'a pas pu être évalué pour cette zone. » ; ③ « Contact rapproché non évalué : cette évaluation ne tient pas compte du contact de la peau du nourrisson avec la peau traitée. » ; ④ « Inhalation par le nourrisson non évaluée : cette évaluation ne tient pas compte de l'inhalation du produit par le nourrisson. »
- **Conséquences visibles** : la zone de tétée non évaluée garde son explication sur l'orange et le rouge (`D-257` : « sur toutes les couleurs ») ; les pastilles portent l'étiquette entière (`D-256` : « un seul texte par élément, le même partout ») : « Inhalation par le nourrisson non évaluée » y passe sur deux lignes en taille standard, et décale la suite d'environ 16 px.
- **Pas touché** : la condition parfum (le registre ne fixe pas son texte), le savon (§3, point 3), les phrases des niveaux, les planches de l'étape 0 et de traçabilité.
- **Contrôles** : script qui part des fichiers relus en ligne et ne remplace un texte que s'il apparaît une fois ; familles alignées avant et après (17 verdicts, 5 listes) ; `renderVals()` exécuté 3 928 812 fois (produit complet des réglages qui changent les éléments, les autres un par un, six états internes) : aucune erreur, aucun ancien texte ; mots interdits (`textes.md` §2) : aucun dans les nouveaux textes ; couleurs inchangées ; rendu local avec la police réelle, avant et après, comparé au pixel (seules les zones attendues changent) ; avant publication, les 24 fichiers en ligne identiques à la copie ; après, identiques à l'envoi.
- **Limites** : le rendu local n'est pas le canevas ; le mode Play n'a pas été essayé ; le texte agrandi n'a été regardé que sur le spray à 200 %.

## 5. Fils clos le 22/10

`38898d40`, `218d65e2`, `eda3a66e` (accord de la porteuse : « 6. Ok »). Reste 34 fils ouverts.

## 6. Liste de fin de session (branche précédente) : points touchés

- Point 13 (ligne allaitement) : les textes du 17/10 sont remplacés par ceux du registre (§4) ; l'étiquette « Contact peau à peau » n'est plus sur le canevas.
- Point 22 (lexique) : groupe allaitement aligné sur les textes du registre.
- « Fils à clore » : trois clos (§5).
- Point 10 et fils ouverts : liste à jour dans `fils-ouverts.md`, attribution corrigée.

## 7. En attente de la porteuse

- Savon : `D-262` ou décision 168 (§3, point 3).
- `D-273` contre `cap-onboarding.md` §2.
- Plan d'action de l'audit du 18/10 et questions du §4.1 de la note : présentés le 22/10.
