# G — ASUS Premium, 3× Gen5 M.2

<div class="hero" markdown>
<span class="eyebrow">Build G · premium board, no MCIO</span>

**ASUS WRX90E-SAGE SE, three Gen5 M.2 drives, no adapter cables.** The premium platform swap: four Gen5 M.2 sockets, a 32+3+3+3 VRM, dual-PSU wiring, and a public 4× R9700 reference build.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [ASUS vs ASRock](../parts/asus-wrx90e-sage-se.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€10,830.86</span></div>
<div><span class="k">With 4 GPUs</span><span class="v">€18,551.70</span></div>
<div><span class="k">Board</span><span class="v">ASUS WRX90E-SAGE</span></div>
<div><span class="k">Memory</span><span class="v">2×64 GB 5600</span></div>
<div><span class="k">Array</span><span class="v">3× Gen5 M.2 / 3 TB</span></div>
</div>

## What it is

Build A’s CPU, memory and storage capacity on the **ASUS Pro WS WRX90E-SAGE SE**. Three 9100 PRO drives go in three of the board’s four onboard Gen5 M.2 sockets; the two MCIO cables disappear. The fourth M.2 socket stays free for a 4× Gen5 build later.

The ASUS costs **€1,288.00**, €479.95 more than the ASRock. Removing the €80 of MCIO cables makes the net parts delta **+€399.95**; with 3% contingency the platform is **+€411.95** over A. The board adds four Gen5 M.2, two SlimSAS Gen4 ports, a 32+3+3+3 VRM, dual-PSU wiring, and the same AST2600 IPMI.

## BOM

<div class="bom" markdown>
--8<-- "_bom/g.md"
</div>

[Download the CSV](../downloads/option-g.csv){ .md-button } [ASUS board dossier](../parts/asus-wrx90e-sage-se.md){ .md-button }

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **Four Gen5 M.2 sockets**: the 3× Gen5 array needs no MCIO cables, and the fourth socket is free.
- **32+3+3+3 VRM** vs the ASRock’s 18+3+3; more margin for the 350 W 9955WX.
- **Dual-PSU wiring** is documented; the PSU connector fix is cleaner than on the ASRock.
- **Public 4× R9700 reference build** on this exact board, CPU and 128 GB 6400 memory.
- **Only +€411.95 over A** for the premium board.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **M.2 sockets sit under the four GPUs**; the ASRock’s MCIO drives in the 2.5" bays are cooler for 24/7 Gen5.
- **The fourth Gen5 drive is tempting but a 4 TB array no longer fits the 4 TB SATA image**; add the 8 TB HDD.
- **The PSU connector issue remains**: four GPUs consume all four PCIe 8-pin, and the ASUS board still wants 2× PCIE_8P.
- **No 8×64 6400 validation**; the reference build is 128 GB, not 512 GB.
- **€1,288 board price**; the premium is real.
</div>
</div>

## Verdict

**Buy G if you want the premium board, no MCIO cabling, and the proven 4-GPU configuration.** It is the best foundation for a 3× Gen5 M.2 build; the only reason to stay on the ASRock is the MCIO thermal layout or the €411.95. If you want the fourth Gen5 drive, go to [H](h-asus-4x-gen5.md).

## Part dossiers

- [ASUS WRX90E-SAGE SE](../parts/asus-wrx90e-sage-se.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 64 GB DDR5-5600](../parts/samsung-64gb-5600.md)
- [Samsung 9100 PRO 1 TB](../parts/samsung-9100-pro.md)
- [Samsung 870 EVO 4 TB](../parts/samsung-870-evo.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
