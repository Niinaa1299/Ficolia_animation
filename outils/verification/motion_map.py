import re, sys, os, hashlib
# For each file: fonts, number of keyframes, keyframe names, transitions count, reduced-motion support, CSS comments mentioning motion.
rows = []
for path in sorted(sys.argv[1:]):
    src = open(path, encoding="utf-8").read()
    name = os.path.basename(path).replace(".dc.html", "")
    style = "\n".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    kf = re.findall(r"@keyframes\s+([A-Za-z0-9_-]+)", style)
    tr = len(re.findall(r"transition\s*:", style))
    rm = "reduce" in style or ".rm" in style
    fonts = sorted(set(f.split(":")[0].replace("+", " ") for f in re.findall(r"family=([^&\"']+)", src)))
    comments = [re.sub(r"\s+", " ", c).strip() for c in re.findall(r"/\*(.*?)\*/", style, re.S)]
    rows.append((name, fonts, kf, tr, rm, comments))
for name, fonts, kf, tr, rm, comments in rows:
    print(f"{name:42s} fonts={','.join(fonts) or '-':55s} kf={len(kf):2d} tr={tr:2d} rm={'Y' if rm else '-'}")
    if kf:
        print("    keyframes:", " ".join(kf)[:400])
    for c in comments:
        print("    /*", c[:300], "*/")
