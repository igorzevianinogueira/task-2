# ADR 001 — Dados orbitais via cache

**Status:** aceito

## Contexto

Prazo 48h; API Sentinel pode falhar na demo.

## Decisão

Gerar `orbital_readings.csv` determinístico (seed=42) com narrativa Sentinel cache. Trial Sentinel Hub opcional (budget R$50).

## Consequências

Demo estável; PDF documenta `sentinel_source: cache`.
