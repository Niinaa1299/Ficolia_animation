"""Varied, realistic packshots: amber dropper bottle, petrol-blue tube, white jar, and an imperfect user photo."""
from pack import ground_shadow, _id, barcode


def amber(cx, base_y, h, label='ATELIER NACRE', sub='Sérum hydratant'):
    k = h / 300; w = 104 * k; body_h = 186 * k; x0 = cx - w / 2; top = base_y - body_h
    gb, gc, gu = _id('ab'), _id('ac'), _id('au')
    s = ground_shadow(cx, base_y, w * 1.5, .2)
    s += (f'<defs><linearGradient id="{gb}" x1="0" x2="1"><stop offset="0" stop-color="#4A2614"/><stop offset=".16" stop-color="#8A4E26"/>'
          f'<stop offset=".42" stop-color="#6B3A1C"/><stop offset=".8" stop-color="#4E2814"/><stop offset="1" stop-color="#36190C"/></linearGradient>'
          f'<linearGradient id="{gc}" x1="0" x2="1"><stop offset="0" stop-color="#1E1A1C"/><stop offset=".35" stop-color="#4A4447"/><stop offset=".6" stop-color="#262123"/><stop offset="1" stop-color="#141113"/></linearGradient>'
          f'<linearGradient id="{gu}" x1="0" x2="1"><stop offset="0" stop-color="#2A2527"/><stop offset=".35" stop-color="#5A5356"/><stop offset="1" stop-color="#1A1618"/></linearGradient></defs>')
    s += f'<rect x="{x0}" y="{top}" width="{w}" height="{body_h}" rx="{14 * k}" fill="url(#{gb})"/>'
    s += f'<rect x="{cx - 24 * k}" y="{top - 12 * k}" width="{48 * k}" height="{18 * k}" rx="{5 * k}" fill="url(#{gb})"/>'
    s += f'<rect x="{cx - 28 * k}" y="{top - 50 * k}" width="{56 * k}" height="{40 * k}" rx="{5 * k}" fill="url(#{gc})"/>'
    s += f'<path d="M{cx - 19 * k} {top - 50 * k} C{cx - 21 * k} {top - 90 * k} {cx - 15 * k} {top - 104 * k} {cx} {top - 104 * k} C{cx + 15 * k} {top - 104 * k} {cx + 21 * k} {top - 90 * k} {cx + 19 * k} {top - 50 * k} Z" fill="url(#{gu})"/>'
    s += f'<rect x="{x0 + 12 * k}" y="{top + 10 * k}" width="{6 * k}" height="{body_h - 26 * k}" rx="{3 * k}" fill="#FFE2C4" opacity=".35"/>'
    s += f'<rect x="{x0 + 12 * k}" y="{top + 62 * k}" width="{w - 24 * k}" height="{80 * k}" rx="{2 * k}" fill="#F6F1EA"/>'
    s += (f'<text x="{cx}" y="{top + 90 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-weight="700" font-size="{8.5 * k}" letter-spacing="{1.2 * k}" fill="#2A2224">{label}</text>'
          f'<text x="{cx}" y="{top + 110 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{8 * k}" fill="#5A5054">{sub}</text>'
          f'<text x="{cx}" y="{top + 126 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{6.5 * k}" fill="#7A6F73">30 ml</text>')
    return s


def petrol_tube(cx, base_y, h, label='BRUME', sub='Baume lèvres', with_code=False):
    k = h / 300; w = 96 * k; cap_h = 56 * k; top = base_y - h
    gb, gc = _id('pb'), _id('pc')
    s = ground_shadow(cx, base_y, w * 1.6, .18)
    s += (f'<defs><linearGradient id="{gb}" x1="0" x2="1"><stop offset="0" stop-color="#103B45"/><stop offset=".22" stop-color="#2E6A75"/>'
          f'<stop offset=".6" stop-color="#1D525C"/><stop offset="1" stop-color="#0D2F37"/></linearGradient>'
          f'<linearGradient id="{gc}" x1="0" x2="1"><stop offset="0" stop-color="#C9C4C0"/><stop offset=".3" stop-color="#F4F1EE"/><stop offset="1" stop-color="#B5AFAA"/></linearGradient></defs>')
    s += f'<rect x="{cx - w / 2 + 6 * k}" y="{base_y - cap_h}" width="{w - 12 * k}" height="{cap_h}" rx="{6 * k}" fill="url(#{gc})"/>'
    s += (f'<path d="M{cx - w / 2 + 4 * k} {base_y - cap_h} L{cx - w / 2 - 6 * k} {top + 16 * k} L{cx + w / 2 + 6 * k} {top + 16 * k} L{cx + w / 2 - 4 * k} {base_y - cap_h} Z" fill="url(#{gb})"/>'
          f'<rect x="{cx - w / 2 - 8 * k}" y="{top}" width="{w + 16 * k}" height="{18 * k}" rx="{2 * k}" fill="url(#{gb})"/>')
    s += f'<rect x="{cx - w / 2 + 4 * k}" y="{top + 30 * k}" width="{5 * k}" height="{h - cap_h - 50 * k}" rx="2.5" fill="#FFFFFF" opacity=".28"/>'
    s += (f'<text x="{cx}" y="{top + 100 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-weight="700" font-size="{14 * k}" letter-spacing="{2.4 * k}" fill="#F3EEE8">{label}</text>'
          f'<text x="{cx}" y="{top + 120 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{9 * k}" fill="#CFE0E2">{sub}</text>')
    if with_code:
        s += barcode(cx - 34 * k, top + 150 * k, 68 * k, 26 * k)
    return s


def white_jar(cx, base_y, w, label='MAISON LÉA', sub='Crème riche'):
    k = w / 200; body_h = 90 * k; lid_h = 40 * k; x0 = cx - w / 2
    gb, gl = _id('wb'), _id('wl')
    s = ground_shadow(cx, base_y, w * 1.3, .2)
    s += (f'<defs><linearGradient id="{gb}" x1="0" x2="1"><stop offset="0" stop-color="#DCD8D4"/><stop offset=".2" stop-color="#FFFFFF"/>'
          f'<stop offset=".55" stop-color="#F2F0EE"/><stop offset="1" stop-color="#CFCAC6"/></linearGradient>'
          f'<linearGradient id="{gl}" x1="0" x2="1"><stop offset="0" stop-color="#9A948F"/><stop offset=".25" stop-color="#D8D3CE"/>'
          f'<stop offset=".6" stop-color="#B9B3AE"/><stop offset="1" stop-color="#8C8681"/></linearGradient></defs>')
    s += f'<path d="M{x0} {base_y - body_h} L{x0} {base_y - 10 * k} Q{x0} {base_y} {x0 + 14 * k} {base_y} L{x0 + w - 14 * k} {base_y} Q{x0 + w} {base_y} {x0 + w} {base_y - 10 * k} L{x0 + w} {base_y - body_h} Z" fill="url(#{gb})"/>'
    s += f'<rect x="{x0 - 4 * k}" y="{base_y - body_h - lid_h}" width="{w + 8 * k}" height="{lid_h}" rx="{6 * k}" fill="url(#{gl})"/>'
    s += f'<rect x="{x0 + 10 * k}" y="{base_y - body_h + 14 * k}" width="{5 * k}" height="{body_h - 30 * k}" rx="2.5" fill="#FFFFFF" opacity=".9"/>'
    s += (f'<text x="{cx}" y="{base_y - body_h + 40 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-weight="700" font-size="{11 * k}" letter-spacing="{1.6 * k}" fill="#2E2A28">{label}</text>'
          f'<text x="{cx}" y="{base_y - body_h + 60 * k}" text-anchor="middle" font-family="Atkinson Hyperlegible Next, sans-serif" font-size="{10 * k}" fill="#6A625E">{sub}</text>')
    return s


def user_photo(x, y, size, uid):
    """An imperfect user photo, cropped square: tilted jar on a busy bathroom shelf, warm cast, slight blur."""
    cx, cy = x + size / 2, y + size / 2
    return (f'<defs><clipPath id="{uid}"><rect x="{x}" y="{y}" width="{size}" height="{size}" rx="16"/></clipPath>'
            f'<filter id="{uid}b"><feGaussianBlur stdDeviation=".7"/></filter>'
            f'<linearGradient id="{uid}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8E7B6A"/><stop offset=".6" stop-color="#B9A48E"/><stop offset="1" stop-color="#6E5B4C"/></linearGradient></defs>'
            f'<g clip-path="url(#{uid})"><rect x="{x}" y="{y}" width="{size}" height="{size}" fill="url(#{uid}g)"/>'
            f'<rect x="{x}" y="{y + size * .72}" width="{size}" height="{size * .06}" fill="#5A4A3E" opacity=".6"/>'
            f'<rect x="{x + size * .02}" y="{y + size * .2}" width="{size * .16}" height="{size * .52}" rx="4" fill="#D6E4E6" opacity=".7"/>'
            f'<g filter="url(#{uid}b)" transform="rotate(-7 {cx} {cy})">{white_jar(cx + 4, y + size * .78, size * .62, "MAISON LÉA", "Gel-crème")}</g>'
            f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="#FFB36B" opacity=".08"/></g>')
