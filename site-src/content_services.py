# -*- coding: utf-8 -*-
"""Les 11 pages prestations."""
from build import (SITE, icon, cta_band, faq_block, page_hero, other_services,
                   schema_breadcrumb, schema_service, schema_faq)

ARROW = icon("arrow")
CHECK = icon("check")


def split_section(kicker, title, paras, img, alt, reverse=False, checklist=None,
                  btn=None, paper=False, sticker=None):
    check_html = ""
    if checklist:
        items = "\n".join(
            "<li>%s<div><strong>%s</strong><span>%s</span></div></li>" % (CHECK, t, s)
            for t, s in checklist)
        check_html = '<ul class="checklist">%s</ul>' % items
    btn_html = ""
    if btn:
        label, href = btn
        btn_html = '<a class="btn btn--primary" href="%s">%s %s</a>' % (href, label, ARROW)
    sticker_html = '<span class="split__sticker">%s</span>' % sticker if sticker else ""
    paras_html = "\n".join("<p>%s</p>" % p for p in paras)
    return """<section class="section%s">
  <div class="container">
    <div class="split%s">
      <div class="split__media reveal %s">
        %s<img src="/assets/img/%s" alt="%s" loading="lazy" width="700" height="560">
      </div>
      <div class="split__text reveal %s">
        <p class="kicker">%s</p>
        <h2>%s</h2>
        %s
        %s
        %s
      </div>
    </div>
  </div>
</section>""" % (" section--paper" if paper else "",
                 " split--reverse" if reverse else "",
                 "reveal--right" if reverse else "reveal--left",
                 sticker_html, img, alt,
                 "reveal--left" if reverse else "reveal--right",
                 kicker, title, paras_html, check_html, btn_html)


def steps_section(kicker, title, steps, ink=False, cols=None):
    cols_style = ' style="grid-template-columns:repeat(%d,1fr)"' % cols if cols else ""
    steps_html = "\n".join(
        '<div class="step reveal"%s><h3>%s</h3><p>%s</p></div>'
        % (' data-delay="%d"' % i if i else "", t, d)
        for i, (t, d) in enumerate(steps))
    return """<section class="section%s">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">%s</p>
      <h2>%s</h2>
    </div>
    <div class="steps"%s>%s</div>
  </div>
</section>""" % (" section--ink" if ink else "", kicker, title, cols_style, steps_html)


def ba_section(before_img, before_alt, after_img, after_alt, title="Avant / Après : jugez par vous-même"):
    return """<section class="section section--paper">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <p class="kicker">Nos réalisations</p>
      <h2>%s</h2>
      <p>Faites glisser le curseur pour comparer — une réalisation Rénov'Solèmur.</p>
    </div>
    <div class="ba reveal reveal--zoom" style="max-width:880px;margin-inline:auto">
      <img src="/assets/img/%s" alt="%s" loading="lazy" width="880" height="550">
      <img class="ba__after" src="/assets/img/%s" alt="%s" loading="lazy" width="880" height="550">
      <span class="ba__label ba__label--avant">Avant</span>
      <span class="ba__label ba__label--apres">Après</span>
      <div class="ba__handle"></div>
    </div>
  </div>
</section>""" % (title, before_img, before_alt, after_img, after_alt)


ILLUS = {
    "platrerie": "illustration-platrerie.png",
    "isolation-interieure": "illustration-platrerie.png",
    "revetements-muraux": "illustration-murs.png",
    "peinture": "illustration-murs.png",
    "papier-peint": "illustration-renovation-2.png",
    "revetements-sol": "illustration-sols.png",
    "carrelage": "illustration-sols.png",
    "parquet": "illustration-sols.png",
    "sol-souple": "illustration-sols.png",
    "renovation-salle-bains": "illustration-salle-bains.png",
    "renovation-apres-sinistre": "illustration-sinistre.png",
}


def svc(slug, title, desc, crumb, h1, lead, hero_img, hero_alt, *parts,
        crumbs=None, faq_title="Vos questions sur cette prestation"):
    # *parts : une ou plusieurs sections HTML, puis la liste FAQ en dernier
    faq_items = parts[-1]
    body_sections = "".join(parts[:-1])
    crumb_list = [("Accueil", "/")] + (crumbs or []) + [(crumb, "/" + slug)]
    body = page_hero({
        "crumb": crumb, "crumbs": crumbs or [], "h1": h1, "lead": lead,
        "hero_img": "/assets/img/" + hero_img, "hero_alt": hero_alt,
        "illu": ILLUS.get(slug),
    })
    body += body_sections
    body += faq_block(faq_items, title=faq_title)
    body += other_services([slug])
    body += cta_band()
    return {
        "slug": slug, "title": title, "desc": desc, "crumb": crumb,
        "hero_img": "/assets/img/" + hero_img, "hero_alt": hero_alt, "body": body,
        "schemas": [
            schema_breadcrumb(crumb_list),
            schema_service(crumb + " à Valence", desc, slug),
            schema_faq(faq_items),
        ],
    }


SERVICE_PAGES = []

# ------------------------------------------------------------- PLÂTRERIE
SERVICE_PAGES.append(svc(
    "platrerie",
    "Plâtrerie traditionnelle et rénovation d'intérieur à Valence",
    "Travaux de plâtrerie à Valence : cloisons sèches, plafonds, faux plafonds et enduits. Des finitions impeccables pour vos murs intérieurs. Devis gratuit.",
    "Plâtrerie",
    "Travaux de plâtrerie à Valence&nbsp;: des finitions impeccables pour vos murs intérieurs",
    "Cloisons sèches, plafonds, faux plafonds, enduits : la plâtrerie est la base de toute rénovation intérieure réussie. Nos plaquistes préparent des surfaces parfaitement lisses, prêtes à recevoir tous vos revêtements.",
    "platrerie-valence-1.jpg",
    "Plaquiste de Rénov'Solèmur réalisant des travaux de plâtrerie à Valence",
    split_section(
        "Cloisons & plafonds",
        "Cloisons sèches, plafonds et faux plafonds sur mesure",
        ["Les travaux de plâtrerie sont essentiels dans la rénovation intérieure : ils permettent de <strong>redistribuer les espaces</strong>, de créer de nouvelles pièces ou d'intégrer un faux plafond avec éclairage encastré.",
         "Nos artisans réalisent des surfaces <strong>parfaitement lisses et homogènes</strong>, prêtes à accueillir peinture, papier peint ou tout autre revêtement mural."],
        "platrerie-valence-2.jpg",
        "Pose de plaques de plâtre pour une cloison sèche dans une maison à Valence",
        checklist=[
            ("Cloisons sèches et distribution", "Création ou suppression de cloisons pour repenser vos espaces."),
            ("Plafonds et faux plafonds", "Pose soignée, intégration d'éclairages et correction acoustique."),
            ("Enduits et bandes", "Finitions lisses, sans reprise visible, prêtes à peindre."),
        ]),
    steps_section("Notre savoir-faire", "Une plâtrerie pensée pour la suite de votre chantier", [
        ("Diagnostic des supports", "Nous évaluons l'état des murs et plafonds existants avant toute intervention."),
        ("Mise en œuvre propre", "Chantier protégé, découpes précises, poussière maîtrisée."),
        ("Finitions impeccables", "Bandes, enduits et ponçage : un support prêt à peindre."),
        ("Coordination des métiers", "La plâtrerie s'enchaîne sans accroc avec l'isolation, la peinture et les sols."),
    ], ink=True),
    split_section(
        "Rénovation complète",
        "La première étape de votre rénovation intérieure",
        ["Associée à l'<a href='/isolation-interieure'>isolation par l'intérieur</a>, la plâtrerie améliore aussi le <strong>confort thermique et acoustique</strong> de votre logement.",
         "Et parce qu'un mur neuf appelle une belle finition, nos équipes enchaînent avec la <a href='/peinture'>peinture</a> ou la pose de <a href='/papier-peint'>papier peint</a> — un seul interlocuteur, du squelette à la décoration."],
        "renovation-guilherand-granges-1.jpg",
        "Mur en plaques de plâtre terminé, prêt à recevoir sa peinture de finition",
        reverse=True, paper=False,
        btn=("Demander un devis plâtrerie", "/contact")),
    [
        ("Quels travaux de plâtrerie réalisez-vous ?",
         "Cloisons sèches, doublages, plafonds et faux plafonds, enduits et bandes, correction de murs abîmés. Nous intervenons en rénovation comme en aménagement."),
        ("Peut-on créer une nouvelle pièce avec des cloisons sèches ?",
         "Oui, la cloison sèche est la solution idéale pour redistribuer un espace : rapide à mettre en œuvre, propre, et compatible avec une isolation acoustique intégrée."),
        ("Vos plâtreries sont-elles prêtes à peindre ?",
         "Oui. Bandes, enduits et ponçage sont inclus pour livrer des surfaces parfaitement lisses, prêtes à recevoir peinture ou papier peint."),
    ],
    faq_title="Vos questions sur la plâtrerie"))

# ------------------------------------------------------------- ISOLATION
SERVICE_PAGES.append(svc(
    "isolation-interieure",
    "Isolation par l'intérieur à Valence - Confort thermique",
    "Isolation thermique par l'intérieur (ITI) à Valence : murs, plafonds, combles, en laine minérale ou naturelle. Améliorez votre confort et économisez l'énergie.",
    "Isolation intérieure",
    "Isolation par l'intérieur à Valence&nbsp;: économisez de l'énergie et améliorez votre confort",
    "Murs froids, factures qui grimpent ? L'isolation thermique par l'intérieur (ITI) en laine minérale ou naturelle améliore durablement le confort de votre logement, été comme hiver.",
    "isolation-interieure-valence-1.jpg",
    "Pose d'isolation thermique par l'intérieur en laine minérale à Valence",
    split_section(
        "Isolation thermique (ITI)",
        "Murs, plafonds et combles : une isolation complète",
        ["Notre entreprise réalise vos travaux d'<strong>isolation thermique par l'intérieur</strong> : murs, plafonds, combles perdus et aménagés. En <strong>laine minérale ou naturelle</strong>, selon votre projet et votre budget.",
         "Une bonne isolation, c'est moins de déperditions de chaleur, un logement plus agréable et des <strong>économies d'énergie immédiates</strong> sur vos factures."],
        "isolation-interieure-valence-2.jpg",
        "Isolation des combles en laine minérale posée par Rénov'Solèmur",
        checklist=[
            ("Murs et doublages isolants", "Suppression de l'effet paroi froide, confort immédiat."),
            ("Plafonds et combles", "Jusqu'à 30 % des pertes de chaleur passent par le toit."),
            ("Laine minérale ou naturelle", "Des matériaux adaptés à votre logement et vos priorités."),
        ]),
    steps_section("Pourquoi isoler ?", "Les bénéfices concrets d'une isolation intérieure", [
        ("Économies d'énergie", "Réduisez vos besoins de chauffage et vos factures, dès le premier hiver."),
        ("Confort été comme hiver", "Une température homogène dans toutes les pièces, toute l'année."),
        ("Confort acoustique", "L'isolation atténue aussi les bruits extérieurs et entre pièces."),
        ("Valeur du bien", "Un logement bien isolé gagne en classe énergétique et en valeur."),
    ], ink=True),
    split_section(
        "Un chantier coordonné",
        "Isolation + plâtrerie + finitions : tout est enchaîné",
        ["L'isolation par l'intérieur va de pair avec la <a href='/platrerie'>plâtrerie</a> : doublage des murs, pose des plaques, bandes et enduits sont réalisés par la même équipe.",
         "Résultat : un chantier plus court, sans coordination à gérer de votre côté, et des murs prêts à recevoir leur <a href='/peinture'>peinture de finition</a>."],
        "isolation-interieure-valence-3.jpg",
        "Doublage isolant des murs avant pose des plaques de plâtre",
        reverse=True,
        btn=("Demander un devis isolation", "/contact")),
    [
        ("Quelle isolation choisir : laine minérale ou naturelle ?",
         "Les deux sont efficaces. La laine minérale offre un excellent rapport performance/prix ; les laines naturelles séduisent par leur confort d'été et leur bilan environnemental. Nous vous conseillons selon votre logement et votre budget."),
        ("L'isolation par l'intérieur fait-elle perdre beaucoup de surface ?",
         "La perte est limitée : quelques centimètres par mur isolé. Nous optimisons l'épaisseur pour concilier performance thermique et surface habitable."),
        ("Isolez-vous aussi les combles ?",
         "Oui, combles perdus comme aménagés. C'est souvent le poste le plus rentable : une grande partie des déperditions de chaleur passe par le toit."),
    ],
    faq_title="Vos questions sur l'isolation"))

# ------------------------------------------------- REVÊTEMENTS MURAUX (hub)
MURAUX_CARDS = """<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Nos solutions murales</p>
      <h2>Peinture, papier peint&nbsp;: à chaque mur sa personnalité</h2>
    </div>
    <div class="cards" style="grid-template-columns:repeat(2,1fr)">
      <article class="card reveal">
        <div class="card__media"><span class="card__tag">Toutes finitions</span><img src="/assets/img/peinture-interieure-valence-1.jpg" alt="Application de peinture intérieure satinée sur un mur à Valence" loading="lazy" width="640" height="400"></div>
        <div class="card__body">
          <h3>Peinture intérieure</h3>
          <p>Mat, satin, brillant, laqué : toutes les finitions, appliquées sur des supports soigneusement préparés.</p>
          <a class="card__link card__cover" href="/peinture">Découvrir la peinture %(arrow)s</a>
        </div>
      </article>
      <article class="card reveal" data-delay="1">
        <div class="card__media"><span class="card__tag">Déco unique</span><img src="/assets/img/pose-papier-peint-valence-1.jpg" alt="Pose de papier peint décoratif dans un salon à Valence" loading="lazy" width="640" height="400"></div>
        <div class="card__body">
          <h3>Papier peint</h3>
          <p>Intissé, vinyle, panoramique : une pose précise et sans bulles pour une décoration tendance.</p>
          <a class="card__link card__cover" href="/papier-peint">Découvrir le papier peint %(arrow)s</a>
        </div>
      </article>
    </div>
  </div>
</section>""" % {"arrow": ARROW}

SERVICE_PAGES.append(svc(
    "revetements-muraux",
    "Pose de revêtements muraux à Valence et ses alentours",
    "Revêtements muraux à Valence : peinture toutes finitions, papier peint, toile de verre. Préparation des supports et pose soignée par des artisans qualifiés.",
    "Revêtements muraux",
    "Revêtements muraux à Valence&nbsp;: embellissez vos espaces intérieurs",
    "Peinture, papier peint, toile de verre : vos murs donnent le ton de votre intérieur. Nos artisans préparent chaque support et posent vos revêtements muraux avec une précision d'orfèvre.",
    "revetement-mural-valence-1.jpg",
    "Pose de revêtement mural décoratif dans un intérieur rénové à Valence",
    MURAUX_CARDS + split_section(
        "Préparation des supports",
        "Un mur bien préparé, c'est 80&nbsp;% du résultat",
        ["Avant toute mise en peinture ou pose de papier peint, nos équipes <strong>préparent minutieusement chaque surface</strong> : rebouchage, ponçage, sous-couche. C'est ce travail invisible qui garantit un rendu impeccable et durable.",
         "Murs abîmés ? Nos compétences en <a href='/platrerie'>plâtrerie</a> permettent de repartir d'une surface parfaitement saine."],
        "revetement-mural-valence-2.jpg",
        "Préparation d'un mur avant pose de revêtement : rebouchage et ponçage",
        paper=True, reverse=True,
        checklist=[
            ("Diagnostic du support", "Chaque mur est inspecté avant de choisir la solution adaptée."),
            ("Préparation complète", "Rebouchage, ponçage, sous-couche : rien n'est laissé au hasard."),
            ("Conseils déco personnalisés", "Couleurs, matières, tendances : nous vous guidons dans vos choix."),
        ],
        btn=("Demander un devis", "/contact")),
    [
        ("Quels revêtements muraux posez-vous ?",
         "Peinture (toutes finitions), papier peint intissé ou vinyle, toile de verre et revêtements décoratifs. Nous vous conseillons selon la pièce, l'usage et le style recherché."),
        ("Pouvez-vous rénover des murs en mauvais état ?",
         "Oui. Grâce à notre savoir-faire en plâtrerie, nous remettons les supports en état (rebouchage, enduits, ponçage) avant la pose du revêtement final."),
        ("Aidez-vous au choix des couleurs et matières ?",
         "Bien sûr : nous mettons à votre disposition des nuanciers et vous conseillons selon la luminosité, le volume de la pièce et vos goûts."),
    ],
    faq_title="Vos questions sur les revêtements muraux"))

# ------------------------------------------------------------- PEINTURE
SERVICE_PAGES.append(svc(
    "peinture",
    "Peinture intérieure à Valence - Réalisation soignée",
    "Peinture intérieure à Valence : mat, satin, brillant, laqué. Préparation des supports, application soignée par nos peintres en bâtiment. Devis gratuit.",
    "Peinture intérieure",
    "Des peintures intérieures durables et esthétiques à Valence pour rénover votre intérieur",
    "Mat, satiné, brillant, laqué… Nos peintres en bâtiment appliquent tout type de peinture pour rénover vos murs et plafonds, avec une préparation des supports digne de ce nom.",
    "peinture-interieure-valence-1.jpg",
    "Peintre en bâtiment appliquant une peinture intérieure au rouleau à Valence",
    steps_section("Toutes les finitions", "Mat, satin, brillant, laqué : un large choix de finitions", [
        ("Peinture mate", "Élégance et sobriété : elle masque les petits défauts et apaise les volumes."),
        ("Peinture satinée", "Résistante aux taches et lessivable, avec un léger reflet chaleureux."),
        ("Peinture brillante", "Relief et profondeur : elle capte la lumière et agrandit les pièces."),
        ("Peinture laquée", "L'effet verni haut de gamme, pour un maximum de luminosité."),
    ]),
    [
        ("Quelle finition de peinture choisir pour quelle pièce ?",
         "Le mat convient aux plafonds et pièces de vie, le satin aux pièces de passage et chambres d'enfants (lessivable), le brillant et le laqué aux boiseries et pièces à mettre en valeur. Nous vous conseillons pièce par pièce."),
        ("Préparez-vous les murs avant de peindre ?",
         "Toujours. Nettoyage, rebouchage, ponçage et sous-couche font partie de notre prestation : c'est la condition d'un résultat uniforme et durable."),
        ("Proposez-vous des conseils couleurs ?",
         "Oui, nous mettons à votre disposition des nuanciers et vous guidons selon la luminosité et l'ambiance recherchée, pour un intérieur qui vous ressemble."),
    ],
    crumbs=[("Revêtements muraux", "/revetements-muraux")],
    faq_title="Vos questions sur la peinture") | {})
# Sections additionnelles peinture (insérées après coup pour garder l'ordre)
_p = SERVICE_PAGES[-1]
_extra = split_section(
    "Préparation & application",
    "Du ponçage à la dernière couche, on s'occupe de tout",
    ["Nos peintres prennent en charge le <strong>rafraîchissement complet de vos murs et plafonds</strong> : nettoyage, ponçage, apprêt des surfaces puis application en couches régulières.",
     "L'objectif : un résultat <strong>parfait et uniforme</strong>, avec une adhérence durable de la peinture — y compris sur plafonds anciens ou supports délicats."],
    "plafond-renove-peinture.jpg",
    "Plafond rénové et repeint en blanc par les peintres de Rénov'Solèmur",
    paper=True,
    checklist=[
        ("Protection du chantier", "Sols et meubles bâchés, chantier rendu propre chaque soir."),
        ("Supports apprêtés", "Nettoyage, ponçage, sous-couche : l'assurance d'une tenue parfaite."),
        ("Peintures de qualité", "Nous travaillons avec des gammes professionnelles, dont Zolpan."),
    ]) + split_section(
    "Peintures décoratives",
    "Des teintes et des nuances pour un intérieur unique",
    ["Envie d'un mur d'accent, d'une ambiance sobre pour vos locaux professionnels ou d'une touche de modernité dans le salon ? Nos peintres vous accompagnent dans <strong>le choix des couleurs et des effets</strong>.",
     "Nuanciers à l'appui, nous concrétisons vos envies de décoration — en cohérence avec vos <a href='/revetements-sol'>sols</a> et votre mobilier."],
    "peinture-interieure-valence-2.jpg",
    "Choix de teintes décoratives sur nuancier pour une peinture intérieure",
    reverse=True,
    btn=("Demander un devis peinture", "/contact"))
_p["body"] = _p["body"].replace('<section class="section section--paper">\n  <div class="container">\n    <div class="section-head section-head--center reveal">', _extra + '<section class="section section--paper">\n  <div class="container">\n    <div class="section-head section-head--center reveal">', 1)

# ----------------------------------------------------------- PAPIER PEINT
SERVICE_PAGES.append(svc(
    "papier-peint",
    "Pose de papier peint à Valence - Réalisation soignée",
    "Pose de papier peint à Valence : intissé, vinyle, panoramique. Une pose précise, sans bulles ni raccords visibles, pour une décoration unique et tendance.",
    "Papier peint",
    "Pose de papier peint à Valence pour transformer et embellir votre intérieur",
    "Intissé, vinyle, panoramique : le papier peint fait son grand retour dans la décoration. Nos poseurs garantissent des raccords invisibles et une finition sans bulles, lé après lé.",
    "pose-papier-peint-valence-1.jpg",
    "Pose soignée de papier peint décoratif par Rénov'Solèmur à Valence",
    split_section(
        "Pose professionnelle",
        "Des raccords invisibles, une pose qui dure",
        ["La pose de papier peint ne s'improvise pas : <strong>préparation du support, traçage, encollage adapté et marouflage soigné</strong> font toute la différence entre une pose amateur et un résultat professionnel.",
         "Nos artisans maîtrisent tous les types de papiers peints : <strong>intissé, vinyle, expansé, panoramique</strong> — y compris les motifs à raccords complexes."],
        "pose-papier-peint-valence-2.jpg",
        "Marouflage d'un lé de papier peint pour une pose sans bulles",
        checklist=[
            ("Supports préparés", "Murs rebouchés, poncés et encollés selon le type de papier."),
            ("Raccords parfaits", "Motifs alignés au millimètre, lés invisibles."),
            ("Conseils déco", "Tendances, motifs, panoramiques : nous vous guidons."),
        ]),
    split_section(
        "Décoration tendance",
        "Un mur d'accent qui change tout",
        ["Un seul pan de mur en papier peint panoramique suffit à <strong>transformer l'ambiance d'une pièce</strong> : tête de lit, salon, entrée ou bureau.",
         "Associé à une <a href='/peinture'>peinture</a> coordonnée sur les autres murs, le résultat est spectaculaire — et entièrement réalisé par la même équipe."],
        "pose-papier-peint-valence-3.jpg",
        "Mur d'accent en papier peint panoramique dans un intérieur moderne",
        reverse=True, paper=True,
        btn=("Demander un devis papier peint", "/contact")),
    [
        ("Quels types de papier peint posez-vous ?",
         "Tous : intissé (le plus courant et le plus résistant), vinyle, expansé, papiers panoramiques et décors muraux. Nous vous conseillons selon la pièce et l'effet recherché."),
        ("Le papier peint tient-il dans une pièce humide ?",
         "Certains papiers vinyles supportent les pièces humides comme la cuisine. Pour la salle de bains, nous vous orientons vers les revêtements les plus adaptés au cas par cas."),
        ("Faut-il retirer l'ancien papier peint avant la pose ?",
         "Oui dans la plupart des cas : nous décollons l'ancien revêtement et préparons le mur (rebouchage, ponçage) pour garantir une pose durable et sans défaut."),
    ],
    crumbs=[("Revêtements muraux", "/revetements-muraux")],
    faq_title="Vos questions sur le papier peint"))

# ---------------------------------------------------- REVÊTEMENTS SOL (hub)
SOL_CARDS = """<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="kicker">Nos solutions de sols</p>
      <h2>Carrelage, parquet, sols souples&nbsp;: à chaque pièce son sol</h2>
      <p>Vous souhaitez remplacer un vieux carrelage par du parquet&nbsp;? Avec Rénov'Solèmur, c'est possible. Nous proposons un large choix de revêtements et assurons une pose dans les règles de l'art.</p>
    </div>
    <div class="cards">
      <article class="card reveal">
        <div class="card__media"><span class="card__tag">Solide & esthétique</span><img src="/assets/img/pose-carrelage-valence-1.jpg" alt="Pose de carrelage grand format dans une pièce de vie à Valence" loading="lazy" width="640" height="400"></div>
        <div class="card__body">
          <h3>Carrelage</h3>
          <p>Grès cérame, faïence, grands formats : un revêtement durable pour sols et murs.</p>
          <a class="card__link card__cover" href="/carrelage">Découvrir le carrelage %(arrow)s</a>
        </div>
      </article>
      <article class="card reveal" data-delay="1">
        <div class="card__media"><span class="card__tag">Chaleureux & naturel</span><img src="/assets/img/pose-parquet-valence-1.jpg" alt="Pose de parquet en bois dans un salon à Valence" loading="lazy" width="640" height="400"></div>
        <div class="card__body">
          <h3>Parquet</h3>
          <p>Flottant ou bois massif, pose et rénovation (ponçage, vitrification) de vos parquets.</p>
          <a class="card__link card__cover" href="/parquet">Découvrir le parquet %(arrow)s</a>
        </div>
      </article>
      <article class="card reveal" data-delay="2">
        <div class="card__media"><span class="card__tag">Pratique & économique</span><img src="/assets/img/pose-sol-souple-valence-1.jpg" alt="Pose de sol souple en PVC imitation bois à Valence" loading="lazy" width="640" height="400"></div>
        <div class="card__body">
          <h3>Sols souples</h3>
          <p>PVC, lino, moquette, jonc de mer : des solutions confortables et faciles d'entretien.</p>
          <a class="card__link card__cover" href="/sol-souple">Découvrir les sols souples %(arrow)s</a>
        </div>
      </article>
    </div>
  </div>
</section>""" % {"arrow": ARROW}

SERVICE_PAGES.append(svc(
    "revetements-sol",
    "Pose de revêtements de sol à Valence et ses alentours",
    "Pose de revêtements de sol à Valence : carrelage, parquet, PVC, lino, moquette. Préparation des supports et pose professionnelle pour un rendu impeccable.",
    "Revêtements de sol",
    "Revêtements de sol à Valence&nbsp;: un choix esthétique et durable pour votre intérieur",
    "Carrelage, parquet, moquette ou lino : le sol structure toute la décoration d'une pièce. Nous vous aidons à choisir le bon revêtement et assurons une pose professionnelle, pour un rendu impeccable qui dure.",
    "revetement-sol-valence-1.jpg",
    "Pose d'un revêtement de sol moderne dans un intérieur rénové à Valence",
    SOL_CARDS + ba_section(
        "salle-bains-pose-placo.jpg",
        "Pièce en cours de rénovation avant la pose du nouveau revêtement de sol",
        "parquet-apres-ponctage.jpg",
        "Parquet rénové, poncé et vitrifié par Rénov'Solèmur",
        title="Du chantier brut au sol fini") + split_section(
        "Préparation des sols",
        "Ragréage, dépose, préparation : la base d'un sol durable",
        ["Un beau sol commence par un <strong>support propre et plan</strong>. Nos équipes assurent la dépose de l'ancien revêtement, le ragréage et la préparation complète avant toute pose.",
         "Nous travaillons avec des matériaux de qualité professionnelle, notamment les gammes <strong>Gerflor</strong> pour les sols souples."],
        "sol-cuisine-apres-vitrification.jpg",
        "Sol de cuisine après rénovation et vitrification, prêt à vivre",
        reverse=True,
        btn=("Demander un devis sols", "/contact")),
    [
        ("Quel revêtement de sol choisir ?",
         "Tout dépend de la pièce : carrelage pour les pièces humides et passages intensifs, parquet pour le cachet des pièces de vie, sols souples pour le confort et le budget. Nous vous conseillons gratuitement lors de la visite."),
        ("Peut-on poser un nouveau sol sur l'ancien ?",
         "Parfois oui (PVC sur carrelage par exemple), parfois non. Nous évaluons le support existant et incluons la dépose et le ragréage au devis si nécessaire."),
        ("Rénovez-vous les parquets anciens ?",
         "Oui : ponçage, réparation des lames et vitrification redonnent une seconde vie à un parquet ancien, souvent pour moins cher qu'un remplacement."),
    ],
    faq_title="Vos questions sur les sols"))

# ------------------------------------------------------------- CARRELAGE
SERVICE_PAGES.append(svc(
    "carrelage",
    "Pose de carrelage à Valence - Finitions impeccables",
    "Pose de carrelage à Valence : sols et murs, grès cérame, faïence, grands formats. Un revêtement solide et esthétique posé par des carreleurs qualifiés.",
    "Carrelage",
    "Pose de carrelage à Valence pour un revêtement solide et esthétique",
    "Résistant, facile d'entretien et infiniment déclinable, le carrelage reste la valeur sûre des sols et murs intérieurs. Nos carreleurs assurent une pose au cordeau, joints compris.",
    "pose-carrelage-valence-1.jpg",
    "Carreleur posant du carrelage au sol avec croisillons à Valence",
    split_section(
        "Sols & murs",
        "Du grès cérame à la faïence, tous les formats",
        ["Grès cérame, faïence, carreaux de ciment, <strong>grands formats contemporains</strong> ou mosaïque : nous posons tous les types de carrelage, au sol comme au mur.",
         "Cuisine, salle de bains, pièce de vie ou local professionnel : le carrelage allie <strong>résistance, facilité d'entretien et esthétique</strong>, pour des années."],
        "pose-carrelage-valence-2.jpg",
        "Pose de faïence murale dans une salle de bains rénovée",
        checklist=[
            ("Pose droite, diagonale ou décalée", "Le calepinage est étudié avec vous avant la pose."),
            ("Découpes précises", "Angles, contours et finitions réalisés avec un outillage professionnel."),
            ("Joints soignés", "Couleur et largeur de joints choisies pour sublimer le carreau."),
        ]),
    steps_section("Notre méthode", "Une pose de carrelage dans les règles de l'art", [
        ("Préparation du support", "Dépose éventuelle, ragréage et planéité contrôlée avant toute pose."),
        ("Calepinage", "Sens de pose, point de départ, raccords : tout est défini à l'avance."),
        ("Pose et découpes", "Double encollage si nécessaire, croisillons, découpes nettes."),
        ("Joints et finitions", "Jointoiement soigné et nettoyage complet du chantier."),
    ], ink=True),
    split_section(
        "Et pourquoi pas ?",
        "Remplacer un vieux carrelage par du parquet",
        ["Votre carrelage a fait son temps ? Nous assurons la <strong>dépose complète</strong> et la pose du nouveau revêtement de votre choix : carrelage neuf, <a href='/parquet'>parquet</a> ou <a href='/sol-souple'>sol souple</a>.",
         "Un seul devis, une seule équipe, et un sol transformé du tout au tout."],
        "pose-carrelage-valence-3.jpg",
        "Carrelage imitation bois posé dans une pièce de vie lumineuse",
        reverse=True, paper=True,
        btn=("Demander un devis carrelage", "/contact")),
    [
        ("Posez-vous du carrelage grand format ?",
         "Oui, y compris les formats XXL (60×120 et plus) qui demandent un support parfaitement plan et un double encollage : c'est notre spécialité."),
        ("Le carrelage convient-il à une salle de bains ?",
         "C'est même le revêtement idéal : étanche, résistant et facile d'entretien. Associé à notre prestation de rénovation de salle de bains, le résultat est garanti."),
        ("Combien de temps dure un chantier de carrelage ?",
         "Selon la surface et la préparation nécessaire, comptez de quelques jours à une semaine. Le délai exact figure sur votre devis gratuit."),
    ],
    crumbs=[("Revêtements de sol", "/revetements-sol")],
    faq_title="Vos questions sur le carrelage"))

# --------------------------------------------------------------- PARQUET
SERVICE_PAGES.append(svc(
    "parquet",
    "Pose de parquet flottant et en bois massif à Valence",
    "Pose de parquet à Valence : flottant, contrecollé ou bois massif. Rénovation, ponçage et vitrification de parquets anciens. Un sol chaleureux et durable.",
    "Parquet",
    "Pose de parquet à Valence pour un sol durable, chaleureux et naturel",
    "Rien ne remplace la chaleur du bois sous les pieds. Parquet flottant, contrecollé ou massif : nous posons et rénovons vos parquets pour un sol authentique qui traverse les années.",
    "pose-parquet-valence-1.jpg",
    "Pose de parquet en bois naturel dans une pièce de vie à Valence",
    split_section(
        "Pose de parquet",
        "Flottant, contrecollé ou massif : à chaque projet son parquet",
        ["Le <strong>parquet flottant</strong> offre un excellent rapport qualité/prix et une pose rapide. Le <strong>contrecollé</strong> combine vraie couche de bois noble et stabilité. Le <strong>massif</strong>, lui, est le choix du caractère et de la longévité.",
         "Chêne, essences claires ou foncées, pose droite ou à bâtons rompus : nous vous guidons vers le parquet qui correspond à votre pièce et à votre budget."],
        "sol-cuisine-apres-vitrification.jpg",
        "Parquet vitrifié dans une cuisine rénovée par Rénov'Solèmur",
        checklist=[
            ("Sous-couche adaptée", "Confort acoustique et protection contre l'humidité."),
            ("Pose soignée", "Sens de pose étudié, plinthes et seuils assortis."),
            ("Finition au choix", "Brut, huilé ou vitrifié selon l'usage de la pièce."),
        ]),
    ba_section(
        "chantier-avant-renovation.jpg",
        "Sol ancien avant la rénovation du parquet",
        "parquet-apres-ponctage.jpg",
        "Le même parquet après ponçage et vitrification par Rénov'Solèmur",
        title="Rénovation de parquet : avant / après"),
    [
        ("Vaut-il mieux rénover ou remplacer un parquet ancien ?",
         "Si les lames sont saines, le ponçage suivi d'une vitrification redonne un aspect neuf pour un coût souvent inférieur au remplacement. Nous évaluons l'état du parquet lors de la visite gratuite."),
        ("Peut-on poser du parquet dans une cuisine ?",
         "Oui, avec une essence et une finition adaptées (vitrification résistante). Pour les pièces d'eau, nous vous orientons vers des solutions compatibles avec l'humidité."),
        ("Quelle différence entre parquet flottant et contrecollé ?",
         "Le flottant désigne le mode de pose (non collé au support). Le contrecollé est un type de parquet avec une couche d'usure en bois noble : il peut se poser flottant et se poncer comme un massif."),
    ],
    crumbs=[("Revêtements de sol", "/revetements-sol")],
    faq_title="Vos questions sur le parquet"))
# Section rénovation parquet additionnelle
_pq = SERVICE_PAGES[-1]
_pq_extra = split_section(
    "Rénovation de parquet",
    "Ponçage et vitrification : offrez une seconde vie à votre parquet",
    ["Un parquet terni, rayé ou grisé n'est pas un parquet perdu. Nos artisans le <strong>poncent, réparent les lames abîmées puis le vitrifient</strong> pour un résultat comme neuf.",
     "La vitrification protège le bois pour de longues années et facilite l'entretien au quotidien — la preuve en images ci-dessous."],
    "parquet-apres-ponctage.jpg",
    "Parquet ancien rénové : ponçage et vitrification réalisés à Valence",
    reverse=True, paper=True,
    btn=("Demander un devis parquet", "/contact"))
_pq["body"] = _pq["body"].replace('<section class="section section--paper">\n  <div class="container">\n    <div class="section-head section-head--center reveal">\n      <p class="kicker">Nos réalisations</p>', _pq_extra + '<section class="section section--paper">\n  <div class="container">\n    <div class="section-head section-head--center reveal">\n      <p class="kicker">Nos réalisations</p>', 1)

# ------------------------------------------------------------ SOL SOUPLE
SERVICE_PAGES.append(svc(
    "sol-souple",
    "Pose de sol en PVC à Valence - Installation et rénovation",
    "Pose de sol souple à Valence : PVC, lino, moquette, jonc de mer. Économique, confortable et moderne, posé par des professionnels. Devis gratuit.",
    "Sols souples",
    "Pose de sol en PVC, lino, moquette et jonc de mer à Valence",
    "Économiques, confortables et bluffants d'imitation, les sols souples ont tout bon. Lames PVC effet bois, lino, moquette ou jonc de mer : nous posons le revêtement adapté à chaque pièce.",
    "pose-sol-souple-valence-1.jpg",
    "Pose de lames de sol PVC imitation bois dans un appartement à Valence",
    split_section(
        "PVC & vinyle",
        "Des sols PVC qui imitent (vraiment) le bois et le carrelage",
        ["Lames et dalles <strong>PVC clipsables ou collées</strong>, rouleaux vinyles : les sols souples d'aujourd'hui imitent le parquet et le carrelage à s'y méprendre, pour un budget maîtrisé.",
         "<strong>Résistants à l'eau</strong>, silencieux et faciles d'entretien, ils sont parfaits pour les cuisines, chambres, locaux professionnels et locations. Nous posons notamment les gammes <strong>Gerflor</strong>."],
        "pose-sol-souple-valence-2.jpg",
        "Sol vinyle moderne posé dans une cuisine rénovée",
        checklist=[
            ("Pose collée ou clipsée", "Selon le support, l'usage et la pièce concernée."),
            ("Support préparé", "Ragréage inclus si nécessaire pour un rendu parfaitement plan."),
            ("Large choix de décors", "Effet bois, béton, carreaux de ciment : à vous de choisir."),
        ]),
    split_section(
        "Confort & nature",
        "Moquette et jonc de mer : le confort au naturel",
        ["Pour les chambres et les espaces cosy, la <strong>moquette</strong> apporte chaleur et silence. Le <strong>jonc de mer</strong>, fibre naturelle et résistante, donne du caractère aux pièces de vie.",
         "Chaque revêtement a ses atouts : nous vous aidons à choisir selon l'usage, l'entretien souhaité et votre budget."],
        "pose-sol-souple-valence-3.jpg",
        "Moquette confortable posée dans une chambre rénovée",
        reverse=True, paper=True,
        btn=("Demander un devis sol souple", "/contact")),
    [
        ("Le sol PVC est-il adapté aux pièces humides ?",
         "Oui, c'est l'un de ses grands atouts : le PVC résiste à l'eau et convient parfaitement aux cuisines et salles d'eau, avec une pose et des finitions adaptées."),
        ("Peut-on poser un sol souple sur un carrelage existant ?",
         "Dans la plupart des cas oui, après vérification de la planéité et un éventuel ragréage des joints. Cela évite la dépose et réduit le coût du chantier."),
        ("Quelle durée de vie pour un sol PVC ?",
         "Avec une pose professionnelle et une couche d'usure adaptée au trafic de la pièce, un sol PVC de qualité dure 15 à 25 ans."),
    ],
    crumbs=[("Revêtements de sol", "/revetements-sol")],
    faq_title="Vos questions sur les sols souples"))

# ------------------------------------------------------ SALLE DE BAINS
SERVICE_PAGES.append(svc(
    "renovation-salle-bains",
    "Rénovation de salle de bains à Valence - Transformation complète",
    "Rénovation de salle de bains à Valence : démontage, plomberie, douche, carrelage, finitions. Une transformation complète clés en main, y compris PMR.",
    "Salle de bains",
    "Rénovation de salle de bains à Valence pour une modernité et un confort renouvelés",
    "Du démontage des anciens équipements à la pose du dernier joint, nous rénovons votre salle de bains de A à Z : plomberie, douche, baignoire, meuble vasque, revêtements. Clés en main, vraiment.",
    "renovation-salle-bains-valence.jpg",
    "Douche accessible PMR avec barres d'appui et siège, aménagée par Rénov'Solèmur",
    steps_section("Clés en main", "Une rénovation complète, étape par étape", [
        ("Démontage", "Retrait des anciens équipements sanitaires et mise à nu des surfaces, pour repartir sur une base saine."),
        ("Plomberie & cloisons", "Reprise des réseaux, pose de cloisons et d'une étanchéité parfaite (SEL) sous les zones d'eau."),
        ("Équipements", "Installation et raccordement : douche, baignoire, WC, robinetterie, meuble vasque."),
        ("Finitions", "Carrelage, faïence, éclairage, montage des meubles : votre salle de bains est prête à vivre."),
    ]),
    [
        ("Combien de temps dure la rénovation d'une salle de bains ?",
         "Pour une rénovation complète, comptez généralement une à trois semaines selon la surface et les travaux de plomberie nécessaires. Le planning précis figure sur votre devis gratuit."),
        ("Peut-on remplacer une baignoire par une douche ?",
         "Oui, c'est l'une de nos demandes les plus fréquentes : dépose de la baignoire, reprise de l'étanchéité et pose d'une douche moderne, éventuellement à l'italienne."),
        ("Réalisez-vous des salles de bains PMR ?",
         "Oui : barres d'appui, sièges de douche, lavabos adaptés, revêtements antidérapants. Nos aménagements respectent les normes en vigueur pour une utilisation sécurisée et confortable."),
    ],
    faq_title="Vos questions sur la salle de bains"))
_sdb = SERVICE_PAGES[-1]
_sdb_extra = ba_section(
    "salle-bains-transformation.jpg",
    "Salle de bains en cours de transformation, avant les finitions",
    "salle-bains-apres-transformation.jpg",
    "La même salle de bains après sa rénovation complète par Rénov'Solèmur",
    title="Une vraie transformation : avant / après") + split_section(
    "Accessibilité PMR",
    "Une salle de bains accessible, sécurisée et confortable",
    ["Nous rendons les salles de bains accessibles à tous, et plus particulièrement aux <strong>personnes à mobilité réduite (PMR)</strong> : barres d'appui, sièges de douche, lavabos adaptés, revêtements antidérapants.",
     "Chaque aménagement respecte <strong>les normes en vigueur</strong>, avec une mise en œuvre rigoureuse, du sol au plafond."],
    "salle-bains-pose-placo.jpg",
    "Travaux de salle de bains : pose de placo et étanchéité avant carrelage",
    reverse=True, paper=True,
    btn=("Demander un devis salle de bains", "/contact"))
_sdb["body"] = _sdb["body"].replace('<section class="section section--paper">\n  <div class="container">\n    <div class="section-head section-head--center reveal">\n      <p class="kicker">Questions fréquentes</p>', _sdb_extra + '<section class="section section--paper">\n  <div class="container">\n    <div class="section-head section-head--center reveal">\n      <p class="kicker">Questions fréquentes</p>', 1)

# --------------------------------------------------------- APRÈS SINISTRE
SERVICE_PAGES.append(svc(
    "renovation-apres-sinistre",
    "Rénovation après sinistre à Valence - Intervention soignée",
    "Rénovation après sinistre à Valence : dégât des eaux, incendie. Remise en état complète en relation avec votre assurance. Intervention rapide et soignée.",
    "Après sinistre",
    "Rénovation après sinistre à Valence pour redonner vie à votre habitat",
    "Dégât des eaux, incendie : un sinistre bouleverse votre quotidien. Nos professionnels remettent votre logement en état, du sol au plafond, en relation directe avec votre compagnie d'assurance.",
    "renovation-apres-sinistre-1.jpg",
    "Remise en état d'un logement après un dégât des eaux à Valence",
    split_section(
        "Dégât des eaux & incendie",
        "Une remise en état complète, du sol au plafond",
        ["Après un <strong>dégât des eaux ou un incendie</strong>, nous réalisons tous les travaux de remise en état : <a href='/platrerie'>plâtrerie</a>, <a href='/isolation-interieure'>isolation</a>, <a href='/peinture'>peinture</a> et pose de revêtements pour les sols et les murs.",
         "Notre objectif : vous faire <strong>retrouver un habitat sûr et confortable</strong>, le plus rapidement possible, avec un seul interlocuteur pour l'ensemble du chantier."],
        "renovation-apres-sinistre-2.jpg",
        "Travaux de reprise des murs et plafonds après un sinistre",
        checklist=[
            ("Diagnostic complet", "Évaluation des dégâts visibles et cachés (humidité, supports)."),
            ("Tous corps de métier", "Plâtrerie, isolation, peinture, sols : une seule équipe coordonnée."),
            ("Remise à neuf durable", "Des matériaux sains et des finitions soignées, comme avant — en mieux."),
        ]),
    split_section(
        "Avec votre assurance",
        "Nous travaillons en relation directe avec les assureurs",
        ["Particulier, professionnel ou compagnie d'assurance : nous établissons des <strong>devis détaillés compatibles avec les expertises</strong> et échangeons directement avec votre assureur pour simplifier vos démarches.",
         "Contactez-nous dès maintenant pour programmer un rendez-vous et échanger sur votre situation : chaque jour compte après un sinistre."],
        "renovation-apres-sinistre-3.jpg",
        "Logement remis à neuf après des travaux de rénovation post-sinistre",
        reverse=True, paper=True,
        btn=("Décrire mon sinistre", "/contact")),
    [
        ("Intervenez-vous rapidement après un sinistre ?",
         "Oui, nous savons qu'un sinistre ne peut pas attendre : contactez-nous pour programmer un rendez-vous d'évaluation dans les meilleurs délais."),
        ("Travaillez-vous avec les compagnies d'assurance ?",
         "Oui, nous sommes en relation directe avec les assureurs : devis détaillés compatibles avec les expertises, échanges simplifiés, travaux conformes aux prises en charge."),
        ("Quels travaux réalisez-vous après un dégât des eaux ?",
         "Assèchement des supports, reprise de la plâtrerie et de l'isolation touchées, remise en peinture et remplacement des revêtements de sols et murs endommagés."),
    ],
    faq_title="Vos questions après un sinistre"))
