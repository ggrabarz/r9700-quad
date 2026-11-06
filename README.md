# R9700 ×4 — ASRock WRX90 WS EVO build book

**Scope:** a four-GPU AMD Radeon AI PRO R9700 (32 GB) inference platform for the Strata engine, serving Qwen3.8-Flash-Next Swift 1.5 IQ3_S (or IQ3_XXS) at up to 262,144 tokens of context with as many full-context streams as 128 GB of VRAM will hold. The four GPUs are already owned; this book prices and specifies everything else.

**Price snapshot:** 2026-11-06, EUR including VAT, EU (Germany/Austria comparison, Alternate DE retail). Prices are listed offers, not quotes; stock moves. The machine-readable snapshot is [`bom/prices.json`](bom/prices.json), the arithmetic is [`tools/calc.py`](tools/calc.py), the build sheets are [`bom/`](bom/), and the one-page visual is [`report.html`](report.html).

---

## 0. The short answer

**Build Option A — “Balanced, 3× Gen5”.**

| | Part | Why |
|---|---|---|
| Board | **ASRock WRX90 WS EVO** | Proper WRX90 for the 9955WX + RDIMM, **IPMI/AST2600**, 7× PCIe 5.0 x16, 6 NVMe ports, 8 DIMM/2 TB, €808.05. |
| CPU | **Ryzen Threadripper PRO 9955WX** | 16C/32T, 5.4 GHz, 350 W, **128 PCIe 5.0 lanes**, **8-channel DDR5 ECC**, €1,637.70. |
| RAM | **2× 64 GB Samsung M321R8GA0PB0-CWM** | DDR5-5600 CL46 2Rx4 ECC RDIMM. 128 GB now in 2 of 8 channels; 8× 64 GB = 512 GB later. |
| Storage | **3× Samsung 9100 PRO 1 TB, RAID 0** | **3 TB, all-Gen5** (1 Gen5 M.2 + 2 Gen5 MCIO), ~42–44 GB/s, ~5.6M 4K IOPS. €792. |
| Cold | **Samsung 870 EVO 4 TB SATA** | OS + model archive; a 3 TB array image fits in the 3.6 TB usable space. |
| PSU | **Seasonic PRIME PX-2200** | 2,200 W ATX 3.1, 2× native 12V-2x6 + 2 adapters + 4× PCIe 8-pin; 26% headroom. |
| Cooling | **SilverStone XE360-TR5** | 360 mm sTR5 AIO, top-mounted exhaust. |
| Case | **Fractal Design Meshify 2 XL** | EEB 305×330, 9+3 slots, 250 mm PSU, 4× 2-slot GPUs. |

**Platform total (GPUs excluded): €10,115.45 + 3% contingency = €10,418.91.**

With the four GPUs at today’s replacement price: **€18,139.75**.

The alternatives: **Option B — 6× Gen4, 6 TB** at **€11,705.38**; **Option C — 4× Gen4, 4 TB** at **€10,682.59**. The rest of this book explains why A is the middle.

**Headline numbers**

- 4× 32 GB = **128 GB VRAM**; IQ3_S is a **79 GB** download (≈50 GB experts, 1.5 GB dense on disk / ≈3.5 GiB per card in VRAM, 28.8 GB PLE table).
- KV at 262,144 tokens is **10.55 KB/token with `k8v4`** → **2.64 GB per full-context stream**; **8 streams = 21.1 GB** of KV, about 5.3 GB per card. Eight streams fit with ≈6.5 GB left on the main card; twelve are a test target; sixteen do not fit the conservative budget.
- **1,630 W continuous** (4×300 W GPU + 350 W CPU + 80 W platform), **2,200 W PSU** → 570 W / 25.9% headroom, 7.54 A at 230 V.
- **76 PCIe 5.0 lanes used in Option A** (64 for the GPUs + 12 for the three Gen5 ports) of the 9955WX’s 128 → 52 spare; Option B uses 88 (40 spare), Option C 80 (48 spare).
- **Measured anchors:** one R9700 does 94.7 tok/s decode on IQ3_S at a 27K prompt; two R9700 reach 125 tok/s with a pipeline window, and the published 3/4-card steps add +19%/+22%. **Projection for this build: ~150 tok/s single-stream decode, 3,000+ tok/s prefill at 32K.** That projection is unverified until the acceptance run in [`docs/VALIDATION.md`](docs/VALIDATION.md).

### Buy list — Option A

| Qty | Part | Line |
|---:|---|---:|
| 1 | ASRock WRX90 WS EVO | €808.05 |
| 1 | AMD Ryzen Threadripper PRO 9955WX (boxed, no cooler) | €1,637.70 |
| 2 | Samsung 64 GB DDR5-5600 CL46 2Rx4 ECC RDIMM (M321R8GA0PB0-CWM) | €4,998.00 |
| 3 | Samsung 9100 PRO 1 TB (PCIe 5.0 x4) | €792.00 |
| 1 | Samsung 870 EVO 4 TB SATA SSD | €665.00 |
| 2 | MCIO-to-M.2 NVMe adapter cable (estimate) | €80.00 |
| 1 | Seasonic PRIME PX-2200 (2200 W, ATX 3.1) | €489.90 |
| 1 | SilverStone SST-XE360-TR5 (360 mm sTR5 AIO) | €389.90 |
| 1 | Fractal Design Meshify 2 XL | €209.90 |
| 3 | 140 mm PWM case fan (estimate) | €45.00 |
| | **Parts subtotal** | **€10,115.45** |
| | 3% contingency | €303.46 |
| | **Platform total (GPUs excluded)** | **€10,418.91** |

**Today’s pick: ASRock WRX90 WS EVO.** It is the proper WRX90 platform for the 9955WX + RDIMM, it includes IPMI (the TRX50 AI TOP cannot add it), it is cheaper than the TRX50 AI TOP before cabling, and its six NVMe ports make the 3× Gen5 array a clean all-Gen5 build. The one trade is the TRX50 AI TOP’s four Gen5 M.2 sockets; with the current **Gen5 9100 PRO at €264** — the same price as the Gen4 990 PRO — the three Gen5 drives on the ASRock are the better array today anyway.

---

## 1. What the machine has to do

### 1.1 The GPUs

| Property | Radeon AI PRO R9700 32 GB |
|---|---|
| Architecture | RDNA 4, Navi 48, gfx1201 |
| Compute units | 64 (4,096 stream processors) |
| VRAM | 32 GB GDDR6, 256-bit, 20 Gbps |
| Board power | 300 W |
| Power connector | 1× 12V-2x6 (16-pin) |
| Form factor | 2-slot blower, 266.7 × 111.2 × 40 mm |
| Bus | PCIe 5.0 x16 |
| Outputs | 4× DisplayPort 2.1a (some partners add HDMI) |

The reference design and the board-partner cards checked here are 2-slot blowers at 267 × 111 × 40 mm. That is what makes a four-card tower possible: each card exhausts out the back instead of recirculating into the card below. Verify all four are the 2-slot blower variant.

### 1.2 The model

| Property | Value |
|---|---|
| Architecture | `qwen4exp`, 48 layers, hybrid attention/SSM (every 4th layer full attention) |
| Experts | 512 per layer, 10 active per token |
| Context | 262,144 tokens |
| Attention | 24 heads, 2 KV heads, key/value length 256 |
| Weights | IQ3_S: 79 GB on disk; ≈50 GB expert arena + 1.5 GB dense; PLE table 28.8 GB |
| Alternative | IQ3_XXS: 76 GB, ≈43 GB experts — 7 GB cheaper in VRAM, slightly lower quality |
| KV (int8) | 13.7 KB/token → 3.42 GB per 262K stream |
| KV (`k8v4`) | 10.55 KB/token → 2.64 GB per 262K stream |

The PLE table is why the storage plan matters: Strata reads a few rows per token from a 28.8 GB n-gram table. With 128 GB of RAM it can live in memory (`--ple-io ram`); the 3 TB array is still the fast working set for the model and checkpoints.

### 1.3 Software path

Strata (upstream Niko1221/Strata; if your “coldniko” build is a fork, check its flag names) runs on the R9700 through its HIP backend, compiled for `gfx1201`. The engine package carries its own ROCm runtime; the host only needs the kernel `amdgpu` driver. Multi-GPU is a **layer split**: each card holds a contiguous range of layers, its share of the expert cache, a copy of the dense weights and its own session state; the last card runs the head and the MTP draft layer. The split needs no NVLink and tolerates x8/x4 links; all four cards here are Gen5 x16.

The published AMD support matrix lists the R9700 as maintainer-tested, and the multi-GPU docs include measured 2/3/4-card results. HIP multi-GPU is younger than CUDA; the acceptance run is mandatory.

---

## 2. The board: ASRock WRX90 WS EVO

### 2.1 Specs and why

| Feature | Detail | Why it matters |
|---|---|---|
| Chipset / CPU | AMD WRX90, sTR5, PRO 9000/7000 WX | Native PRO + RDIMM platform; no TRX50 hybrid caveats. |
| Memory | 8× DDR5 RDIMM/RDIMM-3DS, 8-channel, 2 TB | 2×64 now; 8×64 = 512 GB later. |
| PCIe | 7× PCIe 5.0 x16 (6× x16 + 1× x8) | Four GPUs fit; the extra slots are covered by 2-slot cards. |
| NVMe | 1× Gen5 M.2 + 1× Gen4 M.2 + 2× Gen5 MCIO + 2× Gen4 SlimSAS | Six NVMe ports: 3× Gen5 or 6× Gen4 arrays. |
| SATA | 4× SATA3 | OS/cold SSD and an 8 TB image drive. |
| LAN / BMC | 2× Intel X710 10GbE + **AST2600 IPMI** | Out-of-band power/KVM/monitoring; the TRX50 AI TOP has no BMC. |
| VRM | 18+3+3, 110 A, active VRM cooling | Adequate for the 350 W 9955WX; good sustained margin. |
| Form | EEB 305×330 mm | Meshify 2 XL fits. |
| Price | **€808.05** (Geizhals, 59 offers) | €88.70 cheaper than the TRX50 AI TOP. |

The 9955WX is a PRO part; the ASRock is the native WRX90 board for it. The **TRX50 AI TOP is a hybrid** (TRX50 chipset, 8 RDIMM slots, PRO support, 4 Gen5 M.2, no IPMI); it works, but it is not the standard TRX50 UDIMM/non-Pro platform and it cannot add a BMC. The **Gigabyte WRX90 AI TOP** is the announced Gigabyte WRX90 alternative (IPMI, 7 slots, 2 Gen5 M.2 + 1 Gen4 M.2 + 2 MCIO); no price/retail offers at the snapshot.

### 2.2 Slots with four 2-slot GPUs

The ASRock’s seven x16 slots are 1-slot pitch. Four 2-slot cards go in **PCIE1, 3, 5, 7**; slots 2/4/6 are covered, and the fourth card’s second bracket lands in the case’s 8th slot. There is **no free slot** for a 4× M.2 carrier or a NIC/HBA. The storage expansion is the MCIO/SlimSAS ports, not a carrier.

The Meshify 2 XL has 9+3 slots, so the four cards fit with the 9th slot spare. The 9000D’s 8 slots fit exactly.

### 2.3 Lane and port budget

| Consumer | Lanes / ports | Notes |
|---|---:|---|
| 4× PCIe 5.0 x16 | 64 lanes | One per GPU. |
| 6 NVMe ports | 4× x4 + 2× x4 (Gen5/Gen4) | 3 Gen5 + 3 Gen4; 3 Gen5 array or 6 Gen4. |
| SATA | 4 ports | 4 TB SATA + optional 8 TB HDD. |
| 10GbE / IPMI | 2× 10G + 1× 1G BMC | Onboard. |
| CPU lanes | 128 total | A 76, B 88, C 80 used; 40–52 spare. |

No PLX switch and no lane-sharing gamble. The ASRock’s MCIO/SlimSAS ports are independent of the x16 slots.

---

## 3. Memory: 2×64 now, 8×64 later

### 3.1 Population and speed

| Now / later | Slots | Channels | Bandwidth at DDR5-5600 | Capacity |
|---|---|---:|---:|---:|
| 2 DIMMs (now) | A1 + E1 | 2 | 89.6 GB/s | 128 GB |
| 4 DIMMs | A1 + C1 + E1 + G1 | 4 | 179.2 GB/s | 256 GB |
| 8 DIMMs (later) | all | 8 | 358.4 GB/s | 512 GB |

The ASRock’s 8-channel population is the native WRX90 layout. The 2-DIMM start uses A1 + E1; confirm the final pair against the board’s memory support list.

**Speed ceilings:** the 9955WX is officially **DDR5-6400**. The ASRock advertises **7600+ OC**, the WRX90 AI TOP **7800 OC** (reported), the TRX50 AI TOP has no published max (TRX50 OC R-DIMM kits ~7200). Those are **2–4 DIMM OC R-DIMM** numbers, not 8×64 GB 2Rx4. With the specified **5600** modules, all boards run **5600**; with 6400-rated 64 GB 2Rx4 modules on the QVL, the 8×64 realistic ceiling is **6400** (409.6 GB/s). The current 5600 modules are the limit, not the board.

**Why 5600 in the BOM?** Because it is the fastest **64 GB 2Rx4 ECC RDIMM** that is a volume, JEDEC, QVL-friendly part at a sane price. The 64 GB 2Rx4 5600 module is €39.05/GB; 6400 64 GB 2Rx4 modules are rarer and carry a premium, and the 7600/7800 figures are 2–4 DIMM OC R-DIMM kits (16/24/32 GB), not eight 64 GB modules. The 9955WX’s official 6400 is only **+14% host bandwidth** (89.6 → 102.4 GB/s at 2 DIMMs; 358.4 → 409.6 at 8), and the decode loop is GPU-bound with the experts in VRAM; the host bandwidth mostly affects model load, PLE, checkpoints and CPU fallback. The 8×64 capacity is the real endgame lever, not the last 800 MT/s. If you can source 6400-rated 64 GB 2Rx4 modules on the QVL at a fair price, take them; otherwise 5600 is the correct cost/benefit choice, and the 8×64 endgame at 5600 is the stable target.

### 3.2 Why 128 GB now

- The model is 79 GB on disk; the PLE table is 28.8 GB. With 128 GB of VRAM the experts live on the GPUs, but the host needs the PLE table (28.8 GB with `--ple-io ram`), the OS/page cache and checkpoint headroom. 64 GB is the documented minimum (IQ3_S “with little else open”); 128 GB is the comfortable floor.
- 2×64 keeps four slots free for the 8× path; four 32 GB DIMMs would consume half the slots and make 512 GB a full replacement.
- 2Rx4 is the right organisation at 64 GB; do not mix 2Rx4/2Rx8 or brands/timings in a channel set.

### 3.3 The DRAM tax

At the snapshot the Samsung 64 GB 2Rx4 5600 RDIMM is **€2,499** — **€39.05/GB**, **~48% of the platform total**. This is the 2026 DRAM shortage, not a design choice. 64 GB modules are the cheapest per-GB RDIMM in this snapshot (a 4×16 GB kit is €3,346 for 64 GB). A 2×32 GB start saves ~€2,500 but leaves 64 GB — the wrong trade for a 79 GB model with a 28.8 GB PLE. If you can wait/buy used-server pulls, 64 GB DDR5-4800/5600 2Rx4 can cut this line; verify part/rank/ECC and run MemTest86+.

### 3.4 One stick or two?

One 64 GB RDIMM runs the GPU-resident IQ3_S workload in low-RAM mode with the PLE on the SSD, but it blocks `--ple-io ram` (28.8 GB), the full 16 GB conversation cache, two Saber Flash-Next servers, and leaves ~4 GB headroom. Two sticks are the practical floor and the specified dual-channel configuration; the second is €2,499 and is the first step of the 8×64 path. The detailed math and test plan are in [`docs/RAM-START.md`](docs/RAM-START.md).

---

## 4. Storage: 3× Gen5, 6× Gen4, or 4× Gen4

The ASRock’s six NVMe ports make three coherent arrays:

| Option | Array | Capacity | Ports used | Extra | Image on 4 TB SATA? |
|---|---|---:|---|---|---|
| **A** | **3× 9100 PRO 1 TB Gen5 RAID 0** | **3 TB** | 1 Gen5 M.2 + 2 Gen5 MCIO | 2 MCIO cables | **yes (3 TB < 3.6 TB)** |
| B | 6× 990 PRO 1 TB Gen4 RAID 0 | 6 TB | 2 M.2 + 2 MCIO + 2 SlimSAS | 4 cables + 8 TB HDD | no — needs the 8 TB HDD |
| C | 4× 990 PRO 1 TB Gen4 RAID 0 | 4 TB | 2 M.2 + 2 MCIO | 2 MCIO cables | no (4 TB > 3.6 TB) |

### 4.1 Why 3× Gen5 wins the middle

- **Price parity:** the Samsung 9100 PRO 1 TB is **€264**, the 990 PRO 1 TB **€262**. Three Gen5 drives cost €792 vs €786 for three Gen4 — €6 more for all-Gen5.
- **Speed:** 3× Gen5 ≈ **42–44 GB/s** sequential and **~5.6M** 4K IOPS, versus 4× Gen4 ≈ 28–30 GB/s and ~4.8M. The 3-drive Gen5 array is faster than the 4-drive Gen4 array, with 1 TB less capacity.
- **Topology:** 1 Gen5 M.2 + 2 Gen5 MCIO = exactly the ASRock’s three Gen5 ports. The Gen4 M.2 is free for the OS/scratch or a 4th Gen4 drive; there is no Gen4 member in the array.
- **Backup:** 3 TB fits a full image on the 4 TB SATA (3.6 TB usable). A 4 TB or 6 TB array does not; the 6 TB option needs an 8 TB HDD.

### 4.2 The 4 TB SATA

The 870 EVO 4 TB is **€665**. Partition it as **256 GB OS + 3.6 TB archive**. The 3 TB array image fits; keep the model/tokenizer/pack archive there. A 500 GB 870 EVO is €203.90; the 4 TB is the better €/GB. The PM893 3.84 TB is €2,430 — not worth it for cold archives.

### 4.3 6× Gen4 (Option B) and 4× Gen4 (Option C)

- **6× Gen4:** 6 TB, ~44 GB/s, ~7.2M IOPS. It uses all six NVMe ports, so the OS goes on the 4 TB SATA; add an **8 TB N300 HDD (€389)** for a full array image. The six-drive RAID 0 has a higher failure probability; the 8 TB image is the mitigation.
- **4× Gen4:** 4 TB, ~28–30 GB/s, ~4.8M IOPS, €1,048 in drives. It is the cheapest per TB; the 4 TB array cannot be fully imaged on the 4 TB SATA, so add an 8 TB HDD if you want the same backup discipline.
- **4× Gen5:** only on the TRX50 AI TOP (4 Gen5 M.2); 4 TB, ~56–59 GB/s, no IPMI. It is the max-speed alternative, not the ASRock build.

### 4.4 M.2/MCIO thermal reality

The ASRock’s two onboard M.2 sit near the slots; the MCIO/SlimSAS drives can be mounted in the case’s 2.5" bays away from the GPU heat. That is a real advantage over the TRX50 AI TOP’s four M.2 under the cards. Use the case’s bottom intake; monitor `smartctl -A`; target <70 °C. Gen5 drives run hotter than Gen4; the MCIO placement is why the 3× Gen5 array is practical.

### 4.5 RAID 0 reality

RAID 0 has no redundancy. The array is a working set, not a backup. Keep the model/config archive on the 4 TB SATA; for the 3 TB array, the SATA can hold a full image; for 4/6 TB, add the 8 TB HDD. A single drive failure loses the array; the archive is the recovery path.

---

## 5. Power, cooling, chassis

### 5.1 Power

| Load | Continuous |
|---|---:|
| 4× R9700 at 300 W | 1,200 W |
| 9955WX at 350 W | 350 W |
| Board, RAM, 3–6 NVMe, 1–2 SATA, fans | 80 W |
| **Total** | **1,630 W** |
| PSU | 2,200 W |
| **Headroom** | **570 W / 25.9%** |

Input at 94% efficiency ≈1,734 W, **7.54 A at 230 V**. Use a **16 A circuit** and a C19/C20 cord; the PX-2200 is **200–240 V only**.

The ASRock has **2× 8-pin ATX12V**, **2× 6-pin PCIe 12V**, and **2× 6-pin GFX 12V**. It requires 6-pin PCIe 12V to GFX_12V1/2 or it may not boot. The Seasonic’s 4× PCIe 6+2 cables cover the GFX inputs; the 2× native 12V-2x6 + 2 adapters feed the four GPUs. Connect the board GFX first.

**Do not** substitute a 1600 W unit: 1,630 W continuous is 102% of its rating. It only works with all four GPUs capped to ~250 W.

### 5.2 Cooling and chassis

- Four blowers exhaust out the back; 3×140 front intake (2 included, add one), 1×140 rear, 2×140 bottom for the M.2/GPU zone.
- 9955WX 350 W: the XE360-TR5 360 mm AIO top-mounted is the right choice; Noctua NH-U14S TR5-SP6 is the air alternative if you accept less sustained margin.
- Heat: 1,630 W = **5,562 BTU/h**; utility room/AC. Noise ~45–50 dBA at load.
- Meshify 2 XL: EEB 305×330, 9+3 slots, 250 mm PSU, 480 mm top radiator, 6×3.5 + 2×2.5; fits the ASRock, four 2-slot GPUs, the 360 AIO and the 210 mm PSU.
- The ASRock’s 7 slots: four 2-slot GPUs in 1/3/5/7; no free carrier. The 6 NVMe ports are the storage path.

### 5.3 UPS

A 2,200 VA / 1,600–1,800 W pure-sine UPS is the right class; budget €500–900. The RAID 0 has no redundancy and an unclean shutdown during a checkpoint write is the most likely way to lose it.

---

## 6. Will it serve the model?

### 6.1 Model fit

| Item | IQ3_S | IQ3_XXS |
|---|---:|---:|
| Download | 79 GB | 76 GB |
| Experts | ≈50 GB | ≈43 GB |
| Dense | 1.5 GB on disk; ≈3.5 GiB/card in VRAM | same |
| PLE | 28.8 GB (SSD/RAM) | 28.8 GB |
| Verdict | **Fits 128 GB VRAM with 8×262K streams** | More headroom; more streams |

### 6.2 Per-card budget (first-order)

| Item per card | Helper | Main |
|---|---:|---:|
| Experts share (50 GB / 4) | 12.50 GB | 12.50 GB |
| Dense copy (VRAM) | 3.50 GB | 3.50 GB |
| Prompt/session buffers | 2.00 GB | 2.00 GB |
| Head + MTP draft | — | 0.80 GB |
| GPU vision reader | — | 1.47 GB |
| **Used** | **18.00 GB** | **20.27 GB** |
| **Free of 32 GB** | **14.00 GB** | **11.73 GB** |

This is a budgeting model; the actual split depends on layers/cache/prompt path. The dense copy is the docs’ 3.5 GiB/card for IQ3_S, not the 1.5 GB file.

### 6.3 Full-context streams

At 262,144 tokens:

| KV format | KB/token | GB per 262K stream | 8 streams | Per card at 8 |
|---|---:|---:|---:|---:|
| int8 | 13.7 | 3.42 | 27.4 GB | 6.85 GB |
| **k8v4** | **10.55** | **2.64** | **21.1 GB** | **5.28 GB** |

| Streams at 262K | KV total | Per card | Main free after KV | Verdict |
|---:|---:|---:|---:|---|
| 4 | 10.6 GB | 2.6 GB | 9.1 GB | Trivial |
| **8** | **21.1 GB** | **5.3 GB** | **6.5 GB** | **Recommended** |
| 12 | 31.7 GB | 7.9 GB | 3.8 GB | Test target |
| 16 | 42.2 GB | 10.6 GB | 1.2 GB | Too tight |

**Starting config:** `--batch 8`, `--max-context 262144`, `--kv k8v4`, `--kv-resident 0` (all KV in VRAM). Test 12 at 262K, 16 at 131K.

### 6.4 Measured anchors and projection

| Configuration | Decode | Prefill | Source |
|---|---:|---:|---|
| 1× R9700, IQ3_S, 27K | 94.7 tok/s | 2,411 tok/s (KVA off) | Strata KVA doc |
| 2× R9700, code, pipeline | 125 tok/s | — | Strata multi-GPU doc |
| 3/4× R9700 steps | +19% / +22% | — | same table |
| 4× RX 7900 XT, IQ3_S, 262K | 67.6 @4K; 65.6 @32K | — | same |
| 4× R9700, DeepSeek V4.1 2.00 bpw | 74–77 tok/s | 400–450 @8K | Strata README |

**Projection for this build:** ≈150 tok/s single-stream decode, 3,000+ tok/s prefill at 32K, from the 125 tok/s two-card anchor and +22% four-card step, plus no CPU expert fallback. Unverified; the acceptance run replaces it.

At 8 concurrent 262K streams, per-stream decode is lower; plan 300–500 tok/s aggregate as the target band and measure.

---

## 7. The three builds

All three use the ASRock WRX90 WS EVO, 9955WX, 2×64 GB, 2,200 W, XE360-TR5 and Meshify 2 XL. They differ only in storage.

### Option A — Balanced, 3× Gen5 (recommended)

| Item | Qty | Unit | Line |
|---|---:|---:|---:|
| ASRock WRX90 WS EVO | 1 | €808.05 | €808.05 |
| Threadripper PRO 9955WX | 1 | €1,637.70 | €1,637.70 |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | 2 | €2,499.00 | €4,998.00 |
| Samsung 9100 PRO 1 TB Gen5 | 3 | €264.00 | €792.00 |
| Samsung 870 EVO 4 TB SATA | 1 | €665.00 | €665.00 |
| MCIO-to-M.2 cable (est.) | 2 | €40.00 | €80.00 |
| Seasonic PRIME PX-2200 | 1 | €489.90 | €489.90 |
| SilverStone XE360-TR5 | 1 | €389.90 | €389.90 |
| Fractal Meshify 2 XL | 1 | €209.90 | €209.90 |
| 140 mm fans (est.) | 3 | €15.00 | €45.00 |
| **Platform subtotal** | | | **€10,115.45** |
| Contingency 3% | | | €303.46 |
| **Platform total** | | | **€10,418.91** |
| GPUs (owned, replacement) | 4 | €1,930.21 | €7,720.84 |
| **Total if buying GPUs** | | | **€18,139.75** |

**Why it wins:** 3 TB all-Gen5 at the price of 3× Gen4, 3 TB fits a full image on the 4 TB SATA, IPMI/proper WRX90, and 1 TB less than C but faster and cheaper. The 3 TB array holds the stated models (~1.1 TB used) with ~1.9 TB free.

### Option B — Capacity, 6× Gen4

| Item | Qty | Unit | Line |
|---|---:|---:|---:|
| ASRock WRX90 WS EVO | 1 | €808.05 | €808.05 |
| Threadripper PRO 9955WX | 1 | €1,637.70 | €1,637.70 |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | 2 | €2,499.00 | €4,998.00 |
| Samsung 990 PRO 1 TB Gen4 | 6 | €262.00 | €1,572.00 |
| Samsung 870 EVO 4 TB SATA | 1 | €665.00 | €665.00 |
| Toshiba N300 8 TB SATA HDD | 1 | €389.00 | €389.00 |
| MCIO-to-M.2 cable (est.) | 2 | €40.00 | €80.00 |
| SlimSAS-to-NVMe cable (est.) | 2 | €40.00 | €80.00 |
| Seasonic PRIME PX-2200 | 1 | €489.90 | €489.90 |
| SilverStone XE360-TR5 | 1 | €389.90 | €389.90 |
| Fractal Meshify 2 XL | 1 | €209.90 | €209.90 |
| 140 mm fans (est.) | 3 | €15.00 | €45.00 |
| **Platform subtotal** | | | **€11,364.45** |
| Contingency 3% | | | €340.93 |
| **Platform total** | | | **€11,705.38** |
| GPUs (owned, replacement) | 4 | €1,930.21 | €7,720.84 |
| **Total if buying GPUs** | | | **€19,426.22** |

**Buy this if:** you need a 6 TB working set/model library. It uses all six NVMe ports, needs the 8 TB HDD for a full image, and has a higher RAID 0 failure domain. It is +€1,286.47 over A for +3 TB.

### Option C — Value, 4× Gen4

| Item | Qty | Unit | Line |
|---|---:|---:|---:|
| ASRock WRX90 WS EVO | 1 | €808.05 | €808.05 |
| Threadripper PRO 9955WX | 1 | €1,637.70 | €1,637.70 |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | 2 | €2,499.00 | €4,998.00 |
| Samsung 990 PRO 1 TB Gen4 | 4 | €262.00 | €1,048.00 |
| Samsung 870 EVO 4 TB SATA | 1 | €665.00 | €665.00 |
| MCIO-to-M.2 cable (est.) | 2 | €40.00 | €80.00 |
| Seasonic PRIME PX-2200 | 1 | €489.90 | €489.90 |
| SilverStone XE360-TR5 | 1 | €389.90 | €389.90 |
| Fractal Meshify 2 XL | 1 | €209.90 | €209.90 |
| 140 mm fans (est.) | 3 | €15.00 | €45.00 |
| **Platform subtotal** | | | **€10,371.45** |
| Contingency 3% | | | €311.14 |
| **Platform total** | | | **€10,682.59** |
| GPUs (owned, replacement) | 4 | €1,930.21 | €7,720.84 |
| **Total if buying GPUs** | | | **€18,403.43** |

**Buy this if:** 4 TB capacity matters more than Gen5 speed and you accept a Gen4 array. It is **€263.68 more than A** for +1 TB but slower (28–30 vs 42–44 GB/s) and cannot be fully imaged on the 4 TB SATA without the 8 TB HDD.

### What not to buy

- **A 24-core 9965WX (+€1,378).** The 16C/32T 9955WX gives the 15 expert workers Strata’s AMD reference config uses; more cores do not help a GPU-resident model.
- **128/256 GB RDIMMs.** Worse €/GB than 8×64; the 2 TB ceiling is not a target.
- **A 1600 W PSU.** 1,630 W continuous is over its rating.
- **A 7th/8th GPU.** The case/power/PCIe and 2-slot stacking do not support it; the 9-GPU marketing is single-slot/riser territory.
- **A 4× M.2 carrier.** With four 2-slot GPUs there is no free slot; the ASRock’s six NVMe ports are the storage path.

---

## 8. Cost/benefit

| Metric | A 3× Gen5 | B 6× Gen4 | C 4× Gen4 |
|---|---:|---:|---:|
| Platform total | €10,418.91 | €11,705.38 | €10,682.59 |
| With GPUs at replacement | €18,139.75 | €19,426.22 | €18,403.43 |
| Array capacity | 3 TB | 6 TB | 4 TB |
| Array sequential (approx.) | 42–44 GB/s | 44–45 GB/s | 28–30 GB/s |
| 4K IOPS (approx.) | 5.6M | 7.2M | 4.8M |
| Storage cost (drives/cables/archive) | €1,537 | €2,786 | €1,793 |
| Storage €/TB | ~€512 | ~€464 | ~€448 |
| Per VRAM GB (platform) | €81.40 | €91.45 | €83.46 |
| Per 262K stream at 8 (platform) | €1,302.36 | €1,463.17 | €1,335.32 |
| Energy 100% / 50% (wall) | €3,797.55 / €1,888.73 | same | same |

A is the middle: it is €263.68 cheaper than C and faster, with 1 TB less; it is €1,286.47 cheaper than B with 3 TB less. B is the capacity outlier; C is the 4 TB value outlier.

At 50% load the machine draws ~862 W at the wall (~7,550 kWh/year, €1,889 at €0.25/kWh). Add the platform amortized over three years (€3,473/year for A) and the all-in compute cost is ~€5,362/year before GPUs, comparable to a cloud GPU rental at 8×262K streams.

---

## 9. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Gen5/MCIO drives run hot | Medium | Throttling/array slowdown | Mount MCIO drives in the 2.5" bays, bottom intake, SMART <70 °C. |
| RAID 0 loses a drive | Low–Medium | Array lost | 4 TB SATA image for the 3 TB array; 8 TB HDD for 4/6 TB; UPS; archive. |
| 6× Gen4 higher failure domain | Medium | Array lost | 8 TB HDD image; cold archive; replace the drive and restore. |
| 8×64 GB RDIMM training/QVL | Medium | Lower speed/no boot | Buy the exact Samsung part; check the QVL; 2× start is low-risk; 8× is the stress case. |
| ASRock 6-pin GFX 12V not connected | Certain | No boot | Connect 6-pin PCIe 12V to GFX_12V1/2; the Seasonic 6+2 cables cover it. |
| TRX50 AI TOP has no IPMI | Certain | No out-of-band | Choose ASRock/WRX90 AI TOP if IPMI is required; BMC cannot be added to the TRX50. |
| 9955WX/ASRock stock | Medium | Delay | Geizhals offers; re-check before ordering; ASRock is available at the snapshot. |
| DRAM price | High | Budget | 2×64 now; 8× later; used-server pulls with warranty. |
| BIOS needs 9000WX support | Medium | No boot | Flash the latest BIOS; ASRock supports PRO 9000WX. |
| Noise/heat in a living space | High | Comfort | Utility room/rack; 5,562 BTU/h; 45–50 dBA. |

---

## 10. Build order and BIOS

### 10.1 Before assembly

1. Flash the latest ASRock BIOS; confirm 9955WX support.
2. Check the ASRock memory QVL for the exact Samsung M32... part, especially at 8 DIMMs.
3. Verify all four GPUs are 2-slot blowers (40 mm).
4. Dry-fit the 360 AIO top and the 210 mm PSU; confirm the 2.5" bays for the MCIO drives.

### 10.2 Assembly

1. CPU into sTR5; 2×64 GB RDIMMs in A1 + E1.
2. 1× 9100 PRO in M2_1 (Gen5); 2× 9100 PRO on the MCIO Gen5 ports via the adapter cables, mounted in the 2.5" bays. The Gen4 M.2 stays free.
3. Board into the case; EEB standoffs.
4. 360 AIO top; pump/fans to CPU headers.
5. PSU, 24-pin, 2× EPS, 6-pin PCIe 12V to PCIE12V1/2 and GFX_12V1/2.
6. GPUs in PCIE1/3/5/7; 2 native 12V-2x6 + 2 adapters; board GFX first.
7. 4 TB SATA to SATA3_0; 8 TB HDD (B only) to SATA3_1.
8. Front/bottom/rear fans; fan curves.

### 10.3 BIOS

- Above 4G Decoding: Enabled; Re-Size BAR: Enabled; CSM: Disabled.
- IOMMU: Enabled (diagnostics); PCIe slots Auto/Gen5; verify x16 on all four GPUs.
- Memory: EXPO/XMP off for ECC stability; JEDEC 5600; ECC auto. Confirm ECC in the OS.
- Fan curves: front/bottom intake on GPU temp; AIO pump full; rear moderate.
- Power: balanced/typical; no extreme OC on a 24/7 server.
- BMC: set the IPMI LAN IP; enable remote power/KVM.

### 10.4 OS and engine

- **OS:** Ubuntu 24.04 LTS with HWE kernel (6.14+) or 26.04 LTS. RDNA4/Zen5 need a current kernel.
- **Driver:** kernel `amdgpu`; the Strata `rx9070` package carries its own ROCm runtime; no system ROCm install.
- **Strata:** install the `rx9070` Linux package (gfx1200/gfx1201) or build HIP `gfx1201`; `strata-device --list-devices` must show four R9700s.
- **Model:** IQ3_S shards, pack, tokenizer, MTP on `/srv/models` (the 3 TB array); PLE on the same array; `--ple-io ram` with 128 GB RAM.
- **Config:** start from [`configs/strata-4x-r9700-8x262k.json`](configs/strata-4x-r9700-8x262k.json), adjust paths.

---

## 11. Acceptance

Full protocol in [`docs/VALIDATION.md`](docs/VALIDATION.md). Short version:

1. MemTest86+ 8 passes; ECC zero.
2. `fio` on `/dev/md0`: 3× Gen5 ≥35 GB/s sequential, ≥4M 4K IOPS; SMART <70 °C.
3. Wall meter: ≤2,000 W full load; 12V-2x6/6-pin connectors <60 °C.
4. Thermals: GPU edge/hotspot, CPU, M.2/MCIO, VRM; 30 min; no throttle.
5. PCIe: 32 GT/s x16 on all four; no AER.
6. Strata: 1 stream 262K, then 8 streams 262K; decode/prefill/TTFT/VRAM/power.
7. Soak: 24 h 8 streams + 64K cold prompts; no drops/VRAM growth/ECC.

**Gates:** 8×262K stable; ≥250 tok/s aggregate decode (target 300–500, no stream <25); ≥2,500 tok/s prefill at 32K; <2,000 W; zero ECC/AER; M.2 <75 °C.

---

## 12. Sources and price snapshot

| Item | Price | Source |
|---|---:|---|
| ASRock WRX90 WS EVO | €808.05 | [Geizhals EU](https://geizhals.eu/asrock-wrx90-ws-evo-90-mxbmh0-a0uayz-a3167681.html) |
| Threadripper PRO 9955WX | €1,637.70 | [Geizhals DE](https://geizhals.de/amd-ryzen-threadripper-pro-9955wx-100-100000725wof-a3531872.html) |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | €2,499.00 | [Geizhals EU](https://geizhals.eu/samsung-rdimm-64gb-m321r8ga0pb0-cwm-a3528359.html) |
| Samsung 9100 PRO 1 TB | €264.00 | [Alternate DE](https://www.alternate.de/Samsung/9100-PRO-1-TB-SSD/html/product/100118126) |
| Samsung 990 PRO 1 TB | €262.00 | [Alternate DE](https://www.alternate.de/Samsung/990-PRO-1-TB-SSD/html/product/1864239) |
| Samsung 870 EVO 4 TB | €665.00 | [Alternate DE](https://www.alternate.de/Samsung/870-EVO-4-TB-SSD/html/product/1706407) |
| Toshiba N300 8 TB | €389.00 | [Alternate DE](https://www.alternate.de/Toshiba/N300-8-TB-Festplatte/html/product/100111191) |
| Seasonic PRIME PX-2200 | €489.90 | [Alternate DE](https://www.alternate.de/Seasonic/PRIME-PX-2200-2200W-ATX-3-1-PC-Netzteil/html/product/100076188) |
| SilverStone XE360-TR5 | €389.90 | [Alternate DE](https://www.alternate.de/SilverStone/SST-XE360-TR5-Wasserk%C3%BChlung/html/product/100114775) |
| Fractal Meshify 2 XL | €209.90 | [Alternate DE](https://www.alternate.de/Fractal-Design/Meshify-2-XL-Black-TG-Light-Tint-Big-Tower-Geh%C3%A4use/html/product/1669747) |
| PowerColor R9700 32 GB (reference) | €1,930.21 | [Geizhals EU](https://geizhals.eu/powercolor-radeon-ai-pro-r9700-a3504726.html) |
| Gigabyte TRX50 AI TOP (alternative) | €896.75 | [Geizhals EU](https://geizhals.eu/gigabyte-trx50-ai-top-a3246131.html) |
| Gigabyte WRX90 AI TOP (announced) | TBD | [Geizhals listing](https://geizhals.eu/gigabyte-wrx90-ai-top-amd-str5-a3995002.html) |

**Technical sources:** [ASRock WRX90 WS EVO spec](https://www.asrock.com/mb/AMD/WRX90%20WS%20EVO/index.asp), [ASRock manual](https://download.asrock.com/Manual/WRX90%20WS%20EVO.pdf), [AMD 9955WX](https://www.amd.com/en/products/processors/workstations/ryzen-threadripper/9000-wx-series/amd-ryzen-threadripper-pro-9955wx.html), [Seasonic PX-2200 datasheet](https://seasonic.com/wp-content/uploads/2024/06/ATX-3.1-PRIME-PX-2200.pdf), [Fractal Meshify 2 XL sheet](https://assets.fractal-design.com/files/uxzbxy2o/production/1bc60fe11df0e6b0269090a88eec38f36586ff3c.pdf), and the Strata docs in `/root/git/strata/docs/`.

**Price caveat:** listed “from” prices are not reservations. Re-check every offer before ordering; the 3% contingency covers shipping/volatility.

---

## Appendix — files

| File | Purpose |
|---|---|
| [`report.html`](report.html) | One-page visual summary. |
| [`bom/prices.json`](bom/prices.json) | Price snapshot, options, assumptions. |
| [`bom/option-a.csv`](bom/option-a.csv) | Balanced 3× Gen5 build sheet. |
| [`bom/option-b.csv`](bom/option-b.csv) | Capacity 6× Gen4 build sheet. |
| [`bom/option-c.csv`](bom/option-c.csv) | Value 4× Gen4 build sheet. |
| [`tools/calc.py`](tools/calc.py) | Totals, power, lanes, memory, VRAM/KV/streams. |
| [`tools/export_bom.py`](tools/export_bom.py) | Regenerates CSVs. |
| [`configs/strata-4x-r9700-8x262k.json`](configs/strata-4x-r9700-8x262k.json) | 8×262K Strata preset. |
| [`configs/strata-4x-r9700-16x131k.json`](configs/strata-4x-r9700-16x131k.json) | 16×131K preset. |
| [`docs/RAM-START.md`](docs/RAM-START.md) | 1×64 vs 2×64, one-stick test plan. |
| [`docs/WRX90-ASROCK.md`](docs/WRX90-ASROCK.md) | Board comparison, storage tiers, dense/MoE streaming. |
| [`docs/SABER.md`](docs/SABER.md) / [`docs/SABER-4X.md`](docs/SABER-4X.md) | Saber engine evaluation and 4-rank limits. |
| [`docs/VALIDATION.md`](docs/VALIDATION.md) | Acceptance protocol. |
| [`docs/SOURCES.md`](docs/SOURCES.md) | Source links and verification notes. |
