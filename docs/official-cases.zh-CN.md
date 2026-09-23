# 从模型官方案例开始

[返回首页](../README_ZH.md#official-models) · [English](official-cases.md) · [来源清单](official-cases.json)

核对日期：2026-09-23。下面将官方案例、官方使用说明和本库练习建议分开标注。不是模型排名；没有复现生成结果。所有外部案例和输入素材仍归原权利人所有；练习请换成自有或获授权的素材。

<a id="seedance-concert"></a>

## Seedance 2.5：把一场音乐会分配给不同参考

[![Seedance 2.5 官方音乐会演示截图](../assets/official/seedance-concert.jpg)](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

[▶ 直接观看官方片段](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4xfa4ms8au6q0.mp4)

**官方案例与提示词：** [ByteDance Seed 发布文章](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)中的音乐会段落。原作使用分别编号的场地、主唱、乐器、乐团与合唱团参考，按顺序安排入场、演奏和收尾。完整原提示词与演示保留在官网。

**本库建议的学习步骤：**

1. 先对照官方视频和提示词，记录每份图片负责谁、什么场地或哪件乐器，不要混用编号。
2. 第一次练习缩减为一个场地、一个主唱和一位伴奏者，给人物固定位置。
3. 按“全景介绍→主唱开始→伴奏回应→共同结束”写顺序，先生成短片段，再检查切镜后人物和乐器是否连续。

本练习不是官方原作的完整复现配方；实际可上传的参考数量与时长以所用入口为准。[官方模型页](https://seed.bytedance.com/en/seedance2_5)。

<a id="h3-singing"></a>

## MiniMax H3：人物、运镜、歌声各有来源

[![MiniMax H3 官方演唱示例输入图：咖啡馆中端杯的女子](https://filecdn.minimax.chat/public/h3-en-v2-image-000-1785473644038.png)](https://www.minimax.io/blog/minimax-h3)

[▶ 直接观看官方片段](https://filecdn.minimax.chat/public/h3-en-v2-video-003-1785473642166.mp4)

**官方案例：** [MiniMax 发布文章](https://www.minimax.io/blog/minimax-h3)的 Multimodal context understanding 一节。图为输入人像，原页同时给出运镜视频、歌声音频与生成结果。

**官方入口说明：** [Hailuo H3 使用页](https://hailuoai.video/tools/minimax-h3)。需要同时利用人物与歌声时查看 Omni Reference（多素材参考），音频须配合图片或视频输入。

**本库建议的学习步骤：**

1. 准备一张人像和一句完整的授权歌声；先用固定镜头减少变量。
2. 在参考模式加入素材，明确哪份确定人物、哪份确定歌声。需要运镜时，再补相应视频参考。
3. 先看嘴部与句尾，再检查人物是否改变。若输出声音发生变化，剪辑时选择保留哪条音轨，并重新核对同步。

继续练习可用本库[10 秒人像演唱教程](first-video.zh-CN.md#vocal)。提示词表达的是目标，不保证准确口型。

<a id="veo-instrument"></a>

## Veo：让画面动作与声音描述对应

[![Veo 官方小提琴演奏示例封面](https://lh3.googleusercontent.com/UT25RAscZHkbsQFSSaHjqUuuw8haNKxc73APSp9lP8qG4tPiOOdCI3TyWxSjMNZXYm2Vqn40k_xY6KBGAUoLjsruDZpSqjwvylS0QA_jZEKJyJs9PPs=w1440-h810-n-nu)](https://deepmind.google/models/veo/)

[▶ 直接观看官方片段](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo__veo-3__violinist.webm)

**官方案例：** [Google DeepMind Veo 页面](https://deepmind.google/models/veo/)的小提琴演奏示例。当前页面介绍 Veo 3.1，但该演示素材和对应提示词属于 Veo 3，不改标为 3.1 实测。

**官方教程：** [Veo 提示词指南](https://deepmind.google/models/veo/prompt-guide/)，讲解构图、动作、光线与声音描述。

**本库建议的学习步骤：**

1. 从原页对照演奏画面和声音描述，关注可见动作与期望声音的对应关系。
2. 自己练习时写清一种乐器、一位演奏者、一个场景和一种镜头运动；声音另写一小段。
3. 输出后检查弓、手指与乐器是否稳定，再听音画是否协调。外加已完成歌曲时，关闭不需要的生成声音。

这类演示不证明能逐音符还原你上传的歌曲；也不能把原生声音生成等同于完整歌曲驱动的视频制作。

<a id="act-two-performance"></a>

## Runway Act-Two：用表演视频驱动角色

[![Runway 官方 Act-Two 教程中的人物输入：机舱内的空乘角色](https://help.runwayml.com/hc/article_attachments/43008957767443)](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two)

**官方案例与教程：** [Performance Capture with Act-Two](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two)，展示表演视频、人物图片／视频与输出的对照。图为人物输入；这是通用表演迁移案例，不是官方歌曲成片。

**按官方教程操作：**

1. 在 Runway 的 Apps 中打开 Performance Capture with Act-Two；准备单人、不切镜、脸部清楚的表演视频和人物参考。
2. 上传两类输入。若使用人物图片，可设置 Gestures（动作控制）；人物视频则保留原有运镜与环境运动，不能按同样方式控制肢体。
3. 先用默认表情强度，查看预计消耗后生成；出现表情失真再减少强度或调整输入。

**用于音乐视频的本库建议：** 自录一段有使用权的演唱表演作为驱动素材，先做固定近景。不要只上传音频便期待完成表演迁移。官方页面目前要求 Standard 或更高计划。
