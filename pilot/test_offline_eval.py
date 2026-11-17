import unittest
from pilot.offline_eval import load_items,messages

class OfflinePilotTests(unittest.TestCase):
    def test_balanced_items(self):
        rows=load_items()
        self.assertEqual(len(rows),12)
        self.assertEqual({c:len([x for x in rows if x['country']==c]) for c in ['Rwanda','Kenya','Nigeria']},dict.fromkeys(['Rwanda','Kenya','Nigeria'],4))
        self.assertEqual(len({x['id'] for x in rows}),12)
        for x in rows:
            for field in ['reference_answer','context_fact','source','source_locator','trace','rubric']:
                self.assertTrue(x[field])
    def test_paired_prompt_no_leakage(self):
        for r in load_items():
            closed=messages(r,'closed'); context=messages(r,'context')
            self.assertEqual(closed[0],context[0])
            self.assertIn(r['question'],closed[1]['content'])
            self.assertIn(r['question'],context[1]['content'])
            self.assertNotIn(r['context_fact'],closed[1]['content'])
            self.assertIn(r['context_fact'],context[1]['content'])
if __name__=='__main__':unittest.main()