"""Write README.txt (all measurements from info.json) into pack2/<name>/ and ZC_Snare_<name>_RoundRobins.zip (ZIP_STORED, 16 WAV + README).
Usage: python3 pack_readme.py <name> "<Band>" "<Song>" ["<mixer credit>"]   (run from the working dir that holds pack2/)"""
import zipfile, json, os, sys
n, band, song = sys.argv[1], sys.argv[2], sys.argv[3]; mixer = sys.argv[4] if len(sys.argv) > 4 else 'Zakk Cervini'
if True:
    info=json.load(open(f'pack2/{n}/info.json')); sel=info['selected']
    lr=info.get('layers_real',{}); nreal={k:sum(v) for k,v in lr.items()}
    if info.get('real_velocity'):
        layers_txt=f"""LAYERS (this record contains real quieter snare hits, so the quieter layers are REAL hits at their REAL level, not transforms)
 Every aligned hit was levelled against the loud cluster (75th percentile of hit gain = 0 dB). Velocity bands: hard >= -3 dB,
 medium -10..-3 dB, soft -18..-10 dB, ghost < -18 dB. Each layer takes the 4 cleanest real hits in its band (same tail/background/
 kick tests as the hard hits). Real hits in this pack: hard {nreal.get('hard',0)}/4, medium {nreal.get('medium',0)}/4, soft {nreal.get('soft',0)}/4, ghost {nreal.get('ghost',0)}/4.
 Any slot marked ESTIMATE below is a hard hit with the lighter-stroke transform used on the other packs (nominal -6/-12/-20 dB).
 Levels of the real quiet hits are the record's own (see rel dB per file below); hard rr1-4 keep the record's natural +/-1.5 dB spread."""
    else:
        layers_txt="""LAYERS
 hard   rr1-4 : four distinct real hits, untouched (hard = how the record was played).
 medium rr1-4 : four other real hits with physics-informed lighter-stroke transforms (ESTIMATE - the record has no quiet hits):
                nominal -6 dB, gentle tilt above 3 kHz (-2.5 dB), wire decay x0.9, pitch glide x0.8, attack x0.95.
 soft   rr1-4 : four other real hits: nominal -12 dB, tilt above 2 kHz (-5 dB), wire decay x0.75, glide x0.5, attack x0.85.
 ghost  rr1-4 : four other real hits: nominal -20 dB, tilt above 1.5 kHz (-8 dB) + above 5 kHz (-4 dB), wire decay x0.6, glide x0.3, attack x0.7.
 Each layer has +/-0.7 dB random level scatter so no two files are volume copies."""

    readme=f"""ZC SNARE EXTRACT v3.0 - {band} - "{song}" (mixed by {mixer})
=====================================================================
All files: 48 kHz / 24-bit stereo WAV, trimmed to the stick hit, peak-normalised as a set (loudest hard hit = -1 dBFS).

WHAT THESE ARE
Real snare hits lifted off the record. Nothing is synthesised, nothing is EQ'd, no averaging in the audible part.
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
 4. Each file is ONE real hit, full length, with its own transient, body, wires and reverb as it sits on the record.
    The real tail is used for as long as it stays 6 dB above the background measured 20..5 ms before that same hit
    (previous tails, cymbal wash, bleed). Below that level the hit is inaudible under the record anyway; that remainder
    is continued per band with the hit's own late texture at the decay rate measured on this song (ESTIMATE, see below)
    and the file ends where the level is under -88 dBFS. Hits were picked for long clean air before the next snare,
    low background, typical envelope and no coincident kick (40-120 Hz excess test).
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
""" + "\n".join(f"  {h.get('layer',['hard','medium','soft','ghost'][i//4])} rr{i%4+1}: t={h['t']} s, gap {h['gap_ms']} ms, bg {h['bg_rel_peak_db']} dB, real to {h['real_to_ms'] if h['real_to_ms'] else 'end'} ms, len {h['len_ms']} ms" + (f", rel {h['rel_db']} dB {'REAL' if h.get('real') else 'ESTIMATE'}" if info.get('real_velocity') else '') for i,h in enumerate(sel))
    with zipfile.ZipFile(f'ZC_Snare_{n}_RoundRobins.zip','w',zipfile.ZIP_STORED) as z:
        for lay in ['ghost','soft','medium','hard']:
            for i in range(1,5): z.write(f'pack2/{n}/ZC_{n}_{lay}_rr{i}.wav',f'ZC_{n}_{lay}_rr{i}.wav')
        z.writestr('README.txt',readme)
    open(f'pack2/{n}/README.txt','w').write(readme); print(n, os.path.getsize(f'ZC_Snare_{n}_RoundRobins.zip')//1024,'KB')
# Full HTML with embedded FLACs
