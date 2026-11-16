# AI Policy Grounding — African Governance Reliability Pilot

**Status: v0.2 source-screened research instrument, with AI-assisted desk-review and corrected citations; original official PDF page-span checks, external second review, and live model study remain pending. NOT a validated benchmark or completed paper.** 15 November 2026.

**Research question.** To what extent does providing verified official national AI policy excerpts, rather than no documents, change the factual accuracy, evidential support and responsible expression of uncertainty of one language model answering questions about national AI governance in selected African countries?

## What is here

- 60 preliminary questions: 20 each for Rwanda (RWA), Kenya (KEN), Nigeria (NGA).
- 42 document-answerable, 9 false-premise, and 9 corpus-unanswerable questions.
- Links to **official government PDFs**, question-level anchor phrases, expected-answer notes, and a transparent annotation status.
- A paired **closed-book vs oracle-excerpt** model evaluation script; manual adjudication sheet generator; paired-bootstrap descriptive analysis.
- Tests for dataset integrity, outcome scoring and basic prompt construction.

**Important:** The 60 items received a separate AI-assisted desk audit and corrective editorial review on 15 November 2026, with official-source spot checks, not full PDF-span verification. This is NOT external independent expert annotation, a complete page-span audit using the local original PDF bytes, or inter-rater reliability assessment. The author/owner must review and correct each item before releasing benchmark claims. This is an *individual* research project; it does not represent TPP RAIDA or ARAPI, and does not reuse their private research material.

## Primary sources

| Country | Source | Document status (do not confuse with laws) |
|---|---|---|
| Rwanda | [National AI Policy](https://rura.rw/fileadmin/Documents/ICT/Laws/Rwanda_national_Artificial_intelligence_Policy.pdf) | Government policy/roadmap |
| Kenya | [Kenya AI Strategy 2025–2030](https://ict.go.ke/sites/default/files/2025-03/Kenya%20AI%20Strategy%202025%20-%202030.pdf) | Government strategy, officially launched 27 March 2025 |
| Nigeria | [National Artificial Intelligence Strategy, September 2025](https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf) | Government-published national strategy |

A strategy recommending a regulator **does not prove** a regulator exists or exercises powers. 'Not established in the provided document' **does not mean** 'does not exist in reality'. We explicitly distinguish these.

## Run locally

```bash
python -m venv .venv
# activate virtual environment (platform-specific)
pip install -r requirements.txt
python -m src.validate_dataset
python -m unittest discover -s tests -v
python -m src.fetch_sources               # network access required
python -m src.audit_evidence              # manually review all 60 PDF spans
python -m src.run_eval --model YOUR_MODEL_ID --dry-run
```

**Only after** reviewing source-page selections and question labels, with an API-compatible model endpoint and credits:

```bash
export AI_EVAL_API_KEY="your-private-api-key"
python -m src.run_eval --model YOUR_PINNED_MODEL --condition both --max-items 10
python -m src.run_eval --model YOUR_PINNED_MODEL --condition both --max-items 60
python -m src.prepare_reviews
# Human reviewer fills correct, supported, status_confusion, appropriate_abstention
python -m src.score --review results/review_sheet.csv
```

The runner uses the Chat Completions API format; `--endpoint` changes its location. Not every provider supports the same temperature or token parameters. Make a small pilot request first and revise the provider adapter if necessary. Usage charges apply. **Never commit API keys.**

Results, cached PDFs and private review sheets are ignored by `.gitignore` until explicitly vetted. The source download reports SHA-256 checksums. The model runner records timestamp, randomisation seed, exact prompts, model ID, response, usage, document hash, excerpt hash, PDF page and output parsing status. It skips completed request-condition-model combinations when resuming the same output file; do not mix runs with different model settings in one output file.

## Protocol and boundaries

Read [Independent desk audit](docs/INDEPENDENT_AUDIT.md), [Study protocol](docs/PROTOCOL.md), [review rubric](docs/REVIEW_RUBRIC.md), [related work](docs/RELATED_WORK.md), and [sources and provenance](docs/SOURCES.md). The study tests *document-grounded QA*, not full legal compliance determination, deployment certification or real-world AI safety performance.

**Acceptance for research claims:** Every answer key checked against official PDFs, evidence context manually approved, independent second-reviewer subset, actual model calls run, blinded adjudication completed, error analysis reported, and reproducibility run passed on another machine. Until then there are **no model-performance findings**.

## Attribution

Provisional project owner and intended researcher: **Williams Stonard Kaphika** (independent research). Initial draft dataset, code scaffolding and documentation were prepared with AI assistance; human-led review, experiment execution and scientific responsibility remain pending. No institutional sponsorship, external validation or publication is implied.

## Reuse

Original code and question templates may be reused with attribution to the eventual authors. Government PDFs are *not redistributed here*; check official source rights and download from the ministries. No private ARAPI or TPP RAIDA material is included.

## Release readiness

See [Independent desk audit and limitations](docs/INDEPENDENT_AUDIT.md) and [review ledger](audit/item_review_ledger.csv). No live model outputs or benchmark claims are included. The repository is a **research instrument preview**, not a completed research article.

### Publishing

See [publishing instructions](docs/PUBLISHING.md). A prepared local release is not itself a GitHub publication.