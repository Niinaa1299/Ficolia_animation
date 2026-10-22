// Mesure les boîtes des tracés de la figue (symbole et « o » du logo).
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const data = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const browser = await chromium.launch();
const page = await browser.newPage();
await page.setContent('<svg id="s" width="800" height="800"></svg>');
const res = await page.evaluate(data => {
  const s = document.getElementById('s');
  const bb = ds => { const g = document.createElementNS('http://www.w3.org/2000/svg', 'g'); s.appendChild(g);
    for (const d of ds) { const p = document.createElementNS('http://www.w3.org/2000/svg', 'path'); p.setAttribute('d', d); g.appendChild(p); }
    const b = g.getBBox(); g.remove(); return [b.x, b.y, b.width, b.height].map(v => +v.toFixed(1)); };
  const L = data.LOGO, F = data.FIG;
  return {
    o_contour: bb([...L.contourA, ...L.contourB]), o_chair: bb(L.chair), o_stem: bb([L.contourB[1]]), o_bas: bb([L.contourB[2]]),
    fic: bb([L.fic]), lia: bb([L.lia]),
    sym_contour: bb([F.contour]), sym_arc: bb([F.arc]), sym_veins: bb([F.veins]), sym_seeds: bb(F.seeds),
    sym_vein_start: F.veins.slice(0, 40)
  };
}, data);
console.log(JSON.stringify(res, null, 1));
await browser.close();
