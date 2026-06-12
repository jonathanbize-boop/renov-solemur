/* Rénov'Solèmur — interactions & animations */
(function () {
  "use strict";

  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ----- Header sticky ----- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 30);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ----- Menu mobile ----- */
  var burger = document.querySelector(".burger");
  var menu = document.querySelector(".nav__menu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    // Sous-menus en mobile
    menu.querySelectorAll(".nav__list > li").forEach(function (li) {
      var link = li.querySelector(".nav__link");
      var dd = li.querySelector(".dropdown");
      if (link && dd) {
        link.addEventListener("click", function (e) {
          if (window.matchMedia("(max-width: 880px)").matches) {
            e.preventDefault();
            li.classList.toggle("is-open");
          }
        });
      }
    });
  }

  /* ----- Révélation au scroll (+ compteurs + pinceau) ----- */
  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        entry.target.querySelectorAll("[data-count]").forEach(animateCounter);
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.18, rootMargin: "0px 0px -40px 0px" }
  );
  document.querySelectorAll(".reveal, .brush").forEach(function (el) {
    io.observe(el);
  });

  function animateCounter(el) {
    if (el.dataset.done) return;
    el.dataset.done = "1";
    var target = parseInt(el.dataset.count, 10);
    var suffix = el.dataset.suffix || "";
    if (prefersReduced) {
      el.textContent = target + suffix;
      return;
    }
    var start = null;
    var dur = 1600;
    function tick(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  /* ----- Slider avant / après ----- */
  document.querySelectorAll(".ba").forEach(function (ba) {
    var after = ba.querySelector(".ba__after");
    var handle = ba.querySelector(".ba__handle");
    if (!after || !handle) return;

    function setPos(clientX) {
      var rect = ba.getBoundingClientRect();
      var x = Math.max(0, Math.min(clientX - rect.left, rect.width));
      var pct = (x / rect.width) * 100;
      after.style.clipPath = "inset(0 0 0 " + pct + "%)";
      handle.style.left = pct + "%";
    }
    function onMove(e) {
      setPos(e.touches ? e.touches[0].clientX : e.clientX);
    }
    ["mousedown", "touchstart"].forEach(function (evt) {
      ba.addEventListener(evt, function (e) {
        onMove(e);
        var moveEvt = e.type === "touchstart" ? "touchmove" : "mousemove";
        var endEvt = e.type === "touchstart" ? "touchend" : "mouseup";
        function stop() {
          window.removeEventListener(moveEvt, onMove);
          window.removeEventListener(endEvt, stop);
        }
        window.addEventListener(moveEvt, onMove, { passive: true });
        window.addEventListener(endEvt, stop);
      });
    });
    // Clavier
    handle.setAttribute("tabindex", "0");
    handle.setAttribute("role", "slider");
    handle.setAttribute("aria-label", "Comparer avant et après");
    handle.addEventListener("keydown", function (e) {
      var cur = parseFloat(handle.style.left || "50");
      if (e.key === "ArrowLeft") cur -= 4;
      else if (e.key === "ArrowRight") cur += 4;
      else return;
      e.preventDefault();
      cur = Math.max(0, Math.min(100, cur));
      after.style.clipPath = "inset(0 0 0 " + cur + "%)";
      handle.style.left = cur + "%";
    });
  });

  /* ----- Marquee : duplication de la piste ----- */
  document.querySelectorAll(".marquee__track").forEach(function (track) {
    track.appendChild(track.children[0].cloneNode(true));
  });

  /* ----- Formulaire contact (mailto enrichi) ----- */
  var form = document.getElementById("devis-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var sujet = "Demande de devis — " + (d.get("projet") || "rénovation intérieure");
      var corps =
        "Bonjour,\n\n" +
        "Nom : " + d.get("nom") + "\n" +
        "Téléphone : " + d.get("tel") + "\n" +
        "Email : " + d.get("email") + "\n" +
        "Ville : " + (d.get("ville") || "—") + "\n" +
        "Projet : " + (d.get("projet") || "—") + "\n\n" +
        "Message :\n" + d.get("message") + "\n";
      window.location.href =
        "mailto:renovsolemur@yahoo.fr?subject=" +
        encodeURIComponent(sujet) +
        "&body=" +
        encodeURIComponent(corps);
      var ok = document.getElementById("form-success");
      if (ok) {
        ok.hidden = false;
        ok.focus();
      }
    });
  }

  /* ----- Année courante ----- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
