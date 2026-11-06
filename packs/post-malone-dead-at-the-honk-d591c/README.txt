ZC SNARE EXTRACT v3.0 - Post Malone - "Dead at the Honky Tonk" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 109 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.729,
    hit-to-hit level SD 11.83 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -12.4  vs full drum stem -11.5  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.4  vs drum stem -8.4
    Hit-locked energy left in the separator residual (snare that got dropped): -45.8 dBFS at 0-5 ms vs -19.7 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -23.4, '150-300': -2.3, '300-600': -3.8, '600-1200': -3.6, '1200-2500': -3.4, '2500-5000': -1.8, '5000-8000': -1.2, '8000-12000': -1.3, '12000-16000': -2.1}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.97, 2.68, 3.49, 4.1] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-183.0, -30.0, -85.0, -85.0, -133.0] dB/s  ->  T60 [0.33, 2.0, 0.71, 0.71, 0.45] s
  early part (60-150 ms, body + early reflections): [-183.0, -127.0, None, -85.0, -133.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -1.5, '30ms': -4.2, '50ms': -8.3, '100ms': -16.3, '150ms': -18.4, '200ms': -21.4}
  Snare-stem noise floor between hits: -91.9 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 3/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_post-malone-dead-at-the-honk-d591c_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=138.32 s, gap 1438 ms, bg -30.0 dB, real to 259 ms, len 1282 ms, rel -0.9 dB REAL
  hard rr2: t=103.62 s, gap 581 ms, bg -30.2 dB, real to 249 ms, len 1282 ms, rel -0.6 dB REAL
  hard rr3: t=177.35 s, gap 1079 ms, bg -34.7 dB, real to 294 ms, len 1282 ms, rel 0.7 dB REAL
  hard rr4: t=126.75 s, gap 1438 ms, bg -34.7 dB, real to 294 ms, len 1281 ms, rel -2.3 dB REAL
  medium rr1: t=170.71 s, gap 848 ms, bg -45.3 dB, real to 204 ms, len 548 ms, rel -8.7 dB REAL
  medium rr2: t=146.99 s, gap 610 ms, bg -35.9 dB, real to 149 ms, len 1173 ms, rel -3.3 dB REAL
  medium rr3: t=53.6 s, gap 351 ms, bg -34.9 dB, real to 149 ms, len 1283 ms, rel -7.4 dB REAL
  medium rr4: t=88.08 s, gap 1071 ms, bg -43.3 dB, real to 149 ms, len 978 ms, rel -3.8 dB REAL
  soft rr1: t=55.05 s, gap 129 ms, bg -40.8 dB, real to 113 ms, len 1283 ms, rel -11.0 dB REAL
  soft rr2: t=104.2 s, gap 136 ms, bg -47.2 dB, real to 121 ms, len 1104 ms, rel -11.0 dB REAL
  soft rr3: t=30.26 s, gap 222 ms, bg -31.4 dB, real to 149 ms, len 1200 ms, rel -12.3 dB REAL
  soft rr4: t=105.06 s, gap 586 ms, bg -35.6 dB, real to 274 ms, len 1282 ms, rel -12 dB ESTIMATE
  ghost rr1: t=86.27 s, gap 1439 ms, bg -37.5 dB, real to 164 ms, len 1280 ms, rel -20 dB ESTIMATE
  ghost rr2: t=116.63 s, gap 618 ms, bg -31.2 dB, real to 154 ms, len 1280 ms, rel -20 dB ESTIMATE
  ghost rr3: t=77.59 s, gap 702 ms, bg -39.4 dB, real to 149 ms, len 1281 ms, rel -20 dB ESTIMATE
  ghost rr4: t=67.47 s, gap 583 ms, bg -33.6 dB, real to 159 ms, len 1282 ms, rel -20 dB ESTIMATE