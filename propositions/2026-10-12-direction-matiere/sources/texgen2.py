import numpy as np, sys
from PIL import Image
from scipy.ndimage import gaussian_filter, zoom, shift as nd_shift
sys.path.insert(0, sys.argv[1]); from texgen import smooth_noise, hexrgb

def lit(hgt, colmap, gmask, rng, light=(-.5, -.75, .55), gloss=80, ks=.45, strength=1.0, base_lum=.72, occ_k=14, cast=(16, 12), cast_k=.28, warm_shadow='#C99E98'):
    gy, gx = np.gradient(hgt)
    n = np.dstack([-gx * strength, -gy * strength, np.ones_like(hgt)]); n /= np.linalg.norm(n, axis=2, keepdims=True)
    L = np.array(light); L /= np.linalg.norm(L)
    H = L + np.array([0, 0, 1.]); H /= np.linalg.norm(H)
    flatness = np.array([0, 0, 1.]) @ L
    diff = np.clip(n @ L, 0, 1) / flatness  # 1 on flat ground
    spec = np.clip(n @ H, 0, 1) ** gloss
    occ = np.clip((gaussian_filter(hgt, 20) - hgt) / occ_k, 0, 1)
    sh_src = nd_shift(hgt, cast, order=1, mode='nearest')
    sh = np.clip(gaussian_filter(sh_src - hgt, 8) / 10, 0, 1)
    lum = base_lum + (1 - base_lum) * diff - .22 * occ - cast_k * sh
    col = colmap * lum[..., None]
    t = np.clip(occ * .6 + sh * .8, 0, 1)[..., None] * .35
    col = col * (1 - t) + hexrgb(warm_shadow)[None, None, :] * t
    col += (spec * ks * (1 - gmask * .85))[..., None]
    col += rng.normal(0, .0055, col.shape)
    return np.clip(col, 0, 1)

def cream(w, h, seed=5):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    a = np.deg2rad(-24); cx, cy = w * .5, h * .56
    u = (xx - cx) * np.cos(a) + (yy - cy) * np.sin(a)
    v = -(xx - cx) * np.sin(a) + (yy - cy) * np.cos(a)
    n1 = smooth_noise(h, w, 380, rng, 3); n2 = smooth_noise(h, w, 220, rng, 2)
    v2 = v + n1 * w * .06
    width = w * (.40 + .05 * np.tanh(u / (w * .6)))
    d = np.abs(v2) / width
    body = np.clip(1 - d, 0, 1) ** .45
    taper = 1 / (1 + np.exp(-(u + w * 1.05) / (w * .06)))
    body *= taper
    ridges = (np.sin(v2 / width * 15 + n2 * 2.2) * .5 + .5) ** 1.6 * body * .06
    lip = np.exp(-((d - .97) ** 2) / .0025) * taper * .22
    hgt = gaussian_filter(body * .5 + ridges + lip + smooth_noise(h, w, 60, rng, 2) * .006, 2.2) * 70
    gmask = 1 - np.clip(body * 4, 0, 1)
    ground = hexrgb('#F1DDD5') * (1 - .06 * (yy / h))[..., None]
    colmap = hexrgb('#FDF6F2')[None, None, :] * (1 - gmask[..., None]) + ground * gmask[..., None]
    return lit(hgt, colmap, gmask, rng, gloss=55, ks=.38, base_lum=.74)

def serum(w, h, seed=9):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    g = smooth_noise(h, w, 500, rng, 2) * .5 + .5
    ground = hexrgb('#F6E7E1')[None, None, :] * (1 - g[..., None] * .25) + hexrgb('#EBD3CC')[None, None, :] * (g[..., None] * .25)
    hgt = np.zeros((h, w)); mask = np.zeros((h, w)); inner = np.zeros((h, w)); caus = np.zeros((h, w)); rim = np.zeros((h, w))
    spots = [(.66, .30, .19), (.30, .62, .13), (.74, .70, .085), (.22, .26, .06), (.52, .48, .045), (.84, .46, .035), (.40, .84, .05), (.12, .80, .03)]
    for fx, fy, fr in spots:
        cx, cy, r = fx * w, fy * h, fr * w
        wob = 1 + .05 * smooth_noise(h, w, r * 1.4, rng, 2)
        rr = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / (r * wob)
        m = np.clip((1 - rr) * r * .12, 0, 1)
        dome = np.clip(1 - rr ** 2, 0, 1) ** .6
        hgt += dome * r * .5; mask = np.maximum(mask, m)
        inner += np.exp(-(((xx - cx - r * .28) ** 2 + (yy - cy - r * .32) ** 2) / (r * .5) ** 2)) * m
        rim += np.exp(-((rr - .9) ** 2) / .006) * m
        dd = np.sqrt((xx - cx - r * .55) ** 2 + (yy - cy - r * .62) ** 2) / r
        caus += np.exp(-((dd - .78) ** 2) / .03) * (1 - m) * np.clip(1.6 - dd, 0, 1)
    hgt = gaussian_filter(hgt, 1.0)
    gmask = 1 - mask
    col = lit(hgt, ground, gmask, rng, gloss=220, ks=1.0, strength=1.25, base_lum=.82, occ_k=30, cast=(22, 17), cast_k=.35)
    # translucency: inside the drop show the ground, brighter toward the far side, darker rim
    tint = hexrgb('#F9EDE8')
    col = col * (1 - mask[..., None] * .25) + tint * mask[..., None] * .25
    col += inner[..., None] * .10
    col -= rim[..., None] * hexrgb('#5E3C45') * .10
    col += caus[..., None] * np.array([.10, .085, .07])
    return np.clip(col, 0, 1)

if __name__ == '__main__':
    out = sys.argv[1]; W, H = 780, 1688
    for name, fn in (('creme', cream), ('serum', serum)):
        Image.fromarray((fn(W, H) * 255).astype(np.uint8)).save(f'{out}/{name}.jpg', quality=85, optimize=True, progressive=True)
    print('ok')
