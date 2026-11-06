# ASRock WRX90 WS EVO vs Gigabyte TRX50 AI TOP — and what it means for SSD weight streaming

**Short answer:** yes, the ASRock WRX90 WS EVO is the more capable board on paper, and at the 2026-11-06 snapshot it is also **cheaper** (€808.05 vs €896.75). It has 7 PCIe 5.0 x16 slots, 6 NVMe-capable ports (1 Gen5 M.2 + 1 Gen4 M.2 + 2 Gen5 MCIO + 2 Gen4 SlimSAS), IPMI, dual 10GbE and a stronger VRM. The catch is that the four 2-slot R9700s still consume the slot stack: the extra x16 slots are covered, and the ASRock has only **one Gen5 M.2** plus two Gen5 MCIO, so a 4-drive RAID 0 is 3 Gen5 + 1 Gen4 unless you use a carrier that has no free slot. For the exact 4×1 TB M.2 RAID 0, the Gigabyte’s four Gen5 M.2 sockets are simpler. For a **giant-model library** with IPMI and more NVMe ports, the ASRock is the better board.

## 1. Board comparison

| Capability | ASRock WRX90 WS EVO | Gigabyte TRX50 AI TOP |
|---|---|---|
| Chipset | AMD WRX90 (full workstation) | AMD TRX50 (hybrid; PRO CPU unlocks 8ch/Gen5) |
| CPU | TR PRO 9000/7000 WX | TR PRO 9000/7000 WX and TR 9000/7000 |
| Memory | 8× DDR5 RDIMM, 8-channel, 2 TB, up to 7600+ OC | 8× DDR5 RDIMM, 8-channel with PRO, 2 TB |
| PCIe x16 slots | **7× PCIe 5.0 x16** (6 at x16, PCIE6 at x8) | 4× PCIe 5.0 x16 |
| M.2 | 1× Gen5 x4 (M2_1) + 1× Gen4 x4 (M2_2) | **4× Gen5 x4** |
| Other NVMe | 2× MCIO Gen5 x4, 2× SlimSAS Gen4 x4 | — |
| SATA | 4× SATA3 + SATA via MCIO/SlimSAS | 4× SATA3 |
| LAN | 2× Intel X710 10GbE + **dedicated IPMI** | 2× Marvell AQC113C 10GbE |
| BMC | **ASPEED AST2600 IPMI** | none |
| VRM | 18+3+3, 110 A SPS, active VRM cooling | 16+8+4 |
| Power connectors | 2× 8-pin ATX12V, 2× 6-pin PCIe 12V, 2× 6-pin GFX 12V | 2× 8-pin ATX12V, 4× 8-pin PCIe aux |
| Form factor | EEB 30.5×33.0 cm | E-ATX 30.5×33.0 cm |
| Price (2026-11-06) | **€808.05** (Geizhals, 59 offers) | €896.75 (Geizhals, 48 offers) |

The ASRock is **€88.70 cheaper** and adds IPMI, six NVMe ports and three more x16 slots. The Gigabyte’s counter is four Gen5 M.2 sockets on the board, which is exactly what the 4×1 TB RAID 0 wants.

## 2. The slot reality with four 2-slot R9700s

The ASRock’s seven x16 slots are on a **1-slot pitch**. Four 2-slot cards go in PCIE1, 3, 5 and 7; slots 2, 4 and 6 are covered by the cards. The fourth card’s second bracket lands in the case’s 8th slot. So:

- Four R9700s fit, but there is **no free slot** for a 4× M.2 carrier or a NIC/HBA.
- The extra x16 slots are useful for seven single-slot cards, or three dual-slot GPUs plus a single-slot card — not for four dual-slot GPUs plus an add-in.
- The onboard MCIO/SlimSAS and dual 10GbE/IPMI are what make the ASRock more capable without a free slot.

The Gigabyte’s four x16 slots are **2-slot spaced**, so the same four cards consume eight bracket positions with no slot-sharing; its four Gen5 M.2 sockets are the storage path.

## 3. The 4×1 TB RAID 0 on each board

| Board | 4-drive topology | Gen5 drives | Verdict |
|---|---|---:|---|
| Gigabyte TRX50 AI TOP | 4× onboard Gen5 M.2 | **4** | Plug-and-play, all Gen5, but the M.2 sit under the GPUs. |
| ASRock WRX90 WS EVO | 1× Gen5 M.2 + 2× Gen5 MCIO + 1× Gen4 M.2 | **3** | 3 Gen5 + 1 Gen4; MCIO cables/drives needed; the fourth drive is the slow link. |
| ASRock + 4× M.2 carrier | Carrier in a free x16 slot | 4 | **No free slot** with four 2-slot GPUs; needs a riser/3-GPU layout. |

If you want four Gen5 drives in RAID 0, the Gigabyte is the simpler board. If you want **more than four NVMe drives** (a giant-model library), the ASRock’s six ports are the advantage: 3 Gen5 + 3 Gen4, and the MCIO/SlimSAS drives can live in the case’s 2.5" bays away from the GPU heat.

The ASRock’s 4-drive array at 3 Gen5 + 1 Gen4 is not a disaster: RAID 0 sums sequential bandwidth and random IOPS, so the array is still fast; the Gen4 member simply contributes less. The 4 TB capacity is unchanged.

## 4. Giant-model weight streaming: what the 4× RAID 0 actually buys

The 4×1 TB RAID 0 is useful, but not for the reason the “sequential read” headline suggests.

- **Cold start / model load is sequential.** A 191 GB DeepSeek 2.00 bpw load at ~28 GB/s (4× Gen4 990 PRO) is ~6.8 s; at ~56 GB/s (4× Gen5) it is ~3.4 s; a 508 GB model is ~18 s vs ~9 s. This is the part where 4× RAID 0 sequential shines.
- **Steady-state weight/PLE streaming is random.** The engine reads expert records and PLE rows in small, scattered chunks, not one sequential file. The relevant numbers are **random IOPS and latency**, plus the host RAM/page cache, not the 28–56 GB/s sequential figure. RAID 0 still helps because it stripes those random reads over four drives; four Gen4 990 PROs already give ~4.8M 4K IOPS theoretical, and the engine’s I/O threads/PCIe usually become the limit before the drives do.
- **Capacity is the first constraint for giant models.** 4 TB holds a 191 GB model plus a 508 GB model plus the 79 GB Strata set (≈778 GB), so the array is big enough for the stated experiments. A library of many giant models wants more drives — the ASRock’s six NVMe ports help; the Gigabyte’s four M.2 + four SATA is more limited (SATA is too slow for steady-state streaming).
- **Host RAM is the bigger constraint.** The 128 GB build can hold the 28.8 GB PLE and a page-cache slice, but a 508 GB model’s CPU lane is ~171.5 GB (per `docs/DECISIONS.md`); the 8×64 GB = 512 GB endgame is what makes that model comfortable. The board choice does not change the DIMM count: both are 8× DDR5, 8-channel, 2 TB.
- **Gen5 vs Gen4.** Gen5 doubles sequential load speed and improves random IOPS, but the drives run hotter. The Gigabyte’s four Gen5 M.2 sit **under the GPUs**; the ASRock’s MCIO/SlimSAS drives can be placed in the case’s 2.5" bays. For a machine that streams weights for hours, the ASRock’s thermal placement may matter more than the fourth Gen5 port.

Measured anchors for the giant-model case (Strata docs): 4× R9700, DeepSeek V4.1 2.00 bpw, **74–77 tok/s** decode and 400–450 tok/s prefill at 8K (README table); the app’s four-card DeepSeek number is ~31 tok/s (MULTI_GPU). The 4 TB array is not the bottleneck at those rates; the expert cache hit rate, the host RAM and the CPU/PCIe path are.

## 5. Does the build change?

**Board only, if you choose the ASRock:**

| Item | Change |
|---|---|
| Motherboard | Gigabyte TRX50 AI TOP €896.75 → ASRock WRX90 WS EVO €808.05 (**−€88.70**) |
| RAID 0 drives | Same 4× 1 TB 990 PRO; on the ASRock use 1 Gen5 M.2 + 2 Gen5 MCIO + 1 Gen4 M.2 (3 Gen5 + 1 Gen4) |
| MCIO cables | 2× MCIO-to-M.2 NVMe cables/adapters, roughly €60–100 (estimate; source depends on the drive form) |
| Net | Roughly −€29 to +€11 versus the Gigabyte, with IPMI and two more NVMe ports |
| CPU/RAM/PSU/case | Unchanged: 9955WX, 2×64 GB, 2,200 W, Meshify 2 XL (EEB 305×330 fits) |
| 4 GPUs | Unchanged; ASRock slots 1/3/5/7, fourth card uses the case’s 8th bracket; no free slot for a carrier |
| Power | ASRock needs 6-pin PCIe 12V to GFX_12V1/2; the Seasonic’s 6+2 cables cover it |

If you want the simplest four-Gen5-M.2 RAID 0 and no MCIO cabling, keep the Gigabyte. If you want IPMI, six NVMe ports, a stronger VRM and a cheaper board for a giant-model library, the ASRock is the better buy — provided you accept 3 Gen5 + 1 Gen4 in the four-drive array or add drives on the MCIO/SlimSAS ports.

## 6. Recommendation

- **For the IQ3_S-in-VRAM build as specified:** the Gigabyte TRX50 AI TOP is the lower-integration-risk choice because of its four Gen5 M.2 sockets and 2-slot-spaced x16 slots. The ASRock works, but the 4-drive array is 3 Gen5 + 1 Gen4 and needs MCIO cabling.
- **For giant-model streaming / a storage-heavy server:** the ASRock WRX90 WS EVO is the better board: IPMI, six NVMe ports, cheaper, and the MCIO/SlimSAS drives can be placed away from the GPUs. The 4×1 TB RAID 0 is still the working set; the sequential read helps load, while random IOPS and the 8×64 GB RAM are the steady-state levers.
- **Do not buy the ASRock for the seven x16 slots alone.** With four 2-slot R9700s, slots 2/4/6 are covered; the seventh slot does not give you a free carrier. The MCIO/SlimSAS and IPMI are the real gains.
