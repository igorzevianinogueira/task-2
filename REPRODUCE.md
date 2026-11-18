# Reproduzir localmente (perspectiva do professor)

> **Entrega oficial:** o link no PDF aponta para o **repo de entrega** (GitHub novo, template TIAO) — não para `fiap-academic-workflow`. Instruções abaixo valem para o conteúdo exportado desse repo.

> **Meta:** clone → produto rodando em **≤5 minutos**, sem conhecimento prévio do grupo.

## Pré-requisitos

- Python 3.10+
- Git
- Navegador Chrome ou Firefox

## Passo a passo

```bash
git clone https://github.com/higorhg/fiap-academic-workflow.git
cd fiap-academic-workflow/tasks/task10_global_solution

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python scripts/run_pipeline.py     # Gera dados + snapshot + ML + SQL
streamlit run dashboard/app.py     # Abre http://localhost:8501
```

## O que fazer na UI (ordem sugerida)

| # | Ação | O que o professor deve ver |
|---|------|----------------------------|
| 1 | Clicar **Executar fusão** (sidebar) | Pipeline roda; snapshot atualiza |
| 2 | Mission Control (área principal) | 3 zonas com números reais |
| 3 | Menu **Navegação** (quando shell existir) | Home → Mission Control → Talhão → ML |
| 4 | Abrir `dashboard/mission_control/palette-lab.html` (opcional) | Identidade visual |

## Telas sem Streamlit (abrir no navegador)

| Arquivo | Tela |
|---------|------|
| `dashboard/shell/home.html` | Entrada da plataforma (S2) |
| `dashboard/mission_control/index.html` | Mission Control (M1) |
| `dashboard/screens/talhao.html` | Detalhe talhão (M3) |
| `dashboard/screens/ml_lab.html` | Métricas ML (F3) |

> Se `dashboard/screens/` ainda não existir, ver `specs/task10_global_solution/screens/` — specs para implementação.

## Verificação (gates)

```bash
python scripts/run_pipeline.py          # exit 0
python ml/train_fusion_model.py         # exit 0
test -f data/snapshot.json && echo OK
```

## Problemas comuns

| Sintoma | Solução |
|---------|---------|
| Snapshot vazio na UI | Rodar `python scripts/run_pipeline.py` |
| `index.html` sem dados | Abrir via Streamlit embed ou servir pasta `dashboard/` |
| Erro de dependência | `pip install -r requirements.txt` no venv |

## Documentação de produto

- Mapa de telas: `docs/platform_map.md`
- Demo 5 min (vídeo): `docs/demo_script_5min.md`
- Specs por tela: `specs/task10_global_solution/SCREEN_REGISTRY.md`
