ZC SNARE EXTRACT v5.0 - Nickelback - "San Quentin" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 204 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.949,
    hit-to-hit level SD 3.23 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.6  vs full drum stem -8.2  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.1  vs drum stem -9.9
    Hit-locked energy left in the separator residual (snare that got dropped): -28.7 dBFS at 0-5 ms vs -10.2 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -33.3, '150-300': -0.4, '300-600': -1.3, '600-1200': -1.6, '1200-2500': -2.3, '2500-5000': -5.3, '5000-8000': -8.5, '8000-12000': -8.3, '12000-16000': -11.8}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    239 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.97, 1.68, 2.7, 2.93] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-93.0, -110.0, -97.0, -60.0, -88.0] dB/s  ->  T60 [0.65, 0.55, 0.62, 1.0, 0.68] s
  early part (60-150 ms, body + early reflections): [None, -66.0, -43.0, -57.0, -71.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.4, '30ms': -16.3, '50ms': -15.3, '100ms': -10.9, '150ms': -13.1, '200ms': -19.7, '300ms': -29.0}
  Snare-stem noise floor between hits: -85.4 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.50 from the record's medium hits (25).
 ZC_nickelback-san-quentin-offic-39akj_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=164.82 s, gap 961 ms, bg -39.8 dB, real to 89 ms, len 940 ms, rel 0.2 dB REAL
  hard rr2: t=167.72 s, gap 475 ms, bg -41.6 dB, real to 89 ms, len 1023 ms, rel 0.7 dB REAL
  hard rr3: t=225.79 s, gap 961 ms, bg -42.8 dB, real to 84 ms, len 1014 ms, rel -0.6 dB REAL
  hard rr4: t=170.62 s, gap 581 ms, bg -42.5 dB, real to 89 ms, len 989 ms, rel 1.3 dB REAL
  medium rr1: t=22.32 s, gap 477 ms, bg -19.8 dB, real to 299 ms, len 958 ms, rel -3.5 dB REAL
  medium rr2: t=26.92 s, gap 313 ms, bg -20.2 dB, real to 109 ms, len 914 ms, rel -3.0 dB REAL
  medium rr3: t=13.59 s, gap 240 ms, bg -27.9 dB, real to 234 ms, len 1049 ms, rel -5.2 dB REAL
  medium rr4: t=25.46 s, gap 123 ms, bg -19.6 dB, real to 144 ms, len 1013 ms, rel -4.2 dB REAL
  soft rr1: t=77.72 s, gap 583 ms, bg -40.2 dB, real to 109 ms, len 1029 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))
  soft rr2: t=91.51 s, gap 396 ms, bg -41.4 dB, real to 89 ms, len 1023 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))
  soft rr3: t=208.85 s, gap 461 ms, bg -35.6 dB, real to 144 ms, len 1024 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))
  soft rr4: t=157.08 s, gap 471 ms, bg -41.7 dB, real to 89 ms, len 988 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))
  ghost rr1: t=34.17 s, gap 480 ms, bg -42.0 dB, real to 94 ms, len 1026 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))
  ghost rr2: t=130.22 s, gap 354 ms, bg -40.9 dB, real to 99 ms, len 1049 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))
  ghost rr3: t=129.01 s, gap 476 ms, bg -43.2 dB, real to 89 ms, len 1003 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))
  ghost rr4: t=129.5 s, gap 384 ms, bg -37.7 dB, real to 144 ms, len 1025 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (25))