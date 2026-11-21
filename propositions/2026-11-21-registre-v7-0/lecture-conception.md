# Registre v7.0 (20/11) : ce qui touche à la conception et au prototype

Lecture du 21/11/2026, faite par Claude Code à la demande de la porteuse (« lis le attentivement afin de voir tout ce qui touche au design/prototypage/conception »). Ce document ne décide rien. Pour chaque point, il dit ce que le registre décide ou laisse ouvert, ce que le prototype montre aujourd'hui (vérifié sur les sources du dépôt, identiques au canevas le 21/11) et qui tranche.

## 0. Méthode et limites

**Source.** `mamaCARE_Registre_Projet_20_11_26_v7-0 (1).md`, sur `main` (commit `45df40c`, 21/11), 2 396 lignes, 1 515 395 octets, SHA-256 `12797ccd32df6bc1…`. Copié tel quel dans la branche de travail, comme le v6.9 le 04/11.

**Méthode.**
1. Comparaison entrée par entrée avec le v6.9 : 311 entrées nouvelles (`D-358` à `D-475`, `C-321` à `C-419`, `L-151` à `L-201`, `O-71` à `O-109`, `T-643` à `T-646`) et 203 entrées annotées. Ces chiffres sont ceux de l'en-tête du v7.0. Une seule ligne disparaît : un doublon de `T-507`, close, dans une liste de fin de registre.
2. Lecture des titres des 311 entrées nouvelles et du début du texte ajouté aux 203 entrées annotées.
3. Recherche de mots (prototype, canevas, maquette, écran, planche, libellé, phrase, bouton, volet, panneau, accueil, logo, nom, marque, couleur, police, historique, signalement, « Nous écrire », photo, conditions d'utilisation, mention, alerte, réglages, affichage, vignette, verdict…) dans tout le texte nouveau ou ajouté.
4. Lecture intégrale des entrées retenues : 57 entrées nouvelles, le texte ajouté de 56 entrées annotées, puis huit entrées que la recherche de mots a fait remonter (`D-369`, `O-90`, `L-187`, `D-382`, `D-384`, `D-431`, et des extraits de `C-390`, `C-139` et `D-378`).
5. Vérification, sur les planches, de chaque point qui touche le prototype.

**Limites.**
- Les entrées inchangées depuis le v6.9 n'ont pas été relues : ce qu'elles disent de la conception était déjà la base du prototype.
- Le tri par titres a pu laisser passer un détail de conception logé dans une entrée d'un autre sujet. La recherche de mots dans tout le texte nouveau réduit ce risque sans l'annuler.
- Les sources que le registre cite n'ont pas été lues : le dossier v4 des avocats, le document des stores, les fichiers de TE-2.7 et de TE-2.8. Elles sont à l'archive.
- La liste des écarts du prototype remise le 11/11 (`O-73`) n'est pas dans le registre (« texte non repris ; d'après le résumé de la conversation »). Deux de ses points ne peuvent pas être rattachés à une planche sans elle ou sans le dossier v4 (§1, point 5).
- Le registre ne contient pas les décisions du prototype au-delà de celles de la note du 14/10 : l'étape 8 n'est pas faite (`D-223`, `D-473`). Il ne connaît donc ni les décisions 218 à 283 ni l'idée de la porteuse du 19/11 (supprimer la phrase sous le badge).

## 1. Ce qui change pour le prototype

| # | Sujet | Ce que dit le registre | État du prototype (21/11) | Qui tranche |
| --- | --- | --- | --- | --- |
| 1 | **Rappel d'un lot** | Décision de conception (`D-367`, porteuse, 11/11) : le rappel d'un lot et les versions multiples vont sur l'écran du produit ; l'évaluation incomplète et les données anciennes, sur l'écran du verdict. Écart du prototype à corriger (`O-73`). | **Écart confirmé.** La planche « Écran produit · rappel de lot » (`E3-Produit-Rappel`) n'affiche aucun rappel ; le message « Un rappel officiel concerne certains lots de ce produit. » n'est que sur le verdict grossesse (`E3-Verdict-Rappel`). La liste du 11/11 cite aussi « le rappel sur le verdict allaitement » : à préciser (§1, point 5). | porteuse (le rappel quitte-t-il le verdict ?) |
| 2 | Versions multiples, évaluation incomplète, données anciennes | même décision (`D-367`) | Conformes : `E3-Produit-AutreVersion` (écran produit) ; `E3-Verdict-Incomplet` et `E3-Verdict-Actualiser` (verdict). | — |
| 3 | **« La juriste » devient « l'avocat »** | La juriste ne répond plus ; deux avocats consultés (`D-364`) ; choix de l'avocat le week-end du 21-22/11 (`D-469`) ; les mentions « la juriste » sont un écart du prototype (`O-73`) ; les tâches JU sont réécrites sans la juriste (`O-107`). | Le mot est dans une centaine de planches, en partie dans du texte visible : « [durée à fixer avec la juriste] » (« Nous écrire », signalements, photos) ; « texte en attente de la juriste et de la toxicologue » (catégories protectrices, crevasses) ; « à relire par la juriste » (conditions, confidentialité). | porteuse (le mot à mettre, une fois l'avocat choisi) |
| 4 | **Qui relit les textes de l'application ?** | « la relecture des textes en phase 2, comprise dans aucune des deux offres » (`O-107`, JU-8) ; les phrases du niveau 4 sont relues par l'avocat retenu (`T-604`). | Tous les textes marqués « à relire par la juriste » n'ont pour l'instant plus de relecteur prévu. | porteuse |
| 5 | Les autres écarts de la liste du 11/11 | (`O-73`, point 1) « le second paragraphe des conditions d'utilisation ; le panneau ouvert de l'écran E3.3 ; les références internes ». La numérotation (E3.3, E5.10) est celle du dossier v4. | **Références internes** : « Formes à éprouver (D-159) », note de statut affichée sur 22 verdicts allaitement ; le réglage des statuts peut la masquer pour des captures. **Second paragraphe des conditions et écran E3.3** : non identifiables sans la liste ou le dossier v4. | porteuse (me donner la liste, ou m'autoriser à lire le dossier v4 à l'archive) |
| 6 | **Interrupteur des compteurs** | Troisième ligne de « Réglages », qui coupe le comptage et l'envoi ; actif par défaut sous réserve des avocats ; libellé sans « anonymes » tant que l'adresse IP n'est pas tranchée ; « à inscrire aux éléments qui restent à prototyper » (`D-438`, `D-114`) ; le rapport d'erreur est coupé par le même interrupteur (`D-439`). | **Absent.** « Réglages » (`E5-Reglages`) n'a que l'historique et la caméra. | porteuse (libellé), avocats (état par défaut) |
| 7 | « Message envoyé » | Un écran « Message envoyé » qui rappelle l'adresse saisie, parmi les restes de TE-2.8 (`O-96`, « prototype ») ; les signalements ne portent aucune adresse (`D-441`). | `E6-Ecrire-Envoye` dit « Ficolia vous répondra par e-mail. », sans l'adresse. Les signalements ne demandent pas d'adresse : conforme. | porteuse |
| 8 | **Volet de première alerte** | La porteuse, le 11/11 : il « n'est pas prototypé encore c'est normal » ; sa question part aux avocats « une fois l'écran prototypé » (`D-369`, `O-73`, `O-108`). | Le prototype a un volet qui s'ouvre de lui-même une fois, au premier verdict de niveau 3 ou 4, et que le « i » rouvre (`E1-Verdict` et ses copies) ; ses textes des niveaux 2 à 4 sont à écrire avec la toxicologue. Ce qui manque pour le dire « prototypé » est à préciser. | porteuse |
| 9 | Écran du coffret | Coffret : « pas encore évalué » refusé ; le verdict de chaque produit du coffret, option à confirmer à TE-2.8, « à prototyper si option choisie » (`D-410`, `O-86` point 10, `O-87`). | Absent ; pas encore à faire. | porteuse, à TE-2.8 |
| 10 | Écran d'information caméra, sur Android | Option A proposée par Claude : un écran d'information propre à Android, juste avant la première demande (`O-71`) ; l'avertissement que prévoyait la porteuse « était juste pour Android » (`C-322`). | La décision 52 du prototype (07/10) a supprimé tout écran avant la demande de la caméra, d'après les règles d'Apple. L'option A y reviendrait pour Android seulement. | porteuse (PU-1.2) |
| 11 | Zone d'application non relevée ; précaution imprimée | L'affichage « Zone de tétée non évaluée » pour tout « non relevé » est retiré (`D-416`) ; l'affichage quand la zone n'est pas relevée reste à trancher (`O-86`, point 7) ; l'effet d'une précaution du fabricant (par exemple, jamais de vert) est pour plus tard, aux avocats et au toxicologue (`O-87`). | Rien à changer pour l'instant. | porteuse, à TE-2.8 |
| 12 | Recherche par nom sans connexion | Le catalogue embarqué sert aussi en ligne ; s'en servir pour chercher par nom « reste à l'étude » (`D-368`) ; proposition sans objection : « recherche par nom sur le téléphone, avec le catalogue embarqué » (`T-555`, 10/11). | Si elle est retenue, le message « Pas de connexion » de `E2-Recherche-HorsLigne` et `E5-Recherche-HorsLigne` ne vaudrait plus que pour les produits absents du catalogue. | à surveiller |
| 13 | Liste collée | La liste lue en photo est fermée ; le copier-coller reste, sa forme restant une proposition ; inclusion au lancement à CA-6.2 (`D-413`, `D-344`). | `E2-Liste-Coller` est cohérent : « Coller » est un geste de l'utilisatrice, « La liste n'est pas conservée. ». | CA-6.2 |
| 14 | Formules multiples d'un même code | `O-68`, `D-361` et `D-362` ne valent que pour la base ouverte, sans effet au lancement si `T-517` n'en retient pas les verdicts ; « relevée pour le marché français » se lit « relevée en France » (`D-363`). | `E3-Produit-AutreVersion` (`D-347`) reste juste. | — |

## 2. Le nom, le logo et l'animation

- **Ficolia devient un nom de travail** (`D-366`, porteuse, 10/11) : « il est très probable que le nom change encore ». Deux noms d'une lettre d'écart relevés à l'INPI ; noms de domaine et comptes suspendus (`D-390`, `T-463`, `D-330`) ; dépôt de la marque après le choix du nom définitif et l'avis de l'avocat retenu (`O-107`).
- **Le logo et l'animation d'ouverture** sont une question posée aux avocats, en phase 1 (7.26 du dossier v4, `T-636`). Les polices n'y sont pas : une police gratuite reste à trouver pour le lancement (`T-558`).
- **Poids du nom dans le prototype** : 299 occurrences de « Ficolia » dans le texte visible de 82 planches. Le logo, la révélation, l'accroche, « Bienvenue sur Ficolia » et les vidéos exportées portent le lettrage.
- **Proposition de Claude** : ne plus rien investir dans ce qui dépend du nom (lettrage, logo, animations du nom) avant son choix. Les textes se remplacent en une passe, et les exports ont déjà leurs textes posés à part. La révélation du logo et ses vidéos seraient à refaire. Le symbole de la figue tient-il sans le nom ? Question à te poser le moment venu.

## 3. Les textes, désormais chez l'avocat

Questions du dossier v4 qui toucheront des textes ou des écrans du prototype. La phase 1 est prévue « idéalement d'ici début décembre 2026 » (`D-369`).

| Question du dossier v4 | Phase | Registre |
| --- | --- | --- |
| Où placer le rappel de consulter un professionnel de santé (1.3) | 1 | `O-27` |
| Notre règle contre l'appel à l'action et sa dérogation (3.9) | 1 | `O-52` |
| Le libellé « Composition incompatible » (2.3) | 1 | `O-22` |
| Le logo et l'animation d'ouverture (7.26) | 1 | `T-636` |
| Prouver l'acceptation des conditions | 1 | `T-557` |
| Les compteurs sans identifiant | 1 | `D-415` |
| Une précaution imprimée par le fabricant | 2 | `D-369`, `O-87` |
| Les dates affichées (1.15) | 2 | `O-21` |
| Un message de détresse (4.22) | 2 | `T-404` |
| Une huile essentielle pure, dans une version ultérieure (2.16) | 2 | `T-416` |
| Deux formules connues pour un même code-barres (2.10) | — | `O-67` |
| Le choix d'un nouveau nom (7.25) | 2 | `D-366` |

Aussi au dossier : ce que Ficolia présume des produits, le rappel officiel d'un lot, la liste collée, la fiche « Crevasses » ouverte depuis un produit nommé, le site web de la structure, le libellé du niveau 4 sur un produit conforme (`D-365`).

**Retirée du dossier** : « Les affirmations sur la méthode à borner » (`D-369`, `T-534`). Le texte « Qui évalue » de la page « À propos et méthode » (décision 281, laissé à rédiger) n'a donc pour l'instant ni règle ni relecteur.

## 4. Les phrases sous le verdict

- `O-74` (05/11) attend **huit** décisions : (1) deux phrases pour le NB 1 sous le seuil ; (2) l'ordre quand deux causes fixent le même niveau ; (3) le vocabulaire du bébé ; (4) garder « interdit en cosmétique » ; (5) pas de phrase pour le plafond de `D-213` ; (6) tracer les deux écarts de règle ; (7) « signalé par précaution » pour le NB 2 ; (8) une phrase pour le NB 4 sans base officielle.
- **Erreur de Claude Code, à corriger ici** : le 10/11, j'ai reposé six choix d'après la v2 de CT-1.1 (les six de CT-1.2 v1). Je n'avais pas les points 7 et 8, posés le 05/11 dans la conversation de CT-1.
- Le 19/11, la porteuse a proposé de supprimer la phrase sous le badge et de mettre l'explication ailleurs, puis a mis la question de côté (« je trancherai plus tard »). Le registre ne le sait pas.
- Le commentaire « à reprendre car pas clair d'après un user externe » de l'ancien canevas est rattaché à `T-609` et `T-604` (validé le 20/11).

## 5. Pour les tests et l'étape 8

- **Tests du prototype** (`D-378`) : si la part des jaunes dus au seul NB_nourrisson égal à 1 dépasse le seuil pré-enregistré, « le risque de renoncement au soin est examiné aux tests du prototype (M18) ». À reprendre dans la préparation des tests (`A-FAIRE` 2.10).
- **Étape 8** (`D-223`, `D-473`) : les décisions du prototype au-delà de la note du 14/10 restent hors du registre, ainsi que le fichier du bloc G. Le relevé des écarts (`A-FAIRE` 4.1) se fera contre le v7.0. Le registre note ce qu'il ignore et que le journal du prototype sait :
  - par où le gel douche entre dans le parcours, la couleur de son verdict, qui l'a prototypé et quand (`D-354`) ;
  - le sort d'une question d'un tiers du 17/10 sur l'ancien canevas (`D-312`). L'inventaire du 02/11 compte quatre fils de la personne extérieure le 17/10, tous traités par les décisions 214 à 216.
- **Archive et contrôles** : tout document qui passe dans les conversations du projet va aussi à l'archive (`D-382`). Un texte qui nomme des ingrédients et entre au projet passe par le contrôle de R1 de la porteuse : lancé sans `--noms`, sortie jamais collée, seul retour « contrôle fait » (`D-472`, `D-475`, `D-431`). Les documents du dépôt du prototype nomment des ingrédients (exemples des planches, inventaire CT-1.1). À appliquer s'ils passent au projet.

## 6. Pour plus tard (V2 et au-delà)

- Une deuxième version « pourrait proposer d'autres produits mieux notés » ; « Elle ne propose ni conseil ni alternative. » est retiré du dossier (`D-369`). Android d'abord, iOS peu après.
- Deux contenances d'un même produit : une seule formule au lancement, les distinguer en V2 (`D-409`).
- Les règles de `O-68` pour la base ouverte (`D-361` à `D-363`).
