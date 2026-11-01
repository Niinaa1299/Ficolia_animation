import re, sys, html
# Print a compact digest of a .dc.html file: CSS comments + keyframes/animation rules, visible text, props.
for path in sys.argv[1:]:
    src = open(path, encoding="utf-8").read()
    print("=" * 100)
    print("FILE:", path.split("/project/")[-1], f"({len(src)} bytes)")
    t = re.search(r"<title>(.*?)</title>", src)
    print("TITLE:", t.group(1) if t else "-")
    fonts = re.findall(r"family=([^&\"]+)", src)
    print("FONTS:", fonts)
    style = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    # Drop very long path data inside CSS (unlikely) and print the CSS rules compactly
    for line in style.splitlines():
        line = line.strip()
        if not line or line.startswith("body{") or line.startswith("a{"):
            continue
        if len(line) > 400:
            line = line[:400] + " …"
        print("  CSS|", line)
    # Visible text: strip svg blocks, tags
    body = re.sub(r"<svg.*?</svg>", " [svg] ", src, flags=re.S)
    body = re.sub(r"<style>.*?</style>", " ", body, flags=re.S)
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<head>.*?</head>", " ", body, flags=re.S)
    text = re.sub(r"<[^>]+>", "\n", body)
    lines = [html.unescape(l.strip()) for l in text.splitlines() if l.strip() and l.strip() != "[svg]"]
    print("TEXT:", " | ".join(lines)[:1500])
    aria = re.findall(r'aria-label="([^"]+)"', src)
    if aria: print("ARIA:", aria)
    props = re.search(r"data-props='(.*?)'", src, re.S)
    if props: print("PROPS:", props.group(1)[:600])
    scr = re.search(r"<script type=\"text/x-dc\"[^>]*>(.*?)</script>", src, re.S)
    if scr:
        s = scr.group(1).strip()
        print("LOGIC:", (s[:1200] + " …") if len(s) > 1200 else s)
    colors = sorted(set(c.upper() for c in re.findall(r"#[0-9A-Fa-f]{6}\b", src)))
    print("COLORS:", colors)
