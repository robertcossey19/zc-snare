ZC SNARE EXTRACT v3.0 - Nickelback - "San Quentin" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 213 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.952,
    hit-to-hit level SD 2.34 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.8  vs full drum stem -8.4  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.2  vs drum stem -10.0
    Hit-locked energy left in the separator residual (snare that got dropped): -31.3 dBFS at 0-5 ms vs -10.4 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -33.2, '150-300': -0.3, '300-600': -1.2, '600-1200': -1.4, '1200-2500': -2.2, '2500-5000': -5.4, '5000-8000': -8.9, '8000-12000': -8.6, '12000-16000': -12.0}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.2, 3.81, 2.95, 3.02] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-93.0, -134.0, -98.0, -79.0, -88.0] dB/s  ->  T60 [0.64, 0.45, 0.61, 0.76, 0.68] s
  early part (60-150 ms, body + early reflections): [None, -57.0, -53.0, -55.0, -73.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.1, '30ms': -16.3, '50ms': -15.2, '100ms': -10.6, '150ms': -12.7, '200ms': -20.1, '300ms': -26.6}
  Snare-stem noise floor between hits: -86.1 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_nickelback-san-quentin-offic-39akj_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=90.79 s, gap 718 ms, bg -38.8 dB, real to 144 ms, len 1024 ms, rel 0.3 dB REAL
  hard rr2: t=151.04 s, gap 1675 ms, bg -35.3 dB, real to 149 ms, len 1008 ms, rel -1.4 dB REAL
  hard rr3: t=170.62 s, gap 581 ms, bg -41.9 dB, real to 109 ms, len 994 ms, rel 1.3 dB REAL
  hard rr4: t=129.5 s, gap 476 ms, bg -38.9 dB, real to 144 ms, len 985 ms, rel -0.5 dB REAL
  medium rr1: t=18.44 s, gap 306 ms, bg -19.4 dB, real to 299 ms, len 993 ms, rel -4.1 dB REAL
  medium rr2: t=26.92 s, gap 2410 ms, bg -20.2 dB, real to 229 ms, len 1008 ms, rel -3.1 dB REAL
  medium rr3: t=15.04 s, gap 244 ms, bg -38.7 dB, real to 234 ms, len 1025 ms, rel -7.5 dB REAL
  medium rr4: t=25.46 s, gap 123 ms, bg -19.8 dB, real to 154 ms, len 1023 ms, rel -3.8 dB REAL
  soft rr1: t=208.85 s, gap 476 ms, bg -37.4 dB, real to 144 ms, len 954 ms, rel -12 dB ESTIMATE
  soft rr2: t=226.75 s, gap 552 ms, bg -40.9 dB, real to 289 ms, len 959 ms, rel -12 dB ESTIMATE
  soft rr3: t=160.94 s, gap 959 ms, bg -34.7 dB, real to 438 ms, len 1028 ms, rel -12 dB ESTIMATE
  soft rr4: t=131.91 s, gap 404 ms, bg -38.4 dB, real to 109 ms, len 998 ms, rel -12 dB ESTIMATE
  ghost rr1: t=34.17 s, gap 483 ms, bg -41.2 dB, real to 139 ms, len 981 ms, rel -20 dB ESTIMATE
  ghost rr2: t=130.22 s, gap 354 ms, bg -38.6 dB, real to 89 ms, len 979 ms, rel -20 dB ESTIMATE
  ghost rr3: t=228.21 s, gap 239 ms, bg -41.4 dB, real to 224 ms, len 1018 ms, rel -20 dB ESTIMATE
  ghost rr4: t=204.25 s, gap 293 ms, bg -42.4 dB, real to 119 ms, len 1024 ms, rel -20 dB ESTIMATE