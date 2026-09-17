# 半人马AI学院 · 国潮科技 — Style Reference

> 深海藏青底上的鎏金细线与一抹马身橘橙，半人马像神兽一样在发光云纹里登场

**Theme:** dark

国潮科技是第四轮「土中带着炫酷」里土炫平衡的一版。底色取 logo 马身蓝往深里压的深海藏青（#050E24 → #0A1B3F → #10275A 三层），不用纯黑——这是 WAIC、火山 FORCE 和博鳌主视觉里老板们熟悉的「深蓝配金」的高级感。鎏金 #D8B46A 只做细线、描边、云纹、回纹和 ≥28px 的金属渐变大字，正文一个金字都不放。logo 人身的橘橙 #F58A2A 是点睛色，只给「联系学院顾问」主按钮、引号和印章，全页可见面积 ≤3%。中国味靠纹样而不是靠红：云纹、回纹、山脊线用 1px 发光细线画成电路和数据流，接点是金色小圆点，像在电路板上描了一幅山水。标题是「粗黑 + 书法」混排——「让 AI 成为」Noto Sans SC 900 字距拉开，「你的能力。」马善政毛笔楷书金属渐变；书法全站只出现两处（主标题下半句、竖排题签），其余标题一律 Noto Serif SC 900 粗宋，稳、正、有分量。签名记忆点是**半人马登场**：滚动时神兽从 0.55 倍放大到终态，身后金环由暗转亮、钴蓝光束从天而降，钉住的一小段里一道暖金扫光掠过马身，像发布会主角出场；手机上终态宽 359px，桌面 720px，都在分辨率天花板以内。

## Tokens — Colors

| Name       | Value     | Token                      | Role                                              |
| ---------- | --------- | -------------------------- | ------------------------------------------------- |
| 深海       | `#050E24` | `--color-abyss`            | 页面底色，比纯黑多一层蓝                          |
| 藏青       | `#0A1B3F` | `--color-navy`             | 共学五步、入局区块底                              |
| 抬升藏青   | `#10275A` | `--color-navy-raised`      | 卡片、产品铭牌、题跋底                            |
| 高位藏青   | `#1A3470` | `--color-navy-high`        | 主视觉光晕中心、禁用按钮底、卷轴纸                |
| 藏青细线   | `#274A8C` | `--color-navy-line`        | 输入框、禁用按钮描边                              |
| 钴蓝       | `#2F6FE0` | `--color-cobalt`           | 预留：与 logo 马身同色系的实色块                  |
| 钴蓝光     | `#6FB4FF` | `--color-cobalt-glow`      | 数据流虚线、粒子、光束，不用于文字                |
| 钴蓝字     | `#A6D1FF` | `--color-cobalt-ink`       | Cinzel 英文标签（对高位藏青 7.4:1，对深海 12:1）  |
| 鎏金       | `#D8B46A` | `--color-gold`             | 细线、描边、云纹、回纹、链接下划线                |
| 浅金       | `#F6E2AE` | `--color-gold-light`       | 纹样接点、hover 描边                              |
| 暗金       | `#A57C35` | `--color-gold-deep`        | 金属渐变的暗部反光                                |
| 马身橘橙   | `#F58A2A` | `--color-orange`           | 主按钮，全页 ≤3%                                  |
| 亮橘       | `#FFB066` | `--color-orange-light`     | 主按钮高光、引号                                  |
| 印泥橙     | `#D9650F` | `--color-orange-deep`      | 院长印章                                          |
| 宣白       | `#F5F1E6` | `--color-ink`              | 正文与标题（对深海 17:1，对抬升藏青 12.8:1）      |
| 月灰       | `#C4CEE2` | `--color-ink-muted`        | 次要文字（对藏青 10.7:1，对抬升藏青 9.1:1）       |
| 禁用灰     | `#AEB8CF` | `--color-ink-disabled`     | 禁用按钮文字、占位符（对高位藏青 6:1）            |
| 按钮深字   | `#050E24` | `--color-on-orange`        | 橘橙按钮上的字（7.8:1）                           |
| 焦点金     | `#FFD27A` | `--color-focus`            | 键盘焦点环 3px                                    |

### 柔和语义色（深底版：半透明叠加，只用于线和光）

| Name     | Background                  | Text / Line | Token                         |
| -------- | --------------------------- | ----------- | ----------------------------- |
| 金·强    | `rgba(216,180,106,.5)`      | `#D8B46A`   | `--color-gold-a50`            |
| 金·中    | `rgba(216,180,106,.3)`      | `#D8B46A`   | `--color-gold-a30`            |
| 金·弱    | `rgba(216,180,106,.15)`     | `#F5F1E6`   | `--color-gold-a15`            |
| 金·底    | `rgba(216,180,106,.08)`     | `#F5F1E6`   | `--color-gold-a08`            |
| 蓝·光    | `rgba(111,180,255,.4)`      | `#6FB4FF`   | `--color-cobalt-a40`          |
| 蓝·网格  | `rgba(111,180,255,.15)`     | —           | `--color-cobalt-a15`          |

### 渐变（金属与光效）

| Name     | Token                  | Role                                         |
| -------- | ---------------------- | -------------------------------------------- |
| 金属金   | `--gradient-gold`      | 五段式带暗部反光，只给 ≥28px 大字、卷轴轴头  |
| 金线     | `--gradient-gold-line` | 两端渐隐的鎏金线，眉标两侧                   |
| 橘橙     | `--gradient-orange`    | 主按钮，上亮下实                             |
| 天光     | `--gradient-hero`      | 主视觉顶部的藏青光晕                         |
| 光束     | `--gradient-beam`      | 半人马头顶的钴蓝光柱                         |
| 扫光     | `--gradient-sweep`     | 登场时掠过马身的暖金光带（以抠图作遮罩）     |
| 面板     | `--gradient-panel`     | 卡片、窗格、题跋底                           |

## Tokens — Typography

### 马善政毛笔楷书 Ma Shan Zheng — 题字 · `--font-brush`

- **Substitute:** STKaiti, KaiTi, Kaiti SC
- **Weights:** 400
- **Sizes:** 28px（手机题签）, 34–42px（竖排题签）, 62–128px（主标题下半句）
- **Tracking:** 题签（横排与竖排）-0.04em——马善政字面只占字格约 0.8–0.9em，负字距后字与字的实际空隙约 0.1em，读起来是一句话；「AI」横入竖排时字距归 0，保持正常宽度
- **Role:** 全站只用两处：H1「你的能力。」、主视觉竖排题签「人决定方向，AI 拓展人的能力。」。按 `&text=` 只加载这 16 个字，不用于正文和长句。

### Noto Serif SC 900 — 粗宋标题 · `--font-title`

- **Substitute:** Songti SC, STSong, SimSun
- **Weights:** 700, 900
- **Sizes:** 20px（顶栏品牌）, 22–28px, 34–60px, 30–44px（页脚口号）
- **Role:** 章节标题、五步标题、卡片标题、院长引文、口号——最「正」的那种字，像牌匾。
- **Tracking:** 标题 0.06em；页脚口号「各有知君，共创万象。」0.08em——超过 0.12em 会读成一个字一个字地蹦，口号要读成一句话。

### Noto Sans SC — 粗黑主标与正文 · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei
- **Weights:** 400（正文）, 500（导语）, 700（按钮）, 900（主标）
- **Sizes:** 16px, 18–19px, 20–24px, 46–88px
- **Line height:** 正文 1.8 / 导语 1.7 / 主标 1.15
- **Role:** 「让 AI 成为」900 字距 0.06em；其余所有正文。上线可换阿里妈妈数黑体（主标）+ 阿里巴巴普惠体（正文），均免费商用、需自托管。

### Cinzel — 碑刻罗马字 · `--font-latin`

- **Substitute:** Trajan Pro, Times New Roman
- **Weights:** 700
- **Sizes:** 13–14px（大写，字距 0.12–0.18em）
- **Role:** CENTAUR AI ACADEMY、HUMAN × AI 等英文小标签，钴蓝光色，不承载关键信息。

### Oswald — 编号 · `--font-num`

- **Substitute:** DIN Condensed, Bahnschrift
- **Weights:** 600
- **Sizes:** 28px, 40px, 48–60px
- **Role:** 只给「三章节 01–03」和「共学五步 01–05」这两组真实顺序，金属金填充。

同屏中文字体：书法 1 + 粗宋 1 + 黑体 1 = 3 种，不再加。

### Type Scale

| Role    | Size                           | Line Height | Letter Spacing | Token            |
| ------- | ------------------------------ | ----------- | -------------- | ---------------- |
| brush   | clamp(62px, 6vw+38px, 128px)   | 1.15        | 0.02em         | `--text-brush`   |
| hero    | clamp(46px, 4.4vw+28px, 88px)  | 1.15        | 0.06em         | `--text-hero`    |
| display | clamp(34px, 2.6vw+24px, 60px)  | 1.3         | 0.04em         | `--text-display` |
| heading | clamp(26px, 1.2vw+20px, 36px)  | 1.3         | 0.04em         | `--text-heading` |
| title   | clamp(22px, .5vw+20px, 28px)   | 1.3–1.4     | 0.06em         | `--text-title`   |
| lead    | clamp(20px, .4vw+18.5px, 24px) | 1.7         | 0              | `--text-lead`    |
| body    | clamp(18px, .15vw+17.5px, 19px)| 1.8         | 0              | `--text-body`    |
| small   | 16px                           | 1.6         | 0              | `--text-small`   |
| label   | 14px                           | 1.4         | 0.18em         | `--text-label`   |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 4px`）

**Density:** 宽松——老花眼优先，手机正文 18px/1.8，按钮 56px 高

### Spacing Scale

| Name        | Value                       | Token           |
| ----------- | --------------------------- | --------------- |
| gutter      | clamp(16px, 4vw, 48px)      | `--gutter`      |
| section-gap | 48px（<700）/ clamp(88px, 9vw, 150px)（≥700） | `--section-gap` |
| container   | 1200px                      | `--container`   |
| header      | 64px（手机）/ 78px（桌面）  | `--header-h`    |

### Border Radius

| Name   | Value | Token             |
| ------ | ----- | ----------------- |
| sm     | 4px   | `--radius-sm`     |
| md     | 10px  | `--radius-md`     |
| lg     | 18px  | `--radius-lg`     |
| window | 28px  | `--radius-window` |
| full   | 999px | `--radius-full`   |

| Element        | Value           |
| -------------- | --------------- |
| 按钮 / 输入框  | 10px (md)       |
| 卡片 / 铭牌    | 18px (lg)       |
| 插画圆角窗格   | 28px (window)   |
| 题跋 / 徽标 / 印章 | 4px (sm)    |
| 卷轴轴头       | full            |

### Shadows & Glow

| Name        | Value                                                                  | Token           |
| ----------- | ---------------------------------------------------------------------- | --------------- |
| glow-gold   | `0 0 0 1px rgba(216,180,106,.45), 0 0 22px rgba(216,180,106,.16)`      | `--glow-gold`   |
| glow-cobalt | `0 0 0 1px rgba(111,180,255,.35), 0 0 26px rgba(111,180,255,.14)`      | `--glow-cobalt` |
| glow-orange | `0 0 0 1px rgba(255,176,102,.6), 0 8px 28px rgba(245,138,42,.35)`      | `--glow-orange` |
| deep        | `0 24px 60px rgba(0,0,0,.45)`                                          | `--shadow-deep` |
| text        | `0 2px 0 rgba(0,0,0,.35)`                                              | `--shadow-text` |

外发光只给三样东西：鎏金细框、主按钮、五步奖章。卡片静止时只有 1px 金线，hover 才亮。

### Motion

| Name       | Value                              | Token          |
| ---------- | ---------------------------------- | -------------- |
| ease-rise  | `cubic-bezier(0.22, 1, 0.36, 1)`   | `--ease-rise`  |
| dur-fast   | 160ms                              | `--dur-fast`   |
| dur-base   | 280ms                              | `--dur-base`   |
| pin-top    | 76px（手机）/ 96px（桌面）         | `--pin-top`    |
| zoom-lead  | min(46svh, 400px)                  | `--zoom-lead`  |
| zoom-hold  | min(8svh, 64px)（<700）/ min(36svh, 300px)（≥700） | `--zoom-hold`  |
| glint-lead | min(16svh, 140px)（<700）/ 0px（≥700）| `--glint-lead` |
| zoom-from  | 0.55                               | `--zoom-from`  |

- 半人马登场：`.stage` 做 `view-timeline`，画框 `position:sticky` 钉在 `--pin-top`。钉线前 `zoom-lead` 距离内 scale 0.55→1、金环 0.8→1、透明度 0.6→1（首屏就能看见金环）、光束淡入；钉住的 `zoom-hold`（额外滚动 ≤300px，远小于 90svh）里暖金扫光从左到右掠过马身。只写 transform / opacity。
- 手机（<700）防空屏：钉住段只留 64px，扫光提前 `glint-lead` 在放大后段开始；图注与题签不淡入、始终可见；首个章节上边距 40px、区块间距 48px、入局框上下 36px、页脚上边距 28px。验收标准：390×844 从顶部每滚 100px，视口内无文字/图片/按钮的纵向空带 ≤160px（实测最大 150px）。
- 桌面（≥1024）首屏：hero 上边距 28px、各段间距收紧、舞台上边距 8px、放大原点改为画框顶边（50% 0），1440×900 在 scrollY=0 时能看到金环与半人马上半身（初始 0.55 倍，画框顶 652px）。
- 写在 `@supports (animation-timeline: view())` + `prefers-reduced-motion: no-preference` + `max-height:1600px` 里，`animation-timeline` 在 `animation` 简写之后。
- JS 兜底：不支持时（安卓微信、iOS 26 以下）或 URL 带 `?nosd` 时启用；IntersectionObserver 只在舞台附近（±200px）挂 passive scroll，rAF 合帧，与 CSS 同一区间。
- `prefers-reduced-motion: reduce`：不钉住、不放大，直接终态。
- 常驻微动效只有两个：外圈钴蓝虚线环 90s 一圈、粒子 4.8s 呼吸，全部 reduce 时关掉。

### Layout

- **Section gap:** 88–150px
- **Card padding:** 12px 外框 + 8px 内文
- **Element gap:** 16–28px
- **Max content width:** 1200px

## Components

### Primary Button · 联系学院顾问

**Role:** 唯一主 CTA
`background: var(--gradient-orange)` 深海字 `--color-on-orange`（7.8:1），`min-height:56px`（顶栏 52px），`padding:0 28px`，`font:19px/700`，`radius:10px`，`box-shadow: var(--glow-orange)`。hover 亮 6% 上浮 1px；active scale(.98)；focus 3px 焦点金环。文字必须写全「联系学院顾问 ↗」。手机端顶栏不放按钮，改成右下浮钮（首屏按钮可见时隐藏，避免同屏两个）。

### Outline Button · 复制客服链接

**Role:** 次级动作
透明底 + 1px 鎏金内描边，宣白字。hover 金底 8% + 金色外发光；复制后在下方 `role=status` 写「已复制」。

### Disabled Button · 下载知君 / 下载万象

**Role:** 暂未开放
高位藏青底 + 藏青细线 + 禁用灰字（对底 6:1），`min-height:52px`、18px 字，`cursor:not-allowed`，旁边用 16px 月灰写「下载暂未开放」，用 `aria-describedby` 关联。

### Text Link

**Role:** 了解更多类链接
宣白字 + 2px 鎏金下划线（背景图实现），hover 字变浅金、线加粗到 3px。触控高度 ≥44px。

### 章节插画框（三种轮换）

**Role:** 把暖米色纸感插画「装进」深蓝画面
- **圆角窗格**（章节 01）：28px 圆角，10px 藏青面板衬边 + 内侧 1px 金线 + 对角两枚 2px 金色角标。
- **扇面**（章节 02）：SVG `clipPath` 裁成折扇，2px 鎏金扇边 + 5 根 1px 扇骨 + 一道内弧，金色外发光。
- **卷轴**（章节 03）：左右两根金属金轴头（全圆角），中间高位藏青「绫边」上下各 1px 金线。
插画本身不调色、不叠色，靠画框的冷暖对比让它像一幅被装裱起来的画。

### 神兽舞台（Hero Figure）

**Role:** 签名记忆点
透明抠图 + 内联 SVG：双金环（实线 + 1:7 点线）、90s 自转的钴蓝虚线环、三枚菱形金接点、两组呼吸粒子、左右两朵线描云纹托底；背后一道梯形钴蓝光束；抠图上叠一层以抠图为遮罩的暖金扫光。竖排题签贴在舞台右侧（手机横排，左右两道金线夹住）。马善政没有竖排标点字形，竖排时「，」「。」包一层 `.pv` 挪到字格右上（translate .55em, -.6em），紧贴上一字，不在列底孤悬。

### 产品铭牌

**Role:** 知君 / 万象
抬升藏青底 + 1px 金线，18px 圆角。产品名 24px 粗宋 + 说明文字链；下一行禁用下载钮 + 「下载暂未开放」。

### 五步阵

**Role:** 共学五步（真实顺序）
桌面：五枚 96px 圆形奖章（深海心 + 藏青环 + 金线环 + 金色外发光），一上一下错落，挂在一条金实线 + 钴蓝虚线双股「数据流」波浪上。手机：64px 奖章竖排，左侧一根金→蓝→金渐变发光竖线串起来。编号 Oswald 金属金。

### 期刊卡

**Role:** 观点与动态
面板渐变底 + 1px 金线，12px 内框放封面（10px 圆角），「观点」徽标 + 日期 + 粗宋书名号标题 + 月灰摘要。整卡可点（标题链接 `::after` 覆盖），hover 金线亮 + 上浮 2px + 封面 1.03。桌面左大右二。

### 题跋引文

**Role:** 院长寄语
4px 小圆角 + 三层描边（1px 金 / 7px 藏青 / 1px 半金），像装裱的题跋。桌面引文竖排、左右两道细线，引号用亮橘；手机横排。署名旁一枚倾斜 4° 的印泥橙方印「嘉木」。

### 入局邀请

**Role:** 联系区
藏青底 + 金色棋盘细格（径向渐隐）+ 四角两黑两白发光「棋子」，标题「带上你的问题，/ 我们一起往前走。」下半句金属金——邀请入局，不是促销。

### Badge

**Role:** 类型标记
4px 圆角、1px 半金描边、16px 字（「观点」）。另有钴蓝描边版给英文标签。不做实心彩色角标，避免电商感。

### Input Field

**Role:** 预留表单
56px 高、深海底、1px 藏青细线；hover 半金线；focus 金线 + 金色外发光。首页不放表单。

## Surfaces

| Level | Name         | Value                       | Purpose                  |
| ----- | ------------ | --------------------------- | ------------------------ |
| 0     | abyss        | `#050E24`                   | 页面底                   |
| 1     | navy         | `#0A1B3F`                   | 通栏区块（五步、入局）   |
| 2     | panel        | `#10275A → #0A1B3F` 渐变    | 卡片、窗格、题跋         |
| 3     | navy-high    | `#1A3470`                   | 光晕中心、禁用、卷轴纸   |
| 顶栏  | abyss-a92    | `rgba(5,14,36,.92)`         | 吸顶导航                 |

## Do's and Don'ts

### Do

- 底色永远是深海藏青，从 #050E24 往上抬层级，不用 #000。
- 金色只画线和 ≥28px 大字；正文、说明、按钮文字一律宣白或月灰。
- 橘橙是稀缺资源：主按钮、引号、印章，三处以内。
- 纹样一律 1–1.5px 细线，接点用 3px 金圆点，线条要「画得出电路」，不要填色块。
- 书法全站两处，其余标题粗宋，数字 Oswald——字体各司其职。
- 插画进框：窗格、扇面、卷轴三选一轮换，不硬贴在深底上。
- 手机优先：390 宽下正文 18px、按钮 56px、次要文字 16px，再往桌面扩。
- 每个视口高度尺寸都带 px 上限（`min(46svh,400px)`），超高窗口直接静态终态。

### Don't

- 不用彩虹多色、紫粉渐变、满屏闪动、爆炸贴；光效只有金、钴蓝两种。
- 不做仙侠页游：不加火焰、剑气、龙鳞、厚重描边立体字、斜体书法大字。
- 不编任何数字、学员数、客户 logo、评价、合影、奖牌。
- 不把文字压在云纹、网格上——纹样只在留白处，文字区域背景保持干净。
- 不在正文用书法字，不在同屏放第四种中文字体。
- 不用「限时」「震撼」「重磅」类字眼，不加角标轰炸。
- 不钉住超过 300px 额外滚动，不做视差轰炸。

## Imagery

主视觉只有一个物件：透明底折纸半人马，放在深蓝舞台正中偏下，被金环、光束、粒子和云纹「托起来」——借 WAIC、华为全联接「一个物件当主视觉」的做法，而不是满屏堆元素。三张暖米色纸感插画用画框装裱，冷底暖画形成强对比，反而显得贵。期刊封面直接用原图，靠 12px 面板内衬和 10px 圆角统一。背景纹样全部内联 SVG：山脊线（钴蓝 + 鎏金两股折线，带电路引脚）、回纹带（24px 单元）、云纹（四段卷曲弧线）、棋盘细格。图标不用 emoji，箭头用 ↗ → ↓ 字符。

## Layout

- **顶栏**：左 logo + 双行品牌名（粗宋 + Cinzel），桌面右侧四导航 + 橘橙按钮；手机「菜单」按钮 + 抽屉，CTA 改右下浮钮（左侧 116px 让给「全部方案」）。
- **主视觉**：居中对称。眉标（英文 + 中文，两侧金线）→ 粗黑主标 → 书法金字 → 导语 → 说明 → 按钮组 → 神兽舞台（钉住放大）→ 图注 → 回纹带。背景是天光径向渐变 + 渐隐网格 + 山脊电路线。
- **三章节**：桌面 5:7 文图分栏，第二章镜像；编号「01」Oswald 金 + 章节名 + 渐隐金线。
- **共学五步**：藏青通栏，标题居中，桌面五步横排错落于波浪数据流上，左上右下两朵淡云纹。
- **观点与动态**：标题左对齐 + 右侧「全部观点与动态」；卡片左大右二。
- **院长寄语**：题跋框，桌面右侧竖排引文、左侧正文与署名印章。
- **联系**：棋盘入局框，居中。
- **页脚**：居中 logo、金属金口号、回纹短带、三行说明。
- 断点：<700 单列；700–1023 两列卡片、题签竖排；≥1024 桌面栅格。

## Agent Prompt Guide

Quick Color Reference:

```
background: #050E24 (abyss) / #0A1B3F (navy) / #10275A (raised)
foreground: #F5F1E6
muted: #C4CEE2
gold (lines, ≥28px only): #D8B46A  / light #F6E2AE
orange (≤3%, CTA only): #F58A2A → #FFB066
cobalt glow (data lines, particles): #6FB4FF
cobalt ink (latin labels): #A6D1FF
focus: #FFD27A
```

Example Component Prompts:

1. 做一个主按钮：`background: var(--gradient-orange)`，字色 `#050E24`，56px 高、10px 圆角、19px/700，文字「联系学院顾问 ↗」，`box-shadow: var(--glow-orange)`，hover 上浮 1px，active scale .98，focus 3px `#FFD27A` 外环。
2. 做一个扇面插画框：SVG clipPath 裁出 600×305 扇形（外弧 R390、内弧 R150），图片 object-fit:cover；上面叠同路径 2px `#D8B46A` 描边 + 5 根 1px 扇骨（35% 透明），`filter: drop-shadow(0 0 6px rgba(216,180,106,.5))`。
3. 做一个五步奖章：96px 圆，`#050E24` 心，`box-shadow: var(--glow-gold), inset 0 0 0 7px #0A1B3F, inset 0 0 0 8px rgba(216,180,106,.5)`，中间 Oswald 600 40px 金属金编号；下方 Noto Serif SC 900 28px 标题 + 16–18px 月灰说明。

## Similar Brands

- **WAIC 2026 世界人工智能大会** — 借「一个发光物件做主视觉 + 标题只挑关键词上色」：本版只给「你的能力」「起点」「一起做」等关键词上金属金，其余保持宣白；主视觉只放半人马一个物件。
- **火山引擎 FORCE 原动力大会 2022** — 借深海军蓝底（约 #000A3A）+ 体积光：落到 `--color-abyss` 和半人马头顶的钴蓝光束 `--gradient-beam`；避开它「暗底叠暗字」和浮标堆叠的反面。
- **博鳌亚洲论坛** — 借藏蓝 #004077 + 金黄的「论坛主视觉」配色关系，以及居中端正的大标语构图。
- **中欧国际工商学院 CEIBS（手机版）** — 借「金色细线金字塔」的线描手法：本版的山脊电路线、扇骨、云纹都是同样的细金线；也借了它金色标题栏卡片的装裱感（题跋框、铭牌）。
- **长江商学院 CKGSB EMBA 横幅** — 借「深蓝星空 + 金色光尘」老板一眼能懂的炫：落到网格上的粒子与金色接点。
- **云栖大会 / 华为全联接** — 借「中文大标题 + 英文副标」双语格式与字距拉开的品牌名：Cinzel 钴蓝英文眉标、主标 0.06em 字距。

## 新增的结构性文字

以下文字不在 content.md 中，只用于导航、状态和组件样张，不含任何事实性说法：

- 「菜单」「关闭」（手机顶栏菜单按钮）
- 「跳到正文」（键盘跳转链接）
- 「已复制」（复制客服链接后的状态提示）
- 印章「嘉木」（院长署名的装饰性重复，aria-hidden）
- H2「每一次共学，都向前一点」：由 content.md 共学五步的眉标升级为区块标题，文字不变
- kit.html 内的说明文字（色板名与角色、字号标注、状态名 default/hover/active/focus/disabled、「只在样张展示，首页不放表单。」「例：每周的销售复盘」占位、「圆角窗格 · 章节 01」等图注、「国潮科技 · 组件样张」标题与说明句），只出现在组件样张，不进入首页

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 深海藏青底 */
  --color-abyss: #050E24;
  --color-navy: #0A1B3F;
  --color-navy-raised: #10275A;
  --color-navy-high: #1A3470;
  --color-navy-line: #274A8C;
  --color-cobalt: #2F6FE0;
  --color-cobalt-glow: #6FB4FF;
  --color-cobalt-ink: #A6D1FF;

  /* Colors — 鎏金 */
  --color-gold: #D8B46A;
  --color-gold-light: #F6E2AE;
  --color-gold-deep: #A57C35;

  /* Colors — logo 橘橙（点睛） */
  --color-orange: #F58A2A;
  --color-orange-light: #FFB066;
  --color-orange-deep: #D9650F;

  /* Colors — 文字 */
  --color-ink: #F5F1E6;
  --color-ink-muted: #C4CEE2;
  --color-ink-disabled: #AEB8CF;
  --color-on-orange: #050E24;
  --color-focus: #FFD27A;

  /* Colors — 半透明（光效与细线） */
  --color-gold-a50: rgba(216, 180, 106, 0.5);
  --color-gold-a30: rgba(216, 180, 106, 0.3);
  --color-gold-a15: rgba(216, 180, 106, 0.15);
  --color-gold-a08: rgba(216, 180, 106, 0.08);
  --color-cobalt-a40: rgba(111, 180, 255, 0.4);
  --color-cobalt-a15: rgba(111, 180, 255, 0.15);
  --color-orange-a40: rgba(245, 138, 42, 0.4);
  --color-abyss-a92: rgba(5, 14, 36, 0.92);
  --color-shade-a50: rgba(0, 0, 0, 0.5);
  --color-glint: rgba(255, 244, 214, 0.75);

  /* Gradients */
  --gradient-gold: linear-gradient(180deg, #F6E2AE 0%, #E3C27E 42%, #A57C35 50%, #D8B46A 62%, #F6E2AE 100%);
  --gradient-gold-line: linear-gradient(90deg, rgba(216, 180, 106, 0) 0%, #D8B46A 50%, rgba(216, 180, 106, 0) 100%);
  --gradient-orange: linear-gradient(180deg, #FFB066 0%, #F58A2A 100%);
  --gradient-hero: radial-gradient(120% 70% at 50% 0%, #1A3470 0%, #0A1B3F 45%, #050E24 100%);
  --gradient-beam: linear-gradient(180deg, rgba(111, 180, 255, 0.28) 0%, rgba(111, 180, 255, 0.08) 55%, rgba(111, 180, 255, 0) 100%);
  --gradient-sweep: linear-gradient(105deg, rgba(255, 244, 214, 0) 38%, rgba(255, 244, 214, 0.75) 50%, rgba(255, 244, 214, 0) 62%);
  --gradient-panel: linear-gradient(180deg, #10275A 0%, #0A1B3F 100%);

  /* Typography — Font Families（同屏中文 ≤3 种：书法 1 + 粗宋 1 + 黑体 1） */
  --font-brush: 'Ma Shan Zheng', 'STKaiti', 'KaiTi', 'Kaiti SC', serif;
  --font-title: 'Noto Serif SC', 'Songti SC', 'STSong', 'SimSun', serif;
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-latin: 'Cinzel', 'Trajan Pro', 'Times New Roman', serif;
  --font-num: 'Oswald', 'DIN Condensed', 'Bahnschrift', 'PingFang SC', sans-serif;

  /* Typography — Scale（手机起步，clamp 放大） */
  --text-hero: clamp(46px, 4.4vw + 28px, 88px);
  --text-brush: clamp(62px, 6vw + 38px, 128px);
  --text-display: clamp(34px, 2.6vw + 24px, 60px);
  --text-heading: clamp(26px, 1.2vw + 20px, 36px);
  --text-title: clamp(22px, 0.5vw + 20px, 28px);
  --text-lead: clamp(20px, 0.4vw + 18.5px, 24px);
  --text-body: clamp(18px, 0.15vw + 17.5px, 19px);
  --text-small: 16px;
  --text-label: 14px;

  /* Line Height & Tracking */
  --leading-tight: 1.15;
  --leading-heading: 1.3;
  --leading-body: 1.8;
  --tracking-title: 0.04em;
  --tracking-wide: 0.3em;
  --tracking-label: 0.18em;

  /* Spacing (4px base) */
  --spacing: 4px;
  --gutter: clamp(16px, 4vw, 48px);
  --container: 1200px;
  --section-gap: 48px; /* 手机收紧防空屏；≥700px 为 clamp(88px, 9vw, 150px) */
  --header-h: 64px;

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 10px;
  --radius-lg: 18px;
  --radius-window: 28px;
  --radius-full: 999px;

  /* Lines */
  --hairline: 1px;
  --rule: 2px;

  /* Glow & Shadows（外发光克制：只给鎏金细线与主按钮） */
  --glow-gold: 0 0 0 1px rgba(216, 180, 106, 0.45), 0 0 22px rgba(216, 180, 106, 0.16);
  --glow-cobalt: 0 0 0 1px rgba(111, 180, 255, 0.35), 0 0 26px rgba(111, 180, 255, 0.14);
  --glow-orange: 0 0 0 1px rgba(255, 176, 102, 0.6), 0 8px 28px rgba(245, 138, 42, 0.35);
  --shadow-deep: 0 24px 60px rgba(0, 0, 0, 0.45);
  --shadow-text: 0 2px 0 rgba(0, 0, 0, 0.35);

  /* Motion */
  --ease-rise: cubic-bezier(0.22, 1, 0.36, 1);
  --dur-fast: 160ms;
  --dur-base: 280ms;

  /* 半人马登场（钉住段：lead 放大 + hold 扫光，合计 ≤ 82svh；手机 hold 缩到 64px 防空屏，≥700px 回到 min(36svh, 300px)） */
  --pin-top: 76px;
  --zoom-lead: min(46svh, 400px);
  --zoom-hold: min(8svh, 64px);
  --glint-lead: min(16svh, 140px);
  --zoom-from: 0.55;
}
```

### Tailwind v4

```css
@theme {
  /* Colors — 深海藏青底 */
  --color-abyss: #050E24;
  --color-navy: #0A1B3F;
  --color-navy-raised: #10275A;
  --color-navy-high: #1A3470;
  --color-navy-line: #274A8C;
  --color-cobalt: #2F6FE0;
  --color-cobalt-glow: #6FB4FF;
  --color-cobalt-ink: #A6D1FF;

  /* Colors — 鎏金 */
  --color-gold: #D8B46A;
  --color-gold-light: #F6E2AE;
  --color-gold-deep: #A57C35;

  /* Colors — logo 橘橙（点睛） */
  --color-orange: #F58A2A;
  --color-orange-light: #FFB066;
  --color-orange-deep: #D9650F;

  /* Colors — 文字 */
  --color-ink: #F5F1E6;
  --color-ink-muted: #C4CEE2;
  --color-ink-disabled: #AEB8CF;
  --color-on-orange: #050E24;
  --color-focus: #FFD27A;

  /* Colors — 半透明（光效与细线） */
  --color-gold-a50: rgba(216, 180, 106, 0.5);
  --color-gold-a30: rgba(216, 180, 106, 0.3);
  --color-gold-a15: rgba(216, 180, 106, 0.15);
  --color-gold-a08: rgba(216, 180, 106, 0.08);
  --color-cobalt-a40: rgba(111, 180, 255, 0.4);
  --color-cobalt-a15: rgba(111, 180, 255, 0.15);
  --color-orange-a40: rgba(245, 138, 42, 0.4);
  --color-abyss-a92: rgba(5, 14, 36, 0.92);
  --color-shade-a50: rgba(0, 0, 0, 0.5);
  --color-glint: rgba(255, 244, 214, 0.75);

  /* Gradients */
  --gradient-gold: linear-gradient(180deg, #F6E2AE 0%, #E3C27E 42%, #A57C35 50%, #D8B46A 62%, #F6E2AE 100%);
  --gradient-gold-line: linear-gradient(90deg, rgba(216, 180, 106, 0) 0%, #D8B46A 50%, rgba(216, 180, 106, 0) 100%);
  --gradient-orange: linear-gradient(180deg, #FFB066 0%, #F58A2A 100%);
  --gradient-hero: radial-gradient(120% 70% at 50% 0%, #1A3470 0%, #0A1B3F 45%, #050E24 100%);
  --gradient-beam: linear-gradient(180deg, rgba(111, 180, 255, 0.28) 0%, rgba(111, 180, 255, 0.08) 55%, rgba(111, 180, 255, 0) 100%);
  --gradient-sweep: linear-gradient(105deg, rgba(255, 244, 214, 0) 38%, rgba(255, 244, 214, 0.75) 50%, rgba(255, 244, 214, 0) 62%);
  --gradient-panel: linear-gradient(180deg, #10275A 0%, #0A1B3F 100%);

  /* Typography — Font Families（同屏中文 ≤3 种：书法 1 + 粗宋 1 + 黑体 1） */
  --font-brush: 'Ma Shan Zheng', 'STKaiti', 'KaiTi', 'Kaiti SC', serif;
  --font-title: 'Noto Serif SC', 'Songti SC', 'STSong', 'SimSun', serif;
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-latin: 'Cinzel', 'Trajan Pro', 'Times New Roman', serif;
  --font-num: 'Oswald', 'DIN Condensed', 'Bahnschrift', 'PingFang SC', sans-serif;

  /* Typography — Scale（手机起步，clamp 放大） */
  --text-hero: clamp(46px, 4.4vw + 28px, 88px);
  --text-brush: clamp(62px, 6vw + 38px, 128px);
  --text-display: clamp(34px, 2.6vw + 24px, 60px);
  --text-heading: clamp(26px, 1.2vw + 20px, 36px);
  --text-title: clamp(22px, 0.5vw + 20px, 28px);
  --text-lead: clamp(20px, 0.4vw + 18.5px, 24px);
  --text-body: clamp(18px, 0.15vw + 17.5px, 19px);
  --text-small: 16px;
  --text-label: 14px;

  /* Line Height & Tracking */
  --leading-tight: 1.15;
  --leading-heading: 1.3;
  --leading-body: 1.8;
  --tracking-title: 0.04em;
  --tracking-wide: 0.3em;
  --tracking-label: 0.18em;

  /* Spacing (4px base) */
  --spacing: 4px;
  --gutter: clamp(16px, 4vw, 48px);
  --container: 1200px;
  --section-gap: 48px; /* 手机收紧防空屏；≥700px 为 clamp(88px, 9vw, 150px) */
  --header-h: 64px;

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 10px;
  --radius-lg: 18px;
  --radius-window: 28px;
  --radius-full: 999px;

  /* Lines */
  --hairline: 1px;
  --rule: 2px;

  /* Glow & Shadows（外发光克制：只给鎏金细线与主按钮） */
  --glow-gold: 0 0 0 1px rgba(216, 180, 106, 0.45), 0 0 22px rgba(216, 180, 106, 0.16);
  --glow-cobalt: 0 0 0 1px rgba(111, 180, 255, 0.35), 0 0 26px rgba(111, 180, 255, 0.14);
  --glow-orange: 0 0 0 1px rgba(255, 176, 102, 0.6), 0 8px 28px rgba(245, 138, 42, 0.35);
  --shadow-deep: 0 24px 60px rgba(0, 0, 0, 0.45);
  --shadow-text: 0 2px 0 rgba(0, 0, 0, 0.35);

  /* Motion */
  --ease-rise: cubic-bezier(0.22, 1, 0.36, 1);
  --dur-fast: 160ms;
  --dur-base: 280ms;

  /* 半人马登场（钉住段：lead 放大 + hold 扫光，合计 ≤ 82svh；手机 hold 缩到 64px 防空屏，≥700px 回到 min(36svh, 300px)） */
  --pin-top: 76px;
  --zoom-lead: min(46svh, 400px);
  --zoom-hold: min(8svh, 64px);
  --glint-lead: min(16svh, 140px);
  --zoom-from: 0.55;
}
```
