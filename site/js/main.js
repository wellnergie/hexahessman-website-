/* WELLNERGIE — site scripts */
(function () {
  "use strict";

  /* ---------- Header: transparent over hero, solid on scroll ---------- */
  const header = document.querySelector(".site-header");
  const hasHero = document.body.classList.contains("has-hero");
  function onScroll() {
    if (!header) return;
    const y = window.scrollY || document.documentElement.scrollTop;
    header.classList.toggle("is-solid", y > 40);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Mobile drawer ---------- */
  const drawer = document.querySelector(".nav-drawer");
  const toggle = document.querySelector(".menu-toggle");
  const close = document.querySelector(".drawer-close");
  if (drawer && toggle) {
    toggle.addEventListener("click", () => { drawer.classList.add("is-open"); document.body.style.overflow = "hidden"; });
    const shut = () => { drawer.classList.remove("is-open"); document.body.style.overflow = ""; };
    close && close.addEventListener("click", shut);
    drawer.querySelectorAll("a").forEach(a => a.addEventListener("click", shut));
  }

  /* ---------- Hero slider ---------- */
  const hero = document.querySelector(".hero");
  if (hero) {
    const slides = Array.from(hero.querySelectorAll(".slide"));
    const dots = Array.from(hero.querySelectorAll(".hero-dots button"));
    const prev = hero.querySelector(".hero-prev");
    const next = hero.querySelector(".hero-next");
    const INTERVAL = 6500;
    let i = 0, timer = null;

    function go(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, k) => s.classList.toggle("is-active", k === i));
      dots.forEach((d, k) => d.classList.toggle("is-active", k === i));
    }
    function start() { stop(); timer = setInterval(() => go(i + 1), INTERVAL); }
    function stop() { if (timer) clearInterval(timer); timer = null; }

    dots.forEach((d, k) => d.addEventListener("click", () => { go(k); start(); }));
    prev && prev.addEventListener("click", () => { go(i - 1); start(); });
    next && next.addEventListener("click", () => { go(i + 1); start(); });
    hero.addEventListener("mouseenter", stop);
    hero.addEventListener("mouseleave", start);

    // touch swipe
    let x0 = null;
    hero.addEventListener("touchstart", e => { x0 = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener("touchend", e => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) { go(dx < 0 ? i + 1 : i - 1); start(); }
      x0 = null;
    });
    document.addEventListener("keydown", e => {
      if (e.key === "ArrowLeft") { go(i - 1); start(); }
      if (e.key === "ArrowRight") { go(i + 1); start(); }
    });
    if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) start();
    go(0);
  }

  /* ---------- Reveal on scroll ---------- */
  /* Motion setup: mark what animates and in which order */
  const ANIM = ["anim-child", "anim-title", "anim-side", "from-left", "from-right"];
  function prep(el, d) {
    if (getComputedStyle(el).display === "inline") el.style.display = "inline-block";
    el.classList.add("anim-child");
    if (/^H[1-4]$/.test(el.tagName)) el.classList.add("anim-title");
    el.style.setProperty("--d", d);
  }
  const stagger = (els, start) => Array.from(els).forEach((el, k) => prep(el, (start || 0) + k));
  const all = (root, sel) => root.querySelectorAll(sel);

  // Centered statements and section headings: words rise in one after another
  all(document, ".statement.reveal, .statement .reveal, .info-blocks.reveal, .vm.reveal").forEach(g => { g.classList.add("reveal-group"); stagger(g.children); });
  all(document, ".section-head.reveal").forEach(g => { g.classList.add("reveal-group"); stagger(all(g, ":scope > div > *, :scope > a")); });
  // Photo + words: photo from one side, words from the other
  all(document, ".split.reveal").forEach(g => {
    g.classList.add("reveal-group");
    const rev = g.classList.contains("reverse");
    const media = g.querySelector(".split-media"), body = g.querySelector(".split-body");
    if (media) media.classList.add("anim-side", rev ? "from-right" : "from-left");
    if (body) { body.classList.add("anim-side", rev ? "from-left" : "from-right"); stagger(body.children, 2); }
  });
  // Dark callout: box fades up, then its words and list items follow
  all(document, ".wave-callout.reveal").forEach(g => stagger(all(g, ":scope > div > *, :scope > ul > li"), 2));
  // Card grids: queue in from the left, column by column
  all(document, ".grid, .materials, .values, .t-grid").forEach(grid => {
    const cols = Math.max(1, getComputedStyle(grid).gridTemplateColumns.split(" ").length);
    Array.from(grid.children).filter(c => c.classList.contains("reveal")).forEach((c, k) => { c.classList.add("anim-queue"); c.style.setProperty("--d", k % cols); });
  });
  // Page titles on inner pages animate as soon as the page opens
  all(document, ".page-head .wrap").forEach(w => { stagger(w.children); requestAnimationFrame(() => requestAnimationFrame(() => w.classList.add("is-in"))); setTimeout(() => cleanup(w), 3200); });

  // Once an element has finished animating, drop the helpers so hover effects behave normally
  function cleanup(t) {
    [t].concat(Array.from(all(t, ".anim-child, .anim-side"))).forEach(e => { e.classList.remove.apply(e.classList, ANIM.concat("anim-queue")); e.style.removeProperty("--d"); });
  }

  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      en.target.classList.add("is-in"); io.unobserve(en.target);
      setTimeout(() => cleanup(en.target), 3400);
    });
  }, { threshold: 0.12 });
  document.querySelectorAll(".reveal").forEach(el => io.observe(el));

  /* Preloader: release the hero once it has played */
  if (document.body.classList.contains("has-preloader")) {
    setTimeout(() => { const p = document.querySelector(".preloader"); p && p.remove(); }, 3200);
    setTimeout(() => document.body.classList.add("pl-done"), 5200);
  }

  /* ---------- Shop filters ---------- */
  const chips = document.querySelectorAll(".chips button");
  const cards = document.querySelectorAll("[data-cat]");
  chips.forEach(c => c.addEventListener("click", () => {
    chips.forEach(x => x.classList.remove("is-active"));
    c.classList.add("is-active");
    const f = c.dataset.filter;
    cards.forEach(card => { card.style.display = (f === "all" || card.dataset.cat === f) ? "" : "none"; });
  }));

  /* ---------- Product gallery ---------- */
  const main = document.querySelector(".gallery-main img");
  const thumbs = Array.from(document.querySelectorAll(".gallery-thumbs button"));
  const showThumb = k => {
    if (!thumbs.length) return;
    k = (k + thumbs.length) % thumbs.length;
    thumbs.forEach((x, n) => x.classList.toggle("is-active", n === k));
    main.src = thumbs[k].dataset.src;
    thumbs[k].scrollIntoView({ block: "nearest", inline: "nearest" });
  };
  const curThumb = () => thumbs.findIndex(x => x.classList.contains("is-active"));
  thumbs.forEach((t, k) => t.addEventListener("click", () => showThumb(k)));
  const gPrev = document.querySelector(".g-prev"), gNext = document.querySelector(".g-next");
  gPrev && gPrev.addEventListener("click", e => { e.preventDefault(); showThumb(curThumb() - 1); });
  gNext && gNext.addEventListener("click", e => { e.preventDefault(); showThumb(curThumb() + 1); });

  /* ---------- Product card hover slideshow ---------- */
  document.querySelectorAll(".product-card[data-images]").forEach(card => {
    const srcs = card.dataset.images.split("|");
    if (srcs.length < 2) return;
    const img = card.querySelector(".thumb img");
    const dots = Array.from(card.querySelectorAll(".dots i"));
    let k = 0, timer = null, loaded = false;
    const show = n => {
      k = (n + srcs.length) % srcs.length;
      img.classList.add("fade");
      setTimeout(() => { img.src = srcs[k]; img.classList.remove("fade"); }, 180);
      dots.forEach((d, i) => d.classList.toggle("on", i === k));
    };
    card.addEventListener("mouseenter", () => {
      if (!loaded) { srcs.forEach(s => { const p = new Image(); p.src = s; }); loaded = true; }
      timer = setInterval(() => show(k + 1), 1100);
      show(k + 1);
    });
    card.addEventListener("mouseleave", () => { clearInterval(timer); timer = null; show(0); });
  });

  /* ---------- Product tabs ---------- */
  document.querySelectorAll(".tabs").forEach(t => {
    const btns = t.querySelectorAll(".tab-bar button"), panels = t.querySelectorAll(".tab-panel");
    btns.forEach(b => b.addEventListener("click", () => {
      btns.forEach(x => x.classList.remove("is-active")); panels.forEach(x => x.classList.remove("is-active"));
      b.classList.add("is-active"); t.querySelector("#" + b.dataset.tab).classList.add("is-active");
    }));
  });

  /* ---------- Product options + quantity ---------- */
  document.querySelectorAll(".swatches").forEach(group => {
    group.querySelectorAll(".swatch").forEach(s => s.addEventListener("click", () => {
      group.querySelectorAll(".swatch").forEach(x => x.classList.remove("is-active"));
      s.classList.add("is-active");
      const img = s.dataset.img;
      if (img && main) {
        const k = thumbs.findIndex(x => x.dataset.src === img);
        if (k >= 0) showThumb(k); else main.src = img;
      }
    }));
  });
  const qty = document.querySelector(".qty input");
  document.querySelectorAll(".qty button").forEach(b => b.addEventListener("click", () => {
    const v = Math.max(1, (parseInt(qty.value, 10) || 1) + (b.dataset.dir === "up" ? 1 : -1));
    qty.value = v;
  }));

  /* ---------- FAQ tabs ---------- */
  const tabs = document.querySelectorAll(".faq-tabs button");
  const panels = document.querySelectorAll(".faq-panel");
  tabs.forEach(t => t.addEventListener("click", () => {
    tabs.forEach(x => x.classList.remove("is-active"));
    panels.forEach(p => p.classList.remove("is-active"));
    t.classList.add("is-active");
    document.getElementById(t.dataset.panel).classList.add("is-active");
  }));

  /* ---------- Contact form → email client ---------- */
  const form = document.querySelector("form.form");
  if (form) form.addEventListener("submit", e => {
    e.preventDefault();
    const f = new FormData(form);
    const body = ["Name: " + f.get("name"), "Contact Number: " + f.get("phone"), "Email: " + f.get("email"), "Reason: " + f.get("reason"), "", f.get("message")].join("\n");
    window.location.href = "mailto:wellnergie@gmail.com?subject=" + encodeURIComponent("Website enquiry — " + f.get("reason")) + "&body=" + encodeURIComponent(body);
  });

  /* ---------- Testimonial marquee: duplicate cards for a seamless loop ---------- */
  document.querySelectorAll("[data-marquee]").forEach(m => {
    const track = m.querySelector(".marquee-track");
    const cards = Array.from(track.children);
    cards.forEach(c => { const d = c.cloneNode(true); d.setAttribute("aria-hidden", "true"); d.tabIndex = -1; track.appendChild(d); });
    track.style.setProperty("--marquee-duration", (cards.length * 7) + "s");
  });

  /* ---------- Video lightbox ---------- */
  const lb = document.querySelector(".lightbox");
  if (lb) {
    const frame = lb.querySelector(".lightbox-frame");
    const open = id => {
      frame.innerHTML = '<iframe src="https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0" title="Testimonial video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
      lb.hidden = false; document.body.style.overflow = "hidden";
    };
    const shut = () => { lb.hidden = true; frame.innerHTML = ""; document.body.style.overflow = ""; };
    document.querySelectorAll("[data-video]").forEach(a => a.addEventListener("click", e => { e.preventDefault(); open(a.dataset.video); }));
    lb.querySelector(".lightbox-close").addEventListener("click", shut);
    lb.addEventListener("click", e => { if (e.target === lb) shut(); });
    document.addEventListener("keydown", e => { if (e.key === "Escape" && !lb.hidden) shut(); });
  }

  /* ---------- Newsletter (placeholder) ---------- */
  const nl = document.querySelector(".newsletter");
  if (nl) nl.addEventListener("submit", e => {
    e.preventDefault();
    nl.innerHTML = '<p style="color:var(--gold-soft)">Thanks for submitting!</p>';
  });
})();
