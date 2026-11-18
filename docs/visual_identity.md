# Identidade visual — TerraOps Fusion

> **Aprovado PO 07/06** · Travar antes do grupo integrar na `main`.

## Direção (Impeccable shape)

| Eixo | Decisão |
|------|---------|
| **Cenário** | Sala de comando — sobrio, profissional, “missão real” |
| **Pega** | Sci-fi **sutil** (acentos, glow leve, tipografia mono nas métricas) — **não** cyberpunk neon |
| **Tom** | Moderno, arrojado, elegante |
| **Cor** | **Não monocromático** — orbital (teal), solo (ochre), fusão (violeta), alerta (âmbar) |
| **Evitar** | Beige/cream, glassmorphism, hero SaaS genérico, arco-íris futurista |

## Frase na UI

**Tagline:** *Satélite + solo → decisão no tempo certo*

**StressFusion (primeira aparição):** *Índice de stress fundido (0–100)*

## Paletas (testar em `palette-lab.html`)

| ID | Nome | Caráter | Recomendação |
|----|------|---------|--------------|
| **A** | `command-deck` | Navy profundo + teal + violeta + ochre | **Padrão PO** |
| **B** | `orbital-dusk` | Cinza-azulado + ciano + cobre + índigo | Alternativa mais fria |
| **C** | `terra-signal` | Preto azul + ciano claro + âmbar solo + lavanda | Alternativa mais contrastada |

Trocar tema: `document.documentElement.dataset.theme = "command-deck"` ou botões no lab.

**Como escolher:** abrir `dashboard/mission_control/palette-lab.html` no Chrome → comparar lado a lado → PO responde A/B/C no grupo.

## Hierarquia visual

```
Header (marca + tagline + meta Sentinel)
├── Zona Decisão [accent âmbar]     — Carlos — score + recomendação
├── Zona Orbital [accent teal]        — Renata — ranking
└── Zona Calibração [accent violeta]  — Helena — barras + divergência
Footer timeline (alertas)
```

## Motion (sci-fi sutil)

- Entrada stagger das zonas (120ms)
- Count-up métrica principal (800ms, easeOutExpo)
- Pulse âmbar no alerta (2×, sem loop infinito)
- Glow vermelho suave só quando divergência ativa
- `prefers-reduced-motion`: sem animação

## Arquivos de referência

| Arquivo | Função |
|---------|--------|
| `dashboard/mission_control/DESIGN.md` | Tokens + anti-patterns |
| `dashboard/mission_control/styles/tokens.css` | CSS ativo (tema A) |
| `specs/task10_global_solution/VISUAL_BRIEF.md` | Wireframe + Igor |
| `specs/task10_global_solution/VISUAL_LOCK.md` | Decisões travadas |

## Integração grupo

- **Igor:** polish dentro do tema travado — não mudar paleta sem PO
- **Higor:** gravação e Streamlit com tema A até novo aviso
- **PDF:** prints 1920×1080 com tema escolhido
