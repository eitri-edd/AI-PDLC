// Open an optional example or deep dive when a direct link targets it or its content.
// Native details/summary controls remain usable when JavaScript is unavailable.
function revealDiscoveryTarget() {
  const requestedHash = window.location.hash;
  let id;
  try {
    id = decodeURIComponent(window.location.hash.slice(1));
  } catch {
    return;
  }
  const target = document.getElementById(id);
  if (!target) return;
  let detail = target.closest('details');
  while (detail) {
    if (!detail.open) {
      detail.open = true;
    }
    detail = detail.parentElement?.closest('details');
  }
  // Shared diagram text equivalents can expand after the initial layout on mobile.
  // Scroll after that layout settles so a direct link lands on the intended content.
  requestAnimationFrame(() => requestAnimationFrame(() => {
    if (window.location.hash !== requestedHash) return;
    target.scrollIntoView({ block: 'start', behavior: 'instant' });
  }));
}

revealDiscoveryTarget();
window.addEventListener('load', revealDiscoveryTarget);
window.addEventListener('hashchange', revealDiscoveryTarget);

// Keep optional reference and example content readable in printed copies.
let discoveryPrintDetails = [];
window.addEventListener('beforeprint', () => {
  discoveryPrintDetails = [...document.querySelectorAll('.worked-example, .deep-dive')]
    .filter((detail) => !detail.open);
  discoveryPrintDetails.forEach((detail) => { detail.open = true; });
});
window.addEventListener('afterprint', () => {
  discoveryPrintDetails.forEach((detail) => { detail.open = false; });
  discoveryPrintDetails = [];
});
