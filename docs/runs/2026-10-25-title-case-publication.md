# Title-Case Publication

Ted authorized merging and publishing PR #3 on October 25, 2026. Main had advanced with the October 25 edition and the new 3–5-article target, creating conflicts in the reader contract and operations guide. The PR branch merges current main without rewriting history. Reader contract 2.0.3 retains both the title-case policy and the new article target, including its evidence-based shortfall rule and preservation of published edition membership.

The two October 25 article titles, the analysis subheads, the edition title, and its authored Quick Hit title now follow the same capitalization policy. Original wording, body paragraphs, stable IDs, URLs, publication/source dates, reporting window, membership, and hero provenance remain intact; modified_at records the capitalization revision. Upstream feeds and quoted source titles retain their supplied text. The reviewed fixed-content visual baselines are unchanged.

All six local checks passed after reconciliation: 36 Python tests, editorial validation of eight editions and 26 stories, strict Jekyll build, Pagefind indexing, rendered checks for 47 pages, and JavaScript/static smoke checks. The preservation audit compared every article and edition with current main and verified unchanged artwork and feed snapshots.

The merge-and-publish request also requires refreshed PR CI, a successful deployment for the merged commit, and checks of the public headings and metadata. Exact merge/deployment evidence is available through PR #3 and its associated Actions runs after publication.
