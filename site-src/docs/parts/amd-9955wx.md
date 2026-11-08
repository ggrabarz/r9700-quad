# AMD Ryzen Threadripper PRO 9955WX

<p class="muted"><strong>€1,637.70</strong> · Geizhals DE · 16C/32T, 128 PCIe 5.0 lanes, 8-channel DDR5-6400. Used in every WRX90 build.</p>

## What it is

The 16-core Threadripper PRO for the sTR5 WRX90 platform. It has **128 PCIe 5.0 lanes**, **8-channel DDR5 ECC RDIMM** support at an official **6400 MT/s**, and a 350 W TDP. It is the CPU that makes the four x16 GPUs, the six NVMe ports and the 8×64 GB memory path fit on one board without a PLX switch.

The 16 cores are deliberate: Strata’s AMD reference configuration uses 15 expert workers, and the model is GPU-resident. More cores do not help the IQ3_S decode loop; they help the CPU expert lane for DeepSeek spill.

## Specifications

| Feature | Detail |
|---|---|
| Cores / threads | 16C / 32T |
| Clock | 4.5 GHz base, 5.4 GHz boost |
| Cache | 64 MB L3 |
| TDP | 350 W |
| PCIe | **128× PCIe 5.0 lanes** |
| Memory | **8-channel DDR5-6400 ECC RDIMM** |
| Socket | sTR5 |
| Price | **€1,637.70** (MSRP $1,649) |

## Assessment

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Strengths</span>

- **128 PCIe 5.0 lanes**: four x16 GPUs + storage with room to spare.
- **8-channel DDR5-6400**: 409.6 GB/s at 8 DIMMs, the fastest host path in the book.
- **16C/32T** matches the 15 expert workers; no core waste.
- **sTR5 WRX90** native PRO platform; RDIMM/ECC from the start.
- **350 W** is manageable with the XE360-TR5.
</div>
<div markdown>
### <span class="bad">Weaknesses</span>

- **€1,637.70** — a large line for a GPU-resident build.
- **350 W** adds heat and PSU load.
- **DDR5-6400 64 GB modules are expensive**; the CPU supports 6400, the RAM price is the limit.
- **No 8×64 6400 QVL proof**; the CPU is not the question, the board/module combination is.
</div>
</div>

## Where it is used

[A](../builds/a-balanced.md) · [B](../builds/b-capacity.md) · [C](../builds/c-value.md) · [D](../builds/d-staged-6400.md) · [E](../builds/e-fast-ram.md) · [F](../builds/f-full-speed.md) · [G](../builds/g-asus-premium.md) · [H](../builds/h-asus-4x-gen5.md)
