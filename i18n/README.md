# README language editions

The language list follows the public MusicMaker Discover footer, checked on 2026-09-23. See [languages.json](languages.json) for all 15 names, repository files and website destinations.

English, simplified Chinese and traditional Chinese are maintained directly. The other 12 editions are rendered from [readme-locales.json](readme-locales.json) with:

```sh
python3 scripts/build_readmes.py
python3 scripts/check_content.py
```

The renderer also maintains shared navigation and generates the separate mobile editions. Check all 15 desktop and 15 mobile editions when changing shared links or the language list.

Every edition includes creator examples, the nine-track listening shelf, the four-shot nature exercise, the portrait-singing exercise and official model references. Detailed linked documents currently remain English or simplified Chinese; label those destinations clearly. Song titles, model names and creator handles remain unchanged.

When adding a language, translate all reader-facing copy, including image descriptions and action labels. The 12 generated editions explicitly label the shared copyable prompt blocks as English. Preserve source destinations and distinguish source facts from new practice suggestions. Check the page in GitHub at desktop and phone widths. Arabic uses a right-to-left wrapper; inspect mixed model names, filenames and timings after edits.

The gallery manifest owns source URLs and verified scene descriptions. The 12 generated editions currently reuse those English image descriptions for accurate screen-reader alternatives; the visible teaching copy is localized, while shared copyable prompts remain in English and are labeled accordingly. Do not substitute lesson text for a scene description.

The gallery manifest owns source URLs. The nine listening tracks are music works with covers, not generated-video results. The two tutorial cases must not appear in the listening shelf. Each homepage must include exactly one illustrated case per tutorial section.

`tutorials/en.txt` and `tutorials/zh.txt` store the two expanded homepage walkthroughs (root-relative links). The renderer reads the English prompt blocks for the 12 generated editions. When changing these templates, update the matching hand-maintained homepages and traditional Chinese too.

## Translation and review status

AI assists with drafting and translation. Direct maintenance of a language file does not establish native-speaker review. No language edition is currently labeled as independently approved by a named native-language reviewer. Automated checks verify structure, links and shared content; they do not certify natural phrasing, cultural suitability or model output quality.

Detailed guides are mainly English or simplified Chinese. Preserve language labels on those links so readers know before leaving their edition. For Arabic, verify both right-to-left reading order and mixed-language model names and prompts.

[Report a translation problem](https://github.com/aimusicmaker/awesome-music-video-creator-guide/issues/new?template=translation.yml) with the language, page, current text and suggested wording. If a reviewer completes a language review, record the reviewed commit, exact pages, date and reviewer attribution with their permission; do not imply that it covers later changes. See the [editorial policy](../docs/editorial-policy.md) for content and source standards.
