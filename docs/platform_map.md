# Mapa da plataforma — TerraOps Fusion

> **Não é um dashboard.** É um **sistema** com módulos, papéis e dezenas de telas.  
> **GS 2026.1** entrega o **núcleo executável** + **1 tela-hub** (Mission Control) que prova a fusão end-to-end.

## Metáfora

| Errado | Certo |
|--------|-------|
| “Um painel com 3 cards” | **Plataforma** com shell, módulos e fluxos por persona |
| Demo = produto inteiro | Demo = **fatia vertical** do módulo Operações |

## Arquitetura de produto (camadas)

```
┌─────────────────────────────────────────────────────────────┐
│  SHELL — navegação, domínio (Agro · Geo · …), perfil, BRT   │
├──────────────┬──────────────┬──────────────┬──────────────────┤
│  ORBITAL     │  TERRESTRE   │  FUSÃO       │  OPERAÇÕES       │
│  Intel       │  Field Truth │  Engine      │  (Mission Ctrl)  │
├──────────────┴──────────────┴──────────────┴──────────────────┤
│  CIÊNCIA & CALIBRAÇÃO │ RELATÓRIOS │ ADMIN & COMPLIANCE (LGPD) │
└─────────────────────────────────────────────────────────────┘
```

**Backend GS (já existe):** `generate` → `ingest` → `ml` → `fusion_pipeline` → `snapshot.json` → SQL.

**Frontend GS (demo):** Mission Control = **hub da camada Operações** (3 zonas = 3 papéis na mesma missão).

---

## Inventário de telas (visão completa)

### Shell & acesso
| # | Tela | Função | GS |
|---|------|--------|-----|
| S1 | Login / seleção de organização | Multi-tenant | 🔜 |
| S2 | Home / seletor de domínio | Agro · Geoambiental · … | narrativa PDF |
| S3 | Central de notificações | Alertas cross-módulo | 🔜 |

### Módulo Orbital Intelligence
| # | Tela | Função | GS |
|---|------|--------|-----|
| O1 | Mapa orbital (tiles NDVI/NDWI) | Visão macro Sentinel | parcial (ranking) |
| O2 | Série temporal por talhão/área | Histórico orbital | 🔜 |
| O3 | Comparador de passagens | Antes/depois satélite | 🔜 |
| O4 | Catálogo de fontes | Copernicus, Sentinel Hub, cache | doc ADR |

### Módulo Field Truth (terrestre)
| # | Tela | Função | GS |
|---|------|--------|-----|
| T1 | Mapa de sensores / estações | Wokwi, ESP32, estações | `iot/README` |
| T2 | Leitura em tempo real | Umidade, pH, telemetria | CSV + snapshot |
| T3 | Importação de amostras | Upload CSV / API | pipeline |
| T4 | Qualidade do sinal | Confiança ground-truth | 🔜 |

### Módulo Fusion Engine
| # | Tela | Função | GS |
|---|------|--------|-----|
| F1 | Console de fusão | Executar pipeline (Streamlit hoje) | ✅ sidebar |
| F2 | Configuração de pesos StressFusion | Pesos orbital/solo/ML | fórmula doc |
| F3 | Modelo ML — métricas & features | Recall, importance | ✅ ml/ |
| F4 | Log de execuções | Auditoria de fusões | SQL |

### Módulo Operações — **Mission Control (hub GS)**
| # | Tela | Função | GS |
|---|------|--------|-----|
| **M1** | **Mission Control — visão 3 zonas** | Carlos + Renata + Helena numa missão | ✅ **demo vídeo** |
| M2 | Fila de decisões | Aprovar / adiar / escalar | 🔜 |
| M3 | Detalhe do talhão | Drill-down cultura, histórico | 🔜 |
| M4 | Plano de ação | Irrigação, janela de máquina | 🔜 |
| M5 | Modo campo (mobile) | Carlos offline simplificado | 🔜 |

### Módulo Ciência & Calibração (agrônomo / analista)
| # | Tela | Função | GS |
|---|------|--------|-----|
| C1 | Laboratório de divergência | Orbital vs solo, Δ, limiar | zona Calibração |
| C2 | Laudo por talhão (PDF) | Helena exporta parecer | 🔜 |
| C3 | Validação estatística | Correlações, relatório | validation_report |
| C4 | Modo geologia | Métricas de área/alteração | roadmap |

### Módulo Relatórios & Compliance
| # | Tela | Função | GS |
|---|------|--------|-----|
| R1 | Biblioteca de relatórios | Histórico exportações | 🔜 |
| R2 | LGPD & dados simulados | Transparência, retenção | PDF lgpd |
| R3 | Integração disciplinar | Evidências por matéria | PDF |

### Admin
| # | Tela | Função | GS |
|---|------|--------|-----|
| A1 | Fazendas / áreas / talhões | CRUD espacial | dataset |
| A2 | Usuários & papéis | RBAC por persona | 🔜 |
| A3 | Orçamento APIs | Sentinel, budget R$50 | ADR 001 |

**Total visão:** ~25 telas · **GS implementa ~6 de forma real** + roadmap documentado.

---

## O que a GS prova (robustez acadêmica)

| Camada | Evidência executável |
|--------|----------------------|
| Dados 3 camadas | orbital + ground + fusion CSV/DB |
| Motor de fusão | Python + ML + SQL + índice proprietário |
| Contrato API/UI | `snapshot.json` + schema |
| Hub operacional | Mission Control (não é o sistema inteiro, é a **sala de comando**) |
| Extensibilidade | Mesmo motor → modos Agro / Geo / Agronomia no PDF |

## Narrativa para vídeo/PDF (30s)

> “TerraOps é uma **plataforma** — mapas orbitais, sensores no campo, motor de fusão e salas de comando por perfil. Na Global Solution mostramos o **Mission Control** do agronegócio: uma missão ao vivo com operador, gestora e agrônoma. O restante do mapa de telas é a evolução natural do mesmo backend.”

## Próximas telas (pós-GS, prioridade PO)

1. **M3** Detalhe do talhão (drill-down do ranking)
2. **O1** Mapa orbital com tile real/cache
3. **C2** Laudo exportável Helena
4. **S2** Seletor de domínio Agro | Geo

## Igor / UI

Mission Control = **tela M1**. Polish visual não expande escopo GS; novas telas = branches pós-entrega com PO.
