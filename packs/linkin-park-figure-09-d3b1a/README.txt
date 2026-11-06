ZC SNARE EXTRACT v3.0 - Linkin Park - "Figure.09" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 130 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.76,
    hit-to-hit level SD 3.27 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -7.3  vs full drum stem -7.3  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.0  vs drum stem -14.7
    Hit-locked energy left in the separator residual (snare that got dropped): -56.9 dBFS at 0-5 ms vs -8.0 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -3.4, '150-300': -0.1, '300-600': -0.1, '600-1200': 0.0, '1200-2500': -0.0, '2500-5000': -0.7, '5000-8000': -2.4, '8000-12000': -6.3, '12000-16000': -11.1}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [1.97, 1.29, 3.06, 2.29] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-122.0, -94.0, -93.0, -150.0, -212.0] dB/s  ->  T60 [0.49, 0.64, 0.65, 0.4, 0.28] s
  early part (60-150 ms, body + early reflections): [None, -94.0, -93.0, -150.0, -212.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -6.9, '30ms': -13.1, '50ms': -17.1, '100ms': -22.6, '150ms': -25.6}
  Snare-stem noise floor between hits: -95.8 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_linkin-park-figure-09-d3b1a_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=43.55 s, gap 1214 ms, bg -42.4 dB, real to 164 ms, len 709 ms, rel -0.7 dB REAL
  hard rr2: t=91.29 s, gap 1216 ms, bg -40.7 dB, real to 224 ms, len 694 ms, rel -0.3 dB REAL
  hard rr3: t=42.32 s, gap 1217 ms, bg -37.5 dB, real to 204 ms, len 694 ms, rel -1.0 dB REAL
  hard rr4: t=87.61 s, gap 1217 ms, bg -37.1 dB, real to 154 ms, len 725 ms, rel 0.4 dB REAL
  medium rr1: t=63.13 s, gap 308 ms, bg -42.2 dB, real to 149 ms, len 569 ms, rel -3.5 dB REAL
  medium rr2: t=150.04 s, gap 909 ms, bg -36.3 dB, real to 149 ms, len 609 ms, rel -7.4 dB REAL
  medium rr3: t=107.2 s, gap 298 ms, bg -38.5 dB, real to 149 ms, len 579 ms, rel -5.2 dB REAL
  medium rr4: t=112.1 s, gap 348 ms, bg -41.1 dB, real to 149 ms, len 525 ms, rel -8.4 dB REAL
  soft rr1: t=94.96 s, gap 454 ms, bg -34.2 dB, real to 149 ms, len 227 ms, rel -10.8 dB REAL
  soft rr2: t=90.06 s, gap 1215 ms, bg -36.7 dB, real to 199 ms, len 684 ms, rel -12 dB ESTIMATE
  soft rr3: t=115.77 s, gap 1217 ms, bg -36.8 dB, real to 149 ms, len 700 ms, rel -12 dB ESTIMATE
  soft rr4: t=118.22 s, gap 1216 ms, bg -37.7 dB, real to 179 ms, len 710 ms, rel -12 dB ESTIMATE
  ghost rr1: t=28.86 s, gap 605 ms, bg -44.7 dB, real to 154 ms, len 619 ms, rel -20 dB ESTIMATE
  ghost rr2: t=180.65 s, gap 780 ms, bg -38.6 dB, real to 154 ms, len 705 ms, rel -20 dB ESTIMATE
  ghost rr3: t=19.06 s, gap 605 ms, bg -40.0 dB, real to 169 ms, len 699 ms, rel -20 dB ESTIMATE
  ghost rr4: t=33.75 s, gap 654 ms, bg -33.0 dB, real to 149 ms, len 634 ms, rel -20 dB ESTIMATE