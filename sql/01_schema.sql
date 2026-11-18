-- TerraOps Fusion — schema fusão (idempotente)

CREATE TABLE IF NOT EXISTS orbital_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talhao_id TEXT NOT NULL,
    ndvi REAL,
    ndwi REAL,
    precip_mm REAL,
    captured_at TEXT,
    fonte TEXT
);

CREATE TABLE IF NOT EXISTS ground_truth (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talhao_id TEXT NOT NULL,
    umidade_solo REAL,
    ph REAL,
    fonte TEXT,
    captured_at TEXT
);

CREATE TABLE IF NOT EXISTS fused_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talhao_id TEXT NOT NULL,
    stress_fusion INTEGER,
    categoria TEXT,
    divergencia_ativa INTEGER,
    captured_at TEXT
);
