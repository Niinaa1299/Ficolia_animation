// Usage: node retour-deux.mjs <file> <outDir> : écran 2 fini, « Retour », puis images figées pendant le retour.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, outDir] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 1 });
const errors = [];
page.on('pageerror', e => errors.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
await page.goto('file://' + file + '?ecran=2&t=4200');
await page.waitForTimeout(400);
await page.locator('#retour').click();
await page.waitForTimeout(50);
console.log('durée du retour :', await page.evaluate(() => document.getElementById('scrub').max));
console.log('déroulé :', await page.evaluate(() => [...document.querySelectorAll('#beats li')].map(li => li.textContent).join(' | ')));
for (const t of [250, 500, 750, 1000, 1300]) {
  await page.evaluate(t => { const s = document.getElementById('scrub'); s.value = t; s.dispatchEvent(new Event('input')); }, t);
  await page.waitForTimeout(80);
  await page.locator('#screen').screenshot({ path: `${outDir}/retour_${t}.png` });
}
console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'no errors');
await browser.close();
