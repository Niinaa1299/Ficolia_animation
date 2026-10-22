"""Assemble la maquette animée du site vitrine à partir de son gabarit.

Usage : python3 -I site/maquette/assembler.py <gabarit.html> <donnees.json> <textes.md> <fragment.html> <document.html>

Relit tout le texte de la page contre les mots et formules à ne pas écrire (textes.md §2), pose les espaces
insécables du français, fabrique les symboles SVG (le logotype en ivoire, la figue ouverte, la figue pleine),
injecte les tracés de la figue de la révélation, puis écrit le fragment publié en artifact et un document complet.
"""
import html
import json
import math
import re
import sys

gab, don, textes, sortie_fragment, sortie_document = sys.argv[1:6]
page = open(gab, encoding='utf-8').read()
donnees = json.load(open(don, encoding='utf-8'))
LOGO, REV = donnees['LOGO'], donnees['REV']
IVOIRE, CHAIR, VERT, GRAINE = '#FFF7F0', '#FFFFFF', '#9EBE59', '#9F3542'


# ---------- La géométrie des tracés ----------
def cubique(a0, a1, a2, a3, t):
    u = 1 - t
    return u ** 3 * a0 + 3 * u * u * t * a1 + 3 * u * t * t * a2 + t ** 3 * a3


def extrema(a0, a1, a2, a3):
    """Les instants, dans ]0, 1[, où la dérivée d'une courbe de Bézier cubique s'annule sur un axe."""
    a, b, c = -a0 + 3 * a1 - 3 * a2 + a3, 2 * (a0 - 2 * a1 + a2), a1 - a0
    if abs(a) < 1e-12:
        racines = [-c / b] if abs(b) > 1e-12 else []
    else:
        disc = b * b - 4 * a * c
        if disc < 0:
            return []
        r = math.sqrt(disc)
        racines = [(-b + r) / (2 * a), (-b - r) / (2 * a)]
    return [t for t in racines if 0 < t < 1]


def bornes(chemins):
    """La boîte englobante exacte de tracés en commandes absolues (M, L, H, V, C, Z)."""
    xs, ys = [], []
    for d in chemins:
        jetons = re.findall(r'[A-Za-z]|-?(?:\d+\.?\d*|\.\d+)', d)
        inconnues = {t for t in jetons if t.isalpha()} - set('MLHVCZ')
        assert not inconnues, inconnues
        pos, cmd, x, y, x0, y0 = 0, None, 0.0, 0.0, 0.0, 0.0
        while pos < len(jetons):
            if jetons[pos].isalpha():
                cmd = jetons[pos]
                pos += 1
                if cmd == 'Z':
                    x, y = x0, y0
                continue
            if cmd in ('M', 'L'):
                x, y = float(jetons[pos]), float(jetons[pos + 1])
                pos += 2
                if cmd == 'M':
                    x0, y0, cmd = x, y, 'L'
            elif cmd == 'H':
                x = float(jetons[pos])
                pos += 1
            elif cmd == 'V':
                y = float(jetons[pos])
                pos += 1
            elif cmd == 'C':
                p = [float(t) for t in jetons[pos:pos + 6]]
                pos += 6
                for axe, coords in ((xs, (x, p[0], p[2], p[4])), (ys, (y, p[1], p[3], p[5]))):
                    axe.extend(cubique(*coords, t) for t in extrema(*coords))
                x, y = p[4], p[5]
            else:
                raise ValueError(cmd)
            xs.append(x)
            ys.append(y)
    return min(xs), min(ys), max(xs), max(ys)


def cadre(chemins, marge=2):
    x1, y1, x2, y2 = bornes(chemins)
    return f'{x1 - marge:.1f} {y1 - marge:.1f} {x2 - x1 + 2 * marge:.1f} {y2 - y1 + 2 * marge:.1f}'


# ---------- Les symboles ----------
# Règles de remplissage de la révélation : la chair et les nervures y sont des découpes (« nonzero »),
# le nom, les graines et le contour des tracés pleins (« evenodd »).
plein = lambda d, c: f'<path d="{d}" fill="{c}" fill-rule="evenodd"/>'
decoupe = lambda d, c: f'<path d="{d}" fill="{c}"/>'
CONTOUR = LOGO['contourA'] + LOGO['contourB']
FIGUE = LOGO['chair'] + LOGO['nervures'] + LOGO['graines'] + CONTOUR
CADRE_FIGUE = '249 48.8 127 152.4'
assert cadre(FIGUE) == '249.0 48.8 127.0 152.4', cadre(FIGUE)
CADRE_LOGO = cadre([LOGO['fic'], LOGO['lia']] + FIGUE)
assert CADRE_LOGO.endswith('578.3 165.7'), CADRE_LOGO

logo_ivoire = (f'<symbol id="logo-ivoire" viewBox="{CADRE_LOGO}">'
               + plein(LOGO['fic'], IVOIRE) + plein(LOGO['lia'], IVOIRE)
               + ''.join(decoupe(d, IVOIRE) for d in LOGO['nervures'])
               + ''.join(plein(d, IVOIRE) for d in LOGO['graines'])
               + ''.join(plein(d, IVOIRE) for d in CONTOUR) + '</symbol>')
figue_ouverte = (f'<symbol id="figue-ouverte" viewBox="{CADRE_FIGUE}">'
                 + ''.join(decoupe(d, CHAIR) for d in LOGO['chair'])
                 + ''.join(decoupe(d, VERT) for d in LOGO['nervures'])
                 + ''.join(plein(d, GRAINE) for d in LOGO['graines'])
                 + ''.join(plein(d, IVOIRE) for d in CONTOUR) + '</symbol>')
figue_pleine = (f'<symbol id="figue-pleine" viewBox="{CADRE_FIGUE}">'
                + ''.join(decoupe(d, IVOIRE) for d in LOGO['chair'])
                + ''.join(plein(d, IVOIRE) for d in CONTOUR) + '</symbol>')
graines = []
for d in LOGO['graines']:
    x1, y1, x2, y2 = bornes([d])
    graines.append([round((x1 + x2) / 2, 1), round((y1 + y2) / 2, 1)])


# ---------- Les mots et formules à ne pas écrire ----------
ECARTEES = ['zéro risque', 'totalement sûr', 'approuvé médicalement', 'scientifiquement validé']  # le brief du site
T533H = ['application de santé']


def interdits():
    t = open(textes, encoding='utf-8').read()
    section = re.search(r'^## 2\..*?$(.*?)^## 3\.', t, re.S | re.M).group(1)
    return re.findall(r'«\s*([^»]+?)\s*»', section)


def texte_visible(source):
    s = re.sub(r'<(style|script)\b.*?</\1>', ' ', source, flags=re.S)
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s)).replace('\u2019', "'")
    return re.sub(r'\s+', ' ', s)


def motif(m):
    corps = re.escape(m).replace(r'\ ', r'\s+')
    return re.compile(r'(?<![\w-])' + corps + r'(?:e|s|es)?(?![\w-])', re.I)


liste = interdits()
visible = texte_visible(page)
assert len(liste) >= 20 and len(visible) > 5000, (len(liste), len(visible))
touches = [(m, visible[max(0, x.start() - 60):x.end() + 60]) for m in liste + ECARTEES + T533H for x in motif(m).finditer(visible)]
if touches:
    for m, contexte in touches:
        print('MOT À NE PAS ÉCRIRE :', m, '→', contexte)
    sys.exit(1)


# ---------- Assemblage ----------
def espaces(source):
    """Les espaces insécables du français, dans le texte seulement (ni balises, ni styles, ni scripts)."""
    morceaux = re.split(r'(<style>.*?</style>|<script>.*?</script>|<[^>]+>)', source, flags=re.S)
    for k in range(0, len(morceaux), 2):
        t = morceaux[k]
        t = re.sub(r' ([:;?!»])', '\u00a0\\1', t)
        t = t.replace('« ', '«\u00a0')
        t = re.sub(r'(\d) (\d{3})(?!\d)', '\\1\u00a0\\2', t)
        t = re.sub(r'(\d) (ms|s|px|Ko|%)(?![\w])', '\\1\u00a0\\2', t)
        t = re.sub(r'(\d) (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)', '\\1\u00a0\\2', t)
        t = re.sub(r'(\d) (sur) (\d)', '\\1\u00a0\\2\u00a0\\3', t)
        morceaux[k] = t
    return ''.join(morceaux)


compact = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':'))
logo_js = {k: LOGO[k] for k in ('chair', 'nervures', 'graines', 'contourA', 'contourB', 'moyeu')}
rev_js = {k: REV[k] for k in ('gV', 'gA', 'gM', 'gS', 'tip')}
for marque in ('/*@SYMBOLES@*/', '/*@LOGO@*/', '/*@REV@*/', '/*@GRAINES@*/'):
    assert page.count(marque) == 1, marque
page = espaces(page)
page = (page.replace('/*@SYMBOLES@*/', logo_ivoire + figue_ouverte + figue_pleine)
        .replace('/*@LOGO@*/', compact(logo_js)).replace('/*@REV@*/', compact(rev_js))
        .replace('/*@GRAINES@*/', compact(graines)))
assert '</script' not in page.split('<script>', 1)[1].rsplit('</script>', 1)[0]

open(sortie_fragment, 'w', encoding='utf-8').write(page)
tete, corps = page.split('<span id="haut">', 1)
document = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + tete.strip() + '\n</head>\n<body>\n<span id="haut">' + corps.strip() + '\n</body>\n</html>\n')
open(sortie_document, 'w', encoding='utf-8').write(document)
print('ok', len(liste), 'mots relus ;', sortie_fragment, len(page), ';', sortie_document, len(document))
