"""Analyze researcher-adjudicated binary outcomes; never fabricate results."""
import argparse,csv,json,random,statistics
from collections import defaultdict
from pathlib import Path
from .common import BASE

def analyze(rows,reps=3000,seed=2026):
    valid=[];keys=set()
    for r in rows:
        for k in ['correct','supported','status_confusion','appropriate_abstention']:
            if r[k] not in ['0','1']:raise ValueError(f'Nonbinary/unreviewed outcome {k} in {r["id"]}/{r["condition"]}: {r[k]!r}')
        key=(r['id'],r['condition'],r['model'])
        if key in keys:raise ValueError(f'Duplicate review record {key}')
        keys.add(key);valid.append(r)
    by=defaultdict(dict)
    for r in valid:by[(r['model'],r['id'])][r['condition']]=r
    pairs=[v for v in by.values() if set(v)=={'oracle','closed'}]
    if not pairs:raise ValueError('No complete condition pairs')
    rng=random.Random(seed);out={'paired_questions':len(pairs),'models':{}}
    for model in sorted(set(k[0] for k in by)):
        ps=[v for (m,_),v in by.items() if m==model and set(v)=={'oracle','closed'}]
        if not ps:continue
        metric={}
        for name in ['correct','supported','status_confusion','appropriate_abstention']:
            diffs=[int(p['oracle'][name])-int(p['closed'][name]) for p in ps]
            boot=[statistics.mean(rng.choices(diffs,k=len(diffs))) for _ in range(reps)]
            boot.sort();n=len(boot)
            metric[name]={'closed_rate':sum(int(p['closed'][name]) for p in ps)/len(ps),'oracle_rate':sum(int(p['oracle'][name]) for p in ps)/len(ps),'paired_difference':statistics.mean(diffs),'bootstrap_95pct_CI':[boot[int(.025*n)],boot[min(n-1,int(.975*n))]]}
        out['models'][model]={'n_pairs':len(ps),'metrics':metric}
    return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--review',type=Path,default=BASE/'results/review_sheet.csv');p.add_argument('--output',type=Path,default=BASE/'results/summary.json');a=p.parse_args()
 if not a.review.exists():raise SystemExit('Missing completed human review sheet')
 with a.review.open(encoding='utf8',newline='') as f:rows=list(csv.DictReader(f))
 result=analyze(rows);a.output.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()