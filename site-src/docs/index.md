# Four R9700s. One 128 GB VRAM box. Priced.

<div class="hero" markdown>
<span class="eyebrow">R9700 ×4 · WRX90 build book · 2026-11-06/07</span>

# The GPU budget is already spent. The platform is the decision.

Four Radeon AI PRO R9700 32 GB cards, 128 GB of VRAM, and a workstation around them. This site prices the platform, compares the boards and memory paths, and gives every part its own dossier — so you can choose the middle instead of guessing at it.

<div class="hero-meta" markdown>
<span class="chip accent">4× 32 GB = 128 GB VRAM</span>
<span class="chip">WRX90 · 8-channel</span>
<span class="chip">DDR5-6400 fast path</span>
<span class="chip">IPMI</span>
<span class="chip">EU prices</span>
</div>
</div>

## Start with the decision, not the parts list

<div class="grid cards" markdown>

-   **A — the value middle**
    ---
    **€10,418.91** platform · 3× Gen5 3 TB · 2×64 GB 5600
    All-Gen5, a full image on the 4 TB SATA, IPMI, the cheapest proper WRX90 board.
    [:octicons-arrow-right-24: Build A](builds/a-balanced.md)

-   **D — 2× now, 8× later**
    ---
    **€12,027.71** platform · 2×64 GB 6400 Micron · 3 TB Gen5
    The only literal 2×64 GB 6400 start that reaches 8×64 at full 6400 with JEDEC 2Rx4 modules.
    [:octicons-arrow-right-24: Build D](builds/d-staged-6400.md)

-   **F — 512 GB**
    ---
    **€29,057.79*** platform · 8×64 GB 6400 · 8 channels
    G.Skill’s 8-DIMM 6400 octa kit, 409.6 GB/s. The DeepSeek UD-Q8 / large-model endgame.
    [:octicons-arrow-right-24: Build F](builds/f-full-speed.md)

-   **G — the premium board**
    ---
    **€10,830.86** platform · ASUS WRX90E-SAGE SE · no MCIO
    Four Gen5 M.2, 32+3+3+3 VRM, dual-PSU, and a public 4× R9700 reference build.
    [:octicons-arrow-right-24: Build G](builds/g-asus-premium.md)

</div>

<p class="small muted">* F uses Alternate’s notify-only €23,094 price; orderable at Proshop for €33,766.02. Every platform total excludes the four owned GPUs and includes 3% contingency.</p>

## All builds

| Build | Board | Memory | Storage | Platform | With GPUs |
|---|---|---|---:|---:|---:|
| [A — Balanced 3× Gen5](builds/a-balanced.md) | ASRock WRX90 | 2×64 GB 5600 | 3× Gen5 / 3 TB | **€10,418.91** | €18,139.75 |
| [B — Capacity 6× Gen4](builds/b-capacity.md) | ASRock WRX90 | 2×64 GB 5600 | 6× Gen4 / 6 TB | €11,705.38 | €19,426.22 |
| [C — Value 4× Gen4](builds/c-value.md) | ASRock WRX90 | 2×64 GB 5600 | 4× Gen4 / 4 TB | €10,682.59 | €18,403.43 |
| [D — Staged 6400 2×64](builds/d-staged-6400.md) | ASRock WRX90 | 2×64 GB 6400 | 3× Gen5 / 3 TB | €12,027.71 | €19,748.55 |
| [E — Fast RAM 4×64](builds/e-fast-ram.md) | ASRock WRX90 | 4×64 GB 6400 | 3× Gen5 / 3 TB | €17,770.03 | €25,490.87 |
| [F — Full Speed 8×64](builds/f-full-speed.md) | ASRock WRX90 | 8×64 GB 6400 | 3× Gen5 / 3 TB | €29,057.79* | €36,778.63 |
| [G — ASUS Premium 3× Gen5](builds/g-asus-premium.md) | ASUS WRX90E-SAGE | 2×64 GB 5600 | 3× Gen5 M.2 / 3 TB | €10,830.86 | €18,551.70 |
| [H — ASUS 4× Gen5](builds/h-asus-4x-gen5.md) | ASUS WRX90E-SAGE | 2×64 GB 5600 | 4× Gen5 / 4 TB | €11,503.45 | €19,224.29 |
| [Used W790 bundle](builds/w790-used.md) | ASUS W790E-SAGE | 8ch DDR5-4800 | your choice | CHF 1,100–1,200** | — |

<p class="small muted">* Notify-only. ** Board + CPU only, used; add LGA4677 cooler, RAM, storage and PSU. See the <a href="builds/w790-used/">W790 page</a>.</p>

## The three constraints

<div class="grid cards" markdown>

-   **VRAM is fixed**
    ---
    128 GB across four cards. IQ3_S uses ≈50 GB of experts plus ≈3.5 GiB of dense weights per card; the rest is KV. The platform does not change that.

-   **Host memory is the lever**
    ---
    2×64 GB 5600 is the value floor. 2×64 GB 6400 is the staged fast path. 4×64 / 8×64 GB 6400 is where DeepSeek and 512 GB live. The [memory ladder](reference/memory-ladder.md) is the whole argument.

-   **Power connectors are the hidden limit**
    ---
    The PX-2200 has the watts, not the PCIe 8-pin count. Four GPUs consume all four PCIe cables; the board aux needs a second PSU or a different PSU. Read [Power connectors](reference/power-connectors.md) before buying anything.

</div>

## The boards in one paragraph

**ASRock WRX90 WS EVO** is the value pick: €808.05, IPMI, 3 Gen5 + 3 Gen4 NVMe ports, MCIO drives in the 2.5" bays. **ASUS WRX90E-SAGE SE** is the premium pick: €1,288.00, four Gen5 M.2, two SlimSAS, 32+3+3+3 VRM, dual-PSU, and the public 4× R9700 reference build. Both run four 2-slot GPUs at x16 in slots 1/3/5/7; slot 6 is x8 on both. The **used W790E-SAGE SE + W5-3435X** bundle is the cheap older route: 16 cores, 8-channel DDR5-4800, 112 lanes, two Gen5 M.2, 8 SATA.

[Compare the boards →](parts/asrock-wrx90-ws-evo.md){ .md-button } [ASUS board dossier →](parts/asus-wrx90e-sage-se.md){ .md-button }

## Read before ordering

!!! warning "The four-GPU power connector budget"
    Four R9700s use the PSU’s two native 12V-2x6 outputs and both 2×8-pin adapters. Those adapters consume **all four PCIe 8-pin cables**. The ASUS board still wants 2× PCIE_8P; the ASRock wants 4× 6-pin. The PX-2200 is **connector-short**. Budget a second PSU or a PSU with more PCIe 8-pin.

!!! note "The prices are a snapshot"
    EU retail, 2026-11-06/07, incl. VAT. Stock moves. The four GPUs are owned and excluded from platform totals; the “with GPUs” column is replacement value only.

!!! tip "The 6400 QVL is not proven"
    The G.Skill 2Rx4 rank is not printed on the retail listing, the ASRock/ASUS 8×64 6400 QVL is unverified, and the 512 GB training is the stress case. Confirm the module label and the board QVL before ordering.

## Reference

- [Memory ladder](reference/memory-ladder.md) — 5600 vs 6400, 2×/4×/8×, €/GB, platform totals.
- [Power connectors](reference/power-connectors.md) — the PSU cable math and the second-PSU options.
- [Storage & lanes](reference/storage-lanes.md) — Gen5 vs Gen4 arrays, port maps, lane budget.
- [Acceptance protocol](reference/validation.md) — what to measure when the hardware arrives.
- [Sources](reference/sources.md) — every price and spec link.
- [Visual summary](report.html) — the one-page report.html.

## Part dossiers

Every part in every BOM has a page with its own description, specification table, pros, cons and the builds it appears in.

[Open the part index →](parts/index.md){ .md-button .md-button--primary }
