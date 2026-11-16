# Publishing and verification instructions

**Current status:** The repository is prepared locally; not pushed to GitHub by the AI-assisted audit session. The connected GitHub integration lacks a create-repository operation and the accessible existing repositories are unrelated or private. Do not claim a GitHub URL until a push is verified.

## Dedicated repository

Create a new personal repository `african-ai-governance-llm-eval` under `K1williams` (not `tpp-raida`). Choose **public** only if preliminary status is acceptable; otherwise private until item validation is done. Leave 'Initialize with README' unchecked if importing this folder.

From the unzipped research folder:

```bash
cd african-ai-governance-llm-eval
git init -b main
git add .
git commit -m 'Initial AI-assisted research instrument and audited v0.2 methods'
git remote add origin https://github.com/K1williams/african-ai-governance-llm-eval.git
git push -u origin main
```

Note: GitHub requires an authorized credential flow (e.g. Git Credential Manager or SSH). Do not paste tokens into a public terminal log, chat or repository.

## Post-publication verification

1. Verify the actual repository exists and `README.md`, `docs/INDEPENDENT_AUDIT.md`, `audit/item_review_ledger.csv`, `data/questions.csv` and `.github/workflows/tests.yml` are visible.
2. Confirm CI passes in GitHub Actions (not merely locally).
3. Confirm `data/source_pdfs`, `.env`, results files and secret keys are absent.
4. Preserve the next published commit/tag with a protocol version and exact model configurations *before* running the model comparison.
5. Mark the public repository **preliminary research instrument** until manual PDF review, independent second-reviewer validation and actual model experiments are complete.