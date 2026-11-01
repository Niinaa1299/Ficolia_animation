// Le bas de l'écran, instant par instant : la ligne du pré, le haut du fondu de l'herbe et du socle (le vert pâle du bas),
// la part de l'écran qu'ils couvrent, et l'opacité du texte. Repère de l'écran : 390 × 844.
// Usage : node bas-ecran.mjs <maquette> "<réglages>" [de] [à] [pas], par exemple "transition=recul3" 5000 10000 250 (en ms).
// Avec recul3 (29/10), le vert pâle est accroché au pré : son haut suit la ligne du pré, et il couvre l'écran d'un bord à l'autre.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, q = '', de = '5000', a = '', pas = '250'] = process.argv;
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 900 } });
const erreurs = []; p.on('pageerror', e => erreurs.push(String(e))); p.on('console', m => { if (m.type() === 'error') erreurs.push(m.text()); });
await p.goto('file://' + file + '?t=0&notes=off&' + q); await p.waitForTimeout(400);
// La ligne du pré, dans le monde, selon le décor (DECORS dans le gabarit ; le script de la page ne les expose pas).
const G = { a: 712, b: 712, c: 800 }[new URLSearchParams(q).get('decor') || 'a'];
const r = await p.evaluate(([de, a, pas, G]) => {
  const sc = document.getElementById('scrub'); sc.step = 'any';
  const scene = document.getElementById('scene'), monde = document.getElementById('monde');
  const socleR = document.querySelector('#socle rect'), fonduR = document.querySelector('#fondu rect');
  const socle = document.getElementById('socle'), voile = document.getElementById('voile');
  const copy = document.getElementById('copy'), actions = document.getElementById('actions');
  const out = [];
  for (let t = +de; t <= (a ? +a : +sc.max); t += +pas) {
    sc.value = t; sc.dispatchEvent(new Event('input'));
    const S = scene.getBoundingClientRect(), kx = 390 / S.width, ky = 844 / S.height;
    const rep = el => { const R = el.getBoundingClientRect(); return { x0: (R.left - S.left) * kx, x1: (R.right - S.left) * kx, y0: (R.top - S.top) * ky, y1: (R.bottom - S.top) * ky }; };
    const m = (monde.getAttribute('transform') || '').match(/scale\(([-\d.]+)\) translate\(([-\d.]+) ([-\d.]+)\)/);
    const so = socleR ? rep(socleR) : {}, fo = fonduR ? rep(fonduR) : {};
    out.push({ t, pre: m ? 422 + +m[1] * (G + +m[3]) : NaN, z: m ? +m[1] : NaN, so, fo,
      opSocle: +(socle.getAttribute('opacity') ?? 1), voile: +(voile.getAttribute('opacity') ?? 1),
      texte: +getComputedStyle(copy).opacity, boutons: +getComputedStyle(actions).opacity });
  }
  return out;
}, [de, a, pas, G]);
const f = (v, n = 6, d = 0) => (Number.isFinite(v) ? v.toFixed(d) : '—').padStart(n);
console.log('     t    pré  zoom | vert pâle : haut  gauche  droite    bas | fondu : haut | op. socle  voile | texte boutons');
for (const o of r) console.log(f(o.t), f(o.pre), f(o.z, 5, 2), '|', f(o.so.y0, 16), f(o.so.x0, 7), f(o.so.x1, 7), f(o.so.y1, 6), '|', f(o.fo.y0, 12), '|', f(o.opSocle, 9, 2), f(o.voile, 6, 2), '|', f(o.texte, 5, 2), f(o.boutons, 7, 2));
// Le vert pâle doit couvrir l'écran d'un bord à l'autre, et jusqu'en bas, dès qu'il y paraît.
const trous = r.filter(o => o.so.y0 < 844 && o.opSocle > 0 && (o.so.x0 > 0 || o.so.x1 < 390 || o.so.y1 < 844));
console.log(trous.length ? 'BORDS VISIBLES : ' + trous.map(o => o.t).join(', ') + ' ms' : 'le vert pâle couvre l’écran à chaque instant où il y paraît');
console.log('erreurs :', erreurs.length ? erreurs : 'aucune');
await b.close();
