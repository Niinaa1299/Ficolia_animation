// Parcourt la maquette animée du site : erreurs, débordements, et une image de l'écran à des moments choisis de chaque scène.
// Usage : node site-maquette.mjs <maquette.html> <dossier> <largeur> <hauteur> [reduit]
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out, w, h, mode] = process.argv;

// [nom, sélecteur, progression dans la scène épinglée (−1 : élément ordinaire, en haut de l'écran), attente en ms]
const PLANS = [
  ['01-ouv-t04', '.ouv-scene', 0, 400], ['02-ouv-t26', '.ouv-scene', 0, 2600],
  ['03-ouv-20', '.ouv-scene', .2], ['04-ouv-35', '.ouv-scene', .35], ['05-ouv-50', '.ouv-scene', .5],
  ['06-ouv-65', '.ouv-scene', .65], ['07-ouv-80', '.ouv-scene', .8], ['08-ouv-92', '.ouv-scene', .92],
  ['09-geste-00', '.geste-scene', 0], ['10-geste-08', '.geste-scene', .08], ['11-geste-15', '.geste-scene', .15],
  ['12-geste-24', '.geste-scene', .24], ['13-geste-40', '.geste-scene', .4], ['14-geste-60', '.geste-scene', .6],
  ['15-geste-68', '.geste-scene', .68], ['16-geste-95', '.geste-scene', .95],
  ['17-lignes-00', '.lignes-scene', 0], ['18-lignes-20', '.lignes-scene', .2], ['19-lignes-50', '.lignes-scene', .5], ['20-lignes-90', '.lignes-scene', .9],
  ['21-niv-00', '.niveaux-scene', 0], ['22-niv-20', '.niveaux-scene', .2], ['23-niv-50', '.niveaux-scene', .5], ['24-niv-95', '.niveaux-scene', .95],
  ['25-sans', '.sans-resultat', -1], ['26-methode', '.etiquette', -1], ['27-histoire', '.histoire', -1], ['28-histoire-b', '.chapitres', -1],
  ['29-faq', '.faq', -1], ['30-appel', '.appel', -1], ['31-appel-b', '.appel-grille', -1], ['32-pied', '.pied', -1],
];

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1, reducedMotion: mode === 'reduit' ? 'reduce' : 'no-preference' });
const errs = [];
page.on('pageerror', e => errs.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
await page.goto('file://' + file);
await page.evaluate(() => document.fonts.ready);
const etat = await page.evaluate(() => ({
  mode: document.documentElement.className,
  scroll: document.documentElement.scrollWidth, vw: document.documentElement.clientWidth,
  haut: document.documentElement.scrollHeight,
}));
console.log(w + '×' + h, mode || 'mouvement', JSON.stringify(etat));
for (const [nom, sel, p, attente] of PLANS) {
  const y = await page.evaluate(([sel, p]) => {
    const el = document.querySelector(sel);
    const haut = el.getBoundingClientRect().top + window.scrollY;
    return p >= 0 ? haut + p * Math.max(0, el.offsetHeight - window.innerHeight) : haut - window.innerHeight * .08;
  }, [sel, p]);
  await page.evaluate(y => window.scrollTo(0, y), y);
  await page.waitForTimeout(attente || 260);
  await page.screenshot({ path: `${out}/${nom}.png` });
}
// Débordements sur les côtés, page entière.
const trop = await page.evaluate(() => {
  const vw = document.documentElement.clientWidth;
  const nom = el => el.tagName.toLowerCase() + '.' + (typeof el.className === 'string' ? el.className : (el.className.baseVal || ''));
  return [...document.querySelectorAll('body *')].filter(el => {
    const b = el.getBoundingClientRect();
    if (!b.width) return false;
    for (let q = el.parentElement; q; q = q.parentElement) if (getComputedStyle(q).overflowX !== 'visible') return false;
    return b.right > vw + .5 || b.left < -.5;
  }).slice(0, 8).map(nom);
});
console.log('débordements', JSON.stringify(trop), errs.length ? 'ERREURS ' + errs.join(' | ').slice(0, 600) : 'sans erreur');
await browser.close();
