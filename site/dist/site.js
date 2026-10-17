const navigation = document.querySelector('.site-navigation');
const pageLayout = document.querySelector('.page-layout');
const navSummary = navigation?.querySelector('summary');

function syncNavigationState() {
  if (!navigation) return;
  const isCollapsed = !navigation.open;
  if (pageLayout) {
    pageLayout.classList.toggle('sidebar-collapsed', isCollapsed);
  }
  if (navSummary) {
    navSummary.setAttribute(
      'title',
      isCollapsed ? 'Expand guide navigation' : 'Collapse guide navigation'
    );
    navSummary.setAttribute(
      'aria-label',
      isCollapsed ? 'Expand guide navigation' : 'Collapse guide navigation'
    );
  }
}

if (navigation) {
  // Ensure open by default on initial load
  navigation.open = true;
  syncNavigationState();
  navigation.addEventListener('toggle', syncNavigationState);
  navigation.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && navigation.open) {
      navigation.open = false;
      navSummary?.focus();
    }
  });
}

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

// Ensure shared SVG gradients and refined arrowheads exist on every page with diagrams.
function ensureSharedDiagramDefs() {
  const svgNS = 'http://www.w3.org/2000/svg';
  let defsSvg = document.querySelector('.diagram-defs');
  if (!defsSvg && document.querySelector('.concept-figure svg')) {
    defsSvg = document.createElementNS(svgNS, 'svg');
    defsSvg.setAttribute('class', 'diagram-defs');
    defsSvg.setAttribute('width', '0');
    defsSvg.setAttribute('height', '0');
    defsSvg.setAttribute('aria-hidden', 'true');
    defsSvg.setAttribute('focusable', 'false');
    document.body.prepend(defsSvg);
  }
  if (!defsSvg) return;

  let defs = defsSvg.querySelector('defs');
  if (!defs) {
    defs = document.createElementNS(svgNS, 'defs');
    defsSvg.appendChild(defs);
  }

  if (!defs.querySelector('#d-grad-node')) {
    defs.insertAdjacentHTML(
      'beforeend',
      `<linearGradient id="d-grad-node" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#ffffff"/>
        <stop offset="100%" stop-color="#f8fafc"/>
      </linearGradient>
      <linearGradient id="d-grad-accent" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#eff6ff"/>
        <stop offset="100%" stop-color="#dbeafe"/>
      </linearGradient>`
    );
  }
  if (!defs.querySelector('#d-grad-decision')) {
    defs.insertAdjacentHTML(
      'beforeend',
      `<linearGradient id="d-grad-decision" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#f0f7ff"/>
        <stop offset="100%" stop-color="#e0f2fe"/>
      </linearGradient>`
    );
  }
}

// Enhance diagrams with animated flow pulses, interactive node focus, and accessible Replay/Pause controls.
const reducedMotionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');

function enhanceDiagrams() {
  ensureSharedDiagramDefs();
  const svgNS = 'http://www.w3.org/2000/svg';

  document.querySelectorAll('.concept-figure').forEach((figure) => {
    const svg = figure.querySelector('svg');
    if (!svg || svg.dataset.enhanced === 'true') return;
    svg.dataset.enhanced = 'true';

    // Pad viewBox slightly so node borders and drop-shadows at x=0/1 or y=0/1 are never clipped
    const vbAttr = svg.getAttribute('viewBox');
    if (vbAttr) {
      const parts = vbAttr.trim().split(/[\s,]+/).map(Number);
      if (parts.length === 4 && parts.every((n) => !Number.isNaN(n))) {
        const [minX, minY, width, height] = parts;
        const padX = 8;
        const padY = 6;
        svg.setAttribute(
          'viewBox',
          `${minX - padX} ${minY - padY} ${width + padX * 2} ${height + padY * 2}`
        );
      }
    }

    // Ensure diagram detail is expanded by default so the visual diagram is immediately visible
    const detail = figure.querySelector('.diagram-detail');
    if (detail) detail.open = true;

    // Upgrade node rectangles & polygons for smoother corners and interactive hover
    const nodes = [...svg.querySelectorAll('.d-node, .d-decision, .d-planned')];
    nodes.forEach((node) => {
      node.classList.add('d-node-interactive');
      if (node.tagName.toLowerCase() === 'rect') {
        const rx = parseFloat(node.getAttribute('rx') || '0');
        if (rx > 0 && rx < 8) node.setAttribute('rx', '8');
      }
    });

    // Create animated flow overlay pulses along forward connector lines
    const lines = [...svg.querySelectorAll('path.d-line')];
    lines.forEach((line, index) => {
      if (line.classList.contains('d-dash')) return;
      // Skip filled shapes (like the widening scope band on path-to-production)
      if (line.getAttribute('style')?.includes('fill:')) return;

      const pulse = document.createElementNS(svgNS, 'path');
      pulse.setAttribute('d', line.getAttribute('d'));
      pulse.setAttribute('aria-hidden', 'true');
      pulse.setAttribute(
        'class',
        line.classList.contains('d-line-accent')
          ? 'd-flow-pulse d-flow-pulse-accent'
          : 'd-flow-pulse'
      );
      pulse.style.animationDelay = `${(index * 0.22).toFixed(2)}s`;
      line.insertAdjacentElement('afterend', pulse);
    });

    // Add interactive toolbar and figure number badge to figcaption
    const caption = figure.querySelector('figcaption');
    if (caption && !caption.querySelector('.figure-toolbar')) {
      const captionText = document.createElement('span');
      captionText.className = 'figure-caption-text';
      while (caption.firstChild) {
        captionText.appendChild(caption.firstChild);
      }
      // Wrap leading "Figure N." in a sleek pill badge
      const firstNode = captionText.firstChild;
      if (firstNode && firstNode.nodeType === Node.TEXT_NODE) {
        const match = firstNode.textContent.match(/^\s*(Figure\s+\d+)\.\s*(.*)$/s);
        if (match) {
          const figBadge = document.createElement('span');
          figBadge.className = 'figure-number';
          figBadge.textContent = match[1];
          firstNode.textContent = match[2];
          captionText.insertBefore(figBadge, firstNode);
        }
      }
      caption.appendChild(captionText);

      const toolbar = document.createElement('span');
      toolbar.className = 'figure-toolbar';

      const badge = document.createElement('span');
      badge.className = 'figure-badge';
      badge.innerHTML = '<span class="figure-badge-dot" aria-hidden="true"></span><span class="figure-badge-text">Animated flow</span>';

      const replayBtn = document.createElement('button');
      replayBtn.type = 'button';
      replayBtn.className = 'figure-btn';
      replayBtn.textContent = 'Step through';
      replayBtn.setAttribute('aria-label', 'Step through diagram sequence');

      const toggleBtn = document.createElement('button');
      toggleBtn.type = 'button';
      toggleBtn.className = 'figure-btn';
      const startPaused = reducedMotionQuery.matches;
      if (startPaused) figure.classList.add('diagram-paused');
      toggleBtn.setAttribute('aria-pressed', String(!startPaused));
      toggleBtn.textContent = startPaused ? 'Play' : 'Pause';
      const badgeLabel = badge.querySelector('.figure-badge-text');
      if (startPaused && badgeLabel) badgeLabel.textContent = 'Flow paused';

      toggleBtn.addEventListener('click', () => {
        const paused = figure.classList.toggle('diagram-paused');
        toggleBtn.setAttribute('aria-pressed', String(!paused));
        toggleBtn.textContent = paused ? 'Play' : 'Pause';
        if (badgeLabel) badgeLabel.textContent = paused ? 'Flow paused' : 'Animated flow';
      });

      let stepTimers = [];
      replayBtn.addEventListener('click', () => {
        stepTimers.forEach((id) => clearTimeout(id));
        stepTimers = [];
        nodes.forEach((n) => n.classList.remove('d-step-active'));
        lines.forEach((l) => l.classList.remove('d-line-active'));

        nodes.forEach((node, idx) => {
          const t1 = setTimeout(() => {
            nodes.forEach((n) => n.classList.remove('d-step-active'));
            node.classList.add('d-step-active');
            if (lines[idx]) lines[idx].classList.add('d-line-active');
          }, idx * 360);
          stepTimers.push(t1);
        });

        const clearTimer = setTimeout(() => {
          nodes.forEach((n) => n.classList.remove('d-step-active'));
          lines.forEach((l) => l.classList.remove('d-line-active'));
        }, nodes.length * 360 + 600);
        stepTimers.push(clearTimer);
      });

      toolbar.append(badge, replayBtn, toggleBtn);
      caption.appendChild(toolbar);
    }
  });
}

enhanceDiagrams();

// Change the default reading-summary expansion only when a figure crosses the reading-width boundary.
// Keep the visual diagram open on all viewports so readers can always see it.
let printing = false;
const diagramObserver = new ResizeObserver((entries) => {
  for (const { target, contentRect } of entries) {
    if (printing) continue;
    const wide = contentRect.width >= 712;
    if (target.dataset.wide === String(wide)) continue;
    target.dataset.wide = String(wide);
    const detail = target.querySelector('.diagram-detail');
    const reading = target.querySelector('.figure-reading');
    if (detail) detail.open = true;
    if (reading) reading.open = !wide;
  }
});
document.querySelectorAll('.concept-figure').forEach((figure) => diagramObserver.observe(figure));

// Automatically wire up skills catalogue search and status filter if .skills-table exists
const skillsTables = [...document.querySelectorAll('.skills-table')];
if (skillsTables.length && !document.querySelector('.skill-filters')) {
  skillsTables.forEach((table) => {
    table.querySelectorAll('tbody tr').forEach((tr) => {
      if (!tr.hasAttribute('data-skill')) {
        const firstCode = tr.querySelector('td code');
        tr.setAttribute('data-skill', firstCode ? firstCode.textContent.trim() : 'skill');
      }
      if (!tr.hasAttribute('data-status')) {
        const hasPlanned = Boolean(tr.querySelector('.status-planned'));
        tr.setAttribute('data-status', hasPlanned ? 'planned' : 'available');
      }
    });
  });

  const anchorSection = document.querySelector('#skills-by-stage') || skillsTables[0].closest('section');
  if (anchorSection) {
    const filterForm = document.createElement('form');
    filterForm.className = 'skill-filters';
    filterForm.setAttribute('aria-label', 'Filter skills catalogue');
    filterForm.innerHTML = `
      <label for="skill-query">
        Search skills or tasks
        <input id="skill-query" type="search" placeholder="e.g. review, Jira, testing, /do-work" autocomplete="off">
      </label>
      <label for="skill-status">
        Status
        <select id="skill-status">
          <option value="all">All entries</option>
          <option value="available">Available now</option>
          <option value="planned">Planned</option>
        </select>
      </label>
      <button type="reset">Reset</button>
      <p id="skill-results" class="skill-results" aria-live="polite"></p>
    `;
    anchorSection.insertBefore(filterForm, anchorSection.querySelector('h3, .table-scroll, p'));
  }
}

const skillForm = document.querySelector('.skill-filters');
if (skillForm) {
  skillForm.hidden = false;
  const query = document.querySelector('#skill-query');
  const status = document.querySelector('#skill-status');
  const results = document.querySelector('#skill-results');
  const rows = [...document.querySelectorAll('[data-skill]')];
  const groups = [...new Set(rows.map((row) => row.closest('section')).filter(Boolean))];
  const searchable = new Map(rows.map((row) => [row, row.textContent.toLowerCase()]));
  function filterSkills() {
    const terms = query.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    for (const row of rows) {
      row.hidden = !(
        terms.every((term) => searchable.get(row).includes(term)) &&
        (status.value === 'all' || row.dataset.status === status.value)
      );
      if (!row.hidden) count++;
    }
    for (const group of groups) {
      group.hidden = !rows.some((row) => row.closest('section') === group && !row.hidden);
      group.querySelectorAll('table').forEach((table) => {
        const skills = [...table.querySelectorAll('[data-skill]')];
        const wrapper = table.closest('.table-scroll');
        if (wrapper) wrapper.hidden = skills.length > 0 && skills.every((row) => row.hidden);
      });
    }
    results.textContent = count
      ? `${count} of ${rows.length} entries shown.`
      : 'No matching entries. Try a task such as testing, or clear the filters.';
  }
  function revealLinkedSkill() {
    if (!location.hash) return;
    const target = document.getElementById(location.hash.slice(1));
    if (!target?.matches('[data-skill]')) return;
    query.value = '';
    status.value = 'all';
    filterSkills();
    target.scrollIntoView({ block: 'start' });
  }
  skillForm.addEventListener('submit', (event) => event.preventDefault());
  skillForm.addEventListener('input', filterSkills);
  skillForm.addEventListener('change', filterSkills);
  skillForm.addEventListener('reset', () => {
    setTimeout(() => {
      query.value = '';
      status.value = 'all';
      filterSkills();
    }, 0);
  });
  window.addEventListener('hashchange', revealLinkedSkill);
  filterSkills();
  revealLinkedSkill();
}

if (sections.length) {
  let scheduled = false;
  window.addEventListener(
    'scroll',
    () => {
      if (scheduled) return;
      scheduled = true;
      requestAnimationFrame(() => {
        updateContents();
        scheduled = false;
      });
    },
    { passive: true }
  );
  window.addEventListener('resize', updateContents);
  updateContents();
}

// Keep the complete text equivalent available in printed copies.
let printDetails = [];
window.addEventListener('beforeprint', () => {
  printing = true;
  printDetails = [...document.querySelectorAll('.figure-reading, .concept-reference')].map((el) => [el, el.open]);
  printDetails.forEach(([el]) => {
    el.open = true;
  });
});
window.addEventListener('afterprint', () => {
  printDetails.forEach(([el, open]) => {
    el.open = open;
  });
  printing = false;
});

