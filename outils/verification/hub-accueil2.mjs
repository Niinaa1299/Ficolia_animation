// Vérifie l'accueil à deux écrans dans l'aperçu : écran par défaut, boutons de l'écran, structures de comparaison, erreurs.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
await page.goto('file://' + file + '#accueil');
await page.waitForTimeout(500);
console.log('visible au départ :', await page.evaluate(() => [...document.querySelectorAll('.hote')].filter(h => !h.hidden).map(h => h.id)));
console.log('menu :', await page.evaluate(() => [...document.querySelectorAll('nav button, nav a, [role="tab"]')].map(b => b.textContent.trim()).filter(t => /Accueil/.test(t))));
const host = page.locator('#hote-accueil');
const etat = async () => page.evaluate(() => {
  const r = document.getElementById('hote-accueil').shadowRoot;
  const on = k => [...r.querySelectorAll(`.seg[data-key="${k}"] button`)].filter(b => b.getAttribute('aria-pressed') === 'true').map(b => b.dataset.val).join();
  return { ecran: on('ecran'), structure: on('structure'), titre: r.getElementById('titre').textContent, suite: r.getElementById('suite').textContent,
    passer: !r.getElementById('passer').hidden, retour: !r.getElementById('retour').hidden,
    boutons: [...r.querySelectorAll('.seg[data-key="ecran"] button')].filter(b => !b.hidden).map(b => b.textContent).join(' '),
    points: r.getElementById('points').getAttribute('aria-label'), h2: r.querySelector('.panel h2').textContent };
});
await page.waitForTimeout(4200);
await page.screenshot({ path: `${out}-1.png` });
console.log('1/2', JSON.stringify(await etat()));
await host.locator('#suite').click(); await page.waitForTimeout(4400);
await page.screenshot({ path: `${out}-2.png` });
console.log('Continuer →', JSON.stringify(await etat()));
await host.locator('#suite').click(); await page.waitForTimeout(400);
console.log('Accepter (le scanner est hors maquette) →', JSON.stringify(await etat()));
await host.locator('#retour').click(); await page.waitForTimeout(1500);
console.log('Retour →', JSON.stringify(await etat()));
await host.locator('.seg[data-key="structure"] button[data-val="trois"]').click(); await page.waitForTimeout(400);
console.log('Trois écrans →', JSON.stringify(await etat()));
await page.waitForTimeout(3800);
await host.locator('#passer').click(); await page.waitForTimeout(4600);
console.log('Trois, Passer →', JSON.stringify(await etat()));
await host.locator('.seg[data-key="structure"] button[data-val="prototype"]').click(); await page.waitForTimeout(300);
await host.locator('.seg[data-key="ecran"] button[data-val="1"]').click(); await page.waitForTimeout(600);
await host.locator('#passer').click(); await page.waitForTimeout(4400);
console.log('Prototype, Passer →', JSON.stringify(await etat()));
await host.locator('.seg[data-key="structure"] button[data-val="deux"]').click(); await page.waitForTimeout(4600);
console.log('Retour à deux écrans →', JSON.stringify(await etat()));
await host.locator('.seg[data-key="motion"] button[data-val="reduit"]').click(); await page.waitForTimeout(800);
await page.screenshot({ path: `${out}-reduit.png` });
console.log(errs.length ? 'ERRORS\n' + errs.join('\n') : 'no errors');
await browser.close();
