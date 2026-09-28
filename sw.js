/* 1Each offline cache: tools keep working without a connection */
const CACHE = "1each-v1";
const CORE = ["./", "index.html", "tools.html", "split-bill.html", "unit-price.html", "cost-per-use.html", "tip-calculator.html", "trip-splitter.html", "subscription-audit.html", "assets/css/style.css", "assets/js/app.js", "assets/js/tools.js", "assets/js/config.js", "assets/js/picks.js", "assets/js/search-index.js", "assets/img/favicon.svg"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).catch(() => {})); self.skipWaiting(); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); });
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(r => { const c = r.clone(); caches.open(CACHE).then(x => x.put(e.request, c)); return r; }).catch(() => caches.match(e.request, { ignoreSearch: true })));
});
