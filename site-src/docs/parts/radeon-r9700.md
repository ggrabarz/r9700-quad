# Radeon AI PRO R9700 32 GB

<p class="muted"><strong>€1,930.21</strong> replacement value · four owned · 32 GB GDDR6, 300 W, 2-slot blower. The reason for the build.</p>

## What it is

AMD’s RDNA 4 workstation card, Navi 48 / gfx1201, with **32 GB of GDDR6** on a 256-bit bus. It is a **2-slot blower** at 267×111×40 mm, 300 W, with one **12V-2x6** connector and PCIe 5.0 x16. Four of them give 128 GB of VRAM.

The blower is what makes a four-card tower possible: each card exhausts out the back instead of recirculating into the card below. The 32 GB per card is what lets IQ3_S’s expert set live in VRAM.

## Specifications

| Feature | Detail |
|---|---|
| Architecture | RDNA 4, Navi 48, gfx1201 |
| Compute units | 64 (4,096 stream processors) |
| VRAM | **32 GB GDDR6**, 256-bit, 20 Gbps |
| Board power | **300 W** |
| Power connector | **1× 12V-2x6** |
| Bus | PCIe 5.0 x16 |
| Form factor | **2-slot blower**, 267×111×40 mm |
| Outputs | 4× DisplayPort 2.1a (partner-dependent) |
| Price | **€1,930.21** replacement (owned) |

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **32 GB per card**, 128 GB total; the IQ3_S expert set fits in VRAM.
- **2-slot blower**, the only sane four-card stacking layout.
- **PCIe 5.0 x16**, 64 GB/s per direction; no NVLink needed for layer split.
- **300 W** per card, 1,200 W total; the PX-2200 has the watts.
- **ROCm/HIP support**; Strata’s `rx9070` package carries its own runtime.
</div>
<div markdown>
### <span class="bad">Cons</span>

- **300 W per card** and four blowers: 5,562 BTU/h, 45–50 dBA.
- **No NVLink**; multi-GPU is PCIe/layer split, not a unified pool.
- **12V-2x6 per card**; four connectors and a PSU cable budget.
- **Availability/price** moves; the €1,930.21 is a snapshot.
- **The performance projection is unverified** until the acceptance run.
</div>
</div>

## Where it is used

All builds. The four cards are owned and excluded from the platform totals; the €1,930.21 is replacement value only.
