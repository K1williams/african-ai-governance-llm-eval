# Primary-source evidence audit for the 12-question feasibility pilot

**Review date:** 16 November 2026. **Scope:** review of the 12 curated items against government-produced policy texts accessed through web-indexed PDF documents. This is not an independent second human annotation, full 60-question source review, or assessment of laws in force in 2026.

| Document ID | Identified document | Source and provenance | Evidence used in pilot | Limit |
|---|---|---|---|---|
| RWA | Rwanda National AI Policy **summary** (2023), 22 PDF pages, produced by the Ministry of ICT and Innovation; copy hosted by WHO Country Planning Cycle Database | https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/RWA_Rwanda_Artificial_Intelligence_Policy_2023.pdf | PDF pages 4, 9: MINICT/RURA authorship; Responsible AI Office proposal | A **summary**, not necessarily text-identical to longer full ministry or RURA PDF; items are anchored to this version only. |
| KEN | Republic of Kenya AI Strategy 2025–2030, printed March 2025; government-hosted 2025-06 PDF path | https://www.ict.go.ke/sites/default/files/2025-06/National-AI-Strategy_IMPLEMENTATION.pdf | Executive summary (printed pp. 8–9) and section 6.5 (printed p. 96) | This is the strategy, not the separate Dec 2025 implementation roadmap. Original file bytes could not be cached in the local tool runtime; online indexed text inspected. |
| NGA | Nigeria National Artificial Intelligence Strategy, September 2025; NCAIR/NITDA government host | https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf | PDF page 5: five pillars / 34 strategies; PDF p. 44: proposal for ethics body; PDF p. 41: proposed R&D fund | Government strategy is **not** the same legal instrument as an enacted AI law. |

## Audit findings

1. **Document-identified claims** may be checked against the dated texts. Claims about current implementation need new evidence beyond the documents.
2. **Policy-status distinctions:** Rwanda’s Responsible AI Office is presented as a proposal within a 2023 policy summary; Kenya’s Data and Emerging Technologies Directorate is proposed in strategy section 6.5; Nigeria’s AI Ethics Expert Group/Commission is described as an initiative to create. None of those statements proves current status or enforcement powers.
3. **Temporal scope:** A 2023 or 2025 publication cannot itself evidence actions or fines that occurred in calendar year 2026. "Cannot establish" is different from "zero".
4. **Reference answer policy:** Answers in `items.json` are grounded *interpretations of the dated source*, not legal advice or claims about the state of the law in November 2026.
5. **Evidence condition is not a literal excerpt:** `context_fact` is a concise, researcher-curated fact summary based on the cited page. Hence the 12-item experiment tests effects of supplying relevant policy **fact summaries**, not the original project’s stronger treatment of exact official-document excerpts. The latter remains a separate, untested 60-item research question.
6. **Review status:** All 12 items have source URL and section/page trace, and were checked by an AI-assisted desk review; no independent external human adjudicator and no inter-rater reliability estimate. These limits must accompany any use of the outputs.

## Explicitly excluded interpretations

- No claim that Rwanda’s proposed office, Kenya’s proposed directorate, or Nigeria’s proposed commission has *never* existed.
- No claim that a strategy itself is necessarily the entire set of legal obligations in its country.
- No citation to the model’s responses as evidence of actual governance arrangements.

## Next quality gate for the full 60-item study

Obtain exact original PDF bytes/hashes, validate every span and answer key, replace fact-summary intervention with independently approved page excerpts, and secure an external second reviewer. Freeze all conditions and pre-register the accuracy rubric before making inferential claims from new models.