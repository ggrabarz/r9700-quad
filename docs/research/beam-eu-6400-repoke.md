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
