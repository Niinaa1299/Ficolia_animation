// Compute bboxes of the reveal's contour/flesh clip shapes and the symbol's contour, in their own coordinates.
import { createRequire } from 'module'; import fs from 'fs';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, revealPath, symbolPath] = process.argv;
const reveal = fs.readFileSync(revealPath, 'utf8');
const symbol = fs.readFileSync(symbolPath, 'utf8');
const clip = id => reveal.match(new RegExp(`<clipPath id="${id}">([\\s\\S]*?)</clipPath>`))[1];
const symPaths = [...symbol.matchAll(/<path d="([^"]+)"/g)].map(m => m[1]);
const html = `<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10">
<g id="CB">${clip('fcoCB')}</g><g id="CA">${clip('fcoCA')}</g><g id="CF">${clip('fcoCF')}</g>
<path id="S0" d="${symPaths[0]}"/><path id="S1" d="${symPaths[1]}"/><path id="S2" d="${symPaths[2]}"/></svg>`;
const browser = await chromium.launch(); const page = await browser.newPage();
await page.setContent(html);
const out = await page.evaluate(() => Object.fromEntries(['CB','CA','CF','S0','S1','S2'].map(id => {
  const b = document.getElementById(id).getBBox(); return [id, {x:+b.x.toFixed(2), y:+b.y.toFixed(2), w:+b.width.toFixed(2), h:+b.height.toFixed(2)}];
})));
console.log(JSON.stringify(out, null, 1));
await browser.close();
