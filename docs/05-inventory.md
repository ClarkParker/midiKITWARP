# KITWARP — inventory of mapping targets

A work list. The goal is not completeness in the sense of "every device ever built" but a
checkable set that covers realistic demand.

**Status:** `[ ]` open · `[~]` source located, not extracted · `[x]` extracted and validated
· `[-]` dropped, with a reason

**Source type:** `H` manufacturer documentation / manual · `P` preset or mapping file
shipped by the product · `D` DAW drum map · `M` measured here · `?` unclear

Hardware model names come from search and memory and are **to be verified per row** — that
verification is part of working the row, not a precondition for the list.

Every extracted row must carry a provenance record (source, date, method, licence verdict).
A documented gap beats a guessed note.

---

## A. Acoustic drum libraries (VSTi)

The main group. This is where the plugin earns its keep.

| Status | Product | Vendor | Source | Note |
|---|---|---|---|---|
| [~] | Superior Drummer 3 | Toontrack | P/D | `.iom` present |
| [ ] | Superior Drummer 2 | Toontrack | D | own layout |
| [ ] | EZdrummer 3 | Toontrack | D | |
| [~] | EZdrummer 2 | Toontrack | P/D | `.iom` present |
| [ ] | EZdrummer 1 | Toontrack | D | |
| [ ] | Drumkit From Hell / DFHS | Toontrack | D | legacy, appears in GM collections |
| [~] | Addictive Drums 2 | XLN Audio | P/D | `.iom` present |
| [ ] | Addictive Drums 1 | XLN Audio | D | |
| [~] | BFD3 | FXpansion / inMusic | P/D | `.iom` present |
| [ ] | BFD2 / BFD1 | FXpansion | D | |
| [ ] | BFD Eco | FXpansion | D | |
| [ ] | BFD Player | inMusic | H | freeware, good for testing |
| [ ] | BFD Drums (current) | inMusic | H | |
| [~] | SSD5 / SSD 5.5 | Steven Slate | P | `.iom` present; likely origin of the maps |
| [ ] | SSD4 | Steven Slate | D | Reaper note names exist |
| [ ] | SSD3 | Steven Slate | D | |
| [ ] | SSD Free | Steven Slate | H | freeware, good for testing |
| [~] | Studio Drummer | Native Instruments | P/D | `.iom` present |
| [ ] | Abbey Road Drummer (60s/70s/80s/Modern/Vintage) | Native Instruments | D | check one layout per series |
| [ ] | Battery 3 / 4 | Native Instruments | P | kit-dependent, no fixed layout |
| [ ] | GGD Modern & Massive | GetGood Drums | P | `.nka` presets, converter exists |
| [ ] | GGD Invasion | GetGood Drums | P | |
| [ ] | GGD Matt Halpern | GetGood Drums | P | |
| [ ] | GGD One Kit Wonder (series) | GetGood Drums | P | several titles |
| [ ] | GGD Architects | GetGood Drums | P | included in ReaperNoteNames |
| [ ] | MODO Drum | IK Multimedia | D | in the Groove Monkee set |
| [ ] | ML Drums | ML Sound Lab | D | maps for four DAWs available |
| [ ] | Drumforge Classic | Drumforge | P | |
| [ ] | Drumforge Ultimate | Drumforge | P | |
| [ ] | Drumforge Bergstrand | Drumforge | P | |
| [ ] | Power Drum Kit | powerdrumkit.com | H | official maps for Reaper/Cubase/S1 |
| [ ] | MT Power Drum Kit 2 | Manda Audio | H | freeware |
| [ ] | Sennheiser DrumMic'a | Sennheiser | H | freeware |
| [ ] | Larry Seyer Acoustic Drums | Larry Seyer | D | own format in Groove Monkee |
| [ ] | Mixosaurus | Mixosaurus | D | in Groove Monkee |
| [ ] | Perfect Drums | Perfect Drums | ? | |
| [ ] | Ugritone kits | Ugritone | ? | many individual titles |
| [ ] | Wave Alchemy Revolution | Wave Alchemy | ? | |
| [ ] | MDrummer | MeldaProduction | H | |
| [ ] | Jamstix 4 | Rayzoon | P | **ships its own maps for many libraries** |
| [ ] | Ocean Way Drums | Platinum Samples | ? | |
| [ ] | uJAM Virtual Drummer (series) | uJAM | H | SOLID / HEAVY / PHAT / DEEP / 2ND |
| [ ] | VQ Drums | — | ? | |

## B. Electronic drums / samplers / drum-machine plugins

| Status | Product | Vendor | Source |
|---|---|---|---|
| [ ] | Battery 4 factory kits | Native Instruments | P |
| [ ] | Maschine kits | Native Instruments | P |
| [ ] | XO | XLN Audio | ? |
| [ ] | Geist2 | FXpansion | ? |
| [ ] | Spark 2 | Arturia | H |
| [ ] | Nepheton / Drumazon / Punchbox | D16 | H |
| [ ] | BreakTweaker | iZotope | ? |
| [ ] | Punch 2 | Rob Papen | H |
| [ ] | Triaz / Triaz Player | Wave Alchemy | H |
| [ ] | TR-808/909/707/606/626 Plug-Outs | Roland Cloud | H |
| [ ] | Damage 2 | Heavyocity | H |

## C. DAW-internal drum instruments

Each has its own layout and is at the same time an obvious mapping target.

| Status | Product | DAW | Source |
|---|---|---|---|
| [ ] | Groove Agent 5 / SE | Cubase | H |
| [ ] | Groove Agent ONE | Cubase | H |
| [ ] | Drum Kit Designer | Logic | H |
| [ ] | Ultrabeat | Logic | H |
| [ ] | Drum Machine Designer | Logic | H |
| [ ] | Drummer (producer kits) | Logic | H |
| [ ] | Drum Rack factory kits | Ableton Live | P |
| [ ] | Impact XT | Studio One | H |
| [ ] | Kong / Redrum | Reason | H |
| [ ] | FPC | FL Studio | H |
| [ ] | Session Drummer 3 | Cakewalk | P/H |
| [ ] | Studio Instruments Drums | Cakewalk | P/H |
| [ ] | Drum Machine | Bitwig | H |
| [ ] | Boom / Structure | Pro Tools | H |
| [ ] | GarageBand kits | Apple | D |

## D. E-drum modules (hardware)

Roland maintains a "Default MIDI Note Map" support article per module — the best documented
group in this inventory.

### Roland
| Status | Model | Source |
|---|---|---|
| [ ] | TD-1 / TD-02 / TD-07 | H |
| [ ] | TD-3 / TD-4 / TD-6 / TD-6V / TD-8 / TD-9 | H |
| [ ] | TD-10 / TD-11 / TD-12 / TD-15 | H |
| [ ] | TD-17 (+ KV / KVX / KV2 / L) | H — KB article confirmed |
| [ ] | TD-20 | H |
| [ ] | TD-25 | H — KB article confirmed |
| [ ] | TD-27 | H — KB article confirmed |
| [~] | TD-30 | P — `.iom` present |
| [ ] | TD-50 / TD-50X | H |
| [ ] | TD-516 | H — new |
| [ ] | VAD103 / VAD306 / VAD503 / VAD504 / VAD506 / VAD706 | H — confirmed |
| [ ] | SPD-SX / SPD-SX Pro | H |
| [ ] | SPD-30 Octapad / SPD-20 / SPD-11 | H |
| [ ] | TM-1 / TM-2 / TM-6 Pro | H |
| [ ] | HandSonic HPD-20 | H |

### Yamaha
| Status | Model | Source |
|---|---|---|
| [~] | DTX900 / DTX920 | P — `.iom` present |
| [~] | DTXplorer | P — `.iom` present |
| [ ] | DTX400 / 402 / 430 / 450 | H |
| [ ] | DTX500 / 502 / 520 / 522 | H |
| [ ] | DTX700 / 720 / 760 | H |
| [ ] | DTXpress I–IV | H |
| [ ] | DTXtreme I / II / III | H |
| [ ] | DTX-PRO / DTX-PROX / DTX6 / DTX8 / DTX10 | H |
| [ ] | DTX-Multi 12 | H |
| [ ] | EAD10 | H |

### Alesis
| Status | Model | Source |
|---|---|---|
| [~] | DM10 / DM10 MKII | P — `.iom` present |
| [~] | Strike / Strike Pro | P — `.iom` present |
| [ ] | DM5 / DM6 / DM7 / DM8 | H |
| [ ] | Nitro / Nitro Mesh / Nitro Max / Nitro Ultimate | H |
| [ ] | Command / Surge / Forge / Turbo | H |
| [ ] | Crimson / Crimson II | H |
| [ ] | Strata Prime / Strata Core | H |
| [ ] | Strike MultiPad / SamplePad / SamplePad Pro | H |
| [ ] | Trigger iO | H |

### Other vendors
| Status | Model | Vendor | Source |
|---|---|---|---|
| [~] | Mimic Pro | Pearl | P — `.iom` present |
| [ ] | e/Merge | Pearl | H |
| [ ] | DrumIt Five / DrumIt Three | 2Box | H |
| [ ] | aDrums aD5 / xD3 | ATV | H |
| [ ] | EFNOTE 3 / 5 / 5X / 7 / Pro / Mini | EFNOTE | H |
| [ ] | G3 / G5 / G9 / G9 Pro | GEWA | H |
| [ ] | Titan 20 / 50 / 70 | Simmons | H |
| [ ] | SD1000 / SD1200 / SD2000 | Simmons | H |
| [ ] | MPS-150 / 450 / 750X / 850 / 1000 | Millenium | H |
| [ ] | DDTi / DD1 / ddrum4 / ddrum5 | ddrum | H |
| [ ] | Drum 3P / Drum 2 / Drum Pad | Nord | H |
| [ ] | ALCHEM-E | Zildjian | H |
| [ ] | KT2 / KT3 / KTMP1 | KAT Percussion | H |
| [ ] | drumKAT / trapKAT / malletKAT | Alternate Mode | H |
| [ ] | eDRUMin | Audiofront | H |
| [ ] | MegaDrum | DIY | H |
| [ ] | XD80USB | Behringer | H |

## E. Drum machines and grooveboxes (hardware)

The most interesting group for "usable for other things too".

| Status | Model | Vendor |
|---|---|---|
| [ ] | TR-808 / 909 / 707 / 606 / 626 | Roland |
| [ ] | TR-8 / TR-8S / TR-6S | Roland |
| [ ] | R-8 / R-8 MKII | Roland |
| [ ] | SR-16 / SR-18 / HR-16 | Alesis |
| [ ] | MPC (series) | Akai |
| [ ] | Machinedrum / Digitakt / Analog Rytm | Elektron |
| [ ] | Volca Beats / Electribe | Korg |
| [ ] | RX5 / RX11 / RY30 | Yamaha |
| [ ] | DR-880 / DR-670 | Boss |
| [ ] | LinnDrum / Linn 9000 | Linn |
| [ ] | SP-1200 / Drumulator | E-mu |
| [ ] | DMX / DX | Oberheim |
| [ ] | Drumtraks / Tom | Sequential |
| [ ] | DrumBrute / DrumBrute Impact | Arturia |
| [ ] | Circuit Rhythm | Novation |
| [ ] | Play / Tracker | Polyend |

## F. Notation and other

This group has machine-readable percussion definitions — often the cleanest sources of all,
and the least problematic on licensing.

| Status | Target | Source | Note |
|---|---|---|---|
| [ ] | MuseScore drumset definitions | H | open source, XML |
| [ ] | Hydrogen drumkits | H | open source, XML |
| [ ] | Dorico percussion maps | H | XML |
| [ ] | Sibelius percussion maps | H | |
| [ ] | Guitar Pro | H | |
| [ ] | LilyPond drum notation | H | open source |

## G. Standards

| Status | Standard | Note |
|---|---|---|
| [ ] | GM Level 1 percussion (ch 10) | 47 sounds — too small as a pivot, but a mandatory target |
| [ ] | GM2 percussion sets | several sets, larger |
| [ ] | Roland GS drum sets | |
| [ ] | Yamaha XG drum voices | the most extensive of the standard groups |

---

## Numbers

Roughly **190 entries**, eleven of which are already covered by the existing `.iom` files.

## Suggested order

**First wave — high value, source certain:** Roland TD series and VAD (official KB
articles, one article per model), the ten large libraries from group A, the four standards
from group G, and the whole of group F.

**Second wave — source available, more effort:** Yamaha DTX and Alesis via manuals,
DAW-internal instruments, GGD via `.nka`.

**Third wave — only on demand:** vintage drum machines, niche modules, notation beyond
group F.

**No need for completeness.** The value is in pivot quality, not in the number of layouts.
Twenty cleanly curated maps with articulation semantics beat two hundred raw note lists.
