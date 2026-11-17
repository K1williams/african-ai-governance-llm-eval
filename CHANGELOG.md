# Changelog

## v0.2 — 15 November 2026 — Independent desk review and source integrity corrections

- Standardised Kenya's PDF link to the official March 2025 strategy path; the earlier June-hosted path also indexes as the same strategy.
- Switched Rwanda's primary PDF to regulator-hosted publication because original ministry URL was inaccessible to the browser audit.
- Reworded twelve questions to make the scope and temporal boundary explicit; corrected ambiguous reference wording.
- Added item-by-item review ledger distinguishing online source screening from the still-pending full PDF and independent second-reviewer checks.
- Tightened evidence selection: no silent keyword fallback if an anchor is missing.
- Hardened experiment resumption against mixing datasets or model configurations and blocked unapproved oracle evidence in production runs.
- Expanded automated regression tests for rejected evidence, unapproved contexts and run fingerprints.
- No LLM experiments, independent external peer review or research performance findings were created as part of this release.

## v0.3 — 2026-11-16 — Source-traceable, executable feasibility pilot
- Added 12 balanced policy questions anchored to identifiable pages of Rwanda (2023 policy summary), Kenya (2025 strategy), and Nigeria (2025 strategy).
- Added actual open-weight baseline inference script and GitHub Actions execution; outputs are committed only when executed, not guessed or simulated.
- Explicitly distinguished fact-summary context from verbatim PDF evidence and rejected source statements as proof of current legal authority or real-world institutional operation.
- Retained the full 60-item dataset as *draft*, not a completed benchmark. No accuracy claims without a complete reviewer-adjudicated dataset.