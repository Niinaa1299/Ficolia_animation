"""Construit la page de l'artifact « Ficolia · Récit de la figue » à partir des maquettes.

Usage : python3 outils/apercu.py <maquette.html> <sortie.html>

L'artifact enveloppe lui-même la page (doctype, <html>, <head>, <body>) : on retire donc
cette enveloppe de la maquette, on garde le reste tel quel et on ajoute, en tête, l'état
d'avancement des écrans du récit (FICOLIA_DESIGN.md §2).
"""
import re
import sys

TITRE = "Ficolia · Récit de la figue"

# Les écrans du périmètre, dans l'ordre du brief. état : validee, en-cours, a-venir.
ETAPES = [
    ("Ouverture", "validee", "validée"),
    ("Accueil, trois écrans", "a-venir", "à venir"),
    ("Formulaire envoyé", "a-venir", "à venir"),
    ("Connexion insuffisante ou absente", "a-venir", "à venir"),
    ("Mise à jour obligatoire", "en-cours", "maquette en cours"),
    ("Délai de connexion", "a-venir", "à venir"),
    ("Produit inconnu", "a-venir", "à venir"),
    ("Service indisponible", "a-venir", "à venir"),
]

STYLE = """<style>
.recit{padding-block:20px 0;padding-inline:16px}
.recit-in{max-width:840px;margin:0 auto;display:flex;flex-direction:column;gap:10px}
.recit-sur{margin:0;font-size:13px;font-weight:700;letter-spacing:.04em;color:var(--page-texte-2)}
.recit-etapes{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:6px}
.recit-etapes li{display:flex;align-items:center;gap:8px;min-height:34px;padding:0 12px;border-radius:999px;border:1px solid var(--page-trait);background:var(--surface);font-size:14px;color:var(--page-texte-2)}
.recit-etapes li::before{content:"";width:8px;height:8px;border-radius:50%;border:1.5px solid currentColor;flex:none}
.recit-etapes li[data-etat="validee"]::before{background:currentColor}
.recit-etapes li[data-etat="en-cours"]{border-color:var(--choix);color:var(--page-texte);font-weight:700}
.recit-etapes li[data-etat="en-cours"]::before{background:var(--choix);border-color:var(--choix)}
.recit-etapes small{font-size:12px;font-weight:400;color:var(--page-texte-2)}
@media (max-width:760px){
  .recit-etapes{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
  .recit-etapes::-webkit-scrollbar{display:none}
  .recit-etapes li{flex:none}
}
</style>"""

# Sur téléphone, la rangée défile : on la centre sur l'écran en cours.
SCRIPT = """<script>
document.documentElement.lang = "fr";
(() => {
  const rangee = document.querySelector('.recit-etapes');
  const courant = rangee && rangee.querySelector('[aria-current="step"]');
  if (courant) rangee.scrollLeft = courant.offsetLeft - (rangee.clientWidth - courant.offsetWidth) / 2;
})();
</script>"""


def entete():
    items = []
    for nom, etat, libelle in ETAPES:
        courant = ' aria-current="step"' if etat == "en-cours" else ""
        items.append(f'<li data-etat="{etat}"{courant}><span>{nom}</span><small>{libelle}</small></li>')
    return (
        '<header class="recit" aria-label="Avancement du récit de la figue"><div class="recit-in">'
        '<p class="recit-sur">Ficolia · le récit de la figue</p>'
        f'<ol class="recit-etapes">{"".join(items)}</ol></div></header>'
    )


def construire(source):
    page = source
    for motif in (r"<!doctype html>\s*", r"<html[^>]*>\s*", r"</html>\s*", r"<head>\s*", r"</head>\s*",
                  r"<body>\s*", r"</body>\s*", r'<meta charset="utf-8">\s*', r'<meta name="viewport"[^>]*>\s*'):
        page, n = re.subn(motif, "", page, flags=re.I)
        assert n == 1, f"motif attendu une fois : {motif}"
    page, n = re.subn(r"<title>.*?</title>", f"<title>{TITRE}</title>", page, count=1)
    assert n == 1
    page = page.replace("</style>", "</style>\n" + STYLE, 1)
    page, n = re.subn(r'(<main class="page">)', entete() + r"\n\1", page, count=1)
    assert n == 1
    page += "\n" + SCRIPT + "\n"
    return page


if __name__ == "__main__":
    source, sortie = sys.argv[1], sys.argv[2]
    with open(source, encoding="utf-8") as f:
        page = construire(f.read())
    with open(sortie, "w", encoding="utf-8") as f:
        f.write(page)
    print("ok", sortie, len(page))
