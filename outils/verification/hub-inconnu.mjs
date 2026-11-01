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
await page.goto('file://' + file + '#inconnu');
await page.waitForTimeout(500);
const host = page.locator('#hote-inconnu');
const visible = await page.evaluate(() => [...document.querySelectorAll('.hote')].filter(h => !h.hidden).map(h => h.id));
console.log('visible', visible);
const click = async (key, val) => { await host.locator(`.seg[data-key="${key}"] button[data-val="${val}"]`).click(); };
for (const [piste, wait] of [['tiroir', 3300], ['epaules', 2000], ['lunettes', 3600], ['cagette', 3300], ['presentations', 2900]]) {
  await click('piste', piste);
  await page.waitForTimeout(wait);
  await page.screenshot({ path: `${out}-${piste}.png` });
}
await click('contrib', 'off');
console.log('contrib hidden', await page.evaluate(() => document.getElementById('hote-inconnu').shadowRoot.getElementById('contrib').getBoundingClientRect().height === 0));
await page.click('a[data-ecran="formulaire"]');
await page.waitForTimeout(400);
console.log('after switch', await page.evaluate(() => [...document.querySelectorAll('.hote')].filter(h => !h.hidden).map(h => h.id)));
console.log(errs.length ? 'ERRORS\n' + errs.join('\n') : 'no errors');
await browser.close();
