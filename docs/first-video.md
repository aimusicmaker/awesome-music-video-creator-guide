# Your first 16-second music visual

[Home](../README.md) · [Practice kit](../starter-kit/README.md) · [中文入门](first-video.zh-CN.md)

Make a small finished edit before attempting a whole song. This walkthrough uses an original instrumental practice track, so you do not need to find music first.

[Download the completed motion-still example](../starter-kit/night-train-edit-demo.mp4). It uses the same beat and four-shot timing, but moves a still image instead of animating the scene.

## 1. Download the kit

Download [practice-beat-120bpm.wav](../starter-kit/practice-beat-120bpm.wav) and [shot-list.csv](../starter-kit/shot-list.csv). On GitHub, open a file and select **Download raw file**. To get everything together, choose **Code → Download ZIP** on the repository home page and extract it.

The WAV is a deliberately simple 16-second instrumental, composed and synthesized for this repository. It is not a MusicMaker output. It has 32 beats at 120 beats per minute (BPM), arranged as eight four-beat bars. One beat is 0.5 seconds; one bar is two seconds.

## 2. Choose an official or MusicMaker route

Both routes use the same [four complete shot prompts](../starter-kit/train-shot-prompts.md). Make and inspect A before spending time on B–D. Generate separate shots, then trim each to four seconds.

| Task | Model maker’s tool | MusicMaker tool |
|---|---|---|
| Text-to-video environment shots | [Hailuo MiniMax H3](https://hailuoai.video/tools/minimax-h3): select H3 and text-to-video | [Short-video generator](https://musicmaker.im/free-short-music-video-generator/): describe the shot and choose a ratio |
| Animate your own cover | H3 image / first-and-last-frame mode | Same short-video tool: supply Start Frame and End Frame as requested |
| Animate a vocal portrait | H3 multimodal references; see section 6 | [Music-video generator](https://musicmaker.im/ai-music-video-generator/): music + portrait + action description |

**The connection:** MiniMax develops H3; MusicMaker’s short-video page identifies H3 as its model and offers a simplified music-visual workflow. Controls, allowances and output settings differ. The MusicMaker vocal-demo page does not identify its backend model: that is an alternative workflow, not evidence those demos were made with H3.

### Route A — the model maker’s tool

1. Open [Hailuo H3](https://hailuoai.video/tools/minimax-h3), enter the creation workspace and sign in if requested. Select **MiniMax H3** and text-to-video for this exercise. No audio upload is needed.
2. Paste only shot A from the [shot sheet](../starter-kit/train-shot-prompts.md). Keep its carriage, rainy night, warm light and camera direction. Do not paste all four shots together.
3. Choose **9:16** and **5 seconds**. Use an available resolution; check composition and movement before spending on a higher setting.
4. Preview once for the overall framing, then again for warped windows or lamps. Save a good result as `A.mp4`, along with the actual prompt and settings.
5. Repeat for B, C and D. Keep the location and light consistent while changing the focal detail. Any generated sound will be muted in the edit.

These steps follow [Hailuo’s published workflow](https://hailuoai.video/tools/minimax-h3); see [MiniMax’s release](https://www.minimax.io/blog/minimax-h3) for model capabilities. Account availability can vary. We have not submitted these generation jobs for you.

### Route B — MusicMaker

1. Open the [short-video tool](https://musicmaker.im/free-short-music-video-generator/) and set **Aspect Ratio** to **9:16**.
2. Leave frame inputs empty for text-to-video. Paste the same shot A prompt and choose **Generate**. The page currently describes **5-second, 480p** clips, leaving one second to trim.
3. Preview and download a usable result. Apply the same inspection as route A; save four accepted shots as `A.mp4` through `D.mp4`.
4. For your own cover instead, prepare matching-ratio opening and ending images for **Start Frame / End Frame**. Start with a small visual change; do not simultaneously replace the subject, scene and camera angle.
5. Add music in your editor. This short-scene form is not a whole-song automatic editing workflow. For supplied vocals, use section 6.

Page controls and limits checked **2026-09-23** against the [MusicMaker tool instructions](https://musicmaker.im/free-short-music-video-generator/). Check current settings and allowance before generating.

### Inspect each shot before moving on

| Problem | First change | Accept when |
|---|---|---|
| Carriage, weather or lighting jumps | Remove scene changes; use one location and one camera move | Continuous playback has no sudden replacement |
| Rain, reflections and window frames merge | Simplify the action and reduce motion | The main shapes remain readable |
| The next clip belongs to a different world | Repeat the location, palette and time of day | All four shots look related side by side |

**No generator needed for editing practice:** put the [original concept artwork](../assets/music-video-directions.png) on a 16:9 timeline for 16 seconds with the WAV. This is a music-backed still, not scene animation. To build from a MusicMaker example instead, choose an [illustrated brand project](brand-projects.md), then follow the same generation and editing steps.

## 3. Assemble in an editor

Use any editor with a timeline, separate video/audio tracks, text, and export. If you do not have one, [Shotcut](https://www.shotcut.org/) is a free, open-source desktop option. Its [official tutorials](https://www.shotcut.org/tutorials/) cover the interface. The steps below describe common operations so you can also use an editor you already know.

1. Create a 9:16 project for generated vertical clips, or 16:9 for the still-art exercise.
2. Import the WAV and clips. Put the WAV at the very start of the audio track.
3. Put clip A above it at 0:00. Trim its end to 0:04.
4. Put clip B at 0:04, C at 0:08, and D at 0:12. Trim each to four seconds. The finished timeline ends at 0:16 with no gap.
5. Mute audio attached to all four generated clips. Keep the WAV at a comfortable level; do not boost it into distortion.
6. Add your own title over the last shot. Keep it away from the edges and the area occupied by platform buttons.
7. Optionally import [practice-captions.srt](../starter-kit/practice-captions.srt). It contains one optional closing title, “LAST TRAIN HOME,” at 0:12–0:16, **not sung lyrics**. Replace it with your own title when making a different project. If your editor lacks subtitle import, use the timings as instructions for manual text layers.

| Edit time | Shot | Purpose |
|---|---|---|
| 0:00–0:04 | Wide carriage | Establish the place |
| 0:04–0:08 | Rain on glass | Add texture |
| 0:08–0:12 | Window reflection | Change the composition |
| 0:12–0:16 | Wide carriage + title | Return to the opening idea |

### If you are using Shotcut

Add a video track and an audio track from the Timeline menu. Put the clips on the video track and the WAV on the audio track. For a title, select the final clip and add the **Text: Simple** filter. Saving the project preserves your editable work; use **File → Export → Video** to create a shareable video file. See the [official FAQ](https://www.shotcut.org/FAQ/) for these operations.

## 4. Review and export

Play the full sequence with headphones and then on a phone speaker. Look for black frames at cuts, audio duplication, unreadable text, and a title that disappears too quickly. For a first draft, use MP4 with H.264 video and AAC audio if your editor offers them. Keep the source frame rate; upscaling a 480p source does not create true high-resolution detail.

Play the exported file outside the editor. It should last 16 seconds, have one continuous music track, and contain four clean shots. No one has generated these four clips for you in this repository; this is the reproducible plan and practice audio, with results depending on the generator and your edit.

## 5. Replace the practice track

Import your own song and find a short phrase that feels complete. Re-mark the important beats by listening. Re-time the shots to your track instead of forcing the song into the practice track’s 120 BPM grid. Save a new project version so the exercise remains available.

<a id="vocal"></a>

## 6. Make a vocal portrait instead

MusicMaker’s published guitar demo shows a different route: a character image plus music. **The image below is its input portrait; click to watch the source video.** Prepare your own authorized portrait and recording for the exercise.

<a href="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example1_video.mp4"><img src="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example1_cover.webp" alt="Woman holding a guitar in warm light; MusicMaker demo input portrait, linked to its source video" width="640"></a>

Choose a complete **5–10-second vocal phrase**, starting before the first syllable. Use a clear portrait with an unobstructed mouth. Begin with one shot and one small movement, before combining playing, walking and camera changes.

**Official route:** use **Omni Reference** in [Hailuo H3](https://hailuoai.video/tools/minimax-h3), supplying the portrait and audio together. Identify which file controls appearance and which provides the vocals, using the actual reference labels assigned after upload. If your account has no audio-reference control, a text description cannot replace that input.

**MusicMaker route:** open the [music-video tool](https://musicmaker.im/ai-music-video-generator/), supply the same excerpt under **Music File**, the portrait under **Character Image**, and the action under **Prompt**. Check the **Public** setting and the displayed usage estimate before submitting.

Original practice prompt, not the source demo’s prompt; **not render-tested**:

```text
Use the uploaded portrait for the singer's appearance and the supplied audio
as the timing reference for the performance. Warm stage, locked medium close-up.
Keep clothing, microphone and background consistent. The singer faces the camera,
nods slightly and sings naturally. No turn, no cut, no text.
Keep the mouth unobstructed and hand movement small.
```

First listen for correspondence with the chosen phrase, then inspect mouth movement at the start, middle and end. Check teeth, fingers and microphone for deformation. If the generated audio changes the performance, do not simply replace it with the original and call it synchronized: shorten or redo the take and check again. Avoid doubled audio in the final edit.

Continue with the [illustrated guitar or close-up project](brand-projects.md#performance-1). For environment footage, return to either route in section 2. Discover playback access does not grant reuse rights; [MusicMaker’s commercial terms](https://musicmaker.im/commercial-license/) distinguish plan conditions.
