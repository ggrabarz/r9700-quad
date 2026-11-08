# H — ASUS 4× Gen5

<div class="hero" markdown>
<span class="eyebrow">Build H · 4 TB all-Gen5</span>

**Four 9100 PRO drives, four Gen5 M.2 sockets, 4 TB.** The ASUS board at full storage: no MCIO, no SlimSAS in the array, and an 8 TB HDD for the image because 4 TB no longer fits the 4 TB SATA.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [Part dossiers](../parts/index.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€11,503.45</span></div>
<div><span class="k">With 4 GPUs</span><span class="v">€19,224.29</span></div>
<div><span class="k">Board</span><span class="v">ASUS WRX90E-SAGE</span></div>
<div><span class="k">Memory</span><span class="v">2×64 GB 5600</span></div>
<div><span class="k">Array</span><span class="v">4× Gen5 / 4 TB</span></div>
</div>

## What it is

Build G with a **fourth 9100 PRO** and a **Toshiba N300 8 TB HDD**. Four Gen5 M.2 drives use all four onboard sockets; no MCIO, no SlimSAS in the array. The 4 TB array is larger than the 3.6 TB usable space on the 4 TB SATA, so the 8 TB N300 is the image drive.

This is the max-storage ASUS build: 4 TB all-Gen5, ~56–59 GB/s sequential, and a 4 TB array. It is also the hottest M.2 configuration — four Gen5 drives under four 2-slot GPUs.

## BOM

| Part | Qty | Unit | Line | Notes |
|---|---:|---:|---:|---|
| [ASUS Pro WS WRX90E-SAGE SE](../parts/asus-wrx90e-sage-se.md) | 1 | €1,288.00 | €1,288.00 | 4× Gen5 M.2, 2× SlimSAS Gen4, 32+3+3+3, dual-PSU, IPMI. |
| [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md) | 1 | €1,637.70 | €1,637.70 | 16C/32T, 128 lanes, 8-channel. |
| [Samsung 64 GB DDR5-5600](../parts/samsung-64gb-5600.md) | 2 | €2,499.00 | €4,998.00 | 128 GB value pair. |
| [Samsung 9100 PRO 1 TB](../parts/samsung-9100-pro.md) | 4 | €264.00 | €1,056.00 | Four Gen5 M.2 drives. |
| [Samsung 870 EVO 4 TB](../parts/samsung-870-evo.md) | 1 | €665.00 | €665.00 | OS + cold archive; cannot image the 4 TB array. |
| [Toshiba N300 8 TB](../parts/toshiba-n300.md) | 1 | €389.00 | €389.00 | Full array image. |
| [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md) | 1 | €489.90 | €489.90 | 2,200 W; connector caveat. |
| [SilverStone XE360-TR5](../parts/silverstone-xe360-tr5.md) | 1 | €389.90 | €389.90 | 360 mm sTR5 AIO. |
| [Fractal Meshify 2 XL](../parts/fractal-meshify-2-xl.md) | 1 | €209.90 | €209.90 | EEB, 9+3 slots. |
| [140 mm PWM fan](../parts/fan-140.md) | 3 | €15.00 | €45.00 | Bottom/rear airflow. |
| **Platform subtotal** | | | **€11,168.40** | |
| 3% contingency | | | €335.05 | |
| **Platform total** | | | **€11,503.45** | |
| GPUs (owned, replacement) | 4 | €1,930.21 | €7,720.84 | Excluded from platform. |
| **Total if buying GPUs** | | | **€19,224.29** | |

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **4 TB all-Gen5** with no MCIO and no SlimSAS in the array.
- **Four Gen5 M.2 sockets** exactly match the four drives; no carrier.
- **A full image on the 8 TB HDD**, unlike the 4 TB SATA-only plan.
- **The ASUS premium board**: 32+3+3+3, dual-PSU, IPMI, the public 4× R9700 reference.
- **+€1,084.54 over A** for +1 TB and an all-Gen5 4 TB array.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **Four Gen5 M.2 drives under four GPUs**; the hottest storage layout in the book.
- **The 8 TB HDD is required** for a full image; the 4 TB SATA is not enough.
- **The PSU connector issue remains**: 4 GPUs + ASUS 2× PCIE_8P needs a second PSU / more PCIe 8-pin.
- **The RAM is still 2×64 5600**; no 6400 in this build.
- **4 TB RAID 0** is a larger failure domain than A’s 3 TB.
</div>
</div>

## Verdict

**Buy H if 4 TB all-Gen5 is the target and you accept the M.2 thermal risk.** It is the max-storage ASUS build; the 8 TB image is part of the price. If 3 TB is enough, G is cheaper and cooler; if you need 6 TB, B is the capacity route.

## Part dossiers

- [ASUS WRX90E-SAGE SE](../parts/asus-wrx90e-sage-se.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 64 GB DDR5-5600](../parts/samsung-64gb-5600.md)
- [Samsung 9100 PRO 1 TB](../parts/samsung-9100-pro.md)
- [Samsung 870 EVO 4 TB](../parts/samsung-870-evo.md)
- [Toshiba N300 8 TB](../parts/toshiba-n300.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
