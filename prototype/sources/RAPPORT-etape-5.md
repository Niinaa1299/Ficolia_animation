# Rapport de déballage — etape-5

Export : `2026-11-01 (24).html` · déballé le 2026-11-01 · canevas « Ficolia — Prototype »

Planches dans l'export : 1 (manifeste : 25 entrées).

| # | Titre dans l'export | Fichier produit | Nom | Taille | support.js | x-dc | dc-script | $preview | trous | liens | ressources extraites | /_blob/ restants | identifiants restants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Réseau faible, scan mis en attente | `E5-SansVerdict-Faible.dc.html` | table | 48606 o | oui | oui | oui | 390×844 | 41 | 8 | 21 | 0 | 0 |

Polices reconstituées en `<link>` Google Fonts : Atkinson Hyperlegible Next.

Export d'une planche seule : son titre est lu dans la balise `<title>` (le titre du bandeau n'est pas dans ce type d'export).

## Écarts et points à vérifier

- Aucun écart relevé.

## Limites

- Les positions, pages et notes du canevas d'origine ne sont pas dans l'export : `canvas.json` dispose les planches en rangées de 8, dans l'ordre de l'export, sur une page « Étape 5 » (`etape-5`).
- Les noms de fichiers viennent de `noms.json` (déduits, à confirmer sur le canevas).
- Le `<link>` Google Fonts est reconstitué (familles et graisses lues dans les `@font-face`) ; l'original n'est pas dans l'export.
- Aucune comparaison octet par octet avec le canevas n'est possible : le serveur refuse d'en servir les fichiers.
