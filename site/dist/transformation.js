// Keep the optional reference reachable by links and complete in printed copies.
const deliveryReference = document.getElementById('delivery-reference');

function revealTransformationTarget() {
  let id;
  try {
    id = decodeURIComponent(window.location.hash.slice(1));
  } catch {
    return;
  }
  const target = document.getElementById(id);
  if (!target || !deliveryReference?.contains(target)) return;
  for (let element = target; element && element !== deliveryReference; element = element.parentElement) {
    if (element.tagName === 'DETAILS') element.open = true;
  }
  target.scrollIntoView({ block: 'start' });
}

window.addEventListener('hashchange', revealTransformationTarget);
// Reopen a target even when its fragment is already in the address bar.
document.addEventListener('click', (event) => {
  const link = event.target.closest('a[href^="#"]');
  if (link?.hash === window.location.hash) revealTransformationTarget();
});
revealTransformationTarget();

let referencePrintState = [];
window.addEventListener('beforeprint', () => {
  // site.js owns figure-reading state; snapshotting it after its handler would
  // restore the print-expanded state rather than the reader's original choice.
  referencePrintState = [...deliveryReference.querySelectorAll('details:not(.figure-reading)')].map((detail) => [detail, detail.open]);
  referencePrintState.forEach(([detail]) => { detail.open = true; });
});
window.addEventListener('afterprint', () => {
  referencePrintState.forEach(([detail, open]) => { detail.open = open; });
  referencePrintState = [];
});
