import { test, expect } from '@playwright/test';

const cases = [
  ['home', '/'],
  ['edition', '/editions/2026-10-24/'],
  ['article', '/articles/kapitsa-local-inference-operations/']
];
for (const width of [320, 390, 768, 1024, 1280, 1440]) {
  for (const theme of ['light', 'dark']) {
    for (const [name, route] of cases) {
      test(name + ' ' + width + ' ' + theme, async ({ page }) => {
        await page.setViewportSize({width, height: width <= 600 ? 844 : 900});
        await page.clock.install({time:new Date('2026-10-24T20:00:00Z')});
        await page.addInitScript(value => localStorage.setItem('yia-theme',value),theme);
        await page.goto('http://127.0.0.1:4174' + route);
        await page.evaluate(() => document.fonts.ready);
        await expect(page.locator('html')).toHaveAttribute('data-theme',theme);
        await expect(page).toHaveScreenshot(name + '-' + width + '-' + theme + '.png');
        if (name === 'home') {
          await expect(page.locator('.story-featured')).toHaveScreenshot('story-' + width + '-' + theme + '.png');
        }
      });
    }
  }
}
