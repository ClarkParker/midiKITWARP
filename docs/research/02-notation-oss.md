# Dossier 02 — Notation & OSS percussion vocabularies (MuseScore, Hydrogen, LilyPond, SMuFL)

Target: KITWARP pivot vocabulary design.
Date: 2026-09-06. All facts below were extracted from local clones made on that date.

---

## 1. Scope and method

### 1.1 What was fetched

| Source | Method | Local path | Ref |
|---|---|---|---|
| LilyPond | `git clone --depth 1 https://github.com/lilypond/lilypond.git` | `scratch:repos/lilypond` | master @ 2026-09-06 |
| Hydrogen | `git clone --depth 1 https://github.com/hydrogen-music/hydrogen.git` | `scratch:repos/hydrogen` | master @ 2026-09-06 |
| MuseScore Studio | `git clone --depth 1 --filter=blob:none --no-checkout` + sparse-checkout | `scratch:repos/MuseScore` | master @ 2026-09-06 |
| SMuFL (W3C) | `git clone --depth 1 https://github.com/w3c/smufl.git` | `scratch:repos/smufl` | master @ 2026-09-06 |

Files actually read (repo-relative):

- LilyPond: `ly/drumpitch-init.ly`, `Documentation/en/notation/percussion.itely`, `Documentation/en/notation/notation-appendices.itely`, `COPYING`
- Hydrogen: `data/xsd/drumkit_map.xsd`, `data/xsd/drumkit.xsd`, `data/drumkit_maps/*.h2map` (54 files), `data/drumkits/GMRockKit/drumkit.xml`, `data/drumkits/TR808EmulationKit/drumkit.xml`, `src/tests/data/drumkits/legacy_GMkit/drumkit.xml`, `src/core/Basics/DrumkitMap.h`, `src/core/SoundLibrary/SoundLibraryDatabase.cpp`, `docs/proposals/0002-drumkit-independent-patterns_v2.md`, `COPYING`
- MuseScore: `src/engraving/dom/drumset.cpp`, `src/engraving/dom/drumset.h`, `src/engraving/types/types.h`, `src/engraving/types/typesconv.cpp`, `share/instruments/instruments.xml`, `share/instruments/README.md`, `share/templates/*.drm` (6 files), `LICENSE.txt`
- SMuFL: `metadata/ranges.json`, `metadata/glyphnames.json`, `README.md`, `w3c.json`

### 1.2 What could not be obtained, and why

- `curl` to `github.com` / `raw.githubusercontent.com` is blocked by egress policy (403) in this environment; everything was obtained by `git clone` instead. No fact in this dossier depends on a blocked fetch.
- MuseScore's **authoritative** instrument data lives in a Google Sheets spreadsheet (`share/instruments/README.md` names it); `instruments.xml` and `drumset.cpp` are generated from it. The spreadsheet itself was not opened. The generated files in the repo are the artefacts used here, and they are the ones MuseScore actually ships. **UNVERIFIED:** whether the spreadsheet holds additional percussion columns not emitted into `instruments.xml`.
- MuseScore Drumline (MDL) is a separate, non-GPL-repo extension. Its drumsets are not in this repo; only the `share/templates/Marching_*.drm` files and the `marching-*` entries of `instruments.xml` were available. Notes 88–102 named in `typesconv.cpp` (`Snare (Rim shot)`, `Ride (Edge)`, `Cowbell Low`, `Cowbell High`) have no entry in the built-in drumset — **UNVERIFIED** which shipped file consumes them.
- SMuFL: no `LICENSE` file exists in the repo (see §5).
- LilyPond `scm/drums.scm` **does not exist**; the file named in the task brief is `ly/drumpitch-init.ly` (confirmed by `find`). All three LilyPond tables are in that one file.

---

## 2. Extracted vocabularies

### 2.1 LilyPond — `ly/drumpitch-init.ly` (GPL-3.0-or-later)

LilyPond splits the problem into **three independent tables**. This is the single most important architectural fact in this dossier.

| Table | Maps | Cardinality |
|---|---|---|
| `drumPitchNames` | input token (incl. abbreviations/aliases) → **notation symbol** | 129 tokens → 65 symbols |
| `drumStyleTable` (6 named styles) | notation symbol → (notehead, articulation script, staff line) | per-style subsets |
| `midiDrumPitches` / `drumPitchTable` | notation symbol → **MIDI pitch** | 64 symbols → 47 distinct notes |

The identity axis (symbol), the rendering axis (style table), and the MIDI axis (pitch table) are **separately overridable**. `Documentation/en/notation/percussion.itely` (lines 529–615) documents user extension of all three, with a worked djembe example that adds six symbols (`dbass`, `dbassmute`, `dopen`, `dopenmute`, `dslap`, `dslapmute`) plus abbreviations — i.e. the vocabulary is designed to be *extended by third parties without forking*.

#### 2.1.1 Complete `midiDrumPitches` table (64 symbols, MIDI note computed from `ly:make-pitch`)

MIDI note = `60 + 12·octave + [0,2,4,5,7,9,11][notename] + alteration_in_semitones`, verified against GM (e.g. `acousticbassdrum` → 35).

| MIDI | Symbol | Abbreviation |
|---|---|---|
| 35 | `acousticbassdrum` | `bda` |
| 36 | `bassdrum` | `bd` |
| 37 | `hisidestick` | `ssh` |
| 37 | `sidestick` | `ss` |
| 37 | `losidestick` | `ssl` |
| 38 | `acousticsnare` | `sna` |
| 38 | `snare` | `sn` |
| 39 | `handclap` | `hc` |
| 40 | `electricsnare` | `sne` |
| 41 | `lowfloortom` | `tomfl` |
| 42 | `closedhihat` | `hhc` |
| 42 | `hihat` | `hh` |
| 43 | `highfloortom` | `tomfh` |
| 44 | `pedalhihat` | `hhp` |
| 44 | `splashhihat` | `hhs` |
| 45 | `lowtom` | `toml` |
| 46 | `openhihat` | `hho` |
| 46 | `halfopenhihat` | `hhho` |
| 47 | `lowmidtom` | `tomml` |
| 48 | `himidtom` | `tommh` |
| 49 | `crashcymbala` | `cymca` |
| 49 | `crashcymbal` | `cymc` |
| 50 | `hightom` | `tomh` |
| 51 | `ridecymbala` | `cymra` |
| 51 | `ridecymbal` | `cymr` |
| 52 | `chinesecymbal` | `cymch` |
| 53 | `ridebell` | `rb` |
| 54 | `tambourine` | `tamb` |
| 55 | `splashcymbal` | `cyms` |
| 56 | `cowbell` | `cb` |
| 57 | `crashcymbalb` | `cymcb` |
| 58 | `vibraslap` | `vibs` |
| 59 | `ridecymbalb` | `cymrb` |
| 60 | `mutehibongo` | `bohm` |
| 60 | `hibongo` | `boh` |
| 60 | `openhibongo` | `boho` |
| 61 | `mutelobongo` | `bolm` |
| 61 | `lobongo` | `bol` |
| 61 | `openlobongo` | `bolo` |
| 62 | `mutehiconga` | `cghm` |
| 62 | `muteloconga` | `cglm` |
| 63 | `openhiconga` | `cgho` |
| 63 | `hiconga` | `cgh` |
| 64 | `openloconga` | `cglo` |
| 64 | `loconga` | `cgl` |
| 65 | `hitimbale` | `timh` |
| 66 | `lotimbale` | `timl` |
| 67 | `hiagogo` | `agh` |
| 68 | `loagogo` | `agl` |
| 69 | `cabasa` | `cab` |
| 70 | `maracas` | `mar` |
| 71 | `shortwhistle` | `whs` |
| 72 | `longwhistle` | `whl` |
| 73 | `shortguiro` | `guis` |
| 74 | `longguiro` | `guil` |
| 74 | `guiro` | `gui` |
| 75 | `claves` | `cl` |
| 76 | `hiwoodblock` | `wbh` |
| 77 | `lowoodblock` | `wbl` |
| 78 | `mutecuica` | `cuim` |
| 79 | `opencuica` | `cuio` |
| 80 | `mutetriangle` | `trim` |
| 81 | `triangle` | `tri` |
| 81 | `opentriangle` | `trio` |
`tamtam` (abbrev. `tt`) is present in `drumPitchNames` as an alias target but has **no `midiDrumPitches` entry and no `drumPitchNames` self-entry** — a notation-only symbol with no sound. It is the one documented case where LilyPond's notation vocabulary exceeds its MIDI vocabulary.

#### 2.1.2 Name collisions — LilyPond's 64 symbols collapse onto 47 GM notes

Exactly the lossiness KITWARP must avoid. These are **distinct notation identities that GM cannot round-trip**:

| MIDI | Symbols sharing it |
|---|---|
| 37 | `hisidestick`, `sidestick`, `losidestick` |
| 38 | `acousticsnare`, `snare` |
| 42 | `closedhihat`, `hihat` |
| 44 | `pedalhihat`, `splashhihat` |
| 46 | `openhihat`, `halfopenhihat` |
| 49 | `crashcymbala`, `crashcymbal` |
| 51 | `ridecymbala`, `ridecymbal` |
| 60 | `mutehibongo`, `hibongo`, `openhibongo` |
| 61 | `mutelobongo`, `lobongo`, `openlobongo` |
| 62 | `mutehiconga`, `muteloconga` |
| 63 | `openhiconga`, `hiconga` |
| 64 | `openloconga`, `loconga` |
| 74 | `longguiro`, `guiro` |
| 81 | `triangle`, `opentriangle` |

Note the pathological pair at 62: `mutehiconga` and `mute**lo**conga` — a *pitch/instance* distinction, not an articulation one, silently merged.

#### 2.1.3 The six `drumStyleTable` styles

`drums-style` (30 symbols), `agostini-drums-style` (30), `timbales-style` (5), `congas-style` (8), `bongos-style` (8), `percussion-style` (12), `weinberg-drums-style` (22). Source comment cites **Norman Weinberg, "Guidelines for Drumset Notation", Percussive Notes, June 1994, pp. 15–26** as the authority for the last one.

Articulation scripts used in the style tables (the third field) form a small closed vocabulary:

`#f` (none) · `stopped` · `open` · `(open . UP)` · `(open . DOWN)` · `halfopen` · `staccato` · `tenuto`

Noteheads used (second field): `()` (normal) · `cross` · `xcircle` · `triangle` · `diamond` · `mensural` · `mi`

`splashhihat` is notated *below* the staff with `(open . DOWN)` — i.e. LilyPond models "hi-hat splash / foot-splash" as a **left-foot** event distinct from `pedalhihat` even though both sound MIDI 44.

---

### 2.2 MuseScore Studio (GPL-3.0-only)

#### 2.2.1 Built-in "standard MIDI drumset" — `src/engraving/dom/drumset.cpp`, `Drumset::initDrumset()`

61 entries, MIDI notes **27–87** (GM2 extended range, not GM's 35–81). Display names come from `TConv::userName(DrumNum(n))`, table at `src/engraving/types/typesconv.cpp:3038+`. `DRUM_INSTRUMENTS = 128` (`drumset.h:92`) — the array is the full MIDI note range.

Every entry in the current built-in drumset has `stemDirection = UP`, `voice = 0` and **an empty shortcut** (61/61 `String()`); voices/stems/shortcuts are supplied instead by `instruments.xml` (§2.2.2). `panelRow,panelColumn` are the MuseScore 4 Percussion Panel grid coordinates (8 columns).

| MIDI | Name | Notehead (custom SMuFL glyph) | Line | Stem | Voice | Panel r,c |
|---|---|---|---|---|---|---|
| 27 | High Q | SLASH | 8 | UP | 0 | 0,0 |
| 28 | Slap | CUSTOM (noteheadSlashX) | 4 | UP | 0 | 0,1 |
| 29 | Scratch Push | SLASH | 6 | UP | 0 | 0,2 |
| 30 | Scratch Pull | SLASH | 6 | UP | 0 | 0,3 |
| 31 | Sticks | PLUS | -1 | UP | 0 | 0,4 |
| 32 | Square Click | PLUS | 10 | UP | 0 | 0,5 |
| 33 | Metronome Click | CROSS | 10 | UP | 0 | 0,6 |
| 34 | Metronome Bell | TRIANGLE_UP | 10 | UP | 0 | 0,7 |
| 35 | Acoustic Bass Drum | NORMAL | 8 | UP | 1 | 1,0 |
| 36 | Bass Drum 1 | NORMAL | 7 | DOWN | 1 | 1,1 |
| 37 | Side Stick | SLASHED1 | 3 | UP | 0 | 1,2 |
| 38 | Acoustic Snare | NORMAL | 3 | UP | 0 | 1,3 |
| 39 | Hand Clap | PLUS | -2 | UP | 0 | 1,4 |
| 40 | Electric Snare | SLASH | 3 | UP | 0 | 1,5 |
| 41 | Low Floor Tom | NORMAL | 6 | UP | 0 | 1,6 |
| 42 | Closed Hi-Hat | CROSS | -1 | UP | 0 | 1,7 |
| 43 | High Floor Tom | NORMAL | 5 | UP | 0 | 2,0 |
| 44 | Pedal Hi-Hat | CROSS | 9 | UP | 1 | 2,1 |
| 45 | Low Tom | NORMAL | 4 | UP | 0 | 2,2 |
| 46 | Open Hi-Hat | XCIRCLE | -1 | UP | 0 | 2,3 |
| 47 | Low-Mid Tom | NORMAL | 2 | UP | 0 | 2,4 |
| 48 | Hi-Mid Tom | NORMAL | 1 | UP | 0 | 2,5 |
| 49 | Crash Cymbal 1 | CROSS | -2 | UP | 0 | 2,6 |
| 50 | High Tom | NORMAL | 0 | UP | 0 | 2,7 |
| 51 | Ride Cymbal 1 | CROSS | 0 | UP | 0 | 3,0 |
| 52 | Chinese Cymbal | CUSTOM (noteheadHeavyXHat) | -3 | UP | 0 | 3,1 |
| 53 | Ride Bell | DIAMOND | 0 | UP | 0 | 3,2 |
| 54 | Tambourine | DIAMOND | 6 | UP | 0 | 3,3 |
| 55 | Splash Cymbal | CROSS | -4 | UP | 0 | 3,4 |
| 56 | Cowbell | TRIANGLE_DOWN | 0 | UP | 0 | 3,5 |
| 57 | Crash Cymbal 2 | CROSS | -3 | UP | 0 | 3,6 |
| 58 | Vibraslap | TI | 0 | UP | 0 | 3,7 |
| 59 | Ride Cymbal 2 | CROSS | 2 | UP | 0 | 4,0 |
| 60 | Hi Bongo | NORMAL | -1 | UP | 0 | 4,1 |
| 61 | Low Bongo | NORMAL | 0 | UP | 0 | 4,2 |
| 62 | Mute Hi Conga | CUSTOM (noteheadXOrnate) | 1 | UP | 0 | 4,3 |
| 63 | Open Hi Conga | NORMAL | 1 | UP | 0 | 4,4 |
| 64 | Low Conga | NORMAL | 2 | UP | 0 | 4,5 |
| 65 | High Timbale | NORMAL | 5 | UP | 0 | 4,6 |
| 66 | Low Timbale | NORMAL | 7 | UP | 0 | 4,7 |
| 67 | High Agogo | TRIANGLE_DOWN | -2 | UP | 0 | 5,0 |
| 68 | Low Agogo | TRIANGLE_DOWN | -1 | UP | 0 | 5,1 |
| 69 | Cabasa | DIAMOND | 2 | UP | 0 | 5,2 |
| 70 | Maracas | DIAMOND | 4 | UP | 0 | 5,3 |
| 71 | Short Whistle | CROSS | -3 | UP | 0 | 5,4 |
| 72 | Long Whistle | TI | -3 | UP | 0 | 5,5 |
| 73 | Short Güiro | CROSS | -1 | UP | 0 | 5,6 |
| 74 | Long Güiro | SLASHED1 | -1 | UP | 0 | 5,7 |
| 75 | Claves | LA | 0 | UP | 0 | 6,0 |
| 76 | Hi Wood Block | LA | 5 | UP | 0 | 6,1 |
| 77 | Low Wood Block | LA | 7 | UP | 0 | 6,2 |
| 78 | Mute Cuica | CROSS | 8 | UP | 0 | 6,3 |
| 79 | Open Cuica | SLASHED2 | 8 | UP | 0 | 6,4 |
| 80 | Mute Triangle | CROSS | 0 | UP | 0 | 6,5 |
| 81 | Open Triangle | TRIANGLE_UP | 0 | UP | 0 | 6,6 |
| 82 | Shaker | DIAMOND | 5 | UP | 0 | 6,7 |
| 83 | Sleigh Bell | TRIANGLE_DOWN | 3 | UP | 0 | 7,0 |
| 84 | Mark Tree | TI | 2 | UP | 0 | 7,1 |
| 85 | Castanets | LA | 2 | UP | 0 | 7,2 |
| 86 | Mute Surdo | CUSTOM (noteheadSlashX) | 4 | UP | 0 | 7,3 |
| 87 | Open Surdo | SLASH | 4 | UP | 0 | 7,4 |
Names defined in `typesconv.cpp` but **absent from the built-in drumset** (extension notes): 91 `Snare (Rim shot)`, 93 `Ride (Edge)`, 99 `Cowbell Low`, 102 `Cowbell High`.

#### 2.2.2 `share/instruments/instruments.xml` — 287 `<Drum>` entries across 107 instruments

`<Drum pitch="N">` child elements actually used, with occurrence counts across all 287:
`name` 287 · `head` 287 · `line` 287 · `voice` 287 · `panelRow` 287 · `panelColumn` 287 · `stem` 263 · `shortcut` 195 · `noteheads` 9 (`quarter`/`half`/`whole`/`breve` SMuFL glyph names).

`head` values (string enum, `TConv::fromXml` → `NoteHeadGroup`): `normal`, `cross`, `plus`, `xcircle`, `triangle-up`, `triangle-down`, `slashed1`, `slashed2`, `diamond`, `slash`, `la`, `ti`, `mi`, plus `<noteheads>` for arbitrary SMuFL glyph override.

**The four drum-kit presets** (this is MuseScore's own "what is a drum kit" answer, at three sizes):

`drumset` (23 notes) — 35 Bass Drum 2 · 36 Bass Drum 1 · 37 Side Stick · 38 Acoustic Snare · 40 Electric Snare · 41 Low Floor Tom · 42 Closed Hi-Hat · 43 High Floor Tom · 44 Pedal Hi-Hat · 45 Low Tom · 46 Open Hi-Hat · 47 Low-Mid Tom · 48 Hi-Mid Tom · 49 Crash Cymbal 1 · 50 High Tom · 51 Ride Cymbal 1 · 52 China Cymbal · 53 Ride Bell · 54 Tambourine · 55 Splash Cymbal · 56 Cowbell · 57 Crash Cymbal 2 · 59 Ride Cymbal 2

`drum-kit-4` (11) — 36 Bass Drum · 37 **Cross-stick** · 38 Snare · 41 Floor Tom · 42 Closed Hi-Hat · 44 Pedal Hi-Hat · 46 Open Hi-Hat · 49 Crash Cymbal · 50 **Tom** · 51 Ride Cymbal · 53 Ride Bell

`drum-kit-5` (16) — adds 35 Bass Drum 2, 47 Low Tom, 50 High Tom, 52 China Cymbal, 55 Splash Cymbal, 57 Crash Cymbal 2

`percussion` (42) — **remaps hi-hat and ride out of the GM range**: 27 Closed Hi-Hat · 28 Pedal Hi-Hat · 29 Open Hi-Hat · 30 Ride Cymbal · 31 Stick Click · 36 Bass Drum · 37 **Snare Rim** · 38 Snare · 54 Tambourine · 55 Splash Cymbal · 56 Cowbell · 57 **Suspended Cymbal** · 58 Vibraslap · 59 **Hand Cymbals** · 60–87 as GM percussion.

Small single-instrument drumsets (the "instrument = a few articulations" pattern):

| Instrument id | Entries |
|---|---|
| `hi-hat` | 42 Closed Hi-Hat, 44 Pedal Hi-Hat, 46 Open Hi-Hat |
| `ride-cymbal` | 51 Ride Cymbal, 53 Ride Bell |
| `snare-drum` | 37 Side Stick, 38 Snare |
| `military-drum` | 37 Side Stick, 38 Snare |
| `piccolo-snare-drum` | 37 Side Stick, **40** Snare |
| `tom-toms` | 41 Tom 6, 43 Tom 5, 45 Tom 4, 47 Tom 3, 48 Tom 2, 50 Tom 1 (**ordinal, high number = low drum**) |
| `bongos` | 60 High Bongo, 61 Low Bongo |
| `congas` | 62 Mute High Conga, 63 High Conga, 64 Low Conga |
| `timbales` | 65 High Timbale, 66 Low Timbale |
| `agogo-bells` | 68 Low Agogô, 67 High Agogô |
| `triangle` | 80 Mute Triangle, 81 Open Triangle |
| `guiro` | 73 Short Güiro, 74 Long Güiro |
| `cuica` | 78 Mute Cuica, 79 Open Cuica |
| `wood-blocks` | 76 High Wood Block, 77 Low Wood Block |
| `temple-blocks` | 58 Low, 59 Low-Mid, 60 Mid, 61 High-Mid, 62 High Temple Block |
| `log-drum` | 58 Low Sound, 59 Low-Mid, 60 Mid, 61 High-Mid, 62 High Sound |
| `djembe` / `doumbek` | 62 **Slap**, 63 **Open**, 64 **Bass** |
| `tablas` | 62 High Tabla, 64 Low Tabla |
| `taiko` | 86 Taiko Mute, 87 Taiko |
| `cajon` | 38 Hit |
| `tubo` | 62 Mute High Conga, 63 High Conga, 64 Low Conga (**mislabelled reuse of conga names**) |
| `shekere` | 82 Shake |
| `bell-tree`, `mark-tree` | 84 **Glissando Down** |

Marching (MuseScore Drumline conventions, **all outside GM**):

- `marching-snare` (11): 48 Buzz · 50 Battery Snare · 52 Rim Shot · 53 Rim Click · 55 Stick Click · 57 Stick Shot · 59 **Shell** · 60 **Backstick** · 72 Ride Cymbal 1 · 74 Open Hi-Hat · 76 Closed Hi-Hat
- `marching-tenor-drums` (25): `Drum 1..4` and `Spock 1..2`, each × {plain, `Rim`, `Buzz`, `Muted`, `Shell`}, + 43 Stick Click
- `marching-bass-drums` (11): `Drum 1..5` × {plain, `Rim`} + 90 `Unison`
- `marching-cymbals` (13): 72 Full Crash · 74 Half Crash · 76 Hi-Hat · 77 Sizzle · 79 **Crash-Choke** · 81 Tap · 83 **Tap-Choke** · 84 Bell Tap · 86 **Bell Tap-Choke** · 88 Muted Tap · 89 Smash · 91 Zing · 93 Roll

#### 2.2.3 `share/templates/*.drm` (6 shipped drumset files)

`Marching_Snare_Drums.drm` (9): 49 Ping Shot · 50 Hit · 51 Rim Shot · 52 **Gok Shot** · 53 Rim · 55 Stick click · 56 Cross Stick · 57 Stick Shot · 60 Back Stick.
`Marching_Cymbals.drm` (8): 72 Crash · 76 **Crunch (HH)** · 77 Sizzle · 79 **Punch** · 81 Tap · 84 Ting · 89 **Suc** · 91 Zing.
`Marching_Bass_Drums.drm` (18): `Drum 1..5` × {Hits, Rims, Rimshots} + Unison Hits/Rims/Rimshots.
`Marching_Tenors.drm` (22): `Drum 1..4` + `Spock 1..2`, × {plain, Shot, Rim, Shell}.
`orchestral.drm` (12): note the *non-GM* hi-hat block 27/28/29 (Closed/Pedal/Open), 35+36 both "Concert Bass Drum", 38+40 both "Concert Snare Drum", 57 Concert Cymbal 2, 59 Concert Cymbal 1.
`drumset_fr.drm` (25): a French-localised GM kit. **UNVERIFIED:** its `<head>` values are *numeric* (0,1,3,5,6,7) from a legacy `NoteHeadGroup` enum ordering; the current reader parses `head` as a string via `TConv::fromXml` with fallback `HEAD_NORMAL`, so these legacy numeric codes very likely all fall back to `normal` today. Do not treat `drumset_fr.drm` noteheads as authoritative.

Shortcuts (keyboard letters) in the shipped kits are positional, not semantic: `drumset` uses A=BD1, B=Acoustic Snare, C=Closed HH, D=Open HH, E=Crash 1, F=Ride 1, G=Hi-Mid Tom, H=High Floor Tom.

#### 2.2.4 MuseScore's articulation-variant mechanism (`drumset.cpp:180–195`, `drumset.h:38`)

The `.drm`/instruments schema supports:

```xml
<Drum pitch="38">
  <variants>
    <variant pitch="N"><articulation>NAME</articulation><tremolo>TYPE</tremolo></variant>
  </variants>
</Drum>
```

i.e. **one notated drum can resolve to a different MIDI pitch depending on an articulation name and/or a tremolo type**. `Drumset::varPitch` (`drumset.cpp:289–291`) matches `a->articulationName() == v.articulationName`. **No shipped MuseScore file uses `<variants>`** (0 occurrences in `instruments.xml` and all six `.drm`); it exists for the MuseScore Drumline extension. This is a direct precedent for a KITWARP `(pivot-id, articulation-modifier) → note` resolution step.

---

### 2.3 Hydrogen (GPL-2.0-or-later)

Hydrogen is the closest existing analogue to KITWARP: since the "drumkit-independent patterns" work it maps every kit instrument to a **pivot string called an "instrument type"**, and remaps patterns through it when kits are swapped.

#### 2.3.1 The data model

`src/core/Basics/DrumkitMap.h`:

> `DrumkitMap` defines a 1:1 mapping of all `Instrument` of a `Drumkit` to general type strings. By relating two maps using the general type as keys we can load another `Drumkit` or import a `Pattern` without distorting the pattern's content or any other loss of information.
> `Instrument IDs are defined in each individual drumkit while the type strings are arbitrary strings using which instruments of different kits can be mapped onto each other.`

`data/xsd/drumkit_map.xsd` — the entire `.h2map` schema:

```xml
<mapping><instrumentID>int</instrumentID><type>string</type></mapping>
<drumkit_map><formatVersion>uint</formatVersion> mapping* </drumkit_map>
```

`data/xsd/drumkit.xsd:104` — inside `<instrument>`: `<type>` is `xsd:string`, `minOccurs="0"`. Separate from `<name>` (display) and `<id>` (kit-local index). `nCurrentFormatVersion = 2`.

#### 2.3.2 The governance decision — and why it went wrong

`docs/proposals/0002-drumkit-independent-patterns_v2.md` (status: implemented, 2024-07-26), §"Instrument types":

> "The particular strings we use as instrument types **are not formally defined in this design**. This makes it easy to support arbitrary kits, allows for easy customization, but **probably will also result in some mismatches**. […] the user will also be able to set them to arbitrary strings. This way we are not the single source of truth."

The GUI's "possible choices" are not a controlled list: `DrumkitPropertiesDialog.cpp:731-732` builds them as `SoundLibraryDatabase::getAllTypes()` ∪ `m_pDrumkit->getAllTypes()` — i.e. **the union of whatever strings happen to be installed**. The consequences are visible in the shipped data (§2.3.3): 219 distinct strings for what is functionally ~35 instruments.

#### 2.3.3 Complete instrument-type vocabulary across the 54 shipped `.h2map` files

54 files, 1330 instrument→type mappings, **219 distinct type strings**. (Count = number of kits using that exact string.)

| Type string | Kits |
|---|---|
| `Agogo High` | 6 |
| `Agogo Low` | 5 |
| `Bell Tree Down` | 2 |
| `Bell Tree Up` | 2 |
| `Bongo High` | 5 |
| `Bongo High 2` | 1 |
| `Bongo High 3` | 1 |
| `Bongo Low` | 6 |
| `Bongo Low 2` | 1 |
| `Bongo Low 3` | 1 |
| `Bucket` | 1 |
| `Cabasa Cut` | 1 |
| `Cabasa Down` | 1 |
| `Cabasa Up` | 4 |
| `Cajon Slap` | 2 |
| `Cajon Slap 2` | 1 |
| `Cajon Thumb` | 2 |
| `China` | 12 |
| `China 2` | 3 |
| `China 3` | 1 |
| `China 4` | 1 |
| `China 5` | 1 |
| `China 6` | 1 |
| `China 7` | 1 |
| `China 8` | 1 |
| `China 9` | 1 |
| `China Bell` | 1 |
| `Claves` | 6 |
| `Conga High` | 12 |
| `Conga High 2` | 7 |
| `Conga High 3` | 3 |
| `Conga High Mute` | 3 |
| `Conga High Mute 2` | 1 |
| `Conga Low` | 11 |
| `Conga Low 2` | 5 |
| `Conga Low Mute 2` | 1 |
| `Conga Slap` | 1 |
| `Cowbell` | 30 |
| `Cowbell 10` | 1 |
| `Cowbell 11` | 1 |
| `Cowbell 12` | 1 |
| `Cowbell 13` | 1 |
| `Cowbell 14` | 1 |
| `Cowbell 2` | 5 |
| `Cowbell 3` | 3 |
| `Cowbell 4` | 1 |
| `Cowbell 5` | 1 |
| `Cowbell 6` | 1 |
| `Cowbell 7` | 1 |
| `Cowbell 8` | 1 |
| `Cowbell 9` | 1 |
| `Crash` | 43 |
| `Crash 2` | 31 |
| `Crash 3` | 10 |
| `Crash 4` | 6 |
| `Crash 5` | 2 |
| `Crash 6` | 1 |
| `Crash 7` | 1 |
| `Crash 8` | 1 |
| `Crash 9` | 1 |
| `Crash Bell` | 2 |
| `Crash Bow` | 2 |
| `Crash Choke` | 5 |
| `Crash Choke 2` | 6 |
| `Crash Flink` | 1 |
| `Djembe Bass` | 1 |
| `Djembe Bass 2` | 1 |
| `Djembe Bass 3` | 1 |
| `Djembe Bass 4` | 1 |
| `Djembe Bass 5` | 1 |
| `Djembe Slap` | 1 |
| `Djembe Slap 2` | 1 |
| `Djembe Slap 3` | 1 |
| `Djembe Slap 4` | 1 |
| `Djembe Slap 5` | 1 |
| `Djembe Tone` | 1 |
| `Djembe Tone 2` | 1 |
| `Djembe Tone 3` | 1 |
| `Djembe Tone 4` | 1 |
| `Djembe Tone 5` | 1 |
| `Dununba Bell` | 1 |
| `Dununba Bell Mute` | 1 |
| `Dununba Head` | 1 |
| `Dununba Head Mute` | 1 |
| `Finger Snap` | 2 |
| `Foot Stomp` | 1 |
| `Gong` | 1 |
| `Guiro Long` | 4 |
| `Guiro Long 2` | 1 |
| `Guiro Long 3` | 1 |
| `Guiro Short` | 1 |
| `Guiro Short 2` | 1 |
| `Guiro Short 3` | 1 |
| `Hand Clap` | 31 |
| `Hand Clap 2` | 8 |
| `Hand Clap 3` | 4 |
| `Hi-hat Closed` | 50 |
| `Hi-hat Closed 2` | 18 |
| `Hi-hat Closed 3` | 9 |
| `Hi-hat Closed 4` | 4 |
| `Hi-hat Closed 5` | 1 |
| `Hi-hat Open` | 43 |
| `Hi-hat Open 2` | 15 |
| `Hi-hat Open 3` | 5 |
| `Hi-hat Open 4` | 1 |
| `Hi-hat Open 5` | 1 |
| `Hi-hat Open 6` | 1 |
| `Hi-hat Open Choke` | 2 |
| `Hi-hat Pedal` | 29 |
| `Hi-hat Pedal 2` | 4 |
| `Hi-hat Semi-Open` | 11 |
| `Hi-hat Swish` | 6 |
| `Kenkeni Bell` | 1 |
| `Kenkeni Bell Mute` | 1 |
| `Kenkeni Head` | 1 |
| `Kenkeni Head Mute` | 1 |
| `Kick` | 50 |
| `Kick 10` | 1 |
| `Kick 11` | 1 |
| `Kick 12` | 1 |
| `Kick 2` | 25 |
| `Kick 3` | 17 |
| `Kick 4` | 12 |
| `Kick 5` | 8 |
| `Kick 6` | 6 |
| `Kick 7` | 2 |
| `Kick 8` | 2 |
| `Kick 9` | 1 |
| `Maracas` | 10 |
| `Ride Bell` | 27 |
| `Ride Bell 2` | 2 |
| `Ride Bell 3` | 1 |
| `Ride Bow` | 34 |
| `Ride Bow 2` | 13 |
| `Ride Bow 3` | 4 |
| `Ride Choke` | 4 |
| `Ride Flink` | 1 |
| `Ride Side` | 5 |
| `Ride Side 2` | 1 |
| `Sangban Bell` | 1 |
| `Sangban Bell Mute` | 1 |
| `Sangban Head` | 1 |
| `Sangban Head Mute` | 1 |
| `Shaker` | 7 |
| `Shaker 2` | 1 |
| `Snare` | 49 |
| `Snare 2` | 32 |
| `Snare 3` | 20 |
| `Snare 4` | 13 |
| `Snare 5` | 7 |
| `Snare 6` | 6 |
| `Snare Flam` | 2 |
| `Snare Rimshot` | 25 |
| `Snare Rimshot 2` | 10 |
| `Snare Rimshot 3` | 1 |
| `Snare Roll` | 5 |
| `Snare Roll 2` | 1 |
| `Splash` | 15 |
| `Splash 2` | 4 |
| `Splash 3` | 2 |
| `Splash 4` | 1 |
| `Splash Choke` | 2 |
| `Stick` | 24 |
| `Stick 2` | 11 |
| `Stick 3` | 2 |
| `Stick 4` | 1 |
| `Tambourine` | 13 |
| `Tambourine Mute` | 2 |
| `Thunder Tube` | 1 |
| `Thunder Tube 2` | 1 |
| `Timbale High` | 7 |
| `Timbale High 2` | 1 |
| `Timbale High 3` | 1 |
| `Timbale High 4` | 1 |
| `Timbale High Roll` | 1 |
| `Timbale High Roll 2` | 1 |
| `Timbale Low` | 6 |
| `Tom Floor` | 43 |
| `Tom Floor 2` | 8 |
| `Tom Floor Flam` | 1 |
| `Tom Floor Rimshot` | 4 |
| `Tom Floor Roll` | 1 |
| `Tom Floor Roll 2` | 1 |
| `Tom Floor Roll 3` | 1 |
| `Tom High` | 14 |
| `Tom High 2` | 9 |
| `Tom High 3` | 6 |
| `Tom High 4` | 1 |
| `Tom High Roll` | 1 |
| `Tom High Roll 2` | 1 |
| `Tom Low` | 37 |
| `Tom Low 2` | 6 |
| `Tom Low 3` | 1 |
| `Tom Low Flam` | 2 |
| `Tom Low Rimshot` | 2 |
| `Tom Low Roll` | 1 |
| `Tom Low Roll 2` | 1 |
| `Tom Mid` | 43 |
| `Tom Mid 2` | 7 |
| `Tom Mid Flam` | 2 |
| `Tom Mid Rimshot` | 2 |
| `Tom Mid Roll` | 1 |
| `Tom Mid Roll 2` | 1 |
| `Vibra Slap` | 1 |
| `Whistle` | 9 |
| `Whistle 10` | 5 |
| `Whistle 11` | 5 |
| `Whistle 12` | 3 |
| `Whistle 13` | 1 |
| `Whistle 14` | 1 |
| `Whistle 15` | 1 |
| `Whistle 2` | 8 |
| `Whistle 3` | 6 |
| `Whistle 4` | 5 |
| `Whistle 5` | 5 |
| `Whistle 6` | 5 |
| `Whistle 7` | 5 |
| `Whistle 8` | 5 |
| `Whistle 9` | 5 |
#### 2.3.4 Structural decomposition of those 219 strings

The de-facto grammar is `<Instrument> [<Zone|Articulation>] [<ordinal>]`, with no separator and no schema.

Head instruments (count of distinct type strings per head): Tom 26 · Hi-hat 16 · Whistle 15 · Djembe 15 · Crash 14 · Cowbell 14 · Kick 12 · Snare 12 · Ride 10 · China 10 · Conga 9 · Timbale 7 · Bongo 6 · Guiro 6 · Splash 5 · Stick 4 · Dununba 4 · Kenkeni 4 · Sangban 4 · Hand(clap) 3 · Cajon 3 · Cabasa 3 · Tambourine 2 · Shaker 2 · Bell(Tree) 2 · Agogo 2 · Thunder(Tube) 2 · Maracas · Finger(Snap) · Claves · Foot(Stomp) · Bucket · Vibra(Slap) · Gong.

Non-head tokens actually used, with the number of distinct type strings each appears in. This is the de-facto zone/articulation/size vocabulary, and it is flat — nothing in the string says which axis a token belongs to:

`High` 21 · `Low` 15 · `Roll` 13 · `Bell` 11 · `Mute` 10 · `Slap` 9 · `Floor` 7 · `Open` 7 · `Rimshot` 6 · `Mid` 6 · `Head` 6 · `Closed` 5 · `Choke` 5 · `Bass` 5 · `Tone` 5 · `Bow` 4 · `Flam` 4 · `Clap` 3 · `Long` 3 · `Short` 3 · `Pedal` 2 · `Side` 2 · `Tree` 2 · `Down` 2 · `Up` 2 · `Tube` 2 · `Flink` 2 · `Semi-Open` 1 · `Swish` 1 · `Thumb` 1 · `Snap` 1 · `Stomp` 1 · `Cut` 1

Mixed into one flat token space here are: **size/pitch** (`High`, `Low`, `Mid`, `Floor`), **striking zone** (`Bell`, `Bow`, `Side`, `Head`, `Rimshot`), **articulation** (`Mute`, `Open`, `Closed`, `Semi-Open`, `Choke`, `Roll`, `Flam`, `Slap`, `Tone`, `Swish`, `Long`, `Short`), **limb/controller** (`Pedal`), **gesture direction** (`Up`, `Down`, `Cut`), and **instrument-name fragments** (`Clap`, `Snap`, `Stomp`, `Tree`, `Tube`). `Flink` (2) is undocumented — **UNVERIFIED** meaning.

Ordinal suffixes reach absurd depth because the ordinal is overloaded to mean *instance*, *variation*, and *round-robin slot* simultaneously:
`Whistle` up to 15 · `Cowbell` up to 14 · `Kick` up to 12 · `Crash` up to 9 · `China` up to 9 · `Snare` up to 6 · `Hi-hat Open` up to 6 · `Hi-hat Closed` up to 5 · `Splash`/`Stick`/`Tom High`/`Timbale High` up to 4.

Naming inconsistencies visible in the shipped data (each is a real interop failure):
- `Crash Choke` (5 kits) vs `Crash Choke 2` (6 kits) — the "2" variant is *more* common than the base, so ordinal ≠ instance.
- `Hi-hat Semi-Open` (named level) coexists with `Hi-hat Open 2…6` (ordinal levels) — the same axis encoded two ways.
- `Ride Bow` / `Ride Bell` / `Ride Side` / `Ride Choke` (zones) sit in the same slot as `Ride Bow 2` (instance).
- `Crash Bow` / `Crash Bell` exist for crashes but `Crash` alone is the bow hit — zone is optional and therefore ambiguous.
- `Cabasa Up` / `Cabasa Down` / `Cabasa Cut` — a *gesture direction* axis with no other user.
- `Tom Floor Rimshot`, `Tom Low Flam`, `Tom Mid Roll` — articulation applied per tom instance, multiplying the vocabulary.

#### 2.3.5 Shipped kits (`type` → `name` → `midiOutNote`)

`data/drumkits/GMRockKit/drumkit.xml` (18 instruments) — shows type/name/MIDI are three separate things:

| id | type (pivot) | name (display) | midiOutNote |
|---|---|---|---|
| 0 | Kick | Kick | 36 |
| 1 | Stick | Stick | 37 |
| 2 | Snare | Snare | 38 |
| 3 | Hand Clap | Hand Clap | 39 |
| 4 | Snare Rimshot | Snare Rimshot | 40 |
| 5 | Tom Floor | Floor Tom | 41 |
| 6 | Hi-hat Closed | Hat Closed | 42 |
| 7 | Tom Low | Tom 2 | 43 |
| 8 | Hi-hat Pedal | Hat Pedal | 44 |
| 9 | Tom Mid | Tom 1 | 45 |
| 10 | Hi-hat Open | Hat Open | 46 |
| 11 | Cowbell | Cowbell | 56 |
| 12 | Ride Bow | Ride | 51 |
| 13 | Crash | Crash | 49 |
| 14 | Ride Bow 2 | Ride 2 | 59 |
| 15 | Splash | Splash | 55 |
| 16 | **Hi-hat Semi-Open** | Hat Semi-Open | **82** |
| 17 | Ride Bell | Bell | 53 |

Note `Hi-hat Semi-Open` → MIDI **82**, i.e. Hydrogen already has to leave GM to express a third hi-hat openness level, and it lands on GM's "Shaker".

`data/drumkits/TR808EmulationKit/drumkit.xml` (16) — shows the tom-naming trap: types `Tom Floor` / `Tom Low` / `Tom Mid` carry display names `Tom Low` / `Tom Mid` / `Tom Hi`. **The same three drums are named two different ways in one file.**

`src/tests/data/drumkits/legacy_GMkit/drumkit.xml` — pre-type-system kit, `<type>` empty for all 16 instruments, names only (`Snare Jazz`, `Snare Rock`, `Ride Jazz`, `Ride Rock`, `Crash Jazz`). Confirms the retrofit problem: the `.h2map` files exist *only* to back-fill types onto kits that predate the pivot.

---

### 2.4 SMuFL — percussion pictogram glyph names (W3C Music Notation Community Group)

SMuFL is the only source here that gives **stable, machine-readable, versioned identifiers** for percussion instruments and playing techniques, independent of MIDI notes and independent of any one application. Source: `metadata/ranges.json` + `metadata/glyphnames.json` (132 ranges total; 14 are pictogram ranges).

Pictogram ranges and sizes: `beatersPictograms` 128 · `electronicMusicPictograms` 65 · `percussionPlayingTechniquePictograms` 31 · `drumsPictograms` 21 · `tunedMalletPercussionPictograms` 19 · `woodenStruckOrScrapedPercussionPictograms` 13 · `cymbalsPictograms` 11 · `bellsPictograms` 11 · `whistlesAndAerophonesPictograms` 11 · `chimesPictograms` 9 · `shakersOrRattlesPictograms` 9 · `miscellaneousPercussionInstrumentPictograms` 8 · `gongsPictograms` 5 · `metallicStruckPercussionPictograms` 2.

**drumsPictograms** — Drums pictograms, U+E6D0–U+E6EF, 21 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictTimpani` | U+E6D0 | Timpani |
| `pictSnareDrum` | U+E6D1 | Snare drum |
| `pictSnareDrumSnaresOff` | U+E6D2 | Snare drum, snares off |
| `pictSnareDrumMilitary` | U+E6D3 | Military snare drum |
| `pictBassDrum` | U+E6D4 | Bass drum |
| `pictBassDrumOnSide` | U+E6D5 | Bass drum on side |
| `pictTenorDrum` | U+E6D6 | Tenor drum |
| `pictTomTom` | U+E6D7 | Tom-tom |
| `pictTomTomChinese` | U+E6D8 | Chinese tom-tom |
| `pictTomTomJapanese` | U+E6D9 | Japanese tom-tom |
| `pictTomTomIndoAmerican` | U+E6DA | Indo-American tom tom |
| `pictTambourine` | U+E6DB | Tambourine |
| `pictTimbales` | U+E6DC | Timbales |
| `pictBongos` | U+E6DD | Bongos |
| `pictConga` | U+E6DE | Conga |
| `pictLogDrum` | U+E6DF | Log drum |
| `pictSlitDrum` | U+E6E0 | Slit drum |
| `pictBrakeDrum` | U+E6E1 | Brake drum |
| `pictGobletDrum` | U+E6E2 | Goblet drum (djembe, dumbek) |
| `pictTabla` | U+E6E3 | Indian tabla |
| `pictCuica` | U+E6E4 | Cuica |

**cymbalsPictograms** — Cymbals pictograms, U+E720–U+E72F, 11 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictCrashCymbals` | U+E720 | Crash cymbals |
| `pictSuspendedCymbal` | U+E721 | Suspended cymbal |
| `pictHiHat` | U+E722 | Hi-hat |
| `pictHiHatOnStand` | U+E723 | Hi-hat cymbals on stand |
| `pictSizzleCymbal` | U+E724 | Sizzle cymbal |
| `pictVietnameseHat` | U+E725 | Vietnamese hat cymbal |
| `pictChineseCymbal` | U+E726 | Chinese cymbal |
| `pictFingerCymbals` | U+E727 | Finger cymbals |
| `pictCymbalTongs` | U+E728 | Cymbal tongs |
| `pictEdgeOfCymbal` | U+E729 | Edge of cymbal |
| `pictBellOfCymbal` | U+E72A | Bell of cymbal |

**metallicStruckPercussionPictograms** — Metallic struck percussion pictograms, U+E700–U+E70F, 2 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictTriangle` | U+E700 | Triangle |
| `pictAnvil` | U+E701 | Anvil |

**woodenStruckOrScrapedPercussionPictograms** — Wooden struck or scraped percussion pictograms, U+E6F0–U+E6FF, 13 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictWoodBlock` | U+E6F0 | Wood block |
| `pictTempleBlocks` | U+E6F1 | Temple blocks |
| `pictClaves` | U+E6F2 | Claves |
| `pictGuiro` | U+E6F3 | Guiro |
| `pictRatchet` | U+E6F4 | Ratchet |
| `pictFootballRatchet` | U+E6F5 | Football rattle |
| `pictWhip` | U+E6F6 | Whip |
| `pictBoardClapper` | U+E6F7 | Board clapper |
| `pictCastanets` | U+E6F8 | Castanets |
| `pictCastanetsWithHandle` | U+E6F9 | Castanets with handle |
| `pictQuijada` | U+E6FA | Quijada (jawbone) |
| `pictBambooScraper` | U+E6FB | Bamboo scraper |
| `pictRecoReco` | U+E6FC | Reco-reco |

**shakersOrRattlesPictograms** — Shakers or rattles pictograms, U+E740–U+E74F, 9 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictFlexatone` | U+E740 | Flexatone |
| `pictMaraca` | U+E741 | Maraca |
| `pictMaracas` | U+E742 | Maracas |
| `pictCabasa` | U+E743 | Cabasa |
| `pictThundersheet` | U+E744 | Thundersheet |
| `pictVibraslap` | U+E745 | Vibraslap |
| `pictSistrum` | U+E746 | Sistrum |
| `pictRainstick` | U+E747 | Rainstick |
| `pictChainRattle` | U+E748 | Chain rattle |

**bellsPictograms** — Bells pictograms, U+E710–U+E71F, 11 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictSleighBell` | U+E710 | Sleigh bell |
| `pictCowBell` | U+E711 | Cow bell |
| `pictAlmglocken` | U+E712 | Almglocken |
| `pictBellPlate` | U+E713 | Bell plate |
| `pictBell` | U+E714 | Bell |
| `pictHandbell` | U+E715 | Handbell |
| `pictCencerro` | U+E716 | Cencerro |
| `pictAgogo` | U+E717 | Agogo |
| `pictShellBells` | U+E718 | Shell bells |
| `pictJingleBells` | U+E719 | Jingle bells |
| `pictBellTree` | U+E71A | Bell tree |

**gongsPictograms** — Gongs pictograms, U+E730–U+E73F, 5 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictTamTam` | U+E730 | Tam-tam |
| `pictTamTamWithBeater` | U+E731 | Tam-tam with beater (Smith Brindle) |
| `pictGong` | U+E732 | Gong |
| `pictGongWithButton` | U+E733 | Gong with button (nipple) |
| `pictSlideBrushOnGong` | U+E734 | Slide brush on gong |

**chimesPictograms** — Chimes pictograms, U+E6C0–U+E6CF, 9 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictTubularBells` | U+E6C0 | Tubular bells |
| `pictWindChimesGlass` | U+E6C1 | Wind chimes (glass) |
| `pictChimes` | U+E6C2 | Chimes |
| `pictBambooChimes` | U+E6C3 | Bamboo tube chimes |
| `pictShellChimes` | U+E6C4 | Shell chimes |
| `pictGlassTubeChimes` | U+E6C5 | Glass tube chimes |
| `pictGlassPlateChimes` | U+E6C6 | Glass plate chimes |
| `pictMetalTubeChimes` | U+E6C7 | Metal tube chimes |
| `pictMetalPlateChimes` | U+E6C8 | Metal plate chimes |

**whistlesAndAerophonesPictograms** — Whistles and aerophones pictograms, U+E750–U+E75F, 11 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictSlideWhistle` | U+E750 | Slide whistle |
| `pictBirdWhistle` | U+E751 | Bird whistle |
| `pictPoliceWhistle` | U+E752 | Police whistle |
| `pictSiren` | U+E753 | Siren |
| `pictWindMachine` | U+E754 | Wind machine |
| `pictCarHorn` | U+E755 | Car horn |
| `pictKlaxonHorn` | U+E756 | Klaxon horn |
| `pictDuckCall` | U+E757 | Duck call |
| `pictWindWhistle` | U+E758 | Wind whistle (or mouth siren) |
| `pictMegaphone` | U+E759 | Megaphone |
| `pictLotusFlute` | U+E75A | Lotus flute |

**miscellaneousPercussionInstrumentPictograms** — Miscellaneous percussion instrument pictograms, U+E760–U+E76F, 8 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictPistolShot` | U+E760 | Pistol shot |
| `pictCannon` | U+E761 | Cannon |
| `pictSandpaperBlocks` | U+E762 | Sandpaper blocks |
| `pictLionsRoar` | U+E763 | Lion's roar |
| `pictGlassHarp` | U+E764 | Glass harp |
| `pictGlassHarmonica` | U+E765 | Glass harmonica |
| `pictMusicalSaw` | U+E766 | Musical saw |
| `pictJawHarp` | U+E767 | Jaw harp |

**percussionPlayingTechniquePictograms** — Percussion playing technique pictograms, U+E7F0–U+E80F, 31 glyphs

| Glyph name | Codepoint | Description |
|---|---|---|
| `pictStickShot` | U+E7F0 | Stick shot |
| `pictScrapeCenterToEdge` | U+E7F1 | Scrape from center to edge |
| `pictScrapeEdgeToCenter` | U+E7F2 | Scrape from edge to center |
| `pictScrapeAroundRim` | U+E7F3 | Scrape around rim (counter-clockwise) |
| `pictOnRim` | U+E7F4 | On rim |
| `pictOpenRimShot` | U+E7F5 | Closed / rim shot |
| `pictHalfOpen1` | U+E7F6 | Half-open |
| `pictHalfOpen2` | U+E7F7 | Half-open 2 (Weinberg) |
| `pictOpen` | U+E7F8 | Open |
| `pictDamp1` | U+E7F9 | Damp |
| `pictDamp2` | U+E7FA | Damp 2 |
| `pictDamp3` | U+E7FB | Damp 3 |
| `pictDamp4` | U+E7FC | Damp 4 |
| `pictRimShotOnStem` | U+E7FD | Rim shot for stem |
| `pictCenter1` | U+E7FE | Center (Weinberg) |
| `pictCenter2` | U+E7FF | Center (Ghent) |
| `pictCenter3` | U+E800 | Center (Caltabiano) |
| `pictRim1` | U+E801 | Rim or edge (Weinberg) |
| `pictRim2` | U+E802 | Rim (Ghent) |
| `pictRim3` | U+E803 | Rim (Caltabiano) |
| `pictNormalPosition` | U+E804 | Normal position (Caltabiano) |
| `pictChokeCymbal` | U+E805 | Choke (Weinberg) |
| `pictRightHandSquare` | U+E806 | Left hand (Agostini) |
| `pictLeftHandCircle` | U+E807 | Right hand (Agostini) |
| `pictSwishStem` | U+E808 | Combining swish for stem |
| `pictTurnRightStem` | U+E809 | Combining turn right for stem |
| `pictTurnLeftStem` | U+E80A | Combining turn left for stem |
| `pictTurnRightLeftStem` | U+E80B | Combining turn left or right for stem |
| `pictCrushStem` | U+E80C | Combining crush for stem |
| `pictDeadNoteStem` | U+E80D | Combining X for stem (dead note) |
| `pictScrapeAroundRimClockwise` | U+E80E | Scrape around rim (clockwise) |
**`beatersPictograms` (128 glyphs, U+E770–U+E7EF)** — not reproduced in full; the axis it defines is what matters. It decomposes as `<material/hardness> × <instrument family> × <orientation>`:

- hardness: `Soft`, `Medium`, `Hard`, `Wood`, `Metal`, `Double`
- material/type: `Xylophone`, `Glockenspiel`, `Timpani`, `BassDrum`, `Yarn`, `Superball`, `Wound` (hard/soft core), `Gum` (soft/medium/hard), `Metal`, `HammerWood`/`HammerPlastic`/`HammerMetal`, `SnareSticks`, `JazzSticks`, `Triangle`, `WireBrushes`, `BrassMallets`, `SpoonWoodenMallet`, `GuiroScraper`, `Bow`, `KnittingNeedle`, `Coins`, `DrumStick`
- body parts: `pictBeaterHand`, `pictBeaterFinger`, `pictBeaterFist`, `pictBeaterFingernails`
- orientation: `Up`, `Down`, `Left`, `Right` (a *notational* axis, not a sonic one)
- modifiers: `pictBeaterCombiningParentheses` (padded), `pictBeaterCombiningDashedCircle` (plated), `pictBeaterBox`

The sonically-relevant beater terms for a drum-kit product are: **snare sticks, jazz sticks, wire brushes, brass mallets (rutes), soft/medium/hard yarn or gum mallets, hand, finger, fist, fingernails, superball, drum stick, bow**.

SMuFL's percussion *technique* vocabulary (`percussionPlayingTechniquePictograms`, 31 glyphs) is the closest thing in notation to KITWARP's articulation axis, and it names the striking-position axis explicitly and separately: `pictCenter1/2/3` (Weinberg/Ghent/Caltabiano), `pictRim1/2/3`, `pictNormalPosition`, `pictOnRim`, `pictOpenRimShot`, `pictStickShot`, `pictEdgeOfCymbal` (U+E729), `pictBellOfCymbal` (U+E72A), `pictChokeCymbal`, `pictOpen`, `pictHalfOpen1`, `pictHalfOpen2`, `pictDamp1..4`, `pictScrapeCenterToEdge`, `pictScrapeEdgeToCenter`, `pictScrapeAroundRim` (cw/ccw), `pictDeadNoteStem`, `pictCrushStem`, `pictSwishStem`, `pictTurnLeft/RightStem`, `pictRightHandSquare`/`pictLeftHandCircle` (Agostini — a **limb/hand** axis).

Two SMuFL facts that directly contradict drum-remap's model:

1. **`pictEdgeOfCymbal` and `pictBellOfCymbal` are cymbal-generic**, not ride-specific. SMuFL treats *zone* as an axis over any cymbal, not as an enum member of one instrument.
2. **`pictHalfOpen1` / `pictHalfOpen2 (Weinberg)`** — the "half-open" concept is one named level with two competing glyph conventions, i.e. openness is a *level*, and the ordinal-vs-named split in drum-remap (`open-0..open-3` vs `open`) has no precedent in notation.

---

## 3. Implications for the KITWARP pivot vocabulary

### 3.1 The strongest single lesson: separate identity from rendering from MIDI (LilyPond), and formalise the identity layer (Hydrogen's mistake)

LilyPond and Hydrogen are a controlled experiment on the same problem.

| | LilyPond | Hydrogen |
|---|---|---|
| Pivot identity | closed symbol set in `ly/drumpitch-init.ly` | free-form `<type>` string |
| Extension path | documented, user-defined, additive (`drumPitchNames.foo = #'foo`) | "set them to arbitrary strings" |
| Result after N years | 65 symbols, no drift, aliases explicit | 219 strings for ~35 instruments across only 54 kits |

Hydrogen's proposal document states the trade-off up front and accepts the mismatches. KITWARP should take the opposite decision: **the pivot term set is closed and versioned; the extension path is a registry, not free text.** The cost of Hydrogen's choice is legible in §2.3.4 — `Crash Choke` vs `Crash Choke 2`, `Hi-hat Semi-Open` vs `Hi-hat Open 2`, `Tom Floor` type on an instrument displayed as `Tom Low`.

LilyPond's three-table split maps cleanly onto KITWARP:

| LilyPond | KITWARP equivalent |
|---|---|
| `drumPitchNames` (token → symbol, many-to-one) | device-layout alias table → pivot ID |
| `drumStyleTable` (symbol → notehead/script/line, per style) | *no equivalent needed*, but proves the presentation layer must not be in the pivot |
| `midiDrumPitches` (symbol → pitch, overridable per score) | pivot ID → target-layout note |

The critical property is that LilyPond's symbol layer has **no MIDI note in it**. `tamtam` exists as a symbol with no pitch; `splashhihat` and `pedalhihat` are distinct symbols that happen to share pitch 44. KITWARP's pivot IDs must likewise be defined without reference to any note number, or GM's 47-note ceiling leaks back in.

### 3.2 Axes the sources demand

drum-remap has `instrument · articulation · role · instance`. The evidence here says that is under-factored in three places and over-factored in one.

**(a) `zone` must be its own axis, not articulation values.**
SMuFL names `pictEdgeOfCymbal` / `pictBellOfCymbal` / `pictCenter*` / `pictRim*` / `pictNormalPosition` as *positions*, applicable to any instrument. MuseScore names `Shell` (marching snare 59, tenors) as a strike location distinct from `Rim` and from `Rim Shot`. Hydrogen uses `Bow`/`Bell`/`Side` on ride **and** `Crash Bow`/`Crash Bell`/`China Bell` on crashes and chinas. drum-remap encodes bow/bell only under `ride/*` and `megabell/*`; it cannot express "crash bell", which all three sources can. Zone values evidenced: `center`, `edge`, `rim`, `shell`, `bow`, `bell`, `side`, `head`, `tip`, `shank`.
This also resolves drum-remap's own noted defect: `hihat/shank` is a *zone*, and `hihat/*-tip` / `hihat/*-edge` are `(articulation=closed, zone=tip|edge)` pairs, not 16 flat articulation strings.

**(b) `beater` / `implement` is a real axis with a standard vocabulary — SMuFL's 128 beater glyphs.**
Sonically relevant values: `stick`, `jazz-stick`, `brush`, `rod`/`brass-mallet`, `mallet` (soft/medium/hard), `hand`, `finger`, `fist`, `fingernail`, `superball`, `bow`. This matters for KITWARP specifically because Superior Drummer, EZdrummer and BFD3 ship brush and mallet and rod kits whose notes are the *same physical drums played with a different implement*. drum-remap has no way to say this; a brush sweep will fall back to a stick hit silently. SMuFL also proves the axis is orthogonal (hardness × family × orientation), and that **orientation (`Up`/`Down`/`Left`/`Right`) is purely notational** and must NOT enter the pivot.

**(c) `limb` / `hand` is named in notation and is missing.**
SMuFL `pictRightHandSquare` / `pictLeftHandCircle` (Agostini); LilyPond documents `R`/`L` sticking markup (`percussion.itely`, "Drum rolls" section). More decisively for KITWARP: LilyPond's `splashhihat` (`hhs`) is notated **below the staff with `(open . DOWN)` in `drums-style` and `weinberg-drums-style`**, i.e. it is a *left-foot* event, sonically distinct from `pedalhihat` but colliding with it on MIDI 44. Foot-splash is a real e-drum/library articulation and drum-remap has no term for it.

**(d) `role` has zero support in any source examined.**
None of LilyPond, MuseScore, Hydrogen or SMuFL encodes anything like `foundation | backbeat | ghost | timekeeping | fill | accent | effect`. LilyPond's `percussion.itely` has a "Ghost notes" section but treats ghost notes as a *notational parenthesis/dead-note marking*, and SMuFL's nearest glyph is `pictDeadNoteStem`. Conclusion: `role` is not an identity axis — it is an annotation on a *note event*, not on a *sound*. Keeping it in the pivot ID (as drum-remap does) makes the ID unstable, because the same sound has different roles in different bars. **Recommendation: move `role` out of the pivot term and into optional per-mapping metadata.**

**(e) `instance` must be structured, and must never be an unbounded ordinal.**
Hydrogen shows the failure mode at full scale: `Whistle 15`, `Cowbell 14`, `Kick 12`, `Crash 9`, `Hi-hat Open 6`. The ordinal simultaneously means "second crash on the kit", "alternate sample", and "unrelated sound that happened to be a cowbell". MuseScore shows the opposite trap: `tom-toms` is `Tom 6 … Tom 1` where **the high ordinal is the low drum**, while `temple-blocks` is `Low → High`; and `TR808EmulationKit` has type `Tom Floor` on a drum named `Tom Low`. So:
- ordinals must be **defined relative to a stated origin** (KITWARP should pick one and state it: e.g. `tom-1` = highest-pitched rack tom, ascending toward the floor), and
- `instance` must be a *typed slot* (`rack-1`, `floor-1`, `left`, `right`) rather than a free integer, with a documented projection from ordinal-only device layouts.

**(f) Openness is a level, not a set of ordinals mixed with names.**
Evidence: GM/MuseScore give 3 (`closed` 42, `pedal` 44, `open` 46); LilyPond adds `halfopenhihat` as a fourth symbol (sharing pitch 46); Hydrogen ships `Hi-hat Closed`, `Hi-hat Semi-Open`, `Hi-hat Open`, `Hi-hat Swish`, `Hi-hat Pedal`, plus ordinal levels up to `Hi-hat Open 6`; SMuFL has `pictOpen`, `pictHalfOpen1`, `pictHalfOpen2`, `pictDamp1..4`. Every source agrees the axis is **ordered**; none of them agrees on the number of steps. drum-remap's mixture of named (`tight`, `closed`, `closed-loose`, `open`) and ordinal (`open-0..open-3`) levels is therefore the right *shape* but the wrong *encoding*. **Recommendation: a single normalised openness scalar (0.0 closed … 1.0 fully open) plus named anchor points, so a 4-level device and a 6-level device map without inventing terms.** This also gives the controller/pedal-position model drum-remap lacks: hi-hat pedal CC4 position and articulation openness are the same axis measured two ways.

### 3.3 Vocabulary breadth: GM's 47 is not the only ceiling — so is drum-remap's 12 instruments

| Source | Distinct percussion identities |
|---|---|
| General MIDI percussion | 47 |
| LilyPond `drumPitchNames` symbols | 65 (64 with MIDI) |
| MuseScore built-in drumset | 61 (notes 27–87) |
| MuseScore `instruments.xml` `<Drum>` entries | 287 across 107 instruments |
| Hydrogen shipped instrument types | 219 |
| SMuFL percussion pictograms (excl. beaters, mallet, electronic) | ~120 |
| drum-remap | 12 instruments / 40 pairs |

drum-remap covers a rock/metal kit. Every one of these sources covers hand percussion, orchestral percussion and world percussion as a matter of course. KITWARP's target devices make this concrete: Roland TD/VAD and Yamaha DTX modules ship tambourine, cowbell, block, and hand-percussion voices on kit pads by default, and SD3/BFD3 ship percussion expansions. A pivot that cannot name `tambourine` cannot round-trip a stock TD kit.

**Minimum percussion instrument set the sources agree on** (present in ≥3 of {GM, LilyPond, MuseScore drumset/percussion, Hydrogen, SMuFL}): tambourine, cowbell, hand-clap, maracas, cabasa, shaker, claves, wood-block (hi/lo), agogo (hi/lo), triangle, guiro, vibraslap, castanets, sleigh-bells, mark-tree/bell-tree, whistle (short/long), cuica, surdo, timbale (hi/lo), conga (hi/lo), bongo (hi/lo), tam-tam/gong, brake-drum, anvil, ratchet, whip, finger-snap, sizzle-cymbal, suspended-cymbal, hand-cymbals, finger-cymbals, temple-blocks, log-drum, slit-drum, djembe, doumbek, cajon, tabla, taiko, frame-drum, quijada, thundersheet, rainstick, flexatone, sistrum, reco-reco, chimes (glass/bamboo/shell/metal).

### 3.4 Stable numeric IDs — what the sources do and do not give you

- **SMuFL is the only source with stable numeric identifiers** (Private Use Area codepoints, e.g. `pictHiHat` = U+E722), and they are versioned and governed by a W3C Community Group. They are, however, identifiers for *pictograms*, not for sounds: `pictHiHat` (U+E722) and `pictHiHatOnStand` (U+E723) are two drawings of one instrument, and there is no SMuFL codepoint for "hi-hat closed tip".
- MuseScore's identifiers are **MIDI note numbers**, which is exactly the mistake KITWARP exists to fix — `percussion` and `drumset` in the same `instruments.xml` assign Closed Hi-Hat to 27 and 42 respectively.
- Hydrogen's identifiers are display strings.
- LilyPond's identifiers are Scheme symbols — stable, but with no numeric form.

**Recommendation:** KITWARP should mint its own integer IDs, and carry `smufl:` glyph names as an *optional cross-reference* field on instrument terms only (not articulations). SMuFL cross-references buy interop with notation tooling at no design cost; they cannot serve as the primary key.

### 3.5 Real vs cosmetic distinctions

**Real** (some source encodes them as separate identities *and* they differ sonically):

- `sidestick` / `cross-stick` / `rim-click` — one sound, three names (LilyPond `sidestick`; MuseScore `Side Stick`, `Cross-stick`, `Rim Click`; Hydrogen `Stick`). Real *sound*, cosmetic *naming* — needs alias resolution.
- `rimshot` vs `rim` (on-rim) vs `shell` vs `stick-shot` vs `back-stick` vs `ping shot` vs `gok shot` — MuseScore's marching-snare set treats all seven as distinct notes (48/50/51/52/53/55/57/59/60). Sonically real, and drum-remap has only `snare/rimshot`.
- `snares-off` — LilyPond has `pictSnareDrumSnaresOff` in SMuFL and MuseScore has no note for it; drum-remap's `snare/wires-off` is *ahead* of all four sources here. Keep it.
- `buzz` / `roll` — Hydrogen ships 13 `* Roll` types; MuseScore marching-snare has `Buzz` (48) and marching-cymbals has `Roll` (93). This is a sustained-articulation class drum-remap lacks entirely.
- `flam` — Hydrogen `Snare Flam`, `Tom Low Flam`, `Tom Mid Flam`, `Tom Floor Flam`; drum-remap has `snare/flam` but not tom flams. Flam is an axis value applicable to any drum, not a snare-only articulation.
- `choke` on any cymbal — SMuFL `pictChokeCymbal` is generic; MuseScore marching has `Crash-Choke`, `Tap-Choke`, `Bell Tap-Choke`; Hydrogen has `Crash Choke`, `Ride Choke`, `Splash Choke`, `Hi-hat Open Choke`. drum-remap has choke on crash/china/splash/ride but not on hi-hat. **`hihat/open-choke` is a missing term.**
- `mute` / `damp` levels — SMuFL `pictDamp1..4` (four levels); MuseScore `Taiko Mute`, `Mute Surdo`, `Muted` on marching tenors; Hydrogen 10 `* Mute` types. Damping is an ordered axis, like openness.
- Hand-drum stroke set `bass` / `tone` / `open` / `slap` / `mute` — MuseScore `djembe`/`doumbek` (62 Slap, 63 Open, 64 Bass), LilyPond's documented djembe example (`dbass`, `dbassmute`, `dopen`, `dopenmute`, `dslap`, `dslapmute`), Hydrogen `Djembe Bass/Slap/Tone`, `Cajon Slap/Thumb`, `Conga Slap`, `* Head`/`* Bell` for dunun family. This is a *closed, well-attested* articulation set that drum-remap has none of.
- `unison` (MuseScore marching-bass 90) — a **1→N expand** target: one note that means "all drums in the section". drum-remap already has 1→N expand rules; this is the same mechanism, and confirms it belongs in the model.

**Cosmetic** (naming/notation only — must NOT become separate pivot terms):

- Notehead, staff line, stem direction, voice, panel row/column (MuseScore); notehead + script + line (LilyPond `drumStyleTable`). Pure presentation. MuseScore itself ships four different notehead choices for China Cymbal across files (`normal` in `instruments.xml` vs `HEAD_CUSTOM`/`noteheadHeavyXHat` in `drumset.cpp`).
- Beater orientation `Up`/`Down`/`Left`/`Right` (SMuFL) — a page-layout concern.
- `pictCenter1/2/3`, `pictRim1/2/3`, `pictHalfOpen1/2` — the numeric suffixes are *competing engraving conventions* (Weinberg / Ghent / Caltabiano), not different sounds. One pivot term each.
- `Acoustic Bass Drum` (35) vs `Bass Drum 1` (36); `Acoustic Snare` (38) vs `Electric Snare` (40); `Ride Cymbal 1` (51) vs `Ride Cymbal 2` (59); Hydrogen `Ride Jazz`/`Ride Rock`, `Snare Jazz`/`Snare Rock`. These are **instance/timbre-variant** distinctions, not articulation distinctions, and GM conflates the two — treat as `instance`, not as separate instruments.
- MuseScore keyboard `shortcut` letters — per-file and positional.
- Localisation (`drumset_fr.drm`: `Charleston Fermé` = Closed Hi-Hat, `Grosse Caisse` = Bass Drum) — a display-name layer, and further proof the pivot ID must not be an English word.

### 3.6 Concrete recommendations

1. Pivot term = `instrument · zone · articulation · (instance)`. Drop `role` from the term; keep it as optional event metadata.
2. Add axes: `zone`, `beater`, `limb`, and a numeric `openness`/`damping` scalar with named anchors.
3. Mint opaque integer pivot IDs; keep human-readable slugs as a display alias table (LilyPond's `drumPitchNames` pattern) so localisation and vendor spellings never touch the ID.
4. Close the vocabulary; version it; provide a registry for extension. Explicitly do **not** repeat Hydrogen's "arbitrary strings" decision.
5. Carry optional `smufl:<glyphName>` cross-references on instrument terms for notation interop.
6. Broaden coverage beyond the rock kit to at least the ~48-instrument percussion set in §3.3 before collecting device data, because adding an instrument axis value later is cheap but adding an *axis* later is not.

---

## 4. New terms this dossier contributes (relative to drum-remap's model)

Axis key: `instrument` | `articulation` | `zone` | `instance` | `role` | `controller` | `modifier` | `other`.

### 4.1 New axes proposed

| Term | Axis | Meaning | Source |
|---|---|---|---|
| `zone` | other (new axis) | striking position on the instrument, orthogonal to instrument and articulation | SMuFL `pictCenter*`/`pictRim*`/`pictEdgeOfCymbal`/`pictBellOfCymbal`; MuseScore `Shell`/`Rim`; Hydrogen `Bow`/`Bell`/`Side` |
| `beater` | modifier (new axis) | implement used to strike | SMuFL `beatersPictograms` (128 glyphs) |
| `limb` | modifier (new axis) | which limb produces the event (L/R hand, L/R foot) | SMuFL `pictLeftHandCircle`/`pictRightHandSquare`; LilyPond `splashhihat` notated below staff |
| `openness` | controller (new axis) | ordered scalar 0..1 with named anchors, unifying hi-hat articulation levels and pedal CC position | LilyPond `closedhihat`/`halfopenhihat`/`openhihat`; Hydrogen `Hi-hat Closed`/`Semi-Open`/`Open`/`Open 2..6`; SMuFL `pictOpen`/`pictHalfOpen1`/`pictHalfOpen2` |
| `damping` | controller (new axis) | ordered scalar for mute/damp depth | SMuFL `pictDamp1`..`pictDamp4`; Hydrogen 10 `* Mute` types |

### 4.2 New zone values

`center`, `edge`, `rim`, `shell`, `bow`, `bell`, `side`, `head`, `tip`, `shank`, `dome`.
Sources: SMuFL `pictCenter1/2/3`, `pictRim1/2/3`, `pictOnRim`, `pictEdgeOfCymbal`, `pictBellOfCymbal`, `pictNormalPosition`; MuseScore `marching-snare` 59 `Shell`, tenors `Drum n Shell`; Hydrogen `Ride Bow`/`Ride Bell`/`Ride Side`/`Crash Bow`/`Crash Bell`/`China Bell`, `Dununba Head`/`Dununba Bell`.

### 4.3 New articulation values

| Term | Meaning | Source |
|---|---|---|
| `roll` | sustained multi-stroke roll | Hydrogen 13 `* Roll` types; MuseScore marching-cymbals 93 `Roll` |
| `buzz` | pressed/multiple-bounce roll | MuseScore `marching-snare` 48 `Buzz`, tenors `Drum n Buzz` |
| `rim-click` | stick tip on rim only | MuseScore `marching-snare` 53 `Rim Click`; `percussion` 37 `Snare Rim` |
| `stick-shot` | stick-on-stick against head | MuseScore `marching-snare` 57; SMuFL `pictStickShot` (U+E7F0) |
| `back-stick` | butt-end strike | MuseScore `marching-snare` 60 `Backstick`; `Marching_Snare_Drums.drm` 60 `Back Stick` |
| `ping-shot` | rimshot near the rim (bright) | MuseScore `Marching_Snare_Drums.drm` 49 |
| `gok-shot` | rimshot near centre (dark) | MuseScore `Marching_Snare_Drums.drm` 52 |
| `mute` / `damp` | hand-damped strike | SMuFL `pictDamp1..4`; MuseScore 86 `Mute Surdo`, `Taiko Mute`, `Mute Triangle`, `Mute Cuica`, `Mute Hi Conga`; Hydrogen `* Mute` |
| `dead` | fully choked/dead stroke | SMuFL `pictDeadNoteStem` (U+E80D) |
| `crush` | crushed/buzzed grace | SMuFL `pictCrushStem` (U+E80C) |
| `swish` | brush/stick sweep across cymbal or head | SMuFL `pictSwishStem` (U+E808); Hydrogen `Hi-hat Swish` |
| `scrape` | scraped (guiro, cymbal, head) with direction | SMuFL `pictScrapeCenterToEdge`/`pictScrapeEdgeToCenter`/`pictScrapeAroundRim` cw+ccw |
| `sizzle` | sizzle/rivet cymbal sustain | SMuFL `pictSizzleCymbal`; MuseScore `marching-cymbals` 77, `Marching_Cymbals.drm` 77 |
| `half-open` | intermediate hi-hat/cymbal openness | SMuFL `pictHalfOpen1/2`; LilyPond `halfopenhihat`; Hydrogen `Hi-hat Semi-Open` |
| `open-choke` | open hi-hat immediately choked | Hydrogen `Hi-hat Open Choke` |
| `slap` | hand-drum slap stroke | MuseScore `djembe`/`doumbek` 62 `Slap`, 28 `Slap`; Hydrogen `Djembe Slap`, `Cajon Slap`, `Conga Slap`; LilyPond doc `dslap` |
| `tone` | hand-drum open tone | Hydrogen `Djembe Tone`; MuseScore `djembe` 63 `Open` |
| `bass` | hand-drum bass stroke (centre, full hand) | MuseScore `djembe`/`doumbek` 64 `Bass`; Hydrogen `Djembe Bass`; LilyPond doc `dbass` |
| `thumb` | thumb stroke (cajon/conga) | Hydrogen `Cajon Thumb` |
| `heel` / `toe` | pedal technique distinction | **UNVERIFIED** — implied by `Foot Stomp`/`Hi-hat Pedal` but not named in any source read |
| `tap` / `bell-tap` / `smash` / `zing` / `crunch` / `punch` / `suc` / `ting` | marching-cymbal technique set | MuseScore `marching-cymbals` 81/84/89/91 and `Marching_Cymbals.drm` 72/76/79/81/84/89/91 |
| `full-crash` / `half-crash` | two-plate crash depth | MuseScore `marching-cymbals` 72, 74 |
| `flam` (generic) | flam applicable to any drum, not snare-only | Hydrogen `Snare Flam`, `Tom Low Flam`, `Tom Mid Flam`, `Tom Floor Flam` |
| `glissando-down` | bell-tree / mark-tree sweep | MuseScore `bell-tree`, `mark-tree` 84 |
| `gesture-up` / `gesture-down` / `gesture-cut` | shaker/cabasa stroke direction | Hydrogen `Cabasa Up`/`Cabasa Down`/`Cabasa Cut`; SMuFL `shekere`→`Shake` |

### 4.4 New beater (modifier) values

`stick`, `jazz-stick`, `brush` (wire), `rod`/`brass-mallet`, `mallet-soft`, `mallet-medium`, `mallet-hard`, `yarn-mallet`, `gum-mallet`, `wood-mallet`, `metal-beater`, `superball`, `hand`, `finger`, `fist`, `fingernail`, `bow`, `guiro-scraper`, `triangle-beater`, `knitting-needle`, `coins`.
Source: SMuFL `beatersPictograms` U+E770–U+E7EF (`pictBeaterSnareSticksUp`, `pictBeaterJazzSticksUp`, `pictBeaterWireBrushesUp`, `pictBeaterBrassMalletsUp`, `pictBeaterSoftYarnUp`, `pictGumSoftUp`, `pictBeaterSuperballUp`, `pictBeaterHand`, `pictBeaterFinger`, `pictBeaterFist`, `pictBeaterFingernails`, `pictBeaterBow`, `pictBeaterGuiroScraper`, `pictBeaterTriangleUp`, `pictBeaterKnittingNeedle`, `pictCoins`, `pictDrumStick`).

### 4.5 New instrument values (percussion beyond the rock kit)

Present in ≥2 of the four sources unless noted:

`tambourine`, `hand-clap`, `finger-snap`, `foot-stomp` (Hydrogen only), `maracas`, `cabasa`, `shaker`, `claves`, `wood-block` (hi/lo), `temple-block` (5 sizes), `log-drum`, `slit-drum`, `agogo` (hi/lo), `triangle`, `guiro` (short/long), `vibraslap`, `castanets`, `sleigh-bells`, `mark-tree`, `bell-tree`, `whistle` (short/long), `cuica`, `surdo`, `timbale` (hi/lo), `conga` (hi/lo), `bongo` (hi/lo), `tam-tam`, `gong`, `brake-drum`, `anvil`, `ratchet`, `whip`, `quijada`, `reco-reco`, `bamboo-scraper`, `sandpaper-blocks`, `thundersheet`, `rainstick`, `flexatone`, `sistrum`, `chain-rattle`, `sizzle-cymbal`, `suspended-cymbal`, `hand-cymbals`, `finger-cymbals`, `vietnamese-hat-cymbal`, `chimes` (glass/bamboo/shell/metal-tube/metal-plate/glass-tube/glass-plate), `almglocken`, `cencerro`, `bell-plate`, `handbell`, `jingle-bells`, `shell-bells`, `djembe`, `doumbek`/`goblet-drum`, `cajon`, `tabla`, `taiko`, `frame-drum`, `military-snare`, `piccolo-snare`, `field-drum`, `tenor-drum`, `ocean-drum`, `bucket` (Hydrogen only), `dununba`, `sangban`, `kenkeni`, `pistol-shot`, `cannon`, `lions-roar`, `musical-saw`, `jaw-harp`, `glass-harp`, `siren`, `police-whistle`, `bird-whistle`, `slide-whistle`, `duck-call`, `car-horn`, `klaxon-horn`, `wind-machine`, `board-clapper`, `metal-castanets`, `stones`, `iron-pipes`, `chains`, `sistrum`.

### 4.6 New instance values

| Term | Meaning | Source |
|---|---|---|
| `spock-1`, `spock-2` | the two small top drums on a marching tenor rack | MuseScore `marching-tenor-drums` 84/96, `Marching_Tenors.drm` |
| `unison` | 1→N expand target meaning "all drums in section" | MuseScore `marching-bass-drums` 90 `Unison`, `Marching_Bass_Drums.drm` 90/91/92 |
| `drum-1..drum-5` | section-relative ordinal (marching bass line) | MuseScore `marching-bass-drums` |
| `rack-1`, `rack-2`, `floor-1`, `floor-2` (structured, with stated origin) | replaces bare ordinals | forced by MuseScore `tom-toms` (`Tom 6`=lowest) vs `temple-blocks` (`Low`→`High`) conflict, and Hydrogen `Tom Floor` type on drum named `Tom Low` |

---

## 5. Provenance and licences

### 5.1 Per-source

| Source | Licence (as stated in the repo) | Evidence |
|---|---|---|
| **LilyPond** | **GPL-3.0-or-later**. `ly/drumpitch-init.ly` header: "Copyright (C) 2001–2026 Rune Zedeler, Han-Wen Nienhuys … LilyPond is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License … either version 3 of the License, or (at your option) any later version." Repo root `COPYING` = GPLv3. Separate `LICENSE.DOCUMENTATION` (docs) and `LICENSE.OFL` (fonts). | `repos/lilypond/ly/drumpitch-init.ly` lines 1–19; `repos/lilypond/COPYING` |
| **MuseScore Studio** | **GPL-3.0-only**. `LICENSE.txt`: "MuseScore Studio, free and open source music notation software / Copyright (C) 1999–2026 MuseScore Limited and others / This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License **version 3** as published by …" (no "or later"). | `repos/MuseScore/LICENSE.txt` lines 1–6 |
| **Hydrogen** | **GPL-2.0-or-later**. `COPYING` = GPL v2, June 1991. Per-file headers (e.g. `src/core/Basics/DrumkitMap.h`): "Copyright(c) 2008-2026 The hydrogen development team … either version 2 of the License, or (at your option) any later version." | `repos/hydrogen/COPYING`; `repos/hydrogen/src/core/Basics/DrumkitMap.h` lines 1–20 |
| **SMuFL** | **No `LICENSE` file in the repository.** `w3c.json` declares `"repo-type": "cg-report"` — a W3C Community Group report, maintained by the W3C Music Notation Community Group. **UNVERIFIED**: the exact licence. W3C CG deliverables are normally covered by the W3C Community Contributor License Agreement (CLA) and published under the W3C Software and Document Licence or CC-BY; this repo does not state which. The *Bravura font* shipped in `font/` is separately SIL OFL (per its own metadata) but was not used here. Treat the SMuFL **specification text** as unlicensed-in-repo and re-check before redistributing any verbatim block. | `repos/smufl/w3c.json`; `repos/smufl/README.md`; absence of `LICENSE*` confirmed by `ls` |
| **General MIDI percussion key map** | The GM Level 1 percussion assignments are a MIDI Manufacturers Association / AMEI specification. Not obtained here; reached only indirectly through the four repos above. MuseScore's `share/instruments/README.md` states the GM constants live in *hidden third-party sheets* of its source spreadsheet, i.e. MuseScore itself treats them as third-party data. | `repos/MuseScore/share/instruments/README.md` |

### 5.2 The copyright position for KITWARP

**Facts are not copyrightable; a curated file is.** The distinction that matters here:

- **Safe to use freely**: the *assignments themselves* — "GM note 42 is a closed hi-hat", "MuseScore maps Ride Bell to 53", "Hydrogen's GMRockKit uses `Hi-hat Semi-Open` on note 82". These are facts about how a system behaves, and facts have no copyright protection (US: *Feist v. Rural*, 499 U.S. 340 (1991); EU: facts are outside the Art. 2 Berne scope, though see the *sui generis* database right below). KITWARP can state, re-derive and act on every note→sound assignment in this dossier without a licence.
- **Not safe**: copying a *curated file* wholesale — e.g. shipping `ly/drumpitch-init.ly`'s 129-token alias list verbatim, or the 219-string Hydrogen type list as a data file, or MuseScore's `instruments.xml` percussion block. The *selection, arrangement and naming* is the authorship. Doing that pulls the GPL into KITWARP's data and, if KITWARP links it into a VST3 plugin, into the plugin.
- **EU database right (Directive 96/9/EC)**: independent of copyright, a *sui generis* right can attach to a database that represents substantial investment in obtaining/verifying/presenting the contents, and it prohibits extraction of a *substantial part* even where no element is individually protected. The Hydrogen `.h2map` corpus (54 curated files) and MuseScore's `instruments.xml` are plausibly such databases. This is a further reason to re-derive rather than extract. **UNVERIFIED**: whether any rightsholder here asserts it; none of the repos mentions a database right.
- **Names as terms**: single words and short phrases (`closedhihat`, `Ride Bell`, `pictBellOfCymbal`) are generally too short for copyright. Adopting individual *terms* into KITWARP's vocabulary is low risk; adopting a whole curated *list* in its original selection and order is not.

**Practical rule for KITWARP:** treat this dossier as *evidence about what distinctions exist*, design KITWARP's vocabulary independently from that evidence, and cite the sources. Do not ship any of these files, and do not ship a data file that is recognisably one of these lists reordered. Where SMuFL glyph names are used as cross-references, they are identifiers pointing *at* a spec, which is the intended use and is the lowest-risk form of reuse in this dossier.

### 5.3 Fact-by-fact provenance index

| Fact block | Path |
|---|---|
| LilyPond 64-symbol MIDI table, 129 alias tokens, 6 style tables | `lilypond/ly/drumpitch-init.ly` |
| LilyPond 3-table architecture; user extension; djembe example; ghost notes; sticking R/L | `lilypond/Documentation/en/notation/percussion.itely` lines 60–115, 525–640 |
| Weinberg citation | `lilypond/ly/drumpitch-init.ly`, comment above `weinberg-drums-style` |
| MuseScore 61-entry built-in drumset (notes 27–87) | `MuseScore/src/engraving/dom/drumset.cpp`, `initDrumset()` lines 309–1024 |
| MuseScore drum display names incl. 91/93/99/102 | `MuseScore/src/engraving/types/typesconv.cpp` lines 3038+ |
| `DRUM_INSTRUMENTS = 128`; `DrumInstrumentVariant` | `MuseScore/src/engraving/dom/drumset.h` lines 38, 92 |
| `<variants>`/`<articulation>`/`<tremolo>` reader; `head`/`noteheads` parsing | `MuseScore/src/engraving/dom/drumset.cpp`, `readDrumProperties()` lines 160–210, `varPitch()` ~289 |
| `NoteHeadGroup` enum order | `MuseScore/src/engraving/types/types.h` lines 526–556 |
| 287 `<Drum>` entries / 107 instruments; the 4 kit presets; marching sets | `MuseScore/share/instruments/instruments.xml` |
| Instrument data generated from a Google spreadsheet; hidden GM sheets | `MuseScore/share/instruments/README.md` |
| 6 shipped `.drm` drumsets | `MuseScore/share/templates/{Marching_Bass_Drums,Marching_Cymbals,Marching_Snare_Drums,Marching_Tenors,drumset_fr,orchestral}.drm` |
| Hydrogen pivot data model + "arbitrary strings" | `hydrogen/src/core/Basics/DrumkitMap.h` lines 38–48, 130–145 |
| `.h2map` schema | `hydrogen/data/xsd/drumkit_map.xsd` |
| `<instrument><type>` optional string | `hydrogen/data/xsd/drumkit.xsd` line 104 |
| 219 types / 1330 mappings / 54 kits | `hydrogen/data/drumkit_maps/*.h2map` |
| Governance decision not to formalise the vocabulary | `hydrogen/docs/proposals/0002-drumkit-independent-patterns_v2.md`, §"Instrument types" |
| GUI type suggestions = union of installed kits | `hydrogen/src/gui/src/DrumkitPropertiesDialog.cpp` lines 731–732; `hydrogen/src/core/SoundLibrary/SoundLibraryDatabase.cpp` line 472 |
| GMRockKit / TR808EmulationKit / legacy GMkit | `hydrogen/data/drumkits/{GMRockKit,TR808EmulationKit}/drumkit.xml`; `hydrogen/src/tests/data/drumkits/legacy_GMkit/drumkit.xml` |
| SMuFL pictogram ranges and glyph names | `smufl/metadata/ranges.json`, `smufl/metadata/glyphnames.json` |
| SMuFL governance | `smufl/w3c.json`, `smufl/README.md` |

Upstream URLs: <https://github.com/lilypond/lilypond>, <https://github.com/musescore/MuseScore>, <https://github.com/hydrogen-music/hydrogen>, <https://github.com/w3c/smufl>. Working data files produced during extraction: `scratch:{ly.json,ms_drumset.json,ms_instruments_drums.json,h2types.json}`.

### 5.4 Unverified claims collected

1. Whether MuseScore's source spreadsheet holds percussion columns not emitted into `instruments.xml`.
2. Which shipped MuseScore file consumes drum names 91, 93, 99, 102 (`Snare (Rim shot)`, `Ride (Edge)`, `Cowbell Low`, `Cowbell High`).
3. The exact licence of the SMuFL specification repository (no `LICENSE` file present).
4. Whether `drumset_fr.drm`'s numeric `<head>` values still resolve to their originally intended noteheads under the current string-based reader.
5. The meaning of Hydrogen's `Crash Flink` / `Ride Flink` types.
6. Whether any rightsholder asserts an EU *sui generis* database right over these datasets.
7. `heel` / `toe` as pedal-technique articulation values — implied by the sources but not named in any of them.
