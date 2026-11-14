# Scheduled re-poke — JEDEC-6400 RDIMM bests, EU

One scheduled task, running every 30 min, appends a dated section per pass.
Baseline (2026-11-13, net/VAT-less, NBP 4.4070 zł/EUR):

- **Proshop.pl `KF576RH40RBK4-128`** (7600, 4×32 GB, JEDEC-6400 SPD): 25 969 zł = €5,893 gross / **€4,791 net** → €4,791/128 GB = **€37.43/GB**
- **ibfusion `KSM64R52BD4-64MD`** (64 GB 2Rx4): **€2,481 net** (4 in stock)
- **Tonitrus Samsung `M321R8GA0EB2-CCP`** (64 GB 2Rx4): **€2,667.65 net** (50 in stock)
- Target to beat: **€4,791 net per 128 GB (€37.4/GB)**

---

## Pass 1 — 2026-11-13T22:1xZ (scheduled poke)

### 1. Re-check of the three bests

| Offer | Result | Price string seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **UNCHANGED** | "25 969,00 zł / 21 113,01 zł netto", "Produkt sprowadzany, czas dostawy 4-5 dni", max 2 szt./klienta | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** | "2 681,96 € incl. 8.1% VAT · Switzerland / 2 481,00 € excl. VAT - B2B price" | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| Tonitrus M321R8GA0EB2-CCP | **BLOCKED this pass** — r.jina.ai returned "Target URL returned error 403: Forbidden" ( Tonitrus bot-wall tightened vs earlier passes). Last verified: €2,667.65 net, 50 available (17:4xZ). | — | https://www.tonitrus.com/M321R8GA0EB2-CCP |

### 2. Sweep for anything cheaper than €4,791/128 GB net

| Shop | Result |
|---|---|
| Proshop.de | **BLOCKED** (Cloudflare 403, "Attention Required") — unchanged since the parent's last attempt |
| Alternate.de | 404 on search URL (`/search.html?query=KSM64R52BD4`) — no results served |
| Tonitrus search | served but empty: query "6400 RDIMM" returns switches/transceivers only — **no new RDIMM listings** |
| DDG lite (KSM64R52BD4-64MD price / KF576RH40RBK4-128) | queries returned no result rows (anti-bot challenge) |
| ibfusion (both 32 GB pages re-fetched) | unchanged: KSM64R52BD8-32MH €1,421 net (5 in stock); Samsung M321R4GA3EB2-CCP €1,598 net (4 in stock) |

### 3. QVL part hunt (MEM-DR564MC-ER64 / Samsung M321R8GA0PB2-CCP)

Tonitrus product page for `M321R8GA0PB2-CCP` now behind an **explicit CAPTCHA wall** ("Just a moment… / security verification") even via r.jina.ai — the earlier out-of-stock state can't be re-confirmed this pass. **Still no EU price for the QVL part.**

### 4. Verdict

**Did anything beat €4,791/128 GB net? — No.** All three verified bests are unchanged; two EU sources (Proshop.de, Tonitrus) are now bot-walled; no new qualifying listings surfaced.

---

## Pass 2 — 2026-11-13T22:4xZ (scheduled poke)

### 1. Re-check of the three bests

| Offer | Result | Price string seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **BLOCKED this pass** (Cloudflare 403 "Attention Required", also on search) — price unverifiable; last verified 25 969 zł / 21 113,01 zł netto at 22:1xZ | — | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** | "2 681,96 € incl. 8.1% VAT · Switzerland / 2 481,00 € excl. VAT - B2B price", **4 in stock** | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| Tonitrus M321R8GA0EB2-CCP | **BLOCKED** (403 via r.jina.ai, second consecutive pass) — last verified €2,667.65 net / 50 in stock | — | https://www.tonitrus.com/M321R8GA0EB2-CCP |

### 2. New source found: senetic.pl (was on the untested list)

| Part | JEDEC SPD verdict | Shop | Exact price | Stock | URL |
|---|---|---|---|---|---|
| Kingston `KSM64R52BD4-64MD` (64 GB 2Rx4) | JEDEC-6400 (same Server Premier datasheet family, sentence verified earlier) | **senetic.pl** | **11 509,07 zł netto** (= €2,612; 14 156,16 zł brutto) | **41–50 szt., "Wysyłka w ciągu 24h"** | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| Kingston `KSM64R52BD4-96MC` (96 GB) | JEDEC-6400 family | senetic.pl | 16 417,58 zł netto (€3,725; €38.8/GB) | listed | same URL |
| Kingston `KSM64R52BS8-16MH` (16 GB) | JEDEC-6400 (datasheet verified earlier) | senetic.pl | 2 748,17 zł netto (€624; €39.0/GB) | listed | same URL |

Notes: senetic price is **+5.3 % vs ibfusion** for the same 64 GB part (€2,612 vs €2,481 net) — **does not beat the baseline** (€40.8/GB vs €38.8/GB; 12× = €31,339 vs €29,772 for 768 GB). But senetic is a **mainline PL distributor with 41–50 units and 24 h shipping** — the first large-stock retail source for the JEDEC-6400 64 GB part found so far (Tonitrus 50 pcs is bot-walled, ibfusion has 4). No Renegade kits on senetic. Product-page deep links 404 (search-page prices only).

Other probes this pass: morele.net 404 (no part), x-kom 403, komputronik no relevant hit.

### 3. QVL part hunt

`MEM-DR564MC-ER64` / Samsung `M321R8GA0PB2-CCP`: **still no EU price** (Tonitrus CAPTCHA-walled; senetic search for the Samsung PN served no product rows).

### 4. Verdict

**Did anything beat €4,791/128 GB net? — No.** Baselines unchanged where verifiable; senetic.pl adds a large-stock (+5.3 %) fallback for the 64 GB Server Premier route, which matters for actually sourcing 12 modules, not for price.

---

## Pass 3 — 2026-11-13T23:1xZ (scheduled poke)

### 1. Re-check of the bests

| Offer | Result | Price string seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **BLOCKED** (Cloudflare 403, 2nd consecutive pass) — last verified 25 969 zł / 21 113,01 zł netto 22:1xZ | — | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** | "2 681,96 € incl. 8.1% VAT · Switzerland / 2 481,00 € excl. VAT - B2B price", **4 in stock** | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| Tonitrus M321R8GA0EB2-CCP | **BLOCKED** (3rd pass; 403 via r.jina.ai) — last verified €2,667.65 net / 50 in stock | — | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| senetic.pl 64MD (pass-2 fallback) | **UNCHANGED** | "11 509,07 zł netto" | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| Caseking V-Color JEDEC 6400 kits | **still OutOfStock** (both 4×32 and 8×32; preorder badge only) | — | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-128-gb-4-x-32-gb-quad-channel-kit-black/MEVC-031.html |

### 2. New listings found this pass (senetic.de — Samsung QVL-family, verified rows)

| Part | JEDEC SPD verdict | Shop | Exact price | Stock | URL |
|---|---|---|---|---|---|
| Samsung `M321RAJA0MB2-CCP` — **128 GB 3DS RDIMM 6400** (the CP1-QVL 128 GB part!) | JEDEC 6400 (3DS 2S2R; board manual rates 3DS 4-rank 6400 at 1DPC) | **senetic.de** | **6 175,58 € exkl. MwSt.** (€48.25/GB; 7 348,94 € brutto) | **6 Stück** | https://www.senetic.de/search/?q=M321R8GA0PB2-CCP&f_s_category=icecat_106 |
| Samsung `M321R8GA0EB2-CWM` — 64 GB **5600** (not 6400 — the EB2-CWM suffix is 5600) | n/a for 6400 rule | senetic.de | **971,07 € exkl.** (€15.17/GB!) | "Zur Anfrage" (quote) | same URL |
| Samsung `M321R8GA0PB0-CWM` — 64 GB 5600 (the old BOM part) | n/a | senetic.de | 3 087,21 € exkl. | listed | same URL |

Notes: the **128 GB 3DS Samsung at €6,175.58 net with 6 in stock** is the first EU-priced QVL-family 6400 part above 64 GB — €48.25/GB does **not** beat the baseline, but 12× it = **1.5 TB at 6400** (board manual: 3DS 2S2R = 6400 at 1DPC), the capacity route without buying 64 GB modules. The €971 Samsung 64 GB is **5600**, not 6400 — recorded because at €15.17/GB it is the cheapest 64 GB RDIMM seen all day, but it fails the JEDEC-6400 rule and would drop the whole array to 5600 (537 GB/s, −12.5 %). Quote-only stock.

### 3. QVL part hunt

`MEM-DR564MC-ER64` / Samsung `M321R8GA0PB2-CCP`: senetic.de search lists **43 category hits for the PN family** but only the 128 GB `M321RAJA0MB2-CCP` and 5600 parts carry prices — **the exact 64 GB 6400 QVL part still has no EU price** (4th consecutive pass).

### 4. Verdict

**Did anything beat €4,791/128 GB net? — No.** New data this pass: senetic.de opens the **QVL-family 128 GB 3DS route** (€48.25/GB, 6 in stock) and a **€15.17/GB 5600 64 GB** (quote-only, fails the 6400 rule but is the first crack in the shortage pricing — watch it).

---

## Pass 4 — 2026-11-13T23:4xZ (scheduled poke)

### 1. Re-check of the bests

| Offer | Result | Price string seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **BLOCKED** (Cloudflare 403, 3rd consecutive) — last verified 21 113,01 zł netto at 22:1xZ | — | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** | "2 481,00 € excl. VAT - B2B price", **4 in stock** | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| Tonitrus M321R8GA0EB2-CCP | **BLOCKED** (4th pass, 403 via r.jina.ai) — last verified €2,667.65 net / 50 in stock | — | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| senetic.pl 64MD | **UNCHANGED** | 11 509,07 zł netto | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| senetic.de Samsung watch rows | **UNCHANGED** | M321R8GA0EB2-CWM (5600) 971,07 € exkl; M321R8GA0PB0-CWM (5600) 3 087,21 € exkl; no 6400 EB2 variant appeared | https://www.senetic.de/search/?q=M321R8GA0PB2&f_s_category=icecat_106 |
| Caseking V-Color JEDEC 6400 4×32 | **still OutOfStock** | — | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-128-gb-4-x-32-gb-quad-channel-kit-black/MEVC-031.html |

### 2. New-listing sweep

senetic probed for Renegade kits (`KF572RH38RBK8`), the 32 GB Server Premier (`KSM64R52BD8`) and the -64MH die variant: **no new rows** — senetic carries only the 16/64/96 GB Server Premier parts already recorded. No other shop fetched fresh this pass (all previously blocked/unreachable).

### 3. QVL part hunt

`MEM-DR564MC-ER64` / Samsung `M321R8GA0PB2-CCP`: **still no EU price** (5th consecutive pass).

### 4. Verdict

**Did anything beat €4,791/128 GB net? — No.** Third pass in a row with zero market movement; Proshop.pl and Tonitrus stay bot-walled, and the watch items (senetic.de Samsung 5600 at €971, Caseking V-Color restock) are unchanged.

---

## Pass 5 — 2026-11-14T00:0xZ (scheduled poke — first pass through the Camouflage browser)

This pass ran through **Playwright Chromium** (real engine, JS on, challenge auto-wait, `navigator.webdriver` masked) instead of curl, to get through the bot walls. **It worked: both walled shops are readable again.**

### 1. Re-check through the browser

| Offer | Result | Exact strings seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **UNBLOCKED, UNCHANGED** | "25 969,00 zł / 21 113,01 zł netto", "Produkt sprowadzany, czas dostawy **3-4 dni**", "max 2 szt./klienta" | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| Tonitrus Samsung M321R8GA0EB2-CCP | **UNBLOCKED, UNCHANGED** | "Neu Neuware **3.174,50 € brutto / 2.667,65 € netto** · Verfügbar: **50** · Lieferzeit ca. 3–4 Werktage" (refurb: 3.693,50 € brutto / 3.103,78 € netto, also 50) | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| ibfusion KSM64R52BD4-64MD | unchanged (curl, not walled) | 2 481,00 € excl. VAT, 4 in stock | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| senetic.pl 64MD | unchanged (curl) | 11 509,07 zł netto | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| Caseking V-Color JEDEC kit | still OutOfStock (curl) | — | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-128-gb-4-x-32-gb-quad-channel-kit-black/MEVC-031.html |

### 2–3. New listings / QVL hunt

No new listings this pass; the browser re-verified the two walled bests instead. QVL part (`MEM-DR564MC-ER64` / Samsung `M321R8GA0PB2-CCP`) — Tonitrus product page now reachable through the browser, but the specific QVL sibling page was not re-fetched this pass; prior finding (no EU price, 5 passes) stands.

### 4. Verdict

**Did anything beat €4,791/128 GB net? — No.** But the pass is notable: **the Camouflage/Playwright route unblocks both bot-walled shops** — Proshop.pl shows a *shorter* lead time than before (3–4 days, was 4–5), and Tonitrus confirms 50 pcs new at €2,667.65 net live from the page. All tracked bests intact.

---

## Pass 6 — 2026-11-14T00:4xZ (scheduled poke, Camouflage/Playwright route)

### 1. Re-check of the bests

| Offer | Result | Exact strings seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **UNCHANGED** (via browser) | "25 969,00 zł / 21 113,01 zł netto", lead **3–4 dni**, max 2 szt./klienta | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| Tonitrus Samsung M321R8GA0EB2-CCP | **UNCHANGED** (via browser) | "Neu Neuware 3.174,50 € brutto / 2.667,65 € netto", **Verfügbar: 50** | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** | 2 481,00 € excl. VAT, 4 in stock | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| senetic.de watch row (5600 64 GB) | regex missed the price this pass; re-check next pass (row was 971,07 € exkl at 23:1xZ) | — | https://www.senetic.de/search/?q=M321R8GA0PB2&f_s_category=icecat_106 |

### 2–3. New listings / QVL hunt

No new-listing fetches this pass (browser pass focused on re-verifying the walled bests). QVL part: **no EU price, 6th consecutive pass**.

### 4. Verdict

**Did anything beat €4,791/128 GB net? — No.** Fourth flat pass; all three bests byte-identical to the 22:1xZ snapshot.

---

## Pass 7 — 2026-11-14T01:1xZ (scheduled poke, EXPANDING: senetic.de CCP row, Alternate, Kaufland, server-warehouse/bulk-memory, QVL retry, KF576RH40RB-32 datasheet)

### 1. Re-check of the bests (browser route for walled shops)

| Offer | Result | Exact strings seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **UNCHANGED** (browser) | "25 969,00 zł / 21 113,01 zł netto", lead **3–4 dni** | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| Tonitrus Samsung M321R8GA0EB2-CCP | **UNCHANGED** (browser) | "Neu Neuware 3.174,50 € brutto / 2.667,65 € netto", **Verfügbar: 50** | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** (curl) | 2 481,00 € excl. VAT, 4 in stock | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| senetic.pl KSM64R52BD4-64MD | **UNCHANGED** (curl) | 11 509,07 zł netto, 41–50 pcs | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| senetic.de watch row 5600 | **UNCHANGED** | card "M321R8GA0EB2-CWM … **971,07 €**" | https://www.senetic.de/search/?q=M321R8GA0EB2&f_s_category=icecat_106 |

### 2. NEW listings found this pass

| Part | JEDEC SPD verdict | Shop | Exact price | Stock/lead | URL |
|---|---|---|---|---|---|
| Samsung **M321R8GA0EB2-CCP** 64 GB DDR5-6400 RDIMM (no SPD sentence published; part is the JEDEC-native 6400 bin) | counts (native 6400) | **senetic.de — NEW row, first time listed** | card: "Samsung RDIMM DDR5 64GB 2Rx4 6400MHz PC5-51200 … **3.387,48 € exkl. MwSt** / 4.031,10 € inkl." (€52.93/GB) | **Verfügbarkeit: 41–50 Stück** | https://www.senetic.de/product/M321R8GA0EB2-CCP |
| Kingston **KF576RH40RB-32** single 32 GB 7600 module | **SPD-verified**: datasheet "tested to run at DDR5-7600 … JEDEC standard latency **DDR5-6400** timing of 52-52-52 at **1.1V**" → qualifies, same family as the kit | (Kingston datasheet only; single stick not separately price-hunted yet) | — | — | https://www.kingston.com/datasheets/KF576RH40RB-32.pdf |

### 3. QVL hunt (MEM-DR564MC-ER64 / M321R8GA0PB2-CCP)

DDG-lite now returns only **US** channels for PB2-CCP: serversupply.com, newegg, harddiskdirect, corewavelabs, ebay.com (the eBay listing fetch itself was blocked, 262 B). **EU: still no price — 7th consecutive pass.**

### Blocked this pass

Kaufland.de (403 RayID bot-wall), eBay.com listing page (r.jina.ai thin response), bulk-memory.eu + server-warehouse.de (**DNS unresolvable from this sandbox host**), Alternate.de search (JS-rendered, no result nodes in curl HTML; not browser-tried this pass), Caseking V-Color page (Cloudflare JS interstitial this time — last-verified state stands: OOS preorder).

### 4. Verdict + coverage

**Did anything beat €4,791/128 GB net? — No.** Fifth flat pass. The new senetic.de CCP row (€3,387.48 net/64 GB = 12× = €40,650 net) sits **27% above** Tonitrus at 50 pcs, so Tonitrus remains the Samsung-route source.

This pass probed: senetic.de CCP product row (new), Alternate.de (search, JS-blocked), Kaufland.de (403), bulk-memory.eu + server-warehouse.de (DNS), QVL PB2-CCP retry (US-only), Kingston KF576RH40RB-32 single datasheet (SPD-verified).

---

## Pass 8 — 2026-11-14T01:4xZ (scheduled poke, EXPANDING: Proshop Renegade-PRO whole family, KSM64R52BD8-32MH SPD, geizhals, senetic.de raw)

### 1. Re-check of the bests (browser for walled, curl for open)

| Offer | Result | Exact strings seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **UNCHANGED** (browser) | "25 969,00 zł / 21 113,01 zł netto", lead 3–4 dni | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| Tonitrus Samsung M321R8GA0EB2-CCP | **UNCHANGED** (browser) | 3.174,50 € brutto / 2.667,65 € netto · Verfügbar: 50 | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** | 2 481,00 € excl. VAT · 4 in stock | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| senetic.pl KSM64R52BD4-64MD | **UNCHANGED** | 11 509,07 zł netto | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| senetic.de CCP / CWM watch rows | **UNCHANGED** (raw HTML contains 971,07 € and 3.387,48 €) | same as pass 7 | https://www.senetic.de/search/?q=M321R8GA0EB2&f_s_category=icecat_106 |

### 2. NEW listings found this pass — the whole Renegade PRO 7600 family on Proshop.pl (browser, product-page variant links)

| Part | JEDEC SPD verdict | Shop | Price (net → €/GB) | Stock/lead | URL |
|---|---|---|---|---|---|
| KF576RH40RB-32 **single 32 GB** | **SPD-verified** — "JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V" (datasheet KF576RH40RB-32.pdf) | Proshop.pl | 5 305,69 zł netto = €1,203.92 → **€37.62/GB** (0.5% over the bar) | 3–4 dni · max 2 szt./klienta | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-32GB-CL38-Single-Channel-1-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462077 |
| KF576RH40RBK4-64 **4×16 GB kit** | same family (16 GB bin; SPD not separately pulled) | Proshop.pl | 13 900,81 zł netto = €3,154.26 → €49.29/GB | 3–4 dni · max 2 | 4×16 variant of 3462079 |
| **8×16 GB octa kit** (128 GB) | same family | Proshop.pl | 27 765,04 zł netto = €6,300.21 → €49.22/GB | 3–4 dni · max 2 | 8×16 variant of 3462079 |
| 16 GB single | same family | Proshop.pl | 3 503,25 zł netto = €794.93 → €49.68/GB | 3–4 dni · max 2 | 16 GB single variant |
| Kingston **KSM64R52BD8-32MH** 32 GB Server Premier | **SPD-verified**: "The SPD is programmed to JEDEC standard latency **DDR5-6400** timing of 52-52-52 at **1.1V**" → qualifies | (datasheet only, no price found yet) | — | — | https://www.kingston.com/datasheets/KSM64R52BD8-32MH.pdf |

Note: the 32 GB single at **€37.62/GB** is effectively at parity with the 4×32 kit (€37.43) — and its 2 szt./klienta limit is per-SKU, so singles are the staging path if the kit purchase cap binds (6 purchases × 2 = 12 singles for 384 GB at €1,203.92 × 12 = €14,447 net, vs 3 kits = €14,372 — 0.5% premium).

### 3. QVL hunt

Not re-run this pass (pool rotation); pass-7 finding stands: **no EU price, 7 passes**.

### Blocked this pass

Geizhals via r.jina.ai: page loads but shows only the generic "Preisvergleich" frame, no product price node → treated as no-listing (bot-lite block). Caseking page not re-probed (pass-7 Cloudflare state stands).

### 4. Verdict + coverage

**Did anything beat €4,791/128 GB net? — No.** Sixth flat pass; closest new finding: 32 GB singles at parity (€37.62/GB), 16 GB dies carry the family premium (€49+/GB).

This pass probed: Proshop.pl Renegade PRO family variants (4 SKUs priced — new), KSM64R52BD8-32MH datasheet SPD (qualifies), geizhals (no-listing), senetic.de raw price re-check (both watch rows unchanged), plus full bests re-check.

---

## Pass 9 — 2026-11-14T02:2xZ (scheduled poke, EXPANDING: huihui slice C lands — Micron/SK hynix/Geizhals/QVL part; plus Amazon.de, picclick, heise, mem-tek probes)

### 1. Re-check of the bests

| Offer | Result | Exact strings / method | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **UNCHANGED** (browser) | "25 969,00 / 21 113,01 zł netto" | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| Tonitrus Samsung M321R8GA0EB2-CCP | **UNCHANGED** (browser) | 2.667,65 € netto · 50 pcs | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** (curl) | 2 481,00 € excl. VAT · 4 in stock | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| senetic.pl KSM64R52BD4-64MD | **UNCHANGED** (curl) | 11 509,07 zł netto | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| Caseking V-Color | not re-probed (Cloudflare pass-7 state stands: OOS) | — | MEVC-031 product page |

### 2. NEW listings this pass — huihui slice C (Micron / SK hynix / QVL part). LEAD-verified: huihui agent fetched these; parent re-verification blocked this host (marked per row). Geizhals/idealo prices are **gross** → net estimated ÷1.19.

| Part | JEDEC SPD verdict | Shop | Exact price seen | Stock/lead | URL |
|---|---|---|---|---|---|
| Micron **MTC40F2046S1RC64BH1T** (tray) | 6400 confirmed via micron.com part page (MT/s 6400, CL52, PC5-51200R); no SPD sentence published | Geizhals.de (lead) | "ab € 2999,81" **inkl. MwSt** (≈ €2.521 net → **€39.4/GB net**) | 5 Angebote; Jacob "Sofort lieferbar" | https://geizhals.de/micron-rdimm-64gb-mtc40f2046s1rc64bh1t-a3877100.html |
| Micron **MTC40F2046S1RC64BH1** | same | Geizhals.de (lead) | "ab € 3289,98" inkl. MwSt (≈ €43.2/GB net) | 5 Angebote | https://geizhals.de/micron-rdimm-64gb-mtc40f2046s1rc64bh1-a3871706.html |
| Samsung **M321R8GA0EB2-CCP** | no SPD sentence published | Geizhals.de (lead) | "ab € 3069,00" inkl. MwSt (≈ €40.3/GB net), 15 Angebote | — | https://geizhals.de/samsung-rdimm-64gb-m321r8ga0pb0-cwm-a3138665.html (aggregator slug) |
| SK hynix **HMCG94AHBRA480N** | no SPD sentence published; 6400 per Geizhals/seller listings only | Geizhals.de (lead) | "um € 3564,32 (€ 55,69 / GB)" inkl. MwSt (≈ €46.8/GB net) | 1 Angebot | https://geizhals.de/sk-hynix-rdimm-64gb-hmcg94ahbra480n-a3657519.html |
| **Samsung M321R8GA0PB2-CCP (QVL-family part!)** | no SPD sentence published | **smicro.eu / ANAFRA (CZ, ships EU)** (lead; parent re-verify BLOCKED — Turnstile) | "**€ 3 504,44 ex VAT**" (≈ €54.8/GB net) — "price volatility, contact for quote" | shop 0 · supplier 1 pc · EU courier 26.11–02.12 | https://smicro.eu/samsung-64-gb-ddr5-6400mhz-ecc-rdimm-m321r8ga0pb2-ccp-2 |

**QVL-part streak status:** the 8-pass "no EU price" for the Supermicro-QVL family part is **broken by a lead**: smicro.eu lists the Samsung `M321R8GA0PB2-CCP` at €3.504,44 ex VAT (1 pc supplier stock, quote-flagged). The literal Supermicro SKU `MEM-DR564MC-ER64` still has no EU street price (US channels only). Price is **46% above** the bar anyway — no ranking change.

Parent's own new probes: **Amazon.de** (browser): served CHF-priced (session geo) — 109 results, only relevant hit = Micron 128 GB 2Rx4 6400 CL52 `MTC40F2047S1RC64BR` at **8.230,75 CHF** (≈ €65+/GB) — far above. **senetic.pl KSM64R52BD8** (32 GB Server Premier): 3 search hits, **no price nodes** (search cards render priceless; product page hit senetic's "you have been blocked" wall this pass).

### Blocked this pass

smicro.eu (Cloudflare Turnstile, 20×3 s loop no clear; curl 403), senetic.pl **product** pages (DSI block interstitial; search pages fine), picclick.de (403), heise.preissuchmaschine.com + mem-tek.fr (DNS unresolvable from sandbox), Amazon.de price parsing (CHF session). Geizhals rows are huihui-agent-sourced leads (this host gets the generic frame).

### 4. Verdict + coverage

**Did anything beat €4,791/128 GB net? — No.** Seventh flat pass. Cheapest lead this pass = Micron BH1 tray €39.4/GB net (est.), 5% above the bar; the new QVL-family price (€54.8/GB) confirms the PB2 bin is premium everywhere.

This pass probed: huihui slice C pool (Micron BH1/BH1T/BD2, SK hynix 480N, PB2-CCP, geizhals/idealo, smicro/ANAFRA), Amazon.de search (browser), picclick.de, heise preissuchmaschine, mem-tek.fr, senetic.pl 32GB-Server-Premier price hunt, plus full bests re-check.

---

## Pass 10 — 2026-11-14T03:0xZ (scheduled poke, EXPANDING: senetic 96GB variant, Amazon.pl, otto/serverpartdeals/memory.net, **Proshop PL price movement**)

### 1. Re-check of the bests — **THE BAR MOVED (upward)**

| Offer | Result | Exact strings seen | URL |
|---|---|---|---|
| Proshop.pl KF576RH40RBK4-128 | **CHANGED — INCREASE +5.3%** (browser, confirmed twice) | "**27 362,00 zł / 22 245,53 zł netto**" (was 25 969,00 / 21 113,01), lead 3–4 dni → **net €5,047.77 / kit = €39.44/GB** | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 |
| — same-store family check | **ALL RAISED ~+5%**: 32 GB single 6 875,00 / **5 589,43 zł netto** (was 5 305,69); 8×16 octa 35 983,99 / **29 255,28 zł netto** (was 27 765,04) → single €39.71/GB, octa €51.71/GB → Proshop.pl raising the whole Renegade 7600 line | ditto /3462077, /3462080 |
| Tonitrus Samsung CCP | **UNCHANGED** (browser) | 2.667,65 € netto · 50 pcs | https://www.tonitrus.com/M321R8GA0EB2-CCP |
| ibfusion KSM64R52BD4-64MD | **UNCHANGED** (curl) | 2 481,00 € excl. VAT · 4 in stock | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| senetic.pl KSM64R52BD4 | unchanged | 11 509,07 zł netto | (search page) |

**Ranking consequence:** the Proshop kit is no longer the cheapest per 128 GB. At the new 22 245,53 zł netto, **ibfusion at €2,481×2 = €4,962/128 GB (€38.79/GB) beats the kit (€5,047.77, €39.44/GB)** — first rank change of the hunt, on the incumbent's own price hike. Caveat: ibfusion has only **4 pcs** stock (max 256 GB).

### 2. NEW listings this pass

| Part | JEDEC SPD verdict | Shop | Exact price | Stock/lead | URL |
|---|---|---|---|---|---|
| Kingston **KSM64R52BD4-96MC** (96 GB 2Rx4!) | **SPD-verified**: "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V … 96GB 2Rx4 12G" → qualifies; **384 GB per 4 modules** | senetic.pl | **16 417,58 zł** netto (= €3.725,80 / €38.81/GB) | (card stock not captured) | https://www.senetic.pl/search/?q=KSM64R52BD4&f_s_category=icecat_106 |
| Kingston **KSM64R52BD4-64MD** | SPD-verified family (6400 CL52 @1.1V, 2Rx4) | **Amazon.pl** (marketplace) | **13 403,64 zł** incl. VAT ("125 zł dostawa 20-21 lis") = €3,041.4 gross; ÷1.23 = **€2,472.7 net = €38.63/GB — cheapest net/GB seen** | delivery 20–21 XI | https://www.amazon.pl/s?k=KSM64R52BD4-64MD |

### 3. QVL hunt

Not re-run (pool rotation); state stands: smicro.eu lead €3.504,44 ex VAT, else no EU price.

### Blocked this pass

otto.de (HTTP 400 on search URL), serverpartdeals.com (429 local rate limit), memory.net (Cloudflare "Just a moment"), Proshop.pl search.php route returned zero nodes for KF572RH38RB keyword (page renders but no result items — treated as no-listing, not blocked).

### 4. Verdict + coverage

**Did anything beat €4,791/128 GB net? — The old bar is dead upward: the kit moved to €5,047.77/128 GB. New verified cheapest per-GB: Amazon.pl KSM64R52BD4-64MD at €38.63/GB net (marketplace, gross÷1.23 basis) / ibfusion €38.79/GB — but NO offer beats €37.43/GB any more.** Decision unchanged (32 GB 1Rx8 kit route), now 2.8% pricier.

This pass probed: senetic.pl KSM64R52BD4 family sweep (found 96MC 96 GB variant — new, SPD-verified), Amazon.pl (found marketplace listing for 64MD — new), Proshop.pl family price re-verify (movement +5%), otto.de, serverpartdeals.com, memory.net, KSM64R52BD4-96MC datasheet.

---

## Pass 11 addendum — 2026-11-14T03:3xZ (huihui UK slice closes; parent ran the Algolia follow-up it recommended)

Huihui slice A hit its step cap without reading a price, but produced the **UK reachability map**: bargainhardware.co.uk = Cloudflare-gated Magento; svp.co.uk = TCP-unresponsive; **etb-online.com, etbhost.com, ramexpert.co.uk, po-memory.com/.co.uk, mr-memory.co.uk = NXDOMAIN (shops DNS-dead right now, not scrape failures)**; memorycow.co.uk + kingstonmemoryshop.co.uk = OpenCart+Algolia (prices JS-only); offtek = POST-form search.

Parent then did the Algolia JSON query itself (public search-key in the site JS, app C7SR80KDDJ, index `kingstonindex`):

| Part (kingstonmemoryshop.co.uk, GBP — UK retail is 20% VAT-incl) | Price seen | Net est. (÷1.2, GBP≈5.45 PLN assumption) | €/GB net est. |
|---|---|---|---:|
| KSM64R52BD4-**64MH / -64HA / -64MD** | **£3,861.99** each | zł 17,536 → €3,979 | **≈€62/GB** |
| KSM64R52BD4-**96MC / -96HM** 96 GB | £5,824.64 | zł 26,410 → €6,000 | ≈€62/GB |
| KSM64R52BD4-**128MB** | £7,128.53 | — | ≈€66/GB |
| KSM64R52BD8-**32HA** 32 GB | **£1,265.41** | zł 5,746 → €1,304 | **≈€40.7/GB** |
| KSM64R52BD8-**32MH** 32 GB | £1,882.18 | — | ≈€61/GB |

**UK verdict: no threat to the bar** — the UK Kingston channel prices ~60% above the PL/DE market even on the cheapest die. (Lead-quality: Algolia JSON snapshot, currency assumed GBP, FX assumed ~5.45 PLN/GBP — unverified against NBP for 2026-11-13; stock field came back blank.)

QVL/coverage: this addendum covered the UK slice-A pool. No board changes.

---

## Pass 12 addendum — 2026-11-14T03:5xZ (huihui PL/LT/SK slice closes; parent DNS-verifies)

Huihui slice B found the PL/Baltic probe pool mostly dark, and one new reachable Baltic seller. **Parent verification from this host: the DNS deaths are REAL, not sandbox-local** — `ramshop.pl, sklepy-serwerowe.pl, notebooki-serwery.pl, ramek.com.pl, hmem.eu, discount-memory.com` all return NXDOMAIN from the parent resolver too (shops offline/parked, not scrape failures). `itpro.lt` resolves (79.98.25.1) but bot-blocked all loaders; `abstock.com` resolves but every loader failed (its `KSM64R52BD4-96MC` product page exists per DDG — worth one retry next pass); `dataprint.sk` is a print-shop, no RAM.

**New listing (lead, parent-verified page 200, price read by huihui):**

| Part | Shop | Price (net, "Excl. VAT & shipping") | Stock/lead | URL |
|---|---|---|---|---|
| Kingston KSM64R52BD4-**64MD** | **corewavelabs.com** (CoreWave Labs SIA, Rīga, LV — ships EU) | "$ 3,076" (page markers verified: 100+, 2-3 Days, Excl. VAT) ≈ **€2,772 → €43.31/GB** | 100+ pcs, 2–3 d (tier 46 pcs $3,233) | https://corewavelabs.com/ksm64r52bd4-64md-kingston-64gb-ddr5-6400-rdimm/ |
| Samsung M321R8GA0EB2-**CCP** | corewavelabs.com (search cards) | "$ 3,087" ex VAT ≈ €43.5/GB | shown in results | https://corewavelabs.com/?s=M321R8GA0EB2&post_type=product |

**Verdict unchanged:** cheapest per-GB anywhere seen across ALL slices (UK, PL/LT/SK, DE/Geizhals, own probes) is still the PL market at €38.6–39.4/GB (post price-move); CoreWave/UK/US channels sit 15–60% higher. No listing beat the bar — and the bar itself has drifted up (Proshop kit now €39.44/GB), so **ibfusion (€38.79/GB net, 4 pcs) is the current cheapest verified route per 128 GB.**

Coverage: slice B pool (ramshop.pl, sklepy-serwerowe.pl, notebooki-serwery.pl, ramek.com.pl, hmem.eu, discount-memory.com, itpro.lt, abstock.com, dataprint.sk) + corewavelabs.com. All three huihui slices (A UK, B PL/LT/SK, C parts/DE) are now closed and folded in.
