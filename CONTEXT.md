# TerraOps Fusion

Plataforma de observação da Terra que funde telemetria orbital e medições no terreno para decisões profissionais. **Demo GS:** agronegócio multi-cultura. **Visão:** mesma arquitetura para agrônomos, gestores e extensão futura (geologia, geoambiental).

## Language

**StressFusion**:
Índice 0–100 que combina stress orbital, leitura solo e penalidade de divergência.
_Avoid_: score, risk score

**Camada Orbital**:
Dados de sensoriamento remoto (NDVI, NDWI, precipitação) por talhão.
_Avoid_: satélite genérico

**Camada Terrestre**:
Ground-truth de sensores locais (Wokwi/ESP32) — umidade e pH.
_Avoid_: IoT solto

**Divergência**:
Diferença entre índice orbital e umidade solo acima do limiar configurado.
_Avoid_: erro, bug

**Mission Control**:
Interface híbrida Streamlit + HTML/Anime.js com três zonas por persona.
_Avoid_: painel, dashboard genérico

**Talhão**:
Unidade espacial de monitoramento (café, soja, milho).
_Avoid_: fazenda inteira
