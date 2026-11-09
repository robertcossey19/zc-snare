ZC SNARE EXTRACT v5.0 - Nothing More - "If It Doesn't Hurt" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 136 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.91,
    hit-to-hit level SD 5.83 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.0  vs full drum stem -9.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.5  vs drum stem -11.2
    Hit-locked energy left in the separator residual (snare that got dropped): -43.1 dBFS at 0-5 ms vs -11.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -10.8, '150-300': -0.1, '300-600': -0.1, '600-1200': -0.1, '1200-2500': -0.2, '2500-5000': -1.2, '5000-8000': -1.5, '8000-12000': -3.0, '12000-16000': -4.9}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak); a bin well below it after 30 ms is a hole
    the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    303 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [1.66, 2.18, 2.2, 7.28] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-126.0, -89.0, -122.0, -129.0, -176.0] dB/s  ->  T60 [0.48, 0.67, 0.49, 0.46, 0.34] s
  early part (60-150 ms, body + early reflections): [None, -154.0, -123.0, -127.0, -176.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -12.2, '50ms': -9.9, '100ms': -16.8, '150ms': -23.7, '200ms': -27.0}
  Snare-stem noise floor between hits: -83.9 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 9 soft hits; scaled x2.50 from the record's medium hits (19).
 ZC_nothing-more-if-it-doesn-t-h-ztf6s_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=84.61 s, gap 1255 ms, bg -41.3 dB, real to 433 ms, len 565 ms, rel 1.0 dB REAL
  hard rr2: t=104.82 s, gap 781 ms, bg -46.2 dB, real to 468 ms, len 565 ms, rel -0.5 dB REAL
  hard rr3: t=87.14 s, gap 1255 ms, bg -43.3 dB, real to 468 ms, len 545 ms, rel 0.4 dB REAL
  hard rr4: t=133.24 s, gap 624 ms, bg -44.9 dB, real to 294 ms, len 586 ms, rel -0.3 dB REAL
  medium rr1: t=176.35 s, gap 157 ms, bg -26.2 dB, real to 144 ms, len 520 ms, rel -4.5 dB REAL
  medium rr2: t=176.03 s, gap 152 ms, bg -26.3 dB, real to 149 ms, len 549 ms, rel -4.5 dB REAL
  medium rr3: t=176.5 s, gap 154 ms, bg -24.6 dB, real to 149 ms, len 576 ms, rel -3.7 dB REAL
  medium rr4: t=100.56 s, gap 201 ms, bg -17.0 dB, real to 74 ms, len 579 ms, rel -4.3 dB REAL
  soft rr1: t=24.13 s, gap 167 ms, bg -15.1 dB, real to 59 ms, len 556 ms, rel -15.7 dB REAL
  soft rr2: t=44.19 s, gap 468 ms, bg -45.0 dB, real to 284 ms, len 516 ms, rel -14.5 dB ESTIMATE (measured on 9 soft hits)
  soft rr3: t=160.08 s, gap 938 ms, bg -41.6 dB, real to 384 ms, len 545 ms, rel -14.5 dB ESTIMATE (measured on 9 soft hits)
  soft rr4: t=47.82 s, gap 465 ms, bg -39.7 dB, real to 349 ms, len 562 ms, rel -14.5 dB ESTIMATE (measured on 9 soft hits)
  ghost rr1: t=119.35 s, gap 782 ms, bg -42.4 dB, real to 438 ms, len 520 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  ghost rr2: t=162.61 s, gap 938 ms, bg -45.0 dB, real to 199 ms, len 536 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  ghost rr3: t=157.56 s, gap 940 ms, bg -37.8 dB, real to 404 ms, len 545 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))
  ghost rr4: t=36.45 s, gap 347 ms, bg -42.0 dB, real to 324 ms, len 595 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (19))