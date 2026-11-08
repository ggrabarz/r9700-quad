# W790E-SAGE SE + W5-3435X vs WRX90 + 9955WX

<p class="muted">The used Intel alternative: a much cheaper 16-core, 8-channel, 112-lane platform that still runs four GPUs at x16. It is not a WRX90 and it is not a 6400 platform.</p>

## The short version

At **CHF 1,100–1,200** (eBay sold for the same board + CPU pair), the used **ASUS W790E-SAGE SE + Xeon W5-3435X** bundle is roughly half the new **ASUS WRX90E-SAGE SE + 9955WX** board+CPU cost. It runs the four R9700s at **x16** in slots 1/3/5/7, has 8 SATA and IPMI, and uses less CPU power.

It also gives up **DDR5-6400** (the W5 is 4800; 307 GB/s vs 410 GB/s), has only **two Gen5 M.2** sockets, needs an **LGA4677 cooler**, and is **used**. The Ricardo listing price is behind a CAPTCHA; the eBay sold range is the reference.

## Comparison

| | ASUS W790E-SAGE SE + W5-3435X | ASUS WRX90E-SAGE SE + 9955WX |
|---|---|---|
| CPU | 16C/32T, 3.1–4.7 GHz, **270 W base / 324 W turbo** | 16C/32T, 4.5–5.4 GHz, **350 W** |
| PCIe 5.0 lanes | **112** | **128** |
| Memory | 8× DDR5 RDIMM, 8-channel, **DDR5-4800** | 8× DDR5 RDIMM, 8-channel, **DDR5-6400** |
| Bandwidth | **307.2 GB/s** | **409.6 GB/s** (+33%) |
| 4-GPU layout | 7 slots, 1/3/5/7 all **x16**, slot 6 x8 | Same |
| M.2 | **2× Gen5 + 1× Gen4** | **4× Gen5** |
| SlimSAS / SATA | 2× Gen4 / **8 SATA** | 2× Gen4 / 4 SATA |
| IPMI | AST2600 | AST2600 |
| Price | **CHF 1,100–1,200 used** | **€2,925.70 new** board + CPU |

## What changes

- **GPU links:** same four x16; GPU inference is not CPU-bound.
- **Memory:** 307 GB/s at 4800. Fine for IQ3_S fully resident; weaker for DeepSeek spill and 512 GB.
- **Storage:** only two Gen5 M.2; a 3× Gen5 array needs a carrier or a 2 Gen5 + 2 Gen4 mix. Eight SATA is a plus.
- **Cooling:** LGA4677, not sTR5; the XE360-TR5 does not fit.
- **Power:** the board lists 2× 24-pin, 4× 8-pin +12V, 1× 8-pin PCIe, 1× 6-pin PCIe. Check the single-PSU table; the four-GPU PSU connector caveat still applies.
- **Used:** no new warranty, unknown BIOS/revision, seller matters.

## Verdict

**At CHF 1,100–1,200, good value for a GPU-resident IQ3_S build.** It is cheaper, lower power, and runs the same four x16 GPUs. **At CHF 2,000+, skip it.** For DeepSeek spill, 512 GB, or a native 3× Gen5 array, the WRX90 + 9955WX is the better platform.

Listing: <https://www.ricardo.ch/de/a/asus-pro-ws-w790e-sage-se-xeon-w5-3435x-cpu-1318880842/>
