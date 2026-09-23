"""Place two attributed full music videos before the official model gallery."""
from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]
COPY=json.loads((ROOT/'i18n/comparison-locales.json').read_text())
CASES=json.loads((ROOT/'docs/comparison-cases.json').read_text())['cases']
for lang in json.loads((ROOT/'i18n/languages.json').read_text())['languages']:
    p=ROOT/lang['file'];s=p.read_text();c=COPY[lang['code']]
    s=re.sub(r'<!-- COMPARISON:START -->.*?<!-- COMPARISON:END -->\n*','',s,flags=re.S)
    s=re.sub(r'<a href="#ai-vs-live"><kbd>.*?</kbd></a>(?: &nbsp; )?','',s)
    s=s.replace('<p align="center"><a href="#official-models">','<p align="center"><a href="#ai-vs-live"><kbd>◈ '+html.escape(c['nav'])+'</kbd></a> &nbsp; <a href="#official-models">',1)
    cards=[]
    for case,key in zip(CASES,['ai','live']):
        alt=case['artist']+' — '+case['title']+' · '+c[key+'_alt']
        cards.append(f'<td width="50%" valign="top"><b>{html.escape(c[key+"_label"])}</b><br><a href="{case["video"]}"><img src="{case["image"]}" alt="{html.escape(alt,quote=True)}" width="100%"></a><br><b>{case["artist"]} — {case["title"]}</b><br><sub>{html.escape(c[key+"_credit"])}</sub><br>{html.escape(c[key+"_caption"])}<br><a href="{case["video"]}"><kbd>▶ {c["watch"]}</kbd></a> · <a href="{case["making"]}">{c["making"]} ↗</a></td>')
    section='<!-- COMPARISON:START -->\n<a id="ai-vs-live"></a>\n\n## '+c['title']+'\n\n'+c['intro']+'\n\n<table>\n<tr>\n'+'\n'.join(cards)+'\n</tr>\n</table>\n\n'
    # Two columns keep the comparison readable both in a table and stacked mobile cards.
    section+='<table>\n'
    for row in c['rows']:
        section+='<tr>'+''.join('<td width="50%" valign="top"><b>'+html.escape(row[0])+' · '+html.escape(c['headers'][i+1])+'</b><br>'+html.escape(row[i+1])+'</td>' for i in range(2))+'</tr>\n'
    section+='</table>\n\n'+c['bridge']+'\n\n'
    notes='docs/ai-vs-live.zh-CN.md' if lang['code'] in ('zh','tw') else 'docs/ai-vs-live.md'
    suffix='' if lang['code'] in ('en','zh','tw') else ' (English)'
    section+='[✦ '+c['next']+'](#official-models) · ['+c['notes']+suffix+']('+notes+')\n\n<!-- COMPARISON:END -->\n\n'
    assert s.count('<!-- OFFICIAL:START -->')==1
    s=s.replace('<!-- OFFICIAL:START -->',section+'<!-- OFFICIAL:START -->',1)
    p.write_text(s)
