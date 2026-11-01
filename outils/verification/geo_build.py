import re, sys, json
reveal_path, symbol_path, out_json, out_html = sys.argv[1:5]
rev = open(reveal_path, encoding="utf-8").read()
sym = open(symbol_path, encoding="utf-8").read()
K, TX, TY = 1.72, -431.85, -89.0
cf = re.search(r'<clipPath id="fcoCF"><path d="([^"]+)"', rev).group(1)
assert not re.search(r"[a-z]", cf.replace("e-", "")), "relative commands present"
assert set(re.findall(r"[A-Za-z]", cf)) <= set("MCLZ"), set(re.findall(r"[A-Za-z]", cf))
def tf(m):
    nums = [float(v) for v in m.group(2).replace(",", " ").split()]
    pts = []
    for i in range(0, len(nums), 2):
        pts.append(f"{nums[i]*K+TX:.2f} {nums[i+1]*K+TY:.2f}")
    return m.group(1) + " ".join(pts)
flesh = re.sub(r"([MCL])([^MCLZ]*)", tf, cf)
paths = [m.group(1) for m in re.finditer(r'<path d="([^"]+)"', sym)]
data = {"viewBox": [0, 0, 212, 254], "flesh": flesh, "contour": paths[0], "arc": paths[1], "veins": paths[2], "seeds": paths[3:14]}
json.dump(data, open(out_json, "w"), ensure_ascii=False)
svg = f'''<svg viewBox="-4 -4 220 262" width="440" height="524">
<path d="{flesh}" fill="#F2C9A0"/>
<path d="{paths[2]}" fill="#9EBE59"/>{''.join(f'<path d="{s}" fill="#9F3542"/>' for s in paths[3:14])}
<path d="{paths[0]}" fill="#4C2944" fill-opacity=".85"/><path d="{paths[1]}" fill="#4C2944" fill-opacity=".85"/></svg>'''
open(out_html, "w").write(f"<!doctype html><body style='margin:0;background:#fff'>{svg}</body>")
print("flesh len", len(flesh), "seeds", len(paths[3:14]))
