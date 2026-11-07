"""Check the static website without third-party Python packages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self,path):
        super().__init__();self.links=[];self.ids=[];self.language=None
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self,tag,attributes):
        a=dict(attributes)
        if tag=='html':self.language=a.get('lang')
        if 'id' in a:self.ids.append(a['id'])
        for key in ['href','src','data-zoom']:
            if a.get(key):self.links.append(a[key])
docs={p.name:Document(p) for p in ROOT.glob('*.html')}
errors=[];links=0
for name,doc in docs.items():
    if doc.language!='en':errors.append(name+': language must be English')
    if len(doc.ids)!=len(set(doc.ids)):errors.append(name+': duplicate IDs')
    for link in doc.links:
        p=urlsplit(link)
        if p.scheme or p.netloc:continue
        links+=1;target=ROOT/unquote(p.path) if p.path else ROOT/name
        if not target.is_file():errors.append(name+': missing '+link)
        elif p.fragment and target.name in docs and p.fragment not in docs[target.name].ids:errors.append(name+': missing anchor '+link)
manifest=json.loads((ROOT/'downloads/releases.json').read_text())
entries=[*manifest['products'].values(),manifest['source']]
for item in entries:
    file=ROOT/'downloads'/item['file']
    if hashlib.sha256(file.read_bytes()).hexdigest()!=item['sha256']:errors.append('Checksum mismatch: '+file.name)
    with zipfile.ZipFile(file) as z:
        if z.testzip():errors.append('ZIP integrity: '+file.name)
        for name in z.namelist():
            if '/.git/' in name or name.endswith('.settings') or '/TestTakes/' in name:errors.append('Private/runtime file in archive: '+name)
print(json.dumps({'pages':len(docs),'local_references':links,'verified_downloads':len(entries),'errors':errors},indent=2))
raise SystemExit(bool(errors))
