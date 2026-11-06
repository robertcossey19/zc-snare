"""Collective snare library: every song that produced a pack leaves a measured profile behind, and every new song is
placed against that library before any decision is made.

What this is (honestly): a calibration database + strategy selection with fallbacks. It is not a trained model.
 - profile(report)  : the compact measured fingerprint of one finished song (separation, hit statistics, spectrum, decay, hat load)
 - load(root)       : all OK profiles in packs/*/report.json plus library/*.json seeds (the shipped reference packs)
 - nearest(p, lib)  : closest library song by normalised distance over the features that decide how a record behaves
 - ranges(lib)      : min/max of each feature over the library -> 'within library range' / 'outside library range' notes
 - strategy_order() : which detection/alignment parameter sets to try, nearest reference's winning strategy first

STRATEGIES are the parameter sets that produced the shipped packs. Each one is a complete recipe for the hit detector
(candidate band + rise threshold), the aligner (correlation floor), and the per-file QC (hat-bleed centroid limit scale).
The separation (Demucs htdemucs -> MDX23C DrumSep, sha-verified) is identical for every song and every strategy.
"""
import glob, json, math, os

STRATEGIES = {
    # name: candidate band (Hz), rise height (dB), aligner corr floor, template corr floor for velocity bands, note
    'A_bright':   dict(band=(2000, 9000), height=5.0, cthr=0.50, cthr_band=0.40, note='reference recipe (Architects, BMTH, Nothing More, Limp Bizkit, Nickelback): crack-band 2-9 kHz, 5 dB rise'),
    'B_dark':     dict(band=(1200, 6000), height=4.0, cthr=0.45, cthr_band=0.38, note='darker / lo-fi snare or <160 kbps source: lower crack band, 4 dB rise, corr floor 0.45'),
    'C_dense':    dict(band=(2500, 10000), height=6.5, cthr=0.55, cthr_band=0.42, note='dense mix with hat/crash on the backbeat: tighter band, 6.5 dB rise so hat rises alone do not become candidates'),
    'D_sparse':   dict(band=(1500, 9000), height=3.5, cthr=0.40, cthr_band=0.35, note='sparse or quiet-snare record (few hits aligned on A): 3.5 dB rise, corr floor 0.40'),
}
ORDER_DEFAULT = ['A_bright', 'C_dense', 'B_dark', 'D_sparse']

# features used for the nearest-reference distance: (key path in profile, scale = one 'unit' of difference)
FEATURES = [('hat_vs_snare_5_8k_db', 4.0), ('coherent_resid_below_snare_db', 8.0), ('separation_residual_below_drums_db', 3.0),
            ('hits_per_min', 25.0), ('corr_median', 0.06), ('level_sd_db', 1.5), ('tilt_5_8k_db', 3.0), ('t60_mid_s', 0.3), ('input_kbps', 80.0), ('hat_minus_snare_stem_db', 4.0)]


def profile(report):
    """compact fingerprint of a finished song; returns None when the report lacks measurements"""
    m = report.get('measurements') or {}
    if not m: return None
    coh = m.get('coherent_resid_0_5ms') or {}; hvs = m.get('hat_vs_snare_db') or {}; tilt = m.get('tilt') or {}; t60 = list((m.get('t60_band') or {}).values())
    dur = report.get('duration_s') or 0
    return dict(
        job=report.get('job'), artist=report.get('artist'), title=report.get('title'), status=report.get('status'), pipeline=report.get('pipeline'),
        strategy=report.get('strategy_used', 'A_bright'), input_sha256=report.get('input_sha256'),
        hits_aligned=m.get('hits_aligned'), hits_per_min=round(60.0 * (m.get('hits_aligned') or 0) / dur, 1) if dur else None,
        corr_median=m.get('corr_median'), level_sd_db=m.get('level_sd_db'),
        coherent_resid_below_snare_db=round(coh['snare_dB'] - coh['coherent_resid_dB'], 1) if coh else None,
        separation_residual_below_drums_db=report.get('separation_residual_below_drums_db'),
        hat_vs_snare_5_8k_db=hvs.get('5000-8000'), hat_vs_snare_2_5_5k_db=hvs.get('2500-5000'),
        tilt_5_8k_db=tilt.get('5000-8000'), lost_to_resid_db=m.get('lost_to_resid_db'),
        t60_band=m.get('t60_band'), t60_mid_s=round(sum(t60[1:4]) / 3, 2) if len(t60) >= 4 else None,
        noise_floor_dbfs=m.get('noise_floor_dbfs'), layers_real=report.get('layers_real'),
        input_kbps=round((report.get('input_bitrate') or 0) / 1000), input_codec=report.get('input_codec'), duration_s=dur,
        stem_rms_dbfs=report.get('stem_rms_dbfs'), hat_minus_snare_stem_db=round(report['stem_rms_dbfs']['Hh'] - report['stem_rms_dbfs']['Snare'], 1) if report.get('stem_rms_dbfs') else None,
        warnings=len(report.get('warnings') or []))


def load(root):
    lib = {}
    for p in sorted(glob.glob(os.path.join(root, 'library', '*.json'))):
        try:
            d = json.load(open(p))
            if d.get('status') == 'OK' and d.get('hits_aligned'): lib[d['job']] = d
        except Exception: pass
    for p in sorted(glob.glob(os.path.join(root, 'packs', '*', 'report.json'))):
        try:
            r = json.load(open(p))
            if r.get('status') != 'OK': continue
            d = profile(r)
            if d and d.get('hits_aligned'): lib[d['job']] = d
        except Exception: pass
    return lib


def _dist(a, b):
    s = 0.0; n = 0
    for k, sc in FEATURES:
        if a.get(k) is None or b.get(k) is None: continue
        s += ((a[k] - b[k]) / sc) ** 2; n += 1
    return math.sqrt(s / n) if n else 9.9


def nearest(p, lib, k=3):
    rows = sorted(((round(_dist(p, q), 2), q) for q in lib.values()), key=lambda r: r[0])
    return [dict(job=q['job'], artist=q.get('artist'), title=q.get('title'), distance=d, strategy=q.get('strategy', 'A_bright')) for d, q in rows[:k]]


def ranges(lib):
    out = {}
    for k, _ in FEATURES + [('lost_worst_db', 1), ('noise_floor_dbfs', 1)]:
        vals = []
        for q in lib.values():
            v = q.get(k)
            if k == 'lost_worst_db' and q.get('lost_to_resid_db'): v = -min(q['lost_to_resid_db'].values())
            if v is not None: vals.append(v)
        if vals: out[k] = (round(min(vals), 2), round(max(vals), 2), len(vals))
    return out


def place(p, lib):
    """notes comparing this song to the library, feature by feature"""
    notes = []; rg = ranges(lib)
    for k, (lo, hi, n) in rg.items():
        v = p.get(k)
        if k == 'lost_worst_db' and p.get('lost_to_resid_db'): v = -min(p['lost_to_resid_db'].values())
        if v is None: continue
        if v < lo or v > hi: notes.append(f'{k} = {v}: outside the library range {lo}..{hi} (n={n})')
    return notes


def strategy_order(pre, lib):
    """pre: the partial profile known BEFORE the build (separation residual, stem levels, input kbps, hat load on the drum stem).
    Nearest library songs vote for their winning strategy; the rest follow in default order."""
    order = []
    if lib:
        for nb in nearest(pre, lib, k=3):
            if nb['strategy'] in STRATEGIES and nb['strategy'] not in order: order.append(nb['strategy'])
    if pre.get('input_kbps') and 0 < pre['input_kbps'] < 160:   # lossy under 160 kbps: the dark recipe is the first fallback (HF ceiling and pre-echo blur the 2-9 kHz rise)
        if 'B_dark' in order: order.remove('B_dark')
        order.insert(1 if order else 0, 'B_dark')
    for s in ORDER_DEFAULT:
        if s not in order: order.append(s)
    return order
