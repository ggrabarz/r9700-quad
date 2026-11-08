# Gigabyte TRX50 AI TOP

<p class="muted"><strong>€896.75</strong> · Geizhals EU, 48 offers · four Gen5 M.2, no IPMI. Not used in the main builds; the four-Gen5 alternative.</p>

## What it is

A **TRX50 hybrid** workstation board that supports Threadripper PRO 9000/7000 WX with 8 RDIMM slots, 8-channel memory, 2 TB, and the PRO’s 128 PCIe 5.0 lanes — but on the TRX50 chipset. It has four PCIe 5.0 x16 slots and **four Gen5 M.2 sockets**, the cheapest way to a 4× Gen5 M.2 array.

It is not a standard TRX50 board. With a non-PRO Threadripper it drops to 4 channels, four active DIMM slots, PCIEX16_4 at Gen4 and M2D disabled. With the 9955WX it runs the full PRO memory/lane configuration. It has **no BMC/IPMI**, and the TPM header cannot add one.

## Specifications

| Feature | Detail |
|---|---|
| Chipset / socket | AMD TRX50, sTR5 (PRO hybrid) |
| CPU | Threadripper PRO 9000/7000 WX; non-PRO TR 9000/7000 |
| Memory | 8× DDR5 RDIMM, 8-channel with PRO, 2 TB |
| PCIe | 4× PCIe 5.0 x16 |
| NVMe | **4× Gen5 M.2** |
| SATA | 4× SATA3 |
| LAN / BMC | 2× 10GbE, **no BMC/IPMI** |
| VRM | 16+8+4 |
| Form factor | E-ATX 305×330 mm |
| Price | **€896.75** |

## Pros

<div class="pros-cons" markdown>
<div markdown>
### <span class="good">Pros</span>

- **Four Gen5 M.2** for a 4× Gen5 array without a carrier or MCIO cables.
- **Full PRO 8-channel / 128-lane** support with the 9955WX.
- **Lower board price** than the ASUS WRX90.
- **Four x16 slots** for four GPUs.
</div>
<div markdown>
### <span class="bad">Cons</span>

- **No IPMI/BMC.** The TPM header is not a BMC; a PiKVM/smart PDU is the substitute.
- **TRX50 hybrid**, not native WRX90; narrower 8-DIMM RDIMM validation matrix.
- **Only four x16 slots**; no spare slot for a carrier/NIC.
- **Four Gen5 M.2 under the GPUs**; the same thermal problem as the ASUS.
- **The 4 TB array no longer fits the 4 TB SATA image**; add an 8 TB HDD.
- **No 8×64 6400 QVL proof.**
</div>
</div>

## Where it is used

Not in the A–H BOMs. It is the four-Gen5 alternative when IPMI is not required and the board price matters more than management.
