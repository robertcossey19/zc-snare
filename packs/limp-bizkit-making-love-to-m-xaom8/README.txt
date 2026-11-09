ZC SNARE EXTRACT v3.0 - Limp Bizkit - "Making Love To Morgan Wallen" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 152 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.768,
    hit-to-hit level SD 12.51 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.1  vs full drum stem -9.7  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.8  vs drum stem -11.6
    Hit-locked energy left in the separator residual (snare that got dropped): -45.0 dBFS at 0-5 ms vs -12.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -4.9, '150-300': -0.0, '300-600': -0.1, '600-1200': -0.1, '1200-2500': -0.1, '2500-5000': -0.7, '5000-8000': -1.1, '8000-12000': -2.1, '12000-16000': -4.2}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.65, 3.36, 4.04, 5.1] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-30.0, -105.0, -100.0, -117.0, -137.0] dB/s  ->  T60 [2.0, 0.57, 0.6, 0.51, 0.44] s
  early part (60-150 ms, body + early reflections): [-29.0, -97.0, -88.0, -93.0, -123.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -9.5, '50ms': -8.8, '100ms': -13.7, '150ms': -16.6, '200ms': -22.4, '300ms': -32.3}
  Snare-stem noise floor between hits: -81.0 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_limp-bizkit-making-love-to-m-xaom8_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=136.49 s, gap 709 ms, bg -45.3 dB, real to 419 ms, len 770 ms, rel 0.4 dB REAL
  hard rr2: t=134.21 s, gap 689 ms, bg -41.1 dB, real to 279 ms, len 765 ms, rel 0.6 dB REAL
  hard rr3: t=67.92 s, gap 716 ms, bg -42.0 dB, real to 488 ms, len 731 ms, rel 0.4 dB REAL
  hard rr4: t=79.35 s, gap 693 ms, bg -39.1 dB, real to 289 ms, len 656 ms, rel 0.6 dB REAL
  medium rr1: t=234.99 s, gap 174 ms, bg -15.5 dB, real to 169 ms, len 734 ms, rel -3.0 dB REAL
  medium rr2: t=243.73 s, gap 253 ms, bg -22.6 dB, real to 109 ms, len 734 ms, rel -8.3 dB REAL
  medium rr3: t=122.06 s, gap 705 ms, bg -25.4 dB, real to 194 ms, len 750 ms, rel -6.8 dB REAL
  medium rr4: t=199.75 s, gap 200 ms, bg -26.2 dB, real to 164 ms, len 704 ms, rel -7.7 dB REAL
  soft rr1: t=209.5 s, gap 1276 ms, bg -41.2 dB, real to 503 ms, len 766 ms, rel -12 dB ESTIMATE
  soft rr2: t=213.05 s, gap 553 ms, bg -46.7 dB, real to 264 ms, len 740 ms, rel -12 dB ESTIMATE
  soft rr3: t=34.79 s, gap 421 ms, bg -38.7 dB, real to 399 ms, len 729 ms, rel -12 dB ESTIMATE
  soft rr4: t=22.23 s, gap 402 ms, bg -40.4 dB, real to 384 ms, len 719 ms, rel -12 dB ESTIMATE
  ghost rr1: t=115.92 s, gap 400 ms, bg -40.1 dB, real to 389 ms, len 684 ms, rel -20 dB ESTIMATE
  ghost rr2: t=104.5 s, gap 400 ms, bg -45.1 dB, real to 389 ms, len 774 ms, rel -20 dB ESTIMATE
  ghost rr3: t=56.5 s, gap 397 ms, bg -40.5 dB, real to 379 ms, len 749 ms, rel -20 dB ESTIMATE
  ghost rr4: t=26.8 s, gap 393 ms, bg -38.8 dB, real to 379 ms, len 749 ms, rel -20 dB ESTIMATE