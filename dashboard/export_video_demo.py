#!/usr/bin/env python3
"""Exporta a Mission Control estática para gravação do vídeo."""

from __future__ import annotations

import json
from pathlib import Path

from embed_builder import build_standalone_html


TASK_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = TASK_ROOT / "data" / "snapshot.json"
OUTPUT = Path(__file__).resolve().parent / "video_demo.html"


def main() -> None:
    data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    if not data.get("talhoes"):
        raise SystemExit("Snapshot sem talhões. Rode scripts/run_pipeline.py.")

    OUTPUT.write_text(build_standalone_html(data), encoding="utf-8")
    print(f"Demo de vídeo: {OUTPUT}")


if __name__ == "__main__":
    main()
