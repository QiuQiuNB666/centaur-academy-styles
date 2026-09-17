# 半人马AI学院 · 报告版 — Style Reference

> 把学院写成一本年度报告：白纸与暖灰交替，一支钴蓝，发丝线分格，图像只有一种处理

**Theme:** light（白 / 暖灰交替分区，院长左页与联系、页脚用黑场）

这一版的骨架照 AI in Design Report 2026（stateofaidesign.com）逐屏搭：顶栏是一截书脊——黑方块字标、钴蓝满高 CTA 条、纯文字导航；首屏上半是一整条切片拼贴，下半是不对称的两栏，导语缩在左窄栏，132px 的紧排大标题从 41.47% 的右栏起笔线出发，这条线贯穿全页，所有正文、章节引语、黑条按钮都从它起。三个叙事章节写成报告小节：左栏「章节号 + 章名」同字号，右栏衬线大引语，下半「切片图框 ｜ 图注 + 黑条按钮」。钴蓝 #0c6ccc 是唯一的界面强色，只出现在顶栏 CTA、主按钮、强调词、目录里的「§07」一格和放大舞台的构图线上，全页累计面积不超过 6%；logo 的橙只留在 logo 和插画里，界面一处不用。灰全部带同一个暖色相（#f3f1ec → #e9e6df → #dcd8cf → #57534b → #1b1916），暖插画放进来不打架。层次只靠三样东西：1px 线（黑色分区线、暖发丝、蓝网格）、底色切换、字号跳变——零圆角面、零阴影，唯一的圆是胶囊按钮。签名记忆点是「滑动放大」：首屏拼贴里那格暖灰网格上站着半人马抠图（scale 0.5），往下滚 640px，拼贴向两侧退场、导语淡出，半人马放大到 740px 居中，钴蓝构图线从中心展开，「人的意愿 / 能力的延伸 / HUMAN × AI」三条标注在终态浮现，然后释放进入目录。

## Tokens — Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| 纸白 | `#ffffff` | `--color-paper` | 主画布、目录格、按钮上的字 |
| 暖灰 | `#f3f1ec` | `--color-stone` | 与纸白交替的分区底（章节 01/03、观点、放大舞台） |
| 深暖灰 | `#e9e6df` | `--color-stone-deep` | 图框衬底（灰阶叠印的底色）、院长寄语右页 |
| 暖发丝 | `#dcd8cf` | `--color-rule` | 列表分隔线、台阶竖线、黑场外的次级线 |
| 暖墨 | `#1b1916` | `--color-ink` | 正文、标题、分区顶部 1px 黑线 |
| 次要墨 | `#57534b` | `--color-ink-muted` | 说明、日期；白底 7.65:1，暖灰底 6.78:1，深暖灰底 6.14:1 |
| 禁用底 | `#e4e1da` | `--color-disabled-bg` | 「下载知君 / 下载万象」禁用按钮 |
| 禁用字 | `#6d685f` | `--color-disabled-fg` | 禁用按钮文字（4.24:1，禁用态豁免但仍可读） |
| 黑场 | `#0f0e0c` | `--color-night` | 书脊字标块、院长左页、联系区、页脚 |
| 黑场浮层 | `#1c1a17` | `--color-night-raised` | 黑场按钮悬停底 |
| 黑场线 | `#3a3730` | `--color-night-rule` | 页脚分隔线 |
| 黑场字 | `#f3f1ec` | `--color-on-night` | 黑场主文字，17.09:1 |
| 黑场次要字 | `#aaa498` | `--color-on-night-muted` | 黑场说明、书眉，7.78:1 |
| 钴蓝（唯一强色） | `#0c6ccc` | `--color-cobalt` | 顶栏 CTA 条、主按钮、强调词、§07 格；白字 5.21:1，≤6% |
| 深钴蓝 | `#0a58a8` | `--color-cobalt-deep` | 钴蓝元素的悬停 / 按下；白字 7.06:1 |
| 黑场钴蓝 | `#5c9fe6` | `--color-cobalt-on-night` | 黑场上的引号、链接悬停，6.94:1 |
| 蓝发丝 | `#d3e0f1` | `--color-grid` | 满屏栅格线、目录格缝、拼贴舞台网格 |
| 黑场蓝发丝 | `#26303d` | `--color-grid-night` | 预留：黑场上的网格线 |
| logo 橙（界面禁用） | `#f07800` | `--color-logo-orange` | 只存在于 logo 与插画，不许进任何界面元素 |

### 成对色（底 + 字，本范式没有柔和语义色）

报告体不用粉彩状态色。需要「状态」时只用下面四对，靠明暗和线表达：

| Name | Background | Text | Token |
| --- | --- | --- | --- |
| 纸面 | `#ffffff` | `#1b1916` | `--color-paper` / `--color-ink` |
| 分区 | `#f3f1ec` | `#57534b` | `--color-stone` / `--color-ink-muted` |
| 黑场 | `#0f0e0c` | `#aaa498` | `--color-night` / `--color-on-night-muted` |
| 强调 | `#0c6ccc` | `#ffffff` | `--color-cobalt` / `--color-paper` |

### 线色

| Name | Value | Token | 用在哪 |
| --- | --- | --- | --- |
| 分区黑线 | `#1b1916` 1px | `--color-ink` | 每个分区、每个章节的顶线（照 ② 的「线 + 等宽标签」） |
| 暖发丝 | `#dcd8cf` 1px | `--color-rule` | 列表行、台阶竖线 |
| 蓝发丝 | `#d3e0f1` 1px | `--color-grid` | 满屏栅格：左边距线、右栏起笔线、右边距线；目录格缝 |
| 构图线 | `#0c6ccc` 1px × 35% 不透明 | `--color-cobalt` | 只在放大舞台终态出现 |

## Tokens — Typography

### Instrument Sans + Noto Sans SC — 喊：展示与界面 · `--font-display` / `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif
- **Weights:** 拉丁 400–700（可变）；中文 400 / 500 / 700 / 900
- **Sizes:** 12, 14, 16, 18, 22, 32, 50, 78, 132px；页脚字标 15.8vw（上限 250px）
- **Line height:** 展示 1.02–1.06 / 标题 1.22 / 正文 1.7
- **Letter spacing:** 展示 -0.02em（字标 -0.03em，数字 -0.04em）/ 正文 0
- **Role:** 大字（H1、章名、分区标题、联系标题）一律 500，照 ② 的 Medium；22–32px 的小标题、目录格、产品名、页脚字标用 700。用于首屏 H1、章节号与章名、目录格标题、共学台阶数字、页脚字标、全部正文。拉丁在前、中文在后：「AI」「01」由 Instrument Sans 出字，汉字交给 Noto Sans SC。字体没加载到时回退苹方，标题靠字号撑住，不靠字重。

### Instrument Serif + Noto Serif SC — 讲：叙述句 · `--font-serif`

- **Substitute:** Songti SC, STSong, SimSun, serif
- **Weights:** 拉丁 400；中文 500 / 700
- **Sizes:** 18, 22–30, 56px；院长寄语 32–60px
- **Line height:** 1.26–1.36
- **Letter spacing:** -0.01em
- **Role:** 首屏副标题、章节大引语（H2）、图注中文句、院长寄语、首屏底栏「人决定方向，AI 拓展人的能力。」。只讲故事，不做按钮和导航。

### Geist Mono — 标：书眉、标签、日期 · `--font-mono`

- **Substitute:** ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
- **Weights:** 400, 500
- **Sizes:** 9px（字标副名）, 10px（图框标签）, 12px（书眉）
- **Letter spacing:** 0.06em，全大写
- **Role:** 分区书眉（「目录 / INDEX」「§04」）、图框小白标签（EXPERIENCE）、日期「观点 · 2026.09.15」、放大终态标注。中文混排时汉字回退系统黑体，保持 12px。

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| wordmark | clamp(40px, 15.8vw, 250px) | 0.92 | -0.03em | `--text-wordmark` |
| display-xl | clamp(50px, 9.2vw, 132px) | 1.06 | -0.02em | `--text-display-xl` |
| display-l | clamp(40px, 5.4vw, 78px) | 1.02 | -0.02em | `--text-display-l` |
| quote（衬线） | clamp(30px, 3.9vw, 56px) | 1.3 | -0.01em | `--text-quote` |
| display-m | clamp(30px, 3.5vw, 50px) | 1.22 | -0.02em | `--text-display-m` |
| heading | clamp(24px, 2.3vw, 32px) | 1.22 | -0.01em | `--text-heading` |
| title | 22px | 1.3 | 0 | `--text-title` |
| body-lg | 18px | 1.7 | 0 | `--text-body-lg` |
| body | 16px | 1.7 | 0 | `--text-body` |
| body-sm | 14px | 1.6 | 0 | `--text-body-sm` |
| label（等宽） | 12px | 1.3 | 0.06em | `--text-label` |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 0.25rem`）

**Density:** 报告式——分区内部紧（45–90px），分区之间松（150–250px），满屏色块下方故意留空

### Spacing Scale

| Name | Value | Token |
| --- | --- | --- |
| gutter | 16px（页边距与栏缝同值，照 ②） | `--gutter` |
| split | 0.4147（右栏起笔线位置，1440 下约 601px） | `--split` |
| measure | 454px（右栏正文最大行宽，约 28 个汉字） | `--measure` |
| header | 56px | `--header-h` |
| section-a | clamp(72px, 10vw, 150px) | `--space-section-a` |
| section-b | clamp(96px, 16vw, 250px) | `--space-section-b` |
| section-c | clamp(48px, 6vw, 90px) | `--space-section-c` |
| 章节内留白 | 01 章 170px / 02 章 96px / 03 章 210px（每章不同） | 页内 `.ch-gap-1/2/3` |

### Border Radius

| Name | Value | Token |
| --- | --- | --- |
| none | 0px | `--radius-none` |
| pill | 999px | `--radius-pill` |

| Element | Value |
| --- | --- |
| 面（分区、图框、目录格、黑条、输入框、顶栏） | 0 |
| 按钮（主按钮、黑场描边按钮、禁用下载） | pill |
| 等宽标签 | 0 |
| 日期胶囊（仅样张） | pill |

### Shadows

| Name | Value | Token |
| --- | --- | --- |
| none | `none` | `--shadow-none` |

全站不用阴影。层次只来自线、底色和字号。半人马抠图脚下那片影子是图里自带的，不是 CSS。

### Motion

| Name | Value | Token |
| --- | --- | --- |
| ease-report | `cubic-bezier(0.44, 0, 0.37, 1)` | `--ease-report` |
| ease-link | `cubic-bezier(0.44, 0, 0.56, 1)` | `--ease-link` |
| duration-fast | 0.2s | `--duration-fast` |
| zoom-distance | 640px（钉住段额外滚动距离，≤120vh） | `--zoom-distance` |
| zoom-max-width | 740px（终态宽度上限，1448px 原图在 2x 屏不糊） | `--zoom-max-width` |

- 悬停只动颜色（0.2s ease-link），按下 `scale(.97)`。
- 滑动放大：CSS `animation-timeline: scroll(root)`，`animation-range: 0 640px`，整段放在 `@supports (animation-timeline: scroll())` 和 `prefers-reduced-motion: no-preference` 里；只动 `translate / scale / opacity`。盒子按终态 740px 排版，从 `scale(.5)`（手机 .62）放到 `scale(1)`，不从 1 往上放。不支持或减少动效时：不钉住，首屏拼贴里静态放半人马，下面单独排一段暖灰舞台显示终态。

### Layout

- **Section gap:** 150–250px（分区之间）；45–90px（分区内部）
- **Card padding:** 目录格 18px；黑条左右 20px
- **Element gap:** 16px（与页边距同值）
- **Max content width:** 不设上限，满宽 16px 边距；正文限 454px；终态半人马限 740px

## Components

### 顶栏 · 书脊

**Role:** 全站导航
高 56px，底部 1px 暖墨线，sticky。左格宽度 = 右栏起笔线：黑场字标块（logo 36px + 「半人马AI学院」17px/700 + 9px 等宽「CENTAUR AI ACADEMY」）紧接钴蓝满高条，条内右对齐「联系学院顾问 ↗」17px/500，悬停变深钴蓝。右格纯文字导航 17px/500，悬停出 1px 下划线。<900px 时导航收进钴蓝条「菜单 +」，展开为白底抽屉。

### 主按钮（胶囊）

**Role:** 唯一主 CTA
`bg-cobalt`(#0c6ccc) `text-paper`，`border-radius: 999px`，高 48px，左右 24px，16px/500。hover `#0a58a8`；active `scale(.97)`；focus 2px 钴蓝外框、3px 间距；手机端满宽。

### 黑场描边按钮

**Role:** 黑场次按钮（复制客服链接）
透明底，1px `#aaa498` 边，`#f3f1ec` 字，胶囊。hover 边变 `#f3f1ec`、底变 `#1c1a17`；focus 外框用黑场字色。

### 禁用下载按钮

**Role:** 暂未开放的下载
`#e4e1da` 底、`#6d685f` 字，胶囊，高 44px，`cursor:not-allowed`，下方配 12px 等宽「下载暂未开放」。

### 章节黑条

**Role:** 章节末尾的主链接（照 ② 的「Read the Tools Chapter」）
右栏满宽，高 84px，`#0f0e0c` 底、`#f3f1ec` 18px 字，右端 26px 细箭头，零圆角。hover 整条变钴蓝、箭头右移 4px。

### 行链接

**Role:** 次级链接（阅读院长来信）
宽 454px，顶部 1px 暖墨线，高 52px，左文字右箭头，hover 文字变钴蓝。

### 目录瓦片

**Role:** 首页即目录
四列 `1fr 1.8fr 1.4fr 1fr`，格缝 1px 蓝发丝（`gap:1px` + 蓝底），每格白底、最低 230px。左上等宽「§01」、右上「↘」；左下 30px/700 标题；章节格右上角贴一张原色小图（38%，上限 200px，1px 暖发丝框）；§04–§06 格用浅暖灰大字形（01—05 / 09.15 / “）。唯一一格钴蓝（§07 联系），右下 90px 白色「↗」。hover 白格变暖灰。

### 切片图框（章节插画框）

**Role:** 全站唯一的图像处理
4:3 盒子，底色 `#e9e6df`；插画 `grayscale(1) contrast(1.08) brightness(1.04)` + `mix-blend-mode: multiply`，变成暖灰单色叠印。上面开 1–2 个原色「窗」：同一张图、同一位置按 `--x/--y/--w/--h` 百分比对位裁出，1px 白框，右下角贴等宽白标签（EXPERIENCE）。首屏拼贴是同一手法的横向版本：四块灰阶面板 + 三块原色浮窗 + 小白标签。

### 报告小节头

**Role:** 三个叙事章节
顶部 1px 暖墨线，下 18px。左栏：「01」与章名同为 500 字重、78px、行高 1.02。右栏：衬线 56px 大引语（强调词钴蓝），下 28px 接 18px 说明（≤454px）。之后按章留不同高度的空底，再进入「图框 ｜ 图注 + 黑条」下半。

### 图注行

**Role:** 图像说明
右栏 454px，顶部 1px 暖墨线；上等宽英文（MAKE IT REAL），下 22–30px 衬线中文（亲手试用，持续改进。）。

### 共学台阶（流程步骤）

**Role:** 共学五步
五等分，上下 1px 暖墨线，格间 1px 暖发丝。数字 108px/500/-0.04em，顶部按 `(5 − i) × 40px` 下沉，01 最低、05 最高并染钴蓝——台阶本身就是「向前一点」。数字下方 22px/700 步骤名 + 16px 次要墨说明，底部对齐。手机端改为一行一步，数字 56px 在左。

### 产品下载行

**Role:** 知君 / 万象
右栏宽，第一行顶部 1px 暖墨线，行间 1px 暖发丝。左：32px/700 产品名 + 18px 衬线说明「— 让积累参与思考 ↗」（整段是链接）；右：禁用下载按钮；下行右对齐等宽「下载暂未开放」。

### 期刊卡（一大两小）

**Role:** 观点与动态
左栏一张大卡：4:3 切片图框，底边 8px 钴蓝条；下接等宽日期、32px/700 标题、16px 次要墨摘要。右栏两张横卡：图 45% ｜ 文字 55%，卡间 1px 暖发丝。整卡可点（标题链接 `::after` 覆盖），hover 标题变钴蓝。

### 引文块（整屏大引语）

**Role:** 院长寄语
左右对开，分界就是右栏起笔线，最低 `min(100svh, 820px)`。左页黑场：52px 钴蓝引号、等宽「FROM THE FOUNDER」、底部 22px 署名 + 14px 次要字头衔。右页深暖灰：衬线 60px 引文（`text-wrap: balance`），底部 18px 正文 + 行链接。

### 联系横幅

**Role:** 黑场里唯一的居中对称
上下 170px，等宽书眉 → 64px/500 两行标题 → 18px 次要字 → 主按钮 + 黑场描边按钮。

### 输入框（预留）

**Role:** 以后接表单时用
高 62px，1px 暖墨边，零圆角，右侧直接拼钴蓝直角提交块（照 ② 的订阅表单）。focus 2px 钴蓝内框；错误态底边 3px 钴蓝线。

### 等宽小标签（徽标）

**Role:** 图框标签、舞台标注
白底、暖墨字，10px Geist Mono 大写，内距 5×7px，零圆角，贴在图框右下角；放大舞台上的标注改为 12px 钴蓝字、无底。

### 滑动放大舞台（签名）

**Role:** 首屏到正文的过渡
外层高度 = 视口（上限 1000px）− 顶栏 + 640px；内层 sticky、`container-type: size`。起点：半人马 740×555 盒子 `translate(拼贴格中心) scale(.5)`，站在首屏拼贴第三格（暖灰 + 蓝网格）里。过程：拼贴左右组各外移 24cqw 并淡出，导语上移 48px 淡出；暖灰 + W/4 方格的舞台底淡入，方格与终态盒子对齐（4×3 格）。终态：半人马居中，1px 钴蓝构图线（盒子四边 + 内切圆）展开，标注「人的意愿」「能力的延伸」「HUMAN × AI」浮现，然后释放。

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | paper | `#ffffff` | 首屏文字区、目录、章节 02、共学五步 |
| 1 | stone | `#f3f1ec` | 章节 01 / 03、观点与动态、放大舞台 |
| 2 | stone-deep | `#e9e6df` | 图框衬底、首屏拼贴底、院长右页 |
| 3 | night | `#0f0e0c` | 书脊字标、院长左页、联系、页脚 |
| accent | cobalt | `#0c6ccc` | 顶栏 CTA 条、§07 目录格（仅这两块面） |

## Do's and Don'ts

### Do

- 所有正文、引语、黑条、产品行都从右栏起笔线（41.47%）起，左栏宁可空着。
- 分区一律「1px 暖墨顶线 + 12px 等宽书眉」开头，书眉下 28–56px 再放标题。
- 钴蓝只给：顶栏 CTA 条、主按钮、强调词、§07 格、台阶 05、期刊卡底条、构图线。全页 ≤6%。
- 每张插画都先灰阶叠印，再开 1–2 个原色窗，窗口右下贴等宽白标签。
- 纸白与暖灰交替；黑场只出现在书脊字标、院长左页、联系与页脚。
- 章节内留白每章不同（170 / 96 / 210px），别让三章长得一样。
- 中文展示字距不低于 -0.02em，行高不低于 1.02。
- 任何视口高度都加 px 上限：`min(100svh, 1000px)`。

### Don't

- 不要让 logo 橙进入界面——按钮、强调、图标、线都不许用 `#f07800`。
- 不要给任何面加圆角或阴影；圆只属于胶囊按钮。
- 不要用中性灰（#888、#eee 之类）——灰必须带暖色相。
- 不要把插画原色整张贴出来；整张原色只允许在目录格小图和终态半人马。
- 不要编数字、学员数、客户、评价；「大数字」只有 01–05、§01–§07、2026、2026.09.15。
- 不要用紫蓝渐变、渐变文字、玻璃拟态、外发光、emoji、Inter / Roboto / Arial。
- 不要做三张等宽卡一排；期刊区固定「一大两小」。
- 不要把放大动画写成从 scale(1) 往上放——终态超过 740px 会糊。

## Imagery

图像只有一种处理，照 ② 第三章那张「黑白花 + 彩色矩形切片 + 等宽小标签」：插画先转灰阶并正片叠底到深暖灰上，暖纸感被压成统一的单色底；再按百分比坐标开 1–2 个原色窗，让人一眼看到「经验 / 同伴 / 做出来」各自的关键物件（罗盘、桌上的图纸、小房子模型）。首屏拼贴是这套手法的横向长卷：经验、共学、创造三张图做灰阶面板，三块原色浮窗压在面板交界处，中间一格留给半人马抠图——它是全站唯一不做灰阶的整图，因为它是「人 × AI」本身。目录格的小图保留原色，作为入口的颜色提示。不生成任何新图，图形只用内联 SVG（箭头、引号、标注线）。

## Layout

满宽，16px 页边距，两栏 `41.47fr / 58.53fr`、栏缝 16px；右栏起笔线在 1440 下约 601px，背景上用 1px 蓝发丝画出「左边距线 / 起笔线 / 右边距线」三条竖线，贯穿所有纸白与暖灰分区。节奏：书脊顶栏 → 首屏（拼贴 + 不对称标题，钉住 640px 做滑动放大）→ 目录格 → 三个报告小节（暖灰 / 白 / 暖灰）→ 共学台阶（白）→ 观点（暖灰，一大两小）→ 院长对开（黑 ｜ 深暖灰）→ 联系居中（黑）→ 页脚（黑，链接列 + 满宽字标 + 2026）。900px 以下全部单栏；560px 以下目录格两列、按钮满宽。

## Agent Prompt Guide

Quick Color Reference:

```
paper: #ffffff
stone: #f3f1ec
stone-deep: #e9e6df
ink: #1b1916
ink-muted: #57534b
night: #0f0e0c
cobalt (only accent, ≤6%): #0c6ccc
grid hairline: #d3e0f1
logo orange (never in UI): #f07800
```

Example Component Prompts:

1. Create a report chapter head: top `1px solid #1b1916`, 2-col grid `41.47fr 58.53fr` gap 16px. Left: "02" (Instrument Sans 500) and "与同行者一起" (Noto Sans SC 500) stacked, both 78px, line-height 1.02, letter-spacing -0.02em. Right: serif H2 56px/1.3 (Noto Serif SC 700) with the emphasis words in `#0c6ccc`, then an 18px paragraph max-width 454px. No radius, no shadow.
2. Create a sliced image plate: 4:3 box, background `#e9e6df`, image `filter: grayscale(1) contrast(1.08) brightness(1.04); mix-blend-mode: multiply`. Add one window span positioned by `--x --y --w --h` percentages showing the same image in full color, aligned, with `outline: 1px solid #fff`, and a white Geist Mono 10px uppercase tag at its bottom-right.
3. Create a chapter CTA slab: full right-column width, height 84px, background `#0f0e0c`, text `#f3f1ec` 18px/500 on the left, 26px thin arrow on the right, radius 0; hover turns the whole slab `#0c6ccc` and nudges the arrow 4px right in 0.2s `cubic-bezier(.44,0,.56,1)`.

## Similar Brands

- **② AI in Design Report 2026**（stateofaidesign.com，Awwwards SOTD 2026-08-26）— 本版骨架。逐条借用：
  - 顶栏书脊：黑方块字标 + 满高色条 CTA + 纯文字导航（study/ai-in-design-report/s01.png）→ 色条换成钴蓝。
  - 不对称首屏：上半切片拼贴、下半左窄导语 + 右栏超大紧排标题（s01.png）→ H1 132px / -0.02em / 1.06。
  - 右栏起笔线贯穿全页、右栏正文 454px（s04.png）→ `--split` / `--measure`。
  - 分区头「1px 黑线 + 等宽大写标签」（s02.png「OUR PARTNERS」「AN INFLECTION POINT」）→ `.sec-head`。
  - 图像只有一种处理：灰阶花 + 原色矩形切片 + 小白标签（s08.png、s09.png 第三章图；s01.png 拼贴）→ 切片图框。
  - 章节卡：左「编号 + 章名」同字号、右标题 + 摘要、下半「图 ｜ 目录 + 黑色长条按钮」（s06.png、s07.png）→ 报告小节 + 章节黑条。
  - 引语对开：左黑右浅、大引语从右栏起（s05.png）→ 院长寄语。
  - 黑底居中订阅（s12.png）→ 联系横幅；四格数字表（s13.png 上沿）→ 共学台阶的格线；满宽字标 + 巨型「2026」页脚（s13.png）→ 页脚。
  - 零圆角零阴影、白与暖灰 `#f7f6f4` 交替（STYLE.md）→ 暖灰阶。
- **③ Dropbox Brand**（brand.dropbox.com，Awwwards SOTM 2025-02、CSSDA 2025 年度）—
  - 满屏发丝网格就是装饰，内容只占几格（study/dropbox-brand/s01.png、s07.png）→ 蓝发丝三竖线 + 首屏拼贴第三格网格 + 放大舞台方格。
  - 一个强色 + 近黑（s01.png 只有蓝）→ 钴蓝唯一强色，橙关进 logo。
  - 首页即目录：同构瓦片做各板块入口（s03.png 八宫格）→ 目录瓦片，四列不等宽 `1fr 1.8fr 1.4fr 1fr`，一格强色。
  - 滚动驱动的 sticky 容器（s04.png → s05.png → s03.png 的收拢过程）→ 放大舞台的钉住段。
  - 留白里的度量标注「120%」「75% complete」（s07.png、s09.png）→ 终态「人的意愿 / 能力的延伸」钴蓝标注线。
  - 一大两小的演示卡组（s10.png）→ 期刊卡。
- **④ Shopify Editions Winter '26**（Awwwards SOTM 2026-02、Webby 2026 最佳视觉设计大众之选）—
  - 三声部：巨型无衬线喊章名、衬线讲叙述、小字做标签（study/shopify-editions-winter26/s04.png、s10.png）→ Instrument Sans / Noto Serif SC / Geist Mono。
  - 带同一色相的灰阶（STYLE.md 橄榄灰 #DCDCD0 / #909083 / #5C5C4E）→ 暖色相灰阶。
  - 零圆角面 + 白色胶囊按钮（s01.png「Start for free」）→ 胶囊主按钮。
  - 黑场段落与构图线（fold.png 黄金分割线 + 居中锁定框）→ 放大终态的构图线与内切圆；黑场给院长左页、联系、页脚。
  - 章节标题上下留白每章不同（PATTERNS.md：11vh–35vh）→ 三章 170 / 96 / 210px。
  - 两栏条目清单、无线（s12.png）→ 产品下载行的「名称 ｜ 说明 + 状态」结构（本版加了发丝分隔）。

覆盖 BRIEF-v3 清单：1、2、3、4、5、6、8、9、10、11、12（共 11 条）；第 7 条「黑场开幕」按站主本轮方向改为「白底拼贴开幕 + 黑场收尾」，开场不用 `#000`。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 纸面（暖灰阶，全部带同一暖色相底调） */
  --color-paper: #ffffff;
  --color-stone: #f3f1ec;
  --color-stone-deep: #e9e6df;
  --color-rule: #dcd8cf;
  --color-ink: #1b1916;
  --color-ink-muted: #57534b;
  --color-disabled-bg: #e4e1da;
  --color-disabled-fg: #6d685f;

  /* Colors — 黑场 */
  --color-night: #0f0e0c;
  --color-night-raised: #1c1a17;
  --color-night-rule: #3a3730;
  --color-on-night: #f3f1ec;
  --color-on-night-muted: #aaa498;

  /* Colors — 唯一界面强色：钴蓝（取自 logo 马身主峰） */
  --color-cobalt: #0c6ccc;
  --color-cobalt-deep: #0a58a8;
  --color-cobalt-on-night: #5c9fe6;
  --color-grid: #d3e0f1;
  --color-grid-night: #26303d;

  /* Colors — 只留在 logo 与插画里，界面不用 */
  --color-logo-orange: #f07800;

  /* Typography — Font Families（拉丁字体在前，中文由后续字体接管） */
  --font-display: 'Instrument Sans', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-sans: 'Instrument Sans', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-serif: 'Instrument Serif', 'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  /* Typography — Scale */
  --text-wordmark: clamp(40px, 15.8vw, 250px);
  --text-display-xl: clamp(50px, 9.2vw, 132px);
  --text-display-l: clamp(40px, 5.4vw, 78px);
  --text-display-m: clamp(30px, 3.5vw, 50px);
  --text-quote: clamp(30px, 3.9vw, 56px);
  --text-heading: clamp(24px, 2.3vw, 32px);
  --text-title: 22px;
  --text-body-lg: 18px;
  --text-body: 16px;
  --text-body-sm: 14px;
  --text-label: 12px;

  /* Line Height & Tracking */
  --leading-display: 1.06;
  --leading-heading: 1.22;
  --leading-quote: 1.3;
  --leading-body: 1.7;
  --tracking-display: -0.02em;
  --tracking-heading: -0.01em;
  --tracking-body: 0em;
  --tracking-label: 0.06em;

  /* Spacing（4px 基数；章节留白每章不同） */
  --spacing: 0.25rem;
  --gutter: 16px;
  --split: 0.4147;
  --measure: 454px;
  --header-h: 56px;
  --space-section-a: clamp(72px, 10vw, 150px);
  --space-section-b: clamp(96px, 16vw, 250px);
  --space-section-c: clamp(48px, 6vw, 90px);

  /* Shapes */
  --radius-none: 0px;
  --radius-pill: 999px;
  --hairline: 1px;

  /* Shadows：不用 */
  --shadow-none: none;

  /* Motion */
  --ease-report: cubic-bezier(0.44, 0, 0.37, 1);
  --ease-link: cubic-bezier(0.44, 0, 0.56, 1);
  --duration-fast: 0.2s;
  --zoom-distance: 640px;
  --zoom-max-width: 740px;
}
```

### Tailwind v4

```css
@theme {
  --color-paper: #ffffff;
  --color-stone: #f3f1ec;
  --color-stone-deep: #e9e6df;
  --color-rule: #dcd8cf;
  --color-ink: #1b1916;
  --color-ink-muted: #57534b;
  --color-disabled-bg: #e4e1da;
  --color-disabled-fg: #6d685f;
  --color-night: #0f0e0c;
  --color-night-raised: #1c1a17;
  --color-night-rule: #3a3730;
  --color-on-night: #f3f1ec;
  --color-on-night-muted: #aaa498;
  --color-cobalt: #0c6ccc;
  --color-cobalt-deep: #0a58a8;
  --color-cobalt-on-night: #5c9fe6;
  --color-grid: #d3e0f1;
  --color-grid-night: #26303d;
  --color-logo-orange: #f07800;
  --font-display: 'Instrument Sans', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-sans: 'Instrument Sans', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-serif: 'Instrument Serif', 'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-mono: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --text-wordmark: clamp(40px, 15.8vw, 250px);
  --text-display-xl: clamp(50px, 9.2vw, 132px);
  --text-display-l: clamp(40px, 5.4vw, 78px);
  --text-display-m: clamp(30px, 3.5vw, 50px);
  --text-quote: clamp(30px, 3.9vw, 56px);
  --text-heading: clamp(24px, 2.3vw, 32px);
  --text-title: 22px;
  --text-body-lg: 18px;
  --text-body: 16px;
  --text-body-sm: 14px;
  --text-label: 12px;
  --leading-display: 1.06;
  --leading-heading: 1.22;
  --leading-quote: 1.3;
  --leading-body: 1.7;
  --tracking-display: -0.02em;
  --tracking-heading: -0.01em;
  --tracking-body: 0em;
  --tracking-label: 0.06em;
  --space-section-a: clamp(72px, 10vw, 150px);
  --space-section-b: clamp(96px, 16vw, 250px);
  --space-section-c: clamp(48px, 6vw, 90px);
  --radius-none: 0px;
  --radius-pill: 999px;
  --shadow-none: none;
  --ease-report: cubic-bezier(0.44, 0, 0.37, 1);
  --ease-link: cubic-bezier(0.44, 0, 0.56, 1);
}
```

布局与动效量（`--spacing` `--gutter` `--split` `--measure` `--header-h` `--hairline` `--duration-fast` `--zoom-*`）不进 `@theme`，保留在 `:root`。

## 新增的结构性文字

以下文字不在首页文案稿里，是为了报告体的书眉、目录和交互加上的，全部列出：

- 「目录 / INDEX」——目录区书眉、页脚链接列标题
- 「CENTAUR AI ACADEMY · 2026」——目录区右侧书眉
- 「§01」「§02」「§03」「§04」「§05」「§06」「§07」——目录格编号与分区书眉
- 「01—05」——共学五步书眉与目录格大字形
- 「09.15」——观点目录格大字形（取自真实日期 2026.09.15）
- 「“」——院长目录格大字形
- 「↘」——目录格右上角指向符
- 「2026」——页脚巨型年份
- 「菜单 +」——移动端顶栏按钮
- 「跳到正文」——键盘跳转链接（聚焦时才出现）
- 「已复制」——复制客服链接后的状态提示（读屏播报）
- 放大终态把图注「HUMAN × AI ｜ 人的意愿 · 能力的延伸」拆成三条标注，文字未改，分隔符对读屏保留、视觉隐藏
- 首屏拼贴与切片图框的小标签「HUMAN × AI」「EXPERIENCE」「LEARN TOGETHER」「MAKE IT REAL」取自图注英文部分，未新增
- 目录格标题复用文案稿里的章节名与眉标（从你的积累出发 / 与同行者一起 / 让想法落地 / 每一次共学，都向前一点 / CENTAUR JOURNAL / 观点与动态 / FROM THE FOUNDER / THE NEXT CHAPTER · 从这里开始）
- kit.html 里的说明文字（色板角色、步骤说明、「scale 0.5」等）只属于样张，不进首页
