# ASUS Pro WS W790E-SAGE SE

<p class="muted">Used bundle with Xeon W5-3435X, <strong>CHF 1,100–1,200</strong> comparable eBay sold price · the cheap older LGA4677 platform. Used in the <a href="../../builds/w790-used/">used W790 alternative</a>.</p>

## What it is

An Intel W790 workstation board for LGA4677 Xeon W-3400/3500 (and W-2400/2500) processors. It is the older, cheaper route to four x16 GPUs: 8-channel DDR5 RDIMM, 7 PCIe 5.0 slots, AST2600 IPMI, 8 SATA, and **two Gen5 M.2 + one Gen4 M.2** plus two SlimSAS Gen4.

The W790E is not a WRX90. It uses a different CPU socket (LGA4677), a different cooler, and DDR5-4800 with the W5-3435X. It is a used-market alternative, not a like-for-like new platform.

## Specifications

| Feature | Detail |
|---|---|
| Chipset / socket | Intel W790, LGA4677 |
| CPU | Xeon W-3500/3400 (7 slots), W-2500/2400 (4 slots) |
| Memory | 8× DDR5 RDIMM, 8-channel, 2 TB, DDR5-4800 official |
| PCIe | 7× PCIe 5.0 x16: x16/x16/x16/x16/x16/x8/x16 |
| 4-GPU layout | slots 1/3/5/7, all **x16**; slot 6 x8 |
| NVMe | **2× Gen5 M.2 + 1× Gen4 M.2 + 2× SlimSAS Gen4** |
| SATA | **8× SATA3** |
| LAN / BMC | Intel dual 10G + Realtek 1G BMC; AST2600 IPMI |
| Power | 2× 24-pin, 4× 8-pin +12V, 1× 8-pin PCIe, 1× 6-pin PCIe |
| Form factor | EEB 305×330 mm |
| Price | **CHF 1,100–1,200 used** (board + W5-3435X; Ricardo price not readable) |

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **Cheap used bundle**: roughly half the new WRX90 + 9955WX board+CPU cost.
- **Four x16 GPU links** in 1/3/5/7; slot 6 is x8.
- **8 SATA ports** — more cold storage than either WRX90 board.
- **8-channel memory and 112 CPU lanes**; enough for four GPUs.
- **IPMI/AST2600** and dual 10G.
- **270 W base CPU** — lower heat than the 350 W 9955WX.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **DDR5-4800 only** (307 GB/s with the W5-3435X); the 6400 modules downclock.
- **Only two Gen5 M.2**; no native 3× Gen5 array.
- **LGA4677 cooler** is a separate purchase; sTR5 AIOs do not fit.
- **Used, no new warranty**, unknown BIOS/revision; check the seller and socket.
- **Power:** 2× 24-pin + 4× 8-pin + PCIe aux is a lot of connectors; check the single-PSU table. The four-GPU PSU caveat still applies.
- **No public 4× R9700 reference** for this exact bundle.
</div>
</div>

## Where it is used

- [Used W790E + W5-3435X alternative](../builds/w790-used.md)

## Notes

!!! note "It is not a WRX90"
    The W790E is LGA4677, DDR5-4800, and two Gen5 M.2. It runs the four GPUs at x16, but it is a different platform with a different memory ceiling. Read the [W790 comparison](../reference/w790-bundle.md) before treating it as a substitute.
