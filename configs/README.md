# Strata launch notes for the 4× R9700 build

Two presets are included:

| File | Context | Batch slots | KV total at k8v4 | Use |
|---|---|---:|---:|---|
| [`strata-4x-r9700-8x262k.json`](strata-4x-r9700-8x262k.json) | 262,144 | 8 | ≈21.1 GB | Default; the safe full-context target. |
| [`strata-4x-r9700-16x131k.json`](strata-4x-r9700-16x131k.json) | 131,072 | 16 | ≈21.1 GB | Throughput preset; same VRAM, shorter streams. |

## Before the first start

1. Edit every `/srv/models/...` path to the real location on the RAID 0.
2. Set a real `api_key` (long random string) and keep port 8095 loopback-only if a reverse proxy terminates TLS.
3. Confirm the engine binary path (`/opt/strata/bin/strata` is a placeholder). The HIP build's binary is usually `build-hip/strata`.
4. Run `strata-device --list-devices` (or the package's equivalent) and confirm four `gfx1201` devices.
5. Start with `--batch 8` at 262K; do not start at 16. Measure, then raise.

## Why these flags

| Flag | Reason |
|---|---|
| `--gpu 0,1,2,3` / `gpu_roles` | Layer split across all four; main is the last card (head + MTP draft). All four are identical, so the highest index is main. |
| `--max-context 262144` | The model's full window. Use 131072 in the throughput preset. |
| `--kv k8v4` | 23% less KV than int8; 10.55 KB/token. More streams in the same VRAM. |
| `--kv-resident 0` | Keep the whole context's KV in VRAM. `0` is the sentinel for “fully resident”, not “zero cells”; it is preferred over `262144`, which is equivalent today but couples to the context value. |
| `--batch 8` | Eight full-context slots. The per-card budget in the README leaves ~8.5 GB free on the main card after 8×262K. |
| `--mmap-experts` + `--resident-cpu-experts` | AMD/HIP path: map the experts and keep the complement of the GPU cache in pageable RAM. Requires enough RAM; this build has 128 GB. |
| `--expert-cache auto` | Let the engine size the cache from free VRAM. |
| `--mtp` + `--spec 4` + `--suffix-draft 12` | MTP speculative decoding; the measured best-config family. |
| `--vision` | GPU picture reader (≈1.47 GB on the main card). Use `--vision cpu` or `--vision off` if you need the VRAM for another stream. |
| `--vram-reserve-mib 1024` | Keep 1 GB per card for the driver/desktop; the machine is headless but the reserve avoids fragmentation surprises. |
| `--conversation-cache-mib 32768` / `--slots 16` | Host-RAM checkpoint cache; 32 GB of the 128 GB is a reasonable ceiling for agent sessions. |

## Tuning after the baseline

- **More streams:** test `--batch 12` at 262K, then `--batch 16` only if the 12-stream soak is clean and the main card keeps ≥3 GB free. The arithmetic allows 16; the engine's per-slot buffers and fragmentation are the real limit.
- **Throughput preset:** `16×131K` has the same KV total as `8×262K` and usually serves more concurrent agent sessions.
- **Concurrent cold reads:** `STRATA_PIPED_CONCURRENT=1` (environment) lets streams keep decoding while a long prompt is read; the published measurement on 2× RTX 5090 shows a large improvement in stream continuity. Validate on this box before enabling it permanently.
- **Pipeline windows:** `--pipeline-windows 2` improved prefill in the published 2× RTX 3090 measurement; it is a tuning candidate, not a default.
- **Expert cache adaptivity:** `--adapt-async 1` is already in the preset; `--adapt-every` / `--adapt-swaps` are workload-specific. Do not tune them until the baseline is stable.
- **Preload/vision:** if you do not need images, `--vision off` frees 1.47 GB on the main card and removes the image reader from the critical path.
- **KV format:** `k8v4` is the quality/capacity compromise. `int8` is slightly more precise and 30% larger; `q4_0` is smaller but measurably less precise on long documents. Do not use `q4_0` for 262K agent work without a quality check.

## Service wrapper

For a boot-time service, wrap the engine in a systemd unit with `Restart=on-failure`, a dedicated user, `LimitMEMLOCK=infinity` if the engine pins memory, and the config path as an argument. Keep the model and pack paths on the RAID 0, the expert profile on the SATA or RAID 0, and the logs on the SATA so a full RAID 0 does not take the logs with it.

The exact service unit syntax depends on your Strata build; the host's reference unit is `/root/git/engines/strata-provider-launch.sh` in this environment. Do not copy its CUDA-specific environment variables to the AMD box.
