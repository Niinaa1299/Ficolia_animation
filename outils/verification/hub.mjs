import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const errs = [];
const runs = [['light', 1280, 900, '', 'connexion'], ['light', 1280, 900, '#mise-a-jour', 'maj'], ['light', 1280, 900, '#formulaire', 'form'], ['dark', 1280, 900, '#mise-a-jour', 'maj-dark'], ['light', 400, 860, '', 'phone']];
for (const [scheme, w, h, hash, name] of runs) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, colorScheme: scheme });
  page.on('pageerror', e => errs.push(name + ': ' + e));
  page.on('console', m => { if (m.type() === 'error') errs.push(name + ': ' + m.text()); });
  await page.goto('file://' + file + hash);
  await page.waitForTimeout(3200);
  const over = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  await page.screenshot({ path: `${out}-${name}.png` });
  console.log(name, 'overflow', over);
  await page.close();
}
// Bascule par clic : de connexion vers mise à jour, puis retour.
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
page.on('pageerror', e => errs.push('switch: ' + e));
await page.goto('file://' + file);
await page.waitForTimeout(500);
await page.click('a[data-ecran="mise-a-jour"]');
await page.waitForTimeout(400);
await page.click('a[data-ecran="connexion"]');
await page.waitForTimeout(300);
console.log('visible hosts', await page.evaluate(() => [...document.querySelectorAll('.hote')].filter(h => !h.hidden).map(h => h.id)));
console.log(errs.length ? errs.join('\n') : 'no errors');
await browser.close();
