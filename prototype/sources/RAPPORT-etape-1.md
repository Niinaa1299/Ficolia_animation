# Rapport de déballage — etape-1

Export : `2026-11-02 (29).html` · déballé le 2026-11-02 · canevas « Ficolia — Prototype »

Planches dans l'export : 1 (manifeste : 11 entrées).

| # | Titre dans l'export | Fichier produit | Nom | Taille | support.js | x-dc | dc-script | $preview | trous | liens | ressources extraites | /_blob/ restants | identifiants restants |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Accueil 2/2 · conditions d'utilisation (29/10) | `E1-Accueil-Conditions.dc.html` | table | 20307 o | oui | oui | oui | 390×844 | 8 | 3 | 7 | 0 | 0 |

Polices reconstituées en `<link>` Google Fonts : Atkinson Hyperlegible Next.

Export d'une planche seule : son titre est lu dans la balise `<title>` (le titre du bandeau n'est pas dans ce type d'export).

## Écarts et points à vérifier

- Aucun écart relevé.

## Limites

- Les positions, pages et notes du canevas d'origine ne sont pas dans l'export : `canvas.json` dispose les planches en rangées de 8, dans l'ordre de l'export, sur une page « Étape 1 — sans animation » (`etape-1`).
- Les noms de fichiers viennent de `noms.json` (déduits, à confirmer sur le canevas).
- Le `<link>` Google Fonts est reconstitué (familles et graisses lues dans les `@font-face`) ; l'original n'est pas dans l'export.
- Aucune comparaison octet par octet avec le canevas n'est possible : le serveur refuse d'en servir les fichiers.
