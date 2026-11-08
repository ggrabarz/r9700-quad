# Storage and lanes

<p class="muted">The four GPUs take 64 PCIe 5.0 lanes. The storage choice is about which ports are left, how the drives are cooled, and whether the array fits a backup.</p>

## The four arrays

| | A — 3× Gen5 | B — 6× Gen4 | C — 4× Gen4 | H — 4× Gen5 |
|---|---|---|---|---|
| Capacity | **3 TB** | **6 TB** | **4 TB** | **4 TB** |
| Drives | 3× 9100 PRO | 6× 990 PRO | 4× 990 PRO | 4× 9100 PRO |
| Ports | 1 Gen5 M.2 + 2 Gen5 MCIO | 2 M.2 + 2 MCIO + 2 SlimSAS | 2 M.2 + 2 MCIO | 4 Gen5 M.2 (ASUS) |
| Sequential | ~42–44 GB/s | ~44–45 GB/s | ~28–30 GB/s | ~56–59 GB/s |
| 4K IOPS | ~5.6M | ~7.2M | ~4.8M | ~7.4M |
| Image on 4 TB SATA | **yes** | no — 8 TB HDD | no | no — 8 TB HDD |
| Extra | 2 MCIO cables | 4 cables + 8 TB HDD | 2 MCIO cables | 8 TB HDD |

## Port maps

**ASRock WRX90 WS EVO:**

- 1× Gen5 M.2
- 1× Gen4 M.2
- 2× Gen5 MCIO (x4)
- 2× Gen4 SlimSAS (x4)
- 4× SATA

**ASUS WRX90E-SAGE SE:**

- 4× Gen5 M.2
- 2× Gen4 SlimSAS (x4)
- 4× SATA

Both boards: 4-way GPUs use slots 1/3/5/7 at x16; slot 6 is x8 and unused.

## Thermal reality

- The ASRock’s MCIO/SlimSAS drives can live in the 2.5" bays, away from the GPU heat. That is why the 3× Gen5 array is practical.
- The ASUS’s four M.2 sockets sit on the board, under the four 2-slot GPUs. ASUS fits M.2 heatsinks and an active M.2 fan, but four Gen5 drives are still the hottest layout.
- Target <70 °C on `smartctl -A`; bottom intake and a 2.5" bay with airflow.

## RAID 0 reality

- RAID 0 has no redundancy. The array is a working set, not a backup.
- A 3 TB array fits a full image on the 4 TB SATA (3.6 TB usable). A 4 TB or 6 TB array does not; add the 8 TB N300.
- A single drive failure loses the array; the archive/image is the recovery path.
- The six-drive array has a higher failure probability; the 8 TB HDD is part of build B, not an optional extra.

## Lane budget

| Consumer | Lanes |
|---|---:|
| 4× PCIe 5.0 x16 GPUs | 64 |
| 3× Gen5 ports (A/D/E/F) | 12 |
| 4× Gen5 M.2 (H) | 16 |
| 6× Gen4 ports (B) | 24 |
| 4× Gen4 ports (C) | 16 |
| CPU total | 128 |

All builds are inside the 9955WX’s 128 lanes. The constraint is ports and cooling, not lane count.
