# Supermicro / ASUS single-socket EPYC 9135 board research

Scope: single-socket SP5 boards for one AMD EPYC 9135 (Turin), 4x Radeon AI PRO R9700 (2-slot, 300 W). Requirement: four physical PCIe x16 slots carrying a double-width card at x16.

## Supermicro H14SSL-N

- Source: https://www.supermicro.com/en/products/motherboard/H14SSL-N ; reseller https://www.wiredzone.com/shop/product/10032891-...-15588
- Socket: single SP5 (AMD EPYC 9005/9004). Form factor: ATX, 12" x 10.1" (30.48 x 25.65 cm).
- DIMMs: 12 DDR5 RDIMM/3DS RDIMM slots, 1DPC, up to 3 TB, 6400 MT/s max (per board spec).
- PCIe: 3 PCIe 5.0 x16 (in x16) + 2 PCIe 5.0 x8; 2x M.2 PCIe 5.0 x4.
- Power/connectors: 6x 4-pin fan headers, 8 SATA3, MCIO hybrid ports; no on-board GPU power connectors (PSU must feed cards). BMC: ASPEED AST2600, IPMI/remote mgmt via dedicated 1 GbE IPMI LAN.
- LAN: dual 1 GbE (Broadcom BCM5720).
- Price/availability: $994.50 at WiredZone (US), in stock; 3-yr labor/1-yr parts warranty.
- 4-GPU validated config: none published for this board; Supermicro's Radeon-validated single-node 4-GPU platform is AS-2115HV-TRNT (Threadripper PRO, not EPYC). Slot pitch UNVERIFIED.
- Verdict: only 3 x16 slots — does NOT meet 4x x16 requirement.

## Supermicro H14SSL-NT

- Source: https://www.supermicro.com/en/products/motherboard/H14SSL-NT
- Socket: single SP5 (EPYC 9005/9004). Form factor: ATX, 12" x 10.1".
- DIMMs: 12 DDR5, 1DPC, up to 3 TB, 6400 MT/s.
- PCIe: 3 PCIe 5.0 x16 + 2 PCIe 5.0 x8; 2x M.2 PCIe 5.0 x4.
- Power/connectors: as H14SSL-N; LAN upgraded to dual 10 GbE (Broadcom BCM57416); IPMI via dedicated 1 GbE.
- Price/availability: UNVERIFIED (no price found on fetched pages).
- 4-GPU validated config: none published.
- Verdict: same 3 x16 limitation — does NOT meet requirement.

## Supermicro H14SSL-i

- Not a real product: no H14SSL-i exists in Supermicro's lineup (search returned only H12SSL-i for EPYC 7000/Genoa). Treat as invalid model name. Use H14SSL-N/NT instead.

## Supermicro H14DSG-* (H14DSG-O-CPU, H14DSG-OD, H14DSG-OM)

- Source: https://www.supermicro.com/en/products/motherboard/h14dsg-o-cpu ; https://www.wiredzone.com/.../h14dsg-om...
- All dual-socket SP5 (2x EPYC), not single-socket; 24 DIMM slots; PCIe via MCIO (12x PCIe 5.0 x8 MCIO, 1x PCIe 5.0 x16 AIOM) — no four discrete x16 slots on a single CPU. Not applicable to one EPYC 9135. UNVERIFIED slot pitch.

## ASUS K14PA-U12

- Source: https://servers.asus.com/products/servers/server-motherboards/K14PA-U12
- Socket: single SP5 (EPYC 9004, up to 128 cores; 9005 support via BIOS per ASUS EPYC 9005 page — verify). Form factor: SSI CEB (per Icecat). 12 DIMM DDR5 RDIMM, up to 3 TB, DDR5-4800 (per ASUS page; 6400 UNVERIFIED).
- PCIe: supports "up to two dual-slot GPUs" only (i.e. 2 x16-class slots) + MCIO/NVMe expansion; no 4 x16.
- BMC: ASMB11-iKVM with ASPEED AST2600 (IPMI).
- LAN: dual 25 GbE (SFP28).
- Price/availability: UNVERIFIED.
- Verdict: only 2 GPU slots — does NOT meet 4x requirement.

## ASUS K14PA-U24

- Source: ASL Omega 9125 spec (https://www.aslab.com/products/storage/omega9125_spec.html) using K14PA-U24-T; ASUS K14PA-U12 page for family context.
- Socket: single SP5 (EPYC 9005/9004). 24 DIMM DDR5-6400 ECC RDIMM, 12-channel, up to 3 TB.
- PCIe: only 2 PCIe 5.0 x16 (full height, full length, GPU) + 1 PCIe 5.0 x16 (x8 signal, low profile). Not 4 x16.
- BMC: ASMB11-iKVM (AST2600), IPMI.
- LAN: dual 1 GbE (Intel i350).
- Price/availability: UNVERIFIED (board sold inside ASUS ESC4000A-E12 / RS520A-E12 systems).
- Verdict: 2 x16 + 1 x8 — does NOT meet 4x x16 requirement.

## ASUS Pro WS variants

- No Pro WS workstation board for SP5/EPYC 9005 found; ASUS Pro WS line targets Ryzen/Threadripper/Intel (e.g. Pro WS B850M-ACE SE is AM5). ASUS's 4-GPU EPYC solution is the ESC4000A-E12 2U server (uses K14PA-U24-class board + risers), not a standalone 4-x16 motherboard.
- UNVERIFIED: whether any ASUS standalone board exposes 4 x16 for SP5.

## Supermicro Radeon-validated note

- Supermicro's Radeon AI PRO R9700 validated platforms (https://www.supermicro.com/en/accelerators/amd/radeon-validated-systems) list AS-2115HV-TRNT (Threadripper PRO, 4 double-width GPUs) and AS-4125GS-TNRT (dual-socket EPYC, 8 GPUs). No single-socket EPYC 9135 board with 4 x16 is validated.

## Overall verdict

Neither Supermicro (H14SSL-N/NT, 3 x16) nor ASUS (K14PA-U12/U24, ≤2 x16) offers a single-socket board with four physical PCIe x16 slots for one EPYC 9135. To run 4x R9700 at x16 each on this CPU, use a board with 4 x16 slots (e.g. Gigabyte MZ73-LM1: 4x PCIe Gen4 x16, but dual-socket — UNVERIFIED single-CPU operation) or accept x8 on the H14SSL-N's two x8 slots (via bifurcation/riser, not native x16). Price verified only for H14SSL-N ($994.50, WiredZone US).