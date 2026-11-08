# Memory ladder

<p class="muted">The host memory decision is the second-biggest line after the GPUs, and the one that changes with the workload. This is the whole ladder, from the 5600 value floor to the 512 GB 6400 endgame.</p>

## The population

| DIMMs | Slots | Channels | DDR5-5600 | DDR5-6400 | Capacity |
|---|---|---:|---:|---:|---:|
| 2 | A1 + E1 | 2 | 89.6 GB/s | 102.4 GB/s | 128 GB |
| 4 | A1 + C1 + E1 + G1 | 4 | 179.2 GB/s | 204.8 GB/s | 256 GB |
| 8 | all | 8 | 358.4 GB/s | 409.6 GB/s | 512 GB |

WRX90 has **8 slots for 8 channels**, so 8 DIMMs is **1 DIMM per channel**. The 9955WX’s official DDR5-6400 is the 8-DIMM, 1DPC ceiling — not a 2-DIMM-per-channel overclock.

## The parts

| Part | Type | Capacity | Speed / timings | Voltage | Rank | Price | €/GB |
|---|---|---|---:|---:|---|---:|---:|
| [Samsung 64 GB DDR5-5600](../parts/samsung-64gb-5600.md) | single | 64 GB | 5600 CL46 | 1.1 V | 2Rx4 | €2,499.00 | €39.05 |
| [Micron 64 GB DDR5-6400](../parts/micron-64gb-6400.md) | single | 64 GB | 6400 CL52 | 1.1 V | **2Rx4** | €3,279.97 | €51.25 |
| [Kingston 64 GB DDR5-6400](../parts/kingston-64gb-6400.md) | single | 64 GB | 6400 CL52 | 1.1 V | not confirmed | €3,202.74 | €50.04 |
| [G.Skill 4×64 GB DDR5-6400](../parts/gskill-4x64-6400.md) | 4×64 kit | 256 GB | 6400 CL36 | 1.30 V | not printed | €12,135.01 | €47.40 |
| [G.Skill 8×64 GB DDR5-6400](../parts/gskill-8x64-6400.md) | 8×64 kit | 512 GB | 6400 CL38 | 1.35 V | not printed | €23,094.00* | €45.11 |

<p class="small muted">* Notify-only at Alternate; Proshop orderable €27,666.06 (€54.04/GB).</p>

## The ladder

| Config | Capacity | Channels | Bandwidth | RAM price | €/GB | Platform | With GPUs |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2×64 5600 (A) | 128 GB | 2 | 89.6 GB/s | €4,998.00 | €39.05 | €10,418.91 | €18,139.75 |
| 2×64 6400 Micron (D) | 128 GB | 2 | 102.4 GB/s | €6,559.94 | €51.25 | €12,027.71 | €19,748.55 |
| 4×64 6400 G.Skill (E) | 256 GB | 4 | 204.8 GB/s | €12,135.01 | €47.40 | €17,770.03 | €25,490.87 |
| 8×64 6400 G.Skill (F) | 512 GB | 8 | 409.6 GB/s | €23,094.00* | €45.11 | €29,057.79* | €36,778.63* |
| 8×64 6400 Micron | 512 GB | 8 | 409.6 GB/s | €26,239.76 | €51.25 | €32,297.93 | €40,018.77 |

## What to buy

- **If the 2× start is the requirement:** 2× Micron. It is the only path that starts at 2 DIMMs and reaches 8× at full 6400 with JEDEC 2Rx4 modules. It costs +31.2% per GB over the 5600 pair.
- **If 256 GB is enough:** 4× G.Skill. €47.40/GB, 204.8 GB/s, four slots left.
- **If 512 GB is the target:** G.Skill octa at the notify-only price, or eight Micron singles if you need an orderable price. Eight Micron is €26,239.76 / €32,297.93 platform.
- **If 128 GB is enough and budget is the constraint:** 2× 5600. It cannot reach 6400; the fast upgrade replaces the pair.

!!! warning "QVL and rank"
    G.Skill does not print 2Rx4/2Rx8 on the retail listing, and the ASRock/ASUS 8×64 6400 QVL is unverified. Confirm the module label and the board QVL before ordering. The 512 GB 8-DIMM 6400 training is the stress case.

!!! note "DeepSeek is different"
    IQ3_S fully resident is GPU-bound. DeepSeek V4.1 spill puts host RAM bandwidth on the decode path; the 6400 ladder is worth more there. See [build F](../builds/f-full-speed.md).
