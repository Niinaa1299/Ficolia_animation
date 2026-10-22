// Vitesse de la vue et du logo, image par image (60 i/s), pour chaque transition : pics et à-coups.
// Usage : node vitesse.mjs <maquette.html> <transition>...
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, ...types] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 900 } });
for (const ty of types) {
  await page.goto('file://' + file + '?t=0&transition=' + ty);
  await page.waitForTimeout(300);
  const r = await page.evaluate(() => {
    const scrub = document.getElementById('scrub'), monde = document.getElementById('monde'), logo = document.getElementById('logo');
    scrub.step = 'any';
    const out = [];
    for (let t = 4460; t <= +scrub.max; t += 1000 / 60) {
      scrub.value = t; scrub.dispatchEvent(new Event('input'));
      const m = monde.getAttribute('transform').match(/scale\(([-\d.]+)\) translate\(([-\d.]+) ([-\d.]+)\)/);
      const l = logo.getAttribute('transform').match(/translate\(([-\d.]+) ([-\d.]+)\)/);
      out.push([t, +m[1], -m[2], -m[3], +l[2]]);
    }
    return out;
  });
  // Vitesse du monde à l'écran (px/s) : le déplacement d'un point fixe du monde au centre de l'écran, plus le zoom.
  let vmax = 0, tmax = 0, amax = 0, tA = 0, prev = null, vprev = null;
  const lignes = [];
  for (const [t, z, x, y, ly] of r) {
    if (prev) {
      const v = Math.hypot((x - prev.x) * z, (y - prev.y) * z) * 60 + Math.abs(Math.log(z / prev.z)) * 422 * 60;
      if (v > vmax) { vmax = v; tmax = t; }
      if (vprev !== null) { const a = Math.abs(v - vprev) * 60; if (a > amax) { amax = a; tA = t; } }
      vprev = v;
      if (Math.round(t) % 250 < 17) lignes.push(`${Math.round(t)}:${Math.round(v)}`);
    }
    prev = { x, y, z };
  }
  console.log(ty.padEnd(10), 'vue : pic', Math.round(vmax), 'px/s à', Math.round(tmax), 'ms ; plus forte variation', Math.round(amax), 'px/s² à', Math.round(tA), 'ms');
  console.log('   ', lignes.join(' '));
}
await browser.close();
