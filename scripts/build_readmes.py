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
    return '<p align="center">'+' &nbsp; '.join(f'<a href="#{id}"><kbd>{icon} {esc(label)}</kbd></a>' for id,icon,label in zip(['x-creators','listen','first-video','next-project','toolkit'],['▶','♫','✦','→','🧰'],labels))+'</p>'
def grid(cards,columns=2):
    return '<table>\n'+'\n'.join('<tr>\n'+'\n'.join(cards[i:i+columns])+'\n</tr>' for i in range(0,len(cards),columns))+'\n</table>'
def brand_card(id,desc,label,project=False,titles=None,columns=2):
    b=B[id];target=b.get('video',b['source'])
    title=f'<b>{esc((titles or {}).get(id,b["title"]))}</b>'
    action=f'<a href="{target}"><kbd>▶ {esc(label)}</kbd></a>'
    if project:action=f'<a href="docs/brand-projects.md#{id}"><kbd>→ {esc(label)}</kbd></a>'
    description='<b>'+esc(desc.split(' · ',1)[0])+'</b><br><sub>'+esc(desc.split(' · ',1)[1])+'</sub>' if ' · ' in desc else esc(desc)
    return f'<td width="{100//columns}%" valign="top"><a href="{target}"><img src="{b["thumbnail"]}" alt="{esc(b["alt"])}" width="100%"></a><br>{title}<br>{description}<br>{action}</td>'

def toolkit(c,zh=False):
    links=[
      [('Free image generator','https://musicmaker.im/free-chatgpt-images-2-5/')],
      [('5s short video','https://musicmaker.im/free-short-music-video-generator/'),('Text to video','https://musicmaker.im/free-text-to-video/')],
      [('Lo-fi song maker','https://musicmaker.im/lofi-song-maker/')],
      [('MP3 → WAV','https://musicmaker.im/audio-converter/mp3-to-wav/'),('MP3 tag editor','https://musicmaker.im/mp3-tag-editor-online/')],
      [('Discover','https://musicmaker.im/discover/'),('Video examples','https://musicmaker.im/ai-music-video-generator/'),('12 prompts','prompts/README.md')]
    ]
    if zh:
        links[-1][-1]=('12 prompts','prompts/README_ZH.md')
        names=['免费制图','5 秒短片','文字生成视频','低保真音色转换','MP3 → WAV','歌曲信息编辑','歌曲与封面','视频示例','12 套提示词'];i=iter(names)
        links=[[(next(i),u) for _,u in row] for row in links]
    out='<a id="toolkit"></a>\n\n## '+c['title']+'\n\n'+c['note']+'\n\n<table>\n'
    for label,row in zip(c['rows'],links):
        out+='<tr><td width="35%"><b>'+esc(label)+'</b></td><td>'+ ' · '.join(f'<a href="{u}"><kbd>↗ {esc(n)}</kbd></a>' for n,u in row)+'</td></tr>\n'
    return out+'</table>\n\n[→ '+c['catalog']+'](docs/brand-resources'+('.zh-CN' if zh else '')+'.md)\n\n'

for lang in LANGS:
    code=lang['code']
    if code in ('en','zh','tw'):continue
    c=COPY[code];L=c['labels']
    s=f'# {c["title"]}\n\n{language_bar(code)}\n\n**{c["lead"]}**\n\n{navigation(c["nav"]+[c["toolkit"]["nav"]])}\n\n'
    s+=f'[![{c["hero"]}](assets/social-preview.jpg)](#first-video)\n\n{c["hero"]}\n\n'
    s+=f'<a id="x-creators"></a>\n\n## {c["nav"][0]}\n\n{c["x_intro"]}\n\n'
    cards=[]
    for x,desc in zip(G['x'],c['x_lessons']):
        cards.append(f'<td width="50%" valign="top"><a href="{x["post"]}"><img src="{x["thumbnail"]}" alt="{esc(x["alt"])}" width="100%"></a><br><b>{esc(desc)}</b><br><sub><a href="{x["post"]}">@{x["author"]}</a> · {esc(x["model"])}</sub><br><a href="{x["post"]}">{L[0]} ↗</a> · <a href="docs/x-cases.md#{x["id"]}">{L[1]} →</a></td>')
    s+=grid(cards)+f'\n\n{c["x_note"]}\n\n'
    s+=f'<a id="listen"></a>\n\n## {c["nav"][1]}\n\n{c["listen_intro"]}\n\n<!-- LISTENING-GRID:START -->\n'
    s+=grid([brand_card(id,desc,c['play'],columns=3) for id,desc in zip(G['listening'],c['cover_notes'])],3)+'\n<!-- LISTENING-GRID:END -->\n\n'
    s+=c['toolkit']['bridge']+f' [→ {c["toolkit"]["nav"]}](#toolkit) · [↗ {c["toolkit"]["sources"]}](docs/listening-notes.md)\n\n'
    for section,id,intro,steps,note in [
        ('first-video','brightside',c['first_intro'],c['steps'],c['limits']),
        ('next-project','performance-2',c['next_intro'],c['vocal_steps'],c['vocal'])]:
        b=B[id];target=b.get('video',b['source']);heading=L[7] if section=='first-video' else L[8]
        s+=f'<a id="{section}"></a>\n\n## {heading}\n\n'
        s+=f'<table><tr><td width="42%" valign="top"><a href="{target}"><img src="{b["thumbnail"]}" alt="{esc(b["alt"])}" width="100%"></a></td><td width="58%" valign="top">{esc(intro)}<br><br><b>1.</b> {esc(steps[0])}</td></tr></table>\n\n'
        action=c['play'] if section=='first-video' else c['watch_demo']
        s+=f'[▶ {action}]({target}) · [↗ {L[3]}](https://hailuoai.video/tools/minimax-h3) · '
        tool='free-short-music-video-generator' if section=='first-video' else 'ai-music-video-generator'
        s+=f'[↗ MusicMaker](https://musicmaker.im/{tool}/)\n\n'
        if section=='first-video':s+=f'[♫ {L[5]}](starter-kit/practice-beat-120bpm.wav)\n\n'
        s+='\n\n'.join(f'{i+1}. {step}' for i,step in enumerate(steps[1:],start=1))+'\n\n'
        s+=f'**{c["prompt_intro"]}**\n\n'
        source=(ROOT/'i18n/tutorials/en.txt').read_text()
        prompts=re.findall(r'```text\n(.*?)```',source,re.S)
        if code=='ar':s+='<div dir="ltr">\n\n'
        for prompt in (prompts[:4] if section=='first-video' else prompts[4:]):s+='```text\n'+prompt+'```\n\n'
        if code=='ar':s+='</div>\n\n'
        s+=note+'\n\n'
        anchor='3-assemble-in-an-editor' if section=='first-video' else 'vocal'
        s+=f'[→ {L[2]}](docs/first-video.md#{anchor})\n\n'
    s+=toolkit(c['toolkit'])
    s+=f'## {L[6]}\n\n'
    sources=[('Seedance 2.5','https://seed.bytedance.com/en/seedance2_5'),('MiniMax H3','https://www.minimax.io/blog/minimax-h3'),('MiniMax Music 3.0','https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model'),('Eleven Music','https://elevenlabs.io/docs/overview/capabilities/music/best-practices')]
    for (name,url),note in zip(sources,c['models']):s+=f'- **[{name}]({url})** — {note}\n'
    s+=f'\n[→ {L[9]}](assets/README.md) · [MIT](LICENSE)\n\n{c["footer"]}\n'
    if code=='ar':s='<div dir="rtl">\n\n'+s+'\n</div>\n'
    (ROOT/lang['file']).write_text(s)
# English and simplified Chinese keep their expanded hand-edited walkthroughs.
for code,filename,labels in [('en','README.md',['X examples','Listen','Make your first video','Next technique']),('zh','README_ZH.md',['X 创作者案例','MusicMaker 试听','制作第一支视频','下一种技巧'])]:
    p=ROOT/filename;s=p.read_text()
    s=re.sub(r'\n*<!-- BRAND:START -->.*?<!-- BRAND:END -->\n*','\n\n',s,flags=re.S)
    s=re.sub(r'<!-- LANGUAGES:START -->.*?<!-- LANGUAGES:END -->\n*','',s,flags=re.S)
    first=s.index('\n')
    s=s[:first]+'\n\n'+language_bar(code)+s[first:]
    old=r'^\[Explore real examples\].*$' if code=='en' else r'^\[看 X 创作者案例\].*$'
    if re.search(old,s,re.M):s=re.sub(old,navigation(labels),s,flags=re.M)
    # Make the existing play actions distinct without external badge dependencies.
    s=re.sub(r'<a href="([^\"]+)">(试听这首歌 →|Listen to the track →|播放视频|Watch video)</a>',lambda m:f'<a href="{m[1]}"><kbd>▶ {m[2].replace(" →", "")}</kbd></a>',s)
    p.write_text(s)

# Keep the localized affiliate invitation at the end of every homepage.
affiliate_copy=json.loads((ROOT/'i18n/affiliate-locales.json').read_text())
for lang in LANGS:
    p=ROOT/lang['file'];s=p.read_text()
    s=re.sub(r'\n*<!-- TRUST:START -->.*?<!-- TRUST:END -->\n*','\n\n',s,flags=re.S)
    s=re.sub(r'\n*<!-- TRANSLATION:START -->.*?<!-- TRANSLATION:END -->\n*','\n\n',s,flags=re.S)
    s=re.sub(r'\n*<!-- AFFILIATE:START -->.*?<!-- AFFILIATE:END -->\n*','',s,flags=re.S)
    title,body,action=affiliate_copy[lang['code']]
    block=f'\n\n<!-- AFFILIATE:START -->\n**{title}**\n\n{body}\n\n<a href="https://musicmaker.im/affiliate-program/"><kbd>↗ {esc(action)}</kbd></a>\n<!-- AFFILIATE:END -->\n'
    if lang['code']=='ar':
        closing=s.rfind('</div>')
        s=s[:closing].rstrip()+block+'\n</div>\n'
    else:s=s.rstrip()+block
    p.write_text(s)

# Use GitHub-supported alignment for the brand, main title and introduction.
for lang in LANGS:
    p=ROOT/lang['file'];s=p.read_text()
    s=re.sub(r'\n*<!-- BRAND:START -->.*?<!-- BRAND:END -->\n*','\n\n',s,flags=re.S)
    s=re.sub(r'^# (.+)$',lambda m: '<h1 align="center">'+esc(m[1])+'</h1>',s,count=1,flags=re.M)
    logo='\n\n<!-- BRAND:START -->\n<p align="center"><a href="https://musicmaker.im/"><img src="https://musicmaker.im/images/logo.svg" alt="MusicMaker logo" width="88" height="88"></a></p>\n<!-- BRAND:END -->'
    s=re.sub(r'(<h1 align="center">.*?</h1>)',lambda m:m[1]+logo,s,count=1)
    # Only the opening prose is centered; tutorials and galleries keep their layout.
    start=s.index('<!-- LANGUAGES:END -->')+len('<!-- LANGUAGES:END -->')
    end=re.search(r'<p align="center"><a href="#(?:official-models|x-creators)">',s[start:]).start()+start
    intro=s[start:end]
    intro=re.sub(r'^\*\*(.+)\*\*$',lambda m:'<p align="center"><strong>'+esc(m[1])+'</strong></p>',intro,flags=re.M)
    paragraphs=intro.split('\n\n')
    for i,paragraph in enumerate(paragraphs):
        if paragraph.strip() and not paragraph.lstrip().startswith('<'):
            paragraphs[i]='<p align="center">'+esc(paragraph.strip())+'</p>'
    s=s[:start]+'\n\n'.join(paragraphs)+s[end:]
    p.write_text(s)

# Device-specific pages are derived after all desktop content is finalized.
import runpy
runpy.run_path(str(ROOT/'scripts/build_official.py'))
runpy.run_path(str(ROOT/'scripts/build_trust.py'))
runpy.run_path(str(ROOT/'scripts/build_header.py'))
runpy.run_path(str(ROOT/'scripts/build_mobile.py'))
