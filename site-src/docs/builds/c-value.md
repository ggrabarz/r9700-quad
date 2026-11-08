# C — Value, 4× Gen4

<div class="hero" markdown>
<span class="eyebrow">Build C · 4 TB value</span>

**Four Gen4 drives, 4 TB, the cheapest per TB.** The simple array: two onboard M.2 sockets and two MCIO ports, no SlimSAS, no 8 TB HDD in the base build.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [Part dossiers](../parts/index.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€10,682.59</span></div>
<div><span class="k">With 4 GPUs</span><span class="v">€18,403.43</span></div>
<div><span class="k">Board</span><span class="v">ASRock WRX90</span></div>
<div><span class="k">Memory</span><span class="v">2×64 GB 5600</span></div>
<div><span class="k">Array</span><span class="v">4× Gen4 / 4 TB</span></div>
</div>

## What it is

Four Samsung 990 PRO 1 TB Gen4 drives in RAID 0: two onboard M.2 and two Gen5 MCIO ports running Gen4 drives. It is the simplest array in the book — four drives, two adapter cables, no SlimSAS, no HDD.

The trade is speed and backup. A 4 TB array is larger than the 3.6 TB usable space on the 4 TB SATA, so the base build has **no full image**. Add the 8 TB N300 if you want the same backup discipline as A or B.

## BOM

<div class="bom" markdown>
--8<-- "_bom/c.md"
</div>

[Download the CSV](../downloads/option-c.csv){ .md-button } [Memory ladder](../reference/memory-ladder.md){ .md-button }

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **Cheapest storage per TB** of the three storage tiers: four 1 TB drives, two MCIO cables.
- **4 TB capacity** without the six-drive failure domain of B.
- **Simpler build** than B: no SlimSAS, no 8 TB HDD in the base.
- **Same WRX90 platform** as A/B, with IPMI and the 8×64 upgrade path.
- **€263.68 more than A for +1 TB**, but the array is slower.
</div>
<div markdown>
### <span class="bad">Cons</span>

- **Gen4, not Gen5**: ~28–30 GB/s sequential and ~4.8M 4K IOPS, well below A.
- **No full image on the 4 TB SATA** (4 TB > 3.6 TB usable); add the 8 TB HDD or accept no image.
- **Four-drive RAID 0** is still a failure domain; the archive matters.
- **The PSU connector issue remains** for the four GPUs plus board aux.
- **The 2×64 5600 memory** is the value floor, not the fast path.
</div>
</div>

## Verdict

**Buy C if 4 TB matters more than Gen5 speed and you accept the backup gap.** It is the value outlier: the cheapest per TB and the simplest array. If you want the 3 TB all-Gen5 array with a full SATA image, A is better; if you need 6 TB, B is better.

## Part dossiers

- [ASRock WRX90 WS EVO](../parts/asrock-wrx90-ws-evo.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 64 GB DDR5-5600](../parts/samsung-64gb-5600.md)
- [Samsung 990 PRO 1 TB](../parts/samsung-990-pro.md)
- [Samsung 870 EVO 4 TB](../parts/samsung-870-evo.md)
- [MCIO to M.2 cable](../parts/mcio-cable.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
