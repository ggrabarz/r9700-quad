# WRX90 board options vs the Gigabyte TRX50 AI TOP — and what it means for SSD weight streaming

**Short answer:** there are now three relevant boards, and no single one wins every column.

- **ASRock WRX90 WS EVO** — WRX90, IPMI, 7 slots, 6 NVMe ports, **available at €808.05**. The 4-drive RAID 0 is 3 Gen5 + 1 Gen4 (1 Gen5 M.2 + 2 Gen5 MCIO + 1 Gen4 M.2).
- **Gigabyte WRX90 AI TOP** — WRX90, IPMI, 7 slots, 2 Gen5 M.2 + 1 Gen4 M.2 + 2 MCIO. **Announced 2026-10-30, no price or retail offers at the snapshot.** The 4-drive RAID 0 is also 3 Gen5 + 1 Gen4, because MCIOX8_1 shares bandwidth with the two Gen5 M.2 slots.
- **Gigabyte TRX50 AI TOP** — TRX50, **no IPMI**, 4 slots, but **4 Gen5 M.2**; €896.75. The only one of the three that runs four Gen5 drives in RAID 0 without a carrier.

So: if you need **WRX90 + IPMI now**, the ASRock is the board. If you want the **Gigabyte AI TOP ecosystem with WRX90 + IPMI** and can wait, the WRX90 AI TOP is the natural choice — but it does not restore the four Gen5 M.2 sockets. If **four Gen5 M.2 drives** are the priority, the TRX50 AI TOP remains the one.

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

**Bottom line:** WRX90 buys **management, platform correctness, VRM/memory margin and storage expansion**. TRX50 buys **four Gen5 M.2 in the four-drive array**, a lower price and immediate availability, at the cost of no IPMI and a hybrid platform. For the IQ3_S workload the GPU performance is identical; the choice is operational.

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
- Always check the board’s **memory QVL** for the exact Samsung M321R8GA0PB0-CWM at 8 DIMMs. The 2-DIMM start is low-risk; the 8-DIMM speed (5600 vs 5200/4800) is where the platform and BIOS matter.

### VRM and memory margin

| | TRX50 AI TOP | WRX90 AI TOP |
|---|---|---|
| VCore phases | 16+8+4 | **32+3+3+3** |
| PCB | E-ATX (layer count not stated in the manual) | **14-layer server-grade, 2 oz copper** |
| VRM cooling | Heatsinks | **Active VRM cooling + full-metal backplate** |
| Memory cooling | None | **DDR Wind Blade XTREME Duo fans** |
| CPU support | 350 W PRO (9955WX) | 350 W PRO, more headroom for 96-core |

The 9955WX is a **350 W** part; the TRX50 AI TOP’s 16+8+4 VRM is adequate for it, and Gigabyte supports the combination. The WRX90 AI TOP’s 32+3+3+3 stage is **not required for a 16-core 9955WX**; it is margin — lower phase current/temperature, better transient response, and headroom for a future 64/96-core PRO or a sustained all-core workload. In a 4-GPU case, the active VRM and memory fans also help the 8-DIMM configuration. For the 9955WX + 2×64 GB build, this is comfort, not a performance requirement; for the 8×64 GB/512 GB endgame and 24/7 operation, it is the safer envelope.

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

- **For the IQ3_S-in-VRAM build as specified:** the TRX50 AI TOP is the lower-integration-risk choice because of its four Gen5 M.2 sockets and 2-slot-spaced x16 slots. If you need IPMI/WRX90, the ASRock is available now; the WRX90 AI TOP is the Gigabyte-native alternative once it ships.
- **For giant-model streaming / a storage-heavy server:** the WRX90 boards are the better fit: IPMI, MCIO/SlimSAS drives outside the GPU heat, and (on the ASRock) six NVMe ports. The 4×1 TB RAID 0 is still the working set; sequential read helps load, while random IOPS and the 8×64 GB RAM are the steady-state levers.
- **Do not buy a WRX90 board for four Gen5 drives.** None of them can run four Gen5 NVMe drives with four 2-slot GPUs: the ASRock has 3 Gen5 ports, the WRX90 AI TOP has 3 usable Gen5 ports because MCIOX8_1 shares with the M.2 slots, and the TRX50 AI TOP is the only one with 4 Gen5 M.2.
- **Do not buy the WRX90 AI TOP for the seven x16 slots alone.** With four 2-slot R9700s, slots 2/4/6 are covered; the MCIO and IPMI are the real gains.
