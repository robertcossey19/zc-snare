ZC SNARE EXTRACT v3.0 - Asking Alexandria - "Breathless" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 293 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.91,
    hit-to-hit level SD 2.8 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.1  vs full drum stem -8.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -12.7  vs drum stem -9.9
    Hit-locked energy left in the separator residual (snare that got dropped): -43.0 dBFS at 0-5 ms vs -9.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -28.6, '150-300': -0.1, '300-600': -0.7, '600-1200': -1.1, '1200-2500': -1.8, '2500-5000': -3.6, '5000-8000': -3.6, '8000-12000': -5.5, '12000-16000': -7.2}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [6.28, 7.78, 2.24, 3.29] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-136.0, -155.0, -148.0, -112.0, -125.0] dB/s  ->  T60 [0.44, 0.39, 0.41, 0.54, 0.48] s
  early part (60-150 ms, body + early reflections): [None, -132.0, -114.0, -112.0, -125.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.8, '30ms': -16.0, '50ms': -14.0, '100ms': -20.2, '150ms': -28.5, '200ms': -31.1}
  Snare-stem noise floor between hits: -85.4 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 1/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_asking-alexandria-breathless-d53a2_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=193.89 s, gap 1497 ms, bg -39.8 dB, real to 304 ms, len 531 ms, rel 0.5 dB REAL
  hard rr2: t=201.39 s, gap 742 ms, bg -43.6 dB, real to 189 ms, len 500 ms, rel -0.3 dB REAL
  hard rr3: t=139.52 s, gap 750 ms, bg -42.7 dB, real to 468 ms, len 481 ms, rel 0.6 dB REAL
  hard rr4: t=118.52 s, gap 746 ms, bg -40.3 dB, real to 379 ms, len 461 ms, rel -0.4 dB REAL
  medium rr1: t=229.89 s, gap 161 ms, bg -42.1 dB, real to 119 ms, len 476 ms, rel -3.8 dB REAL
  medium rr2: t=36.13 s, gap 740 ms, bg -42.2 dB, real to 379 ms, len 490 ms, rel -6 dB ESTIMATE
  medium rr3: t=195.39 s, gap 1494 ms, bg -44.0 dB, real to 194 ms, len 500 ms, rel -6 dB ESTIMATE
  medium rr4: t=72.88 s, gap 560 ms, bg -41.6 dB, real to 279 ms, len 490 ms, rel -6 dB ESTIMATE
  soft rr1: t=60.13 s, gap 743 ms, bg -45.4 dB, real to 189 ms, len 510 ms, rel -12 dB ESTIMATE
  soft rr2: t=234.96 s, gap 9000 ms, bg -26.2 dB, real to 94 ms, len 525 ms, rel -12 dB ESTIMATE
  soft rr3: t=202.9 s, gap 557 ms, bg -41.7 dB, real to 184 ms, len 532 ms, rel -12 dB ESTIMATE
  soft rr4: t=103.59 s, gap 1420 ms, bg -20.9 dB, real to 154 ms, len 534 ms, rel -12 dB ESTIMATE
  ghost rr1: t=138.02 s, gap 563 ms, bg -41.2 dB, real to 389 ms, len 485 ms, rel -20 dB ESTIMATE
  ghost rr2: t=232.89 s, gap 745 ms, bg -41.4 dB, real to 119 ms, len 494 ms, rel -20 dB ESTIMATE
  ghost rr3: t=54.5 s, gap 499 ms, bg -42.5 dB, real to 199 ms, len 521 ms, rel -20 dB ESTIMATE
  ghost rr4: t=162.21 s, gap 369 ms, bg -33.5 dB, real to 244 ms, len 500 ms, rel -20 dB ESTIMATE