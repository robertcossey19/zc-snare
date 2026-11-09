ZC SNARE EXTRACT v5.0 - Deftones - "Change (In the House of Flies)" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 143 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.696,
    hit-to-hit level SD 2.39 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.5  vs full drum stem -10.0  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -17.6  vs drum stem -16.2
    Hit-locked energy left in the separator residual (snare that got dropped): -55.8 dBFS at 0-5 ms vs -13.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -12.5, '150-300': -0.1, '300-600': -0.3, '600-1200': -0.1, '1200-2500': -0.6, '2500-5000': -4.0, '5000-8000': -5.9, '8000-12000': -11.0, '12000-16000': -18.5}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    262 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.33, 4.17, 1.86, 4.22] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-124.0, -124.0, -124.0, -124.0, -124.0] dB/s  ->  T60 [0.49, 0.49, 0.49, 0.49, 0.49] s
  early part (60-150 ms, body + early reflections): [None, None, -124.0, None, None] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -5.7, '30ms': -14.6, '50ms': -20.1, '100ms': -26.1}
  Snare-stem noise floor between hits: -98.4 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.50 from the record's medium hits (26).
 ZC_deftones-change-in-the-house-d4460_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=92.09 s, gap 866 ms, bg -35.6 dB, real to 114 ms, len 342 ms, rel 0.7 dB REAL
  hard rr2: t=81.6 s, gap 1328 ms, bg -36.3 dB, real to 59 ms, len 362 ms, rel 0.8 dB REAL
  hard rr3: t=84.44 s, gap 642 ms, bg -35.3 dB, real to 59 ms, len 338 ms, rel 0.7 dB REAL
  hard rr4: t=58.93 s, gap 1075 ms, bg -35.9 dB, real to 59 ms, len 397 ms, rel -0.7 dB REAL
  medium rr1: t=227.45 s, gap 524 ms, bg -21.9 dB, real to 99 ms, len 370 ms, rel -4.9 dB REAL
  medium rr2: t=211.81 s, gap 978 ms, bg -19.8 dB, real to 79 ms, len 377 ms, rel -7.3 dB REAL
  medium rr3: t=103.39 s, gap 976 ms, bg -21.5 dB, real to 59 ms, len 372 ms, rel -3.7 dB REAL
  medium rr4: t=56.66 s, gap 526 ms, bg -14.9 dB, real to 294 ms, len 393 ms, rel -3.2 dB REAL
  soft rr1: t=97.34 s, gap 1750 ms, bg -35.6 dB, real to 159 ms, len 368 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  soft rr2: t=105.47 s, gap 627 ms, bg -33.1 dB, real to 64 ms, len 407 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  soft rr3: t=78.1 s, gap 858 ms, bg -31.4 dB, real to 149 ms, len 359 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  soft rr4: t=199.2 s, gap 614 ms, bg -37.1 dB, real to 59 ms, len 392 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  ghost rr1: t=93.83 s, gap 1736 ms, bg -27.4 dB, real to 59 ms, len 342 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  ghost rr2: t=194.32 s, gap 630 ms, bg -35.0 dB, real to 229 ms, len 386 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  ghost rr3: t=209.4 s, gap 1686 ms, bg -37.6 dB, real to 249 ms, len 387 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))
  ghost rr4: t=216.2 s, gap 1694 ms, bg -36.4 dB, real to 229 ms, len 386 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (26))