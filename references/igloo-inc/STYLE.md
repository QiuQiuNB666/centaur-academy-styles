# Igloo Inc — Style Reference

> 一座冰屋、一台镜头、一套等宽小字：整个官网就是一段可滚动的 3D 短片。

**Theme**：冷灰雪原 × 纯 WebGL 沉浸 × 等宽技术标注（注意：实测首屏是**冷灰浅调**，不是深色站）

整站 HTML 只有一个空 `<body>` 和一个 JS 入口，全部画面（含文字）都在 WebGL 画布里渲染。首屏是一座发光冰屋立在雪地上，
四角悬浮极小的等宽字：左上 logo 与版权、右上宣言、左下滚动提示与声音开关。没有导航栏、没有卡片、没有分栏。
滚动 = 镜头推进，冰砖散开、数字标注与细线连到 3D 物件上。高级感来自「只做一件事并做到电影级」。

## Colors（均读自源码 index-*.js / App3D-*.js）

| Name | Value | Role |
|---|---|---|
| Fog Grey | `#A0A5B1` | 页面画布 `--bgColor`，加载期与场景雾色的底 |
| Ice White | `#FFFFFF` | 全部 UI 文字、logo、标注线（着色器里出现 17 次） |
| Frost | `#E1E6F1` | 着色器 uColor2：冰/雪的亮面 |
| Slate | `#6A6F7D` | 着色器 uColor1：冰/雪的暗面 |
| Glow Blue | `#D1E3FF` / `#B5D5FF` | 冰砖缝隙的冷蓝辉光 |
| Amber | `#CDA05E` → `#AB8349` | 唯一的暖色，只在后段某个场景的粒子/材质里成对出现 |
| Black | `#000000` | 后段空场（仅 3 处） |

线/边框：未能读到 CSS 线色——站内的「线」是 WebGL 里画的白色 1px 细线。

## Typography

- 唯一字体：**IBM Plex Mono**（IBM 出品，SIL OFL 开源），自托管 woff2，两个切口 Regular / Medium（`@font-face` 均声明为 400）。
- 文字不是 DOM：字体被烘成 MSDF 贴图（`IBMPlexMono-Medium-datatexture.ktx2`）在画布内绘制，所以能跟 3D 一起做故障/解码动画。
- **没有 H1**。DOM 里无任何标题元素；首屏最大的字就是 logo 字标。正文级小字目测 13–15px、行高很紧（源码里文本组件 `lineHeight: .8`/`1`）。
- 唯一读到的 CSS 字号：`font-size: 17px` + `font-family: monospace`（降级/提示层）。字距：未能读到。
- 文案习惯：`//`、`//////` 作前缀的代码注释式小标题，右栏文字右对齐成窄柱。

## Shapes & Motion

- 圆角、阴影：CSS 层面**不存在**（未能读到任何 border-radius / box-shadow）；体积感全靠 3D 光照、雾、辉光后期。
- 栅格：无栅格。四角钉字 + 中央主体，边距目测约 50px；中间 80% 留给 3D。
- 动效：GSAP 驱动，曲线以 `sine.out`、`power2.out`、`power2.inOut` 为主（偏柔、无回弹）；无 cubic-bezier 自定义曲线。
- 加载态：雾灰底上一行 ASCII 进度符（`===---==+=` 这类），不用转圈。
- 资源：Draco 几何（.drc）+ KTX2 贴图 + EXR 环境光，主包约 1.5MB JS（不含模型贴图）。有声音开关，默认关。

## Signature（签名手法）

1. **一物到底**：全站只有一个 3D 主体，滚动让它经历「完整 → 解体 → 重组」，叙事靠镜头不靠版块。
2. **四角钉字**：所有文字缩成等宽小字钉在视口四角，中央永远留给物件；字小到像仪器读数。
3. **数据标注线**：在 3D 物件表面打点、连白色细线、挂两位数字，让一张「好看的图」变成「被测量的对象」。
4. **单色到底 + 一次暖色**：全程冷灰白，暖色只在一个场景出现一次，稀缺感即高级感。
5. **ASCII 加载条**：连 loading 都在同一套等宽语言里。

## 迁移到半人马AI学院

- **借什么**：首屏「一物到底 + 四角钉字 + 标注线」。把 3D 半人马放中央，滚动时折纸面片展开/重组；用标注线把「人决定方向」「AI 拓展能力」挂到人身与马身两个部位上——这比任何 slogan 排版都直接。
- **要补什么**：① 半人马的真 3D 模型（glb，低多边形本身面数低，很合适），只有渲染图就做不了；② 字体 IBM Plex Mono 免费可商用，但**不含中文**，中文需配一款等宽感/窄体黑体（如思源黑体 / IBM Plex Sans SC，均 OFL）；③ 懂 three.js + GSAP 的前端，或降级为「预渲染序列帧 + 滚动擦洗」。
- **风险**：① 该站冷灰单色，学院 logo 是橙蓝高饱和——只能借结构，不能借配色，否则 logo 会突兀；② 纯画布文字对 SEO、无障碍、微信内置浏览器、低端机都不友好，中文正文**必须回到 DOM**；③ 只适合首屏，课程/师资/报名等长内容页要另配一套常规范式；④ 首屏加载重，需要 ASCII 式轻加载态兜底与移动端静态图降级。

## Sources（均已亲自打开核实，2026-09-17）

- https://www.igloo.inc/ — HTML 与 `assets/index-2eb69c09.js`、`assets/App3D-f554a111.js`
- https://winners.webbyawards.com/winners/websites-and-mobile-sites/features-design/best-visual-design-aesthetic — 2026，Webby Winner，Entrant: Bureaux
- https://thefwa.com/cases/igloo-inc — FWA of the Day 2024-06-26（86 分）；FWA of the Month July 2024；Credits: Bureaux
- 截图：`fold.png`（1440×900，加载完成后约 40 秒）、`fold-early.png`（UI 淡入前）
