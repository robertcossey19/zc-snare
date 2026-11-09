ZC SNARE EXTRACT v5.0 - Metallica - "Fuel" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 295 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.684,
    hit-to-hit level SD 3.1 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -11.9  vs full drum stem -11.2  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.4  vs drum stem -13.2
    Hit-locked energy left in the separator residual (snare that got dropped): -55.2 dBFS at 0-5 ms vs -16.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -16.6, '150-300': -0.1, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.3, '2500-5000': -1.1, '5000-8000': -2.5, '8000-12000': -4.8, '12000-16000': -7.6}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    442 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [5.74, 3.15, 6.3, 5.6] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-91.0, -92.0, -90.0, -69.0, -108.0] dB/s  ->  T60 [0.66, 0.65, 0.66, 0.87, 0.56] s
  early part (60-150 ms, body + early reflections): [None, -106.0, -110.0, -136.0, -151.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.6, '30ms': -7.0, '50ms': -9.6, '100ms': -16.8, '150ms': -21.9, '200ms': -24.4}
  Snare-stem noise floor between hits: -79.0 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.50 from the record's medium hits (80).
 ZC_metallica-fuel-d55fc_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=263.35 s, gap 555 ms, bg -39.0 dB, real to 289 ms, len 605 ms, rel 1.8 dB REAL
  hard rr2: t=90.08 s, gap 1117 ms, bg -33.3 dB, real to 134 ms, len 620 ms, rel 0.6 dB REAL
  hard rr3: t=88.95 s, gap 1124 ms, bg -33.4 dB, real to 234 ms, len 630 ms, rel 1.0 dB REAL
  hard rr4: t=155.29 s, gap 1120 ms, bg -41.3 dB, real to 144 ms, len 610 ms, rel 1.7 dB REAL
  medium rr1: t=71.25 s, gap 143 ms, bg -28.4 dB, real to 129 ms, len 614 ms, rel -3.2 dB REAL
  medium rr2: t=250.33 s, gap 134 ms, bg -25.1 dB, real to 119 ms, len 644 ms, rel -3.2 dB REAL
  medium rr3: t=249.22 s, gap 139 ms, bg -25.7 dB, real to 79 ms, len 606 ms, rel -4.1 dB REAL
  medium rr4: t=241.0 s, gap 137 ms, bg -42.9 dB, real to 99 ms, len 623 ms, rel -4.4 dB REAL
  soft rr1: t=84.77 s, gap 558 ms, bg -42.1 dB, real to 349 ms, len 639 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))
  soft rr2: t=114.06 s, gap 563 ms, bg -34.9 dB, real to 249 ms, len 600 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))
  soft rr3: t=85.89 s, gap 550 ms, bg -37.3 dB, real to 304 ms, len 630 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))
  soft rr4: t=112.66 s, gap 853 ms, bg -34.4 dB, real to 488 ms, len 646 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))
  ghost rr1: t=120.59 s, gap 1123 ms, bg -31.3 dB, real to 329 ms, len 660 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))
  ghost rr2: t=104.81 s, gap 1126 ms, bg -30.9 dB, real to 94 ms, len 655 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))
  ghost rr3: t=129.51 s, gap 1093 ms, bg -43.2 dB, real to 114 ms, len 649 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))
  ghost rr4: t=101.41 s, gap 554 ms, bg -34.2 dB, real to 139 ms, len 655 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (80))