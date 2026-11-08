# Micron 64 GB DDR5-6400 ECC RDIMM

<p class="muted"><strong>€3,279.97</strong> per 64 GB module · Galaxus DE · the JEDEC 2×64 GB 6400 path. Used in <a href="../../builds/d-staged-6400/">D</a>.</p>

## What it is

The Micron **MTC40F2046S1RC64BH1**: a 64 GB DDR5-6400 **2Rx4 ECC RDIMM**, CL52 at **1.1 V**, with 40× 4Gb x4 components. It is a single-module JEDEC part, not an EXPO kit, and Micron’s part page confirms the 2Rx4 organisation.

Two modules give 128 GB, two channels and 102.4 GB/s; eight give 512 GB, eight channels and 409.6 GB/s. It is the only part in the book that lets a 2×64 GB start reach 8×64 GB at 6400 without changing the memory family.

## Specifications

| Feature | Detail |
|---|---|
| Capacity | 64 GB |
| Speed | DDR5-6400 |
| Timings | CL52 |
| Organisation | **2Rx4** (40× 4Gb x4) |
| ECC | Yes, registered RDIMM |
| Voltage | **1.1 V JEDEC** |
| Price | **€3,279.97** |
| €/GB | **€51.25** |

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **JEDEC 2Rx4, CL52, 1.1 V**, manufacturer-confirmed.
- **The literal 2×64 GB 6400 start**; no kit, no unused sticks.
- **The 8×64 path is the same part**: 512 GB / 409.6 GB/s for €26,239.76.
- **No EXPO/OC dependency**; it is the conservative 6400 part.
- **Available as a single module**, so you can buy two now and six later.
</div>
<div markdown>
### <span class="bad">Cons</span>

- **€51.25/GB**, +31.2% over the 5600 module.
- **Two channels at 2×**; 102.4 GB/s is only +14.3% over the 5600 pair.
- **Eight modules are the dearest 512 GB path**; €26,239.76 RAM, €32,297.93 platform.
- **QVL/8-DIMM 6400 training** is still unverified on the ASRock/ASUS boards.
- **Stock/price at Galaxus** is a single listing; re-check before ordering.
</div>
</div>

## Where it is used

- [D — Staged 6400 2×64](../builds/d-staged-6400.md)
