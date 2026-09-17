#!/usr/bin/env python3
"""Build references/index.html from references/manifest.json (workflow output) + references/<slug>/fold.png."""
import json, html, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).parent; REF = ROOT/'references'
BLOB = 'https://github.com/QiuQiuNB666/centaur-academy-styles/blob/main/references/'
m = json.loads((REF/'manifest.json').read_text()); e = html.escape
cards = []
for r in m['references']:
    d = REF/r['slug']; shot = d/'fold.png'; thumb = d/'fold.webp'
    if r.get('screenshot_ok') and shot.exists():
        im = Image.open(shot).convert('RGB'); im.thumbnail((960, 100000)); im.save(thumb, 'WEBP', quality=80, method=6)
    img = f'<img src="{r["slug"]}/fold.webp" alt="{e(r["name"])} 首屏" loading="lazy" width="960" height="600">' if thumb.exists() else '<span>未能截到首屏，请直接打开原站</span>'
    rec = ''.join(f'<li><a href="{e(x["url"])}" target="_blank" rel="noopener noreferrer">{e(x["source"])}</a> — {e(x["detail"])}{(" · " + e(x["year"])) if x.get("year") else ""}</li>' for x in r['recognition_verified'])
    if not rec: rec = '<li class="warn">背书未能独立核实，仅作风格参考</li>'
    chips = ''.join(f'<li title="{e(p["name"])}：{e(p["role"])}"><i style="background:{e(p["hex"])}"></i><code>{e(p["hex"])}</code></li>' for p in r['palette'] if p['hex'].startswith('#'))
    sig = ''.join(f'<li>{e(s)}</li>' for s in r['signature'])
    agency = f'<p class="line"><b>操刀</b>{e(r["agency"])}</p>' if r.get('agency') else ''
    style_md = f'<a href="{BLOB}{r["slug"]}/STYLE.md">风格档案</a>' if (d/'STYLE.md').exists() else ''
    note = f'<p class="shotnote">{e(r["shot_note"])}</p>' if r.get('shot_note') else ''
    cards.append(f'''<article class="card" id="{e(r["slug"])}"><a class="shot" href="{e(r["url"])}" target="_blank" rel="noopener noreferrer">{img}</a><div class="meta">
{note}<p class="no">{e(r["family"])}</p><h2>{e(r["name"])}</h2>
<h3>公开背书（均已点开核实）</h3><ul class="rec">{rec}</ul>{agency}
<h3>它高级在哪</h3><ul class="sig">{sig}</ul>
<ul class="chips">{chips}</ul><p class="line"><b>字体</b>{e(r["fonts"])}</p><p class="line"><b>字号</b>{e(r["type_notes"])}</p><p class="line"><b>形与动</b>{e(r["shape_motion"])}</p>
<h3>搬到半人马学院</h3><p class="transfer">{e(r["transfer"])}</p>
<nav><a class="go" href="{e(r["url"])}" target="_blank" rel="noopener noreferrer">打开原站 ↗</a>{style_md}</nav></div></article>''')
dropped = ''.join(f'<li>{e(x)}</li>' for x in m.get('dropped_notable', []))
page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>公认高级的参考站 · 半人马AI学院</title><meta name="description" content="有公开奖项或行业背书的真实网站，逐个核实后供挑选美术范式。">
<style>
:root{{--bg:#f3f3f1;--ink:#1b1c1e;--mute:#5f6166;--line:#dcdcd8;--card:#fff}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",system-ui,sans-serif}}
main{{width:min(1240px,100% - 40px);margin:0 auto;padding-block:56px 96px}}h1{{font-size:clamp(1.6rem,3.4vw,2.4rem);line-height:1.25;margin:0 0 12px}}
header p{{margin:0 0 8px;color:var(--mute);max-width:48em}}header a{{color:var(--ink)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,520px),1fr));gap:28px;margin-top:40px}}
.card{{background:var(--card);border:1px solid var(--line);display:flex;flex-direction:column}}
.shot{{display:grid;place-items:center;aspect-ratio:16/10;overflow:hidden;background:#e9e9e6;border-bottom:1px solid var(--line);color:var(--mute);font-size:.875rem;text-decoration:none}}.shot img{{display:block;width:100%;height:100%;object-fit:cover;object-position:top}}
.shotnote{{margin:0 0 4px;font-size:.8125rem;color:var(--mute);border-left:2px solid var(--line);padding-left:10px}}.meta{{padding:22px 24px 24px;display:flex;flex-direction:column;gap:8px;flex:1}}.no{{margin:0;font:12px/1 ui-monospace,Menlo,monospace;color:var(--mute);letter-spacing:.08em}}
h2{{margin:0;font-size:1.5rem;line-height:1.3}}h3{{margin:10px 0 0;font-size:.8125rem;letter-spacing:.06em;color:var(--mute);font-weight:600}}
ul{{margin:0;padding-left:1.15em}}.rec li,.sig li{{font-size:.9375rem;margin:3px 0}}.rec a{{color:var(--ink);font-weight:600;text-underline-offset:3px}}.warn{{color:#9a3b1f}}
.chips{{list-style:none;display:flex;flex-wrap:wrap;gap:6px 12px;margin:10px 0 2px;padding:0}}.chips li{{display:flex;align-items:center;gap:6px}}.chips i{{width:18px;height:18px;border-radius:50%;border:1px solid rgba(0,0,0,.12)}}.chips code{{font:12px ui-monospace,Menlo,monospace;color:var(--mute)}}
.line{{margin:0;font-size:.875rem;color:var(--mute)}}.line b{{display:inline-block;min-width:3.6em;color:var(--ink);font-weight:600}}.transfer{{margin:0;font-size:.9375rem}}
nav{{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:auto;padding-top:12px;font-size:.9375rem}}nav a{{color:var(--ink);text-underline-offset:4px;min-height:44px;display:inline-flex;align-items:center}}nav .go{{font-weight:600}}
a:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}details{{margin-top:48px;color:var(--mute);font-size:.9375rem}}summary{{cursor:pointer;color:var(--ink)}}footer{{margin-top:32px;color:var(--mute);font-size:.875rem}}
</style></head><body><main>
<header><h1>公认高级的参考站</h1><p>这一页只收真实存在、现在能打开的网站，每个都有可以点开的公开背书（奖项页、权威设计媒体评论或操刀机构的案例页），背书由另一个 agent 独立点开核实过，对不上的已删掉。色值和字体是从它们的真实 CSS 里读出来的。缩略图只是首屏截图，<b>一定要点开原站滚一滚</b>，高级感一大半在排版节奏和动效里。</p>
<p>从 {m.get("pool_size","?")} 个候选里策展出 {len(m["references"])} 个，<b>按「学院现有素材能搬多少」从易到难排序</b>。挑中 1–2 个告诉我，我再严格照着它给学院做完整的 DESIGN.md 和首页。<a href="../">← 回到第一轮的六套自拟方案</a></p></header>
<section class="grid">{"".join(cards)}</section>
<details><summary>有名但这次没选的</summary><ul>{dropped}</ul></details>
<footer>缩略图版权归各站所有，仅用于本次内部选型参考。</footer></main></body></html>'''
(REF/'index.html').write_text(page); print('references page:', len(m['references']), 'sites')
