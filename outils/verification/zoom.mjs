// Usage: node zoom.mjs <file> <out.png> <x> <y> <w> <h> <query>... : captures a region of the illustration (viewBox units) at 6x.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out, x, y, w, h, ...queries] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 6 });
const shots = [];
for (const q of queries) {
  await page.goto('file://' + file + '?' + q);
  await page.waitForTimeout(300);
  const box = await page.locator('.illu svg').boundingBox();
  shots.push((await page.screenshot({ clip: { x: box.x + +x, y: box.y + +y, width: +w, height: +h } })).toString('base64'));
}
await page.setViewportSize({ width: 1200, height: 900 });
await page.setContent('<body style="margin:0;background:#ccc;display:flex;flex-wrap:wrap;gap:6px;padding:6px">' + shots.map(b => `<img src="data:image/png;base64,${b}" style="width:${w * 3}px">`).join('') + '</body>');
await page.screenshot({ path: out, fullPage: true });
await browser.close();
console.log('saved', out);
