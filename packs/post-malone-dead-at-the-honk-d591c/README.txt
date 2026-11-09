ZC SNARE EXTRACT v3.0 - Post Malone - "Dead at the Honky Tonk" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 133 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.72,
    hit-to-hit level SD 15.11 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -12.6  vs full drum stem -11.7  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.0  vs drum stem -8.4
    Hit-locked energy left in the separator residual (snare that got dropped): -46.1 dBFS at 0-5 ms vs -20.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -24.9, '150-300': -2.8, '300-600': -4.1, '600-1200': -3.7, '1200-2500': -3.3, '2500-5000': -1.7, '5000-8000': -1.2, '8000-12000': -1.2, '12000-16000': -2.0}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [5.46, 3.49, 4.1, 4.69] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-105.0, -35.0, -105.0, -105.0, -158.0] dB/s  ->  T60 [0.57, 1.71, 0.57, 0.57, 0.38] s
  early part (60-150 ms, body + early reflections): [None, -129.0, None, -105.0, -158.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -2.0, '30ms': -4.7, '50ms': -7.9, '100ms': -15.8, '150ms': -20.4, '200ms': -20.9}
  Snare-stem noise floor between hits: -91.8 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_post-malone-dead-at-the-honk-d591c_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=68.06 s, gap 2656 ms, bg -42.1 dB, real to 69 ms, len 454 ms, rel 0.9 dB REAL
  hard rr2: t=177.35 s, gap 1081 ms, bg -33.0 dB, real to 59 ms, len 441 ms, rel 1.5 dB REAL
  hard rr3: t=126.75 s, gap 1437 ms, bg -36.5 dB, real to 59 ms, len 435 ms, rel -2.3 dB REAL
  hard rr4: t=168.68 s, gap 585 ms, bg -35.5 dB, real to 59 ms, len 426 ms, rel 0.1 dB REAL
  medium rr1: t=146.99 s, gap 395 ms, bg -38.6 dB, real to 59 ms, len 415 ms, rel -3.7 dB REAL
  medium rr2: t=88.08 s, gap 234 ms, bg -28.5 dB, real to 219 ms, len 393 ms, rel -8.6 dB REAL
  medium rr3: t=55.05 s, gap 127 ms, bg -34.0 dB, real to 99 ms, len 402 ms, rel -6.8 dB REAL
  medium rr4: t=97.84 s, gap 351 ms, bg -31.1 dB, real to 59 ms, len 410 ms, rel -3.1 dB REAL
  soft rr1: t=7.11 s, gap 352 ms, bg -40.4 dB, real to 69 ms, len 431 ms, rel -12 dB ESTIMATE
  soft rr2: t=116.63 s, gap 570 ms, bg -34.5 dB, real to 59 ms, len 440 ms, rel -12 dB ESTIMATE
  soft rr3: t=43.61 s, gap 1438 ms, bg -34.5 dB, real to 79 ms, len 430 ms, rel -12 dB ESTIMATE
  soft rr4: t=86.27 s, gap 1424 ms, bg -36.8 dB, real to 74 ms, len 445 ms, rel -12 dB ESTIMATE
  ghost rr1: t=175.91 s, gap 720 ms, bg -29.5 dB, real to 59 ms, len 440 ms, rel -20 dB ESTIMATE
  ghost rr2: t=103.62 s, gap 581 ms, bg -30.7 dB, real to 59 ms, len 446 ms, rel -20 dB ESTIMATE
  ghost rr3: t=90.97 s, gap 350 ms, bg -39.9 dB, real to 99 ms, len 431 ms, rel -20 dB ESTIMATE
  ghost rr4: t=181.69 s, gap 1436 ms, bg -34.8 dB, real to 59 ms, len 456 ms, rel -20 dB ESTIMATE