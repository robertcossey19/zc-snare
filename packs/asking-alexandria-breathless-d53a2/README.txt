ZC SNARE EXTRACT v3.0 - Asking Alexandria - "Breathless" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 297 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.909,
    hit-to-hit level SD 2.41 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -8.7  vs full drum stem -8.2  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -12.5  vs drum stem -9.7
    Hit-locked energy left in the separator residual (snare that got dropped): -43.9 dBFS at 0-5 ms vs -8.8 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -28.7, '150-300': -0.1, '300-600': -0.6, '600-1200': -1.1, '1200-2500': -1.9, '2500-5000': -3.5, '5000-8000': -3.6, '8000-12000': -5.6, '12000-16000': -7.4}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [9.34, 1.79, 4.67, 3.85] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-131.0, -135.0, -145.0, -101.0, -127.0] dB/s  ->  T60 [0.46, 0.45, 0.41, 0.59, 0.47] s
  early part (60-150 ms, body + early reflections): [None, -135.0, -94.0, -101.0, -127.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.9, '30ms': -16.3, '50ms': -14.3, '100ms': -20.7, '150ms': -27.2, '200ms': -31.2}
  Snare-stem noise floor between hits: -84.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 3/4, soft 0/4, ghost 1/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_asking-alexandria-breathless-d53a2_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=201.39 s, gap 742 ms, bg -42.7 dB, real to 204 ms, len 626 ms, rel -0.5 dB REAL
  hard rr2: t=195.39 s, gap 561 ms, bg -39.7 dB, real to 194 ms, len 555 ms, rel 0.0 dB REAL
  hard rr3: t=58.63 s, gap 557 ms, bg -43.2 dB, real to 189 ms, len 546 ms, rel -1.8 dB REAL
  hard rr4: t=234.96 s, gap 9000 ms, bg -26.6 dB, real to 149 ms, len 660 ms, rel -0.4 dB REAL
  medium rr1: t=160.33 s, gap 193 ms, bg -39.3 dB, real to 178 ms, len 534 ms, rel -3.1 dB REAL
  medium rr2: t=229.89 s, gap 161 ms, bg -42.4 dB, real to 146 ms, len 590 ms, rel -3.2 dB REAL
  medium rr3: t=92.27 s, gap 264 ms, bg -42.8 dB, real to 154 ms, len 534 ms, rel -5.1 dB REAL
  medium rr4: t=202.89 s, gap 922 ms, bg -36.9 dB, real to 194 ms, len 581 ms, rel -6 dB ESTIMATE
  soft rr1: t=138.02 s, gap 741 ms, bg -40.2 dB, real to 214 ms, len 590 ms, rel -12 dB ESTIMATE
  soft rr2: t=162.21 s, gap 369 ms, bg -36.1 dB, real to 219 ms, len 630 ms, rel -12 dB ESTIMATE
  soft rr3: t=103.59 s, gap 1420 ms, bg -20.8 dB, real to 149 ms, len 674 ms, rel -12 dB ESTIMATE
  soft rr4: t=232.89 s, gap 1496 ms, bg -41.1 dB, real to 234 ms, len 699 ms, rel -12 dB ESTIMATE
  ghost rr1: t=218.87 s, gap 137 ms, bg -27.9 dB, real to 122 ms, len 548 ms, rel -24.1 dB REAL
  ghost rr2: t=123.39 s, gap 1492 ms, bg -40.7 dB, real to 174 ms, len 545 ms, rel -20 dB ESTIMATE
  ghost rr3: t=31.89 s, gap 406 ms, bg -41.7 dB, real to 244 ms, len 655 ms, rel -20 dB ESTIMATE
  ghost rr4: t=136.14 s, gap 366 ms, bg -43.8 dB, real to 279 ms, len 590 ms, rel -20 dB ESTIMATE