import csv, hashlib, json, re, unicodedata
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]

def read_questions(path=None):
    with open(path or BASE/'data/questions.csv',encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

def read_sources():
    return {x['id']:x for x in json.loads((BASE/'data/sources.json').read_text(encoding='utf-8'))}

def sha(data): return hashlib.sha256(data).hexdigest()

def normalize(text):
    # Compact ordinary PDF line-wrap hyphenation and compatible ligatures.
    text = re.sub(r'(?<=\w)-\s*\n\s*(?=\w)', '', text)
    text = unicodedata.normalize('NFKC', text).casefold()
    return ' '.join(re.findall(r'\w+', text))