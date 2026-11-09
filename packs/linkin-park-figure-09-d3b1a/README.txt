ZC SNARE EXTRACT v5.0 - Linkin Park - "Figure.09" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 141 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.755,
    hit-to-hit level SD 4.0 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -8.2  vs full drum stem -8.1  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -16.0  vs drum stem -15.6
    Hit-locked energy left in the separator residual (snare that got dropped): -58.7 dBFS at 0-5 ms vs -10.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -3.9, '150-300': -0.1, '300-600': -0.1, '600-1200': 0.0, '1200-2500': -0.0, '2500-5000': -0.8, '5000-8000': -2.6, '8000-12000': -6.7, '12000-16000': -11.6}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    332 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.17, 1.41, 1.47, 6.87] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-126.0, -109.0, -91.0, -144.0, -176.0] dB/s  ->  T60 [0.48, 0.55, 0.66, 0.42, 0.34] s
  early part (60-150 ms, body + early reflections): [None, -109.0, -106.0, -144.0, -176.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -7.1, '30ms': -13.5, '50ms': -17.8, '100ms': -22.9, '150ms': -25.4, '200ms': -30.2}
  Snare-stem noise floor between hits: -96.3 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 2/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 6 soft hits; scaled x2.50 from the record's medium hits (29).
 ZC_linkin-park-figure-09-d3b1a_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=42.32 s, gap 1217 ms, bg -41.8 dB, real to 114 ms, len 470 ms, rel -1.0 dB REAL
  hard rr2: t=37.42 s, gap 1215 ms, bg -37.9 dB, real to 104 ms, len 480 ms, rel 0.6 dB REAL
  hard rr3: t=26.41 s, gap 1215 ms, bg -33.5 dB, real to 104 ms, len 470 ms, rel -0.3 dB REAL
  hard rr4: t=33.75 s, gap 662 ms, bg -34.2 dB, real to 124 ms, len 475 ms, rel -1.6 dB REAL
  medium rr1: t=47.22 s, gap 1216 ms, bg -28.8 dB, real to 59 ms, len 419 ms, rel -9.1 dB REAL
  medium rr2: t=63.13 s, gap 595 ms, bg -42.8 dB, real to 354 ms, len 460 ms, rel -3.1 dB REAL
  medium rr3: t=23.96 s, gap 145 ms, bg -24.7 dB, real to 134 ms, len 430 ms, rel -4.5 dB REAL
  medium rr4: t=150.04 s, gap 1216 ms, bg -36.5 dB, real to 304 ms, len 466 ms, rel -4.6 dB REAL
  soft rr1: t=94.96 s, gap 454 ms, bg -31.8 dB, real to 59 ms, len 465 ms, rel -11.1 dB REAL
  soft rr2: t=93.73 s, gap 453 ms, bg -33.8 dB, real to 59 ms, len 402 ms, rel -13.1 dB REAL
  soft rr3: t=176.97 s, gap 1215 ms, bg -37.1 dB, real to 374 ms, len 455 ms, rel -12.1 dB ESTIMATE (measured on 6 soft hits)
  soft rr4: t=115.77 s, gap 1217 ms, bg -37.0 dB, real to 164 ms, len 470 ms, rel -12.1 dB ESTIMATE (measured on 6 soft hits)
  ghost rr1: t=174.53 s, gap 1216 ms, bg -37.8 dB, real to 149 ms, len 474 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (29))
  ghost rr2: t=32.53 s, gap 1215 ms, bg -33.8 dB, real to 79 ms, len 470 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (29))
  ghost rr3: t=36.2 s, gap 1217 ms, bg -34.4 dB, real to 99 ms, len 491 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (29))
  ghost rr4: t=41.1 s, gap 1216 ms, bg -34.2 dB, real to 109 ms, len 480 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (29))