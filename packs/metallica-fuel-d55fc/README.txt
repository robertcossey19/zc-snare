ZC SNARE EXTRACT v3.0 - Metallica - "Fuel" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 291 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.675,
    hit-to-hit level SD 2.79 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -11.8  vs full drum stem -11.1  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.3  vs drum stem -13.1
    Hit-locked energy left in the separator residual (snare that got dropped): -55.6 dBFS at 0-5 ms vs -17.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -17.8, '150-300': -0.1, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.3, '2500-5000': -1.2, '5000-8000': -2.5, '8000-12000': -4.7, '12000-16000': -7.5}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [5.74, 5.6, 3.15, 5.15] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-70.0, -67.0, -74.0, -66.0, -142.0] dB/s  ->  T60 [0.86, 0.9, 0.82, 0.9, 0.42] s
  early part (60-150 ms, body + early reflections): [None, -101.0, -108.0, -131.0, -147.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.7, '30ms': -7.1, '50ms': -9.5, '100ms': -16.9, '150ms': -21.4, '200ms': -23.2}
  Snare-stem noise floor between hits: -78.9 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 2/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_metallica-fuel-d55fc_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=263.36 s, gap 553 ms, bg -40.7 dB, real to 264 ms, len 1282 ms, rel 2.0 dB REAL
  hard rr2: t=155.29 s, gap 1120 ms, bg -40.3 dB, real to 369 ms, len 915 ms, rel 1.8 dB REAL
  hard rr3: t=90.08 s, gap 1117 ms, bg -35.0 dB, real to 254 ms, len 1004 ms, rel 0.7 dB REAL
  hard rr4: t=262.22 s, gap 559 ms, bg -34.5 dB, real to 244 ms, len 1282 ms, rel 1.4 dB REAL
  medium rr1: t=250.33 s, gap 136 ms, bg -20.1 dB, real to 121 ms, len 1034 ms, rel -3.3 dB REAL
  medium rr2: t=205.45 s, gap 131 ms, bg -36.5 dB, real to 116 ms, len 909 ms, rel -5.4 dB REAL
  medium rr3: t=249.22 s, gap 139 ms, bg -25.7 dB, real to 124 ms, len 1035 ms, rel -3.9 dB REAL
  medium rr4: t=70.27 s, gap 143 ms, bg -34.3 dB, real to 128 ms, len 973 ms, rel -6.6 dB REAL
  soft rr1: t=51.77 s, gap 159 ms, bg -39.3 dB, real to 144 ms, len 642 ms, rel -13.8 dB REAL
  soft rr2: t=128.27 s, gap 1229 ms, bg -28.8 dB, real to 149 ms, len 751 ms, rel -15.4 dB REAL
  soft rr3: t=41.15 s, gap 838 ms, bg -36.5 dB, real to 234 ms, len 884 ms, rel -12 dB ESTIMATE
  soft rr4: t=261.08 s, gap 1129 ms, bg -33.9 dB, real to 209 ms, len 1281 ms, rel -12 dB ESTIMATE
  ghost rr1: t=104.81 s, gap 1126 ms, bg -31.5 dB, real to 249 ms, len 1281 ms, rel -20 dB ESTIMATE
  ghost rr2: t=101.41 s, gap 554 ms, bg -33.3 dB, real to 274 ms, len 1281 ms, rel -20 dB ESTIMATE
  ghost rr3: t=11.83 s, gap 561 ms, bg -35.2 dB, real to 229 ms, len 959 ms, rel -20 dB ESTIMATE
  ghost rr4: t=181.01 s, gap 1102 ms, bg -32.9 dB, real to 209 ms, len 1281 ms, rel -20 dB ESTIMATE