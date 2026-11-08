# Builds

<p class="muted">Every priced configuration in the book. The four GPUs are owned and excluded; the “with GPUs” figure is today’s replacement value. Prices include 3% contingency.</p>

<div class="grid cards" markdown>

-   **A — Balanced 3× Gen5**
    ---
    **€10,418.91** · with GPUs €18,139.75  
    ASRock WRX90 · 2×64 GB 5600 · 3× Gen5 / 3 TB  
    The value middle; full SATA image.
    [:octicons-arrow-right-24: Build A](a-balanced.md)

-   **B — Capacity 6× Gen4**
    ---
    **€11,705.38** · with GPUs €19,426.22  
    ASRock WRX90 · 2×64 GB 5600 · 6× Gen4 / 6 TB  
    The model library; 8 TB HDD image.
    [:octicons-arrow-right-24: Build B](b-capacity.md)

-   **C — Value 4× Gen4**
    ---
    **€10,682.59** · with GPUs €18,403.43  
    ASRock WRX90 · 2×64 GB 5600 · 4× Gen4 / 4 TB  
    Cheapest per TB; no full image.
    [:octicons-arrow-right-24: Build C](c-value.md)

-   **D — Staged 6400 2×64**
    ---
    **€12,027.71** · with GPUs €19,748.55  
    ASRock WRX90 · 2×64 GB 6400 · 3× Gen5 / 3 TB  
    The literal 2× 6400 start.
    [:octicons-arrow-right-24: Build D](d-staged-6400.md)

-   **E — Fast RAM 4×64**
    ---
    **€17,770.03** · with GPUs €25,490.87  
    ASRock WRX90 · 4×64 GB 6400 · 3× Gen5 / 3 TB  
    256 GB at 204.8 GB/s.
    [:octicons-arrow-right-24: Build E](e-fast-ram.md)

-   **F — Full Speed 8×64**
    ---
    **€29,057.79*** · with GPUs €36,778.63*  
    ASRock WRX90 · 8×64 GB 6400 · 3× Gen5 / 3 TB  
    512 GB at 409.6 GB/s.
    [:octicons-arrow-right-24: Build F](f-full-speed.md)

-   **G — ASUS Premium 3× Gen5**
    ---
    **€10,830.86** · with GPUs €18,551.70  
    ASUS WRX90E-SAGE · 2×64 GB 5600 · 3× Gen5 M.2 / 3 TB  
    Four Gen5 M.2, no MCIO.
    [:octicons-arrow-right-24: Build G](g-asus-premium.md)

-   **H — ASUS 4× Gen5**
    ---
    **€11,503.45** · with GPUs €19,224.29  
    ASUS WRX90E-SAGE · 2×64 GB 5600 · 4× Gen5 / 4 TB  
    4 TB all-Gen5; 8 TB HDD image.
    [:octicons-arrow-right-24: Build H](h-asus-4x-gen5.md)

-   **Used W790 bundle**
    ---
    **CHF 1,100–1,200**** · board + CPU  
    ASUS W790E-SAGE · 8ch DDR5-4800 · storage your choice  
    Cheap older 16-core platform.
    [:octicons-arrow-right-24: W790 alternative](w790-used.md)

</div>

<p class="small muted">* F uses Alternate’s notify-only €23,094 octa-kit price. Orderable at Proshop: €33,766.02 / €41,486.86 with GPUs.<br>** Board + CPU only, used; add LGA4677 cooler, RAM, storage, PSU. Ricardo price not readable; comparable eBay sold bundles.</p>

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
