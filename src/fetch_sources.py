import argparse, json
from .common import read_sources
from .evidence import fetch_source
from .common import sha

def main():
    p=argparse.ArgumentParser(description='Download government PDFs; verify downloaded bytes before testing.')
    p.add_argument('--sources',nargs='*',default=list(read_sources()))
    args=p.parse_args()
    for k in args.sources:
        path=fetch_source(k)
        print(json.dumps({'id':k,'path':str(path),'bytes':path.stat().st_size,'sha256':sha(path.read_bytes())}))
if __name__=='__main__':main()