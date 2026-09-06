# Dossier 07 — Percussion naming beyond the drumkit

Scope: the vocabulary KITWARP needs for congas, bongos, timbales, cajon, shakers, scrapers,
metals, orchestral percussion and effects — the ~85 % of the percussion world that GM's 47
kit slots and drum-remap's single `cowbell` tag cannot name.

Sibling dossiers this one deliberately does **not** repeat:
- `03-midi-standards.md` §3 — the normalised GM1/GM2/GS/XG union (184 sounds). Its
  "Hand/Latin/World (72)" and "Orchestral (4)" tables are the *standards* column used below.
- `05-libraries-articulations.md` §2.7 — the Toontrack `.drm` percussion bucket inventory and
  NI Studio Drummer percussion. Extended here, not restated.
- `02-notation-oss.md` §2.4 — SMuFL pictogram names. Re-derived here **exhaustively and by
  range**, because that dossier used them for kit glyphs only.

---

## 1. Scope and method

### 1.1 Obtained (primary, full text)

| # | Source | How | Size / completeness |
|---|---|---|---|
| S1 | **SMuFL 1.4** metadata (`glyphnames.json`, `ranges.json`) | already cloned `w3c/smufl` @ `scratchpad/repos/smufl` | **exhaustive** — 278 `pict*` glyphs across 13 ranges |
| S2 | **MusicXML 4.0** `musicxml.xsd` percussion enumerations | already cloned `w3c/musicxml` @ `scratchpad/repos/musicxml` | **exhaustive** — 100 instrument values + 47 beater/stick values |
| S3 | **MusicXML Standard Sounds** percussion IDs | `scratchpad/research/data/musicxml_sounds_percussion.txt` (from dossier 02/03 run) | **exhaustive** — 405 IDs in 6 families |
| S4 | **Sibelius SoundWorld** unpitched sound IDs | `scratchpad/research/data/sibelius_unpitched_soundids.txt` | **exhaustive corpus** — 7 062 IDs; 627 after stripping vendor-library suffixes |
| S5 | **Sibelius Sound Set Editor User Guide** (Avid) | `https://www.sibelius.com/download/sse/Sound%20Set%20Editor%20User%20Guide.pdf` → `scratchpad/pdf/SibeliusSSE.txt` | full — this is Sibelius's "percussion map" format |
| S6 | **Toontrack EZX Latin Percussion** Cubase drum map | already cloned repo `jim_cubase_drum_maps_for_toontrack/drum_maps/EZX Latin Percussion.drm` | **exhaustive** — all 128 note names |
| S7 | **NI Discovery Series: Cuba** manual | `https://www.native-instruments.com/fileadmin/ni_media/downloads/manuals/spotlight_collection/Cuba_Manual_English_29_06_2021.pdf` | full; the "List of Percussion Symbols" appendix is an explicit cross-instrument articulation table |
| S8 | **VSL Vienna Instruments Percussion — Mapping Documentation v1.1** | `https://odl.vsl.co.at/cms-vsl/legacy-manuals/collections/vi_percussion_manual_v1.1.pdf` → `scratchpad/pdf/VSL_perc.txt` (8 089 lines) | full; per-patch articulation + keymap for ~70 orchestral/world percussion instruments |
| S9 | **Spitfire Percussion** user manual | `https://d1t3zg51rvnesz.cloudfront.net/p/files/product-manuals/1553/1529333485/SpitfirePercussion_UserManual.pdf` | full; instrument/preset list is exhaustive, per-instrument technique list is **not** in the manual (it is runtime UI) |
| S10 | **Roland HandSonic HPD-20 Owner's Manual** | `https://static.roland.com/assets/media/pdf/HPD-20_OM.pdf` | full manual; **contains kit list, not the instrument list** |
| S11 | **Roland SPD-SX / Octapad SPD-30 Owner's Manuals** | `https://static.roland.com/assets/media/pdf/SPD-SX_OM.pdf`, `.../SPD-30_OM.pdf` | full manuals; **neither contains a wave/instrument list** |
| S12 | **Dorico Percussion Maps dialog** reference | `https://archive.steinberg.help/dorico_se/v3/en/dorico/topics/play_mode/play_mode_percussion_maps_dialog_r.html` | field-by-field description obtained |

### 1.2 NOT obtained, and why

| Wanted | Outcome |
|---|---|
| **Dorico's enumerated list of playing/playback techniques** | **NOT OBTAINED.** Dorico ships them inside the application (`.doricolib` factory libraries). GitHub code search for `extension:doricolib` returns 16 files, all *expression* maps for pitched instruments (repos `mhcoffin/fiddle`, `taylorbrook/O-Audio-VST-Development`, `manolo/vst-plectro`); none is a percussion map. Steinberg's help pages describe the dialog but never enumerate the technique list. Third-party count only: Scoring Notes' Dorico 1.2 review says "more than 200 techniques listed" across all families. Treat the Dorico technique list as **UNVERIFIED / unobtainable remotely**. |
| **Roland HPD-20 / SPD-SX / SPD-30 instrument (wave) lists** | **NOT OBTAINED.** Roland publishes these as separate "Data List" PDFs; every filename probed under `static.roland.com/assets/media/pdf/` returned 403 (`HPD-20_InstList`, `HPD-20_DataList`, `HPD-20_dat`, `SPD-30_IL`, `SPD-SX_DataList`, …) while `*_OM.pdf` returned 200 — i.e. the OM exists at that path and the data lists do not. `roland.com` support pages render the manual list via JS. `vdrums.com` forum returns 403 to WebFetch. Only fragments recovered (§2.10). |
| **VSL Synchron Percussion I/II patch lists** | product pages give instrument groups only; `vsl.co.at/en/Synchron_Percussion_II/Instrumentation` returns 502. The **legacy Vienna Instruments** documentation (S8) was obtained instead and is far more detailed. |
| **Spitfire per-instrument technique names** | The Kickstart engine lists techniques at runtime; the manual has only the preset/instrument list. |
| **Yamaha DTX-MULTI 12 voice list** | official PDF path not found; mirrors (`usermanual.wiki`, `manualzz`, `scribd`) all 403. |

### 1.3 Working files written by this dossier

```
scratchpad/research/data/smufl_pictograms.txt            278 SMuFL pict* glyphs, by range
scratchpad/research/data/sibelius_perc_articulations.txt per-instrument modifier tokens (Sibelius)
scratchpad/pdf/VSL_perc.txt                              VSL percussion mapping doc, text
scratchpad/pdf/NI_Cuba.txt  SibeliusSSE.txt  SpitfirePerc.txt  HPD-20_OM.txt  SPD-SX_OM.txt  SPD-30_OM.txt
```

---

## 2. Extracted facts

### 2.1 SMuFL 1.4 — percussion pictograms, exhaustive by range

278 glyphs whose name begins `pict`. **The structural fact that matters more than the names:
SMuFL splits them into three orthogonal kinds, in different code ranges.**

| Kind | Ranges | Count |
|---|---|---|
| **instrument** pictograms | drums, woodenStruckOrScraped, shakersOrRattles, metallicStruck, bells, chimes, cymbals, gongs, tunedMalletPercussion, whistlesAndAerophones, miscellaneousPercussionInstrument | 119 |
| **playing-technique** pictograms | `percussionPlayingTechniquePictograms` | 31 |
| **beater / implement** pictograms | `beatersPictograms` | 128 (53 beater types × up to 4 stem directions) |

That is a three-axis model — instrument / technique / implement — asserted by the notation
standard itself, independently of any DAW.

#### 2.1.1 Instrument pictograms (119)

`drumsPictograms` (21) — Timpani, Snare drum, Snare drum snares off, Military snare drum,
Bass drum, Bass drum on side, Tenor drum, Tom-tom, Chinese tom-tom, Japanese tom-tom,
Indo-American tom tom, Tambourine, Timbales, Bongos, Conga, Log drum, Slit drum, Brake drum,
Goblet drum (djembe, dumbek), Indian tabla, Cuica.

`woodenStruckOrScrapedPercussionPictograms` (13) — Wood block, Temple blocks, Claves, Guiro,
Ratchet, Football rattle, Whip, Board clapper, Castanets, Castanets with handle,
Quijada (jawbone), Bamboo scraper, Reco-reco.

`shakersOrRattlesPictograms` (9) — Flexatone, Maraca, Maracas, Cabasa, Thundersheet,
Vibraslap, Sistrum, Rainstick, Chain rattle.

`metallicStruckPercussionPictograms` (2) — Triangle, Anvil.

`bellsPictograms` (11) — Sleigh bell, Cow bell, Almglocken, Bell plate, Bell, Handbell,
Cencerro, Agogo, Shell bells, Jingle bells, Bell tree.

`chimesPictograms` (9) — Tubular bells, Wind chimes (glass), Chimes, Bamboo tube chimes,
Shell chimes, Glass tube chimes, Glass plate chimes, Metal tube chimes, Metal plate chimes.

`cymbalsPictograms` (11) — Crash cymbals, Suspended cymbal, Hi-hat, Hi-hat cymbals on stand,
Sizzle cymbal, Vietnamese hat cymbal, Chinese cymbal, Finger cymbals, Cymbal tongs,
**Edge of cymbal**, **Bell of cymbal**  ← note: the last two are *zones*, mis-filed as instruments.

`gongsPictograms` (5) — Tam-tam, Tam-tam with beater (Smith Brindle), Gong,
Gong with button (nipple), Slide brush on gong.

`tunedMalletPercussionPictograms` (19) — Glockenspiel, Xylophone, Tenor xylophone,
Bass xylophone, Trough xylophone, Trough tenor xylophone, Marimba, Vibraphone,
Metallophone (vibraphone motor off), Empty trapezoid, Glockenspiel (Smith Brindle),
Xylophone (Smith Brindle), Marimba (Smith Brindle), Vibraphone (Smith Brindle), Crotales,
Steel drums, Celesta, Lithophone, Tubaphone.

`whistlesAndAerophonesPictograms` (11) — Slide whistle, Bird whistle, Police whistle, Siren,
Wind machine, Car horn, Klaxon horn, Duck call, Wind whistle (or mouth siren), Megaphone,
Lotus flute.

`miscellaneousPercussionInstrumentPictograms` (8) — Pistol shot, Cannon, Sandpaper blocks,
Lion's roar, Glass harp, Glass harmonica, Musical saw, Jaw harp.

#### 2.1.2 Playing-technique pictograms (31) — exhaustive

| glyph | description | axis it really belongs to |
|---|---|---|
| `pictStickShot` | Stick shot | technique |
| `pictScrapeCenterToEdge` | Scrape from center to edge | technique + direction |
| `pictScrapeEdgeToCenter` | Scrape from edge to center | technique + direction |
| `pictScrapeAroundRim` | Scrape around rim (counter-clockwise) | technique + direction |
| `pictScrapeAroundRimClockwise` | Scrape around rim (clockwise) | technique + direction |
| `pictOnRim` | On rim | **zone** |
| `pictOpenRimShot` | Closed / rim shot | technique |
| `pictRimShotOnStem` | Rim shot for stem | technique (stem-attached form) |
| `pictHalfOpen1` / `pictHalfOpen2` | Half-open / Half-open 2 (Weinberg) | **openness scalar** |
| `pictOpen` | Open | openness scalar |
| `pictDamp1` … `pictDamp4` | Damp / Damp 2 / Damp 3 / Damp 4 | **damping scalar** (4 notational variants, one concept) |
| `pictCenter1` / `pictCenter2` / `pictCenter3` | Center (Weinberg / Ghent / Caltabiano) | **zone** (3 notational variants, one concept) |
| `pictRim1` / `pictRim2` / `pictRim3` | Rim or edge (Weinberg / Ghent / Caltabiano) | zone |
| `pictNormalPosition` | Normal position (Caltabiano) | zone |
| `pictChokeCymbal` | Choke (Weinberg) | technique |
| `pictRightHandSquare` | "Left hand (Agostini)" | **limb** (note the name/description mismatch in SMuFL itself) |
| `pictLeftHandCircle` | "Right hand (Agostini)" | limb |
| `pictSwishStem` | Combining swish for stem | technique |
| `pictTurnRightStem` / `pictTurnLeftStem` / `pictTurnRightLeftStem` | Combining turn right / left / left-or-right for stem | technique + direction |
| `pictCrushStem` | Combining crush for stem | technique |
| `pictDeadNoteStem` | Combining X for stem (dead note) | technique |

**Finding:** 31 glyphs collapse to **~12 distinct concepts** once the Weinberg/Ghent/
Caltabiano/Agostini notational variants are merged. Damp×4 and Center×3 and Rim×3 are
cosmetic; open / half-open / damp is an **ordered openness scalar**; center / normal / rim is
a **zone axis**; left/right hand is a **limb axis**.

#### 2.1.3 Beater pictograms — 53 distinct beater types (128 glyphs = type × direction)

Soft/Medium/Hard/Wood **xylophone stick**; Soft/Hard **glockenspiel stick**;
Soft/Medium/Hard/Wood **timpani stick**; Soft/Medium/Hard/Metal/Double **bass drum stick**;
Soft/Medium/Hard **yarn beater**; **Superball beater**, **Superball**;
**Wound beater hard core**, **Wound beater soft core**; Soft/Medium/Hard **gum beater**;
**Metal beater**; Wooden/Plastic/Metal **hammer**; **Snare sticks**; **Jazz sticks**;
**Triangle beater**, **Triangle beater plain**; **Wire brushes**; **Brass mallets**;
**Soft xylophone beaters**; **Spoon-shaped wooden mallet**; **Guiro scraper**; **Bow**;
**Chime hammer**; **Hammer**; **Knitting needle**; **Hand**; **Finger**; **Fist**;
**Fingernails**; **Coins**; **Drum stick**; plus two combining modifiers
("parentheses for round beaters (padded)", "dashed circle for round beaters (plated)") and
"Box for percussion beater".

The direction suffix (up/down/left/right) is **stem orientation, not semantics** — cosmetic.

**Finding:** the beater axis is *large* (53 values, factorable as `material × hardness ×
form`) and it is *orthogonal to instrument* — the same `Soft yarn beater` glyph is used on
marimba, tam-tam and suspended cymbal.

### 2.2 MusicXML 4.0 `<percussion>` — the normative notation vocabulary (exhaustive)

Extracted from `scratchpad/repos/musicxml/schema/musicxml.xsd`. Six *instrument* enumerations
and four *modifier* enumerations. This is the only source in the whole research programme that
is both **normative** and **enumerable** for the beater/zone axes.

| simpleType | n | values |
|---|---|---|
| `membrane-value` | 17 | bass drum, bass drum on side, bongos, Chinese tomtom, conga drum, cuica, goblet drum, Indo-American tomtom, Japanese tomtom, military drum, snare drum, snare drum snares off, tabla, tambourine, tenor drum, timbales, tomtom |
| `metal-value` | 32 | agogo, almglocken, bell, bell plate, bell tree, brake drum, cencerro, chain rattle, Chinese cymbal, cowbell, crash cymbals, crotale, cymbal tongs, domed gong, finger cymbals, flexatone, gong, hi-hat, high-hat cymbals, handbell, jaw harp, jingle bells, musical saw, shell bells, sistrum, sizzle cymbal, sleigh bells, suspended cymbal, tam tam, tam tam with beater, triangle, Vietnamese hat |
| `wood-value` | 21 | bamboo scraper, board clapper, cabasa, castanets, castanets with handle, claves, football rattle, guiro, log drum, maraca, maracas, quijada, rainstick, ratchet, reco-reco, sandpaper blocks, slit drum, temple block, vibraslap, whip, wood block |
| `pitched-value` | 11 | celesta, chimes, glockenspiel, lithophone, mallet, marimba, steel drums, tubaphone, tubular chimes, vibraphone, xylophone |
| `glass-value` | 3 | glass harmonica, glass harp, wind chimes |
| `effect-value` | 16 | anvil, auto horn, bird whistle, cannon, duck call, gun shot, klaxon horn, lions roar, lotus flute, megaphone, police whistle, siren, slide whistle, thunder sheet, wind machine, wind whistle |
| **`stick-type`** | 10 | bass drum, double bass drum, glockenspiel, gum, hammer, superball, timpani, wound, xylophone, yarn |
| **`stick-material`** | 5 | soft, medium, hard, shaded, x |
| **`stick-location`** | 4 | **center, rim, cymbal bell, cymbal edge** |
| **`beater-value`** | 20 | bow, chime hammer, coin, drum stick, finger, fingernail, fist, guiro scraper, hammer, hand, jazz stick, knitting needle, metal hammer, slide brush on gong, snare stick, spoon mallet, superball, triangle beater, triangle beater plain, wire brush |
| `tip-direction` | 8 | up, down, left, right, northwest, northeast, southeast, southwest (cosmetic — stem/tip orientation) |

**Findings.**
1. MusicXML models the implement as **`stick-type` × `stick-material`** — a factored
   (form × hardness) pair, *not* one flat list. SMuFL flattens the same space to 53 glyph
   names. KITWARP should factor, like MusicXML, and derive display names.
2. `stick-location` is a **first-class zone axis with exactly 4 normative values**, and two of
   them (`cymbal bell`, `cymbal edge`) are cymbal-specific — evidence that zone values are
   *instrument-scoped*, not global.
3. There is **no articulation/technique enumeration at all** in MusicXML's percussion element:
   technique is carried by `<notehead>`, `<articulations>` and `<other-technical>`. So
   MusicXML has instrument + implement + zone, and **no technique axis** — a real gap that
   Dorico and Sibelius both had to fill.

### 2.3 MusicXML Standard Sounds — percussion instrument IDs (405)

`drum.*` 149, `metal.*` 80, `pitched-percussion.*` 64, `effect.*` 63, `wood.*` 27,
`rattle.*` 22. Purely an **instrument identity** namespace: dotted, hierarchical, and with
**zero articulation content** (`drum.bata.iya` is an instrument, `drum.frame-drum.arabian` is
an instrument). Examples of the taxonomic depth: `drum.bata` → `.itotele`, `.iya`,
`.okonkolo`; `drum.group.chinese/.ewe/.indian/.multi-bass`; `metal.cymbal.*` has 22 members
including `.ceng-ceng`, `.kesi`, `.tebyoshi`, `.tingsha`; `metal.gong.*` has 15 including
`.kempul`, `.ketuk`, `.kkwenggwari`.

**Finding:** Standard Sounds is the right *shape* for KITWARP's instrument axis (dotted,
hierarchical, generalisation by truncation) and the wrong shape for the whole pivot, because it
cannot say "open" or "slap".

### 2.4 Sibelius — SoundWorld sound IDs and the sound-set "drum map"

#### 2.4.1 The format (S5, Sound Set Editor User Guide)

Sibelius's equivalent of a percussion map is a **`DrumMap`** inside a sound set XML:

```xml
<DrumMapList>
  <DrumMap Name="General MIDI">
    <DrumSound Pitch="27" SoundID="unpitched.exotic.high q"  Name="High Q" />
    <DrumSound Pitch="28" SoundID="unpitched.exotic.slap"    Name="Slap"   />
    ...
  </DrumMap>
</DrumMapList>
```

- `DrumSound` attributes: **Pitch** (MIDI note or Sibelius pitch name, middle C = C4),
  **SoundID** (mandatory — "the complete sound ID that best describes this sound"),
  **Name** (human-readable, "e.g. from the device manufacturer's documentation").
- A `DrumSound` may carry `StartSwitch` / `EndSwitch` children (keyswitch / MIDI controller)
  and an `IsMultipleNoteSample` flag (true for sampled rolls/trills/tremolos, which suppresses
  Sibelius's own roll synthesis).
- A `Patch` element carries **either** `SoundID` **or** `DrumMap` — "these two elements are
  mutually exclusive".

**The mechanism KITWARP should copy — `SoundIDChange`.** Sibelius switch definitions do not
name whole sound IDs; they name **relative changes** to the current sound ID:

> "`SoundIDChange`, representing the sound ID change (in the form e.g. `+pizzicato` or
> `-mute`, or the special value `[reset]`, which removes all relative sound ID changes)"

and the guide explicitly recommends *multiple independent* relative changes over one compound
token: "You can define multiple relative sound ID changes in the same switch, e.g.
`+pizzicato +mute` … This is normally preferable to specifying `+pizzicato.mute`" — except
where the compound is genuinely one concept, in which case it must be atomic:
"if you want to switch to very specific relative sound IDs, e.g. `+mute.harmon`,
`+mute.straight`, `+trill.half`, `+trill.whole`, then you should specify them as a single,
multi-element sound ID change."

Fallback is likewise built in: the guide instructs authors to invent new IDs "by basing them on
the closest existing sound ID, e.g. by adding one or more elements to the end. This ensures
that Sibelius's SoundWorld system will be able to properly substitute your chosen sound ID for
the **closest available one**".

**This is a shipping, 15-year-old precedent for exactly the KITWARP pivot design: a
hierarchical symbolic ID, additive/subtractive facet modifiers, and prefix-truncation
fallback.** It is also a precedent for the axis question: Sibelius stores facets as *path
segments*, and its own editor guide warns that compounding them into one token is usually wrong.

#### 2.4.2 The corpus (S4)

7 062 unpitched sound IDs. Grammar in practice:

```
unpitched . <family> . <size/register> . <instrument> . <modifier>* . <library-tag>*
family      ∈ {drum, metal, wood, rattle, exotic, wind, tom-tom}
size        ∈ {very low, low, medium-low, medium, medium-high, high}   (a 6-step register scale)
```

Stripping the vendor tags (`vi-one`, `eop`, `midi`, `kit-*`, and ~40 sample-set names such as
`grover`, `lefima`, `vaughncraft`, `clemente`, `columbia`, `hot rods`, `tucson`) leaves a
**627-entry core tree**.

Per-instrument modifier tokens actually attested (file
`scratchpad/research/data/sibelius_perc_articulations.txt`; tokens ordered by frequency;
`ids=` is the number of sound IDs containing that instrument token):

| instrument | ids | attested modifier tokens |
|---|---|---|
| conga | 181 | slap, muffled, mute, open, palm, pressed, closed, bass tone, heel, tip, fingers, finger, hands, knuckles, flam, roll, pop, shell, bass, *(plus style tokens: marcha, qua qua, samba, songo, calypso, owl cry)* |
| bongo | 91 | mute, muffled, slap, bass tone, palm, pop, two hands |
| timbale | 30 | rim, flam, stick, shot, mute |
| cajon | 46 | flam, left, right, damp, soft, hand, mute, hard, slap, stick, brush, pattern |
| tambourine | 175 | roll, stroke, frame, thumb, shake, shell, fist, flam, crescendo, head, pop, hit, closed, short, left, right, crescendo diminuendo, stick |
| guiro / guira | 84 / 7 | up down, long, short, fast, stroke |
| cuica | 52 | mute, open |
| surdo | 2 | muffled |
| djembe | 28 | slap, open, flam, bass tone, closed, edge, mute, palm, pressed, roll, shell, muffled |
| frame drum (incl. riq, ganjira, bendir) | 138 | damp, mute, short, hard, roll, shake, edge, double, slap, crescendo, lower, mallet, long, hand, flam, muffled, fast |
| udu | 26 | bend, high, low, neck, shell, stroke, long, short, palm, mallet |
| tabla | 20 | dayan, bayan, mute, damp, soft, up, bend, edge, tip |
| shaker | 214 | egg, short, long, metal, steel, wood, clay, motion, down, up, tremolo, high, low, stroke, left, right, single, fast, slow, medium |
| cabasa | 24 | long, short, high, slap, tap, itchy |
| maraca | 64 | down, up, roll, long, short, fast, slow, shake |
| triangle | 81 | closed, open, mute, damp, roll, choke, flam, long, short, triple, hard, soft, portato, crescendo, diminuendo, aerate |
| castanets | 19 | roll, flam, short, left, right |
| claves | 33 | flam, slowing *(+ material: grenadilla; style: candombe)* |
| woodblock | 88 | roll, soft, hard, flam, triple, diminuendo |
| agogo | 63 | soft, closed, mute, roll, short |
| cowbell | 102 | single, top, side, damp, mute, bongo, timbale, cha-cha, salsa, funky |
| whistle | 72 | police, samba, long, short, flutter, slide, high, low, medium, up, down |
| vibraslap | 24 | *(no modifiers in core tree)* |
| bata | 32 | iya, itotele, okonkolo, slap, flam, muffled, pressed, mute, open, fingers, left, right |
| ratchet | 19 | long, short |
| sleigh bells | 23 | roll, shake, tap |
| mark tree | 10 | gliss, up, down, fast, slow, tinkle |
| caxixi | 8 | down, up |
| shekere | 13 | high, low, down, up, medium, short |
| finger cymbals | 6 | bell, edge, choke, rub, zing |
| log drum | 25 | mute, damp, roll |
| ipu drum | 27 | three strikes, four strikes, triple, hand, roll, mute, short |
| berimbau | 15 | with caxixi, damp, gourd fx, mute, roll |
| talking drum | 20 | up, down, mute, flam |
| anvil | 12 | flam, damp, scrape |
| jawbone | 4 | fingers, palm, slap |
| flexatone | 5 | bend, high, low, short |
| bell tree | 19 | up, down, slow, tremolo |
| gong / tam-tam | 80 | roll, nipple, scrape, tip, stick, choke, bell, clang, crescendo, long, short, soft, wind, saw, opera, chinese *(+ sizes 6/12/14/24/30 inch; makers wuhan, paiste, zildjian; beater yarn, brush, metal, rattle)* |
| concert snare drum | 659 | snares on, snares off, side stick, rim, rim shot, stick shot, drag, flam, ruff, roll, crush, open, cut off, brush, left, right, ensemble, marching |
| concert bass drum | 118 | concert, rim, roll, crush, damp, damped, muffled, mute, hit, accent, crescendo, diminuendo, flam, short, long, left, right, ensemble, lower, soft, hard, felt, rute, large, small, lite |
| tenor drum | 98 | ensemble, roll, buzz, rim, rim shot, crush, dry, flam, short, triple, stick on stick, stick click, shell, crescendo, diminuendo, left, right, spock |

*(Caveat: a handful of tokens in the raw corpus are sample-set names that survived filtering —
`coco rico` (guiro), `big head`/`monster`/`aluminum`/`copper` (tambourine), `ap1`/`ap2`/`prl`/
`gladstone`/`maple` (snare). They are **not** articulations.)*

**Findings from Sibelius.**
- The **left/right hand** distinction is pervasive (conga, cajon, castanets, bass drum, snare,
  tenor drum, tambourine, shaker) — a **limb axis**, not an instance axis.
- **`stroke`** and the **`up`/`down`** pair appear on every shaken and scraped instrument
  (shaker, maraca, cabasa, caxixi, guiro, mark tree, bell tree, talking drum) — the
  *direction of a reciprocating gesture* is a first-class articulation for these families and
  has no drum-kit analogue.
- **`crescendo` / `diminuendo` / `crescendo diminuendo` / `tremolo` / `roll`** are single
  *events* here, not dynamics — a sampled swell is a distinct articulation.
- Register (`very low … high`) is a **separate path segment from the instrument**: Sibelius
  models conga size as an axis, not as three instruments. GM models the same thing as three
  instrument names (`Low Conga`, `Mute Hi Conga`, `Open Hi Conga`).

### 2.5 Dorico — percussion maps

**Structure (verified, S12).** A percussion map (`.doricolib`) has map-level data
**Name**, **ID**, **Version**, and **"Map defines sounds for"** ∈ {Multiple Instruments,
Single Instrument}. Its table — the *Drum Kit Note Map* — has exactly these columns:

| column | meaning |
|---|---|
| **MIDI Note** | the note that triggers the sound |
| **Name** | "the displayed name for the specific combination of instrument and playback playing technique" |
| **Instrument** | selected from Dorico's instrument list |
| **Key Switch** | optional MIDI note emitted to select the sound |
| **Playing Techniques** | one or more **playback** playing techniques applied to the instrument |

Separately, each unpitched instrument has a **Percussion Instrument Playing Techniques**
dialog holding (a) a list of playing-technique-specific **noteheads** with notehead set and
**staff position** (on line / above line / below line), and (b) a **"Playback of Articulations
and Tremolos"** override list — i.e. `technique × articulation` and `technique × tremolo`
combinations can be redirected to a different sound.

**The structural findings, which are the point of this section:**

1. Dorico's percussion identity is exactly **(instrument, playback playing technique)** — the
   *Name* field is literally defined as "the specific combination of instrument and playback
   playing technique". A MIDI note is an *output* of that pair, never the identity. This is
   independent corroboration of KITWARP's central decision.
2. Dorico splits **playing technique** (what is written) from **playback technique** (what is
   sounded), and the map maps the latter. KITWARP's pivot is the *playback* side.
3. Dorico allows **multiple techniques per map row** (`Playing Techniques`, plural) — i.e. the
   identity is a *set* of facets, not a single opaque tag. Same conclusion as Sibelius's
   `+pizzicato +mute`.
4. **Notehead and staff position are stored on the instrument's technique list, not in the
   map** — rendering is separated from identity, the same lesson dossier 02 drew from LilyPond.
5. Articulations and single-note tremolos are **modifiers that can override the technique's
   sound**, not techniques themselves. A pivot that folds `flam`, `roll` and `accent` into the
   same enum as `open`/`slap` is making a category error Dorico avoids.

**NOT OBTAINED:** the enumerated technique list. Only these percussion-relevant technique
names are attested in Steinberg/third-party text: *Natural*, *Side stick*, *rim*, *scrape*,
*open* (`o`), *closed* (`+`), *snares on* / *snares off*, *rim shot*, *roll*, *cross-stick*,
*ghost notes*, plus articulations *staccato* / *tenuto* / *accent* used as overrides.
Scoring Notes reports "more than 200 techniques listed" across all instrument families.
Treat any longer Dorico list as **UNVERIFIED**.

### 2.6 Toontrack EZX Latin Percussion — full 128-note map (S6)

Exhaustive, because it is a Cubase drum map file. 24 instrument buckets. Verbatim bracket
names, articulations grouped:

| bucket | articulations (verbatim) |
|---|---|
| `[Conga 1]` | Left/Right Open, Left/Right Muted, Left/Right BassTone, Left/Right Open Slap, Left/Right Closed Slap, Left/Right Heel, Crescendo, Slap Crescendo, Flams, Slap Flams, FX |
| `[Conga 2]` | Left/Right Open, Left/Right Muted, Left/Right BassTone, Crescendo, Flams, FX |
| `[Bongo 1]` | Left/Right Open, Left/Right Heel, Crescendo, Flams |
| `[Bongo 2]` | Left/Right Open, Crescendo, Flams |
| `[Timbale 1]` | Left/Right OpenTone, RimShot, SideStrokes, Flams, Ruff |
| `[Timbale 2]` | Left/Right OpenTone, RimShot, SideStrokes, Flams |
| `[Cajon]` | Left/Right BassTone, Left/Right GhostStroke, Left/Right Sidestick, Left/Right Slap Norm, Left/Right Slap Mid, Left/Right Brush Hit, Left/Right Brushed, Crescendo, Flams |
| `[Udu]` | OpenTone High, OpenTone Low, Open Slap, Muted Slap, Left/Right Ghostnote, Crescendo, Slap Crescendo, Flams |
| `[Tambourine]` | Open Hit, Muted Hit, On Beat, Off Beat, Crescendo |
| `[Shaker 1]` / `[Shaker 2]` | On Beat, Off Beat, Shakings |
| `[Maracas]` | On Beat, Off Beat, Shakings |
| `[Caxixi]` | Beat, On Beat, Off Beat, FX |
| `[Shekere]` | Beat, On Beat, Off Beat, Shakings |
| `[Afuche]` | Beat |
| `[Guiro]` | Short, Long |
| `[Triangle]` | Open, Muted |
| `[Cowbell]` | Hit |
| `[Woodblocks]` | Block 1, Block 2, Block 3 |
| `[Vibraslap]` | Stroke |
| `[Bells]` | Stroke, Crescendo |
| `[Chimes]` | Stroke |
| `[Crickets]` / `[Waterfall]` | Stroke, Crescendo |
| `[Cymbal 1]` / `[Cymbal 2]` | Crash, Crescendo |
| `[Splash]` | Hit |

Notes: notes 111–118 duplicate `[Conga 2]` 102–109 (an octave-shifted alias block); one entry
is spelled `[Cymbal 1] *Crescendo` with a stray asterisk. Both are real artefacts of the file.

**New vocabulary this map contributes over dossier 05's `.drm` scan:** `Slap Norm` vs
`Slap Mid` (cajon strike height), `Brush Hit` vs `Brushed` (attack vs sustained sweep),
`Sidestick` on a **cajon**, `OpenTone` as a distinct token from `Open`, `Ruff`.

### 2.7 NI Discovery Series: Cuba — the cross-instrument articulation table (S7)

The manual's Appendix "List of Percussion Symbols" is the single most explicit statement
anywhere in the corpus that **percussion articulations are the same small set applied across
different instruments**. Verbatim (symbol → meaning → per-instrument reading):

| symbol role | reading per instrument |
|---|---|
| "The most basic or neutral stroke" | **Open** (Conga, Bongos, Cajón) · **Top** (Bells) · **Normal Hit** (Clave) · **Long Stroke** (Guiro) · **Low Woodblock** |
| "A louder or higher sound compared to the basic stroke" | **Slap** (Congas, Bongos) · **Center** (Bells) · **Cascara** (Timbales) · **Accent** (Maracas, Shekere) · **High Woodblock** |
| "Bass or special stroke" | **Bass** (Congas, Cajón, Shekere) · **Rimshot** (High Timbale), **Cross Stick** (Low Timbale) · **Rotation** (Maracas) · **Flam** (Woodblock) |
| "Indicates direction of movement or part of the hand" | **Heel** (Congas) · **Up** (Maracas) · **Down** (Guiro) · **Front** (Shekere) |
| "Indicates direction of movement or part of the hand" | **Tip** (Congas, Bongos) · **Down** (Maracas) · **Guiro (Up)** · **Back** (Shekere) |
| "Soft sound" | **Muted** (Timbales) · **Tip** (Cajón) · **Up Fast** (Guiro) |
| "Roll, usually with the basic sound" | (exception: the *hembra* track on the timbales produces a **cascara roll**) |

Instrument naming in the same manual: bongos are **macho** (larger) / **hembra** (smaller);
timbales are **macho / hembra**; the sets are *Conga Set* (three congas, one virtual player) vs
*Conga Single* ("a single conga with more articulations than the conga set"); *Clave Block*
is distinguished from *Claves*.

**Findings.**
- **`heel` and `tip` are a limb-part pair, not two unrelated articulations**, and NI groups them
  with `up`/`down` and `front`/`back` under one heading "direction of movement or part of the
  hand". That is a **gesture-phase axis** shared by hand drums (heel/toe) and shakers
  (up/down) and shekere (front/back).
- **`cascara` is a timbale articulation** (playing the shell), and NI ranks it in the same slot
  as `slap` — i.e. it is a zone/technique, not a groove name. It did **not** appear anywhere in
  the Sibelius corpus (`grep -i cascara` → 0 hits) nor in GM/GS/XG. It is library-only.
- **`Rimshot` on the high timbale vs `Cross Stick` on the low timbale** — the same notated
  symbol maps to *different techniques on different instances of the same instrument*. Any
  pivot that treats `timbale-hi` and `timbale-lo` as instances of one entry must still allow
  their articulation sets to differ.

### 2.8 VSL Vienna Instruments Percussion (S8) — orchestral articulation naming

#### 2.8.1 VSL's own axis vocabulary (from the manual's Abbreviations table, verbatim)

**Implement / mallet axis** — `SO+` very soft, `SO` soft, `SO-med` medium soft, `MD` medium,
`MHA` medium hard, `HA` hard, `HA-super` extra hard, `WO` wood, `FE` felt, `YA`/`yarn`
yarn-wound, `PL` plastic (`sPL` soft, `mPL` medium, `hPL` hard), `ME` metal, `bME` large metal,
`CLU` cluster mallet, `Rubber`, `Rod` metal rod, `Rub-stick` rubbing stick, `Stick` wood
stick/drumsticks, `Tri` triangle beater, `Tmp` timpani mallet, `FI` fingers.
→ i.e. **hardness is a 7-step ordered scale (`SO+ < SO < SO-med < MD < MHA < HA < HA-super`)
crossed with material** — precisely MusicXML's `stick-material` × `stick-type` factoring, with
a finer hardness scale.

**Articulation / event-shape axis** — `cre` crescendo, `dim` diminuendo, `dyn` dynamics
(cresc+dim), `dyn9` dynamics 9 repetitions, `dyn-me` / `dyn-str` medium/strong dynamics,
`acc` accelerando, `fa`/`me`/`sl` fast/medium/slow, `lo` long, `1s, 2s, …` tone length in
seconds, `UB` upbeat, `UB-a1/-a2` 1/2 upbeats, `perf-rep` repetition performance,
`Gliss` glissando, `pizz` pizzicato, `on`/`off` snare on/off, `v1, v2 …` variation,
`Vib` with vibrato, `XF` cell-crossfade matrix.

**Instrument-size axis** — `50, 60, …` centimetres diameter; `6Z, 8Z, …` inches diameter;
piatti makers/types as instance descriptors (`Za` Zildjian Avedis, `K`/`K2` Avedis K1/K2,
`Is` Istanbul Janissary/Symphonic, `Chi` China).

#### 2.8.2 Per-instrument articulations (selected, verbatim from the keymaps)

| instrument | articulations |
|---|---|
| **Tambourine (A–D)** | single hits **middle** vs **rim**, left/right hand · single hits **normal** vs **sforzato** · performance repetitions (slow/fast, 105/120/130/240 BPM) · 1–4 **upbeats** (medium/fast) · **tremolo** normal · **tremolo crescendo** (2 and 4 sec) · **shakes** long/short · **shakes dynamics** short/long · **thumb tremolo** (= thumb roll) long/short · **thumb tremolo dynamics** |
| **Triangle (A–D)** | **hit from the side** and **hit from above**, each **open** or **damped** (4 alternations) · performance repetitions · performance-repetition dynamics (cresc/dim, 9 reps) · 1–3 upbeats · tremolo normal · tremolo strong crescendo/diminuendo at 1/2/4/8 sec |
| **Castanets** | single strokes left/right (2 alternations) · performance repetitions var. 1 & 2 (80 BPM) · 1–4 upbeats · 4 upbeats fast · tremolo 1 sec and 8 sec |
| **Guiro (wood / gourd)** | strokes **short / medium / long / accelerando**, each **up** and **down**, each **open** or **muted attack** · performance repetitions, 4 patterns, slow (67 BPM) / medium (84 BPM) |
| **Shaker (bamboo / chrome / kiwi)** | single shakes var 1/2 · 1–2 upbeats · performance repetitions, 3 patterns (88 BPM) · tremolo normal · tremolo dynamics · tremolo **accelerando** and **ritardando** |
| **Caxixi (low / high / double)** | single stroke · slow and fast upbeat · performance repetitions p/f at 80 and 120 BPM |
| **Claves (fiber / wood, low / high)** | single strokes · 1–3 upbeats |
| **Concert snare drum (A/B), snares on** | **Rim clicks** l/r · **Rim head** l/r · **Rim shaft** l/r · **Rim SOS** l/r · **Rim SOSOR** l/r · single hits l/r (4 alternations) · performance repetitions at 60/113/120 BPM · **press rolls** left/right/unisono · 1–4 upbeats · 2–4 **upbeat rolls** · rolls normal · rolls strong/medium dynamics at 0.5/1/2/4/8 sec |
| **Concert snare drum, snares off** | single hits, performance repetitions, upbeats, upbeat rolls, rolls normal, rolls dynamics |
| **Concert bass drum (A/B)** | single hits **normal** and **secco**, l/r (4 alternations) · performance repetitions slow/fast · 1–3 upbeats · rolls normal (AB switch long/short release) · rolls strong/medium dynamics 1/2/4 sec — all duplicated per mallet (`SO`, `HA`) |
| **Tam-tam (A, series B, series C)** | single hits **normal sound** and **hard sound**, l/r · tremolo · **long scratch** · sizes 60/100/130 cm · "various beaters" |
| **Gongs** | soft-mallet single notes · soft-mallet **rolls** · soft-mallet **rolls crescendo** · wood-mallet single notes · metal-mallet single notes · **bowed** single notes |
| **Cowbells** | single notes **bright** and **dark** × 5 pitches, per implement: **wool mallet**, **wood mallet**, **triangle beater** · **bowed** normal and **overtones** · **rubbing stick** |
| **Timpani** | per mallet (`Standard`, `Medium`, `Hard`, `Wood`, `Medium hard`, `Felt`, `Finger`): single strokes, **rolls**, **glissandi**, **glissandi-roll**, "additionals" |
| **Ratchets (1–5)** | **staccato**, **short**, **medium**, **long** tone (with release samples) |
| **Ocean drum (A/B)** | **short**, **long**, **motion** sounds; **accents** as full sample + excerpts |
| **Rainmaker (1–3)** | **slow**, **fast**, **shaken**; patterns at named BPM |
| **Spring drum** | **pizzicato** (p/mf/ff), **finger snip**, **finger slide** slow/fast, **rotation** (p/f/stereo), **pulse** single strokes / slow / medium / fast |
| **Flexatone (A/B)** | **static tones** 2 s and 4 s · **glissandi up/down** 2 s and 4 s at named intervals · **FX** (full sample + excerpts) |
| **Vibratone** | single strokes · 1/2/4-fold **pitch change** up/down · fast double pitch change · tremolo normal · tremolo accelerando / ritardando |
| **Whip** | 2 whips × 2 variations |
| **Hammer** | beats on **wood blocks**, **wood boards**, **wood crates** |
| **Log drum** | single hits and rolls per mallet (hard / medium / soft / wood) |
| **Sirens (1–3)** | dry and wet tones of named durations |
| **Bull roarer** | 6 sounds, full sample + 3–8 excerpts each |
| **Gun shots** | 6 mm pistol / 6 mm revolver / 9 mm revolver; single and double shots; wet and dry |

VSL's front-matter instrument list (72 instruments) additionally names: Altar-boy bells,
Anklung, Bicycle horns, Boobam, Brake disks, Burma bells, Car horns, Cencerros, Church bells,
Crotales, Cuica, Field drum, Finger cymbals, Handbells, Japanese singing bowls, Jingle ring,
Lion roar, Lithophone, Piatti, Piccolo drum, Plate bells, Railway rails, Ship's bell, Springs,
Stir xylophone, Thundersheets, Waldteufel, Waterphone, Wind machine.

**Findings.**
- **"Upbeat" (`UB`, 1–4 upbeats) is an articulation on nearly every orchestral instrument** — a
  pre-recorded pickup gesture. It has no equivalent anywhere in the drum-kit vocabulary or in
  drum-remap, and it is *not* a roll or a flam.
- **"Performance repetition" (`perf-rep`) at a named BPM** and **tremolo/roll of a named
  duration in seconds** are distinct sampled-event kinds. `IsMultipleNoteSample` in Sibelius is
  the same concept. A pivot entry needs a flag for "this entry is a multi-note sample".
- **Tambourine `middle` vs `rim`, triangle `from the side` vs `from above`, snare
  `Rim clicks / Rim head / Rim shaft`** are *zone* values that only make sense per-instrument.
  `Rim SOS` / `Rim SOSOR` are VSL-internal and their expansion is **UNVERIFIED**.
- **Guiro's `up`/`down` × `open`/`muted attack` × `short/medium/long/accelerando`** is a clean
  three-facet product; enumerating it as flat tags would need 24 tokens.

### 2.9 Spitfire Percussion (S9) — instrument inventory

Individual instruments, verbatim, grouped as Spitfire groups them:

- **Drums – High:** Bongos, Conga 1, Conga 2, Rototoms, Snare 1, Snare 2, Snare 3, Timbales
- **Drums – Low:** Bass Drum, Field Drum, **Gong Drum**, Tom Ensemble, Toms
- **Toys:** Agogo, Cabasa, Castanets, Cowbells, **Gankogui**, Guiro, **Jawbone**, Ratchet,
  Shakers, **Ships Bell**, Sleighbells, Tambourines
- **Unpitched – Metal:** Anvil, **Mini Anvil**, Cymbal Hi/Lo/Med, Mark Tree, **Piatti**,
  **Rain Sheet**, **Rivet Cymbal**, Tam Tam, **Trash Metals**, Triangle 1, Triangle 2,
  **Wind Gong**
- **Unpitched – Wood:** Claves, Temple Blocks, Woodblocks
- **Tuned:** Celeste, Crotales, **Desk Bells**, Glockenspiel, Marimba, Timpani, Tubular Bells,
  Vibraphone, Xylophone
- **Ensembles:** Contemporary, Hands and Hits, Low Ensemble, Metal Clangs, Snare Ensemble,
  Traditional Orchestra

The manual documents the *mechanism* rather than the technique names: "In Kickstart, a
technique is a way the instrument can be played. Available techniques differ between
instruments"; techniques are user-remappable to arbitrary MIDI notes; some techniques expose a
**"single vs double key"** toggle ("The latter expands this to two keys allowing you to play
rolls, flams and trills much easier") and a **beater/mallet switch** ("the Gong Drum in
Spitfire Percussion was recorded being struck with both a stick and a wooden mallet"); a
`ROLL ON HIGH VEL.` option makes velocity select the roll articulation; `Snares on/off` is a
per-instrument toggle.

**Findings.** (a) Spitfire's model is *(instrument, technique, beater)* with beater as an
explicit switch. (b) Instrument names like `Gong Drum`, `Piatti`, `Rivet Cymbal`, `Wind Gong`,
`Trash Metals`, `Rain Sheet`, `Gankogui`, `Ships Bell`, `Desk Bells`, `Mini Anvil` exist in no
MIDI standard and only partially in SMuFL/MusicXML — the long tail is real and is *not*
covered by GM.

### 2.10 Roland hand-percussion hardware (S10, S11) — partial

The instrument lists could not be obtained (§1.2). What *is* documented:

- **HPD-20 conga naming** (Owner's Manual, Kit List, kit 8 "Conga II / Live Stage"): "The tone
  will change depending on the dynamics and location of your strike at left/right or from the
  centre to the edge, allowing you to naturally utilize the performance techniques that are
  unique to the conga, such as **heel/toe, slap, and mute**."
- **HPD-20 djembe naming** (kit 7 "Twin-Djembe"): "The M5 pad plays the **bass tone**, and the
  M1 and M2 pads separately play the **centre** and **edge**".
- **HPD-20 frame drum** (kit 16 "Frame Drum w/ Bendir"): "tonal changes produced by the
  **strike location** and **muting**"; frame drum and **bendir** are separate instruments.
- **HPD-20 timbales** (kit 18): performance nuances "produced by applying **pressure with the
  stick** for a **closed shot**" — i.e. a pressed/closed stick technique on timbales.
- **HPD-20 conga kit 32** is named "Conga w/ **Quinto & Tumba**" — Roland names the three conga
  sizes with the Cuban names (quinto/conga/tumba), not high/mid/low.
- **HPD-20 bongo instrument naming pattern** (Sound On Sound review, verbatim): "**Bongo Hi,
  Bongo H Inner, Bongo H Edge, Bongo H Slap, Bongo H/Heel, Bongo H/Toe, Bongo Low and Bongo L
  slap**", "all of these are available in both **left- and right-hand versions**."
- Specification: 850 instruments, 200 kits.
- **SPD-SX**: the manual documents only the on-device `WAVE LIST` screen (sorted by number or
  alphabetically, and "sorted by category"); the wave names themselves are not in the manual.
  **The SPD-SX is a sample player, not a tone generator — its "instruments" are user waves**,
  so there may be no fixed vocabulary to harvest at all. **UNVERIFIED.**
- **Octapad SPD-30** manual contains no instrument list; the string "conga" does not occur.

**Finding:** Roland's hand-percussion naming grammar is
`<instrument> <register-letter> <zone|technique> [/ <hand-part>]` with an implicit
left/right-hand pairing — e.g. `Bongo H Edge`, `Bongo H/Toe`. Register is a letter suffix
(`H`, `L`), zone is a word (`Inner`, `Edge`), technique is a word (`Slap`), hand part is after
a slash (`Heel`, `Toe`). That is four axes in one string.

---

## 3. THE DELIVERABLE — normalised (instrument, articulation) list for percussion

Grouped by the families the brief asks for. Columns:

- **std** — named by a MIDI standard: `1` GM1, `2` GM2, `G` Roland GS, `X` Yamaha XG
  (source: dossier 03 §3, verbatim). `—` = named by no standard.
- **also in** — `N` notation vocabularies (SMuFL / MusicXML / Sibelius / Dorico),
  `L` sample libraries (Toontrack / NI / VSL / Spitfire), `H` hardware (Roland HPD-20).
- **v1** — `●` belongs in the first KITWARP pivot release, `○` long tail (see §5 for the rule).

### 3.A Hand-struck membranophones

| instrument | instance / register axis | articulations | std | also in | v1 |
|---|---|---|---|---|---|
| `conga` | `quinto`/`conga`/`tumba` **or** high/mid/low (both attested); L/R hand | open, muted, closed-slap, open-slap, bass-tone, heel, tip/toe, palm, fingers, knuckles, pressed, slide, flam, slap-flam, roll, crescendo, slap-crescendo, shell/pop | 1 2 G X (mute-hi, open-hi, open-lo, mute-lo, slap, slide) | N L H | ● |
| `bongo` | `macho`/`hembra` **or** hi/lo; L/R hand | open, muted, slap, bass-tone, heel, tip/toe, palm, two-hands, inner, edge, flam, crescendo | 1 2 G X (hi, lo) | N L H | ● |
| `cajon` | 1..n; L/R hand | bass-tone, open, slap-normal, slap-mid, tip, ghost-stroke, side-stick, brush-hit, brushed, damp, mute, hand, stick, flam, crescendo | — | N L H | ● |
| `djembe` | hi/lo | bass-tone, open/tone, slap, closed, muted, edge, centre, palm, pressed, shell, roll, flam | G (`Djembe`, `Djembe Rim`) | N L H | ● |
| `udu` / `ipu` | hi/lo | open-tone-high, open-tone-low, open-slap, muted-slap, ghost-note, bend, neck, shell, palm, mallet, stroke, long, short, crescendo, flam | G (`Udo Long/Short/Slap`) | N L | ○ |
| `frame-drum` (incl. `riq`, `bendir`, `ganjira`, `pandeiro`, `tar`) | small/large | open, damp, mute, slap, edge, roll, shake, double, mallet, hand, hard, crescendo, flam | G (`Bendir`, `Mute/Open Pandiero`) | N L H | ○ |
| `tabla` | `dayan` (treble) / `bayan` (bass) | na, tin, tun, ge, te (stroke names); mute, damp, edge, tip, bend, up, soft | G (`Tabla Ge / Ge Hi / Na / Te / Tun`) | N L H | ○ |
| `bata` | `iya` / `itotele` / `okonkolo`; L/R head | open, slap, muffled, mute, pressed, fingers, flam | — | N L | ○ |
| `darbuka`/`doumbek`/`goblet-drum` | — | dum, tek, ka, slap, roll | G (`Req Dum`, `Req Tik`) | N | ○ |
| `talking-drum` | — | hit, bend-up, bend-down, mute, flam | G (`Talking Drum`, `Bend Talking Drum`) | N | ○ |
| `cuica` | — | open, mute, up-stroke, down-stroke | 1 2 G X (open, mute) | N | ● |
| `surdo` | hi/lo | open, muted/mute, rim | 2 G X (open, mute) | N | ● |
| `tamborim` | — | hit, turn | G | N | ○ |
| `hand-drum` (generic) | — | centre, edge/rim, open, muted, closed-rim, closed-slap, open-rim, open-slap | — | L | ○ |

### 3.B Stick-struck membranophones (non-kit)

| instrument | instance | articulations | std | also in | v1 |
|---|---|---|---|---|---|
| `timbale` | hi (`macho`) / lo (`hembra`) | open-tone, rimshot, side-stroke/cross-stick, **cascara** (shell), paila, closed-shot (pressed stick), mute, flam, ruff, roll, cowbell-mounted | 1 2 G X (hi, lo, `Timbales Paila`) | N L H | ● |
| `concert-snare-drum` | — | hit, snares-on, snares-off, rim-shot, rim-click/side-stick, stick-shot, stick-on-stick, press-roll, buzz-roll, open-roll, drag, ruff, flam, crush, rim-head, rim-shaft, upbeat, upbeat-roll, roll-crescendo | 2 G X (`Concert SD`, `Snare Roll`) | N L | ● |
| `orchestral-bass-drum` (`gran cassa`) | — | hit, secco, muffled/damped, rim, roll, roll-crescendo, crush, upbeat, flam, accent, L/R | 2 G X (`Concert BD`, `Gran Casa`) | N L | ● |
| `tenor-drum` | — | hit, rim, rim-shot, buzz-roll, roll, crush, dry, flam, shell, stick-click, stick-on-stick, triple | — | N L | ○ |
| `field-drum` / `military-drum` | — | hit, roll | — | N L | ○ |
| `gong-drum` | — | hit (stick), hit (wooden mallet) | — | L | ○ |
| `timpani` | pitched, 1..5 drums | single stroke (per mallet), roll, roll-crescendo, glissando, glissando-roll, muted/coperto, secco, finger | 2 G (13 pitch-named notes) | N L | ● |
| `taiko` (`wadaiko`, `shime-daiko`, `nagado`, `okedo`) | — | hit, rim, ka (rim), don (centre) | G (`Wadaiko`, `Wadaiko Rim`, `Shime Taiko`) | N | ○ |
| `boobam` / `octoban` / `rototom` | 1..n | centre, hit, glissando (rototom) | — | N L | ○ |
| `piccolo-drum` | — | hit, roll | — | L | ○ |
| `log-drum` / `slit-drum` | tongue 1..n | hit, mute, damp, roll (per mallet hardness) | — | N L | ○ |

### 3.C Shaken idiophones

| instrument | instance | articulations | std | also in | v1 |
|---|---|---|---|---|---|
| `shaker` (egg / tube / metal / steel / wood / clay / gourd) | 1..n; L/R | on-beat, off-beat, shake/shakings, single, stroke, up, down, motion, tremolo, tremolo-accelerando, tremolo-ritardando, long, short, crescendo | 2 G X (`Shaker`) | N L | ● |
| `maracas` | 1 or 2; L/R | hit, on-beat, off-beat, shake, accent, rotation, up, down, roll, fast, slow, long, short | 1 2 G X | N L | ● |
| `cabasa` / `afuche` | — | hit, beat, on-beat, long, short, slap, tap, **up-stroke**, **down-stroke** | 1 2 G X (`Cabasa`, GS `Cabasa Up`/`Cabasa Down`) | N L | ● |
| `caxixi` | low / high / double | beat, on-beat, off-beat, single-stroke, upbeat-slow, upbeat-fast, up, down, FX | G (`Caxixi`) | N L | ○ |
| `shekere` | hi / lo | beat, on-beat, off-beat, shake, accent, bass, front, back, up, down | G (via `Caxixi`/GS ext.) — mostly `—` | N L | ○ |
| `tambourine` | — | **open hit**, **muted hit**, **thumb roll**, **shake/tremolo**, **roll**, **shake-dynamics**, fist, frame/shell, head, stick, on-beat, off-beat, pop, flam, crescendo, upbeat, short, jingle-only | 1 2 G X (`Tambourine`) | N L H | ● |
| `sleigh-bells` / `jingle-bells` | — | hit, tap, shake, roll | 2 G X (`Jingle Bell`) | N L | ● |
| `jingle-ring` | — | hit, shake | — | N L | ○ |
| `rainstick` / `rainmaker` | 1..3 | slow, fast, shaken, pattern | — | N L | ○ |
| `chain-rattle` / `ratchet-rattle` / `ganza` / `hosho` / `kayamba` | — | shake, on-beat, off-beat | — | N | ○ |
| `vibraslap` | — | hit, stroke | 1 2 G X (`Vibra-slap`) | N L | ● |
| `flexatone` | — | static-tone (by length), glissando-up, glissando-down, bend, FX | — | N L | ○ |
| `sistrum` | — | shake | — | N | ○ |
| `bell-tree` / `mark-tree` / `wind-chimes` | glass / metal / bamboo / shell | gliss-up, gliss-down (fast/slow), tinkle, tremolo, reverse | 2 G X (`Bar Chimes`/`Bell Tree`/`Wind Chimes`; GS `Reverse Bell Tree`) | N L | ● |

### 3.D Scraped idiophones

| instrument | instance | articulations | std | also in | v1 |
|---|---|---|---|---|---|
| `guiro` (wood / gourd / metal `guira`) | — | **short scrape**, **long scrape**, medium, accelerando, up, down, open-attack, muted-attack, up-fast, stroke, pattern | 1 2 G X (`Guiro Short`, `Guiro Long`; GS `Reverse Guiro`) | N L H | ● |
| `reco-reco` | — | short, long, up, down | — | N | ○ |
| `bamboo-scraper` | — | scrape | — | N | ○ |
| `washboard` | — | scrape, hit | — | N | ○ |
| `quijada` / `jawbone` | — | hit, rattle, scrape, fingers, palm, slap | — | N L | ○ |
| `ratchet` | 1..5 | staccato, short, medium, long, turn | — | N L | ○ |
| `sandpaper-blocks` | — | scrape | — | N | ○ |
| `guiro-on-drum` (scrape technique on a membrane) | — | scrape-centre-to-edge, scrape-edge-to-centre, scrape-around-rim-cw, scrape-around-rim-ccw | — | N (SMuFL) | ○ |

### 3.E Struck idiophones — wood

| instrument | instance | articulations | std | also in | v1 |
|---|---|---|---|---|---|
| `woodblock` | hi / lo, or `Block 1..5` | hit, soft, hard, roll, triple, flam, diminuendo | 1 2 G X (hi, lo) | N L | ● |
| `temple-block` | 1..5 | hit, soft | — | N L | ○ |
| `claves` | fiber / wood, hi / lo | hit, flam, upbeat 1–3 | 1 2 G X | N L | ● |
| `castanets` (hand / with handle / machine) | — | single stroke L/R, roll, flam, upbeat 1–4, tremolo (1 s / 8 s), short | 2 G X (`Castanet`) | N L | ● |
| `jam-block` / `agogo-block` / `tic-toc-block` / `granite-block` | hi / lo | hit | — | N | ○ |
| `whip` / `slapstick` | 1..2 | single, flam, variation | — | N L | ○ |
| `board-clapper` / `pan-clappers` / `bones` / `spoons` | — | hit, roll, off-beat, on-beat | — | N L | ○ |
| `hyoushigi` | — | hit | G | N | ○ |
| `drum-sticks` (sticks clicked together) | — | hit, count-in, in | 1 2 G X (`Sticks`) | N L | ● |
| `sandblock` / `gourd` / `ipu` | — | hit, roll, three-strikes, four-strikes, triple, mute | — | N | ○ |

### 3.F Struck idiophones — metal

| instrument | instance | articulations | std | also in | v1 |
|---|---|---|---|---|---|
| `cowbell` | 1..n; `bongo bell`, `timbale bell`, `cha-cha bell`, `mambo bell` | hit, **top**, **side/mouth**, muted, damped, single | 1 2 G X (`Cowbell`) | N L H | ● |
| `agogo` | hi / lo | hit, mute, closed, soft, roll, short | 1 2 G X (hi, lo) | N L | ● |
| `cencerro` / `almglocken` / `gankogui` / `dawuro` | 1..n | hit, mute | — | N L | ○ |
| `triangle` | 1..n, by size | **open**, **muted/damped**, **closed**, hit-from-side, hit-from-above, roll/tremolo, roll-crescendo, roll-diminuendo, choke, flam, triple, upbeat, long, short, portato | 1 2 G X (`Open Triangle`, `Mute Triangle`) | N L | ● |
| `finger-cymbals` / `zills` / `crotales` | hi / lo | bell, edge, open, choke, rub, zing, bowed | — | N L | ○ |
| `tam-tam` | by size (60/100/130 cm) | hit-normal, hit-hard, roll/tremolo, long-scratch, slide-brush, bowed, choke, crescendo | G (via `Big Gong`/`Gamelan Gong`) partially | N L | ● |
| `gong` (nipple/domed, Chinese, opera, wind, thai, gamelan) | by size and type | hit, roll, roll-crescendo, bend, nipple/button, scrape, bowed, choke, tip, per-mallet (soft / wood / metal) | G (`Big Gong`, `Small Gong`, `Thai Gong`, `Gamelan Gong`, `Bend Gong`, `Reverse Gong`) | N L | ● |
| `anvil` / `brake-drum` / `railway-rail` / `mini-anvil` | 1..n | hit, flam, damp, scrape | — | N L | ○ |
| `bell-plate` / `plate-bell` / `church-bell` / `handbell` / `desk-bell` / `ship's-bell` | 1..n | hit, damp, swing | — | N L | ○ |
| `thundersheet` / `rain-sheet` / `trash-metals` | — | hit, shake, roll | — | N L | ○ |
| `metal-tube-chimes` / `metal-plate-chimes` / `bamboo-chimes` / `shell-chimes` / `glass-chimes` | — | stroke, gliss-up, gliss-down | 2 G X (`Wind Chimes`) | N L | ○ |
| `singing-bowl` / `tibetan-bowl` | 1..n | struck, rubbed/bowed | — | N L | ○ |
| `steel-drum` / `hang` | pitched | hit | 2 G X (in melodic banks, not the drum map) | N | ○ |
| `musical-saw` / `waterphone` / `vibratone` / `flexatone`(metal) | — | bowed, glissando, pitch-change, tremolo-accel/rit | — | N L | ○ |
| `sizzle-cymbal` / `rivet-cymbal` / `piatti` (crash cymbals, hand) | pairs | clash open, clash damped, `hand cym. closed/open` (XG), suspended roll | 2 G X (`Concert Cymbal`, `Hand Cym. Open/Closed H/L`) | N L | ● |

### 3.G Effects / aerophones / non-instrument sounds

| instrument | articulations | std | also in | v1 |
|---|---|---|---|---|
| `whistle` (samba) | **short**, **long**, high, low, flutter, up, down | 1 2 G X (`Short Whistle`, `Long Whistle`) | N L | ● |
| `police-whistle` | short, long, trill | — | N L | ○ |
| `slide-whistle` | up, down, gliss | — | N | ○ |
| `bird-whistle` / `duck-call` / `lotus-flute` | call | 2 G X (`Bird`) | N | ○ |
| `siren` | dry, wet, by duration | 2 G X | N L | ○ |
| `wind-machine` | variation 1–7 | — | N L | ○ |
| `lion's-roar` / `spring-drum` / `bull-roarer` | pizzicato, finger-slide, finger-snip, rotation, pulse, full/excerpt | — | N L | ○ |
| `ocean-drum` | short, long, motion, accent | — | N L | ○ |
| `hand-clap` | hit, single, multi, big, crowd | 1 2 G X | N L | ● |
| `finger-snap` | hit | G X | N L | ● |
| `stomp` / `body` | chest-hit, stomp, zip, hand-breath | — | L | ○ |
| `gun-shot` / `cannon` / `pistol-shot` | single, double, wet, dry | 2 G | N L | ○ |
| `car-horn` / `klaxon` / `bicycle-horn` | open, muted | 2 G X | N L | ○ |
| `applause` | — | 2 G | N L | ○ |
| `metronome` | click, bell | 2 G X | N | ● |

---

## 4. Implications for the KITWARP pivot vocabulary

### 4.1 Axes this dossier confirms, and the sources that force them

| axis | forced by | note |
|---|---|---|
| **instrument** | every source | ~400 identities in MusicXML Standard Sounds alone. Must be an open, hierarchical namespace, not a closed enum. |
| **instance / register** | Sibelius (`very low … high` as its own path segment), Roland (`Quinto & Tumba`, `Bongo H/L`), NI (`macho`/`hembra`), Toontrack (`Conga 1/2`, `Timbale 1/2`), Spitfire (`Conga 1/2`, `Triangle 1/2`) | **Register naming is culture-specific**: hi/mid/low, quinto/conga/tumba, macho/hembra, iya/itotele/okonkolo all denote the same *relative position in a set*. The pivot needs an ordinal-with-descriptor instance, exactly as the draft axes propose. |
| **zone** | MusicXML `stick-location` (normative: center, rim, cymbal bell, cymbal edge); SMuFL `pictCenter*`/`pictRim*`/`pictOnRim`/`pictEdgeOfCymbal`/`pictBellOfCymbal`; VSL tambourine middle/rim, triangle side/above, snare rim-head/rim-shaft; Roland `Bongo H Inner`/`Bongo H Edge` | Zone values are **instrument-scoped**. New percussion values needed beyond the kit set: `inner`, `edge`, `centre`, `shell`, `frame`, `head`, `neck` (udu), `mouth`/`top`/`side` (cowbell), `nipple`/`button` (gong), `paila` (timbale shell). |
| **technique** | all | see §4.2. |
| **openness scalar** | SMuFL `pictOpen` / `pictHalfOpen1,2` / `pictDamp1..4`; Sibelius `open`/`closed`/`mute`/`muffled`/`damp`/`pressed`; NI "Soft sound = Muted"; VSL `open`/`damped` on triangle | Confirms an ordered scalar with anchors, not a flat enum. **For hand drums the anchors are different from the hi-hat's**: `open > muffled > muted > pressed > closed > slap-closed`. Two named scales, one mechanism. |
| **implement / beater** | **SMuFL 53 beater types**; **MusicXML `stick-type`(10) × `stick-material`(5) + `beater-value`(20)**; VSL 22 mallet abbreviations with a 7-step hardness scale; Spitfire's per-instrument beater switch | This is the axis most under-served by every existing converter. It must be **factored** (`form × material × hardness`) not enumerated flat, or it multiplies the vocabulary by 20–50. |
| **limb / hand-part** | Sibelius (`left`/`right` on 8 instrument families), Toontrack (`Left/Right` on every Latin bucket), VSL (`l/r` on nearly every patch), SMuFL `pictRightHandSquare`/`pictLeftHandCircle`, NI (`heel`/`tip` grouped with `up`/`down`) | Two *distinct* things are being conflated by every source: **which limb** (L/R) and **which part of the limb** (heel / toe / tip / palm / fingers / knuckles / fist). KITWARP should split them: `limb ∈ {left,right}` and `contact ∈ {heel,toe,tip,palm,fingers,knuckles,fist,hand,fingernail}`. `contact` is really a *value of the implement axis* (SMuFL and MusicXML both list `hand`, `finger`, `fist`, `fingernail` as **beaters**). |
| **gesture phase / direction** | Sibelius `up`/`down`/`stroke` on shaker, maraca, cabasa, caxixi, guiro, mark tree, bell tree; GS `Cabasa Up`/`Cabasa Down`; NI "Up/Down (Maracas)", "Front/Back (Shekere)"; VSL guiro `up`/`down`; Toontrack `On Beat`/`Off Beat` on ~10 shaken instruments | **A new axis with no drum-kit analogue.** Values: `up`, `down`, `front`, `back`, `on-beat`, `off-beat`. NI groups `heel`/`tip` under the same heading, which suggests `gesture-phase` and `contact` may be one axis for hand drums — but the shaker `up/down` clearly is not a body part. Recommend two axes and a documented mapping between them. |
| **event kind / multi-note** | Sibelius `IsMultipleNoteSample`; VSL `perf-rep`, `UB`, `tremolo n sec`, `dyn9`; Toontrack `Crescendo`, `Flams`, `Ruff`; Dorico's separation of *single-note tremolos* from techniques | An entry must declare whether it is a **single stroke**, a **compound stroke** (flam, drag, ruff, triple), a **sustained/repeated sample** (roll, tremolo, shake, scrape, performance repetition), a **shaped sample** (crescendo, diminuendo, cresc-dim, accelerando, ritardando), or a **pickup** (upbeat 1–4). This is *not* the same axis as technique, and drum-remap has no place for it. |
| **duration / speed qualifier** | VSL (`1s, 2s, 4s, 8s`, BPM-named repetitions, `fa/me/sl`); Sibelius (`long`, `short`, `fast`, `slow`, `medium`); GM (`Guiro Short`/`Guiro Long`, `Short Whistle`/`Long Whistle`) | GM itself makes `short`/`long` part of the *identity* of guiro and whistle. So this qualifier must be representable in the pivot, not discarded as performance data. |

### 4.2 The technique vocabulary the percussion families actually need

Merging all sources and removing notational duplicates, the **technique** axis needs at least
these values beyond the drum-kit set (`hit`, `rimshot`, `sidestick`, `choke`, `flam`, `drag`,
`roll`, `buzz`):

`open` · `open-tone` · `slap` · `open-slap` · `closed-slap` · `bass-tone` · `mute` ·
`muffled` · `damped` · `pressed` · `heel` · `toe` · `tip` · `palm` · `fingers` · `knuckles` ·
`two-hands` · `ghost` · `pop` · `shell` · `cascara` · `paila` · `cross-stick` ·
`stick-shot` · `stick-on-stick` · `stick-click` · `press-roll` · `buzz-roll` · `crush` ·
`ruff` · `triple` · `scrape` (with 4 directional variants) · `shake` · `stroke` ·
`tremolo` · `swirl` · `rub` · `bow` · `bend` · `glissando` · `pitch-change` · `rotation` ·
`slide` · `turn` · `zing` · `tinkle` · `secco` · `sforzato` · `portato` · `upbeat` ·
`crescendo` · `diminuendo` · `accelerando` · `ritardando` · `reverse`.

That is ~55 technique values. Combined with ~200 instruments and the instance/zone/implement
axes it is obvious why an enumerated-tag model (drum-remap: 40 pairs) and a 170-key tree
(`lotkey/Drum-MIDI-Converter`) both fail: **the percussion space is a product space, and the
only tractable representation is faceted with derived fallbacks.**

### 4.3 Terms missing from the reference models

Against `marty-615/drum-remap` (12 instruments, 40 pairs, 1 percussion instrument = `cowbell`):

- **Every instrument in §3 except `cowbell` is inexpressible.** That is ~120 instruments.
- Missing axes: implement/beater, limb, contact-part, gesture-phase, event-kind, duration
  qualifier, register/instance-naming-scheme.
- `role` remains unattested: **no percussion source in this dossier has a role field.** NI's
  "basic or neutral stroke / louder or higher / bass or special" ranking is the closest thing —
  and it is explicitly a *relative loudness/timbre ranking within one instrument*, i.e. a
  fallback-ordering hint, exactly as dossier 00 predicted `role` would turn out to be.

Against `lotkey/Drum-MIDI-Converter` (170 keys, perc = 10): the percussion branch is 10 keys
against the ~120 instruments and ~400 (instrument, articulation) pairs enumerated here.

### 4.4 Real vs cosmetic distinctions

**Real (must be representable):**
- conga `open` vs `muted` vs `bass-tone` vs `slap` vs `heel` vs `tip` — five distinct samples in
  every library, and GM itself distinguishes open/mute.
- timbale `open-tone` vs `rimshot` vs `cascara` vs `paila` vs `cross-stick`.
- tambourine `hit` vs `shake` vs `roll` vs `thumb-roll` — VSL samples all four separately and
  `thumb tremolo` has its own velocity layering.
- triangle `open` vs `muted`; and `hit from the side` vs `hit from above` (different samples).
- guiro `short` vs `long` (GM makes this identity) and `up` vs `down` (VSL, NI, Sibelius).
- shaker/maraca `on-beat` vs `off-beat` vs `up` vs `down` — different samples in Toontrack, NI
  and VSL; collapsing them destroys the groove.
- `snares on` vs `snares off` — a state, not a stroke.
- mallet hardness on timpani, tam-tam, gong, log drum, bass drum, cowbell.
- L/R hand where libraries sample them separately (conga, cajon, castanets, bass drum, snare).

**Cosmetic (normalise away):**
- SMuFL's Weinberg / Ghent / Caltabiano / Agostini notational variants (`pictCenter1..3`,
  `pictRim1..3`, `pictDamp1..4`, `pictHalfOpen1..2`) — 12 glyphs, 4 concepts.
- SMuFL beater stem directions (up/down/left/right) — 128 glyphs, 53 concepts.
- MusicXML `tip-direction` (8 values) — pure engraving.
- Sibelius library/sample-set tags (`vi-one`, `eop`, `kit-*`, `grover`, `vaughncraft`,
  `clemente`, …) — vendor provenance, not identity.
- Toontrack's octave-duplicated `[Conga 2]` block (notes 111–118 = 102–109).
- Spelling: `Tamburin`/`Tambourine`, `Pandiero`/`Pandeiro`, `viborslap`/`vibraslap`,
  `Woodbocks`/`Woodblocks`, `guira`/`güira`.
- `Bongo H` vs `High Bongo` vs `Hi Bongo` vs `Bongo Hi` — register spelling.

**Deliberately borderline (decide explicitly):**
- `muted` vs `damped` vs `muffled` vs `closed` vs `pressed`: five words, and the sources do not
  agree on how many concepts they name. Recommendation: one **damping scalar** with named
  anchors `open → half-open → muffled → damped → pressed → closed`, and treat the source words
  as aliases onto anchors, not as separate techniques.
- `open-tone` vs `open`: Toontrack uses both in the same file (`[Timbale 1] Right OpenTone`,
  `[Conga 1] Left Open`). Treat as one concept.
- `slap` on a conga (a *technique*) vs `Slap` in GM's SFX bank (a *sound effect*) — different
  things with the same word. Namespacing by family prevents the collision.

### 4.5 What the notation sources add that the audio sources do not

1. **Sibelius's `SoundIDChange` grammar (`+x`, `-x`, `[reset]`) is a ready-made design for
   KITWARP's facet modifiers**, including the explicit guidance on when to keep facets separate
   (`+pizzicato +mute`) and when a compound is atomic (`+mute.harmon`). Adopt it.
2. **Sibelius's "substitute the closest available sound ID" is the fallback semantics KITWARP
   needs**, and it is prefix-based on a hierarchical ID — which is exactly the "walk up parents"
   rule in the draft axes.
3. **Dorico proves the identity is (instrument, technique-set)** and that noteheads / staff
   positions / articulation overrides live *outside* that identity.
4. **MusicXML proves the implement axis should be factored** and gives a normative 4-value
   `stick-location`.
5. **SMuFL proves instrument / technique / beater are three separate namespaces.**

---

## 5. v1 vs long tail — the recommendation

**Rule used for the `v1` column in §3:** an (instrument, articulation) pair is v1 if it meets
**either** of:
(a) it is named by GM1/GM2/GS/XG — because every hardware module and every GM-mode library
    emits it, so KITWARP will meet it on day one; **or**
(b) it appears in the *percussion section of a drum-kit library that KITWARP already targets*
    (Superior Drummer / EZdrummer percussion buckets, BFD3, Addictive Drums, NI Studio Drummer)
    — i.e. it can arrive on a drum-kit MIDI track without the user ever loading a percussion
    library.

Everything else is long tail.

### 5.1 v1 percussion set (recommended: ~40 instruments, ~150 pairs)

- **Hand drums:** conga (open/muted/bass-tone/open-slap/closed-slap/heel/tip/slide/flam/
  crescendo), bongo (open/muted/slap/heel/flam/crescendo), cajon (bass/slap-norm/slap-mid/
  ghost/side-stick/brush), djembe (bass/tone/slap/rim), cuica (open/mute), surdo (open/mute).
- **Stick drums:** timbale (open-tone/rimshot/side-stroke/paila/flam/ruff), concert snare
  (hit/rimshot/rim-click/roll/press-roll/snares-off), orchestral bass drum (hit/muffled/roll),
  timpani (hit/roll).
- **Shaken:** shaker (on-beat/off-beat/shake), maracas (hit/shake/up/down), cabasa
  (hit/long/short/up/down), tambourine (open/muted/shake/roll/thumb-roll/on-beat/off-beat),
  sleigh-bells, vibraslap, bell-tree/mark-tree (gliss-up/gliss-down), caxixi *(borderline —
  GS-named, include)*.
- **Scraped:** guiro (short/long/up/down).
- **Wood:** woodblock hi/lo, claves, castanets, temple blocks *(borderline)*, drum-sticks.
- **Metal:** cowbell (hit/top/side/muted) + bongo-bell + timbale-bell, agogo hi/lo (hit/mute),
  triangle (open/muted/roll/choke), tam-tam (hit/roll/scratch), gong (hit/roll/bend),
  hand-cymbals/piatti (open/closed), finger cymbals *(borderline)*.
- **Effects:** samba whistle (short/long), hand-clap, finger-snap, metronome click/bell,
  applause.

That is comfortably inside the "beat 170 keys / 80 SD3 entries" target while covering
100 % of the GM/GM2/GS/XG percussion namespace (all 72 Hand/Latin/World sounds + the
4 orchestral ones from dossier 03 §3).

### 5.2 Long tail (defer, but reserve the namespace shape)

Bata, tabla (dayan/bayan stroke names), darbuka/req, talking drum, udu/ipu, frame-drum family
(riq/bendir/ganjira/pandeiro/tar), taiko family, boobam/octoban/rototom, log/slit drum,
shekere, ganza/hosho/kayamba, rainstick, ratchet, reco-reco, washboard, quijada,
sandpaper blocks, whip/slapstick, bones/spoons/clappers, jam/tic-toc/granite blocks,
cencerro/almglocken/gankogui, bell-plate/church-bell/handbell/desk-bell/ship's-bell,
crotales/zills, anvil/brake-drum/railway-rail, thundersheet/rain-sheet/trash-metals,
singing bowls, musical saw / waterphone / vibratone / flexatone, chimes families (glass /
bamboo / shell / metal tube / metal plate), lion's roar / spring drum / bull roarer,
ocean drum, wind machine, sirens/horns/whistles beyond samba, gun-shot/cannon,
body percussion.

**Critical constraint:** the long tail must be *addressable* in v1's namespace even if it is not
*populated*. Because the pivot is symbolic and hierarchical, adding `wood.reco-reco.scrape.up`
later costs nothing — but only if v1 already commits to (i) a hierarchical dotted instrument
namespace of the MusicXML Standard Sounds shape, (ii) facet modifiers of the Sibelius
`+facet` shape, and (iii) instrument-scoped zone and technique value sets. Changing any of
those three later invalidates collected device data, which is the failure mode the brief warns
about.

### 5.3 One concrete naming decision to make now

The three register-naming schemes (`hi/mid/low`, `quinto/conga/tumba`, `macho/hembra`,
`iya/itotele/okonkolo`, `dayan/bayan`) must resolve to **one canonical ordinal plus an optional
culture-specific descriptor**, e.g.

```
conga.instance{ordinal: 1, descriptor: "quinto"}   ← highest
conga.instance{ordinal: 2, descriptor: "conga"}
conga.instance{ordinal: 3, descriptor: "tumba"}    ← lowest
bongo.instance{ordinal: 1, descriptor: "macho"}
bongo.instance{ordinal: 2, descriptor: "hembra"}
```

with the ordering convention (1 = highest) fixed and documented, because GM says `Hi Bongo` =
note 60 and `Low Bongo` = 61 (higher instrument on the *lower* note), Toontrack says
`Bongo 1`/`Bongo 2` with no pitch semantics at all, and NI says `macho` is the *larger* drum of
a bongo pair while for timbales `macho` is the *smaller*. **Getting this backwards silently
swaps every conga and bongo in every conversion.** Flagged as the single highest-risk naming
decision in the percussion vocabulary.

---

## 6. Provenance

### 6.1 Fact → source index

| § | Fact | Source | Licence |
|---|---|---|---|
| 2.1 | 278 SMuFL `pict*` glyph names, range membership, descriptions | `w3c/smufl` `metadata/glyphnames.json`, `metadata/ranges.json`, SMuFL 1.4 | W3C Community Contributor Licence; SMuFL specification text CC BY 4.0. **Glyph names are factual identifiers.** |
| 2.2 | MusicXML percussion enumerations | `w3c/musicxml` `schema/musicxml.xsd` | W3C Community Final Specification Agreement; MusicXML 4.0 released under W3C CLA. Enumeration values are a normative vocabulary. |
| 2.3 | Standard Sounds percussion IDs | `w3c/musicxml` `schema/sounds.xsd` (extracted to `data/musicxml_sounds_percussion.txt` by dossier 02/03) | as above |
| 2.4.1 | Sibelius sound set XML structure, `DrumMap`/`DrumSound`/`SoundIDChange` quotes | `https://www.sibelius.com/download/sse/Sound Set Editor User Guide.pdf` | © Avid. Quoted under fair dealing for factual reporting; **the format description, not the file contents, is what KITWARP reuses.** |
| 2.4.2 | 7 062 Sibelius sound IDs and their token structure | `data/sibelius_unpitched_soundids.txt` (harvested by dossier 02/03) | © Avid — sound IDs are Avid's namespace. **Do not ship Avid sound ID strings as KITWARP's pivot IDs.** Use them as evidence of structure only. |
| 2.5 | Dorico Percussion Maps dialog fields | `https://archive.steinberg.help/dorico_se/v3/en/dorico/topics/play_mode/play_mode_percussion_maps_dialog_r.html` | © Steinberg. Quoted for factual reporting. |
| 2.5 | ">200 techniques listed" | `https://www.scoringnotes.com/reviews/dorico-1-2-review-part-3-percussion/` | third-party review; **secondary source** |
| 2.6 | EZX Latin Percussion 128 note names | `scratchpad/repos/jim_cubase_drum_maps_for_toontrack/drum_maps/EZX Latin Percussion.drm` (repo `jim/cubase_drum_maps_for_toontrack`) | drum map file generated from Toontrack product data; **Toontrack product naming is Toontrack's.** Use as evidence, map to KITWARP's own IDs. |
| 2.7 | NI Cuba percussion symbol table, instrument descriptions | `https://www.native-instruments.com/fileadmin/ni_media/downloads/manuals/spotlight_collection/Cuba_Manual_English_29_06_2021.pdf` | © Native Instruments. Quoted for factual reporting. |
| 2.8 | VSL abbreviations table and per-instrument keymaps | `https://odl.vsl.co.at/cms-vsl/legacy-manuals/collections/vi_percussion_manual_v1.1.pdf` (© 2006 Vienna Symphonic Library) | © VSL. Quoted for factual reporting. |
| 2.9 | Spitfire instrument/preset list and engine description | `https://d1t3zg51rvnesz.cloudfront.net/p/files/product-manuals/1553/1529333485/SpitfirePercussion_UserManual.pdf` | © Spitfire Audio Holdings Ltd |
| 2.10 | HPD-20 kit descriptions and specification | `https://static.roland.com/assets/media/pdf/HPD-20_OM.pdf` | © Roland Corporation |
| 2.10 | HPD-20 bongo instrument names | `https://www.soundonsound.com/reviews/roland-handsonic-hpd20` | © Sound On Sound; **secondary source, single-sourced** |
| 2.10 | SPD-SX / SPD-30 absence of instrument list | `https://static.roland.com/assets/media/pdf/SPD-SX_OM.pdf`, `.../SPD-30_OM.pdf` | © Roland |
| 3 | `std` column | dossier `03-midi-standards.md` §3 (GM1/GM2/GS/XG union) | see that dossier |

### 6.2 Licensing conclusion for KITWARP

The only sources here that are safe to *reuse as identifiers* are **SMuFL glyph names** and
**MusicXML enumeration values / Standard Sounds IDs** — both are open-standard vocabularies
published for interoperability by the W3C Music Notation Community Group. Sibelius sound IDs,
Dorico technique names, VSL/Spitfire/NI/Toontrack patch names and Roland instrument names are
all vendor namespaces: they are **evidence for the shape of the vocabulary and a source of
aliases for import**, and KITWARP must mint its own IDs. Recording "this vendor calls it X" in
an alias table is normal interoperability practice; adopting the vendor's namespace as the
pivot is not.

---

## 7. Explicitly UNVERIFIED

1. **Dorico's enumerated playing/playback technique list** — not obtained (§1.2). The technique
   names attributed to Dorico in §2.5 are the only ones documented in retrievable text.
2. **Roland HPD-20 (850 instruments) and SPD-SX instrument/wave lists** — not obtained. The
   naming grammar inferred in §2.10 rests on one secondary source (Sound On Sound) plus the
   kit-description prose in the official manual.
3. **Roland Octapad SPD-30 instrument list** — not obtained; the manual contains no such list.
4. **VSL `Rim SOS` / `Rim SOSOR`** — the expansions are not given in the VSL manual. Probable
   readings ("stick on stick", "stick on stick on rim") are **speculation and are not asserted**.
5. **Whether the SPD-SX has any fixed instrument vocabulary at all** — it is a sample player;
   the manual documents only a user WAVE LIST. Unresolved.
6. **`macho`/`hembra` orientation** — NI's Cuba manual states bongos are "one larger drum,
   macho (male), and one smaller drum, hembra (female)". Several percussion references use the
   opposite convention, and for **timbales** the convention is generally the reverse of bongos.
   This is flagged in §5.3 as a decision to make deliberately; the present dossier asserts only
   what the NI manual says.
7. **Sibelius modifier tokens vs sample-set names** — the filter in §2.4.2 is heuristic. Tokens
   such as `coco rico`, `big head`, `monster`, `ap1`, `prl`, `gladstone` are believed to be
   sample-set names, not articulations, but this was not confirmed against an Avid list.
8. **Toontrack EZX Latin Percussion notes 111–118** are asserted here to be an octave-duplicate
   alias block of notes 102–109 on the basis of identical names; Toontrack has not documented
   this.
9. **Spitfire per-instrument technique names** — not obtained; §2.9 lists instruments only.
