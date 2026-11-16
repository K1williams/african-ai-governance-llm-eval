from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT,TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path

OUTPUT=Path(__file__).resolve().parents[1]/'AI_Governance_LLM_Evaluation_Study_Protocol_v0.1.pdf'
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if Path(font).exists():
 pdfmetrics.registerFont(TTFont('DejaVu',font));pdfmetrics.registerFont(TTFont('DejaVu-Bold',bold));reg='DejaVu';strong='DejaVu-Bold'
else:reg='Helvetica';strong='Helvetica-Bold'
navy=HexColor('#172A45');black=HexColor('#273448');gray=HexColor('#657283');light=HexColor('#E2E8F0');accent=HexColor('#155E75')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Top',fontName=strong,fontSize=9,leading=13,textColor=accent,spaceAfter=8))
styles.add(ParagraphStyle(name='Hero',fontName=strong,fontSize=21,leading=28,textColor=navy,spaceAfter=12))
styles.add(ParagraphStyle(name='Sub',fontName=reg,fontSize=10.6,leading=16,textColor=gray,spaceAfter=15))
styles.add(ParagraphStyle(name='H',fontName=strong,fontSize=12.5,leading=17,textColor=navy,spaceBefore=14,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name='P',fontName=reg,fontSize=9,leading=14.2,textColor=black,spaceAfter=8))
styles.add(ParagraphStyle(name='Note',fontName=reg,fontSize=8,leading=12,textColor=gray,spaceAfter=7))
styles.add(ParagraphStyle(name='Small',fontName=reg,fontSize=8.4,leading=13,textColor=black,spaceAfter=6))
styles.add(ParagraphStyle(name='TableHead',fontName=strong,fontSize=8,leading=11,textColor=navy))
styles.add(ParagraphStyle(name='TableBody',fontName=reg,fontSize=8,leading=12,textColor=black))

def pp(x,style='P'):return Paragraph(x,styles[style])
def section(h,t):return [pp(h,'H'),pp(t)]
def paged(canvas,doc):
 canvas.saveState();w,h=A4
 canvas.setStrokeColor(light);canvas.line(20*mm,19*mm,w-20*mm,19*mm)
 canvas.setFont(reg,7);canvas.setFillColor(gray)
 canvas.drawString(20*mm,14*mm,'INDEPENDENT RESEARCH PILOT | Protocol v0.1 | 15 Nov 2026')
 canvas.drawRightString(w-20*mm,14*mm,f'Page {doc.page}')
 canvas.restoreState()
doc=SimpleDocTemplate(str(OUTPUT),pagesize=A4,leftMargin=21*mm,rightMargin=21*mm,topMargin=20*mm,bottomMargin=24*mm,title='AI Governance LLM Evaluation Study — Protocol v0.1',author='Provisional project: Williams Stonard Kaphika')
story=[]
story +=[pp('RESEARCH PROTOCOL / IMPLEMENTATION STATUS','Top'), pp('When AI Reads AI Governance','Hero'),pp('Evaluating factual accuracy, source grounding, and policy–law confusion in language-model answers about African national AI frameworks','Sub')]
story +=[pp('<b>Primary research question.</b> To what extent does providing verifiable excerpts from official AI governance documents change the factual accuracy, evidential support and appropriate expression of uncertainty in LLM responses, compared with responses produced without those documents?')]
story +=[pp('Experimental unit and scope','H')]
story +=[pp('Sixty source-linked draft questions based on official government documents from Rwanda, Kenya and Nigeria. The task is document-grounded question answering, not a legal determination of the current national regulatory landscape. This project is independent of TPP RAIDA and ARAPI.')]
rows=[['Measure','Current status'],['Source documents','3 official documents identified'],['Question set','60 draft items; 20 per country'],['Question classes','42 answerable · 9 false premise · 9 unanswerable'],['Code verification','Five local automated tests passed'],['Actual model responses','0 — model run not yet executed'],['Expert annotation','Not yet independently reviewed']]
t=Table([[pp(z,'TableHead' if i==0 else 'TableBody') for z in row] for i,row in enumerate(rows)],colWidths=[56*mm,106*mm],repeatRows=1,hAlign='LEFT')
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#EFF4F7')),('LINEBELOW',(0,0),(-1,0),.7,light),('LINEBELOW',(0,1),(-1,-1),.25,light),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
story += [t]
story += section('Why the distinction matters','An AI system that treats a proposal to establish an AI regulator as proof of an operational authority, or describes a national strategy as a law imposing fines, may mislead institutional policy analysis. The study isolates these failure modes and records when a document cannot establish a requested fact.')
story +=[PageBreak(),pp('METHODS','Top'),pp('Controlled paired evaluation','Hero')]
story+=section('Conditions','<b>A: Closed-book.</b> The model answers without an official excerpt, with instructions to be accurate and avoid speculation. <b>B: Oracle-evidence.</b> The same model and instructions receive a selected excerpt from the official source PDF. Evidence is chosen by a question-specific anchor, and each selected paragraph requires manual review. The oracle condition is not a production retrieval system.')
story+=section('Controls','Pin model identifier and provider, temperature, token budget, prompt template, question wording and run date. Use stateless API calls and a deterministic random order of condition-by-item requests. Log exact requests and responses, PDF page locations, source hashes, usage and model identifiers.')
story+=section('Scoring and analysis','Primary endpoint: human-adjudicated factual correctness per response, paired by question. Secondary endpoints: document support, policy-status confusion (lower is better) and appropriate abstention. Compare within-question differences and report descriptive paired-bootstrap confidence intervals. Include country-level descriptive breakdowns; do not generalise from three purposively selected countries to the continent.')
story+=section('Four pre-specified hypotheses','<b>H1/H2:</b> Official evidence increases factual correctness and support. <b>H3:</b> Evidence reduces mistaken claims that proposals are implemented or that strategy recommendations are legally binding. <b>H4:</b> Evidence improves uncertainty handling when the chosen document cannot substantiate an answer.')
story+=section('Credibility safeguards','Draft questions need independent answer-key adjudication and source-span checking. Any ambiguous or unsupported items must be corrected before model runs, with changes logged. Reviewers should initially be blinded to the source condition where feasible, and disputes should be recorded. Claims about unseen laws, penalties or implementation must not be inferred from a source document’s silence.')
story +=[PageBreak(),pp('DOCUMENTATION AND EXECUTION','Top'),pp('Evidence and next verification gates','Hero')]
story +=[pp('Sources','H'),pp('<b>Rwanda:</b> National AI Policy, Ministry of ICT and Innovation. <b>Kenya:</b> AI Strategy 2025–2030, Ministry of Information, Communications and the Digital Economy. <b>Nigeria:</b> National AI Strategy (September 2025), hosted by the National Centre for AI and Robotics / NITDA. Exact official URLs are recorded in the source manifest and README; the government PDFs are not redistributed.')]
story +=[pp('Next gates before any empirical claim','H'),pp('1. Download three PDFs on an internet-enabled machine; calculate hashes and verify all selected evidence anchors against original pages.<br/>2. Audit the 60 draft questions for correctness, diversity and answerability; seek independent review of a stratified sample.<br/>3. Run a 10-question API pilot on a pinned model; inspect JSON conformity, model cost and evidence selection.<br/>4. Run the 60-item, two-condition comparison and independently grade its 120 answers.<br/>5. Compute paired analysis and document examples, failure modes and sensitivity tests.')]
story +=[pp('Related research','H'),pp('Mathur et al. (2026), <i>Retrieval Improvements Do Not Guarantee Better Answers: A Study of RAG for AI Policy QA</i> (arXiv:2603.24580); Das et al. (2026), <i>How Much Do Legal RAG Systems Still Hallucinate?</i> (arXiv:2608.14210); Magesh et al. (2024), <i>Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools</i> (arXiv:2405.20362). The related literature prevents claiming the general problem is new; novelty, if any, must be shown empirically.')]
story +=[pp('Boundary of the current deliverable','H'),pp('<b>This is a draft protocol and tested software scaffold, not an evaluated model or published scientific result.</b> The dataset was drafted with AI assistance and source-screened using official online texts. The model study has not been executed, the official PDF excerpts have not yet been batch-verified locally, and independent annotation is pending. A public claim of reproducible results would be premature.')]
story +=[Spacer(1,6*mm),pp('Provisional project owner: Williams Stonard Kaphika | Independent research','Note')]
doc.build(story,onFirstPage=paged,onLaterPages=paged)
print(OUTPUT)