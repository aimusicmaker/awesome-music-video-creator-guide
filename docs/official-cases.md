# Learn from official model examples

[Home](../README.md#official-models) · [简体中文](official-cases.zh-CN.md) · [Source manifest](official-cases.json)

Checked 2026-09-23. Official examples, maker documentation and our practice suggestions are labeled separately. These are not our generation tests or a ranking. Linked media retain their original rights; use your own or authorized inputs for practice.

<a id="seedance-concert"></a>

## Seedance 2.5: assign concert references clearly

[MusicMaker · Seedance 2.5 ↗](https://musicmaker.im/model/seedance-2-5/)

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

[MusicMaker · MiniMax H3 ↗](https://musicmaker.im/model/minimax-h3/)

[![Official H3 character input: a woman holding a cup in a cafe](https://filecdn.minimax.chat/public/h3-en-v2-image-000-1785473644038.png)](https://www.minimax.io/blog/minimax-h3)

[▶ Watch the official clip](https://filecdn.minimax.chat/public/h3-en-v2-video-003-1785473642166.mp4)

**Official example:** the multimodal-context section of [MiniMax’s release](https://www.minimax.io/blog/minimax-h3). This is its character input; the page also provides camera and vocal references and the result. [Hailuo’s H3 guide](https://hailuoai.video/tools/minimax-h3) explains the available input modes; audio reference needs an image or video alongside it.

**Our practice steps:**

1. Prepare a portrait and one authorized vocal phrase. Start with a fixed camera.
2. Use the reference mode and explain which input determines identity and which supplies vocals; add a camera reference only when needed.
3. Check mouth timing and identity, then choose one soundtrack and recheck synchronization in the edit.

Continue with our [portrait-singing walkthrough](first-video.md#vocal). Prompted timing is a target, not a guarantee.

<a id="veo-scene"></a>

## Veo 3.1: place a singer in a surreal garden

[![Veo · official garden-singing input/output comparison](https://lh3.googleusercontent.com/B3TEWPmHGddbqymciVXc6yVwXbmxZtTBG5PZrUHNZbgISHlOLJokWGoDR0Dqfug4QPIzNUgP9T23Iktd11yMvzfYLqURXmvCDGLr1RIliT9VeZs82g=w1440-h810-n-nu)](https://deepmind.google/models/veo/)

[▶ Watch the official clip](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo-3__visual-identity-preservation-3__9x16__light.webm) · [MusicMaker · Veo 3.1 ↗](https://musicmaker.im/model/veo-3-1-ai/)

**Official example:** the Add ingredients to your video showcase on the [current Veo 3.1 page](https://deepmind.google/models/veo/) shows a singer in an abstract garden with floating macarons. The clip, prompt and input/output comparison are public: three reference images appear on the left and the output on the right. We have not obtained the separate original inputs or complete generation settings. Its media filename retains `veo-3`; we group it by the current 3.1 capability page without asserting the individual clip’s generation version.

**Official guidance:** [Veo prompting](https://deepmind.google/models/veo/prompt-guide/) and [Veo 3.1 inputs and controls](https://ai.google.dev/gemini-api/docs/video).

**Our practice steps:**

1. Separate character appearance, setting, floating objects and performance when studying the original.
2. For your own exercise, prepare authorized character and setting images, then plan one shot with restrained singing and slow floral motion. This is our suggestion, not a complete reproduction recipe.
3. Open MusicMaker, check the Veo 3.1 or Fast selection, and use the text or first-frame controls available. Do not assume its interface exposes official multi-image Ingredients controls; if absent, try a prepared composite scene as a first frame instead.
4. Check identity, mouth visibility and sound. When using your own song, keep one soundtrack and recheck synchronization before exporting.

<a id="seedance-piano"></a>

## Seedance 2.0: performance first, expression next

[![Seedance 2.0 · official piano performance poster](https://p11-sign.douyinpic.com/tos-cn-p-13c08f/6867a9183a794734882c56d613a4fba5_1770872187~tplv-noop.image?dy_q=1770875442&l=20260212134538DCD5D5DD0148D91D5FFB&x-expires=2086235454&x-signature=F%2B11iuE4gyzLtI%2BIRgWao6c8W0g%3D)](https://seed.bytedance.com/en/seedance2_0)

**Official example and prompt:** the black-suited pianist in the [Seedance 2.0 showcase](https://seed.bytedance.com/en/seedance2_0). The maker supplies the clip and prompt, covering performance framing, an expression close-up and sound. This does not demonstrate performance driven by an uploaded song.

**Our practice steps:**

1. Watch the official clip and separate subject, lighting, action, cut and sound directions.
2. Start your own exercise with one pianist in a medium shot and one cut to the face. Leave out audience shots, orbiting cameras and location changes.
3. Check hands, keys and clothing continuity. When editing to your own track, mute generated audio and place cuts around the musical phrase.

**Brand route:** open MusicMaker Seedance 2.0 below, confirm the selected version and use the text or image controls actually available. Check reference limits, duration and credits in that interface.

[MusicMaker · Seedance 2.0 ↗](https://musicmaker.im/model/seedance-2-0/)
