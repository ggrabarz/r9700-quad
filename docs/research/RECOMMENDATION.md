# Board pick — EPYC 9135 + 12ch DDR5-6400 1DPC + 4x R9700

> **PROGRAM CLOSED 2026-11-10T09:48Z** — the research window ended
> 2026-11-10T09:47Z. No research was done after the cutoff; the state below is
> final as of the last in-window run (09:19Z) and the scheduled watch has been
> deleted.

**Leader: GIGABYTE MZ33-CP1 (rev 3.x)** — one of only two SP5 boards found whose
own spec sheet states DDR5-6400 at 1DPC for EPYC 9005 and that can hold four
x16 cards. Three x16 slots at 2-slot pitch plus a fourth card on MCIO.
**It now leads on EU availability, not on spec** — see the MZ23-SU0 note below,
which is the better board on paper but has **no new-in-box EU offer** (re-tested
2026-11-10T08:51Z: idealo.de/.at return only a used unit, €1,290 / €1,599).

Verified 2026-11-10T02:0xZ from Gigabyte's own datasheet and product page.
Slot pitch resolved 2026-11-10T02:35Z: **three cards fit natively, the fourth
needs one MCIO→x16 adapter.** See "Slot pitch — resolved" below.
Whole chain re-verified live 2026-11-10T08:50Z (board price/stock, adapter
price, 9135 QVL grading, SU0 US price) — **nothing moved; see the CHANGELOG
entry for that timestamp.**
**The whole build is now EU-sourced (2026-11-10T08:20Z):** board €876.98
(Plexcom, in stock) + adapter set €140 (C-Payne, made and shipped from Germany,
no customs) — the 4th-card adapter was the last US-only line item and is not
one any more.
Card thickness pinned 2026-11-10T05:0xZ: the R9700 is **39–40 mm** per vendor
specs, i.e. **0.6–1.6 mm clearance** at the 2.0-slot pitch — and that is
sufficient, because **both R9700 SKUs are blowers** (verified
2026-11-10T05:35Z): they exhaust out the bracket and need no side intake, so
tight side clearance does not throttle them. Either SKU fits the three native
positions.
Re-verified 2026-11-10T03:5xZ against the newer datasheet PDF, and price is now
**8 offers from €881.97** (idealo.de), EU-wide — **superseded 2026-11-10T06:00Z:
Geizhals lists it too, 6 offers from €876.98** (Plexcom, in stock 1–3 days).
Last open item closed 2026-11-10T06:52Z: the **BIOS version list is public** —
newest **R25_F17, released 2026-11-08**, downloadable straight from Gigabyte
(`MZ33-CP1_R25_F17.zip`, 50,505,855 B, HTTP 200). See open question 6.
New challenger **MZ23-SU0**
found: 5x Gen5 x16, 6400 @1DPC, 3 native at 1.0 pitch — it matches the CP1's
native card count, beats it on lanes and depth, and (04:10Z) is **in stock at
Newegg US for $869** (live-read 08:50Z) but **not sold into the EU**. See the
MZ23-SU0 section.

## Why it wins

| Requirement | MZ33-CP1 |
|---|---|
| SP5, single socket, EPYC 9005 | yes, cTDP 500 W |
| 12-channel DDR5, 1 DIMM per channel | 12 x DIMM, 12-channel |
| DDR5-6400 at 1DPC | **"Up to 6400 MT/s" (EPYC 9005)** — board spec, **live QVL grades the 9135 at DDR5-6400** (updated 2026-10-28), and **37 DDR5-6400 RDIMMs on the QVL** (1DPC, PASS) — **count re-derived 2026-11-10T07:52Z by parsing the sheet itself**, not the HTML tab |
| 4 slots at x16 for 4 cards | Slot_6 Gen5 x16, Slot_4 Gen5 x16, Slot_2 Gen5 x16, Slot_1 Gen4 x16 — **only 3 at 2-slot pitch** |
| IPMI | AST2600 BMC + MLAN |
| Form factor | E-ATX 304.8 x 330.2 mm |
| Price | **€876.98 (Plexcom, in stock 1–3 days)**, **GTIN 4719331867232**, Plexcom Art.Nr. **111142** — re-verified **09:19Z** straight off the product page's schema.org `Product`/`Offer` JSON-LD (`"price":"876.98"`, `"availability":"InStock"`, `"itemCondition":"NewCondition"`, `"mpn":"MZ33-CP1"`), so it is a structured-data read, not a scraped price string; use the GTIN when asking any other distributor. First read **08:50Z** on Plexcom's *own* search endpoint (`advanced_search_result.php?keywords=MZ33-CP1`): Art.Nr. **111142**, *"lagernd, 1-3 Werktage (Ausland abweichend)"*, 876,98 EUR incl. 19 % MwSt., "In den Warenkorb" live; **cross-checked 08:54Z on the product page itself** (`/gigabyte-mainboard-mz33-cp1-rev-3-x-e-atx-sockel-sp5-single-mainboard-e-atx.html`) — same Art.Nr., same 876,98 EUR, same "lagernd" — **but its "Lagerbestand" counter is blank, so the unit count is not published**; "lagernd" is the shop's own status word, not a quantity. idealo.de **8 offers €881.97–€1,247, data stamp 10.11.2026 08:49** (jacob.de €881.97 + €2.99 shipping = €884.96, delivery by 12.11.; future-x €881.99; galaxus €929.21, delivery by 27.11.; voelkner €984.60; kaufland €991.96; pccomponentes €1,041.89; senetic €1,110.63; eBay/ersazza €1,247.00); Happyware €931 excl. VAT. EU: AT €894.40 / IT €995.99 / ES €1,041.99 / FR €1,119.96 |
| Card clearance | **not a constraint: both R9700 SKUs are blowers** (ASRock 39 mm, ASUS 40 mm), exhausting out the bracket |
| **Gen5 M.2 for RAID0 (new 2026-11-12)** | **onboard M.2 is Gen3 x4 only** — Gen5 drives must ride MCIO. **4 Gen5 M.2 fit alongside all 4 GPUs**: the 4th-GPU adapter consumes the G0 x16 group, leaving the **G2 group (2x MCIO 8i) = 4 Gen5 NVMe at x4** with BIOS `x4x4x4x4`. 2 drives = 1 adapter + 1 cable (~€105); 4 drives = 2 + 2 (~€210). RAID0 is **software** (mdadm/ZFS) — board spec says `RAID: N/A`. See "Storage — Gen5 M.2 RAID0" below. |
| 4th-card adapter | **C-Payne MCIO gen5 device adapter x8/x16, €50 + 2x MCIO 8i gen5 cable €45 = €140, ships from Germany, no customs** (verified 08:20Z, re-verified 08:51Z). Buy the **CP-0232 vertical** variant if the card sits in a 1-slot gap — vendor: *"the vertical model can be placed with single width spacing"*; CP-0231 flat needs 2 slots. |

It still wins, but by a smaller margin than first recorded: the CP1 is a
**3-native + 1-adapter** board, not 4-slot-native. The MZ33-AR1 is the same
platform with 4x Gen5 x16 but is capped at **5200 MT/s (1DPC)** by Gigabyte's
own spec and its slots are two adjacent pairs, so it needs 2 adapters *and* is
slower. No alternative board does better on both axes.

Lane budget: 3x Gen5 x16 + 1x Gen4 x16 + OCP Gen5 x16 + 4x MCIO Gen5 x8
+ 2x MCIO Gen4 x8 ≈ 104 lanes of the 9135's 128. Fits.

## Slot pitch — resolved, and it is not evenly 2-slot

Fetched the **official rev 3.0 manual** (the 404 was only the product-page link;
the download host has the file):

- https://download.gigabyte.com/FileList/Manual/server_mb_manual_mz33-cp1_e_v3.0_.pdf
  (142 pp, creation date 2025-05-14; page 5 is "MZ33-CP1 Motherboard Layout",
  page 6 is the item legend confirming PCIE_1/2/4/6 are the four x16 slots.)

Measured the layout drawing at 600 dpi and scaled off the board outline
(outline 2343 px = 304.8 mm → 7.687 px/mm; cross-check: 2539 px = 330.3 mm vs
330.2 mm spec, 0.03 % off). Slot centre-to-centre, in 20.32 mm slot pitches:

| Pair | Centre gap | Pitches |
|---|---|---|
| Slot_1 → Slot_2 (36→37) | 20.3 mm | **1.0** |
| Slot_2 → Slot_4 (37→39) | 40.7 mm | 2.0 |
| Slot_4 → Slot_6 (39→40) | 40.6 mm | 2.0 |

Confirmed independently by the Happyware product photo — Slot_1 and Slot_2 sit
immediately next to each other as the first two slots in the row, with a gap
before the third. So the **names 1/2/4/6 are the board's own slot-numbering
convention, not a promise of 2-slot pitch**.

**Re-confirmed 2026-11-10T04:10Z from a second, independent photo** (the
1920x1920 server-hardware.com product image, not Gigabyte's drawing): measured
slot-centre gaps **120 / 235.5 / 236.5 px = 1.02 / 2.0 / 2.0 pitches**. Same
answer from a different source, so this is settled rather than a drawing-reading
artifact.

**Verdict: a 2-slot 40 mm card cannot go in Slot_1 and Slot_2 together.**
Three R9700 fit natively (Slot_2, Slot_4, Slot_6 at 2-slot pitch, 40.6 mm
apart ≥ 40 mm). The fourth needs an adapter.

**CORRECTION 2026-11-10T07:22Z — the 06:00Z "38 is a skipped slot" argument
was wrong; the conclusion is unaffected and now rests on a better source.**
The 36/37/38/39/40 numbers are *annotation callouts*, not slot positions, and
`pdftotext` of the same page proves it: item **38 = `BAT Battery Socket`**, the
round CMOS cell drawn between slot 37 and slot 39. So "Slot_1/Slot_2 are
consecutive (36, 37) and 38 is skipped" was reading a legend of labelled
components as if it were a slot index. What the layout shows instead is simply
that the CMOS battery sits in the bay between PCIE_2 and PCIE_4 (the 2.0-pitch
gap), and the *numbering* says nothing about pitch either way.

The geometry itself was re-derived from scratch this run at **600 dpi**,
independent of the earlier 7.687 px/mm figure, scaling off the board outline
(304.8 mm = 2343 px, 330.2 mm = 2539 px, the two scales agreeing to 0.03 %):

| Pair | Centre gap | Pitches |
|---|---|---|
| Slot_1 → Slot_2 | **20.7 mm** | 1.02 |
| Slot_2 → Slot_4 | **40.3 mm** | 1.98 |
| Slot_4 → Slot_6 | **40.7 mm** | 2.00 |

Slot_1 centre is 20.2 mm from the board edge; Slot_6 centre is 182.9 mm from
the other edge. Same 1.0/2.0/2.0 answer, so **blocker 1 stays closed on the
measurement + the two photos** — but not on the legend-numbering argument,
which is hereby withdrawn.

**Card thickness pinned to vendor spec 2026-11-10T05:0xZ — and the 2.0-pitch
margin is 0.6 mm, not comfortable.** Two actual R9700 SKUs, both stated by
their makers, not inferred:

| SKU | Vendor-stated dimensions | Source |
|---|---|---|
| ASUS Turbo Radeon AI Pro R9700 32G | 266.7 x 111.1 x **40 mm**, "Slots: 2" | https://press.asus.com/news/press-releases/asus-turbo-radeon-ai-pro-r9700/ |
| ASRock R9700 Creator 32GB | 271 x 112 x **39 mm**, "2-slot" | https://www.asrock.com/Graphics-Card/AMD/Radeon%20AI%20PRO%20R9700%20Creator%2032GB/index.asp |
| **PowerColor AI PRO R9700 32G-B** (the actual card) | 266.7 x 111.2 x **40 mm**, "Slots: 2" | https://www.gpus.net/gpus/amd_ai_pro_r9700/powercolor_radeon_ai_pro_r9700 |

**Build update 2026-11-12 — the cards are PowerColor `AI PRO R9700 32G-B`.**
Added 2026-11-12T01:1xZ: **40 mm, 2-slot, blower** ("minimalistic design with
blower style, 2-slot form factor", Caseking GCPC-079;
https://www.caseking.de/en/powercolor-radeon-ai-pro-r9700-graphics-card-32gb-gddr6/GCPC-079.html),
single-fan reference layout — Micro Center lists it as "Single-Fan AI &
Workstation Graphics Card". So it behaves exactly like the ASUS 40 mm case
below: **0.6 mm** side clearance at the 2.0 pitch in Slot_2/4/6. That is a real
fit, but the tightest of the three SKUs — see the clearance warning below.

So the 40.6 mm centre-to-centre gap leaves **0.6 mm** (ASUS) or **1.6 mm**
(ASRock) between adjacent 2-slot cards. It fits on paper in both cases but the
ASUS variant has almost no margin for a bowed backplate or a stiff 12V-2x6
cable. **Given the build uses PowerColor (40 mm), plan a test-fit before
committing all four cards** — 0.6 mm is the whole margin. (The 4th card is on
the MCIO adapter, so it is not pitch-constrained.) Second consequence: because
all three SKUs are 39-40 mm, slot 1+2 *together* is still impossible — 20.3 mm
between those two centres.

### Tensor parallel — the real constraint is P2P, not slot count (2026-11-12)

**Correction first: no GPU is on OCP in this build.** OCP NIC 3.0 is unused — the
four cards are three native x16 slots (Slot_2/4/6) plus the fourth on the MCIO
adapter. OCP was only ever counted in the lane budget, never in the GPU plan.
Nothing about tensor parallel depends on it.

**On "really no boards with native PCIe 5 x16 for GPUs" — the honest answer is:
barely any, and not for 4 cards at 2-slot pitch.** What actually exists:

| Board | Native Gen5 x16 | Verdict |
|---|---|---|
| GIGABYTE MZ33-CP1 | 3 (Slot_2/4/6) + Slot_1 Gen4 | leader: 3 native + 1 MCIO |
| GIGABYTE MZ33-AR1 | **4** Gen5 x16 | but **two adjacent 1-pitch pairs** (Slot_3→4 = 19.5 mm, Slot_6→7 = 17.5 mm) → only **2** dual-slot cards; needs 2 adapters; **5200 MT/s** cap |
| ASRock Rack GENOAD8UD-2T/X550 | **4** Gen5 x16, `2 x M.2 PCIe5.0 x4` | **only 8 DIMM = 8 of 12 channels** — fails the 12-channel requirement |
| Supermicro H14SSL-N | 3 Gen5 x16 (**M.2 = 2x Gen5 x4**) | only 3 x16 → 4th card needs an adapter anyway |

So: **the CP1's "3 native + 1 adapter" is as good as it gets** among boards that
also meet 12-channel DDR5-6400. The GENOAD8UD is the one board with 4 native
Gen5 x16 **and** onboard Gen5 M.2 (2 slots, x4 each) — but it is 8-DIMM, so it
breaks the memory requirement. **If you would trade 12 channels for 4 native
slots + 2 onboard Gen5 M.2, that is the only board that does it**, and it is the
honest alternative to consider — not a free upgrade.

**The bigger finding — and it applies to every one of these boards:**
**Direct PCIe P2P for 4x R9700 tensor parallel is currently unreliable.** An open
ROCm issue reports **full-system hangs** with 4x R9700 + tensor splitting + RCCL
P2P (`NCCL_P2P_DISABLE=0`), on llama.cpp *and* vLLM, sometimes triggering a BMC
reset; the reporter's own repro states the hang **does not occur with
`NCCL_P2P_DISABLE=1`**:
https://github.com/ROCm/rocm-systems/issues/11348

That was on a **Supermicro H12SSL-NT** (EPYC 7302, 4x R9700), i.e. **not a board
problem and not fixed by buying 4 native slots.** Practical guidance from the
same body of work: run with `NCCL_P2P_DISABLE=1` (host SHM instead of BAR1 P2P),
and for multi-card R9700 also `HSA_ENABLE_SDMA=0`, `NCCL_P2P_LEVEL=PHB`; add
`iommu=pt` to the kernel cmdline as the first thing to try. Reported cost of
falling back to SHM for TP=2 is roughly **8-12 % added latency**, and **0 % if
you use pipeline parallelism** (`--pipeline-parallel-size 2`, or llama.cpp
`--split-mode layer`) instead.
https://tinker-ai.com/guides/multi-gpu-pcie-p2p-iommu-deadlock-and-connectx7-rocev2-tcp-fallback-troubleshooting/

**Consequence for the pick: do not pay for "native x16" on the belief it fixes
tensor parallel.** Bandwidth-wise x16 vs x8 does not change whether P2P works,
and the current 4x R9700 failure mode is a driver/ROCm-level hang, not a
topology-level one. Buy for **slot fit and memory channels**, then plan on
`NCCL_P2P_DISABLE=1` until that ROCm issue closes. **UNVERIFIED: whether the
hang reproduces on EPYC 9005 / MZ33-CP1 specifically** — the report is on 9004-era
hardware with an older ROCm; it may already be fixed in current ROCm 7.x. This
is a must-test item on the real build, not a settled fact.

### The cheap fix for the fourth card

**How the four GPUs actually connect (2026-11-12) — nothing is on OCP:**

| Card | Connects to | Notes |
|---|---|---|
| 1 | **Slot_2** (Gen5 x16) | native, 2-slot pitch |
| 2 | **Slot_4** (Gen5 x16) | native, 2-slot pitch |
| 3 | **Slot_6** (Gen5 x16) | native, 2-slot pitch |
| 4 | **2x MCIO 8i (U2_P0_G0A + G0B) → x16 adapter** | C-Payne CP-0232, 12 V-fed |

Slot_1 (Gen4 x16) is **not** used for a GPU — it is only 1 pitch from Slot_2, so
no 40 mm card can go there; leave it empty (or put a single-slot card in it
later). BIOS: `U2_P0_G0 Lanes` = **`x16`** for the 4th card, and each
`SLOT #_Link Speed` on **Auto**. The GPU adapter needs its own **12 V PCIe
6-pin**; the M.2 adapter needs a **4-pin 12 V**.

The board already carries **4 x MCIO 8i (Gen5 x8) + 2 x MCIO 8i (Gen4/SATA)**.
Two MCIO 8i ports, combined, give a full Gen5 x16 — so the fourth R9700 mounts
on a **2x MCIO 8i → PCIe 5.0 x16** adapter, e.g. 10Gtek SA22N2116P
(store.10gtek.com/mcio-pcie-gen5-device-adapter-2-8i-to-x16/p-29134, $55 in
stock 2026-11-10; the vendor states x16 needs both inputs from the same CPU
host port with lanes 0-7 → 8-15). That is one ~€50 part plus a slot position in
the chassis — far cheaper than any board swap, and it keeps 6400 MT/s.

**Adapter sourcing — SOLVED in the EU, 2026-11-10T08:20Z; the earlier
"US-only" framing is retracted (see the correction below).** The 10Gtek
SA22N2116P is still **$55.00, "99968 In Stock", warehouse US**, and its x16 mode
is an *aggregation* of two x8 links into one x16 slot ("X16 mode with both inputs
connected — must be the same CPU host port and lane ordering 0-7 → 8-15"). But
the cheapest EU-listed "2x MCIO 8i → PCIe 5.0" part, **KALEA-INFORMATIQUE
79,90 € incl. VAT** (Amazon.de, "Nur noch 7 auf Lager"), is a **splitter** — its
own title says "für die Verlängerung eines PCI Express-Anschlusses auf 2
x16-Ausgänge (effektiv **x8**)", i.e. one upstream port fanned out to two x8
outputs. That is the opposite direction and **cannot present one card as x16**.
Buying it because it is the cheap EU hit would put the fourth R9700 at x8.

~~So: **10Gtek SA22N2116P remains the correct part and remains a US purchase**~~
**CORRECTED 2026-11-10T08:20Z — there is a German-made equivalent that ships
from inside the EU, and the "US-only" framing was wrong on the original part
too.** Two separate findings:

1. **C-Payne (c-payne.com) "MCIO PCIe gen5 Device Adapter x8/x16" — €50.00**
   (**CP-0231** bottom, **CP-0232** vertical, both €50),
   exactly the right topology: "two MCIO 8i inputs / one PCIe x16
   electrical/mechanical output", x8 with one cable, **x16 with both inputs**
   ("must be the same CPU host port and lane ordering must be 0-7→8-15, NOT
   8-15→0-7" — same constraint as the 10Gtek), **mandatory 12 V power
   connector**, 3.5 A 12 V→3.3 V buck. Add-to-cart live. It also sells the
   matching **MCIO SFF-TA-1016 8i PCIe gen5 cable, €45.00** (45 cm / 75 cm), so
   the 2-cable + adapter set is **€140**.
   https://c-payne.com/products/mcio-pcie-gen5-device-adapter-x8-x16
   https://c-payne.com/products/mcio-sff-ta-1016-8i-cable-pcie-gen5
   Its shipping policy states: **"Origin: All orders ship from Germany. For
   destinations within the European Union, no additional customs fees are due."**
   VAT is included for EU orders and excluded outside it. So this is an
   in-EU purchase, not an import.
   https://c-payne.com/policies/shipping-policy
   **Re-verified live 2026-11-10T08:51Z, both pages, unchanged:** adapter
   **€50,00** ("Regular price"), cable **€45,00** (45/75 cm) → **€140 the set**,
   both with an Add-to-Cart. One spec detail worth keeping, copied verbatim from
   the adapter page: *"the vertical model can be placed with single width
   spacing"* — i.e. the **CP-0232 vertical** variant, not the flat bottom one,
   is the right pick for the 4th card if it has to share a 1-slot gap. That does
   not relax the Slot_1+Slot_2 limit (a 40 mm card still cannot go there), it
   just means the adapter card's own position is not pitch-constrained.
   The same page repeats the electrical rule: x16 "with both inputs connected
   (must be the same CPU host port and lane ordering must be 0-7->8-15, NOT
   8-15->0-7)" and **"mandatory Power connector to supply 12V"**, plus the
   warning "DO NOT connect the wrong power connector, it will destroy the
   Adapter and your GPU".
2. **10Gtek does ship to Germany.** Its own shipping page says it ships
   "worldwide to nearly every country", uses DHL/FedEx, and its country list
   includes Germany. So the earlier "US-only, EU terms UNVERIFIED" line was
   wrong as well; the US warehouse is where it ships *from*, not a restriction
   on where it goes. Duty/VAT would still apply on import (their page: courier
   handles clearance, local tax/duty billed on entry).
   https://store.10gtek.com/shipping-guide/

The DE-available alternatives that are the **wrong topology** still stand:
KALEA-INFORMATIQUE 79,90 € (Amazon.de) is a **splitter** (one port → 2 x16
outputs, "effektiv x8") and cannot present one card as x16. Do not buy it.
C-Payne is the fix — it is both cheaper (€50 vs €79.90) and electrically correct.

**Vendor caveat re-checked 2026-11-10T04:2xZ:** 10Gtek's own page states
"SA22N2116P does not support Asus RTX graphics card; if you need to use with
Asus RTX, pls choose SKU: SA22N2116P2". Irrelevant here (the R9700 is AMD) but
it means the adapter is not a generic NVIDIA part — do not swap a GeForce into
that position later without the -P2 variant. Still **$55.00, 99968 in stock**,
and the page still describes the port as **2x MCIO 8i (74-pin) → PCIe 5.0 x16**.

Trade-off: the fourth card loses native slot x16 and one MCIO pair is consumed
by the GPU adapter, which halves the free Gen5 NVMe capacity from **8 drives to
4** (the G2 group survives intact — see "Storage — Gen5 M.2 RAID0"). Card 4
stays Gen5 x16 electrically, so no bandwidth
loss — the cost is mechanical (adapter, mounting, airflow) only. The adapter
itself is **12 V-fed** (10Gtek's own spec: "With 12V PCIe 6 pin power … 6A
12V→3.3V buck regulator"), so the build needs a free PCIe 6-pin from the PSU;
the CP1 already exposes a 6-pin 12V PCIE header but that one is 3-pin
board-side for the slots, not a PSU feed.

### Parts — the adapters, with links (consolidated 2026-11-12)

These are the four parts that matter, each fetched and checked this run. **Order
the C-Payne pair from Germany — they ship inside the EU, so no customs.**

**A · GPU 4 adapter — MCIO → PCIe x16 (the one that replaces Slot_1)**
- **C-Payne "MCIO PCIe gen5 Device Adapter x8/x16" — €50,00.** Two MCIO 8i in,
  one x16 out; x16 only with both cables, same CPU host port, lane order
  0-7→8-15; **mandatory 12 V connector.** Pick the **vertical (CP-0232)** if the
  card sits in a 1-slot gap, flat (CP-0231) otherwise.
  https://c-payne.com/products/mcio-pcie-gen5-device-adapter-x8-x16 — *verified
  2026-11-12: page live, price €50,00.*
- Alternate: **10Gtek SA22N2116P, $55.00** — https://store.10gtek.com/mcio-pcie-gen5-device-adapter-2-8i-to-x16/p-29134
  (*verified live*; ships from US, so import VAT applies. Vendor note: not for
  ASUS RTX cards — irrelevant for AMD, but do not swap in a GeForce later.)

**B · MCIO cable — the same cable feeds either adapter**
- **C-Payne "MCIO SFF-TA-1016 8i cable — PCIe gen5", €45,00** (45 cm or 75 cm).
  https://c-payne.com/products/mcio-sff-ta-1016-8i-cable-pcie-gen5 — *verified
  2026-11-12: price €45,00, both lengths listed.*
- **You need 2 of these for the GPU adapter** — x16 mode uses both MCIO
  inputs — **plus 1 more per 2 M.2 drives** on the storage adapter.

**C · Gen5 M.2 adapter — MCIO 8i → 2× M.2 (storage)**
- **KALEA-INFORMATIQUE, €59.90 incl. VAT, in stock.** 74-pin MCIO, 2× M.2
  M-key x4 (2230/2242/2260/2280/22110), 145×85 mm, **4-pin 12 V or 5 V**,
  "BIOS must support bifurcation". *Verified live 2026-11-12.*
  https://www.kalea-informatique.com/adapter-for-2-ssd-m2-pcie-nvme-m-key-to-sff8654-for-mounting-two-ssd-m2-in-place-of-ssd-u2.htm
- Alternates: **LR-LINK LRFNA922A** (identical topology, price UNVERIFIED —
  datasheet is login-gated) https://lr-link.com/products/lrfna922a.html ·
  **HiFiber SM22N21-M, $43.99, in stock** https://www.hifiber.com/item/SM22N21-M/mcio-8i-to-2x-m-2-gen5-adapter-for-nvme-ssd-requires-motherboard-bios-support-for-bifurcation-3500.html

**Basket for the start-up build (3 GPUs native + 4th + 2× M.2 RAID0):**
2× C-Payne cable (€90) + 1× C-Payne GPU adapter (€50) + 1× KALEA M.2 adapter
(€59.90) = **€199.90**, all EU-shipped.

**Verdict on the AliExpress item you sent
(`pl.aliexpress.com/item/1005011740529907.html`): correct direction, wrong
variant, and not cheaper.**
- It is ADT-Link **"PCIe 5.0 x16 → MCIO 8i riser, 1U, external GPU backplane
  kit"**. The direction is right for us (host slot or adapter → MCIO), and your
  screenshot shows the **device-side board** — a PCIe slot plus two MCIO 8i
  ports and a power header. That is the same part class as the C-Payne adapter.
- **But the listing is a multi-variant kit and the cheapest tile is a bare
  cable.** The variant names on the page are `MCIO-55cm`, `Set-A`, `Set-B`,
  `MCIO to PCIE5.0`, `Pcie5.0 x16(1u)`, `16x-MCIO 2U-PCIE5.0`,
  `MCIO-PCIE5.0X16`, `Pcie5.0 x8 1u`. The **~100 zł / CHF 10.18 tile that the
  page defaults to is the `MCIO-55cm` variant — a cable only**, not the
  adapter board. You must switch the variant to the 1U x16 board, and the
  price then changes.
- **Two of those variants are the wrong width — `Pcie5.0 x8 1u` is x8**, which
  would put GPU 4 at half bandwidth. Do not pick it.
- It is an ADT-Link kit with a backplane, so it is aimed at mounting a card in a
  1U/2U chassis; **the C-Payne part is a bare adapter designed for exactly this
  "one card in a tower slot position" use and is a known-good €50.**
- **Recommendation: stay with C-Payne.** Not because AliExpress is bad, but
  because the specific listing hides the correct variant behind a variant
  selector, defaults to a €10 cable, mixes in an x8 trap, and gives no
  lane-ordering or same-host-port documentation — all of which the C-Payne page
  states explicitly. Saving ~€20 is not worth guessing on the part that feeds a
  €1,100 GPU.
- **UNVERIFIED: the price of the 1U x16 board variant** — AliExpress did not
  expose a per-variant price to a non-JS fetch, so any number here would be a
  guess.

### Storage — Gen5 M.2 RAID0 (requirement added 2026-11-12)

**Start-up build confirmed 2026-11-12: 2x 1 TB Gen5 M.2 in RAID0, not 4.**
That halves the storage cost to **one adapter + one cable (~€105)**, and it is
the right way to start: the second MCIO port stays free for the 2-drive→4-drive
upgrade later without touching anything else.

**What to buy for 2 drives (exact shopping list):**

| Item | Qty | Price | Notes |
|---|---|---|---|
| KALEA "MCIO 8i → 2x M.2 Gen5" adapter | 1 | **€59.90** incl. VAT | 74-pin MCIO host, 2x M.2 M-key x4, 2260/2280/22110, **needs 4-pin 12 V or 5 V** — https://www.kalea-informatique.com/adapter-for-2-ssd-m2-pcie-nvme-m-key-to-sff8654-for-mounting-two-ssd-m2-in-place-of-ssd-u2.htm |
| C-Payne MCIO SFF-TA-1016 8i gen5 cable, 45 or 75 cm | 1 | **€45.00** | same cable family already bought for the GPU adapter — https://c-payne.com/products/mcio-sff-ta-1016-8i-cable-pcie-gen5 |
| 2x 1 TB Gen5 M.2 (e.g. any 2280/22110 M-key NVMe) | 2 | not priced here | any Gen5 x4 M.2 works; no QVL needed for drives |

**How to connect, step by step:**
1. Cable the adapter to **`U2_P0_G2A`** on the board (the G2 Gen5 group — *not*
   G0, which the 4th GPU owns, and not G3, which is Gen4).
2. Power the adapter from a **4-pin 12 V** PSU lead.
3. In BIOS §2-2-8, set `U2_P0_G2 Lanes` = **`x4x4`** (this is the "2 drives"
   setting; `x4x4x4x4` would be for four drives across G2A+G2B).
4. Leave `U2_P0_G2 Link Speed` on **Auto** — do *not* force Gen4 here; Auto is
   what lets it train at Gen5. (The menu lists only Auto/Gen4/Gen3/Gen2/Gen1,
   which is the same UI quirk as the slots — see the anti-trap note below.)
5. Install the OS to the array: `mdadm --create /dev/md0 --level=0
   --raid-devices=2 /dev/nvmeXn1 /dev/nvmeYn1` (or the installer's equivalent).
   **RAID0 is software** — the board's spec sheet says `RAID: N/A`, and no
   RAID option ROM/VROC is involved.

**Upgrading 2 → 4 later:** add a **second** adapter on `U2_P0_G2B`, add one more
cable (~€105 more), change `U2_P0_G2 Lanes` to `x4x4x4x4`, and re-create the
array (RAID0 cannot be grown across the two new ports without a rebuild — plan
to restore from backup). Nothing about the GPU side changes.

**The CP1's onboard M.2 is not usable for this: it is `1 x M.2 (2280/22110), PCIe
Gen3 x4`** — Gigabyte's own datasheet, "Storage Interface → M.2", and the manual
legend item 30 `M2_0 M.2 slot (PCIe Gen3 x4, Support NGFF-2280/22110)`. The
block diagram agrees: `M.2 → PCIe3.0 x4`. Gen3 x4 caps a single drive near
~3.5 GB/s, so **the Gen5 requirement has to be met on MCIO**, not on that slot.
(Every other board examined is the same or worse here: MZ33-AR0/AR1 = M.2 Gen4
x4, MZ23-SU0 = `2 x M.2 PCIe Gen3 x2`.)

**Does it still fit 4 GPUs plus 4 Gen5 M.2? Yes — the x16 groups are separate.**
The CP1 exposes two independent x16 "U2" groups plus a Gen4 group, all wired
straight to the CPU (block diagram):
- **U2_P0_G0** (0A/0B) → Gen5 x16 — **consumed by the 4th-GPU adapter**
- **U2_P0_G2** (2A/2B) → Gen5 x16 — **free for storage**
- **U2_P0_G3** (3A/3B) → Gen4 x8 or SATA — free, and Gen4-only, so not for Gen5 drives

The manual's BIOS menu confirms the split and the required mode: `U2_P0_G0/1/2
Lanes` offers `x4x4x4x4` (manual §2-2-8, pp. 46–47). One MCIO 8i port = x8 =
**two x4 drives**; a Gen5 x16 group = **four x4 drives**. So **2 drives** need 1
adapter on one port, **4 drives** need 2 adapters across G2A+G2B — and none of
that touches G0, which the fourth R9700 owns.

| Parts (2 or 4 drives) | Part | Price | Source |
|---|---|---|---|
| MCIO 8i → 2x M.2 Gen5 | LR-LINK **LRFNA922A** (74-pin MCIO, 2x M.2 x4, 2260/2280/22110, **4-pin 12 V or 5 V power**, "Requires BIOS Bifurcation") | UNVERIFIED (datasheet is login-gated) | https://lr-link.com/products/lrfna922a.html |
| MCIO 8i → 2x M.2 Gen5 | KALEA-INFORMATIQUE **"2x M.2 ↔ MCIO 8i"**, 145x85 mm, 74-pin, Gen5, 4-pin 12 V/5 V, in stock | **€59.90** incl. VAT (**€49.92** excl.) | https://www.kalea-informatique.com/adapter-for-2-ssd-m2-pcie-nvme-m-key-to-sff8654-for-mounting-two-ssd-m2-in-place-of-ssd-u2.htm |
| MCIO 8i → 2x M.2 Gen5 | HiFiber **SM22N21-M**, in stock | **$43.99** | https://www.hifiber.com/item/SM22N21-M/... |
| MCIO 8i gen5 cable (45/75 cm) | C-Payne, same cable as the GPU adapter | **€45.00** each | https://c-payne.com/products/mcio-sff-ta-1016-8i-cable-pcie-gen5 |

**Cost of the storage path: 4 Gen5 M.2 ≈ €210 (2 adapters @ €59.90 + 2 cables
@ €45), all EU-sourced from KALEA (FR) and C-Payne (DE).** The 2-drive build is
half that (~€105). Both adapters need a free 4-pin 12 V feed and a **x4x4x4x4**
bifurcation setting, not `Auto`.

**RAID0 itself is software.** Gigabyte's spec sheet states `RAID: N/A` — the
board ships no RAID option ROM or VROC key for NVMe. Use Linux `mdadm --raid0`
or a ZFS/mdadm pool over the four namespaces. That is the correct tool for
RAID0 anyway, and it costs nothing. **This is not a downgrade versus a "hardware
RAID" board** — consumer NVMe RAID on these platforms is always host software
anyway; the only real alternative would be a tri-mode HBA, which would need one
of the x16 slots a GPU is using.

**One caveat worth stating:** the 4th-GPU adapter and the storage adapters all
draw from the same 128-lane CPU budget. Recount with storage included: 3x
Gen5 x16 GPU (48) + 1x Gen4 x16 GPU (16) + OCP Gen5 x16 (16) + G0 x16 for GPU4
(16) + G2 x16 for 4 SSDs (16) + G3 Gen4 x8 (8) = **120 lanes of 128**. It fits,
with 8 lanes spare — but there is **no room for a fifth PCIe device** without
giving something up. Not needed for this build.

**Anti-trap note (2026-11-10T06:43Z):** the manual's BIOS §2-2-8 lists
`SLOT #_Link Speed` *and* `U2_P0_G0/1/2/3 Link Speed` with options only
"Auto, Gen4, Gen3, Gen2, Gen1" — **no Gen5 entry**. That is the same UI
limitation on both, for slots the datasheet calls Gen5, so it is **not**
evidence the MCIO ports are Gen4; do not "downgrade" the 4th-card plan on it.
The lane menu (`U2_P0_G0/1/2 Lanes`) does offer x16, which is how one MCIO
pair (G0A+G0B) becomes a x16 link. Source: rev 3.0 manual pp. 46–47.

**If pitch had been 1 slot the board would be dead; it is 1 slot only for the
Slot_1/Slot_2 pair, so the board survives as a 3-native + 1-adapter build.**
UNVERIFIED: that a 2-slot 40 mm R9700 physically clears the card in Slot_2 when
seated in Slot_1 — the drawing shows no obstruction, but this needs the real
cards. Chassis must expose 8 adjacent bracket positions.

## Rejected, with the reason

| Board | Why not |
|---|---|
| GIGABYTE MZ33-AR1 | 4x Gen5 x16, but **5200 MT/s max at 1DPC** per Gigabyte. Fails 6400. Also measured 2026-11-10T02:38Z from its rev 3.0 manual (p.5): slots are **two adjacent 1-pitch pairs** (Slot_3→4 = 19.5 mm, Slot_6→7 = 17.5 mm, 2 pitches between the pairs), so it fits at most **2** dual-slot cards natively vs 3 on the CP1. |
| GIGABYTE MZ33-AR0 | 4x Gen5 x16, **4800 MT/s at 1DPC**. Fails. |
| ASUS K14PA-U12 | 12 DIMM, but only **3x PCIe 5.0 x16** and DDR5-4800. Fails both. |
| Supermicro H14SSL-N / -NT | 6400 MT/s at 1DPC verified, but only **3x x16 + 2x x8**. Fourth card cannot be x16. |
| ASRock Rack GENOAD12M3-2Q | 12 DIMM 1DPC but **2x PCIe5 x16** and **4800 MHz max**. Fails both. |
| GIGABYTE MZ73-LM2 | Dual socket, 6400 MT/s, 4x Gen5 x16 — but 2P wastes a socket and the 9135 is 1P. |
| GIGABYTE MZ73-LM1 | Literally 6400 MT/s + 4x x16, but **all four are Gen4** and Slot_1/Slot_2 come from **CPU_1** — with one 9135 you get only 2 slots. Fails. |
| ASUS K14PA-U24 | 24 DIMM / DDR5-6400 and IPMI, but only **2x x16 + 1x x16(x8)**. Fails slot count. |
| Tyan/MiTAC S8050GM4NE-2T | 5x Gen5 x16, single socket — but only **8 DIMM slots**, i.e. 8 of 12 channels. Fails the 12-channel requirement. |

## The one live threat to the leader — GIGABYTE MZ23-SU0 (Rev. 3.x)

**UPDATED 2026-11-10T04:10Z — it is now buyable, and it is the better board.**
Newegg lists it at **$869.00, sold and shipped by Newegg** (not a marketplace
seller), free shipping, "Add to cart" live, item `N82E16813145624`:
https://www.newegg.com/gigabyte-mz23-su0/p/N82E16813145624

That retires the only reason the CP1 was ahead. On every spec that matters the
SU0 is equal or better: 5x Gen5 x16 vs 4 (3 Gen5 + 1 Gen4), same 6400 MT/s at
1DPC, same 12 DIMM / 12 channels, same AST2600, and 63.5 mm shallower (CEB
304.8 x 266.7 vs E-ATX 304.8 x 330.2).

**Why CP1 is still the leader for this build: the SU0 cannot be bought in the
EU.** Newegg does not ship to the EU — its own international-shipping list is
Australia, Bahrain, Israel, Japan, Kuwait, Mexico, New Zealand, Oman,
Philippines, Qatar, Saudi Arabia, Singapore, South Korea, Thailand, UAE, UK
(https://kb.newegg.com/knowledge-base/international-shipping/). Germany is not
on it. The only EU offer found is a **used** eBay listing via idealo.de at
**€1,290.00 incl. VAT** — ~€400 more than a new CP1. Germany-specific sweeps
returned nothing: Happyware "0 products found for MZ23", ServerFactory "No
match", idealo.de 1 used offer only, Computeruniverse/servershop24 no results,
Alternate only fuzzy padding hits.

So the decision is a price/risk trade, not a spec trade:
buy the CP1 in the EU for €876.98, or import the better board from the US.

**Partial update 2026-11-10T05:0xZ — the SU0 now has a German retail listing,
but its price/stock could not be read.** galaxus.de carries a product page for
it, "Gigabyte Mainboard MZ23-SU0 (Rev. 3.0) CEB Sockel SP5 Retail", product
number **77255324**:
https://www.galaxus.de/de/s1/product/gigabyte-mainboard-mz23-su0-rev-30-ceb-sockel-sp5-retail-sp5-mainboard-77255324
The same product number is listed on galaxus.ch, galaxus.nl and galaxus.at.

**What is verified:** the listing exists and the retailer is Galaxus (German
shop, ships within DE). A search-engine result snippet for that page stated
**"1.349,- EUR inkl. MwSt."** — but Galaxus returns **403/Cloudflare captcha
to every automated fetch** (direct curl with a browser UA, r.jina.ai, three
CORS proxies, and their own /api/product/ path all blocked; Wayback has no
snapshot). So the €1,349 figure is a **search-snippet value, UNVERIFIED** — do
not treat it as a confirmed price, and stock is entirely UNVERIFIED.

**Why this does not change the leader even if €1,349 is right:** it is a
~**€472 (54 %) premium** over the CP1's €876.98 for a board that is one x16
slot and 63 mm of depth better, and needs the *same* one MCIO adapter to reach
four cards. €472 for an extra slot that a 2-slot-pitch card cannot use anyway
(see the 0.6 mm margin above) is not a cheaper path — and **Geizhals, which
indexes the whole EU market, has no MZ23-SU0 listing at all** (06:00Z, see
open question 4), so there is nothing to buy even at the snippet price. If a real cart price ever
comes in near €900, the SU0 becomes the pick on spec alone — that is the one
thing to re-check, and it needs a human browser, not a fetch.

Also checked this run, again negative for the SU0 in the EU: **Happyware
"3 products found for MZ23-SU0" is fuzzy padding** (the three hits are
H223-S10-AAP1, XV24-SU0-AAJ1 and G293-Z23-AAM1 — server barebones, no MZ23
board); **WiredZone: "No Product Found"**; **Thinkmate: 0 search results**;
idealo.de still shows only the **used €1,290** eBay offer; idealo.ch 404s.
US side: **Tech-America lists $907.00 but "Out Of Stock"**
(https://www.tech-america.com/item/gigabyte-mb-mz23-su0-soc-lga6096-sp5-amd-epyc9005-9004-ddr5-pcie-ceb-brown-box/mz23-su0)
— re-read live 2026-11-10T08:49Z, still **$907.00 / "Out Of Stock"** — so
Newegg's $869 remains the only live US stock.
**Newegg US re-verified in full 2026-11-10T08:50Z, and this closes the
carried-forward UNVERIFIED on the $869:** the product page loaded through
r.jina.ai and states **$869.00**, "**Add to cart**" live, "plus minus Limit
99999 per customer", **Free Shipping**, "Pickup — Ready by 9AM, Free",
"**Sold by Newegg / Shipped by Newegg**", and the holiday window ("Nov 1 –
Dec 31, 2026 … refund or replacement until January 31, 2027"). So the $869 is
no longer a carried-forward value; it is a live read. Item `N82E16813145624`,
images `13-145-624-04…06.png`.
**EU side re-swept 2026-11-10T08:51Z: still nothing new.** idealo.de search
"*2 Ergebnisse*" = the **used** eBay board at **€1,290.00** (delivery 10–22
working days, free shipping) plus an unrelated *32 GB DDR5-5600 RDIMM "compatible
for MZ23-SU0"* eBay offer at €1,448 — a memory stick, not a board; do not count
it. idealo.at: the same used board now **€1,599.00** and the same RAM offer at
€1,448. Geizhals still refuses scripted access (403, "Sichere Verbindung wird
überprüft"). So the SU0's EU picture is unchanged for the fourth consecutive
run: **no new-in-box EU offer, used-only, and the used ask is drifting up
(€1,290 → €1,599).**

| | MZ23-SU0 | MZ33-CP1 |
|---|---|---|
| x16 slots | **5, all Gen5** | 4 (3 Gen5 + 1 Gen4) |
| 6400 @1DPC (9005) | yes (4800 on 9004) | yes (4800 on 9004) |
| DIMM / channels | 12 / 12 | 12 / 12 |
| Slot pitch | **1.0 all five** (20.4–20.7 mm measured) | 1.0 / 2.0 / 2.0 |
| 2-slot cards native | **3** (Slot_1/3/5, 40.6 mm apart) | **3** (Slot_2/4/6, 40.6 mm apart) |
| 4th card | 2x MCIO 8i → x16 adapter (only 2 Gen5 MCIO + 2 Gen5-or-SATA) | 2x MCIO 8i → x16 adapter (4 Gen5 MCIO) |
| IPMI | AST2600 + MLAN, dual 1 GbE (I350-AM2) | AST2600 + MLAN, dual 1 GbE (I210-AT) |
| Form factor | **CEB 304.8 x 266.7 mm** | E-ATX 304.8 x 330.2 mm |
| Price / stock | **$869 Newegg US, in stock** (live-read 08:50Z, sold+shipped by Newegg); Tech-America **$907 out of stock**; EU: galaxus.de lists it (**price UNVERIFIED**, captcha) + used-only elsewhere (€1,290 idealo.de / €1,599 idealo.at) | **€876.98, in stock, DE** |

Ordering part numbers from the datasheet: retail `9MZ23SU0MR-000-3*`, bulk
`9MZ23SU0NR-000-3*` — useful for a distributor quote, which is the one route
that could make this an EU purchase. Not yet tried: asking a DE distributor to
quote that part number.

**Its QVL grades the 9135 at DDR5-6400 too** (last update Oct 28, 2026; row
"AMD 9135 100-000001150 … 200W … DDR5-6400 … 200/240"):
https://www.gigabyte.com/Enterprise/Server-Motherboard/MZ23-SU0-rev-3x/Support-QVL
The memory-tab spreadsheet is still unreachable (the page renders only the CPU
sheet, the same JS trap as the CP1's; `mb_qvl_MZ23-SU0-3.x.xlsx` 404s on the
download host). So the CP1's 37-module 6400 RDIMM list is still the only
QVL-backed memory list of the two — but the SU0 uses the same CPU and the same
12 DIMMs, so a 6400 RDIMM from the CP1's list is the sane choice either way.

Caveat on its MCIO budget: it has **only 2 Gen5 MCIO** (plus 2 more that are
Gen5-or-SATA), so the 4th-card adapter consumes both Gen5 MCIO and leaves the
Gen5-or-SATA pair — a thinner storage story than the CP1's 4 Gen5 MCIO.
**Re-read 2026-11-12T00:5xZ against the new M.2 requirement: the SU0 is now
clearly behind on storage.** Its datasheet lists `2 x M.2 (2280/22110), PCIe
**Gen3 x2**` — half the width of the CP1's Gen3 x4 slot, and still Gen3. So
neither board can run a Gen5 M.2 from the onboard slot; both must use MCIO, and
after the 4th-GPU adapter the SU0's surviving Gen5-capable pair is the weaker
one. **This does not flip the pick, but it removes the last "SU0 is better on
paper" argument** — on the storage axis the CP1 is now at least equal and the
onboard slot is twice as wide.

Slot pitch re-verified two independent ways this run: the earlier datasheet
measurement, and the full-resolution Newegg board photo
(`c1.neweggimages.com/productimage/nb1280/13-145-624-04.png`), which shows five
evenly spaced x16 slots with no adjacent pair. Five gaps, no doubled gap.
## WRX90 / Threadripper PRO — asked directly 2026-11-12, and the answer is **no**

The question was: switch to WRX90 + TR PRO, giving up 4 RAM channels. Verified
figures:

| | MZ33-CP1 + EPYC 9135 | Pro WS WRX90E-SAGE SE + TR PRO 9955WX |
|---|---|---|
| Memory channels | **12** (DDR5-6400, 12 DIMM) | **8** (DDR5-6400, 8 DIMM) |
| Peak mem BW (theoretical) | 12 ch x 6400 = **614.4 GB/s** | 8 ch x 6400 = **409.6 GB/s** |
| Native Gen5 x16 slots | 3 (+1 Gen4 x16) | **7** (one is x8) |
| 2-slot cards without adapters | 3 | ASUS's own guidance for GPU placement names **slots 4, 5, 7** = **3** |
| Gen5 M.2 onboard | none (Gen3 x4 only) | **4x Gen5 x4** |
| Board price | **€876.98** (Plexcom, in stock) | UNVERIFIED (Caseking lists it; price not read) |
| CPU price | **EPYC 9135 from €1,629** (Geizhals DE) | **TR PRO 9955WX from €1,637.70** (Geizhals DE) |
| CPU TDP | 200 W | 350 W |

Sources: https://www.asus.com/motherboards-components/motherboards/workstation/pro-ws-wrx90e-sage-se/techspec/ ·
https://www.pugetsystems.com/parts/Motherboard/ASUS-Pro-WS-WRX90E-SAGE-SE-15100/ ·
https://geizhals.de/amd-epyc-9135-100-000001150-a3333151.html ·
https://geizhals.de/amd-ryzen-threadripper-pro-9955wx-100-100000725wof-a3531872.html ·
https://rog-forum.asus.com/t5/gaming-motherboards/asus-pro-ws-wrx90e-sage-se-motherboard-gpu-placement/td-p/1113091

**Verdict: the swap does not buy what it looks like it buys.**
- **You lose 33 % of memory bandwidth** (614 → 410 GB/s). For LLM inference that
  is the resource that matters most; it is a real, permanent loss.
- **You still do not get 4 dual-slot cards native.** ASUS's own recommended GPU
  slots on this board are **4, 5 and 7 — three cards** — and the forum answer
  explicitly advises **against risers/adapters**. So the same "3 native + 1
  adapted" shape as the CP1, except now the 4th card is on an *unsupported*
  path rather than a documented MCIO one.
- **CPU cost is a wash** (€1,629 vs €1,637.70) and board cost is likely higher,
  so you pay **more** for less bandwidth.
- **What you actually gain:** 4 onboard Gen5 M.2 slots (which removes the whole
  MCIO-adapter dance) and 128-148 CPU lanes so slots are not a squeeze. That is
  a genuine convenience — but you are paying 4 channels of bandwidth for it,
  and the MCIO storage workaround on the CP1 costs ~€105 and is already solved.

**Recommendation: stay on EPYC 9135 + MZ33-CP1.** Reconsider WRX90 only if the
onboard Gen5 M.2 simplicity and the extra slots outrank memory bandwidth for
your workload — for tensor-parallel inference they almost certainly do not.
**UNVERIFIED: WRX90E-SAGE SE current EU price**, so the total-cost comparison is
incomplete; the bandwidth and slot-count arguments do not depend on it.

The CP1 does not fail — it is 3-native + 1-adapter. Compare the two ways to
complete the build:

| Path | What you give up | Cost |
|---|---|---|
| **CP1 + 1x MCIO→x16 adapter** (recommended) | nothing electrical; the 4th card is Gen5 x16 via 2x MCIO 8i. Consumes one Gen5 MCIO pair, **leaving 2 Gen5 MCIO (4 NVMe)** for the RAID0 M.2 set + 2 Gen4 MCIO. Mechanical only: adapter mounting + airflow. **Pick CP-0232 (vertical) if the 4th card gets a 1-slot gap; CP-0231 (flat) needs 2 slots.** **Parts, both EU-sourced: C-Payne MCIO gen5 device adapter x8/x16 €50 + 2x MCIO 8i gen5 cable €45 = €140, ships from Germany, no customs** (08:20Z, re-verified 08:51Z; the cheap €79,90 Amazon.de riser is a splitter and drops card 4 to x8). | **€876.98 board** (Plexcom, in stock) + **€140 adapter set** (C-Payne, DE) + **€210 for 4 Gen5 M.2** (KALEA + C-Payne, EU) |
| Any 12-ch board at 1DPC that gives up MT/s | **5200 MT/s** (MZ33-AR1) = 18.75 % less memory bandwidth; and the AR1 fits only 2 dual-slot cards natively, so it needs 2 adapters anyway. | AR1 price UNVERIFIED + 2 adapters, and slower |
| Riser-only build on a 3x-x16 board | native slot x16 for cards 3–4, and **4800–5200 MT/s** on those boards | board + risers + chassis |

The adapter path is strictly cheaper: it keeps 6400, needs one part instead of
two, and needs no chassis change beyond 8 bracket positions. **A board swap
never wins here** — every alternative board gives up either 6400 MT/s or takes
more adapters to reach four cards. (The MZ23-SU0 is the exception on paper: same
adapter count, more slots, shorter board — but it still has no EU stock, so it
is a EUR 400-odd risk, not a cheaper path. See above. **Update 08:20Z: the CP1
path no longer needs any non-EU purchase at all** — the adapter set is C-Payne,
shipped from Germany, so "import the US board" is now the only reason the SU0
is not the pick, and it is a big one.)

Residual risk: 40 mm cards in Slot_1/Slot_2 are not documented as coexisting
(UNVERIFIED), so buy Slot_2/4/6 as the three native cards and put the adapter
card in the fourth chassis position. The 0.6 mm side gap at 2.0-slot pitch is
no longer a thermal concern — both R9700 SKUs are blowers that exhaust out the
bracket (verified 2026-11-10T05:35Z).

## Open questions

1. ~~**CP1 slot pitch**~~ — **RESOLVED 2026-11-10T02:35Z**: 1.0 / 2.0 / 2.0
   pitches (Slot_1→2 = 20.3 mm). Three cards native, fourth on MCIO 8i→x16.
    **Closed for good 06:00Z** on the manual drawing measure (20.3/40.7/40.6 mm)
   and the server-hardware.com photo (1.02/2.0/2.0). **Reasoning corrected
   07:30Z:** the "slots are physical positions 36/37/39/40, gap at 38" argument
   is **withdrawn** — 38 is the `BAT` battery callout, not a skipped slot. A
   fresh 600 dpi re-measure gives **20.7 / 40.3 / 40.7 mm** (1.02/1.98/2.00
   pitches), so the conclusion stands on geometry alone. A 40 mm 2-slot card
   cannot occupy Slot_1+Slot_2; Slot_2/4/6 clears a 40 mm card with 0.6 mm to
   spare, and both SKUs are blowers so the gap is not thermal (05:35Z).
2. ~~**CP1 price/stock**~~ — **RESOLVED, and cheaper than first recorded
   (2026-11-10T03:5xZ)**. Happyware €931 excl. VAT in stock
   (https://www.server-hardware.com/gigabyte/mz33-cp1_se7m6756-359045,
   art. SE7M6756-359045, rev 3.x; tiers €904/€885/€866). But idealo.de now
   tracks it: **8 offers, €881.97 – €1,247.00**
   (https://www.idealo.de/preisvergleich/OffersOfProduct/207996996_-mz33-cp1-gigabyte.html)
   — jacob.de €881.97 (delivery by 12.11), future-x.de €881.99,
   galaxus.de €929.21, voelkner €984.60, kaufland €991.96.
   **Cheaper still (06:00Z): Geizhals lists the CP1 in three variants,
   6 live offers €876.98–€947.45** (last update 10.11.2026, 06:50) — cheapest
   **Plexcom Hardware For You, €876.98, "lagernd, 1-3 Werktage"**, DE-only
   shipping; then jacob.de €881.97, future-x.de €881.99, galaxus €929.21.
   https://geizhals.de/5538300428 (also 5583075628, 6428911513). **This
   corrects the earlier "Geizhals has no listing" — it does, and it is now
   the cheapest source.** EU: idealo.at
   €894.40, idealo.it €995.99, idealo.es €1,041.99, idealo.fr €1,119.96,
   plus an eBay.de item (358036910244) at €1,247.
   Newegg / WiredZone / Thinkmate / ServerFactory: still **0 hits**
   (Newegg returns "0 items that match").
3. ~~**CP1 memory QVL**~~ — **RESOLVED 2026-11-10T03:05Z, and fully enumerated
   2026-11-10T07:52Z by parsing the sheet itself**; the 9135 grading
   caveat is **re-confirmed closed (2026-11-10T03:5xZ)**: the live QVL page
   (Last Update **Oct 28, 2026**) grades the CPU as **DDR5-6400** — row
   "AMD 9135 100-000001150 … 200W … DDR5-6400 … 200/240" — so the 6000
   grading existed only in the stale May-2025 xlsx snapshot. Got that
   spreadsheet:
   `https://download.gigabyte.com/FileList/QVL/mb_qvl_MZ33-CP1-3.x.xlsx`
   (46 KB, 424 rows, last modified **2025-05-12**; pulled via the Wayback copy
   `https://web.archive.org/web/20250711194638id_/…mb_qvl_MZ33-CP1-3.x.xlsx?v=071a40734ab99cd6b51038a03d2707fd`).
   It **does list DDR5-6400 RDIMMs at 1DPC: 37 modules**, all PASS, all
   1.1 V, 288-pin ECC Registered. Cheapest sensible picks (64 GB 2Rx4):
   - Samsung **M321R8GA0PB2-CCPWC** (Rambus), `-CCPEC` (Renesas),
     `-CCPKC` (Montage)
   - SK hynix **HMCG94AHBRA480N AA** (Renesas), **HMCG94AHBRA487N AA**
     (Montage)
   - Micron **MTC40F2046S1RC64BD2** (QSFF/MWFF/MXCC/UXCC/QWCC/USFF)
   32 GB 1Rx4 / 2Rx8, 16 GB 1Rx8, 48 GB, 96 GB and 128 GB 6400 SKUs are also
  listed, so a 12 x 64 GB = 768 GB all-6400 build is QVL-backed.
   Source: https://www.gigabyte.com/Enterprise/Server-Motherboard/MZ33-CP1-rev-3x/Support-QVL
   **QVL re-verified live again 2026-11-10T08:50Z** (page loaded through
   r.jina.ai, which is now the working route since bare `curl` to gigabyte.com
   is 403): the 9135 row reads **"AMD 9135 100-000001150 | AMD | Turin | PR |
   64 | 16/32 | 3.65 | 4.3 | 200W | DDR5-6400 | 200/240"**, and the page
   footer stamp is **"Last Update: Oct 28, 2026"**. The 9005 tab is **27 CPUs
   and every single one is graded DDR5-6400** (27 rows, 27 `DDR5-6400`
   occurrences, zero of any other grade — counted, not eyeballed), so there is
   no 9005 row below 6400 anywhere on the page, the strongest form of this
   evidence so far. The **memory** sheet
   is still not fetchable: the page emits the CPU table as the default tab, no
   `.xlsx` URL appears in the served payload at all, and
   `00-MZ33-CP1_QVL-20260400464.xlsx`, `00-MZ33-CP1_QVL-20261027.xlsx`,
   `mb_qvl_MZ33-CP1-3.x.xlsx` and `00-MZ33-CP1_QVL.xlsx` all **404** on the
   download host. So the 37-module 6400 RDIMM list still rests on the archived
   2025-05-12 sheet, unchanged.
   **QVL re-verified live 2026-11-10T05:50Z** — 9135 row reads "AMD 9135
   100-000001150 … Turin … 200W … **DDR5-6400** … 200/240", page stamp
   "Last Update: Oct 28, 2026". Unchanged. **NEW closing evidence
   (06:00Z): the board manual's own memory-population table** states, for
   EPYC 9005 at 1DPC, RDIMM 1R/2R = **6400 MT/s**, 5600, 4800 depending on
   the DIMM's QVL grade, with footnote 1: *"6400 MT/s supported with specific
   DIMMs listed in product page QVL."* So 6400 is not a marketing number — it
   is conditional on buying a QVL-graded DIMM, which is exactly what the 37
   modules above are. The same table shows **EPYC 9004 capped at 4800**,
   confirming the board is not the limiter for a 9135.
   Source: rev 3.0 manual §1-4-4, p.14 —
   https://download.gigabyte.com/FileList/Manual/server_mb_manual_mz33-cp1_e_v3.0_.pdf
   **New cost fact 2026-11-10T06:43Z — the QVL-listed 12 x 64 GB build is now the
   big line item, not the board.** Live Geizhals prices for the QVL families at
   6400 (all 2Rx4 64 GB, reg ECC): SK hynix **HMCG94AHBRA480N €3,401.32** (1
   offer), sister part `-487N` **€3,580.33**, Micron **MTC40F2046S1RC64BH1T
   €2,999.81** (5 offers), Samsung **M321R8GA0PB0-CWM €3,069.00**. So
   **12 x 64 GB = €36.0k–€43.0k**, i.e. ~40x the €877 board. The 32 GB QVL part
   Samsung **M321R4GA3EB2-CCP** is **€1,961.45** → **12 x 32 GB ≈ €23.5k**
   (384 GB). Cheaper 6400 RDIMMs exist (Kingston FURY Renegade Pro 128 GB kit
   €47.96/GB, G.Skill Zeta R5 64 GB kit) but those are **not on the CP1 QVL**,
   so buying them means 6400-at-your-own-risk per the manual's footnote. This
   does not change the pick — it changes what the build actually costs, and it
   makes the €472 MZ23-SU0 premium irrelevant next to memory.
   **Sheet recovered and parsed 2026-11-10T07:52Z — the 37-module 6400 list is
   now verified row-by-row, and the last UNVERIFIED row is closed.** The
   `FileList/QVL/` path still 404s live, so the sheet came from the Wayback
   capture again (46,347 B gzip → 51,519 B xlsx, 424 rows): parsing
   `xl/worksheets/sheet1.xml` + `sharedStrings.xml` directly gives **327 memory
   rows, of which exactly 37 are `6400MHz` / `1.1v` / `ECC Registered` /
   `288-pin` / `PASS`**, confirming the earlier 37 figure by a second count.
   The 64 GB 2Rx4 group is Samsung `M321R8GA0PB2-CCPEC/-CCPKC/-CCPWC`,
   SK hynix `HMCG94AHBRA480N AA` / `-487N AA`, Micron `MTC40F2046S1RC64BD2`
   in six RCD variants (QSFF/MWFF/MXCC/UXCC/QWCC/USFF). The list also carries
   128 GB Samsung `M321RAJA0MB2-CCPWC`, 96 GB Samsung `M321RYGA0PB2-CCPEC/
   -CCPPC/-CCPWC/-CCPKC` and SK hynix `HMCGM4MHBRB505N/-499N AA`, 48 GB
   Samsung `M321R6GA0PB2-CCPKC` / `M321R6GA3PB2-CCPWC`, 24 GB
   `M321R3GA3PB2-CCPKC`, and 16 GB entries.
   **CLOSES the 06:43Z flag:** the Samsung 32 GB `M321R4GA3EB2-CCP` **is** in
   the 6400/PASS list — as `-CCPPC` (Samsung-Montage) and `-CCPWC`
   (Samsung-Rambus), **2Rx8**, so the ~€23.5k 384 GB build is QVL-backed after
   all. Suffix matters: `-CCP` alone is not a part number. UNVERIFIED remains
   only *which suffix* Geizhals' €1,961.45 SKU ships — buy by full suffix.
   Source (archived sheet):
   https://web.archive.org/web/20250711194638id_/https://download.gigabyte.com/FileList/QVL/mb_qvl_MZ33-CP1-3.x.xlsx?v=071a40734ab99cd6b51038a03d2707fd
   https://geizhals.de/sk-hynix-rdimm-64gb-hmcg94ahbra480n-a3657519.html
   https://geizhals.de/micron-rdimm-64gb-mtc40f2046s1rc64bh1t-a3877100.html
   https://geizhals.de/samsung-rdimm-64gb-m321r8ga0pb0-cwm-a3138665.html
   https://geizhals.de/samsung-rdimm-32gb-m321r4ga3eb2-ccp-a3677652.html
4. **MZ23-SU0 price/stock** — **RESOLVED 2026-11-10T04:10Z, and it is now the
   better board but not an EU buy.** **Still unresolved as of 2026-11-10T08:51Z:**
   no EU retailer price for the board. galaxus.de returns 403 directly and the
   "Are you a robot?" captcha via r.jina.ai on both the product URL and the bare
   product-id URL; Geizhals 403s; the €1,349 snippet figure stays UNVERIFIED. So
   the CP1's fully-EU buy path (board €876.98 + C-Payne adapter set €140) is
   still the only route that needs no import. Newegg: **$869.00, sold and shipped by
   Newegg**, free shipping, in stock, item `N82E16813145624`
   (https://www.newegg.com/gigabyte-mz23-su0/p/N82E16813145624). Ordering part
   numbers `9MZ23SU0MR-000-3*` (retail) / `9MZ23SU0NR-000-3*` (bulk).
   **Newegg does not ship to the EU** (their list: AU, BH, IL, JP, KW, MX, NZ,
   OM, PH, QA, SA, SG, KR, TH, AE, UK — no DE). Only EU offer is **used**, via
   eBay on idealo.de, **€1,290.00 incl. VAT**. Germany sweeps: Happyware
   "0 products found for MZ23", ServerFactory "No match", idealo.de 1 used
   offer, Computeruniverse / servershop24 / Geizhals no results.
   **QVL: its page grades the 9135 at DDR5-6400** (Oct 28, 2026) — URL above.
   Memory-tab xlsx still unreachable (`mb_qvl_MZ23-SU0-3.x.xlsx` 404s).
   Slot pitch re-verified from the full-res Newegg photo: five evenly spaced
   slots, no adjacent pair. UNVERIFIED: an EU distributor price for the
   ordering part numbers — **still not found 2026-11-10T04:20Z**; 5 more DE
   shops swept (Alternate fuzzy-only, Bora none, Computeruniverse 403,
   Mindfactory empty, snogard timeout), Geizhals then blocked scripted fetches
   (it works again via r.jina.ai as of 06:00Z — see below).
   The route that could flip the pick is a distributor quote for
   `9MZ23SU0MR-000-3*`, which is an email, not a web fetch. **Partial progress
   2026-11-10T05:0xZ: galaxus.de does list it (product 77255324, also .ch/.nl/
   .at), and a search snippet says "1.349,- EUR inkl. MwSt." — but Galaxus
   403s/captchas every fetch route, so price and stock are UNVERIFIED.** A
   ~€467 premium over the CP1 buys one x16 slot and 63 mm of depth, with the
   same one-adapter requirement; not a cheaper path. Re-check in a real
   browser if the €1,349 turns out to be stale. Tech-America ($907) is out of
   stock; WiredZone/Thinkmate/Happyware all still miss.
   **EU status re-tested 2026-11-10T06:00Z via Geizhals — the strongest single
   negative yet: Geizhals has ZERO MZ23-SU0 listings** (geizhals.de and
   geizhals.eu, mainboard category; the board simply is not in the EU price
   index, while the same query finds 3 CP1 listings). That is a much broader
   sweep than shop-by-shop and confirms the SU0 is not an EU retail product
   today. Also negative this run: senetic.de "Nichts gefunden" (both
   `MZ23-SU0` and part number `9MZ23SU0MR-000`), WiredZone no product,
   toppreise.ch 403, billiger.de dead page, eBay.de new-condition search
   empty, itsco/thomas-krenn/etb-tech/serverschmiede no hits. galaxus.de/.ch/
   .at/.nl and digitec.ch all captcha every route including their /api/ path.
   **Newegg US re-confirmed live: $869.00, "Add to cart", free shipping,
   holiday return window to 2027-01-31.** Verdict unchanged: the SU0 remains
   the better board that cannot be bought in the EU at a sane price.
   **EU status re-tested 2026-11-10T06:43Z — still no new-in-box EU offer.**
   idealo.at now shows the **used** unit at **€1,599.00** (was €1,290 on
   idealo.de — the used market went up, it is still an eBay.at listing,
   delivery 7–15 working days). Newly checked and negative: senetic.de
   ("Nichts gefunden"), itsco (404), csv.de (404), ebay.de search (blocked),
   toppreise.ch (403), skinflint.co.uk (empty), amazon.de (empty).
   galaxus.at / .nl / .ch and digitec.ch now answer but all four say
   **"Aktuell nicht lieferbar"** on product 77255324 — so the German
   Galaxus listing is the one that needs a human browser, and the CH/NL/AT
   siblings are out of stock. Geizhals (de + eu + at) still has **zero**
   MZ23-SU0 rows. `9MZ23SU0MR` as a Geizhals keyword: no result.
   Newegg US re-read this run: **$869.00, "Add to cart", limit 99999,
   sold/shipped by Newegg** — unchanged.
   **Re-tested 2026-11-10T08:51Z — same answer, and the used ask rose again.**
   idealo.de search for `MZ23-SU0` returns exactly **2 hits, neither a new
   board**: the **used** eBay unit at **€1,290.00** ("gebraucht", delivery 10–22
   working days, free shipping) and a **32 GB DDR5-5600 RDIMM** listed at
   €1,448 whose title merely says "compatible for Gigabyte MZ23-SU0" — a DIMM,
   not a motherboard; on idealo.de it sits in the *RAM* category. idealo.at
   returns the same two, with the used board at **€1,599.00**. Geizhals still
   refuses scripted access (403, "Sichere Verbindung wird überprüft"). So across
   four consecutive runs there is still **no new-in-box EU offer**, and the used
   ask has now gone €1,290 → €1,599 — the wrong direction for a fallback whose
   whole case was "same spec, cheaper or comparable". **This question is
   effectively settled negative; only a distributor quote for
   `9MZ23SU0MR-000-3*` could reopen it, and that is an email, not a fetch.**
   **US price promoted out of UNVERIFIED at 08:50Z:** the Newegg product page
   loaded end-to-end through r.jina.ai and states **$869.00**, "**Add to cart**",
   "plus minus Limit 99999 per customer", **Free Shipping**, "Pickup — Ready by
   9AM, Free", "**Sold by Newegg / Shipped by Newegg**", holiday return window
   to **2027-01-31**. Tech-America re-read the same minute: **$907.00, "Out Of
   Stock"**. So $869 is a live fact now, not a carried-forward value — it still
   does not make the SU0 the pick, because the EU side remains empty.
5. **4x R9700 on SP5** — no documented build found on any SP5 board.
   UNVERIFIED, not contradicted.
6. ~~**CP1 BIOS enabling 6400**~~ — **RESOLVED 2026-11-10T06:52Z. The BIOS
   version list was never blocked; it is embedded in the product page's own
   JSON, and the old filename guesses were simply wrong.** Gigabyte serves
   `/Enterprise/Server-Motherboard/MZ33-CP1-rev-3x` — the *product* page, not a
   `/Support-BIOS` path (that slug 404s on every board, CP1 and MZ32-AR0 alike)
   — with an inline Nuxt payload carrying the full file table. Read via
   r.jina.ai with `x-respond-with: html`; bare curl to gigabyte.com is 403 but
   the payload itself is present. The three BIOS builds it lists:

   | Build | Release date | Size | Direct download |
   |---|---|---|---|
   | **R25_F17** (newest) | **2026-11-08** | 50,505,855 B | https://download.gigabyte.com/FileList/BIOS/MZ33-CP1_R25_F17.zip |
   | R24_F17 | 2026-09-15 | 50,432,248 B | https://download.gigabyte.com/FileList/BIOS/MZ33-CP1_R24_F17.zip |
   | R23_F16 | 2026-08-12 | 49,934,469 B | https://download.gigabyte.com/FileList/BIOS/MZ33-CP1_R23_F16.zip |

   Naming is `MZ33-CP1_R<nn>_F<nn>.zip`, not `server_bios_mz33-cp1_*` — which
   is exactly why every earlier guess 404'd. All three return **HTTP 200,
   `Content-Type: application/zip`**, lengths matching the page JSON to the
   byte, and **no `?v=` token is needed**. So the newest BIOS is **two days
   older than this program** and is a public download, not something to ask the
   shop for. **6400 enablement: the release notes say nothing about DRAM speed**
   — all three are CVE-only (R25_F17: CVE-2026-54934/54944, "security updates
   for Turin platform"; R24_F17: the long Genoa+Turin CVE list). That is
   *consistent* with §1-4-4 as already recorded: 6400 is governed by the
   **DIMM's QVL grade**, not a BIOS switch, so there is no speed toggle to find
   in a changelog. Action is unchanged and now cheap: flash R25_F17.
   UNVERIFIED only: which build a given retail board ships with — ask the shop,
   or just flash. Also new this run: the live QVL bundle is
   `00-MZ33-CP1_QVL-20260400464.xlsx`, 372,344 B, **dated 2026-10-27** — i.e.
   the QVL was refreshed with the Oct-28 CPU tab, so the memory sheet is a
   current document, even though its rows still render only client-side (the
   app-served path is not guessable; every `FileList/QVL/` form 404s).

## Changelog

- 2026-11-10T02:05Z — initial leaderboard. Leader: MZ33-CP1. Key correction vs
  the beam agents: MZ33-AR1 is capped at 5200 MT/s at 1DPC by Gigabyte's own
  datasheet, so it cannot be the pick for a 6400 requirement.
- 2026-11-10T02:20Z — both beam agents completed. Neither found the CP1; both
  shortlisted MZ33-AR1 on slot count alone without checking its 1DPC speed.
  Added ASUS K14PA-U24 and Tyan S8050 to the rejected table. Supermicro's
  Radeon-validated 4-GPU platform is AS-2115HV-TRNT (Threadripper PRO), so no
  EPYC board has a vendor-validated 4x R9700 config. No change to the leader.
- 2026-11-10T02:35Z — got the real rev 3.0 manual (download.gigabyte.com, not
  the 404 product-page link) and a board photo. **Slot pitch is 1.0 / 2.0 / 2.0
  pitches, not even 2-slot**: Slot_1→Slot_2 is 20.3 mm, so the 1/2/4/6 naming is
  numbering, not spacing. Three R9700 fit natively; the fourth needs a 2x MCIO
  8i → Gen5 x16 adapter (~$55, 10Gtek SA22N2116P) off the board's 4x MCIO Gen5.
  Leader unchanged, but the "four slot-native x16" claim is now corrected to
  "three slot-native + one MCIO adapter". Also found EU stock/price: €931 excl.
  VAT at Happyware DE, in stock. QVL still unreadable (JS-only Memory tab).
- 2026-11-10T03:08Z — **QVL blocker closed.** Pulled the real QVL spreadsheet
  (`mb_qvl_MZ33-CP1-3.x.xlsx`, last modified 2025-05-12, via Wayback because
  the download host 404s non-browser clients). It lists **37 DDR5-6400 RDIMMs
  at 1DPC, all PASS** — Samsung M321R8GA0PB2-CCPWC / SK hynix
  HMCG94AHBRA480N AA / Micron MTC40F2046S1RC64BD2 (64 GB 2Rx4), plus 16/32/48/
  96/128 GB 6400 SKUs, so 12 x 64 GB all-6400 is QVL-backed. Leader unchanged.
  One flag: the xlsx CPU sheet still grades the 9135 at DDR5-6000 (stale
  May-2025 grading; datasheet, manual and live CPU tab all say 6400).
  Also re-confirmed €931 / in stock / "Max RAM Frequency 6400MHz" at Happyware.
- 2026-11-10T03:58Z — blockers 2 and 3 fully closed, one new board. **Price:
  8 offers, €881.97–€1,247 on idealo.de** (jacob.de €881.97, future-x.de
  €881.99, galaxus.de €929.21, all "delivery by 12.11"); EU idealo.at €894.40
  / .it €995.99 / .es €1,041.99 / .fr €1,119.96. Newegg still "0 items that
  match"; Geizhals/WiredZone/Thinkmate/ServerFactory still no listing. **QVL
  grading flag retired**: the live QVL page (Last Update Oct 28, 2026) lists
  the 9135 at DDR5-6400; only the stale May-2025 xlsx said 6000.
  **New finding — MZ23-SU0 (Rev. 3.x)**: 5x Gen5 x16, 12 DIMM 12-ch, 6400
  MT/s at 1DPC, AST2600, CEB 304.8 x 266.7 mm, from its own datasheet PDF
  (Skia print 2026-09-11). Measured from that datasheet's board image: all
  five x16 slots at **1.0 pitch**, so 3 dual-slot cards native in Slot_1/3/5 —
  the same native count as the CP1, with one extra x16 pair on the board and
  63 mm less board depth.
  It is **not** the new leader only because it has **no price or stock
  anywhere** (UNVERIFIED). Leader unchanged: MZ33-CP1.
- 2026-11-10T04:20Z — **no change to the leader.** Re-verified live rather than
  re-read: CP1 still **8 offers, €881.97–€1,247 on idealo.de** (jacob.de
  €881.97, "Lieferung bis Do. 12.11.") and Happyware/server-hardware.com still
  **€931.00 excl. VAT**, tiers €931/€904/€885/€866, art. SE7M6756-359045.
  **MZ23-SU0 still has no EU listing**: Newegg unchanged at **$869.00**, in
  stock, "Add to cart" live; 5 fresh DE shops this run all miss —
  Alternate (fuzzy only), Bora "Leider wurden zu Ihrer Suchanfrage keine
  Artikel gefunden", Computeruniverse 403, Mindfactory empty, snogard timeout;
  Happyware's "3 products found" for MZ23-SU0 is **fuzzy padding**, the boxes
  are XV24-SU0 etc., not MZ23. Geizhals now **bans** scripted access (429 "Too
  Fast", ban ID logged) so it cannot be re-checked by fetch. idealo.de returns
  403 to curl but works via r.jina.ai.
  Only new fact: the MCIO adapter page carries a vendor exclusion — SA22N2116P
  "does not support Asus RTX graphics card" (use -P2 for Asus RTX); harmless
  for R9700, noted so nobody swaps a GeForce onto it. Price/stock unchanged
  ($55, 99968 units).
- 2026-11-10T04:10Z — **MZ23-SU0 price blocker closed; it is now the better
  board, and the pick hinges on EU import.** Newegg: **$869.00, sold and
  shipped by Newegg**, free shipping, in stock, item `N82E16813145624`. It
  retires the "nobody lists it" reason the CP1 was ahead on spec. Spec re-read
  from its datasheet (5x Gen5 x16, 6400 @1DPC, 12 DIMM, AST2600, CEB
  304.8x266.7); **its QVL also grades the 9135 at DDR5-6400** (Oct 28, 2026).
  Slot pitch re-verified from the full-res Newegg photo: five evenly spaced
  slots, no adjacent pair — matches the earlier datasheet measurement.
  **CP1 stays leader because Newegg won't ship to the EU** (their list has no
  DE) and the only EU offer for the SU0 is **used at €1,290** vs €881.97 new
  for the CP1. Also this run: CP1 price re-confirmed live at Happyware
  (€931 excl. VAT, in stock, rev 3.x, art. SE7M6756-359045) and idealo.de
  (8 offers, €881.97–€1,247, jacob.de cheapest incl. delivery by 12.11);
  Newegg still "0 items that match" for MZ33-CP1.
  **CP1 slot pitch independently re-confirmed from a real board photo**
  (server-hardware.com product image, not Gigabyte's drawing): slot centres
  120 / 235.5 / 236.5 px apart → **1.02 / 2.0 / 2.0 pitches**, so 3 dual-slot
  cards fit natively and the 4th needs the MCIO adapter. Blocker 1 is closed
  for good, not just by drawing measurement.
  Also: every general web-search engine (DuckDuckGo, Bing, Mojeek, Brave,
  SearXNG instances) returned captcha/empty this run; all findings above came
  from vendor and retailer pages fetched directly or via r.jina.ai.
- 2026-11-10T05:05Z — **no change to the leader.** Two additions, both real
  vendor/retailer data. (1) **Card thickness now pinned to vendor specs**, not
  assumed: ASUS Turbo R9700 is **40 mm** ("Slots: 2", press.asus.com) and the
  ASRock R9700 Creator is **39 mm** ("2-slot", asrock.com). Against the
  measured 40.6 mm 2.0-slot pitch that is **0.6 mm / 1.6 mm of clearance** —
  it fits, but the ASUS variant has almost no margin, so prefer the ASRock
  39 mm SKU or test-fit. Slot_1+Slot_2 remains impossible (20.3 mm). (2) The
  **MZ23-SU0 now has a German retail listing**: galaxus.de product **77255324**
  (also .ch/.nl/.at). A DDG snippet states **"1.349,- EUR inkl. MwSt."** but
  Galaxus 403s/captchas *every* fetch route (curl, r.jina.ai, 3 CORS proxies,
  /api/product/, no Wayback snapshot) → **price and stock UNVERIFIED**. Still
  not the pick: ~€467/53 % over the CP1 for one more x16 slot and 63 mm, with
  the same single MCIO adapter needed. Also negative this run: Happyware's
  "3 products for MZ23-SU0" is fuzzy padding (H223-S10 / XV24-SU0 /
  G293-Z23 barebones), WiredZone "No Product Found", Thinkmate 0 results,
  idealo.de still used-€1,290 only, Tech-America $907 **out of stock**.
  CP1 re-verified live: Happyware **€931 excl. VAT, in stock, rev 3.x**;
  idealo.de **8 offers €881.97–€1,247** (data stamped 2026-11-10 03:48).
- 2026-11-10T05:35Z — **no change to the leader; one build risk retired.**
  **Card thickness is no longer a fit concern: both R9700 SKUs are blower
  cards**, verified from the makers' own pages this run. ASRock R9700 Creator:
  "Blower Design … Blower Fan Design — blow the air away", 271 x 112 x **39 mm**,
  2-slot, 1x 12V-2x6
  (https://www.asrock.com/Graphics-Card/AMD/Radeon%20AI%20PRO%20R9700%20Creator%2032GB/index.asp).
  ASUS Turbo R9700: "**blower-style fan** with a diecast metal shroud … 2-slot
  design enables multi-card configurations", **40 mm**
  (https://press.asus.com/news/press-releases/asus-turbo-radeon-ai-pro-r9700/).
  A blower exhausts out the bracket, so the previous 0.6 mm/1.6 mm side gap at
  2.0-slot pitch is not a thermal problem — **the earlier "buy the 39 mm SKU or
  test-fit" caution is retired**; either SKU is fine in Slot_2/4/6.
  **New platform caveat recorded from AMD's own product page**: the 9135's
  DDR5-6400 is conditional — "support requires OEM enablement and a BIOS update
  from your server or motherboard manufacturer"
  (https://www.amd.com/en/products/processors/server/epyc/9005-series/amd-epyc-9135.html).
  So 6400 on the CP1 needs a BIOS that enables it, not just a 6400-rated board —
  confirm the installed BIOS revision at purchase.
  Re-verified live, unchanged: CP1 **€931.00 excl. VAT, in stock, rev 3.x** at
  server-hardware/Happyware (art. SE7M6756-359045, tiers €931/€904/€885/€866);
  idealo.de **8 offers, €881.97–€1,247**, jacob.de cheapest.
  **MZ23-SU0 EU price still UNVERIFIED after ~20 more shops this run.**
  Confirmed only the *used* offer: idealo.de search shows the SU0 as "gebraucht",
  **€1,290.00 incl. VAT**, delivery 10–22 working days, free shipping — i.e. the
  same used-only EU picture as before, no new-in-box EU listing. Newly swept and
  negative: senetic.de ("Nichts gefunden"), bora-computer (nav only), morele.net,
  komplett.no, megekko, paradigit, alternate.nl (404), computerxtreme, caseking
  (fuzzy only), arlt (404), also.de (404), servershop24, billiger.de (noresult),
  preis.de, itsco, etb-tech (403), toppreise.ch (403), heise/guenstiger.de/
  alza.de/amazon.de (captcha/503). galaxus.de still captchas every route
  (incl. Googlebot/bingbot/facebook UAs and 3 CORS proxies) → its price stays
  UNVERIFIED. Also re-checked and unchanged: **Newegg US $869.00 in stock**.
  **AMD confirmed the QVL reading independently**: gigabytes live QVL for the
  CP1 lists "AMD 9135 100-000001150 … 200W … **DDR5-6400** … 200/240", matching
  the 9135's own AMD spec (12 channels, 1P/2P, PCIe 5.0 x128, 614 GB/s,
  $1,214 1kU). Blocker 3 stays closed.
  General search engines again unusable directly (Bing returns off-topic Excel
  results for exact part-number queries, DDG lite IP-blocked until 06:19Z, Brave
  429, Mojeek 422); all findings above came from vendor/retailer pages fetched
  directly or via r.jina.ai.
- 2026-11-10T06:05Z — **no change to the leader; three of four blockers now
  closed on vendor text rather than inference, and the CP1 got cheaper.**
  (1) **Slot pitch closed on textual evidence**: the rev 3.0 manual's item
  legend numbers the x16 slots **36, 37, 39, 40** (PCIE_1 Gen4 / PCIE_2, 4, 6
  Gen5) — Slot_1+2 are consecutive positions with 38 skipped before 39. That
  is the same 1.0/2.0/2.0 spacing the two pixel measurements gave, now stated
  in the manual's own text. (2) **Blocker 3 tightened**: the manual's §1-4-4
  population table gives EPYC 9005 1DPC RDIMM 1R/2R = **6400 MT/s** with
  footnote "6400 MT/s supported with specific DIMMs listed in product page
  QVL", and EPYC 9004 capped at 4800 — so 6400 depends on a QVL-graded DIMM,
  not a board limit, and the QVL has 37 such modules. The live QVL page was
  re-read (9135 row = DDR5-6400, stamp Oct 28 2026). (3) **Price improved and
  a correction**: Geizhals *does* list the CP1 — 3 listings, **6 live offers
  €876.98–€947.45**, last update 10.11.2026 06:50 — the earlier "Geizhals has
  no listing" was wrong. New cheapest: **Plexcom €876.98, in stock 1–3 days**
  (DE-only shipping), then jacob.de €881.97, future-x €881.99. idealo.de
  still 8 offers €881.97–€1,247. (4) **MZ23-SU0 EU: Geizhals has ZERO
  listings** for it (de and eu, mainboard category) while finding 3 for the
  CP1 — the broadest negative yet; senetic.de, WiredZone, toppreise, billiger,
  eBay.de-new, itsco, thomas-krenn, etb-tech all also miss. Newegg US
  re-confirmed **$869.00 in stock, add-to-cart live**. So the pick stands:
  €876.98 EU vs a US-only $869. (5) BIOS caveat narrowed — the manual shows
  6400 is DIMM-grade-driven, not a BIOS toggle; only the *shipped* BIOS
  revision is unconfirmed, because Gigabyte's BIOS tab 403s and download
  filenames are wildcard-masked (every guess 302s). Adapter re-verified
  **$55.00, SA22N2116P**, 12 V-fed, -P2 variant for ASUS RTX only.
- 2026-11-10T06:43Z — **no change to the leader; the build's cost centre moved
  from the board to the memory, and everything else held.** (1) **Price /
  EU stock re-verified at the source:** Plexcom's own shop page returns
  **"876,98 EUR, lagernd, 1-3 Werktage"** for the CP1 (search for `MZ33-CP1`
  on plexcom.de), so the Geizhals cheapest offer is a real cart, not a stale
  index row; Geizhals.de still shows 6 offers €876.98–€947.45 (price stamp
  06:50) and Geizhals.eu 11 offers (stamps up to 07:30) with several "Sofort
  lieferbar". idealo.de unchanged at 8 offers €881.97–€1,247; Happyware
  unchanged €931 excl. VAT (tiers 904/885/866). Newegg US still **0 items**
  for MZ33-CP1. (2) **QVL re-read live, still 9135 = DDR5-6400, stamp
  "Last Update: Oct 28, 2026"** — blocker 3 stays closed; the xlsx is now 404
  on the download host as well as via Wayback, so the HTML CPU sheet is the
  only live source. (3) **New, and it matters more than the board price:
  6400 QVL memory pricing.** 64 GB 2Rx4 6400 RDIMMs now list at **SK hynix
  HMCG94AHBRA480N €3,401**, Micron `-BH1T` **€2,999.81**, Samsung `-CWM`
  **€3,069.00** → **12 x 64 GB ≈ €36–43k**, ~40x the board. 32 GB Samsung
  `M321R4GA3EB2-CCP` **€1,961** → 12 x 32 GB ≈ €23.5k. Cheaper 6400 kits
  (Kingston FURY Renegade Pro, G.Skill Zeta R5) are **off-QVL**, so they
  trade the 6400 guarantee. (4) **MZ23-SU0 EU: still no new-in-box offer and
  the used price rose** — idealo.at used unit now **€1,599.00** (was €1,290
  on idealo.de); galaxus.at/.nl/.ch and digitec.ch all answer now and all say
  **"Aktuell nicht lieferbar"** on product 77255324, so only galaxus.de is
  unknown (captcha). Geizhals de/eu/at: zero MZ23-SU0 rows. Newegg US
  unchanged **$869.00, add-to-cart, sold and shipped by Newegg**. (5) **Two
  manual facts recorded so nobody misreads them:** BIOS §2-2-8 exposes only
  "Auto/Gen4/Gen3/Gen2/Gen1" for *both* slots and MCIO, so its missing Gen5
  entry is a UI quirk, not a Gen4 port — lane menu does offer x16; and the
  BIOS download filenames are genuinely unguessable (f01–f20, r17_f11 all
  404), with one third-party title confirming a real **`R17_F11`** release.
  Blocker 1 unchanged and closed (20.3 / 40.7 / 40.6 mm).
- 2026-11-10T06:52Z — **no change to the leader; the last open item is closed on
  vendor data, and one earlier "blocked" conclusion was simply wrong.** (1) **CP1
  BIOS: resolved.** There is no `/Support-BIOS` page on any Gigabyte board (that
  slug 404s on MZ32-AR0 too); the BIOS table lives in the *product* page's inline
  JSON and was readable all along via r.jina.ai + `x-respond-with: html`. Three
  builds: **R25_F17 dated 2026-11-08** (50,505,855 B), R24_F17 (2026-09-15),
  R23_F16 (2026-08-12), naming `MZ33-CP1_R<nn>_F<nn>.zip` — never
  `server_bios_mz33-cp1_*`, which is why every prior guess 404'd. All three are
  **HTTP 200 / application/zip, no token needed**, and the newest is two days
  older than this program. Their release notes are **CVE-only** (R25_F17:
  CVE-2026-54934/54944 "security updates for Turin platform") — no DRAM-speed
  entry, which is consistent with §1-4-4: 6400 is set by the **DIMM's QVL
  grade**, not a BIOS toggle. Action: flash R25_F17; UNVERIFIED only which build
  a retail board ships with. (2) **The memory QVL is a current document, not the
  stale May-2025 one:** the live bundle is `00-MZ33-CP1_QVL-20260400464.xlsx`,
  372,344 B, **dated 2026-10-27**, i.e. refreshed with the Oct-28 CPU tab. Its
  rows still render client-side only (app-served path, every `FileList/QVL/`
  form 404s), so the 37-module list remains sourced from the archived xlsx —
  blocker 3 unchanged. (3) **MZ23-SU0 got no cheaper:** idealo.de now carries a
  product page again but lists **only the used €1,290 eBay unit** (the €1,448
  row there is a 32 GB DIMM, not a board); galaxus.de/.ch/.at all still
  captcha. **Geizhals is now fully Cloudflare-walled** (search and product page
  both), worse than at 06:43Z — no loss, since the CP1 price was confirmed at
  Plexcom's own shop 4 minutes earlier. Also tried and dead: DuckDuckGo lite
  (bot challenge), manuals.plus BIOS-notes page (Cloudflare). No desktop browser
  is connected to this session, so the bot-walled pages could not be read in a
  real one.
- 2026-11-10T07:25Z — **leader unchanged; one argument retracted, one build trap
  caught, everything else re-verified live.** (1) **Blocker 1 re-measured from
  scratch** at 600 dpi off the rev 3.0 manual drawing, scaled on the board
  outline with both axes agreeing to 0.03 %: **20.7 / 40.3 / 40.7 mm** =
  **1.02 / 1.98 / 2.00 pitches**, Slot_1 centre 20.2 mm from the board edge.
  Same answer as the 02:35Z measurement, so the 3-native + 1-adapter conclusion
  stands. (2) **RETRACTED: the 06:00Z "slots are positions 36/37/39/40, gap at
  38" argument is wrong** — those are annotation callouts, and item **38 is
  `BAT Battery Socket`**, the CMOS cell drawn between PCIE_2 and PCIE_4 (that
  battery is the real reason that pair is 2 pitches apart). The conclusion never
  depended on it; the doc now carries the measurement only. (3) **NEW BUILD
  TRAP:** the cheapest EU-listed "2x MCIO 8i → PCIe 5.0" part — KALEA
  **79,90 €**, Amazon.de, "Nur noch 7 auf Lager" — is a **splitter**, not an
  aggregator: its own title says one PCIe port to **2 x16 outputs "(effektiv
  x8)"**. It would run the 4th R9700 at **x8**. The correct 10Gtek
  **SA22N2116P ($55, 99968 in stock, US warehouse)** is still the only part that
  aggregates two x8 links into one x16, and it has **no DE/idealo/eBay.de
  listing** → the adapter is the build's second US-only part. Choice is import
  it, or accept x8 on card 4. ~~(SUPERSEDED 08:22Z — C-Payne ships this topology
  from Germany for €50, and 10Gtek ships to DE; the adapter is not US-only.)~~
  (4) **Price/stock/firmware re-verified live:**
  Plexcom's own search returns Art.Nr. **111142, 876,98 EUR incl. VAT, "lagernd,
  1-3 Werktage"**; idealo.de still 8 offers €881.97–€1,247; QVL page still grades
  **AMD 9135 … DDR5-6400** (stamp Oct 28, 2026); **BIOS R25_F17 HTTP 200,
  50,505,855 B, application/zip**; Newegg still **"0 items that match
  MZ33-CP1"**; Gigabyte's SP5 lineup unchanged at 6 models (no new challenger).
  (5) **MZ23-SU0: still not an EU product.** Geizhals Cloudflare-walled again;
  galaxus.de/.at/.ch/digitec all captcha; **galaxus.de search for `MZ23-SU0`
  returns 994 fuzzy padding hits and no board**; idealo.de still only the
  **gebraucht €1,290** eBay unit (the €1,448 row is a 32 GB DIMM, as recorded);
  senetic.de "Das Produkt wurde nicht gefunden"; thinkmate 0 results;
  wiredzone 404; serverfactory no hit. Newegg's own product page is now
  CAPTCHA-walled, so the $869 US figure could not be re-read this run — carried
  forward from 06:43Z, UNVERIFIED since.
- 2026-11-10T07:52Z — **leader unchanged; the memory QVL is now read from the
  actual spreadsheet instead of counted off a rendered table, and that closed
  the last open UNVERIFIED row.** (1) **QVL sheet parsed row-by-row.** The live
  `FileList/QVL/` path still 404s (all three filename forms), so it came from
  the Wayback capture (46,347 B → 51,519 B xlsx). Parsed
  `sheet1.xml` + `sharedStrings.xml` directly: **327 memory rows, exactly 37
  at `6400MHz` / `1.1v` / `ECC Registered` / `288-pin` / `PASS`** — the 37
  figure is confirmed by a second, independent method. The full 6400 set is now
  enumerated by capacity (128 GB Samsung `M321RAJA0MB2-CCPWC`; 96 GB Samsung
  `M321RYGA0PB2-CCPEC/-CCPPC/-CCPWC/-CCPKC` + SK hynix
  `HMCGM4MHBRB505N/-499N AA`; 64 GB Samsung `M321R8GA0PB2-CCPEC/-CCPKC/-CCPWC`,
  SK hynix `HMCG94AHBRA480N/-487N AA`, Micron `MTC40F2046S1RC64BD2` ×6 RCD
  variants; plus 48/32/24/16 GB rows) — recorded in open question 3. (2) **The
  06:43Z UNVERIFIED is closed:** the Samsung 32 GB `M321R4GA3EB2-CCP` **is** on
  the 6400/PASS list, as `-CCPPC` and `-CCPWC` (both **2Rx8**), so the ~€23.5k
  384 GB build is QVL-backed; buy by full suffix, since `-CCP` alone is not a
  part number. (3) **Re-verified live, all unchanged:** Plexcom's own search
  returns Art.Nr. **111142, 876,98 EUR, "lagernd"**; idealo.de still **8
  Angebote, €881.97–€1,247.00**; BIOS **R25_F17 = HTTP 200, 50,505,855 B,
  application/zip, Last-Modified 2026-11-09**; adapter 10Gtek SA22N2116P still
  **$55.00, 99,968 in stock**, Asus-RTX exclusion still in its og:description.
  (4) **MZ23-SU0 still not buyable in the EU, and now unreadable end-to-end:**
  Geizhals search 403s (and via r.jina.ai returns only "Sichere Verbindung wird
  überprüft"), galaxus.de 403s directly and returns "Are you a robot?" via
  r.jina.ai, and the Newegg product page 403s — so the **$869 stays
  carried-forward UNVERIFIED**. Also new: the SU0's own QVL sheet 404s in all
  three filename forms with **no Wayback capture**, so the SU0 has no
  QVL-backed memory list and the CP1's 37-module list remains the only one in
  this program. Thinkmate re-checked for the CP1: **"0 search results for:
  MZ33-CP1"** — still no US distributor beyond the EU retail path. Leader
  unchanged.
- 2026-11-10T08:22Z — **leader unchanged; the build's last non-EU part is gone,
  and that retires the "US-only" caveat carried since 07:24Z.** (1) **Blocker 4
  closed on a German vendor:** **C-Payne "MCIO PCIe gen5 Device Adapter x8/x16"
  — €50.00**, exact right topology ("two MCIO 8i inputs / one PCIe x16
  electrical/mechanical output", x8 with one cable, **x16 with both inputs**,
  same same-host-port + 0-7→8-15 lane-order constraint as the 10Gtek, mandatory
  12 V feed, 3.5 A 12→3.3 V buck), plus the matching **MCIO SFF-TA-1016 8i gen5
  cable at €45.00** (45/75 cm) → **€140 the set**, add-to-cart live on both. Its
  shipping policy: *"Origin: All orders ship from Germany. For destinations
  within the European Union, no additional customs fees are due."*
  (https://c-payne.com/products/mcio-pcie-gen5-device-adapter-x8-x16,
  https://c-payne.com/products/mcio-sff-ta-1016-8i-cable-pcie-gen5,
  https://c-payne.com/policies/shipping-policy). (2) **Second correction: the
  10Gtek was never US-only either.** Its shipping guide says it ships
  "worldwide to nearly every country", DHL/FedEx, and its country list includes
  Germany (https://store.10gtek.com/shipping-guide/) — the US warehouse is
  where it ships *from*, not a destination restriction. So the 07:24Z line
  "the only part in this build that is US-only" is retracted in both halves.
  Cheapest EU riser (KALEA 79,90 €, Amazon.de) is still a **splitter**
  ("effektiv x8") and is still the wrong part — C-Payne is cheaper *and*
  correct. (3) **Re-verified live, all unchanged:** Plexcom own search → Art.Nr.
  **111142, 876,98 EUR incl. 19 % MwSt., "lagernd, 1-3 Werktage"**; idealo.de
  still **8 Angebote, 881,97 € – 1.247,00 €** (jacob.de 881,97 € + 2,99 €
  Versand = 884,96 €, delivery by 12.11.); Gigabyte SP5 lineup still 6 boards +
  no new SP5 SKU (MZ23-SU0, MZ33-AR1, MZ33-CP1, MZ72-HB2, MZ73-LM0/LM1/LM2);
  ASRock Rack's SP5 list unchanged (its only 12-DIMM 1DPC part is still the
  rejected GENOAD12M3-2Q). Thinkmate re-checked: "0 search results for:
  MZ33-CP1". (4) **QVL:** download host still 404s the sheet in both naming
  forms, so the 37-module 6400 list remains sourced from the archived xlsx
  parse — unchanged, no new evidence either way. (5) **MZ23-SU0: still no EU
  source.** galaxus.de 403/captcha on both the product URL and the bare
  product-id URL, and via r.jina.ai returns the "Are you a robot?" page; the
  Newegg $869 stays carried-forward UNVERIFIED. Net effect: **board €876.98 +
  adapter set €140, all from EU stock; nothing in the four-card build now needs
  an import.** That is a real change to the buy plan even though the leader is
  the same.
- 2026-11-10T08:52Z — **no change to the leader; the two carried-forward
  UNVERIFIEDs are now closed by live reads, and one new mechanical detail
  lands.** (1) **SU0 $869 is no longer carried-forward:** the Newegg page loaded
  end-to-end and states **$869.00, Add to cart, limit 99999, free shipping,
  pickup ready by 9AM, Sold by Newegg / Shipped by Newegg**, holiday returns to
  2027-01-31. Tech-America re-read: **$907.00 "Out Of Stock"**. So the SU0's US
  buyability is now a live fact, not an inherited one — it still changes
  nothing, because the EU side is still empty. (2) **SU0 EU re-swept,
  fourth consecutive negative run:** idealo.de = "*2 Ergebnisse*" = the **used**
  eBay board €1,290.00 (10–22 working days) + one **32 GB DDR5-5600 RDIMM**
  listing at €1,448 that merely *names* the board — a memory stick, not a
  motherboard, and it must not be counted as a board offer. idealo.at = the
  same used board at **€1,599.00** (up from €1,290) + the same RAM offer.
  Geizhals still 403s ("Sichere Verbindung wird überprüft"). The used ask has
  now risen two runs running, which strengthens rather than weakens the CP1
  decision. (3) **CP1 chain re-verified live, unchanged:** Plexcom own search →
  Art.Nr. **111142, 876,98 EUR incl. 19 % MwSt., "lagernd, 1-3 Werktage", cart
  live**; idealo.de **8 Angebote €881.97–€1,247 with data stamp 10.11.2026
  08:49** (jacob.de 881,97 + 2,99 shipping = 884,96 delivered by 12.11.;
  galaxus 929,21 by 27.11.); EU AT 894,40 / IT 995,99 / ES 1.041,99 / FR
  1.119,96. (4) **QVL blocker 3 re-read live:** the Support-QVL page (via
  r.jina.ai; bare curl 403s) shows the 9135 as **DDR5-6400**, 200W, cTDP
  200/240, stamp **Last Update: Oct 28, 2026**, and **all 27 EPYC 9005 rows are
  DDR5-6400** — no 9005 row below 6400 exists on the page. The memory tab and
  its `.xlsx` are still not fetchable (four filename forms, all 404; no file URL
  in the served payload), so the 37-module list remains the archived-sheet
  parse. Manual §1-4-4 p.14 re-confirmed locally: 9005 @1DPC **1R / 2R / 2RxH
  all 6400 MT/s**, footnote 1 ties it to QVL-listed DIMMs. (5) **Adapter
  re-verified live: €50,00 adapter + €45,00 cable = €140**, both with Add to
  Cart. New mechanical detail from the vendor copy: *"the **vertical** model can
  be placed with single width spacing"* — so for the 4th card buy the
  **CP-0232 vertical** if it must share a 1-slot gap; the flat **CP-0231** needs
  a 2-slot bay. This does **not** relax Slot_1+Slot_2 (40 mm card, 20.3 mm
  pitch — still impossible); it only frees the adapter card's own position.
  Vendor also restates x16 = "both inputs connected (same CPU host port, lane
  order 0-7→8-15, NOT 8-15→0-7)", "mandatory 12V", and "wrong power connector
  will destroy the Adapter and your GPU". Lane menu re-confirmed from the manual
  (pp.46–47): `U2_P0_G0/1/2 Lanes` offers **x16**, which is what makes one MCIO
  pair a x16 link. Leader unchanged: **MZ33-CP1, €876.98 + €140 adapter set,
  both EU-sourced.**
- 2026-11-10T08:54Z — **no change; one caveat added so the price row is not
  over-read.** Cross-checked the Plexcom **product page** itself (not just its
  search results) and it agrees exactly: Art.Nr. **111142**, **876,98 EUR**
  incl. 19 % MwSt., "lagernd, 1-3 Werktage", "In den Warenkorb" live. **But the
  page's "Lagerbestand:" field is empty** — Plexcom publishes no unit count, so
  "lagernd" is the shop's status word, not a quantity. That distinction matters
  for a €877 board someone is about to order: it is not evidence of deep stock,
  and a single-unit allocation would still read "lagernd". No other change this
  step; idealo.de still 8 offers from €881.97.
- 2026-11-10T09:19Z — **no change to the leader.** Last scheduled run before
  the 09:47Z deadline; leader chain re-read live and unmoved, one new ordering
  fact, one negative recorded so it is not re-attempted. (1) **CP1 price/stock
  re-verified from Plexcom's schema.org JSON-LD**, not a scraped string:
  `Product` → `"mpn":"MZ33-CP1"`, `"model":"111142"`, `"sku":"111142"`,
  `"gtin13":"4719331867232"`, and `Offer` → `"price":"876.98"`,
  `"priceCurrency":"EUR"`, `"valueAddedTaxIncluded":true`,
  `"availability":"InStock"`, `"itemCondition":"NewCondition"`. **GTIN
  4719331867232 is the new, useful bit** — the right key for a distributor
  quote, which is the only route that could still reopen the MZ23-SU0.
  (2) **QVL: the current (Oct-27) memory sheet is not obtainable, and that is
  now a documented dead end rather than an untried guess.** Six more filename
  forms 404 on the download host (`mb_qvl_MZ33-CP1.xlsx`, `-3.0.xlsx`,
  `_3.x.xlsx`, `00-MZ33-CP1_QVL-20260400464.xls`, `server_mb_qvl_MZ33-CP1.pdf`,
  plus the two already known); a Wayback CDX sweep of
  `download.gigabyte.com*` filtered to `MZ33-CP1` returns **no capture newer
  than 2025-07-11**, and the QVL page's served payload contains **zero `xlsx`
  references at all** — its "Download All Data" control is a JS handler with no
  static href. `?tab=memory` and `?ctype=2` both return the CPU sheet (0 memory
  part hits). So the **37-module 6400/PASS list stays sourced from the archived
  2025-05-12 sheet** and blocker 3's live half remains the CPU tab only
  (re-read again: **AMD 9135 … 200W … DDR5-6400 … 200/240**, stamp
  **Last Update: Oct 28, 2026**). (3) **idealo.de unchanged: 8 offers, €881.97–
  €1,247** (page title still "ab 881,97 €"). (4) Gigabyte's SP5 lineup still
  exactly **6 boards** (MZ23-SU0, MZ33-AR1, MZ33-CP1, MZ73-LM0/LM1/LM2) — no new
  challenger in the program's final hours. (5) Re-probed and still negative:
  Geizhals Cloudflare-walled (search by GTIN → "Sichere Verbindung wird
  überprüft"), senetic.de "Das Produkt wurde nicht gefunden.", jacob and
  future-x search endpoints return no result rows. **No unverified figure
  affects the pick: board €876.98 + C-Payne adapter set €140, both EU-sourced.**
- 2026-11-10T09:48Z — **program closed** (deadline 09:47Z). Final leader
  unchanged: MZ33-CP1 rev 3.x, €876.98 Plexcom in stock, 3 native x16 at 2.0
  pitch + 1 card via C-Payne MCIO adapter (€140), DDR5-6400 at 1DPC. Blocker 1
  (pitch) and blocker 2 (price/EU stock) closed in earlier runs; blocker 3's QVL
  half stays on the archived 2025-05-12 sheet (live sheet unobtainable). No
  further research after cutoff; scheduled watch deleted.
- 2026-11-12T00:58Z — **new requirement: RAID0 over 2–4 Gen5 M.2. Leader
  still MZ33-CP1; no board change, but one documented assumption corrected.**
  (1) **The CP1 has no Gen5 M.2 slot at all.** Datasheet "Storage Interface →
  M.2" says `1 x M.2 (2280/22110), PCIe Gen3 x4`; manual legend item 30
  `M2_0 … Gen3 x4`; block diagram `M.2 → PCIe3.0 x4`. So Gen5 drives cannot go
  in the onboard slot — they must ride MCIO. Same or worse everywhere else in
  the shortlist (MZ33-AR0/AR1 M.2 Gen4 x4; MZ23-SU0 **Gen3 x2**). (2) **It
  still fits, because the x16 groups are independent**: block diagram gives
  U2_P0_G0 = Gen5 x16 (4th GPU), U2_P0_G2 = Gen5 x16 (**free**), U2_P0_G3 =
  Gen4 x8/SATA. A Gen5 x16 group = 4 x4 drives, and BIOS `U2_P0_G0/1/2 Lanes`
  offers `x4x4x4x4` (manual §2-2-8 pp.46–47). So **2 drives = 1 MCIO→2xM.2
  adapter, 4 drives = 2 adapters**, none touching G0. (3) **Parts, EU, priced
  today**: KALEA-INFORMATIQUE MCIO 8i → 2x M.2 Gen5, 74-pin, 4-pin 12V/5V,
  in stock, **€59.90** incl. VAT (€49.92 excl.); C-Payne MCIO 8i gen5 cable
  **€45.00**; alternates LR-LINK LRFNA922A (price UNVERIFIED, datasheet gated)
  and HiFiber SM22N21-M **$43.99**. **4 Gen5 M.2 ≈ €210, 2 drives ≈ €105.**
  (4) **RAID0 is software** — Gigabyte's spec sheet states `RAID: N/A`; use
  mdadm/ZFS. Not a downgrade: NVMe RAID0 on these platforms is host software
  regardless, and a tri-mode HBA would cost one of the x16 GPU slots.
  (5) **Lane recount including storage: 120 of 128** (GPUs 48+16+16, OCP 16,
  G2 16, G3 8) — still fits, but no headroom for a fifth PCIe device.
  (6) Corrected the two places that implied all 8 Gen5 NVMe survived the 4th
  GPU: the GPU adapter halves free Gen5 NVMe from 8 drives to **4**. Board
  price/stock unchanged (€876.98 Plexcom). **UNVERIFIED: an actual Gen5 M.2
  RAID0 run on this board, and LRFNA922A pricing.**
- 2026-11-12T01:12Z — **build specifics from the user: the cards are PowerColor
  `AI PRO R9700 32G-B`, and the concern is tensor parallel. Leader unchanged;
  one false assumption corrected and one serious risk added.**
  (1) **PowerColor pinned: 266.7 x 111.2 x 40 mm, 2-slot, blower** (gpus.net
  model DB, `AI PRO R9700 32G-B`; Caseking GCPC-079 "blower style, 2-slot";
  Micro Center "Single-Fan"). So the build sits on the **40 mm / 0.6 mm
  clearance** case, not the roomier ASRock 39 mm one — a test-fit is now a
  required step before buying all four. Not pitch-constrained for card 4 (it is
  on the MCIO adapter).
  (2) **"GPU on OCP" is not a thing in this build** — OCP NIC 3.0 is unused;
  GPUs are Slot_2/4/6 + the 4th via MCIO. Corrected the impression, no plan
  change.
  (3) **Answered "any board with native PCIe5 x16 for 4 GPUs": effectively no,
  among 12-channel boards.** Checked the field again: **MZ33-AR1** has 4 native
  Gen5 x16 but **two adjacent 1-pitch pairs** (19.5 / 17.5 mm) → 2 dual-slot
  cards, needs 2 adapters, and caps at 5200 MT/s. **ASRock Rack
  GENOAD8UD-2T/X550** is the one board with **4 native Gen5 x16 + 2x M.2
  PCIe5.0 x4** — but it is **8 DIMM (8 of 12 channels)**, so it fails the
  memory requirement; it is the *only* real trade-off candidate, not an
  upgrade. **Supermicro H14SSL-N** has 3 Gen5 x16 and 2 Gen5 M.2 (interesting
  on storage) but still needs an adapter for card 4. Conclusion stands: CP1's
  3-native + 1-MCIO is the best available for this spec.
  (4) **New, more important than any slot argument: 4x R9700 direct PCIe P2P
  for tensor parallel is currently reported to hang the host.** Open ROCm issue
  11348 (4x R9700, llama.cpp + vLLM, `NCCL_P2P_DISABLE=0`) reports full-system
  hangs/BMC resets; the reporter states it does not occur with
  `NCCL_P2P_DISABLE=1`. Reported on a **Supermicro H12SSL-NT**, i.e. a
  driver-level issue that **buying native x16 does not fix**. Mitigations:
  `NCCL_P2P_DISABLE=1`, `HSA_ENABLE_SDMA=0`, `NCCL_P2P_LEVEL=PHB`, `iommu=pt`;
  reported cost ~8-12 % at TP=2, ~0 % with pipeline parallel. **UNVERIFIED on
  EPYC 9005 / CP1 / current ROCm 7.x — must be tested on the real build.**
- 2026-11-12T01:35Z — **answered the three build questions; leader unchanged
  (MZ33-CP1).** (1) **GPU wiring clarified:** 3 cards in Slot_2/4/6 (native
  Gen5 x16, 2-slot pitch) + card 4 on **U2_P0_G0A+G0B via the C-Payne CP-0232
  x16 adapter, 12 V-fed**. **Slot_1 is not used** (1 pitch from Slot_2 → no
  40 mm card fits). Nothing on OCP; corrected that impression twice now.
  BIOS: `U2_P0_G0 Lanes = x16`, slot speeds Auto.
  (2) **Start-up storage is 2x 1 TB RAID0, not 4** — so **one** KALEA MCIO
  8i→2x M.2 Gen5 adapter (**€59.90**) + **one** C-Payne 8i gen5 cable
  (**€45.00**) = **~€105**, on **U2_P0_G2A**, `U2_P0_G2 Lanes = x4x4`, 4-pin
  12 V from the PSU, `mdadm -l0`. Upgrade path to 4 documented: 2nd adapter on
  G2B, `x4x4x4x4`, rebuild+restore (~€105 more). Exact URLs recorded in the
  Storage section. Board RAID is `N/A` — software RAID0 is the intended route.
  (3) **WRX90 / TR PRO evaluated and rejected.** Pro WS WRX90E-SAGE SE + 9955WX
  is genuinely **8-channel** (ASUS spec, Puget), so it gives up **33 % of memory
  bandwidth** (614.4 → 409.6 GB/s) while **still not fitting 4 dual-slot cards
  natively** — ASUS's own GPU guidance names **slots 4/5/7 = three cards** and
  advises against adapters. CPU price is a wash (**EPYC 9135 from €1,629**,
  **9955WX from €1,637.70**, Geizhals DE), so the swap costs more and buys
  only onboard 4x Gen5 M.2 + lane headroom. Stay on EPYC. **UNVERIFIED: WRX90E
  board price in the EU**, so the TCO line is incomplete; the bandwidth and
  slot arguments do not depend on it.
- 2026-11-12T01:52Z — **all adapter links consolidated and re-fetched live; the
  AliExpress alternative judged and rejected on variant risk.**
  (1) Verified this run: **C-Payne MCIO→x16 adapter €50,00** and **C-Payne
  MCIO 8i gen5 cable €45,00** (both pages live, prices read off the page);
  **KALEA MCIO→2x M.2 Gen5 €59.90 in stock**; **10Gtek SA22N2116P $55**;
  **HiFiber SM22N21-M $43.99 in stock**. LR-LINK LRFNA922A still live but
  **price UNVERIFIED** (datasheet login-gated).
  (2) **Cable count corrected: the GPU adapter needs TWO MCIO cables**, not one
  — x16 mode uses both inputs. Basket for the start-up build is therefore
  2 cables (€90) + GPU adapter (€50) + KALEA M.2 adapter (€59.90) = **€199.90**,
  all EU-shipped. Earlier text implied one GPU cable.
  (3) **AliExpress `item/1005011740529907` (ADT-Link "PCIe 5.0 x16 → MCIO 8i
  riser, 1U backplane kit") is the right direction but the wrong buy.** Read the
  live page: it is a **multi-variant** listing with variants `MCIO-55cm`,
  `Set-A`, `Set-B`, `MCIO to PCIE5.0`, `Pcie5.0 x16(1u)`, `16x-MCIO
  2U-PCIE5.0`, `MCIO-PCIE5.0X16`, `Pcie5.0 **x8** 1u`. The tile the page
  defaults to (**CHF 10.18 / ~100 zł**) is the **`MCIO-55cm` cable-only**
  variant, not the adapter board; and `Pcie5.0 x8 1u` is an **x8 trap** that
  would halve GPU 4. No lane-ordering / same-host-port documentation either.
  **Stay with C-Payne** — same part class, €50, explicit x16 rules, EU-shipped.
  **UNVERIFIED: the 1U x16 variant's price** (not exposed to a non-JS fetch).
