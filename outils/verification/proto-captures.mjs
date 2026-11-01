// Photographie des planches du canevas du prototype, affichées par le moteur du canevas.
// Usage : node proto-captures.mjs <dossier project/> <dc-runtime.js> <dossier de rendu> <dossier des captures>
// Les copies de rendu ne changent que les réglages par défaut (data-props) ; les originaux ne sont pas touchés.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import http from 'http';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const [,, projet, moteur, rendu, sortie] = process.argv;

// nom de la capture : [planche, réglages imposés]
const ECRANS = {
  'scanner': ['E1-Scan', { statuts: false, bandeau: false, alerte: 'Aucune', lampe: false }],
  'produit': ['EA-Produit-Lait', {}],
  'verdict-g1': ['E2-Verdict-N1', { statuts: false, alerte: false, voletOuvert: false }],
  'verdict-g2': ['E2-Verdict-N2', { statuts: false, alerte: false, voletOuvert: false }],
  'verdict-g3': ['E2-Verdict-N3', { statuts: false, alerte: false, voletOuvert: false }],
  'verdict-g4': ['E2-Verdict-N4', { statuts: false, alerte: false, voletOuvert: false }],
  'verdict-a': ['EA-Verdict-Lait-Drapeau', { statuts: false, alerte: false, voletOuvert: false, renvoiOuvert: false, source: false }],
  'composition-a': ['EA-Ingredients-Lait', { statuts: false, panneau: 'Aucun' }],
  'composition-g': ['E1-Ingredients', { statuts: false, panneau: 'Fermé' }],
  'panneau-g': ['E1-Ingredients', { statuts: false, panneau: 'Ingrédient qui détermine le niveau' }],
  'inconnu': ['E3-SansVerdict-Inconnu', { statuts: false, animation: 'Image fixe (réduire les animations)' }],
  'recherche': ['E2-Recherche-Resultats', { statuts: false }],
  'lexique': ['E6-Methode-Lexique', { statuts: false }],
};

const echapper = s => s.replace(/&/g, '&amp;').replace(/'/g, '&#39;');
const desechapper = s => s.replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');

fs.mkdirSync(rendu, { recursive: true });
fs.mkdirSync(sortie, { recursive: true });
fs.copyFileSync(moteur, path.join(rendu, 'support.js'));
for (const [nom, [planche, reglages]] of Object.entries(ECRANS)) {
  const src = fs.readFileSync(path.join(projet, planche + '.dc.html'), 'utf8');
  const m = /data-props='([^']*)'/.exec(src);
  const props = JSON.parse(desechapper(m[1]));
  for (const [k, v] of Object.entries(reglages)) {
    if (!props[k]) throw new Error(`${planche} : réglage inconnu ${k}`);
    props[k].default = v;
  }
  const copie = src.replace(m[0], `data-props='${echapper(JSON.stringify(props))}'`);
  fs.writeFileSync(path.join(rendu, nom + '.dc.html'), copie);
}

const serveur = http.createServer((req, res) => {
  const fichier = path.join(rendu, decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!fichier.startsWith(path.resolve(rendu)) || !fs.existsSync(fichier)) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'content-type': fichier.endsWith('.js') ? 'text/javascript' : 'text/html; charset=utf-8' });
  res.end(fs.readFileSync(fichier));
});
await new Promise(r => serveur.listen(0, '127.0.0.1', r));
const port = serveur.address().port;

const browser = await chromium.launch();
for (const nom of Object.keys(ECRANS)) {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3 });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await page.goto(`http://127.0.0.1:${port}/${nom}.dc.html`);
  await page.waitForFunction(() => document.querySelector('#dc-root') && document.querySelector('#dc-root').innerText.trim().length > 0, null, { timeout: 15000 }).catch(() => errs.push('rendu vide'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(900);
  await page.screenshot({ path: path.join(sortie, nom + '.png') });
  console.log(nom, errs.length ? 'ERREURS ' + errs.join(' | ').slice(0, 400) : 'ok');
  await page.close();
}
await browser.close();
serveur.close();
