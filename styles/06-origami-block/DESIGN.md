# 半人马AI学院 · 折纸色块 — Style Reference

> 把 logo 的折纸切面铺成整站的色块

**Theme:** light

这一套不是「给网站配一个 logo」，而是让网站从 logo 里长出来。logo 是一只低多边形折纸半人马——橘橙人身、钴蓝马身，每个面都有受光、本色、背光三种明度。我们把这条规则原样搬到页面上：钴蓝 #1450c8 和橘橙 #f47216 各带一组「三面色」（lit / base / deep），整段铺色而不是点缀，区块之间用一道斜折痕过渡，折痕旁边永远跟着一块背光三角面。画布是米白 #f6f1e6（纸的正面），文字与硬投影是墨蓝 #0e1a3a（不用纯黑）。全站只有这两种彩色，没有第三种；橘橙上只放墨蓝字（5.92:1），钴蓝上只放白字（6.97:1）。容器一律方正（radius 0），右上角切掉一个 45° 折角并露出一小块「纸背」；阴影只有一种——不带模糊的 4 / 8 / 16px 位移色块，像两张纸错开叠放。签名记忆点有两个：首屏半人马抠图站在一块橘橙折纸台座上、身后是斜切的钴蓝大色块；以及「共学五步」的**经折流程带**——五块面板上下沿交替错开，读起来像一条拉开的经折装纸带。气质上要的是「明快、自信、敢用颜色」，对象是 35–55 岁的经营者，所以没有吉祥物、没有彩虹色、没有圆滚滚的圆角。

## Tokens — Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| 米白画布 | `#f6f1e6` | `--color-background` | 页面底色，纸的正面；也是墨蓝底上的主文字色 |
| 墨蓝前景 | `#0e1a3a` | `--color-foreground` / `--color-ink` | 主文字、2px 边线、硬投影、深色分区与页脚；替代纯黑 |
| 白卡 | `#fffdf7` | `--color-card` | 卡片、图片衬纸、输入框、次级按钮面 |
| 深米 | `#ebe3d2` | `--color-secondary` / `--color-muted` | 次级分区底（观点与动态）、米白上的背光折面、禁用底 |
| 灰蓝次文 | `#4a5470` | `--color-muted-foreground` | 次要文字；米白底 6.67:1、深米底 5.89:1、白卡底 7.39:1 |
| 钴蓝 · 受光 | `#2a66dc` | `--color-cobalt-lit` | 钴蓝色块上的高光折面；白字 5.21:1，可以压字 |
| 钴蓝 · 本色 | `#1450c8` | `--color-cobalt` / `--color-brand` | 品牌主色块：首屏左半、第三章、流程带、强调词垫条；白字 6.97:1 |
| 钴蓝 · 背光 | `#0d3a96` | `--color-cobalt-deep` | 折痕旁的阴影面、流程带偶数面板、钴蓝标签的纸背；白字 10.18:1 |
| 蓝上次文 | `#dbe6fc` | `--color-cobalt-muted-foreground` | 钴蓝底上的说明文字 5.56:1 |
| 橘橙 · 受光 | `#ffb070` | `--color-orange-lit` | 台座顶面、橘橙色块上的高光折面、墨蓝底上的文字链 8.30:1 |
| 橘橙 · 本色 | `#f47216` | `--color-orange` / `--color-primary` | 主 CTA、第二章与联系区整段铺色；只配墨蓝字 5.92:1，不配白字 |
| 橘橙 · 背光 | `#e0640c` | `--color-orange-deep` | 橘橙色块的阴影面、主按钮折角的纸背；不承载 16px 以下文字 |
| 墨上次文 | `#b3bdd6` | `--color-ink-muted-foreground` | 墨蓝底上的次要文字 9.10:1 |
| 焦点环 | `#0e1a3a` / `#ffb070` | `--color-ring` / `--color-ring-inverse` | 浅底用墨蓝环，钴蓝 / 墨蓝底用受光橘环；3px 实线、offset 3px |

### 三面色（本范式的语义色，代替 pastel 对）

本站没有成功 / 警告 / 危险这类状态，所以不设 pastel 语义色。成对出现的是「底色 + 它上面允许的字色 + 它的纸背色」：

| 底 | Background | Text | 折角纸背 / 位移色块 | Token |
| --- | --- | --- | --- | --- |
| 钴蓝 | `#1450c8` | `#ffffff` | `#0d3a96` | `--color-cobalt*` |
| 橘橙 | `#f47216` | `#0e1a3a` | `#e0640c` | `--color-orange*` |
| 墨蓝 | `#0e1a3a` | `#f6f1e6` | `#1450c8` | `--color-ink*` |
| 白卡 | `#fffdf7` | `#0e1a3a` | `#ebe3d2`，或所在分区的对比色 | `--color-card*` |
| 禁用 | `#ebe3d2` | `#4a5470` | `#f6f1e6`，无位移色块 | `--color-disabled-*` |

## Tokens — Typography

### Bricolage Grotesque + 思源黑体 Heavy — 标题 · `--font-display`

- **Substitute:** 拉丁回退 Avenir Next / Trebuchet MS；中文回退 PingFang SC（Semibold）/ Hiragino Sans GB / Microsoft YaHei（Bold）
- **Weights:** 拉丁与数字 800（Bricolage 可变字重 500–800，opsz 12–96）；中文 900（Noto Sans SC Black）
- **Sizes:** 24px, 28–40px, 36–68px, 44–104px（全部 `clamp()`）
- **Line height:** display 1.08 / heading 1.16 / subheading 1.3
- **Letter spacing:** display -0.02em / heading -0.01em
- **OpenType features:** tabular-nums（章节号、步骤号）
- **Role:** H1、H2、卡片标题、章节号方块、步骤数字、产品名。字重必须厚——色块这么重，细字压不住。回退到苹方时最重只有 Semibold，字面变窄约 3%，折行位置不变。

### 思源黑体 Noto Sans SC — 正文与 UI · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, system-ui
- **Weights:** 400（正文）, 500（导航、产品副链）, 700（按钮、文字链、小标题）
- **Sizes:** 14px, 15px, 16px, 17px, 19px
- **Line height:** 1.75（正文）/ 1.6（卡片内）
- **Letter spacing:** 0；首屏底栏与页脚口号 +0.06em
- **Role:** 全站正文、导航、按钮、表单。不用 Inter / Roboto / Arial。

### Space Mono — 眉标 / 图注 / 日期 · `--font-mono`

- **Substitute:** ui-monospace, SFMono-Regular, Menlo, Consolas；中文落到 PingFang SC
- **Weights:** 400（图注、日期）, 700（眉标、图注英文段）
- **Sizes:** 10px（logo 下小字）, 12px
- **Letter spacing:** +0.08em，英文全大写
- **Role:** `CENTAUR AI ACADEMY`、`HUMAN × AI`、`2026.09.15`、「下载暂未开放」这类标注性文字。等宽字不进正文和标题。

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| display | clamp(44px, 7.2vw, 104px) | 1.08 | -0.02em | `--text-display` |
| heading-lg | clamp(36px, 4.8vw, 68px) | 1.16 | -0.01em | `--text-heading-lg` |
| heading | clamp(28px, 3vw, 40px) | 1.16 | -0.01em | `--text-heading` |
| subheading | 24px | 1.3 | 0 | `--text-subheading` |
| body-lg | 19px | 1.7 | 0 | `--text-body-lg` |
| body | 16px | 1.75 | 0 | `--text-body` |
| body-sm | 14px | 1.75 | 0 | `--text-body-sm` |
| caption | 12px（mono） | 1.5 | +0.08em | `--text-caption` |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 0.25rem`）

**Density:** 宽松。色块本身很重，所以区块上下留 72–144px，让颜色有地方「落下来」。

### Spacing Scale

| Name | Value | Token |
| --- | --- | --- |
| 1 | 4px | `--spacing-1` |
| 2 | 8px | `--spacing-2` |
| 3 | 12px | `--spacing-3` |
| 4 | 16px | `--spacing-4` |
| 6 | 24px | `--spacing-6` |
| 8 | 32px | `--spacing-8` |
| 12 | 48px | `--spacing-12` |
| 16 | 64px | `--spacing-16` |
| 24 | 96px | `--spacing-24` |
| 36 | 144px | `--spacing-36` |
| section-y | clamp(72px, 10vw, 144px) | `--section-y` |
| gutter | clamp(20px, 5vw, 48px) | `--gutter` |

### Border Radius

| Name | Value | Token |
| --- | --- | --- |
| none（base） | 0px | `--radius` |
| sm | 2px | `--radius-sm` |

| Element | Value |
| --- | --- |
| 卡片 / 画框 / 色块 | 0 + 右上折角 36px（`--fold-lg`） |
| 按钮 / 章节号方块 | 0 + 右上折角 18px（`--fold-md`） |
| 徽标 / 小按钮 | 0 + 右上折角 10px（`--fold-sm`） |
| 输入框 | 2px（sm），无折角——可输入的东西不「折」 |

### Fold & Crease（折角与折痕）

| Name | Value | Token | 用法 |
| --- | --- | --- | --- |
| fold-sm / md / lg | 10 / 18 / 36px | `--fold-*` | `clip-path` 切掉右上角，同尺寸方格内画一个纸背三角 |
| crease-h | clamp(48px, 7vw, 112px) | `--crease-h` | 两个色块分区之间的斜折痕高度；折痕右侧 42% 处起一块背光 / 受光三角面 |

### Shadows

只有硬位移，没有模糊、没有透明度。被 `clip-path` 裁过的元素用同形伪元素位移来做纸影。

| Name | Value | Token |
| --- | --- | --- |
| offset-sm | 4px（按钮、输入框 focus） | `--offset-sm` |
| offset-md | 8px（卡片、产品行、流程带） | `--offset-md` |
| offset-lg | 16px（插画画框、联系区折纸箭头） | `--offset-lg` |
| block-sm | `4px 4px 0 0 #0e1a3a` | `--shadow-block-sm` |
| block-md | `8px 8px 0 0 #0e1a3a` | `--shadow-block-md` |

### Motion

| Name | Value | Token |
| --- | --- | --- |
| ease-fold | `cubic-bezier(0.2, 0.9, 0.25, 1)` | `--ease-fold` |
| duration-press | 140ms（按钮抬起 / 压下） | `--duration-press` |
| duration-fold | 320ms（箭头位移、卡片纸影拉开、导航下划条） | `--duration-fold` |

只动 transform。插画入场用 `animation-timeline: view()` 从 scale 1.07 落到 1（包在 `@supports` 里，终态就是默认态）。`prefers-reduced-motion` 下全部关闭。

### Layout

- **Section gap:** 72–144px（`--section-y`），色块分区之间再加一道 48–112px 折痕
- **Card padding:** 28–32px（移动端 24px）
- **Element gap:** 32px 栅格间距；卡片之间 48px（要给 8px 纸影留位置）
- **Max content width:** 1240px + 两侧 gutter；色块与折面一律出血到视口边缘

## Components

### Primary Button

**Role:** 主 CTA（联系学院顾问）
面 `--color-orange` + 字 `--color-ink`，`min-height: 52px`，`padding: 0 28px 0 24px`，`font: 700 16px`。右上 18px 折角，纸背 `--color-orange-deep`；身后一块同形墨蓝纸影位移 4px。hover：整体 `translate(-2px,-2px)`、纸影拉到 6px、箭头 ↗ 再走 2px；active：压到纸影上（位移 4px、纸影归零）；disabled：深米底灰蓝字、无纸影、`cursor:not-allowed`；focus-visible：3px 实线环。墨蓝 / 钴蓝底上纸影改用 `--color-cobalt`。

### Ink Button / Paper Button

**Role:** 橘橙分区里的主次按钮
橘橙底上不能再放橘橙按钮：主按钮换成墨蓝面米白字、纸背与纸影用钴蓝；次按钮（复制客服链接）是白卡面墨蓝字、墨蓝纸影。两个按钮同高同折角，只靠面色区分主次，不用描边按钮——`clip-path` 的斜边画不出描边。

### Cobalt Button

**Role:** 米白分区里的第二主张
钴蓝面白字，纸背 `--color-cobalt-deep`。同一视图里橘橙主按钮最多一个，其余用钴蓝或文字链。

### Text Link

**Role:** 章节内「了解…… ↗」
700 字重、2px 下划线、offset 6px，hover 下划线加粗到 4px、箭头斜向位移 3px。触控高度 44px。墨蓝底上用 `--color-orange-lit`。

### Emphasis Strip（强调词垫条）

**Role:** 标题里的强调词（你的能力 / 起点 / 一起做 / “我来做” / 继续对话）
`display:inline-block` 的色条，右端斜切 0.24em，像一条裁下来的色纸压在字下面。配色按所在分区取「对面」：米白底→钴蓝条白字；钴蓝底→橘橙条墨蓝字；橘橙底→墨蓝条米白字。不用渐变字、不用下划线波浪。

### Chapter Tile（章节号方块）

**Role:** 三个叙事章节的 01 / 02 / 03
64×64 折角方块，Bricolage 800 / 26px。只给真实有顺序的内容编号（三章节、共学五步）。

### Plate（章节插画框）

**Role:** 承载暖色纸感插画，解决它与高饱和色块的冲突
四层：① 向右下错开 16px 的实色垫块（米白区钴蓝、橘橙区墨蓝、钴蓝区橘橙）；② 10px 白卡衬纸，右上 36px 折角；③ 4:3 插画，左下角压一枚 40–84px 的叠印三角（取分区对比色）；④ 衬纸下沿 48px 图注条，Space Mono，`EXPERIENCE ｜ 经验，值得新的可能。`。插画从不裸贴在色块上。

### Journal Card（期刊卡）

**Role:** 观点与动态
白卡 + 36px 折角 + 8px 位移色块（三张分别用钴蓝 / 橘橙 / 墨蓝，只是装饰，不代表分类）。版式是一大两小：左侧主卡 7 栏（16:10 封面在上），右侧两张横排卡 5 栏（34% 封面 + 文字）。hover 时卡片抬 3px、色块拉到 14px。米色底的半人马封面用 `mix-blend-mode:multiply` 融进卡底。

### Accordion Strip（共学五步 · 经折流程带）

**Role:** 本范式的签名组件，只用于真实顺序流程
五列等宽面板，奇数面板 `polygon(0 0,100% 30px,100% calc(100% - 30px),0 100%)`，偶数面板镜像，颜色按本色 / 背光交替，最后一步换橘橙墨蓝字；父级 `filter: drop-shadow(8px 8px 0 ink)` 给整条纸带一个硬影。数字 56px 在上、标题与说明压底。≤960px 改成竖排，面板右沿左右交替斜切 18px。

### Product Row（产品下载行）

**Role:** 知君 / 万象
钴蓝分区里的两张白卡，36px 橘橙纸背折角 + 8px 墨蓝纸影。左：产品名 34px/900 + 副链；右：禁用态小按钮「下载知君 ↓」+ mono 小字「下载暂未开放」。

### Quote Block（院长寄语）

**Role:** 引文
墨蓝整段铺色，右侧出血两块钴蓝折面。引文 28–50px/900 米白字，开引号用 `text-indent:-0.5em` 悬挂；署名区是一枚米白折角方块装 logo + 40px 名字。不放头像占位。

### Contact Banner（联系横幅）

**Role:** 页尾行动区
橘橙整段铺色，左下一块背光三角面；H2 38–80px 墨蓝；右侧一枚由 6 个三角面拼成的折纸箭头 ↗（白卡 / 钴蓝 / 钴蓝背光 / 墨蓝），带 16px 橘橙背光硬影——箭头就是全站 ↗ 的放大版。

### Input Field

**Role:** 文本输入（咨询表单预留）
白卡底、2px 墨蓝边、`--radius-sm`、高 52px。focus：`translate(-2px,-2px)` + `--shadow-block-sm`；error：纸影换橘橙 + 下方三角标提示（墨蓝字，不用橘字——橘橙在米白上只有 2.6:1）；disabled：深米底、虚线边。

### Badge

**Role:** 分类与状态标注
24px 高、10px 折角的小色签，12px/700。钴蓝（默认）/ 橘橙 / 墨蓝 / 深米（弱）。不用圆角胶囊。

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | background | `#f6f1e6` | 页面画布、页头、第一章、共学五步 |
| 1 | secondary | `#ebe3d2` | 观点与动态分区；米白区里的背光折面 |
| 2 | card | `#fffdf7` | 卡片、衬纸、输入框——永远带折角或 2px 边 |
| B | cobalt block | `#1450c8` | 首屏左半、第三章；内含 lit / deep 折面 |
| O | orange block | `#f47216` | 第二章、联系区、台座；内含 lit / deep 折面 |
| I | ink block | `#0e1a3a` | 首屏底栏、院长寄语、页脚 |

层级不靠阴影深浅，靠「哪张纸压在哪张纸上」：色块 → 折面 → 位移垫块 → 白卡。

## Do's and Don'ts

### Do

- 颜色整段铺。一个分区要么是米白，要么整段钴蓝 / 橘橙 / 墨蓝；页面滚下来的节奏是 蓝+米 → 米 → 橘 → 蓝 → 米 → 深米 → 墨 → 橘 → 墨。
- 每个彩色分区至少放一块出血的受光或背光三角面，让它读起来是「折过的纸」而不是一块平涂。
- 橘橙上只放墨蓝字，钴蓝上只放白字或 `--color-cobalt-muted-foreground`；次要文字压到折面上之前先核对对比度。
- 容器右上角折角，纸背取该容器的背光色或所在分区的对比色；折角尺寸只用 10 / 18 / 36 三档。
- 阴影只用 4 / 8 / 16px 硬位移；卡片之间至少留 48px，别让纸影撞到邻居。
- 强调词用斜切垫条，一条标题只垫一个词。
- 暖色插画先裱白卡衬纸再上色块。
- 编号只给三章节和共学五步。

### Don't

- 不要加第三种彩色。绿色成功、红色错误、紫色渐变都不属于这套；错误提示用橘橙三角标 + 墨蓝字。
- 不要在橘橙上放白字（2.9:1），也不要把橘橙字放在米白或钴蓝上。
- 不要给色块加圆角、模糊阴影、描边发光或渐变；`linear-gradient` 只允许用来画硬边折角。
- 不要让折面斜边穿过正文段落的中线——折面待在角落和边缘。
- 不要做吉祥物、表情、彩色圆点、波浪线；这不是儿童产品，几何只有直线和 45° / 任意斜线，没有圆。
- 不要用 `#000`，不要用 Inter / Roboto / Arial。
- 不要把三张期刊卡排成等宽一排；保持一大两小。
- 不要编造数字、客户 logo、学员评价。

## Imagery

主视觉只有一个：半人马折纸抠图（`academy-centaur-cutout.webp`），站在橘橙台座上——台座顶面用受光橘、正面用本色橘并承载图注、左端一小块背光橘收边，三个面就是一次完整的「三面色」示范。因为马身本身是蓝色，抠图不放在钴蓝本色上（会糊），只放在米白、墨蓝或让尾巴轻轻搭到背光蓝上。三张场景插画是暖色纸感风格，色相（陶土、藏青、米）与品牌色相近但饱和度低很多，直接贴会显脏，所以一律走 Plate 四层画框；期刊封面则裁成 16:10 / 竖条，靠白卡与位移色块隔开。米色底版半人马图只在白卡 / 米白面上用 multiply。除此之外的图形全部是 CSS `clip-path` 三角面和一枚内联 SVG 折纸箭头；图标只有文字箭头 ↗ → ↓ 和三角折标，不引入图标库。

## Layout

1240px 内容宽 + 12 栏 32px 间距；色块、折面、折痕出血到视口。页头 76px，米白底 + 2px 墨蓝底边，sticky、不透明、无模糊。首屏不是居中构图：左侧钴蓝大色块从左上铺到 60%→47% 的斜边（旁边贴一条背光蓝折面），H1 左对齐压在上面；右侧米白区里半人马站在出血到右缘的橘橙台座上；最底一条 56px 墨蓝底栏放品牌主张。首屏高度 `min(780px, 100svh - 76px)`。三个章节左右交替（文 5 栏 / 图 6 栏），分区之间用折痕过渡并左右翻转方向。共学五步是整行流程带；观点与动态 7+5 不对称；院长寄语 4+7；联系区 8+4。≤960px 全部改单栏：首屏变成「钴蓝文字块（下沿斜切）→ 半人马与台座 → 墨蓝底栏」，导航收进 44px 方形菜单钮，展开为墨蓝整块面板；≤520px 按钮撑满宽度。

## Agent Prompt Guide

Quick Color Reference:

```
background (paper): #f6f1e6
foreground / ink:   #0e1a3a
card:               #fffdf7
secondary (paper-2):#ebe3d2
muted-foreground:   #4a5470
cobalt lit/base/deep: #2a66dc / #1450c8 / #0d3a96   (text on it: #ffffff, muted #dbe6fc)
orange lit/base/deep: #ffb070 / #f47216 / #e0640c   (text on it: #0e1a3a only)
on-ink muted:       #b3bdd6
```

Example Component Prompts:

1. Create a primary CTA: square button, `background: var(--color-orange)`, text `var(--color-ink)` 700 16px, min-height 52px, padding 0 28px 0 24px, radius 0. Cut the top-right corner with `clip-path: polygon(0 0, calc(100% - 18px) 0, 100% 18px, 100% 100%, 0 100%)` and paint an 18×18 hard-stop triangle in `var(--color-orange-deep)` at that corner as the paper back. Put an identical ink-colored shape behind it offset 4px/4px (pseudo-element, because clip-path eats box-shadow). Hover: translate(-2px,-2px), shadow to 6px; active: translate(4px,4px), shadow 0. Ease `cubic-bezier(0.2,0.9,0.25,1)`, 140ms.
2. Create a chapter section on a full-bleed orange block: background `var(--color-orange)`, all text `var(--color-ink)`, one bleeding triangle facet in `var(--color-orange-lit)` at the top-right and one in `var(--color-orange-deep)` at the bottom-left. H2 in `--font-display` 900 at `--text-heading-lg`; wrap the emphasis word in an inline-block ink strip with paper-colored text and a slanted right end. The illustration goes in a Plate: 16px offset ink block → 10px card-white mat with a 36px folded corner → 4:3 image with a cobalt triangle tab at bottom-left → mono caption bar.
3. Create the five-step accordion strip: a 5-column grid, each `li` min-height 340px; odd panels `clip-path: polygon(0 0,100% 30px,100% calc(100% - 30px),0 100%)` in `var(--color-cobalt)`, even panels mirrored in `var(--color-cobalt-deep)`, last panel `var(--color-orange)` with ink text. Number 56px display-800 at top, title 24px/900 and one-line description pinned to the bottom. Parent gets `filter: drop-shadow(8px 8px 0 var(--color-ink))`. Below 960px stack vertically with alternating slanted right edges.

## Similar Brands

调研方式：直接抓取各站首页 HTML 与主样式表，用正则统计色值、`font-family`、`border-radius`、`box-shadow` 的出现频次（2026-09-17）。

- **Gumroad**（gumroad.com，design-*.css）— 读到：`--color-pink:#ff90e8`、`--color-orange:#ffc900`、底色 `#f4f4f0`、深色 `#242423`；字体 ABC Favorit；圆角只有 `.25rem`；阴影是 `.25rem .25rem 0 currentColor` 的无模糊硬位移，边框 `solid .0625rem`。借了：**硬位移纸影（4px → `--offset-sm`）**、hover 抬起 / active 压下的按钮物理、亮色底上坚持放深色字而不是白字。没借：粉黄多色与 1px 描边——我们用折角代替描边。
- **Headspace**（headspace.com）— 读到：蓝 `#0040ea` / `#0061ef` 与黄 `#ffce00` 大面积对撞，暖白 `#f9f4f2`，正文 `#2d2c2b` / `#44423f`（不用纯黑），字体 Apercu，按钮阴影 `0 .125rem 0`（同样无模糊），圆角 2rem。借了：**高饱和蓝 + 暖色对撞、整段铺色、暖白而非纯白的画布、正文不用纯黑**。没借：2rem 大圆角和圆脸插画——那是它「亲切」的来源，也是我们要避开的「幼」。
- **Pitch**（pitch.com）— 读到：Mark Pro Bold 做标题、Space Mono 做标注，深紫 `#280f62` / `#5318eb` 整屏铺底，圆角 4 / 8 / 24px。借了：**厚重几何无衬线标题 + 等宽小字标注的双声部**（→ Bricolage Grotesque 800 + Space Mono），以及深色整屏分区做节奏停顿（→ 墨蓝院长寄语）。
- **Mailchimp**（mailchimp.com，common / critical css）— 读到：胡椒黑 `#231e15`、暖灰 `#efeeea`、蜜黄 `#e7b75f`，阴影色是带色相的 `rgba(35,30,21,.15)` 而不是中性黑；标题 Means、正文 Graphik。借了：**中性色全部带品牌色相**（墨蓝代替黑、灰蓝次文代替中性灰）。没借：衬线标题与手绘插画。
- **Figma**（figma.com）— 读到的只有自有字体 figmaSans / figmaMono 的声明（样式内联在 JS 里，未取到色值）。借的是可见的版式习惯：首页按功能切成整屏色块、每屏换底色。此项未能落到具体数值，仅作方向参考。
- **Bauhaus 海报**（Herbert Bayer / Joost Schmidt 一路）— 借了：斜线分割画面、两种原色 + 米纸 + 黑（此处为墨蓝）的限色原则、文字压在色块上的排法。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 画布与中性 */
  --color-background: #f6f1e6;
  --color-foreground: #0e1a3a;
  --color-card: #fffdf7;
  --color-card-foreground: #0e1a3a;
  --color-secondary: #ebe3d2;
  --color-secondary-foreground: #0e1a3a;
  --color-muted: #ebe3d2;
  --color-muted-foreground: #4a5470;
  --color-border: #0e1a3a;
  --color-input: #0e1a3a;
  --color-ring: #0e1a3a;
  --color-ring-inverse: #ffb070;

  /* Colors — 钴蓝三面（受光 / 本色 / 背光） */
  --color-cobalt-lit: #2a66dc;
  --color-cobalt: #1450c8;
  --color-cobalt-deep: #0d3a96;
  --color-cobalt-foreground: #ffffff;
  --color-cobalt-muted-foreground: #dbe6fc;

  /* Colors — 橘橙三面（受光 / 本色 / 背光） */
  --color-orange-lit: #ffb070;
  --color-orange: #f47216;
  --color-orange-deep: #e0640c;
  --color-orange-foreground: #0e1a3a;

  /* Colors — 墨蓝 */
  --color-ink: #0e1a3a;
  --color-ink-foreground: #f6f1e6;
  --color-ink-muted-foreground: #b3bdd6;

  /* Colors — 语义别名 */
  --color-primary: #f47216;
  --color-primary-foreground: #0e1a3a;
  --color-brand: #1450c8;
  --color-brand-foreground: #ffffff;
  --color-disabled-bg: #ebe3d2;
  --color-disabled-text: #4a5470;

  /* Typography — Font Families */
  --font-display:
    'Bricolage Grotesque', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', 'Avenir Next', 'Trebuchet MS', sans-serif;
  --font-sans:
    'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei',
    'Avenir Next', 'Segoe UI', system-ui, sans-serif;
  --font-mono:
    'Space Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    'PingFang SC', 'Microsoft YaHei', monospace;

  /* Typography — Scale */
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 19px;
  --text-subheading: 24px;
  --text-heading: clamp(28px, 3vw, 40px);
  --text-heading-lg: clamp(36px, 4.8vw, 68px);
  --text-display: clamp(44px, 7.2vw, 104px);

  /* Line Height & Tracking */
  --leading-display: 1.08;
  --leading-heading: 1.16;
  --leading-body: 1.75;
  --tracking-display: -0.02em;
  --tracking-heading: -0.01em;
  --tracking-body: 0em;
  --tracking-mono: 0.08em;

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
  --spacing-36: 144px;
  --section-y: clamp(72px, 10vw, 144px);
  --gutter: clamp(20px, 5vw, 48px);
  --container: 1240px;

  /* Border & Radius — 方正，折角代替圆角 */
  --border-width: 2px;
  --radius: 0px;
  --radius-sm: 2px;

  /* Fold — 折角与折痕 */
  --fold-sm: 10px;
  --fold-md: 18px;
  --fold-lg: 36px;
  --crease-h: clamp(48px, 7vw, 112px);

  /* Shadows — 只有硬投影（叠纸位移），没有模糊 */
  --offset-sm: 4px;
  --offset-md: 8px;
  --offset-lg: 16px;
  --shadow-block-sm: 4px 4px 0 0 #0e1a3a;
  --shadow-block-md: 8px 8px 0 0 #0e1a3a;

  /* Motion */
  --ease-fold: cubic-bezier(0.2, 0.9, 0.25, 1);
  --duration-press: 140ms;
  --duration-fold: 320ms;
}
```

### Tailwind v4

```css
@theme {
  --color-background: #f6f1e6;
  --color-foreground: #0e1a3a;
  --color-card: #fffdf7;
  --color-card-foreground: #0e1a3a;
  --color-secondary: #ebe3d2;
  --color-secondary-foreground: #0e1a3a;
  --color-muted: #ebe3d2;
  --color-muted-foreground: #4a5470;
  --color-border: #0e1a3a;
  --color-input: #0e1a3a;
  --color-ring: #0e1a3a;
  --color-ring-inverse: #ffb070;
  --color-cobalt-lit: #2a66dc;
  --color-cobalt: #1450c8;
  --color-cobalt-deep: #0d3a96;
  --color-cobalt-foreground: #ffffff;
  --color-cobalt-muted-foreground: #dbe6fc;
  --color-orange-lit: #ffb070;
  --color-orange: #f47216;
  --color-orange-deep: #e0640c;
  --color-orange-foreground: #0e1a3a;
  --color-ink: #0e1a3a;
  --color-ink-foreground: #f6f1e6;
  --color-ink-muted-foreground: #b3bdd6;
  --color-primary: #f47216;
  --color-primary-foreground: #0e1a3a;
  --color-brand: #1450c8;
  --color-brand-foreground: #ffffff;
  --color-disabled-bg: #ebe3d2;
  --color-disabled-text: #4a5470;
  --font-display:
    'Bricolage Grotesque', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', 'Avenir Next', 'Trebuchet MS', sans-serif;
  --font-sans:
    'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei',
    'Avenir Next', 'Segoe UI', system-ui, sans-serif;
  --font-mono:
    'Space Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    'PingFang SC', 'Microsoft YaHei', monospace;
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 19px;
  --text-subheading: 24px;
  --text-heading: clamp(28px, 3vw, 40px);
  --text-heading-lg: clamp(36px, 4.8vw, 68px);
  --text-display: clamp(44px, 7.2vw, 104px);
  --radius: 0px;
  --radius-sm: 2px;
  --shadow-block-sm: 4px 4px 0 0 #0e1a3a;
  --shadow-block-md: 8px 8px 0 0 #0e1a3a;
  --ease-fold: cubic-bezier(0.2, 0.9, 0.25, 1);
}
```
