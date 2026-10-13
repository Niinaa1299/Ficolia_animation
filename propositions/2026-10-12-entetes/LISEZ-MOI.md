# En-têtes des écrans : étude des 12 et 13 octobre 2026

Comment habiller le haut des écrans de l'application, qui paraît vide et inachevé. L'étude part de l'écran Historique du prototype : même liste, même barre d'onglets, seul le haut change. Ouvrir `entetes.html` dans un navigateur.

Version du 13 octobre : la ligne « 5 produits consultés… » est retirée, et le rose poudré a laissé place au lin et au grège.

## Variantes

- **A · Grand titre** : 34 pt, aligné sur la liste.
- **B · Voile de lin** (recommandé comme base) : une seule teinte, `#F2EDE6`, de la famille du cadre et de la bordure, qui s'efface vers le blanc sur 280 pt, avec un grain à 7 %.
- **C · Bandeau de lin** : une toile de lin ivoire, sur laquelle la liste monte comme une feuille. Plutôt pour « À propos ».
- **D · Gaufrage** : la silhouette entière du symbole en relief à sec, à côté du titre, sans couleur ni détail intérieur.
- **E · Aubergine** : bandeau de marque et titre blanc. Écart : l'aubergine est réservée aux éléments actifs.
- **F · Titre de marque** (recommandé en signature) : le grand titre en Antic Didone, police de marque autorisée pour les grands titres (`D-115`).

En défilement, le grand titre se replie en barre compacte translucide (blanc à 82 %, flou de 18 pt). Une ombre de 10 pt marque le bord, sans trait.

## À trancher

- La teinte `#F2EDE6` n'est pas dans `tokens.json`.
- L'en-tête ne s'applique pas aux écrans de verdict : fiche produit, composition et panneau d'un ingrédient (`D-115`, §3.1).
