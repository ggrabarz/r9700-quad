# Used ASUS W790E-SAGE SE + Xeon W5-3435X bundle vs WRX90 + 9955WX

**Short answer:** at the **CHF 1,100–1,200** these bundles have sold for, it is a much cheaper 16-core, 8-channel, 112-lane platform and it will run four R9700s at x16. It is **not** a direct substitute for the WRX90 + 9955WX: memory is DDR5-4800 (307 GB/s), there are only **two Gen5 M.2** slots, the platform is used/older, and it needs a different LGA4677 cooler. For IQ3_S fully resident, the GPU does the work and this is a credible value route; for DeepSeek V4.1 spill or a 512 GB build, the 9955WX’s 6400 memory is materially better.

## 1. What the Ricardo bundle is

- **ASUS Pro WS W790E-SAGE SE** — Intel W790, LGA4677, 8× DDR5 RDIMM (8-channel, 2 TB), 7× PCIe 5.0 slots, IPMI/AST2600, EEB 305×330.
- **Intel Xeon W5-3435X** — 16C/32T, 3.1–4.7 GHz, **270 W base / 324 W turbo**, **112 PCIe 5.0 lanes**, **8-channel DDR5-4800**, 45 MB cache.
- The listing is **board + CPU**, used. The public page is behind Ricardo’s CAPTCHA; the price was not readable from the snapshot. eBay sold bundles of the same pair have gone for **CHF 1,200** (May) and **CHF 1,100** (June).

## 2. Platform comparison

| | ASUS W790E-SAGE SE + W5-3435X | ASUS WRX90E-SAGE SE + 9955WX |
|---|---|---|
| CPU | 16C/32T, 3.1–4.7 GHz, **270 W base / 324 W turbo** | 16C/32T, 4.5–5.4 GHz, **350 W** |
| PCIe 5.0 lanes | **112** | **128** |
| Memory | 8× DDR5 RDIMM, 8-channel, **DDR5-4800** | 8× DDR5 RDIMM, 8-channel, **DDR5-6400** |
| Memory bandwidth | **307.2 GB/s** | **409.6 GB/s** (+33%) |
| PCIe slots | 7× x16 (x16/x16/x16/x16/x16/x8/x16); 4-way 1/3/5/7 all x16 | Same |
| M.2 | **2× Gen5 + 1× Gen4** | **4× Gen5** |
| SlimSAS | 2× Gen4 x4 | 2× Gen4 x4 |
| SATA | **8** | 4 |
| IPMI | AST2600 | AST2600 |
| VRM | W790E-SAGE class; check the board revision | 32+3+3+3 |
| Form | EEB 305×330 | EEB 305×330 |
| Price | **CHF 1,100–1,200 used** (eBay sold; Ricardo price not readable) | **€2,925.70 new** (board + CPU) |

## 3. What changes for the 4× R9700 build

- **GPU links are the same.** Both boards put four 2-slot cards in slots 1/3/5/7 at **x16**; slot 6 is x8 and unused. The GPU inference rate is not set by the CPU choice.
- **CPU/RAM matter for the host lane.** IQ3_S fully resident is GPU-bound; the W5-3435X is enough. DeepSeek V4.1 spill and the CPU expert lane want bandwidth: the 9955WX gives **409.6 GB/s** at 6400 versus **307.2 GB/s** at 4800. The W790 can run 5600/6400-rated modules, but the W5-3435X’s official speed is 4800; 8×64 at 6400 is not a realistic target on this CPU.
- **Storage is the bigger compromise.** The W790E has only **two Gen5 M.2** sockets. The current 3× Gen5 array would need a carrier or a 2 Gen5 + 2 Gen4 mix; the ASUS WRX90 runs 3× or 4× Gen5 M.2 natively. The W790’s **8 SATA** ports are a genuine plus for cold drives.
- **Cooling changes.** The W5-3435X is LGA4677, not sTR5; the XE360-TR5 in the BOM will not fit. Add an LGA4677 cooler (360 AIO or 4U air) to the bundle price.
- **Power connectors still bite.** The W790E-SAGE SE lists 2× 24-pin, 4× 8-pin +12V, 1× 8-pin PCIe and 1× 6-pin PCIe; check the manual’s single-PSU table for which are mandatory. Either way, the four R9700s consume the PX-2200’s 2 native 12V-2x6 and both 2×8-pin adapters (all four PCIe 8-pin), so the board’s PCIe aux has no cable left. The same second-PSU / higher-connector-PSU caveat applies.
- **Used platform.** No new warranty, unknown BIOS/revision, and the seller’s history matter. The WRX90 + 9955WX is current, new, and has the 4× Gen5 M.2 / 6400 path.

## 4. Verdict

- **At CHF 1,100–1,200, the used bundle is a strong value for a GPU-resident IQ3_S build.** It saves roughly half the new board+CPU cost; the four R9700s run at the same x16 links. Budget an LGA4677 cooler and check the PSU connectors.
- **At CHF 2,000+, it stops being a bargain.** The new WRX90 + 9955WX is the better long-term platform, especially for DeepSeek spill and 512 GB.
- **Do not buy it for the 3× Gen5 array as specified** unless you accept a Gen4 member or a carrier; the W790E has only two Gen5 M.2 sockets.
- **For DeepSeek/512 GB, stay with the 9955WX.** The 6400 memory and 128 lanes are the point of the WRX90 build.

Listing: <https://www.ricardo.ch/de/a/asus-pro-ws-w790e-sage-se-xeon-w5-3435x-cpu-1318880842/>
