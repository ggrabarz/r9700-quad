# Beam EU research — DDR5-6400 RDIMMs that run at 6400 on H14SSL-N/NT (JEDEC SPD, EU buyable)

Fetch date: 2026-11-13. Scope: QVL / special-order channel for the Supermicro H14SSL-N/-NT (Turin, 12-channel, JEDEC-only BIOS).

## What I checked

- Supermicro H14SSL-N/-NT memory QVL: one 6400 entry only — `MEM-DR564MC-ER64` (64GB DDR5-6400 2Rx4 ECC RDIMM, low profile).
- Manufacturer datasheets: Kingston datasheets (`https://www.kingston.com/datasheets/<PART>.pdf`) fetched with `pdftotext`; SPD sentence quoted per qualifying part. Micron/Samsung/Supermicro/Innodisk/ADATA/SMART/ATP/Virtium/NEMIX/A-Tech pages checked for SPD wording.
- EU distributors and shops: Plexcom, Happyware, senetic.de, servershop24, itsco, Thomas-Krenn, ComputerUniverse, Snogard, Memorysolution, datacenterdisk, ibfusion, idealo/heise price comparison, plus AB/ALSO/Action (PL). Bot walls recorded as blocked rather than guessed.
- Third-party “same class” brands: SMART Modular, Innodisk, ATP, ADATA (TRUSTA), Virtium, NEMIX, A-Tech, RAM-Quote.
- Explicitly excluded: UDIMM/SODIMM/CUDIMM (wrong form factor), EXPO/XMP-rated 6400 kits whose JEDEC SPD default is below 6400 (e.g. Kingston `KF564R32RBE` = JEDEC-4800), and 4800/5600-only bins.

## Results table

| Part number | Capacity / ranks | JEDEC SPD default + voltage | EU shop | Price | Stock / lead | URL | Notes |
|---|---|---|---|---|---|---|---|
| Supermicro `MEM-DR564MC-ER64` | 64GB 2Rx4 (16Gb), low profile | JEDEC DDR5-6400 CL52 1.1V (QVL-tested module) | none found (special order) | not public; US: Supermicro eStore $2,860; ServerSupply $4,000 new | order-only | https://store.supermicro.com/us_en/supermicro-micron-64gb-288-pin-ddr5-6400-pc5-38400-server-memory-mem-dr564mc-er64.html | The only 6400 entry on the H14SSL-N/-NT Turin QVL. EU distributors quote on request. |
| Kingston `KSM64R52BD4-64MD` | 64GB 2Rx4 X4, Micron D-die | “SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V.” | ibfusion.com | €2,481.00 excl. VAT (€2,681.96 incl. 8.1% CH VAT) | 4 in stock; EU delivery 7–21 business days | https://ibfusion.com/ram/64gb-ddr5-rdimm-ecc-6400mhz/ | Confirmed qualifying; idealo snippet “ab 2.980,41 €”. |
| Kingston `KSM64R52BD4-64HA` | 64GB 2Rx4 X4, Hynix A-die | “SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V.” | heise/preisvergleich (Jacob Elektronik / Nexus) | €3,674.93 (Jacob, +€2.99 ship) / €3,674.95 (Nexus) | Jacob 1–2 weeks; Nexus “Sofort lieferbar, 2–3 Werktage” | https://preisvergleich.heise.de/kingston-server-premier-rdimm-64gb-ksm64r52bd4-64ha-a3590377.html | Confirmed qualifying. |
| Kingston `KSM64R52BD4-64MH` | 64GB 2Rx4 X4, Micron H-die | Same Server Premier family; SPD quote not re-fetched this run (Kingston datasheet blocked by Cloudflare) — UNVERIFIED | none found | not priced | n/a | https://www.kingston.com/en/memory/server-premier/ddr5-6400mts-ecc-registered-dimm | Treat as unverified until datasheet is read. |
| Kingston `KSM64R52BD8-32MH` | 32GB 2Rx8 X8, Micron H-die | “The SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V.” | ibfusion.com (as equivalent) | €1,598.00 (ibfusion 32GB page) | 4 in stock; EU delivery 11–24 business days | https://ibfusion.com/ram/32gb-ddr5-6400-ecc-rdimm/ | Confirmed qualifying; 12× = 384GB at 6400. |
| Kingston `KSM64R52BS8-16MH` | 16GB 1Rx8 X8, Micron H-die | “SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V.” | none found | not priced EU | n/a | https://www.kingston.com/datasheets/KSM64R52BS8-16MH.pdf | Qualifies but 16GB is not preferred; 12× = 192GB. |
| Samsung `M321R4GA3EB2-CCP` | 32GB 2Rx8 X8 | CL52 at 1.1V (ServerSupply); JEDEC SPD sentence not fetched — UNVERIFIED wording | ibfusion.com | €1,598.00 excl. VAT (€1,727.44 incl. CH VAT) | 4 in stock; EU delivery 11–24 business days | https://ibfusion.com/ram/32gb-ddr5-6400-ecc-rdimm/ | Confirmed buyable in EU; ibfusion lists SK Hynix / Micron / Kingston / Lenovo / HPE / Dell / Supermicro equivalents. |
| Micron `MTC40F2046S1RC64BH1` / `BD2` | 64GB 2Rx4 | Micron server DRAM DDR5-6400 CL52 1.1V (Micron/Crucial); JEDEC SPD sentence not fetched — UNVERIFIED | none found (Mouser/Avnet US, ServerSupply US) | not public in EU (ServerSupply US $4,000 new) | US stock only | https://www.micron.com/products/memory/dram-modules/rdimm/part-catalog/part-detail/mtc40f2046s1rc64bh1 | Same silicon class as Supermicro QVL part; order via distributor. |
| Innodisk DDR5 6400 RDIMM | 16–64GB | 1.1V listed; JEDEC SPD default not stated on product page — UNVERIFIED | none found (contact Innodisk) | not public | order-only | https://www.innodisk.com/en/products/dram-modules/ddr5/ddr5-6400-rdimm | No EU retail price found. |
| ADATA TRUSTA RDIMM DDR5 6400 | up to 128GB | Vendor claims JEDEC compliance; SPD sentence not fetched — UNVERIFIED | none found | not public | n/a | https://trusta.adata.com/en/product/dram/r-dimm/ | No EU retail price found. |
| SMART Modular (Penguin) DDR5 RDIMM | up to 256GB | Vendor states 4800–6400 MT/s; JEDEC SPD default not quoted — UNVERIFIED | none found | not public | n/a | https://www.penguinsolutions.com/en-us/products/smart-modular/ddr5-rdimm | No EU retail price found. |
| ATP wide-temperature DDR5 RDIMM | 16–256GB | Vendor states up to 7200 MT/s; SPD not quoted — UNVERIFIED | none found | not public | n/a | https://www.atpinc.com/products/DDR5-wide-temperature-operable-DIMM | No EU retail price found. |
| NEMIX DDR5 6400 RDIMM | 16–256GB | Vendor “JEDEC-compliant”, 1.1V | none found (US) | not public in EU | US stock | https://nemixram.com/products/ddr5-6400mhz-pc5-51200-rdimm | US-based; special order only. |
| A-Tech 64GB DDR5 6400 RDIMM | 64GB 2Rx4 | “JEDEC DDR5 standard 1.1V” (Amazon listing) | none found (US) | datacenterdisk.com quotes $3,109.55 | US only | https://datacenterdisk.com/drives/a-tech-64gb-ddr5-6400-jxrh | Not EU-buyable. |

Not qualifying (noted and moved on): UDIMM/SODIMM/CUDIMM (including ADATA 6400 CUDIMM), EXPO/XMP 6400 kits whose JEDEC SPD default is below 6400 (Kingston `KF564R32RBE` = JEDEC-4800), Virtium (only 4800/5600), RAM-Quote (no 6400 RDIMM listing found), G.Skill 6400 CL32 kits (JEDEC SPD not verified this run).

## Could not verify / blocked

- Distributors with no public 6400 RDIMM listing: Plexcom (consumer DDR5 page only), Happyware (no product hit), servershop24 (no product hit), itsco (HTTP 500), Thomas-Krenn (404 search), Memorysolution (no relevant 6400 RDIMM), datacenterdisk (no exact part; price tracker only), Snogard (timeout), ComputerUniverse (403), AB/ALSO/Action (PL, 404/no listing).
- senetic.de: search returns 13 fuzzy hits including Supermicro `MEM-DR564MC-ER48` (not ER64); exact `MEM-DR564MC-ER64` not listed and Supermicro module prices are hidden (`show_price=false`) — quote on request.
- Supermicro `MEM-DR564MC-ER64` has no EU retail price found; directmacro.com is Cloudflare-blocked; only US channels (Supermicro eStore $2,860, ServerSupply $4,000 new/refurbished, eBay UK “compatible” listings) are visible.
- Kingston datasheets for `KSM64R52BD4-64MH` were blocked by Cloudflare this run, so that row is marked UNVERIFIED despite family match.
- Micron/Samsung/Supermicro third-party SPD sentences were not found verbatim; their 1.1V DDR5-6400 CL52 specs are consistent with JEDEC 6400 but the exact SPD-programming sentence was only quoted from Kingston datasheets.

## Top-line list by cost per 12 DIMMs (confirmed qualifying)

1. Samsung `M321R4GA3EB2-CCP` 32GB (ibfusion) — €1,598.00 × 12 = **€19,176** (384GB total).
2. Kingston `KSM64R52BD8-32MH` 32GB (ibfusion equivalent) — €1,598.00 × 12 = **€19,176** (384GB total).
3. Kingston `KSM64R52BD4-64MD` 64GB (ibfusion) — €2,481.00 × 12 = **€29,772** (768GB total).
4. Kingston `KSM64R52BD4-64HA` 64GB (heise/Nexus) — €3,674.95 × 12 = **€44,099** (768GB total).
5. Supermicro `MEM-DR564MC-ER64` 64GB — no EU price; US eStore $2,860 only.
6. Micron `MTC40F2046S1RC64BH1` / `BD2` 64GB — no EU price; US channels only.
