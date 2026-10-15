const navigation = document.querySelector('.site-navigation');
const mobile = window.matchMedia('(max-width: 1099px)');
function syncNavigation() {
  navigation.open = !mobile.matches;
}
syncNavigation();
mobile.addEventListener('change', syncNavigation);
navigation.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && mobile.matches && navigation.open) {
    navigation.open = false;
    navigation.querySelector('summary').focus();
  }
});

const contentsLinks = [...document.querySelectorAll('.page-contents a')];
const sections = contentsLinks.map((link) => document.querySelector(link.hash)).filter(Boolean);
function updateContents() {
  let active = sections[0];
  for (const section of sections) {
    if (section.getBoundingClientRect().top <= window.innerHeight * 0.35) active = section;
  }
  if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 4) {
    active = sections[sections.length - 1];
  }
  for (const link of contentsLinks) {
    if (active && link.hash === `#${active.id}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}

// Change the default only when a figure crosses the reading-width boundary.
// A reader's choice to expand/collapse is otherwise preserved during resizing.
let printing = false;
const diagramObserver = new ResizeObserver((entries) => {
  for (const { target, contentRect } of entries) {
    if (printing) continue;
    const wide = contentRect.width >= 712;
    if (target.dataset.wide === String(wide)) continue;
    target.dataset.wide = String(wide);
    target.querySelector('.diagram-detail').open = wide;
    target.querySelector('.figure-reading').open = !wide;
  }
});
document.querySelectorAll('.concept-figure').forEach(figure => diagramObserver.observe(figure));

const skillForm = document.querySelector('.skill-filters');
if (skillForm) {
  skillForm.hidden = false;
  const query = document.querySelector('#skill-query');
  const status = document.querySelector('#skill-status');
  const results = document.querySelector('#skill-results');
  const rows = [...document.querySelectorAll('[data-skill]')];
  const groups = [...new Set(rows.map(row => row.closest('section')))];
  const searchable = new Map(rows.map(row => [row, row.textContent.toLowerCase()]));
  function filterSkills() {
    const terms = query.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    for (const row of rows) {
      row.hidden = !(terms.every(term => searchable.get(row).includes(term)) &&
        (status.value === 'all' || row.dataset.status === status.value));
      if (!row.hidden) count++;
    }
    for (const group of groups) {
      group.hidden = !rows.some(row => row.closest('section') === group && !row.hidden);
      group.querySelectorAll('table').forEach(table => {
        const skills = [...table.querySelectorAll('[data-skill]')];
        table.closest('.table-scroll').hidden = skills.length > 0 && skills.every(row => row.hidden);
      });
    }
    results.textContent = count ? `${count} of ${rows.length} entries shown.` : 'No matching entries. Try a task such as testing, or clear the filters.';
  }
  function revealLinkedSkill() {
    const target = document.getElementById(location.hash.slice(1));
    if (!target?.matches('[data-skill]')) return;
    query.value = '';
    status.value = 'all';
    filterSkills();
    target.scrollIntoView({ block: 'start' });
  }
  skillForm.addEventListener('submit', event => event.preventDefault());
  skillForm.addEventListener('input', filterSkills);
  skillForm.addEventListener('change', filterSkills);
  skillForm.addEventListener('reset', () => { query.value = ''; status.value = 'all'; filterSkills(); });
  window.addEventListener('hashchange', revealLinkedSkill);
  filterSkills();
  revealLinkedSkill();
}
if (sections.length) {
  let scheduled = false;
  window.addEventListener('scroll', () => {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => { updateContents(); scheduled = false; });
  }, { passive: true });
  window.addEventListener('resize', updateContents);
  updateContents();
}

// Keep the complete text equivalent available in printed copies.
let printDetails = [];
window.addEventListener("beforeprint", () => {
  printing = true;
  printDetails = [...document.querySelectorAll(".figure-reading, .concept-reference")].map(el => [el, el.open]);
  printDetails.forEach(([el]) => { el.open = true; });
});
window.addEventListener("afterprint", () => {
  printDetails.forEach(([el, open]) => { el.open = open; });
  printing = false;
});
