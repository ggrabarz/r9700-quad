# Builds

<p class="muted">Every priced configuration in the book, in one place. The four GPUs are owned and excluded from the platform totals; the “with GPUs” column uses today’s replacement price.</p>

| Build | Board | Memory | Storage | Platform | With GPUs | Best for |
|---|---|---|---:|---:|---:|---|
| [A — Balanced 3× Gen5](a-balanced.md) | ASRock WRX90 | 2×64 GB 5600 | 3× Gen5 / 3 TB | **€10,418.91** | €18,139.75 | The value middle |
| [B — Capacity 6× Gen4](b-capacity.md) | ASRock WRX90 | 2×64 GB 5600 | 6× Gen4 / 6 TB | €11,705.38 | €19,426.22 | A model library |
| [C — Value 4× Gen4](c-value.md) | ASRock WRX90 | 2×64 GB 5600 | 4× Gen4 / 4 TB | €10,682.59 | €18,403.43 | Cheapest per TB |
| [D — Staged 6400 2×64](d-staged-6400.md) | ASRock WRX90 | 2×64 GB 6400 | 3× Gen5 / 3 TB | €12,027.71 | €19,748.55 | The literal 2× 6400 start |
| [E — Fast RAM 4×64](e-fast-ram.md) | ASRock WRX90 | 4×64 GB 6400 | 3× Gen5 / 3 TB | €17,770.03 | €25,490.87 | 256 GB at 6400 |
| [F — Full Speed 8×64](f-full-speed.md) | ASRock WRX90 | 8×64 GB 6400 | 3× Gen5 / 3 TB | €29,057.79* | €36,778.63 | 512 GB endgame |
| [G — ASUS Premium 3× Gen5](g-asus-premium.md) | ASUS WRX90E-SAGE | 2×64 GB 5600 | 3× Gen5 M.2 / 3 TB | €10,830.86 | €18,551.70 | Premium board, no MCIO |
| [H — ASUS 4× Gen5](h-asus-4x-gen5.md) | ASUS WRX90E-SAGE | 2×64 GB 5600 | 4× Gen5 / 4 TB | €11,503.45 | €19,224.29 | 4 TB all-Gen5 |
| [Used W790 bundle](w790-used.md) | ASUS W790E-SAGE | 8ch DDR5-4800 | your choice | CHF 1,100–1,200** | — | Cheap 4-GPU platform |

<p class="small muted">* F uses Alternate’s notify-only €23,094 octa-kit price. Orderable at Proshop: €33,766.02 / €41,486.86 with GPUs.<br>** Board + CPU only; Ricardo price not readable, comparable eBay sold bundles. Add LGA4677 cooler, RAM, storage, PSU.</p>

## How to choose

<div class="grid cards" markdown>

-   **A — the default**
    ---
    All-Gen5 3 TB, a full image on the 4 TB SATA, IPMI, and the cheapest proper WRX90 board. Start here unless you need 6 TB or 6400 memory.
    [:octicons-arrow-right-24: Build A](a-balanced.md)

-   **D — 2× now, 8× later**
    ---
    Two Micron 64 GB DDR5-6400 modules, JEDEC 2Rx4, with six more later for 512 GB. The only literal 2× 6400 start.
    [:octicons-arrow-right-24: Build D](d-staged-6400.md)

-   **F — 512 GB**
    ---
    G.Skill’s 8×64 GB 6400 octa kit, eight channels, 409.6 GB/s. The DeepSeek UD-Q8 / large-model endgame.
    [:octicons-arrow-right-24: Build F](f-full-speed.md)

-   **G — premium board**
    ---
    ASUS WRX90E-SAGE SE, four Gen5 M.2, no MCIO, 32+3+3+3 VRM, dual-PSU. A public 4× R9700 build exists on this board.
    [:octicons-arrow-right-24: Build G](g-asus-premium.md)

</div>

## The one caveat that applies to every four-GPU build

The Seasonic PX-2200 is fine on watts, but **four GPUs consume both native 12V-2x6 outputs and both 2×8-pin adapters — all four PCIe 8-pin cables**. The board aux then has no cable left: ASUS wants 2× PCIE_8P, ASRock wants 4× 6-pin. Budget a second PSU or a PSU with more PCIe 8-pin before ordering. See [Power connectors](../reference/power-connectors.md).
