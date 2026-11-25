#!/usr/bin/env python3
"""Recherche sans connexion dans le catalogue embarqué (D-91, D-368 ; décision 287 : « à modéliser » ; porteuse, 25/11 :
« captures d'abord »). Proposition du 25/11, en attente de l'accord de la porteuse : ne pas lancer avant.

Ajoute aux neuf copies du gabarit de la recherche un réglage « Sans connexion : recherche » (D-368, décision 287), à deux
valeurs : « Indisponible (02/11) », l'état actuel, par défaut ; « Catalogue embarqué (proposition, 25/11) ». Dans ce second
mode, sans connexion : le champ reste actif ; seuls les produits évalués, enregistrés dans l'application, sont cherchés ;
une note le dit sous le champ ; sans résultat, le texte dit « Aucun produit enregistré dans l'application ne correspond à
cette recherche. » et « Réessayez une fois le téléphone connecté. » ; ni liste collée, ni invitation à contribuer (elles
demandent le réseau). Tous les textes nouveaux : Proposition.

Usage, depuis la racine du dépôt : python3 -I propositions/2026-11-25-hors-ligne-et-camera/appliquer-recherche-hors-ligne.py
Le réglage reste éteint par défaut sur les neuf copies : leur image ne change pas. Pour en faire l'état par défaut d'une
planche (par exemple E2-Recherche-HorsLigne), changer ensuite la valeur « default » de ce réglage dans sa source.
Le script s'arrête sans rien écrire si une ancre manque (une copie a changé depuis le 25/11).
"""
import os
import sys

D = os.path.join('prototype', 'sources', 'project')
COPIES = ['E2-Produit', 'E2-Produit-Gel', 'E2-Recherche', 'E2-Recherche-Aucun', 'E2-Recherche-HorsLigne',
          'E2-Recherche-ListeA', 'E2-Recherche-ListeC', 'E2-Recherche-Resultats', 'E5-Recherche-HorsLigne']
HLCAT = 'Catalogue embarqué (proposition, 25/11)'
STATUS = ('<p role="status" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); '
          'margin: 0">{{srStatus}}</p>')
SCAN = ("Scannez le code-barres du produit avec l'onglet « Scanner » : s'il nous est toujours inconnu, "
        "vous pourrez nous aider à l'ajouter.")


def note(vb):
    return ("<!-- Recherche sans connexion dans le catalogue embarqué (D-91, D-368 ; décision 287 : « à modéliser » ; "
            "porteuse, 25/11 : captures d'abord). Réglage « Sans connexion : recherche ». Textes : Proposition. -->\n"
            '<sc-if value="{{hlCatalogue}}" hint-placeholder-val="{{ false }}">\n'
            '<p role="note" style="margin: 0; display: flex; align-items: flex-start; gap: 8px; font-size: 15px; '
            'line-height: 1.4; color: #FFFFFF"><svg width="20" height="20" ' + vb + '="0 0 24 24" fill="none" '
            'stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
            'style="flex-shrink: 0; margin-top: 1px"><path d="M2 8.5a15 15 0 0 1 20 0"></path><path d="M5.5 12a10 10 0 0 1 '
            '13 0"></path><path d="M9 15.5a5 5 0 0 1 6 0"></path><path d="M12 19h.01"></path><path d="M3 3l18 18"></path>'
            "</svg><span>Sans connexion : la recherche porte sur les produits enregistrés dans l'application.</span></p>\n"
            '</sc-if>\n' + STATUS)


def remplacements(s):
    vb = 'sc-camel-view-box' if 'sc-camel-view-box' in s.split('<sc-if value="{{isSearch}}"')[1][:3000] else 'viewBox'
    return [
        (STATUS, note(vb)),
        ('>Aucun produit ne correspond à cette recherche.</p>', '>{{aucunTexte}}</p>'),
        ('>' + SCAN + '</p>', '>{{fgTexte}}</p>'),
        ("    var depart = D.indexOf(this.props.depart) >= 0 ? this.props.depart : D[0];\n",
         "    var depart = D.indexOf(this.props.depart) >= 0 ? this.props.depart : D[0];\n"
         "    // Sans connexion, recherche dans le catalogue embarqué (D-91, D-368 ; décision 287, proposition) : seuls les produits\n"
         "    // évalués, enregistrés dans l'application, sont cherchés ; ni liste collée, ni invitation à contribuer (elles demandent le réseau).\n"
         "    var hlCat = depart === D[4] && this.props.horsLigneRecherche === '" + HLCAT + "';\n"),
        ("    var large = this.props.catalogue === LARGE || optB;",
         "    var large = (this.props.catalogue === LARGE || optB) && !hlCat;"),
        ("      isSearch: view !== 'product' && depart !== D[4],",
         "      isSearch: view !== 'product' && (depart !== D[4] || hlCat),\n      hlCatalogue: hlCat,\n"
         "      aucunTexte: hlCat ? \"Aucun produit enregistré dans l'application ne correspond à cette recherche.\" : "
         "'Aucun produit ne correspond à cette recherche.',\n"
         "      fgTexte: hlCat ? 'Réessayez une fois le téléphone connecté.' : \"" + SCAN + "\","),
        ("      isOffline: view !== 'product' && depart === D[4],",
         "      isOffline: view !== 'product' && depart === D[4] && !hlCat,"),
        ("      listeA: active && n === 0 && (", "      listeA: !hlCat && active && n === 0 && ("),
        ("      listeC: this.props.liste ===", "      listeC: !hlCat && this.props.liste ==="),
        ("      showContrib: this.props.contribution !== false,",
         "      showContrib: this.props.contribution !== false && !hlCat,"),
        (',&quot;$preview&quot;',
         ',&quot;horsLigneRecherche&quot;:{&quot;editor&quot;:&quot;enum&quot;,&quot;options&quot;:[&quot;Indisponible '
         '(02/11)&quot;,&quot;' + HLCAT + '&quot;],&quot;default&quot;:&quot;Indisponible (02/11)&quot;,&quot;section'
         '&quot;:&quot;Sans connexion : recherche (D-368, décision 287)&quot;},&quot;$preview&quot;'),
    ]


def main():
    sorties = {}
    for b in COPIES:
        f = os.path.join(D, b + '.dc.html')
        s = open(f, encoding='utf-8').read()
        if 'horsLigneRecherche' in s:
            sys.exit(f'{b} : déjà appliqué, rien n\'est écrit')
        for o, n in remplacements(s):
            # E2-Produit-Gel n'a pas la liste collée (copie antérieure au 05/11) : ces deux ancres y manquent, sans dommage.
            if s.count(o) == 0 and o.startswith(('      listeA:', '      listeC:')):
                continue
            if s.count(o) != 1:
                sys.exit(f'{b} : ancre introuvable ou en double ({o[:50]!r}), rien n\'est écrit')
            s = s.replace(o, n)
        sorties[f] = s
    for f, s in sorties.items():
        open(f, 'w', encoding='utf-8').write(s)
        print('appliqué :', os.path.basename(f))


if __name__ == '__main__':
    main()
