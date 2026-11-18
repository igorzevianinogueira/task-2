#!/usr/bin/env python3
"""Ingestão CSV → SQLite — TerraOps Fusion."""

from __future__ import annotations

import sqlite3

import pandas as pd

from paths import DB_PATH, DEFAULT_CSV, GROUND_CSV, ORBITAL_CSV


def ingest() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        fusion = pd.read_csv(DEFAULT_CSV)
        orbital = pd.read_csv(ORBITAL_CSV)
        ground = pd.read_csv(GROUND_CSV)
        fusion.to_sql("fusion_raw", conn, if_exists="replace", index=False)
        orbital.to_sql("orbital_readings", conn, if_exists="replace", index=False)
        ground.to_sql("ground_truth", conn, if_exists="replace", index=False)
        print(f"[ingest] {DB_PATH} — fusion={len(fusion)} orbital={len(orbital)} ground={len(ground)}")
    finally:
        conn.close()


if __name__ == "__main__":
    ingest()
