# CT-1.1 — Inventaire des causes du niveau, par ligne, avec les chemins du moteur

Planning, chantier `CT-1` (« Phrases sous le verdict »), tâche `CT-1.1` (Claude, 1 h). Fait le 04/11/2026, à la demande de la porteuse (« lance CT1.1 et CT 1.2 du planning »), sur le **registre v6.9** (02/11). Il prépare `CT-1.2`, qui est la tienne : écrire les phrases (voir `CT-1.2-preparation.md`, à côté).

Ce document ne décide rien. Il dit, pour chaque niveau de chaque ligne, **ce qui peut le produire** (les « chemins »), et vérifie si les phrases candidates de la session du 24 au 27/10 (`T-609`, `T-604`) sont **vraies sur tout leur chemin** (règle de `D-104`).

## 0. Ce que vaut cet inventaire (limites, à lire d'abord)

1. **Le moteur n'est pas dans le dépôt.** Le classeur de calibration (onglet « Paramètres ») n'y est pas. Les chemins sont **reconstitués à partir du registre** (`D-50`, `D-214`, `D-277`, `D-289`, `T-609`), et les valeurs chiffrées (0,50 ; 1,99 ; 5,97…) sont **celles qu'il cite**, pas des calculs refaits. Une erreur du registre passerait ici.
2. **Les chemins sont provisoires**, comme le tableau de basculement de `D-289` : ils dépendent de règles jamais validées par le toxicologue (plancher gradué, rincés sans plancher, NB 4 absolu sur les rincés, `T-380`), de la DAp de l'anti-vergetures (`L-13`) et des réponses attendues à ②-A.
3. **Les bases des notes** (ce qui fonde un NB 1, 2, 3 ou 4) sont lues dans `D-306`, `D-307` et `D-315`. Plusieurs restent en attente (arbitrages 21 et 22, question 27, H362 en allaitement). Le §2 dit lesquelles.
4. **Hors de cet inventaire** : l'état « Évaluation incomplète » (ce n'est pas un niveau, il a son cadre, `D-275`) ; le flacon d'huile essentielle pure (écran de refus au lancement, `D-338`) ; les produits hors champ (médicament, dispositif médical, produit pour bébé : refus, `D-214` étape 0).

## 1. Le moteur, en bref

**Le calcul** (`D-214`, étape 4 ; `D-50`) : `NM = NB × DAp × SED_cat / SED_ref`. Seuils en « supérieur ou égal » : **0,5** (niveau 2), **2** (niveau 3), **5** (niveau 4). La catégorie de référence est le lait corps : à NB 1, il donne exactement 0,50, donc le niveau 2. C'est l'étalonnage du modèle, pas un effet de bord (`D-50`).

**Les garde-fous**, qui court-circuitent le calcul :
- **plancher gradué**, produits non rincés seulement : un NB 2 donne au moins le niveau 2, un NB 3 au moins le niveau 3 ;
- **produits rincés** : aucun plancher (option B, `T-380`), sauf le **bain de bouche**, seul rincé hors de la classe majoritaire (`T-450`) ;
- **NB 4 → niveau 4**, partout, rincés compris (« une interdiction ne se dilue pas », `C-307`).

**En allaitement, deux routes** (`D-214`, étapes 4 et 5) :
- **la route du lait** : le même calcul, avec NB_allaitement et les DAp de l'allaitement, et les mêmes planchers ;
- **la route de la bouche** (zone de tétée), pour les produits à l'attribut seulement (soins des mamelons) : la note NB_nourrisson la plus haute donne le niveau directement. 0 : rien. 1 ou 2 : au moins le niveau 2. 3 : au moins le niveau 3. 4 : niveau 4.
- **Le niveau affiché** est le plus haut établi entre les deux routes (`D-147`).
- **Chemin provisoire** (`D-213`) : un ingrédient noté 4 en grossesse pour une contre-indication propre à la grossesse, pas encore noté pour l'allaitement, y compte comme un 3.

## 2. Ce qui fonde une note (les « bases »)

Lecture de Claude, à partir de `D-306` (réponses écrites du toxicologue, 26/10), `D-307` (arbitrages 18 à 24) et `D-315`. C'est ce qui permet de dire si une phrase qui qualifie l'ingrédient (« restriction », « avis officiel », « interdit ») est vraie.

| NB | Bases connues | Statut |
| --- | --- | --- |
| 1 | parfum et « Aroma » (composition non déclarée, arbitrage 18) ; allergène à étiquetage obligatoire (règlement 2023/1545) ; « insufficient data » du CIR ou du SCCS ; H361F non harmonisée ; fertilité « suspectée » | confirmé par écrit, sauf l'arbitrage 21 (en attente) |
| 2 | restriction de l'annexe III propre au profil ; perturbateur endocrinien présumé (ANSES, priorité 2) ; H361F harmonisée ; H361D non harmonisée ; fertilité « présumée » ; nanomatériau (2 au minimum : dioxyde de titane nano, silice nano) ; notification C&L isolée (2 au plus) ; doute entre 1 et 2 | confirmé, sauf la silice nano (point 22) |
| 3 | H360F harmonisée ; H361D harmonisée ; H360D ou H360F du seul dossier REACH ; H361d REACH ; H341, H351 (`D-315`) ; conclusion « unsafe » du CIR (3 au plus) ; fertilité « avérée » ; nanomatériau en spray, aérosol ou poudre libre ; oxyde de zinc en forme inhalable ; H360 admise par dérogation (3 au minimum) ; *allaitement* : H362 (renvoyé après l'étalon) ; *allaitement, provisoire* : le 4 grossesse non recopié (`D-213`) | confirmé ; H362 en attente |
| 4 | annexe II (sauf exception, comme la vaseline) ; H360D harmonisée sans dérogation (interdite par l'article 15) ; H340, H350 (`D-315`), **harmonisées ou non** ; contre-indication d'une autorité, ou avis du SCCS, **visant explicitement** la population ; *nourrisson* : contre-indication de l'Anses (miel) | confirmé |

## 3. Ligne grossesse : douze chemins (les dix causes de la session, plus deux)

« Vraie ? » : la candidate du 24 au 27/10 est-elle vraie sur tout le chemin, avec les bases du §2 ?

| Code | Niveau | Chemin | Exemple (registre) | Candidate (24-27/10) | Vraie ? |
| --- | --- | --- | --- | --- | --- |
| G1a | 1 | calcul sous 0,5, produit non rincé, toutes les notes à 0 | — | « Aucun ingrédient de ce produit n'a de donnée défavorable pour la grossesse. » | **oui** |
| G1a' | 1 | calcul sous 0,5, produit non rincé, une note à 1 dans un produit peu exposant | crème visage parfumée | (la même) | **non** : un NB 1 est une donnée défavorable (allergène, H361F non harmonisée, « insufficient data »). Chemin **plus fréquent depuis le 27/10**, le parfum étant noté 1 |
| G1b | 1 | produit rincé, note la plus haute de 1 à 3 (bain de bouche exclu) | gel douche jusqu'à NB 3 | « Ce produit se rince : l'ingrédient signalé ne reste pas sur la peau. » | **à nuancer** : un rincé en laisse un peu (facteur de rétention), « ne reste pas » est trop fort (`T-533` c) |
| G2a | 2 | calcul : NB 1 dans un produit très exposant | lait corps 0,50 ; anti-vergetures 1,99 ; solaire corps, amincissant | « Ce niveau tient au type de produit plus qu'à l'ingrédient, dont la donnée est faible. » | **à vérifier** au chemin du seul parfum : « donnée faible » pour une composition inconnue (`CT-1.3`, `T-621`) |
| G2b | 2 | bain de bouche, NB 2 ou 3 | 0,53 ; 0,79 | « Ce niveau vient d'un ingrédient dont l'avis officiel est défavorable, atténué par le rinçage. » | **non** : beaucoup de NB 2 et 3 ne sont pas un « avis officiel » (nanomatériau, H361D non harmonisée, « unsafe » du CIR, dossier REACH) |
| G2c | 2 | plancher : NB 2, produit non rincé | spray solaire corps à NB 2 (1,9997) | « Ce niveau vient d'un ingrédient qui fait l'objet d'une restriction ou d'un classement officiel. » | **non** : faux pour un nanomatériau sans restriction, une notification C&L isolée, le doute entre 1 et 2 |
| G3a | 3 | calcul : NB 2 dans un produit très exposant | anti-vergetures 3,98 ; solaire corps ; amincissant | « Ce niveau tient autant au type de produit qu'à l'ingrédient, dont la donnée est défavorable. » | **oui** |
| G3b | 3 | plancher : NB 3, produit non rincé | lait corps à NB 3 | « Ce niveau vient d'un ingrédient dont les données sont nettement défavorables. » | **oui** (toutes les bases du NB 3) |
| G4a | 4 | annexe II, ou H360D harmonisée sans dérogation | — | « Ce niveau vient d'un ingrédient interdit en cosmétique. » | **oui** sur ce chemin ; mot soumis à la juriste (`T-533`, 28/10) |
| G4a' | 4 | H340 ou H350 **non harmonisée** (`D-315`) | — | (la même) | **non** : une classification non harmonisée n'entraîne pas d'interdiction. **Chemin nouveau**, né le 28/10, après la session |
| G4b | 4 | contre-indication officielle visant la grossesse | rétinoïdes (ANSM) | « Ce niveau vient d'un ingrédient officiellement déconseillé pendant la grossesse. » | **oui** |
| G4c | 4 | calcul : NB 3 dans l'anti-vergetures (5,97), seul niveau 4 par le calcul | — | deux candidates en attente (`L-13`) | dépend de la DAp de l'anti-vergetures |

## 4. Ligne allaitement : quinze chemins (les onze causes de la session, plus quatre)

| Code | Niveau | Chemin | Exemple (registre) | Candidate (24-27/10) | Vraie ? |
| --- | --- | --- | --- | --- | --- |
| A1a | 1 | route du lait sous 0,5, notes à 0 | — | « Aucun ingrédient de ce produit n'a de donnée défavorable pour l'allaitement. » | **oui** |
| A1a' | 1 | route du lait sous 0,5, une note à 1 | — | (la même) | **non**, comme G1a' |
| A1b | 1 | produit rincé, note la plus haute de 1 à 3 (bain de bouche exclu) | gel douche à NB 3 → 0,03 | « Ce produit se rince : l'ingrédient signalé ne reste pas sur la peau. » | **à nuancer**, comme G1b |
| A1c | 1 | produit à l'attribut : toutes les notes nourrisson à 0, chacune jugée, et route du lait sous 0,5 | baume pour mamelons | « Chaque ingrédient a été jugé pour la zone de tétée, et aucun n'appelle de précaution. » | **oui**, mais ne dit rien de la route du lait ; construite sur « et » (règle de syntaxe proposée, `T-533`) |
| A2a | 2 | calcul : NB 1 dans un produit très exposant | lait corps 0,50 ; après-solaire 0,57 ; spray solaire visage 0,60 ; jambes lourdes 0,75 ; déodorant spray 0,76 ; anti-vergetures 0,995 ; spray solaire corps 0,9998 ; solaire corps 1,22 ; amincissant 1,46 | **aucune** | **trou** |
| A2b | 2 | bain de bouche, NB 2 ou 3 | 0,53 ; 0,79 | **aucune** | **trou** |
| A2c | 2 | plancher : NB 2, produit non rincé | spray solaire corps 1,9997 ; anti-vergetures 1,99 | « Ce niveau vient d'un ingrédient aux données défavorables, quelle que soit la quantité présente. » | **oui** |
| A2d | 2 | route de la bouche : note nourrisson 1 ou 2 | baume pour mamelons | « Ce niveau vient d'un ingrédient que le nourrisson peut avaler depuis la zone de tétée. » | **oui** |
| A3a | 3 | calcul : NB 2 dans un produit très exposant | solaire corps 2,44 ; amincissant 2,92 | **aucune** | **trou** |
| A3b | 3 | plancher : NB 3, produit non rincé (H362 compris, si retenu) | — | « Ce niveau vient d'un ingrédient dont les données sont nettement défavorables. » | **oui** |
| A3c | 3 | route de la bouche : note nourrisson 3 | baume pour mamelons | « Ce niveau vient d'un ingrédient qui pose un problème si le nourrisson l'avale. » | vraie, mais vague (« pose un problème ») |
| A3d | 3 | provisoire (`D-213`) : 4 grossesse propre à la grossesse, compté 3 | rétinoïde | « Cet ingrédient n'a pas encore été jugé pour l'allaitement : son niveau grossesse s'applique. » | **non** : le niveau grossesse est 4, la ligne en affiche 3. Et « pas encore » annonce une évaluation future (brief §4, aucune promesse). Ce chemin **n'atteint aucune utilisatrice** : NB_allaitement doit être validé avant la publication (`VERROU-1`) |
| A4a | 4 | annexe II (et H360D sans dérogation) | — | « Ce niveau vient d'un ingrédient interdit en cosmétique. » | **oui** ; même réserve que G4a' pour H340 et H350 non harmonisées |
| A4b | 4 | contre-indication officielle visant l'allaitement | — | « Ce niveau vient d'un ingrédient officiellement déconseillé pendant l'allaitement. » | **oui** |
| A4c | 4 | route de la bouche : note nourrisson 4 | miel (Anses 2023) | « Ce niveau vient d'un ingrédient qui ne doit pas être avalé par un nourrisson. » | vraie, mais « ne doit pas » se lit comme une consigne (`D-66`, aucun appel à l'action sur un verdict) |

Pas de niveau 4 allaitement par le calcul (au plus 4,38 : amincissant à NB 3, `D-277`). Le flacon d'huile essentielle pure n'est plus un chemin du niveau 4 (`D-338`).

## 5. Ce qui a bougé depuis la session du 24 au 27/10

- **Parfum et « Aroma » notés 1** (`D-298`, `D-306`, `D-307`, 26 et 27/10) : ils entrent dans le calcul. D'où le chemin G1a' / A1a', beaucoup plus fréquent (parfum présent dans 20 des 35 produits vérifiés, `D-298`), et le lait corps parfumé au niveau 2 par le seul parfum (`T-621`, `CT-1.3`).
- **Allergènes à étiquetage et « insufficient data » notés 1** (`D-306`) : même effet.
- **Nanomatériaux à 2 au minimum, 3 en forme inhalable** (`D-306`) : G2c devient faux.
- **H340 et H350 → 4, H341 et H351 → 3** (`D-315`, 28/10) : le chemin G4a' / A4a' apparaît.
- **Le flacon d'huile essentielle pure sort des chemins** (`D-338`, 30/10).
- **Le savon sort du verdict** (`D-339`) : sans effet sur les phrases, c'était une condition.
- **La présomption européenne** (`D-353`) : aucun chemin nouveau ; sa limite va dans les conditions ou la fiche méthode.

## 6. Ce que l'inventaire fait apparaître

1. **Trois trous en allaitement** : la session n'a écrit aucune phrase pour les chemins du calcul (A2a, A2b, A3a), alors qu'ils existent comme en grossesse. Le plus courant d'entre eux est **le lait corps parfumé** (A2a), celui du parcours principal du prototype.
2. **Cinq candidates fausses sur une partie de leur chemin** : G1a' / A1a' (le NB 1 sous le seuil), G2b (« avis officiel »), G2c (« restriction ou classement »), G4a' / A4a' (« interdit », pour H340 et H350 non harmonisées), A3d (le niveau grossesse et « pas encore »).
3. **Trois à nuancer** : G1b / A1b (« ne reste pas sur la peau »), A3c (« pose un problème »), A4c (« ne doit pas », lu comme une consigne).
4. **Une règle manque** : quand deux causes fixent le même niveau (deux ingrédients, ou les deux routes), laquelle donne la phrase ? `D-278` marque les deux ingrédients, mais la phrase est une seule. Il faut un ordre.
5. **Une règle ouverte s'en trouve touchée** : « Ne rien écrire sur la manière dont les verdicts sont établis » (textes, §1 ; `D-116`, `T-534`). Une phrase par cause dit précisément d'où vient le niveau. `D-302` l'a choisi ; l'écart reste à tracer.
6. **Le vocabulaire du bébé** : la session proposait « le nourrisson », à la troisième personne. Le 04/11, tu as choisi « bébé », sans article, sur les cases du prototype (décision 264, écart à `D-114` C1). Les phrases doivent suivre l'un ou l'autre.

Les propositions de phrases sont dans `CT-1.2-preparation.md`.
