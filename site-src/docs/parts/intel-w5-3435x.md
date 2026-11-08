# Intel Xeon W5-3435X

<p class="muted"><strong>Used bundle</strong> with ASUS W790E-SAGE SE, CHF 1,100–1,200 comparable · 16C/32T, 112 PCIe 5.0 lanes, 8-channel DDR5-4800. Used in the <a href="../../builds/w790-used/">W790 alternative</a>.</p>

## What it is

A 16-core Sapphire Rapids workstation Xeon on LGA4677. It has **112 PCIe 5.0 lanes**, **8-channel DDR5-4800**, 45 MB cache, and a 270 W base / 324 W turbo power envelope. It is the cheaper older alternative to the 9955WX: same core count, lower memory speed, lower power, different socket and cooler.

The W5-3435X is the CPU in the used ASUS W790E-SAGE SE bundle. Its 8-channel memory gives 307.2 GB/s, about 25% less than the 9955WX at 6400 and 14% less than 5600. For IQ3_S fully resident, the GPU does the work; for DeepSeek spill, that bandwidth gap matters.

## Specifications

| Feature | Detail |
|---|---|
| Cores / threads | 16C / 32T |
| Clock | 3.1 GHz base, 4.7 GHz boost |
| Cache | 45 MB |
| Power | **270 W base / 324 W turbo** |
| PCIe | **112× PCIe 5.0 lanes** |
| Memory | **8-channel DDR5-4800 ECC RDIMM** |
| Socket | LGA4677 |
| Price | **Used bundle CHF 1,100–1,200** (board + CPU) |

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **16C/32T, 8-channel, 112 lanes** — enough for four x16 GPUs.
- **Much cheaper used** than a new 9955WX + WRX90 board.
- **270 W base** — lower heat and PSU load.
- **8-channel memory** keeps the host lane usable for IQ3_S.
- **LGA4677 W790E board has 8 SATA** and IPMI.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **DDR5-4800 only**: 307 GB/s, 25% below 6400.
- **112 lanes** vs 128; still enough, but less spare.
- **LGA4677 cooler** required; sTR5 AIOs do not fit.
- **Used, no new warranty**, unknown history.
- **The W790 platform is older**; DDR5-6400 and 4× Gen5 M.2 are not its strengths.
</div>
</div>

## Where it is used

- [Used W790E + W5-3435X alternative](../builds/w790-used.md)
