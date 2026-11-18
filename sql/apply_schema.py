#!/usr/bin/env python3
"""Aplica schema e popula fused_scores a partir do snapshot."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DB = BASE / "data" / "terraops.db"
SCHEMA = Path(__file__).parent / "01_schema.sql"
SNAPSHOT = BASE / "data" / "snapshot.json"


def main() -> None:
    conn = sqlite3.connect(DB)
    try:
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))
        if SNAPSHOT.is_file():
            data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        else:
            import sys

            sys.path.insert(0, str(BASE / "scripts"))
            from fusion_pipeline import export_snapshot

            export_snapshot()
            data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        conn.execute("DELETE FROM fused_scores")
        for t in data.get("talhoes", []):
            conn.execute(
                """
                INSERT INTO fused_scores
                (talhao_id, stress_fusion, categoria, divergencia_ativa, captured_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    t["id"],
                    t["stress_fusion"],
                    t["categoria"],
                    1 if t["divergencia"]["ativa"] else 0,
                    data["generated_at"],
                ),
            )
        conn.commit()
        print(f"[sql] schema aplicado em {DB}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
