# E — Fast RAM, 4×64 GB 6400

<div class="hero" markdown>
<span class="eyebrow">Build E · 256 GB at 6400</span>

**Four 64 GB G.Skill modules, 256 GB, four channels, 204.8 GB/s.** The 256 GB middle: twice the capacity and twice the channels of the 2× builds, at a lower €/GB than the 2× Micron pair.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [Memory ladder](../reference/memory-ladder.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€17,770.03</span></div>
<div><span class="k">With 4 GPUs</span><span class="v">€25,490.87</span></div>
<div><span class="k">Memory</span><span class="v">4×64 GB 6400</span></div>
<div><span class="k">Channels</span><span class="v">4 / 204.8 GB/s</span></div>
<div><span class="k">Array</span><span class="v">3× Gen5 / 3 TB</span></div>
</div>

## What it is

Build A’s storage with one **G.Skill T5 Neo 4×64 GB DDR5-6400 CL36 kit** (F5-6400R3644E64GQ4-T5N). It is an AMD EXPO R-DIMM kit at 1.30 V, 4 channels, 204.8 GB/s. Four DIMMs fill half the board; the other four slots stay open.

The kit is **€12,135.01 at Proshop** (1–2 months, max 2 per customer), or €12,269 at Alternate with 17–25 days. The 4×64 kit is CL36; the 8×64 octa kit is CL38. They are not the same bin.

## BOM

<div class="bom" markdown>
--8<-- "_bom/e.md"
</div>

[Download the CSV](../downloads/option-e.csv){ .md-button } [G.Skill 4×64 dossier](../parts/gskill-4x64-6400.md){ .md-button }

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **256 GB and four channels** for €12,135.01 — 2× the capacity and 2× the channels of the 2× builds.
- **€47.40/GB**, cheaper than the 2× Micron pair (€51.25/GB) and only +21.4% over the 5600 module.
- **204.8 GB/s** is enough for DeepSeek 2.00/2.25 bpw and a comfortable PLE/page-cache.
- **Leaves four slots open** for the 8×64 endgame.
- **Uses A’s 3 TB Gen5 array and 4 TB SATA image.**
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **€7,351.12 over A**; the RAM line is now 68.3% of the platform.
- **The 8×64 upgrade is the octa kit, not a second 4×64 kit.** Two quads cost €24,270.02 and are not the validated 8-DIMM bin.
- **1–2 months lead time** at Proshop; Alternate is faster but €134 more.
- **Rank/QVL unverified**: G.Skill does not print 2Rx4/2Rx8; confirm on the label and the ASRock QVL.
- **The PSU connector issue remains.**
</div>
</div>

## Verdict

**Buy E if 256 GB is the target and you want the cheapest 6400 per GB before the octa kit.** It is the fast middle. If 128 GB is enough, D is the literal 2× start; if you need 512 GB, F is the endgame.

## Part dossiers

- [G.Skill 4×64 GB DDR5-6400](../parts/gskill-4x64-6400.md)
- [ASRock WRX90 WS EVO](../parts/asrock-wrx90-ws-evo.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 9100 PRO 1 TB](../parts/samsung-9100-pro.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
