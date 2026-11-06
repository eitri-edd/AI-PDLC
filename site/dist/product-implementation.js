// Position journey links after the shared diagrams finish their responsive layout.
function revealImplementationJourney() {
  const requestedHash = window.location.hash;
  let id;
  try {
    id = decodeURIComponent(requestedHash.slice(1));
  } catch {
    return;
  }
  if (!id.startsWith('asset-') && id !== 'example-annual-workflow' && id !== 'example-permission-check') return;
  const target = document.getElementById(id === 'example-permission-check' ? 'example-annual-workflow' : id);
  if (!target) return;
  requestAnimationFrame(() => requestAnimationFrame(() => {
    if (window.location.hash !== requestedHash) return;
    target.scrollIntoView({ block: 'start', behavior: 'instant' });
  }));
}

revealImplementationJourney();
window.addEventListener('load', revealImplementationJourney);
window.addEventListener('hashchange', revealImplementationJourney);
