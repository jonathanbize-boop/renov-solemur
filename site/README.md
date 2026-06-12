# Site Rénov'Solèmur — nouvelle version

Refonte complète du site www.renov-solemur.com : 16 pages statiques (HTML/CSS/JS),
sans dépendance à une plateforme. L'organisation et les titres des pages de
l'ancien site sont conservés (mêmes URLs : `/carrelage`, `/peinture`, etc.).

## Contenu du dossier

```
site/
├── index.html                  Accueil
├── a-propos/                   L'entreprise
├── platrerie/                  ... 11 pages prestations ...
├── guilherand-granges/         Page SEO locale
├── contact/                    Formulaire de devis
├── mentions-legales/           Mentions légales (noindex)
├── sitemap.xml                 Plan du site pour Google
├── robots.txt
└── assets/
    ├── css/style.css           Design system complet
    ├── js/main.js              Animations & interactions
    └── img/                    54 visuels (noms optimisés SEO)
```

## Mise en ligne

Le site est 100 % statique : il fonctionne sur n'importe quel hébergeur.

- **Hébergement simple (OVH, o2switch…)** : copier le CONTENU du dossier `site/`
  à la racine du serveur web (FTP). Les URLs propres (`/carrelage`) fonctionnent
  automatiquement grâce aux dossiers `slug/index.html`.
- **Netlify / Vercel / Cloudflare Pages (gratuit)** : glisser-déposer le dossier
  `site/` — HTTPS et CDN inclus.

⚠️ Avant la mise en ligne, conserver le nom de domaine www.renov-solemur.com
(les balises canoniques et le sitemap pointent vers ce domaine).

## Après la mise en ligne (SEO)

1. Déclarer le site dans **Google Search Console** et soumettre `sitemap.xml`.
2. Vérifier que la fiche Google Business pointe vers le site.
3. Les anciennes URLs étant conservées, aucune redirection n'est nécessaire.

## Modifier le site

Les pages sont générées par les scripts du dossier `../site-src/` :

- `build.py` — gabarit commun (header, footer, SEO, schémas)
- `content_core.py` — accueil, à propos, contact, Guilherand-Granges, mentions
- `content_services.py` — les 11 pages prestations

Pour régénérer après modification : `python site-src/build.py`
(nécessite Python 3, déjà installé sur ce poste).

Pour prévisualiser en local : `python -m http.server 8742 --directory site`
puis ouvrir http://localhost:8742

## Points à personnaliser (suggestions)

- **Formulaire de contact** : il ouvre actuellement le logiciel de messagerie du
  visiteur (mailto vers renovsolemur@yahoo.fr). Pour un envoi direct sans
  ouverture de messagerie, brancher un service comme Formspree ou le module de
  formulaire de l'hébergeur.
- **Avis Google** : la section avis renvoie vers la fiche Google. Si vous me
  fournissez 3 avis réels (texte + prénom), je peux les afficher en cartes sur
  la page d'accueil.
- **Photos de chantier** : plus vous ajouterez de vraies photos avant/après,
  plus les sliders de comparaison seront percutants.
