ZC SNARE EXTRACT v5.0 - Limp Bizkit - "Making Love To Morgan Wallen" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 158 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.779,
    hit-to-hit level SD 12.08 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.7  vs full drum stem -9.3  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.4  vs drum stem -11.3
    Hit-locked energy left in the separator residual (snare that got dropped): -44.2 dBFS at 0-5 ms vs -11.7 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -4.7, '150-300': -0.0, '300-600': -0.1, '600-1200': -0.1, '1200-2500': -0.1, '2500-5000': -0.7, '5000-8000': -1.1, '8000-12000': -2.1, '12000-16000': -4.3}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    282 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.9, 4.78, 4.97, 6.46] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-52.0, -113.0, -105.0, -117.0, -125.0] dB/s  ->  T60 [1.14, 0.53, 0.57, 0.51, 0.48] s
  early part (60-150 ms, body + early reflections): [-52.0, -98.0, -88.0, -92.0, -120.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -9.6, '50ms': -9.1, '100ms': -14.0, '150ms': -17.7, '200ms': -22.2, '300ms': -30.2}
  Snare-stem noise floor between hits: -80.8 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 3/4, soft 1/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 12 medium hits; measured on 22 ghost hits; measured on 32 soft hits.
 ZC_limp-bizkit-making-love-to-m-xaom8_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=134.21 s, gap 689 ms, bg -42.3 dB, real to 443 ms, len 805 ms, rel 0.6 dB REAL
  hard rr2: t=136.49 s, gap 579 ms, bg -45.2 dB, real to 448 ms, len 790 ms, rel 0.4 dB REAL
  hard rr3: t=209.5 s, gap 1276 ms, bg -42.1 dB, real to 443 ms, len 716 ms, rel 0.7 dB REAL
  hard rr4: t=213.05 s, gap 558 ms, bg -45.9 dB, real to 299 ms, len 801 ms, rel -1.1 dB REAL
  medium rr1: t=234.99 s, gap 174 ms, bg -17.8 dB, real to 79 ms, len 709 ms, rel -3.3 dB REAL
  medium rr2: t=122.06 s, gap 707 ms, bg -24.5 dB, real to 159 ms, len 720 ms, rel -6.8 dB REAL
  medium rr3: t=239.92 s, gap 284 ms, bg -16.6 dB, real to 189 ms, len 769 ms, rel -7.9 dB REAL
  medium rr4: t=81.63 s, gap 711 ms, bg -42.8 dB, real to 279 ms, len 800 ms, rel -5.4 dB ESTIMATE (measured on 12 medium hits)
  soft rr1: t=183.19 s, gap 178 ms, bg -23.3 dB, real to 104 ms, len 638 ms, rel -14.5 dB REAL
  soft rr2: t=90.8 s, gap 406 ms, bg -42.0 dB, real to 119 ms, len 784 ms, rel -16.1 dB ESTIMATE (measured on 32 soft hits)
  soft rr3: t=22.23 s, gap 402 ms, bg -40.9 dB, real to 389 ms, len 804 ms, rel -16.1 dB ESTIMATE (measured on 32 soft hits)
  soft rr4: t=115.92 s, gap 400 ms, bg -41.5 dB, real to 384 ms, len 794 ms, rel -16.1 dB ESTIMATE (measured on 32 soft hits)
  ghost rr1: t=56.5 s, gap 396 ms, bg -41.2 dB, real to 369 ms, len 759 ms, rel -20.8 dB ESTIMATE (measured on 22 ghost hits)
  ghost rr2: t=104.5 s, gap 400 ms, bg -45.7 dB, real to 384 ms, len 779 ms, rel -20.8 dB ESTIMATE (measured on 22 ghost hits)
  ghost rr3: t=38.22 s, gap 385 ms, bg -43.5 dB, real to 374 ms, len 806 ms, rel -20.8 dB ESTIMATE (measured on 22 ghost hits)
  ghost rr4: t=26.8 s, gap 393 ms, bg -39.0 dB, real to 369 ms, len 809 ms, rel -20.8 dB ESTIMATE (measured on 22 ghost hits)