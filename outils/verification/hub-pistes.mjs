// Vérifie la piste dans l'aperçu : clic sur les boutons dans la zone isolée, captures, erreurs.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
await page.goto('file://' + file + '#formulaire');
await page.waitForTimeout(400);
const host = page.locator('#hote-formulaire');
const click = async (key, val) => { await host.locator(`.seg[data-key="${key}"] button[data-val="${val}"]`).click(); };
const state = async () => page.evaluate(() => {
  const r = document.getElementById('hote-formulaire').shadowRoot;
  return { title: r.getElementById('title').textContent, disabled: [...r.querySelectorAll('.seg[data-key="piste"] button')].filter(b => b.disabled).map(b => b.dataset.val),
           pressed: [...r.querySelectorAll('.seg[data-key="piste"] button')].filter(b => b.getAttribute('aria-pressed') === 'true').map(b => b.dataset.val) };
});
await click('text', 'humour');
for (const [form, piste, wait] of [['signalement', 'tampon', 2500], ['signalement', 'feuille', 2300], ['photo', 'photomaton', 3300]]) {
  await click('form', form); await click('piste', piste);
  await page.waitForTimeout(wait);
  await page.screenshot({ path: `${out}-${piste}.png` });
  console.log(form, piste, JSON.stringify(await state()));
}
await click('form', 'signalement');
console.log('after switching to signalement', JSON.stringify(await state()));
await click('form', 'support');
console.log('support', JSON.stringify(await state()));
await click('form', 'photo'); await click('motion', 'reduit'); await click('piste', 'photomaton');
await page.waitForTimeout(900);
await page.screenshot({ path: `${out}-reduit.png` });
console.log(errs.length ? 'ERRORS\n' + errs.join('\n') : 'no errors');
await browser.close();
