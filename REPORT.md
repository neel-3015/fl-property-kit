# Florida Property Decision Kit — Orlando vs. Brevard (Sept 2026)

**Audience:** parents deciding between buying in the Orlando MSA vs. Melbourne / Viera / Palm Bay / Titusville (Brevard).
**Companion tool:** `analyzer.html` (open by double-click) — presets match every number below. Math validated by `validate.py` (31/31 checks pass, run 2026-09-17).

All headline numbers below were re-verified on **2026-09-17** from primary sources (dates cited). Items marked *(est.)* are modeled assumptions, not facts.

---

## 1. Market snapshot (verified 2026-09-17)

| Metric | Value | Source (date) |
|---|---|---|
| Orlando‑Kissimmee‑Sanford MSA SFH median | **$439,000** (Aug, −0.6% YoY); **$445,000** YTD (0.0% YoY) | Florida Realtors MSA summary PDF, released 2026‑09‑16 |
| Palm Bay‑Melbourne‑Titusville MSA (Brevard) SFH median | **$375,000** (Aug, +2.6% YoY); $375,000 YTD (+1.4%) | same PDF |
| Orlando condo/townhouse median | $299,000 YTD (**−5.1%** YoY); Aug $300K (−3.2%) | same PDF |
| Brevard condo/townhouse median | $279,000 YTD (−2.1%) | same PDF |
| Statewide SFH median | $415,000 (Aug, +1.2%) | FL Realtors release 2026‑09‑16 |
| FL inventory | SFH 4.3 months' supply; condo/townhouse 7.7 months (condo = buyer's market) | same release |
| Orlando metro median asking rent | **$1,672** (Aug, −1.5% YoY); **58.5% of listings offer concessions** | realtor.com Aug‑2026 monthly rental report |
| National asking rent | $1,699 (Aug), 37th straight YoY decline; 2‑bed $1,896 (−0.9%) | same report |
| 30‑yr fixed mortgage | **6.95%** (week of 2026‑09‑17; 6.66% end‑July — rising through 2026) | FRED PMMS series, fetched 2026‑09‑17 |
| Amendment 3 (Nov 2026 ballot) | Homestead exemption → **$150K in 2027, $250K in 2028** if 60% approve | Fort Lauderdale civic coverage / FL Realtors affiliates, Aug–Sep 2026 |

**Corrections vs. the prior baseline used to build this kit:** Orlando MSA median is **$445K YTD (flat), not $455K (+2.5%)** — prices have gone sideways, not up. Brevard is confirmed at **$375K, +1–3%**. Orlando rent is **$1,672 (−1.5%)**, slightly below the prior $1,682. Mortgage rate is **6.95% and rising**, not stable — this is the single most important change; FL Realtors' chief economist noted YoY sales-growth streaks *ended* in August 2026 because of rising rates.

## 2. Verdict: Orlando vs. Brevard

1. **Do not buy a leveraged (20%‑down) rental right now in either market.** The math is not close: non‑homestead tax ≈1.85–1.9% of full value + Brevard insurance (~$4,280/yr county average, 2026) + a 6.95% mortgage exceed what rents pay. Every investment preset in `analyzer.html` shows year‑1 cash flow of **−$1,700 to −$2,150/month** with realistic 2026 inputs. (Even all‑cash West Palm Bay only breaks even, ≈−$51/mo after a 1% capex reserve.)
2. **Buy to live in, Brevard beats Orlando on entry price** ($375K vs $445K median, −16%) **but you pay it back in insurance** (Brevard avg ~$4,280/yr vs Orange ~$2,180–2,400/yr — 2026 estimates; get quotes, they swing ±$2K by zone/roof/credit). Net: roughly a wash on total cost at equal home value; Brevard wins if you find below-market, Orlando wins on liquidity/rental depth.
3. **Condos are the buyer's market** (7.7 months statewide supply, Orlando condo prices −5.1% YTD) — but SB‑4/SB‑122 milestone‑inspection **special assessments ($10K–$100K+ one-time)** are the reason prices are cheap. Only buy condos with recent SIRS/milestone docs fully funded.
4. **Rents are still falling** (37 straight months nationally; Orlando concessions at 58.5% mean real collected rent is ~5–8% below asking). Underwrite rent at asking **minus 7%**.
5. **Amendment 3 (Nov 3, 2026) matters only for a primary residence.** If it passes, a $450K Viera/Olando homestead cuts taxable value by $100K more in 2027 (≈$1,850/yr at 1.85% effective) and $200K more from 2028. Buying as an **investment property captures none of it**. If you're deciding primary-vs-investment, this asymmetry is material — modeled in the tool's A3 toggle.

## 3. Submarket cards (tool presets; NOI/cap computed with validated model, yr‑1, 20% down, 6.95%)

Assumptions common to all: closing 3%, vacancy 5% (LTR), repairs+capex ~2%, expense growth 3%, rent growth 2%, appreciation 3%. Insurance: Brevard‑inland $4,280 / Orange‑inland $2,400 *(est. — get quotes)*.

### West Palm Bay (new-build SFR, investment)
- Price $340K (baseline $310–380K) · rent $1,750 (baseline $1,700–1,900) · taxes $6,290 · insurance $4,280
- **NOI $2,785/yr · cap 0.8% · levered CF −$1,852/mo · breakeven rent $3,916/mo**
- Story: new construction (warranty, impact windows) is a lifestyle/safety buy, not a yield buy. Space‑station‑adjacent rental demand is real but rent growth can't outrun 6.95% debt + 1.85% non‑homestead tax.

### South Melbourne (investment)
- Price $410K (baseline $340–480K) · rent $2,000 (baseline $1,800–2,200) · HOA $60
- **NOI $4,291/yr · cap 1.1% · levered CF −$2,155/mo · breakeven rent $4,466/mo**
- Story: best tenant quality in Brevard (KSC/healthcare professionals), best schools — hold-for-appreciation logic only.

### Titusville (investment)
- Price $320K (baseline $280–360K) · rent $1,600 (baseline $1,400–1,900)
- **NOI $2,536/yr · cap 0.8% · levered CF −$1,750/mo · breakeven rent $3,647/mo**
- ⚠ Many Titusville/Scott Acres/South BeachArea homes are on **septic and in flood/evac zones**; unincorporated Brevard sewer availability changes both cost and rental eligibility.

### Viera (primary residence)
- Price $450K · 25% down · P&I $2,234/mo · HOA ~$130 · insurance ~$3,000 *(est., new-build)* · yr‑1 property tax after current $50K homestead: $7,400 (($450K−$50K)×1.85% eff.)
- With current homestead ($50K): yr‑1 tax ≈$7,400 (model applies exemption to $450K → taxable $400K). **Amendment‑3 scenario: yr‑1 $7,400 → yr‑2 $5,800 → yr‑3+ ~$4,200–4,750** (Save‑Our‑Homes 3% cap + $150K/$250K exemptions; validated series in `validate.py`).
- Story: premium price per sq‑ft, thin equity upside vs. Palm Bay, but it's where the schools/mall/commutes work for a family. If you live there 7+ years and A3 passes, SOH cap + bigger exemption compounds.

### Kissimmee edge STR (vacation rental)
- Price $475K · ADR $215 · 62% occupancy · STR mgmt 25% · Osceola TDT 6% *(verify current; sales tax adds more)* · permits $1,500/yr
- **NOI $14,577/yr · cap 3.1% · levered CF −$1,697/mo · breakeven ADR $345**
- ⚠ Zone trap: **Orlando city bans non‑owner‑occupied STRs** (post‑2024 ordinance; state SB‑252 framework allows strict local rules). **Cocoa Beach** heavily restricted + raised STR fees in 2025 (prior research cites Ordinances 1695/1697 — verify at city hall before counting on STR income). **Indialantic: east of A1A only.** Kissimmee (unincorporated Osceola) is the tolerant zone — rules can change; get it in writing from the county.

## 4. Florida cost-traps checklist

1. **Insurance quote BEFORE the offer** (Brevard inland avg ~$4,280/yr vs Orange ~$2,180–2,400 — 2026 est.; coastal/ICW $6,800+). DMS reports premiums falling in 51 counties this year (July 2026 news) but Insurify reports first‑half‑2026 rate spikes up to 33% in some counties — averages lie; your parcel's quote is the only number that matters. Roof age, elevation certificate, wind mitigation (HIP roof, impact glass) move it ±50%.
2. **Elevation / flood zone**: request FIRM panel + elevation cert; AE/X500 zone flood policies can double the insurance line.
3. **Septic vs sewer (unincorporated Brevard)**: septic pumping/replacement $5–25K; failed drainfield can block a re‑sale; check Brevard SWM district septic‑to‑sewer conversion programs — and that "sewer available" means at the property, not "planned."
4. **Condo SB‑4/SB‑122 milestone & SIRS**: demand the Structural Integrity Reserve Study, milestone inspection reports, and the reserve budget. Deferred special assessments run $10K–$100K+ and are yours on closing. 39‑unit+ buildings in Miami‑Dade had fully funded reserves mandated by 2026 — most 1970s Brevard/Orange stock did not get the same scrutiny.
5. **STR zoning in writing**: city/county permit pre‑approval email; verify owner‑occupancy rule, nights cap, TDT registration. Don't trust the listing, the HOA rep, or an agent.
6. **HOA/COA assessment authority**: read the bylaws for special‑assessment power and any rental caps / tenant screening rules / move‑in fees.
7. **Non‑homestead taxes**: investment property gets NO exemption, no 3% cap; budget full ~1.85–1.9% effective. The optional 15% assessed‑value reduction (toggled in tool) is conditional — confirm eligibility with the appraiser's office.

## 5. Timing & negotiation (Sept 2026)

- Rents down 37 straight months; 58.5% of Orlando rental listings offer concessions; Orlando inventory and price cuts rising (housingwire, recent); FL condo supply 7.7 months. Sellers are cutting. **Ask for:** price cuts with comps, seller‑paid rate buydown (biggest lever at 6.95%), closing‑cost credits, and repair credits instead of repairs.
- **Rising-rate environment = keep negotiating into late fall/winter** (Dec–Feb is Florida's weakest seller season, offset partly by snowbird season in Brevard — Palm Bay/Melbourne see a Dec–Mar bump).
- Rate direction is the biggest model variable: ±0.75% moves monthly cash flow by ~$170 (tool sensitivity table). Don't wait for a rate drop you can't time; do lock a rate with a float‑down if offered.
- **Amendment‑3 uncertainty (Nov 3 vote)** adds tax‑planning noise but shouldn't drive purchase timing for investment purchases (A3 excludes investment property).

## 6. Due-diligence checklist

See `checklist.csv` (printable rows) — condensed: pre-offer (quote, comps at appraiser sites below, insurance quote in hand, lender pre‑approval with rate‑lock terms), contract period (inspection incl. roof/AC/sewer‑scope, elevation cert, wind‑mitigation form O-E for credit, HOA docs + estoppels, condo SIRS/milestone/budget, deed restrictions, permit/zone letter in writing, survey/flood cert, well/septic if applicable, tax escrow confirmation incl. non‑homestead classification + TRIM notice), closing (Title I/II commitments, per‑diem interest, final figures/CD vs LE), post‑close (file homestead application by Mar 1 for primaries, confirm parcel tax status next July TRIM, calendar roof/AC/pressure‑test for condos, register for TDT if STR).

**Comps & tax portals (official):**
- Brevard: `pabrevard.org` (Property Appraiser) — note: this domain was unreachable from the build environment on 2026‑09‑17 (county-site network block; works from residential ISPs / their phone line). Brevard County Tax Collector for actual millage after the Sept TRIM roll.
- Orange/Osceola-adjacent: `https://www.ocpafl.org` — **verified live 2026‑09‑17 (HTTP 200)**. Orange County Property Appraiser (Jeff Green) parcel search + TRIM notices.
- Mortgage-rate series: FRED `MORTGAGE30US` (fetched 2026‑09‑17).

## 7. Amendment 3 — tax detail baked into the model (cycle 4)

- Current: homestead exemption $50K (first $25K + additional $25K on value $50K–$75K) + Assessment Limitation ("Save Our Homes"): assessed value can rise only min(3%, CPI−2%). Investment property: no exemption, no cap (non‑homestead reassessment; state law caps AV growth at 10%/yr for non‑homestead — model grows it with the market but taxes are small enough vs. debt service that this barely moves the result).
- Amendment 3 (Nov 2026): raises total homestead to $150K (2027) then $250K (2028); needs 60%. Analysts (Sheriffs, counties, Sierra Club) warn of service cuts / millage backfill — assume some offsetting millage increase in worst case (tool's effective‑millage input is editable for this).
- **Decapture/turnover:** SOH caps reset to market value for the next buyer when the homestead sells ("decapture"), so your low assessed value is not portable, and it quietly caps your *future* sale price vs. non-cap neighbors ("assessment limitation paradox"). Buyers of capped homes should model taxes rising to market levels in year 2+.
- Primary vs investment asymmetry table (from validated `vieraA3` series, $450K Viera, 1.85% eff.): tax yr‑1 $7,400 → yr‑2 $5,800 → yr‑3 $4,207 → yr‑4 $4,472 → yr‑5 $4,745 (A3 passes). Investment twin pays ~$8,325→$9,380 over the same 5 years — **≈ $17–19K of tax difference on a 5‑year hold**, before income‑tax depreciation effects.

## Sources
1. Florida Realtors, "August 2026 MSA summary" PDF + release "Fla.'s Housing Market: Median Prices Hold Steady as Pace Eases" — released 2026‑09‑16 (fetched 2026‑09‑17).
2. realtor.com Research, "August 2026 Rental Report: Rents Fall for 37th Straight Month…" (fetched 2026‑09‑17).
3. FRED (Freddie Mac PMMS) `MORTGAGE30US`, weekly to 2026‑09‑17 (fetched 2026‑09‑17).
4. Amendment 3 reporting: Fort Lauderdale town-hall coverage via Google News resolver (Sep 2026); Ballotpedia page absent at time of check — figures cross-checked across ≥2 outlets (WPEC, Tallahassee Democrat, Center Square headlines).
5. Brevard/Orange insurance averages and submarket price/rent bands: prior-baseline research, retained as *(est.)* pending quote-level verification; DMS "premiums falling in 51 counties" (Spectrum News 13, 2026‑07‑30) and Insurify H1‑2026 "up to 33% county spikes" headlines fetched 2026‑09‑17.
6. STR rules: Orlando post‑2024 non‑owner‑occupied ban (no repeal found in 2026 coverage, checked 2026‑09‑17); Cocoa Beach fee/condo STR adjustments (Florida Today Apr 2025 headline, checked 2026‑09‑17 — ordinance numbers NOT independently verified); state SB‑252 (2024) framework.
7. Portal availability checks 2026‑09‑17: ocpafl.org HTTP 200; pabrevard.org unreachable from build network.
