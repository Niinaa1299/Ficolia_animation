// Vérifie « l'arbre et la figue » dans l'aperçu : le bas de l'écran (quatre versions), la fin de chaque version, les erreurs.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
await page.goto('file://' + file + '#arbre');
await page.waitForTimeout(600);
const host = page.locator('#hote-arbre');
const etat = () => page.evaluate(() => {
  const r = document.getElementById('hote-arbre').shadowRoot;
  const on = [...r.querySelectorAll('.seg[data-key="bas"] button')].filter(b => b.getAttribute('aria-pressed') === 'true').map(b => b.dataset.val).join();
  return { visible: !document.getElementById('hote-arbre').hidden, bas: on, boutons: [...r.querySelectorAll('.seg[data-key="bas"] button')].map(b => b.textContent), max: r.getElementById('scrub').max, beats: r.querySelectorAll('#beats li').length, dataBas: r.getElementById('screen').dataset.bas };
});
console.log('au départ', JSON.stringify(await etat()));
for (const v of ['pale', 'profond', 'pale-bis', 'profond-bis']) {
  await host.locator(`.seg[data-key="bas"] button[data-val="${v}"]`).click();
  await host.locator('#replay').click();
  await page.waitForTimeout(10200);
  console.log(v, JSON.stringify(await etat()));
  await host.locator('#screen').screenshot({ path: `${out}-${v}.png` });
}
console.log(errs.length ? 'ERREURS ' + errs.join(' | ') : 'sans erreur');
await browser.close();
