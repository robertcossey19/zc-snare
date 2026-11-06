#!/usr/bin/env python3
"""
listen.py - sit on the public ntfy mailbox until a job note arrives (or the time budget runs out).

Why: GitHub's 5-minute cron is best-effort (it can be delayed for an hour or more, and new repos often wait hours before the
first scheduled run ever fires). So the intake workflow keeps ONE runner subscribed to the jobs topic. The moment the page
posts a note this exits 0 with found=1, the normal intake steps run, and the workflow re-dispatches itself to listen again.
GitHub jobs are capped at 6 h, so the budget is ZC_LISTEN_S (default 5 h 35 min); on timeout it exits with found=0 and the
workflow still re-dispatches. The cron is kept only as a restart net in case a hand-off is ever lost. A file named
LISTENER_OFF at the repo root turns the listener off (pure cron mode).
"""
import json, os, sys, time, urllib.request

TOPIC = os.environ.get('ZC_NTFY_TOPIC', '')
BUDGET = float(os.environ.get('ZC_LISTEN_S', '20100'))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def log(*a): print(time.strftime('[%H:%M:%S]'), *a, flush=True)


def out(found):
    p = os.environ.get('GITHUB_OUTPUT')
    if p:
        with open(p, 'a') as f: f.write(f'found={found}\n')
    print('found =', found)


def main():
    if not TOPIC: print('ZC_NTFY_TOPIC not set'); sys.exit(2)
    if os.path.exists(os.path.join(ROOT, 'LISTENER_OFF')): log('LISTENER_OFF present - cron mode'); out(0); return
    t_end = time.time() + BUDGET
    since = str(int(time.time()) - 60)          # catch a note posted while the previous link was finishing
    while time.time() < t_end:
        url = f'https://ntfy.sh/{TOPIC}/json?since={since}'
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'zc-snare-listen/1.0'})
            with urllib.request.urlopen(req, timeout=120) as r:       # ntfy keepalives every ~45 s keep this alive
                log('subscribed', url)
                for line in r:
                    if time.time() >= t_end: break
                    try: m = json.loads(line)
                    except Exception: continue
                    if m.get('event') == 'message':
                        log('job note', m.get('message', '')[:120]); out(1); return
        except Exception as e:
            log('stream dropped:', e)
        time.sleep(5)
    log('time budget used, no notes'); out(0)


if __name__ == '__main__':
    main()
