"""Paired closed-book vs oracle-excerpt model evaluation.
No model request is issued without user-supplied API credentials and local official PDFs.
This is a research instrument, not a completed empirical study.
"""
import argparse, csv, datetime as dt, json, os, pathlib, random, time, urllib.request, urllib.error
from .common import BASE,read_questions,read_sources,sha
from .evidence import extract_relevant_context

SYSTEM=('You are assisting with factual analysis of national AI governance documents. '
        'Treat proposals, future intentions, adopted strategies, binding laws and proven operational implementation as distinct. '
        'Never invent statutory duties, enforcement penalties, implementation results or documents. '
        'If the supplied materials cannot establish an answer, say so, and identify the limitation. '
        'Return one JSON object with keys "answer" (string), "cannot_establish" (boolean), "evidence_reference" (string).')

def make_messages(item,condition,evidence=None):
    # Both arms use identical instruction text; only availability of evidence differs.
    instruction=('Answer the question as accurately as possible. Use any official document excerpt '
                 'provided below as supporting evidence. If no excerpt is supplied, use your '
                 'existing knowledge. In either case, distinguish proposals from enacted laws '
                 'and observed implementation, and abstain when the available information is '
                 'insufficient.\n\n')
    if condition=='oracle':
        assert evidence is not None and evidence.get('text')
        context=f'Official document excerpt (source {item["source_id"]}):\n{evidence["text"]}\n\n'
    else:
        context='Official document excerpt: [NOT PROVIDED]\n\n'
    return [{'role':'system','content':SYSTEM},
            {'role':'user','content':instruction+context+'Question: '+item['question']}]

def chat(endpoint,key,model,messages,temp,max_output,timeout):
    request={'model':model,'messages':messages,'temperature':temp,'max_tokens':max_output}
    data=json.dumps(request).encode()
    req=urllib.request.Request(endpoint,data,{'Content-Type':'application/json','Authorization':f'Bearer {key}'})
    try:
        with urllib.request.urlopen(req,timeout=timeout) as res:
            obj=json.load(res)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'API HTTP {e.code}: {e.read()[:300]!r}') from e
    return obj['choices'][0]['message']['content'],obj.get('usage',{})

def parse_json(text):
    t=text.strip()
    if t.startswith('```'):
        t=t.split('\n',1)[-1].rsplit('```',1)[0].strip()
    try:
        obj=json.loads(t)
        if not isinstance(obj,dict):return None
        if not {'answer','cannot_establish','evidence_reference'}.issubset(obj):return None
        return obj
    except (json.JSONDecodeError,ValueError):return None

def verify_approval(row,evidence,approval_csv):
    if not approval_csv.exists():
        raise ValueError('Missing evidence approval CSV. Download and review official PDFs; run python -m src.audit_evidence first.')
    with approval_csv.open(encoding='utf8',newline='') as f:
        matches=[r for r in csv.DictReader(f) if r['id']==row['id']]
    if len(matches)!=1:
        raise ValueError(f'Missing/duplicate evidence approval for {row["id"]}')
    approval=matches[0]
    if approval.get('reviewer_approved','').strip()!='1' or not approval.get('reviewer_notes','').strip():
        raise ValueError(f'Evidence for {row["id"]} has not been manually approved with reviewer notes.')
    for key,value in (('pdf_sha256',evidence['pdf_sha256']),('excerpt_sha256',evidence['excerpt_sha256']),('pdf_page',str(evidence['page_number_one_based'])),('anchor',row['evidence_anchor'])):
        if approval.get(key)!=value:raise ValueError(f'Stale evidence approval for {row["id"]}: {key} mismatch')


def compute_fingerprint(args):
    params={'model':args.model,'endpoint':args.endpoint,'temperature':args.temperature,'max_output':args.max_output,
            'order_seed':args.order_seed,'question_sha256':sha((BASE/'data/questions.csv').read_bytes()),
            'source_sha256':sha((BASE/'data/sources.json').read_bytes()),'prompt_revision':'v0.2'}
    return sha(json.dumps(params,sort_keys=True).encode('utf8'))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--model',required=True,help='A fixed model ID supported by your endpoint')
    p.add_argument('--endpoint',default='https://api.openai.com/v1/chat/completions')
    p.add_argument('--key-env',default='AI_EVAL_API_KEY')
    p.add_argument('--condition',choices=['both','closed','oracle'],default='both')
    p.add_argument('--max-items',type=int,default=60)
    p.add_argument('--temperature',type=float,default=0)
    p.add_argument('--max-output',type=int,default=350)
    p.add_argument('--timeout',type=int,default=60)
    p.add_argument('--sleep',type=float,default=0.0)
    p.add_argument('--order-seed',type=int,default=2026,help='Deterministic randomised order of model calls')
    p.add_argument('--output',type=pathlib.Path,default=BASE/'results'/'model_outputs.jsonl')
    p.add_argument('--approval-csv',type=pathlib.Path,default=BASE/'results/evidence_anchor_audit.csv')
    p.add_argument('--dry-run',action='store_true',help='Show scope only; no API calls')
    args=p.parse_args()
    rows=read_questions()[:args.max_items]
    conditions=['closed','oracle'] if args.condition=='both' else [args.condition]
    tasks=[(row,condition) for row in rows for condition in conditions]
    random.Random(args.order_seed).shuffle(tasks)
    if args.dry_run:
        print(json.dumps({'model':args.model,'items':len(rows),'conditions':conditions,'planned_calls':len(tasks),'requires_source_pdfs':'oracle' in conditions,'requires_api_key':True},indent=2));return
    key=os.environ.get(args.key_env)
    if not key:raise SystemExit(f'Missing API key in {args.key_env}. No requests were sent.')
    args.output.parent.mkdir(exist_ok=True,parents=True)
    existing=set()
    fingerprint=compute_fingerprint(args)
    if args.output.exists():
        for line in args.output.read_text().splitlines():
            if line.strip():
                old=json.loads(line)
                if old.get('run_fingerprint')!=fingerprint:
                    raise SystemExit('Existing output has a different run fingerprint; use a new --output path. No requests were sent.')
                existing.add((old['id'],old['condition'],old['model']))
    srcs=read_sources()
    # Deterministic randomised condition-item order; each request uses independent context.
    with args.output.open('a',encoding='utf8') as f:
        for row,condition in tasks:
            if (row['id'],condition,args.model) in existing:continue
            evidence=extract_relevant_context(row['source_id'],row['evidence_anchor']) if condition=='oracle' else None
            if condition=='oracle':verify_approval(row,evidence,args.approval_csv)
            messages=make_messages(row,condition,evidence)
            response,usage=chat(args.endpoint,key,args.model,messages,args.temperature,args.max_output,args.timeout)
            rec={'run_fingerprint':fingerprint,'id':row['id'],'country':row['country'],'condition':condition,'model':args.model,'timestamp_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'temperature':args.temperature,'endpoint':args.endpoint,'order_seed':args.order_seed,'request_messages':messages,'raw_response':response,'parsed_response':parse_json(response),'usage':usage,'evidence_meta':{k:v for k,v in (evidence or {}).items() if k!='text'}}
            f.write(json.dumps(rec,ensure_ascii=False)+'\n');f.flush()
            print(f'{row["id"]} {condition}: recorded')
            if args.sleep:time.sleep(args.sleep)
if __name__=='__main__':main()