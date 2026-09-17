# 半人马AI学院 · 纸上学刊 — Style Reference

> 两种纸，一种墨，一种专色，线比色块重要

**Theme:** light

「纸上学刊」把现站的暖纸 + 宋体方向留下，把让它显得像模板的东西全部换掉：陶土橙点缀换成从 logo 马身取的钴蓝专色（#1b4bb0），圆角卡片换成栏线，居中 hero 换成一张有刊头、目录和贴页图版的封面。画布是偏灰的书纸（#f2efe7，接近 Anthropic 的 ivory-medium #f0eee6，刻意比常见的 AI 米色少一分黄），图版另用一种更暖的纸（#fcf8f0，与主视觉烤进图里的底色同值，所以半人马放上去没有接缝）。墨只有一种（#1c1b18），粗线、正文、主按钮共用。钴蓝按双色印刷里「专色」的规矩使用：只印强调词、着重号、悬停与刊物封面，文字与界面累计 ≤5%。深度不靠阴影，全站唯一的阴影是「贴页图版」脚下那一道。签名记忆点是**文武线刊头 + 常驻页边栏**：每个版面左侧都有一条 200px 的页边栏，放章节号、栏目名和图注（与图底对齐），中间一根细栏线从头贯到尾；强调词下面点着钴蓝着重号——这是中文排版自己的强调传统，不是渐变字。

## Tokens — Colors

| Name           | Value     | Token                        | Role                                                   |
| -------------- | --------- | ---------------------------- | ------------------------------------------------------ |
| 书纸           | `#f2efe7` | `--color-background`         | 主画布，偏灰的象牙白，不换成纯白也不再加黄             |
| 墨             | `#1c1b18` | `--color-foreground`         | 正文、标题、粗线；对书纸 15:1                          |
| 图版纸         | `#fcf8f0` | `--color-card`               | 图版衬纸、贴页底；与 hero 图烤入底色同值               |
| 墨（主色）     | `#1c1b18` | `--color-primary`            | 主按钮底、封底墨版                                     |
| 反白           | `#f7f4ec` | `--color-primary-foreground` | 墨底上的文字                                           |
| 旧纸           | `#e9e4d8` | `--color-secondary`          | 次级底、骨架屏、表头                                   |
| 次要墨         | `#5d594f` | `--color-muted-foreground`   | 次要文字；对书纸 6.1:1、对旧纸 5.5:1                   |
| 细线灰         | `#d3cdbf` | `--color-border`             | 栏线、细分割线（hairline）                             |
| 粗线墨         | `#1c1b18` | `--color-rule`               | 文武线、版面顶线、图注顶线                             |
| 框线灰         | `#857e6f` | `--color-input`              | 输入框底线、禁用态虚线；对书纸 3.6:1                   |
| 钴蓝专色       | `#1b4bb0` | `--color-brand`              | 取自 logo 马身。强调词、着重号、悬停、焦点环、专色单印；字与界面 ≤5% |
| 暖深红危险     | `#8f2f26` | `--color-destructive`        | 表单出错、不可逆动作                                   |
| 暖深绿成功     | `#2f5d3a` | `--color-success`            | 复制成功等确认                                         |
| 封底墨版       | `#1c1b18` | `--color-inverse-background` | 联系区整版反白                                         |
| 墨版次要字     | `#b9b3a5` | `--color-inverse-muted`      | 墨版上的次要文字，8.3:1                                |
| 墨版细线       | `#45423b` | `--color-inverse-border`     | 墨版上的栏线                                           |

### 柔和语义色（浅底 + 深字，成对使用）

| Name | Background | Text      | Token                      |
| ---- | ---------- | --------- | -------------------------- |
| 柔蓝 | `#e1e7f3`  | `#1b4bb0` | `--color-pastel-blue-*`    |
| 柔赭 | `#f1e6cf`  | `#7a4f14` | `--color-pastel-ochre-*`   |
| 柔绿 | `#e2eadd`  | `#2f5d3a` | `--color-pastel-green-*`   |
| 柔赤 | `#f3e0da`  | `#8f2f26` | `--color-pastel-red-*`     |

四对对比度均 ≥5.7:1。柔赭专给「下载暂未开放」一类的待定状态——陶土色在本范式里只以这种低饱和形态出现，插画里的橙已经够了。

### 图表色

本站没有可引用的数据，不设图表色。将来需要时只用墨的三个灰阶 + 钴蓝一色，仍按「单专色印刷」处理。

## Tokens — Typography

### Noto Serif SC 思源宋体 — 标题 / 引文 / 导航 / 栏目名 · `--font-serif`

- **Substitute:** Songti SC, Source Han Serif SC, STSong, SimSun
- **Weights:** 500（导航、目录、封面底栏）/ 700（H2、文章标题、引文）/ 900（H1、首字下沉、产品名、署名）
- **Sizes:** 13px, 15px, 20px, 22px, 28px, 30px, 32–58px, 26–46px, 56–124px
- **Line height:** display 1.1 / 标题 1.25 / 引文 1.5
- **Letter spacing:** 标题 0.02em，导航与栏目名 0.08–0.12em（宋体小字必须拉开字距才不糊）
- **OpenType features:** `text-emphasis: dot`（着重号）
- **Role:** 一切「要被读出声」的文字。栈首放 Newsreader，让标题里的拉丁字母与数字（AI、2026）自动走衬线拉丁字形，而不是宋体自带的西文。

### Newsreader — 拉丁字、数字、英文眉标 · `--font-latin`

- **Substitute:** Iowan Old Style, Palatino Linotype, Georgia
- **Weights:** 300（章节大号数字）/ 400–500（眉标、日期）；italic 300（流程编号）
- **Sizes:** 10px, 11px, 12px, 13px, 44px, 72px
- **Letter spacing:** 全大写眉标 0.16em；刊头英文名 0.22em
- **OpenType features:** `lining-nums tabular-nums`（日期、编号）
- **Role:** 英文眉标、图注英文段、日期、章节号 01–03、流程号 01–05、箭头 ↗ → ↺。是一款为长文阅读设计的报刊衬线，opsz 轴让 72px 的章节号足够细、12px 的眉标足够稳。不用 Fraunces / Instrument Serif——这两款在 AI 生成页面里已经用滥了。

### Noto Sans SC 思源黑体 — 正文 / 按钮 / 说明 · `--font-sans`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei；拉丁回退 Helvetica Neue
- **Weights:** 400（正文）/ 500（按钮、文字链、徽标）
- **Sizes:** 13px, 14px, 15px, 16px, 18px
- **Line height:** 1.75（16px 正文 = 28px 基线）/ 1.8（18px 导语）
- **Letter spacing:** 0.02em；按钮 0.06em
- **Role:** 一切「要被扫读」的文字。回退到系统黑体时字宽几乎不变，版式不会塌。

### ui-monospace — 仅样张页 · `--font-mono`

- **Substitute:** SFMono-Regular, Menlo, Consolas
- **Role:** 只在 kit 页标 hex 与 token 名。首页不出现等宽字。

### Type Scale

| Role       | Size                      | Line Height | Letter Spacing | Token               |
| ---------- | ------------------------- | ----------- | -------------- | ------------------- |
| display    | clamp(56px, 8.4vw, 124px) | 1.1         | 0.01em         | `--text-display`    |
| heading-lg | clamp(32px, 4.2vw, 58px)  | 1.25        | 0.02em         | `--text-heading-lg` |
| quote      | clamp(26px, 3.3vw, 46px)  | 1.5         | 0.02em         | `--text-quote`      |
| heading    | 30px                      | 1.35        | 0.02em         | `--text-heading`    |
| subheading | 22px                      | 1.4         | 0.02em         | `--text-subheading` |
| body-lg    | 18px                      | 1.8         | 0.02em         | `--text-body-lg`    |
| body       | 16px                      | 1.75        | 0.02em         | `--text-body`       |
| body-sm    | 14px                      | 1.7         | 0.02em         | `--text-body-sm`    |
| caption    | 12px                      | 1.4         | 0.16em（大写） | `--text-caption`    |

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 0.25rem`）；竖向节奏以 28px 基线（`--baseline`，即 16px × 1.75）为单位，区块间距取它的整数倍。

**Density:** 舒展。刊物感来自留白被线「框住」，不是来自空。

### Spacing Scale

| Name | Value           | Token          |
| ---- | --------------- | -------------- |
| 1    | 4px             | `--spacing-1`  |
| 2    | 8px             | `--spacing-2`  |
| 3    | 12px            | `--spacing-3`  |
| 4    | 16px            | `--spacing-4`  |
| 6    | 24px            | `--spacing-6`  |
| 7    | 28px（1 基线）  | `--spacing-7`  |
| 10   | 40px            | `--spacing-10` |
| 14   | 56px（2 基线）  | `--spacing-14` |
| 21   | 84px（3 基线）  | `--spacing-21` |
| 28   | 112px（4 基线） | `--spacing-28` |
| 35   | 140px（5 基线） | `--spacing-35` |

### Border Radius

| Name | Value | Token           |
| ---- | ----- | --------------- |
| none | 0px   | `--radius-none` |
| sm   | 2px   | `--radius-sm`   |
| full | 999px | `--radius-full` |

| Element                    | Value      |
| -------------------------- | ---------- |
| 图版、期刊卡、徽标、输入框 | 0px (none) |
| 按钮                       | 2px (sm)   |
| 全站返回钮（外部规定）     | full       |

印刷品没有圆角。2px 只是让按钮在屏幕上不显得锋利，肉眼应当读作「方的」。

### Rules（线）

| Name  | Value                           | Token          | 用途                               |
| ----- | ------------------------------- | -------------- | ---------------------------------- |
| hair  | `1px solid var(--color-border)` | `--rule-hair`  | 栏线、行间分割、页边栏竖线         |
| ink   | `1px solid var(--color-rule)`   | `--rule-ink`   | 每个版面的顶线、图注顶线、目录顶线 |
| thick | `3px solid var(--color-rule)`   | `--rule-thick` | 文武线的粗线、流程表头             |

文武线 = 3px 粗线 + 3px 空 + 1px 细线，只出现在刊头下方一次。

### Shadows

| Name        | Value                                                                  | Token                  |
| ----------- | ---------------------------------------------------------------------- | ---------------------- |
| none        | `none`                                                                 | `--shadow-none`        |
| plate       | `0 1px 1px rgba(28,27,24,0.05), 0 14px 28px -18px rgba(28,27,24,0.28)` | `--shadow-plate`       |
| plate-hover | `0 1px 1px rgba(28,27,24,0.06), 0 22px 36px -18px rgba(28,27,24,0.34)` | `--shadow-plate-hover` |

阴影只属于图版：负扩散让它只在图版脚下露出一道，像一张贴进书页的插图微微翘起。按钮、卡片、输入框、导航一律无阴影。

### Motion

| Name          | Value                            | Token             |
| ------------- | -------------------------------- | ----------------- |
| ease-page     | `cubic-bezier(0.2, 0.7, 0.2, 1)` | `--ease-page`     |
| duration-fast | `160ms`                          | `--duration-fast` |
| duration-slow | `480ms`                          | `--duration-slow` |

颜色与箭头位移用 fast；标题下划线展开、图版抬起用 slow。图版入场是 `animation-timeline: view()` 的 1.06 → 1 微缩放，放在 `@supports` 里，终态即默认态；`prefers-reduced-motion` 下全部关闭。

### Layout

- **Section gap:** 版面上 56px / 下 84px（移动端 40 / 56），版面之间只隔一根墨线
- **页边栏:** 200px（≤1100px 收到 148px；≤860px 折成正文上方的一行）
- **栏间距:** 48px（≤1100px 为 32px），页边栏竖线落在栏间距正中
- **Element gap:** 28px（1 基线）
- **Max content width:** 1328px（含两侧 gutter，`clamp(20px, 4vw, 56px)`）

## Components

### 刊头 Masthead

**Role:** 全站页眉
Logo 38px + 「半人马AI学院」宋体 700/22px/0.06em + 英文名 Newsreader 10px/0.22em。导航是宋体 500/15px，项与项之间用中圆点「·」分隔（不是间距），悬停时一根 1px 钴蓝线从左向右展开。右端主按钮。下方一道文武线，再下面是一行眉标条：左侧英文眉标，右侧口号「各有知君，共创万象。」当刊物格言。不吸顶——刊头属于封面，不跟着读者走。

### 目录 TOC

**Role:** 封面左下的页内导航
顶上一根墨线，标题「目录」12px；每行宋体 500/13px，行首是 Newsreader italic 的章节号（只有真实有序的三章有号，其余用「·」）。移动端分两栏、行高 44px。

### Primary Button

**Role:** 主 CTA（联系学院顾问）
`bg-primary`(#1c1b18) `text-primary-foreground`(#f7f4ec)，1px 同色边，`border-radius: var(--radius-sm)`(2px)，`min-height: 48px`，`padding: 0 24px`，黑体 500/15px/0.06em，箭头 ↗ 用 Newsreader。hover：底与边变钴蓝 #1b4bb0，箭头 translate(2px,-2px)；active：translateY(1px)；focus-visible：2px 钴蓝环、offset 3px；disabled：透明底 + 1px 框线灰虚线 + 次要墨文字。墨版上反转为反白底墨字，hover 同样变钴蓝。

### Outline Button

**Role:** 并列的次级动作（复制客服链接）
透明底 + 1px 墨边，其余同 Primary。hover 填墨反白。墨版上边框用 `--color-inverse-muted`，hover 填反白。

### Text Link

**Role:** 行内去向（了解学院的主张 ↗）
黑体 500/16px，1px 墨色下划线，`text-underline-offset: .42em`，触控高度 44px。hover：文字与下划线变钴蓝，线加粗到 2px，箭头右上移 2px。

### 图版 Plate（章节插画框）

**Role:** 所有插画与主视觉的统一容器
`bg-card`(#fcf8f0) + `--rule-hair` 边 + 10px 衬纸留边 + `--shadow-plate`，无圆角，图 `object-fit: cover`。比例按版面定：封面 4:5（裁掉马尾，让人身顶天立地）、章节 4:3、跨栏大图 2.2:1、文章头条 2:1、列表缩略 1:1。

### 图注 Caption

**Role:** 图的说明，体例固定
一根墨线顶线 + 英文段（Newsreader 500/11px/0.16em 大写，墨色）+ 中文段（黑体 13px，次要墨）。桌面端章节图注**进页边栏**并与图底对齐；封面与移动端落在图下。

### 专色单印 Spot Print

**Role:** 观点与动态的文章封面
图 `grayscale(1) contrast(1.3) brightness(.96)`，上盖一层钴蓝 `mix-blend-mode: screen`，再盖一层图版纸 `multiply`——暗部成钴蓝，高光回到纸色，像单色胶印。作用有二：把文章封面和章节彩图拉开层级；同一张 co-learning 在页面里出现两次也不重复。

### 版面 Spread + 页边栏 Margin

**Role:** 首页每个区块的骨架（签名组件）
`grid-template-columns: 200px 1fr`，顶上一根 `--rule-ink`。页边栏放：章节号（Newsreader 300/72px）、栏目名（宋体 700/15px/0.1em）、英文眉标、图注；右缘一根 `--rule-hair` 竖线，落在 48px 栏间距正中，从版面顶贯到底。主栏内部再按 7:5 / 6:6 / 整栏分。

### 章节导语 Lede（首字下沉）

**Role:** 三个章节各自的第一段
黑体 18px/1.8，`::first-letter` 为宋体 900、3.3em、左浮动，恰好占两行。只用于章节开篇，别处不用。

### 着重号强调 Emphasis Mark

**Role:** H2 里的强调词
`color: var(--color-brand)` + `text-emphasis: dot`（under）。H1 字太大，只变钴蓝不加点。

### 产品下载行 Product Row

**Role:** 知君 / 万象
不是卡片，是表格行：顶线 `--rule-ink`，行间 `--rule-hair`。第一行产品名（宋体 900/28px/0.08em）+ 带下划线的一句话与 ↗；第二行禁用态下载按钮（虚线框）+ 13px「下载暂未开放」。

### 流程步骤 Steps

**Role:** 共学五步
五栏等分，顶上一根 3px 粗线，栏与栏之间 `--rule-hair`。编号 Newsreader italic 300/44px，步名宋体 700/20px，说明 14px 次要墨。前四栏右上角一个「→」，第五栏是钴蓝「↺」——流程是循环的。移动端改为「编号 | 步名+说明」的行。

### 期刊卡 Journal Card

**Role:** 观点与动态
无底色、无边框、无圆角。头条占 7 栏：2:1 专色单印封面 + 元信息行（栏目名钴蓝黑体 0.2em + 日期 Newsreader tabular）+ 宋体 700/30px 标题 + 摘要。右 5 栏是两条「132px 方图 + 文」的次条，之间一根细线，左侧一根竖栏线。hover：标题下 1px 墨线展开，图版上抬 2px、阴影换 plate-hover。

### 引文块 Pull Quote

**Role:** 院长寄语
宋体 700、26–46px、行高 1.5。开引号钴蓝并**悬挂**（`padding-left:.56em; text-indent:-.56em`），第二行与首字对齐；按意群断行（每个意群一个 `inline-block`），不让「人机共生」被拆开。署名在右栏：一根墨线顶线，名字前是一段 1.6em 的墨线（不用破折号字符，衬线字体里它会断成两截），宋体 900/26px/0.2em，职务两行 14px 次要墨。

### 联系横幅 Back Cover

**Role:** 页尾 CTA
整版墨底（全页唯一的大色块，当作封底），页边栏与栏线照旧但换墨版色。H2 宋体 900、32–62px，反白；右栏一句话 + 主按钮（反白底）+ 描边按钮，复制成功后在下方眉标位显示「已复制」。

### 版权页 Colophon

**Role:** 页脚
回到书纸。三栏：Logo 与名称 / 口号宋体 700、24–36px、0.16em / 右对齐的发起方链接。底下一根细线，居中一行宋体 13px/0.2em 的品牌主张。

### Input Field

**Role:** 文本输入（表单页用，首页暂无）
只有底线：`border-bottom: 1px solid var(--color-input)`，高 48px，宋体 17px，无底色无圆角——像表格里的填写线。focus：底线 2px 钴蓝；error：底线 2px `--color-destructive` + 13px 提示；disabled：虚线 + 次要墨。

### Badge

**Role:** 栏目名与状态
方角，高 24px，`padding: 0 8px`，黑体 500/12px/0.2em。默认是 1px 墨框；状态用柔和语义色成对填充（柔蓝=栏目、柔赭=未开放、柔绿=已复制、柔赤=出错）。

## Surfaces

| Level | Name       | Value     | Purpose                        |
| ----- | ---------- | --------- | ------------------------------ |
| 0     | background | `#f2efe7` | 书纸，全部版面                 |
| 1     | card       | `#fcf8f0` | 图版纸，只垫在图下面，不装文字 |
| 2     | secondary  | `#e9e4d8` | 旧纸，表头、骨架、次级底       |
| 3     | inverse    | `#1c1b18` | 封底墨版，每页至多一处         |

层级靠「换纸」和线建立。文字内容永远直接印在书纸上，不装进卡片。

## Do's and Don'ts

### Do

- 先画线再放内容：每个版面以一根 `--rule-ink` 起头，分栏用 `--rule-hair`，文武线全站只在刊头下出现一次。
- 每个区块都保留页边栏，哪怕里面只有一个栏目名——空着的页边是版式的一部分。
- 钴蓝 `#1b4bb0` 当专色用：强调词 + 着重号、悬停、焦点环、开引号、末步 ↺、专色单印。文字与界面累计 ≤5%。
- 拉丁字母和数字一律走 Newsreader（标题靠字体栈自动实现，眉标与日期显式指定），日期用 `tabular-nums`。
- 图一律进图版：图版纸衬底 + 细线框 + 10px 留边 + plate 阴影；主视觉直接放在 #fcf8f0 图版纸上，不用 multiply 硬融。
- 图注守体例：墨线顶线 + 英文大写段 + 中文段；桌面端章节图注进页边栏与图底对齐。
- 按意群手工断行：H1、H2、引文、导语都照文案稿的「/」断，不交给浏览器。
- 只给真实有序的东西编号（三章、五步）；目录里其余条目用「·」。

### Don't

- 不要把陶土橙请回来当强调色——「暖米 + 宋体 + 陶土」正是要逃离的那张脸，橙色留给插画和 logo 自己。
- 不要给任何东西加圆角卡片底。要分区就画线，要强调就换纸。
- 不要在图版以外的任何元素上用阴影；不要用大于 2px 的圆角。
- 不要用纯黑 `#000000` 和纯白 `#ffffff`：墨是 #1c1b18，最亮的纸是 #fcf8f0。
- 不要让钴蓝成块出现在静止状态（悬停中的按钮、专色单印图除外）；不要做钴蓝渐变、钴蓝发光。
- 不要在章节开篇以外的地方用首字下沉。
- 不要用 Fraunces、Instrument Serif、Inter；不要让宋体小于 13px，不要让宋体小字不拉字距。
- 不要编造期号、页码、数据、客户 logo。刊物感来自版式，不来自假装有一本刊物。
- 不要写「全面、深入、赋能、打造、极致」。

## Imagery

四张插画本身就是暖色纸艺风格，和书纸同一家族，所以处理原则是「装裱」而不是「调色」：一律进图版（图版纸衬底、细线框、10px 留边、脚下一道阴影），像贴进书页的插图。主视觉半人马的底色 #fcf8f0 烤在图里，图版纸取同值，接缝自然消失；封面用 4:5 竖裁，裁掉马尾，让人身到马蹄撑满图版。跨栏大图用 2.2:1 横裁（对准三人上半身），文章头条用 2:1 裁同一张图的下半（桌面与纸），再加专色单印——同图两用而不重复。文章封面统一钴蓝专色单印，和章节彩图形成「正文插图 / 目录缩略」两个层级。图标不用图标库：箭头 ↗ → ↓ ↺ 直接用 Newsreader 的字形，细、带衬线感，和正文一个调子。没有装饰性图形，没有背景纹理——纸感来自颜色和线，不来自噪点贴图。

## Layout

1328px 容器，两侧 gutter `clamp(20px,4vw,56px)`。封面是三行网格：眉标条通栏；H1 横跨「页边栏 + 正文栏」两栏，右侧 456px 的竖图版从第二行贯到底；第三行左为目录、右为副标题/说明/按钮，两者顶线对齐成一条水平基准。封面以一行通栏的品牌主张收尾（上墨线下细线）。其后每个区块都是「200px 页边栏 + 主栏」的版面，主栏内三章分别用 7:5（图左文右）、整栏跨栏大图 + 下方 7:5 文字、6:6（图左，文与产品行右）；五步是五栏表；观点是 7:5 头条 + 次条；寄语是整栏引文 + 7:5 正文/署名；联系是 8:4。全页只有联系区一处满幅色块（封底墨版），其余全部是书纸加线。≤1100px 页边栏收窄到 148px；≤860px 全部单栏，页边栏折成「章节号 + 栏目名」一行并带一根细底线，导航收进「目录」按钮，五步改为竖排行。

## Agent Prompt Guide

Quick Color Reference:

```
background (书纸): #f2efe7
foreground / rule (墨): #1c1b18
card (图版纸，只垫图): #fcf8f0
secondary (旧纸): #e9e4d8
border (细线): #d3cdbf
muted-foreground: #5d594f
brand 钴蓝专色 (≤5%): #1b4bb0
inverse (封底墨版): #1c1b18 / #f7f4ec / #b9b3a5
```

Example Component Prompts:

1. Create a section "spread": CSS grid `200px 1fr`, gap 48px, `border-top: 1px solid #1c1b18`, padding 56px 0 84px. Left margin column holds a Newsreader 300 72px chapter number and a Noto Serif SC 700 15px label with 0.1em tracking; its right edge carries a `1px solid #d3cdbf` rule centered in the gap. No card backgrounds, no radius. Below 860px collapse to one column and turn the margin column into a single baseline-aligned row with a hairline underneath.
2. Create an image plate: wrapper `background:#fcf8f0; border:1px solid #d3cdbf; padding:10px; box-shadow:0 1px 1px rgba(28,27,24,.05), 0 14px 28px -18px rgba(28,27,24,.28)`, no radius, image `object-fit:cover` at a fixed aspect ratio. Caption: `border-top:1px solid #1c1b18`, an uppercase Newsreader 11px label tracked 0.16em in ink, then a 13px sans line in #5d594f. On desktop position the caption absolutely into the left margin column, bottom-aligned with the image.
3. Create a heading with emphasis: Noto Serif SC 700, `clamp(32px,4.2vw,58px)`, line-height 1.25, manual line breaks. Wrap the key word in `<em>` styled `font-style:normal; color:#1b4bb0; text-emphasis: dot #1b4bb0; text-emphasis-position: under right`. Never use gradient text or a colored underline instead.
4. Create a primary button: `background:#1c1b18; color:#f7f4ec; border:1px solid #1c1b18; border-radius:2px; min-height:48px; padding:0 24px; font: 500 15px sans; letter-spacing:.06em`, trailing ↗ set in Newsreader. Hover swaps background and border to #1b4bb0 and nudges the arrow `translate(2px,-2px)` over 160ms `cubic-bezier(.2,.7,.2,1)`. Disabled: transparent, `1px dashed #857e6f`, text #5d594f. No shadow in any state.

## Similar Brands

- **Anthropic（anthropic.com）** — 抓了 `ant-brand.shared…min.css`：ivory 三阶 #faf9f5 / #f0eee6 / #e8e6dc、slate #141413、clay #d97757、正文也用衬线、圆角 4/8/16px、阴影透明度只有 0.01–0.04。借了「偏灰的象牙白而不是偏黄的米色」（书纸 #f2efe7 贴着它的 ivory-medium）、暖近黑当墨、阴影近乎没有；**没借**它的 clay 橙和 8px 圆角——那正是被模仿得最多的部分。
- **Stripe Press（press.stripe.com）** — 抓了 `v1-Page…css`：全站 Ivar Text / Ivar Headline / Ivar Display 三款衬线，正文字重 500，按钮字距 0.32px，`h1–h6 { line-height:1 }`，页边距 `calc(10px + 1vw)`，每本书自带一套底色。借了「衬线不只给标题，也给导航和小字」的胆量、随视口线性变化的 gutter，以及「一本书一个颜色」→ 本站「一份刊一个专色」。
- **The New Yorker（newyorker.com）** — 首页内联样式里：墨色 #231f20 而非纯黑；TNY Adobe Caslon + Irvin Heading + Graphik 三分工；分割线明确分两档 `1px solid rgba(51,51,51,1)` 与 `1px solid rgba(229,229,229,1)`；容器 max-width 1600px。借了「深线 / 浅线」两档制（→ `--rule-ink` / `--rule-hair`）、衬线标题 + 无衬线元信息 + 特征字体三分工、元信息行「栏目 · 日期」的体例。
- **Monocle（monocle.com）** — 首页变量：Plantin + Helvetica Neue，画布 #fdfcf3 / #fdfbe4，neutral 灰阶 #f9f9f9 → #2a2929，圆角只有 2px / 4px，红 #e10912 极少量，正文栏宽 `min(50rem, 100vw - 2.5rem)`。借了 2px 圆角上限、「Plantin 配 Helvetica」式的衬线标题 + 黑体正文（拉丁回退首选 Helvetica Neue）、小号全大写拉字距的栏目标。
- **单向空间 owspace（owspace.com）** — 抓了 `style.css`：正文 `'Hiragino Sans GB','Microsoft YaHei'` 16/22px，内容栏只有 760px，链接与按钮是金色 #bea353 + `border:solid 1px` 的方角描边框，底色 #f8f7f5。借了中文语境下「方角 1px 描边按钮 + 窄栏 + 大量留白」的做法，确认了「单一强调色 + 无圆角」在中文文化品牌里成立；没借金色。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 两种纸 + 一种墨 + 一种专色 */
  --color-background: #f2efe7;
  --color-foreground: #1c1b18;
  --color-card: #fcf8f0;
  --color-card-foreground: #1c1b18;
  --color-primary: #1c1b18;
  --color-primary-foreground: #f7f4ec;
  --color-secondary: #e9e4d8;
  --color-secondary-foreground: #1c1b18;
  --color-muted: #e9e4d8;
  --color-muted-foreground: #5d594f;
  --color-brand: #1b4bb0;
  --color-brand-foreground: #f7f4ec;
  --color-border: #d3cdbf;
  --color-rule: #1c1b18;
  --color-input: #857e6f;
  --color-ring: #1b4bb0;
  --color-destructive: #8f2f26;
  --color-destructive-foreground: #f7f4ec;
  --color-success: #2f5d3a;
  --color-success-foreground: #f7f4ec;

  /* Inverse — 封底墨版 */
  --color-inverse-background: #1c1b18;
  --color-inverse-foreground: #f7f4ec;
  --color-inverse-muted: #b9b3a5;
  --color-inverse-border: #45423b;

  /* Pastel semantic pairs */
  --color-pastel-blue-bg: #e1e7f3;
  --color-pastel-blue-text: #1b4bb0;
  --color-pastel-ochre-bg: #f1e6cf;
  --color-pastel-ochre-text: #7a4f14;
  --color-pastel-green-bg: #e2eadd;
  --color-pastel-green-text: #2f5d3a;
  --color-pastel-red-bg: #f3e0da;
  --color-pastel-red-text: #8f2f26;

  /* Typography — Font Families */
  --font-serif:
    'Newsreader', 'Noto Serif SC', 'Songti SC', 'Source Han Serif SC', STSong,
    SimSun, 'Iowan Old Style', Georgia, serif;
  --font-sans:
    'Helvetica Neue', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', sans-serif;
  --font-latin:
    'Newsreader', 'Iowan Old Style', 'Palatino Linotype', Georgia, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  /* Typography — Scale */
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 22px;
  --text-heading: 30px;
  --text-heading-lg: clamp(32px, 4.2vw, 58px);
  --text-display: clamp(56px, 8.4vw, 124px);
  --text-quote: clamp(26px, 3.3vw, 46px);

  /* Line Height & Tracking */
  --leading-display: 1.1;
  --leading-heading: 1.25;
  --leading-body: 1.75;
  --tracking-display: 0.01em;
  --tracking-heading: 0.02em;
  --tracking-body: 0.02em;
  --tracking-caps: 0.16em;

  /* Spacing — 4px base，竖向节奏以 28px 基线为单位 */
  --spacing: 0.25rem;
  --baseline: 28px;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-6: 24px;
  --spacing-7: 28px;
  --spacing-10: 40px;
  --spacing-14: 56px;
  --spacing-21: 84px;
  --spacing-28: 112px;
  --spacing-35: 140px;

  /* Layout */
  --container: 1328px;
  --gutter: clamp(20px, 4vw, 56px);
  --margin-col: 200px;
  --col-gap: 48px;

  /* Rules — 线是这套范式的主要装饰 */
  --rule-hair: 1px solid var(--color-border);
  --rule-ink: 1px solid var(--color-rule);
  --rule-thick: 3px solid var(--color-rule);

  /* Border Radius — 印刷品没有圆角 */
  --radius-none: 0px;
  --radius-sm: 2px;
  --radius-full: 999px;

  /* Shadows — 只有「贴页图版」一处 */
  --shadow-none: none;
  --shadow-plate:
    0 1px 1px rgba(28, 27, 24, 0.05), 0 14px 28px -18px rgba(28, 27, 24, 0.28);
  --shadow-plate-hover:
    0 1px 1px rgba(28, 27, 24, 0.06), 0 22px 36px -18px rgba(28, 27, 24, 0.34);

  /* Motion */
  --ease-page: cubic-bezier(0.2, 0.7, 0.2, 1);
  --duration-fast: 160ms;
  --duration-slow: 480ms;
}
```

### Tailwind v4

```css
@theme {
  /* Colors — 两种纸 + 一种墨 + 一种专色 */
  --color-background: #f2efe7;
  --color-foreground: #1c1b18;
  --color-card: #fcf8f0;
  --color-card-foreground: #1c1b18;
  --color-primary: #1c1b18;
  --color-primary-foreground: #f7f4ec;
  --color-secondary: #e9e4d8;
  --color-secondary-foreground: #1c1b18;
  --color-muted: #e9e4d8;
  --color-muted-foreground: #5d594f;
  --color-brand: #1b4bb0;
  --color-brand-foreground: #f7f4ec;
  --color-border: #d3cdbf;
  --color-rule: #1c1b18;
  --color-input: #857e6f;
  --color-ring: #1b4bb0;
  --color-destructive: #8f2f26;
  --color-destructive-foreground: #f7f4ec;
  --color-success: #2f5d3a;
  --color-success-foreground: #f7f4ec;

  /* Inverse — 封底墨版 */
  --color-inverse-background: #1c1b18;
  --color-inverse-foreground: #f7f4ec;
  --color-inverse-muted: #b9b3a5;
  --color-inverse-border: #45423b;

  /* Pastel semantic pairs */
  --color-pastel-blue-bg: #e1e7f3;
  --color-pastel-blue-text: #1b4bb0;
  --color-pastel-ochre-bg: #f1e6cf;
  --color-pastel-ochre-text: #7a4f14;
  --color-pastel-green-bg: #e2eadd;
  --color-pastel-green-text: #2f5d3a;
  --color-pastel-red-bg: #f3e0da;
  --color-pastel-red-text: #8f2f26;

  /* Typography — Font Families */
  --font-serif:
    'Newsreader', 'Noto Serif SC', 'Songti SC', 'Source Han Serif SC', STSong,
    SimSun, 'Iowan Old Style', Georgia, serif;
  --font-sans:
    'Helvetica Neue', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', sans-serif;
  --font-latin:
    'Newsreader', 'Iowan Old Style', 'Palatino Linotype', Georgia, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  /* Typography — Scale */
  --text-caption: 12px;
  --text-body-sm: 14px;
  --text-body: 16px;
  --text-body-lg: 18px;
  --text-subheading: 22px;
  --text-heading: 30px;
  --text-heading-lg: clamp(32px, 4.2vw, 58px);
  --text-display: clamp(56px, 8.4vw, 124px);
  --text-quote: clamp(26px, 3.3vw, 46px);

  --spacing: 0.25rem;

  /* Border Radius — 印刷品没有圆角 */
  --radius-none: 0px;
  --radius-sm: 2px;
  --radius-full: 999px;

  /* Shadows — 只有「贴页图版」一处 */
  --shadow-none: none;
  --shadow-plate:
    0 1px 1px rgba(28, 27, 24, 0.05), 0 14px 28px -18px rgba(28, 27, 24, 0.28);
  --shadow-plate-hover:
    0 1px 1px rgba(28, 27, 24, 0.06), 0 22px 36px -18px rgba(28, 27, 24, 0.34);

  /* Motion */
  --ease-page: cubic-bezier(0.2, 0.7, 0.2, 1);
}
```

间距、栏宽、线与时长类 token（`--baseline`、`--margin-col`、`--rule-*`、`--duration-*` 等）不进 `@theme`，留在 `:root` 由组件直接引用。
