// Usage : node figzoom.mjs <fichier> <sortie.png> <requête>... : la figue de l'ouverture, en gros plan (×5), pour chaque requête.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out, ...queries] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 5 });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
const shots = [];
for (const q of queries) {
  await page.goto('file://' + file + '?' + q);
  await page.waitForTimeout(300);
  const b = await page.evaluate(() => {
    const g = [document.getElementById('figue'), document.getElementById('figLive')].find(e => +e.getAttribute('opacity') !== 0) || document.getElementById('figue');
    const r = g.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height };
  });
  const m = 6;
  shots.push((await page.screenshot({ clip: { x: b.x - m, y: b.y - m, width: b.w + 2 * m, height: b.h + 2 * m } })).toString('base64'));
}
await page.setViewportSize({ width: 1400, height: 900 });
await page.setContent('<body style="margin:0;background:#999;display:flex;flex-wrap:wrap;gap:8px;padding:8px;align-items:flex-start">' + shots.map(s => `<img src="data:image/png;base64,${s}" style="height:300px">`).join('') + '</body>');
await page.screenshot({ path: out, fullPage: true });
console.log(errs.length ? 'ERREURS ' + errs.join(' | ') : 'sans erreur');
await browser.close();
