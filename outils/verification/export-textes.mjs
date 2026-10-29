// Usage : node export-textes.mjs <maquettes/ouverture-arbre.html> <exports/ouverture/ouverture.html> (chemins absolus)
// Les textes de la page de référence contre ceux de la maquette : opacité, déplacement, place, instant par instant.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, maquette, reference] = process.argv;
const CHOIX = 'place=b&bas=pale-bis&descente=a&decor=a&transition=recul3&notes=off&mouvement=normal';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1200, height: 1000 } });
const errs = []; p.on('pageerror', e => errs.push('page: ' + e)); p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
const mesure = (sels, origine) => p.evaluate(([sels, origine]) => {
  const o = document.querySelector(origine).getBoundingClientRect();
  const out = {};
  for (const [nom, sel] of Object.entries(sels)) {
    const el = document.querySelector(sel); if (!el) { out[nom] = null; continue; }
    // opacité vue : le produit des opacités des ancêtres jusqu'à l'écran ; caché si visibility hidden
    let op = 1, e = el; while (e && e !== document.body) { op *= +getComputedStyle(e).opacity; e = e.parentElement; }
    const vis = getComputedStyle(el).visibility !== 'hidden' && !el.closest('[hidden]');
    const r = el.getBoundingClientRect();
    out[nom] = { op: vis ? +op.toFixed(3) : 0, y: +(r.top - o.top).toFixed(1), x: +(r.left - o.left).toFixed(1), h: +r.height.toFixed(1) };
  }
  return out;
}, [sels, origine]);
const SM = { l1: '#l1', l2: '#l2', titre: '#copy h1', rappel: '#copy .rappel', bouton: '#continuer', titre2: '#copy2 h1', bouton2: '#accepter', retour: '#retour' };
const SR = { l1: '.accroche p:nth-of-type(2)', l2: '.accroche p:nth-of-type(3)', titre: '.accueil.un h1', rappel: '.accueil.un .rappel', bouton: '#continuer', titre2: '.accueil.deux h1', bouton2: '#accepter', retour: '#retour' };
const cas = [['1', [3400, 3600, 3700, 3900, 4100, 4400, 4600, 4800, 5000, 5300, 7900, 8000, 8100, 8250, 8400, 8600, 10000]], ['2', [0, 150, 300, 1400, 1550, 1700, 1800, 2000, 2200, 4400]]];
let pire = { op: 0, y: 0 };
for (const [ecran, temps] of cas) {
  for (const t of temps) {
    await p.goto('file://' + maquette + '?' + CHOIX + '&ecran=' + ecran + '&t=0'); await p.waitForTimeout(250);
    await p.evaluate(t => { const s = document.getElementById('scrub'); s.step = 'any'; s.value = t; s.dispatchEvent(new Event('input')); }, t);
    const m = await mesure(SM, '#screen');
    await p.goto('file://' + reference + '?statuts=off&mouvement=normal&ecran=' + ecran + '&t=' + t);
    await p.waitForFunction(() => document.documentElement.dataset.pret === '1');
    const r = await mesure(SR, '#ecran');
    const ecarts = [];
    for (const k of Object.keys(SM)) {
      const a = m[k], c = r[k]; if (!a || !c) continue;
      const dop = Math.abs(a.op - c.op), dy = (a.op > 0.01 || c.op > 0.01) ? Math.abs(a.y - c.y) : 0;
      pire.op = Math.max(pire.op, dop); if (!k.startsWith('l')) pire.y = Math.max(pire.y, dy);
      if (dop > 0.02 || dy > 0.6) ecarts.push(`${k}: op ${a.op}→${c.op}, y ${a.y}→${c.y}`);
    }
    console.log(`écran ${ecran}, ${String(t).padStart(5)} ms :`, ecarts.length ? ecarts.join(' ; ') : 'identiques (opacité ±0,02, place ±0,6 px)');
  }
}
console.log('pire écart d’opacité :', pire.op.toFixed(3), '; pire écart de place (hors accroche) :', pire.y.toFixed(1), 'px');
console.log(errs.length ? errs.join('\n') : 'console : aucune erreur');
await b.close();
