ZC SNARE EXTRACT v3.0 - Asking Alexandria - "Breathless" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 298 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.914,
    hit-to-hit level SD 2.56 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -8.7  vs full drum stem -8.2  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -12.5  vs drum stem -9.8
    Hit-locked energy left in the separator residual (snare that got dropped): -44.8 dBFS at 0-5 ms vs -8.8 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -28.6, '150-300': -0.1, '300-600': -0.7, '600-1200': -1.1, '1200-2500': -1.9, '2500-5000': -3.4, '5000-8000': -3.5, '8000-12000': -5.4, '12000-16000': -7.3}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.01, 1.81, 5.76, 4.99] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-103.0, -77.0, -127.0, -90.0, -116.0] dB/s  ->  T60 [0.58, 0.78, 0.47, 0.67, 0.52] s
  early part (60-150 ms, body + early reflections): [None, -122.0, -94.0, -103.0, -116.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.8, '30ms': -16.0, '50ms': -13.9, '100ms': -20.4, '150ms': -26.9, '200ms': -34.0}
  Snare-stem noise floor between hits: -85.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 2/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_asking-alexandria-breathless-d53a2_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=61.63 s, gap 744 ms, bg -42.0 dB, real to 224 ms, len 632 ms, rel -0.2 dB REAL
  hard rr2: t=195.39 s, gap 1494 ms, bg -44.2 dB, real to 209 ms, len 680 ms, rel -0.1 dB REAL
  hard rr3: t=234.96 s, gap 9000 ms, bg -26.2 dB, real to 149 ms, len 854 ms, rel -0.5 dB REAL
  hard rr4: t=202.9 s, gap 557 ms, bg -40.7 dB, real to 194 ms, len 860 ms, rel 1.3 dB REAL
  medium rr1: t=84.24 s, gap 282 ms, bg -25.0 dB, real to 149 ms, len 814 ms, rel -3.0 dB REAL
  medium rr2: t=229.89 s, gap 253 ms, bg -40.3 dB, real to 238 ms, len 655 ms, rel -4.9 dB REAL
  medium rr3: t=162.21 s, gap 369 ms, bg -38.7 dB, real to 324 ms, len 939 ms, rel -6 dB ESTIMATE
  medium rr4: t=225.39 s, gap 415 ms, bg -45.8 dB, real to 234 ms, len 784 ms, rel -6 dB ESTIMATE
  soft rr1: t=34.63 s, gap 262 ms, bg -43.6 dB, real to 247 ms, len 834 ms, rel -12 dB ESTIMATE
  soft rr2: t=201.39 s, gap 370 ms, bg -41.6 dB, real to 204 ms, len 730 ms, rel -12 dB ESTIMATE
  soft rr3: t=72.88 s, gap 380 ms, bg -41.5 dB, real to 219 ms, len 680 ms, rel -12 dB ESTIMATE
  soft rr4: t=136.14 s, gap 366 ms, bg -44.4 dB, real to 244 ms, len 730 ms, rel -12 dB ESTIMATE
  ghost rr1: t=183.39 s, gap 395 ms, bg -38.7 dB, real to 264 ms, len 779 ms, rel -20 dB ESTIMATE
  ghost rr2: t=141.39 s, gap 366 ms, bg -41.9 dB, real to 229 ms, len 795 ms, rel -20 dB ESTIMATE
  ghost rr3: t=135.39 s, gap 367 ms, bg -46.4 dB, real to 264 ms, len 724 ms, rel -20 dB ESTIMATE
  ghost rr4: t=186.39 s, gap 459 ms, bg -35.5 dB, real to 264 ms, len 830 ms, rel -20 dB ESTIMATE