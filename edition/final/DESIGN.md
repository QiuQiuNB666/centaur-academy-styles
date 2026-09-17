# 半人马AI学院 · 刊本 · 定稿（Final Edition） — Style Reference

> 黑场开幕，半人马随滚动放大成「HUMAN × AI」终幕，撕开进入奶油纸页；章节名用喊的，故事用讲的，标签用记的。

**Theme:** 开幕 dark（纯黑 #000000）→ 正文 light（橄榄奶油 #f1efe6，第三章翻成橄榄墨 #25251b）→ 收尾 dark（橄榄深墨 #1b1b13）

这一版的骨架照 Shopify Editions Winter '26：先是一块只有黄金分割构图线、细白画框和标题锁定的黑场，框里站着一只小小的半人马；往下滚，它在钉住的舞台里从 0.46 倍放大到 1 倍，构图线同步向外展开，开幕文字退场，框上方升起一行超大拉丁字「HUMAN × AI」，右上是等宽书眉，底部两角是带橘橙短横的宋体「人的意愿 / 能力的延伸」——这一屏是终幕；终幕一到位，页面就沿一条像素撕纸边切进奶油纸页。纸页第一眼是一条全宽主张大字带「人决定方向，/ AI 拓展人的能力。」（第二行纸面橘橙），然后才是三章。正文是「三声部」编排：Noto Sans SC 900 的巨型紧排字喊章节名，Noto Serif SC 讲叙述句，Geist Mono 小字记编号、日期、图注。颜色只有两个——橄榄奶油和橄榄墨——加一组同色相的橄榄灰；logo 里的橘橙 #f07800 是唯一的界面强色，只出现在顶栏色条、主 CTA、开幕标题的强调词、终幕短横线、第三章的下载描边、第一步瓦片的大数字和引号上，主张带第二行用加深一档的纸面橘橙 #c25f00，全页面积不超过 3%；logo 的钴蓝一滴都不进界面，留给 logo 和插画。插画不做滤镜，像画作一样放进衬纸（#e4e1d4）里装裱，外加 1px 墨线内框，右下角压一块奶油底等宽角标（EXPERIENCE），图下一行衬线中文图注。所有面零圆角、零阴影，只有按钮和标签是胶囊；层次靠发丝线和底色切换：纸面上三根竖发丝贯穿全页，每个区块顶线处再有一根横发丝通到两侧页边；第三章整章翻成墨色，是纸页中段唯一一次明暗翻转。签名记忆点是开幕的**「画框放大」**：黑场里的细画框先把半人马装成一幅小画，滚动时画和框一起长大，画框标签（PLATE I）与图注沿对角线被推到放大后的框角。

## Tokens — Colors

| Name             | Value     | Token                        | Role                                                         |
| ---------------- | --------- | ---------------------------- | ------------------------------------------------------------ |
| 黑场             | `#000000` | `--color-void`               | 只用于开幕舞台与顶栏书脊                                     |
| 橄榄奶油纸       | `#f1efe6` | `--color-paper`              | 正文画布；暗面上的主文字                                     |
| 衬纸             | `#e4e1d4` | `--color-paper-deep`         | 插画衬纸、期刊卡封面衬底、步骤瓦片、引文右半                 |
| 橄榄墨           | `#25251b` | `--color-ink`                | 正文文字、分区头黑线、第三章整章底、第一步瓦片、院长寄语左半、焦点环、步骤大数字 |
| 橄榄深墨         | `#1b1b13` | `--color-ink-deep`           | 联系区与页脚的暗底                                           |
| 发丝             | `#d2cfc0` | `--color-hair`               | 纸面分隔线、描边瓦片、目录与主张带左栏竖线                   |
| 暗面发丝         | `#3a3a2e` | `--color-hair-dark`          | 暗面分隔线、顶栏竖线、第三章里的横发丝                       |
| 橄榄灰 · 中      | `#5e5d51` | `--color-grey-mid`           | 次要文字、日期、目录罗马数字；纸上 5.8:1、衬纸上 5.1:1       |
| 橄榄灰 · 深      | `#45443a` | `--color-grey-dark`          | 正文说明段落；衬纸上 7.5:1                                   |
| 暗面主文字       | `#f1efe6` | `--color-on-dark`            | 黑场与深墨上的标题、正文                                     |
| 暗面次要         | `#bfbeb0` | `--color-on-dark-muted`      | 黑场小字、第三章说明与禁用按钮字；黑底 11.2:1、墨底 8.3:1、深墨底 9.2:1 |
| 橘橙（唯一强色） | `#f07800` | `--color-accent`             | 顶栏色条、主 CTA、开幕强调词、01 大数字、引号；≤3%          |
| 橘橙按下         | `#d86a00` | `--color-accent-press`       | 橘橙的 hover / active、输入框错误边                           |
| 纸面橘橙字       | `#c25f00` | `--color-accent-ink`         | 只用于纸面上 ≥34px 的 900 大字（主张带第二行），奶油纸上 3.7:1，过大字 3:1 线 |
| 橘橙上的字       | `#25251b` | `--color-accent-foreground`  | 橘橙底上的文字，5.4:1                                        |
| logo 钴蓝        | `#0c6ccc` | `--color-logo-blue`          | 只记录，不进界面；logo 与插画里自带                          |
| 构图线           | `rgba(241,239,230,.17)` | `--color-construct` | 黑场黄金分割线                                          |
| 构图线 · 强      | `rgba(241,239,230,.42)` | `--color-construct-strong` | 开幕画框、暗面描边按钮                             |
| 纸面构图线       | `rgba(37,37,27,.07)` | `--color-construct-paper` | 按钮图标圆的底                                          |
| 网格发丝         | `rgba(94,93,81,.25)` | `--color-grid` | ③ 的可见网格：三根贯穿竖发丝 + 各区块顶线处的全宽横发丝；橄榄灰，不用 Dropbox 的钴蓝 |
| 返回钮垫底       | `rgba(241,239,230,.88)` | `--color-back-pad` | 左下「← 全部方案」下面垫的奶油半透明胶囊，保证黑场上能看见 |
| 禁用底 / 字      | `#e4e1d4` / `#5e5d51` | `--color-disabled-bg` / `--color-disabled-fg` | 「下载暂未开放」按钮                    |
| 焦点环           | `#25251b` / `#f07800` | `--color-ring` / `--color-ring-dark` | 纸面用墨色环，暗面用橘橙环，2px + 3px 偏移      |

### 柔和语义色（本范式不设）

| Name | Background | Text | Token |
| ---- | ---------- | ---- | ----- |
| —    | —          | —    | —     |

刊本没有「成功 / 警告」类状态，唯一的状态是「下载暂未开放」，用禁用底色 + 等宽小字表达，不引入第三种色相。橘橙也不当状态色用。

### 图表色（本范式不设）

| Name | Value | Token |
| ---- | ----- | ----- |
| —    | —     | —     |

学院首页没有图表，也没有任何可引用的数据；需要示意时用发丝线与等宽标注，不引入图表色。

## Tokens — Typography

### Noto Sans SC — 喊：章节名、开幕标题、步骤名、页脚字标 · `--font-sans`（`--font-display` 的中文部分）

- **Substitute:** PingFang SC, "Hiragino Sans GB", "Microsoft YaHei", system-ui
- **Weights:** 400（正文）, 700（导航、按钮、卡片标题）, 900（喊）
- **Sizes:** 15px, 16px, 21px, 32px, 56px, 92px, 104px, 148px, 236px
- **Line height:** 喊 1.02 / 开幕 1.06 / 正文 1.75
- **Letter spacing:** 喊与开幕 -0.02em（中文下限，不再更紧）/ 正文 0
- **Role:** 全站中文 UI 与所有「喊」的声部。回退到苹方时 900 会落成 600，所以版式靠字号撑，不靠字重。

### Instrument Sans — 喊的拉丁部分 · `--font-display`

- **Substitute:** 同上中文栈（Instrument Sans 没有中文，中文字符自动落到 Noto Sans SC）
- **Weights:** 400–700（可变），wdth 75–100
- **Role:** 标题里的「AI」、步骤大数字 01–05（02–05 用 400 细体墨色，01 用 700 橘橙）、终幕「HUMAN × AI」（600，clamp(64px, 8.2vw, 124px)，字距 -0.045em，行高 1）。替代 Shopify 的 NeueMontreal，比 Inter 更窄更硬。

### Noto Serif SC — 讲：叙述句、章节 H2、引文、图注 · `--font-serif-zh`

- **Substitute:** "Songti SC", STSong, SimSun
- **Weights:** 500, 700
- **Sizes:** 16px, 17px, 18px, 20px, 26px, 30px, 46px, 50px
- **Line height:** 标题 1.18 / 叙述 1.45–1.5 / 引文 1.36
- **Role:** Shopify 的 HWCigars 那一声。强调词不换色，换声部：落回 Noto Sans SC 900（例：你走过的路，都是**起点**。）

### Instrument Serif — 罗马数字与引号 · `--font-serif`

- **Substitute:** Noto Serif SC → Songti SC → serif
- **Weights:** 400
- **Role:** 目录与分区头右端的 I–VII、院长寄语的大引号。代替 Shopify 的 ImperialScript 花体，只做点睛。

### Geist Mono — 记：编号、日期、图注、分区头 · `--font-mono`

- **Substitute:** ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas
- **Weights:** 400, 500
- **Sizes:** 12px, 13px, 14px
- **Letter spacing:** +0.06em，大写
- **Role:** ② 的 Geist Mono 署名与标签、插画角标。只在 12–14px 出现，从不放大；35–55 岁读者为主，默认 13px。

### Type Scale

| Role      | Size                               | Line Height | Letter Spacing | Token              |
| --------- | ---------------------------------- | ----------- | -------------- | ------------------ |
| wordmark  | clamp(64px, 14.6vw, 216px)（页面实用 min(16.2vw, 236px)） | 1.0 | -0.03em | `--text-wordmark` |
| shout     | clamp(52px, 9.4vw − 8px, 148px)    | 1.02        | -0.02em        | `--text-shout`     |
| finale    | clamp(64px, 8.2vw, 124px) Instrument Sans 600 | 1.0 | -0.045em | —（仅终幕）      |
| claim     | clamp(34px, 7vw, 112px) Noto Sans SC 900 | 1.1 | -0.02em | —（仅主张带）      |
| display   | clamp(44px, 5.4vw + 8px, 92px)（开幕 H1 用 clamp(44px, 8vw − 12px, 104px)，1024px 时约 70px，给放大后的画框留出 70px 以上） | 1.06        | -0.02em        | `--text-display`   |
| heading   | clamp(30px, 2.4vw + 14px, 50px)    | 1.18        | -0.01em        | `--text-heading`   |
| narrative | clamp(22px, 1.2vw + 14px, 30px)    | 1.5         | 0              | `--text-narrative` |
| lede      | 19px                               | 1.75        | 0              | `--text-lede`      |
| body      | 16px                               | 1.75        | 0              | `--text-body`      |
| body-sm   | 16px（期刊摘要、图注）             | 1.75        | 0              | `--text-body-sm`   |
| caption   | 15px（输入框提示、样张注释）       | 1.5         | 0              | `--text-caption`   |
| label     | 13px mono 大写                     | 1.4         | +0.06em        | `--text-label`     |

规律照 ②④：字越大字距越紧、行高越贴；但中文字距封底 -0.02em、展示级行高不低于 1.02。读者 35–55 岁：正文与说明不小于 16px，其余小字不小于 15px，等宽标签不小于 12px，黑底上的次要灰用 #bfbeb0 而不是更暗的一档。

## Tokens — Spacing & Shapes

**Base unit:** 4px（`--spacing: 4px`）

**Density:** 中疏——章节之间 88–120px，区块内部 28–72px，章节标题上下留白每章不同；空纸不超过 150px，避免读成「内容缺失」

### Spacing Scale

| Name          | Value  | Token          |
| ------------- | ------ | -------------- |
| gutter        | 16px   | `--gutter`     |
| col-gap       | 16px   | `--col-gap`    |
| header        | 56px   | `--header-h`   |
| toc           | 248px  | `--toc-width`  |
| content max   | 1160px | `--content-max`|
| 主张带上      | 112px  | —              |
| 章首 I 上/下  | 88 / 64px   | —         |
| 章首 II 上/下 | 104 / 88px  | —         |
| 章首 III 上/下| 88 / 112px（墨色整章内） | — |
| 返回钮安全区  | 左下 64px，黑场里的文字不下探到这里 | — |
| 返回钮垫底宽  | 94px   | `--back-pad-w` |

### Border Radius

| Name | Value  | Token           |
| ---- | ------ | --------------- |
| none | 0px    | `--radius-none` |
| pill | 999px  | `--radius-pill` |

| Element          | Value |
| ---------------- | ----- |
| 画框 / 衬纸      | 0     |
| 瓦片 / 期刊卡    | 0     |
| 输入框           | 0     |
| 顶栏 CTA 色条    | 0     |
| 按钮             | pill  |
| 按钮内图标圆     | pill  |
| 标签             | pill  |

两极化：面一律直角，能点的一律胶囊。中间值（4px、8px、12px）不存在。

### Shadows

| Name | Value  | Token           |
| ---- | ------ | --------------- |
| none | `none` | `--shadow-none` |

不用阴影。插画的层次来自「衬纸 + 1px 墨线内框」，卡片的层次来自衬纸底色。

### Motion

| Name        | Value                                  | Token          |
| ----------- | -------------------------------------- | -------------- |
| ease-edition| `cubic-bezier(0.72, 0.16, 0.19, 0.96)` | `--ease-edition` |
| ease-settle | `cubic-bezier(0.41, 0.19, 0.13, 0.95)` | `--ease-settle`  |
| dur-fast    | 0.2s                                   | `--dur-fast`   |
| dur-base    | 0.45s                                  | `--dur-base`   |

两条曲线都取自 Shopify Editions 的实测值。**滑动放大 + 终幕**：`.stage` 高两屏（`--pin-h = max(640px, min(100svh, 900px) − 56px)`，额外滚动正好一屏，<120vh），内层 `.stage-pin` `position: sticky`。钉住层按页面滚动距离驱动（`animation-timeline: scroll(root)`，页面顶部就是舞台）：0 → 0.7 屏 `.figure-box` 从 `scale(.46)` 到 `scale(1)`，构图线 SVG 从 `scale(1) / opacity 1` 到 `scale(1.28) / opacity .6`，画框标签与图注沿对角线平移 28% 的框半径；0.5 → 0.78 屏开幕文字（眉标、H1、导语与按钮、主张、INDEX、画框标签、图注）淡出并 `visibility: hidden`。终幕 `.finale` 与钉住层同高，绝对定位在舞台底部，声明 `view-timeline: --fin` 且 `view-timeline-inset: 56px 0`：它从下方升起的最后 40% 里 HUMAN × AI、书眉与两角宋体淡入；它的半人马副本只在 `exit-crossing -2px → 0` 这 2px 里出现，此时与钉住层的半人马像素级重合，释放后两层一起滚走，接撕纸边。整段写在 `@supports (animation-timeline: view())` + `min-width:1024px` + `prefers-reduced-motion: no-preference` 里，`animation-timeline` 都写在 `animation` 简写之后；终幕淡入再多一层 `max-height:1600px`。默认样式是静态终态：钉住层是放大后的画面，终幕是一块不透明黑卡，滚动时像 ② 的叠卡一样从下面盖上来——不支持的浏览器、减少动效、超高窗口（整页截图）都看到「开幕 + 终幕」两屏，1023px 以下终幕隐藏、舞台改为堆叠（见下方「手机/平板滑动放大」）。图框按终态排版（`min(760px, 52vw)`），只从小放到 1，2 倍屏不糊。只动 transform、opacity（与 visibility 的离散切换）。

**手机/平板滑动放大（<1024px）**：舞台是纵向堆叠（标题 → 画框 → 导语 → 主张），画框外包一层不钉住的 `.stage-zoom`，它声明 `view-timeline: --mz`（`.stage-pin` 上 `timeline-scope: --mz`），`view-timeline-inset` 顶边 = 顶栏 56px + 16px（钉线 `--mz-top`）。画框 `.stage-figure` 在外层里 `position: sticky; top: 72px`，外层用 `::after` 垫出 `--mz-extra = min(10svh, 84px)` 的钉住距离（sticky 只能在父级内容盒里移动，垫 padding 无效）；这段垫高在钉住开始时就等于画框与导语之间多出的黑带，所以只给一小段——45svh 时首屏以约 220px 黑带收尾、钉住期间黑带占视口约 40%，已弃用。区间变量（`--mz-top / --mz-lead / --mz-extra / --zoom-w / --mz-shift`）挂在 `.stage-pin` 上，构图线不在 `.stage-zoom` 里也能读到同一区间。区间 `exit-crossing −lead → exit-crossing +extra`，`--mz-lead = min(24svh, 200px)`：外层顶边从「钉线下方 lead」滚到「钉线上方 extra」；390×844 下即 scrollY 约 0 → 260，其中约 180 → 260 画框钉住；首屏画框下方约 150px 后即是导语。区间内同时发生：半人马 `scale(.62) → 1`；画框细线（`.stage-frame`，装饰 span）`scale(.985, .8) → 1`（横向只收一点：768 宽下每边收进约 5px，不碰 14px 内边距里的标签与图注）；「PLATE I」与图注从贴近小图的位置（±`--zoom-w × .075 + 11px`，约等于细线收进的距离）让位回原位；构图线 `scale(.86) / opacity .7 → 1 / .45`；手机/平板上构图线 SVG 左对齐页边距、宽 `100cqw`（`.stage-pin` 设 `container-type: inline-size`）、高 `100cqw × 844 / 380`、`overflow: visible`，于是 530 / 910 两根竖线在终态正好与画框细线重合，放大过程中从内侧收拢过去，不会出现相距几 px 的「双线」（三根竖线的端点延长到视框外，桌面端被 SVG 视口裁掉，外观不变）。曲线都是 `--ease-settle`。**尺寸**：按终态排版，`--zoom-w = min(100vw, 724px, (min(100svh, 900px) − 180px) × 4/3)`，≥2.5dppx 时上限改 480px——原图 1448px 宽，3 倍屏超过 480 CSS px、2 倍屏超过 724 CSS px 就发糊，所以只从小放到 1、不往上放；终态宽 100vw，左右越出画框细线约 16px（破框），`.stage-pin` 用 `overflow: clip` 裁掉，不产生横向滚动也不破坏 sticky；高度项让画框在横屏矮视口里也装得下。放大只在画框自己的盒子里发生，不压标题和导语。实测宽度：390 宽 245 → 390px，768 宽 451 → 724px。静态样式就是终态，减少动效时直接显示。**兜底**：页面底部脚本在 `!CSS.supports('(animation-timeline: view())')`（安卓微信内核、iOS 26 以下 Safari）且非减少动效时给 `<html>` 加 `.sd-js`，用 IntersectionObserver 只在舞台附近挂 passive `scroll` 监听，rAF 节流，按同一区间与同一贝塞尔曲线直接写 transform / opacity；钉住段放在 `@supports (overflow: clip)` 里，老内核只放大不钉住。桌面端兜底复刻 `scrollY 0 → 0.7 屏` 的 `.46 → 1` 放大和构图线展开，开幕文字不退场，终幕按静态两屏显示。调试：URL 带 `?nosd` 时加 `.nosd`，所有 CSS 滚动动画选择器都挂在 `:root:not(.nosd)` 下失效，强制走 JS 路径。

### Layout

- **Section gap:** 章节 88–120px，区块内 28–72px
- **Card padding:** 衬纸 clamp(18px, 4.2vw, 64px)；瓦片 22–24px
- **Element gap:** 10px（瓦片）/ 16px（栏距）
- **Max content width:** 左侧 248px 固定目录 + 1160px 内容区，内容区 12 列

## Components

### 顶栏书脊（Masthead）

**Role:** 全站唯一的固定层
高 56px，纯黑底。左起：248px 宽字标块（logo 26px + 「半人马AI学院」900/17px + 等宽 CENTAUR AI ACADEMY），右侧 1px 暗面发丝；紧接满高橘橙色条 `clamp(200px,24vw,340px)`，文字「联系学院顾问 ↗」贴右，箭头与文字同字体、同 700 字重、同墨色；再往右是纯文字导航 15px/700，hover 变橘橙。1023px 以下导航收进「菜单 +」橘橙块，展开为黑底全宽列表，「+」旋转 45° 成「×」。

### Primary Button（accent 胶囊）

**Role:** 主 CTA「联系学院顾问」
`bg --color-accent` `color --color-accent-foreground`，`border-radius: var(--radius-pill)`，高 48px，`padding: 4px 4px 4px 22px`，15px/700。右端嵌 40px 墨色圆，圆里是 17px 奶油色 ↗（按钮套按钮；橘橙箭头在墨圆里对比不够，已弃用）。hover：底色 `--color-accent-press`，图标圆 `translate(2px,-2px)`；active：`scale(.97)`；focus：2px 环 + 3px 偏移。每屏最多一个。

### Ink / Line Button

**Role:** 次级动作
ink：墨底奶油字，图标圆奶油底；line：透明底 1px 墨线，hover 反成墨底、图标圆变橘橙。小号 `.btn--sm` 高 44px。暗面上 line 按钮改用 `--color-construct-strong` 描边。

### Disabled Download Button

**Role:** 「下载知君 ↓」「下载万象 ↓」
`disabled` 属性，衬纸底 + 发丝边 + 橄榄灰字，图标圆透明、不响应 hover；右侧并排等宽小字「下载暂未开放」。在第三章墨色整章里改为透明底 + 1px 橘橙描边 + `#bfbeb0` 字。

### 分区头（Section Rule）

**Role:** ② 的「线 + 等宽标签」
1px 墨色通栏线，线下 12px：左端等宽标签（01 / 、CENTAUR JOURNAL / 观点与动态、FROM THE FOUNDER），右端 Instrument Serif 罗马数字。每个区块都以它开头。线的位置再向左右各延一根 `--color-grid` 横发丝直到视口边（`::before`，`left/right: -100vw`，`.edition { overflow-x: clip }` 收边），穿过左侧目录栏——这是 ③「线贯穿一切」的落地。

### 章首喊字（Shout）

**Role:** 章节名
Noto Sans SC 900，148px，行高 1.02，字距 -0.02em，一行到底。章 I 左齐、章 II 右齐、章 III 左齐且反白在墨色整章里——三章三种位置，不重复。

### 画作式装裱框（Plate）

**Role:** 三张章节插画的唯一处理
`figure.plate` → 衬纸 `.mat`（clamp 18–64px 内边距）→ 插画 1448:1086 + 1px 墨线内框 → 插画右下角压一块奶油底等宽角标（EXPERIENCE / LEARN TOGETHER / MAKE IT REAL，13px，`padding: 7px 10px 6px 12px`，贴图角，照 ② 的切片标签）→ 52px 高的图注行，右齐衬线中文（｜ 经验，值得新的可能。），下边 1px 发丝；读屏器在图注里读到隐藏的英文词。插画不调色、不加滤镜。

### 期刊卡（Journal Card）

**Role:** 观点与动态
6 + 3 + 3 列错落（第二、三张分别下沉 64 / 128px）。封面衬纸 12–24px 内边距，4:3 裁切；学院主视觉那张用 `mix-blend-mode: multiply` 把烤在图里的米色底融进衬纸。下方：胶囊标签「观点」+ 14px 等宽日期 → 21px/700 标题 → 16px 橄榄深灰摘要。hover 封面放大 1.02。

### 共学五步瓦片（Steps Tiles）

**Role:** 五步真实顺序
12 列、10px 间距的不等宽瓦片：01 占 5 列 × 2 行（墨底、橘橙巨型「01」贴右下），02 占 4、03 占 3、04 占 3、05 占 4；02/05 衬纸底，03/04 透明底 + 发丝边。每块：左上墨色等宽 STEP、右上 76px 墨色 400 细体数字（只有 01 是 700 橘橙巨字）、底部 900 步骤名 + 18px 衬线说明。

### 产品下载行（Product Row）

**Role:** 知君 / 万象
Shopify 章末清单式，放在墨色第三章里：顶部 1px `#bfbeb0` 线，每行下边暗面发丝。左 56px/900 奶油产品名，右上衬线 20px 链接「— 让积累参与思考 ↗」（hover 变橘橙），右下橘橙描边的禁用下载按钮 + 等宽说明。

### 院长寄语对开（Founder Split）

**Role:** 引文块
② 的对开：左 5 份墨底（橘橙 Instrument Serif 大引号、底部 60px/900「嘉木」+ 等宽职衔），右 7 份衬纸底（46px 衬线引文、正文、文字链接）。

### 联系暗场 + 字标页脚（Contact & Footer）

**Role:** 收尾
从纸页用反向撕纸边切回橄榄深墨，底下铺一组淡构图线；全页唯一的居中对称区：等宽眉标 → 92px/900 两行标题 → 19px 说明 → 主 CTA + 描边「复制客服链接」（点击写入剪贴板，状态行读出「已复制」）。页脚三栏 + 满宽 900 字标「半人马AI学院」+ 底行。

### 终幕（HUMAN × AI Finale）

**Role:** 放大终态的一屏
照 ① 的 b-grid 暗场：与钉住层同高的 `.finale`（`aria-hidden`），左上 Instrument Sans 600 超大「HUMAN × AI」，右上 13px 等宽「CENTAUR AI ACADEMY · 2026」，底部左右两角 Noto Serif SC 500「人的意愿」「能力的延伸」，字上方各一根 48×2px 橘橙短横（右侧的短横右齐）。两角文字离底 64px，给返回钮留安全区。中间是与钉住层重合的半人马副本，画框骨架不变。

### 主张大字带（Claim Band）

**Role:** 纸页第一记重音
撕纸边之后、01 章之前，全宽两栏：左 248px 栏放等宽「HUMAN × AI」并画目录同款竖发丝，右栏 Noto Sans SC 900 `clamp(34px, 7vw, 112px)` 两行「人决定方向，/ AI 拓展人的能力。」，第二行 `--color-accent-ink`。没有滑杆，只有一句。

### 返回钮垫底（Back Pad）

**Role:** 让「← 全部方案」在黑场上也找得到
按钮本身的内联样式不动；在它下面放一个固定定位的 `.back-pad`：左 8px、下 8px、94×36px 胶囊、`--color-back-pad` 奶油半透明。按钮字继承纸页墨色，垫底后在黑场、墨色章、奶油纸上都可读。

### Input Field

**Role:** 文本输入（样张备用）
直角，1px 墨线，高 52px，内边距 16px。focus：2px 橘橙环、0 偏移；错误：2px `--color-accent-press` 边；禁用：衬纸底 + 发丝边。

### Tag

**Role:** 类型标记
胶囊，高 28px，1px 墨线，等宽 12px 大写。变体：accent（橘橙实底）、muted（发丝边 + 灰字）。

## Surfaces

| Level | Name        | Value     | Purpose                                   |
| ----- | ----------- | --------- | ----------------------------------------- |
| 0     | void        | `#000000` | 开幕舞台、顶栏                            |
| 1     | paper       | `#f1efe6` | 正文画布                                  |
| 2     | paper-deep  | `#e4e1d4` | 衬纸、瓦片、引文右半                      |
| 3     | ink         | `#25251b` | 第三章整章、第一步瓦片、引文左半          |
| 4     | ink-deep    | `#1b1b13` | 联系区、页脚                              |

层级之间不用阴影，靠硬切：黑 → 奶油用像素撕纸边，奶油 → 深墨用反向撕纸边，纸内的层级只差一个衬纸色；第三章奶油 → 墨色是直接硬切（照 ③ 的白 ↔ 近黑硬切），墨面从目录竖线起铺到右页边，目录栏留在纸上。撕纸边是 24px 高、3–6px 一格的连续随机游走（高度 3–14px，相邻两格最多差 3px），`preserveAspectRatio="none"` 拉伸到任何宽度都连成一条，不会出现孤立的方块。

## Do's and Don'ts

### Do

- 开幕只用纯黑 `#000000`；正文进入后所有暗色都换成带橄榄底调的 `#25251b` / `#1b1b13`。
- 橘橙 `#f07800` 全页累计面积 ≤3%，只放在：顶栏色条、主 CTA、开幕强调词、终幕短横、第三章下载描边、01 大数字、院长引号；纸面上的橘橙大字一律用 `#c25f00`。
- 章节名用 Noto Sans SC 900 喊，叙述用 Noto Serif SC 讲，编号日期用 Geist Mono 记——三个声部不串岗。
- 强调词换声部（衬线 → 900 黑体），不换颜色。例外只有两处：开幕 H1 的「你的能力」和主张带第二行。
- 插画一律进衬纸装裱，带 1px 墨线内框、右下奶油底等宽角标和衬线中文图注。
- 每一个区块都以「1px 墨线 + 等宽标签 + 罗马数字」开头。
- 三章的喊字位置、上下留白、图文排法各不相同。
- 滚动动效只动 transform / opacity，默认样式即终态。
- 黑场里左下 64px 留给返回钮，任何文字不进这块。

### Don't

- 不要让钴蓝进入界面——它属于 logo 和插画。
- 不要给任何面加圆角或阴影；不要出现 4 / 8 / 12px 这种中间圆角。
- 不要用中性灰；所有灰都带同一橄榄色相。
- 不要把中文字距压到 -0.02em 以下，也不要照搬拉丁 0.9 行高。
- 不要把 Geist Mono 放大到 14px 以上，也不要缩到 12px 以下。
- 不要让纸面上出现超过 150px 的纯空纸带。
- 不要给插画加滤镜、双色调或切片——装裱是唯一处理。
- 不要编造数字、学员数、客户、评价、期号；「大数字」只用 01–05、I–VII 与 2026.09.15。
- 不要用紫蓝渐变、渐变文字、玻璃拟态、外发光、emoji、Inter / Roboto / Arial。

## Imagery

两类图，两种处理，各自贯穿全站。**抠图半人马**只出现在黑场里：透明底版站在细白画框中，背后是黄金分割构图线（两个相切大圆 + 两条 30° 对角线 + 两组嵌套黄金矩形），像一幅被量过比例的古典画稿；滚动时画和框一起长大，终幕在框上方压上「HUMAN × AI」。**三张暖色场景插画**只出现在纸页上：不调色，放进衬纸，墨线内框，右下角压奶油底等宽英文角标（② 的招牌手法），下方一行衬线中文图注——这是 Shopify「画作式大留白」在学院素材上的落地，暖插画配橄榄衬纸，色温差被衬纸吸收。期刊卡复用同三张图，学院主视觉（米色底烤在图里）用 multiply 融进衬纸。图形只用内联 SVG：构图线、像素撕纸边。没有图标库，箭头用等宽字符 ↗ ↓ →。

## Layout

页面是三段：56px 黑色书脊顶栏；钉住的黑场舞台（四角 + 中心构图：左上眉标与两行 104px 标题，右上衬线导语与按钮，中心画框与半人马，左下衬线主张，右下等宽 INDEX；放大后换成终幕：左上 HUMAN × AI、右上书眉、底部两角宋体）；奶油纸页正文，以全宽主张大字带开头。正文照 Shopify 做成「左 248px 固定目录 + 右 12 列内容」：目录贴在视口下部，七个条目带点线引到罗马数字；内容区背后有三根贯穿全页的橄榄灰发丝竖线，每个区块顶线处一根横发丝贯穿全宽（Dropbox 的网格延续开幕构图线）。三章节依次是「文窄图宽（4 + 7 列，底对齐）」「图大文窄（8 + 4 列，文字下沉）」「墨色整章：文 + 清单（5 + 6 列）再接 9 列大图」；共学五步是不等宽瓦片；观点三卡 6 + 3 + 3 逐级下沉；院长寄语 5 : 7 对开；收尾是反撕纸边后的居中暗场与满宽字标。1199px 以下目录收起；1023px 以下舞台不再钉住，改为「眉标 → 标题 → 画框 → 导语 → 主张」的静态堆叠，所有栅格落成单列；600px 以下瓦片单列、按钮满宽。

## Agent Prompt Guide

Quick Color Reference:

```
void (opening only): #000000
paper: #f1efe6
paper-deep (mat): #e4e1d4
ink: #25251b
ink-deep: #1b1b13
hair: #d2cfc0
grey-mid: #5e5d51
accent (≤3%): #f07800
on-dark-muted: #bfbeb0
accent-ink (paper, ≥34px only): #c25f00
grid hairline: rgba(94,93,81,.25)
```

Example Component Prompts:

1. Create a chapter opener: 1px `#25251b` rule with a Geist Mono 12px uppercase label on the left ("02 /") and an Instrument Serif roman numeral on the right; below it a single-line shout in Noto Sans SC 900, 148px, line-height 1.02, letter-spacing -0.02em, right-aligned; 88px below, a 12-column row with an 8-column plate (mat `#e4e1d4`, 64px padding, 1px ink inner keyline, mono + serif caption row) and a 4-column text block (Noto Serif SC 700 50px H2 whose emphasis word switches to Noto Sans SC 900, 16px/1.75 `#45443a` body, 44px line pill button). Zero radius on every surface, no shadow.
2. Create the primary CTA: pill, `#f07800` background, `#25251b` 15px/700 text, 48px tall, padding 4px 4px 4px 22px, a 40px `#25251b` circle flush right containing a 17px cream `#f1efe6` "↗". Hover `#d86a00` and nudge the circle `translate(2px,-2px)` with `cubic-bezier(.72,.16,.19,.96)`; active `scale(.97)`.
3. Create the pinned opening: a black stage two screens tall with a sticky inner layer; full-bleed SVG golden-ratio construction lines at `rgba(241,239,230,.17)` and a 380×520 frame at `.42`; a transparent cutout centered, laid out at its final width `min(760px,52vw)` and scroll-scaled from `.46` to `1` via `animation-timeline: scroll(root)` inside `@supports (animation-timeline: view())`; construction SVG scales `1 → 1.28` while fading to `.6`; opening copy fades out; then an absolutely positioned finale layer of the same height rises from below and fades in a 124px Instrument Sans "HUMAN × AI" top-left, a 13px Geist Mono running head top-right, and two Noto Serif SC corner captions with 48×2px orange ticks. Default styles equal the end state.
4. Create the claim band: full width, 248px left rail with a mono label and a hairline, then two lines of Noto Sans SC 900 at `clamp(34px,7vw,112px)`, line-height 1.1, the second line `#c25f00`.

## Similar Brands

逐条对应 BRIEF-v3 的 12 条（本版覆盖 12 条中的 12 条），每条写明出处截图：

- **① 超大紧排标题**（②④）— 开幕 104px、章首 148px，字距 -0.02em、行高 1.02–1.06。出处：`study/shopify-editions-winter26/s03.png`（Sidekick 194px 章名）、`references/ai-in-design-report/fold.png`（120px 标题）。
- **② 三声部分工**（④ + ②）— Noto Sans SC 900 喊 / Noto Serif SC 讲 / Geist Mono 记。出处：`study/shopify-editions-winter26/s04.png`、`s08.png`（花体衬线小节标题 + 粗体标签 + 衬线段落），`study/ai-in-design-report/s06.png`（IN THIS CHAPTER 等宽标签）。
- **③ 零圆角面 + 胶囊按钮 + 零阴影**（②③④）— 出处：`study/ai-in-design-report/s07.png`（直角色块与黑条）、`references/shopify-editions-winter26/fold.png`（白色胶囊 Start for free）。
- **④ 发丝网格即装饰**（③）— 开幕构图线网格 + 正文三根橄榄灰 25% 竖发丝 + 各区块顶线处全宽横发丝（线的浓度照 ③ 的 `#C5DBFF` 在白底上的可见度，色相换成橄榄灰）。出处：`references/dropbox-brand/fold.png`、`study/dropbox-brand/s07.png`、`s08.png`（内页网格线贯穿留白）。
- **⑤ 一个界面强色 + 近黑**（③）— logo 橘橙择一，钴蓝不进界面。出处：`study/dropbox-brand/s01.png`（白 + 一个蓝）。
- **⑥ 带色温的灰阶**（④）— 全部灰带橄榄底调。出处：`study/shopify-editions-winter26/s04.png`–`s12.png`（橄榄奶油纸与 grey-mid 说明字）。
- **⑦ 黑场开幕 → 纸页正文**（④）— 构图线 + 细框 + 标题锁定，放大后收在「HUMAN × AI」终幕，像素撕纸边切入。出处：`references/shopify-editions-winter26/fold.png`（黄金分割构图线）、`study/shopify-editions-winter26/s01.png`（细白框）、`s04.png` / `s12.png`（撕纸边）。
- **⑧ 顶栏书脊**（②）— 黑方块字标 + 满高橘橙色条 CTA + 纯文字导航。出处：`references/ai-in-design-report/fold.png`、`study/ai-in-design-report/mobile.png`（窄屏「Menu +」色条）。
- **⑨ 首页即目录的格子**（③ + ④）— 共学五步不等宽瓦片（左上标题、角落大字形）；左侧固定目录带点线与罗马数字。出处：`study/dropbox-brand/s03.png`（八宫格瓦片）、`study/shopify-editions-winter26/s04.png`（左下固定 I–XII 目录）。
- **⑩ 图像只有一种处理**（④ + ②）— 画作式衬纸装裱 + 右下奶油底等宽角标（② 首屏切片右下角的白底标签，`study/ai-in-design-report/s06.png`、`references/ai-in-design-report/fold.png`）+ 衬线图注，全站三张插画同一手法。出处：`study/shopify-editions-winter26/s07.png`、`s09.png`（画作当卡底、大留白）。
- **⑪ 不对称首屏**（②）— 标题在左、导语在右上、主视觉居中，四角各放一件事。出处：`references/ai-in-design-report/fold.png`（左导语、右大标题）。
- **⑫ 章节标题上下留白每章不同**（④）— 88/64、104/88、88/112px，喊字左/右/左轮换，第三章翻成墨色整章（④ `s14.png` 的深色段 + ③ `study/dropbox-brand/s10.png` 的反相硬切），图文组合不重复。出处：`study/shopify-editions-winter26/PATTERNS.md` 节奏总结与 `s03.png` / `s13.png`（两章章首构图不同）。
- 另借：② 的引文对开（`study/ai-in-design-report/s05.png`）→ 院长寄语；② 的黑底居中订阅 + 满宽字标页脚（`s12.png`、`s13.png`）→ 联系区与页脚；④ 的章末两栏清单（`study/shopify-editions-winter26/s12.png`）→ 知君 / 万象下载行；③ 的错落卡组（`study/dropbox-brand/s10.png`）→ 观点三卡错落；② 的巨字论点句（`study/ai-in-design-report/s02.png`）+ ③ 的大字页（`study/dropbox-brand/s09.png`）→ 撕纸边后的主张大字带；③ 暗面上的「标注语言」与 ② 的黑底收尾 → 终幕的书眉与两角宋体。

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 两色 + 橄榄灰阶 + 唯一强色 */
  --color-void: #000000;
  --color-paper: #f1efe6;
  --color-paper-deep: #e4e1d4;
  --color-ink: #25251b;
  --color-ink-deep: #1b1b13;
  --color-hair: #d2cfc0;
  --color-hair-dark: #3a3a2e;
  --color-grey-mid: #5e5d51;
  --color-grey-dark: #45443a;
  --color-on-dark: #f1efe6;
  --color-on-dark-muted: #bfbeb0;
  --color-accent: #f07800;
  --color-accent-press: #d86a00;
  --color-accent-ink: #c25f00;
  --color-accent-foreground: #25251b;
  --color-logo-blue: #0c6ccc;
  --color-construct: rgba(241, 239, 230, 0.17);
  --color-construct-strong: rgba(241, 239, 230, 0.42);
  --color-construct-paper: rgba(37, 37, 27, 0.07);
  --color-grid: rgba(94, 93, 81, 0.25);
  --color-back-pad: rgba(241, 239, 230, 0.88);
  --color-disabled-bg: #e4e1d4;
  --color-disabled-fg: #5e5d51;
  --color-ring: #25251b;
  --color-ring-dark: #f07800;

  /* Typography — Font Families */
  --font-display:
    'Instrument Sans', 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', system-ui, sans-serif;
  --font-sans:
    'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei',
    system-ui, sans-serif;
  --font-serif:
    'Instrument Serif', 'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-serif-zh: 'Noto Serif SC', 'Songti SC', STSong, SimSun, serif;
  --font-mono:
    'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    monospace;

  /* Typography — Scale */
  --text-label: 13px;
  --text-caption: 15px;
  --text-body-sm: 16px;
  --text-body: 16px;
  --text-lede: 19px;
  --text-narrative: clamp(22px, 1.2vw + 14px, 30px);
  --text-heading: clamp(30px, 2.4vw + 14px, 50px);
  --text-display: clamp(44px, 5.4vw + 8px, 92px);
  --text-shout: clamp(52px, 9.4vw - 8px, 148px);
  --text-wordmark: clamp(64px, 14.6vw, 216px);

  /* Line Height & Tracking — 字越大越紧 */
  --leading-shout: 1.02;
  --leading-display: 1.06;
  --leading-heading: 1.18;
  --leading-narrative: 1.5;
  --leading-body: 1.75;
  --tracking-shout: -0.02em;
  --tracking-display: -0.02em;
  --tracking-heading: -0.01em;
  --tracking-body: 0em;
  --tracking-label: 0.06em;

  /* Spacing (4px base) */
  --spacing: 4px;
  --gutter: 16px;
  --col-gap: 16px;
  --toc-width: 248px;
  --content-max: 1160px;
  --header-h: 56px;
  --back-pad-w: 94px;

  /* Shapes — 面零圆角，控件胶囊 */
  --radius-none: 0px;
  --radius-pill: 999px;
  --hairline: 1px;

  /* Shadows — 不用 */
  --shadow-none: none;

  /* Motion */
  --ease-edition: cubic-bezier(0.72, 0.16, 0.19, 0.96);
  --ease-settle: cubic-bezier(0.41, 0.19, 0.13, 0.95);
  --dur-fast: 0.2s;
  --dur-base: 0.45s;
}
```

### Tailwind v4

```css
@theme {
  --color-void: #000000;
  --color-paper: #f1efe6;
  --color-paper-deep: #e4e1d4;
  --color-ink: #25251b;
  --color-ink-deep: #1b1b13;
  --color-hair: #d2cfc0;
  --color-hair-dark: #3a3a2e;
  --color-grey-mid: #5e5d51;
  --color-grey-dark: #45443a;
  --color-on-dark: #f1efe6;
  --color-on-dark-muted: #bfbeb0;
  --color-accent: #f07800;
  --color-accent-press: #d86a00;
  --color-accent-ink: #c25f00;
  --color-accent-foreground: #25251b;
  --color-logo-blue: #0c6ccc;
  --color-construct: rgba(241, 239, 230, 0.17);
  --color-construct-strong: rgba(241, 239, 230, 0.42);
  --color-construct-paper: rgba(37, 37, 27, 0.07);
  --color-grid: rgba(94, 93, 81, 0.25);
  --color-back-pad: rgba(241, 239, 230, 0.88);

  --font-display: 'Instrument Sans', 'Noto Sans SC', 'PingFang SC', sans-serif;
  --font-sans: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
  --font-serif: 'Instrument Serif', 'Noto Serif SC', 'Songti SC', serif;
  --font-serif-zh: 'Noto Serif SC', 'Songti SC', STSong, serif;
  --font-mono: 'Geist Mono', ui-monospace, Menlo, monospace;

  --text-label: 13px;
  --text-caption: 15px;
  --text-body-sm: 16px;
  --text-body: 16px;
  --text-lede: 19px;
  --text-narrative: clamp(22px, 1.2vw + 14px, 30px);
  --text-heading: clamp(30px, 2.4vw + 14px, 50px);
  --text-display: clamp(44px, 5.4vw + 8px, 92px);
  --text-shout: clamp(52px, 9.4vw - 8px, 148px);
  --text-wordmark: clamp(64px, 14.6vw, 216px);

  --radius-none: 0px;
  --radius-pill: 999px;

  --ease-edition: cubic-bezier(0.72, 0.16, 0.19, 0.96);
  --ease-settle: cubic-bezier(0.41, 0.19, 0.13, 0.95);
}
```

## 新增的结构性文字

以下文字不在 content.md 里，是为刊物版式新增的书眉、标签与控件字：

- 画框标签：`PLATE I`
- 终幕（视觉装饰，`aria-hidden`）：`HUMAN × AI`、`人的意愿`、`能力的延伸`（三者取自文案稿主视觉图注，拆开重排）、`CENTAUR AI ACADEMY · 2026`
- 主张大字带：`人决定方向，` / `AI 拓展人的能力。`（文案稿 Hero 底栏原句，在纸页开头重复一次放大），左栏标签 `HUMAN × AI`（取自图注）
- 插画角标：`EXPERIENCE`、`LEARN TOGETHER`、`MAKE IT REAL`（文案稿图注的英文部分移到图角；图注行保留中文，并为读屏器保留隐藏的英文词）
- 开幕右下锚点：`INDEX ↓`
- 目录标题：`目录 / INDEX`
- 目录条目：`从你的积累出发 I`、`与同行者一起 II`、`让想法落地 III`、`共学五步 IV`、`观点与动态 V`、`院长寄语 VI`、`从这里开始 VII`（条目文字取自文案稿的章节名与区块名，罗马数字为新增）
- 目录落款与页脚底行：`CENTAUR AI ACADEMY · 2026`
- 分区头：`01 /`、`02 /`、`03 /`、`01 — 05`，以及右端罗马数字 `I`–`VI`
- 步骤瓦片：`STEP`、大数字 `01`–`05`（数字来自文案稿，作为装饰字形重复出现）
- 院长寄语分区头：`FROM THE FOUNDER`（沿用文案眉标，移到分区头）
- 屏幕阅读器标题：`院长寄语`（视觉隐藏）
- 移动端菜单按钮：`菜单 +`
- 跳转链接：`跳到正文`
- 复制按钮反馈：`已复制`
- 组件样张页（kit.html）的说明文字与区块名：`组件样张 · C / EDITION`、`刊本：黑场开幕，纸页正文。`、`色板`、`三声部`、`胶囊按钮 · 全状态`、`画作式装裱 · 构图线 · 撕纸边`、`期刊卡 · 徽标`、`共学五步瓦片`、`引文对开 · 产品下载行`、`01 / COLOR` 等分区头、输入框示例 `你的问题` / `聊聊你正在做的事` / `暂未开放`，色板新增项 `橘橙 · 纸上字` / `纸面大字强调 3.7:1` / `网格发丝` / `贯穿竖线与横线` / `黑场上的小字 11:1`，以及注释 `第三章墨色整章里，禁用下载按钮改为橘橙描边。`、`主张大字带：第二行用纸面橘橙字 --color-accent-ink。`
