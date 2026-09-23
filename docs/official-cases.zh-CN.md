# 从模型官方案例开始

[返回首页](../README_ZH.md#official-models) · [English](official-cases.md) · [来源清单](official-cases.json)

核对日期：2026-09-23。下面将官方案例、官方使用说明和本库练习建议分开标注。不是模型排名；没有复现生成结果。所有外部案例和输入素材仍归原权利人所有；练习请换成自有或获授权的素材。

<a id="seedance-concert"></a>

## Seedance 2.5：把一场音乐会分配给不同参考

[MusicMaker · Seedance 2.5 ↗](https://musicmaker.im/model/seedance-2-5/)

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

[MusicMaker · MiniMax H3 ↗](https://musicmaker.im/model/minimax-h3/)

[![MiniMax H3 官方演唱示例输入图：咖啡馆中端杯的女子](https://filecdn.minimax.chat/public/h3-en-v2-image-000-1785473644038.png)](https://www.minimax.io/blog/minimax-h3)

[▶ 直接观看官方片段](https://filecdn.minimax.chat/public/h3-en-v2-video-003-1785473642166.mp4)

**官方案例：** [MiniMax 发布文章](https://www.minimax.io/blog/minimax-h3)的 Multimodal context understanding 一节。图为输入人像，原页同时给出运镜视频、歌声音频与生成结果。

**官方入口说明：** [Hailuo H3 使用页](https://hailuoai.video/tools/minimax-h3)。需要同时利用人物与歌声时查看 Omni Reference（多素材参考），音频须配合图片或视频输入。

**本库建议的学习步骤：**

1. 准备一张人像和一句完整的授权歌声；先用固定镜头减少变量。
2. 在参考模式加入素材，明确哪份确定人物、哪份确定歌声。需要运镜时，再补相应视频参考。
3. 先看嘴部与句尾，再检查人物是否改变。若输出声音发生变化，剪辑时选择保留哪条音轨，并重新核对同步。

继续练习可用本库[10 秒人像演唱教程](first-video.zh-CN.md#vocal)。提示词表达的是目标，不保证准确口型。

<a id="veo-scene"></a>

## Veo 3.1：把演唱放进奇幻花园

[![Veo · 官方花园演唱输入与输出对照](https://lh3.googleusercontent.com/B3TEWPmHGddbqymciVXc6yVwXbmxZtTBG5PZrUHNZbgISHlOLJokWGoDR0Dqfug4QPIzNUgP9T23Iktd11yMvzfYLqURXmvCDGLr1RIliT9VeZs82g=w1440-h810-n-nu)](https://deepmind.google/models/veo/)

[▶ 观看官方片段](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo-3__visual-identity-preservation-3__9x16__light.webm) · [MusicMaker · Veo 3.1 ↗](https://musicmaker.im/model/veo-3-1-ai/)

**官方案例：** [Veo 3.1 当前官网](https://deepmind.google/models/veo/)的 Add ingredients to your video（用参考素材生成视频）展示，内容是人物在抽象花园中演唱，周围有漂浮的马卡龙。官方公开了成片、提示词，以及参考图与输出的对照；上图左侧是三张输入图，右侧是生成画面。本库未取得独立原始参考文件与完整生成设置。该视频文件名仍含 `veo-3`，这里按当前 3.1 能力展示页归类，不据此断言单条片段的生成版本。

**官方教程：** [Veo 提示词指南](https://deepmind.google/models/veo/prompt-guide/)；[Veo 3.1 输入与功能说明](https://ai.google.dev/gemini-api/docs/video)。

**本库建议的学习步骤：**

1. 先看原片，分开观察人物外观、花园风格、漂浮物和演唱动作；参考图承担不同角色，不要混成一个模糊描述。
2. 自己练习时准备有使用权的人物图与环境图，先做人物轻微演唱、花朵缓慢运动的单镜头。这是新编练习建议，不是原作的完整复现配方。
3. 到 MusicMaker 页面核对 Veo 3.1 或 Fast 选项，按当前控件选择文字或首帧输入。页面没有提供多参考图控件时，不要把官方 Ingredients 工作流当成品牌已开放功能；可先制作一张合成场景图再尝试首帧路线。
4. 检查人物是否保持一致、嘴部是否被遮挡、声音是否符合预期。若配自己的歌曲，保留一条音轨，重新核对同步后导出。

<a id="seedance-piano"></a>

## Seedance 2.0：先拍演奏，再切表情

[![Seedance 2.0 · 官方钢琴演奏视频封面](https://p11-sign.douyinpic.com/tos-cn-p-13c08f/6867a9183a794734882c56d613a4fba5_1770872187~tplv-noop.image?dy_q=1770875442&l=20260212134538DCD5D5DD0148D91D5FFB&x-expires=2086235454&x-signature=F%2B11iuE4gyzLtI%2BIRgWao6c8W0g%3D)](https://seed.bytedance.com/en/seedance2_0)

**官方案例与提示词：** [Seedance 2.0 官方展示页](https://seed.bytedance.com/en/seedance2_0)中的黑色西装钢琴家。原页提供演示及提示词，说明演奏中景、表情特写和声音安排；这不是上传歌曲驱动演奏的证明。

**本库建议的学习步骤：**

1. 先看官方演示，分别记下主体、光线、动作、切镜和声音如何描述。
2. 自己练习时先做一位钢琴家的中景，只安排一次切到面部特写；不要同时加入观众、绕拍和换场。
3. 检查琴键、双手和切镜后的衣着是否稳定。若配自己的歌曲，剪辑时关闭生成声音，再按乐句安排切点。

**品牌路线：** 打开下方 MusicMaker Seedance 2.0 页面，核对当前模型版本，按界面选择文字或图片输入；参考数量、时长和额度以实际界面为准。

[MusicMaker · Seedance 2.0 ↗](https://musicmaker.im/model/seedance-2-0/)
