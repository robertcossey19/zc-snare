ZC SNARE EXTRACT v3.0 - Nickelback - "San Quentin" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 217 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.95,
    hit-to-hit level SD 3.86 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.5  vs full drum stem -8.2  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -13.9  vs drum stem -9.8
    Hit-locked energy left in the separator residual (snare that got dropped): -29.6 dBFS at 0-5 ms vs -10.2 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -32.9, '150-300': -0.3, '300-600': -1.2, '600-1200': -1.4, '1200-2500': -2.2, '2500-5000': -5.4, '5000-8000': -8.8, '8000-12000': -8.5, '12000-16000': -11.9}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.81, 2.97, 1.68, 2.34] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-107.0, -126.0, -103.0, -70.0, -111.0] dB/s  ->  T60 [0.56, 0.48, 0.58, 0.85, 0.54] s
  early part (60-150 ms, body + early reflections): [None, -52.0, -49.0, -56.0, -77.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.2, '30ms': -16.2, '50ms': -15.3, '100ms': -10.5, '150ms': -12.9, '200ms': -20.4, '300ms': -27.1}
  Snare-stem noise floor between hits: -83.3 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_nickelback-san-quentin-offic-39akj_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=151.04 s, gap 1675 ms, bg -30.1 dB, real to 274 ms, len 899 ms, rel -1.2 dB REAL
  hard rr2: t=164.82 s, gap 961 ms, bg -39.8 dB, real to 399 ms, len 925 ms, rel 0.3 dB REAL
  hard rr3: t=167.72 s, gap 475 ms, bg -40.1 dB, real to 319 ms, len 664 ms, rel 0.7 dB REAL
  hard rr4: t=208.85 s, gap 461 ms, bg -36.6 dB, real to 314 ms, len 680 ms, rel 0.4 dB REAL
  medium rr1: t=26.92 s, gap 2410 ms, bg -21.0 dB, real to 184 ms, len 889 ms, rel -3.1 dB REAL
  medium rr2: t=23.04 s, gap 512 ms, bg -22.2 dB, real to 179 ms, len 949 ms, rel -5.6 dB REAL
  medium rr3: t=18.92 s, gap 243 ms, bg -29.4 dB, real to 204 ms, len 908 ms, rel -5.6 dB REAL
  medium rr4: t=17.7 s, gap 488 ms, bg -22.6 dB, real to 159 ms, len 968 ms, rel -5.2 dB REAL
  soft rr1: t=15.04 s, gap 244 ms, bg -35.1 dB, real to 229 ms, len 959 ms, rel -11.5 dB REAL
  soft rr2: t=169.66 s, gap 720 ms, bg -42.1 dB, real to 319 ms, len 694 ms, rel -12 dB ESTIMATE
  soft rr3: t=77.72 s, gap 583 ms, bg -40.3 dB, real to 319 ms, len 759 ms, rel -12 dB ESTIMATE
  soft rr4: t=226.75 s, gap 552 ms, bg -41.8 dB, real to 294 ms, len 765 ms, rel -12 dB ESTIMATE
  ghost rr1: t=91.51 s, gap 411 ms, bg -43.0 dB, real to 396 ms, len 779 ms, rel -20 dB ESTIMATE
  ghost rr2: t=170.62 s, gap 389 ms, bg -42.1 dB, real to 374 ms, len 804 ms, rel -20 dB ESTIMATE
  ghost rr3: t=129.5 s, gap 364 ms, bg -36.0 dB, real to 314 ms, len 760 ms, rel -20 dB ESTIMATE
  ghost rr4: t=157.07 s, gap 474 ms, bg -40.1 dB, real to 399 ms, len 933 ms, rel -20 dB ESTIMATE