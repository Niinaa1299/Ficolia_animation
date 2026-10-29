// Exporte l'ouverture retenue (29/10) en plein écran et sans aucun texte : la révélation et « l'arbre et la figue »
// (recul3), puis l'accueil 2/2, piste A. Les textes restent du HTML, posés par-dessus et modifiables
// (exports/ouverture/ouverture.html) : rien n'est écrit dans les vidéos ni dans les images.
//
// Usage (depuis la racine du dépôt) : NODE_PATH=<dossier où Playwright est installé> node outils/exporter-ouverture.mjs [dossier de sortie] [--garder]
// Il faut Playwright (Chromium) et ffmpeg (libx264, libvpx-vp9). --garder laisse les images de chaque vidéo à côté (.images-…).
//
// Comme outils/exporter-animations.mjs : la maquette est ouverte figée (?t=0), puis rejouée image par image à 60 images/s
// par sa réglette de lecture. Ici, tout l'écran est gardé (390 × 844 pt, en ×2 : 780 × 1688 px), fond compris, sauf les textes.
import { createRequire } from 'module';
import { execFileSync } from 'child_process';
import { mkdirSync, rmSync, writeFileSync, copyFileSync, statSync } from 'fs';
import { resolve, join } from 'path';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const args = process.argv.slice(2);
const GARDER = args.includes('--garder');
const SORTIE = resolve(args.find(a => !a.startsWith('--')) || 'exports/ouverture');
const IPS = 60;          // images par seconde
const ECHELLE = 2;       // pixels par point : 780 × 1688 px
const MAQUETTE = resolve('maquettes/ouverture-arbre.html');

// Les choix de la porteuse, écrits en entier : la maquette ne dépend pas de ses réglages par défaut.
const CHOIX = 'place=b&bas=pale-bis&descente=a&decor=a&transition=recul3&notes=off';
const VIDEOS = [
  // La révélation, puis l'arbre et la figue, jusqu'à l'image fixe de l'accueil 1/2 (10 s).
  { nom: 'ouverture', requete: CHOIX + '&ecran=1&mouvement=normal' },
  // Après « Continuer » : l'accueil 2/2, piste A, de la dernière image du 1/2 à son image fixe (4,4 s).
  { nom: 'accueil-2_piste-a', requete: CHOIX + '&ecran=2&piste2=a&mouvement=normal' }
];
// La fin de la révélation, seule, pour « réduire les animations » : le logo, sans l'accroche (mouvement réduit, à 1 s),
// détouré : posé sur le blanc de l'écran, il s'efface pendant que le paysage paraît, comme dans la maquette.
const REVELATION = { nom: 'revelation_derniere-image', requete: CHOIX + '&ecran=1&mouvement=reduit', t: 1000 };

// Les textes disparaissent ; le reste de l'écran est gardé tel quel, sans les coins arrondis ni l'ombre du téléphone.
const CSS = `
html,body,.page,.stage-wrap,.stage{background:transparent!important}
.panel{display:none!important}
.screen{border-radius:0!important;box-shadow:none!important}
#accroche,#accueil,#accueil2,#bienvenue{visibility:hidden!important}
`;

function aller(page, t) {
  return page.evaluate(t => {
    const s = document.getElementById('scrub');
    s.step = 'any';
    s.value = t;
    s.dispatchEvent(new Event('input'));
  }, t);
}

async function ouvrir(page, requete) {
  await page.goto('file://' + MAQUETTE + '?' + requete + '&t=0');
  await page.addStyleTag({ content: CSS });
  await page.waitForTimeout(300);
  return page.evaluate(() => +document.getElementById('scrub').max);
}

const octets = f => (statSync(f).size / 1e6).toFixed(2) + ' Mo';

mkdirSync(SORTIE, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1000 }, deviceScaleFactor: ECHELLE });
const erreurs = [];
page.on('pageerror', e => erreurs.push(String(e)));
const manifeste = { videos: [], images: [] };

for (const { nom, requete } of VIDEOS) {
  const duree = await ouvrir(page, requete);
  const n = Math.round(duree / 1000 * IPS);
  const images = join(SORTIE, '.images-' + nom);
  rmSync(images, { recursive: true, force: true });
  mkdirSync(images);
  for (let i = 0; i <= n; i++) {
    await aller(page, Math.min(duree, i * 1000 / IPS));
    await page.locator('#screen').screenshot({ path: join(images, String(i).padStart(4, '0') + '.png') });
  }
  // Couleurs : la matrice BT.709, écrite dans le fichier, pour que le navigateur rende les couleurs de la maquette.
  const entree = ['-y', '-v', 'error', '-framerate', String(IPS), '-i', join(images, '%04d.png'),
    '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p',
    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv'];
  execFileSync('ffmpeg', [...entree, '-c:v', 'libx264', '-preset', 'slow', '-crf', '14', '-tune', 'animation',
    '-movflags', '+faststart', join(SORTIE, nom + '.mp4')]);
  execFileSync('ffmpeg', [...entree, '-c:v', 'libvpx-vp9', '-crf', '20', '-b:v', '0', '-row-mt', '1',
    '-deadline', 'good', '-cpu-used', '1', join(SORTIE, nom + '.webm')]);
  copyFileSync(join(images, String(n).padStart(4, '0') + '.png'), join(SORTIE, nom.replace(/^ouverture$/, 'accueil-1') + '_derniere-image.png'));
  if (!GARDER) rmSync(images, { recursive: true, force: true });
  manifeste.videos.push({ nom, maquette: 'maquettes/ouverture-arbre.html?' + requete, duree_ms: duree, images_par_seconde: IPS,
    largeur_pt: 390, hauteur_pt: 844, pixels_par_point: ECHELLE, mp4: octets(join(SORTIE, nom + '.mp4')), webm: octets(join(SORTIE, nom + '.webm')) });
  console.log(`${nom} : ${duree} ms, ${n + 1} images ; mp4 ${octets(join(SORTIE, nom + '.mp4'))}, webm ${octets(join(SORTIE, nom + '.webm'))}`);
}

await ouvrir(page, REVELATION.requete);
await page.addStyleTag({ content: '.screen{background:transparent!important}' });
await aller(page, REVELATION.t);
await page.locator('#screen').screenshot({ path: join(SORTIE, REVELATION.nom + '.png'), omitBackground: true });
for (const nom of ['revelation_derniere-image', 'accueil-1_derniere-image', 'accueil-2_piste-a_derniere-image']) {
  manifeste.images.push({ nom: nom + '.png', largeur_pt: 390, hauteur_pt: 844, pixels_par_point: ECHELLE });
}
writeFileSync(join(SORTIE, 'exports.json'), JSON.stringify(manifeste, null, 2) + '\n');
await browser.close();
if (erreurs.length) { console.error('ERREURS\n' + erreurs.join('\n')); process.exit(1); }
