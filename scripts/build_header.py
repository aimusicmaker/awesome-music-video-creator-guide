"""Build compact centered headers with linked SVG language buttons."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1]
LANGS=json.loads((ROOT/'i18n/languages.json').read_text())['languages']
COPY=json.loads((ROOT/'i18n/header-locales.json').read_text())
DEVICE=json.loads((ROOT/'i18n/mobile-locales.json').read_text())
OUT=ROOT/'assets/navigation'; OUT.mkdir(exist_ok=True)
ORDER=['en','zh','tw','ja','ko','id','it','pt','es','de','ru','fr','th','vi','ar']
BY_CODE={x['code']:x for x in LANGS}
def badge(label,width,active=False,phone=False):
    height=40 if phone else 32
    color='#8200e8' if active else '#253744'
    icon='<rect x="16" y="10" width="12" height="20" rx="2" fill="none" stroke="white" stroke-width="1.6"/><path d="M20 26h4" stroke="white"/>' if phone else ''
    x=width/2+10 if phone else width/2
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(label,quote=True)}"><rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="8" fill="{color}" stroke="{color if active else "#485c69"}"/>{icon}<text x="{x}" y="{height/2}" dy=".35em" text-anchor="middle" fill="white" font-family="Arial, Noto Sans, sans-serif" font-size="13" font-weight="700">{html.escape(label)}</text></svg>\n'
for code in ORDER:
    label=BY_CODE[code]['name'];width=140 if code=='id' else 96
    for active in (False,True):
        (OUT/f'{code}{"-active" if active else ""}.svg').write_text(badge(label,width,active))
    (OUT/f'mobile-{code}.svg').write_text(badge(DEVICE[code]['mobile'],200,True,True))
for lang in LANGS:
    code=lang['code'];p=ROOT/lang['file'];s=p.read_text();c=COPY[code]
    nav=re.search(r'<p align="center"><a href="#(?:ai-vs-live|official-models|x-creators)">',s)
    assert nav,f'{p}: missing section navigation'
    title=f'<h1 align="center"><a href="https://musicmaker.im/"><img src="https://musicmaker.im/images/logo.svg" alt="AI Music Maker logo" width="30" height="30"></a> {html.escape(c["title"])}</h1>'
    header=title+'\n\n<p align="center"><strong>'+html.escape(c['tagline'])+'</strong></p>\n\n'
    if c['intro']:header+='<p align="center">'+html.escape(c['intro'])+'</p>\n\n'
    rows=[]
    for group in (ORDER[:8],ORDER[8:]):
        row=[]
        for target in group:
            item=BY_CODE[target];width=140 if target=='id' else 96
            path=f'assets/navigation/{target}{"-active" if target==code else ""}.svg'
            row.append(f'<a href="{item["file"]}"><img src="{path}" alt="{html.escape(item["name"])}" width="{width}" height="32"></a>')
        rows.append(' '.join(row))
    header+='<!-- LANGUAGES:START -->\n<p align="center">'+'<br>\n'.join(rows)+'</p>\n<!-- LANGUAGES:END -->\n\n'
    s=('<div dir="rtl">\n\n' if code=='ar' else '')+header+s[nav.start():]
    p.write_text(s)
