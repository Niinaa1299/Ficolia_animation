// Usage: node illu.mjs <file> <out.png> <query>... ; captures the illustration area at 2x for each query, side by side.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out, ...queries] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 2 });
const shots = [];
for (const q of queries) {
  await page.goto('file://' + file + '?' + q);
  await page.waitForTimeout(300);
  shots.push({ q, b64: (await page.locator('.illu').screenshot()).toString('base64') });
}
const html = '<body style="margin:0;background:#ccc;font:13px sans-serif;display:flex;flex-wrap:wrap;gap:6px;padding:6px">' +
  shots.map(s => `<div><div>${s.q}</div><img src="data:image/png;base64,${s.b64}" style="width:390px;background:#fff"></div>`).join('') + '</body>';
await page.setViewportSize({ width: 1200, height: 1000 });
await page.setContent(html);
await page.waitForTimeout(200);
await page.screenshot({ path: out, fullPage: true });
await browser.close();
console.log('saved', out);
