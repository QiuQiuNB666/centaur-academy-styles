# 半人马AI学院 · 董事会深蓝 — Style Reference

> 深蓝定调，象牙行文，黄铜只画线

**Theme:** light

「董事会深蓝」把学院当成一份写给经营者的年度报告来排：首屏和整段色带用深海军蓝（#0b1f3a）压住场子，正文区退回象牙白（#f5f2ea），中间靠一条 1px 墨蓝通栏线加左端 56×3 的黄铜签（书眉线）分节——每个区块都从这条线开始，像翻开报告的新一章。标题用 Noto Serif SC 配 Frank Ruhl Libre，平常词 500、强调词 900 再压一条 2px 黄铜底线，强调靠字重和线，不换颜色。黄铜（#b08d4c）是全站最贵的东西：只做线、签、空心数字的描边和小标，累计面积 ≤3%，不做填充块、不做渐变、不给正文上色。圆角统一 2px，阴影只给插画画框一处（借 Bridgewater 的 0 10px 40px 低透明度大扩散），其余层级全靠线。签名记忆点是首屏的**黄铜经纬**：抠图半人马站在一副细线罗盘里，一根黄铜指针顺着他的视线指出去——「人决定方向」不写在装饰里，画在构图里；配套的是三章节的**空心描边大数字**（1px 旧金描边、不填色）。暖色纸感插画不硬贴：在象牙上装进衬纸 + 黄铜内线的画框并降饱和到 .88，在深蓝上则是一幅挂在墙上的象牙衬纸画。

## Tokens — Colors

| Name           | Value     | Token                                | Role                                                   |
| -------------- | --------- | ------------------------------------ | ------------------------------------------------------ |
| 象牙画布       | `#f5f2ea` | `--color-background`                 | 正文区主背景；比米色更白更冷，避开「暖米 + 陶土」长相  |
| 墨蓝前景       | `#111c2e` | `--color-foreground`                 | 主文字、象牙上的重线（15.27:1）                        |
| 衬纸           | `#fbf9f4` | `--color-card`                       | 画框衬纸、缩略图衬底、输入框底                         |
| 深象牙         | `#ebe6d9` | `--color-secondary`                  | 次级色带（共学五步）、描边钮 hover                     |
| 石板灰次要文   | `#4f5b6e` | `--color-muted-foreground`           | 次要文字，象牙上 6.15:1、深象牙上 5.52:1               |
| 栏线           | `#d9d3c3` | `--color-border`                     | 行间细线、画框外沿                                     |
| 重线           | `#111c2e` | `--color-border-strong`              | 书眉线、表头线、描边钮边框                             |
| 输入框线       | `#8d8673` | `--color-input`                      | 输入框边框，3.24:1 满足非文本对比                      |
| 董事会深蓝     | `#0b1f3a` | `--color-primary`                    | Hero、整段色带、主按钮；全页面积约三分之一             |
| 象牙主前景     | `#f5f2ea` | `--color-primary-foreground`         | 深蓝上的文字（14.77:1）                                |
| 午夜蓝         | `#07162b` | `--color-primary-deep`               | 页脚、移动菜单、按钮按压态                             |
| 抬升蓝         | `#15305a` | `--color-primary-raised`             | 深蓝上的 hover 面                                      |
| 雾蓝次要文     | `#a9b4c6` | `--color-primary-muted-foreground`   | 深蓝上的次要文字（7.89:1）                             |
| 深蓝栏线       | `#2a4166` | `--color-primary-border`             | 深蓝上的细线、罗盘刻度                                 |
| 黄铜（稀缺）   | `#b08d4c` | `--color-brass`                      | 线、签、按钮分隔线、画框内线；不做文字、不做填充，≤3% |
| 旧金           | `#765a1f` | `--color-brass-deep`                 | 象牙上的眉标小字与空心数字描边（5.77:1）               |
| 浅铜           | `#d4b97c` | `--color-brass-light`                | 深蓝上的眉标小字与 focus 环（8.68:1）                  |
| 砖红危险       | `#80241e` | `--color-destructive`                | 表单错误、不可逆动作（取自 Bridgewater 的 #80241e）    |
| 松绿成功       | `#2f5d46` | `--color-success`                    | 成功状态                                               |

### 柔和语义色（浅底 + 深字，只用于徽标）

| Name | Background | Text      | Token                      |
| ---- | ---------- | --------- | -------------------------- |
| 柔蓝 | `#e1e7f0`  | `#1d3a66` | `--color-pastel-navy-*`    |
| 柔铜 | `#f0e7d0`  | `#6b4f14` | `--color-pastel-brass-*`   |
| 柔石 | `#e7e3d8`  | `#4a5261` | `--color-pastel-stone-*`   |
| 柔红 | `#f4e2de`  | `#80241e` | `--color-pastel-red-*`     |

### 面积配比

| 象牙 | 深象牙 | 深蓝 | 黄铜 |
| ---- | ------ | ---- | ---- |
| 56%  | 8%     | 33%  | ≤3%  |

## Tokens — Typography

### Noto Serif SC + Frank Ruhl Libre — 标题与引文 · `--font-display` / `--font-serif`

- **Substitute:** Source Han Serif SC, Songti SC, STSong, SimSun, Georgia
- **Weights:** 500（标题常态）, 700（期刊标题、步骤名）, 900（强调词、产品名）；拉丁 400（空心数字）
- **Sizes:** 22px, 24px, 28px, 30–44px, 36–68px, 52–116px
- **Line height:** display 1.12 / 标题 1.22 / 引文 1.42
- **Letter spacing:** display 0.01em / 标题 0.02em；中文衬线不收紧，靠略放的字距出庄重感
- **Role:** 全部 H1/H2/H3、副标题（lede）、院长引文、页脚口号。拉丁字母与数字落在 Frank Ruhl Libre 上（「AI」两个字母在首屏要和宋体的粗细对得上，这是选它而不是 Playfair 的原因）。回退到 Songti SC 时字面略窄，版式不依赖固定字宽，不会塌

### Noto Sans SC + Libre Franklin — 正文与界面 · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, Helvetica Neue, system-ui
- **Weights:** 400, 500, 600
- **Sizes:** 12px, 13px, 14px, 15px, 16px, 18px
- **Line height:** 1.8（中文正文）/ 1.6（眉标）
- **Letter spacing:** 正文 0.01em / 英文眉标 0.16em 全大写 / 中文眉标 0.24em
- **Role:** 正文、导航、按钮、眉标、图注说明。Libre Franklin 是新闻无衬线血统，和 HBR 的 GT America、HBS 的 Graphik 同一路数

### IBM Plex Mono — 日期 / 编号 / 图注标签 · `--font-mono`

- **Substitute:** ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas
- **Weights:** 400, 500
- **Sizes:** 11px, 12px, 13px
- **OpenType features:** tabular-nums
- **Role:** 期刊日期 `2026.09.15`、共学五步编号、图注英文标签（EXPERIENCE）、「下载暂未开放」这类状态注记。不给中文正文用

### Type Scale

| Role       | Size              | Line Height | Letter Spacing | Token               |
| ---------- | ----------------- | ----------- | -------------- | ------------------- |
| display    | clamp(52–116px)   | 1.12        | 0.01em         | `--text-display`    |
| heading-xl | clamp(36–68px)    | 1.22        | 0.02em         | `--text-heading-xl` |
| heading-lg | clamp(30–44px)    | 1.22        | 0.02em         | `--text-heading-lg` |
| heading    | 28px              | 1.35        | 0.02em         | `--text-heading`    |
| subheading | 22px              | 1.6         | 0.02em         | `--text-subheading` |
| body-lg    | 18px              | 1.8         | 0.01em         | `--text-body-lg`    |
| body       | 16px              | 1.8         | 0.01em         | `--text-body`       |
| body-sm    | 14px              | 1.8         | 0.01em         | `--text-body-sm`    |
| caption    | 12px              | 1.6         | 0.16em（眉标） | `--text-caption`    |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 0.25rem`）

**Density:** 宽松。区块上下 64–120px，报告式的大页边；行内元素紧凑

### Spacing Scale

| Name        | Value               | Token            |
| ----------- | ------------------- | ---------------- |
| 1           | 4px                 | `--spacing` × 1  |
| 2           | 8px                 | `--spacing` × 2  |
| 3           | 12px                | `--spacing` × 3  |
| 4           | 16px                | `--spacing` × 4  |
| 6           | 24px（栅格槽）      | `--spacing` × 6  |
| 8           | 32px                | `--spacing` × 8  |
| 12          | 48px                | `--spacing` × 12 |
| 18          | 72px                | `--spacing` × 18 |
| section-gap | clamp(64px–120px)   | `--section-gap`  |
| page-gutter | clamp(20px–60px)    | `--page-gutter`  |

### Border Radius

| Name | Value          | Token           |
| ---- | -------------- | --------------- |
| sm   | 1px            | `--radius-sm`   |
| md   | 2px（base）    | `--radius-md`   |
| lg   | 4px            | `--radius-lg`   |
| full | 999px          | `--radius-full` |

| Element      | Value                       |
| ------------ | --------------------------- |
| 按钮         | 2px (md)                    |
| 输入框       | 2px (md)                    |
| 徽标         | 1px (sm)，不用胶囊          |
| 画框、缩略图 | 0，直角                     |
| Logo 衬牌    | 1px (sm)                    |

### Rules（线是这套范式的主要层级手段）

| Name       | Value      | Token               |
| ---------- | ---------- | ------------------- |
| 细线       | 1px        | `--rule-hair`       |
| 重线       | 2px        | `--rule-heavy`      |
| 黄铜签宽   | 56px       | `--rule-tab-width`  |
| 黄铜签高   | 3px        | `--rule-tab-height` |

### Shadows

| Name       | Value                               | Token                 |
| ---------- | ----------------------------------- | --------------------- |
| sm         | `0 1px 2px 0 rgba(7,22,43,0.06)`    | `--shadow-sm`         |
| frame      | `0 10px 40px 0 rgba(7,22,43,0.1)`   | `--shadow-frame`      |
| frame-navy | `0 18px 50px 0 rgba(3,10,22,0.45)`  | `--shadow-frame-navy` |

阴影只属于章节插画框。按钮、期刊行、输入框、徽标一律无阴影。

### Motion

| Name          | Value                           | Token             |
| ------------- | ------------------------------- | ----------------- |
| ease-board    | `cubic-bezier(0.32, 0.72, 0, 1)` | `--ease-board`    |
| duration-fast | 180ms（按压、箭头位移）         | `--duration-fast` |
| duration-slow | 600ms（底线生长、缩略图放大）   | `--duration-slow` |

只动 transform / opacity / background-size。插画入场用 `animation-timeline:view()` 做 1.06→1 的微缩放，包在 `@supports` 和 `prefers-reduced-motion:no-preference` 里，终态即默认态。

### Layout

- **Section gap:** 64–120px（`--section-gap`）
- **Grid:** 12 栏，槽 24px
- **Element gap:** 24px；标题到正文 28px；书眉线到内容 32–56px
- **Max content width:** 1320px（取 HBS Online 1340 与 Bridgewater 1320 之间）

## Components

### Primary Button（分格按钮）

**Role:** 主 CTA「联系学院顾问 ↗」
`bg-primary`(#0b1f3a) `text-primary-foreground`(#f5f2ea)，`border-radius: var(--radius-md)`(2px)，`min-height: 48px`，文字格 `padding: 0 22px`、`font: 15px/500`、字距 0.06em；箭头单独一格，左侧 1px 黄铜分隔线。hover: 底色 → `primary-raised`，箭头 translate(2px,-2px)；active: `primary-deep` + scale(.98)；focus-visible: 2px `--color-ring` 环、offset 3px。深蓝色带上反转为 `.btn-inverse`（象牙底墨蓝字），focus 环换 `--color-ring-inverse`(#d4b97c)。

### Outline Button

**Role:** 次级动作「复制客服链接」、页头 CTA
透明底 + 1px `border-strong`，hover 出现 `bg-secondary`；深蓝上边框换 `primary-border`、hover `primary-raised`。

### Disabled Button

**Role:** 「下载知君 ↓ / 下载万象 ↓」暂未开放
透明底、`muted-foreground` 字、1px **虚线** `border`，分隔线同为虚线，`cursor:not-allowed`；旁边用等宽小字注明「下载暂未开放」。虚线表达「位置留着、尚未开放」，不用灰块。

### Text Link

**Role:** 行内去向「了解学院的主张 ↗」
15px/500，下方 1px 黄铜底线；hover 底线变为当前文字色、箭头位移 2px。触控高度 44px。

### 书眉线 Section Rule（签名组件）

**Role:** 每个区块的开头
`border-top: 1px solid border-strong` + `::before` 左端 56×3 黄铜签，坐在线上方。深蓝上线色换 `primary-border`，黄铜签不变。线下 18–28px 放眉标或章节号。

### 章节号 Chapter Numeral（签名组件）

**Role:** 三个叙事章节的「01 / 从你的积累出发」
数字 Frank Ruhl Libre 400、clamp(64–104px)、`color: transparent` + `-webkit-text-stroke: 1px brass-deep`（深蓝上 `brass-light`），后接 `/` 与 14px/500、字距 0.14em 的章节名。只用于三章节；共学五步用等宽小号，别处不编号。

### 罗盘经纬 Compass（签名组件）

**Role:** 首屏主视觉的底
内联 SVG：外圈 + 72 刻度（`stroke-dasharray`）+ 十字经纬 + 虚线内圈，全部 `primary-border`；一个 214 半径的黄铜圆和一根指向右上的黄铜指针（1.2px）带实心箭头。抠图半人马叠在上面，指针从躯干后穿出、顺着视线方向。全站只出现一次。罗盘是正圆、比 4:3 的图高出约 12%，会探出图框：承载它的深蓝色带必须 `overflow-x:clip`（旧浏览器回退 `hidden`），≤900px 时主视觉上方留 `12vw + 12px`，别让外圈压到文字链。

### 章节插画框 Plate

**Role:** 三张章节插画
`bg-card` 衬纸 `padding: 8–14px` + 1px `border` + `--shadow-frame`；图片上叠 `inset 0 0 0 1px brass`（70% 不透明）内线，`filter: saturate(.88)` 把暖橙压到和深蓝同一个音量。深蓝上边框换衬纸色、阴影换 `--shadow-frame-navy`。图注在框外：等宽 11px 英文标签（旧金/浅铜）+ 14px 中文说明。第三章用 21:8 横幅裁切，移动端回到 4:3。

### 期刊目录行 Journal Row

**Role:** 观点与动态列表
三列栅格 `132px | 1fr | 176px`：左列等宽日期 + 直角描边徽标「观点」，中列 28px/700 衬线标题 + 15px 摘要，右列 4:3 衬纸缩略图。行间 1px `border`，表头 1px `border-strong`。整行可点；hover 标题下长出 1px 墨线、缩略图 scale(1.04)。不装卡片、不加阴影——它是目录，不是营销卡。

### 流程步骤 Steps

**Role:** 共学五步
五栏等分，顶部 1px `border-strong`，每栏起点一个 7px 黄铜方钉，栏间 1px `border`；等宽 13px 编号（旧金）→ 48px 空 → 24px/700 衬线步骤名 → 15px 说明。≤900px 变成左侧竖线 + 方钉的时间轴。

### 产品下载行 Product Row

**Role:** 知君 / 万象
表格式一行：28px/900 衬线产品名（字距 0.08em）| 文字链 | 禁用态小按钮 | 等宽注记。表头重线、行间细线。

### 引文块 Quote

**Role:** 院长寄语
左侧 1px 黄铜竖线，`padding-left: 20–44px`；衬线 500、clamp(26–48px)、行高 1.42，`text-indent:-.5em` 让开引号悬挂。左栏放 220–320px 的空心描边引号和署名；署名上方一条 1px 黄铜签名线，名字 32px/700、字距 0.3em。

### 联系横幅 Contact Banner

**Role:** 页尾转化
不做色块横幅：书眉线 + 眉标，H2 放到 clamp(40–92px) 占 8 栏，右侧 4 栏底对齐放一句话 + 主按钮 + 描边钮。全页第二处大标题，和首屏呼应。

### Input Field

**Role:** 文本输入（预约、留言）
`bg-card` + 1px `--color-input`(#8d8673)，`border-radius: var(--radius-md)`，`height: 48px`，`padding: 0 14px`，16px 字。focus: 2px `--color-ring` 环 offset 2px；error: 边框 `destructive` + 下方 13px 砖红提示。

### Badge

**Role:** 栏目 / 状态标记
高 22px、`padding: 0 8px`、1px 圆角、12px/500、字距 0.1em。默认描边款（`inset 0 0 0 1px border-strong`）用于栏目「观点」；状态用 pastel 成对色（柔蓝 / 柔铜 / 柔石 / 柔红）。不用胶囊形。

### Logo 衬牌

**Role:** 深蓝上放 Logo
Logo 的钴蓝马身在深蓝上会沉下去，所以给它一块 40×48 的象牙衬牌（1px 圆角），像书脊上的藏书票。页头、页脚同款。

## Surfaces

| Level | Name           | Value     | Purpose                                  |
| ----- | -------------- | --------- | ---------------------------------------- |
| 0     | background     | `#f5f2ea` | 正文区                                   |
| 1     | card           | `#fbf9f4` | 衬纸、输入框、缩略图衬底                 |
| 2     | secondary      | `#ebe6d9` | 次级色带、hover                          |
| 3     | primary        | `#0b1f3a` | Hero、第二章、院长寄语整段色带           |
| 4     | primary-deep   | `#07162b` | 页脚、移动端菜单                         |
| 5     | primary-raised | `#15305a` | 深蓝上的 hover 面                        |

## Do's and Don'ts

### Do

- 每个区块用书眉线开头：1px 线 + 左端黄铜签。它是这套范式的页眉，别省。
- 深蓝成段使用——整个 hero、整段色带、整个页脚。深蓝小方块散落在象牙页面上会像银行 App。
- 强调词一律「900 字重 + 2px 黄铜底线」，颜色不变。
- 黄铜只出现在：书眉签、按钮分隔线、文字链底线、画框内线、罗盘指针、步骤方钉、引文竖线、签名线。先数一遍，超过 3% 就删。
- 象牙上的小字用旧金 `#765a1f`，深蓝上用浅铜 `#d4b97c`；`#b08d4c` 本身在象牙上只有 2.78:1，不能当文字色。
- 日期、编号、英文图注标签用 IBM Plex Mono + tabular-nums。
- 暖色插画必须进画框（衬纸 + 内线 + saturate .88）；深蓝上的半人马只用抠图版。
- 大标题敢放大：首屏 116px、联系区 92px，其余区块克制，全页只有这两处破局。
- 动效曲线用 `var(--ease-board)`，只动 transform / opacity / background-size。

### Don't

- 不要金色渐变、金色填充按钮、金色大字——黄铜一旦成块，立刻从「董事会」掉到「会所」。
- 不要圆角卡片加阴影装内容；层级靠线和留白，阴影只属于插画框。
- 不要把期刊做成三张等宽封面卡；它是目录行。
- 不要用纯黑 `#000` 或纯白 `#fff`；最深是午夜蓝 `#07162b`，最亮是衬纸 `#fbf9f4`。
- 不要给中文衬线标题收紧字距，也不要用超过 0.04em 的正字距排大标题——前者挤，后者散。
- 不要在三章节和共学五步之外使用编号；区块不编号。
- 不要让深蓝和钴蓝 Logo 直接相贴——Logo 必须站在象牙衬牌上。
- 不要编造数字、客户 logo、学员评价；本范式里等宽数字只服务真实的日期和顺序。
- 不要用「全面 / 深入 / 赋能 / 打造 / 极致」。

## Imagery

图像分两类处理。**半人马**是品牌形象，首屏用透明抠图版站在深蓝上，背后是细线罗盘，脚下的半透明投影自然落在深蓝里；在象牙场景（期刊封面）用米色底原图 + `mix-blend-mode:multiply` 融进衬纸。**三张场景插画**是暖色纸感风格，好在画面里本来就有藏蓝与赭红，和深蓝色板是亲戚；处理方式是「装裱」而不是「铺满」：衬纸、黄铜内线、轻降饱和，图注放在框外按「英文等宽标签 + 中文一句话」的图版体例写。第三章把插画裁成 21:8 横幅，正好取到「草图 → 纸模 → 成品」那一排，和「让想法落地」对上。不用图标库；需要的图形（罗盘、箭头、方钉）全部是内联 SVG 或 CSS 线条。箭头用文字字符 ↗ → ↓，随字体走。

## Layout

1320px 容器、12 栏、24px 槽，页边 20–60px。页面节奏是深浅交替的整段色带：**深蓝 hero → 象牙第一章 → 深蓝第二章 → 象牙第三章 → 深象牙五步 → 象牙期刊 → 深蓝寄语 → 象牙联系 → 午夜蓝页脚**。Hero 左 7 栏排文字、右 6 栏放主视觉（第 7 栏重叠），底部一条书眉线收住品牌主张与图注（下内边距 48px，给左下角的固定返回钮让位）——不居中、不堆两个并排按钮（主按钮 + 一条文字链）。Hero 的副标题与说明并排成「摘要」体例，中间一条竖细线。三章节各不相同：第一章文左图右、整块文字沉底与画框下沿对齐（标题、说明、链接不拆开，空白留在章节号下方）；第二章整段深蓝、图左文右；第三章横幅图通栏，下方左标题右产品表。期刊区左 4 栏是 sticky 的栏目头，右 8 栏是目录行。寄语区左 3 栏署名、右 9 栏引文。≤900px 全部单栏，导航收进 44px 的菜单钮，五步变竖向时间轴。页头不吸顶——它属于 hero 这张「封面」。

## Agent Prompt Guide

Quick Color Reference:

```
background: #f5f2ea
foreground: #111c2e
card (mat): #fbf9f4
secondary band: #ebe6d9
muted-foreground: #4f5b6e
border: #d9d3c3
primary (navy): #0b1f3a
primary-deep: #07162b
on-navy muted: #a9b4c6
on-navy rule: #2a4166
brass (lines only, ≤3%): #b08d4c
brass-deep (small text on ivory): #765a1f
brass-light (small text on navy): #d4b97c
```

Example Component Prompts:

1. Create a section opener: `border-top: 1px solid #111c2e` full width, with a `56px × 3px` brass (#b08d4c) tab sitting on top of the line at the left end. 18px below, an eyebrow in Libre Franklin 12px/500, uppercase, `letter-spacing: .16em`, color #765a1f. On navy bands the line becomes #2a4166 and the eyebrow #d4b97c.
2. Create the primary CTA: navy (#0b1f3a) button, ivory (#f5f2ea) text, `border-radius: 2px`, `min-height: 48px`, label cell `padding: 0 22px` 15px/500 `letter-spacing: .06em`, then a separate arrow cell divided by a 1px brass line containing `↗`. Hover: background #15305a and the arrow shifts `translate(2px,-2px)` with `cubic-bezier(.32,.72,0,1)` 180ms. Active: #07162b + `scale(.98)`.
3. Create a journal row (not a card): grid `132px 1fr 176px`, gap 32px, `padding: 32px 0`, bottom hairline #d9d3c3. Left: date in IBM Plex Mono 13px tabular-nums (#4f5b6e) above a square outlined badge. Middle: title Noto Serif SC 28px/700 #111c2e, summary 15px #4f5b6e. Right: 4:3 thumbnail inside a 6px #fbf9f4 mat with 1px #d9d3c3 border. Hover grows a 1px underline under the title over 600ms.
4. Create an illustration plate: wrapper `background:#fbf9f4; padding:14px; border:1px solid #d9d3c3; box-shadow:0 10px 40px rgba(7,22,43,.1)`; image 4:3 `object-fit:cover; filter:saturate(.88)`; overlay `box-shadow: inset 0 0 0 1px #b08d4c` at 70% opacity. Caption outside the frame: mono 11px uppercase label in #765a1f + 14px Chinese sentence in #4f5b6e.
5. Emphasise a word inside a serif heading: `font-weight:900; text-decoration: underline 2px #b08d4c; text-underline-offset:.16em`. Never change its color.

## Similar Brands

- **a16z.com** — 实抓 CSS：主色藏蓝 `#092344`、象牙系 `#f6f4ee / #f0ece3 / #e1d9c7`、灰褐线 `#aca08d`，衬线 Orpheus Pro 配 Domaine Sans。借了「藏蓝 + 象牙 + 灰金线」这组三色关系（本范式的 #0b1f3a / #f5f2ea / #b08d4c 由此校准），以及页脚用金属色细线收边的做法。
- **Harvard Business School Online（online.hbs.edu）** — 实抓 CSS：Tiempos 衬线标题 + Graphik 正文，圆角几乎全是 4px，暖白底 `#f6f4f2`，容器 1340px，唯一的大阴影是 `0 10px 45px rgba(0,0,0,.08)`。借了「衬线标题 / 无衬线正文」的分工、小圆角、1320–1340 的宽容器。
- **Harvard Business Review（hbr.org）** — 实抓 CSS：Tiempos Headline + GT America，圆角 2–3px，分隔线 `#e2e2e2` 用得极多、几乎没有阴影。借了「层级靠线不靠阴影」、目录式的文章列表（日期 / 栏目 / 标题 / 摘要分列）和 2px 圆角。
- **Bridgewater（bridgewater.com）** — 实抓 CSS：Mercury Display 衬线 + Whitney，`border-radius:0` 为主，阴影只有一档 `0 10px 40px rgba(0,0,0,.1)`，强调色砖红 `#80241e`。借了这一档阴影（只给画框）、直角图片，以及 `#80241e` 直接用作 destructive。
- **长江商学院（ckgsb.edu.cn）** — 实抓 CSS：主色亮蓝 `#0190c5 / #0b9ada`、5px 圆角、蓝色发光阴影 `0 4px 15px rgba(11,154,218,.3)`。这是反面锚点：同是中文商学院，亮蓝 + 发光阴影读起来像门户；本范式把蓝压到 #0b1f3a、去掉所有彩色阴影，就是为了和它拉开。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — ivory side */
  --color-background: #f5f2ea;
  --color-foreground: #111c2e;
  --color-card: #fbf9f4;
  --color-card-foreground: #111c2e;
  --color-popover: #fbf9f4;
  --color-popover-foreground: #111c2e;
  --color-secondary: #ebe6d9;
  --color-secondary-foreground: #111c2e;
  --color-muted: #ebe6d9;
  --color-muted-foreground: #4f5b6e;
  --color-accent: #ebe6d9;
  --color-accent-foreground: #111c2e;
  --color-border: #d9d3c3;
  --color-border-strong: #111c2e;
  --color-input: #8d8673;
  --color-ring: #0b1f3a;

  /* Colors — navy side */
  --color-primary: #0b1f3a;
  --color-primary-foreground: #f5f2ea;
  --color-primary-deep: #07162b;
  --color-primary-raised: #15305a;
  --color-primary-muted-foreground: #a9b4c6;
  --color-primary-border: #2a4166;
  --color-ring-inverse: #d4b97c;

  /* Colors — brass (lines and small labels only, ≤3%) */
  --color-brass: #b08d4c;
  --color-brass-deep: #765a1f;
  --color-brass-light: #d4b97c;

  /* Colors — status */
  --color-destructive: #80241e;
  --color-destructive-foreground: #fbf9f4;
  --color-success: #2f5d46;
  --color-success-foreground: #fbf9f4;

  /* Pastel semantic pairs */
  --color-pastel-navy-bg: #e1e7f0;
  --color-pastel-navy-text: #1d3a66;
  --color-pastel-brass-bg: #f0e7d0;
  --color-pastel-brass-text: #6b4f14;
  --color-pastel-stone-bg: #e7e3d8;
  --color-pastel-stone-text: #4a5261;
  --color-pastel-red-bg: #f4e2de;
  --color-pastel-red-text: #80241e;

  /* Typography — Font Families */
  --font-display:
    'Frank Ruhl Libre', 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC',
    STSong, SimSun, Georgia, serif;
  --font-serif:
    'Frank Ruhl Libre', 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC',
    STSong, SimSun, Georgia, serif;
  --font-sans:
    'Libre Franklin', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', 'Helvetica Neue', system-ui, sans-serif;
  --font-mono:
    'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    monospace;

  /* Typography — Scale */
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 22px;
  --text-heading: 28px;
  --text-heading-lg: clamp(30px, 3.2vw, 44px);
  --text-heading-xl: clamp(36px, 4.7vw, 68px);
  --text-display: clamp(52px, 8vw, 116px);

  /* Line Height & Tracking */
  --leading-display: 1.12;
  --leading-heading: 1.22;
  --leading-body: 1.8;
  --tracking-display: 0.01em;
  --tracking-heading: 0.02em;
  --tracking-body: 0.01em;
  --tracking-label: 0.16em;

  /* Spacing (4px base) */
  --spacing: 0.25rem;
  --section-gap: clamp(64px, 8vw, 120px);
  --page-gutter: clamp(20px, 5vw, 60px);
  --container: 1320px;

  /* Border Radius */
  --radius: 2px;
  --radius-sm: 1px;
  --radius-md: 2px;
  --radius-lg: 4px;
  --radius-full: 999px;

  /* Rules */
  --rule-hair: 1px;
  --rule-heavy: 2px;
  --rule-tab-width: 56px;
  --rule-tab-height: 3px;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(7, 22, 43, 0.06);
  --shadow-frame: 0 10px 40px 0 rgba(7, 22, 43, 0.1);
  --shadow-frame-navy: 0 18px 50px 0 rgba(3, 10, 22, 0.45);

  /* Motion */
  --ease-board: cubic-bezier(0.32, 0.72, 0, 1);
  --duration-fast: 180ms;
  --duration-slow: 600ms;
}
```

### Tailwind v4

```css
@theme {
  /* Colors — ivory side */
  --color-background: #f5f2ea;
  --color-foreground: #111c2e;
  --color-card: #fbf9f4;
  --color-card-foreground: #111c2e;
  --color-popover: #fbf9f4;
  --color-popover-foreground: #111c2e;
  --color-secondary: #ebe6d9;
  --color-secondary-foreground: #111c2e;
  --color-muted: #ebe6d9;
  --color-muted-foreground: #4f5b6e;
  --color-accent: #ebe6d9;
  --color-accent-foreground: #111c2e;
  --color-border: #d9d3c3;
  --color-border-strong: #111c2e;
  --color-input: #8d8673;
  --color-ring: #0b1f3a;

  /* Colors — navy side */
  --color-primary: #0b1f3a;
  --color-primary-foreground: #f5f2ea;
  --color-primary-deep: #07162b;
  --color-primary-raised: #15305a;
  --color-primary-muted-foreground: #a9b4c6;
  --color-primary-border: #2a4166;
  --color-ring-inverse: #d4b97c;

  /* Colors — brass (lines and small labels only, ≤3%) */
  --color-brass: #b08d4c;
  --color-brass-deep: #765a1f;
  --color-brass-light: #d4b97c;

  /* Colors — status */
  --color-destructive: #80241e;
  --color-destructive-foreground: #fbf9f4;
  --color-success: #2f5d46;
  --color-success-foreground: #fbf9f4;

  /* Pastel semantic pairs */
  --color-pastel-navy-bg: #e1e7f0;
  --color-pastel-navy-text: #1d3a66;
  --color-pastel-brass-bg: #f0e7d0;
  --color-pastel-brass-text: #6b4f14;
  --color-pastel-stone-bg: #e7e3d8;
  --color-pastel-stone-text: #4a5261;
  --color-pastel-red-bg: #f4e2de;
  --color-pastel-red-text: #80241e;

  /* Typography — Font Families */
  --font-display:
    'Frank Ruhl Libre', 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC',
    STSong, SimSun, Georgia, serif;
  --font-serif:
    'Frank Ruhl Libre', 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC',
    STSong, SimSun, Georgia, serif;
  --font-sans:
    'Libre Franklin', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', 'Helvetica Neue', system-ui, sans-serif;
  --font-mono:
    'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    monospace;

  /* Typography — Scale */
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 22px;
  --text-heading: 28px;
  --text-heading-lg: clamp(30px, 3.2vw, 44px);
  --text-heading-xl: clamp(36px, 4.7vw, 68px);
  --text-display: clamp(52px, 8vw, 116px);

  /* Line Height & Tracking */
  --leading-display: 1.12;
  --leading-heading: 1.22;
  --leading-body: 1.8;
  --tracking-display: 0.01em;
  --tracking-heading: 0.02em;
  --tracking-body: 0.01em;
  --tracking-label: 0.16em;

  /* Spacing (4px base) */
  --spacing: 0.25rem;
  --section-gap: clamp(64px, 8vw, 120px);
  --page-gutter: clamp(20px, 5vw, 60px);
  --container: 1320px;

  /* Border Radius */
  --radius: 2px;
  --radius-sm: 1px;
  --radius-md: 2px;
  --radius-lg: 4px;
  --radius-full: 999px;

  /* Rules */
  --rule-hair: 1px;
  --rule-heavy: 2px;
  --rule-tab-width: 56px;
  --rule-tab-height: 3px;

  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(7, 22, 43, 0.06);
  --shadow-frame: 0 10px 40px 0 rgba(7, 22, 43, 0.1);
  --shadow-frame-navy: 0 18px 50px 0 rgba(3, 10, 22, 0.45);

  /* Motion */
  --ease-board: cubic-bezier(0.32, 0.72, 0, 1);
  --duration-fast: 180ms;
  --duration-slow: 600ms;
}
```
