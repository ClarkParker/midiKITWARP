# Dossier 01 — Existing open-source drum remappers: data models, pivots, and inversion loss

Task: extract the data model of every open-source drum remapper, count its pivot slots, determine
whether the pivot is General MIDI, and locate exactly where inversion loses information.
Target: KITWARP pivot vocabulary design.

Date: 2026-09-06. All facts below are from source files in repositories cloned at the commits listed
in §4. Nothing here is from memory or from a summarising fetch.

---

## 1. Scope and method

### 1.1 What was cloned (all via `git clone --depth 1`, all read with `cat`/`grep`/`python3`)

| Repo | Commit | Licence (verified from file) |
|---|---|---|
| `insomnimus/drum-mapper` | `677b07ada3cc4b9b496690615fa89d06b1175a01` | MIT (`LICENSE`, "MIT License Copyright (c) 2023 Taylan Gökkaya <insomnimus@pm.me>") |
| `Abstractize/drum-midi-remapper` | `19efaf2e35b6cb9bcabfd997cf12c4c9e674c4c9` | MIT (`LICENSE`, "Copyright (c) 2025 Gabriel Abarca Aguilar") |
| `markheath/midifilemapper` | `3a4d2a49a7a516be31a4e1611d548175568b042d` | **NO LICENCE FILE IN REPO.** Only `MidiFileMapper/Properties/AssemblyInfo.cs:13` → `AssemblyCopyright("Copyright © Mark Heath 2007-2017")`. Treat the map XML files as **unlicensed / all rights reserved** unless clarified. |
| `DigitalInBlue/ReaperNoteNames` | `5644e07f4c47ab63dab33a57b8821192fc6dfaf0` | **README claims CC BY 4.0; the `LICENSE` file is CC0 1.0 Universal.** See §2.4.1 — this is a real contradiction, not a mis-read. |
| `JPplayground/MidiNoteNameGen` | `793b3adfcf873e99e96c34b1c35dd005068dd816` | GPL-3.0 (`LICENSE.txt`) |
| `lotkey/Drum-MIDI-Converter` | `f585d2185cb68027238b8c80ee6886f5ff562eda` | GPL-3.0 (`LICENSE`) |

### 1.2 The "lotkey drum map / Drumforge" repo

The task named `lotkey/...` without a repo name. `mcp__github__search_repositories user:lotkey` +
`search_code "Drumforge drum map midi"` resolved it uniquely to **`lotkey/Drum-MIDI-Converter`**
(C++/Qt + Python Dash), which contains `src-cpp/mappings/Mapping/Mappings/Drumforge/Bergstrand.cpp`
and `.../Drumforge/Ultimate.cpp`. `lotkey/drum-maps`, `drummaps`, `drum_maps`, `DrumMaps` do not exist.

**This repo turned out to be the single most important source in this dossier** — it is the only
existing open-source converter that already uses a **non-GM, tree-structured pivot vocabulary with
an explicit fallback algorithm**. It is direct prior art for KITWARP and for `marty-615/drum-remap`.

### 1.3 What could not be obtained

- GitHub Issues for `insomnimus/drum-mapper`: `mcp__github__list_issues` is scoped to
  `clarkparker/midikitwarp` only in this session; `curl` to github.com is blocked (403).
  **The author's lossiness statement was found in the repo README instead** (§2.1.4), which is a
  primary source and is quoted verbatim with file+line.
- `midifilemapper` wiki (documentation lives at `https://github.com/markheath/midifilemapper/wiki`,
  not in the repo). The XML rule schema was reconstructed from source instead (§2.3.2), which is
  authoritative.
- `MidiNoteNameGen/download/preset-pack.zip` and `.exe` were not unpacked (binary, not needed —
  the `presets/` directory contains the same `.nka`/`.txt` pairs uncompressed).

---

## 2. Extracted facts, per project

---

### 2.1 `insomnimus/drum-mapper` — Rust VST3/CLAP + CLI

#### 2.1.1 Data model

There is **no vocabulary at all**. A "mapping" is a bare 128-entry `u8 → u8` table.

`mappings/src/lib.rs:9-13`:
```rust
pub struct Mapping {
    pub to_gm:   [u8; 128],
    pub from_gm: [u8; 128],
}
```

Storage format (`readme.md`, "Adding Custom Mappings"): one plain-text file per library in
`drums/`, filename stem = library name in the UI, one `gm_note -> library_note` line per mapping,
`#` comments and blank lines ignored, anything else is a hard parse error.
Parsed at **build time** by `mappings/build.rs`, which code-generates a `Library` enum and `static`
128-byte arrays into `OUT_DIR/libraries.rs`. Mappings are therefore compiled in; adding a library
requires rebuilding the plugin.

#### 2.1.2 Pivot

**Pivot = General MIDI note numbers. 128 nominal slots, of which only the 47 GM percussion sounds
(notes 35–81) are meaningful; the shipped files use 25 of them (35–59) plus a handful of
out-of-GM-range notes as scratch space.**

`mappings/src/lib.rs:29-32` — the entire conversion:
```rust
impl Mapping {
    pub fn to(&self, to: &Self, note: u8) -> u8 {
        to.from_gm[self.to_gm[note as usize] as usize]
    }
}
```
i.e. `source note → GM → target note`. There is no vocabulary, no articulation, no instance, no role.

#### 2.1.3 Where inversion loses information — exact mechanism

`mappings/build.rs` builds the inverse by **overwriting**:
```rust
let mut to_gm = Vec::from_iter(0_u8..=127);
for (gm, to) in &map {          // BTreeMap: ascending GM order
    to_gm[*to as usize] = *gm;  // last (= highest) GM wins
}
```
Because `map` is a `BTreeMap<u8,u8>` iterated in ascending key order, when several GM notes map to
one library note **the highest-numbered GM note silently wins** and all others become unreachable.

Measured over the 9 shipped `drums/*.txt` files (each a full 128-line table):

| Library | identity lines | remapped lines | distinct targets | colliding target notes |
|---|---|---|---|---|
| Addictive Drums 2 | 107 | 21 | 112 | 12 |
| Bogren Digital – Trivium Drums | 106 | 22 | 113 | 12 |
| EzDrummer 2 | 114 | 14 | 117 | 9 |
| EzDrummer 3 | 113 | 15 | 116 | 9 |
| GGD – OKW Architects | 105 | 23 | 113 | 10 |
| GGD – OKW Metal | 105 | 23 | 112 | 11 |
| SSD 5 | 113 | 15 | 117 | 9 |
| Superior Drummer 3 | 113 | 15 | 116 | 9 |
| Ugritone Drums | 116 | 12 | 120 | 7 |

Representative collisions (all verified by parsing the shipped files):

| Library | library note | GM notes collapsed onto it | inverse resurrects |
|---|---|---|---|
| all 9 | 0 | 0, 56 Cowbell, 58 Vibraslap | GM 58 |
| Superior Drummer 3 | 22 | 22, 42 Closed HH, 54 Tambourine | GM 54 |
| Superior Drummer 3 | 29 | 29, 51 Ride 1, 59 Ride 2 | GM 59 |
| EzDrummer 3 | 86 | 49 Crash 1, 52 China, 55 Splash, 86 | GM 86 |
| GGD – OKW Architects | 35 | 45 Low Tom, 47 Low-Mid, 48 Hi-Mid, 50 High Tom | GM 50 |
| Addictive Drums 2 | 60 | 51 Ride 1, 59 Ride 2, 60 Hi Bongo | GM 60 |
| Addictive Drums 2 | 65 | 41 Low Floor Tom, 43 High Floor Tom, 65 High Timbale | GM 65 |
| Ugritone Drums | 38 | 37 Side Stick, 38 Ac. Snare | GM 38 |
| Ugritone Drums | 42 | 42 Closed HH, 54 Tambourine | GM 54 |

**Concrete wrong conversions produced by the plugin** (computed by applying
`to.from_gm[self.to_gm[n]]` over the 9 libraries + GM, source note = each library's own note for
each GM percussion sound 35–59):

- `Addictive Drums 2` Closed Hi-Hat (note 52) → `Bogren Trivium` note 42 = **Tambourine**
- `Addictive Drums 2` Side Stick (note 42) → `Ugritone` note 38 = **Acoustic Snare**
- `Addictive Drums 2` Cowbell (note 47) → `Bogren Trivium` note 0 = **Vibraslap**
- `Bogren Trivium` Crash 1 (note 52) → `EzDrummer 2` note 55 = **Splash**
- `Bogren Trivium` Low Tom (note 35) → `GGD OKW Architects` note 35 = **High Tom**
- `EzDrummer 2` Ride 1 (note 51) → `EzDrummer 3` note 51 = **Ride 2**
- `EzDrummer 2` China (note 55) → `General MIDI` note 55 = **Splash**

Round-trip A→B→A failure rate over the 25 GM percussion sounds 35–59 (worst pairs):

| pair | broken of 25 |
|---|---|
| General MIDI → Addictive Drums 2 → back | 15 |
| EzDrummer 2 → Addictive Drums 2 → back | 14 |
| Ugritone → Addictive Drums 2 → back | 13 |
| SSD 5 / Superior Drummer 3 → Addictive Drums 2 → back | 12 |
| General MIDI → GGD OKW Architects → back | 11 |

#### 2.1.4 The author's own statement that GM-as-intermediate is lossy — VERBATIM

`drum-mapper/readme.md`, **line 95** (under the heading `## Issues` at line 94):

> Currently mappings other than General MIDI -> X are lossy; the plugin reverses the mapping while converting between libraries. This is going to be addressed in future versions. For now, it's wise to keep the original MIDI file around in case you want to swap libraries.

URL: `https://github.com/insomnimus/drum-mapper/blob/677b07ada3cc4b9b496690615fa89d06b1175a01/readme.md#L95`

#### 2.1.5 Other model gaps

- **CC / hi-hat pedal position is declared but never implemented.**
  `mappings/src/lib.rs:14-17` defines `pub struct LibraryMapping { pub notes: Mapping, pub ccs: Mapping }`,
  but `grep -rn "ccs" --include=*.rs .` returns **only that one line** — `build.rs` never emits a `ccs`
  table and `plugin/src/lib.rs` never reads one. The plugin remaps `NoteEvent::NoteOn` /
  `NoteEvent::NoteOff` only (`plugin/src/lib.rs:104,117`); everything else passes through unchanged.
  Hi-hat pedal CC (CC4 on most libraries) therefore reaches the target library **unremapped**.
- Libraries shipped: 9 `.txt` files (Addictive Drums 2, Bogren Digital – Trivium Drums, EzDrummer 2,
  EzDrummer 3, GGD – OKW Architects, GGD – OKW Metal, SSD 5, Superior Drummer 3, Ugritone Drums)
  plus a synthesised `General MIDI` identity mapping injected in `build.rs::main`.
  **The README's "Included Libraries" list is stale** — it omits Bogren Trivium and GGD OKW Metal.

---

### 2.2 `Abstractize/drum-midi-remapper` — .NET 8 CLI + MAUI GUI

#### 2.2.1 Data model

`src/Models/DrumMap.cs`:
```csharp
public class DrumMap {
    public string Name { get; set; } = string.Empty;
    public Dictionary<string, int> Mapping { get; set; } = new();
}
```
Storage: one JSON file per standard, embedded as an assembly resource
(`src/Services/Implementations/MapLoaderService.cs` → `$"Services.Resources.Maps.{type}.json"`).
`src/Models/DrumMapType.cs` enumerates the 4 available maps as a C# enum — **adding a map requires
editing the enum and recompiling** (the README's "Adding a New Mapping" section says so explicitly,
step 3).

#### 2.2.2 Pivot — **not GM note numbers; a named vocabulary of exactly 9 slots**

The pivot is the *string key* shared across all map files. `src/Services/Extensions/MidiFileExtensions.cs`:
```csharp
foreach (var kvp in sourceMap.Mapping) {
    if (targetMap.Mapping.TryGetValue(kvp.Key, out int targetNote))
        mapping[kvp.Value] = targetNote;   // sourceNote -> targetNote, keyed by NAME
}
```

**The complete pivot vocabulary is 9 terms**, identical in all four shipped files:
`Kick`, `Snare`, `HiHatClosed`, `HiHatOpen`, `TomLow`, `TomMid`, `TomHigh`, `Crash`, `Ride`.

Exhaustive dump of all four map files:

| key | GuitarPro | LogicPro | ProTools | StevenSlate |
|---|---|---|---|---|
| Kick | 35 | 36 | 36 | 36 |
| Snare | 40 | 38 | 40 | 38 |
| HiHatClosed | 42 | 42 | 42 | 42 |
| HiHatOpen | 46 | 46 | 46 | 46 |
| TomLow | 43 | 43 | 41 | 41 |
| TomMid | 47 | 47 | 45 | 45 |
| TomHigh | 50 | 50 | 48 | 48 |
| Crash | 49 | 57 | 49 | 49 |
| Ride | 51 | 59 | 51 | 51 |

#### 2.2.3 Where information is lost

1. **Vocabulary poverty.** 9 slots. No sidestick, no rimshot, no ride bell, no pedal hi-hat, no china,
   no splash, no choke, no more than three toms, no left/right instance, no percussion, no articulation
   axis whatsoever. Everything not in the 9 is unrepresentable.
2. **Unmatched notes pass through unchanged** — `RemapNotes` only rewrites notes present in the built
   dictionary; every other note is left alone. Combined with (3) this corrupts.
3. **Aliasing bug (verified by reading the code, not run):** GuitarPro→LogicPro builds
   `{35→36, 40→38, 43→43, 47→47, 50→50, 49→57, 51→59, 42→42, 46→46}`. A source note **36** (a real
   GM Bass Drum 1) is not a dictionary key, so it passes through as 36 and now collides with the
   remapped Kick. Same for source 38 colliding with the remapped Snare. Two distinct source sounds
   become one target note. The map is not injective on the full 0–127 domain, only on its 9 keys.
4. Notes are rewritten **in place on the `MidiFile` object** (`noteOn.NoteNumber = …`), NoteOn and
   NoteOff handled separately — no expansion (1→N) and no velocity/timing adjustment is possible.

---

### 2.3 `markheath/midifilemapper` — .NET WinForms + NAudio

#### 2.3.1 Pivot — **there is none. It stores direct N×N maps.**

Each XML file is a one-directional map between one specific pair. The `Maps/` directory contains 27
files, and the pairs are enumerated by hand:
`GM to EZdrummer`, `GM to AD`, `GM to Triaz`, `GM to GGD Invasion`, `GM to Latin Percussion EZX`,
`GM to 4x4 Bitwig`, `EZD to GM`, `EZD to AD`, `AD to EZD`, `DFH1 to DFH EZX`, `DFH EZX to GM`,
`Drum Lab to GM`, `Studio Drummer to GM`, `GGD Invasion to GM`, `GGD_Invasion-to-Metal_EZX`,
`Metal_EZX-to-GGD_Invasion`, plus non-mapping utilities (`Transpose2SemitonesUp`,
`Fixed Note Durations - 1 Tick`).
This is the combinatorial explosion KITWARP's pivot architecture exists to avoid: **16 real maps for
~10 libraries, and the pairs that exist are the ones somebody happened to need.**

#### 2.3.2 Mapping config format (reconstructed from source; authoritative)

Root element `MidiMappingRules` (`MidiMappingRules.cs:17`). Child elements, all optional and repeatable:

| Element | Attributes (source: `Rules/*.cs` `LoadFromXmlNode`) |
|---|---|
| `General` | free-form; every attribute is stored in a `Dictionary<string,string>`. Source comment (`MidiMappingRules.cs:20-26`) lists intended-but-unimplemented keys: `author`, `description`, `version`, `date`, `url`, `mode` (first-match / all-matches). In practice only `Name` is used. |
| `NoteMap` | `Name`, `InNote`, `InChannel`, `InVelocity`, `OutNote`, `OutChannel`, `OutVelocity`, `OutDuration` (`OutStartTime` is present but commented out) |
| `ControllerMap` | `Name`, `InController`, `InChannel`, `InValue`, `OutController`, `OutChannel`, `OutValue` |
| `AfterTouchMap` | `Name`, `Type` (`Channel`\|…), `InChannel`, `OutChannel`, `OutValue` |
| `PitchWheelMap` | `Name`, `InChannel`, `OutChannel`, `OutValue` (0–0x4000) |
| `TextMap` | `Name`, `EventType`, `InValue`, `OutValue`, `MatchType` (default `Regex`) |
| `Exclude` | `EventType` (default `All`), `Channel` |
| `Insert` | `EventType`, `Time`, `Value` |

**Input value syntax** (`InputValueParameters.cs`, `ValueRange.cs`): `*` = any; otherwise a
comma-or-semicolon separated list of items, each either `n` or `min-max`; spaces stripped.
Used heavily, e.g. `InNote="28,32,84-92,108-116"` in `DFH EZX to GM.xml`.

**Output value syntax** (`NoteEventOutputParameters.cs:35-63`): `*` = copy input;
`+n` / `-n` = offset (clamped to the field's min/max); `p%` = scale input by p percent then offset;
a bare integer = fixed value. Order of operations in `ProcessValue`: percent, then offset, then clamp.

**Rule application semantics** (`MidiMappingRules.Process`, lines ~176-215):
- NoteOff events are dropped and re-derived from their NoteOn.
- Note events run through `noteRules` in **document order, first match wins, then return**.
- **An unmatched note event is DELETED** (`// an unmatched note event / // TODO: configure to have an
  option to retain these / return false;`). This is why the shipped maps carry comments like
  `<!-- Filter out 54 - tambourine -->` and `<!-- Filter out all percussion sounds (60 upwards) -->`.
- Non-note events run through `excludeRules` first, then **all** `eventRules` accumulate.

It can also import **Cakewalk SONAR `.map`** (`CakewalkDrumMapping`: `NoteName`, `InNote`, `OutNote`,
`Channel`, `VelocityAdjust`, `VelocityScale`) and **Steinberg Cubase Drum Maps** (`INote`, `ONote`,
`Channel`, `Name`; the source's TODO comment names the unhandled Cubase fields: `Length`, `Mute`,
`DisplayNote`, `HeadSymbol`, `Voice`, `PortIndex`, `QuantizeIndex`). Relevant to KITWARP's storage
format work — these are the two DAW drum-map formats with real installed bases.

#### 2.3.3 Where inversion / GM-pivot loses information — the best worked example in any repo

`Maps/GGD Invasion to GM.xml` maps a **47-articulation** library onto **27 GM slots**. Nine of the 27
rules are many-to-one; they destroy **21 articulations** outright:

| GM out | GGD Invasion notes collapsed | articulations lost |
|---|---|---|
| 42 Closed Hi-Hat | 41, 42, 43, 44, 70 | HH Tip Tight, HH Edge Tight, HH Tip Closed, HH Edge Closed, X-Hats Closed → 1 |
| 46 Open Hi-Hat | 45, 46, 47, 71 | HH Open 1/2/3, X-Hats Open → 1 |
| 49 Crash Cymbal 1 | 52, 53, 56, 57 | Main Crash L Hit **and its Choke**, Wide Crash L Hit **and its Choke** → 1 |
| 57 Crash Cymbal 2 | 54, 55, 58, 59, 78 | Main Crash R Hit/Choke, Wide Crash R Hit/Choke, **Stack Hit** → 1 |
| 52 Chinese Cymbal | 65, 66, 67, 68 | China L Hit/Choke, China R Hit/Choke → 1 |
| 51 Ride Cymbal 1 | 62, 63 | Ride Hit, Ride Edge → 1 |
| 54 Tambourine | 73, 74 | Splash L Hit, Splash L Choke → 1 |
| 55 Splash Cymbal | 75, 76 | Splash R Hit, Splash R Choke → 1 |
| 40 Electric Snare | 29, 30 | Snare Off (wires-off), Snare Click → 1 |

Additionally, GM has no slot for several articulations at all, so the author **abused semantically
unrelated GM slots as scratch space** — this is the clearest possible demonstration that GM is too
small a pivot:

| GGD Invasion articulation | forced into GM slot | GM's actual meaning |
|---|---|---|
| Snare **Flam** (27) | 37 | Side Stick |
| Snare **Ruff** (28) | 39 | Hand Clap |
| **Bell L Hit** (79) | 56 | Cowbell |
| **Bell R Hit** (80) | 58 | Vibraslap |
| **Hats CC** (17) | 29 | *(not in the GM percussion key map at all)* |
| **ADK / auto double kick** (22) | 34 | *(not in the GM percussion key map at all)* |
| Splash L Hit/Choke (73, 74) | 54 | Tambourine |
| Stack Hit (78) | 57 | Crash Cymbal 2 |

Choke is silently *merged with* its own hit in every case: **GM cannot express choke at all.**

Two further defects in the same file: GGD note **63 (Ride Edge) is assigned twice** — to GM 51
*and* GM 59 — and since rules are first-match-wins, the second rule is dead. And the reverse file
`Maps/GM to GGD Invasion.xml` is *not* the inverse of the forward file (e.g. forward maps GGD 41/42/43/44/70
→ GM 42, reverse maps GM 42 → GGD **43** only), so a round trip through these two shipped maps is not
identity even in principle.

#### 2.3.4 Library note-layout vocabularies documented in the XML comments (primary data)

These comment blocks are the richest source of real library articulation naming in any repo studied.
Exhaustive:

**Addictive Drums 2** (`Maps/GM to AD.xml`, `Maps/AD to EZD.xml`, `Maps/EZD to AD.xml`), 43 named slots:
36 Kick · 37 Snare Rimshot L · 38 Snare Open Hit L · 39 Snare Rimshot R · 40 Snare Open Hit R ·
41 Snare Shallow Rimshot · 42 Snare Sidestick · 43 Snare Shallow Hit · 44 Snare Rim Click ·
45 Ride Pearl (Double) · 46 Cymbal 1 (Double) · 47 Cowbell · 48 HH Pedal Closed ·
49 HH Closed 1 Pearl · 50 HH Closed 1 Shaft · 51 HH Closed 2 Pearl · 52 HH Closed 2 Shaft ·
53 HH Closed Bell · 54 HH Open A · 55 HH Open B · 56 HH Open C · 57 HH Open D · 58 HH Open Bell ·
59 HH Pedal Open · 60 Ride Pearl · 61 Ride Bell · 62 Ride Shaft · 63 Ride Choke ·
65/67/69/71 Tom 4/3/2/1 Open Hit · 66/68/70/72 Tom 4/3/2/1 **Rimshot** · 75 Sticks ·
77/79/81 Cymbal 1/2/3 · 78/80/82 Cymbal 1/2/3 **Choke**.

**EZdrummer 2 standard kit** (`Maps/EZD to AD.xml`), 40 named slots including:
Hats Pedal chick (21) · Hats closed edge (22) · Hats foot splash (23) · Open Hats (24) ·
Open Hats 2 (25) · Open Hats 3 (26) · Crash A/B **alias** notes (27–32) · Snare Left (33) ·
Kick alias (34, 35) · Kick (36) · Side Stick (37) · Snare Right (38) · Snare Right alias (39) ·
Snare rimshot (40) · FT alias (41) · Floor Tom (43) · RT2 alias (45) · Rack Tom 2 (47) ·
RT1 alias (48) · Rack Tom 1 (50) · Ride bow (51) · Crash B (GM) (52) · Ride Bell (53) ·
Crash A muted (54) · Crash A sustained (55) · Cowbell (56) · Crash B sustained (57) ·
Crash B **muted** (58) · **Ride punch** (59) · Hats open max (60) · Hats closed tip (61) ·
Hats tight edge (62) · Hats tight tip (63) · **Hats seq hard** (64) · **Hats seq soft** (65).

**Metal! EZX** (`Maps/GGD_Invasion-to-Metal_EZX.xml`), 43 named slots, adds:
HH Closed Pedal (21) · HH Open Pedal (23) · China 1/2 Crashed · Cymbal 1–6 Crashed ·
Cymbal 2/5 **Muted** · **Spock Crashed** (29) · Splash Crashed · Snare alias · Kick alias ·
`Cymbal 2 alias`, `Cymbal 5 alias`, `Ride alias`.

**Latin Percussion EZX** (`Maps/GM to Latin Percussion EZX.xml`), **125 named slots, notes 3–127** —
the single largest enumerated percussion vocabulary in the corpus. Instruments: Maracas, Caxixi,
Cajon, Timbale Hi/Lo, Tambourine, Bongo Hi/Lo, Udu Hi/Lo, Shaker, Big Shaker, Wood Block 1–3,
Conga1/Conga2/Conga Hi/Lo, Guiro, Chimes, Crickets, Waterfall, Bells, Afuche, Shekere, Triangle,
Cymbal 1/2, Vibraslap, Cowbell, Splash. Articulation terms used: Open, Muted, Slap, Open Slap,
Closed Slap, Basstone / Bastone, Heel, Ghost, Flam, Ruff, Crescendo, Sidestroke, Rimshot,
Brush Hit, Brushed, Sidestick, Special, On Beat, Off Beat, Beat, Shake, Left / Right.

**GGD Invasion, NI Drum Lab, NI Studio Drummer, Triaz, 4x4 Bitwig** layouts are likewise documented in
their respective files.

---

### 2.4 `DigitalInBlue/ReaperNoteNames` — data-only note-name collection

#### 2.4.1 Licence — VERIFIED CONTRADICTION

- `README.md`: *"This project is licensed under the **Creative Commons Attribution 4.0 International
  (CC BY 4.0)** license."*
- `LICENSE` (121 lines): line 3 reads `CC0 1.0 Universal`; the body is the CC0 dedication text
  ("associating CC0 with a Work (the 'Affirmer')…"). `grep -n "CC BY\|Attribution 4.0" LICENSE`
  returns **nothing**.

So the task's premise ("reported CC BY 4.0") matches the README but **not** the file. The two
licences differ materially (CC0 waives the attribution requirement). **For KITWARP, treat this data
as CC BY 4.0 and attribute** — that is the stricter of the two claims and is safe under either.

#### 2.4.2 File format

`<manufacturer>_<instrument>.txt`, all lowercase, underscores for spaces (README, "File Naming
Convention"). Content: `#`-prefixed comments and blank lines, otherwise
`<midi note number><whitespace><name>` — one line per note, **no channel field, no CC lines, no
velocity field** anywhere in the repo (`grep` for `^CC`, for `\d+ \d+ ` → zero hits). Separator is
inconsistent: GGD files use a single space, the Korg files use a tab.
Consumed by REAPER via *File > Note/CC Names > Load Note/CC Names from File…*
(REAPER's own format additionally supports CC-name and per-channel lines — **UNVERIFIED**, no file
in this repo exercises it.)

#### 2.4.3 Coverage — exhaustive

43 files, **450 note-name lines total**. By vendor: orchestraltools 34, getgooddrums 4, korg 2,
generalmidi 1, solemntones 1, submissionaudio 1.

Drum/percussion-relevant files and their note counts:

| File | notes | subject |
|---|---|---|
| `korg_m1_i49.txt` | 61 | Korg M1 drum patch (header says "Patch I49") |
| `korg_m1_i29.txt` | 61 | Korg M1 drum patch — **header also says "Patch I49"** (see §2.4.5) |
| `getgooddrums_invasion.txt` | 47 | GGD Invasion |
| `generalmidi_drums.txt` | 47 | GM percussion key map (35–81) |
| `getgooddrums_architects.txt` | 32 | GGD OKW Architects |
| `getgooddrums_modernandmassive_halpern.txt` | 30 | GGD M&M Halpern |
| `getgooddrums_modernandmassive.txt` | 28 | GGD M&M |
| `orchestraltools_..._percussion_drums.txt` | 1 | (stub) |

Non-drum files are included in the repo but are irrelevant to the pivot except as evidence that the
format is instrument-agnostic (`solemntones_odiniii.txt` = 44 *guitar* articulations;
`submissionaudio_djinbass2.txt` = 31 *bass* articulations, both key-switch layouts).

#### 2.4.4 Exhaustive GGD vocabularies extracted (primary data for the pivot)

**GGD Invasion (47 notes)** — grouped exactly as the file groups them:
Kick: 22 Auto Double Kick, 23 Kick Left, 24 Kick Right.
Snare: 26 Hit, 27 Flam, 28 Ruff, 29 Snare Off, 30 (Cross Stick).
Toms: 33/34/35 Rack Tom 1/2/3, 36/37/38 Floor Tom 1/2/3.
Ride: 61 Bell, 62 Bow, 63 Rim.
Crashes: 52/53 Main Crash L Hit/Choke, 54/55 Main Crash R Hit/Choke,
56/57 Wide Crash L Hit/Choke, 58/59 Wide Crash R Hit/Choke.
Hats: 41 Tip Tight, 42 Edge Tight, 43 Tip Closed, 44 Edge Closed, 45/46/47 Open 1/2/3,
48 Pedal, **17 Hats CC**.
Splash: 73/74 Splash L Hit/Choke, 75/76 Splash R Hit/Choke.
China: 65/66 China L Hit/Choke, 67/68 China R Hit/Choke.
Stack: 78 Stack Hit. Bells: 79 Bell L Hit, 80 Bell R Hit. X-Hats: 70 Closed, 71 Open.

**GGD OKW Architects (32)** adds `Ride Crash` (63), `Ride Choke` (64), `Mini China Hit/Choke` (65/66),
and reuses note **78 for "X-HATS Hit"** where Invasion uses 78 for "Stack Hit".

**GGD Modern & Massive – Halpern (30)** adds hi-hat openness levels named `Open0`…`Open3`,
`Closed Loose`, `Tight`, `Ching`, `Pedal Chick`; and `Snare - Snare Off`, `Snare - Side Stick`,
`Snare - Ruff`, `Snare - Flam`; `Ride - Tip / Crash / Bell`.

#### 2.4.5 Provenance defects (relevant because KITWARP must record provenance)

- `generalmidi_drums.txt` header comment reads `# Getgood Drums - Modern and Massive - Halpern` —
  wrong; the content is the GM key map.
- `getgooddrums_modernandmassive.txt` header also reads `- Halpern` but its note layout differs
  from `getgooddrums_modernandmassive_halpern.txt`.
- `getgooddrums_architects.txt` header reads `One Kit Wonder: Modern Fusion - Invasion Preset`,
  filename says architects.
- `korg_m1_i29.txt` header says `Patch I49`.
- Duplicate names within one file: `getgooddrums_modernandmassive.txt` has `Floor Tom 1` on **both**
  43 and 45; `..._halpern.txt` has `Floor Tom 1` on **both** 35 and 37. The name is not a key.

---

### 2.5 `JPplayground/MidiNoteNameGen` — the GGD `.nka` converter

#### 2.5.1 What a GGD `.nka` preset actually contains

A `.nka` is a **Kontakt KSP script-array dump**, plain ASCII, LF-separated:

```
%ART__articulation_map      <- line 0: array name, literal, identical in every shipped preset
-1                          <- line 1: slot 0 (unused / mode)
23                          <- line 2: slot 1  -> articulation #1's assigned MIDI note
24                          <- line 3
...
-1                          <- unassigned slots
```

- **256 value lines** follow the header (measured: 257 total lines in the Invasion/Halpern/P4 presets,
  258 in the OKW ones — one trailing newline difference).
- **Index = articulation ordinal, fixed per library. Value = the MIDI note assigned to it.**
  There are **no names in the file** — the ordinal→name table lives only in the converter's source.
- Unassigned sentinel is **`-1`** in `InvasionDefault.nka`, `HalpernOriginalDefault.nka`,
  `P4HalpernDefault.nka`, `OKWArchitectsDefault.nka`, `OKWAggressiveRockDefault.nka`, but **`0`**
  in `OKWMetalDefault.nka`. The sentinel is not consistent across GGD exports.
- Produced in Kontakt by *settings page → "Export Map"* (README, "If you want to help").
- Because the file carries only ordinals, **a `.nka` is meaningless without knowing which library
  produced it** — the user must select the kit in the GUI (`main.py`, `self.checkbox_texts`).

Measured assignment counts in the shipped default presets:

| preset | articulations assigned | distinct notes |
|---|---|---|
| `HalpernOriginalDefault.nka` | 48 | 48 |
| `InvasionDefault.nka` | 47 | 47 |
| `P4HalpernDefault.nka` | 36 | 36 |
| `OKWArchitectsDefault.nka` | 32 | 32 |
| `OKWMetalDefault.nka` | 32 (of the 33 in-range slots) | 33 |
| `OKWAggressiveRockDefault.nka` | 24 | 24 |

#### 2.5.2 Articulation naming — exhaustive, per library (`src/ggd_data.py`)

Slot counts: **Invasion 47, Matt Halpern Signature Pack ("halpern_original") 49, P4 Matt Halpern 37,
OKW Metal 32, OKW Architects 32, OKW Aggressive Rock 24.**

`halpern_original_nka` — the richest vocabulary anywhere in this corpus (49 slots), verbatim:
```
Kick Main Hit · Stick Click Kick Hit · Snare Hit · Flam · Ruff · Snare-Off · Stick Click ·
Hi Tom Hit · Hi Tom Rim Hit · Mid Tom 1 Main Hit · Mid Tom 1 Rim Hit · Mid Tom 2 Main Hit ·
Mid Tom 2 Rim Hit · Floor Tom Main Hit · Floor Tom Rim Hit · Pedal Chik · Pedal Ching ·
Tip Tight · Edge Tight · Tip Closed · Edge Closed · Tip Loose · Edge Loose ·
Tip Open 1 · Edge Open 1 · Tip Open 2 · Edge Open 2 · Tip Open 3 · Edge Open 3 ·
Tip Wide · Edge Wide · Hi Hat CC ·
Left Crash Hit · Left Crash Bell · Left Crash Choke · Left Crash Swell ·
Right Crash Hit · Right Crash Bell · Right Crash Choke · Right Crash Swell ·
Ride Tip · Ride Crash · Ride Bell Tip · Ride Bell Shoulder ·
China Main Hit · China Choke · Stack Tight Hit · Stack Loose Hit · Splash Hit
```
Note the **full 2 × 7 cross-product** of striking position (Tip / Edge) × openness
(Tight, Closed, Loose, Open 1, Open 2, Open 3, Wide) = 14 hi-hat articulations, plus 2 pedal
articulations and a CC — 17 hi-hat slots in one library. GM has three.

`invasion_nka` adds `Wires Off`, `Xhat Closed`, `Xhat Open`, `Bell L Hit`, `Bell R Ht`,
`Stack Hit`, and ride `Bell` / `Edge` / `Rim`.
`p4_nka` adds `Pedal Chink`, `Mini Hats Hit`.
`architects_nka` adds `Ride Crash`, `Ride Choke`, `Mini China Hit/Choke`, `X-hat Hit`.

**The dictionaries are typo-ridden and are the shipped identifiers:** `Ruft` (Ruff), `Peal` (Pedal),
`Eye Closed` (Edge Closed), `Bell R: Ht` (Bell R Hit), `Ede Closed:` (Edge Closed),
`China L Choke ` (trailing space), `Splash Lefts Hit`, `Tom 1: Hit` (colon). They appear verbatim
in the emitted note-name files. Naming here is *not* a controlled vocabulary.

#### 2.5.3 What the converter emits

A **REAPER MIDI note-name file** — exactly 128 lines, `<note> <name>`, unassigned notes written as
`<note> ~` (`src/logic.py`, final loop). Verified against `presets/Default/InvasionDefault.txt`
(47 named lines + 81 `~` lines = 128).

Note-number transform (`ggd_data.py::convert_kontakt_note_to_reaper_note`): Kontakt's `C-2 = 0`
convention → REAPER's `C-1 = 0`, implemented as a round trip through **note-name strings**. It is
intended to be a numeric identity and is one for notes 0–113, but:

- `KONTAKT_NOTES` has only **126 entries**, so an articulation assigned to note **126 or 127 crashes
  the converter** (`IndexError`, swallowed by `main.py`'s bare `except Exception` → "Something went wrong").
- For notes **114–125 the transform is off by one** (e.g. 114 → `'G7'` → `'G8'` → **115**), because
  the table drops `F#8` ("Kontakt skips F#8 for some reason", source comment) without compensating.

There is **no remapping between libraries** in this tool at all — it is a documentation generator.
It contributes vocabulary, not a pivot.

---

### 2.6 `lotkey/Drum-MIDI-Converter` — the only non-GM pivot in the corpus

#### 2.6.1 Data model — a hierarchical "SampleTree" of pivot keys

The pivot is defined as **six independent root trees** in plain text
(`src-cpp/mappings/tree/{cymbal,hat,kick,perc,snare,tom}.txt`), indentation = nesting,
a leading `*` marks a node as a **default** for fallback. README rules, verbatim:

> - Each root has it's own text file. These roots are completely separate, there is no crossover, and the kit pieces under one root cannot replace or substitute kit pieces under any other root.
> - Defaults have an \*asterisk\* in the beginning of the name

`update --keys` code-generates `src-cpp/mappings/SampleTree/Keys.hpp` (330 lines) from the tree.
Each leaf becomes a flat string id formed by joining the path with `_` (double `_` before the
ordinal): e.g. `cymbal_hit_ride_bow_tip__1`, `hat_hit_closed_edge_tight__1`, `snare_alt_side_stick`.

**Pivot size: 170 distinct keys.** By root: cymbal 71, hat 50, tom 24, snare 12, perc 10, kick 3.
Full enumeration is in §2.6.2. **150 of the 170 are actually used** by at least one of the 37 shipped
library mappings.

A library mapping is `pivot key → MidiNoteGroup` (a *set* of notes), so **one pivot key can own
several aliased MIDI notes** in a library. Example `Mappings/Drumforge/Bergstrand.cpp`:
```cpp
{Cymbal::Bell::Crash::_1,        {{Note::A, 3}, {Note::D, 4}}},   // two aliases
{Cymbal::Hit::Ride::Bow::Tip::_1,{{Note::G, 3}, {Note::C, 4}}},
{Kick::_1,                       {{Note::C, 1}}},
{Kick::left,                     {{Note::C_SHARP, 1}}},
```
Note numbering is Yamaha/Kontakt style: `Mappings::yamahatoi(note, octave) = 12*(octave+2) + note`,
so `Note::C, 1` = 36.

#### 2.6.2 The full 170-key pivot vocabulary (exhaustive)

```
kick (3)      kick__1 · kick_adk · kick_left

snare (12)    snare_hit__1 · snare_hit_electric · snare_hit_flam · snare_hit_off ·
              snare_hit_roll · snare_hit_ruff ·
              snare_alt_side__1 · snare_alt_side_stick ·
              snare_alt_rim__1 · snare_alt_rim_click ·
              snare_alt_rim_shot__1 · snare_alt_rim_shot_edge1

tom (24)      tom_hit_{rack,floor}__{1,2,3,4}  (8)
              tom_rim_{rack,floor}__{1,2,3,4}  (8)
              tom_rim_shot_{rack,floor}__{1,2,3,4} (8)

hat (50)      hat_hit_closed__0
              hat_hit_closed_{tip,edge,shank}__1        + _{tip,edge,shank}_tight__1
              hat_hit_closed_{bell,foot,x,tight,loose}__1
              hat_hit_open__{0,1,2,3,4,5}
              hat_hit_open_{tip,edge,bell}__{0,1,2,3,4,5}   (18)
              hat_hit_open_shank__{0,1,2}
              hat_hit_open_{tip,edge,bell,shank}_loose__1
              hat_hit_open_{ching,loose,x}__1
              hat_hit_open_pedal_splash__1
              hat_midi_cc · hat_midi_seq · hat_midi_trigger

cymbal (71)   cymbal_hit_crash__{1..6} · cymbal_hit_crash_bow__{1..6} ·
              cymbal_hit_crash_bow_tip__{1..6}
              cymbal_bell_crash__{1..6} · cymbal_bell_crash_tip__{1..6}
              cymbal_choke_crash__{1..6}
              cymbal_hit_ride__{1,2} · cymbal_hit_ride_bow__{1,2} ·
              cymbal_hit_ride_bow_tip__{1,2} · cymbal_hit_ride_edge__{1,2}
              cymbal_bell_ride__{1,2} · cymbal_bell_ride_tip__{1,2} · cymbal_choke_ride__{1,2}
              cymbal_hit_china__{1,2} · cymbal_hit_china_bow__1 · cymbal_hit_china_bow_tip__1 ·
              cymbal_bell_china__1 · cymbal_bell_china_tip__1 · cymbal_choke_china__{1,2}
              cymbal_hit_splash__{1,2,3} · cymbal_hit_splash_tip__1 · cymbal_choke_splash__{1,2,3}
              cymbal_hit_stack__{1,2,3} · cymbal_choke_stack__{1,2,3}

perc (10)     perc_clap · perc_shaker · perc_sticks · perc_vibraslap ·
              perc_cowbell_{hit,tip,shank} · perc_tambourine_{hit,up,down}
```

#### 2.6.3 The fallback algorithm (`SampleTree::findNearestFit`)

```cpp
// exact hit?
mapKey = keyFromPath(path);
if (mapping.containsKey(mapKey)) return mapping[mapKey];
exclude = path.back(); path.pop_back();
while (path.size() > 0) {
    std::vector<std::string> defaults = at(path).getDefaultKeys(exclude);
    std::shuffle(defaults.begin(), defaults.end(), rd);   // <-- RANDOM
    for (const auto &key : defaults) {
        path.push_back(key);
        if (mapping.containsKey(keyFromPath(path))) return mapping[keyFromPath(path)];
        path.pop_back();
    }
    exclude = path.back(); path.pop_back();
}
return {};   // give up: the note is dropped
```
Semantics: exact key → else walk one level up the tree, try that node's `*`-marked default children
(excluding the branch we came from) → repeat upward → give up and **drop the note**.

**Defect: `std::shuffle` makes fallback non-deterministic.** When more than one default sibling
matches, the result differs run to run. Since `update --cmaps` bakes the result into
`src-python/conversions.lkcmap`, the shipped Python web-app tables are one random draw.

#### 2.6.4 Where information is lost here

1. **Alias collapse.** `MidiNoteGroup::operator int()` returns `*m_notes.begin()`, i.e. the *lowest*
   note of the target group. `ConversionMap::insert(group, value)` inserts every source alias → the
   one target value. N source aliases → 1 target note; the distinction is unrecoverable.
2. **Drop on no-fit.** `makeConversionMapping` only inserts a pair when `findNearestFit` returned a
   value; otherwise the source note has **no entry** and is passed through / lost.
3. **Duplicate keys in a mapping.** `Mappings/Drumforge/Bergstrand.cpp` assigns
   `Hat::Hit::Closed::Tip::Tight::_1` **twice** (G#2 at line ~34 and A#2 at line ~40). One wins.
4. **Runtime is still N×N.** `src-python/conversions.lkcmap` (3954 lines ≈ 1318 direction pairs, i.e.
   37×37 minus self) is a precomputed dump of every ordered library pair as raw byte-pair tables.
   The tree is a *build-time* pivot only.
5. **No velocity, no timing, no CC, no 1→N expansion.** `ConversionMap` is `map<uint8_t,uint8_t>`.
   `hat_midi_cc` exists as a pivot key but resolves to a note, not to a controller.

#### 2.6.5 GM's poverty measured against this project's own pivot

`Mappings/GeneralMIDI/GmStandard.cpp` uses **22 of the 170 pivot keys** (12.9 %):
`kick__1`, `snare_hit__1`, `snare_alt_side_stick`, `tom_hit_rack__{1,2,3,4}`,
`tom_hit_floor__{1,2}`, `hat_hit_closed__0`, `hat_hit_closed_foot__1`, `hat_hit_open__1`,
`cymbal_hit_crash__{1,2}`, `cymbal_hit_ride__{1,2}`, `cymbal_bell_ride__1`, `cymbal_hit_china__1`,
`cymbal_hit_splash__1`, `perc_cowbell_hit`, `perc_tambourine_hit`, `perc_vibraslap`.

Compare `Toontrack/SuperiorDrummer3.cpp` (**80** pivot keys), `StevenSlateDrums/SSD.cpp` (61),
`Fxpansion/Bfd3.cpp` (58), `GGD Invasion` (47), `XLNAudio/AddictiveDrums2.cpp` (48).
**Any conversion routed through GM discards ≥ 58 of Superior Drummer 3's 80 distinctions.**

37 library mappings ship: Drumforge Bergstrand + Ultimate; EastWest ProDrummer; FXpansion BFD3;
General MIDI Standard; GetGoodDrums (Groove Player MIDI Pack, Invasion ×2, Modern&Massive ×3,
Matt Halpern ×3, OKW AggressiveRock/Architects/ClassicRock ×4/Metal/ModernFusion); GuitarPro;
Logic Pro Drummer (**empty — 0 keys**); Manda Audio MT Power Drum Kit 2; Mixwave Gojira / Thomas
Pridgen; Naughty Seal Perfect Drums; Prenc Kinglake; Singular Sound BeatBuddy; Solemn Tones Mjolnir;
SSD + SSD5; Toontrack EZDrummer / EZD Progressive Foundry / Superior Drummer 3; XLN Addictive Drums 2.

---

## 3. Implications for the KITWARP pivot vocabulary

### 3.1 Pivot-size summary

| Project | Pivot | Distinct pivot slots | GM-based? |
|---|---|---|---|
| `insomnimus/drum-mapper` | GM note numbers | 128 nominal / 47 GM percussion / **25 used** | **Yes** |
| `Abstractize/drum-midi-remapper` | named string keys | **9** | No, but degenerate |
| `markheath/midifilemapper` | **none** — direct N×N XML rule files | n/a (16 hand-written pairs) | GM used as a hub by convention |
| `DigitalInBlue/ReaperNoteNames` | **none** — documentation only | n/a (450 note-name lines) | No |
| `JPplayground/MidiNoteNameGen` | per-library ordinal slots, no cross-library pivot | 24–49 per library | No |
| `lotkey/Drum-MIDI-Converter` | **hierarchical tree, `*`-default fallback** | **170** | **No** |
| `marty-615/drum-remap` (reference) | flat instrument/articulation tags | 40 pairs / 12 instruments | No |

**Conclusion: 170 tree keys (lotkey) is the largest existing non-GM pivot and the number to beat.
40 tags (drum-remap) is not enough — it is smaller than a single library's own vocabulary
(GGD Halpern Signature Pack alone has 49; Superior Drummer 3 needs 80 in lotkey's model).**

### 3.2 Concrete list of articulations GM cannot express

Every entry below is attested by at least one primary source in §2. GM 35–81 has no slot for any of them.

**Damping / sustain state**
- `choke` on crash / china / splash / stack / ride — GGD Invasion has 8 dedicated choke notes;
  `GM to AD.xml` shows AD has 78/80/82 Cymbal 1/2/3 Choke; GM has none. GM's Crash 1 and Crash 2
  are *instances*, not hit-vs-choke.
- `muted` distinct from `choke` — EZdrummer 2 "Crash A muted" (54) vs "Crash A sustained" (55);
  Metal! EZX "Cymbal 2 Muted" (50) vs "Cymbal 2 Crashed" (49).
- `swell` — GGD Halpern Signature `Left Crash Swell`, `Right Crash Swell`.

**Striking position (the single largest gap)**
- hi-hat `tip` vs `edge` vs `shank` — GGD every library; AD calls the same axis `Pearl` vs `Shaft`;
  EZD calls it `tip` vs `edge`. Three vendor synonym sets for one axis.
- hi-hat `bell` (closed and open) — AD 53 `HH Closed Bell`, 58 `HH Open Bell`.
- ride `bow` vs `edge` vs `tip` vs `rim` vs `crash` — GGD Invasion 62/63, GGD Architects 63 `Ride Crash`,
  AD 60 `Ride Pearl` / 62 `Ride Shaft`, EZD 59 `Ride punch`.
- ride bell sub-position: `Ride Bell Tip` vs `Ride Bell Shoulder` (GGD Halpern Signature).
- crash `bell` — GGD Halpern Signature `Left Crash Bell` / `Right Crash Bell`; lotkey
  `cymbal_bell_crash__{1..6}`.
- cowbell `tip` vs `shank` (lotkey `perc_cowbell_tip` / `_shank`).

**Hi-hat openness — ordinal, not binary**
- GM has exactly three: Closed (42), Pedal (44), Open (46).
- GGD Invasion needs 8 + CC. GGD M&M Halpern needs `Tight, Closed, Closed Loose, Open0, Open1,
  Open2, Open3` = 7 levels. GGD Halpern Signature needs `Tight, Closed, Loose, Open1, Open2, Open3,
  Wide` × `Tip|Edge` = 14, plus `Pedal Chik` and `Pedal Ching`. AD needs `Open A/B/C/D` + `Open Bell`.
  lotkey models `hat_hit_open__{0..5}` × `{tip,edge,bell}`.
- `foot splash` / `pedal open` — EZD 23 `Hats foot splash`, AD 59 `HH Pedal Open`,
  lotkey `hat_hit_open_pedal_splash__1`. GM's 44 Pedal Hi-Hat is a *chick*, not a splash.
- `ching` — GGD M&M `Hat - Ching`, GGD Halpern `Pedal Ching`, lotkey `hat_hit_open_ching__1`.

**Snare**
- `rimshot` (GM's 40 "Electric Snare" is repeatedly abused for it — `GM to EZdrummer.xml`
  comment: *"we will allow electric snare through to play a rim shot"*).
- `rim click` distinct from `sidestick` — AD has **both**: 42 Snare Sidestick and 44 Snare Rim Click.
  GM has one slot (37).
- `wires off` / `snare-off` — GGD every library. GM has none.
- `flam`, `ruff`, `roll` — GGD Invasion 27/28, GGD Halpern; forced into GM 37 Side Stick and
  GM 39 Hand Clap by `GGD Invasion to GM.xml`.
- `shallow hit` / `shallow rimshot` — AD 41/43.
- `stick click` — GGD Halpern Signature (a distinct slot from sidestick).
- snare `left` / `right` — EZD 33 Snare Left, 38 Snare Right; AD 37/38/39/40 Rimshot L/R and
  Open Hit L/R. GM cannot express hand.

**Toms**
- **tom rimshot / rim** — AD 66/68/70/72 `Tom 1–4 Rimshot`; GGD Halpern Signature
  `Hi Tom Rim Hit`, `Mid Tom 1/2 Rim Hit`, `Floor Tom Rim Hit`; lotkey has 16 `tom_rim*` keys.
  GM: zero. **`marty-615/drum-remap` also has zero — this is a gap in the reference taxonomy too.**
- more than 6 toms and the rack/floor distinction: GGD Invasion has 3 rack + 3 floor;
  lotkey models `rack 1–4` + `floor 1–4`. GM's six tom slots (41,43,45,47,48,50) are ordered by pitch
  and carry no rack/floor semantics.

**Kick**
- `left` / `right` (double pedal) — GGD Invasion 23/24, EZD Metal! 35/36. GM's 35/36 are two
  *different bass drum sounds*, not two feet.
- `auto double kick` / `ADK` — GGD Invasion 22. Forced into GM 34 (outside the GM key map) by
  `GGD Invasion to GM.xml`. lotkey has `kick_adk`.

**Extra cymbals with no GM slot**
- `stack` (GGD Invasion 78, GGD Halpern `Stack Tight Hit` / `Stack Loose Hit`, lotkey 6 stack keys).
- `x-hat` / auxiliary closed hats (GGD Invasion 70/71, GGD Architects 78, lotkey `hat_hit_*_x__1`).
- `mini china` (GGD Architects 65/66), `mini hats` (GGD P4 Halpern).
- `bell` / megabell (GGD Invasion 79/80 `Bell L/R Hit` — forced into GM 56 Cowbell and GM 58 Vibraslap).
- more than 2 crashes: GGD Invasion has 4 (Main L/R, Wide L/R); lotkey models crash 1–6,
  splash 1–3, stack 1–3, china 1–2, ride 1–2. GM has Crash 1, Crash 2, Splash, China, Ride 1, Ride 2.

**Sequencer / controller articulations**
- `hi-hat CC` as a first-class kit piece — GGD note **17** ("Hats CC") in Invasion, Architects,
  Metal, Aggressive Rock, P4, Halpern Signature; lotkey `hat_midi_cc`, `hat_midi_seq`,
  `hat_midi_trigger`; EZD `Hats seq hard` (64) / `Hats seq soft` (65).
  **GM has no controller axis at all**, and `drum-mapper` proves the practical consequence: its
  `ccs` field is dead code, so pedal CC passes through unremapped.
- `alias` notes — EZD explicitly labels `Kick alias`, `Snare Right alias`, `RT1 alias`, `FT alias`,
  `Crash A alias` ×3, `Crash B alias` ×3, `Cymbal 2 alias`, `Cymbal 5 alias`, `Ride alias`.
  A pivot term can legitimately own several notes in one library; GM's flat 1:1 cannot say so.

**Percussion beyond the rock kit** (`GM to Latin Percussion EZX.xml`, 125 slots)
- GM has *one* slot per Latin instrument; the EZX has 6–17 articulations each:
  conga `Open / Muted / Open Slap / Closed Slap / Heel / Basstone / Flam / Crescendo / Special`
  × `Left / Right`; timbale `Open / Rimshot / Sidestroke / Flam / Ruff` × `Hi / Lo` × `L / R`;
  cajon `Slap / Slap Mid / Ghost / Basstone / Sidestick / Brush Hit / Brushed / Flam / Crescendo`
  × `L / R`; udu, caxixi, shekere, afuche, big shaker, crickets, waterfall, chimes, bells —
  **none of which exist in GM at all.**

### 3.3 Which axes KITWARP needs (evidence-driven)

1. **`instrument`** — must extend `drum-remap`'s 12. Missing, attested: `adk` (or a kick `pedal`
   modifier), `mini-china`, `mini-hihat`, `bell` (crash/kit bell — distinct from cowbell), `sticks`,
   `clap`, `shaker`, `tambourine`, `vibraslap`, and the whole Latin family
   (conga, bongo, timbale, cajon, udu, caxixi, shekere, afuche, guiro, agogo, claves, woodblock,
   cuica, triangle, maracas, cabasa, whistle, chimes).
2. **`articulation`** — must be **factored**, not a flat enum. `drum-remap`'s
   `hihat/open-close-tip` already mixes three orthogonal facts. lotkey's tree and the GGD Halpern
   2×7 grid both show the axes are independent:
   - `position`: tip / edge / shank / bell / bow / rim / shoulder (+ vendor synonyms pearl→tip, shaft→shank)
   - `openness`: an **ordinal** 0…5 with a canonical name per level (tight, closed, closed-loose,
     open-1…open-3, wide) — never mix named and ordinal in one enum, which is `drum-remap`'s
     stated weakness and is confirmed here as a real cross-vendor problem.
   - `damping`: open / muted / choke / swell — **three distinct values, not a boolean**.
   - `technique`: hit / flam / ruff / roll / crescendo / ghost / brush.
   - `state`: wires-on / wires-off (snare only).
3. **`instance`** — must carry *both* an ordinal and a spatial label, because sources use both and
   they are not interchangeable. Attested spatial labels: `left`, `right`, `center`,
   `main` vs `wide` (GGD's crash rows), `rack 1–4`, `floor 1–4`, `A/B/C/D` (AD hi-hat).
   lotkey's `__1..__6` ordinals lose the L/R/main/wide information that GGD's own names carry.
4. **`controller`** — REQUIRED as a first-class axis, not an afterthought. Evidence: GGD ships
   "Hats CC" as note 17 in six libraries; lotkey has `hat_midi_cc/seq/trigger`; EZD has
   `Hats seq hard/soft`; and `drum-mapper` demonstrates the failure mode of omitting it.
   Needs at minimum: hi-hat pedal position (CC), and the note-vs-CC duality (some libraries expose
   pedal position as a *note*, some as a CC).
5. **`role`** — `drum-remap`'s 7-value role enum is **unattested anywhere in this corpus.** No
   converter studied records role. It is a KITWARP/drum-remap invention; keep it, but it is
   orthogonal to everything measured here and cannot be populated from any existing data set.
6. **`alias` cardinality** — a pivot term must be able to own **a set** of library notes
   (lotkey's `MidiNoteGroup`; EZD's explicit "alias" notes). One canonical note plus N aliases,
   with a rule for which one to emit. lotkey emits `*begin()` (lowest); that choice should be
   explicit, not incidental.
7. **`provenance`** — mandatory. §2.4.5 and §2.5.2 document six wrong headers, three duplicate
   names, and a set of typo'd identifiers shipped as data. Every KITWARP row needs source,
   version, and a confidence marker.
8. **Stable numeric IDs** — lotkey's keys are path-derived strings; reorganising the tree
   invalidates every mapping (the README says so: *"If you reorganized the tree or removed some kit
   pieces, the other mappings will not compile."*). KITWARP must decouple id from path.

### 3.4 Real vs cosmetic distinctions

**Real (keep as separate pivot terms):**
- hit vs choke vs muted vs swell (four distinct samples in AD, EZD, GGD).
- tip vs edge vs shank on hi-hat and ride (separate samples in AD, EZD, GGD, lotkey).
- rimshot vs rim-click vs sidestick (AD ships all three: 37/39/41, 44, 42).
- tom rim vs tom hit (AD, GGD Halpern).
- wires-off vs hit (GGD, every library).
- flam vs ruff vs single hit (GGD, Latin EZX).
- kick left vs right vs ADK (GGD Invasion, EZD Metal!).
- crash main vs wide, left vs right (GGD Invasion has 4 distinct crash *pieces*).
- stack vs china vs mini-china (GGD Architects has both china and mini china).
- x-hat vs main hi-hat (GGD Invasion has separate 70/71).

**Cosmetic (should be synonyms of one pivot term, not separate terms):**
- `Pearl` (AD) = `tip` (GGD/EZD/lotkey) = bead of the stick.
- `Shaft` (AD) = `shank` (lotkey) = `punch` in EZD's `Ride punch`.
- `Cross Stick` (GGD) = `Side Stick` (GM/EZD/AD) = `snare_alt_side_stick` (lotkey).
- `Snare Off` (ReaperNoteNames) = `Wires Off` (MidiNoteNameGen) = `Snare-Off` (GGD Halpern)
  = `snare_hit_off` (lotkey).
- `Pedal Chick` / `Pedal Chik` / `Hats Pedal chick` / `HH Pedal Closed` — one thing.
- `Crashed` (EZD suffix on every cymbal name) is not an articulation; it is EZD's word for "hit".
- `Ride Crash` (GGD) vs `crash on the ride edge` — one thing; do not create a `megabell`-style
  instrument for it (`drum-remap`'s `megabell` is a *piece*, which is correct; `ride/crash` is an
  articulation, which is also correct — but they must not be conflated).
- Ordinal vs named openness (`Open 1/2/3` vs `Open A/B/C/D` vs `Open0..3`) — same axis,
  different vendor labelling. Normalise to one ordinal scale with named anchors.

### 3.5 Architectural lessons

- **Every project that used GM as pivot is provably lossy, and two of the three authors say so in
  their own repos** (`drum-mapper` readme line 95; `midifilemapper`'s map comments
  *"Filter out 54 - tambourine"*, *"we will allow hand clap through to play a snare rim click"*).
- **Every project that avoided GM built a tree or a name table** — and the one that built a tree
  (lotkey, 170 keys) is the only one able to represent Superior Drummer 3's 80 distinctions.
- **A pivot alone is not enough: a fallback policy is required and must be deterministic.**
  lotkey's `*`-default + walk-up-the-tree is the right shape; `std::shuffle` inside it is the wrong
  implementation. `drum-remap`'s curated fallback chains with `velocityDelta` are strictly better.
- **1→N expansion is needed and no existing project has it.** `drum-remap`'s `expand` rules
  (open-close hi-hat = open + pedal-close 1/32 later; splash = crash + choke 1/8 later) have no
  counterpart in any converter studied — lotkey, drum-mapper and drum-midi-remapper are all strictly
  1→1. The `Hit`/`Choke` note pairs shipped by GGD/AD/EZD are exactly the data that makes such
  expansion possible, and are exactly what GM destroys.

---

## 4. Provenance

Every fact above traces to one of the following. All repositories were cloned into
`scratch:repos/`.

| Fact group | Source path / URL | Licence |
|---|---|---|
| drum-mapper model, build-time inversion, README quote (line 95) | `drum-mapper/{readme.md,mappings/src/lib.rs,mappings/build.rs,plugin/src/lib.rs}` · https://github.com/insomnimus/drum-mapper @ `677b07a` | MIT |
| drum-mapper collision & round-trip tables | computed by parsing `drum-mapper/drums/*.txt` (9 files × 128 lines) with the exact `to_gm` construction from `build.rs` | MIT |
| 9-slot named pivot, 4 map files | `drum-midi-remapper/src/{Models/DrumMap.cs,Models/DrumMapType.cs,Services/Resources/Maps/*.json,Services/Extensions/MidiFileExtensions.cs}` · https://github.com/Abstractize/drum-midi-remapper @ `19efaf2` | MIT |
| XML rule schema, value syntax, first-match/drop semantics | `midifilemapper/MidiFileMapper/{MidiMappingRules.cs,Rules/*.cs,InputValueParameters.cs,ValueRange.cs,NoteEventOutputParameters.cs}` · https://github.com/markheath/midifilemapper @ `3a4d2a4` | **no licence file**; `AssemblyInfo.cs:13` "© Mark Heath 2007-2017" |
| GGD Invasion → GM 47→27 collapse; AD / EZD / Metal! EZX / Latin EZX layouts | `midifilemapper/MidiFileMapper/Maps/{GGD Invasion to GM.xml,GM to GGD Invasion.xml,GM to AD.xml,AD to EZD.xml,EZD to AD.xml,GGD_Invasion-to-Metal_EZX.xml,GM to Latin Percussion EZX.xml,DFH EZX to GM.xml,Drum Lab to GM.xml,Studio Drummer to GM.xml,GM to Triaz.xml,GM to 4x4 Bitwig.xml,GM to EZdrummer.xml}` | same as above |
| Reaper note-name format, licence contradiction, GGD vocabularies, provenance defects | `ReaperNoteNames/{README.md,LICENSE,getgooddrums_*.txt,generalmidi_drums.txt,korg_m1_*.txt}` · https://github.com/DigitalInBlue/ReaperNoteNames @ `5644e07` | README says CC BY 4.0; `LICENSE` file is CC0 1.0 |
| `.nka` structure, 6 GGD articulation tables, converter output, off-by-one bug | `MidiNoteNameGen/src/{ggd_data.py,logic.py,main.py}`, `MidiNoteNameGen/presets/{Default,Custom}/*.{nka,txt}` · https://github.com/JPplayground/MidiNoteNameGen @ `793b3ad` | GPL-3.0 |
| 170-key tree pivot, `findNearestFit`, alias collapse, 37 library mappings, GM=22/170 | `Drum-MIDI-Converter/src-cpp/mappings/{tree/*.txt,SampleTree/{Keys.hpp,SampleTree.cpp,SampleTree.hpp},Mapping/{Mapping.hpp,Mappings.cpp,ConversionMap.cpp},Midi/MidiNoteGroup.cpp,Mapping/Mappings/**/*.cpp}`, `src-python/{conversions.lkcmap,conversionmap.py}`, `README.md` · https://github.com/lotkey/Drum-MIDI-Converter @ `f585d21` | GPL-3.0 |

**Licence caution for KITWARP:** `lotkey/Drum-MIDI-Converter` and `JPplayground/MidiNoteNameGen` are
**GPL-3.0**. Their *note-layout facts* (which MIDI note a library assigns to which articulation) are
factual data and not copyrightable expression, but their *source files and key naming* are.
Re-derive layouts from vendor manuals rather than copying these files into a non-GPL codebase.
`midifilemapper` has **no licence at all** — its XML maps must not be copied.

### UNVERIFIED

- REAPER's note-name file format supporting CC-name lines and per-channel note names. No file in
  `ReaperNoteNames` exercises it; not checked against REAPER documentation.
- Whether `insomnimus` has restated the lossiness point in a GitHub issue (issues were unreachable
  from this session; the README statement is a primary source and suffices).
- The exact vendor-side names for AD2's "Pearl"/"Shaft" — these come from `midifilemapper`'s
  hand-written XML comments, not from an XLN Audio manual.
- `Drumforge` article vocabulary beyond what `Bergstrand.cpp` and `Ultimate.cpp` encode (34 and 22
  pivot keys respectively); no Drumforge manual was consulted.
