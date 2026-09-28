# 1Each.com: phased build prompt

Copy one phase at a time into an AI builder. Each phase builds on the one before it. The current repo is the finished result of Phases 1–7. Phases 8–10 are for growth.

---

## The concept

**1Each: one smart answer for each decision.**
Three parts, all built around the word "each":

1. **Fair split.** "$37.88 each." Calculators for splitting bills, trips and shared costs.
2. **True cost of each option.** Unit price, cost per use, subscription audit.
3. **The one pick.** For each purchase: one decision rule, a checklist, and a budget, top and upgrade pick.

**Why this concept makes money:**
- Calculators bring in steady search and repeat traffic, with little competition from big media sites.
- Buying guides earn affiliate commissions.
- Money and insurance topics pay some of the highest AdSense rates.
- Lead generation (the "Get Matched" form) sells opted-in requests at a per-lead price.

**Revenue stack:**
- Google AdSense
- Affiliate links
- Tool, guide, newsletter and video sponsorships
- Pay-per-lead partners (insurance, solar, finance, home services)
- YouTube Partner Program plus sponsored video segments
- Reader donations and memberships
- Contest sponsorships
- Job posts

---

## Phase 1: Foundation and brand
> Build a static, mobile-first site for **1Each.com** that needs no build tools and can be hosted on GitHub Pages' free plan. Use plain HTML, CSS and JS, one shared stylesheet, and design tokens on `:root`. Include dark mode (follows the system setting, with a manual toggle) and use the Inter and Space Grotesk fonts. Brand colours: violet `#5b3df5` and lime `#c6f432`.
>
> Every page must have:
> - a black top bar reading *"Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership"*, linking to `https://web.works/contact`
> - a sticky header with the logo, navigation, search, theme toggle and a "Get my 1 pick" button
> - a mobile menu
> - a newsletter band
> - a five-column footer carrying the copyright, trademark and affiliate notice
>
> Generate pages from one Python template (`build.py` plus `pages.py`) so the header and footer are the same everywhere. Use relative links so the site works under `username.github.io/repo/`.

## Phase 2: Traffic engine (calculators)
> Build six pure client-side calculators. Each one must update as the user types, show the formula and working, let the user pick a currency, have a Share button, a FAQ with FAQPage structured data, WebApplication structured data, related tools, and an ad slot.
>
> 1. **Split the bill.** Two modes: split evenly, or by what each person ordered plus shared items. Tip either before or after tax, with an option to round up.
> 2. **Unit price comparer.** Handles g, kg, oz, lb, ml, l, fl oz and count. Highlights the best value and shows the overpay percentage.
> 3. **Cost per use.** Compares two options, including upkeep and resale value.
> 4. **Tip calculator.** Rounding options plus a tipping guide table.
> 5. **Group trip settle-up.** Works out who owes whom with the fewest transfers (greedy matching).
> 6. **Subscription audit.** Monthly and yearly totals, plus the 10-year value of cancelling, assuming 7% returns.
>
> Put a live "quick split" widget in the homepage hero.

## Phase 3: Content engine (One Pick guides)
> Store guides as data in `picks.js`, one object per guide: category, icon, title, the one rule, a 4-point checklist, budget/top/upgrade picks, and a lead-form category.
>
> Show them in a filterable, searchable card grid. Each card gets a "Get my 1 pick" button that pre-fills the lead form with `?need=`. Start with 18 guides across Home, Kitchen, Tech, Money, Travel, Health, Software and Kids.
>
> Add a "How we choose" section and a "How we're paid" section for trust.

## Phase 4: Lead generation
> Build a four-step "Get Matched" form:
> 1. **Category:** 12 tiles; tapping one moves to the next step automatically.
> 2. **Budget and timeline.**
> 3. **Must-haves,** plus what the user wants back: one recommendation, provider quotes, or a call.
> 4. **Contact details,** a consent checkbox and a newsletter opt-in.
>
> The form needs a progress bar, a privacy promise, and a "How it works" / "Our promise" sidebar. Add a provider-partner application form (for businesses buying leads).
>
> Add these site-wide:
> - an exit-intent pop-up with a short two-field form
> - a sticky call-to-action button once the user has scrolled 900px
> - the newsletter form in every footer

## Phase 5: Private form routing
> **Never print the contact address.** Store it obfuscated in `config.js` (reversed, then base64). Decode it only at send time.
>
> Send every form through FormSubmit's AJAX endpoint as JSON, with:
> - a honeypot field against bots
> - HTML5 validation
> - success and error messages
> - a fallback that opens the user's email app
> - page, referrer and referral code attached to each submission
>
> After the first activation, swap in the FormSubmit alias (`formAlias`) so the address never appears even in the endpoint.

## Phase 6: Money and community
> - **Support page:**
>   - one-time amounts ($5, $15, $50, $100 or custom)
>   - a choice of which fund to support: operations, promotion, hiring or prizes
>   - an allocation bar chart, three monthly tiers, and a supporter wall
>   - Ko-fi, Buy Me a Coffee, PayPal, GitHub Sponsors and Stripe buttons, each shown only when its link is set in the config
> - **Contests page:**
>   - a countdown timer and an entry form
>   - bonus entries: newsletter +1, referral +3, video +5
>   - a referral link generated for each entrant
>   - official rules: no purchase necessary, judging criteria, a skill-testing question for Canada
>   - a "sponsor a prize" call to action
> - **Careers page:** six remote roles, an application form, a talent network, and a "post a job" link.
> - **Advertise page:** a stats strip, a package and rate table (including domain/site acquisition), an inquiry form, and brand-safety promises.

## Phase 7: Compliance, SEO and speed
> - **Legal pages:** Privacy (AdSense cookie wording, GDPR, CCPA, PIPEDA), Terms, and Affiliate/Trademark/Copyright disclosure (independence statement, nominative fair use, DMCA process, FTC wording), plus Cookies.
> - **Consent:** a cookie consent banner. Load GA4 only after the user consents.
> - **AdSense:** load it only when a publisher ID is set in the config. Otherwise show "Advertise here" house ads.
> - **SEO files:** `sitemap.xml`, `robots.txt`, an `ads.txt` template, canonical tags, Open Graph and Twitter tags, and an OG image.
> - **Site extras:** a web manifest, an offline service worker, a 404 page, and site-wide search (press `/` or Ctrl-K).
> - **Accessibility:** a skip link, focus rings, reduced-motion support, and ARIA labels.

## Phase 8: Monetisation switch-on (manual steps)
1. Point 1each.com DNS to GitHub Pages and add a `CNAME` file.
2. Apply for AdSense and paste `adsenseClient` and slot IDs into `config.js`.
3. Replace `ads.txt` with your publisher ID.
4. Add the GA4 ID.
5. Add donation links.
6. Add YouTube video IDs.
7. Send one test form to activate FormSubmit, then set `formAlias`.
8. Join affiliate programmes and add affiliate links to the picks.

## Phase 9: Scale content
> Add one guide page per pick (`/picks/<slug>.html`) with comparison tables, Product and Review structured data (only after real testing), and a date stamp.
>
> Add long-tail tool variants: "split rent by room size", "wedding cost per guest", "cost per mile EV vs gas", "price per sq ft", "per-person party budget".
>
> Aim for 3 new pages a week, with internal links from every tool.

## Phase 10: Growth loops
- **YouTube Shorts:** one Short per tool, linking back to the tool.
- **Newsletter:** a weekly issue that also carries sponsor slots.
- **Contests:** run them monthly to collect user tips, which become new content.
- **Embeddable widget:** a split calculator other sites can embed, with a backlink to 1Each.
- **Lead partners:** sign them by category and region.
- **Paid membership:** an ad-light version for members.
