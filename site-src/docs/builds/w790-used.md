# Used W790E-SAGE SE + W5-3435X

<div class="hero" markdown>
<span class="eyebrow">Alternative platform · used Intel W790</span>

**A cheaper 16-core, 8-channel, 112-lane route to four x16 GPUs.** Not a WRX90, not a drop-in substitute: DDR5-4800, two Gen5 M.2 sockets, a different LGA4677 cooler, and a used board/CPU bundle.

[:octicons-arrow-right-24: Platform comparison](#platform-comparison) · [All builds](index.md) · [W790 board dossier](../parts/asus-w790e-sage-se.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Board + CPU</span><span class="v price">CHF 1,100–1,200*</span></div>
<div><span class="k">Memory</span><span class="v">8ch DDR5-4800</span></div>
<div><span class="k">Bandwidth</span><span class="v">307 GB/s</span></div>
<div><span class="k">4-GPU</span><span class="v">x16 / x16 / x16 / x16</span></div>
</div>

<p class="small muted">* eBay sold prices for the same board + CPU pair. The Ricardo listing is behind a CAPTCHA; its price was not readable from the snapshot. Confirm the seller, board revision, BIOS and socket before buying.</p>

## What it is

A used **ASUS Pro WS W790E-SAGE SE** with an **Intel Xeon W5-3435X**. The W5 is 16C/32T, 270 W base / 324 W turbo, 112 PCIe 5.0 lanes, 8-channel DDR5-4800. The board is LGA4677, 8 DIMM, 2 TB, 7 PCIe 5.0 slots, 3 M.2 (2 Gen5 + 1 Gen4), 2 SlimSAS Gen4, 8 SATA, AST2600 IPMI, EEB.

It runs four 2-slot GPUs in slots 1/3/5/7 at **x16**, the same as the WRX90 boards. The compromise is memory speed and storage: DDR5-4800 is **307 GB/s** at eight channels, and the board has only **two Gen5 M.2** sockets. The W5-3435X is not a Threadripper; it uses a different cooler and a different platform.

## Platform comparison

| | W790E-SAGE SE + W5-3435X | WRX90E-SAGE SE + 9955WX |
|---|---|---|
| CPU | 16C/32T, 3.1–4.7 GHz, **270 W base / 324 W turbo** | 16C/32T, 4.5–5.4 GHz, **350 W** |
| PCIe 5.0 lanes | **112** | **128** |
| Memory | 8× DDR5 RDIMM, 8-channel, **DDR5-4800** | 8× DDR5 RDIMM, 8-channel, **DDR5-6400** |
| Bandwidth | **307 GB/s** | **410 GB/s** (+33%) |
| 4-GPU layout | 7 slots, 1/3/5/7 all **x16**, slot 6 x8 | Same |
| M.2 | **2× Gen5 + 1× Gen4** | **4× Gen5** |
| SlimSAS / SATA | 2× Gen4 / **8 SATA** | 2× Gen4 / 4 SATA |
| IPMI | AST2600 | AST2600 |
| Price | **CHF 1,100–1,200 used** | **€2,925.70 new** board + CPU |

## What it would need

- **Cooler:** LGA4677, not sTR5. The XE360-TR5 will not fit; budget a 4677 AIO or 4U air cooler.
- **Memory:** 8-channel DDR5-4800 RDIMM. The 6400 64 GB modules would downclock; buy 4800/5600-rated modules for this platform.
- **Storage:** 2 Gen5 M.2 + 2 SlimSAS Gen4 + 8 SATA. A 3× Gen5 array needs a carrier or a 2 Gen5 + 2 Gen4 mix.
- **Power:** the board lists 2× 24-pin, 4× 8-pin +12V, 1× 8-pin PCIe and 1× 6-pin PCIe; check the single-PSU table. The four GPUs still consume all four PX-2200 PCIe 8-pin, so the board aux has no cable left.
- **Validation:** no public 4× R9700 reference for this exact bundle; the ASUS WRX90 build has one.

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **Much cheaper** than a new WRX90 + 9955WX; roughly half the board+CPU cost at the eBay sold range.
- **Four x16 GPU links**, same slot layout as the WRX90.
- **16 cores, 8-channel, 112 lanes**: enough for four GPUs and the host lane.
- **8 SATA ports** — more cold storage than the WRX90.
- **270 W base CPU**: lower heat and PSU load than the 350 W 9955WX.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **DDR5-4800 only**: 307 GB/s, 25% below the 6400 WRX90 and 14% below 5600.
- **Only two Gen5 M.2**; no native 3× Gen5 array.
- **LGA4677 cooler** is an extra purchase; the sTR5 AIO will not fit.
- **Used, no new warranty**, unknown BIOS/revision, and the seller matters.
- **The PSU connector issue remains**; the board may also want more CPU 8-pin than the PX-2200 has.
- **No public 4× R9700 reference** for this bundle.
</div>
</div>

## Verdict

**At CHF 1,100–1,200, this is a strong value for a GPU-resident IQ3_S build.** The GPU links are the same, the CPU is enough, and the saving is large. It is not the platform for DeepSeek spill, 512 GB, or a native 3× Gen5 array: the 9955WX’s 6400 memory and the WRX90’s four Gen5 M.2 sockets are the reason to pay more.

Listing: <https://www.ricardo.ch/de/a/asus-pro-ws-w790e-sage-se-xeon-w5-3435x-cpu-1318880842/>  
Full write-up: [W790 bundle comparison](../reference/w790-bundle.md)
