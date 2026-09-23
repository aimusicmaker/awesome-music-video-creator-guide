<div align="center">

# 音乐视频创作指南

**让你的歌，有一个值得被看见的画面。**

写给独立音乐人和第一次制作音乐视频的创作者。<br>
12 套原创方案 · 可下载练习音乐 · 分镜与字幕模板 · 官方案例参考

[开始制作](#做出第一支视频) · [选择方案](#按用途选择方案) · [下载 16 秒示例](starter-kit/night-train-edit-demo.mp4) · [案例参考](docs/inspiration.md) · [English](README.md)

![三种原创画面方向：天台演出、液态金属圆环和雨夜列车](assets/music-video-directions.png)

<sub>本仓库用 AI 制作的概念图，用于展示创意方向，并非 MusicMaker 生成视频的效果截图。</sub>

[制作天台画面](prompts/README_ZH.md#recipe-08) · [制作金属圆环](prompts/README_ZH.md#recipe-05) · [制作雨夜列车](prompts/README_ZH.md#recipe-04)

</div>

**先看一个完成的剪辑练习：** [下载 16 秒雨夜列车视频](starter-kit/night-train-edit-demo.mp4)。它把原创静态图裁成四个镜头，添加简单推拉运动和练习音乐；图中的雨和场景本身没有生成动画，也不是 MusicMaker 实测结果。在 GitHub 文件页点击 **Download raw file** 下载，再用视频播放器打开。

## 你想做什么？

| 目标 | 从这里开始 | 做出来是什么 |
|---|---|---|
| 让专辑封面动起来 | [动态封面](prompts/README_ZH.md#recipe-01) | 保留原构图，只增加轻微运动 |
| 为新歌做短视频 | [发歌预告](prompts/README_ZH.md#recipe-02) | 四个镜头组成的短片 |
| 把歌词放进画面 | [歌词视频](prompts/README_ZH.md#recipe-03) | 简洁背景，加上清楚易读的字幕 |
| 为纯音乐搭配氛围 | [雨夜列车](prompts/README_ZH.md#recipe-04) | 可以尝试循环播放的场景 |
| 配合电子乐的变化 | [金属圆环](prompts/README_ZH.md#recipe-05) | 在音乐转折处改变光线或画面 |
| 让人物照片配合演唱 | [人像演唱](prompts/README_ZH.md#recipe-06) | 先做一小段音画配合测试 |

**还没有自己的歌？** 下载[16 秒练习包](starter-kit/README.md)：原创练习音乐、分镜表和字幕时间轴已经备好。下载不需要注册。

本仓库由 [AI Music Maker](https://musicmaker.im/) 维护。方法也适用于你熟悉的生成工具和剪辑软件。中文版首页、[中文入门教程](docs/first-video.zh-CN.md)和[12 套中文操作卡片](prompts/README_ZH.md)可独立使用；英文提示词可以直接复制。

## 做出第一支视频

**先完成一支 16 秒的雨夜列车短片。** 准备[练习音乐](starter-kit/practice-beat-120bpm.wav)、四段画面和一个可以分别放入视频、音频的剪辑软件。

1. **下载音乐。** 打开 WAV 文件，在 GitHub 文件页选择下载。音乐速度是每分钟 120 拍，共 8 个小节，每小节 4 拍、2 秒。
2. **先生成一个镜头。** 打开 [MusicMaker 短片工具](https://musicmaker.im/free-short-music-video-generator/)，选择 9:16 竖屏，把下方提示词粘贴进去，生成 A 镜头（车厢全景）。本练习可以从文字开始。
3. **再做剩余三个镜头。** 使用[分镜提示词页](starter-kit/train-shot-prompts.md)中的 **B、C、D**：雨滴特写、玻璃倒影、回到全景。这样一共四段，不需要再次生成 A。
4. **按音乐剪辑。** 音乐从 0 秒开始，四段画面各取 4 秒，在第 4、8、12 秒切换。关闭生成视频自带的声音，保留一条连续音乐。
5. **添加片名并导出。** 在最后一个镜头加标题，用手机检查裁切和文字大小。首次剪辑可按[中文完整教程](docs/first-video.zh-CN.md)操作。

```text
An empty night train carriage, teal fabric seats, a small amber reading
lamp and rain on the window. Distant city lights move slowly outside.
Locked camera. Only the rain and outside lights move; the seats and lamp
remain perfectly still. Quiet, intimate mood, textured painted illustration.
Vertical composition, no people, no lettering, no cuts, no camera shake.
```

这段提示词的意思是：空荡的雨夜列车，青绿色座椅、暖色台灯，镜头固定，只让窗外灯光和雨滴缓慢移动，不出现人物或文字。

截至 2026 年 9 月 23 日，[短片工具页面](https://musicmaker.im/free-short-music-video-generator/)标注的是 5 秒、480p 画面。这里的 16 秒短片需要**把多个镜头剪在一起**。功能以实际页面为准；把低分辨率素材导出成大尺寸，不等于增加细节。

## 先看品牌现有示例

<p align="center">
<a href="https://musicmaker.im/ai-music-video-generator/">
<img src="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example1_cover.webp" alt="MusicMaker 吉他演唱示例的输入图片，点击前往原网页观看视频" width="360">
</a>
</p>

**吉他演唱：MusicMaker 官网演示。** [观看视频](https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example1_video.mp4) · [查看来源页](https://musicmaker.im/ai-music-video-generator/)

这段示例来自品牌网页，不是本仓库实测生成的结果。想用自己的歌和照片尝试，可从[人像演唱方案](prompts/README_ZH.md#recipe-06)开始，先检查一小段里的嘴型、脸部和手部表现。

## 按用途选择方案

每套方案包含输入素材、画面提示词、运动提示词、音乐方向、剪辑方法和失败后的改法。均为原创创作方案，**尚未逐条生成视频验证**。

| 方案 | 难度 | 建议剪辑长度 |
|---|---|---|
| [01 · 动态专辑封面](prompts/README_ZH.md#recipe-01) | 入门 | 8 秒 |
| [02 · 四镜头发歌预告](prompts/README_ZH.md#recipe-02) | 入门 | 16 秒 |
| [03 · 窗边歌词视频](prompts/README_ZH.md#recipe-03) | 入门 | 16 秒 |
| [04 · 雨夜末班车](prompts/README_ZH.md#recipe-04) | 入门 | 8 秒画面循环 |
| [05 · 液态金属圆环](prompts/README_ZH.md#recipe-05) | 进阶 | 16 秒 |
| [06 · 人像演唱](prompts/README_ZH.md#recipe-06) | 进阶 | 工具支持的一小段人声 |
| [07 · 剪纸角色故事](prompts/README_ZH.md#recipe-07) | 进阶 | 20 秒 |
| [08 · 天台余晖](prompts/README_ZH.md#recipe-08) | 入门 | 16 秒 |
| [09 · 公路旅行日记](prompts/README_ZH.md#recipe-09) | 入门 | 20 秒 |
| [10 · 同一道具，三个世界](prompts/README_ZH.md#recipe-10) | 进阶 | 12 秒 |
| [11 · 副歌亮灯](prompts/README_ZH.md#recipe-11) | 进阶 | 16 秒 |
| [12 · 完整歌曲分镜](prompts/README_ZH.md#recipe-12) | 高阶 | 按实际歌曲长度 |

这些时长是剪辑目标，不是单次生成的承诺。画面需要准确跟上音乐时，在剪辑软件里对齐切点；单靠提示词里的“跟随节拍”不能保证准确。

## 听音乐，找画面方向

打开 [MusicMaker Discover](https://musicmaker.im/discover/)，听听不同音乐让你想到什么画面。可以先打开 [Neon Pulse](https://musicmaker.im/detail/discover-v2-94/)，本次已确认其播放器能正常播放。[Echoes of You](https://musicmaker.im/detail/discover-v2-95/) 和 [The Open Road](https://musicmaker.im/detail/discover-v2-104/) 是另外两个已核对的曲库条目，本次未测试播放。

先选一段完整乐句，找出希望强调的音乐变化，再选画面方案。这里不按歌名推断曲风或速度。详情页无法加载时，可回到 Discover 按曲名查找。想直接下载音乐练习，可以用仓库内的[原创 16 秒配乐](starter-kit/README.md)；曲库作品的再使用需要另行确认授权。

## 从成熟案例学什么？

- **Lofi Girl：** 学习固定场景如何陪伴长时间听歌。[来源与改编练习](docs/inspiration.md#lofi-girl)。
- **OK Go《The One Moment》：** 学习先选音乐中的重点，再安排视觉变化。[官方制作说明与练习](docs/inspiration.md#ok-go)。
- **Gorillaz《Cracker Island》：** 观察角色在不同镜头中保留哪些识别特征。[官方视频与练习](docs/inspiration.md#gorillaz)。

以上是学习参考，不是 MusicMaker 客户案例，也不代表作品用 AI 制作。仓库不提供这些作品的音乐或视频下载。

## 选对工具入口

| 你手里有什么 | 入口 | 接下来做什么 |
|---|---|---|
| 一个画面想法 | [短片生成工具](https://musicmaker.im/free-short-music-video-generator/) | 逐镜头生成，再在剪辑软件中配乐 |
| 音乐和人物图片 | [音乐视频工具](https://musicmaker.im/ai-music-video-generator/) | 上传素材，先测试短片段 |
| 还没有音乐方向 | [Discover 曲库](https://musicmaker.im/discover/) | 先找灵感，再制作或授权自己的音乐 |
| 已有全部画面 | [剪辑说明（英文）](docs/editing.md) | 配乐、加字幕、检查导出文件 |

音乐视频表单显示积分估算和 Public（是否公开）开关，提交前先确认。这里只核查了公开页面，没有测试付费生成质量。[来源记录](docs/sources.md)。

## 常见问题，先这样改

| 问题 | 先改这一项 |
|---|---|
| 人物变脸、衣服变化 | 复用同一张参考图，缩短镜头并减少动作 |
| 歌词写错 | 只生成背景，文字放到剪辑软件里添加 |
| 画面变化没对上音乐 | 调整切点，不要把整段重做 |
| 循环接头明显 | 固定镜头，找相近的首尾画面，连续播放两遍检查 |
| 镜头之间像不同作品 | 固定颜色、地点、道具和运镜规则 |
| 音乐像播放了两遍 | 关闭各段视频自带音频，只留选定的音乐 |

## 分享你的做法

欢迎[提交方案](https://github.com/aimusicmaker/awesome-music-video-creator-guide/issues/new?template=recipe.yml)：写清素材、提示词、结果，以及哪一步失败、如何修改。[贡献说明](CONTRIBUTING.md)。

**准备好为自己的歌做画面了吗？** [先生成一个短镜头](https://musicmaker.im/free-short-music-video-generator/)，或[带着音乐和照片开始](https://musicmaker.im/ai-music-video-generator/)。

原创文字、代码和练习音乐采用 [MIT 许可](LICENSE)。图片和外部案例见[素材说明](assets/README.md)；仓库许可不包含第三方歌曲和视频。
