#!/usr/bin/env python3
"""1Each.com site generator.

    python3 build.py

Writes two things from pages.py:
  1. Jekyll sources in the repo root (one .html per page = front matter + body, plus
     _layouts/default.html). GitHub Pages builds these for free on every push; no Actions needed.
  2. A fully rendered local preview in _site/ (open _site/index.html), identical to what Pages serves.
Also writes sitemap.xml, assets/js/search-index.js and assets/img/og.png (if Pillow is installed)."""
import json, os, datetime, shutil
from pages import PAGES  # page bodies live in pages.py

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://1each.com/"
TODAY = datetime.date.today().isoformat()
V = TODAY.replace("-", "")  # cache-busting version

NAV = [("picks.html", "Picks"), ("tools.html", "Tools"), ("videos.html", "Videos"), ("get-matched.html", "Get Matched"),
       ("contests.html", "Contests"), ("support.html", "Support"), ("advertise.html", "Advertise")]

# Values differ per page; in the Jekyll layout they become Liquid tags, in the preview real values.
LIQUID = dict(title="{{ page.title }}", desc="{{ page.description }}", canon="{{ page.canon }}",
              robots="{{ page.robots | default: 'index,follow,max-image-preview:large' }}")

def nav_html(cur):
    out = []
    for u, t in NAV:
        if cur is None:
            out.append(f'<a href="{u}"{{% if page.file == "{u}" %}} aria-current="page"{{% endif %}}>{t}</a>')
        else:
            out.append(f'<a href="{u}"' + (' aria-current="page"' if u == cur else '') + f'>{t}</a>')
    return "".join(out)

def head(v, cur):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{v['title']}</title>
<meta name="description" content="{v['desc']}">
<link rel="canonical" href="{SITE}{v['canon']}">
<meta name="robots" content="{v['robots']}">
<meta name="theme-color" content="#5b3df5">
<meta property="og:type" content="website"><meta property="og:site_name" content="1Each">
<meta property="og:title" content="{v['title']}"><meta property="og:description" content="{v['desc']}">
<meta property="og:url" content="{SITE}{v['canon']}"><meta property="og:image" content="{SITE}assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={V}">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="header"><div class="container row">
  <a class="logo" href="index.html" aria-label="1Each home"><span class="mark">1</span>1Each</a>
  <nav class="nav" id="nav" aria-label="Main">{nav_html(cur)}</nav>
  <div class="hdr-actions">
    <button class="icon-btn" data-open="search-modal" aria-label="Search (press /)">🔍</button>
    <button class="icon-btn" id="theme-toggle" aria-label="Toggle dark mode">🌓</button>
    <a class="btn btn-primary btn-sm" href="get-matched.html">Get my 1 pick</a>
    <button class="icon-btn menu-btn" id="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav">☰</button>
  </div>
</div></header>
<main id="main">
"""

def foot(scripts):
    return f"""</main>
<section style="padding-top:0"><div class="container">
  <div class="newsletter reveal">
    <div class="eyebrow" style="color:var(--accent)">The 1Each Letter</div>
    <h2 style="color:#fff">One smart pick, each week. Free.</h2>
    <p style="opacity:.9;margin:0">The best-value pick, one money tool and one deal alert — a 2-minute read. Unsubscribe anytime.</p>
    <form class="js-form" data-subject="Newsletter signup" data-ok="You're in! Watch your inbox for the next edition.">
      <div class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></div>
      <input type="email" name="email" required placeholder="you@email.com" aria-label="Email">
      <input type="hidden" name="list" value="weekly">
      <button class="btn btn-accent" type="submit">Subscribe</button>
      <div class="form-msg" role="status" style="flex-basis:100%"></div>
    </form>
  </div>
</div></section>
<footer class="footer"><div class="container">
  <div class="cols">
    <div>
      <a class="logo" href="index.html" style="color:#fff"><span class="mark">1</span>1Each</a>
      <p style="margin-top:12px">One clear answer for each decision: the best pick, the true cost, the fair split.</p>
      <a class="btn btn-accent btn-sm" href="support.html">♥ Support 1Each</a>
    </div>
    <div><h4>Decide</h4><ul><li><a href="picks.html">One Pick guides</a></li><li><a href="get-matched.html">Get matched</a></li><li><a href="videos.html">Videos</a></li><li><a href="about.html#how-we-choose">How we choose</a></li></ul></div>
    <div><h4>Tools</h4><ul><li><a href="split-bill.html">Split the bill</a></li><li><a href="unit-price.html">Unit price</a></li><li><a href="cost-per-use.html">Cost per use</a></li><li><a href="tip-calculator.html">Tip calculator</a></li><li><a href="trip-splitter.html">Trip settle-up</a></li><li><a href="subscription-audit.html">Subscription audit</a></li></ul></div>
    <div><h4>Community</h4><ul><li><a href="contests.html">Contests &amp; prizes</a></li><li><a href="support.html">Donate / support</a></li><li><a href="careers.html">Careers &amp; talent</a></li><li><a href="advertise.html">Advertise / sponsor</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    <div><h4>Legal</h4><ul><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li><a href="disclosure.html">Affiliate &amp; trademark disclosure</a></li><li><a href="cookies.html">Cookies</a></li><li><a href="about.html">About</a></li></ul></div>
  </div>
  <div class="legal">
    <p>© <span data-year>2026</span> 1Each.com. All original content, tools and design are protected by copyright. "1Each" is used as a descriptive site name meaning "one each"; this site is independent and is not affiliated with, endorsed by, or sponsored by any company, product or trademark owner using a similar name. All third-party names and marks belong to their respective owners and are used for identification only. Some links may be affiliate links — we may earn a commission at no extra cost to you. Content is general information, not financial, legal or medical advice. <a href="disclosure.html">Full disclosure</a>.</p>
    <p>Interested in this website, the domain name, sponsorship, advertising or partnership? <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></p>
  </div>
</div></footer>

<div class="modal" id="search-modal" role="dialog" aria-modal="true" aria-label="Search"><div class="box">
  <button class="icon-btn close" aria-label="Close">✕</button>
  <h3>Search 1Each</h3><input id="search-input" type="search" placeholder="Try: split, tip, laptop, donate…" aria-label="Search">
  <div id="search-results" style="margin-top:12px"></div>
</div></div>
<div class="modal" id="exit-modal" role="dialog" aria-modal="true" aria-label="Get your pick"><div class="box">
  <button class="icon-btn close" aria-label="Close">✕</button>
  <div class="eyebrow">Before you go</div><h3>Stuck choosing? Get ONE personalized pick — free.</h3>
  <p class="muted">Tell us what you need. A human replies with one clear recommendation within 48 hours. No spam, ever.</p>
  <form class="js-form" data-subject="Quick pick request (exit)" data-ok="Got it! Your 1 pick is on its way within 48 hours.">
    <div class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></div>
    <div class="field"><input name="need" required placeholder="What are you deciding on? e.g. a laptop under $900"></div>
    <div class="field"><input type="email" name="email" required placeholder="Your email"></div>
    <button class="btn btn-primary btn-block" type="submit">Send me my 1 pick</button>
    <div class="form-msg" role="status"></div>
  </form>
</div></div>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent">
  <strong>Cookies, briefly.</strong> <span class="small muted">We use essential storage to run tools, and—only with your OK—analytics and ads cookies (Google) to keep 1Each free. <a href="cookies.html">Details</a></span>
  <div style="display:flex;gap:8px;margin-top:10px"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div>
</div>
<a class="btn btn-primary sticky-cta" id="sticky-cta" href="get-matched.html">🎯 Get my 1 pick</a>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/js/config.js?v={V}"></script>
<script src="assets/js/search-index.js?v={V}" defer></script>
{scripts}
<script src="assets/js/app.js?v={V}" defer></script>
</body>
</html>
"""

def canon(p):
    return "" if p["file"] == "index.html" else p["file"]

def page_scripts(js):
    return "".join(f'<script src="assets/js/{s}?v={V}" defer></script>' for s in js)

def front_matter(p):
    q = lambda s: json.dumps(s, ensure_ascii=False)  # JSON strings are valid YAML
    fm = ["---", "layout: default", f"file: {q(p['file'])}", f"title: {q(p['title'])}", f"description: {q(p['desc'])}",
          f"canon: {q(canon(p))}"]
    if p.get("robots"):
        fm.append(f"robots: {q(p['robots'])}")
    if p.get("js"):
        fm.append("js: [" + ", ".join(q(s) for s in p["js"]) + "]")
    if p["file"] == "404.html":
        fm.append("permalink: /404.html")
    fm.append("---")
    return "\n".join(fm) + "\n"

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    # 1) Jekyll layout + page sources (what GitHub Pages builds)
    layout_scripts = '{% for s in page.js %}<script src="assets/js/{{ s }}?v=' + V + '" defer></script>{% endfor %}'
    write(os.path.join(ROOT, "_layouts/default.html"), head(LIQUID, None) + "{{ content }}" + foot(layout_scripts))
    for p in PAGES:
        write(os.path.join(ROOT, p["file"]), front_matter(p) + p.get("ld", "") + p["body"])

    # 2) Local preview, fully rendered (mirrors the Jekyll output)
    out = os.path.join(ROOT, "_site")
    shutil.rmtree(out, ignore_errors=True)
    for item in ["assets", "manifest.webmanifest", "sw.js", "robots.txt", "ads.txt"]:
        src = os.path.join(ROOT, item)
        (shutil.copytree if os.path.isdir(src) else shutil.copy)(src, os.path.join(out, item))

    index = []
    for p in PAGES:
        v = dict(title=p["title"], desc=p["desc"], canon=canon(p), robots=p.get("robots", "index,follow,max-image-preview:large"))
        write(os.path.join(out, p["file"]), head(v, p["file"]) + p.get("ld", "") + p["body"] + foot(page_scripts(p.get("js", []))))
        if p.get("robots", "").startswith("noindex"):
            continue
        index.append({"u": p["file"], "t": p.get("nav", p["title"].split(" | ")[0].split(" — ")[0]), "d": p["desc"], "k": p.get("k", "")})

    si = "window.SEARCH_INDEX=" + json.dumps(index, ensure_ascii=False) + ";\n"
    write(os.path.join(ROOT, "assets/js/search-index.js"), si)
    write(os.path.join(out, "assets/js/search-index.js"), si)
    urls = "".join(f"<url><loc>{SITE}{'' if i['u']=='index.html' else i['u']}</loc><lastmod>{TODAY}</lastmod></url>" for i in index)
    sm = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n'
    write(os.path.join(ROOT, "sitemap.xml"), sm)
    write(os.path.join(out, "sitemap.xml"), sm)
    make_og()
    if os.path.exists(os.path.join(ROOT, "assets/img/og.png")):
        shutil.copy(os.path.join(ROOT, "assets/img/og.png"), os.path.join(out, "assets/img/og.png"))
    print(f"Built {len(PAGES)} pages (Jekyll sources + _site preview)")

def make_og():
    """Render the 1200x630 social share image (needs Pillow; skipped if unavailable)."""
    out = os.path.join(ROOT, "assets/img/og.png")
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return
    im = Image.new("RGB", (1200, 630), "#12121a"); d = ImageDraw.Draw(im)
    def f(s):
        for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
            try: return ImageFont.truetype(p, s)
            except Exception: pass
        return ImageFont.load_default()
    d.rounded_rectangle((80, 80, 230, 230), radius=36, fill="#5b3df5")
    d.text((125, 95), "1", font=f(120), fill="white"); d.ellipse((190, 175, 215, 200), fill="#c6f432")
    d.text((80, 290), "1Each", font=f(110), fill="white")
    d.text((80, 430), "One smart answer. For each decision.", font=f(44), fill="#c6f432")
    d.text((80, 510), "Best pick · True cost · Fair split", font=f(34), fill="#a3a3b8")
    im.save(out)

if __name__ == "__main__":
    main()
