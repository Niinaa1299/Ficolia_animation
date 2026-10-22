// Vérifie le dossier du site vitrine : erreurs, débordements à 360, 390 et 1280 px, thème sombre, et quelques vues.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
for (const [w, h, sombre] of [[360, 780, false], [390, 844, false], [1280, 900, false], [390, 844, true]]) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, colorScheme: sombre ? 'dark' : 'light' });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await page.goto('file://' + file);
  await page.waitForTimeout(1200);
  const r = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const trop = [...document.querySelectorAll('body *')].filter(el => {
      const b = el.getBoundingClientRect();
      if (!b.width) return false;
      for (let p = el.parentElement; p; p = p.parentElement) if (getComputedStyle(p).overflowX !== 'visible') return false;
      return b.right > vw + 0.5 || b.left < -0.5;
    }).slice(0, 8).map(el => el.tagName.toLowerCase() + '.' + el.className + ' ' + Math.round(el.getBoundingClientRect().right));
    const polices = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.style + ' ' + f.weight);
    return { scroll: document.documentElement.scrollWidth, vw, trop, haut: document.documentElement.scrollHeight, polices: [...new Set(polices)] };
  });
  console.log(w, sombre ? 'sombre' : 'clair', JSON.stringify(r), errs.length ? 'ERREURS ' + errs.join(' | ') : 'sans erreur');
  if (w === 390 && !sombre) {
    for (const [sel, nom] of [['.tete', 'tete'], ['.figure-ouv .ms', 'ouverture'], ['.bloquants', 'bloquants'], ['.rythme', 'rythme'], ['#s-f', 'section-f'], ['.dispositifs', 'dispositifs'], ['.faq', 'faq']]) {
      await page.locator(sel).first().screenshot({ path: `${out}/m-${nom}.png` });
    }
  }
  if (w === 1280) {
    for (const [sel, nom] of [['.tete', 'tete'], ['.figure-ouv', 'ouverture'], ['.etat', 'etat'], ['.nuancier', 'nuancier'], ['.specimens', 'specimens'], ['.dispositifs', 'dispositifs'], ['.evite', 'evite'], ['.test', 'test'], ['.mouv', 'mouv'], ['#tests', 'tests']]) {
      await page.locator(sel).first().screenshot({ path: `${out}/d-${nom}.png` });
    }
    // Le logotype en grand, pour juger le tracé.
    await page.evaluate(() => {
      const s = document.querySelector('.ms-entete svg').cloneNode(true);
      s.setAttribute('style', 'width:900px;height:auto;display:block;background:#fff');
      s.id = 'logo-grand';
      document.body.prepend(s);
    });
    await page.locator('#logo-grand').screenshot({ path: `${out}/logo-grand.png` });
  }
  if (sombre) {
    await page.locator('.tete').screenshot({ path: `${out}/s-tete.png` });
    await page.locator('.figure-ouv').screenshot({ path: `${out}/s-ouverture.png` });
    await page.locator('.test').screenshot({ path: `${out}/s-test.png` });
  }
  await page.close();
}
await browser.close();
