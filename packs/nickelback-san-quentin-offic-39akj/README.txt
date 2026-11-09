ZC SNARE EXTRACT v5.0 - Nickelback - "San Quentin" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 232 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.953,
    hit-to-hit level SD 3.43 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.5  vs full drum stem -8.1  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.0  vs drum stem -9.8
    Hit-locked energy left in the separator residual (snare that got dropped): -33.6 dBFS at 0-5 ms vs -10.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -33.5, '150-300': -0.5, '300-600': -1.5, '600-1200': -1.5, '1200-2500': -2.3, '2500-5000': -5.5, '5000-8000': -8.8, '8000-12000': -8.6, '12000-16000': -12.1}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak); a bin well below it after 30 ms is a hole
    the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    239 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.63, 1.79, 2.97, 2.86] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-103.0, -138.0, -96.0, -65.0, -111.0] dB/s  ->  T60 [0.58, 0.43, 0.63, 0.93, 0.54] s
  early part (60-150 ms, body + early reflections): [None, -62.0, -47.0, -54.0, -77.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.3, '30ms': -16.7, '50ms': -15.5, '100ms': -11.2, '150ms': -12.9, '200ms': -20.3, '300ms': -26.4}
  Snare-stem noise floor between hits: -85.6 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.50 from the record's medium hits (28).
 ZC_nickelback-san-quentin-offic-39akj_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=77.72 s, gap 582 ms, bg -39.9 dB, real to 109 ms, len 1049 ms, rel 0.3 dB REAL
  hard rr2: t=169.66 s, gap 720 ms, bg -42.7 dB, real to 139 ms, len 1014 ms, rel -0.0 dB REAL
  hard rr3: t=170.62 s, gap 573 ms, bg -41.1 dB, real to 109 ms, len 994 ms, rel 1.3 dB REAL
  hard rr4: t=226.75 s, gap 552 ms, bg -42.0 dB, real to 294 ms, len 1019 ms, rel 0.4 dB REAL
  medium rr1: t=18.44 s, gap 305 ms, bg -18.5 dB, real to 124 ms, len 1008 ms, rel -3.9 dB REAL
  medium rr2: t=18.92 s, gap 240 ms, bg -31.1 dB, real to 234 ms, len 1038 ms, rel -5.1 dB REAL
  medium rr3: t=23.04 s, gap 532 ms, bg -23.8 dB, real to 239 ms, len 989 ms, rel -5.2 dB REAL
  medium rr4: t=15.04 s, gap 241 ms, bg -38.3 dB, real to 234 ms, len 980 ms, rel -8.7 dB REAL
  soft rr1: t=43.85 s, gap 536 ms, bg -42.4 dB, real to 84 ms, len 920 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  soft rr2: t=208.85 s, gap 461 ms, bg -36.4 dB, real to 144 ms, len 1024 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  soft rr3: t=91.51 s, gap 376 ms, bg -41.9 dB, real to 109 ms, len 1023 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  soft rr4: t=157.08 s, gap 474 ms, bg -44.4 dB, real to 244 ms, len 1057 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  ghost rr1: t=34.17 s, gap 480 ms, bg -40.9 dB, real to 139 ms, len 1051 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  ghost rr2: t=129.5 s, gap 379 ms, bg -37.7 dB, real to 414 ms, len 1025 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  ghost rr3: t=228.21 s, gap 242 ms, bg -40.3 dB, real to 239 ms, len 949 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  ghost rr4: t=168.21 s, gap 478 ms, bg -39.7 dB, real to 114 ms, len 989 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))