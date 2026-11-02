#!/usr/bin/env node
// Rend une planche (.dc.html) avec un ou plusieurs réglages imposés, et liste les liens présents à l'écran.
// Complète outils/rendre.mjs, qui rend chaque planche avec ses réglages par défaut et ne relève pas les liens.
//
// Usage, depuis n'importe où :
//   node outils/rendre-reglage.mjs <source.dc.html> [reglage=valeur ...]
// Variables facultatives :
//   CLIC="texte"       touche le premier élément qui contient ce texte avant de relever les liens
//   CAPTURE=chemin.png enregistre une capture (390 × 844, échelle 1)
// Exemples :
//   node outils/rendre-reglage.mjs prototype/sources/project/E1-Scan.dc.html "resultat=Produit reconnu, type suggéré (piste a)"
//   CLIC="Lait corps hydratant" node outils/rendre-reglage.mjs prototype/sources/project/E2-Recherche-Resultats.dc.html "catalogue=Catalogue évalué et produits reconnus, option (b)"
//
// Le réglage est imposé en remplaçant sa valeur « default » dans data-props, sur une copie en mémoire : la source
// n'est jamais modifiée. Les ressources assets/ sont servies depuis le dossier de la planche.
// Écrit le 02/11/2026 pour vérifier les liens de la piste (a), du filigrane et des réglages.
//
// Limites : comme rendre.mjs, c'est une reconstitution, pas le canevas ; les liens relevés sont ceux de l'écran
// rendu dans l'état demandé, pas ceux des autres états de la planche.
import fs from 'fs';
import path from 'path';
import http from 'http';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const runtime = path.join(path.dirname(new URL(import.meta.url).pathname), 'runtime');
const MOTEUR = ['react.production.min.js', 'react-dom.production.min.js', 'support.js'];
const [, , src, ...regl] = process.argv;
if (!src) { console.error('usage : rendre-reglage.mjs <source.dc.html> [reglage=valeur ...]'); process.exit(2); }
let html = fs.readFileSync(src, 'utf8');
for (const r of regl) {
  const [k, ...v] = r.split('='); const val = v.join('=');
  const re = new RegExp(`(&quot;${k}&quot;:\\{[^}]*?&quot;default&quot;:)(&quot;[^&]*&quot;|true|false)`);
  if (!re.test(html)) { console.error('réglage introuvable : ' + k); process.exit(2); }
  const enc = (val === 'true' || val === 'false') ? val : `&quot;${val}&quot;`;
  html = html.replace(re, `$1${enc}`);
}
html = html.replace('<script src="./support.js"></script>', MOTEUR.map(f => `<script src="/${f}"></script>`).join('\n'));
const nom = path.basename(src);
const serveur = http.createServer((req, res) => {
  const n = decodeURIComponent(req.url.slice(1));
  if (n === nom) { res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); return res.end(html); }
  if (MOTEUR.includes(n)) { res.writeHead(200, { 'Content-Type': 'text/javascript' }); return res.end(fs.readFileSync(path.join(runtime, n))); }
  if (n.startsWith('assets/') && !n.includes('..')) {
    const f = path.join(path.dirname(path.resolve(src)), n);
    if (fs.existsSync(f)) { res.writeHead(200); return res.end(fs.readFileSync(f)); }
  }
  res.writeHead(404); res.end();
});
await new Promise(r => serveur.listen(0, '127.0.0.1', r));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
const errs = [];
page.on('pageerror', e => errs.push(e.message.slice(0, 150)));
await page.goto(`http://127.0.0.1:${serveur.address().port}/${encodeURIComponent(nom)}`);
await page.waitForTimeout(2000);
if (process.env.CLIC) { await page.getByText(process.env.CLIC, { exact: false }).first().click(); await page.waitForTimeout(800); }
if (process.env.CAPTURE) await page.screenshot({ path: process.env.CAPTURE });
const liens = await page.evaluate(() => [...document.querySelectorAll('a[href]')]
  .map(a => (a.getAttribute('aria-label') || a.innerText.replace(/\s+/g, ' ').trim()).slice(0, 70) + ' → ' + a.getAttribute('href'))
  .filter(t => !/fonts\.g/.test(t)));
console.log(`${nom} ${regl.join(' ')} · erreurs : ${errs.length}${errs.length ? ' · ' + errs[0] : ''}`);
for (const l of liens) console.log('  ' + l);
await browser.close(); serveur.close();
