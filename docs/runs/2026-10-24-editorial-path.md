# Normal editorial publishing-path check

The launch collection already contains today’s validated retrospective edition, so this check creates no duplicate edition, article, or hero. It runs in an isolated clean worktree based on origin/main and publishes this editorial audit record using scripts/publish.py ship. That path fetches, rebases, checks the allowed file scope, reruns tests and validation, builds Jekyll, checks rendered links and feeds, and pushes without force.

Before this check, the initial Build and publish run 40140348443 succeeded. The custom-domain homepage returned the October 24 edition over trusted HTTPS, with the canonical https://yesterdai.tedt.org/ URL. GitHub Pages has HTTPS enforcement enabled and its certificate approved. Cloudflare’s DNS-only CNAME points to tedtschopp.github.io. The hourly importer was dispatched independently for verification.

The standalone daily Codex task publish-yesterday-in-ai is active for 5 a.m. local Pacific time, using gpt-6.1-sol and max reasoning. The operating instructions anchor coverage in America/Los_Angeles and compute elapsed-hour windows in UTC across daylight-saving changes. The computer and desktop application must be running for that project-based task.

This document records the preflight state. The resulting commit and deployment checks establish the outcome; final cutover verification is recorded after those checks.
