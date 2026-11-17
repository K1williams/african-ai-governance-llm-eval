"""Small, explicitly exploratory, paired evaluation of a public open-weight LLM.

Not a substitute for the study's full PDF-grounded arm or blinded human review.
No real-world legal status conclusions are inferred from the scores.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / 'pilot'


def load_items():
    return json.loads((PILOT / 'items.json').read_text(encoding='utf-8'))


def messages(row, condition):
    system = ("You answer questions about historical national AI policy documents. "
              "Distinguish recommendations and planned institutions from binding laws and verified operations. "
              "Do not invent enforcement figures or legal powers. If a dated source cannot establish the answer, "
              "say so. Give a short answer.")
    if condition == 'context':
        context = ('Verified, researcher-curated SOURCE FACT SUMMARY (not a verbatim PDF quotation): '
                   + row['context_fact'] + '\n')
    else:
        context = 'No source summary is provided.\n'
    return [{'role': 'system', 'content': system},
            {'role': 'user', 'content': context + 'Question: ' + row['question']}]


def render_report(records, model, revision, out):
    table = { (r['id'], r['condition']): r for r in records }
    items = load_items()
    lines = [
        '# Exploratory open-weight model evaluation: raw responses', '',
        '> This file reports observed model outputs, **not human-adjudicated accuracy**. '
        'A small weak baseline model and fact summaries rather than verbatim PDFs were used. '
        'Do not cite as a validated benchmark or make legal-status assertions from model responses.', '',
        f'- Model: `{model}`', f'- Resolved model revision: `{revision}`',
        '- Deterministic decoding (`do_sample=False`, `max_new_tokens=128`); temperature not applicable.',
        f'- Complete question pairs: {sum((i["id"],"closed") in table and (i["id"],"context") in table for i in items)} / {len(items)}',
        '- Conditions: no source facts vs researcher-verified policy fact summary; identical questions and general instruction.',
        '- Data are **descriptive observations**, not numerical factual-accuracy claims.',
        '', '## Per-question outputs', ''
    ]
    for item in items:
        lines.extend([f'### {item["id"]}: {item["type"]}',
                      f'Question: {item["question"]}',
                      f'Reference answer (source-based): {item["reference_answer"]}',
                      f'Source: {item["source"]} — {item["source_locator"]}', ''])
        for cond in ['closed','context']:
            res=table.get((item['id'],cond))
            lines.append(f'**{cond}:** '+(res['response'].replace('\n',' ').replace('|','\\|') if res else '*not run*'))
            lines.append('')
    out.write_text('\n'.join(lines),encoding='utf-8')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--model', default='Qwen/Qwen2.5-0.5B-Instruct')
    parser.add_argument('--max-new-tokens',type=int,default=128)
    parser.add_argument('--max-items',type=int,default=12)
    parser.add_argument('--output',type=Path,default=PILOT/'observations.jsonl')
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    items=load_items()[:args.max_items]
    if args.dry_run:
        print(json.dumps({'model':args.model,'questions':len(items),'planned_inferences':len(items)*2,'conditions':['closed','context']},indent=2))
        return
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    torch.set_num_threads(2)
    tokenizer=AutoTokenizer.from_pretrained(args.model,trust_remote_code=False)
    model=AutoModelForCausalLM.from_pretrained(args.model,torch_dtype=torch.float32,trust_remote_code=False).eval()
    revision=model.config._commit_hash or 'not-reported-by-provider'
    tasks=[(r,c) for r in items for c in ['closed','context']]
    random.Random(2026).shuffle(tasks)
    records=[]
    for row,condition in tasks:
        chat=messages(row,condition)
        prompt=tokenizer.apply_chat_template(chat,tokenize=False,add_generation_prompt=True)
        enc=tokenizer(prompt,return_tensors='pt',truncation=True,max_length=2048)
        with torch.inference_mode():
            generated=model.generate(**enc,max_new_tokens=args.max_new_tokens,do_sample=False,pad_token_id=tokenizer.eos_token_id)
        response=tokenizer.decode(generated[0,enc.input_ids.shape[-1]:],skip_special_tokens=True).strip()
        record={'id':row['id'],'country':row['country'],'type':row['type'],'condition':condition,
                'question':row['question'],'response':response,'model':args.model,'resolved_revision':revision,
                'prompt_sha256':hashlib.sha256(prompt.encode('utf8')).hexdigest(),
                'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'max_new_tokens':args.max_new_tokens,'greedy_decoding':True}
        records.append(record)
        print(f'{row["id"]} {condition}: {len(response)} chars',flush=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in records)+'\n',encoding='utf8')
    render_report(records,args.model,revision,args.output.parent/'OBSERVED_RESPONSES.md')
    print(f'Wrote {len(records)} observations to {args.output}')

if __name__=='__main__':main()