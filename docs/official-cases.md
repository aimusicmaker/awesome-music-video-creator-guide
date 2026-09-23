# Learn from official model examples

[Home](../README.md#official-models) · [简体中文](official-cases.zh-CN.md) · [Source manifest](official-cases.json)

Checked 2026-09-23. Official examples, maker documentation and our practice suggestions are labeled separately. These are not our generation tests or a ranking. Linked media retain their original rights; use your own or authorized inputs for practice.

<a id="seedance-concert"></a>

## Seedance 2.5: assign concert references clearly

[![Frame from Seedance 2.5’s official concert demonstration](../assets/official/seedance-concert.jpg)](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

[▶ Watch the official clip](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4xfa4ms8au6q0.mp4)

**Official example and prompt:** the concert section in [ByteDance Seed’s release](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) assigns separate numbered references to the venue, performers and ensembles. Watch the original and read its full prompt there.

**Our practice steps:**

1. Map each reference to a specific person, instrument or location.
2. Simplify your own exercise to a venue, singer and accompanist with fixed positions.
3. Plan an establishing view, vocal entrance, instrumental response and ending. Generate a short test and inspect continuity across cuts.

This is a learning adaptation, not a reproduction recipe. Reference limits depend on the chosen interface. [Official model page](https://seed.bytedance.com/en/seedance2_5).

<a id="h3-singing"></a>

## MiniMax H3: separate character, camera and vocals

[![Official H3 character input: a woman holding a cup in a cafe](https://filecdn.minimax.chat/public/h3-en-v2-image-000-1785473644038.png)](https://www.minimax.io/blog/minimax-h3)

[▶ Watch the official clip](https://filecdn.minimax.chat/public/h3-en-v2-video-003-1785473642166.mp4)

**Official example:** the multimodal-context section of [MiniMax’s release](https://www.minimax.io/blog/minimax-h3). This is its character input; the page also provides camera and vocal references and the result. [Hailuo’s H3 guide](https://hailuoai.video/tools/minimax-h3) explains the available input modes; audio reference needs an image or video alongside it.

**Our practice steps:**

1. Prepare a portrait and one authorized vocal phrase. Start with a fixed camera.
2. Use the reference mode and explain which input determines identity and which supplies vocals; add a camera reference only when needed.
3. Check mouth timing and identity, then choose one soundtrack and recheck synchronization in the edit.

Continue with our [portrait-singing walkthrough](first-video.md#vocal). Prompted timing is a target, not a guarantee.

<a id="veo-instrument"></a>

## Veo: connect visible action with sound design

[![Official Veo violin performance poster](https://lh3.googleusercontent.com/UT25RAscZHkbsQFSSaHjqUuuw8haNKxc73APSp9lP8qG4tPiOOdCI3TyWxSjMNZXYm2Vqn40k_xY6KBGAUoLjsruDZpSqjwvylS0QA_jZEKJyJs9PPs=w1440-h810-n-nu)](https://deepmind.google/models/veo/)

[▶ Watch the official clip](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo__veo-3__violinist.webm)

**Official example:** the violin performance on [Google DeepMind’s Veo page](https://deepmind.google/models/veo/). The current page presents Veo 3.1, but this retained example is labeled Veo 3; we do not relabel it as a 3.1 test.

**Official tutorial:** the [Veo prompt guide](https://deepmind.google/models/veo/prompt-guide/) covers framing, movement, light and sound.

**Our practice steps:**

1. Compare the official performance with its audio description.
2. For your own shot, choose one instrument, performer, setting and camera movement; write the sound direction separately.
3. Inspect hands and instrument continuity, then listen for audiovisual coherence. Mute unwanted generated sound if you edit to an existing song.

Native sound generation is not evidence of note-perfect reproduction or full-song audio-driven video.

<a id="act-two-performance"></a>

## Runway Act-Two: drive a character with a performance

[![Official Act-Two character input: a flight attendant in an aircraft cabin](https://help.runwayml.com/hc/article_attachments/43008957767443)](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two)

**Official example and tutorial:** [Performance Capture with Act-Two](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two) compares driving footage, character inputs and results. The image is an input from a general acting example, not an official song video.

**Follow the official workflow:**

1. Open Act-Two in Runway Apps. Prepare uninterrupted footage of one clearly visible performer and a character image or video.
2. Upload both inputs. Gesture control applies to character images; character videos retain their original camera and environment movement.
3. Start with default expressiveness, review usage, then generate. Reduce expressiveness or improve the inputs if artifacts appear.

**Our music-video adaptation:** record an authorized vocal performance for the driving video and start with a close-up. Audio alone is not the required driving input. The official page currently requires Standard or higher.
