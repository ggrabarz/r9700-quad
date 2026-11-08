# ASUS Pro WS WRX90E-SAGE SE

<p class="muted"><strong>€1,288.00</strong> · Alternate DE, in stock · the premium WRX90 board. Used in <a href="../../builds/g-asus-premium/">G</a> and <a href="../../builds/h-asus-4x-gen5/">H</a>.</p>

## What it is

A native WRX90 workstation board with the strongest storage and power design in the book: **four Gen5 M.2 sockets**, two SlimSAS Gen4 ports, four SATA, a **32+3+3+3** VRM, AST2600 IPMI, dual 10G, and documented dual-PSU wiring.

It is the board of the public 4× R9700 reference build: ASUS WRX90 Sage, 9955WX, 128 GB DDR5-6400, four R9700s, Radiance TP4 at 236 tok/s single stream. That is a user report, not an independent benchmark, and it is 128 GB, not 8×64 — but it validates the four x16 links, the CPU/RAM combination and the board layout.

## Specifications

| Feature | Detail |
|---|---|
| Chipset / socket | AMD WRX90, sTR5 |
| CPU | Threadripper PRO 9000/7000 WX |
| Memory | 8× DDR5 RDIMM, 8-channel, 2 TB, 1DPC |
| PCIe | 7× PCIe 5.0 x16: 6× x16 + **slot 6 x8** |
| 4-GPU layout | slots 1/3/5/7, all **x16**; slot 6 unused |
| NVMe | **4× Gen5 M.2 x4 + 2× SlimSAS Gen4 x4** |
| SATA | 4× SATA3 |
| LAN / BMC | Intel X710 dual 10G + **AST2600 IPMI**, 1G BMC |
| VRM | **32+3+3+3**, active VRM cooling |
| Power | 2× 8-pin CPU, 2× PCIE_8P; dual-PSU PCIE_CPU_12V headers |
| M.2 cooling | heatsinks + active M.2 fan |
| Form factor | EEB 305×330 mm |
| Price | **€1,288.00** |

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **Four Gen5 M.2 sockets**: a 3× Gen5 array needs no MCIO cables; a fourth drive makes 4 TB.
- **32+3+3+3 VRM**, more margin for the 350 W 9955WX.
- **Dual-PSU wiring** is documented; the second-PSU fix is cleaner.
- **Public 4× R9700 reference build** on this exact board, CPU and 128 GB 6400.
- **IPMI, dual 10G, four SATA, EEB**; same 4-way x16 layout.
- **No MCIO cable estimates**; the onboard M.2 path is all listed hardware.
</div>
<div markdown>
### <span class="bad">Cons</span>

- **€1,288.00** vs €808.05 for the ASRock; +€479.95.
- **M.2 sockets sit under the four GPUs**; four Gen5 drives are the hottest storage layout.
- **Only 4 SATA**; the ASRock also has 4, but the W790 alternative has 8.
- **Single-PSU wiring still wants 2× PCIE_8P**, and the PX-2200 has no PCIe 8-pin left after the GPU adapters.
- **No 8×64 6400 validation**; the reference build is 128 GB.
- **The fourth Gen5 drive breaks the 4 TB SATA image**; add the 8 TB HDD.
</div>
</div>

## Reference build

| | |
|---|---|
| Board | ASUS WRX90E-SAGE SE |
| CPU | 9955WX |
| Memory | 128 GB DDR5-6400 ECC |
| GPUs | 4× R9700, PCIe 5.0 x16 |
| Engine | Radiance 1.11, TP4 |
| Model | Qwen3.8-Flash-Next IQ4_R, 113.6 GiB |
| Result | 236 tok/s single, 1,190 tok/s at 16 streams, 11.27 ms step, 6.5× 262K KV |
| Source | [r/LocalLLM report](https://www.reddit.com/r/LocalLLM/comments/1xe1u1i/qwen38flashnext_on_4x_r9700_with_radiance_at_tp4/) |

The 236 tok/s is **Radiance TP4**, not Strata; Strata’s four-card mode is a pipeline layer split. Do not transfer the number.

## Where it is used

- [G — ASUS Premium 3× Gen5 M.2](../builds/g-asus-premium.md)
- [H — ASUS 4× Gen5](../builds/h-asus-4x-gen5.md)

## Notes

!!! warning "Power connectors"
    The single-PSU wiring wants 2× CPU 8-pin + **2× PCIE_8P**. Four GPUs consume all four PX-2200 PCIe 8-pin through the two 12V-2x6 adapters, so the board aux has no cable left. See [Power connectors](../reference/power-connectors.md).

[ASRock value comparison →](asrock-wrx90-ws-evo.md){ .md-button }
