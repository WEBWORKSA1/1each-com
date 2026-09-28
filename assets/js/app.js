/* 1Each.com — core interactions */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- Private contact routing (address never rendered) ---------- */
  function addr() { try { return atob(C._c).split("").reverse().join(""); } catch (e) { return ""; } }
  function endpoint() { return "https://formsubmit.co/ajax/" + (C.formAlias || addr()); }
  window.OneEach = window.OneEach || {};
  window.OneEach.mailto = function (subject) {
    window.location.href = "mailto:" + addr() + "?subject=" + encodeURIComponent(subject || "1Each inquiry");
  };
  $$("[data-mail]").forEach(function (a) {
    a.setAttribute("href", "contact.html");
    a.addEventListener("click", function (e) { e.preventDefault(); window.OneEach.mailto(a.getAttribute("data-mail")); });
  });

  /* ---------- Theme ---------- */
  var saved = store("theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  var tBtn = $("#theme-toggle");
  if (tBtn) tBtn.addEventListener("click", function () {
    var cur = document.documentElement.getAttribute("data-theme") ||
      (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next); store("theme", next);
  });

  /* ---------- Mobile menu ---------- */
  var mBtn = $("#menu-btn"), nav = $("#nav");
  if (mBtn && nav) mBtn.addEventListener("click", function () {
    var o = nav.classList.toggle("open"); mBtn.setAttribute("aria-expanded", o);
  });

  /* ---------- Toast ---------- */
  function toast(msg) {
    var t = $("#toast"); if (!t) return; t.textContent = msg; t.style.display = "block";
    clearTimeout(t._h); t._h = setTimeout(function () { t.style.display = "none"; }, 2600);
  }
  window.OneEach.toast = toast;

  /* ---------- Modals ---------- */
  function openModal(id) { var m = document.getElementById(id); if (m) { m.classList.add("open"); var i = $("input", m); if (i) setTimeout(function () { i.focus(); }, 50); } }
  function closeModal(m) { m.classList.remove("open"); }
  $$("[data-open]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); openModal(b.getAttribute("data-open")); }); });
  $$(".modal").forEach(function (m) {
    m.addEventListener("click", function (e) { if (e.target === m || e.target.closest(".close")) closeModal(m); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") $$(".modal.open").forEach(closeModal);
    if ((e.key === "/" || (e.key === "k" && (e.metaKey || e.ctrlKey))) && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); openModal("search-modal"); }
  });

  /* ---------- Site search ---------- */
  var sIn = $("#search-input"), sOut = $("#search-results");
  if (sIn && sOut) {
    var render = function () {
      var q = sIn.value.trim().toLowerCase(), idx = window.SEARCH_INDEX || [];
      var res = !q ? idx.slice(0, 8) : idx.filter(function (p) { return (p.t + " " + p.d + " " + (p.k || "")).toLowerCase().indexOf(q) > -1; }).slice(0, 12);
      sOut.innerHTML = res.length ? res.map(function (p) { return '<a href="' + p.u + '"><strong>' + p.t + '</strong><br><span class="muted small">' + p.d + "</span></a>"; }).join("") : '<p class="muted">No match. Try "split", "tip", "donate", "contest".</p>';
    };
    sIn.addEventListener("input", render); render();
  }

  /* ---------- Cookie consent, AdSense, Analytics ---------- */
  function loadScript(src, attrs) { var s = document.createElement("script"); s.async = true; s.src = src; for (var k in (attrs || {})) s.setAttribute(k, attrs[k]); document.head.appendChild(s); return s; }
  function initAds() {
    var slots = $$(".ad-slot");
    if (C.adsenseClient) {
      loadScript("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient, { crossorigin: "anonymous" });
      slots.forEach(function (s) {
        var pos = s.getAttribute("data-pos") || "top";
        s.innerHTML = '<div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient + '"' + (C.adSlots && C.adSlots[pos] ? ' data-ad-slot="' + C.adSlots[pos] + '"' : "") + ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
        try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
      });
    } else {
      slots.forEach(function (s) {
        s.innerHTML = '<div class="ad-label">Advertisement</div><div class="ad-box"><div><strong>Your brand here.</strong> Reach people at the exact moment they decide.<br><a href="advertise.html">Advertise or sponsor on 1Each →</a></div></div>';
      });
    }
  }
  function initAnalytics() {
    if (!C.ga4) return;
    loadScript("https://www.googletagmanager.com/gtag/js?id=" + C.ga4);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date()); gtag("config", C.ga4, { anonymize_ip: true });
  }
  var consent = store("consent"), ck = $("#cookie");
  initAds();
  if (consent === "all") initAnalytics();
  if (!consent && ck) ck.classList.add("show");
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () { var v = b.getAttribute("data-consent"); store("consent", v); ck.classList.remove("show"); if (v === "all") initAnalytics(); });
  });
  window.OneEach.track = function (name, params) { if (window.gtag) gtag("event", name, params || {}); };

  /* ---------- Forms (all routed privately) ---------- */
  $$("form.js-form").forEach(function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = $(".form-msg", f), btn = $("[type=submit]", f);
      if (f.querySelector(".hp input") && f.querySelector(".hp input").value) return; // bot
      if (!f.checkValidity()) { f.reportValidity(); return; }
      var data = {}; new FormData(f).forEach(function (v, k) { if (k !== "_hp") data[k] = data[k] ? data[k] + ", " + v : v; });
      data._subject = "[1Each] " + (f.getAttribute("data-subject") || "Form submission") + (data.name ? " — " + data.name : "");
      data._template = "table"; data._captcha = "false";
      data.page = location.pathname; data.referrer = document.referrer || "direct";
      var ref = store("ref"); if (ref) data.referred_by = ref;
      if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === "false") throw new Error(j.message || "fail"); }); })
        .then(function () {
          if (msg) { msg.className = "form-msg ok"; msg.textContent = f.getAttribute("data-ok") || "Thanks! We received your message and will reply soon."; }
          window.OneEach.track("generate_lead", { form: f.getAttribute("data-subject") });
          f.reset(); f.dispatchEvent(new CustomEvent("sent"));
        })
        .catch(function () {
          if (msg) { msg.className = "form-msg err"; msg.innerHTML = 'Could not send right now. <a href="#" class="js-fallback">Open your email app instead</a>.'; var fb = $(".js-fallback", msg); if (fb) fb.onclick = function (ev) { ev.preventDefault(); window.OneEach.mailto(data._subject); }; }
        })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = btn._t; } });
    });
  });

  /* ---------- Referral capture (contest bonus entries) ---------- */
  var p = new URLSearchParams(location.search);
  if (p.get("ref")) store("ref", p.get("ref").slice(0, 40));

  /* ---------- YouTube facade ---------- */
  var vg = $("#video-grid");
  if (vg && C.videos) {
    var lim = parseInt(vg.getAttribute("data-limit") || "99", 10);
    vg.innerHTML = C.videos.slice(0, lim).map(function (v) {
      return '<div><div class="video" data-id="' + (v.id || "") + '" data-q="' + encodeURIComponent(v.q || v.title) + '" role="button" tabindex="0" aria-label="Play: ' + v.title + '">' +
        (v.id ? '<img loading="lazy" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt="" style="width:100%;height:100%;object-fit:cover">' : "") +
        '<div class="ph"' + (v.id ? ' style="background:rgba(0,0,0,.35)"' : "") + '><div><div class="play">▶</div><strong>' + v.title + "</strong>" + (v.id ? "" : '<div class="small" style="opacity:.8">Watch on YouTube</div>') + "</div></div></div></div>";
    }).join("");
    $$(".video", vg).forEach(function (el) {
      var go = function () {
        var id = el.getAttribute("data-id");
        if (id) el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="YouTube video"></iframe>';
        else window.open("https://www.youtube.com/results?search_query=" + el.getAttribute("data-q"), "_blank", "noopener");
        window.OneEach.track("video_play", { id: id || "search" });
      };
      el.addEventListener("click", go); el.addEventListener("keydown", function (e) { if (e.key === "Enter") go(); });
    });
  }

  /* ---------- Contest countdown ---------- */
  var cd = $("#countdown");
  if (cd && C.contest) {
    var end = new Date(C.contest.ends).getTime();
    var tick = function () {
      var d = Math.max(0, end - Date.now()), s = Math.floor(d / 1000);
      var vals = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60];
      cd.innerHTML = ["Days", "Hours", "Min", "Sec"].map(function (l, i) { return "<div><b>" + vals[i] + "</b><span class=\"small\">" + l + "</span></div>"; }).join("");
    };
    tick(); setInterval(tick, 1000);
  }
  $$("[data-contest-prize]").forEach(function (el) { el.textContent = C.contest.prize; });
  $$("[data-contest-name]").forEach(function (el) { el.textContent = C.contest.name; });
  $$("[data-contest-ends]").forEach(function (el) { el.textContent = new Date(C.contest.ends).toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" }); });

  /* ---------- Referral link generator ---------- */
  var rf = $("#ref-form");
  if (rf) rf.addEventListener("sent", function () {
    var code = Math.random().toString(36).slice(2, 8);
    var link = location.origin + location.pathname + "?ref=" + code;
    var box = $("#ref-link"); if (box) { box.value = link; box.closest(".card").style.display = "block"; }
  });
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () { var t = document.getElementById(b.getAttribute("data-copy")); if (!t) return; (navigator.clipboard ? navigator.clipboard.writeText(t.value) : Promise.reject()).then(function () { toast("Copied!"); }, function () { t.select(); document.execCommand("copy"); toast("Copied!"); }); });
  });

  /* ---------- Share ---------- */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var data = { title: document.title, url: location.href };
      if (navigator.share) navigator.share(data).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(location.href).then(function () { toast("Link copied"); });
    });
  });

  /* ---------- Donations ---------- */
  var dForm = $("#donate-form");
  if (dForm) {
    var amt = $("#d-amount");
    $$(".amount", dForm).forEach(function (b) {
      b.addEventListener("click", function () { $$(".amount", dForm).forEach(function (x) { x.classList.remove("sel"); }); b.classList.add("sel"); amt.value = b.getAttribute("data-v"); });
    });
    var links = $("#donate-links"), D = C.donate || {}, names = { kofi: "Ko-fi", buymeacoffee: "Buy Me a Coffee", paypal: "PayPal", githubSponsors: "GitHub Sponsors", stripe: "Card (Stripe)" };
    var html = Object.keys(names).filter(function (k) { return D[k]; }).map(function (k) { return '<a class="btn btn-ghost" target="_blank" rel="noopener" href="' + D[k] + '">' + names[k] + " →</a>"; }).join("");
    if (links) links.innerHTML = html || '<p class="small muted">Instant payment buttons are being connected. Send a pledge below and we\'ll reply with a secure payment link within 24 hours.</p>';
  }

  /* ---------- Multi-step lead form ---------- */
  var lf = $("#lead-form");
  if (lf) {
    var steps = $$(".step", lf), cur = 0, bar = $(".steps-bar i", lf);
    var show = function (i) {
      steps.forEach(function (s, j) { s.classList.toggle("active", j === i); });
      cur = i; if (bar) bar.style.width = ((i + 1) / steps.length * 100) + "%";
      var st = $("#step-num"); if (st) st.textContent = (i + 1) + " / " + steps.length;
    };
    $$(".opt", lf).forEach(function (o) {
      o.addEventListener("click", function () {
        var grp = o.closest(".opt-grid"), multi = grp.hasAttribute("data-multi");
        if (!multi) $$(".opt", grp).forEach(function (x) { x.classList.remove("sel"); });
        o.classList.toggle("sel", multi ? !o.classList.contains("sel") : true);
        var hidden = $('input[name="' + grp.getAttribute("data-name") + '"]', lf);
        hidden.value = $$(".opt.sel", grp).map(function (x) { return x.getAttribute("data-v"); }).join(", ");
        if (!multi) setTimeout(function () { if (cur < steps.length - 1) show(cur + 1); }, 180);
      });
    });
    $$("[data-next]", lf).forEach(function (b) { b.addEventListener("click", function () {
      var req = $$("[required]", steps[cur]).filter(function (i) { return !i.checkValidity(); });
      if (req.length) { req[0].reportValidity(); return; }
      var g = $(".opt-grid", steps[cur]); if (g && !$('input[name="' + g.getAttribute("data-name") + '"]', lf).value) { toast("Pick one option to continue"); return; }
      show(Math.min(cur + 1, steps.length - 1)); }); });
    $$("[data-prev]", lf).forEach(function (b) { b.addEventListener("click", function () { show(Math.max(cur - 1, 0)); }); });
    var pre = new URLSearchParams(location.search).get("need");
    if (pre) { var o = $('.opt[data-v="' + pre + '"]', lf); if (o) o.click(); }
    lf.addEventListener("sent", function () { show(0); $$(".opt.sel", lf).forEach(function (x) { x.classList.remove("sel"); }); });
    show(0);
  }

  /* ---------- Sticky CTA + exit intent ---------- */
  var sticky = $("#sticky-cta");
  if (sticky && !$("#lead-form")) {
    window.addEventListener("scroll", function () { sticky.classList.toggle("show", scrollY > 900); }, { passive: true });
  }
  if (!store("exit_seen") && !$("#lead-form") && $("#exit-modal")) {
    var fired = false, fire = function () { if (fired) return; fired = true; store("exit_seen", "1"); openModal("exit-modal"); };
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 8) fire(); });
    setTimeout(function () { if (scrollY > 1400) fire(); }, 45000);
  }

  /* ---------- Reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .08 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else $$(".reveal").forEach(function (el) { el.classList.add("in"); });

  /* ---------- Year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Service worker ---------- */
  if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(function () {});
})();
