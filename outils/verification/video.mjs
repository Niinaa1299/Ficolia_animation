// Records the mise-à-jour mockup frame by frame (deterministic seeking), humour text.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, outDir] = process.argv;
const FPS = 30, STEP = 1000 / FPS;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 900, height: 900 }, deviceScaleFactor: 2 });
await page.goto('file://' + file + '?texte=humour&notes=off&mouvement=normal&t=0');
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
await page.evaluate(() => { document.getElementById('scrub').step = '1'; });
const screen = page.locator('#screen');
let n = 0;
const shot = () => screen.screenshot({ path: `${outDir}/f_${String(n++).padStart(4, '0')}.png` });
const seek = ms => page.evaluate(v => { const s = document.getElementById('scrub'); s.value = v; s.dispatchEvent(new Event('input')); }, ms);
async function play(duration, hold) {
  for (let t = 0; t <= duration; t += STEP) { await seek(t); await shot(); }
  for (let i = 0; i < Math.round(hold * FPS); i++) await shot();
}
// 1. Ancienne version : la figue sèche.
await play(2500, 0.9);
// 2. Appui sur « Mettre à jour ».
await page.evaluate(() => { const b = document.getElementById('cta'); b.style.transition = 'none'; b.style.transform = 'scale(0.97)'; });
for (let i = 0; i < 5; i++) await shot();
await page.evaluate(() => { document.getElementById('cta').style.transform = 'none'; });
// 3. Le store prend la main (fondu 200 ms, barre 1,4 s).
await page.evaluate(() => {
  const st = document.getElementById('store'), bar = st.querySelector('.bar span');
  st.style.transition = 'none'; bar.style.transition = 'none'; st.style.opacity = '0'; bar.style.transform = 'scaleX(0)';
});
const storeFrames = Math.round(1.7 * FPS);
for (let i = 0; i < storeFrames; i++) {
  const ms = i * STEP;
  await page.evaluate(([op, k]) => {
    const st = document.getElementById('store');
    st.style.opacity = String(op); st.querySelector('.bar span').style.transform = 'scaleX(' + k + ')';
  }, [Math.min(1, ms / 200), Math.min(1, ms / 1400)]);
  await shot();
}
// 4. Nouvelle version : la goutte, la figue réhydratée.
await page.click('.seg[data-key="screen"] button[data-val="new"]');
await page.evaluate(() => { document.getElementById('scrub').step = '1'; });
const NEW = 1900;
for (let t = 0; t <= NEW; t += STEP) {
  await seek(t);
  await page.evaluate(op => { document.getElementById('store').style.opacity = String(op); }, Math.max(0, 1 - t / 200));
  await shot();
}
for (let i = 0; i < Math.round(1.6 * FPS); i++) await shot();
console.log('frames', n);
await browser.close();
