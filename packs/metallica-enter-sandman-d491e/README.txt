ZC SNARE EXTRACT v3.0 - Metallica - "Enter Sandman" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 172 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.59,
    hit-to-hit level SD 4.88 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.9  vs full drum stem -9.8  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -15.7  vs drum stem -14.3
    Hit-locked energy left in the separator residual (snare that got dropped): -46.5 dBFS at 0-5 ms vs -15.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -8.8, '150-300': -0.2, '300-600': -0.3, '600-1200': -0.5, '1200-2500': -0.7, '2500-5000': -2.9, '5000-8000': -4.2, '8000-12000': -6.9, '12000-16000': -10.8}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [3.54, 4.6, 5.56, 1.93] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-76.0, -100.0, -106.0, -96.0, -132.0] dB/s  ->  T60 [0.79, 0.6, 0.56, 0.62, 0.45] s
  early part (60-150 ms, body + early reflections): [-76.0, -74.0, -76.0, -84.0, -115.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.3, '30ms': -9.4, '50ms': -13.1, '100ms': -18.9, '150ms': -21.5, '200ms': -24.5, '300ms': -27.4}
  Snare-stem noise floor between hits: -96.3 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 4/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_metallica-enter-sandman-d491e_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=259.56 s, gap 1782 ms, bg -37.8 dB, real to 194 ms, len 697 ms, rel -0.5 dB REAL
  hard rr2: t=242.5 s, gap 716 ms, bg -39.0 dB, real to 244 ms, len 714 ms, rel -0.6 dB REAL
  hard rr3: t=156.99 s, gap 2889 ms, bg -36.1 dB, real to 279 ms, len 854 ms, rel -2.1 dB REAL
  hard rr4: t=76.07 s, gap 950 ms, bg -38.7 dB, real to 294 ms, len 679 ms, rel -0.4 dB REAL
  medium rr1: t=221.84 s, gap 262 ms, bg -39.6 dB, real to 164 ms, len 589 ms, rel -9.5 dB REAL
  medium rr2: t=134.89 s, gap 181 ms, bg -36.9 dB, real to 166 ms, len 749 ms, rel -4.2 dB REAL
  medium rr3: t=235.98 s, gap 286 ms, bg -41.4 dB, real to 271 ms, len 700 ms, rel -4.0 dB REAL
  medium rr4: t=144.5 s, gap 234 ms, bg -33.4 dB, real to 164 ms, len 655 ms, rel -5.9 dB REAL
  soft rr1: t=314.03 s, gap 240 ms, bg -27.4 dB, real to 149 ms, len 720 ms, rel -13.5 dB REAL
  soft rr2: t=144.74 s, gap 235 ms, bg -18.0 dB, real to 149 ms, len 575 ms, rel -17.7 dB REAL
  soft rr3: t=235.75 s, gap 230 ms, bg -30.9 dB, real to 149 ms, len 451 ms, rel -11.0 dB REAL
  soft rr4: t=52.42 s, gap 134 ms, bg -37.5 dB, real to 119 ms, len 685 ms, rel -10.0 dB REAL
  ghost rr1: t=257.87 s, gap 723 ms, bg -38.4 dB, real to 224 ms, len 664 ms, rel -20 dB ESTIMATE
  ghost rr2: t=281.04 s, gap 644 ms, bg -31.5 dB, real to 194 ms, len 739 ms, rel -20 dB ESTIMATE
  ghost rr3: t=129.08 s, gap 961 ms, bg -35.3 dB, real to 209 ms, len 696 ms, rel -20 dB ESTIMATE
  ghost rr4: t=104.93 s, gap 2176 ms, bg -39.0 dB, real to 279 ms, len 784 ms, rel -20 dB ESTIMATE