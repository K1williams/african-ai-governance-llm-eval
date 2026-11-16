# Human scoring and quality assurance rubric

Reviewers must not simply compare surface wording against the reference answer. Verify substance against the **designated official document**, paying attention to document date, voice and modality (will, proposes, recommends, established, enforced).

## Required fields (enter 0 or 1)

- `correct`: 1 if substantively correct within source scope, including rejection of an embedded false premise or a justified refusal when not established; 0 if false, unsupported, or incomplete on an essential fact.
- `supported`: 1 if substantive factual claims in the answer are supported by the designated source (when excerpt is absent, cross-check against official source yourself); 0 if at least one important factual claim is unsupported or contradicted.
- `status_confusion`: 1 if the answer presents a future proposal, policy recommendation or strategic aspiration as an enacted legal duty or a demonstrably completed activity; 0 otherwise. **Lower is better.**
- `appropriate_abstention`: 1 if the model answers when evidence suffices or abstains/corrects when it does not; 0 if it hallucinates from absence or needlessly refuses an answerable item.

## Error taxonomy

1. `strategy_as_law`: claims a strategy itself creates legal penalty.
2. `recommendation_as_implemented`: treats proposed offices/funds as already operating.
3. `absence_as_nonexistence`: treats no evidence in a document as proof nothing exists in the jurisdiction.
4. `fabricated_detail`: invents fines, dates, mandates, projects or reported outcomes.
5. `temporal_confusion`: misreads publication date or later developments.
6. `citation_mismatch`: cites a source for an assertion absent from it.
7. `other`.

## Reviewer workflow

1. Verify source PDF authenticity and page from the ministry/NCAIR website.
2. Check the question and reference answer; mark ambiguous questions for removal *before* running model experiments.
3. Check that the automatic evidence anchor returns the intended page and that the excerpt contains sufficient information.
4. Independently grade model responses; where possible hide condition labels to reduce observer bias.
5. Use adjudication notes for contentious decisions; retain original grading records.
6. Recompute outcomes only after every field is filled. The analyzer refuses blank outcomes.