ZC SNARE EXTRACT v3.0 - Linkin Park - "Figure.09" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 135 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.762,
    hit-to-hit level SD 3.53 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -7.6  vs full drum stem -7.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.3  vs drum stem -15.0
    Hit-locked energy left in the separator residual (snare that got dropped): -56.8 dBFS at 0-5 ms vs -8.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -4.6, '150-300': -0.2, '300-600': -0.1, '600-1200': 0.0, '1200-2500': -0.1, '2500-5000': -0.9, '5000-8000': -2.6, '8000-12000': -6.6, '12000-16000': -11.6}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.06, 3.67, 3.22, 18.16] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-132.0, -100.0, -109.0, -155.0, -181.0] dB/s  ->  T60 [0.45, 0.6, 0.55, 0.39, 0.33] s
  early part (60-150 ms, body + early reflections): [None, -100.0, -96.0, -155.0, -181.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -7.0, '30ms': -13.4, '50ms': -16.9, '100ms': -23.4, '150ms': -25.3, '200ms': -30.2}
  Snare-stem noise floor between hits: -94.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 1/4, ghost 1/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_linkin-park-figure-09-d3b1a_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=42.32 s, gap 1217 ms, bg -40.5 dB, real to 264 ms, len 694 ms, rel -0.8 dB REAL
  hard rr2: t=34.97 s, gap 1050 ms, bg -40.4 dB, real to 209 ms, len 675 ms, rel -0.2 dB REAL
  hard rr3: t=77.82 s, gap 1214 ms, bg -42.1 dB, real to 149 ms, len 560 ms, rel -0.9 dB REAL
  hard rr4: t=19.06 s, gap 605 ms, bg -43.1 dB, real to 244 ms, len 585 ms, rel -0.3 dB REAL
  medium rr1: t=63.13 s, gap 318 ms, bg -38.2 dB, real to 149 ms, len 620 ms, rel -4.7 dB REAL
  medium rr2: t=55.79 s, gap 304 ms, bg -47.0 dB, real to 149 ms, len 424 ms, rel -3.5 dB REAL
  medium rr3: t=150.04 s, gap 914 ms, bg -41.6 dB, real to 149 ms, len 519 ms, rel -9.3 dB REAL
  medium rr4: t=64.36 s, gap 1215 ms, bg -35.9 dB, real to 149 ms, len 594 ms, rel -7.2 dB REAL
  soft rr1: t=94.96 s, gap 449 ms, bg -25.4 dB, real to 149 ms, len 225 ms, rel -15.9 dB REAL
  soft rr2: t=186.77 s, gap 1214 ms, bg -39.5 dB, real to 149 ms, len 540 ms, rel -12 dB ESTIMATE
  soft rr3: t=33.75 s, gap 669 ms, bg -32.4 dB, real to 149 ms, len 580 ms, rel -12 dB ESTIMATE
  soft rr4: t=141.48 s, gap 628 ms, bg -36.7 dB, real to 154 ms, len 605 ms, rel -12 dB ESTIMATE
  ghost rr1: t=93.73 s, gap 452 ms, bg -30.6 dB, real to 149 ms, len 275 ms, rel -18.3 dB REAL
  ghost rr2: t=174.53 s, gap 1216 ms, bg -37.3 dB, real to 149 ms, len 579 ms, rel -20 dB ESTIMATE
  ghost rr3: t=118.22 s, gap 899 ms, bg -34.6 dB, real to 159 ms, len 600 ms, rel -20 dB ESTIMATE
  ghost rr4: t=38.65 s, gap 654 ms, bg -38.9 dB, real to 174 ms, len 619 ms, rel -20 dB ESTIMATE