# Acceptance protocol

<p class="muted">The projections are not measurements. This is the short version of the acceptance run that replaces them. The full protocol lives in the repository at <code>docs/VALIDATION.md</code>.</p>

## 1. Memory

- MemTest86+: **8 complete passes**, zero errors.
- `edac-util -v`, `ras-mc-ctl --error-count`, `dmesg | grep -i edac`: all DIMMs visible, zero corrected/uncorrected.
- Population: A/B/C/D 2×64 in A1+E1; E 4×64 in A1/C1/E1/G1; F 8×64 all slots.
- 6400 builds: confirm 6400 MT/s and the expected timings; watch for ECC/WHEA in the soak.

**Gate:** 8 passes clean, zero ECC errors, chosen capacity visible, stable 6400 training.

## 2. Storage

- `lsblk`, `nvme list`, `smartctl -a`.
- `mdadm --create /dev/md0 --level=0 --raid-devices=<3/4/6> --chunk=128K ...`
- `fio` sequential 1M and random 4K; record exact numbers.
- Targets: A ≥35 GB/s / ≥4M IOPS; B ≥40 / ≥6M; C ≥25 / ≥3M; H ≥50 / ≥6M.
- SMART <70 °C; target <75 °C under load.

## 3. PCIe

- `lspci -d 1002: -vv | grep -E 'LnkCap:|LnkSta:'`: four **32 GT/s x16** links.
- Slot 6 must be empty; 4-way uses 1/3/5/7.
- `dmesg | grep -i -E 'aer|pcie bus error'`: zero AER after the full run.

## 4. Power and thermals

- Wall meter: full load ≤2,000 W; 1,630 W continuous expected.
- 12V-2x6 and board aux connectors <60 °C after 20 minutes.
- GPU edge/hotspot, CPU Tctl/Tccd, M.2/MCIO, VRM: no throttle.
- **Connector count first:** four GPUs consume all four PCIe 8-pin; board aux needs the second PSU / higher-connector PSU.

## 5. Engine

- `strata-device --list-devices`: four R9700s.
- 1 stream at 262K; then 8 streams at 262K.
- Record decode, TTFT, prefill, VRAM, wall power, per-card power.
- Gate: 8×262K stable; ≥250 tok/s aggregate decode (target 300–500); ≥2,500 tok/s prefill at 32K; no stream <25 tok/s.

## 6. Soak

- 24 h at 8 streams + 64K cold prompts.
- No drops, no VRAM growth, no ECC/AER, no thermal throttle.

**Only after this sheet is complete should the machine be called serving.**
