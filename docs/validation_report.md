# Relatório de validação — TerraOps Fusion

## Correlação orbital ↔ solo

Métrica: Pearson entre `ndvi` e `umidade_solo/100` no dataset `fusion_dataset.csv`.

| Métrica | Valor típico (seed=42) |
|---------|------------------------|
| Correlação | ~0.35–0.55 (simulado) |
| Interpretação | Correlação moderada; divergências justificam fusão |

## Modelo ML

Ver `models/fusion_metrics.json` após `run_pipeline.py`.

## Divergência

Limiar 0.15 em `fusion_pipeline.py`. Talhões com `divergencia.ativa=true` listados no snapshot com explicação detalhada (`tipo`, `resumo`, `explicacao`, `hipoteses`, `acao_sugerida`) via `explain_divergence()`.

## Reprodutibilidade

`python scripts/generate_fusion_dataset.py --seed 42`
