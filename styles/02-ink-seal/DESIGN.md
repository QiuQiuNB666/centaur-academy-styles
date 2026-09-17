# 半人马AI学院 · 墨与印 — Style Reference

> 月白纸上，墨分五色，朱砂只落印

**Theme:** light

「墨与印」把品牌自带的文言气质（知君、万象、嘉木、各有知君共创万象）当作版式来做，而不是当作装饰来贴。画布是偏青的月白（#f2f4f1），不是米色——这一点把它和所有「暖纸 + 衬线 + 陶土橙」的页面分开。中性阶不用灰，用墨：焦 #16181a、浓 #26292c、重 #474c50、淡 #5f6569、清 #a9aeaa，标题的强调不靠换颜色，靠把墨从「重」提到「焦」、再在字下点一排朱砂芝麻点（传统圈点，`text-emphasis: filled sesame`）。朱砂 #b5301f 是全页唯一的彩色，面积 ≤3%，并且只以「印」的形态出现：卷首的长方白文印、署名旁的名章、产品名前的朱文小印、按钮末端的钤印格、压在墨池与地脚接缝上的骑缝章——没有红色按钮，没有红色标题。标题与引文用霞鹭文楷（钢笔楷，不是毛笔字），正文用黑体保证经营者读得舒服，拉丁与数字用 Source Serif 4。版式上，H1 竖排立在卷首右侧（`writing-mode: vertical-rl`，AI 用纵中横），章节名做成书口，五步流程排进乌丝栏，院长的话写在朱丝栏信笺上；圆角 ≤3px，阴影只有装裱用的一层纸影。橙蓝折纸半人马和暖色插画不硬贴：半人马按「器物」处理，抠图直接立在月白上、脚下一根焦墨地线；插画一律「册页式装裱」——宣纸白衬纸、界格细线、竖排题签，饱和度收到 .84。签名记忆点就是这套**印 + 竖排题签 + 装裱框**：任何一屏截下来，都认得出是这一家。

## Tokens — Colors

| Name | Value | Token | Role |
| ---- | ----- | ----- | ---- |
| 月白画布 | `#f2f4f1` | `--color-background` | 主页面背景。偏青的冷白，刻意不用米色 |
| 浓墨前景 | `#26292c` | `--color-foreground` | 正文，对画布 13.2:1 |
| 宣纸白 | `#fbfbf8` | `--color-card` | 衬纸、信笺、乌丝栏底、墨池上的文字 |
| 绫边灰 | `#e8ebe6` | `--color-secondary` / `--color-muted` | 次级底、禁用态按钮 |
| 焦墨 | `#16181a` | `--color-ink-jiao` / `--color-primary` | 着重字、主按钮、粗界线、墨池底 |
| 浓墨 | `#26292c` | `--color-ink-nong` | 正文、院长寄语正文 |
| 重墨 | `#474c50` | `--color-ink-zhong` | 标题的常态字、说明文，7.9:1 |
| 淡墨 | `#5f6569` | `--color-ink-dan` / `--color-muted-foreground` | 次要文字、眉标，对画布 5.35:1、对绫边灰 4.91:1 |
| 清墨 | `#a9aeaa` | `--color-ink-qing` / `--color-input` | 输入底线、墨池上的次要字（7.9:1） |
| 界格线 | `#d5d9d3` | `--color-border` | 栏线、分隔、衬纸边 |
| 画心描线 | `rgba(22,24,26,.12)` | `--color-image-outline` | 装裱框内画心的 1px 内描线 |
| 朱砂（不漂移） | `#b5301f` | `--color-brand` | 只以「印」出现：白文印底、朱文印框、钤印格、圈点，全页 ≤3% |
| 朱砂 · 沉 | `#8f2217` | `--color-brand-deep` / `--color-destructive` | 链接 hover 文字、错误提示，7.9:1 |
| 朱丝栏 | `rgba(181,48,31,.34)` | `--color-brand-rule` | 信笺栏线，只此一处 |
| 竹青成功 | `#35573a` | `--color-success` | 成功状态 |
| 墨池 | `#16181a` | `--color-inverse` | 联系区整块深色底，全页只出现一次 |

### 柔和语义色（浅底 + 深字）

| Name | Background | Text | Token |
| ---- | ---------- | ---- | ----- |
| 朱 | `#f4e3de` | `#8f2217` | `--color-pastel-red-*` |
| 黛 | `#e0e7ed` | `#2b4a63` | `--color-pastel-blue-*` |
| 竹青 | `#e2eae0` | `#35573a` | `--color-pastel-green-*` |
| 缃 | `#f0e9d4` | `#76570f` | `--color-pastel-yellow-*` |

四对均 ≥5.5:1。只用于徽标（文章分类、开放状态），不做区块底色。本站没有图表，不设图表色。

## Tokens — Typography

### 霞鹭文楷 LXGW WenKai — 标题 / 题签 / 引文 / 印文 · `--font-display`

- **Substitute:** Kaiti SC, STKaiti, KaiTi（Windows 楷体）, Songti SC
- **Weights:** 400（常态）、700（着重、印文、文章标题）
- **Sizes:** 13px（题签）, 17px, 22px, 30px, clamp(32–54px), clamp(52–108px)
- **Line height:** 竖排 display 1.16 / 横排标题 1.3 / 信笺 2.2
- **Letter spacing:** display 0.06em / 标题 0.04em / 题签与书口 0.2–0.32em——楷体要松排，紧了就像字帖
- **Role:** 一切「有人在说话」的文字。预览页经 jsDelivr 的 `lxgw-wenkai-webfont`（GB 字形）加载；正式站请自托管子集。不要用 Google Fonts 上的 LXGW WenKai TC：实测「真」等字会出台标字形、逗号句号居中，简体站不能用。栈首放 Source Serif 4，让夹在楷体里的 AI、数字走衬线。

### Noto Sans SC — 正文 / UI · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, system-ui
- **Weights:** 400, 500
- **Sizes:** 12px, 13px, 14px, 15px, 16px, 18px
- **Line height:** 1.9（比常规松，配大留白）
- **Letter spacing:** 0.02em；导航与按钮 0.1–0.14em
- **Role:** 说明文、导航、按钮、表单。受众 35–55 岁，正文不用楷体，保证久读不累。

### Source Serif 4 — 拉丁 / 数字 / 眉标 · `--font-latin`

- **Substitute:** Georgia, Times New Roman
- **Weights:** 400, 600；italic 400
- **Sizes:** 10px（品牌小字）, 11–12px（眉标，全大写，字距 0.22em）, 15–16px（步骤号、章号）
- **OpenType features:** tabular-nums（日期、步骤号）
- **Role:** CENTAUR AI ACADEMY、日期 2026.09.15、01–05。安静的旧式衬线，借自日本设计中心官网的中西文搭配。

### 宋体栈 · `--font-serif` / 等宽 · `--font-mono`

- `--font-serif`（Source Serif 4 + Noto Serif SC / Songti SC）留给文章详情页长文；首页不用。
- `--font-mono`（ui-monospace 系统栈）只在样张页标 hex 与 token 名，站内不出现。

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| ---- | ---- | ----------- | -------------- | ----- |
| display（竖排 H1） | clamp(52px, 7.2vw, 108px) | 1.16 | 0.06em | `--text-display` |
| heading-lg（章节 H2） | clamp(32px, 3.7vw, 54px) | 1.3 | 0.04em | `--text-heading-lg` |
| heading | 30px | 1.3 | 0.04em | `--text-heading` |
| subheading | 22px | 1.4 | 0.04em | `--text-subheading` |
| body-lg | 18px | 1.9 | 0.02em | `--text-body-lg` |
| body | 16px | 1.9 | 0.02em | `--text-body` |
| body-sm | 14px | 1.8 | 0.02em | `--text-body-sm` |
| caption / label | 12px | 1.6 | 0.22em（拉丁大写） | `--text-caption` |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 0.25rem`）

**Density:** 疏。留白是这套范式的主材料，不是剩下来的地方。

### Spacing Scale

| Name | Value | Token |
| ---- | ----- | ----- |
| 1 | 4px | `--spacing-1` |
| 2 | 8px | `--spacing-2` |
| 3 | 12px | `--spacing-3` |
| 4 | 16px | `--spacing-4` |
| 6 | 24px | `--spacing-6` |
| 8 | 32px | `--spacing-8` |
| 12 | 48px | `--spacing-12` |
| 16 | 64px | `--spacing-16` |
| 24 | 96px | `--spacing-24` |
| 40 | 160px | `--spacing-40` |
| 56 | 192px | `--spacing-56` |

### Border Radius

| Name | Value | Token |
| ---- | ----- | ----- |
| none | 0 | `--radius-none` |
| sm | 2px | `--radius-sm` |
| md | 3px | `--radius-md` |

| Element | Value |
| ------- | ----- |
| 装裱框、信笺、乌丝栏 | 0 |
| 按钮、印、徽标 | 2px (sm) |
| 钤印格（按钮内） | 1px |
| 输入框 | 0（只有底线） |

纸和印都是直角。任何 ≥4px 的圆角都会把这套东西拉回「App 卡片」。

### Shadows

| Name | Value | Token |
| ---- | ----- | ----- |
| none | `none` | `--shadow-none` |
| mount | `0 1px 0 rgba(22,24,26,.05), 0 24px 48px -36px rgba(22,24,26,.28)` | `--shadow-mount` |

全站只有一种阴影：装裱框与信笺底下那层贴着桌面的纸影（大负扩散，只在底边露一点）。按钮、徽标、导航一律无阴影。

### Motion

| Name | Value | Token |
| ---- | ----- | ----- |
| ease-ink | `cubic-bezier(0.16, 1, 0.3, 1)` | `--ease-ink` |
| duration-fast | `0.3s` | `--duration-fast` |
| duration-slow | `1s` | `--duration-slow` |

只动 transform / opacity / 颜色。hover 是「墨色转淡 + 印格下压 scale(.9)」；装裱框内的插画用 `animation-timeline: view()` 从 scale 1.07 落到 1（包在 `@supports` 里，终态即默认态）。`prefers-reduced-motion` 下全部关掉。

### Layout

- **Section gap:** 160–192px（移动端 96px）
- **Mount padding:** 天头 44px / 左右 20–32px / 地脚 32px（天头永远大于地脚）
- **Element gap:** 32px 栏距
- **Max content width:** 1320px，12 栏；页边 clamp(20px, 5vw, 72px)

## Components

### Primary Button（钤印按钮）

**Role:** 主 CTA（联系学院顾问）
`bg-primary`(#16181a) `text-primary-foreground`(#fbfbf8)，`border-radius: 2px`，`min-height: 48px`，文字 `15px/500`、字距 0.1em、左右 22px；末端嵌一格 36px 宽的朱砂 `chop`（#b5301f，四周留 5px 墨边），里面放 ↗。hover：底色转重墨 #474c50，印格 `scale(.9)`；active：整体 `scale(.98)`，印格转沉朱；focus-visible：2px 焦墨描边、offset 3px。墨池上反相：宣纸白底 + 焦墨字，印格不变。朱砂永远不铺满按钮。

### Outline Button

**Role:** 次级动作（复制客服链接）
透明底 + 1px 焦墨边，hover 反相为墨底白字。墨池上用 20% 宣纸白描边。

### Disabled Button

**Role:** 暂未开放的下载
`bg-muted`(#e8ebe6) + 淡墨字 + 界格线边，`cursor: not-allowed`，不带印格。旁边必须配一句说明（「下载暂未开放」）。

### Text Link

**Role:** 行内去向
焦墨字 + 1px 焦墨下划线（background 画，离基线 9px）+ 箭头；hover 文字转沉朱、下划线转朱砂、箭头位移 2px。触控高度 44px。

### Seal（印）

**Role:** 签名记忆点，朱砂的唯一载体
`writing-mode: vertical-rl`，霞鹭文楷 700，行高 1.12，直角 2px，平涂，无做旧、无破边。三种：**白文印**（朱砂底宣纸白字：卷首 8 字长方印「各有知君共创万象」、名章「嘉木」、骑缝章「共学共创」）；**朱文印**（2px 朱砂框 + 朱砂字：产品名「知君」「万象」）；**钤印格**（按钮内）。印文只取文案里已有的词，不另造。一屏之内最多一方白文印。

### Mount（章节插画框 · 册页式装裱）

**Role:** 让暖色插画进入墨色体系
`bg-card`(#fbfbf8) + 1px 界格线 + `--shadow-mount`，padding `44px 32px 32px 20px`；两列网格：左列竖排**题签**（13px 文楷，字距 0.2em，1px 线框，英文部分顺排成书脊），右列画心（1px 12% 焦墨内描线，`filter: saturate(.84) contrast(.98)`）。三种开本：横披 4:3、斗方 1:1、手卷 3:2——同一页里不重复。≤1180px 题签改横排落在画心下方。

### Plinth（器物式 · 只给半人马）

**Role:** 卷首主视觉
透明底抠图直接立在月白上，`saturate(.92)`，脚下一根 1px 焦墨地线向右出血 32px，左侧立一枚竖排题签。橙蓝是全页唯一的高饱和，所以四周必须空。

### Spine（书口 · 章节标）

**Role:** 01 / 02 / 03 章节名
竖排 15px 文楷、字距 0.32em，贴一根贯穿整章高度的 1px 焦墨线；章号用 Source Serif 4 纵中横。奇数章在左、偶数章在右。

### Steps（乌丝栏 · 共学五步）

**Role:** 真实顺序流程
宣纸白通栏，上下各一根焦墨线；五栏以界格线分开，每栏：左上步骤号（Source Serif 4 tabular）、右侧竖排步骤名（34px 文楷）、栏底一句横排说明。移动端退成横排行表。

### Journal Entry（期刊条目）

**Role:** 观点与动态
不做三张等宽卡。首篇为大条目（16:9 画心的装裱框 + 元信息 + 《书名号标题》），其余为右栏的行式条目（132px 斗方小框 + 文字），以界格线分隔。标题 `text-indent: -.5em` 让《悬出栏外。hover 只有标题转沉朱。

### Letter（引文块 · 朱丝栏信笺）

**Role:** 院长寄语
宣纸白信笺 + 纸影；引文竖排，30px 上下的文楷、行距 2.2em、字距 0.12em，背景用 `repeating-linear-gradient(to left, …)` 画 34% 朱砂栏线。信笺固定 5 栏、每栏约 8 字（`height:9.3em; width:11em`），引文占 4 栏，左侧留 1 空栏给落款的气口——空栏超过 1 栏就像没写完。右侧落款：34px「嘉木」+ 名章 + 两行身份。

### Product Row（产品下载行）

**Role:** 知君 / 万象
上一根焦墨线起头，行间界格线；每行：朱文小印 · 24px 产品名 + 一句话 ↗ · 禁用下载钮 + 说明。

### Contact Banner（墨池）

**Role:** 页尾联系
全宽焦墨底，宣纸白文楷 H2 居左、说明与两枚按钮居右下；骑缝章一半压在墨池、一半压在地脚。全页只有这一块深色。

### Input Field

**Role:** 文本输入
无框，只有一根 1px 清墨底线，高 48px；focus 底线变 2px 焦墨；error 底线变 2px 沉朱 + 下方 13px 提示。

### Badge

**Role:** 分类 / 状态
2px 圆角（不是胶囊），高 24px，12px 字、字距 0.14em；pastel-* 成对使用，或 1px 焦墨描边。

## Surfaces

| Level | Name | Value | Purpose |
| ----- | ---- | ----- | ------- |
| 0 | background 月白 | `#f2f4f1` | 主画布 |
| 1 | card 宣纸白 | `#fbfbf8` | 衬纸、信笺、乌丝栏、Logo 衬板 |
| 2 | secondary 绫边灰 | `#e8ebe6` | 禁用态、骨架 |
| 3 | inverse 墨池 | `#16181a` | 联系区，一页一次 |

层级靠「纸叠在纸上」的 1px 界格线区分，不靠阴影堆叠。

## Do's and Don'ts

### Do

- 画布一律月白 `#f2f4f1`。换成米色，这套就和「纸上学刊」撞了；换成纯白，墨色会发硬。
- 朱砂只以印的形态出现，全页 ≤3%；想强调就加墨，不要加红。
- 标题着重 = 重墨 → 焦墨 + 700 + 朱砂芝麻点，三件事一起做，不单用。
- 竖排只给短句：H1、步骤名、题签、书口、引文。超过 30 字的内容一律横排。
- 竖排里的拉丁缩写用 `text-combine-upright: all`（AI、01），长英文顺排成书脊。
- 天头大于地脚、左右不等宽；每屏至少留一整块什么都不放的空。
- 插画一律进装裱框，饱和度收到 .84；半人马用抠图 + 地线。
- 线分两级：界格线 `#d5d9d3` 管分隔，焦墨线 `#16181a` 管起止（区块首尾、书口、地线）。
- 动效统一 `var(--ease-ink)`，hover 0.3s。

### Don't

- 不要祥云、回纹、卷轴、水墨晕染底图、毛笔大字、仿古做旧纹理、破边印章——那是景区门户和茶叶礼盒。
- 不要红色按钮、红色标题、红色大色块；朱砂离开「印」就廉价。
- 不要用 Google Fonts 的 LXGW WenKai TC（台标字形）；不要用毛笔书法字体。
- 不要圆角 ≥4px、胶囊徽标、卡片大阴影、玻璃拟态、渐变。
- 不要纯黑 `#000`；最深就是焦墨 `#16181a`。
- 不要把插画直接贴在月白上——暖底和冷底会打架，必须隔一层宣纸白衬纸。
- 不要编造印文、数字、学员数、客户 logo；印文只从既有文案里取词。
- 不要「全面/深入/赋能/打造/极致」。品牌的文言感来自克制，不来自辞藻。
- 不要给正文用楷体；楷体只服务标题、引文、题签、印。

## Imagery

图像有两种待遇。**器物**：折纸半人马是品牌的「镇馆之物」，用透明抠图立在大片月白里，脚下一根地线、身侧一枚题签，像博物馆图录里的单品页；它的橙与钴蓝是全页唯一的高饱和，所以周围不放任何彩色。**册页**：三张暖色场景插画（经验 / 共学 / 创造）和期刊封面全部装裱——宣纸白衬纸隔开冷画布与暖画心，1px 内描线收边，`saturate(.84)` 把陶土橙压向赭石、把海军蓝压向黛色，让它们读起来像墨色体系里的「设色」而不是外来物。开本在横披、斗方、手卷之间轮换，避免三张同尺寸的图排成一列。Logo 在页眉页脚坐在 46px 的宣纸白衬板里（1px 界格线），不直接踩在画布上。图标不用图标库：箭头用字符 ↗ → ↓，其余一切图形需求由线、印、竖排字承担。

## Layout

1320px 容器、12 栏、32px 栏距。**卷首**三列不对称：左下是副标题与 CTA，中间是立在地线上的半人马，右侧顶格立竖排 H1（两列，右起），较短的右列下方落长方印；上方与左上大面积留空作天头；卷首底部一条双线书眉放品牌主张。**三章**每章一根贯穿的书口线：第一章文左图右（横披），第二章图左文右且文字下沉 88px（斗方），第三章文字一侧接产品行（手卷）。**共学五步**是全宽宣纸白乌丝栏。**观点与动态**是 7 + 4 栏的目录式排法，中间一根竖界格。**院长寄语**左信笺右落款，整体从第 2 栏起排，左边让出一栏空。**联系**是全页唯一的墨池，骑缝章压缝进入地脚。页眉不吸顶、不悬浮，就是一行书眉。断点：≤1180px 题签横排；≤900px 单列、书口保留在标题左侧、H1 仍竖排立在右上；≤520px 按钮通栏。

## Agent Prompt Guide

Quick Color Reference:

```
background 月白: #f2f4f1
card 宣纸白: #fbfbf8
ink 焦/浓/重/淡/清: #16181a / #26292c / #474c50 / #5f6569 / #a9aeaa
border 界格线: #d5d9d3
brand 朱砂 (≤3%, 只作印): #b5301f
brand-deep 沉朱: #8f2217
inverse 墨池: #16181a
```

Example Component Prompts:

1. Create a primary CTA: `inline-flex`, `min-height:48px`, `background:var(--color-primary)` (#16181a), `color:var(--color-primary-foreground)`, `border-radius:2px`, label `15px/500` Noto Sans SC with `letter-spacing:.1em` and `padding:0 22px`; append a 36px-wide `.chop` cell (`background:var(--color-brand)`, `margin:5px 5px 5px 0`, `border-radius:1px`) holding ↗. Hover: background → `--color-ink-zhong`, chop `scale(.9)` with `var(--ease-ink)` 0.3s. Never fill the whole button with cinnabar.
2. Create a chapter illustration mount: `figure` with `background:var(--color-card)`, `border:1px solid var(--color-border)`, `box-shadow:var(--shadow-mount)`, `padding:44px 32px 32px 20px`, grid `auto 1fr` gap 20px. Left cell is a `figcaption` title slip: `writing-mode:vertical-rl`, LXGW WenKai 13px, `letter-spacing:.2em`, 1px border, padding `14px 7px`. Right cell is the image at 4:3 / 1:1 / 3:2 with `object-fit:cover`, `filter:saturate(.84) contrast(.98)` and a 1px inset outline at 12% ink. No border-radius anywhere.
3. Create a section heading with emphasis: `font-family:var(--font-display)`, weight 400, `color:var(--color-ink-zhong)`, `font-size:var(--text-heading-lg)`, `letter-spacing:.04em`; wrap the key phrase in `<em>` with `font-style:normal; font-weight:700; color:var(--color-ink-jiao); text-emphasis:filled sesame var(--color-brand); text-emphasis-position:under right`. Do not color the text red.
4. Create a founder quote: card-colored letter paper with `--shadow-mount`; `blockquote` in `writing-mode:vertical-rl`, LXGW WenKai ~30px, `line-height:2.2`, `letter-spacing:.12em`, fixed `height:13.2em; width:13.2em`, background `repeating-linear-gradient(to left, transparent 0 calc(2.2em - 1px), var(--color-brand-rule) calc(2.2em - 1px) 2.2em)`; leave the unused ruled columns empty. Beside it: signature 34px bold + a white-on-cinnabar vertical name seal.

## Similar Brands

- **日本设计中心 NDC（原研哉）ndc.co.jp** — 抓取其 `_astro/*.css`：画布 `#fcfcfc`、字 `#1a1a1a`、灰 `#6f6f6f`、线 `#eee`，全站 0 处 `box-shadow`，缓动 `cubic-bezier(.16,1,.3,1)`，中文版字体栈为 Source Serif 4 + Songti SC。借了：**近白画布 + 近黑字 + 几乎不用阴影**的底盘、`--ease-ink` 的曲线原值、Source Serif 4 作拉丁、1500px 级宽容器的疏排。
- **故宫博物院 dpm.org.cn** — 抓取 `main.css`：宫墙红 `#761e1d` / `#b73736` 只占色值出现次数的极小比例，正文 `#474747` / `#707070`；`writing-mode: vertical-rl/tb-rl` 在样式表里出现 50 余次，竖排用于栏目名与展品题名。借了：**竖排只给短题名**的用法、红色作点题而非铺底、`#474747` 一档的「重墨」正文灰。没借：它的圆形按钮（`border-radius:50%` 103 处）、金棕 `#9a7646` 和大投影。
- **茑屋书店 T-SITE store.tsite.jp** — 抓取 `index.css`：主体只有黑白 + 暖灰线 `#e5e5e1` / `#f6f6f3`，圆角几乎为 0，全表仅 1 处 1px 阴影。借了：**用一根暖灰细线做所有分隔**的习惯（界格线 `#d5d9d3` 由此校冷）、目录式而非卡片式的内容列表。
- **无印良品 muji.com.cn** — 抓取 `muji.2.1.css` / `portal.1.0.css`：`#333` 字、`#eee` / `#ccc` 线、`max-width:1024px`、无阴影。借了：**信息靠线与空白分组、不靠容器**；反过来提醒自己不要学它的 15–20px 圆角按钮。
- **观夏 tosummer.com / 上下 shang-xia.com** — 列为气质参照（东方留白、器物式单品摄影、竖排点题）；调研时两站在本机网络下 TCP 不通 / DNS 无解析，Firecrawl 与 Exa 亦未取回，**未能读到真实 CSS，故未从它们取任何具体数值**。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 纸 */
  --color-background: #f2f4f1;
  --color-foreground: #26292c;
  --color-card: #fbfbf8;
  --color-card-foreground: #26292c;
  --color-popover: #fbfbf8;
  --color-popover-foreground: #26292c;
  --color-secondary: #e8ebe6;
  --color-secondary-foreground: #26292c;
  --color-muted: #e8ebe6;
  --color-muted-foreground: #5f6569;
  --color-accent: #e8ebe6;
  --color-accent-foreground: #16181a;

  /* Colors — 墨分五色 */
  --color-ink-jiao: #16181a;
  --color-ink-nong: #26292c;
  --color-ink-zhong: #474c50;
  --color-ink-dan: #5f6569;
  --color-ink-qing: #a9aeaa;
  --color-primary: #16181a;
  --color-primary-foreground: #fbfbf8;
  --color-border: #d5d9d3;
  --color-border-strong: #16181a;
  --color-input: #a9aeaa;
  --color-ring: #16181a;
  --color-image-outline: rgba(22, 24, 26, 0.12);

  /* Colors — 朱砂印（全页 ≤3%） */
  --color-brand: #b5301f;
  --color-brand-deep: #8f2217;
  --color-brand-foreground: #fbfbf8;
  --color-brand-rule: rgba(181, 48, 31, 0.34);
  --color-destructive: #8f2217;
  --color-destructive-foreground: #fbfbf8;
  --color-success: #35573a;
  --color-success-foreground: #fbfbf8;

  /* Colors — 墨池（深色区块） */
  --color-inverse: #16181a;
  --color-inverse-foreground: #fbfbf8;
  --color-inverse-muted: #a9aeaa;
  --color-inverse-border: rgba(251, 251, 248, 0.2);

  /* Pastel semantic pairs — 朱 / 黛 / 竹青 / 缃 */
  --color-pastel-red-bg: #f4e3de;
  --color-pastel-red-text: #8f2217;
  --color-pastel-blue-bg: #e0e7ed;
  --color-pastel-blue-text: #2b4a63;
  --color-pastel-green-bg: #e2eae0;
  --color-pastel-green-text: #35573a;
  --color-pastel-yellow-bg: #f0e9d4;
  --color-pastel-yellow-text: #76570f;

  /* Typography — Font Families */
  --font-display:
    'Source Serif 4', 'LXGW WenKai', 'Kaiti SC', STKaiti,
    KaiTi, 'Songti SC', STSong, serif;
  --font-sans:
    'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei',
    system-ui, sans-serif;
  --font-serif:
    'Source Serif 4', 'Noto Serif SC', 'Songti SC', STSong, SimSun, Georgia,
    serif;
  --font-latin: 'Source Serif 4', Georgia, 'Times New Roman', serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  /* Typography — Scale */
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 22px;
  --text-heading: 30px;
  --text-heading-lg: clamp(32px, 3.7vw, 54px);
  --text-display: clamp(52px, 7.2vw, 108px);

  /* Line Height & Tracking */
  --leading-display: 1.16;
  --leading-heading: 1.3;
  --leading-body: 1.9;
  --tracking-display: 0.06em;
  --tracking-heading: 0.04em;
  --tracking-body: 0.02em;
  --tracking-label: 0.22em;

  /* Spacing (4px base) */
  --spacing: 0.25rem;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-12: 48px;
  --spacing-16: 64px;
  --spacing-24: 96px;
  --spacing-40: 160px;
  --spacing-56: 192px;
  --page-gutter: clamp(20px, 5vw, 72px);
  --content-max: 1320px;

  /* Border Radius — 纸与印都是直角 */
  --radius-none: 0;
  --radius-sm: 2px;
  --radius-md: 3px;

  /* Shadows — 只有装裱的一层纸影 */
  --shadow-none: none;
  --shadow-mount: 0 1px 0 rgba(22, 24, 26, 0.05), 0 24px 48px -36px rgba(22, 24, 26, 0.28);

  /* Motion */
  --ease-ink: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 0.3s;
  --duration-slow: 1s;
}
```

### Tailwind v4

```css
@theme {
  --color-background: #f2f4f1;
  --color-foreground: #26292c;
  --color-card: #fbfbf8;
  --color-card-foreground: #26292c;
  --color-popover: #fbfbf8;
  --color-popover-foreground: #26292c;
  --color-secondary: #e8ebe6;
  --color-secondary-foreground: #26292c;
  --color-muted: #e8ebe6;
  --color-muted-foreground: #5f6569;
  --color-accent: #e8ebe6;
  --color-accent-foreground: #16181a;
  --color-ink-jiao: #16181a;
  --color-ink-nong: #26292c;
  --color-ink-zhong: #474c50;
  --color-ink-dan: #5f6569;
  --color-ink-qing: #a9aeaa;
  --color-primary: #16181a;
  --color-primary-foreground: #fbfbf8;
  --color-border: #d5d9d3;
  --color-border-strong: #16181a;
  --color-input: #a9aeaa;
  --color-ring: #16181a;
  --color-image-outline: rgba(22, 24, 26, 0.12);
  --color-brand: #b5301f;
  --color-brand-deep: #8f2217;
  --color-brand-foreground: #fbfbf8;
  --color-destructive: #8f2217;
  --color-destructive-foreground: #fbfbf8;
  --color-success: #35573a;
  --color-success-foreground: #fbfbf8;
  --color-inverse: #16181a;
  --color-inverse-foreground: #fbfbf8;
  --color-inverse-muted: #a9aeaa;
  --color-pastel-red-bg: #f4e3de;
  --color-pastel-red-text: #8f2217;
  --color-pastel-blue-bg: #e0e7ed;
  --color-pastel-blue-text: #2b4a63;
  --color-pastel-green-bg: #e2eae0;
  --color-pastel-green-text: #35573a;
  --color-pastel-yellow-bg: #f0e9d4;
  --color-pastel-yellow-text: #76570f;

  --font-display: 'Source Serif 4', 'LXGW WenKai', 'Kaiti SC', STKaiti, KaiTi, serif;
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif;
  --font-serif: 'Source Serif 4', 'Noto Serif SC', 'Songti SC', serif;
  --font-latin: 'Source Serif 4', Georgia, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, monospace;

  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 22px;
  --text-heading: 30px;
  --text-heading-lg: clamp(32px, 3.7vw, 54px);
  --text-display: clamp(52px, 7.2vw, 108px);

  --radius-none: 0;
  --radius-sm: 2px;
  --radius-md: 3px;

  --shadow-mount: 0 1px 0 rgba(22, 24, 26, 0.05), 0 24px 48px -36px rgba(22, 24, 26, 0.28);

  --ease-ink: cubic-bezier(0.16, 1, 0.3, 1);
}
```
