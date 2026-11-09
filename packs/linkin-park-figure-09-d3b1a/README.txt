ZC SNARE EXTRACT v5.0 - Linkin Park - "Figure.09" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 133 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.776,
    hit-to-hit level SD 4.29 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -7.9  vs full drum stem -7.8  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.6  vs drum stem -15.3
    Hit-locked energy left in the separator residual (snare that got dropped): -57.2 dBFS at 0-5 ms vs -8.6 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -3.8, '150-300': -0.1, '300-600': -0.1, '600-1200': 0.0, '1200-2500': -0.1, '2500-5000': -0.8, '5000-8000': -2.5, '8000-12000': -6.6, '12000-16000': -11.5}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak); a bin well below it after 30 ms is a hole
    the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    343 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.08, 1.22, 1.5, 1.43] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-135.0, -104.0, -88.0, -167.0, -188.0] dB/s  ->  T60 [0.44, 0.58, 0.68, 0.36, 0.32] s
  early part (60-150 ms, body + early reflections): [None, -104.0, -105.0, -167.0, -188.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -7.0, '30ms': -13.1, '50ms': -16.8, '100ms': -22.6, '150ms': -25.7, '200ms': -30.9}
  Snare-stem noise floor between hits: -95.8 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 2/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.18 from the record's medium hits (23); scaled x2.50 from the record's medium hits (23).
 ZC_linkin-park-figure-09-d3b1a_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=42.32 s, gap 1217 ms, bg -39.0 dB, real to 169 ms, len 520 ms, rel -1.1 dB REAL
  hard rr2: t=37.42 s, gap 1215 ms, bg -39.1 dB, real to 159 ms, len 490 ms, rel 0.4 dB REAL
  hard rr3: t=36.2 s, gap 1216 ms, bg -36.8 dB, real to 164 ms, len 505 ms, rel 0.1 dB REAL
  hard rr4: t=41.1 s, gap 1216 ms, bg -35.8 dB, real to 119 ms, len 500 ms, rel -0.3 dB REAL
  medium rr1: t=123.11 s, gap 594 ms, bg -39.7 dB, real to 59 ms, len 477 ms, rel -9.4 dB REAL
  medium rr2: t=121.89 s, gap 282 ms, bg -38.8 dB, real to 59 ms, len 432 ms, rel -8.0 dB REAL
  medium rr3: t=63.13 s, gap 595 ms, bg -43.7 dB, real to 174 ms, len 450 ms, rel -3.9 dB REAL
  medium rr4: t=23.96 s, gap 145 ms, bg -27.9 dB, real to 134 ms, len 445 ms, rel -4.4 dB REAL
  soft rr1: t=94.96 s, gap 454 ms, bg -35.2 dB, real to 59 ms, len 501 ms, rel -12.2 dB REAL
  soft rr2: t=58.23 s, gap 240 ms, bg -41.5 dB, real to 319 ms, len 439 ms, rel -11.8 dB REAL
  soft rr3: t=90.06 s, gap 1215 ms, bg -34.1 dB, real to 164 ms, len 494 ms, rel -14.0 dB ESTIMATE (scaled x2.18 from the record's medium hits (23))
  soft rr4: t=77.82 s, gap 1219 ms, bg -40.1 dB, real to 384 ms, len 476 ms, rel -14.0 dB ESTIMATE (scaled x2.18 from the record's medium hits (23))
  ghost rr1: t=30.08 s, gap 1216 ms, bg -35.5 dB, real to 94 ms, len 480 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (23))
  ghost rr2: t=26.41 s, gap 1215 ms, bg -32.4 dB, real to 134 ms, len 480 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (23))
  ghost rr3: t=39.87 s, gap 1215 ms, bg -35.2 dB, real to 144 ms, len 519 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (23))
  ghost rr4: t=115.77 s, gap 1217 ms, bg -37.5 dB, real to 194 ms, len 480 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (23))