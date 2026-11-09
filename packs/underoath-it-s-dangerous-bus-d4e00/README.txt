ZC SNARE EXTRACT v5.0 - Underoath - "It's Dangerous Business Walking Out Your Front Door" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 130 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.872,
    hit-to-hit level SD 1.58 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -16.5  vs full drum stem -16.4  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -23.2  vs drum stem -22.8
    Hit-locked energy left in the separator residual (snare that got dropped): -62.5 dBFS at 0-5 ms vs -17.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -16.1, '150-300': -0.2, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.4, '2500-5000': -1.7, '5000-8000': -2.4, '8000-12000': -6.1, '12000-16000': -12.6}
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
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [1.29, 2.79, 2.88, 1.09] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-128.0, -132.0, -83.0, -123.0, -141.0] dB/s  ->  T60 [0.47, 0.45, 0.72, 0.49, 0.43] s
  early part (60-150 ms, body + early reflections): [None, -96.0, -83.0, -123.0, -141.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -6.5, '30ms': -14.1, '50ms': -15.2, '100ms': -19.8, '150ms': -24.6, '200ms': -26.4}
  Snare-stem noise floor between hits: -93.5 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.50 from the record's medium hits (19).
 ZC_underoath-it-s-dangerous-bus-d4e00_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=86.55 s, gap 659 ms, bg -39.3 dB, real to 219 ms, len 475 ms, rel -0.3 dB REAL
  hard rr2: t=16.33 s, gap 1007 ms, bg -44.3 dB, real to 244 ms, len 510 ms, rel 1.2 dB REAL
  hard rr3: t=17.68 s, gap 738 ms, bg -33.5 dB, real to 299 ms, len 500 ms, rel 0.1 dB REAL
  hard rr4: t=199.03 s, gap 1512 ms, bg -35.3 dB, real to 189 ms, len 445 ms, rel -1.7 dB REAL
  medium rr1: t=140.6 s, gap 217 ms, bg -20.7 dB, real to 59 ms, len 484 ms, rel -3.3 dB REAL
  medium rr2: t=104.77 s, gap 1342 ms, bg -20.4 dB, real to 294 ms, len 530 ms, rel -7.7 dB REAL
  medium rr3: t=94.8 s, gap 231 ms, bg -30.1 dB, real to 214 ms, len 503 ms, rel -3.1 dB REAL
  medium rr4: t=106.12 s, gap 877 ms, bg -30.2 dB, real to 249 ms, len 450 ms, rel -3.1 dB REAL
  soft rr1: t=109.68 s, gap 889 ms, bg -44.7 dB, real to 438 ms, len 420 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  soft rr2: t=195.46 s, gap 1140 ms, bg -30.7 dB, real to 304 ms, len 390 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  soft rr3: t=117.68 s, gap 650 ms, bg -38.4 dB, real to 324 ms, len 495 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  soft rr4: t=131.9 s, gap 880 ms, bg -34.6 dB, real to 339 ms, len 495 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  ghost rr1: t=207.02 s, gap 1840 ms, bg -40.9 dB, real to 329 ms, len 504 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  ghost rr2: t=125.67 s, gap 886 ms, bg -37.2 dB, real to 294 ms, len 490 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  ghost rr3: t=90.12 s, gap 679 ms, bg -33.8 dB, real to 154 ms, len 515 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  ghost rr4: t=114.12 s, gap 505 ms, bg -43.5 dB, real to 334 ms, len 500 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))