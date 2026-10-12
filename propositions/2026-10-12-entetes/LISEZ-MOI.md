# En-têtes des écrans : étude du 12 octobre 2026

Comment habiller le haut des écrans de l'application, qui paraît vide et inachevé. L'étude part de l'écran Historique du prototype : même liste, même barre d'onglets, seul le haut change. Ouvrir `entetes.html` dans un navigateur.

## Variantes

- **A · Grand titre** : 34 pt, aligné sur la liste, avec une ligne de contexte (« 5 produits consultés sur ce téléphone », Proposition).
- **B · Voile de lumière** (recommandé) : le grand titre posé dans une seule teinte chaude, `#F7EFEA`, qui s'efface vers le blanc sur 300 pt, avec un grain à 6 %.
- **C · Bandeau de matière** : le fond poudré de la texture de baume, avec la liste qui monte dessus comme une feuille. Plutôt pour « À propos ».

En défilement, le grand titre se replie en barre compacte translucide (blanc à 82 %, flou de 18 pt). Une ombre de 10 pt marque le bord, sans trait.

## À trancher

- La teinte `#F7EFEA` n'est pas dans `tokens.json`. L'ivoire rosé de la marque est réservé hors de l'interface, et le cadre `#FAF8F4` est plus neutre.
- L'en-tête ne s'applique pas aux écrans de verdict : fiche produit, composition et panneau d'un ingrédient (`D-115`, §3.1).
