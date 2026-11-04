# Ficolia

Ce dépôt porte le prototype de Ficolia (les écrans du canevas de conception, leurs sources, leurs outils) et le récit de la figue (animations et maquettes, branche `claude/happy-mccarthy-5akhfh`). Le brief est importé ci-dessous ; les fichiers de référence du brief sont dans `Ficolia_contexte_Claude_Code_09_10_2026.zip`. La porteuse du projet écrit en français et se tutoie : réponds-lui de même.

@FICOLIA_DESIGN.md

## Le récit de la figue (animations, ouverture, accueil)

Les maquettes sont dans `maquettes/` ; `outils/apercu.py` les réunit en un seul aperçu ; les exports validés (vidéos et images sans texte, page de référence des textes) sont dans `exports/` (index : `exports/LISEZMOI.md`) ; les sources des artéfacts et leur mode d'emploi dans `outils/sources/LISEZ-MOI.md`. Le cap de l'accueil et la note de passation du 22/10 (où est chaque artéfact, ce qui est décidé, ce qui attend la porteuse) sont importés ci-dessous.

@cap-onboarding.md

@PASSATION.md

## Le canevas de travail

- **Un seul canevas de travail** : « ficolia - prototype_vTravail », https://claude.ai/artifact/FB6cC6xawyir9Y1QwCYosb (identifiant `72c8d58f-8aa6-4090-b17c-fc9e3f77fcf6`), créé le 31/10/2026 depuis le dépôt. L'ancien canevas (https://claude.ai/artifact/EuTtpHhP8LubH91j4wpsVw) est une archive : ses fichiers sont illisibles depuis Claude Code, on n'y travaille plus, on ne le supprime pas (il garde l'historique et les commentaires).
- **Les sources font foi** : `prototype/sources/project/` (planches, index `canvas.json`, ressources `assets/`), `prototype/sources/noms.json`, `prototype/sources/blobs.json`. Mode d'emploi et limites : `prototype/LISEZ-MOI.md`. Outils : `outils/deballer-export.py`, `outils/rendre.mjs`, `outils/rendre-reglage.mjs`, `outils/verifier-liens.py`, `outils/preparer-publication.py`.
- **Branche de travail du prototype** : `claude/magical-mendel-cwpmji`. Une seule session à la fois sur le canevas et sur cette branche.

## Règles, à appliquer sans qu'on te le demande

### R1. Au début de chaque séance, vérifier l'accès au canevas, sans rien modifier

Avant tout travail, lire la liste des fichiers du canevas de travail (outil « Artifact » : `action: list`, `scope: files`, sur son adresse) et dire à la porteuse, en une ligne, si la lecture passe. Si elle est refusée : ne rien publier, continuer dans le dépôt seul, et le dire clairement. Ce contrôle existe parce que l'ancien canevas est devenu illisible sans prévenir.

### R2. Toute modification d'une planche passe par le dépôt avant le canevas

Dans cet ordre, sans exception :
1. modifier la source dans `prototype/sources/project/` (jamais une copie ailleurs) ;
2. rendre la planche (`node outils/rendre.mjs <dossier> <source>`) et regarder l'image ;
3. enregistrer et pousser (`git commit`, `git push`) ;
4. publier dans le canevas : directement pour une planche sans ressource ; par `outils/preparer-publication.py` pour une planche qui référence `assets/` (le canevas n'affiche pas un chemin relatif) ; `canvas.json` avec, si la disposition change.

Rien n'est publié qui ne soit pas d'abord dans le dépôt. Une nouvelle planche reçoit son entrée dans `canvas.json` (page, position, `is_interactive` si elle a des liens, des gestionnaires ou une vidéo). Une nouvelle ressource est téléversée dans la réserve du canevas et ajoutée à `blobs.json` avant la publication de la planche qui l'utilise.

### R3. Les modifications faites à la main sur la page reviennent dans le dépôt

La porteuse modifie des planches directement sur la page du canevas. Au début de chaque séance, après R1, comparer les fichiers du canevas à ceux du dépôt (la liste donne les tailles ; pour les planches à ressources, comparer aux copies de `outils/preparer-publication.py`) ; pour chaque fichier différent, lire la version du canevas et l'enregistrer dans le dépôt avant toute autre chose. Une publication refusée pour conflit signifie la même chose : relire d'abord, publier ensuite. Une taille identique ne prouve pas l'absence de retouche : avant de remplacer une planche, lire sa version en ligne et la comparer à celle du dépôt. On n'écrase jamais une modification de la porteuse.

### R4. Qui écrit dans le canevas

Seulement le compte de la porteuse : elle-même sur la page, et les sessions Claude Code ouvertes avec ce compte. Jamais un autre compte ni une autre organisation (c'est ce qui a rendu l'ancien canevas illisible : versions 280 à 342 publiées depuis un compte d'une autre organisation, passation du 22/10). Ne pas transférer la propriété du canevas ; ne pas donner de droit d'écriture hors de l'organisation.

### R5. Une seule session à la fois

Sur le canevas comme sur la branche de travail. Deux sessions le 31/10 ont écrit sur la même branche : conflits. Avant de pousser, `git fetch` et relire ce qui a changé.

### R6. Ce qui ne se fait pas sans l'accord de la porteuse

Publier une planche nouvelle ou une refonte (une proposition se montre d'abord en captures), supprimer une planche ou une ressource, fusionner des branches, ouvrir une PR, modifier `FICOLIA_DESIGN.md`, répondre à un commentaire sur un canevas.

## Reprise

La note de reprise du 21/10 (`Ficolia — note de reprise.md`, racine) et son complément du 31/10 (`Ficolia — note de reprise, complément du 31-10.md`, racine ; journaux des 22 et 29/10 dans `propositions/`) disent l'état des décisions (1 à 269 ; les 218 à 269, des 01 au 04/11, au §2 bis du complément), des commentaires et de ce qui reste à faire. Depuis le 02/11, il ne manque plus aucune planche au dépôt ; l'état du prototype, l'usage de l'outil « Artifact » et la portée du contrôle R3 sont en tête de `prototype/LISEZ-MOI.md`. Les choix des 01 et 02/11 : `propositions/2026-11-02-voie-savon/journal-01-02-11.md`. **Ce qui reste à faire, par ordre de priorité, tâche par tâche, jusqu'à la clôture du prototype et aux tests : `prototype/A-FAIRE.md`** (à tenir à jour à chaque séance ; commencer par sa section « Reprendre ici » ; les numéros du planning y sont repris, les coches restent dans la page « Planning Ficolia »).
