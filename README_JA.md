<h1 align="center">ミュージックビデオ制作ガイド</h1>

<!-- BRAND:START -->
<p align="center"><a href="https://musicmaker.im/"><img src="https://musicmaker.im/images/logo.svg" alt="MusicMaker logo" width="88" height="88"></a></p>
<!-- BRAND:END -->

<!-- LANGUAGES:START -->
<p align="center">🌐 <a href="README.md"><kbd>English</kbd></a> · <b>日本語</b> · <a href="README_ID.md"><kbd>Bahasa Indonesia</kbd></a> · <a href="README_IT.md"><kbd>Italiano</kbd></a> · <a href="README_PT.md"><kbd>Português</kbd></a> · <a href="README_ES.md"><kbd>Español</kbd></a> · <a href="README_DE.md"><kbd>Deutsch</kbd></a> · <a href="README_RU.md"><kbd>Русский</kbd></a> · <a href="README_FR.md"><kbd>Français</kbd></a> · <a href="README_ZH.md"><kbd>简体中文</kbd></a> · <a href="README_TW.md"><kbd>繁體中文</kbd></a> · <a href="README_KO.md"><kbd>한국어</kbd></a> · <a href="README_TH.md"><kbd>ไทย</kbd></a> · <a href="README_VI.md"><kbd>Tiếng Việt</kbd></a> · <a href="README_AR.md"><kbd>العربية</kbd></a></p>
<!-- LANGUAGES:END -->

<!-- DEVICE:START -->
<p align="center"><a href="mobile/README_JA.md"><kbd>📱 モバイル版</kbd></a></p>
<!-- DEVICE:END -->

<p align="center"><strong>一曲に、最後まで見たくなる映像を。作品を見て、作り方を学び、自分の短い動画を完成させましょう。</strong></p>

<p align="center"><a href="#official-models"><kbd>✦ モデル公式の作例とチュートリアル</kbd></a> &nbsp; <a href="#x-creators"><kbd>▶ Xの作例</kbd></a> &nbsp; <a href="#listen"><kbd>♫ MusicMakerで試聴</kbd></a> &nbsp; <a href="#first-video"><kbd>✦ 最初の動画</kbd></a> &nbsp; <a href="#next-project"><kbd>→ 次の練習</kbd></a> &nbsp; <a href="#toolkit"><kbd>🧰 無料ツール</kbd></a></p>

[![曲を選ぶ → 絵コンテとプロンプト → 映像生成 → 編集と書き出し。歌唱、旅、抽象映像へ広がる制作フローのオリジナル図です。](assets/social-preview.jpg)](#first-video)

曲を選ぶ → 絵コンテとプロンプト → 映像生成 → 編集と書き出し。歌唱、旅、抽象映像へ広がる制作フローのオリジナル図です。

<!-- OFFICIAL:START -->
<a id="official-models"></a>

## モデル公式の作例とチュートリアル

開発元の作例と入力方法を見てから、コミュニティの応用へ。

<table>
<tr>
<td width="50%" valign="top"><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5"><img src="assets/official/seedance-concert.jpg" alt="Frame from the official Seedance 2.5 concert demonstration" width="100%"></a><br><sub>公式デモのフレーム</sub><br><b>Seedance 2.5</b> · ByteDance Seed<br>演奏会：会場と演奏者の参照を分ける。<br><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5"><kbd>▶ 公式作例</kbd></a> · <a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#seedance-concert">手順ノート（英語） →</a> · <a href="https://musicmaker.im/model/seedance-2-5/"><kbd>MusicMaker ↗</kbd></a></td>
<td width="50%" valign="top"><a href="https://www.minimax.io/blog/minimax-h3"><img src="https://filecdn.minimax.chat/public/h3-en-v2-image-000-1785473644038.png" alt="Official MiniMax H3 character reference image for the singing demonstration" width="100%"></a><br><sub>公式入力画像</sub><br><b>MiniMax H3</b> · MiniMax<br>歌唱：カメラ・人物・歌声の参照を分ける。<br><a href="https://www.minimax.io/blog/minimax-h3"><kbd>▶ 公式作例</kbd></a> · <a href="https://hailuoai.video/tools/minimax-h3">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#h3-singing">手順ノート（英語） →</a> · <a href="https://musicmaker.im/model/minimax-h3/"><kbd>MusicMaker ↗</kbd></a></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://deepmind.google/models/veo/"><img src="https://lh3.googleusercontent.com/B3TEWPmHGddbqymciVXc6yVwXbmxZtTBG5PZrUHNZbgISHlOLJokWGoDR0Dqfug4QPIzNUgP9T23Iktd11yMvzfYLqURXmvCDGLr1RIliT9VeZs82g=w1440-h810-n-nu" alt="Official Veo comparison: three reference images beside a singer in an abstract flower garden" width="100%"></a><br><sub>公式の入力・出力比較</sub><br><b>Veo 3.1</b> · Google DeepMind<br>幻想的な歌唱シーン：人物と背景の参照を組み合わせる。<br><a href="https://deepmind.google/models/veo/"><kbd>▶ 公式作例</kbd></a> · <a href="https://deepmind.google/models/veo/prompt-guide/">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#veo-scene">手順ノート（英語） →</a> · <a href="https://musicmaker.im/model/veo-3-1-ai/"><kbd>MusicMaker ↗</kbd></a></td>
<td width="50%" valign="top"><a href="https://seed.bytedance.com/en/seedance2_0"><img src="https://p11-sign.douyinpic.com/tos-cn-p-13c08f/6867a9183a794734882c56d613a4fba5_1770872187~tplv-noop.image?dy_q=1770875442&l=20260212134538DCD5D5DD0148D91D5FFB&x-expires=2086235454&x-signature=F%2B11iuE4gyzLtI%2BIRgWao6c8W0g%3D" alt="Official Seedance 2.0 video poster: pianist in a black suit" width="100%"></a><br><sub>公式動画のサムネイル</sub><br><b>Seedance 2.0</b> · ByteDance Seed<br>ピアノ演奏：ミディアムショットから表情のアップへ。<br><a href="https://seed.bytedance.com/en/seedance2_0"><kbd>▶ 公式作例</kbd></a> · <a href="https://seed.bytedance.com/en/seedance2_0">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#seedance-piano">手順ノート（英語） →</a> · <a href="https://musicmaker.im/model/seedance-2-0/"><kbd>MusicMaker ↗</kbd></a></td>
</tr>
</table>

<!-- OFFICIAL:END -->

<a id="x-creators"></a>

## Xの作例

公開プロンプトや解説のある6本。画像から作者の元投稿へ進めます。

<table>
<tr>
<td width="50%" valign="top"><a href="https://x.com/Just_sharon7/status/2083422886686031982"><img src="https://pbs.twimg.com/amplify_video_thumb/2083422025452765184/img/ZFIIYS0hQ9OI5TpK.jpg" alt="Two dancers on a pink studio set" width="100%"></a><br><b>二人の位置を固定し、全景とアップを切り替える。</b><br><sub><a href="https://x.com/Just_sharon7/status/2083422886686031982">@Just_sharon7</a> · Seedance 2.5</sub><br><a href="https://x.com/Just_sharon7/status/2083422886686031982">元投稿 ↗</a> · <a href="docs/x-cases.md#duo">練習プラン（英語） →</a></td>
<td width="50%" valign="top"><a href="https://x.com/techhalla/status/2086915118307119269"><img src="https://pbs.twimg.com/amplify_video_thumb/2086903458251112448/img/jSPsz35xEe3ZFz47.jpg" alt="A performer lying on the ground in the opening of TechHalla’s music clip" width="100%"></a><br><b>人物画像と音声を分けて準備し、歌唱を組み立てる。</b><br><sub><a href="https://x.com/techhalla/status/2086915118307119269">@techhalla</a> · MiniMax H3 + Seedream 5 Pro</sub><br><a href="https://x.com/techhalla/status/2086915118307119269">元投稿 ↗</a> · <a href="docs/x-cases.md#h3-performance">練習プラン（英語） →</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://x.com/AIwithkhan/status/2087754389624860911"><img src="https://pbs.twimg.com/amplify_video_thumb/2087754331089166336/img/uJ0ET9rgvlWZOLj-.jpg" alt="A performer silhouetted in a backlit corridor" width="100%"></a><br><b>同じ人物の参考画像で、異なる場所の演技をつなぐ。</b><br><sub><a href="https://x.com/AIwithkhan/status/2087754389624860911">@AIwithkhan</a> · Seedance 2.5</sub><br><a href="https://x.com/AIwithkhan/status/2087754389624860911">元投稿 ↗</a> · <a href="docs/x-cases.md#y2k">練習プラン（英語） →</a></td>
<td width="50%" valign="top"><a href="https://x.com/oggii_0/status/2041392542659584302"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2041392519330840576/pu/img/gJnakn0aUsx_Pqnd.jpg" alt="White concentric rings on a black background" width="100%"></a><br><b>一つの形を連続して変える。音楽映像にも応用できるモーションデザイン。</b><br><sub><a href="https://x.com/oggii_0/status/2041392542659584302">@oggii_0</a> · Seedance 2.0</sub><br><a href="https://x.com/oggii_0/status/2041392542659584302">元投稿 ↗</a> · <a href="docs/x-cases.md#motion-design">練習プラン（英語） →</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://x.com/Strength04_X/status/2098290630179057858"><img src="https://pbs.twimg.com/amplify_video_thumb/2098289904409362432/img/-LuU_JZblovIR9HB.jpg" alt="A traveler waiting on a dim station platform" width="100%"></a><br><b>出発、変化、到着をつなぐ。原作は幻想的な短編。</b><br><sub><a href="https://x.com/Strength04_X/status/2098290630179057858">@Strength04_X</a> · Seedance 2.5</sub><br><a href="https://x.com/Strength04_X/status/2098290630179057858">元投稿 ↗</a> · <a href="docs/x-cases.md#lunar-train">練習プラン（英語） →</a></td>
<td width="50%" valign="top"><a href="https://x.com/Strength04_X/status/2090399966988550435"><img src="https://pbs.twimg.com/amplify_video_thumb/2090399674129940480/img/zvDQqERbmMVkeaIT.jpg" alt="An older performer standing on a gold-lit talent-show stage" width="100%"></a><br><b>静かな間を置き、強い拍で舞台の変化を見せる。</b><br><sub><a href="https://x.com/Strength04_X/status/2090399966988550435">@Strength04_X</a> · Seedance 2.5</sub><br><a href="https://x.com/Strength04_X/status/2090399966988550435">元投稿 ↗</a> · <a href="docs/x-cases.md#beat-drop">練習プラン（英語） →</a></td>
</tr>
</table>

<a id="listen"></a>

## MusicMakerで試聴

9曲を3列3段で比較。静かなピアノからロック、管弦楽、ダンス音楽まで、音の密度とリズムを聴き比べましょう。曲風は出典のStyle欄に基づきます。

<!-- LISTENING-GRID:START -->
<table>
<tr>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-21/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/sleeptown_windowlight.webp" alt="An illustrated girl listening beside a turntable and keyboard by a sunlit window" width="100%"></a><br><b>Sleeptown Windowlight</b><br><b>ピアノ独奏</b><br><sub>長回し</sub><br><a href="https://musicmaker.im/detail/discover-v2-21/"><kbd>▶ 試聴する</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-52/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/voltage_in_my_veins.webp" alt="An illustrated performer surrounded by bright blue and pink light trails" width="100%"></a><br><b>Voltage In My Veins</b><br><b>モダンロック</b><br><sub>強い拍で切る</sub><br><a href="https://musicmaker.im/detail/discover-v2-52/"><kbd>▶ 試聴する</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-24/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/crown_of_the_tempest.webp" alt="An orchestra and choir performing outdoors under a blue sky" width="100%"></a><br><b>Crown of the Tempest</b><br><b>壮大な管弦楽</b><br><sub>広い情景</sub><br><a href="https://musicmaker.im/detail/discover-v2-24/"><kbd>▶ 試聴する</kbd></a></td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-87/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/rain_on_beale.webp" alt="An illustrated cafe with a turquoise awning reflected on a wet street" width="100%"></a><br><b>Rain On Beale</b><br><b>ローファイ・ジャズ</b><br><sub>雨のループ</sub><br><a href="https://musicmaker.im/detail/discover-v2-87/"><kbd>▶ 試聴する</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-42/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/tidal_release.webp" alt="A woman in a white dress beside the sea beneath glowing wave-shaped lights" width="100%"></a><br><b>Tidal Release</b><br><b>プログレッシブ・ハウス</b><br><sub>高揚で転換</sub><br><a href="https://musicmaker.im/detail/discover-v2-42/"><kbd>▶ 試聴する</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-48/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/back_roads_lead_me_home.webp" alt="A man playing acoustic guitar on a porch overlooking fields" width="100%"></a><br><b>Back Roads Lead Me Home</b><br><b>カントリー・バラード</b><br><sub>暖かな物語</sub><br><a href="https://musicmaker.im/detail/discover-v2-48/"><kbd>▶ 試聴する</kbd></a></td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-22/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/midnight_garden_circuits.webp" alt="A green meadow under a pastel sky with abstract waves and cover lettering" width="100%"></a><br><b>Midnight Garden Circuits</b><br><b>アンビエント電子音楽</b><br><sub>抽象映像</sub><br><a href="https://musicmaker.im/detail/discover-v2-22/"><kbd>▶ 試聴する</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-60/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/basement_crown.webp" alt="A gold crown on a studio speaker beside a mixing desk" width="100%"></a><br><b>Basement Crown</b><br><b>ヒップホップ</b><br><sub>明確なカット</sub><br><a href="https://musicmaker.im/detail/discover-v2-60/"><kbd>▶ 試聴する</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-90/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/keep_it_open.webp" alt="A seated man and woman talking beside an open doorway facing the sea" width="100%"></a><br><b>Keep It Open</b><br><b>電子R&amp;B</b><br><sub>表情のアップ</sub><br><a href="https://musicmaker.im/detail/discover-v2-90/"><kbd>▶ 試聴する</kbd></a></td>
</tr>
</table>
<!-- LISTENING-GRID:END -->

好きな音が見つかったら、まずジャケットと短い一場面を作ってみましょう。必要な道具を制作順に選べます。 [→ 無料ツール](#toolkit) · [↗ 詳細な曲風と出典（英語）](docs/listening-notes.md)

<a id="first-video"></a>

## 最初の動画を作る

<table><tr><td width="42%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-98/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/living_on_the_brightside.webp" alt="A rainbow above a green valley with a stream and wildflowers" width="100%"></a></td><td width="58%" valign="top">Living on the Brightside のジャケットに描かれた虹、渓流、野花を参考に、16秒の自然映像を作ります。<br><br><b>1.</b> 自作または利用許諾のある曲から16秒を選びます。練習音源は Download raw file で保存。編集ソフトで0・4・8・12・16秒に印を付け、別の曲なら拍に合わせ直します。</td></tr></table>

[▶ 試聴する](https://musicmaker.im/detail/discover-v2-98/) · [↗ 公式ツール](https://hailuoai.video/tools/minimax-h3) · [↗ MusicMaker](https://musicmaker.im/free-short-music-video-generator/)

[♫ 練習音源](starter-kit/practice-beat-120bpm.wav)

2. 公式HailuoではH3のテキスト動画を選択。MusicMaker短編ツールもテキストから始められます。9:16、各5秒。ブランド側は現在480pでH3使用を明記しています。

3. Aの野花を先に確認し、Bの渓流、Cの虹の全景、Dの締めの遠景へ進みます。下の英語プロンプトを一つずつ使用。MusicMakerで画像を使う場合は自分の許諾済み開始画像・終了画像を用意します。

4. 各動画の安定した4秒を順に配置し、元の動画音声を消して曲を一つだけ残します。最後の2秒にタイトルを加え、音楽の終わりを短くフェードします。

5. 9:16のMP4を書き出し、黒いコマ、川の流れ、虹や地形の変形を確認。480pを拡大しても細部は増えません。変形するなら動きを減らし、同じ許諾済み場面画像で再生成します。

**コピー用の英語プロンプト**

```text
A: A green valley after rain, soft afternoon sunlight.
Close-up of purple wildflowers with water droplets beside a shallow stream.
Locked camera; a light breeze moves only the flower stems. Soft grassy background.
Natural photographic realism. No people, buildings or text; keep flower count stable.
```

```text
B: The same green valley after rain in soft afternoon sunlight.
Medium view of a shallow stream flowing between grassy slopes toward the foreground.
Locked camera; water moves slowly over stones, purple flowers sway subtly.
Keep the riverbanks stable. No people, buildings or text.
```

```text
C: Wide view of a green valley after rain in soft afternoon sunlight.
One rainbow spans the distant sky; a shallow stream and purple flowers fill the foreground.
Locked wide camera; grass moves subtly and clouds drift slowly.
Keep the rainbow stationary. No extra rainbows, people, buildings, text or fast camera moves.
```

```text
D: A distant view of the same green valley after rain, soft afternoon sunlight.
A shallow stream leads toward one rainbow. Locked camera; only water and grass move subtly.
Leave clean grass in the lower frame for a title added later.
Keep terrain and rainbow stable. No people, buildings or generated text.
```

光と地形をそろえ、映像と音楽を同時に終えます。

[→ 詳しい手順（英語）](docs/first-video.md#3-assemble-in-an-editor)

<a id="next-project"></a>

## 次の技術を学ぶ

<table><tr><td width="42%" valign="top"><a href="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_video.mp4"><img src="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_cover.webp" alt="Input portrait: smiling singer at a gold microphone under pink stage lights" width="100%"></a></td><td width="58%" valign="top">次は約10秒の歌唱アップ。画像はMusicMaker公開例の入力用人物画像です。クリックで動画が開きます。<br><br><b>1.</b> 口を遮らない正面寄りの許諾済み人物写真と、自分の歌声または許諾済み歌声を用意。約10秒の一節を前後に呼吸の余白を残して切り出します。器楽の練習音源は歌声の代わりになりません。</td></tr></table>

[▶ ブランドの動画を見る](https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_video.mp4) · [↗ 公式ツール](https://hailuoai.video/tools/minimax-h3) · [↗ MusicMaker](https://musicmaker.im/ai-music-video-generator/)

2. 公式H3ではOmni ReferenceのRefsに人物画像と歌声を一緒に追加し、約10秒と画像に合う比率を選びます。音声参照には画像または動画の併用が必要です。

3. MusicMakerではMusic Fileに歌声、Character Imageに人物写真、Promptに下の指示を入力。音声範囲、予想消費、Publicの公開設定を確認してGenerateを押します。

4. 最初は固定アップのみ。冒頭・中間・末尾の口と声を確認。一定のずれなら編集で調整し、ずれが広がるなら短い一節で再生成。顔が変わる場合はうなずきも減らします。

5. 原音を使うなら生成音を消し、生成音を使うなら重複音声を削除。最後に曲名を加えてMP4を書き出し、一節と呼吸が切れずに終わるか確認してから、次回だけ緩い寄りを試します。

**コピー用の英語プロンプト**

```text
Use my uploaded portrait as the only character reference and my uploaded vocal as the timing guide.
Keep the same adult singer, face, hairstyle, clothes and lighting as in the supplied portrait.
Locked shoulder-up close-up. Keep the microphone below and beside the lips, never covering them.
Hands stay outside the frame. Perform the supplied phrase with natural matching mouth movements,
subtle breathing, blinking and a slight nod. Hold the pose through sustained notes.
Relax naturally after the phrase. Do not add dialogue or change lyrics.
No costume change, turning around, cuts, additional people, text or exaggerated expressions.
```

同じ人物、見える口、一つの音声、自然な句末を確認。

[→ 詳しい手順（英語）](docs/first-video.md#vocal)

<a id="toolkit"></a>

## 無料から始める制作ツール集

最初の4行は各ページで無料と案内されるツール、5行目は参考素材です。利用枠・ログイン・待ち時間は現在のページで確認してください。 楽曲生成や人物歌唱は利用枠・料金を別途確認してください。公開素材の閲覧は再利用許諾ではありません。

<table>
<tr><td width="35%"><b>🖼 ジャケット・絵コンテを作る</b></td><td><a href="https://musicmaker.im/free-chatgpt-images-2-5/"><kbd>↗ Free image generator</kbd></a></td></tr>
<tr><td width="35%"><b>🎬 短い映像に動かす</b></td><td><a href="https://musicmaker.im/free-short-music-video-generator/"><kbd>↗ 5s short video</kbd></a> · <a href="https://musicmaker.im/free-text-to-video/"><kbd>↗ Text to video</kbd></a></td></tr>
<tr><td width="35%"><b>🎧 音の質感を変える</b></td><td><a href="https://musicmaker.im/lofi-song-maker/"><kbd>↗ Lo-fi song maker</kbd></a></td></tr>
<tr><td width="35%"><b>📦 形式と曲情報を整える</b></td><td><a href="https://musicmaker.im/audio-converter/mp3-to-wav/"><kbd>↗ MP3 → WAV</kbd></a> · <a href="https://musicmaker.im/mp3-tag-editor-online/"><kbd>↗ MP3 tag editor</kbd></a></td></tr>
<tr><td width="35%"><b>📚 素材・プロンプトを探す</b></td><td><a href="https://musicmaker.im/discover/"><kbd>↗ Discover</kbd></a> · <a href="https://musicmaker.im/ai-music-video-generator/"><kbd>↗ Video examples</kbd></a> · <a href="prompts/README.md"><kbd>↗ 12 prompts</kbd></a></td></tr>
</table>

[→ 全素材・ツール一覧（英語）](docs/brand-resources.md)

## モデルの選び方：公式資料と MusicMaker

<!-- CAPABILITIES:START -->
<table>
<tr><td width="650"><b>Seedance 2.5</b><br>本ガイドの練習提案: テキスト・画像 → 複数ショットの設計。MusicMaker で開発元の全参照機能が使えるとは限りません。</td><td width="350"><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#seedance-concert">手順ノート（英語） →</a><br><a href="https://musicmaker.im/model/seedance-2-5/"><kbd>MusicMaker · Seedance 2.5 ↗</kbd></a></td></tr>
<tr><td width="650"><b>MiniMax H3</b><br>本ガイドの練習提案: テキスト・画像の短編と歌声参照は別の経路です。MusicMaker の無料短編入口は5秒・480p。歌唱音声はテキスト欄に入れられません。</td><td width="350"><a href="https://hailuoai.video/tools/minimax-h3">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#h3-singing">手順ノート（英語） →</a><br><a href="https://musicmaker.im/model/minimax-h3/"><kbd>MusicMaker · MiniMax H3 ↗</kbd></a></td></tr>
<tr><td width="650"><b>Veo 3.1</b><br>本ガイドの練習提案: テキスト・開始フレーム → 場面の短編。Fast と通常版を先に確認し、MusicMaker に複数画像参照があると想定しないでください。</td><td width="350"><a href="https://deepmind.google/models/veo/prompt-guide/">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#veo-scene">手順ノート（英語） →</a><br><a href="https://musicmaker.im/model/veo-3-1-ai/"><kbd>MusicMaker · Veo 3.1 ↗</kbd></a></td></tr>
<tr><td width="650"><b>Seedance 2.0</b><br>本ガイドの練習提案: テキスト・画像 → 一人の演奏ショット。手や楽器の連続性を確認してください。音符ごとの正確な再現は保証されません。</td><td width="350"><a href="https://seed.bytedance.com/en/seedance2_0">公式ガイド・プロンプト ↗</a><br><a href="docs/official-cases.md#seedance-piano">手順ノート（英語） →</a><br><a href="https://musicmaker.im/model/seedance-2-0/"><kbd>MusicMaker · Seedance 2.0 ↗</kbd></a></td></tr>
</table>
<!-- CAPABILITIES:END -->

- **[MiniMax Music 3.0](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model)** — 曲の構想と必要に応じた歌詞から制作。先に音楽の構成を決めます。 [MusicMaker ↗](https://musicmaker.im/minimax/minimax-music-v3-0/)
- **[Eleven Music](https://elevenlabs.io/docs/overview/capabilities/music/best-practices)** — ジャンル、雰囲気、楽器、テンポを具体的に伝えます。 [MusicMaker ↗](https://musicmaker.im/eleven-labs/eleven-labs-music/)

[→ 素材の出典と利用条件](assets/README.md) · [MIT](LICENSE)

AI Music Maker が管理。独自の文章・コード・練習音源はMIT。外部の音楽、画像、映像は各権利者に帰属します。

<!-- AFFILIATE:START -->
**アフィリエイト提携**

MusicMaker はアフィリエイト提携を受け付けています。チュートリアル、レビュー、コミュニティで音楽制作ツールを紹介し、プログラムの規定に沿って対象の紹介購入から報酬を得られます。

<a href="https://musicmaker.im/affiliate-program/"><kbd>↗ 提携プログラムの詳細・申請</kbd></a>
<!-- AFFILIATE:END -->

<!-- TRUST:START -->
<details>
<summary>編集・管理方針</summary>

MusicMaker チームが管理し、ブランドで利用できるモデルを優先的に紹介しています。紹介リンクに本リポジトリのアフィリエイト用パラメータは付けていませんが、商業的な利害がないという意味ではありません。 [ 編集・管理方針 (English) → ](docs/editorial-policy.md)

独自の16秒編集デモは制作済みです。外部事例は公開情報とアクセス可否のみを確認し、2つの AI 生成チュートリアルは全工程を実測していません。

公式公開例であり、本庫の生成テストや順位付けではありません。

4つのモデル版にはMusicMakerの対応ページがあります。作例とガイドは開発元の資料です。MusicMakerの機能は実際の画面で確認してください。H3画像は入力素材です。

ホームの表紙は独自のコンセプトイラストです。Discover の画像は曲のジャケット、歌唱チュートリアルの人物画像はブランドのデモに使われた入力画像です。いずれも本庫が生成した動画の実績を示すものではありません。

X のモデル名は作者の説明に基づきます。公開ミラーで投稿本文と添付メディアを確認しましたが、動画は再現していません。制作時のプロンプトは作者の元投稿を参照してください。[出典メモ（英語）](docs/x-cases.md#source-notes)。

試聴欄の映像案は本庫の提案です。自然映像と人物歌唱のチュートリアルは新規の練習であり、元作品の制作記録ではありません。MusicMaker は公開歌唱デモのモデルを明かしていません。両方のプロンプトは全工程を実測しておらず、ジャケットの再現、元の音声の保持、正確な口の同期を保証しません。

公開試聴・視聴は再利用の許可を意味しません。外部の音楽・画像・動画を使うには、適切な許可が必要です。

[▶ 独自の編集デモを見る](starter-kit/night-train-edit-demo.mp4) · [根拠と検証状況 (EN / 简体中文)](docs/generation-tests.md) · [訂正を報告](https://github.com/aimusicmaker/awesome-music-video-creator-guide/issues/new/choose)

</details>
<!-- TRUST:END -->

<!-- TRANSLATION:START -->
文章と翻訳には AI を使用しています。独立した母語話者による校閲記録はありません。詳細資料は英語と簡体字中国語です。 [🌐 言語とレビュー状況 (English)](i18n/README.md)
<!-- TRANSLATION:END -->
