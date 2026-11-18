#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

.venv/bin/python scripts/run_pipeline.py
.venv/bin/python dashboard/export_video_demo.py

echo
echo "Abra no navegador:"
echo "file://$(pwd)/dashboard/video_demo.html"
