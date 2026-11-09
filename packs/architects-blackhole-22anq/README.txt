ZC SNARE EXTRACT v5.0 - Architects - "Blackhole" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 150 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.929,
    hit-to-hit level SD 4.58 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.2  vs full drum stem -9.8  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -9.6  vs drum stem -9.2
    Hit-locked energy left in the separator residual (snare that got dropped): -43.8 dBFS at 0-5 ms vs -11.3 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -18.2, '150-300': -0.1, '300-600': -0.3, '600-1200': -0.2, '1200-2500': -0.6, '2500-5000': -1.1, '5000-8000': -1.3, '8000-12000': -3.0, '12000-16000': -5.8}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak); a bin well below it after 30 ms is a hole
    the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    187 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.13, 4.67, 4.58, 3.29] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-107.0, -170.0, -95.0, -88.0, -119.0] dB/s  ->  T60 [0.56, 0.35, 0.63, 0.68, 0.51] s
  early part (60-150 ms, body + early reflections): [None, -114.0, -84.0, -88.0, -119.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -8.6, '50ms': -13.3, '100ms': -14.9, '150ms': -19.3, '200ms': -31.3}
  Snare-stem noise floor between hits: -82.8 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 3/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 14 medium hits; scaled x2.50 from the record's medium hits (14).
 ZC_architects-blackhole-22anq_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=161.22 s, gap 1491 ms, bg -38.8 dB, real to 219 ms, len 657 ms, rel 0.3 dB REAL
  hard rr2: t=17.22 s, gap 1391 ms, bg -34.7 dB, real to 264 ms, len 655 ms, rel 0.8 dB REAL
  hard rr3: t=44.6 s, gap 501 ms, bg -39.9 dB, real to 224 ms, len 640 ms, rel -1.0 dB REAL
  hard rr4: t=155.22 s, gap 1493 ms, bg -34.7 dB, real to 468 ms, len 675 ms, rel -0.7 dB REAL
  medium rr1: t=141.44 s, gap 191 ms, bg -18.4 dB, real to 209 ms, len 638 ms, rel -3.4 dB REAL
  medium rr2: t=165.35 s, gap 246 ms, bg -18.3 dB, real to 249 ms, len 639 ms, rel -3.5 dB REAL
  medium rr3: t=142.1 s, gap 276 ms, bg -14.6 dB, real to 239 ms, len 639 ms, rel -3.2 dB REAL
  medium rr4: t=131.22 s, gap 916 ms, bg -32.3 dB, real to 319 ms, len 660 ms, rel -3.4 dB ESTIMATE (measured on 14 medium hits)
  soft rr1: t=111.16 s, gap 378 ms, bg -41.5 dB, real to 249 ms, len 670 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))
  soft rr2: t=77.22 s, gap 378 ms, bg -39.4 dB, real to 379 ms, len 665 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))
  soft rr3: t=132.72 s, gap 364 ms, bg -44.4 dB, real to 219 ms, len 649 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))
  soft rr4: t=23.6 s, gap 375 ms, bg -42.6 dB, real to 404 ms, len 637 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))
  ghost rr1: t=195.72 s, gap 366 ms, bg -41.1 dB, real to 219 ms, len 661 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))
  ghost rr2: t=115.1 s, gap 931 ms, bg -22.0 dB, real to 284 ms, len 692 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))
  ghost rr3: t=184.1 s, gap 183 ms, bg -38.6 dB, real to 169 ms, len 660 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))
  ghost rr4: t=183.72 s, gap 306 ms, bg -41.2 dB, real to 284 ms, len 664 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (14))