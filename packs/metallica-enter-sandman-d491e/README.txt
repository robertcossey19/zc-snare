ZC SNARE EXTRACT v5.0 - Metallica - "Enter Sandman" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 169 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.594,
    hit-to-hit level SD 4.54 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.8  vs full drum stem -9.9  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.7  vs drum stem -14.4
    Hit-locked energy left in the separator residual (snare that got dropped): -45.5 dBFS at 0-5 ms vs -15.0 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -8.6, '150-300': -0.1, '300-600': -0.3, '600-1200': -0.4, '1200-2500': -0.6, '2500-5000': -2.6, '5000-8000': -3.9, '8000-12000': -6.6, '12000-16000': -10.6}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    366 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.13, 4.65, 2.54, 3.58] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-92.0, -90.0, -110.0, -102.0, -124.0] dB/s  ->  T60 [0.65, 0.67, 0.55, 0.59, 0.48] s
  early part (60-150 ms, body + early reflections): [-92.0, -71.0, -75.0, -83.0, -122.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.3, '30ms': -9.3, '50ms': -13.2, '100ms': -18.9, '150ms': -20.9, '200ms': -24.3}
  Snare-stem noise floor between hits: -96.5 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 3/4, soft 1/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 11 soft hits; measured on 42 medium hits; scaled x2.50 from the record's medium hits (42).
 ZC_metallica-enter-sandman-d491e_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=76.07 s, gap 950 ms, bg -41.3 dB, real to 79 ms, len 525 ms, rel -0.6 dB REAL
  hard rr2: t=187.85 s, gap 952 ms, bg -32.5 dB, real to 458 ms, len 535 ms, rel -0.1 dB REAL
  hard rr3: t=164.71 s, gap 972 ms, bg -35.4 dB, real to 259 ms, len 524 ms, rel -0.8 dB REAL
  hard rr4: t=259.56 s, gap 2171 ms, bg -38.8 dB, real to 239 ms, len 548 ms, rel -0.7 dB REAL
  medium rr1: t=82.83 s, gap 154 ms, bg -34.3 dB, real to 74 ms, len 503 ms, rel -3.1 dB REAL
  medium rr2: t=134.89 s, gap 181 ms, bg -33.6 dB, real to 134 ms, len 550 ms, rel -4.1 dB REAL
  medium rr3: t=144.5 s, gap 234 ms, bg -36.0 dB, real to 119 ms, len 552 ms, rel -5.9 dB REAL
  medium rr4: t=160.82 s, gap 998 ms, bg -36.7 dB, real to 184 ms, len 530 ms, rel -5.7 dB ESTIMATE (measured on 42 medium hits)
  soft rr1: t=314.03 s, gap 237 ms, bg -27.6 dB, real to 79 ms, len 520 ms, rel -13.3 dB REAL
  soft rr2: t=274.98 s, gap 492 ms, bg -39.7 dB, real to 399 ms, len 540 ms, rel -12.1 dB ESTIMATE (measured on 11 soft hits)
  soft rr3: t=254.03 s, gap 717 ms, bg -34.8 dB, real to 389 ms, len 525 ms, rel -12.1 dB ESTIMATE (measured on 11 soft hits)
  soft rr4: t=190.72 s, gap 950 ms, bg -31.2 dB, real to 319 ms, len 544 ms, rel -12.1 dB ESTIMATE (measured on 11 soft hits)
  ghost rr1: t=189.99 s, gap 718 ms, bg -35.1 dB, real to 468 ms, len 549 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (42))
  ghost rr2: t=174.11 s, gap 713 ms, bg -36.2 dB, real to 269 ms, len 535 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (42))
  ghost rr3: t=149.32 s, gap 953 ms, bg -36.1 dB, real to 473 ms, len 535 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (42))
  ghost rr4: t=74.14 s, gap 396 ms, bg -39.3 dB, real to 104 ms, len 540 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (42))