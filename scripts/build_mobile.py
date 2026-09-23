"""Build single-column homepages while keeping desktop content and layouts intact."""
from pathlib import Path
from urllib.parse import urlsplit
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
LANGS = json.loads((ROOT / 'i18n/languages.json').read_text())['languages']
LABELS = json.loads((ROOT / 'i18n/mobile-locales.json').read_text())
(ROOT / 'mobile').mkdir(exist_ok=True)

def stacked_html_table(match):
    # Cards and tutorial image/text cells become consecutive full-width blocks.
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', match[0], re.S)
    blocks = []
    for row in rows:
        for cell in re.findall(r'<td[^>]*>(.*?)</td>', row, re.S):
            blocks.append('<p>' + cell.strip() + '</p>')
    return '\n\n'.join(blocks)

def stacked_markdown_table(match):
    rows = [line.strip().strip('|').split('|') for line in match[0].strip().splitlines()]
    headers = [x.strip() for x in rows[0]]
    records = []
    for row in rows[2:]:
        records.append('\n\n'.join(f'**{header}** — {value.strip()}' for header, value in zip(headers, row)))
    return '\n\n---\n\n'.join(records) + '\n\n'

def mobile_target(url):
    if not url or url.startswith('#') or urlsplit(url).scheme or url.startswith('//'):
        return url
    # Language switches stay inside mobile; all other resources remain canonical.
    if url.split('#')[0] in {x['file'] for x in LANGS}:
        return url
    return '../' + url

for lang in LANGS:
    path = ROOT / lang['file']
    desktop = re.sub(r'\n*<!-- DEVICE:START -->.*?<!-- DEVICE:END -->\n*', '\n\n', path.read_text(), flags=re.S)
    copy = LABELS[lang['code']]
    mobile_label, desktop_label = copy['mobile'], copy['desktop']
    end = desktop.index('<!-- LANGUAGES:END -->') + len('<!-- LANGUAGES:END -->')
    button = f'\n\n<!-- DEVICE:START -->\n<p align="center"><a href="mobile/{lang["file"]}"><kbd>📱 {html.escape(mobile_label)}</kbd></a></p>\n<!-- DEVICE:END -->'
    path.write_text(desktop[:end] + button + desktop[end:])
    # Transform only prose: prompts in fenced code blocks remain byte-for-byte intact.
    parts = re.split(r'(```.*?```)', desktop, flags=re.S)
    for i in range(0, len(parts), 2):
        text = re.sub(r'<table\b.*?</table>', stacked_html_table, parts[i], flags=re.S)
        text = re.sub(r'^\|[^\n]+\|\n\|[ :|\-]+\|\n(?:\|[^\n]+\|\n)+', stacked_markdown_table, text, flags=re.M)
        text = re.sub(r'(href|src)="([^"]+)"', lambda m: f'{m[1]}="{mobile_target(m[2])}"', text)
        text = re.sub(r'(\]\()([^\s)]+)(\))', lambda m: m[1] + mobile_target(m[2]) + m[3], text)
        parts[i] = text
    mobile = ''.join(parts)
    mobile = re.sub(r'(<a id="listen"></a>\n\n## [^\n]+\n\n).*?(\n\n<!-- LISTENING-GRID:START -->)', lambda m: m[1] + copy['listen_intro'] + m[2], mobile, count=1, flags=re.S)
    for original, replacement in copy['layout_replacements']:
        mobile = mobile.replace(original, replacement)
    end = mobile.index('<!-- LANGUAGES:END -->') + len('<!-- LANGUAGES:END -->')
    back = f'\n\n<!-- DEVICE:START -->\n<p align="center"><b>📱 {html.escape(mobile_label)}</b> · <a href="../{lang["file"]}"><kbd>🖥 {html.escape(desktop_label)}</kbd></a></p>\n<!-- DEVICE:END -->'
    mobile = mobile[:end] + back + mobile[end:]
    (ROOT / 'mobile' / lang['file']).write_text(mobile)
