# Shopify Editions Winter '26 — The Renaissance Edition — Style Reference

> 一本「版本刊」：黑场开幕，奶油纸页上排满更新清单，章节之间挂古典油画。

**Theme**：产品发布刊 / 古典绘画 × 现代排版（开场黑底，正文奶油底）

Shopify 把半年 150+ 条产品更新做成一期有主题的刊物。开场是纯黑底上的黄金分割构图线 + 居中标题锁定（标题里的 "ai" 换成花体字，一语双关）；进入正文后切到奶油纸色，粗无衬线章节大标题、衬线体叙述句、Inter 小标签三种声音分工明确。全站只有两个主色加三级橄榄灰，没有任何彩色强调——颜色全部让给插画。

## Colors（读自 tailwind-G-N6aznT.css 的具名类）

| Name | Value | Role |
|---|---|---|
| light | `#F7F7EE` | 正文画布（HTML 中 bg-light 133 次，最多）；黑场上的文字色 |
| dark | `#292919` | 正文文字（text-dark 165 次）；深色章节底（bg-dark 33 次） |
| black | `#000000` | body 底色与开场 hero（浏览器实测 body = rgb(0,0,0)） |
| grey-light | `#DCDCD0` | 发丝分隔线（border-grey-light 59 次） |
| grey-mid | `#909083` | 次要文字 / 元信息（text-grey-mid 137 次） |
| grey-dark | `#5C5C4E` | 深底上的次级文字与边线 |
| white | `#FFFFFF` | 仅导航胶囊按钮等少量控件 |

灰阶全部带黄绿底调（橄榄灰），没有一个中性灰。焦点环 `#57AFDF` 只用于无障碍。

## Typography（读自 fonts-latin-CzfLCQn_.css + 浏览器 document.fonts 实测）

- **标题：NeueMontreal 700**（Pangram Pangram 出品，商业授权）。`.headline-1`：72px → 桌面 `clamp(7.5rem, 35.79px + 10.96vw, 13.75rem)`（120–220px），行高 0.9，字距 -0.03em，`text-wrap:pretty` + `text-box:trim-both cap alphabetic`。headline-4 = 32px / 0.95 / -0.03em。
- **叙述：HWCigars 400**（衬线，开了 liga/dlig/smcp 特性）。`.narrative-1`：28px → `clamp(2rem,…,3rem)`，行高 0.96，字距 -0.05em——衬线体也压得很紧。
- **花体：ImperialScript 400**，`.script-1` 70px / 0.96 / -0.02em，只做点睛（标题里的 "ai"）。
- **标签/UI：Inter-Variable**，11–16px，行高 100–120%，字距 0，部分全大写。
- 日文版回退 NotoSansJP；没有中文字体方案。

## Shapes & Motion

- 圆角：大面积 `border-radius:0`；小控件 3–4px；按钮/标签用全圆胶囊（rounded-full）。
- 阴影：基本没有（除焦点环外只有一处粒子光晕）。层次靠发丝线和底色切换。
- 栅格：12 列为主，另有 2 / 5 / 6 列与 subgrid；章节标题上下留白用 vh（11vh–35vh），每章位置刻意不同。
- 动效：过渡多为 .3s / .6s；曲线有 `cubic-bezier(.72,.16,.19,.96)`（主入场）、`(.34,1.56,.64,1)`（回弹）、`(.41,.19,.13,.95)`。页面含 2 个 canvas（WebGL 转场）；类名带 `motion-safe:`，尊重减少动效设置。

## Signature（签名手法）

1. **两色 + 同色相灰阶**：奶油 / 橄榄黑 + 三级橄榄灰，颜色预算全部留给绘画。
2. **三种字体三种声部**：巨型紧排无衬线喊章节名，衬线体讲故事，Inter 小字做清单标签；花体只出现一两次。
3. **标题行高 0.9 + text-box trim**：大字顶天立地贴着构图线，像印刷品而不是网页。
4. **黑场开幕 → 纸页正文**：先用黄金分割构图线建立「古典」语境，再进入高密度清单。

## 迁移到半人马AI学院

- **借**：`#F7F7EE / #292919 / #DCDCD0 / #909083` 这套带色温的两色灰阶；标题 0.9 行高 + 负字距；「章节大标题 + 衬线引语 + 小标签清单」的三声部编排；0 圆角 + 发丝线 + 胶囊按钮；黑场开幕只放 logo 与一句主张。
- **补**：NeueMontreal / HWCigars 均为商业字体，需购买授权或换替代（无衬线可用 Inter Tight / 思源黑体 Heavy，衬线用思源宋体 / Noto Serif SC）。中文没有花体对应物，"ai" 式双关要另想。学院只有 1 张 3D 主视觉 + 3 张插画，撑不起 11 个章节的绘画量。
- **风险**：中文大字行高 0.9 会挤（建议 1.05–1.15）；橙蓝 logo 放在橄榄奶油底上色温要试；去掉 WebGL 和成套绘画后，剩下的只是「干净」，需要靠排版密度和章节节奏补足。

## Sources（均已亲自打开核实）

- https://www.shopify.com/editions/winter2026 （HTTP 200；CSS：cdn.shopify.com/oxygen-v2/…/tailwind-G-N6aznT.css、fonts-latin-CzfLCQn_.css）
- https://www.awwwards.com/sites/the-renaissance-edition （SOTD 2026-02-09，7.92；Dev Award 8.05）
- https://winners.webbyawards.com/winners/websites-and-mobile-sites/features-design/best-visual-design-aesthetic （渲染后 DOM 含 "The Renaissance Edition … People's Voice Winner, 2026 Shopify"）
- 截图说明：fold.png 为无头 Chrome 拍到的开场黑场帧（构图线 + 标题），未能拍到奶油正文页（WebGL/滚动驱动，4 次尝试均停在开场）。
