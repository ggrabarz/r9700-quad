# D — Staged 6400, 2×64 GB

<div class="hero" markdown>
<span class="eyebrow">Build D · the literal 2× start</span>

**Two 64 GB DDR5-6400 Micron modules now, six later, all JEDEC 2Rx4.** The only path in the book that starts at two DIMMs and reaches 8×64 GB at full 6400 without replacing the pair.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [Memory ladder](../reference/memory-ladder.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€12,027.71</span></div>
<div><span class="k">With 4 GPUs</span><span class="v">€19,748.55</span></div>
<div><span class="k">Memory</span><span class="v">2×64 GB 6400</span></div>
<div><span class="k">Channels</span><span class="v">2 / 102.4 GB/s</span></div>
<div><span class="k">Array</span><span class="v">3× Gen5 / 3 TB</span></div>
</div>

## What it is

Build A’s storage and platform with **two Micron MTC40F2046S1RC64BH1** 64 GB DDR5-6400 modules instead of the Samsung 5600 pair. The Micron part is JEDEC **2Rx4, CL52, 1.1 V**, not an EXPO kit; it is the single-module path that lets you start with two DIMMs and add six more without changing the memory family.

Two modules give 128 GB, two channels and **102.4 GB/s**. It is only +14.3% bandwidth over the 5600 pair, but it is **+31.2% per GB** — the premium for staying at 6400 from the first stick to the eighth.

## BOM

<div class="bom" markdown>
--8<-- "_bom/d.md"
</div>

[Download the CSV](../downloads/option-d.csv){ .md-button } [Micron part dossier](../parts/micron-64gb-6400.md){ .md-button }

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **The literal 2×64 GB 6400 start.** No 4×64 kit, no unused sticks.
- **JEDEC 2Rx4, CL52, 1.1 V**, with Micron’s manufacturer spec confirmed.
- **The 8×64 path is the same part**: eight modules = 512 GB / 409.6 GB/s, €26,239.76 at the listed price.
- **No replacement of the first pair** when you expand; the 5600 pair would have to be replaced.
- **Keeps A’s 3 TB Gen5 array and 4 TB SATA image.**
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **€6,559.94 for 128 GB** — +€1,561.94 over the 5600 pair, +31.2% per GB.
- **Two channels only**; 102.4 GB/s is barely above the 5600 pair’s 89.6, and far below 4×/8×.
- **The 8× Micron path is the dearest 512 GB option** (€26,239.76 RAM; €32,297.93 platform).
- **QVL/8-DIMM training** is still unverified; the Micron part is single-module, not an octa kit.
- **The PSU connector issue remains.**
</div>
</div>

## Verdict

**Buy D if the 2× start is non-negotiable and you want to stay at 6400 to 8×.** It is the conservative, spec-confirmed path. If you can start at 4×64, [E](e-fast-ram.md) is cheaper per GB; if you can buy 512 GB at once, [F](f-full-speed.md) is cheaper per GB and is G.Skill’s 8-DIMM kit.

## Part dossiers

- [Micron 64 GB DDR5-6400](../parts/micron-64gb-6400.md)
- [ASRock WRX90 WS EVO](../parts/asrock-wrx90-ws-evo.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 9100 PRO 1 TB](../parts/samsung-9100-pro.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
