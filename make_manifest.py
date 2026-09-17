#!/usr/bin/env python3
"""Turn the workflow journal (structured agent results) into manifest.json for build_gallery.py."""
import json, sys, pathlib
journal = pathlib.Path(sys.argv[1]); labels = {}; cands = {}; judge = {}
for line in journal.read_text().splitlines():
    try: e = json.loads(line)
    except ValueError: continue
    if e.get('type') == 'started': labels[e['key']] = e.get('label', '')
    elif e.get('type') == 'result' and isinstance(e.get('result'), dict):
        kind, _, slug = labels.get(e['key'], '').partition(':'); r = e['result']
        if kind == 'build': cands.setdefault(slug, {}).update(r, slug=slug)
        elif kind == 'art-direct': cands.setdefault(slug, {'slug': slug})['review'] = r
        elif kind == 'judge': judge = r
out = {'candidates': [cands[k] for k in sorted(cands)], 'judge': judge}
(pathlib.Path(__file__).parent/'manifest.json').write_text(json.dumps(out, ensure_ascii=False, indent=2))
print('candidates:', len(cands), '| reviewed:', sum('review' in c for c in cands.values()), '| judged:', bool(judge))
