# Collective snare library

Every song that produces a pack writes `packs/<job>/profile.json` (its measured fingerprint: separation residual,
hit count and alignment correlation, level spread, coherent residual, hat-vs-snare per band, tilt, T60 per band,
noise floor, real-velocity layer counts, input codec/bitrate, and the detection strategy that held).

`pipeline/library.py` loads every OK profile at run time. A new song is placed against the library before the build
(nearest reference by normalised distance), that reference's winning strategy is tried first, and the other recipes
in `STRATEGIES` follow as fallbacks before a FAIL is allowed. After the build the song's own profile is compared to
the library ranges feature by feature; anything outside the range is written into the report as a library note.

This is a calibration database plus strategy selection with fallbacks. It is not a trained model: nothing in the
separation (Demucs htdemucs -> MDX23C DrumSep) changes per song; what adapts is hit detection, alignment floor and
the hat-bleed QC limit, and the gates still have fixed physical floors (snare lost to the unassigned residual <= 1 dB,
corr >= 0.70, >= 60 hits, noise floor < -60 dBFS).
