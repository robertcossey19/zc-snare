ZC SNARE EXTRACT v3.0 - Deftones - "Change (In the House of Flies)" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 147 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.689,
    hit-to-hit level SD 3.75 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.5  vs full drum stem -10.2  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -17.5  vs drum stem -16.5
    Hit-locked energy left in the separator residual (snare that got dropped): -56.8 dBFS at 0-5 ms vs -13.0 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -3.4, '150-300': -0.1, '300-600': -0.3, '600-1200': -0.1, '1200-2500': -0.6, '2500-5000': -3.8, '5000-8000': -5.7, '8000-12000': -10.6, '12000-16000': -17.7}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [6.1, 5.24, 4.15, 5.56] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-128.0, -128.0, -128.0, -128.0, -128.0] dB/s  ->  T60 [0.47, 0.47, 0.47, 0.47, 0.47] s
  early part (60-150 ms, body + early reflections): [None, None, -128.0, None, None] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -5.8, '30ms': -14.6, '50ms': -20.1, '100ms': -24.7}
  Snare-stem noise floor between hits: -97.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_deftones-change-in-the-house-d4460_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=228.19 s, gap 701 ms, bg -35.4 dB, real to 149 ms, len 427 ms, rel -1.7 dB REAL
  hard rr2: t=222.95 s, gap 180 ms, bg -33.7 dB, real to 149 ms, len 412 ms, rel -2.2 dB REAL
  hard rr3: t=224.63 s, gap 875 ms, bg -33.4 dB, real to 149 ms, len 337 ms, rel -1.7 dB REAL
  hard rr4: t=231.37 s, gap 215 ms, bg -30.0 dB, real to 149 ms, len 477 ms, rel -0.1 dB REAL
  medium rr1: t=211.81 s, gap 981 ms, bg -19.8 dB, real to 149 ms, len 472 ms, rel -8.0 dB REAL
  medium rr2: t=227.45 s, gap 524 ms, bg -24.9 dB, real to 149 ms, len 400 ms, rel -4.6 dB REAL
  medium rr3: t=64.11 s, gap 220 ms, bg -40.2 dB, real to 149 ms, len 337 ms, rel -3.4 dB REAL
  medium rr4: t=246.54 s, gap 205 ms, bg -31.8 dB, real to 149 ms, len 386 ms, rel -4.4 dB REAL
  soft rr1: t=233.05 s, gap 819 ms, bg -38.3 dB, real to 149 ms, len 476 ms, rel -12 dB ESTIMATE
  soft rr2: t=234.71 s, gap 1696 ms, bg -38.2 dB, real to 149 ms, len 437 ms, rel -12 dB ESTIMATE
  soft rr3: t=236.41 s, gap 187 ms, bg -36.9 dB, real to 149 ms, len 481 ms, rel -12 dB ESTIMATE
  soft rr4: t=238.94 s, gap 333 ms, bg -30.4 dB, real to 149 ms, len 497 ms, rel -12 dB ESTIMATE
  ghost rr1: t=243.16 s, gap 1055 ms, bg -32.8 dB, real to 149 ms, len 463 ms, rel -20 dB ESTIMATE
  ghost rr2: t=244.85 s, gap 653 ms, bg -27.6 dB, real to 149 ms, len 441 ms, rel -20 dB ESTIMATE
  ghost rr3: t=206.03 s, gap 1041 ms, bg -29.1 dB, real to 149 ms, len 408 ms, rel -20 dB ESTIMATE
  ghost rr4: t=187.22 s, gap 237 ms, bg -36.0 dB, real to 149 ms, len 452 ms, rel -20 dB ESTIMATE