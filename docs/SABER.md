# Saber engine — evaluation for the 4× R9700 build

**Source:** [GGZ14/saber-engine](https://github.com/GGZ14/saber-engine) (Apache-2.0, 21 stars, 5 forks, 3 commits as of 2026-11-06) and the launch post by [@bkuyper](https://x.com/bkuyper/status/2118433092230606937) on 2026-11-05. The author also maintains the MXFP4 vLLM build for the R9700.

## What it is

A Rust inference engine written specifically for **AMD Radeon AI PRO R9700 (gfx1201 / RDNA4)**. HIP kernels ship as precompiled code objects with manifests; the host owns launch decisions; the server speaks the OpenAI API. It runs in a podman/docker container on a ROCm 7.x base, so the host needs the `amdgpu` kernel driver (`/dev/kfd`, `/dev/dri`) but no ROCm toolchain.

Two models are implemented:

| Model | Format | Download | Notes |
|---|---|---|---|
| Qwen3.8-27B (dense) | NVFP4 pack + DFlash2 drafter | ~26 GB | 229 tok/s single-stream on 2× R9700, TTFT ~47 ms, 5,000+ tok/s prefill at 210 W/card, 262K context. |
| Qwen3.8 Flash-Next (MoE) | MXFP4 pack + AMD Quark checkpoint | ~70 GB packs + 170 GB checkpoint | Same binary; 262K context, prefix tree, lazy vision, `FN_KV=fp8` default, `FN_EXPERTS=tp2` or `ep`. |

It does **not** load GGUF or IQ3_S/IQ3_XXS. Saber boots from its own `SBRPACK1` packs (one aligned file per GPU, weights pre-arranged for its kernels). The pack builders are not part of the release, and only the two Qwen3.8 architectures are implemented.

## The decisive limitation: TP=1 or TP=2 only

The README is explicit: *“The engine refuses any other TP (3, 4, ...) by name: it is built for TP=1 and TP=2.”* The wizard and launchers cover **TP=2 on two R9700s**; TP=1 works on one card but the single-card packs are not hosted.

On a four-GPU machine, one Saber server therefore uses **two cards**. The other two are idle for that model. The README also says only one server runs at a time (both launchers share the cards), so you cannot run two TP=2 servers simultaneously to use all four. That is the opposite of the objective here: one Flash-Next model across four cards with as many full-context streams as fit.

## The 95.4 GiB PLE table

Saber’s Flash-Next pack points into AMD’s 170 GB checkpoint for the embeddings, norms, router and the per-layer-embedding (PLE) table. The README sizes that table at **320,001,536 rows × 160 bf16 = 95.4 GiB**, split across 128 shards. Each token reads **16 rows (5,120 bytes)** from the drive with `O_DIRECT`; the table is not copied to RAM and page cache does not hold it. That is why Saber insists on a fast NVMe for the checkpoint.

This is a different footprint from the Strata IQ3_S build in this book:

| | Strata IQ3_S | Saber Flash-Next |
|---|---:|---:|
| PLE table | 28.8 GB (quantized, per Strata docs) | 95.4 GiB (bf16, per Saber README) |
| PLE I/O | `--ple-io ram` can cache it in 128 GB | `O_DIRECT`, 16 rows/token from NVMe |
| Pack/checkpoint | 79 GB | ~70 GB packs + 170 GB checkpoint |

The hardware conclusion does not change: the **4×1 TB RAID 0** is the right place for both. If anything, Saber makes the RAID 0 more important, because its PLE table cannot be RAM-resident in 128 GB and every token touches the drive. The 128 GB RAM remains right for Strata’s 28.8 GB table and the OS/page cache; it is not a Saber PLE cache.

## Fit against the objective

| Requirement | Strata (HIP layer split) | Saber |
|---|---|---|
| One model across **4** R9700s | Yes (2/3/4-card layer split, measured) | **No — TP=1/2 only** |
| IQ3_S / IQ3_XXS GGUF | Yes | **No — MXFP4 packs only** |
| Qwen3.8 Flash-Next | Yes (IQ3_S / IQ3_XXS / other) | Yes (AMD Quark MXFP4) |
| 262,144-token context | Yes | Yes |
| 8 concurrent full-context streams | `--batch 8` (this build’s target) | `MAX_SEQS=8` default, but only on 2 cards |
| Multi-GPU scaling to 4 | Yes | **No** |
| Maturity on this host | High (measured configs, docs) | Low (new project, 3 commits) |
| Performance evidence | 94.7 tok/s 1×, 125 tok/s 2×, ~150 tok/s 4× projection | 229 tok/s 27B on 2×; Flash-Next number not published |

## What it would change in the BOM

**For the stated 4-GPU/IQ3_S objective: nothing.** The board, CPU, RAM, PSU, chassis and RAID 0 are all still correct. Saber is a software alternative that cannot use the fourth GPU for a single model.

**If Saber became the primary engine:** the right machine would be a **2-GPU** box, not this one. Two R9700s, the same TRX50 AI TOP (or a cheaper board), 128 GB RAM, and the 4 TB RAID 0 would be enough; the second pair of GPUs would be wasted. That is a different build and contradicts the “4× R9700” premise.

**If you want to test Saber without changing the build:** run it on two of the four cards (TP=2) and keep Strata on all four for production. The 4 TB array has room for both packs. The test is cheap; the risk is that Saber is young and its Flash-Next numbers are unpublished.

## Recommendation

1. **Keep Strata as the production engine** for the 4-GPU, IQ3_S, 8×262K-stream objective. It is the only one of the two that can use all four cards for one model, and it is the engine with measured configs on this class of hardware.
2. **Watch Saber.** Its 27B result (229 tok/s on two cards at 210 W/card) is excellent, and a future TP=4 path plus GGUF/IQ3_S support would make it a serious challenger. Today it is a 2-GPU engine with two model architectures and a very young codebase.
3. **Do not change the storage plan.** Saber’s 95.4 GiB PLE table is another argument for the 4×1 TB RAID 0; the 128 GB RAM is for Strata’s quantized table, not Saber’s bf16 one.
4. **If you test it,** use the two-card launcher (`tools/serve_flashnext.sh`) with `MAX_CTX=262144`, `MAX_SEQS=8`, `FN_KV=fp8`, and measure VRAM, wall power and per-stream decode. Do not expect it to use cards 3 and 4.

## Caveats

- The 229 tok/s headline is the **27B dense** model, not Flash-Next. The tweet’s screenshot is a terminal capture; the README does not publish a Flash-Next decode number. Do not transfer the 27B number to the MoE model.
- Saber’s Flash-Next path depends on AMD’s Quark MXFP4 checkpoint and its 95.4 GiB PLE table; it is a different quantization and a different quality point from Swift 1.5 IQ3_S. It is not a drop-in quality comparison.
- The project is three commits old and has one open issue at the snapshot. Treat it as a promising experiment, not a production dependency.
