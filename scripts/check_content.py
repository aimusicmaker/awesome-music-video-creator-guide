"""Check local reader links, recipe structure, and starter-kit timing."""
from pathlib import Path
import csv
import json
from html.parser import HTMLParser
import re
import struct
import sys
import wave
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []

def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    seen = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        result.add(slug + (f'-{n}' if n else ''))
    return result

mds = sorted(p for p in ROOT.rglob('*.md') if not any(x.startswith('.') for x in p.relative_to(ROOT).parts))
refs = 0
for path in mds:
    text = path.read_text()
    stripped = re.sub(r'```.*?```', '', text, flags=re.S)
    targets = re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', stripped)
    targets += re.findall(r'(?:href|src)="([^"]+)"', stripped)
    for raw in targets:
        url = urlsplit(raw)
        if url.scheme or url.netloc:
            continue
        refs += 1
        dest = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not dest.is_relative_to(ROOT):
            errors.append(f'{path.relative_to(ROOT)}: link escapes repository: {raw}')
        elif not dest.exists():
            errors.append(f'{path.relative_to(ROOT)}: missing {raw}')
        elif url.fragment and dest.suffix == '.md' and unquote(url.fragment) not in anchors(dest.read_text()):
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {raw}')
    if text.count('```') % 2:
        errors.append(f'{path.relative_to(ROOT)}: unclosed code fence')

recipes = sorted((ROOT/'prompts').glob('[0-9][0-9]-*.md'))
if len(recipes) != 12:
    errors.append(f'Expected 12 recipes, found {len(recipes)}; update advertised counts when changing the catalog')
for recipe in recipes:
    content = recipe.read_text()
    for heading in ['Bring these inputs', 'Image direction', 'Copy the motion prompt', 'Music direction', 'Assemble the edit', 'If it fails']:
        if f'## {heading}' not in content:
            errors.append(f'{recipe.name}: missing {heading}')
    if 'not render-tested' not in content:
        errors.append(f'{recipe.name}: missing render status')

with wave.open(str(ROOT/'starter-kit/practice-beat-120bpm.wav'),'rb') as w:
    duration = w.getnframes()/w.getframerate()
    if (w.getnchannels(),w.getsampwidth(),w.getframerate(),duration) != (1,2,44100,16):
        errors.append('Practice WAV format or duration differs from documentation')
    samples = struct.unpack('<'+'h'*w.getnframes(),w.readframes(w.getnframes()))
    peak = max(abs(x) for x in samples)
    if not 1000 < peak < 32767:
        errors.append('Practice WAV is silent/too quiet or clipped')

with (ROOT/'starter-kit/shot-list.csv').open() as f:
    rows = list(csv.DictReader(f))
expected = [(0,4),(4,8),(8,12),(12,16)]
if [(float(r['start_seconds']),float(r['end_seconds'])) for r in rows] != expected:
    errors.append('Shot list does not fill the 16-second practice timeline')

srt = (ROOT/'starter-kit/practice-captions.srt').read_text()
times = re.findall(r'(\d\d):(\d\d):(\d\d),(\d{3})',srt)
seconds = [int(h)*3600+int(m)*60+int(s)+int(ms)/1000 for h,m,s,ms in times]
if not seconds or len(seconds)%2 or any(not 0<=a<b<=16 for a,b in zip(seconds[::2],seconds[1::2])):
    errors.append('Subtitle cues exceed the practice track or have invalid ordering')

image = (ROOT/'assets/music-video-directions.png').read_bytes()
if image[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II',image[16:24]) != (1536,1024):
    errors.append('Concept artwork is missing or has unexpected dimensions')

# The editorial gallery is a reader contract: correct source destinations,
# useful alternative text, language parity and a balanced brand/community mix.
class GalleryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.href = None
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a':
            self.href = attrs.get('href')
        elif tag == 'img':
            self.images.append((attrs.get('src'), attrs.get('alt', ''), self.href))

    def handle_endtag(self, tag):
        if tag == 'a':
            self.href = None

gallery = json.loads((ROOT/'docs/gallery-sources.json').read_text())
locale_copy = json.loads((ROOT/'i18n/readme-locales.json').read_text())
languages = json.loads((ROOT/'i18n/languages.json').read_text())['languages']
if len(languages) != 15 or len({x['code'] for x in languages}) != 15:
    errors.append('Expected the 15 language options recorded from the brand website')
if len(gallery['x']) != 6 or len({x['id'] for x in gallery['brand']}) != len(gallery['brand']):
    errors.append('Expected six X cases and unique cataloged brand references')
if len(set(gallery['listening'])) != 9:
    errors.append('Listening shelf must contain nine distinct tracks')
if len({item['post'] for item in gallery['x']}) != len(gallery['x']):
    errors.append('Duplicate X post in gallery')
for language in languages:
    filename = language['file']
    path = ROOT/filename
    if not path.exists():
        errors.append(f'Missing language edition: {filename}')
        continue
    content = path.read_text()
    parser = GalleryParser(); parser.feed(content)
    for item in gallery['x'] + gallery['brand']:
        matches = [row for row in parser.images if row[0] == item['thumbnail']]
        target = item['post'] if 'post' in item else item.get('video', item['source'])
        expected_count = 1 if 'post' in item or item['id'] in gallery['listening'] + gallery['tutorials'] else 0
        if len(matches) != expected_count or any(row[2] != target for row in matches):
            errors.append(f'{filename}: missing, duplicated or mislinked image: {item["id"]}')
        elif any(len(row[1].strip()) < 12 for row in matches):
            errors.append(f'{filename}: uninformative image alt: {item["id"]}')
    if language['code'] not in ('en','zh','tw'):
        for item in gallery['x'] + gallery['brand']:
            if any(alt != item['alt'] for src,alt,href in parser.images if src == item['thumbnail']):
                errors.append(f'{filename}: scene alt differs from verified source: {item["id"]}')
        for item in gallery['x']:
            if f'<a href="{item["post"]}">@{item["author"]}</a>' not in content:
                errors.append(f'{filename}: author must link to original X post')
    shelf = re.search(r'<!-- LISTENING-GRID:START -->(.*?)<!-- LISTENING-GRID:END -->',content,re.S)
    if not shelf or shelf[1].count('<tr>') != 3 or shelf[1].count('<td ') != 9:
        errors.append(f'{filename}: listening grid must have three columns and three rows')
    else:
        for item in gallery['brand']:
            if item['id'] in gallery['listening'] and shelf[1].count(item['thumbnail']) != 1:
                errors.append(f'{filename}: listening track mismatch: {item["id"]}')
    if set(gallery['listening']) & set(gallery['tutorials']) or len(gallery['tutorials']) != 2:
        errors.append('Tutorials must use exactly two cases outside the listening shelf')
    for marker,case,prompt_count in [('first-video','brightside',4),('next-project','performance-2',1)]:
        part = content.split(f'<a id="{marker}"></a>',1)[-1]
        part = part.split('<a id="next-project"></a>',1)[0] if marker == 'first-video' else part.split('<a id="toolkit"></a>',1)[0]
        images = GalleryParser(); images.feed(part)
        if len(images.images) != 1:
            errors.append(f'{filename}: {marker} must illustrate exactly one case')
        if marker == 'next-project' and language['code'] in locale_copy:
            c = locale_copy[language['code']]
            if f'[▶ {c["watch_demo"]}]' not in part or f'[▶ {c["labels"][0]}]' in part:
                errors.append(f'{filename}: wrong brand demo action label')
        if part.count('```text') != prompt_count:
            errors.append(f'{filename}: incomplete inline prompts in {marker}')
    if 'assets/music-video-workflow.png' not in content:
        errors.append(f'{filename}: missing workflow cover')
    for destination in languages:
        if destination['code'] != language['code'] and f'href="{destination["file"]}"' not in content:
            errors.append(f'{filename}: missing language switch to {destination["file"]}')
    order = [content.find(f'<a id="{a}">') for a in ['official-models','x-creators','listen','first-video','next-project','toolkit']]
    if min(order) < 0 or order != sorted(order):
        errors.append(f'{filename}: incorrect reader journey section order')
# Official case cards must retain source, guide and learning-note links.
official = json.loads((ROOT/'docs/official-cases.json').read_text())['cases']
brand_catalog=(ROOT/'docs/brand-resources.json').read_text()
for case in official:
    if case.get('brand_url','MISSING') not in brand_catalog:
        errors.append(f'Official model lacks cataloged MusicMaker route: {case["model"]}')
for language in languages:
    for folder in ['', 'mobile/']:
        content=(ROOT/(folder+language['file'])).read_text()
        section=content.split('<!-- OFFICIAL:START -->',1)[-1].split('<!-- OFFICIAL:END -->',1)[0]
        if section.count('<img ') != len(official):
            errors.append(f'{folder}{language["file"]}: missing official case images')
        capability=content.split('<!-- CAPABILITIES:START -->',1)[-1].split('<!-- CAPABILITIES:END -->',1)[0]
        for case in official:
            if case['brand_url'] not in section or case['brand_url'] not in capability:
                errors.append(f'{folder}{language["file"]}: missing paired MusicMaker route')
            if case['source'] not in section or case['tutorial'] not in section or '#'+case['id'] not in section:
                errors.append(f'{folder}{language["file"]}: incomplete official case {case["id"]}')
# Mobile layouts are derived from desktop content, with intact copyable prompts.
for language in languages:
    filename = language['file']
    desktop = (ROOT/filename).read_text()
    mobile_path = ROOT/'mobile'/filename
    if not mobile_path.exists():
        errors.append(f'Missing mobile homepage: {filename}')
        continue
    mobile = mobile_path.read_text()
    if desktop.count(f'href="mobile/{filename}"') != 1 or mobile.count(f'href="../{filename}"') != 1:
        errors.append(f'{filename}: missing or duplicated device switch')
    if '<table' in mobile or re.search(r'^\|',mobile,re.M):
        errors.append(f'{filename}: mobile must use a single-column layout')
    if re.findall(r'```.*?```',desktop,re.S) != re.findall(r'```.*?```',mobile,re.S):
        errors.append(f'{filename}: mobile prompts differ from desktop')
    for destination in languages:
        if destination['code'] != language['code'] and f'href="{destination["file"]}"' not in mobile:
            errors.append(f'{filename}: mobile language switch missing')
workflow = (ROOT/'assets/music-video-workflow.png').read_bytes()
if workflow[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II',workflow[16:24]) != (1536,1024):
    errors.append('Workflow cover is missing or has unexpected dimensions')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(mds)} Markdown files, {refs} local links, {len(recipes)} recipes, artwork, audio and edit timings')
print('This does not verify external playback, rendered layout, or generator output quality.')
