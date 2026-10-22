# Vectorise le « o » de l'image du mot complet fournie par la porteuse (22/10), dans le repère des tracés du logo.
# Usage : python -I nom/tracer.py <ficolia-porteuse.png> <sortie.json>
# Dépendances : pillow, numpy, potracer (portage de potrace en Python pur ; vérifié avec potracer 0.0.4).
# Le « o » obtenu est recopié dans outils/sources/arbre/gabarit.html (LETTRE_O), avec le décalage de « lia » (LIA_LETTRES).
import json, sys
import numpy as np
from PIL import Image
import potrace

img, out = sys.argv[1:3]
a = np.array(Image.open(img).convert('RGBA')).astype(float)
rgb = a[..., :3] * (a[..., 3:] / 255) + 255 * (1 - a[..., 3:] / 255)
cov = np.clip((255 - rgb.mean(axis=2)) / (255 - 60), 0, 1)   # couverture d'encre, de 0 à 1 (l'encre est vers 60)

# Les lettres de l'image, séparées par des colonnes vides ; leurs bords au seuil de couverture 0,5.
ink = cov >= 0.5
col = ink.any(axis=0)
groupes, debut = [], None
for x, v in enumerate(col):
    if v and debut is None: debut = x
    if not v and debut is not None: groupes.append((debut, x - 1)); debut = None
assert len(groupes) == 7, groupes                              # F i c o l i a
noms = ['F', 'i1', 'c', 'o', 'l', 'i2', 'a']
bords = {}
for n, (x0, x1) in zip(noms, groupes):
    ys, xs = np.where(ink[:, x0:x1 + 1])
    bords[n] = (x0 + xs.min(), x0 + xs.max() + 1, ys.min(), ys.max() + 1)

# Les mêmes lettres dans les tracés du logo (getBBox des sous-chemins de LOGO.fic et LOGO.lia, donnees.json).
logo = {'F': (16.6, 96.92, 49.1, 194.9), 'i1': (109.29, 158.72, 49.1, 194.94), 'c': (173.02, 242.24, 93.9, 194.94),
        'l': (388.03, 423.76, 37.5, 194.9), 'i2': (434.28, 483.46, 49.1, 194.9), 'a': (498.6, 590.91, 93.9, 195.0)}

# logo = s × image + t : une seule échelle, une translation pour « Fic », une pour « lia » (moindres carrés).
rows, rhs = [], []
for n in logo:
    g = 0 if n in ('F', 'i1', 'c') else 1
    for k in range(4):
        r = [0.0] * 5
        r[0] = bords[n][k]
        r[(1 if k < 2 else 2) + 2 * g] = 1.0
        rows.append(r); rhs.append(logo[n][k])
A, B = np.array(rows), np.array(rhs)
sol = np.linalg.lstsq(A, B, rcond=None)[0]
s, txF, tyF, txL, tyL = sol
ecart = np.abs(A @ sol - B)
print('échelle %.5f ; écart moyen %.2f, max %.2f unités ; « lia » se rapproche de %.2f' % (s, ecart.mean(), ecart.max(), txL - txF))

# Le « o » : agrandi ×4 (bicubique) pour garder la précision de l'anticrénelage, puis seuil 0,5.
# potracer trace les pixels à False : on lui donne l'encre à False.
x0, x1, y0, y1 = 330, 448, 96, 246
K = 4
crop = Image.fromarray((cov[y0:y1, x0:x1] * 255).astype(np.uint8)).resize(((x1 - x0) * K, (y1 - y0) * K), Image.BICUBIC)
plist = potrace.Bitmap(np.array(crop).astype(float) / 255 < 0.5).trace(turdsize=8, alphamax=1.0, opticurve=True, opttolerance=0.2)
P = lambda pt: (s * (x0 + pt.x / K) + txF, s * (y0 + pt.y / K) + tyF)   # pixel agrandi → image → repère de « Fic »
d = []
for c in plist:
    d.append('M%.1f %.1f' % P(c.start_point))
    for g in c.segments:
        if g.is_corner: d.append('L%.1f %.1f L%.1f %.1f' % (P(g.c) + P(g.end_point)))
        else: d.append('C%.1f %.1f %.1f %.1f %.1f %.1f' % (P(g.c1) + P(g.c2) + P(g.end_point)))
    d.append('Z')
assert len(plist) == 2, len(plist)                             # le contour extérieur et le trou
json.dump({'o': ''.join(d), 'echelle': s, 'decalageLia': txF - txL, 'tFic': [txF, tyF]}, open(out, 'w'), indent=1, default=float)
print('ok', out)
