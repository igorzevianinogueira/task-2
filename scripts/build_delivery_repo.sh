#!/usr/bin/env bash
# Monta repo de entrega GS no layout TIAO (1TIAO/Global-Solution-1).
set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")/../../.." && pwd)"
TASK="$WORKSPACE/tasks/task10_global_solution"
DEST="${1:-$HOME/terraops-fusion-gs49}"
TEMPLATE="https://github.com/CaiqueFiap-2026/TEMPLATE-TIAO-2026.git"
GS="$DEST/1TIAO/Global-Solution-1"

rm -rf "$DEST"
git clone --depth 1 "$TEMPLATE" "$DEST"
rm -rf "$DEST/.git"

mkdir -p "$GS/src" "$GS/docs" "$GS/data"

for item in scripts ml sql dashboard iot models requirements.txt REPRODUCE.md; do
  if [[ -e "$TASK/$item" ]]; then
    cp -a "$TASK/$item" "$GS/src/"
  fi
done

for f in proposta.md stress_fusion_formula.md platform_map.md validation_report.md \
  demo_script_5min.md CONTRIBUICOES.md visual_identity.md ml_model.md snapshot_schema.md; do
  if [[ -f "$TASK/docs/$f" ]]; then
    cp "$TASK/docs/$f" "$GS/docs/"
  fi
done

for f in "$TASK"/data/*; do
  base="$(basename "$f")"
  [[ "$base" == "terraops.db" ]] && continue
  cp -a "$f" "$GS/data/"
done

echo "Repo montado em $DEST"
