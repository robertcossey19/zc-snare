ZC SNARE EXTRACT v3.0 - Asking Alexandria - "The Final Episode" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 166 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.937,
    hit-to-hit level SD 3.2 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -9.9  vs full drum stem -9.0  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -11.7  vs drum stem -10.9
    Hit-locked energy left in the separator residual (snare that got dropped): -43.2 dBFS at 0-5 ms vs -11.1 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -14.2, '150-300': -0.0, '300-600': -0.4, '600-1200': -0.9, '1200-2500': -1.5, '2500-5000': -4.1, '5000-8000': -5.1, '8000-12000': -8.9, '12000-16000': -14.0}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [1.61, 1.43, 2.2, 2.81] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-104.0, -127.0, -114.0, -93.0, -75.0] dB/s  ->  T60 [0.58, 0.47, 0.52, 0.65, 0.8] s
  early part (60-150 ms, body + early reflections): [None, -104.0, -106.0, -119.0, -134.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -0.4, '30ms': -11.8, '50ms': -12.8, '100ms': -23.3, '150ms': -28.1, '200ms': -29.1}
  Snare-stem noise floor between hits: -91.7 dBFS.

LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard 4/4, medium 1/4, soft 0/4, ghost 0/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread.
 ZC_asking-alexandria-the-final--d3f79_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=68.48 s, gap 603 ms, bg -41.5 dB, real to 184 ms, len 565 ms, rel -0.7 dB REAL
  hard rr2: t=70.93 s, gap 603 ms, bg -42.5 dB, real to 179 ms, len 579 ms, rel -0.8 dB REAL
  hard rr3: t=45.19 s, gap 917 ms, bg -45.1 dB, real to 204 ms, len 570 ms, rel 0.2 dB REAL
  hard rr4: t=69.09 s, gap 605 ms, bg -43.2 dB, real to 264 ms, len 618 ms, rel -1.1 dB REAL
  medium rr1: t=127.92 s, gap 252 ms, bg -44.5 dB, real to 149 ms, len 411 ms, rel -3.3 dB REAL
  medium rr2: t=75.82 s, gap 532 ms, bg -43.9 dB, real to 184 ms, len 634 ms, rel -6 dB ESTIMATE
  medium rr3: t=54.67 s, gap 1522 ms, bg -34.5 dB, real to 229 ms, len 839 ms, rel -6 dB ESTIMATE
  medium rr4: t=191.03 s, gap 3053 ms, bg -26.9 dB, real to 149 ms, len 639 ms, rel -6 dB ESTIMATE
  soft rr1: t=130.37 s, gap 3823 ms, bg -28.5 dB, real to 149 ms, len 659 ms, rel -12 dB ESTIMATE
  soft rr2: t=198.53 s, gap 751 ms, bg -25.5 dB, real to 149 ms, len 534 ms, rel -12 dB ESTIMATE
  soft rr3: t=28.65 s, gap 446 ms, bg -43.4 dB, real to 384 ms, len 709 ms, rel -12 dB ESTIMATE
  soft rr4: t=96.67 s, gap 401 ms, bg -41.4 dB, real to 169 ms, len 620 ms, rel -12 dB ESTIMATE
  ghost rr1: t=64.8 s, gap 398 ms, bg -40.5 dB, real to 159 ms, len 567 ms, rel -20 dB ESTIMATE
  ghost rr2: t=56.21 s, gap 388 ms, bg -47.0 dB, real to 199 ms, len 569 ms, rel -20 dB ESTIMATE
  ghost rr3: t=104.01 s, gap 364 ms, bg -44.4 dB, real to 199 ms, len 524 ms, rel -20 dB ESTIMATE
  ghost rr4: t=92.99 s, gap 353 ms, bg -41.8 dB, real to 209 ms, len 580 ms, rel -20 dB ESTIMATE