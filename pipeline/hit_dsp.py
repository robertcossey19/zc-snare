"""Band-split and lighter-stroke transform helpers used by build_pack.py for ESTIMATE velocity layers."""
import numpy as np, scipy.signal as sg, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import extract, frac_shift, SR, PRE, LEN
FR = int(0.005 * SR)
XO = [150, 600, 2000, 6000]          # band crossovers (Hz)
NB = len(XO) + 1
rng = np.random.RandomState(7)

def band_weights(n):
    f = np.fft.rfftfreq(n, 1 / SR); W = np.zeros((NB, len(f)))
    def lowpass(fc):  # raised cosine over +-1/3 oct
        lo, hi = fc / 2 ** (1 / 3), fc * 2 ** (1 / 3); w = np.ones_like(f)
        m = (f > lo) & (f < hi); w[m] = 0.5 * (1 + np.cos(np.pi * (np.log2(f[m] / lo) / np.log2(hi / lo)))); w[f >= hi] = 0; return w
    prev = np.zeros_like(f)
    for b, fc in enumerate(XO):
        lp = lowpass(fc); W[b] = lp - prev; prev = lp
    W[NB - 1] = 1 - prev; return W

def bandsplit(x):  # x (n,2) -> (NB,n,2); zero padded so the split is not circular
    n0 = len(x); x = np.vstack([x, np.zeros((4096, x.shape[1]))]); n = len(x); W = band_weights(n); X = np.fft.rfft(x, axis=0); out = np.empty((NB, n0, 2))
    for b in range(NB): out[b] = np.fft.irfft(X * W[b][:, None], n, axis=0)[:n0]
    return out

def env_db(y):  # y mono -> dB per FR frame (3-frame smoothed)
    n = len(y) // FR; E = (y[:n * FR].reshape(n, FR) ** 2).mean(1); E = np.convolve(E, np.ones(3) / 3, mode='same'); return 10 * np.log10(E + 1e-13)

def gate_time(Eb, rise=7.0, floor=-55.0):  # first onset after the hit, seconds after onset; from band envelope dB
    f0 = PRE // FR; start = f0 + 4; best = None
    for i in range(start, len(Eb)):
        if Eb[i] > floor and Eb[i] - Eb[max(i - 8, f0 + 2):i].min() > rise: best = (i * FR - PRE) / SR; break
    return best if best is not None else (len(Eb) * FR - PRE) / SR

def fade_mask(n, t_end, fade=0.006, lead=0.008):
    m = np.ones(n); k = int((t_end - lead) * SR) + PRE; w = int(fade * SR)
    if k < 0: return np.zeros(n)
    k0 = max(k - w, 0); r = np.arange(k0, min(k, n)); m[k0:min(k, n)] = 0.5 * (1 + np.cos(np.pi * (r - k0) / max(w, 1))); m[min(k, n):] = 0; return m

def shelf(x, f0, gdb):  # RBJ high shelf, applied zero-phase (filtfilt) with gain split
    A = 10 ** (gdb / 40); w0 = 2 * np.pi * f0 / SR; S = 1.0; al = np.sin(w0) / 2 * np.sqrt((A + 1 / A) * (1 / S - 1) + 2); c = np.cos(w0)
    b0 = A * ((A + 1) + (A - 1) * c + 2 * np.sqrt(A) * al); b1 = -2 * A * ((A - 1) + (A + 1) * c); b2 = A * ((A + 1) + (A - 1) * c - 2 * np.sqrt(A) * al)
    a0 = (A + 1) - (A - 1) * c + 2 * np.sqrt(A) * al; a1 = 2 * ((A - 1) - (A + 1) * c); a2 = (A + 1) - (A - 1) * c - 2 * np.sqrt(A) * al
    return sg.lfilter([b0 / a0, b1 / a0, b2 / a0], [1, a1 / a0, a2 / a0], x, axis=0)

PAD = 8192   # FFT filtering is circular: without zero padding the attack wraps round into the last samples of the file (an audible click at the end of every estimate layer up to 4.3.1)

def wires(x, factor, t_ref=0.08):  # shorten the 1.5-10 kHz (snare-wire) decay after 12 ms
    n0 = len(x); x = np.vstack([x, np.zeros((PAD, x.shape[1]))]); n = len(x); f = np.fft.rfftfreq(n, 1 / SR); W = np.zeros_like(f); m = (f > 1500) & (f < 10000); W[m] = 1
    e = (f > 1000) & (f <= 1500); W[e] = 0.5 * (1 - np.cos(np.pi * (f[e] - 1000) / 500)); e = (f >= 10000) & (f < 14000); W[e] = 0.5 * (1 + np.cos(np.pi * (f[e] - 10000) / 4000))
    hf = np.fft.irfft(np.fft.rfft(x, axis=0) * W[:, None], n, axis=0); t = np.arange(n) / SR - 0.012
    g = np.where(t > 0, np.exp(-np.maximum(t, 0) * (1 / factor - 1) / t_ref), 1.0); return (x - hf + hf * g[:, None])[:n0]

def glide(x, s, a=0.20, tau=0.012):  # reduce the early pitch glide of the <600 Hz band (lighter hit = less membrane tension modulation)
    n0 = len(x); x = np.vstack([x, np.zeros((PAD, x.shape[1]))]); n = len(x); f = np.fft.rfftfreq(n, 1 / SR); W = np.ones_like(f); e = (f > 450) & (f < 800); W[e] = 0.5 * (1 + np.cos(np.pi * (f[e] - 450) / 350)); W[f >= 800] = 0
    lo = np.fft.irfft(np.fft.rfft(x, axis=0) * W[:, None], n, axis=0); t = np.arange(n) / SR
    r = (1 + a * s * np.exp(-t / tau)) / (1 + a * np.exp(-t / tau)); pos = np.cumsum(r) - r[0]
    out = np.empty_like(lo); idx = np.arange(n)
    for ch in range(2): out[:, ch] = np.interp(pos, idx, lo[:, ch])
    return (x - lo + out)[:n0]

def attack(x, fct):
    t = np.arange(len(x)) / SR; w = np.where(t < 0.0025, 1.0, np.where(t < 0.005, 0.5 * (1 + np.cos(np.pi * (t - 0.0025) / 0.0025)), 0.0)); return x * (1 - (1 - fct) * w)[:, None]
