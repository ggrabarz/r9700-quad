#!/usr/bin/env python3
"""Write one CSV build sheet per option from bom/prices.json."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRICES = ROOT / "bom" / "prices.json"

GROUP = {
    "mainboard": "compute",
    "cpu": "compute",
    "ram_64gb": "memory",
    "nvme_gen5_1tb": "storage",
    "nvme_gen4_1tb": "storage",
    "sata_4tb": "storage",
    "sata_8tb": "storage",
    "mcio_cable": "storage",
    "slimsas_cable": "storage",
    "psu": "power",
    "cooler_aio": "cooling",
    "case_meshify": "chassis",
    "case_9000d": "chassis",
    "case_enthoo": "chassis",
    "fan_140": "chassis",
}


def main() -> None:
    data = json.loads(PRICES.read_text(encoding="utf-8"))
    items = data["items"]
    for code, option in data["options"].items():
        path = ROOT / "bom" / f"option-{code.lower()}.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(["group", "item", "model", "qty", "unit_eur", "line_eur", "source", "note"])
            subtotal = 0.0
            for key, qty in option["items"].items():
                item = items[key]
                line = item["price"] * qty
                subtotal += line
                writer.writerow([
                    GROUP.get(key, "other"),
                    key,
                    item["name"],
                    qty,
                    f"{item['price']:.2f}",
                    f"{line:.2f}",
                    item["source"],
                    item["note"],
                ])
            contingency = subtotal * data["assumptions"]["contingency_pct"] / 100.0
            writer.writerow([])
            writer.writerow(["", "", "Platform subtotal", "", "", f"{subtotal:.2f}", "", "GPUs excluded"])
            writer.writerow(["", "", f"Contingency {data['assumptions']['contingency_pct']}%", "", "", f"{contingency:.2f}", "", "price/stock volatility"])
            writer.writerow(["", "", "Platform total", "", "", f"{subtotal + contingency:.2f}", "", ""])
            gpu = items["gpu_r9700"]
            writer.writerow(["", "", "GPU replacement value (owned, excluded)", gpu["qty"], f"{gpu['price']:.2f}",
                             f"{gpu['price'] * gpu['qty']:.2f}", gpu["source"], "for reference only"])
            writer.writerow(["", "", "Total if buying GPUs", "", "", f"{subtotal + contingency + gpu['price'] * gpu['qty']:.2f}", "", ""])
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
