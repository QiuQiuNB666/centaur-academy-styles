# Siena Film Foundation — Style Reference

> 黑场、米白字、一张电影票：把官网做成「入场」的仪式。

**Theme:** 黑 + 米白纸感 / 电影感编辑风（暗底为主，米白反相为辅）
**URL:** https://siena.film/ （2026-09-17 可访问；Webflow 站 + Vercel 托管的自写 CSS/JS）

整站几乎只有两种颜色：纯黑与偏暖的米白 #FAF7EF。权威感不靠图形装饰，而靠一款窄长的展示衬线标题字，用极紧的行高（0.7–0.9em）叠成海报式字块。首屏不是 banner，而是一道「入口」：黑白竖条纹扫过字标，底部一枚票根形状的 ENTER 按钮。红与金只作为极小的状态点出现。注意：Awwwards 对它的描述是精品电影制作公司，并非严格意义的基金会。

## Colors（均读自 Webflow 样式表 :root 变量）

| Name | Value | Role |
|---|---|---|
| Black | `#000000`（`--black:black`） | body 背景，主画布 |
| Paper White | `#FAF7EF`（`--white`） | 正文与标题色；反相区块/票根按钮的底色 |
| Paper 30% | `#FAF7EF4D`（`--white--30`） | 细线、次要文字、半透明描边 |
| Gray | `#222222`（`--gray`） | 暗面板、分隔 |
| Mid Gray | `#BABABA`（`--col--gray`） | 弱化说明文字 |
| Signal Red | `#FF0F00`（`--red`） | 圆点、悬停底、向下箭头按钮，极少量 |
| Gold | `#FFC700`（`--gold`） | 作品筛选的当前态文字，极少量 |

## Typography（@font-face 实际加载，均为单字重 400，TTF，font-display: swap）

- **标题：Neue Brucke Regular** — 窄长展示字，全大写；出品方未能核实。
- **点缀衬线：P22 Parrish Roman** — 字名显示属 P22 字库；仅少数几处使用。
- **正文：NB International Regular** — body 20px / 行高 1.3em。
- 字阶变量：h1 `5.6rem`（移动端 `3.2rem`）、h2 `3.2rem`、h3 `3rem`、h4 `2rem`、h5 `1.6rem`、正文大 `1.05rem`、眉题 `.8rem` / `.6rem`。
- H1 用法：`letter-spacing:-.03em`、`line-height:.77em`、`max-width:8ch`（强制断成窄栏海报块）；CTA/页脚大字 `line-height:.9em / .7em`，`text-transform:uppercase`，`font-weight:400`。
- html 根字号声明未能读到（疑由 JS 或视口单位设置；main.css 内有 `4vw` / `1.8vw` 的字号覆盖）。

## Shapes & Motion

- 圆角三档：`6px`（--rounded-xs，票根/小件）、`12px`（--rounded-md）、`100rem`（胶囊/圆点）。业务样式里基本没有 box-shadow，层次靠黑/米白反相与 `mix-blend-mode:difference`。
- 按钮用 SVG `clip-path:url(#ticketMask)` 裁出票根缺口，另有一排「打孔」小圆（`--white--hole-size:.6rem`）。
- 间距变量：页边 `--gx:3rem`（移动 1.5rem）、纵向 `--gy:3rem`、槽 `--gutter:1.2rem`。
- 曲线：`--customEase: cubic-bezier(.19,1,.22,1)`、`--easeOutQuint: cubic-bezier(.23,1,.32,1)`、`--easeOut: cubic-bezier(.77,0,.175,1)`；时长 .2s–1.1s，面板展开 `.9s`（过渡 grid-template-rows），滑块 `.8s`。
- JS 侧可见 GSAP 的 ScrollTrigger / SplitText / Flip 与 Lenis 平滑滚动；开场为 mp4 字标动画。

## Signature（签名手法）

1. **两色纪律**：全站只有黑与暖米白，彩色压到「一个红点」的量级——任何彩色物件放上去都会成为视觉焦点。
2. **入口仪式**：首屏只有字标 + 竖条纹转场 + 一枚 ENTER 票根，进入后才给内容；短，且只发生一次。
3. **窄长标题字 + 压扁行高**：`max-width:8ch` + `line-height:.77em` + `-0.03em`，把标题排成电影海报字块。
4. **把隐喻做进控件**：按钮是票根（clip-path 缺口 + 打孔），导航是胶片条——隐喻落在可点击的零件上，而不是插画上。

## 迁移到半人马AI学院

- **借**：黑 / 米白 #FAF7EF 两色纪律（橙蓝折纸半人马将成为唯一彩色）；窄栏大标题的排法；一次性的短开场；「隐喻进控件」的思路（可换成折纸折痕/折角，而不是票根）。
- **要补**：三款字体均为商业授权且只含拉丁字符，需另选中文标题字（窄长、高对比的宋/明朝体或定制字标）与中文正文字，并处理授权；中文不宜用 .77em 行高，建议 1.05–1.15 起调；需要一段 2–3 秒的 logo 开场动画素材。
- **风险**：暗底 + 入口门槛对「经营者/管理者」受众偏戏剧化，可能拖慢获取课程信息；建议以米白为主画布、黑为反相区块，并让开场可跳过。胶片条滑块依赖大量剧照，学院无此素材，不取。

## Sources（已亲自打开核实）

- https://www.awwwards.com/sites/siena-film-foundation — SOTD 2025-03-18，7.9 分，Developer Award，制作方与调色板
- https://www.awwwards.com/websites/sites_of_the_month/ — 列为 2025 年 3 月 Site of the Month
- https://siena.film/ 首页 HTML；https://cdn.prod.website-files.com/6728a72e769070a603d43c13/css/siena-work-space.webflow.5a4c7c0c2.min.css；https://siena-film-foundation.vercel.app/styles/main.css
