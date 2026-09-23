<h1 align="center">뮤직비디오 제작 가이드</h1>

<!-- BRAND:START -->
<p align="center"><a href="https://musicmaker.im/"><img src="https://musicmaker.im/images/logo.svg" alt="MusicMaker logo" width="88" height="88"></a></p>
<!-- BRAND:END -->

<!-- LANGUAGES:START -->
<p align="center">🌐 <a href="README.md"><kbd>English</kbd></a> · <a href="README_JA.md"><kbd>日本語</kbd></a> · <a href="README_ID.md"><kbd>Bahasa Indonesia</kbd></a> · <a href="README_IT.md"><kbd>Italiano</kbd></a> · <a href="README_PT.md"><kbd>Português</kbd></a> · <a href="README_ES.md"><kbd>Español</kbd></a> · <a href="README_DE.md"><kbd>Deutsch</kbd></a> · <a href="README_RU.md"><kbd>Русский</kbd></a> · <a href="README_FR.md"><kbd>Français</kbd></a> · <a href="README_ZH.md"><kbd>简体中文</kbd></a> · <a href="README_TW.md"><kbd>繁體中文</kbd></a> · <b>한국어</b> · <a href="README_TH.md"><kbd>ไทย</kbd></a> · <a href="README_VI.md"><kbd>Tiếng Việt</kbd></a> · <a href="README_AR.md"><kbd>العربية</kbd></a></p>
<!-- LANGUAGES:END -->

<!-- DEVICE:START -->
<p align="center"><a href="mobile/README_KO.md"><kbd>📱 모바일 버전</kbd></a></p>
<!-- DEVICE:END -->

<p align="center"><strong>한 곡에 끝까지 보고 싶은 영상을 더하세요. 작품을 보고 제작 방법을 배운 뒤, 나만의 짧은 영상을 완성해 보세요.</strong></p>

<p align="center"><a href="#official-models"><kbd>✦ 모델 공식 사례와 튜토리얼</kbd></a> &nbsp; <a href="#x-creators"><kbd>▶ X 제작 사례</kbd></a> &nbsp; <a href="#listen"><kbd>♫ MusicMaker 미리 듣기</kbd></a> &nbsp; <a href="#first-video"><kbd>✦ 첫 영상 만들기</kbd></a> &nbsp; <a href="#next-project"><kbd>→ 다음 연습</kbd></a> &nbsp; <a href="#toolkit"><kbd>🧰 무료 도구</kbd></a></p>

[![음악 선택 → 장면과 프롬프트 설계 → 영상 생성 → 편집과 내보내기. 노래, 여행, 추상 영상으로 이어지는 과정을 그린 창작 안내도입니다.](assets/social-preview.jpg)](#first-video)

음악 선택 → 장면과 프롬프트 설계 → 영상 생성 → 편집과 내보내기. 노래, 여행, 추상 영상으로 이어지는 과정을 그린 창작 안내도입니다.

<!-- OFFICIAL:START -->
<a id="official-models"></a>

## 모델 공식 사례와 튜토리얼

개발사의 사례와 입력 방법을 먼저 보고 커뮤니티 활용법으로 이어집니다.

<table>
<tr>
<td width="50%" valign="top"><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5"><img src="assets/official/seedance-concert.jpg" alt="Frame from the official Seedance 2.5 concert demonstration" width="100%"></a><br><sub>공식 데모 장면</sub><br><b>Seedance 2.5</b> · ByteDance Seed<br>음악회: 장소와 연주자 참조를 나눕니다.<br><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5"><kbd>▶ 공식 사례</kbd></a> · <a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#seedance-concert">단계별 노트 · 영어 →</a> · <a href="https://musicmaker.im/model/seedance-2-5/"><kbd>MusicMaker ↗</kbd></a></td>
<td width="50%" valign="top"><a href="https://www.minimax.io/blog/minimax-h3"><img src="https://filecdn.minimax.chat/public/h3-en-v2-image-000-1785473644038.png" alt="Official MiniMax H3 character reference image for the singing demonstration" width="100%"></a><br><sub>공식 입력 이미지</sub><br><b>MiniMax H3</b> · MiniMax<br>노래: 카메라·인물·보컬 참조를 나눕니다.<br><a href="https://www.minimax.io/blog/minimax-h3"><kbd>▶ 공식 사례</kbd></a> · <a href="https://hailuoai.video/tools/minimax-h3">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#h3-singing">단계별 노트 · 영어 →</a> · <a href="https://musicmaker.im/model/minimax-h3/"><kbd>MusicMaker ↗</kbd></a></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://deepmind.google/models/veo/"><img src="https://lh3.googleusercontent.com/B3TEWPmHGddbqymciVXc6yVwXbmxZtTBG5PZrUHNZbgISHlOLJokWGoDR0Dqfug4QPIzNUgP9T23Iktd11yMvzfYLqURXmvCDGLr1RIliT9VeZs82g=w1440-h810-n-nu" alt="Official Veo comparison: three reference images beside a singer in an abstract flower garden" width="100%"></a><br><sub>공식 입력·출력 비교</sub><br><b>Veo 3.1</b> · Google DeepMind<br>환상적인 노래 장면: 인물과 배경 참조를 조합합니다.<br><a href="https://deepmind.google/models/veo/"><kbd>▶ 공식 사례</kbd></a> · <a href="https://deepmind.google/models/veo/prompt-guide/">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#veo-scene">단계별 노트 · 영어 →</a> · <a href="https://musicmaker.im/model/veo-3-1-ai/"><kbd>MusicMaker ↗</kbd></a></td>
<td width="50%" valign="top"><a href="https://seed.bytedance.com/en/seedance2_0"><img src="https://p11-sign.douyinpic.com/tos-cn-p-13c08f/6867a9183a794734882c56d613a4fba5_1770872187~tplv-noop.image?dy_q=1770875442&l=20260212134538DCD5D5DD0148D91D5FFB&x-expires=2086235454&x-signature=F%2B11iuE4gyzLtI%2BIRgWao6c8W0g%3D" alt="Official Seedance 2.0 video poster: pianist in a black suit" width="100%"></a><br><sub>공식 동영상 표지</sub><br><b>Seedance 2.0</b> · ByteDance Seed<br>피아노 연주: 미디엄 샷에서 표정 클로즈업으로.<br><a href="https://seed.bytedance.com/en/seedance2_0"><kbd>▶ 공식 사례</kbd></a> · <a href="https://seed.bytedance.com/en/seedance2_0">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#seedance-piano">단계별 노트 · 영어 →</a> · <a href="https://musicmaker.im/model/seedance-2-0/"><kbd>MusicMaker ↗</kbd></a></td>
</tr>
</table>

<!-- OFFICIAL:END -->

<a id="x-creators"></a>

## X 제작 사례

공개 프롬프트나 제작 설명이 있는 영상 6개입니다. 이미지를 누르면 제작자의 원문 게시물로 이동합니다.

<table>
<tr>
<td width="50%" valign="top"><a href="https://x.com/Just_sharon7/status/2083422886686031982"><img src="https://pbs.twimg.com/amplify_video_thumb/2083422025452765184/img/ZFIIYS0hQ9OI5TpK.jpg" alt="Two dancers on a pink studio set" width="100%"></a><br><b>두 사람의 위치를 고정하고 전체 화면과 클로즈업을 번갈아 사용합니다.</b><br><sub><a href="https://x.com/Just_sharon7/status/2083422886686031982">@Just_sharon7</a> · Seedance 2.5</sub><br><a href="https://x.com/Just_sharon7/status/2083422886686031982">원문 ↗</a> · <a href="docs/x-cases.md#duo">연습 기획안·영어 →</a></td>
<td width="50%" valign="top"><a href="https://x.com/techhalla/status/2086915118307119269"><img src="https://pbs.twimg.com/amplify_video_thumb/2086903458251112448/img/jSPsz35xEe3ZFz47.jpg" alt="A performer lying on the ground in the opening of TechHalla’s music clip" width="100%"></a><br><b>인물 이미지와 음성을 따로 준비해 노래 장면을 구성합니다.</b><br><sub><a href="https://x.com/techhalla/status/2086915118307119269">@techhalla</a> · MiniMax H3 + Seedream 5 Pro</sub><br><a href="https://x.com/techhalla/status/2086915118307119269">원문 ↗</a> · <a href="docs/x-cases.md#h3-performance">연습 기획안·영어 →</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://x.com/AIwithkhan/status/2087754389624860911"><img src="https://pbs.twimg.com/amplify_video_thumb/2087754331089166336/img/uJ0ET9rgvlWZOLj-.jpg" alt="A performer silhouetted in a backlit corridor" width="100%"></a><br><b>동일한 인물 참고 이미지로 여러 장소의 연기를 연결합니다.</b><br><sub><a href="https://x.com/AIwithkhan/status/2087754389624860911">@AIwithkhan</a> · Seedance 2.5</sub><br><a href="https://x.com/AIwithkhan/status/2087754389624860911">원문 ↗</a> · <a href="docs/x-cases.md#y2k">연습 기획안·영어 →</a></td>
<td width="50%" valign="top"><a href="https://x.com/oggii_0/status/2041392542659584302"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2041392519330840576/pu/img/gJnakn0aUsx_Pqnd.jpg" alt="White concentric rings on a black background" width="100%"></a><br><b>하나의 형태를 연속해서 바꾸는 모션 디자인입니다. 음악 시각화에 응용할 수 있습니다.</b><br><sub><a href="https://x.com/oggii_0/status/2041392542659584302">@oggii_0</a> · Seedance 2.0</sub><br><a href="https://x.com/oggii_0/status/2041392542659584302">원문 ↗</a> · <a href="docs/x-cases.md#motion-design">연습 기획안·영어 →</a></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://x.com/Strength04_X/status/2098290630179057858"><img src="https://pbs.twimg.com/amplify_video_thumb/2098289904409362432/img/-LuU_JZblovIR9HB.jpg" alt="A traveler waiting on a dim station platform" width="100%"></a><br><b>출발, 변화, 도착을 연결합니다. 원작은 판타지 단편입니다.</b><br><sub><a href="https://x.com/Strength04_X/status/2098290630179057858">@Strength04_X</a> · Seedance 2.5</sub><br><a href="https://x.com/Strength04_X/status/2098290630179057858">원문 ↗</a> · <a href="docs/x-cases.md#lunar-train">연습 기획안·영어 →</a></td>
<td width="50%" valign="top"><a href="https://x.com/Strength04_X/status/2090399966988550435"><img src="https://pbs.twimg.com/amplify_video_thumb/2090399674129940480/img/zvDQqERbmMVkeaIT.jpg" alt="An older performer standing on a gold-lit talent-show stage" width="100%"></a><br><b>잠깐의 정적 뒤 강한 박자에 맞춰 무대의 변화를 보여 줍니다.</b><br><sub><a href="https://x.com/Strength04_X/status/2090399966988550435">@Strength04_X</a> · Seedance 2.5</sub><br><a href="https://x.com/Strength04_X/status/2090399966988550435">원문 ↗</a> · <a href="docs/x-cases.md#beat-drop">연습 기획안·영어 →</a></td>
</tr>
</table>

<a id="listen"></a>

## MusicMaker 미리 듣기

아홉 곡을 3열 3행으로 비교합니다. 피아노부터 록, 관현악, 댄스 음악까지 소리의 밀도와 리듬을 들어보세요. 장르는 원문의 Style 항목을 따릅니다.

<!-- LISTENING-GRID:START -->
<table>
<tr>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-21/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/sleeptown_windowlight.webp" alt="An illustrated girl listening beside a turntable and keyboard by a sunlit window" width="100%"></a><br><b>Sleeptown Windowlight</b><br><b>피아노 연주</b><br><sub>긴 호흡의 장면</sub><br><a href="https://musicmaker.im/detail/discover-v2-21/"><kbd>▶ 곡 듣기</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-52/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/voltage_in_my_veins.webp" alt="An illustrated performer surrounded by bright blue and pink light trails" width="100%"></a><br><b>Voltage In My Veins</b><br><b>모던 록</b><br><sub>강한 박자에 컷</sub><br><a href="https://musicmaker.im/detail/discover-v2-52/"><kbd>▶ 곡 듣기</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-24/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/crown_of_the_tempest.webp" alt="An orchestra and choir performing outdoors under a blue sky" width="100%"></a><br><b>Crown of the Tempest</b><br><b>웅장한 관현악</b><br><sub>넓은 풍경</sub><br><a href="https://musicmaker.im/detail/discover-v2-24/"><kbd>▶ 곡 듣기</kbd></a></td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-87/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/rain_on_beale.webp" alt="An illustrated cafe with a turquoise awning reflected on a wet street" width="100%"></a><br><b>Rain On Beale</b><br><b>로파이 재즈</b><br><sub>빗속 반복 영상</sub><br><a href="https://musicmaker.im/detail/discover-v2-87/"><kbd>▶ 곡 듣기</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-42/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/tidal_release.webp" alt="A woman in a white dress beside the sea beneath glowing wave-shaped lights" width="100%"></a><br><b>Tidal Release</b><br><b>프로그레시브 하우스</b><br><sub>고조되는 전환</sub><br><a href="https://musicmaker.im/detail/discover-v2-42/"><kbd>▶ 곡 듣기</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-48/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/back_roads_lead_me_home.webp" alt="A man playing acoustic guitar on a porch overlooking fields" width="100%"></a><br><b>Back Roads Lead Me Home</b><br><b>컨트리 발라드</b><br><sub>따뜻한 이야기</sub><br><a href="https://musicmaker.im/detail/discover-v2-48/"><kbd>▶ 곡 듣기</kbd></a></td>
</tr>
<tr>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-22/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/midnight_garden_circuits.webp" alt="A green meadow under a pastel sky with abstract waves and cover lettering" width="100%"></a><br><b>Midnight Garden Circuits</b><br><b>앰비언트 전자음악</b><br><sub>추상 화면</sub><br><a href="https://musicmaker.im/detail/discover-v2-22/"><kbd>▶ 곡 듣기</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-60/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/basement_crown.webp" alt="A gold crown on a studio speaker beside a mixing desk" width="100%"></a><br><b>Basement Crown</b><br><b>힙합</b><br><sub>또렷한 컷</sub><br><a href="https://musicmaker.im/detail/discover-v2-60/"><kbd>▶ 곡 듣기</kbd></a></td>
<td width="33%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-90/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/keep_it_open.webp" alt="A seated man and woman talking beside an open doorway facing the sea" width="100%"></a><br><b>Keep It Open</b><br><b>일렉트로닉 R&amp;B</b><br><sub>감정 클로즈업</sub><br><a href="https://musicmaker.im/detail/discover-v2-90/"><kbd>▶ 곡 듣기</kbd></a></td>
</tr>
</table>
<!-- LISTENING-GRID:END -->

마음에 드는 소리를 찾았다면 커버와 짧은 장면부터 만들어 보세요. 제작 순서에 따라 도구를 고를 수 있습니다. [→ 무료 도구](#toolkit) · [↗ 곡풍과 출처 · 영어](docs/listening-notes.md)

<a id="first-video"></a>

## 첫 영상 만들기

<table><tr><td width="42%" valign="top"><a href="https://musicmaker.im/detail/discover-v2-98/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/living_on_the_brightside.webp" alt="A rainbow above a green valley with a stream and wildflowers" width="100%"></a></td><td width="58%" valign="top">Living on the Brightside의 커버에 담긴 무지개, 개울, 들꽃에서 출발해 16초 자연 영상을 만듭니다.<br><br><b>1.</b> 직접 만든 곡이나 허가받은 곡에서 16초를 고릅니다. 연습 음원은 Download raw file로 저장합니다. 편집기에 0·4·8·12·16초를 표시하고 다른 곡을 쓰면 박자에 맞춰 조정합니다.</td></tr></table>

[▶ 곡 듣기](https://musicmaker.im/detail/discover-v2-98/) · [↗ 공식 도구](https://hailuoai.video/tools/minimax-h3) · [↗ MusicMaker](https://musicmaker.im/free-short-music-video-generator/)

[♫ 연습 음원](starter-kit/practice-beat-120bpm.wav)

2. 공식 Hailuo에서 H3 텍스트 영상 모드를 선택하거나 MusicMaker 짧은 영상 도구를 사용합니다. 9:16, 각 5초로 만들며 브랜드 페이지는 현재 480p와 H3 사용을 명시합니다.

3. 먼저 A의 들꽃을 확인하고 B 개울, C 무지개 전경, D 마무리 전경을 만듭니다. 영어 프롬프트를 하나씩 복사하세요. MusicMaker 이미지 경로는 사용 권한이 있는 시작·끝 이미지가 필요합니다.

4. 각 영상에서 안정적인 4초를 골라 이어 붙입니다. 생성 영상 소리를 끄고 음악 한 트랙만 남깁니다. 마지막 2초에 제목을 넣고 음악 끝을 짧게 페이드합니다.

5. 9:16 MP4를 내보내 검은 프레임, 물 흐름, 무지개와 지형 변형을 확인합니다. 480p 확대는 디테일을 늘리지 않습니다. 변형되면 움직임을 줄이고 동일한 허가된 장면 이미지를 참조해 다시 만듭니다.

**복사할 영어 프롬프트**

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

빛과 지형을 유지하고 음악과 영상을 함께 끝냅니다.

[→ 상세 단계·영어](docs/first-video.md#3-assemble-in-an-editor)

<a id="next-project"></a>

## 다음 기술 익히기

<table><tr><td width="42%" valign="top"><a href="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_video.mp4"><img src="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_cover.webp" alt="Input portrait: smiling singer at a gold microphone under pink stage lights" width="100%"></a></td><td width="58%" valign="top">이번에는 약 10초의 인물 노래 클로즈업입니다. 사진은 MusicMaker 공개 영상의 입력 인물 이미지이며 누르면 영상을 봅니다.<br><br><b>1.</b> 입이 가려지지 않는 정면에 가까운 허가된 인물 사진과 직접 녹음하거나 허가받은 노래를 준비합니다. 약 10초의 한 구절에 앞뒤 숨 쉴 여백을 남기세요. 연습용 반주는 보컬 입력을 대신하지 못합니다.</td></tr></table>

[▶ 브랜드 영상 보기](https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_video.mp4) · [↗ 공식 도구](https://hailuoai.video/tools/minimax-h3) · [↗ MusicMaker](https://musicmaker.im/ai-music-video-generator/)

2. 공식 H3 Omni Reference의 Refs에 인물과 노래를 함께 넣고 약 10초와 사진에 맞는 비율을 선택합니다. 오디오 참조는 이미지나 영상과 함께 사용해야 합니다.

3. MusicMaker의 Music File에는 노래, Character Image에는 인물, Prompt에는 아래 지시문을 넣습니다. 오디오 구간, 예상 사용량, Public 설정을 확인하고 Generate를 누릅니다.

4. 고정 클로즈업부터 시작합니다. 시작·중간·끝의 입과 소리를 비교하세요. 일정한 지연은 편집으로 맞추고 점점 어긋나면 더 짧은 구절로 재생성합니다. 얼굴이 바뀌면 고개 움직임도 줄입니다.

5. 원음을 쓰면 생성 소리를 끄고 생성 소리를 쓰면 중복 트랙을 지웁니다. 끝에 곡명을 넣고 MP4를 내보내 구절과 호흡이 잘리지 않는지 확인한 뒤 다음 시도에서만 천천히 다가가는 카메라를 추가합니다.

**복사할 영어 프롬프트**

```text
Use my uploaded portrait as the only character reference and my uploaded vocal as the timing guide.
Keep the same adult singer, face, hairstyle, clothes and lighting as in the supplied portrait.
Locked shoulder-up close-up. Keep the microphone below and beside the lips, never covering them.
Hands stay outside the frame. Perform the supplied phrase with natural matching mouth movements,
subtle breathing, blinking and a slight nod. Hold the pose through sustained notes.
Relax naturally after the phrase. Do not add dialogue or change lyrics.
No costume change, turning around, cuts, additional people, text or exaggerated expressions.
```

같은 인물, 보이는 입, 하나의 음성, 자연스러운 끝을 확인합니다.

[→ 상세 단계·영어](docs/first-video.md#vocal)

<a id="toolkit"></a>

## 무료로 시작하는 제작 도구 모음

첫 네 줄은 각 페이지가 무료로 안내하는 도구이며, 다섯째 줄은 참고 자료입니다. 사용량, 로그인, 대기 조건은 현재 페이지에서 확인하세요. 곡 생성과 인물 노래는 별도 사용량·요금을 확인하세요. 공개 자료 열람은 재사용 허가가 아닙니다.

<table>
<tr><td width="35%"><b>🖼 커버와 장면 설계</b></td><td><a href="https://musicmaker.im/free-chatgpt-images-2-5/"><kbd>↗ Free image generator</kbd></a></td></tr>
<tr><td width="35%"><b>🎬 짧은 영상 만들기</b></td><td><a href="https://musicmaker.im/free-short-music-video-generator/"><kbd>↗ 5s short video</kbd></a> · <a href="https://musicmaker.im/free-text-to-video/"><kbd>↗ Text to video</kbd></a></td></tr>
<tr><td width="35%"><b>🎧 소리 질감 바꾸기</b></td><td><a href="https://musicmaker.im/lofi-song-maker/"><kbd>↗ Lo-fi song maker</kbd></a></td></tr>
<tr><td width="35%"><b>📦 형식과 곡 정보 정리</b></td><td><a href="https://musicmaker.im/audio-converter/mp3-to-wav/"><kbd>↗ MP3 → WAV</kbd></a> · <a href="https://musicmaker.im/mp3-tag-editor-online/"><kbd>↗ MP3 tag editor</kbd></a></td></tr>
<tr><td width="35%"><b>📚 자료와 프롬프트 찾기</b></td><td><a href="https://musicmaker.im/discover/"><kbd>↗ Discover</kbd></a> · <a href="https://musicmaker.im/ai-music-video-generator/"><kbd>↗ Video examples</kbd></a> · <a href="prompts/README.md"><kbd>↗ 12 prompts</kbd></a></td></tr>
</table>

[→ 전체 자료·도구 목록 · 영어](docs/brand-resources.md)

## 모델 선택: 공식 자료와 MusicMaker

<!-- CAPABILITIES:START -->
<table>
<tr><td width="650"><b>Seedance 2.5</b><br>이 가이드의 연습 제안: 텍스트·이미지 → 여러 샷 구성. MusicMaker에서 개발사의 모든 참조 기능을 제공한다고 보장하지 않습니다.</td><td width="350"><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#seedance-concert">단계별 노트 · 영어 →</a><br><a href="https://musicmaker.im/model/seedance-2-5/"><kbd>MusicMaker · Seedance 2.5 ↗</kbd></a></td></tr>
<tr><td width="650"><b>MiniMax H3</b><br>이 가이드의 연습 제안: 텍스트·이미지 단편과 보컬 참조 생성은 별도 경로입니다. MusicMaker: 무료 입구는 5초·480p이며, 노래 음원을 텍스트 칸에 넣을 수 없습니다.</td><td width="350"><a href="https://hailuoai.video/tools/minimax-h3">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#h3-singing">단계별 노트 · 영어 →</a><br><a href="https://musicmaker.im/model/minimax-h3/"><kbd>MusicMaker · MiniMax H3 ↗</kbd></a></td></tr>
<tr><td width="650"><b>Veo 3.1</b><br>이 가이드의 연습 제안: 텍스트·첫 프레임 → 장면 단편. Fast와 일반 버전을 먼저 확인하세요. MusicMaker에 다중 이미지 참조 기능이 있다고 가정하지 마세요.</td><td width="350"><a href="https://deepmind.google/models/veo/prompt-guide/">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#veo-scene">단계별 노트 · 영어 →</a><br><a href="https://musicmaker.im/model/veo-3-1-ai/"><kbd>MusicMaker · Veo 3.1 ↗</kbd></a></td></tr>
<tr><td width="650"><b>Seedance 2.0</b><br>이 가이드의 연습 제안: 텍스트·이미지 → 1인 연주 샷. 손과 악기의 연속성을 확인하세요. 음표 하나하나의 재현은 보장하지 않습니다.</td><td width="350"><a href="https://seed.bytedance.com/en/seedance2_0">공식 안내·프롬프트 ↗</a><br><a href="docs/official-cases.md#seedance-piano">단계별 노트 · 영어 →</a><br><a href="https://musicmaker.im/model/seedance-2-0/"><kbd>MusicMaker · Seedance 2.0 ↗</kbd></a></td></tr>
</table>
<!-- CAPABILITIES:END -->

- **[MiniMax Music 3.0](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model)** — 구상과 선택적 가사로 곡을 만듭니다. 음악 구성을 먼저 정하세요. [MusicMaker ↗](https://musicmaker.im/minimax/minimax-music-v3-0/)
- **[Eleven Music](https://elevenlabs.io/docs/overview/capabilities/music/best-practices)** — 장르, 분위기, 악기, 빠르기를 구체적으로 설명하세요. [MusicMaker ↗](https://musicmaker.im/eleven-labs/eleven-labs-music/)

[→ 출처와 사용 조건](assets/README.md) · [MIT](LICENSE)

AI Music Maker가 관리합니다. 자체 글·코드·연습 음원은 MIT 라이선스이며 외부 음악·이미지·영상의 권리는 각 소유자에게 있습니다.

<!-- AFFILIATE:START -->
**제휴 마케팅 협력**

MusicMaker는 제휴 마케팅 협력을 지원합니다. 튜토리얼, 리뷰 또는 커뮤니티에서 음악 제작 도구를 소개하고, 프로그램 조건에 맞는 추천 구매에 대해 수수료를 받을 수 있습니다.

<a href="https://musicmaker.im/affiliate-program/"><kbd>↗ 제휴 프로그램 알아보고 신청하기</kbd></a>
<!-- AFFILIATE:END -->

<!-- TRUST:START -->
<details>
<summary>편집·관리 방침</summary>

MusicMaker 팀이 관리하며 브랜드에서 제공하는 모델을 우선 소개합니다. 추천 링크에 이 저장소의 제휴 매개변수는 없지만, 상업적 이해관계가 없다는 뜻은 아닙니다. [ 편집·관리 방침 (English) → ](docs/editorial-policy.md)

자체 제작한 16초 편집 예제는 완성되었습니다. 외부 사례는 공개 출처와 접근 가능 여부만 확인했으며, 두 AI 생성 튜토리얼은 전체 과정을 실측하지 않았습니다.

공식 공개 사례이며 자체 생성 테스트나 순위가 아닙니다.

네 모델 버전 모두 MusicMaker 페이지가 있습니다. 사례와 안내는 개발사 자료이며 실제 기능은 MusicMaker 화면에서 확인하세요. H3 이미지는 입력 자료입니다.

홈 표지는 자체 제작한 콘셉트 일러스트입니다. Discover 이미지는 노래 커버이며, 인물 노래 튜토리얼의 사진은 브랜드 데모에 사용한 입력 인물 이미지입니다. 이 이미지들은 저장소에서 생성한 영상 결과의 증거가 아닙니다.

X 사례의 모델 이름은 제작자의 설명을 따릅니다. 공개 미러로 게시물과 첨부 미디어를 확인했지만 영상을 재현하지 않았습니다. 제작에 사용한 프롬프트는 원본 게시물에서 확인하세요. [출처 설명 · 영어](docs/x-cases.md#source-notes).

감상 섹션의 영상 아이디어는 이 저장소의 제안입니다. 자연 영상과 인물 노래 튜토리얼은 새로 작성한 연습이며 원작 제작 기록이 아닙니다. MusicMaker는 공개 노래 데모의 모델을 밝히지 않았습니다. 두 프롬프트는 전체 과정을 실측하지 않았으며 커버 재현, 원음 유지, 정확한 입 모양 일치를 보장하지 않습니다.

공개 감상은 재사용 허가를 뜻하지 않습니다. 외부 음악·이미지·영상을 사용하려면 적절한 권한이 필요합니다.

[▶ 자체 편집 예제 보기](starter-kit/night-train-edit-demo.mp4) · [근거와 테스트 현황 (EN / 简体中文)](docs/generation-tests.md) · [오류·수정 제보](https://github.com/aimusicmaker/awesome-music-video-creator-guide/issues/new/choose)

</details>
<!-- TRUST:END -->

<!-- TRANSLATION:START -->
작성과 번역에 AI를 활용했습니다. 독립적인 원어민 감수 기록은 없습니다. 상세 문서는 영어와 중국어 간체로 제공합니다. [🌐 언어 및 검토 현황 (English)](i18n/README.md)
<!-- TRANSLATION:END -->
