ZC SNARE EXTRACT v3.0 - Architects - "Blackhole" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 154 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.925,
    hit-to-hit level SD 4.74 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.9  vs full drum stem -9.6  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -9.3  vs drum stem -9.0
    Hit-locked energy left in the separator residual (snare that got dropped): -44.5 dBFS at 0-5 ms vs -11.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -17.1, '150-300': -0.1, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.6, '2500-5000': -1.1, '5000-8000': -1.3, '8000-12000': -3.1, '12000-16000': -5.8}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.17, 3.72, 4.78, 6.01] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-140.0, -170.0, -154.0, -85.0, -126.0] dB/s  ->  T60 [0.43, 0.35, 0.39, 0.71, 0.47] s
  early part (60-150 ms, body + early reflections): [None, -120.0, -77.0, -85.0, -126.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -8.5, '50ms': -13.6, '100ms': -15.4, '150ms': -20.7, '200ms': -31.8}
  Snare-stem noise floor between hits: -81.8 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_architects-blackhole-22anq_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=161.22 s, gap 1491 ms, bg -39.1 dB, real to 229 ms, len 657 ms, rel 0.2 dB REAL
  hard rr2: t=124.29 s, gap 554 ms, bg -43.4 dB, real to 349 ms, len 555 ms, rel -0.6 dB REAL
  hard rr3: t=44.6 s, gap 506 ms, bg -40.0 dB, real to 234 ms, len 620 ms, rel -0.8 dB REAL
  hard rr4: t=59.22 s, gap 1490 ms, bg -33.4 dB, real to 399 ms, len 580 ms, rel -0.3 dB REAL
  medium rr1: t=33.26 s, gap 122 ms, bg -24.9 dB, real to 59 ms, len 587 ms, rel -9.4 dB REAL
  medium rr2: t=191.22 s, gap 236 ms, bg -36.3 dB, real to 189 ms, len 561 ms, rel -3.1 dB REAL
  medium rr3: t=82.1 s, gap 286 ms, bg -16.7 dB, real to 59 ms, len 640 ms, rel -4.4 dB REAL
  medium rr4: t=142.1 s, gap 278 ms, bg -15.5 dB, real to 269 ms, len 629 ms, rel -3.2 dB REAL
  soft rr1: t=120.72 s, gap 376 ms, bg -39.8 dB, real to 379 ms, len 591 ms, rel -12 dB ESTIMATE
  soft rr2: t=77.22 s, gap 378 ms, bg -39.5 dB, real to 369 ms, len 620 ms, rel -12 dB ESTIMATE
  soft rr3: t=132.72 s, gap 363 ms, bg -43.9 dB, real to 264 ms, len 585 ms, rel -12 dB ESTIMATE
  soft rr4: t=24.35 s, gap 362 ms, bg -43.0 dB, real to 354 ms, len 605 ms, rel -12 dB ESTIMATE
  ghost rr1: t=28.85 s, gap 360 ms, bg -45.0 dB, real to 344 ms, len 581 ms, rel -20 dB ESTIMATE
  ghost rr2: t=196.1 s, gap 185 ms, bg -39.9 dB, real to 174 ms, len 580 ms, rel -20 dB ESTIMATE
  ghost rr3: t=22.85 s, gap 366 ms, bg -45.8 dB, real to 349 ms, len 610 ms, rel -20 dB ESTIMATE
  ghost rr4: t=154.29 s, gap 191 ms, bg -42.8 dB, real to 234 ms, len 626 ms, rel -20 dB ESTIMATE