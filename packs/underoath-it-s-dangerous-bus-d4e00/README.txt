ZC SNARE EXTRACT v3.0 - Underoath - "It's Dangerous Business Walking Out Your Front Door" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 129 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.868,
    hit-to-hit level SD 1.52 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -16.6  vs full drum stem -16.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -23.3  vs drum stem -22.9
    Hit-locked energy left in the separator residual (snare that got dropped): -62.8 dBFS at 0-5 ms vs -17.4 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -16.1, '150-300': -0.2, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.4, '2500-5000': -1.9, '5000-8000': -2.6, '8000-12000': -6.1, '12000-16000': -12.9}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [1.09, 1.25, 4.26, 1.47] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-121.0, -124.0, -106.0, -119.0, -139.0] dB/s  ->  T60 [0.49, 0.49, 0.57, 0.5, 0.43] s
  early part (60-150 ms, body + early reflections): [None, -95.0, -106.0, -119.0, -139.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -6.8, '30ms': -14.3, '50ms': -15.4, '100ms': -19.9, '150ms': -24.9, '200ms': -29.7}
  Snare-stem noise floor between hits: -93.6 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_underoath-it-s-dangerous-bus-d4e00_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=86.55 s, gap 659 ms, bg -38.3 dB, real to 229 ms, len 549 ms, rel -0.1 dB REAL
  hard rr2: t=131.9 s, gap 880 ms, bg -35.2 dB, real to 154 ms, len 525 ms, rel -0.3 dB REAL
  hard rr3: t=117.68 s, gap 649 ms, bg -36.5 dB, real to 154 ms, len 495 ms, rel -1.2 dB REAL
  hard rr4: t=219.0 s, gap 2211 ms, bg -37.5 dB, real to 199 ms, len 545 ms, rel -0.9 dB REAL
  medium rr1: t=106.12 s, gap 877 ms, bg -31.6 dB, real to 149 ms, len 515 ms, rel -3.1 dB REAL
  medium rr2: t=102.11 s, gap 441 ms, bg -25.1 dB, real to 149 ms, len 450 ms, rel -3.4 dB REAL
  medium rr3: t=104.77 s, gap 1342 ms, bg -20.4 dB, real to 149 ms, len 460 ms, rel -7.9 dB REAL
  medium rr4: t=140.6 s, gap 212 ms, bg -19.6 dB, real to 197 ms, len 644 ms, rel -3.3 dB REAL
  soft rr1: t=185.22 s, gap 1774 ms, bg -38.4 dB, real to 204 ms, len 550 ms, rel -12 dB ESTIMATE
  soft rr2: t=130.12 s, gap 876 ms, bg -44.3 dB, real to 214 ms, len 495 ms, rel -12 dB ESTIMATE
  soft rr3: t=116.79 s, gap 887 ms, bg -41.3 dB, real to 164 ms, len 499 ms, rel -12 dB ESTIMATE
  soft rr4: t=16.33 s, gap 1022 ms, bg -42.7 dB, real to 304 ms, len 544 ms, rel -12 dB ESTIMATE
  ghost rr1: t=79.45 s, gap 644 ms, bg -38.2 dB, real to 214 ms, len 540 ms, rel -20 dB ESTIMATE
  ghost rr2: t=88.32 s, gap 904 ms, bg -35.3 dB, real to 214 ms, len 605 ms, rel -20 dB ESTIMATE
  ghost rr3: t=17.68 s, gap 738 ms, bg -35.1 dB, real to 199 ms, len 490 ms, rel -20 dB ESTIMATE
  ghost rr4: t=125.67 s, gap 886 ms, bg -38.4 dB, real to 179 ms, len 504 ms, rel -20 dB ESTIMATE