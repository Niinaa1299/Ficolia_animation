"""Builds the shared <svg><defs> block: cleaned fig symbol with flesh, logotype symbol, offset-outline filter."""
import re, math
import os
S=os.path.dirname(os.path.abspath(__file__))

def catmull(points, closed=True, t=0.5):
    n=len(points); d=f'M{points[0][0]:.1f} {points[0][1]:.1f}'
    rng = range(n) if closed else range(n-1)
    for i in rng:
        p0=points[(i-1)%n]; p1=points[i]; p2=points[(i+1)%n]; p3=points[(i+2)%n]
        c1=(p1[0]+(p2[0]-p0[0])*t/3, p1[1]+(p2[1]-p0[1])*t/3)
        c2=(p2[0]-(p3[0]-p1[0])*t/3, p2[1]-(p3[1]-p1[1])*t/3)
        d+=f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return d+(' Z' if closed else '')

def fig_symbol():
    s=open(f'{S}/assets/figue-symbole.svg').read()
    paths=re.findall(r'<path d="([^"]+)"([^>]*)/>',s)
    keep=[]
    for d,a in paths:
        if '#E2D9CD' in a or '#94564B' in a: continue          # restes de vectorisation retirés
        a=a.replace('url(#paint0_linear_2_24)','#4C2944')
        a=re.sub(r' fill-opacity="[^"]*"','',a)
        keep.append(f'<path d="{d}"{a}/>')
    flesh=catmull([(107,29),(135,62),(163,105),(186,140),(196,177),(180,215),(145,240),(112,250),(93,252),(62,234),(38,203),(28,170),(32,135),(55,98),(82,60),(97,40)])
    return keep, flesh

def defs():
    keep, flesh = fig_symbol()
    body=''.join(keep)
    logo=open(f'{S}/assets/logotype-inline.svg').read()
    vb=re.search(r'viewBox="([^"]+)"',logo).group(1)
    inner=logo[logo.find('>')+1:logo.rfind('</svg>')]
    return f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<symbol id="fig" viewBox="0 0 212 254"><path d="{flesh}" fill="#FFFFFF"/>{body}</symbol>
<symbol id="fig-nochair" viewBox="0 0 212 254">{body}</symbol>
<symbol id="fig-sil" viewBox="0 0 212 254"><path d="{flesh}" fill="currentColor"/>{re.sub(r'fill="#[0-9A-Fa-f]{{6}}"','fill="currentColor"',body)}</symbol>
<symbol id="logo" viewBox="{vb}">{inner}</symbol>
<filter id="contour-limites" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
 <feGaussianBlur in="SourceAlpha" stdDeviation="6.5" result="b"/>
 <feComponentTransfer in="b" result="outer"><feFuncA type="discrete" tableValues="0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"/></feComponentTransfer>
 <feComponentTransfer in="b" result="inner"><feFuncA type="discrete" tableValues="0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"/></feComponentTransfer>
 <feComposite in="outer" in2="inner" operator="out" result="ring"/>
 <feFlood flood-color="#4C2944"/><feComposite in2="ring" operator="in"/>
</filter>
<filter id="contour-limites-s" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
 <feGaussianBlur in="SourceAlpha" stdDeviation="2.2" result="b"/>
 <feComponentTransfer in="b" result="outer"><feFuncA type="discrete" tableValues="0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"/></feComponentTransfer>
 <feComponentTransfer in="b" result="inner"><feFuncA type="discrete" tableValues="0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"/></feComponentTransfer>
 <feComposite in="outer" in2="inner" operator="out" result="ring"/>
 <feFlood flood-color="#4C2944"/><feComposite in2="ring" operator="in"/>
</filter>
</defs></svg>'''

if __name__=='__main__':
    open(f'{S}/build/defs.html','w').write(defs())
    print(len(defs()))
