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
if len(gallery['x']) != 6 or len(gallery['brand']) != 6:
    errors.append('Homepage gallery requires six community and six brand entries; revise stated counts together')
if len({item['post'] for item in gallery['x']}) != len(gallery['x']):
    errors.append('Duplicate X post in gallery')
for filename in ['README.md', 'README_ZH.md']:
    parser = GalleryParser()
    content = (ROOT/filename).read_text()
    parser.feed(content)
    for item in gallery['x'] + gallery['brand']:
        matches = [row for row in parser.images if row[0] == item['thumbnail']]
        target = item['post'] if 'post' in item else item.get('video', item['source'])
        if len(matches) != 1 or matches[0][2] != target:
            errors.append(f'{filename}: missing, duplicated or mislinked gallery image: {item["id"]}')
        elif len(matches[0][1].strip()) < 12:
            errors.append(f'{filename}: uninformative image alt: {item["id"]}')
    if content.find(gallery['x'][0]['post']) > content.find(gallery['brand'][0]['source']):
        errors.append(f'{filename}: creator examples must precede brand examples')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(mds)} Markdown files, {refs} local links, {len(recipes)} recipes, artwork, audio and edit timings')
print('This does not verify external playback, rendered layout, or generator output quality.')
