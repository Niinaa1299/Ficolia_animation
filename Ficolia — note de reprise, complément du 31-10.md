Ficolia · prototype · document interne

# Ficolia — Prototype : complément à la note de reprise du 21/10

31 octobre 2026 · décisions 182 à 217, état du canevas et de ses commentaires, ce qui reste à faire · écrit sans accès au canevas · document interne

**Ce complément se lit après la note de reprise du 21/10** (`Ficolia — note de reprise.md`, à la racine du dépôt). Il ne la remplace pas et ne la modifie pas : la note reste telle quelle, pour ne rien écraser (règle de la porteuse, 31/10). Ce qui suit complète la note, ou la corrige là où les choses ont changé depuis le 21/10.

**Sources**, toutes dans le dépôt, branche `claude/relaxed-noether-g2fdj1` :

- `propositions/2026-10-22-reprise/journal-22-10.md` : séance du 22/10, décisions 182 à 186 ;
- `propositions/2026-10-29-page-par-page/journal-29-10.md` : revue page par page du 29 au 31/10, décisions 187 à 217 (§1 à §39) ;
- `propositions/2026-10-22-reprise/fils-ouverts.md` et `propositions/2026-10-22-reprise/commentaires-23-24-10.md` : les fils relus les 22 et 26/10 ;
- le registre v6.7 (`main`), lu pour les seules entrées citées ;
- lus le 31/10 : la fiche du canevas, ses fils envoyés à Claude, et le message d'erreur de l'outil du canevas dans la session précédente.

Dans ce complément, « journal » sans autre précision désigne le journal du 29/10, et « note » la note de reprise du 21/10.

**Deux documents l'accompagnent**, dans `propositions/2026-10-31-hors-canevas/` :

- `ecarts-au-registre-etape-8.md` : les écarts au registre nés depuis le 21/10, à inscrire à l'étape 8 ;
- `reponses-commentaires.md` : l'état de chacun des fils ouverts au 29/10, avec une réponse proposée.

Sommaire

1. [État au 31/10](#1-état-au-3110)
2. [Décisions 182 à 217](#2-décisions-182-à-217)
3. [Décisions révisées ou remplacées depuis le 21/10](#3-décisions-révisées-ou-remplacées-depuis-le-2110)
4. [Les questions du 21/10 : où elles en sont](#4-les-questions-du-2110--où-elles-en-sont)
5. [Ce qui reste à faire](#5-ce-qui-reste-à-faire)
6. [Commentaires du canevas](#6-commentaires-du-canevas)
7. [Consignes ajoutées depuis le 21/10](#7-consignes-ajoutées-depuis-le-2110)
8. [Limites de ce complément](#8-limites-de-ce-complément)

---

## 1. État au 31/10

### Le canevas

- **Lien et propriété** : inchangés (note, §1). Le canevas est privé. Le compte des sessions Claude Code depuis le 22/10 en est le propriétaire.
- **Version en ligne** : **1793448707-c41e**, enregistrée depuis la page le 31/10 à 12 h 11 UTC.
- **Dernière publication de Claude** : version 420 (1793398495-9fc2), le 30/10 à 22 h 14 UTC (journal, §35).
- **Deux enregistrements depuis la page ont suivi** : 1793447226-0a4e (31/10, 11 h 47 UTC), puis 1793448707-c41e (12 h 11 UTC). Leur contenu n'a pas été lu. Retouches de la porteuse ou mise à jour du type de canevas, comme le 21/10 (note, §1) : on ne sait pas.
- **L'identifiant de version donne l'heure d'enregistrement**, en secondes depuis le 1er janvier 1970. 1793448707 correspond au 31/10, 12 h 11 min 47 s UTC, à une seconde près de la date de mise à jour donnée par le service. Les identifiants des versions 365, 417 et 420 tombent aussi une à deux minutes avant les envois au dépôt qui les rapportent.
- **Planches** : 212 relues le 29/10 au soir (journal, §19). Ensuite, d'après le journal, 7 ajoutées en version 395 (§20) et 1 en 409 (§29), et 1 retirée par la porteuse avant la 409 (`EA-Verdict-Renvoi-Pastille`, §29). Cela fait environ 219 planches à la version 420. Ce nombre est déduit, pas compté.
- **Copies** :
  - La seule copie complète connue est l'archive du 22/10, remise à la porteuse, qui la garde en local (journal du 22/10, §2) : version 1792536570-62b1, d'avant la publication 344, avec l'index, les 193 planches et les 49 fichiers de la réserve.
  - Elle n'est pas dans le dépôt, qui est public. Elle ne contient ni les commentaires ni l'historique des versions.
  - Il n'existe aucune copie des versions suivantes. Les dossiers de travail des séances (`.travail/`, scripts, copies de référence) étaient dans des conteneurs qui ne durent pas.

### L'accès depuis Claude Code, le 31/10

- **L'outil habituel du canevas est coupé.** Le journal le dit dès le 31/10 au matin (§36 : « L'outil de publication habituel est désactivé dans cette session »).
  - Dans la session « Ficolia prototype », le 31/10 à 12 h 31 UTC, l'appel à l'outil « Artifact » a reçu cette réponse : « Artifact is still listed for this conversation but is switched off in this session right now, so it cannot run. »
  - Dans la session suivante, ouverte à 12 h 33 UTC, il n'est plus proposé du tout.
  - La cause et la date de retour ne sont pas connues. Aucun réglage connu, côté porteuse, ne le rallume.
- **Le second outil, le serveur d'artefacts**, lit la fiche du canevas (titre, version, propriétaire), mais refuse ses fichiers :
  - message : « this artifact was made from an artifact type: this tool serves one only to the user who owns it, and not once anyone outside their organization has written to it. No tool here reads its files. Do not send files to it: the user changes it on its own page » ;
  - le compte Claude Code d'une autre organisation a publié les versions 280 à 342 (note, §1) : ce refus est donc sans doute durable ;
  - l'autre canevas du compte, « Ficolia — Prototype (v.6) », est refusé de la même façon.
- **Commentaires** :
  - le second outil ne lit que les fils envoyés à Claude ;
  - un fil non envoyé répond « not found », même demandé par son identifiant exact (essayé sur `b61eb6d5` et `68ef4661`, avec un fil envoyé en témoin) ;
  - un seul message envoyé à Claude dans un fil rend tout le fil lisible, messages anciens compris (constaté sur `6c55f949`) ;
  - Claude peut répondre dans un fil envoyé : la session précédente l'a fait le 31/10 dans `6c55f949`.
- **Pour savoir si l'outil est revenu** : dans une nouvelle session, demander « Peux-tu lire le canevas Ficolia, sans rien modifier ? ».

### Le dépôt

- Branche de travail du prototype depuis le 22/10 : `claude/relaxed-noether-g2fdj1`. Elle porte les journaux, les listes de fils et ce complément.
- Autres branches :
  - `claude/ecstatic-lamport-qjpucd` : le travail jusqu'au 22/10, dont la liste de fin de session ;
  - `claude/compassionate-shannon-qu70ot` : les animations et `cap-onboarding.md` ;
  - `claude/happy-mccarthy-5akhfh` : les exports de l'ouverture et de l'accueil pour le prototype (29/10).
- Le registre v6.7 est sur `main`.
- Le dépôt est public (note, §6).

---

## 2. Décisions 182 à 217

Elles sont numérotées à la suite de la note, qui s'arrête à 181. Les décisions 182 à 186 sont dans le journal du 22/10, les 187 à 217 dans celui du 29/10.

Sur le canevas, le journal nomme la note qui porte la plupart des décisions 187 à 216, mais pas pour la 193, la 198 et la 199. Pour 182 à 186, le journal du 22/10 ne le dit que pour la 184. La 217 n'a pas pu être posée sur le canevas.

Le détail des effets sur le registre est dans `propositions/2026-10-31-hors-canevas/ecarts-au-registre-etape-8.md`.

| # | Décision | Date | Sur le canevas | Effet sur le registre ou le dossier |
| --- | --- | --- | --- | --- |
| 182 | L'étude allaitement suit les textes du registre du 20/10 (`D-256` à `D-260`, `D-275`, `D-161`), étiquette « Contact rapproché » comprise | 22/10 | version 344 | aligne l'étude sur le registre ; textes remplacés le 30/10 par la 215 |
| 183 | Savon : la décision 168 est maintenue, la condition savon reste hors du verdict ; la fiche « Toilette des seins » reste, à écrire | 22/10 | — | `D-262` à réviser dans la discussion de méthodologie, où se tient le registre, avec `D-265`, `D-266` et `T-605` |
| 184 | Question du type : piste (a), un type suggéré à confirmer, la liste en secours. Sans réponse, rien n'est supposé (« autre » par défaut) | 22/10 | version 348 : `E3-QuestionSuggeree`, `E3-QuestionSuggeree-Recherche` ; pas encore reliées au scanner, à la recherche ni à l'historique | écart de forme à `T-442` ; règle à écrire : jamais un type suggéré moins exposant que ce que dit le nom (`D-49`) |
| 185 | Accueil en deux écrans pour le prototype | 22/10 | construit le 29/10, version 368 | voir 192 ; `D-273` attend la décision de la porteuse |
| 186 | Prise en main guidée : trois conseils | 22/10 | version 349 | complétée par la 187, révisée par la 193 |
| 187 | Prise en main : quatre conseils, chacun une seule fois, jamais deux à la fois (Rechercher au premier lancement, « i » au premier verdict, Historique au premier retour, Menu au deuxième retour) ; textes retenus le 29/10, provisoires | 29/10 | versions 365 et 366 | révisée par la 193 |
| 188 | Liste des ingrédients : le repère « Signalé » est retiré | 29/10 | dans les planches d'idées seulement | écart à `D-112` (A1 : « repère neutre ») et à la décision 27 |
| 189 | Chaque ingrédient qui détermine le niveau porte le repère « Détermine ce niveau » (fil `53d81c43`) | 29/10 | dans les planches d'idées seulement | applique `D-112` (A1) |
| 190 | Écran d'attente allaitement : réponse « a puis c » (fil `ac01e1a4` : l'échelle manque sur cet écran) | 29/10 | non dit par le journal | énoncé exact sur la note « Décisions de séance — étape 1 », non recopié dans le journal ; dépassée en pratique par la 217, qui remplace ces écrans |
| 191 | Ouverture et accueil en deux écrans : voir la colonne de droite | 29/10 | version 368 | le journal ne donne pas l'énoncé de la 191 à part (§11) ; sans doute l'ouverture et l'accueil eux-mêmes : placement A, textes de l'export, « Retour » des huit pages légales vers le 2/2. À vérifier sur la note du canevas |
| 192 | Au 2/2 de l'accueil, une seule limite : « Les verdicts sont établis pour une grossesse physiologique. » ; le reste ailleurs | 29/10 | version 368 | écart à `D-114` (C7) et à `D-273` (journal, §11) ; déjà noté comme écart à tracer par `cap-onboarding.md`, §2 |
| 193 | Prise en main, révise la 187 : au premier verdict, la bulle pointe vers le « i » ; au deuxième verdict, une bulle sur l'échelle. Ordre des moments : Rechercher, « i », échelle, Historique, Menu | 29/10 | versions 369 et 373 | phrase de l'échelle : trois propositions en attente (§14), à revoir depuis l'arc (213) |
| 194 | Recherche, « Aucun résultat » : les deux boutons sont retirés ; une phrase invite à scanner le produit pour aider à l'ajouter, au réglage « Invitation à photographier la liste (option) », activé par défaut ; pas d'image | 29/10 | version 388 ; `E2-Produit`, oubliée, en 403 | revient sur les décisions 32 et 147 ; le réglage suit `D-113` (B2) |
| 195 | Verdict à actualiser : le bouton « Actualiser » est retiré ; titre « Verdict non affiché pour l'instant » (proposition) ; phrase A | 29/10 | version 395 | revient sur la décision 58 ; libellé à confronter à `T-511` (« verdict à actualiser ») |
| 196 | Les états du verdict sont reliés au parcours : scans simulés, écrans produit et listes propres à chaque état ; libellé « Non reconnu » | 29/10 | version 395 | libellé nouveau, provisoire ; à confronter à `D-112` (A3) |
| 197 | Vérification globale des liens, en fin de revue | 29/10 | à faire | demandée de nouveau le 31/10 (§36) |
| 198 | Signalement « Ce n'est pas le bon produit » : nom et marque du bon produit obligatoires, photos facultatives | 29/10 | version 402 | nouveau. Limite : qui ne peut lire ni le nom ni la marque ne peut plus signaler cette erreur |
| 199 | « C'est noté » (e-mail enregistré) reçoit l'animation « La figue s'incline » | 29/10 | version 402 | nouveau ; la même figue sert à deux confirmations |
| 200 | L'encadré « Ce produit a été réévalué. » passe sur une ligne, à la même place | 30/10 | version 403 | conforme à `D-282`. Durée, première ouverture seulement : proposition de Claude, à confirmer |
| 201 | Recherche sans connexion : « En attendant, vous pouvez scanner : si le produit ne s'affiche pas, votre scan est gardé. Le résultat s'affichera dans l'historique au retour de la connexion. » | 30/10 | version 403 | — |
| 202 | Les quatre choix de construction du 08/10 (étape 5) sont confirmés | 30/10 | version 403, note `etatE5` | — |
| 203 | Chaque fiche « Bonnes pratiques » porte le rappel général, là où son texte en a besoin | 30/10 | version 406, sur la fiche « Crevasses » | cinquième endroit pour `D-114` (C8), que permet `O-27` ; revient sur la construction de la décision 155 |
| 204 | Aucune formule sur la méthode ; à sa place, « [Présentation générale de la méthode, sans entrer dans le détail — à rédiger] » | 30/10 | version 406 | la formule de la toxicologue (`T-320`) n'est plus affichée ; avec elle, « Ce n'est pas un avis médical. » quitte la page de la méthode |
| 205 | « Une erreur sur un produit se signale depuis la fiche de verdict. » | 30/10 | version 406 | — |
| 206 | Menu, dans l'ordre : Réglages, Bonnes pratiques, À propos et méthode, Nous écrire, Revoir la prise en main | 30/10 | version 407 | « ok, go etape 7 » a été lu comme un accord : lecture signalée à la porteuse (§27) |
| 207 | « À propos » et « Méthode » forment une seule page | 30/10 | version 407 ; l'ancienne planche « À propos » est marquée « À SUPPRIMER » | écart au dossier de conception (§3.2 : deux entrées) ; même lecture que la 206 |
| 208 | Réglages : l'interrupteur des alertes couvre aussi les produits maintenant évalués ; une section « Caméra » dit l'état de l'autorisation et ouvre les réglages du téléphone | 30/10 | version 407 | suit `D-114` (C1) ; pas de notification du téléphone (`T-224`) ; même lecture que la 206 |
| 209 | Les choix de construction du 09/10 (étape 6) sont confirmés | 30/10 | version 407 | même lecture que la 206 |
| 210 | L'aromathérapie sort de l'analyse au plancher : seuls les flacons d'huile essentielle pure sont concernés ; un cosmétique qui en contient reste évalué | 30/10 | version 409 | entrées à revoir : `D-57`, `D-113` (B6), `D-114` (C11), `D-217`, `T-431`, `T-453`, `T-416`, `L-87` |
| 211 | Nouvel écran `E7-NonEvalue` : « Ficolia n'évalue pas ce type de produit. » ; les scanners proposent le résultat simulé « Huile essentielle pure » | 30/10 | version 409 | remplace, au plancher, le parcours des décisions 148 à 151 |
| 212 | Les quatre planches de l'étude de l'étape 7 restent, sous le titre « Hors plancher (30/10) » | 30/10 | version 409 | — |
| 213 | L'arc sans aiguille remplace les paliers, sur les 49 écrans vivants qui les portaient (76 × 40 px) | 30/10 | version 417 | révise la forme de la décision 3 ; tranche entre les variantes (144, 163) ; `T-220` respectée : le secteur du niveau est plus épais et cerné d'encre |
| 214 | Ligne allaitement : des cases égales sous le cadre du verdict, sous le titre « À savoir sur ce verdict » ; un pictogramme, un sujet et son état par case ; tout sur l'écran du verdict, plus de plafond, rien en tête de la liste des ingrédients ; taille des cases au réglage « Cases » | 30/10 | version 420 | écarts à `D-165`, `D-265` et G1.7 (plafond de deux, surplus en tête de liste), à `D-256` (la case porte une forme courte) |
| 215 | Textes de la ligne allaitement en mots simples, provisoires (`T-604`) | 30/10 | version 420 | écarts aux textes de `D-257` à `D-260` et de `D-275` (« zone de tétée », « nourrisson », « contact rapproché », « cette évaluation ») |
| 216 | Renvoi « Crevasses » : le petit rond sur la photo par défaut ; une bulle à la première utilisation ; l'ancienne pastille devient une case parmi les autres | 30/10 | version 420 | aucun écart relevé par le journal |
| 217 | Clôture du volet allaitement au prototype : la ligne allaitement entre dans le parcours principal | 31/10 | non appliquée : canevas inaccessible | revient sur la décision 13 ; statut « module non clos » de l'annexe A.8 à revoir ; ne clôt pas le module au registre (§5.4) |

**Choix de la porteuse sans numéro**, à numéroter quand ils seront posés sur le canevas :

- **30/10, écran des ingrédients** : l'idée 5 « à plat », sur fond `#FAFAFA` (journal, §33 et §34 : « oui »). Non appliqué.
- **31/10, cases de la ligne allaitement** : « Largeur partagée » par défaut (§36 : « taille des cases) largeur partagées »). Non appliqué.
- **29/10, tenue du slogan** : 3 s par défaut, au réglage (§15). C'est une proposition de Claude, publiée en 377 ; le fil `778d3ee5` reste ouvert.

---

## 3. Décisions révisées ou remplacées depuis le 21/10

- La **3** (échelle en paliers) est révisée par la **213** (l'arc sans aiguille). Les variantes D (144) et E (163) ne sont plus que des traces.
- La **13** (écran d'attente allaitement jusqu'à la clôture) est remplacée par la **217**, qui n'est pas encore appliquée.
- La **27** (« Signalé » en étiquette neutre) est révisée par la **188**, appliquée aux seules planches d'idées.
- La **32** et la **147** (deux sorties sur « Aucun résultat ») sont remplacées par la **194**.
- La **47** est fermée au registre par `D-280` (accord exprès du 21/10, déjà porté par le registre v6.7).
- La **58** (« Actualiser » affiche le verdict) est remplacée par la **195**.
- Les **148 à 151** (parcours de l'huile essentielle pure) sortent du plancher par les **210 à 212**. Leurs planches restent, comme étude « hors plancher ».
- La **155** : sa construction (rappel général) est révisée par la **203**.
- Les **165** et **169** (libellés « Contact peau à peau » et « Inhalation par le nourrisson ») sont remplacées par les textes du registre (**182**), eux-mêmes remplacés par la **215**.
- La **167** (forme du renvoi « Crevasses ») est révisée par la **216**.
- La **168** (condition savon retirée du verdict) est maintenue par la **183**.
- Les **181** et **186** (prise en main en trois conseils) sont complétées par la **187**, elle-même révisée par la **193**.

---

## 4. Les questions du 21/10 : où elles en sont

Les quatorze questions du §4.1 de la note, dans leur ordre.

| N° | Question (note, §4.1) | Où elle en est au 31/10 | Source |
| --- | --- | --- | --- |
| 1 | Échelle du verdict | Tranchée : l'arc sans aiguille (213), publié en 417 sur 49 écrans | journal, §33 et §34 |
| 2 | Forme du renvoi « Crevasses » | Tranchée : le petit rond sur la photo, avec une bulle au premier usage (216), publié en 420 | §30, §31, §35 |
| 3 | Fiche « Toilette des seins » | Gardée, à écrire (183). Le 31/10, PR-1.6 propose un lien des nettoyants vers une fiche, en tension avec la décision 168 (§37) | journal du 22/10, §7 ; §37 |
| 4 | Panneau « source » d'une mention | La forme en cases garde le volet de l'ancienne forme B : étiquette, explication, source (214). Le fil `b89f1c0b` (« pas intuitif, pas joli ») est à rejuger sur la version 420 | §35 |
| 5 | Produits reconnus de la recherche | Ouverte : « repose moi la question plus tard » (22/10) | journal du 22/10, §7 |
| 6 | Question du type, autres formes | Piste (a) retenue (184), construite en 348. Le 22/10, ses planches n'étaient pas encore reliées au scanner, à la recherche ni à l'historique ; rien dans le journal du 29/10 ne dit que ce soit fait | journal du 22/10, §7 et §8 |
| 7 | Écran de pause | Laissé en l'état : « laisse comme ca pour l'instant » (22/10) | journal du 22/10, §7 |
| 8 | Rappel général sur les fiches | Tranchée : un rappel sur chaque fiche (203), posé sur « Crevasses » en 406 | §26 |
| 9 | Image fixe pour « réduire les animations » | Traitée dans la discussion des animations (22/10). Le 29/10, la porteuse ouvre le chantier des images fixes tirées des animations (§18) | journal du 22/10, §7 ; §18 |
| 10 | Prise en main guidée | Faite : trois conseils (186), puis quatre (187), puis cinq moments (193). La phrase de la bulle de l'échelle attend un choix (§14) | journal du 22/10, §8 ; §3 à §14 |
| 11 | Actions P1 de l'audit | Pas de réponse au 22/10. Le 29/10, A1, A2 et A6 sont toujours en attente pour l'étape 1 | journal du 22/10, §7 ; §7 |
| 12 | Fiches grossesse | « en brainstorming coté chat » (22/10) | journal du 22/10, §7 |
| 13 | Accueil | Deux écrans (185), construits en 368 (191, 192) ; ouverture rejouée par la planche (373) ; tenue du slogan (377). `D-273` attend la décision de la porteuse | §9 à §15 ; journal du 22/10, §10 |
| 14 | Annexe pour la juriste | Le 22/10, l'additif au dossier juriste (`T-610`) n'était pas parti. L'annexe du prototype suit avec lui, en retard sur les textes allaitement et sur `D-104`. Un rappel était programmé le 23/10. Le dépôt n'en dit pas plus | journal du 22/10, §9 |

---

## 5. Ce qui reste à faire

### 5.1 Au canevas, dès que l'outil revient

Dans cet ordre, d'après le journal (§34 à §39), avec les règles de la porteuse : ne rien écraser ni supprimer, lire la version en ligne avant chaque publication, ne publier que les planches modifiées, montrer les rendus avant de publier.

0. **Relire avant tout** : la version en ligne, l'index, les notes et les fils.
   - La porteuse a enregistré deux fois depuis la page le 31/10.
   - Faute de copie de la version 420, une retouche ne se repérera pas en comparant des empreintes.
   - Lui demander ce qu'elle a changé, et relire en entier les planches à modifier.
1. **Cases de la ligne allaitement en « Largeur partagée » par défaut**, sur les 9 verdicts vivants de l'étude (§36).
2. **Écran des ingrédients, idée 5 « à plat »**, sur toutes les listes vivantes, grossesse et allaitement, y compris les trois listes d'état de l'étape 3 (§36) :
   - fond `#FAFAFA`, verdict rappelé en tête, barre d'onglets blanche ;
   - ni ombre ni carte, sauf l'encadré du produit ;
   - avec les décisions 188 et 189, appliquées jusqu'ici aux seules planches d'idées (journal, §5) ;
   - les planches de comparaison (`E1-Ingredients-Idee1` à `Idee5`) et les traces restent telles quelles.
3. **Clôture du volet (217)** (§38) :
   - relever les écrans d'attente allaitement et leurs listes aux étapes 1, 2 et 5, avec leurs copies ; l'étape 7 n'a plus de ligne allaitement depuis la 210 ;
   - les remplacer par le gabarit de l'étude pour le lait corps : cases en largeur partagée, arc, renvoi, textes marqués provisoires, listes à l'idée 5 avec l'arc ;
   - donner un vrai verdict à l'écran d'attente réévalué de l'étape 5 ;
   - liens : écran produit, puis verdict allaitement, puis liste ; les retours mènent au parcours principal, non à l'étude ;
   - la page d'étude reste, comme référence de ses réglages.
4. **« Icône verdict allaitement »** : lecture à confirmer avec la porteuse avant d'agir (§36).
5. **Écart entre le bouton « Ce n'est pas ce produit » et la ligne Allaitement**, sur tous les écrans produit qui portent les deux (§39) :
   - mesurer en texte standard, à 130 et à 200 % ;
   - poser le même écart partout, aligné sur l'espacement entre les blocs ;
   - montrer l'avant et l'après ;
   - le premier message du fil `6c55f949` (29/10, sur `E3-Produit-TypeAPreciser`) disait aussi : « le bouton est trop collé a l'encadré du haut ».
6. **Liens (197)**, demandés de nouveau le 31/10 : « assure toi que toutes les connexions possibles entre écrans soient faites » (§36). Vérifier :
   - les cibles existantes et les retours ;
   - la barre d'onglets ;
   - les boutons sans action ;
   - puis poser les liens manquants, dont le chemin allaitement du point 3.
7. **`E0-Fondations` et `E0-Polices`** : l'arc à la place des paliers (§34). Plus largement, la page « Fondations » (liste de fin de session, point 3).
8. **Petite dette connue** : dans 22 planches, des commentaires du code parlent encore de « palier allumé », sans effet à l'écran (§34).

### 5.2 Questions qui attendent la porteuse

1. **« Icône verdict allaitement »** (31/10) : que faut-il changer ? (§36)
2. **Durée de l'encadré « réévalué »** (200) : la marque ne paraîtrait qu'à la première ouverture du verdict après le changement. Proposition de Claude, à confirmer (§24).
3. **Phrase de la bulle de l'échelle** : trois propositions (§14). L'image des niveaux étant arrêtée (213), il reste à choisir.
4. **Taille de l'arc** : 76 × 40 px, la plus grande qui ne déplace rien à l'écran. Pour un arc plus grand, il faut accepter le retour à la ligne du nom, ou déplacer l'arc. À trancher si c'est trop petit, notamment au regard du « rapport de taille » du fil `92b44169` (§34).
5. **Décisions 206 à 209** : « ok, go etape 7 » a été lu comme un accord. La lecture a été signalée à la porteuse ; sa réponse n'est pas connue (§27).
6. **Retouche de `E2-Recherche-Aucun`** par la porteuse (29/10) : message centré, bloc de 101 px de haut, phrase de contribution sortie du réglage. La garder ? La reporter sur les quatre autres copies ? (§18)
7. **PR-1.6, lien des nettoyants vers une fiche** : couleurs, plafond, place et texte, avec les recommandations provisoires de Claude (§37).
   - Le fichier du 30/10 qui la décrit (`claude/registre_travail/a_inscrire_registre_30_10_2026.md`) est introuvable.
   - PR-1.5 renvoie à `O-65`, qui n'est pas dans le registre v6.7.
8. **`D-273` contre `cap-onboarding.md`, §2** : où mettre le signal poitrine (journal du 22/10, §3 et §10).
9. **Actions P1 de l'audit** (A1 à A8).
10. **Police du logo** : nom, source et licence (`T-558`). La porteuse cherche (29/10, §14).
11. **Fil `0bf17029`** (« la phrase est mal formulée ») : quelle phrase ?
12. **Plus tard**, d'après la porteuse : les produits reconnus de la recherche, l'écran de pause, les fiches grossesse.
13. **Tenue du slogan** : 3 s par défaut. « Continuer » paraît alors à 11 s, ce qui allonge l'écart au cap (§15).

### 5.3 Écrans qui restent à modéliser

Réponse, d'après le dépôt, à la question de la porteuse du 31/10 : « reste-il des écrans à modéliser ? ou en sommes-nous ? » (§36). Le canevas n'a pas pu être relu : cette liste vient des journaux et de la note, pas des planches.

- **Décidés, pas encore construits** :
  - le parcours allaitement principal (217) : le verdict allaitement du lait corps aux étapes 1, 2 et 5 et dans leurs copies, sa liste, et l'écran réévalué de l'étape 5 avec un vrai verdict ;
  - l'idée 5 sur toutes les listes ;
  - les cases en largeur partagée.
- **Relevés au 21/10, sans trace de construction depuis** (liste de fin de session, point 16) :
  - le produit déjà utilisé qui passe au niveau 3 ou 4 ;
  - « deux retours manquants », que la note ne précise pas ;
  - le troisième, la ligne allaitement du flacon pur, est sans objet depuis la 210.
- **Proposés par l'audit, non décidés** : l'écran « Réaction » ; le moment « je l'ai déjà utilisé », le même que ci-dessus ; une version de test sans étiquettes de prototype.
- **En discussion** : le lien des nettoyants vers une fiche (PR-1.6) ; le déclencheur du renvoi « Crevasses » (PR-1.5).
- **Fiches à écrire plutôt qu'à dessiner** : « Toilette des seins » (183) ; les fiches grossesse, dont la liste reste à arrêter.
- **Chemins manquants connus** :
  - « Type non pris en charge » ne s'obtient que par un réglage (journal, §20) ;
  - la question du type (184) n'était pas reliée au scanner, à la recherche ni à l'historique le 22/10.
- **Images fixes tirées des animations** : chantier ouvert le 29/10, dans la discussion des animations.

### 5.4 Validations dues, que la clôture du volet ne change pas

D'après le journal, §38 :

- les phrases des niveaux, par la porteuse (`D-105`) ;
- la toxicologue, après l'étalon (`D-250`), puis la juriste ;
- les tests de formulation (`D-159`) ;
- l'état « non évaluable » (`O-31`) ;
- la revue du bloc G ;
- les points `O-52` à `O-57` ;
- au registre, à l'étape 8 : la révision de la décision 13 et le statut « module non clos » (annexe A.8).

Le registre v6.7 dit déjà `O-31` et `O-52` à `O-56` « fermés » (13 et 15/10), certains à titre provisoire. `O-57` est ouvert. La liste du journal reprend celle de la note (§5) ; elle est à confronter au registre à l'étape 8.

### 5.5 La liste de fin de session du 21/10 : ce qui a bougé

La liste est sur `claude/ecstatic-lamport-qjpucd` (`propositions/A-FAIRE-fin-de-session.md`) et dans la note (§5). Seuls les points qui ont bougé d'après les journaux sont repris ici. Les autres sont sans trace de changement.

| N° | Point | Ce qui a bougé |
| --- | --- | --- |
| 2 | Note d'état de la page « Étape 6 » | mise à jour le 30/10, version 406 (journal, §26) ; à relire pour savoir si elle décrit encore les tuiles |
| 3 | Page « Fondations » | toujours à faire ; s'y ajoute l'arc (§34) |
| 4 | Planches « Traçabilité » | `E0-Trace-2`, ligne `T-320` : « Non affichée » (204) ; le reste, toujours à faire |
| 5 | Accueil et son animation | faits le 29/10 depuis les exports (368 à 377). Logo : « vient d'une police », nom et licence à retrouver |
| 11 | Suites des décisions 153 à 155 | rappel général tranché (203) |
| 13 | Ligne allaitement | 182, puis 214 à 216, puis la clôture (217), à appliquer |
| 15 | Question du type | piste (a) (184), construite en 348 |
| 16 | Trois écrans à modéliser | la ligne allaitement du flacon pur est sans objet (210) ; les deux autres restent |
| 17 | Échelle du verdict | tranchée (213) |
| 19 | Menu et fiches par thème | rappel tranché (203) ; fiches grossesse en réflexion |
| 21 | Image fixe pour « réduire les animations » | discussion des animations ; chantier du 29/10 |
| 23 | Prise en main guidée | faite (186, 187, 193) |
| 24 | Plan de l'audit | toujours sans réponse |

---

## 6. Commentaires du canevas

- **Lisibles le 31/10** : 78 fils envoyés à Claude, dont 4 ouverts :
  - `2c39b9fd` : police 29LT Riwaya, 29/09 ;
  - `3355a2cf` : la question de la personne extérieure sur les réglages, 17/10 ;
  - `778d3ee5` : tenue du slogan, 29/10 ;
  - `6c55f949` : bouton « Ce n'est pas ce produit », 29 et 31/10.
- **Non lisibles** : les fils jamais envoyés à Claude.
  - Au 29/10, 60 d'entre eux étaient ouverts : 66 fils ouverts, moins les 6 envoyés à Claude.
  - Ils sont décrits dans `fils-ouverts.md` (28 fils, état au 22/10) et dans `commentaires-23-24-10.md` (32 fils, relus le 26/10).
  - Leur état au 30/10 d'après le journal, avec une réponse proposée pour chacun, est dans `propositions/2026-10-31-hors-canevas/reponses-commentaires.md`.
  - Leur état depuis le 30/10 n'est pas connu.
- **Total** : au moins 138 fils. 133 au 26/10, plus 5 créés le 29/10 : `b29469a3`, `8192aeeb` et `c6f9b939`, clos depuis ; `778d3ee5` et `6c55f949`, ouverts.
- **Fils clos par Claude depuis le 21/10**, d'après les journaux : `38898d40`, `218d65e2` et `eda3a66e` (22/10) ; `c467689f` (§24) ; `ae10f83b` et `250e78da` (§27) ; `9bc05b25` (§34).
- **Pour rendre un fil lisible** : y envoyer un message à Claude depuis la page du canevas.

---

## 7. Consignes ajoutées depuis le 21/10

Elles s'ajoutent à celles du §6 de la note.

- **Règles de la porteuse, rappelées le 31/10** : ne rien écraser ni supprimer ; lire la version en ligne avant chaque publication ; ne publier que les planches modifiées ; montrer les rendus avant de publier.
- **Copie avant la première modification** : le 22/10, une copie complète du canevas a été faite et vérifiée contre les empreintes du service avant toute modification (journal du 22/10, §2). Le Drive n'a pas pu la recevoir : l'outil demande le contenu entier dans l'appel, trop gros pour 15,6 Mo.
- **Publication refusée** quand l'index a changé sur la page entre la relecture et l'envoi (29/10, §15) : relire l'index, réappliquer la seule modification, garder les retraits de la porteuse.
- **La porteuse retire des planches depuis la page** : idées 3, 4-Plus et 5-Plus de l'écran des ingrédients, `EA-Verdict-Renvoi-Pastille`, formes écartées de la ligne allaitement. Relire l'index avant chaque modification.
- **Les cinq copies du gabarit de recherche** : `E2-Recherche`, `E2-Recherche-Resultats`, `E2-Recherche-Aucun`, `E2-Produit` et `E5-Recherche-HorsLigne`. La décision 194 avait d'abord oublié `E2-Produit` (§23) : une modification de gabarit se reporte sur toutes ses copies.
- **Vidéos sur le canevas** : le canevas ne tient au début les vidéos en lecture automatique que si une option, côté serveur, est active. La planche d'ouverture lance donc elle-même sa vidéo, et la rejoue (§14).
- **Réglages des planches (« Tweaks »)** (§24, d'après le code du canevas, pas d'après un essai) :
  - un bouton dans l'en-tête de chaque planche, et l'onglet « Tweaks » du panneau latéral ;
  - ils sont désactivés pour qui ne peut pas modifier le canevas (« View only ») : une personne avec un accès en commentaire voit chaque planche dans son état par défaut.
- **Réponses courtes** : « ok, go etape 7 » a été lu comme un accord sur des points restés ouverts (§27). Quand une réponse ne couvre pas toutes les questions posées, redemander.
- **L'identifiant de version donne l'heure d'enregistrement** (§1). Il permet de dater un enregistrement fait depuis la page.
- **Commentaires** : un message envoyé à Claude dans un fil rend tout le fil lisible, et Claude peut y répondre (§1).

---

## 8. Limites de ce complément

- **Il est écrit sans voir le canevas.** Rien ici n'est vérifié contre les planches, et la version en ligne a changé deux fois depuis la dernière publication de Claude.
- **Les journaux sont la seule source des décisions 182 à 217.** Leur énoncé exact est sur les notes du canevas, non relues. Pour les décisions 190, 191 et 192, le journal ne donne pas l'énoncé (§2).
- **Les échanges des séances ne sont connus que par les journaux.** La mémoire des conversations ne suit pas d'une session à l'autre.
- **La note du 21/10 n'a pas été relue en entier** pour ce complément : seulement le §0, le début du §1, le début et la fin du §3, le §4.1, le §5, le §6 et le §7. Une contradiction avec une autre partie de la note reste possible.
- **Le registre v6.7 n'a été lu que pour les entrées citées.**
- **Le fichier du 30/10 de la discussion du registre** (`a_inscrire_registre_30_10_2026.md`) n'a pas été trouvé (journal, §37). Ce qu'il contient n'est pas ici.
- **Le nombre de planches est déduit**, pas compté (§1).
