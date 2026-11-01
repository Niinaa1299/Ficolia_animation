// Quand le texte et « Continuer » arrivent : opacité du texte, bouton entièrement à l'écran et opaque ; fin de l'animation.
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, file, ...types] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 900 } });
for (const ty of types) {
  await page.goto('file://' + file + '?t=0&transition=' + ty);
  await page.waitForTimeout(300);
  const r = await page.evaluate(() => {
    const scrub = document.getElementById('scrub'); scrub.step = 'any';
    const scr = document.getElementById('screen').getBoundingClientRect();
    const acc = document.getElementById('accueil'), btn = document.getElementById('continuer'), copy = document.getElementById('copy'), actions = document.getElementById('actions');
    let texte = null, bouton = null, boutonVisible = null;
    for (let t = 4000; t <= +scrub.max; t += 10) {   // jusqu'à la fin : avec recul3 (29/10), le texte arrive vers 8 s
      scrub.value = t; scrub.dispatchEvent(new Event('input'));
      if (acc.hidden) continue;
      const b = btn.getBoundingClientRect(), o = +getComputedStyle(copy).opacity, oa = +getComputedStyle(actions).opacity;
      if (texte === null && o > 0.02) texte = t;
      if (boutonVisible === null && b.top < scr.bottom && oa > 0.02) boutonVisible = t;
      if (bouton === null && b.bottom <= scr.bottom && oa > 0.98) bouton = t;
    }
    return { texte, boutonVisible, bouton, fin: +scrub.max };
  });
  const debut = Math.min(...[r.texte, r.boutonVisible].filter(v => v !== null));
  console.log(ty.padEnd(10), JSON.stringify(r), 'animation avec le texte :', Number.isFinite(debut) ? ((r.fin - debut) / 1000).toFixed(2) + ' s' : 'texte jamais affiché');
}
await browser.close();
