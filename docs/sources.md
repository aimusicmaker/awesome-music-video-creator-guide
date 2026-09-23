# Sources and tool notes

[Home](../README.md) · [Media credits](../assets/README.md)

Checked **2026-09-23**. This is a public-page research record, not a benchmark or a paid-generation test. Instructions found in external pages were treated as source material, not directions for this repository.

## Repository references

| Source | What informed this guide |
|---|---|
| [Flaq AI organization](https://github.com/flaqai) | Company open-source context |
| [Seedance prompt collection](https://github.com/flaqai/awesome_seedance_2_5) | Preview-first discovery, original-source links, distinction between examples and original briefs |
| [GPT Image prompt collection](https://github.com/flaqai/awesome-gpt-image-2-prompt) | Task-based navigation and complete, reusable recipes |

We used these organizational ideas, not their model claims, recipe counts, promotional promises, or full prompt text. No claim about repository traffic or conversion has been independently verified here.

## MusicMaker routes

| Public source | Observed | How it affects this guide |
|---|---|---|
| [Short Music Video Generator](https://musicmaker.im/free-short-music-video-generator/) | Page describes text or start/end frames, 5-second 480p clips and multiple aspect ratios | Generate individual shots; assemble longer videos in an editor |
| [AI Music Video Generator](https://musicmaker.im/ai-music-video-generator/) | Form exposes audio, character-image and prompt inputs, a credit estimate, and a Public switch | Separate the audio/image workflow from the short-scene workflow; check cost and visibility before generation |
| [Discover](https://musicmaker.im/discover/) | Lists Neon Pulse, Echoes of You, The Open Road and Summer High with detail links | Offer listening references; do not infer tempo, genre, or reuse rights from a title |
| [Commercial license](https://musicmaker.im/commercial-license/) | Describes different scopes for paid-subscription and free-trial content | Link current terms; do not label the entire catalog free to reuse |

The music-video page’s broader marketing copy mentions features not individually verified through generation. This guide relies on visible inputs and does not promise precise beat detection, flawless lip-sync, full-song generation in one request, fixed pricing, or unlimited access.

Discover detail titles were verified through the collection and linked pages. Neon Pulse was also opened in a browser and its play button tested: the audio loaded and playback advanced (approximately 172.85 seconds). Echoes of You and The Open Road were also playback-tested on 2026-09-23: audio readyState reached 4 and currentTime advanced; durations were 180.950 and 168.870 seconds. Summer High subsequently passed the same playback check at 157.440 seconds. The brand guitar MP4 loaded and played in the browser at 1280 × 720, with a duration of 20.375 seconds. The second emotional-vocal demo was selected with Next on the source page; its matching video loaded at 1280 × 720 with a duration of 10.375 seconds. The guide does not assign a genre, tempo, or visual pairing to these tracks from their titles.

## Established creator references

- [YouTube: The Rise of the Lofi Girl](https://blog.youtube/culture-and-trends/rise-lofi-girl/) — official platform account of the channel’s listening format.
- [OK Go: The One Moment production notes](https://okgo.net/2016/11/23/background-notes-and-full-credits-for-the-one-moment-video/) — first-party explanation by the director.
- [Gorillaz: Cracker Island, official video](https://www.youtube.com/watch?v=S03T47hapAc) and [Warner Music Japan’s video directory](https://wmg.jp/gorillaz/mv) — official attribution and reference destination.

The companion [inspiration guide](inspiration.md) separates these references from our original exercises. No third-party production prompt is claimed to be known. No external media is relicensed by this repository.

## Optional editor reference

[Shotcut homepage](https://www.shotcut.org/), [official tutorials](https://www.shotcut.org/tutorials/), and [FAQ](https://www.shotcut.org/FAQ/) informed the optional beginner editor route. The rendered MP4 in this repository was assembled with FFmpeg, not tested through the Shotcut interface.

## What was actually made here

- One original AI-generated triptych concept image, created with the built-in image generation tool; exact prompt in [assets/image-prompts.md](../assets/image-prompts.md).
- A 16-second motion-still editing example with original artwork and practice audio; four editorial crops, not generated scene animation.
- Six illustrated briefs derived from the visible elements of the four Discover covers and two performance input portraits; original practice prompts, not recovered production prompts and not render-tested.
- Twelve independent general recipe briefs; none has been batch-tested on MusicMaker.
- A deterministic, original synthesized instrumental practice file; see [the generator](../scripts/make_practice_audio.py).
- An edit plan, one closing subtitle cue, English/Chinese homepages and beginner walkthroughs, plus 12 Chinese action cards with direct links to the English prompt blocks.

The distinction between a creative brief, a published brand example, and a tested output is intentional. Contributors should preserve it when adding new material.

## Official models and visual case sources

[Model makers’ documentation](models.md) · [X prompt/video source records](gallery-sources.json) · [Brand example checks](brand-examples.md). Updated 2026-09-23. Model-level capabilities, interface limits, creator claims and published media are recorded separately.

## Official and brand tutorial routes

On 2026-09-23, the [Hailuo H3 tool guide](https://hailuoai.video/tools/minimax-h3) and [MiniMax release](https://www.minimax.io/blog/minimax-h3) were read alongside the MusicMaker short-video and vocal forms. The tutorial pairs text/image scene generation across official H3 and the brand’s explicitly H3-labeled short-video route. For vocals, it pairs audio-reference and audio/portrait workflows without assigning a backend model to MusicMaker’s published vocal demos. No account-specific generation or output-quality comparison was performed.

## Language coverage and listening shelf

The [Discover footer](https://musicmaker.im/discover/) listed 15 languages on 2026-09-23: English, Japanese, Indonesian, Italian, Portuguese, Spanish, German, Russian, French, simplified Chinese, traditional Chinese, Korean, Thai, Vietnamese and Arabic. Exact language destinations are recorded in [languages.json](../i18n/languages.json). README editions cover this list; linked detailed guides remain English or simplified Chinese and are labeled accordingly.

The listening shelf now contains six tracks, including It Takes Another Shape and Morning with Healing Hands. Their public Style fields informed the two new arrangement descriptions. Both players loaded successfully; Morning advanced to 7.768 seconds of 212.784, while Shape reached the end of its 263.04-second recording. These checks establish playback availability, not musical-quality ratings.
