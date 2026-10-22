# Usage: python3 -I planche.py <out.png> <img>... : side by side at half size.
import sys
from PIL import Image
out, files = sys.argv[1], sys.argv[2:]
ims = [Image.open(f).convert('RGB') for f in files]
ims = [i.resize((i.width // 2, i.height // 2)) for i in ims]
W = sum(i.width for i in ims) + 8 * (len(ims) - 1); H = max(i.height for i in ims)
c = Image.new('RGB', (W, H), '#bbb'); x = 0
for i in ims: c.paste(i, (x, 0)); x += i.width + 8
c.save(out); print(c.size)
