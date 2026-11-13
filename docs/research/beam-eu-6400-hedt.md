# EU-buyable DDR5-6400 RDIMMs for the JEDEC-only H14SSL-N/NT (HEDT OC lines)

Fetch date: **2026-11-13**. Qualification rule (decisive): a module counts only if its **SPD default at 1.1 V** is DDR5-6400 — the H14SSL-N/NT BIOS has no EXPO/XMP menu, no DIMM voltage control, and its "Memory Target Speed" list stops at 5200. 288-pin DDR5 **RDIMM registered ECC** only; UDIMM/SODIMM/CUDIMM excluded.

## What I checked

- Kingston FURY Renegade Pro DDR5 RDIMM datasheets (`kingston.com/datasheets/<PN>.pdf`) for every SKU the product page lists (singles 16/32 GB, 4-kit 64/128 GB, 8-kit 128/256 GB across 5600/6000/6400/7200/7600) — 24 part numbers fetched and the SPD sentence quoted.
- Kingston server line: `KSM64R52BD4-64MD` datasheet (JEDEC-6400 CL52 1.1 V) and parent-verified Micron `MTC40F2046S1RC64BH1` / Supermicro QVL `MEM-DR564MC-ER64`.
- G.Skill Zeta R5 / Zeta R5 Neo / T5 Neo product pages; Corsair WS DDR5 RDIMM; V-Color OC R-DIMM; TeamGroup T-Create Master OC RDIMM — all checked for a stated JEDEC SPD speed.
- EU shops: Proshop.de (fetched product pages incl. stock/limit), Proshop.pl prices from parent snapshot, Galaxus.de prices from parent snapshot.
- Blocked: Geizhals, idealo, Newegg, Mouser, Mindfactory, Alternate, Caseking product pages returned bot walls for this host — prices/stock not invented.

## Table 1 — SKU → JEDEC SPD verdict

Kingston FURY Renegade Pro (all SKUs 288-pin DDR5 RDIMM, ECC; graphene label ≤6400 = 31.25 mm high, aluminium heat spreader ≥7200 = 34.12 mm high):

| Part number | Capacity / ranks | JEDEC SPD default + V | Verdict |
|---|---|---|---|
| KF556R36RB-16 | 16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF556R36RBK4-64 | 4×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF556R36RBK8-128 | 8×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF556R36RBK8-256 | 8×32 GB 1Rx4 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF556R28RBE2K4-128 | 4×32 GB 2Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF556R28RBE2K8-256 | 8×32 GB 2Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF560R32RB-32 | 32 GB 1Rx4 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF560R32RBEK4-64 | 4×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF560R32RBK4-64 | 4×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF560R32RBEK4-128 | 4×32 GB 1Rx4 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF560R32RBK8-128 | 8×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF564R32RB-32 | 32 GB 1Rx4 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF564R32RBEK4-64 | 4×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF564R32RBK4-64 | 4×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF564R32RBEK4-128 | 4×32 GB 1Rx4 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF564R32RBK8-128 | 8×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF564R32RBEK8-128 | 8×16 GB 1Rx8 | DDR5-4800 CL40-39-39 @1.1 V | FAIL |
| KF572RH38RB-32 | 32 GB 1Rx8 | DDR5-6400 CL52-52-52 @1.1 V | PASS |
| KF572RH38RBK4-128 | 4×32 GB 1Rx8 | DDR5-6400 CL52-52-52 @1.1 V | PASS |
| KF572RH38RBK8-128 | 8×16 GB 1Rx8 | DDR5-6400 CL52-52-52 @1.1 V | PASS |
| KF572RH38RBK8-256 | 8×32 GB 1Rx8 | DDR5-6400 CL52-52-52 @1.1 V | PASS |
| KF576RH40RB-32 | 32 GB 1Rx8 | DDR5-6400 CL52-52-52 @1.1 V | PASS |
| KF576RH40RBK4-64 | 4×16 GB 1Rx8 | DDR5-6400 CL52-52-52 @1.1 V | PASS |
| KF576RH40RBK4-128 | 4×32 GB 1Rx8 | DDR5-6400 CL52-52-52 @1.1 V | PASS |

Kingston server / other verified:

| Part number | Capacity / ranks | JEDEC SPD default + V | Verdict |
|---|---|---|---|
| KSM64R52BD4-64MD | 64 GB 2Rx4 | DDR5-6400 CL52 @1.1 V | PASS |
| MTC40F2046S1RC64BH1 (Micron) | 64 GB 2Rx4 | DDR5-6400 CL52 @1.1 V | PASS |
| MEM-DR564MC-ER64 (Supermicro QVL) | 64 GB 2Rx4 | QVL-listed DDR5-6400 (datasheet not fetched) | PASS (per QVL) |

HEDT OC lines whose datasheets/product pages do **not** state a JEDEC SPD speed (mark UNVERIFIED; treat as non-qualifying until proven otherwise):

| Line / example PN | Rated | JEDEC SPD stated? | Verdict |
|---|---|---|---|
| G.Skill Zeta R5 Neo (F5-6400R3239G32GQ4-ZR5NK, F5-6400R3239G16GE8-ZR5NK, F5-6400R3239G48GQ4-ZR5NK) | DDR5-6400 CL32 1.40 V EXPO/XMP | No | UNVERIFIED |
| G.Skill Zeta R5 (Intel XMP) | DDR5-6400 CL32 1.40 V | No | UNVERIFIED |
| G.Skill T5 Neo (F5-6400R3644E64GQ4-T5N, F5-6400R3848F64GE8-T5N) | DDR5-6400 CL36/CL38 1.30/1.35 V EXPO | No | UNVERIFIED |
| Corsair WS DDR5 RDIMM (CMA…5600/6400) | 5600–6400 MT/s XMP/EXPO | No | UNVERIFIED |
| V-Color OC R-DIMM (TRA5…6000/6400) | 6000–6400 MT/s 1.25–1.4 V EXPO | No (V-Color does ship a separate "JEDEC" 4800 kit) | UNVERIFIED |
| TeamGroup T-Create Master OC RDIMM (CTCMD5…6400) | DDR5-6400 CL32 1.40 V XMP | No | UNVERIFIED |

## Table 2 — qualifying SKU → EU price / stock

| SKU | EU shop | Price | Stock / lead | URL | Notes |
|---|---|---|---|---|---|
| KF576RH40RBK4-128 (4×32 GB, 7600, JEDEC-6400) | Proshop.de | €5,739.82 (€4,797.07 ex VAT) | Bestellware 3–5 Tage; **max 2 pcs/customer** | https://www.proshop.de/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Schwarz/3462079 | 3 kits = 12×32 GB = 384 GB; needs 3 separate orders/accounts (limit 2) |
| KF576RH40RBK4-64 (4×16 GB, 7600) | Proshop.de | €3,777.63 | Bestellware 3–5 Tage; max 2 pcs/customer | https://www.proshop.de/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-64GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Schwarz/3462078 | |
| KF576RH40RB-32 (1×32 GB, 7600) | Proshop.de | €1,439.07 | Bestellware 3–5 Tage; max 2 pcs/customer | https://www.proshop.de/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-32GB-CL38-Single-Channel-1-pcs-AMD-EXPO-Intel-EXPO-Schwarz/3462077 | |
| KF576RH40RB-16 (1×16 GB, 7600) | Proshop.de | €948.51 (€797.07 ex VAT) | Bestellware 3–5 Tage; max 2 pcs/customer | https://www.proshop.de/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-16GB-CL38-Single-Channel-1-pcs-AMD-EXPO-Intel-EXPO-Schwarz/3462076 | |
| KF572RH38RBK8-256 (8×32 GB, 7200) | Proshop.pl | 50 712,00 zł ≈ €11,507 gross (€9,356 net) | not captured; check page | https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7200-256GB-CL38-Octa-Channel-8-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462075 | 256 GB in 8 of 12 channels |
| KF572RH38RB-16 (1×16 GB, 7200) | Proshop.de | €926.57 (search snippet) | Bestellware 3–5 Tage; max 2 pcs/customer | https://www.proshop.de/RAM/Kingston-FURY-Renegade-PRO-DDR5-7200-16GB-CL38-Single-Channel-1-pcs-AMD-EXPO-Intel-EXPO-Schwarz/3462066 | SPD printed as 6400 MT/s @1.1 V CL52 |
| KSM64R52BD4-64MD (64 GB, JEDEC) | Galaxus.de | €3,202.74 | not captured; single listing | https://www.galaxus.de/de/s1/product/kingston-ksm64r52bd4-1-x-64gb-6400-mhz-ddr5-ram-dimm-ram-52967925 | Server RDIMM, no EXPO needed |
| MTC40F2046S1RC64BH1 (Micron, 64 GB, JEDEC) | Galaxus.de | €3,279.97 | not captured; single listing | https://www.galaxus.de/de/s1/product/micron-crucial-64-gb-reg-ecc-ddr5-6400-mtc40f2046s1rc64bh1-6400-mhz-ddr5-ram-dimm-ram-68867097 | 2×64 = 128 GB / 2 channels start |
| MEM-DR564MC-ER64 (Supermicro QVL, 64 GB) | — | not found in EU retail | n/a | — | QVL part; no price/stock captured |

## Could not verify / blocked

- Bot walls: Geizhals, idealo, Newegg, Mouser, Mindfactory, Alternate, Caseking, Galaxus search returned challenges for this host — any price/stock there is **not** claimed.
- No 7600 8-module kit exists in Kingston's datasheet set (`KF576…K8-*` all 404); 384 GB needs 3× 4-module kits.
- Proshop's **max 2 pcs/customer** on Renegade Pro pages blocks a single 3-kit order; plan multiple orders/accounts.
- Mechanical: 7200+ modules use the **34.12 mm aluminium heat spreader** vs 31.25 mm PCB-only graphene modules; whether they clear the DIMM channels next to an EPYC 9555 socket on the H14SSL-N is **unverified** — flag as risk, not a guess.
- JEDEC SPD speed is not published for G.Skill Zeta R5/Neo, T5 Neo, Corsair WS, V-Color OC and TeamGroup T-Create OC lines; all marked UNVERIFIED (default likely 4800/5600, but not proven).

## Best test-purchase recommendation

Buy one **KF576RH40RBK4-128** (4×32 GB, 7600, JEDEC-6400 SPD at 1.1 V) from Proshop.de at €5,739.82 (3–5 days, max 2/customer) and validate it in a single H14SSL-N before committing to the 3-kit/384 GB order.