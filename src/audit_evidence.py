"""Evidence-page audit to be run after PDFs are locally fetched.
Machine matching is NOT a substitute for source verification by a researcher.
"""
import csv
from .common import BASE,read_questions,normalize
from .evidence import extract_relevant_context

def main():
    out=BASE/'results'/'evidence_anchor_audit.csv';out.parent.mkdir(exist_ok=True)
    fields=['id','source_id','locator','anchor','pdf_page','pdf_sha256','excerpt_sha256','anchor_exact','selected_text_first_180_chars','reviewer_approved','reviewer_notes']
    with out.open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fields);w.writeheader()
        for r in read_questions():
            e=extract_relevant_context(r['source_id'],r['evidence_anchor'])
            w.writerow(dict(id=r['id'],source_id=r['source_id'],locator=r['evidence_locator'],anchor=r['evidence_anchor'],pdf_page=e['page_number_one_based'],pdf_sha256=e['pdf_sha256'],excerpt_sha256=e['excerpt_sha256'],anchor_exact=int(e['retrieval_score']>=1000),selected_text_first_180_chars=e['text'][:180],reviewer_approved='',reviewer_notes=''))
    print('Written',out,': requires independent manual page/excerpt review.')
if __name__=='__main__':main()