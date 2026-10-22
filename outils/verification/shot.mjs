// Usage: node shot.mjs <url-or-file> <out.png> [width] [height] [waitMs] [scale]
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, target, out, w = '390', h = '844', wait = '300', scale = '2'] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +scale });
const url = /^https?:|^file:/.test(target) ? target : 'file://' + target;
await page.goto(url);
await page.waitForTimeout(+wait);
await page.screenshot({ path: out });
await browser.close();
console.log('saved', out);
