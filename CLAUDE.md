# Ardmore Chamber — Hallpass Digital

Repo for client-facing web deliverables for the **Ardmore Chamber of Commerce**,
published via GitHub Pages at `https://ryan-hallpass.github.io/chamber-benefits/`.

Owner: Ryan McNeill, Hall Pass Digital, LLC.

---

## What lives here

| Path | Live URL | What it is |
|---|---|---|
| `index.html` | `/chamber-benefits/` | Member benefits landing page |
| `brochure/` | `/chamber-benefits/brochure/` | Scroll brochure (navy/red Chamber brand) |
| `hiring/` | `/chamber-benefits/hiring/` | "Now Hiring in Ardmore" job board prototype |
| `proposal/` | `/chamber-benefits/proposal/` | 2026–27 program proposal deck |
| `proposal/_src/` | *not published* | Generator + assets for the deck |

`_`-prefixed directories are excluded by Jekyll, so `proposal/_src/` never ships.
Do not add a `.nojekyll` file without moving the source out first.

---

## The engagement

Three separate Ardmore organizations, one shared audience:

- **ADA** — Ardmore Development Authority (economic development)
- **ATA** — Ardmore Tourism Authority
- **Chamber** — Ardmore Chamber of Commerce

**Bill Murphy** is President & CEO of the Chamber and also signs for ATA.
**Kelly Fryer** is Chamber EVP. **Albert Perrotta ("Al")** is a collaborator on the ADA side
who supplies performance metrics.

Everything publishes under the shared **"Ardmore Means More"** brand.

### The four agreements — read this before scoping anything

1. **ADA LOA, Sept 22 2025 — $150,000.** Term Oct 1 2025 – Sep 30 2026. *Expiring.*
   Line items: positioning strategy $6K, branded assets $8K, social $98K,
   three shoots $23K, two longform campaign videos $15K.
2. **Chamber "Member Engagement & Visibility Agreement," May 12 2026.** **STILL LIVE.**
   Covers membership collateral, lifecycle member email automation, digital member
   business profiles, the member directory page, the Annual Visibility Report, and
   testimonial video. Year 2 renewal decision due **Dec 1 2026**.
3. **ATA LOA, drafted Aug 7 2026 — $46,800. NEVER EXECUTED.** Its scope is being
   folded into agreement 4. It is dead; do not reference it as active.
4. **NEW — Chamber Marketing, Content & Community Engagement Program.**
   Oct 1 2026 – Sep 30 2027. **$199,200** ($16,600/mo). Currently DRAFT v6 in
   Google Drive. This is what the deck pitches.

### Do NOT scope or re-pitch these — they are already sold under agreement 2

Member business profiles · the member directory · the Annual Visibility Report ·
membership collateral · member lifecycle email · testimonial video ·
"new member recruitment campaign" (that *is* agreement 2).

Referencing them to *coordinate with, feed data into, or extend the reach of* is fine.
Re-billing them is not. This mistake has been made twice; the client caught it both times.

---

## The proposal deck

**Never hand-edit `proposal/index.html` — it is generated.**

```bash
cd proposal/_src
python3 build.py          # writes ../index.html
```

`build.py` is a single self-contained script: CSS block → chart SVGs → `slide()` calls
in order → assembly. Photos are base64-inlined from the `.png` files and `.b64` files
beside it, so the output is one ~800KB standalone HTML file with no external assets.

### Current structure (15 slides)

```
01  Cover — "People are already watching Ardmore. Let's keep building momentum."
02  What We've Built ...... Q1 vs Q2 small multiples          (dark)
03  The Audience .......... cumulative views + local/outside  (sage)
04  The Momentum .......... projection chart                  (dark)
05  Why This Has Worked ... three boxes, no body copy
06  How This Proposal Is Structured — ADA/ATA/Chamber flywheel (sage)
07  Proposed Initiatives for the Coming Year — numbered list
08  01 Ardmore Means More Social                              (sage)
09  02 Tourism Card Measurement & Reporting
10  03 Event Promotion Email Campaign                         (sage)
11  04 Chamber Member Learning Library
12  05 Employment in Ardmore Email                            (dark)
13  Implementation — three phases                             (sage)
14  Investment
15  Next Step                                                 (dark)
```

### Rules when editing slides

- `slide(n, cls, inner)` — `n` must stay sequential; it drives the page number
  **and** the footer logo colour.
- `DARK={2,4,12,15}` must list exactly the dark slide numbers, or the footer logo
  inverts wrongly. **Update it whenever slides are added, removed or reordered.**
- **Never two consecutive slides with the same background.** Rotate
  `''` (cream) → `slide--sage` → `slide--dark`. Verify after any reorder.
- Reordering slides means renumbering every `slide()` call after the move. Do the
  renumber with a mapping applied in one pass, or numbers will collide.
- After any structural change, screenshot with Playwright before claiming it works.
  Force `[data-reveal]` elements visible first and wait ~2.5s for staggered delays:
  ```js
  document.querySelectorAll('[data-reveal]').forEach(e=>e.classList.add('is-visible'))
  ```

### Design system (deck)

Cream `#F2EFE8` · ink `#1A1A18` · ink-soft `#3D3D38` · sage `#7A9E7E` ·
sage-light `#B8D0BB` · sage-wash `#EAF0EB` · warm-white `#FAFAF7` ·
rule `rgba(26,26,24,.12)`. Playfair Display (serif) + DM Sans (sans).
Scroll reveal via `[data-reveal]` + `data-delay` and an IntersectionObserver.
Keyboard nav for presenting: `→` `PgDn` `Space` next slide, `←` `PgUp` `Shift+Space`
previous (`↑`/`↓` stay native scroll so tall slides remain reachable).

The `hiring/` and `brochure/` pages use the **Chamber's own** brand instead:
navy `#0D2240`, red `#C0392B` / `#E85449`, Montserrat + Open Sans, 14px radius.
Don't mix the two systems.

---

## Editorial rules learned the hard way

- **Minimal text on slides.** Ryan presents these live; the slide is the visual aid,
  not the script. Three bullets max, short fragments, no paragraphs.
- **Never imply Hallpass takes over Chamber social accounts.** The line is
  *"we supply the assets, not the passwords."*
- Longform / campaign video is **deliberately out of scope** in the new agreement.
- Featured businesses do **not** keep their own footage (that language was removed).
- Don't assert months for Al's site-selector trip — he said "end of Sept/early October."
- Be precise with arithmetic. The line items sum to **$199,000**; the contracted
  total is **$199,200** (rounding to a clean $16,600/mo). Both figures appear on purpose.

## Verified numbers — do not invent or round these

- Q1 → Q2 2026: views **391,350 → 813,870** (+108%); engagements **20,670 → 42,410**
  (+105%); followers **~3,000 → ~6,000** (+100%)
- **1.4M** cumulative video views to date; **61%** of reach outside Ardmore, 39% local
- Projection: **~4.65M** cumulative (≈3.25M additional), ~24,000 additional followers
- **587** Chamber members — Kelly Fryer, quoted
- Job board test: **180+** open positions, **41** employers, in one week of collection
- Carter County lost roughly **a third** of manufacturing employment (Michelin wind-down)
- Economic Vision Plan: **10.3%** increase in local business applications;
  Oklahoma committed **$1M** to entrepreneurship

### Dead ends — do not retry

- **Oklahoma Secretary of State** business registrations cannot be scraped. This killed
  the "New Business Welcome Engine" idea.
- The **"683 new ventures"** figure is unsourceable from BFS data. Do not cite it.
- The **"Ardmore Business Barometer"** concept is dead. The data paints a grim picture
  and counter-positions against Bill's actual job, which is selling Ardmore.

---

## Deploy

```bash
cd proposal/_src && python3 build.py
cd ../.. && git add -A && git commit -m "..." && git push origin main
```

Pages updates about a minute after the push.

**Credentials:** `gh` is the global credential helper and its *active* account is
`oklahomaisok`, which has no write access here. The remote is pinned to
`https://ryan-hallpass@github.com/ryan-hallpass/chamber-benefits.git` so git asks `gh`
for the `ryan-hallpass` account specifically. If a push 403s, fall back to
`gh auth switch --user ryan-hallpass` and switch back afterwards.

The proposal deck carries `<meta name="robots" content="noindex,nofollow">` because it
has pricing on it. Keep it. The `hiring/` page also carries a `noindex` that should be
**removed** if and when it moves to the Chamber's real domain.

---

## Open items

- ~~Two-tier investment slide.~~ **DONE 2026-09-03.** Slide 14 now shows two options —
  **$199,200** "The Program" (featured ink card, five initiatives named, no per-initiative
  prices) and **$214,200** "The Program + Campaign Video" (adds two 2–5 min videos).
  Slide 15 carries the flat-spend line ($196,800 last year vs $199,200 ask).
  Per-initiative pricing lives in the contract only.
- If per-initiative pricing is ever wanted, the **$46,800** covering LOA sections 3–7
  needs splitting between initiatives 02 and 03. No agreed split exists — ask, don't invent.
- **Al's pre-Hallpass baseline metrics** are still needed for a flat-line-then-spike chart.
- **ADA creative-reuse clause** — the 2025 contract barred reuse for any other client
  outright; the new draft softens it. Needs a decision.
- A **speaker-notes companion** (one page per slide: the point, the number, the likely
  objection) has been offered and not yet built. All the copy trimmed off the slides
  belongs there.

## Selling notes

The strongest anti-negotiation frame: last year across the two organizations was
**$150,000 (ADA) + $46,800 (the tourism engagement put in front of Bill)** = **$196,800**.
The ask is **$199,200** — essentially flat — with one-time branding work and the longform
videos removed and the learning library and hiring channel added.

If Bill pushes on price, **concede on timing, not scope**: defer initiatives 04 and 05 to
month four. And if he targets the measurement layer specifically: there is no version where
it is cut and the other four initiatives still produce numbers a member can be shown.
The tracked redirect, the subscriber list and the dashboard are what make everything else
reportable.
