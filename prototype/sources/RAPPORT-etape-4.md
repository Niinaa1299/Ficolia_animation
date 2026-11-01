# Rapport de déballage — etape-4

Export : `2026-11-01 (11).html` · déballé le 2026-10-31 · canevas « Ficolia — Prototype »

Planches dans l'export : 1 (manifeste : 7 entrées).

| # | Titre dans l'export | Fichier produit | Nom | Taille | support.js | x-dc | dc-script | $preview | trous | liens | ressources extraites | /_blob/ restants | identifiants restants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Signalement — choix du type de produit | `E4-Signalement-Types.dc.html` | table | 67210 o | oui | oui | oui | 390×844 | 70 | 9 | 3 | 0 | 0 |

Polices reconstituées en `<link>` Google Fonts : Atkinson Hyperlegible Next.

Export d'une planche seule : son titre est lu dans la balise `<title>` (le titre du bandeau n'est pas dans ce type d'export).

## Écarts et points à vérifier

- Aucun écart relevé.

## Limites

- Les positions, pages et notes du canevas d'origine ne sont pas dans l'export : `canvas.json` dispose les planches en rangées de 8, dans l'ordre de l'export, sur une page « Étape 4 — contribution photo et signalement » (`etape-4`).
- Les noms de fichiers viennent de `noms.json` (déduits, à confirmer sur le canevas).
- Le `<link>` Google Fonts est reconstitué (familles et graisses lues dans les `@font-face`) ; l'original n'est pas dans l'export.
- Aucune comparaison octet par octet avec le canevas n'est possible : le serveur refuse d'en servir les fichiers.
