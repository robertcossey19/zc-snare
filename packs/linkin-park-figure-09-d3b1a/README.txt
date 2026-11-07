ZC SNARE EXTRACT v3.0 - Linkin Park - "Figure.09" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 134 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.755,
    hit-to-hit level SD 4.03 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -7.6  vs full drum stem -7.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.3  vs drum stem -15.0
    Hit-locked energy left in the separator residual (snare that got dropped): -57.2 dBFS at 0-5 ms vs -8.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -3.9, '150-300': -0.1, '300-600': -0.1, '600-1200': 0.0, '1200-2500': -0.0, '2500-5000': -0.7, '5000-8000': -2.4, '8000-12000': -6.4, '12000-16000': -11.3}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.08, 1.84, 2.11, 8.39] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-132.0, -104.0, -87.0, -160.0, -213.0] dB/s  ->  T60 [0.45, 0.57, 0.69, 0.38, 0.28] s
  early part (60-150 ms, body + early reflections): [None, -104.0, -87.0, -160.0, -213.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -7.3, '30ms': -13.1, '50ms': -17.3, '100ms': -22.5, '150ms': -25.3, '200ms': -28.2}
  Snare-stem noise floor between hits: -95.3 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 2/4, ghost 3/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_linkin-park-figure-09-d3b1a_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=42.32 s, gap 1217 ms, bg -39.2 dB, real to 214 ms, len 739 ms, rel -0.9 dB REAL
  hard rr2: t=37.42 s, gap 1215 ms, bg -42.1 dB, real to 289 ms, len 715 ms, rel 0.4 dB REAL
  hard rr3: t=36.2 s, gap 1216 ms, bg -40.1 dB, real to 199 ms, len 750 ms, rel -0.0 dB REAL
  hard rr4: t=33.75 s, gap 662 ms, bg -37.1 dB, real to 149 ms, len 696 ms, rel -1.5 dB REAL
  medium rr1: t=63.13 s, gap 595 ms, bg -40.8 dB, real to 149 ms, len 575 ms, rel -4.4 dB REAL
  medium rr2: t=23.96 s, gap 145 ms, bg -35.3 dB, real to 130 ms, len 514 ms, rel -4.9 dB REAL
  medium rr3: t=153.72 s, gap 605 ms, bg -37.9 dB, real to 149 ms, len 520 ms, rel -3.6 dB REAL
  medium rr4: t=55.79 s, gap 306 ms, bg -42.3 dB, real to 149 ms, len 509 ms, rel -3.2 dB REAL
  soft rr1: t=94.96 s, gap 454 ms, bg -25.2 dB, real to 149 ms, len 342 ms, rel -11.5 dB REAL
  soft rr2: t=126.79 s, gap 898 ms, bg -28.3 dB, real to 149 ms, len 336 ms, rel -12.5 dB REAL
  soft rr3: t=34.97 s, gap 1217 ms, bg -37.5 dB, real to 179 ms, len 750 ms, rel -12 dB ESTIMATE
  soft rr4: t=180.65 s, gap 811 ms, bg -40.2 dB, real to 164 ms, len 759 ms, rel -12 dB ESTIMATE
  ghost rr1: t=96.18 s, gap 178 ms, bg -40.8 dB, real to 149 ms, len 225 ms, rel -18.1 dB REAL
  ghost rr2: t=95.88 s, gap 297 ms, bg -26.9 dB, real to 149 ms, len 394 ms, rel -25.5 dB REAL
  ghost rr3: t=103.53 s, gap 192 ms, bg -34.4 dB, real to 149 ms, len 524 ms, rel -21.4 dB REAL
  ghost rr4: t=90.06 s, gap 1215 ms, bg -35.6 dB, real to 184 ms, len 734 ms, rel -20 dB ESTIMATE