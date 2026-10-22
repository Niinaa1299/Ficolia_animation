import re, sys, html
# Print the visible text of a .dc.html file, one block per line, without SVG/CSS/JS.
for path in sys.argv[1:]:
    src = open(path, encoding="utf-8").read()
    print("=" * 30, path.split("/project/")[-1])
    body = src.split("<x-dc>", 1)[-1].split("</x-dc>", 1)[0]
    body = re.sub(r"<helmet>.*?</helmet>", " ", body, flags=re.S)
    body = re.sub(r"<svg.*?</svg>", " ", body, flags=re.S)
    body = re.sub(r"</(p|div|h1|h2|h3|h4|li|button|a|label|span|td|th|tr|section|header|footer)>", "\n", body)
    text = re.sub(r"<[^>]+>", " ", body)
    out = []
    for l in text.splitlines():
        l = re.sub(r"\s+", " ", html.unescape(l)).strip()
        if l:
            out.append(l)
    print("\n".join(out))
