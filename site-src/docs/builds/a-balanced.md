# A — Balanced, 3× Gen5

<div class="hero" markdown>
<span class="eyebrow">Build A · value recommendation</span>

**All-Gen5 3 TB, IPMI, and a full image on the 4 TB SATA.** This is the middle of the book: enough Gen5 to be fast, enough capacity for the stated models, and none of the 6-drive RAID 0 exposure.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [Part dossiers](../parts/index.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€10,418.91</span></div>
<div><span class="k">With 4 GPUs</span><span class="v">€18,139.75</span></div>
<div><span class="k">Board</span><span class="v">ASRock WRX90</span></div>
<div><span class="k">Memory</span><span class="v">2×64 GB 5600</span></div>
<div><span class="k">Array</span><span class="v">3× Gen5 / 3 TB</span></div>
</div>

## What it is

A four-GPU WRX90 workstation with the four R9700s owned and excluded. The storage is a **3-drive all-Gen5 RAID 0** built from one onboard Gen5 M.2 socket and two Gen5 MCIO ports. The two MCIO drives live in the case’s 2.5" bays, away from the GPU heat. A **4 TB SATA SSD** holds the OS and a full image of the 3 TB array, which is the backup discipline the 4 TB and 6 TB arrays cannot match without another drive.

The memory is the **2×64 GB DDR5-5600** value pair: 128 GB, two channels, 89.6 GB/s, 48% of the platform. It is the cheapest configuration that runs IQ3_S fully resident with the PLE in RAM, and it leaves six DIMM slots open for the 8×64 GB endgame.

## BOM

<div class="bom" markdown>
--8<-- "_bom/a.md"
</div>

[Download the CSV](../downloads/option-a.csv){ .md-button } [Memory ladder](../reference/memory-ladder.md){ .md-button }

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **The cheapest all-Gen5 3 TB array** in the book: €792 in drives, two €40 MCIO cables.
- **3 TB fits a full image on the 4 TB SATA** (3.6 TB usable). The 4 TB and 6 TB arrays do not.
- **MCIO drives sit in the 2.5" bays**, outside the GPU heat; the onboard Gen5 M.2 is the only hot drive.
- **IPMI/AST2600** and dual 10G are onboard; no add-in card needed.
- **The 2×64 5600 pair is the cheapest 128 GB floor** and leaves six slots for 8×64 later.
- **The board is €808.05**, the cheapest proper WRX90/IPMI option.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **5600 memory only**: 89.6 GB/s at 2 DIMMs, 358.4 GB/s at 8; the 6400 path needs different modules.
- **Two sticks, two channels.** It is a staging configuration for DeepSeek, not a DeepSeek configuration.
- **No 4× Gen5 option.** The array is 3 TB, not 4 TB; the fourth Gen5 port would be a Gen4 M.2 or another MCIO.
- **The 2×64 RAM is €4,998**, 48% of the platform — the 2026 DRAM tax.
- **The PSU connector budget needs fixing** before ordering: four GPUs consume all four PCIe 8-pin, leaving none for the board aux. See [Power connectors](../reference/power-connectors.md).
</div>
</div>

## Verdict

**Start here unless you specifically need 6 TB or 6400 memory.** It is the best cost/benefit middle: all-Gen5, a full image on the SATA, IPMI, and a board that leaves the door open to the 8×64 endgame. If you want the ASUS four-Gen5-M.2 board, go to [G](g-asus-premium.md); if you want the 2×64 6400 start, go to [D](d-staged-6400.md).

## Part dossiers

- [ASRock WRX90 WS EVO](../parts/asrock-wrx90-ws-evo.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 64 GB DDR5-5600](../parts/samsung-64gb-5600.md)
- [Samsung 9100 PRO 1 TB](../parts/samsung-9100-pro.md)
- [Samsung 870 EVO 4 TB](../parts/samsung-870-evo.md)
- [MCIO to M.2 cable](../parts/mcio-cable.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [SilverStone XE360-TR5](../parts/silverstone-xe360-tr5.md)
- [Fractal Meshify 2 XL](../parts/fractal-meshify-2-xl.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
