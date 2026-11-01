// Détail image par image de la vue autour d'un instant : node vitesse-detail.mjs <maquette> <transition> <de> <à>
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, ty, a, b] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + file + '?t=0&transition=' + ty);
await page.waitForTimeout(300);
const r = await page.evaluate(([a, b]) => {
  const scrub = document.getElementById('scrub'), monde = document.getElementById('monde');
  const out = [];
  for (let t = a; t <= b; t += 1000 / 60) {
    scrub.value = t; scrub.dispatchEvent(new Event('input'));
    const m = monde.getAttribute('transform').match(/scale\(([-\d.]+)\) translate\(([-\d.]+) ([-\d.]+)\)/);
    out.push([Math.round(t), +m[1], -m[2], -m[3]]);
  }
  return out;
}, [+a, +b]);
let p = null;
for (const [t, z, x, y] of r) { console.log(t, z.toFixed(4), x.toFixed(2), y.toFixed(2), p ? `dx ${((x - p[2]) * z).toFixed(2)} dy ${((y - p[3]) * z).toFixed(2)} dz ${(z - p[1]).toFixed(4)}` : ''); p = [t, z, x, y]; }
await browser.close();
