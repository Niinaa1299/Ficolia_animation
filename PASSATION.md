# Passation : reprendre le travail dans un autre compte

Note du 22/10/2026, écrite par la session qui s'arrête pour celle qui reprend. `CLAUDE.md` importe le brief, le cap et cette note : tu les as déjà sous les yeux. Lis ensuite `outils/sources/LISEZ-MOI.md` pour assembler, publier et vérifier. Le brief (`FICOLIA_DESIGN.md`) et le cap (`cap-onboarding.md`) ne se modifient pas sans l'accord de la porteuse du projet. Elle écrit en français et se tutoie : réponds-lui de même.

Tout le travail est sur la branche `claude/compassionate-shannon-qu70ot`. Rien n'est sur `main`, et aucune PR n'est ouverte : la porteuse n'en a pas demandé.

Mise à jour du 22/10 par la session qui reprend : une PR est en fait ouverte depuis le 08/10 (`Niinaa1299/Ficolia_animation#1`, de `compassionate-shannon` vers `main`, sa description ne parle que de la mise à jour obligatoire). Le récit de la figue continue sur `claude/happy-mccarthy-5akhfh`, partie de `e30b47b` ; le prototype se poursuit dans une autre discussion. `main` porte le registre du projet v6.7 (22/10). Le dépôt est public.

## 1. Où en est le récit de la figue

Les statuts sont ceux de l'aperçu (`outils/apercu.py`).

| Écran | Statut | Fichier |
| --- | --- | --- |
| Ouverture, la révélation du logo | validée | `design/reference/revelation-logo.dc.html`, dans le zip du brief |
| Ouverture : l'arbre et la figue | maquette, en cours | `maquettes/ouverture-arbre.html` |
| Accueil, deux écrans | maquette | `maquettes/accueil.html` |
| Formulaire envoyé | validée, retouches : le tampon bis pour le signalement, le photomaton bis pour les photos, la figue s'incline pour le support | `maquettes/formulaire-envoye.html` |
| Connexion insuffisante ou absente, mise à jour obligatoire, délai de connexion, produit inconnu, service indisponible | validées | `maquettes/*.html` |

Les six états ont été exportés en vidéo : `exports/animations/` (voir son `LISEZMOI.md` et `outils/exporter-animations.mjs`). L'ouverture n'y est pas.

## 2. Les trois artéfacts

Les adresses sont privées, celles du compte d'origine. Dans un autre compte, les artéfacts se republient depuis les sources et reçoivent de nouvelles adresses.

| Artéfact | Adresse d'origine | Source dans le dépôt |
| --- | --- | --- |
| Récit de la figue : l'aperçu de tous les écrans (v23 ; v24 le 22/10, publiée à la même adresse depuis l'autre compte, qui a le droit de modifier) | https://claude.ai/artifact/PRP2wzjUmB1Yv4X7wRT8hW | `maquettes/*.html`, assemblées par `outils/apercu.py` |
| Site vitrine : le dossier (v2) | https://claude.ai/artifact/SiQZA1oUejLmDmzuBnRPFq | `outils/sources/site/gabarit-proposition.html`, résultat dans `site/proposition.html` |
| Site vitrine : la maquette animée | https://claude.ai/artifact/F6vTnY69zkAkHPoZUNt1Gv | `outils/sources/site/maquette/gabarit.html`, résultat dans `site/maquette.html`, images dans `site/captures/` |

## 3. L'ouverture « l'arbre et la figue »

**Décidé par la porteuse** (tracé dans `cap-onboarding.md` §4)
- 18/10 : elle ne joue qu'au premier lancement ; la figue s'ouvre calmement.
- 20/10 : après la révélation ; la figue saute de sa branche ; un paysage du Sud sur tout l'écran (le ciel entier en haut, derrière le logo ; l'herbe fondue jusqu'au bas de l'écran ; le texte et « Continuer » posés dessus) ; la vue descend du ciel jusqu'au figuier ; pas de « Passer », l'accueil n'ayant que deux écrans.
- 21/10 : ce jeu d'écrans ne se joue qu'une fois, au premier lancement ; ensuite, l'écran de chargement est plus court. Le blanc est écarté pour le bas de l'écran ; **vert pâle bis est retenu** (vert pâle, vert profond et vert profond bis restent jouables, pour mémoire).
- 21/10 : la transition entre « Ficolia, vos cosmétiques, en toute sérénité » et l'arbre ne lui plaît pas. Elle veut « smooth, continu, fluide ». Par « imbriqué », elle entend qu'à n'importe quelle pause tout paraît fluide : aucune étape n'attend la fin de la précédente.
- 21/10 : la figue du « o » doit en être le personnage principal. Elle a demandé deux idées, « gros plan, puis recul » et « elle saute du logo », et choisi pour le « o » la réponse a : « Fic » et « lia » s'effacent pendant son absence, et le logo revient complet en haut.
- 22/10 (session qui reprend, autre compte) : sur l'écran du paysage, « Ficolia » s'écrit **en toutes lettres**, sans la figue à la place du « o », dans la même écriture que « Fic » et « lia ». Elle a fourni l'image du mot complet ; le « o » en est vectorisé, recalé sur les tracés du logo (`outils/sources/nom/`). Appliqué aux versions bis (réglage `nom`, « Avec la figue » gardé pour mémoire) ; vert pâle et vert profond restent tels qu'au 20/10. Pas encore tracé dans `cap-onboarding.md` §4 : à lui demander.
- 22/10, plus tard : **elle choisit « gros plan, puis recul »**. Deux corrections : le vert du bas de l'écran paraissait avant le paysage et avant que la figue n'arrive dans l'arbre (« fais en sorte que tout se dévoile dans un ordre correct ») ; et plus de « Ficolia » en haut de l'écran, « Bienvenue sur Ficolia » portant déjà le nom. D'où la version `recul2` (« Ton choix », par défaut) : le paysage sort du blanc pendant que la vue recule (5,45 s), puis le bas prend la couleur du pré (5,75 à 6,35 s), puis le texte et « Continuer » (6,05 à 6,55 s) ; le nom ne revient pas. « Continuer » est entier à 6,51 s au lieu de 5,61 s ; l'animation qui accompagne le texte dure 3,9 s. `recul` du 21/10 reste jouable, identique. Pas encore tracé dans `cap-onboarding.md` §4.

**En attente d'elle**
1. ~~Le choix de la transition~~ : **tranché le 22/10, gros plan puis recul** (`recul2`). Elle pourra demander des ajustements : vitesse du recul, regard, moment du texte.
2. **L'étal et ses deux ardoises** : l'arbre prend le 1/2 de l'accueil ; l'étal passerait au 2/2, celui des conditions, ou serait retiré. Question posée, sans réponse.
3. **Le feuillage qui repasse un instant derrière le logo** quand la vue redescend vers le pré, dans toutes les versions bis : le laisser, ou cadrer plus bas. Question posée, sans réponse.
4. **L'écran de chargement court** des lancements suivants : à proposer (forme et durée ; le cap §1 rappelle qu'Android conseille une seconde au plus).
5. **La chair de la figue qui monte jusqu'à la queue** n'existe que dans les versions bis. À étendre aux autres écrans qui montrent la figue ouverte, si elle l'approuve.
6. **Trois écarts à tracer au registre** : sans « Passer », les 5 s de la révélation se regardent en entier au premier lancement (cap §1, « Le lancement doit être immédiat ») ; la maquette ramène la révélation à la palette de marque, alors que l'ouverture validée emploie des teintes voisines (brief §5), ce qu'elle doit trancher ; et, depuis le 22/10, l'accueil 1/2 de son choix (`recul2`) ne porte plus de logotype, seulement « Bienvenue sur Ficolia » en police d'interface, alors que la séance du 28/09 prévoit le « logotype complet à l'accueil » (brief §5) ; dans les autres versions, le nom en toutes lettres est une nouvelle variante du logo, dont le choix reste ouvert (`T-558`).
7. **Le passage de la figue à la lettre** (22/10, proposition) : dans la brume, le soleil, un seul mouvement et le bis, le logo monte avec sa figue ; de 5 à 5,6 s, elle laisse la place à la lettre « o » et « lia » se rapproche. Hors de son choix depuis qu'elle a retenu le recul : sans objet, sauf si elle revient à l'une de ces versions.
8. **Le point 3 (feuillage derrière le logo)** est sans objet dans `recul2`, qui n'a plus de logo en haut.

## 4. Les autres points ouverts du cap (§4)

- L'objectif de Ficolia en une phrase, au premier écran : à écrire.
- Les limites essentielles, au second écran : en attente de la juriste.
- L'aide au bon moment : le scénario est à proposer, sans figue (hors du récit, brief §2).
- Retrouver l'accueil une fois passé, par exemple depuis « À propos ».

## 5. Le site vitrine

Le dossier et la maquette animée sont faits, rien n'est construit. Les réponses de la porteuse du 18/10 sont en tête du dossier (« Tes réponses du 18 octobre ») : l'application sera en ligne avec le site ; le bouton principal est « Télécharger l'application » ; les captures et les quatre niveaux viennent du prototype ; la ligne allaitement aura ses niveaux ; l'accroche reste provisoire ; les tons sont ceux de l'application et les couleurs de la figue ; l'histoire de la fondation sans présentation personnelle ; un site en motion design, « comme sur TikTok ».

**En attente d'elle** (dossier §7 et questions posées après la maquette)
1. La plongée dans la figue : lui plaît-elle ? Vigilance : les graines peuvent se lire comme une grossesse (brief §4).
2. Le figuier de la section « Histoire » (il pousse, une figue y pend sans mûrir) : à valider.
3. Qui écrit les définitions des niveaux pour la ligne allaitement.
4. Le texte de l'histoire de la fondation.
5. Les liens des deux stores, l'adresse de contact, les réseaux sociaux, le nom de domaine, l'hébergeur.
6. Le feu vert pour construire le site (le dossier recommande un site statique, Astro, ou des pages écrites à la main).

À la juriste : les mentions légales, la politique de confidentialité, les textes publics, la place du rappel général sur le site.

## 6. Comment elle travaille

- **Méthode du brief §3** : le scénario d'abord, en deux ou trois pistes avec leur pointe d'humour ; puis des maquettes animées ; le code Flutter seulement après validation. Tout texte nouveau est marqué « Proposition ». Jamais d'écart silencieux à une règle du §4 : nomme la règle.
- **Ses consignes, telles qu'elle les a écrites**
  - « conserve tout le travail qu'on a fait jusque là. n'écrase rien. » On ajoute les variantes à côté, comme boutons du panneau (d'où les versions « bis »), sans remplacer les précédentes. Garde « Revoir la transition ».
  - « NE SUPPRIME PAS l'actuel tampon. » C'est la piste du tampon, dans `maquettes/formulaire-envoye.html`.
  - « ne te restreint pas en terme de couleurs : il faut que ca soit joli et homogène et attrayant. » Les quatre couleurs de verdict restent réservées aux verdicts (brief §4).
- **Quand elle demande des idées**, décris-les en conversation avant de les coder ; elle choisit ensuite.
- **À chaque modification** : assembler, regarder des images à plusieurs instants, tester le mouvement réduit et la console, comparer avec l'état précédent (les anciennes versions doivent rester identiques à l'image près), reconstruire l'aperçu, committer, pousser sur la branche.
- **Accessibilité** : le texte et « Continuer » ne sont jamais bloqués par l'animation ; l'animation qui les accompagne reste sous 5 s (`outils/verification/arrivee.mjs`) ; avec « réduire les animations », des fondus sans déplacement.
- **Vigilance** (brief §4) : une figue qui mûrit, s'arrondit ou porte ses graines peut se lire comme une grossesse. La chute de la figue doit se lire comme un saut choisi, jamais comme un accident.

## 7. Ce qui ne passe pas avec les fichiers

Les adresses des artéfacts, leur historique de versions et leurs commentaires ; la conversation elle-même, dont seules les décisions sont reprises ici et dans `cap-onboarding.md` ; les planches de captures temporaires du site, qu'on refait avec `outils/verification/`.
