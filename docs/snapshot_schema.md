# Schema — data/snapshot.json

```json
{
  "generated_at": "ISO-8601",
  "talhoes": [
    {
      "id": "T-01",
      "cultura": "cafe|soja|milho",
      "stress_fusion": 0,
      "categoria": "baixo|medio|alto",
      "orbital": { "ndvi": 0.0, "ndwi": 0.0, "precip_mm": 0.0, "tile_url": "" },
      "terrestre": { "umidade_solo": 0.0, "ph": 0.0, "fonte": "wokwi" },
      "divergencia": {
        "ativa": false,
        "delta_ndvi_umidade": 0.0,
        "limiar": 0.15,
        "tipo": "coerente|orbital_otimista|orbital_pessimista",
        "orbital_interp": "string",
        "solo_interp": "string",
        "resumo": "string",
        "explicacao": "cadeia Δ verificável",
        "hipoteses": ["string"],
        "penalidade": 0,
        "acao_sugerida": "string"
      },
      "recomendacao": "string"
    }
  ],
  "alertas": [
    {
      "tipo": "stress_hidrico|divergencia",
      "talhao_id": "T-01",
      "severidade": "alto|medio",
      "mensagem": "opcional — resumo da divergência"
    }
  ],
  "meta": { "sentinel_source": "cache|live", "wokwi_url": "https://..." },
  "feature_importance": [{ "feature": "string", "importance": 0.0 }]
}
```

Gerado por `scripts/fusion_pipeline.py` após `run_pipeline.py`.
