# Starting with 1×64 GB instead of 2×64 GB — what it blocks

**Short answer:** one 64 GB RDIMM should boot and run Strata IQ3_S on this four-GPU box, because the 128 GB of VRAM holds the experts in low-RAM mode and the PLE table can stay on the SSD. It is the **minimum viable** host, not the specified build. It blocks the PLE-in-RAM mode, the full 16 GB conversation cache and two Saber Flash-Next servers, and it leaves almost no headroom for checkpoints/page cache. Verify the board POSTs with one DIMM before relying on it. **Two sticks are the practical floor** for the build as designed; the second stick is not wasted and can be added later.

The rest of this note is the evidence and the exact numbers.

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

## 2. What one stick costs in bandwidth

The board has eight channels; one DIMM uses one channel:

| DIMMs | Channels | Bandwidth at DDR5-5600 | Share of the 8-channel maximum |
|---:|---:|---:|---:|
| 1×64 GB | 1 | 44.8 GB/s | 12.5% |
| 2×64 GB | 2 | 89.6 GB/s | 25% |
| 4×64 GB | 4 | 179.2 GB/s | 50% |
| 8×64 GB | 8 | 358.4 GB/s | 100% |

For the Strata workload with all experts in VRAM, **decode is GPU-bound**; the host bandwidth mostly affects model load, PLE reads, checkpoint/park copies and any CPU expert fallback. One channel is slower, but it is not the decode bottleneck. It becomes a real bottleneck if you later run a model that does not fit in VRAM and falls back to CPU experts.

## 3. What one stick blocks

- **PLE in RAM (`--ple-io ram`)**: 28.8 GB + 50 GB experts + 10 GB OS = 88.8 GB, over 64 GB. Keep the PLE on the RAID 0 (`--ple-io direct` or the default); the 4×1 TB array is fast and the PLE reads are small.
- **The full 16 GB conversation cache**: 50 + 16 + 10 = 76 GB, over 64 GB. Reduce it (e.g. 4–8 GB) or disable parking; agent sessions lose the park/restore continuity the 128 GB build provides.
- **Checkpoints and page cache**: 64 GB leaves ~4 GB after the 50 GB experts and 10 GB OS; a checkpoint write or a large prompt cache can push it into swap. The 128 GB build leaves ~68 GB.
- **Two Saber TP=2 servers**: Saber’s own launcher notes put the 2-card Flash-Next boot at **~34–35 GiB RSS**. Two servers on two pairs need ~70 GB, over 64 GB; 128 GB fits.
- **A future 4-rank Saber**: the PLE is `O_DIRECT` from NVMe, so 64 GB is not a PLE cache, but a 4-rank engine’s pinned slabs, KV host buffers and four rank processes will want more than the 2-card 34 GB. 128 GB is the safer floor.
- **Not blocked:** the four GPUs, the 128 GB VRAM, the model itself (low-RAM mode), the 4 TB RAID 0, the 8× upgrade path, or Saber on one pair. The first stick is not a dead end.

## 4. Does the board boot with one DIMM?

The manual’s memory sections document 8-channel (PRO) and 4-channel (non-PRO) populations; it does not publish a one-DIMM table. A single RDIMM in **A1** is likely to POST, but **2 DIMMs in A1 + E1 is the documented dual-channel minimum** and the configuration this build specifies. Check the board’s memory support list/QVL before relying on a one-stick boot; if the board refuses a single DIMM, that is the only hard block in this note.

The upgrade path is mechanical:

```
1×64  A1            -> 64 GB,  1 channel
2×64  A1 + E1       -> 128 GB, 2 channels
4×64  A1,C1,E1,G1   -> 256 GB, 4 channels
8×64  all           -> 512 GB, 8 channels
```

Buy the same part (Samsung M321R8GA0PB0-CWM, 64 GB DDR5-5600 CL46 2Rx4 ECC RDIMM) for the later sticks; mixing rank/brand/timing in one channel set is the thing to avoid.

## 5. Test plan if you start with one stick

1. Boot with 1×64 GB in A1; confirm POST, ECC enabled, 64 GB visible, 1 channel.
2. Start Strata with the PLE on the SSD (no `--ple-io ram`), a small conversation cache (4–8 GB) and low-RAM mode; watch `free -g` and the engine log for OOM/arena allocation.
3. Run 1 stream and 8 streams at 262K; record decode, TTFT, prefill, VRAM, wall power. Decode should be close to the 2-stick number because the experts are in VRAM; prefill/PLE and park/restore may be slower.
4. Add the second 64 GB in E1; repeat. Compare decode (should be within noise), prefill, park/restore, model load and the conversation-cache hit rate.
5. Only after the 2-stick run is clean should the machine be called production.

## 6. Recommendation

- **If you can buy two now, buy two.** The second stick is €2,499 at the snapshot, and it converts the machine from “IQ3_S with little else open, PLE on SSD, no full conversation cache” to the specified dual-channel 128 GB build with PLE-in-RAM and the 16 GB cache. It also covers two Saber servers and a future 4-rank engine.
- **If budget forces one, start with one.** It will run the GPU-resident IQ3_S workload, and the 128 GB of VRAM is doing the heavy lifting. Keep the PLE on the SSD, shrink the conversation cache, and add the second stick before production. The first stick is not wasted; it is the first channel of the 8× path.
- **Do not buy two 32 GB sticks instead.** They give the same 64 GB, consume two slots and two channels (better bandwidth than one 64 GB, but half the capacity of 2×64), and they break the clean 8×64 = 512 GB path. The 64 GB module is also the cheapest per-GB RDIMM in this snapshot.
