"""Primitives for drawing 390 x 844 pt phone frames as HTML + inline SVG (1 pt = 1 CSS px before scaling)."""
import html

AUB = '#4C2944'; PIS = '#9EBE59'; GRE = '#9F3542'; TXT = '#321C31'; SEC = '#6E5A6B'
CADRE = '#FAF8F4'; BORD = '#E7E1DA'; BLANC = '#FFFFFF'
FONT = "'Atkinson Hyperlegible Next', 'Atkinson Hyperlegible', system-ui, sans-serif"
NUNITO = "'Nunito', ui-rounded, system-ui, sans-serif"


def esc(s):
    return html.escape(s, quote=False)


def text(x, y, lines, size=18, weight=400, color=TXT, lh=1.45, w=None, align='left', font=FONT, ls=None, extra=''):
    """lines: list of pre-escaped HTML fragments (explicit line breaks, as measured by the pistes) or one string."""
    if isinstance(lines, str):
        lines = [lines]
    body = '<br>'.join(lines)
    width = f'width:{w}px;' if w else ''
    if align == 'center' and not w:
        style = 'left:0;right:0;text-align:center;'
    else:
        style = f'left:{x}px;{width}text-align:{align};'
    lsp = f'letter-spacing:{ls};' if ls else ''
    return (f'<div class="t" style="{style}top:{y}px;font:{weight} {size}px/{lh} {font};color:{color};{lsp}{extra}">'
            f'{body}</div>')


def box(x, y, w, h, bg='transparent', radius=0, border=None, extra=''):
    b = f'border:1px solid {border};' if border else ''
    return f'<div class="b" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border-radius:{radius}px;{b}{extra}"></div>'


def button(x, y, w, h, label, radius=28, bg=AUB, color=BLANC, weight=700, size=18, border=None, extra=''):
    b = f'border:1px solid {border};' if border else ''
    return (f'<div class="btn" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border-radius:{radius}px;{b}'
            f'color:{color};font:{weight} {size}px/1 {FONT};{extra}">{label}</div>')


def svg(inner, extra=''):
    return f'<svg class="scene" viewBox="0 0 390 844" width="390" height="844" aria-hidden="true" {extra}>{inner}</svg>'


def logo(cx, y, w, extra=''):
    h = w * 180 / 590
    return f'<use href="#logo" x="{cx - w / 2:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" {extra}/>'


def fig(x, y, h, ref='#fig', extra=''):
    w = h * 212 / 254
    return f'<use href="{ref}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" {extra}/>'


def dots(active, y, w_pill=20, h=6, gap=10, inactive=SEC):
    """Pagination: three marks centred on x=195."""
    total = w_pill + 2 * h + 2 * gap
    x = 195 - total / 2
    out = ''
    for i in range(3):
        if i == active:
            out += f'<rect x="{x}" y="{y}" width="{w_pill}" height="{h}" rx="{h / 2}" fill="{AUB}"/>'
            x += w_pill + gap
        else:
            out += f'<circle cx="{x + h / 2}" cy="{y + h / 2}" r="{h / 2}" fill="{inactive}"/>'
            x += h + gap
    return out


def statusbar(color=TXT):
    c = color
    return (f'<div class="sb" style="color:{c}"><span>9:41</span>'
            f'<svg width="68" height="12" viewBox="0 0 68 12" aria-hidden="true"><g fill="{c}">'
            f'<rect x="0" y="7" width="3" height="5" rx="1"/><rect x="5" y="5" width="3" height="7" rx="1"/>'
            f'<rect x="10" y="2.5" width="3" height="9.5" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/>'
            f'<rect x="40" y="0.5" width="24" height="11" rx="3" fill="none" stroke="{c}" stroke-opacity=".45"/>'
            f'<rect x="42" y="2.5" width="18" height="7" rx="1.6"/><rect x="65" y="4" width="2" height="4" rx="1" fill-opacity=".45"/>'
            f'</g></svg></div>')


def phone(content, label, caption, bg=BLANC, sb=True, sb_color=TXT):
    return (f'<figure class="frame"><div class="device"><div class="screen" style="background:{bg}">'
            f'{statusbar(sb_color) if sb else ""}{content}<div class="home"></div></div></div>'
            f'<figcaption><b>{esc(label)}</b><span>{caption}</span></figcaption></figure>')
