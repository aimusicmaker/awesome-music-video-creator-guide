"""Add sourced model-maker examples before community examples in each language."""
from pathlib import Path
import html
import json
import re

ROOT=Path(__file__).resolve().parents[1]
LANGS=json.loads((ROOT/'i18n/languages.json').read_text())['languages']
COPY=json.loads((ROOT/'i18n/official-locales.json').read_text())
CASES=json.loads((ROOT/'docs/official-cases.json').read_text())['cases']
for lang in LANGS:
    p=ROOT/lang['file'];s=p.read_text();c=COPY[lang['code']]
    s=re.sub(r'<!-- OFFICIAL:START -->.*?<!-- OFFICIAL:END -->\n*','',s,flags=re.S)
    s=re.sub(r'(?: &nbsp; )?<a href="#official-models"><kbd>.*?</kbd></a>(?: &nbsp; )?','',s)
    s=s.replace('<p align="center"><a href="#x-creators">','<p align="center"><a href="#official-models"><kbd>✦ '+html.escape(c['title'])+'</kbd></a> &nbsp; <a href="#x-creators">',1)
    notes='docs/official-cases.zh-CN.md' if lang['code'] in ('zh','tw') else 'docs/official-cases.md'
    cards=[]
    for case,lesson,image_label in zip(CASES,c['lessons'],c['image_labels']):
        cards.append(f'<td width="50%" valign="top"><a href="{case["source"]}"><img src="{case["image"]}" alt="{html.escape(case["alt"],quote=True)}" width="100%"></a><br><sub>{html.escape(image_label)}</sub><br><b>{case["model"]}</b> · {case["publisher"]}<br>{html.escape(lesson)}<br><a href="{case["source"]}"><kbd>▶ {c["example"]}</kbd></a> · <a href="{case["tutorial"]}">{c["guide"]} ↗</a><br><a href="{notes}#{case["id"]}">{c["notes"]} →</a> · <a href="{case["brand_url"]}"><kbd>MusicMaker ↗</kbd></a></td>')
    section='<!-- OFFICIAL:START -->\n<a id="official-models"></a>\n\n## '+c['title']+'\n\n'+c['intro']+'\n\n<table>\n'
    section+='\n'.join('<tr>\n'+'\n'.join(cards[i:i+2])+'\n</tr>' for i in range(0,len(cards),2))
    section+='\n</table>\n\n'+c['boundary']+'\n\n<!-- OFFICIAL:END -->\n\n'
    s=s.replace('<a id="x-creators"></a>',section+'<a id="x-creators"></a>',1)
    rows=[]
    for case,lesson in zip(CASES,c['capabilities']):
        rows.append(f'<tr><td width="650"><b>{case["model"]}</b><br>{html.escape(c["advice_label"])}: {html.escape(lesson)}</td><td width="350"><a href="{case["tutorial"]}">{c["guide"]} ↗</a><br><a href="{notes}#{case["id"]}">{c["notes"]} →</a><br><a href="{case["brand_url"]}"><kbd>MusicMaker · {case["model"]} ↗</kbd></a></td></tr>')
    capability='<!-- CAPABILITIES:START -->\n<table>\n'+'\n'.join(rows)+'\n</table>\n<!-- CAPABILITIES:END -->\n'
    if '<!-- CAPABILITIES:START -->' in s:
        s=re.sub(r'<!-- CAPABILITIES:START -->.*?<!-- CAPABILITIES:END -->\n',lambda m:capability,s,flags=re.S)
    else:
        s=re.sub(r'^- \*\*.*Seedance 2\.5.*\n- \*\*.*MiniMax H3.*\n',lambda m:capability+'\n',s,count=1,flags=re.M)
    for model,url in [('MiniMax Music 3.0','https://musicmaker.im/minimax/minimax-music-v3-0/'),('Eleven Music','https://musicmaker.im/eleven-labs/eleven-labs-music/')]:
        s=re.sub(r'^(- \*\*.*'+re.escape(model)+r'.*)$',lambda m:m[1] if url in m[1] else m[1]+' [MusicMaker ↗]('+url+')',s,flags=re.M)
    s=re.sub(r'## [^\n]+\n\n(?=<!-- CAPABILITIES:START -->)',lambda m:'## '+c['capability_title']+'\n\n',s)
    p.write_text(s)
