#!/usr/bin/env python3
"""Pipeline TerraOps Fusion — dados → SQL → ML → snapshot."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from paths import DASHBOARD_APP, TASK_ROOT


def _run(rel: str, label: str) -> None:
    path = TASK_ROOT / rel
    if not path.is_file():
        print(f"ERRO: ausente {rel}", file=sys.stderr)
        sys.exit(1)
    print(f"\n[pipeline] {label}")
    subprocess.run([sys.executable, str(path)], cwd=TASK_ROOT, check=True)


def run_pipeline(*, skip_generate: bool = False) -> None:
    print("=" * 60)
    print("TerraOps Fusion — run_pipeline.py")
    print("=" * 60)
    if not skip_generate:
        _run("scripts/generate_fusion_dataset.py", "Etapa 1 — dataset multi-cultura")
    _run("scripts/ingest_data.py", "Etapa 2 — SQLite")
    _run("ml/train_fusion_model.py", "Etapa 3 — ML fusão")
    _run("scripts/fusion_pipeline.py", "Etapa 4 — snapshot JSON")
    _run("sql/apply_schema.py", "Etapa 5 — schema + fused_scores")
    print("\n[pipeline] Concluído.")
    if DASHBOARD_APP.is_file():
        print(f"  UI: cd {TASK_ROOT.name} && streamlit run dashboard/app.py")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-generate", action="store_true")
    args = parser.parse_args()
    run_pipeline(skip_generate=args.skip_generate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
