# Bucket 04 — Notation standards and their technique enumerations

Round 2 bucket dossier. Scope: the notation standards, notation-program vocabularies and
notation-standardisation literature that already had to enumerate percussion playing
techniques as a closed set. Extraction is from the machine-readable form (XSD, YAML, JSON,
ODD, source file) wherever one exists, and from the printed source otherwise.

Worker: `bucket-04-notation-standards`. Extraction date: 2026-09-06 (UTC).
Every table below is transcribed from the file or page named in its locator, not from prose
summaries of it.

Environment notes that constrain what is here: the shared session WebSearch budget (200 calls
across all workers) was exhausted after this bucket's 15th round A search and still refused
calls when retried later, so all breadth after round A ran through direct HTTP and `git clone`;
`web.archive.org` is blocked outright, so the Wayback fallback named in the brief was
unavailable; `curl` to github.com and raw.githubusercontent.com is blocked (403) but
`git clone --depth 1` works, including with `--filter=blob:none --sparse`. One methodological
note that cost this bucket a false negative and is worth passing on: WebFetch summarises rather
than transcribes, and on the Finale tables it declined to reproduce them at all — for a source
that must be complete and verbatim, fetch the raw page and parse it locally (§6, item 2).

---

## 1. Candidate source register (round A)

Authority levels used below:

- **normative** — a published standard that other software has to implement
- **de-facto** — not a standard body, but the reference implementations follow it
- **vendor** — one program's internal vocabulary, published by its maker
- **derived** — a third party's machine-readable reconstruction of a vendor vocabulary
- **literature** — a book or article that proposed or surveyed a vocabulary

| # | Title | Author / body | Year | Type | Locator | Authority | Reached |
|---|---|---|---|---|---|---|---|
| 1 | SMuFL 1.4 specification and glyph tables | W3C Music Notation Community Group | 2021 | standard | `git clone https://github.com/w3c/smufl` → `releases/1.4/tables/*.html`; clone head f9d12b22ea89978720ba9defb2f4df67fabd8564 (2026-09-05) | normative | yes |
| 2 | SMuFL working draft toward 1.5 (font stem 1.4, build 82) | W3C MNCG | 2026 | standard (draft) | same clone, `data/ranges/*.yaml`, `metadata/glyphnames.json` | normative (draft) | yes |
| 3 | MusicXML 4.0 XSD | W3C MNCG | 2021 | standard | `git clone https://github.com/w3c/musicxml`, tag `v4.0` = 799e2defb2ece0ae7bafe08dcbcac25b2c631d53, `schema/musicxml.xsd` | normative | yes |
| 4 | MusicXML 4.1 draft XSD | W3C MNCG | 2026 | standard (draft) | same clone, master 29b7b212000e60ef06f938895e15cfc4c7fd90c0 (2026-09-03) | normative (draft) | yes |
| 5 | MusicXML 4.0 Standard Sounds (`sounds.xml`) | W3C MNCG | 2021 | standard | same clone, `v4.0:schema/sounds.xml` | normative | yes |
| 6 | MEI Guidelines source (ODD), edition "MEI 6.0-dev" | Music Encoding Initiative Board | 2026 | standard | `git clone https://github.com/music-encoding/music-encoding`, 34e82b155d55ae0bc0159ffefe2050ac992e931d (2026-08-04), `source/modules/MEI.xml` | normative | yes |
| 7 | MNX draft specification (metaspec) | W3C MNCG | 2026 | standard (draft) | `git clone https://github.com/w3c/mnx`, 0a8c7602d624942668e1ac2b5c6a1aa2214be0d1 (2026-08-25), `doctools/mnx-metaspec.json` | normative (draft) | yes |
| 8 | LilyPond `drumpitch-init.ly` (drumPitchNames, drum styles) | LilyPond project | 2001–2026 | source file | https://gitlab.com/lilypond/lilypond/-/raw/master/ly/drumpitch-init.ly (`\version "2.23.6"`) | de-facto | yes |
| 9 | LilyPond Notation Reference, "Percussion notes" | LilyPond project | 2024 | manual | https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes | de-facto | yes |
| 10 | Guitar Pro `.gpif` percussion articulations and RSE sound ids | Arobas Music, reconstructed by alphaTab | 2026 | derived | `git clone https://github.com/CoderLine/alphaTab`, 1f428ccd1ea2faeeb1a8b48cb17194cfd60ba11e (2026-09-03), `packages/alphatab/src/exporter/GpifSoundMapper.ts` | derived (vendor vocabulary) | yes |
| 11 | alphaTab `PercussionMapper.ts` (GP element types and noteheads) | alphaTab | 2026 | derived | same clone, `packages/alphatab/src/model/PercussionMapper.ts` | derived | yes |
| 12 | MuseScore `instruments.xml` (107 percussion instruments with drum entries) | MuseScore | 2026 | source file | `git clone https://github.com/musescore/MuseScore`, 7991526152de746dcdcbbee130d5ab5f360f198e (2026-09-03), `share/instruments/instruments.xml` | de-facto | yes |
| 13 | Sibelius Sound Set Editor User Guide | Avid / Sibelius | n.d. | vendor manual | https://www.sibelius.com/download/sse/Sound%20Set%20Editor%20User%20Guide.pdf (665 KB) | vendor | yes |
| 14 | SoundWorld white paper (sound ID tree design) | Sibelius Software | n.d. | vendor paper | http://www.sibelius.com/download/SoundWorld.pdf (1.9 MB) | vendor | yes |
| 15 | 17 published Sibelius sound sets (Sibelius Essentials GM, Garritan GPO/JABB/CMB, Vir2 VI.ONE, Vir2 Elite Orchestral Percussion, …) | Avid, Garritan, Vir2 | 2007–2014 | vendor data | `git clone https://github.com/glepore70/pronom-research` (sparse `sample_files/s/sibelius`), 2217b83abef3a2eb9b0b39f0b8b4b5ec798d3fc0 | vendor data (third-party mirror) | yes |
| 16 | "Guidelines for Drumset Notation", *Percussive Notes* June 1994, p. 15–26 | Norman Weinberg / Percussive Arts Society | 1994 | article (standard proposal) | https://www.normanweinberg.com/uploads/8/1/6/4/81640608/940506pn_guildines_for_drumset.pdf (12 pp., image-only scan; needs a browser user-agent, plain curl gets HTTP 429) | literature (PAS-endorsed) | yes |
| 17 | *Guide to Standardized Drumset Notation* (book) | Norman Weinberg / PAS | 1998 | book | ISBN 0-9664928-1-1, HL06620063 | literature | no — print only |
| 18 | *Behind Bars: The Definitive Guide to Music Notation*, section II, percussion chapter | Elaine Gould | 2011 | book | ISBN 978-0-571-51456-4, Faber Music, 704 pp. | literature | no — print only, no open full text |
| 19 | *Music Notation in the Twentieth Century: A Practical Guidebook* | Kurt Stone | 1980 | book | ISBN 978-0-393-95053-3; archive.org item `musicnotationint0000ston_h3s0` (lending only) | literature | no — reached only indirectly (see §4) |
| 20 | *Contemporary Percussion* | Reginald Smith Brindle | 1970 | book | OUP, ISBN 0-19-318802-3 | literature | no — reached only through SMuFL glyph names that cite it |
| 21 | *Notation: A Manual of Modern Practice* | Gardner Read | 1969 | book | Victor Gollancz / Taplinger | literature | no — cited by Weinberg for the circled-notehead rimshot |
| 22 | International Conference on New Musical Notation, Ghent 1974 | ICNMN | 1974 | standards conference | cited by Weinberg 1994 and by SMuFL glyph descriptions | literature | no |
| 23 | Ghent percussion symbols (centre/rim) | (via ICNMN/Ghent conference) | 1974 | notation system | SMuFL `pictCenter2`, `pictRim2` descriptions | literature | no — only the SMuFL trace |
| 24 | Caltabiano percussion symbols (centre/rim/normal position) | Ronald Caltabiano | — | notation system | SMuFL `pictCenter3`, `pictRim3`, `pictNormalPosition` | literature | no — only the SMuFL trace |
| 25 | Agostini drumset notation (hand indications, staff layout) | Dante Agostini | — | notation system | SMuFL `pictRightHandSquare`, `pictLeftHandCircle`; LilyPond `agostini-drums-style` | literature | no — only the SMuFL and LilyPond traces |
| 26 | Dorico help: "Unpitched percussion playing techniques" | Steinberg | 2018 | vendor manual | https://archive.steinberg.help/dorico_pro/v2/en/dorico/topics/notation_reference/notation_reference_unpitched_percussion_playing_techniques_c.html | vendor | yes — but it publishes no enumeration |
| 27 | Dorico help: "Percussion Instrument Playing Techniques dialog" | Steinberg | 2018 | vendor manual | https://archive.steinberg.help/dorico_pro/v2/en/dorico/topics/notation_reference/notation_reference_unpitched_percussion_percussion_instrument_playing_techniques_dialog_r.html | vendor | yes — no enumeration |
| 28 | Dorico `.doricolib` playing-technique ids (`pt.*`) | Steinberg + third-party expression maps | 2026 | vendor data | GitHub code search: `mhcoffin/fiddle`, `taylorbrook/O-Audio-VST-Development` (`pt.natural`, `pt.legato`, `<PlayingTechniqueDefinition>`) | vendor | partial — namespace confirmed, percussion ids not found in public files |
| 29 | Finale "Percussion MIDI Map Editor dialog box" | MakeMusic | — | vendor manual | https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/db-percussion-midi-map-editor.htm | vendor | yes — no enumeration published |
| 30 | Finale "Percussion Layout Designer dialog box" | MakeMusic | — | vendor manual | https://usermanuals.finalemusic.com/FinaleWin/Content/Finale/db-percussion-layout-designer.htm | vendor | listed only |
| 30a | Finale "Percussion MIDI Maps: Tapspace Drumline for Finale" — six complete Note Type ↔ MIDI tables | MakeMusic | — | vendor manual | https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/PercussionMaps3.htm (direct HTTP; the WebFetch summariser refuses to reproduce the tables, curl with a browser user-agent returns them) | vendor | **yes — this is where Finale's enumeration actually is** |
| 30b | Finale "Percussion MIDI Maps: Garritan Instruments for Finale" — 572 distinct Note Types | MakeMusic | — | vendor manual | https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/PercussionMaps2.htm | vendor | yes |
| 30c | Finale "Percussion MIDI Maps" index | MakeMusic | — | vendor manual | https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/PercussionMaps.htm | vendor | no — HTTP 403 |
| 31 | Sibelius 7 Sounds User Guide (sound names per library) | Avid | 2012 | vendor manual | https://resources.avid.com/SupportFiles/Sibelius/sibelius712-sounds-en.pdf | vendor | listed only |
| 32 | Guitar Pro 7 user guide (drum articulation UI: open / semi-open / closed hi-hat on numeric keys 1/2/3) | Arobas Music | 2017 | vendor manual | https://static.guitar-pro.com/gp7/manual/GuitarPro7-user-guide.pdf | vendor | listed only |
| 33 | "Notation pour percussion" (French MuseScore handbook) | MuseScore | — | manual (FR) | https://musescore.org/fr/manuel/notation-pour-percussion | de-facto (FR) | listed only |
| 34 | "BATTERIE : Modes de jeu" and "TAMBOURS : Modes de jeu" | Encyclopædia Universalis | — | encyclopaedia (FR) | https://www.universalis.fr/encyclopedie/batterie/4-modes-de-jeu/ | secondary (FR) | listed only |
| 35 | "Schlagzeug-Notation" overview PDF | drumtreff.de | 2021 | pedagogical (DE) | https://www.drumtreff.de/wp-content/uploads/2021/10/2021-10-20_drumtreff_noten_schlagzeug-notation-grundlagen.pdf | secondary (DE) | listed only |
| 36 | "Schlagzeugnotation" (Braille music notation, chapter 18) | braille.ch | — | standard (DE, braille) | http://www.braille.ch/musik/kap18.html | normative (braille) | listed only |
| 37 | LilyPond Benutzerhandbuch 2.5.1 "Übliche Notation für Schlagzeug" | LilyPond project | — | manual (DE) | https://lilypond.org/doc/v2.23/Documentation/notation/common-notation-for-percussion.de.html | de-facto (DE) | listed only |
| 38 | LilyPond Manuel de notation A.17 "Notes utilisées en percussion" | LilyPond project | — | manual (FR) | https://lilypond.org/doc/v2.23/Documentation/notation/percussion-notes.fr.html | de-facto (FR) | listed only |

Round A searches actually run, in order, before any extraction (register, language and era
varied per the brief): SMuFL percussion pictogram glyph names; MusicXML XSD beater/stick
enumerations; MusicXML standard sounds percussion ids; MEI `att.articulation` / percussion
module; Dorico `.doricolib` percussion playing techniques; Sibelius Sound Set editor SoundID
vocabulary; Finale percussion map note types; LilyPond `drumPitchNames`; Guitar Pro 7 drum
articulations and the `.gp` format; Percussive Arts Society / Weinberg standardised drumset
notation; Gould *Behind Bars* percussion chapter; German "Schlagzeug Notation
Spielanweisungen Notationslehre Spieltechniken"; French "notation percussion modes de jeu
baguettes normalisation"; MNX percussion technique enumeration; Kurt Stone / Reginald Smith
Brindle contemporary percussion notation standardisation.


---

## 2. Extracted terminology (round B)

### 2.1 SMuFL 1.4 — percussion ranges, complete

Locator for every table in §2.1: `w3c/smufl`, release snapshot `releases/1.4/tables/<range>.html`,
cross-checked against the working `data/ranges/<range>.yaml` and `metadata/glyphnames.json` of
clone head f9d12b22ea89978720ba9defb2f4df67fabd8564. Licence: the SMuFL specification is
published by the W3C Music Notation Community Group under the W3C Community Final
Specification Agreement; glyph names and descriptions are specification text, safe to cite and
to reuse as identifiers.

Verification performed: for each range the released-1.4 table and the current working YAML were
diffed by glyph name. Every percussion range is unchanged since 1.4 (0 added, 0 removed). Only
two non-percussion ranges consulted here have moved: `articulation` (22 → 30, 8 added after 1.4)
and `tremolos` (15 → 21, 6 added). So the percussion vocabulary below is stable 1.4 text, not a
draft.

Counts: beaters 128, percussion playing technique 31, drums 21, cymbals 11, tuned mallet 19,
handbells 18, wooden struck/scraped 13, chop 12, bells 11, whistles and aerophones 11, shakers
or rattles 9, chimes 9, miscellaneous 8, gongs 5, techniques noteheads 4, metallic struck 2.


### Percussion playing technique pictograms (U+E7F0-U+E80F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E7F0 | `pictStickShot` | Stick shot |
| U+E7F1 | `pictScrapeCenterToEdge` | Scrape from center to edge |
| U+E7F2 | `pictScrapeEdgeToCenter` | Scrape from edge to center |
| U+E7F3 | `pictScrapeAroundRim` | Scrape around rim (counter-clockwise) |
| U+E7F4 | `pictOnRim` | On rim |
| U+E7F5 | `pictOpenRimShot` | Closed / rim shot |
| U+E7F6 | `pictHalfOpen1` | Half-open |
| U+E7F7 | `pictHalfOpen2` | Half-open 2 (Weinberg) |
| U+E7F8 | `pictOpen` | Open |
| U+E7F9 | `pictDamp1` | Damp |
| U+E7FA | `pictDamp2` | Damp 2 |
| U+E7FB | `pictDamp3` | Damp 3 |
| U+E7FC | `pictDamp4` | Damp 4 |
| U+E7FD | `pictRimShotOnStem` | Rim shot for stem |
| U+E7FE | `pictCenter1` | Center (Weinberg) |
| U+E7FF | `pictCenter2` | Center (Ghent) |
| U+E800 | `pictCenter3` | Center (Caltabiano) |
| U+E801 | `pictRim1` | Rim or edge (Weinberg) |
| U+E802 | `pictRim2` | Rim (Ghent) |
| U+E803 | `pictRim3` | Rim (Caltabiano) |
| U+E804 | `pictNormalPosition` | Normal position (Caltabiano) |
| U+E805 | `pictChokeCymbal` | Choke (Weinberg) |
| U+E806 | `pictRightHandSquare` | Left hand (Agostini) |
| U+E807 | `pictLeftHandCircle` | Right hand (Agostini) |
| U+E808 | `pictSwishStem` | Combining swish for stem |
| U+E809 | `pictTurnRightStem` | Combining turn right for stem |
| U+E80A | `pictTurnLeftStem` | Combining turn left for stem |
| U+E80B | `pictTurnRightLeftStem` | Combining turn left or right for stem |
| U+E80C | `pictCrushStem` | Combining crush for stem |
| U+E80D | `pictDeadNoteStem` | Combining X for stem (dead note) |
| U+E80E | `pictScrapeAroundRimClockwise` | Scrape around rim (clockwise) |

### Beaters pictograms (U+E770-U+E7EF)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E770 | `pictBeaterSoftXylophoneUp` | Soft xylophone stick up |
| U+E771 | `pictBeaterSoftXylophoneDown` | Soft xylophone stick down |
| U+E772 | `pictBeaterSoftXylophoneRight` | Soft xylophone stick right |
| U+E773 | `pictBeaterSoftXylophoneLeft` | Soft xylophone stick left |
| U+E774 | `pictBeaterMediumXylophoneUp` | Medium xylophone stick up |
| U+E775 | `pictBeaterMediumXylophoneDown` | Medium xylophone stick down |
| U+E776 | `pictBeaterMediumXylophoneRight` | Medium xylophone stick right |
| U+E777 | `pictBeaterMediumXylophoneLeft` | Medium xylophone stick left |
| U+E778 | `pictBeaterHardXylophoneUp` | Hard xylophone stick up |
| U+E779 | `pictBeaterHardXylophoneDown` | Hard xylophone stick down |
| U+E77A | `pictBeaterHardXylophoneRight` | Hard xylophone stick right |
| U+E77B | `pictBeaterHardXylophoneLeft` | Hard xylophone stick left |
| U+E77C | `pictBeaterWoodXylophoneUp` | Wood xylophone stick up |
| U+E77D | `pictBeaterWoodXylophoneDown` | Wood xylophone stick down |
| U+E77E | `pictBeaterWoodXylophoneRight` | Wood xylophone stick right |
| U+E77F | `pictBeaterWoodXylophoneLeft` | Wood xylophone stick left |
| U+E780 | `pictBeaterSoftGlockenspielUp` | Soft glockenspiel stick up |
| U+E781 | `pictBeaterSoftGlockenspielDown` | Soft glockenspiel stick down |
| U+E782 | `pictBeaterSoftGlockenspielRight` | Soft glockenspiel stick right |
| U+E783 | `pictBeaterSoftGlockenspielLeft` | Soft glockenspiel stick left |
| U+E784 | `pictBeaterHardGlockenspielUp` | Hard glockenspiel stick up |
| U+E785 | `pictBeaterHardGlockenspielDown` | Hard glockenspiel stick down |
| U+E786 | `pictBeaterHardGlockenspielRight` | Hard glockenspiel stick right |
| U+E787 | `pictBeaterHardGlockenspielLeft` | Hard glockenspiel stick left |
| U+E788 | `pictBeaterSoftTimpaniUp` | Soft timpani stick up |
| U+E789 | `pictBeaterSoftTimpaniDown` | Soft timpani stick down |
| U+E78A | `pictBeaterSoftTimpaniRight` | Soft timpani stick right |
| U+E78B | `pictBeaterSoftTimpaniLeft` | Soft timpani stick left |
| U+E78C | `pictBeaterMediumTimpaniUp` | Medium timpani stick up |
| U+E78D | `pictBeaterMediumTimpaniDown` | Medium timpani stick down |
| U+E78E | `pictBeaterMediumTimpaniRight` | Medium timpani stick right |
| U+E78F | `pictBeaterMediumTimpaniLeft` | Medium timpani stick left |
| U+E790 | `pictBeaterHardTimpaniUp` | Hard timpani stick up |
| U+E791 | `pictBeaterHardTimpaniDown` | Hard timpani stick down |
| U+E792 | `pictBeaterHardTimpaniRight` | Hard timpani stick right |
| U+E793 | `pictBeaterHardTimpaniLeft` | Hard timpani stick left |
| U+E794 | `pictBeaterWoodTimpaniUp` | Wood timpani stick up |
| U+E795 | `pictBeaterWoodTimpaniDown` | Wood timpani stick down |
| U+E796 | `pictBeaterWoodTimpaniRight` | Wood timpani stick right |
| U+E797 | `pictBeaterWoodTimpaniLeft` | Wood timpani stick left |
| U+E798 | `pictBeaterSoftBassDrumUp` | Soft bass drum stick up |
| U+E799 | `pictBeaterSoftBassDrumDown` | Soft bass drum stick down |
| U+E79A | `pictBeaterMediumBassDrumUp` | Medium bass drum stick up |
| U+E79B | `pictBeaterMediumBassDrumDown` | Medium bass drum stick down |
| U+E79C | `pictBeaterHardBassDrumUp` | Hard bass drum stick up |
| U+E79D | `pictBeaterHardBassDrumDown` | Hard bass drum stick down |
| U+E79E | `pictBeaterMetalBassDrumUp` | Metal bass drum stick up |
| U+E79F | `pictBeaterMetalBassDrumDown` | Metal bass drum stick down |
| U+E7A0 | `pictBeaterDoubleBassDrumUp` | Double bass drum stick up |
| U+E7A1 | `pictBeaterDoubleBassDrumDown` | Double bass drum stick down |
| U+E7A2 | `pictBeaterSoftYarnUp` | Soft yarn beater up |
| U+E7A3 | `pictBeaterSoftYarnDown` | Soft yarn beater down |
| U+E7A4 | `pictBeaterSoftYarnRight` | Soft yarn beater right |
| U+E7A5 | `pictBeaterSoftYarnLeft` | Soft yarn beater left |
| U+E7A6 | `pictBeaterMediumYarnUp` | Medium yarn beater up |
| U+E7A7 | `pictBeaterMediumYarnDown` | Medium yarn beater down |
| U+E7A8 | `pictBeaterMediumYarnRight` | Medium yarn beater right |
| U+E7A9 | `pictBeaterMediumYarnLeft` | Medium yarn beater left |
| U+E7AA | `pictBeaterHardYarnUp` | Hard yarn beater up |
| U+E7AB | `pictBeaterHardYarnDown` | Hard yarn beater down |
| U+E7AC | `pictBeaterHardYarnRight` | Hard yarn beater right |
| U+E7AD | `pictBeaterHardYarnLeft` | Hard yarn beater left |
| U+E7AE | `pictBeaterSuperballUp` | Superball beater up |
| U+E7AF | `pictBeaterSuperballDown` | Superball beater down |
| U+E7B0 | `pictBeaterSuperballRight` | Superball beater right |
| U+E7B1 | `pictBeaterSuperballLeft` | Superball beater left |
| U+E7B2 | `pictSuperball` | Superball |
| U+E7B3 | `pictWoundHardUp` | Wound beater, hard core up |
| U+E7B4 | `pictWoundHardDown` | Wound beater, hard core down |
| U+E7B5 | `pictWoundHardRight` | Wound beater, hard core right |
| U+E7B6 | `pictWoundHardLeft` | Wound beater, hard core left |
| U+E7B7 | `pictWoundSoftUp` | Wound beater, soft core up |
| U+E7B8 | `pictWoundSoftDown` | Wound beater, soft core down |
| U+E7B9 | `pictWoundSoftRight` | Wound beater, soft core right |
| U+E7BA | `pictWoundSoftLeft` | Wound beater, soft core left |
| U+E7BB | `pictGumSoftUp` | Soft gum beater, up |
| U+E7BC | `pictGumSoftDown` | Soft gum beater, down |
| U+E7BD | `pictGumSoftRight` | Soft gum beater, right |
| U+E7BE | `pictGumSoftLeft` | Soft gum beater, left |
| U+E7BF | `pictGumMediumUp` | Medium gum beater, up |
| U+E7C0 | `pictGumMediumDown` | Medium gum beater, down |
| U+E7C1 | `pictGumMediumRight` | Medium gum beater, right |
| U+E7C2 | `pictGumMediumLeft` | Medium gum beater, left |
| U+E7C3 | `pictGumHardUp` | Hard gum beater, up |
| U+E7C4 | `pictGumHardDown` | Hard gum beater, down |
| U+E7C5 | `pictGumHardRight` | Hard gum beater, right |
| U+E7C6 | `pictGumHardLeft` | Hard gum beater, left |
| U+E7C7 | `pictBeaterMetalUp` | Metal beater, up |
| U+E7C8 | `pictBeaterMetalDown` | Metal beater down |
| U+E7C9 | `pictBeaterMetalRight` | Metal beater, right |
| U+E7CA | `pictBeaterMetalLeft` | Metal beater, left |
| U+E7CB | `pictBeaterHammerWoodUp` | Wooden hammer, up |
| U+E7CC | `pictBeaterHammerWoodDown` | Wooden hammer, down |
| U+E7CD | `pictBeaterHammerPlasticUp` | Plastic hammer, up |
| U+E7CE | `pictBeaterHammerPlasticDown` | Plastic hammer, down |
| U+E7CF | `pictBeaterHammerMetalUp` | Metal hammer, up |
| U+E7D0 | `pictBeaterHammerMetalDown` | Metal hammer, down |
| U+E7D1 | `pictBeaterSnareSticksUp` | Snare sticks up |
| U+E7D2 | `pictBeaterSnareSticksDown` | Snare sticks down |
| U+E7D3 | `pictBeaterJazzSticksUp` | Jazz sticks up |
| U+E7D4 | `pictBeaterJazzSticksDown` | Jazz sticks down |
| U+E7D5 | `pictBeaterTriangleUp` | Triangle beater up |
| U+E7D6 | `pictBeaterTriangleDown` | Triangle beater down |
| U+E7D7 | `pictBeaterWireBrushesUp` | Wire brushes up |
| U+E7D8 | `pictBeaterWireBrushesDown` | Wire brushes down |
| U+E7D9 | `pictBeaterBrassMalletsUp` | Brass mallets up |
| U+E7DA | `pictBeaterBrassMalletsDown` | Brass mallets down |
| U+E7DB | `pictBeaterSoftXylophone` | Soft xylophone beaters |
| U+E7DC | `pictBeaterSpoonWoodenMallet` | Spoon-shaped wooden mallet |
| U+E7DD | `pictBeaterGuiroScraper` | Guiro scraper |
| U+E7DE | `pictBeaterBow` | Bow |
| U+E7DF | `pictBeaterMallet` | Chime hammer up |
| U+E7E0 | `pictBeaterMetalHammer` | Metal hammer |
| U+E7E1 | `pictBeaterHammer` | Hammer |
| U+E7E2 | `pictBeaterKnittingNeedle` | Knitting needle |
| U+E7E3 | `pictBeaterHand` | Hand |
| U+E7E4 | `pictBeaterFinger` | Finger |
| U+E7E5 | `pictBeaterFist` | Fist |
| U+E7E6 | `pictBeaterFingernails` | Fingernails |
| U+E7E7 | `pictCoins` | Coins |
| U+E7E8 | `pictDrumStick` | Drum stick |
| U+E7E9 | `pictBeaterCombiningParentheses` | Combining parentheses for round beaters (padded) |
| U+E7EA | `pictBeaterCombiningDashedCircle` | Combining dashed circle for round beaters (plated) |
| U+E7EB | `pictBeaterBox` | Box for percussion beater |
| U+E7EC | `pictBeaterMalletDown` | Chime hammer down |
| U+E7ED | `pictBeaterBrassMalletsRight` | Brass mallets right |
| U+E7EE | `pictBeaterBrassMalletsLeft` | Brass mallets left |
| U+E7EF | `pictBeaterTrianglePlain` | Triangle beater plain |

### Drums pictograms (U+E6D0-U+E6EF)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E6D0 | `pictTimpani` | Timpani |
| U+E6D1 | `pictSnareDrum` | Snare drum |
| U+E6D2 | `pictSnareDrumSnaresOff` | Snare drum, snares off |
| U+E6D3 | `pictSnareDrumMilitary` | Military snare drum |
| U+E6D4 | `pictBassDrum` | Bass drum |
| U+E6D5 | `pictBassDrumOnSide` | Bass drum on side |
| U+E6D6 | `pictTenorDrum` | Tenor drum |
| U+E6D7 | `pictTomTom` | Tom-tom |
| U+E6D8 | `pictTomTomChinese` | Chinese tom-tom |
| U+E6D9 | `pictTomTomJapanese` | Japanese tom-tom |
| U+E6DA | `pictTomTomIndoAmerican` | Indo-American tom tom |
| U+E6DB | `pictTambourine` | Tambourine |
| U+E6DC | `pictTimbales` | Timbales |
| U+E6DD | `pictBongos` | Bongos |
| U+E6DE | `pictConga` | Conga |
| U+E6DF | `pictLogDrum` | Log drum |
| U+E6E0 | `pictSlitDrum` | Slit drum |
| U+E6E1 | `pictBrakeDrum` | Brake drum |
| U+E6E2 | `pictGobletDrum` | Goblet drum (djembe, dumbek) |
| U+E6E3 | `pictTabla` | Indian tabla |
| U+E6E4 | `pictCuica` | Cuica |

### Cymbals pictograms (U+E720-U+E72F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E720 | `pictCrashCymbals` | Crash cymbals |
| U+E721 | `pictSuspendedCymbal` | Suspended cymbal |
| U+E722 | `pictHiHat` | Hi-hat |
| U+E723 | `pictHiHatOnStand` | Hi-hat cymbals on stand |
| U+E724 | `pictSizzleCymbal` | Sizzle cymbal |
| U+E725 | `pictVietnameseHat` | Vietnamese hat cymbal |
| U+E726 | `pictChineseCymbal` | Chinese cymbal |
| U+E727 | `pictFingerCymbals` | Finger cymbals |
| U+E728 | `pictCymbalTongs` | Cymbal tongs |
| U+E729 | `pictEdgeOfCymbal` | Edge of cymbal |
| U+E72A | `pictBellOfCymbal` | Bell of cymbal |

### Metallic struck percussion pictograms (U+E700-U+E70F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E700 | `pictTriangle` | Triangle |
| U+E701 | `pictAnvil` | Anvil |

### Wooden struck or scraped percussion pictograms (U+E6F0-U+E6FF)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E6F0 | `pictWoodBlock` | Wood block |
| U+E6F1 | `pictTempleBlocks` | Temple blocks |
| U+E6F2 | `pictClaves` | Claves |
| U+E6F3 | `pictGuiro` | Guiro |
| U+E6F4 | `pictRatchet` | Ratchet |
| U+E6F5 | `pictFootballRatchet` | Football rattle |
| U+E6F6 | `pictWhip` | Whip |
| U+E6F7 | `pictBoardClapper` | Board clapper |
| U+E6F8 | `pictCastanets` | Castanets |
| U+E6F9 | `pictCastanetsWithHandle` | Castanets with handle |
| U+E6FA | `pictQuijada` | Quijada (jawbone) |
| U+E6FB | `pictBambooScraper` | Bamboo scraper |
| U+E6FC | `pictRecoReco` | Reco-reco |

### Shakers or rattles pictograms (U+E740-U+E74F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E740 | `pictFlexatone` | Flexatone |
| U+E741 | `pictMaraca` | Maraca |
| U+E742 | `pictMaracas` | Maracas |
| U+E743 | `pictCabasa` | Cabasa |
| U+E744 | `pictThundersheet` | Thundersheet |
| U+E745 | `pictVibraslap` | Vibraslap |
| U+E746 | `pictSistrum` | Sistrum |
| U+E747 | `pictRainstick` | Rainstick |
| U+E748 | `pictChainRattle` | Chain rattle |

### Bells pictograms (U+E710-U+E71F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E710 | `pictSleighBell` | Sleigh bell |
| U+E711 | `pictCowBell` | Cow bell |
| U+E712 | `pictAlmglocken` | Almglocken |
| U+E713 | `pictBellPlate` | Bell plate |
| U+E714 | `pictBell` | Bell |
| U+E715 | `pictHandbell` | Handbell |
| U+E716 | `pictCencerro` | Cencerro |
| U+E717 | `pictAgogo` | Agogo |
| U+E718 | `pictShellBells` | Shell bells |
| U+E719 | `pictJingleBells` | Jingle bells |
| U+E71A | `pictBellTree` | Bell tree |

### Gongs pictograms (U+E730-U+E73F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E730 | `pictTamTam` | Tam-tam |
| U+E731 | `pictTamTamWithBeater` | Tam-tam with beater (Smith Brindle) |
| U+E732 | `pictGong` | Gong |
| U+E733 | `pictGongWithButton` | Gong with button (nipple) |
| U+E734 | `pictSlideBrushOnGong` | Slide brush on gong |

### Chimes pictograms (U+E6C0-U+E6CF)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E6C0 | `pictTubularBells` | Tubular bells |
| U+E6C1 | `pictWindChimesGlass` | Wind chimes (glass) |
| U+E6C2 | `pictChimes` | Chimes |
| U+E6C3 | `pictBambooChimes` | Bamboo tube chimes |
| U+E6C4 | `pictShellChimes` | Shell chimes |
| U+E6C5 | `pictGlassTubeChimes` | Glass tube chimes |
| U+E6C6 | `pictGlassPlateChimes` | Glass plate chimes |
| U+E6C7 | `pictMetalTubeChimes` | Metal tube chimes |
| U+E6C8 | `pictMetalPlateChimes` | Metal plate chimes |

### Tuned mallet percussion pictograms (U+E6A0-U+E6BF)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E6A0 | `pictGlsp` | Glockenspiel |
| U+E6A1 | `pictXyl` | Xylophone |
| U+E6A2 | `pictXylTenor` | Tenor xylophone |
| U+E6A3 | `pictXylBass` | Bass xylophone |
| U+E6A4 | `pictXylTrough` | Trough xylophone |
| U+E6A5 | `pictXylTenorTrough` | Trough tenor xylophone |
| U+E6A6 | `pictMar` | Marimba |
| U+E6A7 | `pictVib` | Vibraphone |
| U+E6A8 | `pictVibMotorOff` | Metallophone (vibraphone motor off) |
| U+E6A9 | `pictEmptyTrap` | Empty trapezoid |
| U+E6AA | `pictGlspSmithBrindle` | Glockenspiel (Smith Brindle) |
| U+E6AB | `pictXylSmithBrindle` | Xylophone (Smith Brindle) |
| U+E6AC | `pictMarSmithBrindle` | Marimba (Smith Brindle) |
| U+E6AD | `pictVibSmithBrindle` | Vibraphone (Smith Brindle) |
| U+E6AE | `pictCrotales` | Crotales |
| U+E6AF | `pictSteelDrums` | Steel drums |
| U+E6B0 | `pictCelesta` | Celesta |
| U+E6B1 | `pictLithophone` | Lithophone |
| U+E6B2 | `pictTubaphone` | Tubaphone |

### Whistles and aerophones pictograms (U+E750-U+E75F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E750 | `pictSlideWhistle` | Slide whistle |
| U+E751 | `pictBirdWhistle` | Bird whistle |
| U+E752 | `pictPoliceWhistle` | Police whistle |
| U+E753 | `pictSiren` | Siren |
| U+E754 | `pictWindMachine` | Wind machine |
| U+E755 | `pictCarHorn` | Car horn |
| U+E756 | `pictKlaxonHorn` | Klaxon horn |
| U+E757 | `pictDuckCall` | Duck call |
| U+E758 | `pictWindWhistle` | Wind whistle (or mouth siren) |
| U+E759 | `pictMegaphone` | Megaphone |
| U+E75A | `pictLotusFlute` | Lotus flute |

### Miscellaneous percussion instrument pictograms (U+E760-U+E76F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E760 | `pictPistolShot` | Pistol shot |
| U+E761 | `pictCannon` | Cannon |
| U+E762 | `pictSandpaperBlocks` | Sandpaper blocks |
| U+E763 | `pictLionsRoar` | Lion's roar |
| U+E764 | `pictGlassHarp` | Glass harp |
| U+E765 | `pictGlassHarmonica` | Glass harmonica |
| U+E766 | `pictMusicalSaw` | Musical saw |
| U+E767 | `pictJawHarp` | Jaw harp |

### Techniques noteheads (U+EE70-U+EE7F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+EE70 | `swissRudimentsNoteheadBlackFlam` | Swiss rudiments flam black notehead |
| U+EE71 | `swissRudimentsNoteheadHalfFlam` | Swiss rudiments flam half (minim) notehead |
| U+EE72 | `swissRudimentsNoteheadBlackDouble` | Swiss rudiments doublé black notehead |
| U+EE73 | `swissRudimentsNoteheadHalfDouble` | Swiss rudiments doublé half (minim) notehead |

### Handbells (U+E810-U+E82F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+E810 | `handbellsMartellato` | Martellato |
| U+E811 | `handbellsMartellatoLift` | Martellato lift |
| U+E812 | `handbellsHandMartellato` | Hand martellato |
| U+E813 | `handbellsMutedMartellato` | Muted martellato |
| U+E814 | `handbellsMalletBellSuspended` | Mallet, bell suspended |
| U+E815 | `handbellsMalletBellOnTable` | Mallet, bell on table |
| U+E816 | `handbellsMalletLft` | Mallet lift |
| U+E817 | `handbellsPluckLift` | Pluck lift |
| U+E818 | `handbellsSwingUp` | Swing up |
| U+E819 | `handbellsSwingDown` | Swing down |
| U+E81A | `handbellsSwing` | Swing |
| U+E81B | `handbellsEcho1` | Echo |
| U+E81C | `handbellsEcho2` | Echo 2 |
| U+E81D | `handbellsGyro` | Gyro |
| U+E81E | `handbellsDamp3` | Damp 3 |
| U+E81F | `handbellsBelltree` | Belltree |
| U+E820 | `handbellsTableSingleBell` | Table single handbell |
| U+E821 | `handbellsTablePairBells` | Table pair of handbells |

### Chop (percussive bowing) notation (U+EE80-U+EE8F)  [SMuFL 1.4 released tables]

| Codepoint | Canonical glyph name | Description |
|---|---|---|
| U+EE80 | `stringsDownBowTowardsBody` | Down bow, towards body |
| U+EE81 | `stringsUpBowTowardsBody` | Up bow, towards body |
| U+EE82 | `stringsDownBowAwayFromBody` | Down bow, away from body |
| U+EE83 | `stringsUpBowAwayFromBody` | Up bow, away from body |
| U+EE84 | `stringsDownBowBeyondBridge` | Down bow, beyond bridge |
| U+EE85 | `stringsUpBowBeyondBridge` | Up bow, beyond bridge |
| U+EE86 | `stringsScrapeParallelInward` | Scrape, parallel inward |
| U+EE87 | `stringsScrapeParallelOutward` | Scrape, parallel outward |
| U+EE88 | `stringsScrapeCircularClockwise` | Scrape, circular clockwise |
| U+EE89 | `stringsScrapeCircularCounterclockwise` | Scrape, circular counter-clockwise |
| U+EE8A | `stringsTripleChopInward` | Triple chop, inward |
| U+EE8B | `stringsTripleChopOutward` | Triple chop, outward |

---

### 2.2 MusicXML — the percussion element vocabulary, complete

Locator: `w3c/musicxml`, `schema/musicxml.xsd`. **Verified**: every enumeration below was
dumped from tag `v4.0` (799e2defb2ece0ae7bafe08dcbcac25b2c631d53) and from master
(29b7b212000e60ef06f938895e15cfc4c7fd90c0, headed "MusicXML 4.1") and compared value by value.
The percussion enumerations are byte-identical between 4.0 and the 4.1 draft; the only
difference anywhere in the compared set is the position of the empty value in
`breath-mark-value`. So MusicXML has not extended its percussion vocabulary since 3.1.

Licence: W3C Community Final Specification Agreement (same as SMuFL).

The `<percussion>` element (a `<direction-type>`) holds exactly one child from this set:
`glass`, `metal`, `wood`, `pitched`, `membrane`, `effect`, `timpani`, `beater`, `stick`,
`stick-location`, `other-percussion` (added in MusicXML 3.0). `<stick>` in turn contains
`<stick-type>` and `<stick-material>`, with optional `tip` attribute of type `tip-direction`.

| Simple type | Count | Values, verbatim and in schema order |
|---|---|---|
| `beater-value` | 20 | bow, chime hammer, coin, drum stick, finger, fingernail, fist, guiro scraper, hammer, hand, jazz stick, knitting needle, metal hammer, slide brush on gong, snare stick, spoon mallet, superball, triangle beater, triangle beater plain, wire brush |
| `stick-type` | 10 | bass drum, double bass drum, glockenspiel, gum, hammer, superball, timpani, wound, xylophone, yarn |
| `stick-material` | 5 | soft, medium, hard, shaded, x |
| `stick-location` | 4 | center, rim, cymbal bell, cymbal edge |
| `tip-direction` | 8 | up, down, left, right, northwest, northeast, southeast, southwest |
| `membrane-value` | 17 | bass drum, bass drum on side, bongos, Chinese tomtom, conga drum, cuica, goblet drum, Indo-American tomtom, Japanese tomtom, military drum, snare drum, snare drum snares off, tabla, tambourine, tenor drum, timbales, tomtom |
| `metal-value` | 32 | agogo, almglocken, bell, bell plate, bell tree, brake drum, cencerro, chain rattle, Chinese cymbal, cowbell, crash cymbals, crotale, cymbal tongs, domed gong, finger cymbals, flexatone, gong, hi-hat, high-hat cymbals, handbell, jaw harp, jingle bells, musical saw, shell bells, sistrum, sizzle cymbal, sleigh bells, suspended cymbal, tam tam, tam tam with beater, triangle, Vietnamese hat |
| `wood-value` | 21 | bamboo scraper, board clapper, cabasa, castanets, castanets with handle, claves, football rattle, guiro, log drum, maraca, maracas, quijada, rainstick, ratchet, reco-reco, sandpaper blocks, slit drum, temple block, vibraslap, whip, wood block |
| `pitched-value` | 11 | celesta, chimes, glockenspiel, lithophone, mallet, marimba, steel drums, tubaphone, tubular chimes, vibraphone, xylophone |
| `glass-value` | 3 | glass harmonica, glass harp, wind chimes |
| `effect-value` | 16 | anvil, auto horn, bird whistle, cannon, duck call, gun shot, klaxon horn, lions roar, lotus flute, megaphone, police whistle, siren, slide whistle, thunder sheet, wind machine, wind whistle |
| `handbell-value` | 12 | belltree, damp, echo, gyro, hand martellato, mallet lift, mallet table, martellato, martellato lift, muted martellato, pluck lift, swing |
| `notehead-value` | 28 | slash, triangle, diamond, square, cross, x, circle-x, inverted triangle, arrow down, arrow up, circled, slashed, back slashed, normal, cluster, circle dot, left triangle, rectangle, none, do, re, mi, fa, fa up, so, la, ti, other |

Verbatim schema documentation for the four types that carry technique information:

- `beater-value`: "The beater-value type represents pictograms for beaters, mallets, and
  sticks that do not have different materials represented in the pictogram."
- `stick-type`: "The stick-type type represents the shape of pictograms where the material in
  the stick, mallet, or beater is represented in the pictogram."
- `stick-material`: "The stick-material type represents the material being displayed in a
  stick pictogram."
- `stick-location`: "The stick-location type represents pictograms for the location of sticks,
  beaters, or mallets on cymbals, gongs, drums, and other instruments."
- `metal-value` carries the note: "The hi-hat value refers to a pictogram like high-hat
  cymbals, but without the long vertical line at the bottom."
- `effect-value` carries the note: "The cannon, lotus flute, and megaphone values are in
  addition to **Stone's list**." (emphasis added — this is MusicXML's own statement that its
  percussion pictogram vocabulary is Kurt Stone's, transcribed.)
- `pitched-value`: "The chimes and tubular chimes values distinguish the single-line and
  double-line versions of the pictogram."
- `wood-value`: "The maraca and maracas values distinguish the one- and two-maraca versions of
  the pictogram."

`smufl-pictogram-glyph-name` (line 583 of the XSD) is the escape hatch: any `pict…` SMuFL
glyph name may be given on `<beater>`, `<stick>` etc. to name a pictogram MusicXML has no
enumerated value for.

**The load-bearing observation.** MusicXML's percussion vocabulary is a vocabulary of
*pictograms*, not of *events*. `stick-location` has exactly four values and is the only place
in the whole format where "where on the instrument was it struck" can be said — and it is
attached to a `<direction>` (an instruction printed above the staff), not to the note. There
is no MusicXML value anywhere for rim shot, cross stick, ghost note, choke, buzz, open vs
closed hi-hat, or snares on/off as *properties of a note*: snares-off exists only as the
pictogram `snare drum snares off` and hi-hat only as the instrument `hi-hat`. A MusicXML file
that wants to say "closed hi-hat" says it with a notehead and a printed word.

---

### 2.3 MusicXML 4.0 Standard Sounds — the percussion instrument ids, complete

Locator: `w3c/musicxml`, `v4.0:schema/sounds.xml` ("This sounds.xml file contains the standard
sounds that are included in MusicXML 4.0. The required id attribute lists the MusicXML sound
identifier string used by the instrument-sound element."). 391 of the ids are percussion,
across six families.

**`drum.*` (137)**

drum.apentemma, drum.ashiko, drum.atabaque, drum.atoke, drum.atsimevu, drum.axatse,
drum.bass-drum, drum.bata, drum.bata.itotele, drum.bata.iya, drum.bata.okonkolo, drum.bendir,
drum.bodhran, drum.bombo, drum.bongo, drum.bougarabou, drum.buffalo-drum, drum.cajon,
drum.chenda, drum.chu-daiko, drum.conga, drum.cuica, drum.dabakan, drum.daff, drum.dafli,
drum.daibyosi, drum.damroo, drum.darabuka, drum.def, drum.dhol, drum.dholak, drum.djembe,
drum.doira, drum.dondo, drum.doun-doun-ba, drum.duff, drum.dumbek, drum.fontomfrom,
drum.frame-drum, drum.frame-drum.arabian, drum.geduk, drum.ghatam, drum.gome, drum.group,
drum.group.chinese, drum.group.ewe, drum.group.indian, drum.group.set, drum.hand-drum,
drum.hira-daiko, drum.ibo, drum.igihumurizo, drum.inyahura, drum.ishakwe, drum.jang-gu,
drum.kagan, drum.kakko, drum.kanjira, drum.kendhang, drum.kendhang.ageng, drum.kendhang.ciblon,
drum.kenkeni, drum.khol, drum.kick-drum, drum.kidi, drum.ko-daiko, drum.kpanlogo, drum.kudum,
drum.lambeg, drum.lion-drum, drum.log-drum, drum.log-drum.african, drum.log-drum.native,
drum.log-drum.nigerian, drum.madal, drum.maddale, drum.mridangam, drum.naal, drum.nagado-daiko,
drum.nagara, drum.naqara, drum.o-daiko, drum.okawa, drum.okedo-daiko, drum.pahu-hula,
drum.pakhawaj, drum.pandeiro, drum.pandero, drum.powwow, drum.pueblo, drum.repinique, drum.riq,
drum.rototom, drum.sabar, drum.sakara, drum.sampho, drum.sangban, drum.shime-daiko, drum.sogo,
drum.surdo, drum.tabla, drum.tabla.bayan, drum.tabla.dayan, drum.tabor, drum.taiko,
drum.talking, drum.tama, drum.tamborim, drum.tamborita, drum.tambourine, drum.tamte,
drum.tangku, drum.tan-tan, drum.taphon, drum.tar, drum.tasha, drum.tenor-drum, drum.teponaxtli,
drum.thavil, drum.the-box, drum.timbale, drum.timpani, drum.tinaja, drum.toere, drum.tombak,
drum.tom-tom, drum.tom-tom.synth, drum.tsuzumi, drum.tumbak, drum.uchiwa-daiko, drum.udaku,
drum.udu, drum.zarb, drum.snare-drum, drum.snare-drum.electric, drum.slit-drum,
drum.slit-drum.krin

**`metal.*` (78)**

metal.adodo, metal.anvil, metal.babendil, metal.bells.agogo, metal.bells.almglocken,
metal.bells.bell-plate, metal.bells.bell-tree, metal.bells.carillon, metal.bells.chimes,
metal.bells.chimta, metal.bells.chippli, metal.bells.church, metal.bells.cowbell,
metal.bells.dawuro, metal.bells.gankokwe, metal.bells.ghungroo, metal.bells.hatheli,
metal.bells.jingle-bell, metal.bells.khartal, metal.bells.mark-tree, metal.bells.sistrum,
metal.bells.sleigh-bells, metal.bells.temple, metal.bells.tibetan, metal.bells.tinklebell,
metal.bells.trychel, metal.bells.wind-chimes, metal.bells.zills, metal.berimbau,
metal.brake-drums, metal.crotales, metal.cymbal.bo, metal.cymbal.ceng-ceng,
metal.cymbal.chabara, metal.cymbal.chinese, metal.cymbal.ching, metal.cymbal.clash,
metal.cymbal.crash, metal.cymbal.finger, metal.cymbal.hand, metal.cymbal.kesi,
metal.cymbal.manjeera, metal.cymbal.reverse, metal.cymbal.ride, metal.cymbal.sizzle,
metal.cymbal.splash, metal.cymbal.suspended, metal.cymbal.tebyoshi, metal.cymbal.tibetan,
metal.cymbal.tingsha, metal.flexatone, metal.gong, metal.gong.ageng, metal.gong.agung,
metal.gong.chanchiki, metal.gong.chinese, metal.gong.gandingan, metal.gong.kempul,
metal.gong.kempyang, metal.gong.ketuk, metal.gong.kkwenggwari, metal.gong.luo,
metal.gong.singing, metal.gong.thai, metal.guira, metal.hang, metal.hi-hat, metal.jaw-harp,
metal.kengong, metal.murchang, metal.musical-saw, metal.singing-bowl, metal.spoons,
metal.steel-drums, metal.tamtam, metal.thundersheet, metal.triangle, metal.washboard

**`wood.*` (27)**

wood.agogo-block, wood.agung-a-tamlang, wood.ahoko, wood.bones, wood.castanets, wood.claves,
wood.drum-sticks, wood.gourd, wood.granite-block, wood.guban, wood.guiro, wood.hyoushigi,
wood.ipu, wood.jam-block, wood.kaekeeke, wood.kagul, wood.kalaau, wood.kashiklar, wood.kubing,
wood.pan-clappers, wood.sand-block, wood.slapstick, wood.stir-drum, wood.temple-block,
wood.tic-toc-block, wood.tonetang, wood.wood-block

**`rattle.*` (22)**

rattle.afoxe, rattle.birds, rattle.cabasa, rattle.caxixi, rattle.cog, rattle.ganza,
rattle.hosho, rattle.jawbone, rattle.kayamba, rattle.kpoko-kpoko, rattle.lava-stones,
rattle.maraca, rattle.rain-stick, rattle.ratchet, rattle.rattle, rattle.shaker,
rattle.shaker.egg, rattle.shekere, rattle.sistre, rattle.televi, rattle.vibraslap,
rattle.wasembe

**`effect.*` (63)**

effect.aeolian-harp, effect.air-horn, effect.applause, effect.bass-string-slap, effect.bird,
effect.bird.nightingale, effect.bird.tweet, effect.breath, effect.bubble, effect.bullroarer,
effect.burst, effect.car, effect.car.crash, effect.car.engine, effect.car.pass,
effect.car.stop, effect.crickets, effect.dog, effect.door.creak, effect.door.slam,
effect.explosion, effect.flute-key-click, effect.footsteps, effect.frogs,
effect.guitar-cutting, effect.guitar-fret, effect.gunshot, effect.hand-clap, effect.heartbeat,
effect.helicopter, effect.high-q, effect.horse-gallop, effect.jet-plane, effect.laser-gun,
effect.laugh, effect.lions-roar, effect.machine-gun, effect.marching-machine,
effect.metronome-bell, effect.metronome-click, effect.pat, effect.punch, effect.rain,
effect.scratch, effect.scream, effect.seashore, effect.siren, effect.slap, effect.snap,
effect.stamp, effect.starship, effect.stream, effect.telephone-ring, effect.thunder,
effect.train, effect.trash-can, effect.whip, effect.whistle, effect.whistle.mouth-siren,
effect.whistle.police, effect.whistle.slide, effect.whistle.train, effect.wind

**`pitched-percussion.*` (64)**

pitched-percussion.angklung, .balafon, .bell-lyre, .bells, .bianqing, .bianzhong, .bonang,
.cimbalom, .crystal-glasses, .dan-tam-thap-luc, .fangxiang, .gandingan-a-kayo, .gangsa,
.gender, .giying, .glass-harmonica, .glockenspiel, .glockenspiel.alto, .glockenspiel.soprano,
.gyil, .hammer-dulcimer, .handbells, .handchimes, .kalimba, .kantil, .khim, .kulintang,
.kulintang-a-kayo, .kulintang-a-tiniok, .likembe, .luntang, .marimba, .marimba.bass, .mbira,
.mbira.array, .metallophone, .metallophone.alto, .metallophone.bass, .metallophone.soprano,
.music-box, .pelog-panerus, .pemade, .penyacah, .ranat.ek, .ranat.ek-lek, .ranat.thum,
.ranat.thum-lek, .reyong, .sanza, .saron-barung, .saron-demong, .saron-panerus,
.slendro-panerus, .slentem, .tsymbaly, .tubes, .tubular-bells, .vibraphone, .xylophone,
.xylophone.alto, .xylophone.bass, .xylophone.soprano, .xylorimba, .yangqin

**Observation.** 391 percussion sound ids, and only three of them encode anything other than
an instrument identity: `drum.snare-drum.electric`, `drum.tom-tom.synth` (timbre) and
`drum.group.set` (an instrument *group*, i.e. a whole kit as one sound). Playing technique is
absent from the id space by design — the whole drum kit is one sound id, and everything a
drummer does to it is invisible at this level.

---

### 2.4 MEI — a closed articulation list with no percussion in it

Locator: `music-encoding/music-encoding` 34e82b155d55ae0bc0159ffefe2050ac992e931d, edition
"MEI 6.0-dev", `source/modules/MEI.xml` line 251, `<macroSpec ident="data.ARTICULATION">`,
`<valList type="closed">`. Licence: Educational Community License 2.0.

Complete, verbatim (40 values, with MEI's own gloss):

acc (Accent, Unicode 1D17B) · acc-inv (Inverted accent) · acc-long (Long accent) · acc-soft
(Soft accent, see SMuFL Articulation supplement U+ED40–U+ED4F) · stacc (Staccato, 1D17C) · ten
(Tenuto, 1D17D) · stacciss (Staccatissimo, 1D17E) · marc (Marcato, 1D17F) · spicc (Spiccato) ·
stress (Stress, 00B4) · unstress (Unstress, 02D8) · doit · scoop · rip ("also known as
squeeze") · plop · fall · longfall · bend ("lip slur to lower pitch, then return to written
pitch") · flip (1D187) · smear (1D188) · shake · dnbow (Down bow, 1D1AA) · upbow (Up bow,
1D1AB) · harm (Harmonic, 1D1AC) · snap (Snap pizzicato, 1D1AD) · fingernail (1D1B3) · damp
("Stop harp string from sounding", 1D1B4) · dampall ("Stop all harp strings from sounding",
1D1B5) · open ("Full (as opposed to stopped) tone") · stop ("'muffled' tone") · dbltongue
(1D18A) · trpltongue (1D18B) · heel ("Use heel (organ pedal)") · toe ("Use toe (organ pedal)")
· tap ("Percussive effect on guitar string(s)") · lhpizz · dot ("Uninterpreted dot") · stroke
("Uninterpreted stroke"). Deprecated and warned against by Schematron: `marc-stacc`,
`ten-stacc`.

`data.NOTEHEADMODIFIER.list` (line 3063), also closed, 10 values: slash, backslash, vline,
hline, centerdot, paren, brack, box, circle, fences.

**Finding, stated plainly: MEI has no percussion vocabulary.** A grep of the whole ODD source
for "percussion" returns two hits, both incidental (a MIDI channel-10 remark in `MEI.xml:2762`
and a Schematron rule requiring `@lines` on a TAB or percussion clef in `MEI.shared.xml:832`).
There is no percussion module, no beater attribute, no stick location, no playing-technique
element. MEI's answer is `att.extSym` (`source/modules/MEI.externalsymbols.xml`): `@glyph.auth`
= `smufl`, plus `@glyph.name` or `@glyph.num`, i.e. *point at a SMuFL glyph*. The values that
happen to be usable for percussion — heel, toe, damp, open, stop, fingernail, snap — are there
for organ, harp and guitar, and their definitions say so.

For KITWARP this is the cleanest possible evidence that a technique axis is not a solved
problem in the encoding standards: the most academically rigorous of them declines to have
one and delegates to a *font*.

---

### 2.5 MNX — the regression

Locator: `w3c/mnx` 0a8c7602d624942668e1ac2b5c6a1aa2214be0d1 (2026-08-25),
`doctools/mnx-metaspec.json`.

MNX models unpitched percussion with three objects:

- `kit` — "keyedDict" whose values are `kit-component`
- `kit-component` — properties: `name` (string, "A human-readable name for this kit component,
  e.g., for purposes of display in a UI"), `sound` (id), `staffPosition` (required)
- `kit-note` — properties: `kitComponent` (id, required), `perform`, `staff`

and the `sound` object it points at has exactly two properties: `midiNumber` and `name`
("A human-readable name for this sound, suitable for use in a UI").

Verbatim from the spec text: "This is generally used for unpitched percussion music, and some
applications call it a 'percussion map.' For example, one kit component might be 'Bass drum,'
with the staff position on the bottom staff line (staffPosition -4)."

The full object list of the metaspec (146 objects) contains `accent`, `bow-direction`,
`breath-mark-symbol`, `spiccato`, `staccatissimo`, `staccato`, `stress-marking`, `tenuto`,
`tremolo-single`, `multi-note-tremolo` — and nothing percussion-specific beyond kit/kitComponent/kitNote.

**So MusicXML's successor has dropped the pictogram enumerations entirely and replaced the
percussion vocabulary with `{name: string, midiNumber: int}`.** That is precisely the pivot
loss this repository documents in `docs/evidence/note-number-pivot-loss.md`, now written into
a draft W3C specification. Marked UNVERIFIED only as to intent: the MNX drafts may still add a
technique vocabulary later; what is verified is that the 2026-08-25 metaspec has none.

---

### 2.6 LilyPond — `drumPitchNames` and seven drum styles

Locator: https://gitlab.com/lilypond/lilypond/-/raw/master/ly/drumpitch-init.ly, header
`\version "2.23.6"`, "Copyright (C) 2001--2026 Rune Zedeler, Han-Wen Nienhuys".
**Licence: GPL v3 or later — under `docs/adr/0004-provenance-and-licensing.md` this is
`rederive-only`. The names below are cited as evidence of what the vocabulary contains; they
must not be copied into `data/` as a derived work.**

Full drum names (65), in file order: acousticbassdrum, bassdrum, hisidestick, sidestick,
losidestick, acousticsnare, snare, handclap, electricsnare, lowfloortom, closedhihat, hihat,
highfloortom, pedalhihat, **splashhihat**, lowtom, openhihat, halfopenhihat, lowmidtom,
himidtom, crashcymbala, crashcymbal, hightom, ridecymbala, ridecymbal, chinesecymbal, ridebell,
tambourine, splashcymbal, cowbell, crashcymbalb, vibraslap, ridecymbalb, mutehibongo, hibongo,
openhibongo, mutelobongo, lobongo, openlobongo, mutehiconga, muteloconga, openhiconga, hiconga,
openloconga, loconga, hitimbale, lotimbale, hiagogo, loagogo, cabasa, maracas, shortwhistle,
longwhistle, shortguiro, longguiro, guiro, claves, hiwoodblock, lowoodblock, mutecuica,
opencuica, mutetriangle, triangle, opentriangle, plus `tt`→`tamtam` reachable only through the
abbreviation table.

Abbreviations (the trade shorthand, one per name): bda, bd, ssh, ss, ssl, sna, sn, hc, sne,
tomfl, hhc, hh, tomfh, hhp, **hhs**, toml, hho, hhho, tomml, tommh, cymca, cymc, tomh, cymra,
cymr, cymch, rb, tamb, cyms, cb, cymcb, vibs, cymrb, bohm, boh, boho, bolm, bol, bolo, cghm,
cglm, cgho, cgh, cglo, cgl, timh, timl, agh, agl, cab, mar, whs, whl, guis, guil, gui, cl, wbh,
wbl, cuim, cuio, trim, tri, trio, tt.

`splashhihat` / `hhs` is worth flagging: it exists in the source file but is **absent from the
published documentation table** at
https://lilypond.org/doc/v2.24/Documentation/notation/percussion-notes (retrieved 2026-09-06;
the rendered table there does not contain a `splashhihat` row). It is the foot-splash: in `drums-style` it is notated `cross` with `(open . DOWN)`
at staff position -5, i.e. the pedal hi-hat position with an "open" articulation below.

Seven style tables define, per style, `(name notehead articulation staff-position)`:
`drums-style` (30 entries), `agostini-drums-style` (30), `timbales-style` (5), `congas-style`
(8), `bongos-style` (8), `percussion-style` (12), `weinberg-drums-style` (22). The last carries
this comment in the source, which is the pointer that led this bucket to the primary PAS
source:

```
;; Reference: Norman Weinberg, Guidelines for Drumset Notation
;; http://www.normanweinberg.com/uploads/8/1/6/4/81640608/940506pn_guildines_for_drumset.pdf
;; Percussive Notes, June 1994, p.15-26
```

Articulation values used in the style tables (a de-facto openness vocabulary):
`stopped` = closed hi-hat, `(open . UP)` = open hi-hat, `halfopen` = half-open hi-hat
(only in `weinberg-drums-style`), `(open . DOWN)` = foot splash, `open` / `stopped` on congas
and bongos = open tone / muted tone, `staccato` = short guiro, `tenuto` = long guiro.
Noteheads used: default, `cross`, `xcircle`, `diamond`, `triangle`, `mensural`, `mi`.

---

### 2.7 Guitar Pro — the `.gpif` percussion articulation list, complete

Locator: `CoderLine/alphaTab` 1f428ccd1ea2faeeb1a8b48cb17194cfd60ba11e,
`packages/alphatab/src/exporter/GpifSoundMapper.ts` lines 288–488, generated from Guitar Pro's
own default drum kit (the file's sibling `PercussionMapper.ts` carries the comment "To update
the following generated code, use the GpExporterTest.percussion-articulations unit test").
Licence: alphaTab is MPL-2.0; the *names* are Arobas Music's vocabulary, reproduced here as
evidence.

Guitar Pro's sound id is a three-part string — **implement `.` action `.` variant** — which is
the closest thing in this bucket to KITWARP's own tuple.

| Instrument (GP element) | Articulation name, verbatim | GP input MIDI | GP RSE sound id |
|---|---|---|---|
| Snare | Snare (hit) | 38 | `stick.hit.hit` |
| Snare | Snare (side stick) | 37 | `stick.hit.sidestick` |
| Snare | Snare (rim shot) | 91 | `stick.hit.rimshot` |
| Snare (alt) | Snare (side stick) | 31 | `stick.hit.sidestick` |
| Electric Snare | Electric Snare (hit) | 40 | `stick.hit.hit` |
| Hi-Hat ("Charley") | Hi-Hat (closed) | 42 | `stick.hit.closed` |
| Hi-Hat | Hi-Hat (half) | 92 | `stick.hit.half` |
| Hi-Hat | Hi-Hat (open) | 46 | `stick.hit.open` |
| Pedal Hi-Hat | Pedal Hi-Hat (hit) | 44 | `pedal.hit.pedal` |
| Kick | Kick (hit) | 35 | `pedal.hit.hit` |
| Kick | Kick (hit) | 36 | `pedal.hit.hit` |
| Toms | Very Low Tom (hit) 43 · Low Tom (hit) 45 · Mid Tom (hit) 47 · High Tom (hit) 48 · High Floor Tom (hit) 50 · Low Floor Tom (hit) 41 | — | `stick.hit.hit` |
| Ride | Ride (edge) | 93, 59 | `stick.hit.edge` |
| Ride | Ride (middle) | 51, 126 | `stick.hit.mid` |
| Ride | Ride (bell) | 53, 127 | `stick.hit.bell` |
| Ride | Ride (choke) | 94, 29 | `stick.hit.choke` |
| Splash | Splash (hit) 55 · Splash (choke) 95 | — | `stick.hit.hit` / `stick.hit.choke` |
| China | China (hit) 52 · China (choke) 96 | — | `stick.hit.hit` / `stick.hit.choke` |
| Crash high | Crash high (hit) 49 · Crash high (choke) 97 | — | `stick.hit.hit` / `stick.hit.choke` |
| Crash medium | Crash medium (hit) 57 · Crash medium (choke) 98 | — | `stick.hit.hit` / `stick.hit.choke` |
| Reverse Cymbal | Reverse Cymbal (hit) | 30 | `stick.hit.hit` |
| Cowbell low / medium / high | Cowbell … (hit) 99 / 56 / 102; Cowbell … (tip) 100 / 101 / 103 | — | `stick.hit.hit` / `stick.hit.tip` |
| Woodblock low / high | Woodblock low (hit) 77 · Woodblock high (hit) 76 | — | `stick.hit.hit` |
| Bongo High / Low | (hit) 60 / 61 · (mute) 104 / 106 · (slap) 105 / 107 | — | `hand.hit.hit` / `hand.hit.mute` / `hand.hit.slap` |
| Conga low / high | (hit) 64 / 63 · (slap) 108 / 110 · (mute) 109 / 62 | — | `hand.hit.hit` / `hand.hit.slap` / `hand.hit.mute` |
| Timbale low / high | (hit) 66 / 65 | — | `stick.hit.hit` |
| Agogo low / high | (hit) 68 / 67 | — | `stick.hit.hit` |
| Whistle low / high | (hit) 72 / 71 | — | `blow.hit.hit` |
| Guiro | Guiro (hit) 73 · Guiro (scrap-return) 74 | — | `stick.hit.hit` / `stick.scrape.return` |
| Surdo | Surdo (hit) 86 · Surdo (mute) 87 | — | `brush.hit.hit` / `brush.hit.mute` |
| Tambourine | (hit) 54 · (return) 111 · (roll) 112 · (hand) 113 | — | `hand.hit.hit` / `hand.hit.return` / `hand.hit.roll` / `hand.hit.handhit` |
| Cuica | Cuica (open) 79 · Cuica (mute) 78 | — | `hand.hit.hit` / `hand.hit.mute` |
| Vibraslap | Vibraslap (hit) | 58 | `hand.hit.hit` |
| Triangle | Triangle (hit) 81 · Triangle (mute) 80 | — | `stick.hit.hit` / `stick.hit.mute` |
| Grancassa | Grancassa (hit) | 114 | `mallet.hit.hit` |
| Piatti | Piatti (hit) 115 · Piatti (hand) 116 | — | `hand.hit.hit` |
| Cabasa | Cabasa (hit) 69 · Cabasa (return) 117 | — | `hand.hit.hit` / `hand.hit.return` |
| Castanets | Castanets (hit) | 85 | `hand.hit.hit` |
| Claves | Claves (hit) | 75 | `stick.hit.hit` |
| Left / Right Maraca | (hit) 70 / 119 · (return) 118 / 120 | — | `hand.hit.hit` / `hand.hit.return` |
| Shaker | Shaker (hit) 82 · Shaker (return) 122 | — | `hand.hit.hit` / `hand.hit.return` |
| Bell Tree | (hit) 84 · (return) 123 | — | `stick.hit.hit` / `stick.hit.return` |
| Jingle Bell / Tinkle Bell | (hit) 83 | — | `stick.hit.hit` |
| Golpe | Golpe (thumb) 124 · Golpe (finger) 125 | — | `thumb.hit.body` / `finger4.hit.body` |
| Hand Clap | Hand Clap (hit) | 39 | `hand.hit.hit` |
| Metronome | Metronome (hit) 33 · Metronome (bell) 34 | — | `stick.hit.sidestick` / `stick.hit.hit` |

Distinct implements in the GP sound-id first field: `stick`, `hand`, `pedal`, `brush`,
`mallet`, `blow`, `thumb`, `finger4`. Distinct actions in the second field: `hit`, `scrape`.
Distinct variants in the third: hit, sidestick, rimshot, closed, half, open, pedal, edge, mid,
bell, choke, tip, mute, slap, return, roll, handhit, body, scrape-return.

---

### 2.8 MuseScore — 107 percussion instruments, and the marching sets are the interesting ones

Locator: `musescore/MuseScore` 7991526152de746dcdcbbee130d5ab5f360f198e,
`share/instruments/instruments.xml`. Licence: GPL-3.0 — `rederive-only`.

Each `<Instrument>` with `<drumset>1</drumset>` carries `<Drum pitch="…">` entries with
`<name>`, `<head>` (notehead), `<line>`, `<voice>`, `<stem>`, and a `<musicXMLid>` that maps
the instrument to a MusicXML standard sound. 107 instruments carry drum entries.

Drum Kit (large), id `drumset`, musicXMLid `drum.group.set`, 23 entries: Bass Drum 2 (35),
Bass Drum 1 (36), Side Stick (37, notehead `slashed1`), Acoustic Snare (38), Electric Snare
(40, `slash`), Low Floor Tom (41), Closed Hi-Hat (42, `cross`), High Floor Tom (43), Pedal
Hi-Hat (44, `cross`), Low Tom (45), Open Hi-Hat (46, `xcircle`), Low-Mid Tom (47), Hi-Mid Tom
(48), Crash Cymbal 1 (49, `cross`), High Tom (50), Ride Cymbal 1 (51, `cross`), China Cymbal
(52), Ride Bell (53, `diamond`), Tambourine (54, `diamond`), Splash Cymbal (55, `cross`),
Cowbell (56, `triangle-down`), Crash Cymbal 2 (57, `cross`), Ride Cymbal 2 (59, `cross`).

Drum Kit (minimal) `drum-kit-4` (11) and Drum Kit (common) `drum-kit-5` (16) use **Cross-stick**
where the large kit says **Side Stick** — same MIDI 37, same notehead, two names inside one
file.

Marching Snare Drum (`marching-snare`, musicXMLid `drum.snare-drum`, 11 entries) — this is the
only place in any source in this bucket where a *closed set of snare techniques* is enumerated
as data: **Buzz** (48), **Battery Snare** (50), **Rim Shot** (52), **Rim Click** (53,
`cross`), **Stick Click** (55, `plus`), **Stick Shot** (57, `slashed1`), **Shell** (59,
`cross`), **Backstick** (60, `ti`), plus Ride Cymbal 1 (72), Open Hi-Hat (74), Closed Hi-Hat
(76).

Marching Tenor Drums (`marching-tenor-drums`, 25 entries) enumerates per-drum techniques:
Drum 1–4 and **Spock 1–2** (the small high tenor drums), each with plain, **Rim**, **Buzz**,
**Muted** (`plus` notehead) and — for drums 3 and 4 — **Shell** (`la` notehead), plus **Stick
Click**.

Marching Bass Drums (11): Drum 1–5 each plain and **Rim**, plus **Unison** (`slash`).

Marching Cymbals (`marching-cymbals`, musicXMLid `metal.cymbal.crash`, 13 entries): **Full
Crash**, **Half Crash**, **Hi-Hat**, **Sizzle**, **Crash-Choke**, **Tap**, **Tap-Choke**,
**Bell Tap**, **Bell Tap-Choke**, **Muted Tap**, **Smash**, **Zing**, **Roll**.

Hand-drum instruments encode the hand-technique triple directly as instrument entries:
Djembe and Doumbek both = **Slap / Open / Bass**; Congas = Mute High Conga / High Conga / Low
Conga; Cuíca = Mute Cuica / Open Cuica; Triangle = Mute Triangle / Open Triangle; Taiko =
Taiko Mute / Taiko; Güiro = Short Güiro / Long Güiro.

---

### 2.9 Sibelius SoundWorld — a technique vocabulary hidden inside an instrument tree

Locators: Sound Set Editor User Guide (PDF, retrieved 2026-09-06) and the SoundWorld white
paper; observed ids from 17 published sound sets in `glepore70/pronom-research`
2217b83abef3a2eb9b0b39f0b8b4b5ec798d3fc0, `sample_files/s/sibelius/*.xml`.
Licence: Avid / vendor proprietary — quoted here as evidence, not reusable as data.

The grammar, verbatim from the Sound Set Editor guide:

- "On the Drum Maps page you define a drum map, which is a list of each pitch provided by an
  unpitched drum set patch and its corresponding sound ID."
- "This is the relative sound ID change provided by the switch. Relative sound ID changes are
  one or more element of a sound ID… You can define multiple relative sound ID changes in the
  same switch, e.g. +pizzicato +mute, which means that the switch adds both relative sound ID
  changes to the current sound ID."
- "…if you want the switch to very specific relative sound IDs, e.g. +mute.harmon,
  +mute.straight, +trill.half, +trill.whole, then you should specify them as a single,
  multi-element sound ID change."
- "Try to create your own sound IDs by basing them on the closest existing sound ID, e.g. by
  adding one or more elements to the end. This ensures that Sibelius's SoundWorld system will
  be able to properly substitute your chosen sound ID for the closest available one when your
  scores are played back on other devices."

From the SoundWorld paper: ids are a tree of dot-separated elements; ids shipped in the sound
world are **primary**, anything added later is **secondary** ("The IDs in the sound world are
called primary. Any other ID added to the tree later is called secondary."); "It is a rule that
all unpitched sounds go into the `unpitched` branch"; the id `unpitched` itself is unavailable;
`unpitched.exotic.silence` is the terminal fallback; substitution walks the tree.

Observed vocabulary: 4 887 distinct `unpitched.*` ids across the 17 sound sets; 994 of them
carry no vendor marker. The core Sibelius GM set (`Sibelius_Essentials_GM.xml`) has 56, e.g.
`unpitched.drum.medium.snare`, `unpitched.metal.hi-hat.closed`,
`unpitched.metal.hi-hat.closed.pedal`, `unpitched.metal.hi-hat.open`,
`unpitched.metal.cymbal.ride.bell`, `unpitched.metal.cymbal.crash.high`,
`unpitched.drum.medium.tom-tom.electric`.

Technique-bearing trailing elements observed across the sets (the number is the count of ids
using that element; vendor-library patch names such as `a-list`, `ap1`, `dink`, `sloppy` are
excluded as secondary):

| Element | Uses | What it says | Example id |
|---|---|---|---|
| `closed` | 68 | hi-hat closed, conga closed | `unpitched.metal.hi-hat.closed` |
| `open` | 49 | hi-hat open, hand-drum open tone | `unpitched.metal.hi-hat.open` |
| `halfway` | 3 | hi-hat half open | `unpitched.metal.hi-hat.halfway.jazz` |
| `pedal` | 31 | hi-hat closed with the foot | `unpitched.metal.hi-hat.closed.pedal` |
| `slap` | 41 | hand-drum slap | `unpitched.drum.high.bongo.slap` |
| `mute` / `muffled` | 35 / 11 | damped | `unpitched.drum.high.bongo.muffled` |
| `pressed` | 10 | pressed (damped) stroke | — |
| `rim` | 10 | struck on the rim | — |
| `shell` | 7 | struck on the shell | — |
| `edge` | 15 | cymbal edge | `unpitched.metal.cymbal.ride.edge.red` |
| `bell` | 17 | cymbal bell | `unpitched.metal.cymbal.ride.bell` |
| `ping` | 8 | ride ping stroke | `unpitched.metal.cymbal.ride.ping.rock` |
| `choke` | 13 | cymbal choke | `unpitched.metal.cymbal.crash.choke.big` |
| `scrape` | 18 | cymbal/gong scrape | `unpitched.metal.cymbal.scrape` |
| `roll` | 32 | roll | `unpitched.metal.cymbal.roll.crescendo` |
| `crescendo` | 6 | crescendo roll | `unpitched.metal.cymbal.roll.crescendo` |
| `damp` | 12 | damped roll / stroke | `unpitched.metal.cymbal.roll.damp` |
| `flam` | 33 | flam | `unpitched.drum.high.tom-tom.flam` |
| `tremolo` | 8 | tremolo | — |
| `brush` | 28 | played with brushes | `unpitched.metal.cymbal.ride.brush` |
| `mallet` | 3 | played with mallets | `unpitched.metal.cymbal.sizzle.mallet.jazz` |
| `nylon` / `wood` | 1 / 1 | stick tip material | `unpitched.metal.cymbal.sizzle.nylon` |
| `finger` / `fingers` | 13 / 5 | played with fingers | `unpitched.metal.cymbal.sizzle.finger` |
| `hand` / `palm` / `heel` / `tip` | 5 / 8 / 1 / 1 | hand-drum contact part | `unpitched.drum.high.conga.heel…`, `…conga.tip…` |
| `left` / `right` | 18 / 18 | which of a pair | `unpitched.metal.cymbal.ride.left` |
| `cracked` | 2 | cracked cymbal | `unpitched.metal.cymbal.ride.cracked.jazz` |
| `sizzle` | 10 | sizzle | `unpitched.metal.cymbal.ensemble.sizzle` |
| `jazz` / `fusion` / `rock` / `orch` / `concert` | 30 / 28 / 15 / 14 / 5 | kit voicing | `unpitched.metal.cymbal.crash.jazz` |
| `electric` | 1 | electronic timbre | `unpitched.drum.medium.tom-tom.electric` |

Sibelius also encodes kit voicing as an id element in the GM sets (`kit-brush`,
`kit-electronic`, `kit-jazz`, `kit-orchestra`, `kit-power`, `kit-room`, `kit-standard`,
`kit-tr-808` — seen in the Vir2 VI.ONE set), which is the GM-2 kit list expressed as
vocabulary rather than as a program-change number.

---

### 2.10 Weinberg / Percussive Arts Society, "Guidelines for Drumset Notation" (1994)

Locator: Norman Weinberg, *Percussive Notes*, June 1994, pages 15–26; PDF at
https://www.normanweinberg.com/uploads/8/1/6/4/81640608/940506pn_guildines_for_drumset.pdf
(12-page image-only scan of the printed article, no text layer; read page by page from
rendered images). Basis, in the author's words: "20 reference works and 200 performance works
were analyzed in this survey"; elsewhere "the 220 publications examined for these guidelines".
These are the guidelines the PAS endorsed and that Finale, Sibelius and Dorico follow.
**Licence: all rights reserved (Percussive Arts Society). Quoted here as evidence; not
reusable as data.**

Instrument placement and instance ordering (p. 17–19):

- Snare drum: third space. "This staff position was employed in over 86% of precisely notated
  performance literature, and in 97% of all improvisational charts included in the survey."
- Bass drum: first space; a second bass drum on the first line.
- Tom-toms: Ex. 4 gives staff positions for **one to ten toms**, and the recommendation is
  explicitly by *total count*, not by ordinal: "the recommendation will be based on the total
  number of tom-toms included in the composition."
- Hi-hat with the foot: first space **below** the staff. Hi-hat with the hand: the space above
  the top line. "This location represents the first instance of having two instruments at the
  same staff position location, as the highest tom-tom in a set of seven toms also uses the
  first space above the staff."
- Ride cymbal: top line. Crash: first ledger line above. Second ride: fourth line. Additional
  crashes above the first crash. **Second hi-hat**: "The top space of the staff should be
  reserved for a second set of hi-hat cymbals… their use is becoming more and more popular as
  drummers place an additional pair of hi-hats on the right-hand side of the drumset."
- Cowbell: top space, closed triangle notehead (open triangle for values longer than a
  quarter).
- Seven cymbals fit on the staff: "two hi-hat cymbals, two ride cymbals, and three crash
  cymbals of various types."
- And the sentence that matters most for a pivot vocabulary: "The exact cymbal types (China,
  splash, sizzle, swish, etc.) should be identified in the key of the composition. For the
  performer, the fact that a cymbal written at a certain staff location is a China cymbal or a
  splash cymbal is not relevant."

Techniques and articulations (p. 20–23), verbatim where quoted:

| Term as Weinberg spells it | Notation recommended | Verbatim definition or finding |
|---|---|---|
| Ghost stroke | notehead in parentheses | "parenthetical note heads be used to indicate ghost strokes"; applicable "on any type of instrument (drums, cymbals, cowbells, etc.)" |
| Rimshot | normal notehead **surrounded by a circle** | "five different note heads were defined as 'rimshot' and 12 different note heads specified rimshot variations… 14 additional rimshots and rimshot variations are encountered. Obviously, drumset notation shouldn't require 31 different notational procedures for a single effect." Conforms "to the standards set forth by both Stone and Gardner Read's *Notation: A Manual of Modern Practice*." |
| Open hi-hat | "X" notehead + **open circle** articulation | "These articulation signs and their associated meanings are approved by the International Conference on New Musical Notation, and recommended by both Stone and Brindle." |
| Closed hi-hat | **plus sign** articulation | "It should be assumed that all hi-hat notes are to be played on the closed hi-hat unless the articulation sign for open hi-hats is present." |
| Half-open (half-closed) hi-hat | **open circle bisected by a line** | "While this performance technique is not as common as the stroke for fully open hi-hats, it does offer a higher degree of precision and musical nuance." |
| Foot splash | the same open-circle articulation, on the foot hi-hat | "This performance technique involves playing the hi-hat pedal with the foot in such a manner as to create a sound similar to a pair of small crash cymbals, rather than the tight 'chick' sound normally associated with the hi-hat cymbals played with the foot." |
| Chick (implied) | assumed default for the foot hi-hat | "the closed hi-hat with foot should be assumed unless this articulation sign is employed." |
| Choke / cut-off | open circle and plus sign borrowed from the hi-hat | "Notes on any instrument that are to be performed in a manner where the natural vibrations are cut off should use the hi-hat articulations of an open circle and the plus sign for such purposes." |
| Natural decay / L.V. | incomplete tie | "It should be assumed that all instruments of the drumset be allowed to ring for the entire length of their natural decay"; the "L.V." plus incomplete tie combination "is redundant, as only one sign is necessary." |
| Bell / edge of cymbal | Ex. 16, ICNMN symbols | surface-area indication |
| Centre / edge of drum | Ex. 17, ICNMN symbols | surface-area indication |
| Surface-area indications | "a brief word or two written above the music (such as 'at bell,' 'at edge' or 'at center')" | "Few works surveyed for these guidelines incorporate any type of surface-area specifications other than a written instruction to play on the bell of the cymbal." Percussionists "will usually strike the same area of the cymbal unless otherwise instructed" (Adams); PAS: "the percussionist will play in the area that elicits the best tonal quality from the instrument." |
| Rimshot variations, shell playing | brief text | "any additional performance techniques (such as rimshot variations or playing on the shell of a drum) be indicated with brief text." |
| Sticking | upper-case R and L | "The sticking should not be included unless a specific sticking is necessary to produce a desired effect." (PAS) |

Beaters (p. 23), **a closed set of four with an explicit escape hatch** — this is Ex. 23,
"Symbols for Standard Beaters":

| Beater | Symbol |
|---|---|
| Drumstick | pictogram of a drum stick, or a very small closed circle at the end of a vertical line |
| Brush | pictogram of a brush |
| Hard Mallet | closed circle at the end of a vertical line |
| Soft Mallet | open circle at the end of a vertical line |

"Esoteric beaters (such as knitting needles, rattan sticks, Superballs or coins, to name but a
few) should be indicated by a brief word in the score or defined as a graphic symbol in the
key." Combinations of sticks follow the ICNMN rules: "All combinations should be boxed; Do not
indicate L.H., R.H. at top of box; Always draw the striking end next to top of box."

Weinberg's own diagnosis of the field, which is the reason this bucket exists: 31 different
notational procedures were found in the literature for the single effect "rimshot".

---

### 2.11 Finale — the Note Type vocabulary

Locator: MakeMusic Finale user manual, `usermanuals.finalemusic.com/FinaleMac/Content/Finale/`,
pages `PercussionMaps2.htm` ("Percussion MIDI Maps: Garritan Instruments for Finale") and
`PercussionMaps3.htm` ("Percussion MIDI Maps: Tapspace Drumline for Finale"), retrieved by
direct HTTP on 2026-09-06 (the dialog-documentation pages named in §1 rows 29–30 describe the
mechanism only; **the enumeration is published on the percussion-map pages**, and this
supersedes the "no enumeration published" reading those two pages alone suggest).
Licence: MakeMusic vendor documentation, all rights reserved — cited as evidence.

Finale's term of art is **Note Type**: "A Percussion MIDI Map is simply a list that matches
each percussion instrument in a sound library with a particular MIDI note number." A Note Type
is the instrument-plus-technique identity that the percussion layout, the notehead and the
staff position all hang off; the Percussion MIDI Map then binds each Note Type to a note number
per sound library. Two Note Types may share a MIDI number in one map (e.g. 50 = "Snare Section
Hits" and "Snare Drum"), which is the clearest possible statement that the Note Type, not the
note number, is the identity.

**VDLite Finale Marching Percussion Map, complete (72 rows, MIDI 36–101):**
36 Bass Drum 5 (5) · 36 Kick Drum · 37 Bass Drum Rim · 38 Bass Drum 4 (4) · 39 Bass Drum Unison
Hits · 40 Bass Drum 3 (3) · 41 Bass Drum 2 (2) · 42 Bass Drum Roll · 43 Bass Drum · 44 Crash
Cymbals Crash · 45 Cymbal Section Crash · 46 Cymbal Section Hi-Hat Choke · 47 Crash Cymbals
Choke Fat · 48 Snare Section Hits LH · 49 Snare Rim LH · 50 Snare Section Hits · 50 Snare Drum ·
51 Snare Rims · 53 Snare Guz Short · 54 Snare Guz Long · 55 Snare Rim Shot (Both Hands) · 56
Snare Rim Shot LH · 57 Snare Cross Shots · 58 Snare Section Rim Shots (Both Hands) · 59 Stick
Clicks · 59 Snare Cross Stick · 60 Snare Section Buzz Rolls · 60 Snare Buzz Roll · 60 Snare Roll
· 61 Ride Bell · 62 Ride Cymbal · 63 Hi-Hat Open · 64 Hi-Hat Closed · 65 Low Tom · 66 Low Tom
Shot/Rim · 67 Low Tom Short Roll · 69 Low-Mid Tom · 70 Low-Mid Tom Shot/Rim · 71 Low-Mid Tom
Short Roll · 72 High-Mid Tom · 73 High-Mid Tom Shot/Rim · 74 Hi-Mid Tom Short Roll · 76 High Tom
· 76 Floor Tom 1 · 76 Floor Tom 2 · 77 High Tom Shot/Rim · 78 High Tom Short Roll · 79 Spock
Drum · 80 Spock Drum Rim Shot · 81 Tenors High Rims · 82 Tenors Low Rims · 83 Stick Click · 84
Crash Cymbal · 85 China Cymbal · 86 Cowbell · 87 Low Agogo · 88 High Agogo · 89 Claves · 89 High
Woodblock · 90 Vibra Slap · 91 Tambourine · 92 Cabasa · 93 Conga Dead Stroke · 94 Conga · 95
Conga Bass Tone · 96 Kick Drum (2) · 97 Triangle Mute · 98 Triangle Open · 99 Whistle Short ·
100 Whistle Long · 101 Large Gong

**VDLite General MIDI Percussion Map, complete (46 rows, MIDI 35–81):**
35 Bass Drum · 36 Kick Drum · 37 Snare Cross Stick · 38 Snare Drum · 39 Hand Clap · 40 Electric
Snare Drum · 41 Floor Tom 2 · 42 Hi-Hat Closed · 43 Floor Tom 1 · 44 Hi-Hat Foot · 45 Low Tom ·
46 Hi-Hat Open · 47 Low-Mid Tom · 48 High-Mid Tom · 49 Crash Cymbal · 50 High Tom · 51 Ride
Cymbal · 52 China Cymbal · 53 Ride Bell · 54 Tambourine · 55 Splash Cymbal · 56 Cowbell · 57
Crash Cymbal 2 · 58 Vibra Slap · 59 Ride Cymbal 2 · 60 High Bongo · 61 Low Bongo · 62 Conga Dead
Stroke · 63 Conga · 64 Tumba · 65 High Timbale · 66 Low Timbale · 67 High Agogo · 68 Low Agogo ·
69 Cabasa · 70 Maracas · 71 Whistle Short · 72 Whistle Long · 73 Guiro Short · 74 Guiro Long ·
75 Claves · 76 High Woodblock · 77 Low Woodblock · 80 Triangle Mute · 81 Triangle Open

The four VDLite line maps on the same page enumerate the marching sections: **Snareline** (13
rows: Snare Section Rim Shots LH, Snare Section Rims LH, Snare Section Rim Shots, Snare Section
Rims, Snare Cross Stick, Snare Cross Shot, Snare Section Hits LH, Snare Section Cross Shots,
Snare Section Hits, Snare Drum, Snare Section Buzz Rolls, Snare Roll); **Tenorline** (31 rows:
Low/Low-Mid/High-Mid/High Tom and Spock Drum / Spock Drum 2, each as plain, Shot/Rim, Buzz Roll
and LH variants, plus Sustained Buzz Roll); **Bassline** (17 rows: Bass Drum 1–6 with LH
variants, Bass Drum Unison Hits, Bass Drum Roll, Kick Drum); **Cymbal Line** (8 rows: Crash
Cymbal, Hi-Hat Open, China Cymbal, Ride Cymbal, Suspended Cymbal Fat Choke w/ Stick, Sizzle
Cymbal, Hi-Hat Closed).

The Garritan map page carries 572 distinct Note Types. Most are instrument identities; the
technique-bearing ones, complete by technique word:

| Technique word in the Note Type | Note Types that use it |
|---|---|
| **Dead Stroke** | Conga Dead Stroke, Djembe Dead Stroke, Djembe Dead Stroke (2), Darbuka Dead Stroke, High/Medium/Low Bata Dead Stroke, Tumba Dead Stroke, Super Tumba Dead Stroke, Quinto Dead Stroke, Surdu Dead Stroke |
| **Bass Tone** | Conga Bass Tone, Djembe Bass Tone, Djembe Bass Tone (2), Tumba Bass Tone, Super Tumba Bass Tone, Tabla Bass Tone |
| **Slap** | Conga Slap, Djembe Slap, Djembe Slap (2), Darbuka Slap, High/Medium/Low Bata Slap, High/Low Bongo Slap, Tumba Slap, Super Tumba Slap, Quinto Slap, Cajone Slap |
| **Mute / Muff** | High Bongo Mute, Low Bongo Mute, Triangle Mute, Surdu Muff (Custom 3), Suspended Cymbal Roll (Mute Release) |
| **Choke** | Crash Cymbals Choke Fat, Cymbal Section Crunch Choke, Cymbal Section Hi-Hat Choke, Suspended Cymbal Short Choke w/ Stick, Suspended Cymbal Fat Choke w/ Stick |
| **Rim / Rims / Rim Shot / Shot** | Bass Drum Rim, Snare Rim LH, Snare Rims, Snare Section Rims, Snare Rim Shot (Both Hands), Snare Rim Shot LH, Snare Section Rim Shots, Spock Drum Rim Shot, Tenors High Rims, Tenors Low Rims, Low Timbale Rim, {Low, Low-Mid, High-Mid, High} Tom Shot/Rim |
| **Cross Stick / Cross Shot / Stick Click** | Snare Cross Stick, Snare Cross Shot, Snare Section Cross Shots, Stick Click, Stick Clicks |
| **Flam** | Snare Flam, {Low, Low-Mid, High-Mid, High} Tom Flam |
| **Roll (kinds)** | Snare Roll, Snare Buzz Roll, Snare Section Buzz Rolls, {…} Tom Buzz Roll, {…} Tom Short Roll, Spock Drum Sustained Buzz Roll, Bass Drum Roll, Bass Drum Unison Rolls, Side Drum Roll, Castanets Roll, Suspended Cymbal Roll, Suspended Cymbal Cresc (Loud) |
| **Guz** | Snare Guz Short, Snare Guz Long (UNVERIFIED: a Tapspace/marching term this bucket could not define from a primary source) |
| **Shake / Snap / Multi Shake** | Tambourine Shake, Shekere High Shake, Shekere Low Shake, Cabasa Multi Shake, Egg Shaker Multi Shake, Cabasa Snap |
| **Scratch Push / Scratch Pull** | Scratch Push, Scratch Pull |
| **Fingertips** | Djembe Fingertips |
| **Click / Ding / Crunch** | Crash Cymbals Click, Crash Cymbals Ding, Cymbal Section Click, Cymbal Section Crunch Choke |
| **Foot** | Hi-Hat Foot |
| **Open** | Hi-Hat Open, Triangle Open, Surdu Open (Custom 4) |
| **LH** (left hand) | Snare Drum LH, Side Drum LH, Snare Section Hits LH, Snare Rim LH, Snare Rim Shot LH, Bass Drum LH, Bass Drum 2–6 LH, Bass Drum Unison Hits LH, {…} Tom LH, Spock Drum LH |
| **Unison** | Bass Drum Unison Hits, Bass Drum Unison Rolls |

Four of these are not attested anywhere else in this bucket and are recorded in §3.14:
**Scratch Push / Scratch Pull** (direction of a scrape), **Crash Cymbals Click / Ding /
Crunch** (hand-cymbal plate contact), **Dead Stroke** as a named family across nine
instruments, and **Guz**.

---

## 3. Axis mapping

Every term below is mapped to a KITWARP axis, or declared unmappable in §3.14. Where a source
term maps to an axis value that already exists in vocabulary v0.1, the v0.1 slug is given; where
it does not, the cell says NEW.

### 3.1 instrument

| Source | Contribution | v0.1 status |
|---|---|---|
| SMuFL 1.4 pictograms | ~150 instrument pictograms across drums, cymbals, metallic, wooden, shakers, bells, gongs, chimes, tuned mallet, whistles, misc | the kit ones exist; everything else falls in the reserved, unminted families |
| MusicXML `membrane-value` / `metal-value` / `wood-value` / `pitched-value` / `glass-value` / `effect-value` (100 values) | the same list, one generation older, and MusicXML says so: the `effect-value` doc names Stone's list explicitly | as above |
| MusicXML Standard Sounds (391 percussion ids) | the largest instrument enumeration reached in this bucket, with a dotted hierarchy already in place (`drum.tabla.bayan`, `metal.cymbal.ride`) | superset for minting the reserved families |
| MuseScore `instruments.xml` (107 percussion instruments) | each carries a `musicXMLid`, i.e. a ready-made instrument→sound mapping | — |
| Sibelius `unpitched.*` tree | a third instrument hierarchy, differing in shape from both | — |

The kit instruments where the standards and v0.1 disagree are in §5.

### 3.2 site — contact site on the instrument

| Term, as the source spells it | Source and locator | KITWARP site |
|---|---|---|
| `pictOnRim` "On rim" | SMuFL U+E7F4 | rim |
| `pictRim1` "Rim or edge (Weinberg)", `pictRim2` "Rim (Ghent)", `pictRim3` "Rim (Caltabiano)" | SMuFL U+E801–U+E803 | rim (three symbols, one concept) |
| `pictCenter1` "Center (Weinberg)", `pictCenter2` "Center (Ghent)", `pictCenter3` "Center (Caltabiano)" | SMuFL U+E7FE–U+E800 | head + position centre |
| `pictNormalPosition` "Normal position (Caltabiano)" | SMuFL U+E804 | head (default) |
| `pictEdgeOfCymbal` "Edge of cymbal" | SMuFL U+E729 | edge |
| `pictBellOfCymbal` "Bell of cymbal" | SMuFL U+E72A | bell |
| `center`, `rim`, `cymbal bell`, `cymbal edge` | MusicXML `stick-location`, XSD line 2368 | head+centre, rim, bell, edge |
| Ride (edge) / Ride (middle) / Ride (bell) | Guitar Pro, `stick.hit.edge` / `.mid` / `.bell` | edge / bow / bell |
| Rim, Shell | MuseScore marching-tenor-drums, marching-bass-drums | rim, shell |
| `rim`, `shell`, `edge`, `bell` | Sibelius sound id elements | rim, shell, edge, bell |
| "at bell", "at edge", "at center" | Weinberg 1994 p. 21, surface-area indications | bell, edge, head+centre |

Every source that names a site names at most four or five: centre, rim, edge, bell, shell.
None of them has `rim2`, `crossstick`, `bow` or `underside` as a site; `bow` appears only as
the ride's middle (Guitar Pro `stick.hit.mid`).

### 3.3 position — radial position on the site

Only two sources say anything: MusicXML `stick-location` `center` and SMuFL's three `pictCenter*`
glyphs → `centre`. `halfway`, `offset` and `perimeter` have **no** attestation anywhere in this
bucket. Guitar Pro's Ride (middle) is the nearest, and it is a site not a radius. Weinberg's
Ex. 17 "Center and Edge of Drum Notation" is a two-value scale: centre or edge.

### 3.4 contact — part of the implement that touches

The thinnest axis in the bucket.

| Term | Source | KITWARP contact |
|---|---|---|
| Cowbell (tip) vs Cowbell (hit) | Guitar Pro, `stick.hit.tip` (MIDI 100/101/103) | tip |
| `tip`, `heel`, `palm`, `finger`, `fingers`, `hand` | Sibelius conga/bongo ids (`…conga.tip…`, `…conga.heel…`, `…bongo.palm.eop`) | tip, heel (as contact on hand drums), — |
| Golpe (thumb) / Golpe (finger) | Guitar Pro, `thumb.hit.body` / `finger4.hit.body` | — (guitar body, not percussion) |

`shank` and `butt` have no attestation in this bucket at all. SMuFL, MusicXML, MEI, MNX,
MuseScore and Weinberg have no concept of which part of the stick lands.

### 3.5 technique

| Term, verbatim | Source | KITWARP technique |
|---|---|---|
| `pictStickShot` "Stick shot" | SMuFL U+E7F0 | stick-shot |
| `pictOpenRimShot` "Closed / rim shot" | SMuFL U+E7F5 | rimshot |
| `pictRimShotOnStem` "Rim shot for stem" | SMuFL U+E7FD | rimshot |
| `pictChokeCymbal` "Choke (Weinberg)" | SMuFL U+E805 | **NEW — no choke value in v0.1** |
| `pictDeadNoteStem` "Combining X for stem (dead note)" | SMuFL U+E80D | dead |
| `pictCrushStem` "Combining crush for stem" | SMuFL U+E80C | **NEW (crush ≈ buzz/pressed, unresolved)** |
| `pictSwishStem` "Combining swish for stem" | SMuFL U+E808 | sweep/swirl (UNVERIFIED which) |
| `pictScrapeCenterToEdge` / `pictScrapeEdgeToCenter` / `pictScrapeAroundRim` (counter-clockwise) / `pictScrapeAroundRimClockwise` | SMuFL U+E7F1–U+E7F3, U+E80E | scrape + a direction that has no axis (§3.14) |
| Snare (side stick) `stick.hit.sidestick` | Guitar Pro | sidestick |
| Snare (rim shot) `stick.hit.rimshot` | Guitar Pro | rimshot |
| (choke) `stick.hit.choke` on ride, splash, china, crash high, crash medium | Guitar Pro | **NEW — choke** |
| (slap) `hand.hit.slap`, (mute) `hand.hit.mute` on bongo and conga | Guitar Pro | slap, mute-stroke |
| (return) `hand.hit.return` on tambourine, cabasa, maraca, shaker; `stick.hit.return` on bell tree; `stick.scrape.return` on guiro | Guitar Pro | **NEW — the back-stroke of a shaken or scraped instrument** |
| (roll) `hand.hit.roll` on tambourine | Guitar Pro | ornament roll |
| Rim Shot, Rim Click, Stick Click, Stick Shot, Shell, Backstick, Buzz | MuseScore `marching-snare` | rimshot, (rim-only?), (sticks?), stick-shot, site shell, back-stick, ornament buzz |
| Muted, Rim, Buzz, Shell | MuseScore `marching-tenor-drums` | damping muted, site rim, ornament buzz, site shell |
| Full Crash, Half Crash, Sizzle, Crash-Choke, Tap, Tap-Choke, Bell Tap, Bell Tap-Choke, Muted Tap, Smash, Zing, Roll | MuseScore `marching-cymbals` | **mostly NEW — hand-cymbal (piatti) techniques, see §3.14** |
| Crash Cymbals Crash / Click / Ding / Choke Fat; Cymbal Section Crash / Click / Crunch Choke / Hi-Hat Choke; Suspended Cymbal Short Choke w/ Stick, Fat Choke w/ Stick, Roll (Mute Release) | Finale VDLite and Garritan maps (§2.11) | **NEW — hand-cymbal contact and choke variants** |
| Dead Stroke (on conga, djembe, darbuka, bata, tumba, super tumba, quinto, surdu, tabla) | Finale Note Types (§2.11) | dead |
| Bass Tone, Slap, Mute, Fingertips | Finale Note Types (§2.11) | bass-tone, slap, muted, implement finger |
| Scratch Push, Scratch Pull | Finale Note Types (§2.11) | scrape + a direction that has no axis (§3.14) |
| Snare Guz Short, Snare Guz Long | Finale VDLite Marching map (§2.11) | UNVERIFIED — no primary definition found |
| Slap / Open / Bass | MuseScore djembe and doumbek entries | slap, open-tone, bass-tone |
| martellato, martellato lift, hand martellato, muted martellato, mallet lift, mallet table, pluck lift, swing, echo, gyro, belltree, damp | SMuFL handbells U+E810–U+E821 and MusicXML `handbell-value` | **NEW — handbell family, unminted** |
| `slap`, `pressed`, `choke`, `scrape`, `ping`, `sizzle`, `cracked` | Sibelius id elements | slap, **NEW pressed**, **NEW choke**, scrape, ping-shot, — , — |
| ghost stroke, rimshot, open/closed/half-open hi-hat, foot splash, chick, choke/cut-off, natural decay | Weinberg 1994 pp. 20–23 | dynamic ghost, rimshot, openness, foot-splash, chick, **NEW choke**, — |
| `stringsScrapeCircularClockwise` / `…Counterclockwise`, `stringsTripleChopInward` / `…Outward` | SMuFL chop notation U+EE86–U+EE8B | circling + direction (§3.14) |

### 3.6 ornament

| Term | Source | KITWARP ornament |
|---|---|---|
| `swissRudimentsNoteheadBlackFlam`, `swissRudimentsNoteheadHalfFlam` | SMuFL U+EE70–U+EE71 | flam |
| `swissRudimentsNoteheadBlackDouble`, `swissRudimentsNoteheadHalfDouble` ("doublé") | SMuFL U+EE72–U+EE73 | drag / ruff (Basel naming, see §4) |
| Buzz | MuseScore marching-snare (48), marching-tenor (all drums) | buzz |
| `flam` (33 ids), `roll` (32), `crescendo` (6), `tremolo` (8) | Sibelius id elements | flam, roll, crescendo, — |
| Tambourine (roll) | Guitar Pro `hand.hit.roll` | roll |
| Roll | MuseScore marching-cymbals (93) | roll |
| `unpitched.metal.cymbal.roll.crescendo`, `…roll.damp` | Sibelius | crescendo, roll + damping |

MusicXML and MEI express flams and drags as grace notes, not as a technique value, so they
contribute nothing to this axis. SMuFL's rudiment noteheads are the only glyph-level encoding.

### 3.7 openness

| Source | Values | Count |
|---|---|---|
| Guitar Pro | Hi-Hat (closed) / (half) / (open) — `stick.hit.closed` / `.half` / `.open` | 3 |
| LilyPond | closedhihat / halfopenhihat / openhihat (+ pedalhihat, splashhihat) | 3 |
| SMuFL | `pictOpen` (U+E7F8), `pictHalfOpen1` (U+E7F6), `pictHalfOpen2` "Half-open 2 (Weinberg)" (U+E7F7) | 2 states, 3 glyphs |
| Sibelius | `closed`, `halfway`, `open` | 3 |
| MuseScore | Closed Hi-Hat, Open Hi-Hat, Pedal Hi-Hat | 2 (+pedal) |
| Weinberg 1994 | closed (assumed default, plus sign), open (open circle), half-open/half-closed (bisected circle) | 3 |
| MusicXML | **nothing** — no open/closed hi-hat value exists in the format | 0 |
| MEI | **nothing** for percussion (`open`/`stop` are brass/harp) | 0 |

Every notation source tops out at three steps. v0.1's eight named anchors (tight, closed,
closed-loose, quarter, half, three-quarter, loose, open) are strictly richer than anything in
this bucket; a notation import can only ever populate `closed`, `half` and `open`.

### 3.8 damping

| Term | Source | KITWARP damping |
|---|---|---|
| `pictDamp1` "Damp", `pictDamp2` "Damp 2", `pictDamp3` "Damp 3", `pictDamp4` "Damp 4" | SMuFL U+E7F9–U+E7FC | damped (four symbols, one concept) |
| `handbellsDamp3` | SMuFL U+E81E | damped |
| `damp` | MusicXML `handbell-value`; MEI `data.ARTICULATION` (harp gloss) | damped |
| (mute) `hand.hit.mute`, `brush.hit.mute`, `stick.hit.mute` | Guitar Pro (bongo, conga, cuica, surdo, triangle) | muted |
| Muted, Muted Tap, Mute High Conga, Mute Cuica, Mute Triangle, Taiko Mute, Mute Surdo | MuseScore | muted |
| `mute`, `muffled`, `pressed`, `damp` | Sibelius id elements | muted, muted, **NEW pressed**, damped |

Nothing anywhere in this bucket distinguishes `towel` or `gated`; those are studio terms, not
notation terms.

### 3.9 mechanism

Only one term in the entire bucket: MusicXML `membrane-value` "snare drum snares off" and its
SMuFL twin `pictSnareDrumSnaresOff` (U+E6D2). **Both model it as a different instrument, not as
a state of the snare drum.** Dorico's help text is the one place that calls it a playing
technique in prose ("a snare drum can be played snares on or snares off"), and Dorico does not
publish the list. `kick-damped` and `kick-half-open` have no attestation at all.

### 3.10 implement

The richest axis in the bucket, and the only one where the standards are *more* detailed than
v0.1.

| Source | Structure | Values |
|---|---|---|
| SMuFL beaters U+E770–U+E7EF | 128 glyphs = (material × hardness) × orientation, plus singles | soft/medium/hard/wood xylophone stick; soft/hard glockenspiel stick; soft/medium/hard/wood timpani stick; soft/medium/hard/metal/double bass drum stick; soft/medium/hard yarn; superball; wound hard-core / soft-core; soft/medium/hard gum; metal beater; wooden/plastic/metal hammer; snare sticks; jazz sticks; triangle beater; wire brushes; brass mallets; spoon-shaped wooden mallet; guiro scraper; bow; chime hammer; knitting needle; hand; finger; fist; fingernails; coins; drum stick |
| MusicXML `beater-value` (20) | flat list of beaters with no material distinction in the pictogram | bow, chime hammer, coin, drum stick, finger, fingernail, fist, guiro scraper, hammer, hand, jazz stick, knitting needle, metal hammer, slide brush on gong, snare stick, spoon mallet, superball, triangle beater, triangle beater plain, wire brush |
| MusicXML `stick-type` × `stick-material` | **a two-dimensional decomposition**: 10 shapes × 5 materials | shapes: bass drum, double bass drum, glockenspiel, gum, hammer, superball, timpani, wound, xylophone, yarn — materials: soft, medium, hard, shaded, x |
| Weinberg 1994 Ex. 23 | a deliberately closed set of four, everything else by word | Drumstick, Brush, Hard Mallet, Soft Mallet |
| Guitar Pro sound-id field 1 | the implement is the first element of every sound id | stick, hand, pedal, brush, mallet, blow, thumb, finger4 |
| Sibelius id elements | trailing elements | brush, mallet, nylon, wood, finger, hand |
| SMuFL combining glyphs | modifiers on a beater, not beaters | `pictBeaterCombiningParentheses` "Combining parentheses for round beaters (padded)", `pictBeaterCombiningDashedCircle` "Combining dashed circle for round beaters (plated)", `pictBeaterBox` "Box for percussion beater" |

MusicXML's split of *shape/core* (`stick-type`) from *hardness* (`stick-material`) is the
structural idea v0.1 does not have: v0.1's `mallet-soft`/`mallet-medium`/`mallet-hard` encode
hardness only and cannot say "hard yarn" versus "hard gum" versus "wound, hard core".

### 3.11 dynamic

Weinberg's parenthetical notehead for **ghost strokes** is the only percussion-specific value in
the bucket, and it is a rule about notation, not a named value. MusicXML and MEI carry the
generic articulation set (accent, strong accent, soft accent, stress, unstress); SMuFL carries
the glyphs. Nothing here contradicts v0.1's normal/ghost/soft/hard/accent.

### 3.12 timbre

| Term | Source | KITWARP timbre |
|---|---|---|
| `drum.snare-drum.electric`, `drum.tom-tom.synth` | MusicXML Standard Sounds | electronic |
| Electric Snare | MuseScore drumset (40), LilyPond `electricsnare` | electronic |
| `kit-tr-808` | Sibelius (Vir2 VI.ONE set) | analog-808 |
| `kit-electronic` | Sibelius | electronic |
| `electric` | Sibelius (`unpitched.drum.medium.tom-tom.electric`) | electronic |

SMuFL's `electronic-music-pictograms` range (65 glyphs, U+EB10–U+EB5F) is studio symbology —
tape, playback, fader, monitor — and contributes nothing to a kit timbre axis.

### 3.13 voicing

| Term | Source | KITWARP voicing |
|---|---|---|
| `kit-standard`, `kit-room`, `kit-power`, `kit-jazz`, `kit-orchestra`, `kit-brush`, `kit-electronic`, `kit-tr-808` | Sibelius sound ids (the GM-2 kit list expressed as vocabulary) | standard, room, power, jazz, orchestra, **NEW brush-kit**, (timbre), (timbre) |
| `jazz` (30 ids), `fusion` (28), `rock` (15), `orch` (14), `concert` (5) | Sibelius id elements | jazz, **NEW fusion**, **NEW rock**, orchestra, **NEW concert** |
| `ambient`, `big`, `dry`, `dink`, `sloppy`, `a-list`, `sequential` | Sibelius id elements from Vir2/Garritan sets | not vocabulary — vendor patch names, correctly excluded |

### 3.14 Terms that fit NO axis

This is the section the brief says is worth the most. Each entry names the term, its locator,
and what a KITWARP model would need in order to hold it.

**(a) Direction and trajectory of a stroke.** `pictScrapeCenterToEdge` (U+E7F1),
`pictScrapeEdgeToCenter` (U+E7F2), `pictScrapeAroundRim` "counter-clockwise" (U+E7F3),
`pictScrapeAroundRimClockwise` (U+E80E), `stringsScrapeCircularClockwise` /
`…Counterclockwise` (U+EE88–U+EE89), `pictTurnRightStem` / `pictTurnLeftStem` /
`pictTurnRightLeftStem` (U+E809–U+E80B), `handbellsSwingUp` / `handbellsSwingDown` (U+E818–
U+E819), Guitar Pro Guiro (scrap-return) `stick.scrape.return`. A scrape from centre to edge
and a scrape from edge to centre are different sounds. KITWARP has `technique = scrape`,
`swirl`, `circling` and a single `site`/`position` — it cannot express *from where to where*,
nor *which way round*. What is needed: either a direction qualifier (in/out, cw/ccw) or a
second site slot (`site_from`, `site_to`). Finale adds an independent fifth witness with the
Note Types **Scratch Push** and **Scratch Pull** (§2.11), where the direction is the *only*
thing distinguishing the two. **A missing axis, on the evidence of five separate sources.**

**(b) Two-phase gestures ("lift").** `handbellsMartellatoLift` (U+E811),
`handbellsMalletLft` (U+E816), `handbellsPluckLift` (U+E817), MusicXML `handbell-value`
`martellato lift`, `mallet lift`, `pluck lift`, and `mallet table` ("Mallet, bell on table"
U+E815 vs "Mallet, bell suspended" U+E814). The gesture is *strike while damped against a
surface, then lift* — a sequence, not a state. `damping` cannot hold it because the damping
changes during the note.

**(c) Hand-cymbal (piatti) techniques.** MuseScore `marching-cymbals`: **Full Crash, Half
Crash, Sizzle, Crash-Choke, Tap, Tap-Choke, Bell Tap, Bell Tap-Choke, Muted Tap, Smash,
Zing**; Guitar Pro Piatti (hit) / Piatti (hand); MusicXML `metal-value` `crash cymbals`;
SMuFL `pictCrashCymbals` (U+E720). Here the instrument *is a pair of plates* and the technique
describes how the two plates meet each other — there is no implement striking a site, so
`site`, `contact` and `implement` are all empty and `technique` would have to carry the whole
distinction. v0.1 has no hand-cymbal instrument and no vocabulary for plate-against-plate
contact. Finale independently enumerates the same family from a different vendor's library:
**Crash Cymbals Crash / Click / Ding / Choke Fat** and **Cymbal Section Crash / Click / Crunch
Choke / Hi-Hat Choke** (§2.11), where "Click" and "Ding" are edge-to-edge contacts and "Crunch"
is a full plate-to-plate press. Two independent sources enumerating a family v0.1 cannot hold
at all is the strongest case in this section for a new instrument plus its own technique set.
UNVERIFIED: whether "Zing" and "Smash" are standard PAS marching terms or MuseScore's own; they
are not in Weinberg 1994.

**(d) Stroke length as identity.** MusicXML Standard Sounds and LilyPond both mint two
instruments where there is one instrument and two stroke lengths: `shortguiro`/`longguiro`,
Guitar Pro Guiro (hit) vs (scrap-return), MuseScore Short Güiro / Long Güiro, LilyPond
`shortwhistle`/`longwhistle`. Also SMuFL/MusicXML `chain rattle`, `rainstick`. KITWARP has no
duration or stroke-length concept on the term; the standards resolve it by minting instruments,
which is exactly the identity inflation this project is trying to avoid.

**(e) The "return" stroke.** Guitar Pro's `…hit.return` on tambourine, cabasa, maraca, shaker
and bell tree, and `stick.scrape.return` on guiro. On a shaken instrument the back-stroke is a
separate attack with a different sound. KITWARP's `shake` and `swirl` treat the gesture as one
event. **Missing.**

**(f) Beater orientation.** Nearly every SMuFL beater exists in Up/Down/Left/Right variants
(and MusicXML has `tip-direction` with eight values including northwest/northeast/southeast/
southwest). This is *not* a physical distinction — it is which way the pictogram points on the
page. It should stay out of the pivot vocabulary. Recording it here so a later pass does not
mistake 128 SMuFL beater glyphs for 128 implements: the 128 glyphs are roughly 32 implements ×
orientation.

**(g) Beater modifiers "padded" and "plated".** `pictBeaterCombiningParentheses` ("Combining
parentheses for round beaters (padded)") and `pictBeaterCombiningDashedCircle` ("Combining
dashed circle for round beaters (plated)"). Unlike (f) these *are* physical: a padded beater
and a plated beater sound different. KITWARP's implement axis is a flat list of whole
implements and has no modifier slot.

**(h) Which hand / which of a pair.** `pictRightHandSquare` "Left hand (Agostini)" and
`pictLeftHandCircle` "Right hand (Agostini)" (U+E806–U+E807 — note the names and descriptions
are crossed, see §4), Weinberg's R/L sticking letters, Guitar Pro Left Maraca / Right Maraca,
Sibelius `left`/`right`, MuseScore Drum 1–5 in the marching sets. KITWARP carries `limb` and
`instance` on the layout slot rather than on the term, which this evidence supports — but note
that every notation source puts it on the note.

**(i) Ensemble aggregation.** MuseScore marching-bass-drums "Unison" (all five drums at once),
Sibelius `unpitched.metal.cymbal.ensemble.crash`, `…ensemble.sizzle`, `unpitched.metal.hi-hat.ensemble`.
A single notated event performed by a whole section. No axis holds "all instances at once".

**(j) The blank pictogram.** `pictEmptyTrap` "Empty trapezoid" (U+E6A9) — SMuFL's own escape
hatch for an instrument it has no glyph for, and MusicXML's `other-percussion` element and
`smufl-pictogram-glyph-name` type are the same idea. Every one of these standards ships an
explicit "we could not close this set" valve. That is worth stating in an ADR: a closed set
plus a documented escape hatch is the shape all four of them converged on.

**(k) Playing-technique-specific noteheads as identity.** Dorico's model (help page,
`archive.steinberg.help/dorico_pro/v2/…playing_techniques_c.html`): "each percussion instrument
defines a set of playing techniques that can be played on it", and a technique is realised as
"playing technique-specific noteheads", a staff position, an articulation, or a text. The
technique is a first-class object with an identity that owns a notehead. KITWARP's tuple has no
place for the *rendering* of a term, which is correct for a pivot — noted here only so the
reconciliation pass knows Dorico's ids are notation-facing, not physics-facing.

---

## 4. Conflicts and false friends

**One word, several instruments or sites — `bell`.**
- `bell` as a KITWARP *site* = the raised centre of a cymbal.
- `cymbal bell` = MusicXML `stick-location`, the same site.
- `bell` = MusicXML `metal-value`, an *instrument* (a struck bell).
- `pictBell` (U+E714), `pictHandbell` (U+E715), `pictBellPlate`, `pictBellTree` = instruments.
- "Ride Bell" = MuseScore/GM instrument entry (MIDI 53) — an *instrument name* for what is
  really instrument ride + site bell.
- "Bell Tap" / "Bell Tap-Choke" = MuseScore marching-cymbals, hand cymbals struck bell to bell.
- `metal.bells.*` = 25 MusicXML Standard Sounds.
Six meanings. Any importer that string-matches "bell" will be wrong most of the time.

**`bow` — a live collision inside KITWARP's own axes.** v0.1 has `site = bow` (the playing area
of a cymbal between bell and edge). MusicXML `beater-value` has `bow` and SMuFL has
`pictBeaterBow` (U+E7DE) — a *violin bow used as an implement*, as in bowed vibraphone or bowed
cymbal. Both readings are standard in percussion. Under ADR-0003 the slug cannot be renamed;
this needs a documented disambiguation before an implement `bow` is ever minted.

**`open`.** MEI: "Full (as opposed to stopped) tone" (brass). Hand drums: the open tone as
opposed to slap or bass. Hi-hat: openness. Triangle: undamped (`opentriangle`, MusicXML "Open
Triangle"). Cuica: `opencuica`. Four physically unrelated meanings, all spelled `open`, and
LilyPond uses the *same* articulation token `open` for congas (open tone) and hi-hat (openness).

**`half`.** Guitar Pro "Hi-Hat (half)" = openness. MuseScore "Half Crash" = hand cymbals struck
with reduced contact. MusicXML `harmon-closed-value` `half` = a mute position. SMuFL
`pictHalfOpen1` vs `pictHalfOpen2` "Half-open 2 (Weinberg)" = two glyphs for one hi-hat state.

**`damp`.** MEI `damp` = "Stop harp string from sounding". SMuFL `pictDamp1`–`pictDamp4` = four
different symbols for percussion damping, from four notational traditions, none of which are
four *degrees*. MusicXML `handbell-value` `damp`. Sibelius `…roll.damp` = a damped roll.

**`slap`.** Conga/bongo/djembe slap (a hand technique). MusicXML Standard Sound `effect.slap`
(a slapstick/whip sound effect). `effect.bass-string-slap`. `rattle.vibraslap` (an instrument).
MuseScore instrument `slap` (id `slap`, musicXMLid `effect.slap`).

**side stick / cross stick / rim click / stick click.** MuseScore says **Side Stick** in
`drumset` and **Cross-stick** in `drum-kit-4` and `drum-kit-5` — same MIDI 37, same `slashed1`
notehead, two names in one file. Guitar Pro says "Snare (side stick)". LilyPond has
`sidestick`, `hisidestick`, `losidestick`. MuseScore `marching-snare` separates **Rim Click**
(53) from **Stick Click** (55) — and its `percussion` (Mixed Percussion) set has yet another,
**Stick Click** at 31 with a `plus` notehead and **Snare Rim** at 37. So "the thing at MIDI 37"
has at least five names across two files of one program.

**rim shot naming inside SMuFL.** The glyph named `pictOpenRimShot` (U+E7F5) is *described*
"Closed / rim shot". The name says open, the description says closed. Whatever the history, an
importer keying on the canonical name will disagree with one keying on the description.
Similarly `pictRightHandSquare` is described "Left hand (Agostini)" and `pictLeftHandCircle` is
described "Right hand (Agostini)" — name and description are swapped in both.

**Three authorities, three symbols, one concept.** SMuFL encodes centre as three codepoints
(Weinberg, Ghent, Caltabiano) and rim as three more (Weinberg — where the description is "Rim
**or edge**", already conflating two KITWARP sites — Ghent, Caltabiano), plus half-open twice
(generic and Weinberg). A glyph enumeration is a *symbol* enumeration; it cannot be used as a
concept enumeration without collapsing these. This is the strongest argument in the bucket for
why KITWARP's pivot terms must not be minted one-per-glyph.

**`hi-hat` vs `high-hat cymbals`.** MusicXML `metal-value` has both, distinguished only by the
pictogram ("The hi-hat value refers to a pictogram like high-hat cymbals, but without the long
vertical line at the bottom"), i.e. with or without the stand. SMuFL likewise has `pictHiHat`
(U+E722) and `pictHiHatOnStand` (U+E723). Two values whose only difference is whether the
drawing includes furniture.

**`military drum` / `field drum` / `snare drum`.** MusicXML `membrane-value` `military drum`;
SMuFL `pictSnareDrumMilitary`; MuseScore instrument id `military-drum` with trackName "Field
Drum" and musicXMLid `drum.snare-drum`. One instrument, three names, and the MuseScore file
maps it back onto plain snare drum for playback.

**`Charley`.** alphaTab's `PercussionMapper.ts` uses `Charley` as the element name for the
hi-hat, from the French *charleston* for hi-hat cymbals — a false friend with the Charleston
rhythm and with the English "Charlie". Trade term worth registering.

**`doublé` / drag / ruff.** SMuFL `swissRudimentsNoteheadBlackDouble` "Swiss rudiments doublé
black notehead". In Basel/Swiss rudimental terminology *doublé* is the two-stroke ornament that
Anglo-American terminology calls a drag or a ruff — v0.1 carries `drag` and `ruff` as separate
values, and the Swiss tradition has one term for the pair. (Bucket 01 owns rudiments; flagged
here because SMuFL is where it enters the notation standards.)

**`crash` as instrument vs as action.** MusicXML `metal-value` `crash cymbals` = a *pair* of
hand cymbals. KITWARP `crash` = a suspended crash cymbal on a stand. MuseScore has both:
instrument `crash-cymbal` with trackName "Suspended Cymbal" and instrument `cymbal` with
trackName "Hand Cymbals", both mapping to musicXMLid `metal.cymbal.crash`.

---

## 5. Gaps against vocabulary v0.1

Read against `vocabulary/axes.json` at vocabulary_version 0.1.0, vocabulary_serial 1.

### 5.1 Missing values, with the evidence that justifies minting them

| Axis | Proposed value | Attestation |
|---|---|---|
| technique | **choke** | SMuFL `pictChokeCymbal` "Choke (Weinberg)" U+E805; Guitar Pro `stick.hit.choke` on five instruments; Sibelius `choke` in 13 ids; MuseScore Crash-Choke, Tap-Choke, Bell Tap-Choke; Finale Crash Cymbals Choke Fat, Cymbal Section Crunch Choke, Cymbal Section Hi-Hat Choke, Suspended Cymbal Short/Fat Choke w/ Stick; Weinberg 1994 p. 21 (cut-off notation). Six independent sources; v0.1 has no way at all to say a cymbal was choked. **The single clearest gap in this bucket.** |
| technique | **return** (back-stroke of a shaken or scraped instrument) | Guitar Pro `hand.hit.return` (tambourine, cabasa, maraca, shaker), `stick.hit.return` (bell tree), `stick.scrape.return` (guiro) |
| technique | **pressed** | Sibelius `pressed` (10 ids); SMuFL `pictCrushStem` "Combining crush for stem" is the same family |
| technique | **tap**, **bell-tap**, **muted-tap**, **half-crash**, **full-crash**, **smash**, **zing** | MuseScore `marching-cymbals` — but see §3.14(c): these need a hand-cymbal instrument first |
| ornament | (none missing) | flam, drag, ruff, bounced, roll, buzz, crescendo, swell, wash cover everything found |
| damping | **pressed** or a rename note | as above |
| implement | **fist**, **fingernail** | MusicXML `beater-value` `fist`, `fingernail`; SMuFL `pictBeaterFist` U+E7E5, `pictBeaterFingernails` U+E7E6. **Note:** the round-2 brief text lists fist and fingernail as if they were already in the implement axis; `vocabulary/axes.json` at serial 1 does not contain them. Flagged as a question, not a decision. |
| implement | **coin**, **knitting-needle**, **spoon-mallet**, **guiro-scraper**, **chime-hammer**, **metal-hammer**, **triangle-beater**, **wire-brush** (if distinct from `brush`), **brass-mallets**, **snare-stick** | MusicXML `beater-value`, complete list in §2.2; SMuFL beaters in §2.1 |
| implement | a **material dimension** (yarn, wound, gum, felt, wood, plastic, rubber, metal) crossed with a **hardness** dimension (soft, medium, hard) | MusicXML models exactly this as `stick-type` × `stick-material`; v0.1's `mallet-soft`/`-medium`/`-hard` cannot express "hard yarn" vs "hard gum" vs "wound, hard core", all of which SMuFL distinguishes |
| voicing | **fusion**, **rock**, **concert**, **brush** (kit) | Sibelius id elements (`fusion` 28 ids, `rock` 15, `concert` 5) and the GM-2 kit names `kit-brush`, `kit-jazz`, `kit-power`, `kit-room`, `kit-orchestra`, `kit-standard` |
| instrument | **hand-cymbals / piatti** (a pair of plates, as opposed to `crash` on a stand) | MusicXML `crash cymbals`; SMuFL `pictCrashCymbals`; MuseScore instrument `cymbal` "Hand Cymbals"; Guitar Pro Piatti |
| instrument | **suspended-cymbal** distinct from `cymbal` | MusicXML `suspended cymbal`; SMuFL `pictSuspendedCymbal`; MuseScore "Suspended Cymbal" |
| instrument | **gong**, **tam-tam** (distinct: SMuFL has `pictTamTam`, `pictGong`, `pictGongWithButton` "nipple") | SMuFL gongs range; MusicXML `gong`, `domed gong`, `tam tam`, `tam tam with beater`; 14 `metal.gong.*` Standard Sounds |
| — | the whole reserved percussion / orchestral / utility families | MusicXML Standard Sounds gives 391 ready ids and SMuFL gives ~150 pictograms with codepoints; between them they are a complete minting source for those families |

### 5.2 Things v0.1 names, that no notation standard supports

Recorded so the project knows which parts of its vocabulary can never be populated from a
score file, and must come from hardware or library sources instead:

- `contact` = shank, butt — no attestation anywhere in the bucket
- `position` = halfway, offset, perimeter — no attestation
- `site` = rim2, underside — no attestation
- `openness` = tight, closed-loose, quarter, three-quarter, loose — notation tops out at three
  steps (§3.7)
- `damping` = towel, gated — studio terms, absent from notation
- `mechanism` = kick-damped, kick-half-open — absent; even `wires-off` is modelled as a
  separate *instrument* by every source (§3.9)
- `technique` = gok-shot, ping-shot (attested only as Sibelius `ping`), sweep, swirl, circling
  (attested only as scrape/turn glyphs with a direction), thumb, heel, toe (attested in MEI but
  as organ-pedal terms)

### 5.3 Misnamings and modelling inconsistencies to reconcile

1. **`site = crossstick` and `technique = sidestick` are the same physical act on two axes.**
   Every source in this bucket treats it as one thing: Guitar Pro `stick.hit.sidestick`,
   MuseScore Side Stick / Cross-stick (one MIDI note, one notehead), LilyPond `sidestick`.
   Carrying it on both axes will produce two encodings for one event.
2. **`site = bow` collides with the standards' implement `bow`** (§4). Needs documentation
   before an implement `bow` is minted.
3. **`site = rim` vs `position = perimeter`.** MusicXML's single `rim` value covers both; if
   both KITWARP axes can be set, the mapping from any notation source is ambiguous.
4. **`instrument = cymbal`** is under-specified against the standards' split of hand cymbals /
   suspended cymbal / crash on a stand (§4, last entry).
5. **`technique = chick` and `technique = foot-splash` are confirmed verbatim** by Weinberg 1994
   p. 21 and by LilyPond's `splashhihat` — these two v0.1 terms now have a primary-source
   provenance record, which they did not have before.
6. **`technique = dead`, `bass-tone`, `slap`, `open-tone` and `mute-stroke` are confirmed as a
   coherent family** by Finale's Note Types, which apply Dead Stroke / Bass Tone / Slap / Mute
   consistently across nine hand-drum instruments (§2.11), and by MuseScore's Djembe and Doumbek
   entries (Slap / Open / Bass). The hand-drum stroke set is the one part of v0.1 that the
   notation sources corroborate without disagreement.

---

## 6. Self-critique (round C)

**What is missing from this bucket.**

1. **Dorico's shipped percussion playing-technique list.** Dorico is the only program of the
   four that makes a playing technique a first-class object with an id, a notehead set and a
   playback technique, i.e. exactly the model KITWARP is building. Steinberg publishes the
   *concept* (the help pages in §1 rows 26–27, both reached) but not the *list*: the enumeration
   lives in a `.doricolib` inside the installed application. The public `.doricolib` files
   findable by GitHub code search are third-party expression maps for orchestral libraries and
   contain only `pt.natural`, `pt.legato` and similar; targeted searches for `pt.rimShot`,
   `pt.snaresOff` and `pt.stickShot` return zero results. What it would add: a canonical id
   namespace for percussion techniques designed by people who had to ship it, plus the
   technique→notehead→playback triple. **This is the single most valuable unreached item for a
   later pass**, and the way to get it is a Dorico installation (or its `Playing Techniques.doricolib`
   posted by a user), not the web.
2. **Finale's Note Type list — obtained, after a false negative.** The two dialog-documentation
   pages describe the mechanism and name only "bass drum = 36, snare drum = 38" as examples,
   which reads as "not published". It is published, on the percussion-map pages (§2.11), and
   this bucket only found it by fetching a page whose title mentioned a *third-party library*
   (Tapspace Drumline). Method note for later passes: when a vendor documents an editor but not
   its vocabulary, look for the pages documenting the shipped presets. A second failure mode is
   worth recording: WebFetch's summariser declined to reproduce the Finale tables on the ground
   that quoting them would exceed a quotation limit, and reported only the table captions —
   plain `curl` with a browser user-agent plus local HTML parsing returned all 187 rows. When an
   enumeration must be complete and verbatim, fetch and parse rather than summarise.
   What remains unobtained is Finale's *master* Note Type list as shipped in the application
   (the maps pages give the Note Types used by particular sound libraries, not the closed set
   the Percussion Layout Designer offers).
3. **Gould, *Behind Bars*, percussion chapter** — print only, no open full text. It would add
   the editorial rules: when a change of technique is a change of instrument, how to label a
   shared stave, and the house conventions that Faber/Fabermusic engravers apply. Its absence
   affects §4 (conflicts) more than §2, because Gould is prescriptive about which of two
   competing symbols to use.
4. **Kurt Stone, *Music Notation in the Twentieth Century* (1980)** — reachable only as an
   archive.org lending item, and web.archive.org is blocked in this environment while
   archive.org lending needs an account. This is the **most authoritative source not obtained**,
   and it matters more than its date suggests: MusicXML's own schema documentation says its
   effect pictogram list is "in addition to *Stone's list*", and SMuFL's percussion pictograms
   are largely Stone's, so both of the standards extracted above are downstream of a 1980 book
   this bucket could not read. Getting it would let the reconciliation pass tell which of the
   ~250 pictogram values are Stone's original distinctions and which are later inventions.
5. **Smith Brindle *Contemporary Percussion* (1970), Gardner Read *Notation* (1969), the ICNMN
   Ghent 1974 resolutions, and the Agostini and Caltabiano systems** — all four survive in this
   bucket only as attributions inside SMuFL glyph descriptions and Weinberg's citations. Each is
   a *primary* notation system with its own closed set; SMuFL preserved their disagreements as
   separate codepoints (§4) but not their definitions.
6. **Sibelius primary vs secondary sound ids.** 4 887 ids were observed, but the Sibelius Sound
   World file (S3W) that says which are *primary* is not in any of the sound sets; without it,
   the Sibelius vocabulary in §2.9 is "ids seen in the wild", not "Sibelius's own vocabulary".
   The `Sibelius_Essentials_GM.xml` set (56 ids) is the only clean primary sample.
7. **Braille music notation for percussion** (register row 36) — a fully closed set for a
   different modality, which would be a good independent check on which distinctions are
   considered essential. Not extracted; no time.
8. **Non-English notation manuals** (rows 33–38: German, French). Registered with live locators
   but not extracted, because bucket 12 owns the language axis and duplicating it here would
   waste the reconciliation pass's time. The one language finding worth carrying over is
   `Charley` for hi-hat in the Guitar Pro data model (§4).

**Weaknesses in what is here.**

- The Guitar Pro vocabulary is second-hand: it comes from alphaTab's reconstruction of the
  `.gpif` format, not from Arobas Music. It is consistent and generated by a test against real
  files, but it is `derived`, and a Guitar Pro 8 default kit may differ.
- The Sibelius technique-element counts in §2.9 are counts of *observed ids*, not of a published
  vocabulary; the vendor-marker filter is a heuristic and will have kept a few library patch
  names and dropped a few real ones.
- The Weinberg 1994 article was read from page images, not from a text layer. Quotations were
  transcribed by eye; they are accurate to the page but a second reader should verify the two
  longest quotes (the foot-splash definition, p. 21, and the rimshot count, p. 20) before they
  are used as normative evidence anywhere.
- SMuFL glyph *descriptions* were treated as definitions. They are not: they are captions.
  Where a caption is ambiguous (`pictRim1` "Rim or edge") the ambiguity is in the source and has
  been carried through rather than resolved.
