import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, out] = process.argv;
const browser = await chromium.launch();
const errs = [];
for (const [scheme, w, h, name] of [['light', 1280, 900, 'light'], ['dark', 1280, 900, 'dark'], ['light', 400, 860, 'phone']]) {
  const page = await browser.newPage({ viewport: { width: w, height: h }, colorScheme: scheme, deviceScaleFactor: 1 });
  page.on('pageerror', e => errs.push(String(e)));
  await page.goto('file://' + file);
  await page.waitForTimeout(2800);
  const over = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
  await page.screenshot({ path: out + '-' + name + '.png' });
  console.log(name, 'horizontal overflow:', over);
  await page.close();
}
console.log(errs.length ? errs.join('\n') : 'no errors');
await browser.close();
