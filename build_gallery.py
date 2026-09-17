#!/usr/bin/env python3
"""Regenerate index.html + README.md from styles/*/ (DESIGN.md, tokens.css, shot-*.png) and optional manifest.json."""
import json, re, html, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).parent
PAGES = 'https://qiuqiunb666.github.io/centaur-academy-styles/'
BLOB = 'https://github.com/QiuQiuNB666/centaur-academy-styles/blob/main/'
PLAN = [  # slug, 中文名, 一句话方向（方案未完成时显示）
  ('01-paper-journal', '纸上学刊', '现站方向的精修版：暖纸、宋体，靠真实刊物版式取胜'),
  ('02-ink-seal', '墨与印', '新中式留白：宣纸白、墨色层次、朱砂印一点'),
  ('03-swiss-grid', '瑞士网格', '国际主义平面：纯白、近黑、钴蓝单信号色，可见网格'),
  ('04-boardroom', '董事会深蓝', '商学院式权威：深海军蓝、象牙白、黄铜细线'),
  ('05-night-precision', '夜航精密', '深色精密：近黑画布、发丝线、logo 橙唯一强调'),
  ('06-origami-block', '折纸色块', '从 logo 长出来：钴蓝与橘橙大色块、折纸切面'),
]
manifest = json.loads((ROOT/'manifest.json').read_text()) if (ROOT/'manifest.json').exists() else {}
cands = {c['slug']: c for c in manifest.get('candidates', [])}
judge = {r['slug']: r for r in manifest.get('judge', {}).get('ranking', [])}

def webp(src, dst, width):
    if not src.exists(): return False
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime: return True
    im = Image.open(src).convert('RGB'); im.thumbnail((width, 100000)); im.save(dst, 'WEBP', quality=82, method=6); return True

def tokens(d):
    css = (d/'tokens.css').read_text() if (d/'tokens.css').exists() else ''
    out = []
    for name, val in re.findall(r'--color-([a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{3,8})\s*;', css):
        if val.lower() not in [v.lower() for _, v in out] and not name.endswith('-foreground'): out.append((name, val))
    return out[:7]

rows = []
for slug, zh, plan in PLAN:
    d = ROOT/'styles'/slug; ready = (d/'index.html').exists() and (d/'DESIGN.md').exists()
    item = dict(slug=slug, zh=zh, plan=plan, ready=ready)
    if ready:
        md = (d/'DESIGN.md').read_text()
        t = re.search(r'^>\s*(.+)$', md, re.M); item['tagline'] = (cands.get(slug, {}).get('tagline') or (t.group(1).strip() if t else plan))
        th = re.search(r'\*\*Theme:\*\*\s*(\w+)', md); item['theme'] = th.group(1) if th else ''
        c = cands.get(slug, {})
        item['zh'] = c.get('name_zh') or zh
        item['palette'] = [(p['name'], p['hex']) for p in c.get('palette', [])] or tokens(d)
        item['fonts'] = c.get('fonts', ''); item['signature'] = c.get('signature', '')
        item['anchors'] = [a['brand'] for a in c.get('anchors', [])]
        item['fits'] = judge.get(slug, {}).get('fits', ''); item['cost'] = judge.get(slug, {}).get('cost', ''); item['rank'] = judge.get(slug, {}).get('rank')
        item['thumb'] = webp(d/'shot-fold.png', d/'thumb.webp', 1200)
        item['mobile'] = webp(d/'shot-mobile.png', d/'thumb-mobile.webp', 480)
        item['kit'] = (d/'kit.html').exists()
        item['draft'] = not bool(c.get('review'))
    rows.append(item)

e = html.escape
def rich(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', e(t))
    out, items = [], []
    for line in [l.strip() for l in t.splitlines() if l.strip()]:
        if line.startswith('- '): items.append(f'<li>{line[2:]}</li>')
        else:
            if items: out.append('<ul>' + ''.join(items) + '</ul>'); items = []
            out.append(f'<p>{line}</p>')
    if items: out.append('<ul>' + ''.join(items) + '</ul>')
    return ''.join(out)
def card(i):
    base = f"styles/{i['slug']}/"
    if not i['ready']:
        return f'<article class="card pending"><div class="shot"><span>制作中</span></div><div class="meta"><h2>{e(i["zh"])}</h2><p class="tag">{e(i["plan"])}</p></div></article>'
    chips = ''.join(f'<li title="{e(n)} {e(h)}"><i style="background:{e(h)}"></i><code>{e(h)}</code></li>' for n, h in i['palette'])
    shot = f'<img src="{base}thumb.webp" alt="{e(i["zh"])} 首屏截图" loading="lazy" width="1200" height="750">' if i['thumb'] else '<span>预览</span>'
    extra = ''
    if i['signature']: extra += f'<p class="line"><b>记忆点</b>{e(i["signature"])}</p>'
    if i['fonts']: extra += f'<p class="line"><b>字体</b>{e(i["fonts"])}</p>'
    if i['anchors']: extra += f'<p class="line"><b>锚点</b>{e(" · ".join(i["anchors"]))}</p>'
    if i['fits']: extra += f'<p class="line"><b>适合</b>{e(i["fits"])}</p>'
    if i['cost']: extra += f'<p class="line"><b>代价</b>{e(i["cost"])}</p>'
    kit = f'<a href="{base}kit.html">组件样张</a>' if i['kit'] else ''
    return (f'<article class="card"><a class="shot" href="{base}">{shot}</a><div class="meta">'
            f'<p class="no">{e(i["slug"][:2])} · {e(i.get("theme",""))}{" · 初稿，美术总监审稿中" if i["draft"] else ""}{(" · 评审排序 " + str(i["rank"]) + "/6") if i.get("rank") else ""}</p><h2>{e(i["zh"])}</h2><p class="tag">{e(i["tagline"])}</p>'
            f'<ul class="chips">{chips}</ul>{extra}'
            f'<nav><a class="go" href="{base}">打开预览 →</a>{kit}<a href="{BLOB}styles/{i["slug"]}/DESIGN.md">DESIGN.md</a></nav></div></article>')

overall = manifest.get('judge', {}).get('overall', '')
order = [r['slug'] for r in sorted(manifest.get('judge', {}).get('ranking', []), key=lambda r: r['rank'])]
note = ''
if overall:
    names = {i['slug']: i['zh'] for i in rows}
    note = f'<aside><h3>横向评审的看法（独立评委 agent，仅供参考，你说了算）</h3>{rich(overall)}<p class="order">评审排序：{e(" → ".join(names.get(s, s) for s in order))}</p></aside>'

# --- round 3: one edition built strictly after references 2/3/4 ---
featured_v3 = ''
ED = ROOT/'edition'
if (ED/'final'/'index.html').exists():
    webp(ED/'final'/'shot-fold.png', ED/'final'/'thumb.webp', 1400)
    ed = json.loads((ED/'manifest.json').read_text()) if (ED/'manifest.json').exists() else {}
    summary = ed.get('refine', {}).get('summary', '')
    names = {b['key']: b['name_zh'] for b in ed.get('builds', [])}
    winner = ed.get('judge', {}).get('winner', '')
    drafts = ''.join(f'<a href="edition/{k}/">{e(names.get(k, k))}（{"胜出原稿" if k == winner else "落选草稿"}）</a>' for k in ('a-report', 'b-grid', 'c-edition') if (ED/k/'index.html').exists())
    featured_v3 = (f'<section class="v3"><a class="v3shot" href="edition/final/"><img src="edition/final/thumb.webp" alt="第三轮版本首屏截图" width="1400" height="875"></a>'
        f'<div class="v3meta"><p class="no">第三轮 · 照着参考 ②③④ 做的一版</p><h2>照着 AI in Design Report、Dropbox Brand、Shopify Editions</h2>'
        f'<p>{e(summary)}</p><nav><a class="go" href="edition/final/">打开这一版 →</a><a href="edition/final/kit.html">组件样张</a>'
        f'<a href="{BLOB}edition/final/DESIGN.md">DESIGN.md</a><a href="references/">三个参考站</a></nav>'
        f'<p class="drafts">同一轮的三个骨架原稿：{drafts}</p></div></section>')
done = sum(i['ready'] for i in rows)
page = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>半人马AI学院 · 美术范式候选</title><meta name="description" content="六套候选美术范式：每套含 DESIGN.md、首页预览与组件样张。">
<style>
:root{{--bg:#f3f3f1;--ink:#1b1c1e;--mute:#63656a;--line:#dcdcd8;--card:#fff}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",system-ui,sans-serif}}
main{{width:min(1240px,100% - 40px);margin:0 auto;padding-block:56px 96px}}
header h1{{font-size:clamp(1.6rem,3.4vw,2.4rem);line-height:1.25;margin:0 0 12px;letter-spacing:-.01em}}header p{{margin:0;color:var(--mute);max-width:46em}}header .round2{{margin-top:14px}}header .round2 a{{color:var(--ink);font-weight:600;text-underline-offset:4px}}.v3{{margin-top:36px;background:var(--card);border:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr)}}.v3shot{{display:block;overflow:hidden;border-right:1px solid var(--line);aspect-ratio:16/10}}.v3shot img{{display:block;width:100%;height:100%;object-fit:cover;object-position:top}}.v3meta{{padding:28px;display:flex;flex-direction:column;gap:12px}}.v3meta h2{{font-size:1.375rem}}.v3meta p{{margin:0;color:var(--mute)}}.v3meta .drafts{{font-size:.875rem}}.v3meta .drafts a{{color:var(--ink);margin-left:10px}}.r1{{margin:64px 0 0;font-size:1.25rem}}@media(max-width:860px){{.v3{{grid-template-columns:1fr}}.v3shot{{border-right:0;border-bottom:1px solid var(--line)}}}}
aside{{margin-top:28px;padding:18px 20px;border:1px solid var(--line);border-left:3px solid var(--ink);background:var(--card);font-size:.9375rem}}aside h3{{margin:0 0 6px;font-size:1rem}}aside p{{margin:6px 0 0;color:var(--mute)}}aside ul{{margin:8px 0 0;padding-left:1.2em;color:var(--mute)}}aside li{{margin:4px 0}}aside b{{color:var(--ink)}}aside .order{{color:var(--ink);margin-top:12px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,520px),1fr));gap:28px;margin-top:40px}}
.card{{background:var(--card);border:1px solid var(--line);display:flex;flex-direction:column}}
.shot{{display:block;aspect-ratio:16/10;overflow:hidden;background:#e9e9e6;border-bottom:1px solid var(--line)}}.shot img{{display:block;width:100%;height:100%;object-fit:cover;object-position:top;transition:transform .5s cubic-bezier(.23,1,.32,1)}}
@media(hover:hover) and (pointer:fine){{.card a.shot:hover img{{transform:scale(1.015)}}}}@media(prefers-reduced-motion:reduce){{.shot img{{transition:none}}}}
.pending .shot{{display:grid;place-items:center;color:var(--mute);font-size:.875rem;letter-spacing:.2em}}
.meta{{padding:22px 24px 24px;display:flex;flex-direction:column;gap:10px;flex:1}}.no{{margin:0;font:12px/1 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mute);letter-spacing:.08em;text-transform:uppercase}}
h2{{margin:0;font-size:1.5rem;line-height:1.3}}.tag{{margin:0;color:var(--mute)}}
.chips{{list-style:none;display:flex;flex-wrap:wrap;gap:6px 12px;margin:4px 0;padding:0}}.chips li{{display:flex;align-items:center;gap:6px}}.chips i{{width:18px;height:18px;border-radius:50%;border:1px solid rgba(0,0,0,.12)}}.chips code{{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mute)}}
.line{{margin:0;font-size:.875rem;color:var(--mute)}}.line b{{display:inline-block;min-width:3.6em;color:var(--ink);font-weight:600}}
nav{{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:auto;padding-top:14px;font-size:.9375rem}}nav a{{color:var(--ink);text-underline-offset:4px;min-height:44px;display:inline-flex;align-items:center}}nav .go{{font-weight:600}}
a:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}footer{{margin-top:56px;color:var(--mute);font-size:.875rem}}
</style></head><body><main>
<header><h1>半人马AI学院 · 美术范式候选</h1><p>同一份首页文案、同一批插画，六种美术范式。每套都有完整的 DESIGN.md（色板、字体、间距、组件、Do / Don't、Agent Prompt Guide）、可滚动的首页预览和一页组件样张。当前完成 {done} / {len(rows)}。</p><p class="round2"><a href="references/">第二轮：有奖项和行业背书的真实高级参考站 →</a></p></header>{featured_v3}<h2 class="r1">第一轮 · 六套自拟方案</h2>{note}
<section class="grid">{''.join(card(i) for i in rows)}</section>
<footer>挑中哪套告诉我编号即可；也可以混搭（例：02 的版式 + 04 的配色）。预览页左下角「← 全部方案」返回这里。</footer>
</main></body></html>'''
(ROOT/'index.html').write_text(page)

md = ['# 半人马AI学院 · 美术范式候选', '', f'在线挑选：**{PAGES}**', '', '同一份首页文案、同一批插画，六种美术范式。每套含 `DESIGN.md`、`tokens.css`、首页预览 `index.html`、组件样张 `kit.html`。', '']
if overall: md += ['**横向评审（独立评委 agent，仅供参考）**', ''] + [('> ' + l if l.strip() else '>') for l in overall.splitlines()] + ['', '评审排序：' + ' → '.join({i['slug']: i['zh'] for i in rows}.get(x, x) for x in order), '']
if featured_v3: md += ['## 第三轮 · 照着参考 ②③④ 做的一版', '', f'[打开]({PAGES}edition/final/) · [组件样张]({PAGES}edition/final/kit.html) · [DESIGN.md](edition/final/DESIGN.md) · [三个参考站]({PAGES}references/)', '', '## 第一轮 · 六套自拟方案', '']
md += ['| # | 范式 | 一句话 | 预览 | 样张 | 范式文档 |', '|---|---|---|---|---|---|']
for i in rows:
    if i['ready']: md.append(f"| {i['slug'][:2]} | **{i['zh']}** | {i['tagline']} | [打开]({PAGES}styles/{i['slug']}/) | [kit]({PAGES}styles/{i['slug']}/kit.html) | [DESIGN.md](styles/{i['slug']}/DESIGN.md) |")
    else: md.append(f"| {i['slug'][:2]} | {i['zh']} | {i['plan']}（制作中） | — | — | — |")
md += ['', '## 目录', '', '```', 'assets/            共用图片（WebP；academy-centaur-cutout 为透明底抠图版）', 'styles/<编号>/     DESIGN.md · tokens.css · index.html · kit.html · thumb*.webp', 'build_gallery.py   由各方案目录重新生成本页与 index.html', '```', '']
(ROOT/'README.md').write_text('\n'.join(md))
print(f'gallery: {done}/{len(rows)} ready')
