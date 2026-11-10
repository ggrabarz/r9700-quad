# Beam research: SP5 single-socket boards for 4x R9700 (AMD EPYC 9135)

Source: fetched datasheets/product pages (Gigabyte PDFs, ASRock Rack manuals, MiTAC product pages). Price/availability/region and slot pitch largely UNVERIFIED (no reseller quote fetched).

## Gigabyte MZ33-AR0 (rev 1.x/3.x)
- Socket: 1x LGA 6096 (SP5); AMD EPYC 9004/9005 single, cTDP up to 400 W.
- DIMMs: 24 (12-ch DDR5 RDIMM); max 4800 MT/s at 1DPC (both 9004/9005 per datasheet).
- PCIe: 4x PCIe Gen5 x16 slots (+ 7 MCIO, 1 M.2 Gen4 x4). Generation/width verified.
- Form factor: E-ATX 305 x 330 mm. Slot pitch/spacing for 2-slot cards: UNVERIFIED.
- PSU: 1x 24-pin ATX + 2x 8-pin + 1x 6-pin 12V. BMC: ASPEED AST2600 (IPMI).
- Price/availability/region: UNVERIFIED.
- 4-GPU validated config: UNVERIFIED.
- Verdict: Meets "4x x16"; Gen5 x16 all four. Good candidate (E-ATX, fits 4x 2-slot).

## Gigabyte MZ33-AR1 (rev 3.x)
- Socket: 1x SP5; EPYC 9004/9005 single, cTDP up to 500 W.
- DIMMs: 24 (12-ch DDR5 RDIMM); max 5200 MT/s 1DPC (9005), 4800 (9004).
- PCIe: 4x PCIe Gen5 x16 (+ 6 MCIO, 1 M.2 Gen4 x4).
- Form factor: E-ATX 304.8 x 330.2 mm. Slot pitch: UNVERIFIED.
- PSU: 24-pin + 2x 8-pin + 1x 6-pin. BMC: AST2600.
- Price/availability/region: UNVERIFIED.
- 4-GPU validated config: UNVERIFIED.
- Verdict: Best of the Gigabyte single-socket set (higher 1DPC speed 5200, 500 W cTDP, 4x Gen5 x16).

## Gigabyte MZ73-LM0 (rev 3.x) — dual socket
- Socket: 2x SP5 (DP); EPYC 9004/9005, cTDP up to 400 W. Single-CPU operation: UNVERIFIED.
- DIMMs: 24 (12-ch); max 6000 MT/s (9005), 4800 (9004) at 1DPC.
- PCIe: 4x PCIe Gen5 x16 (+ 2 MCIO, 1 M.2 Gen4 x4, 1 SlimSAS).
- Form factor: E-ATX 304.8 x 335.2 mm. Slot pitch: UNVERIFIED.
- PSU: 24-pin + 2x 8-pin + 3x 6-pin. BMC: AST2600.
- Price/availability/region: UNVERIFIED.
- 4-GPU validated config: UNVERIFIED.
- Verdict: 4x Gen5 x16 and 6000 MT/s, but dual-socket DP board; overkill/extra cost for one 9135; single-CPU use unverified.

## Gigabyte MZ73-LM1 (rev 3.x) — dual socket
- Socket: 2x SP5 (DP); EPYC 9004/9005, cTDP up to 400 W. Single-CPU: UNVERIFIED.
- DIMMs: 24; max 6400 MT/s (9005), 4800 (9004).
- PCIe: 4x PCIe Gen4 x16 (+ 2 SlimSAS, 1 M.2 Gen4 x4). (Gen4 only, not Gen5.)
- Form factor: E-ATX 305 x 330 mm. Slot pitch: UNVERIFIED.
- PSU: 24-pin + 2x 8-pin + 3x 6-pin. BMC: AST2600.
- Price/availability/region: UNVERIFIED.
- Verdict: 4x x16 but Gen4 only; highest 1DPC (6400) yet dual-socket. Consider only if Gen4 x16 suffices.

## ASRock Rack TURIN2D24G-2L+/500W
- Socket: 2x SP5 (DP, 9004/9005 + 97x4); cTDP up to 500 W. Single-CPU: UNVERIFIED.
- DIMMs: 24 (12+12, 1DPC); max 6400 MT/s (Turin), 4800 (Genoa). Form factor: proprietary 429 x 351 mm.
- PCIe: NO physical x16 slots; only MCIO (Gen5 x8) + 2 M.2 (Gen3 x4). Not usable for 4 double-width GPUs directly.
- PSU: 6x Micro-Hi 8-pin + 4-pin signal (ATX adapter). BMC: ASPEED AST2600 (IPMI).
- Price/availability/region: UNVERIFIED.
- Verdict: NOT suitable as a 4x double-width GPU board (no x16 slots).

## ASRock Rack GENOAD12M3-2H
- Spec page for "-2H" not found/verified. UNVERIFIED in full.
- Proxy (verified) GENOAD12M3-2Q: single SP5, 12 DIMM, DDR5 4800 1DPC, only 2x PCIe 5.0 x16 + 1 OCP x16; not 4 x16.
- Verdict: UNVERIFIED; likely not a 4x x16 board. Do not select without spec confirmation.

## ASRock Rack TURIN2D16-2T
- Socket: 2x SP5 (DP); cTDP up to 400 W. Single-CPU: UNVERIFIED.
- DIMMs: 16 (8+8, 1DPC); max 6400 MT/s. Form factor: EEB 304.8 x 335.3 mm.
- PCIe: 5x PCIe x16 slots (3x Gen4 + 2x Gen5 x16) + 3 MCIO + 1 M.2.
- PSU: 24-pin + 5x 8-pin. BMC: AST2600 (IPMI).
- Price/availability/region: UNVERIFIED.
- Verdict: 5 physical x16 slots but mixed Gen4/Gen5 and dual-socket; 4 could be used at x16 with 3 at Gen4.

## Tyan/MiTAC Tomcat HX S8050 (S8050GM4NE-2T)
- Socket: 1x SP5; EPYC 9005/9004 single. Form factor: CEB.
- DIMMs: 8 (not 12-channel full); DDR5 up to 6000 MT/s 1DPC. (Only 8 of 12 channels.)
- PCIe: 5x PCIe 5.0 x16 + 2 MCIO + 2 M.2.
- BMC: AST2600 (IPMI 2.0/Redfish). PSU connectors: UNVERIFIED.
- Price/availability/region: UNVERIFIED.
- Verdict: 5x Gen5 x16 and single socket, but only 8 DIMM slots (loses 4 memory channels) — not ideal for 12-ch EPYC, though plenty for 4 GPUs.

## Tyan/MiTAC Tomcat HX S8056 (S8056GME)
- Socket: 1x SP5; EPYC 9004 only (not 9005). Form factor: proprietary 12" x 14".
- DIMMs: 24 (12-ch); DDR5 4800 MT/s 1DPC.
- PCIe: only 1x PCIe 5.0 x16 + 1x PCIe 5.0 x24 + 1x OCP 3.0 x16 mezzanine + MCIO. Not 4 double-width slots.
- BMC: AST2600. PSU: UNVERIFIED.
- Price/availability/region: UNVERIFIED.
- Verdict: NOT suitable for 4 double-width GPUs.

## Summary verdict
Only boards with four physical Gen4/Gen5 x16 slots verified: Gigabyte MZ33-AR0, MZ33-AR1, MZ73-LM0, MZ73-LM1. Of these, single-socket + 12-DIMM + 4x Gen5 x16: MZ33-AR0/AR1. MZ33-AR1 is the pick (5200 MT/s 1DPC, 500 W cTDP). All prices/availability UNVERIFIED. Slot pitch/spacing for 2-slot cards UNVERIFIED on every board.
