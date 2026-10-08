# Ficolia — brief de conception pour Claude Code

Version du 9 octobre 2026. Tiré du registre de projet v6.4, qui fait foi, du dossier de conception du 30/09 et des décisions de séance jusqu'au 09/10. Ce fichier ne remplace pas le registre. Ne le modifie pas sans l'accord de la porteuse du projet.

Les références entre parenthèses (`D-115`, `T-512`…) renvoient au registre. Elles servent à la traçabilité et ne s'affichent jamais à l'écran.

## 1. Ficolia en bref

- Application mobile gratuite (`D-19`), en Flutter (`D-78`). Elle informe sur la composition d'un produit cosmétique pendant la grossesse et l'allaitement, à partir d'un scan du code-barres ou d'une recherche par nom.
- Elle informe, elle ne prescrit pas (`D-24`). Ce n'est pas un avis médical.
- France seulement, en français seulement (`D-98`, `T-173`).
- Pas de compte, pas de profil, aucune question sur la personne (`D-59`). Chaque produit reçoit deux lignes, grossesse et allaitement, chacune avec son verdict.
- Public : femmes enceintes ou allaitantes, et leurs proches. Le registre le décrit comme un public anxieux (`T-541`). Certaines lectrices peuvent avoir vécu une grossesse arrêtée (`T-424`).
- Usage : surtout en magasin, où le réseau est souvent mauvais (Périmètre MVP §1.6, `T-130`).

## 2. Ta mission

**Le brief de la porteuse.** Construire un récit autour de la figue, le symbole de Ficolia. Chaque étape de la vie d'une figue correspond à un état de l'application (« un état du téléphone », dans ses mots). Son exemple : une mise à jour obligatoire, c'est une figue séchée, qui redevient fraîche une fois l'application à jour. Avec une pointe d'humour.

Tu proposes des animations et des designs originaux. Il n'y a aucune consigne de style, de durée ni de courbe : seules s'appliquent les règles du §4.

**Le périmètre** (décisions de la porteuse, 08 et 09/10) :

1. **L'animation d'ouverture**, « Révélation du logo » : validée en l'état, améliorable (§6).
2. **Les trois écrans d'accueil** : apparence à refaire entièrement. Ils doivent donner la meilleure impression dès le premier lancement ; leur beauté compte. Ils font partie du récit.
3. **Six états** :
   - formulaire envoyé (signalement d'une erreur, contribution photo, message au support) ;
   - connexion insuffisante ou absente ;
   - mise à jour obligatoire ;
   - délai pendant la recherche de connexion ;
   - produit scanné mais inconnu ;
   - service indisponible (« l'application est indisponible », dans les mots de la porteuse).

Le récit de la figue s'arrête là : aucune animation de figue sur les autres écrans.

Chaque écran est détaillé dans `design/etats.md` : ce que dit le projet, les textes, les points ouverts. Lis-le avant de proposer.

## 3. Méthode

1. **Scénario d'abord.** Avant de construire, propose quelle étape de la vie de la figue pour quel état, en deux ou trois pistes, avec la pointe d'humour de chacune. Rien n'est construit avant le choix de la porteuse.
2. **Puis des maquettes animées.** Un fichier HTML autonome par écran (HTML, CSS, SVG, et JavaScript si nécessaire), au format d'un téléphone en portrait, lisible dans un navigateur. Ces maquettes seront intégrées au prototype, puis au code.
3. **Le code Flutter vient ensuite**, une fois les maquettes validées.
4. **Tout est proposition.** La porteuse tranche, et chaque choix est tracé dans le projet. Si une proposition s'écarte d'une règle du §4 ou d'une décision citée ici, dis-le en nommant la règle. Jamais d'écart silencieux.
5. **Les textes.** Les textes existants (`design/textes.md`) sont repris mot pour mot. Tout texte nouveau, humoristique compris, est marqué « Proposition » : les textes de Ficolia passent par des règles strictes et, pour certains, par la juriste.

## 4. Règles du projet

Ce ne sont pas des consignes de style. Ce sont des règles qui valent pour tout élément de Ficolia, figue comprise.

**Couleurs et verdicts**
- Les quatre couleurs de verdict ne servent qu'aux verdicts. Ces valeurs ne s'emploient nulle part ailleurs (liste dans `design/tokens.json` ; `D-115` D2, `T-548`).
- Ni figue, ni logo, ni couleur de marque près d'un verdict : écran de verdict, liste des ingrédients et son panneau (`D-115`). L'écran produit reste dépouillé : la photo, l'identité, les deux lignes, rien d'autre (dossier §3.1). Aucun de ces écrans n'est dans ton périmètre.

**Les écrans d'échec** : connexion insuffisante ou absente, produit inconnu, service indisponible.
- Jamais un feu vert, jamais une alerte ; l'absence d'évaluation est dite en clair (`D-113` B3, `T-512`). Cela vaut aussi pour l'humeur et la couleur de la figue.
- Le registre visuel des états sans verdict, dont produit inconnu et service indisponible, est « ni rassurant, ni alarmant » (`T-196`, tâche ouverte).
- Chaque écran dit sa cause (`T-512`).

**Aucune promesse**
- Rien ne promet une évaluation future : un produit inconnu rejoint la file de transcription sans message de promesse (dossier §5.7).
- Pour la contribution photo : « si le produit est publié », jamais « quand » (`T-81`).
- Pas de figue qui « veille » : « nous veillons sur les ingrédients » fait partie des formules interdites (dossier §4.4), et la règle proposée `T-533` (e) exclut toute promesse de surveillance ou de certitude.

**Neutralité et moments sensibles**
- Aucun texte ne suppose une grossesse en cours, un bébé né, ni même que la lectrice est concernée (`D-114` C1 ; dossier §4.3).
- Point de vigilance, pas une interdiction : une figue qui mûrit, s'arrondit ou porte ses graines peut se lire comme une grossesse. Pour une lectrice qui a vécu une grossesse arrêtée, ce n'est pas neutre.
- Après un message au support : animation sobre, sans humour (porteuse, 09/10). Ce message peut signaler un effet indésirable survenu ou une détresse (`T-457`, `T-404`).

**Accessibilité**
- L'état se dit en texte, jamais par la seule allure de la figue. C'est la règle du projet pour les verdicts, étendue ici à la figue : le libellé porte le sens, la couleur le renforce (`T-219`) ; aucune information n'est codée par la seule couleur (`T-220`).
- Libellés alternatifs pour les lecteurs d'écran, cibles tactiles d'au moins 44 px, structure sémantique (`D-58`, `T-388`). Une figue décorative est masquée aux lecteurs d'écran ; une figue qui porte un sens a son libellé.
- Texte d'au moins 4,5:1 de contraste (`T-388`, référence WCAG 2.1 AA). Le texte s'agrandit sans casser l'écran (`T-220`, `T-559`).
- Une animation de plus de 5 secondes, affichée avec d'autres contenus, doit pouvoir être mise en pause, arrêtée ou masquée (WCAG 2.1, critère 2.2.2). Seule à l'écran, elle n'y est pas tenue. Rien ne clignote plus de trois fois par seconde (critère 2.3.1).
- Le réglage « réduire les animations » du téléphone est respecté (choix de l'étape 1 du prototype, confirmé par la porteuse le 09/10). En Flutter, Android le signale par `MediaQueryData.disableAnimations` ; la réduction des animations d'iOS ne l'active pas et passe par `AccessibilityFeatures.reduceMotion` (documentation Flutter, à revérifier dans la version du projet).

**Ce qui n'existe pas au lancement, à ne pas dessiner**
- Notifications push (`T-224`), partage d'un verdict (`T-250`), partage entrant (`T-254`), compte (`D-59`), liste de favoris (seul l'emplacement du cœur figure, `D-115`).
- Mode sombre : thème clair seulement (`D-115` D1, `T-386`).

**Les mots** : règles et mots interdits dans `design/textes.md`. Le nom Ficolia, seul (`D-108`).

## 5. Identité visuelle au 9 octobre

| Élément | Valeur | Statut |
| --- | --- | --- |
| Palette de marque | aubergine `#4C2944` · pistache `#9EBE59` · grenade `#9F3542` · ivoire rosé `#FFF7F0` · texte profond `#321C31` | Acté (`D-115`, `T-548`) |
| Interface | fond `#FFFFFF` · cadres `#FAF8F4` · bordures `#E7E1DA` ; aubergine pour les éléments actifs ; ivoire rosé hors interface | Séance 27-28/09, à inscrire au registre |
| Texte secondaire | `#6E5A6B` (6,3:1 sur blanc) | Page « Fondations » du prototype |
| Police d'interface | Atkinson Hyperlegible Next, seule famille pour les libellés, phrases et listes | Séance 01/10, à inscrire |
| Polices de marque | Antic Didone, Pompiere, Simonetta : logo et grands titres seulement. Pompiere est illisible en petite taille | Acté (`D-115`) |
| Nunito (500, 600) | Employée par l'animation d'ouverture pour sa phrase d'accroche | À confirmer par la porteuse |
| Logo | Logotype complet à l'accueil, symbole seul ailleurs | Séance 28/09, à inscrire |
| Variante du logo | L'animation d'ouverture emploie le tracé manuscrit vectorisé, la figue y faisant le « o » de Ficolia | Choix définitif à confirmer (`T-558`) |
| Symbole | `design/assets/figue-symbole.svg`, en aubergine, pistache et grenade de la marque ; quatre tracés minuscules d'une autre teinte (`#94564B`, `#E2D9CD`) semblent des restes de vectorisation | Fourni par la porteuse |

Écart à connaître : l'animation d'ouverture emploie des variantes proches des couleurs de marque (encre `#4A334A`, nervures `#A7BD50`, graines `#943F42`, texte `#4B3738`). Pour un travail nouveau, pars de la palette de marque et signale l'écart : la porteuse tranchera.

## 6. L'animation d'ouverture, validée en l'état

Fichier : `design/reference/revelation-logo.dc.html`. C'est une planche du canevas de conception du prototype : ses réglages (`{{cls}}`, `{{chair}}`) sont remplis par le canevas, qui n'est pas fourni.

Format 1080 × 1920. À vitesse réelle, l'animation dure 5 secondes. Dans le canevas, en lecture en boucle, l'image finale est ensuite tenue 3 secondes, puis tout reprend.

| Temps | Ce qui se passe |
| --- | --- |
| 0 à 0,9 s · graine | Un point aubergine apparaît et s'étire en goutte. |
| 0,9 à 1,6 s · contour | Le contour de la figue et sa queue se dessinent, en grand au centre de l'écran. |
| 1,6 à 2,6 s · ouverture | La goutte vire au vert puis s'efface ; la chair blanche s'ouvre ; les nervures vertes partent du centre ; les graines apparaissent une à une. |
| 2,4 à 3,5 s · transformation | La figue rapetisse et vient se placer entre « Fic » et « lia », qui glissent depuis les côtés : elle devient le « o » de Ficolia. |
| 3,5 à 4,4 s · accroche | Deux lignes montent sous le logo : « Vos cosmétiques, » puis « en toute sérénité. » |
| 4,4 à 5 s · image finale | La figue respire une fois, légèrement, puis l'image se fige. |

Statut des éléments :
- L'animation est validée ; tu peux proposer de l'améliorer.
- L'accroche est un texte provisoire (`design/textes.md`).
- Quand elle joue (à chaque ouverture ou au premier lancement seulement) et à quelle vitesse, ce n'est pas tranché : voir `design/etats.md` §1.

## 7. Fichiers de référence

- `design/etats.md` : chaque écran du périmètre, un par un.
- `design/textes.md` : règles de texte, mots interdits, textes existants et leur statut.
- `design/tokens.json` : couleurs (dont celles à ne jamais employer), polices, valeurs d'accessibilité.
- `design/assets/figue-symbole.svg` : le symbole.
- `design/reference/revelation-logo.dc.html` : l'animation d'ouverture.
- `design/captures/` : captures du prototype actuel, si la porteuse les a ajoutées. Elles montrent l'existant, pas une cible : l'accueil va être refait.

Ne servent pas de référence : les maquettes « V11 » et les anciens prototypes du projet, qui portent au moins 29 éléments caducs (`T-366`, `D-115`).

## 8. Limites de ce fichier

- Instantané au 9 octobre 2026 : le registre peut évoluer.
- Plusieurs décisions citées ici ont été prises en séance et ne sont pas encore inscrites au registre ; elles le seront en fin de prototype.
- Dans ton périmètre, deux textes sont actés : « Nous ne connaissons pas ce produit » et le bouton « Accepter ». Le rappel général de l'accueil est acté sous réserve de la juriste. Les autres textes sont provisoires ou à écrire.
