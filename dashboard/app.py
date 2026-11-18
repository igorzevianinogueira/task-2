"""TerraOps Fusion — Streamlit + Mission Control embed."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from embed_builder import build_standalone_html

TASK_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TASK_ROOT / "scripts"))
from paths import SNAPSHOT_PATH  # noqa: E402


def run_pipeline() -> None:
    subprocess.run(
        [sys.executable, str(TASK_ROOT / "scripts" / "run_pipeline.py")],
        cwd=TASK_ROOT,
        check=True,
    )


def load_snapshot_text() -> str:
    if not SNAPSHOT_PATH.is_file():
        return "{}"
    return SNAPSHOT_PATH.read_text(encoding="utf-8")




st.set_page_config(page_title="TerraOps Fusion", layout="wide")
st.title("TerraOps Fusion — Mission Control")

if "fusion_status" not in st.session_state:
    st.session_state.fusion_status = None

with st.sidebar:
    st.markdown("**Grupo 49** · GS 2026.1")
    if st.button("Executar fusão", type="primary"):
        st.session_state.fusion_status = None
        try:
            with st.spinner("Pipeline…"):
                run_pipeline()
            st.session_state.fusion_status = "ok"
        except subprocess.CalledProcessError as exc:
            st.session_state.fusion_status = f"erro: {exc}"
        st.rerun()

    if st.session_state.fusion_status == "ok":
        st.success("Fusão concluída.")
    elif st.session_state.fusion_status and st.session_state.fusion_status.startswith("erro:"):
        st.error(st.session_state.fusion_status.removeprefix("erro: "))

snapshot = load_snapshot_text()
try:
    meta = json.loads(snapshot)
    st.caption(f"Gerado: {meta.get('generated_at', '—')} · Talhões: {len(meta.get('talhoes', []))}")
except json.JSONDecodeError:
    st.warning("Snapshot ausente. Execute a fusão.")

try:
    snap_obj = json.loads(snapshot) if snapshot.strip() else {}
except json.JSONDecodeError:
    snap_obj = {}

if snap_obj.get("talhoes"):
    components.html(build_standalone_html(snap_obj), height=720, scrolling=True)
else:
    st.info("Execute a fusão na barra lateral para carregar o Mission Control.")
