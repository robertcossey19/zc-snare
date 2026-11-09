ZC SNARE EXTRACT v5.0 - Asking Alexandria - "The Final Episode" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 170 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.94,
    hit-to-hit level SD 3.46 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.0  vs full drum stem -9.2  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.8  vs drum stem -11.1
    Hit-locked energy left in the separator residual (snare that got dropped): -36.5 dBFS at 0-5 ms vs -10.9 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -15.1, '150-300': -0.0, '300-600': -0.3, '600-1200': -0.9, '1200-2500': -1.7, '2500-5000': -4.2, '5000-8000': -5.2, '8000-12000': -8.9, '12000-16000': -14.4}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak); a bin well below it after 30 ms is a hole
    the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    349 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.45, 1.84, 2.22, 0.84] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-98.0, -115.0, -148.0, -81.0, -81.0] dB/s  ->  T60 [0.61, 0.52, 0.4, 0.74, 0.74] s
  early part (60-150 ms, body + early reflections): [None, -103.0, -120.0, -118.0, -153.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -0.2, '30ms': -12.2, '50ms': -13.2, '100ms': -23.1, '150ms': -27.9, '200ms': -28.6}
  Snare-stem noise floor between hits: -91.2 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 3/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: generic (no quieter hits on this record).
 ZC_asking-alexandria-the-final--d3f79_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=69.09 s, gap 605 ms, bg -44.9 dB, real to 319 ms, len 577 ms, rel -1.2 dB REAL
  hard rr2: t=34.16 s, gap 611 ms, bg -39.8 dB, real to 399 ms, len 535 ms, rel -0.5 dB REAL
  hard rr3: t=45.19 s, gap 1827 ms, bg -44.4 dB, real to 294 ms, len 555 ms, rel 0.1 dB REAL
  hard rr4: t=191.03 s, gap 3053 ms, bg -25.6 dB, real to 204 ms, len 549 ms, rel 0.1 dB REAL
  medium rr1: t=256.9 s, gap 237 ms, bg -45.5 dB, real to 59 ms, len 526 ms, rel -3.7 dB REAL
  medium rr2: t=161.0 s, gap 286 ms, bg -40.5 dB, real to 104 ms, len 531 ms, rel -4.6 dB REAL
  medium rr3: t=127.92 s, gap 252 ms, bg -50.7 dB, real to 129 ms, len 486 ms, rel -3.5 dB REAL
  medium rr4: t=130.37 s, gap 3818 ms, bg -28.3 dB, real to 214 ms, len 524 ms, rel -6 dB ESTIMATE (generic (no quieter hits on this record))
  soft rr1: t=75.82 s, gap 532 ms, bg -42.1 dB, real to 219 ms, len 515 ms, rel -12 dB ESTIMATE (generic (no quieter hits on this record))
  soft rr2: t=241.47 s, gap 495 ms, bg -43.4 dB, real to 339 ms, len 500 ms, rel -12 dB ESTIMATE (generic (no quieter hits on this record))
  soft rr3: t=54.67 s, gap 685 ms, bg -33.9 dB, real to 94 ms, len 525 ms, rel -12 dB ESTIMATE (generic (no quieter hits on this record))
  soft rr4: t=96.67 s, gap 623 ms, bg -41.1 dB, real to 204 ms, len 520 ms, rel -12 dB ESTIMATE (generic (no quieter hits on this record))
  ghost rr1: t=165.29 s, gap 1215 ms, bg -32.6 dB, real to 159 ms, len 522 ms, rel -20 dB ESTIMATE (generic (no quieter hits on this record))
  ghost rr2: t=72.15 s, gap 459 ms, bg -41.1 dB, real to 414 ms, len 505 ms, rel -20 dB ESTIMATE (generic (no quieter hits on this record))
  ghost rr3: t=68.48 s, gap 456 ms, bg -41.0 dB, real to 359 ms, len 510 ms, rel -20 dB ESTIMATE (generic (no quieter hits on this record))
  ghost rr4: t=28.65 s, gap 454 ms, bg -42.3 dB, real to 234 ms, len 505 ms, rel -20 dB ESTIMATE (generic (no quieter hits on this record))