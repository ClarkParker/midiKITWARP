# 08 — Export target formats: what each container can actually carry

Goal: establish, per export target, the exact set of fields that must be filled, so the
KITWARP pivot data model can be checked for **lossless export**. Every grammar below is
derived from real files that were cloned and parsed, not from prose descriptions, except
where explicitly marked UNVERIFIED.

---

## 1. Scope and method

### 1.1 Corpora obtained

| Corpus | How | Size actually parsed |
|---|---|---|
| `jim/cubase_drum_maps_for_toontrack` | `git clone` | 19 Cubase `.drm` (EZX/EZD/SDX/SD2) |
| `janminor/cubase` | `git clone` | 8 Cubase `.drm` |
| `thebruce/drumCartographer` | `git clone` | 1 Cubase `.drm` + 5 JSON emitter templates |
| `markheath/midifilemapper`, `midifilemapper` | already cloned | 2 Cubase `.drm` (older schema variant) |
| `MuseScore/MuseScore` | already cloned | 6 `.drm` — **different format**, same extension (see §2.1.6) |
| `DigitalInBlue/ReaperNoteNames` | `git clone` | 39 Reaper note-name `.txt` |
| `tsunetakaryu/MIDINoteNames-for-REAPER` | `git clone` | 1 236 note-name lines |
| `knpwrs/reaper-midi-note-names`, `shadowflower64/yarg-reaper-template`, `HarleyGaniere/Reaper-Track-Builder` | `git clone` | further Reaper `.txt` incl. the only CC-name file found |
| `ReaTeam/Doc` → `State Chunk Definitions` | `git clone` | authoritative `<MIDINOTENAMES>` RPP grammar |
| `Ultraschall/ultraschall-lua-api-for-reaper` (sparse) | `git clone` | ReaScript API doc for `SetTrackMIDINoteNameEx` |
| `darobyn/instrumentdefinitions` | already cloned | 20 Cakewalk `.ins`, incl. 310 792 lines of `cakewalkmodified/*` |
| `chad-ramos/studio-one-drum-maps`, `WaltRitscher/studio-one-user-presets`, `tephrocactus/studio-one` | `git clone` | **164** `.pitchlist` (17 720 `Music.PitchName` elements) + **46** `.keyswitch` |
| `jaredthirsk/cubase-expression-maps` | `git clone` | **76** `.expressionmap` (3 968 `PSoundSlot` objects, 13 460 `POutputEvent`) |
| `mhcoffin/fiddle` → `example-expression-maps/` | already cloned | **11** Dorico `.doricolib` (22 `ExpressionMapDefinition`, 496 `playingTechniqueCombination`) |
| `nobodo/logic-pro-x-articulation-sets`, `simonlehmann/…-bbc-symphony-orchestra` | `git clone` | **49** Logic articulation-set `.plist` (659 articulations) |
| `chrisself/switchboard` | `git clone` | Go generator + `plist.tmpl` — independent confirmation of the Logic schema |
| `MinMax25/QBDrumMap` | `git clone` | C# writer for `.drm` **and** `.pitchlist`; documents Cubase 12+ entity fields |
| `Ardour/ardour` `share/patchfiles` (sparse) | `git clone` | **471** MMA `.midnam` files (31 626 `<Note>` elements) |
| `data/legacy-iom/*.iom` (this repo) | local | 11 `.iom` |

### 1.2 Not obtainable

| Target | Why |
|---|---|
| Studio One **Sound Variation** internals beyond `.keyswitch` | PreSonus support pages return 403/500 to the fetcher; the on-disk format for the newer Sound Variation editor (symbols, groups, non-note switching) is not in any public repository found. `.keyswitch` *is* obtained and is the on-disk form of the older/simple case. Marked UNVERIFIED where extrapolated. |
| Cubase `HeadSymbol` integer → symbol name table | Not in any file, tool or doc found. Steinberg docs state only that head symbols are arranged in **pairs** (empty head / filled head). Values observed in the wild: `0,1,2,3,10,14`. |
| Cubase 12+ `instruments.xml` / `playingTechniqueDefinitions.xml` entity ID lists | Ship inside the Cubase installation (`Components/ScoringEngine/`), not redistributable. The *reference mechanism* is fully established from `QBDrumMap` source. |
| Logic **mapped instrument** as a file | It is an Environment object inside the project; Apple provides no standalone file format. Confirmed by Apple's own docs listing only in-window editing. |
| Pro Tools proprietary instrument definition | None exists; Pro Tools uses MMA `.midnam` (§2.5). |

---

## 2. Note-name / drum-map export targets

### 2.1 Cubase Drum Map — `.drm`

#### 2.1.1 Container

Plain UTF-8 XML, `<?xml version="1.0" encoding="utf-8"?>`, root `<DrumMap>`. Steinberg's
generic typed-value serialisation: every value is an element `<int|float|string
name="Field" value="…"/>`, containers are `<list name="…" type="list">` of `<item>`.
Strings that may hold non-ASCII carry `wide="true"`.

**A drum map is always exactly 128 slots — one per MIDI note number.** Verified: all 34
valid `.drm` files carry exactly 128 `<item>` in `Map` and exactly 128 `<item value>` in
`Order`. (Steinberg's own doc: "settings for 128 drum sounds, one for each MIDI note
number".)

#### 2.1.2 Top-level structure

```
<DrumMap>
  <string name="Name"           .../>   map display name
  <list   name="Quantize"       ...>    1 item (observed) — quantize presets
  <list   name="Map"            ...>    128 items — the drum sounds
  <list   name="Order"          ...>    128 <item value="pitch"/> — row display order
  <list   name="OutputDevices"  ...>    n items — {DeviceName, PortName}
  <int    name="Flags" value="0"/>      present only in newer files
</DrumMap>
```

#### 2.1.3 Verbatim excerpt — real file

`jim_cubase_drum_maps_for_toontrack/drum_maps/SDX Metal Foundry.drm`, slots 34–38:

```xml
    <item>
      <int name="INote" value="34"/>
      <int name="ONote" value="34"/>
      <int name="Channel" value="9"/>
      <float name="Length" value="200"/>
      <int name="Mute" value="0"/>
      <int name="DisplayNote" value="34"/>
      <int name="HeadSymbol" value="0"/>
      <int name="Voice" value="0"/>
      <int name="PortIndex" value="0"/>
      <string name="Name" value="[Kick 1] Right" wide="true"/>
      <int name="QuantizeIndex" value="0"/>
    </item>
    <item>
      <int name="INote" value="37"/>
      <int name="ONote" value="37"/>
      <int name="Channel" value="9"/>
      <float name="Length" value="200"/>
      <int name="Mute" value="0"/>
      <int name="DisplayNote" value="37"/>
      <int name="HeadSymbol" value="0"/>
      <int name="Voice" value="0"/>
      <int name="PortIndex" value="0"/>
      <string name="Name" value="[Snare] Sidestick" wide="true"/>
      <int name="QuantizeIndex" value="0"/>
    </item>
```

A slot that *does* use the notation fields —
`thebruce_drumCartographer/examples/ezd2-drummap-example.drm`:

```xml
      <item>
         <int name="INote" value="42"/>
         <int name="ONote" value="42"/>
         <int name="Channel" value="9"/>
         <float name="Length" value="200"/>
         <int name="Mute" value="0"/>
         <int name="DisplayNote" value="76"/>
         <int name="HeadSymbol" value="3"/>
         <int name="Voice" value="0"/>
         <int name="PortIndex" value="0"/>
         <string name="Name" value="Closed Hi-Hat" wide="true"/>
         <int name="QuantizeIndex" value="0"/>
      </item>
```

Header and trailer, verbatim:

```xml
<?xml version="1.0" encoding="utf-8"?>
<DrumMap>
  <string name="Name" value="EZX Jazz" wide="true"/>
  <list name="Quantize" type="list">
     <item>
        <int name="Grid" value="4"/>
        <int name="Type" value="0"/>
        <float name="Swing" value="0"/>
        <int name="Unquantized" value="0"/>
        <int name="Legato" value="50"/>
     </item>
  </list>
  <list name="Map" type="list">
  …128 items…
  </list>
  <list name="Order" type="list">
    <item value="0"/> … <item value="127"/>
  </list>
  <list name="OutputDevices" type="list">
     <item>
        <string name="DeviceName" value="Default Device"/>
        <string name="PortName" value="Default Port"/>
     </item>
  </list>
</DrumMap>
```

Cubase 12+ variant (`janminor_cubase/drummaps/EZD Singer Songwriter.drm`) adds three
fields per slot and `<int name="Flags" value="0"/>` at the end:

```xml
         <int name="QuantizeIndex" value="0"/>
         <int name="NoteheadSet" value="0"/>
         <string name="InstrumentEntityID" value=""/>
         <string name="TechniqueEntityID" value=""/>
```

Older variant (`markheath_midifilemapper/MappingTests/TestFiles/EZD Map.drm`) has no XML
declaration, no `wide="true"`, and a different `Quantize` item:

```xml
      <item>
         <int name="Grid" value="4"/>
         <int name="Type" value="0"/>
         <float name="Swing" value="0"/>
         <float name="MaxDiff" value="0"/>
         <int name="Tuplet" value="1"/>
         <int name="Move CC" value="0"/>
      </item>
```

#### 2.1.4 FIELD TABLE — `.drm` `Map` item

Domains measured over 4 352 slots (34 files).

| Field | Type | Observed domain | Semantics | What the pivot must store to fill it losslessly |
|---|---|---|---|---|
| `INote` | int | 0–127, always == slot index | **Input** note: what the user plays / what arrives | The **target layout's** note number for this pivot symbol. In the drum-map idiom the slot index doubles as the row's *Pitch*. |
| `ONote` | int | 0–127 | **Output** note actually sent to the instrument | Same note number as `INote` for a plain naming map; for a *remapping* map, the note number in the destination layout. So: pivot symbol → (source note, target note). |
| `Channel` | int | `9` (3 920), `0` (304), `-1` (128) | MIDI channel, `-1` = "use track channel" | A per-entry **output channel**, nullable. Needed for multi-channel modules (Roland VAD hi-hat on a second channel, TD-50 aux). |
| `Length` | float | `200` in **all** 4 352 slots | Default length of an inserted note, in Cubase ticks (480 PPQN ⇒ 200 ticks ≈ 5/12 quarter) | **Export-only decoration.** Store as an optional per-entry default; emit `200` when unset. |
| `Mute` | int | `0` (4 302), `1` (50) | Row muted in the drum editor | Optional per-entry boolean. Real files use it (Addictive Drums map mutes unused rows). |
| `DisplayNote` | int | 0–127 | Staff position in the Score editor | **Notation decoration.** Equivalent to Studio One `scorePitch`. Must be derivable from the pivot symbol via a notation table. |
| `HeadSymbol` | int | `0`(4335) `14`(6) `3`(5) `2`(4) `10`(1) `1`(1) | Index into Cubase's fixed notehead-**pair** palette | **Notation decoration.** Enum mapping to symbol names UNVERIFIED. Correlation observed: `1`=pedal hat, `2`=open hat/crash, `3`=closed hat/ride, `10`=side stick, `14`=toms & muted crash. |
| `Voice` | int | `0`(4341) `1`(11) | Score voice. `QBDrumMap` enum: `Up1=0, Down1=1, Up2=2, Down2=3` | **Notation decoration.** In the ezd2 example: cymbals→0, drums→1, i.e. the classic two-voice drum staff. |
| `PortIndex` | int | `0` in all 4 352 | Index into the `OutputDevices` list | Per-entry output-port selector. Needed only for multi-port maps. |
| `Name` | string(wide) | free text | Row label | The **display name** of the pivot symbol, in the user's language. |
| `QuantizeIndex` | int | `0` in all 4 352 | Index into the `Quantize` list | Export-only. Emit `0`. |
| `NoteheadSet` | int (12+) | `0` | 1-based index into `scoreLibrary.xml` `NoteheadSetDefinition`; `0` = none | Notation decoration; supersedes `HeadSymbol` in Cubase 12+. |
| `InstrumentEntityID` | string (12+) | `""` in the one file found | **Symbolic** percussion-instrument ID from `Components/ScoringEngine/instruments.xml` (`InstrumentEntityDefinition@entityID`, filtered to those with a `percussionInstrumentDataID`) | **This is a first-class symbolic instrument slot in the file format.** The pivot's `instrument` axis maps here. |
| `TechniqueEntityID` | string (12+) | `""` | **Symbolic** playing-technique ID from `playingTechniqueDefinitions.xml` (`PlayingTechniqueDefinition@entityID`, `groupType == "kTechniques"`) | **The pivot's articulation/technique axis maps here.** |

Source for the two entity fields' provenance: `QBDrumMap/Class/Cubase/CubaseScore.cs`,
which reads `Components\ScoringEngine\{instruments.xml, scoreLibrary.xml,
playingTechniqueDefinitions.xml, l10n\instrumentnames_*.xml}` from the Cubase install
directory. **Cubase 12+ therefore already carries a symbolic (instrument, technique) pair
per drum-map slot — exactly the KITWARP pivot shape**, and it is Dorico's `kScoreLibrary`
vocabulary (§3.4).

#### 2.1.5 FIELD TABLE — `.drm` other lists

| List | Field | Domain | Pivot requirement |
|---|---|---|---|
| root | `Name` | string(wide) | Map/layout display name |
| `Quantize` item | `Grid` | `4` (34/34) | export-only constant |
| | `Type` | `0` | export-only |
| | `Swing` | `0` | export-only |
| | `Unquantized` | `0` (newer files) / absent | export-only |
| | `Legato` | `50` (newer) / absent | export-only |
| | `MaxDiff`,`Tuplet`,`Move CC` | older schema only | export-only |
| `Order` | 128 × `item@value` | permutation of 0–127 | **Row display order.** 8 of 34 files use a non-identity permutation (e.g. `DrumMica GM.drm` starts `35,36,37,38,39,40,55,67,…`). The pivot must be able to emit an **ordering** — either a stored per-layout order or one derived from the pivot's own canonical instrument order. |
| `OutputDevices` item | `DeviceName`, `PortName` | `"Default Device"`/`"Default Port"` in all files | export-only unless multi-port |
| root | `Flags` | `0` | export-only |

#### 2.1.6 Extension collision — MuseScore `.drm`

MuseScore drumsets also use `.drm` and are **not** the same format:
`<museScore version="…"><Drum pitch="…"><head/><line/><voice/><name/><stem/><shortcut/>…`.
Six such files sit in the MuseScore repo. An importer must sniff the root element
(`DrumMap` vs `museScore`). MuseScore's schema is analysed in dossier `02-notation-oss.md`
and is not repeated here.

---

### 2.2 Reaper — `MIDINoteNames/*.txt`

#### 2.2.1 Grammar (measured, not guessed)

Across ~1 500 non-blank lines from four independent corpora, exactly **four** line shapes
occur and no others:

```
line      ::= comment | blank | note-line | cc-line
comment   ::= ( "#" | "//" ) <rest of line>
note-line ::= <int 0..127> WS <name to end of line>
cc-line   ::= "CC" <int 0..127> WS <name to end of line>
```

- Whitespace separator may be a single space or a TAB (both occur in the wild).
- Names may contain spaces; they are **not** quoted and run to end of line.
- Order is free; files in the wild are commonly descending, and gaps are allowed.
- Convention (not required): first line `# MIDI note/CC name map`.
- `~` is used by one generator (`MidiNoteNameGen`) as a "blank" name for unused notes;
  `----` and `---` are used by others. **No format-level "empty" marker exists.**

Verbatim, `HarleyGaniere/Reaper-Track-Builder/MIDINoteNames/TC Electronic M300.txt` — the
only CC-name file found in any public corpus:

```
# MIDI note/CC name map
CC83 Reverb Off
CC82 Multi-Effect Off
CC81 Bypass
CC80 Multi-Effect Tap
CC51 Reverb Type
CC50 Multi-Effect Type
CC20 Reverb Color
```

Verbatim, `DigitalInBlue/ReaperNoteNames/getgooddrums_modernandmassive.txt`:

```
# Getgood Drums - Modern and Massive - Halpern
# MIDI note/CC name map

83 Splash - Choke
77 Splash - Main Hit
76 Ride - Crash
74 Ride - Bell
73 Ride - Tip
```

#### 2.2.2 What the `.txt` cannot express

**There are no per-channel sections and no colour lines in the `.txt` format.** Zero
occurrences in 1 500+ lines; no generator emits them.

Channel *is* expressible in Reaper — but only in the project file and via ReaScript:

- `SetTrackMIDINoteNameEx(proj, track, pitch, chan, name)` — Ultraschall's copy of the
  ReaScript API doc states verbatim: *"channel > 0 assigns note name to all channels.
  pitch 128 assigns name for CC0, pitch 129 for CC1, etc."* (The `> 0` is almost certainly
  a doc typo for `< 0`/`-1`; the RPP data below uses `-1` for omni. UNVERIFIED.)
- RPP chunk, from `ReaTeam/Doc` → `State Chunk Definitions` (verbatim, comments included):

```
  <MIDINOTENAMES                  // Custom MIDI note names applied to Piano roll in all MIDI items
   -1 36 "My note 1" 0 36         //  on the track
   -1 38 "My note 2" 0 38         //  field 1, int, MIDI channel number, -1 = Omni, named notes can be
   -1 40 "My note 3" 0 40         //  assigned to different channels, and the same named note can be
   -1 41 "My note 4" 0 41         //  assigned to more that one channel, in which case its listed as many
   -1 43 "My note 5" 0 43         //  times as there're channels it's assigned to appearing under
  >                               //  different channel numbers;
                                  //  field 2, int, 0-based note number; field 3, string, note name,
                                  //  if the name contains spaces it's enclosed within quotes;
                                  //  field 4 ??; field 5, int, note number.
                                  //  …
                                  //  Manual input of note names in the MIDI Editor always results in Omni
                                  //  assignment. Linking note names to specific MIDI channel is only
                                  //  possible via API using Get/SetTrackMIDINoteName(Ex) functions
                                  //  or by manual editing of the .rpp file.
```

Note colouring in Reaper is done with **colormaps** (PNG files), a separate mechanism
entirely — confirmed by `shadowflower64/yarg-reaper-template`, which ships colormaps and
note-name files as different artefacts.

#### 2.2.3 FIELD TABLE — Reaper `.txt`

| Field | Required by format | Pivot requirement |
|---|---|---|
| note number 0–127 | yes | target-layout note number |
| name (free text, to EOL, unquoted) | yes | display name; **must not contain a newline**; leading token must not be parseable as another number if a stray leading digit would confuse the reader |
| CC number 0–127 (`CC<n>` prefix) | optional | **controller axis**: the pivot must carry named controllers (hi-hat pedal CC, positional-sensing CC) as first-class entries, not only notes |
| comment lines | optional | provenance/source header — nice-to-have |
| — no channel | — | a multi-channel layout **loses its channel split** on this target |
| — no colour, no notehead, no length | — | drop silently |

**Loss on export:** channel, output note (the format is naming-only, never remapping),
colour, all notation fields.

---

### 2.3 Cakewalk instrument definitions — `.ins`

#### 2.3.1 Grammar

Windows-INI-like plain text, one or many instruments per file. Comments start with `;`.
Six top-level sections, each introduced by a line starting with a dot **at column 1, no
brackets**:

```
.Patch Names
.Note Names
.Controller Names
.RPN Names
.NRPN Names
.Instrument Definitions
```

Occurrence over 20 files: `.Patch Names` 19, `.Instrument Definitions` 19,
`.Note Names` 18, `.Controller Names` 18, `.RPN Names` 6, `.NRPN Names` 6.

Inside the first five sections:

```
[<Subsection Name>]
BasedOn=<Other Subsection Name>     ; optional inheritance
<number>=<Text Name>                ; number is 0..127 for notes/controllers,
                                    ; 0..16383 for NRPN
```

Two built-in subsection names exist and need no definition: `0..127` and `1..128`.
`BasedOn=` is used in the wild (e.g. `[CS2x 909 Kit]` with `BasedOn=CS2x 808 Kit` in
`cakewalkmodified/Yamaha.ins`).

Inside `.Instrument Definitions`:

```
[<Instrument Name>]
Patch[<bank>]=<Patch-Names subsection>       ; bank = (MSB<<7)+LSB, or "*" = any bank
Key[<bank>,<program>]=<Note-Names subsection>; "*" allowed in either position
Drum[<bank>,<program>]=1                     ; 1 ⇒ open a drum editor for this voice
Control=<Controller-Names subsection>
RPN=<RPN-Names subsection>
NRPN=<NRPN-Names subsection>
BankSelMethod=<0|1|2|3>                      ; 0 normal, 1 MSB only, 2 LSB only, 3 PC only
UseNotesAsControllers=<0|1>                  ; default 0
```

Measured key frequencies across the 20 `.ins`: `Key[…]` 4 389, `Patch[…]` 3 481,
`Drum[…]` 1 475 (**value is `1` in every single occurrence**), `Control=` 181,
`BankSelMethod=` 61 (`1`×49, `2`×5, `3`×7), `RPN=` 48, `NRPN=` 36.
`UseNotesAsControllers` occurs 0 times in this corpus.

#### 2.3.2 Verbatim excerpt

`instrumentdefs/cakewalkmodified/Roland.ins`:

```
.Note Names


[1:Standard 1]
22=MC500 Beep1
23=MC500 Beep2
24=Concert SD
…
35=Kick Drum 2
36=Kick Drum 1
37=Side Stick
38=Reg.Snr 2
```

```
.Instrument Definitions


[Roland JUNO-Gi:Rhythm]

Patch[11008]=JUNO-Gi PRESET Rhythm 1-14
Key[11008,0]=1:Standard 1
Key[11008,1]=2:Standard 2
Key[11008,2]=3:Standard 3
…
Drum[11008,*]=1
```

#### 2.3.3 FIELD TABLE — `.ins`

| Field | Pivot requirement |
|---|---|
| `.Note Names` subsection name | A **kit / layout name** — the pivot needs a stable layout identifier and a display name |
| `<note>=<name>` | target-layout note number + display name. **Only 0–127; no output note, no channel, no colour, no notation.** |
| `BasedOn=` | optional: a *derivation* relation between layouts (kit B = kit A plus overrides). KITWARP's fallback/inheritance data could emit this, but nothing is lost if it does not. |
| `.Controller Names` `<cc>=<name>` | **controller axis** — same requirement as Reaper `CC<n>` lines |
| `.RPN` / `.NRPN` `<n>=<name>` | out of scope for drum layouts; emit nothing |
| `Patch[bank]=` | a **program/bank** address for the kit: bank = `(MSB<<7)+LSB`. Hardware modules (TD/DTX/GM2) select kits this way. The pivot's *layout* record needs an optional `{bankMSB, bankLSB, program}` address. |
| `Key[bank,prog]=` | binds a note-name subsection to a specific bank+program — i.e. **"this kit's note layout"**. |
| `Drum[bank,prog]=1` | a boolean "this is a drum kit" |
| `BankSelMethod` | 0 normal / 1 MSB only / 2 LSB only / 3 program-change only — a per-device property, not per-note |
| `Control=` / `RPN=` / `NRPN=` | reference by subsection name |

**Loss on export:** output note, channel, colour, notehead, display note, length,
articulation. `.ins` is purely `note → name`, plus a bank/program addressing layer that
none of the other targets have.

Spec cross-check: `https://tse3.sourceforge.net/doc/InsFiles.html` (TSE3 project's
reverse-engineered spec) agrees with every construct measured above, and supplies the
`BankSelMethod` value meanings and the `(MSB<<7)+LSB` bank formula.

---

### 2.4 Studio One — `.pitchlist` (pitch names / drum map)

#### 2.4.1 Grammar

UTF-8 XML (files in the wild carry a BOM), root `<Music.PitchNameList>`, one
self-closing `<Music.PitchName>` per named pitch. **Sparse** — only named pitches appear;
files in the corpus range from 29 to 128 entries.

#### 2.4.2 Verbatim examples

`chad-ramos/studio-one-drum-maps/Superior Drummer 3.pitchlist` (head):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Music.PitchNameList>
	<Music.PitchName pitch="127" name="127 Sn Forward Brushtrig" color="FF51D361"/>
	<Music.PitchName pitch="118" name="118 Ri Mute Hit" color="FF5C00FF"/>
	<Music.PitchName pitch="117" name="117 Ri Bell Tip" color="FF5C00FF"/>
	<Music.PitchName pitch="116" name="116 Ri Bow Shank" color="FF5C00FF"/>
</Music.PitchNameList>
```

`tephrocactus/studio-one/drum-maps/GGD Invasion.pitchlist` — the full attribute set:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Music.PitchNameList title="GGD Invasion">
	<Music.PitchName pitch="23" name="Kick L" scorePitch="65"/>
	<Music.PitchName pitch="30" name="Snare Sidestick" scorePitch="72" notehead="nhdX"/>
	<Music.PitchName pitch="45" name="Hat Open 1" scorePitch="79" notehead="nhdX" technique="circ"/>
	<Music.PitchName pitch="53" name="Main Crash L Choke" scorePitch="79" notehead="nhdX" technique="stac"/>
	<Music.PitchName pitch="80" name="Bell R Hit" scorePitch="91" notehead="nhDi"/>
</Music.PitchNameList>
```

#### 2.4.3 FIELD TABLE — `.pitchlist`

Domains measured over 17 720 `Music.PitchName` elements in 164 files.

| Attribute | On element | Occurrences | Domain | Pivot requirement |
|---|---|---|---|---|
| `title` | `Music.PitchNameList` | 17 (optional) | free text | layout display name |
| `pitch` | `Music.PitchName` | 17 720 (required) | 0–127 | target-layout note number |
| `name` | `Music.PitchName` | 17 610 | free text; `---` used 8 511× as "unused" | display name |
| `color` | `Music.PitchName` | 1 488, 98 distinct | 8 hex digits **ARGB**, e.g. `FF51D361` | **Colour decoration.** The pivot should carry a canonical colour per instrument *group* so the same kit piece is the same colour on every export. |
| `scorePitch` | `Music.PitchName` | 946, 20 distinct (`79`×267, `81`, `72`, `77`, `93`, `69`…) | 0–127 staff position | **Notation decoration.** Direct analogue of Cubase `DisplayNote`. |
| `notehead` | `Music.PitchName` | 582, 5 distinct: `nhdX`(480) `nhDi`(80) `nhSl`(12) `nhCX`(9) `nhTr`(1) | short symbolic codes (x-head, diamond, slash, circled-x, triangle — UNVERIFIED expansion) | **Notation decoration**, and unlike Cubase's integer this one is *symbolic*. |
| `technique` | `Music.PitchName` | 25, 2 distinct: `circ`(17) `stac`(8) | symbolic technique code | **A first-class articulation slot on a drum-map entry.** `circ` on open hi-hats, `stac` on chokes. Same role as Cubase's `TechniqueEntityID`. |
| `flags` | `Music.PitchName` | 3 | `show` | UNVERIFIED; row visibility |
| `collor` | `Music.PitchName` | 3 | typo in a user file — ignore | — |

Writer confirmation (`QBDrumMap/Class/StudioOne/PitchList.cs`) emits exactly:
`pitch`, `name`, and — only when non-empty — `color`, `scorePitch`, `notehead`,
`technique`, plus `title` on the list. That is the complete authoring surface.

**Loss on export:** output note, channel, length, mute, port. `.pitchlist` is
naming + notation + colour, never remapping.

---

### 2.5 MMA MIDI Name Document — `.midnam`
(Pro Tools, Logic external instruments, Digital Performer, Ardour, Mixbus)

This is the only *cross-vendor standardised* target, and it is the answer to "Pro Tools
instrument definition": **Pro Tools has no proprietary format; it reads `.midnam`.** Files
live in `/Library/Audio/MIDI Patch Names/<vendor>/` (macOS) or
`Program Files\Common Files\Avid\Pro Tools\MIDI Patch Names\` (Windows). Avid's own help
states Pro Tools "shows individual note names in piano roll editors (think drum kits…)".

#### 2.5.1 Grammar

XML with the MMA DTD:

```xml
<!DOCTYPE MIDINameDocument PUBLIC "-//MIDI Manufacturers Association//DTD MIDINameDocument 1.0//EN"
  "http://www.midi.org/dtds/MIDINameDocument10.dtd">
```

Verbatim, `Ardour/share/patchfiles/XLN_Audio_Addictive_Drums_2.midnam`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE MIDINameDocument PUBLIC "-//MIDI Manufacturers Association//DTD MIDINameDocument 1.0//EN" "http://www.midi.org/dtds/MIDINameDocument10.dtd">
<MIDINameDocument>
  <Author>Antti-Pekka Meronen</Author>
  <MasterDeviceNames>
    <Manufacturer>XLN Audio</Manufacturer>
    <Model>Addictive Drums 2</Model>
    <CustomDeviceMode Name="Drumkit Keymap">
      <ChannelNameSetAssignments>
        <ChannelNameSetAssign Channel="1" NameSet="Names"/>
        <ChannelNameSetAssign Channel="10" NameSet="Names"/>
      </ChannelNameSetAssignments>
    </CustomDeviceMode>
    <ChannelNameSet Name="Names">
      <AvailableForChannels>
        <AvailableChannel Channel="1" Available="true"/>
        <AvailableChannel Channel="10" Available="true"/>
      </AvailableForChannels>
      <UsesNoteNameList Name="Notes"/>
      <PatchBank Name="User Patches">
        <PatchNameList Name="User Patches"/>
      </PatchBank>
    </ChannelNameSet>
    <NoteNameList Name="Notes">
      <Note Number="7" Name="HiHat CC Hihat Shaft"/>
      <Note Number="36" Name="Kick"/>
      <Note Number="42" Name="Snare SideStick"/>
      <Note Number="49" Name="HiHat Closed 1 Tip"/>
    </NoteNameList>
  </MasterDeviceNames>
</MIDINameDocument>
```

#### 2.5.2 Element inventory (471 files)

| Element | Count | Attributes seen |
|---|---|---|
| `MIDINameDocument` | 471 | — |
| `Author` | 471 | — |
| `MasterDeviceNames` / `ExtendingDeviceNames` | 397 / 121 | — |
| `Manufacturer`, `Model` | 518 / 1 339 | text |
| `CustomDeviceMode` | 404 | `Name` |
| `ChannelNameSetAssign` | 5 162 | `Channel` 1–16, `NameSet` |
| `ChannelNameSet` | 513 | `Name` |
| `AvailableChannel` | 6 997 | `Channel` 1–16, `Available` true/false |
| `UsesNoteNameList` | 596 | `Name` |
| `NoteNameList` | 519 | `Name` |
| `NoteGroup` | 524 | `Name` (15 distinct: `Hi-Hat`, `Agogo`, `Triangle`, `Cuica`, `Conga Hi Mute/Open`…) |
| `Note` | **31 626** | **only `Number` and `Name`** |
| `PatchBank` | 4 178 | `Name`, `ROM` |
| `PatchNameList` / `Patch` | 4 601 / 207 075 | `Number`, `Name`, `ProgramChange` |
| `MIDICommands`/`PatchMIDICommands` → `ControlChange` | 48 940 | `Control` (0 or 32 — bank MSB/LSB), `Value` |
| `ControlNameList` / `Control` | 97 / 2 096 | `Type` (`7bit`/`14bit`/`NRPN`), `Number`, `Name` |
| `ValueNameList` / `Value` | 129 / 1 602 | `Number`, `Name`; `Values@Min/@Max` |
| `SysEx`, `SysExDeviceID`, `LocalControl` | 91 / 56 / 10 | device-mode plumbing |

#### 2.5.3 FIELD TABLE — `.midnam`

| Field | Pivot requirement |
|---|---|
| `Manufacturer`, `Model` | vendor + product for the layout — the pivot's **layout metadata** needs both |
| `Author` | provenance string |
| `CustomDeviceMode@Name` | a **named variant of a layout** (e.g. "Drumkit Keymap" vs "GM Keymap") — maps to KITWARP's notion of alternative presets for one product |
| `ChannelNameSet` + `ChannelNameSetAssign@Channel` | **per-channel note naming**, 1–16. This is the only text-based target that can express a channel split. The pivot must therefore carry an output channel per entry. |
| `NoteNameList@Name` | kit name |
| `NoteGroup@Name` | **an instrument-group label wrapping a set of notes** — a direct precedent for the pivot's `instrument` axis being a grouping level above the individual articulation. Only 15 distinct group names in this corpus, all coarse (`Hi-Hat`, `Triangle`…). |
| `Note@Number`, `Note@Name` | note number + display name. **No colour, no length, no output note, no notehead** — a `Colour` attribute appears in exactly one third-party file (`zynthian` `Fabla-Generic.midnam`) and is **not** in the DTD. |
| `PatchBank` + `Patch@ProgramChange` + `ControlChange@Control=0/32` | bank/program addressing (MSB=CC0, LSB=CC32) — same requirement as Cakewalk `Patch[bank]` |
| `Control@Number/@Name/@Type` | **controller axis**, with an explicit `7bit`/`14bit`/`NRPN` type — richer than Reaper or Cakewalk |
| `Value@Number/@Name` inside `ValueNameList` | **named values of a controller** — e.g. naming hi-hat-pedal CC positions. Nothing else in this dossier can express that. |

**Loss on export:** output note, notehead, display note, length, mute, colour.

---

### 2.6 `.iom` (SSD5-lineage I/O map)

Already reverse-engineered in this repository (`docs/01-format-iom.md`); restated here for
the field table. Verified against the 11 files in `data/legacy-iom/`.

#### 2.6.1 Container

| Offset | Size | Content |
|---|---|---|
| 0 | 4 | magic `56 43 32 21` = `VC2!` |
| 4 | 4 | uint32 LE = XML byte length, excluding the NUL |
| 8 | N | XML payload, latin-1, no declaration, no whitespace |
| 8+N | 1 | `0x00` terminator |
| 9+N | 1 | uninitialised padding byte — ignore on read, write `0x00` |

File size is always exactly `10 + N`.

#### 2.6.2 Payload

One self-closing XML element; everything is attributes:

```xml
<SAMPLER_IOMapInfo IOMapInfoVersion="2" IOMapName="ED_Superior3"
    Nv2_0Cnt="1" Nv2_0-0="76" Nv2_1Cnt="1" Nv2_1-0="74" …
    Cv2_127Cnt="1" Cv2_127-0="127"/>
```

- `Nv2_<k>Cnt` = number of targets for note index k (k = 0…127), then `Nv2_<k>-<i>`.
- `Cv2_<k>Cnt` / `Cv2_<k>-<i>` = identical shape for controllers.
- Both tables always hold 128 entries. `Cnt` is `0` or `1` in all 11 files; the format
  formally permits 1:n.
- Direction: index = note in the **foreign** layout, value = note in the **host's
  internal** layout.

#### 2.6.3 FIELD TABLE — `.iom`

| Field | Pivot requirement |
|---|---|
| `IOMapInfoVersion` | constant `"2"` — export-only |
| `IOMapName` | layout name, conventionally prefixed `ED_` |
| `Nv2_k` → list of ints | source note → one or more host notes. Requires: pivot symbol → source-layout note **and** pivot symbol → host-layout note. |
| `Cv2_k` → list of ints | controller remap. Identity in all 11 files, so it carries no information today — but the slot exists, and it is where the **CC4-vs-CC1 hi-hat pedal problem** would be expressed. |
| — no names | **The format carries no text at all.** Every name, every articulation, every notation attribute is lost. |

`.iom` is the **poorest** target: 128×128 integer→integer, twice. It is the lower bound
that the whole export set must degrade to.

---

### 2.7 Targets where a file export is not feasible

| Target | Verdict | Evidence |
|---|---|---|
| **Ableton Live drum rack** | **No importable naming file exists.** Pad names live inside a Drum Rack device group (`.adg`, gzipped XML) or the Live Set (`.als`). Pads are renamed only in the UI (Cmd/Ctrl-R). Live shows the pad name in the MIDI editor automatically; there is no "load note names from file". A KITWARP export would have to **generate a whole `.adg`** — one chain per pad with a `Show Names in MIDI Editor` MIDI Effect Rack, or a 128-pad Drum Rack. Technically possible (`Miserlou/ADGMaker`, `manuz888/L2Move` do generate `.adg`), but it is *device generation*, not *map export*, and the file would have to embed an instrument. **Recommend: out of scope for v1.** |
| **Logic Pro "mapped instrument"** | **No file format.** A mapped instrument is an Environment object stored inside the Logic project; Apple's documentation describes only in-window editing and `Initialize > Names as General MIDI`. It cannot be written or read as a standalone file. For *external* MIDI instruments Logic reads `.midnam` — so §2.5 is the only Logic-facing export. **Recommend: export `.midnam`, not a mapped instrument.** |
| **Pro Tools instrument definition** | **Does not exist as a proprietary format.** Pro Tools consumes MMA `.midnam` (§2.5). So this target is already covered. |

---

## 3. Articulation-map formats (a different class)

These do not name notes; they model an **articulation as a first-class object** with an
identity, a display, and an *action* (what MIDI to emit). They are the closest external
precedent for the KITWARP pivot's articulation axis.

### 3.1 Cubase Expression Map — `.expressionmap`

Same Steinberg typed-XML serialiser as `.drm`. Root `<InstrumentMap>`. Measured over
76 files / 3 968 sound slots.

#### 3.1.1 Object model

```
InstrumentMap
├─ string name                       map name
├─ member "slotvisuals" → list of USlotVisuals   (the palette of articulation "looks")
├─ member "slots"       → list of PSoundSlot     (the articulations themselves)
│   ├─ obj PSlotThruTrigger  name="remote"       what selects this slot from the keyboard
│   ├─ obj PSlotMidiAction   name="action"       what this slot emits
│   │   ├─ member "noteChanger"  → list of PSlotNoteChanger
│   │   └─ member "midiMessages" → list of POutputEvent
│   ├─ member "sv"   → list of USlotVisuals      (this slot's articulation symbols)
│   ├─ member "name" → string s                 slot display name
│   └─ int color
└─ member "controller"               (empty in all 76 files)
```

#### 3.1.2 Verbatim slot — `cbexpr/VSL/SY Drums/SY Taikos.expressionmap`

```xml
         <obj class="PSoundSlot" ID="12079598064">
            <obj class="PSlotThruTrigger" name="remote" ID="24028158000">
               <int name="status" value="144"/>
               <int name="data1" value="-1"/>
            </obj>
            <obj class="PSlotMidiAction" name="action" ID="7723476800">
               <int name="version" value="600"/>
               <member name="noteChanger">
                  <int name="ownership" value="1"/>
                  <list name="obj" type="obj">
                     <obj class="PSlotNoteChanger" ID="1041538288">
                        <int name="channel" value="-1"/>
                        <float name="velocityFact" value="1"/>
                        <float name="lengthFact" value="1"/>
                        <int name="minVelocity" value="0"/>
                        <int name="maxVelocity" value="127"/>
                        <int name="transpose" value="0"/>
                        <int name="minPitch" value="0"/>
                        <int name="maxPitch" value="127"/>
                     </obj>
                  </list>
               </member>
               <member name="midiMessages">
                  <int name="ownership" value="1"/>
                  <list name="obj" type="obj">
                     <obj class="POutputEvent" ID="2154833424">
                        <int name="status" value="144"/>
                        <int name="data1" value="46"/>
                        <int name="data2" value="120"/>
                     </obj>
                     <obj class="POutputEvent" ID="23712387728">
                        <int name="status" value="144"/>
                        <int name="data1" value="24"/>
                        <int name="data2" value="120"/>
                     </obj>
                  </list>
               </member>
               <int name="channel" value="-1"/>
               <float name="velocityFact" value="1"/>
               <float name="lengthFact" value="1"/>
               <int name="minVelocity" value="0"/>
               <int name="maxVelocity" value="127"/>
               <int name="transpose" value="0"/>
               <int name="maxPitch" value="127"/>
               <int name="minPitch" value="0"/>
               <int name="key" value="46"/>
               <int name="key2" value="24"/>
            </obj>
            <member name="sv">
               <int name="ownership" value="2"/>
               <list name="obj" type="obj">
                  <obj class="USlotVisuals" ID="7392658304">
                     <int name="displaytype" value="1"/>
                     <int name="articulationtype" value="1"/>
                     <int name="symbol" value="73"/>
                     <string name="text" value="cudgel" wide="true"/>
                     <string name="description" value="cudgel" wide="true"/>
                     <int name="group" value="0"/>
                  </obj>
               </list>
            </member>
            <member name="name">
               <string name="s" value="Cudgel" wide="true"/>
            </member>
            <int name="color" value="1"/>
         </obj>
```

#### 3.1.3 FIELD TABLE — `.expressionmap`

| Object · field | Count | Domain | Meaning | Pivot requirement |
|---|---|---|---|---|
| `InstrumentMap` `name` | 76 | string | map name | layout/patch name |
| `USlotVisuals.text` | 12 498 | 306 distinct (`legato`, `normal release`, `soft release`, `fast attack`, `portamento`…) | the text shown on the score | **articulation display token** |
| `USlotVisuals.description` | 12 498 | 332 distinct | tooltip / long name | articulation long name |
| `USlotVisuals.symbol` | 12 498 | 37 distinct; `73` = 8 880 (the text placeholder), `43` = 1 021, `0` = 229 | index into Cubase's articulation-symbol palette | symbol decoration; enum names UNVERIFIED |
| `USlotVisuals.displaytype` | 12 498 | `1` (12 191) / `0` (301) | `0` correlates with `text=""` in 282/301 cases ⇒ **0 = symbol, 1 = text** | display-mode decoration |
| `USlotVisuals.articulationtype` | 12 498 | `1` (12 476) / `0` (22) | Cubase's *Direction* vs *Attribute*. The file `Arkanthara/cubase-scripts/testexpression/Toms_attribute.expressionmap` carries `0`, so **0 = Attribute (one note), 1 = Direction (until changed)** | **A real semantic axis**: does this articulation apply to a single hit or persist? For drums, per-hit (Attribute) is the norm; hi-hat *openness held by a pedal* is arguably a Direction. |
| `USlotVisuals.group` | 12 498 | `0`–`3` | Cubase's four articulation groups; slots from different groups combine | **The pivot's axes are exactly this idea**: independent, simultaneously-selectable dimensions. Cubase caps it at 4. |
| `PSoundSlot` `name/s` | 3 968 | 1 095 distinct | slot name | articulation name |
| `PSoundSlot` `color` | 3 968 | `1`–`16` | Cubase's 16 slot colours | colour decoration (**integer index**, not RGB — unlike Studio One's ARGB) |
| `PSlotThruTrigger.status` | 3 968 | `144` (note-on) only | trigger message type | — |
| `PSlotThruTrigger.data1` | 3 968 | `-1` (3 938) or a note 0–127 | **remote key** that selects the slot from the keyboard; `-1` = none | optional "remote select" note per articulation |
| `PSlotMidiAction.key` / `key2` | 3 968 / 3 791 | 50 / 46 distinct notes | the keyswitch note(s) written back | **articulation → keyswitch note**, up to 2 |
| `POutputEvent.status/data1/data2` | 13 460 | status `144`(13 425 note-on) or `176`(35 CC); data2 `120` for 13 425 | the actual MIDI emitted, **an ordered list** | **1→N expansion:** one articulation may emit several messages. KITWARP's `expand` rules map here directly. |
| `PSlotMidiAction.controller1num` / `controller1value` | 35 | `3`,`1`,`0` / 9 values | a CC sent with the slot | controller axis |
| `PSlotNoteChanger` `channel` | 3 968 | `-1` | output channel override | per-articulation channel |
| `PSlotNoteChanger` `velocityFact` | 3 968 | `1` (3 960), `1.2` (8) | velocity multiplier | **velocity scaling** — KITWARP's `velocityDelta` is the additive cousin |
| `PSlotNoteChanger` `lengthFact` | 3 968 | `1`, `0.5` | length multiplier | length scaling |
| `PSlotNoteChanger` `minVelocity`/`maxVelocity` | 3 968 | `0`/`127`, one map uses `56` | **input velocity range that selects this slot** | **velocity-layer axis** — an articulation can be velocity-gated |
| `PSlotNoteChanger` `minPitch`/`maxPitch` | 3 968 | `0`/`127` | input pitch range gate | pitch-range gate |
| `PSlotNoteChanger` `transpose` | 3 968 | `0` | transposition | transpose |
| `PSlotMidiAction.version` | 3 968 | `600` | schema version | export-only |

### 3.2 Logic Pro Articulation Set — `.plist`

Apple property list (XML plist 1.0). Measured over 49 files / 659 articulations.

#### 3.2.1 Verbatim — `nobodo/logic-pro-x-articulation-sets/Cinematic Studio Strings.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Articulations</key>
	<array>
		<dict>
			<key>ArticulationID</key>
			<integer>1</integer>
			<key>ID</key>
			<integer>1001</integer>
			<key>Name</key>
			<string>Legato</string>
			<key>Output</key>
			<dict>
				<key>MB1</key>
				<integer>58</integer>
				<key>Status</key>
				<string>Controller</string>
				<key>ValueLow</key>
				<integer>10</integer>
			</dict>
		</dict>
	</array>
	<key>MultipleOutputsActive</key>
	<false/>
	<key>Name</key>
	<string>Cinematic Studio Strings.plist</string>
	<key>Switches</key>
	<array/>
</dict>
</plist>
```

#### 3.2.2 FIELD TABLE — Logic articulation set

| Key | Count | Domain | Meaning (from `chrisself/switchboard` source comments + corpus) | Pivot requirement |
|---|---|---|---|---|
| `Name` (top) | 49 | string, usually the filename | set name | layout/patch name |
| `Articulations[]` | 659 | array | the articulations | one entry per pivot articulation |
| `…ArticulationID` | 659 | 86 distinct, 1-based by default | **the value stamped on every MIDI note event in the project** — the stable, user-visible ID | **A per-articulation stable integer ID.** If KITWARP re-exports a set, this number must not move, or existing MIDI in the user's project re-points to the wrong articulation. The pivot must therefore carry a **stable numeric alias** per (layout, articulation), not just a symbolic name. |
| `…ID` | 659 | 107 distinct, generated from 1001 | Logic-internal, not user-assignable | export-only; emit `1000 + ArticulationID` |
| `…Name` | 659 | 162 distinct | display name | articulation display name |
| `…Symbol` | 119 | 8 distinct: `Marcato`(42) `Staccatissimo`(32) `Pizzicato (Left Hand)`(20) `Tenuto`(11) `Staccato`(10) `Pizzicato`(2) `Doit Short` `Fall Short` | **notation symbol, referenced by name string** (not an integer) | symbol decoration — and note it is *symbolic*, so a symbolic pivot symbol axis maps cleanly |
| `…Output` | 192 as dict, 467 as array-of-dict | — | what to emit; **either one message or an ordered list** | 1→N expansion |
| `…Output.Status` | 659 | `Note On` (552) / `Controller` (107) | message type | message-type axis |
| `…Output.MB1` | 659 | note number or CC number | first data byte | keyswitch note / CC number |
| `…Output.ValueLow` | 192 | 89 distinct | second data byte (velocity / CC value) | value |
| `Switches[]` | 49, **empty in all 49** | — | input-side selectors (what the *player* does to pick the articulation) | UNVERIFIED shape; no public example found |
| `MultipleOutputsActive` | 1 | `False` | enables the array form of `Output` | export-only flag, set `true` when emitting >1 message |
| `InputMidiChannel` | 13 | `-1` | input channel filter | optional |
| `OctaveOffset` | 13 | `0` | display octave offset | export-only |
| `SwitchingEnabled` | 13 | `False` | — | export-only |

### 3.3 Studio One Sound Variations — `.keyswitch`

Stored under *Studio One User Data / Keyswitches*. UTF-8-BOM XML, root
`<Music.KeySwitchList>`, one `<Attributes>` element per variation. Measured over 46 files
/ 339 variations.

Verbatim, `WaltRitscher/studio-one-user-presets/Key Switches/Electric Sunburst Pure Patterns.keyswitch`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Music.KeySwitchList name="Electric Sunburst Pure Patterns" target.class="5653544E694B4B6B6F6D706C65746520">
	<Attributes name="Pure A" color="FFDD6105" id="36" pitch="36" activation="note36"/>
	<Attributes name="Pure B" color="FFD89D00" id="37" pitch="37" activation="note37"/>
	<Attributes name="Ending: Long" color="FF04FFE1" id="44" pitch="44" activation="note44"/>
</Music.KeySwitchList>
```

The minimal form used by most files:

```xml
<Music.KeySwitchList>
	<Attributes pitch="24" name="Sustain p"/>
	<Attributes pitch="25" name="Sustain f"/>
</Music.KeySwitchList>
```

#### 3.3.1 FIELD TABLE — `.keyswitch`

| Attribute | Count | Domain | Meaning | Pivot requirement |
|---|---|---|---|---|
| `Music.KeySwitchList@name` | 15 | string | map name | layout name |
| `Music.KeySwitchList@target.class` | 5 | hex-encoded ASCII plug-in class ID (`5653544E694B4B6B…` = `VSTNiKKkomplete `) | binds the map to a specific plug-in | **plug-in identity per layout** — worth storing; nothing else in this dossier records it |
| `Attributes@pitch` | 332 | 0–127 | keyswitch note | keyswitch note |
| `Attributes@name` | 332 | 103 distinct | display name | articulation display name |
| `Attributes@color` | 35 | 8 hex ARGB | colour | colour decoration |
| `Attributes@id` | 36 | int | stable variation ID | **stable numeric alias**, same requirement as Logic's `ArticulationID` |
| `Attributes@activation` | 35 | `note<n>` (23 distinct) | **how the variation is activated**, as a symbolic string | activation-method axis; only `note*` seen. The newer Sound Variation editor also offers Note on/off, Note off, Controller changes, Program Changes and Bank Changes (Spitfire's Studio One guide) — presumably other `activation` tokens. **UNVERIFIED.** |
| `Attributes@symbol` | 6 | `stac` `slur` `trm3` `circ` `pizz` `sord` | **symbolic** musical symbol — same vocabulary family as `.pitchlist@technique` | symbol/technique decoration |
| `Attributes@variationID` | 6 | 0–6 | UNVERIFIED; probably links to a plug-in-side variation index | — |
| `Attributes@useGenerator` | 2 | `0`/`1` | UNVERIFIED | — |

Note the shared vocabulary: `.keyswitch@symbol` and `.pitchlist@technique` both use the
four-letter codes (`stac`, `circ`). Studio One uses **one symbolic technique vocabulary**
across its drum-map and its articulation-map formats.

### 3.4 Dorico expression maps — `.doricolib`

XML, root `<kScoreLibrary>` with **48 sibling containers**, of which only
`<expressionMapDefinitions>` is populated for an expression-map file; the other 47 are
`<entities array="true"/>`. Measured over 11 files / 22 `ExpressionMapDefinition` /
496 `playingTechniqueCombination` / 1 185 `switchOnAction`.

#### 3.4.1 Verbatim — `fiddle/example-expression-maps/BWWA Eb Clarinet.doricolib`

```xml
	<expressionMapDefinitions>
		<entities array="true">
			<ExpressionMapDefinition>
				<name>BWWA Eb Clarinet</name>
				<entityID>xmap.user.bwwa_eb_clarinet</entityID>
				<parentEntityID/>
				<inheritanceMask>0</inheritanceMask>
				<creator>Andy Hyner</creator>
				<description/>
				<version>1</version>
				<pluginNames/>
				<autoMutualExclusion>true</autoMutualExclusion>
				<allowMultipleNotesAtSamePitch>false</allowMultipleNotesAtSamePitch>
				<initSwitchData>
					<enabled>true</enabled>
					<initActions array="true"/>
				</initSwitchData>
				<playingTechniqueCombinations array="true">
					<playingTechniqueCombination>
						<baseSwitchID>0</baseSwitchID>
						<techniqueIDs>pt.natural</techniqueIDs>
						<enabled>true</enabled>
						<flags>0</flags>
						<conditionString>NoteLength &lt; kMedium</conditionString>
						<velocityRange>1,127</velocityRange>
						<pitchRange>0,127</pitchRange>
						<transpose>0</transpose>
						<ticksBefore>0</ticksBefore>
						<velocityFactor>1.000000</velocityFactor>
						<lengthFactor>1.000000</lengthFactor>
						<volumeType>
							<type>kCC</type>
							<param1>1</param1>
						</volumeType>
						<volumeType2>
							<type>kCC</type>
							<param1>11</param1>
						</volumeType2>
						<attackType>
							<type>kNoteVelocity</type>
							<param1>0</param1>
						</attackType>
						<switchOnActions array="true">
							<switchOnAction>
								<type>kKeySwitch</type>
								<param1>27</param1>
								<param2>127</param2>
							</switchOnAction>
						</switchOnActions>
						<switchOffActions array="true"/>
					</playingTechniqueCombination>
```

#### 3.4.2 FIELD TABLE — Dorico expression map

| Element | Count | Domain | Meaning | Pivot requirement |
|---|---|---|---|---|
| `name` | 22 | string | map name | layout name |
| `entityID` | 22 | all distinct, pattern `xmap.user.<slug>` | **globally unique, stable, symbolic map ID** | KITWARP layouts need exactly this: a stable slug ID separate from the display name |
| `parentEntityID` + `inheritanceMask` | 22 | empty / `0` here | **map inheritance** — a map can extend another | precedent for KITWARP's layered/fallback layouts |
| `creator`, `description`, `version`, `pluginNames` | 22 each | strings | provenance + plug-in binding | metadata |
| `autoMutualExclusion` | 21 | `true`(17)/`false`(4) | auto-derive which techniques cancel each other | — |
| `allowMultipleNotesAtSamePitch` | 17 | `false` | — | — |
| `mutualExclusionGroups/mutualExclusionGroup` | 20 | `{groupID, name, techniqueIDs}`; groupIDs like `ptmg.user.short_strings`, `ptmg.user.pizzarco`, `ptmg.user.mute`, `ptmg.user.divisi` | **explicit named groups of mutually exclusive techniques** | **This is the axis concept made explicit and *named*.** `pizz/arco` = one axis; `mute` = another; `divisi` = another. KITWARP's axes (openness, damping, zone, implement) are precisely such mutual-exclusion groups. Dorico allows an arbitrary number, unlike Cubase's 4. |
| `playingTechniqueCombination/techniqueIDs` | 496 | **171 distinct**; comma-separated lists of `pt.*` IDs (`pt.natural`, `pt.legato`, `pt.staccato`, `pt.accent`, `pt.tremolo`, `pt.trill.half`, plus user IDs `pt.user.divisi_1`, `pt.user.solo`, `pt.user.tutti`) | **A slot is keyed by a SET of orthogonal technique IDs, not by one name.** | **The single most important precedent in this dossier.** Dorico does not enumerate articulations; it enumerates *combinations of independent technique tags*. That is the KITWARP pivot's multi-axis identity, in a shipping product. Also note the `pt.user.*` namespace for user-defined techniques — the pivot needs an extension namespace. |
| `…/baseSwitchID` | 496 | 177 distinct | stable slot ID | stable numeric alias |
| `…/name` | 200 | 158 distinct (`Legato + Marcato`, `Natural short`…) | optional display override; otherwise derived from the technique IDs ("`{pt.staccato, pt.legato}` → *Staccato + Legato*", per `fiddle/Source/Server/ExpressionMapParser.cpp`) | **display name is derivable from the axis values** — the pivot need not store one |
| `…/conditionString` | 496 | 10 distinct: `NoteLength < kShort`, `NoteLength == kVeryShort`, `NoteLength > kVeryShort`, `NoteLength >= kMedium`… | **a condition expression that gates the slot** | conditional selection — richer than a velocity range |
| `…/velocityRange`, `velocityRange2` | 496 / 58 | `0,127`, `1,127`, `10,127`, `56,127`; `60,127`, `1,2` | input velocity gate (two independent ranges) | **velocity-layer axis** |
| `…/pitchRange` | 496 | `0,127` | pitch gate | pitch gate |
| `…/transpose` | 496 | `0`, `-24` | transposition | transpose |
| `…/velocityFactor`, `lengthFactor` | 496 / 342 | `1`; `0.8`, `1.1` | scaling | velocity/length scaling |
| `…/monophonic` | 197 | `false`(164)/`true`(33) | — | — |
| `…/exclusionGroup` | 187 | `1` | group membership | axis membership |
| `…/flags` | 496 | `0`(455)/`1`(41) | UNVERIFIED | — |
| `…/millisecondsBefore`, `ticksBefore`, `applyMillisecondsBeforeToControllers`, `applyMillisecondsBeforeToEndOffsets` | 197/496/126/126 | `0`,`0`,`true`,`true` | pre-roll timing for keyswitches | timing decoration |
| `…/switchOnActions/switchOnAction{type,param1,param2}` | 1 185 | **type ∈ {`kKeySwitch`(991), `kNoteVelocity`(158), `kControlChange`(24), `kChannelSwitch`(12)}**; param1 = note/CC/channel, param2 = value (`127`×876, `120`×273) | **an ordered list of switching actions** | **1→N expansion with typed actions.** The `kChannelSwitch` type is the multi-channel case; `kNoteVelocity` is UACC-style. |
| `…/switchOffActions` | 496 | empty in this corpus | actions to undo the switch | needed for held/Direction articulations |
| `…/volumeType`, `volumeType2` `{type,param1}` | 496 / 232 | type ∈ {`kNoteVelocity`, `kCC`}; param1 ∈ {0,1,2,11} | which controller carries dynamics | **controller-role binding**: "dynamics is CC1", "expression is CC11". KITWARP's controller axis needs the same idea for hi-hat pedal. |
| `…/attackType` | 496 | `kNoteVelocity` / `0` | which controller carries attack | controller-role binding |
| `techniqueAddOns/techniqueAddOn{name, techniqueIDs, techAddOnSwitchID, switchOnActions, switchOffActions, enabled}` | 7 | `pt.soft`, `pt.fadeOut`, `pt.muted`, `pt.flautando`, `pt.sulPonticello` | **modifiers layered on top of a base combination** | **A second-order axis**: a technique that composes with any base slot rather than defining its own slot. Directly relevant to KITWARP's damping/openness modifiers. |
| `playbackOptionsOverrides/optionsOverride{option,value}` | 8 | `timingOptions.staccatoDurationPercent` etc., `int: 80` | per-map playback option overrides | out of scope |
| `microtonalPlaybackMethod`, `pitchBendRange`, `applyStageTemplateSettings` | 3 each | `kAuto`, `2`, `false` | — | out of scope |

### 3.5 The Cubase 12 ↔ Dorico entity bridge

Cubase 12+ adopted Dorico's `kScoreLibrary` scoring engine. Consequences established from
`QBDrumMap/Class/Cubase/CubaseScore.cs`:

| Cubase `.drm` field | Resolved against | Element | Key |
|---|---|---|---|
| `InstrumentEntityID` | `Components/ScoringEngine/instruments.xml` | `InstrumentEntityDefinition` | `@entityID`; only those with a non-empty `@percussionInstrumentDataID` are offered in a drum map; display name from `@name` or, localised, from `instrumentnames_<lang>.xml` via `@nameID` |
| `TechniqueEntityID` | `Components/ScoringEngine/playingTechniqueDefinitions.xml` | `PlayingTechniqueDefinition` | `@entityID`, filtered to `@groupType == "kTechniques"`; display name `@name` |
| `NoteheadSet` | `Components/ScoringEngine/scoreLibrary.xml` | `NoteheadSetDefinition` | **1-based ordinal** into the list; `0` = none |

So a modern Cubase drum-map slot is already
`(inputNote, outputNote, instrumentID, techniqueID, noteheadSet, …)` — i.e. Steinberg
independently arrived at *symbolic instrument + symbolic technique* per slot, which is the
KITWARP pivot. **KITWARP should be able to emit both IDs**, and its own instrument/
articulation vocabulary should be crosswalk-able to Dorico's `pt.*` and Cubase's
percussion `InstrumentEntityDefinition` IDs.

---

## 4. Union of required fields, and the export-only decorations

### 4.1 Union — what the pivot data model must be able to produce

Grouped by whether it belongs to the pivot **symbol** (layout-independent) or to a
**layout binding** (per target device/library).

#### A. Pivot symbol (layout-independent)

| Field | Needed by | Notes |
|---|---|---|
| stable symbolic ID (slug) | Dorico `entityID`/`pt.*`, Cubase 12 `TechniqueEntityID`/`InstrumentEntityID` | must never change once published |
| instrument axis value | Cubase `InstrumentEntityID`; `.midnam` `NoteGroup`; every display name | |
| articulation / technique axis values (a **set**, not one) | Dorico `techniqueIDs`; Studio One `technique`/`symbol`; Cubase `TechniqueEntityID` | Dorico proves the set form is the right shape |
| axis membership → mutual-exclusion group | Dorico `mutualExclusionGroups`; Cubase `USlotVisuals.group` (capped at 4) | |
| display name (per language) | every target | Dorico shows it is *derivable* from the axis values; localisation precedent in Cubase's `instrumentnames_<lang>.xml` |
| long description | Cubase `USlotVisuals.description` | |
| canonical colour | Studio One `color`/ARGB, Cubase `PSoundSlot.color`/index 1–16 | store one canonical colour per instrument group; map to each target's encoding |
| notation: staff position | Cubase `DisplayNote`, Studio One `scorePitch` | derived from instrument + zone |
| notation: notehead | Cubase `HeadSymbol` (int) / `NoteheadSet` (int), Studio One `notehead` (symbolic `nhdX`…), Logic `Symbol` (name string) | store the **symbolic** notehead; map to each target's encoding |
| notation: score voice | Cubase `Voice` (Up1/Down1/Up2/Down2) | derived from instrument family (cymbals up, drums down) |
| canonical display order | Cubase `Order` list (8/34 files use a non-identity permutation) | |

#### B. Layout binding (per source or target device/library)

| Field | Needed by | Notes |
|---|---|---|
| note number 0–127 | all note-name targets | |
| **output** note number (may differ from input) | Cubase `ONote`, `.iom` `Nv2_k-i` | naming-only targets ignore it |
| output channel 1–16 (or "inherit") | Cubase `Channel`, `.midnam` `ChannelNameSet`, Dorico `kChannelSwitch` | Reaper `.txt`, `.ins`, `.pitchlist` cannot express it |
| output port index | Cubase `PortIndex` + `OutputDevices` | |
| keyswitch note(s) | Cubase `key`/`key2`, Logic `Output.MB1`, Studio One `pitch`, Dorico `kKeySwitch` | up to 2 in Cubase; a list elsewhere |
| controller number + value | Reaper `CC<n>`, `.ins` `.Controller Names`, `.midnam` `Control`, Cubase `controller1num/value` + `POutputEvent` status 176, Dorico `kControlChange` / `volumeType` | **first-class controller entries, not just notes** |
| named controller values | `.midnam` `ValueNameList`/`Value` | only `.midnam` can carry these |
| controller **role** binding (dynamics / expression / attack / hi-hat position) | Dorico `volumeType`, `volumeType2`, `attackType` | |
| ordered list of emitted messages (1→N) | Cubase `midiMessages`, Logic `Output` array, Dorico `switchOnActions` | |
| velocity gate (min,max) | Cubase `minVelocity/maxVelocity`, Dorico `velocityRange`, `velocityRange2` | |
| pitch gate (min,max) | Cubase `minPitch/maxPitch`, Dorico `pitchRange` | |
| condition expression (note length) | Dorico `conditionString` | only Dorico |
| velocity factor / delta | Cubase `velocityFact`, Dorico `velocityFactor` | KITWARP's existing `velocityDelta` is additive; these are multiplicative — **store both, or store one and mark the conversion lossy** |
| length factor | Cubase `lengthFact`, Dorico `lengthFactor` | |
| transpose | Cubase/Dorico `transpose` | |
| articulation persistence: per-note vs held | Cubase `articulationtype` (Attribute/Direction), Dorico `switchOffActions` | |
| remote-select note | Cubase `PSlotThruTrigger.data1` | |
| stable numeric alias per articulation | Logic `ArticulationID`, Studio One `id`, Dorico `baseSwitchID` | **must be stable across re-exports** or existing project MIDI breaks |
| bank MSB / LSB / program | `.ins` `Patch[bank]`/`Key[bank,prog]`/`BankSelMethod`, `.midnam` `PatchBank`+`ProgramChange`+`ControlChange 0/32` | hardware modules and GM2 |
| "is a drum kit" flag | `.ins` `Drum[bank,prog]=1` | trivial |
| plug-in identity | Studio One `target.class`, Dorico `pluginNames`, `.midnam` `Manufacturer`/`Model` | |
| layout variant name | `.midnam` `CustomDeviceMode@Name` | e.g. "GM keymap" vs "full keymap" for one product |
| map inheritance / parent | Dorico `parentEntityID`, `.ins` `BasedOn=` | |
| provenance: author, version, description | Dorico `creator`/`version`/`description`, `.midnam` `Author` | |

### 4.2 Export-only decorations

These carry no information the pivot needs for *remapping*, but **the pivot must
nevertheless store or derive them**, because otherwise the export is lossy relative to
hand-made maps that users already have.

| Decoration | Targets that want it | Store or derive? |
|---|---|---|
| **notehead symbol** | Cubase `HeadSymbol` / `NoteheadSet`, Studio One `notehead`, Logic `Symbol`, MuseScore `<head>` | **Derive** from `(instrument, zone, technique)`. A single symbolic notehead per pivot symbol, plus per-target encoding tables. Each target uses a *different* encoding (int index vs `nhdX` vs `"Marcato"`), so a symbolic internal value is mandatory. |
| **display note / score pitch** | Cubase `DisplayNote`, Studio One `scorePitch` | **Derive** from `(instrument, instance)` via one notation table. Values cluster hard: `79` (hi-hat/cymbal line) accounts for 267 of 946 Studio One occurrences. |
| **score voice** | Cubase `Voice` | **Derive** from instrument family. |
| **note length** | Cubase `Length` (`200` in 4 352/4 352 slots) | **Constant.** Store as an optional per-entry override; emit `200`. |
| **quantize preset / index** | Cubase `Quantize` list + `QuantizeIndex` (`0` everywhere) | **Constant.** Emit a single default preset. |
| **colour** | Studio One `color` (ARGB), Cubase `PSoundSlot.color` (1–16), Reaper (colormap PNG — not exportable) | **Store** one canonical colour per instrument group in the pivot; convert per target. Reaper cannot receive it. |
| **row display order** | Cubase `Order` (non-identity in 8/34 files) | **Derive** from the pivot's canonical instrument ordering; allow a per-layout override. |
| **articulation symbol index** | Cubase `USlotVisuals.symbol` (37 distinct ints), Logic `Symbol` (name), Studio One `symbol` (`stac`/`circ`/`pizz`…) | **Store symbolically**, map per target. |
| **colour/symbol group id** | Cubase `USlotVisuals.group` 0–3 | Derive from axis identity; Cubase's 4-group cap is a *lossy* constraint to be aware of. |
| **mute flag** | Cubase `Mute` (50 slots in the corpus) | **Store** as optional boolean; used to hide unused rows. |
| **port / device name** | Cubase `OutputDevices` | Constant `"Default Device"`/`"Default Port"` unless multi-port. |

### 4.3 Lossless-export matrix

Rows = pivot field class, columns = target. ● carried, ○ carried but re-encoded, — lost.

| | `.drm` (11) | `.drm` (12+) | Reaper `.txt` | `.ins` | `.pitchlist` | `.midnam` | `.iom` | `.expressionmap` | Logic `.plist` | `.keyswitch` | `.doricolib` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| input note | ● | ● | ● | ● | ● | ● | ● | ○ gate | — | ○ | ○ gate |
| output note | ● | ● | — | — | — | — | ● | ● | ● | — | ● |
| display name | ● | ● | ● | ● | ● | ● | **—** | ● | ● | ● | ● |
| output channel | ● | ● | — | — | — | ● | — | ● | — | — | ● |
| output port | ● | ● | — | — | — | — | — | — | — | — | — |
| symbolic instrument | — | ● | — | — | — | ○ `NoteGroup` | — | — | — | — | — |
| symbolic technique | — | ● | — | — | ○ `technique` | — | — | ○ text | ○ `Symbol` | ○ `symbol` | ● `pt.*` set |
| axis / exclusion group | — | — | — | — | — | — | — | ○ 0–3 | — | — | ● named, unbounded |
| colour | — | — | — | — | ● ARGB | — | — | ○ 1–16 | — | ● ARGB | — |
| notehead | ○ int | ○ int | — | — | ○ `nhdX` | — | — | — | ○ name | — | — |
| display note | ● | ● | — | — | ● | — | — | — | — | — | — |
| score voice | ● | ● | — | — | — | — | — | — | — | — | — |
| note length | ● | ● | — | — | — | — | — | ○ factor | — | — | ○ factor |
| mute | ● | ● | — | — | ○ `flags` | — | — | — | — | — | ○ `enabled` |
| controller by number | — | — | ● | ● | — | ● | ● identity | ● | ● | — | ● |
| named controller values | — | — | — | — | — | ● | — | — | — | — | — |
| bank / program | — | — | — | ● | — | ● | — | — | — | — | — |
| velocity gate | — | — | — | — | — | — | — | ● | — | — | ● |
| velocity/length scaling | — | — | — | — | — | — | — | ● | — | — | ● |
| 1→N expansion | — | — | — | — | — | — | ○ (`Cnt`>1 permitted, unused) | ● | ● | — | ● |
| stable numeric alias | — | — | — | — | — | — | — | ○ slot ID | ● | ● | ● |
| map inheritance | — | — | — | ● `BasedOn` | — | ○ `ExtendingDeviceNames` | — | — | — | — | ● |
| plug-in identity | — | — | — | — | — | ● | — | — | — | ● | ● |

---

## 5. Implications for the KITWARP pivot vocabulary

1. **A symbolic, unbounded articulation identity is not a KITWARP invention — it is what
   the two most modern targets already require.** Dorico keys every slot on a *set* of
   `pt.*` technique IDs; Cubase 12+ keys every drum-map slot on
   `(InstrumentEntityID, TechniqueEntityID)`. If the pivot were a note number, neither
   field could be filled. This is independent corroboration of the decision already
   recorded in `docs/01-format-iom.md`.

2. **The "axes" design has a shipping precedent with a name: `mutualExclusionGroup`.**
   Dorico's `ptmg.user.pizzarco`, `ptmg.user.mute`, `ptmg.user.short_strings`,
   `ptmg.user.divisi` are exactly orthogonal, named, mutually-exclusive dimensions.
   Cubase's `USlotVisuals.group` is the same idea capped at 4. KITWARP should adopt the
   pattern *and* the ID-namespace convention (`<kind>.<namespace>.<slug>`), including a
   user/extension namespace (`pt.user.*`).

3. **Display names should be derivable, not stored per entry.** `fiddle`'s Dorico parser
   builds a name from the technique IDs (`{pt.staccato, pt.legato}` → "Staccato + Legato")
   when `<name>` is absent. That is the right default for KITWARP: axis values →
   generated name, with an optional override, and localisation as a separate table
   (Cubase ships `instrumentnames_ja.xml` for exactly this).

4. **`technique` and `symbol` are the same vocabulary in Studio One.** `.pitchlist`
   `technique="circ"` (open hi-hat) and `.keyswitch` `symbol="circ"` share codes. So a
   *drum-map* entry and an *articulation-map* entry can carry the same technique token.
   KITWARP should likewise use one technique vocabulary across both export classes rather
   than a drum vocabulary and an articulation vocabulary.

5. **A controller axis is required, not optional.** Four targets can name controllers
   (Reaper `CC<n>`, `.ins` `.Controller Names`, `.midnam` `Control`/`ValueNameList`,
   `.iom` `Cv2_*`), and three articulation formats bind controllers to *roles*
   (Dorico `volumeType`/`volumeType2`/`attackType`; Cubase `controller1num`). A drum
   layout's hi-hat pedal CC (CC4 vs CC1) is a pivot entity in its own right, with a role
   ("hi-hat position"), a number per layout, and optionally named values.

6. **Stable numeric aliases are a hard requirement, not a convenience.** Logic stamps
   `ArticulationID` onto every MIDI note event in the user's project; Studio One's `id`
   and Dorico's `baseSwitchID` play the same role. If KITWARP re-exports a set and the
   numbers move, existing project MIDI silently re-points. The pivot must therefore assign
   and *freeze* a numeric alias per (layout, pivot-symbol) at first publication.

7. **`instance` must survive into the notation fields.** `DisplayNote`/`scorePitch` and
   `Voice` are functions of *which* tom / *which* crash, not just of the instrument class.
   A bare ordinal is enough to place a note on a staff, but the structured `instance` the
   earlier dossiers argued for is what makes the placement stable when a kit gains a drum.

8. **Notehead must be stored symbolically.** Three targets encode it three
   incompatible ways (Cubase int index into a *pair* palette, Studio One `nhdX`-style
   codes, Logic symbol *names*). Only a symbolic internal value can be mapped to all
   three; an integer would bind the pivot to one host.

9. **Velocity semantics are multiplicative in the wild.** Cubase `velocityFact` and Dorico
   `velocityFactor` are factors; the reference model `marty-615/drum-remap` uses an
   additive `velocityDelta`. Store both, or store the factor and record that
   delta→factor conversion is not exact.

10. **`.iom` is the floor.** It carries integers only. Any export pipeline must degrade
    cleanly to "note number in, note number out, everything else discarded", and the UI
    should say so.

11. **Three targets are not reachable as files** (Ableton drum rack, Logic mapped
    instrument, a Pro Tools proprietary format — which does not exist). For Logic and Pro
    Tools, `.midnam` is the answer and covers both. For Ableton, an export would mean
    generating an `.adg` device group, which is a different kind of product feature.

---

## 6. Provenance

### 6.1 Files and repositories

| Fact set | Source | Licence |
|---|---|---|
| Cubase `.drm` schema, 19 maps | `github.com/jim/cubase_drum_maps_for_toontrack` → `drum_maps/*.drm`, `template.erb`, `create_drm_files.rb` | **no LICENSE file** |
| Cubase `.drm` 12+ variant, 8 maps | `github.com/janminor/cubase` → `drummaps/*.drm` | **no LICENSE file** |
| `.drm` emitter templates, `Order`/`HeadSymbol` examples | `github.com/thebruce/drumCartographer` → `templates/*.json`, `examples/ezd2-drummap-example.drm` | Apache-2.0 |
| `.drm` older schema (`MaxDiff`/`Tuplet`/`Move CC`) | `github.com/markheath/midifilemapper` → `MappingTests/TestFiles/EZD Map.drm` | no LICENSE file |
| Cubase `.drm` field list, `CubaseVoiceType`, ScoringEngine entity resolution, `.pitchlist` writer | `github.com/MinMax25/QBDrumMap` → `QBDrumMap/Class/Cubase/{MapItem.cs, CubaseScore.cs, CubaseVoiceType.cs}`, `QBDrumMap/Class/StudioOne/PitchList.cs` | README badge states MIT; no LICENSE file in tree |
| Cubase Drum Map Setup / drum sound list column semantics; "128 drum sounds, one per MIDI note number"; ".drm" extension | `archive.steinberg.help/cubase_pro_artist/v9/en/cubase_nuendo/topics/midi_editors/midi_editors_drum_editor_{drum_map_setup_dialog_r,drum_sound_list_r}.html` | Steinberg docs |
| Cubase head symbols are **pairs** | `archive.steinberg.help/.../score_editor_note_head_pairs_using_t.html` | Steinberg docs |
| MuseScore `.drm` extension collision | `github.com/musescore/MuseScore` → `share/templates/*.drm` | GPL-3.0 |
| Reaper `.txt` grammar, 39 drum/instrument maps | `github.com/DigitalInBlue/ReaperNoteNames` | LICENSE file = **CC0-1.0**; README claims CC BY 4.0 (discrepancy in the repo) |
| Reaper `.txt`, 1 236 further lines | `github.com/tsunetakaryu/MIDINoteNames-for-REAPER` | MIT |
| Reaper `CC<n>` line form (only public example) | `github.com/HarleyGaniere/Reaper-Track-Builder` → `MIDINoteNames/TC Electronic M300.txt` | GPL-3.0 |
| Reaper `.txt` + colormaps as separate artefacts | `github.com/shadowflower64/yarg-reaper-template` | Unlicense |
| Reaper `.txt` | `github.com/knpwrs/reaper-midi-note-names` | CC0 (README) |
| Reaper `.txt` generator, `~` blank convention | `github.com/JPplayground/MidiNoteNameGen` → `src/logic.py` | GPL-3.0 (header) |
| Reaper `<MIDINOTENAMES>` RPP grammar, channel `-1` = Omni | `github.com/ReaTeam/Doc` → `State Chunk Definitions`, lines 378–399 | ReaTeam/Doc repo |
| `SetTrackMIDINoteNameEx(proj, track, pitch, chan, name)`; "pitch 128 assigns name for CC0, pitch 129 for CC1" | `github.com/Ultraschall/ultraschall-lua-api-for-reaper` → `ultraschall_api/Documentation/Reaper_Api_Documentation.html` | Ultraschall API docs |
| Cakewalk `.ins` corpus (20 files, incl. 310 792-line `cakewalkmodified/`) | `github.com/darobyn/instrumentdefinitions` | **no LICENSE file**; `cakewalkmodified/*` explicitly "NOT BY ME … came with ancient Cakewalk" |
| Cakewalk `.ins` spec: sections, `Patch[#]`, `Key[#,%]`, `Drum[#,%]`, `BankSelMethod` 0–3, `(MSB<<7)+LSB`, `BasedOn`, `UseNotesAsControllers`, built-in `0..127`/`1..128` | `tse3.sourceforge.net/doc/InsFiles.html` | TSE3 project docs |
| Studio One `.pitchlist`, 4 drum maps | `github.com/chad-ramos/studio-one-drum-maps` | **no LICENSE file** |
| Studio One `.pitchlist` + `.keyswitch`, 164 + 46 files | `github.com/WaltRitscher/studio-one-user-presets` | CC0-1.0 |
| Studio One `.pitchlist` with `scorePitch`/`notehead`/`technique` | `github.com/tephrocactus/studio-one` → `drum-maps/*.pitchlist` | MIT |
| Studio One Sound Variation switching methods (Note on/off, Note on, Note off, Controller changes, Program Changes, Bank Changes); Sound Variation presets under *Studio One User Data / Keyswitches* | `support.spitfireaudio.com/en/articles/11816165-…`; VI-Control thread 151116 | vendor / forum |
| MMA `.midnam`, 471 files | `github.com/Ardour/ardour` → `share/patchfiles/*.midnam` | Ardour is GPL-2.0+; individual patchfiles carry per-file `<Author>` attributions |
| Pro Tools reads `.midnam`; install paths; "shows individual note names in piano roll editors" | `apps.avid.com/proToolsFirstHelp/version12.0/enu/Pro Tools First Help/MIDI1.EditMIDI.29.045.html` | Avid docs |
| Cubase `.expressionmap`, 76 files | `github.com/jaredthirsk/cubase-expression-maps` | Unlicense |
| `.expressionmap` with `articulationtype=0` (Attribute) | `github.com/Arkanthara/cubase-scripts` → `testexpression/Toms_attribute.expressionmap` | (via GitHub code search; repo not cloned) |
| Dorico `.doricolib`, 11 expression maps; name-derivation rule | `github.com/mhcoffin/fiddle` → `example-expression-maps/*.doricolib`, `Source/Server/ExpressionMapParser.cpp` | **no LICENSE file** |
| Logic articulation sets, 5 files | `github.com/nobodo/logic-pro-x-articulation-sets` | GPL-3.0 |
| Logic articulation sets, 44 files (BBCSO) | `github.com/simonlehmann/logic-pro-articulation-sets-for-bbc-symphony-orchestra` | MIT |
| Logic `ArticulationID` / `ID` semantics, `plist.tmpl` | `github.com/chrisself/switchboard` → `internal/logic/generate.go`, `internal/logic/plist.tmpl` | MIT |
| Ableton pad naming (Cmd/Ctrl-R), `.adg` = device group | `ableton.com/en/manual/instrument-drum-and-effect-racks/`; `github.com/manuz888/L2Move`; `github.com/Miserlou/ADGMaker` | vendor / repos |
| Logic mapped instrument is Environment-only | `support.apple.com/guide/logicpro/{mapped-instrument-window-lgcp1254dd59, lgcpc37fc656}/mac` | Apple docs |
| `.iom` container + payload | this repository: `docs/01-format-iom.md`, `data/legacy-iom/*.iom` (11 files), re-verified by direct byte/XML dump | project-internal |

### 6.2 Open points / UNVERIFIED

1. Cubase `HeadSymbol` integer → notehead-pair name table. Observed values `0,1,2,3,10,14`
   with the instrument correlations noted in §2.1.4; no authoritative enumeration found.
2. Cubase `USlotVisuals.symbol` integer → articulation-symbol name table (37 values
   observed; `73` is overwhelmingly the "text" placeholder).
3. Cubase `USlotVisuals.displaytype` / `articulationtype` enum labels. Inferred from
   text-emptiness correlation and one file named `*_attribute.expressionmap`; not from a
   Steinberg document.
4. Studio One `.pitchlist` `notehead` code expansion (`nhdX`, `nhDi`, `nhSl`, `nhCX`,
   `nhTr`) and `flags="show"` semantics.
5. Studio One `.keyswitch` `activation` token grammar beyond `note<n>`; `variationID`,
   `useGenerator` meanings; whether the newer Sound Variation editor writes a different
   file. No non-`note*` example exists in any public corpus found.
6. Logic `Switches[]` array element schema — empty in all 49 files found.
7. Reaper: whether the ReaScript doc's "channel > 0 assigns note name to all channels" is
   a typo for `< 0` / `-1` (the RPP grammar uses `-1` for Omni).
8. Dorico `playingTechniqueCombination/flags` (`0`/`1`) meaning.
9. Whether any host accepts `.iom` `Cnt > 1` on read.
