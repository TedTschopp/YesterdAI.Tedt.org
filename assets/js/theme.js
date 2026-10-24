(() => {
  let preference;
  try { preference = localStorage.getItem('yia-theme'); } catch (_) { /* Storage may be unavailable. */ }
  document.documentElement.dataset.theme = preference === 'dark' || preference === 'light'
    ? preference : (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
})();
