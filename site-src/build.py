# -*- coding: utf-8 -*-
"""Générateur du site Rénov'Solèmur — template commun + contenus par page."""
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site")

SITE = {
    "name": "Rénov'Solèmur",
    "url": "https://www.renov-solemur.com",
    "tel": "06 63 06 65 17",
    "tel_link": "+33663066517",
    "email": "renovsolemur@yahoo.fr",
    "address": "Rue Jean Vilar, 26000 Valence",
    "city": "Valence",
    "google": "https://share.google/py0PtZemcee7yS6UK",
}

# ---------------------------------------------------------------- icônes SVG
def icon(name, cls=""):
    paths = {
        "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
        "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
        "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
        "check": '<path d="M21.801 10A10 10 0 1 1 17 3.335"/><path d="m9 11 3 3L22 4"/>',
        "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
        "chevron": '<path d="m6 9 6 6 6-6"/>',
        "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
        "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
        "hammer": '<path d="m15 12-8.373 8.373a1 1 0 1 1-3-3L12 9"/><path d="m18 15 4-4"/><path d="m21.5 11.5-1.914-1.914A2 2 0 0 1 19 8.172V7l-2.26-2.26a6 6 0 0 0-4.202-1.756L9 2.96l.92.82A6.18 6.18 0 0 1 12 8.4V10l2 2h1.172a2 2 0 0 1 1.414.586L18.5 14.5"/>',
        "roller": '<path d="M10 2v2"/><path d="M14 2v4"/><path d="M17 2a1 1 0 0 1 1 1v9H6V3a1 1 0 0 1 1-1z"/><path d="M6 12a1 1 0 0 0-1 1v1a2 2 0 0 0 2 2h2a1 1 0 0 1 1 1v2.9a2 2 0 1 0 4 0V17a1 1 0 0 1 1-1h2a2 2 0 0 0 2-2v-1a1 1 0 0 0-1-1"/>',
        "wallpaper": '<circle cx="8" cy="9" r="2"/><path d="m9 17 6.1-6.1a2 2 0 0 1 2.81.01L22 15V5a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2"/><path d="M8 21h8"/><path d="M12 17v4"/>',
        "grid": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/><path d="M15 3v18"/>',
        "wood": '<path d="M2 20h20"/><path d="M2 4h20"/><path d="M4 4v16"/><path d="M10 4v16"/><path d="M16 4v16"/><path d="M7 8v2"/><path d="M13 14v2"/><path d="M19 7v3"/>',
        "layers": '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
        "bath": '<path d="M10 4 8 6"/><path d="M17 19v2"/><path d="M2 12h20"/><path d="M7 19v2"/><path d="M9 5 7.62 3.62A2.12 2.12 0 1 0 4.62 6.62L6 8"/><path d="M2 12v4a4 4 0 0 0 4 4h12a4 4 0 0 0 4-4v-4"/>',
        "alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
        "wall": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v6"/><path d="M15 9v6"/><path d="M9 15v6"/>',
        "thermo": '<path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/>',
        "home": '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
        "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
        "ruler": '<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.41 2.41 0 0 1 0-3.4l2.6-2.6a2.41 2.41 0 0 1 3.4 0Z"/><path d="m14.5 12.5 2-2"/><path d="m11.5 9.5 2-2"/><path d="m8.5 6.5 2-2"/><path d="m17.5 15.5 2-2"/>',
        "sparkle": '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/>',
    }
    return ('<svg class="%s" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>' % (cls, paths[name]))


BRUSH_SVG = ('<svg viewBox="0 0 320 30" preserveAspectRatio="none" aria-hidden="true">'
             '<path d="M4 22 C 60 12, 120 26, 180 17 S 280 14, 316 19"/></svg>')


def brush(text):
    return '<span class="brush">%s%s</span>' % (text, BRUSH_SVG)


# ------------------------------------------------------- prestations (nav)
PRESTATIONS = [
    ("platrerie", "Plâtrerie", "Cloisons, plafonds, enduits", "wall"),
    ("isolation-interieure", "Isolation intérieure", "Confort thermique & économies", "thermo"),
    ("peinture", "Peinture intérieure", "Murs & plafonds, toutes finitions", "roller"),
    ("papier-peint", "Papier peint", "Pose soignée, déco unique", "wallpaper"),
    ("carrelage", "Carrelage", "Sols & murs, intérieur", "grid"),
    ("parquet", "Parquet", "Flottant, massif, rénovation", "wood"),
    ("sol-souple", "Sols souples", "PVC, lino, moquette, jonc de mer", "layers"),
    ("renovation-salle-bains", "Salle de bains", "Rénovation complète clés en main", "bath"),
    ("renovation-apres-sinistre", "Après sinistre", "Dégât des eaux, incendie", "alert"),
]


def nav_dropdown():
    items = []
    for slug, label, desc, ic in PRESTATIONS:
        items.append(
            '<li><a href="/%s"><span class="ic">%s</span><span><strong>%s</strong>'
            '<span>%s</span></span></a></li>' % (slug, icon(ic), label, desc))
    items.append('<li><a class="dropdown__all" href="/revetements-sol">Tous les revêtements de sol %s</a></li>'
                 % icon("arrow"))
    items.append('<li><a class="dropdown__all" href="/revetements-muraux">Tous les revêtements muraux %s</a></li>'
                 % icon("arrow"))
    return "\n".join(items)


def header(active=""):
    def cur(slug):
        return ' aria-current="page"' if active == slug else ""
    return """<a class="skip-link" href="#main">Aller au contenu principal</a>
<div class="topbar">
  <div class="container">
    <p class="topbar__zone">%(pin)s Valence · Guilherand-Granges · Drôme &amp; Ardèche</p>
    <p>Devis gratuit&nbsp;: <a href="tel:%(tel_link)s">%(tel)s</a></p>
  </div>
</div>
<header class="site-header">
  <nav class="nav container" aria-label="Navigation principale">
    <a class="nav__logo" href="/" aria-label="Rénov'Solèmur — retour à l'accueil">
      <img src="/assets/img/logo-renov-solemur.webp" alt="Logo Rénov'Solèmur, entreprise de rénovation intérieure à Valence" width="180" height="130">
    </a>
    <div class="nav__menu" id="menu">
      <ul class="nav__list">
        <li><a class="nav__link" href="/"%(cur_home)s>Accueil</a></li>
        <li><a class="nav__link" href="/a-propos"%(cur_apropos)s>L'entreprise</a></li>
        <li>
          <a class="nav__link" href="/revetements-sol" aria-haspopup="true">Nos prestations %(chevron)s</a>
          <ul class="dropdown">%(dropdown)s</ul>
        </li>
        <li><a class="nav__link" href="/guilherand-granges"%(cur_gg)s>Guilherand-Granges</a></li>
        <li><a class="nav__link" href="/contact"%(cur_contact)s>Contact</a></li>
      </ul>
    </div>
    <div class="nav__cta">
      <a class="nav__tel" href="tel:%(tel_link)s">%(phone)s<span>%(tel)s</span></a>
      <a class="btn btn--primary" href="/contact">Devis gratuit</a>
      <button class="burger" aria-expanded="false" aria-controls="menu" aria-label="Ouvrir le menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</header>
<a class="fab-tel" href="tel:%(tel_link)s" aria-label="Appeler Rénov'Solèmur au %(tel)s">%(phone)s</a>""" % {
        "pin": icon("pin"), "phone": icon("phone"), "chevron": icon("chevron"),
        "tel": SITE["tel"], "tel_link": SITE["tel_link"], "dropdown": nav_dropdown(),
        "cur_home": cur("index"), "cur_apropos": cur("a-propos"),
        "cur_gg": cur("guilherand-granges"), "cur_contact": cur("contact"),
    }


def footer():
    presta_links = "\n".join('<li><a href="/%s">%s</a></li>' % (s, l) for s, l, _, _ in PRESTATIONS)
    return """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/img/logo-renov-solemur.webp" alt="Rénov'Solèmur" width="160" height="116" loading="lazy">
        <p>Entreprise de rénovation intérieure à Valence depuis 2012. Du sol au plafond, nous coordonnons tous les corps de métier pour transformer durablement votre habitat.</p>
        <span class="hand">L'artisan qui donne vie à vos murs&nbsp;!</span>
      </div>
      <div>
        <h3>Nos prestations</h3>
        <ul>%(presta)s</ul>
      </div>
      <div>
        <h3>L'entreprise</h3>
        <ul>
          <li><a href="/a-propos">Qui sommes-nous&nbsp;?</a></li>
          <li><a href="/revetements-sol">Revêtements de sol</a></li>
          <li><a href="/revetements-muraux">Revêtements muraux</a></li>
          <li><a href="/guilherand-granges">Rénovation à Guilherand-Granges</a></li>
          <li><a href="/contact">Demander un devis</a></li>
          <li><a href="%(google)s" rel="noopener" target="_blank">Nos avis Google</a></li>
        </ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul class="footer-contact">
          <li>%(pin)s<span>%(address)s</span></li>
          <li>%(phone)s<a href="tel:%(tel_link)s">%(tel)s</a></li>
          <li>%(mail)s<a href="mailto:%(email)s">%(email)s</a></li>
          <li>%(clock)s<span>Du lundi au vendredi — devis gratuit</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© <span data-year>2026</span> Rénov'Solèmur — Entreprise de rénovation intérieure à Valence. Tous droits réservés.</p>
      <p><a href="/mentions-legales">Mentions légales &amp; confidentialité</a></p>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>""" % {
        "presta": presta_links, "google": SITE["google"], "pin": icon("pin"),
        "phone": icon("phone"), "mail": icon("mail"), "clock": icon("clock"),
        "address": SITE["address"], "tel": SITE["tel"], "tel_link": SITE["tel_link"],
        "email": SITE["email"],
    }


# --------------------------------------------------------------- schémas SEO
def schema_business():
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": SITE["url"] + "/#business",
        "name": "Rénov'Solèmur",
        "description": "Entreprise de rénovation intérieure à Valence : plâtrerie, isolation, peinture, revêtements de sols et murs, salle de bains, rénovation après sinistre.",
        "url": SITE["url"],
        "telephone": "+33 6 63 06 65 17",
        "email": SITE["email"],
        "image": SITE["url"] + "/assets/img/logo-renov-solemur.webp",
        "logo": SITE["url"] + "/assets/img/logo-renov-solemur.webp",
        "foundingDate": "2012",
        "priceRange": "€€",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Rue Jean Vilar",
            "addressLocality": "Valence",
            "postalCode": "26000",
            "addressCountry": "FR",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 44.933, "longitude": 4.892},
        "areaServed": [
            {"@type": "City", "name": "Valence"},
            {"@type": "City", "name": "Guilherand-Granges"},
            {"@type": "AdministrativeArea", "name": "Drôme"},
            {"@type": "AdministrativeArea", "name": "Ardèche"},
        ],
        "hasMap": SITE["google"],
    }


def schema_breadcrumb(crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE["url"] + path}
            for i, (name, path) in enumerate(crumbs)
        ],
    }


def schema_service(name, desc, slug):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": desc,
        "url": SITE["url"] + "/" + slug,
        "provider": {"@id": SITE["url"] + "/#business"},
        "areaServed": {"@type": "City", "name": "Valence"},
    }


def schema_faq(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }


# ------------------------------------------------------------ blocs communs
def page_hero(page):
    """Hero standard des pages internes."""
    crumbs_html = ['<a href="/">Accueil</a>']
    for name, path in page.get("crumbs", []):
        crumbs_html.append(icon("chevron"))
        crumbs_html.append('<a href="%s">%s</a>' % (path, name))
    crumbs_html.append(icon("chevron"))
    crumbs_html.append("<span>%s</span>" % page["crumb"])
    return """<section class="page-hero">
  <div class="container">
    <div class="reveal reveal--left">
      <nav class="breadcrumb" aria-label="Fil d'Ariane">%(crumbs)s</nav>
      <h1>%(h1)s</h1>
      <p class="lead">%(lead)s</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="/contact">Demander un devis gratuit %(arrow)s</a>
        <a class="btn btn--light" href="tel:%(tel_link)s">%(phone)s %(tel)s</a>
      </div>
    </div>
    <div class="page-hero__media reveal reveal--right" data-delay="1">
      <img src="%(img)s" alt="%(alt)s" width="900" height="650" fetchpriority="high">%(illu)s
    </div>
  </div>
</section>""" % {
        "crumbs": "\n".join(crumbs_html), "h1": page["h1"], "lead": page["lead"],
        "img": page["hero_img"], "alt": page["hero_alt"],
        "illu": ('<img class="page-hero__illu" src="/assets/img/%s" alt="" width="120" height="120" loading="lazy">'
                 % page["illu"]) if page.get("illu") else "",
        "arrow": icon("arrow"), "phone": icon("phone"),
        "tel": SITE["tel"], "tel_link": SITE["tel_link"],
    }


def cta_band(title=None, hand=None):
    return """<section class="cta-band">
  <div class="container">
    <div class="reveal">
      <span class="hand">%(hand)s</span>
      <h2>%(title)s</h2>
    </div>
    <div class="cta-band__actions reveal" data-delay="1">
      <a class="btn btn--light" href="/contact">Demander un devis gratuit %(arrow)s</a>
      <a class="btn btn--ghost" href="tel:%(tel_link)s">%(phone)s %(tel)s</a>
    </div>
  </div>
</section>""" % {
        "title": title or "Parlons de votre projet de rénovation",
        "hand": hand or "Devis gratuit & réponse rapide",
        "arrow": icon("arrow"), "phone": icon("phone"),
        "tel": SITE["tel"], "tel_link": SITE["tel_link"],
    }


def faq_block(items, kicker="Questions fréquentes", title="On répond à vos questions"):
    detail = "\n".join(
        """<details class="reveal"%s>
  <summary>%s</summary>
  <div class="faq__a"><p>%s</p></div>
</details>""" % (' data-delay="%d"' % min(i, 3) if i else "", q, a)
        for i, (q, a) in enumerate(items))
    return """<section class="section section--paper">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="kicker">%s</p>
      <h2>%s</h2>
    </div>
    <div class="faq">%s</div>
  </div>
</section>""" % (kicker, title, detail)


def other_services(exclude, title="Découvrez nos autres prestations"):
    cards = []
    pool = [p for p in PRESTATIONS if p[0] not in exclude][:3]
    imgs = {
        "platrerie": "platrerie-valence-1.jpg", "isolation-interieure": "isolation-interieure-valence-2.jpg",
        "peinture": "peinture-interieure-valence-1.jpg", "papier-peint": "pose-papier-peint-valence-1.jpg",
        "carrelage": "pose-carrelage-valence-1.jpg", "parquet": "pose-parquet-valence-1.jpg",
        "sol-souple": "pose-sol-souple-valence-1.jpg",
        "renovation-salle-bains": "renovation-salle-bains-valence.jpg",
        "renovation-apres-sinistre": "renovation-apres-sinistre-1.jpg",
    }
    for i, (slug, label, desc, _) in enumerate(pool):
        cards.append("""<article class="card reveal"%s>
  <div class="card__media"><img src="/assets/img/%s" alt="%s à Valence — Rénov'Solèmur" loading="lazy" width="640" height="400"></div>
  <div class="card__body">
    <h3>%s</h3>
    <p>%s.</p>
    <a class="card__link card__cover" href="/%s">Découvrir %s</a>
  </div>
</article>""" % (' data-delay="%d"' % i if i else "", imgs[slug], label, label, desc, slug, icon("arrow")))
    return """<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Pour aller plus loin</p>
      <h2>%s</h2>
    </div>
    <div class="cards">%s</div>
  </div>
</section>""" % (title, "\n".join(cards))


# ------------------------------------------------------------------ template
def render(page):
    schemas = [schema_business()] + page.get("schemas", [])
    jsonld = "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False)
        for s in schemas)
    canonical = SITE["url"] + ("/" if page["slug"] == "index" else "/" + page["slug"])
    og_img = SITE["url"] + page.get("hero_img", "/assets/img/renovation-interieure-valence-hero.jpg")
    html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%(title)s</title>
  <meta name="description" content="%(desc)s">
  <link rel="canonical" href="%(canonical)s">
  <meta name="robots" content="%(robots)s">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Rénov'Solèmur">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="%(title)s">
  <meta property="og:description" content="%(desc)s">
  <meta property="og:url" content="%(canonical)s">
  <meta property="og:image" content="%(og_img)s">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#c2491f">
  <link rel="icon" type="image/webp" href="/assets/img/logo-renov-solemur.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Outfit:wght@400;500;600;700&family=Caveat:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
  %(jsonld)s
</head>
<body>
%(header)s
<main id="main">
%(body)s
</main>
%(footer)s
</body>
</html>""" % {
        "title": page["title"], "desc": page["desc"], "canonical": canonical,
        "robots": page.get("robots", "index, follow"), "og_img": og_img,
        "jsonld": jsonld, "header": header(page["slug"]), "body": page["body"],
        "footer": footer(),
    }
    if page["slug"] == "index":
        path = os.path.join(OUT, "index.html")
    else:
        os.makedirs(os.path.join(OUT, page["slug"]), exist_ok=True)
        path = os.path.join(OUT, page["slug"], "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("OK  %s" % os.path.relpath(path, OUT))


def sitemap(pages):
    rows = []
    for p in pages:
        if p.get("robots", "").startswith("noindex"):
            continue
        loc = SITE["url"] + ("/" if p["slug"] == "index" else "/" + p["slug"])
        prio = "1.0" if p["slug"] == "index" else ("0.5" if p["slug"] == "mentions-legales" else "0.8")
        rows.append("  <url><loc>%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>" % (loc, prio))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
           % "\n".join(rows))
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE["url"])
    print("OK  sitemap.xml + robots.txt")


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    from content_core import CORE_PAGES
    from content_services import SERVICE_PAGES
    pages = CORE_PAGES + SERVICE_PAGES
    for p in pages:
        render(p)
    sitemap(pages)
    print("\n%d pages générées." % len(pages))
