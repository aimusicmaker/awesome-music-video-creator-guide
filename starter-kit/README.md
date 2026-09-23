# The 16-second practice kit

[Home](../README.md) · [Step-by-step edit](../docs/first-video.md) · [中文入门](../docs/first-video.zh-CN.md)

Download the files individually with GitHub’s **Download raw file** button, or download the whole repository with **Code → Download ZIP**.

| File | What it is for |
|---|---|
| [night-train-edit-demo.mp4](night-train-edit-demo.mp4) | Finished 16-second motion-still editing example with the practice beat; not a MusicMaker generation |
| [practice-beat-120bpm.wav](practice-beat-120bpm.wav) | Original 16-second instrumental practice track; 120 beats per minute |
| [train-shot-prompts.md](train-shot-prompts.md) | Four complete prompts for generating separate train shots |
| [shot-list.csv](shot-list.csv) | Four-shot edit plan; opens in a spreadsheet or text editor |
| [practice-captions.srt](practice-captions.srt) | Optional closing title at 12–16 seconds, not sung lyrics |
| [brief-template.md](brief-template.md) | Reusable plan for your own release |
| [Concept artwork](../assets/music-video-directions.png) | Still-image option if you want to practice without generating clips |

The beat was composed and synthesized specifically for this repository using [make_practice_audio.py](../scripts/make_practice_audio.py). It uses generated oscillators and noise, with no sampled songs, artist voices, or external recordings. It is a modest timing exercise, not a polished commercial track or a MusicMaker output. Original practice audio and code are included under the repository’s [MIT License](../LICENSE).

To recreate the same WAV with Python 3:

```sh
python3 scripts/make_practice_audio.py
```

Run this from the repository root. No third-party Python packages are required. A fixed random seed makes the noise percussion repeatable.

## Recreate the example video

The MP4 uses four crops of the original train artwork and simple camera moves made in the editor. The train, rain, and light are not independently animated. It demonstrates timing and framing, not video-generation quality. No captions are burned into this example; the SRT remains optional.

With FFmpeg installed, run `python3 scripts/make_edit_demo.py` from the repository root. If FFmpeg is elsewhere, pass `--ffmpeg /path/to/ffmpeg`. This produces a 720 × 1280, 24-frame-per-second MP4 with the practice audio; the source crop has less detail than the export size.
