# B — Capacity, 6× Gen4

<div class="hero" markdown>
<span class="eyebrow">Build B · capacity outlier</span>

**6 TB across all six NVMe ports, with an 8 TB HDD for the image.** The same WRX90 platform as A, but the storage is tuned for a model library rather than all-Gen5 speed.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [Part dossiers](../parts/index.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€11,705.38</span></div>
<div><span class="k">With 4 GPUs</span><span class="v">€19,426.22</span></div>
<div><span class="k">Board</span><span class="v">ASRock WRX90</span></div>
<div><span class="k">Memory</span><span class="v">2×64 GB 5600</span></div>
<div><span class="k">Array</span><span class="v">6× Gen4 / 6 TB</span></div>
</div>

## What it is

Six Samsung 990 PRO 1 TB Gen4 drives in RAID 0: two onboard M.2 sockets, two Gen5 MCIO ports running Gen4 drives, and two Gen4 SlimSAS ports. That uses every NVMe port on the ASRock, so the OS and the archive move to SATA: a 4 TB 870 EVO for the OS and a **Toshiba N300 8 TB HDD** for a full image of the 6 TB array.

The pitch is capacity and cost per TB, not latency. The six-drive array has a higher RAID 0 failure domain than the three-drive A, which is why the 8 TB image is part of the build rather than an optional extra.

## BOM

<div class="bom" markdown>
--8<-- "_bom/b.md"
</div>

[Download the CSV](../downloads/option-b.csv){ .md-button } [Memory ladder](../reference/memory-ladder.md){ .md-button }

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **6 TB of working set**: room for several model packs, checkpoints and a cold archive.
- **All six NVMe ports used**; no carrier and no free-slot problem.
- **Good cost per TB** on 1 TB 990 PRO drives; the 6-drive array is ~44–45 GB/s sequential and ~7.2M 4K IOPS.
- **The 8 TB HDD gives a full image** of the array; the 4 TB SATA alone cannot.
- **Same board, CPU, RAM and PSU as A**, so the platform risk is unchanged.
</div>
<div markdown>
### <span class="bad">Cons</span>

- **Six-drive RAID 0** has a higher failure probability; the 8 TB HDD is mandatory, not optional.
- **Gen4, not Gen5**: ~44–45 GB/s vs 42–44 GB/s for A — sequential is similar, but the random/Gen5 ceiling is lower per drive.
- **No Gen5 array at all**; the MCIO and SlimSAS ports run Gen4 drives.
- **+€1,286.47 over A** for +3 TB; that is the price of capacity.
- **The PSU connector issue remains**: four GPUs consume all four PCIe 8-pin, leaving none for the board aux.
</div>
</div>

## Verdict

**Buy B only if 6 TB is the requirement.** It is the capacity outlier: more room, a real image drive, and a sensible cost per TB, at the cost of six drives and a slower per-drive ceiling. For the stated IQ3_S workload, A is the better middle; for a model library, B is the one.

## Part dossiers

- [ASRock WRX90 WS EVO](../parts/asrock-wrx90-ws-evo.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 64 GB DDR5-5600](../parts/samsung-64gb-5600.md)
- [Samsung 990 PRO 1 TB](../parts/samsung-990-pro.md)
- [Samsung 870 EVO 4 TB](../parts/samsung-870-evo.md)
- [Toshiba N300 8 TB](../parts/toshiba-n300.md)
- [MCIO to M.2 cable](../parts/mcio-cable.md)
- [SlimSAS to NVMe cable](../parts/slimsas-cable.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
