# -*- coding: utf-8 -*-
"""Pages principales : accueil, à propos, contact, Guilherand-Granges, mentions légales."""
from build import (SITE, icon, brush, cta_band, faq_block, page_hero,
                   schema_breadcrumb, schema_faq, PRESTATIONS)

ARROW = icon("arrow")
CHECK = icon("check")
PHONE = icon("phone")
STAR = icon("star")

# ============================================================== ACCUEIL
HOME_CARDS = [
    ("platrerie", "Plâtrerie", "Cloisons sèches, plafonds et faux plafonds : des surfaces parfaitement lisses, prêtes à recevoir tous vos revêtements", "platrerie-valence-1.jpg", "Travaux de plâtrerie et cloisons sèches à Valence", "Murs & plafonds"),
    ("isolation-interieure", "Isolation intérieure", "Isolation thermique par l'intérieur (ITI) en laine minérale ou naturelle : murs, plafonds et combles", "isolation-interieure-valence-2.jpg", "Isolation thermique par l'intérieur à Valence", "Confort & économies"),
    ("revetements-muraux", "Peinture & papier peint", "Toutes les finitions de peinture (mat, satin, brillant) et pose de papier peint pour une décoration unique", "peinture-interieure-valence-1.jpg", "Peinture intérieure et revêtements muraux à Valence", "Revêtements muraux"),
    ("revetements-sol", "Revêtements de sol", "Carrelage, parquet, sols souples : un large choix de matériaux posés dans les règles de l'art", "pose-parquet-valence-1.jpg", "Pose de revêtements de sol, carrelage et parquet à Valence", "Sols"),
    ("renovation-salle-bains", "Salle de bains", "Rénovation complète clés en main, du démontage aux finitions, y compris aménagements PMR", "renovation-salle-bains-valence.jpg", "Rénovation complète de salle de bains à Valence", "Clés en main"),
    ("renovation-apres-sinistre", "Après sinistre", "Dégât des eaux ou incendie : remise en état complète, en lien direct avec votre assurance", "renovation-apres-sinistre-1.jpg", "Rénovation après sinistre, dégât des eaux et incendie à Valence", "Urgence & assurance"),
]

home_cards_html = "\n".join("""<article class="card reveal"%s>
  <div class="card__media">
    <span class="card__tag">%s</span>
    <img src="/assets/img/%s" alt="%s" loading="lazy" width="640" height="400">
  </div>
  <div class="card__body">
    <h3>%s</h3>
    <p>%s.</p>
    <a class="card__link card__cover" href="/%s">En savoir plus %s</a>
  </div>
</article>""" % (' data-delay="%d"' % (i % 3) if i % 3 else "", tag, img, alt, label, desc, slug, ARROW)
    for i, (slug, label, desc, img, alt, tag) in enumerate(HOME_CARDS))

HOME_BODY = """
<section class="hero">
  <svg class="hero__splat" style="top:8%%;left:46%%" viewBox="0 0 100 100" fill="currentColor" aria-hidden="true"><circle cx="50" cy="50" r="28"/><circle cx="82" cy="30" r="8"/><circle cx="20" cy="72" r="6"/><circle cx="76" cy="74" r="5"/></svg>
  <div class="container">
    <div class="hero__text">
      <span class="hero__hand reveal">Artisans à Valence depuis 2012</span>
      <h1 class="reveal" data-delay="1">Rénov'Solèmur, rénovation intérieure à Valence&nbsp;: transformez votre espace %(brush_style)s</h1>
      <p class="lead reveal" data-delay="2">Du sol au plafond, nous rénovons votre logement ou votre local professionnel&nbsp;: <strong>plâtrerie, isolation, peinture, sols, salle de bains</strong>. Un seul interlocuteur coordonne tous les corps de métier — et le devis est toujours gratuit.</p>
      <div class="hero__actions reveal" data-delay="3">
        <a class="btn btn--primary" href="/contact">Demander un devis gratuit %(arrow)s</a>
        <a class="btn btn--ghost" href="tel:%(tel_link)s">%(phone)s %(tel)s</a>
      </div>
      <ul class="hero__badges reveal" data-delay="4">
        <li>%(shield)s Garantie décennale</li>
        <li>%(check)s Devis gratuit</li>
        <li>%(users)s Particuliers &amp; professionnels</li>
      </ul>
    </div>
    <div class="hero__media reveal reveal--right" data-delay="2">
      <div class="hero__frame">
        <img src="/assets/img/artisan-renovation-valence.jpg" alt="Mur en cours de mise en peinture lors d'une rénovation intérieure à Valence" width="900" height="760" fetchpriority="high">
      </div>
      <img class="hero__illu" src="/assets/img/illustration-renovation-1.png" alt="" width="120" height="120">
      <img class="page-hero__illu" src="/assets/img/illustration-renovation-2.png" alt="" width="120" height="120" loading="lazy" style="animation-delay:1.2s">
      <div class="hero__card">
        <span class="num" data-count="10" data-suffix="+">10+</span>
        <span class="lbl">années<br>d'expérience<br>à Valence</span>
      </div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee__track"><span>Plâtrerie <i>✦</i> Isolation intérieure <i>✦</i> Peinture <i>✦</i> Papier peint <i>✦</i> Carrelage <i>✦</i> Parquet <i>✦</i> Sols souples <i>✦</i> Salle de bains <i>✦</i> Rénovation après sinistre <i>✦</i></span></div>
</div>

<section class="section" id="prestations">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Nos prestations</p>
      <h2>Toutes nos prestations de rénovation intérieure à Valence</h2>
      <p>Rénovons votre intérieur du sol au plafond&nbsp;! Nous intervenons sur tous types de chantiers en coordonnant les différents corps de métier, avec un seul objectif&nbsp;: <strong>rénover durablement votre logement ou votre local professionnel</strong>.</p>
    </div>
    <div class="cards">
%(cards)s
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="split">
      <div class="split__media split__media--duo reveal reveal--left">
        <span class="split__sticker">Fait main, fait bien&nbsp;!</span>
        <img src="/assets/img/renovation-interieure-valence-hero.jpg" alt="Isolation et aménagement de combles réalisés par Rénov'Solèmur" loading="lazy" width="700" height="600">
        <img src="/assets/img/sol-cuisine-apres-vitrification.jpg" alt="Sol de cuisine rénové et vitrifié par Rénov'Solèmur à Valence" loading="lazy" width="420" height="420">
      </div>
      <div class="split__text reveal reveal--right">
        <p class="kicker">Votre entreprise de rénovation</p>
        <h2>Un artisan local, un chantier %(brush_maitrise)s</h2>
        <p>Fondée en <strong>2012 à Valence</strong>, Rénov'Solèmur accompagne particuliers, professionnels et collectivités dans leurs projets de rénovation intérieure. Notre force&nbsp;: un interlocuteur unique qui étudie la faisabilité de votre projet, vous conseille sur les matériaux et coordonne tous les corps de métier.</p>
        <ul class="checklist">
          <li>%(check)s<div><strong>Garantie décennale</strong><span>Votre chantier est couvert pendant 10 ans après les travaux.</span></div></li>
          <li>%(check)s<div><strong>Devis gratuit et détaillé</strong><span>Étude de faisabilité, conseils matériaux et chiffrage transparent.</span></div></li>
          <li>%(check)s<div><strong>Respect des délais et du budget</strong><span>Un planning clair, tenu du premier au dernier jour du chantier.</span></div></li>
        </ul>
        <a class="btn btn--ghost" href="/a-propos">Découvrir l'entreprise %(arrow)s</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="kicker">Avant / Après</p>
      <h2>La preuve par nos chantiers</h2>
      <p>Faites glisser le curseur pour découvrir une de nos transformations réalisées à Valence.</p>
    </div>
    <div class="ba reveal reveal--zoom" style="max-width:900px;margin-inline:auto">
      <img src="/assets/img/chantier-avant-renovation.jpg" alt="Pièce avant les travaux de rénovation intérieure" loading="lazy" width="900" height="560">
      <img class="ba__after" src="/assets/img/chantier-apres-renovation.jpg" alt="La même pièce après rénovation complète par Rénov'Solèmur" loading="lazy" width="900" height="560">
      <span class="ba__label ba__label--avant">Avant</span>
      <span class="ba__label ba__label--apres">Après</span>
      <div class="ba__handle"></div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Notre méthode</p>
      <h2>Un déroulé simple, un résultat impeccable</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>Échange &amp; visite</h3><p>Vous nous présentez votre projet, nous nous déplaçons pour évaluer le chantier et écouter vos envies.</p></div>
      <div class="step reveal" data-delay="1"><h3>Devis gratuit</h3><p>Étude de faisabilité, conseils matériaux et chiffrage détaillé — sans engagement.</p></div>
      <div class="step reveal" data-delay="2"><h3>Travaux coordonnés</h3><p>Nos artisans interviennent en coordination, dans le respect des délais et du budget convenus.</p></div>
      <div class="step reveal" data-delay="3"><h3>Livraison soignée</h3><p>Réception du chantier ensemble, finitions vérifiées, garantie décennale activée.</p></div>
    </div>
    <div class="stats" style="margin-top:4rem">
      <div class="stat reveal"><span class="num" data-count="2012">2012</span><span class="lbl">Année de création</span></div>
      <div class="stat reveal" data-delay="1"><span class="num" data-count="10" data-suffix="+">10+</span><span class="lbl">Ans d'expérience</span></div>
      <div class="stat reveal" data-delay="2"><span class="num" data-count="10">10</span><span class="lbl">Ans de garantie décennale</span></div>
      <div class="stat reveal" data-delay="3"><span class="num" data-count="100" data-suffix="%%">100%%</span><span class="lbl">Devis gratuits</span></div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="split split--reverse">
      <div class="split__media reveal reveal--right">
        <img src="/assets/img/degat-des-eaux-salon.jpg" alt="Salon inondé après un dégât des eaux, avant remise en état par Rénov'Solèmur" loading="lazy" width="700" height="560">
      </div>
      <div class="split__text reveal reveal--left">
        <p class="kicker">Dégât des eaux · Incendie</p>
        <h2>Un sinistre&nbsp;? On remet votre habitat en état</h2>
        <p>Après un <strong>dégât des eaux ou un incendie</strong>, nos professionnels interviennent pour la remise en état complète de votre logement&nbsp;: plâtrerie, isolation, sols et murs. Nous travaillons <strong>en relation directe avec les compagnies d'assurances</strong> pour simplifier vos démarches.</p>
        <p>Particulier, professionnel ou assureur&nbsp;: contactez-nous pour programmer un rendez-vous et échanger sur votre situation.</p>
        <a class="btn btn--primary" href="/renovation-apres-sinistre">Rénovation après sinistre %(arrow)s</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="kicker">Ils nous font confiance</p>
      <h2>Nos clients recommandent notre travail</h2>
      <p>Retrouvez les avis laissés par nos clients sur notre fiche Google et faites-vous votre propre idée.</p>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:1.4rem" class="reveal" data-delay="1">
      <div class="review__stars" style="transform:scale(1.6)" aria-label="Note moyenne sur Google">%(stars)s</div>
      <a class="btn btn--ghost" href="%(google)s" target="_blank" rel="noopener">Lire nos avis Google %(arrow)s</a>
    </div>
    <div class="partners reveal" data-delay="2" style="margin-top:4.5rem">
      <img src="/assets/img/logo-gerflor.png" alt="Gerflor, partenaire revêtements de sol" loading="lazy" width="160" height="52">
      <img src="/assets/img/logo-zolpan.png" alt="Zolpan, partenaire peintures professionnelles" loading="lazy" width="160" height="52">
      <img src="/assets/img/logo-pointp.png" alt="Point P, partenaire matériaux de construction" loading="lazy" width="160" height="52">
    </div>
  </div>
</section>

<section class="section section--tight section--white">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Zone d'intervention</p>
      <h2>Nous intervenons à Valence et dans ses alentours</h2>
    </div>
    <ul class="zones reveal" data-delay="1">
      <li>%(pin)s Valence</li>
      <li>%(pin)s <a href="/guilherand-granges">Guilherand-Granges</a></li>
      <li>%(pin)s Bourg-lès-Valence</li>
      <li>%(pin)s Portes-lès-Valence</li>
      <li>%(pin)s Saint-Péray</li>
      <li>%(pin)s Drôme (26)</li>
      <li>%(pin)s Ardèche (07)</li>
    </ul>
  </div>
</section>

%(faq)s
%(cta)s
""" % {
    "brush_style": brush("avec style"),
    "brush_maitrise": brush("maîtrisé"),
    "cards": home_cards_html,
    "arrow": ARROW, "check": CHECK, "phone": PHONE, "pin": icon("pin"),
    "shield": icon("shield"), "users": icon("users"),
    "stars": STAR * 5, "google": SITE["google"],
    "tel": SITE["tel"], "tel_link": SITE["tel_link"],
    "faq": faq_block([
        ("Quels types de travaux de rénovation réalisez-vous à Valence ?",
         "Nous prenons en charge la rénovation intérieure complète : plâtrerie, isolation par l'intérieur, peinture, papier peint, pose de carrelage, parquet et sols souples, rénovation de salle de bains et remise en état après sinistre. Un seul interlocuteur coordonne l'ensemble des corps de métier."),
        ("Le devis est-il vraiment gratuit ?",
         "Oui, tous nos devis sont gratuits et sans engagement. Nous nous déplaçons pour étudier la faisabilité de votre projet, vous conseiller sur les matériaux et vous remettre un chiffrage détaillé et transparent."),
        ("Êtes-vous couverts par une garantie décennale ?",
         "Oui. Rénov'Solèmur dispose de la garantie décennale : notre responsabilité est engagée pendant dix ans après l'achèvement des travaux, pour tous les dommages pouvant compromettre la solidité de l'ouvrage."),
        ("Dans quelles communes intervenez-vous ?",
         "Nous intervenons à Valence et dans ses alentours : Guilherand-Granges, Bourg-lès-Valence, Portes-lès-Valence, Saint-Péray, et plus largement en Drôme et en Ardèche."),
    ], title="Vos questions sur la rénovation intérieure"),
    "cta": cta_band("Votre projet mérite un artisan de confiance", "Et si on en parlait autour d'un café ?"),
}

# ============================================================== À PROPOS
APROPOS_BODY = page_hero({
    "crumb": "L'entreprise",
    "h1": "Rénov'Solèmur&nbsp;: entreprise de rénovation à Valence, à votre service depuis plus de 10&nbsp;ans",
    "lead": "Particuliers, professionnels et collectivités : confiez vos travaux de rénovation intérieure à une équipe d'artisans qualifiés qui transforme maisons, appartements et locaux professionnels en espaces fonctionnels et esthétiques.",
    "hero_img": "/assets/img/equipe-renovation-valence-2.jpg",
    "hero_alt": "Salle de bains sous combles entièrement rénovée — une réalisation Rénov'Solèmur",
    "illu": "illustration-artisan.png",
}) + """
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split__media reveal reveal--left">
        <span class="split__sticker">Depuis 2012&nbsp;!</span>
        <img src="/assets/img/chantier-renovation-en-cours.jpg" alt="Chantier de rénovation intérieure en cours, mené par Rénov'Solèmur" loading="lazy" width="700" height="560">
      </div>
      <div class="split__text reveal reveal--right">
        <p class="kicker">Notre histoire</p>
        <h2>Depuis 2012, notre entreprise rénove vos intérieurs à Valence</h2>
        <p>Fondée en 2012, Rénov'Solèmur a accumulé <strong>plus d'une décennie d'expérience</strong> dans la rénovation intérieure de maisons, d'appartements et de locaux professionnels. Reconnus pour notre savoir-faire, nous coordonnons tous les corps de métier nécessaires à votre chantier&nbsp;: plâtrerie, isolation, peinture, revêtements, salle de bains.</p>
        <p>Chez Rénov'Solèmur, chaque projet est une nouvelle création, un défi à relever <strong>avec passion et professionnalisme</strong>. Nous prenons aussi en charge les rénovations après sinistre, avec une remise en état complète, du sol au plafond.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="split split--reverse">
      <div class="split__media reveal reveal--right">
        <img src="/assets/img/contact-renovation-valence.jpg" alt="Grand volume à rénover : l'étude de faisabilité commence ici" loading="lazy" width="700" height="560">
      </div>
      <div class="split__text reveal reveal--left">
        <p class="kicker">Notre accompagnement</p>
        <h2>Étude de faisabilité, devis gratuit et conseils personnalisés</h2>
        <p>Nous vous accompagnons <strong>du premier rendez-vous jusqu'au parfait achèvement des travaux</strong>. Étude de faisabilité, conseils sur les matériaux, les revêtements, l'isolation et les aménagements&nbsp;: tout est pensé pour faciliter vos choix.</p>
        <ul class="checklist">
          <li>%(check)s<div><strong>Écoute attentive de vos besoins</strong><span>La satisfaction client est notre leitmotiv depuis le premier jour.</span></div></li>
          <li>%(check)s<div><strong>Devis gratuits et détaillés</strong><span>Pour prendre les meilleures décisions, en toute transparence.</span></div></li>
          <li>%(check)s<div><strong>Qualité, délais, budget</strong><span>Un travail soigné, dans le respect du planning et du budget convenus.</span></div></li>
        </ul>
        <a class="btn btn--primary" href="/contact">Parler de mon projet %(arrow)s</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="container">
    <div class="split">
      <div class="split__text reveal reveal--left">
      <p class="kicker">Votre sécurité</p>
      <h2>Garantie décennale&nbsp;: une protection pour tous vos travaux</h2>
      <p>L'entreprise Rénov'Solèmur dispose de la <strong>garantie décennale</strong>, quel que soit votre projet. Cette garantie engage notre responsabilité pendant <strong>dix ans après l'achèvement des travaux</strong>&nbsp;: elle couvre tous les dommages qui pourraient compromettre la solidité de votre bâtiment ou le rendre inadapté à son usage.</p>
      <p>Cuisine, salle de bains, revêtements, isolation&nbsp;: chaque chantier est réalisé avec le plus grand soin — et vous êtes protégé dans la durée.</p>
      </div>
      <div class="reveal reveal--right">
        <img src="/assets/img/equipe-renovation-valence-1.jpg" alt="Garantie décennale : vos travaux de rénovation couverts pendant 10 ans" loading="lazy" width="700" height="560" style="border-radius:var(--radius-lg);box-shadow:var(--shadow-lg);aspect-ratio:4/3.2;object-fit:cover">
      </div>
    </div>
    <div class="stats" style="margin-top:4rem">
      <div class="stat reveal"><span class="num" data-count="10">10</span><span class="lbl">Ans de garantie</span></div>
      <div class="stat reveal" data-delay="1"><span class="num" data-count="100" data-suffix="%%">100%%</span><span class="lbl">Chantiers couverts</span></div>
      <div class="stat reveal" data-delay="2"><span class="num" data-count="2012">2012</span><span class="lbl">Année de création</span></div>
      <div class="stat reveal" data-delay="3"><span class="num" data-count="1">1</span><span class="lbl">Interlocuteur unique</span></div>
    </div>
  </div>
</section>
""" % {"check": CHECK, "arrow": ARROW} + faq_block([
    ("Qui est Rénov'Solèmur ?",
     "Rénov'Solèmur est une entreprise de rénovation intérieure fondée en 2012 à Valence. Nous rénovons maisons, appartements et locaux professionnels en coordonnant tous les corps de métier : plâtrerie, isolation, peinture, sols, salle de bains."),
    ("Travaillez-vous avec les professionnels et les collectivités ?",
     "Oui. Nous accompagnons les particuliers, les professionnels et les collectivités, du petit rafraîchissement à la rénovation complète d'un local ou d'un bâtiment."),
    ("Comment se déroule un projet avec vous ?",
     "Premier échange, visite sur place, devis gratuit et détaillé, puis réalisation des travaux par nos artisans qualifiés avec un planning clair. Nous restons votre interlocuteur unique du début à la fin."),
], title="Mieux nous connaître") + cta_band("Confiez vos travaux à une équipe passionnée", "Plus de 10 ans à vos côtés")

# ============================================================== CONTACT
CONTACT_BODY = page_hero({
    "crumb": "Contact",
    "h1": "Prenez contact avec Rénov'Solèmur, entreprise de rénovation située à Valence",
    "lead": "Une question, un projet, besoin d'un devis ? Appelez-nous ou écrivez-nous via le formulaire : nous vous répondons dans les plus brefs délais.",
    "hero_img": "/assets/img/contact-renovation-valence.jpg",
    "hero_alt": "Grand volume lumineux prêt à être rénové : parlons de votre projet",
    "illu": "illustration-renovation-1.png",
}) + """
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="reveal reveal--left">
        <p class="kicker">Nos coordonnées</p>
        <h2 style="margin-bottom:1.6rem">Parlons de votre projet</h2>
        <div class="contact-info">
          <div class="contact-info__item">
            <span class="ic">%(phone)s</span>
            <div><strong>Par téléphone</strong><a href="tel:%(tel_link)s">%(tel)s</a><p class="form__hint">Du lundi au vendredi</p></div>
          </div>
          <div class="contact-info__item">
            <span class="ic">%(mail)s</span>
            <div><strong>Par email</strong><a href="mailto:%(email)s">%(email)s</a><p class="form__hint">Réponse rapide garantie</p></div>
          </div>
          <div class="contact-info__item">
            <span class="ic">%(pin)s</span>
            <div><strong>Notre adresse</strong><span>%(address)s</span><p class="form__hint">Intervention à Valence et alentours, Drôme &amp; Ardèche</p></div>
          </div>
          <div class="contact-info__item">
            <span class="ic">%(star)s</span>
            <div><strong>Nos avis clients</strong><a href="%(google)s" target="_blank" rel="noopener">Consulter notre fiche Google</a></div>
          </div>
        </div>
      </div>
      <div class="reveal reveal--right" data-delay="1">
        <form class="form" id="devis-form" novalidate>
          <h2 style="font-size:1.5rem;margin-bottom:0.4rem">Demande de devis gratuit</h2>
          <p class="form__hint" style="margin-bottom:1.4rem">Décrivez votre projet : nous revenons vers vous rapidement avec une réponse claire.</p>
          <div class="form__row">
            <div class="form__group">
              <label for="f-nom">Nom et prénom <span class="req" aria-hidden="true">*</span></label>
              <input id="f-nom" name="nom" type="text" autocomplete="name" required>
            </div>
            <div class="form__group">
              <label for="f-tel">Téléphone <span class="req" aria-hidden="true">*</span></label>
              <input id="f-tel" name="tel" type="tel" autocomplete="tel" required>
            </div>
          </div>
          <div class="form__row">
            <div class="form__group">
              <label for="f-email">Email <span class="req" aria-hidden="true">*</span></label>
              <input id="f-email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="form__group">
              <label for="f-ville">Ville du chantier</label>
              <input id="f-ville" name="ville" type="text" autocomplete="address-level2" placeholder="Valence, Guilherand-Granges…">
            </div>
          </div>
          <div class="form__group">
            <label for="f-projet">Votre projet</label>
            <select id="f-projet" name="projet">
              <option value="">— Choisissez une prestation —</option>
              <option>Plâtrerie</option>
              <option>Isolation intérieure</option>
              <option>Peinture intérieure</option>
              <option>Papier peint</option>
              <option>Carrelage</option>
              <option>Parquet</option>
              <option>Sol souple (PVC, lino…)</option>
              <option>Rénovation de salle de bains</option>
              <option>Rénovation après sinistre</option>
              <option>Rénovation complète</option>
              <option>Autre</option>
            </select>
          </div>
          <div class="form__group">
            <label for="f-message">Votre message <span class="req" aria-hidden="true">*</span></label>
            <textarea id="f-message" name="message" required placeholder="Décrivez votre projet : type de travaux, surface, délais souhaités…"></textarea>
            <p class="form__hint">Plus votre description est précise, plus notre réponse sera rapide et juste.</p>
          </div>
          <button class="btn btn--primary" type="submit" style="width:100%%;justify-content:center">Envoyer ma demande %(arrow)s</button>
          <p id="form-success" hidden tabindex="-1" style="margin-top:1rem;color:var(--success);font-weight:600">Votre messagerie va s'ouvrir avec votre demande pré-remplie. Merci&nbsp;!</p>
          <p class="form__note">* Champs obligatoires. Vos données ne sont utilisées que pour répondre à votre demande.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight section--paper">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Zone d'intervention</p>
      <h2>Où intervenons-nous&nbsp;?</h2>
    </div>
    <ul class="zones reveal" data-delay="1">
      <li>%(pin)s Valence</li>
      <li>%(pin)s <a href="/guilherand-granges">Guilherand-Granges</a></li>
      <li>%(pin)s Bourg-lès-Valence</li>
      <li>%(pin)s Portes-lès-Valence</li>
      <li>%(pin)s Saint-Péray</li>
      <li>%(pin)s Drôme (26)</li>
      <li>%(pin)s Ardèche (07)</li>
    </ul>
  </div>
</section>
""" % {
    "phone": PHONE, "mail": icon("mail"), "pin": icon("pin"), "star": STAR,
    "arrow": ARROW, "tel": SITE["tel"], "tel_link": SITE["tel_link"],
    "email": SITE["email"], "address": SITE["address"], "google": SITE["google"],
}

# ====================================================== GUILHERAND-GRANGES
GG_BODY = page_hero({
    "crumb": "Guilherand-Granges",
    "h1": "Rénov'Solèmur&nbsp;: entreprise de rénovation intérieure à Guilherand-Granges",
    "lead": "Artisan local installé à Valence, juste de l'autre côté du Rhône, nous réalisons vos projets de rénovation intérieure à Guilherand-Granges : plâtrerie, peinture, pose de sols et salle de bains. Devis gratuit !",
    "hero_img": "/assets/img/renovation-guilherand-granges-1.jpg",
    "hero_alt": "Menuiseries intérieures et portes posées lors d'une rénovation à Guilherand-Granges",
    "illu": "illustration-artisan.png",
}) + """
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split__media reveal reveal--left">
        <img src="/assets/img/renovation-guilherand-granges-2.jpg" alt="Intérieur rénové à Guilherand-Granges par l'entreprise Rénov'Solèmur" loading="lazy" width="700" height="560">
      </div>
      <div class="split__text reveal reveal--right">
        <p class="kicker">Artisan local</p>
        <h2>Un artisan qualifié, à cinq minutes de chez vous</h2>
        <p>Installés à Valence, nous intervenons quotidiennement à <strong>Guilherand-Granges</strong> et dans les communes voisines d'Ardèche. Cette proximité, c'est l'assurance d'une <strong>réactivité réelle</strong>&nbsp;: visite rapide, suivi régulier du chantier et interventions sans frais de déplacement excessifs.</p>
        <p>Maison, appartement ou local professionnel&nbsp;: nous coordonnons tous les corps de métier pour rénover votre intérieur du sol au plafond, avec la même exigence de qualité depuis 2012.</p>
        <a class="btn btn--primary" href="/contact">Demander un devis gratuit %(arrow)s</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Nos prestations à Guilherand-Granges</p>
      <h2>Tous vos travaux de rénovation intérieure</h2>
    </div>
    <div class="steps" style="grid-template-columns:repeat(3,1fr)">
      <div class="step reveal"><h3>Plâtrerie &amp; isolation</h3><p>Cloisons sèches, plafonds, faux plafonds et isolation thermique par l'intérieur pour un confort durable.</p></div>
      <div class="step reveal" data-delay="1"><h3>Peinture &amp; murs</h3><p>Peintures toutes finitions, papier peint et revêtements muraux pour transformer vos pièces.</p></div>
      <div class="step reveal" data-delay="2"><h3>Sols &amp; salle de bains</h3><p>Carrelage, parquet, sols souples et rénovation complète de salle de bains, clés en main.</p></div>
    </div>
  </div>
</section>
""" % {"arrow": ARROW} + faq_block([
    ("Intervenez-vous vraiment à Guilherand-Granges ?",
     "Oui, Guilherand-Granges fait partie de notre zone d'intervention quotidienne : la commune est à quelques minutes de notre siège de Valence, de l'autre côté du Rhône."),
    ("Le déplacement pour le devis est-il facturé ?",
     "Non. La visite et le devis sont entièrement gratuits à Guilherand-Granges comme dans toute notre zone d'intervention."),
    ("Quels travaux réalisez-vous à Guilherand-Granges ?",
     "Tous nos métiers : plâtrerie, isolation intérieure, peinture, papier peint, carrelage, parquet, sols souples, rénovation de salle de bains et remise en état après sinistre."),
], title="Vos questions, côté Ardèche") + cta_band("Un projet à Guilherand-Granges ?", "On traverse le Rhône pour vous !")

# ====================================================== MENTIONS LÉGALES
MENTIONS_BODY = """
<section class="page-hero">
  <div class="container" style="grid-template-columns:1fr">
    <div>
      <nav class="breadcrumb" aria-label="Fil d'Ariane"><a href="/">Accueil</a>%(chevron)s<span>Mentions légales</span></nav>
      <h1>Mentions légales de Rénov'Solèmur, entreprise de rénovation à Valence</h1>
    </div>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:820px">
    <h2>Éditeur du site</h2>
    <p>Le site <strong>www.renov-solemur.com</strong> est édité par l'entreprise <strong>Rénov'Solèmur</strong>, entreprise de rénovation intérieure.</p>
    <ul class="checklist" style="margin-block:1.2rem 2.2rem">
      <li>%(check)s<div><strong>Adresse</strong><span>%(address)s</span></div></li>
      <li>%(check)s<div><strong>Téléphone</strong><span>%(tel)s</span></div></li>
      <li>%(check)s<div><strong>Email</strong><span>%(email)s</span></div></li>
    </ul>
    <h2>Hébergement</h2>
    <p style="margin-block:0.8rem 2.2rem">Les informations relatives à l'hébergeur du site sont disponibles sur demande auprès de l'éditeur.</p>
    <h2>Propriété intellectuelle</h2>
    <p style="margin-block:0.8rem 2.2rem">L'ensemble des contenus présents sur ce site (textes, photographies, logo, éléments graphiques) est la propriété de Rénov'Solèmur ou de ses partenaires. Toute reproduction, totale ou partielle, sans autorisation préalable est interdite.</p>
    <h2>Données personnelles &amp; confidentialité</h2>
    <p style="margin-block:0.8rem 1rem">Les informations transmises via le formulaire de contact (nom, téléphone, email, message) sont utilisées uniquement pour répondre à votre demande. Elles ne sont ni cédées ni revendues à des tiers.</p>
    <p style="margin-block:0 2.2rem">Conformément au Règlement général sur la protection des données (RGPD), vous disposez d'un droit d'accès, de rectification et de suppression de vos données. Pour l'exercer, contactez-nous à l'adresse <a href="mailto:%(email)s">%(email)s</a>.</p>
    <h2>Cookies</h2>
    <p style="margin-block:0.8rem 0">Ce site n'utilise pas de cookies de suivi publicitaire. Seuls des cookies techniques strictement nécessaires à son fonctionnement peuvent être déposés.</p>
  </div>
</section>
""" % {"chevron": icon("chevron"), "check": CHECK, "address": SITE["address"],
       "tel": SITE["tel"], "email": SITE["email"]}

# ------------------------------------------------------------------- export
CORE_PAGES = [
    {
        "slug": "index",
        "title": "Rénov'Solémur - Rénovation intérieure à Valence - Modernisation",
        "desc": "Entreprise de rénovation intérieure à Valence depuis 2012 : plâtrerie, isolation, peinture, sols, salle de bains. Garantie décennale, devis gratuit. ☎ 06 63 06 65 17.",
        "hero_img": "/assets/img/artisan-renovation-valence.jpg",
        "body": HOME_BODY,
        "schemas": [schema_faq([
            ("Quels types de travaux de rénovation réalisez-vous à Valence ?",
             "Rénovation intérieure complète : plâtrerie, isolation par l'intérieur, peinture, papier peint, carrelage, parquet, sols souples, salle de bains et remise en état après sinistre."),
            ("Le devis est-il vraiment gratuit ?",
             "Oui, tous nos devis sont gratuits et sans engagement, avec étude de faisabilité et conseils matériaux."),
            ("Êtes-vous couverts par une garantie décennale ?",
             "Oui, Rénov'Solèmur dispose de la garantie décennale couvrant les travaux pendant dix ans après leur achèvement."),
            ("Dans quelles communes intervenez-vous ?",
             "Valence, Guilherand-Granges, Bourg-lès-Valence, Portes-lès-Valence, Saint-Péray et plus largement la Drôme et l'Ardèche."),
        ])],
    },
    {
        "slug": "a-propos",
        "title": "Rénov'Solémur - Entreprise de rénovation à Valence",
        "desc": "Fondée en 2012 à Valence, Rénov'Solèmur rénove maisons, appartements et locaux professionnels. Artisans qualifiés, garantie décennale, devis gratuit.",
        "crumb": "L'entreprise",
        "hero_img": "/assets/img/equipe-renovation-valence-2.jpg",
        "hero_alt": "Salle de bains sous combles entièrement rénovée — une réalisation Rénov'Solèmur",
        "body": APROPOS_BODY,
        "schemas": [schema_breadcrumb([("Accueil", "/"), ("L'entreprise", "/a-propos")])],
    },
    {
        "slug": "contact",
        "title": "Contactez Rénov'Solémur - Entreprise de rénovation à Valence",
        "desc": "Contactez Rénov'Solèmur au 06 63 06 65 17 ou via notre formulaire pour votre devis gratuit de rénovation intérieure à Valence et alentours.",
        "crumb": "Contact",
        "hero_img": "/assets/img/contact-renovation-valence.jpg",
        "hero_alt": "Échange entre un artisan Rénov'Solèmur et un client autour d'un projet de rénovation",
        "body": CONTACT_BODY,
        "schemas": [schema_breadcrumb([("Accueil", "/"), ("Contact", "/contact")])],
    },
    {
        "slug": "guilherand-granges",
        "title": "Rénovation intérieure, Guilherand‑Granges | Artisan qualifié",
        "desc": "Rénovation intérieure à Guilherand-Granges par un artisan local : plâtrerie, peinture, pose de sols, salle de bains. Visite et devis gratuits, sans frais de déplacement.",
        "crumb": "Guilherand-Granges",
        "hero_img": "/assets/img/renovation-guilherand-granges-1.jpg",
        "hero_alt": "Travaux de rénovation intérieure réalisés à Guilherand-Granges en Ardèche",
        "body": GG_BODY,
        "schemas": [schema_breadcrumb([("Accueil", "/"), ("Guilherand-Granges", "/guilherand-granges")])],
    },
    {
        "slug": "mentions-legales",
        "title": "Mentions légales du site internet renov-solemur.com",
        "desc": "Mentions légales et politique de confidentialité du site de Rénov'Solèmur, entreprise de rénovation intérieure à Valence.",
        "robots": "noindex, follow",
        "hero_img": "/assets/img/renovation-interieure-valence-hero.jpg",
        "body": MENTIONS_BODY,
    },
]
