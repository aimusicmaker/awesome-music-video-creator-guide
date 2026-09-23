# Models: official sources and practical choices

[Home](../README.md) · [中文首页](../README_ZH.md) · [Creator examples](x-cases.md)

Checked **2026-09-23**. These are model makers’ descriptions, not our quality measurements. MusicMaker and other interfaces may expose only part of a model’s capabilities.

## Seedance 2.5

**Official source:** [ByteDance Seed model page](https://seed.bytedance.com/en/seedance2_5).

ByteDance describes joint sound-and-picture generation, videos up to 30 seconds in one generation, and reference/editing controls. For a music video, decide which input establishes the performer, which establishes the camera, and which establishes the soundtrack. Do not assume that a product with the model’s name accepts every reference type.

**中文：** 官方介绍了音视频联合生成、单次最长 30 秒与参考/编辑能力。实际创作时分别说明人物、运镜和声音由哪份素材确定；产品页面出现模型名称，不等于开放了全部参考输入。

[Related case / 对应案例：双人舞](x-cases.zh-CN.md#duo) · [MusicMaker model route](https://musicmaker.im/model/seedance-2-5/)

## Seedance 2.0

**Official source:** [ByteDance Seedance 2.0 model page](https://seed.bytedance.com/en/seedance2_0). The maker describes text, image, audio and video inputs and reference controls. Our linked motion-design example is labeled 2.0 by its author; it must not be relabeled 2.5.

**中文：** 官方介绍了文字、图片、音频和视频输入及参考控制。这里的动态图形案例由作者标为 2.0，不能因为当前推荐 2.5 就改写原案例的模型名称。

## MiniMax H3

**Official source:** [MiniMax H3 release, July 31, 2026](https://www.minimax.io/blog/minimax-h3).

MiniMax describes combined text, image, video and audio context, stereo audio, and up to 15 seconds at 2K. Its release includes a singing example that assigns camera movement, character appearance and vocals to different references. Use this distinction when preparing assets; more adjectives cannot substitute for missing reference inputs.

**中文：** 官方介绍了文字、图像、视频、音频的组合输入，并提供演唱示例：运镜、人物、声音分别来自不同参考。准备素材时可照着这个分工；如果入口不支持某种参考，增加形容词也不能补上缺失输入。

[Related workflow / 对应工作流](x-cases.zh-CN.md#h3-performance). MusicMaker’s [free short-video route](https://musicmaker.im/free-short-music-video-generator/) listed **5-second, 480p** clips when checked; those interface limits differ from the model-level announcement. Treat longer recipe durations as editing targets.

## MiniMax Music 3.0

**Official source:** [MiniMax Music 3.0 release, August 13, 2026](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model).

The release describes creating complete songs from a concept and optional lyrics, with structured control over song sections. Write where an instrument enters, where energy increases, and where the arrangement becomes sparse. Finish the audio before placing exact video cuts.

**中文：** 官方介绍了从构思与可选歌词生成歌曲，以及按歌曲段落控制编排。提示词可以写清乐器何时进入、情绪何时增强、何处减少伴奏；先确定音轨，再精确安排剪辑点。

[MusicMaker music route](https://musicmaker.im/minimax/minimax-music-v3-0/) · [Full-song storyboard](../prompts/12-full-song.md)

## Eleven Music

**Official source:** [ElevenLabs music prompting best practices](https://elevenlabs.io/docs/overview/capabilities/music/best-practices).

The guide recommends specifying musical style, feeling, instruments, speed and production period, with explicit arrangement and vocal choices. For a loop, make the intended length and ending behavior clear. Avoid relying on a vague mood word alone.

**中文：** 官方建议具体描述曲风、情绪、乐器、速度、制作年代，以及编排和人声需求。循环音乐还需说明长度与结尾如何处理，不只写“有氛围”。

[MusicMaker music route](https://musicmaker.im/eleven-labs/eleven-labs-music/) · [Loop recipe](../prompts/04-lofi-loop.md)

## Use the official or MusicMaker workflow / 选择官方或品牌入口

For a first project, follow the [English walkthrough](first-video.md) or [中文逐步教程](first-video.zh-CN.md): the same shot plan can be used in [official Hailuo H3](https://hailuoai.video/tools/minimax-h3) or the [MusicMaker short-video tool](https://musicmaker.im/free-short-music-video-generator/). The tutorial explains the actual input steps and the separate audio-and-portrait route for singing.

第一次制作可直接跟着教程操作：两种入口共用同一分镜，区别在于输入控件与输出设置。先看[品牌素材衍生的图文提案](brand-projects.zh-CN.md)，选中画面后再决定用哪个入口。

## Before you generate / 开始前

Keep the song you intend to publish as the timing reference. If you generate visuals separately, mute unwanted clip audio and align cuts in the editor. A prompt requesting accurate lip-sync or beat alignment does not prove the resulting clip achieved it.

先确定最终要使用的歌曲。画面单独生成时，关掉不需要的片段音频，并在剪辑软件对齐切点。提示词要求“口型准确”或“卡点”，不等于成片已达到要求。

[Tool/source notes](sources.md) · [Editing help](editing.md)
