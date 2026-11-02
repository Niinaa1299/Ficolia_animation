# Ce qui reste à faire pour clore le prototype et lancer les tests

Liste de suivi, tenue tâche par tâche. État au **02/11/2026, fin d'après-midi**. On la met à jour à chaque séance : une tâche faite reçoit sa date et son commit, une tâche tranchée reçoit les mots de la porteuse.

## 0. Reprendre ici (fin de la séance du 02/11)

**État à la fin de la séance**
- Le canevas de travail est en version 37 (`1793629912-68bf`), identique au dépôt (vérifié en fin de séance, R3). La seule retouche faite sur la page, la tenue du slogan à 2 s, est rapatriée.
- La branche `claude/magical-mendel-cwpmji` est à jour sur GitHub.

**Ce qui attend tes réponses** (rien n'est posé avant ton choix). Le texte exact de chaque proposition est dans `propositions/2026-11-02-fils-canevas-travail/propositions.md` :
- les mentions de la ligne allaitement, piste A ou B, et leurs explications (2.5a ; fils `111f9ffa`, `8b340b1d`) ;
- « Les données » du verdict à actualiser, A ou B (3.6a ; fil `a5b20715`) ;
- le report du message centré et du logo en filigrane sur les quatre autres planches de recherche (3.6 ; fil `99641baa`) ;
- les chemins critiques de la version de test, et ton accord pour la construire (2.8 ; `propositions/2026-11-02-version-de-test/proposition.md`) ;
- les autres questions du §3.1.

**Ce que la prochaine session fait d'abord**
1. R1 et R3 : l'accès au canevas, puis les retouches faites sur la page.
2. Lire les fils du canevas de travail (outil `ArtifactComments`, `action: read`). Si tu as répondu, appliquer tes choix (R2, captures avant publication).
3. Sinon, ce qui ne dépend que de Claude : l'inventaire des causes (2.1, `CT-1.1`) et la préparation de l'étape 8 sur le registre v6.8 (4.1, 4.2). Puis la base technique de la version de test, si tu as donné ton accord (2.8).

**Où trouver ce qui sert**
- **Le registre v6.8** est sur `main`, pas sur la branche de travail. Pour le lire sans fusionner (une fusion demande ton accord, R6) : `git show "origin/main:mamaCARE_Registre_Projet_29_10_26_v6-8.md"`.
- **Le planning** : page « Planning Ficolia », https://claude.ai/artifact/6LnGHNHjsMJELgzBKjCojR. Le plan est dans son fichier `plan.json` (outil « Artifact », `action: read`, `path: plan.json`). Les coches sont dans sa base (outil `ArtifactData`, `action: list`, `collection: coches`), à lire seulement : seule la porteuse coche (`D-309`).
- **Les commentaires de l'ancien canevas** : l'inventaire du 02/11, `propositions/2026-11-02-commentaires-ancien-canevas/fils-ancien-canevas.md`.
- **Les outils** : `outils/rendre.mjs` (rendu) ; `outils/rendre-reglage.mjs` (rendu avec un réglage imposé, et les liens présents à l'écran) ; `outils/verifier-liens.py` (audit des liens et des boutons, pour le contrôle final) ; `outils/preparer-publication.py`.

## Sur quoi elle s'appuie

- **Le registre v6.8** (29/10, sur `main`), en attendant la v6.9.
- **Le planning**, page « Planning Ficolia » : état au 31/10, 20 h 40. Ses coches ont été relues le 02/11.
- **La note de reprise du 31/10** (§5) et les journaux des 22 et 29/10, puis des 01 et 02/11.
- **L'inventaire des commentaires de l'ancien canevas** (02/11).
- **L'état du dépôt et du canevas de travail** au 02/11.

## Comment la lire

- **Les numéros entre parenthèses** (`PR-2.1`, `CT-1.3`…) sont ceux des sous-tâches du planning. C'est là que tu coches : le planning fait foi pour les coches (`D-309`), et Claude ne coche rien.
- **« Nouveau »** marque une tâche absente du planning, à y ajouter (message prêt au §7).
- **Les durées** sont les estimations du planning (Claude, 31/10). « ? » veut dire non estimé.
- **Les dates** sont celles du scénario central du planning. La semaine 0 commence le lundi 26/10/2026.
- **« toi »** désigne la porteuse.

## L'ordre en une phrase

Régler tout de suite les quelques points qui bloquent ou qui pressent (§1). Puis suivre le chemin du **test hors cible** (§2) : c'est le premier test, et il n'attend ni la juriste ni la fin du prototype. En parallèle, **clore le prototype** (§3) et préparer **l'étape 8** (§4). Les **tests avec la cible** (§5) viennent après la juriste et la clôture.

---

## 1. Tout de suite (cette semaine)

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 1.1 | **Données d'un tiers dans le dépôt public** : réglé le 02/11. La porteuse a eu l'autorisation (« on s'en fiche. j'ai eu l'autorisation. ») ; rien à retirer. | toi | — | — | **réglé** |
| 1.2 | **Mettre le planning à jour.** Le canevas de référence de PR-1 est maintenant le canevas de travail (depuis le 01/11). La question « Canevas refusé à Claude » est réglée. Coches proposées au §7. | toi (Claude prépare le message, §7) | 0,25 h | — | message prêt |
| 1.3 | **Fermer les fils réglés de l'ancien canevas** (`PR-1.2`). Inventaire : `propositions/2026-11-02-commentaires-ancien-canevas/fils-ancien-canevas.md`. 26 fils ouverts non envoyés à Claude : c'est toi qui les fermes, sur la page. 4 fils envoyés à Claude : `6c55f949` (réglé le 01/11) et `778d3ee5` (réglé le 02/11, tenue de 2 s), Claude y répond puis les ferme si tu le demandes ; `2c39b9fd` (police 29LT Riwaya) : capture ou abandon ; `3355a2cf` (question de la personne extérieure du 17/10) : y répondre ou non. | toi, Claude | 4 h | 1.1 pour `3355a2cf` | à faire |
| 1.4 | **Supprimer les trois planches marquées « À SUPPRIMER »** : `E3-Scan-Avant`, `E6-APropos`, `E6-BonnesPratiques`. Tu les supprimes sur la page, ou tu me le dis (R6). | toi | 0,1 h | — | à trancher |
| 1.5 | **Tenue du slogan sur les trois autres planches** au même réglage (`E1-Ouverture-Arbre-Reduit`, `E1-Accueil-Bienvenue`, `E1-Accueil-Conditions`) : 2 s aussi ? Question posée dans le fil du 02/11. | toi | — | — | **fait le 02/11** : « oui passe les à 2s » |
| 1.6 | **Numéroter les décisions des 01 et 02/11** (218 et suivantes) dans la note de reprise, d'après le journal. L'étape 8 en a besoin (§4). | Claude, sur ton accord | 0,5 h | — | à trancher |

---

## 2. Le chemin vers le premier test : le test hors cible (`PR-2`)

**Ce qu'est ce test** (protocole du 20/10, « Premier tour de test hors cible ») : cinq personnes **hors** de la population cible, aucune donnée de santé, des tâches et des critères fixés d'avance. Il ne mesure que la compréhension, pas l'usage par des femmes enceintes ou qui allaitent. Il éprouve les phrases sous le verdict (`CT-1`) et le lien vers la fiche « Toilette des seins ». Il n'attend pas la juriste (`T-464`). Estimation du 20/10 : 10 à 26 h en tout.

**Ce dont il dépend dans le planning** : `CT-1` (les phrases) et `PR-1` (le canevas, dont les fils de commentaires, tâche 1.3).

### 2.1 Les phrases sous le verdict (`CT-1`), du 09/11 au 07/12

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Inventaire des causes par niveau et par ligne, avec les chemins du moteur (`CT-1.1`) | Claude | 1 h | — | **peut commencer** |
| 2.2 | Écrire les phrases par cause, pour les deux lignes, en une passe, à partir des séries candidates du 24 au 27/10 (`CT-1.2` ; `D-302`, `T-604`, `T-609`) | toi | 4 h | 2.1 | à faire |
| 2.3 | Vérifier la phrase du niveau 2 sur le chemin du seul parfum (`CT-1.3`) | Claude | 0,5 h | 2.2 | à faire |
| 2.4 | Spécifier la mention « ce que ça change » (`CT-1.4`, `T-528`) | Claude | 1 h | 2.2 | à faire |
| 2.5 | Relire l'ensemble et le figer pour le test (`CT-1.5`) | toi | 2 h | 2.3, 2.4 | à faire |
| 2.5a | **Nouveau. Reformuler les mentions de la ligne allaitement et leurs explications** (« ne sont toujours pas clair pour un user tiers », fils `111f9ffa` et `8b340b1d`, 02/11). Deux pistes pour les cases (A : « sujet · état » en mots courants ; B : une phrase par case) et des explications nouvelles (la situation concrète, puis ce que le verdict en fait), proposées dans les fils le 02/11. Ensuite : Claude les pose sur les 13 planches de verdict et dans les listes d'ingrédients, captures avant publication. Textes « Proposition », provisoires jusqu'à `T-604`, à relire par la toxicologue. | toi, puis Claude | ? | — | **à choisir** |
| 2.6 | **Nouveau.** Reporter les phrases figées dans les planches de verdict, grossesse et allaitement, et leurs copies (règle R2) | Claude | ? | 2.5 | à faire |

### 2.2 Ce que le prototype doit offrir pour le test

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 2.7 | Valider le lien vers la fiche « Toilette des seins » (`PR-1.7`). Il est publié depuis le 02/11, sur le verdict du gel douche et dans « Bonnes pratiques ». Coche-le si ton « ok » du 02/11 valait validation. | toi | 0,5 h | — | à confirmer |
| 2.8 | **Nouveau. La version de test.** Forme choisie le 02/11 : « un lien à envoyer avec le prototype comme s'ils avaient téléchargé l'application. navigation libre + menu ou on peut séléctionner des chemins critiques qu'on veut tester absolument » ; puis « une page hmtl plein écran » « + possibilité de mettre des commentaires » ; le menu des chemins est visible des testeurs (« oui »). Proposition de Claude : une page web plein écran publiée sur claude.ai (pas un canevas), construite par un script à partir des sources du dépôt, sans étiquettes de prototype, avec le menu des chemins et un bouton « Commenter cet écran » qui ouvre la boîte de commentaires de claude.ai, rattachée à l'écran affiché. À trancher : la liste des chemins (tu y réfléchis), l'écran de départ, le partage (qui peut ouvrir et commenter : à vérifier dans le menu « Partager » sur une première version privée). Captures avant toute publication partagée (R6). | toi, puis Claude | ? | 2.6 (les phrases) | forme choisie ; chemins en réflexion |

### 2.3 Le test lui-même, du 16/11 au 18/01

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 2.9 | Recruter cinq personnes hors cible (`PR-2.2`) | toi | 1 h | — | **fait le 02/11** : 2 hommes, 3 femmes |
| 2.10 | Préparer les tâches et les critères, selon le protocole du 20/10, dont une tâche sur le lien de la troisième voie du savon (`PR-2.1`) | Claude | 1 h | 2.5 | à faire |
| 2.11 | Valider la préparation (`PR-2.3`) | toi | 2 h | 2.8, 2.10 | à faire |
| 2.12 | Passer les cinq tests (`PR-2.4`) | toi | 5 h | 2.9, 2.11 | à faire |
| 2.13 | Analyser les résultats (`PR-2.5`) | Claude | 1 h | 2.12 | à faire |
| 2.14 | Lire l'analyse ; corriger les phrases et les repères (`PR-2.6`), puis les reporter dans les planches (Claude) | toi, Claude | 3 h + ? | 2.13 | à faire |

---

## 3. Clore le prototype (`PR-3`, hors étape 8)

### 3.1 Les décisions qui t'attendent

Elles débloquent des modifications de planches. Pour chacune, tu peux répondre en un mot.

| N° | Question | D'où elle vient | État |
| --- | --- | --- | --- |
| 3.1 | « Icône verdict allaitement » (31/10) : qu'est-ce qui doit changer ? | note du 31/10, §5.2 | à trancher |
| 3.2 | L'encadré « réévalué » : combien de temps ? Trois possibilités proposées le 02/11 (fil `19560b13`) : (1) à la première ouverture seulement, recommandée ; (2) jusqu'à ce qu'on le ferme ; (3) un nombre de jours, déconseillé. | fil `907c529c` ; décision 200 ; `D-282` | **tranché le 02/11** : possibilité 1 (« on garde la 1 », fil `19560b13`) |
| 3.3 | La phrase de la bulle de l'échelle : trois propositions, au réglage de `E1-Aide-Echelle` | fil `8192aeeb` | à choisir |
| 3.4 | La taille de l'arc (76 × 40 px) : assez grande ? Plus grand, il faut accepter que le nom du produit passe à la ligne, ou déplacer l'arc | fils `92b44169`, `d9867524` | à trancher |
| 3.5 | Décisions 206 à 209 : ton « ok, go etape 7 » valait-il accord ? | note du 31/10, §5.2 | à confirmer |
| 3.6 | Ta retouche de `E2-Recherche-Aucun` (29/10) : la garder ? la reporter sur les quatre autres copies ? Le filigrane est tranché le 02/11 au soir : le symbole de Ficolia, au milieu de l'espace blanc (« non juste le logo simple », version 39, commit `eac7321`) ; reste son report sur les quatre autres copies. | journal du 29/10, §18 ; fil `99641baa` | à trancher |
| 3.6a | Le verdict « à actualiser » : « Les données de ce verdict… » est flou. Deux formulations proposées le 02/11 (fil `a5b20715`), A (la cause) ou B (ce qui a pu changer), sur 9 planches, et la ligne « Pas de connexion » sur 6. | fil `a5b20715` ; `D-91`, `T-511`, `T-242` | à choisir |
| 3.7 | Fil `0bf17029` (« la phrase est mal formulée », `EA-Verdict-Lait-Sous`) : de quelle phrase s'agit-il ? | inventaire du 02/11 | à préciser |
| 3.8 | Panneau « source » du verdict (« pas intuitif, pas joli », fil `b89f1c0b`) : veux-tu des idées de disposition ? Claude les décrit d'abord, sans rien construire. | inventaire du 02/11 | à trancher |
| 3.9 | Le signal poitrine : `D-273` contre le cap de l'accueil (§2) | journal du 22/10 | à trancher |
| 3.10 | La police du logo : nom, source, licence (`T-558`, `T-636`) | fil `2c39b9fd` ; ta réponse du 02/11 (fil `0940e8c9`) | **répondu le 02/11** : 29LT Riwaya Informal, sous licence ; gardée pour le prototype ; une police gratuite à trouver pour le lancement (§6) |
| 3.11 | **Le plan de l'audit du 18/10.** À trier : ses huit actions P1 « avant les tests ». (1) nommer sur le verdict ce qui détermine le niveau ; (2) les textes des niveaux 2 à 4 (toxicologue, juriste) ; (3) le moment « je l'ai déjà utilisé » ; (4) un écran « Réaction » ; (5) « À propos » et « Méthode » ; (6) le langage courant ; (7) supprimer les impasses de l'étape 3 ; (8) la version de test (tâche 2.8). Certaines ont avancé depuis (par exemple la fusion d'« À propos » et de « Méthode », décisions 206 et 207), mais leur état n'a pas été vérifié une à une. | note du 21/10, plan de l'audit | sans réponse depuis le 21/10 |

### 3.2 Valider les étapes 5 à 7

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 3.12 | Préparer chaque étape et tenir la note de reprise (`PR-3.4`) | Claude | 3 h | — | à faire |
| 3.13 | Valider l'étape 5 : historique, réévaluation, réglages, échelle (`PR-3.1`) | toi | 4 h | 3.12 | à faire |
| 3.14 | Valider l'étape 6 : menu, pages, fiches, « Nous écrire » (`PR-3.2`) | toi | 4 h | 3.12 | à faire |
| 3.15 | Valider l'étape 7 : l'écran de refus des flacons d'huile essentielle pure, construit le 30/10 (`E7-NonEvalue`, décision 211) (`PR-3.3`) | toi | 1 h | — | à faire |
| 3.16 | L'échelle (`PR-3.5`) : tranchée le 30/10, l'arc sans aiguille (décision 213), sous réserve de sa taille (3.4). Coche proposée. | toi | — | 3.4 | à cocher |

### 3.3 Ce qui reste à modéliser

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 3.17 | Le produit déjà utilisé qui passe au niveau 3 ou 4 : premier verdict de niveau 3 ou 4, ou réévaluation d'un produit de l'historique (`T-404` ; audit, action 3) | toi, puis Claude ; toxicologue et juriste pour les textes | ? | 3.11 | à décider |
| 3.18 | Les ajouts du 30/10 (`PR-3.11`) : la limite déterminante au panneau de détail et la version des règles sur la fiche méthode (`PI4-D4`) ; la liste fournie par l'utilisatrice (`PI4-D6`) ; le choix entre les variantes d'un même code (`PI4-D7`). Le fichier de travail du 30/10 qui les définit n'est pas dans le dépôt : seules les définitions du planning sont connues. | Claude, toi | 3,5 h | les définitions | à faire |
| 3.19 | « Type de produit non pris en charge » : on ne l'obtient que par le réglage « Raison » des écrans d'évaluation incomplète. Une planche dédiée, ou le réglage suffit ? | toi | 0,1 h | — | à trancher |
| 3.20 | L'écran « Réaction » (audit, action 4), à décider avec 3.11 | toi, juriste | ? | 3.11 | à décider |
| 3.21 | Les « deux retours manquants » relevés le 21/10 : la note ne dit pas lesquels. À retrouver ou à abandonner. | toi | — | — | à préciser |
| 3.22 | Si le test (§2) retient la voie du savon : poser le renvoi sur les autres planches du même modèle de verdict | Claude | ? | 2.13 | plus tard |
| 3.23 | Plus tard, selon toi : les produits reconnus de la recherche, l'écran de pause, les fiches grossesse (`D-66` à rouvrir) | toi | — | — | plus tard |

### 3.4 Finir

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 3.24 | La séance de design dédiée (`PR-3.6`, `T-373` : « le design est jugé moche, une session dédiée est prévue ») | toi | 4 h | 3.13 à 3.15 | à faire |
| 3.25 | Le contrôle final (`PR-3.7`) : mots interdits, contrastes (4,5:1), cibles de 44 px, texte agrandi, mouvement réduit, liens et boutons, cohérence entre les copies d'un même gabarit, sur les 191 planches | Claude | 2 h | 3.24 | à faire |
| 3.26 | Valider le contrôle final (`PR-3.8`) | toi | 2 h | 3.25 | à faire |

---

## 4. L'étape 8 : inscrire au registre (`PR-3.9`, `PR-3.10`), sur la base du registre v6.8

**Ce que c'est** : faire entrer au registre les décisions de séance du prototype (`D-223`), qui n'y sont pas encore, sauf la décision 86 (`D-334`). Le registre se tient dans la discussion de méthodologie : Claude prépare, tu valides, l'inscription se fait là-bas.

| N° | Tâche | Qui | Durée | Dépend de | État |
| --- | --- | --- | --- | --- | --- |
| 4.1 | Compléter le relevé des écarts au registre (`propositions/2026-10-31-hors-canevas/ecarts-au-registre-etape-8.md`, décisions 182 à 217) avec les choix des 01 et 02/11 : savon, « Crevasses », bandeau grisé, idée 5, boutons, piste (a), « Accepter », tenue du slogan… | Claude | ? | 1.6 | **peut commencer** |
| 4.2 | Confronter l'annexe A de la note du 21/10 (177 lignes) au registre v6.8, ligne à ligne | Claude | ? (le planning ne compte que 2 h pour tout `PR-3.9`, ce qui semble court ; à réestimer après les 20 premières lignes) | — | **peut commencer** |
| 4.3 | Rédiger la note d'inscription : les décisions de séance, la correction de la palette de verdict de `D-107`, et la mise à jour de `D-312` (le canevas de référence est maintenant le canevas de travail) | Claude | 2 h | 4.1, 4.2, et le §3 | à faire, en dernier |
| 4.4 | Valider l'inscription (`PR-3.10`) | toi | 2 h | 4.3 | à faire |
| 4.5 | Quand la v6.9 arrive : repasser le relevé sur ce qu'elle change par rapport à la v6.8 | Claude | ? | la v6.9 | en attente |

**Pourquoi 4.3 vient en dernier** : chaque décision prise au §3 serait sinon à ajouter après coup. Les tâches 4.1 et 4.2 peuvent commencer tout de suite.

---

## 5. Les tests avec la cible (`PR-4`), plus tard

**Pas avant** :
- la juriste. `JU-1` : relire l'additif (`JU-1.3`), l'envoyer (`JU-1.4`), le rendez-vous. Puis `JU-2` : intégrer ses réponses ;
- le cadre juridique du recrutement (`T-464`) : recruter revient à recueillir des informations qui révèlent une grossesse ;
- la forme des tests, à fixer (`PI-4.4`, `T-508`) : sur le prototype, par installation directe sur Android, ou par une piste de test d'un store ;
- la clôture du prototype (§3).

Scénario central du planning : juillet à septembre 2027.

| N° | Tâche | Qui | Durée |
| --- | --- | --- | --- |
| 5.1 | Fixer la forme des tests (`PI-4.4`, `T-508`) | toi | 0,5 h |
| 5.2 | Protocole et critères d'acceptation fixés d'avance (`PR-4.1` ; `T-398`, `T-541`, `T-540`) | Claude | 1 h |
| 5.3 | Valider le protocole (`PR-4.2`) | toi | 2 h |
| 5.4 | Recruter les testeuses (`PR-4.3`, `T-414`) | toi | 4 h |
| 5.5 | Passer les tests (`PR-4.4`) | toi | 8 h |
| 5.6 | Analyser (`PR-4.5`) | Claude | 1 h |
| 5.7 | Lire l'analyse ; décider des corrections (`PR-4.6`) | toi | 4 h |

**Deux questions du planning à porter à la juriste** (`JU-1.3`) :
- le savon sort du verdict : un lien vers une fiche « Bonnes pratiques » sous le verdict compte-t-il comme un appel à l'action ?
- le flacon d'huile pure n'aura plus de verdict au lancement (« Ficolia n'évalue pas ce type de produit. »).

---

## 6. Hors du prototype, à garder en tête

- **La police du logo** (02/11) : 29LT Riwaya Informal, sous licence, gardée pour le prototype ; une police gratuite à trouver pour le lancement, ou une licence à acheter (`T-636`). Changer de police, c'est changer le lettrage du logo : la révélation, les vidéos d'ouverture exportées et les maquettes du récit et du site seraient à refaire. Aucun fichier de la police n'est dans le dépôt ni sur le canevas (vérifié le 02/11).
- **Le récit de la figue** (`PASSATION.md`) : l'écran de chargement court des lancements suivants, à proposer ; la chair de la figue jusqu'à la queue, à étendre ou non ; les choix des 22 et 29/10, à inscrire dans le cap de l'accueil.
- **Le site vitrine** : il attend tes réponses et ton feu vert.
- **Les relectures** : la toxicologue (calendrier `D-310`, premier envoi le 23/11), la juriste, les phrases des niveaux (`D-105`).

---

## 7. Message à coller dans la conversation du planning

> Mise à jour du 02/11 (session du prototype) :
> 1. Canevas de référence (PR-1) : depuis le 01/11, le travail se fait sur un canevas neuf, « ficolia - prototype_vTravail » (https://claude.ai/artifact/FB6cC6xawyir9Y1QwCYosb), reconstruit depuis les exports. Claude le lit et le modifie. L'original, « Ficolia — Prototype », reste en archive avec ses commentaires (139 fils, dont 30 ouverts, inventoriés le 02/11). La question « Canevas refusé à Claude » est réglée ; D-312 est à annoter de nouveau.
> 2. Faits, à cocher :
>    - PR-1.3 : réponses aux commentaires préparées (31/10), inventaire des 139 fils de l'original (02/11) ;
>    - PR-1.5 : déclencheur du renvoi « Crevasses », première lecture (02/11) ;
>    - PR-1.6 : troisième voie du savon prototypée et publiée (02/11) ;
>    - PR-1.7 : le lien de la troisième voie, si mon « ok » du 02/11 vaut validation ;
>    - PR-2.2 : cinq personnes hors cible recrutées, 2 hommes et 3 femmes (02/11) ;
>    - PR-3.5 : échelle choisie, l'arc sans aiguille (décision 213, 30/10 ; reste sa taille).
> 3. Tranché le 02/11 :
>    - tenue du slogan à 2 s ;
>    - police du logo : 29LT Riwaya Informal, sous licence, gardée pour le prototype ; une police gratuite à trouver pour le lancement (T-636, T-558) ;
>    - dépôt public et données de la personne extérieure : j'ai eu l'autorisation ; la question du 31/10 est close ;
>    - forme du test hors cible (PR-2) : un lien à envoyer, qui ouvre le prototype comme une application téléchargée, en navigation libre, avec un menu pour lancer les chemins critiques à tester.
> 4. Sous-tâches à ajouter :
>    - CT-1 ou PR-2 : reporter les phrases figées dans les planches (Claude) ;
>    - PR-2 : construire la version de test (Claude), puis la valider (moi) ;
>    - CT ou PR-2 : reformuler les mentions de la ligne allaitement et leurs explications (propositions du 02/11, choix attendu) ;
>    - PR-3 : choisir la formulation du verdict « à actualiser » (proposition du 02/11) ; la durée de l'encadré « réévalué » est tranchée (possibilité 1, 02/11).

---

## 8. Limites de cette liste

- **Le registre** : elle repose sur la v6.8. La v6.9 peut avoir inscrit ou changé des entrées citées ici.
- **Le planning** : c'est l'état du 31/10 au soir. Ses dates supposaient le canevas débloqué avant la semaine du 14/12 ; il l'est depuis le 01/11, ce qui devrait permettre d'avancer `PR-1`, donc `PR-2`. Ce n'est pas recalculé ici.
- **Le fichier du 30/10** (`a_inscrire_registre_30_10_2026.md`, qui porte `O-65`) et le fichier de travail du PI-4 restent introuvables. Les définitions de `PI4-D4`, `D6` et `D7` ne viennent que du planning.
- **Les actions de l'audit** (3.11) et les questions du 31/10 (3.1 à 3.10) n'ont pas été revérifiées une à une sur les planches. Tu as pu en trancher sur la page depuis.
- **Les durées marquées « ? »** ne sont pas estimées. Les autres sont celles du planning.
