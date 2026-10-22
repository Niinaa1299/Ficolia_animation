// Vérifie le formulaire dans l'aperçu : pistes retenues par défaut, tampon bis, photomaton bis, réduit, erreurs.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
await page.goto('file://' + file);
await page.waitForTimeout(400);
const host = page.locator('#hote-formulaire');
console.log('visible au départ :', await page.evaluate(() => [...document.querySelectorAll('.hote')].filter(h => !h.hidden).map(h => h.id)));
console.log('étapes :', await page.evaluate(() => [...document.querySelectorAll('.recit-etapes li')].map(li => li.dataset.etat + ':' + li.textContent).join(' | ')));
const click = async (key, val) => { await host.locator(`.seg[data-key="${key}"] button[data-val="${val}"]`).click(); };
const state = async () => page.evaluate(() => {
  const r = document.getElementById('hote-formulaire').shadowRoot;
  const seg = k => [...r.querySelectorAll(`.seg[data-key="${k}"] button`)];
  return { title: r.getElementById('title').textContent,
    disabled: seg('piste').filter(b => b.disabled).map(b => b.dataset.val),
    piste: seg('piste').filter(b => b.getAttribute('aria-pressed') === 'true').map(b => b.dataset.val),
    beats: r.getElementById('beats').children.length };
});
console.log('défaut', JSON.stringify(await state()));
await page.waitForTimeout(3600);
await page.screenshot({ path: `${out}-tamponbis.png` });
await click('form', 'photo');
console.log('photo (piste gardée)', JSON.stringify(await state()));
await click('text', 'humour');
await click('piste', 'photomatonbis');
console.log('photomaton bis', JSON.stringify(await state()));
await page.waitForTimeout(3900);
await page.screenshot({ path: `${out}-photomatonbis.png` });
await click('form', 'signalement');
console.log('retour signalement', JSON.stringify(await state()));
await click('form', 'photo'); await click('piste', 'photomatonbis'); await click('motion', 'reduit');
await page.waitForTimeout(800);
await page.screenshot({ path: `${out}-reduit.png` });
console.log('réduit', JSON.stringify(await state()));
console.log(errs.length ? 'ERRORS\n' + errs.join('\n') : 'no errors');
await browser.close();
