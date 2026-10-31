#!/usr/bin/env node
// Rend localement une ou plusieurs sources de planche (.dc.html) avec le moteur extrait d'un export du
// canevas (outils/runtime/, produit par outils/deballer-export.py), et en fait une capture PNG à l'échelle 2.
//
// Usage : node outils/rendre.mjs <dossier-de-sortie> <source.dc.html> [...]
//
// Principe : on recompose la page que le canevas fabrique pour une planche : React, puis support.js
// (dc-runtime), puis la source. Le moteur ne charge React depuis un CDN que s'il n'est pas déjà là ;
// ici il est fourni en local, donc aucun accès réseau n'est requis, sauf pour Google Fonts (si le
// réseau les refuse, la police de repli s'affiche, et la ligne de résultat le dit).
//
// Le précédent du projet, outils/verification/proto-captures.mjs (branche happy-mccarthy), rend une liste
// fixe de planches avec des réglages imposés ; ce script rend n'importe quelle source, sans rien imposer.
//
// Limites : c'est une reconstitution du rendu, pas le canevas lui-même ; les liens de prototype entre
// planches ne sont pas suivis ; aucune image téléversée (/_blob/) ne peut s'afficher.
import fs from 'fs';
import path from 'path';
import http from 'http';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const [, , sortie, ...sources] = process.argv;
if (!sortie || !sources.length) { console.error('usage : rendre.mjs <dossier-de-sortie> <source.dc.html> [...]'); process.exit(2); }
const runtime = path.join(path.dirname(new URL(import.meta.url).pathname), 'runtime');
const MOTEUR = ['react.production.min.js', 'react-dom.production.min.js', 'support.js'];
for (const f of MOTEUR) {
  if (!fs.existsSync(path.join(runtime, f))) { console.error(`moteur absent : ${f} (lancer outils/deballer-export.py d'abord)`); process.exit(2); }
}
fs.mkdirSync(sortie, { recursive: true });

// Un petit serveur local : le moteur relit sa propre page par fetch(), ce que file:// interdit.
const pages = new Map();
const serveur = http.createServer((req, res) => {
  const nom = decodeURIComponent(req.url.slice(1));
  if (pages.has(nom)) { res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); return res.end(pages.get(nom)); }
  if (MOTEUR.includes(nom)) { res.writeHead(200, { 'Content-Type': 'text/javascript' }); return res.end(fs.readFileSync(path.join(runtime, nom))); }
  res.writeHead(404); res.end();
});
await new Promise(r => serveur.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${serveur.address().port}/`;

const browser = await chromium.launch();
for (const src of sources) {
  let html = fs.readFileSync(src, 'utf8');
  const m = html.match(/&quot;\$preview&quot;:\{&quot;width&quot;:(\d+),&quot;height&quot;:(\d+)/) || html.match(/"\$preview":\{"width":(\d+),"height":(\d+)/);
  const w = m ? +m[1] : 390, h = m ? +m[2] : 844;
  const inject = MOTEUR.map(f => `<script src="/${f}"></script>`).join('\n');
  if (!html.includes('<script src="./support.js"></script>')) { console.log(`${path.basename(src)} : pas de ligne support.js, ignoré`); continue; }
  html = html.replace('<script src="./support.js"></script>', inject);
  const nom = path.basename(src);
  pages.set(nom, html);
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
  const errs = [];
  page.on('pageerror', e => errs.push(e.message.slice(0, 200)));
  // Les erreurs « Expected moveto path command … {{…}} » sont le navigateur qui lit le gabarit avant que
  // le moteur ne remplisse les trous ; elles se produisent aussi sur le canevas et ne sont pas comptées.
  page.on('console', c => { if (c.type() === 'error' && !/\{\{.*\}\}/.test(c.text())) errs.push(c.text().slice(0, 200)); });
  await page.goto(base + encodeURIComponent(nom));
  await page.waitForTimeout(2500);
  const info = await page.evaluate(() => ({
    texte: document.body.innerText.replace(/\s+/g, ' ').slice(0, 90),
    polices: [...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight))],
  }));
  const png = path.join(sortie, path.basename(src).replace(/\.dc\.html$/, '') + '.png');
  await page.screenshot({ path: png });
  console.log(`${path.basename(src)} → ${png} · ${w}×${h} · polices chargées : ${info.polices.join(', ') || 'aucune (repli)'} · erreurs : ${errs.length}${errs.length ? ' · ' + errs[0] : ''}\n   « ${info.texte} »`);
  await page.close();
  pages.delete(nom);
}
await browser.close();
serveur.close();
