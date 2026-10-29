(async () => {
  'use strict';
  const { publicationNotice } = await import('/assets/js/reader-state.js');
  document.querySelectorAll('.publication-notice').forEach(notice => {
    const state = publicationNotice(notice.dataset);
    if (!state) return;
    notice.textContent = state.message;
    if (state.href) {
      const link = document.createElement('a'); link.href = state.href; link.textContent = state.link; notice.append(link);
    }
    notice.hidden = false;
  });

  const input = document.getElementById('search-input');
  if (!input) return;
  const form = document.querySelector('.search-form');
  const status = document.getElementById('search-status');
  const results = document.getElementById('search-results');
  const empty = document.getElementById('search-empty');
  const filters = [...document.querySelectorAll('[data-filter]')];
  const subject = document.getElementById('subject-filter');
  const pagination = document.querySelector('.search-pagination');
  const previous = document.querySelector('[data-search-previous]');
  const next = document.querySelector('[data-search-next]');
  const pageLabel = document.querySelector('[data-search-page]');
  const initial = new URLSearchParams(location.search);
  let section = initial.get('topic') || 'all';
  if (!filters.some(button => button.dataset.filter === section)) section = 'all';
  input.value = initial.get('q') || '';
  subject.value = initial.get('tag') || '';
  if (subject.selectedIndex < 0) subject.value = '';
  let page = Math.max(1, Number(initial.get('page')) || 1);
  const pageSize = 20;
  let articles = [], byId = new Map(), pagefind, sequence = 0, timer;
  let ready = false, fullTextFailed = false;

  function saveState(push = false) {
    const params = new URLSearchParams();
    if (input.value.trim()) params.set('q', input.value.trim());
    if (section !== 'all') params.set('topic', section);
    if (subject.value) params.set('tag', subject.value);
    if (page > 1) params.set('page', page);
    const url = '/search/' + (params.size ? '?' + params : '');
    if (url !== location.pathname + location.search) history[push ? 'pushState' : 'replaceState'](null, '', url);
  }
  function compactResult(article, excerpt) {
    const row = document.createElement('article'); row.className = 'compact-story'; row.dataset.articleId = article.id;
    const meta = document.createElement('p'); meta.className = 'meta';
    const date = new Date(article.edition_date + 'T12:00:00Z').toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
    meta.textContent = date + ' · ' + article.section_name + ' · ' + article.format + ' · ' + article.minutes + ' min';
    const heading = document.createElement('h2'), link = document.createElement('a'); link.href = article.url; link.textContent = article.title; heading.append(link);
    const description = document.createElement('p'); description.className = 'body-sm';
    description.textContent = excerpt || article.summary;
    row.append(meta, heading, description);
    return row;
  }
  function fallbackMatches(query) {
    const words = query.toLocaleLowerCase().split(/\s+/).filter(Boolean);
    return articles.filter(article =>
      (section === 'all' || article.section === section) &&
      (!subject.value || (article.topics || []).includes(subject.value)) &&
      words.every(word => (article.title + ' ' + article.summary).toLocaleLowerCase().includes(word))
    ).map(article => ({ article, excerpt: '' }));
  }
  async function search(push = false) {
    if (!ready) return;
    const ticket = ++sequence;
    const query = input.value.trim();
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === section)));
    let matches;
    if (query && !fullTextFailed) {
      status.textContent = 'Searching…';
      try {
        pagefind ||= import('/pagefind/pagefind.js');
        const engine = await pagefind;
        const options = { filters: {} };
        if (section !== 'all') options.filters.section = section;
        if (subject.value) options.filters.tag = subject.value;
        const response = await engine.search(query, options);
        const data = await Promise.all(response.results.map(result => result.data()));
        matches = data.map(item => {
          const article = byId.get(item.meta.article_id);
          if (!article) return null;
          const excerpt = new DOMParser().parseFromString(item.excerpt, 'text/html').body.textContent;
          return { article, excerpt };
        }).filter(Boolean);
      } catch (_) {
        fullTextFailed = true;
        matches = fallbackMatches(query);
      }
    } else matches = fallbackMatches(query);
    if (ticket !== sequence) return;
    const pages = Math.max(1, Math.ceil(matches.length / pageSize));
    page = Math.min(page, pages);
    results.replaceChildren(...matches.slice((page - 1) * pageSize, page * pageSize).map(item => compactResult(item.article, item.excerpt)));
    empty.hidden = matches.length !== 0;
    pagination.hidden = pages === 1;
    previous.disabled = page === 1; next.disabled = page === pages;
    pageLabel.textContent = 'Page ' + page + ' of ' + pages;
    status.textContent = matches.length + (matches.length === 1 ? ' article' : ' articles') + (query ? ' matching “' + query + '”' : '') + (fullTextFailed && query ? '. Full-text search is unavailable; matching titles and summaries.' : '');
    saveState(push);
  }
  form.addEventListener('submit', event => { event.preventDefault(); clearTimeout(timer); page = 1; search(true); });
  input.addEventListener('input', () => { clearTimeout(timer); ++sequence; page = 1; timer = setTimeout(() => search(), 160); });
  filters.forEach(button => button.addEventListener('click', () => { section = button.dataset.filter; page = 1; search(true); }));
  subject.addEventListener('change', () => { page = 1; search(true); });
  previous.addEventListener('click', () => { page--; search(true); });
  next.addEventListener('click', () => { page++; search(true); });
  addEventListener('popstate', () => {
    const params = new URLSearchParams(location.search);
    input.value = params.get('q') || '';
    section = params.get('topic') || 'all';
    if (!filters.some(button => button.dataset.filter === section)) section = 'all';
    subject.value = params.get('tag') || '';
    if (subject.selectedIndex < 0) subject.value = '';
    page = Math.max(1, Number(params.get('page')) || 1); search();
  });
  fetch('/search-index.json').then(response => {
    if (!response.ok) throw new Error('Article list unavailable');
    return response.json();
  }).then(data => {
    articles = data; byId = new Map(data.map(article => [article.id, article]));
    ready = true; search();
  }).catch(() => { status.textContent = 'Search is temporarily unavailable. Browse the articles below or explore a topic.'; });
})();
