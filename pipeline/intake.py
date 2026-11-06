#!/usr/bin/env python3
"""
intake.py - pull new jobs from the public ntfy mailbox, fetch each song from its temp host, stage it for extract.yml.

The page never touches GitHub. It uploads the song to tmpfiles.org (anonymous, 60 min expiry) and posts one JSON note to the
ntfy topic in ZC_NTFY_TOPIC: {"id","url","artist","title","name","size","t0"}. This script runs on the 5-minute cron:
  * reads every cached note on the topic (ntfy keeps 12 h), ignores anything malformed or not from the allowed host
  * skips ids already claimed (queue/<id>.json) or finished (packs/<id>/report.json)
  * downloads the song to work/intake/<id>/input.<ext> (cap 100 MB), records sha256 + size
  * writes queue/<id>.json (the page reads this to show "picked up") and prints the ids for the workflow
An expired upload writes packs/<id>/report.json with status FAIL so the page stops waiting and says why.
"""
import hashlib, json, os, re, subprocess, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.environ.get('ZC_WORK', os.path.join(ROOT, 'work'))
TOPIC = os.environ.get('ZC_NTFY_TOPIC', '')
ID_RX = re.compile(r'^[a-z0-9][a-z0-9-]{2,48}$')
EXT_OK = {'.mp3', '.wav', '.flac', '.m4a', '.aif', '.aiff', '.ogg', '.aac', '.wma', '.opus'}
CAP = 100 * 1024 * 1024
UA = 'Mozilla/5.0 (X11; Linux x86_64) zc-snare-intake/1.0'


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return urllib.request.urlopen(req, timeout=timeout)


def log(*a): print(time.strftime('[%H:%M:%S]'), *a, flush=True)


def fail_report(jid, note, msg):
    d = os.path.join(ROOT, 'packs', jid); os.makedirs(d, exist_ok=True)
    json.dump(dict(job=jid, status='FAIL', error=msg, artist=note.get('artist'), title=note.get('title'), gates=[], warnings=[],
                   started=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), elapsed_s=0), open(os.path.join(d, 'report.json'), 'w'), indent=1)


def resolve(url):
    """tmpfiles.org gives a page URL; the direct link (with its time token) is on that page."""
    if url.startswith('https://tmpfiles.org/dl/'): return url
    html = get(url, 30).read(400000).decode('utf-8', 'replace')
    m = re.search(r'https://tmpfiles\.org/dl/[^"\'<\s]+', html)
    if not m: raise RuntimeError('download link not found on host page (upload expired?)')
    return m.group(0)


def main():
    if not TOPIC: print('ZC_NTFY_TOPIC not set'); sys.exit(2)
    raw = get(f'https://ntfy.sh/{TOPIC}/json?poll=1&since=12h', 60).read().decode('utf-8', 'replace')
    notes = []
    for line in raw.splitlines():
        try:
            m = json.loads(line)
            if m.get('event') != 'message': continue
            n = json.loads(m.get('message', ''))
            if not isinstance(n, dict): continue
            jid = str(n.get('id', '')); url = str(n.get('url', ''))
            if not ID_RX.match(jid) or not url.startswith('https://tmpfiles.org/'): log('ignored note', jid[:40], url[:40]); continue
            n['id'] = jid; n['ntfy_time'] = m.get('time'); notes.append(n)
        except Exception as e: log("bad note:", repr(line[:80]), e); continue
    log(f'{len(notes)} valid note(s) on the topic')
    picked = []
    seen = set()
    for n in notes:
        jid = n['id']
        if jid in seen: continue
        seen.add(jid)
        if n.get('ntfy_time') and time.time() - float(n['ntfy_time']) > 75 * 60: continue   # older than the temp host's 60-min life: expired, never re-run (a deleted pack must not re-open a job)
        if os.path.exists(os.path.join(ROOT, 'queue', jid + '.json')) or os.path.exists(os.path.join(ROOT, 'packs', jid, 'report.json')): continue
        ext = os.path.splitext(str(n.get('name', '')))[1].lower()
        if ext not in EXT_OK: ext = '.bin'
        d = os.path.join(WORK, 'intake', jid); os.makedirs(d, exist_ok=True); dst = os.path.join(d, 'input' + ext)
        try:
            link = resolve(n['url']); log(jid, 'fetching', link)
            h = hashlib.sha256(); size = 0
            with get(link, 120) as r, open(dst, 'wb') as f:
                ct = r.headers.get('Content-Type', '')
                if 'text/html' in ct: raise RuntimeError('host returned a web page instead of the file (upload expired?)')
                while True:
                    b = r.read(1 << 20)
                    if not b: break
                    size += len(b)
                    if size > CAP: raise RuntimeError('file larger than 100 MB')
                    h.update(b); f.write(b)
            if size < 20000: raise RuntimeError(f'file too small ({size} bytes)')
        except Exception as e:
            log(jid, 'FAIL', e); fail_report(jid, n, f'could not fetch the upload: {e}. Re-upload and hit GO again (temp uploads live 60 min).')
            os.makedirs(os.path.join(ROOT, 'queue'), exist_ok=True)
            json.dump(dict(id=jid, status='FAIL', claimed=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), open(os.path.join(ROOT, 'queue', jid + '.json'), 'w'))
            subprocess.run([sys.executable, os.path.join(ROOT, 'pipeline', 'notify.py'), jid, 'FAIL', '', f'could not fetch the upload: {e}'], check=False)
            continue
        meta = dict(id=jid, artist=str(n.get('artist') or 'Unknown artist')[:60], title=str(n.get('title') or jid)[:80], mixer='',
                    source_name=str(n.get('name', ''))[:120], size=size, sha256=h.hexdigest(), ext=ext, submitted=n.get('t0'),
                    claimed=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), intake_run=os.environ.get('GITHUB_RUN_ID', ''), status='QUEUED')
        os.makedirs(os.path.join(ROOT, 'queue'), exist_ok=True)
        json.dump(meta, open(os.path.join(ROOT, 'queue', jid + '.json'), 'w'), indent=1)
        json.dump(meta, open(os.path.join(d, 'meta.json'), 'w'))
        picked.append(jid); log(jid, 'staged', size, 'bytes', meta['sha256'][:12])
        subprocess.run([sys.executable, os.path.join(ROOT, 'pipeline', 'notify.py'), jid, 'QUEUED'], check=False)
    out = os.environ.get('GITHUB_OUTPUT')
    if out:
        with open(out, 'a') as f: f.write('ids=' + ' '.join(picked) + '\n')
    print('picked:', ' '.join(picked))


if __name__ == '__main__':
    main()
