# IZANAMI（baqemono.inc.，日本） — Style Reference
> 雾里只放一行小字：用「小」和「空」而不是「大」来制造分量。

**Theme:** 暗色（近黑画布 + 暖灰白文字），首屏为全幅雾中针叶林影像。

IZANAMI 是一家横跨东京与迪拜的生活方式品牌官网，业务为 School / Craft / Retreat 三线。整站只有两个颜色变量在干活，全部衬线字体、全部 400 字重、零字距调整、几乎零圆角零阴影；层级完全靠字号阶梯、行高两档（1 与 1.8）和大面积留空拉开。首屏 H1 实测只有约 20px，孤零零放在左侧 1/6 处——这是它最反直觉也最值得学的一点。
**更正发现者的描述：**首屏底图是雾中森林而非云；首页 HTML 里「和」只作为正文中的一个行内字（带 `lang="ja"`）出现，我没有在 DOM/CSS 中读到一个「巨大的和字」元素，若内页有大字也应是图像或 WebGL 绘制，未能核实。

## Colors（全部来自 `:root` 变量）
| Name | Value | Role |
|---|---|---|
| Black | `#0A0801` | 画布（body 背景），带一点暖的近黑 |
| White | `#D9D7D4` | 正文与界面文字，暖灰白 |
| White Pure | `#FFFFFF` | 仅首屏 H1 等压在影像上的文字 |
| Black Pure | `#000000` | 已定义，极少使用 |
| Hairline | `rgba(217,215,212,.2)` | 分隔线/边框（另有 .4 一档） |
| Yellow | `#CAA100` | 唯一彩色，只用于表单报错边框与提示 |

## Typography
- 字体由 JS 注入 Google Fonts：`Cinzel`（标签/导航/时钟，小型大写感）、`Playfair Display`（英文标题与口号）、`Shippori Mincho`（日文明朝体正文与标题）。三者均为 SIL OFL 开源。body 回退为 Helvetica Neue / Hiragino 系统黑体。JS 中还出现 use.typekit.net 字样，但未读到具体 kit。
- 字重：全站 `font-weight:400`（30 处），几乎不用粗体。`letter-spacing` 在样式表中出现 0 次。
- 字号全部 `clamp(0.75x, vw, 1.125x)` 流体：50 档 = `clamp(37.5px,3.125vw,56.25px)`，30 档 = `clamp(22.5px,1.875vw,33.75px)`，20 档 = `clamp(15px,1.25vw,22.5px)`，最小 14 档。
- 首页 H1：Playfair Display 400，20 档（1440 宽下约 18–20px），`line-height:1`，纯白。内页 H1 是 Cinzel 20 档的小标签，真正的大句子用 50 档的 `<p>`。
- 行高只有两种性格：标题 `1`，日文/英文段落 `1.8`（少量 2 / 2.4）。

## Shapes & Motion
- 圆角：只有 `50%`（小圆点、圆形按钮）和 `0`；另有一处 `3.125vw` 胶囊。`box-shadow`：未读到（0 处）。
- 栅格：全部用 vw 计量。常见 `grid-template-columns:12.5vw 1fr`、`32.5vw 1fr`，以及 32/36 等分细栅格；内容左缩进反复出现 `14.93vw`（约 1/6.7 屏宽）与 `12.5vw`，移动端 gutter `5vw`。断点只有 768px 一个。
- 动效：GSAP（ScrollTrigger + SplitText）+ Lenis 平滑滚动 + swup 页面过渡 + OGL（轻量 WebGL）。缓动以 `expo.out`、`quart.out`、`cubic.out` 为主，时长集中在 `1.4s` 与 `0.7s`——慢、长、只减速不回弹。CSS 侧仅 `opacity .4s linear`。
- 有进场 loader（0→100 计数）；无头浏览器的虚拟时间会卡在 loader，需真实时钟才能截到首屏。

## Signature（签名手法）
1. **反向层级**：首屏只放一句约 20px 的衬线小字，位于左侧约 17% 处垂直居中，其余 95% 画面留给影像。分量来自孤立，不来自字号。
2. **三衬线分工、单字重**：Cinzel 管标签、Playfair 管英文句子、明朝体管日文；全 400、零字距，靠字体性格而非粗细分层。
3. **两色 + 一条 20% 透明发丝线**：彩色被压到只剩报错黄，画面里任何彩色都会成为焦点。
4. **四角钉住的界面**：logo 左上、语言/菜单右上、版权与两地实时时钟左下、scroll 右下，中间完全放空；小圆点作为可点击标记。

## 迁移到半人马AI学院
- **借什么**：两色变量体系 + 20% 发丝线；vw 流体字号阶梯与「标题行高 1 / 正文 1.8」两档；四角钉住的 chrome；左缩进约 15vw 的不对称版心；「小字 + 大空」的首屏。橙蓝半人马 logo 正好占据它空出来的唯一彩色位。三条业务线的编号分节（01/02/03）可直接对应 课程 / 共学 / 社群。
- **需要补什么**：中文无 Shippori Mincho，可用思源宋体 / Noto Serif SC（OFL，免费）400 字重替代，英文沿用 Playfair Display + Cinzel（均 OFL，无需授权费）；若想要更精的中文宋体（方正/汉仪）需商用授权。首屏需要一张自有版权、低饱和、带颗粒的氛围影像或一张纸纹底图；无 WebGL 时用静态图 + 1.4s expo.out 的淡入位移即可。
- **风险**：这套语言偏「静修/疗愈」，对经营者受众可能显得太虚、信息密度太低，报名/课程信息必须另设高密度区块；暗底 + 400 细宋体在中文小字号下可读性差，正文建议不低于 16px 或改浅色纸底；「和字大锚点」我未能在源码核实，不要把它当作该站已验证的做法来宣传。

## Sources
- https://izanami-official.com/ （首页 HTML、/assets/css/index.By0AFpwc.css、/assets/js/index.PhJuwueo.js，2026-09-17 抓取）
- https://www.awwwards.com/sites/izanami （SOTD 2026-07-18，7.19；Developer Award 7.26）
- https://baqemono.jp/topics/ （制作方 2026.7.18 自述获奖）
- https://www.topcssgallery.com/gallery/izanami/ （画廊收录）
