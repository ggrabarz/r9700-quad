# R9700 ×4 — Gigabyte TRX50 AI TOP build book

**Scope:** a four-GPU AMD Radeon AI PRO R9700 (32 GB) inference platform for the Strata engine, serving Qwen3.8-Flash-Next Swift 1.5 IQ3_S (or IQ3_XXS) at up to 262,144 tokens of context with as many full-context streams as the 128 GB of VRAM will hold. The four GPUs are already owned; this book prices and specifies everything else.

**Price snapshot:** 2026-11-06, EUR including VAT, EU (Germany/Austria comparison, Alternate DE retail). Prices are listed offers, not quotes; stock moves. The full machine-readable snapshot is in [`bom/prices.json`](bom/prices.json), the arithmetic is in [`tools/calc.py`](tools/calc.py), each option has a CSV build sheet in [`bom/`](bom/), and the one-page visual summary is [`report.html`](report.html).

---

## 0. The short answer

**Build Option B — “Recommended”.** It is the middle of the quality/cost/performance triangle:

| | Part | Why |
|---|---|---|
| Board | **Gigabyte TRX50 AI TOP** | 4× PCIe 5.0 x16 for the GPUs, 4× PCIe 5.0 x4 M.2, 8 DIMM slots, 4 on-board PCIe aux feeds, 2× 10GbE, E-ATX. With a PRO CPU it runs all four x16 slots at Gen5 and all four M.2 at Gen5. |
| CPU | **Ryzen Threadripper PRO 9955WX** | 16C/32T, 5.4 GHz boost, 350 W, **128 PCIe 5.0 lanes**, **8-channel DDR5 ECC**, €1,637.70. The cheapest CPU that unlocks the board’s 8 DIMMs and full lane budget. |
| RAM | **2× 64 GB Samsung M321R8GA0PB0-CWM** | DDR5-5600 CL46, 2Rx4 ECC RDIMM. 128 GB now in 2 of 8 channels; 8× 64 GB = 512 GB octa-channel later. |
| Storage | **4× Samsung 990 PRO 1 TB, RAID 0** | 4 TB working set for weights, PLE table and checkpoints; ~28 GB/s sequential, ~4.8M 4K read IOPS across the four drives. |
| Cold | **Samsung 870 EVO 4 TB SATA** | 256 GB OS + 3.6 TB archive/backup of the model, configs and checkpoints. |
| PSU | **Seasonic PRIME PX-2200** | 2200 W ATX 3.1, 80+ Platinum, 2× native 12V-2x6 + 2× adapters + 4× PCIe 8-pin, 3× EPS. 26% headroom over the 1,630 W continuous budget. |
| Cooling | **SilverStone XE360-TR5 360 mm AIO** | sTR5/SP6 mount, 350 W class, top-mounted exhaust. |
| Case | **Fractal Design Meshify 2 XL** | SSI-EEB (305×330 mm) support, 9+3 slots, 250 mm PSU, 549 mm GPU, 480 mm top radiator, 3× 140 mm fans included. |

**Platform total (GPUs excluded): €10,380.15 + 3% contingency = €10,691.55.**

With the four GPUs at today’s replacement price: **€18,412.39**.

The same platform total with the lean air cooler and one extra fan is **€10,392.85** (Option A); the 256 GB / 8×-ready version is **€16,823.14** (Option C).

**The headline engineering numbers**

- 4× 32 GB = **128 GB VRAM**; IQ3_S is a **79 GB** download (≈50 GB of experts, 1.5 GB dense, 28.8 GB PLE table).
- KV at 262,144 tokens is **10.55 KB/token with `k8v4`** → **2.64 GB per full-context stream**; **8 streams = 21.1 GB** of KV, about 5.3 GB per card. Eight full-context streams fit with ≈6.5 GB left on the main card; twelve are a test target; sixteen do not fit the conservative budget.
- **1,630 W continuous** (4×300 W GPU + 350 W CPU + 80 W platform), **2,200 W PSU** → 570 W / 25.9% headroom, 7.54 A at 230 V.
- **80 PCIe 5.0 lanes used** (64 for GPUs + 16 for M.2) of the 9955WX’s 128 → 48 spare.
- **Measured anchors:** one R9700 does 94.7 tok/s decode on IQ3_S at a 27K prompt; two R9700 reach 125 tok/s with a pipeline window, and the published 3/4-card steps add +19%/+22%. **Projection for this build: ~150 tok/s single-stream decode, 3,000+ tok/s prefill at 32K.** That projection is explicitly unverified until the acceptance run in [`docs/VALIDATION.md`](docs/VALIDATION.md).

> **The one caveat that matters:** the CPU, board and RAM are chosen so the GPUs are the only bottleneck. The 16-core 9955WX is deliberate: Strata defaults to one expert worker per physical core (one less on 17+ cores), and the published AMD reference configuration uses 15 pool workers — exactly what a 16-core part provides. A 24-core 9965WX costs +€1,378 and adds workers that reference configuration does not use. Spend the difference on the 2.2 kW PSU, the AIO and the case, not on cores.

### Buy list — Option B

| Qty | Part | Line |
|---:|---|---:|
| 1 | Gigabyte TRX50 AI TOP | €896.75 |
| 1 | AMD Ryzen Threadripper PRO 9955WX (boxed, no cooler) | €1,637.70 |
| 2 | Samsung 64 GB DDR5-5600 CL46 2Rx4 ECC RDIMM (M321R8GA0PB0-CWM) | €4,998.00 |
| 4 | Samsung 990 PRO 1 TB (PCIe 4.0 x4) | €1,048.00 |
| 1 | Samsung 870 EVO 4 TB SATA SSD | €665.00 |
| 1 | Seasonic PRIME PX-2200 (2200 W, ATX 3.1) | €489.90 |
| 1 | SilverStone SST-XE360-TR5 (360 mm sTR5 AIO) | €389.90 |
| 1 | Fractal Design Meshify 2 XL | €209.90 |
| 3 | 140 mm PWM case fan (estimate) | €45.00 |
| | **Parts subtotal** | **€10,380.15** |
| | 3% contingency | €311.40 |
| | **Platform total (GPUs excluded)** | **€10,691.55** |

If you change one thing, change the cooling: the 360 AIO plus two extra bottom fans is the €290 (€299 with contingency) step from Option A to B, and it is the difference between a server that survives a hot room and one that throttles. Keep the 16-core CPU and the 2×64 GB RAM.

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
| Outputs | 4× DisplayPort 2.1a (some board partners add HDMI) |

The reference design and the board-partner cards checked here are blower-style 2-slot cards at 267 × 111 × 40 mm. That is what makes a four-card tower possible: each card exhausts out the back instead of recirculating into the card below. Verify that all four of your cards are the 2-slot blower variant before committing to the stack.

### 1.2 The model

From the GGUF metadata of the actual checkpoint and the Strata model documentation:

| Property | Value |
|---|---|
| Architecture | `qwen4exp`, 48 layers, hybrid attention/SSM (every 4th layer full attention) |
| Experts | 512 per layer, 10 active per token |
| Context | 262,144 tokens |
| Attention | 24 heads, 2 KV heads, key/value length 256 |
| Weights | IQ3_S: 79 GB on disk; ≈50 GB expert arena + 1.5 GB dense; PLE table 28.8 GB (figures rounded) |
| Alternative | IQ3_XXS: 76 GB download, ≈43 GB experts — 7 GB cheaper in VRAM, slightly lower quality |
| KV (int8) | 13.7 KB per token → 3.42 GB per 262K stream |
| KV (`k8v4`) | 23% less than int8 → 10.55 KB per token → 2.64 GB per 262K stream |

The PLE table is the reason the storage plan matters: Strata reads a few rows per token from a 28.8 GB n-gram table. On this machine it can live in the 128 GB of RAM (`--ple-io ram`), but the 4×1 TB RAID 0 still earns its place by making cold starts and re-reads fast.

### 1.3 The software path

Strata (upstream Niko1221/Strata; if your “coldniko” build is a fork, check its flag names against the upstream flags used here) runs on the R9700 through its HIP backend, compiled for `gfx1201`. The engine package carries its own ROCm runtime; the host only needs the kernel `amdgpu` driver. Multi-GPU is a **layer split** (pipeline parallelism), not tensor parallelism: each card holds a contiguous range of layers, its share of the expert cache, a copy of the dense weights and its own session state. The last card runs the output head and the MTP draft layer. The split needs no NVLink and tolerates x8/x4 links, but all four cards here are on Gen5 x16.

The published AMD support matrix lists the R9700 as maintainer-tested, and the multi-GPU documentation includes measured 2/3/4-card R9700 results. HIP multi-GPU is nevertheless younger than the CUDA path; treat the acceptance run as mandatory, not a formality.

**Alternative engine — Saber.** A new Rust engine, [Saber](https://github.com/GGZ14/saber-engine), targets the R9700 and serves Qwen3.8 Flash-Next, with a headline **229 tok/s for the 27B dense model on two cards**. It is **TP=1/2 only** and explicitly refuses TP=3/4, and it uses MXFP4 packs rather than IQ3_S/GGUF. It therefore cannot use all four cards for one model and does not change this build. The full evaluation — including its 95.4 GiB PLE table and what it would mean for a 2-GPU box — is in [`docs/SABER.md`](docs/SABER.md). The code-level answer to “can we just expand the 2× config to 4×?” — and the upstream docs/RFC patch — is in [`docs/SABER-4X.md`](docs/SABER-4X.md) and [`patches/`](patches/).

---

## 2. Why this board and this CPU

### 2.1 Gigabyte TRX50 AI TOP

From the board manual (rev. 1.07) and product specifications:

| Feature | Detail | Why it matters here |
|---|---|---|
| CPU socket | sTR5, TR PRO 9000-WX / 7000-WX and TR 9000 / 7000 | Drop-in path from a 16-core PRO to a 96-core PRO later. |
| Memory | 8× DDR5 RDIMM/RDIMM-3DS, up to 2 TB; 8-channel with PRO, 4-channel with non-PRO | Exactly the “2 DIMMs now, 8 DIMMs later” topology. |
| PCIe slots | 4× PCIe 5.0 x16 (PCIEX16_1…4), all CPU-attached | Four GPUs at full x16. With a non-PRO TR 7000, PCIEX16_4 is Gen4; with the PRO 9955WX all four are Gen5. |
| M.2 | 4× PCIe 5.0 x4 CPU-attached (M2C/B/A + M2D) | Four 1 TB drives at full Gen5 x4. M2D requires a PRO 9000WX/7000WX; the 9955WX is PRO, so all four work. |
| SATA | 4× SATA 6 Gb/s, RAID 0/1/10 for NVMe, RAID 0/1 for SATA | OS + cold SSD; the 4 TB SATA can be mirrored later if wanted. |
| Slot power | 4× on-board PCIe 8-pin power connectors (PCIE_12V1…4) | Supplemental 12 V for the x16 slots. With one PSU the manual calls for PCIE_12V1/2; all four are for a two-PSU setup. |
| LAN | 2× Marvell AQtion AQC113C 10GbE | Serve and manage on separate links without an add-in NIC. |
| USB4 | 2× USB4 Type-C (one with DisplayPort in) | Display/console without consuming a GPU slot. |
| Form factor | E-ATX, 30.5 × 33.0 cm | Needs a true E-ATX/SSI-EEB case; the Meshify 2 XL and 9000D both qualify. |
| BIOS recovery | Q-Flash Plus | Update the BIOS for the 9955WX without CPU/RAM installed. |

The block diagram is unambiguous: four x16 slots and four x4 M.2 sockets all hang directly off the sTR5 CPU. There is no chipset bottleneck and no lane-sharing switch to decode.

### 2.2 Ryzen Threadripper PRO 9955WX

| Property | 9955WX | 7965WX | 9965WX | 9975WX |
|---|---:|---:|---:|---:|
| Cores/threads | 16/32 | 24/48 | 24/48 | 32/64 |
| Zen generation | Zen 5 | Zen 4 | Zen 5 | Zen 5 |
| Boost | 5.4 GHz | 5.3 GHz | 5.4 GHz | 5.4 GHz |
| TDP | 350 W | 350 W | 350 W | 350 W |
| PCIe 5.0 lanes | 128 | 128 | 128 | 128 |
| Memory channels | 8 | 8 | 8 | 8 |
| EU price (2026-11-06) | **€1,637.70** | €2,460.54 | €3,016.00 | €4,009.00 |

The 9955WX is the value pick for three reasons:

1. **It unlocks the board.** A non-PRO 7960X would save money but leave four DIMM slots dead, the fourth M.2 disabled and PCIEX16_4 at Gen4 — it breaks the stated 8× memory path. The 9955WX is the cheapest current-generation (9000WX) part that does not.
2. **Strata does not need more cores.** The engine’s CPU pool computes experts only when they are not in VRAM. With 128 GB of VRAM the entire 50 GB expert set is resident, so the CPU is orchestrating prefill/decode, not grinding MoE experts. The engine defaults to one expert worker per physical core (one less on 17+ cores), and the published AMD reference configuration uses **15 pool workers** — exactly what a 16-core 9955WX supplies. A 24-core part would add workers the reference configuration does not use.
3. **It is the newest IOD at the lowest price.** Zen 5, 5.4 GHz, 128 lanes, 8 channels, 350 W. The 9965WX adds eight cores for +€1,378; that money buys the PSU, the AIO and the case instead, with a bigger effect on uptime and noise.

### 2.3 Lane and port budget

| Consumer | Lanes / ports | Notes |
|---|---:|---|
| 4× PCIe 5.0 x16 | 64 lanes | One per GPU; all Gen5 with the PRO CPU. |
| 4× M.2 PCIe 5.0 x4 | 16 lanes | 4× 1 TB RAID 0. |
| **Total CPU lanes** | **80 of 128** | 48 spare for future NIC/HBA/device. |
| SATA | 4 ports | OS/cold SSD; two spare. |
| 10GbE | 2 ports | Onboard. |
| PCIe aux power | 4 connectors | Feed from the PSU’s PCIe 8-pin cables. |

No PLX switch, no bifurcation card, no lane-sharing gamble. That is the main reason this board is the right foundation for four GPUs.

---

## 3. Memory: 2×64 GB now, 8×64 GB later

### 3.1 Population and bandwidth

The board has eight slots, one per channel, in two banks:

```
DDR5_H1  DDR5_G1  DDR5_F1  DDR5_E1
DDR5_A1  DDR5_B1  DDR5_C1  DDR5_D1
```

| Now / later | Slots | Channels | Bandwidth at DDR5-5600 | Capacity |
|---|---|---:|---:|---:|
| 2 DIMMs (now) | A1 + E1 | 2 | 89.6 GB/s | 128 GB |
| 4 DIMMs | A1 + C1 + E1 + G1 | 4 | 179.2 GB/s | 256 GB |
| 8 DIMMs (later) | all | 8 | 358.4 GB/s | 512 GB |

The 4-channel list (A1/C1/E1/G1) is exactly the board manual’s quad-channel population; the 2-DIMM start uses the two ends of that set, A1 and E1, so both memory controllers are used. Confirm the final 2-DIMM slot pair against the board’s memory support list before ordering; population rules on sTR5 are stricter than on AM5.

### 3.2 Why 128 GB is the right amount now

- The model download is 79 GB; the PLE table alone is 28.8 GB. With 128 GB of VRAM the experts live on the GPUs, but the host still needs the PLE table (28.8 GB with `--ple-io ram`), the OS/page cache, the engine’s RAM arena and headroom for checkpoints. 64 GB is the documented minimum — Strata says IQ3_S fits “with little else open” — but it forces the PLE table back to the SSD and limits the conversation cache; 128 GB is the comfortable floor.
- 2×64 GB keeps four slots free for the 8× path. Four 32 GB DIMMs would give the same 128 GB but consume half the slots and make the eventual 512 GB upgrade a full replacement.
- 2Rx4 is the right rank/organization for these capacities; do not mix 2Rx4 and 2Rx8, and do not mix brands/timings in one channel set.

**One stick or two?** One 64 GB RDIMM will run the GPU-resident IQ3_S workload in low-RAM mode with the PLE on the RAID 0, but it blocks `--ple-io ram` (28.8 GB), the full 16 GB conversation cache and two Saber TP=2 servers, and it leaves ~4 GB of headroom. Two sticks are the practical floor and the specified dual-channel configuration; the second stick is €2,499 and is the first step of the 8×64 GB path. The full capacity/bandwidth math and a one-stick test plan are in [`docs/RAM-START.md`](docs/RAM-START.md).

### 3.3 The DRAM tax

At the snapshot date, the Samsung 64 GB 2Rx4 5600 RDIMM is **€2,499.00** — **€39.05/GB**, and **48% of the entire platform**. This is not a normal market; it is the 2026 DRAM shortage. The consequences:

- The 64 GB module is actually the cheapest per-GB RDIMM in this snapshot (a 4×16 GB kit is €3,346 for 64 GB, €52/GB). Do not “save” by going to small modules.
- A 2×32 GB start would save roughly €2,500 but leave 64 GB of RAM, which is the wrong trade for a 79 GB model with a 28.8 GB PLE table. It is a false economy unless the machine will only ever run IQ3_XXS with the PLE on SSD.
- If you can wait or buy from a reputable used-server supplier, 64 GB DDR5-4800/5600 2Rx4 pulls can cut this line substantially. Verify part number, rank, ECC and return policy; run MemTest86+ before trusting them.

Do not buy 128 GB modules “to fill two slots”. They are far more expensive per GB and the 8×64 GB path is the stated plan.

---

## 4. Storage

### 4.1 The 4×1 TB RAID 0 working set

| Property | Value |
|---|---|
| Drives | 4× Samsung 990 PRO 1 TB, PCIe 4.0 x4, 7,450/6,900 MB/s, 1.2M/1.55M IOPS |
| Array | RAID 0 via `mdadm` (Linux), 128 KiB chunk, 4 TB usable |
| Sequential read | ≈28 GB/s theoretical (4× ~7 GB/s); expect 25–27 GB/s in `fio` |
| 4K random read | ≈4.8M IOPS theoretical (4× 1.2M); expect 3M+ in `fio` |
| Role | `/srv/models`: GGUF shards, PLE table, expert profile, checkpoints, conversation cache spill |
| Redundancy | None. A single drive failure loses the array. |

Why Gen4 rather than Gen5:

- The 990 PRO 1 TB is **€262**; a Gen5 1 TB drive is roughly €350–400 in this market. Four drives save €350–550.
- The M.2 sockets sit **between the x16 slots**, directly under the GPUs. Gen5 drives idle and load hotter; Gen4 drives are easier to keep under the board’s M.2 thermal guards.
- The PLE reads are small random rows, not a sequential stream. The 990 PRO’s 1.2M random-read IOPS is the relevant number; Gen5’s extra sequential bandwidth mostly helps cold starts, which the 4-drive array already handles at ~28 GB/s.

The RAID 0 is a working set, not a backup. Keep a full copy of the model, tokenizer, packs, MTP runtime and configs on the 4 TB SATA drive. A rebuild from that archive is a few minutes at SATA speed; a re-download is not.

### 4.2 The SATA cold store

The Samsung 870 EVO 4 TB is **€665** at the snapshot. Partition it as:

- **256 GB** — Ubuntu 24.04/26.04 LTS, the Strata engine package, logs.
- **~3.6 TB** — model archive, configs, checksums, checkpoints, benchmark results.

A 500 GB 870 EVO is **€203.90** — €0.41/GB versus €0.17/GB for the 4 TB. The 4 TB is the better buy even if you only use a quarter of it. The enterprise Samsung PM893 3.84 TB is **€2,430** at the same snapshot; its endurance is irrelevant for cold model archives and it is not worth the 3.6× premium here.

### 4.3 M.2 thermal reality

The board’s M.2 sockets are under the GPUs. The board ships M.2 Thermal Guard heatsinks, but a 300 W blower card’s backplate radiates into that space. Mitigations, in order:

1. Use the Gen4 990 PRO, not a Gen5 drive.
2. Keep the two bottom 140 mm intake fans (Option B/C) blowing across the M.2 area.
3. Monitor `smartctl -A` temperature sensors during the acceptance run; target <70 °C, investigate above 75 °C.
4. If a drive still throttles, fit a slim 120 mm fan over the M.2 row or move the two hottest drives to the M2D/M2A positions with the most clearance.

Do not put the OS on the RAID 0. A drive failure or an `mdadm` mistake should not take the boot device with it.

---

## 5. Power, cooling, chassis

### 5.1 Power budget

| Load | Continuous |
|---|---:|
| 4× R9700 at 300 W | 1,200 W |
| Threadripper PRO 9955WX at 350 W | 350 W |
| Board, 128 GB RAM, 4 NVMe, 1–2 SATA, fans | 80 W |
| **Total** | **1,630 W** |
| PSU | 2,200 W |
| **Headroom** | **570 W / 25.9%** |

At 94% efficiency the input is ≈1,734 W, or **7.54 A at 230 V**. A 10 A circuit is technically enough but leaves no margin for transients, a monitor, or the next device; use a **16 A circuit** and a C19/C20 cord. The PX-2200 is **200–240 V only** — it is not a 115 V unit.

The GPUs are 12V-2x6 cards, not 8-pin cards. The PSU provides:

- 2× native 12V-2x6 cables,
- 2× 2×8-pin-to-12V-2x6 adapter cables (for GPUs 3 and 4),
- 4× PCIe 8-pin cables (two for the board’s PCIE_12V1/2 aux inputs; the other two are spare or feed PCIE_12V3/4 in a two-PSU setup),
- 3× EPS 8-pin (two for the CPU, one spare),
- 16× SATA.

At 300 W per card, the 2×8-pin adapter path is within its rating: a 2×8-pin cable is nominally 300 W, and the card splits its 300 W between that cable and the slot’s 75 W, so the adapter carries less than its nominal maximum. The 12V-2x6 connector itself is 600 W class. Connect the board aux feeds before the GPUs; the manual’s one-PSU configuration is PCIE_12V1/2, and the 24-pin alone can supply slot power if a cable is unavailable.

**Do not** substitute a 1600 W unit. The be quiet! Dark Power Pro 13 1600 W is an excellent PSU, but 1,630 W continuous is 102% of its rating; it would only be acceptable with all four GPUs power-capped to ~250 W. The 2200 W unit is the correct 24/7 choice.

### 5.2 Cooling and airflow

- **GPU cooling:** four blowers exhaust out the back. The case needs strong front-to-back flow: 3× 140 mm front intake (2 included with the Meshify 2 XL; add one), 1× 140 mm rear exhaust (included), 2× 140 mm bottom intake for the M.2/GPU zone (Option B/C).
- **CPU cooling:** the 9955WX is a 350 W part. The Noctua NH-U14S TR5-SP6 (Option A) is adequate for bursty inference and is the value choice. The SilverStone XE360-TR5 (Option B/C) is the right choice for sustained all-core work and for keeping CPU heat out of the GPU intake; mount it in the top as exhaust.
- **Positive pressure:** more intake than exhaust, with filters, keeps the M.2 row and the GPU intakes cleaner. Clean the front filter monthly in a 24/7 machine.
- **Heat load:** 1,630 W is **5,562 BTU/h**. This is a space heater. Put it in a room with active cooling or a utility space; do not tuck it under a desk.
- **Noise:** four 300 W blowers at load plus a 360 AIO and a 2.2 kW PSU will land around 45–50 dBA at 1 m. If that matters, the next step is a rack/utility room, not a different cooler.

### 5.3 Chassis comparison

| Case | Slots | Board support | PSU max | GPU max | Radiator | Price | Verdict |
|---|---:|---|---:|---:|---|---:|---|
| **Fractal Meshify 2 XL** | 9+3 | E-ATX, SSI-EEB | 250 mm | 549 mm (open) / 359 mm (storage) | 480 top/front | €209.90 | **Recommended.** Four 2-slot cards, 360 AIO, 6× 3.5" + 2× 2.5", 3 fans included. |
| Corsair 9000D Airflow | 8 | E-ATX, SSI-EEB | 225 mm | 400 mm | 4× 480 | €469.90 | Option C. More service room, exactly 8 slots, 5× 3.5" + 6× 2.5". |
| Phanteks Enthoo Pro 2 | 8 | E-ATX | check | check | check | €154.90 | Budget alternate; verify 305×330 mm board and 210 mm PSU clearance before ordering. |

The Meshify 2 XL’s 9th slot is not cosmetic: four 2-slot cards consume eight bracket positions, and the extra slot gives cable/air clearance. The 9000D’s 8 slots fit exactly, with less margin.

### 5.4 UPS and circuit

A 2,200 VA / 1,600–1,800 W pure-sine UPS is the right class for this machine (e.g., APC Smart-UPS 2200 VA class). It is not in the BOM because it is site-specific, but a 24/7 inference server with a 4 TB RAID 0 working set should have one: the RAID 0 has no redundancy, and an unclean shutdown during a checkpoint write is the most likely way to lose the array. Budget €500–900.

---

## 6. Will it serve the model? VRAM, KV and streams

### 6.1 The model fits with room

| Item | IQ3_S | IQ3_XXS |
|---|---:|---:|
| Download | 79 GB | 76 GB |
| Experts (VRAM/arena) | ≈50 GB | ≈43 GB |
| Dense weights | 1.5 GB on disk; ≈3.5 GiB in VRAM per card | same |
| PLE table | 28.8 GB (SSD/RAM) | 28.8 GB (SSD/RAM) |
| Quality | Better | Slightly lower |
| Verdict | **Fits 128 GB VRAM with 8×262K streams** | Fits with more headroom; use if you want 12+ streams or lower power |

### 6.2 Per-card budget (first-order)

Strata’s layer split puts a contiguous range of layers on each card. Every card holds a copy of the dense weights, its share of the expert cache, its session state and prompt buffers; the last card also holds the output head and the MTP draft layer.

| Item per card | Helper | Main |
|---|---:|---:|
| Experts share (50 GB / 4) | 12.50 GB | 12.50 GB |
| Dense copy (VRAM) | 3.50 GB | 3.50 GB |
| Prompt/session buffers | 2.00 GB | 2.00 GB |
| Head + MTP draft | — | 0.80 GB |
| GPU vision reader | — | 1.47 GB |
| **Used** | **18.00 GB** | **20.27 GB** |
| **Free of 32 GB** | **14.00 GB** | **11.73 GB** |

This is a budgeting model, not an engine measurement: the actual split depends on the layer assignment, the expert cache policy and the prompt path. The dense copy is the docs’ **3.5 GiB per card for IQ3_S**, not the 1.5 GB on-disk file: the engine dequantizes the dense weights into VRAM. The model is deliberately conservative on buffers and includes the GPU vision reader on the main card.

### 6.3 Full-context streams

Each stream needs its own KV. At 262,144 tokens:

| KV format | KB/token | GB per 262K stream | 8 streams total | Per card at 8 |
|---|---:|---:|---:|---:|
| int8 | 13.7 | 3.42 | 27.4 GB | 6.85 GB |
| **k8v4** | **10.55** | **2.64** | **21.1 GB** | **5.28 GB** |

With `k8v4` and the per-card budget above:

| Streams at 262K | KV total | KV per card | Main free after KV | Verdict |
|---:|---:|---:|---:|---|
| 4 | 10.6 GB | 2.6 GB | 9.1 GB | Trivial |
| **8** | **21.1 GB** | **5.3 GB** | **6.5 GB** | **Recommended starting point** |
| 12 | 31.7 GB | 7.9 GB | 3.8 GB | Test target; watch fragmentation |
| 16 | 42.2 GB | 10.6 GB | 1.2 GB | Too tight for the conservative budget |

The engine also supports KV streaming from host RAM (`--kv-streaming`, with `--kv-resident` setting the VRAM window), but with 128 GB of VRAM there is no reason to stream: `--kv-resident 0` keeps all KV in VRAM (it is the sentinel for “fully resident”, not “zero cells”). Use the 128 GB of RAM for the PLE table, the expert arena and conversation checkpoints.

**Recommended starting configuration:** `--batch 8`, `--max-context 262144`, `--kv k8v4`, `--kv-resident 0` (all KV in VRAM). Test `--batch 12` at 262K and `--batch 16–24` at 131K/65K; keep the setting that survives a 24-hour soak without VRAM growth or dropped streams.

### 6.4 Measured anchors and the projection

These are measured numbers from the Strata documentation, not this machine:

| Configuration | Decode | Prefill | Source |
|---|---:|---:|---|
| 1× R9700, IQ3_S, 27K prompt | 94.7 tok/s | 2,411 tok/s (KVA off) | Strata KVA doc |
| 2× R9700, code, pipeline window | 125 tok/s | — | Strata multi-GPU doc |
| 3 / 4× R9700, same table | +19% / +22% | — | Strata multi-GPU doc |
| 4× RX 7900 XT (older, 24 GB), IQ3_S, 262K | 67.6 tok/s @4K; 65.6 @32K | — | Strata multi-GPU doc |
| 4× R9700, DeepSeek V4.1 2.00 bpw (much larger model) | 74–77 tok/s | 400–450 tok/s @8K | Strata README |

**Projection for this build:** ≈150 tok/s single-stream decode (125 tok/s at two cards, +22% at four, and no CPU expert fallback because the four-card cache can hold the whole expert set instead of streaming it as a 32 GB card must), and 3,000+ tok/s prefill at 32K. The projection is plausible but unverified. The acceptance run in [`docs/VALIDATION.md`](docs/VALIDATION.md) replaces it with real numbers before the machine is accepted.

At eight concurrent 262K streams, per-stream decode will be lower than the single-stream number; the aggregate is the number that matters for serving. Plan for 300–500 tok/s aggregate as a target band and measure. Do not quote the single-stream projection as a concurrent-stream guarantee.

---

## 7. The three builds

All three share the same board, CPU, PSU and 4 TB RAID 0. They differ in cooling, chassis, RAM population and cold-archive redundancy: one 4 TB SATA in A/B, two in C.

### Option A — Lean

*Lowest cost per token; air cooling; one 4 TB SATA.*

| Item | Qty | Unit | Line |
|---|---:|---:|---:|
| Gigabyte TRX50 AI TOP | 1 | €896.75 | €896.75 |
| Threadripper PRO 9955WX | 1 | €1,637.70 | €1,637.70 |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | 2 | €2,499.00 | €4,998.00 |
| Samsung 990 PRO 1 TB | 4 | €262.00 | €1,048.00 |
| Samsung 870 EVO 4 TB SATA | 1 | €665.00 | €665.00 |
| Seasonic PRIME PX-2200 | 1 | €489.90 | €489.90 |
| Noctua NH-U14S TR5-SP6 | 1 | €129.90 | €129.90 |
| Fractal Meshify 2 XL | 1 | €209.90 | €209.90 |
| 140 mm fan (estimate) | 1 | €15.00 | €15.00 |
| **Platform subtotal** | | | **€10,090.15** |
| Contingency 3% | | | €302.70 |
| **Platform total** | | | **€10,392.85** |
| GPUs (owned, replacement value) | 4 | €1,930.21 | €7,720.84 |
| **Total if buying GPUs** | | | **€18,113.69** |

**Buy this if:** the machine runs in a cool room, the CPU load is bursty, and €300 matters more than 24/7 thermal margin.

### Option B — Recommended

*24/7 thermal headroom; 360 AIO; same compute.*

| Item | Qty | Unit | Line |
|---|---:|---:|---:|
| Gigabyte TRX50 AI TOP | 1 | €896.75 | €896.75 |
| Threadripper PRO 9955WX | 1 | €1,637.70 | €1,637.70 |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | 2 | €2,499.00 | €4,998.00 |
| Samsung 990 PRO 1 TB | 4 | €262.00 | €1,048.00 |
| Samsung 870 EVO 4 TB SATA | 1 | €665.00 | €665.00 |
| Seasonic PRIME PX-2200 | 1 | €489.90 | €489.90 |
| SilverStone XE360-TR5 | 1 | €389.90 | €389.90 |
| Fractal Meshify 2 XL | 1 | €209.90 | €209.90 |
| 140 mm fans (estimate) | 3 | €15.00 | €45.00 |
| **Platform subtotal** | | | **€10,380.15** |
| Contingency 3% | | | €311.40 |
| **Platform total** | | | **€10,691.55** |
| GPUs (owned, replacement value) | 4 | €1,930.21 | €7,720.84 |
| **Total if buying GPUs** | | | **€18,412.39** |

**Why it wins:** €290 of parts over Option A (€299 with contingency) buys a 360 mm AIO (the 350 W CPU and four GPUs in one box are not an air-cooler showcase), two extra bottom fans for the M.2 row, and a cooler that exhausts CPU heat out of the top instead of into the GPU intake. That is the cheapest reliability upgrade in the BOM. It is the recommended middle.

### Option C — Expand

*4×64 GB now (quad-channel, 8× path), bigger case, RAID 1 cold archive.*

| Item | Qty | Unit | Line |
|---|---:|---:|---:|
| Gigabyte TRX50 AI TOP | 1 | €896.75 | €896.75 |
| Threadripper PRO 9955WX | 1 | €1,637.70 | €1,637.70 |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | 4 | €2,499.00 | €9,996.00 |
| Samsung 990 PRO 1 TB | 4 | €262.00 | €1,048.00 |
| Samsung 870 EVO 4 TB SATA | 2 | €665.00 | €1,330.00 |
| Seasonic PRIME PX-2200 | 1 | €489.90 | €489.90 |
| SilverStone XE360-TR5 | 1 | €389.90 | €389.90 |
| Corsair 9000D Airflow | 1 | €469.90 | €469.90 |
| 140 mm fans (estimate) | 5 | €15.00 | €75.00 |
| **Platform subtotal** | | | **€16,333.15** |
| Contingency 3% | | | €489.99 |
| **Platform total** | | | **€16,823.14** |
| GPUs (owned, replacement value) | 4 | €1,930.21 | €7,720.84 |
| **Total if buying GPUs** | | | **€24,543.98** |

**Buy this if:** you already know you will run models that need more than 128 GB of host RAM, or you want to reach 512 GB in one more step (four more 64 GB modules) rather than two. The +€5,953 over Option B is **€4,998 of RAM** plus €260 for the bigger case, €665 for the second 4 TB SSD and €30 for fans. It is not faster for the IQ3_S workload described here — it is more expandable.

### What not to buy

- **A 24-core 9965WX (+€1,378).** Strata’s CPU pool is not the bottleneck when every expert is in VRAM; 16 cores/32 threads at 5.4 GHz is the sweet spot.
- **Gen5 1 TB NVMe (+€350–550).** Hotter under the GPUs, no meaningful gain for random PLE reads; the 4-drive Gen4 array already exceeds the model’s cold-start needs.
- **A 1600 W PSU.** 1,630 W continuous is over its rating; it only works with GPUs capped to ~250 W.
- **128 GB or 256 GB RDIMMs.** Far worse €/GB than 4× or 8× 64 GB; the board’s 2 TB ceiling (8× 256 GB) is not a target.
- **A second GPU vendor or mixed CUDA/AMD cards.** Strata’s engine drives one make at a time; a mixed box is a support problem, not a performance feature.
- **A water block on each GPU.** The blowers are the point: four 2-slot cards, no external radiator, no leak risk over a 24/7 server.

---

## 8. Cost/benefit

### 8.1 Unit economics

| Metric | Option A | Option B | Option C |
|---|---:|---:|---:|
| Platform total (with 3%) | €10,392.85 | €10,691.55 | €16,823.14 |
| With GPUs at replacement | €18,113.69 | €18,412.39 | €24,543.98 |
| Per VRAM GB (platform) | €81.19 | €83.53 | €131.43 |
| Per 262K stream at 8 streams (platform) | €1,299.11 | €1,336.44 | €2,102.89 |
| Energy at 100% load, €0.25/kWh (wall) | €3,797.55/yr | €3,797.55/yr | €3,797.55/yr |
| Energy at 50% average (wall) | €1,888.73/yr | €1,888.73/yr | €1,888.73/yr |

The compute cost is fixed by the four GPUs; the platform is the “socket” that lets them run at full context. At 8×262K streams, Option B costs about **€1,336 per resident full-context stream** — the number to compare against API tokens or a second machine.

### 8.2 The DRAM anomaly

Remove the RAM line and Option B is **€5,382.15** before contingency (**€5,693.55** with it). The 2×64 GB kit is **€4,998**, or 48% of the build. If DRAM prices normalize to their pre-2025 level (roughly €300–400 per 64 GB RDIMM), the same platform is a ~€6,000 build. That is the single biggest timing risk in this book: if the machine can wait, waiting on RAM is worth more than waiting on any other part.

### 8.3 Why not 4× RTX 5090?

A 4× RTX 5090 build also gives 128 GB of VRAM, and the GPUs cost less per card at MSRP. But:

- **Power:** 4× 575 W = 2,300 W of GPU alone, before a 350 W CPU. That is a 3 kW+ machine, two PSUs or a 2.5 kW+ unit, a 16 A circuit at the edge, and a much louder case.
- **Form factor:** most 5090s are 3–3.5-slot axial cards; four do not fit in a 7–9 slot tower without risers and open-air frames. The R9700’s 2-slot blower is the reason this build is a normal tower.
- **Software:** the workload is Strata on HIP; the R9700 is the maintainer-tested AMD path. A 5090 build would use the CUDA path (also supported), but it would be a different machine with different power/cooling economics.
- **Cost:** at the snapshot, four R9700s are €7,720.84; four 5090s at current street prices are not cheaper enough to offset the PSU/case/cooling delta. The R9700 wins the cost/performance/watt triangle for a dense 4-GPU server.

### 8.4 Total cost of ownership

At 50% average load, the machine draws ~862 W at the wall (~7,550 kWh/year, €1,889 at €0.25/kWh). Add the platform amortized over three years (€3,564/year for Option B) and the all-in compute cost is roughly €5,450/year before GPUs. That is the number to compare with cloud GPU rental; at 8×262K streams and ~150 tok/s single-stream, it is a strong local-serving case.

---

## 9. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| HIP multi-GPU layer split is less mature than CUDA | Medium | Performance/stability | Acceptance run with 8×262K streams and a 24 h soak; keep the CUDA path as a fallback only if you add NVIDIA cards (not planned). |
| Engine-choice drift: Saber is faster on 2 cards but TP=2 only | Medium | Wrong build for 4 GPUs | Keep Strata for the 4-GPU objective; if you test Saber, test it on a pair, not as a 4-GPU replacement. See [`docs/SABER.md`](docs/SABER.md). |
| M.2 drives throttle under the GPUs | Medium | Model/PLE read slowdown | Gen4 drives, board heatsinks, bottom intake, SMART monitoring, 70 °C target. |
| RAID 0 loses a drive | Low–Medium | Working set lost | Full model/config archive on the 4 TB SATA; checksum manifest; UPS; rebuild procedure documented. |
| 2-channel RAM now limits CPU-side work | Medium | Slower CPU expert fallback/PLE | All experts fit VRAM; 8× path documented; move to 4 or 8 DIMMs if you later run bigger models. |
| PSU is 200–240 V only | Certain | No 115 V operation | EU site; 16 A circuit; C19/C20 cord; label the inlet. |
| 9955WX stock is thin | Medium | Delay | Geizhals listed EU offers at the snapshot, but Alternate could not take orders; 9965WX is in stock at +€1,378 if you cannot wait (but it is not faster here). |
| Board needs a BIOS update for 9000WX | Medium | No boot | Q-Flash Plus with a USB stick before installing the CPU; update to the latest BIOS. |
| RDIMM QVL mismatch | Low | No boot/instability | Buy the exact Samsung part; check the board QVL; MemTest86+ 8 passes; ECC error count zero. |
| 12V-2x6 connector heating | Low | Shutdown/damage | Fully seat; use native cables/adapters; IR-check connector temperature under load; no daisy-chaining beyond the included adapters. |
| Noise/heat in a living space | High | Comfort | Utility room/rack; 5,562 BTU/h; 45–50 dBA at load. |

---

## 10. Build order and BIOS

### 10.1 Before assembly

1. Flash the latest BIOS with Q-Flash Plus (USB, no CPU/RAM needed). The board supports 9000WX, but early BIOSes may not.
2. Check the board’s memory QVL for the exact Samsung M321R8GA0PB0-CWM part.
3. Verify all four GPUs are 2-slot blowers (40 mm thick), not 2.5/3-slot axial cards.
4. Dry-fit the AIO radiator in the top of the Meshify 2 XL and confirm the 210 mm PSU clears the bottom cage.

### 10.2 Assembly order

1. CPU into sTR5 (drop-in, torque in the order printed on the socket frame).
2. 2× 64 GB RDIMMs in A1 + E1.
3. 4× 990 PRO in M2C/M2B/M2A/M2D; remove the thermal-pad protective films before mounting the drives.
4. Board into the case; standoffs for SSI-EEB.
5. 360 AIO top-mounted, pump/fan headers to CPU_FAN/CPU_OPT.
6. PSU, 24-pin, 2× EPS, 2× PCIe 8-pin to PCIE_12V1/2.
7. GPUs in PCIEX16_1…4, from the top; connect 12V-2x6 feeds (2 native + 2 adapters).
8. SATA SSD to SATA3_0; power.
9. Front/bottom/rear fans; fan curves.
10. First boot with one GPU? No — the board’s slots are wired for four; install all four, but power up with the GPUs idle and check `lspci` link width before loading the model.

### 10.3 BIOS settings

- **Above 4G Decoding:** Enabled.
- **Re-Size BAR Support:** Enabled (if offered).
- **CSM:** Disabled (UEFI only).
- **IOMMU:** Enabled (useful for diagnostics; not required for Strata).
- **PCIe slots:** Auto/Gen5; verify x16 on all four in `lspci -vv`.
- **Memory:** EXPO/XMP off; JEDEC 5600; ECC auto. Confirm ECC is enabled in the BIOS event log/OS.
- **Fan curves:** front/bottom intake responsive to GPU temp; AIO pump full speed; rear exhaust moderate.
- **Power:** set the platform to “typical current” or balanced; do not enable extreme OC profiles on a 24/7 server.

### 10.4 OS and engine

- **OS:** Ubuntu 24.04 LTS with the HWE kernel (6.14+) or Ubuntu 26.04 LTS. RDNA4 (`gfx1201`) and Zen 5 need a current kernel; the HWE stack covers both. Use a server install, no desktop.
- **Driver:** the kernel `amdgpu` driver; no system ROCm install is required for the Strata `rx9070` Linux package, which carries its own ROCm 7.10 runtime.
- **Strata:** install the `rx9070` Linux package (gfx1200/gfx1201) or build from source with `-DSTRATA_ENABLE_HIP=ON -DCMAKE_HIP_ARCHITECTURES=gfx1201`. The engine’s `strata-device --list-devices` must show all four R9700s before the model starts.
- **Model:** place the 79 GB IQ3_S shards, pack, tokenizer and MTP runtime on `/srv/models` (the RAID 0). Put the PLE table on the same array; `--ple-io ram` will cache it in the 128 GB of RAM.
- **Config:** start from [`configs/strata-4x-r9700-8x262k.json`](configs/strata-4x-r9700-8x262k.json), adjust the paths, and run the acceptance tests.

---

## 11. Acceptance tests

The full protocol is in [`docs/VALIDATION.md`](docs/VALIDATION.md). The short version:

1. **Memory:** MemTest86+ 8 passes, ECC error count zero.
2. **Storage:** `fio` sequential and 4K random on `/dev/md0`; SMART temperatures under load.
3. **Power:** wall meter at idle, 4-GPU load, CPU+GPU combined; <2,000 W; 12V-2x6 connector temperature <60 °C.
4. **Thermals:** GPU edge/hotspot, CPU package, M.2, VRM; 30 min steady; no throttle.
5. **PCIe:** `lspci -vv` shows 32 GT/s x16 on all four GPUs; no AER errors.
6. **Strata:** 1 stream at 262K, then 8 streams at 262K; record decode, prefill, TTFT, VRAM per card, wall power.
7. **Soak:** 24 h with 8 streams and periodic 64K cold prompts; no drops, no VRAM growth, no ECC errors.

**Acceptance gates:** 8×262K streams stable; ≥250 tok/s aggregate decode at 8 streams (target 300–500, no stream below 25 tok/s); ≥2,500 tok/s prefill at 32K; <2,000 W wall; zero ECC/AER errors; no M.2 above 75 °C.

---

## 12. Sources and price snapshot

All prices are from 2026-11-06 and include VAT. The exact line items, sources and notes are in [`bom/prices.json`](bom/prices.json); the BOM CSVs are in [`bom/`](bom/).

| Item | Price | Source |
|---|---:|---|
| Gigabyte TRX50 AI TOP | €896.75 | [Geizhals EU](https://geizhals.eu/gigabyte-trx50-ai-top-a3246131.html) |
| Threadripper PRO 9955WX | €1,637.70 | [Geizhals DE](https://geizhals.de/amd-ryzen-threadripper-pro-9955wx-100-100000725wof-a3531872.html) |
| Samsung 64 GB DDR5-5600 2Rx4 ECC RDIMM | €2,499.00 | [Geizhals EU](https://geizhals.eu/samsung-rdimm-64gb-m321r8ga0pb0-cwm-a3528359.html) |
| Samsung 990 PRO 1 TB | €262.00 | [Alternate DE](https://www.alternate.de/Samsung/990-PRO-1-TB-SSD/html/product/1864239) |
| Samsung 870 EVO 4 TB | €665.00 | [Alternate DE](https://www.alternate.de/Samsung/870-EVO-4-TB-SSD/html/product/1706407) |
| Seasonic PRIME PX-2200 | €489.90 | [Alternate DE](https://www.alternate.de/Seasonic/PRIME-PX-2200-2200W-ATX-3-1-PC-Netzteil/html/product/100076188) |
| SilverStone XE360-TR5 | €389.90 | [Alternate DE](https://www.alternate.de/SilverStone/SST-XE360-TR5-Wasserk%C3%BChlung/html/product/100114775) |
| Noctua NH-U14S TR5-SP6 | €129.90 | [Alternate DE](https://www.alternate.de/Noctua/NH-U14S-TR5-SP6-CPU-K%C3%BChler/html/product/100020811) |
| Fractal Meshify 2 XL | €209.90 | [Alternate DE](https://www.alternate.de/Fractal-Design/Meshify-2-XL-Black-TG-Light-Tint-Big-Tower-Geh%C3%A4use/html/product/1669747) |
| Corsair 9000D Airflow | €469.90 | [Alternate DE](https://www.alternate.de/Corsair/iCUE-LINK-9000D-Airflow-Big-Tower-Geh%C3%A4use/html/product/100064495) |
| PowerColor R9700 32 GB (reference) | €1,930.21 | [Geizhals EU](https://geizhals.eu/powercolor-radeon-ai-pro-r9700-a3504726.html) |

**Primary technical sources:** [Gigabyte TRX50 AI TOP manual (PDF)](https://download.gigabyte.com/FileList/Manual/mb_manual_trx50-ai-top_107_e.pdf), [AMD Ryzen Threadripper PRO 9955WX](https://www.amd.com/en/products/processors/workstations/ryzen-threadripper/9000-wx-series/amd-ryzen-threadripper-pro-9955wx.html), [Seasonic PRIME PX-2200 datasheet (PDF)](https://seasonic.com/wp-content/uploads/2024/06/ATX-3.1-PRIME-PX-2200.pdf), [Fractal Meshify 2 XL product sheet (PDF)](https://assets.fractal-design.com/files/uxzbxy2o/production/1bc60fe11df0e6b0269090a88eec38f36586ff3c.pdf), and the Strata docs in `/root/git/strata/docs/` (`AMD_HIP.md`, `MULTI_GPU.md`, `MODELS.md`, `DETAILS.md`, `BATCHING.md`).

**Price caveat:** the listed “from” price is not a reservation. On the snapshot date, Alternate could not take orders for the TRX50 AI TOP, the 9955WX, the 870 EVO 4 TB or the Meshify 2 XL; Geizhals showed other EU offers for the board, CPU and RAM. Re-check every listed offer before placing orders; the 3% contingency is there for exactly this.

---

## Appendix A — Files in this build book

| File | Purpose |
|---|---|
| [`report.html`](report.html) | One-page visual summary: options, cost composition, power/lanes/VRAM, stream table. |
| [`bom/prices.json`](bom/prices.json) | Machine-readable price snapshot, options and assumptions. |
| [`bom/option-a.csv`](bom/option-a.csv) | Lean build sheet. |
| [`bom/option-b.csv`](bom/option-b.csv) | Recommended build sheet. |
| [`bom/option-c.csv`](bom/option-c.csv) | Expand build sheet. |
| [`tools/calc.py`](tools/calc.py) | Totals, power, lanes, memory topology, VRAM/KV/stream model. |
| [`tools/export_bom.py`](tools/export_bom.py) | Regenerates the CSV build sheets from `prices.json`. |
| [`configs/strata-4x-r9700-8x262k.json`](configs/strata-4x-r9700-8x262k.json) | Starting Strata launch config for 4 GPUs, 262K, 8 slots. |
| [`configs/strata-4x-r9700-16x131k.json`](configs/strata-4x-r9700-16x131k.json) | Throughput preset, 131K, 16 slots. |
| [`configs/README.md`](configs/README.md) | Flag-by-flag notes and tuning levers. |
| [`docs/SABER.md`](docs/SABER.md) | Evaluation of the Saber engine: TP=2 limit, MXFP4 packs, 95.4 GiB PLE, fit against this build. |
| [`docs/SABER-4X.md`](docs/SABER-4X.md) | Code-level answer to “expand the 2× config to 4×”: why Flash-Next cannot be dense-TP=4, the three 4-GPU paths, and the BOM impact. |
| [`docs/RAM-START.md`](docs/RAM-START.md) | 1×64 GB vs 2×64 GB at the start: capacity, bandwidth, PLE/cache impact, upgrade path and a one-stick test plan. |
| [`patches/`](patches/) | Upstream Saber docs/RFC patch (against `cebec82`), apply/submit instructions and PR body. |
| [`docs/VALIDATION.md`](docs/VALIDATION.md) | Acceptance and benchmark protocol. |
| [`docs/SOURCES.md`](docs/SOURCES.md) | Source links and what each one verifies. |
