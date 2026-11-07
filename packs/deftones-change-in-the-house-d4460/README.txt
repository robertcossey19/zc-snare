ZC SNARE EXTRACT v3.0 - Deftones - "Change (In the House of Flies)" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 149 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.703,
    hit-to-hit level SD 2.43 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.5  vs full drum stem -10.1  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -17.6  vs drum stem -16.6
    Hit-locked energy left in the separator residual (snare that got dropped): -55.1 dBFS at 0-5 ms vs -13.5 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -2.3, '150-300': -0.1, '300-600': -0.3, '600-1200': -0.1, '1200-2500': -0.6, '2500-5000': -4.0, '5000-8000': -5.9, '8000-12000': -10.9, '12000-16000': -17.8}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.61, 4.69, 1.27, 4.35] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-118.0, -118.0, -118.0, -114.0, -144.0] dB/s  ->  T60 [0.51, 0.51, 0.51, 0.52, 0.42] s
  early part (60-150 ms, body + early reflections): [None, None, -118.0, -114.0, -144.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -5.9, '30ms': -14.7, '50ms': -20.2, '100ms': -24.4}
  Snare-stem noise floor between hits: -97.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_deftones-change-in-the-house-d4460_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=81.6 s, gap 852 ms, bg -37.2 dB, real to 169 ms, len 602 ms, rel 0.4 dB REAL
  hard rr2: t=88.61 s, gap 1737 ms, bg -31.1 dB, real to 149 ms, len 562 ms, rel 1.0 dB REAL
  hard rr3: t=90.36 s, gap 801 ms, bg -31.2 dB, real to 149 ms, len 492 ms, rel 1.9 dB REAL
  hard rr4: t=58.93 s, gap 1075 ms, bg -36.2 dB, real to 149 ms, len 741 ms, rel -0.6 dB REAL
  medium rr1: t=64.11 s, gap 220 ms, bg -38.2 dB, real to 149 ms, len 1284 ms, rel -3.0 dB REAL
  medium rr2: t=113.06 s, gap 219 ms, bg -38.8 dB, real to 149 ms, len 690 ms, rel -3.5 dB REAL
  medium rr3: t=246.54 s, gap 292 ms, bg -32.7 dB, real to 149 ms, len 703 ms, rel -4.0 dB REAL
  medium rr4: t=127.05 s, gap 195 ms, bg -32.8 dB, real to 149 ms, len 433 ms, rel -7.2 dB REAL
  soft rr1: t=86.19 s, gap 227 ms, bg -46.5 dB, real to 149 ms, len 368 ms, rel -14.5 dB REAL
  soft rr2: t=65.87 s, gap 637 ms, bg -34.3 dB, real to 149 ms, len 511 ms, rel -12 dB ESTIMATE
  soft rr3: t=92.09 s, gap 472 ms, bg -35.0 dB, real to 149 ms, len 459 ms, rel -12 dB ESTIMATE
  soft rr4: t=207.91 s, gap 1481 ms, bg -34.7 dB, real to 149 ms, len 406 ms, rel -12 dB ESTIMATE
  ghost rr1: t=37.96 s, gap 768 ms, bg -30.3 dB, real to 149 ms, len 556 ms, rel -20 dB ESTIMATE
  ghost rr2: t=79.86 s, gap 1731 ms, bg -25.5 dB, real to 149 ms, len 490 ms, rel -20 dB ESTIMATE
  ghost rr3: t=62.38 s, gap 628 ms, bg -34.5 dB, real to 149 ms, len 1225 ms, rel -20 dB ESTIMATE
  ghost rr4: t=45.03 s, gap 1758 ms, bg -33.0 dB, real to 149 ms, len 606 ms, rel -20 dB ESTIMATE