// Vérifie le réglage « Couleurs » des trois écrans d'échec dans l'aperçu : bascule, captures, erreurs.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
for (const ancre of ['connexion', 'inconnu', 'service']) {
  await page.goto('file://' + file + '#' + ancre);
  await page.waitForTimeout(3300);
  const host = page.locator('#hote-' + ancre);
  const gris = () => page.evaluate(a => document.getElementById('hote-' + a).shadowRoot.getElementById('screen').classList.contains('gris'), ancre);
  const peau = () => page.evaluate(a => getComputedStyle(document.getElementById('hote-' + a).shadowRoot.getElementById('screen')).getPropertyValue('--f-peau').trim(), ancre);
  const before = [await gris(), await peau()];
  await page.screenshot({ path: `${out}-${ancre}-couleurs.png` });
  await host.locator('.seg[data-key="couleurs"] button[data-val="gris"]').click();
  await page.waitForTimeout(200);
  const after = [await gris(), await peau()];
  await page.screenshot({ path: `${out}-${ancre}-gris.png` });
  console.log(ancre, 'défaut', before, '→ grisé', after);
}
console.log(errs.length ? 'ERRORS\n' + errs.join('\n') : 'no errors');
await browser.close();
