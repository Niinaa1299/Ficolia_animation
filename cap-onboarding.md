# Notre cap : ce qui fait un onboarding réussi

Version du 17 octobre 2026. La porteuse du projet en a fait notre cap le 17/10 : « à garder toujours à l'esprit ». Il vaut pour l'accueil et pour toute aide donnée dans l'application. Il ne remplace ni le registre ni le brief (`FICOLIA_DESIGN.md`). Ne le modifie pas sans l'accord de la porteuse du projet.

## 1. Les sept principes

Tirés de la recherche du 17/10, repris mot pour mot. Sources au §5.

- **Le mieux, c'est de ne pas en avoir besoin.** Une application doit se comprendre en s'en servant. S'il faut un onboarding, Apple le veut « rapide, plaisant et facultatif ». Le Nielsen Norman Group, un cabinet de référence en ergonomie, conseille de s'en passer quand c'est possible : chaque écran demande un geste et un effort de mémoire.
- **Les tutos en écrans s'oublient.** Le Nielsen Norman Group a testé 70 personnes sur 4 applications. Les tutos n'ont rendu personne plus rapide ni plus efficace, et ceux qui les avaient lus trouvaient même les tâches plus difficiles. S'il en faut un : un « Passer » bien visible, très peu d'écrans, une idée par écran.
- **L'aide au bon moment vaut mieux.** Une indication donnée au moment du geste, à l'endroit du geste, est lue et retenue. Et on apprend mieux en faisant qu'en regardant.
- **Trois écrans au plus, une seule fois.** Google limite ce format à trois écrans, montrés au premier lancement seulement. Si quelqu'un passe l'onboarding, Apple conseille de ne pas le remontrer, mais de le laisser retrouvable.
- **Les autorisations, au moment où on en a besoin.** C'est déjà notre choix pour la caméra.
- **Le juridique.** Apple conseille d'intégrer les conditions « de façon équilibrée, sans casser l'expérience ». En France, il faut pouvoir les lire avant de les accepter, puis les accepter par un geste clair, sans case précochée. Ce point vient de guides juridiques et reste à confirmer par la juriste. Et rien ne doit pousser à accepter : la CNIL range ces pressions parmi les « designs trompeurs ».
- **Le lancement doit être immédiat.** Selon Apple, un écran de marque peut ouvrir l'onboarding, mais juste le temps d'être vu. Android conseille une animation de démarrage d'une seconde au plus.

## 2. Ce que nous en faisons

Décisions de la porteuse du 17/10, sauf mention contraire.

- **Deux écrans d'accueil.** Le premier présente Ficolia ; le second porte les conditions d'utilisation.
- **« Accepter » ouvre le scanner.** Rien ne s'intercale entre l'acceptation et le premier scan.
- **Pas de tuto à l'accueil.** L'aide viendra au bon moment, pendant la navigation.
- **Pas de texte sur ce que Ficolia fait ou ne fait pas.** Les limites (grossesse physiologique, produits vendus hors de France, données qui datent de leur source) passent dans les limites essentielles du second écran, que la juriste doit écrire. C'est un écart à `D-114` C7, qui leur donnait un écran : à tracer au registre.
- **Le rappel général reste sur l'accueil** (`D-114` C8) : au premier écran, sous l'objectif.
- **Aucune demande d'autorisation sur l'accueil** : pas de notification (`T-224`) ; la caméra n'est demandée qu'au premier scan (`T-232`, décision du 05/10).
- **L'acceptation** : lien vers les conditions d'utilisation, bouton « Accepter », aucune case précochée ; une nouvelle acceptation à chaque nouvelle version des conditions (`T-557`).
- **L'animation d'ouverture ne joue qu'au premier lancement** (porteuse, 18/10).

Ce que la maquette de l'accueil (`maquettes/accueil.html`) en applique déjà :
- une idée par écran ;
- des scènes de moins de 5 secondes, puis une image fixe (WCAG 2.1, critère 2.2.2) ;
- un bouton jamais bloqué par l'animation ;
- des points qui montrent où l'on en est ;
- si le texte est agrandi, il défile et les boutons restent en bas ;
- la figue lit les conditions sans jamais regarder le bouton « Accepter » : rien ne pousse à accepter ;
- avec « réduire les animations », un fondu, sans aucun déplacement.

## 3. Les questions à poser devant chaque proposition

1. **Peut-on s'en passer ?** Ce qui se comprend en s'en servant n'a pas besoin d'écran.
2. **Une seule idée par écran ?**
3. **Peut-on avancer sans attendre ?** Aucun bouton bloqué par une animation ; aucune animation de plus de 5 secondes sans pause, si d'autres contenus l'accompagnent.
4. **Pour une aide : arrive-t-elle au moment du geste, à l'endroit du geste ?** Fait-elle faire plutôt que regarder ?
5. **Ce qui ne sert qu'une fois ne se montre-t-il qu'au premier lancement ?** Reste-t-il retrouvable ensuite ?
6. **Une autorisation est-elle demandée avant d'en avoir besoin ?**
7. **Les conditions se lisent-elles avant d'être acceptées ?** Le geste d'accepter est-il clair, sans case précochée ? Rien ne presse-t-il d'accepter ?
8. **Le lancement reste-t-il immédiat ?** Un moment de marque dure juste le temps d'être vu.
9. **Et toujours les règles du brief** (`FICOLIA_DESIGN.md` §4) : neutralité, aucune promesse, accessibilité, couleurs de verdict réservées aux verdicts.

## 4. Ce qui reste ouvert

- **L'objectif de Ficolia, en une phrase**, au premier écran : à écrire.
- **Les limites essentielles**, au second écran : en attente de la juriste.
- **L'aide au bon moment** : son scénario est à proposer (premier scan, recherche par nom…). Ces écrans sont hors du récit de la figue (`FICOLIA_DESIGN.md` §2) : l'aide s'y passe de figue. L'écran produit reste dépouillé, et rien n'y appelle à l'action (`D-66`).
- **Retrouver l'accueil** une fois passé, par exemple depuis « À propos ».
- **L'arbre et la figue**, idée de la porteuse du 17/10 : maquette du 18/10 (`maquettes/ouverture-arbre.html`), pour comparer sa place (après la révélation, ou fondue avec elle), ses quatre descentes et ses trois décors. Au sol, la figue s'ouvre calmement (porteuse, 18/10). À trancher : la place, la descente, le décor ; garder ou non le décor quand le nom paraît ; « Passer », proposé pour l'animation.

## 5. Sources

- [Apple, Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
- [Apple, Launching](https://developer.apple.com/design/human-interface-guidelines/launching)
- [Android, écran de démarrage](https://developer.android.com/develop/ui/views/launch/splash-screen)
- [Nielsen Norman Group, Mobile-App Onboarding](https://www.nngroup.com/articles/mobile-app-onboarding/)
- [Nielsen Norman Group, Onboarding Tutorials vs. Contextual Help](https://www.nngroup.com/articles/onboarding-tutorials/)
- [Nielsen Norman Group, Mobile Tutorials](https://www.nngroup.com/articles/mobile-tutorials/)
- [Material Design, Onboarding](https://m2.material.io/design/communication/onboarding.html)
- [CNIL, guide des designs trompeurs](https://apparences-trompeuses.beta.cnil.fr/Assets/files/Guide-designs-trompeurs.pdf)
- [Legalplace, CGU d'une application mobile](https://www.legalplace.fr/guides/conditions-generales-utilisation-application-mobile/)

Le site du Nielsen Norman Group n'a pas pu être ouvert directement : pour lui, la recherche s'appuie sur les extraits de ses articles.
