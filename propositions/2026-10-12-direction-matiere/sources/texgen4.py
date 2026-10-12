import numpy as np, sys
from PIL import Image
from scipy.ndimage import gaussian_filter
sys.path.insert(0, sys.argv[1]); from texgen import smooth_noise, hexrgb
from texgen2 import lit

def baume(w, h, seed=8):
    """Matte balm swatch: one spatula stroke with fine drag marks and soft pores, little gloss."""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    a = np.deg2rad(-12); cx, cy = w * .46, h * .52
    u = (xx - cx) * np.cos(a) + (yy - cy) * np.sin(a)
    v = -(xx - cx) * np.sin(a) + (yy - cy) * np.cos(a)
    n1 = smooth_noise(h, w, 300, rng, 3)
    v2 = v + n1 * w * .05
    width = w * (.30 + .06 * (u / w))
    d = np.abs(v2) / width
    body = np.clip(1 - d, 0, 1) ** .35
    start = 1 / (1 + np.exp(-(u + w * .62) / (w * .035)))
    end = 1 / (1 + np.exp((u - w * .55) / (w * .12)))
    body *= start * end
    drag = smooth_noise(h, w, 9, rng, 1)                    # fine streaks along the stroke
    drag = gaussian_filter(drag, (1, 14)) if False else drag
    streak = np.sin(v2 / width * 60 + smooth_noise(h, w, 80, rng, 2) * 6) * .5 + .5
    pores = gaussian_filter(rng.standard_normal((h, w)), 1.4)
    lip = np.exp(-((d - .95) ** 2) / .003) * start * end * .25
    edge_end = np.exp(-((u - w * .5) ** 2) / (w * .05) ** 2) * np.clip(1 - d, 0, 1) * .25
    hgt = body * .45 + streak * body * .025 + lip + edge_end + pores * .004 * (1 - body) + pores * .0025 * body
    hgt = gaussian_filter(hgt, 1.3) * 70
    gmask = 1 - np.clip(body * 4, 0, 1)
    ground = hexrgb('#EFDDD5')[None, None, :] * np.ones((h, w, 1))
    ground = ground * (1 - .05 * (yy / h))[..., None]
    colmap = hexrgb('#FBF4EF')[None, None, :] * (1 - gmask[..., None]) + ground * gmask[..., None]
    return lit(hgt, colmap, gmask, rng, gloss=26, ks=.16, base_lum=.76, occ_k=16, cast_k=.25)

if __name__ == '__main__':
    out = sys.argv[1]
    Image.fromarray((baume(780, 1688) * 255).astype(np.uint8)).save(f'{out}/baume.jpg', quality=85, optimize=True, progressive=True)
    print('ok')
