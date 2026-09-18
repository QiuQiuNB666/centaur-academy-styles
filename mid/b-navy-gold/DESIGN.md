# 半人马AI学院 · 藏青金章 — Style Reference

> 藏青底上一圈细金环，首屏端正、正文像一本商学院年报

**Theme:** dark

藏青金章是第五轮「取中间值」的深色一版，从第四轮「国潮科技」往第三轮「刊本」挪了一大步。颜色只有四个角色：藏青底色系（#050E24 → #0A1B3F → #10275A）、一种金 #D8B46A、logo 马身橘橙 #F58A2A、象牙白文字 #F5F1E6——老板熟悉的「深蓝配金」没变，但金只做 1px 细线、章节编号和标题里的强调词，并且一律平涂；全站只有 H1 的「你的能力」一个词用极轻的两段金渐变。橘橙只给「联系学院顾问」主按钮，不发光、不渐变。书法字、云纹、回纹、山脊线、扇面、卷轴、印章、题跋框、光束、粒子、背景网格全部拿掉，分量改由字来扛：所有标题、编号、产品名都用 Noto Serif SC 900 粗宋，正文 Noto Sans SC，同屏中文只有这两种。版式是「首屏居中、正文左对齐」：首屏像典礼一样端正，从第一章起换成刊本的节奏——左栏大号金色编号 + 章名，中栏标题与正文，右栏细金线画框里的插画，章节之间只有一根 1px 金线。签名记忆点是**半人马在细金环里登场**：滚动时半人马从 0.55/0.6 倍放大到终态，外圈同心圆刻度由暗转亮，钉住的一小段里一道暖金扫光掠过马身——这是全站唯一的光效。

## Tokens — Colors

| Name       | Value     | Token                  | Role                                                    |
| ---------- | --------- | ---------------------- | ------------------------------------------------------- |
| 深海藏青   | `#050E24` | `--color-abyss`        | 页面底色，比纯黑多一层蓝                                |
| 藏青       | `#0A1B3F` | `--color-navy`         | 共学五步、联系区块底、画框衬底、首屏渐变顶              |
| 抬升藏青   | `#10275A` | `--color-navy-raised`  | 预留给浮层；首页不用大面积                              |
| 高位藏青   | `#1A3470` | `--color-navy-high`    | 禁用按钮底                                              |
| 藏青细线   | `#274A8C` | `--color-navy-line`    | 输入框、禁用按钮描边                                    |
| 金         | `#D8B46A` | `--color-gold`         | 1px 分隔线、章节/步骤编号、标题强调词（≥28px）、金环   |
| 浅金       | `#F6E2AE` | `--color-gold-light`   | 链接与卡片标题 hover                                    |
| 暗金       | `#A57C35` | `--color-gold-deep`    | 预留；不在首页出现                                      |
| 马身橘橙   | `#F58A2A` | `--color-orange`       | 只给主按钮，全页 ≤3 处                                  |
| 亮橘       | `#FFA553` | `--color-orange-light` | 主按钮 hover                                            |
| 象牙白     | `#F5F1E6` | `--color-ink`          | 正文与标题（对深海 17:1）                               |
| 月灰       | `#C4CEE2` | `--color-ink-muted`    | 次要文字、英文眉标（对深海 12:1，对藏青 10.7:1）        |
| 禁用灰     | `#C0C9DB` | `--color-ink-disabled` | 禁用按钮文字、占位符（对高位藏青 7.1:1）               |
| 按钮深字   | `#050E24` | `--color-on-orange`    | 橘橙按钮上的字（7.8:1）                                 |
| 焦点金     | `#FFD27A` | `--color-focus`        | 键盘焦点环 3px                                          |

### 柔和语义色（深底版：金的四档透明度，只用于线）

| Name   | Background              | Text / Line | Token              |
| ------ | ----------------------- | ----------- | ------------------ |
| 金·强  | `rgba(216,180,106,.5)`  | `#D8B46A`   | `--color-gold-a50` |
| 金·中  | `rgba(216,180,106,.3)`  | `#D8B46A`   | `--color-gold-a30` |
| 金·弱  | `rgba(216,180,106,.15)` | `#F5F1E6`   | `--color-gold-a15` |
| 金·底  | `rgba(216,180,106,.08)` | `#F5F1E6`   | `--color-gold-a08` |

金·强分章节与区块；金·中分列表行、步骤列、卡片封面框；金·弱只给页脚内线、同心圆刻度外圈；金·底只做次按钮 hover 底。

### 渐变（全站只有三条）

| Name   | Token              | Role                                                          |
| ------ | ------------------ | ------------------------------------------------------------- |
| 淡金   | `--gradient-gold`  | 两段极轻金渐变，只给 H1「你的能力」一个词                     |
| 首屏   | `--gradient-hero`  | 藏青到深海的纵向过渡，不做顶光、不做光晕                      |
| 扫光   | `--gradient-sweep` | 登场时掠过马身的暖金光带（以抠图作遮罩），全站唯一光效        |

## Tokens — Typography

### Noto Serif SC — 标题 / 编号 / 产品名 · `--font-title`

- **Substitute:** Songti SC, STSong, SimSun, serif；正式上线可换思源宋体 Heavy 自托管子集
- **Weights:** 900（标题、编号），700（预留）
- **Sizes:** 22–28px（小标题）、24–28px（底栏）、34–58px（章节标题）、44–64px（编号）、56–92px（H1）
- **Line height:** H1 1.18 / 标题 1.3 / 引文 1.55
- **Letter spacing:** H1 0.02em / 标题 0.04em / 小标题与底栏 0.06–0.12em
- **Role:** 分量感全部靠它；数字编号也用它的衬线数字，不另起数字字体

### Noto Sans SC — 正文 / 导航 / 按钮 · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif
- **Weights:** 400（正文）、500（导语、链接）、700（按钮、章名）
- **Sizes:** 16px（次要）、18–19px（正文）、20–24px（导语）
- **Line height:** 正文 1.8 / 导语 1.7
- **Role:** 所有要读的句子；老花眼友好，手机正文不小于 18px

### Cinzel — 英文眉标 · `--font-latin`

- **Substitute:** Trajan Pro, Times New Roman, serif
- **Weights:** 700
- **Sizes:** 13–14px，字距 0.18em，全大写
- **Role:** CENTAUR AI ACADEMY、HUMAN × AI、图注英文词；只做点缀，不承载关键信息，颜色用月灰不用金

### Type Scale

| Role     | Size      | Line Height | Letter Spacing | Token            |
| -------- | --------- | ----------- | -------------- | ---------------- |
| hero     | 56–92px   | 1.18        | 0.02em         | `--text-hero`    |
| num      | 44–64px   | 1           | 0              | `--text-num`     |
| display  | 34–58px   | 1.3         | 0.04em         | `--text-display` |
| title    | 22–28px   | 1.3–1.45    | 0.06em         | `--text-title`   |
| lead     | 20–24px   | 1.7         | 0              | `--text-lead`    |
| body     | 18–19px   | 1.8         | 0              | `--text-body`    |
| small    | 16px      | 1.6         | 0.08em         | `--text-small`   |
| label    | 14px      | 1.3         | 0.18em         | `--text-label`   |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 4px`）

**Density:** 宽松，但任一滚动位置视口内纵向空带 ≤ 160px

### Spacing Scale

| Name        | Value                                    | Token           |
| ----------- | ---------------------------------------- | --------------- |
| gutter      | 16–48px                                  | `--gutter`      |
| section     | 56px（手机）/ 72–96px（≥700px）          | `--section-gap` |
| container   | 1200px                                   | `--container`   |
| header      | 64px / 78px（≥1024px）                   | `--header-h`    |
| 章节栏距    | 48px（左栏 180px + 两等分栏）            | —               |

### Border Radius

| Name | Value | Token           |
| ---- | ----- | --------------- |
| sm   | 2px   | `--radius-sm`   |
| md   | 6px   | `--radius-md`   |
| full | 999px | `--radius-full` |

| Element  | Value                 |
| -------- | --------------------- |
| 按钮     | 6px (md)              |
| 画框     | 0（直角细线）         |
| 徽标     | 2px (sm)              |
| 输入框   | 2px (sm)              |
| 联系横幅 | 0                     |

### Shadows

| Name   | Value                            | Token             |
| ------ | -------------------------------- | ----------------- |
| figure | `0 18px 30px rgba(0,0,0,0.5)`    | `--shadow-figure` |

全站只有半人马脚下这一处投影（手机浮钮另加一层 shade-a50 防止压字）。卡片、按钮、画框都不投影、不外发光。

### Motion

| Name        | Value                           | Token            |
| ----------- | ------------------------------- | ---------------- |
| ease-rise   | `cubic-bezier(0.22, 1, 0.36, 1)` | `--ease-rise`    |
| fast / base | 160ms / 280ms                   | `--dur-fast` / `--dur-base` |
| 登场放大    | 起点 0.55（手机/平板）/ 0.6（桌面）→ 1 | `--zoom-from` |
| 放大段      | min(46svh, 400px)               | `--zoom-lead`    |
| 钉住段      | 手机 min(8svh, 64px) / ≥700px min(36svh, 300px) | `--zoom-hold` |
| 钉线        | 手机 76px / 平板 clamp(76px, 50svh − 320px, 200px) / 桌面 clamp(96px, 50svh − 290px, 160px) | `--pin-top` |

### Layout

- **Section gap:** 手机 56px，≥700px 72–96px；共学五步区块上下各取一半
- **Card padding:** 画框内衬 10px，期刊卡封面内衬 6px
- **Element gap:** 14–24px
- **Max content width:** 1200px

## Components

### Primary Button

**Role:** 唯一主 CTA「联系学院顾问 ↗」
`bg-orange`(#F58A2A) `text-on-orange`(#050E24)，圆角 6px，高 56px（顶栏 52px），`font: 19px/700`，字距 0.04em。hover 换 `orange-light`(#FFA553)；active scale(0.98)。不渐变、不外发光。手机端顶栏按钮挪成右下浮钮，首屏按钮可见时隐藏。

### Secondary Button

**Role:** 「复制客服链接」
透明底 + 1px 金内描边，象牙白字；hover 金·底 + 浅金描边。

### Disabled Button

**Role:** 「下载知君 ↓」「下载万象 ↓」
`bg-navy-high` + 1px `navy-line` 描边 + 禁用灰字，高 52px，旁边 16px 月灰注「下载暂未开放」。

### Text Link

**Role:** 「了解学院的主张 ↗」等
象牙白 500，下方 1px 金线（离基线 8px）；hover 字变浅金、线加粗到 2px。

### Chapter Mark

**Role:** 三章节的编号与章名（签名节奏）
粗宋 900 金色编号 44–64px + 章名 Noto Sans 700；桌面在 180px 左栏里上下排，手机横排。上方一根贯穿整章的 1px 金·强线。

### Framed Illustration

**Role:** 章节插画框
1px 金·强细线 + 10px 藏青衬底 + 4:3 裁切插画，直角。下方图注左对齐：Cinzel 英文词 + 「｜ 中文」月灰。暖色纸感插画靠这圈藏青衬边和金线「装裱」，不做扇面、圆窗、卷轴。

### Product Row

**Role:** 知君 / 万象
上下 1px 金·中线夹一行：粗宋 26px 产品名 + 一句定位链接；下一行禁用下载按钮 + 说明。

### Step Column

**Role:** 共学五步
桌面五等分列，顶上一根金·强线，列之间 1px 金·中竖线；每列粗宋金色编号 48px + 粗宋小标题 + 月灰说明。手机改成横排行，行间 1px 金·中线。

### Journal Card

**Role:** 观点与动态
无底色面板；顶上 1px 金·强线，封面 6px 内衬 + 1px 金·中框。桌面左大右二，右侧两张为 180px 方图横排。「观点」徽标 1px 金·强内描边，2px 圆角。

### Quote Block

**Role:** 院长寄语
粗宋 900 28–44px 横排引文，引号平涂金；右栏月灰正文 + 1px 金·中线下的署名（粗宋 28px）+ 链接。无题跋框、无印章。

### Contact Banner

**Role:** 联系
藏青底 + 1px 金·强直角边框，左对齐标题与按钮；桌面右侧三圈金·弱同心圆，呼应半人马金环。

## Surfaces

| Level | Name   | Value     | Purpose                              |
| ----- | ------ | --------- | ------------------------------------ |
| 0     | abyss  | `#050E24` | 页面底                               |
| 1     | navy   | `#0A1B3F` | 共学五步、联系横幅、画框衬底         |
| 2     | raised | `#10275A` | 预留浮层                             |
| 3     | high   | `#1A3470` | 禁用按钮                             |

## Do's and Don'ts

### Do

- 金只有两种用法：1px 线，和 ≥28px 的平涂字（编号、强调词、口号）。
- 金属渐变全站只出现一次：H1「你的能力」。
- 橘橙只给主按钮，同屏最多两个（手机浮钮在首屏按钮可见时隐藏）。
- 首屏居中，其余一律左对齐；章节靠「编号 + 1px 金线 + 左栏」建立节奏。
- 所有标题用 Noto Serif SC 900；正文不小于 18px，行高 1.8。
- 插画统一用细金线画框，一个框型用到底。
- 半人马的扫光是唯一光效；背景只留金环外那圈极淡的同心圆刻度。

### Don't

- 不用书法字（马善政等）、云纹、回纹、山脊线、扇面、卷轴、印章、题跋框、对联式排版。
- 不用光束、粒子、发光线条、外发光阴影、背景网格。
- 不用纯黑底、撕纸边、橄榄奶油纸页、整屏拉丁大字当主视觉、满屏等宽小标签。
- 不把金用在正文或 16px 以下的字上。
- 不给卡片加面板底色和投影——面板感来自线，不来自块。
- 不编造数字、客户、评价、期号。

## Imagery

主视觉只有一个物件：透明底半人马，放在一圈 1px 金环 + 一圈金·中短刻度 + 一圈金·弱外环里，像奖章或表盘的刻度，不是神坛。三张暖色纸感插画不去色、不叠印，靠藏青衬边与细金线装裱成「挂在深色墙上的画」。期刊卡的「AI 越强大」一篇用米色底的 academy-centaur-hero，同样进 6px 衬框。无图标库、无 emoji。

## Layout

1200px 容器，4px 基准。首屏居中：Cinzel 眉标 → 两行 H1 → 导语 → 说明 → 主按钮 + 文字链 → 半人马舞台（桌面终态 720px 宽，平板 ≤700px，手机 ≤440px）；底栏「人决定方向，AI 拓展人的能力。」三档都是横排粗宋象牙白，上方一根金·强细线，不做竖排（竖排金字读起来像对联题跋，属于「太土」一端）。首屏以下切到左对齐三栏：180px 编号栏 | 正文栏 | 画框栏（1fr 1fr），共学五步的标题也对齐到这两栏。观点与动态左大右二；院长寄语 7:5 两栏；联系横幅通栏；页脚一根金·强线 + 院名 + 右侧口号，再一根金·弱线下放链接。

## Agent Prompt Guide

Quick Color Reference:

```
background: #050E24
section: #0A1B3F
foreground: #F5F1E6
muted: #C4CEE2
gold (lines, numbers, ≥28px accents, flat): #D8B46A
primary button only: #F58A2A on #050E24
focus: #FFD27A
```

Example Component Prompts:

1. Create a chapter row: top 1px `rgba(216,180,106,.5)` rule; grid `180px 1fr 1fr` gap 48px; left: number "01" Noto Serif SC 900 64px #D8B46A above chapter name Noto Sans SC 700 20px; middle: H2 Noto Serif SC 900 58px with one flat-gold keyword, lead 20px #C4CEE2, link with 1px gold underline; right: 4:3 illustration inside 10px #0A1B3F mat and 1px gold-a50 border, caption Cinzel 14px + Chinese 16px #C4CEE2.
2. Create the hero: centered; eyebrow Cinzel 14px 0.18em; H1 two lines Noto Serif SC 900 92px, second line keyword with `linear-gradient(180deg,#EBD196,#D8B46A)` text fill; primary button flat #F58A2A 56px tall 6px radius; below, a transparent centaur inside a 1px gold ring and a faint tick ring, scaling from 0.6 to 1 on scroll with one warm sweep.
3. Create a five-step row: 5 equal columns, top 1px gold-a50 rule, 1px gold-a30 vertical dividers; each: "01" Noto Serif SC 900 48px gold, title 28px serif 900, one line 18px #C4CEE2.

## Similar Brands

- **第三轮「刊本」（styles-repo/edition/final，照 Shopify Editions / AI in Design Report 做）** — 借章节节奏：左栏编号、贯穿全宽的 1px 分隔线、插画进直角画框、图注「英文词 ｜ 中文」。不借它的纯黑底、橘橙满屏和等宽小字。
- **第四轮「国潮科技」（styles-repo/tu/guochao-tech）** — 本版起点。保留深海藏青 + 金 + 橘橙按钮、首屏居中端正、半人马金环登场、手机固定咨询按钮、老花眼字号；删掉书法、纹样、光束粒子、题跋与印章。
- **中欧国际工商学院 CEIBS（tu-study/edu-brands 调研）** — 借「金色细线」的线描与装裱感，落到画框、产品行、步骤列的 1px 金线；不借红底。
- **长江商学院 CKGSB（tu-study/edu-brands 调研）** — 借「深蓝 + 金」的商学院配色关系；反面教材是它的细弱灰标题，所以本版标题一律粗宋 900。
- **帆书 / 得到（tu-study/edu-brands 调研）** — 借「大标题 + 一行灰色副标题」的区块头与克制的主按钮用色；不借角标与评分。

## 新增的结构性文字

以下文字不在 content.md 中，只用于导航、状态、区块标签和组件样张，不含任何事实性说法：

- 「菜单」「关闭」（手机顶栏菜单按钮）
- 「跳到正文」（键盘跳转链接）
- 「已复制」（复制客服链接后的状态提示）
- 「LEARNING TOGETHER」（共学五步区块的英文眉标）
- H2「每一次共学，都向前一点」：由 content.md 共学五步的眉标升级为区块标题，文字不变
- 章名「从你的积累出发」「与同行者一起」「让想法落地」与编号 01/02/03 来自 content.md 章节标题，只改排版位置
- kit.html 内的说明文字（区块字母 A–G、色板名与角色、字号标注、状态名 default/hover/active/focus/disabled、「只在样张展示，首页不放表单。」「例：每周的销售复盘」占位、「细金线画框 · 章节插画」等图注、金线三档说明、「藏青金章 · 组件样张」标题与说明句、「CENTAUR AI ACADEMY · NAVY & GOLD」眉标），只出现在组件样张，不进入首页

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 藏青底（底色系） */
  --color-abyss: #050E24;
  --color-navy: #0A1B3F;
  --color-navy-raised: #10275A;
  --color-navy-high: #1A3470;
  --color-navy-line: #274A8C;

  /* Colors — 金（唯一金属点缀） */
  --color-gold: #D8B46A;
  --color-gold-light: #F6E2AE;
  --color-gold-deep: #A57C35;

  /* Colors — logo 橘橙（只给主按钮） */
  --color-orange: #F58A2A;
  --color-orange-light: #FFA553;

  /* Colors — 文字 */
  --color-ink: #F5F1E6;
  --color-ink-muted: #C4CEE2;
  --color-ink-disabled: #C0C9DB;
  --color-on-orange: #050E24;
  --color-focus: #FFD27A;

  /* Colors — 半透明（细线与遮罩） */
  --color-gold-a50: rgba(216, 180, 106, 0.5);
  --color-gold-a30: rgba(216, 180, 106, 0.3);
  --color-gold-a15: rgba(216, 180, 106, 0.15);
  --color-gold-a08: rgba(216, 180, 106, 0.08);
  --color-abyss-a92: rgba(5, 14, 36, 0.92);
  --color-shade-a50: rgba(0, 0, 0, 0.5);

  /* Gradients（金属渐变只给 H1 关键词；扫光只给半人马登场） */
  --gradient-gold: linear-gradient(180deg, #EBD196 0%, #D8B46A 100%);
  --gradient-hero: linear-gradient(180deg, #0A1B3F 0%, #050E24 100%);
  --gradient-sweep: linear-gradient(105deg, rgba(255, 244, 214, 0) 40%, rgba(255, 244, 214, 0.6) 50%, rgba(255, 244, 214, 0) 60%);

  /* Typography — Font Families（同屏中文 2 种：粗宋 + 黑体） */
  --font-title: 'Noto Serif SC', 'Songti SC', 'STSong', 'SimSun', serif;
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-latin: 'Cinzel', 'Trajan Pro', 'Times New Roman', serif;

  /* Typography — Scale（手机起步，clamp 放大） */
  --text-hero: clamp(56px, 3.6vw + 44px, 92px);
  --text-display: clamp(34px, 2.4vw + 25px, 58px);
  --text-num: clamp(44px, 1.6vw + 38px, 64px);
  --text-title: clamp(22px, 0.5vw + 20px, 28px);
  --text-lead: clamp(20px, 0.4vw + 18.5px, 24px);
  --text-body: clamp(18px, 0.15vw + 17.5px, 19px);
  --text-small: 16px;
  --text-label: 14px;

  /* Line Height & Tracking */
  --leading-tight: 1.18;
  --leading-heading: 1.3;
  --leading-body: 1.8;
  --tracking-title: 0.04em;
  --tracking-label: 0.18em;

  /* Spacing (4px base) */
  --spacing: 4px;
  --gutter: clamp(16px, 4vw, 48px);
  --container: 1200px;
  --section-gap: 56px; /* 手机收紧防空屏；≥700px 为 clamp(72px, 6vw, 96px) */
  --header-h: 64px;

  /* Border Radius（方正为主） */
  --radius-sm: 2px;
  --radius-md: 6px;
  --radius-full: 999px;

  /* Lines */
  --hairline: 1px;
  --rule: 2px;

  /* Shadows（只给半人马落地影） */
  --shadow-figure: 0 18px 30px rgba(0, 0, 0, 0.5);

  /* Motion */
  --ease-rise: cubic-bezier(0.22, 1, 0.36, 1);
  --dur-fast: 160ms;
  --dur-base: 280ms;

  /* 半人马登场（钉住段：lead 放大 + hold 扫光，合计 ≤ 82svh；手机 hold 64px 防空屏，≥700px 回到 min(36svh, 300px)） */
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
  --color-abyss: #050E24;
  --color-navy: #0A1B3F;
  --color-navy-raised: #10275A;
  --color-navy-high: #1A3470;
  --color-navy-line: #274A8C;
  --color-gold: #D8B46A;
  --color-gold-light: #F6E2AE;
  --color-gold-deep: #A57C35;
  --color-orange: #F58A2A;
  --color-orange-light: #FFA553;
  --color-ink: #F5F1E6;
  --color-ink-muted: #C4CEE2;
  --color-ink-disabled: #C0C9DB;
  --color-on-orange: #050E24;
  --color-focus: #FFD27A;
  --color-gold-a50: rgba(216, 180, 106, 0.5);
  --color-gold-a30: rgba(216, 180, 106, 0.3);
  --color-gold-a15: rgba(216, 180, 106, 0.15);
  --color-gold-a08: rgba(216, 180, 106, 0.08);
  --color-abyss-a92: rgba(5, 14, 36, 0.92);
  --color-shade-a50: rgba(0, 0, 0, 0.5);
  --gradient-gold: linear-gradient(180deg, #EBD196 0%, #D8B46A 100%);
  --gradient-hero: linear-gradient(180deg, #0A1B3F 0%, #050E24 100%);
  --gradient-sweep: linear-gradient(105deg, rgba(255, 244, 214, 0) 40%, rgba(255, 244, 214, 0.6) 50%, rgba(255, 244, 214, 0) 60%);
  --font-title: 'Noto Serif SC', 'Songti SC', 'STSong', 'SimSun', serif;
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-latin: 'Cinzel', 'Trajan Pro', 'Times New Roman', serif;
  --text-hero: clamp(56px, 3.6vw + 44px, 92px);
  --text-display: clamp(34px, 2.4vw + 25px, 58px);
  --text-num: clamp(44px, 1.6vw + 38px, 64px);
  --text-title: clamp(22px, 0.5vw + 20px, 28px);
  --text-lead: clamp(20px, 0.4vw + 18.5px, 24px);
  --text-body: clamp(18px, 0.15vw + 17.5px, 19px);
  --text-small: 16px;
  --text-label: 14px;
  --radius-sm: 2px;
  --radius-md: 6px;
  --radius-full: 999px;
  --shadow-figure: 0 18px 30px rgba(0, 0, 0, 0.5);
  --ease-rise: cubic-bezier(0.22, 1, 0.36, 1);
}
```
