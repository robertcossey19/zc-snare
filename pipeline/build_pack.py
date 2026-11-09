"""ZC Snare Extract v3 - rebuild from the DrumSep snare-only stem.
No band gating, no averaged backbone in the audible part: every file is one real hit, full length,
with its own tail as it sits on the record. Usage: python3 build_pack.py <name> [--realvel] [--analyse]
  <name>      : ds/in/<name>.wav (drum stem) and ds/out/<name>/{Kick,Snare,Toms,Hh,Ride,Crash}.wav must exist
  --realvel   : the record contains real quieter snare hits -> medium/soft/ghost layers from REAL hits in level bands
  --analyse   : print candidate lists and stop before writing files
"""
import numpy as np, soundfile as sf, scipy.signal as sg, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import extract, frac_shift, candidates, envdb, SR, PRE
from hit_dsp import shelf, wires, glide, attack, bandsplit, NB, XO
from recon import Prior, reconstruct, layer_prior
EXTRA = int(0.06 * SR)   # 5.0: extra pre-roll handed to the reconstruction (per-hit background frames 55..25 ms before the onset)
FR = int(0.005 * SR)
LEN = int(1.3 * SR)            # analysis window per hit (s)
rng = np.random.RandomState(7)
HP1K = sg.butter(2, 1000, btype='high', fs=SR, output='sos')
STEMS = ['Kick', 'Snare', 'Toms', 'Hh', 'Ride', 'Crash']
REAL_VEL = set()   # or pass --realvel; songs that contain real quieter snare hits: align everything down to -26 dB and build medium/soft/ghost from REAL hits where the record has them
VEL_BANDS = {'hard': (-3, 99), 'medium': (-10, -3), 'soft': (-18, -10), 'ghost': (-30, -18)}   # dB re the loud cluster

def load(name):
    d = f'ds/out'
    S = {}
    for s in STEMS:
        p = f'{d}/{name}_{s}.wav'
        if not os.path.exists(p): p = f'{d}/{name}/{s}.wav'
        S[s], sr = sf.read(p, dtype='float64'); assert sr == SR
    D, _ = sf.read(f'ds/in/{name}.wav', dtype='float64')
    n = min(len(D), *[len(v) for v in S.values()])
    return D[:n], {k: v[:n] for k, v in S.items()}

def env_db(y, fr=FR):
    n = len(y) // fr; E = (y[:n * fr].reshape(n, fr) ** 2).mean(1); return 10 * np.log10(E + 1e-14)

def onsets(stem, lo, hi, height):
    """onset times (samples) from band-energy rise, used for 'what interrupts this hit' bookkeeping"""
    fr = int(0.0025 * SR); m = stem.mean(1)
    c = envdb(sg.sosfilt(sg.butter(4, [lo, hi], btype='band', fs=SR, output='sos'), m), fr)
    g = np.full(len(c), -99.0)
    for i in range(16, len(c) - 6): g[i] = c[i:i + 4].max() - c[i - 16:i - 3].mean()
    pk, _ = sg.find_peaks(g, height=height, distance=int(0.05 / 0.0025))
    return pk * fr, c[pk]

def align_series(x, starts, lags, gains, L):
    out = np.zeros((len(starts), L, 2))
    for j, (a, lag) in enumerate(zip(starts, lags)):
        seg = x[a:a + L]
        if len(seg) < L: seg = np.vstack([seg, np.zeros((L - len(seg), 2))])
        for ch in range(2): out[j, :, ch] = frac_shift(seg[:, ch], lag) / gains[j]
    return out

def build(name, analyse_only=False, realvel=None, strategy=None):
    """strategy: a library.STRATEGIES entry (band, height, cthr, cthr_band); None = the reference recipe A_bright"""
    D, S = load(name); X = S['Snare']
    st = dict(band=(2000, 9000), height=5.0, cthr=0.5, cthr_band=0.4); st.update(strategy or {})
    others = sum(S[k] for k in STEMS if k != 'Snare'); resid = D - (X + others)
    print(name, 'stem rms dBFS:', {k: round(float(20 * np.log10(np.sqrt((v ** 2).mean()) + 1e-12)), 1) for k, v in S.items()}, 'residual', round(float(20 * np.log10(np.sqrt((resid ** 2).mean()) + 1e-12)), 1))
    # ---- 1. hits: detect + sub-sample align on the snare stem itself ----
    import extract as EX; EX.LEN = LEN; EX.P.update(band=tuple(st['band']), height=float(st['height']))
    realvel = (name in REAL_VEL) if realvel is None else realvel
    T0, kept, meta = extract(X, st['cthr'], verbose=False); n = len(kept)
    if realvel:   # quiet hits are aligned against a template of THEIR OWN band (a soft stroke is not a scaled loud stroke); levels then measured absolutely (RMS first 60 ms re 75th pct of the loud set)
        from extract import W as EXW
        sets = [(kept, meta)]
        for lname, (lo, hi) in VEL_BANDS.items():
            if lname == 'hard': continue
            try: _, kb, mb = extract(X, st['cthr_band'], verbose=False, sel_rel=(lo, hi)); sets.append((kb, mb)); print(f'  {lname} band {lo}..{hi} dB: {len(kb)} hits aligned on own template, corr med {np.median(mb["corr"]):.2f}')
            except ValueError as e: print('  ', lname, e)
        raw = np.concatenate([k * np.array(m['gains'])[:, None, None] for k, m in sets]); amp = np.sqrt((raw[:, :PRE + EXW].mean(2) ** 2).mean(1))
        nh = len(kept); amp = amp / np.percentile(amp[:nh], 75)
        kept = raw / amp[:, None, None]; meta = {k: sum([list(m[k]) for _, m in sets], []) for k in ['corr', 'res', 'times', 'starts', 'lags']}; meta['gains'] = amp.tolist(); n = len(kept)
        print(f'  total {n} hits (hard set {nh}); level re loud cluster pct 5/25/50/75/95: {np.percentile(20*np.log10(amp), [5, 25, 50, 75, 95]).round(1)}')
    starts = np.array(meta['starts']); lags = np.array(meta['lags']); gains = np.array(meta['gains']); corr = np.array(meta['corr']); res = np.array(meta['res'])
    hm = (20 * np.log10(gains / (1.0 if realvel else np.median(gains))) >= -3) if realvel else np.ones(n, bool)   # audits below are done on the loud set only (quiet hits normalised up would swamp the averages)
    print(f'  hits aligned {n}; corr med {np.median(corr):.3f}; level sd {np.std(20*np.log10(gains)):.2f} dB; loud set {hm.sum()}')
    # every snare onset incl. ghosts (lower threshold) -> gap to next snare for each kept hit
    so, slv = onsets(X, 1500, 9000, 3.0); hit_t = starts + PRE
    def next_gap(t):
        k = np.where(so > t + int(0.03 * SR))[0]; own = slv[np.argmin(np.abs(so - t))]
        for i in k:
            if slv[i] > own - 30: return (so[i] - t) / SR
        return 9.0
    gap = np.array([next_gap(t) for t in hit_t])
    ko, _ = onsets(S['Kick'], 40, 120, 5.0); kgap = np.array([((ko[ko > t + int(0.005 * SR)].min() - t) / SR) if (ko > t + int(0.005 * SR)).any() else 9.0 for t in hit_t])
    # ---- 2. leakage audit: what the other stems / residual carry at the snare onsets, aligned & coherently averaged ----
    A = {k: align_series(S[k], starts, lags, gains, LEN) for k in ['Kick', 'Hh', 'Ride', 'Crash', 'Toms']}; AR = align_series(resid, starts, lags, gains, LEN); AD = align_series(D, starts, lags, gains, LEN)
    def win_db(a, t0, t1): i0, i1 = PRE + int(t0 * SR), PRE + int(t1 * SR); return 10 * np.log10((a[..., i0:i1, :] ** 2).mean() + 1e-14)
    audit = {}
    for lab, (t0, t1) in {'0-5ms': (0, 0.005), '5-30ms': (0.005, 0.03), '30-150ms': (0.03, 0.15), '150-500ms': (0.15, 0.5), '500-1000ms': (0.5, 1.0)}.items():
        audit[lab] = dict(snare=round(win_db(kept[hm], t0, t1), 1), drums=round(win_db(AD[hm], t0, t1), 1), resid=round(win_db(AR[hm], t0, t1), 1), **{k.lower(): round(win_db(A[k][hm], t0, t1), 1) for k in A})
    print('  energy audit (dBFS, mean over hits):'); [print('   ', k, v) for k, v in audit.items()]
    # coherent (hit-locked) part of the residual = snare energy the separator dropped; incoherent part averages out ~1/N
    w = np.where(hm, 1 / (res + 1e-9), 0); w /= w.sum(); Rc = np.tensordot(w, AR, axes=(0, 0)); Tc = np.tensordot(w, kept, axes=(0, 0)); nn = int(hm.sum())
    coh = {}
    for lab, (t0, t1) in {'0-5ms': (0, 0.005), '5-30ms': (0.005, 0.03), '30-150ms': (0.03, 0.15), '150-500ms': (0.15, 0.5)}.items():
        i0, i1 = PRE + int(t0 * SR), PRE + int(t1 * SR); eR = (Rc[i0:i1] ** 2).mean(); eI = (AR[hm, i0:i1] ** 2).mean(); C = max((eR - eI / nn) / (1 - 1 / nn), 1e-14)
        coh[lab] = dict(coherent_resid_dB=round(10 * np.log10(C), 1), snare_dB=round(10 * np.log10((Tc[i0:i1] ** 2).mean() + 1e-14), 1))
    print('  coherent residual vs snare template:', coh)
    # ---- 3. spectrum check: snare stem hits vs drum-stem hits over the first 60 ms (is the stem spectrally filtered?) ----
    def spec(a, t0, t1):
        i0, i1 = PRE + int(t0 * SR), PRE + int(t1 * SR); seg = a[:, i0:i1, :].mean(2) * np.hanning(i1 - i0); P = (np.abs(np.fft.rfft(seg, axis=1)) ** 2).mean(0); f = np.fft.rfftfreq(i1 - i0, 1 / SR); return f, P
    f, Ps = spec(kept[hm], 0, 0.06); _, Pd = spec(AD[hm], 0, 0.06)
    bands = [(60, 150), (150, 300), (300, 600), (600, 1200), (1200, 2500), (2500, 5000), (5000, 8000), (8000, 12000), (12000, 16000)]
    tilt = {f'{a}-{b}': round(float(10 * np.log10(Ps[(f >= a) & (f < b)].sum() / Pd[(f >= a) & (f < b)].sum())), 1) for a, b in bands}
    print('  snare-stem minus drum-stem level per band, first 60 ms (dB; negative = separator removed energy there, expected where hat/kick live):', tilt)
    # what the separator dropped into NOTHING (not into kick/hat/cymbal stems): snare vs snare+unassigned residual, hit-locked, first 60 ms
    _, Pr = spec(AR[hm], 0, 0.06); dropped = {f'{a}-{b}': round(float(10 * np.log10(Ps[(f >= a) & (f < b)].sum() / (Ps + Pr)[(f >= a) & (f < b)].sum())), 2) for a, b in bands}
    _, Ph = spec(A['Hh'][hm], 0, 0.06); _, Pc = spec(A['Crash'][hm], 0, 0.06); hat_vs_snare = {f'{a}-{b}': round(float(10 * np.log10((Ph + Pc)[(f >= a) & (f < b)].sum() / Ps[(f >= a) & (f < b)].sum())), 1) for a, b in bands}
    i0h, i1h = PRE, PRE + int(0.03 * SR)   # 5.0: cymbal stroke coincident with this hit (hat/ride/crash stems 0-30 ms vs the snare stem 0-30 ms, dB). The first 8 ms of a file are the raw stem: a coincident stroke there is bleed no mask can take out, so selection avoids it
    hat_on = 10 * np.log10(((A['Hh'] + A['Ride'] + A['Crash'])[:, i0h:i1h] ** 2).mean((1, 2)) + 1e-20) - 10 * np.log10((kept[:, i0h:i1h] ** 2).mean((1, 2)) + 1e-20)
    print(f'  cymbal-stroke coincidence (hat+ride+crash vs snare, 0-30 ms, dB) pct 10/50/90: {np.percentile(hat_on, [10, 50, 90]).round(1)}; hits with a stroke within 12 dB: {int((hat_on > -12).sum())} of {n}')
    AO = AD.copy(); AO -= kept; AO -= A['Kick']   # 4.3.0: everything the drum stem carries at this hit that is neither the snare stem nor the kick stem (hat/ride/crash/tom stems + unassigned residual) - where a thin snare stem's tail ends up
    del A
    print('  snare lost to unassigned residual per band (dB; this is the real separation loss):', dropped)
    print('  hat+crash stems vs snare stem at the snare onsets per band (dB; how much cymbal rides the backbeat on this record):', hat_vs_snare)
    # ---- 4. tail: masked (next-snare excluded) median envelope per band -> measured decay slope per band; stem noise floor ----
    E = np.array([env_db(h.mean(1)) for h in kept]); f0 = PRE // FR; t_ax = (np.arange(E.shape[1]) * FR - PRE) / SR
    HB = np.array([bandsplit(h) for h in kept]); EB = np.array([[env_db(HB[j, b].mean(1)) for b in range(NB)] for j in range(n)])
    quiet = env_db(X.mean(1)); floor = float(np.percentile(quiet, 5)); print(f'  snare-stem noise floor (5th pct, 5 ms frames): {floor:.1f} dBFS')
    PL = np.median(E[:, f0 - 4:f0 - 1], 1); PLB = np.median(EB[:, :, f0 - 4:f0 - 1], 2)   # per-hit background measured 20..5 ms before the hit (what sits under the tail that is not this snare)
    pkj = E[:, f0:f0 + 3].max(1); print(f'  pre-hit background rel own peak (dB) pct10/50/90: {np.percentile(PL - pkj, [10, 50, 90]).round(1)}')
    gapmask = np.array([t_ax < gap[j] - 0.015 for j in range(n)])
    def mmed(Eb, bg):   # masked median: only frames before the next snare and >= 8 dB above that hit's own background
        out = np.full(Eb.shape[1], np.nan); cnt = np.zeros(Eb.shape[1], int); m = gapmask & (Eb > bg[:, None] + 8)
        for i in range(Eb.shape[1]):
            v = Eb[m[:, i], i]; cnt[i] = len(v)
            if len(v) >= 6: out[i] = np.median(v)
        return out, cnt
    mf, cnt = mmed(E, PL); pk = float(np.nanmax(mf)); medE = mf
    tailinfo = {f'{int(t*1000)}ms': round(float(mf[f0 + int(t / 0.005)] - pk), 1) for t in [0.01, 0.03, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5] if f0 + int(t / 0.005) < len(mf) and not np.isnan(mf[f0 + int(t / 0.005)])}
    slope = np.zeros(NB); fit_to = np.zeros(NB); nfit = np.zeros(NB, int); iqr = np.zeros(NB); slope_early = np.zeros(NB)
    for b in range(NB):   # per-hit decay fit on its own valid range (>= 8 dB above own background, before the next snare), song rate = median over hits
        sls = []; ends = []; late = []
        for j in range(n):
            if gap[j] < 0.25 or (PL[j] - pkj[j]) > -28: continue
            i0 = f0 + 12; i1 = i0
            while i1 < len(t_ax) and t_ax[i1] < gap[j] - 0.015 and EB[j, b, i1] > PLB[j, b] + 8: i1 += 1
            if i1 - i0 >= 12: sls.append(np.polyfit(t_ax[i0:i1], EB[j, b, i0:i1], 1)[0]); ends.append(t_ax[i1])
            if i1 - (f0 + 30) >= 10: late.append(np.polyfit(t_ax[f0 + 30:i1], EB[j, b, f0 + 30:i1], 1)[0])   # late part only (150 ms -> end of clean range): the rate the continuation must follow
        if len(late) >= 5: slope[b] = float(np.clip(np.median(late), -300, -30)); fit_to[b] = float(np.median(ends)); nfit[b] = len(late); iqr[b] = float(np.subtract(*np.percentile(late, [75, 25])))
        elif len(sls) >= 5: slope[b] = float(np.clip(np.median(sls), -300, -30)); fit_to[b] = float(np.median(ends)); nfit[b] = len(sls); iqr[b] = float(np.subtract(*np.percentile(sls, [75, 25])))
        else: slope[b] = np.nan
        slope_early[b] = float(np.median(sls)) if len(sls) >= 5 else np.nan
    fb = np.nanmedian(slope[1:]) if np.isfinite(slope[1:]).any() else -100.0
    slope = np.where(np.isfinite(slope), slope, fb)
    t60 = {f'band{b}': round(float(-60 / slope[b]), 2) for b in range(NB)}
    print('  tail rel peak:', tailinfo, '| per-band late slope dB/s', slope.round(0), 'early(60-150ms)', slope_early.round(0), 'IQR', iqr.round(0), 'n hits', nfit, 'median fit end ms', (fit_to * 1000).round(0), 'T60', t60)
    # ---- 4b. thin-stem test (4.3.0): on some records (Deftones 'Change') the separator hands the snare's own ring/room beyond ~60 ms to the hat/cymbal stems:
    #      the snare stem falls under its background within 100 ms while the OTHER stems carry a hit-locked, smoothly decaying bump for 200-300 ms (a hat stroke alone is back
    #      at its background by ~100 ms). Measured per band on exposed hits; a band is 'thin' when the other-stem excess at 100 ms >= 4 dB, decays >= 3 dB by 250 ms, and
    #      exceeds the snare stem's own excess at 150 ms by >= 3 dB. Only then is the tail reclaimed from that material (Wiener gain against its pre-hit background).
    expo = [j for j in range(n) if gap[j] > 0.3 and (PL[j] - pkj[j]) < -25]
    if len(expo) > 80: expo = [expo[i] for i in np.linspace(0, len(expo) - 1, 80).astype(int)]
    EOBx = np.array([[env_db(bandsplit(AO[j])[b].mean(1)) for b in range(NB)] for j in expo]) if len(expo) >= 10 else None
    reclaim = np.zeros(NB, bool); thin = {}
    if EOBx is not None:
        bgO = np.median(EOBx[:, :, f0 - 4:f0 - 1], 2); ox = EOBx - bgO[:, :, None]; sx = EB[expo] - PLB[expo][:, :, None]
        for b in range(NB):
            o100, o150, o250 = [float(np.median(ox[:, b, f0 + k])) for k in (20, 30, 50)]; s150 = float(np.median(sx[:, b, f0 + 30]))
            # hat-dependence test: split the exposed hits by how much other-stem energy rides the first 30 ms of the hit in this band (= hat/cymbal stroke on the backbeat).
            # a snare's own tail is the same whether or not a hat was struck with it; a hat's decay is not. Deftones 'Change', >6 kHz: high-hat third +13.1 dB vs low third +2.6 dB
            # at 100 ms -> hat, not reclaimed; 2-6 kHz: +7.6 vs +7.0 -> hit-locked snare ring the separator moved out -> reclaimed.
            hon = EOBx[:, b, f0:f0 + 6].mean(1) - EB[expo][:, b, f0:f0 + 6].mean(1); q = np.argsort(hon); third = max(len(q) // 3, 3); lo_, hi_ = q[:third], q[-third:]
            o100_lo, o250_lo = [float(np.median(ox[lo_, b, f0 + k])) for k in (20, 50)]; o100_hi = float(np.median(ox[hi_, b, f0 + 20]))
            reclaim[b] = (o100_lo >= 4) and (o100_lo - o250_lo >= 3) and (o150 - s150 >= 3) and (o100_hi - o100_lo < 4) and b >= 1
            thin[f'band{b}'] = dict(other_excess_db_100_150_250=[round(o100, 1), round(o150, 1), round(o250, 1)], stem_excess_db_150=round(s150, 1), other_excess_100_low_hat=round(o100_lo, 1), other_excess_100_high_hat=round(o100_hi, 1), reclaim=bool(reclaim[b]))
    print('  thin-stem test (other-stem hit-locked excess vs snare-stem excess, exposed hits):', thin, '-> reclaim bands', reclaim.astype(int).tolist())
    band_on = {}   # per reclaimed band: every stroke on the record in that band's own range in the other-stem material (hat/ride/crash/tom strokes); a decaying tail has no rise, so it does not register
    if reclaim.any():
        Ofull = D - X - S['Kick']
        for b in np.where(reclaim)[0]: band_on[int(b)] = onsets(Ofull, XO[b - 1] if b > 0 else 30, XO[b] if b < NB - 1 else 16000, 5.0)[0]; print(f'    band{b}: {len(band_on[int(b)])} other-stem strokes on the record ({60 * len(band_on[int(b)]) / (len(D) / SR):.0f}/min)')
        del Ofull
    # ---- 5. selection: real full-length hits whose tail is uninterrupted by the next snare, best alignment, typical level/spectrum ----
    finE = np.isfinite(medE[f0:f0 + 30])   # 4.3.0: frames where the masked median exists; on a thin stem (Deftones: tail under background+8 dB from ~100 ms) the old mean() was NaN for every hit -> argsort of NaN -> arbitrary selection
    dev = np.array([np.abs(E[j, f0:f0 + 30][finE] - medE[f0:f0 + 30][finE]).mean() if finE.sum() >= 6 else 0.0 for j in range(n)])   # envelope conformity over first 150 ms
    i0t, i1t = PRE + int(0.03 * SR), PRE + int(0.3 * SR)   # 4.3.0: per-hit tail SNR = this hit's snare-stem energy 30-300 ms vs everything else the drum stem carries in that window (hat/kick/cymbal/room wash)
    tsnr = 10 * np.log10((kept[:, i0t:i1t] ** 2).mean((1, 2)) / (((AD - kept)[:, i0t:i1t] ** 2).mean((1, 2)) + 1e-20))
    print(f'  per-hit tail SNR 30-300 ms (dB) pct 10/50/90: {np.percentile(tsnr, [10, 50, 90]).round(1)}')
    tail_need = 0.6
    SUB = sg.butter(4, [40, 120], btype='band', fs=SR, output='sos'); i0s, i1s = PRE, PRE + int(0.06 * SR)
    sub = np.array([10 * np.log10((sg.sosfilt(SUB, kept[j][i0s:i1s].mean(1)) ** 2).mean() + 1e-14) for j in range(n)]); subx = sub - np.median(sub)
    print(f'  sub-band (40-120 Hz) excess over median, pct 50/90/max: {np.percentile(subx, [50, 90, 100]).round(1)}; hits > +6 dB (kick-coincident leak): {(subx > 6).sum()}')
    gref = 1.0 if realvel else float(np.median(gains)); rel = 20 * np.log10(gains / gref)
    if realvel: print('  level re loud cluster (dB) histogram:', {f'{a}..{a+3}': int(((rel >= a) & (rel < a + 3)).sum()) for a in range(-27, 6, 3)})
    bgrel = PL - pkj; score = np.where(subx > 6, 50, 0) + dev + 10 * (1 - corr) + np.where(gap < tail_need, (tail_need - gap) * 40, 0) + np.where(kgap < 0.03, 5, 0) + np.maximum(bgrel + 40, 0) * 0.6 + np.maximum(6 - tsnr, 0) * 0.4 + np.maximum(hat_on + 15, 0) * 0.8   # 4.3.0: exposure weighs more (bg under the hit, and how much non-snare rides under its tail)
    EXT = [float(v) for v in os.environ.get('ZC_EXCLUDE', '').split(',') if v.strip()]   # per-file QC re-pick: hit times (s) the orchestrator rejected on a previous build
    ex = np.array([any(abs(meta['times'][j] - t) < 0.01 for t in EXT) for j in range(n)]); print(f'  excluded by QC: {int(ex.sum())}')
    order = [int(j) for j in np.argsort(score) if not ex[j]]
    if realvel:   # spectral gate for quiet candidates: a snare has a 150-400 Hz body that rises >= 10 dB at the hit and a 0-30 ms centroid well under 1.5 kHz; hat bleed in the snare stem has neither
        BODY = sg.butter(4, [150, 400], btype='band', fs=SR, output='sos'); fq = np.fft.rfftfreq(int(0.03 * SR), 1 / SR)
        cent = np.zeros(n); brise = np.zeros(n)
        for j in range(n):
            m_ = kept[j].mean(1); seg_ = m_[PRE:PRE + int(0.03 * SR)]; P = np.abs(np.fft.rfft(seg_ * np.hanning(len(seg_)))) ** 2; cent[j] = (P * fq).sum() / (P.sum() + 1e-20)
            bb = sg.sosfilt(BODY, m_); brise[j] = 10 * np.log10((bb[PRE:PRE + int(0.04 * SR)] ** 2).mean() + 1e-14) - 10 * np.log10((bb[PRE - int(0.018 * SR):PRE - int(0.003 * SR)] ** 2).mean() + 1e-14)
        print(f'  quiet-gate: centroid 0-30 ms pct 10/50/90 {np.percentile(cent, [10, 50, 90]).round(0)} Hz; body rise pct 10/50/90 {np.percentile(brise, [10, 50, 90]).round(1)} dB; rejected (cent>1.5k or rise<10): {int(((cent > 1500) | (brise < 10)).sum())} of {n}')
    if realvel:   # per layer: the 4 best-scoring REAL hits in that velocity band; a band with <4 clean real hits is filled from hard hits with the lighter-stroke transform (flagged)
        sel = []; lay_sel = {}; used = set(); T_ = np.asarray(meta['times'], float)
        def near(j): return any(abs(T_[j] - T_[u]) < 0.05 for u in used)   # two onsets aligned to the same stroke must not fill two slots: every file is a distinct hit
        for lname, (lo, hi) in VEL_BANDS.items():
            if lname != 'hard':
                cand = [int(j) for j in np.where((rel >= lo) & (rel < hi))[0]]
                print(f'    {lname} candidates ({len(cand)}): ' + '; '.join(f't{meta["times"][j]:.1f} rel{rel[j]:.0f} gap{int(gap[j]*1000)} bg{bgrel[j]:.0f} sub{subx[j]:.0f} dev{dev[j]:.1f} corr{corr[j]:.2f} sc{score[j]:.0f}' for j in cand[:24]))
            if lname == 'hard':
                c = []
                for j in order:
                    if lo <= rel[j] < hi and j not in used and not any(abs(T_[j] - T_[u]) < 0.05 for u in c) and not near(j): c.append(int(j))
                    if len(c) == 4: break
            else:   # quiet layers: shape conformity to the LOUD median envelope does not apply; need the hit >= 8 dB over its own background, no coincident kick, >= 120 ms to the next snare
                qs = 10 * (1 - corr) + np.maximum(bgrel + 20, 0) + np.maximum(0 - tsnr, 0) * 0.3 + np.maximum(hat_on + 15, 0) * 0.8 + np.where(cent > 1500, 50, 0) + np.where(brise < 10, 30, 0) + np.where(subx > 6, 50, 0) + np.where(gap < 0.12, 40, 0) + np.where(kgap < 0.03, 5, 0) + np.where(bgrel > -8, 50, 0)
                c = []
                for j in np.argsort(qs):
                    if lo <= rel[j] < hi and j not in used and qs[j] < 30 and not ex[j] and not near(j) and corr[j] >= 0.75 * float(np.median(corr[hm])) and hat_on[j] < -9 and not any(abs(T_[j] - T_[u]) < 0.05 for u in c): c.append(int(j))
                    if len(c) == 4: break
            lay_sel[lname] = c; used |= set(c); print(f'  {lname}: {len(c)} real hits in [{lo},{hi}) dB, levels {[round(float(rel[j]),1) for j in c]}, times {[round(meta["times"][j],1) for j in c]}, gaps ms {[int(gap[j]*1000) for j in c]}')
        extra = []   # estimate donors: loud hits not used as real slots, each a distinct stroke
        for j in order:
            if rel[j] >= -3 and j not in used and not near(j) and not any(abs(T_[j] - T_[u]) < 0.05 for u in extra): extra.append(int(j))
        sel = lay_sel['hard']
    else: sel = [int(j) for j in order[:16]]
    print(f'  selected 16 hits: gap to next snare (ms) {[int(gap[j]*1000) for j in sel]}, background rel peak {[int(bgrel[j]) for j in sel]}, score {score[sel[0]]:.2f}..{score[sel[-1]]:.2f}, times {[round(meta["times"][j],1) for j in sel]}')
    if analyse_only: return
    # ---- 5.0 ensemble priors: per layer, the aligned hits of that level band (>= 8) with 60 ms extra pre-roll; the hard prior is the fallback ----
    def ref_set(js, nmax=60):   # the best-exposed hits of the band (selection order = exposure score), with the drum stem's non-snare material for per-frame validity
        js = np.asarray(list(js)[:nmax], int); R = align_series(X, starts[js] - EXTRA, lags[js], gains[js], LEN + EXTRA)
        O = align_series(D, starts[js] - EXTRA, lags[js], gains[js], LEN + EXTRA) - R
        return R, gap[js], O
    priors = {}; layer_of = {}
    hard_js = [j for j in order if rel[j] >= -3] if realvel else list(order)
    if len(hard_js) < 4: hard_js = list(order)
    R_, G_, O_ = ref_set(hard_js); priors['hard'] = Prior(R_, G_, PRE + EXTRA, slope, XO, other=O_); del R_, O_
    print(f"  prior[hard]: {len(hard_js[:60])} hits, frames valid {priors['hard'].valid_frac:.2f}, ensemble median real to {priors['hard'].prior_real_to_ms:.0f} ms (median over bins), sigma pct 10/50/90 {np.percentile(priors['hard'].sig, [10, 50, 90]).round(1)} dB, continuation slope pct 10/50/90 {np.percentile(priors['hard'].slope_bin, [10, 50, 90]).round(0)} dB/s, band late slopes {getattr(priors['hard'], 'slope_band', np.zeros(1)).mean(0).round(0)}")
    if os.environ.get('ZC_PRIOR_DUMP'): _p = priors['hard']; np.savez(os.environ['ZC_PRIOR_DUMP'], M=_p.M, Ms=_p.Ms, sig=_p.sig, real_to=_p.real_to, cnt=_p.cnt, tc=_p.tc, f=_p.f, Bmed=_p.Bmed, slope_bin=_p.slope_bin)
    if realvel:
        q_ = 10 * (1 - corr) + np.maximum(bgrel + 20, 0)
        for lname in ['medium', 'soft', 'ghost']:
            for j in lay_sel[lname]: layer_of[int(j)] = lname
            lo_, hi_ = VEL_BANDS[lname]; js = [int(j) for j in np.argsort(q_) if lo_ <= rel[j] < hi_ and not ex[j]]
            if len(js) >= 30: R_, G_, O_ = ref_set(js); priors[lname] = Prior(R_, G_, PRE + EXTRA, slope, XO, other=O_); del R_, O_; print(f"  prior[{lname}]: {len(js[:60])} hits, frames valid {priors[lname].valid_frac:.2f}, ensemble median real to {priors[lname].prior_real_to_ms:.0f} ms")
            elif len(js) >= 6:   # too few hits for a tail ensemble of their own: the hard ensemble's tail with this layer's measured spectral offset over the first 80 ms (velocity law)
                R_, G_, O_ = ref_set(js); sh_ = Prior(R_, G_, PRE + EXTRA, slope, XO, other=O_); del R_, O_
                priors[lname] = layer_prior(priors['hard'], sh_); print(f"  prior[{lname}]: {len(js)} hits -> hard ensemble + this layer's spectral offset (median {np.median(priors[lname].offset_db):+.1f} dB, 10/90 pct {np.percentile(priors[lname].offset_db, [10, 90]).round(1)})")
            else: print(f"  prior[{lname}]: only {len(js)} hits in band -> hard prior used as mask reference")
    # ---- 6. assemble: real hit untouched; only (a) a measured-floor fade so the file ends in silence instead of stem noise, (b) a fade at the next snare if one arrives before that ----
    def grains(src, length, b, j, seed=0):   # granular late texture from real material (40 ms Hann grains, random offset/sign), unit level
        grain = min(int(0.04 * SR), max(16, len(src) // 2)); hop = grain // 2; win = np.hanning(grain); rs = np.random.RandomState(1000 * b + j + 77 * seed); ext = np.zeros((length + 2 * grain, 2))   # clamp: a hit cut <100 ms in used to wrap to a negative slice ('high <= 0')
        if len(src) <= grain: src = np.vstack([src, np.zeros((grain + 1 - len(src), 2))])
        for k in range(0, len(ext) - grain, hop):
            off = rs.randint(0, len(src) - grain); ext[k:k + grain] += win[:, None] * src[off:off + grain] * rs.choice([-1, 1])
        return ext[:length]
    def finish_hit(j, real_level=False):
        y = kept[j].copy()
        # 5.0 ensemble-constrained reconstruction (recon.py): this hit's own bytes wherever they sit inside the ensemble's per-bin tolerance; bleed /
        # separator holes / the next snare's attack rebuilt at the ensemble-measured magnitude; beyond the ensemble's own floor the prior decays at the band slope (ESTIMATE)
        hitR = align_series(X, [starts[j] - EXTRA], [lags[j]], [gains[j]], LEN + EXTRA)[0]
        pr = priors.get(layer_of.get(j, 'hard'), priors['hard'])
        yR, rinfo = reconstruct(hitR, pr, float(gap[j]), seed=int(j))
        y = yR[EXTRA:LEN + EXTRA]
        # where this hit's own content stops carrying the file: first 20 ms (4 frames) window after 60 ms in which >50 % of the energy-weighted bins were replaced
        ext_ms = None; rec_ms = dict(prior_real_to_ms=int(pr.prior_real_to_ms), replaced_frac=rinfo['replaced_frac'], bleed_frac=rinfo['bleed_frac'], hole_frac=rinfo['hole_frac'])
        n_cut = LEN
        ePre = env_db(kept[j].mean(1)); ePost = env_db(y.mean(1))
        for i in range(f0 + 12, min(len(ePre), len(ePost)) - 4):   # the file leaves this hit's own tail where the reconstruction differs from the raw stem by > 3 dB for 20 ms
            if (np.abs(ePre[i:i + 4] - ePost[i:i + 4]) > 3).all(): n_cut = i * FR; break
        ext_ms = int((n_cut - PRE) / SR * 1000) if n_cut < LEN else None
        # 4.3.1 decay guard (every song, every hit): one snare hit decays. From 60 ms on, no band above 150 Hz may rise more than 3 dB over the lowest
        # level it has already reached in this file; whatever does is another event (next hit's pre-ring, a hat/ride stroke the masks missed, cymbal
        # wash in a continuation) and is held down to that level. It only ever attenuates, never shapes a real decay (ring-mode beating stays within 3 dB).
        Bs = bandsplit(y); yg = np.zeros((LEN, 2)); kg = f0 + 12
        for b in range(NB):
            if b == 0: yg += Bs[b]; continue
            frb = 4 * FR if b == 1 else FR; e = env_db(Bs[b].mean(1), frb); k6 = (f0 * FR) // frb + (12 * FR) // frb
            if len(e) <= k6 + 2: yg += Bs[b]; continue
            em = sg.medfilt(e, 5)   # 5-frame median: a separator-mask flicker (one or two near-silent frames) must not set the floor for the rest of the file
            rm = np.maximum(np.minimum.accumulate(em[k6:]), float(e[f0:f0 + 6].max()) - 70.0)   # and nothing below peak-70 dB is held (inaudible under the stem floor anyway)
            g = np.ones(len(e)); g[k6:] = np.minimum(1.0, 10 ** ((rm + 3 - e[k6:]) / 20))
            yg += Bs[b] * np.interp(np.arange(LEN), np.arange(len(e)) * frb + frb // 2, g)[:, None]
            if os.environ.get('ZC_DEBUG') and g.min() < 0.5: w = np.where(g < 0.5)[0]; print(f'    guard dbg hit t{meta["times"][j]:.1f} band{b}: {len(w)} frames held, first {int((w[0] * frb - PRE) / SR * 1000)} ms, deepest {20 * np.log10(g.min()):.1f} dB at {int((np.argmin(g) * frb - PRE) / SR * 1000)} ms, env there {e[np.argmin(g)]:.1f} vs floor {rm[np.argmin(g) - k6]:.1f}')
        guard_db = float(np.max(np.clip(env_db(y.mean(1)) - env_db(yg.mean(1)), 0, None)[f0 + 12:])) if LEN // FR > f0 + 13 else 0.0; y = yg
        # (c) end the file where the envelope is below -88 dBFS (inaudible; the stem floor is {floor:.0f}), 40 ms fade
        e = env_db(y.mean(1)); end = LEN
        for i in range(f0 + 40, len(e)):
            if e[i] < -88: end = i * FR; break
        fl = int(0.04 * SR); a0 = max(end - fl, 0); wdw = np.ones(LEN); wdw[a0:end] = 0.5 * (1 + np.cos(np.pi * np.arange(end - a0) / max(end - a0, 1))); wdw[end:] = 0; y = y * wdw[:, None]
        # (d) onset: the STFT separator smears ~15 ms of pre-echo ahead of the stick hit; the true onset is read off the aligned time-domain drum stem
        #     (no pre-echo): walk back from the attack peak until the 0.2 ms-smoothed level drops under max(3 % of peak, 2x the pre-hit level), start 0.3 ms before that
        dm = np.abs(sg.sosfilt(HP1K, AD[j].mean(1))); sm = np.convolve(dm, np.ones(9) / 9, mode='same'); pkx = PRE - int(0.005 * SR) + sm[PRE - int(0.005 * SR):PRE + int(0.03 * SR)].argmax()
        pre = np.median(sm[PRE - int(0.015 * SR):PRE - int(0.008 * SR)]); thr = max(0.05 * sm[pkx], 3 * pre); n0 = pkx
        while n0 > 0 and sm[n0] > thr: n0 -= 1
        ss = np.convolve(np.abs(sg.sosfilt(HP1K, y.mean(1))), np.ones(9) / 9, mode='same'); pks = PRE - int(0.005 * SR) + ss[PRE - int(0.005 * SR):PRE + int(0.03 * SR)].argmax()
        n10 = PRE - int(0.005 * SR) + int(np.argmax(ss[PRE - int(0.005 * SR):pks + 1] > 0.1 * ss[pks]))   # snare stem itself: first sample within 20 dB of its attack peak
        pre_s = np.median(ss[PRE - int(0.015 * SR):PRE - int(0.008 * SR)]); thr_s = max(0.05 * ss[pks], 3 * pre_s); n0s = pks
        while n0s > 0 and ss[n0s] > thr_s: n0s -= 1   # same walk-back on the snare stem itself (the drum stem is unreliable for quiet hits: its louder kick/hat set the threshold)
        n0 = max(min(n0, n0s), n10 - int(0.0007 * SR))   # earliest of the two onsets, but never more than 0.7 ms ahead of the snare stem's own -20 dB crossing (pre-echo sits ~30 dB down)
        st = max(n0 - int(0.0003 * SR), 0); k = int(0.0003 * SR)
        if real_level:   # quiet hits sit in busy context: the walk-back thresholds (3x pre-level) stop right under the peak and would clip the attack. Start instead where the snare stem's own attack envelope last crossed -10.5 dB re its peak (0.5 ms margin, 1 ms fade)
            w0 = PRE - int(0.005 * SR); eb = np.convolve(np.abs(y.mean(1)), np.ones(int(0.001 * SR)) / int(0.001 * SR), mode='same'); pkb = w0 + eb[w0:PRE + int(0.03 * SR)].argmax()
            idx = np.where(eb[w0:pkb] < 0.3 * eb[pkb])[0]; n3 = w0 + idx[-1] + 1 if len(idx) else w0   # broadband 1 ms envelope (soft hits are body-dominant, and the 0.2 ms HP envelope oscillates cycle by cycle)
            st = min(st, max(n3 - int(0.0005 * SR), 0)); k = int(0.001 * SR)
        fi = np.ones(LEN); fi[:st] = 0; fi[st:st + k] = 0.5 * (1 - np.cos(np.pi * np.arange(k) / k)); pre_echo_ms = round((pkx - st) / SR * 1000, 2)
        y = (y * fi[:, None])[st:end]
        lv = float(np.clip(rel[j], -30, 1.5)) if real_level else float(np.clip(rel[j], -1.5, 1.5))   # real layers keep the record's actual level re the loud cluster; hard = natural spread, capped
        return y * 10 ** (lv / 20), dict(t=round(meta['times'][j], 2), gap_ms=int(gap[j] * 1000), bg_rel_peak_db=round(float(bgrel[j]), 1), sub_excess_db=round(float(subx[j]), 1), cymbal_coincident_db=round(float(hat_on[j]), 1), guard_db=round(guard_db, 1), real_to_ms=ext_ms, reclaimed_ms=rec_ms, attack_to_peak_ms=pre_echo_ms, len_ms=int(len(y) / SR * 1000), dbg=dict(st=round((st - PRE) / SR * 1000, 2), n0d=round((n0 - PRE) / SR * 1000, 2), n0s=round((n0s - PRE) / SR * 1000, 2), n10=round((n10 - PRE) / SR * 1000, 2), pkx=round((pkx - PRE) / SR * 1000, 2), pks=round((pks - PRE) / SR * 1000, 2), end_ms=int(end / SR * 1000)), lvl_db=round(float(lv), 2), corr=round(float(corr[j]), 3))
    layers = {'hard': [], 'medium': [], 'soft': [], 'ghost': []}; hinfo = []; layers_real = {}
    spec_v = {'medium': dict(tilt=[(3000, -2.5)], w=0.9, g=0.8, a=0.95, lv=-6), 'soft': dict(tilt=[(2000, -5)], w=0.75, g=0.5, a=0.85, lv=-12), 'ghost': dict(tilt=[(1500, -8), (5000, -4)], w=0.6, g=0.3, a=0.7, lv=-20)}
    def est(j, lname):
        p = spec_v[lname]; y, inf = finish_hit(j)
        for f0s, gdb in p['tilt']: y = shelf(y, f0s, gdb)
        y = wires(y, p['w']); y = glide(y, p['g']); y = attack(y, p['a']); y = y * 10 ** ((p['lv'] + rng.uniform(-0.7, 0.7)) / 20); inf.update(layer=lname, real=False, rel_db=p['lv']); return y, inf
    if realvel:
        hits = []
        for j in lay_sel['hard']: y, inf = finish_hit(j); inf.update(layer='hard', real=True, rel_db=round(float(rel[j]), 1)); hits.append(y); hinfo.append(inf)
        layers['hard'] = hits; layers_real['hard'] = [True] * len(hits)
        for lname in ['medium', 'soft', 'ghost']:
            flags = []
            for j in lay_sel[lname]: y, inf = finish_hit(j, real_level=True); inf.update(layer=lname, real=True, rel_db=round(float(rel[j]), 1)); layers[lname].append(y); hinfo.append(inf); flags.append(True)
            while len(layers[lname]) < 4:
                if not extra: extra = list(lay_sel['hard'])   # tiny loud set: reuse hard hits as donors rather than crash
                j = extra.pop(0); y, inf = est(j, lname); layers[lname].append(y); hinfo.append(inf); flags.append(False)
            layers_real[lname] = flags
        print('  layers real/estimate:', {k: sum(v) for k, v in layers_real.items()})
    else:
        hits = []
        for j in sel: y, inf = finish_hit(j); hits.append(y); hinfo.append(inf)
        for i in range(4): layers['hard'].append(hits[i]); hinfo[i].update(layer='hard', real=True)
        for li, lname in enumerate(['medium', 'soft', 'ghost']):
            p = spec_v[lname]
            for i in range(4):
                y = hits[4 * (li + 1) + i]
                for f0s, gdb in p['tilt']: y = shelf(y, f0s, gdb)
                y = wires(y, p['w']); y = glide(y, p['g']); y = attack(y, p['a']); y = y * 10 ** ((p['lv'] + rng.uniform(-0.7, 0.7)) / 20); layers[lname].append(y); hinfo[4 * (li + 1) + i].update(layer=lname, real=False)
        layers_real = {k: [k == 'hard'] * 4 for k in layers}
    peak = max(np.abs(h).max() for h in layers['hard']); G = 10 ** (-1 / 20) / peak
    def to48(y): return sg.resample_poly(y * G, 160, 147, axis=0)
    out = f'pack2/{name}'; os.makedirs(out, exist_ok=True)
    for lname in ['ghost', 'soft', 'medium', 'hard']:
        for i, y in enumerate(layers[lname]):
            sf.write(f'{out}/ZC_{name}_{lname}_rr{i + 1}.wav', to48(y), 48000, subtype='PCM_24'); sf.write(f'{out}/flac_{lname}_{i + 1}.flac', to48(y), 48000, format='FLAC', subtype='PCM_24')
    sf.write(f'{out}/ZC_{name}_oneshot.wav', to48(layers['hard'][0]), 48000, subtype='PCM_24')
    info = dict(song=name, hits_aligned=n, corr_median=round(float(np.median(corr)), 3), level_sd_db=round(float(np.std(20 * np.log10(gains))), 2), noise_floor_dbfs=round(floor, 1), tail_rel_peak_db=tailinfo, slope_db_s=slope.round(0).tolist(), slope_early_db_s=[None if np.isnan(v) else float(v) for v in slope_early.round(0)], fit_to_ms=(fit_to*1000).round(0).tolist(), t60_band=t60, audit=audit, coherent_resid=coh, stem_vs_drums_tilt_db=tilt, lost_to_resid_db=dropped, hat_vs_snare_db=hat_vs_snare, thin_stem=thin, reclaim_bands=reclaim.astype(int).tolist(), selected=hinfo, layers_real=layers_real, real_velocity=realvel, strategy=st)
    json.dump(info, open(f'{out}/info.json', 'w'), indent=1); print('  wrote', out)
    return info

if __name__ == '__main__':
    build(sys.argv[1], analyse_only=('--analyse' in sys.argv or 'analyse' in sys.argv[2:]), realvel=('--realvel' in sys.argv))
