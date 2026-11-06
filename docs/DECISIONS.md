# Settled decisions — RAM, platform and engine flags

Consolidated record of the outcomes from two discussion threads, with the claims
that were later superseded called out explicitly so they are not reintroduced.
Every source-level statement below was re-checked against `/root/git/strata` on
2026-11-06.

Threads consolidated:

- `79b2e60d-7793-403d-b603-89c6ca52c92e` — "I've heard 2Rx4 for LLM inference is best"
- `9445c513-c29a-43ce-a771-ae3a7826d2df` — 4×R9700 on a non-Pro TRX50 board with a single 32 GB stick

## 1. Memory organisation and platform

### 1.1 The 8×64 GB 2Rx4 endgame is correct

For the stated WRX90 / Threadripper PRO build with **8 × 64 GB DDR5 2Rx4 ECC
RDIMM**, octa-channel:

| Property | Value |
|---|---|
| Capacity | 512 GB |
| Channels | 8 (one DIMM per channel) |
| Ranks | 16 total (2 per DIMM) — the heaviest load the board trains |
| Bandwidth, TR PRO 9000 @ DDR5-6400 | 8 × 51.2 = **409.6 GB/s** |
| Bandwidth, TR PRO 7000 @ DDR5-5200 | 8 × 41.6 = **333 GB/s** |

`x4` organisation buys **density**, not bandwidth. A 64 GB x8 module would put
the same bytes on the same eight channels at the same MT/s; nothing in the
memory controller makes x8 faster, and x4 additionally carries more banks per
rank for scattered reads. The only thing that would improve is chip count
(18 x8 dies vs 36 x4 dies per DIMM -> lower power/heat), which is not a reason
to spec a part that does not exist.

### 1.2 What 1Rx8 and 2Rx8 would mean at 64 GB — neither is a product

- **1Rx8 64 GB** needs 64 Gbit x8 dies (one rank, nine dies). JEDEC defines the
  organisation; the dies are not shipping in volume. Not a purchasable module.
- **2Rx8 64 GB** needs 32 Gbit x8 dies, and that is not what the catalog sells.
  The 64 GB RDIMMs in volume (Samsung `M321R8GA0PB0-CWM`, Micron
  `MTC40F2046…`) are **2Rx4 built from 16 Gbit x4 dies**.
- Conclusion: **keep 2Rx4.** There is no x8 upgrade path at this capacity.

### 1.3 Rank does not change latency

- CAS/access latency is set by the DRAM bin, not the rank count.
- **Single rank** removes rank-to-rank turnaround and halves the chip-selects
  per channel; that is what allows one rank per channel (1RPC) at eight DIMMs to
  train at 6400 on TR PRO 9000.
- **Dual rank** adds rank interleaving — more independent bank work to overlap.
- At two DIMMs the difference is low single-digit percent and workload-dependent.
- The memory controller is in the CPU IOD on sTR5, not the WRX90 chipset; rank
  count does not burden the chipset.

### 1.4 32 GB single-rank ECC RDIMMs exist — as 1Rx4

Correction to an earlier claim in the thread ("32 GB RDIMMs are 2Rx8, single
rank does not exist"). Both organisations ship:

| Part | Capacity / speed | Organisation |
|---|---|---|
| Samsung `M321R4GA0BB0-CQK` | 32 GB DDR5-4800 | 1Rx4 (single rank) |
| SK hynix `HMCG84AGBRA188N` | 32 GB DDR5-5600 | 1Rx4 (single rank) |
| A-Tech 32 GB 5600 | 32 GB DDR5-5600 | 1Rx4 (single rank) |
| Samsung `M321R4GA3EB0-CWM` / `A3EB2-CCP` | 32 GB 5600 / 6400 | 2Rx8 (dual rank) |
| SK hynix `HMCG88AGBRA`, Micron `MTC20F2085S1RC56BR` | 32 GB 5600 | 2Rx8 (dual rank) |

Caveats: do **not** mix x4 and x8 modules (EC8 10x4 vs EC4 9x4 organisations are
not interchangeable); the 1Rx4 32 GB parts are 4800/5600, the 6400 32 GB parts
are 2Rx8; 1Rx4 is more server-stock than desktop-stock, so check the board QVL
and buy returnable.

### 1.5 WRX90 is RDIMM ECC only

Octa-channel Threadripper PRO means WRX90, and WRX90 is registered ECC only
(ASUS Pro WS WRX90E-SAGE SE: "8 x DIMM slots, DDR5, ECC Registered Memory";
ASRock WRX90 WS EVO: "supports only DDR5 RDIMM ECC memory"). There is no
non-ECC octa-channel configuration on sTR5, and it is not a BIOS setting. The
fork is WRX90 + PRO (8 channels, RDIMM) or TRX50 + non-PRO (4 channels, UDIMM).

### 1.6 What this means for Strata

The host RAM question is a capacity question first, bandwidth second, rank
third-or-lower:

- Qwen3.8 Q4: all 24,576 experts in VRAM; host holds the 28.8 GB PLE table and
  page cache.
- DeepSeek 2.00 / 2.25 bpw at 8K: CPU lane 3.7 GB / 20.7 GB; 12.7 / 29.7 GB
  wanted.
- DeepSeek UD-Q8 (508 GB set): 171.5 GB CPU lane, 180.5 GB wanted — the only
  one of these loads that needs more than 256 GB.

At 512 GB every load above has multiple times the headroom. Capacity and
channel count dominate; rank organisation is a low-single-digit term on a lane
that is already idle for two of the three targets.

## 2. Engine behaviour and flags

### 2.1 Strata on four GPUs is a pipeline layer split, not tensor parallel

`docs/MULTI_GPU.md` is explicit: contiguous layer ranges per card, one hand-off
per verify window through pinned RAM, no NCCL, no all-reduce, no peer-to-peer
requirement. Four cards on a non-Pro TRX50 board (48 PCIe 5.0 lanes, x16/x16/x8/x8)
is therefore fine; the PCIe topology is not the constraint it would be for TP=4.

### 2.2 One 32 GB stick: what it actually costs

With every expert resident on the cards, host RAM traffic per token is the
stage hand-off (a few hundred KB per verify window), the PLE rows (a few 90 B
rows per token, from SSD with `--ple-io direct`), and nothing else — single-digit
MB/s at ~60 tok/s against ~30 GB/s real from one DDR5-5600 channel.

Where it bites:

1. **Cold start.** The full model is 44,900,816,736 + 38,842,920,384 =
   **83,743,737,120 B**. 32 GB cannot page-cache it, so each cold start re-reads
   the whole file. Measured on the two-of-four R9700 box: 33 s and 59 s with the
   files cached, **114 s the first time** (`docs/MULTI_GPU.md:206`).
2. **No page-cache safety net.** If the four per-card expert caches come up a few
   percent short, the missing experts are read per token, and on a small-RAM host
   the engine reads them unbuffered by design. On a 128 GB host the same
   shortfall hides in page cache. A 3 % shortfall on 32 GB is a drive-bound
   crawl.
3. **Flags that turn "slow" into "won't start":** `--ple-io ram` locks the whole
   28.8 GB PLE table in RAM (correct on 128 GB, wrong on 32 GB); a split skips
   the automatic expert-mmap path, so pass `--mmap-experts --resident-cpu-experts`
   (or the `--resident-experts` bundle, which adds pinned + 4 GiB headroom);
   `--kv-resident` must stay at its default (see 2.3).

Verdict recorded: not RAM-blocked at decode **provided** every expert is
resident and the mmap/resident flags are passed; the cost is cold-start minutes
and the loss of the overflow cushion. Buy the second stick before the fourth
card — 2×32 in the correct slots is dual-channel, 64 GB.

### 2.3 `--kv-resident 0` means "all KV in VRAM"

Verified in this checkout:

```
src/program/generate.cpp:669   int64_t kv_resident = 0;   ///< KV streaming: resident cells per QSA layer (0: all in VRAM)
src/core/layer.cpp:743         if (g_kv_resident <= 0 || ring_cells < 0) return p;   // ring_cells < 0: always fully resident
src/core/layer.cpp:917         if (p.mode != 0) { ... pinned host copy of the layer's KV ... }
```

- `0` is the sentinel that disables streaming; it does **not** mean "zero cells
  resident". This is the value to use on a box with VRAM to spare.
- `N > 0` with `N < max_context` turns streaming on: the layer keeps at least
  `qsa_kv_resident_min()` cells in VRAM and pins the rest of that layer's KV in
  host RAM, giving the freed VRAM to expert slots.
- `N == max_context` stays in the fully-resident path (no pinned host copy), so
  the configs' `--kv-resident 262144` at `--max-context 262144` is equivalent
  today — but it is coupled to the context value and silently starts streaming
  if the context is raised. **Prefer `0` in new configs.**
- The minimum window is **4096 cells** on non-Metal builds and **20480** on
  Metal, overridable with `STRATA_KV_RESIDENT_MIN`. The "min 20480" figure in
  the earlier thread is stale for Linux/ROCm.

### 2.4 `--low-ram` is a launcher switch, not an engine flag

`strata generate` has no `--low-ram` option (`src/program/generate.cpp` has no
match). The setup/launcher script takes `--low-ram on|off|resident|mmap`; the
engine-side equivalents are `--mmap-experts`, `--resident-cpu-experts` and the
`--resident-experts` bundle. `docs/MODELS.md:141` states that `strata launch`
has no `--low-ram` flag.

### 2.5 Fit on 4 × 32 GB with the full Flash-Next model

Experts ≈ 46 GiB, PLE table 28.8 GB on SSD with `--ple-io direct`, dense
weights 1.54 GB per card, head + MTP ≈ 4 GB — roughly 80 GB of the 128 GB of
VRAM before per-card buffers. The pruned IQ1_M release (23 GB experts, 29.6 GB
first shard) is documented as running standalone on 32 GB of host RAM and is
oversized for four cards.

## 3. Superseded statements (do not carry forward)

| Earlier claim | Corrected position |
|---|---|
| "A single-rank 32 GB ECC RDIMM is not a catalog part today." | It exists as **1Rx4** (Samsung `M321R4GA0BB0-CQK`, SK hynix `HMCG84AGBRA188N`). 1Rx8 does not. |
| "4×64 GB is half the channels of 8×32 GB." | Wrong framing: channel count follows DIMM count, not capacity. 8×64 and 8×32 are both eight channels. |
| "2Rx4 64 GB is a trap for a 256 GB ladder." | Withdrawn. 8×64 GB 2Rx4 is the correct endgame for the stated build. Mixing organisations is the only real trap. |
| "`--kv-resident` pins the whole KV in RAM." | Only for `0 < N < max_context`. `N = 0`, and `N >= max_context`, allocate no pinned host copy. |
| "The streaming minimum is 20480 cells." | 4096 cells on CUDA/ROCm, 20480 on Metal; `STRATA_KV_RESIDENT_MIN` overrides. |

## 4. Sources checked

- `/root/git/strata/src/program/generate.cpp` lines 663, 669, 3716-3719,
  4255, 4272-4276, 6666
- `/root/git/strata/src/core/layer.cpp` lines 738-756, 769-786, 895-945
- `/root/git/strata/docs/MULTI_GPU.md` (layer split; 206 for the 33/59/114 s
  load times)
- `/root/git/strata/docs/AMD_HIP.md` 312 (`STRATA_PLE_AUTO_RAM`), 417-423 (PLE
  direct vs RAM on gfx1201)
- `/root/git/strata/docs/MODELS.md` 141-142 (`--low-ram` is a setup flag)
- `README.md` §3 (2×64 GB now -> 8×64 GB later), `bom/option-c.csv`,
  `configs/strata-4x-r9700-8x262k.json`
