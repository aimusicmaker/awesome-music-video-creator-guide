# README language editions

The language list follows the public MusicMaker Discover footer, checked on 2026-09-23. See [languages.json](languages.json) for all 15 names, repository files and website destinations.

English, simplified Chinese and traditional Chinese are maintained directly. The other 12 editions are rendered from [readme-locales.json](readme-locales.json) with:

```sh
python3 scripts/build_readmes.py
python3 scripts/check_content.py
```

The renderer updates the shared navigation for English and simplified Chinese as well. Keep the traditional Chinese selector in sync when the language list changes.

Every edition includes creator examples, the nine-track listening shelf, the four-shot nature exercise, the portrait-singing exercise and official model references. Detailed linked documents currently remain English or simplified Chinese; label those destinations clearly. Song titles, model names and creator handles remain unchanged.

When adding a language, translate all reader-facing copy, including image descriptions and action labels. The 12 generated editions explicitly label the shared copyable prompt blocks as English. Preserve source destinations and distinguish source facts from new practice suggestions. Check the page in GitHub at desktop and phone widths. Arabic uses a right-to-left wrapper; inspect mixed model names, filenames and timings after edits.

The gallery manifest owns source URLs and verified scene descriptions. The 12 generated editions currently reuse those English image descriptions for accurate screen-reader alternatives; the visible teaching copy and prompts are localized. Do not substitute lesson text for a scene description.

The gallery manifest owns source URLs. The nine listening tracks are music works with covers, not generated-video results. The two tutorial cases must not appear in the listening shelf. Each homepage must include exactly one illustrated case per tutorial section.

`tutorials/en.txt` and `tutorials/zh.txt` store the two expanded homepage walkthroughs (root-relative links). The renderer reads the English prompt blocks for the 12 generated editions. When changing these templates, update the matching hand-maintained homepages and traditional Chinese too.
