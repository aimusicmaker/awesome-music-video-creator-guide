# Your first 16-second music visual

[Home](../README.md) · [Practice kit](../starter-kit/README.md) · [中文入门](first-video.zh-CN.md)

Make a small finished edit before attempting a whole song. This walkthrough uses an original instrumental practice track, so you do not need to find music first.

[Download the completed motion-still example](../starter-kit/night-train-edit-demo.mp4). It uses the same beat and four-shot timing, but moves a still image instead of animating the scene.

## 1. Download the kit

Download [practice-beat-120bpm.wav](../starter-kit/practice-beat-120bpm.wav) and [shot-list.csv](../starter-kit/shot-list.csv). On GitHub, open a file and select **Download raw file**. To get everything together, choose **Code → Download ZIP** on the repository home page and extract it.

The WAV is a deliberately simple 16-second instrumental, composed and synthesized for this repository. It is not a MusicMaker output. It has 32 beats at 120 beats per minute (BPM), arranged as eight four-beat bars. One beat is 0.5 seconds; one bar is two seconds.

## 2. Choose how to obtain your visuals

**Generate them:** use [recipe 04](../prompts/04-lofi-loop.md) for the scene and motion direction. Use the [four ready-to-copy shot prompts](../starter-kit/train-shot-prompts.md) to make four separate five-second clips. Keep the same train and lighting, changing the framing between wide carriage, rain detail, window reflection, and wide carriage again. Each clip will be trimmed to four seconds. Review each result before making the next.

**Practice editing without a generator:** import the [concept artwork](../assets/music-video-directions.png) as a still image. Use a landscape timeline for this wide triptych and hold it for the full 16 seconds. This is a simple music-backed still, not an animated video. You can replace the still later with your own clips.

The short-video tool is for individual shots. For a vocal portrait experiment instead, follow [recipe 06](../prompts/06-portrait-performance.md) and the music-video tool’s audio/image route. Do not assume that a short-video scene prompt can produce reliable singing lip-sync.

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
