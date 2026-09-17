# 半人马AI学院 · 中国红大会 — Style Reference

> 红铺底、金点睛、米白托正文：像一场办得体面的企业家年会

**Theme:** light（红金主视觉 + 米白阅读区）

「中国红大会」把官网当成一场企业家年会来布置：开幕是一整块朱砂红舞台（#a30f17 → #6e0910 径向渐变），中心一枚米白奖章托起半人马，12 道细金光芒只占 0.8° 宽、透明度 30%，比年会 PPT 的放射光克制得多。标题用粗宋 900 撑住分量，整页只有「你的能力。」一处用马善政毛笔题字并做金箔渐变，右上角压一方「半人马AI学院」朱文方印。金色是细线资源：边框 1px、回纹 10px 高、牌匾外框 1px，题字、牌匾字和主按钮之外不出现大块金。正文区一律回到宣纸米白 #fbf5ea，墨色正文 #2a1a14 对比 15.4:1，次要字 #5a4638 也有 8.17:1，适合 50 多岁的老板在微信里看。版式居中对称：共学五步做成典礼流程单，院长寄语做成上下带轴头的题词卷轴，联系区像报名台（红底上一张米白台面、顶边一条金）。签名记忆点是**奖章登场**：滚动时米白奖章从 0.5 放到 1，金色光芒同时展开并回正 24°，一道斜向扫光（overlay 混合，在金边和半人马上显出金属反光）掠过奖章，最后亮出托在绛红名牌条上的「HUMAN × AI」图注。

## Tokens — Colors

| Name       | Value     | Token                   | Role                                               |
| ---------- | --------- | ----------------------- | -------------------------------------------------- |
| 朱砂红     | `#a30f17` | `--color-red`           | 大面积铺底（开幕、共学五步、联系区）、主按钮、编号 |
| 绛红       | `#6e0910` | `--color-red-deep`      | 页眉、页脚、牌匾底、对联底、奖章外圈               |
| 光心红     | `#d0231f` | `--color-red-glow`      | 只做径向光晕的中心，不做文字和按钮                 |
| 印泥红     | `#5e070c` | `--color-red-ink`       | 金按钮上的文字（8.23:1）、题字投影                 |
| 赤金       | `#e9c274` | `--color-gold`          | 1px 细线、边框、回纹、题字的回退色                 |
| 淡金       | `#fbe9b7` | `--color-gold-light`    | 金箔渐变高光、红底上的焦点环                       |
| 中金       | `#d6a553` | `--color-gold-mid`      | 金箔渐变暗部、卷轴轴头                             |
| 古铜金     | `#b8863b` | `--color-gold-deep`     | 米白底上的点线、编号外环、输入框边                 |
| 宣纸米白   | `#fbf5ea` | `--color-ivory`         | 正文区底色、流程单、报名台                         |
| 纯白       | `#ffffff` | `--color-paper`         | 卡片、画框衬纸、卷轴纸面                           |
| 红底前景   | `#fff3e0` | `--color-cream`         | 红底上的正文（对 #a30f17 为 7.26:1）               |
| 红底次要   | `#f0cdb5` | `--color-cream-muted`   | 绛红底上的次要文字（8.25:1）                       |
| 墨         | `#2a1a14` | `--color-ink`           | 正文、标题（对米白 15.4:1）                        |
| 淡墨       | `#5a4638` | `--color-ink-muted`     | 次要文字（对米白 8.17:1）                          |
| 金米线     | `#e6d3ae` | `--color-line`          | 分割线、卡片边                                     |
| 禁用底     | `#efe6d6` | `--color-disabled-bg`   | 禁用按钮底                                         |
| 禁用字     | `#4a3a2e` | `--color-disabled-text` | 禁用按钮字（8.76:1）                               |

### 光效与渐变（只做装饰层，不压正文）

| Name     | Value                                              | Token           |
| -------- | -------------------------------------------------- | --------------- |
| 金箔     | `linear-gradient(180deg,#fbe9b7,#e9c274 46%,#d6a553 58%,#f6dc9f)` | `--grad-gold`   |
| 按钮金   | `linear-gradient(180deg,#fbe9b7,#e9c274 50%,#dfb566 62%,#f6dc9f)` | `--grad-gold-btn` |
| 舞台红   | `radial-gradient(ellipse 70% 55% at 50% 72%,#d0231f,#a30f17 55%,#6e0910)` | `--grad-stage`  |
| 奖章面   | `radial-gradient(circle at 50% 38%,#fff,#fbf5ea 48%,#f3e2bf)` | `--grad-medal`  |
| 网格线   | `rgba(233,194,116,.06)`                            | `--gold-a06`    |
| 光芒     | `rgba(233,194,116,.30)`                            | `--gold-a30`    |
| 外框金   | `rgba(233,194,116,.55)`                            | `--gold-a55`    |
| 扫光     | `rgba(255,250,235,.60)`                            | `--shine-a60`   |

## Tokens — Typography

### 马善政毛笔楷书 Ma Shan Zheng — 主题题字 · `--font-brush`

- **Substitute:** STKaiti, KaiTi, Kaiti SC（Google Fonts 只按 `text=` 子集加载 5 个字）
- **Weights:** 400
- **Sizes:** clamp(58px, 16vw, 132px)
- **Role:** 全站只用于 H1 的「你的能力。」一处，填金箔渐变 + 3px 印泥红投影；不用于任何长句

### 思源宋体 Noto Serif SC — 标题粗宋 · `--font-title`

- **Substitute:** Songti SC, STSong, SimSun；正式上线可换自托管的站酷小薇或方正粗宋（需授权）
- **Weights:** 700, 900
- **Sizes:** 20, 24, 28, clamp(32–56), clamp(42–84)
- **Line height:** 1.15–1.3
- **Role:** H1 首行、H2、卡片标题、牌匾、对联、印章、题词引文、页脚口号

### 思源黑体 Noto Sans SC — 正文 · `--font-body`

- **Substitute:** PingFang SC, Hiragino Sans GB, Microsoft YaHei；正式上线可换阿里巴巴普惠体（免费商用，自托管）
- **Weights:** 400, 500, 700
- **Sizes:** 16, 18, 20
- **Line height:** 1.75
- **Role:** 正文、导语、按钮、导航、日期

### Cinzel — 碑刻罗马字 · `--font-latin`

- **Substitute:** Trajan Pro, Times New Roman
- **Weights:** 500, 700
- **Sizes:** 13–15px，字距 .18em；编号 24px
- **Role:** CENTAUR AI ACADEMY、HUMAN × AI、图注英文、流程编号 01–05；不承载关键信息

同屏中文字体固定 3 种：题字 1 + 粗宋 1 + 黑体 1。

### Type Scale

| Role     | Size                     | Line Height | Letter Spacing | Token            |
| -------- | ------------------------ | ----------- | -------------- | ---------------- |
| brush    | clamp(58px, 16vw, 132px) | 1.1         | 0              | `--text-brush`   |
| h1       | clamp(42px, 5vw+22px, 84px) | 1.15     | .04em          | `--text-h1`      |
| h2       | clamp(32px, 4.4vw+14px, 56px) | 1.25   | .02em          | `--text-h2`      |
| title    | 28px                     | 1.3         | 0              | `--text-title`   |
| title-s  | 24px                     | 1.3–1.4     | 0              | `--text-title-s` |
| lead     | 20px                     | 1.75        | 0              | `--text-lead`    |
| body     | 18px                     | 1.75        | 0              | `--text-body`    |
| note     | 16px                     | 1.5–1.75    | 0              | `--text-note`    |
| label    | 13px（Cinzel）           | 1.2         | .18em          | `--text-label`   |

## Tokens — Spacing & Shapes

**Base unit:** 4px

**Density:** 宽松，给老花眼留行距

### Spacing Scale

| Name | Value | Token        |
| ---- | ----- | ------------ |
| 1    | 4px   | `--space-1`  |
| 2    | 8px   | `--space-2`  |
| 3    | 12px  | `--space-3`  |
| 4    | 16px  | `--space-4`  |
| 6    | 24px  | `--space-6`  |
| 8    | 32px  | `--space-8`  |
| 12   | 48px  | `--space-12` |
| 16   | 64px  | `--space-16` |
| 24   | 96px  | `--space-24` |
| 页边 | clamp(16px, 4vw, 48px) | `--gutter` |

### Border Radius

| Name  | Value | Token            |
| ----- | ----- | ---------------- |
| sm    | 2px   | `--radius-sm`    |
| md    | 4px   | `--radius-md`    |
| lg    | 8px   | `--radius-lg`    |
| round | 50%   | `--radius-round` |

| Element          | Value       |
| ---------------- | ----------- |
| 卡片、画框、牌匾 | 0（直角）   |
| 按钮、输入框     | 4px (md)    |
| 印章、角标       | 2px (sm)    |
| 奖章、编号、徽标 | 50%         |

### Shadows

| Name   | Value | Token |
| ------ | ----- | ----- |
| card   | `0 1px 0 rgba(94,7,12,.08), 0 18px 40px -22px rgba(94,7,12,.25)` | `--shadow-card` |
| lift   | `0 2px 0 rgba(94,7,12,.08), 0 24px 48px -20px rgba(94,7,12,.25)` | `--shadow-lift` |
| medal  | 3px 金圈 + 11px 绛红圈 + 1px 淡金线 + 90px 金色外晕 + 下投影 | `--shadow-medal` |
| button | `0 1px 0 #fbe9b7 inset, 0 10px 24px -12px rgba(40,0,0,.5)` | `--shadow-button` |

阴影一律带红调（rgba(94,7,12,…)），不用纯黑阴影，免得米白底发灰。

### Motion

| Name      | Value                          | Token         |
| --------- | ------------------------------ | ------------- |
| ease-rise | `cubic-bezier(.22,.8,.2,1)`    | `--ease-rise` |
| ease-zoom | `cubic-bezier(.5,1,.89,1)`     | `--ease-zoom` |
| fast      | 180ms                          | `--dur-fast`  |

**奖章登场（签名动效）：** 外层 `.stage-zoom` 用 `view-timeline`，里面的奖章 `position:sticky` 钉在视口中线附近；区间从奖章顶边进入视口底部开始，到额外滚动 `min(36svh,300px)` 为止。奖章 `scale(.5→1)`，光芒 `scale(.6→1) rotate(-24°→0)`、透明度 .25→1，扫光在进度 40% 后从左掠到右（伪元素不能放进 `:is()`，`.sweep::before` 的 `animation-timeline` 必须单独写一条选择器，否则扫光走文档时间线、0 秒就结束，永远看不到），图注在最后 35% 淡入；图注托在绛红底 + 上下 1px 金线的名牌条上，避免 16px 字落在光心红上（直接压光心只有 4.86:1）。写在 `@supports (animation-timeline: view())` 里，`animation-timeline` 放在 `animation` 简写之后；不支持时（安卓微信、iOS 26 以下）JS 兜底：IntersectionObserver 只在舞台附近挂 passive scroll，rAF 里只写 transform/opacity；`?nosd` 强制走兜底；`prefers-reduced-motion` 和视口高于 1600px 时直接显示终态。实测半人马终态宽度：390 宽 372px、768 宽 639px、1440 宽 659px，均在分辨率天花板内。

### Layout

- **Section gap:** 手机 64px / 桌面 96px
- **Card padding:** 18–20px
- **Element gap:** 16–24px
- **Max content width:** 1200px（页眉 1360px）
- **Header:** 手机 64px / 桌面 76px，绛红底 + 1px 金底线，sticky

## Components

### 金箔主按钮 Gold CTA

**Role:** 红底上的唯一主动作（页眉、开幕）
`background: var(--grad-gold-btn)`（最暗处 #dfb566，对印泥红字仍有 7.24:1；题字用的 `--grad-gold` 暗部更深，不用于按钮），文字 `--color-red-ink` 18px/700，高 56px（页眉 52px），圆角 4px，`--shadow-button`。hover 提亮 6%；active 下沉 1px；focus 3px 淡金外环。手机上撑满到 340px 宽。

### 朱砂按钮 Red Button

**Role:** 米白底上的主动作（报名台）
`--color-red` 底 + `--color-cream` 字，高 56px。hover 转 `--color-red-deep`。

### 描边按钮 Line Button

**Role:** 次动作「复制客服链接」
透明底 + 2px 朱砂内描边，hover 反白成朱砂实底。

### 禁用按钮 Disabled

**Role:** 「下载知君 ↓ / 下载万象 ↓」
`--color-disabled-bg` + `--color-disabled-text`（8.76:1），无阴影，旁边 16px 淡墨小字「下载暂未开放」。

### 牌匾标题 Plaque

**Role:** 红底区块的主标题（共学五步、联系区）
绛红底 + 1px 赤金边 + 5px 外偏移的半透明金线，字为粗宋 900 金箔渐变，28–44px。

### 章节签 Plate

**Role:** 章节眉标（01 / 从你的积累出发、CENTAUR JOURNAL / 观点与动态）
朱砂底米白字，16px/700，圆角 2px，Cinzel 数字 15px。

### 方印 Seal

**Role:** 品牌落款
米白底朱文，竖排两列「半人马 / AI学院」（AI 横排合字），双线内框。开幕跟在题字右上角，全站只盖一次。

### 对联 Couplet

**Role:** 桌面开幕两侧（≥1024px）
副标题两行竖排：右联「面向经营者与管理者的」、左联「长期共学与共创学院。」，绛红底、28px 粗宋、字距 .3em、双层金框。手机上回到横排居中。

### 画框 Frame

**Role:** 三章插画
白衬纸 12px + 5px 内缩 1px 赤金线 + 四角 22px 朱砂角花，下接「EXPERIENCE ｜ 中文图注」。暖色插画靠衬纸隔开红色，不直接贴在红底上。

### 产品行 Product Row

**Role:** 知君 / 万象
白底卡、顶边 3px 朱砂，左侧 48px 朱文单字印（知 / 万）+ 产品名 20px/700，下一行禁用按钮 + 说明。

### 期刊卡 Journal Card

**Role:** 观点与动态
白底、1px 金米线边、图片下沿 3px 朱砂线，正文区内缩 1px 半透明金框（不压图）。角标「观点」朱砂小方块。桌面 7:5 两栏，首篇跨两行。

### 典礼流程单 Program

**Role:** 共学五步
米白纸面 + 金框 + 6px 外金线，放在朱砂底上。编号 64px 朱砂圆 + 古铜金外环，Cinzel 数字；步骤之间用 2px 古铜金点线连接（手机竖向、桌面横向）。

### 题词卷轴 Scroll Quote

**Role:** 院长寄语
白纸面，上下各一根 14px 绛红轴、两端 10px 中金轴头。引文粗宋 900，26–44px，「人机共生」朱砂色；下接 64×2 朱砂短线与署名。

### 报名台 Contact Desk

**Role:** 联系区
朱砂底 + 背后放射金线；米白台面、顶边 6px 赤金；正文 20px 居中，主按钮 + 描边按钮并排（手机竖排）。

### 回纹带 Fret Band

**Role:** 开幕底栏「人决定方向，AI 拓展人的能力。」上下的装饰
20×10 回纹 SVG 做 mask 平铺，赤金 55% 透明度，绛红底。

### Input Field

**Role:** 报名表（本页未用，样张备用）
白底、1px 古铜金边、高 52px、圆角 4px；focus 3px 朱砂外环；错误态朱砂边 + 16px 朱砂提示。

## Surfaces

| Level | Name   | Value                  | Purpose                        |
| ----- | ------ | ---------------------- | ------------------------------ |
| 0     | 舞台红 | `--grad-stage`         | 开幕、共学五步、联系区         |
| 0     | 宣纸   | `#fbf5ea`              | 三章、观点、院长寄语           |
| 1     | 纸面   | `#ffffff`              | 卡片、画框、卷轴               |
| 1     | 台面   | `#fbf5ea`（红底之上）  | 流程单、报名台                 |
| 2     | 绛红   | `#6e0910`              | 页眉、页脚、牌匾、底栏         |

## Do's and Don'ts

### Do

- 红底只铺开幕、共学五步、联系区三段，中间用米白阅读区隔开，红白交替像会场的主背景板与嘉宾席。
- 金色只做三件事：细线、题字/牌匾字、主按钮。正文和 28px 以下的字不用金。
- 书法题字全站只出现一次（「你的能力。」），其他标题一律粗宋 900。
- 光芒用 `repeating-conic-gradient` 画 0.8° 细线，透明度 30%，外缘用 mask 淡出。
- 手机正文 18px、行高 1.75；按钮 56px 高、18px 字，写全「联系学院顾问 ↗」。
- 阴影带红调（rgba(94,7,12,…)），直角卡片配 1px 金米线。

### Don't

- 不要满屏放射光、斜体描边大字、立体「2026」——那是年会 PPT 模板（鸿鹄开年盛典反例）。
- 不要写「限时」「震撼」「圆满成功」，不要感叹号，不要任何数字、学员数、客户 logo、合影、奖牌。
- 不要在花纹、光芒上直接压正文；红底上的正文只用 `--color-cream`。
- 不要用第二种书法字体，不要在按钮、导航里用书法。
- 不要让扫光、光芒循环播放——只在登场时随滚动走一次。
- 不要用纯黑 #000 或 Inter / Roboto / Arial。

## Imagery

主视觉只有一个物件：透明底半人马放在米白奖章里，奖章外是绛红圈和细金光芒，思路和华为全联接大会「一个 3D 物件当主视觉」一致，但换成颁奖盛典的奖章语言。三张暖色插画不上红底，一律进白衬纸画框，靠红角花把它们拉进红金体系。期刊封面直接用插画与 `academy-centaur-hero.webp`，裁 16:10。装饰全部是 CSS / 内联 SVG：网格（6% 金）、回纹、光芒、印章，没有位图装饰。

## Layout

居中对称为主轴：开幕全部居中，桌面两侧挂竖排对联；三章回到左右图文交错（5:6 栅格），给老板一个「看得懂」的阅读节奏；共学五步桌面横排五格、手机竖排带点线；观点区 7:5 大小卡；院长寄语与联系区又回到居中。1440 / 768 / 390 三档成立，390 宽任何滚动位置无横向溢出。左下角留返回钮安全区。

## Agent Prompt Guide

Quick Color Reference:

```
stage red: #a30f17 → #6e0910 (radial, glow #d0231f)
ivory reading area: #fbf5ea, cards #ffffff
ink: #2a1a14, muted: #5a4638
on-red text: #fff3e0
gold hairline: #e9c274, gold foil gradient: #fbe9b7 → #e9c274 → #d6a553 → #f6dc9f
```

Example Component Prompts:

1. 做一块开幕：朱砂径向渐变底 + 6% 金网格，居中粗宋 900「让 AI 成为」，下一行马善政题字金箔渐变「你的能力。」，右上角米白朱文方印；下面 56px 金箔按钮「联系学院顾问 ↗」。
2. 做一个流程单：米白纸面放在朱砂底上，1px 赤金框 + 6px 外偏移金线；五个 64px 朱砂圆编号（Cinzel），2px 古铜金点线相连，标题粗宋 24px，说明 18px 淡墨。
3. 做一段引文：白纸面上下各一根 14px 绛红卷轴、两端中金轴头；粗宋 900 引文居中，关键词朱砂色，下接 64×2 朱砂短线与署名。

## Similar Brands

- **中欧国际工商学院 CEIBS（cn.ceibs.edu）** — 红 + 金 + 米白三色关系（#BF0008 / #BD8E1F / #F5F2EE）、手机首屏整屏红渐变配金线；落到 `--color-red` / `--color-gold` / `--color-ivory`。
- **《中国企业家》iceo.com.cn** — 红色正式字标下配宽字距小口号；落到开幕的「CENTAUR AI ACADEMY —— 学习 · 实践 · 共创」眉标和 Cinzel .18em 字距。
- **2025 中国企业家年度榜单（腾讯新闻转《企业家》）** — 红底 + 圆形白底主体 + 印章 logo 的荣誉版式；落到米白奖章托半人马和朱文方印。
- **中国企业联合会 cec1979.org.cn** — 「书法题字 + 会徽」的分量感；只取题字一处，不取它的多色服务块。
- **华为全联接大会 2026 / 云栖大会 2026** — 主视觉只放一个物件、品牌名字距拉开、居中对称像牌匾；落到奖章登场与对联、牌匾。
- **反例：鸿鹄中国 2025 开年盛典** — 红底放射光 + 立体年份 + 斜体书法 + 金额标题；本范式的光芒只有 0.8° 细线、30% 透明度，且不写任何数字。

## 新增的结构性文字

以下文字不在 content.md 里，是为版式新增的结构性标签，均不含事实性说法：

- 页面 `<title>`：「半人马AI学院 · 中国红大会」；kit 页 `<title>`：「中国红大会 · 组件样张」
- 开幕方印：「半人马 AI学院」（品牌名重排，装饰用，`aria-hidden`）
- 产品行单字印：「知」「万」（`aria-hidden`）
- 跳转链接：「跳到正文」；菜单按钮无障碍名：「打开菜单 / 关闭菜单」
- 复制反馈：「已复制」
- kit.html 的样张说明：「CENTAUR AI ACADEMY · DESIGN KIT」「红铺底、金点睛、米白托正文」、各区块名（色板 / 字体与字号 / 按钮全状态 / 徽标、印章、牌匾、对联 / 卡片与产品行 / 题词引文 / 流程步骤 · 典礼流程 / 图片框处理 / 报名台）及其英文小标签、色名与用途说明、状态名（default / hover / active / focus / disabled）、字号说明、输入框示例（「您的称呼」「例如：王总」「联系电话」「请填写 11 位手机号」「输入框 · default / focus」）、图片框说明（「暖色插画：白衬纸 + 金内线 + 红角花」「MEDAL ｜ 透明底半人马：米白奖章 + 克制金光」）

## Quick Start

### CSS Custom Properties

```css
:root {
  /* Colors — 红 */
  --color-red: #a30f17;
  --color-red-deep: #6e0910;
  --color-red-glow: #d0231f;
  --color-red-ink: #5e070c;

  /* Colors — 金 */
  --color-gold: #e9c274;
  --color-gold-light: #fbe9b7;
  --color-gold-mid: #d6a553;
  --color-gold-deep: #b8863b;

  /* Colors — 米白与墨 */
  --color-ivory: #fbf5ea;
  --color-paper: #ffffff;
  --color-cream: #fff3e0;
  --color-cream-muted: #f0cdb5;
  --color-ink: #2a1a14;
  --color-ink-muted: #5a4638;
  --color-line: #e6d3ae;
  --color-disabled-bg: #efe6d6;
  --color-disabled-text: #4a3a2e;

  /* Colors — 透明度（光效专用，不压正文） */
  --gold-a06: rgba(233, 194, 116, 0.06);
  --gold-a14: rgba(233, 194, 116, 0.14);
  --gold-a30: rgba(233, 194, 116, 0.3);
  --gold-a55: rgba(233, 194, 116, 0.55);
  --shine-a60: rgba(255, 250, 235, 0.6);
  --shade-a50: rgba(40, 0, 0, 0.5);
  --shade-a25: rgba(94, 7, 12, 0.25);
  --shade-a08: rgba(94, 7, 12, 0.08);

  /* Gradients */
  --grad-gold: linear-gradient(180deg, #fbe9b7 0%, #e9c274 46%, #d6a553 58%, #f6dc9f 100%);
  --grad-gold-btn: linear-gradient(180deg, #fbe9b7 0%, #e9c274 50%, #dfb566 62%, #f6dc9f 100%);
  --grad-stage: radial-gradient(ellipse 70% 55% at 50% 72%, #d0231f 0%, #a30f17 55%, #6e0910 100%);
  --grad-medal: radial-gradient(circle at 50% 38%, #ffffff 0%, #fbf5ea 48%, #f3e2bf 100%);

  /* Typography — Families */
  --font-brush: "Ma Shan Zheng", "STKaiti", "KaiTi", "Kaiti SC", serif;
  --font-title: "Noto Serif SC", "Songti SC", "STSong", "SimSun", serif;
  --font-body: "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  --font-latin: "Cinzel", "Trajan Pro", "Times New Roman", serif;

  /* Typography — Scale */
  --text-label: 13px;
  --text-note: 16px;
  --text-body: 18px;
  --text-lead: 20px;
  --text-title-s: 24px;
  --text-title: 28px;
  --text-h2: clamp(32px, 4.4vw + 14px, 56px);
  --text-h1: clamp(42px, 5vw + 22px, 84px);
  --text-brush: clamp(58px, 16vw, 132px);

  /* Line Height & Tracking */
  --leading-title: 1.25;
  --leading-body: 1.75;
  --tracking-latin: 0.18em;
  --tracking-couplet: 0.3em;

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
  --gutter: clamp(16px, 4vw, 48px);
  --maxw: 1200px;
  --header-h: 64px;

  /* Border Radius — 端正，基本直角 */
  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
  --radius-round: 50%;

  /* Borders */
  --hair: 1px;
  --rule-gold: 1px solid var(--color-gold);
  --rule-line: 1px solid var(--color-line);

  /* Shadows & Glow */
  --shadow-card: 0 1px 0 var(--shade-a08), 0 18px 40px -22px var(--shade-a25);
  --shadow-lift: 0 2px 0 var(--shade-a08), 0 24px 48px -20px var(--shade-a25);
  --shadow-medal: 0 0 0 3px var(--color-gold), 0 0 0 11px var(--color-red-deep), 0 0 0 12px var(--gold-a55), 0 0 90px 10px var(--gold-a30), 0 40px 80px -30px var(--shade-a50);
  --shadow-button: 0 1px 0 var(--color-gold-light) inset, 0 10px 24px -12px var(--shade-a50);

  /* Motion */
  --ease-rise: cubic-bezier(0.22, 0.8, 0.2, 1);
  --ease-zoom: cubic-bezier(0.5, 1, 0.89, 1);
  --dur-fast: 180ms;
}
@media (min-width: 1024px) {
  :root {
    --header-h: 76px;
  }
}
```

### Tailwind v4

```css
@theme {
  --color-red: #a30f17;
  --color-red-deep: #6e0910;
  --color-red-glow: #d0231f;
  --color-red-ink: #5e070c;
  --color-gold: #e9c274;
  --color-gold-light: #fbe9b7;
  --color-gold-mid: #d6a553;
  --color-gold-deep: #b8863b;
  --color-ivory: #fbf5ea;
  --color-paper: #ffffff;
  --color-cream: #fff3e0;
  --color-cream-muted: #f0cdb5;
  --color-ink: #2a1a14;
  --color-ink-muted: #5a4638;
  --color-line: #e6d3ae;
  --color-disabled-bg: #efe6d6;
  --color-disabled-text: #4a3a2e;

  --font-brush: "Ma Shan Zheng", "STKaiti", "KaiTi", "Kaiti SC", serif;
  --font-title: "Noto Serif SC", "Songti SC", "STSong", "SimSun", serif;
  --font-body: "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  --font-latin: "Cinzel", "Trajan Pro", "Times New Roman", serif;

  --text-label: 13px;
  --text-note: 16px;
  --text-body: 18px;
  --text-lead: 20px;
  --text-title-s: 24px;
  --text-title: 28px;

  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;

  --shadow-card: 0 1px 0 rgba(94, 7, 12, 0.08), 0 18px 40px -22px rgba(94, 7, 12, 0.25);
  --shadow-lift: 0 2px 0 rgba(94, 7, 12, 0.08), 0 24px 48px -20px rgba(94, 7, 12, 0.25);

  --ease-rise: cubic-bezier(0.22, 0.8, 0.2, 1);
  --ease-zoom: cubic-bezier(0.5, 1, 0.89, 1);
}
```
