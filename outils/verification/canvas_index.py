import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))
print("TITLE:", c.get("title"))
print("KEYS:", list(c.keys()))
print("LAUNCH:", c.get("launch"))
print("DESIGN SYSTEMS:", c.get("designSystems"))
pages = c.get("pages", [])
print("PAGES:", [(p["id"], p["name"]) for p in pages])
boards = c.get("boards", {})
order = c.get("order", [])
bypage = {}
for name in order:
    b = boards.get(name, {})
    bypage.setdefault(b.get("page", "(first)"), []).append((name, b))
for pg, items in bypage.items():
    print(f"\n## PAGE {pg} ({len(items)} boards)")
    for name, b in sorted(items, key=lambda t: (t[1].get("y", 0), t[1].get("x", 0))):
        extra = {k: v for k, v in b.items() if k not in ("x", "y", "w", "h", "title", "page")}
        print(f"  [{b.get('x')},{b.get('y')} {b.get('w')}x{b.get('h')}] {name} :: {b.get('title','')} {extra if extra else ''}")
notes = c.get("notes", {})
print(f"\n## NOTES ({len(notes)})")
for nid, n in sorted(notes.items(), key=lambda t: (str(t[1].get('page','')), t[1].get('y',0), t[1].get('x',0))):
    txt = n.get("text", "")
    print(f"  - [{n.get('page','(first)')}] ({n.get('kind','sticky')}) @{n.get('x')},{n.get('y')}: {txt}")
for k in c:
    if k not in ("boards","order","notes","pages","title","launch","designSystems","v"):
        print("OTHER KEY", k, json.dumps(c[k])[:500])
