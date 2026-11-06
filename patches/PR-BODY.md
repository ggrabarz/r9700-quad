# docs: add 4× R9700 host guide and 4-rank RFC

This adds two documents for four-card Radeon AI PRO R9700 hosts. It is documentation only; no engine code changes.

## What it adds

- **`docs/4X-R9700.md`** — the hardware envelope (4× R9700 32 GB, TRX50 AI TOP, Threadripper PRO 9955WX, 2×64 GB DDR5 ECC, 4×1 TB NVMe RAID 0, 2.2 kW PSU, 360 mm AIO, Meshify 2 XL), what works today (one TP=2 server on a pair; the other pair idle), what does not (TP=3/4; two servers on four cards with the current launcher), the Flash-Next 95.4 GiB PLE/O_DIRECT storage requirement, and a benchmark plan.
- **`docs/RFC-4-RANK.md`** — a design proposal for a four-rank mode. It compares EP=4 + dense TP=2 (two pairs) with a pipeline/layer split, lists the code touchpoints (`saber-plan/src/reference.rs`, `saber-engine/src/tp2.rs`/`device.rs`, `qwen4_exp/pack_plan.rs`, launchers/setup) and the acceptance gates.

## Why the RFC is needed

Flash-Next has **24 query heads and 2 KV heads**. The current path is **EP=2 + dense TP=2**; a dense TP=4 split would need 0.5 KV heads per rank, which is not a head count. The all-reduce and the command protocol are two-rank. So `tp = 4` is not a config change: it needs a 4-rank all-reduce, a 4-rank pack, and either EP=4 with pair-local TP or a pipeline split. The RFC proposes starting with the dense 27B (4 KV heads, TP=4 is head-legal) before the Flash-Next MoE.

## What this PR does not do

- It does not claim TP=4 support.
- It does not claim two servers on four cards work with the current launcher.
- The 229 tok/s figure in the guide is the 27B dense model, not Flash-Next.

## Testing

Docs only. The hardware guide was checked against the board/CPU/PSU/chassis datasheets and the Strata/Saber docs; the code references are against `cebec82`.
