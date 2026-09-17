# Mistral AI — Style Reference

> 近黑画布上铺一块会呼吸的橙红像素地毯，角落蹲一只像素黑猫。

**Theme:** Dark（另有 cream 浅色主题 token）· 像素模块 / 暖橙色阶

整站是「冷静的工程骨架 + 一块滚烫的色块」。导航、分栏、卡片全部用 1px 细线切成硬边格子，几乎不用阴影和大圆角；所有情绪都交给首屏那片由黄→橙→红→树莓红方块拼成的动态马赛克。Logo 的 M 由同样的方块堆成，像素猫与各模型小图标也出自同一套单元，所以品牌从 16px favicon 到整屏 hero 是同一种语法。等宽小字标签（全大写）钉在网格交点旁，像工程图的标注。

## Colors（均读自 `/_astro/astro.*.css` 的 CSS 变量）

| Name | Value | Role |
|---|---|---|
| steel-950 | `#101013` | 深色主题画布（surface-brand-primary） |
| steel-900 | `#1a1a1e` | 次级面板（首屏右栏） |
| border | `#31313a` | 1px 分隔线 / 格线（浅色主题为 `#e4e3de`） |
| cream-50 | `#fafaf4` | 深色下正文字色；浅色主题画布近似 `#fbfbf8` |
| steel-400 | `#a1a1aa` | 弱化文字、eyebrow |
| orange-500 | `#ff5229` | 品牌主橙（orange-strong / surface-brand） |
| orange-600 | `#fa500f` | 马赛克底色橙 |
| tangerine-500 | `#ff8204` | 中橙 |
| yellow-500 | `#ffaf01` | 亮黄（色阶最亮端） |
| red-600 | `#e51300` | 红 |
| raspberry-700 | `#c4001d` | 色阶最深端 |
| blue-600 | `#0082e6` | 少量辅助强调（text-brand-2） |

## Typography

- **ALTMistral**（自托管定制家族，400/500/600 + 斜体，`--font-mistral`）：标题与正文。出品字库未能从源码读到，不写。
- **Space Mono** 400（`--font-mono`）：全大写 eyebrow、按钮小字、网格标注。
- **Inter** 可变字体（`--font-inter`）：备用。
- Display：6rem / 行高 6rem / 500 / -0.02em（移动端 2.5rem/3rem）。
- H1：4.5rem / 4.5rem / 500 / -0.02em（移动端 2.5rem/3rem）；H2 3.5rem/3.75rem，-0.01em。
- 正文 1rem/1.5rem，-0.01em；大正文 1.25rem/1.75rem，-0.02em；eyebrow 0.75–0.8125rem，字距 0。
- 标题一律 Medium(500)，不用粗体——靠字号和紧行高出气势。

## Shapes & Motion

- 圆角：Tailwind 默认阶，实际用量 rounded-md(6px) 55 次、rounded-sm(4px) 44 次、rounded-lg(8px) 13 次；大圆角几乎不出现。导航项是直角满高格。
- 阴影：基本不用；仅见一处 `3px 3px #5a5a5ab3` 的硬边像素投影（无模糊）。
- 栅格：全宽，1px 线分栏（首屏约 70/30 左右分），container 上限 72rem；间距基数 0.25rem。
- 动效：品牌方块入场 `.7s ease-out`，分 0.1s–2s 错峰从各方向滑入；hero 方块 4s ease-in-out 无限循环换位；通用过渡 duration-300 占绝对多数，曲线 `cubic-bezier(.4,0,.2,1)`；弹出用回弹 `cubic-bezier(.68,-.55,.27,1.55)`。

## Signature

1. **单元延展**：Logo = 方块；图标、吉祥物、hero 背景、加载态全用同一方块单元，缩到 16px 也成立。
2. **一段连续暖色阶**（黄→橙→红→树莓红共 5–6 档）只用于色块，不用于文字和 UI 控件；UI 保持黑/灰/米白。
3. **线框格子 + 等宽标注**：1px 线把页面切成工程图，Space Mono 全大写小字贴在交点旁，交点放小黑方点。
4. **硬边到底**：无渐变、无模糊阴影、无大圆角；连投影都是像素位移。

## 迁移到半人马AI学院

- **借**：把低多边形半人马拆成「三角面片」作为构成单元，延展成课程图标、分隔纹样、hero 动态马赛克；橙做 5 档连续色阶，蓝只留 1–2 档做对位；1px 线框格 + 等宽标注的工程感骨架；标题 500 字重、-0.02em、行高≈字号。
- **需要补**：一套三角面片图标/插画（需设计师或脚本生成）；ALTMistral 是定制字体不可用，中文可用思源黑体/阿里巴巴普惠体 Medium 顶替，标注用 Space Mono（OFL）或 JetBrains Mono。
- **风险**：像素/面片风一旦单元不统一就显廉价；深色 + 高饱和橙对经营者人群偏「技术公司」，建议以 cream 浅色主题为主、橙色块限量；中文无等宽气质，标注只用英文/数字。

## Sources

- https://mistral.ai （首页 HTML 与 `/_astro/astro.DkG4wX1c.css`，2026-09-17 抓取）
- https://mistral.ai/brand/ （官方品牌页：M 标、像素猫、模型像素插画的说明）
- https://www.underconsideration.com/brandnew/archives/new_logo_and_identity_for_mistral_ai_by_sylvain_boyer_studio.php （Brand New，Noted，2025-02-11；正文在订阅墙后）
- https://www.creativereview.co.uk/mistral-ai-design-sylvain-boyer/ （Creative Review，2025-03-11，Jean Grogan；部分付费墙）
