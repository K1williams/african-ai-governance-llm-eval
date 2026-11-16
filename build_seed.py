"""AI-assisted preliminary questions, source-screened against official documents on 15 Nov 2026.
Not an independently validated benchmark. Delete/replace this generation script once adjudicated.
"""
import csv,json,pathlib
ROOT=pathlib.Path(__file__).parent
# fields: question, gold answer (for answerable), type, official-document anchor, locator, error taxonomy
D={
'RWA':[
('Which ministry is named on Rwanda’s National AI Policy cover?','Ministry of ICT and Innovation','answerable','Ministry of ICT and Innovation','Cover','institution'),
('How does Rwanda’s National AI Policy describe its purpose?','It is a roadmap for harnessing AI benefits while mitigating associated risks.','answerable','serves as a roadmap','Executive Summary','policy_status'),
('Which two Rwandan bodies developed the National AI Policy?','MINICT and RURA.','answerable','developed by MINICT and RURA','Executive Summary','institution'),
('What is Rwanda’s stated vision for AI research and innovation?','To become a global centre for AI research and innovation.','answerable','global center for AI','Executive Summary','objective'),
('How many priority policy areas does Rwanda’s policy identify?','Six.','answerable','Six priority policy areas','Executive Summary','quantity'),
('How many key policy recommendations are described in the Rwanda policy?','Fourteen.','answerable','14 key policy recommendations','Highlights','quantity'),
('What is recommended to improve access to AI-ready data in Rwanda?','A multi-sectoral task force to develop data governance frameworks and data-sharing protocols.','answerable','multi-sectoral task force','Recommendation 7','planned_vs_operational'),
('Which two areas of AI adoption are distinguished between public and private sectors?','Trustworthy adoption in the public sector and widely beneficial adoption in the private sector.','answerable','Trustworthy AI Adoption','Six Priority Areas','objective'),
('What is recommended for benchmarking Rwanda’s AI competitiveness?','An annual AI Readiness Index developed through international collaboration.','answerable','annual ‘AI Readiness Index’','Recommendation 9','planned_vs_operational'),
('What body does the policy recommend creating within MINICT to coordinate its implementation?','A Responsible AI Office (RAIO).','answerable','Responsible AI Office','Highlights','planned_vs_operational'),
('Which regulator is described as leading promotion of Rwanda’s AI ethical guidelines?','RURA.','answerable','led by RURA','Recommendation 13','institution'),
('Which five sectors are highlighted for responsible AI adoption in Rwanda?','Healthcare; banking and digital payments; e-commerce and trade; transportation; agriculture.','answerable','Healthcare','Sectoral deep-dive','sector'),
('What mechanism is proposed to advise government and industry on AI in Rwanda?','A Presidential Council on AI consisting of academic and industry leaders.','answerable','Presidential Council on AI','Recommendation 11','planned_vs_operational'),
('What network does Rwanda’s policy recommend creating across government institutions to champion ethical AI?','A network of AI Ethics Officers across government institutions.','answerable','network of AI Ethics Officers','Recommendation 13','institution'),
('Since Rwanda’s Responsible AI Office is already fully operational according to this policy, what are its reported audit results?','The policy proposes establishing the office; it does not provide operational audit results.','false_premise','Proposal to establish a Responsible AI Office','Highlights','planned_vs_operational'),
('Which binding prison sentence does Rwanda’s National AI Policy impose for failure to adopt AI?','The policy is a roadmap and does not itself specify such a criminal sentence.','false_premise','serves as a roadmap','Executive Summary','policy_vs_law'),
('What amount of mandatory AI licensing fees has Rwanda already collected under the National AI Policy?','No collection figure is documented in the cited policy; it cannot establish that any fee was collected.','false_premise','Implementation Plan Summary','Implementation Plan Summary','implementation_overclaim'),
('Which private company received the first AI licence under Rwanda’s policy?','Not established by the cited policy document.','unanswerable','National AI Policy','Cover','unsupported_inference'),
('How many enforcement actions occurred under Rwanda’s AI policy in 2026?','Not established by the cited policy document.','unanswerable','Implementation Plan Summary','Implementation Plan Summary','implementation_overclaim'),
('What was Rwanda’s exact AI funding expenditure in October 2026?','Not established by the cited policy document.','unanswerable','Implementation Plan Summary','Implementation Plan Summary','out_of_scope'),
],
'KEN':[
('What date range appears in the title of Kenya’s national AI strategy?','2025–2030.','answerable','KENYA ARTIFICIAL INTELLIGENCE STRATEGY 2025-2030','Cover','quantity'),
('What is the date printed on the Kenya AI Strategy?','March 2025.','answerable','March 2025','Cover','date'),
('What are the three principal pillars of Kenya’s AI strategy?','AI digital infrastructure; data; AI research and innovation.','answerable','three key pillars','Executive Summary','objective'),
('How many cross-cutting enablers support the strategy’s pillars?','Four.','answerable','four enablers','Executive Summary','quantity'),
('What are the four cross-cutting enablers in the Kenya strategy?','Governance; talent development; investment; ethics, equity and inclusion.','answerable','cross-cutting enablers','Executive Summary','objective'),
('What is the infrastructure pillar intended to improve?','Access to affordable, modern AI digital infrastructure.','answerable','AI digital infrastructure','Executive Summary','objective'),
('What is the data pillar intended to establish?','A robust and sustainable data ecosystem for AI and innovation.','answerable','second pillar, data','Executive Summary','objective'),
('What is the R&D pillar intended to advance?','Localised AI model research, innovation and commercialisation.','answerable','third pillar, AI research and innovation','Executive Summary','objective'),
('Which major safeguards does Kenya’s strategy mention for AI deployment?','Data sovereignty, cybersecurity and ethical oversight.','answerable','data sovereignty','Executive Summary','governance'),
('Name three priority use sectors for AI adoption in the strategy.','Any three of agriculture, security, healthcare, education and public service delivery.','answerable','agriculture, security, healthcare','Executive Summary','sector'),
('Which stakeholder groups contributed to drafting Kenya’s strategy?','Government, private sector, academia, civil society, international partners and local communities.','answerable','extensive consultations','Executive Summary','institution'),
('Which stakeholders does the strategy assign the lead in AI R&D?','Academia is identified as advancing AI research.','answerable','academia will advance research','Executive Summary','institution'),
('What does the strategy propose to track implementation progress?','A monitoring and evaluation framework.','answerable','monitoring and evaluation framework','Executive Summary','planned_vs_operational'),
('Does Kenya’s strategy describe developing a national AI policy as a milestone or as an already completed legislative act?','As a future implementation milestone.','answerable','developing a national AI policy','Executive Summary','planned_vs_operational'),
('As Kenya’s AI strategy already enacts a new AI Act, what fine does that Act prescribe?','The strategy is not itself an AI Act and does not set such a fine.','false_premise','developing a national AI policy','Executive Summary','policy_vs_law'),
('Which existing independent AI regulator was fully operationalised by publication of Kenya’s strategy?','The cited text proposes governance improvements; it does not verify that such a regulator was fully operationalised.','false_premise','agile and dynamic governance framework','Executive Summary','implementation_overclaim'),
('According to Kenya’s strategy, which compulsory AI examination has every civil servant already passed?','The strategy promotes training and capacity building; it does not document such an examination or universal completion.','false_premise','Talent development','Executive Summary','implementation_overclaim'),
('How many AI safety incidents were officially recorded nationwide in Kenya in September 2026?','Not established by this strategy.','unanswerable','risk analysis and mitigation','Table of Contents','out_of_scope'),
('What was the total value of fines collected under a Kenya AI Act in 2026?','Not established by this strategy.','unanswerable','governance framework','Executive Summary','out_of_scope'),
('Which company won Kenya’s largest national AI procurement contract in October 2026?','Not established by this strategy.','unanswerable','private-sector actors will drive innovation','Executive Summary','out_of_scope'),
],
'NGA':[
('What is the publication month and year on Nigeria’s National AI Strategy?','September 2025.','answerable','SEPTEMBER, 2025','Cover','date'),
('How does Nigeria’s strategy characterize itself?','A living document guiding national AI adoption for socio-economic change.','answerable','living document','Executive Summary','policy_status'),
('What is the stated overall vision of Nigeria’s AI strategy?','Global AI leadership through ethical, inclusive innovation, local talent and strategic collaboration for sustainable development.','answerable','global leader in AI','Executive Summary','objective'),
('How many strategic pillars underpin Nigeria’s National AI Strategy?','Five.','answerable','5 strategic pillars','Executive Summary','quantity'),
('How many strategies are described as supporting its five pillars?','Thirty-four.','answerable','34 strategies','Executive Summary','quantity'),
('What is the first pillar of Nigeria’s AI strategy?','Building foundational AI infrastructure.','answerable','Building Foundational AI Infrastructure','Executive Summary','objective'),
('What is the third pillar of Nigeria’s AI strategy?','Accelerating AI adoption and sector transformation.','answerable','Accelerating AI Adoption and Sector Transformation','Executive Summary','objective'),
('What is the fifth pillar of Nigeria’s AI strategy?','Developing a robust AI governance framework.','answerable','Developing a Robust AI Governance Framework','Executive Summary','objective'),
('Which expert group or commission does the strategy propose for AI ethics?','A high-level AI Ethics Expert Group or National AI Ethics Commission.','answerable','Create a High-Level AI Ethics Expert Group','Pillar 4 / Objective 4.1','planned_vs_operational'),
('Which four factors are named in Nigeria’s discussion of AI risk assessment?','Accuracy, bias, transparency and governance.','answerable','fourfold: accuracy, bias, transparency, and governance','Mitigating AI Risks','governance'),
('What are the three trade-offs discussed in Nigeria’s strategy?','Innovation versus regulation; individual versus state; transparency versus system vulnerability.','answerable','three primary AI trade-offs','Trade-offs','governance'),
('What public–private data-sharing initiative does Nigeria’s strategy propose?','An Open Data Initiative (ODI).','answerable','Open Data Initiative','Objective 3.2','planned_vs_operational'),
('What research funding programme does Nigeria’s AI strategy propose?','A National AI Research and Development Fund.','answerable','National AI Research and Development (R&D) Fund','Objective 3.3','planned_vs_operational'),
('Which national network is proposed to improve research and education connectivity?','A National Research and Education Network (NREN).','answerable','National Research and Education Network','Objective 3.3','planned_vs_operational'),
('Since Nigeria’s proposed National AI Ethics Commission is already issuing binding rulings, what is its first ruling?','The strategy proposes creating a commission; it provides no evidence of binding rulings.','false_premise','Create a High-Level AI Ethics Expert Group','Pillar 4 / Objective 4.1','planned_vs_operational'),
('What imprisonment penalty does Nigeria’s National AI Strategy legally impose on AI developers?','A strategic document is not itself a penal statute, and no such punishment is specified in the cited material.','false_premise','living document','Executive Summary','policy_vs_law'),
('Since the National AI R&D Fund is already disbursing grants, which applicant received its first award?','The cited strategy proposes the fund and does not document the first award.','false_premise','Develop a National AI Research and Development (R&D) Fund','Objective 3.3','planned_vs_operational'),
('How many audited AI providers were fined by Nigeria’s AI regulator in 2026?','Not established by the cited strategy.','unanswerable','Developing a Robust AI Governance Framework','Executive Summary','out_of_scope'),
('What was the exact October 2026 budget spent on training Nigerian AI ethics auditors?','Not established by the cited strategy.','unanswerable','Develop National AI Ethical Principles','Pillar 4 / Objective 4.1','out_of_scope'),
('Which firm currently administers every Nigerian government AI system?','Not established by the cited strategy.','unanswerable','Accelerating AI Adoption and Sector Transformation','Executive Summary','out_of_scope'),
]
}
urls={
'RWA':('Rwanda','Rwanda National AI Policy','https://www.minict.gov.rw/fileadmin/user_upload/minict_user_upload/Documents/Policies/Artificial_Intelligence_Policy.pdf','official policy, not an AI penal statute'),
'KEN':('Kenya','Kenya AI Strategy 2025–2030','https://ict.go.ke/sites/default/files/2025-06/National-AI-Strategy_IMPLEMENTATION.pdf','government strategy, launched March 2025'),
'NGA':('Nigeria','Nigeria National AI Strategy (September 2025)','https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf','government-published strategy; not itself a binding AI statute'),
}
(ROOT/'data'/'sources.json').write_text(json.dumps([{'id':k,'country':v[0],'title':v[1],'official_url':v[2],'document_classification':v[3],'retrieved_for_review':'2026-11-15','sha256':None} for k,v in urls.items()],indent=2,ensure_ascii=False))
fields=['id','country','source_id','question','answerability','reference_answer','error_category','evidence_anchor','evidence_locator','source_url','review_status']
with (ROOT/'data'/'questions.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fields);w.writeheader()
 for c,rows in D.items():
  for i,(q,a,t,anchor,locator,tag) in enumerate(rows,1):
   w.writerow(dict(id=f'{c}-{i:03}',country=urls[c][0],source_id=c,question=q,answerability=t,reference_answer=a,error_category=tag,evidence_anchor=anchor,evidence_locator=locator,source_url=urls[c][2],review_status='ai_assisted_source_screened_independent_review_pending'))
print('Wrote',sum(len(v) for v in D.values()),'questions')