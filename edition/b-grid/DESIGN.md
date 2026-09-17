# 半人马AI学院 · 发丝网格 — Style Reference

> 白纸上铺满钴蓝发丝线，一格放字，一格放半人马；往下滚，半人马走进黑场，整页变成一本可以点开的目录。

**Theme:** light（纸白为主；开幕终态与联系区为纯黑场，第三章与页脚为橄榄墨面）

这一版以 ③ Dropbox Brand 为骨架：纸白画布（#f8f8f3）上，1px 钴蓝发丝线（#cddff2）按 12.2 / 38.9 / 8.9 / 30 / 10 的不等分比例把页面切成五栏，全站所有文字、图片、按钮都从这几条线起笔，线本身就是装饰。首屏几乎是空的：左边一格放钴蓝 H1「让 AI 成为 / 你的能力。」，右边一格放半人马，其余格子只留标注小字。马身钴蓝 #0c6ccc 是唯一的界面强色，只落在 H1、强调词、主按钮、书脊色条和一块目录瓦片上；logo 的橘橙不进界面，只留在 logo 与插画里。灰阶全部带同一个橄榄底调（④ 的做法），近黑是 #20211a 而不是中性黑。字体分三个声部：Noto Sans SC 用 560 / 860 这样的非整百字重并横向放宽到 104% 来喊标题，Noto Serif SC 讲叙述句，Geist Mono 做标签与度量标注。面一律直角（0–2px），能按的一律胶囊，几乎不用阴影，层次靠发丝线和底色硬切。签名记忆点是「滑动放大」：首屏右格里的半人马以 0.5 倍起步，随滚动放大到居中的 760px 终态，同时白纸网格淡出、黄金分割构图线在黑场里展开，放完后整页释放进八格目录。

## Tokens — Colors

| Name       | Value     | Token                        | Role                                              |
| ---------- | --------- | ---------------------------- | ------------------------------------------------- |
| 纸白       | `#f8f8f3` | `--color-paper`              | 全站画布，带一点橄榄暖意，容得下暖色插画          |
| 橄榄浅纸   | `#ecece3` | `--color-paper-2`            | 目录瓦片、共学五步带、引语右半                    |
| 橄榄墨     | `#20211a` | `--color-ink` / `--color-foreground` | 正文；第三章、院长左半、页脚的深色面      |
| 深面二层   | `#2b2c24` | `--color-ink-2`              | 深色面上的产品卡、深底按钮悬停                    |
| 开幕黑     | `#000000` | `--color-black`              | 只给首屏黑场终态与联系区，正文不用                |
| 马身钴蓝   | `#0c6ccc` | `--color-accent`             | 唯一界面强色；纸白上 4.89:1，只用于 ≥16px 文字与色块 |
| 深钴蓝     | `#0a56a6` | `--color-accent-deep`        | 悬停、按下；纸白上 6.81:1                         |
| 夜钴蓝     | `#5b9be0` | `--color-accent-on-dark`     | 深色面上的强调词与小标签；橄榄墨上 5.57:1         |
| 钴蓝上文字 | `#f8f8f3` | `--color-on-accent`          | 钴蓝色块上的文字，4.89:1                          |
| 深底文字   | `#f8f8f3` | `--color-on-dark`            | 深色面上的正文                                    |
| 橄榄灰     | `#63645a` | `--color-muted`              | 次要文字；纸白 5.63:1、橄榄浅纸 5.05:1            |
| 浅橄榄灰   | `#a9aa9c` | `--color-muted-on-dark`      | 深色面次要文字；橄榄墨 6.89:1、黑 8.92:1          |
| 钴蓝发丝   | `#cddff2` | `--color-hairline`           | 网格线，只做结构，不承载信息                      |
| 橄榄分隔   | `#d9d9cc` | `--color-rule`               | 列表、步骤格之间的分隔；瓦片悬停底                |
| 深面分隔   | `#3a3b32` | `--color-rule-dark`          | 深色面上的网格线与分隔                            |
| 构图线     | `#34352d` | `--color-construct`          | 预留给深色面上的构图线（当前实现用浅橄榄灰 30% 透明度） |
| 禁用底     | `#e2e2d8` | `--color-disabled-bg`        | 「下载知君 / 下载万象」禁用胶囊                   |
| 禁用字     | `#5a5b51` | `--color-disabled-fg`        | 禁用胶囊文字，禁用底上 5.2:1                      |
| 焦点环     | `#0c6ccc` | `--color-focus`              | `:focus-visible` 2px 外框                         |

钴蓝是稀缺资源：一屏之内最多一块钴蓝色块（书脊条算一块），其余只准出现在字上。橘橙 `#f07800` 一带只存在于 logo 与插画，不写进任何 token。

### 深浅面配对（本站没有柔和语义色，改用成对的面）

| Name     | Background | Text      | 次要文字  | 强调      |
| -------- | ---------- | --------- | --------- | --------- |
| 纸面     | `#f8f8f3`  | `#20211a` | `#63645a` | `#0c6ccc` |
| 浅纸面   | `#ecece3`  | `#20211a` | `#63645a` | 只用色块，不用钴蓝小字（4.38:1 不达标） |
| 墨面     | `#20211a`  | `#f8f8f3` | `#a9aa9c` | `#5b9be0` |
| 黑场     | `#000000`  | `#f8f8f3` | `#a9aa9c` | `#5b9be0` |
| 钴蓝面   | `#0c6ccc`  | `#f8f8f3` | `#f8f8f3` | 无        |

### 线（替代图表色）

| Name       | Value                         | 用在哪                                      |
| ---------- | ----------------------------- | ------------------------------------------- |
| 网格竖线   | `#cddff2` 1px                 | 12.2% / 51.1% / 60% / 90% 四条，贯穿纸面各段 |
| 首屏横线   | `#cddff2` 1px                 | 首屏 7% / 67% / 88% 三条                    |
| 深面竖线   | `#3a3b32` 1px                 | 第三章                                      |
| 构图线     | `#a9aa9c` × 30%               | 黑场：两条对角线、三条竖线、两个大圆、三级方格 |
| 细线框     | `#a9aa9c` × 45% / 100%        | 黑场里的半人马画框；联系区的居中锁定框      |

## Tokens — Typography

### Noto Sans SC — 中文展示与界面 · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, system-ui
- **Weights:** 可变 100–900；实际只用 380 / 420（正文）/ 560（标题）/ 860（强调词）
- **Sizes:** 12, 14, 15, 16, 18, 22–30（瓦片）, 34–60（H2）, 44–92px（H1）
- **Line height:** 展示 1.06 / 标题 1.12 / 正文 1.75
- **Letter spacing:** 标题 -0.02em（中文下限，不再收紧）/ 正文 0
- **Width:** 标题行 `transform: scaleX(1.04)`，即中文排版里的「平体 4%」，替代 ③ 的 wdth 108
- **Role:** H1、H2、瓦片标题、按钮、正文。回退到苹方时 560 会落到 Semibold，版式靠字号撑住不塌

### Noto Serif SC — 中文叙述声部 · `--font-serif`

- **Substitute:** Songti SC, STSong, SimSun
- **Weights:** 500, 700
- **Sizes:** 15, 18, 19, 22, 28–48px（引语）
- **Line height:** 叙述 1.55 / 引语 1.32
- **Role:** 副标题、章节说明、图注、五步小标题带、院长引语、文章标题

### Bricolage Grotesque — 拉丁展示 · `--font-display-latin`

- **Substitute:** Helvetica Neue, PingFang SC
- **Weights:** 可变 200–800，只用 540
- **Axes:** `wdth` 100（该字族上限，即「最宽」）、`opsz` 96
- **Sizes:** 64–132px（编号 01–05、03）, 48–118px（HUMAN × AI）
- **Letter spacing / Line height:** -0.045em / 0.9（拉丁字可以按 ②④ 收紧）
- **Role:** 只给阿拉伯数字编号与 HUMAN × AI 这类拉丁大字

### Newsreader — 拉丁叙述 · `--font-serif-latin`

- **Substitute:** Georgia, Songti SC
- **Weights:** 400–500
- **Role:** 引号字形（“ ”）与叙述句里的拉丁字母，排在 Noto Serif SC 之前

### Geist Mono — 标签与度量 · `--font-mono`

- **Substitute:** ui-monospace, SFMono-Regular, Menlo
- **Weights:** 400, 500
- **Sizes:** 10px（书脊英文）, 11px（钴蓝度量标注）, 12px（标签）
- **Letter spacing:** 0.06em，大写
- **Role:** 眉标、图片挂签、日期、`§01` 书眉、`WGHT 560` 这类度量标注

### Type Scale

| Role        | Size                           | Line Height | Letter Spacing | Token             |
| ----------- | ------------------------------ | ----------- | -------------- | ----------------- |
| wordmark    | clamp(56px, 16.4vw, 250px)     | 1           | -0.03em        | `--text-wordmark` |
| numeral     | clamp(72px, 8.4vw, 132px)      | 0.9         | -0.045em       | `--text-numeral`  |
| display     | clamp(44px, 5.9vw, 92px)       | 1.06        | -0.02em        | `--text-display`  |
| h2          | clamp(34px, 4vw, 60px)         | 1.12        | -0.02em        | `--text-h2`       |
| quote       | clamp(28px, 3.2vw, 48px)       | 1.32        | 0              | `--text-quote`    |
| tile        | clamp(22px, 1.9vw, 30px)       | 1.15        | -0.02em        | `--text-tile`     |
| h3          | 28px                           | 1.35        | 0              | `--text-h3`       |
| narrative   | 22px                           | 1.55        | 0              | `--text-narrative`|
| body        | 16px                           | 1.75        | 0              | `--text-body`     |
| sm          | 14px                           | 1.6         | 0              | `--text-sm`       |
| label       | 12px mono                      | 1.4         | 0.06em         | `--text-label`    |

规律照 ② 与 ④：字越大行越贴、距越紧；中文到 -0.02em 为止，行高不低于 1.06。字号只跳档不插值，44→60→92 之间没有中间级。

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 4px`）

**Density:** 画廊级留白（③ 的首屏一格有字、其余全空）

### Spacing Scale

| Name       | Value  | Token             |
| ---------- | ------ | ----------------- |
| 瓦片间距   | 10px   | `--tile-gap`      |
| 移动页边   | 16px   | `--gutter`        |
| 格内边距   | 24px   | `6 × --spacing`   |
| 五步上空   | 96px   | `--space-steps`   |
| 第三章上空 | 120px  | `--space-ch3`     |
| 第一章上空 | 160px  | `--space-ch1`     |
| 观点上空   | 200px  | `--space-journal` |
| 第二章上空 | 240px  | `--space-ch2`     |

章节上空每章不同（④ 的 11vh–35vh 节奏），纸面章节比深色面章节留得更多。

### Border Radius

| Name  | Value  | Token            |
| ----- | ------ | ---------------- |
| none  | 0px    | `--radius-none`  |
| face  | 2px    | `--radius-face`  |
| pill  | 999px  | `--radius-pill`  |

| Element          | Value        |
| ---------------- | ------------ |
| 图片、分区、面   | 0            |
| 瓦片、产品卡、输入框 | 2px      |
| 按钮、徽标、滑杆控件 | full     |

两极之间没有 6px、8px、12px。

### Shadows

| Name | Value                                | Token           |
| ---- | ------------------------------------ | --------------- |
| none | `none`                               | `--shadow-none` |
| ring | `0 0 0 1px rgba(32, 33, 26, 0.14)`   | `--shadow-ring` |

全站没有投影。唯一的「影」是半人马抠图自带的地面投影。

### Motion

| Name       | Value                               | Token          |
| ---------- | ----------------------------------- | -------------- |
| ease-quick | `cubic-bezier(0.2, 0.1, 0, 1)`      | `--ease-quick` |
| ease-stage | `cubic-bezier(0.72, 0.16, 0.19, 0.96)` | `--ease-stage` |
| dur-fast   | 0.15s                               | `--dur-fast`   |
| dur-base   | 0.3s                                | `--dur-base`   |

- 悬停只换底色与文字色（③ 的做法），按下 `scale(.97)`。
- 滑动放大用 CSS scroll-driven animation：`animation-timeline: scroll(root)`，整段写在 `@media (min-width:768px) and (prefers-reduced-motion:no-preference)` 与 `@supports (animation-timeline: scroll())` 里；`animation-timeline` 写在 `animation` 简写之后；只动 transform 和 opacity。
- 时间轴（额外滚动距离 E = `min(100vh, 900px)`）：半人马 0 → 0.82E 从 `translate(+25vw, -13% 钉住高) scale(.5)` 到 `translate(-50%,-50%) scale(1)`；首屏网格 0.12E → 0.42E 淡出、黑场同步淡入；构图线 0.25E → 0.9E 从 scale(.72) 展开；画框 0.55E → 0.9E；HUMAN × AI 与两侧小字 0.6E → 0.95E 上浮。
- 不支持或减少动效时：不钉住，首屏网格与黑场终态上下排开，半人马直接以 760px 终态放在黑场里。

### Layout

- **栅格:** 五栏 `12.2fr 38.9fr 8.9fr 30fr 10fr`，无栏距，内容在格内留 24px；1440 宽下栏线落在 176 / 736 / 864 / 1296px
- **首屏:** 钉住高度 `min(100svh - 56px, 844px)`，行高 7% / 60% / 21% / 12%
- **钉住段额外滚动:** `min(100vh, 900px)`，约 100vh，低于 120vh 上限
- **半人马终态宽:** `min(760px, 56vw)`，抠图原图 1448px，2 倍屏下仍有 1.9 倍余量
- **目录板:** 4 栏 `1fr 1.8fr 1.4fr 1fr` × 6 行，高 `min(880px, max(720px, 100svh))`，外边距与间距都是 10px
- **Section gap:** 96–240px，逐章不同
- **断点:** 1100（目录板改 3 栏）/ 900（导航收进「目录 +」）/ 767（全部单栏，网格线只剩左右两条 16px 线）

## Components

### 书脊顶栏

**Role:** 全站顶栏，照 ② 的「黑方块字标 + 满高色条 + 纯文字导航」
高 56px，sticky。左块 `bg-ink`，logo 30×40 + 「半人马AI学院」16px/700 + `CENTAUR AI ACADEMY` 10px mono；宽度 ≥1101px 时锁定为 12.2%，正好压在第一条网格线上。中间钴蓝满高色条宽 38.9%，右对齐「联系学院顾问 ↗」，右边缘对齐第二条网格线。右侧四个纯文字导航 15px/500，间距 40px。≤900px 时导航收进「目录 +」按钮，展开为整宽下拉，每行 48px。

### Primary Pill

**Role:** 主 CTA「联系学院顾问 ↗」
`bg-accent` + `text-on-accent`，`border-radius: 999px`，高 48px，左右 24px，16px/600。hover `bg-accent-deep`；active `scale(.97)`；focus 2px 钴蓝外框、3px 间隙。每屏最多一枚。

### Line Pill（深底）

**Role:** 次按钮「复制客服链接」
透明底 + 1px `muted-on-dark` 边，文字 `on-dark`。hover 边变 `on-dark`、底变 `ink-2`。点击后下方 `role="status"` 行显示「已复制客服链接」。

### Disabled Pill

**Role:** 「下载知君 ↓ / 下载万象 ↓」
`bg-disabled-bg` + `text-disabled-fg`，`aria-disabled="true"`，无指针事件；右侧 14px 灰字「下载暂未开放」。

### 文字链与行链

**Role:** 次级跳转
文字链：16px/600，1px 下划线离字 10px，hover 变钴蓝。行链（照 ② 的「Get notified」）：上方 1px 实线、高 52px、左文字右箭头、最宽 454px。

### 目录瓦片

**Role:** 首页即目录，照 ③ 八宫格
`border-radius: 2px`，内边距 22/24px；左上标题（tile 字号，560，平体 104%）+ 下方 mono 标签，右上 ↘ 箭头（hover 时右下移 3px），右下放图形或插画。三种底：橄榄浅纸（hover 变 `rule`）、橄榄墨、钴蓝（整板只有一块）。八格分别是：共学五步 / 01 / 02 / 03 三章 / 院长寄语 / 观点与动态 / 从这里开始 / logo 小方块。

### 章节插画框

**Role:** 全站唯一的图片处理
直角、无滤镜、无阴影、无圆角；左下角挂一块与所在面同色的等宽标签（`EXPERIENCE`、`LEARN TOGETHER`、`MAKE IT REAL`），图注的中文句子放在图外。第二章把同一幅插画放大 1.9 倍取两处局部，拼成「一大两小」（③ s08 的三图组合）。

### 产品行（知君 / 万象）

**Role:** 第三章里的两件工具
深色面上的 `ink-2` 卡，2px 圆角，内边距 22/24px；顶部夜钴蓝描边胶囊写产品名，下面 24–32px 标题链接「让积累参与思考 ↗」，底部禁用胶囊 + 说明。两张上下叠，和左侧插画组成 ③ s10 的「一大两小」。

### 流程步骤

**Role:** 共学五步
橄榄浅纸底，上方 1px 墨线，五格等分，格间 1px `rule` 竖线（照 ② 页尾数字表）；每格 64–112px Bricolage 编号、72px 下空、22px/700 小标题、15px 灰字。hover 整格变纸白、编号变钴蓝。移动端改成「编号 | 标题 + 说明」横排列表。

### 引语对开

**Role:** 院长寄语，照 ② s05
左 40.8% 墨面：120px 夜钴蓝引号 + `FROM THE FOUNDER` + 32px 宋体署名 + 灰字头衔；右 59.2% 橄榄浅纸：28–48px 宋体引语（每行 ≤15 字），下接 19px 叙述与行链。

### 演示件：人的意愿 ↔ 能力的延伸

**Role:** 可拖的小部件，照 ③ s11 的字重滑杆
上方两行 44–104px 大字「人决定方向，/ AI 拓展人的能力。」，下方 56px 高胶囊控件：左标签「人的意愿」、原生 range、右标签「能力的延伸」。拖向左：第一行字重升到 860、横向放到 110%，第二行降到 360、收到 98%；拖向右反之。左侧钴蓝 mono 实时显示 `人 · WGHT 610 / AI · WGHT 610`。标签只用文案稿已有的词。

### 输入框

**Role:** 表单（预留，首页未用）
标签在上 15px/600，框高 48px、1px 墨线、2px 圆角、纸白底；帮助文字 13px 灰字在下；focus 钴蓝外框；错误态左侧 3px 墨色内条 + 加粗说明，不引入红色。

### 徽标

**Role:** 状态与类别
胶囊 28px 高，三种：钴蓝描边、墨底、浅纸底；日期用 mono 描边版。

## Surfaces

| Level | Name     | Value     | Purpose                                   |
| ----- | -------- | --------- | ----------------------------------------- |
| 0     | paper    | `#f8f8f3` | 首屏网格、演示件、第一二章、观点          |
| 1     | paper-2  | `#ecece3` | 目录瓦片、共学五步、引语右半              |
| 2     | ink      | `#20211a` | 第三章、院长左半、页脚、书脊字标          |
| 3     | ink-2    | `#2b2c24` | 深色面上的产品卡                          |
| 4     | black    | `#000000` | 首屏黑场终态、联系区                      |
| 5     | accent   | `#0c6ccc` | 书脊色条、「从这里开始」瓦片、主按钮      |

面与面之间硬切，不做渐变过渡（③ s07、s10）。

## Do's and Don'ts

### Do

- 所有内容从五栏线起笔；新增区块先决定落在哪几栏，再决定写什么。
- 空格子就让它空着，用 11px 钴蓝 mono 度量标注（`行高 1.06`、`1 : 2`）让空白读起来像图纸。
- 钴蓝每屏最多一块色块；强调词用钴蓝 + 860 字重，一个标题只强调一处。
- 中文标题用平体 104%，字距停在 -0.02em；拉丁编号才收到 -0.045em。
- 深色面上的强调一律换成夜钴蓝 `#5b9be0`。
- 图片只用「直角装裱 + 等宽挂签」一种处理；同一幅插画可以放大取局部反复用。
- 滑动放大的盒子按终态排版，从 scale(.5) 放到 1，终态宽不超过 760px。
- 章节上空每章不同：160 / 240 / 120 / 96 / 200px。

### Don't

- 不要把 logo 的橘橙拿来做按钮、标签或强调色。
- 不要用中性灰；所有灰都带橄榄底调。
- 不要给图片加圆角、阴影、滤镜或渐变遮罩。
- 不要出现 6–12px 的「中间圆角」。
- 不要在钴蓝以外再引入第二个界面强色，也不要紫蓝渐变、渐变文字、玻璃拟态、外发光。
- 不要编造数字：大数字只能是 01–05、03、2026、2026.09.15。
- 不要在浅纸面上用钴蓝小字（4.38:1 不达标）。
- 不要把三张等宽卡排成一行；观点区是一大两行。
- 不要用 Inter / Roboto / Arial。

## Imagery

素材只有一张 3D 折纸半人马（透明底 + 米色底两版）和三张暖色纸感插画。半人马是首屏与黑场的主角，用透明底版，白纸上与黑场上都成立；米色底版只在观点列表缩略图里以 `mix-blend-mode: multiply` 融进浅纸。三张插画统一「直角装裱 + 左下等宽挂签」，不加任何滤镜；插画自带的钴蓝与赭石正好和界面钴蓝、纸白呼应，所以画面里的暖色不需要压。第二章用放大取局部拼出一大两小，第三章把插画放在墨面上，像挂在深色墙上的画。图形只用内联 SVG：目录瓦片里的五节点折线、引号、叠页，黑场与联系区的黄金分割构图线。

## Layout

页面顺序：书脊顶栏 → 钉住的首屏（白纸网格 → 黑场）→ 八格目录板 → 演示件 → 第一章（纸，编号左 / 标题右 / 图左下）→ 第二章（纸，标题左上 / 一大两小）→ 第三章（墨面硬切，编号左 / 标题右 / 图 + 两张产品卡）→ 共学五步（浅纸数字格）→ 观点（纸，左标题 / 右一大两行）→ 院长寄语（墨 + 浅纸对开）→ 联系（黑场构图线 + 居中细线框）→ 页脚（墨面满宽字标）。十一段用了九种版式，没有两段相邻同构。纸面各段左侧第一栏放 `§01` 书眉和竖排章节名（sticky），这是 ③ 内页左竖栏的中文版本。移动端全部单栏，首屏网格与黑场上下排开，目录板改两栏。

## Agent Prompt Guide

Quick Color Reference:

```
paper: #f8f8f3
paper-2: #ecece3
ink / foreground: #20211a
accent (≤ 一块/屏): #0c6ccc
accent-on-dark: #5b9be0
muted: #63645a
hairline: #cddff2
black (只给黑场): #000000
```

Example Component Prompts:

1. 做一格首屏：`display:grid; grid-template-columns:12.2fr 38.9fr 8.9fr 30fr 10fr; grid-template-rows:7% 60% 21% 12%`，背景画 1px `#cddff2` 竖线于 12.2/51.1/60/90%、横线于 7/67/88%。第 2 栏第 2 行左上放 H1：Noto Sans SC 560，`clamp(44px,5.9vw,92px)`，行高 1.06，字距 -0.02em，每行 `scaleX(1.04)`，颜色 `#0c6ccc`，强调词 860。第 4 栏第 2 行放半人马，其余格子空着。
2. 做一块目录瓦片：`background:#ecece3; border-radius:2px; padding:22px 24px`，左上 26px/560 平体标题，下接 12px Geist Mono 大写标签 `#63645a`，右上 ↘，右下贴一张直角插画占 78% 宽；hover 底色变 `#d9d9cc`，箭头右下移 3px，曲线 `cubic-bezier(.2,.1,0,1)`。
3. 做一段墨面章节：`background:#20211a`，竖网格线换 `#3a3b32`；第 2 栏放 Bricolage Grotesque 540 编号（132px，`#a9aa9c`，-0.045em，行高 .9），第 3–4 栏放 60px 标题，强调词 `#5b9be0`；下方一大两小：左侧直角插画，右侧两张 `#2b2c24` 产品卡，卡内夜钴蓝描边胶囊 + 禁用胶囊按钮。

## Similar Brands

逐条写明本版从三个参考站借了什么、出自哪一屏（截图在 `styles-kit/study/<slug>/`）。

- **③ Dropbox Brand（brand.dropbox.com，Daybreak Studio，Awwwards SOTM 2025-02 / CSSDA 2025 年度）— 骨架**
  - 发丝网格本身就是装饰，不等分格子，内容只占其中几格（清单第 4 条）→ `s01.png`、`fold.png`：淡蓝 hairline 竖线 320/608/832/1120；本站换成钴蓝发丝 `#cddff2` 与 176/736/864/1296 五栏。
  - 首屏几乎是空的，一格放唯一强色大字 → `s01.png`：蓝色宽体字放在中央大格左上；本站 H1 放第 2 栏左上，半人马放第 4 栏。
  - 一个界面强色 + 近黑，辅助色关在板块里（清单第 5 条）→ `s01.png`、`s03.png`；本站取 logo 马身钴蓝，橘橙只留在 logo 与插画。
  - 首页即目录，同构瓦片做入口（清单第 9 条）→ `s03.png`：八宫格，四栏不等宽 268/477/377/268、10px 外边距与间距、左上标题右下图形、一块小 logo 格；本站照搬 4 栏 1 : 1.8 : 1.4 : 1 与 10px。
  - 网格淡出、强色块居中的滚动过程 → `s04.png`、`s02.png`、`s05.png`：由滚动驱动的 sticky 容器；本站的滑动放大沿用「钉住 + 滚动进度驱动」的结构。
  - 非整百字重 + 略加宽字宽 → STYLE.md 记录的 `"wght" 483, "wdth" 108`；本站 560 / 860 + 中文平体 104%。
  - 可拖的字重滑杆演示件 → `s11.png`：白色控件、蓝色滑块；本站「人的意愿 ↔ 能力的延伸」滑杆。
  - 留白里的度量标注 → `s07.png`（「120%」）、`s09.png`（「75% complete」）；本站 `WGHT 560`、`行高 1.06`、`1 : 2`。
  - 内页左竖栏 + 竖排板块名 → `s06.png`–`s11.png`；本站 `§01` 书眉 + 竖排章节名 sticky。
  - 标题从固定起笔线开始、图片一大两小 → `s08.png`（x≈528 起笔、一张竖图 + 两张横图）；本站第二章。
  - 底色硬切到近黑、一大两小演示卡 + 胶囊标签 → `s10.png`；本站第三章墨面 + 产品卡。
  - 圆角两极：功能件 0–2px、胶囊 100px（清单第 3 条）→ STYLE.md。
- **② AI in Design Report 2026（stateofaidesign.com，++hellohello，Awwwards SOTD 2026-08-26）**
  - 顶栏像书脊：黑方块字标 + 满高色条 CTA + 纯文字导航（清单第 8 条）→ `s01.png`、`fold.png`；本站色条换成钴蓝，并让两块边缘对齐网格线。
  - 等宽大写标签做署名、分区名（清单第 2 条的标签声部）→ `s01.png`（`BY DESIGNER FUND…`）、`s02.png`（`OUR PARTNERS`）。
  - 大引语对开：左黑块 + 引号 + 署名，右色块 + 50px 引语 → `s05.png`；本站院长寄语。
  - 章节「编号 + 章名 | 标题 + 摘要，图在左下」→ `s06.png`；本站第一章。
  - 带顶线的行链 → `s11.png`（「Get notified when they're released」）；本站「了解学院的主张 ↗」等。
  - 数字格：一行多格、1px 竖线分隔、超大数字 + 小说明 → `s13.png`；本站共学五步。
  - 满宽品牌字标页脚 → `s13.png`（「Ai in Design」）；本站「半人马AI学院」。
  - 观点区「左栏空 / 右栏大图 + 标题 + 正文 + 行链」→ `s11.png`；本站观点与动态。
  - 超大紧排标题的规律：字越大距越紧、行越贴（清单第 1 条）→ STYLE.md；本站中文停在 -0.02em / 1.06。
- **④ Shopify Editions Winter '26（shopify.com/editions/winter2026，Awwwards SOTM 2026-02，Webby 2026 最佳视觉设计大众之选）**
  - 黑场开幕 + 黄金分割构图线 + 标题锁定，再进入纸页（清单第 7 条）→ `fold.png`（黑底、两大圆弧、对角线、三级方格、居中细线框）；本站首屏滚动后的黑场终态与联系区。
  - 居中细线框就是锁定区 → `s01.png`、`mobile.png`；本站联系区的居中细线框。
  - 三种字体三种声部：粗无衬线喊章节、衬线讲叙述、小字做标签（清单第 2 条）→ `s03.png`、`s04.png`、`s12.png`。
  - 带色温的灰阶，全部是同一色相（清单第 6 条）→ STYLE.md 的橄榄灰 `#DCDCD0 / #909083 / #5C5C4E`；本站 `#ecece3 / #d9d9cc / #a9aa9c / #63645a / #20211a`。
  - 章节标题上下留白每章不同（清单第 12 条）→ PATTERNS.md「11vh–35vh」；本站 160 / 240 / 120 / 96 / 200px。
  - 滚动驱动的开场转场、章首满屏大图 → `s02.png`、`s03.png`；本站把「滚动放大」做成签名动效。
  - 大面零圆角 + 胶囊按钮、几乎无阴影（清单第 3 条）→ STYLE.md。

清单 12 条覆盖了 1-10 与 12，共 11 条；第 11 条（大标题从栅格中线起）没有照做，因为骨架按 ③ 把 H1 放进左侧内容格，中线右侧留给半人马。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — surfaces */
  --color-paper: #f8f8f3;
  --color-paper-2: #ecece3;
  --color-ink: #20211a;
  --color-ink-2: #2b2c24;
  --color-black: #000000;

  /* Colors — text */
  --color-foreground: #20211a;
  --color-muted: #63645a;
  --color-on-dark: #f8f8f3;
  --color-muted-on-dark: #a9aa9c;

  /* Colors — the one accent (logo horse cobalt) */
  --color-accent: #0c6ccc;
  --color-accent-deep: #0a56a6;
  --color-accent-on-dark: #5b9be0;
  --color-on-accent: #f8f8f3;

  /* Colors — lines */
  --color-hairline: #cddff2;
  --color-rule: #d9d9cc;
  --color-rule-dark: #3a3b32;
  --color-construct: #34352d;
  --color-focus: #0c6ccc;
  --color-disabled-bg: #e2e2d8;
  --color-disabled-fg: #5a5b51;

  /* Typography — families */
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', system-ui, sans-serif;
  --font-serif: 'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-display-latin: 'Bricolage Grotesque', 'Helvetica Neue', 'PingFang SC', sans-serif;
  --font-serif-latin: 'Newsreader', Georgia, 'Songti SC', serif;
  --font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, monospace;

  /* Typography — scale */
  --text-label: 12px;
  --text-sm: 14px;
  --text-body: 16px;
  --text-narrative: 22px;
  --text-tile: clamp(22px, 1.9vw, 30px);
  --text-h3: 28px;
  --text-quote: clamp(28px, 3.2vw, 48px);
  --text-h2: clamp(34px, 4vw, 60px);
  --text-display: clamp(44px, 5.9vw, 92px);
  --text-numeral: clamp(72px, 8.4vw, 132px);
  --text-wordmark: clamp(56px, 16.4vw, 250px);

  /* Typography — weights (variable, 非整百) */
  --wght-light: 380;
  --wght-text: 420;
  --wght-display: 560;
  --wght-heavy: 860;
  --wdth-latin: 100;
  --stretch-cjk: 1.04;

  /* Line height & tracking */
  --leading-display: 1.06;
  --leading-heading: 1.12;
  --leading-quote: 1.32;
  --leading-narrative: 1.55;
  --leading-body: 1.75;
  --tracking-display: -0.02em;
  --tracking-latin-display: -0.045em;
  --tracking-label: 0.06em;

  /* Spacing (4px base) */
  --spacing: 4px;
  --gutter: 16px;
  --tile-gap: 10px;
  --space-ch1: 160px;
  --space-ch2: 240px;
  --space-ch3: 120px;
  --space-steps: 96px;
  --space-journal: 200px;

  /* Grid — 5 unequal columns, same fractions everywhere */
  --cols: 12.2fr 38.9fr 8.9fr 30fr 10fr;
  --header-h: 56px;
  --pin-h: min(calc(100svh - 56px), 844px);
  --pin-extra: min(100vh, 900px);

  /* Radius — two poles */
  --radius-face: 2px;
  --radius-none: 0px;
  --radius-pill: 999px;

  /* Shadows — none; one ring for controls on dark */
  --shadow-none: none;
  --shadow-ring: 0 0 0 1px rgba(32, 33, 26, 0.14);

  /* Motion */
  --ease-quick: cubic-bezier(0.2, 0.1, 0, 1);
  --ease-stage: cubic-bezier(0.72, 0.16, 0.19, 0.96);
  --dur-fast: 0.15s;
  --dur-base: 0.3s;
}
```

### Tailwind v4

```css
@theme {
  --color-paper: #f8f8f3;
  --color-paper-2: #ecece3;
  --color-ink: #20211a;
  --color-ink-2: #2b2c24;
  --color-black: #000000;
  --color-foreground: #20211a;
  --color-muted: #63645a;
  --color-on-dark: #f8f8f3;
  --color-muted-on-dark: #a9aa9c;
  --color-accent: #0c6ccc;
  --color-accent-deep: #0a56a6;
  --color-accent-on-dark: #5b9be0;
  --color-on-accent: #f8f8f3;
  --color-hairline: #cddff2;
  --color-rule: #d9d9cc;
  --color-rule-dark: #3a3b32;
  --color-construct: #34352d;
  --color-focus: #0c6ccc;
  --color-disabled-bg: #e2e2d8;
  --color-disabled-fg: #5a5b51;

  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', system-ui, sans-serif;
  --font-serif: 'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-display: 'Bricolage Grotesque', 'Helvetica Neue', 'PingFang SC', sans-serif;
  --font-serif-latin: 'Newsreader', Georgia, 'Songti SC', serif;
  --font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, monospace;

  --text-label: 12px;
  --text-sm: 14px;
  --text-body: 16px;
  --text-narrative: 22px;
  --text-tile: clamp(22px, 1.9vw, 30px);
  --text-h3: 28px;
  --text-quote: clamp(28px, 3.2vw, 48px);
  --text-h2: clamp(34px, 4vw, 60px);
  --text-display: clamp(44px, 5.9vw, 92px);
  --text-numeral: clamp(72px, 8.4vw, 132px);
  --text-wordmark: clamp(56px, 16.4vw, 250px);

  --font-weight-light: 380;
  --font-weight-text: 420;
  --font-weight-display: 560;
  --font-weight-heavy: 860;

  --spacing: 4px;

  --radius-none: 0px;
  --radius-face: 2px;
  --radius-pill: 999px;

  --ease-quick: cubic-bezier(0.2, 0.1, 0, 1);
  --ease-stage: cubic-bezier(0.72, 0.16, 0.19, 0.96);
}
```

## 签名记忆点

**滑动放大**：首屏右格里 0.5 倍的半人马，随滚动走到画面中央放大到 760px，白纸网格淡出，黄金分割构图线在黑场里从 72% 展开到满幅，细线框随后合拢，两侧浮出「人的意愿」「能力的延伸」。滚完约一屏后，黑场整体上移，露出八格目录。它把 ③ 的「网格收拢成目录」和 ④ 的「黑场开幕」接成了一个动作。

## 新增的结构性文字

以下文字不在文案稿里，是本版为版式加的书眉、标签与度量标注：

- 书眉 / 标签：`§00`（样张页）、`§01`、`§02`、`§03`、`CENTAUR AI ACADEMY · 2026`（首屏右栏竖排、黑场右上、页脚底行）
- 首屏度量标注：`WGHT 560`、`WGHT 860`、`行高 1.06`
- 黑场装饰字（`aria-hidden`，均取自文案稿）：`HUMAN × AI`、`人的意愿`、`能力的延伸`
- 目录瓦片标题：`共学五步`、`院长寄语`、`观点与动态`、`从这里开始`（前三个取自文案稿的区块名，第四个取自眉标）
- 目录瓦片标签：`01 - 05`、`01 / EXPERIENCE`、`02 / LEARN TOGETHER`、`03 / MAKE IT REAL`、`FROM THE FOUNDER`、`CENTAUR JOURNAL`、`THE NEXT CHAPTER`
- 目录瓦片与章节里的竖排章节名：`从你的积累出发`、`与同行者一起`、`让想法落地`（取自文案稿章节名）
- 演示件：`人 · WGHT 610`、`AI · WGHT 610`（随滑杆变化的数值）、右侧 `HUMAN × AI`；演示件大字复用品牌句「人决定方向，AI 拓展人的能力。」
- 第二章度量标注：`1 : 2`、`同一幅画`、`三处取景`
- 图片挂签：`EXPERIENCE`、`LEARN TOGETHER`、`MAKE IT REAL`（取自图注）
- 五步标注：`01 → 05`
- 移动端菜单按钮：`目录 +` / `目录 −`
- 复制反馈：`已复制客服链接`
- 页脚底行：`人的意愿 × 能力的延伸`
- 样张页（kit.html）另有：`返回首页预览 ↗`、`KIT · 发丝网格`、各节标题与说明、输入框示例文字
