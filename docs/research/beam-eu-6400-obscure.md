# Beam EU research — DDR5-6400 ECC RDIMM, obscure-shop sweep — 2026-11-13

Scope: cheapest DDR5- **ECC Registered DIMM (RDIMM)**, 288-pin, JEDEC-6400 **SPD at 1.1 V**
(Supermicro H14SSL-NT BIOS is JEDEC-only, no EXPO/XMP), accepting only 16/32/64 GB modules or
kits of 4/8; rejecting UDIMM/SODIMM/CUDIMM and anything that needs EXPO/XMP (1.35–1.4 V) to reach
6400 MHz.

Conv.: PLN → EUR × 4.4070. UK shop prices exclude UK VAT and are post-Brexit imports — **not
directly comparable**. Today: 2026-11-13.

## Slice: DE/AT/FR/IT/ES

### A. Mainstream DE consumer/IT big-box + marketplace slice

| Shop | Part | JEDEC SPD verdict | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 128 GB (4×32) Quad Channel Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC ("JEDEC standard at 1.1 V"); SPD = 6400 MT/s - 1.1 V - CL52 - 52-52-52 | **€5,392.42**, OutOfStock (JSON-LD price; tile showed €5,371.78) | OOS | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-128-gb-4-x-32-gb-quad-channel-kit-black/MEVC-031.html |
| Caseking (DE) | G.Skill Zeta R5 DDR5-6400 CL32, XMP, ECC reg., 128 GB Octa-Kit (8×16) | **REJECTS** — CL32 @ 1.4 V via XMP → not JEDEC-6400/1.1 V | **€1,580.08**, OutOfStock, MEGS-318 | OOS | https://www.caseking.de/en/g.skill-zeta-r5-ddr5-6400-ram-cl32-xmp-ecc-reg.-128-gb-octo-kit-black/MEGS-318.html |
| Caseking (DE) | KLEVV / PATRIOT / V-Color Manta DDR5-6400 CL30–38 kits | **REJECTS** — 6400 reached via XMP 3.0 / EXPO only | various, mostly OutOfStock; e.g. KLEVV CRAS V RGB EXPO CL32 32GB **€517.26** OOS, MEGV/MEKV | mixed | https://www.caseking.de/en/pc-components/memory/ddr5/6400-mhz-ddr5-ram |

### B. Server-specialist slice (DE/AT/FR/IT/ES)

| Shop | Part | JEDEC SPD verdict | Exact price + currency | Stock / lead | URL |
|---|---|---|---|---|---|
| ibfusion (DE/ES) | Kingston KSM64R52BD4-64MD (64 GB, 2Rx4) | **QUALIFIES** — "SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." | **€2,481.00 excl. VAT (€2,681.96 incl. 8.1 % CH VAT)**, 4 in stock | EU delivery 7–21 business days | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ |
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 256 GB (8×32) Octa-Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC | **€12,784.85**, OutOfStock | OOS | https://www.caseking.de/en/v-color-rdimm-ddr5-6400-ram-cl52-jedec-256-gb-octa-kit-black/MEVC-033.html |
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 64 GB (4×16) Quad Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC | **€3,386.92**, OutOfStock | OOS | https://www.caseking.de/en/v-color-rdimm-jedec-ddr5-6400-ram-cl52-64-gb-4-x-16-gb-quad-channel-kit-black/MEVC-025.html |
| Caseking (DE) | V-Color R-DIMM JEDEC DDR5-6400 CL52, 128 GB (8×16) Octa-Kit | **QUALIFIES** — JEDEC 6400 CL52 1.1 V, ECC | **€6,775.97**, OutOfStock | OOS | https://www.caseking.de/en/v-color-rdimm-ddr5-6400-ram-cl52-jedec-128-gb-octa-kit-black/MEVC-027.html |

### C. Other slice shops checked this pass

| Shop | Part | JEDEC SPD verdict | Exact price + currency | Stock / lead | URL | Note |
|---|---|---|---|---|---|---|
| Proshop (PL/DE) | Kingston FURY Renegade PRO `KF576RH40RBK4-128` (4×32 GB) | **QUALIFIES** — SPD 6400 MT/s - 1.1 V - CL52 - 52-52-52; XMP 7600 @ 1.4 V (not used) | **€4,791 net** (25 969 zł / 21 113,01 zł netto; ×4.4070) | max 2 szt./client; sourced from Proshop | https://www.proshop.pl/RAM/Kingston-Fury-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079 | €37.43/GB net — baseline to beat |
| Thomas-Krenn (DE) | — | — | — | no relevant 6400 RDIMM hit retrieved | — | no product result |
| Happyware (DE) | — | — | — | no relevant 6400 RDIMM hit retrieved | — | no product result |
| Plexcom (FR) | — | — | — | — | — | no relevant hit retrieved |
| itsco (IT) | — | — | — | — | — | no relevant hit retrieved |
| servershop24 (DE) | — | — | — | only server bundles w/ DDR5, no bare DIMM | — | no DIMM hit |
| memorysolution (DE) | — | — | — | no relevant hit retrieved | — | no DIMM hit |

## Blocked / unreachable (this pass)

- **Alternate.de** — search endpoints returned 404 / no result rows retrieved (blocked/no data).
- **Mindfactory** — Cloudflare managed challenge ("Just a moment…") → blocked.
- **Cyberport** — Cloudflare managed challenge → blocked.
- **notebooksbilliger.de** — 404 → unreachable/no data.
- **computeruniverse.de** — 403 → blocked.
- **Snogard** — request timeout → unreachable.
- **Kaufland.de** (marketplace) — 403 → blocked; no verified server-RAM seller retrieved.
- **Galaxus.de / Galaxus.at** — 403 → blocked.
- **senetic.fr** — "Rien trouvé" (no 6400 RDIMM results); senetic.de/.it/.es not re-verified this pass.
- **Fujitsu TS parts channel** — HTTP 429 rate-limited → blocked.
- **Interdiscount.ch** — 403 → blocked (CH VAT note applies if retried).
- **digitec.ch** — 403 → blocked.
- **Terra PC** — SSL certificate mismatch → unreachable.
- **server-warehouse.de / raidlinks.de** — DNS unresolvable → unreachable.
- **Tonitrus** — r.jina.ai returned 403 Forbidden (bot-wall tightened); last verified state €2,667.65 net / 50 in stock (17:4xZ) — BLOCKED this pass.
- **Proshop.de** — Cloudflare 403 "Attention Required" — unchanged since prior pass.
- **geizhals.eu / skinflint.co.uk** — Cloudflare bot-wall / CAPTCHA → blocked (index-only lead list, unverified).

## Verdict — does anything beat €37.43/GB net?

**No.** Nothing verified this pass beat the €37.43/GB net baseline (Kingston `KF576RH40RBK4-128` 4×32 GB Proshop.pl kit, €4,791 net / 128 GB).

- Best qualifying single module this pass: **ibfusion `KSM64R52BD4-64MD`** — €2,481 net (VAT 0 %) / 64 GB = **€38.77/GB net** → does **not** beat €37.43/GB, and was already known.
- Caseking's only in-stock JEDEC-6400 ECC RDIMM listings (V-Color R-DIMM JEDEC) are **OutOfStock**; its cheaper ECC kit (G.Skill Zeta R5 CL32 XMP ECC) was rejected (XMP 1.4 V, not JEDEC-1.1 V) and the V-Color JEDEC 128 GB kit sits at **€42.13/GB** OOS.
- Everything cheaper seen on Caseking (KLEVV/PATRIOT/V-Color Manta, EXPO) was **rejected** (needs EXPO).
- ibfusion KSM64R52BD4-64MD remains the cheapest confirmed qualifying source at **~€2,481 net / 64 GB (€38.77/GB)**; the 4×32 GB Proshop.pl kit at **€4,791 net (€37.43/GB)** stays the current net-best per GB.

**Bottom line:** no new or obscure-shop offer this pass beat the €37.43/GB net bar; the bar stands.

---

### Slice notes (DE/AT/FR/IT/ES)

- Caseking (DE) is the only DE slice shop that surfaced JEDEC-6400 ECC RDIMM stock data; all of it OutOfStock, and its only in-stock 6400 kits were EXPO/XMP gaming modules → correctly excluded.
- ibfusion (DE/ES) is the only confirmed qualifying, in-stock, VAT-excluded source this pass; no competitor undercut it on a per-GB basis.
- All other slice shops (Mindfactory, Cyberport, Galaxus, Kaufland, Otto, Interdiscount, digitec, notebooksbilliger, computeruniverse, Snogard, Happyware, Plexcom, itsco, Thomas-Krenn, senetic*, servershop24, memorysolution, Dell/HP/Fujitsu/PC-Specialist outlets, Terra PC, raidlinks, server-warehouse) returned no verifiable qualifying price this pass — blocked, unreachable, or no relevant hit.
