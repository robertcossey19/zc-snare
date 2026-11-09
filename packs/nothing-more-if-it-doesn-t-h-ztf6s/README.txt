ZC SNARE EXTRACT v5.0 - Nothing More - "If It Doesn't Hurt" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 140 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.9,
    hit-to-hit level SD 6.67 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.9  vs full drum stem -9.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.4  vs drum stem -11.1
    Hit-locked energy left in the separator residual (snare that got dropped): -43.1 dBFS at 0-5 ms vs -11.0 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -12.1, '150-300': -0.1, '300-600': -0.2, '600-1200': -0.1, '1200-2500': -0.2, '2500-5000': -1.2, '5000-8000': -1.4, '8000-12000': -2.7, '12000-16000': -4.6}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    308 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.2, 1.66, 3.9, 1.9] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-119.0, -85.0, -123.0, -114.0, -181.0] dB/s  ->  T60 [0.5, 0.71, 0.49, 0.52, 0.33] s
  early part (60-150 ms, body + early reflections): [None, -134.0, -123.0, -125.0, -181.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -11.7, '50ms': -9.6, '100ms': -16.9, '150ms': -23.2, '200ms': -26.7}
  Snare-stem noise floor between hits: -83.0 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 10 soft hits; measured on 6 ghost hits.
 ZC_nothing-more-if-it-doesn-t-h-ztf6s_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=104.82 s, gap 781 ms, bg -44.1 dB, real to 463 ms, len 585 ms, rel -0.7 dB REAL
  hard rr2: t=84.61 s, gap 1255 ms, bg -36.5 dB, real to 468 ms, len 575 ms, rel 0.8 dB REAL
  hard rr3: t=41.66 s, gap 1255 ms, bg -35.3 dB, real to 304 ms, len 601 ms, rel 0.2 dB REAL
  hard rr4: t=36.45 s, gap 467 ms, bg -41.0 dB, real to 209 ms, len 560 ms, rel 0.1 dB REAL
  medium rr1: t=176.35 s, gap 157 ms, bg -24.1 dB, real to 144 ms, len 590 ms, rel -4.2 dB REAL
  medium rr2: t=176.5 s, gap 156 ms, bg -22.4 dB, real to 144 ms, len 626 ms, rel -3.7 dB REAL
  medium rr3: t=176.03 s, gap 153 ms, bg -26.1 dB, real to 144 ms, len 579 ms, rel -4.6 dB REAL
  medium rr4: t=175.87 s, gap 157 ms, bg -43.7 dB, real to 159 ms, len 601 ms, rel -3.8 dB REAL
  soft rr1: t=24.13 s, gap 157 ms, bg -14.4 dB, real to 129 ms, len 649 ms, rel -15.4 dB REAL
  soft rr2: t=174.77 s, gap 466 ms, bg -42.3 dB, real to 289 ms, len 581 ms, rel -13.5 dB ESTIMATE (measured on 10 soft hits)
  soft rr3: t=44.19 s, gap 468 ms, bg -45.9 dB, real to 339 ms, len 545 ms, rel -13.5 dB ESTIMATE (measured on 10 soft hits)
  soft rr4: t=89.5 s, gap 466 ms, bg -39.9 dB, real to 184 ms, len 602 ms, rel -13.5 dB ESTIMATE (measured on 10 soft hits)
  ghost rr1: t=47.82 s, gap 468 ms, bg -40.3 dB, real to 359 ms, len 622 ms, rel -24.2 dB ESTIMATE (measured on 6 ghost hits)
  ghost rr2: t=160.08 s, gap 938 ms, bg -42.9 dB, real to 463 ms, len 566 ms, rel -24.2 dB ESTIMATE (measured on 6 ghost hits)
  ghost rr3: t=121.87 s, gap 1255 ms, bg -43.4 dB, real to 294 ms, len 605 ms, rel -24.2 dB ESTIMATE (measured on 6 ghost hits)
  ghost rr4: t=70.72 s, gap 687 ms, bg -42.5 dB, real to 109 ms, len 590 ms, rel -24.2 dB ESTIMATE (measured on 6 ghost hits)