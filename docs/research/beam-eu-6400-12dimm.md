# DDR5-6400 RDIMMs that are JEDEC-6400 at 1.1 V and buyable in the EU

Research sub-agent output for the H14SSL-N/NT (Supermicro, EPYC 9555, 12 slots, 1DPC) question.
Fetch date for all prices/quotes: 2026-11-13. Prices are the exact strings seen on the fetched pages.

## What I checked

- Kingston datasheets fetched as `https://www.kingston.com/datasheets/<PART>.pdf` and read with `pdftotext` (cached PDFs in /tmp/opencode from prior passes: KSM64R52BD4-64MD, KSM64R52BD4-64HA, KSM64R52BD4-64MH, KSM64R52BD8-32HA, KSM64R52BD8-32MH, KF572RH38RBK8-256, KF576RH40RBK4-128, KF564R32RBEK4-128).
- Galaxus DE search (`r.jina.ai` on galaxus.de/de/search) for candidate part numbers and generic "6400 RDIMM" listings.
- DuckDuckGo lite for Supermicro MEM-DR564MC-ER64, Micron MTC40F2046S1RC64BH1, Samsung M321R4GA0PB2, H14SSL BIOS, forum/memory reports.
- Supermicro H14SSL-N and H14SSL-NT product + BIOS-download pages and their RSS feeds.
- Supermicro H13SSL-N product page (for the rev 2.0 vs 2.01 memory-speed evidence).
- H14 manual `h14man.pdf` (cached) for the "Memory Target Speed" menu text.

## Results table (qualifying = JEDEC SPD default is DDR5-6400 at 1.1 V)

| Part number | Capacity / ranks | JEDEC SPD default + voltage | EU shop | Price | Stock / lead | URL | notes |
|---|---|---|---|---|---|---|---|
| Kingston KSM64R52BD4-64MD (and -64HA / -64MH) | 64 GB, 2Rx4 | "The SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." (KSM64R52BD4-64MD.pdf p.1); same sentence for -64HA/-64MH | Galaxus DE | EUR 3149,– (KSM64R52BD4, truncated listing) / EUR 3262,26 (Kingston "DDR5 64GB PC 6400 CL52 Server Premier ECC Reg retail") | not shown (captcha on product page) | https://www.galaxus.de/de/s1/product/kingston-ksm64r52bd4-1-x-64gb-6400-mhz-ddr5-ram-dimm-ram-52967925 | D-die (-64MD) = Micron DRAM; -64HA = Hynix A-die; -64MH = Micron H-die. All three datasheets quote the same JEDEC-6400/1.1 V sentence. |
| Kingston KSM64R52BD8-32HA (and -32MH) | 32 GB, 2Rx8 | "The SPD is programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V." (KSM64R52BD8-32HA.pdf p.1) | Galaxus DE | EUR 1445,17 / EUR 1457,21 ("Kingston 32GB DDR5 6400MT/s ECC Reg 2Rx8 Module") and EUR 1445,54 ("Kingston DDR5 32GB PC 6400 CL52 Server Premier ECC Reg retail") | not shown | https://www.galaxus.de/de/s1/product/kingston-32gb-ddr5-6400mts-ecc-reg-2rx8-module-1-x-32gb-6400-mhz-ddr5-ram-dimm-ram-61921052 | 32 GB option for 12-slot boards; same JEDEC sentence. |
| Micron MTC40F2046S1RC64BH1 | 64 GB, 2Rx4 | JEDEC 6400 CL52 at 1.1 V per reseller listing + project record; manufacturer SPD sentence NOT fetched (UNVERIFIED quote) | Galaxus DE | EUR 3363,96 | not shown | https://www.galaxus.de/de/s1/product/micron-crucial-64-gb-reg-ecc-ddr5-6400-mtc40f2046s1rc64bh1-6400-mhz-ddr5-ram-dimm-ram-68867097 | Project docs already mark this part "JEDEC 2Rx4, CL52, 1.1 V, manufacturer-confirmed"; Micron datasheet PDF was not retrievable in this pass. |
| Supermicro MEM-DR564MC-ER64 (QVL part) | 64 GB, 2Rx4, CL52, 1.1 V | QVL/listing: "64GB 2Rx4 DDR5-6400 ECC RDIMM" (parent-verified PASS) | eBay UK | EUR 1.919,00 (2 available) | "New", 2 available (from DDG snippet) | https://www.ebay.co.uk/itm/336407366489 | Price/stock taken from the DuckDuckGo snippet; the eBay item page returned 403. US alternative: ServerSupply.com $3.700,00 refurbished, in stock, US-only shipping (freight forwarder needed). |
| Samsung M321R4GA0PB2-CCP (probable Galaxus listing) | 32 GB, 1Rx4, CL52, 1.1 V | Reseller claim: "JEDEC PC5-51200R compliant, 1.1 V"; manufacturer SPD sentence NOT fetched (UNVERIFIED) | Galaxus DE | EUR 1.906,81 ("Samsung RAM D5 6400 32GB ECC R") | not shown | https://www.galaxus.de/de/s1/product/samsung-ram-d5-6400-32gb-ecc-r-1-x-32gb-ddr5-ram-dimm-ram-65624127 | Galaxus does not print the Samsung part number; mapped to M321R4GA0PB2-CCP via reseller listings (corewavelabs/globalmemorysupply). Mark UNVERIFIED until Samsung datasheet is read. |
| Samsung "RAM D5 6400 64GB ECC R" (part unknown) | 64 GB, ranks unconfirmed | Reseller claim only; UNVERIFIED | Galaxus DE | EUR 3.481,15 | not shown | https://www.galaxus.de/de/s1/product/samsung-ram-d5-6400-64gb-ecc-r-1-x-64gb-6400-mhz-ddr5-ram-dimm-ram-65624129 | Part number not printed; no manufacturer datasheet quote. Treat as candidate only. |
| Micron / Crucial 32 GB 6400 CL52 2Rx8 | 32 GB, 2Rx8 | UNVERIFIED (Micron server RDIMM; JEDEC assumed, datasheet not fetched) | Galaxus DE | EUR 1.932,87 ("Crucial DDR5 RDIMM 2Rx8 6400 CL52") / EUR 2.089,00 ("Micron 32GB 6400MHz CL52 2Rx8 RDIMM (16Gbit) TRAY") | not shown | https://www.galaxus.de/de/s1/product/crucial-ddr5-rdimm-2rx8-6400-cl52-1-x-32gb-ddr5-ram-r-dimm-ram-68946303 | JEDEC quote missing; do not order without verifying the Micron SPD sentence. |

## Could not verify / blocked

- **Kingston KF572RH38RB (32 GB, 1Rx8) and KF576RH40RB (32 GB, 1Rx8)** — datasheets qualify them: kit KF572RH38RBK8-256 says "The SPDs are programmed to JEDEC standard latency DDR5-6400 timing of 52-52-52 at 1.1V"; KF576RH40RBK4-128 says the same. But no EU single-module retail listing was found in this pass (Galaxus/Proshop searches returned no exact hit). They are sold as kits (KF572RH38RBK8-256 = 8×32 GB; KF576RH40RBK4-128 = 4×32 GB) via Kingston resellers; EU availability/price/stock UNVERIFIED.
- **Kingston KF564R32RBE (32 GB, 1Rx4, "6400 CL32")** — FAILS: kit datasheet KF564R32RBEK4-128 says "The SPDs are programmed to JEDEC standard latency DDR5-4800 timing of 40-39-39 at 1.1V." Not qualifying despite the 6400 XMP/EXPO rating.
- **Supermicro MEM-DR564L-CL01-ER64 / -HL01-ER64 / -SL02-ER64** — third-party "compatible" 64 GB 6400 modules (ServerSupply $3.470,00 refurbished; corewavelabs "100% JEDEC compliant"). Not on Supermicro's QVL; SPD sentence not verified against a manufacturer datasheet. Excluded from the qualifying table.
- **NEMIX / CloudNinjas "compatible" kits** for H13/H14 — no manufacturer part number, JEDEC claim only, no EU shop price/stock verified.
- **Geizhals / idealo / Newegg / Mouser** — blocked (403/bot wall) for price comparison; only Galaxus DE and ServerSupply US prices above are from fetched pages.
- **Kingston "DDR5 64GB PC 6400 CL52 Server Premier ECC Reg retail" (Galaxus EUR 3.262,26)** and **"Kingston 64GB DDR5 6400MT/s ECC Reg 2Rx4 Module" (EUR 3.985,72)** — likely KSM64R52BD4 variants but the exact die suffix is not printed on the Galaxus listing; treated as the same JEDEC-6400 family.

## Risk / real-world evidence

### Evidence table

| Claim | Source URL | Quote | Confidence |
|---|---|---|---|
| H14SSL-N/NT board spec advertises DDR5-6400 at 12 DIMMs (1DPC) | https://www.supermicro.com/en/products/motherboard/H14SSL-N (fetched) | "Support up to DDR5 12 DIMM slots (1DPC), speed up to 6400MT/s" | High |
| H14 manual lists Memory Target Speed options Auto/3600/4000/4400/4800/5200 only (no 6400 entry) | cached h14man.pdf p. (Memory Configuration) | "Use this setting to specify the memory target speed in MT/s. The options are Auto, DDR3600, DDR4000, DDR4400, DDR4800, and DDR5200." | High |
| H13SSL-N rev 2.0 supports 6000, rev 2.01 supports 6400 (board/BIOS sets the ceiling) | https://www.supermicro.com/en/products/motherboard/H13SSL-N (fetched) | "Max Memory (1DPC): Up to 3TB 6000MT/s ECC DDR5 RDIMM (AMD EPYC 9005 Series Processor, MB R2.0)" and "Up to 3TB 6400MT/s ECC DDR5 RDIMM (AMD EPYC 9005 Series Processor, MB R2.01)" | High |
| EPYC 9005 (Turin) official 1DPC speed is DDR5-6400 | https://www.kingston.com/en/memory/server-memory/turin (cited in project docs) | "AMD lists DDR5-6400 1DPC" | Medium |
| No public user report found of 12× off-QVL JEDEC-6400 modules training on H14SSL-N/NT | ServeTheHome forums search + Reddit (blocked) | Search returned H14SSL threads about GPUs/M.2/POST codes, none about 12-DIMM 6400 memory training | Medium (null result) |
| Latest BIOS bundle for MBD-H14SSL-N / MBD-H14SSL-NT is H14SSL_2.0 (BIOS 2.0, BMC 01.07.05.01), published 2026-06-17 | https://www.supermicro.com/en/support/resources/downloadcenter/firmware/MBD-H14SSL-N/BIOS (fetched) + RSS feed | RSS: `<pubDate>Wed, 17 Jun 2026 03:48:53 -0700</pubDate>`; "BIOS Revision: 2.0"; "BMC Firmware Revision: 01.07.05.01" | High (version/date); Low (content) |
| BIOS release notes are JS-gated and were not readable; no memory-speed or memory-profile line could be verified | same download page | "BIOS Release Notes" link is `javascript:void(0)` | High (inaccessibility) |
| Whether the board auto-trains a JEDEC-6400 SPD to 6400 despite the menu listing only up to 5200 is not documented; Auto is the only path that could do it | inferred from manual menu vs. board spec | Manual: Auto/3600/4000/4400/4800/5200; board spec: up to 6400MT/s | Medium (inference, unverified) |
| Third-party vendor claims 12× 64 GB 6400 kits work on H13SSL-N (eBay "768GB 12x 64GB 6400 RDIMM ... for Supermicro H13SSL-N") | https://www.ebay.de/itm/336789583197 (from DDG) | listing title "768GB 12x 64GB 6400 RDIMM ECC DDR5 RAM Compatible for Supermicro H13DSH H13SSL-N" | Low (vendor bundle, not a user test report) |
| NEMIX/CloudNinjas claim JEDEC-compliant 1.1 V 6400 modules for H13/H14 | https://nemixram.com/products/nemix-ram-memory-compatible-with-supermicro-h14ssl-n-ddr5-6400-pc5-51200 (from DDG) | "JEDEC-compliant for stable operation in enterprise servers and workstations" at 1.1 V | Low (vendor claim, no part number) |

### What would still have to be tested on the bench

1. Install a JEDEC-6400 module (e.g. Kingston KSM64R52BD4-64MD or Micron MTC40F2046S1RC64BH1) in slot A1 with BIOS on Auto, boot, and read the trained frequency in the BMC/IPMI memory info or `dmidecode -t memory` — confirm it shows 6400 and not 4800/5200.
2. Repeat with all 12 slots populated (1DPC) and run a memory stress test (memtest86+ or `stress-ng`/`mprime`) for several hours; watch for training failures, ECC errors, or fallback to 5600/5200.
3. Verify the BIOS "Memory Target Speed" menu still shows only Auto/3600-5200 on the shipped BIOS 2.0 (i.e. no hidden 6400 option) and that Auto is the only way to reach 6400.
4. Cross-check the trained speed across a cold boot and a warm reboot (H14SSL-NT has a known warm-reboot hang at POST 0x4B per ServeTheHome — verify memory training is stable).
5. If 6400 does not train at 12 DIMMs, test 8 and 4 DIMMs to find the population ceiling, and decide whether to fall back to 5600 modules (Samsung M321R8GA0PB0-CWM / Kingston KSM56R46BD4-64MD) which are JEDEC-5600 and guaranteed.
6. Confirm ECC/registered operation and that the SPD's 52-52-52 timing is what actually trains (not a derated default).