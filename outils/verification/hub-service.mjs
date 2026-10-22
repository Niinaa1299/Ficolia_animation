// Vérifie l'écran « produit inconnu » dans l'aperçu : pistes, réglages, erreurs.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
await page.goto('file://' + file + '#service');
await page.waitForTimeout(500);
const host = page.locator('#hote-service');
const visible = await page.evaluate(() => [...document.querySelectorAll('.hote')].filter(h => !h.hidden).map(h => h.id));
console.log('visible by default', visible);
const click = async (key, val) => { await host.locator(`.seg[data-key="${key}"] button[data-val="${val}"]`).click(); };
for (const [piste, wait] of [['cafe', 3700], ['ombre', 3100], ['store', 3300], ['petanque', 3500], ['pause', 2900]]) {
  await click('piste', piste);
  await page.waitForTimeout(wait);
  await page.screenshot({ path: `${out}-${piste}.png` });
}
await click('cause', 'inconnue');
console.log('title after cause', await page.evaluate(() => document.getElementById('hote-service').shadowRoot.getElementById('title').textContent));
await page.click('a[data-ecran="formulaire"]');
await page.waitForTimeout(400);
console.log('after switch', await page.evaluate(() => [...document.querySelectorAll('.hote')].filter(h => !h.hidden).map(h => h.id)));
console.log(errs.length ? 'ERRORS\n' + errs.join('\n') : 'no errors');
await browser.close();
