"""Gera HTML standalone para iframe Streamlit."""

from __future__ import annotations

import json
from pathlib import Path

TASK_ROOT = Path(__file__).resolve().parent.parent
MC = Path(__file__).resolve().parent / "mission_control"


def build_standalone_html(snapshot: dict) -> str:
    css = (MC / "styles" / "tokens.css").read_text(encoding="utf-8")
    payload = json.dumps(snapshot, ensure_ascii=False)
    body = (MC / "index.html").read_text(encoding="utf-8")
    start = body.find('<header class="header">')
    end = body.find('<script type="module">')
    if start < 0 or end < 0:
        raise ValueError("Estrutura da Mission Control não reconhecida.")
    inner = body[start:end]
    script = f"""
<script>
const DATA = {payload};
function render(data) {{
  const top = (data.talhoes || [])[0];
  if (!top) {{
    document.getElementById("timeline").textContent = "Nenhuma leitura orbital. Execute a fusão.";
    return;
  }}
  document.getElementById("gen-time").textContent = data.generated_at || "—";
  document.getElementById("sentinel-src").textContent = (data.meta && data.meta.sentinel_source) || "cache";
  const score = top.stress_fusion;
  const el = document.getElementById("sf-score");
  const bar = document.getElementById("sf-bar");
  el.textContent = score;
  bar.style.width = score + "%";
  document.getElementById("sf-rec").textContent = top.recomendacao || "—";
  const rank = document.getElementById("rank-list");
  rank.innerHTML = "";
  (data.talhoes || []).forEach((t, i) => {{
    const d = document.createElement("div");
    d.className = "ranking-item";
    d.innerHTML = "<span>" + (i+1) + ". " + t.id + " " + t.cultura + "</span><strong>" + t.stress_fusion + "</strong>";
    rank.appendChild(d);
  }});
  const orb = Math.round((top.orbital.ndvi || 0) * 100);
  const soil = Math.round(top.terrestre.umidade_solo || 0);
  document.getElementById("orb-bar").style.width = orb + "%";
  document.getElementById("soil-bar").style.width = soil + "%";
  document.getElementById("orb-val").textContent = orb + "%";
  document.getElementById("soil-val").textContent = soil + "%";
  const div = top.divergencia || {{}};
  const deltaLabel = div.ativa
    ? div.delta_ndvi_umidade + " (limiar " + div.limiar + ")"
    : String(div.delta_ndvi_umidade ?? "—");
  document.getElementById("div-delta").textContent = deltaLabel;
  const explainEl = document.getElementById("div-explain");
  if (explainEl && div.resumo) {{
    explainEl.hidden = false;
    document.getElementById("div-resumo").textContent = div.resumo;
    document.getElementById("div-chain").textContent = div.explicacao || "";
    const hipList = document.getElementById("div-hipoteses");
    hipList.innerHTML = "";
    (div.hipoteses || []).forEach(h => {{
      const li = document.createElement("li");
      li.textContent = h;
      hipList.appendChild(li);
    }});
    document.getElementById("div-acao").textContent = div.acao_sugerida ? "→ " + div.acao_sugerida : "";
    if (div.ativa) document.getElementById("zone-cal").classList.add("divergence-active");
  }}
  document.getElementById("timeline").textContent = (data.alertas || []).map(a => a.mensagem ? a.talhao_id + ": " + a.mensagem : a.tipo + " " + a.talhao_id).join(" · ") || "Sem alertas";
}}
render(DATA);
</script>
"""
    return f"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'><style>{css}</style></head><body>{inner}{script}</body></html>"
