#!/usr/bin/env python3
"""Cost, power, lane and VRAM/KV model for the 4x R9700 TRX50 AI TOP platform.

Reads bom/prices.json and prints Markdown tables. No third-party packages.
Run from the repository root: python3 tools/calc.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICES = ROOT / "bom" / "prices.json"


def eur(value: float) -> str:
    return f"€{value:,.2f}"


def load() -> dict:
    with PRICES.open(encoding="utf-8") as handle:
        return json.load(handle)


def option_total(data: dict, option: dict) -> tuple[float, float, dict[str, float]]:
    items = data["items"]
    groups = {
        "compute": ("mainboard", "cpu"),
        "memory": ("ram_64gb",),
        "storage": (
            "nvme_gen5_1tb",
            "nvme_gen4_1tb",
            "sata_4tb",
            "sata_8tb",
            "mcio_cable",
            "slimsas_cable",
        ),
        "power_cooling": ("psu", "cooler_aio"),
        "chassis": ("case_meshify", "case_9000d", "case_enthoo", "fan_140"),
    }
    subtotal = 0.0
    by_group: dict[str, float] = {}
    for key, qty in option["items"].items():
        line = items[key]["price"] * qty
        subtotal += line
    for group, keys in groups.items():
        by_group[group] = sum(
            items[key]["price"] * option["items"].get(key, 0)
            for key in keys
            if key in items
        )
    contingency = subtotal * data["assumptions"]["contingency_pct"] / 100.0
    return subtotal, subtotal + contingency, by_group


def main() -> None:
    data = load()
    a = data["assumptions"]
    gpu = data["items"]["gpu_r9700"]
    gpu_total = gpu["price"] * a["gpu_count"]

    print("# 4x R9700 — ASRock WRX90 WS EVO computed model")
    print()
    print(f"Price snapshot: {data['as_of']} ({data['region']}, {data['currency']} {data['tax']})")
    print()

    print("## Build totals (GPUs owned, excluded)")
    print()
    print("| Option | Name | Platform subtotal | +3% contingency | With 4 GPUs at replacement | CPU | RAM | Storage | Power/cooling | Case |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for code, option in data["options"].items():
        subtotal, total, groups = option_total(data, option)
        print(
            f"| {code} | {option['name']} | {eur(subtotal)} | {eur(total)} | "
            f"{eur(total + gpu_total)} | {eur(groups['compute'])} | {eur(groups['memory'])} | "
            f"{eur(groups['storage'])} | {eur(groups['power_cooling'])} | {eur(groups['chassis'])} |"
        )
    print()
    print(f"GPU replacement value (excluded): {eur(gpu_total)} = 4 x {eur(gpu['price'])}")
    print()

    print("## Power")
    print()
    gpu_w = a["gpu_count"] * a["gpu_w"]
    total_w = gpu_w + a["cpu_w"] + a["platform_w"]
    headroom = a["psu_w"] - total_w
    print(f"- GPUs: {a['gpu_count']} x {a['gpu_w']} W = {gpu_w} W")
    print(f"- CPU: {a['cpu_w']} W")
    print(f"- Board, RAM, 4 NVMe, 1-2 SATA, fans: {a['platform_w']} W")
    print(f"- Continuous total: {total_w} W")
    print(f"- PSU: {a['psu_w']} W -> headroom {headroom} W ({headroom / a['psu_w'] * 100:.1f}%)")
    ac_w = total_w / 0.94
    ac_half = total_w * 0.5 / 0.945
    print(f"- Input at 94% efficiency: {ac_w:.0f} W; at 230 V that is {ac_w / 230:.2f} A")
    print(f"- Annual energy at 100% load, €{a['energy_eur_per_kwh']:.2f}/kWh (wall): "
          f"{eur(ac_w / 1000 * 8760 * a['energy_eur_per_kwh'])}")
    print(f"- Annual energy at 50% average load (wall): "
          f"{eur(ac_half / 1000 * 8760 * a['energy_eur_per_kwh'])}")
    print(f"- Heat rejected at full load: {total_w * 3.412:.0f} BTU/h")
    print()

    print("## Lanes and ports")
    print()
    print("- 4 x PCIe 5.0 x16 (GPUs) = 64 lanes")
    print("- ASRock WRX90 WS EVO: 6 NVMe ports (2 M.2 + 2 MCIO + 2 SlimSAS), 3 Gen5 + 3 Gen4")
    print("- Option A (3 Gen5): 64 + 12 = 76 lanes -> 52 spare")
    print("- Option B (6 Gen4): 64 + 24 = 88 lanes -> 40 spare")
    print("- Option C (4 Gen4): 64 + 16 = 80 lanes -> 48 spare")
    print("- 9955WX: 128 PCIe 5.0 lanes; 7 x16 slots (6 x16 + 1 x8)")
    print()

    print("## Memory topology")
    print()
    for dimms, channels in ((2, 2), (4, 4), (8, 8)):
        bw = channels * 8 * 5600 / 1000
        print(f"- {dimms} x 64 GB -> {channels} channels, {bw:.1f} GB/s at DDR5-5600, {dimms*64} GB total")
    print("- 2 DIMMs now: A1 + E1 (channels A and E). 4 DIMMs: A1, C1, E1, G1. 8 DIMMs: all.")
    print("- 8 x 64 GB = 512 GB, the board maximum with 64 GB RDIMMs (the board's 2 TB ceiling needs 256 GB modules).")
    print()

    print("## Model fit (Qwen3.8-Flash-Next Swift 1.5 IQ3_S)")
    print()
    vram = a["vram_gb"]
    experts = a["model_experts_gb"]
    dense = a["model_dense_gb"]
    ple = a["model_ple_gb"]
    model = a["model_iq3s_gb"]
    kv_kb = a["kv_k8v4_kb_per_token"]
    ctx = a["context_tokens"]
    kv_stream_gb = kv_kb * ctx / 1024 / 1024
    print(f"- Download / weights: {model} GB (shard 1 experts {experts} GB, dense {dense} GB on disk / "
          f"{a['model_dense_vram_gb']} GiB in VRAM per card; PLE table {ple} GB)")
    print(f"- Total VRAM: {vram} GB = {a['gpu_count']} x 32 GB")
    print(f"- KV at {ctx:,} tokens, k8v4: {kv_kb} KB/token -> {kv_stream_gb:.2f} GB per stream")
    int8_stream = a["kv_int8_kb_per_token"] * ctx / 1024 / 1024
    print(f"- KV at {ctx:,} tokens, int8: {a['kv_int8_kb_per_token']} KB/token -> {int8_stream:.2f} GB per stream")
    print()
    print("Per-card budget (pipeline split, 4 cards):")
    per_card_experts = experts / a["gpu_count"]
    per_card_dense = a["model_dense_vram_gb"]
    per_card_buffers = 2.0
    per_card_total = per_card_experts + per_card_dense + per_card_buffers
    main_extra = 0.8 + 1.47  # head + draft layer, GPU vision reader
    print(f"- experts share {per_card_experts:.2f} GB + dense copy {per_card_dense:.2f} GB + buffers {per_card_buffers:.1f} GB "
          f"= {per_card_total:.2f} GB")
    print(f"- main card adds head/draft 0.8 GB + GPU vision 1.47 GB -> {per_card_total + main_extra:.2f} GB")
    print(f"- free per helper card: {32 - per_card_total:.2f} GB; main: {32 - per_card_total - main_extra:.2f} GB")
    for streams in (4, 8, 12, 16):
        per_card_kv = kv_stream_gb * streams / a["gpu_count"]
        free = 32 - per_card_total - main_extra - per_card_kv
        verdict = "safe" if streams <= 8 else ("test" if streams <= 12 else "too tight")
        print(f"- {streams:2d} x 262K streams: {streams * kv_stream_gb:5.1f} GB KV total, "
              f"{per_card_kv:4.1f} GB per card; main free after KV: {free:5.1f} GB ({verdict})")
    print()
    print("Recommended starting points: 8 x 262K (safe), 12 x 262K (test with >=3 GB main free),")
    print("16-24 x 131K/65K (throughput; the 131K preset has the same KV total as 8 x 262K).")
    print()

    print("## Cost metrics")
    print()
    for code, option in data["options"].items():
        _, total, _ = option_total(data, option)
        streams = 8
        print(f"- Option {code} ({option['name']}): {eur(total)} platform, "
              f"{eur(total / vram)} per VRAM GB, {eur(total / streams)} per 262K stream, "
              f"{eur(total + gpu_total)} with GPUs at replacement")
    print()

    print("## Performance anchors (measured, not projections)")
    print()
    print("- 1x R9700, IQ3_S, 27K prompt: 94.7 tok/s decode, 2,411 tok/s prefill (KVA off).")
    print("- 2x R9700, code, pipeline window: 125 tok/s decode; 3 cards +19%, 4 cards +22% (same table).")
    print("- 4x RX 7900 XT, IQ3_S, 262K: 67.6 tok/s decode at 4K, 65.6 at 32K (older, 24 GB cards).")
    print("- 4x R9700, DeepSeek V4.1 2.00 bpw: 74-77 tok/s decode, 400-450 tok/s prefill at 8K (much larger model).")
    print("- Projection for this build: ~150 tok/s single-stream decode, ~3,000+ tok/s prefill at 32K, 8 x 262K streams.")
    print("  The projection must be replaced by an on-delivery benchmark; see docs/VALIDATION.md.")


if __name__ == "__main__":
    main()
