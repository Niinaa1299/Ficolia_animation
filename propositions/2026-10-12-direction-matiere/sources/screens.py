"""Direction « Matière », version 2 (after the three reviews): key screens, 390 x 844 pt."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phone import AUB, TXT, SEC, CADRE, BORD, BLANC, FONT, text, box, button, svg, logo, fig, phone
import pack, pack2

NB = ' '
LINE = '#8F7F8C'          # 3,5:1 on white: field outlines, inactive marks
V = {1: '#CADCA4', 2: '#E7B93F', 3: '#E27A46', 4: '#B8192C'}   # palette retenue, verdict marks only
VLAB = {1: '[Niveau 1]', 2: '[Niveau 2]', 3: '[Niveau 3]', 4: '[Niveau 4]'}


def ap(s):
    return s.replace("'", '’')


def img(cls, x=0, y=0, w=390, h=844, extra=''):
    return f'<div class="b {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"></div>'


# ---------------------------------------------------------------- icons (24 pt grid, 2 pt stroke)
P = {
    'back': 'M15 5 L8 12 L15 19', 'chev': 'M9 5 L16 12 L9 19', 'close': 'M6 6 L18 18 M18 6 L6 18',
    'heart': 'M12 20 C5 15 3 11.5 3 8.6 C3 6 5 4 7.5 4 C9.4 4 10.9 5.1 12 6.8 C13.1 5.1 14.6 4 16.5 4 C19 4 21 6 21 8.6 C21 11.5 19 15 12 20 Z',
    'search': 'M10.5 4 a6.5 6.5 0 1 0 0.01 0 M15.4 15.4 L20.5 20.5', 'torch': 'M8 3 L16 3 L16 7 L14 10 L14 21 L10 21 L10 10 L8 7 Z M12 13 L12 16',
    'menu': 'M4 7 H20 M4 12 H20 M4 17 H14', 'source': 'M6 3.5 L14 3.5 L18 7.5 L18 20.5 L6 20.5 Z M14 3.5 L14 7.5 L18 7.5 M9 12 L15 12 M9 15.5 L15 15.5',
    'barcode': 'M3 5 V19 M6 5 V19 M9 5 V15 M12 5 V19 M15 5 V15 M18 5 V19 M21 5 V19',
}


def ico(name, x, y, color=TXT, size=24, sw=2):
    k = size / 24
    return (f'<g transform="translate({x} {y}) scale({k})"><path d="{P[name]}" fill="none" stroke="{color}" '
            f'stroke-width="{sw / k if name == "barcode" else sw}" stroke-linecap="round" stroke-linejoin="round"/></g>')


def rbtn(cx, cy, name, on='white'):
    """44 pt round button. on='image' → white .9 + ring; on='white' → cadre; on='cadre' → white."""
    bg = {'image': 'rgba(255,255,255,.9)', 'white': CADRE, 'cadre': BLANC}[on]
    ring = 'box-shadow:0 0 0 1px rgba(31,22,28,.15);backdrop-filter:blur(14px)' if on == 'image' else ''
    return box(cx - 22, cy - 22, 44, 44, bg, 22, extra=ring) + svg(ico(name, cx - 12, cy - 12))


def sheet(y, bg=BLANC):
    return box(0, y, 390, 900 - y, bg, 0, extra='border-radius:32px 32px 0 0')


# ---------------------------------------------------------------- one verdict grammar
def vdot(cx, cy, level, r=6):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{V[level]}" stroke="{TXT}" stroke-opacity=".5" stroke-width="1"/>'


def scale(x, y, w, level, seg_h=8):
    """Hypothèse à valider : échelle à quatre crans. Le cran actif se lit par sa forme (plus haut, cerné)."""
    gap = 8; sw = (w - 3 * gap) / 4; out = ''
    for i in range(4):
        xx = x + i * (sw + gap)
        if i + 1 == level:
            out += f'<rect x="{xx}" y="{y - 3}" width="{sw}" height="{seg_h + 6}" rx="{(seg_h + 6) / 2}" fill="{V[level]}" stroke="{TXT}" stroke-width="1"/>'
        else:
            out += f'<rect x="{xx + .5}" y="{y + .5}" width="{sw - 1}" height="{seg_h - 1}" rx="{seg_h / 2}" fill="none" stroke="{LINE}" stroke-width="1"/>'
    return out


def verdict_card(y, line, level, x=24, w=342):
    c = box(x, y, w, 132, BLANC, 22, extra='box-shadow:0 1px 2px rgba(50,28,49,.05)')
    c += text(x + 20, y + 18, line, size=15, weight=600, color=TXT, lh=1.3)
    c += svg(vdot(x + 28, y + 63, level, 7) + scale(x + 20, y + 102, w - 40, level) + ico('chev', x + w - 38, y + 18, SEC, 22))
    c += text(x + 44, y + 42, VLAB[level], size=30, weight=700, color=TXT, lh=1.2, ls='-0.4px')
    return c


def vline(xr, cy, level, size=15):
    """Dot + label, right-aligned to xr: the compact form used in lists."""
    w = 120
    est = .53 * size * len(VLAB[level])          # Atkinson 600, approximate advance
    return (text(xr - w, cy - size * .65, VLAB[level], size=size, weight=600, color=TXT, lh=1.3, w=w, align='right') +
            svg(vdot(xr - est - 11, cy, level, 5 if size <= 15 else 6)))


# ---------------------------------------------------------------- screens
def s_accueil():
    c = img('tex-baume', 0, -40, 390, 560)
    c += svg(logo(195, 96, 196))
    # légende de planche : le filet part du contour extérieur de la figue, jamais de son centre
    c += svg('<circle cx="220" cy="152" r="2" fill="#321C31"/><path d="M220 152 L228 172" stroke="#321C31" stroke-width=".75" stroke-linecap="round"/>')
    c += text(226, 172, f'Composition{NB}: figue.', size=15, color=TXT, lh=1.3, extra='font-style:italic')
    c += sheet(480)
    c += svg(''.join(f'<rect x="{x}" y="508" width="{w}" height="6" rx="3" fill="{f}"/>' for x, w, f in ((171, 20, AUB), (199, 6, '#9C8D99'), (213, 6, '#9C8D99'))))
    c += text(28, 538, ['Ficolia informe sur la composition', ap("d'un produit cosmétique pendant"), ap("la grossesse et l'allaitement.")], size=22, weight=500, lh=1.3, ls='-0.2px')
    c += text(28, 640, [ap("Ce n'est pas un avis médical. Pour toute"), 'question de santé, adressez-vous à un', f'professionnel de{NB}santé.'], size=16, color=SEC, lh=1.5)
    c += button(24, 748, 342, 56, 'Continuer')
    return phone(c, 'Accueil 1/3', 'Une matière de soin remplit le haut de l’écran. Le logotype porte une légende de planche, tirée du contour de la figue : « Composition&nbsp;: figue. » (Proposition), lue après le texte.', bg='#EFDDD5')


def finder(x, y, w, h, solid=False):
    out = ''
    for (cx, cy, sx, sy) in ((x, y, 1, 1), (x + w, y, -1, 1), (x, y + h, 1, -1), (x + w, y + h, -1, -1)):
        d = f'M{cx} {cy + sy * 30} L{cx} {cy + sy * 18} Q{cx} {cy} {cx + sx * 18} {cy} L{cx + sx * 30} {cy}'
        out += (f'<path d="{d}" fill="none" stroke="#1F161C" stroke-opacity=".45" stroke-width="6.5" stroke-linecap="round"/>'
                f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="{4.5 if solid else 3.5}" stroke-linecap="round"/>')
    return out


def s_camera():
    c = img('tex-baume', 0, -120, 390, 640)
    c += svg(f'<rect x="130" y="214" width="130" height="64" rx="6" fill="#FFFFFF" opacity=".92"/>' + pack.barcode(150, 226, 90, 30) + finder(96, 180, 198, 132))
    c += sheet(480)
    c += text(24, 514, 'Scanner un produit', size=32, weight=700, lh=1.15, ls='-0.6px')
    c += text(24, 566, ['Pour lire le code-barres, Ficolia a besoin', ap("d'accéder à la caméra de votre téléphone.")], size=17, color=SEC, lh=1.5)
    c += button(24, 700, 342, 56, 'Autoriser la caméra')
    c += button(24, 764, 342, 48, 'Rechercher par nom', bg='transparent', color=AUB, weight=600, size=17)
    return phone(c, 'Caméra, au premier scan', 'La demande n’arrive qu’au premier scan (T-232). L’image montre ce que fera la caméra : un viseur sur un code-barres.', bg='#EFDDD5')


def camera_scene(uid, dim=.38, hole=(70, 396, 250, 120), focus_tube=True):
    x, y, w, h = hole
    return (f'<defs><radialGradient id="{uid}k"><stop offset="0" stop-color="#F3E6DF"/><stop offset="1" stop-color="#F3E6DF" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="{uid}r" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#BFA99F"/><stop offset=".55" stop-color="#DCC9C0"/><stop offset="1" stop-color="#A88E84"/></linearGradient>'
            f'<filter id="{uid}f"><feGaussianBlur stdDeviation="9"/></filter><filter id="{uid}g"><feGaussianBlur stdDeviation=".9"/></filter></defs>'
            f'<rect width="390" height="844" fill="url(#{uid}r)"/>'
            f'<g filter="url(#{uid}f)"><circle cx="70" cy="150" r="60" fill="url(#{uid}k)"/><circle cx="330" cy="230" r="80" fill="url(#{uid}k)"/>'
            f'<rect x="-20" y="600" width="430" height="20" fill="#93776D"/><rect x="36" y="430" width="70" height="170" rx="14" fill="#EDE3DE"/>'
            f'<rect x="300" y="400" width="60" height="200" rx="10" fill="#C9D6D8"/></g>'
            f'<g filter="url(#{uid}g)">{pack2.petrol_tube(195, 690, 520, with_code=True)}</g>'
            f'<path fill-rule="evenodd" d="M0 0 H390 V844 H0 Z M{x + 20} {y} h{w - 40} a20 20 0 0 1 20 20 v{h - 40} a20 20 0 0 1 -20 20 h-{w - 40} a20 20 0 0 1 -20 -20 v-{h - 40} a20 20 0 0 1 20 -20 Z" fill="#1F161C" opacity="{dim}"/>')


def thumbs(y):
    items = ((lambda cx, by: pack2.amber(cx, by, 58), 'Sérum hydratant'),
             (lambda cx, by: pack2.white_jar(cx, by, 52), 'Crème riche'),
             (lambda cx, by: pack2.petrol_tube(cx, by, 58), 'Baume lèvres'))
    c, sv = '', ''
    for i, (fn, lab) in enumerate(items):
        x = 24 + i * 118
        c += box(x, y, 106, 74, CADRE, 16)
        sv += fn(x + 53, y + 66)
        c += text(x, y + 80, lab, size=13, weight=600, color=TXT, lh=1.3, w=106, align='center')
    return c + svg(sv)


def s_scanner():
    c = svg(camera_scene('sc'))
    # the tube's barcode sits around y 410 in the scene; the viewfinder frames it
    c += svg(finder(70, 396, 250, 120))
    c += box(110, 532, 170, 34, 'rgba(31,22,28,.72)', 17)
    c += text(110, 539, 'Visez le code-barres', size=15, weight=600, color='#FFFFFF', lh=1.3, w=170, align='center')
    c += rbtn(46, 84, 'menu', 'image') + rbtn(344, 84, 'torch', 'image')
    c += svg(fig(183, 70, 28))
    c += box(0, 584, 390, 280, 'rgba(255,255,255,.95)', 0, extra='border-radius:28px 28px 0 0;backdrop-filter:blur(20px)')
    c += box(177, 594, 36, 5, '#B5A6B1', 3)
    c += box(24, 612, 342, 50, '#F4EFEC', 16, border=LINE) + svg(ico('search', 40, 625, SEC, 22))
    c += text(72, 625, 'Rechercher un produit', size=17, color=SEC, lh=1.4)
    c += text(24, 680, 'Consultés récemment', size=15, weight=600, color=TXT, lh=1.3)
    c += thumbs(706)
    return phone(c, 'Scanner', 'La caméra remplit l’écran ; la consigne est posée sur une capsule pour rester lisible sur n’importe quel fond. Les produits consultés restent lisibles hors réseau (D-91).', bg='#BFA99F', sb_color='#FFFFFF')


def s_scan_ok():
    c = svg(camera_scene('so', dim=.5, hole=(96, 412, 198, 90)))
    c += svg(finder(96, 412, 198, 90, solid=True))
    c += rbtn(344, 84, 'torch', 'image')
    c += box(0, 530, 390, 340, BLANC, 0, extra='border-radius:28px 28px 0 0;box-shadow:0 -10px 30px rgba(31,22,28,.18)')
    c += box(177, 540, 36, 5, '#B5A6B1', 3)
    c += box(24, 558, 56, 56, CADRE, 14) + svg(pack2.petrol_tube(52, 606, 44))
    c += text(96, 562, 'BRUME', size=12, weight=700, color=SEC, lh=1.3, ls='.08em')
    c += text(96, 580, 'Baume lèvres', size=20, weight=600, color=TXT, lh=1.25, ls='-0.2px')
    for i, (line, lv) in enumerate((('Grossesse', 1), ('Allaitement', 2))):
        y = 630 + i * 64
        c += box(24, y, 342, 56, CADRE, 16)
        c += text(40, y + 17, line, size=15, weight=600, color=TXT, lh=1.3)
        c += vline(350, y + 28, lv, 20)
    c += button(24, 762, 342, 48, 'Voir la fiche', bg=BLANC, color=TXT, weight=600, size=17, border=LINE)
    return phone(c, 'Scan réussi', 'Les coins se resserrent sur le code, une vibration légère, et la fiche monte d’en bas. Le symbole s’efface : rien de la marque près d’un verdict (D-115). « Voir la fiche » ouvre la fiche.', bg='#BFA99F', sb_color='#FFFFFF')


def product_screen(packshot, brand, name_lines, g, a, label, caption):
    c = box(0, 0, 390, 844, CADRE, 0) + svg(packshot)
    c += rbtn(38, 84, 'back', 'cadre') + rbtn(352, 84, 'heart', 'cadre')
    c += text(24, 360, brand, size=12, weight=700, color=SEC, lh=1.3, ls='.08em')
    c += text(24, 380, name_lines, size=22, weight=600, color=TXT, lh=1.25, ls='-0.2px')
    y0 = 380 + 27.5 * len(name_lines) + 22
    c += verdict_card(y0, 'Grossesse', g) + verdict_card(y0 + 144, 'Allaitement', a)
    return phone(c, label, caption, bg=CADRE)


def s_produit_a():
    return product_screen(pack2.amber(195, 330, 272), 'ATELIER NACRE', ['Sérum hydratant', ap("à l'acide hyaluronique")], 1, 1,
                          'Fiche produit', 'La photo, l’identité, les deux lignes, rien d’autre (§3.1). Ni figue, ni logo, ni aubergine (D-115). Le verdict est le plus grand texte de l’écran ; la chaleur vient du fond crème et des cartes blanches.')


def s_produit_b():
    return product_screen(pack2.white_jar(195, 322, 196), 'MAISON LÉA', ['Crème riche nourrissante'], 3, 2,
                          'Fiche produit, autre cas', 'Le libellé porte le verdict, la couleur le renforce (T-219, T-220). Hypothèse à valider : l’échelle à quatre crans, où le cran actif se lit par sa forme.')


ING = [(['Aqua'], 'Eau', 1), (['Glycerin'], 'Glycérine', 1), (['Butyrospermum Parkii', 'Butter'], 'Beurre de karité', 1),
       (['Salicylic Acid'], 'Acide salicylique', 3), (['Tocopherol'], 'Vitamine E', 1), (['Parfum'], 'Parfum', 2),
       (['Sodium Hyaluronate'], 'Hyaluronate de sodium', 1), (['Citric Acid'], 'Acide citrique', 1)]


def composition(dim=False):
    c = box(0, 0, 390, 844, CADRE, 0)
    c += rbtn(38, 82, 'back', 'cadre')
    c += text(24, 116, 'Composition', size=32, weight=700, lh=1.15, ls='-0.6px')
    c += text(24, 158, f'Crème riche nourrissante · 24{NB}ingrédients', size=15, color=SEC, lh=1.4)
    c += box(24, 190, 342, 48, '#EFE8E2', 24) + box(28, 194, 167, 40, BLANC, 20, extra='box-shadow:0 1px 3px rgba(50,28,49,.14)')
    c += text(28, 204, 'Grossesse', size=15, weight=600, color=TXT, lh=1.3, w=167, align='center')
    c += text(195, 204, 'Allaitement', size=15, weight=600, color=SEC, lh=1.3, w=167, align='center')
    c += box(16, 254, 358, 620, BLANC, 22)
    y = 254
    for i, (lines, fr, g) in enumerate(ING):
        eh = 21 * (len(lines) - 1)
        c += text(32, y + 15, lines, size=16, weight=600, color=TXT, lh=1.3)
        c += text(32, y + 38 + eh, fr, size=14, color=SEC, lh=1.3)
        c += vline(334, y + 36 + eh / 2, g)
        c += svg(ico('chev', 340, y + 26 + eh / 2, SEC, 18))
        if i < len(ING) - 1:
            c += box(32, y + 71 + eh, 326, 1, BORD)
        y += 72 + eh
    if dim:
        c += box(0, 0, 390, 844, 'rgba(50,28,49,.22)', 0)
    return c


def s_composition():
    return phone(composition(), 'Composition', 'Une seule grammaire de verdict : un point cerné et le libellé en toutes lettres, sans pastille pleine. Les noms passent à la ligne. Hypothèse à valider : un verdict par ingrédient et par ligne, d’où le sélecteur.', bg=CADRE)


def mini_card(x, y, w, line, level):
    c = box(x, y, w, 104, CADRE, 18)
    c += text(x + 16, y + 14, line, size=15, weight=600, color=TXT, lh=1.3)
    c += svg(vdot(x + 22, y + 52, level, 6) + scale(x + 16, y + 80, w - 32, level, 6))
    c += text(x + 36, y + 38, VLAB[level], size=22, weight=700, color=TXT, lh=1.25, ls='-0.2px')
    return c


def s_panneau():
    c = composition(dim=True)
    c += box(0, 292, 390, 560, BLANC, 0, extra='border-radius:28px 28px 0 0;box-shadow:0 -8px 24px rgba(50,28,49,.10)')
    c += box(177, 302, 36, 5, '#B5A6B1', 3)
    c += rbtn(344, 340, 'close', 'white')
    c += text(24, 324, 'Salicylic Acid', size=26, weight=600, lh=1.2, ls='-0.4px')
    c += text(24, 358, 'Acide salicylique', size=15, color=SEC, lh=1.4)
    c += mini_card(24, 394, 165, 'Grossesse', 3) + mini_card(201, 394, 165, 'Allaitement', 2)
    c += text(24, 520, ['[Ce que disent les sources, en mots simples —', 'en attente du toxicologue]'], size=16, color=SEC, lh=1.5)
    c += text(24, 588, 'Sources', size=15, weight=600, color=TXT, lh=1.3)
    y = 616
    for t, d in (('[Titre de la source 1]', f'Publiée le 14{NB}mars 2022'), ('[Titre de la source 2]', f'Publiée le 3{NB}novembre 2019'), ('[Titre de la source 3]', f'Publiée le 21{NB}juin 2016')):
        c += svg(ico('source', 24, y + 6, SEC, 22, 1.7))
        c += text(58, y, t, size=16, weight=600, color=TXT, lh=1.35) + text(58, y + 23, d, size=14, color=SEC, lh=1.35, extra='font-variant-numeric:tabular-nums')
        y += 60
    return phone(c, 'Panneau d’un ingrédient', 'La même carte de verdict, en réduction. Les sources et leur date de publication, seule date admise (D-52, D-94). Un bouton Fermer. Hypothèse à valider : le résumé des sources.', bg=CADRE)


def search_field(q, cursor_x):
    c = box(24, 58, 262, 48, '#F4EFEC', 16, border=AUB) + svg(ico('search', 38, 70, SEC, 22))
    c += text(70, 70, q, size=17, color=TXT, lh=1.4) + box(cursor_x, 70, 1.6, 24, AUB, 1)
    c += button(286, 58, 92, 48, 'Annuler', bg='transparent', color=AUB, weight=600, size=16)
    return c


def s_recherche():
    c = search_field('sérum hyal', 160)
    c += text(24, 132, '3 résultats', size=15, weight=600, color=SEC, lh=1.3)
    rows = [(lambda x, y: pack2.amber(x + 38, y + 70, 64), 'ATELIER NACRE', ['Sérum hydratant', ap("à l'acide hyaluronique")]),
            (lambda x, y: pack2.amber(x + 38, y + 70, 64, label='ORÉE', sub='Sérum'), 'ORÉE', ['Sérum repulpant hyaluronique']),
            (lambda x, y: pack2.user_photo(x, y, 76, 'up1'), 'MAISON LÉA', ['Gel-crème hydratant', 'au hyaluronate'])]
    y = 162; sv = ''
    for fn, brand, lines in rows:
        c += box(24, y, 76, 76, CADRE, 16)
        sv += fn(24, y)
        c += text(116, y + 10, brand, size=12, weight=700, color=SEC, lh=1.3, ls='.08em')
        c += text(116, y + 28, lines, size=17, weight=600, color=TXT, lh=1.3)
        c += box(116, y + 92, 250, 1, BORD)
        y += 100
    c += svg(sv)
    return phone(c, 'Recherche par nom', 'Photo détourée sur fond chaud quand elle existe ; une photo d’utilisatrice, même imparfaite, est cadrée dans le même carré (troisième résultat). Aucun verdict ici : il est sur la fiche.')


def s_recherche_vide():
    c = search_field('sérum xyz', 157)
    c += svg(ico('search', 24, 160, SEC, 40, 1.6))
    c += text(24, 220, [f'Aucun produit ne correspond', f'à «{NB}sérum xyz{NB}»'], size=22, weight=600, lh=1.3, ls='-0.2px')
    c += text(24, 290, ap("Vérifiez l'orthographe, ou scannez"), size=17, color=SEC, lh=1.5)
    c += text(24, 316, 'le code-barres du produit.', size=17, color=SEC, lh=1.5)
    c += button(24, 370, 342, 52, 'Scanner le code-barres', bg=BLANC, color=AUB, weight=600, size=17, border=AUB)
    return phone(c, 'Recherche sans résultat', 'Un état vide qui dit ce qui se passe et propose la suite. Même grammaire : une icône au trait, un titre, une phrase, une action.')


def s_inconnu():
    c = box(0, 0, 390, 844, CADRE, 0)
    c += rbtn(38, 82, 'close', 'cadre')
    c += svg(ico('barcode', 24, 124, SEC, 44))
    c += text(24, 186, ['Nous ne connaissons', 'pas ce produit'], size=32, weight=700, lh=1.15, ls='-0.6px')
    c += text(24, 266, ['Ce code-barres ne correspond à aucun', 'produit de notre base. Aucun verdict ne', f'peut donc être donné pour{NB}lui.'], size=17, color=SEC, lh=1.5)
    c += box(24, 588, 342, 1, BORD)
    c += text(24, 604, ['Votre photo peut servir à ajouter ce produit', f'à la base. Elle ne donne pas de{NB}verdict.'], size=15, color=SEC, lh=1.45)
    c += button(24, 664, 342, 56, 'Photographier les ingrédients', size=17)
    c += button(24, 730, 342, 48, 'Scanner un autre produit', bg='transparent', color=AUB, weight=600, size=17)
    return phone(c, 'Produit inconnu', 'Ni rassurant, ni alarmant (T-196) : pas d’image d’ambiance, la cause dans le premier tiers (T-512). La photo ne promet rien (§5.7, L-7). Variante avec contribution activée.', bg=CADRE)


def s_produit_200():
    c = box(0, 0, 390, 844, CADRE, 0) + svg(pack2.amber(195, 196, 150))
    c += rbtn(38, 82, 'back', 'cadre') + rbtn(352, 82, 'heart', 'cadre')
    c += text(24, 210, 'ATELIER NACRE', size=24, weight=700, color=SEC, lh=1.3, ls='.06em')
    c += text(24, 246, ['Sérum', 'hydratant à', ap("l'acide"), 'hyaluronique'], size=44, weight=600, color=TXT, lh=1.12, ls='-0.6px')
    y = 456
    c += box(24, y, 342, 270, BLANC, 22)
    c += text(44, y + 18, 'Grossesse', size=30, weight=600, color=TXT, lh=1.3)
    c += svg(vdot(54, y + 106, 1, 12) + scale(44, y + 224, 302, 1, 12))
    c += text(80, y + 64, ['[Niveau', '1]'], size=60, weight=700, color=TXT, lh=1.1, ls='-0.8px')
    c += box(24, y + 282, 342, 140, BLANC, 22)
    c += text(44, y + 300, 'Allaitement', size=30, weight=600, color=TXT, lh=1.3)
    c += box(383, 260, 3, 120, 'rgba(50,28,49,.35)', 2)
    return phone(c, 'Fiche produit, texte à 200 %', 'Rien n’est coupé : le nom passe sur quatre lignes, le libellé sur deux, la photo se réduit, les cartes s’empilent et l’écran défile (T-220, T-559).', bg=CADRE)


def all_screens():
    first = [s_accueil(), s_camera()]
    main = [s_scanner(), s_scan_ok(), s_produit_a(), s_produit_b(), s_composition(), s_panneau(),
            s_recherche(), s_recherche_vide(), s_inconnu(), s_produit_200()]
    return first, main
