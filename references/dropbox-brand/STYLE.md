# Dropbox Brand — Style Reference

> 一本会动的品牌手册：白纸、蓝色细线网格、一个强蓝，其余全靠字和可玩的小部件。

**Theme**：品牌手册式 / 瑞士网格 · 亮色为主（另有近黑反相面）
**URL**：https://brand.dropbox.com/ · 制作：Daybreak Studio（加拿大）· 平台：Webflow + Lottie

首屏几乎是空的：白底上铺着淡蓝 hairline 画出的不等分网格，只有一个单元格里放一段强蓝色的宽体大字，右下角一个向下箭头。
往下滚，网格单元展开成八个板块的色块入口；每个板块内部用可拖、可调参的小部件解释规则（例如可变字体的字重/字宽滑动）。
高级感来自克制——默认态只有「白 + 一个蓝 + 近黑」，二十来个辅助色只在对应板块里短暂出场。

## Colors（均读自主样式表 CSS 变量）

| Name | Value | Role |
|---|---|---|
| Canvas | `#FFFFFF`（--surface--background-light） | 画布 |
| Dropbox Blue | `#0061FE`（--accent--ui-accent / --accent--tab） | 唯一强色：标题、板块色块、交互态 |
| Ink | `#1A1918`（--text--base）/ `#1E1919`（--text--text-light、深色面底） | 正文、反相底 |
| Subtle text | `#736C64`（亮面）/ `#BBB5AE`（暗面） | 次级说明 |
| Hairline | `#C5DBFF`（--annotation--hairline） | 网格线 |
| Annotation | `#5F9DFF`（实线）/ `#5F9DFF66`（40% 透明） | 标注线、箭头 |
| Overlay / Coconut | `#F7F6F5` / `#F7F5F2` | 浅暖灰卡面 |
| 辅助色（板块内才出现） | Tangerine `#FF8C19`、Sunset `#FA551E`、Lime `#B4DC19`、Zen `#14C8EB`、Orchid `#C8AFF0`、Navy `#283750` 等 | 每个辅助色配一个深色「on-」文字色 |

## Typography

- 标题：**Sharp Grotesk DB 可变字体**（CSS 名 `Dbsharpgroteskvariable Vf`，wght 250–900，另有 wdth 轴；Sharp Type 为 Dropbox 定制，专有）。另加载静态切片 `Sharpgroteskdbbook 20/23`。
- 正文：**Atlas Grotesk Web** 400/500 含斜体（Commercial Type，商业授权），body 14px/20px，色 `--text--text-light`。
- 等宽：Noto Sans Mono 400/500（Google Fonts，用于标注）。
- 首页没有 `<h1>`；首屏大字是 `h3.nav-button-title-1`，36px（≤991px 降到 24px）。板块瓦片标题 `.tile-title`：`min(2.75vw - 6px, 1.375vw + 15px)`，weight 500，字距 -0.02em，行高 0.8em。
- 板块内巨字 `.heading-fill`：`clamp(0px, 6.25vw - 15px, 120px)`，行高 120%，`font-variation-settings: "wght" 483, "wdth" 108`——用非整百字重和略加宽的字宽，是它「不像默认字体」的来源。
- 全部 `font-display: block`。

## Shapes & Motion

- 圆角两极：功能件 2px（最多）或 0；胶囊/圆点 100px / 50%；卡片 10–12px、少量 20/24px。
- 阴影基本不用：唯一成形的是 `0 0 0 1px #0000001a, 0 1px 3px #0000001a`（细描边式）。层次靠线和色块。
- 栅格：12 列 `1fr` 为主（另见 10/16/20 列变体），列距 24px；断点 991 / 767 / 479。字号大量用 vw/clamp/min 随视口缩放。
- 动效：CSS 过渡 `cubic-bezier(.4,0,.2,1)`，.15–.4s，只动 color / background / border-radius；页面内联脚本里多用 `cubic-bezier(.5,0,.2,1)`、`(.2,.1,0,1)`、`(.5,0,0,1)` 这类「慢入急停」曲线；logo 用 Lottie JSON。

## Signature（可照做）

1. **网格线本身就是装饰**：1px 淡蓝 hairline 画出不等分格子铺满白底，内容只占其中一格，其余留空。
2. **一个强色 + 近黑**：默认态蓝占比很低但全是关键位（标题、箭头、悬停）；辅助色被关在各自板块里。
3. **可变字体当主角**：用 wght 483 / wdth 108 这种中间值，并把「调字重、调字宽」做成可拖动的演示件。
4. **板块 = 色块瓦片**：首页即目录，八个入口是同尺寸瓦片，点开后瓦片扩张成整页（border-radius 与 padding 一起过渡）。

## 迁移到半人马AI学院

- **借**：hairline 网格铺底 + 单格大字首屏；「橙或蓝择一」做唯一强色、近黑正文；把方法论拆成 6–8 个同构瓦片板块；每个板块配一个能拖能调的小演示（如「人定方向 / AI 扩能力」的滑杆）。
- **补**：Sharp Grotesk 与 Atlas Grotesk 都是商业/定制字体且不含中文，不能照搬。中文需另选有宽体气质、最好带可变字重的字体（如思源黑体可变版、阿里巴巴普惠体 3.0 等可免费商用的先顶上），西文可用开源宽体 grotesk 替代；还需要为每个板块设计一个小交互件，这是主要工作量。
- **风险**：中文字没有 wdth 轴，「宽体大字」的辨识度会打折；首屏极空，若文案不够硬会显得「没内容」；折纸半人马 logo 是橙蓝双色，与「只留一个强色」冲突，需要定好 logo 以外只用其中一色。

## Sources（均已亲自打开核对）

- https://brand.dropbox.com/ （HTTP 200，首页 HTML + 主样式表 brand-app-site.webflow.*.css）
- https://www.awwwards.com/sites/dropbox-brand — SOTD 2025-02-12，7.67，Developer Award 7.8，Daybreak Studio
- https://www.awwwards.com/websites/sites_of_the_month/ — Site of the Month，Feb 2025
- https://www.cssdesignawards.com/blog/2025-website-of-the-year-winners/430/ — WOTY 2025 冠军 + Best UX Site，9.03，2026-02-12 发布
- https://www.cssdesignawards.com/woty2025/sites/dropbox-brand — 作品页，9.03，Daybreak Studio / Canada
- 截图：fold.png（1440×900 真实首屏；左下角有 cookie 弹窗未遮住主内容，未点同意）
