import collections
from .common import read_questions,read_sources

def validate(rows=None):
    rows=rows if rows is not None else read_questions()
    srcs=read_sources(); problems=[]; seen=set(); by=collections.Counter(); labels=collections.Counter()
    for r in rows:
        id=r['id']; by[r['source_id']]+=1; labels[r['answerability']]+=1
        if id in seen:problems.append(f'duplicate {id}')
        seen.add(id)
        if r['source_id'] not in srcs: problems.append(f'{id} invalid source')
        elif r['source_url'] != srcs[r['source_id']]['official_url']:problems.append(f'{id} URL mismatch')
        if r['answerability'] not in {'answerable','false_premise','unanswerable'}:problems.append(f'{id} invalid class')
        for key in ('question','reference_answer','evidence_anchor','evidence_locator','error_category','review_status'):
            if not r.get(key,'').strip():problems.append(f'{id} missing {key}')
    if len(rows)!=60: problems.append(f'expected 60 draft items, got {len(rows)}')
    for c in srcs:
        if by[c]!=20:problems.append(f'{c} has {by[c]} not 20')
    return problems,by,labels

def main():
    problems,by,labels=validate()
    print('Counts:',dict(by),'Answerability:',dict(labels),'Errors:',len(problems))
    for p in problems:print('ERROR:',p)
    if problems:raise SystemExit(1)
if __name__=='__main__':main()