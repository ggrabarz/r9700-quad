# EPYC 9135 (SP5) board research for 4x R9700 @ x16

Source: web research (Gigabyte reseller, Supermicro product pages, AMD/Kingston refs). Items not verified marked UNVERIFIED.

## 1. AMD EPYC 9005 memory spec (1DPC)
- AMD EPYC 9005 (Turin) official: DDR5-6400 at 1 DIMM per channel across 12 channels (Kingston Turin guide; NEMIX note: AMD lists DDR5-6400 1DPC; independent reviews describe 6000 base / 6400 on qualified platforms). Source: https://www.kingston.com/en/memory/server-memory/turin
- Board-level QVL evidence needed: reseller spec for Gigabyte MZ33-AR1 lists max 5200 MHz. Whether the board validates DDR5-6400 1DPC RDIMMs is UNVERIFIED (no QVL fetched).

## 2. Gigabyte MZ33-AR1 (rev 3.x) -- only verified 4x x16 SP5 board
- Socket: SP5 (LGA 6096); AMD EPYC 9005/9004; single CPU, cTDP up to 500W.
- Form factor: E-ATX, 304.8 x 330.2 mm.
- DIMMs: 24 slots, 12-channel DDR5 ECC RDIMM; max 3 TB; reseller lists max 5200 MHz (AMD lists 6400 1DPC).
- PCIe: 4x PCIe 5.0 x16 (mechanical + electrical). No x8 slots mentioned.
- Network: 2x 10GbE RJ45; AST2600 BMC/IPMI (out-of-band).
- Storage: 1x M.2 PCIe 4.0 x4; multiple NVMe/SATA (per reseller).
- Price/avail: ~EUR 1,134 (Happyware reseller), out of stock at that reseller; Newegg listed from ~$763.57. Region: EU/US.
- 4x R9700 validated config: UNVERIFIED (no documented build found).
- Power connectors on board: UNVERIFIED from fetched pages (server board: 2x 8-pin EPS expected; no PCIe aux). Confirm in manual.

## 3. Supermicro H14SSL-NT / H14SSL-N (near-miss)
- Socket SP5, ATX 304.8 x 256.5 mm, 12 DIMM, DDR5 up to 6400 MT/s (1DPC), 3x PCIe 5.0 x16 + 2x PCIe 5.0 x8, AST2600 BMC/IPMI.
- Only 3 physical x16 slots -> cannot host four 2-slot x16 cards at x16; fourth card would run at x8 (or need riser). Source: https://www.supermicro.com/en/products/motherboard/H14SSL-N

## 4. Fit / pitch
- MZ33-AR1: 4 x16 slots on E-ATX; physical slot pitch UNVERIFIED from fetched pages. Four 2-slot (40 mm) R9700 cards need ~8 slot positions; verify pitch >= 2 slots between x16 slots. If 1-slot pitch, adjacent 2-slot cards will collide -> need riser/vertical mount or a case with 8+ slots.
- Case requirement: 4x 267 mm dual-slot cards = 8 expansion slots minimum; E-ATX board (305 x 330) needs E-ATX/SSI-EEB chassis.

## 5. Power
- 4x R9700 300 W + EPYC 9135 ~200 W = ~1.4 kW plus drives/fans; size PSU >= 1600-2000 W (existing 2200 W unit covers).
- Each R9700 uses 1x 12V-2x6. Board PCIe aux unverified. Use PSU with 4x 12V-2x6 (or adapters from dual 8-pin). MZ33-AR1 likely needs 2x 8-pin EPS for CPU; no onboard PCIe power expected.

## Verdict
- Only verified SP5 board with four x16 slots: Gigabyte MZ33-AR1 (E-ATX, ~EUR 1,134, out of stock at one EU reseller). Memory validation above 5200 MHz and physical 2-slot pitch are UNVERIFIED and must be confirmed against Gigabyte QVL/manual before ordering. No documented 4x R9700 build on SP5 found.