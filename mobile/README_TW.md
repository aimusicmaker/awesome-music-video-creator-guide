<h1 align="center">音樂影片創作指南</h1>

<!-- BRAND:START -->
<p align="center"><a href="https://musicmaker.im/"><img src="https://musicmaker.im/images/logo.svg" alt="MusicMaker logo" width="88" height="88"></a></p>
<!-- BRAND:END -->

<!-- LANGUAGES:START -->
<p align="center">🌐 <a href="README.md"><kbd>English</kbd></a> · <a href="README_JA.md"><kbd>日本語</kbd></a> · <a href="README_ID.md"><kbd>Bahasa Indonesia</kbd></a> · <a href="README_IT.md"><kbd>Italiano</kbd></a> · <a href="README_PT.md"><kbd>Português</kbd></a> · <a href="README_ES.md"><kbd>Español</kbd></a> · <a href="README_DE.md"><kbd>Deutsch</kbd></a> · <a href="README_RU.md"><kbd>Русский</kbd></a> · <a href="README_FR.md"><kbd>Français</kbd></a> · <a href="README_ZH.md"><kbd>简体中文</kbd></a> · <b>繁體中文</b> · <a href="README_KO.md"><kbd>한국어</kbd></a> · <a href="README_TH.md"><kbd>ไทย</kbd></a> · <a href="README_VI.md"><kbd>Tiếng Việt</kbd></a> · <a href="README_AR.md"><kbd>العربية</kbd></a></p>
<!-- LANGUAGES:END -->

<!-- DEVICE:START -->
<p align="center"><b>📱 手機版</b> · <a href="../README_TW.md"><kbd>🖥 桌面版</kbd></a></p>
<!-- DEVICE:END -->

<p align="center"><strong>讓一首歌，有一個值得看完的畫面。</strong></p>

<p align="center">從新歌預告、人物演唱到迴圈視覺，即使第一次剪影片，也可以從這裡開始：選喜歡的畫面，拆解創作者的做法，再做自己的版本。</p>

<p align="center"><a href="#official-models"><kbd>✦ 模型官方案例與教學</kbd></a> &nbsp; <a href="#x-creators"><kbd>▶ X 創作者案例</kbd></a> &nbsp; <a href="#listen"><kbd>♫ MusicMaker 試聽</kbd></a> &nbsp; <a href="#first-video"><kbd>✦ 製作第一支影片</kbd></a> &nbsp; <a href="#next-project"><kbd>→ 下一種技巧</kbd></a> &nbsp; <a href="#toolkit"><kbd>🧰 免費工具庫</kbd></a></p>

[![選音樂、設計分鏡與提示詞、生成鏡頭、剪輯匯出；下方展示人物演唱、旅行敘事與抽象音樂視覺](../assets/music-video-workflow.png)](#first-video)

原創流程示意圖，展示本庫怎樣把案例、提示詞、工具與剪輯連起來；畫面是概念設計，不是生成影片實測結果。

**從哪裡開始：** [看案例找靈感](#x-creators) → [聽音樂定方向](#listen) → [做四鏡頭自然短片](#first-video) → [嘗試人像演唱](#next-project)。

<!-- OFFICIAL:START -->
<a id="official-models"></a>

## 模型官方案例與教學

先看模型開發者的示範與輸入方法，再看社群創作者如何延伸。這裡收錄官方發布案例，並非本庫實測，也不作為模型排名。

<p><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5"><img src="../assets/official/seedance-concert.jpg" alt="Frame from the official Seedance 2.5 concert demonstration" width="100%"></a><br><sub>官方示範截圖</sub><br><b>Seedance 2.5</b> · ByteDance Seed<br>音樂會：分別指定場地、主唱、樂手與合唱團參考。<br><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5"><kbd>▶ 看官方案例</kbd></a> · <a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#seedance-concert">逐步學習筆記 →</a> · <a href="https://musicmaker.im/model/seedance-2-5/"><kbd>MusicMaker ↗</kbd></a></p>

<p><a href="https://www.minimax.io/blog/minimax-h3"><img src="https://filecdn.minimax.chat/public/h3-en-v2-image-000-1785473644038.png" alt="Official MiniMax H3 character reference image for the singing demonstration" width="100%"></a><br><sub>官方輸入圖</sub><br><b>MiniMax H3</b> · MiniMax<br>人像演唱：將運鏡、人物和歌聲分配給不同參考。<br><a href="https://www.minimax.io/blog/minimax-h3"><kbd>▶ 看官方案例</kbd></a> · <a href="https://hailuoai.video/tools/minimax-h3">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#h3-singing">逐步學習筆記 →</a> · <a href="https://musicmaker.im/model/minimax-h3/"><kbd>MusicMaker ↗</kbd></a></p>

<p><a href="https://deepmind.google/models/veo/"><img src="https://lh3.googleusercontent.com/B3TEWPmHGddbqymciVXc6yVwXbmxZtTBG5PZrUHNZbgISHlOLJokWGoDR0Dqfug4QPIzNUgP9T23Iktd11yMvzfYLqURXmvCDGLr1RIliT9VeZs82g=w1440-h810-n-nu" alt="Official Veo comparison: three reference images beside a singer in an abstract flower garden" width="100%"></a><br><sub>官方輸入與輸出對照</sub><br><b>Veo 3.1</b> · Google DeepMind<br>奇幻演唱場景：用參考素材組織人物與環境。<br><a href="https://deepmind.google/models/veo/"><kbd>▶ 看官方案例</kbd></a> · <a href="https://deepmind.google/models/veo/prompt-guide/">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#veo-scene">逐步學習筆記 →</a> · <a href="https://musicmaker.im/model/veo-3-1-ai/"><kbd>MusicMaker ↗</kbd></a></p>

<p><a href="https://seed.bytedance.com/en/seedance2_0"><img src="https://p11-sign.douyinpic.com/tos-cn-p-13c08f/6867a9183a794734882c56d613a4fba5_1770872187~tplv-noop.image?dy_q=1770875442&l=20260212134538DCD5D5DD0148D91D5FFB&x-expires=2086235454&x-signature=F%2B11iuE4gyzLtI%2BIRgWao6c8W0g%3D" alt="Official Seedance 2.0 video poster: pianist in a black suit" width="100%"></a><br><sub>官方影片封面</sub><br><b>Seedance 2.0</b> · ByteDance Seed<br>鋼琴演奏：從人物中景切到表情特寫。<br><a href="https://seed.bytedance.com/en/seedance2_0"><kbd>▶ 看官方案例</kbd></a> · <a href="https://seed.bytedance.com/en/seedance2_0">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#seedance-piano">逐步學習筆記 →</a> · <a href="https://musicmaker.im/model/seedance-2-0/"><kbd>MusicMaker ↗</kbd></a></p>

這四個模型版本均有 MusicMaker 對應頁面。案例與教學來自模型開發者，品牌入口的可用功能以實際介面為準；H3 配圖為輸入圖。

<!-- OFFICIAL:END -->

<a id="x-creators"></a>

## 從 X 創作者的案例開始

六個已釋出影片案例，配有公開提示詞或截圖教程。**點圖片看原帖，點“輸入與做法”瞭解參考素材並獲取原創練習提示詞。**

<p><a href="https://x.com/Just_sharon7/status/2083422886686031982"><img src="https://pbs.twimg.com/amplify_video_thumb/2083422025452765184/img/ZFIIYS0hQ9OI5TpK.jpg" alt="粉色影棚中跳舞的兩位表演者；點選檢視作者 X 原帖" width="100%"></a><br><b>粉色影棚雙人舞</b><br><sub><a href="https://x.com/Just_sharon7/status/2083422886686031982">@Just_sharon7</a> · Seedance 2.5</sub><br>固定人物，交替使用全景與特寫。<br><a href="https://x.com/Just_sharon7/status/2083422886686031982">看原帖與提示詞</a> · <a href="../docs/x-cases.zh-CN.md#duo">輸入與做法</a></p>

<p><a href="https://x.com/techhalla/status/2086915118307119269"><img src="https://pbs.twimg.com/amplify_video_thumb/2086903458251112448/img/jSPsz35xEe3ZFz47.jpg" alt="TechHalla 音樂短片開頭躺在地面的表演者；點選檢視作者 X 原帖" width="100%"></a><br><b>參考素材驅動演唱</b><br><sub><a href="https://x.com/techhalla/status/2086915118307119269">@techhalla</a> · MiniMax H3</sub><br>先做參考圖，再按音訊安排鏡頭。<br><a href="https://x.com/techhalla/status/2086915118307119269">看影片與提示詞執行緒</a> · <a href="../docs/x-cases.zh-CN.md#h3-performance">輸入與做法</a></p>

<p><a href="https://x.com/AIwithkhan/status/2087754389624860911"><img src="https://pbs.twimg.com/amplify_video_thumb/2087754331089166336/img/uJ0ET9rgvlWZOLj-.jpg" alt="逆光長廊中張開雙臂的表演者；點選檢視作者 X 原帖" width="100%"></a><br><b>魚眼鏡頭說唱表演</b><br><sub><a href="https://x.com/AIwithkhan/status/2087754389624860911">@AIwithkhan</a> · Seedance 2.5</sub><br>用一份人物參考串聯不同場景。<br><a href="https://x.com/AIwithkhan/status/2087754389624860911">看原帖與提示詞</a> · <a href="../docs/x-cases.zh-CN.md#y2k">輸入與做法</a></p>

<p><a href="https://x.com/oggii_0/status/2041392542659584302"><img src="https://pbs.twimg.com/ext_tw_video_thumb/2041392519330840576/pu/img/gJnakn0aUsx_Pqnd.jpg" alt="黑色背景中的白色同心圓；點選檢視作者 X 原帖" width="100%"></a><br><b>抽象形狀變化</b><br><sub><a href="https://x.com/oggii_0/status/2041392542659584302">@oggii_0</a> · Seedance 2.0</sub><br>動態圖形參考：讓同一形狀連續變化。<br><a href="https://x.com/oggii_0/status/2041392542659584302">看原帖與提示詞</a> · <a href="../docs/x-cases.zh-CN.md#motion-design">輸入與做法</a></p>

<p><a href="https://x.com/Strength04_X/status/2098290630179057858"><img src="https://pbs.twimg.com/amplify_video_thumb/2098289904409362432/img/-LuU_JZblovIR9HB.jpg" alt="在昏暗車站站臺等候的旅客；點選檢視作者 X 原帖" width="100%"></a><br><b>從車站駛向太空</b><br><sub><a href="https://x.com/Strength04_X/status/2098290630179057858">@Strength04_X</a> · Seedance 2.5</sub><br>奇幻短片參考：讓場景轉變有跡可循。<br><a href="https://x.com/Strength04_X/status/2098290630179057858">看原帖與提示詞</a> · <a href="../docs/x-cases.zh-CN.md#lunar-train">輸入與做法</a></p>

<p><a href="https://x.com/Strength04_X/status/2090399966988550435"><img src="https://pbs.twimg.com/amplify_video_thumb/2090399674129940480/img/zvDQqERbmMVkeaIT.jpg" alt="站在金色燈光才藝秀舞臺上的年長表演者；點選檢視作者 X 原帖" width="100%"></a><br><b>重拍處的舞臺反轉</b><br><sub><a href="https://x.com/Strength04_X/status/2090399966988550435">@Strength04_X</a> · Seedance 2.5</sub><br>短暫停頓、重拍揭曉，再切反應鏡頭。<br><a href="https://x.com/Strength04_X/status/2090399966988550435">看原帖與提示詞</a> · <a href="../docs/x-cases.zh-CN.md#beat-drop">輸入與做法</a></p>

模型名稱由創作者自述。本次透過公開 X 映象核對正文和所附媒體，未復現這些影片；完整提示詞保留在作者原帖。[來源說明](../docs/x-cases.zh-CN.md#source-notes)。

<a id="listen"></a>

## MusicMaker 試聽

向下試聽九種不同曲風，從鋼琴、搖滾到管弦與舞曲。曲風依據原作詳情的 Style（風格）欄位；影片方向是新編練習建議。

<!-- LISTENING-GRID:START -->
<p><a href="https://musicmaker.im/detail/discover-v2-21/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/sleeptown_windowlight.webp" alt="窗邊唱片機與鍵盤旁聽音樂的插畫女孩" width="100%"></a><br><b>Sleeptown Windowlight</b><br><b>鋼琴獨奏</b><br><sub>長鏡頭與細節特寫</sub><br><a href="https://musicmaker.im/detail/discover-v2-21/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-52/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/voltage_in_my_veins.webp" alt="被藍粉色光帶圍繞的插畫表演者" width="100%"></a><br><b>Voltage In My Veins</b><br><b>現代搖滾</b><br><sub>舞臺切鏡與重拍定格</sub><br><a href="https://musicmaker.im/detail/discover-v2-52/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-24/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/crown_of_the_tempest.webp" alt="藍天下戶外演出的管絃樂隊與合唱團" width="100%"></a><br><b>Crown of the Tempest</b><br><b>史詩管絃</b><br><sub>奇幻敘事與寬闊場景</sub><br><a href="https://musicmaker.im/detail/discover-v2-24/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-87/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/rain_on_beale.webp" alt="溼潤街道映出青綠色遮陽篷咖啡館的插畫" width="100%"></a><br><b>Rain On Beale</b><br><b>低保真爵士</b><br><sub>雨夜城市與迴圈畫面</sub><br><a href="https://musicmaker.im/detail/discover-v2-87/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-42/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/tidal_release.webp" alt="海邊白裙女子上空浮現發光波紋" width="100%"></a><br><b>Tidal Release</b><br><b>漸進浩室舞曲</b><br><sub>逐步加強剪輯與高潮變景</sub><br><a href="https://musicmaker.im/detail/discover-v2-42/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-48/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/back_roads_lead_me_home.webp" alt="面向田野的門廊上彈木吉他的男子" width="100%"></a><br><b>Back Roads Lead Me Home</b><br><b>鄉村抒情</b><br><sub>鄉野故事與暖光人物</sub><br><a href="https://musicmaker.im/detail/discover-v2-48/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-22/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/midnight_garden_circuits.webp" alt="柔色天空下的草地，疊有抽象波紋與封面文字" width="100%"></a><br><b>Midnight Garden Circuits</b><br><b>氛圍電子</b><br><sub>抽象形態與緩慢運動</sub><br><a href="https://musicmaker.im/detail/discover-v2-22/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-60/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/basement_crown.webp" alt="錄音室調音臺旁的音箱上放著金色皇冠" width="100%"></a><br><b>Basement Crown</b><br><b>嘻哈節拍</b><br><sub>街頭質感與利落切點</sub><br><a href="https://musicmaker.im/detail/discover-v2-60/"><kbd>▶ 試聽原作</kbd></a></p>

<p><a href="https://musicmaker.im/detail/discover-v2-90/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/keep_it_open.webp" alt="海景敞門旁相對而坐交談的男女" width="100%"></a><br><b>Keep It Open</b><br><b>電子節奏布魯斯</b><br><sub>情緒近景與呼吸停頓</sub><br><a href="https://musicmaker.im/detail/discover-v2-90/"><kbd>▶ 試聽原作</kbd></a></p>
<!-- LISTENING-GRID:END -->

喜歡哪一種聲音，就先為它做一張封面、一個短鏡頭。[🧰 按創作步驟選免費工具](#toolkit) · [檢視曲風與來源說明](../docs/listening-notes.zh-CN.md) · [瀏覽全部歌曲](https://musicmaker.im/discover/)。封面不是影片截圖；試聽不等於獲得素材使用權。

<a id="first-video"></a>

## 製作你的第一支影片

### 案例一：彩虹山谷，16 秒自然音樂短片

<p><a href="https://musicmaker.im/detail/discover-v2-98/"><img src="https://cdn.musicmaker.im/musicmaker/discover_v2/living_on_the_brightside.webp" alt="溪流、野花與綠色山谷上空的一道彩虹；點選試聽 Living on the Brightside" width="100%"></a></p>

<p>從 MusicMaker《Living on the Brightside》的封面取景：溪流、野花、綠色山谷和彩虹。<b>先不拍人物，用四個鏡頭學會把畫面剪成一個完整樂句。</b><br><br><b>1. 先準備音樂，再確定四個切點</b><br>用自有或獲授權的音樂擷取完整的 16 秒樂句；沒有現成音樂，就用上方原創伴奏，在 GitHub 檔案頁點 <b>Download raw file</b> 儲存。把音訊匯入剪輯軟體，標記 0、4、8、12、16 秒。練習伴奏適用這些切點；換歌后應聽重拍和樂句結束的位置，再調整剪輯。</p>

[▶ 試聽案例原曲](https://musicmaker.im/detail/discover-v2-98/) · [♫ 下載原創練習伴奏](../starter-kit/practice-beat-120bpm.wav)

這是歌曲封面，不是影片截圖。下方是據此新編的練習，不是原作生成記錄。試聽區的九首歌曲與這兩個教程案例不重複。

#### 2. 選一條工具路線

**選擇** — [模型官方：Hailuo H3](https://hailuoai.video/zh-Intl/tools/minimax-h3)

**怎麼開始** — 選擇 MiniMax H3、文字生成影片；每次貼上一段提示詞

**本練習的設定** — 9:16，每段 5 秒；共四段

---

**選擇** — [品牌工具：MusicMaker 短片](https://musicmaker.im/free-short-music-video-generator/)

**怎麼開始** — 文字路線填寫提示詞；圖片路線另需上傳開始圖和結束圖

**本練習的設定** — 頁面當前為 5 秒、480p；選擇 9:16


MusicMaker 短片頁標註使用 MiniMax H3，官方入口則提供更多參考輸入與設定。**本次最容易上手的是文字路線**，不需要下載品牌封面。如果改用圖片路線，使用自己有權使用的同場景圖片；首尾畫面保持相近，別讓清晨突然變成夜晚。

#### 3. 一次只生成一個鏡頭

先生成 A，確認草地、水流與彩虹沒有明顯變形，再做 B、C、D。下面四段分別複製；不必把整張分鏡表塞進一次生成請求。

**成片位置** — 0—4 秒

**鏡頭** — 溪邊野花特寫

**看什麼** — 花瓣不閃爍，運動幅度小

---

**成片位置** — 4—8 秒

**鏡頭** — 溪流與草坡中景

**看什麼** — 水向同一方向流動

---

**成片位置** — 8—12 秒

**鏡頭** — 山谷與彩虹全景

**看什麼** — 彩虹位置穩定，地平線不彎曲

---

**成片位置** — 12—16 秒

**鏡頭** — 同一山谷的靜止遠景

**看什麼** — 留出片名位置，完成收尾


```text
A｜雨後綠色山谷，柔和午後陽光，溪邊紫色野花上留有水珠。
固定特寫，微風只讓花莖輕輕搖動，背景草坡柔和虛化。
寫實自然攝影，不出現人物、建築、文字，不改變花朵數量。
```

```text
B｜雨後同一綠色山谷，柔和午後陽光，淺溪從草坡間流向前景。
固定中景，清水緩慢流過石頭，岸邊紫色野花輕輕搖動。
寫實自然攝影，河道形狀保持穩定，不出現人物、建築或文字。
```

```text
C｜雨後綠色山谷全景，柔和午後陽光，一道彩虹橫跨遠處天空。
前景是淺溪與紫色野花。固定廣角機位，草葉輕動，雲緩慢飄動。
彩虹位置穩定，不新增彩虹，不出現人物、建築、文字或快速運鏡。
```

```text
D｜雨後同一綠色山谷的遠景，柔和午後陽光，淺溪通向遠處的一道彩虹。
固定機位，只有溪水和草葉輕微運動；畫面下部留出乾淨草地供後期加片名。
保持地形和彩虹穩定，不出現人物、建築或文字。
```

#### 4. 剪成 16 秒，再加標題

將四段依次拖入剪輯時間軸，每段選取最穩定的 4 秒，使用直接切換。關閉生成片段自帶聲音，只保留選定的伴奏。在最後 2 秒加入片名，片尾給音樂做短淡出；不要靠拉長靜幀掩蓋缺失鏡頭。匯出 MP4，豎屏比例保持 9:16，解析度按實際素材選擇，放大 480p 不會增加細節。[剪輯按鈕與匯出步驟](../docs/first-video.zh-CN.md#edit-timeline)。

**完成標準：** 音樂與畫面同時結束；沒有黑幀和重複音軌；溪水方向、光線和彩虹沒有明顯跳變。彩虹變形就減小運動、固定機位；鏡頭間地形差異太大，就用同一張自有場景圖作為參考重做。以上提示詞尚未實測生成，不保證復現封面。

<a id="next-project"></a>

## 把一個提案做完，再學下一種技巧

### 案例二：一句副歌，10 秒人像演唱

<p><a href="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_video.mp4"><img src="https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_cover.webp" alt="粉色舞臺燈光下、金色麥克風前的歌手輸入人像；點選觀看品牌演唱示例" width="100%"></a></p>

<p>這次從自然風景切換到<b>固定近景的人物表演</b>。目標是唱完一句自己的副歌，並讓嘴形、表情與聲音一致；先不加舞蹈、換裝或切鏡。<br><br><b>1. 準備一張人像、一句歌聲</b><br>選擇有使用權的正面或輕微側面人像，嘴部清楚可見，麥克風不遮嘴，先將雙手放在畫面外。用自己錄製或有授權的歌聲剪出約 10 秒完整樂句，開頭和結尾各留一點呼吸空隙。儘量選主唱清晰、沒有多人疊唱的一句。上面的器樂練習伴奏<b>不能代替歌聲音訊</b>。</p>

[▶ 觀看品牌演唱示例](https://cdn.musicmaker.im/musicmaker/ai_music_video_generator/example/example2_video.mp4) · [檢視案例來源](../docs/brand-examples.md)

圖為官網示例的**輸入人像**，點圖觀看約 10 秒成片。官網沒有公佈該演唱示例使用的底層模型；下面的兩條路線是練習選擇，不是對原作模型的推斷。

#### 2. 按工具放入相同素材

**選擇** — [模型官方：Hailuo H3](https://hailuoai.video/zh-Intl/tools/minimax-h3)

**輸入位置** — 選擇 H3 → Omni Reference；在 Refs 放入人像與歌聲音訊，再填提示詞

**先核對什麼** — 音訊參考須與圖片或影片配合；設定約 10 秒和匹配人像的畫幅

---

**選擇** — [品牌工具：MusicMaker 演唱](https://musicmaker.im/ai-music-video-generator/)

**輸入位置** — 歌聲放到 Music File，人像放到 Character Image，提示詞放到 Prompt

**先核對什麼** — 先裁好音訊，再看預計消耗和 Public 開關，確認後 Generate


官方參考模式能結合人物與音訊；品牌入口將音樂、人像和提示詞放在同一流程中。兩者設定不同，不能把短片頁的“文字生成”當成音訊驅動演唱。

#### 3. 複製這一段完整提示詞

```text
以我上傳的人像為唯一人物參考，以我上傳的歌聲音訊為表演時間依據。
同一位成年歌手，保持輸入人像的臉部、髮型、服裝和原有燈光不變。
固定肩部以上近景，麥克風位於嘴部側下方，不遮住嘴唇；雙手不進入畫面。
跟隨輸入樂句自然演唱，嘴形對應歌聲，輕微呼吸、眨眼和點頭。
長音時保持姿態，樂句結束後自然放鬆；不要說額外臺詞或改變歌詞。
不換裝、不轉身、不切鏡、不新增其他人物、文字或誇張表情。
```

這是新編練習提示詞，不是原作提示詞，也未實測生成。提示詞提出的是目標，不能保證輸出保留原音軌或準確對口型。

#### 4. 先修口型，再考慮運鏡

先聽開頭、句中和結尾，再看嘴唇開合是否對應母音與收音。整段只是固定提前或延後，可在剪輯軟體中小幅移動畫面；越到後面越錯位，說明不是簡單偏移，應縮短樂句或重新生成。臉部漂移時去掉點頭與運鏡；嘴被遮擋時更換人像，不要只往提示詞裡繼續加限制。

#### 5. 留一個聲音版本，匯出完整樂句

把成片與原歌聲放到同一時間軸。若使用原歌聲，關閉生成影片的聲音並重新檢查同步；若使用生成聲音，就移除重複音軌。先保持單鏡頭，在最後一秒新增自己的歌曲名。匯出 MP4 後檢查嘴形、臉部、音量與句尾，確保樂句唱完而非突然截斷。[詳細剪輯與演唱檢查](../docs/first-video.zh-CN.md#vocal)。

**完成標準：** 同一個人唱完同一句；嘴部始終清晰；只有一條主音軌；片尾保留自然呼吸。達到這四項後，再嘗試緩慢推近，同一輪只增加一種變化。

<a id="toolkit"></a>

## 免費起步的音樂影片工具庫

從剛才的曲風選擇出發，按缺少的素材選工具。下面前四項是官網標註免費的入口；歌曲生成、人像演唱及完整目錄中的其他工具可能需要額度或付費，見[當前價格](https://musicmaker.im/pricing/)。公開示例可供參考，使用素材仍需相應授權。

<p><b>🖼 補封面與分鏡圖</b></p>

<p><a href="https://musicmaker.im/free-chatgpt-images-2-5/"><kbd>↗ 免費製圖</kbd></a></p>

<p><b>🎬 做一個短鏡頭</b></p>

<p><a href="https://musicmaker.im/free-short-music-video-generator/"><kbd>↗ 5 秒短片</kbd></a> · <a href="https://musicmaker.im/free-text-to-video/"><kbd>↗ 文字生成影片</kbd></a></p>

<p><b>🎧 改變聲音質感</b></p>

<p><a href="https://musicmaker.im/lofi-song-maker/"><kbd>↗ 低保真音色轉換</kbd></a></p>

<p><b>📦 整理音訊格式與曲目資訊</b></p>

<p><a href="https://musicmaker.im/audio-converter/mp3-to-wav/"><kbd>↗ MP3 → WAV</kbd></a> · <a href="https://musicmaker.im/mp3-tag-editor-online/"><kbd>↗ 歌曲資訊編輯</kbd></a></p>

<p><b>📚 找歌曲、案例和提示詞</b></p>

<p><a href="https://musicmaker.im/discover/"><kbd>↗ 歌曲與封面</kbd></a> · <a href="https://musicmaker.im/ai-music-video-generator/"><kbd>↗ 影片示例</kbd></a> · <a href="../prompts/README_ZH.md"><kbd>↗ 12 套提示詞</kbd></a></p>

[→ 展開全部素材與工具：六類導航、93 個入口](../docs/brand-resources.zh-CN.md)

## 模型能力，回到官方資料核對

<!-- CAPABILITIES:START -->
<p><b>Seedance 2.5</b><br>音樂會：分別指定場地、主唱、樂手與合唱團參考。</p>

<p><a href="https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#seedance-concert">逐步學習筆記 →</a><br><a href="https://musicmaker.im/model/seedance-2-5/"><kbd>MusicMaker · Seedance 2.5 ↗</kbd></a></p>

<p><b>MiniMax H3</b><br>人像演唱：將運鏡、人物和歌聲分配給不同參考。</p>

<p><a href="https://hailuoai.video/tools/minimax-h3">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#h3-singing">逐步學習筆記 →</a><br><a href="https://musicmaker.im/model/minimax-h3/"><kbd>MusicMaker · MiniMax H3 ↗</kbd></a></p>

<p><b>Veo 3.1</b><br>奇幻演唱場景：用參考素材組織人物與環境。</p>

<p><a href="https://deepmind.google/models/veo/prompt-guide/">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#veo-scene">逐步學習筆記 →</a><br><a href="https://musicmaker.im/model/veo-3-1-ai/"><kbd>MusicMaker · Veo 3.1 ↗</kbd></a></p>

<p><b>Seedance 2.0</b><br>鋼琴演奏：從人物中景切到表情特寫。</p>

<p><a href="https://seed.bytedance.com/en/seedance2_0">官方教學／提示詞 ↗</a><br><a href="../docs/official-cases.zh-CN.md#seedance-piano">逐步學習筆記 →</a><br><a href="https://musicmaker.im/model/seedance-2-0/"><kbd>MusicMaker · Seedance 2.0 ↗</kbd></a></p>

這四個模型版本均有 MusicMaker 對應頁面。案例與教學來自模型開發者，品牌入口的可用功能以實際介面為準；H3 配圖為輸入圖。
<!-- CAPABILITIES:END -->

- **MiniMax Music 3.0**：輸入包括“creative concept and optional lyrics”（創作構思與可選歌詞）。[MiniMax 官方釋出](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model)。先描述歌曲各段如何變化，再安排分鏡。 [MusicMaker ↗](https://musicmaker.im/minimax/minimax-music-v3-0/)
- **Eleven Music**：官方建議寫明“genre, mood, instrumentation, tempo, and production era”（曲風、情緒、樂器、速度與製作年代）。[ElevenLabs 提示詞指南](https://elevenlabs.io/docs/overview/capabilities/music/best-practices)。這些具體資訊比單寫“好聽、有氛圍”更便於表達需求。 [MusicMaker ↗](https://musicmaker.im/eleven-labs/eleven-labs-music/)

[模型資料與實際用法 →](../docs/models.md) · [工具限制與來源記錄](../docs/sources.md)

## 繼續創作

[看 Lofi Girl、OK Go 與 Gorillaz 的做法](../docs/inspiration.md) · [複製分鏡計劃模板](../starter-kit/brief-template.md) · [貢獻自己的方案](../CONTRIBUTING.md)

由 [AI Music Maker](https://musicmaker.im/) 維護，可搭配你習慣的生成與剪輯工具。原創文字、程式碼和練習音樂採用 [MIT 許可](../LICENSE)；外部音樂、圖片、影片仍歸各自權利人所有，見[素材來源與使用說明](../assets/README.md)。

<!-- AFFILIATE:START -->
**聯盟推廣合作**

MusicMaker 支援聯盟推廣合作。歡迎透過教學、評測或社群分享我們的音樂創作工具，並依計畫規則獲得有效推薦訂單的佣金。

<a href="https://musicmaker.im/affiliate-program/"><kbd>↗ 瞭解並申請聯盟合作</kbd></a>
<!-- AFFILIATE:END -->
