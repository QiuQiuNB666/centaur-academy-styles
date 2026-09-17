# Exat Typeface（Hot Type 字体发布站） — Style Reference

> 一块纯橙画布，一个顶天立地的字。没有照片，字就是图。

**Theme**：现代主义几何色块 × 动态排版（零摄影）。https://exat.hottype.co/ · 制作：Studio Size（克罗地亚）+ RISE2 Studio

整站只用一套自家字体和十来个纯色。每一章换一块底色、换一种网格（2 / 5 / 7 / 10 列），字重和字宽跟着滚动与鼠标实时变形。首屏「Exat」不是文字而是一张撑满宽度的 SVG，四个字母从底部依次顶上来。全站零圆角、零阴影、零渐变、零照片——高级感全部来自比例、负字距和颜色的笃定。

## Colors（取自 main.css 的 :root）

| Name | Value | Role |
|---|---|---|
| white | `#eeefeb` | 暖灰白，主画布与反白字（出现最多） |
| black | `#1c1d1e` | 正文、导航、黑底章节 |
| orange-01 | `#ff6200` | 首屏底色、大标题强调 |
| yellow-01 / 02 | `#ffce2e` / `#ffae00` | 色块章节、下拉列表底 |
| blue-03 / 02 / 01 | `#0000cb` / `#2546ff` / `#5c92ff` | 三阶蓝色块 |
| red-01 | `#ff0b00` | 点睛色块 |
| blue-00 | `#beeeff` | 浅蓝底 |
| pink / green | `#ff98fb` / `#1c7511` | 少量点缀 |

线：未见独立的分隔线色，分区靠色块相接。

## Typography

- 字体：全站只有 Exat 一家（Hot Type 出品，自托管 woff2）：`Exat` 200/300/400/500/700/800/900，另有 `Exat Condensed`、`Exat Wide`、`Exat Variable`（可变字体，`font-variation-settings` 由 JS 写入 CSS 变量）。无等宽字体，无回退到网络字体，只有 `sans-serif` 兜底。
- 缩放：`html{font-size:6.944vw}`（1440 宽时 1rem=100px；移动端 26.667vw），所有尺寸用 rem，整页等比缩放。
- 正文：`.16rem`（≈16px@1440）/ 行高 1.125em / 字距 -0.04em，字重 400–500 为主。
- 页面没有 `<h1>` 标签：首屏大字是 SVG 路径（宽度 = 100% − .4rem）。最大的活字是字重游乐场标题 `6.5417rem`（≈654px@1440）、行高 .78em、字距 -0.04em；章节大标题 1.06–1.14rem（≈106–114px）、字重 500、行高 .78–.88em、字距 -0.02 ~ -0.04em；数字块 3rem、字距 -0.07em。

## Shapes & Motion

- 圆角：只有 `0` 和 `50%`（正圆按钮/圆点）两种；`box-shadow` 全站只出现一次且为 `none`。
- 栅格：`repeat(2|5|7|10, 1fr)`，页边距 .2rem（≈20px），首屏上下 padding .176rem。
- 动效：签名曲线 `cubic-bezier(0.84, 0.01, 0.18, 1)` 800ms（首屏字母上推，逐字母延迟 0/100/200/300ms）；小交互一律 `200ms ease` / `300ms ease`。滚动动效用 GSAP + ScrollTrigger + SplitText，Lenis 平滑滚动，Splide 做无限跑马灯。

## Signature（签名手法）

1. **单字撑满首屏**：纯色底 + 一个贴底、贴边的巨字，导航缩到 16px。对比度来自尺寸差（约 40:1），不是装饰。
2. **vw 驱动的 rem**：根字号绑定视口宽，整页像海报一样等比放大，任何屏幕都保持同一构图。
3. **色块即分章**：每章一个饱和纯色 + 一种列数的网格，不画线、不加阴影，颜色相撞本身就是分隔。
4. **字会动，别的不动**：动效预算全花在字重/字宽形变和字母错峰入场上，统一用一条「慢起急收」曲线。

## 迁移到半人马AI学院

- **借什么**：暖灰白 + 近黑 + 一个橙一个蓝的纯色块体系（logo 的橙蓝正好对上 `#ff6200` / `#2546ff` 这一档）；vw-rem 等比缩放；首屏「一个巨字/巨形」构图——可把折纸半人马的三角折面拆成平涂色块，随滚动重排成网格；800ms 签名曲线 + 逐块错峰入场。
- **需要补什么**：Exat 是商业字体且无中文，不能直接用。需要一款有多字重、最好有可变轴的中文黑体（如思源黑体可变版，开源可商用）来承接「字重随滚动变化」；标题级中文若想要同等几何感，需另购授权字体。还需要把 logo 重绘成可拆解的矢量折面（SVG 分层）。
- **风险**：零摄影对「学院」类站点意味着讲师、学员、课堂实景无处安放，信任感要靠文案和数字撑；中文负字距 -0.04em 会挤，需重调；整站偏设计圈趣味，经营者受众可能觉得「好看但不知道卖什么」，建议只借首屏与分章色块，课程信息区回归常规版式。

## Sources（均已亲自打开核实，2026-09-17）

- CSSDA WOTY 2025 获奖公告（2026-02-12）：https://www.cssdesignawards.com/blog/2025-website-of-the-year-winners/430/
- CSSDA WOTY 2025 作品页：https://www.cssdesignawards.com/woty2025/sites/exat-typeface
- Webby 2026 Best Visual Design – Aesthetic（Nominee）：https://winners.webbyawards.com/winners/websites-and-mobile-sites/features-design/best-visual-design-aesthetic
- Awwwards Site of the Day（2025-04-03）：https://www.awwwards.com/sites/exat-typeface
- Codrops 案例拆解（2026-04-10，Studio Size 自述技术栈）：https://tympanus.net/codrops/2026/04/10/the-exat-microsite-pushing-a-typography-showcase-to-new-creative-extremes/
- Abduzeedo 评论（2026-04-16）：https://abduzeedo.com/node/89291
- CSS 来源：站点 `dist/styles/main.css` 与 `layouts/*/style.css`（ver 23.04）
