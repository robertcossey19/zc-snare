ZC SNARE EXTRACT v3.0 - Asking Alexandria - "The Final Episode" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 166 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.945,
    hit-to-hit level SD 1.15 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.9  vs full drum stem -9.0  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.7  vs drum stem -10.9
    Hit-locked energy left in the separator residual (snare that got dropped): -43.4 dBFS at 0-5 ms vs -10.4 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -16.4, '150-300': -0.0, '300-600': -0.4, '600-1200': -1.0, '1200-2500': -1.7, '2500-5000': -4.2, '5000-8000': -5.2, '8000-12000': -8.9, '12000-16000': -14.0}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.79, 1.84, 2.2, 0.68] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-141.0, -170.0, -140.0, -107.0, -142.0] dB/s  ->  T60 [0.42, 0.35, 0.43, 0.56, 0.42] s
  early part (60-150 ms, body + early reflections): [None, -97.0, -116.0, -121.0, -142.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -0.3, '30ms': -12.0, '50ms': -13.1, '100ms': -22.9, '150ms': -28.6, '200ms': -29.6}
  Snare-stem noise floor between hits: -91.1 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 2/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_asking-alexandria-the-final--d3f79_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=69.09 s, gap 605 ms, bg -43.6 dB, real to 179 ms, len 558 ms, rel -0.9 dB REAL
  hard rr2: t=34.16 s, gap 611 ms, bg -40.2 dB, real to 179 ms, len 545 ms, rel -0.2 dB REAL
  hard rr3: t=45.19 s, gap 917 ms, bg -44.3 dB, real to 219 ms, len 540 ms, rel 0.2 dB REAL
  hard rr4: t=130.37 s, gap 3818 ms, bg -28.1 dB, real to 149 ms, len 554 ms, rel 0.6 dB REAL
  medium rr1: t=96.67 s, gap 269 ms, bg -42.6 dB, real to 179 ms, len 500 ms, rel -3.0 dB REAL
  medium rr2: t=127.92 s, gap 252 ms, bg -43.7 dB, real to 149 ms, len 397 ms, rel -3.2 dB REAL
  medium rr3: t=54.67 s, gap 672 ms, bg -35.3 dB, real to 254 ms, len 665 ms, rel -6 dB ESTIMATE
  medium rr4: t=75.82 s, gap 525 ms, bg -44.8 dB, real to 194 ms, len 495 ms, rel -6 dB ESTIMATE
  soft rr1: t=72.15 s, gap 459 ms, bg -43.3 dB, real to 174 ms, len 600 ms, rel -12 dB ESTIMATE
  soft rr2: t=89.32 s, gap 357 ms, bg -45.1 dB, real to 269 ms, len 520 ms, rel -12 dB ESTIMATE
  soft rr3: t=71.54 s, gap 311 ms, bg -54.1 dB, real to 289 ms, len 490 ms, rel -12 dB ESTIMATE
  soft rr4: t=68.48 s, gap 456 ms, bg -39.3 dB, real to 164 ms, len 530 ms, rel -12 dB ESTIMATE
  ghost rr1: t=28.65 s, gap 441 ms, bg -42.7 dB, real to 364 ms, len 630 ms, rel -20 dB ESTIMATE
  ghost rr2: t=70.93 s, gap 304 ms, bg -44.5 dB, real to 174 ms, len 440 ms, rel -20 dB ESTIMATE
  ghost rr3: t=65.42 s, gap 305 ms, bg -46.1 dB, real to 174 ms, len 405 ms, rel -20 dB ESTIMATE
  ghost rr4: t=140.01 s, gap 757 ms, bg -17.0 dB, real to 149 ms, len 654 ms, rel -20 dB ESTIMATE