const navigation = document.querySelector('.site-navigation');
const mobile = window.matchMedia('(max-width: 959px)');
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
const sections = contentsLinks.map((link) => document.querySelector(link.hash));
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
