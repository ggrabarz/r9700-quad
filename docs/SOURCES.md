# Sources and verification notes

Snapshot date: **2026-11-06/07** (platform 06, RAM retail 07). Prices include VAT and are “from” offers, not reservations.

## Board and platform

| Source | What it verifies |
|---|---|
| [Gigabyte TRX50 AI TOP specification](https://www.gigabyte.com/Motherboard/TRX50-AI-TOP/sp) (blocked to some crawlers; the manual PDF is the accessible copy) | 4× PCIe 5.0 x16, 4× M.2, 8× DDR5 RDIMM, 4× SATA, 2× 10GbE, E-ATX 30.5×33.0 cm. |
| [ASRock WRX90 WS EVO specification](https://www.asrock.com/mb/AMD/WRX90%20WS%20EVO/index.asp) | 7× PCIe 5.0 x16, 1× Gen5 M.2 + 1× Gen4 M.2, 2× MCIO Gen5, 2× SlimSAS Gen4, 8× DDR5 RDIMM (2 TB), IPMI/AST2600, dual 10GbE, EEB 30.5×33.0 cm. |
| [ASRock WRX90 WS EVO manual (PDF)](https://download.asrock.com/Manual/WRX90%20WS%20EVO.pdf) | Slot layout (PCIE1-7), MCIO/SlimSAS wiring, 6-pin GFX 12V requirement, memory population, form factor. |
| [ASRock WRX90 WS EVO price](https://geizhals.eu/asrock-wrx90-ws-evo-90-mxbmh0-a0uayz-a3167681.html) | €808.05 from 59 offers on 2026-11-06 (vs €896.75 for the TRX50 AI TOP). |
| [ASUS Pro WS WRX90E-SAGE SE spec](https://www.asus.com/motherboards-components/motherboards/workstation/pro-ws-wrx90e-sage-se/techspec/) | 7× PCIe 5.0 x16 (6× x16 + 1× x8), 4× Gen5 M.2, 2× SlimSAS Gen4, 4× SATA, 8× RDIMM/2 TB, AST2600 BMC, dual 10G, 32+3+3+3 VRM, EEB 30.5×33 cm. |
| [ASUS WRX90E-SAGE SE manual (PDF)](https://dlcdnets.asus.com/pub/ASUS/mb/SocketsTR5/Pro_WS_WRX90E-SAGE_SE/E27563_Pro_WS_WRX90E-SAGE_SE_EM_V4_WEB.pdf) | Slot 6 is x8; 4-way VGA uses slots 1/3/5/7 (all x16); 4× Gen5 M.2; single-PSU wiring 2× CPU + 2× PCIE_8P; dual-PSU PCIE_CPU_12V headers. |
| [ASUS WRX90E-SAGE SE price](https://www.alternate.de/ASUS/PRO-WS-WRX90E-SAGE-SE-Mainboard/html/product/100042953) | €1,288.00 at Alternate, in stock, 2026-11-07. |
| [ASUS W790E-SAGE SE spec](https://www.asus.com/motherboards-components/motherboards/workstation/pro-ws-w790e-sage-se/techspec/) | W790, LGA4677, 8× DDR5 RDIMM/2 TB, 8-channel, 7× PCIe 5.0 (x16/x16/x16/x16/x16/x8/x16), 2× Gen5 M.2 + 1× Gen4 M.2, 2× SlimSAS Gen4, 8 SATA, AST2600 IPMI, EEB 305×330. |
| [Intel Xeon W5-3435X](https://www.intel.com/content/www/us/en/products/sku/233421/intel-xeon-w53435x-processor-45m-cache-3-10-ghz/specifications.html) | 16C/32T, 3.1–4.7 GHz, 270 W base / 324 W turbo, 112 PCIe 5.0 lanes, 8-channel DDR5-4800, 45 MB cache. |
| [Ricardo W790E + W5-3435X bundle](https://www.ricardo.ch/de/a/asus-pro-ws-w790e-sage-se-xeon-w5-3435x-cpu-1318880842/) | Used board + CPU listing; public page behind CAPTCHA, price not readable. Comparable eBay sold bundles CHF 1,100–1,200. |
| [r/LocalLLM 4× R9700 Radiance TP4 build](https://www.reddit.com/r/LocalLLM/comments/1xe1u1i/qwen38flashnext_on_4x_r9700_with_radiance_at_tp4/) | User report: ASUS WRX90 Sage, 9955WX, 128 GB DDR5-6400, 4× R9700, Radiance 1.11 TP4: 236 tok/s single, 1,190 tok/s at 16 streams, 11.27 ms step, 6.5× 262K KV. Not independently verified. |
| [Gigabyte WRX90 AI TOP specification](https://www.gigabyte.com/Motherboard/WRX90-AI-TOP/sp) | WRX90, sTR5, 8× RDIMM/2 TB, 6× x16 + 1× x8, 2× Gen5 M.2 + 1× Gen4 M.2 + 2× MCIO 8i, 4× SATA, AST2600 BMC/IPMI, dual 10GbE, E-ATX. |
| [Gigabyte WRX90 AI TOP announcement](https://www.techpowerup.com/354325/gigabyte-advances-local-ai-infrastructure-with-wrx90-ai-top-motherboard) | Announced 2026-10-30; 32+3+3+3-phase VRM, 14-layer PCB, BMC/IPMI, active memory cooling; no price/release date. |
| [Gigabyte WRX90 AI TOP price listing](https://geizhals.eu/gigabyte-wrx90-ai-top-amd-str5-a3995002.html) | Product page exists but **no offers** on 2026-11-06; not yet retail-priced. |
| [TRX50 AI TOP manual, rev. 1.07 (PDF)](https://download.gigabyte.com/FileList/Manual/mb_manual_trx50-ai-top_107_e.pdf) | 8-channel with PRO 9000WX/7000WX; 4-channel with non-PRO; M2D disabled on non-PRO; PCIEX16_4 Gen4 on TR 7000; 4× PCIe 8-pin aux (PCIE_12V1/2 for one PSU); memory population A1/C1/E1/G1 for quad-channel. |
| [AMD Ryzen Threadripper PRO 9955WX](https://www.amd.com/en/products/processors/workstations/ryzen-threadripper/9000-wx-series/amd-ryzen-threadripper-pro-9955wx.html) | 16C/32T, 5.4 GHz, 350 W, 128 PCIe 5.0 lanes, 8-channel DDR5 ECC. |
| [AMD Radeon AI PRO R9700](https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html) | 32 GB GDDR6, 300 W, 2-slot blower, 1× 12V-2x6, 267 mm. |
| [TechPowerUp R9700 database](https://www.techpowerup.com/gpu-specs/radeon-ai-pro-r9700.c4290) | 267 × 111 × 40 mm, dual-slot, 1× 16-pin, 300 W, PCIe 5.0 x16. |
| [ASUS Turbo R9700 launch coverage](https://videocardz.com/newz/asus-ai-pro-r9700-turbo-first-radeon-from-asus-with-12v-2x6-connector-oc-support-confirmed) | Confirms blower/2-slot/267 mm and 12V-2x6 across board partners. |
| [Gigabyte R9700 AI TOP dimensions](https://www.expreview.com/100805.html) | 267 × 111 × 40 mm, dual-slot. |

## Memory

| Source | What it verifies |
|---|---|
| [Micron MTC40F2046S1RC64BH1 part page](https://www.micron.com/products/memory/dram-modules/rdimm/part-catalog/part-detail/mtc40f2046s1rc64bh1) | 64 GB, x80 ECC, **dual rank**, **4Gb x4** (2Rx4), 6400 MT/s, CL52, 1.1 V, RDIMM. The single-module 2×64 6400 path. |
| [G.Skill T5 Neo 4×64 kit at Proshop](https://www.proshop.de/RAM/GSkill-T5-Neo-DDR5-6400-256GB-CL36-Quad-Channel-4-pcs-AMD-EXPO-Schwarz/3402039) | 256 GB (4×64), DDR5-6400, CL36-44-44-102, 1.3 V, registered + ECC, AMD EXPO; 1–2 months, max 2 per customer. |
| [G.Skill T5 Neo 8×64 kit at Alternate](https://www.alternate.de/G-Skill/RIMM-512-GB-DDR5-6400-8x-64-GB-Octa-Kit-ECC-Arbeitsspeicher/html/product/100203342) | 512 GB (8×64), DDR5-6400, CL38-48-48-102, 1.35 V, registered + ECC, AMD EXPO; notify-only at the snapshot. |

## Power and chassis

| Source | What it verifies |
|---|---|
| [Seasonic PRIME PX-2200 datasheet (PDF)](https://seasonic.com/wp-content/uploads/2024/06/ATX-3.1-PRIME-PX-2200.pdf) | 2200 W, ATX 3.1, 80+ Platinum, 2× native 12V-2x6 + 2× 2×8-pin adapters + 4× PCIe 8-pin, 3× EPS, 16× SATA, 210×150×86 mm, 200–240 V only. |
| [be quiet! Dark Power Pro 13 1600 W](https://www.bequiet.com/en/powersupply/4393) | 1600 W, 2× native 12V-2x6, 6× PCIe 6+2, 200 mm; used as the “why not 1600 W” comparison. |
| [Fractal Meshify 2 XL product sheet (PDF)](https://assets.fractal-design.com/files/uxzbxy2o/production/1bc60fe11df0e6b0269090a88eec38f36586ff3c.pdf) | E-ATX/SSI-EEB, 9+3 slots, 250 mm PSU, 549 mm GPU (open) / 359 mm (storage), 480 mm top/front radiator, 3× 140 mm included, 6× 3.5" + 2× 2.5". |
| [Corsair 9000D Airflow](https://www.corsair.com/us/en/explorer/diy-builder/cases/corsair-9000d-rgb-airflow/) | E-ATX/SSI-EEB, 8 slots, 400 mm GPU, 225 mm PSU, 5× 3.5" + 6× 2.5". |
| [Phanteks Enthoo Pro 2 (Alternate listing)](https://www.alternate.de/Phanteks/Enthoo-Pro-2-Big-Tower-Geh%C3%A4use/html/product/100042214) | E-ATX, 8 slots, 4× 3.5" + 11× 2.5", €154.90; budget alternate. |

## Prices

| Item | Price | Source |
|---|---:|---|
| ASRock WRX90 WS EVO | €808.05 | [Geizhals EU](https://geizhals.eu/asrock-wrx90-ws-evo-90-mxbmh0-a0uayz-a3167681.html) |
| Gigabyte TRX50 AI TOP (alternative) | €896.75 | [Geizhals EU](https://geizhals.eu/gigabyte-trx50-ai-top-a3246131.html) |
| Threadripper PRO 9955WX | €1,637.70 | [Geizhals DE](https://geizhals.de/amd-ryzen-threadripper-pro-9955wx-100-100000725wof-a3531872.html) |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | €2,499.00 | [Geizhals EU](https://geizhals.eu/samsung-rdimm-64gb-m321r8ga0pb0-cwm-a3528359.html) |
| Micron MTC40F2046S1RC64BH1 64 GB DDR5-6400 CL52 2Rx4 RDIMM (single) | €3,279.97 | [Galaxus DE](https://www.galaxus.de/de/s1/product/micron-crucial-64-gb-reg-ecc-ddr5-6400-mtc40f2046s1rc64bh1-6400-mhz-ddr5-ram-dimm-ram-68867097) |
| Kingston KSM64R52BD4 64 GB DDR5-6400 CL52 RDIMM (single) | €3,202.74 | [Galaxus DE](https://www.galaxus.de/de/s1/product/kingston-ksm64r52bd4-1-x-64gb-6400-mhz-ddr5-ram-dimm-ram-52967925) |
| G.Skill T5 Neo 4×64 GB DDR5-6400 CL36 R-DIMM kit | €12,135.01 | [Proshop DE](https://www.proshop.de/RAM/GSkill-T5-Neo-DDR5-6400-256GB-CL36-Quad-Channel-4-pcs-AMD-EXPO-Schwarz/3402039) |
| G.Skill T5 Neo 8×64 GB DDR5-6400 CL38 R-DIMM kit | €23,094.00 notify-only; €27,666.06 orderable at Proshop | [Alternate DE](https://www.alternate.de/G-Skill/RIMM-512-GB-DDR5-6400-8x-64-GB-Octa-Kit-ECC-Arbeitsspeicher/html/product/100203342) / [Proshop DE](https://www.proshop.de/RAM/GSkill-T5-Neo-DDR5-6400-512GB-CL38-Octa-Channel-8-pcs-AMD-EXPO-Schwarz/3402040) |
| Kingston FURY Renegade Pro 4×32 GB DDR5-7600 CL40 kit (KF576RH40RBK4-128) | 25 969,00 zł / €5,893 gross (€4,791 net) | [Proshop PL](https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7600-128GB-CL38-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462079) — **SPD = JEDEC-6400**, runs 6400 on the JEDEC-only H14 BIOS; 3 kits = 12× 32 GB = 384 GB. |
| Kingston FURY Renegade Pro 4×32 GB DDR5-6400 CL32 kit (KF564R32RBE2K4-128) | 32 458,00 zł / €7,365 gross (€5,988 net) | [Proshop PL](https://www.proshop.pl/RAM/Kingston-FURY-Renegade-Pro-DDR5-6400-128GB-CL32-Quad-Channel-4-pcs-AMD-EXPO-Intel-EXPO-Czarny/3246165) — **SPD = JEDEC-4800**, 6400 only via EXPO/1.4 V, not offered by the H14 BIOS. |
| Kingston FURY Renegade Pro 8×32 GB DDR5-7200 CL38 kit (KF572RH38RBK8-256) | 50 712,00 zł / €11,507 gross (€9,356 net) | [Proshop PL](https://www.proshop.pl/RAM/Kingston-FURY-Renegade-PRO-DDR5-7200-256GB-CL38-Octa-Channel-8-pcs-AMD-EXPO-Intel-EXPO-Czarny/3462075) — **SPD = JEDEC-6400**; 256 GB in 8 of 12 channels. |
| Micron MTC40F2046S1RC64BD2 64 GB DDR5-6400 (US reference) | US$4,270.00 | [ServerSupply](https://www.serversupply.com/MEMORY/PC5-51200/64GB/MICRON/MTC40F2046S1RC64BD2_387264.htm) |
| PowerColor R9700 32 GB | €1,930.21 | [Geizhals EU](https://geizhals.eu/powercolor-radeon-ai-pro-r9700-a3504726.html) |
| Samsung 9100 PRO 1 TB Gen5 | €264.00 | [Alternate DE](https://www.alternate.de/Samsung/9100-PRO-1-TB-SSD/html/product/100118126) |
| Samsung 990 PRO 1 TB Gen4 | €262.00 | [Alternate DE](https://www.alternate.de/Samsung/990-PRO-1-TB-SSD/html/product/1864239) |
| Samsung 870 EVO 4 TB | €665.00 | [Alternate DE](https://www.alternate.de/Samsung/870-EVO-4-TB-SSD/html/product/1706407) |
| Toshiba N300 8 TB HDD | €389.00 | [Alternate DE](https://www.alternate.de/Toshiba/N300-8-TB-Festplatte/html/product/100111191) |
| Seasonic PRIME PX-2200 | €489.90 | [Alternate DE](https://www.alternate.de/Seasonic/PRIME-PX-2200-2200W-ATX-3-1-PC-Netzteil/html/product/100076188) |
| SilverStone XE360-TR5 | €389.90 | [Alternate DE](https://www.alternate.de/SilverStone/SST-XE360-TR5-Wasserk%C3%BChlung/html/product/100114775) |
| Noctua NH-U14S TR5-SP6 | €129.90 | [Alternate DE](https://www.alternate.de/Noctua/NH-U14S-TR5-SP6-CPU-K%C3%BChler/html/product/100020811) |
| Fractal Meshify 2 XL | €209.90 | [Alternate DE](https://www.alternate.de/Fractal-Design/Meshify-2-XL-Black-TG-Light-Tint-Big-Tower-Geh%C3%A4use/html/product/1669747) |
| Corsair 9000D Airflow | €469.90 | [Alternate DE](https://www.alternate.de/Corsair/iCUE-LINK-9000D-Airflow-Big-Tower-Geh%C3%A4use/html/product/100064495) |

## Model and engine

| Source | What it verifies |
|---|---|
| `/root/git/strata/models/swift-IQ3_S/Swift-Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00001-of-00002.gguf` | GGUF metadata: 48 layers, 512 experts, 10 active, 24/2 heads, 262,144 context, hybrid attention/SSM. |
| `/root/git/strata/docs/AMD_HIP.md` | R9700/gfx1201 maintainer-tested; HIP package carries the runtime; multi-GPU layer split; `--gpu`/`--gpu-roles`; `--resident-cpu-experts` semantics. |
| `/root/git/strata/docs/MULTI_GPU.md` | Layer split mechanics, per-card dense copy, 2/3/4-card R9700 decode steps, 4× RX 7900 XT IQ3_S 262K numbers. |
| `/root/git/strata/docs/MODELS.md` | IQ3_S/IQ3_XXS sizes, expert/RAM requirements, Swift 1.5, PLE table, 262K context. |
| `/root/git/strata/docs/DETAILS.md` | KV formats (`int8`, `k8v4`), 13.7 KB/token KV-streaming cost, 28.8 GB PLE table, 1× R9700 94.7 tok/s anchor. |
| `/root/git/strata/docs/BATCHING.md` | Batch-slot behavior, 2× RTX 5090 `--batch 6` at 262K, concurrent read measurements. |
| [Strata repository](https://github.com/Niko1221/Strata) | Upstream project and release packages. |

## Alternative engine (Saber)

| Source | What it verifies |
|---|---|
| [Saber repository](https://github.com/GGZ14/saber-engine) | Rust/HIP engine for gfx1201; Qwen3.8-27B and Qwen3.8 Flash-Next; **TP=1/2 only**, refuses 3/4; MXFP4 `SBRPACK1` packs; 95.4 GiB bf16 PLE table with `O_DIRECT`; 229 tok/s 27B on 2× R9700. |
| [Launch post by @bkuyper, 2026-11-05](https://x.com/bkuyper/status/2118433092230606937) | Announcement and the project link; the screenshot is a terminal capture, not a Flash-Next benchmark table. |
| [`docs/SABER.md`](SABER.md) | The fit analysis against this 4-GPU build; why it does not change the BOM. |
| [`docs/SABER-4X.md`](SABER-4X.md) | Code-level 4-GPU feasibility: Flash-Next 2-KV-head limit, EP=4/TP=2 vs pipeline, code touchpoints, BOM impact. |
| [`patches/`](../patches/) | Upstream Saber docs/RFC patch, apply/submit instructions, PR body. |

The Saber numbers are the project’s claims, not measurements on this host. The 229 tok/s figure is the 27B dense model, not Flash-Next; do not transfer it to the MoE workload.

## Arithmetic and derived figures

The following are **derived**, not quoted:

- KV `k8v4` = 13.7 KB/token × 0.77 = 10.55 KB/token (the docs state k8v4 is 23% less than int8).
- 262,144 tokens × 10.55 KB = 2.64 GB per stream.
- 50 GB experts / 4 cards = 12.5 GB per card (first-order even split; the real layer split is not even).
- 1/2/4/8 populated channels at DDR5-5600 = 44.8 / 89.6 / 179.2 / 358.4 GB/s (8 bytes × 5,600 MT/s × channels).
- The same at DDR5-6400 = 51.2 / 102.4 / 204.8 / 409.6 GB/s (8 bytes × 6,400 MT/s × channels).
- 4×300 + 350 + 80 = 1,630 W; 2,200 − 1,630 = 570 W headroom.
- 1,630 W / 0.94 / 230 V = 7.54 A.
- 1,630 W × 8,760 h × €0.25/kWh = €3,569.70/year at 100% load.
- All BOM totals come from `tools/calc.py` reading `bom/prices.json`; run it to reproduce them.

## What is **not** verified

- The ~150 tok/s decode and 3,000+ tok/s prefill projections. They are extrapolations from published R9700 measurements, not a run on this exact four-card/9955WX configuration.
- The 8×262K stream count. It fits the arithmetic; the engine's per-slot buffers, fragmentation and HIP behavior can lower it.
- The 45–50 dBA noise estimate and the 5,562 BTU/h heat figure (the latter is arithmetic from 1,630 W; the former is an estimate).
- The 2026 DRAM/NAND prices are a snapshot; they are the largest source of variance in the BOM.
- The G.Skill T5 Neo kit rank (2Rx4 vs 2Rx8) and the ASRock WRX90 WS EVO QVL entry for the exact Micron or G.Skill part. The G.Skill retail listings do not print the rank; Micron confirms 2Rx4 for MTC40F2046S1RC64BH1, but ASRock’s QVL was not machine-readable at the snapshot.
- 8×64 GB DDR5-6400 training on the ASRock/ASUS/9955WX. The G.Skill octa kit is sold as an 8-DIMM 6400 kit, but the board/BIOS combination is not measured here; validate with the acceptance run. The r/LocalLLM ASUS build is **128 GB**, not 8×64, so it does not settle the 512 GB QVL question.
- The r/LocalLLM Radiance TP4 numbers (236 tok/s single, 1,190 tok/s at 16 streams) are a user report, not an independent benchmark, and Radiance is tensor-parallel; they do not transfer to Strata’s pipeline layer split.
