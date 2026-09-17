# Terminal Industries — Style Reference
> 把货场调度这种「最不性感」的 B2B 题材，拍成一部有黄昏光线的工业短片。

**Theme:** 工业精密 / B2B 产品叙事。白底墨绿字为正文层，黑色影像为开场层，一点荧光青柠做唯一的「通电」信号。

**总述：** 首屏是一辆侧光下的整车剪影，导航收在一块半透明磨砂胶囊里，三个按钮按「青柠 / 白 / 灰」排出主次。往下滚动，画布切回白底墨绿字，用 12 栏栅格、超大细字重标题和等宽大写小标签交替推进：主张 → 客户背书 → 分层方案 → 收益计算器 → 分 Tab 平台讲解 → FAQ，最后以墨绿大页脚收束。技术栈为 Nuxt/Vue + Tailwind + Lenis 平滑滚动（源码可见 `html.lenis`、`/_nuxt/`）。

## Colors（全部读自首页内联 `:root` 变量）
| Name | Value | Role |
|---|---|---|
| White | `#ffffff` (`--c-white`) | html 画布底色 |
| Dark Green | `#052424` (`--c-dark-green`) | 正文默认字色、页脚底色；另有 20%/15%/5% 透明度做线与浅底 |
| Black | `#000000` (`--c-black`) | 开场影像层 / 深色段落 |
| Lime | `#abff02` (`--c-lime`) | 唯一强调：主 CTA、logo 图形 |
| Orange | `#fb6b3c` (`--c-orange`) | 次级点缀（用量很少） |
| Dirty White | `#f0f0f0` (`--c-dirty-white`) | 浅灰卡片/分区底 |
| Gray | `#454742` / `#7f7f7f` / `#c2c2c2` / `#ddd` | 次要文字与分隔线阶梯 |
| White α | `#ffffff1a`、`hsla(0,0%,100%,.15–.4)` | 深色段上的描边与磨砂玻璃 |

## Typography
- 标题/正文：**SuisseIntl**（Swiss Typefaces 出品，商业字体，自托管 woff2），加载字重 400 / 450(Book) / 500 / 600。
- 等宽：**Geist Mono**（Vercel，OFL 开源），400 / 600 / 700，用于标签、按钮、编号。
- H1（`.title-h1`）：桌面 `font-size:min(5.729vw,146.67px)`，`letter-spacing:min(-.057vw,-1.47px)`，`font-weight:400`，`line-height:.95`；移动端 `10.256vw` / 字距 `-.308vw`。
- H2 `min(3.333vw,85.33px)`、行高 .96–1.05；正文 `.body-1` `min(1.198vw,30.67px)`；`.body-3` 1.25rem / 1.46。
- 标签 `.label-4`：0.6875rem、`letter-spacing:.18em`、全大写、等宽——和巨大的细体标题形成两极对比。
- 整套字号用 vw 流体缩放并以 px 封顶，没有中间档的「将就字号」。

## Shapes & Motion
- 圆角克制：主流是 `.5rem / 8px`，少量 `1.25rem`，圆形仅用于图标；没有大圆角气泡卡。
- 阴影几乎不用：仅 `0 8px 32px #0524240f`（墨绿 6%）与抽屉 `-4px 0 24px #0003`；层次靠 `backdrop-filter:blur(27px)` + 白 15% 的磨砂玻璃。
- 栅格：桌面 12 栏，`--grid-gutter:min(1.042vw,26.67px)`，`--grid-margin:min(3.646vw,93.33px)`；移动端 2 栏，边距 5.128vw。
- 动效曲线：最常见 `cubic-bezier(.19,1,.22,1)`（expo-out），其次 `cubic-bezier(.39,.575,.565,1)`、`(.16,1,.3,1)`；Lenis 平滑滚动 + 标题逐字符（`.--char`）揭示 + 序列帧/Canvas 背景。

## Signature（签名手法）
1. **一个荧光色，只给一个动作**：全站近乎黑白墨绿，青柠 `#abff02` 只出现在主 CTA 与 logo，其余按钮用白/灰降级。
2. **巨大细体 + 微小等宽大写**：400 字重、行高 .95、负字距的超大标题，配 11px、字距 .18em 的等宽标签，像仪表盘刻度。
3. **大数字当主视觉**：效率指标用标题级字号单独成块，旁边用等宽小字标注口径与来源。
4. **磨砂胶囊导航**：导航悬浮在影像上，8px 圆角、半透明模糊，不抢画面。
5. **访客自己算收益**：内嵌计算器把「说服」变成「自证」。

## 迁移到半人马AI学院
- **借什么：** 叙事骨架（主张 → 学员/企业背书 → 分层课程 → 「你的团队能省多少工时」计算器 → FAQ）；白底 + 一个深色（可把墨绿换成 logo 的深蓝）+ 一个强调色（青柠换成 logo 橙）；大数字指标排版；等宽小标签体系；expo-out 曲线与逐行揭示。
- **需要补：** 一张能撑满首屏的半人马 3D 主视觉（静帧或短循环）顶替卡车影像；SuisseIntl 是付费字体且无中文，中文建议思源黑体/HarmonyOS Sans 细到常规字重配 Geist Mono（开源可直接用）；真实可标注来源的学员数据，否则大数字反而失信。
- **风险：** 中文超大细体在低分屏易发虚，行高 .95 对汉字太挤（建议 1.1–1.15）；vw 流体字号需对中文长标题设上限；重动效/序列帧对 35–55 岁用户的旧设备与微信内置浏览器不友好，需降级方案。

## Sources（已亲自打开核实）
- https://terminal-industries.com/ （首页 HTML 内联 CSS 与 `/_nuxt/*.css`，2026-09-17 抓取）
- https://www.awwwards.com/sites/terminal-industries （SOTD 2025-09-03，7.68；Dev Award 7.89；REJOUICE® + PROPAGANDE）
- https://www.awwwards.com/websites/sites_of_the_month/ （2025 年 9 月 Site of the Month）
