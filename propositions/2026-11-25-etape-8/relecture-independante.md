# Relecture indépendante du relevé des décisions 218 à 286 (étape 8) — 25/11

Ficolia · prototype · document interne · relecture : rien n'est modifié, rien n'est inscrit

**Ce que c'est.** La relecture critique de `propositions/2026-11-25-etape-8/releve-218-286.md` (« le relevé »), faite sans connaître le raisonnement de son auteur. Chaque affirmation vérifiée l'a été à la source : le tableau du §2 bis de « Ficolia — note de reprise, complément du 31-10.md » (« la source »), le journal `propositions/2026-11-02-voie-savon/journal-01-02-11.md`, le registre v7.0 (`mamaCARE_Registre_Projet_20_11_26_v7-0 (1).md`, lu entrée par entrée, par recherche de mots et d'identifiants), le registre v6.7 et v6.9 du dépôt pour les dates, l'historique git, et le relevé du 31/10 (`propositions/2026-10-31-hors-canevas/ecarts-au-registre-etape-8.md`).

**Gravité.** Bloquant : une affirmation fausse qui changerait une conclusion du relevé. Important : une affirmation fausse ou mal fondée qui change un statut, un « À faire » ou un point soumis à la porteuse. Mineur : une citation inexacte, un oubli ou une imprécision sans effet sur les conclusions.

## Bilan

| Gravité | Nombre |
| --- | --- |
| bloquant | 0 |
| important | 6 |
| mineur | 18 |

Le relevé est solide. Ses 69 lignes couvrent bien toutes les décisions 218 à 286. Ses décomptes sont justes : 16 + 18 + 3 + 32 pour les statuts, 15 + 13 + 12 + 4 + 25 pour les « À faire », et chaque liste correspond aux lignes. Presque toutes ses citations du registre sont exactes au mot près, annotations datées comprises (liste au §5). Les cinq constats sont vrais. Un seul appelle une réserve, celui sur `D-259` (§3). Les six constats importants portent sur la manière de poser quatre des 14 points, sur un statut et sur un point qui manque.

---

## 1. Constats importants

**I1. Décision 268 : « absente » est faux, `D-342` porte déjà la place.**
- Le relevé : « `D-342` : la limite et la version « confiées au prototype » ». Statut : absente ; À faire : inscrire.
- Le registre, `D-342` : « au prototype (planning, PR-3, étapes 5 à 8), la limite déterminante au panneau de détail et la version des règles sur la fiche méthode, après vérification de ce que couvrent déjà C6 et C11 (`D-114` […]) et les écrans d'échec (`T-512`) » ; « un numéro, non une date (`D-52` tient) ».
- La 268 suit donc cette entrée. La version va sur la fiche méthode, en numéro et non en date. La « limite B » est le résultat de la vérification prévue : les textes actuels disent déjà la limite. `T-521` (annotation du 30/10) le dit aussi : « question 3 (l'affichage) tranchée (`D-342`) ».
- Statut juste : déjà inscrite (en partie). À faire : annoter `D-342` avec le résultat (limite B, version A). Le point 11 du §5 reste valable : `D-342` confiait aussi la place de la version aux testeuses.

**I2. Point 1, premier sous-point, et décision 280 : la question sur `D-259` est déjà tranchée.**
- Le relevé : « Laquelle des deux fait foi ? »
- La source (280) : « la case du canevas garde « Dépôt du produit sur la peau de bébé » ; le registre dit « Contact rapproché non évalué ». Écart à tracer à l'étape 8. »
- `prototype/A-FAIRE.md`, l. 26 : « ~~`D-259`~~ : **tranché le 10/11** (décision 280 […]) : la case du canevas reste telle quelle ; l'écart au registre […] est à tracer à l'étape 8 ».
- La porteuse a donc tranché le 10/11, en sachant ce que dit le registre. Ce qui reste à faire, c'est réviser `D-259` dans la discussion de méthodologie. Il n'y a pas à lui reposer la question.
- Le constat « deux décisions contraires » est vrai dans les faits. Mais la seconde décision remplace la première, elle ne la contredit pas.

**I3. Point 4 et décision 227 : le relevé tait que la porteuse a déjà retenu la règle du canevas.**
- `O-65` : « (choix de Claude du 15/10, tranché par la porteuse le 17/10 : décision du canevas, à inscrire à l'étape 8, `D-223`) ».
- Le relevé cite `O-65`, mais pas ce passage, et présente au point 4 le choix entre la règle du canevas et la lettre du registre comme ouvert.
- Ce choix est fait depuis le 17/10, et la 227 (02/11) l'applique. Ce qui reste à faire, c'est réviser `D-214` (étape 7) et le cas 2 de `T-593`, et fermer `O-65`, dans la discussion de méthodologie.

**I4. Point 10 : sa prémisse n'est pas établie.**
- Le relevé : « la piste (a), qui suggère le type d'après le nom au scan ».
- Rien ne le dit dans les sources :
  - la piste (a) est « type suggéré, à confirmer : « Ce produit est-il un lait corps ? Oui / Choisir un autre type » » (« Ficolia — note de reprise.md », §4.1, question 6) ;
  - le scan simulé de la 232 dit « Produit reconnu, type suggéré (piste a) » ;
  - la règle de la 184 fait du nom un contrôle, non la source de la suggestion : « jamais un type suggéré moins exposant que ce que dit le nom (`D-49`) » ;
  - `D-49` : « vérifier que son nom ne contient pas » les mots surveillés.
- Dans la 272, le type était suggéré d'après le nom tapé par l'utilisatrice, pour une liste collée sans produit reconnu. Le motif « rare qu'un nom de produit donne sa catégorie » ne se transpose pas tel quel.
- Le point peut rester, posé comme une question à vérifier : d'où vient le type suggéré en piste (a) ? Il ne doit pas affirmer que la suggestion vient du nom.

**I5. Il manque un point au §5 : les trois adaptations de `L-147` pour la décision 269.**
- La source (269) : « le texte du registre du 02/11, adapté pour un texte public (« la femme tient » → « celle du produit en main », `D-114` C1 ; « sans que l'écran du produit le signale » et « La part des produits concernés n'est pas mesurée » retirés) ; […] les trois adaptations sont à valider ».
- Le relevé les range en « annoter `L-147` » dans le tableau, sans les soumettre à la porteuse.
- L'une d'elles touche le cœur de `D-353`, qui écrit : « l'utilisatrice la plus exposée […] ne reçoit aucun signal sur l'écran du produit : c'est le prix de la règle simple ». Retirer « sans que l'écran du produit le signale » du texte public efface cette limite. Il ne la reformule pas.
- `T-493` met aussi en garde contre un texte des CGU qui ferait office de clause d'exonération (art. R. 212-1), question posée aux avocats (annotation du 10/11). `prototype/A-FAIRE.md`, l. 27, range aussi « le texte de la présomption européenne (269) » parmi les sujets à réunir pour la juriste.
- À ajouter au §5 : valider les trois adaptations, ou garder la phrase sur l'écran du produit.

**I6. Point 7 et décision 259 : `O-27` est fermé, et sa « piste » n'a pas été reprise telle quelle.**
- Le relevé cite `O-27` (« orientation permise dans le support et les fiches par sujet ») comme une règle en vigueur, et en tire la question : l'écran « Réaction » entre-t-il dans « le support » ?
- `O-27` : « ⚠ **29/09** : **fermé** — `D-114` (C8), sous réserve de la juriste ». Le texte de C8 ne reprend pas l'orientation « dans le support et les fiches par sujet ». Il dit « à quatre endroits — onboarding, « À propos » et fiche méthode, CGU, description des stores — jamais sur l'écran produit ni de verdict ».
- La question devient donc : C8, qui a fermé `O-27`, admet-il l'orientation dans le support ? Ou l'écran « Réaction » est-il un cinquième endroit, quoi qu'il en soit ?
- Le relevé du 31/10 (§8, décision 203) s'appuyait déjà sur `O-27` de la même façon : la réserve vaut pour lui aussi.
- Nouveau au v7.0 : `O-27`, annoté le 17/11, envoie la question du rappel à l'avocat (question 1.3 du dossier v4, phase 1). Le point 7 peut renvoyer à cette question.

---

## 2. Constats mineurs

| # | Ligne ou point | Constat | Preuve |
| --- | --- | --- | --- |
| M1 | 235 | Citation inexacte. Le relevé fait dire à `D-473` : « l'étape 8 du prototype n'est pas encore faite ». | `D-473` : « 4. l'étape 8 n'est pas encore faite, quel est le risque qu'il reste en dehors ? » (mots de la porteuse) |
| M2 | 237 | « `T-636` et `T-558`, annotés le 02/11, mot pour mot » : vrai pour `T-636`, pas pour `T-558`, qui reformule. | `T-558` : « police du logo au lancement : une police gratuite à trouver ; 29LT Riwaya Informal, sous licence, gardée pour le prototype » |
| M3 | §4, décompte | La 248 est comptée parmi les trois « écarts de fait », alors que sa ligne dit « écart », sans « (de fait) ». | Tableau §1, ligne 248 |
| M4 | 251 | « Le retrait […] est confirmé le 03/11 (journal : « on laisse ») » : le journal rapporte une lecture de Claude, que le relevé ne signale pas. | Journal, l. 84 : « « on laisse » (réponse aux deux questions ; lecture de Claude) » |
| M5 | 257, point 2 | Deux entrées de plus portent l'item du signal poitrine à l'onboarding : à annoter avec `D-273`. | `T-394` (close), annotation du 15/10 : « signal poitrine replacé : un item de la rubrique « ce que fait l'application, ce qu'elle ne sait pas faire » de l'onboarding » ; `O-53` (même renvoi) |
| M6 | 234 | Le registre note déjà la tension entre un écran avant la caméra et le prototype : à citer avec `O-71`. | `T-7`, annotation : « un écran maison avant la caméra contredirait le choix « B » du prototype » ; puis « le libellé « choix « B » », qui désigne la décision 52 du prototype » |
| M7 | 270, point 6 | « que `T-638` pose déjà à l'avocat pour le savon » : `T-638` vise la juriste et dit la question « pas encore posée ». La question générale est à l'avocat par `O-52`. Le relevé omet aussi que `D-274` borne `T-117` à la fiche produit. | `T-638` : « reste ouverte la question à la juriste […], pas encore posée » ; `O-52`, 17/11 : « question 3.9 du dossier v4 (« Notre règle contre l'appel à l'action et sa dérogation ») » ; `D-274` : « « faites-vous accompagner » y est admis (`T-117` vise la fiche produit) » |
| M8 | Point 1, deuxième sous-point | « bébé » sans article ne reste pas seulement dans les cases 4 et 5 : l'explication 5, gardée par la 265, l'emploie aussi. | Source, 263 : (5) « Ce verdict ne tient pas compte du produit déposé sur la peau de bébé. » ; 265 : « la 5 telle quelle » |
| M9 | 254 | Rapprochement forcé avec `L-142`, dont la crainte est autre : que le refus se lise comme rassurant, non qu'il se confonde avec l'évaluation incomplète. | `L-142` : « si la phrase du refus ne se lit pas comme rassurante, sans tomber dans l'alerte » |
| M10 | 267 | La source relève un écart que le relevé ne reprend pas : « **écart à la règle de l'écran produit dépouillé** (dossier §3.1, brief §4) » ; et « les verdicts eux-mêmes ne portent pas la mention ». `D-367` couvre la place, mais le registre traite ailleurs une exception de ce genre comme temporaire, à valider au test. | `D-282` : « exception temporaire au dépouillement du dossier de conception, §3.1, jusqu'à l'ouverture, à valider au test » |
| M11 | 228 et 256 | L'écart levé (« à `D-262`, `D-265`, `D-266` ») est dit pour la 228. La 256 le note aussi, et il est levé de même. | Source, 256 : « écart à `D-262`, `D-265`, `D-266` (`T-605`) » |
| M12 | Point 1, troisième sous-point | `D-261` décrit lui-même le mécanisme comme un risque : à citer. Le point reste juste : le texte public doit s'en tenir au fait établi, faute de recommandation P1 à P3. | `D-261` : « couvre M14 (un parfum près de l'aréole peut masquer l'odeur du sein qui guide le nouveau-né) » ; « sinon énoncé du mécanisme limité au fait établi » |
| M13 | Point 1, en tête | « Soit on les révise d'après la 265, soit on revient aux textes du registre » : le registre dit ses propres textes provisoires, ce qui affaiblit la seconde branche. | `D-256` : « formes à éprouver au test de formulation (`D-159`) ; textes finaux rédigés par la porteuse (`T-604`) » ; `T-604` : « Rédiger […] les textes finaux des éléments — la porteuse, quand elle le souhaite » |
| M14 | 248, point 13 | La 248 touche aussi le commentaire resté ouvert de l'ancien canevas, que `D-352` signale : le relevé ne parle que de la question du tiers. | `D-352`, 03/11 : « reste ouvert le commentaire sur les phrases allaitement et grossesse » |
| M15 | 265 | Une question de la source n'est pas reprise : l'accord grammatical des cases. Elle est hors registre, mais attend une réponse. | Source, 265 : « accord à relire : « Application… » et « Inhalation… » sont au féminin, l'état « pas pris en compte » reste invariable comme une étiquette » |
| M16 | 226 | « déjà inscrite » est généreux : `T-559` exige un verdict lisible en texte agrandi, il ne dit rien du défilement ni de la barre d'onglets fixe. Mieux : annoter `T-559` avec la solution retenue. | `T-559` : « le cadre de verdict doit rester lisible quand l'utilisatrice grossit le texte » |
| M17 | 269 | « absente » discutable : `D-353` donne déjà le choix entre les deux supports ; la 269 tranche à l'intérieur de ce choix. Statut plus juste : déjà inscrite (le principe), comme la 254. | `D-353` : « va dans les CGU ou la fiche méthode » ; `T-493` : « support à trancher » |
| M18 | 234, §5 | La tension avec `O-71` (option A, un écran avant la demande de la caméra) est dans le tableau, mais pas au §5. Or `O-71` attend une décision de la porteuse. | `O-71` : « qui tranche : la porteuse » ; cap §2 : « Rien ne s'intercale entre l'acceptation et le premier scan » |

---

## 3. Les cinq constats demandés

| Constat du relevé | Verdict | Preuve |
| --- | --- | --- |
| L'écart au registre du savon, que note la 228, est levé depuis le v6.9 | **vrai** (le même constat vaut pour la 256, M11) | Les annotations du 30/10 et du 02/11 sont au v6.9 (02/11), absentes du v6.7 (22/10), qui était le registre du dépôt quand la 228 a été écrite : `D-262` (« retiré du verdict » ; « son périmètre […] est repris tel quel pour le renvoi ») ; `D-265` (« rang 3 : le parfum seul ») ; `D-266` (« le groupe (12) […] n'a plus aucun élément ») ; `T-605` (« la condition savon devient le texte de la fiche « Toilette des seins » ») ; `L-77` et `T-581` (« l'ANAES 2002 fonde désormais la fiche ») |
| 236 à 238 sont déjà au registre | **vrai** (réserve M2 sur « mot pour mot ») | `T-636`, 02/11 : « tenue du slogan à 2 s ; police du logo : « 29LT Riwaya Informal, sous licence, gardée pour le prototype ; une police gratuite à trouver pour le lancement » » ; `T-558`, 02/11 ; `L-146`, 02/11 : « question close par la porteuse » |
| `O-65` existe au v7.0 | **vrai** | Absent du v6.7 du dépôt (0 occurrence), présent au v6.9 et au v7.0 (l. 2138), avec son annotation du 02/11 : « son contenu n'est pas transmis ici » |
| Deux décisions contraires sur `D-259` | **vrai dans les faits, mal posé** (I2) | `D-259`, 30/10 : « libellé « Contact rapproché non évalué » confirmé par la porteuse le 30/10 (19 h 57 : « 2. oui je confirme ») » ; puis la 280 (10/11), tranchée en sachant ce que dit le registre (`A-FAIRE.md`, l. 26) |
| Les dates du gel douche : la coche de PR-1.8 précède sa construction | **vrai** | `D-354`, 03/11 : « qui l'a prototypé et quand (au plus tard le 03/11 à 0 h 07, heure de la coche de PR-1.8) » ; construit le 04/11 : source (266, date 04/11, version 98), journal l. 100, commit `656b1c5` (04/11, 23 h 01, « Gel douche dans le parcours principal […] (D-354, décision 266) ») |

---

## 4. Les 14 points soumis à la porteuse

| Point | Réel ? | Remarque |
| --- | --- | --- |
| 1 | oui, avec réserves | Premier sous-point déjà tranché (I2) ; « bébé » aussi dans l'explication 5 (M8) ; `D-261` M14 (M12) ; textes du registre provisoires (M13) |
| 2 | oui | `D-273`, `D-114` (annotation du 15/10), `T-605` vérifiés ; ajouter `T-394` et `O-53` (M5) |
| 3 | oui | `D-114` (C7) cité mot pour mot ; déjà au relevé du 31/10, §2 (vérifié) |
| 4 | oui, mal posé | Le choix est fait depuis le 17/10 (I3) ; reste à réviser `D-214` et `T-593` |
| 5 | oui | `D-344` (« proposé quand la recherche par nom ne trouve pas le produit » ; « rien de conservé »), `D-437` (3) et l'annotation du 11/11 de `D-344` vérifiés |
| 6 | oui | `D-274`, `D-66` (15/10), `D-282`, `T-117` vérifiés ; à corriger sur `T-638` et l'avocat (M7) |
| 7 | oui, mal fondé en partie | `O-27` est fermé par C8 (I6) |
| 8 | oui | `D-368` (« s'en servir pour chercher un produit par son nom reste à l'étude ») et `T-555` (10/11) vérifiés |
| 9 | oui | `D-410` (« option formulée sous condition »), `O-86` (« points 5 à 10 non ouverts au 19/11 »), `O-87` vérifiés |
| 10 | prémisse non établie | I4 |
| 11 | oui | `D-342` : « le prototype et les testeuses décident de sa place » ; « puis test avec la cible (PR-4) ». Mais la place sur la fiche méthode était déjà au registre (I1) |
| 12 | oui, mineur | `D-363` dit la défense éditoriale à l'échelle de l'application (`T-173`), pas forcément dans cette mention : la proposition « ajouter « en France » » est une lecture |
| 13 | oui | `D-312`, 03/11 : « encore ouverte le 12/11 » ; inventaire du 02/11 confirmé par `lecture-conception.md`, l. 84 ; voir aussi M14 |
| 14 | oui | `O-73` (1) : « les mentions « la juriste » ; les références internes », et « dresse une liste de tous ces écarts je corrigerai le prototype » |

**Ce qui manque :**
- les trois adaptations de `L-147` (269), à valider (I5) ;
- l'option A d'`O-71` (234), à trancher par la porteuse (M18) ;
- au besoin, la tension avec la décision 168 : la source de la 228 dit « à trancher après le test », et la 256 revient en partie sur elle avant. Le relevé la note au §4. Elle n'est pas au §5, ce qui se défend : la décision attend le test hors cible.

---

## 5. Vérifié sans écart

**Citations du registre, exactes au mot près :**
- les annotations datées : `D-352` ; `D-312` (« remplacée », 02/11 ; « encore ouverte le 12/11 », 03/11) ; `D-265` (02/11) ; `D-339` (02/11) ; `T-638` (« validation confirmée par la porteuse le 02/11 » ; la forme du test hors cible, 02/11) ; `D-223` (03/11) ; `O-60` (« l'arc sans aiguille (décision 213, 30/10 ; reste sa taille) ») ; `D-259` (30/10) ; `D-354` (03/11) ; `O-86` (19/11) ; `D-344` (11/11) ;
- les entrées de la ligne allaitement et de l'onboarding : `D-112` (A1, A7, A8 ; aucune annotation après le 15/10) ; `D-114` (C7, C8 et l'annotation du 15/10) ; `D-214` (étape 7) ; `D-256` ; `D-257` ; `D-258` ; `D-260` (libellé) ; `D-261` (« au fait établi ») ; `D-268` ; `D-270` ; `D-272` ; `D-275` ; `D-273` ; `T-605` ;
- les autres : `T-442` ; `D-282` ; `D-103` ; `D-347` ; `D-363` ; `D-367` ; `D-437` (3) et (5) ; `D-438` (l'interrupteur, « sans « anonymes » ») ; `D-369` ; `O-73` (1) et (2) ; `O-108` (Q6) ; `D-19` ; `T-146` ; `O-107` ; `O-71` ; `T-232` ; `T-404` ; `T-117`.

**Sens prêté aux identifiants (§6 du relevé) :**
- `T-232` porte bien sur les « Contraintes iOS » ;
- `D-206` porte bien les niveaux de NB_nourrisson ; le risque de dénigrement passe par `C-154`, `T-470`, `D-255` et l'additif (A1, A12, cités par `T-639`) ;
- aucune occurrence de « figue », « prise en main », « tutoriel » ni « bulle » (au sens de l'interface) au v7.0.

**Le reste :**
- `E5-Reglages` nomme bien, pour une erreur, « la version du système et le modèle du téléphone », comme `D-439` (TE28-D10).
- Le v6.9 est entré dans le dépôt le 04/11 (commit `e3d47f9`), le v7.0 le 21/11 (`4eaca75`).
- Les résumés de la colonne « Ce qu'elle décide » sont fidèles à la source pour les 69 décisions. Seules omissions : la suppression d'`E3-SansVerdict-Source` (281), le bouton « Effacer » (251) et les points relevés en M10 et M15.
- La consigne d'aveugle est respectée : hors parfum, le relevé ne nomme que des types de produits et des éléments de la ligne (« savon », « gel douche », « lait corps »), aucun ingrédient.

---

## 6. Limites de cette relecture

- Le registre n'a pas été lu en entier. Les recherches de mots ont couvert les sujets du relevé, plus « caméra », « symbole », « logotype », « onboarding », « réévalué », « dénigrement », « bleu », « dépouillé », « Message envoyé », « Toilette des seins » et les textes nouveaux des planches. Une entrée formulée autrement a pu échapper.
- Les planches du canevas n'ont pas été relues. Seule `E5-Reglages` a été ouverte, dans le dépôt.
- Les lectures I3, I4 et I6 sont les miennes : la porteuse ne les a pas vues.
