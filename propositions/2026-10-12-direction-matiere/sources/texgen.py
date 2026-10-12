"""Procedural macro textures (cream swipe, serum drops) rendered with continuous lighting, for Ficolia mockups."""
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, zoom
import sys

def smooth_noise(h, w, scale, rng, octaves=4, persistence=.5):
    out = np.zeros((h, w)); amp = 1; tot = 0
    for o in range(octaves):
        gh, gw = max(2, int(h / scale) + 2), max(2, int(w / scale) + 2)
        g = rng.standard_normal((gh, gw))
        up = zoom(g, (h / (gh - 1), w / (gw - 1)), order=3)[:h, :w]
        out += amp * up; tot += amp; amp *= persistence; scale /= 2
    return out / tot

def hexrgb(s):
    s = s.lstrip('#'); return np.array([int(s[i:i + 2], 16) for i in (0, 2, 4)], float) / 255

def shade(hgt, base, shadow_col, ground_mask, light=(-.55, -.65, .55), gloss=60, ks=.35, ks_ground=.04, strength=3.0, ao=1.0, cast=(14, 18), cast_k=.9, rng=None):
    gy, gx = np.gradient(hgt)
    n = np.dstack([-gx * strength, -gy * strength, np.ones_like(hgt)])
    n /= np.linalg.norm(n, axis=2, keepdims=True)
    L = np.array(light); L /= np.linalg.norm(L)
    V = np.array([0, 0, 1.]); H = (L + V); H /= np.linalg.norm(H)
    diff = np.clip(n @ L, 0, 1)
    spec = np.clip(n @ H, 0, 1) ** gloss
    ks_map = ks * (1 - ground_mask) + ks_ground * ground_mask
    # ambient occlusion from local concavity
    occ = np.clip((gaussian_filter(hgt, 18) - hgt) * ao, 0, 1)
    # soft cast shadow: height shifted towards light direction
    dy, dx = cast
    shifted = np.roll(np.roll(hgt, dy, 0), dx, 1)
    sh = np.clip(gaussian_filter(shifted - hgt, 10) * cast_k, 0, 1)
    lum = .62 + .48 * diff - .55 * occ - .45 * sh
    col = base[None, None, :] * lum[..., None] + (shadow_col - base)[None, None, :] * np.clip(occ + sh, 0, 1)[..., None] * .5
    col += (spec * ks_map)[..., None] * np.array([1, .99, .98])
    if rng is not None:
        col += rng.normal(0, .006, col.shape)  # fine grain, kills banding
    return np.clip(col, 0, 1)

def cream(w, h, seed=3, base='#F7EBE5', ground='#EAD6CF', shadow='#B98F8E', angle=-28):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    a = np.deg2rad(angle)
    cx, cy = w * .52, h * .5
    u = (xx - cx) * np.cos(a) + (yy - cy) * np.sin(a)
    v = -(xx - cx) * np.sin(a) + (yy - cy) * np.cos(a)
    n1 = smooth_noise(h, w, 260, rng, 4); n2 = smooth_noise(h, w, 120, rng, 3)
    v2 = v + n1 * w * .09
    width = w * (.34 + .07 * np.tanh(u / (w * .5)))  # widens along stroke
    d = np.abs(v2) / width
    band = np.clip(1 - d, 0, 1)
    band = band ** .55
    taper = 1 / (1 + np.exp(-(u + w * .78) / (w * .05)))  # start of swipe
    body = band * taper
    ridges = (np.sin(v2 / width * 26 + n2 * 4) * .5 + .5) ** 2 * body * .09
    lip = np.exp(-((d - .96) ** 2) / .004) * taper * .32
    hgt = body * .55 + ridges + lip + n2 * .03 + smooth_noise(h, w, 30, rng, 2) * .004
    hgt = gaussian_filter(hgt, 1.6) * 60
    gmask = 1 - np.clip(body * 3, 0, 1)
    col_base = hexrgb(base)[None, None, :] * (1 - gmask[..., None]) + hexrgb(ground)[None, None, :] * gmask[..., None]
    out = shade_map(hgt, col_base, hexrgb(shadow), gmask, rng)
    return out

def shade_map(hgt, colmap, shadow_col, gmask, rng, light=(-.55, -.7, .5), gloss=70, ks=.42, strength=1.0):
    gy, gx = np.gradient(hgt)
    n = np.dstack([-gx * strength, -gy * strength, np.ones_like(hgt)])
    n /= np.linalg.norm(n, axis=2, keepdims=True)
    L = np.array(light); L /= np.linalg.norm(L)
    H = L + np.array([0, 0, 1.]); H /= np.linalg.norm(H)
    diff = np.clip(n @ L, 0, 1)
    spec = np.clip(n @ H, 0, 1) ** gloss * (1 - gmask * .9)
    occ = np.clip((gaussian_filter(hgt, 22) - hgt) / 14, 0, 1)
    shifted = np.roll(np.roll(hgt, 16, 0), 13, 1)
    sh = np.clip(gaussian_filter(shifted - hgt, 9) / 9, 0, 1)
    lum = .55 + .55 * diff - .35 * occ - .38 * sh
    col = colmap * lum[..., None]
    col = col * (1 - (occ + sh)[..., None] * .25) + shadow_col[None, None, :] * ((occ + sh)[..., None] * .25)
    col += spec[..., None] * ks
    col += rng.normal(0, .007, col.shape)
    return np.clip(col, 0, 1)

def drops(w, h, seed=7, base='#F2E3DD', ground2='#E6CFC8', shadow='#B48D8B', tint='#FBF3EF', n=9):
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    g = smooth_noise(h, w, 400, rng, 3)
    colmap = hexrgb(base)[None, None, :] * (1 - (g[..., None] * .5 + .5) * .35) + hexrgb(ground2)[None, None, :] * ((g[..., None] * .5 + .5) * .35)
    hgt = np.zeros((h, w)); mask = np.zeros((h, w))
    placed = []
    sizes = [w * .2, w * .13, w * .09, w * .07, w * .055, w * .045, w * .04, w * .03, w * .025][:n]
    for r in sizes:
        for _ in range(200):
            cx, cy = rng.uniform(r, w - r), rng.uniform(h * .12, h * .88)
            if all((cx - px) ** 2 + (cy - py) ** 2 > (r + pr + w * .03) ** 2 for px, py, pr in placed):
                break
        placed.append((cx, cy, r))
        wob = 1 + .06 * smooth_noise(h, w, r * 1.2, rng, 2)
        rr = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / (r * wob)
        dome = np.clip(1 - rr ** 2, 0, 1) ** .75
        hgt += dome * r * .55; mask = np.maximum(mask, (rr < 1).astype(float) * np.clip((1 - rr) * 8, 0, 1))
    hgt = gaussian_filter(hgt, 1.2)
    gmask = 1 - mask
    drop_col = hexrgb(tint)
    colmap = colmap * gmask[..., None] + (colmap * .55 + drop_col * .45) * mask[..., None]
    out = shade_map(hgt, colmap, hexrgb(shadow), gmask, rng, gloss=140, ks=.9, strength=1.3)
    # caustic: bright crescent on the shadow side of each drop
    caus = np.zeros((h, w))
    for cx, cy, r in placed:
        d = np.sqrt((xx - cx - r * .35) ** 2 + (yy - cy - r * .42) ** 2) / r
        caus += np.exp(-((d - .55) ** 2) / .02) * .35
    out = np.clip(out + caus[..., None] * np.array([1, .96, .9]) * mask[..., None] * .5, 0, 1)
    return out

if __name__ == '__main__':
    out = sys.argv[1]
    W, H = 780, 1688
    Image.fromarray((cream(W, H) * 255).astype(np.uint8)).save(f'{out}/creme.jpg', quality=84, optimize=True, progressive=True)
    Image.fromarray((drops(W, H) * 255).astype(np.uint8)).save(f'{out}/serum.jpg', quality=84, optimize=True, progressive=True)
    print('ok')
