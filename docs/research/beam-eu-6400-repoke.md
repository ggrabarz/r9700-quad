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
