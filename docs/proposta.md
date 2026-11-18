# Proposta GS — TerraOps Fusion

**Grupo 49** · Global Solution 2026.1 · Economia espacial

## Uma frase (produto)

**TerraOps Fusion** é a plataforma que cruza o que o satélite vê com o que o solo mede — para agrônomos, gestores e operadores decidirem no tempo certo; com potencial para geologia e outros domínios de observação da Terra.

## Pergunta do enunciado

Como a tecnologia espacial pode melhorar a vida das pessoas e processos na Terra?

## Resposta

Hoje, quem trabalha com a Terra (lavoura, solo, área monitorada) usa **dados isolados**: mapa orbital de um lado, sensor ou amostra local do outro. A plataforma **funde as duas camadas** num Mission Control com índice **StressFusion 0–100**, ranking de prioridade e alerta quando satélite e solo **divergem**.

**Demonstração GS:** núcleo da plataforma (dados + fusão + ML + SQL) + **Mission Control** — sala de comando do módulo Operações (1 tela-hub, 3 papéis). Não é “só um dashboard”: o mapa completo (~25 telas, 7 módulos) está em `docs/platform_map.md`.

**Visão de plataforma:** Orbital Intelligence, Field Truth, Fusion Engine, Operações, Ciência & Calibração, Relatórios e Admin — mesmo motor para agrônomos, gestores e evolução geoambiental/geologia.

## Personas (vídeo)

| Persona | Quem representa | Pergunta que responde |
|---------|-----------------|----------------------|
| **Carlos** | Operador | Posso agir no campo agora? |
| **Renata** | Gestora | O que priorizo hoje? |
| **Helena** | Agrônoma / analista | Por que as fontes discordam? |

## Disciplinas

| Disciplina | Evidência |
|------------|-----------|
| Python | `scripts/fusion_pipeline.py`, `run_pipeline.py` |
| Pandas / EDA | `data/fusion_dataset.csv` |
| ML | `ml/train_fusion_model.py` |
| Estatística | `docs/validation_report.md` |
| SQL | `sql/01_schema.sql`, `02_queries_fusion.sql` |
| IoT | `iot/README.md`, Wokwi |
| Visualização | `dashboard/mission_control/` |
| Economia espacial | Sentinel, NDVI, PDF |
| Formação Social | LGPD em `entrega/PDF_SECTIONS/lgpd.md` |

## Vídeo

O vídeo demonstrativo é obrigatório, tem limite de cinco minutos e será
publicado como não listado. O grupo não concorrerá ao pódio.

## Integrantes

Higor Henrique Garcia (571820), Vinicius Anjos (572814), Igor (572822), Humberto (570536).
