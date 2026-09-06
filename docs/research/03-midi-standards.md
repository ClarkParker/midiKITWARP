# Dossier 03 — MIDI standard percussion vocabularies (GM1 / GM2 / Roland GS / Yamaha XG)

Purpose: extract, completely, the percussion **sound-name** vocabularies of the four MIDI
standards, and reduce them to one normalised list of distinct sounds. This union is the
**minimum coverage floor** for the KITWARP pivot vocabulary: any pivot that cannot name
these sounds cannot round-trip a GM/GS/XG source layout.

---

## 1. Scope and method

### 1.1 What was fetched

| Source | How obtained | Status |
|---|---|---|
| midi.org `general-midi-2`, `general-midi-level-1`, `midi-ci-profile-for-default-drum-note-map` | WebFetch | **Tables not public.** All three pages describe the spec and gate the PDF behind MIDI Association membership ("Join Us to Download"). No note tables served in HTML. |
| midi.org `gm-level-1-sound-set`, `specifications-old/item/gm-level-1-sound-set` | WebFetch | HTTP 404 (pages removed in the site rebuild). |
| `github.com/jpcima/gm-xg-gs` → `instrument/GM1_GM2.ins` | `git clone --depth 1` | **Obtained.** Cakewalk instrument-definition file, header states: *"This list is based on 'GM1/GM2 Recommended Practice (RP024)'"*, (c)2008 kuzu / openmidiproject, version 2008/7/26. |
| `github.com/jpcima/gm-xg-gs` → `instrument/Roland_SC-8850.ins` | `git clone --depth 1` | **Obtained.** Header: *"based on 'SC-8850 Users Manual' pp.167-245"*. Contains the SC-55, SC-88, SC-88Pro **and** SC-8850 drum maps as separate note-name sections (86 sections). |
| `github.com/jpcima/gm-xg-gs` → `instrument/YAMAHA_MU1000_MU2000.ins` | `git clone --depth 1` | **Obtained.** Header: *"based on 'MU1000/MU2000 List Book'"*. 44 drum-kit sections (XG level B / MU-native). |
| `github.com/pedrolcl/VMPK` → `data/gmgsxg.ins` | `git clone --depth 1` | **Obtained.** Contains the **XG Level 1** eleven-kit set and the base Roland GS nine-set map as note-name sections. Used as the XG L1 authority (the MU1000 file is a superset and does not isolate XG L1). |
| `github.com/DigitalInBlue/ReaperNoteNames` → `generalmidi_drums.txt` (already cloned in this workspace) | filesystem | Used as an **independent cross-check** of the GM1 35–81 names. Agrees on all 47 (spelling variants only: "Accoustic Bass Drum", "Vibroslap", "Mute HiConga"). |

### 1.2 Method

1. Parsed the Cakewalk `.ins` `.Note Names` blocks with a purpose-written parser
   (`/tmp/.../scratchpad/parse_ins.py`), resolving `BasedOn=` inheritance so every kit is
   materialised as a full note→name map.
2. Materialised **135 drum sets** across the four standards + their vendor extensions
   (`research/data/drumsets.json`, 345 KB).
3. Indexed every distinct name string per standard (`research/data/core_names.txt`).
4. Normalised name strings to **canonical sounds** with an explicit, auditable rule table
   (`norm.py`; 0 unmapped residuals) — collapsing (a) spelling variants, (b) kit-timbre
   prefixes that name the *same physical sound* in a differently-voiced kit
   (Room/Power/Jazz/Brush/Standard 1/Standard 2/Dance/House/…), and (c) ordinal suffixes
   that index pieces of the same instrument (Tom 1..6, Snare 1/2, Kick 1/2).
5. Kept as **separate** sounds anything that is a different physical object, a different
   striking articulation, or a categorically different synthesis source
   (acoustic vs analog-drum-machine vs reversed sample).

### 1.3 Counts

| Standard | Sets parsed | Raw distinct name strings | Notes used |
|---|---|---|---|
| GM Level 1 | 1 | 47 | 35–81 |
| GM Level 2 | 9 | 167 | 27–88 |
| GS (SC-55) | 10 | 193 | 27–108 |
| GS (SC-88) | 14 | 347 | 25–99 |
| XG Level 1 | 11 | 186 | 13–91 |
| **Core union (the four standards)** | **45** | **588 raw strings → 184 distinct sounds** | **13–108** |
| GS extension (SC-88Pro) | 25 | 676 | — |
| GS extension (SC-8850) | 37 | 1153 | — |
| XG extension (MU1000/MU2000) | 44 | 981 | — |

### 1.4 Caveats

- **UNVERIFIED against the paid primary specs.** GM1/GM2 names are taken from a
  third-party transcription of MMA RP-024; GS/XG names from third-party transcriptions of
  Roland/Yamaha manuals. GM1 was independently cross-checked (§1.1). GM2/GS/XG were not
  cross-checked against a second independent source; spelling may differ by a space or a
  hyphen from the printed spec. **Sound identity is reliable; exact spelling is not.**
- The GS "base" nine sets in VMPK's `gmgsxg.ins` are the SC-55-era GS sets; they agree
  with the SC-55 sections of the SC-8850 file (158 vs 193 distinct strings — the SC-8850
  file additionally carries the SC-55 CM-64/32L set and the SFX-set high notes).
- XG Level 1 kit membership is taken from VMPK's file (11 kits). The MU-series files add
  33 further kits that are **not** part of XG Level 1.
---

## 2. The extracted vocabularies

### 2.1 GM Level 1 — percussion key map, all 47 sounds (notes 35–81)

Source: `jpcima/gm-xg-gs` `instrument/GM1_GM2.ins`, section `[General MIDI Level 2 STANDARD Set]`, notes 35–81 (GM2's Standard set is by definition GM1-compatible on 35–81). Cross-checked against `DigitalInBlue/ReaperNoteNames/generalmidi_drums.txt`.

| Note | Name | Note | Name | Note | Name |
|---|---|---|---|---|---|
| 35 | Acoustic Bass Drum | 51 | Ride Cymbal 1 | 67 | High Agogo |
| 36 | Bass Drum 1 | 52 | Chinese Cymbal | 68 | Low Agogo |
| 37 | Side Stick | 53 | Ride Bell | 69 | Cabasa |
| 38 | Acoustic Snare | 54 | Tambourine | 70 | Maracas |
| 39 | Hand Clap | 55 | Splash Cymbal | 71 | Short Whistle |
| 40 | Electric Snare | 56 | Cowbell | 72 | Long Whistle |
| 41 | Low Floor Tom | 57 | Crash Cymbal 2 | 73 | Short Guiro |
| 42 | Closed Hi-hat | 58 | Vibra-slap | 74 | Long Guiro |
| 43 | High Floor Tom | 59 | Ride Cymbal 2 | 75 | Claves |
| 44 | Pedal Hi-hat | 60 | High Bongo | 76 | Hi Wood Block |
| 45 | Low Tom | 61 | Low Bongo | 77 | Low Wood Block |
| 46 | Open Hi-hat | 62 | Mute Hi Conga | 78 | Mute Cuica |
| 47 | Low-Mid Tom | 63 | Open Hi Conga | 79 | Open Cuica |
| 48 | High Mid Tom | 64 | Low Conga | 80 | Mute Triangle |
| 49 | Crash Cymbal 1 | 65 | High Timbale | 81 | Open Triangle |
| 50 | High Tom | 66 | Low Timbale |  |  |

**47 sounds.** GM1 defines nothing below 35 or above 81; notes outside that range are undefined by GM1.

### 2.2 GM Level 2 — additional notes and the nine percussion sets

Source: `jpcima/gm-xg-gs` `instrument/GM1_GM2.ins` (transcription of MMA **RP-024**).

#### 2.2.1 Notes GM2 adds outside the GM1 range

| Note | Standard-set name | | Note | Standard-set name |
|---|---|---|---|---|
| 27 | High Q |  | 82 | Shaker |
| 28 | Slap |  | 83 | Jingle Bell |
| 29 | Scratch Push |  | 84 | Bell Tree |
| 30 | Scratch Pull |  | 85 | Castanets |
| 31 | Sticks |  | 86 | Mute Surdo |
| 32 | Square Click |  | 87 | Open Surdo |
| 33 | Metronome Click |  |  |  |
| 34 | Metronome Bell |  |  |  |

Note **88 = Applause** exists only in the ORCHESTRA set. The SFX set is a wholesale replacement occupying 39–84.

GM2 percussion selection: Bank Select **MSB 120 / LSB 0**, then **Program Change selects the set**. Program numbers below are 0-based (`Key[120,n]` entries in the `.ins` file); add 1 for the 1-based numbers printed in the spec.

| Set | Program # (0-based) | Overridden notes vs Standard |
|---|---|---|
| STANDARD | 0 | — (base, 62 notes: 27–87) |
| ROOM | 8 | 6: 41, 43, 45, 47, 48, 50 |
| POWER | 16 | 8: 36, 38, 41, 43, 45, 47, 48, 50 |
| ELECTRONIC | 24 | 10: 36, 38, 40, 41, 43, 45, 47, 48, 50, 52 |
| ANALOG | 25 | 19: 36, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 56, 62, 63, 64, 70, 75 |
| JAZZ | 32 | 2: 35, 36 |
| BRUSH | 40 | 5: 35, 36, 38, 39, 40 |
| ORCHESTRA | 48 | 25: 27, 28, 29, 30, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 57, 59, 88 |
| SFX | 56 | **all 46** (39–84) — an independent map, shares nothing with Standard |

#### 2.2.2 Exactly what changes per set (exhaustive)

**ROOM** — 41=Room Low Tom 2; 43=Room Low Tom 1; 45=Room Mid Tom 2; 47=Room Mid Tom 1; 48=Room Hi Tom 2; 50=Room Hi Tom 1

**POWER** — 36=Power Kick Drum; 38=Power Snare Drum; 41=Power Low Tom 2; 43=Power Low Tom 1; 45=Power Mid Tom 2; 47=Power Mid Tom 1; 48=Power Hi Tom 2; 50=Power Hi Tom 1

**ELECTRONIC** — 36=Electric Bass Drum; 38=Electric Snare 1; 40=Electric Snare 2; 41=Electric Low Tom 2; 43=Electric Low Tom 1; 45=Electric Mid Tom 2; 47=Electric Mid Tom 1; 48=Electric Hi Tom 2; 50=Electric Hi Tom 1; 52=Reverse Cymbal

**ANALOG** — 36=Analog Bass Drum; 37=Analog Rim Shot; 38=Analog Snare 1; 41=Analog Low Tom 2; 42=Analog CHH 1; 43=Analog Low Tom 1; 44=Analog CHH 2; 45=Analog Mid Tom 2; 46=Analog OHH; 47=Analog Mid Tom 1; 48=Analog Hi Tom 2; 49=Analog Cymbal; 50=Analog Hi Tom 1; 56=Analog Cowbell; 62=Analog High Conga; 63=Analog Mid Conga; 64=Analog Low Conga; 70=Analog Maracas; 75=Analog Claves

**JAZZ** — 35=Jazz Kick 2; 36=Jazz Kick 1

**BRUSH** — 35=Jazz Kick 2; 36=Jazz Kick 1; 38=Brush Tap; 39=Brush Slap; 40=Brush Swirl

**ORCHESTRA** — 27=Closed Hi-hat 2; 28=Pedal Hi-hat; 29=Open Hi-hat 2; 30=Ride Cymbal 1; 35=Concert BD 2; 36=Concert BD 1; 38=Concert SD; 39=Castanets; 40=Concert SD; 41=Timpani F; 42=Timpani F#; 43=Timpani G; 44=Timpani G#; 45=Timpani A; 46=Timpani A#; 47=Timpani B; 48=Timpani c; 49=Timpani c#; 50=Timpani d; 51=Timpani d#; 52=Timpani e; 53=Timpani f; 57=Concert Cymbal 2; 59=Concert Cymbal 1; 88=Applause

**SFX** — 39=High Q; 40=Slap; 41=Scratch Push; 42=Scratch Pull; 43=Sticks; 44=Square Click; 45=Metronome Click; 46=Metronome Bell; 47=Guitar Fret Noise; 48=Guitar Cutting Noise Up; 49=Guitar Cutting Noise Down; 50=String Slap of Double Bass; 51=Fl.Key Click; 52=Laughing; 53=Scream; 54=Punch; 55=Heart Beat; 56=Footsteps 1; 57=Footsteps 2; 58=Applause; 59=Door Creaking; 60=Door; 61=Scratch; 62=Wind Chimes; 63=Car-Engine; 64=Car-Stop; 65=Car-Pass; 66=Car-Crash; 67=Siren; 68=Train; 69=Jetplane; 70=Helicopter; 71=Starship; 72=Gun Shot; 73=Machine Gun; 74=Lasergun; 75=Explosion; 76=Dog; 77=Horse-Gallop; 78=Birds; 79=Rain; 80=Thunder; 81=Wind; 82=Seashore; 83=Stream; 84=Bubble

**Set-dependence summary.** Across the six *kit-variant* sets (Room, Power, Electronic,
Analog, Jazz, Brush) the set-dependent notes are exactly
**35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 56, 62, 63, 64, 70, 75** (23 notes).
Everything else (27–34, 51, 53–55, 57–61, 65–69, 71–74, 76–87) is **set-invariant** in GM2.
The Orchestra set additionally rewrites 27–30, 51, 53, 57, 59 and adds 88; the SFX set replaces the map entirely.

### 2.3 Roland GS — SC-55 drum sets (the original GS map)

Source: `jpcima/gm-xg-gs` `instrument/Roland_SC-8850.ins`, sections `[Roland SC-55 * Set]` (the SC-8850 reproduces the SC-55 map for compatibility mode). 10 sets, 193 distinct name strings. GS selects drum sets by Program Change on a percussion part (bank irrelevant for the set choice).

**Base set `STANDARD Set` — full map (61 notes):**

| Note | Name | Note | Name | Note | Name |
|---|---|---|---|---|---|
| 27 | High Q | 48 | High Tom 2 | 69 | Cabasa |
| 28 | Slap | 49 | Crash Cymbal 1 | 70 | Maracas |
| 29 | Scratch Push | 50 | High Tom 1 | 71 | Short Hi Whistle |
| 30 | Scratch Pull | 51 | Ride Cymbal 1 | 72 | Long Low Whistle |
| 31 | Sticks | 52 | Chinese Cymbal | 73 | Short Guiro |
| 32 | Square Click | 53 | Ride Bell | 74 | Long Guiro |
| 33 | Metronome Click | 54 | Tambourine | 75 | Claves |
| 34 | Metronome Bell | 55 | Splash Cymbal | 76 | High Wood Block |
| 35 | Kick Drum 2 | 56 | Cowbell | 77 | Low Wood Block |
| 36 | Kick Drum 1 | 57 | Crash Cymbal 2 | 78 | Mute Cuica |
| 37 | Side Stick | 58 | Vibra-slap | 79 | Open Cuica |
| 38 | Snare Drum 1 | 59 | Ride Cymbal 2 | 80 | Mute Triangle |
| 39 | Hand Clap | 60 | High Bongo | 81 | Open Triangle |
| 40 | Snare Drum 2 | 61 | Low Bongo | 82 | Shaker |
| 41 | Low Tom 2 | 62 | Mute High Conga | 83 | Jingle Bell |
| 42 | Closed Hi-Hat | 63 | Open High Conga | 84 | Belltree |
| 43 | Low Tom 1 | 64 | Low Conga | 85 | Castanets |
| 44 | Pedal Hi-Hat | 65 | High Timbale | 86 | Mute Surdo |
| 45 | Mid Tom 2 | 66 | Low Timbale | 87 | Open Surdo |
| 46 | Open Hi-Hat | 67 | High Agogo |  |  |
| 47 | Mid Tom 1 | 68 | Low Agogo |  |  |

**Every other set, as a diff against the base (exhaustive):**

- **BRUSH Set** (5 changed): `35`=Jazz BD 2; `36`=Jazz BD 1; `38`=Brush Tap; `39`=Brush Slap; `40`=Brush Swirl
- **CM-64/32L Set** (67 changed, absent: 27, 28, 29, 30, 31, 32, 33, 34, 52, 53, 55, 57, 58, 59, 74): `35`=CM Kick Bass Drum; `36`=CM Kick Bass Drum; `37`=CM Rim Shot; `38`=CM Snare Drum; `39`=CM Hand Clap; `40`=CM Electronic Snare Drum; `41`=CM Acoustic Low Tom; `42`=CM Closed High Hat; `43`=CM Acoustic Low Tom; `44`=CM Open High Hat 2; `45`=CM M.Acoustic Middle Tom; `46`=CM Open High Hat 1; `47`=CM M.TomAcoustic Middle Tom; `48`=CM Acoustic High Tom; `49`=CM Crash Cymbal; `50`=CM Acoustic High Tom; `51`=CM Ride Cymbal; `54`=CM Tambourine; `56`=CM Cowbell; `60`=CM High Bongo; `61`=CM Low Bongo; `62`=CM Mute High Conga; `63`=CM High Conga; `64`=CM Low Conga; `65`=CM High Timbale; `66`=CM Low Timbale; `67`=CM High Agogo; `68`=CM Low Agogo; `69`=CM Cabasa; `70`=CM Maracas; `71`=CM Short Whistle; `72`=CM Long Whistle; `73`=CM Vibrato Slap; `75`=CM Claves; `76`=Laughing; `77`=Screaming; `78`=Punch; `79`=Heartbeat; `80`=Footsteps 1; `81`=Footsteps 2; `82`=Applause; `83`=Creaking; `84`=Door; `85`=Scratch; `86`=Wind Chimes; `87`=Car-Engine; `88`=Car-Stop; `89`=Car-Pass; `90`=Car-Crash; `91`=Siren; `92`=Train; `93`=Jetplane; `94`=Helicopter; `95`=Starship; `96`=Gun Shot; `97`=Machine Gun; `98`=Lasergun; `99`=Explosion; `100`=Dog; `101`=Horse-Gallop; `102`=Birds; `103`=Rain; `104`=Thunder; `105`=Wind; `106`=Waves; `107`=Stream; `108`=Bubble
- **ELECTRONIC Set** (10 changed): `36`=Elec BD; `38`=Elec SD; `40`=Gated SD; `41`=Elec Low Tom 2; `43`=Elec Low Tom 1; `45`=Elec Mid Tom 2; `47`=Elec Mid Tom 1; `48`=Elec Hi Tom 2; `50`=Elec Hi Tom 1; `52`=Reverse Cymbal
- **JAZZ Set** (2 changed): `35`=Jazz BD 2; `36`=Jazz BD 1
- **ORCHESTRA Set** (25 changed): `27`=Closed Hi-Hat; `28`=Pedal Hi-Hat; `29`=Open Hi-Hat; `30`=Ride Cymbal; `35`=Concert BD 2; `36`=Concert BD 1; `38`=Concert SD; `39`=Castanets; `40`=Concert SD; `41`=Timpani F; `42`=Timpani F#; `43`=Timpani G; `44`=Timpani G#; `45`=Timpani A; `46`=Timpani A#; `47`=Timpani B; `48`=Timpani c; `49`=Timpani c#; `50`=Timpani d; `51`=Timpani d#; `52`=Timpani e; `53`=Timpani f; `57`=Concert Cymbal 2; `59`=Concert Cymbal 1; `88`=Applause
- **POWER Set** (8 changed): `36`=MONDO Kick; `38`=Gated SD; `41`=Room Low Tom 2; `43`=Room Low Tom 1; `45`=Room Mid Tom 2; `47`=Room Mid Tom 1; `48`=Room Hi Tom 2; `50`=Room Hi Tom 1
- **ROOM Set** (6 changed): `41`=Room Low Tom 2; `43`=Room Low Tom 1; `45`=Room Mid Tom 2; `47`=Room Mid Tom 1; `48`=Room Hi Tom 2; `50`=Room Hi Tom 1
- **SFX Set** (46 changed, absent: 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 85, 86, 87): `39`=High Q; `40`=Slap; `41`=Scratch Push; `42`=Scratch Pull; `43`=Sticks; `44`=Square Click; `45`=Metronome Click; `46`=Metronome Bell; `47`=Guitar Fret Noise; `48`=Guitar cutting noise / up; `49`=Guitar cutting noise /down; `50`=String slap of double Bass; `51`=Fl.Key click; `52`=Laughing; `53`=Screaming; `54`=Punch; `55`=Heart Beat; `56`=Footsteps 1; `57`=Footsteps 2; `58`=Applause; `59`=Door Creaking; `60`=Door; `61`=Scratch; `62`=Windchimes; `63`=Car-Engine; `64`=Car-Stop; `65`=Car-Pass; `66`=Car-Crash; `67`=Siren; `68`=Train; `69`=Jetplane; `70`=Helicopter; `71`=Starship; `72`=Gun Shot; `73`=Machine Gun; `74`=Lasergun; `75`=Explosion; `76`=Dog; `77`=Horse-Gallop; `78`=Birds; `79`=Rain; `80`=Thunder; `81`=Wind; `82`=Seashore; `83`=Stream; `84`=Bubble
- **TR-808 Set** (19 changed): `36`=808 Bass Drum; `37`=808 Rim Shot; `38`=808 Snare Drum; `41`=808 Low Tom 2; `42`=808 CHH; `43`=808 Low Tom 1; `44`=808 CHH; `45`=808 Mid Tom 2; `46`=808 OHH; `47`=808 Mid Tom 1; `48`=808 Hi Tom 2; `49`=808 Cymbal; `50`=808 Hi Tom 1; `56`=808 Cowbell; `62`=808 High Conga; `63`=808 Mid Conga; `64`=808 Low Conga; `70`=808 Maracas; `75`=808 Claves

### 2.4 Roland GS — SC-88 drum sets

Source: same file, sections `[Roland SC-88 * Set]`. 14 sets, 347 distinct name strings. SC-88 both extends the GS map upward (to note 99) and downward (to note 25) and introduces per-kit *named* kick/snare pairs (`Standard 1 Kick 1`, `Room Snare 2`, …) exposed on high notes, so one kit can address several kits' kick/snare samples simultaneously.

**Base set `STANDARD 1 Set` — full map (63 notes):**

| Note | Name | Note | Name | Note | Name |
|---|---|---|---|---|---|
| 25 | Snare Roll | 46 | Open Hi-hat | 67 | High Agogo |
| 26 | Finger Snap | 47 | Mid Tom 1 | 68 | Low Agogo |
| 27 | High Q | 48 | High Tom 2 | 69 | Cabasa |
| 28 | Slap | 49 | Crash Cymbal 1 | 70 | Maracas |
| 29 | Scratch Push | 50 | High Tom 1 | 71 | Short Hi Whistle |
| 30 | Scratch Pull | 51 | Ride Cymbal 1 | 72 | Long Low Whistle |
| 31 | Sticks | 52 | Chinese Cymbal | 73 | Short Guiro |
| 32 | Square Click | 53 | Ride Bell | 74 | Long Guiro |
| 33 | Metronome Click | 54 | Tambourine | 75 | Claves |
| 34 | Metronome Bell | 55 | Splash Cymbal | 76 | High Wood Block |
| 35 | Standard 1 Kick 2 | 56 | Cowbell | 77 | Low Wood Block |
| 36 | Standard 1 Kick 1 | 57 | Crash Cymbal 2 | 78 | Mute Cuica |
| 37 | Side Stick | 58 | Vibra-slap | 79 | Open Cuica |
| 38 | Standard 1 Snare 1 | 59 | Ride Cymbal 2 | 80 | Mute Triangle |
| 39 | Hand Clap | 60 | High Bongo | 81 | Open Triangle |
| 40 | Standard 1 Snare 2 | 61 | Low Bongo | 82 | Shaker |
| 41 | Low Tom 2 | 62 | Mute High Conga | 83 | Jingle Bell |
| 42 | Closed Hi-hat 1 | 63 | Open High Conga | 84 | Bell Tree |
| 43 | Low Tom 1 | 64 | Low Conga | 85 | Castanets |
| 44 | Pedal Hi-hat | 65 | High Timbale | 86 | Mute Surdo |
| 45 | Mid Tom 2 | 66 | Low Timbale | 87 | Open Surdo |

**Every other set, as a diff against the base (exhaustive):**

- **BRUSH Set** (16 changed): `35`=Jazz Kick 2; `36`=Jazz Kick 1; `38`=Brush Tap 1; `39`=Brush Slap 1; `40`=Brush Swirl 1; `41`=Brush Low Tom 2; `42`=Brush Closed Hi-hat; `43`=Brush Low Tom 1; `45`=Brush Mid Tom 2; `46`=Brush Open Hi-hat; `47`=Brush Mid Tom 1; `48`=Brush Hi Tom 2; `49`=Brush Crash Cymbal; `50`=Brush Hi Tom 1; `51`=Brush Ride Cymbal; `53`=Brush Ride Bell
- **DANCE Set** (20 changed): `29`=Scratch Push 2; `30`=Scratch Pull 2; `35`=Dance Kick; `36`=Electric Kick 2; `38`=Dance Snare 1; `40`=Dance Snare 2; `41`=Electric Low Tom 2; `42`=CR-78 CHH; `43`=Electric Low Tom 1; `44`=808 CHH; `45`=Electric Mid Tom 2; `46`=CR-78 OHH; `47`=Electric Mid Tom 1; `48`=Electric High Tom 2; `50`=Electric High Tom 1; `52`=Reverse Cymbal; `78`=High Hoo; `79`=Low Hoo; `80`=Electric Mute Triangle; `81`=Electric Open Triangle
- **ELECTRONIC Set** (15 changed): `29`=Scratch Push 2; `30`=Scratch Pull 2; `35`=Electric Kick 2; `36`=Electric Kick 1; `38`=Electric Snare 1; `40`=Electric Snare 2; `41`=Electric Low Tom 2; `42`=Closed Hi-hat 2; `43`=Electric Low Tom 1; `45`=Electric Mid Tom 2; `46`=Open Hi-hat 2; `47`=Electric Mid Tom 1; `48`=Electric Hi Tom 2; `50`=Electric Hi Tom 1; `52`=Reverse Cymbal
- **ETHNIC Set** (75 changed): `25`=Finger Snap; `26`=Tambourine; `27`=Castanets; `28`=Crash Cymbal 1; `29`=Snare Roll; `30`=Concert Snare Drum; `31`=Concert Cymbal; `32`=Concert BD 1; `33`=Jingle Bell; `34`=Bell Tree; `35`=Bar Chimes; `36`=Wadaiko; `37`=Wadaiko Rim; `38`=Shime Taiko; `39`=Atarigane; `40`=Hyoushigi; `41`=Ohkawa; `42`=High Kotsuzumi; `43`=Low Kotsuzumi; `44`=Ban Gu; `45`=Big Gong; `46`=Small Gong; `47`=Bend Gong; `48`=Thai Gong; `49`=Rama Cymbal; `50`=Gamelan Gong; `51`=Udo Short; `52`=Udo Long; `53`=Udo Slap; `54`=Bendir; `55`=Req Dum; `56`=Req Tik; `57`=Tabla Te; `58`=Tabla Na; `59`=Tabla Tun; `60`=Tabla Ge; `61`=Tabla Ge Hi; `62`=Talking Drum; `63`=Bend Talking Drum; `64`=Caxixi; `65`=Djembe; `66`=Djembe Rim; `67`=Timbales Low; `68`=Timbales Paila; `69`=Timbales High; `70`=Cowbell; `71`=Hi Bongo; `72`=Low Bongo; `73`=Mute Hi Conga; `74`=Open Hi Conga; `75`=Mute Low Conga; `76`=Conga Slap; `77`=Open Low Conga; `78`=Conga Slide; `79`=Mute Pandiero; `80`=Open Pandiero; `81`=Open Surdo; `82`=Mute Surdo; `83`=Tamborim; `84`=High Agogo; `85`=Low Agogo; `86`=Shaker; `87`=High Whistle; `88`=Low Whistle; `89`=Mute Cuica; `90`=Open Cuica; `91`=Mute Triangle; `92`=Open Triangle; `93`=Short Guiro; `94`=Long Guiro; `95`=Cabasa Up; `96`=Cabasa Down; `97`=Claves; `98`=High Wood Block; `99`=Low Wood Block
- **JAZZ Set** (7 changed): `35`=Jazz Kick 2; `36`=Jazz Kick 1; `38`=Jazz Snare 1; `39`=Hand Clap2; `40`=Jazz Snare 2; `42`=Closed Hi-hat 2; `46`=Open Hi-hat 2
- **KICK & SNARE Set** (52 changed, absent: 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39): `40`=Standard 1 Kick 1; `41`=Standard 1 Kick 2; `42`=Standard 2 Kick 1; `43`=Standard 2 Kick 2; `44`=Kick 1; `45`=Kick 2; `46`=Soft Kick; `47`=Jazz Kick 1; `48`=Jazz Kick 2; `49`=Concert BD; `50`=Room Kick 1; `51`=Room Kick 2; `52`=Power Kick 1; `53`=Power Kick 2; `54`=Electric Kick 2; `55`=Electric Kick 1; `56`=Electric Kick; `57`=808 Bass Drum; `58`=909 Bass Drum; `59`=Dance Kick; `60`=Standard 1 Snare 1; `61`=Standard 1 Snare 2; `62`=Standard 2 Snare 1; `63`=Standard 2 Snare 2; `64`=Tight Snare; `65`=Concert Snare; `66`=Jazz Snare 1; `67`=Jazz Snare 2; `68`=Room Snare 1; `69`=Room Snare 2; `70`=Power Snare 1; `71`=Power Snare 2; `72`=Gated Snare; `73`=Dance Snare 1; `74`=Dance Snare 2; `75`=Disco Snare; `76`=Electric Snare 2; `77`=House Snare; `78`=Electric Snare 1; `79`=Electric Snare 3; `80`=808 Snare 1; `81`=808 Snare 2; `82`=909 Snare 1; `83`=909 Snare 2; `84`=Brush Tap 1; `85`=Brush Tap 2; `86`=Brush Slap 1; `87`=Brush Slap 2; `88`=Brush Slap 3; `89`=Brush Swirl 1; `90`=Brush Swirl 2; `91`=Brush Long Swirl
- **ORCHESTRA Set** (25 changed): `27`=Closed Hi Hat 2; `28`=Pedal Hi Hat; `29`=Open Hi Hat 2; `30`=Ride Cymbal 1; `35`=Jazz Kick 1; `36`=Concert BD 1; `38`=Concert SD; `39`=Castanets; `40`=Concert SD; `41`=Timpani F; `42`=Timpani F#; `43`=Timpani G; `44`=Timpani G#; `45`=Timpani A; `46`=Timpani A#; `47`=Timpani B; `48`=Timpani c; `49`=Timpani c#; `50`=Timpani d; `51`=Timpani d#; `52`=Timpani e; `53`=Timpani f; `57`=Concert Cymbal 2; `59`=Concert Cymbal 1; `88`=Applause
- **POWER Set** (12 changed): `35`=Power Kick 2; `36`=Power Kick 1; `38`=Power Snare 1; `40`=Power Snare 2; `41`=Power Low Tom 2; `42`=Closed Hi-hat 3; `43`=Power Low Tom 1; `45`=Power Mid Tom 2; `46`=Open Hi-hat 3; `47`=Power Mid Tom 1; `48`=Power Hi Tom2; `50`=Power Hi Tom 1
- **RHYTHM FX Set** (53 changed, absent: 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35): `36`=Reverse Kick 1; `37`=Reverse Concert BD 1; `38`=Reverse Power Kick 1; `39`=Reverse Electric Kick 1; `40`=Reverse Snare 1; `41`=Reverse Snare 2; `42`=Reverse Standard Set 1 Snare 1; `43`=Reverse Tight Snare; `44`=Reverse Dance Snare; `45`=Reverse 808 Snare; `46`=Reverse Tom 1; `47`=Reverse Tom 2; `48`=Reverse Sticks; `49`=Reverse Slap; `50`=Reverse Cymbal 1; `51`=Reverse Cymbal 2; `52`=Reverse Open Hi-hat; `53`=Reverse Ride Cymbal; `54`=Reverse CR-78 OHH; `55`=Reverse Closed Hi-hat; `56`=Reverse Gong; `57`=Reverse Bell Tree; `58`=Reverse Guiro; `59`=Reverse Bendir; `60`=Reverse Gun Shot; `61`=Reverse Scratch; `62`=Reverse Laser; `63`=Key Click; `64`=Tekno Trip; `65`=Pop Drop; `66`=Woody Slap; `67`=Distortion Kick; `68`=Syn.Drop; `69`=Reverse High Q; `70`=Pipe; `71`=Ice Block; `72`=Digital Tambourine; `73`=Alias; `74`=Modulated Bell; `75`=Spark; `76`=Metalic Percussion; `77`=Velocity Noise FX; `78`=Stereo Noise Clap; `79`=Swish; `80`=Slappy; `81`=Voice Ou; `82`=Voice Au; `83`=Hoo; `84`=Tape Stop 1; `85`=Tape Stop 2; `86`=Missile; `87`=Space Bird; `88`=Flying Monster
- **ROOM Set** (12 changed): `35`=Room Kick 2; `36`=Room Kick 1; `38`=Room Snare 1; `40`=Room Snare 2; `41`=Room Low Tom2; `42`=Closed Hi-hat 3; `43`=Room Low Tom 1; `45`=Room Mid Tom 2; `46`=Open Hi-Hat 3; `47`=Room Mid Tom 1; `48`=Room Hi Tom 2; `50`=Room Hi Tom 1
- **SFX Set** (60 changed, absent: 25, 26, 27, 28, 29, 30): `31`=Scratch Push 2; `32`=Scratch Pull 2; `33`=Cutting Noise 2 Up; `34`=Cutting Noise 2 Down; `35`=Distortion Guitar Cutting Noise Up; `36`=Distortion Guitar Cutting Noise Down; `37`=Bass Slide; `38`=Pick Scrape; `39`=High Q; `40`=Slap; `41`=Scratch Push; `42`=Scratch Pull; `43`=Sticks; `44`=Square Click; `45`=Metronome Click; `46`=Metronome Bell; `47`=Guitar Fret Noise; `48`=Guitar Cutting Noise Up; `49`=Guitar Cutting Noise Down; `50`=String Slap of Double Bass; `51`=Fl.Key Click; `52`=Laughing; `53`=Scream; `54`=Punch; `55`=Heart Beat; `56`=Footsteps 1; `57`=Footsteps 2; `58`=Applause; `59`=Door Creaking; `60`=Door; `61`=Scratch; `62`=Wind Chimes; `63`=Car-Engine; `64`=Car-Stop; `65`=Car-Pass; `66`=Car-Crash; `67`=Siren; `68`=Train; `69`=Jetplane; `70`=Helicopter; `71`=Starship; `72`=Gun Shot; `73`=Machine Gun; `74`=Lasergun; `75`=Explosion; `76`=Dog; `77`=Horse-Gallop; `78`=Birds; `79`=Rain; `80`=Thunder; `81`=Wind; `82`=Seashore; `83`=Stream; `84`=Bubble; `85`=Kitty; `86`=Bird 2; `87`=Growl; `88`=Applause 2; `89`=Telephone 1; `90`=Telephone 2
- **STANDARD 2 Set** (7 changed): `35`=Standard 2 Kick 2; `36`=Standard 2 Kick 1; `38`=Standard 2 Snare 1; `40`=Standard 2 Snare 2; `42`=Closed Hi-hat 2; `46`=Open Hi-hat 2; `84`=Bar Chimes
- **TR-808/909 Set** (23 changed): `29`=Scratch Push 2; `30`=Scratch Pull 2; `35`=909 Bass Drum; `36`=808 Bass Drum; `37`=808 Rim Shot; `38`=808 Snare 1; `40`=909 Snare 1; `41`=808 Low Tom 2; `42`=808 CHH; `43`=808 Low Tom 1; `44`=808 CHH; `45`=808 Mid Tom 2; `46`=808 OHH; `47`=808 Mid Tom 1; `48`=808 Hi Tom 2; `49`=808 Cymbal; `50`=808 Hi Tom 1; `56`=808 Cowbell; `62`=808 High Conga; `63`=808 Mid Conga; `64`=808 Low Conga; `70`=808 Maracas; `75`=808 Claves

### 2.5 Yamaha XG — the eleven XG Level 1 drum kits

Source: `pedrolcl/VMPK` `data/gmgsxg.ins`, sections `[XG * Kit]` / `[XG SFX *]`. 11 kits, 186 distinct name strings, note range **13–91** — the widest of the four standards. XG selects kits by Bank Select MSB 127 (128 for SFX kits) + Program Change.

**Base set `Standard Kit` — full map (72 notes):**

| Note | Name | Note | Name | Note | Name |
|---|---|---|---|---|---|
| 13 | Surdo Mute | 37 | Side Stick | 61 | Bongo L |
| 14 | Surdo Open | 38 | Snare M | 62 | Conga H Mute |
| 15 | Hi Q | 39 | Hand Clap | 63 | Conga H Open |
| 16 | Whip Slap | 40 | Snare H | 64 | Conga L |
| 17 | Scratch Push | 41 | Floor Tom L | 65 | Timbale H |
| 18 | Scratch Pull | 42 | Hi-Hat Closed | 66 | Timbale L |
| 19 | Finger Snap | 43 | Floor Tom H | 67 | Agogo H |
| 20 | Click Noise | 44 | Hi-Hat Pedal | 68 | Agogo L |
| 21 | Metronome Click | 45 | Low Tom | 69 | Cabasa |
| 22 | Metronome Bell | 46 | Hi-Hat Open | 70 | Maracas |
| 23 | Seq Click L | 47 | Mid Tom L | 71 | Samba Whistle H |
| 24 | Seq Click H | 48 | Mid Tom H | 72 | Samba Whistle L |
| 25 | Brush Tap | 49 | Crash Cymbal 1 | 73 | Guiro Short |
| 26 | Brush Swirl L | 50 | High Tom | 74 | Guiro Long |
| 27 | Brush Slap | 51 | Ride Cymbal 1 | 75 | Claves |
| 28 | Brush Swirl H | 52 | Chinese Cymbal | 76 | Wood Block H |
| 29 | Snare Roll | 53 | Ride Cymbal Cup | 77 | Wood Block L |
| 30 | Castanet | 54 | Tambourine | 78 | Cuica Mute |
| 31 | Snare L | 55 | Splash Cymbal | 79 | Cuica Open |
| 32 | Sticks | 56 | Cowbell | 80 | Triangle Mute |
| 33 | Bass Drum L | 57 | Crash Cymbal 2 | 81 | Triangle Open |
| 34 | Open Rim Shot | 58 | Vibraslap | 82 | Shaker |
| 35 | Bass Drum M | 59 | Ride Cymbal 2 | 83 | Jingle Bell |
| 36 | Bass Drum H | 60 | Bongo H | 84 | Bell Tree |

**Every other set, as a diff against the base (exhaustive):**

- **Analog Kit** (27 changed): `28`=Reverse Cymbal; `30`=Hi Q; `31`=SD Rock H; `33`=Bass Drum M; `35`=BD Analog L; `36`=BD Analog H; `37`=Analog Side Stick; `38`=Analog Snare L; `40`=Analog Snare H; `41`=Analog Tom 1; `42`=Analog HH Closed 1; `43`=Analog Tom 2; `44`=Analog HH Closed 2; `45`=Analog Tom 3; `46`=Analog HH Open; `47`=Analog Tom 4; `48`=Analog Tom 5; `49`=Analog Cymbal; `50`=Analog Tom 6; `56`=Analog Cowbell; `62`=Analog Conga H; `63`=Analog Conga M; `64`=Analog Conga L; `70`=Analog Maracas; `75`=Analog Claves; `78`=Scratch Push; `79`=Scratch Pull
- **Brush Kit** (10 changed): `31`=Brush Slap L; `36`=BD Soft; `38`=Brush Slap; `40`=Brush Tap; `41`=Brush Tom 1; `43`=Brush Tom 2; `45`=Brush Tom 3; `47`=Brush Tom 4; `48`=Brush Tom 5; `50`=Brush Tom 6
- **Classic Kit** (11 changed): `36`=Gran Casa; `41`=Jazz Tom 1; `43`=Jazz Tom 2; `45`=Jazz Tom 3; `47`=Jazz Tom 4; `48`=Jazz Tom 5; `49`=Hand Cym.Open L; `50`=Jazz Tom 6; `51`=Hand Cym.Closed L; `57`=Hand Cym.Open H; `59`=Hand Cym.Closed H
- **Electro Kit** (16 changed): `28`=Reverse Cymbal; `30`=Hi Q; `31`=Snare M; `33`=Bass Drum H 4; `35`=BD Rock; `36`=BD Gate; `38`=SD Rock L; `40`=SD Rock H; `41`=E Tom 1; `43`=E Tom 2; `45`=E Tom 3; `47`=E Tom 4; `48`=E Tom 5; `50`=E Tom 6; `78`=Scratch Push; `79`=Scratch Pull
- **Jazz Kit** (7 changed): `36`=BD Jazz; `41`=Jazz Tom 1; `43`=Jazz Tom 2; `45`=Jazz Tom 3; `47`=Jazz Tom 4; `48`=Jazz Tom 5; `50`=Jazz Tom 6
- **Rock Kit** (12 changed): `31`=SD Rock M; `33`=Bass Drum M; `35`=Bass Drum H 3; `36`=BD Rock; `38`=SD Rock; `40`=SD Rock Rim; `41`=Rock Tom 1; `43`=Rock Tom 2; `45`=Rock Tom 3; `47`=Rock Tom 4; `48`=Rock Tom 5; `50`=Rock Tom 6
- **Room Kit** (7 changed): `36`=BD Room; `41`=Room Tom 1; `43`=Room Tom 2; `45`=Room Tom 3; `47`=Room Tom 4; `48`=Room Tom 5; `50`=Room Tom 6
- **SFX 1** (21 changed, absent: 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83): `36`=Guitar Cutting Noise; `37`=Guitar Cutting Noise 2; `38`=Dist. Cut Noise; `39`=String Slap; `40`=Bass Slide; `41`=Pick Scrape; `52`=FL.Key Click; `68`=Rain; `69`=Thunder; `70`=Wind; `71`=Stream; `72`=Bubble; `73`=Feed; `84`=Dog; `85`=Horse Gallop; `86`=Bird 2; `87`=Kitty; `88`=Growl; `89`=Haunted; `90`=Ghost; `91`=Maou
- **SFX 2** (18 changed, absent: 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 43, 44, 45, 46, 47, 48, 49, 50, 51, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84): `36`=Dial Tone; `37`=Door Creaking; `38`=Door Slam; `39`=Scratch; `40`=Scratch 2; `41`=Windchime; `42`=Telephone Ring2; `52`=Engine Start; `53`=Tire Screech; `54`=Car Passing; `55`=Crash; `56`=Siren; `57`=Train; `58`=Jetplane; `59`=Starship; `60`=Burst Noise; `61`=Coaster; `62`=SbMarine
- **Standard2 Kit** (5 changed): `34`=Open Rim Shot 2; `35`=Bass Drum M 2; `36`=Bass Drum H 2; `38`=Snare M 2; `40`=Snare H 2

### 2.6 Vendor extensions beyond the four standards (SC-88Pro / SC-8850, MU100–MU2000)

Not part of "the standards", but they are the same vendors' own successors and they tell
you where the standards' vocabulary was heading. Extracted for structural evidence only;
the raw list is in `research/data/ext_families.txt` (1520 name families beyond the core
588 strings).

**Structural findings that a GM/GS/XG-shaped vocabulary cannot represent but Roland/Yamaha
themselves needed:**

| Finding | Evidence (SC-8850 `CYMBAL&CLAPS` / `CYM&CLAPS 2` sets, notes as listed) | Axis it implies |
|---|---|---|
| Hi-hat openness is a **graded** axis, not 3 states | `Closed Hi-Hat`, `Closed Hi-Hat 2`, `Closed Hi-Hat 3`, `Closed Hi-Hat 4`, `Half-Open Hi-Hat 1`, `Half-Open Hi-Hat 2`, `Open Hi-Hat`, `Open Hi-Hat 2`, `Open Hi-Hat 3`, `Pedal Hi-Hat` — 10 openness steps on one instrument | ordinal `openness` (0..n) |
| **Cymbal choke exists** in GS | `Mute Crash Cymbal 1`, `Mute Crash Cymbal 2`, and per-kit `Standard 1 / Room / Jazz / Brush Mute Crash Cymbal` | `crash/choke` articulation |
| **Ride striking position** (radial zone) exists in GS | `Ride Cymbal Low Inner`, `Ride Cymbal Mid Inner`, `Ride Cymbal High Inner`, `Ride Cymbal Low Edge`, `Ride Cymbal Mid Edge`, `Ride Cymbal High Edge`, plus `Ride Bell` / `Ride Cymbal Cup` | `zone` = bell/bow(inner)/edge, orthogonal to instrument |
| **Kit-timbre is an independent axis** from sound identity | The same physical articulation is voiced per kit and *addressed simultaneously*: `Standard 1 Closed Hi-Hat` (36), `Room Closed Hi-Hat` (37), `Jazz Closed Hi-Hat` (38), `Brush Closed Hi-Hat` (39) all in one map | kit/voicing tag, not an instrument |
| **Reversed samples are a first-class articulation family** | 30+ `Reverse *` entries (`Reverse Crash Cymbal 1/2/3`, `Reverse Closed Hi-Hat`, `Reverse Snare 1/2`, `Reverse Kick 1`, `Reverse Tom 1/2`, `Reverse Guiro`, `Reverse Gong`, …) | `modifier: reverse` |
| **Drum-machine lineage is a named axis** | `TR-808 / TR-909 / TR-707 / TR-606 / CR-78` prefixes applied systematically to kick, snare, rim, CHH, OHH, crash, ride, claps, cowbell, claves, guiro, maracas, tambourine, bongo, toms | `source/machine` provenance tag |
| **Snare rim is per-kit and independent of side-stick** | `House Snare Rim`, `Jungle Snare Rim`, `LoFi Snare Rim`, `Dance Rim Shot`, `TR-808/909/707 Rim Shot`, `Rim Gate 1–5` | `snare/rimshot` distinct from `snare/sidestick` |
| Yamaha's XG-B extension is mostly a **filter/EQ variant axis**, not new sounds | Suffix markers on nearly every voice: `B`, `V`, `H`, `L`, `Q`, `Sk`, `HPF`, `BPF`, `Dark`, `Lo-Fi`, `Short`, `Tight`, `#` — e.g. `Crash Cymbal 1 B`, `Crash Cymbal 2 Dark`, `Conga H Mute HPF` | processed-variant tag, **not** vocabulary |
| Large **world-percussion** catalogue | Chinese: `Muyu High/Mid-High/Mid/Mid-Low/Low`, `Paigu High/Middle/Low`, `Dagu Heavy/Mute`, `Bangu`, `Banzi`, `Xiaoluo Open`, `Zhongluo Open/Mute`, `Zhongcha Open/Mute`. Korean: `Buk`, `Buk Rim`, `Jang-Gu Rim`, `Gengari f/p/Mute High/Mute Low/Small`. Indonesian gamelan: `Bonang 1–5`, `Gender 1–5`, `Gamelan Gong 1–20`, `Gamelan Gong Lanang/Wadon`, `Bebarongan`, `Ceng-Ceng`. Indian: `Dholak 1/2`, tabla strokes. Japanese: `Ohdaiko`, `Ohdaiko Rim`, `Gran Cassa` | open-ended `instrument` axis; a closed 12-value enum cannot hold it |
---

## 3. THE DELIVERABLE — normalised union of all four standards

**184 distinct percussion sounds**, reduced from 588 raw name strings by the rules in §1.2.
`named by` = which of the four standards names this sound (GM1 / GM2 / GS / XG; GS covers
SC-55 and SC-88 together). `note range` = the lowest and highest MIDI note on which any of
the four standards places this sound — the spread is itself the argument against
note-number-based identity. The last column is the answer to *"can drum-remap's
12-instrument model express this?"*:

- **YES** — an exact `instrument/articulation` pair already exists in drum-remap.
- **LOSSY** — drum-remap has a tag it can be forced into, but doing so **discards a
  distinction the standard makes** (acoustic vs analog-drum-machine vs orchestral timbre).
  Inverting the map cannot recover it. This is exactly the lossiness the KITWARP brief
  cites for GM-based converters.
- **NO** — no tag in the 12-instrument model can name it at all.

**Score: 14 exact / 8 lossy / 162 inexpressible out of 184.**

#### Kit core (30 sounds)

| # | pivot sound id | named by | note range | source spellings | drum-remap can express? |
|---|---|---|---|---|---|
| 1 | `china.hit` | GM1/GM2/GS/XG | 52-52 | Chinese Cymbal | YES — `china/hit` |
| 2 | `crash.hit` | GM1/GM2/GS/XG | 28-57 | Brush Crash Cymbal, CM Crash Cymbal, Crash, Crash Cymbal 1, Crash Cymbal 2, Rama Cymbal | YES — `crash/hit` |
| 3 | `crash.hit.electronic` | GM2/GS/XG | 49-49 | 808 Cymbal, Analog Cymbal | LOSSY — collapses to `crash/hit` |
| 4 | `crash.reverse` | GM2/GS/XG | 28-52 | Reverse Cymbal, Reverse Cymbal 1, Reverse Cymbal 2 | NO |
| 5 | `hihat.closed` | GM1/GM2/GS/XG | 27-42 | Brush Closed Hi-hat, CM Closed High Hat, Closed Hi Hat 2, Closed Hi-Hat, Closed Hi-hat, Closed Hi-hat 1, Closed Hi-hat 2, Closed Hi-hat 3, Hi-Hat Closed | YES — `hihat/closed` |
| 6 | `hihat.closed.electronic` | GM2/GS/XG | 42-44 | 808 CHH, Analog CHH 1, Analog CHH 2, Analog HH Closed 1, Analog HH Closed 2, CR-78 CHH | LOSSY — collapses to `hihat/closed` |
| 7 | `hihat.open` | GM1/GM2/GS/XG | 29-46 | Brush Open Hi-hat, CM Open High Hat 1, CM Open High Hat 2, Hi-Hat Open, Open Hi Hat 2, Open Hi-Hat, Open Hi-Hat 3, Open Hi-hat, Open Hi-hat 2, Open Hi-hat 3 | YES — `hihat/open` |
| 8 | `hihat.open.electronic` | GM2/GS/XG | 46-46 | 808 OHH, Analog HH Open, Analog OHH, CR-78 OHH | LOSSY — collapses to `hihat/open` |
| 9 | `hihat.pedal` | GM1/GM2/GS/XG | 28-44 | Hi-Hat Pedal, Pedal Hi Hat, Pedal Hi-Hat, Pedal Hi-hat | YES — `hihat/pedal` |
| 10 | `hihat.reverse` | GS | 52-55 | Reverse CR-78 OHH, Reverse Closed Hi-hat, Reverse Open Hi-hat | NO |
| 11 | `kick.hit` | GM1/GM2/GS/XG | 33-67 | Acoustic Bass Drum, BD Gate, BD Jazz, BD Rock, BD Room, BD Soft, Bass Drum 1, Bass Drum H, Bass Drum H 2, Bass Drum H 3, Bass Drum H 4, Bass Drum L, Bass Drum M, Bass Drum M 2, ... | YES — `kick/hit` |
| 12 | `kick.hit.electronic` | GM2/GS/XG | 35-58 | 808 Bass Drum, 909 Bass Drum, Analog Bass Drum, BD Analog H, BD Analog L, Elec BD, Electric Bass Drum, Electric Kick, Electric Kick 1, Electric Kick 2 | LOSSY — collapses to `kick/hit` |
| 13 | `kick.hit.reverse` | GS | 36-39 | Reverse Concert BD 1, Reverse Electric Kick 1, Reverse Kick 1, Reverse Power Kick 1 | NO |
| 14 | `ride.bell` | GM1/GM2/GS/XG | 53-53 | Brush Ride Bell, Ride Bell, Ride Cymbal Cup | YES — `ride/bell` |
| 15 | `ride.bow` | GM1/GM2/GS/XG | 30-59 | Brush Ride Cymbal, CM Ride Cymbal, Ride Cymbal, Ride Cymbal 1, Ride Cymbal 2 | YES — `ride/bow` |
| 16 | `ride.reverse` | GS | 53-53 | Reverse Ride Cymbal | NO |
| 17 | `snare.brush-slap` | GM2/GS/XG | 27-88 | Brush Slap, Brush Slap 1, Brush Slap 2, Brush Slap 3, Brush Slap L | NO |
| 18 | `snare.brush-swirl` | GM2/GS/XG | 26-91 | Brush Long Swirl, Brush Swirl, Brush Swirl 1, Brush Swirl 2, Brush Swirl H, Brush Swirl L | NO |
| 19 | `snare.brush-tap` | GM2/GS/XG | 25-85 | Brush Tap, Brush Tap 1, Brush Tap 2 | NO |
| 20 | `snare.hit` | GM1/GM2/GS/XG | 30-77 | Acoustic Snare, CM Snare Drum, Concert SD, Concert Snare, Concert Snare Drum, Dance Snare 1, Dance Snare 2, Disco Snare, Elec SD, Electric Snare, House Snare, Jazz Snare 1, Jazz... | YES — `snare/hit` |
| 21 | `snare.hit.electronic` | GM2/GS/XG | 38-83 | 808 Snare 1, 808 Snare 2, 808 Snare Drum, 909 Snare 1, 909 Snare 2, Analog Snare 1, Analog Snare H, Analog Snare L, CM Electronic Snare Drum, Electric Snare 1, Electric Snare 2,... | LOSSY — collapses to `snare/hit` |
| 22 | `snare.hit.reverse` | GS | 40-45 | Reverse 808 Snare, Reverse Dance Snare, Reverse Snare 1, Reverse Snare 2, Reverse Standard Set 1 Snare 1, Reverse Tight Snare | NO |
| 23 | `snare.rimshot` | GM2/GS/XG | 34-40 | 808 Rim Shot, Analog Rim Shot, Open Rim Shot, Open Rim Shot 2, SD Rock Rim | YES — `snare/rimshot` |
| 24 | `snare.roll` | GS/XG | 25-29 | Snare Roll | NO |
| 25 | `snare.sidestick` | GM1/GM2/GS/XG | 31-43 | Analog Side Stick, CM Rim Shot, Side Stick, Sticks | YES — `snare/sidestick` |
| 26 | `snare.sidestick.reverse` | GS | 48-48 | Reverse Sticks | NO |
| 27 | `splash.hit` | GM1/GM2/GS/XG | 55-55 | Splash Cymbal | YES — `splash/hit` |
| 28 | `tom.hit` | GM1/GM2/GS/XG | 41-50 | Brush Hi Tom 1, Brush Hi Tom 2, Brush Low Tom 1, Brush Low Tom 2, Brush Mid Tom 1, Brush Mid Tom 2, Brush Tom 1, Brush Tom 2, Brush Tom 3, Brush Tom 4, Brush Tom 5, Brush Tom 6,... | YES — `tom/hit` |
| 29 | `tom.hit.electronic` | GM2/GS/XG | 41-50 | 808 Hi Tom 1, 808 Hi Tom 2, 808 Low Tom 1, 808 Low Tom 2, 808 Mid Tom 1, 808 Mid Tom 2, Analog Hi Tom 1, Analog Hi Tom 2, Analog Low Tom 1, Analog Low Tom 2, Analog Mid Tom 1, A... | LOSSY — collapses to `tom/hit` |
| 30 | `tom.hit.reverse` | GS | 46-47 | Reverse Tom 1, Reverse Tom 2 | NO |

#### Orchestral (4 sounds)

| # | pivot sound id | named by | note range | source spellings | drum-remap can express? |
|---|---|---|---|---|---|
| 1 | `applause` | GM2/GS | 58-88 | Applause, Applause 2 | NO |
| 2 | `concert-bass-drum.hit` | GM2/GS/XG | 32-49 | Concert BD, Concert BD 1, Concert BD 2, Gran Casa | LOSSY — collapses to `kick/hit` |
| 3 | `concert-cymbal.hit` | GM2/GS/XG | 31-59 | Concert Cymbal, Concert Cymbal 1, Concert Cymbal 2, Hand Cym.Closed H, Hand Cym.Closed L, Hand Cym.Open H, Hand Cym.Open L | LOSSY — collapses to `crash/hit` |
| 4 | `timpani.hit` | GM2/GS | 41-53 | Timpani A, Timpani A#, Timpani B, Timpani F, Timpani F#, Timpani G, Timpani G#, Timpani c, Timpani c#, Timpani d, Timpani d#, Timpani e, Timpani f | NO |

#### Hand/Latin/World (72 sounds)

| # | pivot sound id | named by | note range | source spellings | drum-remap can express? |
|---|---|---|---|---|---|
| 1 | `agogo-hi.hit` | GM1/GM2/GS/XG | 67-84 | Agogo H, CM High Agogo, High Agogo | NO |
| 2 | `agogo-lo.hit` | GM1/GM2/GS/XG | 68-85 | Agogo L, CM Low Agogo, Low Agogo | NO |
| 3 | `atarigane.hit` | GS | 39-39 | Atarigane | NO |
| 4 | `bangu.hit` | GS | 44-44 | Ban Gu | NO |
| 5 | `bell-tree.hit` | GM2/GS/XG | 34-84 | Bar Chimes, Bell Tree, Belltree | NO |
| 6 | `bell-tree.reverse` | GS | 57-57 | Reverse Bell Tree | NO |
| 7 | `bendir.hit` | GS | 54-54 | Bendir | NO |
| 8 | `bendir.reverse` | GS | 59-59 | Reverse Bendir | NO |
| 9 | `bongo-hi.hit` | GM1/GM2/GS/XG | 60-71 | Bongo H, CM High Bongo, Hi Bongo, High Bongo | NO |
| 10 | `bongo-lo.hit` | GM1/GM2/GS/XG | 61-72 | Bongo L, CM Low Bongo, Low Bongo | NO |
| 11 | `cabasa.hit` | GM1/GM2/GS/XG | 69-69 | CM Cabasa, Cabasa | NO |
| 12 | `cabasa.stroke` | GS | 95-96 | Cabasa Down, Cabasa Up | NO |
| 13 | `castanets.hit` | GM2/GS/XG | 27-85 | Castanet, Castanets | NO |
| 14 | `caxixi.hit` | GS | 64-64 | Caxixi | NO |
| 15 | `claves.hit` | GM1/GM2/GS/XG | 75-97 | 808 Claves, Analog Claves, CM Claves, Claves | NO |
| 16 | `conga-hi.mute` | GM1/GM2/GS/XG | 62-73 | 808 High Conga, Analog Conga H, CM Mute High Conga, Conga H Mute, Mute Hi Conga, Mute High Conga | NO |
| 17 | `conga-hi.open` | GM1/GM2/GS/XG | 63-74 | 808 Mid Conga, Analog Conga M, CM High Conga, Conga H Open, Open Hi Conga, Open High Conga | NO |
| 18 | `conga-lo.mute` | GS | 75-75 | Mute Low Conga | NO |
| 19 | `conga-lo.open` | GM1/GM2/GS/XG | 62-77 | 808 Low Conga, Analog Conga L, Analog High Conga, Analog Low Conga, Analog Mid Conga, CM Low Conga, Conga L, Low Conga, Open Low Conga | NO |
| 20 | `conga.slap` | GS | 76-76 | Conga Slap | NO |
| 21 | `conga.slide` | GS | 78-78 | Conga Slide | NO |
| 22 | `cowbell.hit` | GM1/GM2/GS/XG | 56-70 | 808 Cowbell, Analog Cowbell, CM Cowbell, Cowbell | YES — `cowbell/hit` |
| 23 | `cuica.mute` | GM1/GM2/GS/XG | 78-89 | Cuica Mute, Mute Cuica | NO |
| 24 | `cuica.open` | GM1/GM2/GS/XG | 79-90 | Cuica Open, Open Cuica | NO |
| 25 | `djembe.hit` | GS | 65-65 | Djembe | NO |
| 26 | `djembe.rim` | GS | 66-66 | Djembe Rim | NO |
| 27 | `finger-snap.hit` | GS/XG | 19-26 | Finger Snap | NO |
| 28 | `gong.bend` | GS | 47-47 | Bend Gong | NO |
| 29 | `gong.hit` | GS | 45-50 | Big Gong, Gamelan Gong, Small Gong, Thai Gong | NO |
| 30 | `gong.reverse` | GS | 56-56 | Reverse Gong | NO |
| 31 | `guiro.long` | GM1/GM2/GS/XG | 74-94 | Guiro Long, Long Guiro | NO |
| 32 | `guiro.reverse` | GS | 58-58 | Reverse Guiro | NO |
| 33 | `guiro.short` | GM1/GM2/GS/XG | 73-93 | Guiro Short, Short Guiro | NO |
| 34 | `handclap.hit` | GM1/GM2/GS/XG | 39-78 | CM Hand Clap, Hand Clap, Hand Clap2, Stereo Noise Clap | NO |
| 35 | `hyoushigi.hit` | GS | 40-40 | Hyoushigi | NO |
| 36 | `ice-block.hit` | GS | 71-71 | Ice Block | NO |
| 37 | `jingle-bell.hit` | GM2/GS/XG | 33-83 | Jingle Bell | NO |
| 38 | `kotsuzumi.hit` | GS | 42-43 | High Kotsuzumi, Low Kotsuzumi | NO |
| 39 | `maracas.hit` | GM1/GM2/GS/XG | 70-70 | 808 Maracas, Analog Maracas, CM Maracas, Maracas | NO |
| 40 | `metal-perc.hit` | GS | 76-76 | Metalic Percussion | NO |
| 41 | `ohkawa.hit` | GS | 41-41 | Ohkawa | NO |
| 42 | `pandeiro.mute` | GS | 79-79 | Mute Pandiero | NO |
| 43 | `pandeiro.open` | GS | 80-80 | Open Pandiero | NO |
| 44 | `pipe.hit` | GS | 70-70 | Pipe | NO |
| 45 | `req.dum` | GS | 55-55 | Req Dum | NO |
| 46 | `req.tik` | GS | 56-56 | Req Tik | NO |
| 47 | `shaker.hit` | GM2/GS/XG | 82-86 | Shaker | NO |
| 48 | `shime-daiko.hit` | GS | 38-38 | Shime Taiko | NO |
| 49 | `surdo.mute` | GM2/GS/XG | 13-86 | Mute Surdo, Surdo Mute | NO |
| 50 | `surdo.open` | GM2/GS/XG | 14-87 | Open Surdo, Surdo Open | NO |
| 51 | `swish.hit` | GS | 79-79 | Swish | NO |
| 52 | `tabla.stroke` | GS | 57-61 | Tabla Ge, Tabla Ge Hi, Tabla Na, Tabla Te, Tabla Tun | NO |
| 53 | `talking-drum.bend` | GS | 63-63 | Bend Talking Drum | NO |
| 54 | `talking-drum.hit` | GS | 62-62 | Talking Drum | NO |
| 55 | `tamborim.hit` | GS | 83-83 | Tamborim | NO |
| 56 | `tambourine.hit` | GM1/GM2/GS/XG | 26-72 | CM Tambourine, Digital Tambourine, Tambourine | NO |
| 57 | `timbale-hi.hit` | GM1/GM2/GS/XG | 65-69 | CM High Timbale, High Timbale, Timbale H, Timbales High | NO |
| 58 | `timbale-lo.hit` | GM1/GM2/GS/XG | 66-67 | CM Low Timbale, Low Timbale, Timbale L, Timbales Low | NO |
| 59 | `timbale.paila` | GS | 68-68 | Timbales Paila | NO |
| 60 | `triangle.mute` | GM1/GM2/GS/XG | 80-91 | Electric Mute Triangle, Mute Triangle, Triangle Mute | NO |
| 61 | `triangle.open` | GM1/GM2/GS/XG | 81-92 | Electric Open Triangle, Open Triangle, Triangle Open | NO |
| 62 | `udo.hit` | GS | 51-52 | Udo Long, Udo Short | NO |
| 63 | `udo.slap` | GS | 53-53 | Udo Slap | NO |
| 64 | `vibraslap.hit` | GM1/GM2/GS/XG | 58-73 | CM Vibrato Slap, Vibra-slap, Vibraslap | NO |
| 65 | `wadaiko.hit` | GS | 36-36 | Wadaiko | NO |
| 66 | `wadaiko.rim` | GS | 37-37 | Wadaiko Rim | NO |
| 67 | `whistle.long` | GM1/GM2/GS/XG | 72-88 | CM Long Whistle, Long Low Whistle, Long Whistle, Low Whistle, Samba Whistle L | NO |
| 68 | `whistle.short` | GM1/GM2/GS/XG | 71-87 | CM Short Whistle, High Whistle, Samba Whistle H, Short Hi Whistle, Short Whistle | NO |
| 69 | `wind-chime.hit` | GM2/GS/XG | 41-86 | Wind Chimes, Windchime, Windchimes | NO |
| 70 | `woodblock-hi.hit` | GM1/GM2/GS/XG | 76-98 | Hi Wood Block, High Wood Block, Wood Block H | NO |
| 71 | `woodblock-lo.hit` | GM1/GM2/GS/XG | 77-99 | Low Wood Block, Wood Block L | NO |
| 72 | `woody-slap.hit` | GS | 66-80 | Slappy, Woody Slap | NO |

#### Utility/click (16 sounds)

| # | pivot sound id | named by | note range | source spellings | drum-remap can express? |
|---|---|---|---|---|---|
| 1 | `click-noise.fx` | XG | 20-20 | Click Noise | NO |
| 2 | `high-q.fx` | GM2/GS/XG | 15-39 | Hi Q, High Q | NO |
| 3 | `high-q.reverse` | GS | 69-69 | Reverse High Q | NO |
| 4 | `key-click.fx` | GS | 63-63 | Key Click | NO |
| 5 | `metronome.bell` | GM2/GS/XG | 22-46 | Metronome Bell | NO |
| 6 | `metronome.click` | GM2/GS/XG | 21-45 | Metronome Click | NO |
| 7 | `scratch.fx` | GM2/GS/XG | 39-85 | Scratch, Scratch 2 | NO |
| 8 | `scratch.pull` | GM2/GS/XG | 18-79 | Scratch Pull, Scratch Pull 2 | NO |
| 9 | `scratch.push` | GM2/GS/XG | 17-78 | Scratch Push, Scratch Push 2 | NO |
| 10 | `scratch.reverse` | GS | 61-61 | Reverse Scratch | NO |
| 11 | `seq-click.fx` | XG | 23-24 | Seq Click H, Seq Click L | NO |
| 12 | `slap.fx` | GM2/GS | 28-40 | Slap | NO |
| 13 | `slap.reverse` | GS | 49-49 | Reverse Slap | NO |
| 14 | `spark.fx` | GS | 75-75 | Spark | NO |
| 15 | `square-click.fx` | GM2/GS | 32-44 | Square Click | NO |
| 16 | `whip-slap.fx` | XG | 16-16 | Whip Slap | NO |

#### SFX (62 sounds)

| # | pivot sound id | named by | note range | source spellings | drum-remap can express? |
|---|---|---|---|---|---|
| 1 | `sfx.alias` | GS | 73-73 | Alias | NO |
| 2 | `sfx.bass-slide` | GS/XG | 37-40 | Bass Slide | NO |
| 3 | `sfx.birds` | GM2/GS/XG | 78-102 | Bird 2, Birds | NO |
| 4 | `sfx.bubble` | GM2/GS/XG | 72-108 | Bubble | NO |
| 5 | `sfx.burst-noise` | XG | 60-60 | Burst Noise | NO |
| 6 | `sfx.car-crash` | GM2/GS | 66-90 | Car-Crash | NO |
| 7 | `sfx.car-engine` | GM2/GS/XG | 52-87 | Car-Engine, Engine Start | NO |
| 8 | `sfx.car-pass` | GM2/GS/XG | 54-89 | Car Passing, Car-Pass | NO |
| 9 | `sfx.car-stop` | GM2/GS | 64-88 | Car-Stop | NO |
| 10 | `sfx.cat` | GS/XG | 85-87 | Kitty | NO |
| 11 | `sfx.coaster` | XG | 61-61 | Coaster | NO |
| 12 | `sfx.dial-tone` | XG | 36-36 | Dial Tone | NO |
| 13 | `sfx.dog` | GM2/GS/XG | 76-100 | Dog | NO |
| 14 | `sfx.door` | GM2/GS | 60-84 | Door | NO |
| 15 | `sfx.door-creaking` | GM2/GS/XG | 37-83 | Creaking, Door Creaking | NO |
| 16 | `sfx.door-slam` | XG | 38-38 | Door Slam | NO |
| 17 | `sfx.explosion` | GM2/GS | 75-99 | Explosion | NO |
| 18 | `sfx.feedback` | XG | 73-73 | Feed | NO |
| 19 | `sfx.flute-key-click` | GM2/GS/XG | 51-52 | FL.Key Click, Fl.Key Click, Fl.Key click | NO |
| 20 | `sfx.flying-monster` | GS | 88-88 | Flying Monster | NO |
| 21 | `sfx.footsteps` | GM2/GS | 56-81 | Footsteps 1, Footsteps 2 | NO |
| 22 | `sfx.ghost` | XG | 90-90 | Ghost | NO |
| 23 | `sfx.growl` | GS/XG | 87-88 | Growl | NO |
| 24 | `sfx.guitar-cut-noise` | GM2/GS/XG | 33-49 | Cutting Noise 2 Down, Cutting Noise 2 Up, Dist. Cut Noise, Distortion Guitar Cutting Noise Down, Distortion Guitar Cutting Noise Up, Guitar Cutting Noise, Guitar Cutting Noise 2... | NO |
| 25 | `sfx.guitar-fret-noise` | GM2/GS | 47-47 | Guitar Fret Noise | NO |
| 26 | `sfx.gunshot` | GM2/GS | 72-96 | Gun Shot | NO |
| 27 | `sfx.gunshot.reverse` | GS | 60-60 | Reverse Gun Shot | NO |
| 28 | `sfx.haunted` | XG | 89-89 | Haunted | NO |
| 29 | `sfx.heartbeat` | GM2/GS | 55-79 | Heart Beat, Heartbeat | NO |
| 30 | `sfx.helicopter` | GM2/GS | 70-94 | Helicopter | NO |
| 31 | `sfx.horse-gallop` | GM2/GS/XG | 77-101 | Horse Gallop, Horse-Gallop | NO |
| 32 | `sfx.jetplane` | GM2/GS/XG | 58-93 | Jetplane | NO |
| 33 | `sfx.lasergun` | GM2/GS | 74-98 | Lasergun | NO |
| 34 | `sfx.lasergun.reverse` | GS | 62-62 | Reverse Laser | NO |
| 35 | `sfx.laughing` | GM2/GS | 52-76 | Laughing | NO |
| 36 | `sfx.machine-gun` | GM2/GS | 73-97 | Machine Gun | NO |
| 37 | `sfx.maou` | XG | 91-91 | Maou | NO |
| 38 | `sfx.missile` | GS | 86-86 | Missile | NO |
| 39 | `sfx.modulated-bell` | GS | 74-74 | Modulated Bell | NO |
| 40 | `sfx.pick-scrape` | GS/XG | 38-41 | Pick Scrape | NO |
| 41 | `sfx.pop-drop` | GS | 65-65 | Pop Drop | NO |
| 42 | `sfx.punch` | GM2/GS | 54-78 | Punch | NO |
| 43 | `sfx.rain` | GM2/GS/XG | 68-103 | Rain | NO |
| 44 | `sfx.scream` | GM2/GS | 53-77 | Scream, Screaming | NO |
| 45 | `sfx.seashore` | GM2/GS | 82-106 | Seashore, Waves | NO |
| 46 | `sfx.siren` | GM2/GS/XG | 56-91 | Siren | NO |
| 47 | `sfx.space-bird` | GS | 87-87 | Space Bird | NO |
| 48 | `sfx.starship` | GM2/GS/XG | 59-95 | Starship | NO |
| 49 | `sfx.stream` | GM2/GS/XG | 71-107 | Stream | NO |
| 50 | `sfx.string-slap` | GM2/GS/XG | 39-50 | String Slap, String Slap of Double Bass, String slap of double Bass | NO |
| 51 | `sfx.submarine` | XG | 62-62 | SbMarine | NO |
| 52 | `sfx.synth-drop` | GS | 68-68 | Syn.Drop | NO |
| 53 | `sfx.tape-stop` | GS | 84-85 | Tape Stop 1, Tape Stop 2 | NO |
| 54 | `sfx.tekno-trip` | GS | 64-64 | Tekno Trip | NO |
| 55 | `sfx.telephone-ring` | GS/XG | 42-90 | Telephone 1, Telephone 2, Telephone Ring2 | NO |
| 56 | `sfx.thunder` | GM2/GS/XG | 69-104 | Thunder | NO |
| 57 | `sfx.tire-screech` | XG | 53-53 | Tire Screech | NO |
| 58 | `sfx.train` | GM2/GS/XG | 57-92 | Train | NO |
| 59 | `sfx.velocity-noise` | GS | 77-77 | Velocity Noise FX | NO |
| 60 | `sfx.voice-hoo` | GS | 78-83 | High Hoo, Hoo, Low Hoo | NO |
| 61 | `sfx.voice-syllable` | GS | 81-82 | Voice Au, Voice Ou | NO |
| 62 | `sfx.wind` | GM2/GS/XG | 70-105 | Wind | NO |

---

## 4. Implications for the KITWARP pivot vocabulary

### 4.1 What this union proves about drum-remap's model

| Claim | Evidence |
|---|---|
| The 12-instrument enum covers **7.6 %** of the standards' vocabulary exactly | 14 of 184 sounds have an exact tag |
| It is **provably lossy** even on the sounds it can absorb | 8 sounds (electronic kick/snare/tom/CHH/OHH/crash, concert BD, concert cymbal) collapse onto acoustic tags; GM2's ANALOG and ELECTRONIC sets, XG's Analog/Electro kits and every GS TR-808/909/606/707/CR-78 set become indistinguishable from the Standard set after a round trip |
| **Three drum-remap instruments have no referent in any of the four standards** | `megabell`, `stack`, `xhat` appear nowhere in GM1/GM2/GS/XG. They are modern extended-kit concepts. Conversely all four standards name `Chinese Cymbal`, so `china` is well-founded |
| The two vocabularies are **near-disjoint outside the rock kit** | drum-remap: 40 pairs, all rock/metal kit. Standards: 184 sounds, of which only 30 are drum-kit core; the other 154 are hand/Latin/world percussion (72), SFX (62), utility clicks (16) and orchestral (4) |
| drum-remap's `role` axis has **no analogue** in any standard | GM/GS/XG name timbres, never musical function. `role` is a KITWARP invention — legitimate, but it cannot be derived from any standard's data and must be authored |

### 4.2 Axes the standards force into the pivot

1. **`instrument` must be an open registry, not a closed enum.** 184 sounds from four
   standards alone, plus ~1500 more name-families in the vendor extensions, including
   whole regional families (gamelan, Chinese opera percussion, Korean, Indian, Japanese,
   Middle-Eastern frame drums). A 12-value enum cannot be widened later without
   invalidating collected data — which is the stated reason this vocabulary must be fixed
   first. Model instruments as **stable IDs in a registry with a `family` grouping**
   (kit-core / hand-percussion / orchestral / utility / sfx / world-<region>).

2. **`pitch-instance` is a required, separate axis.** Every standard indexes multiple
   pieces of one instrument: toms 1–6 (XG `Rock Tom 1..6`, GS `Low Tom 2 / Low Tom 1 /
   Mid Tom 2 / Mid Tom 1 / High Tom 2 / High Tom 1`, GM1 `Low Floor / High Floor / Low /
   Low-Mid / High-Mid / High`), kicks 1–2, snares 1–2, bongo H/L, conga H/M/L, timbale
   H/L, agogo H/L, woodblock H/L, whistle short/long, muyu 5 sizes, paigu 3 sizes.
   drum-remap's optional `instance` is the right idea but is **ordinal-vs-named
   inconsistent**; the standards are uniformly ordinal-by-pitch (low→high). Adopt a
   signed/ordered `instance` with a documented low→high convention, and keep
   `hihat "shank"`-style striking positions **out** of it (a KITWARP weakness already
   identified — the standards agree with that critique: they put edge/inner/cup on the
   *ride*, which is a zone, not an instance).

3. **`zone` (striking position) is real and orthogonal.** GS names
   `Ride Cymbal Low/Mid/High Inner` vs `Low/Mid/High Edge` vs `Ride Bell`; XG names
   `Ride Cymbal Cup`; all four name `Open Rim Shot` vs `Side Stick` on the snare;
   GS names `Djembe` vs `Djembe Rim`, `Wadaiko` vs `Wadaiko Rim`, `Buk` vs `Buk Rim`.
   Zone values needed at minimum: `head/bow`, `rim`, `edge`, `bell/cup`, `shoulder`,
   `centre`. This is a **different axis** from articulation (a rim can be struck open or
   muted).

4. **Hi-hat openness must be ordinal with a defined scale.** GS SC-88Pro/SC-8850 name
   `Closed 1..4`, `Half-Open 1..2`, `Open 1..3`, `Pedal` — ten steps. drum-remap already
   mixes named (`tight`/`closed`/`open`) and ordinal (`open-0..3`) values; the standards
   say **pick ordinal and define the endpoints**, with named aliases mapping onto it.

5. **`timbre/kit-voicing` is an axis, not part of the sound name.** GM2 uses seven
   voicings of the *same* map (Standard/Room/Power/Electronic/Analog/Jazz/Brush); GS and
   XG do the same and go further by exposing *several kits' kick/snare simultaneously*
   (`Standard 1 Kick 1` at note 40 alongside `Room Kick 1` at 50 in SC-88's KICK & SNARE
   set; `Standard 1 / Room / Jazz / Brush Closed Hi-Hat` at 36–39 in SC-8850's
   `CYM&CLAPS 2`). Therefore: `kick` + `voicing=room` is a tag pair, and a target layout
   with four kick voicings must be addressable without inventing four instruments.

6. **`synthesis-source` must be distinguishable from `voicing`.** `Analog Bass Drum`,
   `TR-808 Snare 1`, `909 Bass Drum`, `CR-78 Closed Hi-Hat`, `Electric Snare 1` are not
   "a room-mic'd acoustic snare" — they are a different sound-generating object. If they
   share a tag with the acoustic sound, every GM2 ANALOG / GS TR-808 / XG Analog Kit
   source becomes unrecoverable. Suggested values: `acoustic`, `electronic`,
   `analog-machine` (+ optional `machine` provenance: 808/909/707/606/CR-78), `sampled-fx`.

7. **`modifier: reverse` is needed.** GM2 ELECTRONIC names `Reverse Cymbal` at note 52 —
   a *standard*, not an extension. GS carries 30+ `Reverse *` entries covering kick,
   snare, tom, all three hi-hat states, crash, ride, guiro, gong, scratch, high-Q, sticks.
   Reverse is a transform of another sound, so model it as a modifier on an existing tag,
   not as 30 new instruments.

8. **Pitched percussion needs a `pitch` field.** GM2/GS ORCHESTRA sets place a chromatic
   timpani run on notes 41–53 (`Timpani F` … `Timpani f`). XG-B adds pitched gamelan
   (`Bonang 1–5`, `Gender 1–5`, `Gamelan Gong 1–20`) and `Paigu High/Middle/Low`. A pivot
   with only `instrument/articulation` turns 13 timpani notes into one sound.

9. **A `category` axis is needed to make fallback safe.** 62 of the 184 sounds are sound
   effects (car, siren, dog, telephone, laughing…) and 16 are utility clicks
   (metronome, seq-click, square click, high-Q). Curated velocity-delta fallback chains
   are meaningless across these; a fallback from `sfx.helicopter` must be allowed to fail
   rather than resolve to `crash/hit`. Mark `category ∈ {percussion, utility, sfx}` and
   forbid cross-category fallback by default.

10. **Note-number identity is unusable as a key — confirming the pivot architecture.**
    Same sound, different note across the standards: `Bell Tree` = 84 (GM2/GS/XG) but 34
    in SC-88's ETHNIC set; `Castanets` = 85 (GM2/GS) but 39 in GM2 ORCHESTRA and 27 in
    SC-88; `High Q` = 27 (GM2/GS Standard) but 39 (GM2 SFX) and 15 (XG); `Scratch Push` =
    29, 41, 17 and 78 depending on standard and set. The `note range` column in §3 shows
    74 of the 184 sounds appearing on notes more than an octave apart. **Stable numeric
    IDs must be assigned to the *sound*, never derived from a note number** — this
    directly answers drum-remap's "no stable numeric IDs" weakness.

### 4.3 Distinctions that are real vs cosmetic

**Real (must be preserved by the pivot):**
- acoustic / electronic / analog-machine kick, snare, tom, hi-hat, crash (GM2 sets are built on it)
- `Side Stick` vs `Open Rim Shot` — every standard names both, on different notes
- Brush tap / brush slap / brush swirl — three distinct articulations, all in GM2 BRUSH, GS BRUSH, XG Brush Kit; XG splits swirl into `L`/`H`
- `Snare Roll` (GS, XG note 29) — distinct from a fast repeat; drum-remap has no roll
- Mute vs open on conga, cuica, triangle, surdo, pandeiro, cuíca, gong, Chinese gongs
- Ride bow vs bell/cup vs edge/inner (GS)
- Hi-hat closed vs half-open vs open vs pedal
- Concert/orchestral BD, SD, cymbals as *separate instruments* from kit BD/SD/crash — GM2 ORCHESTRA and GS/XG all name them separately and place them on notes that also carry kit sounds in other sets
- Pitched timpani

**Cosmetic (safe to normalise away, and this dossier already has):**
- Spelling and spacing: `Vibra-slap`/`Vibraslap`, `Belltree`/`Bell Tree`, `Closed Hi-hat`/`Closed Hi-Hat`/`Hi-Hat Closed`, `Fl.Key Click`/`FL.Key Click`/`Fl.Key click`, `Windchimes`/`Windchime`/`Wind Chimes`, `Heart Beat`/`Heartbeat`, `Scream`/`Screaming`, `Mute Hi Conga`/`Mute High Conga`/`Conga H Mute`
- Kit-name prefixes on an otherwise identical articulation: `Room Low Tom 2`, `Power Mid Tom 1`, `Jazz Kick 1`, `Standard 1 Snare 2`, `Brush Hi Tom 1` → `tom.hit` / `kick.hit` / `snare.hit` **plus** a `voicing` tag
- XG-B processing suffixes: `B`, `V`, `H`, `L`, `Q`, `Sk`, `HPF`, `BPF`, `Dark`, `Lo-Fi`, `#`
- Ordinal duplicates of the same piece: `Kick 1`/`Kick 2`, `Snare 1`/`Snare 2` → `instance`
- Roland's `[55]` / `[88]` / `[Pro]` compatibility-map prefixes in SC-8850 sets

### 4.4 Minimum-coverage assertion

Any KITWARP pivot must be able to name **all 184 sounds in §3** with a distinct tag, or it
cannot losslessly ingest a GM1, GM2, GS or XG source layout. The 72 hand/Latin/world plus 4
orchestral sounds and the 62 SFX sounds do not need *fallback chains* for drum-kit
remapping to work, but they do need **identity**, so that a GM/GS/XG note that carries them
survives a round trip instead of being silently folded into `crash/hit`.

---

## 5. Provenance and licensing

### 5.1 Per-fact provenance

| Fact set | Exact source | Licence / status |
|---|---|---|
| GM1 percussion key map, notes 35–81 (§2.1) | `https://github.com/jpcima/gm-xg-gs` → `instrument/GM1_GM2.ins`, section `[General MIDI Level 2 STANDARD Set]`, lines 315–372. File header credits *"GM1/GM2 Recommended Practice (RP024)"*, `(c)2008 kuzu / openmidiproject`, version 2008/7/26 | Repo has **no LICENSE file**. The `.ins` header carries only a no-warranty notice, no explicit grant. **Treat as unlicensed third-party transcription** — use as a research reference, do not vendor the file into KITWARP. The underlying note-name facts are the MMA RP-024 specification. |
| GM1 cross-check | `https://github.com/DigitalInBlue/ReaperNoteNames` → `generalmidi_drums.txt` | **CC0 1.0 Universal** (repo `LICENSE`) |
| GM2 extra notes 27–34 / 82–88, the nine sets and their per-set overrides (§2.2) | same `GM1_GM2.ins`, sections `[General MIDI Level 2 {ROOM,POWER,ELECTRONIC,ANALOG,JAZZ,BRUSH,ORCHESTRA,SFX} Set]`, lines 375–500 | as above |
| GM2 set selection (MSB 120 / LSB 0 / Program) | same file, `.Instrument Definitions` → `[General MIDI Level 2 Drumsets]`, `Key[120,n]=…` entries, lines 604–615 | as above |
| Roland GS SC-55 drum sets (§2.3) | `https://github.com/jpcima/gm-xg-gs` → `instrument/Roland_SC-8850.ins`, `.Note Names` block (file lines 4648–9375), sections `[Roland SC-55 * Set]`. Header: *"based on 'SC-8850 Users Manual' pp.167-245"* | as above; underlying facts are Roland's SC-8850 Owner's Manual |
| Roland GS SC-88 drum sets (§2.4) | same file, sections `[Roland SC-88 * Set]` | as above |
| SC-88Pro / SC-8850 extensions (§2.6) | same file, sections `[Roland SC-88Pro * Set]`, `[Roland SC-8850 * Set]` (incl. `CYMBAL&CLAPS`, `CYM&CLAPS 2`) | as above |
| Yamaha XG Level 1 kits (§2.5) | `https://github.com/pedrolcl/VMPK` → `data/gmgsxg.ins`, `.Note Names` block, sections `[XG * Kit]`, `[XG SFX 1]`, `[XG SFX 2]` | VMPK repo is **GPL-3.0** (`COPYING`). GPL is incompatible with vendoring into a proprietary plugin; use as reference only, or re-derive names from Yamaha's own XG spec. |
| Roland GS base nine sets (cross-check for §2.3) | same VMPK file, sections `[Roland GS * Set]` | GPL-3.0 |
| Yamaha XG-B / MU-series extensions (§2.6) | `https://github.com/jpcima/gm-xg-gs` → `instrument/YAMAHA_MU1000_MU2000.ins`. Header: *"based on 'MU1000/MU2000 List Book'"* | unlicensed transcription (as above) |
| midi.org pages | `https://midi.org/general-midi-2`, `https://midi.org/general-midi-level-1`, `https://midi.org/midi-ci-profile-for-default-drum-note-map` — all fetched, **none contain the tables**; PDFs gated behind MIDI Association membership. `https://midi.org/gm-level-1-sound-set` and `https://www.midi.org/specifications-old/item/gm-level-1-sound-set` return 404. | MMA specifications are copyright The MIDI Association; the note *names* are facts, the documents are not redistributable |

### 5.2 Licensing conclusion for KITWARP

The extracted note-name tables are **facts about published specifications**, not creative
works, and the sound names themselves (`Acoustic Bass Drum`, `Ride Bell`, `Cabasa`) are not
protectable. However:

- **Do not vendor** `GM1_GM2.ins`, `Roland_SC-8850.ins`, `YAMAHA_MU1000_MU2000.ins`
  (no licence grant) or `gmgsxg.ins` (GPL-3.0) into a proprietary plugin.
- **Do** re-key the vocabulary into KITWARP's own IDs and own canonical names (as §3 does),
  citing the specification (MMA RP-024, Roland SC-55/SC-88 Owner's Manuals, Yamaha XG
  Specification) as the authority. The GM1 names in particular are independently
  reproducible from the CC0 `ReaperNoteNames` file.
- If KITWARP wants a redistributable primary check, the **MMA GM1/GM2 specification PDFs**
  require a MIDI Association membership (free tier exists) — **UNVERIFIED** whether the
  free tier grants download; the pages only show "Join Us to Download".

### 5.3 Working data written

| Path | Contents |
|---|---|
| `…/scratchpad/research/data/drumsets.json` | 135 fully-resolved drum sets (`BasedOn` inheritance expanded), keyed by standard → set → note → name. 345 KB. The machine-readable form of §2. |
| `…/scratchpad/research/data/core_names.txt` | 588 raw distinct name strings across the four standards, each with the standards and note numbers that use it |
| `…/scratchpad/research/data/canon.json` | canonical sound id → list of raw name strings that normalise to it |
| `…/scratchpad/research/data/final_table.txt` | the 184-row union (§3) in TSV |
| `…/scratchpad/research/data/diffs.txt` | full per-set diff tables for SC-55, SC-88 and XG L1 |
| `…/scratchpad/research/data/ext_families.txt` | 1520 extension name-families beyond the core union (SC-88Pro, SC-8850, MU1000/MU2000) |
| `…/scratchpad/parse_ins.py`, `build.py`, `norm.py`, `final.py` | the parser and the auditable normalisation rule table (0 unmapped residuals) |

### 5.4 Explicitly UNVERIFIED

1. Exact spelling/spacing of every GM2, GS and XG name against the printed primary specs —
   all four `.ins` files warn *"the spelling or spacing may be different from those of the
   actual module"*. Sound identity is reliable; strings are not authoritative.
2. XG Level 1's official kit membership (11 kits) is taken from VMPK's file, not from the
   Yamaha XG Specification document.
3. GS drum-set Program Change numbers were **not** extracted (only the set names and maps);
   the `.ins` `.Instrument Definitions` block carries them but they were out of scope.
4. Whether `Applause` at GM2 note 88 is formally part of the ORCHESTRA set or an
   out-of-range extension in the transcription.
5. Whether the MIDI-CI "Default Drum Note Map" profile (midi.org) extends the GM vocabulary
   at all — the public page describes it only as standardising the existing GM mapping, and
   the specification itself is gated.
