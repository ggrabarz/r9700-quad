# F — Full Speed, 8×64 GB 6400

<div class="hero" markdown>
<span class="eyebrow">Build F · the 512 GB endgame</span>

**Eight 64 GB modules, eight channels, 409.6 GB/s.** The full-speed configuration: G.Skill’s 8-DIMM 6400 octa kit, sold as one validated 512 GB kit.

[:octicons-arrow-right-24: Jump to BOM](#bom) · [All builds](index.md) · [Memory ladder](../reference/memory-ladder.md)
</div>

<div class="build-meta" markdown>
<div><span class="k">Platform total</span><span class="v price">€29,057.79*</span></div>
<div><span class="k">Orderable Proshop</span><span class="v">€33,766.02</span></div>
<div><span class="k">Memory</span><span class="v">8×64 GB 6400</span></div>
<div><span class="k">Channels</span><span class="v">8 / 409.6 GB/s</span></div>
<div><span class="k">Array</span><span class="v">3× Gen5 / 3 TB</span></div>
</div>

<p class="small muted">* The €29,057.79 total uses Alternate’s <strong>notify-only</strong> €23,094 price. Proshop can order the same kit at €27,666.06, which puts the platform at €33,766.02 and the four-GPU total at €41,486.86.</p>

## What it is

Build A’s storage with one **G.Skill T5 Neo 8×64 GB DDR5-6400 CL38 octa kit** (F5-6400R3848F64GE8-T5N). It is a different bin from the 4×64 kit: CL38-48-48-102 at 1.35 V, binned for eight DIMMs. On WRX90, 8 DIMMs is **1 DIMM per channel**, so 6400 is the CPU’s native 1DPC topology, not a 2-DIMM-per-channel overclock.

This is the configuration for DeepSeek UD-Q8 (508 GB set), a large model library, and the full 512 GB host side. It is also the most expensive line in the book: the RAM is 79.5% of the platform at the notify-only price.

## BOM

<div class="bom" markdown>
--8<-- "_bom/f.md"
</div>

[Download the CSV](../downloads/option-f.csv){ .md-button } [G.Skill 8×64 dossier](../parts/gskill-8x64-6400.md){ .md-button }

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **512 GB at 409.6 GB/s**, eight channels, 1 DIMM per channel.
- **G.Skill’s 8-DIMM 6400 octa kit**, not two 4×64 kits; the bin is intended for this load.
- **The cheapest 512 GB 6400 at the notify-only price** (€45.11/GB).
- **DeepSeek UD-Q8 / large-model streaming** becomes a host-RAM problem, not a capacity problem.
- **Uses A’s 3 TB Gen5 array and 4 TB SATA image.**
</div>
<div markdown>
### <span class="bad">Cons</span>

- **€23,094 notify-only / €27,666.06 orderable** — the RAM is 79.5% of the platform.
- **Eight DIMMs at 6400 is the training stress case**; the ASRock/ASUS QVL is still unverified.
- **G.Skill does not print the rank**; confirm 2Rx4 on the label/QVL.
- **Two 4×64 kits are not a substitute**: €24,270.02, CL36, not the 8-DIMM bin.
- **The PSU connector issue remains**; the build also needs the second-PSU decision.
- **The 236 tok/s Radiance reference is not a Strata number**; this build still needs the acceptance run.
</div>
</div>

## Verdict

**Buy F if 512 GB is the target and you can accept the octa-kit price.** At the notify-only price it is the cheapest 512 GB 6400; orderable, eight Micron singles are €26,239.76 and the platform is €32,297.93 — €1,426.30 cheaper than the orderable G.Skill octa. For a 2× start, use D.

## Part dossiers

- [G.Skill 8×64 GB DDR5-6400](../parts/gskill-8x64-6400.md)
- [ASRock WRX90 WS EVO](../parts/asrock-wrx90-ws-evo.md)
- [AMD Threadripper PRO 9955WX](../parts/amd-9955wx.md)
- [Samsung 9100 PRO 1 TB](../parts/samsung-9100-pro.md)
- [Seasonic PRIME PX-2200](../parts/seasonic-px-2200.md)
- [Radeon AI PRO R9700](../parts/radeon-r9700.md)
