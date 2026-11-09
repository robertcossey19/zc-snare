ZC SNARE EXTRACT v5.0 - Asking Alexandria - "Breathless" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 305 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.91,
    hit-to-hit level SD 1.8 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -8.9  vs full drum stem -8.4  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -12.6  vs drum stem -9.9
    Hit-locked energy left in the separator residual (snare that got dropped): -43.8 dBFS at 0-5 ms vs -9.0 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -28.4, '150-300': -0.1, '300-600': -0.6, '600-1200': -1.1, '1200-2500': -1.8, '2500-5000': -3.5, '5000-8000': -3.6, '8000-12000': -5.4, '12000-16000': -7.5}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    320 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [9.34, 2.61, 1.52, 2.11] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-137.0, -135.0, -140.0, -160.0, -119.0] dB/s  ->  T60 [0.44, 0.44, 0.43, 0.37, 0.51] s
  early part (60-150 ms, body + early reflections): [None, -130.0, -94.0, -102.0, -119.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.7, '30ms': -16.0, '50ms': -13.7, '100ms': -20.0, '150ms': -27.2, '200ms': -32.1}
  Snare-stem noise floor between hits: -85.3 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 2/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 22 medium hits; scaled x2.50 from the record's medium hits (22).
 ZC_asking-alexandria-breathless-d53a2_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=201.39 s, gap 742 ms, bg -40.9 dB, real to 204 ms, len 462 ms, rel -0.5 dB REAL
  hard rr2: t=108.02 s, gap 741 ms, bg -43.4 dB, real to 379 ms, len 501 ms, rel -0.8 dB REAL
  hard rr3: t=177.39 s, gap 1492 ms, bg -42.9 dB, real to 84 ms, len 475 ms, rel 1.3 dB REAL
  hard rr4: t=60.13 s, gap 743 ms, bg -45.8 dB, real to 189 ms, len 440 ms, rel -0.9 dB REAL
  medium rr1: t=160.34 s, gap 154 ms, bg -39.2 dB, real to 144 ms, len 468 ms, rel -3.1 dB REAL
  medium rr2: t=229.89 s, gap 161 ms, bg -41.8 dB, real to 114 ms, len 421 ms, rel -3.8 dB REAL
  medium rr3: t=234.96 s, gap 9000 ms, bg -26.8 dB, real to 79 ms, len 460 ms, rel -3.7 dB ESTIMATE (measured on 22 medium hits)
  medium rr4: t=58.63 s, gap 553 ms, bg -43.6 dB, real to 189 ms, len 451 ms, rel -3.7 dB ESTIMATE (measured on 22 medium hits)
  soft rr1: t=202.9 s, gap 557 ms, bg -39.5 dB, real to 389 ms, len 487 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  soft rr2: t=162.21 s, gap 366 ms, bg -38.1 dB, real to 239 ms, len 455 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  soft rr3: t=225.39 s, gap 415 ms, bg -46.8 dB, real to 264 ms, len 500 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  soft rr4: t=103.59 s, gap 1420 ms, bg -21.0 dB, real to 99 ms, len 475 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  ghost rr1: t=195.39 s, gap 1190 ms, bg -44.3 dB, real to 189 ms, len 502 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  ghost rr2: t=65.0 s, gap 934 ms, bg -45.8 dB, real to 374 ms, len 456 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  ghost rr3: t=122.27 s, gap 921 ms, bg -28.5 dB, real to 124 ms, len 440 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))
  ghost rr4: t=72.88 s, gap 380 ms, bg -42.1 dB, real to 379 ms, len 470 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (22))