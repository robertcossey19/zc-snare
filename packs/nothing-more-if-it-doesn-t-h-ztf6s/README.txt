ZC SNARE EXTRACT v3.0 - Nothing More - "If It Doesn't Hurt" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 135 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.916,
    hit-to-hit level SD 3.65 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.4  vs full drum stem -9.9  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.7  vs drum stem -11.5
    Hit-locked energy left in the separator residual (snare that got dropped): -42.5 dBFS at 0-5 ms vs -11.6 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -11.2, '150-300': -0.1, '300-600': -0.1, '600-1200': -0.1, '1200-2500': -0.3, '2500-5000': -1.2, '5000-8000': -1.5, '8000-12000': -2.9, '12000-16000': -5.0}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [5.31, 1.66, 1.84, 5.8] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-126.0, -127.0, -125.0, -125.0, -168.0] dB/s  ->  T60 [0.48, 0.47, 0.48, 0.48, 0.36] s
  early part (60-150 ms, body + early reflections): [None, -168.0, -110.0, -103.0, -168.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -12.1, '50ms': -9.8, '100ms': -16.7, '150ms': -23.3, '200ms': -27.4}
  Snare-stem noise floor between hits: -83.8 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_nothing-more-if-it-doesn-t-h-ztf6s_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=41.66 s, gap 1255 ms, bg -37.5 dB, real to 244 ms, len 591 ms, rel 0.3 dB REAL
  hard rr2: t=84.61 s, gap 1255 ms, bg -35.9 dB, real to 254 ms, len 630 ms, rel 0.9 dB REAL
  hard rr3: t=160.08 s, gap 938 ms, bg -40.8 dB, real to 254 ms, len 585 ms, rel -0.7 dB REAL
  hard rr4: t=121.87 s, gap 469 ms, bg -42.8 dB, real to 224 ms, len 576 ms, rel 0.6 dB REAL
  medium rr1: t=176.35 s, gap 158 ms, bg -25.2 dB, real to 143 ms, len 570 ms, rel -4.5 dB REAL
  medium rr2: t=176.5 s, gap 156 ms, bg -23.3 dB, real to 141 ms, len 521 ms, rel -4.1 dB REAL
  medium rr3: t=176.66 s, gap 465 ms, bg -29.0 dB, real to 149 ms, len 609 ms, rel -3.2 dB REAL
  medium rr4: t=176.03 s, gap 153 ms, bg -27.0 dB, real to 138 ms, len 544 ms, rel -4.5 dB REAL
  soft rr1: t=24.13 s, gap 167 ms, bg -11.0 dB, real to 152 ms, len 450 ms, rel -15.1 dB REAL
  soft rr2: t=104.82 s, gap 468 ms, bg -47.1 dB, real to 329 ms, len 595 ms, rel -12 dB ESTIMATE
  soft rr3: t=35.98 s, gap 464 ms, bg -44.5 dB, real to 274 ms, len 595 ms, rel -12 dB ESTIMATE
  soft rr4: t=44.19 s, gap 467 ms, bg -45.0 dB, real to 279 ms, len 585 ms, rel -12 dB ESTIMATE
  ghost rr1: t=174.77 s, gap 464 ms, bg -42.6 dB, real to 249 ms, len 581 ms, rel -20 dB ESTIMATE
  ghost rr2: t=47.82 s, gap 468 ms, bg -39.1 dB, real to 259 ms, len 647 ms, rel -20 dB ESTIMATE
  ghost rr3: t=173.03 s, gap 1730 ms, bg -24.7 dB, real to 149 ms, len 540 ms, rel -20 dB ESTIMATE
  ghost rr4: t=131.98 s, gap 468 ms, bg -37.2 dB, real to 304 ms, len 675 ms, rel -20 dB ESTIMATE