# -*- coding: utf-8 -*-
"""Page bodies for 1Each.com. Each page = dict(file, title, desc, body, js, ld, k)."""
import json

def ad(pos="top"):
    return f'<div class="ad-slot" data-pos="{pos}" aria-label="Advertisement"></div>'

def page_hero(eyebrow, h1, lead, crumb):
    return f'''<section class="page-hero"><div class="container">
  <div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
  <span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="muted" style="font-size:1.15rem;max-width:720px">{lead}</p>
</div></section>'''

def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs) + "</div>"

def faq_ld(faqs):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}) + "</script>"

def hp():
    return '<div class="hp"><input name="_hp" tabindex="-1" autocomplete="off"></div>'

CUR = '''<select class="cur-select" aria-label="Currency" style="width:auto;padding:6px 10px">
<option>USD</option><option>CAD</option><option>EUR</option><option>GBP</option><option>INR</option><option>AUD</option><option>AED</option><option>LKR</option></select>'''

TOOLS = [
    ("split-bill.html", "🧾", "Split the Bill", "Tax, tip, uneven orders — everyone's fair share in seconds."),
    ("unit-price.html", "⚖️", "Unit Price Comparer", "Which size is really cheaper? Compare per 100 g, per ml or per each."),
    ("cost-per-use.html", "🔁", "Cost Per Use", "When the expensive one is actually the cheaper buy."),
    ("tip-calculator.html", "💵", "Tip Calculator", "Right tip, rounded smart, split any number of ways."),
    ("trip-splitter.html", "🧳", "Group Trip Settle-Up", "Who owes whom — with the fewest transfers."),
    ("subscription-audit.html", "📆", "Subscription Audit", "See your yearly total and what cutting one is worth."),
]

def tool_cards(exclude=None):
    return '<div class="grid g3">' + "".join(
        f'<a class="card link reveal" href="{u}"><div class="ico" aria-hidden="true">{i}</div><h3>{n}</h3><p class="muted">{d}</p><span>Open tool →</span></a>'
        for u, i, n, d in TOOLS if u != exclude) + "</div>"

LEAD_CTA = '''<section><div class="container"><div class="banner reveal">
  <div class="grid g2" style="align-items:center">
    <div><span class="eyebrow" style="color:var(--accent)">Free · 48-hour reply · No spam</span>
      <h2 style="color:#fff">Stop comparing 40 tabs. Get ONE answer.</h2>
      <p class="muted">Tell us what you're deciding. A real person sends you one clear pick — or connects you with vetted providers for quotes when that saves you more.</p></div>
    <div class="cta-row" style="justify-content:flex-end"><a class="btn btn-accent" href="get-matched.html">Get my 1 pick →</a><a class="btn btn-ghost" href="picks.html">Browse guides</a></div>
  </div></div></div></section>'''

def tool_page(file, name, desc, lead, k, form, result, guide, faqs):
    body = page_hero("Free tool · No sign-up · Works offline", name, lead, f'<a href="tools.html">Tools</a> / {name}') + f'''
<section style="padding-top:32px"><div class="container">
  <div style="display:flex;justify-content:flex-end;gap:8px;align-items:center;margin-bottom:12px"><span class="small muted">Currency</span>{CUR}<button class="btn btn-ghost btn-sm" data-share>Share</button></div>
  <div class="tool" id="{TOOL_IDS[file]}">
    <div class="card">{form}</div>
    <div>{result}</div>
  </div>
</div></section>
{ad("inArticle")}
<section><div class="container prose">{guide}
<h2>FAQ</h2>{faq_html(faqs)}</div></section>
{LEAD_CTA}
<section style="padding-top:0"><div class="container"><h2>More one-minute tools</h2>{tool_cards(file)}</div></section>
{ad("footer")}'''
    ld = faq_ld(faqs) + '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "WebApplication", "name": name, "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": "https://1each.com/" + file}) + "</script>"
    return dict(file=file, title=f"{name} — Free, Instant | 1Each", desc=desc, body=body, js=["tools.js"], ld=ld, k=k, nav=name)

def result_card(big_id, big_label, table_id, extra=""):
    return f'''<div class="result" aria-live="polite"><div class="small" style="opacity:.85">{big_label}</div><div class="big" id="{big_id}">—</div>
<table><tbody id="{table_id}"></tbody></table></div>{extra}'''

TOOL_IDS = {"split-bill.html": "tool-split", "unit-price.html": "tool-unit", "cost-per-use.html": "tool-cpu",
            "tip-calculator.html": "tool-tip", "trip-splitter.html": "tool-trip", "subscription-audit.html": "tool-subs"}

PAGES = []

# ---------------------------------------------------------------- HOME
home_ld = '<script type="application/ld+json">' + json.dumps([
    {"@context": "https://schema.org", "@type": "WebSite", "name": "1Each", "url": "https://1each.com/",
     "potentialAction": {"@type": "SearchAction", "target": "https://1each.com/picks.html?q={q}", "query-input": "required name=q"}},
    {"@context": "https://schema.org", "@type": "Organization", "name": "1Each", "url": "https://1each.com/", "logo": "https://1each.com/assets/img/favicon.svg"}]) + "</script>"
home_faqs = [
    ("What is 1Each?", "1Each gives one clear answer for each everyday decision: a single best-value pick per category, free calculators that show the true cost of each option, and a fair split for every shared bill."),
    ("Is 1Each free?", "Yes. Every guide and tool is free, with no sign-up. We're supported by ads, affiliate commissions, sponsors and reader donations — never by paid rankings."),
    ("How do you choose the one pick?", "We start from a single decision rule per category, apply a checklist of must-haves, then give a budget, top and upgrade option. The math behind every tool is shown on the page."),
    ("Can I get a personal recommendation?", "Yes — use Get Matched. Tell us your budget and must-haves and a person replies with one pick, usually within 48 hours."),
]
PAGES.append(dict(file="index.html", nav="Home", title="1Each — One Smart Answer for Each Decision",
  desc="The one best pick for each need, free calculators for the true cost of each option, and a fair split every time. Tools, guides, videos and contests.",
  js=["tools.js", "picks.js"], ld=home_ld + faq_ld(home_faqs), k="home best pick split each",
  body=f'''
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="eyebrow">Best pick · True cost · Fair split</span>
    <h1>One smart answer.<br><span class="hl">For each decision.</span></h1>
    <p class="lead">Skip the 40 tabs. 1Each gives you the <strong>one</strong> pick worth buying, the real cost of <strong>each</strong> option, and exactly what everyone owes — in under a minute.</p>
    <div class="cta-row"><a class="btn btn-primary" href="get-matched.html">🎯 Get my 1 pick — free</a><a class="btn btn-ghost" href="tools.html">Try the tools</a></div>
    <div class="trust"><span>Free, no sign-up</span><span>No paid rankings</span><span>Math shown on every tool</span><span>Private: tools run in your browser</span></div>
  </div>
  <div class="card" id="hero-split" style="border-radius:24px">
    <div style="display:flex;justify-content:space-between;align-items:center"><strong>Quick split</strong><a class="small" href="split-bill.html">Full calculator →</a></div>
    <div class="row2" style="margin-top:12px">
      <div class="field"><label for="hs-bill">Bill</label><input id="hs-bill" type="number" min="0" step="0.01" value="128.40" inputmode="decimal"></div>
      <div class="field"><label for="hs-people">People</label><input id="hs-people" type="number" min="1" value="4" inputmode="numeric"></div>
    </div>
    <label>Tip</label><input type="hidden" id="hs-tip" value="18">
    <div class="chips" id="hs-tips"><button class="chip" data-v="0">0%</button><button class="chip" data-v="15">15%</button><button class="chip active" data-v="18">18%</button><button class="chip" data-v="20">20%</button><button class="chip" data-v="25">25%</button></div>
    <div class="result" style="margin-top:16px"><div class="small" style="opacity:.85">Each person pays</div><div class="big" id="hs-each">—</div><div class="small" id="hs-sub" style="opacity:.85;margin-top:6px"></div></div>
  </div>
</div></section>
{ad("top")}
<section><div class="container">
  <div class="section-head"><div><span class="eyebrow">Start with your moment</span><h2>What are you deciding right now?</h2></div></div>
  <div class="grid g3">
    <a class="card link reveal" href="split-bill.html"><div class="ico">🍽️</div><h3>Dinner with friends</h3><p class="muted">Tax, tip and who-had-what — settled before the check lands.</p></a>
    <a class="card link reveal" href="trip-splitter.html"><div class="ico">🏕️</div><h3>Group trip or roommates</h3><p class="muted">Log who paid; we compute the fewest transfers to square up.</p></a>
    <a class="card link reveal" href="unit-price.html"><div class="ico">🛒</div><h3>Grocery aisle</h3><p class="muted">Big pack or small? The per-unit price answers in 5 seconds.</p></a>
    <a class="card link reveal" href="cost-per-use.html"><div class="ico">👟</div><h3>A bigger purchase</h3><p class="muted">Cost-per-use shows when "expensive" is the smart buy.</p></a>
    <a class="card link reveal" href="subscription-audit.html"><div class="ico">📺</div><h3>Monthly subscriptions</h3><p class="muted">See the yearly total and what cutting one is really worth.</p></a>
    <a class="card link reveal" href="get-matched.html"><div class="ico">🎯</div><h3>"Just tell me what to buy"</h3><p class="muted">Get one personal recommendation from a human, free.</p></a>
  </div>
</div></section>
<section style="background:var(--surface)"><div class="container">
  <div class="section-head"><div><span class="eyebrow">One Pick guides</span><h2>The one rule for each thing you buy</h2><p class="muted" style="margin:0">Each guide: 1 decision rule, a must-have checklist, and a budget / top / upgrade pick.</p></div><a class="btn btn-ghost" href="picks.html">All guides →</a></div>
  <div class="grid g3" id="picks-grid" data-limit="6"></div>
</div></section>
<section><div class="container">
  <div class="section-head"><div><span class="eyebrow">Free tools</span><h2>Know the true cost of each option</h2></div><a class="btn btn-ghost" href="tools.html">All tools →</a></div>
  {tool_cards()}
</div></section>
{LEAD_CTA}
<section><div class="container">
  <div class="section-head"><div><span class="eyebrow">Watch</span><h2>Money-smart in 60 seconds</h2></div><a class="btn btn-ghost" href="videos.html">All videos →</a></div>
  <div class="grid g3" id="video-grid" data-limit="3"></div>
</div></section>
{ad("inArticle")}
<section><div class="container"><div class="banner reveal">
  <div class="grid g2" style="align-items:center">
    <div><span class="eyebrow" style="color:var(--accent)">Contest open</span><h2 style="color:#fff" data-contest-name>The Split-It Challenge</h2>
      <p class="muted">Share your best money-saving "one each" tip. Prize: <strong style="color:#fff" data-contest-prize></strong>. Bonus entries for every friend you refer.</p>
      <a class="btn btn-accent" href="contests.html">Enter free →</a></div>
    <div><div class="countdown" id="countdown" aria-label="Time left"></div></div>
  </div></div></div></section>
<section style="background:var(--surface)"><div class="container grid g2" style="align-items:center">
  <div><span class="eyebrow">Why trust 1Each</span><h2>Independent by design</h2>
    <p class="muted">Rankings are never for sale. Sponsors are labelled. Every calculator shows its formula, so you can check our work.</p>
    <div class="stats" style="margin-top:20px"><div class="stat"><b>{len(TOOLS)}</b>free tools</div><div class="stat"><b>18</b>One Pick guides</div><div class="stat"><b>0</b>paid rankings</div><div class="stat"><b>48h</b>pick reply</div></div></div>
  <div class="card"><h3>Keep 1Each free &amp; independent</h3><p class="muted">Reader support funds operations, promotion, new tools, hiring writers and contest prizes.</p>
    <div class="alloc"><span>Operations</span><div class="bar"><i style="width:35%"></i></div><b>35%</b></div>
    <div class="alloc"><span>New content &amp; talent</span><div class="bar"><i style="width:30%"></i></div><b>30%</b></div>
    <div class="alloc"><span>Marketing &amp; promotion</span><div class="bar"><i style="width:20%"></i></div><b>20%</b></div>
    <div class="alloc"><span>Contests &amp; prizes</span><div class="bar"><i style="width:15%"></i></div><b>15%</b></div>
    <a class="btn btn-primary" href="support.html">♥ Support 1Each</a></div>
</div></section>
<section><div class="container prose" style="margin:0 auto"><h2 class="center">Questions</h2>{faq_html(home_faqs)}</div></section>
{ad("footer")}
'''))

# ---------------------------------------------------------------- PICKS
PAGES.append(dict(file="picks.html", nav="One Pick Guides", title="One Pick Guides — The 1 Rule for Each Purchase | 1Each",
  desc="Buying guides reduced to one decision rule, a must-have checklist and a budget, top and upgrade pick — for home, kitchen, tech, money, travel and more.",
  js=["picks.js"], k="guides buy best mattress laptop credit card headphones",
  body=page_hero("One Pick guides", "The one rule for each thing you buy", "Every guide gives you 1 decision rule, a short must-have checklist, and three honest price points. Need it tailored? Get a personal pick free.", "Picks") + f'''
<section style="padding-top:28px"><div class="container">
  <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:20px">
    <div class="chips" id="pick-filters"></div>
    <input id="pick-q" type="search" placeholder="Filter guides…" style="max-width:260px;margin-left:auto" aria-label="Filter guides">
  </div>
  <div class="grid g3" id="picks-grid"></div>
  <p class="small muted" style="margin-top:20px">How we choose: guides are built from published specifications, standards and consumer-protection guidance, then reviewed for clarity. Sponsored placements, if any, are always labelled. <a href="disclosure.html">Disclosure</a>.</p>
</div></section>
{ad("inArticle")}{LEAD_CTA}'''))

# ---------------------------------------------------------------- TOOLS INDEX
PAGES.append(dict(file="tools.html", nav="All Tools", title="Free Money Calculators — Split, Unit Price, Tip & More | 1Each",
  desc="Free, private calculators: split the bill, unit price comparer, cost per use, tip calculator, group trip settle-up and subscription audit.",
  k="calculator tools", body=page_hero("Free tools", "Know the true cost of each option", "Six one-minute calculators. No sign-up, nothing stored on a server — every number stays in your browser.", "Tools") + f'''
<section><div class="container">{tool_cards()}</div></section>{ad("inArticle")}
<section style="padding-top:0"><div class="container"><div class="card"><h3>Want a tool we don't have?</h3><p class="muted">Suggest it — the most-requested tool each month gets built, and the person who suggested it gets credit on the page.</p>
<form class="js-form" data-subject="Tool suggestion" data-ok="Thanks! We read every suggestion.">{hp()}<div class="row2"><div class="field"><input name="tool_idea" required placeholder="Calculator idea"></div><div class="field"><input type="email" name="email" placeholder="Email (optional, for credit)"></div></div><button class="btn btn-primary" type="submit">Suggest a tool</button><div class="form-msg" role="status"></div></form></div></div></section>'''))

# ---------------------------------------------------------------- TOOL PAGES
PAGES.append(tool_page("split-bill.html", "Split the Bill Calculator",
  "Split a restaurant bill with tax and tip — evenly or by what each person ordered. See exactly what each person owes, with the math shown.",
  "Evenly or by what each person ordered — tax and tip included, math shown.", "split bill restaurant each person tax tip",
  '''<div class="seg" role="tablist" style="margin-bottom:16px"><button class="active" data-mode="equal">Split evenly</button><button data-mode="items">By what each ordered</button></div>
<div id="sb-equal"><div class="row2"><div class="field"><label for="sb-bill">Subtotal (before tax)</label><input id="sb-bill" type="number" min="0" step="0.01" value="142.60" inputmode="decimal"></div>
<div class="field"><label for="sb-ppl">People</label><input id="sb-ppl" type="number" min="1" value="4" inputmode="numeric"></div></div></div>
<div id="sb-items" style="display:none"><label>People and their own items</label><div id="sb-people"></div><button type="button" class="btn btn-ghost btn-sm" id="sb-add">+ Add person</button>
<div class="field" style="margin-top:12px"><label for="sb-shared">Shared items (split equally)</label><input id="sb-shared" type="number" min="0" step="0.01" value="22"></div></div>
<div class="row2"><div class="field"><label for="sb-tax">Tax %</label><input id="sb-tax" type="number" min="0" step="0.01" value="13"></div>
<div class="field"><label>Tip %</label><input id="sb-tip" type="number" min="0" step="0.5" value="18"></div></div>
<div class="chips" id="sb-tips" style="margin:-6px 0 14px"><button class="chip" data-v="15">15%</button><button class="chip active" data-v="18">18%</button><button class="chip" data-v="20">20%</button><button class="chip" data-v="22">22%</button></div>
<label class="check"><input type="checkbox" id="sb-tippre" checked> Tip on pre-tax amount (common etiquette)</label>
<label class="check"><input type="checkbox" id="sb-round"> Round each share up to a whole number</label>''',
  result_card("sb-each", "Each person pays", "sb-out", '<div class="working" id="sb-work"></div>'),
  '''<h2>How to split a bill fairly</h2><p>Splitting evenly is fastest when orders are similar. When one person had a steak and another had soup, split by items: each person pays their own items plus an equal share of anything shared (appetizers, a bottle), then tax and tip are applied proportionally so nobody subsidises anybody.</p>
<h2>Tip on pre-tax or post-tax?</h2><p>Etiquette guides generally suggest tipping on the pre-tax subtotal. The difference is small on a single meal — on a $150 bill with 13% tax and 18% tip, it's about $3.51 — but the toggle lets your group choose.</p>''',
  [("Should tax be split evenly?", "Tax should follow what each person ordered. Our by-items mode applies tax proportionally, which is the fairest method."),
   ("What is a normal tip?", "In the US and Canada, 15–20% for table service is typical; 18–20% is common in cities. Many countries include service — check the bill."),
   ("Does this store my data?", "No. The calculation runs entirely in your browser.")]))

PAGES.append(tool_page("unit-price.html", "Unit Price Comparer",
  "Compare unit prices across package sizes and units (g, kg, oz, lb, ml, l, fl oz, count). Instantly see the best value and how much you overpay.",
  "Which size is really cheaper? Mix grams, kilos, ounces or pounds — we convert and rank.", "unit price per ounce grocery compare bulk",
  '''<label>Items to compare</label><div id="up-items"></div><button type="button" class="btn btn-ghost btn-sm" id="up-add">+ Add item</button>
<p class="form-note" style="margin-top:12px">Tip: compare like with like — weight with weight, volume with volume, or count with count.</p>''',
  result_card("up-best", "Best value", "up-out"),
  '''<h2>Why unit price beats the sale sign</h2><p>"Family size" and "2 for $5" labels don't always mean cheaper. The unit price — cost per 100 g, per litre, or per item — is the only fair comparison across sizes and brands.</p>
<h2>When the bigger pack isn't worth it</h2><ul><li>You won't finish it before it spoils.</li><li>A smaller size is on sale below the bulk unit price.</li><li>Storage space or cash flow is tight.</li></ul>''',
  [("How is unit price calculated?", "Unit price = price ÷ quantity, converted to a common unit. We normalise to per 100 g, per 100 ml or per item."),
   ("Can I compare ounces with grams?", "Yes — we convert oz, lb, kg and g to a common base automatically. Fluid ounces are converted as volume.")]))

PAGES.append(tool_page("cost-per-use.html", "Cost Per Use Calculator",
  "Compare two purchases by true cost per use, including upkeep and resale value. Find out when the expensive option is actually cheaper.",
  "Compare two options by what each use really costs — upkeep and resale included.", "cost per use buy once cry once value",
  "".join(f'''<fieldset style="border:1px solid var(--line);border-radius:12px;padding:14px;margin:0 0 14px"><legend class="small" style="padding:0 6px"><strong>Option {x.upper()}</strong></legend>
<div class="field"><input id="cpu-{x}-name" value="{n}" aria-label="Option {x} name"></div>
<div class="row2"><div class="field"><label for="cpu-{x}-price">Price</label><input id="cpu-{x}-price" type="number" min="0" step="0.01" value="{p}"></div>
<div class="field"><label for="cpu-{x}-uses">Uses per week</label><input id="cpu-{x}-uses" type="number" min="0" step="0.1" value="{u}"></div>
<div class="field"><label for="cpu-{x}-years">Years it lasts</label><input id="cpu-{x}-years" type="number" min="0" step="0.1" value="{y}"></div>
<div class="field"><label for="cpu-{x}-maint">Upkeep per year</label><input id="cpu-{x}-maint" type="number" min="0" step="0.01" value="{m}"></div></div>
<div class="field" style="margin:0"><label for="cpu-{x}-resale">Resale value at end</label><input id="cpu-{x}-resale" type="number" min="0" step="0.01" value="{r}"></div></fieldset>'''
    for x, n, p, u, y, m, r in [("a", "Cheap boots", 60, 3, 1, 0, 0), ("b", "Quality boots", 240, 3, 6, 15, 30)]),
  result_card("cpu-best", "Lower cost per use", "cpu-out", '<div class="working" id="cpu-work"></div>'),
  '''<h2>The "buy once" math</h2><p>A $240 pair that lasts six years costs less per wear than a $60 pair replaced every year. Cost per use turns that instinct into a number — and also shows when the cheap option wins because you'll rarely use it.</p>''',
  [("What counts as a use?", "Anything you'd reasonably count: a wear, a ride, a cook, a session. Keep it consistent across both options."),
   ("Should I include resale value?", "Yes, if you'd realistically sell it. Quality items often keep resale value, which lowers their true cost.")]))

PAGES.append(tool_page("tip-calculator.html", "Tip Calculator",
  "Calculate the tip and total, split it between people, and round smartly. Includes a quick tipping guide by service.",
  "The right tip, rounded smart, split any number of ways.", "tip gratuity calculator restaurant",
  '''<div class="row2"><div class="field"><label for="tp-bill">Bill amount</label><input id="tp-bill" type="number" min="0" step="0.01" value="86.50"></div>
<div class="field"><label for="tp-ppl">People</label><input id="tp-ppl" type="number" min="1" value="2"></div></div>
<div class="field"><label for="tp-pct">Tip %</label><input id="tp-pct" type="number" min="0" step="0.5" value="18"></div>
<div class="chips" id="tp-tips" style="margin:-6px 0 14px"><button class="chip" data-v="10">10%</button><button class="chip" data-v="15">15%</button><button class="chip active" data-v="18">18%</button><button class="chip" data-v="20">20%</button><button class="chip" data-v="25">25%</button></div>
<div class="field"><label for="tp-round">Rounding</label><select id="tp-round"><option value="none">No rounding</option><option value="total">Round total up</option><option value="each">Round each share up</option></select></div>''',
  result_card("tp-each", "Each person pays", "tp-out"),
  '''<h2>Quick tipping guide (US/Canada norms)</h2><div class="table-wrap"><table class="cmp"><tr><th>Service</th><th>Typical tip</th></tr>
<tr><td>Sit-down restaurant</td><td>15–20%</td></tr><tr><td>Bar</td><td>$1–2 per drink or 15–20%</td></tr><tr><td>Food delivery</td><td>15–20%, minimum a few dollars</td></tr>
<tr><td>Taxi / rideshare</td><td>10–20%</td></tr><tr><td>Hair / salon</td><td>15–20%</td></tr><tr><td>Hotel housekeeping</td><td>$2–5 per night</td></tr></table></div>
<p class="small muted">Customs vary by country; in many places service is included. This is general guidance only.</p>''',
  [("Is 18% a good tip?", "18% is a common standard for sit-down service in North American cities; 20% for excellent service."),
   ("Do I tip on takeout?", "It's optional; many people leave 10% or round up for larger or complex orders.")]))

PAGES.append(tool_page("trip-splitter.html", "Group Trip Settle-Up",
  "Split group trip, roommate or event expenses. Log who paid what and get the fewest transfers to settle everyone up.",
  "Log who paid; get the fewest transfers to square up.", "group expenses roommates trip settle up who owes",
  '''<label for="tr-name">People</label><div style="display:flex;gap:8px;margin-bottom:10px"><input id="tr-name" placeholder="Add a name"><button type="button" class="btn btn-ghost" id="tr-add-p">Add</button></div>
<div id="tr-people" class="chips" style="margin-bottom:16px"></div>
<label>Expenses (paid by · amount · what for)</label><div id="tr-exps"></div><button type="button" class="btn btn-ghost btn-sm" id="tr-add-e">+ Add expense</button>
<p class="form-note" style="margin-top:12px">All expenses are split equally among everyone listed.</p>''',
  result_card("tr-each", "Fair share each", "tr-out", '<div class="card" style="margin-top:16px"><strong>Settle up with these transfers</strong><div class="working" id="tr-tx"></div></div>'),
  '''<h2>How we minimise transfers</h2><p>We compute each person's balance (what they paid minus their fair share), then match the biggest debtor with the biggest creditor repeatedly. This settles a group with at most n − 1 payments.</p>''',
  [("Can I split unequally?", "This version splits every expense equally. For different shares, use Split the Bill's by-items mode for each expense."),
   ("Is anything saved?", "No. Refreshing clears the list — screenshot or share the transfer list with your group.")]))

PAGES.append(tool_page("subscription-audit.html", "Subscription Audit Calculator",
  "Add up every subscription, see your monthly and yearly total, and what cancelling the ones you don't need is worth over 10 years.",
  "Your real yearly total — and what cutting one is worth in 10 years.", "subscriptions audit cancel save monthly yearly",
  '''<label>Subscriptions (uncheck "keep" to model cancelling)</label><div id="sa-list"></div><button type="button" class="btn btn-ghost btn-sm" id="sa-add">+ Add subscription</button>''',
  result_card("sa-year", "You spend per year", "sa-out"),
  '''<h2>The 3-question subscription test</h2><ol><li>Did I use it in the last 30 days?</li><li>Would I sign up again today at this price?</li><li>Is there a free or shared alternative?</li></ol><p>Two "no" answers = cancel. Investment figures assume 7% annual return compounded monthly and are illustrative only.</p>''',
  [("How often should I audit subscriptions?", "Every quarter, and before any annual renewal date."),
   ("Is the investment figure guaranteed?", "No. It's an illustration at a 7% assumed return; real returns vary and can be negative.")]))

# ---------------------------------------------------------------- VIDEOS
PAGES.append(dict(file="videos.html", nav="Videos", title="Videos — Money-Smart in 60 Seconds | 1Each",
  desc="Short videos on splitting bills, unit prices, cost per use, group expenses and choosing the one best pick.", k="youtube video watch",
  body=page_hero("1Each on YouTube", "Money-smart in 60 seconds", "Short, practical videos that pair with each tool. Subscribe for a new one each week.", "Videos") + f'''
<section><div class="container">
  <div class="cta-row" style="margin:0 0 24px"><a class="btn btn-primary" id="yt-sub" href="https://www.youtube.com/results?search_query=1Each" target="_blank" rel="noopener">▶ Subscribe on YouTube</a><a class="btn btn-ghost" href="careers.html">Become a creator partner</a></div>
  <div class="grid g3" id="video-grid"></div>
</div></section>{ad("inArticle")}
<section style="padding-top:0"><div class="container"><div class="card"><h3>Sponsor a video series</h3><p class="muted">Integrated, clearly-labelled sponsorships inside our tool tutorials. Performance reporting included.</p><a class="btn btn-primary" href="advertise.html#packages">See packages</a></div></div></section>
<script>document.addEventListener("DOMContentLoaded",function(){{var c=window.SITE_CONFIG;if(c&&c.youtubeChannel)document.getElementById("yt-sub").href=c.youtubeChannel;}});</script>'''))

# ---------------------------------------------------------------- GET MATCHED (lead gen)
needs = [("home", "🏠", "Home"), ("kitchen", "🍳", "Kitchen"), ("tech", "💻", "Tech"), ("money", "💳", "Money & banking"), ("insurance", "🛡️", "Insurance"),
         ("travel", "✈️", "Travel"), ("health", "🏃", "Health & fitness"), ("software", "🤖", "Software & AI"), ("business", "📈", "Business services"),
         ("solar", "☀️", "Solar & energy"), ("family", "🧸", "Kids & family"), ("other", "✨", "Something else")]
PAGES.append(dict(file="get-matched.html", nav="Get Matched", title="Get Matched — Your 1 Personalized Pick, Free | 1Each",
  desc="Tell us what you're deciding and your budget. Get one clear personalized recommendation — or vetted provider quotes — free within 48 hours.",
  k="lead recommendation quote personal advice help me choose",
  body=page_hero("Free · 60 seconds · Human reply in 48h", "Get your ONE pick", "Answer 4 quick questions. A real person sends you one clear recommendation — or, when it saves you more, introductions to up to 3 vetted providers for quotes. You choose.", "Get Matched") + f'''
<section style="padding-top:32px"><div class="container grid" style="grid-template-columns:minmax(0,1.4fr) minmax(0,.9fr);gap:28px">
  <div class="card">
    <form id="lead-form" class="js-form" data-subject="LEAD: Get Matched request" data-ok="🎉 Request received! Your 1 pick is on its way — check your inbox within 48 hours.">
      {hp()}
      <div style="display:flex;justify-content:space-between" class="small muted"><span>Step <span id="step-num">1 / 4</span></span><span>🔒 Your details are never sold</span></div>
      <div class="steps-bar"><i></i></div>
      <div class="step"><h3>What are you deciding on?</h3><input type="hidden" name="category">
        <div class="opt-grid" data-name="category">{"".join(f'<button type="button" class="opt" data-v="{v}"><b>{i}</b>{n}</button>' for v, i, n in needs)}</div></div>
      <div class="step"><h3>Budget and timing</h3><input type="hidden" name="budget">
        <div class="opt-grid" data-name="budget">{"".join(f'<button type="button" class="opt" data-v="{b}">{b}</button>' for b in ["Under $100", "$100–500", "$500–2,000", "$2,000–10,000", "$10,000+", "Not sure"])}</div>
        <div class="field" style="margin-top:16px"><label for="lf-when">When do you plan to decide?</label><select id="lf-when" name="timeline"><option>This week</option><option>This month</option><option>1–3 months</option><option>Just researching</option></select></div>
        <div style="display:flex;gap:8px"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
      <div class="step"><h3>Tell us the must-haves</h3>
        <div class="field"><label for="lf-what">What exactly do you need?</label><textarea id="lf-what" name="details" required placeholder="e.g. A quiet laptop for spreadsheets and video calls, under 1.5 kg, good keyboard. Or: 3 quotes for rooftop solar for a 2,000 sq ft home."></textarea></div>
        <div class="field"><label>What do you want back?</label><div class="chips">{"".join(f'<label class="chip"><input type="checkbox" name="wants" value="{w}" style="width:auto;margin-right:6px" {"checked" if i == 0 else ""}>{w}</label>' for i, w in enumerate(["One recommendation", "Provider quotes", "A quick call"]))}</div></div>
        <div style="display:flex;gap:8px"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
      <div class="step"><h3>Where should we send your pick?</h3>
        <div class="row2"><div class="field"><label for="lf-name">First name</label><input id="lf-name" name="name" required autocomplete="given-name"></div>
        <div class="field"><label for="lf-email">Email</label><input id="lf-email" type="email" name="email" required autocomplete="email"></div>
        <div class="field"><label for="lf-phone">Phone (optional, for quotes/calls)</label><input id="lf-phone" type="tel" name="phone" autocomplete="tel"></div>
        <div class="field"><label for="lf-loc">Country / region</label><input id="lf-loc" name="location" autocomplete="country-name" placeholder="e.g. Canada, Ontario"></div></div>
        <label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this request. If I asked for quotes, 1Each may share my request with up to 3 relevant providers. <a href="privacy.html">Privacy</a></label>
        <label class="check"><input type="checkbox" name="newsletter" value="yes" checked> Also send me the free weekly 1Each Letter</label>
        <div style="display:flex;gap:8px;margin-top:8px"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="submit" class="btn btn-primary">Send me my 1 pick →</button></div></div>
      <div class="form-msg" role="status"></div>
    </form>
  </div>
  <aside>
    <div class="card" style="margin-bottom:16px"><h3>How it works</h3><ol style="padding-left:18px;margin:0"><li><strong>Tell us</strong> your need and budget (60 sec).</li><li><strong>We research</strong> against our One Pick rules.</li><li><strong>You get one answer</strong> — plus quotes only if you asked.</li></ol></div>
    <div class="card" style="margin-bottom:16px"><h3>Our promise</h3><ul style="padding-left:18px;margin:0"><li>Free for you, always</li><li>No paid rankings</li><li>Never sold to data brokers</li><li>Unsubscribe in one click</li></ul></div>
    <div class="card"><h3>Are you a business?</h3><p class="muted">Receive qualified, opted-in requests in your category.</p><a class="btn btn-ghost btn-sm" href="#partner">Become a provider partner ↓</a></div>
  </aside>
</div></section>
<section id="partner" style="padding-top:0"><div class="container"><div class="card">
  <span class="eyebrow">For providers</span><h2>Get qualified leads from people ready to decide</h2>
  <p class="muted">Insurance, solar, finance, home services, software and retail partners receive opted-in requests that match their service area and category. Pay-per-lead or monthly plans.</p>
  <form class="js-form" data-subject="LEAD: Provider partner application" data-ok="Thanks! Our partnerships team will reply within 2 business days.">{hp()}
    <div class="row2"><div class="field"><label>Company</label><input name="company" required></div><div class="field"><label>Your name</label><input name="name" required></div>
    <div class="field"><label>Work email</label><input type="email" name="email" required></div><div class="field"><label>Category</label><select name="category">{"".join(f"<option>{n}</option>" for _, _, n in needs)}</select></div>
    <div class="field"><label>Service area</label><input name="area" placeholder="Cities, states, countries"></div><div class="field"><label>Monthly lead volume wanted</label><select name="volume"><option>1–25</option><option>25–100</option><option>100–500</option><option>500+</option></select></div></div>
    <button class="btn btn-primary" type="submit">Apply as a partner</button><div class="form-msg" role="status"></div></form>
</div></div></section>
<style>@media (max-width:900px){{#main .container.grid[style*="1.4fr"]{{grid-template-columns:1fr!important}}}}</style>'''))

# ---------------------------------------------------------------- CONTESTS
PAGES.append(dict(file="contests.html", nav="Contests & Prizes", title="Contests & Prizes — Enter Free | 1Each",
  desc="Enter free 1Each contests: share your best money-saving tip, earn bonus entries by referring friends, and win cash prizes.", k="contest giveaway prize win enter",
  body=page_hero("Free to enter", "Contests &amp; prizes", "Share your smartest \"one each\" money tip. Best entries win cash and get featured on 1Each.", "Contests") + f'''
<section style="padding-top:32px"><div class="container grid g2">
  <div class="banner"><span class="eyebrow" style="color:var(--accent)">Now open</span><h2 style="color:#fff" data-contest-name>The Split-It Challenge</h2>
    <p class="muted">Prize: <strong style="color:#fff" data-contest-prize></strong><br>Closes <span data-contest-ends></span></p>
    <div class="countdown" id="countdown" style="margin:16px 0"></div>
    <h3 style="color:#fff">Ways to earn entries</h3><ul class="muted" style="padding-left:18px"><li>Submit a tip — <strong style="color:#fff">1 entry</strong></li><li>Subscribe to the 1Each Letter — <strong style="color:#fff">+1</strong></li><li>Each friend who enters with your link — <strong style="color:#fff">+3</strong></li><li>Share a video tip on YouTube/TikTok tagged #1EachTip — <strong style="color:#fff">+5</strong></li></ul></div>
  <div class="card"><h3>Enter now</h3>
    <form id="ref-form" class="js-form" data-subject="CONTEST entry" data-ok="✅ You're entered! Your personal referral link is below — every friend who enters with it gives you +3 entries.">{hp()}
      <div class="row2"><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input type="email" name="email" required></div></div>
      <div class="field"><label>Your best "one each" money tip</label><textarea name="tip" required maxlength="800" placeholder="e.g. We always split group dinners by items + shared, then tip on pre-tax…"></textarea></div>
      <div class="field"><label>Video link (optional, +5 entries)</label><input type="url" name="video" placeholder="https://"></div>
      <label class="check"><input type="checkbox" name="newsletter" value="yes"> Subscribe me to the 1Each Letter (+1 entry)</label>
      <label class="check"><input type="checkbox" required name="rules" value="accepted"> I'm 18+ (or age of majority) and accept the <a href="#rules">official rules</a>.</label>
      <button class="btn btn-primary btn-block" type="submit">Enter the contest</button><div class="form-msg" role="status"></div></form>
    <div class="card" style="display:none;margin-top:16px;box-shadow:none"><label for="ref-link">Your referral link</label><div style="display:flex;gap:8px"><input id="ref-link" readonly><button class="btn btn-ghost" data-copy="ref-link" type="button">Copy</button></div></div>
  </div>
</div></section>
{ad("inArticle")}
<section style="padding-top:0"><div class="container grid g2">
  <div class="card"><h3>Sponsor a contest</h3><p class="muted">Put your brand on the prize. Contest sponsors get logo placement, a dedicated newsletter mention and opted-in entrant reach.</p><a class="btn btn-primary" href="advertise.html#inquiry">Sponsor a prize</a></div>
  <div class="card"><h3>Past winners</h3><p class="muted">Our first contest is running now — winners will be featured here with their permission.</p></div>
</div></section>
<section id="rules" style="padding-top:0"><div class="container prose"><h2>Official rules (summary)</h2><ol>
<li><strong>No purchase necessary.</strong> A purchase does not improve your chances. Void where prohibited.</li>
<li><strong>Eligibility:</strong> age of majority in your place of residence. Employees of 1Each and immediate family are not eligible.</li>
<li><strong>Entry period:</strong> from publication until the close date shown above. One tip submission per person; bonus entries as listed.</li>
<li><strong>Judging:</strong> winners are chosen on originality (40%), usefulness (40%) and clarity (20%) by the 1Each team. Referral entries are verified; fraudulent or duplicate entries are removed.</li>
<li><strong>Prizes:</strong> as stated above, paid by digital transfer within 30 days of winner verification. Winners are responsible for any taxes. Prizes are non-transferable.</li>
<li><strong>Notification:</strong> winners are notified by email and must respond within 14 days or an alternate is selected.</li>
<li><strong>Licence:</strong> by entering you grant 1Each a non-exclusive licence to publish your tip with credit. You keep ownership.</li>
<li><strong>Privacy:</strong> entrant data is used only to run the contest and, if you opted in, the newsletter. See our <a href="privacy.html">Privacy Policy</a>.</li>
<li>Skill-based contest where required by law (e.g., Canadian entrants may be asked to answer a skill-testing question).</li></ol></div></section>'''))


def tier_cards():
    out = ""
    for n, p, perks, pop in [
        ("Supporter", 3, ["Supporter wall shout-out", "Monthly behind-the-scenes note"], False),
        ("Member", 7, ["Everything in Supporter", "Ad-light experience (coming)", "+2 entries in every contest", "Vote on the next tool"], True),
        ("Patron", 25, ["Everything in Member", "Priority Get-Matched replies", "Name on a tool page", "Quarterly strategy call"], False)]:
        badge = '<span class="badge top">Most popular</span>' if pop else ''
        lis = "".join("<li>" + x + "</li>" for x in perks)
        cls = "btn-primary" if pop else "btn-ghost"
        out += ('<div class="card tier' + (' pop' if pop else '') + '">' + badge + '<h3>' + n + '</h3><div class="price">$' + str(p) +
                '<span class="small muted">/mo</span></div><ul>' + lis + '</ul><button class="btn ' + cls + ' btn-block" data-open="member-modal" '
                'onclick="document.getElementById(\'m-tier\').value=\'' + n + ' ($' + str(p) + '/mo)\'">Join ' + n + '</button></div>')
    return out

# ---------------------------------------------------------------- SUPPORT / DONATE
PAGES.append(dict(file="support.html", nav="Support / Donate", title="Support 1Each — Donate or Become a Member | 1Each",
  desc="Keep 1Each free and independent. One-time or monthly support funds operations, promotion, new tools, hiring talent and contest prizes.", k="donate support membership give fund",
  body=page_hero("Reader-supported", "Keep 1Each free &amp; independent", "No paywalls, no paid rankings. Your support pays for servers and tools, promotion, new writers and developers, and the prizes in our contests.", "Support") + f'''
<section style="padding-top:32px"><div class="container grid g2">
  <div class="card"><h3>Give once</h3>
    <form id="donate-form" class="js-form" data-subject="DONATION pledge" data-ok="Thank you! ❤️ We'll email you a secure payment link within 24 hours.">{hp()}
      <div class="amounts" style="margin-bottom:12px"><button type="button" class="amount" data-v="5">$5</button><button type="button" class="amount sel" data-v="15">$15</button><button type="button" class="amount" data-v="50">$50</button><button type="button" class="amount" data-v="100">$100</button></div>
      <div class="row2"><div class="field"><label for="d-amount">Amount</label><input id="d-amount" name="amount" type="number" min="1" value="15" required></div>
      <div class="field"><label>Direct it to</label><select name="fund"><option>Where it's needed most</option><option>Operations</option><option>Promotion &amp; marketing</option><option>Hiring writers &amp; developers</option><option>Contest prizes</option></select></div>
      <div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input type="email" name="email" required></div></div>
      <div class="field"><label>Message (optional)</label><input name="message" maxlength="200" placeholder="Say something nice — we may feature it"></div>
      <label class="check"><input type="checkbox" name="public" value="yes"> Show my first name on the supporter wall</label>
      <button class="btn btn-primary btn-block" type="submit">♥ Pledge support</button><div class="form-msg" role="status"></div></form>
    <p class="small muted" style="margin-top:14px">Pay instantly:</p><div id="donate-links" class="cta-row" style="margin-top:0"></div>
    <p class="form-note">1Each is not a registered charity; contributions are not tax-deductible.</p>
  </div>
  <div>
    <div class="card" style="margin-bottom:16px"><h3>Where your money goes</h3>
      <div class="alloc"><span>Operations &amp; tools</span><div class="bar"><i style="width:35%"></i></div><b>35%</b></div>
      <div class="alloc"><span>Content &amp; hiring</span><div class="bar"><i style="width:30%"></i></div><b>30%</b></div>
      <div class="alloc"><span>Marketing &amp; promotion</span><div class="bar"><i style="width:20%"></i></div><b>20%</b></div>
      <div class="alloc"><span>Contests &amp; prizes</span><div class="bar"><i style="width:15%"></i></div><b>15%</b></div>
      <p class="small muted">Target allocation. We publish a short transparency note each quarter.</p></div>
    <div class="card"><h3>Supporter wall</h3><p class="muted">Be the first name here. 💜</p></div>
  </div>
</div></section>
<section id="members" style="padding-top:0"><div class="container"><h2 class="center">Or join monthly</h2><div class="grid g3">
  {tier_cards()}
</div></div></section>
<div class="modal" id="member-modal" role="dialog" aria-modal="true" aria-label="Join"><div class="box"><button class="icon-btn close" aria-label="Close">✕</button>
<h3>Join as a monthly supporter</h3><form class="js-form" data-subject="MEMBERSHIP request" data-ok="Welcome aboard! We'll email your secure subscription link shortly.">{hp()}
<div class="field"><label>Tier</label><input id="m-tier" name="tier" readonly></div><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input type="email" name="email" required></div>
<button class="btn btn-primary btn-block" type="submit">Request my link</button><div class="form-msg" role="status"></div></form></div></div>
<section style="padding-top:0"><div class="container"><div class="card"><h3>Other ways to help</h3><div class="grid g3" style="margin-top:8px">
<div><strong>Share a tool</strong><p class="muted small">Send the split calculator to your group chat.</p><button class="btn btn-ghost btn-sm" data-share>Share 1Each</button></div>
<div><strong>Sponsor a prize</strong><p class="muted small">Businesses can fund contest prizes.</p><a class="btn btn-ghost btn-sm" href="advertise.html">Sponsor</a></div>
<div><strong>Contribute</strong><p class="muted small">Write, film, design or code with us.</p><a class="btn btn-ghost btn-sm" href="careers.html">Join the team</a></div></div></div></div></section>'''))

# ---------------------------------------------------------------- CAREERS
roles = [("Freelance Buying-Guide Writer", "Remote · Per article", "Write One Pick guides with clear rules and checklists. Consumer, tech or finance background preferred."),
         ("YouTube Shorts Creator / Editor", "Remote · Per video", "Script, shoot or edit 30–60 second money-smart videos for each tool."),
         ("SEO & Growth Marketer", "Remote · Part-time", "Own keyword strategy, internal linking, and partnerships for 1Each's tools and guides."),
         ("Front-end Developer (JS)", "Remote · Contract", "Build new calculators in vanilla JS — fast, accessible and mobile-first."),
         ("Partnerships & Ad Sales", "Remote · Commission", "Sell sponsorships, contest prizes and lead-gen partnerships."),
         ("Community & Contest Manager", "Remote · Part-time", "Run contests, verify entries, and grow our newsletter community.")]

def role_cards():
    q = "'"
    return "".join('<div class="card"><span class="badge">' + m + '</span><h3 style="margin-top:10px">' + t + '</h3><p class="muted">' + d +
        '</p><a class="btn btn-primary btn-sm" href="#apply" onclick="document.getElementById(' + q + 'c-role' + q + ').value=' + q + t + q + '">Apply →</a></div>' for t, m, d in roles)
PAGES.append(dict(file="careers.html", nav="Careers & Talent", title="Careers — Write, Create & Build With 1Each | 1Each",
  desc="Join 1Each as a writer, video creator, developer, marketer or partnerships lead. Remote, flexible roles and a talent network.", k="jobs hiring careers talent freelance work",
  body=page_hero("We're hiring · Remote", "Build the one-answer internet with us", "Flexible, remote roles for writers, creators, developers and growth people. Not the right role? Join the talent network.", "Careers") + f'''
<section style="padding-top:32px"><div class="container"><div class="grid g2">
{role_cards()}
</div></div></section>
<section id="apply" style="padding-top:0"><div class="container grid" style="grid-template-columns:minmax(0,1.3fr) minmax(0,.9fr);gap:24px">
  <div class="card"><h2>Apply / join the talent network</h2>
  <form class="js-form" data-subject="CAREERS application" data-ok="Application received! If there's a fit, we'll reach out within 7 days.">{hp()}
    <div class="row2"><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input type="email" name="email" required></div>
    <div class="field"><label for="c-role">Role</label><select id="c-role" name="role">{"".join(f"<option>{t}</option>" for t, _, _ in roles)}<option>Talent network (general)</option></select></div>
    <div class="field"><label>Location / time zone</label><input name="location"></div>
    <div class="field"><label>Portfolio / LinkedIn / GitHub</label><input type="url" name="portfolio" required placeholder="https://"></div><div class="field"><label>Rate or salary expectation</label><input name="rate"></div></div>
    <div class="field"><label>Why you, in 3 sentences</label><textarea name="pitch" required maxlength="1200"></textarea></div>
    <button class="btn btn-primary" type="submit">Submit application</button><div class="form-msg" role="status"></div></form></div>
  <aside><div class="card" style="margin-bottom:16px"><h3>How we work</h3><ul style="padding-left:18px;margin:0"><li>Async, remote-first</li><li>Paid per deliverable or monthly</li><li>Your byline on your work</li><li>Fast feedback, clear briefs</li></ul></div>
  <div class="card"><h3>Hiring for your team?</h3><p class="muted">Post a role to our talent network and newsletter audience.</p><a class="btn btn-ghost btn-sm" href="advertise.html#inquiry">Post a job</a></div></aside>
</div></section>
<style>@media (max-width:900px){{#apply .container{{grid-template-columns:1fr!important}}}}</style>'''))

# ---------------------------------------------------------------- ADVERTISE
PAGES.append(dict(file="advertise.html", nav="Advertise & Sponsor", title="Advertise, Sponsor & Partner With 1Each | 1Each",
  desc="Reach people at the moment they decide. Display, tool sponsorships, newsletter, video integrations, contest prizes and lead-gen partnerships.", k="advertise sponsor partnership media kit ads",
  body=page_hero("Media kit", "Reach people at the moment they decide", "1Each audiences arrive with intent — splitting a bill, comparing prices, choosing what to buy. Put your brand right there, clearly labelled and brand-safe.", "Advertise") + f'''
<section style="padding-top:32px"><div class="container">
  <div class="stats card"><div class="stat"><b>6</b>high-intent tools</div><div class="stat"><b>18+</b>buying guides</div><div class="stat"><b>12</b>lead categories</div><div class="stat"><b>100%</b>labelled sponsors</div></div>
</div></section>
<section id="packages" style="padding-top:0"><div class="container"><h2>Packages</h2><div class="table-wrap"><table class="cmp">
<tr><th>Placement</th><th>What you get</th><th>Best for</th><th>From</th></tr>
<tr><td><strong>Tool sponsorship</strong></td><td>"Presented by" on a calculator + logo in results</td><td>Fintech, banks, payment apps</td><td>$499 / mo</td></tr>
<tr><td><strong>Guide sponsorship</strong></td><td>Labelled sponsor slot in a One Pick guide category</td><td>Retail, DTC brands</td><td>$299 / mo</td></tr>
<tr><td><strong>Newsletter</strong></td><td>Primary sponsor slot in the weekly 1Each Letter</td><td>Any consumer brand</td><td>$149 / issue</td></tr>
<tr><td><strong>Video integration</strong></td><td>60-sec integrated read in a YouTube tutorial</td><td>Apps, services</td><td>$399 / video</td></tr>
<tr><td><strong>Contest prize</strong></td><td>Brand the prize; logo, rules mention, entrant reach</td><td>Launches, awareness</td><td>Prize + $199</td></tr>
<tr><td><strong>Lead-gen partner</strong></td><td>Opted-in requests in your category &amp; area</td><td>Insurance, solar, finance, services</td><td>Per lead</td></tr>
<tr><td><strong>Domain / site acquisition</strong></td><td>Acquire or partner on 1Each.com itself</td><td>Investors, operators</td><td><a href="https://web.works/contact" target="_blank" rel="noopener">Inquire</a></td></tr>
</table></div><p class="small muted">Rates are starting points; custom bundles available. We don't sell rankings or reviews.</p></div></section>
{ad("inArticle")}
<section id="inquiry" style="padding-top:0"><div class="container grid" style="grid-template-columns:minmax(0,1.3fr) minmax(0,.9fr);gap:24px">
  <div class="card"><h2>Advertising / sponsorship inquiry</h2>
  <form class="js-form" data-subject="ADVERTISING / SPONSORSHIP inquiry" data-ok="Thanks! Media kit and availability are on the way within 1 business day.">{hp()}
    <div class="row2"><div class="field"><label>Company</label><input name="company" required></div><div class="field"><label>Name</label><input name="name" required></div>
    <div class="field"><label>Work email</label><input type="email" name="email" required></div><div class="field"><label>Website</label><input type="url" name="website" placeholder="https://"></div>
    <div class="field"><label>Interested in</label><select name="interest"><option>Tool sponsorship</option><option>Guide sponsorship</option><option>Newsletter</option><option>Video integration</option><option>Contest prize</option><option>Lead-gen partnership</option><option>Job post</option><option>Website / domain acquisition</option><option>Partnership (other)</option></select></div>
    <div class="field"><label>Monthly budget</label><select name="budget"><option>Under $500</option><option>$500–2,000</option><option>$2,000–10,000</option><option>$10,000+</option></select></div></div>
    <div class="field"><label>Goals &amp; timing</label><textarea name="message" required></textarea></div>
    <button class="btn btn-primary" type="submit">Request media kit</button><div class="form-msg" role="status"></div></form></div>
  <aside><div class="card" style="margin-bottom:16px"><h3>Brand safety</h3><ul style="padding-left:18px;margin:0"><li>All sponsored content labelled</li><li>No paid rankings or fake reviews</li><li>Consent-based ads &amp; analytics</li></ul></div>
  <div class="card"><h3>Buy or partner on this website</h3><p class="muted">Interested in the 1Each.com domain or site?</p><a class="btn btn-accent btn-sm" href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div></aside>
</div></section>
<style>@media (max-width:900px){{#inquiry .container{{grid-template-columns:1fr!important}}}}</style>'''))

# ---------------------------------------------------------------- ABOUT
PAGES.append(dict(file="about.html", nav="About 1Each", title="About 1Each — How We Choose & How We're Paid | 1Each",
  desc="Our mission, how we choose the one pick, editorial standards, and exactly how 1Each makes money.", k="about mission editorial how we choose how we are paid",
  body=page_hero("About", "One clear answer for each decision", "Decision fatigue is real. 1Each exists to cut every choice down to the one answer that matters — and to show our work.", "About") + '''
<section><div class="container prose">
<h2 id="how-we-choose">How we choose</h2><ol><li><strong>One rule first.</strong> Every category starts with the single rule that eliminates most bad options.</li><li><strong>Must-have checklist.</strong> 4–6 criteria, drawn from standards, specifications and consumer-protection guidance.</li><li><strong>Three honest price points.</strong> Budget, top pick and upgrade — so "best" fits your wallet.</li><li><strong>Show the math.</strong> Every tool prints its formula.</li><li><strong>Update.</strong> Guides are reviewed regularly and dated when changed.</li></ol>
<h2 id="how-we-are-paid">How we're paid</h2><p>1Each is free. We earn from display advertising (such as Google AdSense), affiliate commissions when you buy through some links, clearly-labelled sponsorships, lead-generation partnerships (only when you ask for quotes), and reader support. None of these affect our picks — rankings are never for sale.</p>
<h2>Editorial standards</h2><ul><li>Sponsored content is always labelled "Sponsored".</li><li>We never publish fake reviews or invented testimonials.</li><li>Corrections are made promptly and noted.</li><li>Guides are general information — not financial, legal or medical advice.</li></ul>
<h2>Contact</h2><p>Questions, corrections or partnership ideas? <a href="contact.html">Contact us</a>. Interested in this website or domain? <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p>
</div></section>'''))

# ---------------------------------------------------------------- CONTACT
PAGES.append(dict(file="contact.html", nav="Contact", title="Contact 1Each | 1Each",
  desc="Contact 1Each for questions, corrections, partnerships, advertising or press. We reply within 2 business days.", k="contact email message support",
  body=page_hero("Contact", "Talk to us", "Questions, corrections, partnerships, press — send a message and we'll reply within 2 business days.", "Contact") + f'''
<section style="padding-top:32px"><div class="container grid" style="grid-template-columns:minmax(0,1.3fr) minmax(0,.9fr);gap:24px">
  <div class="card"><form class="js-form" data-subject="CONTACT message" data-ok="Message sent! We'll reply within 2 business days.">{hp()}
    <div class="row2"><div class="field"><label>Name</label><input name="name" required></div><div class="field"><label>Email</label><input type="email" name="email" required></div></div>
    <div class="field"><label>Topic</label><select name="topic"><option>General question</option><option>Correction</option><option>Partnership</option><option>Advertising / sponsorship</option><option>Website / domain acquisition</option><option>Press</option><option>Privacy request</option></select></div>
    <div class="field"><label>Message</label><textarea name="message" required></textarea></div>
    <button class="btn btn-primary" type="submit">Send message</button><div class="form-msg" role="status"></div></form></div>
  <aside><div class="card" style="margin-bottom:16px"><h3>Quick routes</h3><ul style="padding-left:18px;margin:0"><li><a href="get-matched.html">Personal pick request</a></li><li><a href="advertise.html#inquiry">Advertising &amp; sponsorship</a></li><li><a href="careers.html#apply">Careers</a></li><li><a href="support.html">Donations</a></li></ul></div>
  <div class="card"><h3>Website, domain or partnership</h3><p class="muted">Interested in acquiring or partnering on 1Each.com?</p><a class="btn btn-accent btn-sm" href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>
  <p class="small muted" style="margin-top:12px">Prefer email? <a href="#" data-mail="1Each inquiry">Open your email app</a>.</p></div></aside>
</div></section>
<style>@media (max-width:900px){{#main .container.grid[style*="1.3fr"]{{grid-template-columns:1fr!important}}}}</style>'''))

# ---------------------------------------------------------------- LEGAL
def legal(file, nav, title, desc, html):
    PAGES.append(dict(file=file, nav=nav, title=f"{title} | 1Each", desc=desc, k="legal",
        body=page_hero("Legal", title, "Last updated: September 28, 2026", title) + f'<section><div class="container prose">{html}</div></section>'))

legal("privacy.html", "Privacy Policy", "Privacy Policy", "How 1Each collects, uses and protects your information.", '''
<p>This policy explains what information 1Each.com ("1Each", "we") collects and how it is used.</p>
<h2>What we collect</h2><ul><li><strong>Information you give us</strong> through forms (name, email, optional phone, your request, messages, contest entries, applications, pledges).</li><li><strong>Tool inputs</strong> — calculator entries are processed in your browser and are not sent to us.</li><li><strong>Usage data</strong> — only if you accept analytics cookies (e.g., Google Analytics).</li><li><strong>Advertising data</strong> — third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites.</li></ul>
<h2>How we use it</h2><ul><li>To reply to you and deliver what you asked for (e.g., your personal pick).</li><li>If you request quotes, to share your request with up to 3 relevant providers — only with your consent.</li><li>To run contests and, if you opt in, send our newsletter.</li><li>To keep the site secure and improve it.</li></ul>
<h2>Advertising (Google AdSense)</h2><p>Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this and other sites. You can opt out of personalised advertising at Google's Ads Settings or at aboutads.info. In the EEA/UK, ads cookies load only after consent.</p>
<h2>Form processing</h2><p>Forms are delivered via a third-party form-forwarding service (FormSubmit) to our private inbox. We don't sell personal information.</p>
<h2>Your rights</h2><p>You may request access, correction or deletion of your data, withdraw consent, or unsubscribe at any time via our <a href="contact.html">contact form</a> (topic: Privacy request). Residents of the EU/UK (GDPR), California (CCPA/CPRA) and Canada (PIPEDA) have additional rights, which we honour.</p>
<h2>Retention &amp; security</h2><p>We keep form data only as long as needed for the purpose collected, typically up to 24 months, then delete it.</p>
<h2>Children</h2><p>1Each is not directed to children under 13 (or 16 in the EEA), and we do not knowingly collect their data.</p>
<h2>Changes</h2><p>We'll post updates here with a new date.</p>''')

legal("terms.html", "Terms of Use", "Terms of Use", "Terms governing your use of 1Each.com.", '''
<p>By using 1Each.com you agree to these terms.</p>
<h2>Information only</h2><p>Guides, tools and videos are general information and estimates. They are not financial, legal, tax, medical or professional advice. Verify important decisions with a qualified professional.</p>
<h2>Calculators</h2><p>Tools are provided "as is" without warranty of accuracy or fitness for a particular purpose. You are responsible for checking results.</p>
<h2>Third parties</h2><p>We link to third-party sites, sellers and providers. We're not responsible for their products, services, prices or policies.</p>
<h2>User submissions</h2><p>By submitting tips, contest entries or other content you grant 1Each a non-exclusive, royalty-free licence to publish it with credit. Don't submit anything unlawful or that infringes others' rights.</p>
<h2>Intellectual property</h2><p>The site's original text, tools, code and design are protected by copyright. You may share links and short quotes with attribution. See our <a href="disclosure.html">trademark &amp; copyright disclosure</a>.</p>
<h2>Limitation of liability</h2><p>To the fullest extent permitted by law, 1Each is not liable for indirect or consequential losses arising from use of the site.</p>
<h2>Changes</h2><p>We may update these terms; continued use means acceptance.</p>''')

legal("disclosure.html", "Affiliate, Trademark & Copyright Disclosure", "Affiliate, Trademark &amp; Copyright Disclosure", "1Each's affiliate, advertising, trademark and copyright disclosures.", '''
<h2>Trademark disclosure</h2><p>"1Each" is used on this website as a descriptive name meaning "one each" — one answer for each decision. 1Each.com is an independent website. It is <strong>not affiliated with, endorsed by, sponsored by, or connected to</strong> any company, product, app, or trademark owner that uses the names "1Each", "One Each", "OneEach", "1 Each" or any similar name, in any jurisdiction. No claim is made to any third party's trademark. If you believe any content on this site infringes your trademark, please <a href="contact.html">contact us</a> and we will review it promptly.</p>
<p>All product names, brands, logos and trademarks mentioned on this site are the property of their respective owners and are used for identification and descriptive purposes only (nominative fair use). Their mention does not imply endorsement.</p>
<h2>Copyright notice</h2><p>© 2026 1Each.com. All original text, calculators, source code, graphics and page designs are protected by copyright. Icons are standard Unicode emoji rendered by your device. Fonts (Inter, Space Grotesk) are used under the SIL Open Font License via Google Fonts. Embedded YouTube videos remain the property of their creators and are shown via YouTube's official embed player under YouTube's Terms of Service.</p>
<h2>Copyright complaints (DMCA)</h2><p>If you believe content here infringes your copyright, send a notice via our <a href="contact.html">contact form</a> including: identification of the work, the URL of the material, your contact details, a good-faith statement, and a statement under penalty of perjury that you are authorised to act. We will respond promptly and remove infringing material.</p>
<h2>Affiliate disclosure</h2><p>Some links on 1Each are affiliate links. If you buy through them we may earn a commission at no extra cost to you. Commissions never influence which option we pick. (FTC 16 CFR Part 255 and equivalent rules.)</p>
<h2>Advertising disclosure</h2><p>We display ads, including Google AdSense. Sponsored placements are always labelled "Sponsored" or "Advertisement". Sponsors cannot buy rankings or editorial conclusions.</p>
<h2>Lead generation disclosure</h2><p>If you ask for provider quotes through Get Matched, we may be compensated by providers for introductions. We only share your request with your consent.</p>
<h2>Not professional advice</h2><p>Content is general information, not financial, legal, tax or medical advice.</p>''')

legal("cookies.html", "Cookie Policy", "Cookie Policy", "How 1Each uses cookies and local storage.", '''
<h2>Essential storage</h2><p>We store small preferences in your browser (theme, currency, cookie choice, contest referral code). These never leave your device.</p>
<h2>Analytics (optional)</h2><p>With your consent we load Google Analytics 4 to understand which tools are useful. IP anonymisation is enabled.</p>
<h2>Advertising</h2><p>Google and its partners may use cookies to serve and measure ads. In the EEA/UK a certified consent platform will govern personalised ads. You can opt out of personalised ads in Google Ads Settings.</p>
<h2>Change your choice</h2><p><button class="btn btn-ghost btn-sm" onclick="try{localStorage.removeItem('consent')}catch(e){};location.reload()">Reset cookie choice</button></p>''')

# ---------------------------------------------------------------- 404
PAGES.append(dict(file="404.html", nav="Not found", title="Page not found | 1Each", desc="This page doesn't exist.", robots="noindex",
  body='''<section class="hero"><div class="container center"><h1>404 — no pick here.</h1><p class="lead" style="margin:0 auto">But we have one answer for each of these:</p>
<div class="cta-row" style="justify-content:center"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="tools.html">Tools</a><a class="btn btn-ghost" href="picks.html">Guides</a></div></div></section>'''))
