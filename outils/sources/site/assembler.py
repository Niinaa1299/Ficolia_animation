"""Assemble le dossier « Site vitrine Ficolia » à partir de son gabarit.

Usage : python3 -I site/assembler.py <gabarit.html> <donnees.json> <figue-symbole.svg> <textes.md> <fragment.html> <document.html>

Relit les textes proposés contre les mots et formules à ne pas écrire (textes.md §2), pose les espaces
insécables de la typographie française, injecte le logotype manuscrit (figé sur la dernière image de la
révélation) et le symbole de la figue, puis écrit deux sorties : le fragment publié en artifact, et un
document complet, lisible tel quel dans un navigateur.
"""
import html
import json
import math
import re
import sys

gab, don, sym, textes, sortie_fragment, sortie_document = sys.argv[1:7]
page = open(gab, encoding='utf-8').read()
LOGO = json.load(open(don, encoding='utf-8'))['LOGO']
ENCRE, VERT, GRAINE, CHAIR = '#4C2944', '#9EBE59', '#9F3542', '#FFFFFF'


# ---------- Le logotype ----------
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


def logotype():
    # Les couches et les règles de remplissage de la révélation : la chair et les nervures y sont des
    # découpes (règle « nonzero »), le nom, les graines et le contour des tracés pleins (« evenodd »).
    tous = [LOGO['fic'], LOGO['lia'], *LOGO['chair'], *LOGO['nervures'], *LOGO['graines'], *LOGO['contourA'], *LOGO['contourB']]
    x1, y1, x2, y2 = bornes(tous)
    m = 2
    cadre = f'{x1 - m:.1f} {y1 - m:.1f} {x2 - x1 + 2 * m:.1f} {y2 - y1 + 2 * m:.1f}'
    plein = lambda d, c: f'<path d="{d}" fill="{c}" fill-rule="evenodd"/>'
    decoupe = lambda d, c: f'<path d="{d}" fill="{c}"/>'
    couches = [plein(LOGO['fic'], ENCRE), plein(LOGO['lia'], ENCRE)]
    couches += [decoupe(d, CHAIR) for d in LOGO['chair']]
    couches += [decoupe(d, VERT) for d in LOGO['nervures']]
    couches += [plein(d, GRAINE) for d in LOGO['graines']]
    couches += [plein(d, ENCRE) for d in LOGO['contourA'] + LOGO['contourB']]
    return f'<svg viewBox="{cadre}" aria-hidden="true" focusable="false">' + ''.join(couches) + '</svg>'


def symbole():
    s = re.sub(r'<\?xml[^>]*\?>\s*', '', open(sym, encoding='utf-8').read()).strip()
    assert s.startswith('<svg ') and s.endswith('</svg>')
    return s.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)


# ---------- Les mots et formules à ne pas écrire ----------
ECARTEES = ['zéro risque', 'totalement sûr', 'approuvé médicalement', 'scientifiquement validé']  # le brief du site
T533H = ['application de santé']


def interdits():
    t = open(textes, encoding='utf-8').read()
    section = re.search(r'^## 2\..*?$(.*?)^## 3\.', t, re.S | re.M).group(1)
    return re.findall(r'«\s*([^»]+?)\s*»', section)


def textes_proposes(source):
    """Le texte de chaque élément qui porte un texte du site : classes « ts… » et « ms-… »."""
    blocs = re.findall(r'<(dd|p|span) class="(?:ts|ms-)[^"]*"[^>]*>(.*?)</\1>', source, re.S)
    plats = [html.unescape(re.sub(r'<[^>]+>', ' ', b)) for _, b in blocs]
    return [re.sub(r'\s+', ' ', p.replace('\u2019', "'")).strip() for p in plats]


def motif(m):
    corps = re.escape(m).replace(r'\ ', r'\s+')
    return re.compile(r'(?<![\w-])' + corps + r'(?:e|s|es)?(?![\w-])', re.I)


liste = interdits()
proposes = textes_proposes(page)
assert len(liste) >= 20 and len(proposes) > 60, (len(liste), len(proposes))
touches = [(m, p) for m in liste + ECARTEES + T533H for p in proposes if motif(m).search(p)]
if touches:
    for m, p in touches:
        print('MOT À NE PAS ÉCRIRE :', m, '→', p)
    sys.exit(1)
verifier = any(re.search(r'(?<!\w)vérifier(?!\w)', p, re.I) for p in proposes)
bilan = (f'aucun des {len(liste)} n\'y figure, ni les quatre expressions que tu écartes (« zéro risque », '
         '« totalement sûr », « approuvé médicalement », « scientifiquement validé »), ni « application de santé » (T-533 h).')
if verifier:
    bilan += ' « Vérifier », dans ton accroche, n\'est pas « vérifié ».'


# ---------- Assemblage ----------
def espaces(source):
    """Les espaces insécables du français, dans le texte seulement (ni balises, ni styles, ni bloc préformaté)."""
    morceaux = re.split(r'(<style>.*?</style>|<pre[^>]*>.*?</pre>|<[^>]+>)', source, flags=re.S)
    for k in range(0, len(morceaux), 2):
        t = morceaux[k]
        t = re.sub(r' ([:;?!»])', '\u00a0\\1', t)
        t = t.replace('« ', '«\u00a0')
        t = re.sub(r'(\d) (\d{3})(?!\d)', '\\1\u00a0\\2', t)
        t = re.sub(r'(\d) (ms|s|px|Ko|%)(?![\w])', '\\1\u00a0\\2', t)
        t = re.sub(r'(\d) (janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)', '\\1\u00a0\\2', t)
        morceaux[k] = t
    return ''.join(morceaux)


for marque in ('/*@VERIF_MOTS@*/', '/*@LOGO_SVG@*/', '/*@FIGUE_SVG@*/'):
    assert page.count(marque) == 1, marque
page = espaces(page.replace('/*@VERIF_MOTS@*/', bilan))
page = page.replace('/*@LOGO_SVG@*/', logotype()).replace('/*@FIGUE_SVG@*/', symbole())

open(sortie_fragment, 'w', encoding='utf-8').write(page)
tete, corps = page.split('<main', 1)
document = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + tete.strip() + '\n</head>\n<body>\n<main' + corps.strip() + '\n</body>\n</html>\n')
open(sortie_document, 'w', encoding='utf-8').write(document)
print('ok', len(liste), 'mots relus sur', len(proposes), 'textes ;', sortie_fragment, len(page), ';', sortie_document, len(document))
