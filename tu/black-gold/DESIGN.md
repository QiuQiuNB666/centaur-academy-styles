# 半人马AI学院 · 黑金发布会 — Style Reference

> 一束光打在台上，金线勾出分量

**Theme:** dark

黑金发布会把首页做成一场国内大厂年度发布会：近黑舞台底（#0b0a08）上大量留黑，标题用思源宋 900 写得又大又正，关键词用鎏金渐变（--metal-gold）描出来，细线、画框、奖章全是香槟金 #d6b46e。颜色只有黑、金、白三类——logo 自带的橙蓝只留在 logo 和半人马插画里，不外溢到任何按钮、线条、背景。「土」来自黑金配色、居中对称、粗宋大字、回纹和题字；「炫」来自三样东西：舞台光束、脚下金色光环、滚动时半人马从 0.58 放大到 1 并被一道金色扫光掠过。金色是「只写大字的颜色」：正文、说明、日期一律象牙白系（对比度 9.2–17.3:1），金色文字一律不小于 28px（小号罗马字标签、分隔符都用象牙白系，金色只留给线和大字）。首屏最上方是一行 28px 鎏金 Cinzel「CENTAUR AI ACADEMY」，像刻在门楣上的院名。签名记忆点是**半人马登场**：一束顶光从标题下方直打到台上，半人马在光里从小放大，脚下光环脉动，一道金色扫光从左到右穿过身体，像主角走上发布会舞台。

## Tokens — Colors

| Name | Value | Token | Role |
| ---- | ----- | ----- | ---- |
| 舞台黑 | `#0b0a08` | `--color-stage` | 页面底色，带一点暖的近黑，不用纯黑 |
| 展台黑 | `#14120e` | `--color-stage-raise` | 时间轴区底、画框衬底、卡片封面衬底 |
| 抬升黑 | `#1b1813` | `--color-stage-lift` | 预留给弹层，全页目前未用 |
| 暗线 | `#2c271e` | `--color-hairline` | 分区线、禁用按钮描边、顶栏底线 |
| 象牙白 | `#f5efe2` | `--color-ivory` | 标题与正文，舞台黑上 17.3:1 |
| 次要白 | `#cfc6b4` | `--color-ivory-soft` | 说明、图注、署名，11.7:1 |
| 弱白 | `#b9b09e` | `--color-ivory-dim` | 日期、禁用文字、「下载暂未开放」，9.2:1 |
| 香槟金 | `#d6b46e` | `--color-gold` | 细线、画框角花、≥28px 标题、链接下划线；作文字时 10:1 |
| 高光金 | `#f3e3b8` | `--color-gold-hi` | 渐变高光、焦点环、时间轴流光 |
| 中金 | `#c9a562` | `--color-gold-mid` | 渐变最暗处的下限（保证金底黑字 ≥ 7.9:1） |
| 暗金 | `#8f6a2f` | `--color-gold-lo` | 光环与时间轴渐变暗端，只做装饰，不放字 |
| 金上墨 | `#1a1206` | `--color-gold-ink` | 金色按钮、奖章上的字 |

### 光效与金属（只做装饰，不承载文字）

| Name | Value | Token |
| ---- | ----- | ----- |
| 金色光晕 | `rgba(214,180,110,.38)` | `--glow-gold` |
| 柔光 | `rgba(214,180,110,.13)` | `--glow-soft` |
| 微光 | `rgba(214,180,110,.06)` | `--glow-faint` |
| 光束 | `rgba(243,227,184,.34)` | `--glow-beam` |
| 扫光 | `rgba(255,246,220,.9)` | `--glow-flash` |
| 金细线 | `rgba(214,180,110,.55)` / `.22` | `--line-gold` / `--line-gold-faint` |
| 网格线 | `rgba(214,180,110,.07)` | `--grid-line` |
| 顶栏幕布 | `rgba(11,10,8,.82)` | `--veil` |
| 鎏金渐变 | 100deg，中金→高光金→香槟金 往返两次 | `--metal-gold` |
| 金线渐变 | 两端透明、中间高光 | `--metal-line` |

## Tokens — Typography

### 思源宋体 Noto Serif SC — 标题 · `--font-title`

- **Substitute:** Songti SC, STSong, SimSun；正式上线可换自托管的「站酷小薇」做章节大标题，或方正/汉仪粗宋（需授权）
- **Weights:** 700（副标题、口号）、900（所有 h1–h3）
- **Sizes:** 21–26（lead）、26–32（h3）、36–60（h2）、40–72（章节）、48–104（display）
- **Line height:** 1.18，字距 0.02em
- **Role:** 「正、粗、有分量」的主角；关键词套鎏金渐变

### 思源黑体 Noto Sans SC — 正文 / 按钮 · `--font-body`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei；正式上线可换阿里巴巴普惠体
- **Weights:** 400、500、700（按钮）
- **Sizes:** 16（次要）、18→20（正文）、18（按钮）
- **Line height:** 1.8
- **Role:** 所有正文、说明、按钮、导航，一律象牙白系，不用金色

### Cinzel — 碑刻罗马字 · `--font-roman`

- **Substitute:** Trajan Pro, Times New Roman
- **Weights:** 700
- **Sizes:** 28（首屏鎏金院名，手机字距 0、≥768px 字距 0.16em）、13（标签，字距 0.2em，全大写，象牙白）、22（奖章数字）、64–80（章节描边编号）
- **Role:** CENTAUR AI ACADEMY、图注英文、01–05 编号；13px 标签只做装饰、不用金色，旁边总有中文承载信息

### 马善政楷书 Ma Shan Zheng — 题字 · `--font-brush`

- **Substitute:** STKaiti, KaiTi, Kaiti SC
- **Weights:** 400
- **Sizes:** 44–72
- **Role:** 全站只用两处：院长署名「嘉木」、页脚口号「各有知君，共创万象。」；用 Google Fonts `text=` 参数只取这 11 个字，几 KB

同屏中文字体最多三种：宋（标题）+ 黑（正文）+ 楷（题字）。

### Type Scale

| Role | Size | Line Height | Letter Spacing | Token |
| ---- | ---- | ----------- | -------------- | ----- |
| display | 48→104px | 1.18 | 0.02em | `--text-display` |
| chapter | 40→72px | 1.18 | 0.02em | `--text-chapter` |
| h2 | 36→60px | 1.18 | 0.02em | `--text-h2` |
| brush | 44→72px | 1.1–1.3 | 0.06em | `--text-brush` |
| h3 | 26→32px | 1.3 | 0.06em | `--text-h3` |
| gold-min | 28px | — | 0.08em | `--text-gold-min` |
| card | 22→28px | 1.4 | 0 | `--text-card` |
| lead | 21→26px | 1.55–1.7 | 0 | `--text-lead` |
| body | 18→20px | 1.8 | 0 | `--text-body` |
| note | 16px | 1.7 | 0.06em | `--text-note` |
| inscription | 28px | 1.3 | 0 → 0.16em | `--text-gold-min` |
| label | 13px | 1.15 | 0.2em | `--text-label` |

## Tokens — Spacing & Shapes

**Base unit:** 4px

**Density:** 宽松——发布会讲究留黑，一屏只讲一件事

### Spacing Scale

| Name | Value | Token |
| ---- | ----- | ----- |
| 1 | 4px | `--space-1` |
| 2 | 8px | `--space-2` |
| 3 | 12px | `--space-3` |
| 4 | 16px | `--space-4` |
| 6 | 24px | `--space-6` |
| 8 | 32px | `--space-8` |
| 12 | 48px | `--space-12` |
| 16 | 64px | `--space-16` |
| 24 | 96px | `--space-24` |
| 32 | 128px | `--space-32` |
| gutter | 16→48px | `--gutter` |

### Border Radius

| Name | Value | Token |
| ---- | ----- | ----- |
| none | 0 | `--radius-none` |
| sm | 2px | `--radius-sm` |
| pill | 999px | `--radius-pill` |

| Element | Value |
| ------- | ----- |
| 画框 / 颁词框 / 邀请函 | 0（直角，像展柜和证书） |
| 按钮 / 徽标 / 菜单钮 | pill |
| 输入框 | 2px |
| 奖章 | 50% |

### Shadows

黑底上不用投影，只用光。

| Name | Value | Token |
| ---- | ----- | ----- |
| glow | `0 0 32px rgba(214,180,110,.28)` | `--shadow-glow` |
| glow-strong | `0 0 48px rgba(214,180,110,.45), 0 0 4px rgba(243,227,184,.6)` | `--shadow-glow-strong` |
| inset-frame | `inset 0 0 0 1px rgba(214,180,110,.22)` | `--shadow-inset-frame` |

### Motion

| Name | Value | Token |
| ---- | ----- | ----- |
| ease-stage | `cubic-bezier(0.22, 1, 0.36, 1)` | `--ease-stage` |
| press | 160ms | `--dur-press` |
| hover | 240ms | `--dur-hover` |
| shimmer | 7s（往返） | `--dur-shimmer` |
| zoom-from | 0.58 | `--zoom-from` |

- **登场（签名动效）：** `.stage` 外层做 `view-timeline`（inset = 顶栏高 + 16px），区间 `exit-crossing -lead` → `exit-crossing +extra`；画框钉住 extra 距离。手机 lead = min(36svh,300px)、extra = min(6svh,48px)（让主按钮留在 390×844 首屏且不碰左下角返回钮）；桌面 lead = min(30svh,270px)、extra = min(18svh,160px)。钉住段 ≤ 160px，远低于 90svh。
- **同步的三件事：** 半人马 scale 0.58→1（手机/平板以脚底为原点 `50% 100%`，站在光环上长高；桌面 `50% 72%`）；光束 opacity .55→1、scaleX .6→1（光束挂在不缩放的 figure 上，登场前就从标题下方一路照到台上，填满留黑）；扫光在 35%–100% 从左穿到右，峰值 opacity .8，高亮副本 `sepia + saturate + mix-blend-mode:screen`，读作金光而非银白（遮罩带 translateX，里面的高亮副本反向 translateX，所以只亮在身体上）。图注始终是完整对比度，不参与动画。
- **兜底：** 不支持 `animation-timeline` 时（安卓微信、iOS 26 以下）JS 接管：IntersectionObserver 只在舞台附近 ±300px 挂 passive scroll，rAF 里只写 transform / opacity，公式与 CSS 同一区间；尺寸只在 resize 时量。`?nosd` 强制走兜底。`prefers-reduced-motion: reduce` 时一切静止在终态（scale 1）。
- **常驻微动：** 标题「你的能力」鎏金 7s 往返流动（background-position，只此一处非 transform 动画，面积小）；光环内圈 3.6s 呼吸；时间轴上一粒流光 5.5s 走一遍。reduced-motion 下全部关闭。

### Layout

- **Section gap:** 手机 88–96px，桌面 120–136px
- **Max content width:** 1240px；首屏三栏放宽到 1520px
- **断点:** 1100px 以上三栏首屏、章节左右分栏、横向时间轴；768px 以上期刊两列、邀请函按钮并排
- **视口高度:** 章节 `min-height:min(900px,100svh)`，所有 svh 都有 px 上限

## Components

### 鎏金主按钮

**Role:** 唯一主 CTA「联系学院顾问 ↗」
`background: var(--metal-gold)`，字 `--color-gold-ink` 18px/700，高 56px（顶栏里 52px），pill，`--shadow-glow`。hover：一道高光从左扫到右（伪元素 translateX，0.9s）+ `--shadow-glow-strong`；active：scale(.97)；focus-visible：3px 高光金外环。金底最暗处 #c9a562 上黑字 7.98:1。

### 金线次按钮

**Role:** 「复制客服链接」等并列动作
透明底 + `inset 0 0 0 1px var(--color-gold)`，象牙白字，hover 铺 `--glow-soft`。

### 禁用下载按钮

**Role:** 「下载知君 ↓」「下载万象 ↓」
`disabled` + 暗线描边 + 弱白字（9.2:1，仍然看得清），右侧/下方跟一行 16px「下载暂未开放」，用 `aria-describedby` 关联。

### 文字链接

**Role:** 「了解学院的主张 ↗」等
象牙白 18–20px/500，金色 1px 下划线，offset 7px，最小高 44px；hover 下划线变 2px 高光金。链接文字不用金色。

### 发布会舞台（签名组件）

**Role:** 首屏半人马登场
四层叠放：锥形光束（conic-gradient + 纵向渐隐遮罩，挂在 figure 上不随缩放）→ 地面光晕（径向）→ 三圈 SVG 金色椭圆光环（实线/粗线呼吸/点线）→ 透明底半人马 → 扫光层。终态宽度手机 ≤ 358px、平板 ≤ 704px、桌面 ≤ 660px（均低于 480/720 的分辨率天花板）。图注「HUMAN × AI ｜ 人的意愿 · 能力的延伸」居中一行，英文象牙白。

### 展柜画框

**Role:** 三章插画
1px 金细线外框 + 3px 内缩的淡金内框 + 8px 展台黑衬边 + 四角 22px 金色 L 形角花（外扩 6px），下方居中图注：13px Cinzel 象牙白英文 +「｜」+ 16px 次要白中文；560px 以下英文与中文上下两行、隐去「｜」，避免竖线孤零零落到行首。暖色插画在黑底上像被灯照亮的展品，不做滤镜。

### 章节页（Keynote 页）

**Role:** 三个叙事章节
描边 Cinzel 大编号「01」+「/」+ 章节名 → 思源宋 900 两行大标题（强调词鎏金）→ lead 说明 → 链接。手机居中；桌面文案 5 : 画框 6 左右分栏，第二章左右对调。

### 产品铭牌行

**Role:** 知君 / 万象
上下金细线夹住的一行：「知君」28px 鎏金宋体 +「— 让积累参与思考 ↗」；右侧禁用下载按钮与说明。

### 金色时间轴

**Role:** 共学五步
64px 鎏金奖章（Cinzel 数字，外加 6px 黑环 + 1px 金环）串在 2px 金线上。手机竖排（奖章左、标题与说明右），桌面横排五等分。线上一粒高光流光循环走过。

### 期刊卡

**Role:** 观点与动态
封面放进 6px 衬边的金细线框，16px 弱白元信息，22–28px 宋体标题，18px 次要白摘要。桌面：首篇占左列两行，另两篇为「168px 方图 + 文字」横卡。

### 颁词框

**Role:** 院长寄语
双线金框（外 1px、内缩 6px 淡金），居中：FROM THE FOUNDER → 金线 → 27–46px 宋体 900 引文 → 正文 → 楷书金字「嘉木」→ 两行职务 → 链接。只借颁奖词的版式，不出现任何奖项字样。

### 邀请函

**Role:** 联系区
舞台黑卡片 + 1px 香槟金框 + 8px 黑间隔 + 淡金外框（box-shadow 叠出双边），四角 40px 回纹 SVG，背后一团金色光晕。标题整句鎏金，主次按钮居中。

### 输入框

**Role:** 预留（咨询表单）
高 56px，展台黑底，1px 金细线，2px 圆角；focus-visible 边框变高光金 + `--shadow-glow`。

### 徽标

**Role:** 分类 / 状态
36px 高 pill：实心鎏金（主分类）、金细线（普通）、暗线弱白（不可用）。

## Surfaces

| Level | Name | Value | Purpose |
| ----- | ---- | ----- | ------- |
| 0 | stage | `#0b0a08` | 页面底、首屏、章节、期刊、邀请函卡面 |
| 1 | stage-raise | `#14120e` | 共学五步整段、画框衬边、封面衬边、输入框 |
| 2 | stage-lift | `#1b1813` | 预留：弹层 |
| 光 | glow-* | rgba 金 | 首屏径向光、章节顶光、邀请函背光——层次靠光，不靠投影 |

## Do's and Don'ts

### Do

- 金色只写 ≥28px 的标题和关键词；正文、说明、日期、链接一律象牙白系。
- 每一屏只讲一个观点：一个大标题 + 一句说明 + 一个动作，四周留黑。
- 标题居中、对称、够大：手机 display 48px，章节标题 40px 起。
- 画框、颁词框、邀请函一律直角；只有按钮和徽标是胶囊。
- 光效集中在首屏舞台：光束、光环、扫光各一次，别处只有微光。
- 主按钮文字写全「联系学院顾问 ↗」，高度 ≥52px。
- 题字全站只用两处，且用 `text=` 子集加载。

### Don't

- 不要红底放射光、斜体描边大「2026」、行书斜标题——那是年会 PPT 模板的味道（鸿鹄开年盛典反例）。
- 不要彩虹光纤、蓝紫渐变——那是 WAIC / 百度世界的浅色 AI 大会语言，和黑金冲突。
- 不要把 logo 的橙蓝拿去做按钮、线条、背景色。
- 不要编造数字、客户 logo、学员评价、奖杯奖牌、「重磅」「限时」「震撼」类标签。
- 不要在复杂纹理上压字：网格只铺在首屏，且透明度 7%、径向渐隐。
- 不要出现 28px 以下的金色字：13px Cinzel 标签、「——」「/」「·」分隔符都用象牙白系。
- 标题里的弯引号用窄西文字形（`Quote Narrow` 只覆盖 U+2018–201D），否则粗宋全角引号会在「从“我想”，」里撑出大空。
- 不要堆浮标：页面只有左下角一个返回钮。

## Imagery

主视觉只有一个物件——透明底半人马，放在舞台光束下、金色光环上，靠滚动登场（借华为全联接大会「一个 3D 物件当主视觉」的思路，但换成黑场）。三张暖色纸感插画不改色，统一装进金细线展柜框里，黑底把它们衬成「被灯照亮的展品」。期刊封面用同一批插画加 6px 衬边细框。图标全部用文字符号（↗ ↓ →）和内联 SVG（光环、回纹），不用图标库、不用 emoji。

## Layout

手机优先：390 宽下全部单列居中，首屏顺序为 鎏金院名 + 眉标 → H1 → 副标题 → 舞台 → 主按钮 → 文字链接 → 说明 → 口号，保证首屏能同时看到大标题、半人马和主按钮。桌面首屏三栏：左栏副标题 + 说明，中栏 660px 舞台，右栏主按钮；三章为左右分栏的 Keynote 页，每章 min(900px,100svh)；五步横排；期刊一大两小；颁词与邀请函居中窄栏（960 / 880px）。

## Agent Prompt Guide

Quick Color Reference:

```
stage: #0b0a08
stage-raise: #14120e
hairline: #2c271e
ivory (text): #f5efe2
ivory-soft (secondary): #cfc6b4
ivory-dim (meta/disabled): #b9b09e
gold (lines, >=28px titles): #d6b46e
gold-hi (highlight/focus): #f3e3b8
gold-ink (text on gold): #1a1206
```

Example Component Prompts:

1. Create the primary CTA: pill button 56px high, `background: var(--metal-gold)`, text `var(--color-gold-ink)` 18px/700「联系学院顾问 ↗」, `box-shadow: var(--shadow-glow)`; on hover a white-gold light band (`--glow-flash`) sweeps left→right via a pseudo-element translateX, shadow becomes `--shadow-glow-strong`; active scale(.97).
2. Create a vitrine frame for an illustration: 1px `--line-gold` border, 8px `--color-stage-raise` padding, inner 1px `--line-gold-faint` border inset 3px, four 22px gold L-corners offset 6px outside; caption centered below: 13px Cinzel uppercase ivory English + 「｜」 + 16px `--color-ivory-soft` Chinese.
3. Create the gold timeline: 64px round medals filled with `--metal-gold`, Cinzel 22px numerals in `--color-gold-ink`, ring `0 0 0 6px stage, 0 0 0 7px --line-gold`; connected by a 2px gold gradient line; step titles Noto Serif SC 900 26–32px ivory, descriptions 18–20px ivory-soft.

## Similar Brands

- **华为全联接大会 2026** — 借「一个物件当主视觉」和「智 启 新 未 来」式字距拉开的正气标题；嘉宾墙那种「照片 + 头衔」的郑重感转成了颁词框。
- **火山引擎 FORCE 2022** — 国内唯一见到的深色发布会页：借了斜向体积光束和「大会亮点 HIGHLIGHTS」式中英双语标签；避开了它暗图压暗字、播放器转圈的坑。
- **胡润百富** — 借黑底 + 金色选中块（#DDA159）这种最克制的黑金用法；金色只做一块，不铺满。
- **福布斯中国** — 借衬线标题居中 + 细小作者行的杂志感，和「金色只用在一个模块」的纪律（订阅块 #C9A227）。
- **中欧国际工商学院** — 借金色细线金字塔与「中 国 深 度」宽字距；手机端课程卡的金色标题栏启发了产品铭牌行的金线。
- **云栖大会 2026** — 借居中对称、像牌匾一样的品牌名排法，和「一张质感大图、不叠多余装饰」的克制。
- **反例：鸿鹄中国 2025 开年盛典** — 红底放射光、斜体描边年份、「圆满成功！」横幅——本范式的「土」必须停在它之前。

## 新增的结构性文字

以下文字不在 content.md 中，仅作导航与状态提示，不含任何事实性说法：

- 「菜单」「关闭」（手机顶栏菜单按钮）
- 「跳到正文」（键盘跳转链接）
- 「已复制」（复制客服链接后的状态提示）
- kit.html 内的说明文字（色板角色、字号标注、状态名、「例：每周的销售复盘」占位、红线清单），只出现在组件样张，不进入首页

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 黑 */
  --color-stage: #0b0a08;
  --color-stage-raise: #14120e;
  --color-stage-lift: #1b1813;
  --color-hairline: #2c271e;

  /* Colors — 白 */
  --color-ivory: #f5efe2;
  --color-ivory-soft: #cfc6b4;
  --color-ivory-dim: #b9b09e;

  /* Colors — 金 */
  --color-gold: #d6b46e;
  --color-gold-hi: #f3e3b8;
  --color-gold-mid: #c9a562;
  --color-gold-lo: #8f6a2f;
  --color-gold-ink: #1a1206;

  /* Light — 光效（只做装饰，不承载文字） */
  --glow-gold: rgba(214, 180, 110, 0.38);
  --glow-soft: rgba(214, 180, 110, 0.13);
  --glow-faint: rgba(214, 180, 110, 0.06);
  --glow-beam: rgba(243, 227, 184, 0.34);
  --glow-flash: rgba(255, 246, 220, 0.9);
  --line-gold: rgba(214, 180, 110, 0.55);
  --line-gold-faint: rgba(214, 180, 110, 0.22);
  --grid-line: rgba(214, 180, 110, 0.07);
  --veil: rgba(11, 10, 8, 0.82);

  /* Metal — 鎏金渐变 */
  --metal-gold: linear-gradient(100deg, #c9a562 0%, #e2c587 22%, #f3e3b8 38%, #d6b46e 52%, #c9a562 70%, #f3e3b8 86%, #d6b46e 100%);
  --metal-line: linear-gradient(90deg, rgba(214, 180, 110, 0) 0%, #d6b46e 30%, #f3e3b8 50%, #d6b46e 70%, rgba(214, 180, 110, 0) 100%);

  /* Typography — Font Families */
  --font-title: 'Noto Serif SC', 'Songti SC', 'STSong', 'SimSun', serif;
  --font-body: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-roman: 'Cinzel', 'Trajan Pro', 'Times New Roman', 'Songti SC', serif;
  --font-brush: 'Ma Shan Zheng', 'STKaiti', 'KaiTi', 'Kaiti SC', serif;

  /* Typography — Scale（手机 → 桌面） */
  --text-label: 13px;
  --text-note: 16px;
  --text-body: clamp(18px, 0.4vw + 16px, 20px);
  --text-lead: clamp(21px, 0.9vw + 17px, 26px);
  --text-card: clamp(22px, 0.8vw + 18px, 28px);
  --text-gold-min: 28px;
  --text-h3: clamp(26px, 1vw + 22px, 32px);
  --text-h2: clamp(36px, 3.4vw + 22px, 60px);
  --text-chapter: clamp(40px, 4.2vw + 22px, 72px);
  --text-display: clamp(48px, 6.4vw + 20px, 104px);
  --text-brush: clamp(44px, 3vw + 30px, 72px);

  /* Line Height & Tracking */
  --leading-title: 1.18;
  --leading-body: 1.8;
  --tracking-title: 0.02em;
  --tracking-roman: 0.2em;

  /* Spacing (4px base) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;
  --space-32: 128px;
  --gutter: clamp(16px, 3.4vw, 48px);
  --wrap: 1240px;

  /* Shapes — 直角为主，只有胶囊按钮是圆的 */
  --radius-none: 0px;
  --radius-sm: 2px;
  --radius-pill: 999px;
  --hairline: 1px;
  --frame-gap: 8px;

  /* Shadows — 黑底上只用光，不用投影 */
  --shadow-glow: 0 0 32px rgba(214, 180, 110, 0.28);
  --shadow-glow-strong: 0 0 48px rgba(214, 180, 110, 0.45), 0 0 4px rgba(243, 227, 184, 0.6);
  --shadow-inset-frame: inset 0 0 0 1px rgba(214, 180, 110, 0.22);

  /* Controls */
  --btn-h: 56px;
  --btn-h-min: 52px;
  --touch-min: 44px;
  --header-h: 64px;

  /* Motion */
  --ease-stage: cubic-bezier(0.22, 1, 0.36, 1);
  --dur-press: 160ms;
  --dur-hover: 240ms;
  --dur-shimmer: 7s;
  --zoom-from: 0.58;
}
```

### Tailwind v4

```css
@theme {
  --color-stage: #0b0a08;
  --color-stage-raise: #14120e;
  --color-stage-lift: #1b1813;
  --color-hairline: #2c271e;
  --color-ivory: #f5efe2;
  --color-ivory-soft: #cfc6b4;
  --color-ivory-dim: #b9b09e;
  --color-gold: #d6b46e;
  --color-gold-hi: #f3e3b8;
  --color-gold-mid: #c9a562;
  --color-gold-lo: #8f6a2f;
  --color-gold-ink: #1a1206;
  --font-title: 'Noto Serif SC', 'Songti SC', 'STSong', 'SimSun', serif;
  --font-body: 'Noto Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --font-roman: 'Cinzel', 'Trajan Pro', 'Times New Roman', 'Songti SC', serif;
  --font-brush: 'Ma Shan Zheng', 'STKaiti', 'KaiTi', 'Kaiti SC', serif;
  --text-label: 13px;
  --text-note: 16px;
  --text-body: clamp(18px, 0.4vw + 16px, 20px);
  --text-lead: clamp(21px, 0.9vw + 17px, 26px);
  --text-card: clamp(22px, 0.8vw + 18px, 28px);
  --text-gold-min: 28px;
  --text-h3: clamp(26px, 1vw + 22px, 32px);
  --text-h2: clamp(36px, 3.4vw + 22px, 60px);
  --text-chapter: clamp(40px, 4.2vw + 22px, 72px);
  --text-display: clamp(48px, 6.4vw + 20px, 104px);
  --text-brush: clamp(44px, 3vw + 30px, 72px);
  --radius-none: 0px;
  --radius-sm: 2px;
  --radius-pill: 999px;
  --shadow-glow: 0 0 32px rgba(214, 180, 110, 0.28);
  --shadow-glow-strong: 0 0 48px rgba(214, 180, 110, 0.45), 0 0 4px rgba(243, 227, 184, 0.6);
  --shadow-inset-frame: inset 0 0 0 1px rgba(214, 180, 110, 0.22);
  --ease-stage: cubic-bezier(0.22, 1, 0.36, 1);
}
```
