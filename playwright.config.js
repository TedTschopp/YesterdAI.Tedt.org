import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/browser',
  timeout: 45000,
  expect: { timeout: 10000, toHaveScreenshot: { maxDiffPixelRatio: 0.001, animations: 'disabled' } },
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  workers: process.env.CI ? 2 : 2,
  reporter: [['list'], ['html', { open: 'never' }]],
  outputDir: 'test-results/browser',
  snapshotPathTemplate: '{testDir}/__screenshots__/{arg}{ext}',
  use: { baseURL: 'http://127.0.0.1:4173', trace: 'retain-on-failure' },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'webkit', testMatch: /reader\.spec\.js/, use: { browserName: 'webkit' } }
  ],
  webServer: [
    { command: 'python3 -m http.server 4173 --bind 127.0.0.1 --directory _site', port: 4173, reuseExistingServer: !process.env.CI },
    { command: 'python3 -m http.server 4174 --bind 127.0.0.1 --directory test-results/fixture-site', port: 4174, reuseExistingServer: !process.env.CI }
  ]
});
