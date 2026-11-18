# TerraOps Mission Control — Design

## Scene

Sala de comando pré-amanhecer: operadores monitoram fusão orbital + solo. Sobrio, moderno, sci-fi **sutil** — não filme de ficção.

## Direção PO (07/06)

- Elegante e arrojado
- Multicolor semântico (orbital / solo / fusão / alerta)
- Tipografia: sans UI + mono métricas
- Glow apenas em alertas e divergência ativa

## Tema padrão: `command-deck`

| Token | Hex | Uso |
|-------|-----|-----|
| `--bg` | `#0a0e17` | Fundo navy espacial |
| `--surface` | `#121a2a` | Painéis |
| `--border` | `#2a3548` | Divisórias |
| `--ink` | `#e8ecf4` | Texto principal |
| `--muted` | `#8b95a8` | Labels |
| `--orbital` | `#2ec4b6` | Teal — satélite, NDVI |
| `--ground` | `#d4a574` | Ochre — solo, umidade |
| `--fusion` | `#9b8cff` | Violeta — índice fundido, acentos sci-fi |
| `--alert` | `#e8b84a` | Âmbar — avisos |
| `--danger` | `#e85d5d` | Divergência crítica |

## Acentos por zona

| Zona | Borda superior | Persona |
|------|----------------|---------|
| Decisão | `--alert` | Carlos |
| Orbital | `--orbital` | Renata |
| Calibração | `--fusion` | Helena |

## Tipografia

- UI: `Segoe UI`, system-ui, sans-serif
- Métricas: `JetBrains Mono`, monospace
- Labels zona: uppercase, letter-spacing 0.08em

## Layout

Grid 3 colunas ≥900px; stack mobile. Header com tagline. Timeline full-width.

## Motion

Anime.js CDN · easeOutExpo · ver `docs/visual_identity.md`

## Anti-patterns (banned)

- Fundo cream/beige
- Monocromia total
- Neon/cyberpunk
- Glassmorphism decorativo
- Hero-metric SaaS template
- Números hardcoded no JS

## Paletas alternativas

Ver `palette-lab.html` — temas `orbital-dusk`, `terra-signal`. Só trocar com OK PO.
