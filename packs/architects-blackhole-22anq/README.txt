ZC SNARE EXTRACT v5.0 - Architects - "Blackhole" (mixed by unknown)
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. 155 snare hits located and sub-sample aligned on the snare stem (median waveform correlation 0.922,
    hit-to-hit level SD 5.54 dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem -10.3  vs full drum stem -9.9  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem -9.6  vs drum stem -9.2
    Hit-locked energy left in the separator residual (snare that got dropped): -43.6 dBFS at 0-5 ms vs -11.7 dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {'60-150': -17.0, '150-300': -0.1, '300-600': -0.2, '600-1200': -0.2, '1200-2500': -0.6, '2500-5000': -1.1, '5000-8000': -1.4, '8000-12000': -3.2, '12000-16000': -5.9}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak), and so is every bin before/after it in time
    that still sits more than one spread above the ensemble (the stroke's quieter wash around its loud part - 5.0.4; without this the kept
    wash met the rebuilt region with a 6-13 dB wall). A bin well below the ensemble after 30 ms is a hole the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    181 ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: [4.17, 6.03, 3.15, 5.03] ms (hard rr1-4).
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): [-108.0, -106.0, -120.0, -83.0, -110.0] dB/s  ->  T60 [0.55, 0.56, 0.5, 0.72, 0.54] s
  early part (60-150 ms, body + early reflections): [None, -106.0, -78.0, -83.0, -110.0] dB/s
  Median envelope of all hits relative to peak (dB): {'10ms': 0.0, '30ms': -8.5, '50ms': -13.2, '100ms': -15.2, '150ms': -19.4}
  Snare-stem noise floor between hits: -82.7 dBFS.

LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard 4/4, medium 4/4, soft 1/4, ghost 0/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: measured on 7 soft hits; measured on 8 ghost hits.
 ZC_architects-blackhole-22anq_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
  hard rr1: t=161.22 s, gap 1491 ms, bg -40.7 dB, real to 189 ms, len 617 ms, rel 0.1 dB REAL
  hard rr2: t=59.22 s, gap 1490 ms, bg -36.6 dB, real to 399 ms, len 630 ms, rel -0.2 dB REAL
  hard rr3: t=29.6 s, gap 485 ms, bg -36.6 dB, real to 204 ms, len 585 ms, rel -0.2 dB REAL
  hard rr4: t=44.6 s, gap 377 ms, bg -42.5 dB, real to 204 ms, len 635 ms, rel -0.9 dB REAL
  medium rr1: t=33.25 s, gap 124 ms, bg -21.0 dB, real to 89 ms, len 631 ms, rel -8.8 dB REAL
  medium rr2: t=165.35 s, gap 293 ms, bg -21.2 dB, real to 174 ms, len 629 ms, rel -3.4 dB REAL
  medium rr3: t=141.44 s, gap 193 ms, bg -17.8 dB, real to 219 ms, len 608 ms, rel -3.6 dB REAL
  medium rr4: t=191.22 s, gap 237 ms, bg -35.6 dB, real to 194 ms, len 606 ms, rel -3.5 dB REAL
  soft rr1: t=40.1 s, gap 169 ms, bg -25.9 dB, real to 94 ms, len 662 ms, rel -10.5 dB REAL
  soft rr2: t=155.22 s, gap 1493 ms, bg -28.2 dB, real to 344 ms, len 669 ms, rel -11.0 dB ESTIMATE (measured on 7 soft hits)
  soft rr3: t=28.85 s, gap 358 ms, bg -45.5 dB, real to 299 ms, len 586 ms, rel -11.0 dB ESTIMATE (measured on 7 soft hits)
  soft rr4: t=195.72 s, gap 366 ms, bg -40.0 dB, real to 354 ms, len 650 ms, rel -11.0 dB ESTIMATE (measured on 7 soft hits)
  ghost rr1: t=183.72 s, gap 306 ms, bg -41.1 dB, real to 289 ms, len 574 ms, rel -21.4 dB ESTIMATE (measured on 8 ghost hits)
  ghost rr2: t=154.29 s, gap 188 ms, bg -44.5 dB, real to 234 ms, len 611 ms, rel -21.4 dB ESTIMATE (measured on 8 ghost hits)
  ghost rr3: t=77.22 s, gap 296 ms, bg -38.5 dB, real to 379 ms, len 615 ms, rel -21.4 dB ESTIMATE (measured on 8 ghost hits)
  ghost rr4: t=116.6 s, gap 253 ms, bg -39.2 dB, real to 274 ms, len 635 ms, rel -21.4 dB ESTIMATE (measured on 8 ghost hits)