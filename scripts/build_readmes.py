"""Render localized homepages and the shared language/navigation controls."""
from pathlib import Path
import html
import json
import re

ROOT=Path(__file__).resolve().parents[1]
LANGS=json.loads((ROOT/'i18n/languages.json').read_text())['languages']
COPY=json.loads((ROOT/'i18n/readme-locales.json').read_text())
G=json.loads((ROOT/'docs/gallery-sources.json').read_text())
B={x['id']:x for x in G['brand']}

def esc(s):return html.escape(s,quote=True)
def language_bar(code):
    links=[]
    for x in LANGS:
        label=esc(x['name'])
        links.append(f'<b>{label}</b>' if x['code']==code else f'<a href="{x["file"]}"><kbd>{label}</kbd></a>')
    return '<!-- LANGUAGES:START -->\n<p align="center">🌐 '+' · '.join(links)+'</p>\n<!-- LANGUAGES:END -->'
def navigation(labels):
    return '<p align="center">'+' &nbsp; '.join(f'<a href="#{id}"><kbd>{icon} {esc(label)}</kbd></a>' for id,icon,label in zip(['x-creators','listen','first-video','next-project'],['▶','♫','✦','→'],labels))+'</p>'
def grid(cards):
    return '<table>\n'+'\n'.join('<tr>\n'+'\n'.join(cards[i:i+2])+'\n</tr>' for i in range(0,len(cards),2))+'\n</table>'
def brand_card(id,desc,label,project=False,titles=None):
    b=B[id];target=b.get('video',b['source'])
    title=f'<b>{esc((titles or {}).get(id,b["title"]))}</b>'
    action=f'<a href="{target}"><kbd>▶ {esc(label)}</kbd></a>'
    if project:action=f'<a href="docs/brand-projects.md#{id}"><kbd>→ {esc(label)}</kbd></a>'
    return f'<td width="50%" valign="top"><a href="{target}"><img src="{b["thumbnail"]}" alt="{esc(b["alt"])}" width="100%"></a><br>{title}<br>{esc(desc)}<br>{action}</td>'

for lang in LANGS:
    code=lang['code']
    if code in ('en','zh','tw'):continue
    c=COPY[code];L=c['labels']
    s=f'# {c["title"]}\n\n{language_bar(code)}\n\n**{c["lead"]}**\n\n{navigation(c["nav"])}\n\n'
    s+=f'[![{c["hero"]}](assets/music-video-directions.png)](#first-video)\n\n{c["hero"]}\n\n'
    s+=f'<a id="x-creators"></a>\n\n## {c["nav"][0]}\n\n{c["x_intro"]}\n\n'
    cards=[]
    for x,desc in zip(G['x'],c['x_lessons']):
        cards.append(f'<td width="50%" valign="top"><a href="{x["post"]}"><img src="{x["thumbnail"]}" alt="{esc(x["alt"])}" width="100%"></a><br><b>{esc(desc)}</b><br><sub><a href="{x["post"]}">@{x["author"]}</a> · {esc(x["model"])}</sub><br><a href="{x["post"]}">{L[0]} ↗</a> · <a href="docs/x-cases.md#{x["id"]}">{L[1]} →</a></td>')
    s+=grid(cards)+f'\n\n{c["x_note"]}\n\n'
    s+=f'<a id="listen"></a>\n\n## {c["nav"][1]}\n\n{c["listen_intro"]}\n\n<!-- LISTENING-GRID:START -->\n'
    s+=grid([brand_card(id,desc,c['play']) for id,desc in zip(G['listening'],c['cover_notes'])])+'\n<!-- LISTENING-GRID:END -->\n\n'
    s+=f'<a id="first-video"></a>\n\n## {L[7]}\n\n{c["first_intro"]}\n\n'
    s+=grid([brand_card(id,c['cover_notes'][i],L[1],True) for id,i in [('the_open_road',2),('summer_high',3)]])+'\n\n'
    s+=f'[♫ {L[5]}](starter-kit/practice-beat-120bpm.wav) · [↗ {L[3]}](https://hailuoai.video/tools/minimax-h3) · [↗ MusicMaker](https://musicmaker.im/free-short-music-video-generator/)\n\n'
    s+='\n'.join(f'{i+1}. {step}' for i,step in enumerate(c['steps']))+'\n\n'
    s+='\n'.join(f'- **{i*4:02d}–{(i+1)*4:02d}s** · {shot}' for i,shot in enumerate(c['shots']))+'\n\n'
    s+=f'<details>\n<summary><b>{c["prompt_intro"]}</b></summary>\n\n'
    # Short lines keep copyable prompts readable on narrow screens.
    for prompt in c['prompts']:
        s+='```text\n'+re.sub(r'(?<=[。.!؟])\s+', '\n',prompt)+'\n```\n\n'
    s+='</details>\n\n'+c['limits']+f'\n\n[→ {L[2]}](docs/first-video.md#3-assemble-in-an-editor)\n\n'
    s+=f'<a id="next-project"></a>\n\n## {L[8]}\n\n{c["next_intro"]}\n\n'
    s+=grid([brand_card(id,desc,L[1],True,c["performance_titles"]) for id,desc in zip(['echoes_of_you','neon_pulse','performance-1','performance-2'],c['next_lessons'])])+'\n\n'
    s+=c['vocal']+f'\n\n[↗ {L[3]}](https://hailuoai.video/tools/minimax-h3) · [↗ MusicMaker](https://musicmaker.im/ai-music-video-generator/) · [→ {L[2]}](docs/first-video.md#vocal)\n\n'
    s+=f'## {L[6]}\n\n'
    sources=[('Seedance 2.5','https://seed.bytedance.com/en/seedance2_5'),('MiniMax H3','https://www.minimax.io/blog/minimax-h3'),('MiniMax Music 3.0','https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model'),('Eleven Music','https://elevenlabs.io/docs/overview/capabilities/music/best-practices')]
    for (name,url),note in zip(sources,c['models']):s+=f'- **[{name}]({url})** — {note}\n'
    s+=f'\n[→ {L[9]}](assets/README.md) · [MIT](LICENSE)\n\n{c["footer"]}\n'
    if code=='ar':s='<div dir="rtl">\n\n'+s+'\n</div>\n'
    (ROOT/lang['file']).write_text(s)
# English and simplified Chinese keep their expanded hand-edited walkthroughs.
for code,filename,labels in [('en','README.md',['X examples','Listen','Make your first video','Next technique']),('zh','README_ZH.md',['X 创作者案例','MusicMaker 试听','制作第一支视频','下一种技巧'])]:
    p=ROOT/filename;s=p.read_text()
    s=re.sub(r'<!-- LANGUAGES:START -->.*?<!-- LANGUAGES:END -->\n*','',s,flags=re.S)
    first=s.index('\n')
    s=s[:first]+'\n\n'+language_bar(code)+s[first:]
    old=r'^\[Explore real examples\].*$' if code=='en' else r'^\[看 X 创作者案例\].*$'
    if re.search(old,s,re.M):s=re.sub(old,navigation(labels),s,flags=re.M)
    # Make the existing play actions distinct without external badge dependencies.
    s=re.sub(r'<a href="([^\"]+)">(试听这首歌 →|Listen to the track →|播放视频|Watch video)</a>',lambda m:f'<a href="{m[1]}"><kbd>▶ {m[2].replace(" →", "")}</kbd></a>',s)
    p.write_text(s)
