import {
  animateZonesIn,
  animateScore,
  pulseAlert,
  staggerRanking,
} from "./anime-motion.js";

let state = null;

function fmtTime(iso) {
  if (!iso) return "—";
  try {
    return new Date(iso).toLocaleString("pt-BR");
  } catch {
    return iso;
  }
}

function renderEmpty(msg) {
  document.getElementById("app-root").innerHTML = `<p class="empty">${msg}</p>`;
}

function render(data) {
  state = data;
  const top = data.talhoes?.[0];
  if (!top) {
    renderEmpty("Nenhuma leitura orbital. Execute a fusão para carregar talhões.");
    return;
  }

  document.getElementById("gen-time").textContent = fmtTime(data.generated_at);
  document.getElementById("sentinel-src").textContent =
    data.meta?.sentinel_source || "cache";

  animateScore(top.stress_fusion, document.getElementById("sf-score"), document.getElementById("sf-bar"));
  document.getElementById("sf-rec").textContent = top.recomendacao || "—";
  const alertEl = document.getElementById("sf-alert");
  const hasAlert = data.alertas?.some((a) => a.talhao_id === top.id);
  alertEl.hidden = !hasAlert;
  if (hasAlert) {
    alertEl.textContent = `Alerta ativo em ${top.id}`;
    pulseAlert(alertEl);
  }

  const rank = document.getElementById("rank-list");
  rank.innerHTML = "";
  data.talhoes.forEach((t, i) => {
    const li = document.createElement("div");
    li.className = "ranking-item";
    li.innerHTML = `<span>${i + 1}. ${t.id} ${t.cultura}</span><strong>${t.stress_fusion}</strong>`;
    rank.appendChild(li);
  });
  staggerRanking(rank.querySelectorAll(".ranking-item"));

  const orbPct = Math.round((top.orbital?.ndvi || 0) * 100);
  const soilPct = Math.round(top.terrestre?.umidade_solo || 0);
  document.getElementById("orb-bar").style.width = `${orbPct}%`;
  document.getElementById("soil-bar").style.width = `${soilPct}%`;
  document.getElementById("orb-val").textContent = `${orbPct}%`;
  document.getElementById("soil-val").textContent = `${soilPct}%`;
  const div = top.divergencia || {};
  const deltaLabel = div.ativa
    ? `${div.delta_ndvi_umidade} (limiar ${div.limiar})`
    : String(div.delta_ndvi_umidade ?? "—");
  document.getElementById("div-delta").textContent = deltaLabel;

  const explainEl = document.getElementById("div-explain");
  const hasExplain = Boolean(div.resumo);
  explainEl.hidden = !hasExplain;
  if (hasExplain) {
    document.getElementById("div-resumo").textContent = div.resumo;
    document.getElementById("div-chain").textContent = div.explicacao || "";
    const hipList = document.getElementById("div-hipoteses");
    hipList.innerHTML = "";
    (div.hipoteses || []).forEach((h) => {
      const li = document.createElement("li");
      li.textContent = h;
      hipList.appendChild(li);
    });
    document.getElementById("div-acao").textContent = div.acao_sugerida
      ? `→ ${div.acao_sugerida}`
      : "";
  }

  const calZone = document.getElementById("zone-cal");
  if (div.ativa) calZone.classList.add("divergence-active");
  else calZone.classList.remove("divergence-active");

  const imp = document.getElementById("imp-list");
  imp.innerHTML = "";
  (data.feature_importance || []).slice(0, 5).forEach((f) => {
    const row = document.createElement("div");
    row.className = "bar-row";
    row.innerHTML = `<div class="bar-label"><span>${f.feature}</span><span>${(f.importance * 100).toFixed(1)}%</span></div>`;
    imp.appendChild(row);
  });

  const tl = document.getElementById("timeline");
  tl.textContent =
    (data.alertas || [])
      .map((a) => (a.mensagem ? `${a.talhao_id}: ${a.mensagem}` : `${a.tipo} ${a.talhao_id}`))
      .join(" · ") || "Sem alertas ativos";
}

export function loadSnapshot(json) {
  try {
    const data = typeof json === "string" ? JSON.parse(json) : json;
    render(data);
    animateZonesIn();
  } catch (e) {
    renderEmpty("Snapshot inválido.");
    console.error(e);
  }
}

window.addEventListener("message", (ev) => {
  if (ev.data?.type === "terraops-snapshot") loadSnapshot(ev.data.payload);
});

window.TerraOpsApp = { loadSnapshot };
