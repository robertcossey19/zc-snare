#!/usr/bin/env python3
"""notify.py <job_id> <status|auto> [commit_sha] - post a compact status note for the page to the public ntfy 'done' topic.
raw.githubusercontent.com caches by path for 5 min and ignores query strings, so the page learns about results here (instant,
CORS-enabled) and then fetches the files by commit sha, which is always fresh."""
import json, os, sys, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPIC = os.environ.get('ZC_NTFY_DONE', '')
def post(note):
    if not TOPIC: print('ZC_NTFY_DONE not set; note:', note); return
    body = json.dumps(note, separators=(',', ':')).encode()
    req = urllib.request.Request(f'https://ntfy.sh/{TOPIC}', data=body, headers={'Content-Type': 'application/json', 'User-Agent': 'zc-snare-notify/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r: print('notified', r.status, note.get('id'), note.get('status'))
if __name__ == '__main__':
    jid, status = sys.argv[1], sys.argv[2]; sha = sys.argv[3] if len(sys.argv) > 3 else ''
    if status == 'auto':
        p = os.path.join(ROOT, 'packs', jid, 'report.json')
        if not os.path.exists(p): post(dict(id=jid, status='FAIL', error='pipeline produced no report (runner crashed); see the Actions log', sha=sha)); sys.exit(0)
        r = json.load(open(p)); m = r.get('measurements') or {}
        post(dict(id=jid, status=r['status'], sha=sha, zip=(r.get('files') or {}).get('zip'), elapsed_s=r.get('elapsed_s'), layers_real=r.get('layers_real'),
                  hits_aligned=m.get('hits_aligned'), corr_median=m.get('corr_median'), warnings=len(r.get('warnings') or []), error=(r.get('error') or '')[:300],
                  failed=[g['name'] for g in r.get('gates', []) if not g.get('ok')][:8]))
    else:
        post(dict(id=jid, status=status, sha=sha, error=(sys.argv[4] if len(sys.argv) > 4 else '')[:300]))
