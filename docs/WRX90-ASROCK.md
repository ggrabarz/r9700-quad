# WRX90 board options vs the Gigabyte TRX50 AI TOP — and what it means for SSD weight streaming

**Short answer:** there are now three relevant boards, and no single one wins every column.

- **ASRock WRX90 WS EVO** — WRX90, IPMI, 7 slots, 6 NVMe ports, **available at €808.05**. The three Gen5 ports (1 Gen5 M.2 + 2 Gen5 MCIO) make a clean **3× Gen5** array; a 4-drive array is 3 Gen5 + 1 Gen4; the same six ports can run **6× Gen4**.
- **Gigabyte WRX90 AI TOP** — WRX90, IPMI, 7 slots, 2 Gen5 M.2 + 1 Gen4 M.2 + 2 MCIO. **Announced 2026-10-30, no price or retail offers at the snapshot.** The 4-drive RAID 0 is also 3 Gen5 + 1 Gen4, because MCIOX8_1 shares bandwidth with the two Gen5 M.2 slots.
- **Gigabyte TRX50 AI TOP** — TRX50, **no IPMI**, 4 slots, but **4 Gen5 M.2**; €896.75. The only one of the three that runs four Gen5 drives in RAID 0 without a carrier.

So: if you need **WRX90 + IPMI now**, the ASRock is the board — 3× Gen5 for the balanced build, 6× Gen4 for capacity. If you want the **Gigabyte AI TOP ecosystem with WRX90 + IPMI** and can wait, the WRX90 AI TOP is the natural choice — but it does not restore the four Gen5 M.2 sockets. If **four Gen5 M.2 drives** are the priority, the TRX50 AI TOP remains the one.

## 1. Board comparison

| Capability | ASRock WRX90 WS EVO | Gigabyte WRX90 AI TOP | Gigabyte TRX50 AI TOP |
|---|---|---|---|
| Chipset | AMD WRX90 | **AMD WRX90** | AMD TRX50 |
| CPU | TR PRO 9000/7000 WX | TR PRO 9000/7000 WX | TR PRO 9000/7000 WX (and TR 9000/7000) |
| Memory | 8× RDIMM, 8ch, 2 TB, 7600+ OC | 8× RDIMM, 8ch, 2 TB | 8× RDIMM, 8ch with PRO, 2 TB |
| PCIe x16 | 7 (6× x16 + 1× x8) | **7 (6× x16 + 1× x8)** | 4× x16 |
| Gen5 M.2 | 1 | **2** | **4** |
| Gen4 M.2 | 1 | 1 | — |
| Other NVMe | 2× MCIO Gen5 x4 + 2× SlimSAS Gen4 x4 | 2× MCIO 8i (MCIOX8_1 shares with M2A/M2B) | — |
| SATA | 4 | 4 | 4 |
| LAN | 2× 10GbE + IPMI | 2× Intel X710 10GbE + **BMC/IPMI LAN** | 2× 10GbE, no BMC |
| BMC | AST2600 | **AST2600** | none |
| VRM | 18+3+3, 110 A | **32+3+3+3**, 14-layer PCB, memory fans | 16+8+4 |
| Power | 2× 8-pin ATX12V, 2× 6-pin PCIe, 2× 6-pin GFX | 2× 8-pin ATX12V, 4× PCIe | 2× 8-pin ATX12V, 4× 8-pin PCIe |
| Form | EEB 305×330 | E-ATX 305×330 | E-ATX 305×330 |
| Price | **€808.05** (59 offers) | **TBD — no offers** | €896.75 (48 offers) |
| 4-drive RAID 0 | 3 Gen5 + 1 Gen4 | 3 Gen5 + 1 Gen4 | **4 Gen5** |
| Availability | now | announced 2026-10-30 | now |

The ASRock is the **available** WRX90/IPMI value; the WRX90 AI TOP is the **Gigabyte-native** WRX90/IPMI board but is not yet priced or on a shelf; the TRX50 AI TOP is the **four-Gen5-M.2** board without IPMI.

**Today’s pick: ASRock WRX90 WS EVO.** With the build’s current **Gen4** 990 PRO drives, its 4-drive RAID 0 is **4 Gen4** — exactly what the TRX50 AI TOP gives with the same drives. The TRX50’s four Gen5 M.2 sockets are latent until you buy Gen5 drives. For roughly the same money after two MCIO cables, the ASRock adds **IPMI, native WRX90/8-DIMM validation, six NVMe ports and active VRM cooling**. Choose the TRX50 AI TOP only if four Gen5 M.2 drives are a hard requirement (or the Gigabyte AI TOP brand is); choose the WRX90 AI TOP if Gigabyte + WRX90 + IPMI is the hard requirement and you can wait for stock/pricing.

**Platform nuance:** the TRX50 AI TOP is **not a standard TRX50 board**. Standard TRX50 is 4-channel UDIMM with a non-Pro Threadripper and 80 PCIe 5.0 lanes. The AI TOP is a hybrid: its manual supports **PRO 9000-WX/7000-WX + DDR5 RDIMM (RDIMM/RDIMM-3DS), 8 DIMM slots, 8-channel, 2 TB**, and exposes the PRO’s 128 lanes to the four x16 slots and four M.2 sockets. With a non-Pro TR 9000/7000 it drops to 4 channels, four active DIMM slots, PCIEX16_4 at Gen4 and M2D disabled. That hybrid behavior is why the 9955WX + 2×64 GB RDIMM works on it; the WRX90 boards are the standard PRO/RDIMM platform.

## 2. The slot reality with four 2-slot R9700s

Both WRX90 boards have seven x16 slots on a **1-slot pitch**. Four 2-slot cards go in PCIE1, 3, 5 and 7; slots 2, 4 and 6 are covered by the cards. The fourth card’s second bracket lands in the case’s 8th slot. So:

- Four R9700s fit, but there is **no free slot** for a 4× M.2 carrier or a NIC/HBA on either WRX90 board.
- The extra x16 slots are useful for seven single-slot cards, or three dual-slot GPUs plus a single-slot card — not for four dual-slot GPUs plus an add-in.
- The onboard MCIO/SlimSAS and dual 10GbE/IPMI are what make the WRX90 boards more capable without a free slot.

The TRX50 AI TOP’s four x16 slots are **2-slot spaced**, so the same four cards consume eight bracket positions with no slot-sharing; its four Gen5 M.2 sockets are the storage path.

## 3. The 4×1 TB RAID 0 on each board

| Board | 4-drive topology | Gen5 drives | Verdict |
|---|---|---:|---|
| Gigabyte TRX50 AI TOP | 4× onboard Gen5 M.2 | **4** | Plug-and-play, all Gen5, but the M.2 sit under the GPUs; no IPMI. |
| ASRock WRX90 WS EVO | 1× Gen5 M.2 + 2× Gen5 MCIO + 1× Gen4 M.2 | **3** | 3 Gen5 + 1 Gen4; MCIO cables/drives needed; the fourth drive is the slow link. |
| Gigabyte WRX90 AI TOP | 2× Gen5 M.2 + 1× Gen4 M.2 + 1× Gen5 MCIO (MCIOX8_2) | **3** | 3 Gen5 + 1 Gen4; MCIOX8_1 is disabled when either Gen5 M.2 is populated; IPMI. |
| Any WRX90 + 4× M.2 carrier | Carrier in a free x16 slot | 4 | **No free slot** with four 2-slot GPUs; needs a riser/3-GPU layout. |

If you want four Gen5 drives in RAID 0, the TRX50 AI TOP is the simpler board. If you want **more than four NVMe drives** (a giant-model library), the ASRock’s six ports and the Gigabyte WRX90 AI TOP’s MCIO are the advantage, and the MCIO/SlimSAS drives can live in the case’s 2.5" bays away from the GPU heat.

The ASRock’s 4-drive array at 3 Gen5 + 1 Gen4 is not a disaster: RAID 0 sums sequential bandwidth and random IOPS, so the array is still fast; the Gen4 member simply contributes less. The 4 TB capacity is unchanged.

**If you settle on three Gen5 drives:** the ASRock (and the WRX90 AI TOP) become a clean **all-Gen5** array — 1 Gen5 M.2 + 2 Gen5 MCIO on the ASRock, 2 Gen5 M.2 + MCIOX8_2 on the WRX90 AI TOP. The Gen4 M.2 is then free for the OS/scratch or a fourth Gen4 drive, and there is no Gen4 member dragging the RAID 0 down. What you give up versus four identical Gen5 drives:

| | 3× Gen5 1 TB | 4× Gen5 1 TB | 4× Gen4 1 TB |
|---|---:|---:|---:|
| Capacity | 3 TB | 4 TB | 4 TB |
| Sequential read (approx.) | 42–44 GB/s | 56–59 GB/s | 28–30 GB/s |
| 4K random IOPS (approx.) | ~5.6M | ~7.4M | ~4.8M |
| All-Gen5 array | **yes** | yes | no |
| Full image on the 4 TB SATA (3.6 TB usable) | **yes (3 TB)** | no (4 TB) | no (4 TB) |
| Relative cost (1 TB drives) | ~€1,050–1,200 + OS drive + 2 MCIO cables | ~€1,400–1,600 | €1,048 |

- Versus **4× Gen5**: you lose **1 TB** and roughly **25%** of sequential and random throughput. You keep an all-Gen5 array and add the 4 TB SATA full-image option.
- Versus **4× Gen4**: you lose **1 TB**, but you gain roughly **50% sequential** and **~16% random IOPS**; with the 9100 PRO at €264, the 3× Gen5 array (€792 + two MCIO cables) is actually **cheaper** than 4× 990 PRO (€1,048 + two cables). The Gen4 array is the 4 TB capacity option, not the value option.
- For the stated workload, **3 TB is ample**: Strata IQ3_S 79 GB + Saber Flash-Next ~335 GB + a 191 GB and a 508 GB giant model ≈ 1.1 TB, leaving ~1.9 TB. The 4 TB SATA can hold a full image of the 3 TB array (3.6 TB usable), which a 4 TB array cannot.
- RAID 0 has no redundancy either way; three drives have a lower failure probability than four, and the 3 TB image fits the SATA. The 3 TB array is the better operational compromise if you want all-Gen5 without a carrier.

So: **3× Gen5 is the clean all-Gen5 compromise** — 1 TB and 25% throughput less than 4× Gen5, but faster than 4× Gen4 and imageable on the 4 TB SATA. If capacity is the priority, 4× Gen4; if maximum array speed, 4× Gen5 on the TRX50 AI TOP; if all-Gen5 plus IPMI/proper WRX90, 3× Gen5 on the ASRock.

**Six Gen4 drives:** the ASRock is the only one of the three boards that can do this natively — its six NVMe ports (2 M.2 + 2 MCIO + 2 SlimSAS) take six 990 PRO 1 TB drives, all at Gen4. The result is **6 TB, ~44 GB/s sequential, ~7.2M 4K IOPS**, using four adapter cables (2 MCIO-to-M.2, 2 SlimSAS-to-NVMe). The catch is the backup: a 6 TB array does **not** fit on the 4 TB SATA (3.6 TB usable), so add an **8 TB SATA HDD** (~€250) for a full array image; the 4 TB SATA stays the OS/model archive. The six-drive RAID 0 also has a higher failure probability than three or four drives, and no redundancy; the 8 TB image is the mitigation.

| | 3× Gen5 1 TB | **6× Gen4 1 TB** | 4× Gen5 1 TB | 4× Gen4 1 TB |
|---|---:|---:|---:|---:|
| Capacity | 3 TB | **6 TB** | 4 TB | 4 TB |
| Sequential read (approx.) | 42–44 GB/s | **44–45 GB/s** | 56–59 GB/s | 28–30 GB/s |
| 4K random IOPS (approx.) | ~5.6M | **~7.2M** | ~7.4M | ~4.8M |
| Full image on the 4 TB SATA | **yes** | no (needs 8 TB HDD) | no | no |
| Relative cost | ~€0.87k | **~€2.12k** | ~€1.06k | ~€1.13k |
| Board support | ASRock / WRX90 AI TOP | **ASRock only** | TRX50 (4 M.2) | any |

- **6× Gen4 vs 3× Gen5:** double the capacity, similar sequential and about **30% higher random IOPS**, for roughly **+€1,250** including the adapters and 8 TB HDD; the cost per TB is better, but you need the 8 TB archive and accept six drives of failure domain.
- **6× Gen4 vs 4× Gen5:** 2 TB more capacity, about **25% less sequential**, similar random IOPS, and roughly **+€1,060**; the 4× Gen5 is the speed/4 TB option, the 6× Gen4 the capacity/6 TB option.
- **6× Gen4 vs 4× Gen4:** 2 TB more and about **50% more sequential/random**, for roughly **+€990** including the 8 TB archive; the 4× Gen4 remains the cheapest per TB.
- The six Gen4 drives use **all six NVMe ports**; there is no free NVMe for the OS. Put the OS on the 4 TB SATA (or a small SATA SSD), and the 8 TB HDD on a SATA port for the array image. The Meshify 2 XL’s six 3.5" + two 2.5" bays fit the six cabled M.2 drives, the 4 TB SATA and the 8 TB HDD with M.2-to-2.5" adapters.
- This is the **ASRock-only capacity play**; the TRX50 AI TOP has four M.2 + four SATA (no six NVMe), and the WRX90 AI TOP tops out at five NVMe ports (2 M.2 + 1 Gen4 M.2 + 2 MCIO, with MCIOX8_1 sharing). If a 6 TB working set and six-way striping are the goal, the ASRock is the board.

## 4. Giant-model weight streaming: what the 4× RAID 0 actually buys

The 4×1 TB RAID 0 is useful, but not for the reason the “sequential read” headline suggests.

- **Cold start / model load is sequential.** A 191 GB DeepSeek 2.00 bpw load at ~28 GB/s (4× Gen4 990 PRO) is ~6.8 s; at ~56 GB/s (4× Gen5) it is ~3.4 s; a 508 GB model is ~18 s vs ~9 s. This is the part where 4× RAID 0 sequential shines.
- **Steady-state weight/PLE streaming is random.** The engine reads expert records and PLE rows in small, scattered chunks, not one sequential file. The relevant numbers are **random IOPS and latency**, plus the host RAM/page cache, not the 28–56 GB/s sequential figure. RAID 0 still helps because it stripes those random reads over four drives; four Gen4 990 PROs already give ~4.8M 4K IOPS theoretical, and the engine’s I/O threads/PCIe usually become the limit before the drives do.
- **Capacity is the first constraint for giant models.** 4 TB holds a 191 GB model plus a 508 GB model plus the 79 GB Strata set (≈778 GB), so the array is big enough for the stated experiments. A library of many giant models wants more drives — the ASRock’s six NVMe ports and the WRX90 AI TOP’s MCIO help; the TRX50 AI TOP’s four M.2 + four SATA is more limited (SATA is too slow for steady-state streaming).
- **Host RAM is the bigger constraint.** The 128 GB build can hold the 28.8 GB PLE and a page-cache slice, but a 508 GB model’s CPU lane is ~171.5 GB (per `docs/DECISIONS.md`); the 8×64 GB = 512 GB endgame is what makes that model comfortable. The board choice does not change the DIMM count: both are 8× DDR5, 8-channel, 2 TB.
- **Gen5 vs Gen4.** Gen5 doubles sequential load speed and improves random IOPS, but the drives run hotter. The TRX50 AI TOP’s four Gen5 M.2 sit **under the GPUs**; the WRX90 boards’ MCIO/SlimSAS drives can be placed in the case’s 2.5" bays. For a machine that streams weights for hours, the MCIO thermal placement may matter more than the fourth Gen5 port.

Measured anchors for the giant-model case (Strata docs): 4× R9700, DeepSeek V4.1 2.00 bpw, **74–77 tok/s** decode and 400–450 tok/s prefill at 8K (README table); the app’s four-card DeepSeek number is ~31 tok/s (MULTI_GPU). The 4 TB array is not the bottleneck at those rates; the expert cache hit rate, the host RAM and the CPU/PCIe path are.

### Dense models are different: sequential, but bandwidth-brutal

A dense model has no expert routing: every token needs every layer’s weights. When a dense model is larger than VRAM and the engine offloads layers, the per-token read is **sequential** (layer 0, layer 1, …), so the 4× RAID 0’s sequential bandwidth is more relevant than it is for MoE. But the requirement scales with the **entire offloaded weight set per token**, not a few experts:

| Dense model, 4-bit (approx.) | Weights | Fits 128 GB VRAM? | Streaming? | What limits it |
|---|---:|---|---|---|
| 27B | 14–26 GB | Yes (2 cards) | No | Compute; Saber measures 229 tok/s on 2× R9700. |
| 70B | 35–40 GB | Yes | No | Compute. |
| 120B | 60–70 GB | Yes | No | Compute / KV. |
| 200B | 100–110 GB | Yes, tight with KV | No or a small spill | VRAM capacity. |
| 400B | 200–220 GB | No | Yes, ~100 GB spill | **Bandwidth wall** (below). |

The arithmetic is unforgiving. Required read bandwidth = offloaded bytes × tokens/s:

- 10 GB spill at 10 tok/s = **100 GB/s**; at 20 tok/s = **200 GB/s**.
- 4× Gen4 990 PRO RAID 0 ≈ **28 GB/s**; 4× Gen5 RAID 0 ≈ **56 GB/s**; 8-channel DDR5-5600 ≈ **358 GB/s**.
- So a 10 GB spill on the SSD tops out around **2.8 tok/s** (Gen4) or **5.6 tok/s** (Gen5) before compute; the same spill served from 8-channel RAM is not the bottleneck.
- A 400B dense model at 4-bit (~200 GB) with 100 GB offloaded would need ~1 TB/s at 10 tok/s; no 4-drive array and no 8-channel RAM reaches that. Dense offload only works for a **small spill** or at **low single-digit tok/s**.

This is why the 4 TB RAID 0 is a **cold-start and load** tool for dense models, not a way to run a giant dense model interactively. The dense models that fit 128 GB VRAM — up to roughly 200B at 4-bit, or 70B at 8-bit — do not stream at all. If you need a dense model larger than that, the first lever is **more VRAM or a smaller quant**, the second is **8×64 GB RAM** (358 GB/s) for a partial spill; the SSD is third.

MoE is the opposite trade: only the active experts are read, so the per-token bytes are much smaller and the access pattern is random; that is why a 191 GB DeepSeek 2.00 bpw can run at 74–77 tok/s on four R9700s while a 200 GB dense model cannot stream at interactive speed. The 4× RAID 0 is still the right array for both, but for dense it mainly buys faster loads and checkpoint writes; for MoE it also serves the steady-state expert misses.

## 4.5 What the WRX90 AI TOP buys over the TRX50 AI TOP

The WRX90 chipset does **not** make the GPUs faster: the 9955WX’s CPU-attached PCIe lanes, 8-channel memory and 128-lane budget are the same on both boards. The advantages are operational and structural:

| WRX90 AI TOP advantage | Why it matters | What it costs |
|---|---|---|
| **IPMI / AST2600 BMC** | Remote power, KVM, monitoring and troubleshooting without a GPU/display; the TRX50 AI TOP has no BMC. | No IPMI on the TRX50; OS-level management only. |
| **Proper PRO/RDIMM platform** | Native 8-channel RDIMM, PRO-only; no hybrid fallback or “non-Pro loses slots/Gen5” caveats. | The TRX50 AI TOP is a hybrid that works with the 9955WX, but it is not the standard platform. |
| **32+3+3+3 VRM, 14-layer PCB, active DDR cooling** | More margin for a 350 W PRO (and a future 96-core), and the DDR Wind Blade fans target the 8-DIMM heat in a 4-GPU case. | TRX50 AI TOP is 16+8+4 without active memory fans. |
| **7× x16 + 2× MCIO + 4× SATA** | More expansion and storage ports; the MCIO drives can sit in the case’s 2.5" bays away from the GPUs. | With four 2-slot R9700s the extra x16 slots are covered; no free carrier slot. |
| **Ubuntu 24.04 LTS + AI TOP Utility** | Matches the Strata server OS; the TRX50 AI TOP’s manual lists Windows 11 only. | Linux works on both, but the WRX90 AI TOP is the one Gigabyte lists for Ubuntu. |
| **4× Gen5 M.2** | **No advantage** — the WRX90 AI TOP has 2 Gen5 M.2 + 1 Gen4 M.2 + 2 MCIO, with MCIOX8_1 sharing the M.2 slots. | The four-drive array is 3 Gen5 + 1 Gen4, versus 4 Gen5 on the TRX50 AI TOP. |

**Bottom line:** WRX90 buys **management, platform correctness, VRM/memory margin and storage expansion**. TRX50 buys **four Gen5 M.2 in the four-drive array** and immediate availability, at the cost of no IPMI, a hybrid platform and a higher board price (€896.75 vs €808.05). For the IQ3_S workload the GPU performance is identical; the choice is operational.

### Proper PRO/RDIMM vs the TRX50 hybrid

| | Standard TRX50 | TRX50 AI TOP (hybrid) | WRX90 (ASRock / WRX90 AI TOP) |
|---|---|---|---|
| CPU | non-Pro Threadripper | PRO or non-Pro | PRO only |
| Memory | 4-channel **UDIMM** | 8-channel **RDIMM** with PRO; 4-channel with non-Pro | 8-channel **RDIMM** |
| DIMM slots | 4 typical | 8 | 8 |
| Max capacity | 4× UDIMM | 2 TB RDIMM with PRO | 2 TB RDIMM |
| PCIe 5.0 | 80 lanes | PRO: 4× x16 + 4× M.2 exposed | 128 lanes; 6–7× x16 + storage |
| IPMI | typically no | no | **yes** |
| 4× Gen5 M.2 | no | **yes** | 3 Gen5 + 1 Gen4 |

“Proper” here means the platform AMD and the board vendor designed and validated for the **PRO CPU + 8× RDIMM** combination. The WRX90 boards are that platform: 8 DIMMs, eight channels, RDIMM/RDIMM-3DS, 2 TB, PRO-only, with the memory VRM/training/BIOS tuned for the full 8-DIMM load. The TRX50 AI TOP is a **Gigabyte-specific hybrid**: it wires the PRO’s 8-channel/128-lane memory and PCIe into a TRX50 board, and Gigabyte explicitly supports the 9955WX + RDIMM on it. It works, but it is not the standard TRX50 UDIMM/non-Pro board, and its 8-DIMM RDIMM validation matrix is narrower than a native WRX90 board’s.

The practical difference is largest at the **8×64 GB = 512 GB endgame**:

- 2×64 GB is easy on both: two channels, two DIMMs, low load. The 9955WX + 2×64 GB RDIMM is a supported configuration on either platform.
- 8×64 GB is 16 ranks across eight channels. RDIMM’s register buffers the address/command load, but the board still has to train and cool eight 2Rx4 modules. The WRX90 AI TOP adds **active DDR cooling (DDR Wind Blade XTREME Duo, up to 43 °C lower memory temperatures)** and a 14-layer server PCB; the ASRock WRX90 is a native 8-DIMM WRX90 board. The TRX50 AI TOP has the slots and the manual support, but not the same memory-cooling/validation margin.
- Always check the board’s **memory QVL** for the exact part at 8 DIMMs: Samsung M321R8GA0PB0-CWM (5600), Micron MTC40F2046S1RC64BH1 (6400 single), or G.Skill F5-6400R3644E64GQ4-T5N (4×64) / F5-6400R3848F64GE8-T5N (8×64). The 2-DIMM start is low-risk; the 8-DIMM speed (5600 vs 5200/4800, or 6400 with JEDEC/EXPO) is where the platform and BIOS matter.

### VRM and memory margin

| | TRX50 AI TOP | WRX90 AI TOP |
|---|---|---|
| VCore phases | 16+8+4 | **32+3+3+3** |
| PCB | E-ATX (layer count not stated in the manual) | **14-layer server-grade, 2 oz copper** |
| VRM cooling | Heatsinks | **Active VRM cooling + full-metal backplate** |
| Memory cooling | None | **DDR Wind Blade XTREME Duo fans** |
| CPU support | 350 W PRO (9955WX) | 350 W PRO, more headroom for 96-core |

The 9955WX is a **350 W** part; the TRX50 AI TOP’s 16+8+4 VRM is adequate for it, and Gigabyte supports the combination. The WRX90 AI TOP’s 32+3+3+3 stage is **not required for a 16-core 9955WX**; it is margin — lower phase current/temperature, better transient response, and headroom for a future 64/96-core PRO or a sustained all-core workload. In a 4-GPU case, the active VRM and memory fans also help the 8-DIMM configuration. For the 9955WX + 2×64 GB build, this is comfort, not a performance requirement; for the 8×64 GB/512 GB endgame and 24/7 operation, it is the safer envelope.

### Memory speed ceilings

| | Gigabyte TRX50 AI TOP | ASRock WRX90 WS EVO | Gigabyte WRX90 AI TOP |
|---|---|---|---|
| CPU official (9955WX) | **6400 MT/s** | **6400 MT/s** | **6400 MT/s** |
| Board OC claim | no published max; TRX50 OC R-DIMM kits ~7200 | **7600+ OC** | **7800 OC** |
| With the specified 2×64 GB 2Rx4 **5600** modules | 5600 | 5600 | 5600 |
| With 2×64 GB 2Rx4 **6400** modules | 6400 (QVL) | 6400 (QVL) | 6400 (QVL) |
| With 8×64 GB 2Rx4 **5600** | 5600 (358.4 GB/s) | 5600 (358.4 GB/s) | 5600 (358.4 GB/s) |
| With 8×64 GB 2Rx4 **6400** | 6400 if QVL (409.6 GB/s) | 6400 if QVL (409.6 GB/s) | 6400 if QVL (409.6 GB/s) |

The board OC numbers are **2–4 DIMM OC R-DIMM** figures (usually 16/24/32 GB modules), not 8×64 GB 2Rx4. The 9955WX’s official 6400 is the realistic JEDEC ceiling; 7600/7800 requires EXPO OC R-DIMM kits, a lucky IMC and the board’s QVL. With the build’s 5600 modules, all three boards run **5600** — the module is the limit, not the board.

For 6400, the EU-retail 64 GB parts found at the snapshot are:

- **Micron MTC40F2046S1RC64BH1** single module, **2Rx4, CL52, 1.1 V**, €3,279.97. Two = **€6,559.94** (2 channels / 102.4 GB/s); eight = **€26,239.76** (8 channels / 409.6 GB/s). This is the literal 2× start that stays JEDEC 6400 to 8×.
- **Kingston KSM64R52BD4** single module, €3,202.74; part number not confirmed on Kingston’s site.
- **G.Skill T5 Neo** 4×64 GB CL36-44-44-102 at 1.30 V, **€12,135.01**, and 8×64 GB CL38-48-48-102 at 1.35 V, **€23,094 notify-only** (Proshop €27,666.06 orderable). The 8×64 kit is G.Skill’s 8-DIMM 6400 octa kit; two 4×64 kits cost €24,270.02 and are not the same bin.

8×64 is 1 DIMM per channel, so 6400 is the native 1DPC topology, not a 2-DIMM-per-channel overclock. Confirm **2Rx4** and the exact QVL entry before ordering; the ASRock QVL was not machine-readable at the snapshot.

The BOM’s **value** RAM stays at 5600 because the 64 GB 2Rx4 5600 part is the volume/JEDEC/QVL-friendly module at €39.05/GB. The **fast** path is €51.25/GB for the 2× Micron pair (+31.2%), €47.40/GB for the 4× G.Skill kit (+21.4%), and €45.11/GB for the 8× G.Skill kit (+15.5%). For **IQ3_S fully resident**, the 9955WX’s 6400 is only +14% host bandwidth and the decode loop is GPU-bound. **For DeepSeek V4.1 that spills out of VRAM, RAM bandwidth is on the decode path**: 2×64 5600 89.6, 2×64 6400 102.4, 4×64 6400 204.8, 8×64 5600 358.4, 8×64 6400 409.6 GB/s. The 2×64 5600 staging config is not a DeepSeek config; 8×64 5600 (512 GB) is the capacity baseline, 8×64 6400 is +14% and the fastest 64 GB configuration, and the 24C 9965WX gives 23 pool workers vs 15. Spend the premium on capacity/channels before the last 800 MT/s.

### BMC: integrated, not an add-on

- The **WRX90 AI TOP** and **ASRock WRX90 WS EVO** have an **integrated ASPEED AST2600 BMC** with a dedicated IPMI LAN port. It is soldered on the board; there is no “BMC module” to buy or install.
- The **TRX50 AI TOP has no BMC** and no BMC header/firmware support. You **cannot add** the WRX90 board’s BMC to it; the Gigabyte BMC is board-specific, not an add-in card. A generic PCIe IPMI card is not a standard product, and the proprietary server-vendor modules (ASMB9-iKVM, iDRAC, iLO) do not apply to this board.
- The TRX50 AI TOP does have a **TPM header** for the GC-TPM2.0 SPI V2 module. That is **TPM, not BMC** — it gives secure boot/attestation, not remote power/KVM.
- If you want the TRX50 AI TOP’s four Gen5 M.2 but need out-of-band management, the practical substitute is a **PiKVM/JetKVM** (HDMI capture + USB HID + ATX power/reset wiring) or a **smart PDU** for remote power, plus Wake-on-LAN. It is not IPMI, but it covers the remote console/power use case.
- If true **IPMI/BMC** is a requirement, choose a board that has it: the ASRock WRX90 now, or the Gigabyte WRX90 AI TOP when it ships. Q-Flash Plus on the TRX50 AI TOP is BIOS recovery from a USB stick, not remote management.

## 5. Does the build change?

**Board only; CPU, RAM, PSU, case and GPUs stay the same.**

| Board choice | Board price | 4-drive RAID 0 | Extra parts | Availability |
|---|---:|---|---|---|
| Gigabyte TRX50 AI TOP (baseline) | €896.75 | **4 Gen5** M.2 | none | now |
| ASRock WRX90 WS EVO | €808.05 | 3 Gen5 + 1 Gen4 | 2× MCIO-to-M.2 cables, ~€60–100 | now |
| Gigabyte WRX90 AI TOP | **TBD** | 3 Gen5 + 1 Gen4 | 1× MCIO-to-M.2 cable (MCIOX8_2) | announced 2026-10-30, no offers |

- The 4 GPUs fit all three boards; the WRX90 boards’ slots 1/3/5/7 are 1-slot pitch, and the fourth card uses the case’s 8th bracket. No free slot for a carrier on either WRX90 board.
- The WRX90 AI TOP’s MCIOX8_1 shares bandwidth with M2A_CPU/M2B_CPU; with both Gen5 M.2 populated it is disabled. Use MCIOX8_2 for the fourth drive. The 2× Gen5 M.2 + 1× Gen4 M.2 + 1× MCIOX8_2 drive is 3 Gen5 + 1 Gen4.
- The ASRock needs 6-pin PCIe 12V to GFX_12V1/2; the Seasonic’s 6+2 cables cover it. The WRX90 AI TOP has 4× PCIe power connectors and 2× 8-pin ATX12V; the same PSU works.
- The Meshify 2 XL (EEB 305×330, 9+3 slots) fits all three; the 9000D’s 8 slots fit the four cards exactly.

If you want the simplest four-Gen5-M.2 RAID 0 and no MCIO cabling, keep the TRX50 AI TOP. If you want **WRX90 + IPMI now**, the ASRock is the available board. If you want **Gigabyte AI TOP + WRX90 + IPMI** and can wait for stock/pricing, the WRX90 AI TOP is the natural choice — but it will still be a 3 Gen5 + 1 Gen4 array, not four Gen5.

## 6. Recommendation

- **For the IQ3_S-in-VRAM build as specified:** the **ASRock 3× Gen5** build is the balanced choice: all-Gen5 3 TB at Gen4 price, IPMI/proper WRX90, and a 3 TB image on the 4 TB SATA. The TRX50 AI TOP only wins if **four Gen5 M.2 drives** (4 TB) or the Gigabyte AI TOP brand is a hard requirement; it has no IPMI. The WRX90 AI TOP is the Gigabyte-native WRX90/IPMI alternative once it ships.
- **For giant-model streaming / a storage-heavy server:** the WRX90 boards are the better fit: IPMI, MCIO/SlimSAS drives outside the GPU heat, and (on the ASRock) six NVMe ports. The Gen5/Gen4 array is still the working set; sequential read helps load, while random IOPS and the 8×64 GB RAM are the steady-state levers.
- **Do not buy a WRX90 board for four Gen5 drives.** None of them can run four Gen5 NVMe drives with four 2-slot GPUs: the ASRock has 3 Gen5 ports, the WRX90 AI TOP has 3 usable Gen5 ports because MCIOX8_1 shares with the M.2 slots, and the TRX50 AI TOP is the only one with 4 Gen5 M.2.
- **Do not buy the WRX90 AI TOP for the seven x16 slots alone.** With four 2-slot R9700s, slots 2/4/6 are covered; the MCIO and IPMI are the real gains.
