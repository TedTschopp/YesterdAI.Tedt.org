import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';

const root = path.resolve(import.meta.dirname, '..');
const site = path.join(root, '_site');
new vm.Script(fs.readFileSync(path.join(root,'assets/js/site.js'),'utf8'));
assert.ok(fs.existsSync(path.join(site,'pagefind/pagefind.js')), 'Build the Pagefind bundle before publishing.');
const entries = JSON.parse(fs.readFileSync(path.join(site,'search-index.json'),'utf8'));
assert.equal(new Set(entries.map(item=>item.id)).size, entries.length, 'Search identities must be unique.');
for (const item of entries) {
  assert.match(item.url,/^\/articles\/[a-z0-9-]+\/$/);
  assert.ok(fs.existsSync(path.join(site,item.url,'index.html')));
}
const fonts = JSON.parse(fs.readFileSync(path.join(root,'assets/fonts/manifest.json'),'utf8'));
for (const item of fonts.files) {
  const data=fs.readFileSync(path.join(root,'assets/fonts',item.file));
  assert.equal(crypto.createHash('sha256').update(data).digest('hex'),item.sha256,'Pinned font changed: '+item.file);
}
console.log('Static publication smoke passed: client syntax, stable search identities, Pagefind bundle, and pinned fonts.');
console.log('Interactive browser, accessibility, and visual checks run as the GitHub deployment gate.');
