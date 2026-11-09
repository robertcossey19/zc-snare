ZC SNARE EXTRACT v5.0 - Underoath - "It's Dangerous Business Walking Out Your Front Door" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 132 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.869,
    hit-to-hit level SD 1.74 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -16.6  vs full drum stem -16.4  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -23.1  vs drum stem -22.6
    Hit-locked energy left in the separator residual (snare that got dropped): -61.9 dBFS at 0-5 ms vs -17.5 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -17.2, '150-300': -0.2, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.4, '2500-5000': -1.7, '5000-8000': -2.5, '8000-12000': -6.1, '12000-16000': -12.4}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    245 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [2.81, 1.25, 1.72, 2.2] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-128.0, -145.0, -104.0, -118.0, -138.0] dB/s  ->  T60 [0.47, 0.41, 0.58, 0.51, 0.44] s
  early part (60-150 ms, body + early reflections): [None, -94.0, -104.0, -118.0, -138.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': -6.5, '30ms': -13.8, '50ms': -15.1, '100ms': -19.7, '150ms': -24.8, '200ms': -27.4}
  Snare-stem noise floor between hits: -93.5 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 0/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: scaled x2.50 from the record's medium hits (20).
 ZC_underoath-it-s-dangerous-bus-d4e00_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=17.68 s, gap 778 ms, bg -34.7 dB, real to 314 ms, len 435 ms, rel -0.1 dB REAL
  hard rr2: t=185.22 s, gap 512 ms, bg -36.2 dB, real to 104 ms, len 480 ms, rel 1.0 dB REAL
  hard rr3: t=233.23 s, gap 3042 ms, bg -37.2 dB, real to 69 ms, len 475 ms, rel -2.6 dB REAL
  hard rr4: t=16.33 s, gap 500 ms, bg -43.1 dB, real to 239 ms, len 440 ms, rel 1.0 dB REAL
  medium rr1: t=104.77 s, gap 1342 ms, bg -20.8 dB, real to 239 ms, len 445 ms, rel -7.9 dB REAL
  medium rr2: t=106.12 s, gap 877 ms, bg -30.7 dB, real to 428 ms, len 455 ms, rel -3.1 dB REAL
  medium rr3: t=94.8 s, gap 236 ms, bg -29.9 dB, real to 214 ms, len 429 ms, rel -3.2 dB REAL
  medium rr4: t=102.11 s, gap 443 ms, bg -26.0 dB, real to 404 ms, len 485 ms, rel -3.6 dB REAL
  soft rr1: t=195.46 s, gap 1143 ms, bg -30.0 dB, real to 164 ms, len 474 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))
  soft rr2: t=131.9 s, gap 880 ms, bg -32.9 dB, real to 274 ms, len 455 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))
  soft rr3: t=117.68 s, gap 649 ms, bg -35.7 dB, real to 324 ms, len 470 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))
  soft rr4: t=90.12 s, gap 679 ms, bg -33.9 dB, real to 149 ms, len 465 ms, rel -14.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))
  ghost rr1: t=219.0 s, gap 2211 ms, bg -38.2 dB, real to 428 ms, len 445 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))
  ghost rr2: t=114.12 s, gap 505 ms, bg -42.9 dB, real to 374 ms, len 480 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))
  ghost rr3: t=125.67 s, gap 886 ms, bg -37.4 dB, real to 234 ms, len 445 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))
  ghost rr4: t=121.24 s, gap 872 ms, bg -38.2 dB, real to 354 ms, len 424 ms, rel -24.0 dB ESTIMATE (scaled x2.50 from the record's medium hits (20))