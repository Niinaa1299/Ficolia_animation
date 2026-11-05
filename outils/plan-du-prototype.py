#!/usr/bin/env python3
"""Écrit la planche « Plan du prototype » (prototype/sources/project/E0-Plan.dc.html) : le point de départ du test
de navigation. Elle mène à chaque planche du canevas, rangée par rubrique ; ensuite, les boutons des écrans mènent
à la suite. Décision de la porteuse du 05/11 (« Plan du prototype », tâche 3.21a de prototype/A-FAIRE.md).

Usage, depuis la racine du dépôt :
    python3 -I outils/plan-du-prototype.py
Puis rendre la planche (node outils/rendre.mjs <dossier> prototype/sources/project/E0-Plan.dc.html).

Ce que fait le script :
- les libellés sont les titres des planches dans canvas.json, tels quels (aucun texte d'application nouveau) ;
  le nom de fichier est rappelé dessous, pour retrouver la planche sur le canevas ;
- il s'arrête si une planche de canvas.json manque au plan, y figure deux fois, ou n'existe pas : quand on
  ajoute une planche, on l'ajoute à une rubrique ci-dessous et on relance ;
- il ajoute ou met à jour l'entrée de E0-Plan dans canvas.json (page Étape 0, à droite de « Polices »),
  avec la hauteur donnée par HAUTEUR, à reprendre après rendu si le nombre de lignes change beaucoup.

Limites : le plan ne dit pas comment on arrive à un écran dans l'application ; il y mène directement. Le canevas
n'a pas de retour « à l'écran précédent » : pour revenir au plan, on sort de la lecture et on relance cette planche.
"""
import html, json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(RACINE, "prototype", "sources", "project")
NOM = "E0-Plan.dc.html"
LARGEUR, HAUTEUR = 1600, 4640

# (titre de la rubrique, phrase d'explication, planches dans l'ordre où on les rencontre)
RUBRIQUES = [
    ("Premier lancement", "Ouverture, accueil, caméra, puis les aides de prise en main au moment du geste.",
     "E1-Ouverture-Arbre E1-Ouverture-Arbre-Reduit E1-Accueil-Bienvenue E1-Accueil-Conditions E6-CGU-Accueil "
     "E6-Confidentialite-Accueil E3-Scan-Demande E3-Scan-Refus E3-Scan-Reglages E1-Aide-Scan E1-Aide-Info "
     "E1-Aide-Echelle E1-Aide-Historique E1-Aide-Menu"),
    ("Lancements suivants", "Le scanner, les alertes à l'ouverture et la mise à jour obligatoire.",
     "E1-Scan E1-Code E5-Scan-Alerte E5-Scan-Repere E5-Scan-Alertes E5-Scan-Evalue E5-Scan-AlertesArretees "
     "E3-MiseAJour E3-MiseAJour-Faite"),
    ("Parcours principal · lait corps", "Le produit évalué : produit, verdicts, ingrédients.",
     "E1-Produit E1-Verdict E1-Ingredients E1-Allaitement E1-Ingredients-Allaitement"),
    ("Parcours principal · gel douche", "Le nettoyant du parcours principal (D-354).",
     "E1-Produit-Gel E1-Verdict-Gel E1-Ingredients-Gel E1-Allaitement-Gel E1-Ingredients-Allaitement-Gel"),
    ("Après un scan · le produit a un écran", "Plusieurs versions, évaluation incomplète, verdict à actualiser, rappel de lot.",
     "E3-Produit-AutreVersion E3-Produit-Incomplet E3-Verdict-Incomplet E3-Ingredients-Incomplet "
     "E3-Produit-Actualiser E3-Verdict-Actualiser E3-Ingredients-Actualiser E3-Produit-ActualiserHorsLigne "
     "E3-Verdict-ActualiserHorsLigne E3-Produit-Rappel E3-Verdict-Rappel"),
    ("Après un scan · le type de produit", "La question du type, et ce qu'elle change sur le produit et le verdict.",
     "E3-Question E3-QuestionSuggeree E3-Produit-Type E3-Produit-TypeAPreciser E3-Produit-TypeAutre "
     "E3-Verdict-TypeNonPrecise E3-Ingredients-TypeNonPrecise E3-Verdict-TypeNonPrisEnCharge"),
    ("Après un scan · sans verdict", "Chaque écran dit sa cause.",
     "E3-SansVerdict-Inconnu E3-SansVerdict-NonEvalue E3-SansVerdict-PasCosmetique E3-SansVerdict-Frontiere "
     "E3-SansVerdict-ListeAbsente E3-SansVerdict-Service E3-SansVerdict-Attente E5-SansVerdict-Recherche "
     "E5-SansVerdict-Faible"),
    ("Huile essentielle pure", "Au plancher et hors plancher (étape 7).",
     "E7-NonEvalue E7-Produit E7-Verdict E7-Allaitement E7-Fiche"),
    ("Rechercher", "Par nom, puis le produit trouvé ; les deux produits du parcours principal.",
     "E2-Recherche E2-Recherche-Resultats E2-Recherche-Aucun E2-Recherche-HorsLigne E5-Recherche-HorsLigne "
     "E2-Produit E2-Verdict E2-Ingredients E2-Allaitement E2-Ingredients-Allaitement E2-Produit-Gel "
     "E2-Verdict-Gel E2-Ingredients-Gel E2-Allaitement-Gel E2-Ingredients-Allaitement-Gel "
     "E3-Question-Recherche E3-QuestionSuggeree-Recherche"),
    ("Rechercher · liste d'ingrédients collée", "Pistes A et C (D-344, décisions 271 et 272).",
     "E2-Recherche-ListeA E2-Recherche-ListeC E2-Liste-Coller E2-Liste-Type E2-Liste-Produit E2-Liste-Verdict "
     "E2-Liste-Allaitement"),
    ("Le verdict à ses quatre niveaux", "Le même verdict grossesse, du niveau 1 au niveau 4.",
     "E2-Verdict-N1 E2-Verdict-N2 E2-Verdict-N3 E2-Verdict-N4"),
    ("Historique", "La liste, ses états, et les produits réévalués.",
     "E5-Historique E5-Historique-Vide E5-Historique-Attente E5-Historique-Reevalue E5-Historique-Reevalues "
     "E5-Historique-Evalue E5-Historique-TypeAPreciser E5-Produit E5-Verdict E5-Ingredients E5-Allaitement "
     "E5-Ingredients-Allaitement E5-Produit-Reevalue E5-Allaitement-Reevalue E5-Verdict-Reevalue "
     "E5-Verdict-Reevalue-N3"),
    ("Signaler une erreur", "Les trois départs, puis les états du formulaire.",
     "E4-Signalement E4-Signalement-Allaitement E4-Signalement-Produit E4-Signalement-Reaction "
     "E4-Signalement-Liste E4-Signalement-Type E4-Signalement-Types E4-Signalement-TypeChoisi "
     "E4-Signalement-Message E4-Signalement-Ingredient E4-Signalement-IngredientChoisi "
     "E4-Signalement-IngredientEcrit E4-Signalement-IngredientAbsent E4-Signalement-Verdict "
     "E4-Signalement-ProduitJointes E4-Signalement-ListeJointes E4-Signalement-IngredientJointes "
     "E4-Signalement-Envoye E4-Signalement-Echec"),
    ("Photos", "Contribuer un produit ou une liste, ou joindre des photos à un signalement.",
     "E4-Photo E4-Photo-Liste E4-Photo-Signalement E4-Photo-SignalementIngredient E4-Photo-SignalementProduit "
     "E4-Photo-CameraRefusee E4-Photo-Face E4-Photo-Ingredients E4-Photo-Relecture E4-Photo-Courriel "
     "E4-Photo-CourrielOk E4-Photo-Envoyees E4-Photo-Echec"),
    ("Menu", "Réglages, bonnes pratiques, méthode, « Nous écrire », pages juridiques.",
     "E6-Menu E5-Reglages E5-Reglages-Arret E5-Reglages-Confirmer E5-Reglages-Efface E6-BonnesPratiques-Themes "
     "E6-Fiche-Crevasses E6-Fiche-ToiletteSeins E6-Fiche-DejaUtilise E6-Methode E6-Methode-Lexique E6-Ecrire "
     "E6-Ecrire-Envoye E6-Ecrire-Echec E6-Ecrire-Limite E6-CGU E6-Confidentialite E6-MentionsLegales"),
    ("Ligne allaitement · l'étude", "Quatre produits et leurs verdicts allaitement.",
     "EA-Produit-Lait EA-Verdict-Lait-Sous EA-Verdict-Lait-Orange EA-Ingredients-Lait EA-Verdict-Gel-Source "
     "EA-Produit-Baume EA-Verdict-Baume-Jaune EA-Verdict-Baume-Vert EA-Verdict-Baume-ZoneIncomplete "
     "EA-Verdict-Baume-Incomplet EA-Ingredients-Baume EA-Produit-Spray EA-Verdict-Spray EA-Ingredients-Spray "
     "EA-Produit-Gel EA-Verdict-Gel EA-Ingredients-Gel"),
    ("Variantes comparées · hors parcours", "Pistes mises côte à côte pour choisir ; aucun bouton n'y mène.",
     "E1-Ingredients-Idee1 E1-Ingredients-Idee2 E1-Ingredients-Idee4 E1-Ingredients-Idee5 E5-Echelle-Cercles "
     "E5-Echelle-Barre E5-Echelle-Paliers E5-Echelle-Curseur E5-Echelle-Jauge E5-Info-Bas-N1 E5-Info-Bas-N4 "
     "E5-Info-Libelle-N1 E5-Info-Entete-N3 E5-Info-Volet-N1"),
    ("Traces datées · « CADUC »", "Gardées pour mémoire, sous le titre « CADUC » de la page Ligne allaitement.",
     "EA-Verdict-Lait-Drapeau EA-Verdict-Gel-Icones EA-Verdict-Baume-RenvoiLien EA-Verdict-Renvoi-Panneau "
     "EA-Verdict-Renvoi-Rond EA-Verdict-Renvoi-Photo EA-Ingredients-Spray-Mention"),
    ("Marquées « À supprimer »", "Doublons ; leur suppression attend ta décision.",
     "E4-Signalement-Detail E3-SansVerdict-Source"),
    ("Fondations et traçabilité", "Étape 0.",
     "E0-Fondations E0-Polices E0-Trace-1 E0-Trace-2 E0-Trace-3 E0-Trace-4 E0-Trace-5 E0-Trace-6 E0-Trace-7 "
     "E0-Trace-8"),
]

TETE = """<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8">
<title>Ficolia — Plan du prototype</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;700&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;font-family:"Atkinson Hyperlegible Next","Atkinson Hyperlegible",system-ui,sans-serif;background:#FFFFFF;color:#321C31}
a{color:#4C2944;text-decoration:none}a:hover{color:#321C31;text-decoration:underline}
a:focus-visible{outline:2px solid #4C2944;outline-offset:2px}
</style>
</helmet>
"""

PIED = """</x-dc>
<script type="text/x-dc" data-dc-script="" data-props="{&quot;$preview&quot;:{&quot;width&quot;:%d,&quot;height&quot;:%d}}">
class Component extends DCLogic {
  renderVals() {
    return {};
  }
}
</script>


</body></html>
"""


def main():
    chemin_index = os.path.join(D, "canvas.json")
    index = json.load(open(chemin_index, encoding="utf-8"))
    boards = index["boards"]
    vus, erreurs = {}, []
    for titre, _, liste in RUBRIQUES:
        for stem in liste.split():
            f = stem + ".dc.html"
            if f in vus:
                erreurs.append(f"{stem} figure deux fois ({vus[f]} et {titre})")
            vus[f] = titre
            if f not in boards or not os.path.exists(os.path.join(D, f)):
                erreurs.append(f"{stem} : planche absente du canevas ou du dossier")
    manquantes = [f for f in boards if f != NOM and f not in vus]
    erreurs += [f"{f[:-8]} n'est dans aucune rubrique" for f in manquantes]
    if erreurs:
        sys.exit("Plan non écrit :\n  " + "\n  ".join(erreurs))

    e = html.escape
    out = [TETE]
    out.append(f'<div style="width: {LARGEUR}px; box-sizing: border-box; padding: 56px; background: #FFFFFF; '
               'color: #321C31; display: flex; flex-direction: column; gap: 32px">\n')
    out.append('<div style="display: flex; flex-direction: column; gap: 10px; max-width: 1180px">\n'
               '<span style="font-size: 13px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; '
               'color: #6E5A6B">Prototype · point de départ du test de navigation</span>\n'
               '<h1 style="margin: 0; font-size: 34px; font-weight: 700; line-height: 1.15">Plan du prototype</h1>\n'
               '<p style="margin: 0; font-size: 17px; line-height: 1.5; color: #321C31">Chaque ligne ouvre un écran ; '
               'ensuite, les boutons de l\'écran mènent à la suite. Certains écrans sont aussi des états d\'un autre '
               '(un signalement envoyé, une photo prise) : on y arrive par ici ou en touchant les boutons de l\'écran '
               'd\'avant. Le canevas n\'a pas de retour à l\'écran précédent : pour revenir ici, sortir de la lecture '
               'et relancer cette planche.</p>\n'
               f'<p style="margin: 0; font-size: 15px; line-height: 1.45; color: #6E5A6B">{len(vus)} écrans, '
               f'{len(RUBRIQUES)} rubriques. Sous chaque titre, le nom de la planche sur le canevas.</p>\n</div>\n')
    out.append('<div style="column-count: 4; column-gap: 24px">\n')
    for titre, phrase, liste in RUBRIQUES:
        stems = liste.split()
        out.append('<section style="break-inside: avoid; display: flex; flex-direction: column; margin: 0 0 24px 0; '
                   'padding: 18px 18px 10px 18px; border: 1px solid #E7E1DA; border-radius: 16px; background: #FAF8F4">\n')
        out.append(f'<h2 style="margin: 0; font-size: 19px; font-weight: 700; line-height: 1.25">{e(titre)} '
                   f'<span style="font-size: 14px; font-weight: 400; color: #6E5A6B">· {len(stems)}</span></h2>\n')
        out.append(f'<p style="margin: 4px 0 8px 0; font-size: 14px; line-height: 1.4; color: #6E5A6B">{e(phrase)}</p>\n')
        for i, stem in enumerate(stems):
            bord = "" if i == 0 else " border-top: 1px solid #E7E1DA;"
            out.append(f'<a href="{stem}.dc.html" style="min-height: 44px; box-sizing: border-box; padding: 7px 0;{bord} '
                       'display: flex; flex-direction: column; justify-content: center; gap: 1px">'
                       f'<span style="font-size: 15px; font-weight: 700; line-height: 1.3">{e(boards[stem + ".dc.html"].get("title", stem))}</span>'
                       f'<span style="font-size: 12px; line-height: 1.3; color: #6E5A6B">{e(stem)}</span></a>\n')
        out.append('</section>\n')
    out.append('</div>\n</div>\n')
    out.append(PIED % (LARGEUR, HAUTEUR))
    open(os.path.join(D, NOM), "w", encoding="utf-8").write("".join(out))

    entree = {"h": HAUTEUR, "is_interactive": True, "page": "etape-0",
              "title": "Plan du prototype · point de départ du test de navigation", "w": LARGEUR, "x": 3360, "y": 0}
    if boards.get(NOM) != entree:
        boards[NOM] = entree
        index["boards"] = dict(sorted(boards.items()))
        if NOM not in index["order"]:
            index["order"].insert(0, NOM)
        open(chemin_index, "w", encoding="utf-8").write(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    print(f"{NOM} : {len(vus)} planches, {len(RUBRIQUES)} rubriques ; canvas.json à jour.")


if __name__ == "__main__":
    main()
