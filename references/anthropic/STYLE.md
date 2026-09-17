# Anthropic — Style Reference

> 象牙纸底上的一句粗黑标题，旁边配一段衬线小字——像一本严肃期刊的扉页，而不是科技公司的落地页。

**Theme:** light（暖象牙底 + 近黑墨色；另有一套反转的深色区块主题）

现站（2026-09-17 抓取，Webflow 搭建）把 2021–2023 年 Geist 定下的「暖色 + 无衬线标题 + 衬线正文」骨架保留了下来，但字体已换成自有命名的 Anthropic Sans / Serif / Mono，调色板扩展成一整套以纸张、陶土、植物命名的色卡。首屏没有任何渐变、光效或 3D：左边一句 64px 粗体无衬线标题（关键词加下划线做链接），右边一段衬线导语，下面一张 16px 圆角的大幅带颗粒感的天空画面。高级感来自克制：一种底色、一种墨色、极少的强调色、极大的留白。

## Colors（全部读自主样式表的 `--swatch--*` 变量）

| Name | Value | Role |
|---|---|---|
| Ivory Medium | `#f0eee6` | 首屏画布（截图取色实测） |
| Ivory Light | `#faf9f5` | 默认主题背景 / 深色区块上的文字 |
| Ivory Dark | `#e8e6dc` | 卡片、次级面 |
| Slate Dark | `#141413` | 正文、标题、主按钮底 |
| Slate Medium / Light | `#3d3d3a` / `#5e5d59` | 按钮 hover / 次级文字、链接 hover |
| Clay | `#d97757` | 品牌陶土橙（插画与点缀） |
| Accent | `#c6613f` | 更深的强调橙 |
| Oat / Manilla / Kraft | `#e3dacc` / `#ebdbbc` / `#d4a27f` | 纸张系辅助底色 |
| Sky / Olive / Cactus / Heather / Fig / Coral | `#6a9bcc` `#788c5d` `#bcd1ca` `#cbcadb` `#c46686` `#ebcece` | 插画与分类用的低饱和辅色 |
| Border | `#1414131a`（hover `#14141333`） | 线：墨色 10% / 20% 透明 |

## Typography

- 真实加载：`Anthropic Sans`（可变字重 300–800，标题与 UI）、`Anthropic Serif`（300–800，正文与导语）、`Anthropic Mono`、另有 `JetBrains Mono` 400。回退分别是 Arial / Georgia。
- H1（`.u-display-xl`）：Anthropic Sans，4rem（64px），字重 700，行高 1.1，字距 0，`text-wrap: balance`。
- 展示字号阶梯：6 / 4.5 / 4 / 3 / 2 / 1.5 / 1.25rem；段落 1.5 / 1.25 / 1.125 / 1rem；细节文字 1.25–0.75rem。
- 行高档位 1 / 1.05 / 1.1 / 1.3 / 1.4 / 1.5；字距只有 0、-0.005em、-0.02em 三档——几乎不调字距。
- 每种字体都定义了上下 text-trim 值（如 Sans 上 .34em 下 .4em），用来把文字盒裁到字面，保证与图片、线条的光学对齐。
- 注：Geist 案例页与 type.today 记载的是早期的 Styrene + Tiempos；现站 CSS 中未读到这两个字体名。

## Shapes & Motion

- 圆角四档：4px / 8px（最常用）/ 16px（大图、卡片）/ 100vw（胶囊）。
- 阴影极淡且多层叠加：`0 2px 2px #00000003, 0 4px 4px #00000005, 0 16px 24px #0000000a`；大多数面根本没有阴影，靠底色差与 10% 墨线分层。
- 栅格：12 列，页边距 64px，列间距 2rem，最大宽度 89.5rem；区块间距 10rem 为常态（另有 4 / 6 / 14rem），页顶留白 12rem。
- 动效：几乎全是 `.2s` 的颜色 / 边框色 / 下划线色过渡；缓动只读到一条 `cubic-bezier(.165,.84,.44,1)`（ease-out-quart）。没有在样式表里读到滚动视差或大位移动画。

## Signature（签名手法）

1. **左粗黑、右衬线的「对开」首屏**：同一水平带里，左 7 列放 64px 粗体标题，右 5 列放 24px 衬线导语，垂直居中对齐；没有按钮、没有副标题徽章。
2. **标题内的下划线即导航**：H1 里的关键词直接是链接，用粗下划线标出，hover 只改下划线颜色——把 CTA 融进句子里。
3. **纸张命名的色卡**：底色不是白而是象牙，辅色全是低饱和的陶土、燕麦、牛皮纸、橄榄；强调橙只在小面积出现。
4. **带颗粒的大幅画面 + 16px 圆角**，满栅格宽，和文字区之间留 100px 以上的空。

## 迁移到半人马AI学院

- **借**：象牙底 `#f0eee6`/`#faf9f5` + 墨色 `#141413` 的双色骨架；对开首屏；标题内下划线链接；10rem 区块留白；10% 墨线代替阴影。logo 的橙可对位 Clay `#d97757`，蓝可对位 Sky `#6a9bcc`，刚好是它现成的辅色关系。
- **补**：Anthropic Sans/Serif 是自有字体，不可用。中文建议标题用思源黑体 Heavy / 阿里巴巴普惠体 Bold，导语与正文用思源宋体（均免费可商用）；西文可配 Inter + Source Serif。三张暖色插画需统一加颗粒、统一 16px 圆角，再补 2–3 张同风格的大幅横图。
- **风险**：这套风格靠「少」成立，学院页若堆课程卡、价格、二维码会立刻变廉价；中文粗黑体在 64px 下比西文更重，需降到 600 字重或 56px；配色与 Anthropic/Claude 辨识度很高，强调色与插画必须用自己的橙蓝折纸语言，避免像仿站。

## Sources

- https://www.anthropic.com （首页 HTML，2026-09-17）
- https://cdn.prod.website-files.com/67ce28cfec624e2b733f8a52/css/ant-brand.shared.3fb5bf118.min.css
- https://geist.co/work/anthropic
- https://type.today/en/journal/anthropic
- https://abduzeedo.com/seamlessly-crafting-ai-branding-and-visual-identity-anthropic
