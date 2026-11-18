# Fórmula StressFusion 0–100

## Componentes

1. **Stress orbital** = `(1 - NDVI) × 40 + max(0, 15 - precip_mm) × 1.5`
2. **Stress solo** = `max(0, 50 - umidade) × 0.6 + max(0, umidade - 70) × 0.4`
3. **Componente ML** = `P(stress_alto) × 30` (Random Forest)
4. **Penalidade divergência** = `20` se `|NDVI - umidade/100| > 0.15`, senão `0`

## Explicação de divergência (Helena)

Quando `Δ > 0.15`, `explain_divergence()` classifica:

| Tipo | Significado |
|------|-------------|
| `orbital_otimista` | NDVI alto vs solo seco — satélite superestima vigor |
| `orbital_pessimista` | NDVI baixo vs solo úmido — satélite subestima umidade local |
| `coerente` | Δ dentro do limiar — fontes alinhadas |

Campos no `snapshot.json`: `resumo`, `explicacao` (cadeia Δ), `hipoteses[]`, `acao_sugerida`, `penalidade`.

## Fórmula final

```
StressFusion = clamp(0.4×orbital + 0.35×solo + ML + penalidade, 0, 100)
```

## Categorias

| Faixa | Categoria |
|-------|-----------|
| 0–33 | baixo |
| 34–66 | medio |
| 67–100 | alto |

Implementação: `scripts/fusion_pipeline.py` → `stress_fusion_score()` + `explain_divergence()`.
