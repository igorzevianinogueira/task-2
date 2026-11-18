#!/usr/bin/env python3
"""Motor de fusão orbital + terrestre → StressFusion."""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd

from paths import DEFAULT_CSV, MODEL_PATH, ORBITAL_CSV, GROUND_CSV, SNAPSHOT_PATH

DIVERGENCE_THRESHOLD = 0.15
WOKWI_URL = "https://wokwi.com/projects/esp32-terraops-fusion"


def _interpret_orbital(ndvi: float) -> str:
    if ndvi >= 0.6:
        return "vegetação vigorosa"
    if ndvi >= 0.4:
        return "cobertura moderada"
    return "stress vegetativo orbital"


def _interpret_solo(umidade: float) -> str:
    if umidade >= 70:
        return "solo encharcado"
    if umidade >= 50:
        return "umidade adequada"
    if umidade >= 35:
        return "solo em atenção"
    return "solo seco"


def explain_divergence(
    ndvi: float,
    umidade: float,
    *,
    limiar: float = DIVERGENCE_THRESHOLD,
) -> dict:
    """Explica divergência orbital↔solo em cadeia verificável (resumo + hipóteses)."""
    umidade_norm = umidade / 100
    delta = abs(ndvi - umidade_norm)
    ativa = delta > limiar
    orbital_interp = _interpret_orbital(ndvi)
    solo_interp = _interpret_solo(umidade)

    if not ativa:
        return {
            "ativa": False,
            "delta_ndvi_umidade": round(delta, 3),
            "limiar": limiar,
            "tipo": "coerente",
            "orbital_interp": orbital_interp,
            "solo_interp": solo_interp,
            "resumo": (
                f"Fontes alinhadas: orbital ({orbital_interp}) e solo ({solo_interp}) "
                f"concordam dentro do limiar."
            ),
            "explicacao": (
                f"Δ = |NDVI − umidade/100| = |{ndvi:.3f} − {umidade_norm:.3f}| = {delta:.3f} "
                f"≤ {limiar}. NDVI {ndvi:.2f} e umidade {umidade:.1f}% sustentam fusão coerente."
            ),
            "hipoteses": [],
            "penalidade": 0,
            "acao_sugerida": "Manter monitoramento de rotina; sem calibração urgente.",
        }

    if ndvi > umidade_norm:
        tipo = "orbital_otimista"
        resumo = (
            f"Satélite indica {orbital_interp} (NDVI {ndvi:.2f}), "
            f"mas solo mede {umidade:.1f}% — {solo_interp}."
        )
        explicacao = (
            f"Δ = |{ndvi:.3f} − {umidade_norm:.3f}| = {delta:.3f} > limiar {limiar}. "
            f"A camada orbital superestima vigor em relação ao ground-truth local."
        )
        hipoteses = [
            "Atraso na resposta do NDVI após evento hídrico local",
            "Sensor de umidade descalibrado ou mal posicionado no talhão",
            "Variação intra-talhão não capturada pelo pixel Sentinel",
        ]
        acao = "Validar leitura Wokwi e comparar com amostra de solo no ponto crítico."
    else:
        tipo = "orbital_pessimista"
        resumo = (
            f"Satélite indica {orbital_interp} (NDVI {ndvi:.2f}), "
            f"mas solo mede {umidade:.1f}% — {solo_interp}."
        )
        explicacao = (
            f"Δ = |{ndvi:.3f} − {umidade_norm:.3f}| = {delta:.3f} > limiar {limiar}. "
            f"A camada orbital subestima a condição hídrica medida no campo."
        )
        hipoteses = [
            "Irrigação recente ainda não refletida no NDVI orbital",
            "Sombra ou nuvem residual na passagem Sentinel",
            "Umidade em subsuperfície não visível ao sensor orbital",
        ]
        acao = "Aguardar próxima passagem orbital ou cruzar com NDWI antes de decisão de campo."

    return {
        "ativa": True,
        "delta_ndvi_umidade": round(delta, 3),
        "limiar": limiar,
        "tipo": tipo,
        "orbital_interp": orbital_interp,
        "solo_interp": solo_interp,
        "resumo": resumo,
        "explicacao": explicacao,
        "hipoteses": hipoteses,
        "penalidade": 20,
        "acao_sugerida": acao,
    }


def stress_fusion_score(
    ndvi: float,
    umidade: float,
    precip: float,
    prob_alto: float | None = None,
) -> int:
    """StressFusion 0–100 — ver docs/stress_fusion_formula.md."""
    orbital_stress = (1.0 - ndvi) * 40 + max(0, 15 - precip) * 1.5
    ground_stress = max(0, 50 - umidade) * 0.6 + max(0, umidade - 70) * 0.4
    ml_component = (prob_alto or 0.5) * 30
    delta = abs(ndvi - (umidade / 100))
    penalty = 20 if delta > DIVERGENCE_THRESHOLD else 0
    raw = orbital_stress * 0.4 + ground_stress * 0.35 + ml_component + penalty
    return int(max(0, min(100, round(raw))))


def categoria(score: int) -> str:
    if score <= 33:
        return "baixo"
    if score <= 66:
        return "medio"
    return "alto"


def recomendacao(score: int, cultura: str) -> str:
    if score >= 67:
        return f"Adiar operação de máquina no talhão ({cultura}) por 6h"
    if score >= 34:
        return f"Monitorar irrigação no talhão ({cultura}) nas próximas 12h"
    return f"Condições favoráveis para operação no talhão ({cultura})"


def _predict_prob(row: pd.Series) -> float:
    if not MODEL_PATH.is_file():
        return 0.5
    bundle = joblib.load(MODEL_PATH)
    model = bundle["pipeline"]
    features = bundle["feature_columns"]
    X = pd.DataFrame([{c: row[c] for c in features}])
    if hasattr(model, "predict_proba"):
        return float(model.predict_proba(X)[0][1])
    return 0.5


def build_snapshot() -> dict:
    fusion = pd.read_csv(DEFAULT_CSV)
    orbital = pd.read_csv(ORBITAL_CSV)
    ground = pd.read_csv(GROUND_CSV)
    talhoes = []
    alertas = []

    for talhao_id in fusion["talhao_id"].unique():
        sub = fusion[fusion["talhao_id"] == talhao_id].iloc[-1]
        orb = orbital[orbital["talhao_id"] == talhao_id].iloc[-1]
        gnd = ground[ground["talhao_id"] == talhao_id].iloc[-1]
        ndvi = float(orb["ndvi"])
        umidade = float(gnd["umidade_solo"])
        divergencia = explain_divergence(ndvi, umidade)
        prob = _predict_prob(sub)
        score = stress_fusion_score(ndvi, umidade, float(orb["precip_mm"]), prob)
        cat = categoria(score)
        entry = {
            "id": talhao_id,
            "cultura": str(sub["cultura"]),
            "stress_fusion": score,
            "categoria": cat,
            "orbital": {
                "ndvi": ndvi,
                "ndwi": float(orb["ndwi"]),
                "precip_mm": float(orb["precip_mm"]),
                "tile_url": "",
            },
            "terrestre": {
                "umidade_solo": umidade,
                "ph": float(gnd["ph"]),
                "fonte": str(gnd.get("fonte", "wokwi")),
            },
            "divergencia": divergencia,
            "recomendacao": recomendacao(score, str(sub["cultura"])),
        }
        talhoes.append(entry)
        if score >= 67:
            alertas.append(
                {
                    "tipo": "stress_hidrico",
                    "talhao_id": talhao_id,
                    "severidade": "alto",
                }
            )
        if divergencia["ativa"]:
            alertas.append(
                {
                    "tipo": "divergencia",
                    "talhao_id": talhao_id,
                    "severidade": "medio",
                    "mensagem": divergencia["resumo"],
                }
            )

    from datetime import datetime, timezone

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "talhoes": sorted(talhoes, key=lambda t: t["stress_fusion"], reverse=True),
        "alertas": alertas,
        "meta": {
            "sentinel_source": "cache",
            "wokwi_url": WOKWI_URL,
        },
        "feature_importance": _load_importance(),
    }


def _load_importance() -> list[dict[str, float]]:
    imp_path = MODEL_PATH.parent / "feature_importance.csv"
    if not imp_path.is_file():
        return []
    df = pd.read_csv(imp_path).head(8)
    return [
        {"feature": str(r["feature"]), "importance": float(r["importance"])}
        for _, r in df.iterrows()
    ]


def export_snapshot(path: Path | None = None) -> Path:
    out = path or SNAPSHOT_PATH
    out.parent.mkdir(parents=True, exist_ok=True)
    data = build_snapshot()
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[fusion] snapshot → {out}")
    return out


if __name__ == "__main__":
    export_snapshot()
