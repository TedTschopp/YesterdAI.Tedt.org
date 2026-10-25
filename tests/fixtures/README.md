# Publication Regression Fixtures

preservation-baseline.json captures the 23 original articles before the October 24 reader revision: immutable identity/source/date/hero metadata, original body anchors, attributed passages, and image/logo hashes.

title-case-migration.json records the exact original and revised titles for Ted's October 24 title-case request. Preservation tests permit those specific capitalization changes while checking that the wording remains identical. The original preservation baseline remains unchanged.

site/ is a frozen rendering fixture, never a production source. It contains eight representative revised article bodies and deliberate date/section assignments to exercise all five sections, an explicit lead independent of section order, multiple formats, long headlines, native-ratio illustrations, Quick Hits, and a quiet day. Those assignments are layout test data, not a publishable historical edition.

The fixture builder combines this content with current templates and fixed assets under ignored test-results/. Tests never copy it into the public _site. The production config excludes tests/. Routine editorial writes cannot update these fixtures or approved PNG baselines.

Initial visual candidates are generated in CI, downloaded for review, and committed explicitly. Subsequent deployment checks compare against those reviewed Linux/Chromium baselines; they never accept changes automatically.
