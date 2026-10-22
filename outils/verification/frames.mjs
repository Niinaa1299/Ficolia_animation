// Usage: node frames.mjs <file> <outDir> <query>... ; captures the phone screen element for each query string.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, outDir, ...queries] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 1 });
const errors = [];
page.on('pageerror', e => errors.push(String(e)));
page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
for (const q of queries) {
  await page.goto('file://' + file + '?' + q);
  await page.waitForTimeout(400);
  const name = q.replace(/[^a-z0-9]+/gi, '_');
  await page.locator('#screen').screenshot({ path: `${outDir}/${name}.png` });
}
console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'no errors');
await browser.close();
