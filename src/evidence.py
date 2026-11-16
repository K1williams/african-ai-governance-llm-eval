"""Oracle evidence context from official PDFs fetched on user's machine.
This is NOT a realistic retrieval system; excerpt selection is curated per item.
"""
from pathlib import Path
import re
import fitz
import requests
from .common import BASE, read_sources, normalize, sha

CACHE=BASE/'data'/'source_pdfs'

def fetch_source(source_id,timeout=60):
    src=read_sources()[source_id]
    CACHE.mkdir(parents=True,exist_ok=True)
    dest=CACHE/f'{source_id}.pdf'
    if dest.exists() and dest.stat().st_size>1000:
        return dest
    response=requests.get(src['official_url'],timeout=timeout,headers={'User-Agent':'AI-Governance-Evaluation-Research/0.1'})
    response.raise_for_status()
    b=response.content
    if not b.startswith(b'%PDF'):
        raise ValueError(f'Source {source_id} is not a PDF; got {response.headers.get("Content-Type")}')
    dest.write_bytes(b)
    return dest

def extract_relevant_context(doc_id,anchor,words=450):
    """Select an excerpt only if the normalized anchor is present verbatim.

    An unmatched anchor is a reproducibility failure, not a cue for a
    misleading keyword-based context selection.
    """
    path=CACHE/f'{doc_id}.pdf'
    if not path.exists():
        raise FileNotFoundError(f'Official {doc_id} PDF not cached. Run python -m src.fetch_sources first.')
    with fitz.open(path) as doc:
        pages=[page.get_text('text') for page in doc]
    needle=normalize(anchor)
    if not needle or len(needle)<6:
        raise ValueError(f'Invalid evidence anchor for {doc_id}: {anchor!r}')
    exact=[i for i,t in enumerate(pages) if needle in normalize(t)]
    if not exact:
        raise ValueError(f'Anchor NOT matched to any page for {doc_id}: {anchor!r}. Review source, OCR and annotation; no context supplied.')
    index=exact[0]  # deterministic and auditable; manually approve correct page
    page_text=' '.join(pages[index].split())
    # Approximate token location for excerpt window. Reference answer is never used.
    words_raw=page_text.split()
    phrase=needle.split()
    idx=0
    for k in range(len(words_raw)):
        if ' '.join(normalize(' '.join(words_raw[k:k+len(phrase)+4])).split()[:len(phrase)]) == needle:
            idx=k;break
    half=words//2
    start=max(0,idx-half);end=min(len(words_raw),start+words)
    excerpt=' '.join(words_raw[start:end])
    if start>0:excerpt='… '+excerpt
    if end<len(words_raw):excerpt+=' …'
    return {'text':excerpt,'page_index_zero_based':index,'page_number_one_based':index+1,
            'pdf_sha256':sha(path.read_bytes()),'excerpt_sha256':sha(excerpt.encode('utf-8')),
            'retrieval_score':1000,'anchor_exact':True}