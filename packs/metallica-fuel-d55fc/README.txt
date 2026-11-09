ZC SNARE EXTRACT v3.0 - Metallica - "Fuel" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 283 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.678,
    hit-to-hit level SD 2.17 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -11.7  vs full drum stem -11.0  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.1  vs drum stem -13.0
    Hit-locked energy left in the separator residual (snare that got dropped): -56.7 dBFS at 0-5 ms vs -16.5 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -16.9, '150-300': -0.2, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.3, '2500-5000': -1.2, '5000-8000': -2.6, '8000-12000': -4.7, '12000-16000': -7.6}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.13, 5.71, 4.51, 5.15] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-83.0, -85.0, -81.0, -69.0, -133.0] dB/s  ->  T60 [0.72, 0.71, 0.74, 0.87, 0.45] s
  early part (60-150 ms, body + early reflections): [None, -102.0, -105.0, -133.0, -157.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.7, '30ms': -7.0, '50ms': -9.5, '100ms': -16.7, '150ms': -21.5, '200ms': -23.3}
  Snare-stem noise floor between hits: -78.6 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_metallica-fuel-d55fc_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=90.08 s, gap 1117 ms, bg -35.6 dB, real to 528 ms, len 645 ms, rel 0.7 dB REAL
  hard rr2: t=263.36 s, gap 553 ms, bg -39.4 dB, real to 533 ms, len 620 ms, rel 1.9 dB REAL
  hard rr3: t=114.06 s, gap 563 ms, bg -35.5 dB, real to 334 ms, len 625 ms, rel -0.0 dB REAL
  hard rr4: t=262.22 s, gap 559 ms, bg -36.1 dB, real to 184 ms, len 626 ms, rel 1.3 dB REAL
  medium rr1: t=71.25 s, gap 143 ms, bg -25.6 dB, real to 129 ms, len 559 ms, rel -3.2 dB REAL
  medium rr2: t=249.22 s, gap 139 ms, bg -25.6 dB, real to 79 ms, len 516 ms, rel -3.7 dB REAL
  medium rr3: t=241.0 s, gap 137 ms, bg -42.8 dB, real to 119 ms, len 578 ms, rel -4.2 dB REAL
  medium rr4: t=212.25 s, gap 256 ms, bg -33.9 dB, real to 244 ms, len 590 ms, rel -3.1 dB REAL
  soft rr1: t=213.23 s, gap 162 ms, bg -11.2 dB, real to 79 ms, len 597 ms, rel -12.7 dB REAL
  soft rr2: t=84.77 s, gap 558 ms, bg -43.5 dB, real to 359 ms, len 589 ms, rel -12 dB ESTIMATE
  soft rr3: t=88.95 s, gap 551 ms, bg -34.5 dB, real to 234 ms, len 631 ms, rel -12 dB ESTIMATE
  soft rr4: t=104.81 s, gap 1126 ms, bg -31.3 dB, real to 174 ms, len 635 ms, rel -12 dB ESTIMATE
  ghost rr1: t=129.51 s, gap 1093 ms, bg -43.8 dB, real to 119 ms, len 634 ms, rel -20 dB ESTIMATE
  ghost rr2: t=12.96 s, gap 558 ms, bg -35.6 dB, real to 304 ms, len 635 ms, rel -20 dB ESTIMATE
  ghost rr3: t=101.41 s, gap 554 ms, bg -35.2 dB, real to 204 ms, len 655 ms, rel -20 dB ESTIMATE
  ghost rr4: t=41.15 s, gap 573 ms, bg -35.9 dB, real to 284 ms, len 635 ms, rel -20 dB ESTIMATE