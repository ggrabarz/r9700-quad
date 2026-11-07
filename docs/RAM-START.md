# Starting with 1×64 GB instead of 2×64 GB — what it blocks

**Short answer:** one 64 GB RDIMM should boot and run Strata IQ3_S on this four-GPU box, because the 128 GB of VRAM holds the experts in low-RAM mode and the PLE table can stay on the SSD. It is the **minimum viable** host, not the specified build. It blocks the PLE-in-RAM mode, the full 16 GB conversation cache and two Saber Flash-Next servers, and it leaves almost no headroom for checkpoints/page cache. Verify the board POSTs with one DIMM before relying on it. **Two sticks are the practical floor** for the build as designed; the second stick is not wasted and can be added later.

**Fast path:** if you want DDR5-6400, the literal **2×64 start is two Micron MTC40F2046S1RC64BH1 modules** (€3,279.97 each, 2Rx4, CL52, 1.1 V): **€6,559.94** for 2 channels / 102.4 GB/s, and **€26,239.76** for 8×64 / 512 GB / 409.6 GB/s. The G.Skill T5 Neo **4×64 GB (€12,135.01, 4 channels, 204.8 GB/s)** and **8×64 GB (€23,094 notify-only; Proshop €27,666.06, 8 channels, 409.6 GB/s)** kits are cheaper per GB but are not 2-DIMM kits. The 5600 modules in this note cannot reach 6400. See the main book’s §3.2–3.4 for the full comparison.

The rest of this note is the evidence and the exact numbers for the **5600 value path**.

## 1. What Strata itself says

From `strata/docs/MODELS.md` (Qwen3.8-Flash-Next):

> “Shard 1 is loaded at start: its experts go into RAM, the rest onto the graphics card. The second shard (a 29 GB lookup table) stays on the SSD. The model fits when RAM is at least the experts plus about 10 GB for the OS and other programs.”

> “With 64 GB of RAM every size fits (IQ3_S with little else open). With 48 GB, Q2_0 and IQ2_XS fit. **A bigger graphics card makes it faster and does not lower the RAM needed, except in low-RAM mode.**”

And the low-RAM mode:

> “When RAM cannot hold the experts beside the system, setup maps them from the model files and keeps in RAM only what the card does not hold. A 32 GB PC with a 24 GB GPU runs Q2_0, IQ2_XS and the Coder this way…”

For IQ3_S the docs put the experts at **≈50 GB**. So:

| Host RAM | Experts + 10 GB rule | PLE 28.8 GB in RAM? | 16 GB conversation cache? | Verdict |
|---:|---:|---|---|---|
| 64 GB | 60 GB → fits with “little else open” | No (50 + 28.8 + 10 = 88.8 GB) | No (50 + 16 + 10 = 76 GB) | Minimum; PLE on SSD, cache reduced/off |
| 128 GB | 60 GB → 68 GB spare | Yes (88.8 GB, ~39 GB left) | Yes (104.8 GB, ~23 GB left) | The specified build |
| 256 GB | 60 GB → 196 GB spare | Yes | Yes, larger | Option C; 8× path |

The 128 GB of VRAM is what makes 64 GB viable: the four cards can hold the whole expert set, so the host does not need to keep the 50 GB expert arena hot in the same way a 32 GB card does. Use the low-RAM path and keep the PLE on the SSD. The host still needs the mapped model, the OS and whatever page cache the engine uses.

### If “one stick” means a 32 GB module

The settled record in [`DECISIONS.md`](DECISIONS.md) covers the 32 GB case:

| Start | Capacity / channels | What it blocks |
|---|---|---|
| 1×32 GB | 32 GB, 1 channel | Strata IQ3_S still runs with every expert resident, but the measured first start is **114 s** on the two-of-four R9700 box, there is no page-cache cushion, `--ple-io ram` and the 16 GB cache do not fit, and Saber’s ~34–35 GiB 2-card boot will not fit in 32 GB. A test configuration, not production. |
| 2×32 GB | 64 GB, 2 channels | The practical minimum: Strata IQ3_S fits “with little else open”, one Saber 2-card server fits, but the PLE must stay on the SSD, the full 16 GB cache does not fit, and two Saber servers do not. It also consumes two slots and is not the 8×64 GB endgame. |

The 8×64 GB 2Rx4 endgame wants 64 GB modules; a 32 GB start is a detour that has to be replaced later. If the choice is one 64 GB stick versus two 32 GB sticks at the same 64 GB, the two 32 GB sticks have dual-channel bandwidth (89.6 vs 44.8 GB/s) but use two slots and still block the PLE/cache features; the one 64 GB stick is the first step of the clean 8×64 path.

## 2. What one stick costs in bandwidth

The board has eight channels; one DIMM uses one channel:

| DIMMs | Channels | DDR5-5600 | DDR5-6400 | Share of the 8-channel 5600 maximum |
|---:|---:|---:|---:|---:|
| 1×64 GB | 1 | 44.8 GB/s | 51.2 GB/s | 12.5% |
| 2×64 GB | 2 | 89.6 GB/s | 102.4 GB/s | 25% |
| 4×64 GB | 4 | 179.2 GB/s | 204.8 GB/s | 50% |
| 8×64 GB | 8 | 358.4 GB/s | 409.6 GB/s | 100% |

At 6400 the 8×64 configuration is **409.6 GB/s**, +14.3% over 5600. The 5600 modules cannot be overclocked to 6400; the 6400 numbers require the G.Skill 4×64 or 8×64 kit.

For the Strata workload with all experts in VRAM, **decode is GPU-bound**; the host bandwidth mostly affects model load, PLE reads, checkpoint/park copies and any CPU expert fallback. One channel is slower, but it is not the decode bottleneck. It becomes a real bottleneck if you later run a model that does not fit in VRAM and falls back to CPU experts.

## 3. What one stick blocks

- **PLE in RAM (`--ple-io ram`)**: 28.8 GB + 50 GB experts + 10 GB OS = 88.8 GB, over 64 GB. Keep the PLE on the RAID 0 (`--ple-io direct` or the default); the 4×1 TB array is fast and the PLE reads are small.
- **The full 16 GB conversation cache**: 50 + 16 + 10 = 76 GB, over 64 GB. Reduce it (e.g. 4–8 GB) or disable parking; agent sessions lose the park/restore continuity the 128 GB build provides.
- **Checkpoints and page cache**: 64 GB leaves ~4 GB after the 50 GB experts and 10 GB OS; a checkpoint write or a large prompt cache can push it into swap. The 128 GB build leaves ~68 GB.
- **Two Saber TP=2 servers**: Saber’s own launcher notes put the 2-card Flash-Next boot at **~34–35 GiB RSS**. Two servers on two pairs need ~70 GB, over 64 GB; 128 GB fits.
- **A future 4-rank Saber**: the PLE is `O_DIRECT` from NVMe, so 64 GB is not a PLE cache, but a 4-rank engine’s pinned slabs, KV host buffers and four rank processes will want more than the 2-card 34 GB. 128 GB is the safer floor.
- **Not blocked:** the four GPUs, the 128 GB VRAM, the model itself (low-RAM mode), the 4 TB RAID 0, the 8× upgrade path, or Saber on one pair. The first stick is not a dead end.

## 4. Does the board boot with one DIMM?

The manual’s memory sections document 8-channel (PRO) and 4-channel (non-PRO) populations; it does not publish a one-DIMM table. A single DIMM has been run on a TRX50 board in the related thread (32 GB), so the AI TOP should POST with one in **A1**; **2 DIMMs in A1 + E1 is the documented dual-channel minimum** and the configuration this build specifies. Check the board’s memory support list/QVL before relying on a one-stick boot; if the board refuses a single DIMM, that is the only hard block in this note.

The upgrade path is mechanical:

```
1×64  A1            -> 64 GB,  1 channel
2×64  A1 + E1       -> 128 GB, 2 channels
4×64  A1,C1,E1,G1   -> 256 GB, 4 channels
8×64  all           -> 512 GB, 8 channels
```

Buy the same part (Samsung M321R8GA0PB0-CWM, 64 GB DDR5-5600 CL46 2Rx4 ECC RDIMM) for the later sticks; mixing rank/brand/timing in one channel set is the thing to avoid.

For 6400 the path is different: **2×64 Micron singles (2 channels, 128 GB)** then **8×64 Micron singles (8 channels, 512 GB)**, or **4×64 G.Skill (4 channels, 256 GB)** then **8×64 G.Skill octa (8 channels, 512 GB)**. Two 4×64 kits cost €24,270.02 versus €23,094.00 for the octa kit, and the 4×64 kit is CL36 while the octa kit is CL38; the octa kit is the validated 8-DIMM 6400 bin.

## 5. Budget effect

One 64 GB stick saves **€2,499 of parts and €74.97 of contingency**, so Option A with one stick is **€7,844.94** instead of €10,418.91. The second stick restores the target. The saving is temporary: the 8×64 GB endgame needs seven more modules anyway, and buying the second now locks the pair at today’s price. A 2×32 GB start buys the same 64 GB with dual-channel bandwidth but uses two slots and is not the 8×64 path; compare its price against the 64 GB module before choosing it. The 6400 fast path is a different purchase: **2×64 Micron €6,559.94** (8× later €26,239.76), **4×64 G.Skill €12,135.01**, or **8×64 G.Skill €23,094**; none uses the 5600 modules.

## 6. Test plan if you start with one stick

1. Boot with 1×64 GB in A1; confirm POST, ECC enabled, 64 GB visible, 1 channel.
2. Start Strata with the PLE on the SSD (no `--ple-io ram`), a small conversation cache (4–8 GB) and low-RAM mode; watch `free -g` and the engine log for OOM/arena allocation.
3. Run 1 stream and 8 streams at 262K; record decode, TTFT, prefill, VRAM, wall power. Decode should be close to the 2-stick number because the experts are in VRAM; prefill/PLE and park/restore may be slower.
4. Add the second 64 GB in E1; repeat. Compare decode (should be within noise), prefill, park/restore, model load and the conversation-cache hit rate.
5. Only after the 2-stick run is clean should the machine be called production.

## 7. Recommendation

- **If you want DDR5-6400 and a 2× start, buy 2× Micron MTC40F2046S1RC64BH1.** €6,559.94 for 2 channels / 102.4 GB/s, 8× later €26,239.76 for 8 channels / 409.6 GB/s. It is the only JEDEC 2Rx4 path that starts at 2 DIMMs and stays 6400. The G.Skill 4×64 (€12,135.01) and 8×64 (€23,094) kits are cheaper per GB but do not offer a 2-DIMM start; the 5600 modules cannot reach 6400.
- **If you can buy two now, buy two.** The second stick is €2,499 at the snapshot, and it converts the machine from “IQ3_S with little else open, PLE on SSD, no full conversation cache” to the specified dual-channel 128 GB build with PLE-in-RAM and the 16 GB cache. It also covers two Saber servers and a future 4-rank engine.
- **If budget forces one, start with one.** It will run the GPU-resident IQ3_S workload, and the 128 GB of VRAM is doing the heavy lifting. Keep the PLE on the SSD, shrink the conversation cache, and add the second stick before production. The first stick is not wasted; it is the first channel of the 8× path.
- **Do not buy two 32 GB sticks instead.** They give the same 64 GB, consume two slots and two channels (better bandwidth than one 64 GB, but half the capacity of 2×64), and they break the clean 8×64 = 512 GB path. The 64 GB module is also the cheapest per-GB RDIMM in this snapshot.
