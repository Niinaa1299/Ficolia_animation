# Direction « Matière » : proposition du 12 octobre 2026

Proposition de design pour toute l'interface de Ficolia, du scan au verdict. Elle fait suite au retour de la porteuse sur les trois pistes du récit de la figue, jugées trop stéréotypées. Tout ici est une proposition : rien n'est inscrit au registre.

Ouvrir `direction-matiere.html` dans un navigateur. La page est autonome et se lit sans réseau, sauf la police, qui vient de Google Fonts.

## Ce que la direction retient des retours

- L'application d'abord : on scanne et on obtient deux verdicts, grossesse et allaitement. La figue n'est plus le sujet des écrans.
- Le registre « beauté responsable », premium et chaleureux. Une matière de soin en grand (ce qui plaisait dans la piste A), mais seulement à l'accueil et à la demande de caméra.
- « Composition : figue. » (ce qui plaisait dans la piste C) devient une légende de planche. Elle est tirée du contour de la figue, jamais de son centre, car la figue est un emblème intime : un sein et ses canaux lactifères, un ventre et sa graine.

## Règles du projet tenues

- Rien de la marque près d'un verdict (`D-115`) : fiche produit, composition et panneau d'un ingrédient n'ont ni figue, ni logo, ni aubergine. Le symbole du scanner s'efface quand un verdict monte.
- Fiche produit dépouillée (dossier §3.1) : la photo, l'identité, les deux lignes.
- Couleurs de verdict réservées aux verdicts (palette retenue de `tokens.json`). Le libellé porte le sens, la couleur le renforce (`T-219`, `T-220`).
- Écrans d'échec : ni rassurants ni alarmants (`T-196`), avec la cause dite en clair (`T-512`) et aucune promesse (§5.7, `L-7`).
- Accessibilité : contraste du texte d'au moins 4,5:1, cibles de 44 pt, texte à 200 % démontré, libellés pour les lecteurs d'écran, variante « animations réduites ».
- Aucun mot interdit, et ni « scientifique » ni « vérifié » (`textes.md` §2, `D-116`). La rigueur se montre par les noms INCI, les sources et leurs dates de publication.

## Hypothèses à valider (non décidées par le registre)

- L'échelle à quatre crans sous chaque verdict.
- Un verdict par ingrédient et par ligne, et donc le sélecteur grossesse / allaitement dans la composition.
- Le résumé des sources dans le panneau d'un ingrédient (`D-116`, `T-534`).
- La carte du scan réussi, qui montre les deux verdicts avant d'ouvrir la fiche.
- La légende « Composition : figue. » sur le logotype de l'accueil.

## Questions pour la porteuse

1. Les quatre libellés de verdict. La maquette affiche `[Niveau 1]` à `[Niveau 4]` en textes de remplacement.
2. Les hypothèses ci-dessus à retenir.
3. L'origine et la qualité des photos de produits.
4. Les grands titres de l'accueil : Atkinson Hyperlegible Next, ou une police de marque ?

## Relecture

La première version a été relue par trois relecteurs indépendants : règles du projet, accessibilité, critique de design. Leurs corrections sont intégrées. La page les résume dans « Ce que la relecture a changé ».

## Sources

`sources/` contient les scripts qui dessinent les maquettes et assemblent la page.

- **Régénérer la page :** `python3 sources/direction.py direction-matiere.html`. Il faut Python 3, sans dépendance.
- **Régénérer la texture de baume :** `texgen*.py`, qui demande numpy, scipy et Pillow.

La texture est un rendu de travail. Elle est à remplacer par une vraie photo macro.
