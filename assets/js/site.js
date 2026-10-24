(() => {
  const toggle = document.querySelector('[data-theme-toggle]');
  function syncTheme() {
    const dark = document.documentElement.dataset.theme === 'dark';
    if (toggle) { toggle.textContent = dark ? 'Light' : 'Dark'; toggle.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`); }
  }
  syncTheme();
  toggle?.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('yia-theme', next); } catch (_) { /* The theme still works without persistence. */ }
    syncTheme();
  });
  const input = document.getElementById('search-input');
  if (!input) return;
  const form = document.querySelector('.search-form');
  const status = document.getElementById('search-status');
  const rows = [...document.querySelectorAll('#search-results .story-row')];
  const filters = [...document.querySelectorAll('[data-filter]')];
  let topic = new URLSearchParams(location.search).get('topic') || 'all';
  let index;
  input.value = new URLSearchParams(location.search).get('q') || '';
  function filter() {
    const words = input.value.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    rows.forEach((row, i) => {
      const item = index?.[i];
      const text = (item ? `${item.title} ${item.summary} ${item.text}` : row.textContent).toLocaleLowerCase();
      const visible = (topic === 'all' || row.dataset.section === topic) && words.every(word => text.includes(word));
      row.hidden = !visible; if (visible) count++;
    });
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === topic)));
    status.textContent = `${count} ${count === 1 ? 'article' : 'articles'}${input.value ? ` matching “${input.value}”` : ''}`;
    const params = new URLSearchParams();
    if (input.value) params.set('q', input.value);
    if (topic !== 'all') params.set('topic', topic);
    history.replaceState(null, '', `/search/${params.size ? '?' + params : ''}`);
  }
  form.addEventListener('submit', event => { event.preventDefault(); filter(); });
  input.addEventListener('input', filter);
  filters.forEach(button => button.addEventListener('click', () => { topic = button.dataset.filter; filter(); }));
  filter();
  fetch('/search-index.json').then(response => { if (!response.ok) throw new Error('Search index unavailable'); return response.json(); }).then(data => { index = data; filter(); }).catch(() => { /* Rendered article titles and summaries remain searchable. */ });
})();
