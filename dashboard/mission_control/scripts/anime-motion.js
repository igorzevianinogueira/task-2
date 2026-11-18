/** Anime.js motion — TerraOps Mission Control */

function prefersReducedMotion() {
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

export function animateZonesIn() {
  if (prefersReducedMotion() || typeof anime === "undefined") return;
  anime({
    targets: ".zone",
    opacity: [0, 1],
    translateY: [16, 0],
    delay: anime.stagger(120),
    duration: 500,
    easing: "easeOutExpo",
  });
}

export function animateScore(targetValue, el, barEl) {
  if (!el) return;
  if (prefersReducedMotion() || typeof anime === "undefined") {
    el.textContent = String(targetValue);
    if (barEl) barEl.style.width = `${targetValue}%`;
    return;
  }
  const obj = { v: 0 };
  anime({
    targets: obj,
    v: targetValue,
    round: 1,
    duration: 800,
    easing: "easeOutExpo",
    update: () => {
      el.textContent = String(obj.v);
      if (barEl) barEl.style.width = `${obj.v}%`;
    },
  });
}

export function pulseAlert(el) {
  if (!el || prefersReducedMotion() || typeof anime === "undefined") return;
  anime({
    targets: el,
    scale: [1, 1.03, 1],
    duration: 400,
    easing: "easeInOutQuad",
    loop: 2,
  });
}

export function staggerRanking(items) {
  if (prefersReducedMotion() || typeof anime === "undefined") return;
  anime({
    targets: items,
    opacity: [0, 1],
    translateX: [-8, 0],
    delay: anime.stagger(80),
    duration: 400,
    easing: "easeOutExpo",
  });
}
