"""Ensemble-constrained reconstruction of one real snare hit (pipeline 5.0).

Every hit the record contains is one realisation of the same instrument in the same room through the same
chain. Bleed (hat, ride, kick, guitars, vocals) is not locked to the snare: it differs from hit to hit. So the
ensemble of aligned hits gives, per STFT bin, the snare's typical magnitude M(f,t) (median over hits, frames
before each hit's next snare only) and the hit-to-hit spread sigma(f,t). One hit's bin that sits far above
M + sigma is bleed; far below M is a separator hole. Everything inside the band is that hit's own real content
and is left untouched (same bytes), so round robins stay distinct real strokes.

Replaced bins get the ensemble magnitude M (the level the record's snare really has there, measured, not
synthesised) with the hit's own phase where the excess is small, otherwise a phase made consistent by a few
Griffin-Lim passes over the replaced bins only (below 700 Hz the bin phase is propagated frame to frame, a
decaying drum mode; above, late reverb is noise-like). Beyond the point where the ensemble median itself falls
into the stem floor, M is continued per band at the song's measured decay slope (that part is an ESTIMATE and
is reported as such: 'real_to_ms' / 'prior_real_to_ms').

The first 8 ms (stick, head crack) are never touched: time-domain crossfade from the raw hit into the
reconstruction between 8 and 18 ms.
"""
import numpy as np, scipy.signal as sg, warnings
from scipy.ndimage import uniform_filter, binary_dilation
SR = 44100; NFFT = 1024; HOP = 256
PROP_F = 700.0     # below this: phase-propagated (tonal drum modes); above: random/GL (noise-like reverb/wires)
FILL_LOW_DB = 1.5  # holes are filled 1.5 dB under this hit's level (a quieter bin may be this hit's own; the separator ducking it under a kick is the common case)

def stft(x):
    return sg.stft(x, fs=SR, window='hann', nperseg=NFFT, noverlap=NFFT - HOP, boundary='zeros', padded=True)[2]

def istft(Z, L):
    y = sg.istft(Z, fs=SR, window='hann', nperseg=NFFT, noverlap=NFFT - HOP, boundary=True)[1]
    if len(y) < L: y = np.concatenate([y, np.zeros(L - len(y))])
    return y[:L]

def frame_times(nfr, pre):
    """centre time (s, re onset) of each STFT frame for a segment whose onset sits 'pre' samples in"""
    return (np.arange(nfr) * HOP - pre) / SR

class Prior:
    """M (dB) per channel/bin/frame from the aligned reference set; floor and extrapolation."""
    def __init__(self, ref, gaps, pre, slopes_db_s, xo, floor_db_gap=8.0, other=None):
        """ref (n,L,2) aligned gain-normalised snare-stem hits; other (n,L,2) what else the drum stem carries at those hits (drums - snare), same alignment.
        A frame of hit j counts for the ensemble only while it is before j's next snare AND the other material is not louder than j's snare there
        (a kick or hat landing in the tail makes the separator duck the snare: that frame says nothing about the snare's tail)."""
        n, L, _ = ref.shape; self.pre = pre; self.L = L; self.xo = list(xo)
        A = np.stack([[np.abs(stft(ref[j, :, c])) for c in range(2)] for j in range(n)]).astype(np.float32)  # (n,2,K,T)
        AdB = 20 * np.log10(A + 1e-9); K, T = AdB.shape[2:]; tc = frame_times(T, pre); self.tc = tc
        # decisions are taken on 3 bin x 3 frame power-smoothed magnitudes (a single STFT bin of noise-like material scatters ~5.6 dB
        # hit to hit even with no bleed at all; smoothing brings the natural spread down to ~2-3 dB so real bleed stands out)
        AsdB = 10 * np.log10(uniform_filter(A ** 2, size=(1, 1, 3, 3), mode='nearest') + 1e-18)
        f = np.fft.rfftfreq(NFFT, 1 / SR); self.f = f
        # frames valid for hit j: before its next snare (15 ms margin)
        valid = tc[None, :] < (np.asarray(gaps)[:, None] - 0.015)                     # (n,T)
        band_of = np.digitize(f, xo)                                                    # 0..len(xo)
        nb = len(xo) + 1
        V = np.broadcast_to(valid[:, None, None, :], AdB.shape).copy()                 # (n,2,K,T) per-bin validity
        if other is not None:
            # per hit, channel and band: the energy of what else the drum stem carries; an EVENT (kick in bands 1-2, hat/ride in 3-4) is
            # > 10 dB above that hit's own quiet level in the band. In those frames the separator ducks the snare in that band, so
            # the frame is dropped from the ensemble for the bins of that band only (the other bands of the same hit still count).
            Ao = np.stack([[np.abs(stft(other[j, :, c])) for c in range(2)] for j in range(n)]).astype(np.float32)
            k30 = int(np.argmax(tc >= 0.03))
            ev_any = np.zeros((n, 2, T), bool); ev_b = {}
            for b in range(nb):
                kk = band_of == b
                if not kk.any(): continue
                E = 10 * np.log10((Ao[:, :, kk, :] ** 2).sum(2) + 1e-14)              # (n,2,T)
                Es_ = 10 * np.log10((A[:, :, kk, :] ** 2).sum(2) + 1e-14)             # this hit's own snare energy in the band
                Em = np.where(valid[:, None, :], E, np.nan); Em[:, :, :k30] = np.nan
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore'); fl = np.nanpercentile(Em, 10, axis=2)   # (n,2) quiet level of the other material per hit
                # an event: other material > 10 dB over this hit's quiet level AND within 6 dB of (or over) the snare's own level in the band. The
                # second clause keeps the separator's hit-locked leak of the snare into the other stems (always present, 10-20 dB under the snare,
                # decaying with it) from flagging every early frame on a dense record (Deftones: 0 valid frames 30-100 ms without it)
                ev = (E > np.nan_to_num(fl, nan=-200.0)[:, :, None] + 10.0) & (E > Es_ - 6.0); ev[:, :, :k30] = False
                ev_any |= ev; ev_b[b] = ev
            # the separator's mask re-allocates energy across stems at an event: a kick (bands 0-1) ducks the whole snare, so it drops the whole
            # frame of that hit; a hat/ride/crash stroke (bands 2-4) ducks its own band and the neighbours, which stay in for the other bands
            for b in range(nb):
                if b not in ev_b: continue
                lo_b, hi_b = (0, nb - 1) if b <= 1 else (b - 1, b + 1)
                kk = (band_of >= lo_b) & (band_of <= hi_b)
                V[:, :, kk, :] &= ~ev_b[b][:, :, None, :]
            del Ao
            # late decay rate per band, measured on the longer-lived per-band-valid ensemble (a frame with only a hat stroke in it still tells
            # the truth about the body's level): band energy per hit -> median over hits -> robust line over [100 ms, end of its real region]
            self.slope_band = np.full((2, nb), np.nan)
            for b in range(nb):
                kk = band_of == b
                if not kk.any(): continue
                Eh = 10 * np.log10((A[:, :, kk, :] ** 2).sum(2) + 1e-18)              # (n,2,T)
                Vb = valid[:, None, :] & ~ev_b[b]
                Em = np.where(Vb, Eh, np.nan); cb = Vb.sum(0)
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore'); Eb = np.nanmedian(Em, axis=0)      # (2,T)
                prefr = (tc > -0.056) & (tc < -0.024)
                Bb = np.percentile(np.median(Eh[:, :, prefr], axis=2), 10, axis=0) if prefr.sum() >= 2 else np.full(2, -200.0)
                for c in range(2):
                    ok = np.isfinite(Eb[c]) & (cb[c] >= 6) & (Eb[c] > Bb[c] + floor_db_gap); k100 = int(np.argmax(tc >= 0.10)); k40 = int(np.argmax(tc >= 0.04))
                    bad = np.where(~ok[k40:])[0]; te = k40 + bad[0] if len(bad) else T
                    t0 = k100 if te - k100 >= 10 else k40
                    tt = np.arange(t0, te); tt = tt[np.isfinite(Eb[c, tt])]
                    if len(tt) < 8: continue
                    x = tc[tt]; yy = Eb[c, tt]; w = np.ones(len(yy))
                    for _ in range(3):
                        co = np.polyfit(x, yy, 1, w=np.sqrt(w)); r = yy - np.polyval(co, x); w = 1.0 / np.maximum(np.abs(r), 2.0)
                    self.slope_band[c, b] = float(co[0])
        self.valid_frac = float(V.mean())
        AdB_m = np.where(V, AdB, np.nan); AsdB_m = np.where(V, AsdB, np.nan)
        cnt = V.sum(0)                                                                  # (2,K,T)
        with np.errstate(all='ignore'), warnings.catch_warnings():
            warnings.simplefilter('ignore')
            M = np.nanmedian(AdB_m, axis=0)                                   # (2,K,T) per-bin median magnitude (fill level)
            Ms = np.nanmedian(AsdB_m, axis=0)                                 # smoothed median (decision reference)
            sig = 1.4826 * np.nanmedian(np.abs(AsdB_m - Ms[None]), axis=0)    # robust hit-to-hit spread of the smoothed magnitude
        del AsdB_m, AdB_m, V
        self.sig = np.clip(np.nan_to_num(sig, nan=3.0), 1.5, 6.0)
        self.Ms = np.nan_to_num(Ms, nan=-120.0)
        # per-hit background: frames centred 55..25 ms before the onset; ensemble median -> what sits under a tail that is not this snare
        pre_fr = (tc > -0.056) & (tc < -0.024)
        B = np.median(AdB[:, :, :, pre_fr], axis=3) if pre_fr.sum() >= 2 else np.full((n, 2, K), -120.0)   # (n,2,K)
        self.Bmed = np.percentile(B, 10, axis=0)                                # (2,K) hits preceded by nothing give the stem's real floor under a tail; the median would be the previous hit's tail on a busy record
        # the prior is real while it is >= floor_db_gap above the ensemble background and rests on >= 6 hits; from the last
        # such frame each bin continues at its band's measured slope (ESTIMATE region)
        sl = np.asarray(slopes_db_s, float)[band_of]                           # (K,)
        onset_fr = int(np.argmax(tc >= 0.03))
        Mx = M.copy(); real_to = np.zeros((2, K), int)
        for c in range(2):
            for k in range(K):
                ok = np.isfinite(M[c, k]) & (cnt[c, k] >= 6) & (M[c, k] > self.Bmed[c, k] + floor_db_gap)
                ok[:onset_fr] = True
                idx = np.where(~ok[onset_fr:])[0]
                te = onset_fr + idx[0] if len(idx) else T
                # also stop at the first frame where the median has flattened (within 3 dB of its running minimum for 60 ms)
                real_to[c, k] = te
                if te < T:
                    base = M[c, k, te - 1] if te > 0 and np.isfinite(M[c, k, te - 1]) else self.Bmed[c, k]
                    Mx[c, k, te:] = base + sl[k] * (tc[te:] - tc[te - 1])
        # from 40 ms on a snare's ring/room decay is close to exponential (linear in dB, a little concave). Per bin, a robust quadratic fit over the real
        # region; the median is clamped to fit +-4 dB. That keeps ring-mode beating (+-3 dB) and removes two things the median cannot: a consistent later
        # event (hat/kick on the next 8th in most bars -> bump) and the separator ducking the snare under that event (-> dip and recovery, Architects at 200 ms)
        k40 = int(np.argmax(tc >= 0.04)); self.clamp_db = np.zeros((2, K)); self.slope_bin = np.tile(sl, (2, 1)).astype(float)
        for c in range(2):
            for k in range(K):
                te = int(real_to[c, k]); tt = np.arange(k40, max(te, k40))
                y = Mx[c, k, tt]; good = np.isfinite(y)
                if good.sum() < 8: continue
                x = tc[tt[good]]; yy = y[good]; w = np.ones(len(yy))
                for _ in range(3):
                    co = np.polyfit(x, yy, 2, w=np.sqrt(w)); r = yy - np.polyval(co, x); w = 1.0 / np.maximum(np.abs(r), 2.0)
                fit = np.polyval(co, tc[tt]); self.clamp_db[c, k] = float(np.max(np.abs(np.nan_to_num(Mx[c, k, tt] - fit, nan=0.0))))
                Mx[c, k, tt] = np.clip(Mx[c, k, tt], fit - 4.0, fit + 4.0)
                if te < T:   # continuation restarts from the clamped end value at the rate this bin was measured decaying over its real region (fit slope at the end, clipped to a drum's range), else the band's rate
                    # the rate: a robust straight line (dB vs s) over the bin's real region from 40 ms; the quadratic's end derivative is dominated by the
                    # last frames, which on a busy record are already the transition into the ducked/invalid region (-> a cliff at ~200 ms, not a decay)
                    if len(tt) >= 12:
                        w1 = np.ones(len(yy))
                        for _ in range(3):
                            c1 = np.polyfit(x, yy, 1, w=np.sqrt(w1)); r1 = yy - np.polyval(c1, x); w1 = 1.0 / np.maximum(np.abs(r1), 2.0)
                        s_end = float(c1[0])
                    else: s_end = sl[k]
                    sb_ = self.slope_band[c, band_of[k]] if hasattr(self, 'slope_band') else np.nan
                    if np.isfinite(sb_): s_end = sb_          # the band's measured late rate beats a line through this bin's early region
                    hi_clip = -60.0 if tc[te - 1] >= 0.08 else -90.0   # a bin whose evidence ends before 80 ms has no measured late rate: keep it inside a snare's range (t60 <= 0.67 s)
                    s_use = float(np.clip(s_end, -300.0, hi_clip)) if np.isfinite(s_end) else min(sl[k], hi_clip); self.slope_bin[c, k] = s_use
                    Mx[c, k, te:] = min(Mx[c, k, te - 1], fit[-1] + 4.0) + s_use * (tc[te:] - tc[te - 1])
        # and never louder later: cap at running-min + 3 dB
        rm = np.minimum.accumulate(np.nan_to_num(Mx[:, :, k40:], nan=-120.0), axis=2)
        Mx[:, :, k40:] = np.minimum(Mx[:, :, k40:], rm + 3.0)
        Mn = np.nan_to_num(M, nan=-120.0); Mxn = np.nan_to_num(Mx, nan=-120.0)
        self.Ms = self.Ms + (Mxn - Mn)   # the smoothed decision reference follows the same continuation/cap as the fill level
        self.M = Mxn; self.real_to = real_to; self.cnt = cnt; self.n = n
        self.prior_real_to_ms = float(np.median(tc[np.clip(real_to, 0, T - 1)]) * 1000)

def extend_prior(P, Q, min_frames=4):
    """Where P's ensemble stops being real early in a bin (busy record: every hard hit has a hat/ride landing in its tail) and another layer Q of
    the same drum is still measured there, continue P's bin with Q's measured decay SHAPE (level matched over the last 3 real frames of P), then
    Q's continuation. The drum's ring/room decay is a property of the drum and the room, not of the stroke level, so the quieter layer's tail is
    a real measurement of the same decay. Returns the number of bins extended; P.real_to is advanced to Q's (still reported as the estimate boundary
    for the frames P itself could not measure: P.ext_from keeps P's own boundary)."""
    T = P.M.shape[2]; n_ext = 0
    if not hasattr(P, 'ext_from'): P.ext_from = P.real_to.copy()
    for c in range(2):
        for k in range(P.M.shape[1]):
            te = int(P.real_to[c, k]); tq = int(Q.real_to[c, k])
            if te >= T or tq - te < min_frames: continue
            a = slice(max(te - 3, 0), te)
            if not (np.all(np.isfinite(P.M[c, k, a])) and np.all(np.isfinite(Q.M[c, k, a]))): continue
            off = float(np.median(P.M[c, k, a] - Q.M[c, k, a]))
            new = Q.M[c, k, te:] + off
            new = np.minimum(new, P.M[c, k, te - 1] + 3.0)            # never louder than where P's own measurement ended
            d = new - P.M[c, k, te:]
            P.M[c, k, te:] = new; P.Ms[c, k, te:] += d
            P.real_to[c, k] = tq; P.slope_bin[c, k] = Q.slope_bin[c, k]; n_ext += 1
    P.prior_real_to_ms = float(np.median(P.tc[np.clip(P.real_to, 0, T - 1)]) * 1000)
    return n_ext

def layer_prior(hard, short, upto_s=0.08, lim=(-24.0, 6.0)):
    """Prior for a quieter layer from few hits: the hard layer's full ensemble (its tail is measured on 60 hits) with the per-bin level offset this
    layer's own hits show over their first `upto_s` (the velocity law of this drum: a softer stroke has a different spectrum, not just less level).
    Offsets are 5-bin smoothed and clipped to `lim`."""
    import copy; P = copy.copy(hard)
    tt = (hard.tc >= 0.0) & (hard.tc < upto_s)
    off = np.nanmedian(short.M[:, :, tt] - hard.M[:, :, tt], axis=2)             # (2,K)
    off = np.nan_to_num(off, nan=0.0)
    off = np.stack([np.convolve(o, np.ones(5) / 5, mode='same') for o in off]); off = np.clip(off, lim[0], lim[1])
    P.M = hard.M + off[:, :, None]; P.Ms = hard.Ms + off[:, :, None]; P.offset_db = off
    return P

def reconstruct(hit, prior, gap_s, gl_iters=4, seed=0, tol_extra_db=2.0, dbg=None):
    """hit (L,2) aligned, gain-normalised real hit (onset at prior.pre). Returns (y (L,2), info)."""
    L = len(hit); P = prior; tc = P.tc; rs = np.random.RandomState(seed)
    out = np.zeros((L, 2)); info = dict(replaced_frac=[], bleed_frac=[], hole_frac=[])
    k8 = int(np.argmax(tc >= 0.008)); k30 = int(np.argmax(tc >= 0.03))
    gf = np.where(tc >= gap_s - 0.015)[0]; gap_fr = int(gf[0]) if len(gf) else len(tc)   # (argmax on an all-False mask returns 0: a hit whose next snare lies beyond the segment used to be flagged bleed everywhere)
    for c in range(2):
        Z = stft(hit[:, c]); A = 20 * np.log10(np.abs(Z) + 1e-9); K, T = A.shape
        As = 10 * np.log10(uniform_filter(np.abs(Z) ** 2, size=(3, 3), mode='nearest') + 1e-18)
        M = P.M[c]; tol = P.sig[c] + tol_extra_db; ex = As - P.Ms[c]
        bleed = ex > tol; hole = ex < -np.maximum(tol + 1.0, 6.0)   # a dip deeper than the natural spread is the separator ducking this hit under a kick/hat (left in, the file's decay guard would lock the whole rest of the tail to that dip -> a cliff)
        bleed[:, :k8] = False; hole[:, :k30] = False
        if gap_fr < T: bleed[:, gap_fr:] = True   # the next snare's attack is not this hit: always rebuilt from the prior there
        # hysteresis: a hat or cymbal stroke is one connected time-frequency region whose excess over the ensemble falls off towards its edges.
        # The core test (ex > tol, up to 8 dB) catches its loud part only; the 3-8 dB wash around it was kept, and where the kept wash met the
        # fill (or the next hit's gap) the file stepped down by that much (measured: 6-13 dB walls at 120-230 ms in 5.0.2 packs). Every bin
        # adjacent in time or frequency to a flagged bin and more than half the natural spread above the ensemble is bleed as well, grown until
        # the region stops growing (bounded at 120 frames = 640 ms).
        grow_ok = ex > P.sig[c]; grow_ok[:, :k30] = False   # one natural spread; the body (< 30 ms) is never grown into
        if gap_fr < T: grow_ok[:, gap_fr:] = True
        along_t = np.ones((1, 3), bool)   # grown along time only: a stroke's wash precedes/follows its loud part in the same bins, while
        for _ in range(120):              # growing across frequency ran into the hit's own partials (which sit above the median too)
            nb = binary_dilation(bleed, structure=along_t) & grow_ok
            if nb.sum() == bleed.sum(): break
            bleed = nb
        info.setdefault('bleed_grown_frac', []).append(round(float((bleed[:, k8:gap_fr] & ~(ex[:, k8:gap_fr] > tol[:, k8:gap_fr])).mean()), 3))
        # per-band continuity: a snare's decay has no step. Frame by frame from 30 ms, each band's level (over its non-bleed bins) is expected to
        # follow the ensemble's own frame-to-frame change; a drop of > 5 dB under that expectation is the separator ducking this hit under a kick
        # or a hat stroke (the per-bin test alone cannot catch it: +-tol per bin lets an 8 dB step through), and the whole band is rebuilt there
        band_k = np.digitize(P.f, P.xo); nbnd = len(P.xo) + 1
        Pz = np.abs(Z) ** 2; Pm = 10 ** (M / 10); duck = np.zeros((nbnd, T), bool)
        for b in range(nbnd):
            kb = band_k == b
            if kb.sum() < 2: continue
            wb = (~bleed[kb]).astype(float)
            ab = 10 * np.log10((Pz[kb] * wb).sum(0) / np.maximum(wb.sum(0), 1) + 1e-18); mb = 10 * np.log10(Pm[kb].mean(0) + 1e-18)
            # reference level + the ensemble's slope since the reference frame -> expectation; the reference moves only while the band tracks
            # the expectation (within 2 dB) or sits above it, so a slow slide (3 dB a frame for three frames) is caught as well as a step
            lvl = ab[k30]; tref = k30
            for t in range(k30 + 1, min(T, gap_fr)):
                expct = lvl + (mb[t] - mb[tref])
                if ab[t] < expct - 5.0: duck[b, t] = True
                elif ab[t] >= expct - 2.0: lvl = ab[t]; tref = t
            hole[kb] |= duck[b][None, :]
        info.setdefault('duck_frac', []).append(round(float(duck[:, k30:].mean()), 3))
        rep = bleed | hole
        # this hit's own level relative to the ensemble, per band and frame, from its kept bins (a stroke that rings 5 dB above the median at 180 ms
        # continues 5 dB above where it is rebuilt from 190 ms: otherwise the switch into the fill is an audible step). Where a band has no kept
        # bins the last measured offset is held and relaxes towards the ensemble with a 150 ms time constant.
        kept = (~rep) & (np.arange(T)[None, :] >= k30) & (np.arange(T)[None, :] < gap_fr)
        off = np.zeros((K, T)); tolmax = float(tol.max())
        for b in range(len(P.xo) + 1):
            kb = band_k == b
            if not kb.any(): continue
            exb = np.where(kept[kb], ex[kb], np.nan)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore'); ob = np.nanmedian(exb, axis=0); nb_ = np.isfinite(exb).sum(0)
            held = 0.0; o2 = np.zeros(T); decay = np.exp(-HOP / SR / 0.15)
            for t in range(T):
                if t >= k30 and nb_[t] >= max(3, kb.sum() // 6) and np.isfinite(ob[t]): held = float(ob[t])
                elif t >= k30: held *= decay
                o2[t] = held if t >= k30 else 0.0
            o2 = np.convolve(o2, np.ones(3) / 3, mode='same'); off[kb] = np.clip(o2, -tolmax, tolmax)[None, :]
        info.setdefault('own_offset_db', []).append(round(float(np.median(off[:, k30:])), 1))
        Mo = M + off
        target = np.where(bleed, Mo, Mo - FILL_LOW_DB)
        target = np.where(np.arange(T)[None, :] >= np.minimum(P.real_to[c][:, None], T), Mo, target)  # in the estimate region fill exactly to the continued prior (at this hit's level)
        mag = np.where(rep, 10 ** (target / 20), np.abs(Z))
        # phase: keep the hit's own where the excess is modest; otherwise start from propagated (low) / random (high) and let GL settle it
        keep_phase = rep & (np.abs(ex) < 10.0)
        ph = np.angle(Z).copy()
        low = P.f < PROP_F
        rnd = rs.uniform(-np.pi, np.pi, size=ph.shape)
        new = rep & ~keep_phase
        ph = np.where(new & ~low[:, None], rnd, ph)
        # propagate low bins frame by frame where replaced
        omega = 2 * np.pi * np.arange(K) * HOP / NFFT
        for t in range(1, T):
            m = new[:, t] & low
            if m.any(): ph[m, t] = ph[m, t - 1] + omega[m]
        Zm = mag * np.exp(1j * ph)
        for it in range(gl_iters):   # consistency passes over the replaced bins only
            Y = stft(istft(Zm, L))
            Zm = np.where(rep, mag * np.exp(1j * np.angle(Y)), Z)
        # an inconsistent STFT loses level on resynthesis (random-phase regions come out 3-5 dB under their target): measure the shortfall per
        # bin over the replaced region (smoothed 5 bins x 3 frames), lift the target by it (<= 8 dB) and settle again
        mag2 = mag.copy()
        for rnd in range(2):
            Y = stft(istft(Zm, L)); Y = Y[:, :T] if Y.shape[1] >= T else np.pad(Y, ((0, 0), (0, T - Y.shape[1])))
            short = np.where(rep, 20 * np.log10((mag + 1e-9) / (np.abs(Y) + 1e-9)), 0.0)
            short = uniform_filter(short, size=(5, 3), mode='nearest'); short = np.clip(short, 0.0, 8.0)
            mag2 = np.where(rep, np.minimum(mag2 * 10 ** (short / 20), mag * 10 ** (8 / 20)), mag); Zm = np.where(rep, mag2 * np.exp(1j * np.angle(Zm)), Z)
            for it in range(2):
                Y = stft(istft(Zm, L))
                Zm = np.where(rep, mag2 * np.exp(1j * np.angle(Y)), Z)
        y = istft(Zm, L)
        # time-domain crossfade: raw hit until 8 ms, reconstruction from 18 ms
        a0 = P.pre + int(0.008 * SR); a1 = P.pre + int(0.018 * SR); w = np.zeros(L); w[a1:] = 1
        w[a0:a1] = 0.5 * (1 - np.cos(np.pi * np.arange(a1 - a0) / (a1 - a0)))
        out[:, c] = hit[:, c] * (1 - w) + y * w
        info['replaced_frac'].append(round(float(rep[:, k8:].mean()), 3)); info['bleed_frac'].append(round(float(bleed[:, k8:].mean()), 3)); info['hole_frac'].append(round(float(hole[:, k30:].mean()), 3))
        if dbg is not None: dbg.update(ex=ex, rep=rep, A=A, M=M)
    return out, info
