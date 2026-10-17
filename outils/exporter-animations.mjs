// Exporte les animations retenues, seules, sans les textes des écrans : une vidéo sur fond blanc (MP4),
// une vidéo sur fond transparent (WebM), et la dernière image (PNG transparent).
//
// Usage (depuis la racine du dépôt) : NODE_PATH=<dossier où Playwright est installé> node outils/exporter-animations.mjs [dossier de sortie]
// Il faut Playwright (Chromium) et ffmpeg (libx264, libvpx-vp9).
//
// Chaque maquette est ouverte en mouvement normal, figée (?t=0), puis rejouée image par image à 60 images/s
// par sa réglette de lecture. Tout l'écran est masqué sauf l'illustration. La vidéo garde toute la largeur
// de l'écran (390 pt) et se cadre en hauteur sur ce qui bouge ; exports.json donne, pour chaque vidéo,
// sa hauteur depuis le haut de l'écran, pour la replacer.
import { createRequire } from 'module';
import { execFileSync } from 'child_process';
import { mkdirSync, rmSync, writeFileSync, copyFileSync } from 'fs';
import { resolve, join } from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const SORTIE = resolve(process.argv[2] || 'exports/animations');
const IPS = 60;          // images par seconde
const ECHELLE = 2;       // pixels par point : 780 px de large
const MARGE = 6;         // points autour de ce qui bouge (les traits débordent un peu des tracés)

// Les animations retenues par la porteuse (12/10).
const EXPORTS = [
  ['formulaire-envoye_signalement_tampon-bis', 'formulaire-envoye.html', 'formulaire=signalement&piste=tamponbis'],
  ['formulaire-envoye_contribution-photo_photomaton-bis', 'formulaire-envoye.html', 'formulaire=photo&piste=photomatonbis'],
  ['formulaire-envoye_support', 'formulaire-envoye.html', 'formulaire=support'],
  ['connexion-insuffisante_couleurs', 'connexion-insuffisante.html', 'cause=faible&couleurs=couleurs'],
  ['connexion-insuffisante_gris', 'connexion-insuffisante.html', 'cause=faible&couleurs=gris'],
  ['pas-de-connexion_couleurs', 'connexion-insuffisante.html', 'cause=aucune&couleurs=couleurs'],
  ['pas-de-connexion_gris', 'connexion-insuffisante.html', 'cause=aucune&couleurs=gris'],
  ['mise-a-jour-obligatoire_ancienne-version', 'mise-a-jour-obligatoire.html', 'ecran=ancienne'],
  ['mise-a-jour-obligatoire_nouvelle-version', 'mise-a-jour-obligatoire.html', 'ecran=nouvelle'],
  ['delai-de-connexion_cent-pas', 'delai-connexion.html', 'piste=centpas&couleurs=couleurs'],
  ['produit-inconnu_cagette-vide', 'produit-inconnu.html', 'piste=cagette&couleurs=couleurs'],
  ['service-indisponible_store-de-l-etal', 'service-indisponible.html', 'piste=store&couleurs=couleurs']
];

// Tout l'écran disparaît, sauf l'illustration ; plus de fond nulle part.
const CSS = `
html,body,.page,.stage-wrap,.stage{background:transparent!important}
.panel{display:none!important}
.screen{background:transparent!important;box-shadow:none!important;border-radius:0!important;visibility:hidden!important}
.screen .illu svg{visibility:visible!important}
`;

// Dans la page : ce qui est visible à cet instant, en points depuis le haut de l'écran.
function etendue() {
  const ecran = document.getElementById('screen').getBoundingClientRect();
  const svg = document.querySelector('.illu svg');
  let haut = Infinity, bas = -Infinity;
  const visible = el => {
    for (let e = el; e && e !== svg; e = e.parentElement) {
      const o = e.getAttribute('opacity');
      if (o !== null && +o <= 0.004) return false;
      if (getComputedStyle(e).display === 'none') return false;
    }
    return true;
  };
  for (const el of svg.querySelectorAll('path,rect,circle,ellipse,line,polyline,polygon,use')) {
    if (el.closest('clipPath') || !visible(el)) continue;
    const r = el.getBoundingClientRect();
    if (!r.width && !r.height) continue;
    if (r.right < ecran.left || r.left > ecran.right) continue;
    haut = Math.min(haut, r.top - ecran.top);
    bas = Math.max(bas, r.bottom - ecran.top);
  }
  return [haut, bas];
}

function aller(page, t) {
  return page.evaluate(t => {
    const s = document.getElementById('scrub');
    s.step = 'any';
    s.value = t;
    s.dispatchEvent(new Event('input'));
  }, t);
}

mkdirSync(SORTIE, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1000 }, deviceScaleFactor: ECHELLE });
const erreurs = [];
page.on('pageerror', e => erreurs.push(String(e)));
const manifeste = [];

for (const [nom, fichier, requete] of EXPORTS) {
  await page.goto('file://' + resolve('maquettes', fichier) + '?' + requete + '&mouvement=normal&notes=off&t=0');
  await page.addStyleTag({ content: CSS });
  await page.waitForTimeout(300);
  const duree = await page.evaluate(() => +document.getElementById('scrub').max);
  const n = Math.round(duree / 1000 * IPS);

  // Premier passage : la hauteur de tout ce qui paraît, d'un bout à l'autre.
  let haut = Infinity, bas = -Infinity;
  for (let t = 0; t <= duree; t += 25) {
    await aller(page, t);
    const [h, b] = await page.evaluate(etendue);
    haut = Math.min(haut, h); bas = Math.max(bas, b);
  }
  haut = Math.max(0, Math.floor(haut - MARGE));
  bas = Math.min(844, Math.ceil(bas + MARGE));

  // Second passage : les images, détourées.
  const ecran = await page.locator('#screen').boundingBox();
  const images = join(SORTIE, '.images-' + nom);
  rmSync(images, { recursive: true, force: true });
  mkdirSync(images);
  for (let i = 0; i <= n; i++) {
    await aller(page, Math.min(duree, i * 1000 / IPS));
    await page.screenshot({
      path: join(images, String(i).padStart(4, '0') + '.png'),
      clip: { x: ecran.x, y: ecran.y + haut, width: 390, height: bas - haut },
      omitBackground: true
    });
  }

  const w = 390 * ECHELLE, h = (bas - haut) * ECHELLE;
  const entree = ['-y', '-v', 'error', '-framerate', String(IPS), '-i', join(images, '%04d.png')];
  execFileSync('ffmpeg', [...entree,
    '-filter_complex', `color=c=white:s=${w}x${h}:r=${IPS}[fond];[fond][0:v]overlay=shortest=1,format=yuv420p`,
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-movflags', '+faststart', join(SORTIE, nom + '.mp4')]);
  execFileSync('ffmpeg', [...entree,
    '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-crf', '18', '-b:v', '0', '-auto-alt-ref', '0', '-row-mt', '1',
    join(SORTIE, nom + '_transparent.webm')]);
  copyFileSync(join(images, String(n).padStart(4, '0') + '.png'), join(SORTIE, nom + '_derniere-image.png'));
  rmSync(images, { recursive: true, force: true });

  manifeste.push({ nom, maquette: 'maquettes/' + fichier + '?' + requete, duree_ms: duree, images_par_seconde: IPS,
    largeur_pt: 390, hauteur_pt: bas - haut, haut_depuis_le_haut_de_l_ecran_pt: haut, pixels_par_point: ECHELLE });
  console.log(`${nom} : ${duree} ms, ${n + 1} images, ${w} × ${h} px, à ${haut} pt du haut de l'écran`);
}
writeFileSync(join(SORTIE, 'exports.json'), JSON.stringify(manifeste, null, 2) + '\n');
await browser.close();
if (erreurs.length) { console.error('ERREURS\n' + erreurs.join('\n')); process.exit(1); }
