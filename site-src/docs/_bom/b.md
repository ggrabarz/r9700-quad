### Compute

| Part | Qty | Unit | Line | Notes |
|---|---:|---:|---:|---|
| [ASRock WRX90 WS EVO (sTR5, WRX90, EEB, 7x PCIe 5.0 x16, 6 NVMe ports, IPMI)](../parts/asrock-wrx90-ws-evo.md) | 1 | €808.05 | €808.05 | WRX90 + AST2600 IPMI; 1 Gen5 M.2 + 1 Gen4 M.2 + 2 Gen5 MCIO + 2 Gen4 SlimSAS. |
| [AMD Ryzen Threadripper PRO 9955WX (16C/32T, 4.5-5.4 GHz, 350 W, 128 PCIe 5.0 lanes, 8-channel DDR5 ECC)](../parts/amd-9955wx.md) | 1 | €1,637.70 | €1,637.70 | MSRP $1,649. Official memory: DDR5-6400, 8 channels, RDIMM. |

### Memory

| Part | Qty | Unit | Line | Notes |
|---|---:|---:|---:|---|
| [Samsung M321R8GA0PB0-CWM 64 GB DDR5-5600 CL46 2Rx4 ECC RDIMM](../parts/samsung-64gb-5600.md) | 2 | €2,499.00 | €4,998.00 | Value baseline: 2 DIMMs = 2 of 8 channels, 128 GB. The 6400 fast path is ram_64gb_6400_2x / _4x / _8x; these 5600 modules cannot be overclocked to 6400. |

### Storage

| Part | Qty | Unit | Line | Notes |
|---|---:|---:|---:|---|
| [Samsung 990 PRO 1 TB (PCIe 4.0 x4, 7,450/6,900 MB/s, 1.2M/1.55M IOPS)](../parts/samsung-990-pro.md) | 6 | €262.00 | €1,572.00 | Used for the 4× Gen4 and 6× Gen4 arrays; Gen4 thermals are easier under the GPUs. |
| [Samsung 870 EVO 4 TB SATA SSD](../parts/samsung-870-evo.md) | 1 | €665.00 | €665.00 | OS partition + cold model archive; a 3 TB array image fits (3.6 TB usable), a 4 TB/6 TB array does not. |
| [Toshiba N300 8 TB SATA HDD (archive/image)](../parts/toshiba-n300.md) | 1 | €389.00 | €389.00 | Only for the 6 TB array: a full 6 TB image on ~7.2 TB usable; slow, cold archive. |
| [MCIO 8i/x4 to M.2 NVMe adapter cable](../parts/mcio-cable.md) | 2 | €40.00 | €80.00 | 2 cables for the 3× Gen5 and 4× Gen4 arrays; 2 for the 6× Gen4 plus 2 SlimSAS. |
| [SlimSAS SFF-8654 to NVMe adapter cable](../parts/slimsas-cable.md) | 2 | €40.00 | €80.00 | Only for the 6× Gen4 array (2 SlimSAS ports). |

### Power

| Part | Qty | Unit | Line | Notes |
|---|---:|---:|---:|---|
| [Seasonic PRIME PX-2200 (2200 W, ATX 3.1, 80+ Platinum, 2x native 12V-2x6 + 2x adapters, 4x PCIe 8-pin)](../parts/seasonic-px-2200.md) | 1 | €489.90 | €489.90 | 200-240 V only; 210 mm; 26% headroom over 1,630 W. |

### Cooling

| Part | Qty | Unit | Line | Notes |
|---|---:|---:|---:|---|
| [SilverStone SST-XE360-TR5 (360 mm AIO, sTR5/SP6, 350 W class)](../parts/silverstone-xe360-tr5.md) | 1 | €389.90 | €389.90 | Top-mounted exhaust; keeps CPU heat out of the GPU intake. |

### Chassis

| Part | Qty | Unit | Line | Notes |
|---|---:|---:|---:|---|
| [Fractal Design Meshify 2 XL (EEB 305x330, 9+3 slots, 6x 3.5", 2x 2.5", 250 mm PSU, 480 mm top rad)](../parts/fractal-meshify-2-xl.md) | 1 | €209.90 | €209.90 | Fits the EEB ASRock, four 2-slot GPUs, the 360 AIO and the 210 mm PSU. |
| [140 mm PWM case fan (Fractal/Arctic class)](../parts/fan-140.md) | 3 | €15.00 | €45.00 | Case includes 3x 140 mm; add bottom/rear fans for the M.2/GPU zone. |

### Totals

| | Amount |
|---|---:|
| **Parts subtotal** | **€11,364.45** |
| 3.0% contingency | €340.93 |
| **Platform total (GPUs excluded)** | **€11,705.38** |
| GPUs (owned, replacement value) | €7,720.84 |
| **Total if buying the four GPUs** | **€19,426.22** |
