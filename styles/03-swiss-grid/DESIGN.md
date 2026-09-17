# 半人马AI学院 · 瑞士网格 — Style Reference

> 白底、近黑、一支钴蓝，全部落在 12 栏上

**Theme:** light

这套范式把学院当成一份国际主义平面作品来排：画布是不加暖、不加灰的纯白（#ffffff），文字是近黑（#141414），全页只有一支信号色——从 logo 马身取样、压深到可读的钴蓝（#0f5fd0），累计面积 ≤8%。层级不靠阴影、不靠卡片、不靠圆角，只靠三样东西：12 栏网格、三种粗细的线（1px / 2px / 6px）、以及 900 字重的思源黑体 + Archivo 大标题。第 1–2 栏永远留给悬挂的编号与栏目名，正文从第 3 栏起，所以整页读起来像一份目录：左边是「第几章、哪一栏」，右边是内容。信息一律排成「行」——期刊是索引行，产品下载是表格行，共学五步是五个等宽栏——没有一张卡片。暖色插画全部转成单色图版压在浅灰衬底上，只有半人马保留橙与蓝，直接踩在首屏那条 6px 的黑线上。签名记忆点是**常显的 12 栏竖线 + 页眉的网格钮**：平时是几乎看不见的发丝线，按一下，整页的栏以 7% 钴蓝显形，访客会发现每一个字、每一张图确实都对在栏上。对经营者说的话很直接：这里教的是方法，不是鸡汤。

## Tokens — Colors

| Name           | Value                    | Token                        | Role                                                         |
| -------------- | ------------------------ | ---------------------------- | ------------------------------------------------------------ |
| 纯白画布       | `#ffffff`                | `--color-background`         | 整页背景。不加暖、不加灰——暖米色是别的方案的事               |
| 近黑前景       | `#141414`                | `--color-foreground`         | 主文字、大标题。不用 #000                                    |
| 近黑主色       | `#141414`                | `--color-primary`            | 主按钮底、实心徽标                                           |
| 纯白主前景     | `#ffffff`                | `--color-primary-foreground` | primary 与钴蓝色块上的文字                                   |
| 结构线黑       | `#141414`                | `--color-rule`               | 6px / 2px / 1px 三种结构线，与文字同色                        |
| 钴蓝信号       | `#0f5fd0`                | `--color-brand`              | 强调词、步骤进度条、悬停、焦点环、联系色块。白底 5.9:1，全页 ≤8% |
| 深钴蓝         | `#0b4fc0`                | `--color-brand-strong`       | 按下态、浅蓝底上的字（7.3:1）                                |
| AA 次要文      | `#5c5f66`                | `--color-muted-foreground`   | 说明、摘要、图注。白底 6.4:1，浅灰底 5.8:1                    |
| 浅灰衬底       | `#f3f3f1`                | `--color-secondary`          | 图版衬底、输入框底、禁用按钮                                 |
| 行线灰         | `#d4d4d1`                | `--color-border`             | 表格行之间的次级发丝线、禁用按钮边                           |
| 栏线灰         | `#ececea`                | `--color-grid`               | 常显的 12 栏竖线，只比白深一点                               |
| 栏显形         | `rgba(15,95,208,0.07)`   | `--color-grid-band`          | 按下网格钮后每一栏的填色                                     |
| 警示红         | `#b3261e`                | `--color-destructive`        | 仅表单错误                                                   |
| 确认绿         | `#1e6b3a`                | `--color-success`            | 仅成功反馈                                                   |

### 柔和语义色（浅底 + 深字，成对使用）

| Name | Background | Text      | Token                     |
| ---- | ---------- | --------- | ------------------------- |
| 柔灰 | `#f3f3f1`  | `#5c5f66` | `--color-pastel-gray-*`   |
| 柔蓝 | `#e7effb`  | `#0b4fc0` | `--color-pastel-blue-*`   |
| 柔橙 | `#fdeede`  | `#95470a` | `--color-pastel-orange-*` |
| 柔绿 | `#e6f2ea`  | `#1e6b3a` | `--color-pastel-green-*`  |

柔橙是 logo 人身的橙在界面里唯一的落点，只做状态徽标，不做按钮、不做标题。本站没有图表，不设图表色。

## Tokens — Typography

### Archivo — 拉丁与数字 · `--font-sans` / `--font-display` 的首位

- **Substitute:** Helvetica Neue, Helvetica（macOS / iOS 自带）；Windows 落到 Microsoft YaHei 的拉丁字形
- **Weights:** 400, 500, 700, 900
- **Sizes:** 12px（标签）到 152px（H1 里的 “AI”）
- **Line height:** 标题 1.04–1.1 / 正文 1.65
- **Letter spacing:** display -0.035em / heading -0.02em / 大写标签 +0.08em
- **OpenType features:** tabular-nums（日期、编号）
- **Role:** 所有英文眉标（CENTAUR JOURNAL、FROM THE FOUNDER）、悬挂编号 01–05、日期。排在字体栈最前，让中英混排里的拉丁字母和数字先吃到 grotesk 字形。禁用 Inter / Roboto / Arial。

### 思源黑体 Noto Sans SC — 中文主字体 · `--font-sans` / `--font-display`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, Source Han Sans SC
- **Weights:** 400（正文）, 500（导航）, 700（小标题、按钮）, 900（H1 / H2 / 引文）
- **Sizes:** 12px, 14px, 16px, 18px, 20px, 28px, 34–68px, 50–152px
- **Line height:** 标题 1.04–1.22 / 正文 1.65
- **Letter spacing:** 大标题 -0.035em（Black 字重的中文字面自带边距，收紧后才成「块」）
- **Role:** 全站中文。Black（900）是这套范式的声音；回退到 PingFang SC 时最重只有 Semibold，标题会变轻但栏宽、换行不变，版式不塌。

### Geist Mono — 样张里的色值与 token 名 · `--font-mono`

- **Substitute:** ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas
- **Weights:** 400, 500
- **Sizes:** 12px, 13px
- **Role:** 只在组件样张和文档里标 hex、token 名。首页不出现等宽字——日期和编号用 Archivo 的 tabular-nums。

### Type Scale

| Role       | Size                        | Line Height | Letter Spacing | Token               |
| ---------- | --------------------------- | ----------- | -------------- | ------------------- |
| display    | clamp(50px, 10vw, 152px)    | 1.04        | -0.035em       | `--text-display`    |
| heading-lg | clamp(34px, 4.6vw, 68px)    | 1.1         | -0.02em        | `--text-heading-lg` |
| index      | clamp(40px, 4.4vw, 64px)    | 1.0         | -0.03em        | `--text-index`      |
| heading    | 28px                        | 1.2         | -0.02em        | `--text-heading`    |
| subheading | 20px                        | 1.4         | 0              | `--text-subheading` |
| body-lg    | 18px                        | 1.65        | 0              | `--text-body-lg`    |
| body       | 16px                        | 1.65        | 0              | `--text-body`       |
| body-sm    | 14px                        | 1.55        | 0              | `--text-body-sm`    |
| caption    | 12px                        | 1.4         | +0.08em（大写）| `--text-caption`    |

字重只有四档：900（标题）、700（小标题 / 按钮 / 标签）、500（导航 / 编号）、400（正文）。没有 300，没有 600。

## Tokens — Spacing & Shapes

**Base unit:** 8px（`--spacing: 0.5rem`）

**Density:** 宽松。区块之间 80–96px，但行内信息密——像一份排得很紧的目录，放在很大的白纸上。

### Spacing Scale

| Name | Value | Token          |
| ---- | ----- | -------------- |
| 1    | 4px   | `--spacing-1`  |
| 2    | 8px   | `--spacing-2`  |
| 3    | 12px  | `--spacing-3`  |
| 4    | 16px  | `--spacing-4`  |
| 6    | 24px  | `--spacing-6`  |
| 8    | 32px  | `--spacing-8`  |
| 12   | 48px  | `--spacing-12` |
| 16   | 64px  | `--spacing-16` |
| 20   | 80px  | `--spacing-20` |
| 24   | 96px  | `--spacing-24` |
| 32   | 128px | `--spacing-32` |
| 40   | 160px | `--spacing-40` |

### Grid

| Name   | Value                       | Token            |
| ------ | --------------------------- | ---------------- |
| 栏数   | 12（手机 4）                | `--grid-columns` |
| 栏距   | 24px（手机 16px）           | `--grid-gutter`  |
| 页边   | clamp(20px, 4.44vw, 64px)   | `--grid-margin`  |
| 容器   | 1440px                      | `--container`    |

### Rules（线 = 这套系统唯一的「深度」）

| Name   | Value | Token           | 用在哪                                       |
| ------ | ----- | --------------- | -------------------------------------------- |
| hair   | 1px   | `--rule-hair`   | 页眉底、章节之间、表格行、图注顶             |
| strong | 2px   | `--rule-strong` | 表头、按钮边、输入框底、步骤顶               |
| heavy  | 6px   | `--rule-heavy`  | 一级分区的顶、首屏「地面线」、步骤进度条     |

### Border Radius

| Name | Value | Token      |
| ---- | ----- | ---------- |
| 全部 | 0px   | `--radius` |

| Element | Value |
| ------- | ----- |
| 按钮    | 0     |
| 输入框  | 0     |
| 徽标    | 0     |
| 图版    | 0     |

只有一个圆角 token，值是 0。需要「柔和」的时候加留白，不加圆角。

### Shadows

| Name | Value  | Token           |
| ---- | ------ | --------------- |
| none | `none` | `--shadow-none` |

没有阴影。唯一的投影是半人马抠图脚下自带的那一片。

### Motion

| Name          | Value                         | Token             |
| ------------- | ----------------------------- | ----------------- |
| ease-swiss    | `cubic-bezier(0.2, 0, 0, 1)`  | `--ease-swiss`    |
| duration-fast | `120ms`                       | `--duration-fast` |
| duration-base | `240ms`                       | `--duration-base` |

动效只有三种：箭头位移 3px、按钮按下下沉 1px、图版进入视口时 1.05→1 的缩放（scroll-driven，终态即默认态）。没有回弹、没有淡入瀑布。`prefers-reduced-motion` 下全部关闭。

### Layout

- **Section gap:** 80–96px（手机 48px）
- **悬挂栏:** 第 1–2 栏只放编号、栏目名、眉标
- **Element gap:** 24px（= 栏距）
- **Max content width:** 1440px 容器，内容区 1312px

## Components

### Primary Button

**Role:** 主 CTA（联系学院顾问）
`bg-primary`(#141414) `text-primary-foreground`, `border: 2px solid`, `border-radius: 0`, `min-height: 48px`, `padding: 0 24px 0 16px`, `font: 15px/700`. 文字靠左、箭头靠右（`justify-content: space-between`），在窄栏里会拉满成一行表格。hover: 底与边变 `--color-brand`；active: `--color-brand-strong` + `translateY(1px)`；focus-visible: 2px 钴蓝 outline，offset 3px；disabled: `bg-secondary` + `border-border` + `muted-foreground`。钴蓝色块上反白。

### Outline Button

**Role:** 并列次动作（复制客服链接）
透明底 + 2px 近黑边。hover 整块反黑；active 钴蓝。与主按钮同高同宽，上下叠放时像两行表格。

### Text Link

**Role:** 行内去向（了解共学与共创 →）
700 字重，2px 下划线，offset 6px，箭头不带下划线。hover 变钴蓝，箭头 `translate(3px,0)`，↗ 则 `translate(2px,-2px)`。点击区上下补到 44px。

### Grid Toggle（签名组件）

**Role:** 让网格显形
页眉右侧 44×44 的图标钮，本体是一个 `<input type="checkbox">` + `<label>`，零 JS：`body:has(#grid-toggle:checked) .guides i::after{opacity:1}`。`.guides` 是 `position:fixed` 的 12 个 `<i>`，左右各外扩半个栏距，所以竖线正好落在栏距中线。默认态只有 #ececea 的发丝线；开启后每栏填 7% 钴蓝。

### Chapter Row（章节行）

**Role:** 三个叙事章节
12 栏：`1–2` 悬挂编号（Archivo 500，40–64px）+ 章节名（14px/700），桌面端 `position:sticky; top:96px`；`3–7` H2 + 说明 + 文字链；`8–12` 图版。第二章翻转为 `3–8` 图、`9–12` 文，编号栏不动。章节之间只有一条 1px 黑线。

### Plate（图版）

**Role:** 所有场景插画
`filter: grayscale(1) contrast(1.08)`，直角，无边无影，衬底 `--color-secondary`，固定 4:3。图注在图下：1px 黑线 + 左侧大写标签（12px/700/+0.08em）+ 右对齐的灰字。半人马抠图是唯一例外：保留原色，不进框。

### Product Row（产品下载行）

**Role:** 知君 / 万象
`grid-template-columns: 4.5em 1fr auto`，顶 2px 黑线，行间 1px 灰线。左：产品名 28px/900；中：主张文字链 + 直角柔灰徽标「下载暂未开放」；右：44px 高的禁用按钮。

### Steps（流程步骤）

**Role:** 共学五步
五个等宽栏，各占 2 个网格栏。每步顶 2px 黑线，上面压一条 6px 钴蓝进度条，宽度 = 步数 × 20%（`--n`）。编号 Archivo 500，下隔 48px 才是标题——留白本身是节奏。手机端改为纵向表格：编号一列、内容一列。

### Index Row（期刊索引行）

**Role:** 观点与动态
整行是一个 `<a>`：`1–2` 日期 + 实心黑徽标，`3–4` 4:3 单色缩略图，`5–8` 标题 28px/900（按词组 `inline-block` 断行，不拆词），`9–11` 摘要，`12` ↗。hover：标题变钴蓝，箭头右上移 3px。行与行之间 1px 黑线。

### Pull Quote（引文）

**Role:** 院长寄语
900 字重，28–56px，`text-indent: -0.48em` 让开引号悬挂到第 3 栏栏线之外。下方两栏：正文与署名各自顶一条 1px 黑线。没有大引号装饰、没有头像占位。

### Contact Field（联系横幅）

**Role:** 页尾行动区
`1–8` 栏是全页唯一的钴蓝色块（min-height 420px，眉标在上、H2 沉底）；`9–12` 栏顶 6px 黑线，正文在上、两个满宽按钮沉底。色块不满宽，是为了把钴蓝总量压在 8% 以内，也为了不对称。

### Input Field

**Role:** 文本输入
`bg-secondary`，无四边框，只有 2px 近黑底线，`height: 48px`，直角。focus: 2px 钴蓝 outline + 底线变钴蓝；error: 底线 `--color-destructive` + 12px 红字提示。

### Badge

**Role:** 栏目与状态
直角小方块，`min-height: 24px`，`padding: 0 8px`，12px/700。实心黑只给栏目名（观点 / 动态）；状态用柔和语义对。

## Surfaces

| Level | Name       | Value     | Purpose                                  |
| ----- | ---------- | --------- | ---------------------------------------- |
| 0     | background | `#ffffff` | 整页，含页眉页脚                         |
| 1     | secondary  | `#f3f3f1` | 图版衬底、输入框、禁用态                 |
| 2     | brand      | `#0f5fd0` | 联系色块，全页一处                       |
| 3     | primary    | `#141414` | 按钮、实心徽标——面积极小，不做整段黑底   |

层级靠线的粗细分，不靠底色叠加。没有「卡片浮在背景上」这回事。

## Do's and Don'ts

### Do

- 每个元素的左边缘都对到某一条栏线上；拿不准就按网格钮检查。
- 第 1–2 栏只放编号、栏目名、眉标，正文从第 3 栏起——「悬挂」是这套版式的骨架。
- 钴蓝 `#0f5fd0` 只给：每个标题里的一个强调词、步骤进度条、悬停 / 焦点、联系色块。全页 ≤8%。
- 一级分区用 6px 线，章节之间用 1px 线，表头用 2px 线——三种粗细各司其职，不混用。
- 场景插画一律转单色图版；只有半人马保留橙与蓝。
- 中文标题按词组断行（`<span class="ph">` = inline-block），不让「工 / 具」被拆开。
- 数字用 Archivo + `tabular-nums`，日期写成 2026.09.15。
- 严格左对齐。图注右侧那一段是唯一允许右对齐的文字。

### Don't

- 不要圆角，1px 也不要；不要任何 box-shadow。
- 不要把信息装进卡片——三篇文章就是三行，两个产品就是两行。
- 不要居中排版，不要居中的 hero。
- 不要渐变——包括用 linear-gradient 画线，线用 border。
- 不要把钴蓝铺成大面积背景或第二个色块；也不要引入橙色做强调，橙只活在半人马身上和柔橙徽标里。
- 不要用 #000 和暖米色底；白就是 #ffffff。
- 不要给没有顺序的东西编号——只有三章和五步有编号。
- 不要用「全面 / 深入 / 赋能 / 打造」；这套版式里一句空话会比在别处更刺眼。

## Imagery

三张场景插画（experience / co-learning / creating）原稿是暖色纸感，和纯白 + 钴蓝的色板冲突，所以一律 `grayscale(1) contrast(1.08)` 转成单色图版，像老设计年鉴里的黑白图录：4:3、直角、无边、浅灰衬底，下面跟一条 1px 线和一行图注。期刊缩略图同样处理。半人马用透明抠图版，保留橙与蓝，直接站在白底上；首屏里它的前蹄压在 6px 黑线上，那条线就是地面——这是全页唯一的「插画时刻」，也是 logo 色唯一完整出现的地方。图标只有三个内联 SVG / 字符（网格钮、菜单、箭头 ↗ → ↓），1.5px 线宽，不用图标库，不用 emoji。

## Layout

1440px 容器、64px 页边、12 栏 × 24px 栏距，竖线常显。页眉 64px 高、白底、底 1px 黑线、sticky：logo 与站名在左，四项导航、网格钮、直角黑按钮在右。首屏：眉标一行 + 灰线；H1 占 `1–8` 栏、顶对齐；副标题（`1–3`）与说明（`4–6`）并排沉底，下面是主按钮与文字链；半人马占 `7–12` 栏、踩在 6px 线上；线下一行左边是品牌主张，右边是图注。之后是三行章节（悬挂编号 / 文 / 图，第二行翻转），6px 线，五步（`1–2` 栏标题 + `3–12` 栏五等分），6px 线，期刊索引（标题行 + 三条索引行），6px 线，院长引文，钴蓝联系色块（`1–8`）+ 行动栏（`9–12`），页脚三段（logo / 口号 / 发起方）+ 一行主张。≤1079px：文与图上下叠，仍留悬挂栏；≤899px：导航收进菜单；≤719px：12 栏收成 4 栏，所有内容通栏，五步变纵向表格，联系色块出血到屏幕边。

## Agent Prompt Guide

Quick Color Reference:

```
background: #ffffff
foreground / primary / rule: #141414
brand (≤8%): #0f5fd0
brand-strong: #0b4fc0
muted-foreground: #5c5f66
secondary: #f3f3f1
border: #d4d4d1
grid line: #ececea
```

Example Component Prompts:

1. Create a primary CTA: `background:#141414; color:#fff; border:2px solid #141414; border-radius:0; min-height:48px; padding:0 24px 0 16px; font:700 15px Archivo,'Noto Sans SC'`. Label left, arrow ↗ right (`justify-content:space-between`). Hover swaps fill and border to `#0f5fd0`, active `#0b4fc0` + `translateY(1px)`. No shadow, no scale.
2. Create a journal index row: a single `<a>` on a 12-column grid with a 1px `#141414` top rule — cols 1–2 date (`tabular-nums`, 14px/500) + square black badge, cols 3–4 a 4:3 thumbnail with `filter:grayscale(1) contrast(1.08)`, cols 5–8 title 28px/900 tracking -0.02em, cols 9–11 excerpt 15px `#5c5f66`, col 12 a ↗ that moves 3px up-right on hover while the title turns `#0f5fd0`. No card, no radius, no background.
3. Create a process strip: five equal columns, each with a 2px `#141414` top rule overlaid by a 6px `#0f5fd0` bar whose width is `calc(var(--n) * 20%)`; number in Archivo 500 at `clamp(40px,4.4vw,64px)`, 48px gap, then title 20px/900 and one line of 14px `#5c5f66` text.

## Similar Brands

- **Pentagram（pentagram.com）** — 实测 CSS：白 `#fff` + `#1a1a1a` 文字 + `#767676` 次要文 + `#e3e4e5` 线，单一信号红 `#e61428`；字体 Neue Haas / Plain；`border-radius:0` 与 `box-shadow:none` 是主流；标题字距 `-0.02em`。借了：「一白一黑一支信号色」的配比、`-0.02em` 标题字距、零圆角零阴影。
- **MIT Media Lab（media.mit.edu）** — 实测：typekit 的 `neue-haas-grotesk-display`，字重只用 700 / 400 两档，`#201f20` 近黑，单一青蓝 `#00aeef`，`border-radius:0` 最多。借了：字重只留极少几档、近黑而非纯黑、学术机构用一支蓝做全部交互信号。
- **teenage engineering（teenage.engineering）** — 实测：`grid-template-columns:repeat(12,minmax(0,1fr))`，`border-radius:0`，全站零 box-shadow，灰阶 `#f5f5f5 / #e5e5e5`。借了：12 栏 `minmax(0,1fr)` 的写法、产品信息排成行与表而不是卡片、浅灰只做衬底。
- **Vercel Geist（vercel.com/geist）** — 实测：`--ds-gray-1000:#171717`，`--ds-gray-100:#f2f2f2`，蓝 `#0070f3 / #0064e2`，12 栏网格与「显形的网格线」是其标志，Geist Mono 标注数值。借了：把网格线当作可见的品牌元素、近黑取值区间、样张里用 Geist Mono 标 token。
- **IDEO U（ideou.com）** — 实测：Gotham + Sentinel，`#2a2623` 暖近黑，信号黄 `#ffd203`，字重以 500 / 700 为主，圆角 4px、有 `0 4px 20px` 阴影。借了：面向管理者的课程站「一句大标题 + 一句人话说明」的文案节奏；**没借**它的圆角、阴影和暖色——那是「董事会」「纸感」方向的地盘。
- **Josef Müller-Brockmann《Grid Systems》** — 借了：悬挂编号栏、图注压在图下的一条线上、用线的粗细而不是底色分层、严格左对齐。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors */
  --color-background: #ffffff;
  --color-foreground: #141414;
  --color-card: #ffffff;
  --color-card-foreground: #141414;
  --color-primary: #141414;
  --color-primary-foreground: #ffffff;
  --color-secondary: #f3f3f1;
  --color-secondary-foreground: #141414;
  --color-muted: #f3f3f1;
  --color-muted-foreground: #5c5f66;
  --color-brand: #0f5fd0;
  --color-brand-strong: #0b4fc0;
  --color-brand-foreground: #ffffff;
  --color-rule: #141414;
  --color-border: #d4d4d1;
  --color-input: #141414;
  --color-ring: #0f5fd0;
  --color-grid: #ececea;
  --color-grid-band: rgba(15, 95, 208, 0.07);
  --color-destructive: #b3261e;
  --color-destructive-foreground: #ffffff;
  --color-success: #1e6b3a;
  --color-success-foreground: #ffffff;

  /* Pastel semantic pairs */
  --color-pastel-blue-bg: #e7effb;
  --color-pastel-blue-text: #0b4fc0;
  --color-pastel-gray-bg: #f3f3f1;
  --color-pastel-gray-text: #5c5f66;
  --color-pastel-orange-bg: #fdeede;
  --color-pastel-orange-text: #95470a;
  --color-pastel-green-bg: #e6f2ea;
  --color-pastel-green-text: #1e6b3a;

  /* Typography — Font Families */
  --font-sans:
    'Archivo', 'Helvetica Neue', Helvetica, 'Noto Sans SC', 'PingFang SC',
    'Hiragino Sans GB', 'Microsoft YaHei', 'Source Han Sans SC', sans-serif;
  --font-display:
    'Archivo', 'Helvetica Neue', Helvetica, 'Noto Sans SC', 'PingFang SC',
    'Hiragino Sans GB', 'Microsoft YaHei', 'Source Han Sans SC', sans-serif;
  --font-mono:
    'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    monospace;

  /* Typography — Scale */
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 20px;
  --text-heading: 28px;
  --text-heading-lg: clamp(34px, 4.6vw, 68px);
  --text-display: clamp(50px, 10vw, 152px);
  --text-index: clamp(40px, 4.4vw, 64px);

  /* Line Height & Tracking */
  --leading-display: 1.04;
  --leading-heading: 1.1;
  --leading-body: 1.65;
  --tracking-display: -0.035em;
  --tracking-heading: -0.02em;
  --tracking-body: 0em;
  --tracking-label: 0.08em;
  --weight-display: 900;
  --weight-strong: 700;
  --weight-body: 400;

  /* Spacing (8px base) */
  --spacing: 0.5rem;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-12: 48px;
  --spacing-16: 64px;
  --spacing-20: 80px;
  --spacing-24: 96px;
  --spacing-32: 128px;
  --spacing-40: 160px;

  /* Grid */
  --grid-columns: 12;
  --grid-gutter: 24px;
  --grid-margin: clamp(20px, 4.44vw, 64px);
  --container: 1440px;

  /* Rules — 线是这套系统唯一的「深度」 */
  --rule-hair: 1px;
  --rule-strong: 2px;
  --rule-heavy: 6px;

  /* Border Radius */
  --radius: 0px;

  /* Shadows */
  --shadow-none: none;

  /* Motion */
  --ease-swiss: cubic-bezier(0.2, 0, 0, 1);
  --duration-fast: 120ms;
  --duration-base: 240ms;
}
```

### Tailwind v4

```css
@theme {
  --color-background: #ffffff;
  --color-foreground: #141414;
  --color-card: #ffffff;
  --color-card-foreground: #141414;
  --color-primary: #141414;
  --color-primary-foreground: #ffffff;
  --color-secondary: #f3f3f1;
  --color-secondary-foreground: #141414;
  --color-muted: #f3f3f1;
  --color-muted-foreground: #5c5f66;
  --color-brand: #0f5fd0;
  --color-brand-strong: #0b4fc0;
  --color-brand-foreground: #ffffff;
  --color-rule: #141414;
  --color-border: #d4d4d1;
  --color-input: #141414;
  --color-ring: #0f5fd0;
  --color-grid: #ececea;
  --color-grid-band: rgba(15, 95, 208, 0.07);
  --color-destructive: #b3261e;
  --color-destructive-foreground: #ffffff;
  --color-success: #1e6b3a;
  --color-success-foreground: #ffffff;
  --color-pastel-blue-bg: #e7effb;
  --color-pastel-blue-text: #0b4fc0;
  --color-pastel-gray-bg: #f3f3f1;
  --color-pastel-gray-text: #5c5f66;
  --color-pastel-orange-bg: #fdeede;
  --color-pastel-orange-text: #95470a;
  --color-pastel-green-bg: #e6f2ea;
  --color-pastel-green-text: #1e6b3a;

  --font-sans: 'Archivo', 'Helvetica Neue', 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  --font-display: 'Archivo', 'Helvetica Neue', 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  --font-mono: 'Geist Mono', ui-monospace, monospace;

  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 20px;
  --text-heading: 28px;
  --text-heading-lg: clamp(34px, 4.6vw, 68px);
  --text-display: clamp(50px, 10vw, 152px);
  --text-index: clamp(40px, 4.4vw, 64px);

  --spacing: 0.5rem;

  --radius: 0px;
  --radius-sm: 0px;
  --radius-md: 0px;
  --radius-lg: 0px;

  --shadow-sm: none;
  --shadow-md: none;

  --ease-swiss: cubic-bezier(0.2, 0, 0, 1);
}
```
