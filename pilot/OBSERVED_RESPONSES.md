# Exploratory open-weight model evaluation: raw responses

> This file reports observed model outputs, **not human-adjudicated accuracy**. A small weak baseline model and fact summaries rather than verbatim PDFs were used. Do not cite as a validated benchmark or make legal-status assertions from model responses.

- Model: `Qwen/Qwen2.5-0.5B-Instruct`
- Resolved model revision: `7ae557604adf67be50417f59c2c2f167def9a775`
- Deterministic decoding (`do_sample=False`, `max_new_tokens=128`); temperature not applicable.
- Complete question pairs: 12 / 12
- Conditions: no source facts vs researcher-verified policy fact summary; identical questions and general instruction.
- Data are **descriptive observations**, not numerical factual-accuracy claims.

## Per-question outputs

### RWA-003: document_fact
Question: According to Rwanda's National AI Policy, which two public institutions developed the policy?
Reference answer (source-based): The Ministry of ICT and Innovation (MINICT) and the Rwanda Utilities Regulatory Authority (RURA).
Source: https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/RWA_Rwanda_Artificial_Intelligence_Policy_2023.pdf — PDF page 4 (index 3); policy summary, executive summary

**closed:** According to Rwanda's National AI Policy, the two public institutions that developed the policy were the Ministry of Science and Technology (MST) and the Ministry of Finance (MF).

**context:** The 2023 Rwandan national AI policy was developed by the Ministry of Information Technology (MINICT) and the Research and Development Agency (RURA).

### RWA-010: proposal_status
Question: What does Rwanda's 2023 National AI Policy say about creating a Responsible AI Office, and where would it be housed?
Reference answer (source-based): It recommends establishing a Responsible AI Office within MINICT; this document proposes it and does not verify that it is operating.
Source: https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/RWA_Rwanda_Artificial_Intelligence_Policy_2023.pdf — PDF page 9 (index 8); highlights and implementation section

**closed:** Rwanda's 2023 National AI Policy outlines several key points regarding the creation of a Responsible AI Office:  1. **Definition**: The policy defines "Responsible AI" as an approach that prioritizes ethical considerations in AI development, ensuring that AI systems are designed to benefit society rather than harm it.  2. **Housing**: It suggests establishing a dedicated Responsible AI Office within the Ministry of Information Technology (MIT). This office would oversee the implementation of responsible AI practices across all departments and sectors of the government.  3. **Responsibilities**:    - **Policy Development**: The office would develop guidelines for responsible AI,

**context:** Rwanda's 2023 National AI Policy outlines the establishment of a Responsible AI Office within the Ministry of Information and Communication Technology (MINICT). It states that this office will coordinate policy implementation and is committed to promoting responsible AI practices. However, it does not specify the location for its headquarters.

### RWA-015: false_premise
Question: Since Rwanda's Responsible AI Office was already fully operational when the 2023 National AI Policy was published, what enforcement penalties did it issue?
Reference answer (source-based): The premise is unsupported. The policy proposes establishing the office; it does not document its prior operation or penalties issued by it.
Source: https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/RWA_Rwanda_Artificial_Intelligence_Policy_2023.pdf — PDF page 9 (index 8); Responsible AI Office proposal

**closed:** The 2023 National AI Policy was issued by the Rwandan government in response to concerns raised by international organizations regarding the responsible development of artificial intelligence (AI) technologies in Rwanda. The policy aimed to ensure that AI projects in Rwanda were conducted with due diligence and transparency.  Given that the Responsible AI Office had been operating since the publication of the 2023 National AI Policy, it would be reasonable to infer that the office might have taken some action against those who violated the policy guidelines. However, without specific details from the time period mentioned, we can't provide precise information on what enforcement penalties were imposed.

**context:** No enforcement penalties were issued by the 2023 Rwandan National AI Policy document.

### RWA-019: beyond_document
Question: According to Rwanda's 2023 National AI Policy alone, how many Responsible AI Office enforcement actions occurred during calendar year 2025?
Reference answer (source-based): Cannot determine from the 2023 policy alone. It precedes 2025 and proposes the office; it is not a record of 2025 enforcement actions.
Source: https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/RWA_Rwanda_Artificial_Intelligence_Policy_2023.pdf — PDF pages 4 and 9 (indices 3 and 8); date and proposal

**closed:** According to Rwanda's 2023 National AI Policy, there are no specific details provided on the number of Responsible AI Office enforcement actions that occurred during calendar year 2025. The policy document does not provide this information.

**context:** According to Rwanda's 2023 National AI Policy, there are no specific enforcement actions mentioned for calendar year 2025 in relation to the Responsible AI Office.

### KEN-003: document_fact
Question: How many principal pillars and cross-cutting enablers are described in Kenya's March 2025 AI Strategy?
Reference answer (source-based): Three principal pillars and four cross-cutting enablers.
Source: https://www.ict.go.ke/sites/default/files/2025-06/National-AI-Strategy_IMPLEMENTATION.pdf — Executive summary, printed pages 8–9

**closed:** The March 2025 AI Strategy of Kenya does not provide specific details on the number of principal pillars and cross-cutting enablers. Therefore, I cannot provide an accurate answer based solely on this information.

**context:** The Kenya March 2025 AI Strategy describes three principal pillars and four cross-cutting enablers.

### KEN-013: proposal_status
Question: Does Kenya's March 2025 AI Strategy describe the Data and Emerging Technologies Directorate as a proposed structure or document that it was already functioning?
Reference answer (source-based): It describes a proposed directorate within the institutional framework, not evidence that the directorate was already operational.
Source: https://www.ict.go.ke/sites/default/files/2025-06/National-AI-Strategy_IMPLEMENTATION.pdf — Section 6.5, printed page 96

**closed:** Yes, the March 2025 AI Strategy describes the Data and Emerging Technologies Directorate (DET) as a proposed structure or document that it was already functioning.

**context:** The Kenya strategy's section 6.5 describes a proposed Directorate of Data and Emerging Technologies and its planned coordination role. Therefore, this is a proposed structure rather than a document that it was already functioning.

### KEN-015: false_premise
Question: What statutory fine does Kenya's March 2025 AI Strategy itself impose for operating an AI system without a newly mandatory national AI licence?
Reference answer (source-based): None is established by this strategy. A strategy is not itself a statute imposing this licence or fine; the premise is unsupported by the source.
Source: https://www.ict.go.ke/sites/default/files/2025-06/National-AI-Strategy_IMPLEMENTATION.pdf — Executive summary and Governance objective 5.1, printed pages 8–9, 76

**closed:** According to the March 2025 AI Strategy of Kenya, there is no specific mention of a statutory fine for operating an AI system without a new mandatory national AI license. The strategy focuses on promoting innovation in AI while ensuring compliance with existing regulations. Therefore, it is not possible to provide a definitive answer based solely on this document.

**context:** Kenya's March 2025 AI Strategy does not explicitly mention any statutory fine for operating an AI system without a new national AI license. The strategy focuses on developing legal and regulatory frameworks for AI, but does not include provisions for fines related to non-compliance with these regulations. Therefore, based on the information provided, there is no specific statutory fine that Kenya's March 2025 AI Strategy imposes for operating an AI system without a new national AI license.

### KEN-019: beyond_document
Question: From Kenya's March 2025 AI Strategy alone, what was the exact amount collected in 2026 as fines under a new AI Act?
Reference answer (source-based): The 2025 strategy cannot establish a 2026 fine-collection total. It does not itself enact an AI Act or record future payments.
Source: https://www.ict.go.ke/sites/default/files/2025-06/National-AI-Strategy_IMPLEMENTATION.pdf — March 2025 cover and Governance section

**closed:** According to the Kenyan government's March 2025 AI Strategy, the exact amount of fines that would be collected in 2026 for non-compliance with an AI Act (likely referring to the National Information Infrastructure Act) remains unclear without specific details from the current implementation of such legislation.

**context:** The exact amount collected in 2026 as fines under a new AI Act, based on the March 2025 Kenyan AI Strategy, is not provided in the given text.

### NGA-004: document_fact
Question: How many strategic pillars and supporting strategies are stated in Nigeria's September 2025 National AI Strategy?
Reference answer (source-based): Five strategic pillars and 34 strategies.
Source: https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf — PDF page 5 (index 4), strategic pillars overview

**closed:** The Nigerian National Artificial Intelligence (AI) Strategy includes nine strategic pillars and twenty-five supporting strategies.

**context:** Nigeria's September 2025 National AI Strategy includes five strategic pillars and thirty-four supporting strategies.

### NGA-009: proposal_status
Question: What does Nigeria's September 2025 National AI Strategy propose regarding an AI Ethics Expert Group or National AI Ethics Commission?
Reference answer (source-based): It proposes creating a high-level AI Ethics Expert Group or National AI Ethics Commission, not reporting that such a body has already been established.
Source: https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf — PDF page 44 (index 43), objective 4.1, strategy 4.1.1

**closed:** Nigeria's September 2025 National AI Strategy proposes establishing an AI Ethics Expert Group to provide guidance on ethical considerations in AI development and deployment. The strategy also aims to create a National AI Ethics Commission to oversee the implementation of AI policies and regulations.

**context:** Nigeria's September 2025 National AI Strategy proposes the establishment of a High-Level AI Ethics Expert Group/National AI Ethics Commission to oversee and guide the development and implementation of AI ethics policies and practices in the country.

### NGA-015: false_premise
Question: Since Nigeria's National AI Ethics Commission was already issuing binding rulings under the September 2025 National AI Strategy, what article grants it that authority?
Reference answer (source-based): That premise is not established: the strategy proposes creating an ethics group or commission and does not cite an enacted article granting it binding ruling authority.
Source: https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf — PDF page 44 (index 43), strategy 4.1.1

**closed:** The article that grants Nigeria's National AI Ethics Commission (NAIEC) the authority to issue binding rulings on AI ethics is Article 14 of the National AI Strategy, which outlines the framework for AI governance in Nigeria. This article sets out the principles and guidelines for AI development, including ethical considerations.

**context:** The article that grants Nigeria's National AI Ethics Commission the authority to issue binding rulings is Article 14 of its National AI Ethics Commission Act.

### NGA-018: beyond_document
Question: According to Nigeria's September 2025 AI Strategy alone, how many grants did the proposed national AI R&D fund award in calendar year 2026?
Reference answer (source-based): The 2025 strategy alone cannot establish a count for 2026; the fund is proposed as an initiative, not documented as having awarded grants in 2026.
Source: https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf — PDF page 41 (index 40), strategy 3.3.2

**closed:** According to Nigeria's September 2025 AI Strategy, the proposed national AI R&D fund awarded approximately $1 billion in calendar year 2026.

**context:** According to Nigeria's September 2025 AI Strategy, the proposed national AI R&D fund awarded 14 grants in calendar year 2026.
