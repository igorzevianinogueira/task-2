# TerraOps Fusion — Produto

## O que é

**Plataforma** de observação da Terra — não um dashboard único. Múltiplos módulos e ~25 telas na visão completa (ver `docs/platform_map.md`).

**GS 2026.1** demonstra o **núcleo** (pipeline + fusão + SQL + ML) e **uma tela-hub**: **Mission Control (M1)** — sala de comando onde operador, gestora e agrônoma executam **uma missão** de fusão orbital + solo.

## Módulos da plataforma

| Módulo | Responsabilidade |
|--------|------------------|
| **Orbital Intelligence** | Mapas, NDVI, séries, fontes Sentinel |
| **Field Truth** | Sensores, IoT, amostras de solo |
| **Fusion Engine** | Pipeline, ML, StressFusion, logs |
| **Operações** | Mission Control, filas, planos de ação |
| **Ciência & Calibração** | Divergência, laudos, validação |
| **Relatórios & LGPD** | Exportações, compliance |
| **Admin** | Áreas, talhões, papéis, APIs |

## Mission Control (esta pasta)

É a tela **M1** do módulo Operações — **hub de missão**, não o sistema inteiro.

| Zona | Tela futura relacionada |
|------|-------------------------|
| Decisão (Carlos) | M2 Fila · M4 Plano de ação · M5 Modo campo |
| Orbital (Renata) | O1 Mapa · O2 Séries · M3 Detalhe talhão |
| Calibração (Helena) | C1 Lab divergência · C2 Laudo · C3 Validação |

## Demo GS (o que rodar no vídeo)

1. Streamlit → **Executar fusão** (F1)
2. Mission Control carrega `snapshot.json` (M1)
3. Três papéis na mesma missão — decisão, priorização, calibração

## Contrato de dados

UI lê `data/snapshot.json`. Backend é fonte da verdade.

## Sucesso na avaliação

Avaliador entende: **plataforma robusta** com demo vertical; Mission Control é a sala de comando do agro, não o produto limitado a 3 cards.
