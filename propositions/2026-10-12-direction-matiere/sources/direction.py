"""Builds the « Matière » direction page. usage: python3 direction.py <out.html> [notes.json]"""
import sys, base64, json, html
import os
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D); sys.path.insert(0, D)
from symbols import defs
import screens
from phone import text, box, svg, button, AUB, TXT, SEC, CADRE, BORD
E = lambda s: html.escape(str(s), quote=False)

first, main = screens.all_screens()
b64 = lambda p: base64.b64encode(open(p, 'rb').read()).decode()


def comp(inner, h, w=390):
    return f'<div class="comp" style="--k:1;width:{w}px;height:{h}px"><div class="screen" style="height:{h}px;width:{w}px;transform:none">{inner}</div></div>'


def swatch(hexv, name, note, dark=False):
    return (f'<li class="sw"><span class="chip" style="background:{hexv}"></span>'
            f'<span class="sw-t"><b>{E(name)}</b><code>{hexv}</code><span>{E(note)}</span></span></li>')


TYPE = [
    ('Titre d’écran', 32, 700, 1.15, '-0.6px', 'Composition'),
    ('Verdict', 30, 700, 1.2, '-0.4px', '[Niveau 1]'),
    ('Titre', 22, 600, 1.25, '-0.2px', 'Crème riche nourrissante'),
    ('Texte courant', 17, 400, 1.5, '0', 'Pour lire le code-barres, Ficolia a besoin d’accéder à la caméra.'),
    ('Libellé', 15, 600, 1.3, '0', 'Grossesse · Consultés récemment · Sources'),
    ('Secondaire', 15, 400, 1.4, '0', 'Acide salicylique · Publiée le 14 mars 2022'),
    ('Marque du produit', 12, 700, 1.3, '.08em', 'ATELIER NACRE'),
]


def type_rows():
    rows = ''
    for name, size, wt, lh, ls, sample in TYPE:
        rows += (f'<li class="ty"><span class="ty-meta"><b>{E(name)}</b><span>{size}&nbsp;pt · {wt} · interligne {lh:g}'
                 f'{" · approche " + ls if ls != "0" else ""}</span></span>'
                 f'<span class="ty-s" style="font:{wt} {min(size, 30)}px/{lh} var(--body);letter-spacing:{ls}">{E(sample)}</span></li>')
    return rows


def components():
    vc = comp(screens.verdict_card(12, 'Grossesse', 1), 156)
    pills = comp(''.join(box(24, 10 + i * 40, 342, 36, '#FFFFFF', 0) + text(24, 18 + i * 40, f'Niveau {lvl}', size=15, weight=600, color=SEC, lh=1.3) + screens.vline(366, 28 + i * 40, lvl) for i, lvl in enumerate((1, 2, 3, 4))), 172)
    btn = comp(button(24, 10, 342, 56, 'Continuer'), 76)
    search = comp(box(24, 10, 342, 50, '#F4EFEC', 16) + svg(screens.ico('search', 40, 23, SEC, 22, 2)) + text(72, 23, 'Rechercher un produit', size=17, color=SEC, lh=1.4), 70)
    return f'''
<div class="comps">
  <figure class="cp"><div class="cp-v">{vc}</div><figcaption><b>Carte de verdict</b>La ligne, le libellé en 30&nbsp;pt gras, un point cerné et, en hypothèse, l’échelle à quatre crans. Le libellé porte le sens, la couleur le renforce.</figcaption></figure>
  <figure class="cp"><div class="cp-v">{pills}</div><figcaption><b>Verdict dans une liste</b>Le même point cerné, suivi du libellé en toutes lettres. Pas de pastille pleine : une liste de verdicts ne doit pas faire un mur de feux verts.</figcaption></figure>
  <figure class="cp"><div class="cp-v">{btn}</div><figcaption><b>Bouton principal</b>Le seul aplat aubergine de l’écran. Jamais sur la fiche produit, la composition ni le panneau d’un ingrédient.</figcaption></figure>
  <figure class="cp"><div class="cp-v">{search}</div><figcaption><b>Champ de recherche</b>Un fond chaud plutôt qu’un contour, 50&nbsp;pt de haut, une icône au trait de 2&nbsp;pt comme toutes les autres.</figcaption></figure>
</div>'''


def build(out, notes=None):
    css = open(D + '/frame.css').read() + open(D + '/direction.css').read()
    css += f".tex-baume{{background:url(data:image/jpeg;base64,{b64(D + '/assets/baume.jpg')}) center/cover}}"
    tpl = open(D + '/direction.tpl.html').read()
    rel = ''
    if notes:
        rel = notes
    page = (tpl.replace('/*CSS*/', css).replace('<!--DEFS-->', defs())
            .replace('<!--FIRST-->', ''.join(first)).replace('<!--MAIN-->', ''.join(main))
            .replace('<!--TYPE-->', type_rows()).replace('<!--COMPS-->', components())
            .replace('<!--RELECTURE-->', rel))
    open(out, 'w').write(page)
    print(out, len(page))


if __name__ == '__main__':
    notes = open(sys.argv[2]).read() if len(sys.argv) > 2 else None
    build(sys.argv[1], notes)
