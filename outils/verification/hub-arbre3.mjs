// Vérifie « l'arbre et la figue » dans l'aperçu : les quatre transitions, « Revoir la transition », la fin, les erreurs.
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
  const on = [...r.querySelectorAll('.seg[data-key="transition"] button')].filter(b => b.getAttribute('aria-pressed') === 'true').map(b => b.dataset.val).join();
  return { visible: !document.getElementById('hote-arbre').hidden, transition: on, t: r.getElementById('scrubOut').textContent, max: r.getElementById('scrub').max, beats: r.querySelectorAll('#beats li').length, dataBas: r.getElementById('screen').dataset.bas };
});
console.log('au départ', JSON.stringify(await etat()));
for (const v of ['saut', 'brume', 'bis', 'recul']) {
  await host.locator(`.seg[data-key="transition"] button[data-val="${v}"]`).click();
  await page.waitForTimeout(150);
  console.log(v, 'juste après le clic', JSON.stringify(await etat()));
  await page.waitForTimeout(6600);
  console.log(v, 'à la fin', JSON.stringify(await etat()));
  await host.locator('#screen').screenshot({ path: `${out}-${v}.png` });
}
await host.locator('#revoir').click(); await page.waitForTimeout(150);
console.log('« Revoir la transition »', JSON.stringify(await etat()));
console.log(errs.length ? 'ERREURS ' + errs.join(' | ') : 'sans erreur');
await browser.close();
