# ASUS Pro WS WRX90E-SAGE SE vs ASRock WRX90 WS EVO

**Short answer:** both are proper WRX90 + IPMI boards and both run four 2-slot GPUs at **PCIe 5.0 x16** in slots 1/3/5/7. The **ASUS is the premium pick**: four Gen5 M.2 slots, two SlimSAS Gen4 ports, 32+3+3+3 VRM, dual-PSU support, and a public 4× R9700 build. It costs **€1,288.00** at Alternate (in stock) versus **€808.05** for the ASRock. The ASRock remains the value pick and the better thermal layout for MCIO drives.

## 1. Specs

| Feature | ASUS Pro WS WRX90E-SAGE SE | ASRock WRX90 WS EVO |
|---|---|---|
| Chipset / CPU | WRX90, sTR5, PRO 9000/7000 WX | WRX90, sTR5, PRO 9000/7000 WX |
| Memory | 8× DDR5 RDIMM, 8-channel, 2 TB, 1DPC | 8× DDR5 RDIMM, 8-channel, 2 TB, 1DPC |
| PCIe slots | 7× PCIe 5.0 x16: 6× x16 + **slot 6 x8** | 7× PCIe 5.0 x16: 6× x16 + **slot 6 x8** |
| 4-GPU layout | **slots 1/3/5/7, all x16** | **slots 1/3/5/7, all x16** |
| NVMe | **4× Gen5 M.2 x4 + 2× SlimSAS Gen4 x4** | 1× Gen5 M.2 + 1× Gen4 M.2 + 2× Gen5 MCIO + 2× Gen4 SlimSAS |
| SATA | 4× SATA3 | 4× SATA3 |
| BMC / IPMI | AST2600, dedicated 1G LAN | AST2600, dedicated 1G LAN |
| LAN | Intel X710 dual 10G + 1G BMC | Intel X710 dual 10G + 1G BMC |
| VRM | **32+3+3+3**, active VRM cooling | 18+3+3, active VRM cooling |
| Form factor | EEB 305×330 mm | EEB 305×330 mm |
| Price | **€1,288.00** (Alternate, in stock) | **€808.05** (Geizhals, 59 offers) |

Both boards have seven x16 slots; **slot 6 is the x8 slot** on both. The four-GPU configuration uses 1/3/5/7, so all four cards are x16. The ASUS manual confirms the 4-way table; the ASRock manual lists `PCIE6 at x8`.

## 2. Storage: the real difference

- **ASUS:** four Gen5 M.2 sockets. A **3× Gen5 RAID 0** can be built entirely in M.2, with **no MCIO cables**; a fourth Gen5 drive can be added for a 4 TB array, but a 4 TB array no longer fits a full image on the 4 TB SATA (3.6 TB usable), so add an 8 TB HDD.
- **ASRock:** 1× Gen5 M.2 + 2× Gen5 MCIO = a 3× Gen5 array, with the MCIO drives mounted in the case’s 2.5" bays **away from the GPU heat**. A fourth Gen4 M.2 and two Gen4 SlimSAS ports complete six NVMe ports (3 Gen5 + 3 Gen4).

The ASUS sockets sit on the board, under the four 2-slot GPUs. ASUS has M.2 heatsinks with an active fan, but a 24/7 Gen5 array runs hotter there than the ASRock’s MCIO drives in the 2.5" bays. The ASUS is the simpler build; the ASRock is the cooler one.

## 3. Power connectors — read this before ordering

The ASUS **single-PSU** wiring is **2× CPU 8-pin + 2× PCIE_8P**. It also has two `PCIE_CPU_12V` connectors for a dual-PSU configuration.

The Seasonic PRIME PX-2200 has:

- 3× EPS 8-pin
- **4× PCIe 8-pin**
- 2× native 12V-2x6
- 2× adapters, each **2× 8-pin to 12V-2x6**

Four R9700s consume the **2 native + 2 adapters**, and the two adapters consume **all four PCIe 8-pin**. That leaves **no PCIe 8-pin cable for the board’s aux connectors**:

- ASUS needs **2× PCIE_8P** for four GPUs.
- ASRock needs **2× PCIE12V 6-pin + 2× GFX 6-pin** (four PCIe cables).

The PX-2200 is fine on watts (1,630 W continuous, 26% headroom) but **short on PCIe 8-pin connectors** for four GPUs plus board aux. For a 4-GPU build, budget either:

1. a **second PSU** for the board aux (the ASUS has documented dual-PSU wiring; the ASRock does not), or
2. a **PSU with at least 6 PCIe 8-pin** outputs for the ASUS, or 8 for the ASRock.

This is a correction to the earlier book’s claim that the four PCIe cables cover the board GFX inputs. They cannot also feed the two 12V-2x6 adapters. The ASUS is the lighter aux load (2 PCIe vs 4) and the only one of the two with a documented dual-PSU path.

## 4. Reference build: 4× R9700 on this exact board

A public r/LocalLLM build by **brainchillzZ** (2026-10-24) uses:

- **ASUS WRX90 Sage**, **9955WX**, **128 GB DDR5-6400 ECC**, **4× R9700**, 122 GB visible, Ubuntu 26.04, kernel 7.0, `CONFIG_PCI_P2PDMA`, 211 W per card cap.
- **Radiance 1.11.0**, `qwen3.8-next-flash-fp8-iq4r-moe.rad` (113.6 GiB, 4-bit experts, int8 trunk, bf16 protected experts, MTP depth 3), TP4.
- **236 tok/s** single stream, **371 / 591 / 890 / 1,192 tok/s** aggregate at 2 / 4 / 8 / 16 streams, **11.27 ms** decode step, **8.4K prefill** at 4.4K and 70K prompts, **6.5× 262K** KV sessions, ~73 GB host RAM in use.

This is a **user report**, not an independent benchmark. It validates the board/CPU/RAM/4-GPU combination, including four x16 links and 128 GB DDR5-6400. It does **not** transfer to Strata: Radiance is tensor-parallel, Strata’s four-card mode is a pipeline layer split. The 236 tok/s is Radiance TP4, not a Strata number. It also does not prove **8×64 GB** — the Reddit build is 128 GB, not 512 GB.

Thread: <https://www.reddit.com/r/LocalLLM/comments/1xe1u1i/qwen38flashnext_on_4x_r9700_with_radiance_at_tp4/>

## 5. Recommendation

**ASUS premium** if you want the proven 4-GPU board, four Gen5 M.2 slots, the stronger VRM and the dual-PSU path. For Option A with **3× Gen5 M.2 and no MCIO cables**, the swap is:

| Item | ASRock A | ASUS A |
|---|---:|---:|
| Board | €808.05 | €1,288.00 |
| MCIO cables | €80.00 | €0.00 |
| Parts subtotal | €10,115.45 | €10,515.40 |
| +3% contingency | €10,418.91 | €10,830.86 |
| With 4 GPUs | €18,139.75 | €18,551.70 |

That is **+€411.95** for the ASUS, or **+€399.95** in parts. A **4× Gen5 M.2** build (4× 9100 PRO, 8 TB HDD for the image) is **€11,503.45 platform / €19,224.29 with GPUs**.

**ASRock value** if you want the cheapest board and the MCIO thermal layout. It keeps the 3× Gen5 + 4 TB SATA image plan and costs **€808.05**.

Do not choose either board on the promise of 8×64 GB DDR5-6400: the Reddit build is 128 GB, and the ASRock/ASUS QVL for 8×64 6400 remains unverified. The RAM ladder in the main book is unchanged.
