# 1Each.com: one smart answer for each decision

1Each is a static, responsive website with three parts:
- **Calculators:** split the bill, unit price, cost per use, tip, trip settle-up, subscription audit
- **One Pick buying guides**
- **Lead generation:** Get Matched, plus a provider-partner form

It also has donation and membership pages, contests with referral entries, careers, an advertising media kit, and full legal pages.

The site runs on the **free GitHub Pages plan**. It has no backend and no build step on the server.

- Live (GitHub Pages): https://webworksa1.github.io/1each-com/
- Build brief: [`PROMPT.md`](PROMPT.md)
- 35-site audit: [`RESEARCH.md`](RESEARCH.md)

## Edit and rebuild
```bash
python3 build.py      # regenerates every *.html, sitemap.xml, the search index and assets/img/og.png (needs Pillow)
```
- **Page content:** `pages.py`
- **Shared header and footer:** `build.py`
- **Guides:** `assets/js/picks.js`
- **Settings:** `assets/js/config.js`. This holds AdSense, GA4, YouTube IDs, donation links and contest dates.

Commit the regenerated HTML. GitHub Pages serves the repo as-is (Settings → Pages → Deploy from branch).

## Go-live checklist
1. **Custom domain.** In the repo, open Settings → Pages → Custom domain, enter `1each.com`, then add these DNS records:
   - A records pointing to 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153
   - a CNAME record for `www` pointing to `webworksa1.github.io`
2. **Social image.** Run `python3 build.py` once locally and commit `assets/img/og.png`.
3. **Forms.** Submit any form once, then click the activation link FormSubmit sends to the site inbox. Optionally paste the alias FormSubmit gives you into `formAlias`. The contact address is stored obfuscated and is never printed on the site.
4. **AdSense.** Once approved, set `adsenseClient` and the `adSlots` values, and put your publisher line in `ads.txt`.
5. **Analytics.** Set `ga4`. It loads only after the visitor gives cookie consent.
6. **Donations.** Set the `donate.*` URLs.
7. **Videos.** Set `videos[].id`, the YouTube video IDs.

## Trademark and copyright
"1Each" is used as a descriptive name meaning "one each". The site is independent and not affiliated with any holder of a similar name. See `disclosure.html`. © 2026 1Each.com.

Interested in this website, domain, sponsorship, advertising or partnership? → https://web.works/contact
