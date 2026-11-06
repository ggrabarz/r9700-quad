# Saber on 4× R9700 — can the 2× config just be expanded?

**Short answer:** the **hardware build does not change**, but the software is not a config-file expansion. Saber’s Flash-Next path is built as **EP=2 + dense TP=2**, and its dense attention has **2 KV heads**, which cannot be split four ways. A 4-GPU Saber for one model needs a new parallel decomposition (EP=4 with TP=2 pairs, or a pipeline/layer split), not `tp = 4` in the TOML. The 27B dense model has 4 KV heads and is graph-legal at TP=4, but the executor and all-reduce are still two-rank.

This note is a code-level review of Saber at commit `cebec82`, plus the PR path that is actually realistic.

---

## 1. What the code says

| Fact | Evidence |
|---|---|
| Flash-Next pack is **EP=2 over two ranks, dense TP=2** | `crates/saber-model/src/qwen4_exp/pack_plan.rs:1-3`, constants `EP: u32 = 2`, `TP: u32 = 2` at lines 54-57. |
| Flash-Next dense TP has only two forms | `crates/saber-model/src/qwen4_exp/layer_graph.rs:73-80`: `enum Tp { One, Two }`. |
| Flash-Next has **2 KV heads** (GQA 12) | `crates/saber-model/src/qwen4_exp/config.rs:82-85`. |
| The Qwen3.8-27B has **4 KV heads** | `crates/saber-model/src/graph.rs:141-162`. |
| The all-reduce is **2-rank only** | `crates/saber-plan/src/reference.rs:444-480`: `ar_oneshot_2rank_*`, `Constraint::eq("world_size", 2)`. |
| The executor refuses a world size other than 1/2 | `crates/saber-engine/src/device.rs:4628-4634`: “the reference’s reduce is `2rank` in its name and in its body, so this engine is TP=1 or TP=2.” |
| The CLI refuses `--tp` other than 1/2 | `crates/saber-cli/src/main.rs:4071-4073`: “this engine is built for TP=1 and TP=2.” |
| The setup wizard disables TP=3/4 | `tools/saber-setup:126-130`. |
| The launch scripts hardcode TP=2 | `tools/serve_flashnext.sh:191` (`--tp 2`), `tools/serve_27b.sh:88` (`--engine-tp 2`). |

So `tp = 4` in `examples/qwen38-27b-nvfp4-tp2.toml` would be rejected by the CLI before the graph is built, and even if the check were relaxed, the plan would find no `world_size == 4` all-reduce and the executor would refuse the world.

## 2. Why Flash-Next cannot be dense-TP=4

The model has **24 query heads and 2 KV heads**. The graph builder’s TP divisor (`crates/saber-model/src/graph.rs:3590-3601`) requires every sharded dimension to divide by `tp`:

- TP=2: 24/2 = 12 q heads, 2/2 = 1 KV head — legal.
- TP=4: 24/4 = 6 q heads, **2/4 = 0.5 KV heads** — not a head count. The builder refuses with the “does not divide by tp” error.

The current Flash-Next design avoids this by splitting **experts** (EP=2, 256 of 512 per rank) while keeping the dense part at TP=2. A 4-GPU version therefore has to choose a different decomposition:

- **EP=4 + dense TP=2**: 512/4 = 128 experts per rank; the dense layers are TP=2 within each pair; the 2 KV heads are split 1 per rank inside a pair and replicated across pairs. This is the closest to the current design, but the KV is duplicated across the two pairs, which cuts the per-card stream capacity roughly in half.
- **EP=4 + dense TP=1**: each rank holds the full dense weights and 128 experts; attention/KV is replicated on all four ranks. More VRAM per rank for dense/KV, fewer experts per rank; not obviously better.
- **Pipeline/layer split**: each rank owns 16 of the 64 layers, with its own experts and KV. This is the design that preserves 8×262K streams, and it is what Strata already does. It is a new executor, not a TP knob.

The 27B is different: 24 q heads and **4 KV heads** divide by 4 (6 q, 1 KV), and the GDN heads (16/48) divide by 4. A 27B TP=4 is graph-legal, but it still needs a 4-rank all-reduce, a 4-rank pack, a 4-rank protocol and a launcher; the current executor is a two-rank pair.

## 3. The three 4-GPU paths

| Path | What it serves | Effort | Meets the 8×262K objective? |
|---|---|---|---|
| **A. Two independent TP=2 servers** (pairs 0,1 and 2,3) | Two models, one per pair | Low: launcher/exclusivity change; no engine math | No — two models, not one |
| **B. EP=4 + dense TP=2** (Flash-Next) | One model on four cards | High: 4-rank expert all-to-all/combine, pair-local TP, 4-rank pack, protocol, tests | Maybe, but KV is replicated per pair; 8×262K is unlikely |
| **C. Pipeline / layer split** | One model on four cards | Very high: new executor, layer handoff, per-rank KV, scheduler | Yes — and Strata already implements it |

Path A is the only one that works without engine surgery, and it does not meet “one model, four cards”. Path B is a research project with a stream-count risk. Path C is the right design, but it duplicates what Strata already does.

## 4. Does the hardware build change?

**No.** The BOM is already the right envelope for either a 2×2 Saber deployment or a future 4-rank Saber:

| Item | Why it still fits |
|---|---|
| 4× R9700 32 GB | Saber TP=2 uses two; a future 4-rank mode would use four. The cards are the same. |
| TRX50 AI TOP, 4× x16, 4× M.2 | A 2×2 deployment needs two x16 links; a 4-rank mode needs four. Already there. |
| 2×64 GB DDR5 ECC | Saber’s PLE is `O_DIRECT` from NVMe, not a RAM cache; 128 GB is the OS/checkpoint floor. No change. |
| 4×1 TB RAID 0 | Saber’s Flash-Next needs ~70 GB packs + 170 GB checkpoint + a **95.4 GiB** PLE table read in place. The 4 TB array is the right home; Strata’s 79 GB fits beside it. |
| 2,200 W PSU | Saber caps at 210 W/card (4×210 = 840 W; ~1,270 W total), so a 1,600 W unit would suffice **for Saber only**. The 2,200 W unit is already specified for Strata’s 4×300 W and costs the same class of money; keep it. |
| Meshify 2 XL / XE360-TR5 | Four 210 W cards are easier than four 300 W cards; the same case and cooler work. No change. |

The only hypothetical saving is a smaller PSU if the machine will **never** run Strata: the Seasonic PX-2200 is €489.90, the be quiet! Dark Power Pro 13 1600 W is €479.90 RRP — about €10. Not worth a BOM change. The 2,200 W unit also covers the 4×300 W Strata mode, which is the build’s primary engine.

## 5. What PRs are realistic

**PR 1 — documentation (low risk, can be submitted now).** Add `docs/4X-R9700.md` to Saber with:

- the 4× R9700 hardware envelope (TRX50 AI TOP, 9955WX, 2×64 GB, 4×1 TB RAID 0, 2,200 W);
- what works today: one TP=2 server on a pair; the second pair idle;
- the measured Saber 27B result (229 tok/s on 2× R9700, 262K, 210 W/card);
- the Flash-Next 95.4 GiB PLE / `O_DIRECT` storage requirement;
- the explicit “TP=4 is not supported” note with the 2-KV-head reason;
- a benchmark plan for 2×2 and for a future 4-rank mode.

**PR 2 — RFC / issue (design, no code).** Add `docs/RFC-4-RANK.md` proposing Path B (EP=4 + TP=2) and Path C (pipeline), with the code touchpoints:

- `saber-plan/src/reference.rs` — a 4-rank all-reduce family (ring or hierarchical 2×2) or a pipeline handoff;
- `saber-engine/src/tp2.rs` / `device.rs` — N-rank frames and world checks;
- `saber-model/src/qwen4_exp/pack_plan.rs` — `EP=4`, per-rank expert files, KV replication or layer split;
- `tools/saber-setup` / launchers — a 4-rank device selection;
- gates: token equality, 262K stream stability, per-card VRAM, 4-rank all-reduce correctness.

**PR 3 — optional 2×2 launcher (experimental).** Add `tools/serve_2x2.sh` that starts two TP=2 servers on `HIP_DEVICES=0,1` and `2,3` with distinct `CNAME`, `PORT`, `SABER_SHARED`, and relax the global “another saber server” check to the selected pair. This uses all four cards for **two models**, not one. It needs a 4-card test before it is more than a draft.

A docs patch for PR 1 and an RFC for PR 2 are prepared in `patches/saber-4x-r9700-docs.patch` (against Saber `cebec82`). There is no `gh` client on this host, so the patch is local; it can be applied to a fork and opened as a PR.

## 6. Recommendation

1. **Build the Strata 4-GPU box as specified.** The hardware does not change, and Strata is the only engine here that serves one model across four cards with 8×262K streams today.
2. **Contribute the 4× hardware doc and the 4-rank RFC to Saber.** That is useful, low-risk, and gives the maintainer the exact 2-KV-head blocker instead of a vague “please support TP=4”.
3. **If you want to use Saber now, run it on one pair** (TP=2) and keep Strata on all four for production. Or run two TP=2 servers on the two pairs for two models, if the launcher exclusivity is relaxed; that is a multi-model deployment, not the stated one-model objective.
4. **Revisit when Saber lands a 4-rank mode.** The box is ready for it; only the software is missing.

## 7. What “expand the 2x config” would actually look like

A hypothetical `tp = 4` manifest for the 27B would pass the graph’s head divisibility (24/4, 4/4, 16/4, 48/4), but it would fail at the CLI’s TP check, then at the 2-rank all-reduce, then at the pack header. For Flash-Next it fails earlier: the 2 KV heads cannot be divided by 4. So the config file is the smallest part of the change; the executor, collectives and pack are the work.

If the goal is simply “use all four cards with Saber”, the honest options are two TP=2 servers (two models) or wait for a 4-rank mode. The 4× R9700 build is not wasted either way: it is the correct hardware for Strata today and for a future 4-rank Saber.
