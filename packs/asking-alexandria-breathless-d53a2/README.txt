ZC SNARE EXTRACT v3.0 - Asking Alexandria - "Breathless" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 302 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.916,
    hit-to-hit level SD 1.94 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -8.9  vs full drum stem -8.4  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -12.6  vs drum stem -9.9
    Hit-locked energy left in the separator residual (snare that got dropped): -45.2 dBFS at 0-5 ms vs -9.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -28.7, '150-300': -0.1, '300-600': -0.7, '600-1200': -1.2, '1200-2500': -2.0, '2500-5000': -3.7, '5000-8000': -3.7, '8000-12000': -5.8, '12000-16000': -7.7}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.7, 1.81, 6.28, 4.65] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-117.0, -167.0, -114.0, -98.0, -121.0] dB/s  ->  T60 [0.51, 0.36, 0.52, 0.61, 0.5] s
  early part (60-150 ms, body + early reflections): [None, -125.0, -104.0, -98.0, -121.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.8, '30ms': -16.0, '50ms': -14.2, '100ms': -19.9, '150ms': -26.3, '200ms': -31.7}
  Snare-stem noise floor between hits: -84.5 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 1/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_asking-alexandria-breathless-d53a2_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=120.77 s, gap 745 ms, bg -39.8 dB, real to 194 ms, len 526 ms, rel -0.3 dB REAL
  hard rr2: t=195.39 s, gap 1190 ms, bg -38.2 dB, real to 179 ms, len 515 ms, rel -0.0 dB REAL
  hard rr3: t=193.89 s, gap 1307 ms, bg -39.4 dB, real to 269 ms, len 640 ms, rel 0.5 dB REAL
  hard rr4: t=58.63 s, gap 552 ms, bg -42.4 dB, real to 184 ms, len 576 ms, rel -1.8 dB REAL
  medium rr1: t=229.89 s, gap 161 ms, bg -41.7 dB, real to 146 ms, len 655 ms, rel -4.0 dB REAL
  medium rr2: t=108.02 s, gap 549 ms, bg -43.5 dB, real to 214 ms, len 521 ms, rel -6 dB ESTIMATE
  medium rr3: t=168.39 s, gap 1492 ms, bg -43.9 dB, real to 309 ms, len 580 ms, rel -6 dB ESTIMATE
  medium rr4: t=122.27 s, gap 1116 ms, bg -30.9 dB, real to 184 ms, len 690 ms, rel -6 dB ESTIMATE
  soft rr1: t=202.9 s, gap 557 ms, bg -41.1 dB, real to 194 ms, len 542 ms, rel -12 dB ESTIMATE
  soft rr2: t=234.96 s, gap 9000 ms, bg -28.8 dB, real to 149 ms, len 665 ms, rel -12 dB ESTIMATE
  soft rr3: t=123.39 s, gap 1492 ms, bg -37.2 dB, real to 169 ms, len 481 ms, rel -12 dB ESTIMATE
  soft rr4: t=201.39 s, gap 370 ms, bg -42.5 dB, real to 194 ms, len 570 ms, rel -12 dB ESTIMATE
  ghost rr1: t=227.77 s, gap 617 ms, bg -18.3 dB, real to 149 ms, len 570 ms, rel -20 dB ESTIMATE
  ghost rr2: t=141.39 s, gap 366 ms, bg -44.8 dB, real to 234 ms, len 521 ms, rel -20 dB ESTIMATE
  ghost rr3: t=136.14 s, gap 366 ms, bg -45.6 dB, real to 249 ms, len 525 ms, rel -20 dB ESTIMATE
  ghost rr4: t=162.21 s, gap 369 ms, bg -36.8 dB, real to 179 ms, len 610 ms, rel -20 dB ESTIMATE