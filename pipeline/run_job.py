#!/usr/bin/env python3
"""ZC Snare Extract - job orchestrator (runs on GitHub Actions, or anywhere with ffmpeg + the pinned python env).

    python3 pipeline/run_job.py <job_id>

Input : jobs/<job_id>/input.<ext>  (+ optional jobs/<job_id>/meta.json {"artist","title","mixer"})
Output: packs/<job_id>/report.json  always
        packs/<job_id>/ZC_Snare_<job_id>_RoundRobins.zip, ZC_<job_id>_oneshot.wav, info.json, README.txt  only when every gate passes

Every song goes through the identical, pinned pipeline:
  decode -> Demucs htdemucs (drums) -> MDX23C DrumSep (6 stems) -> build_pack (realvel, auto per band) -> per-file QC with re-pick -> gates -> pack
No gate is tunable per song. A failed gate produces a FAIL report and no pack (never a 'best effort' pack).
"""
import os, sys, json, time, glob, hashlib, shutil, subprocess, re
import numpy as np, soundfile as sf, scipy.signal as sg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPE = os.path.join(ROOT, 'pipeline')
WORK = os.environ.get('ZC_WORK', os.path.join(ROOT, 'work'))
CKPT_SHA = 'd2a4aa53eb584d21eead358a4e66d1882ad182911be018f052b5da73be9096d0'
CKPT_URL = 'https://huggingface.co/noblebarkrr/mvsepless_resources/resolve/main/mdx23c/mdx23c_drumsep_6stem_aufr33_jarredou.ckpt'
MSST_COMMIT = 'f0b527736e7da24eae5b561a2bb1efd0569ec757'
PIPELINE_VERSION = '5.0.3'
SR = 44100
STEMS = ['Kick', 'Snare', 'Toms', 'Hh', 'Ride', 'Crash']

T0 = time.time()
LOG = []
def log(*a):
    s = f'[{time.time() - T0:7.1f}s] ' + ' '.join(str(x) for x in a); print(s, flush=True); LOG.append(s)

def db(x): return float(20 * np.log10(np.sqrt((np.asarray(x) ** 2).mean()) + 1e-12))

class Gate:
    def __init__(self): self.rows = []; self.failed = False
    def check(self, name, value, ok, limit, note=''):
        self.rows.append(dict(name=name, value=value, limit=limit, pass_=bool(ok), note=note))
        log(('PASS' if ok else 'FAIL'), name, '=', value, '(limit', limit + ')', note)
        if not ok: self.failed = True
        return ok

def sh(cmd, cwd=None, env=None):
    log('$', cmd if isinstance(cmd, str) else ' '.join(cmd))
    r = subprocess.run(cmd, shell=isinstance(cmd, str), cwd=cwd, env=env, text=True, capture_output=True)
    if r.returncode != 0:
        log(r.stdout[-4000:]); log(r.stderr[-4000:]); raise RuntimeError(f'command failed ({r.returncode}): {cmd if isinstance(cmd, str) else cmd[0]}')
    return r.stdout

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def main(job):
    assert re.fullmatch(r'[a-z0-9][a-z0-9_-]{1,40}', job), 'job id must be lowercase alnum/_/-'
    jdir = os.path.join(ROOT, 'jobs', job); odir = os.path.join(ROOT, 'packs', job); os.makedirs(odir, exist_ok=True)
    report = dict(job=job, status='RUNNING', pipeline=PIPELINE_VERSION, stages={}, gates=[], warnings=[], started=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    def save():
        report['log_tail'] = LOG[-60:]; report['elapsed_s'] = round(time.time() - T0, 1)
        json.dump(report, open(os.path.join(odir, 'report.json'), 'w'), indent=1)
    G = Gate()
    try:
        # ---------- 0. input ----------
        ins = [p for p in glob.glob(os.path.join(jdir, 'input.*'))]
        if not ins: raise RuntimeError(f'no jobs/{job}/input.* found')
        src = ins[0]; meta = {}
        if os.path.exists(os.path.join(jdir, 'meta.json')): meta = json.load(open(os.path.join(jdir, 'meta.json')))
        artist = str(meta.get('artist') or 'Unknown artist')[:60]; title = str(meta.get('title') or job)[:80]; mixer = str(meta.get('mixer') or 'unknown')[:60]
        report.update(artist=artist, title=title, mixer=mixer, input_name=os.path.basename(src), input_bytes=os.path.getsize(src), input_sha256=sha256(src))
        log('job', job, '|', artist, '-', title, '|', report['input_name'], report['input_bytes'], 'bytes')
        for d in ['audio', 'sep', 'ds/in', 'ds/out', 'pack2']: os.makedirs(os.path.join(WORK, d), exist_ok=True)
        # ---------- 1. decode ----------
        t = time.time(); wav = os.path.join(WORK, 'audio', f'{job}.wav')
        probe = json.loads(sh(['ffprobe', '-v', 'error', '-print_format', 'json', '-show_format', '-show_streams', src]))
        ast = [s for s in probe.get('streams', []) if s.get('codec_type') == 'audio']
        if not ast: raise RuntimeError('file has no audio stream')
        report['input_codec'] = ast[0].get('codec_name'); report['input_sr'] = int(ast[0].get('sample_rate') or 0); report['input_bitrate'] = int(probe['format'].get('bit_rate') or 0)
        sh(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', src, '-vn', '-ar', str(SR), '-ac', '2', '-c:a', 'pcm_s16le', wav])
        x, sr = sf.read(wav, dtype='float32'); dur = len(x) / SR
        report['duration_s'] = round(dur, 1); report['mix_rms_dbfs'] = round(db(x), 1); report['mix_peak_dbfs'] = round(float(20 * np.log10(np.abs(x).max() + 1e-12)), 1)
        clip = float((np.abs(x) >= 0.999).mean())
        G.check('duration_s', round(dur, 1), 30 <= dur <= 720, '30..720 s')
        G.check('mix_peak_dbfs', report['mix_peak_dbfs'], report['mix_peak_dbfs'] > -30, '> -30 dBFS', 'silent or near-silent file')
        G.check('clipped_fraction', round(clip, 5), clip < 0.02, '< 0.02', 'samples at full scale')
        if report['input_codec'] in ('mp3', 'aac', 'vorbis', 'opus') and report['input_bitrate'] and report['input_bitrate'] < 160000:
            report['warnings'].append(f"lossy input at {report['input_bitrate']//1000} kbps: expect a lower HF ceiling and more pre-echo than the reference packs (built from 128-320 kbps / WAV)")
        if report['input_codec'] in ('mp3', 'aac', 'vorbis', 'opus'): report['warnings'].append('lossy source: top end limited by the codec (~16 kHz for mp3); WAV/FLAC input gives a cleaner result')
        report['stages']['decode_s'] = round(time.time() - t, 1); save()
        if G.failed: raise RuntimeError('input gate failed')
        # ---------- 2. Demucs ----------
        t = time.time(); drums = os.path.join(WORK, 'sep', 'htdemucs', job, 'drums.wav')
        if not os.path.exists(drums):
            sh([sys.executable, '-m', 'demucs', '-n', 'htdemucs', '--two-stems=drums', '-d', 'cpu', '-j', '1', '--segment', '7', '-o', os.path.join(WORK, 'sep'), wav])
        D, _ = sf.read(drums, dtype='float64'); report['drums_rms_dbfs'] = round(db(D), 1)
        G.check('drums_rms_dbfs', report['drums_rms_dbfs'], report['drums_rms_dbfs'] > -45, '> -45 dBFS', 'Demucs found no drum content')
        G.check('drums_minus_mix_db', round(db(D) - db(x), 1), -25 < db(D) - db(x) < 3, '-25..+3 dB', 'drum share of the mix')
        for d_ in ['in', f'in_{job}']:
            os.makedirs(os.path.join(WORK, 'ds', d_), exist_ok=True); lp = os.path.join(WORK, 'ds', d_, f'{job}.wav')
            if not os.path.exists(lp): os.symlink(drums, lp)
        report['stages']['demucs_s'] = round(time.time() - t, 1); save()
        if G.failed: raise RuntimeError('drum-stem gate failed')
        # ---------- 3. DrumSep ----------
        t = time.time(); ckpt = os.path.join(WORK, 'ds', 'drumsep.ckpt'); msst = os.path.join(WORK, 'ds', 'msst')
        if not os.path.exists(ckpt) or sha256(ckpt) != CKPT_SHA:
            log('downloading DrumSep checkpoint'); sh(['curl', '-sL', '-o', ckpt, CKPT_URL])
        if sha256(ckpt) != CKPT_SHA: raise RuntimeError('DrumSep checkpoint sha256 mismatch - refusing to run on an unverified model')
        if not os.path.exists(os.path.join(msst, 'inference.py')):
            sh(['git', 'clone', '-q', 'https://github.com/ZFTurbo/Music-Source-Separation-Training', msst]); sh(['git', 'checkout', '-q', MSST_COMMIT], cwd=msst)
        outd = os.path.join(WORK, 'ds', 'out')
        def stem_path(s):
            for p in [os.path.join(outd, job, f'{s}.wav'), os.path.join(outd, f'{job}_{s}.wav')]:
                if os.path.exists(p): return p
        if not all(stem_path(s) for s in STEMS):
            sh([sys.executable, 'inference.py', '--model_type', 'mdx23c', '--config_path', os.path.join(PIPE, 'drumsep.yaml'), '--start_check_point', ckpt,
                '--input_folder', os.path.join(WORK, 'ds', f'in_{job}'), '--store_dir', outd, '--force_cpu', '--pcm_type', 'FLOAT', '--disable_detailed_pbar'], cwd=msst)
        S = {}
        for s in STEMS:
            p = stem_path(s)
            if not p: raise RuntimeError(f'DrumSep did not write the {s} stem')
            S[s], _ = sf.read(p, dtype='float64')
        n = min(len(D), *[len(v) for v in S.values()]); resid = D[:n] - sum(v[:n] for v in S.values())
        report['stem_rms_dbfs'] = {k: round(db(v), 1) for k, v in S.items()}; rd = round(db(D) - db(resid), 1); report['separation_residual_below_drums_db'] = rd
        # Global residual = what DrumSep assigned to no drum stem. On dense guitar records Demucs leaves guitar bleed in the drum stem and DrumSep rightly
        # puts it nowhere (Nickelback 23.9 dB, Metallica Enter Sandman 17.9 dB) - that is not snare loss. The hard floor is 12 dB (stems do not add up at all);
        # what the snare actually lost is gated per band after the build (snare_lost_to_residual_max_db <= 1.0 dB, hit-locked, 150 Hz-8 kHz, first 60 ms).
        G.check('separation_residual_below_drums_db', rd, rd >= 12, '>= 12 dB', 'the six stems must add back up to the drum stem (reference songs 23.9..32.0; the snare-specific loss is gated per band below)')
        if rd < 25: report['warnings'].append(f'separation residual {rd} dB under the drum stem (reference songs 23.9..32.0): the drum stem carries non-drum bleed the drum separator assigns to no stem; the snare-specific loss gate below is what counts')
        G.check('snare_stem_rms_dbfs', report['stem_rms_dbfs']['Snare'], -45 < report['stem_rms_dbfs']['Snare'] < -8, '-45..-8 dBFS', 'reference songs -20..-30')
        report['stages']['drumsep_s'] = round(time.time() - t, 1); save()
        if G.failed: raise RuntimeError('separation gate failed')
        # ---------- 4. library placement + strategy ladder + per-file QC with re-pick ----------
        t = time.time(); sys.path.insert(0, PIPE); os.chdir(WORK)
        import build_pack, library
        LIB = library.load(ROOT); report['library_size'] = len(LIB)
        pre = dict(separation_residual_below_drums_db=rd, input_kbps=round(report['input_bitrate'] / 1000) if report.get('input_bitrate') else None,
                   hat_minus_snare_stem_db=round(report['stem_rms_dbfs']['Hh'] - report['stem_rms_dbfs']['Snare'], 1))
        order = library.strategy_order(pre, LIB); report['strategy_order'] = order; report['nearest_before_build'] = library.nearest(pre, LIB) if LIB else []
        log('library:', len(LIB), 'songs; strategy order', order, '| nearest by separation/stem facts:', [(n['job'], n['distance']) for n in report['nearest_before_build']])
        attempts = []; info = None; qc_rows = []; excl = []; chosen = None
        for strat in order:
            SP = library.STRATEGIES[strat]; excl = []; info = None; qc_rows = []
            for attempt in range(8):   # 8 re-picks: bleed-heavy records (Enter Sandman, hat stem 2.8 dB under the snare stem) kept throwing bled loud hits past 3 re-picks
                os.environ['ZC_EXCLUDE'] = ','.join(f'{v:.3f}' for v in excl)
                log(f'strategy {strat}: build attempt {attempt + 1}, excluded {len(excl)} hit(s)')
                try: build_pack.rng.seed(7); info = build_pack.build(job, analyse_only=False, realvel=True, strategy=SP)
                except Exception as e:
                    log(f'strategy {strat}: build raised {e}'); info = None; break
                # adaptive hat-bleed limit: the record's own loud template sets what "bright" means on this snare (reference snares 700..1400 Hz 0-30 ms centroid)
                yo, sro = sf.read(f'pack2/{job}/ZC_{job}_oneshot.wav'); mo = yo.mean(1)[:int(0.03 * sro)]; Po = np.abs(np.fft.rfft(mo * np.hanning(len(mo)))) ** 2; fo = np.fft.rfftfreq(len(mo), 1 / sro)
                tcent = int((Po * fo).sum() / (Po.sum() + 1e-20))
                bad = []; qc_rows = []
                for k, h in enumerate(info['selected']):
                    lay = h['layer']; y, sr_ = sf.read(f'pack2/{job}/ZC_{job}_{lay}_rr{k % 4 + 1}.wav'); m = y.mean(1); pk = np.abs(m).max()
                    seg = m[:int(0.03 * sr_)]; P = np.abs(np.fft.rfft(seg * np.hanning(len(seg)))) ** 2; f = np.fft.rfftfreq(len(seg), 1 / sr_)
                    row = dict(slot=f'{lay}_rr{k % 4 + 1}', t=h['t'], real=bool(h.get('real')), rel_db=h.get('rel_db'), peak_dbfs=round(float(20 * np.log10(pk + 1e-12)), 1),
                               first_half_ms_re_peak_db=round(float(20 * np.log10(np.abs(m[:int(0.0005 * sr_)]).max() / pk + 1e-9)), 1), centroid_hz=int((P * f).sum() / (P.sum() + 1e-20)), len_ms=h['len_ms'], ok=True, why='')
                    if lay in ('hard', 'medium') and row['peak_dbfs'] < -40: row.update(ok=False, why='peak under -40 dBFS')
                    lim = -13 if h.get('real') else -6   # real hits: stick attack must build from >= 13 dB down; transformed estimates have their peak in the body, so only a true abrupt start (> -6 dB) fails
                    if row['first_half_ms_re_peak_db'] > lim: row.update(ok=False, why=f'attack clipped (first 0.5 ms within {-lim} dB of peak)')
                    # 5.0: the file must end in silence, not in a burst (every estimate layer of packs <= 4.3.1 ended in a circular-FFT click 30..50 dB
                    # above the tail it followed) and no band may step: after 30 ms the 5 ms broadband envelope may not rise by > 6 dB frame to frame
                    e10 = int(0.01 * sr_); nfr = len(m) // e10; env = 20 * np.log10(np.sqrt((m[:nfr * e10].reshape(nfr, e10) ** 2).mean(1)) + 1e-9)
                    last = float(20 * np.log10(np.abs(m[-int(0.02 * sr_):]).max() + 1e-9)); prev = float(20 * np.log10(np.abs(m[-int(0.1 * sr_):-int(0.02 * sr_)]).max() + 1e-9))
                    d_ = np.diff(env[3:]); okf = env[4:] > env.max() - 50   # ring-mode beating gives <= 8 dB rises between 10 ms frames; the old end click measured 12..32 dB
                    row['end_last20ms_dbfs'] = round(last, 1); row['max_env_rise_db'] = round(float(d_[okf].max()) if okf.any() else 0.0, 1)
                    if last > -60 or last > prev + 3: row.update(ok=False, why=f'file ends in a burst ({last:.0f} dBFS in the last 20 ms, {prev:.0f} before)')
                    if row['max_env_rise_db'] > 10: row.update(ok=False, why=f"envelope rises {row['max_env_rise_db']} dB between 10 ms frames after 30 ms (a second event or a click in the file)")
                    qc_rows.append(row)
                # hat-bleed limit is relative to THIS snare: a bled hit is an outlier against the record's own loud strokes (reference snares 700..1400 Hz,
                # Deftones 'Change' 1080..1500 Hz legitimately); fixed 1500 Hz failed a clean bright hit at 1501 Hz
                pop = [r['centroid_hz'] for r in qc_rows if r['slot'].split('_')[0] in ('hard', 'medium') and r['real']] or [r['centroid_hz'] for r in qc_rows]
                clim = int(max(1500, 1.35 * float(np.median(pop))))
                for row in qc_rows:
                    if row['slot'].startswith('hard') and row['centroid_hz'] > clim: row.update(ok=False, why=f'0-30 ms centroid > {clim} Hz (hat bleed; this record\'s loud strokes sit at {int(np.median(pop))} Hz)')
                    if not row['ok']: bad.append(row['t'])   # real hit or estimate donor: exclude that hit and re-pick
                if not bad: break
                log('per-file QC rejected', [(r['slot'], r['why']) for r in qc_rows if not r['ok']]); excl += bad
            if info is None: attempts.append(dict(strategy=strat, ok=False, why='build raised')); continue
            tt = [h['t'] for h in info['selected']]; mind = min(abs(a - b) for i, a in enumerate(tt) for b in tt[i + 1:])
            why = []
            if info['hits_aligned'] < 60: why.append(f"hits_aligned {info['hits_aligned']} < 60")
            if info['corr_median'] < 0.55: why.append(f"corr_median {info['corr_median']} < 0.55")   # tiered: under 0.55 the template is meaningless; 0.55..0.70 passes with a variation warning (Metallica Fuel 0.65..0.69: one snare, played with more hit-to-hit variation than the reference records, verified by clustering)
            if any(not r['ok'] for r in qc_rows): why.append(f"{sum(not r['ok'] for r in qc_rows)} file(s) failed QC after 7 re-picks")
            if mind < 0.05: why.append(f'selected hits not distinct (min gap {mind:.3f} s)')
            attempts.append(dict(strategy=strat, ok=not why, why='; '.join(why), hits_aligned=info['hits_aligned'], corr_median=info['corr_median'], layers_real={k: int(sum(v)) for k, v in info['layers_real'].items()}, template_centroid_hz=tcent, centroid_limit_hz=clim, qc_repicks=len(excl)))
            attempts[-1]['score'] = round(info['corr_median'] * min(info['hits_aligned'], 200) / 200.0 * (1 + 0.05 * sum(attempts[-1]['layers_real'].get(k, 0) for k in ('medium', 'soft', 'ghost'))), 3)
            attempts[-1]['excluded'] = list(excl); attempts[-1]['qc'] = qc_rows
            log(f'strategy {strat}:', ('OK score ' + str(attempts[-1]['score'])) if not why else 'rejected: ' + '; '.join(why))
            marginal = not why and (info['corr_median'] < float(os.environ.get('ZC_MARGINAL_CORR', 0.85)) or info['hits_aligned'] < 100)   # passes, but under the reference packs (corr 0.92..0.95, 116..217 hits): try the other recipes too and keep the best
            if not why and not marginal: chosen = strat; best = attempts[-1]; break   # (4.2.1) 'best' was unbound on this path: every clean first-try song crashed with UnboundLocalError (Starset Lancaster, corr 0.899)
            if not why and marginal and strat != order[-1]: log(f'strategy {strat} is marginal (corr {info["corr_median"]}, {info["hits_aligned"]} hits): trying the remaining recipes, best score wins')
        report['strategy_attempts'] = [{k: v for k, v in a.items() if k not in ('qc', 'excluded')} for a in attempts]
        if info is None and not any(a.get('ok') for a in attempts): raise RuntimeError('every strategy raised during build: ' + '; '.join(a.get('why', '') for a in attempts))
        passing = [a for a in attempts if a.get('ok')]; best = attempts[-1] if chosen and attempts else None
        if passing and chosen is None:
            best = max(passing, key=lambda a: a['score']); chosen = best['strategy']
            if attempts[-1]['strategy'] != chosen or not attempts[-1].get('ok'):   # rebuild the winner so pack2/ holds its files (deterministic: same seed, same exclusions)
                log(f'rebuilding winner {chosen} (score {best["score"]}) ...'); os.environ['ZC_EXCLUDE'] = ','.join(f'{v:.3f}' for v in best['excluded'])
                build_pack.rng.seed(7); info = build_pack.build(job, analyse_only=False, realvel=True, strategy=library.STRATEGIES[chosen]); qc_rows = best['qc']; excl = best['excluded']
        if not passing:   # nothing held: report the best-looking failed recipe's measurements (most hits aligned) so the FAIL is explainable
            built = [a for a in attempts if a.get('hits_aligned') is not None]
            if not built: raise RuntimeError('every strategy raised during build: ' + '; '.join(a.get('why', '') for a in attempts))
            best = max(built, key=lambda a: (a['hits_aligned'], a['corr_median']))
            if attempts[-1] is not best or info is None:
                os.environ['ZC_EXCLUDE'] = ','.join(f'{v:.3f}' for v in best['excluded']); build_pack.rng.seed(7)
                info = build_pack.build(job, analyse_only=False, realvel=True, strategy=library.STRATEGIES[best['strategy']]); qc_rows = best['qc']; excl = best['excluded']
            report['warnings'].append('no detection recipe passed the hit gates on this record; measurements below are from ' + best['strategy'] + ' (' + best['why'] + ')')
        report['strategy_used'] = chosen or best['strategy']; report['template_centroid_hz'] = best.get('template_centroid_hz') if (not passing or chosen) else attempts[-1].get('template_centroid_hz')
        if chosen and chosen != order[0]: report['warnings'].append(f"detection recipe {order[0]} was not the best on this record; {chosen} won ({library.STRATEGIES[chosen]['note']}); scores: " + ', '.join(f"{a['strategy']} {a.get('score', 'x')}" for a in attempts))
        report['file_qc'] = qc_rows; report['qc_repicks'] = len(excl)
        G.check('file_qc_all_pass', sum(not r['ok'] for r in qc_rows), all(r['ok'] for r in qc_rows), '0 failing files', 'after up to 7 re-picks per strategy')
        # ---------- 5. gates on the measurements ----------
        a5 = info['audit']['0-5ms']; coh = info['coherent_resid']['0-5ms']; tilt = info['stem_vs_drums_tilt_db']
        G.check('hits_aligned', info['hits_aligned'], info['hits_aligned'] >= 60, '>= 60', 'reference songs 116..184')
        if info['hits_aligned'] < 100: report['warnings'].append(f"only {info['hits_aligned']} hits aligned (reference songs 116..184)")
        G.check('corr_median', info['corr_median'], info['corr_median'] >= 0.55, '>= 0.55', 'reference songs 0.76..0.95; 0.55..0.70 passes with a variation warning')
        if info['corr_median'] < 0.7: report['warnings'].append(f"hit-to-hit waveform correlation {info['corr_median']} (reference packs 0.76..0.95): this record's snare varies more from stroke to stroke (player, dense mix, or bleed in the snare stem) - expect audibly different round robins; every file still passed the per-file QC (clean attack, no hat-bleed centroid, level)")
        G.check('audit_0_5ms_snare_vs_drums_db', round(a5['snare'] - a5['drums'], 1), abs(a5['snare'] - a5['drums']) <= 1.5, '|diff| <= 1.5 dB', 'transient intact after separation')
        cohdb = round(coh['snare_dB'] - coh['coherent_resid_dB'], 1)
        G.check('coherent_resid_below_snare_db', cohdb, cohdb >= 12, '>= 12 dB', 'hit-locked snare energy the separator assigned to no stem (reference songs 42..44; dense mixes 18..25)')
        if cohdb < 25: report['warnings'].append(f'coherent residual {cohdb} dB under the snare (reference songs 42..44): denser mix, the separator left a little more hit-locked energy unassigned; per-band loss is gated below')
        lost = info['lost_to_resid_db']; hvs = info['hat_vs_snare_db']
        lk = ['150-300', '300-600', '600-1200', '1200-2500', '2500-5000', '5000-8000']; worst = min(lost[k] for k in lk)
        G.check('snare_lost_to_residual_max_db', round(-worst, 2), -worst <= 1.0, '<= 1.0 dB', 'snare stem vs snare+unassigned residual, 150 Hz-8 kHz, first 60 ms: the real separation loss')
        # 4.0.x gated snare-vs-DRUM-STEM tilt here; that mis-read hat/cymbal energy correctly moved to the hat/crash stems as lost snare (false FAIL on records with a loud hat on the backbeat). Reported only now.
        if tilt['5000-8000'] < -4.0 or max(abs(tilt[k]) for k in lk[:5]) > 2.0:
            report['warnings'].append(f"snare stem sits {tilt['5000-8000']} dB under the full drum stem at 5-8 kHz on the hits: on this record the hat/cymbals ride the backbeat ({hvs['5000-8000']:+.1f} dB hat+crash vs snare in that band); that energy is in the hat/crash stems, not lost (loss to residual {lost['5000-8000']} dB)")
        G.check('noise_floor_dbfs', info['noise_floor_dbfs'], info['noise_floor_dbfs'] < -60, '< -60 dBFS', 'snare stem between hits')
        t60 = list(info['t60_band'].values())
        G.check('t60_mid_bands_s', t60[1:4], all(0.08 <= v <= 3.0 for v in t60[1:4]), '0.08..3.0 s', 'measured late decay 150 Hz-6 kHz')
        lr = {k: int(sum(v)) for k, v in info['layers_real'].items()}; report['layers_real'] = lr
        G.check('selected_hits_distinct_min_gap_s', round(mind, 3), mind >= 0.05, '>= 0.05 s', 'all 16 files come from different strokes')
        report['selected'] = [dict(slot=f"{h['layer']}_rr{i % 4 + 1}", t=h['t'], real=bool(h.get('real')), rel_db=h.get('rel_db'), gap_ms=h['gap_ms'], real_to_ms=h['real_to_ms'], reclaimed_ms=h.get('reclaimed_ms'), guard_db=h.get('guard_db'), len_ms=h['len_ms']) for i, h in enumerate(info['selected'])]
        thin = info.get('thin_stem') or {}; rb = [k for k, v in thin.items() if v.get('reclaim')]
        if rb: report['warnings'].append(f"thin snare stem in {', '.join(rb)} (band1 150-600, band2 600-2k, band3 2-6k, band4 >6k Hz): the separator handed this record's hit-locked snare ring beyond ~100 ms to the hat/cymbal stems (other-stem excess at 100 ms, low-hat vs high-hat hits: " + '; '.join(f"{k} {thin[k]['other_excess_100_low_hat']}/{thin[k]['other_excess_100_high_hat']} dB" for k in rb) + "). Those bands' tails were reclaimed from that material per hit (Wiener gain against its pre-hit background, other strokes masked); see selected[].reclaimed_ms")
        report['measurements'] = dict(hits_aligned=info['hits_aligned'], corr_median=info['corr_median'], level_sd_db=info['level_sd_db'], t60_band=info['t60_band'], slope_db_s=info['slope_db_s'], audit_0_5ms=a5, coherent_resid_0_5ms=coh, tilt=tilt, lost_to_resid_db=lost, hat_vs_snare_db=hvs, noise_floor_dbfs=info['noise_floor_dbfs'], thin_stem=thin, reclaim_bands=info.get('reclaim_bands'))
        prof = library.profile(dict(report, status='OK')); report['profile'] = prof
        if LIB:
            report['nearest'] = library.nearest(prof, LIB); report['library_notes'] = library.place(prof, LIB)
            log('nearest library songs after build:', [(n['job'], n['distance']) for n in report['nearest']]); [log('library note:', w) for w in report['library_notes']]
        for lname in ['medium', 'soft', 'ghost']:
            if lr.get(lname, 0) < 4: report['warnings'].append(f"{lname}: {lr.get(lname,0)}/4 real hits found in that velocity band on this record; the other {4 - lr.get(lname,0)} are flagged estimates (a real full hit carried to that layer with this record's measured velocity law where it has one)")
        # ---------- 6. golden master (known inputs only) ----------
        gpath = os.path.join(ROOT, 'golden', report['input_sha256'] + '.json')
        if os.path.exists(gpath):
            # Bit-identical picks across machines are not achievable: the separators run float math whose rounding differs per CPU, and the quiet
            # velocity bands sit near the stem floor, so soft/ghost membership can flip. The gate therefore checks what must hold on any machine:
            # the loud (hard) picks, the alignment statistics and the measured decay, each within a tolerance measured from local perturbation tests.
            g = json.load(open(gpath)); gt = {h['slot']: h['t'] for h in g['selected']}; nt = {f"{h['layer']}_rr{i % 4 + 1}": h['t'] for i, h in enumerate(info['selected'])}
            hard_same = sum(1 for k, v in gt.items() if k.startswith('hard') and any(abs(v - t) < 0.005 for kk, t in nt.items() if kk.startswith('hard')))   # same strokes, any slot order
            same = sum(1 for k in gt if abs(gt[k] - nt.get(k, -1)) < 0.005)
            g_hard_db = [h['rel_db'] for h in g['selected'] if h['slot'].startswith('hard')]; n_hard_db = [h.get('rel_db') or 0 for h in info['selected'] if h['layer'] == 'hard']
            hard_db_diff = abs(sum(n_hard_db) / max(1, len(n_hard_db)) - sum(g_hard_db) / max(1, len(g_hard_db)))
            report['golden'] = dict(name=g.get('name'), hard_slots_identical=hard_same, slots_identical=same, of=len(gt), expected=gt, got=nt, hard_level_diff_db=round(hard_db_diff, 2),
                                    expected_hits_aligned=g['hits_aligned'], expected_corr_median=g['corr_median'], expected_layers_real=g['layers_real'])
            # Runner vs build-machine (measured 2026-11-06, 4-CPU hosted runner vs 2-CPU sandbox): hard-set overlap 2/4..4/4, hits_aligned within 10%,
            # corr_median within 0.04, mid-band T60 within 0.25 s. The loud candidates sit within ~1 dB of each other, so which 4 win is CPU-rounding
            # sensitive; what must hold is that the winners are the same loud strokes at the same level.
            G.check('golden_hard_picks_overlap', f'{hard_same}/4', hard_same >= 2, '>= 2/4 same strokes (any order)', f"known input ({g.get('name')}): loud picks must come from the same population")
            G.check('golden_hard_level_db', round(hard_db_diff, 2), hard_db_diff <= 1.5, '<= 1.5 dB vs golden hard mean', 'loud picks at the same level as the golden picks')
            g_recipe = g.get('strategy') or order[0]   # goldens recorded before the recipe race ran the default recipe
            if chosen == g_recipe:
                G.check('golden_hits_aligned_tolerance', info['hits_aligned'], abs(info['hits_aligned'] - g['hits_aligned']) <= 0.3 * g['hits_aligned'], f"{g['hits_aligned']} +-30%")
                G.check('golden_corr_median_tolerance', info['corr_median'], abs(info['corr_median'] - g['corr_median']) <= 0.1, f"{g['corr_median']} +-0.10")
            else:   # a different detection recipe won on this run: it aligns a different hit population (more hits at a lower correlation, or fewer tighter ones), so the alignment statistics are not comparable with the golden run; the hard picks, their level and the layers still are
                report['warnings'].append(f"golden run used recipe {g_recipe} ({g['hits_aligned']} hits, corr {g['corr_median']}); this run's race picked {chosen} ({info['hits_aligned']} hits, corr {info['corr_median']}) - alignment statistics not compared (different hit population), hard picks / level / layers compared as usual")
            G.check('golden_layers_real_hard_medium', f"hard {lr.get('hard',0)} medium {lr.get('medium',0)}", lr.get('hard', 0) == 4 and lr.get('medium', 0) >= g['layers_real']['medium'] - 1,
                    f"hard 4, medium >= {g['layers_real']['medium'] - 1}", 'soft/ghost counts are reported, not gated: they sit near the stem floor')
            if 't60_band' in g:
                # Reported, not gated: the 150-300 Hz late-decay fit swings 0.23..0.56 s run-to-run on the SAME input (hosted runners land on different
                # CPUs; the separators' float paths differ; that band is where kick bleed meets the snare tail). The absolute t60 gate above still applies.
                gt60 = list(g['t60_band'].values())[1:4]; nt60 = [round(v, 2) for v in list(info['t60_band'].values())[1:4]]
                report['golden']['t60_mid_expected'] = gt60; report['golden']['t60_mid_got'] = nt60
                if not all(abs(a - b) <= max(0.3 * a, 0.25) for a, b in zip(gt60, nt60)):
                    report['warnings'].append(f'mid-band T60 {nt60} s differs from the golden run {gt60} s by more than 30% / 0.25 s in at least one band (reported, not gated; the tail of every real hit is the record itself)')
        report['stages']['build_s'] = round(time.time() - t, 1); save()
        if G.failed: raise RuntimeError('measurement gate failed')
        # ---------- 7. pack ----------
        sh([sys.executable, os.path.join(PIPE, 'pack_readme.py'), job, artist, title, mixer], cwd=WORK)
        shutil.copy(os.path.join(WORK, f'ZC_Snare_{job}_RoundRobins.zip'), odir); shutil.copy(f'pack2/{job}/ZC_{job}_oneshot.wav', odir)
        shutil.copy(f'pack2/{job}/info.json', odir); shutil.copy(f'pack2/{job}/README.txt', odir)
        report['files'] = dict(zip=f'ZC_Snare_{job}_RoundRobins.zip', oneshot=f'ZC_{job}_oneshot.wav', zip_bytes=os.path.getsize(os.path.join(odir, f'ZC_Snare_{job}_RoundRobins.zip')))
        report['status'] = 'OK'
        json.dump(library.profile(dict(report, status='OK')), open(os.path.join(odir, 'profile.json'), 'w'), indent=1)
    except Exception as e:
        report['status'] = 'FAIL'; report['error'] = str(e); log('FAIL:', e)
        for f_ in glob.glob(os.path.join(odir, 'ZC_*')): os.remove(f_)
    report['gates'] = [dict(name=r['name'], value=r['value'], limit=r['limit'], ok=r['pass_'], note=r['note']) for r in G.rows]
    report['finished'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()); save()
    log('status', report['status'], 'total', round(time.time() - T0, 1), 's')

if __name__ == '__main__':
    main(sys.argv[1])
