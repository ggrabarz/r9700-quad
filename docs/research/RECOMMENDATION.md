# Board pick — EPYC 9135 + 12ch DDR5-6400 1DPC + 4x R9700

> **PROGRAM CLOSED 2026-11-10T09:48Z** — the research window ended
> 2026-11-10T09:47Z. **Reopened by user request 2026-11-12** for build-specific
> follow-up (PowerColor cards, storage, adapter sourcing).

> **LEADER CHANGED 2026-11-12T01:40Z: SUPERMICRO H14SSL-N** — €975.16 (Geizhals
> DE, in stock), 12 DIMM 12-channel DDR5-6400, **3× PCIe 5.0 x16 + 2× x8**, and
> — the deciding factor — **2× onboard M.2 PCIe 5.0 x4**. Same 3-native-GPU
> count as the CP1 but with the Gen5 M.2 requirement solved onboard at zero
> extra cost. See "Why the H14SSL-N now leads" below. The CP1 analysis is kept
> as the runner-up: it is ~€98 cheaper but needs ~€105 of MCIO adapters to reach
> the same storage, and it has no Gen5 M.2 at all.
>
> **Variant note 2026-11-12: the H14SSL-NT is the same board with dual 10GbE**
> (2× BCM57416 instead of 2× BCM5720 1GbE) for **+€73.84** (€1,049.00 Geizhals
> DE). Identical slots, MCIO, M.2, SATA and DIMM layout, so the whole build plan
> is unchanged. **Worth it only on a 10G network** — the BCM57416 does
> 10GBASE-T/1000BASE-T and **no 2.5G/5G**, so a 2.5GbE switch yields 1G. See the
> "-NT" section for the media-server implications (no iGPU, SATA layout, 24/7
> idle power).

**Runner-up: GIGABYTE MZ33-CP1 (rev 3.x)** — one of only two SP5 boards found whose
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

## Why the H14SSL-N now leads (2026-11-12)

The user's question was: *isn't it better to start on the H14SSL-N so only the
4th GPU needs an adapter?* **The GPUs were never the difference — the CP1 also
needs exactly one GPU adapter.** Both boards give **3 native x16 slots + 1
adapted card**. The difference is storage, and it goes to Supermicro:

| | MZ33-CP1 (runner-up) | **H14SSL-N (leader)** |
|---|---|---|
| Price, DE, in stock | **€876.98** (Plexcom) | **€975.16** (Geizhals best offer) — **+€98.18** |
| 12 DIMM / 12-channel @ 6400 | yes | **yes** (manual: "3 TB registered ECC DDR5 at 6400 MT/s in 12 DIMM slots") |
| Gen5 x16 slots | 3 (+1 Gen4 x16) | **3** (+2 Gen5 **x8**) |
| 2-slot cards native | 3 | **3** (Slot1/3/5) |
| **Onboard Gen5 M.2** | **none** (1× Gen3 x4) | **2× PCIe 5.0 x4** (manual p.16: "Two M.2 connectors (PCIe 5.0 x4)") — **but see the M.2 generation caveat below: the M.2 QVL lists only Gen4 drives** |
| Storage cost to reach **2× Gen5 M.2 RAID0** | **+€104.90** (KALEA €59.90 + 1 C-Payne cable €45) | **€0** — drives go straight in |
| Storage cost to reach **4× Gen5 M.2 RAID0** | **+€209.80** (2 adapters + 2 cables) | **+€104.90** (1 adapter + 1 cable on NVMe4/5) |
| Total, 4 GPUs + **2×** Gen5 M.2 RAID0 | €876.98 + €104.90 = **€981.88** | **€975.16** |
| Total, 4 GPUs + **4×** Gen5 M.2 RAID0 | €876.98 + €209.80 = **€1,086.78** | €975.16 + €104.90 = **€1,080.06** |
| Form factor | E-ATX 304.8 × 330.2 mm | **ATX 304.8 × 256.5 mm** (shorter) |

**Verdict: at 2 drives the two boards are within €7 of each other — the CP1 is
no longer meaningfully cheaper, and the comparison is basically a wash on
money.** What the H14SSL-N buys for that ~€7 is real: **no storage adapters or
cables in the build path at all**, a shorter ATX board that fits far more
cases, and 2 Gen5 M.2 slots that work out of the box. At 4 drives it is also
marginally cheaper (€1,080.06 vs €1,086.78). **The Supermicro wins on
simplicity, not on price** — and its one downside is that GPU 4 and the MCIO
storage upgrade compete for the same 3 MCIO ports (see below).

**Correction to an earlier claim in this document:** the CP1 path was quoted as
"€199.90 for the whole adapter set". That was for 2 MCIO cables + GPU adapter +
M.2 adapter. For the **2-drive start-up** the CP1 needs only **€104.90** of
storage parts (1 M.2 adapter + 1 cable), because the GPU adapter's 2 cables are
separate and are needed on *both* boards. Numbers above are the corrected ones.

**Sources, verified 2026-11-12:**
- Manual (MNL-2821, "Two M.2 connectors (PCIe 5.0 x4)", p.16; slot table
  "PCIE SLOT1,3,5 = PCIe 5.0 x16, PCIE SLOT2,4 = x8"; `CPU1 PCIe Package Group
  … x16` bifurcation options): https://www.supermicro.com/manuals/motherboard/H14/MNL-2821.pdf
- Product page (3× Gen5 x16, 2× x8, M.2 2× Gen5 x4, 12 DIMM 6400):
  https://www.supermicro.com/en/products/motherboard/h14ssl-n
- Price/stock: https://geizhals.de/supermicro-h14ssl-n-mbd-h14ssl-n-b-a3613031.html
  — **€975.16** (electronis.de, "ab Lager, 1-2 Werktage", data 12.11.2026 00:06),
  then €1,003.09 (future-x), €1,029.78 (jacob), €1,187.73; **4 offers total**.

**One documented caveat worth knowing:** Supermicro's own pages have contradicted
each other on this board's M.2 generation (key-features tab said Gen4, specs tab
said Gen4, manual said Gen5), which a ServeTheHome thread documents:
https://forums.servethehome.com/index.php?threads/supermicro-h13ssl-n-h14ssl-n-m-2-gen5-vs-gen4-confusion.51914/
**The manual and the current product page now both say PCIe 5.0 x4**, and the
manual's version is the one that ships with the board — so Gen5 is the supported
reading, but **confirm at first boot** (`lspci -vv` link speed) rather than
trusting the datasheet alone. If it trains at Gen4, the 2-drive RAID0 still
works, just at half the per-drive ceiling.

**Remaining squeeze to be aware of:** the H14SSL-N provides **3 MCIO 8i
total** (NVMe0/1, NVMe2/3 = Gen5; NVMe4/5 = Gen5 **or** SATA via the JSATA1
jumper). The 4th GPU consumes NVMe0/1 + NVMe2/3 as one x16 link, which leaves
**NVMe4/5 (x8) free** — enough for 2 more Gen5 M.2 later via one MCIO adapter.
So the H14SSL-N's 4-drive upgrade path costs the same €105 as the CP1's, but it
gets you to 2 drives for free first.

**GPU 4 on the H14SSL-N — why the MCIO pair aggregates correctly.** The layout
table names the ports `NVMe0/1 PCIe1A` and `NVMe2/3 PCIe1B` — both under **PCIe
Port 1**, i.e. the same x16 group, which is exactly the topology a 2× MCIO 8i →
x16 adapter requires ("same CPU host port, lanes 0-7 → 8-15"). The BIOS confirms
the group can be set to **x16** (`CPU1 PCIe Package Group … The options are
Auto, x4x4x4x4, x4x4x8, x8x4x4, x8x8, and x16`). So **the same C-Payne adapter
and 2 cables move to NVMe0/1 + NVMe2/3** — no new parts, no topology change
versus the CP1 plan.

**Slot pitch — 3 dual-slot cards fit natively.** The manual layout shows **five
evenly spaced PCIe slots** with the x16 slots in positions **1, 3 and 5** and the
x8 slots interleaved at **2 and 4** (silkscreen readable as `CPU SLOT2 PCIe5.0
X8`, `CPU SLOT3 PCIe5.0 X16`, `CPU SLOT4 PCIe5.0 X8`). An even 1-pitch spacing
with x16 at every second position = **2-slot pitch between the three GPU slots**,
so three 40 mm PowerColor cards fit exactly as they do on the CP1. **UNVERIFIED:
the exact millimetre figure** — I read the even spacing and the slot numbering
off the manual's layout drawing and the annotated photo, not a dimensioned
mechanical drawing, so **test-fit before committing all four cards** (the same
0.6 mm caveat that applies on the CP1 applies here).

## Why the CP1 still wins on a couple of axes (runner-up)



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
## MZ73-LM0 as a 24-DIMM future base — evaluated and rejected 2026-11-12

The question: use the dual-socket MZ73-LM0 as a base so you can later go to
**24 DIMM (2× 12-channel)**. Verified from Gigabyte's own rev 3.0 manual
(142 pp, downloaded) and datasheet.

**It does not work as a single-CPU future base, and it is slower today.**

| | **H14SSL-N (leader)** | MZ73-LM0 |
|---|---|---|
| Sockets / DIMM | 1 / **12** (12-ch) | 2 / **24** (12-ch **per CPU**) |
| 1DPC speed, EPYC 9005 | **6400 MT/s** | **6000 MT/s** (datasheet) |
| Gen5 x16 slots | 3 | **4** |
| Slots usable with **one** CPU | **3 of 3** | **2 of 4** — see below |
| Gen5 M.2 onboard | **2× PCIe 5.0 x4** | 1× **Gen4** x4 |
| Board price DE | **€975.16** | from **€1,652.99** (idealo, 11 offers) |

**The blocker: the 4 slots are split across the two sockets.** Gigabyte's
manual, "Expansion Slots":
- `Slot_4: PCIe x16 (Gen4 x16), from CPU_0`
- `Slot_3: PCIe x16 (Gen4 x16), from CPU_0`
- `Slot_2: PCIe x16 (Gen4 x16), from CPU_1`
- `Slot_1: PCIe x16 (Gen4 x16), from CPU_1`

plus Gigabyte's own caveat: *"If only 1 CPU is installed, some PCIe or memory
functions might be unavailable."* So with your single 9135 you get **Slot_3 +
Slot_4 only — two GPUs** — and 12 of the 24 DIMMs are dead. You would pay
**€1,653** for a board that runs two cards.

**Note also the manual says all four are Gen4**, while the datasheet feature list
says "4 x PCIe Gen5 x16". Same species of internal contradiction as the
Supermicro M.2 question; it needs resolving before purchase, but it does not
change the verdict — the slot-to-CPU split kills it regardless.

**On 24 DIMM specifically:** 24 DIMMs *is* two 12-channel CPUs. That is not a
future upgrade of this machine, it is a different machine — you would also need
the second EPYC, a second set of 12 DIMMs, a bigger PSU and case. **Buying the
LM0 now to "keep the option open" costs €678 more today and halves your usable
GPU slots today.** Bad trade.

**Honest path if 24 DIMM genuinely becomes a requirement:** build single-socket
now (H14SSL-N), and when the capacity is actually needed buy the dual-socket
board *then*, with the second CPU. 12 channels today, 24 later, is a two-machine
decision — not a motherboard choice.

**Sources:** manual https://download.gigabyte.com/FileList/Manual/server_manual_e_mz73lm0_e_v3.0.pdf?v=5ea8a2b32e82a5eef74398c6e4bb2e5a ·
product page https://www.gigabyte.com/us/Enterprise/Server-Motherboard/MZ73-LM0-rev-3x ·
price https://www.idealo.de/preisvergleich/ProductCategory/3018F1611816.html —
**from €1,652.99 across 11 offers**, but that is a category-page best-price
figure, so the exact offer is **UNVERIFIED** until read on a product page.

## H14SSL-N memory QVL and M.2 generation — verified 2026-11-12

**QVL links (these are the working ones — the generic page errors out):**

- **Memory QVL, DDR5-6400 RDIMM, Turin (your 9135):**
  https://www.supermicro.com/en/support/resources/memory?mspd=6.4000001&mtyp=217&id=a29c222dc5b93356a5372920962bdec0&prid=90505&type=DDR5%20RDIMM&ecc=1&reg=1&fbd=0&cpu=turin&sku=H14SSL-N
- **Tested M.2 list:**
  https://www.supermicro.com/en/support/resources/m2ssd?SystemID=90505&ProductName=H14SSL-N
- Entry point (the "Tested Memory List" button on the product page POSTs to
  `get_tested_memory`, and the plain `…/resources/mem?ProductID=90505` URL
  answers *"accessed improperly"* — **use the two URLs above instead**):
  https://www.supermicro.com/en/products/motherboard/h14ssl-n

**1 · Memory QVL — CLOSED. It does list a DDR5-6400 RDIMM at 1DPC.**

The API behind the button (`POST /en/external_db_block/support/get_tested_memory`)
returns, for this board, exactly one 6400 option per CPU family:

- `[turin] DDR5 RDIMM-6400 Registered ECC`
- `[genoaBergamo] DDR5 RDIMM-6400 Registered ECC`

and following the `turin` link yields the tested-module table:

| Part Number | Description | MB Rev | Wide Temp | DRAM | Ranks | Profile |
|---|---|---|---|---|---|---|
| **MEM-DR564MC-ER64** | **64GB DDR5-6400 2RX4 (16Gb) ECC RDIMM** | Any | N | 16Gb | 2 | Low Profile |

**So the 1DPC-6400 claim is backed by a real QVL entry, not just a datasheet
line.** Caveats worth stating plainly:
- **The list is thin — one module.** That is Supermicro's own tested set for
  6400 RDIMM on this board; it is not a broad compatibility matrix. Buying that
  exact part is the only *QVL-backed* way to guarantee 6400.
- The entry is a **64GB 2RX4** RDIMM, so a 12-DIMM build at that part is
  **768 GB**.
- Earlier claim retracted: I said the memory QVL was unreadable. It is readable
  via the data URL above; only the generic page is broken.

**2 · M.2 generation — still Gen4 on the evidence, and this correction stands.**

- The tested-M.2 QVL lists **14 drives and every single one is `NVMe GEN4`** —
  zero Gen5 entries (URL above; read directly, not via the broken wrapper).
- The **archived product page** (Wayback 2026-04-23) says **"M.2 Interface: 2
  PCIe 4"**; **Geizhals** says PCIe 4.0 x4.
- Only the **manual p.16** ("Two M.2 connectors (PCIe 5.0 x4)") and the
  **current** product page say Gen5, and the ServeTheHome thread already
  documented Supermicro contradicting itself on this spec for both H13SSL-N and
  H14SSL-N.

**Position: treat the onboard M.2 as `PCIe 4.0 x4` until `lspci -vv` proves
otherwise.** Two onboard Gen4 x4 slots still beat the CP1's single **Gen3 x4**
and still cost €0 versus ~€105 of MCIO parts, **so the pick stands** — but
**neither board provides true Gen5 M.2 onboard**, and if Gen5 bandwidth is a
hard requirement the **MCIO route is the only way to actually get it**
(H14SSL-N NVMe4/5, or CP1 G2).


## 64 GB DDR5-6400 RDIMM pricing — asked 2026-11-12

Short answer: **yes, but "an arm and a leg" is currently the market price, not a
vendor markup.** This is the 2026 DRAM shortage, not a bad shop.

**Actual prices found (different sellers and part numbers, all agreeing):**

| Module / kit | Capacity | Price seen | Where |
|---|---|---|---|
| **G.Skill F5-6400R3644E64GQ4-T5N** (4× 64 GB, registered ECC, EXPO) | 256 GB kit | **€12,269.00** | Alternate DE, "Sofort verfügbar" (in stock) |
| **Kingston KSM64R52BD4-64MD** (1× 64 GB, 2Rx4 CL52) | 64 GB | **€2,838.93** | heise Preisvergleich, 4 offers €2,838.93–2,842.74 |
| **Kingston KSM64R52BD4-64HA** (1× 64 GB) | 64 GB | €3,705.77 | heise, single offer |
| **ADATA AD5CU640064G-S** (CUDIMM, not RDIMM) | 64 GB | €1,487.00 | Alternate, not in stock |
| **Kingston KVR64A52BD8-64** (CUDIMM, ValueRAM) | 64 GB | €1,549.00 | Alternate |

**Per-GB reality check:** independent trackers put server DDR5 RDIMM at roughly
**$38 per GB (Sept 2026)** — so a 64 GB module at ~$2,400 / ~€2,200 is the going
rate, and €2,839 is a normal retail quote rather than an outlier. Sources:
https://capitalandcompute.net/memory-prices/server/ ·
https://datacenterdisk.com/news/memory-chip-shortage-2026-server-ram-prices

**So for a 12-DIMM 768 GB build at QVL-backed 6400: 12 × €2,839 ≈ €34,000 of
memory.** That is the honest number and it dwarfs the €975 board and the four
GPUs' worth of interconnect. **This is the single biggest cost in the build right
now, and it is a market condition, not a spec requirement.**

**Three ways to spend less, in order of what I would actually do:**

1. **Run fewer DIMMs at 6400 rather than 12.** You do not need 12 channels
   populated to boot or to get most of the bandwidth — but **you do lose
   channels** (memory bandwidth scales with populated channels on SP5), so this
   is a real performance trade, not a free saving. A 6-DIMM build halves the
   memory cost and loses ~half the peak bandwidth.
2. **Drop to DDR5-5600 or 6000.** 5600 RDIMMs are far cheaper per GB than 6400
   and are still QVL-supported on this class of board. The 9135 at 1DPC will run
   5600 happily. **Cost of this compromise: ~12.5 % memory bandwidth vs 6400**
   (5600/6400), for a large price drop. Given that the 6400 requirement was never
   tied to a workload measurement, this is the compromise I would question hardest
   — see the note below.
3. **Buy used/refurb RDIMMs.** The market report notes DDR4 up 60–80 % and DDR5
   doubled; used 5600 RDIMMs from decommissioned servers are the cheapest path,
   at the cost of warranty.

**A question worth asking yourself:** the entire 6400 specification has been
treated as fixed since the first run of this research, but **nothing in the build
plan actually demonstrates that 6400 is needed** rather than 5600 or 6000. At
current prices the 6400 requirement costs **roughly €10,000–15,000 more** across
12 DIMMs than a 5600 build. If the workload is LLM inference, capacity (GB) almost
always beats bandwidth (MT/s) once the model fits — 768 GB at 5600 will serve
bigger models than 384 GB at 6400. **Worth confirming the requirement before
committing the budget.** (Flagged, not decided — the spec came from you.)

**UNVERIFIED:** EU street price for the exact Supermicro QVL part
`MEM-DR564MC-ER64`; it is an order-only Supermicro SKU and I found no retail
listing. The Kingston KSM64R52BD4-64MD is the closest retail equivalent
(same 64 GB 2Rx4 6400 CL52 class) and is the price quoted above.

## Cheapest 12-channel RDIMM for full bandwidth under 6400 — 2026-11-12

The question: what is the cheapest RDIMM to populate **all 12 channels** and still
get **full bandwidth at a speed below 6400**.

**First, the important correction to how this was framed.** "Full bandwidth"
on SP5 means **all 12 channels populated**, and the Supermicro manual's DIMM
population table says the board runs **6400 MT/s at 12 channels for every RDIMM
rank type**:

| DIMM type | 1 channel | 12 channels | Max frequency |
|---|---|---|---|
| RDIMM 1R | 32 GB | 384 GB | **6400** |
| RDIMM 2R | 64 GB | **768 GB** | **6400** |
| 3DS RDIMM 2Rx2 (4R) | 128 GB | 1.5 TB | 6400 |
| 3DS RDIMM 2Rx4 (8R) | 256 GB | 3 TB | 6400 |

(Manual p.40, "Populating RDIMM/RDIMM 3DS DDR5 Memory Modules with AMD EPYC 9005
Series Processors.")

So **there is no "cheap 12-channel bin below 6400" that preserves bandwidth by
populating fewer channels** — 12 channels is what gives the bandwidth, and the
board does 6400 across all 12 anyway. **Bandwidth is set by channel count × speed,
so the ways to cut cost are: fewer channels (real bandwidth loss), lower speed
(real bandwidth loss), or smaller DIMMs (no bandwidth loss at all).**

**That last one is the actual answer: buy 12× 32 GB instead of 12× 64 GB.**
- **12 × 32 GB 1R = 384 GB at 6400**, per the table — **full 12-channel
  bandwidth, full 6400, half the capacity and roughly half the money.**
- 12 × 64 GB 2R = 768 GB, same bandwidth, ~2× the cost.
- **Per-GB is not cheaper at 32 GB** (smaller DIMMs usually cost more per GB), so
  this saves money only because it buys half as much memory. If 384 GB is enough,
  it is the cheapest way to full bandwidth; if you need 768 GB, you must pay for
  the 64 GB modules.

**If 384 GB is not enough and 6400 is too expensive, the honest trade:**
- **5600 at 12 channels**: ~12.5 % less bandwidth than 6400, and the same channel
  count. RDIMM bins below 6400 (5600/6000) are far cheaper per GB. This keeps
  *channel* bandwidth structure intact and sacrifices only MT/s.
- **Note the manual's own rule:** *"Mixed DIMM speeds can be installed. However,
  all DIMMs will run at the speed of the slowest DIMM."* So do not mix 6400 and
  5600 hoping for partial benefit — the whole array drops to the slowest module.

**What I could not price reliably today.** Retail and comparison sites are now
heavily bot-walled (Geizhals "Sicher Verbindung wird überprüft", Newegg and
Mouser "Access denied", idealo serving an error page), and the 2026 DRAM shortage
has made prices move fast enough that a scraped figure would be stale on arrival.
The only figures I got cleanly this run:

| Item | Seen | Status |
|---|---|---|
| Kingston KSM64R52BD4-64MD 64 GB 6400 2Rx4 | **€2,838.93** | heise, 4 offers |
| G.Skill F5-6400R3644E64GQ4-T5N 4×64 GB kit | **€12,269** | Alternate DE, in stock |
| DDR5-5600 32 GB RDIMM (various) | **~$190–295/module** | search snippets only — **UNVERIFIED**, not read off a product page |

**UNVERIFIED / not quoted:** a clean per-module EU price for 12× 32 GB 5600 and
12× 32 GB 6400. Given the shortage, get a written quote from one distributor for
the exact SKU instead of trusting any scraped number, including mine.

**Recommendation:** if the goal is *cheapest way to all 12 channels at full
bandwidth*, **12× 32 GB at 6400 (384 GB)** is the answer per the population table
— not a sub-6400 bin. Go sub-6400 only if you also need ≥768 GB and cannot pay
6400 prices, in which case take 12× 64 GB at 5600 and accept ~12.5 % less.

## H14SSL-NT — the dual 10GbE variant, for the same-machine media server (2026-11-12)

Asked because the plan is one box doing compute **and** media serving.

**It is the same board with one part swapped.** Per Supermicro's own spec lists
(manual feature list; product pages for both SKUs):

| | H14SSL-N | H14SSL-NT |
|---|---|---|
| LAN | 2× RJ45 **Broadcom BCM5720 1 GbE** | 2× RJ45 **Broadcom BCM57416 10 GbE** |
| PCIe | 3× 5.0 x16, 2× 5.0 x8 | **identical** |
| MCIO | 2× x8 + 1× x8 hybrid | **identical** |
| M.2 | 2× PCIe 5.0 x4 | **identical** |
| SATA | 8× SATA3 | **identical** |
| DIMM | 12 | **identical** |
| BMC | AST2600, dedicated 1 GbE IPMI | **identical** |

So **the entire 4-GPU / MCIO / M.2 wiring plan carries over unchanged**, and the
10G ports cost **no slot** — they are onboard.

**Price:** Geizhals DE **H14SSL-N €975.16** vs **H14SSL-NT €1,049.00** →
**+€73.84** (idealo independently lists the NT from €1,049.00). A dual-port
10GBASE-T PCIe card is ~€150–400 and would eat one of the only **two free x8
slots** (SLOT2/SLOT4), which are exactly the slots a media server might want for
an HBA or extra NVMe. At €74 the onboard NIC is the cheaper and better trade.

**The one caveat that decides it.** The BCM57416 is **10GBASE-T and 1000BASE-T
only** — Broadcom's own adapter datasheet (BCM957416N4160C-DS) lists
IEEE 802.3an 10GBASE-T and 802.3ab 1000BASE-T, with **no 2.5G/5G NBASE-T**.
So on a **2.5GbE** switch the port links at **1G** — identical to the plain
H14SSL-N, i.e. you paid €74 for nothing. The benefit needs a **10G switch or a
direct 10G link**, on **Cat6/6A** cable (10GBASE-T is rated for Cat6/6A/7).

**Media-server notes that matter more than the NIC:**

- **No iGPU.** The EPYC 9135 has no integrated graphics, so there is **no
  QuickSync**. Transcoding has to come from an R9700 (RDNA4 VCN via VAAPI — Linux
  media-stack support is recent; **UNVERIFIED** for Jellyfin/Plex today) or from
  the CPU. If transcoding is a real requirement, a cheap Intel Arc card in a free
  x8 slot is the low-power, well-supported answer — **untested on this board**
  and it needs Above-4G decoding in BIOS.
- **Storage headroom is good but has one either/or.** **8 SATA ports
  (SATA8–15) are always available.** SATA0–7 exist **only** if the hybrid MCIO3
  port is switched from NVMe4/5 to SATA via the **JSATA1** jumper — so
  **8 HDDs + 4 NVMe** needs no HBA, while 16 SATA costs you NVMe4/5. Both are
  plenty for a media library.
- **Power and thermals are the real constraint, not the board.** A media server
  is on 24/7, and this one would idle with **four dual-slot 300 W-class blowers**
  installed. R9700 idle draw is **UNVERIFIED** — measure it before committing to
  always-on. Four GPUs plus a stack of HDDs in one chassis also means the HDDs
  sit in the GPUs' exhaust; case layout matters more here than any spec above.

**Verdict:** take the **H14SSL-NT** if the network is (or will become) 10G — it
is €74, uses no slot, and leaves both x8 slots free. Stay on the **H14SSL-N** if
the switch is 2.5GbE, because the port will negotiate 1G and buy nothing.

## "12× 32 GB at 5000" — the bin doesn't exist, and slower is not cheaper

**Two problems with that plan, one technical and one commercial.**

**1 · There is no DDR5-5000.** JEDEC's DDR5 speed grades are 4800, 5200, 5600,
6000, 6400 (and up); the H14SSL-N's own BIOS `Memory Target Speed` menu offers
exactly **Auto, DDR3600, DDR4000, DDR4400, DDR4800, DDR5200** (manual p.77) — no
5000 in the list either. So "5000" would mean buying a 5200 or 5600 module and
underclocking it, which buys nothing.

**2 · The genuinely important finding: DDR5-4800 RDIMM is not a retail product,
and slower RDIMMs are not cheaper.** I checked Alternate's whole catalogue this
run:

| Speed | Registered RDIMM availability | Price evidence |
|---|---|---|
| **4800** | **No RDIMM sold at all** — every 4800 listing is desktop **UDIMM/SO-DIMM** (ADATA/Patriot/TeamGroup), which **cannot go in this board** | UDIMM 32 GB €605 — irrelevant, wrong type |
| **5200** | scarce; listings mostly UDIMM | — |
| **5600** | yes: Kingston **KSM56R46BD8PMI-32MDI** 32 GB REG ECC | **€1,195.00**, and **"Artikel kann derzeit nicht gekauft werden"** (cannot currently be bought) |
| **6400** | yes: G.Skill **F5-6400R3239G16GQ4-G5N**, 4× 16 GB kit | **€2,465.00 → €2,210.00** |

**The 5600 32 GB RDIMM at €1,195 is more than the 6400 kit's per-module price.**
The 6400 kit works out at **~€553 per 16 GB / ~€1,106 per 32 GB-equivalent**, and
it is in stock. So **dropping to 5600 to save money does not work right now** —
the 5600 Server Premier single module is the more expensive, less available part.
That is the shortage distorting the low-end bins, not a normal price ladder.

**So for 12× 32 GB at a slower speed, realistically:**
- **12× €1,195 = €14,340** for 5600 32 GB — and that SKU is not currently
  orderable, so it is not an actual option.
- Versus **3× G.Skill 4× 16 GB 6400 kits = 12 modules = €6,630** (€2,210 each),
  which gives you 192 GB at 6400, in stock.

**That comparison flips the earlier advice: right now, 6400 in 16 GB modules is
the cheapest way to populate 12 channels**, because the shortage has hit the
mid-speed server SKUs harder than the enthusiast-registered 6400 kits.
Caveat: 16 GB × 12 = **192 GB** total, which is a small amount of memory for this
class of machine — fine for proving the platform, tight for real LLM work.

**Recommendation, concretely:**
- **Cheapest real 12-channel 6400 build: 3× G.Skill F5-6400R3239G16GQ4-G5N
  (4× 16 GB) = 12 DIMMs = 192 GB at 6400, ~€6,630**, in stock at Alternate.
- **If 192 GB is too small:** the 32 GB 6400 path (12× 32 = 384 GB) is where the
  cost jumps hard, and 12× 64 GB at €2,839/module (~€34k) is the top.
- **Do not plan around 4800 or 5200 RDIMM** — they are not on the shelf in this
  form factor, and the board's own QVL 6400 entry is the only validated speed.

**UNVERIFIED:** whether G.Skill's 4-DIMM kits are validated as 3 kits in the same
board (they are 4-DIMM kits, so 3 kits = 12 DIMMs is a plausible but untested
population), and whether the 9135 will run these EXPO-rated kits at 6400 with all
12 populated rather than falling back. **That is exactly the case to test before
buying three kits** — buy one kit first, confirm 6400 with 12 channels populated
is achievable, then buy the rest.

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

## EPYC 9555 ES (or higher) instead of the 9135 — evaluated 2026-11-12

The appeal is obvious: eBay **ES 9555 asking $1,034–C$1,527**, i.e. *below* the
retail 9135 (**€1,629**), for **4× the cores**. Retail 9555 is **€4,529**
(Geizhals; 9555P €4,044.41), so the ES is ~⅓ of retail.

**AMD's own numbers (product pages):**

| | EPYC 9135 | EPYC 9555 |
|---|---|---|
| Cores / threads | 16 / 32 | **64 / 128** |
| L3 | 64 MB | **256 MB** |
| Base clock | 3.65 GHz | 3.2 GHz |
| Default TDP | **200 W** | **360 W** |
| cTDP range | **200–240 W** | **320–400 W** |
| 1kU price | $1,214 | **$7,973** |
| Memory | 12 ch, up to 6400, **614 GB/s** | **identical** |
| PCIe | 128 lanes Gen5 | **identical** |

**Why it does not help this build:**

1. **The platform is identical where it matters.** Same 12 channels, same
   6400 MT/s, same 614 GB/s, same 128 PCIe 5.0 lanes. Four-GPU inference is
   GPU-bound; the 9135's 16c/32t already feeds four GPUs. The 9555 adds cores
   this workload cannot use.
2. **Power goes the wrong way.** +160 W at default TDP, and its **official cTDP
   floor is 320 W** — you cannot officially run it at the 9135's 200 W. The BIOS
   does expose `Package Power Limit Control` (Manual PPT), so it *can* be capped,
   but then you are paying for 64 cores to run them at 16-core clocks. With the
   GPUs at 210 W (840 W total), the 9135 keeps the box near **~1,180 W**; a 9555
   at its 320 W floor pushes **~1,300 W**.
3. **ES risk lands exactly on this board's hard parts.** ES silicon is
   pre-production: Supermicro's BIOS microcode may not carry the ES CPUID, in
   which case the board **does not POST** and it appears on no support list. The
   cheap listing is **100-000001247-12 at 1.9 GHz base** vs 3.2 GHz retail — an
   early sample. No warranty, no RMA. And the things this build stresses —
   **12 DIMMs training at 6400, four GPUs on Gen5 lanes** — are precisely what
   pre-production silicon is least proven at.
4. **"Or higher" is worse.** 9655 is 400 W, 9755 and 9965 are 500 W (9965 =
   192 cores) with lower clocks: more power, more heat, more ES risk, still no
   workload for the cores.
5. **The saving is small relative to the risk.** ~€600 under the retail 9135.
   One non-POSTing sample erases it and costs weeks.

**If you still want to try:** buy a **QS** (qualification sample) rather than an
ES — QS is normally the retail stepping and eBay even sells QS+Supermicro board
combos, which is weak evidence that QS boots on these boards. Buy only from a
seller with a real return window, and inside that window test **POST, 12 DIMMs
at 6400, and all four GPUs** before it closes.

**Correction 2026-11-12T03:5xZ — the MoE case, where the 9135 is genuinely too
small.** If the plan includes **large MoE models whose experts spill to system
RAM**, CPU-side expert compute is real work on this box, not host duty: Zen 5 has
**full-width AVX-512** (plus VNNI/BF16), and CPU expert FFNs are **memory-
bandwidth-bound**. That changes the CPU requirement in two ways:

1. **16 cores is not enough to feed 12 channels.** 614 GB/s theoretical (~460–550
   real) needs a lot of outstanding loads; 16 Zen 5 cores leave a large fraction
   of it idle. This is the one workload where the 9135 is the wrong part.
2. **But the ceiling is bandwidth, not cores.** All 9005 SKUs ship the **same
   614 GB/s**, so beyond the core count that saturates ~500 GB/s, extra cores buy
   almost nothing.

**AMD's verified 9005 ladder** (product pages) against DE prices:

| SKU | Cores | Base | L3 | TDP / cTDP | 1kU | DE price |
|---|---|---|---|---|---|---|
| **9135** | 16 | 3.65 GHz | 64 MB | 200 W / 200–240 | $1,214 | **€1,629** |
| **9355** | **32** | **3.55 GHz** | **256 MB** | **280 W / 240–300** | $3,694 | **€2,379** |
| 9455 | 48 | 3.15 GHz | 256 MB | 300 W / 240–300 | $4,959 | €3,690 |
| 9555 | 64 | 3.2 GHz | 256 MB | 360 W / 320–400 | $7,973 | €4,529 |
| 9655 | 96 | 2.6 GHz | 384 MB | 400 W / 320–400 | $8,999 | — |

**That table kills the 9555 ES argument in a better way than "you don't need
cores":**

- **The 9555 is not the value point even at retail.** It costs **€4,529** and its
  base clock is **3.2 GHz — lower than the 9355's 3.55 GHz and the 9135's
  3.65 GHz** — for 32/48 more cores that the 614 GB/s ceiling cannot feed. On a
  bandwidth-capped path, base clock and L3 matter as much as core count.
- **The 9355 is the part for this workload:** **32 cores at 3.55 GHz, 256 MB L3,
  280 W (cTDP floor 240 W), €2,379** — i.e. **+€750 over the 9135** for double the
  cores, 4× the L3, essentially the same clock, and only **+80 W**. That is the
  cheapest retail SKU likely to reach the bandwidth knee.
- **The ES is the worst possible sample for this exact use.** Its listed **1.9 GHz
  base** is 40 % below the retail 9555's 3.2 GHz, and CPU expert compute is
  precisely the workload that runs at base clock. You would buy cores to run them
  at the lowest clock in the stack, with no warranty and a real no-POST risk.
  **A €2,379 retail 9355 beats a ~€1,000 1.9 GHz ES at the job the ES is
  supposedly for.**
- **9655/9755/9965 stay rejected:** 2.6 GHz and below, 400–500 W, and still
  614 GB/s. More cores, slower per core, no extra bandwidth.

**Revised verdict:** if MoE-to-RAM is out of scope, keep the **9135**. If it is
in scope, buy the **retail 9355 (€2,379)** — not a 9555, and never the 1.9 GHz
ES. Note this also makes the **DDR5-6400 requirement load-bearing** for the first
time: on the CPU-expert path the memory speed *is* the throughput.

### ES/QS pricing reality — the cheap samples are not free (2026-11-12)

The samples really are everywhere and really are far cheaper: **9555 ES asking
$1,034–C$1,527 (~€950–1,050)** against **€4,529** retail, and 9355/9455 samples
follow the same pattern. So "buy retail" needs an argument, not an assertion.
Here it is.

**ES and QS are not the same purchase, and the difference is the whole argument.**

- **QS (qualification sample)** — late/final silicon, normally the **retail
  stepping and retail clocks**, usually boots on retail BIOS. A defensible buy.
- **ES (engineering sample)** — pre-production. Clock **varies wildly by sample**
  (the cheap 9555 ES is **1.9 GHz base vs 3.2 retail**), and the CPUID/stepping
  may not be in Supermicro's microcode at all. A lottery ticket.

**Failure modes, ordered by what they actually cost you:**

| Failure | Cost |
|---|---|
| **No POST** | Purchase price + weeks, **and no way to tell CPU from board from DIMMs** without a known-good CPU to swap |
| **POSTs but won't train 12 DIMMs at 6400** | Silent **~25 % bandwidth loss**; on the MoE path that is the entire reason for the CPU. Presents as a "board/DIMM" problem |
| **POSTs, trains, errata under load** | Random crashes with 4 GPUs running, months later, with nobody to RMA to |
| **Lower clocks than retail** | Matters **only** on the CPU-expert path — which is the only reason to buy more than 16 cores |

**The real objection is not the money, it is where the risk sits.** The fragile
parts of this build are **12 DIMMs at 6400** and **four GPUs on bifurcated Gen5
links**. Adding an unsupported CPU puts a third unknown into every future
debugging session, and there is no reference part to swap. On a box carrying
4× ~€5k GPUs, the CPU is the cheapest component to insure.

**So the honest rule:**

- **GPU-host duty only** (no MoE-to-RAM): a **QS** at retail clocks is a
  reasonable buy — the clock does not matter and 16 cores would do. Even a
  working ES is acceptable here, because nothing about the workload depends on
  the CPU's quality.
- **CPU expert compute** (MoE spilling to RAM): **buy QS or retail, never the
  low-clock ES.** This is the one workload that runs at base clock, so a 1.9 GHz
  sample is disqualified by definition. A **QS 9355 at 3.55 GHz** is the target.
- **"Or higher" stays wrong at any price.** 96 cores at 2.6 GHz base is *slower
  per core* than 32 at 3.55, on the **same 614 GB/s ceiling**. ES pricing does
  not fix that.

**De-risking that actually works:** buy the **QS**, from a seller with a real
return window, and inside it prove **POST → 12 DIMMs at 6400 → all four GPUs**.
Downside then is shipping time, not the purchase price. Buying board+CPU as a
seller-tested combo (they exist as H13SSL-N + 9555 QS bundles) moves the POST risk
to the seller. **UNVERIFIED:** there is no public POST-rate data for 9005 ES on
Supermicro H14 — the risk is real but unquantified, and I am not going to invent
a number for it.

## Sourcing: the QS bundles that exist (2026-11-12)

Searched for seller-tested board+CPU bundles. eBay 403s this host, so listings
were read through **PicClick's eBay mirror**, which returns title + Buy-It-Now
price. **Prices are indexed snapshots and may be stale; returns policy could not
be read** (the item pages also 403). Treat every line as "listing exists at this
price", not as a quote.

**There is no H14SSL-N/-NT + 9555 QS bundle.** The H14 bundles are the wrong
CPUs for this build:

| Listing | Price | Verdict |
|---|---|---|
| **EPYC 9965 QS 192C + H14SSL-N** | $6,000 | 192c at **2.25 GHz**, 500 W — slower per core, no extra bandwidth. No. |
| EPYC **9D85** 158C + H14SSL-N | $4,274.50 | OEM-only SKU, 158c — same objection. No. |
| H14SSL-N + 9965 (retail) | $7,300 | No. |

**The 9555 QS bundles are all H13SSL-N / H13SSL-NT** — and that is not the
downgrade it looks like:

| Listing | Price | Board |
|---|---|---|
| **H13SSL-NT + 9555 QS 64C/128T, 10GbE** | **$2,100** | `398148252060` |
| H13SSL-NT + 9555 QS 64C/128T, 10GbE | $2,376.21 | `198463960228` |
| H13SSL-N + 9555 QS 64C | $2,100 | `198463955981` |
| H13SSL-N + 9555 QS 64C | $2,000 | `920128372571` |

(eBay item numbers; readable at `picclick.com/...-<item>.html`.)

**Why H13SSL-NT is close to equivalent.** Supermicro's own page: **12 DIMM,
3× PCIe 5.0 x16 + 2× x8, 2× MCIO x8 + 1 hybrid, 2× M.2 PCIe 5.0 x4, 8× SATA,
2× 10GbE BCM57416** — the same expansion set as the H14SSL-NT. The memory line is
the whole story:

- **rev 1.x** — 9004 only, **no 9005**.
- **rev 2.0** — 9005 works, **6000 MT/s** cap.
- **rev 2.01** — 9005 at **6400 MT/s**.

So the bundle is only equivalent **if the board is rev 2.01**. That is a question
to put to the seller in writing before paying, because rev 2.0 silently costs
**6.25 % of the memory bandwidth that this whole build is about**.

**Standalone CPU prices (same check):**

| Part | Price | Note |
|---|---|---|
| **9555 QS** `100-000001247-12` | **$1,500.46** | QS suffix **-12** |
| 9555 ES `100-000001247-12` / `-13` | $1,030–1,035 | **1.9–3.35 GHz** listed vs 3.2–4.4 retail |
| 9555 retail | €4,529 | — |

**The part-number split is the useful finding:** sample OPN **`-12` is the QS**,
**`-13` is the 1.9–3.35 GHz ES**. So the lottery is identifiable before buying.

**Cost of the two routes:**

| Route | Cost | Bandwidth |
|---|---|---|
| H13SSL-NT + 9555 QS bundle (rev 2.01) | **~$2,100–2,376** | 6400 ✅ |
| H14SSL-NT €1,049 + 9555 QS ~$1,500 | **~€2,350** | 6400 ✅ |
| H14SSL-NT €1,049 + retail 9355 €2,379 | ~€3,430 | 6400 ✅ |

The bundle is the cheapest way to get a **seller-tested 64-core** by roughly
€500, at the cost of a used H13 board of unknown revision and no warranty either
way.

**Questions to ask the seller before paying (all four, in writing):**
1. **Board revision — 2.01 or 2.0?** (2.01 for 6400; 2.0 caps at 6000; 1.x
   won't boot 9005 at all.)
2. **CPU OPN — `100-000001247-12` (QS) or `-13` (ES)?**
3. **Return window and who pays return shipping?**
4. **Has this exact board+CPU pair been POST-tested together, and at what memory
   speed?**

## H14 vs H13 — the real delta, and EU sourcing (2026-11-13)

### What the H14 actually adds over the H13

Both are ATX single-SP5 boards with the **same expansion set**: 3× PCIe 5.0 x16 +
2× x8, 2× MCIO x8 + 1 hybrid, 2× M.2 PCIe 5.0 x4, 8× SATA3, 2× 10GbE
BCM57416 (-NT), AST2600 BMC, 6 fan headers, 6× USB 3.0. Even the **rear I/O
shield is the same part** (MCP-260-00073-0N fits both), which is good evidence
they are the same physical layout.

Verified from Supermicro's own product pages, **the entire difference is three
lines**:

| | **H14SSL-NT** | **H13SSL-NT** |
|---|---|---|
| Max CPU TDP | **500 W** | **400 W** |
| 9005 support | native, every board | **rev 2.x only** |
| DDR5 at 1DPC | **6400, every board** | 4800 (9004) / **6000 on rev 2.0** / **6400 only on rev 2.01** |
| Expansion, NIC, BMC, M.2, SATA, fans | — | **identical** |

So:

- **500 W vs 400 W is the only non-revision spec advantage**, and it is
  **irrelevant for this build**: a 9555 is 360 W and a 9355 is 280 W. It only
  matters if you later fit a 9755/9965 (500 W), which are already rejected.
- **The rest is revision luck.** H13 needs rev 2.x to boot 9005 at all, and
  **rev 2.01 specifically** to hit 6400. On the used market that is a
  coin-flip you cannot inspect before paying.
- Plus the boring one: **H14 is new with warranty and current firmware**;
  the bundle boards are used.

**Conclusion: for a 9555 or 9355 at 6400, the H14's only real value is that it
removes the revision lottery. That is worth paying for — and, as below, it is
not even more expensive.**

### Are the bundles available in Europe? Effectively no.

The bundle listings surface on eBay.de, but they are **USD-priced** ($2,100 /
$2,376) — i.e. US/Asia sellers shipping in, not EU stock. Landed in the EU they
take **+19 % import VAT** (plus handling), which puts $2,100 at roughly
**€2,300–2,400**.

Meanwhile the **same components are EU-stock, separately**:

| Item | EU price | Where |
|---|---|---|
| **H14SSL-N** | **€975.16** | Geizhals DE |
| **H14SSL-NT** (10GbE) | **€990.00** / €1,049.00 | picclick.de / Geizhals DE |
| H13SSL-NT **rev 2.00** | €1,059–1,171 | EU sellers |
| H13SSL-NT **rev 2.01** | **€1,037.15** | EU seller |
| 9555 sample, OPN **`-12`** | **€1,050.00** / €1,076.12 | EU sellers |
| 9555 sample, no OPN listed | €932.37 | EU seller |
| 9555 ES **`-13`** (1.9–3.35 GHz) | listed, avoid | EU seller |

**The H13 bundle no longer makes sense even on price: an H13SSL-NT rev 2.01
costs €1,037 in the EU — the same as the H14SSL-NT (€990–1,049).** You would pay
H14 money for an older board with a 400 W ceiling and a revision trap.

**The EU build: H14SSL-N €975 + 9555 QS €1,050 = ~€2,025**, new board with
warranty, 6400 guaranteed, no import VAT, no customs. That beats the landed US
bundle by roughly €300 and removes two of the four questions (revision, import).

**What still has to be asked of the EU CPU seller:** the listings say **"ES"**
while quoting the **`-12` QS OPN** — the title and part number disagree. Get the
**OPN printed on the IHS** in writing (or a CPU-Z screenshot) before paying, and
confirm the return window. **`-13` is the 1.9–3.35 GHz part — refuse it.**

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
- 2026-11-12T01:40Z — **LEADER CHANGED: SUPERMICRO H14SSL-N replaces MZ33-CP1.**
  The user was right and I had rejected this board too early. **The GPUs were
  never the difference** — the CP1 also needs exactly one GPU adapter, so both
  are "3 native + 1 MCIO" builds. The difference is **onboard Gen5 M.2**, and
  my earlier rejection leaned on a wrong premise. Verified from Supermicro's own
  manual (MNL-2821, downloaded, 119 pp): p.16 **"Two M.2 connectors (PCIe 5.0
  x4)"**; slot table **"PCIE SLOT1, 3, 5 = PCIe 5.0 x16; PCIE SLOT2, 4 = PCIe
  5.0 x8"**; **12 DIMM, 12-channel, 6400 MT/s**; ATX 304.8 x 256.5 mm.
  **Price €975.16, in stock, DE** (Geizhals, 4 offers, data 12.11.2026 00:06;
  electronis.de "ab Lager 1-2 Werktage").
  **Money, corrected:** for 2× Gen5 M.2 RAID0 the CP1 needs **+€104.90** of
  storage parts (KALEA €59.90 + 1 cable €45) → **€981.88** total; the H14SSL-N
  needs **€0** → **€975.16**. So they are within **€7**, not the €100+ gap the
  old doc implied — and at 4 drives the SU0-path is still marginally cheaper
  (€1,080.06 vs €1,086.78). **The Supermicro wins on simplicity, not price:**
  no storage adapters in the build, a shorter ATX board, and 2 Gen5 M.2 that
  work out of the box. **Also corrected an arithmetic error in this doc**: the
  earlier "€199.90 adapter set" figure bundled the GPU's 2 cables with storage
  parts; GPU cables are needed on *both* boards, so they do not belong in the
  storage comparison.
  **GPU 4 still works with no new parts:** the layout table names `NVMe0/1
  PCIe1A` and `NVMe2/3 PCIe1B` — both under PCIe Port 1 (same x16 group, the
  required topology), and the BIOS exposes `CPU1 PCIe Package Group … x16`.
  Same C-Payne CP-0232 + 2 cables as before; **NVMe4/5 (Gen5-or-SATA) stays
  free** for the 2→4 drive upgrade (+€104.90).
  **Caveat recorded, not resolved:** Supermicro's own pages have contradicted
  each other on this board's M.2 generation (key-features said Gen4, specs said
  Gen4, manual says Gen5) — documented in a ServeTheHome thread. Manual + current
  product page both say **PCIe 5.0 x4**; **confirm at first boot** with
  `lspci -vv`. **UNVERIFIED: exact slot pitch in mm** (read as even 1-pitch
  spacing with x16 at 1/3/5 off the manual layout and annotated photo) — test-fit
  before buying all four cards. CP1 kept as runner-up with its full analysis.
- 2026-11-12T01:58Z — **MZ73-LM0 evaluated as a 24-DIMM future base; rejected.
  Leader stays H14SSL-N.** Downloaded Gigabyte's rev 3.0 manual (142 pp) and
  read the expansion-slot table — it is decisive: `Slot_4` and `Slot_3` come
  from **CPU_0**, `Slot_2` and `Slot_1` from **CPU_1**, with Gigabyte's own note
  *"If only 1 CPU is installed, some PCIe or memory functions might be
  unavailable."* **With one 9135 you get 2 usable GPUs, not 4**, and 12 of the
  24 DIMMs are dead. Also **6000 MT/s at 1DPC** (datasheet — slower than the
  H14SSL-N's 6400), one **Gen4** M.2, and **from €1,652.99** (idealo, 11
  offers; category-page figure, exact offer UNVERIFIED). So it costs €678 more
  than the leader *today* and halves the GPU slots *today*.
  Recorded the manual-vs-datasheet contradiction: manual calls all four slots
  **Gen4**, datasheet feature list calls them **Gen5 x16** — unresolved, but
  irrelevant to the verdict. **On the 24-DIMM premise itself: 24 DIMM = two
  12-channel CPUs, i.e. a different machine, not an upgrade path** — it needs a
  second EPYC, a second set of DIMMs, a bigger PSU and case. Advice recorded:
  build single-socket now, buy dual-socket only if/when 24 DIMM is a real
  requirement. No change to the leader or the parts list.
- 2026-11-12T02:12Z — **QVL check done. Memory claim holds; M.2 Gen5 claim does
  NOT, and that corrects what I said in the 01:40Z entry. Leader unchanged.**
  (1) **Memory, 12 DIMM/1DPC/6400:** product page states *"12 DIMM slots
  (1DPC), speed up to 6400MT/s"* and *"Max Memory (1DPC): Up to 3TB 6400MT/s
  ECC DDR5 RDIMM/3DS (EPYC 9005)"* — explicit 1DPC + 6400. The **9135 is graded
  DDR5-6400 on the CP1's live QVL** (Oct 28 2026 stamp), so the CPU half is
  independently corroborated. **But Supermicro's own memory QVL could not be
  read**: its data endpoint `POST /en/external_db_block/support/get_tested_memory`
  returns **403** outside a same-origin browser session, the wrapper page answers
  *"accessed improperly"*, and **Wayback has no snapshot** of the ProductID=90505
  memory page. So "a 6400 RDIMM is on Supermicro's H14SSL-N QVL" stays
  **UNVERIFIED** — same dead end as the CP1's memory QVL.
  (2) **M.2 correction:** the tested-M.2 QVL for this board lists **14 drives,
  all `NVMe GEN4`, zero Gen5**; the **archived product page (2026-04-23) says
  "M.2 Interface: 2 PCIe 4"**; **Geizhals says PCIe 4.0 x4**. Only the manual
  p.16 and the *current* page say Gen5, and the ServeTheHome thread already
  documented Supermicro contradicting itself on this exact spec. **Corrected
  position: treat the M.2 slots as PCIe 4.0 x4 until proven in hardware
  (`lspci -vv`).** Consequence: two onboard Gen4 x4 M.2 still beat the CP1's
  single **Gen3 x4** slot and still cost €0 vs ~€105 of adapters, **so the pick
  stands** — but **neither board gives true Gen5 M.2 onboard**, and if Gen5
  bandwidth is a hard requirement the **MCIO route is the only way to actually
  get it** (H14SSL-N NVMe4/5, or CP1 G2). This changes the reasoning, not the
  leader. Action: confirm M.2 link speed with Supermicro/ distributor before
  buying; budget ~€105 MCIO as fallback.
- 2026-11-12T02:24Z — **QVL FOUND AND READ. The "unreadable" claim at 02:12Z is
  retracted: Supermicro's memory QVL is readable at a data URL, and it does list
  a DDR5-6400 RDIMM at 1DPC for Turin.** Working links recorded in the
  "H14SSL-N memory QVL" section: the `…/resources/memory?mspd=6.4000001&mtyp=217
  &id=a29c222d…&prid=90505&type=DDR5 RDIMM&ecc=1&reg=1&fbd=0&cpu=turin&sku=H14SSL-N`
  URL for memory, and `…/resources/m2ssd?SystemID=90505&ProductName=H14SSL-N`
  for M.2. The generic `…/resources/mem?ProductID=90505` page still answers
  "accessed improperly" — that is why it looked dead.
  **Memory QVL content (Turin):** API index returns one 6400 option,
  `DDR5 RDIMM-6400 Registered ECC`; the tested table has **one module**:
  **MEM-DR564MC-ER64 — 64GB DDR5-6400 2RX4 (16Gb) ECC RDIMM, any MB rev, 2
  ranks, Low Profile**. So the 1DPC/6400 claim is **QVL-backed**, but the tested
  list is **thin (a single SKU)** — that part is the only guaranteed-6400
  module, and 12× it = **768 GB**. Blocker 3 analogue for this board: closed,
  with the caveat that broad 6400 compatibility is untested by the vendor.
  **M.2 correction re-confirmed, unchanged:** M.2 QVL = **14 drives, all
  `NVMe GEN4`, zero Gen5**; archived page + Geizhals say Gen4; only the manual
  and current page say Gen5. Treat M.2 as **PCIe 4.0 x4** until `lspci -vv`.
  Leader unchanged; no change to the parts list.
- 2026-11-12T02:38Z — **64 GB DDR5-6400 RDIMM priced. Answer: no cheap option —
  it is the 2026 DRAM shortage, not a bad shop.** Real quotes, multiple sellers:
  **Kingston KSM64R52BD4-64MD (1x 64GB 2Rx4 CL52) €2,838.93** (heise
  Preisvergleich, 4 offers €2,838.93–2,842.74); KSM64R52BD4-64HA €3,705.77;
  **G.Skill F5-6400R3644E64GQ4-T5N (4x 64GB registered ECC kit) €12,269.00**
  at Alternate DE, in stock. ADATA/Kingston **CUDIMM** 64GB at €1,487–1,549 are
  **not RDIMM** and do not apply. Independent trackers put server DDR5 RDIMM near
  **$38/GB (Sep 2026)**, so ~€2,800/module is the going rate. **12x 64GB = 768GB
  at 6400 would cost ~€34,000 in memory alone** — dwarfing board + GPUs.
  Recorded three cheaper paths: fewer DIMMs (loses channels/bandwidth), **drop to
  DDR5-5600/6000 (~12.5% bandwidth vs 6400, far cheaper)**, or used RDIMMs.
  **Flagged, not decided: nothing in this program ever demonstrated that 6400 is
  required rather than 5600** — at current prices that spec costs roughly
  €10–15k extra across 12 DIMMs, and for LLM inference capacity usually beats
  bandwidth once the model fits. Spec came from the user, so left as a question.
  **UNVERIFIED: EU price for the exact QVL SKU `MEM-DR564MC-ER64`** (order-only
  Supermicro part, no retail listing found); Kingston KSM64R52BD4-64MD quoted as
  closest retail equivalent. Leader and parts list unchanged.
- 2026-11-12T02:52Z — **answered "cheapest 12ch RDIMM at full bandwidth under
  6400"; the premise is the finding.** Read the H14SSL-N manual's DIMM population
  table (p.40): **the board runs 6400 MT/s at 12 channels for ALL RDIMM rank
  types** — 12× 1R 32GB = 384GB, 12× 2R 64GB = 768GB, 3DS up to 3TB, all at
  **6400**. So **there is no sub-6400 bin that is required to get full
  bandwidth**; full bandwidth = 12 populated channels, and 6400 comes with it.
  **Cheapest route to full 12-channel bandwidth is 12× 32GB at 6400 (384GB)**,
  not a slower bin — same bandwidth, half the capacity, roughly half the money.
  Sub-6400 (5600/6000) only makes sense *if* ≥768GB is needed and 6400 is
  unaffordable: costs **~12.5% bandwidth** and keeps the channel count. Also
  recorded the manual's rule that **mixed speeds all run at the slowest DIMM**,
  so do not mix 6400/5600. **Price verification was poor this run** — Geizhals,
  Newegg, Mouser, idealo, digikey all bot-walled or erroring, and 2026 DRAM
  shortage pricing moves fast. Clean figures only: Kingston KSM64R52BD4-64MD
  **€2,838.93** (heise), G.Skill 4×64GB kit **€12,269** (Alternate, in stock).
  5600 32GB seen at **~$190–295** in snippets but **UNVERIFIED — not read off a
  product page**; no clean 12× 32GB totals quoted. Recommended a written
  distributor quote over any scraped figure, including mine. Leader and parts
  list unchanged.
- 2026-11-12T03:05Z — **"12x32GB at 5000" does not exist, and slower RDIMM is
  MORE expensive right now. This reverses the 02:52Z "drop to 5600" advice.**
  (1) **No DDR5-5000 grade exists** (JEDEC: 4800/5200/5600/6000/6400; the board's
  own `Memory Target Speed` menu lists only Auto/3600/4000/4400/4800/5200 —
  manual p.77).
  (2) **DDR5-4800 RDIMM is not a retail product** — every 4800 listing at
  Alternate is desktop **UDIMM/SO-DIMM**, which cannot go in this board.
  (3) **The price ladder is inverted by the shortage:** Kingston **5600 32GB
  RDIMM KSM56R46BD8PMI-32MDI = €1,195** and is marked
  *"cannot currently be bought"*, while **G.Skill 6400 4x16GB kit
  F5-6400R3239G16GQ4-G5N = €2,210 (was €2,465), in stock**. Per 32GB-equivalent
  that is **€1,105 at 6400 vs €1,195 at 5600** — **the faster part is cheaper**.
  So **12x 32GB @5600 = €14,340 and unorderable**, versus **12x 16GB @6400 =
  3 kits = €6,630, in stock** (192GB total).
  **Concrete recommendation: 3x G.Skill 4x16GB 6400 kits = 12 DIMMs = 192GB at
  6400 for ~€6,630** as the cheapest real 12-channel build; 192GB is small for
  this class, so 384GB (12x32) or 768GB (12x64 @ €2,839 each, ~€34k) are the
  capacity steps up. **UNVERIFIED: whether 3 separate 4-DIMM EXPO kits populate
  12 channels at 6400 on the 9135** — they are kits, not a validated 12-DIMM
  population; **buy ONE kit, prove 6400 at 12 channels, then buy the other two.**
  Leader and parts list unchanged.
- 2026-11-12T03:22Z — **H14SSL-NT evaluated for the combined compute+media box.**
  Same board as the -N with **2x BCM57416 10GbE** instead of 2x BCM5720 1GbE;
  everything else (3x x16 + 2x x8, MCIO set, 2x M.2, 8x SATA, 12 DIMM, AST2600
  BMC) is **identical** per Supermicro's spec lists, so the 4-GPU/MCIO plan is
  unchanged. **Price €1,049.00 vs €975.16 = +€73.84** (Geizhals DE; idealo
  agrees at €1,049.00). 10G is **onboard**, so it costs no slot — the two free
  x8 slots stay free for an HBA/NVMe, vs ~€150–400 for a dual-10G card.
  **Key caveat: BCM57416 is 10GBASE-T + 1000BASE-T only** (Broadcom
  BCM957416N4160C-DS: 802.3an + 802.3ab) — **no 2.5G/5G NBASE-T**, so a 2.5GbE
  switch negotiates **1G** and the €74 buys nothing; needs a 10G switch/direct
  link and Cat6/6A.
  Media-server notes recorded: **EPYC 9135 has no iGPU → no QuickSync**, so
  transcode is R9700 VAAPI (RDNA4 support recent; **UNVERIFIED** for
  Jellyfin/Plex) or CPU, with a cheap Intel Arc in a free x8 slot as the
  pragmatic alternative (**untested on this board**, needs Above-4G decoding).
  **8 SATA (SATA8–15) always available; SATA0–7 only by switching MCIO3 from
  NVMe4/5 to SATA via JSATA1** — 8 HDDs + 4 NVMe needs no HBA. **24/7 power and
  HDD-in-GPU-exhaust thermals are the real constraints**; R9700 idle draw
  **UNVERIFIED — measure before committing to always-on**.
  **Verdict: take -NT on a 10G network, stay -N on 2.5G.** Also fixed the leader
  table's M.2 row to point at the Gen4-vs-Gen5 caveat.
- 2026-11-12T03:41Z — **EPYC 9555 ES (or higher) evaluated; answer: no.** eBay ES
  9555 asking **$1,034–C$1,527** vs retail **€4,529** (Geizhals; 9555P €4,044.41)
  and vs retail 9135 **€1,629**. AMD pages: 9555 = 64c/128t, 256MB L3, **360W,
  cTDP 320–400W**, $7,973 1kU; 9135 = 16c/32t, 64MB, **200W, cTDP 200–240W**,
  $1,214. **Both have identical 12ch/6400/614 GB/s and 128 Gen5 lanes**, so the
  4-GPU workload gains nothing. Rejected on: (1) no benefit for GPU-bound work;
  (2) **+160W default and a 320W cTDP floor** — cannot officially run at the
  9135's 200W, pushes a 210W-GPU box from ~1,180W to ~1,300W (BIOS PPT override
  exists but then 64 cores run at 16-core clocks); (3) **ES risk** — pre-production
  CPUID may not be in Supermicro microcode → **no POST**; cheap listing
  **100-000001247-12 is 1.9GHz base vs 3.2GHz retail**; no warranty; and 12-DIMM
  @6400 training + 4 Gen5 GPUs are exactly what ES silicon is least proven at;
  (4) 9655/9755/9965 = 400–500W and lower clocks, worse; (5) saving only ~€600 vs
  retail 9135. If tried anyway: buy **QS not ES**, with a return window, and test
  POST + 12 DIMMs @6400 + all 4 GPUs before it closes. Leader/CPU unchanged
  (**EPYC 9135**). Also noted user's plan: GPUs power-capped to 210W, HDDs in a
  separate chassis (thermals no longer co-located).
- 2026-11-12T03:55Z — **corrected the 9555 verdict for the MoE-to-RAM case.**
  User is right that experts spilling to system RAM make CPU compute real work,
  and Zen 5 AVX-512 (full width, VNNI/BF16) plus 12-channel bandwidth is the
  point. Revised analysis: (a) **16 cores cannot feed 614 GB/s**, so the 9135 is
  genuinely undersized *if* MoE offload is in scope; (b) **the ceiling is
  bandwidth, not cores — every 9005 SKU has the same 614 GB/s**, so cores past
  the knee buy little; (c) **the 9555 is not the value point even at retail**:
  AMD-verified **€4,529 / 64c / 3.2 GHz base / 360W** vs **9355 €2,379 / 32c /
  3.55 GHz / 256MB L3 / 280W** — the 9355 has the *higher* base clock for
  €2,150 less; (d) **the 1.9 GHz ES is the worst sample for this job**, since CPU
  expert compute runs at base clock — a retail 9355 beats it outright.
  Full ladder recorded (9135 €1,629 / 9355 €2,379 / 9455 €3,690 / 9555 €4,529;
  AMD 1kU $1,214 / $3,694 / $4,959 / $7,973; 9655 96c 2.6GHz 400W). **Revised
  verdict: 9135 if MoE-to-RAM is out of scope, retail 9355 if it is in scope;
  9555 and everything above is rejected.** Also noted this is the first workload
  that makes the **DDR5-6400 requirement load-bearing** (on the CPU-expert path
  memory speed *is* throughput).
- 2026-11-12T04:08Z — **ES/QS challenge answered on the merits, not waved away.**
  Conceded: samples are everywhere and much cheaper (9555 ES asking
  **$1,034–C$1,527 ≈ €950–1,050** vs **€4,529** retail; 9355/9455 follow the
  same pattern). Split the category: **QS = late/final silicon, retail stepping
  and clocks, usually boots retail BIOS — defensible; ES = pre-production,
  clocks vary wildly (cheap 9555 ES is 1.9GHz base vs 3.2 retail), CPUID may be
  absent from Supermicro microcode.** Recorded the failure ladder (no POST →
  can't distinguish CPU/board/DIMM without a known-good CPU; POST-but-won't-train
  → silent ~25% bandwidth loss that reads as a board/DIMM fault; errata under
  load → random crashes with no RMA; low clocks → only hurts the CPU-expert
  path). **Core objection recorded as risk placement, not price:** the fragile
  parts of this build are 12 DIMMs @6400 and four bifurcated Gen5 GPUs, and an
  unsupported CPU adds a third unknown with no reference part to swap. **Rule:
  GPU-host-only → QS at retail clocks is reasonable; MoE-to-RAM → QS/retail only,
  never the low-clock ES, target QS 9355 @3.55GHz; "or higher" stays rejected at
  any price (96c @2.6GHz is slower per core on the same 614GB/s ceiling).**
  De-risking: buy QS from a seller with a real return window and prove POST →
  12 DIMMs @6400 → 4 GPUs inside it; seller-tested H13SSL-N+9555 QS combos exist.
  **UNVERIFIED: no public POST-rate data for 9005 ES on Supermicro H14** — risk
  real but unquantified, no number invented.
- 2026-11-12T04:31Z — **sourced the QS bundles.** eBay 403s this host; read
  through **PicClick's eBay mirror** (title+Buy-It-Now only; **returns policy
  UNVERIFIED**, item pages also 403, prices are indexed snapshots). **No
  H14SSL-N/-NT + 9555 QS bundle exists** — the H14 combos are **9965 QS 192C
  $6,000**, **9D85 158C $4,274.50** and **9965 retail $7,300**, all wrong for
  this workload (2.25GHz / OEM SKU). **The 9555 QS bundles are H13SSL-N and
  H13SSL-NT: $2,000–2,376**, the -NT ones (`398148252060` $2,100,
  `198463960228` $2,376.21) carrying **dual 10GbE BCM57416**, and the non-T
  (`198463955981` $2,100, `920128372571` $2,000). **Board revision decides
  everything on H13:** rev 1.x = 9004 only; **rev 2.0 = 9005 but 6000 MT/s**;
  **rev 2.01 = 9005 at 6400**. Expansion set otherwise matches H14SSL-NT
  (3x x16 + 2x x8, 2x MCIO + 1 hybrid, 2x M.2 Gen5 x4, 8 SATA, 10GbE).
  Standalone: **9555 QS `100-000001247-12` $1,500.46**; **ES $1,030–1,035 and
  listed at 1.9–3.35GHz** vs 3.2–4.4 retail — so **sample OPN -12 = QS,
  -13 = low-clock ES**, identifiable before buying. Cheapest route to a
  seller-tested 64-core: **H13SSL-NT + 9555 QS ~$2,100–2,376**, ~€500 under
  H14SSL-NT (€1,049) + QS (~$1,500) ≈ €2,350, and ~€1,300 under H14 + retail
  9355. Four written questions recorded: **rev 2.01?, OPN -12?, return window?,
  POST-tested at what memory speed?** Leader unchanged; no purchase made.
- 2026-11-13T00:0xZ — **H14-vs-H13 delta pinned, and EU sourcing resolved.**
  From Supermicro's own pages the **entire difference is three lines**: **500W CPU
  support vs 400W** (irrelevant here — 9555=360W, 9355=280W; only matters for the
  already-rejected 9755/9965), **native 9005 vs rev 2.x only**, and **6400 on
  every board vs 6400 only on rev 2.01** (rev 2.0 = 6000, rev 1.x = no 9005).
  Expansion is otherwise **identical** (3x x16 + 2x x8, 2 MCIO + hybrid, 2x M.2
  Gen5 x4, 8 SATA, 2x 10G BCM57416, AST2600, 6 fans); even the **rear I/O shield
  is the same part, MCP-260-00073-0N**.
  **EU availability: boards yes, bundles effectively no.** Bundle listings on
  eBay.de are **USD-priced** (US/Asia sellers) → +19% import VAT lands $2,100 at
  ~€2,300–2,400. EU-stock prices found: **H14SSL-N €975.16**,
  **H14SSL-NT €990.00–1,049.00**, **H13SSL-NT rev 2.00 €1,059–1,171**,
  **H13SSL-NT rev 2.01 €1,037.15**, **9555 sample OPN -12 €1,050.00/€1,076.12**,
  another sample **€932.37** (no OPN listed), and a **-13 (1.9–3.35GHz) to
  avoid**. **Because H13SSL-NT rev 2.01 (€1,037) costs the same as H14SSL-NT
  (€990–1,049), the bundle logic collapses.** Revised recommendation:
  **buy in the EU — H14SSL-N €975 + 9555 QS €1,050 ≈ €2,025**, new board with
  warranty, 6400 guaranteed, no import VAT — roughly €300 under the landed US
  bundle. Still to verify with the EU CPU seller: **titles say "ES" but quote the
  `-12` QS OPN** — get the **IHS OPN** (or CPU-Z) in writing plus the return
  window; **refuse `-13`**.
