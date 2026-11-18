# Desenvolvimento

## Identidade visual

Mission Control em estilo **sala de comando**: interface sóbria com acentos sci-fi sutis (teal orbital, ochre solo, violeta fusão, âmbar alerta). Tagline: *Satélite + solo → decisão no tempo certo*. Plataforma demonstrada no agronegócio; arquitetura extensível para agrônomos e monitoramento geoambiental.

## Plataforma vs. demo GS

TerraOps Fusion é uma **plataforma multi-módulo** (Orbital, Field Truth, Fusion Engine, Operações, Ciência, Relatórios, Admin) com dezenas de telas planejadas — ver `docs/platform_map.md`. A GS implementa o **backend completo da fusão** e a tela-hub **Mission Control** (módulo Operações), onde operador, gestora e agrônoma conduzem uma missão ao vivo.

## Arquitetura técnica (núcleo entregue)

1. **Camada orbital** — NDVI, NDWI, precipitação (`orbital_readings.csv`)
2. **Camada terrestre** — umidade, pH via Wokwi (`ground_truth.csv`)
3. **Fusão** — `fusion_pipeline.py` + Random Forest + StressFusion
4. **Mission Control (M1)** — Streamlit + HTML/Anime.js via `snapshot.json`
5. **Evolução** — detalhe de talhão, mapa orbital, laudos, modo geo (roadmap documentado)

## Disciplinas integradas

Python, Pandas, ML, SQL, IoT, visualização, economia espacial, LGPD.

## Código principal (trecho)

```python
def stress_fusion_score(ndvi, umidade, precip, prob_alto=None):
    orbital_stress = (1.0 - ndvi) * 40 + max(0, 15 - precip) * 1.5
    ground_stress = max(0, 50 - umidade) * 0.6 + max(0, umidade - 70) * 0.4
    ml_component = (prob_alto or 0.5) * 30
    delta = abs(ndvi - (umidade / 100))
    penalty = 20 if delta > 0.15 else 0
    raw = orbital_stress * 0.4 + ground_stress * 0.35 + ml_component + penalty
    return int(max(0, min(100, round(raw))))
```

Repo: ver README em `tasks/task10_global_solution/`.
