/* 1Each.com — "One Pick" decision guides. Add a guide = add an object. */
window.PICKS = [
  { c: "Home", i: "🛏️", t: "The 1 mattress rule", r: "Pick the firmness for your sleep position — not the brand.",
    l: ["Side sleepers: medium-soft; back: medium; stomach: medium-firm", "Insist on a 100+ night trial and free returns", "Hybrid if you sleep hot or weigh 230 lb+ / 105 kg+", "Ignore 'luxury' layers you can't feel in the store"],
    b: { budget: "All-foam, 10-inch, with 100-night trial", top: "Mid-priced hybrid with zoned support", upgrade: "Latex hybrid — longest lifespan per dollar" }, need: "home" },
  { c: "Home", i: "🧹", t: "The 1 vacuum rule", r: "Buy for your floors and pets, not for peak suction numbers.",
    l: ["Pets or long hair: tangle-free brush roll", "Mostly hard floors: lightweight cordless", "Allergies: sealed system + HEPA", "Check the price of replacement batteries first"],
    b: { budget: "Corded upright with HEPA", top: "Cordless stick with swappable battery", upgrade: "Robot + self-empty dock for daily upkeep" }, need: "home" },
  { c: "Kitchen", i: "🍳", t: "The 1 pan you actually need", r: "A 12-inch stainless tri-ply skillet does 80% of cooking.",
    l: ["Fully clad tri-ply, not just a disc bottom", "Oven-safe handle to 500°F / 260°C", "Add one nonstick only for eggs", "Weight 2.5–3.5 lb — heavy enough to sear"],
    b: { budget: "Disc-bottom stainless 12\"", top: "Fully clad tri-ply 12\"", upgrade: "5-ply clad — even heat, lifetime warranty" }, need: "kitchen" },
  { c: "Kitchen", i: "☕", t: "The 1 coffee setup rule", r: "The grinder matters more than the brewer.",
    l: ["Burr grinder over blade — always", "Cost per cup under pods within ~4 months", "Pour-over or drip with a certified brew temperature", "Descale monthly to keep flavor"],
    b: { budget: "Manual burr grinder + pour-over cone", top: "Electric burr + certified drip brewer", upgrade: "Espresso machine with built-in PID" }, need: "kitchen" },
  { c: "Tech", i: "💻", t: "The 1 laptop rule", r: "Buy the RAM and battery you'll need in year 4, not day 1.",
    l: ["16 GB RAM minimum in 2026", "SSD 512 GB+; don't pay for 2 TB you won't use", "10+ hr real-world battery", "A keyboard and screen you'll touch 20,000 times"],
    b: { budget: "Midrange 14\" with 16 GB / 512 GB", top: "Thin-and-light with all-day battery", upgrade: "Pro 16\" if you edit video or code heavily" }, need: "tech" },
  { c: "Tech", i: "🎧", t: "The 1 headphones rule", r: "Match the fit to where you listen most.",
    l: ["Commute/flights: over-ear ANC", "Workouts: earbuds with ear-hooks, IPX4+", "Calls: multi-mic beamforming", "Multipoint Bluetooth for laptop + phone"],
    b: { budget: "ANC earbuds with app EQ", top: "Over-ear ANC, 30-hr battery", upgrade: "Flagship ANC with lossless support" }, need: "tech" },
  { c: "Tech", i: "📱", t: "The 1 phone plan rule", r: "Pay for the data you use in your worst month — not your best.",
    l: ["Check 3 months of usage before switching", "Prepaid/MVNO on the same towers costs less", "Bundle only if every line is used", "Unlocked phone = freedom to switch any month"],
    b: { budget: "Prepaid MVNO, 10–15 GB", top: "Postpaid with hotspot", upgrade: "Family unlimited with international roaming" }, need: "money" },
  { c: "Money", i: "💳", t: "The 1 credit card rule", r: "Choose one card whose rewards match your top spending category.",
    l: ["Never carry a balance — interest erases rewards", "No annual fee unless perks beat it 2×", "Flat 2% beats rotating categories for most people", "Check foreign transaction fees if you travel"],
    b: { budget: "No-fee flat cashback card", top: "Category card matching your #1 spend", upgrade: "Premium travel card if you travel 4+ times a year" }, need: "money" },
  { c: "Money", i: "🏦", t: "The 1 savings account rule", r: "Your emergency fund belongs in the highest insured yield — nowhere else.",
    l: ["Government-insured deposits only", "No monthly fees or minimums", "Transfers settle in 1–2 days", "3–6 months of expenses, then invest the rest"],
    b: { budget: "Online high-yield savings", top: "HYSA + round-up automation", upgrade: "Treasury/T-bill ladder for larger balances" }, need: "money" },
  { c: "Money", i: "🛡️", t: "The 1 insurance rule", r: "Insure the losses you can't afford; self-insure the rest.",
    l: ["Raise deductibles to cut premiums", "Term life over whole life for most families", "Compare 3 quotes every renewal", "Bundle home + auto only when cheaper in writing"],
    b: { budget: "State-minimum + emergency fund", top: "Higher deductible, full liability", upgrade: "Umbrella policy once net worth grows" }, need: "insurance" },
  { c: "Travel", i: "🧳", t: "The 1 carry-on rule", r: "One carry-on that fits every airline sizer beats a bigger bag.",
    l: ["Max 22 × 14 × 9 in / 55 × 35 × 23 cm", "Spinner wheels for airports, 2 wheels for cobblestones", "Front laptop pocket saves security time", "Under 7 lb / 3.2 kg empty"],
    b: { budget: "Hardshell spinner, lifetime warranty", top: "Polycarbonate with compression", upgrade: "Aluminum or premium soft-side with repair program" }, need: "travel" },
  { c: "Travel", i: "✈️", t: "The 1 flight booking rule", r: "Set alerts early; book when the price hits your target — don't wait for a miracle.",
    l: ["Domestic: 1–3 months out; international: 2–8", "Compare total price incl. bags and seats", "Use free 24-hour cancellation windows", "Flexible dates beat flexible airports"],
    b: { budget: "Basic economy + personal item", top: "Main cabin with free changes", upgrade: "Premium economy on flights over 7 hours" }, need: "travel" },
  { c: "Health", i: "🏃", t: "The 1 running shoe rule", r: "Comfort on the first run is the best predictor — fit beats tech.",
    l: ["Thumb-width of space at the toe", "Replace every 300–500 mi / 500–800 km", "Match cushion to distance, not ads", "Buy late in the day when feet are largest"],
    b: { budget: "Last season's version of a daily trainer", top: "Current daily trainer", upgrade: "Plated shoe only for race day" }, need: "health" },
  { c: "Health", i: "💤", t: "The 1 sleep upgrade rule", r: "Fix light and temperature before buying gadgets.",
    l: ["Blackout curtains or eye mask", "Room at 60–67°F / 16–19°C", "Same wake time 7 days a week", "Screens off 30–60 min before bed"],
    b: { budget: "Eye mask + earplugs", top: "Blackout curtains + fan", upgrade: "Cooling mattress topper" }, need: "health" },
  { c: "Software", i: "🤖", t: "The 1 AI assistant rule", r: "Pick the assistant that fits the work you do most — then learn it deeply.",
    l: ["Writing and analysis: strongest reasoning model", "Coding: best IDE integration", "Privacy: business plan with no training on your data", "One paid plan beats three free ones"],
    b: { budget: "Free tier + good prompts", top: "One paid pro plan", upgrade: "Team plan with shared workspaces" }, need: "software" },
  { c: "Software", i: "🌐", t: "The 1 website builder rule", r: "Static for speed and cost; CMS only when non-coders publish weekly.",
    l: ["Free hosting on static hosts for simple sites", "Own your domain at a separate registrar", "Page speed under 2 seconds on mobile", "Export your content — avoid lock-in"],
    b: { budget: "Static site + free hosting", top: "Hosted CMS with custom domain", upgrade: "Headless CMS + CDN" }, need: "business" },
  { c: "Kids", i: "🧸", t: "The 1 toy rule", r: "Open-ended toys get played with 10× longer than single-trick toys.",
    l: ["Blocks, art supplies, pretend play beat light-up toys", "Check age grading and small-parts warnings", "Rotate toys instead of buying new", "Buy one quality item over five cheap ones"],
    b: { budget: "Wooden blocks set", top: "Magnetic tiles", upgrade: "Modular construction system" }, need: "family" },
  { c: "Home", i: "🔌", t: "The 1 energy bill rule", r: "Heating and cooling are about half the bill — start there.",
    l: ["Smart thermostat with schedules", "Seal drafts and add attic insulation", "LEDs everywhere (the easy 5%)", "Get 3 solar quotes before you commit"],
    b: { budget: "Weatherstripping + LEDs", top: "Smart thermostat", upgrade: "Heat pump or solar (with incentives)" }, need: "solar" }
];
(function () {
  var grid = document.getElementById("picks-grid"); if (!grid) return;
  var lim = parseInt(grid.getAttribute("data-limit") || "999", 10), filterWrap = document.getElementById("pick-filters"), q = document.getElementById("pick-q"), active = "All";
  function card(p) {
    return '<article class="card pick reveal in"><div class="meta"><span class="badge">' + p.c + '</span></div><div class="ico" aria-hidden="true">' + p.i + "</div><h3>" + p.t + '</h3><div class="rule">' + p.r + "</div><ul>" + p.l.map(function (x) { return "<li>" + x + "</li>"; }).join("") + "</ul>" +
      '<p class="small"><span class="badge budget">Budget</span> ' + p.b.budget + '<br><span class="badge top">Top pick</span> ' + p.b.top + '<br><span class="badge upgrade">Upgrade</span> ' + p.b.upgrade + "</p>" +
      '<div class="foot"><a class="btn btn-primary btn-sm" href="get-matched.html?need=' + p.need + '">Get my 1 pick →</a><button class="btn btn-ghost btn-sm" data-share>Share</button></div></article>';
  }
  function render() {
    var s = q ? q.value.trim().toLowerCase() : "";
    var list = window.PICKS.filter(function (p) { return (active === "All" || p.c === active) && (!s || (p.t + p.r + p.l.join(" ")).toLowerCase().indexOf(s) > -1); }).slice(0, lim);
    grid.innerHTML = list.length ? list.map(card).join("") : '<p class="muted">No guide yet — <a href="get-matched.html">ask us for your 1 pick</a>.</p>';
    Array.prototype.forEach.call(grid.querySelectorAll("[data-share]"), function (b) { b.onclick = function () { var u = location.href; if (navigator.share) navigator.share({ title: "1Each", url: u }).catch(function () {}); else if (navigator.clipboard) navigator.clipboard.writeText(u).then(function () { window.OneEach && OneEach.toast("Link copied"); }); }; });
  }
  if (filterWrap) {
    var cats = ["All"].concat(window.PICKS.map(function (p) { return p.c; }).filter(function (v, i, a) { return a.indexOf(v) === i; }));
    filterWrap.innerHTML = cats.map(function (c) { return '<button class="chip' + (c === "All" ? " active" : "") + '" data-c="' + c + '">' + c + "</button>"; }).join("");
    filterWrap.addEventListener("click", function (e) { var b = e.target.closest(".chip"); if (!b) return; active = b.getAttribute("data-c"); Array.prototype.forEach.call(filterWrap.children, function (x) { x.classList.toggle("active", x === b); }); render(); });
  }
  if (q) q.addEventListener("input", render);
  render();
})();
