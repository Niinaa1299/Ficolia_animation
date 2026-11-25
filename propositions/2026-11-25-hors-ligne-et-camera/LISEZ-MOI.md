# Deux propositions du 25/11, en attente de l'accord de la porteuse

Ficolia · prototype · rien de ce dossier n'est publié sur le canevas.

La porteuse a demandé, le 25/11 : « 4. La recherche sans connexion avec le catalogue embarqué : captures d'abord. 5. L'écran d'information caméra propre à Android (ton « ok » au point 13), avec captures d'abord. » puis « tu fais ca maintenant ». Les deux sont construites et rangées ici. Elles entrent dans les planches seulement après son accord (règle R6 de `CLAUDE.md`).

## 1. La recherche sans connexion, dans le catalogue embarqué

**Ce que le registre dit.** `D-91` : hors ligne, les verdicts consultés et les verdicts du catalogue transcrit sont embarqués avec leur identité (nom, marque, contenance). `D-368` (11/11) : un produit du catalogue embarqué s'affiche sans rien envoyer au serveur ; « s'en servir pour chercher un produit par son nom reste à l'étude ». Décision de séance 287 (25/11) : « à modéliser ».

**Ce que la proposition fait** (captures : `captures-recherche-hors-ligne.png`, `captures-en-ligne-et-hors-ligne.png`) :
- sans connexion, le champ de recherche reste actif ;
- seuls les produits évalués, enregistrés dans l'application, sont cherchés ; un produit reconnu mais non évalué n'apparaît pas (comparaison en ligne et hors ligne, avec l'index élargi : à gauche « Lait corps hydratant » et « Lait démaquillant doux » apparaissent, à droite non) ;
- une note, sous le champ : « Sans connexion : la recherche porte sur les produits enregistrés dans l'application. » (Proposition) ;
- sans résultat : « Aucun produit enregistré dans l'application ne correspond à cette recherche. » et, sous le symbole, « Réessayez une fois le téléphone connecté. » (Proposition). Le 02/11, la porteuse avait écarté « Aucun produit ne correspond… » hors ligne, parce que c'était « factuellement faux » : la nouvelle phrase ne parle que des produits enregistrés ;
- ni « Coller la liste des ingrédients », ni invitation à photographier la liste : les deux demandent le réseau ;
- un résultat ouvre l'écran du produit comme en ligne.

**Comment l'appliquer**, une fois l'accord donné : `python3 -I propositions/2026-11-25-hors-ligne-et-camera/appliquer-recherche-hors-ligne.py`, depuis la racine du dépôt. Il ajoute aux neuf copies du gabarit de la recherche un réglage « Sans connexion : recherche », éteint par défaut (l'image des neuf copies ne change pas). Reste à choisir où il s'allume : sur `E2-Recherche-HorsLigne` à la place de l'état actuel, ou sur une planche nouvelle à côté. Essayé le 25/11 sur une copie des neuf sources : appliqué, syntaxe vérifiée.

**Limites.**
- Ce que montre l'écran du verdict ouvert sans connexion n'est pas modélisé ici. `D-437` (TE28-D2, point 1) prévoit que, si la dernière vérification réussie a plus de 15 minutes, le téléphone vérifie sa version avant d'afficher un verdict, « avec une attente bornée ». Ce qui s'affiche quand cette attente échoue n'est pas tranché dans le prototype ; l'écran « Verdict à actualiser · sans connexion » existe déjà pour les données trop anciennes.
- Le catalogue embarqué contient aussi les verdicts déjà consultés (`D-91`) : le prototype ne distingue pas les deux.

## 2. L'écran d'information caméra, sur Android

**Ce que le registre dit.** `O-71`, option A, proposée par Claude : « un écran d'information propre à Android, juste avant la première demande ». `C-322` : l'obligation de Google sur la permission de la caméra ne dépend pas d'un usage de santé ; « l'écran d'avertissement que prévoyait la porteuse était juste pour Android ». Réponse de la porteuse le 25/11 (décision 287) : « ok ».

**Ce que la proposition fait** (planche `E3-Scan-InfoAndroid.dc.html`, copie de « Caméra · demande du téléphone » ; captures : `captures-camera-android.png`) :
1. au premier usage du scanner, sur Android seulement, une carte sur l'image du scanner : « La caméra lit le code-barres », « Ficolia utilise la caméra pour lire le code-barres d'un produit. » (la phrase du motif déjà écrite pour l'iPhone), « Votre téléphone va vous demander l'autorisation. », un seul bouton, « Continuer » (Proposition) ;
2. puis la fenêtre du téléphone, telle qu'Android l'affiche : sans aucun motif écrit par Ficolia, avec « Lorsque vous utilisez l'appli », « Uniquement cette fois-ci », « Ne pas autoriser » ;
3. un refus mène à l'écran actuel « La caméra n'est pas autorisée » ; après un refus, « Activer la caméra » rouvre directement la fenêtre, sans repasser par l'information.

**Écarts à nommer.**
- Au cap (`cap-onboarding.md` §2) : « « Accepter » ouvre le scanner. Rien ne s'intercale entre l'acceptation et le premier scan. » L'écran s'affiche sur le scanner lui-même, et sur Android seulement, mais il s'intercale bien avant la fenêtre du téléphone.
- À la décision 52 du prototype (07/10) : « Pas d'écran avant la demande d'autorisation de la caméra ». Elle valait d'après les règles d'Apple ; elle reste vraie sur iPhone.

**Limites.**
- Les libellés de la fenêtre d'Android sont indicatifs : ils dépendent de la version d'Android et du fabricant. Ils n'ont pas été vérifiés sur un téléphone.
- Le texte exact de l'obligation de Google n'est pas dans le dépôt : il est dans le document des stores, que cette session n'a pas lu.
- La planche n'a pas encore le mécanisme du retour « là d'où l'on vient » (décision 288), posé sur les autres planches après sa construction : à ajouter en l'intégrant.
- Aucun lien n'y mène encore : sur le canevas, « Accepter » mène à la demande telle qu'elle est sur iPhone. Où l'intégrer (un réglage « Téléphone » sur l'accueil, ou la planche seule à côté de la demande) reste à décider.
