#!/usr/bin/env python3
"""Gera dataset multi-cultura com camadas orbital + terrestre — TerraOps Fusion."""

from __future__ import annotations

import argparse
import csv
import random
from datetime import datetime, timezone
from pathlib import Path

from paths import DATA_DIR, DEFAULT_CSV, GROUND_CSV, ORBITAL_CSV

TALHOES = [
    ("T-01", "cafe", -22.90, -47.06),
    ("T-02", "soja", -23.55, -46.63),
    ("T-03", "milho", -21.17, -47.81),
    ("T-04", "cafe", -22.12, -46.95),
    ("T-05", "soja", -23.10, -47.20),
]

FUSION_SCHEMA = [
    "talhao_id",
    "cultura",
    "ndvi",
    "ndwi",
    "precip_mm",
    "umidade_solo",
    "ph",
    "temperatura",
    "declividade",
    "stress_label",
]


def _stress_score(
    ndvi: float,
    umidade: float,
    precip: float,
    declividade: float,
) -> tuple[int, float]:
    """Deriva label e score interno para treino."""
    score = 0.0
    if ndvi < 0.35:
        score += 35
    elif ndvi < 0.5:
        score += 20
    if umidade < 25:
        score += 25
    elif umidade > 75:
        score += 15
    if precip < 5:
        score += 20
    if declividade > 12:
        score += 15
    score = min(100.0, score)
    return (1 if score >= 50 else 0, score)


def generate(*, seed: int = 42, rows_per_talhao: int = 40) -> None:
    random.seed(seed)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    fusion_rows: list[dict[str, object]] = []
    orbital_rows: list[dict[str, object]] = []
    ground_rows: list[dict[str, object]] = []
    now = datetime.now(timezone.utc).isoformat()

    for talhao_id, cultura, _lat, _lon in TALHOES:
        for i in range(rows_per_talhao):
            ndvi = round(random.uniform(0.25, 0.85), 3)
            ndwi = round(random.uniform(0.1, 0.6), 3)
            precip = round(random.uniform(0, 45), 1)
            umidade = round(random.uniform(15, 90), 1)
            ph = round(random.uniform(5.0, 7.5), 1)
            temp = round(random.uniform(18, 34), 1)
            decl = round(random.uniform(0, 18), 1)
            label, _ = _stress_score(ndvi, umidade, precip, decl)
            ts = now
            fusion_rows.append(
                {
                    "talhao_id": talhao_id,
                    "cultura": cultura,
                    "ndvi": ndvi,
                    "ndwi": ndwi,
                    "precip_mm": precip,
                    "umidade_solo": umidade,
                    "ph": ph,
                    "temperatura": temp,
                    "declividade": decl,
                    "stress_label": label,
                }
            )
            if i == 0:
                orbital_rows.append(
                    {
                        "talhao_id": talhao_id,
                        "ndvi": ndvi,
                        "ndwi": ndwi,
                        "precip_mm": precip,
                        "captured_at": ts,
                        "fonte": "sentinel-cache",
                    }
                )
                ground_rows.append(
                    {
                        "talhao_id": talhao_id,
                        "umidade_solo": umidade,
                        "ph": ph,
                        "fonte": "wokwi",
                        "captured_at": ts,
                    }
                )

    for path, schema, rows in (
        (DEFAULT_CSV, FUSION_SCHEMA, fusion_rows),
        (ORBITAL_CSV, list(orbital_rows[0].keys()) if orbital_rows else [], orbital_rows),
        (GROUND_CSV, list(ground_rows[0].keys()) if ground_rows else [], ground_rows),
    ):
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=schema)
            writer.writeheader()
            writer.writerows(rows)
        print(f"[generate] {path} — {len(rows)} linhas")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    generate(seed=args.seed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
