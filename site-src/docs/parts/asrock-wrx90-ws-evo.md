# ASRock WRX90 WS EVO

<p class="muted"><strong>€808.05</strong> · Geizhals EU, 59 offers · the value WRX90 board. Used in <a href="../../builds/a-balanced/">A</a>–<a href="../../builds/f-full-speed/">F</a>.</p>

## What it is

The ASRock WRX90 WS EVO is a native AMD WRX90 workstation board for Ryzen Threadripper PRO 9000/7000 WX processors. It has the full 8-channel RDIMM platform, 128 PCIe 5.0 lanes from the CPU, seven x16 slots, AST2600 IPMI, dual 10G, and six NVMe ports split between onboard M.2 and MCIO/SlimSAS.

It is the board that makes the book’s middle work: three Gen5 ports for a 3 TB all-Gen5 array, six NVMe ports for the 6 TB Gen4 option, and MCIO/SlimSAS headers that let the drives live in the 2.5" bays instead of under the GPUs.

## Specifications

| Feature | Detail |
|---|---|
| Chipset / socket | AMD WRX90, sTR5 |
| CPU | Threadripper PRO 9000/7000 WX |
| Memory | 8× DDR5 RDIMM/RDIMM-3DS, 8-channel, 2 TB |
| PCIe | 7× PCIe 5.0 x16: 6× x16 + **PCIE6 x8** |
| 4-GPU layout | PCIE1/3/5/7, all **x16**; PCIE6 unused |
| NVMe | 1× Gen5 M.2 + 1× Gen4 M.2 + 2× Gen5 MCIO + 2× Gen4 SlimSAS |
| SATA | 4× SATA3 |
| LAN / BMC | 2× Intel X710 10GbE + **AST2600 IPMI** |
| VRM | 18+3+3, 110 A, active VRM cooling |
| Power | 2× 8-pin ATX12V, 2× 6-pin PCIe 12V, 2× 6-pin GFX 12V |
| Form factor | EEB 305×330 mm |
| Price | **€808.05** |

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **Cheapest proper WRX90 + IPMI board** in the book.
- **Six NVMe ports**: 3 Gen5 (1 M.2 + 2 MCIO) or 6 Gen4.
- **MCIO drives mount in the 2.5" bays**, away from GPU heat.
- **Full 8-DIMM, 2 TB, 8-channel** platform; 2×64 now, 8×64 later.
- **IPMI/AST2600 and dual 10G** onboard; no add-in card.
- **Four 2-slot GPUs fit in 1/3/5/7 at x16**; slot 6 is the x8 slot.
</div>
<div markdown>
### <span class="bad">Cons</span>

- **Only 1 Gen5 M.2**; the other Gen5 drives need MCIO cables.
- **18+3+3 VRM** is adequate for the 350 W 9955WX, not the margin of the ASUS 32+3+3+3.
- **Four 6-pin aux connectors** (2× PCIE12V + 2× GFX 12V) add to the PSU cable budget.
- **No dual-PSU wiring**; a second PSU is a hack, not a documented path.
- **MCIO cable prices are estimates** (€40 each).
- **The 8×64 6400 QVL is unverified.**
</div>
</div>

## Where it is used

- [A — Balanced 3× Gen5](../builds/a-balanced.md)
- [B — Capacity 6× Gen4](../builds/b-capacity.md)
- [C — Value 4× Gen4](../builds/c-value.md)
- [D — Staged 6400 2×64](../builds/d-staged-6400.md)
- [E — Fast RAM 4×64](../builds/e-fast-ram.md)
- [F — Full Speed 8×64](../builds/f-full-speed.md)

## Notes

!!! warning "Power connectors"
    The board wants **2× 8-pin ATX12V + four 6-pin aux**. With four GPUs, the PX-2200’s four PCIe 8-pin are consumed by the two 12V-2x6 adapters; the board aux has no cable left. See [Power connectors](../reference/power-connectors.md).

!!! note "Slot 6 is x8"
    The ASRock manual lists `PCIE6 at x8`; the 4-way layout uses PCIE1/3/5/7, all x16. Do not put a GPU in slot 6.

[ASUS WRX90E-SAGE SE comparison →](asus-wrx90e-sage-se.md){ .md-button }
