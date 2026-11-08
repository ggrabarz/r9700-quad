# Power connectors

<p class="muted">The PX-2200 has the watts. It does not have the PCIe 8-pin count for four GPUs plus board aux. This is the build’s hidden limit and the first thing to solve before ordering.</p>

## The PSU outputs

Seasonic PRIME PX-2200:

| Output | Count | Notes |
|---|---:|---|
| Native 12V-2x6 | **2** | 600 W class each |
| 12V-2x6 adapters | **2** | Each is **2× PCIe 8-pin → one 12V-2x6** |
| PCIe 8-pin (8P/6P) | **4** | The only PCIe 8-pin outputs |
| EPS 8-pin | 3 | CPU |
| SATA | 16 | drives |
| 24-pin | 1 | main |

## The four-GPU consumption

Four R9700s need four 12V-2x6 feeds:

- 2 GPUs on the **2 native** 12V-2x6.
- 2 GPUs on the **2 adapters**.
- Those two adapters consume **all four PCIe 8-pin**.

That leaves **zero PCIe 8-pin cables** for the board aux.

| Board | Board aux | Cables short |
|---|---|---|
| ASUS WRX90E-SAGE SE (single PSU) | 2× CPU 8-pin + **2× PCIE_8P** | **2 PCIe 8-pin** |
| ASRock WRX90 WS EVO | 2× ATX12V + **2× PCIE12V 6-pin + 2× GFX 6-pin** | **4 PCIe 8-pin** |
| ASUS W790E-SAGE SE | 2× 24-pin, 4× 8-pin +12V, 1× 8-pin PCIe, 1× 6-pin PCIe | check the single-PSU table; still 1× 8-pin + 1× 6-pin |

## The options

1. **Second PSU for the board aux.** The ASUS WRX90 has documented dual-PSU wiring (`PCIE_CPU_12V` headers); the ASRock does not. This is the clean ASUS path.
2. **A single PSU with ≥6 PCIe 8-pin for the ASUS, ≥8 for the ASRock.** The PX-2200 has 4. Check the 2,000 W class units’ connector counts, not just the wattage.
3. **Do not use splitters on 300 W cards.** A 12V-2x6 splitter is not a standard, safe way to run two 300 W GPUs from one output.

!!! danger "Do not assume the 4 PCIe cables cover the board GFX inputs"
    They cannot also feed the two 12V-2x6 adapters. The earlier book claimed they could; that was wrong. Budget the second PSU or a higher-connector PSU before buying the board.

## The ASUS advantage

The ASUS WRX90 needs **2** PCIe 8-pin for board aux; the ASRock needs **4** 6-pin. The ASUS is the lighter aux load and the only one with documented dual-PSU wiring. If you are building a four-GPU box with the PX-2200, the ASUS path is the more coherent one — after you add the second PSU or change the PSU.
