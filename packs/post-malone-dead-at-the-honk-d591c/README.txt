ZC SNARE EXTRACT v3.0 - Post Malone - "Dead at the Honky Tonk" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 115 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.716,
    hit-to-hit level SD 15.29 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -12.7  vs full drum stem -11.7  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.2  vs drum stem -7.9
    Hit-locked energy left in the separator residual (snare that got dropped): -44.4 dBFS at 0-5 ms vs -20.5 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -25.4, '150-300': -2.9, '300-600': -4.5, '600-1200': -3.9, '1200-2500': -3.5, '2500-5000': -2.0, '5000-8000': -1.5, '8000-12000': -1.5, '12000-16000': -2.3}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [5.17, 4.08, 2.74, 4.1] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-149.0, -62.0, -37.0, -104.0, -129.0] dB/s  ->  T60 [0.4, 0.97, 1.61, 0.58, 0.47] s
  early part (60-150 ms, body + early reflections): [-149.0, -130.0, -37.0, -104.0, -129.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.3, '30ms': -4.3, '50ms': -7.4, '100ms': -14.9, '150ms': -18.4}
  Snare-stem noise floor between hits: -91.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 1/4, ghost 2/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_post-malone-dead-at-the-honk-d591c_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=116.63 s, gap 720 ms, bg -36.0 dB, real to 179 ms, len 1028 ms, rel -0.8 dB REAL
  hard rr2: t=126.75 s, gap 1437 ms, bg -36.8 dB, real to 314 ms, len 1139 ms, rel -1.0 dB REAL
  hard rr3: t=177.35 s, gap 1171 ms, bg -34.4 dB, real to 269 ms, len 1178 ms, rel 1.3 dB REAL
  hard rr4: t=92.05 s, gap 1308 ms, bg -33.4 dB, real to 149 ms, len 976 ms, rel -2.5 dB REAL
  medium rr1: t=170.71 s, gap 408 ms, bg -46.9 dB, real to 204 ms, len 493 ms, rel -7.8 dB REAL
  medium rr2: t=53.6 s, gap 351 ms, bg -30.7 dB, real to 149 ms, len 980 ms, rel -6.5 dB REAL
  medium rr3: t=55.91 s, gap 644 ms, bg -28.6 dB, real to 149 ms, len 975 ms, rel -7.4 dB REAL
  medium rr4: t=122.41 s, gap 230 ms, bg -26.9 dB, real to 149 ms, len 1204 ms, rel -4.1 dB REAL
  soft rr1: t=55.05 s, gap 129 ms, bg -36.7 dB, real to 114 ms, len 1066 ms, rel -10.3 dB REAL
  soft rr2: t=161.45 s, gap 1438 ms, bg -31.6 dB, real to 164 ms, len 1114 ms, rel -12 dB ESTIMATE
  soft rr3: t=86.27 s, gap 1803 ms, bg -38.6 dB, real to 169 ms, len 953 ms, rel -12 dB ESTIMATE
  soft rr4: t=103.62 s, gap 581 ms, bg -33.2 dB, real to 254 ms, len 1099 ms, rel -12 dB ESTIMATE
  ghost rr1: t=96.96 s, gap 155 ms, bg -18.9 dB, real to 140 ms, len 815 ms, rel -24.9 dB REAL
  ghost rr2: t=42.16 s, gap 361 ms, bg -12.1 dB, real to 149 ms, len 708 ms, rel -25.1 dB REAL
  ghost rr3: t=168.68 s, gap 585 ms, bg -30.4 dB, real to 154 ms, len 900 ms, rel -20 dB ESTIMATE
  ghost rr4: t=67.47 s, gap 583 ms, bg -33.6 dB, real to 154 ms, len 1025 ms, rel -20 dB ESTIMATE