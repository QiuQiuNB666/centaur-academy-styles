# 半人马AI学院 · 夜航精密 — Style Reference

> 近黑画布上的仪表级克制，一点橙领航

**Theme:** dark

夜航精密的视觉语言建立在一块偏蓝的近黑画布（#0a0c10）上——不是纯黑，是夜间驾驶舱那种带冷色偏的深。层级不靠投影，靠 1px 发丝线（#212731 / #343c4a）和三级极弱的表面亮度差（#0f1217 → #151920 → #1b2029），每升一级只亮约 2%。主字体是思源黑体配 Geist：中文 500 字重、-0.02 ~ -0.03em 紧字距，拉丁与数字交给 Geist；Geist Mono 只做「坐标式标注」——章节号、图号、日期、英文眉标，像仪器面板上的刻字。Logo 橙 #f27a1a 是唯一强调色，全页累计 ≤5%：H1 的强调词、章节号、FIG. 图号、五步刻度、悬浮反馈，除此之外不出现；主按钮刻意用仪表白而不是橙，把橙留给「方向」。钴蓝只活在 logo 与半人马本体里，不进 UI。签名记忆点有两个，互为一体：**亮盒展品**——三张暖色纸感插画不硬贴在黑底上，而是装进「发丝线外框 + 图号刻度条 + 5px 暖纸衬边 + 图注 + 对位角标」的亮盒里，成为冷黑页面里唯一发暖的视觉锚点；**刻度尺与引线**——半人马抠图直接站在一把 8px/80px 刻度尺上，两条工程图式引线把「人的意愿」「能力的延伸」分别指向橙色人身与蓝色马身。全套拒绝霓虹、紫蓝渐变、玻璃拟态和星空粒子：要的是 Linear 的克制，让 45 岁的经营者觉得「精密、可靠、贵」，而不是「程序员网站」。

## Tokens — Colors

| Name              | Value     | Token                                                     | Role                                                  |
| ----------------- | --------- | --------------------------------------------------------- | ----------------------------------------------------- |
| 夜航黑            | `#0a0c10` | `--color-background`                                      | 主画布，偏蓝的近黑，全页约 70%                        |
| 仪表白            | `#eceef2` | `--color-foreground`                                      | 主文字、H2 强调词；对画布 16.9:1                      |
| 舱面一级          | `#0f1217` | `--color-card`                                            | 卡片、亮盒外框、联系横幅                              |
| 舱面二级          | `#151920` | `--color-secondary` / `--color-muted` / `--color-popover` | 次级底、移动菜单、禁用按钮底                          |
| 舱面三级          | `#1b2029` | `--color-accent`                                          | 悬浮态底色                                            |
| 仪表白主色        | `#eceef2` | `--color-primary`                                         | 主按钮底（hover 升到 `#ffffff`）                      |
| 夜航黑主前景      | `#0a0c10` | `--color-primary-foreground`                              | 主按钮上的文字                                        |
| 雾灰              | `#9aa3b2` | `--color-muted-foreground`                                | 次要正文、H2 非强调部分；7.7:1                        |
| 标注灰            | `#7f8999` | `--color-subtle-foreground`                               | 等宽标注、页脚小字；5.5:1（二级舱面上 5.0:1）         |
| 禁用灰            | `#5b6472` | `--color-disabled-foreground`                             | 仅禁用控件文字（豁免对比度），状态说明另用标注灰      |
| 发丝线            | `#212731` | `--color-border`                                          | 分割线、航道线、刻度小格                              |
| 强发丝线          | `#343c4a` | `--color-border-strong`                                   | 刻度大格、交点十字、描边按钮、对位角标                |
| 输入框线          | `#2a313d` | `--color-input`                                           | 输入框边框                                            |
| Logo 橙（不漂移） | `#f27a1a` | `--color-brand` / `--color-ring`                          | 取自 logo 人身；唯一强调色与焦点环，≤5%；对画布 7.1:1 |
| 亮盒衬纸          | `#f4eee3` | `--color-lightbox`                                        | 插画 5px 衬边，只在亮盒内出现                         |
| 信号红            | `#e5645a` | `--color-destructive`                                     | 表单错误，只作信号                                    |
| 信号绿            | `#5fb67c` | `--color-success`                                         | 「已复制」等成功反馈                                  |

### 柔和语义色（深底 + 亮字，成对使用）

| Name | Background | Text      | Token                      |
| ---- | ---------- | --------- | -------------------------- |
| 柔橙 | `#2a1a0e`  | `#f6a562` | `--color-pastel-orange-*`  |
| 柔蓝 | `#0f1c33`  | `#7fb0f5` | `--color-pastel-blue-*`    |
| 柔绿 | `#10231a`  | `#7fcf9b` | `--color-pastel-green-*`   |
| 中性 | `#1b2029`  | `#b9c0cc` | `--color-pastel-neutral-*` |

四对对比度均 ≥7.6:1。首页只用到柔橙（期刊「观点」标签）；其余留给内页状态。

## Tokens — Typography

### 思源黑体 Noto Sans SC — 中文主字体，标题 / 正文 / UI 通用 · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, system-ui（PingFang 的 Medium 与思源 500 字面宽度接近，回退后标题不换行、版式不塌）
- **Weights:** 400（正文）, 500（标题、按钮、强调）, 700（备用，首页未用）
- **Sizes:** 14px, 15px, 16px, 18px, 20px, 28px, 32–56px, 44–92px
- **Line height:** display 1.08 / 标题 1.2 / 正文 1.75
- **Letter spacing:** display -0.03em / 标题 -0.02em / 正文 0 / 署名与口号 +0.12em
- **Role:** 全站中文。大标题靠字号与紧字距取胜，不加粗到 700——500 在深色底上更锐、更不「喊」

### Geist — 拉丁与数字 · `--font-sans`（栈首）

- **Substitute:** system-ui, -apple-system（SF Pro）
- **Weights:** 400, 500, 600
- **Role:** 排在字体栈最前，只接管拉丁字母与数字（「AI」「↗」），中文自动落到思源黑体。禁用 Inter / Roboto / Arial

### Geist Mono — 坐标式标注 · `--font-mono`

- **Substitute:** ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas
- **Weights:** 400, 500
- **Sizes:** 9.5px（logo 下英文）, 11px, 12px, 14px（章节号）
- **Letter spacing:** +0.08em，全大写
- **OpenType features:** tnum, zero
- **Role:** 章节号、FIG. 图号、日期、英文眉标、状态说明。不用于中文长句与正文

### Type Scale

| Role       | Size                     | Line Height | Letter Spacing | Token               |
| ---------- | ------------------------ | ----------- | -------------- | ------------------- |
| display    | clamp(44px, 6.6vw, 92px) | 1.08        | -0.03em        | `--text-display`    |
| heading-lg | clamp(32px, 4.2vw, 56px) | 1.2         | -0.02em        | `--text-heading-lg` |
| heading    | 28px                     | 1.3         | -0.02em        | `--text-heading`    |
| subheading | 20px                     | 1.35        | 0.02em         | `--text-subheading` |
| body-lg    | 18px                     | 1.75        | 0              | `--text-body-lg`    |
| body       | 16px                     | 1.75        | 0              | `--text-body`       |
| body-sm    | 14px                     | 1.7         | 0              | `--text-body-sm`    |
| caption    | 12px（mono）             | 1.6         | 0.08em         | `--text-caption`    |
| label      | 11px（mono）             | 1.6         | 0.06em         | `--text-label`      |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 0.25rem`）

**Density:** 舒展。区块内边距 76–88px，正文行高 1.75——受众 35–55 岁，字不小于 14px，说明文字 18px

### Spacing Scale

| Name | Value | Token          |
| ---- | ----- | -------------- |
| 1    | 4px   | `--spacing-1`  |
| 2    | 8px   | `--spacing-2`  |
| 3    | 12px  | `--spacing-3`  |
| 4    | 16px  | `--spacing-4`  |
| 5    | 20px  | `--spacing-5`  |
| 6    | 24px  | `--spacing-6`  |
| 8    | 32px  | `--spacing-8`  |
| 10   | 40px  | `--spacing-10` |
| 12   | 48px  | `--spacing-12` |
| 16   | 64px  | `--spacing-16` |
| 24   | 96px  | `--spacing-24` |
| 32   | 128px | `--spacing-32` |

### Border Radius

| Name | Value       | Token         |
| ---- | ----------- | ------------- |
| sm   | 2px         | `--radius-sm` |
| md   | 4px         | `--radius-md` |
| lg   | 6px（base） | `--radius-lg` |
| xl   | 10px        | `--radius-xl` |

| Element         | Value     |
| --------------- | --------- |
| 按钮 / 输入框   | 6px (lg)  |
| 卡片 / 亮盒外框 | 6px (lg)  |
| 亮盒衬纸 / 徽标 | 2px (sm)  |
| 导航项 / 图标格 | 4px (md)  |
| 联系横幅        | 10px (xl) |

精密感来自小圆角：全站没有胶囊形，没有 ≥12px 的圆角。

### Shadows

| Name     | Value                                                                         | Token               |
| -------- | ----------------------------------------------------------------------------- | ------------------- |
| edge     | `inset 0 1px 0 0 rgba(255,255,255,0.05)`                                      | `--shadow-edge`     |
| pop      | `0 16px 48px -8px rgba(0,0,0,0.6)`                                            | `--shadow-pop`      |
| lightbox | `0 0 0 1px rgba(255,255,255,0.04), 0 48px 120px -56px rgba(244,238,227,0.16)` | `--shadow-lightbox` |
| ground   | `rgba(214,224,240,0.1)`（径向渐变用色，不是 box-shadow）                      | `--ground-light`    |

深色下投影看不见也不需要：面板只有一道 5% 的顶边高光；亮盒下方有一层 16% 暖纸色的溢光（模拟灯箱落在桌面上的光，不是霓虹）；半人马脚下是一块 10% 的冷白地面光。只有移动菜单用 `--shadow-pop`。

### Motion

| Name          | Value                            | Token             |
| ------------- | -------------------------------- | ----------------- |
| ease-precise  | `cubic-bezier(0.19, 1, 0.22, 1)` | `--ease-precise`  |
| duration-fast | `140ms`（颜色、边线）            | `--duration-fast` |
| duration-base | `260ms`（箭头 1–3px 位移）       | `--duration-base` |

只动 transform / opacity / 颜色。亮盒内的插画在进入视口时 scale 1.05→1（`animation-timeline: view()`，包在 `@supports` 与 `prefers-reduced-motion: no-preference` 里，终态即默认态）。不钉滚动、不视差。

### Layout

- **Section gap:** 区块之间不留空白带，用一条通栏发丝线 + 航道交点十字分隔；区块内边距 76–88px
- **Card padding:** 24px；亮盒外框 12px + 衬纸 5px
- **Element gap:** 12 列栅格，列间距 32px
- **Max content width:** 1240px（`--page-max`），页边 `clamp(20px, 3.2vw, 40px)`
- **刻度:** 小格 8px（`--tick-minor`）、大格 80px（`--tick-major`）

## Components

### Primary Button

**Role:** 主 CTA（全页两处：Hero、联系横幅）
`bg-primary`(#eceef2) `text-primary-foreground`(#0a0c10), `border-radius: var(--radius-lg)`(6px), `min-height: 44px`, `padding: 0 8px 0 20px`, `font: 15px/500`. 箭头 ↗ 收在右侧 28×28 的内嵌方格里（4px 圆角、10% 前景色底）。hover: 底升到 #ffffff，箭头格向右上移 1px；active: scale(0.98)；focus-visible: 2px 橙环、offset 3px。

### Outline Button

**Role:** 次级动作（Header 的联系按钮、复制客服链接）
透明底 + `border-border-strong`(#343c4a) 1px。hover: `bg-accent`(#1b2029)，边线升到标注灰。Header 内用 36px 高的 sm 尺寸。

### Ghost / Nav Item

**Role:** 顶部导航
雾灰文字、无边框，hover 出现 `bg-accent` 4px 圆角底，文字升到仪表白。

### Text Link

**Role:** 章节内「了解…… ↗」
仪表白 15px/500 + 下方 1px 强发丝线（用 background 画，不用 text-decoration）。hover: 文字与线一起变橙，箭头位移 2px。触控高度 44px。

### Disabled Button

**Role:** 「下载知君 ↓ / 下载万象 ↓」
`bg-secondary`(#151920) + 发丝线 + 禁用灰文字，`cursor: not-allowed`。下方必须跟一行标注灰的等宽说明「下载暂未开放」——禁用态不能只靠变灰表达。

### 亮盒展品 Lightbox Figure（签名组件）

**Role:** 三张章节插画、期刊封面
外框：`bg-card` + 发丝线 + 6px 圆角 + `--shadow-edge` + `--shadow-lightbox`，内边距 12px。头部：等宽「FIG. 01」（FIG. 为橙）+ 一段 8px 高的刻度条。中间：`--color-lightbox` 暖纸衬边 5px、2px 圆角，图片 4:3 裁切。底部图注：等宽英文 ｜ 中文说明。外框左上、右下各一枚 12px 的 L 形对位角标（强发丝线），偏移 -9px。缩略图版（期刊行）去掉头部、图注与角标，衬边收到 3px。

### Hero Figure 刻度地台 + 引线（签名组件）

**Role:** 首屏主视觉
`academy-centaur-cutout.webp` 直接放在画布上，占 5–12 列并向右出血 24px；`margin-bottom: -6.4%` 让马蹄正好踩在一把通栏刻度尺上；脚下一块椭圆径向地面光（`--ground-light`）。两条引线：标签（13px 雾灰）+ 1px 强发丝线 + 5px 橙色空心方节点，分别停在人身肩部与马背。图片层级高于刻度尺，刻度不许画到马蹄上。右侧航道线上另有一把竖向刻度（同 8/80px，宽 10px，自地台向上至多 560px），与横尺合成一个「量高台」。≤1080px 时引线隐藏，图注改回整句；≤900px 文案与图上下叠放，图宽 ≤620px 靠右并上提 140px 与文案错位，竖尺隐藏。

### Chapter Row

**Role:** 三个叙事章节
12 列：1–2 列为章节标（橙色等宽「01」+ 24px 短线 + 14px 雾灰章节名），文案 4 列，亮盒 6 列；02 章左右互换。H2 整体用雾灰，强调词提亮到仪表白——橙色不进 H2。

### Step Strip

**Role:** 共学五步
顶部一把刻度尺，下面五等分列，列间发丝线；每列起点有一根 10px 的橙色刻度线刺进刻度尺。等宽编号 01–05 用标注灰，标题 20px/500，说明 15px 雾灰。≤900px 变纵向列表（五等分在平板上每列不足 140px，说明会掉孤字），橙刻度变成每行顶线最左 10px 的橙色段。

### Journal Lead + Rows

**Role:** 观点与动态
左 7 列主推（大亮盒封面 16:9 + 标签/日期 + 28px 标题 + 摘要），右 5 列两条期刊行（文字 + 132px 方形缩略亮盒），行间只用发丝线，不进卡片。hover 只让标题变橙。≤1080px 改为上下两段：主推变「亮盒 7 列 + 文字 5 列」的横排，两条期刊行通栏；标题按语义分段 `nowrap`，不许在词中断行（「我/们」）。

### Quote Block

**Role:** 院长寄语
引文 clamp(26px, 3.1vw, 42px)/500，悬挂引号（`text-indent: -0.5em`），不加装饰引号图形。右侧署名栏用一条发丝线隔开：姓名 28px、字距 +0.12em。

### Contact Banner

**Role:** 页尾行动区
`bg-card` + 发丝线 + 10px 圆角 + 顶边高光；左上角一段 64×2px 的橙色指示线；底边一把刻度尺。左 H2，右说明 + 主按钮 + 描边按钮。

### Standard Card

**Role:** 通用容器（首页几乎不用，留给内页）
`bg-card` + `border-border` 1px + 6px 圆角 + `--shadow-edge`，padding 24px。hover：底升到 `bg-secondary`、边线换强发丝线，不位移、不发光。

### Input Field

**Role:** 文本输入
`bg-background` + `border-input`(#2a313d) 1px，6px 圆角，高 44px，padding 0 12px。focus：边线变橙 + 2px 30% 橙外环；error：`border-destructive` + 下方等宽提示。

### Badge

**Role:** 分类与状态标签
2px 圆角的面板标签（不做胶囊），等宽 12px、字距 +0.1em、padding 3px 7px，用柔和语义色成对上色；图号类用描边版（强发丝线 + 雾灰字）。

## Surfaces

| Level | Name                | Value     | Purpose                              |
| ----- | ------------------- | --------- | ------------------------------------ |
| 0     | background          | `#0a0c10` | 主画布                               |
| 1     | card                | `#0f1217` | 卡片、亮盒外框、联系横幅             |
| 2     | secondary / popover | `#151920` | 次级底、移动菜单、禁用控件           |
| 3     | accent              | `#1b2029` | 悬浮态                               |
| ✦     | lightbox            | `#f4eee3` | 亮盒衬纸——唯一的亮面，只包着插画出现 |

## Do's and Don'ts

### Do

- 主背景一律 `#0a0c10`。它带蓝偏，暖色插画和橙色才会「亮」起来；换成纯黑或中性灰黑，整页会变脏。
- 层级用线不用影：先试一条发丝线，不够再升一级表面色，永远不要加投影。
- Logo 橙只给「方向」：H1 强调词、章节号、FIG.、五步刻度、悬浮与焦点反馈，全页 ≤5%。
- H2 强调词的做法是「雾灰对仪表白」，不是上色。
- 每一张暖色插画都要进亮盒（外框 + 衬纸 + 图注），让它读作「展品」。
- 等宽字只写标注：章节号、图号、日期、英文眉标、状态说明，全大写 +0.08em。
- 编号只给真实顺序：三章节（01–03）、对应图号（FIG. 01–03）、共学五步（01–05）。
- 次要文字用 `#9aa3b2`（7.7:1），标注用 `#7f8999`（≥5:1）；正文不小于 14px，说明文字 18px。
- 动效用 `var(--ease-precise)`，颜色 140ms，位移 ≤3px。

### Don't

- 不要霓虹外发光、紫蓝渐变、玻璃拟态卡片、星空粒子、侧边光带——这是驾驶舱，不是赛博朋克。
- 不要用纯黑 `#000000` 做画布，也不要用纯白 `#ffffff` 做正文（只有主按钮 hover 用到）。
- 不要把钴蓝拿来做链接色或按钮色——蓝色属于半人马的身体，UI 里出现第二个强调色，橙就不值钱了。
- 不要把主按钮做成橙色。橙色按钮 + 橙色 H1 会把首屏的橙推到 10% 以上。
- 不要把插画直接铺在黑底上，也不要给插画加暗色蒙版压暗——用亮盒框住，保持原色。
- 不要用 ≥12px 的圆角和胶囊形；不要三张等宽卡片排一排；不要把内容都装进卡片——期刊、产品行、引文都只用线。
- 不要给区块加「01 / 02 / 03」式装饰编号，不要编造数字、客户 logo、学员数。
- 不要用 Inter / Roboto / Arial；不要给中文长句用等宽字。
- 不要在组件里写裸 hex——全部走 `tokens.css`。

## Imagery

图像只有两类，处理方式截然不同。**抠图**（`academy-centaur-cutout.webp`）是唯一可以直接站在画布上的图像：橙与钴蓝在冷黑底上饱和度最高，脚下配一块 10% 冷白地面光和一把刻度尺，旁边两条工程图式引线做标注——像博物馆里打了光的雕塑。**暖色场景插画**（experience / co-learning / creating，以及米色底的 hero 图）一律进亮盒：暖纸衬边让图的米色有过渡，外框、图号与图注把它变成「展品」，下方一层极弱的暖色溢光暗示盒内有光。插画保持原色，不叠暗、不单色化；裁切只用 4:3（章节）、16:9（期刊主推）、1:1（缩略）。图标不用图标库：箭头直接用字符 ↗ → ↓，菜单用三条 1px 线，装饰只有 CSS 画的刻度尺、交点十字和 L 形角标。不使用 emoji、彩色圆点、渐变色块。

## Layout

1240px 容器、12 列、列距 32px。容器左右各有一条贯穿全页的发丝「航道线」，每个区块顶部一条通栏发丝线，与航道线的交点画 9px 十字——整页像一张被网格标定过的图纸，但网格本身几乎看不见。Header sticky、64px 高、86% 画布色 + 14px 背景模糊（全站只有这一处用模糊）。Hero 是左文右图的不对称构图：文案占 1–6 列垂直居中，半人马占 5–12 列并向右出血，马蹄踩在通栏刻度尺上，刻度尺下方一条 72px 的底栏放主张句与图注。三个章节是「章节标 2 列 + 文案 4 列 + 亮盒 6 列」，第二章镜像。五步是五等分刻度带。期刊是 7 + 5 的主推加两行。寄语是 2 + 7 + 3。联系是一块内嵌面板。≤1080px：期刊上下分段、产品行的下载钮落到名称下方；≤900px：Hero 叠放、五步变纵向列表；<768px：航道线与十字隐藏，全部单列，亮盒满宽，导航收进 44px 菜单钮。

## Agent Prompt Guide

Quick Color Reference:

```
background: #0a0c10
foreground: #eceef2
card: #0f1217
secondary: #151920
border: #212731 / strong #343c4a
muted-foreground: #9aa3b2
subtle (mono labels): #7f8999
brand (≤5%): #f27a1a
lightbox mat: #f4eee3
primary button: #eceef2 bg, #0a0c10 text
```

Example Component Prompts:

1. Create a lightbox figure: outer `bg-card`(#0f1217) `border`(#212731) `rounded-[6px]` `p-3`, inset top highlight `rgba(255,255,255,.05)`; header row with mono uppercase `FIG. 01` (FIG. in #f27a1a, number in #7f8999, 12px, tracking .08em) followed by an 8px-tall tick ruler (1px ticks every 8px in #212731, taller every 80px in #343c4a); image wrapped in a 5px `#f4eee3` mat with 2px radius, 4:3 crop; caption row: mono English label ｜ 14px Chinese caption in #9aa3b2; two 12px L-shaped corner marks in #343c4a offset -9px at top-left and bottom-right. No glow, no dark overlay on the image.
2. Create a primary CTA: `bg-[#eceef2]` `text-[#0a0c10]`, `rounded-[6px]`, `h-11 pl-5 pr-2`, `text-[15px] font-medium`, trailing ↗ inside a 28×28 `rounded-[4px]` square tinted 10% of the text color; hover bg #ffffff and move the arrow square translate(1px,-1px) with `cubic-bezier(.19,1,.22,1)`; active scale .98; focus-visible 2px #f27a1a ring, offset 3px. Never make it orange.
3. Create a chapter heading: H2 `text-[clamp(32px,4.2vw,56px)] font-medium tracking-[-0.02em] leading-[1.2]` in #9aa3b2, with the emphasis word wrapped in `<em>` set to #eceef2 (no italics, no color accent). To its left, a 2-column meta rail: mono `01` in #f27a1a, a 24px hairline, then the chapter name in 14px #9aa3b2.
4. Create a 5-step strip: a full-width tick ruler on top; below it 5 equal columns separated by 1px #212731 lines; each column starts with a 10px-tall 1px #f27a1a tick poking into the ruler, mono number `01`–`05` in #7f8999, 20px/500 title in #eceef2, 15px description in #9aa3b2. On mobile, stack as rows with a 48px number column.

## Similar Brands

- **Linear（linear.app）** — 核心锚点。实读其 CSS：画布 `#08090a`、表面分级 `#0f1011 / #141516 / #191a1b`（每级约 +2% 亮度）、线色 `#23252a`、文字 `#f7f8f8 / #8a8f98`、大标题字距 -0.022em、字重 510/590。借了：「表面亮度差极小 + 线比面重要」的分层法、标题紧字距与中等字重、H2「灰句 + 白强调词」的写法。没借：它的靛紫强调色与 Inter。
- **Vercel / Geist（vercel.com）** — 实读：`--geist-radius: 6px`、marketing 圆角 8px、页宽 1200px、深色灰阶 `#1a1a1a / #1f1f1f / #2e2e2e`、半透明线 `#ffffff24`。借了：6px 基准圆角、Geist + Geist Mono 字体家族、贯穿全页的竖向栅格线与交点十字。
- **Raycast（raycast.com）** — 实读：画布 `#07080a`（偏蓝近黑）、`--color-bg-100: #101111`、线 `#242728`、文字 `#f4f4f6 / #c2c7ca`、主按钮 `#ffffffd0` 底 + `#18191a` 字、Geist Mono 作标注字体。借了：画布的蓝色偏、「深色站的主按钮用白不用品牌色」、等宽字做小标注。
- **Cursor（cursor.com）** — 实读：深色画布 `#14120b`（偏暖）、卡片 `#1b1913`、强调橙 `#f54e00`、线用前景色 2.5–20% 混合、页宽 1300px。借了：「深底上只放一个橙」的配比验证；刻意没跟它的暖黑——我们的插画已经很暖，画布必须冷。
- **Resend（resend.com）** — 实读：深色灰阶 `#141517 / #191b1e / #212629`（带蓝绿偏）、等宽 Commit Mono 做标注、展示字体与正文字体分离。借了：深色底上把实物图像当「打了光的展品」来陈列的做法，落成本范式的亮盒与地面光。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — surfaces */
  --color-background: #0a0c10;
  --color-foreground: #eceef2;
  --color-card: #0f1217;
  --color-card-foreground: #eceef2;
  --color-popover: #151920;
  --color-popover-foreground: #eceef2;
  --color-primary: #eceef2;
  --color-primary-foreground: #0a0c10;
  --color-primary-hover: #ffffff;
  --color-secondary: #151920;
  --color-secondary-foreground: #eceef2;
  --color-muted: #151920;
  --color-muted-foreground: #9aa3b2;
  --color-subtle-foreground: #7f8999;
  --color-disabled-foreground: #5b6472;
  --color-accent: #1b2029;
  --color-accent-foreground: #eceef2;
  --color-brand: #f27a1a;
  --color-brand-foreground: #0a0c10;
  --color-destructive: #e5645a;
  --color-destructive-foreground: #0a0c10;
  --color-success: #5fb67c;
  --color-success-foreground: #0a0c10;
  --color-border: #212731;
  --color-border-strong: #343c4a;
  --color-input: #2a313d;
  --color-ring: #f27a1a;

  /* Lightbox — 亮盒展品的衬纸与盒内文字 */
  --color-lightbox: #f4eee3;
  --color-lightbox-foreground: #1a1d23;
  --color-lightbox-muted: #5a5f69;

  /* Pastel semantic pairs (dark: 深底 + 亮字) */
  --color-pastel-orange-bg: #2a1a0e;
  --color-pastel-orange-text: #f6a562;
  --color-pastel-blue-bg: #0f1c33;
  --color-pastel-blue-text: #7fb0f5;
  --color-pastel-green-bg: #10231a;
  --color-pastel-green-text: #7fcf9b;
  --color-pastel-neutral-bg: #1b2029;
  --color-pastel-neutral-text: #b9c0cc;

  /* Typography — Font Families */
  --font-sans:
    'Geist', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', ui-sans-serif, system-ui, -apple-system, sans-serif;
  --font-mono:
    'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    'PingFang SC', 'Microsoft YaHei', monospace;

  /* Typography — Scale */
  --text-label: 11px;
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 20px;
  --text-heading: 28px;
  --text-heading-lg: clamp(32px, 4.2vw, 56px);
  --text-display: clamp(44px, 6.6vw, 92px);

  /* Line Height & Tracking */
  --leading-display: 1.08;
  --leading-heading: 1.2;
  --leading-body: 1.75;
  --tracking-display: -0.03em;
  --tracking-heading: -0.02em;
  --tracking-body: 0em;
  --tracking-label: 0.08em;

  /* Font weights */
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-semibold: 600;

  /* Spacing (4px base) */
  --spacing: 0.25rem;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 20px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-10: 40px;
  --spacing-12: 48px;
  --spacing-16: 64px;
  --spacing-24: 96px;
  --spacing-32: 128px;

  /* Layout */
  --page-max: 1240px;
  --page-gutter: clamp(20px, 3.2vw, 40px);
  --header-height: 64px;
  --tick-minor: 8px;
  --tick-major: 80px;

  /* Border Radius */
  --radius: 0.375rem;
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);

  /* Shadows — 深色下不靠投影分层，只留顶边高光与亮盒溢光 */
  --shadow-none: 0 0 0 0 transparent;
  --shadow-edge: inset 0 1px 0 0 rgba(255, 255, 255, 0.05);
  --shadow-pop: 0 16px 48px -8px rgba(0, 0, 0, 0.6);
  --shadow-lightbox:
    0 0 0 1px rgba(255, 255, 255, 0.04),
    0 48px 120px -56px rgba(244, 238, 227, 0.16);
  --ground-light: rgba(214, 224, 240, 0.1);

  /* Motion */
  --ease-precise: cubic-bezier(0.19, 1, 0.22, 1);
  --duration-fast: 140ms;
  --duration-base: 260ms;
}
```

### Tailwind v4

```css
@theme {
  --color-background: #0a0c10;
  --color-foreground: #eceef2;
  --color-card: #0f1217;
  --color-card-foreground: #eceef2;
  --color-popover: #151920;
  --color-popover-foreground: #eceef2;
  --color-primary: #eceef2;
  --color-primary-foreground: #0a0c10;
  --color-primary-hover: #ffffff;
  --color-secondary: #151920;
  --color-secondary-foreground: #eceef2;
  --color-muted: #151920;
  --color-muted-foreground: #9aa3b2;
  --color-subtle-foreground: #7f8999;
  --color-disabled-foreground: #5b6472;
  --color-accent: #1b2029;
  --color-accent-foreground: #eceef2;
  --color-brand: #f27a1a;
  --color-brand-foreground: #0a0c10;
  --color-destructive: #e5645a;
  --color-destructive-foreground: #0a0c10;
  --color-success: #5fb67c;
  --color-success-foreground: #0a0c10;
  --color-border: #212731;
  --color-border-strong: #343c4a;
  --color-input: #2a313d;
  --color-ring: #f27a1a;
  --color-lightbox: #f4eee3;
  --color-lightbox-foreground: #1a1d23;
  --color-lightbox-muted: #5a5f69;
  --color-pastel-orange-bg: #2a1a0e;
  --color-pastel-orange-text: #f6a562;
  --color-pastel-blue-bg: #0f1c33;
  --color-pastel-blue-text: #7fb0f5;
  --color-pastel-green-bg: #10231a;
  --color-pastel-green-text: #7fcf9b;
  --color-pastel-neutral-bg: #1b2029;
  --color-pastel-neutral-text: #b9c0cc;
  --font-sans: 'Geist', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', ui-sans-serif, system-ui, -apple-system, sans-serif;
  --font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'PingFang SC', 'Microsoft YaHei', monospace;
  --text-label: 11px;
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 20px;
  --text-heading: 28px;
  --text-heading-lg: clamp(32px, 4.2vw, 56px);
  --text-display: clamp(44px, 6.6vw, 92px);
  --spacing: 0.25rem;
  --radius: 0.375rem;
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  --shadow-none: 0 0 0 0 transparent;
  --shadow-edge: inset 0 1px 0 0 rgba(255, 255, 255, 0.05);
  --shadow-pop: 0 16px 48px -8px rgba(0, 0, 0, 0.6);
  --shadow-lightbox: 0 0 0 1px rgba(255, 255, 255, 0.04), 0 48px 120px -56px rgba(244, 238, 227, 0.16);
  --ease-precise: cubic-bezier(0.19, 1, 0.22, 1);
}
```
