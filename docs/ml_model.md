# Modelo ML — TerraOps Fusion

**Algoritmo:** RandomForestClassifier  
**Target:** `stress_label` (0/1)  
**Features:** ndvi, ndwi, precip_mm, umidade_solo, ph, temperatura, declividade, cultura

**Saída:** probabilidade de stress alto → componente StressFusion

**Artefatos:** `models/fusion_model.joblib`, `models/feature_importance.csv`

```bash
python ml/train_fusion_model.py
```
