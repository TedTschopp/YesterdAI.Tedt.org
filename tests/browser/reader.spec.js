import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import fs from 'node:fs';

const publication = JSON.parse(fs.readFileSync('_site/status.json','utf8'));
const edition = publication.latest_edition;
const article = '/articles/kapitsa-local-inference-operations/';
const routes = ['/', '/editions/' + edition + '/', article, '/archive/', '/search/', '/live/', '/about/', '/topics/', '/404.html'];
test.beforeEach(async ({page}) => {
  // Freeze the edition date without pausing debounced input and search timers.
  await page.clock.setFixedTime(new Date(edition + 'T20:00:00Z'));
});

for (const width of [320,390,768,1024,1280,1440]) {
  for (const theme of ['light','dark']) {
    test('reader layouts ' + width + ' ' + theme, async ({page}) => {
      test.setTimeout(90000);
      const pageErrors=[];
      page.on('pageerror', error=>pageErrors.push(error.message));
      await page.setViewportSize({width,height:width<=600?844:900});
      await page.addInitScript(value=>localStorage.setItem('yia-theme',value),theme);
      for (const route of routes) {
        await page.goto(route);
        await page.evaluate(()=>document.fonts.ready);
        await expect(page.locator('h1')).toHaveCount(1);
        await expect(page.locator('html')).toHaveAttribute('data-theme',theme);
        const dimensions=await page.evaluate(()=>({
          width:document.documentElement.clientWidth, scroll:document.documentElement.scrollWidth,
          bodyFont:getComputedStyle(document.body).fontSize,
          ratios:[...document.querySelectorAll('.hero-image,.story-thumbnail img')].filter(i=>i.clientWidth>0).map(i=>({actual:i.clientWidth/i.clientHeight,native:i.naturalWidth/i.naturalHeight}))
        }));
        expect(dimensions.scroll,route).toBeLessThanOrEqual(dimensions.width+1);
        expect(dimensions.bodyFont).toBe('18px');
        for (const ratio of dimensions.ratios) {
          if (Number.isFinite(ratio.native)) expect(Math.abs(ratio.actual-ratio.native)).toBeLessThan(0.03);
        }
        await expect(page.getByRole('heading',{name:'Looking Ahead',exact:true})).toHaveCount(0);
        await expect(page.getByText('Reconstructed from historical feed snapshots.',{exact:false})).toHaveCount(0);
        if (route==='/') {
          const first=await page.locator('.tldr-panel a').first().boundingBox();
          expect(first.y).toBeLessThan(width<=600?844:900);
        }
      }
      expect(pageErrors).toEqual([]);
    });
  }
}

test('main reading surfaces pass WCAG AA automated checks in both themes',async ({page})=>{
  test.setTimeout(180000);
  for (const theme of ['light','dark']) {
    await page.addInitScript(value=>localStorage.setItem('yia-theme',value),theme);
    for (const route of routes) {
      await page.goto(route);
      await page.evaluate(()=>document.fonts.ready);
      const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();
      expect(result.violations,theme+' '+route+' '+JSON.stringify(result.violations)).toEqual([]);
    }
  }
});

test('keyboard entry, theme persistence, and enlarged text remain usable',async ({page})=>{
  await page.goto('/');
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link',{name:'Skip to content'})).toBeFocused();
  await page.keyboard.press('Enter');
  await expect(page.locator('#main')).toBeFocused();
  await page.getByRole('button',{name:'Switch to dark theme'}).click();
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-theme','dark');
  await page.getByRole('button',{name:'Switch to light theme'}).click();
  await page.setViewportSize({width:320,height:844});
  await page.addStyleTag({content:'html { font-size: 200% !important; }'});
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
  expect(overflow).toBeLessThanOrEqual(1);
});

test('full-text results match the correct identity when metadata ordering changes',async ({page})=>{
  await page.route('**/search-index.json',async route=>{
    const response=await route.fetch();
    const data=await response.json();
    await route.fulfill({response,json:data.reverse()});
  });
  await page.goto('/search/?q=PubMed');
  await expect(page.locator('#search-status')).toHaveText('1 article matching “PubMed”');
  await expect(page.locator('#search-results a')).toHaveAttribute('href','/articles/citation-relevance-verification/');
  await expect(page.locator('#search-results')).toContainText('A real citation');
  await expect(page.locator('#search-results')).toContainText('PubMed');
});

test('bookmark filters, history, empty states and reduced-search fallback work',async ({page})=>{
  await page.goto('/search/?topic=security&tag=evaluation');
  await expect(page.locator('[data-filter="security"]')).toHaveAttribute('aria-pressed','true');
  await expect(page.getByLabel('Subject')).toHaveValue('evaluation');
  await page.getByLabel('Search articles').fill('a-word-that-has-no-matching-story');
  await expect(page.locator('#search-empty')).toBeVisible();
  await page.getByRole('link',{name:'clear the search'}).click();
  await expect(page.locator('#search-status')).toContainText('articles');
  await page.getByRole('button',{name:'Security',exact:true}).click();
  await page.getByRole('button',{name:'Vendors',exact:true}).click();
  await page.goBack();
  await expect(page.locator('[data-filter="security"]')).toHaveAttribute('aria-pressed','true');
  await page.route('**/pagefind/**',route=>route.abort());
  await page.goto('/search/?q=Kapitsa');
  await expect(page.locator('#search-status')).toContainText('Full-text search is unavailable');
  await expect(page.locator('#search-results')).toContainText('Kapitsa');
});

test('a failed metadata download leaves the complete static article list',async ({page})=>{
  await page.route('**/search-index.json',route=>route.fulfill({status:503,body:'Unavailable'}));
  await page.goto('/search/?q=Kapitsa');
  await expect(page.locator('#search-status')).toContainText('temporarily unavailable');
  await expect(page.locator('#search-results')).toContainText('Kapitsa');
  await expect(page.locator('#search-results .compact-story')).not.toHaveCount(0);
});

test('editions keep dated coverage and provide navigation and source access',async ({page})=>{
  await page.goto('/editions/'+edition+'/');
  await expect(page.locator('.tldr-panel a')).not.toHaveCount(0);
  await expect(page.locator('.edition-pagination a')).not.toHaveCount(0);
  await expect(page.locator('.live-label')).toHaveCount(0);
  await page.goto(article);
  await expect(page.locator('.source-credit a')).toHaveAttribute('href',/github\.com/);
  await expect(page.getByRole('heading',{name:'Sources',exact:true})).toBeVisible();
  await expect(page.locator('#for-practitioners')).toHaveCount(1);
  await expect(page.locator('.related-stories a')).not.toHaveCount(0);
});

test('a verified quiet-day fixture renders without inventing a lead',async ({page})=>{
  await page.goto('http://127.0.0.1:4174/editions/2026-10-23/');
  await expect(page.locator('main')).toContainText('No distinct developments');
  await expect(page.locator('.story-row')).toHaveCount(0);
  await expect(page.locator('h1')).toHaveText('A quieter morning');
});
