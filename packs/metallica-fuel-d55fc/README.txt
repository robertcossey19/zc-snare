ZC SNARE EXTRACT v3.0 - Metallica - "Fuel" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 290 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.68,
    hit-to-hit level SD 2.84 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -11.7  vs full drum stem -10.9  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -14.2  vs drum stem -13.0
    Hit-locked energy left in the separator residual (snare that got dropped): -53.1 dBFS at 0-5 ms vs -17.0 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -17.6, '150-300': -0.2, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.3, '2500-5000': -1.2, '5000-8000': -2.5, '8000-12000': -4.6, '12000-16000': -7.2}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [1.81, 4.69, 5.94, 5.8] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-78.0, -81.0, -73.0, -74.0, -104.0] dB/s  ->  T60 [0.77, 0.74, 0.83, 0.81, 0.58] s
  early part (60-150 ms, body + early reflections): [None, -103.0, -105.0, -135.0, -147.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -3.6, '30ms': -6.9, '50ms': -9.4, '100ms': -16.8, '150ms': -21.4, '200ms': -23.8}
  Snare-stem noise floor between hits: -78.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 4/4, soft 2/4, ghost 1/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_metallica-fuel-d55fc_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=90.08 s, gap 1117 ms, bg -35.6 dB, real to 254 ms, len 855 ms, rel 0.6 dB REAL
  hard rr2: t=117.16 s, gap 569 ms, bg -37.4 dB, real to 234 ms, len 680 ms, rel -1.5 dB REAL
  hard rr3: t=112.66 s, gap 853 ms, bg -34.0 dB, real to 204 ms, len 711 ms, rel -2.0 dB REAL
  hard rr4: t=263.35 s, gap 555 ms, bg -38.8 dB, real to 244 ms, len 815 ms, rel 1.9 dB REAL
  medium rr1: t=228.85 s, gap 996 ms, bg -19.5 dB, real to 149 ms, len 856 ms, rel -5.2 dB REAL
  medium rr2: t=212.25 s, gap 250 ms, bg -37.1 dB, real to 159 ms, len 730 ms, rel -3.6 dB REAL
  medium rr3: t=241.0 s, gap 137 ms, bg -42.1 dB, real to 122 ms, len 863 ms, rel -4.1 dB REAL
  medium rr4: t=246.87 s, gap 293 ms, bg -39.0 dB, real to 184 ms, len 773 ms, rel -3.6 dB REAL
  soft rr1: t=65.8 s, gap 152 ms, bg -32.8 dB, real to 137 ms, len 664 ms, rel -16.5 dB REAL
  soft rr2: t=213.23 s, gap 396 ms, bg -10.5 dB, real to 149 ms, len 612 ms, rel -13.8 dB REAL
  soft rr3: t=84.77 s, gap 558 ms, bg -43.0 dB, real to 274 ms, len 818 ms, rel -12 dB ESTIMATE
  soft rr4: t=147.64 s, gap 560 ms, bg -35.5 dB, real to 179 ms, len 824 ms, rel -12 dB ESTIMATE
  ghost rr1: t=51.77 s, gap 159 ms, bg -29.5 dB, real to 144 ms, len 831 ms, rel -21.3 dB REAL
  ghost rr2: t=85.89 s, gap 550 ms, bg -38.2 dB, real to 264 ms, len 854 ms, rel -20 dB ESTIMATE
  ghost rr3: t=256.93 s, gap 553 ms, bg -35.5 dB, real to 224 ms, len 854 ms, rel -20 dB ESTIMATE
  ghost rr4: t=42.0 s, gap 1125 ms, bg -31.8 dB, real to 164 ms, len 794 ms, rel -20 dB ESTIMATE