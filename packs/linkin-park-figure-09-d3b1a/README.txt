ZC SNARE EXTRACT v3.0 - Linkin Park - "Figure.09" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 132 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.753,
    hit-to-hit level SD 3.47 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -7.7  vs full drum stem -7.6  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.5  vs drum stem -15.2
    Hit-locked energy left in the separator residual (snare that got dropped): -56.7 dBFS at 0-5 ms vs -8.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -3.5, '150-300': -0.1, '300-600': -0.1, '600-1200': 0.0, '1200-2500': -0.1, '2500-5000': -0.8, '5000-8000': -2.5, '8000-12000': -6.4, '12000-16000': -11.1}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [5.96, 1.27, 3.06, 1.47] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-133.0, -101.0, -98.0, -164.0, -203.0] dB/s  ->  T60 [0.45, 0.6, 0.61, 0.36, 0.3] s
  early part (60-150 ms, body + early reflections): [None, -101.0, -99.0, -164.0, -203.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -6.9, '30ms': -13.0, '50ms': -16.7, '100ms': -23.4, '150ms': -25.1, '200ms': -29.1}
  Snare-stem noise floor between hits: -95.4 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 2/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_linkin-park-figure-09-d3b1a_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=30.08 s, gap 1216 ms, bg -40.4 dB, real to 94 ms, len 475 ms, rel -0.2 dB REAL
  hard rr2: t=37.42 s, gap 1063 ms, bg -42.4 dB, real to 119 ms, len 470 ms, rel 0.6 dB REAL
  hard rr3: t=42.32 s, gap 1217 ms, bg -38.7 dB, real to 134 ms, len 485 ms, rel -1.1 dB REAL
  hard rr4: t=36.2 s, gap 1216 ms, bg -38.9 dB, real to 104 ms, len 510 ms, rel 0.0 dB REAL
  medium rr1: t=23.96 s, gap 143 ms, bg -36.5 dB, real to 59 ms, len 440 ms, rel -5.9 dB REAL
  medium rr2: t=63.13 s, gap 318 ms, bg -40.0 dB, real to 164 ms, len 420 ms, rel -4.0 dB REAL
  medium rr3: t=153.72 s, gap 605 ms, bg -40.3 dB, real to 199 ms, len 469 ms, rel -3.4 dB REAL
  medium rr4: t=55.79 s, gap 1216 ms, bg -43.0 dB, real to 109 ms, len 479 ms, rel -3.4 dB REAL
  soft rr1: t=94.96 s, gap 454 ms, bg -26.3 dB, real to 59 ms, len 422 ms, rel -10.7 dB REAL
  soft rr2: t=96.18 s, gap 148 ms, bg -39.5 dB, real to 59 ms, len 439 ms, rel -16.1 dB REAL
  soft rr3: t=34.97 s, gap 1217 ms, bg -35.6 dB, real to 139 ms, len 486 ms, rel -12 dB ESTIMATE
  soft rr4: t=83.94 s, gap 1218 ms, bg -35.6 dB, real to 139 ms, len 523 ms, rel -12 dB ESTIMATE
  ghost rr1: t=174.53 s, gap 1216 ms, bg -38.1 dB, real to 299 ms, len 544 ms, rel -20 dB ESTIMATE
  ghost rr2: t=180.65 s, gap 533 ms, bg -39.5 dB, real to 199 ms, len 495 ms, rel -20 dB ESTIMATE
  ghost rr3: t=33.75 s, gap 654 ms, bg -33.1 dB, real to 259 ms, len 511 ms, rel -20 dB ESTIMATE
  ghost rr4: t=118.22 s, gap 1216 ms, bg -34.7 dB, real to 224 ms, len 505 ms, rel -20 dB ESTIMATE