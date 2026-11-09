ZC SNARE EXTRACT v3.0 - Metallica - "Enter Sandman" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 191 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.596,
    hit-to-hit level SD 5.56 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.9  vs full drum stem -10.1  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.8  vs drum stem -14.5
    Hit-locked energy left in the separator residual (snare that got dropped): -44.9 dBFS at 0-5 ms vs -15.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -7.7, '150-300': -0.2, '300-600': -0.2, '600-1200': -0.4, '1200-2500': -0.6, '2500-5000': -2.7, '5000-8000': -3.8, '8000-12000': -6.6, '12000-16000': -10.4}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [1.9, 5.4, 4.58, 4.4] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-96.0, -97.0, -108.0, -100.0, -129.0] dB/s  ->  T60 [0.62, 0.62, 0.56, 0.6, 0.46] s
  early part (60-150 ms, body + early reflections): [-96.0, -75.0, -75.0, -85.0, -116.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.3, '30ms': -9.3, '50ms': -13.2, '100ms': -18.8, '150ms': -21.5, '200ms': -24.3, '300ms': -28.4}
  Snare-stem noise floor between hits: -96.2 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 1/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_metallica-enter-sandman-d491e_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=76.07 s, gap 950 ms, bg -39.7 dB, real to 114 ms, len 550 ms, rel -0.8 dB REAL
  hard rr2: t=150.28 s, gap 943 ms, bg -39.9 dB, real to 269 ms, len 535 ms, rel 0.1 dB REAL
  hard rr3: t=187.85 s, gap 952 ms, bg -35.9 dB, real to 458 ms, len 525 ms, rel -0.1 dB REAL
  hard rr4: t=135.84 s, gap 945 ms, bg -35.6 dB, real to 209 ms, len 529 ms, rel -1.9 dB REAL
  medium rr1: t=134.89 s, gap 181 ms, bg -33.9 dB, real to 109 ms, len 504 ms, rel -3.5 dB REAL
  medium rr2: t=144.5 s, gap 234 ms, bg -32.3 dB, real to 94 ms, len 491 ms, rel -6.3 dB REAL
  medium rr3: t=52.9 s, gap 230 ms, bg -36.2 dB, real to 224 ms, len 485 ms, rel -5.6 dB REAL
  medium rr4: t=53.87 s, gap 239 ms, bg -28.4 dB, real to 229 ms, len 484 ms, rel -3.4 dB REAL
  soft rr1: t=110.75 s, gap 480 ms, bg -40.9 dB, real to 419 ms, len 534 ms, rel -12 dB ESTIMATE
  soft rr2: t=166.64 s, gap 968 ms, bg -37.3 dB, real to 209 ms, len 520 ms, rel -12 dB ESTIMATE
  soft rr3: t=99.41 s, gap 717 ms, bg -36.2 dB, real to 483 ms, len 534 ms, rel -12 dB ESTIMATE
  soft rr4: t=242.5 s, gap 716 ms, bg -37.0 dB, real to 299 ms, len 529 ms, rel -12 dB ESTIMATE
  ghost rr1: t=208.67 s, gap 452 ms, bg -17.2 dB, real to 234 ms, len 545 ms, rel -21.3 dB REAL
  ghost rr2: t=183.98 s, gap 966 ms, bg -36.5 dB, real to 448 ms, len 539 ms, rel -20 dB ESTIMATE
  ghost rr3: t=191.68 s, gap 951 ms, bg -38.5 dB, real to 254 ms, len 531 ms, rel -20 dB ESTIMATE
  ghost rr4: t=66.43 s, gap 488 ms, bg -38.8 dB, real to 229 ms, len 534 ms, rel -20 dB ESTIMATE