"""Write README.txt (all measurements from info.json) into pack2/<name>/ and ZC_Snare_<name>_RoundRobins.zip (ZIP_STORED, 16 WAV + README).
Usage: python3 pack_readme.py <name> "<Band>" "<Song>" ["<mixer credit>"]   (run from the working dir that holds pack2/)"""
import zipfile, json, os, sys
n, band, song = sys.argv[1], sys.argv[2], sys.argv[3]; mixer = sys.argv[4] if len(sys.argv) > 4 else 'Zakk Cervini'
if True:
    info=json.load(open(f'pack2/{n}/info.json')); sel=info['selected']
    lr=info.get('layers_real',{}); nreal={k:sum(v) for k,v in lr.items()}
    laws=sorted({h.get('law','') for h in sel if not h.get('real') and h.get('law')})
    if info.get('real_velocity'):
        layers_txt=f"""LAYERS (velocity bands re the loud cluster: hard >= -3 dB, medium -10..-3, soft -18..-10, ghost < -18; 75th percentile of hit gain = 0 dB)
 Each layer takes the 4 cleanest REAL hits of its band at the record's own level (rel dB per file below). Real hits in this pack:
 hard {nreal.get('hard',0)}/4, medium {nreal.get('medium',0)}/4, soft {nreal.get('soft',0)}/4, ghost {nreal.get('ghost',0)}/4.
 A slot marked ESTIMATE is a real full hit carried to that layer with THIS RECORD'S velocity law: the per-bin spectral offset
 its quieter hits show against the hard ensemble over the first 80 ms (minimum-phase, no pre-ring) and the median level of
 those hits. A layer with no measurable quiet hits takes the nearest measured layer's law scaled to its level (same drum).
 Only when the record has no quieter hits at all does the generic lighter-stroke transform (-6/-12/-20 dB, HF tilt) step in.
 The tail decay is never shortened for a quieter layer (a drum's ring and room decay do not depend on stroke level).
 Laws used here: {'; '.join(laws) if laws else 'none needed (all 16 slots real)'}."""
    else:
        layers_txt="""LAYERS
 hard   rr1-4 : four distinct real hits, untouched (hard = how the record was played).
 medium / soft / ghost rr1-4 : other real hits with the generic lighter-stroke transform (ESTIMATE - the record has no quiet hits):
                nominal -6 / -12 / -20 dB with a gentle HF tilt (-2.5 dB above 3 kHz / -5 dB above 2 kHz / -8 dB above 1.5 kHz + -4 above 5 kHz)."""

    readme=f"""ZC SNARE EXTRACT v5.0 - {band} - "{song}" (mixed by {mixer})
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised; the audible part of every file is the record's own hit, with only the bins the separator got wrong rebuilt to what the same drum measurably does on the other hits.
 1. Two-stage source separation: Demucs htdemucs (song -> drums) then MDX23C DrumSep by aufr33 & jarredou
    (drums -> kick / snare / toms / hi-hat / ride / crash). Everything below is done on the snare-only stem.
 2. {info['hits_aligned']} snare hits located and sub-sample aligned on the snare stem (median waveform correlation {info['corr_median']},
    hit-to-hit level SD {info['level_sd_db']} dB).
 3. Audit of what the separator did at the snare onsets (mean over all hits, dBFS):
      0-5 ms   snare stem {info['audit']['0-5ms']['snare']}  vs full drum stem {info['audit']['0-5ms']['drums']}  (transient intact; difference is the hat/kick share)
      5-30 ms  snare stem {info['audit']['5-30ms']['snare']}  vs drum stem {info['audit']['5-30ms']['drums']}
    Hit-locked energy left in the separator residual (snare that got dropped): {info['coherent_resid']['0-5ms']['coherent_resid_dB']} dBFS at 0-5 ms vs {info['coherent_resid']['0-5ms']['snare_dB']} dBFS of snare -> negligible.
    Snare stem minus drum stem, first 60 ms, per band (dB): {info['stem_vs_drums_tilt_db']}
    (only the sub band where the kick lives and 8-16 kHz where the hat lives lost level; 150 Hz - 8 kHz is within ~1 dB).
 4. Each file is ONE real hit, full length: its own transient, body, wires and room as it sits on the record. The first 8 ms are the
    raw stem, untouched. From there every STFT bin (1024/256) is checked against an ENSEMBLE PRIOR built from up to 100 aligned hits of the
    same layer: per bin, the median magnitude over the hits whose tail is clean there (a frame counts only before that hit's next snare and
    only where the drum stem's other material - kick, hat, ride - is not in event over the snare in that band). A bin that sits above the
    ensemble by more than its measured hit-to-hit spread (+2 dB) is bleed (hat/ride/kick leak); a bin well below it after 30 ms is a hole
    the separator ducked. Only those bins are rebuilt, to the ensemble level at this hit's own level (phase kept where close, otherwise
    re-estimated by Griffin-Lim); everything else is the record. Where the ensemble itself runs out of clean evidence (prior real to
    {sel[0].get('reclaimed_ms',{}).get('prior_real_to_ms','?') if isinstance(sel[0].get('reclaimed_ms'),dict) else '?'} ms, median over bins) each
    bin continues at that band's decay rate measured over the ensemble's late region (ESTIMATE; well under the hit's audible level).
    The file ends where the level falls under -88 dBFS.
 5. Onset: STFT separators smear ~15 ms of pre-echo ahead of the stick; the true onset was read off the time-domain drum
    stem (1 kHz high-passed) and the file starts 0.3 ms before it. Attack-to-peak in the files: {[h['attack_to_peak_ms'] for h in sel[:4]]} ms (hard rr1-4).{'''
    Real quiet-layer hits sit in busy context (kick/hat right before them), where that walk-back stops under the peak and
    clips the attack; those files instead start 0.5 ms before the snare stem's own 1 ms envelope last crossed -10.5 dB re its
    attack peak (1 ms fade-in). Every file starts >= 13 dB below its own peak.''' if info.get('real_velocity') else ''}

MEASURED DECAY (per-hit linear fit in dB on each hit's own clean range, song value = median over hits)
  bands <150 / 150-600 / 600-2k / 2-6k / >6k Hz, late part (150 ms on): {info["slope_db_s"]} dB/s  ->  T60 {list(info["t60_band"].values())} s
  early part (60-150 ms, body + early reflections): {info["slope_early_db_s"]} dB/s
  Median envelope of all hits relative to peak (dB): {info['tail_rel_peak_db']}
  Snare-stem noise floor between hits: {info['noise_floor_dbfs']} dBFS.

{layers_txt}
 ZC_{n}_oneshot.wav = hard rr1.

THE 16 HITS (time in song, air before next snare, background under the tail rel. peak, real tail used to, file length)
""" + "\n".join(f"  {h.get('layer',['hard','medium','soft','ghost'][i//4])} rr{i%4+1}: t={h['t']} s, gap {h['gap_ms']} ms, bg {h['bg_rel_peak_db']} dB, real to {h['real_to_ms'] if h['real_to_ms'] else 'end'} ms, len {h['len_ms']} ms" + (f", rel {h['rel_db']} dB {'REAL' if h.get('real') else 'ESTIMATE ('+str(h.get('law',''))+')'}" if info.get('real_velocity') else '') for i,h in enumerate(sel))
    with zipfile.ZipFile(f'ZC_Snare_{n}_RoundRobins.zip','w',zipfile.ZIP_STORED) as z:
        for lay in ['ghost','soft','medium','hard']:
            for i in range(1,5): z.write(f'pack2/{n}/ZC_{n}_{lay}_rr{i}.wav',f'ZC_{n}_{lay}_rr{i}.wav')
        z.writestr('README.txt',readme)
    open(f'pack2/{n}/README.txt','w').write(readme); print(n, os.path.getsize(f'ZC_Snare_{n}_RoundRobins.zip')//1024,'KB')
# Full HTML with embedded FLACs
