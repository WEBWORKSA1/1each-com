/* 1Each.com — site configuration. Edit values here; no build step needed. */
window.SITE_CONFIG = {
  siteName: "1Each",
  domain: "1each.com",
  // Inquiry link shown in the top bar on every page
  interestUrl: "https://web.works/contact",

  // Contact address is stored obfuscated (reversed + base64) and is only
  // assembled in the browser at the moment a form is sent or a contact link is clicked.
  // It is never printed on any page. Do not replace with a plain address.
  _c: "bW9jLmxpYW1nQDFhc2tyb3diZXc=",
  // Optional: after the first FormSubmit activation, FormSubmit gives you a random
  // alias string. Paste it here to avoid using the address at all in form endpoints.
  formAlias: "",

  // Google AdSense — paste your publisher id (e.g. "ca-pub-1234567890123456").
  // Leave empty to show "Advertise here" house placeholders instead of ads.
  adsenseClient: "",
  adSlots: { top: "", inArticle: "", sidebar: "", footer: "" },

  // Google Analytics 4 measurement id (e.g. "G-XXXXXXX"). Loaded only after cookie consent.
  ga4: "",

  // YouTube
  youtubeChannel: "https://www.youtube.com/results?search_query=1Each",
  // Add real video IDs to embed them. Empty IDs render a "watch on YouTube" search card.
  videos: [
    { id: "", title: "How to split any bill fairly in 30 seconds", q: "how to split a restaurant bill fairly with tip and tax" },
    { id: "", title: "Unit price: the 1 number that beats every sale sign", q: "how to compare unit price grocery shopping" },
    { id: "", title: "Cost-per-use: when the expensive one is cheaper", q: "cost per use explained buy once cry once" },
    { id: "", title: "Group trip money: settle up with the fewest transfers", q: "how to split group trip expenses settle up" },
    { id: "", title: "Subscription audit: find $500 a year you forgot", q: "subscription audit save money cancel subscriptions" },
    { id: "", title: "Tipping guide: what's fair, each time", q: "how much to tip guide" }
  ],

  // Donation / support links — add your own account URLs (leave "" to hide a button).
  donate: {
    kofi: "",            // e.g. https://ko-fi.com/yourname
    buymeacoffee: "",    // e.g. https://buymeacoffee.com/yourname
    paypal: "",          // e.g. https://paypal.me/yourname
    githubSponsors: "",  // e.g. https://github.com/sponsors/yourname
    stripe: ""           // e.g. a Stripe Payment Link
  },

  // Active contest (edit dates/prize)
  contest: {
    name: "The Split-It Challenge",
    prize: "$250 prize pool (1st $150 · 2nd $70 · 3rd $30)",
    ends: "2026-12-31T23:59:59-05:00"
  },

  social: { x: "", instagram: "", tiktok: "", facebook: "", linkedin: "", pinterest: "" }
};
