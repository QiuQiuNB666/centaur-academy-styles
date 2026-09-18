# 半人马AI学院 · 象牙与深海蓝 — Style Reference

> 深海蓝开幕、象牙白正文，金线只做骨架，粗宋立住分量

**Theme:** light（开幕、第三章、联系区为深海蓝整段；正文画布为象牙白）

这一版从第三轮「刊本」往中间走：保留刊本的骨架——左侧粘性目录、章节编号与节奏、细线网格、半人马随滚动放大——把它的年轻腔换成一家商学院或咨询机构的正装。开幕不再是纯黑，而是深海蓝 #0D2240，中心带一层极轻的抬升（#122A4D 径向），构图线是 12%–26% 透明度的金色细线；半人马立在一圈 1px 亮金细环里，环内一圈 6° 一格的刻度，随滚动从半尺寸放到满尺寸，金环由暗转亮，一段亮金沿环掠过一圈后隐去——这是本范式的**签名记忆点：金环登场**。开幕的收尾不是拉丁大字，而是一句居中的粗宋主张「人决定方向，AI 拓展人的能力。」。正文画布是偏暖但不发黄的象牙白 #FAF7F1，字是深蓝近黑 #0F1C30，对比度 16:1；所有标题一律 Noto Serif SC（章节名 900、H2 700），正文 Noto Sans SC 18–20px，行高 1.8，老花眼在微信里不用放大也能读。颜色只有四个角色：深海蓝、象牙白、金、logo 橙——金只做 1px 细线、章节编号和 H1 的一个关键词「你的能力」，全页金色面积 ≤2%；logo 橙只给「联系学院顾问」这类主按钮，≤3%。不用渐变字、不用投影、不用书法、不用云纹回纹，也不用满屏等宽小标签；层次靠字号、字重和深浅两段底色的切换。

## Tokens — Colors

| Name | Value | Token | Role |
| --- | --- | --- | --- |
| 深海蓝 | `#0d2240` | `--color-navy` | 开幕、第三章整章、联系区与页脚；次级实心按钮 |
| 深海蓝 · 顶栏 | `#0a1a33` | `--color-navy-deep` | 顶栏与移动菜单，比开幕深一档，压住页首 |
| 深海蓝 · 抬升 | `#122a4d` | `--color-navy-raise` | 开幕径向光晕中心、深色衬纸、次级按钮 hover |
| 象牙白 | `#faf7f1` | `--color-ivory` | 正文画布，偏暖的白，不是米黄 |
| 象牙衬纸 | `#efe9de` | `--color-ivory-deep` | 插画衬纸、步骤瓦片、院长寄语右栏、禁用底 |
| 深蓝墨 | `#0f1c30` | `--color-ink` | 正文与标题，象牙上 16:1；分区头墨线 |
| 次要文字 | `#3a4659` | `--color-ink-muted` | 说明、日期、次要文字，象牙上 8.9:1、衬纸上 7.9:1 |
| 象牙发丝 | `#dcd5c8` | `--color-hair` | 图注底线、描边瓦片、目录竖线 |
| 网格发丝 | `rgba(15,28,48,0.07)` | `--color-grid` | 正文三根贯穿竖线与区块顶的全宽横线 |
| 蓝底主字 | `#f4f1ea` | `--color-on-navy` | 深海蓝上的标题与正文，14:1 |
| 蓝底次要字 | `#c3cbd8` | `--color-on-navy-muted` | 深海蓝上的说明文字，9.7:1 |
| 蓝底发丝 | `rgba(195,203,216,0.2)` | `--color-hair-navy` | 深色段分隔线、顶栏底线 |
| 金线 | `#b08d4f` | `--color-gold` | 象牙上的细线：眉标短线、强调下划线、画框内线、目录标题线 |
| 金 · 编号 | `#8c6a32` | `--color-gold-deep` | 象牙上的章节编号与步骤数字（≥44px，4.7:1） |
| 亮金 | `#d4b273` | `--color-gold-bright` | 深海蓝上的金：H1 关键词（7.9:1）、金环、段落接缝线 |
| 金 · 构图线 | `rgba(212,178,115,0.26)` | `--color-gold-line` | 开幕中轴与同心圆、金环刻度 |
| 金 · 极淡网格 | `rgba(212,178,115,0.12)` | `--color-gold-faint` | 开幕与联系区的竖横网格 |
| 金 · 掠光 | `#f3e2bc` | `--color-gold-glint` | 金环上掠过的那一段亮光，只在动画里出现 |
| logo 橙 | `#f07800` | `--color-accent` | 只给主按钮（联系学院顾问），全页 ≤3% |
| logo 橙 · 按下 | `#d86a00` | `--color-accent-press` | 主按钮 hover / active、输入框错误边 |
| 橙上字 | `#05080d` | `--color-accent-foreground` | 主按钮文字（近黑深蓝），7.0:1 |
| logo 钴蓝 | `#0c6ccc` | `--color-logo-blue` | 只存在于 logo 与插画里，界面不用 |
| 禁用底 / 字 | `#efe9de` / `#3a4659` | `--color-disabled-bg` / `--color-disabled-fg` | 「下载暂未开放」的禁用按钮 |
| 返回钮垫底 | `rgba(250,247,241,0.9)` | `--color-back-pad` | 左下「全部方案」下面垫的象牙底，深浅两段都找得到 |
| 焦点环 | `#0f1c30` / `#d4b273` | `--color-ring` / `--color-ring-dark` | 象牙上用墨色 2px 焦点环，深海蓝上用亮金 |

### 柔和语义色（本范式不设）

学院官网没有状态型数据（成功 / 警告 / 过期），不设 pastel 成对色。唯一的状态是「下载暂未开放」，用禁用底 + 次要字表达；错误态只在输入框里出现，用 2px logo 橙按下色边框。

### 图表色（本范式不设）

全站没有任何可引用的数据，不做图表，也不做大数字统计。

## Tokens — Typography

### Noto Serif SC — 标题：H1、章节名、H2、步骤名、引文、主张、产品名 · `--font-serif-zh`

- **Substitute:** Songti SC, STSong, SimSun, serif（正式上线可自托管思源宋体 Heavy 子集）
- **Weights:** 500（叙述句、图注）、700（H2、观点标题、引文）、900（H1、章节名、步骤名、主张、产品名、人名）
- **Sizes:** 18px, 22px, 23px, 26px, 32px, 44px, 52px, 56px, 92px, 104px
- **Line height:** 章节名 1.12 / H1 1.14–1.18 / H2 1.28 / 引文 1.5
- **Letter spacing:** 标题 +0.01em，主张与人名 +0.06em（粗宋撑开一点更「正」）
- **OpenType features:** H2 开 `halt`，中文标点半宽，避免「，」空出一整格
- **Role:** 让老板一眼觉得「正、稳、有分量」的那一层；全站所有标题都用它，不混黑体大字

### Noto Sans SC — 正文、按钮、导航、说明 · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei, system-ui
- **Weights:** 400（正文）、500（导航、徽标）、700（按钮、文字链、目录）
- **Sizes:** 16px, 17px, 18px, 19px, 20px, 22px
- **Line height:** 1.8（正文）/ 1.2（按钮）
- **Role:** 讲话的一层。手机正文 ≥18px、次要 ≥16px，按钮 18–19px 粗体

### Cinzel — 少量英文眉标 · `--font-latin`

- **Substitute:** Noto Serif SC, Songti SC, Georgia, serif（中文部分自动落到宋体）
- **Weights:** 500, 600
- **Sizes:** 13px（顶栏、页脚字标）, 14px（眉标、图注英文）, 15px（开幕眉标）
- **Letter spacing:** +0.14em，全大写
- **Role:** 碑刻感的罗马字，只出现在 `CENTAUR AI ACADEMY`、`HUMAN × AI`、`EXPERIENCE` 这类文案稿原有的英文上；全页不超过 8 处，不承载关键信息

### Noto Serif（Noto Serif SC 的拉丁数字）— 编号 · `--font-num`

- **Substitute:** Georgia, Songti SC, serif
- **Weights:** 700, 900
- **Sizes:** 16px（目录）, 44px（章节编号）, 52–68px（步骤编号）, 150–236px（第一步大数字）
- **OpenType features:** lining-nums tabular-nums
- **Role:** 章节编号、步骤编号、目录页码、日期。只有「三章节」「共学五步」「目录顺序」是真实顺序，编号只出现在这三处

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| --- | --- | --- | --- | --- |
| shout（章节名） | clamp(46px, 5.6vw + 10px, 104px) | 1.12 | 0.01em | `--text-shout` |
| display（H1 / 步骤区标题 / 联系标题） | clamp(48px, 4.6vw + 14px, 92px) | 1.14 | 0.01em | `--text-display` |
| heading（H2） | clamp(34px, 2vw + 18px, 56px) | 1.28 | 0.01em | `--text-heading` |
| motto（终幕主张） | clamp(32px, 2.4vw + 12px, 52px) | 1.2 | 0.06em | `--text-motto` |
| narrative（叙述句） | clamp(24px, 0.8vw + 18px, 32px) | 1.5 | 0 | `--text-narrative` |
| lede（导语） | clamp(20px, 0.4vw + 17px, 23px) | 1.8 | 0.01em | `--text-lede` |
| body（正文） | clamp(18px, 0.3vw + 16px, 20px) | 1.8 | 0.01em | `--text-body` |
| button | 19px（次级 18px） | 1.2 | 0.04em | `--text-button` |
| caption（次要） | 16px | 1.8 | 0.01em | `--text-caption` |
| label（英文眉标） | 14px | 1.5 | 0.14em | `--text-label` |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 4px`）

**Density:** 宽松——章节之间 104–120px，老板在手机上一屏只看一件事

### Spacing Scale

| Name | Value | Token |
| --- | --- | --- |
| 页边 | clamp(16px, 2.8vw, 40px) | `--gutter` |
| 栏距 | 20px | `--col-gap` |
| 目录栏宽 | 248px | `--toc-width` |
| 内容最大宽 | 1160px | `--content-max` |
| 顶栏高 | 76px（≤1023px 为 64px） | `--header-h` |
| 1 / 2 / 3 / 4 | 4 / 8 / 12 / 16px | `--spacing` × n |
| 6 / 7 / 10 / 12 | 24 / 28 / 40 / 48px | `--spacing` × n |
| 18 / 26 / 30 | 72 / 104 / 120px | `--spacing` × n（章节上下留白） |

### Border Radius

| Name | Value | Token |
| --- | --- | --- |
| none | 0px | `--radius-none` |
| sm | 4px | `--radius-sm` |
| pill | 999px | `--radius-pill`（只给左下返回钮垫底） |

| Element | Value |
| --- | --- |
| 插画衬纸、步骤瓦片、观点封面、院长对开 | 0（直角） |
| 按钮、输入框、徽标、菜单按钮 | 4px（sm） |
| 金环 | 50%（正圆） |

### Shadows

| Name | Value | Token |
| --- | --- | --- |
| none | `none` | `--shadow-none` |

不用任何投影和外发光。深度只来自两段底色（深海蓝 ↔ 象牙白）和衬纸（#EFE9DE）一层。

### Motion

| Name | Value | Token |
| --- | --- | --- |
| ease-settle | `cubic-bezier(0.41, 0.19, 0.13, 0.95)` | `--ease-settle`（登场放大） |
| ease-calm | `cubic-bezier(0.33, 0, 0.2, 1)` | `--ease-calm`（按钮、hover） |
| dur-fast | 0.2s | `--dur-fast` |
| dur-base | 0.45s | `--dur-base` |

- **金环登场（桌面 ≥1024px）：** 开幕钉住一屏、额外滚动 min(一屏, 90svh)。滚动 0 → 0.7 屏：半人马 `scale(.46 → 1)`、金环不透明度 `.22 → 1`、构图线 `scale(.94 → 1)` + 不透明度 `.3 → 1`；0.35 → 0.8 屏：一段亮金沿环 `rotate(-110° → 250°)` 掠过一圈，首尾淡出；0.4 → 0.68 屏：开幕文字退场；第二屏终幕主张淡入。
- **金环登场（手机 / 平板）：** 外层 `.stage-zoom` 做 view 时间线，画面钉住一小段（额外 ≤60px），`scale(.76 → 1)`，金环与掠光同上。终态 CSS 宽度：手机（≥2.5dppx）≤480px，平板 / 桌面 ≤720px。
- CSS 全部写在 `@supports (animation-timeline: view())` 里，`animation-timeline` 写在 `animation` 简写之后；不支持的内核（安卓微信、iOS 26 以下）由页内 JS 兜底：IntersectionObserver 只在开幕附近监听，passive scroll + requestAnimationFrame，只写 transform / opacity；URL 带 `?nosd` 强制兜底。
- `prefers-reduced-motion: reduce`：全部静态。桌面开幕层半人马停在半尺寸（不压标题），终幕给满尺寸；手机直接是满尺寸终态。

### Layout

- **Section gap:** 104–120px（桌面）/ 72–80px（手机）
- **Card padding:** 28px（步骤瓦片）/ 32px（院长对开）
- **Element gap:** 16–28px
- **Max content width:** 1160px 正文 + 248px 左侧目录；开幕与联系区通栏

## Components

### 顶栏（Masthead）

**Role:** 站点识别 + 主导航 + 常驻咨询入口
深海蓝顶栏 `--color-navy-deep`，高 76px，底边 1px 蓝底发丝。左侧品牌格宽 248px（与正文目录栏对齐）：logo + 粗宋 900「半人马AI学院」19px + Cinzel 13px 字标，右侧 1px 竖线收住。导航黑体 500 17px，hover 底部出现 2px 亮金线。最右一枚橙色主按钮（52px 高）。≤1023px 收成 logo + 「菜单 +」描边按钮（48px 高），菜单展开为通栏深海蓝面板，条目 22px、60px 行高，末尾一枚通栏橙色主按钮。

### Primary Button（logo 橙）

**Role:** 唯一的转化动作「联系学院顾问 ↗」
`bg-accent`(#F07800) `text-accent-foreground`(#05080D)，`border-radius: var(--radius-sm)`(4px)，`min-height: 56px`，`padding: 0 28px`，`font: 700 19px/1.2`，字距 0.04em。hover 变 #D86A00、箭头右上移 2px；active `scale(.98)`。手机上通栏。按钮文字必须写全「联系学院顾问」。

### Navy Button（次级实心）

**Role:** 区块级次要动作（全部观点与动态）
`bg-navy`(#0D2240) `text-on-navy`，52px 高，18px 粗体，hover 变 #122A4D。

### Line Button（描边）

**Role:** 章节里的延伸链接（了解学院的主张、了解共学与共创）、复制客服链接
透明底 + 1px 墨色边，52px 高。hover 反成深海蓝实心 + 象牙字。深色段里边框换成蓝底次要字色，hover 反成象牙实心 + 深海蓝字。

### Text Link

**Role:** 与主按钮并列的轻动作
黑体 700 19px，2px 金线下划线、偏移 8px，48px 触控高度。

### Disabled Download Button

**Role:** 「下载知君 ↓」「下载万象 ↓」
象牙白段：衬纸底 + 次要字 + 象牙发丝边；深海蓝段（第三章）：透明底 + 蓝底发丝边 + 蓝底次要字。旁边黑体 16px「下载暂未开放」。

### 分区头（Section Rule）

**Role:** 每个区块的起点
1px 墨色横线 + 左侧粗宋 900 44px 金色编号（01/02/03），同一高度一根极淡网格横线向两侧贯穿全宽。没有编号的区块改放一个中文小标题（粗宋 700 18px）或文案稿原有的英文眉标（Cinzel 14px）。

### 章节名（Shout）

**Role:** 章节的主标题「从你的积累出发」
粗宋 900，clamp(46px, 5.6vw + 10px, 104px)，深蓝墨；分区头下方 30px。

### H2 与强调词

**Role:** 章节里的论点句
粗宋 700 `--text-heading`；强调词（起点 / 一起做 / “我来做” / 继续对话）不换色，底下压一道 3px 金线。

### 插画装裱（Plate）

**Role:** 三张暖色插画的统一处理
象牙衬纸 `--color-ivory-deep`，内边距 clamp(18px, 3.4vw, 52px)，插画外 1px 金线框（offset 为衬纸宽的 0.42）；下方图注行：Cinzel 灰蓝英文（EXPERIENCE，7:1 以上；金色只留给框线）+ 粗宋 500 18px 中文，底边一根象牙发丝。深海蓝段里衬纸换成 #122A4D、金线换亮金。

### 金环半人马（Hero Figure）

**Role:** 签名记忆点
抠图版半人马，身后一圈直径为图宽 84% 的 1px 亮金细环，环内 12px 处一圈 6° 一格、8px 长的刻度（金 · 构图线色）。一段 3px 宽的亮金掠光（conic-gradient 用 radial mask 裁成环）沿环转过一圈。图注「HUMAN × AI ｜ 人的意愿 · 能力的延伸」居中放在环下。

### 观点卡（Journal Card）

**Role:** 三篇观点
直角象牙衬纸封面（academy-centaur-hero 用 multiply 融进衬纸）；元信息行：金线框、深蓝字的徽标「观点」+ 衬线数字日期 16px；标题粗宋 700 23–32px；摘要黑体 18px。桌面三卡错落（0 / 64 / 128px 下沉），手机单列。

### 共学五步瓦片（Steps Tiles）

**Role:** 真实顺序的流程
12 栏不等宽：第一步占 5 栏 × 2 行，深海蓝底 + 150–236px 亮金大数字；其余四块衬纸 / 描边交替，右上角 52–68px 金色编号，描边瓦片左上一根 36px 金短线。步骤名粗宋 900 28–34px，说明黑体 19px。

### 产品下载行（Product Row）

**Role:** 知君 / 万象
在第三章深海蓝整章里：顶边一根亮金线，每行左侧粗宋 900 42–56px 产品名，右侧「— 让积累参与思考 ↗」粗宋 700 22px + 禁用下载按钮。

### 院长寄语对开（Founder Split）

**Role:** 引文
5:7 对开。左栏深海蓝：亮金大引号 + 亮金横线 + 粗宋 900「嘉木」+ 黑体 17px 头衔；右栏衬纸：粗宋 700 28–44px 引文 + 正文 + 文字链。

### 终幕主张（Finale Motto）

**Role:** 开幕的收尾
深海蓝上居中的粗宋 900「人决定方向，AI 拓展人的能力。」`--text-motto`，字距 0.06em，上方 56px 亮金短线。桌面在放大结束后淡入，与满尺寸金环半人马同屏。

### 联系区与页脚（Contact & Footer）

**Role:** 最后一次转化
深海蓝通栏，顶边一根 1px 亮金接缝线；极淡金色竖网格 + 自底部升起的两道同心弧。居中：Cinzel 眉标、粗宋 900 标题、导语、橙色主按钮 + 描边「复制客服链接」。页脚三栏：品牌 / 口号（粗宋 700 22px）/ 发起方链接，底行主张与字标。

### 返回钮垫底（Back Pad）

**Role:** 让左下「全部方案」在深浅两段都看得见
固定在左下，94×36px 象牙半透明胶囊，垫在返回钮下面，返回钮样式不改。

### Input Field

**Role:** 文本输入（样张备用）
56px 高、1px 墨色边、4px 圆角、18px 字；focus 2px 金色外环；错误态 2px 橙按下色边；禁用态衬纸底。

### Tag

**Role:** 内容类型
30px 高、4px 圆角、黑体 500 16px；金线款（观点）用金边 + 金 · 编号字，默认款墨色边，弱化款象牙发丝边。

## Surfaces

| Level | Name | Value | Purpose |
| --- | --- | --- | --- |
| 0 | ivory | `#faf7f1` | 正文画布 |
| 1 | ivory-deep | `#efe9de` | 插画衬纸、步骤瓦片、院长右栏 |
| 2 | navy | `#0d2240` | 开幕、第三章、步骤第一块、院长左栏、联系区 |
| 3 | navy-raise | `#122a4d` | 开幕光晕中心、深色衬纸 |
| 4 | navy-deep | `#0a1a33` | 顶栏、移动菜单 |

深浅两段之间一律用一根 1px 亮金线接缝，不用撕纸边、不用渐变过渡。

## Do's and Don'ts

### Do

- 开幕、第三章、联系区用深海蓝 #0D2240 整段，正文用象牙白 #FAF7F1——两段底色是全站唯一的「大动作」。
- 标题一律 Noto Serif SC：章节名与 H1 900，H2 700；正文一律 Noto Sans SC，手机 ≥18px、次要 ≥16px。
- 金色只做三件事：1px 细线、章节 / 步骤编号、H1 的「你的能力」。全页金色面积 ≤2%，平涂，不做渐变。
- logo 橙只给主按钮「联系学院顾问」，全页 ≤3%；次级动作用深海蓝实心或描边。
- 主按钮 56px 高、19px 粗体；所有可点目标 ≥48px。
- 强调词用 3px 金线下划线，不换颜色、不换字体。
- 三张插画同一种装裱：象牙衬纸 + 1px 金线内框 + 双语图注。
- 深浅两段接缝处放一根 1px 亮金线。
- 编号只给三章、五步和目录。
- 动效只写 transform / opacity；登场结束后屏内永远有字或半人马，不留空屏。

### Don't

- 不要用纯黑 #000 大底——开幕是深海蓝，不是黑场。
- 不要用撕纸边、橄榄奶油纸色、满屏等宽小标签——那是第三轮的年轻腔。
- 不要让拉丁大字当主视觉（整屏「HUMAN × AI」这类）。
- 不要用书法字体、云纹、回纹、山水、印章、对联、红色大底——那是第四轮的土。
- 不要做金属渐变字、描边字、投影、外发光、光束和粒子。
- 不要把所有东西居中对称：只有终幕主张和联系区居中，开幕标题在左、导语在右。
- 不要在正文或 16px 以下的字上用金色。
- 不要编任何数字、客户、评价、学员数。
- 不要写「全面 / 深入 / 赋能 / 打造 / 极致」。
- 不要在组件里写裸 hex——全部走 tokens.css。

## Imagery

主视觉只有一张：透明底抠图半人马，放在深海蓝场上的一圈细金环里，靠「由小到大 + 金环由暗转亮 + 一段掠光」完成出场，不叠光束、不撒粒子。三张暖色纸感插画（experience / co-learning / creating）统一装进象牙衬纸 + 金线内框，像证书和画册里的插页——插画的暖色和象牙底同温，金线把它们收成一个系列；在第三章深海蓝整章里衬纸换成抬升蓝，插画像被装进深色画框。观点卡封面用同一种直角衬纸，academy-centaur-hero（米色底烤在图里）用 multiply 融进衬纸。图标只用文字箭头 ↗ → ↓，不引图标库。

## Layout

桌面：顶栏 76px 通栏；开幕钉住一屏（高 min(100svh, 900px) − 76px，下限 640px）、额外滚动 ≤90svh；左上眉标 + H1，右上导语 + 按钮，正中金环半人马，左下主张，第二屏居中终幕主张。正文两栏：左 248px 粘性目录（粗宋「目录」+ 金线 + 点线引导 + 金色页码），右侧 1160px 内容区，三根极淡竖网格贯穿。章节图文左右轮换（一章文左图右、二章图左文右、三章深海蓝整章上文下图），步骤瓦片 12 栏不等宽，观点三卡错落，院长对开 5:7，联系区通栏居中。≤1199px 收起目录；≤1023px 开幕改为纵向堆叠（眉标 → H1 → 金环半人马 → 导语 → 按钮 → 主张），正文单列；≤600px 按钮通栏、步骤单列。

## Agent Prompt Guide

Quick Color Reference:

```
navy (开幕/第三章/联系区): #0d2240
navy-deep (顶栏): #0a1a33
ivory (正文画布): #faf7f1
ivory-deep (衬纸): #efe9de
ink (正文): #0f1c30
ink-muted (次要): #3a4659
gold (细线): #b08d4f   gold-deep (编号): #8c6a32   gold-bright (蓝底上的金): #d4b273
accent (只给主按钮, ≤3%): #f07800
```

Example Component Prompts:

1. Create the primary CTA: `bg #f07800` `text #0f1c30`, `border-radius 4px`, `min-height 56px`, `padding 0 28px`, `font 700 19px Noto Sans SC`, letter-spacing .04em, label「联系学院顾问 ↗」; hover `#d86a00`, arrow nudges 2px up-right; full width under 600px. Only one per view plus the header copy.
2. Create a chapter head: 1px `#0f1c30` top rule, then `01` in Noto Serif SC 900 44px `#8c6a32`, then the chapter name in Noto Serif SC 900 clamp(46px, 5.6vw + 10px, 104px) `#0f1c30`; the H2 below uses Noto Serif SC 700 with the keyword underlined by a 3px `#b08d4f` bar at 94%.
3. Create the hero figure: transparent centaur cutout on `#0d2240`; behind it a circle 84% of the image width, 1px `#d4b273` border, plus an inner ring of 8px ticks every 6° in `rgba(212,178,115,.26)`; on scroll scale from .46 to 1 while the ring fades from .22 to 1 and a 3px `#f3e2bc` arc travels once around it.

## Similar Brands

本版没有新开一轮外部调研，锚点取自站主已有的两份实拍笔记（第三轮 `styles-kit/study/`、第四轮 `styles-kit/tu-study/`），每条写明借了什么：

- **中欧国际工商学院 cn.ceibs.edu**（`tu-study/edu-brands/NOTES.md` §3，ceibs-m.png）— 借「暖米底 + 金色细线 + 深字」的商学院配色逻辑：金 #BD8E1F 只做卡头细线，区块底 #F5F2EE、卡片 #FCFAF8 → 本版的象牙白 #FAF7F1 / 衬纸 #EFE9DE 与金线 #B08D4F；不借它的中国红整屏。
- **博鳌亚洲论坛 boaoforum.org**（`tu-study/forums-gala/NOTES.md` §1）— 主色深藏蓝 #004077、主视觉里金黄的年份：老板熟悉的「藏青配金」正式感 → 深海蓝 #0D2240 开幕 + 亮金关键词；不借它的门户式列表。
- **长江商学院 ckgsb.edu.cn**（`tu-study/edu-brands/NOTES.md` §4）— EMBA 横幅的「深蓝星空 + 金色光尘」是老板看得懂的炫 → 收敛成一圈细金环 + 一段掠光；同时记住它的反例「标题太细太灰显旧」→ 本版标题一律粗宋 900。
- **Shopify Editions（Winter ’26）**（`styles-kit/study/shopify-editions-winter26/`，第三轮锚点）— 保留骨架：左侧粘性章节目录、章节编号与章首大字、开幕钉住后放大主视觉；去掉它的撕纸边、橄榄奶油纸与拉丁大字。
- **Dropbox Brand**（`styles-kit/study/dropbox-brand/`，第三轮锚点）— 保留「细线网格即装饰」与不等宽瓦片（共学五步）；网格线色相从灰换成极淡的金与墨。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 深海蓝 + 象牙白 + 金线 + logo 橙（只给主按钮） */
  --color-navy: #0d2240;
  --color-navy-deep: #0a1a33;
  --color-navy-raise: #122a4d;
  --color-ivory: #faf7f1;
  --color-ivory-deep: #efe9de;
  --color-ink: #0f1c30;
  --color-ink-muted: #3a4659;
  --color-hair: #dcd5c8;
  --color-grid: rgba(15, 28, 48, 0.07);
  --color-on-navy: #f4f1ea;
  --color-on-navy-muted: #c3cbd8;
  --color-hair-navy: rgba(195, 203, 216, 0.2);
  --color-gold: #b08d4f;
  --color-gold-deep: #8c6a32;
  --color-gold-bright: #d4b273;
  --color-gold-line: rgba(212, 178, 115, 0.26);
  --color-gold-faint: rgba(212, 178, 115, 0.12);
  --color-gold-glint: #f3e2bc;
  --color-accent: #f07800;
  --color-accent-press: #d86a00;
  --color-accent-foreground: #05080d;
  --color-logo-blue: #0c6ccc;
  --color-disabled-bg: #efe9de;
  --color-disabled-fg: #3a4659;
  --color-back-pad: rgba(250, 247, 241, 0.9);
  --color-ring: #0f1c30;
  --color-ring-dark: #d4b273;

  /* Typography — Font Families */
  --font-serif-zh:
    'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-sans:
    'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei',
    system-ui, sans-serif;
  --font-latin:
    'Cinzel', 'Noto Serif SC', 'Songti SC', Georgia, serif;
  --font-num:
    'Noto Serif SC', Georgia, 'Songti SC', serif;

  /* Typography — Scale（老花眼标准：正文 ≥18px，次要 ≥16px） */
  --text-label: 14px;
  --text-caption: 16px;
  --text-body: clamp(18px, 0.3vw + 16px, 20px);
  --text-lede: clamp(20px, 0.4vw + 17px, 23px);
  --text-narrative: clamp(24px, 0.8vw + 18px, 32px);
  --text-heading: clamp(34px, 2vw + 18px, 56px);
  --text-display: clamp(48px, 4.6vw + 14px, 92px);
  --text-shout: clamp(46px, 5.6vw + 10px, 104px);
  --text-motto: clamp(32px, 2.4vw + 12px, 52px);
  --text-button: 19px;

  /* Line Height & Tracking */
  --leading-shout: 1.12;
  --leading-display: 1.14;
  --leading-heading: 1.28;
  --leading-narrative: 1.5;
  --leading-body: 1.8;
  --tracking-shout: 0.01em;
  --tracking-heading: 0.01em;
  --tracking-body: 0.01em;
  --tracking-label: 0.14em;

  /* Spacing (4px base) */
  --spacing: 4px;
  --gutter: clamp(16px, 2.8vw, 40px);
  --col-gap: 20px;
  --toc-width: 248px;
  --content-max: 1160px;
  --header-h: 76px;
  --back-pad-w: 94px;

  /* Shapes — 面零圆角，控件 4px 小方角 */
  --radius-none: 0px;
  --radius-sm: 4px;
  --radius-pill: 999px;
  --hairline: 1px;

  /* Shadows — 不用 */
  --shadow-none: none;

  /* Motion */
  --ease-settle: cubic-bezier(0.41, 0.19, 0.13, 0.95);
  --ease-calm: cubic-bezier(0.33, 0, 0.2, 1);
  --dur-fast: 0.2s;
  --dur-base: 0.45s;
}
```

### Tailwind v4

```css
@theme {
  --color-navy: #0d2240;
  --color-navy-deep: #0a1a33;
  --color-navy-raise: #122a4d;
  --color-ivory: #faf7f1;
  --color-ivory-deep: #efe9de;
  --color-ink: #0f1c30;
  --color-ink-muted: #3a4659;
  --color-hair: #dcd5c8;
  --color-grid: rgba(15, 28, 48, 0.07);
  --color-on-navy: #f4f1ea;
  --color-on-navy-muted: #c3cbd8;
  --color-hair-navy: rgba(195, 203, 216, 0.2);
  --color-gold: #b08d4f;
  --color-gold-deep: #8c6a32;
  --color-gold-bright: #d4b273;
  --color-gold-line: rgba(212, 178, 115, 0.26);
  --color-gold-faint: rgba(212, 178, 115, 0.12);
  --color-gold-glint: #f3e2bc;
  --color-accent: #f07800;
  --color-accent-press: #d86a00;
  --color-accent-foreground: #05080d;
  --color-logo-blue: #0c6ccc;

  --font-serif-zh: 'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif;
  --font-latin: 'Cinzel', 'Noto Serif SC', Georgia, serif;
  --font-num: 'Noto Serif SC', Georgia, serif;

  --text-label: 14px;
  --text-caption: 16px;
  --text-body: clamp(18px, 0.3vw + 16px, 20px);
  --text-lede: clamp(20px, 0.4vw + 17px, 23px);
  --text-narrative: clamp(24px, 0.8vw + 18px, 32px);
  --text-heading: clamp(34px, 2vw + 18px, 56px);
  --text-display: clamp(48px, 4.6vw + 14px, 92px);
  --text-shout: clamp(46px, 5.6vw + 10px, 104px);
  --text-motto: clamp(32px, 2.4vw + 12px, 52px);

  --radius-none: 0px;
  --radius-sm: 4px;
  --radius-pill: 999px;

  --ease-settle: cubic-bezier(0.41, 0.19, 0.13, 0.95);
  --ease-calm: cubic-bezier(0.33, 0, 0.2, 1);
}
```

## 新增的结构性文字

以下文字不在 content.md 里，或是把文案稿原句换了位置 / 重复出现；均不含事实性说法：

- 终幕主张（桌面开幕第二屏，`aria-hidden`）：`人决定方向，AI 拓展人的能力。`——文案稿 Hero 底栏原句，放大居中重复一次
- 目录标题：`目录`
- 目录条目：`从你的积累出发 01`、`与同行者一起 02`、`让想法落地 03`、`共学五步 04`、`观点与动态 05`、`院长寄语 06`、`从这里开始 07`（条目文字取自文案稿的章节名与区块名，页码为新增）
- 分区头编号：`01`、`02`、`03`（文案稿章节编号，去掉斜杠后单独成为金色编号）
- 共学五步分区头：`共学五步`（文案稿区块名）
- 观点分区头：`CENTAUR JOURNAL` 与 `/ 观点与动态`（文案稿眉标拆成英文眉标 + 中文小标题）
- 院长寄语分区头：`FROM THE FOUNDER`（文案稿眉标，移到分区头）
- 插画图注英文：`EXPERIENCE`、`LEARN TOGETHER`、`MAKE IT REAL`（文案稿图注的英文部分，用 Cinzel 次要字色显示）
- 步骤大数字：`01`–`05`（文案稿编号，作为瓦片里的装饰字形，`aria-hidden`）
- 屏幕阅读器标题：`院长寄语`（视觉隐藏）
- 移动端菜单按钮：`菜单 +`；移动菜单内再放一枚 `联系学院顾问 ↗`（文案稿 CTA 原文）
- 跳转链接：`跳到正文`
- 复制按钮反馈：`已复制`
- 页脚底行字标：`CENTAUR AI ACADEMY`（文案稿页脚原文）
- 组件样张页（kit.html）的标题与说明：`半人马AI学院 · 组件样张`、`深海蓝开幕，象牙正文。`、`深海蓝与象牙白两个底色，金色只做细线与编号，logo 橙只给主按钮；标题一律粗宋，正文黑体按老花眼标准放大。`；分区名 `色板` `字体` `按钮` `图像` `卡片与输入` `流程` `引文与产品`；区块标题 `四个颜色角色`、`粗宋立骨，黑体讲话`、`按钮 · 全状态`、`插画装裱 · 金环登场`、`观点卡 · 徽标 · 输入框`、`共学五步瓦片`、`引文对开 · 产品下载行 · 主张`；色板名称与角色说明（`深海蓝` `开幕、第三章、联系区` 等）、字阶说明（`章节标题 · 粗宋 900 · 104px` 等）、按钮行名 `主按钮 · 橙` `次级 · 深海蓝` `描边` 与状态名 `default` `hover` `active` `focus` `disabled`；输入框示例 `你的问题` / `聊聊你正在做的事` / `默认态` / `错误态：2px 橙深边` / `暂未开放`；徽标示例 `联系`；以及各区块下的注释句（金环说明、按钮尺寸说明、终幕主张说明）
