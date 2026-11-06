"""library/index.json: every published OK pack, newest first - the page reads this one file and shows a button per pack.
Usage: python3 pipeline/index_packs.py   (run from the repo root by the publish step; also fine by hand)"""
import glob, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for p in sorted(glob.glob(os.path.join(ROOT, 'packs', '*', 'report.json'))):
    try: r = json.load(open(p))
    except Exception: continue
    if r.get('status') != 'OK' or not r.get('files'): continue
    d = os.path.basename(os.path.dirname(p)); lr = r.get('layers_real') or {}
    if not os.path.exists(os.path.join(ROOT, 'packs', d, r['files']['zip'])): continue
    rows.append(dict(id=d, artist=r.get('artist'), title=r.get('title'), zip=r['files']['zip'], oneshot=r['files']['oneshot'], pipeline=r.get('pipeline'), finished=r.get('finished'),
                     layers_real=lr, strategy=r.get('strategy_used', 'A_bright'), hits_aligned=(r.get('measurements') or {}).get('hits_aligned'),
                     realn=f"real hits in this pack: hard {lr.get('hard',0)}/4, medium {lr.get('medium',0)}/4, soft {lr.get('soft',0)}/4, ghost {lr.get('ghost',0)}/4; the rest are flagged estimates"))
rows.sort(key=lambda r: r.get('finished') or '', reverse=True)
# one pack per song (same artist+title): keep the newest
seen = set(); out = []
for r in rows:
    k = (str(r['artist']).lower(), str(r['title']).lower())
    if k in seen: continue
    seen.add(k); out.append(r)
os.makedirs(os.path.join(ROOT, 'library'), exist_ok=True)
json.dump(dict(packs=out, count=len(out)), open(os.path.join(ROOT, 'library', 'index.json'), 'w'), indent=1)
print('library/index.json:', len(out), 'packs')
