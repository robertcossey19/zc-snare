ZC SNARE EXTRACT v5.0 - Post Malone - "Dead at the Honky Tonk" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 115 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.728,
    hit-to-hit level SD 15.35 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -12.7  vs full drum stem -11.8  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.0  vs drum stem -8.8
    Hit-locked energy left in the separator residual (snare that got dropped): -44.3 dBFS at 0-5 ms vs -20.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -23.9, '150-300': -2.4, '300-600': -3.9, '600-1200': -3.6, '1200-2500': -3.5, '2500-5000': -2.0, '5000-8000': -1.5, '8000-12000': -1.5, '12000-16000': -2.3}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak); a bin well below it after 30 ms is a hole
    the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    65 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.1, 4.1, 2.7, 4.67] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-142.0, -47.0, -108.0, -108.0, -132.0] dB/s  ->  T60 [0.42, 1.27, 0.55, 0.55, 0.46] s
  early part (60-150 ms, body + early reflections): [-142.0, -127.0, None, -108.0, -132.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.0, '30ms': -3.5, '50ms': -7.2, '100ms': -15.9, '150ms': -17.3}
  Snare-stem noise floor between hits: -91.6 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 1/4, ghost 1/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 7 ghost hits; scaled x2.50 from the record's medium hits (28).
 ZC_post-malone-dead-at-the-honk-d591c_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=7.11 s, gap 352 ms, bg -42.7 dB, real to 349 ms, len 495 ms, rel 5.4 dB REAL
  hard rr2: t=126.75 s, gap 1438 ms, bg -37.2 dB, real to 104 ms, len 505 ms, rel -1.7 dB REAL
  hard rr3: t=105.06 s, gap 591 ms, bg -36.5 dB, real to 139 ms, len 526 ms, rel 0.3 dB REAL
  hard rr4: t=168.68 s, gap 585 ms, bg -33.2 dB, real to 239 ms, len 521 ms, rel 0.4 dB REAL
  medium rr1: t=55.05 s, gap 125 ms, bg -36.2 dB, real to 79 ms, len 519 ms, rel -6.5 dB REAL
  medium rr2: t=53.6 s, gap 351 ms, bg -35.5 dB, real to 94 ms, len 512 ms, rel -7.0 dB REAL
  medium rr3: t=142.65 s, gap 225 ms, bg -34.7 dB, real to 164 ms, len 505 ms, rel -3.2 dB REAL
  medium rr4: t=149.03 s, gap 125 ms, bg -23.4 dB, real to 124 ms, len 507 ms, rel -6.8 dB REAL
  soft rr1: t=170.71 s, gap 278 ms, bg -42.0 dB, real to 59 ms, len 508 ms, rel -10.8 dB REAL
  soft rr2: t=43.61 s, gap 1438 ms, bg -38.6 dB, real to 119 ms, len 519 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  soft rr3: t=175.91 s, gap 1438 ms, bg -30.8 dB, real to 84 ms, len 525 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  soft rr4: t=67.11 s, gap 150 ms, bg -40.3 dB, real to 249 ms, len 514 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (28))
  ghost rr1: t=73.26 s, gap 149 ms, bg -24.1 dB, real to 139 ms, len 520 ms, rel -21.4 dB REAL
  ghost rr2: t=68.06 s, gap 494 ms, bg -43.5 dB, real to 164 ms, len 544 ms, rel -22.1 dB ESTIMATE (measured on 7 ghost hits)
  ghost rr3: t=92.05 s, gap 1308 ms, bg -32.0 dB, real to 149 ms, len 540 ms, rel -22.1 dB ESTIMATE (measured on 7 ghost hits)
  ghost rr4: t=67.47 s, gap 583 ms, bg -34.4 dB, real to 124 ms, len 560 ms, rel -22.1 dB ESTIMATE (measured on 7 ghost hits)