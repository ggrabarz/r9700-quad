# Acceptance and benchmark protocol — 4× R9700 / TRX50 AI TOP

This is the test plan that turns the projections in the README into measured facts. Run it on the assembled machine before putting it into service. Record every number with the date, ambient temperature, BIOS version and engine build hash.

The host rules for this lab apply: one engine owns the GPUs at a time, A/B arms are interleaved (≥5 rounds for a comparison), and a delta only counts past the noise floor (~±35% for decode on this class of box). For a new platform, absolute targets and repeated single-arm runs are more useful than a hurried A/B.

---

## 0. Record sheet

| Field | Value |
|---|---|
| Date / ambient °C | |
| BIOS version | |
| CPU / microcode | |
| RAM part / population | |
| GPU VBIOS ×4 | |
| Engine build / HIP runtime | |
| Kernel / Mesa / amdgpu | |
| PSU / wall meter | |

---

## 1. Memory and ECC

1. Boot MemTest86+ from USB; run **8 complete passes**. Any error stops the build.
2. In Linux:
   ```bash
   sudo apt install edac-utils
   edac-util -v
   sudo ras-mc-ctl --error-count
   dmesg | grep -i -E 'edac|ecc|machine check'
   ```
   Expected: all DIMMs visible, correct size/rank, **zero** corrected/uncorrected errors.
3. Confirm the population is A1 + E1 and the BIOS reports 2 channels (not 4/8). Record the negotiated speed (5600 vs 5200/4800).

**Gate:** 8 passes clean, zero ECC errors, 128 GB visible.

---

## 2. Storage

Identify the four NVMe devices and the SATA device:

```bash
lsblk -o NAME,SIZE,MODEL,SERIAL,TRAN
sudo nvme list
sudo smartctl -a /dev/nvme0 | head -40
```

Create the RAID 0 (device names are examples; use the real ones):

```bash
sudo mdadm --create /dev/md0 --level=0 --raid-devices=4 --chunk=128K \
  /dev/nvme0n1 /dev/nvme1n1 /dev/nvme2n1 /dev/nvme3n1
sudo mkfs.xfs -f /dev/md0
sudo mkdir -p /srv/models
sudo mount /dev/md0 /srv/models
```

Sequential and random reads:

```bash
sudo fio --name=seqread --rw=read --bs=1M --iodepth=32 --numjobs=4 \
  --size=16G --filename=/dev/md0 --direct=1 --runtime=60 --time_based
sudo fio --name=randread --rw=randread --bs=4k --iodepth=256 --numjobs=4 \
  --size=8G --filename=/dev/md0 --direct=1 --runtime=60 --time_based
```

Targets: **≥25 GB/s** sequential read, **≥3M IOPS** 4K random read. Record the exact numbers.

Thermals under load:

```bash
for d in /dev/nvme0 /dev/nvme1 /dev/nvme2 /dev/nvme3; do
  sudo smartctl -A "$d" | grep -i temperature
done
```

**Gate:** array clean, targets met, no drive above 75 °C after 30 minutes of load.

---

## 3. PCIe link integrity

```bash
lspci -d 1002: -vv | grep -E 'LnkCap:|LnkSta:'
```

Expected for each of the four GPUs: `Speed 32GT/s (ok)`, `Width x16 (ok)`. Any `x8`, `x4`, or `downgraded` is a seating/BIOS problem.

```bash
dmesg | grep -i -E 'aer|pcie bus error|corrected error'
```

**Gate:** four x16 Gen5 links, zero AER errors after the full test run.

---

## 4. Power and connectors

Use a wall meter (e.g., Brennenstuhl PM 231 E) at the PSU inlet.

| State | Wall power | Notes |
|---|---:|---|
| Off / standby | | |
| Idle (model loaded, no requests) | | |
| 4 GPUs at 100% (synthetic load) | | |
| CPU + 4 GPUs combined | | |
| 8×262K streams | | |

Expected full load: **≤2,000 W** at the wall, ~7.5–8.5 A at 230 V. If the meter shows >2,100 W, stop and check the GPU power caps / CPU PPT.

Connector check: after 20 minutes at full load, measure the 12V-2x6 connectors and the PSU cable ends with an IR thermometer. Target **<60 °C** at the connector body; a hot connector is a seating/contact problem, not a “normal” condition.

---

## 5. Thermals

```bash
sudo apt install lm-sensors
sensors
watch -n 2 'sensors | grep -E "Tctl|Tccd|edge|junction|Composite"'
```

For each GPU, read the edge and junction temperature from the amdgpu hwmon (or `rocm-smi` if the Strata package provides it):

```bash
for h in /sys/class/drm/card*/device/hwmon/hwmon*; do
  echo "$h"; paste <(cat "$h"/temp*_label 2>/dev/null) <(cat "$h"/temp*_input 2>/dev/null)
done
```

| Sensor | Limit | Action |
|---|---:|---|
| GPU edge | <90 °C | Investigate above 85 °C |
| GPU junction/hotspot | <100 °C | Investigate above 95 °C |
| CPU Tctl/Tdie | <85 °C | Investigate above 80 °C |
| NVMe | <70 °C | Add airflow above 75 °C |
| VRM | <100 °C | Check case airflow |

Run 30 minutes of 4-GPU load plus a 262K prompt; record the steady state, not the first minute.

---

## 6. Strata baseline

1. Confirm the engine sees four devices:
   ```bash
   /opt/strata/bin/strata-device --list-devices
   ```
2. Start the 8×262K preset from `configs/strata-4x-r9700-8x262k.json`.
3. Wait for the engine-ready line; record **start time**, VRAM per card and host RAM.
4. Single-stream 262K:
   - one cold 262K-token prompt (synthetic repeated text is fine), 128 output tokens;
   - record TTFT, prefill tok/s, decode tok/s, wall power.
5. Eight concurrent 262K streams:
   - eight clients, the same prompt, staggered by 2 s;
   - run for 10 minutes;
   - record per-stream decode, aggregate decode, TTFT, VRAM per card, wall power, any dropped request.
6. Repeat the 16×131K preset and compare aggregate throughput.

Use the Strata repo’s `tools/hip/bench_prefill.py` for prompt throughput where possible; it uses the same synthetic prompts and enforces zero reused tokens. For decode, use a fixed prompt and 256 generated tokens; do not compare runs with different generated text.

**Baseline targets (to be replaced by measurement):**

| Metric | Target | Notes |
|---|---:|---|
| Single-stream decode, 262K | ≥100 tok/s | Projection ~150; the 1× R9700 anchor is 94.7 at 27K. |
| 8-stream aggregate decode, 262K | ≥300 tok/s | The number that matters for serving. |
| Prefill at 32K | ≥2,500 tok/s | 1× R9700 anchor 2,411 at 27K. |
| 8×262K streams | 10 min clean | No drops, no VRAM growth. |
| VRAM per card at 8 streams | ≤28 GB | Leave ≥4 GB free on the main card. |
| Wall power at 8 streams | ≤2,000 W | |

If the single-stream decode lands below 80 tok/s, stop and check: PCIe width, layer split, expert cache residency (`--resident-cpu-experts` / `--mmap-experts`), MTP acceptance, and whether the experts are actually in VRAM. Do not “fix” it by raising the power limit.

---

## 7. 24-hour soak

Run for 24 hours:

- 8 concurrent 262K streams;
- every 15 minutes, one cold 64K prompt on a ninth client;
- one client disconnect/reconnect per hour;
- log wall power, per-GPU temperature, VRAM, and ECC/AER counters every minute.

Pass criteria:

- zero dropped/error requests;
- no VRAM growth trend (compare hour 1 and hour 24);
- no ECC errors, no AER errors, no GPU reset;
- no thermal throttle events;
- wall power stable within ±5%.

---

## 8. Acceptance sign-off

| Item | Pass | Evidence |
|---|---|---|
| MemTest86+ 8 passes, ECC clean | ☐ | |
| RAID 0 ≥25 GB/s seq, ≥3M IOPS 4K | ☐ | |
| 4× PCIe 5.0 x16, no AER | ☐ | |
| Full load ≤2,000 W, connectors <60 °C | ☐ | |
| GPU/CPU/M.2/VRM thermals in limits | ☐ | |
| 1×262K and 8×262K Strata runs recorded | ☐ | |
| 24 h soak clean | ☐ | |
| Model archive + configs on the 4 TB SATA, checksums verified | ☐ | |

Only after this sheet is complete should the machine be called “serving”.
