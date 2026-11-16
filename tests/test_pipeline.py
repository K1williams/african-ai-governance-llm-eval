import unittest, json, tempfile, os
from unittest.mock import patch
import fitz
from pathlib import Path
from src.common import read_questions,normalize
from src.validate_dataset import validate
from src.run_eval import make_messages,parse_json
from src.score import analyze
from src import evidence

class TestPipeline(unittest.TestCase):
 def test_dataset(self):
  problems,by,labels=validate();self.assertEqual(problems,[]);self.assertEqual(dict(by),{'RWA':20,'KEN':20,'NGA':20});self.assertEqual(labels['answerable'],42);self.assertEqual(labels['false_premise'],9);self.assertEqual(labels['unanswerable'],9)
 def test_no_gold_leakage(self):
  for r in read_questions():
   for c in ['closed','oracle']:
    msg=make_messages(r,c,{'text':'A retrieved text snippet'})
    self.assertNotIn(r['reference_answer'],msg[1]['content'])
 def test_json_parse(self):
  self.assertEqual(parse_json('{"answer":"ok","cannot_establish":false,"evidence_reference":"RWA"}')['answer'],'ok')
  self.assertIsNone(parse_json('nope'))
 def test_bootstrap(self):
  rows=[]
  for i in range(3):
   for cond in ['closed','oracle']:
    rows.append({'id':str(i),'model':'test','condition':cond,'correct':str(int(cond=='oracle')),'supported':'1','status_confusion':'0','appropriate_abstention':'0'})
  r=analyze(rows,reps=100,seed=1);self.assertEqual(r['models']['test']['metrics']['correct']['paired_difference'],1.0)
 def test_evidence_page_selection_with_synthetic_pdf(self):
  # Test runtime extraction only; these are synthetic pages, not government sources.
  with tempfile.TemporaryDirectory() as t:
   path=Path(t)/'RWA.pdf'; d=fitz.open()
   page=d.new_page();page.insert_text((72,72),'Cover and introduction')
   page=d.new_page();page.insert_text((72,72),'Proposal to establish a Responsible AI Office within MINICT.')
   d.save(str(path));d.close()
   with patch.object(evidence,'CACHE',Path(t)):
    got=evidence.extract_relevant_context('RWA','Responsible AI Office')
   self.assertEqual(got['page_number_one_based'],2)
   self.assertIn('Responsible AI Office',got['text'])
 def test_normalize(self):
  self.assertIn('office',normalize('OFFICE'))
if __name__=='__main__':unittest.main()

class TestReleaseHardening(unittest.TestCase):
 def test_missing_anchor_fails_closed(self):
  with tempfile.TemporaryDirectory() as t:
   path=Path(t)/'RWA.pdf'; doc=fitz.open();page=doc.new_page();page.insert_text((72,72),'The proposal is not an enacted law.');doc.save(str(path));doc.close()
   with patch.object(evidence,'CACHE',Path(t)):
    with self.assertRaisesRegex(ValueError,'Anchor NOT matched'):
     evidence.extract_relevant_context('RWA','completely unrelated regulator mandate')
 def test_oracle_requires_approved_exact_evidence(self):
  import csv
  from src.run_eval import verify_approval
  item=next(r for r in read_questions() if r['id']=='RWA-001')
  meta={'pdf_sha256':'f'*64,'excerpt_sha256':'e'*64,'page_number_one_based':1}
  with tempfile.TemporaryDirectory() as t:
   path=Path(t)/'review.csv';fields=['id','pdf_sha256','excerpt_sha256','pdf_page','anchor','reviewer_approved','reviewer_notes']
   def save(approved,hashval):
    with path.open('w',newline='') as f:
     w=csv.DictWriter(f,fields);w.writeheader();w.writerow({'id':item['id'],'pdf_sha256':hashval,'excerpt_sha256':meta['excerpt_sha256'],'pdf_page':'1','anchor':item['evidence_anchor'],'reviewer_approved':approved,'reviewer_notes':'Checked original PDF'})
   save('0','f'*64)
   with self.assertRaisesRegex(ValueError,'not been manually approved'): verify_approval(item,meta,path)
   save('1','a'*64)
   with self.assertRaisesRegex(ValueError,'Stale evidence approval'): verify_approval(item,meta,path)
   save('1','f'*64)
   verify_approval(item,meta,path)
 def test_run_fingerprint_changes_with_model(self):
  from types import SimpleNamespace
  from src.run_eval import compute_fingerprint
  base=dict(model='a',endpoint='https://example.invalid',temperature=0,max_output=350,order_seed=2026)
  a=compute_fingerprint(SimpleNamespace(**base))
  b=compute_fingerprint(SimpleNamespace(**dict(base,model='b')))
  self.assertNotEqual(a,b)
 def test_all_question_sources_match(self):
  from src.common import read_sources
  sources=read_sources()
  for r in read_questions():self.assertEqual(r['source_url'],sources[r['source_id']]['official_url'])