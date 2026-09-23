"""Publish concise ownership and evidence information in every homepage."""
from pathlib import Path
import html, json, re
ROOT=Path(__file__).resolve().parents[1]
official=json.loads((ROOT/'i18n/official-locales.json').read_text())
locales=json.loads((ROOT/'i18n/readme-locales.json').read_text())
manual=json.loads((ROOT/'i18n/disclosures.json').read_text())
comparison=json.loads((ROOT/'i18n/comparison-locales.json').read_text())
copy=json.loads((ROOT/'i18n/trust-locales.json').read_text())
for lang in json.loads((ROOT/'i18n/languages.json').read_text())['languages']:
    p=ROOT/lang['file']; s=p.read_text(); c=copy[lang['code']]
    s=re.sub(r'<!-- TRUST:START -->.*?<!-- TRUST:END -->\n*','',s,flags=re.S)
    assert s.count('<!-- OFFICIAL:START -->') == 1, f'{p}: missing official insertion point'
    suffix=' (English)' if lang['code'] not in ('en','zh','tw') else ''
    policy='docs/editorial-policy.zh-CN.md' if lang['code'] in ('zh','tw') else 'docs/editorial-policy.md'
    block='<!-- TRUST:START -->\n<details>\n<summary>'+c['policy_label']+'</summary>\n\n'+c['brand']+' [ '+c['policy_label']+suffix+' → ]('+policy+')\n\n'+c['evidence']+'\n\n'
    notices=[comparison[lang['code']]['disclosure'],official[lang['code']]['disclosure'],official[lang['code']]['boundary']]+(manual.get(lang['code']) or locales.get(lang['code'],{}).get('disclosures',[]))
    block+='\n\n'.join(notices)+'\n\n'
    block+='[▶ '+c['demo_label']+'](starter-kit/night-train-edit-demo.mp4) · ['+c['evidence_label']+' (EN / 简体中文)'+'](docs/generation-tests.md) · ['+c['report_label']+'](https://github.com/aimusicmaker/awesome-music-video-creator-guide/issues/new/choose)\n\n</details>\n<!-- TRUST:END -->\n\n'
    s=re.sub(r'<!-- TRANSLATION:START -->.*?<!-- TRANSLATION:END -->\n*','',s,flags=re.S)
    translation='\n\n<!-- TRANSLATION:START -->\n'+c['translation']+' [🌐 '+c['translation_label']+suffix+'](i18n/README.md)\n<!-- TRANSLATION:END -->\n'
    if lang['code']=='ar':
        closing=s.rfind('</div>'); s=s[:closing].rstrip()+'\n\n'+block+translation+'\n</div>\n'
    else: s=s.rstrip()+'\n\n'+block+translation
    assert s.count('<!-- TRUST:START -->') == s.count('<!-- TRANSLATION:START -->') == 1
    s=re.sub(r'\n{3,}', '\n\n', s)
    p.write_text(s)
