# TerraOps Fusion — Global Solution 2026.1

**FIAP 1TIAOA · Grupo 49** · Prazo **09/06/2026 23h59**

| Integrante | RM |
|------------|-----|
| Higor Henrique Garcia | 571820 |
| Vinicius Alves Lopes dos Anjos | 572814 |
| Igor Zeviani Nogueira | 572822 |
| Humberto Salim | 570536 |

## Para o professor (comece aqui)

1. **`REPRODUCE.md`** — clone → rodar em 5 min
2. **`docs/roteiro_video.md`** — roteiro final e teleprompter
3. **`docs/platform_map.md`** — plataforma completa (~25 telas)
4. **`specs/task10_global_solution/SCREEN_REGISTRY.md`** — spec de cada tela

## Proposta

**Plataforma** de observação da Terra (agro na demo) — fusão orbital + IoT, múltiplos módulos. **Mission Control** é a sala de comando, não o sistema inteiro.

Harness do grupo: `specs/task10_global_solution/HARNESS_GRUPO.md`  
Design telas (Codex): `specs/task10_global_solution/CODEX_BRIEF.md`

## Como rodar

```bash
cd tasks/task10_global_solution
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_pipeline.py
streamlit run dashboard/app.py
```

## Estrutura

```
task10_global_solution/
├── scripts/          # pipeline + fusão
├── ml/               # Random Forest
├── sql/              # schema + queries
├── dashboard/        # Streamlit + mission_control/
├── data/             # CSV + snapshot.json
├── docs/             # proposta, fórmulas, contribuições
└── entrega/          # PDF_SECTIONS
```

## Entrega

- PDF: `entrega/GlobalSolution_Grupo49.pdf` (montar de `PDF_SECTIONS/`)
- Vídeo: `link_video.txt` (YouTube não listado)
- Portal: [assign 616909](https://on.fiap.com.br/mod/assign/view.php?id=616909)
