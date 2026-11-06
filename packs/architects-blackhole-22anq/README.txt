ZC SNARE EXTRACT v3.0 - Architects - "Blackhole" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 152 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.927,
    hit-to-hit level SD 4.26 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.9  vs full drum stem -9.6  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -9.4  vs drum stem -9.0
    Hit-locked energy left in the separator residual (snare that got dropped): -43.9 dBFS at 0-5 ms vs -11.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -17.4, '150-300': -0.1, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.5, '2500-5000': -1.1, '5000-8000': -1.3, '8000-12000': -3.1, '12000-16000': -6.0}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.67, 2.83, 5.42, 5.8] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-122.0, -253.0, -110.0, -87.0, -134.0] dB/s  ->  T60 [0.49, 0.24, 0.54, 0.69, 0.45] s
  early part (60-150 ms, body + early reflections): [None, -117.0, -82.0, -87.0, -134.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -8.7, '50ms': -13.5, '100ms': -14.8, '150ms': -19.5}
  Snare-stem noise floor between hits: -83.2 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 2/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_architects-blackhole-22anq_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=17.22 s, gap 1391 ms, bg -39.1 dB, real to 329 ms, len 640 ms, rel 0.7 dB REAL
  hard rr2: t=161.22 s, gap 1491 ms, bg -40.4 dB, real to 179 ms, len 630 ms, rel 0.1 dB REAL
  hard rr3: t=132.72 s, gap 556 ms, bg -43.7 dB, real to 214 ms, len 629 ms, rel 0.3 dB REAL
  hard rr4: t=59.22 s, gap 680 ms, bg -32.2 dB, real to 184 ms, len 710 ms, rel -0.1 dB REAL
  medium rr1: t=165.35 s, gap 251 ms, bg -20.6 dB, real to 149 ms, len 569 ms, rel -4.0 dB REAL
  medium rr2: t=191.22 s, gap 224 ms, bg -38.6 dB, real to 149 ms, len 597 ms, rel -3.2 dB REAL
  medium rr3: t=8.41 s, gap 188 ms, bg -38.6 dB, real to 173 ms, len 719 ms, rel -9.7 dB REAL
  medium rr4: t=141.44 s, gap 193 ms, bg -19.4 dB, real to 149 ms, len 554 ms, rel -3.5 dB REAL
  soft rr1: t=7.09 s, gap 200 ms, bg -20.6 dB, real to 185 ms, len 734 ms, rel -14.1 dB REAL
  soft rr2: t=91.85 s, gap 282 ms, bg -38.3 dB, real to 267 ms, len 868 ms, rel -11.0 dB REAL
  soft rr3: t=195.72 s, gap 366 ms, bg -43.0 dB, real to 219 ms, len 560 ms, rel -12 dB ESTIMATE
  soft rr4: t=28.85 s, gap 357 ms, bg -46.2 dB, real to 342 ms, len 581 ms, rel -12 dB ESTIMATE
  ghost rr1: t=25.85 s, gap 357 ms, bg -42.1 dB, real to 342 ms, len 650 ms, rel -20 dB ESTIMATE
  ghost rr2: t=42.97 s, gap 1111 ms, bg -17.8 dB, real to 149 ms, len 679 ms, rel -20 dB ESTIMATE
  ghost rr3: t=22.85 s, gap 366 ms, bg -46.5 dB, real to 314 ms, len 700 ms, rel -20 dB ESTIMATE
  ghost rr4: t=155.22 s, gap 1493 ms, bg -27.8 dB, real to 159 ms, len 645 ms, rel -20 dB ESTIMATE