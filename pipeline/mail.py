#!/usr/bin/env python3
"""mail.py <job_id> [commit_sha] - get the finished pack to ZC_EMAIL. Three paths, first one that works wins:
  1. Gmail SMTP with the one-shot WAV + round-robin ZIP attached, if the ZC_SMTP_PASS secret (a Google app password) is set
  2. FormSubmit relay with the same attachments (10 MB cap; one-time activation click; their origin was down 2026-11-06)
  3. a GitHub issue in this repo with the download links: GitHub e-mails it to the repo owner (no third party, no setup)
Original FormSubmit notes:
FormSubmit (formsubmit.co) is a no-account form-to-email relay: the first message to an address triggers a one-time activation
mail; after that, submissions deliver. Attachments are capped at 10 MB total, so a pack over 9.5 MB goes as links instead.
A FAIL report is mailed as text with the failed gates. If ZC_EMAIL is empty nothing is sent. Falls back to an ntfy e-mail
(links only, no attachments) when FormSubmit rejects the message.
"""
import json, mimetypes, os, sys, urllib.request, uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = os.environ.get('ZC_EMAIL', '').strip()
REPO = os.environ.get('GITHUB_REPOSITORY', 'robertcossey19/zc-snare')
DONE = os.environ.get('ZC_NTFY_DONE', '')
UA = 'Mozilla/5.0 zc-snare-mail/1.0'


def multipart(fields, files):
    b = uuid.uuid4().hex; out = []
    for k, v in fields.items():
        out.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    for k, path in files:
        ct = mimetypes.guess_type(path)[0] or 'application/octet-stream'
        out.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{os.path.basename(path)}"\r\nContent-Type: {ct}\r\n\r\n'.encode())
        out.append(open(path, 'rb').read()); out.append(b'\r\n')
    out.append(f'--{b}--\r\n'.encode())
    return b''.join(out), f'multipart/form-data; boundary={b}'


def post(url, body, ctype, timeout=120):
    req = urllib.request.Request(url, data=body, headers={'Content-Type': ctype, 'User-Agent': UA, 'Accept': 'application/json', 'Origin': 'https://codepen.io', 'Referer': 'https://codepen.io/'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r: return r.status, r.read(2000).decode('utf-8', 'replace')
    except urllib.error.HTTPError as e: return e.code, e.read(2000).decode('utf-8', 'replace')


def main():
    jid = sys.argv[1]; sha = sys.argv[2] if len(sys.argv) > 2 else 'main'
    if not EMAIL: print('ZC_EMAIL not set; no mail'); return
    d = os.path.join(ROOT, 'packs', jid); rp = os.path.join(d, 'report.json')
    r = json.load(open(rp)) if os.path.exists(rp) else dict(status='FAIL', error='pipeline produced no report (runner crashed)', artist='?', title=jid, gates=[], warnings=[])
    m = r.get('measurements') or {}; lr = r.get('layers_real') or {}; f = r.get('files') or {}
    raw = f'https://raw.githubusercontent.com/{REPO}/{sha}/packs/{jid}/'
    title = f"{r.get('artist', '?')} - {r.get('title', jid)}"
    lines = [f'ZC SNARE EXTRACT  |  {title}  |  {r["status"]}', '']
    if r['status'] == 'OK':
        lines += [f"{m.get('hits_aligned')} hits aligned, waveform corr {m.get('corr_median')}, runner time {r.get('elapsed_s')} s",
                  f"real hits: hard {lr.get('hard', 0)} / medium {lr.get('medium', 0)} / soft {lr.get('soft', 0)} / ghost {lr.get('ghost', 0)} (the rest are flagged estimates)", '',
                  'Round robins ZIP: ' + raw + f.get('zip', ''), 'One-shot WAV:     ' + raw + f.get('oneshot', ''), f'Folder: https://github.com/{REPO}/tree/main/packs/{jid}']
    else:
        lines += ['No pack produced (by design). ' + (r.get('error') or ''), 'Failed gates: ' + ', '.join(g['name'] for g in r.get('gates', []) if not g.get('ok')),
                  f'Report: https://github.com/{REPO}/blob/main/packs/{jid}/report.json']
    if r.get('warnings'): lines += [''] + ['NOTE: ' + w for w in r['warnings']]
    lines += [''] + [('PASS ' if g.get('ok') else 'FAIL ') + f"{g['name']} = {g.get('value')} (limit {g.get('limit')})" for g in r.get('gates', [])]
    body = '\n'.join(lines)
    files = []
    if r['status'] == 'OK':
        cands = [os.path.join(d, f.get('oneshot', '')), os.path.join(d, f.get('zip', ''))]
        if all(os.path.exists(p) for p in cands): files = [('attachment', p) for p in cands]
    small = files if sum(os.path.getsize(p) for _, p in files) <= 9.5 * 1024 * 1024 else []   # FormSubmit's 10 MB cap; SMTP takes up to 20 MB
    subject = f'ZC Snare {r["status"]}: {title}'
    smtp_pass = os.environ.get('ZC_SMTP_PASS', '').strip()
    if smtp_pass:
        try:
            import smtplib
            from email.message import EmailMessage
            msg = EmailMessage(); msg['Subject'] = subject; msg['From'] = EMAIL; msg['To'] = EMAIL; msg.set_content(body)
            for _, pth in (files if sum(os.path.getsize(p) for _, p in files) <= 20 * 1024 * 1024 else []): msg.add_attachment(open(pth, 'rb').read(), maintype='application', subtype='zip' if pth.endswith('.zip') else 'octet-stream', filename=os.path.basename(pth))
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=120) as sm: sm.login(EMAIL, smtp_pass); sm.send_message(msg)
            print('gmail smtp: sent with', len(files), 'attachment(s)'); return
        except Exception as e: print('gmail smtp failed:', e)
    data, ct = multipart({'_subject': subject, '_captcha': 'false', '_template': 'box', 'name': 'ZC Snare Extract', 'message': ('' if small or not files else 'Pack is over the 10 MB mail limit; use the links.\n\n') + body}, small)
    import time
    for attempt in range(3):   # FormSubmit sits behind Cloudflare and returns 522 when its origin is busy; that is marked retryable
        st, resp = post(f'https://formsubmit.co/ajax/{EMAIL}', data, ct)
        print('formsubmit', st, resp[:300].replace('\n', ' '))
        if st == 200 and 'success' in resp.lower() and '"false"' not in resp.lower(): return
        if st not in (502, 503, 504, 522, 524): break
        time.sleep(45)
    # fallback: a GitHub issue with the links. GitHub mails it to the owner (watching own repos is the default). No third party involved.
    import subprocess
    if os.environ.get('GH_TOKEN'):
        ib = body + f'\n\n_Automatic delivery note for job `{jid}`. Attachments could not be mailed (relay unavailable); the links above are direct downloads._'
        rr = subprocess.run(['gh', 'issue', 'create', '-R', REPO, '-t', subject, '-b', ib], capture_output=True, text=True)
        print('github issue', rr.returncode, (rr.stdout or rr.stderr).strip()[:200])


if __name__ == '__main__':
    main()
