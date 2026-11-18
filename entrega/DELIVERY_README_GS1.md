# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png" 
       alt="FIAP" width="40%">
</a>
</p>

<br>

# TerraOps Fusion

## Grupo 49 · Turma 1TIAOA · Global Solution 2026.1

## 👨‍🎓 Integrantes

- Higor Henrique Garcia — RM 571820
- Vinicius Alves Lopes dos Anjos — RM 572814
- Igor Zeviani Nogueira — RM 572822
- Humberto Salim — RM 570536

## 📜 Descrição

**TerraOps Fusion** é uma plataforma de observação da Terra que funde telemetria orbital (NDVI, NDWI, precipitação) com sensores terrestres (umidade, pH via Wokwi/ESP32) para gerar o índice **StressFusion** (0–100) e apoiar decisões no agronegócio.

A demo da Global Solution apresenta o **Mission Control** — interface híbrida Streamlit + HTML com três zonas por persona (operador, gestora, agrônoma).

**Disciplinas integradas:** Python, Pandas, Machine Learning, SQL, IoT, visualização de dados, economia espacial.

**Competição:** o grupo **não concorre** ao pódio da premiação.

## 📁 Estrutura de pastas

- **docs/** — proposta, fórmulas, validação, mapa da plataforma
- **src/** — scripts, ML, SQL, dashboard Streamlit, IoT
- **data/** — CSVs e snapshot JSON da demonstração

## 📎 Links

- **Vídeo (YouTube não listado):** https://www.youtube.com/watch?v=ufqJxUwcyr0
- **Repositório:** https://github.com/higorhg/terraops-fusion-gs49

## 🔧 Como executar

```bash
cd src
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_pipeline.py
streamlit run dashboard/app.py
```

Abra http://localhost:8501 → sidebar **Executar fusão** → Mission Control.

Detalhes: `src/REPRODUCE.md`

## 🗃 Histórico

* 1.0.0 - 09/06/2026 — Entrega Global Solution Grupo 49

---

## 📋 Licença

Projeto acadêmico FIAP — Attribution 4.0 International (template TIAO).
