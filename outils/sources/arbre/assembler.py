# Assemble la maquette « l'arbre et la figue » : injecte les tracés dans le gabarit.
# Usage : python3 -I arbre/assembler.py <gabarit.html> <donnees.json> <sortie.html>
import json, sys
gab, don, out = sys.argv[1:4]
src = open(gab, encoding='utf-8').read()
d = json.load(open(don, encoding='utf-8'))
rev = {k: d['REV'][k] for k in ('gV', 'gA', 'gM', 'gS', 'tip')}
for marque, val in (('/*@FIG@*/', d['FIG']), ('/*@LOGO@*/', d['LOGO']), ('/*@REV@*/', rev)):
    assert src.count(marque) == 1, marque
    src = src.replace(marque, json.dumps(val, ensure_ascii=False, separators=(',', ':')))
open(out, 'w', encoding='utf-8').write(src)
print('ok', out, len(src))
