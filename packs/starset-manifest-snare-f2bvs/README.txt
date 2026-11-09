ZC SNARE EXTRACT v5.0 - STARSET - "MANIFEST snare" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 165 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.911,
    hit-to-hit level SD 4.84 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.7  vs full drum stem -9.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -10.5  vs drum stem -10.3
    Hit-locked energy left in the separator residual (snare that got dropped): -49.8 dBFS at 0-5 ms vs -11.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -18.3, '150-300': 0.0, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.3, '2500-5000': -0.7, '5000-8000': -1.6, '8000-12000': -3.1, '12000-16000': -7.1}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    198 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.18, 1.52, 3.85, 5.33] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-115.0, -80.0, -127.0, -103.0, -140.0] dB/s  ->  T60 [0.52, 0.75, 0.47, 0.58, 0.43] s
  early part (60-150 ms, body + early reflections): [None, -117.0, -124.0, -135.0, -140.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -0.7, '30ms': -11.8, '50ms': -14.1, '100ms': -22.8, '150ms': -28.6, '200ms': -30.8}
  Snare-stem noise floor between hits: -98.3 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.47 from the record's medium hits (22); scaled x2.50 from the record's medium hits (22).
 ZC_starset-manifest-snare-f2bvs_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=30.97 s, gap 1614 ms, bg -43.4 dB, real to 259 ms, len 584 ms, rel 1.4 dB REAL
  hard rr2: t=238.54 s, gap 1614 ms, bg -41.9 dB, real to 409 ms, len 590 ms, rel 0.9 dB REAL
  hard rr3: t=79.62 s, gap 1614 ms, bg -39.2 dB, real to 399 ms, len 626 ms, rel 0.6 dB REAL
  hard rr4: t=108.81 s, gap 601 ms, bg -40.5 dB, real to 169 ms, len 594 ms, rel 1.8 dB REAL
  medium rr1: t=110.23 s, gap 194 ms, bg -22.9 dB, real to 149 ms, len 609 ms, rel -4.3 dB REAL
  medium rr2: t=218.37 s, gap 369 ms, bg -48.1 dB, real to 124 ms, len 559 ms, rel -3.9 dB REAL
  medium rr3: t=126.06 s, gap 194 ms, bg -44.7 dB, real to 89 ms, len 560 ms, rel -8.8 dB REAL
  medium rr4: t=209.96 s, gap 306 ms, bg -27.0 dB, real to 194 ms, len 603 ms, rel -4.0 dB REAL
  soft rr1: t=133.14 s, gap 1614 ms, bg -42.9 dB, real to 284 ms, len 549 ms, rel -14.0 dB ESTIMATE (scaled x2.47 from the record's medium hits (22))
  soft rr2: t=153.41 s, gap 2212 ms, bg -38.8 dB, real to 354 ms, len 590 ms, rel -14.0 dB ESTIMATE (scaled x2.47 from the record's medium hits (22))
  soft rr3: t=126.65 s, gap 453 ms, bg -44.3 dB, real to 79 ms, len 574 ms, rel -14.0 dB ESTIMATE (scaled x2.47 from the record's medium hits (22))
  soft rr4: t=125.03 s, gap 1020 ms, bg -41.7 dB, real to 144 ms, len 554 ms, rel -14.0 dB ESTIMATE (scaled x2.47 from the record's medium hits (22))
  ghost rr1: t=162.33 s, gap 1611 ms, bg -41.3 dB, real to 438 ms, len 604 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  ghost rr2: t=261.65 s, gap 601 ms, bg -37.8 dB, real to 179 ms, len 574 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  ghost rr3: t=139.62 s, gap 401 ms, bg -43.8 dB, real to 498 ms, len 569 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  ghost rr4: t=92.6 s, gap 400 ms, bg -41.7 dB, real to 214 ms, len 535 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))