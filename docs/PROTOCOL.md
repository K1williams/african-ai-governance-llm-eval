# Study protocol and preregistration draft (v0.1)

Prepared 2026-11-15. This protocol is **not registered** in an external repository. Freeze it and timestamp the commit before running the confirmatory study; report changes transparently.

## 1. Research question and scope

Does oracle provision of selected original official government policy paragraphs change an LLM's performance on questions about published national AI governance documents in Rwanda, Kenya and Nigeria relative to a closed-book baseline? The tested unit is a **document-grounded question**, not a country's entire legal situation. The term *oracle* means manually selected evidence, not a production retrieval engine.

## 2. Hypotheses

- **H1 (accuracy):** Accuracy is higher with official evidence than without evidence.
- **H2 (source grounding):** Human-adjudicated support for specific generated claims is higher with supplied excerpts.
- **H3 (policy-status overclaim):** False assertions that recommendations have already been enacted or implemented are lower with excerpts.
- **H4 (abstention):** On items whose answers cannot be established by the source document, appropriate abstention is more common with official excerpts.

These are proposed hypotheses, **not results**.

## 3. Sampling

Three purposively selected English-language, publicly downloadable national documents; this is not statistically representative of African countries or languages. A 60-item AI-assisted draft seed is stratified into 20 items per country: 14 document-answerable, 3 false-premise and 3 corpus-unanswerable. A domain reviewer must validate and revise wording, references, difficulty and answerability. One independent reviewer should evaluate at least a stratified 20-item subset; resolve disagreement before outcomes are analysed. Do not leak hidden labels into model prompts.

## 4. Intervention and controls

Same model ID, provider, API endpoint, system prompt, user instruction, generation temperature, token budget and question wording. Condition A: no official excerpt; condition B: oracle excerpt automatically selected from the official source PDF by a manually checked question anchor. Use separate stateless calls. Pre-register the exact model/version identifier, run date and all parameters. Run conditions in seeded-random order to reduce time/drift confounding. The runner shuffles question-condition calls with a logged `order_seed` and fingerprints configuration and input files to reject incompatible resumed runs. As the model endpoint may change behind a fixed model ID, record the provider response model version when available.

Manual evidence anchors refer to a government PDF page; all 60 retrieval contexts must be reviewed before comparing models. If a PDF is inaccessible, **stop**, do not synthesize its evidence. The 'oracle' is an upper bound on document availability, not evidence that a retriever could find that excerpt.

## 5. Gold labels and citation rule

Each question has a source document, a reference answer, a document-location hint, and one of three classes. 'Unanswerable' means not answerable **from this reference corpus**, not unknown in the world. 'False premise' means the supplied source conflicts with the question's asserted policy-versus-implementation status. Some documents mix legislative background with policy proposals; do not infer an entire jurisdiction's legal status from the document.

### Exclusion criteria

Exclude a question before analysis only if expert checking finds its answer ambiguous, outdated, not supported by the designated document or trivially duplicated. Record item ID, reason and corrected version. Do not remove an item because a tested model failed it.

## 6. Evaluation rubric

Primary endpoint: human-adjudicated binary factual correctness (1=correctly answers or explicitly rejects false premise / appropriately abstains on unanswerable; 0=otherwise). Secondary: claim-level document support (binary per answer in the pilot), policy-status confusion (1=misstates proposed action as legally binding, adopted or operational, 0=no such error), and appropriate abstention (1=appropriate answer-versus-abstention decision, 0=inappropriate). The latter is not a measure of response quality alone. Evaluate exact unsupported claims with an error taxonomy: proposed→implemented, strategy→law, non-evidence→nonexistence, fabricated entity/penalty, wrong document or timeframe, missing uncertainty, other.

Adjudicators should initially see response and question, without the condition, when feasible; check gold/source after first-pass scoring. Report reviewer count and disagreements. A model-generated judge may be exploratory but must not substitute unreported human adjudication.

## 7. Statistical analysis

Compute rates separately by condition and paired differences for each question; paired bootstrap percentile 95% intervals at question level, separately by country where samples permit. Given only 3 purposively selected countries, descriptive intervals **do not support population generalisation**. Report matched-pair contingency tables and optionally exact McNemar tests; label inferential tests exploratory for this small convenience sample. For policy-status confusion, a *negative* paired difference means improvement. Predefine exclusion and missing-response handling; never treat API errors as abstentions.

## 8. Threats to validity

Author-generated benchmark, limited document diversity, question difficulty, prompt effects, changing model snapshots, lack of source-date synchronisation, biased anchor selection, excerpt selection errors, PDF extraction artifacts, contamination from public documents in model pretraining, model refusal bias and manual grader subjectivity. 'Oracle' condition is not retrieval-augmented generation, and it only assesses evidence availability. A real RAG study must separately evaluate retrieval accuracy, coverage, latency and failure cases.

## 9. Disclosure and implementation status

No human participants, sensitive personal data or clinical AI claims are involved in this version. Respect source rights; cache original PDFs locally and publish URLs/hashes rather than republishing government documents. Re-run the original source checks before any submission. As of 2026-11-15, **model experiment not executed**, gold labels **not independently validated**, no performance conclusions.