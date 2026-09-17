# /zeroz Brand Site（大塚制药，SHIFTBRAIN 制作，日本） — Style Reference

> 一本只准用一种绿的品牌书：近黑画布、巨大西文标题、小而疏的日文副题，按章节往下翻。

**Theme:** 日式品牌书 / 单色纪律的章节叙事（首页深色，内页转白）

首页是一条纵向长卷，按 chapter 编号分章（源码里是 homeChapter01–05），每章一个西文大标题加一行日文小标题，背景交给影像与 WebGL。全站 CSS 里真正的「颜色」只有一个绿，其余是近黑、白和两档极浅的绿灰。显贵来自克制：西文标题字重只用 Regular/Medium，不加粗、不压字距、行高 1；日文则反过来，小字号、0.1–0.2em 大字距、2 倍行高。
**必须先说清：** Awwwards 页面自述各章节靠 3DCG 与沉浸式 WebGL 展开（标签含 3D / WebGL / Three.js / Blender）。这部分学院做不出来，也不该学。入选只为三件事：章节结构、单色纪律、西文/汉字分工。

## Colors（读自 /_astro/*.css，Tailwind 编译产物）

| Name | Value | Role |
|---|---|---|
| Ink Canvas | `#111312`（rgb 17 19 18） | 首页画布与深色文字；body 另有 `bg-black` 兜底 |
| Paper | `#FFFFFF` | 内页画布、深底上的文字与 header |
| Zeroz Green | `#00A852`（rgb 0 168 82） | 唯一品牌色：按钮底、强调字、圆点、进度 |
| Mist Green | `#DDEAE5` | 浅色区块底 |
| Pale Mint | `#E8F6F1` | 更浅一档的区块底 |
| Deep Forest | `#133221` / `#2F6457` | 少量深绿底（各出现 1–2 次） |
| Hairline | `#1113124D` / `#11131233` | 墨色 30% / 20% 透明度，做分隔线与弱化文字 |

注：Awwwards 标注的色值是 `#00AA54`，站点 CSS 实际写的是 `#00A852`，以源码为准。

## Typography

- **西文**：`HelveticaNowDisplay-Regular` 为主，`-Md` 用于最大一级标题，`-Bd` 极少（Monotype 的 Helvetica Now Display）。
- **日文**：`TazuganeGothicStdN-Medium / -Regular / -Bold`（Monotype たづがね角ゴシック）。两者都经 FONTPLUS 脚本（webfont.fontplus.jp）按需下发，CSS 里没有 @font-face；另有一条 Google Fonts `Zen Kaku Gothic Antique` 作后备。
- **H1**：真实 `<h1>` 是 `sr-only`（只给读屏器），视觉主标是 logo 字标。视觉上的最大级 `.t-display-xl-en`：桌面 `10rem`（响应式版 `clamp(5rem, … + 11.9vw, 10rem)`），移动 `3rem`，`line-height:1em`，`letter-spacing:0`，字重 Medium。
- 章节西文标题 `.t-display-l-en`：桌面 `6.25rem`，移动 `clamp(3.125rem…3.75rem)`，Regular，行高 1。
- 章节日文标题 `.t-display-l-ja`（即 `<h2>`）：桌面 `1.875rem`/行高 1.8，移动 `1.25rem`/行高 1.6，`letter-spacing:.2em`，Medium。
- 日文正文：`.875–1.125rem`，`line-height:2em`，`letter-spacing:.1em`，开 `palt`（比例假名）。全部西文开 `"case"` 特性。
- 等宽：未能读到专用等宽字体（只有 Tailwind 默认栈）。

## Shapes & Motion

- 圆角几乎为零：`2px` 为主，`.25rem` 一处，圆点/胶囊用 `9999px`。阴影基本不用（只有 Tailwind 默认变量，和一处 `box-shadow:none`）。
- 断点以 `768px` 为绝对主力（294 处），其次 1024 / 1280。版心左右留白变量 `--l-padding-left:34px / --l-padding-right:10px`（移动端，左宽右窄给竖向进度条留位）。栅格列数：未能读到显式 grid，布局靠 flex 与绝对定位。
- 动效曲线高度统一：`cubic-bezier(.3,.26,.38,1)` 出现 66 次，时长只有 `.3s` 与 `.5s` 两档；位移类用 `cubic-bezier(.47,.16,.24,1)` 与 `(.43,.05,.17,1)`。header 颜色随章节明暗切换（`--header-color` + .5s）。
- 技术栈：Astro + Tailwind + Alpine.js + Barba（页面转场），3D 部分为 Three.js。

## Signature（签名手法）

1. **一色到底**：先定一个品牌色，再禁止第二个彩色。浅底只许用「品牌色的极浅灰化版」（#DDEAE5 / #E8F6F1），线条用墨色加透明度，不另造灰。
2. **大小语言倒置**：西文标题 100–160px、字距 0、行高 1、不加粗；母语副题只有 20–30px，却给 0.2em 字距与 1.8 行高。气势和解释分给两种文字，互不抢。
3. **编号章节 + 竖向进度**：每屏一章、章名固定格式（编号 / 西文 / 母语），侧边一根进度条，读起来像翻书而不是滚网页。
4. **首屏只有字标和一张方图**：近黑底、居中一张生活场景方形照片、巨大字标压在图上溢出画面，无按钮、无导航条、无标语。
5. **一条缓动曲线管全站**，时长两档，圆角 2px，无阴影——所有「精致感」来自一致性而不是效果。

## 迁移到半人马AI学院

- **借什么**：章节顺序（理念 → 依据 → 产品 → 真人访谈）对应学院的「主张 → 方法论 → 课程 → 企业主故事」；单色纪律（橙蓝二选一做唯一强调色，另一色只留在 logo 里）；西文大标题 + 中文小副题的分工；2px 圆角、无阴影、单一缓动曲线；用真人访谈轮播代替 logo 墙。
- **需要补什么**：Helvetica Now 与 Tazugane 都是 Monotype 商业字体，不能直接用。西文可换 Inter Display / Neue Haas 的授权版或开源的 Geist；中文用思源黑体 / 霞鹜之外的商用免费黑体，并手动设 0.1–0.2em 字距与 1.8–2 行高。还需要：一组统一调色的真人生活/工作场景照（方构图）、6–10 位企业主的肖像与访谈。
- **风险**：抽掉 3D 与视频后，这套骨架会很「空」，必须靠高质量摄影和文案撑住，否则只剩黑底大字。学院 logo 是橙蓝双色低多边形，与「只准一个颜色」天然冲突，需要先决定谁让位。中文大字距在长句上会显得散，只能用于短副题。

## Sources

- https://otsuka-air.jp/ （2026-09-17 抓取 HTML 与 6 份 /_astro/*.css，首屏截图 fold.png）
- https://www.awwwards.com/sites/zeroz-brand-site （Site of the Day 2026-08-24，7.41 分，署名 SHIFTBRAIN）
