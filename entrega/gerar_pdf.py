#!/usr/bin/env python3
"""Gera o relatório final da Global Solution a partir dos artefatos reais."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import pandas as pd
from fpdf import FPDF


DELIVERY_DIR = Path(__file__).resolve().parent
PROJECT_DIR = DELIVERY_DIR.parent
OUTPUT = DELIVERY_DIR / "GlobalSolution_Grupo49.pdf"

FONT_REGULAR = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
FONT_BOLD = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
FONT_MONO = Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")

REPO_URL_FILE = DELIVERY_DIR / "repo_url.txt"


def load_repository_url() -> tuple[str, bool]:
    """URL do repo de ENTREGA (nunca fiap-academic-workflow)."""
    if not REPO_URL_FILE.is_file():
        return "", False
    first = REPO_URL_FILE.read_text(encoding="utf-8").splitlines()[0].strip()
    ready = first.startswith("http") and "SUBSTITUIR" not in first.upper()
    ready = ready and "fiap-academic-workflow" not in first.lower()
    return first, ready

NAVY = (10, 22, 38)
NAVY_2 = (17, 35, 57)
TEAL = (24, 180, 168)
TEAL_DARK = (13, 119, 112)
OCHRE = (210, 148, 57)
VIOLET = (129, 104, 219)
AMBER = (235, 170, 45)
RED = (191, 56, 65)
GREEN = (32, 143, 102)
INK = (31, 42, 55)
MUTED = (91, 104, 119)
LINE = (215, 222, 230)
LIGHT = (244, 247, 250)
WHITE = (255, 255, 255)


def load_project_data() -> dict:
    snapshot_path = PROJECT_DIR / "data" / "snapshot.json"
    metrics_path = PROJECT_DIR / "models" / "fusion_metrics.json"
    importance_path = PROJECT_DIR / "models" / "feature_importance.csv"
    dataset_path = PROJECT_DIR / "data" / "fusion_dataset.csv"
    video_path = PROJECT_DIR / "link_video.txt"

    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    importance = pd.read_csv(importance_path).head(6)
    dataset = pd.read_csv(dataset_path)

    video_url = ""
    if video_path.is_file():
        video_url = video_path.read_text(encoding="utf-8").splitlines()[0].strip()

    repository_url, repo_ready = load_repository_url()

    return {
        "snapshot": snapshot,
        "metrics": metrics,
        "importance": importance,
        "dataset": dataset,
        "video_url": video_url,
        "video_ready": video_url.startswith("http")
        and "SUBSTITUIR" not in video_url.upper(),
        "repository_url": repository_url,
        "repo_ready": repo_ready,
        "correlation": float(dataset["ndvi"].corr(dataset["umidade_solo"] / 100)),
    }


class ReportPDF(FPDF):
    def __init__(self) -> None:
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(16, 17, 16)
        self.set_auto_page_break(auto=True, margin=16)
        self.add_font("DejaVu", "", str(FONT_REGULAR))
        self.add_font("DejaVu", "B", str(FONT_BOLD))
        self.add_font("DejaVuMono", "", str(FONT_MONO))
        self.set_title("TerraOps Fusion - Global Solution 2026.1")
        self.set_author("Grupo 49 - FIAP 1TIAOA")
        self.set_subject("POC de observação da Terra com fusão orbital, IoT e ML")
        self.alias_nb_pages()

    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_fill_color(*NAVY)
        self.rect(0, 0, self.w, 10, "F")
        self.set_xy(16, 3)
        self.set_font("DejaVu", "B", 7.5)
        self.set_text_color(*WHITE)
        self.cell(0, 4, "TERRAOPS FUSION  |  GLOBAL SOLUTION 2026.1", align="L")
        self.set_xy(-55, 3)
        self.set_font("DejaVu", "", 7.5)
        self.cell(39, 4, "Grupo 49 · 1TIAOA", align="R")
        self.set_xy(self.l_margin, self.t_margin)

    def footer(self) -> None:
        if self.page_no() == 1:
            return
        self.set_y(-11)
        self.set_draw_color(*LINE)
        self.line(16, self.get_y(), self.w - 16, self.get_y())
        self.set_y(-9)
        self.set_font("DejaVu", "", 7.5)
        self.set_text_color(*MUTED)
        self.cell(0, 5, f"Página {self.page_no()} de {{nb}}", align="R")

    def ensure_space(self, height: float) -> None:
        if self.get_y() + height > self.h - 17:
            self.add_page()

    def section_title(self, number: str, title: str, subtitle: str = "") -> None:
        self.set_text_color(*TEAL_DARK)
        self.set_font("DejaVu", "B", 9)
        self.cell(0, 5, number.upper())
        self.ln(5)
        self.set_text_color(*NAVY)
        self.set_font("DejaVu", "B", 20)
        self.multi_cell(0, 9, title, new_x="LMARGIN", new_y="NEXT")
        if subtitle:
            self.set_text_color(*MUTED)
            self.set_font("DejaVu", "", 9.5)
            self.multi_cell(0, 5, subtitle, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*TEAL)
        self.set_line_width(0.8)
        self.line(16, self.get_y() + 2, 48, self.get_y() + 2)
        self.ln(7)

    def heading(self, text: str) -> None:
        self.ensure_space(13)
        self.set_font("DejaVu", "B", 12)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

    def paragraph(self, text: str, *, size: float = 9.4, leading: float = 5.1) -> None:
        self.set_font("DejaVu", "", size)
        self.set_text_color(*INK)
        self.multi_cell(0, leading, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

    def bullet(self, text: str, color: tuple[int, int, int] = TEAL_DARK) -> None:
        self.ensure_space(8)
        x = self.get_x()
        y = self.get_y() + 1.6
        self.set_fill_color(*color)
        self.ellipse(x, y, 2.2, 2.2, "F")
        self.set_xy(x + 5, self.get_y())
        self.set_font("DejaVu", "", 9.1)
        self.set_text_color(*INK)
        self.multi_cell(self.epw - 5, 4.8, text)
        self.ln(0.7)

    def callout(
        self,
        label: str,
        text: str,
        *,
        accent: tuple[int, int, int] = TEAL,
        fill: tuple[int, int, int] = LIGHT,
        height: float = 25,
    ) -> None:
        self.ensure_space(height + 3)
        x, y = self.get_x(), self.get_y()
        self.set_fill_color(*fill)
        self.set_draw_color(*LINE)
        self.rect(x, y, self.epw, height, "DF")
        self.set_fill_color(*accent)
        self.rect(x, y, 3, height, "F")
        self.set_xy(x + 7, y + 4)
        self.set_font("DejaVu", "B", 8)
        self.set_text_color(*accent)
        self.cell(self.epw - 12, 4, label.upper())
        self.set_xy(x + 7, y + 9)
        self.set_font("DejaVu", "", 9.1)
        self.set_text_color(*INK)
        self.multi_cell(self.epw - 12, 4.8, text)
        self.set_y(y + height + 3)

    def metric_cards(self, cards: list[tuple[str, str, tuple[int, int, int]]]) -> None:
        self.ensure_space(27)
        gap = 3
        width = (self.epw - gap * (len(cards) - 1)) / len(cards)
        x0, y0 = self.get_x(), self.get_y()
        for index, (value, label, accent) in enumerate(cards):
            x = x0 + index * (width + gap)
            self.set_fill_color(*LIGHT)
            self.set_draw_color(*LINE)
            self.rect(x, y0, width, 23, "DF")
            self.set_fill_color(*accent)
            self.rect(x, y0, width, 2.2, "F")
            self.set_xy(x + 2, y0 + 5)
            self.set_font("DejaVu", "B", 15)
            self.set_text_color(*NAVY)
            self.cell(width - 4, 7, value, align="C")
            self.set_xy(x + 2, y0 + 14)
            self.set_font("DejaVu", "", 7.3)
            self.set_text_color(*MUTED)
            self.cell(width - 4, 5, label, align="C")
        self.set_y(y0 + 27)

    def code_block(self, code: str, *, font_size: float = 7.3) -> None:
        lines = code.rstrip().splitlines()
        line_height = 3.9
        height = len(lines) * line_height + 7
        self.ensure_space(min(height, 75))
        x, y = self.get_x(), self.get_y()
        self.set_fill_color(22, 31, 45)
        self.rect(x, y, self.epw, height, "F")
        self.set_xy(x + 4, y + 3)
        self.set_font("DejaVuMono", "", font_size)
        self.set_text_color(226, 232, 240)
        for line in lines:
            self.cell(self.epw - 8, line_height, line)
            self.ln(line_height)
            self.set_x(x + 4)
        self.set_y(y + height + 3)

    def simple_table(
        self,
        headers: list[str],
        rows: list[list[str]],
        widths: list[float],
        *,
        font_size: float = 7.7,
        row_height: float = 7.2,
    ) -> None:
        total_height = (len(rows) + 1) * row_height + 2
        self.ensure_space(total_height)
        x0 = self.get_x()
        self.set_font("DejaVu", "B", font_size)
        self.set_text_color(*WHITE)
        self.set_fill_color(*NAVY_2)
        self.set_draw_color(*LINE)
        for header, width in zip(headers, widths):
            self.cell(width, row_height, header, border=1, fill=True)
        self.ln(row_height)
        for row_index, row in enumerate(rows):
            self.set_x(x0)
            self.set_font("DejaVu", "", font_size)
            self.set_text_color(*INK)
            self.set_fill_color(*(WHITE if row_index % 2 == 0 else LIGHT))
            for value, width in zip(row, widths):
                self.cell(width, row_height, str(value), border=1, fill=True)
            self.ln(row_height)
        self.ln(3)

    def horizontal_bars(
        self,
        items: list[tuple[str, float, str]],
        *,
        max_value: float,
        title: str,
        value_suffix: str = "",
        accent: tuple[int, int, int] = TEAL,
    ) -> None:
        height = 11 + len(items) * 8
        self.ensure_space(height)
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(*NAVY)
        self.cell(0, 6, title)
        self.ln(8)
        label_width = 32
        bar_width = self.epw - label_width - 18
        for label, value, display in items:
            y = self.get_y()
            self.set_font("DejaVu", "", 7.7)
            self.set_text_color(*INK)
            self.cell(label_width, 5, label)
            self.set_fill_color(*LINE)
            self.rect(self.get_x(), y + 1, bar_width, 3.4, "F")
            filled = max(0, min(bar_width, bar_width * value / max_value))
            self.set_fill_color(*accent)
            self.rect(self.get_x(), y + 1, filled, 3.4, "F")
            self.set_xy(16 + label_width + bar_width + 2, y)
            self.set_font("DejaVu", "B", 7.7)
            self.cell(16, 5, f"{display}{value_suffix}", align="R")
            self.set_y(y + 8)
        self.ln(2)

    def link_line(self, label: str, url: str, *, warning: bool = False) -> None:
        self.ensure_space(16)
        self.set_font("DejaVu", "B", 9)
        self.set_text_color(*(RED if warning else NAVY))
        self.cell(0, 5, label)
        self.ln(5)
        self.set_font("DejaVu", "", 8.3)
        self.set_text_color(*(RED if warning else TEAL_DARK))
        self.multi_cell(
            0,
            4.8,
            url,
            link="" if warning else url,
            new_x="LMARGIN",
            new_y="NEXT",
        )
        self.ln(2)


def add_cover(pdf: ReportPDF) -> None:
    pdf.add_page()
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, pdf.w, pdf.h, "F")
    pdf.set_fill_color(*TEAL)
    pdf.rect(0, 0, 8, pdf.h, "F")

    pdf.set_xy(22, 24)
    pdf.set_font("DejaVu", "B", 9)
    pdf.set_text_color(*TEAL)
    pdf.cell(0, 6, "FIAP · GLOBAL SOLUTION 2026.1 · ECONOMIA ESPACIAL")

    pdf.set_xy(22, 49)
    pdf.set_font("DejaVu", "B", 31)
    pdf.set_text_color(*WHITE)
    pdf.multi_cell(165, 13, "TerraOps\nFusion")

    pdf.set_xy(22, 83)
    pdf.set_font("DejaVu", "", 13)
    pdf.set_text_color(196, 211, 226)
    pdf.multi_cell(
        158,
        7,
        "Centro de comando de observação da Terra para fusão de dados "
        "orbitais, sensores locais e Machine Learning.",
    )

    pdf.set_xy(22, 117)
    pdf.set_fill_color(*NAVY_2)
    pdf.set_draw_color(48, 70, 93)
    pdf.rect(22, 117, 166, 37, "DF")
    pdf.set_xy(28, 123)
    pdf.set_font("DejaVu", "B", 8)
    pdf.set_text_color(*OCHRE)
    pdf.cell(0, 5, "PROVA DE CONCEITO FUNCIONAL")
    pdf.set_xy(28, 130)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(*WHITE)
    pdf.multi_cell(
        151,
        5.6,
        "Satélite + solo → StressFusion 0–100 → prioridade operacional "
        "e explicação de divergências por talhão.",
    )

    pdf.set_xy(22, 174)
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_text_color(*TEAL)
    pdf.cell(0, 6, "GRUPO 49 · TURMA 1TIAOA")
    members = [
        "Higor Henrique Garcia — RM 571820",
        "Vinicius Alves Lopes dos Anjos — RM 572814",
        "Igor Zeviani Nogueira — RM 572822",
        "Humberto Salim — RM 570536",
    ]
    pdf.set_xy(22, 184)
    pdf.set_font("DejaVu", "", 9.5)
    pdf.set_text_color(*WHITE)
    for member in members:
        pdf.cell(0, 6, member)
        pdf.ln(6)
        pdf.set_x(22)

    pdf.set_xy(22, 251)
    pdf.set_font("DejaVu", "", 8)
    pdf.set_text_color(165, 184, 204)
    pdf.cell(0, 5, "Relatório técnico e demonstrativo · 09 de junho de 2026")


def add_problem_and_solution(pdf: ReportPDF) -> None:
    pdf.add_page()
    pdf.section_title(
        "01 · Introdução",
        "Do dado isolado à decisão operacional",
        "Uma POC aplicada à agricultura baseada em sensoriamento orbital.",
    )
    pdf.callout(
        "Pergunta do desafio",
        "Como a tecnologia espacial pode melhorar a vida das pessoas, tornar "
        "processos mais eficientes e criar novas oportunidades na Terra?",
        accent=VIOLET,
        height=25,
    )
    pdf.heading("Problema")
    pdf.paragraph(
        "Decisões de irrigação e operação agrícola costumam combinar mapas "
        "orbitais, planilhas e sensores locais de forma fragmentada. O satélite "
        "oferece escala, mas pode ter atraso temporal ou interferência de nuvens; "
        "o sensor de solo oferece precisão local, mas não representa sozinho todo "
        "o talhão."
    )
    pdf.heading("Proposta")
    pdf.paragraph(
        "O TerraOps Fusion cruza NDVI, NDWI e precipitação da camada orbital "
        "com umidade e pH da camada terrestre. O motor produz o índice "
        "StressFusion de 0 a 100, classifica a prioridade e explica quando as "
        "fontes divergem. O resultado é publicado em um snapshot JSON consumido "
        "pelo Mission Control."
    )
    pdf.callout(
        "Hipótese",
        "A combinação de evidências orbitais, ground-truth IoT e probabilidade "
        "de ML gera uma triagem mais explicável do que qualquer fonte isolada.",
        accent=TEAL,
        height=25,
    )
    pdf.heading("Aplicabilidade")
    pdf.bullet("Operador: verifica se pode agir no campo naquele momento.")
    pdf.bullet("Gestora: prioriza talhões e recursos com base no ranking de stress.")
    pdf.bullet(
        "Agrônoma ou analista: investiga por que satélite e sensor local discordam."
    )
    pdf.heading("Escopo da POC")
    pdf.paragraph(
        "A demonstração cobre agricultura com café, soja e milho. A mesma "
        "arquitetura pode evoluir para monitoramento geoambiental, geologia, "
        "desastres e outros usos de observação da Terra."
    )


def add_architecture(pdf: ReportPDF) -> None:
    pdf.add_page()
    pdf.section_title(
        "02 · Desenvolvimento",
        "Arquitetura integrada e interdisciplinar",
        "Fluxo executável da coleta simulada até a decisão no Mission Control.",
    )

    x0, y0 = 18, pdf.get_y()
    box_w, box_h, gap = 39, 24, 6
    boxes = [
        ("CAMADA\nORBITAL", "NDVI · NDWI\nprecipitação", VIOLET),
        ("CAMADA\nTERRESTRE", "umidade · pH\nESP32/Wokwi", OCHRE),
        ("FUSION\nENGINE", "Pandas · regras\nRandom Forest", TEAL),
        ("MISSION\nCONTROL", "ranking · alertas\nrecomendação", AMBER),
    ]
    for index, (title, detail, color) in enumerate(boxes):
        x = x0 + index * (box_w + gap)
        pdf.set_fill_color(*LIGHT)
        pdf.set_draw_color(*color)
        pdf.set_line_width(0.7)
        pdf.rect(x, y0, box_w, box_h, "DF")
        pdf.set_xy(x + 2, y0 + 3)
        pdf.set_font("DejaVu", "B", 8)
        pdf.set_text_color(*color)
        pdf.multi_cell(box_w - 4, 4, title, align="C")
        pdf.set_xy(x + 2, y0 + 13)
        pdf.set_font("DejaVu", "", 6.9)
        pdf.set_text_color(*INK)
        pdf.multi_cell(box_w - 4, 3.5, detail, align="C")
        if index < len(boxes) - 1:
            arrow_x = x + box_w + 1
            pdf.set_draw_color(*MUTED)
            pdf.line(arrow_x, y0 + 12, arrow_x + gap - 2, y0 + 12)
            pdf.line(arrow_x + gap - 4, y0 + 10, arrow_x + gap - 2, y0 + 12)
            pdf.line(arrow_x + gap - 4, y0 + 14, arrow_x + gap - 2, y0 + 12)
    pdf.set_y(y0 + 31)

    pdf.callout(
        "Contrato de integração",
        "CSV orbital + CSV terrestre → fusion_dataset.csv → modelo treinado → "
        "snapshot.json → Streamlit e interface Mission Control.",
        accent=TEAL,
        height=23,
    )

    pdf.heading("Disciplinas mobilizadas")
    rows = [
        ["Python", "pipeline, condicionais, laços e automação"],
        ["Pandas / Dados", "ingestão, limpeza, fusão e métricas"],
        ["Machine Learning", "Random Forest para probabilidade de stress"],
        ["Estatística", "correlação, F1, recall e importância"],
        ["Banco de Dados", "SQLite, schema e cinco consultas SQL"],
        ["IoT", "ground-truth de umidade e pH via ESP32/Wokwi"],
        ["Visualização", "Mission Control, ranking e alertas"],
        ["Formação Social", "dados fictícios, privacidade e limites de uso"],
    ]
    pdf.simple_table(["Disciplina", "Evidência na POC"], rows, [42, 136])

    pdf.heading("Organização técnica")
    pdf.paragraph(
        "O projeto separa scripts, dados, modelo, SQL, IoT, dashboard e "
        "documentação. O comando scripts/run_pipeline.py regenera todos os "
        "artefatos e mantém a demonstração reproduzível."
    )


def add_technical_core(pdf: ReportPDF) -> None:
    pdf.add_page()
    pdf.section_title(
        "03 · Desenvolvimento",
        "Núcleo Python e fórmula StressFusion",
        "Código apresentado como texto, com estruturas exigidas no enunciado.",
    )
    pdf.callout(
        "Fórmula",
        "StressFusion = clamp(0,4 × stress orbital + 0,35 × stress do solo "
        "+ P(stress alto) × 30 + penalidade de divergência, 0, 100).",
        accent=VIOLET,
        height=25,
    )
    pdf.heading("Trecho principal")
    pdf.code_block(
        """fusion = pd.read_csv(DEFAULT_CSV)
orbital = pd.read_csv(ORBITAL_CSV)
ground = pd.read_csv(GROUND_CSV)

for talhao_id in fusion["talhao_id"].unique():
    sub = fusion[fusion["talhao_id"] == talhao_id].iloc[-1]
    orb = orbital[orbital["talhao_id"] == talhao_id].iloc[-1]
    gnd = ground[ground["talhao_id"] == talhao_id].iloc[-1]

    divergencia = explain_divergence(
        float(orb["ndvi"]), float(gnd["umidade_solo"])
    )
    prob = _predict_prob(sub)
    score = stress_fusion_score(
        float(orb["ndvi"]),
        float(gnd["umidade_solo"]),
        float(orb["precip_mm"]),
        prob,
    )

    if score >= 67:
        alertas.append({"talhao_id": talhao_id, "severidade": "alto"})"""
    )
    pdf.heading("Decisões da solução")
    pdf.bullet(
        "Laço por talhão: processa várias culturas sem duplicar lógica."
    )
    pdf.bullet(
        "Condicionais: convertem o score em baixo, médio ou alto e geram alertas."
    )
    pdf.bullet(
        "Manipulação de dados: Pandas combina fontes heterogêneas por talhao_id."
    )
    pdf.bullet(
        "Explicabilidade: delta superior a 0,15 registra hipótese e ação sugerida."
    )
    pdf.bullet(
        "Contingência: dados orbitais em cache e dataset sintético com seed 42."
    )
    pdf.heading("Limites assumidos")
    pdf.paragraph(
        "A fórmula e o modelo são introdutórios e demonstrativos. O índice não "
        "substitui diagnóstico agronômico, calibração de sensores ou validação "
        "com dados reais de safra."
    )


def add_data_and_ml(pdf: ReportPDF, data: dict) -> None:
    dataset = data["dataset"]
    metrics = data["metrics"]
    importance = data["importance"]
    pdf.add_page()
    pdf.section_title(
        "04 · Desenvolvimento",
        "Dados, Machine Learning, IoT e SQL",
        "Implementações reais conectadas pelo mesmo pipeline.",
    )
    pdf.metric_cards(
        [
            (str(len(dataset)), "registros simulados", TEAL),
            (str(dataset["talhao_id"].nunique()), "talhões monitorados", OCHRE),
            (str(dataset["cultura"].nunique()), "culturas", VIOLET),
            (f"{metrics['f1']:.2f}", "F1 do modelo", AMBER),
        ]
    )

    items = []
    feature_labels = {
        "num__ndvi": "NDVI",
        "num__umidade_solo": "Umidade do solo",
        "num__ndwi": "NDWI",
        "num__declividade": "Declividade",
        "num__temperatura": "Temperatura",
        "num__precip_mm": "Precipitação",
    }
    for _, row in importance.iterrows():
        value = float(row["importance"])
        items.append(
            (
                feature_labels.get(str(row["feature"]), str(row["feature"])),
                value,
                f"{value * 100:.1f}",
            )
        )
    pdf.horizontal_bars(
        items,
        max_value=max(value for _, value, _ in items),
        title="Importância das variáveis no Random Forest",
        value_suffix="%",
        accent=VIOLET,
    )

    pdf.callout(
        "Leitura responsável das métricas",
        f"Recall = {metrics['recall']:.2f} e F1 = {metrics['f1']:.2f}. "
        "O modelo comprova integração técnica, mas ainda requer mais dados e "
        "validação externa antes de orientar decisões reais.",
        accent=AMBER,
        height=28,
    )

    pdf.heading("Camada IoT")
    pdf.paragraph(
        "A camada terrestre representa leituras de umidade e pH de um ESP32 no "
        "Wokwi. O pipeline exporta ground_truth.csv e registra a fonte no "
        "snapshot. A simulação permite repetir a POC sem depender de hardware "
        "físico durante a avaliação."
    )
    pdf.heading("Persistência e consultas")
    pdf.code_block(
        """SELECT talhao_id, stress_fusion, categoria
FROM fused_scores
ORDER BY stress_fusion DESC
LIMIT 3;

SELECT talhao_id, stress_fusion
FROM fused_scores
WHERE divergencia_ativa = 1;""",
        font_size=7.6,
    )


def add_results(pdf: ReportPDF, data: dict) -> None:
    snapshot = data["snapshot"]
    talhoes = snapshot["talhoes"]
    divergences = [item for item in talhoes if item["divergencia"]["ativa"]]
    pdf.add_page()
    pdf.section_title(
        "05 · Resultados esperados e obtidos",
        "Snapshot reproduzível e decisão explicável",
        "Resultados da execução local mais recente do pipeline.",
    )
    pdf.metric_cards(
        [
            (str(len(talhoes)), "talhões no snapshot", TEAL),
            (str(len(divergences)), "divergências ativas", RED),
            (str(len(snapshot.get("alertas", []))), "alertas gerados", AMBER),
            (f"{data['correlation']:.3f}", "correlação NDVI × solo", VIOLET),
        ]
    )

    stress_items = [
        (
            f"{item['id']} · {item['cultura']}",
            float(item["stress_fusion"]),
            str(item["stress_fusion"]),
        )
        for item in talhoes
    ]
    pdf.horizontal_bars(
        stress_items,
        max_value=100,
        title="Ranking StressFusion por talhão",
        value_suffix="/100",
        accent=TEAL,
    )

    rows = []
    for item in talhoes:
        rows.append(
            [
                item["id"],
                item["cultura"],
                str(item["stress_fusion"]),
                item["categoria"],
                "sim" if item["divergencia"]["ativa"] else "não",
            ]
        )
    pdf.simple_table(
        ["Talhão", "Cultura", "Stress", "Categoria", "Divergência"],
        rows,
        [29, 42, 30, 40, 37],
        font_size=7.5,
    )

    pdf.heading("Exemplo de explicação gerada")
    if divergences:
        example = divergences[0]
        divergence = example["divergencia"]
        pdf.callout(
            f"{example['id']} · {divergence['tipo']}",
            divergence["resumo"] + " Ação sugerida: " + divergence["acao_sugerida"],
            accent=RED,
            fill=(252, 244, 244),
            height=34,
        )

    pdf.heading("Interpretação")
    pdf.paragraph(
        "A correlação linear global entre NDVI e umidade foi próxima de zero "
        "neste conjunto sintético. Isso impede uma conclusão causal e reforça a "
        "necessidade de analisar cada talhão com contexto, divergência e fontes "
        "complementares, em vez de usar uma correlação isolada."
    )


def add_operation_and_conclusion(pdf: ReportPDF, data: dict) -> None:
    pdf.add_page()
    pdf.section_title(
        "06 · Conclusões",
        "Reprodutibilidade, colaboração e próximos passos",
        "Como avaliar a POC e quais limites permanecem.",
    )
    pdf.heading("Execução básica")
    pdf.code_block(
        """cd tasks/task10_global_solution
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_pipeline.py
streamlit run dashboard/app.py"""
    )
    pdf.heading("Trabalho colaborativo")
    collaboration_rows = [
        ["Higor", "PO, trunk, pipeline, snapshot e roteiro"],
        ["Vinicius", "Machine Learning, métricas e análise"],
        ["Igor", "Mission Control e visualização"],
        ["Humberto", "integração, documentação e entrega"],
    ]
    pdf.simple_table(
        ["Integrante", "Responsabilidade principal"],
        collaboration_rows,
        [42, 136],
        font_size=7.7,
    )

    pdf.heading("LGPD e uso responsável")
    pdf.bullet("Talhões, coordenadas e leituras são fictícios e reproduzíveis.")
    pdf.bullet("Não há dados pessoais de terceiros no dataset da demonstração.")
    pdf.bullet(
        "Recomendações são apoio à decisão e não substituem profissional habilitado."
    )

    pdf.heading("Conclusão")
    pdf.paragraph(
        "O TerraOps Fusion demonstra uma cadeia completa: ingestão de dados "
        "orbitais e terrestres, manipulação com Pandas, classificação por "
        "Machine Learning, persistência SQL e comunicação visual. A POC torna "
        "explícita a divergência entre fontes e converte dados técnicos em uma "
        "recomendação operacional rastreável."
    )
    pdf.callout(
        "Próximos passos",
        "Validar com séries temporais reais, calibrar pesos por cultura, conectar "
        "uma API orbital ao vivo e medir redução de água, deslocamentos e horas "
        "de máquina em um piloto de campo.",
        accent=GREEN,
        height=28,
    )

    pdf.heading("Links obrigatórios")
    if data["repo_ready"]:
        pdf.link_line("Repositório do projeto", data["repository_url"])
    else:
        pdf.link_line(
            "ATENÇÃO: link do repositório de entrega ainda precisa ser configurado",
            data["repository_url"] or "repo_url.txt não preenchido",
            warning=True,
        )
    if data["video_ready"]:
        pdf.link_line("Vídeo demonstrativo no YouTube (não listado)", data["video_url"])
    else:
        pdf.link_line(
            "ATENÇÃO: link do vídeo ainda precisa ser substituído antes do envio",
            data["video_url"] or "link não informado",
            warning=True,
        )


def build_pdf() -> tuple[Path, bool]:
    data = load_project_data()
    pdf = ReportPDF()
    add_cover(pdf)
    add_problem_and_solution(pdf)
    add_architecture(pdf)
    add_technical_core(pdf)
    add_data_and_ml(pdf, data)
    add_results(pdf, data)
    add_operation_and_conclusion(pdf, data)
    pdf.output(str(OUTPUT))
    return OUTPUT, data["video_ready"], data["repo_ready"]


def main() -> None:
    output, video_ready, repo_ready = build_pdf()
    print(f"PDF gerado: {output}")
    print(f"Tamanho: {output.stat().st_size:,} bytes")
    print(f"Horário: {datetime.now().astimezone().isoformat(timespec='seconds')}")
    if not video_ready:
        print(
            "ALERTA: o PDF foi gerado, mas o link do vídeo continua pendente. "
            "Atualize link_video.txt e execute este script novamente antes do upload."
        )
    if not repo_ready:
        print(
            "ALERTA: use repo de ENTREGA (template TIAO), nunca fiap-academic-workflow. "
            "Preencha entrega/repo_url.txt e regenere o PDF."
        )


if __name__ == "__main__":
    main()
