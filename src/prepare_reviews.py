"""Generate manual human adjudication sheet. DO NOT substitute an LLM self-judge."""
import argparse,csv,json
from pathlib import Path
from .common import read_questions,BASE

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=BASE/'results/model_outputs.jsonl');p.add_argument('--output',type=Path,default=BASE/'results/review_sheet.csv');a=p.parse_args()
 if not a.input.exists():raise SystemExit('No model outputs. Run evaluation first.')
 gold={r['id']:r for r in read_questions()}
 fields=['id','country','condition','model','question','answerability','reference_answer','evidence_locator','source_url','source_pdf_page','source_excerpt','model_answer','correct','supported','status_confusion','appropriate_abstention','reviewer','notes']
 with a.output.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fields);w.writeheader()
  for line in a.input.read_text(encoding='utf8').splitlines():
   if not line.strip():continue
   r=json.loads(line);g=gold[r['id']];ans=r.get('parsed_response') or {}
   w.writerow(dict(id=r['id'],country=r['country'],condition=r['condition'],model=r['model'],question=g['question'],answerability=g['answerability'],reference_answer=g['reference_answer'],evidence_locator=g['evidence_locator'],source_url=g['source_url'],source_pdf_page=(r.get('evidence_meta') or {}).get('page_number_one_based',''),source_excerpt=(r['request_messages'][-1]['content'].split('Official document excerpt (source '+g['source_id']+'):\n',1)[-1].split('\n\nQuestion:',1)[0] if r['condition']=='oracle' else ''),model_answer=ans.get('answer',r['raw_response']),correct='',supported='',status_confusion='',appropriate_abstention='',reviewer='',notes=''))
 print('Created',a.output,'with UNGRADED responses')
if __name__=='__main__':main()