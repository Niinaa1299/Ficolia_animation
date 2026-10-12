"""Studio packshots of fictional products, drawn in SVG (screen coordinates, 390 x 844 reference)."""

_uid = [0]


def _id(p):
    _uid[0] += 1
    return f'{p}{_uid[0]}'


def ground_shadow(cx, y, w, op=.16):
    g = _id('gs')
    return (f'<defs><radialGradient id="{g}"><stop offset="0" stop-color="#3B2433" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="#3B2433" stop-opacity="0"/></radialGradient></defs>'
            f'<ellipse cx="{cx}" cy="{y}" rx="{w / 2}" ry="{w * .07}" fill="url(#{g})"/>')


def serum(cx, base_y, h, label='ATELIER NACRE', sub='Sérum hydratant'):
    """Frosted glass dropper bottle."""
    k = h / 300
    w = 110 * k
    body_h = 190 * k
    x0 = cx - w / 2
    top = base_y - body_h
    gb, gl, gc, gbulb = _id('gb'), _id('gl'), _id('gc'), _id('gbu')
    s = ground_shadow(cx, base_y, w * 1.5)
    s += (f'<defs><linearGradient id="{gb}" x1="0" x2="1"><stop offset="0" stop-color="#E9DCD8"/><stop offset=".18" stop-color="#FBF6F4"/>'
          f'<stop offset=".45" stop-color="#F1E7E4"/><stop offset=".82" stop-color="#E2D2CE"/><stop offset="1" stop-color="#D4C0BC"/></linearGradient>'
          f'<linearGradient id="{gc}" x1="0" x2="1"><stop offset="0" stop-color="#2A1E26"/><stop offset=".3" stop-color="#4A3A44"/><stop offset=".55" stop-color="#2E222A"/><stop offset="1" stop-color="#1D151B"/></linearGradient>'
          f'<linearGradient id="{gbulb}" x1="0" x2="1"><stop offset="0" stop-color="#3A2C35"/><stop offset=".35" stop-color="#5E4C57"/><stop offset="1" stop-color="#241A21"/></linearGradient></defs>')
    s += f'<rect x="{x0}" y="{top}" width="{w}" height="{body_h}" rx="{16 * k}" fill="url(#{gb})"/>'
    # shoulder
    s += f'<rect x="{cx - 26 * k}" y="{top - 14 * k}" width="{52 * k}" height="{20 * k}" rx="{6 * k}" fill="url(#{gb})"/>'
    # collar + bulb
    s += f'<rect x="{cx - 30 * k}" y="{top - 52 * k}" width="{60 * k}" height="{42 * k}" rx="{5 * k}" fill="url(#{gc})"/>'
    s += f'<path d="M{cx - 20 * k} {top - 52 * k} C{cx - 22 * k} {top - 92 * k} {cx - 16 * k} {top - 108 * k} {cx} {top - 108 * k} C{cx + 16 * k} {top - 108 * k} {cx + 22 * k} {top - 92 * k} {cx + 20 * k} {top - 52 * k} Z" fill="url(#{gbulb})"/>'
    # specular streak
    s += f'<rect x="{x0 + 14 * k}" y="{top + 12 * k}" width="{7 * k}" height="{body_h - 30 * k}" rx="{3.5 * k}" fill="#FFFFFF" opacity=".75"/>'
    # label
    s += f'<rect x="{x0 + 14 * k}" y="{top + 70 * k}" width="{w - 28 * k}" height="{70 * k}" rx="{3 * k}" fill="#FFFFFF" opacity=".88"/>'
    s += (f'<text x="{cx}" y="{top + 96 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-weight="700" font-size="{8.5 * k}" letter-spacing="{1.2 * k}" fill="#3A2C35">{label}</text>'
          f'<text x="{cx}" y="{top + 116 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{8 * k}" fill="#6E5A6B">{sub}</text>'
          f'<text x="{cx}" y="{top + 130 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{6.5 * k}" fill="#8C7A88">30 ml</text>')
    return s


def jar(cx, base_y, w, label='MAISON LÉA', sub='Crème riche'):
    k = w / 200
    body_h = 92 * k
    lid_h = 44 * k
    gb, gl = _id('jb'), _id('jl')
    s = ground_shadow(cx, base_y, w * 1.3, .18)
    s += (f'<defs><linearGradient id="{gb}" x1="0" x2="1"><stop offset="0" stop-color="#E7D9D3"/><stop offset=".2" stop-color="#FFFFFF"/>'
          f'<stop offset=".55" stop-color="#F3EAE6"/><stop offset="1" stop-color="#D8C6C0"/></linearGradient>'
          f'<linearGradient id="{gl}" x1="0" x2="1"><stop offset="0" stop-color="#C9A9A6"/><stop offset=".25" stop-color="#EBD3CF"/>'
          f'<stop offset=".6" stop-color="#D9B8B4"/><stop offset="1" stop-color="#B7928F"/></linearGradient></defs>')
    x0 = cx - w / 2
    s += f'<path d="M{x0} {base_y - body_h} L{x0} {base_y - 10 * k} Q{x0} {base_y} {x0 + 14 * k} {base_y} L{x0 + w - 14 * k} {base_y} Q{x0 + w} {base_y} {x0 + w} {base_y - 10 * k} L{x0 + w} {base_y - body_h} Z" fill="url(#{gb})"/>'
    s += f'<rect x="{x0 - 4 * k}" y="{base_y - body_h - lid_h}" width="{w + 8 * k}" height="{lid_h}" rx="{8 * k}" fill="url(#{gl})"/>'
    s += f'<rect x="{x0 + 8 * k}" y="{base_y - body_h - lid_h + 8 * k}" width="{6 * k}" height="{lid_h - 16 * k}" rx="3" fill="#FFFFFF" opacity=".45"/>'
    s += f'<rect x="{x0 + 10 * k}" y="{base_y - body_h + 14 * k}" width="{5 * k}" height="{body_h - 30 * k}" rx="2.5" fill="#FFFFFF" opacity=".8"/>'
    s += (f'<text x="{cx}" y="{base_y - body_h + 40 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-weight="700" font-size="{11 * k}" letter-spacing="{1.6 * k}" fill="#3A2C35">{label}</text>'
          f'<text x="{cx}" y="{base_y - body_h + 60 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{10 * k}" fill="#6E5A6B">{sub}</text>')
    return s


def tube(cx, base_y, h, label='BRUME', sub='Baume lèvres', angle=0):
    k = h / 300
    w = 96 * k
    gb, gc = _id('tb'), _id('tc')
    s = f'<g transform="rotate({angle} {cx} {base_y})">' + ground_shadow(cx, base_y, w * 1.6, .16)
    s += (f'<defs><linearGradient id="{gb}" x1="0" x2="1"><stop offset="0" stop-color="#E4C9C4"/><stop offset=".22" stop-color="#F8EAE6"/>'
          f'<stop offset=".6" stop-color="#EDD6D1"/><stop offset="1" stop-color="#CDAEA9"/></linearGradient>'
          f'<linearGradient id="{gc}" x1="0" x2="1"><stop offset="0" stop-color="#D9D2CE"/><stop offset=".3" stop-color="#FFFFFF"/><stop offset="1" stop-color="#C9C0BC"/></linearGradient></defs>')
    cap_h = 56 * k
    top = base_y - h
    # crimp at top, widening body, cap at bottom (tube stands on its cap)
    s += f'<rect x="{cx - w / 2 + 6 * k}" y="{base_y - cap_h}" width="{w - 12 * k}" height="{cap_h}" rx="{6 * k}" fill="url(#{gc})"/>'
    s += (f'<path d="M{cx - w / 2 + 4 * k} {base_y - cap_h} L{cx - w / 2 - 6 * k} {top + 16 * k} L{cx + w / 2 + 6 * k} {top + 16 * k} L{cx + w / 2 - 4 * k} {base_y - cap_h} Z" fill="url(#{gb})"/>'
          f'<rect x="{cx - w / 2 - 8 * k}" y="{top}" width="{w + 16 * k}" height="{18 * k}" rx="{2 * k}" fill="url(#{gb})"/>')
    s += f'<rect x="{cx - w / 2 + 6 * k}" y="{top + 30 * k}" width="{5 * k}" height="{h - cap_h - 50 * k}" rx="2.5" fill="#FFFFFF" opacity=".7"/>'
    s += (f'<text x="{cx}" y="{top + 120 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-weight="700" font-size="{13 * k}" letter-spacing="{2 * k}" fill="#3A2C35">{label}</text>'
          f'<text x="{cx}" y="{top + 140 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{9 * k}" fill="#6E5A6B">{sub}</text>')
    return s + '</g>'


def barcode(x, y, w, h, seed=3):
    import random
    r = random.Random(seed)
    s = f'<rect x="{x - 6}" y="{y - 6}" width="{w + 12}" height="{h + 18}" rx="3" fill="#FFFFFF"/>'
    xx = x
    while xx < x + w - 2:
        bw = r.choice([1, 1, 1.6, 2.2, 3])
        if r.random() > .38:
            s += f'<rect x="{xx:.1f}" y="{y}" width="{bw}" height="{h}" fill="#1F161C"/>'
        xx += bw + r.choice([1, 1.4, 2])
    s += f'<text x="{x + w / 2}" y="{y + h + 9}" text-anchor="middle" font-family="ui-monospace, monospace" font-size="7.5" letter-spacing="1.4" fill="#1F161C">3 760123 456789</text>'
    return s
