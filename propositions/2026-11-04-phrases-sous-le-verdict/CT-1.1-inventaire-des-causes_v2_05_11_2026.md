# CT-1.1 — Inventaire des causes du niveau, par ligne, avec les chemins du moteur — version 2

Planning, chantier `CT-1` (« Phrases sous le verdict »), tâche `CT-1.1` (Claude). **Version 2 du 05/11/2026**, faite à la demande de la porteuse (05/11, 0 h 15 : « produis que celui ci pour l'instant », en réponse à « je produis CT-1.1 v2 »). Elle remplace la version 1 du 04/11 (`CT-1.1-inventaire-des-causes.md`).

**Sources** :
- le registre v6.9 (`mamaCARE_Registre_Projet_02_11_26_v6-9 (1).md`, 02/11) ;
- le dossier des règles de la note grossesse v0.1 (`claude/Ficolia_Dossier_Regles_NB_Grossesse_v0-1_28_10_2026.md`). Il réunit chaque règle du NB avec son statut. La porteuse l'a accepté le 28/10 comme base de travail ; le toxicologue ne l'a pas validé (`T-534`) ;
- le compte rendu de l'appel du 22/10, avec les réponses écrites du toxicologue du 26/10 (`claude/Ficolia_CR_Appel_Toxicologue_22_10_2026.md`).

Il prépare `CT-1.2`, la tâche de la porteuse (`CT-1.2-preparation.md`, version 1, à mettre à jour après ses décisions).

Ce document ne décide rien. Pour chaque niveau de chaque ligne, il dit ce qui peut produire ce niveau (les « chemins »). Il vérifie aussi si les phrases candidates de la session du 24 au 27/10 sont vraies sur tout leur chemin : `T-609` pour la grossesse, `T-604` pour l'allaitement. C'est la règle de `D-104` : chaque phrase est vraie pour tous les chemins de son niveau ; depuis `D-302`, on écrit une phrase par cause.

**Repères** :
- G désigne la ligne grossesse, A la ligne allaitement. Les codes de la v1 sont gardés, sauf G4a', redéfini. Les chemins nouveaux prennent une lettre de plus (G4d, G4e, A4d, A4e).
- C1, N1, R4… sont des règles du dossier des règles, et non des entrées du registre. Exception de lecture : dans `D-197` et `D-213`, « P5 » désigne un niveau de preuve (une convention déclarée), et non la règle P5 du dossier (le doute entre 1 et 2).
- Rien n'est inscrit au registre. Les corrections de l'annexe A sont des propositions pour la prochaine génération.

## Ce qui change depuis la version 1

La v1 contenait huit erreurs, toutes de Claude. Les sept premières ont été relevées dans la nuit du 04 au 05/11 (détail et typologies proposées : annexe A) :
1. Quatre bases du §2 reprenaient des valeurs que les arbitrages 19 et 20 ont remplacées : H361f non harmonisée → 1 ; H361d non harmonisée → 2 ; notification isolée → 2 au plus ; H360F harmonisée → 3.
2. « H340, H350, harmonisées ou non » → 4 : seules les classifications harmonisées valent 4 (dossier, C8 ; compte rendu, question 13 ; le registre, `D-306` et `D-315`, ne porte pas le mot). Le chemin G4a' de la v1 n'existe pas ; il est redéfini (§3).
3. Le motif du parfum n'est pas « composition non déclarée », mais celui de l'arbitrage 18.
4. Le bain de bouche n'a pas de plancher : il atteint le niveau 2 par le calcul. À NB 1, la v1 ne le rangeait dans aucun chemin ; il relève de G1a'.
5. Des bases manquaient, dont des chemins du niveau 4 : R6, R8, H1, le rétinol.
6. Les candidates allaitement étaient jugées sur les bases de la grossesse.
7. G3a et A2c étaient dites vraies. Elles sont fausses pour un nanomatériau noté 2.

S'y ajoutent :
- une correction d'un message de Claude (annexe A, point 8) ;
- la huitième erreur de la v1, reprise dans la première remise de cette v2 : le classeur des paramètres donné pour absent du projet (annexe A, point 9) ;
- les erreurs de la première remise que deux relectures indépendantes du 05/11 ont relevées (annexe A, point 10 ; annexe B, relectures 3 et 4). Les principales : G1b, A1b et A1c sont désormais dites fausses sur une partie de leur chemin, G3b fragile ; deux chemins sont ajoutés (le rincé sans aucune note, en G1a ; A4e). Les écarts mineurs sont en fin d'annexe A.

## 0. Ce que vaut cet inventaire (limites, à lire d'abord)

1. **Les facteurs d'exposition sont recalculés sur le classeur.** L'onglet « Paramètres » de `mamaCARE_Benchmark_Calibration_INCI.xlsx` est au projet. C'est la copie du 26/10, figée au tirage du 28/10 (160 209 octets, SHA-256 `d6caa172…` ; `D-317`, `L-132`). Elle donne les seuils, le plancher, et la SED, la DAp et le statut rincé de 76 catégories, dont 56 non rincées. La SED de l'une d'elles, le soin intime sans rinçage, est vide (« à obtenir du toxicologue ») : elle est hors calcul, et ce que le moteur en fait n'est pas lisible. Chaque facteur `DAp × SED_cat / SED_ref` des 75 autres a été recalculé le 05/11 ; tous concordent avec les valeurs du registre. Une réserve : `T-337` (« 5 rincées sur 20 » au-dessus de 0,034) ne se retrouve qu'en calculant sans la DAp. Le registre emploie donc deux définitions du facteur, ce que `T-336` relevait déjà pour le chapitre 3 du périmètre. Exactement 9 catégories atteignent 0,5 à NB 1 : lait corps 0,50 ; après-solaire 0,57 ; spray solaire visage 0,60 ; jambes lourdes 0,75 ; déodorant spray 0,76 ; spray solaire corps 0,9998 ; solaire corps 1,22 ; amincissant 1,46 ; anti-vergetures 1,99. Ces valeurs sont celles de la grossesse ; en allaitement, seul l'anti-vergetures change (DAp 50 %, `D-229`). **Limite** : le code du moteur n'est pas au projet. Ce qu'il fait des paramètres (ordre des étapes, arrondis) est reconstitué à partir du registre (`D-50`, `D-214`, `D-234`, `D-277`, `D-289`), non lu.
2. **Les chemins sont provisoires.** Ils dépendent :
   - de règles jamais validées par le toxicologue : plancher gradué, rincés sans plancher, NB 4 absolu sur les rincés (`T-380`) ;
   - de la DAp de l'anti-vergetures (`L-13`) ;
   - des réponses attendues à ②-A et aux points et questions 21, 22 et 27 à 32, envoyés le 28/10 (`D-318`) ;
   - du prompt allaitement, qui n'existe pas encore (`D-222`).
3. **Les bases.** Celles de la grossesse viennent du dossier des règles v0.1, avec le statut que le dossier donne à chacune ; c'est une consolidation de Claude, relue par Claude seul. Celles de l'allaitement ne sont fixées qu'en principe (`D-197`, `D-222`). La vérité des candidates allaitement est jugée sur ces principes, sous réserve des règles que le prompt allaitement écrira. En attendant, la valeur d'attente est la copie de la grossesse (`D-222`, point 4). Sur cette copie, plusieurs candidates allaitement deviennent fausses (§4, §6).
4. **Hors de cet inventaire** :
   - l'état « Évaluation incomplète », qui n'est pas un niveau (`D-275`) ;
   - le flacon d'huile essentielle pure, qui reçoit au lancement un écran de refus (`D-338`) ;
   - les produits hors champ : médicament, dispositif médical, produit pour bébé, tous refusés (`D-214`, étape 0).
5. **Ce qui est vérifié ici** : la vérité des phrases sur leurs chemins, rien d'autre. Leur compréhension relève du test hors cible. Leur fond relève du toxicologue (J3) et, pour le niveau 4, de la juriste.
6. **Deux renvois de la v1, l'un invérifiable, l'autre relocalisé** :
   - la décision 264 du prototype (le mot « bébé ») : introuvable dans l'historique consultable ;
   - « textes, §1 » : introuvable. La règle visée est au §4.4 du dossier de conception du 30/09 (`Ficolia_Dossier_de_conception_30_09_2026.md`).
7. **Noms d'ingrédients** : seulement ceux que la v1 ou le dossier des règles nomment déjà. Les notes fixées viennent de sa section 9, dont les ingrédients sont sortis des candidats de R1 et R2. Ce fichier n'est ni un texte de règle ni un texte destiné au toxicologue ; `r1_controle.py` n'y a pas été passé.

## 1. Le moteur, en bref

**Le calcul** (`D-214`, étape 4 ; `D-50`) : `NM = NB × DAp × SED_cat / SED_ref`. Les seuils se lisent « supérieur ou égal » : 0,5 donne le niveau 2, 2 le niveau 3, 5 le niveau 4. La catégorie de référence est le lait corps, de DAp 0,5 : à NB 1, il donne exactement 0,50, donc le niveau 2. C'est l'étalonnage du modèle, non un effet de bord (`D-50`).

**L'exposition.** Le facteur `DAp × SED_cat / SED_ref` ne porte que sur le produit : **le moteur ne connaît aucune concentration d'ingrédient**. Une phrase qui affirme une quantité d'ingrédient (« apporte peu », « en dépose beaucoup ») affirme donc ce que le moteur ne calcule pas.
- **Sprays** :
  - leur DAp est de 100 % (dossier, P3 et N7, d'après la réponse 2.1 du brief 2B ; classeur). La voie inhalatoire n'est pas modélisée pour autant : le verdict de ces catégories est partiel (`L-40` ; note du classeur) ;
  - la SED du déodorant spray est la quantité sortie du flacon, dépôt cutané et part inhalée compris. Les fractions cutanées de pire cas sont de 23,5 % pour les sprays à base d'éthanol et de 11,4 % pour les autres (`D-234`). Celle du spray solaire corps est une valeur propre au format (`T-595`).
- **Anti-vergetures** : DAp de 100 % en grossesse, par précaution et sans donnée (`L-13`, `D-228`) ; 50 % en allaitement (`D-229`).
- **Le rincé n'ordonne pas l'exposition.** Le bain de bouche a un facteur supérieur à celui de 43 des 55 catégories non rincées calculables. Ce qui sépare les deux régimes, c'est le plancher, « règle de danger et non d’exposition » (`T-338`). Son facteur est 0,2641 (classeur : SED 32,54, DAp 100 %), le plus haut des rincés (`T-337`) ; le suivant, le savon liquide, est à 0,034.

**Les garde-fous**, qui court-circuitent le calcul :
- **Plancher gradué, produits non rincés seulement** : un NB 2 donne au moins le niveau 2, un NB 3 au moins le niveau 3 (`C-307`, `T-380`).
- **Produits rincés : aucun plancher** (option B, `T-380` ; `C-307`). Le bain de bouche n'y fait pas exception. Il atteint le niveau 2 **par le calcul**, à NB 2 (0,53) et à NB 3 (0,79) (`D-277`). C'est ainsi que Claude lit « seul rincé hors classe majoritaire » (`T-450`). À NB 1, il reste au niveau 1 (0,26, calcul).
- **NB 4 → niveau 4**, partout, rincés compris (« une interdiction ne se dilue pas », `C-307`).

**En allaitement, deux routes** (`D-214`, étapes 4 et 5) :
- **La route du lait** : le même calcul, avec NB_allaitement et les DAp de l'allaitement, et les mêmes planchers.
- **La route de la bouche** (zone de tétée) :
  - elle ne vaut que pour les produits à l'attribut, qui sont tous des non-rincés (`D-186`) ;
  - la note NB_nourrisson la plus haute donne directement le niveau : 0, rien ; 1 ou 2, au moins le niveau 2 ; 3, au moins le niveau 3 ; 4, le niveau 4 (`D-207`, `D-212`, `D-214`) ;
  - un ingrédient « Non évalué » ou en « Données insuffisantes » met la zone de tétée en évaluation incomplète (`D-215`). Le parfum sans décision explicite du toxicologue aussi (`D-276`) ;
  - cette route n'est évaluée qu'après l'attribution manuelle de NB_nourrisson et le succès de la strate des soins des mamelons et des ancres (`VERROU-3`, `D-245`).
- **Le niveau affiché** est le plus haut établi entre les deux routes. L'évaluation incomplète ne s'affiche seule que si rien n'est établi au-dessus du vert ; sinon, elle devient une mention (`D-147` ; `D-214`, étape 8).
- **Chemin provisoire** (`D-213`) : un ingrédient noté 4 en grossesse pour une contre-indication propre à la grossesse, pas encore noté pour l'allaitement, y compte comme un 3. C'est une convention déclarée (« convention (P5) »), sans fondement propre à l'allaitement. Elle n'atteint aucune utilisatrice, NB_allaitement devant être validé avant la publication (`VERROU-1`, `D-245`).
- **Règle encore ouverte** (`D-214`, étape 4 ; `T-283`) : un ingrédient sans NB_allaitement suit la règle de la grossesse.

**Le niveau du produit** est celui de l'ingrédient le plus préoccupant, sans somme (dossier, P9).

**Une seule phrase par verdict.** Quand deux causes fixent le même niveau (deux ingrédients, ou les deux routes), aucune règle ne dit laquelle donne la phrase. `D-278` marque les deux ingrédients.

## 2. Ce qui fonde une note (les « bases »)

### 2.1 Grossesse

Lecture du dossier des règles v0.1, sections 1 à 9. Les statuts du dossier, entre parenthèses quand ils ne sont pas « Écrit » :
- **Écrit** : règle confirmée par écrit par le toxicologue ;
- **Arbitrage** : arbitrage de Claude adopté par la porteuse le 27/10, jamais présenté comme validé par lui ;
- **À soumettre** : proposition appliquée à titre provisoire selon la phrase de repli de `D-254`, la forme des envois au toxicologue ;
- **Prompt** : règle qui ne figure que dans le prompt du 13/10.

| NB | Bases |
| --- | --- |
| 0 | cas A : évaluation favorable d'une autorité, sans classification reprotoxique (I2) ; cas B : jamais examiné, sans signal (I3) ; absent des bases ou récent, avec l'état « Données insuffisantes » (I4) ; classifications générales non CMR (C17) ; restriction de l'annexe III motivée par l'environnement, pour ce motif (R9) ; restriction de l'annexe III motivée par un effet local (R9 bis, à soumettre, question 27) ; oxyde de zinc sans exposition pulmonaire, pour ce critère (N4, Arbitrage 23) ; note fixée : caprylyl glycol (section 9) |
| 1 | parfum, Fragrance, Aroma (F1). Motif retenu : celui de l'arbitrage 18, un signal propre aux mélanges parfumants (allergènes possibles sous le seuil d'étiquetage, constituants examinés comme perturbateurs endocriniens). Le motif écrit du toxicologue (« Sa composition exacte n'est pas déclarée ») contredit I3 et n'a pas été repris ; allergènes à étiquetage obligatoire, liste élargie par le règlement 2023/1545 (F2) ; « insufficient data » du CIR ou du SCCS (I5 ; point 21 à soumettre) ; restriction de l'annexe III pour l'étiquetage, la sensibilisation ou une autre population (R9) ; fertilité « suspectée », hors classification (C9) ; perturbateur endocrinien de priorité 3 (E1) ; signal de perturbation endocrinienne d'une seule source internationale (E2) ; étude animale isolée, « à surveiller » (E3) ; activité endocrinienne in vitro (E4) ; conclusion du CIR avec réserves, 1 ou 2 (I7, Prompt) ; huile essentielle à signal faible (H1) ; notes fixées : chlorhexidine ; cétylpyridinium, éthanol en usage buccal, fluorure de sodium (section 9) ; à soumettre : libérateurs de formaldéhyde, au moins 1 (C16, question 29) ; sensibilisation H317 (C17, question 31) |
| 2 | restriction de l'annexe III qui inclut la femme en âge de procréer ou le fœtus (R9) ; perturbateur endocrinien de priorité 2 (E1) ; signal de perturbation endocrinienne de deux sources internationales concordantes (E2) ; deux études animales concordantes, ou une étude multigénérationnelle (E3) ; H361f harmonisée **ou du dossier REACH** (C4, Arbitrage 20) ; fertilité « présumée », hors classification (C9) ; **tout nanomatériau, au moins 2** (N1 ; motif écrit : « l'incertitude elle-même » ; motif à soumettre, question 30) ; dioxyde de titane nano et silice nano hors inhalation (N2, N3 ; point 22 : silice nano à 2 dans toutes les formes) ; **doute entre 1 et 2** (P5) ; conclusion du CIR avec réserves (I7, Prompt) ; huile essentielle à mécanisme ou signal préoccupant documenté (H1) |
| 3 | H360D ou H360F harmonisée admise par dérogation, au moins 3 (C1) ; H360D ou H360F du seul dossier REACH (C2, Arbitrage 20) ; H361d harmonisée **ou du dossier REACH** (C3) ; H341, H351 (C8 ; la lettre ne dit pas si elles doivent être harmonisées) ; fertilité « avérée », hors classification (C9 ; articulation avec C1 et C4 : lecture de Claude) ; perturbateur endocrinien de priorité 1 (E1) ; **« à déconseiller » de l'ANSM** (R4) ; **avis défavorable du SCCS non traduit en règlement, 3 au plus** (I8) ; conclusion « unsafe » du CIR, 3 au plus, après vérification du motif (I6) ; dioxyde de titane nano et silice nano en forme inhalable (N2, N3) ; oxyde de zinc en forme inhalable (N4, Arbitrage 23) ; restriction de l'annexe III pour un danger d'inhalation, en forme inhalable (R9 bis, à soumettre, question 27) ; huile essentielle déconseillée avec un élément toxicologique préoccupant (H1) ; notes fixées : acide salicylique (H361d harmonisée, C3) ; sels d'aluminium (base à vérifier : aucune recommandation de l'ANSM retrouvée, `C-319` ; question 34, `T-642`) |
| 4 | annexe II (R1). Exceptions qui écartent le 4 : une entrée qui prévoit une forme autorisée, comme la vaseline, fait noter la forme autorisée selon les critères habituels (R2) ; un nom de mélange rattaché à une entrée qui vise un seul de ses composants fait noter le mélange conforme (R2 bis, à soumettre, question 32) ; **H360D ou H360F harmonisée sans dérogation**, interdite par l'article 15 (C1, R7 ; H360F : Arbitrage 19) ; **H340 ou H350 harmonisée** (C8 ; aucune clause de dérogation : question 28) ; règlement d'amendement visant explicitement la grossesse (R3) ; contre-indication explicite de l'ANSM pour la grossesse (R4) ; restriction du SCCS traduite en règlement en vigueur, si elle ou l'avis cible explicitement la grossesse (R5 ; un avis non traduit relève d'I8, 3 au plus : lecture de la lettre du dossier, alors que `D-306` peut se lire comme admettant l'avis seul) ; **interdiction nationale formelle d'un État membre pour la grossesse** (R6 ; « formelle » reste à définir) ; **plusieurs sources indépendantes qui convergent vers un danger avéré**, procédure de dérogation (R8) ; **huile essentielle : contre-indication ou restriction majeure documentée par une source de référence** (H1) ; notes fixées : **rétinol** (base en attente : l'analogie avec la contre-indication des rétinoïdes topiques médicamenteux, question J2a de ②-G) ; D4 (annexe II) |

**Règles qui couvrent plusieurs niveaux, ou aucun** :
- une restriction réglementaire sans mention de la grossesse vaut de 1 à 3 selon sa sévérité (R3, R5) ;
- une mention sans lettre (H360, H361) se traite comme une mention D (C5, Arbitrage 20) ; une double mention prend la plus haute des deux notes (C6) ;
- un CMR de catégorie 2 ne passe pas à 4 en début de grossesse (C13) ;
- H362 est sans effet sur la note grossesse (C10) ;
- les impuretés CMR non déclarées dans la liste INCI ne sont pas évaluées (C14).

**Règles ouvertes ou en attente**, qui pourraient créer des chemins (dossier, §11, et lecture de Claude pour la première) : H340 ou H350 du seul dossier REACH : le principe de l'arbitrage 20 (`D-307` : « dossier REACH traité comme une classification harmonisée sans dépasser 3 ») donnerait 3, mais le dossier ne l'a décliné (C2 à C4) que pour H360 et H361, à confirmer (une H340 ou H350 notifiée relève de C7 : pas une base de note) ; combinaison des règles (P4) ; doute hors de la frontière 1/2 (P6) ; maille de la note (P8) ; épidémiologie humaine (E5) ; classification limitée à une voie (C11) ; classes « perturbateur endocrinien » du CLP (C12) ; liste SVHC (C15) ; annexes IV à VI (R10) ; autres nanomatériaux inhalables (N6) ; huiles essentielles (H2 à H4).

**Valeurs remplacées, à ne plus reprendre.** `D-306` lit le tableau du toxicologue « par statut » : H360F harmonisée → 3 ; H361d non harmonisée → 2 ; H361f non harmonisée → 1 ; notification isolée → « écarté ou NB=2 maximum ». `D-306` range lui-même ces valeurs parmi les réponses « contradictoires, précisées ou remplacées » par les arbitrages 19 et 20 (`D-307`). Les règles en vigueur sont C1, C3, C4 et C7 : une notification isolée n'est pas une base de note. `D-306` y range aussi l'échelle de fertilité ; le dossier la garde (C9, statut « Écrit »), mais pour un effet établi **hors classification**, selon la lettre du dossier ; que cela la sépare de C1 et de C4 est une lecture de Claude (C9).

### 2.2 Allaitement (NB_allaitement)

- **Échelle** (`D-197`). Même sens qu'en grossesse, par convention. Niveaux de référence quand une preuve existe :
  - 4 : interdiction, ou contre-indication d'une autorité ;
  - 3 : H362, effet rapporté à imputabilité établie, synthèse qui conclut à éviter ;
  - 2 : synthèse qui conclut à la prudence ; un cas isolé vaut au plus 2.
  Un mécanisme seul est informatif.
- **Prompt allaitement, à construire** (`D-222`) :
  - en l'absence de donnée sur le lait, règle de repli : le danger propre de la substance, jugé sur les critères communs aux deux profils (perturbation endocrinienne, avis du SCCS, toxicité générale, annexe II) ;
  - H360 et H361 servent de signal de relecture, non de note ;
  - aucune règle de départage du doute ;
  - une restriction de l'annexe III est jugée sur sa pertinence pour le nourrisson.
- **Niveau 4** (`D-212`) :
  - l'annexe II vaut 4 sur les trois colonnes, automatiquement, NB_nourrisson compris ; les entrées assorties d'une exception sont laissées au toxicologue ;
  - une contre-indication d'une autorité vaut 4 sur la seule colonne qu'elle vise ;
  - une recommandation de prudence n'est pas une contre-indication.
- **H362** : 3 ou 4, question renvoyée après l'étalon (`T-622`).
- **Valeur d'attente** : la copie de la grossesse, témoin et valeur provisoire tant que le prompt n'est pas validé (`D-222`, point 4), avec le plafond de `D-213`. Selon la même entrée, la copie porte des ancrages étrangers à l'allaitement : H360, H361, règle du doute, restriction de l'annexe III d'une autre portée, contre-indications de grossesse. Et un 0 de la grossesse ne dit rien du nourrisson.

### 2.3 Nourrisson (NB_nourrisson, route de la bouche)

La note est attribuée à la main par le toxicologue, sur fiches sourcées (`D-193`). Niveaux (`D-206`) :
- 0 : aucune préoccupation ;
- 1 : signal faible ou préoccupation dépendante de la dose, avec un motif positif ;
- 2 : préoccupation documentée (toxicité orale pertinente pour le nourrisson) ;
- 3 : action de précaution officielle visant l'ingestion par le nourrisson, ou intoxications pédiatriques graves ;
- 4 : contre-indication officielle par voie orale chez le nourrisson (miel : Anses, 31/10/2023), ou interdiction ;
- « aucune donnée » : pas de note, évaluation incomplète.

L'annexe II y vaut 4 automatiquement (`D-212`). Le cas du miel dépend de la décision AL-3.3 : la règle provisoire quand le danger tient à un fait que l'INCI ne dit pas, comme la stérilisation (règle de Claude dans l'annotation du 24/10 de `D-206` ; le code AL-3.3 dans celle du 28/10).

## 3. Ligne grossesse : quatorze chemins

Les dix causes de la session, plus quatre ; G4a' est redéfini. « Vraie ? » : la candidate du 24 au 27/10 est-elle vraie sur tout le chemin, avec les bases du §2.1 ?

| Code | Niveau | Chemin | Exemple (registre) | Candidate (24-27/10) | Vraie ? |
| --- | --- | --- | --- | --- | --- |
| G1a | 1 | calcul sous 0,5, toutes les notes à 0 : produit non rincé, ou rincé (bain de bouche compris) | — | « Aucun ingrédient de ce produit n'a de donnée défavorable pour la grossesse. » | **oui**. L'état « Données insuffisantes » (I4) peut coexister ; la phrase reste exacte, puisqu'elle porte sur les données |
| G1a' | 1 | calcul sous 0,5 avec une note la plus haute à 1 : produit non rincé moins exposant que le lait corps, ou bain de bouche (facteur 0,2641) | 46 des 55 catégories non rincées calculables sont sous 0,5 à NB 1 (classeur) ; 43 d'entre elles sont même sous le bain de bouche (`T-338`). Chemin écrit pour l'allaitement (`D-277` : « tous les NB_allaitement sont ≤ 1 ») | (la même) | **non**. Plusieurs bases du NB 1 sont des données défavorables pour la grossesse : perturbateur de priorité 3, étude animale isolée, fertilité suspectée, huile essentielle à signal faible. Même là où la phrase serait littéralement vraie (allergène, « insufficient data »), elle s'affiche à côté d'un ingrédient signalé (`D-112`, A1). Chemin beaucoup plus fréquent depuis le 27/10 : le parfum est présent dans 20 des 35 produits vérifiés (`D-298`) |
| G1b | 1 | produit rincé de la classe majoritaire, note la plus haute de 1 à 3 | gel douche jusqu'à NB 3 (`D-289`) | « Ce produit se rince : l'ingrédient signalé ne reste pas sur la peau. » | **non**. Fausse sur une partie du chemin : « sur la peau » pour un rincé de la bouche, comme le dentifrice (rincé de la classe majoritaire : classeur ; `T-450`) ; « l'ingrédient signalé » s'il y en a plusieurs. « Ne reste pas » est inexact partout : un rincé en laisse un peu (`T-533` c, base factuelle et mesure). La phrase dit enfin le motif de la règle des rincés, non un écart d'exposition : à NB 3, un non-rincé moins exposant reste au niveau 3 (`T-338`) |
| G2a | 2 | calcul : NB 1 dans un produit très exposant | les 9 catégories du §0 : lait corps 0,50 ; après-solaire 0,57 ; spray solaire visage 0,60 ; jambes lourdes 0,75 ; déodorant spray 0,76 ; spray solaire corps 0,9998 ; solaire corps 1,22 ; amincissant 1,46 ; anti-vergetures 1,99 (classeur ; `D-234`, `D-289`) | « Ce niveau tient au type de produit plus qu'à l'ingrédient, dont la donnée est faible. » | **à vérifier** sur le chemin du seul parfum (`CT-1.3`, `T-621`). Lecture préliminaire de Claude : vraie dans les deux sens de « donnée faible » (signal faible ; peu de données). La candidate n'affirme aucune quantité |
| G2b | 2 | calcul : bain de bouche, NB 2 ou 3 | 0,53 ; 0,79 (`D-277`) | « Ce niveau vient d'un ingrédient dont l'avis officiel est défavorable, atténué par le rinçage. » | **non**. Beaucoup de NB 2 et 3 ne reposent sur aucun avis officiel : nanomatériau, dossier REACH, données animales, « unsafe » du CIR, doute entre 1 et 2. « Atténué par le rinçage » est trompeur en plus à NB 2 : le facteur est bien réduit, mais le niveau obtenu (0,53, niveau 2) est celui que le plancher donnerait à un non-rincé |
| G2c | 2 | plancher : NB 2, produit non rincé | spray solaire corps à NB 2 (1,9997, `D-289`) | « Ce niveau vient d'un ingrédient qui fait l'objet d'une restriction ou d'un classement officiel. » | **non**. Faux pour le doute entre 1 et 2 (P5), les données animales (E3), le CIR avec réserves (I7), l'huile essentielle à mécanisme documenté (H1) et le nanomatériau qu'aucune annexe ne restreint |
| G3a | 3 | calcul : NB 2 dans un produit très exposant | anti-vergetures 3,98 (calcul) ; solaire corps 2,44 et amincissant 2,92 (classeur) | « Ce niveau tient autant au type de produit qu'à l'ingrédient, dont la donnée est défavorable. » | **non**. Faux pour un nanomatériau noté 2, dont le motif est l'incertitude (N1). Exemple : un solaire corps minéral au dioxyde de titane nano. Le SCCS le juge sans risque sur une peau saine jusqu'à 25 % comme filtre UV, hors inhalation (avis SCCS/1516/13, révisé le 22/04/2014 ; entrée 27a de l'annexe VI, règlement 2016/1143). Ce produit sort au niveau 3 (`D-289` : solaire corps à NB 2 → orange). Fragile aussi pour le doute entre 1 et 2 (P5) |
| G3b | 3 | plancher : NB 3, produit non rincé | lait corps à NB 3 | « Ce niveau vient d'un ingrédient dont les données sont nettement défavorables. » | **à nuancer**. **Fragile** pour la silice nano en forme inhalable (N3). Le motif écrit, « même motif » que le dioxyde de titane, est jugé inexact par le dossier (N3). L'avis SCCS/1545/15 n'est pas défavorable ; il ne rapporte aucune donnée de toxicité aiguë par inhalation, mais cite une étude de 13 semaines chez le rat, défavorable pour certaines silices amorphes (`C-268`). Que ces données soient « nettement défavorables » est donc discutable (lecture de Claude) ; le point 22, à soumettre, ramènerait la silice nano à 2 dans toutes les formes. Réserves aussi : pour les sels d'aluminium, que le SCCS juge sûrs dans des limites (avis favorable, vérifié le 02/11 : `D-318`), sans recommandation de l'ANSM retrouvée (`C-319`), question 34 en attente (`T-642`) ; pour l'acide salicylique, noté 3 par sa H361d harmonisée mais autorisé sous conditions (annexe III, entrée 98 ; dossier, section 9). Le CMR admis par dérogation est dans le même cas : aujourd'hui, le conservateur H350 de l'annexe V cité en C8 (G4a', question 28) ; aucune H360 harmonisée ne figure aux annexes III à VI, au contrôle du 28/10 par numéro CAS, auquel une entrée sans numéro CAS échappe (R7) |
| G4a | 4 | interdiction : annexe II ; H360D, H360F, H340 ou H350 harmonisées sans dérogation (article 15) | — | « Ce niveau vient d'un ingrédient interdit en cosmétique. » | **oui**. Le mot est soumis à la juriste (`T-533`, 28/10). La phrase revient sur l'acquis de `D-103` (§6, point 6) |
| G4a' | 4 | H340 ou H350 harmonisée, substance admise par dérogation (C8 n'a pas de clause de dérogation) | un conservateur de l'annexe V, cas cité en C8 | (la même) | **sans objet aujourd'hui** : la question 28 propose « 3 au moins », appliquée à titre provisoire (statut « À soumettre », `D-254`). Le cas suit alors les chemins d'un 3 : G3b dans un non-rincé, mais aussi G1b, G2b ou G4c. **Fausse** si la question 28 est refusée. Remplace le G4a' de la v1 (H340 ou H350 non harmonisée), qui n'existe pas |
| G4b | 4 | contre-indication ou restriction officielle visant la grossesse (R3, R4, R5) ; interdiction nationale formelle d'un État membre (R6) | — | « Ce niveau vient d'un ingrédient officiellement déconseillé pendant la grossesse. » | **oui** pour R3 à R5 ; **en deçà de la réalité** pour R6, qui est une interdiction. Les interdictions nationales des autres États membres ne sont pas criblées : R6 ne joue que pour le marché visé (`L-31`) |
| G4c | 4 | calcul : NB 3 dans l'anti-vergetures (5,97), seul niveau 4 obtenu par le calcul | `D-289` | deux candidates en attente (`L-13`) | dépend de la DAp de l'anti-vergetures |
| G4d | 4 | NB 4 sans interdiction ni position officielle : sources indépendantes convergentes (R8) ; huile essentielle dont la contre-indication vient d'une source de référence qui n'est pas une autorité (H1) | — | **aucune** | **trou**. G4b y serait fausse (« officiellement ») |
| G4e | 4 | rétinol, noté 4 par analogie avec les rétinoïdes topiques médicamenteux | dossier, section 9 | (celle de G4b) | **non établie** : la position officielle vise les médicaments ; la base attend J2a (②-G). Piste ouverte : un usage « déconseillé en grossesse » prêté à l'ANSM (`C-319`, non examiné). S'il était confirmé, R4 donnerait 3, et non 4 (dossier, section 9) |

## 4. Ligne allaitement : dix-sept chemins

Les onze causes de la session, plus six. Les candidates sont jugées sur l'échelle de `D-197` et les principes de `D-222` (§2.2). Sur la copie de la grossesse, valeur d'attente, une phrase qui qualifie l'ingrédient peut devenir fausse. La colonne « Vraie ? » le signale. La copie n'atteint aucune utilisatrice tant que `VERROU-1` tient (`D-245`) ; restent le prototype, le test, et la règle ouverte de `T-283` (§6, point 8).

| Code | Niveau | Chemin | Exemple (registre) | Candidate (24-27/10) | Vraie ? |
| --- | --- | --- | --- | --- | --- |
| A1a | 1 | route du lait sous 0,5, notes à 0 | — | « Aucun ingrédient de ce produit n'a de donnée défavorable pour l'allaitement. » | **vraie selon `D-197`, fausse sur la copie** : un 0 de la grossesse ne dit rien du nourrisson (`D-222`). Couvre aussi le rincé sans aucune note |
| A1a' | 1 | route du lait sous 0,5 avec une note la plus haute à 1, bain de bouche compris | chemin écrit pour les non-rincés (`D-277`) ; bain de bouche à NB 1 : ajout de Claude | (la même) | **non**, comme G1a' |
| A1b | 1 | produit rincé de la classe majoritaire, note la plus haute de 1 à 3 | gel douche à NB 3 → 0,03 (`D-277`) | « Ce produit se rince : l'ingrédient signalé ne reste pas sur la peau. » | **non**, comme G1b. Le 3 conventionnel de `D-213` (A3d) peut aussi passer par ce chemin |
| A1c | 1 | produit à l'attribut : toutes les notes nourrisson à 0, chacune jugée, et route du lait sous 0,5 | baume pour mamelons | « Chaque ingrédient a été jugé pour la zone de tétée, et aucun n'appelle de précaution. » | **non**. Vraie sur la route de la bouche : chaque 0 est un jugement relu (`D-215`). Mais le chemin admet un NB_allaitement de 1 sur la route du lait (`D-277`) : « aucun n'appelle de précaution » s'affiche alors à côté d'un ingrédient signalé (`D-112`, A1), comme en G1a'. « A été jugé » décrit la méthode (§6, point 6). La phrase est construite sur « et » (règle de syntaxe proposée, `T-533`) |
| A2a | 2 | calcul : NB 1 dans un produit très exposant | lait corps 0,50 ; après-solaire 0,57 ; spray solaire visage 0,60 ; jambes lourdes 0,75 ; déodorant spray 0,76 ; anti-vergetures 0,995 ; spray solaire corps 0,9998 ; solaire corps 1,22 ; amincissant 1,46 (`D-277`) | **aucune** | **trou** |
| A2b | 2 | calcul : bain de bouche, NB 2 ou 3, dont le 3 conventionnel de `D-213` | 0,53 ; 0,79 | **aucune** | **trou** |
| A2c | 2 | plancher : NB 2, produit non rincé | spray solaire corps 1,9997 ; anti-vergetures 1,99 (`D-277`) | « Ce niveau vient d'un ingrédient aux données défavorables, quelle que soit la quantité présente. » | **vraie selon `D-197`, fausse sur la copie**. Vraie pour les niveaux de référence (synthèse qui conclut à la prudence ; cas isolé). Fausse sur la copie pour un nanomatériau noté 2 (N1), comme G3a |
| A2d | 2 | route de la bouche : note nourrisson 1 (motif positif) ou 2 | baume pour mamelons | « Ce niveau vient d'un ingrédient que le nourrisson peut avaler depuis la zone de tétée. » | **oui** |
| A3a | 3 | calcul : NB 2 dans un produit très exposant | solaire corps 2,44 ; amincissant 2,92 (`D-277`) | **aucune** | **trou** |
| A3b | 3 | plancher : NB 3, produit non rincé (H362, si 3 est retenu) | — | « Ce niveau vient d'un ingrédient dont les données sont nettement défavorables. » | **vraie selon `D-197`, fausse sur la copie**. Vraie pour les niveaux de référence (H362, imputabilité établie, synthèse qui conclut à éviter). Fausse sur la copie pour une base propre à la grossesse, comme H361d harmonisée ; fragile pour la silice nano inhalable, comme G3b |
| A3c | 3 | route de la bouche : note nourrisson 3 | baume pour mamelons | « Ce niveau vient d'un ingrédient qui pose un problème si le nourrisson l'avale. » | **vraie, mais vague** (« pose un problème ») |
| A3d | 3 | provisoire (`D-213`) : 4 en grossesse pour une contre-indication propre à la grossesse, compté 3 | rétinoïde | « Cet ingrédient n'a pas encore été jugé pour l'allaitement : son niveau grossesse s'applique. » | **non**. Le niveau grossesse est 4, la ligne affiche 3. « Pas encore » annonce une évaluation (`T-533` d, e). La phrase d'A3b serait fausse elle aussi : ce 3 est une convention, sans donnée. Chemin qui n'atteint aucune utilisatrice (`VERROU-1`) |
| A4a | 4 | interdiction : annexe II, automatique sur les trois colonnes (`D-212`) ; CMR interdits par l'article 15 (H360D, H360F, H340, H350 harmonisées), par la copie et par l'« interdiction » de `D-197` | — | « Ce niveau vient d'un ingrédient interdit en cosmétique. » | **oui** ; même réserve de la juriste qu'en G4a. Réserve : les entrées de l'annexe II assorties d'une exception sont laissées au toxicologue (`D-212`) ; s'il les note 4, la phrase est fausse (`D-212` ; pour la grossesse, `T-591` et R2) |
| A4b | 4 | contre-indication d'une autorité visant l'allaitement (`D-212`) | — | « Ce niveau vient d'un ingrédient officiellement déconseillé pendant l'allaitement. » | **oui**. Fausse sur le chemin A4e, sur la copie seulement |
| A4c | 4 | route de la bouche : note nourrisson 4 | miel (Anses, 31/10/2023) | « Ce niveau vient d'un ingrédient qui ne doit pas être avalé par un nourrisson. » | **vraie**, mais « ne doit pas » se lit comme une consigne (`D-66`, aucun appel à l'action sur un verdict). Chemin lié à la décision AL-3.3 |
| A4d | 4 | H362 noté 4, si le toxicologue le retient (`T-622`) | — | **aucune** | **conditionnel**. A4b y serait inexacte : une classification n'est pas un conseil, et une H362 du dossier REACH n'a rien d'officiel |
| A4e | 4 | sur la copie : un 4 de la grossesse que le plafond de `D-213` ne vise pas (R8, H1 hors autorité ; G4a', si la question 28 est refusée ; R3, R5 et R6 selon la portée de « contre-indication ») | — | **aucune** | **conditionnel** (sur la copie seulement). A4a et A4b y seraient fausses. La portée exacte de `D-213` reste à trancher. Chemin qui n'atteint aucune utilisatrice (`VERROU-1`) |

Le calcul ne donne pas de niveau 4 en allaitement : au plus 4,38, pour l'amincissant à NB 3 (`D-229`, `D-277`). Le flacon d'huile essentielle pure n'est plus un chemin du niveau 4 (`D-338`).

## 5. Ce qui a bougé depuis la session du 24 au 27/10

- **Parfum et « Aroma » notés 1** (`D-298`, `D-306`, `D-307` ; dossier, F1). Ils entrent dans le calcul, avec le motif de l'arbitrage 18. D'où :
  - le chemin G1a' / A1a', beaucoup plus fréquent (parfum présent dans 20 des 35 produits vérifiés, `D-298`) ;
  - le lait corps parfumé au niveau 2 par le seul parfum (`T-621`, `CT-1.3`).
- **Allergènes à étiquetage et « insufficient data » notés 1** (`D-306` ; F2, I5) : même effet.
- **Nanomatériaux à 2 au moins, à 3 en forme inhalable ; oxyde de zinc inhalable à 3** (`D-306` ; arbitrage 23 ; N1 à N4). G2c reste fausse ; G3a et A2c le deviennent.
- **CMR** (`D-307`, arbitrages 19 et 20 ; dossier, C1 à C8) :
  - H360D et H360F harmonisées → 4 par l'article 15, et 3 au moins par dérogation ;
  - une classification du dossier REACH vaut une classification harmonisée, sans dépasser 3 ;
  - une notification isolée ne fonde aucune note ;
  - H340 et H350 harmonisées → 4, H341 et H351 → 3 (compte rendu, question 13). C'est une exception à `D-44` (un danger non propre à la grossesse descend dans l'information) : pour H350 et H351 le 27/10, étendue à H340 et H341 le 28/10 (`D-315`).
  La session ne savait pas traiter la « quatrième porte du niveau 4 », la base 6 (H360 harmonisée, `D-252`). Elle se range désormais sous l'interdiction (compte rendu, question 10).
- **Dossier des règles v0.1 et questions 27 à 32** (`D-318`, 28/10). Le dossier consolide les règles. Les questions sont parties le 28/10, dont la 28 (dérogation pour H340 et H350) ; réponses attendues à partir du 23/11.
- **Le flacon d'huile essentielle pure sort des chemins** (`D-338`, 30/10).
- **Le savon sort du verdict** (`D-339`). Sans effet sur les phrases : c'était une condition.
- **La présomption européenne** (`D-353`) : aucun chemin nouveau. Sa limite va dans les conditions ou la fiche méthode.

## 6. Ce que l'inventaire fait apparaître

1. **Quatre trous** :
   - en allaitement, les trois chemins du calcul (A2a, A2b, A3a). Le plus courant est le lait corps parfumé (A2a), celui du parcours principal du prototype ;
   - en grossesse, le niveau 4 sans interdiction ni position officielle (G4d).
   S'y ajoutent trois chemins conditionnels sans candidate : G4a', si la question 28 est refusée ; A4d, si H362 vaut 4 ; A4e, sur la copie de la grossesse.
2. **Neuf candidates fausses sur une partie de leur chemin**, avec des notes attribuées selon les règles :
   - G1a', A1a' et A1c, pour le NB 1 qu'elles passent sous silence ;
   - G1b et A1b, pour « sur la peau », le singulier et « ne reste pas » ;
   - G2b, pour « avis officiel » (« atténué par le rinçage » est en outre trompeur à NB 2) ;
   - G2c, pour « restriction ou classement » ;
   - G3a, pour « donnée défavorable » appliquée à un nanomatériau noté 2, dont le motif écrit est l'incertitude (N1) ;
   - A3d.
   **Trois autres sont vraies selon `D-197`, fausses sur la copie** : A1a, A2c, A3b. Par ailleurs, G4b n'est pas établie pour le rétinol (G4e).
3. **À nuancer** :
   - A3c : « pose un problème » ;
   - A4c : « ne doit pas » ;
   - A4a : les entrées de l'annexe II assorties d'une exception ;
   - G3b : la silice nano inhalable (fragile), les sels d'aluminium, l'acide salicylique, le conservateur admis par dérogation ;
   - G4b : R6, limité au marché visé.
4. **Le moteur ne connaît aucune concentration** (§1). Une phrase qui dit une quantité d'ingrédient (« peu », « beaucoup ») dit donc ce qu'il ne calcule pas. Deux cas où le dépôt sur la peau n'est pas ce qui fait le niveau :
   - sur le déodorant spray, l'exposition compte tout ce qui sort du flacon (`D-234`) ;
   - sur l'anti-vergetures en grossesse, la DAp de 100 % est une précaution (`L-13`).
   Enfin, le rincé n'ordonne pas l'exposition (`T-338`).
5. **Une règle manque.** Quand deux causes fixent le même niveau (deux ingrédients, ou les deux routes), laquelle donne la phrase ? `D-278` marque les deux ingrédients, mais il n'y a qu'une phrase. `D-165` ne départage pas : il ordonne des mentions, et le lait est lui aussi une ingestion par le nourrisson.
6. **Deux règles, l'une ouverte, l'autre acquise, en sont touchées** :
   - « Ne rien écrire sur la manière dont les verdicts sont établis, au-delà d'un texte de remplacement pour la fiche méthode » (dossier de conception du 30/09, §4.4). Le registre ne porte pas la règle elle-même, mais trois entrées voisines : `D-116` (l'attribution des notes doit être automatisée, le toxicologue relisant ; c'est un plan : aucune note n'a été produite par le prompt, `C-251`) ; `T-534` (les revendications de la fiche méthode sont à borner) ; `T-551` (règlement IA, article 50(4) : signaler un texte généré par IA qui informe le public, sauf examen humain de fond). Une phrase par cause dit d'où vient le niveau ; A1c décrit même la méthode (« a été jugé »).
   - L'acquis annoté le 29/09 sur `D-103` (les libellés des quatre niveaux) : « « Interdit » écarté (faux pour deux des trois portes du niveau 4) » et « la phrase dit une conclusion de l'application, pas l'état du droit ». Or G4a et G4b disent l'état du droit ou une position officielle. `D-302` a choisi la phrase par cause, et la session avait noté que « interdit » redevenait utilisable pour sa porte (`T-609`, proposition sans réponse).
   Les deux écarts restent à tracer.
7. **Le vocabulaire du bébé.** La session écrivait « le nourrisson ». Les éléments déjà validés de la ligne allaitement aussi : `D-259` (« la peau du nourrisson »), `D-260` (« Inhalation par le nourrisson non évaluée ») ; `D-261` dit « le nouveau-né ». Ces éléments s'affichent sur le même écran que la phrase. Le 04/11, la porteuse aurait choisi « bébé », sans article, pour les cases du prototype (décision 264, non vérifiée, §0). Le libellé de H362 dit « bébés nourris au lait maternel » (compte rendu, réponse sur H362). La v1 voyait dans ce choix (« bébé », sans article) un écart à `D-114` C1 (« aucun texte ne suppose une grossesse en cours », 29/09) ; ce rattachement reste à examiner avec la décision 264.
8. **La vérité des phrases allaitement dépend de l'attribution.** Avec des notes attribuées selon `D-197` et `D-222`, A1a, A2c et A3b tiennent. Elles deviennent fausses dans deux cas : sur la copie de la grossesse, valeur d'attente, qui n'atteint aucune utilisatrice tant que `VERROU-1` tient ; pour un ingrédient sans NB_allaitement que la règle ouverte de `D-214` (étape 4 ; `T-283`) renvoie à la grossesse. `VERROU-1` couvre la validation du prompt, pas cette règle.
9. **Le libellé du niveau 1** (« Composition sans signal identifié », `D-103`) s'affiche à côté d'un ingrédient signalé sur G1a', G1b, A1a', A1b et A1c. C'est plus fréquent depuis que le parfum est noté 1. Point pour le test des libellés (`T-541`).

## 7. Ce que la version 1 de CT-1.2 en hérite

`CT-1.2-preparation.md` (version 1, 04/11) s'appuyait sur la v1 de cet inventaire. Reposent sur ses erreurs ou sur les faits établis ici :
- **le choix 4** : son point de départ (« faux pour H340 et H350 non harmonisées ») ; ses deux phrases pour G4a' n'ont plus de chemin (§3) ;
- **le choix 5** : la phrase d'A3b qu'il propose pour le chemin de `D-213` au prototype est fausse (§4) ;
- **« donnée défavorable » au NB 2** : les propositions qui gardent cette formule (G2b, G2c ; G3a et A2c, conservées telles quelles) sont fausses pour un nanomatériau (§3, §4) ;
- **la proposition de G2a** (« qui en dépose beaucoup sur la peau ») : fausse sur les sprays et sur l'anti-vergetures en grossesse ; « en » n'y a pas d'antécédent (§6, point 4) ;
- **la seconde phrase du choix 1** (« Ce type de produit apporte peu de l'ingrédient signalé ») : elle affirme une quantité que le moteur ne connaît pas (§6, point 4) ;
- **A4a et le décompte du §4** : la mention « G4a' vaut aussi » ; le texte de G4a' ;
- **le choix 2** : « la route de la bouche avant celle du lait (ordre de `D-165`, l'ingestion d'abord) ». `D-165` ne départage pas (§6, point 5) ;
- **la proposition pour G1b et A1b** (« il reste peu de l'ingrédient signalé ») : elle affirme une quantité (§6, point 4), garde le singulier, et dit « peu » d'un dentifrice ou d'un bain de bouche sans fondement (§3) ;
- **les propositions d'A2a, A2b et A3a** (« comme G2a », « comme G2b », « comme G3a ») : elles reprennent des formules que cet inventaire dit fausses ou fragiles ;
- **les « (garder) » de G3b, G4b, A1a, A3b et A4b** : chacun porte désormais une réserve ou un verdict contraire (§3, §4) ;
- **le choix 3** (décision 264, non vérifiée, §0, point 6) et **le choix 6** (« textes §1 », renvoi relocalisé au §4.4 du dossier de conception).

CT-1.2 sera mise à jour après les décisions de la porteuse.

## Annexe A — Corrections à inscrire au registre (propositions)

Les numéros seront attribués à la génération. Les typologies sont à valider par la porteuse :
- (1) raisonner sans lire la source ;
- (2) reproduire une formulation sans la vérifier ;
- (3) lire un point sans ses voisins ;
- (4) balayage asymétrique ;
- (5) inversion incorrecte.

Les points 1 à 7 et 9 sont des erreurs de la v1 de CT-1.1 (04/11), remise à la porteuse ; le point 9 était repris dans la première remise de la v2. Aucune n'est entrée au registre.

1. **Quatre bases du §2 de la v1.** Elles reprenaient la lecture « par statut » de `D-306`, que les arbitrages 19 et 20 (`D-307`) et le dossier des règles (C1, C3, C4, C7) ont remplacée : H361f non harmonisée → 1 ; H361d non harmonisée → 2 ; notification isolée → 2 au plus ; H360F harmonisée → 3. Typologie proposée : (3).
2. **« H340, H350 (`D-315`), harmonisées ou non » → 4**, et le chemin G4a' / A4a' qui en découlait. La question 13 du compte rendu et la règle C8 ne visent que les classifications harmonisées ; le registre ne porte pas le mot (`D-306`, `D-315`). L'ancien chemin se répartit ainsi : une H340 ou H350 du dossier REACH irait à 3 par le principe de l'arbitrage 20, à confirmer ; une notification n'est pas une base de note (C7) (§2.1, règles ouvertes). Typologie proposée : (1).
3. **Motif du parfum, « composition non déclarée » (v1).** C'est, résumé, le motif écrit du toxicologue (« Sa composition exacte n'est pas déclarée »), qui n'a pas été retenu. Le motif retenu est celui de l'arbitrage 18 (F1). Typologie proposée : (2).
4. **Les rincés sans plancher, « sauf le bain de bouche » (v1, §1).** Le bain de bouche n'a pas de plancher : il atteint le niveau 2 par le calcul. À NB 1, il n'était rangé dans aucun chemin (« bain de bouche exclu » de G1b) ; il relève de G1a'. Typologie proposée : (3).
5. **Bases et chemins omis.** Au NB 3 : R4 (« à déconseiller » de l'ANSM), I8, E1, H1. Au NB 4 : R6, R8, H1 et le rétinol. G4b a été dite vraie sans réserve. Typologie proposée : (4).
6. **Candidates allaitement jugées sur les bases de la grossesse.** A2c et A3b ont été dites vraies, et A4a réservée pour H340 et H350, sans `D-197` ni `D-222`. Typologie proposée : (1).
7. **G3a, et A2c, dites vraies.** Elles sont fausses pour un nanomatériau noté 2, alors que la v1 relevait le nanomatériau pour G2c. Typologie proposée : (4).
8. **Correction d'un message de Claude** (réponse au message de la porteuse du 04/11 à 23 h 45). Claude y écrivait que le bain de bouche, à NB 1 (environ 0,26), « relève de G1b, que l'inventaire lui fermait ». Or son facteur d'exposition, 0,2641, dépasse celui de 43 des 55 catégories calculables non rincées (`T-338`). La phrase du rinçage le dirait à tort peu exposé ; il relève de G1a'. La v1 avait raison de l'exclure de G1b. Corrigé avant toute suite, signalé à la porteuse avec la remise de cette version. Typologie proposée : (3).

9. **« Le moteur n'est pas dans le dépôt. Le classeur de calibration (onglet « Paramètres ») n'y est pas. »** C'était faux dans la v1, et la première remise de la v2 le répétait. L'onglet est au projet, dans `mamaCARE_Benchmark_Calibration_INCI.xlsx`. Relevé par la question de la porteuse (05/11, 0 h 35 : « c'est à dire ? on ne la jamais produit ? »). Effet : des valeurs que l'inventaire disait citées sans vérification, ou probables, sont désormais recalculées (§0, point 1). Typologie proposée : (2), car la limite de la v1 a été reprise sans être vérifiée.

10. **Première remise de la v2 (05/11), relevée par la relecture indépendante** (annexe B). Erreurs de Claude, aucune n'est entrée au registre :
    - G1b et A1b dites « à nuancer », alors qu'elles sont fausses sur une partie de leur chemin (dentifrice ; plusieurs ingrédients). La v2 n'appliquait pas à elles la règle qu'elle appliquait aux autres (`D-104`). Typologie proposée : (4).
    - G3b dite vraie sans autre réserve que les sels d'aluminium, alors que la silice nano inhalable, l'acide salicylique et le conservateur admis par dérogation la rendent fragile. Typologie proposée : (4). La correction elle-même a d'abord forcé le trait (« non », et `C-268` lu comme « aucune donnée d'inhalation ») ; la relecture 4 l'a ramenée à « à nuancer ». Typologie proposée pour cet écart : (2).
    - A1c dite vraie, alors que son chemin admet un NB_allaitement de 1 (`D-277`), l'argument qui rendait G1a' fausse. Typologie proposée : (4).
    - Le rincé sans aucune note n'avait pas de chemin en grossesse (lacune héritée de la v1). Un 4 recopié que `D-213` ne plafonne pas n'avait pas de chemin en allaitement (A4e). Typologie proposée : (3).
    - A1a, A2c et A3b portaient trois étiquettes différentes pour une même situation, et le décompte des fausses n'en prenait qu'une. Typologie proposée : (4).
    - R5 reformulé sans la lettre du dossier (« si elle, ou l'avis, cible explicitement la grossesse »). Typologie proposée : (2).
    - Le classeur décrit comme « gelé le 28/10 » (copie du 26/10, `D-317`), avec 75 catégories au lieu de 76. Typologie proposée : (2).

**Écarts mineurs, sans typologie** :
- G2a omettait les sprays de `D-234` ;
- la v1 donnait G1a' comme sans « aucune valeur citée au registre (chemin déduit du calcul) », alors que `D-277` écrit ce chemin pour l'allaitement ;
- « `D-315`, 28/10 » : 27/10 pour H350 et H351, 28/10 pour H340 et H341 ;
- « textes, §1 » renvoyait à une règle qui est au §4.4 du dossier de conception ;
- « anti-vergetures 3,98 » était donné comme un exemple du registre ; c'est un calcul (2 × 1,99) ;
- v1, bases manquantes en plus de celles du point 5 : aucune ligne NB 0 ; au NB 1, E1 à E4, H1, I7, C16 et C17 ; au NB 2, E2, E3, H1 et I7. Son G2a omettait aussi l'après-solaire et les jambes lourdes ;
- v1, A4a réduit dans la première remise de la v2 à l'annexe II, sans les CMR de l'article 15 ;
- première remise de la v2 : deux citations de la v1 entre guillemets n'étaient pas mot pour mot (« absent du projet » ; « aucun plancher, sauf le bain de bouche ») ; « sept erreurs » au lieu de huit ; 43 non-rincées sous 0,5 au lieu de 46 ; la SED de tous les sprays dite « quantité sortie du flacon », ce que `D-234` ne dit que du déodorant spray ; trois renvois (`D-116`, `T-534`, `T-551`) donnés pour la règle du §4.4, qu'ils ne contiennent pas ; AL-3.3 rattaché à la seule annotation du 24/10 de `D-206`.

## Annexe B — Relectures de cette version

**Relecture 1 — complétude** (Claude, 05/11, après l'écriture) :
- **Contre la v1** : chaque section, chaque chemin (12 en grossesse, 15 en allaitement) et chaque point des §5 et §6 ont été retrouvés. Aucun n'est perdu. Les codes sont gardés, sauf G4a', redéfini.
- **Contre le message de Claude qui a relevé les erreurs** (réponse au message de la porteuse de 23 h 45) : chaque erreur, chaque écart mineur et chaque limite qui touche l'inventaire sont repris. Les critiques qui ne portent que sur des propositions de CT-1.2 sont laissées à sa version 2.
- **Contre le dossier des règles, sections 1 à 9** : chaque règle qui fixe une note est rangée au §2.1. Ajouts faits à cette relecture : P9 (le niveau du produit), R9 bis, C5, C6, C14, E5, le caprylyl glycol.
- **Contre les chemins du moteur** : le bain de bouche à NB 1 est rangé en G1a'. Cette relecture concluait qu'aucun niveau n'était sans chemin ; c'était faux (relecture 3).
- **Trouvé et corrigé** : le bain de bouche à NB 1, que le message de Claude rangeait en G1b (annexe A, point 8).

**Relecture 2 — exactitude** (Claude, 05/11), en partie par script (`controle_v2.py`, gardé hors de ce fichier) :
- les renvois au registre existent dans la v6.9 (61 distincts à la première remise, dont 59 entrées ; `VERROU-1` et `VERROU-3` sont définis dans `D-245`) ;
- les 20 candidates citées sont, mot pour mot, celles de `T-609` et de `T-604` ;
- les extraits du registre cités entre guillemets s'y trouvent tels quels (`D-103`, `D-206`, `D-213`, `D-215`, `D-234`, `D-259`, `D-260`, `D-261`, `D-277`, `D-298`, `D-306`, `C-307`, `T-337`, `T-338`, `T-450`). Exception : le motif écrit du parfum est cité d'après le dossier des règles (F1), dont l'apostrophe est droite, et non d'après `D-306` ;
- les 19 valeurs chiffrées citées du registre s'y trouvent. 3,98 et 0,26 sont des calculs, marqués comme tels ;
- les règles du dossier (codes et notes) et les citations du compte rendu (questions 13 et 15, réponse sur H362) ont été relues à la main sur leur texte ;
- l'avis du SCCS sur le dioxyde de titane nano et le règlement 2016/1143 ont été vérifiés le 05/11 sur la page de la Commission européenne et sur le texte du règlement ;
- typographie : aucun guillemet droit, guillemets français appariés, aucune espace de fin de ligne, tableaux à colonnes régulières.

Corrigés à cette relecture :
- une apostrophe d'un extrait de `T-338` ;
- la citation du motif du parfum, qui prêtait au toxicologue la formule de la v1 ;
- R2 bis, présentée comme une base du 4 alors qu'elle l'écarte ;
- le facteur du bain de bouche, déduit et non cité ;
- la lecture de `T-450`, présentée comme un fait ;
- la condition complète de `VERROU-3` ;
- l'ordre des bases du NB_nourrisson 4 ;
- la date des erreurs relevées.

**Relecture 3 — indépendante** (Claude, 05/11, par un agent qui n'avait pas pris part à la rédaction). Il a confronté la première remise (SHA-256 `ec401562…`) au registre v6.9, au classeur et aux deux fichiers de la v1, sans le dossier des règles ni le compte rendu. Bilan : 0 bloquant, 11 constats importants, 22 mineurs. Claude a vérifié chacun sur le registre et sur le dossier des règles avant de l'appliquer :
- **appliqués** : les constats 1 à 5, 7 à 9 et 11 (verdicts de G1b, A1b, G3b, A1c ; convention unique pour la copie ; G1a étendu aux rincés ; A4e ; C9 ; R5 ; §7), le 6 en partie, et les mineurs, sauf le 15, appliqué autrement (la note du classeur et `L-40` vont dans le même sens : DAp de 100 %, inhalation non modélisée), et les 18 et 22, appliqués en partie (complétés à la relecture 4) ;
- **appliqué en partie, le 6** : « harmonisée » est bien dans la lettre de C8 et de la question 13 du compte rendu, lus dans le projet ; seul le registre ne porte pas le mot, ce qui est désormais dit. La base du NB 3 que le relecteur proposait (H340 ou H350 du dossier REACH, par l'arbitrage 20) est inscrite comme règle à confirmer, et non comme base acquise : le principe de l'arbitrage est général, mais le dossier ne l'a décliné que pour H360 et H361 (C2 à C4). Le motif d'abord donné ici (« l'arbitrage 20 ne vise que H360D et H360F ») était faux ; la relecture 4 l'a relevé ;
- **écarté, le 10** : le cétylpyridinium et le fluorure de sodium sont nommés au dossier des règles, section 9, dont les ingrédients sont sortis des candidats de R1 et R2. Le §0, point 7 le précise. `r1_controle.py` n'a toujours pas été passé : ce fichier n'est pas destiné au toxicologue.

**Relecture 4 — indépendante, courte** (Claude, 05/11, par un second agent sans part à la rédaction), limitée au diff entre la première remise et la version corrigée (SHA-256 `106352c4…`), avec le dossier des règles lu en entier et le compte rendu par extraits. Bilan : 0 bloquant, 2 importants, 14 mineurs, tous vérifiés sur le registre et le dossier puis appliqués :
- G3b ramenée de « non » à « à nuancer » : `C-268` avait été lu trop vite (l'avis cite une étude d'inhalation de 13 semaines), et le parallèle avec le motif de G3a était une lecture de Claude. Le décompte du §6, point 2 passe de dix à neuf ;
- H340 et H350 du dossier REACH ou notifiées : « aucune règle » était faux (arbitrage 20, principe général ; C7) ;
- quatorze précisions : A4e étiqueté conditionnel, et sa liste complétée ; A4b réservé ; §6, point 9 complété ; « 55 calculables » ; citation de la v1 de l'annexe A, point 4 ; conservateur admis par dérogation et réserve de R7 en G3b ; C9 marqué comme lecture de Claude ; A2b ; G2b « trompeur » ; `D-114` ; `D-116` ; `T-336` ; bilan de la relecture 3.

**Limites des relectures** :
- les relectures 1 et 2 sont de Claude seul ; la relecture 3 est d'un agent Claude indépendant de la rédaction, mais non d'un humain, et sans le dossier des règles ni le compte rendu ;
- les corrections issues de la relecture 3 ont été relues par la relecture 4 ; celles issues de la relecture 4 n'ont pas été relues à leur tour ;
- le dossier des règles et le compte rendu, rendus dans la conversation et non en fichier, n'ont pas été confrontés par script ;
- les facteurs d'exposition ont été recalculés sur le classeur après la première remise (annexe A, point 9) ; le code du moteur, absent, n'a pas été relu.
