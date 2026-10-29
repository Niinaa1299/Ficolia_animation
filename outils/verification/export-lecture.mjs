// Usage : node export-lecture.mjs <exports/ouverture/ouverture.html> (chemin absolu)
// La page de référence en vraie lecture : la vidéo joue, les textes la suivent ; « Continuer », « Retour » ; mouvement réduit.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, reference] = process.argv;
const b = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
const p = await b.newPage({ viewport: { width: 1200, height: 1000 } });
const errs = []; p.on('pageerror', e => errs.push('page: ' + e)); p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
const etat = () => p.evaluate(() => {
  const vu = s => { const e = document.querySelector(s); const c = getComputedStyle(e); let o = 1, x = e; while (x && x.id !== 'ecran') { o *= +getComputedStyle(x).opacity; x = x.parentElement; } return c.visibility === 'hidden' ? 0 : +o.toFixed(2); };
  const v1 = document.getElementById('video1'), v2 = document.getElementById('video2');
  const btn = document.getElementById('continuer').getBoundingClientRect();
  const sous = document.elementFromPoint(btn.left + btn.width / 2, btn.top + btn.height / 2);
  return { classe: document.getElementById('ecran').className, v1: +v1.currentTime.toFixed(2), v1fin: v1.ended, v2: +v2.currentTime.toFixed(2),
    texte1: vu('.accueil.un .copy'), continuer: vu('#continuer'), continuerCliquable: sous && sous.id === 'continuer',
    texte2: vu('.accueil.deux .copy'), accepter: vu('#accepter'), focus: document.activeElement.id || document.activeElement.tagName };
});
// 1. L'ouverture, jouée : on suit l'opacité du texte du 1/2 contre le temps de la vidéo.
await p.goto('file://' + reference + '?statuts=off&mouvement=normal');
const suivi = await p.evaluate(() => new Promise(fin => {
  const v = document.getElementById('video1'), c = document.querySelector('.accueil.un .copy'), l = document.querySelector('.accroche p:nth-of-type(2)');
  const pts = [];
  const pas = () => { pts.push([v.currentTime * 1000, +getComputedStyle(c).opacity, +getComputedStyle(l).opacity]); if (v.ended || pts.length > 2000) fin(pts); else requestAnimationFrame(pas); };
  requestAnimationFrame(pas);
}));
// Le décalage : l'instant où le texte (ou l'accroche) passe 0,5, contre celui de la maquette.
const DOUX = x => { const cb = (p1x, p1y, p2x, p2y) => { const cx = 3 * p1x, bx = 3 * (p2x - p1x) - cx, ax = 1 - cx - bx, cy = 3 * p1y, by = 3 * (p2y - p1y) - cy, ay = 1 - cy - by; return x => { let t = x; for (let i = 0; i < 20; i++) { const e = ((ax * t + bx) * t + cx) * t - x; const d = (3 * ax * t + 2 * bx) * t + cx; if (Math.abs(e) < 1e-7 || !d) break; t -= e / d; } return ((ay * t + by) * t + cy) * t; }; }; return cb(.37, 0, .63, 1)(x); };
const croise = (i, seuil) => { for (let k = 1; k < suivi.length; k++) if (suivi[k - 1][i] < seuil && suivi[k][i] >= seuil) return suivi[k][0]; return null; };
console.log('lecture : ', suivi.length, 'images suivies ; vidéo jusqu’à', Math.round(suivi[suivi.length - 1][0]), 'ms');
console.log('accroche, 1re ligne à 0,5 : vidéo à', Math.round(croise(2, 0.5)), 'ms (maquette : vers 3640 ms)');
console.log('texte du 1/2 à 0,5 : vidéo à', Math.round(croise(1, 0.5)), 'ms (maquette : 8200 ms)');
console.log('fin de l’ouverture   ', JSON.stringify(await etat()));
// 2. Continuer, puis le 2/2 jusqu'à sa fin.
await p.click("#continuer"); await p.waitForTimeout(100);
console.log("clic, 0,1 s          ", JSON.stringify(await etat()));
await p.waitForTimeout(1600);
console.log('clic « Continuer »   ', JSON.stringify(await etat()));
await p.waitForFunction(() => document.getElementById('video2').ended, null, { timeout: 15000 }); await p.waitForTimeout(700);
console.log('fin du 2/2           ', JSON.stringify(await etat()));
// 3. Retour.
await p.click('#retour'); await p.waitForTimeout(100);
console.log('clic « Retour »      ', JSON.stringify(await etat()));
// 4. Avant 7,95 s, « Continuer » n'est pas cliquable.
await p.goto('file://' + reference + '?statuts=off&mouvement=normal&t=6000');
await p.waitForFunction(() => document.documentElement.dataset.pret === '1');
console.log('à 6 s (figé)         ', JSON.stringify(await etat()));
// 5. Mouvement réduit : l'ouverture, puis le 2/2.
await p.goto('file://' + reference + '?statuts=off&mouvement=reduit'); await p.waitForTimeout(2400);
console.log('réduit, à 2,4 s      ', JSON.stringify(await etat()));
await p.click('#continuer'); await p.waitForTimeout(1400);
console.log('réduit, 2/2 à 1,4 s  ', JSON.stringify(await etat()));
console.log(errs.length ? errs.join('\n') : 'console : aucune erreur');
await b.close();
