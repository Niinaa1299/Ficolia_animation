# Animations retenues, sans les textes des écrans

Exportées par `outils/exporter-animations.mjs` depuis les maquettes (`maquettes/`), en couleurs, sauf la connexion, en couleurs et en gris.

Vérifié le 29/10 : les maquettes n'ont pas changé depuis cet export, et la dernière image de chaque animation, refaite depuis elles, est identique au pixel près. L'ouverture et l'accueil sont dans `../ouverture/` ; l'index de toutes les animations validées, dans `../LISEZMOI.md`.

Pour chaque animation, trois fichiers :

- `….mp4` : la vidéo sur fond blanc, à regarder ou à partager. Elle se lit partout.
- `…_transparent.webm` : la même vidéo sur fond transparent, pour l'intégration (Chrome, Firefox, Android ; Safari ne lit pas la transparence de ce format).
- `…_derniere-image.png` : la dernière image, sur fond transparent. Ce n'est pas l'image fixe retenue pour la situation : celle-ci reste à décider.

Format : 60 images par seconde, 780 px de large (l'écran entier, 390 pt, en ×2). La hauteur est cadrée sur ce qui bouge ; `exports.json` donne, pour chaque animation, sa durée, sa hauteur et sa place depuis le haut de l'écran (en points).

| Écran | Animation | Fichier |
| --- | --- | --- |
| Formulaire envoyé, signalement | Le tampon bis | `formulaire-envoye_signalement_tampon-bis` |
| Formulaire envoyé, contribution photo | Le photomaton bis | `formulaire-envoye_contribution-photo_photomaton-bis` |
| Formulaire envoyé, support | La figue s'incline | `formulaire-envoye_support` |
| Connexion insuffisante | Elle lève le bras (couleurs, gris) | `connexion-insuffisante_couleurs`, `connexion-insuffisante_gris` |
| Pas de connexion | Elle lève le bras (couleurs, gris) | `pas-de-connexion_couleurs`, `pas-de-connexion_gris` |
| Mise à jour obligatoire | L'ancienne version (la figue sèche) | `mise-a-jour-obligatoire_ancienne-version` |
| Mise à jour obligatoire | La nouvelle version (elle redevient fraîche) | `mise-a-jour-obligatoire_nouvelle-version` |
| Délai de connexion | Les cent pas | `delai-de-connexion_cent-pas` |
| Produit inconnu | La cagette vide | `produit-inconnu_cagette-vide` |
| Service indisponible | Le store de l'étal | `service-indisponible_store-de-l-etal` |
