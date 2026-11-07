ZC SNARE EXTRACT v3.0 - Metallica - "Fuel" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 294 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.683,
    hit-to-hit level SD 2.82 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -12.1  vs full drum stem -11.3  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.5  vs drum stem -13.4
    Hit-locked energy left in the separator residual (snare that got dropped): -55.0 dBFS at 0-5 ms vs -16.7 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -17.1, '150-300': -0.2, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.3, '2500-5000': -1.1, '5000-8000': -2.5, '8000-12000': -4.7, '12000-16000': -7.5}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [5.76, 3.15, 5.15, 5.37] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-73.0, -70.0, -76.0, -68.0, -143.0] dB/s  ->  T60 [0.82, 0.86, 0.79, 0.89, 0.42] s
  early part (60-150 ms, body + early reflections): [None, -99.0, -103.0, -126.0, -143.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.6, '30ms': -7.0, '50ms': -9.5, '100ms': -17.1, '150ms': -21.6, '200ms': -23.5}
  Snare-stem noise floor between hits: -79.0 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 1/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_metallica-fuel-d55fc_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=263.35 s, gap 555 ms, bg -39.4 dB, real to 264 ms, len 865 ms, rel 1.8 dB REAL
  hard rr2: t=90.08 s, gap 1117 ms, bg -35.5 dB, real to 254 ms, len 989 ms, rel 0.7 dB REAL
  hard rr3: t=262.22 s, gap 559 ms, bg -37.7 dB, real to 244 ms, len 895 ms, rel 1.2 dB REAL
  hard rr4: t=104.81 s, gap 1126 ms, bg -33.3 dB, real to 254 ms, len 964 ms, rel 0.7 dB REAL
  medium rr1: t=205.45 s, gap 131 ms, bg -36.7 dB, real to 116 ms, len 844 ms, rel -5.3 dB REAL
  medium rr2: t=87.42 s, gap 141 ms, bg -37.0 dB, real to 126 ms, len 975 ms, rel -3.2 dB REAL
  medium rr3: t=250.74 s, gap 141 ms, bg -20.2 dB, real to 126 ms, len 863 ms, rel -3.8 dB REAL
  medium rr4: t=249.08 s, gap 136 ms, bg -19.2 dB, real to 121 ms, len 864 ms, rel -8.3 dB REAL
  soft rr1: t=41.15 s, gap 838 ms, bg -37.6 dB, real to 229 ms, len 869 ms, rel -12 dB ESTIMATE
  soft rr2: t=114.06 s, gap 561 ms, bg -35.2 dB, real to 219 ms, len 849 ms, rel -12 dB ESTIMATE
  soft rr3: t=155.29 s, gap 1120 ms, bg -36.7 dB, real to 279 ms, len 969 ms, rel -12 dB ESTIMATE
  soft rr4: t=12.96 s, gap 558 ms, bg -37.2 dB, real to 224 ms, len 909 ms, rel -12 dB ESTIMATE
  ghost rr1: t=51.77 s, gap 159 ms, bg -26.7 dB, real to 144 ms, len 765 ms, rel -18.0 dB REAL
  ghost rr2: t=11.83 s, gap 561 ms, bg -36.8 dB, real to 234 ms, len 884 ms, rel -20 dB ESTIMATE
  ghost rr3: t=154.17 s, gap 538 ms, bg -35.6 dB, real to 359 ms, len 984 ms, rel -20 dB ESTIMATE
  ghost rr4: t=261.08 s, gap 1130 ms, bg -34.0 dB, real to 154 ms, len 780 ms, rel -20 dB ESTIMATE