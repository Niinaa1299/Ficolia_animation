// Usage: node trace.mjs <file> <query> <selector> <t0> <t1> <step> : scrubs and prints the transform of an element over time.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, q, sel, t0, t1, step] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + file + '?' + q + '&t=0');
await page.waitForTimeout(300);
const rows = await page.evaluate(([sel, t0, t1, step]) => {
  const out = [], s = document.getElementById('scrub'), el = document.querySelector(sel);
  for (let t = t0; t <= t1; t += step) {
    s.value = t; s.dispatchEvent(new Event('input'));
    out.push([t, el.getAttribute('transform'), el.getAttribute('opacity')]);
  }
  return out;
}, [sel, +t0, +t1, +step]);
for (const r of rows) console.log(r.join('\t'));
await browser.close();
