#!/usr/bin/env python3
"""Generate the Markdown BOM snippets used by the docs site.

The site source stays Markdown; this script only keeps the tables in sync
with the same CSV/JSON the calculator uses.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICES = ROOT / "bom" / "prices.json"
SITE_BOM = ROOT / "site-src" / "docs" / "_bom"

PART_SLUGS = {
    "mainboard": "asrock-wrx90-ws-evo",
    "mainboard_asus_sage": "asus-wrx90e-sage-se",
    "cpu": "amd-9955wx",
    "ram_64gb": "samsung-64gb-5600",
    "ram_64gb_6400_2x": "micron-64gb-6400",
    "ram_64gb_6400_4x": "gskill-4x64-6400",
    "ram_64gb_6400_8x": "gskill-8x64-6400",
    "nvme_gen5_1tb": "samsung-9100-pro",
    "nvme_gen4_1tb": "samsung-990-pro",
    "sata_4tb": "samsung-870-evo",
    "sata_8tb": "toshiba-n300",
    "mcio_cable": "mcio-cable",
    "slimsas_cable": "slimsas-cable",
    "psu": "seasonic-px-2200",
    "cooler_aio": "silverstone-xe360-tr5",
    "case_meshify": "fractal-meshify-2-xl",
    "fan_140": "fan-140",
    "gpu_r9700": "radeon-r9700",
}

GROUP_LABEL = {
    "compute": "Compute",
    "memory": "Memory",
    "storage": "Storage",
    "power": "Power",
    "cooling": "Cooling",
    "chassis": "Chassis",
}

GROUP_ORDER = ["compute", "memory", "storage", "power", "cooling", "chassis"]


def eur(value: float) -> str:
    return f"€{value:,.2f}"


def clean(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def main() -> None:
    data = json.loads(PRICES.read_text(encoding="utf-8"))
    items = data["items"]
    assumptions = data["assumptions"]
    gpu = items["gpu_r9700"]
    gpu_total = gpu["price"] * gpu["qty"]
    SITE_BOM.mkdir(parents=True, exist_ok=True)

    for code, option in data["options"].items():
        csv_path = ROOT / "bom" / f"option-{code.lower()}.csv"
        rows = [r for r in csv.DictReader(csv_path.open(encoding="utf-8")) if r.get("group")]
        lines: list[str] = []
        for group in GROUP_ORDER:
            group_rows = [r for r in rows if r["group"] == group]
            if not group_rows:
                continue
            lines.append(f"### {GROUP_LABEL[group]}")
            lines.append("")
            lines.append("| Part | Qty | Unit | Line | Notes |")
            lines.append("|---|---:|---:|---:|---|")
            for row in group_rows:
                slug = PART_SLUGS.get(row["item"])
                name = clean(row["model"])
                label = f"[{name}](../parts/{slug}.md)" if slug else name
                lines.append(
                    f"| {label} | {row['qty']} | {eur(float(row['unit_eur']))} | "
                    f"{eur(float(row['line_eur']))} | {clean(row['note'])} |"
                )
            lines.append("")

        subtotal = sum(float(r["line_eur"]) for r in rows)
        contingency = subtotal * assumptions["contingency_pct"] / 100.0
        total = subtotal + contingency
        lines.extend(
            [
                "### Totals",
                "",
                "| | Amount |",
                "|---|---:|",
                f"| **Parts subtotal** | **{eur(subtotal)}** |",
                f"| {assumptions['contingency_pct']}% contingency | {eur(contingency)} |",
                f"| **Platform total (GPUs excluded)** | **{eur(total)}** |",
                f"| GPUs (owned, replacement value) | {eur(gpu_total)} |",
                f"| **Total if buying the four GPUs** | **{eur(total + gpu_total)}** |",
                "",
            ]
        )
        target = SITE_BOM / f"{code.lower()}.md"
        target.write_text("\n".join(lines), encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
