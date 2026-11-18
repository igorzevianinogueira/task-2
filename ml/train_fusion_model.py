#!/usr/bin/env python3
"""Treina Random Forest — fusão orbital + terrestre."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data" / "fusion_dataset.csv"
MODEL = BASE / "models" / "fusion_model.joblib"
METRICS = BASE / "models" / "fusion_metrics.json"
IMPORTANCE = BASE / "models" / "feature_importance.csv"

NUMERIC = ["ndvi", "ndwi", "precip_mm", "umidade_solo", "ph", "temperatura", "declividade"]
CATEGORICAL = ["cultura"]
TARGET = "stress_label"
FEATURES = NUMERIC + CATEGORICAL


def main() -> None:
    df = pd.read_csv(DATA)
    X = df[FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    preprocessor = ColumnTransformer(
        [
            ("num", "passthrough", NUMERIC),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), CATEGORICAL),
        ]
    )
    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        class_weight="balanced",
        random_state=42,
    )
    pipe = Pipeline([("prep", preprocessor), ("clf", clf)])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    metrics = {
        "recall": float(recall_score(y_test, pred, zero_division=0)),
        "f1": float(f1_score(y_test, pred, zero_division=0)),
        "trained_at": datetime.now(timezone.utc).isoformat(),
    }
    MODEL.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"pipeline": pipe, "feature_columns": FEATURES}, MODEL)
    METRICS.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    prep = pipe.named_steps["prep"]
    names = prep.get_feature_names_out()
    imp = pipe.named_steps["clf"].feature_importances_
    imp_df = pd.DataFrame({"feature": names, "importance": imp}).sort_values(
        "importance", ascending=False
    )
    imp_df.to_csv(IMPORTANCE, index=False)
    print(f"[ml] recall={metrics['recall']:.3f} f1={metrics['f1']:.3f}")
    print(f"[ml] modelo → {MODEL}")


if __name__ == "__main__":
    main()
