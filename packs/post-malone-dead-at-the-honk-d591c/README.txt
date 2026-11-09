ZC SNARE EXTRACT v5.0 - Post Malone - "Dead at the Honky Tonk" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 127 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.731,
    hit-to-hit level SD 15.09 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -12.4  vs full drum stem -11.4  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.8  vs drum stem -8.0
    Hit-locked energy left in the separator residual (snare that got dropped): -46.9 dBFS at 0-5 ms vs -19.5 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -25.1, '150-300': -2.8, '300-600': -4.0, '600-1200': -3.7, '1200-2500': -3.5, '2500-5000': -2.0, '5000-8000': -1.5, '8000-12000': -1.5, '12000-16000': -2.5}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    53 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.1, 5.17, 4.69, 2.59] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-157.0, -157.0, -157.0, -107.0, -196.0] dB/s  ->  T60 [0.38, 0.38, 0.38, 0.56, 0.31] s
  early part (60-150 ms, body + early reflections): [None, -157.0, None, -107.0, -196.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.4, '30ms': -4.3, '50ms': -7.4, '100ms': -14.7, '150ms': -20.7}
  Snare-stem noise floor between hits: -91.1 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 1/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 10 ghost hits; scaled x2.50 from the record's medium hits (26).
 ZC_post-malone-dead-at-the-honk-d591c_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=126.75 s, gap 1438 ms, bg -35.8 dB, real to 99 ms, len 540 ms, rel -1.4 dB REAL
  hard rr2: t=116.63 s, gap 617 ms, bg -35.0 dB, real to 94 ms, len 514 ms, rel -1.2 dB REAL
  hard rr3: t=168.68 s, gap 585 ms, bg -33.2 dB, real to 219 ms, len 526 ms, rel 0.3 dB REAL
  hard rr4: t=67.11 s, gap 150 ms, bg -42.2 dB, real to 99 ms, len 525 ms, rel 3.0 dB REAL
  medium rr1: t=82.29 s, gap 222 ms, bg -29.3 dB, real to 79 ms, len 526 ms, rel -6.2 dB REAL
  medium rr2: t=88.08 s, gap 335 ms, bg -45.9 dB, real to 69 ms, len 538 ms, rel -3.6 dB REAL
  medium rr3: t=55.05 s, gap 127 ms, bg -38.2 dB, real to 194 ms, len 514 ms, rel -7.3 dB REAL
  medium rr4: t=115.19 s, gap 228 ms, bg -24.3 dB, real to 59 ms, len 531 ms, rel -4.9 dB REAL
  soft rr1: t=68.06 s, gap 493 ms, bg -42.6 dB, real to 224 ms, len 564 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  soft rr2: t=103.62 s, gap 581 ms, bg -32.2 dB, real to 94 ms, len 540 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  soft rr3: t=90.97 s, gap 335 ms, bg -45.0 dB, real to 219 ms, len 531 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  soft rr4: t=67.47 s, gap 583 ms, bg -33.3 dB, real to 169 ms, len 531 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  ghost rr1: t=16.15 s, gap 197 ms, bg -17.0 dB, real to 69 ms, len 532 ms, rel -26.3 dB REAL
  ghost rr2: t=77.59 s, gap 1316 ms, bg -36.0 dB, real to 124 ms, len 535 ms, rel -25.0 dB ESTIMATE (measured on 10 ghost hits)
  ghost rr3: t=86.27 s, gap 1803 ms, bg -32.4 dB, real to 109 ms, len 519 ms, rel -25.0 dB ESTIMATE (measured on 10 ghost hits)
  ghost rr4: t=148.44 s, gap 520 ms, bg -37.0 dB, real to 74 ms, len 537 ms, rel -25.0 dB ESTIMATE (measured on 10 ghost hits)