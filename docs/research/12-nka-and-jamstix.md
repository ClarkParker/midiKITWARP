# Dossier 12 — Two named shortcuts evaluated: GGD `.nka` presets (JPplayground/MidiNoteNameGen) and Rayzoon Jamstix 4

Written 2026-09-06. Both shortcuts were named by the project owner as possible ways to
short-circuit data collection. Both were evaluated before any collecting. **Verdict up front:
neither is a shortcut of the kind hoped for. The GGD `.nka` file contains no articulation names
at all — only integers — so it can supply note numbers for libraries whose slot order you have
already reverse-engineered by hand, and nothing else. Jamstix does have a genuine internal
pivot of 99 named slots, fully published in its manual, and it is the single most useful external
artefact found so far for the *shape* of the KITWARP vocabulary — but it is an authoring
vocabulary (what an A.I. drummer can play) and is strictly smaller than what SD3 or BFD3
expose, so it cannot serve as the pivot itself.**

---

## 1. Scope and method

| What | How obtained | Result |
|---|---|---|
| `JPplayground/MidiNoteNameGen` | `git clone --depth 1` → `/tmp/.../scratchpad/repos/MidiNoteNameGen` | Full repo read: `src/main.py` (170 L), `src/logic.py` (110 L), `src/ggd_data.py` (199 L), `README.md`, `LICENSE.txt` (GPL-3.0), 12 `.nka` presets + 12 generated `.txt` |
| The 12 shipped `.nka` files | in-repo, parsed with python3 | Byte-level structure derived; block layout recovered |
| KSP `.nka` format | `docs.native-instruments.com/ni-tech-manuals/ksp-manual/en/load-save-commands` (WebFetch) | Authoritative confirmation of format |
| GGD official mapping docs | `support.ggd.co` — **Cloudflare 403 on both curl and WebFetch**; recovered only via search-result snippets | Partially obtained, flagged below |
| GGD EULA | not obtainable (same 403) | **UNVERIFIED** |
| NI Studio Drummer articulations | `docs.native-instruments.com/ni-tech-manuals/studio-drummer-manual/en/drum-articulations` | Full articulation list obtained |
| Jamstix 4 manual v4.5.0 | `curl https://www.rayzoon2.com/docs/jamstix4_manual.pdf` (200, 3.18 MB, 77 pp) → `pdftotext -layout` | **Complete. Appendix B and C read verbatim.** |
| Jamstix 3 manual | `curl https://www.rayzoon2.com/docs/jamstix3_manual.pdf` (200, 8.67 MB, 67 pp) | Read; has **no** kit-piece ID appendix — Jamstix 4 is the only published source |
| Jamstix shipped map files | `dldemo4.php` returns a ZIP containing only `Jamstix4Manager.exe` (a downloader). Product content not obtainable. | **UNVERIFIED — see §2.9** |

Working files: `scratch:jamstix4_manual.txt`,
`.../scratchpad/ggd_tables2.md`, `.../scratchpad/repos/MidiNoteNameGen/`.

---

# PART 1 — GGD `.nka` presets and `JPplayground/MidiNoteNameGen`

## 1.1 What the tool is

A 480-line Python/tkinter GUI (`ReaperMidiNoteNameGen-GGD`) that reads one `.nka` file exported
from a GetGood Drums Kontakt instrument and writes a **Reaper MIDI note-name file** (`.txt`).
Author Josh Patterson, dated 8/21/2023, licensed **GPL-3.0** (`LICENSE.txt`, 673 lines, verbatim
GPLv3). Repo also carries a prebuilt `download/MidiNoteNameGen.exe` and `download/preset-pack.zip`.
Six libraries supported (the six the author owns): Invasion, P4 Matt Halpern Kit, Matt Halpern
Signature Pack (original), OKW Metal, OKW Architects, OKW Aggressive Rock.

The README states the acquisition method plainly, and it is the crux of everything below:

> open the desired library and: Go to the settings section — Make sure **all articulations are
> assigned to a Midi note** — Hit **'Export Map'** and save the file — **Take a screenshot of the
> settings page** — Send the exported file (it will be an .nka file) **and screenshot** over to me

The screenshot is required *because the `.nka` contains no names*.

## 1.2 Exact structure of a GGD `.nka` file

`.nka` is not a GGD format. It is the generic Kontakt KSP array dump written by `save_array()`.
Per the NI KSP manual: *"The exported .nka file consists of the name of the array followed by all
its values, one value per line"*, and *"this name must be present as the first line of the .nka
file"* for `load_array()` to accept it (variable names must match precisely).

Measured over all 12 shipped presets:

| Property | Value |
|---|---|
| Encoding | plain 7-bit ASCII, LF line endings, trailing newline. `file(1)` says "ASCII text" |
| Line 1 | the KSP array variable name. **Two variants observed:** `%ART__articulation_map` (Invasion, P4 Halpern, all three OKW) and `%ArticulationMap` (Matt Halpern Signature Pack — the older script generation) |
| Lines 2…N | one signed decimal integer per line, no padding, no separators |
| Array length | **256** elements (Invasion, P4 Halpern, Halpern Original) or **257** elements (all three OKW) — two script generations |
| Element 0 | reserved / unused. Always the filler value |
| Elements 1…K | **primary MIDI note number** assigned to articulation slot *k*. `-1` = articulation exists but is unassigned |
| Elements K+1…127 | filler |
| Elements 128 | filler |
| Elements 129…128+K | a **second parallel per-articulation array**, one entry per articulation slot. **`-1` in every single one of the 12 shipped presets.** Semantics UNVERIFIED — most plausibly a secondary/alternate trigger note per articulation, since GGD's mapping UI allows a kit piece to be assigned more than one note |
| Elements 128+K+1…end | filler |
| Filler value | **inconsistent between exports**: `-1` in 8 files, `0` in 4 files (`OKWMetalDefault`, `OKWMetalCustom`, `OKWArchitectsCustom`, and note `OKWArchitectsDefault` uses `-1`). A parser must therefore not treat `0` as "note C-2" outside the known slot range |

Worked example, `Default/OKWMetalDefault.nka`:

```
%ART__articulation_map     <- line 1: KSP array variable name
0                          <- element 0, reserved (filler is 0 in this file)
23                         <- element 1  = articulation slot 1 ("Left" kick)  -> MIDI note 23
24                         <- element 2  = articulation slot 2 ("Right" kick) -> MIDI note 24
...                        <- elements 3..32 = slots 3..32
0 x 96                     <- elements 33..128 padding
-1 x 32                    <- elements 129..160 = second array, slots 1..32, all unassigned
0 x 96                     <- elements 161..256 padding
```

### The two facts that matter

1. **The array index is the articulation ordinal; the value is the MIDI note.** Not the other way
   round. Verified by construction: the non-filler entries sit at indices 1…K (K = 24…49) while
   their *values* range 12…83.
2. **No articulation names appear anywhere in the file. No strings of any kind appear beyond the
   single array-name header line.** A `.nka` is 100 % opaque without an external slot→name table.
   `save_array_str()` would write strings, but GGD does not use it for the map.

The author had to recover the slot→name table by hand. His own commented-out derivation code is
left in `src/ggd_data.py` (lines ~150-160): he manually assigned articulation *i* in the GUI to
MIDI note *i*, exported, then ran `lst.index(str(kit_piece_idx))` to find which array slot held
note *i*. That is a manual, per-library, GUI-driven calibration — which is precisely the work
that a "shortcut" was supposed to avoid.

## 1.3 Articulation slot counts, measured from the arrays vs. named by the converter

Slot count derived from the array itself (index of the last non-filler element in block A), which
is independent of the converter's tables:

| Library | Slots in the array | Slots the converter names | Coverage |
|---|---|---|---|
| Matt Halpern Signature Pack (original) | 49 | 49 | complete |
| Invasion | 47 | 47 | complete |
| P4 Matt Halpern Kit | 37 | 37 | complete |
| OKW Architects | **33** | 32 | **incomplete — slot 4 is missing from `architects_nka`** |
| OKW Metal | 32 | 32 | complete |
| OKW Aggressive Rock | 24 | 24 | complete |
| **Total** | **222** | **221** | |

The missing OKW Architects slot is array index 4 (line 5 in the converter's line numbering). It is
present in the array (value `-1`, distinct from the file's `0` padding) in both the Default and the
Custom preset, i.e. **GGD ships it with no default note assigned**. Its position in the internal
order is immediately after `Snare Hit` and before `Tom 1 Hit`, so it is almost certainly a further
snare articulation — UNVERIFIED which one.

## 1.4 Complete per-library articulation tables

Names below are the converter's `*_nka` dictionary keys — i.e. **exactly the strings it writes into
the Reaper note-name file**, typos included. "default note" is from `presets/Default/*.nka` (the
mapping GGD ships); "optimised note" is from `presets/Custom/*.nka` (the author's re-grouping).
Note numbers are unchanged by the converter's Kontakt→Reaper step (see §1.5), so these are the
real MIDI note numbers.


**Invasion** — 47 articulation slots in the array; converter names 47.

| slot (array idx) | articulation name as emitted by the converter | default note | default name | "optimised" note |
|---|---|---|---|---|
| 1 | Left | 23 | B0 | 12 |
| 2 | Right | 24 | C1 | 13 |
| 3 | Auto Double Kick | 22 | A#0 | 14 |
| 4 | Flam | 27 | D#1 | 17 |
| 5 | Hit | 26 | D1 | 16 |
| 6 | Ruft | 28 | E1 | 19 |
| 7 | Sidestick | 30 | F#1 | 20 |
| 8 | Wires Off | 29 | F1 | 18 |
| 9 | Rack Tom 1 Hit | 33 | A1 | 22 |
| 10 | Rack Tom 2 Hit | 34 | A#1 | 23 |
| 11 | Rack Tom 3 Hit | 35 | B1 | 24 |
| 12 | Floor Tom 1 Hit | 36 | C2 | 25 |
| 13 | Floor Tom 2 Hit | 37 | C#2 | 26 |
| 14 | Floor Tom 3 Hit | 38 | D2 | 27 |
| 15 | Eye Closed | 44 | G#2 | 32 |
| 16 | Tip Closed | 43 | G2 | 31 |
| 17 | Open 1 | 45 | A2 | 33 |
| 18 | Open 2 | 46 | A#2 | 34 |
| 19 | Open 3 | 47 | B2 | 35 |
| 20 | Peal | 48 | C3 | 36 |
| 21 | Edge Tight | 42 | F#2 | 30 |
| 22 | Tip Tight | 41 | F2 | 29 |
| 23 | CC | 17 | F0 | 37 |
| 24 | Xhat Closed | 70 | A#4 | 39 |
| 25 | Xhat Open | 71 | B4 | 40 |
| 26 | Bell | 61 | C#4 | 51 |
| 27 | Edge | 63 | D#4 | 53 |
| 28 | Rim | 62 | D4 | 52 |
| 29 | Wide Crash L Choke | 57 | A3 | 45 |
| 30 | Wide Crash L Hit | 56 | G#3 | 44 |
| 31 | Main Crash L Choke | 53 | F3 | 43 |
| 32 | Main Crash L Hit | 52 | E3 | 42 |
| 33 | Wide Crash R Choke | 59 | B3 | 49 |
| 34 | Wide Crash R Hit | 58 | A#3 | 48 |
| 35 | Main Crash R Choke | 55 | G3 | 47 |
| 36 | Main Crash R Hit | 54 | F#3 | 46 |
| 37 | China L Choke  | 66 | F#4 | 56 |
| 38 | China L Hit | 65 | F4 | 55 |
| 39 | China R Choke | 68 | G#4 | 58 |
| 40 | China R Hit | 67 | G4 | 57 |
| 41 | Splash L Choke | 74 | D5 | 61 |
| 42 | Splash L Hit | 73 | C#5 | 60 |
| 43 | Splash C Choke | 76 | E5 | 63 |
| 44 | Splash C Hit | 75 | D#5 | 62 |
| 45 | Bell L Hit | 79 | G5 | 66 |
| 46 | Bell R Ht | 80 | G#5 | 67 |
| 47 | Stack Hit | 78 | F#5 | 65 |

**OKW Aggressive Rock** — 24 articulation slots in the array; converter names 24.

| slot (array idx) | articulation name as emitted by the converter | default note | default name | "optimised" note |
|---|---|---|---|---|
| 1 | Kick | 24 | C1 | 12 |
| 2 | Cross Stick | 30 | F#1 | 15 |
| 3 | Snare Hit | 26 | D1 | 14 |
| 4 | Tom 1: Hit | 33 | A1 | 17 |
| 5 | Tom 2: Hit | 34 | A#1 | 18 |
| 6 | Ede Closed: | 44 | G#2 | 23 |
| 7 | Tip Closed | 43 | G2 | 22 |
| 8 | Open 1 | 45 | A2 | 24 |
| 9 | Open 2 | 46 | A#2 | 25 |
| 10 | Open 3 | 47 | B2 | 26 |
| 11 | Pedal | 48 | C3 | 27 |
| 12 | Edge Tight | 42 | F#2 | 21 |
| 13 | Tip Tight | 41 | F2 | 20 |
| 14 | CC | 17 | F0 | 28 |
| 15 | Bell | 61 | C#4 | 34 |
| 16 | Bow | 62 | D4 | 35 |
| 17 | Crash L Choke | 53 | F3 | 31 |
| 18 | Crash L Hit | 52 | E3 | 30 |
| 19 | Crash R Choke | 55 | G3 | 33 |
| 20 | Crash R Hit | 54 | F#3 | 32 |
| 21 | China Choke | 66 | F#4 | 37 |
| 22 | China Hit | 65 | F4 | 36 |
| 23 | Splash Choke | 74 | D5 | 39 |
| 24 | Splash Hit | 73 | C#5 | 38 |

**OKW Architects** — 33 articulation slots in the array; converter names 32.

| slot (array idx) | articulation name as emitted by the converter | default note | default name | "optimised" note |
|---|---|---|---|---|
| 1 | Kick | 24 | C1 | 12 |
| 2 | Cross Stick | 30 | F#1 | 15 |
| 3 | Snare Hit | 28 | E1 | 14 |
| 4 | **(UNNAMED — converter omits this slot)** | unassigned | — | unassigned |
| 5 | Tom 1 Hit | 35 | B1 | 17 |
| 6 | Tom 2 Hit | 36 | C2 | 18 |
| 7 | Tom 3 Hit | 37 | C#2 | 19 |
| 8 | Edge Closed | 44 | G#2 | 24 |
| 9 | Tip Closed | 43 | G2 | 23 |
| 10 | Open 1 | 45 | A2 | 25 |
| 11 | Open 2 | 46 | A#2 | 26 |
| 12 | Open 3 | 47 | B2 | 27 |
| 13 | Pedal | 48 | C3 | 28 |
| 14 | Edge Tight | 42 | F#2 | 22 |
| 15 | Tip Tight | 41 | F2 | 21 |
| 16 | CC | 17 | F0 | 29 |
| 17 | Ride Bell | 61 | C#4 | 38 |
| 18 | Ride Bow | 62 | D4 | 39 |
| 19 | Ride Crash | 63 | D#4 | 40 |
| 20 | Main L Choke | 53 | F3 | 32 |
| 21 | Main L Hit | 52 | E3 | 31 |
| 22 | Main R Choke | 55 | G3 | 34 |
| 23 | Main R Hit | 54 | F#3 | 33 |
| 24 | Wide R Choke | 59 | B3 | 36 |
| 25 | Wide R Hit | 58 | A#3 | 35 |
| 26 | Mini China Choke | 66 | F#4 | 46 |
| 27 | Mini China Hit | 65 | F4 | 45 |
| 28 | Splash Choke | 74 | D5 | 51 |
| 29 | Splash Hit | 73 | C#5 | 50 |
| 30 | X-hat Hit | 78 | F#5 | 48 |
| 31 | China Choke | 68 | G#4 | 44 |
| 32 | China Hit | 67 | G4 | 43 |
| 33 | Ride Choke | 64 | E4 | 41 |

**OKW Metal** — 32 articulation slots in the array; converter names 32.

| slot (array idx) | articulation name as emitted by the converter | default note | default name | "optimised" note |
|---|---|---|---|---|
| 1 | Left | 23 | B0 | 14 |
| 2 | Right | 24 | C1 | 13 |
| 3 | Double Kick | 22 | A#0 | 12 |
| 4 | Cross Stick | 30 | F#1 | 17 |
| 5 | Hit | 26 | D1 | 16 |
| 6 | Tom 1: Hit | 33 | A1 | 19 |
| 7 | Tom 2: Hit | 34 | A#1 | 20 |
| 8 | Tom 3: Hit | 35 | B1 | 21 |
| 9 | Tom 4: Hit | 36 | C2 | 22 |
| 10 | Edge Closed | 44 | G#2 | 27 |
| 11 | Tip Closed | 43 | G2 | 26 |
| 12 | Open 1 | 45 | A2 | 28 |
| 13 | Open 2 | 46 | A#2 | 29 |
| 14 | Open 3 | 47 | B2 | 30 |
| 15 | Pedal | 48 | C3 | 31 |
| 16 | Edge Tight | 42 | F#2 | 25 |
| 17 | Tip Tight | 41 | F2 | 24 |
| 18 | CC | 17 | F0 | 32 |
| 19 | Ride Bell | 61 | C#4 | 42 |
| 20 | Ride Bow | 62 | D4 | 43 |
| 21 | Left Choke | 53 | F3 | 35 |
| 22 | Left Hit | 52 | E3 | 34 |
| 23 | Center Choke | 55 | G3 | 37 |
| 24 | Center Hit | 54 | F#3 | 36 |
| 25 | Right Choke | 59 | B3 | 39 |
| 26 | Right Hit | 58 | A#3 | 38 |
| 27 | China Choke | 66 | F#4 | 41 |
| 28 | China Hit | 65 | F4 | 40 |
| 29 | Splash Left Choke | 74 | D5 | 46 |
| 30 | Splash Lefts Hit | 73 | C#5 | 45 |
| 31 | Splash Center Choke | 76 | E5 | 48 |
| 32 | Splash Center Hit | 75 | D#5 | 47 |

**P4 Matt Halpern Kit** — 37 articulation slots in the array; converter names 37.

| slot (array idx) | articulation name as emitted by the converter | default note | default name | "optimised" note |
|---|---|---|---|---|
| 1 | Kick | 24 | C1 | 12 |
| 2 | Sidestick | 30 | F#1 | 18 |
| 3 | Snare Flam | 27 | D#1 | 15 |
| 4 | Snare Hit | 26 | D1 | 14 |
| 5 | Ruft | 28 | E1 | 17 |
| 6 | Wires Off | 29 | F1 | 16 |
| 7 | Rack Tom 1 Hit | 33 | A1 | 21 |
| 8 | Rack Tom 2 Hit | 34 | A#1 | 22 |
| 9 | Floor Tom 1 Hit | 35 | B1 | 23 |
| 10 | Floor Tom 2 Hit | 36 | C2 | 24 |
| 11 | Pedal Chink | unassigned | — | 35 |
| 12 | Edge Closed | 44 | G#2 | 29 |
| 13 | Edge Tight | 42 | F#2 | 27 |
| 14 | Open 1 | 45 | A2 | 31 |
| 15 | Open 2 | 46 | A#2 | 32 |
| 16 | Open 3 | 47 | B2 | 33 |
| 17 | Pedal | 48 | C3 | 34 |
| 18 | Tip Closed | 43 | G2 | 28 |
| 19 | Tip Tight | 41 | F2 | 26 |
| 20 | CC | 17 | F0 | 36 |
| 21 | Ride Bell | 61 | C#4 | 45 |
| 22 | Ride Bow | 62 | D4 | 46 |
| 23 | Main Crash L Choke | 53 | F3 | 39 |
| 24 | Main Crash L Hit | 52 | E3 | 38 |
| 25 | Wide Crash L Choke | 57 | A3 | 41 |
| 26 | Wide Crash L Hit | 56 | G#3 | 40 |
| 27 | Main Crash R Choke | 55 | G3 | 43 |
| 28 | Main Crash R Hit | 54 | F#3 | 42 |
| 29 | China Choke | 66 | F#4 | 49 |
| 30 | China Hit | 65 | F4 | 48 |
| 31 | Splash L Choke | 74 | D5 | 55 |
| 32 | Splash L Hit | 73 | C#5 | 54 |
| 33 | Splash C Choke | 76 | E5 | 57 |
| 34 | Splash C Hit | 75 | D#5 | 56 |
| 35 | Mini Hats Hit | 77 | F5 | 51 |
| 36 | Stack Hit | 78 | F#5 | 52 |
| 37 | Stick Click | 79 | G5 | 19 |

**Matt Halpern Signature Pack** — 49 articulation slots in the array; converter names 49.

| slot (array idx) | articulation name as emitted by the converter | default note | default name | "optimised" note |
|---|---|---|---|---|
| 1 | Kick Main Hit | 24 | C1 | 12 |
| 2 | Stick Click Kick Hit | 25 | C#1 | 13 |
| 3 | Snare Hit | 26 | D1 | 15 |
| 4 | Flam | 27 | D#1 | 16 |
| 5 | Ruff | 28 | E1 | 17 |
| 6 | Snare-Off | 29 | F1 | 18 |
| 7 | Stick Click | 30 | F#1 | 19 |
| 8 | Hi Tom Hit | 33 | A1 | 21 |
| 9 | Hi Tom Rim Hit | 34 | A#1 | 22 |
| 10 | Mid Tom 1 Main Hit | 35 | B1 | 23 |
| 11 | Mid Tom 1 Rim Hit | 36 | C2 | 24 |
| 12 | Mid Tom 2 Main Hit | 37 | C#2 | 25 |
| 13 | Mid Tom 2 Rim Hit | 38 | D2 | 26 |
| 14 | Floor Tom Main Hit | 39 | D#2 | 27 |
| 15 | Floor Tom Rim Hit | 40 | E2 | 28 |
| 16 | Pedal Chik | 43 | G2 | 30 |
| 17 | Pedal Ching | 44 | G#2 | 31 |
| 18 | Tip Tight | 45 | A2 | 32 |
| 19 | Edge Tight | 46 | A#2 | 33 |
| 20 | Tip Closed | 47 | B2 | 34 |
| 21 | Edge Closed | 48 | C3 | 35 |
| 22 | Tip Loose | 49 | C#3 | 36 |
| 23 | Edge Loose | 50 | D3 | 37 |
| 24 | Tip Open 1 | 51 | D#3 | 38 |
| 25 | Edge Open 1 | 52 | E3 | 39 |
| 26 | Tip Open 2 | 53 | F3 | 40 |
| 27 | Edge Open 2 | 54 | F#3 | 41 |
| 28 | Tip Open 3 | 55 | G3 | 42 |
| 29 | Edge Open 3 | 56 | G#3 | 43 |
| 30 | Tip Wide | 57 | A3 | 44 |
| 31 | Edge Wide | 58 | A#3 | 45 |
| 32 | Left Crash Hit | 62 | D4 | 48 |
| 33 | Left Crash Bell | 63 | D#4 | 49 |
| 34 | Left Crash Choke | 64 | E4 | 50 |
| 35 | Left Crash Swell | 65 | F4 | 51 |
| 36 | Right Crash Hit | 67 | G4 | 53 |
| 37 | Right Crash Bell | 68 | G#4 | 54 |
| 38 | Right Crash Choke | 69 | A4 | 55 |
| 39 | Right Crash Swell | 70 | A#4 | 56 |
| 40 | Ride Tip | 72 | C5 | 58 |
| 41 | Ride Crash | 73 | C#5 | 59 |
| 42 | Ride Bell Tip | 74 | D5 | 60 |
| 43 | Ride Bell Shoulder | 75 | D#5 | 61 |
| 44 | China Main Hit | 76 | E5 | 63 |
| 45 | China Choke | 77 | F5 | 64 |
| 46 | Stack Tight Hit | 81 | A5 | 66 |
| 47 | Stack Loose Hit | 82 | A#5 | 67 |
| 48 | Splash Hit | 83 | B5 | 69 |
| 49 | Hi Hat CC | unassigned | — | 46 |

### 1.4.1 The second, parallel name table (`*_TEXT` lists)

`src/ggd_data.py` also carries six `*_TEXT` lists — the same names in **GUI left-to-right column
order**, used only for the manual derivation described above. They are dead code at runtime but
are the closest thing in the repo to a transcription of the GGD settings page. They **disagree**
with the live dictionaries in three places:

| List | Index | `*_TEXT` says | `*_nka` dict says | Note |
|---|---|---|---|---|
| `INVASION_TEXT` | 27 | `Rate` | `Rim` | ride zone; `Rate` is a typo |
| `INVASION_TEXT` | 46 | `Bell R: Ht` | `Bell R Ht` | stray colon |
| `P4_HALPERN_TEXT` | 9 | `Floor Tom 1 Hit` (duplicate of 8) | `Floor Tom 2 Hit` | transcription slip |
| `P4_HALPERN_TEXT` | 30 | `Main Crash L Hit` (duplicate of 25) | `Main Crash R Choke` | transcription slip |

Also, the `*_TEXT` order (GUI order) and the `*_nka` slot order (script-internal order) are **not
the same permutation** — e.g. Invasion GUI order is `… Bell, Rim, Edge …` at TEXT indices 26-28
but slots 27, 29, 28. Anyone reusing this data must use the dictionaries, not the lists.

## 1.5 What the converter emits, and its bugs

Output is a Reaper MIDI note-name file: 128 lines of `<note number> <name>`, unassigned notes
written as `<n> ~`. Emitted in slot order, then unused notes appended — **not sorted by note
number**. Reaper accepts this.

Confirmed bugs, ranked:

| # | Bug | Location | Effect |
|---|---|---|---|
| 1 | **`KONTAKT_NOTES` has 126 entries, not 128.** The author believed "Kontakt skips F#8"; in fact his list omits **both F#7 and F#8**. | `ggd_data.py`, `KONTAKT_NOTES` | Every note number ≥ 114 is decoded one semitone low; notes 126 and 127 raise `IndexError`, which `main.py` swallows into a generic `"Something went wrong"` dialog. **Latent only** — the highest note in any shipped GGD preset is 83, so it never fires on the six supported libraries. It *will* fire on any user map that reaches into the top octave. |
| 2 | `KONTAKT_TO_REAPER['G8'] = 'F#9'` — the one entry in the 127-entry table that is not a clean +1 octave. | `ggd_data.py` | Consequence of bug 1. |
| 3 | The whole Kontakt→Reaper conversion is an **identity on note numbers**. `KONTAKT_NOTES[n]` → `KONTAKT_TO_REAPER` (+1 octave in the *name*) → `REAPER_MIDI_NOTE_MAP` (−1 octave in the *number*). Net effect: `n → n`, except where bug 1 breaks it. | `logic.py` `create_reaper_map` | 200 lines of lookup tables that compute the identity function. Do not copy this code. |
| 4 | **Stale / typo'd names shipped into every generated file**, verified present in the repo's own `.txt` outputs: `Eye Closed` (= Edge Closed, Invasion note 44), `Peal` (= Pedal, Invasion note 48), `Ruft` (= Ruff, Invasion 28 and P4 28), `China L Choke ` (trailing space, Invasion 66), `Ede Closed:` (= Edge Closed, OKW Aggressive Rock 44), `Splash Lefts Hit` (OKW Metal 73), `Bell R Ht` (Invasion 80). | `ggd_data.py` dicts | Any consumer inheriting these tables inherits the typos. |
| 5 | OKW Architects table is missing one articulation (§1.3). | `architects_nka` | 32 of 33 slots. |
| 6 | `logic.py` skips a slot only when `int(value) < 0`. With the `0`-filler export variant (4 of 12 shipped files), a genuinely unassigned slot exported as `0` would be emitted as note 0. Does not bite on the shipped files because the `0`-filler slots fall outside `active_line_numbers`. | `logic.py` | Latent. |
| 7 | `nka_file_dict = {v: k for k, v in <dict>.items()}` inverts a name→slot dict. Two names on one slot would silently drop one. Verified: no duplicate slots in any of the six dicts, so no current loss. | `logic.py` | Latent. |

## 1.6 Does the `.nka` ship with GGD products? Is reading one a "product file" provenance? Is it a licence problem?

**No, and it matters.** Three separate things must be kept apart:

1. **The default mapping** is embedded in the compiled/encoded Kontakt KSP script inside the
   product's `.nki`. It is not a file on disk you can read.
2. **The `.nka`** is produced *by the user*, at runtime, by pressing **Export Map** in the GGD
   instrument's Settings page. It is written to wherever the user's save dialog points. It is a
   **user-generated artefact**, not a shipped asset. The repo's `presets/Default/*.nka` are the
   author's own exports of the untouched factory mapping — which is why the README calls them
   "the default mappings that come with these kits" while the tool's docstring simultaneously
   says the input is "produced by 'EXPORT MAP' in Kontakt".
3. **GGD does ship preset map configurations** *inside* the instrument UI — GGD support documents
   a set of software and hardware presets, including a "Third-Party Hardware Configs" group
   covering Roland, Alesis, Yamaha, Medeli, KAT and others, applied via an **Apply Config**
   button; and in the newer non-Kontakt engine (Modern & Massive 2) a **Manage Map Configs →
   Export Config** flow that writes a **`.preset`** file, not `.nka`. *(Source: search-result
   snippets of `support.ggd.co/hc/en-us/articles/31476793134743` and `…/31476802898967`. The pages
   themselves are behind a Cloudflare interstitial and returned HTTP 403 to both curl with a
   browser UA and WebFetch. Treat the exact preset list as **UNVERIFIED**; that GGD ships
   hardware-vendor presets at all is corroborated but the enumeration is not.)*

**Provenance classification for KITWARP:** a `.nka` read from your own installation is *not*
"product file" provenance in the sense of reading a shipped data file. It is **"instrument export
by the owner"** — a distinct, weaker category, because (a) it requires owning and running the
product, (b) it requires the user to first assign every articulation a note (per the README) or
slots come back `-1`, and (c) it yields **no semantics whatsoever**. The semantic layer — 222 slot
names across six libraries — exists only as a hand transcription from screenshots.

**Licence:** the `.nka` itself carries no GGD expression: no samples, no code, no names, no
creative selection — a list of integers the user chose (or accepted) in their own session. Copying
integers a user assigned in their own instrument is not plausibly a copyright act. The exposure,
such as it is, sits in **the name tables**, which are a transcription of GGD's on-screen
articulation labels. Those are short factual labels ("Tip Tight", "Wide Crash R Choke") with thin
originality individually, but a full 222-entry per-product enumeration is closer to a database.
GGD's EULA could not be retrieved (Cloudflare 403), so **any statement about what it permits is
UNVERIFIED**. Note also that MidiNoteNameGen is **GPL-3.0**: lifting `ggd_data.py`'s tables into
KITWARP verbatim would make KITWARP a derivative work of a GPL-3.0 program. The safe route is to
treat the tables as a *cross-check* and re-derive names independently, or contact the author.

## 1.7 Official GGD note maps, and machine-readable articulation data in Kontakt generally

| Source | Machine-readable? | Reachable without owning the product? |
|---|---|---|
| GGD official published note map / note-name files | **None found.** No PDF map, no downloadable note-name file, no key-map chart located on getgooddrums.com or support.ggd.co | n/a |
| GGD in-instrument preset map configs (software + Roland/Alesis/Yamaha/Medeli/KAT hardware) | Yes, but internal to the instrument; applied via UI, not exposed as files | **No** |
| GGD `.nka` export (Kontakt-era products) | Yes — but integers only, zero semantics | **No** |
| GGD `.preset` export (Modern & Massive 2, non-Kontakt engine) | Format UNVERIFIED | **No** |
| Kontakt `.nki` / `.nkm` (instrument, multi) | **No.** Proprietary binary; commercial libraries are additionally "encoded" (Player-licensed), which encrypts the KSP source. Kontakt has no "export mapping" command of its own. | No |
| Kontakt **Resource Container** (`.nkr`) | Proprietary container for scripts/wallpapers/impulse responses. Not a mapping description. | No |
| Kontakt KSP `.nka` in general | **Yes — plain text, and this is the one genuinely open Kontakt data format.** But it is only whatever array a scripter chose to dump. There is no convention that it holds a note map; GGD's use is a product-specific choice. Other Kontakt drum libraries may expose nothing at all. | Only for products whose script offers an export button, and only by running them |
| Kontakt "note names" / keyswitch labels shown in the keyboard view | Rendered by the script/instrument at runtime. No file export. | No |
| **NI Studio Drummer** | The articulation *vocabulary* is fully published in the online manual (see below). The *note numbers* ship as three PDFs ("The Session Kit — Default Mapping", "The Stadium Kit — Default Mapping", "The Garage Kit — Default Mapping") reachable only via the Info button of the Instrument's Library tab **inside Kontakt**. No machine-readable mapping file. | Vocabulary yes, note numbers **no** |

The one product-family exception worth recording: **third-party Kontakt drum libraries sometimes
ship a plain-text mapping file** alongside the `.nki` (e.g. The Metal Factory bundle advertises "a
mapping text file so you will know exactly what shell, articulation or cymbal is placed in every
note"). That is per-vendor goodwill, not a Kontakt feature, and still requires the purchase.

**Plain answer to the brief's question:** of everything in the table above, **nothing is reachable
without owning the product** except the NI Studio Drummer *articulation vocabulary* (names only,
no notes) and generic KSP format documentation. There is no Kontakt-wide machine-readable
articulation channel comparable to Cubase Expression Maps or Logic Articulation Sets.

### NI Studio Drummer articulation vocabulary (obtained, names only)

Recorded because it is a free, citable, non-GM articulation vocabulary and it exercises axes the
40-tag model does not have. Source: NI Studio Drummer manual, "Drum Articulations".

| Kit piece | Articulations |
|---|---|
| Kick | Dampened, Open |
| Snare 1 & 2 | Center Right/Left Alternating, Center Left Hand, Center Right Hand, Halfway Right/Left Alternating, Halfway Left Hand, Halfway Right Hand, Rimshot, Sidestick, Flam, Roll, Wires Off, Rim Only |
| Hi-hat | Closed Tight Tip R/L Alt, Closed Tight Tip RH, Closed Tight Tip LH, Closed Tip R/L Alt, Closed Tip RH, Closed Tip LH, Closed Shank R/L Alt, Closed Shank RH, Closed Shank LH, Closed Pedal, Open Controller, Open Quarter, Open Half, Open Three-Quarters, Open Loose, Open Full (Garage Kit adds Open Pedal) |
| Toms 1-4 | Center R/L Alt, Center RH, Center LH, Rimshot, Rim Only |
| High Crash, Low Crash | Edge, Tip, Bell, Choke |
| Ride | Tip, Bell, Edge, Choke |
| China | Edge, Tip, Choke |
| Splash | Edge, Choke |
| Tambourine | Tap, Shake |
| Clap | Solo, Multi |
| Stick Hit | Hit |
| Cowbell (and Garage Hi/Lo Cowbell) | Open, Muted |
| Stadium Kit only: Hi/Lo Woodblock | Hit |

Three things to take from it: (a) **limb is explicit in the identity** (`Left Hand` / `Right Hand`
/ `R/L Alternating` as *separate samples*, not metadata); (b) **strike position on the head is an
axis of its own** (`Center` vs `Halfway`), orthogonal to zone (`Rimshot`, `Rim Only`); (c) hi-hat
openness is an **ordered scale with a named continuous member**: Closed Tight → Closed → Quarter
→ Half → Three-Quarters → Loose → Full, plus `Open Controller` which is the *same* opening driven
by a CC.

## 1.8 Verdict on shortcut 1

| Question | Answer |
|---|---|
| Does the `.nka` give KITWARP articulation names for free? | **No.** It contains integers only. |
| Does it give note numbers for free? | Only for libraries whose slot order you already know, and only from a user's own live export. |
| How much of the KITWARP inventory does the repo cover? | **6 GGD libraries, 221 named slots of 222** — out of ~30 GGD products, and out of an inventory that also has Toontrack, FXpansion, XLN, Steven Slate, Roland, Yamaha, Alesis, Pearl. Roughly **1 vendor, partially**. |
| Is the data trustworthy as-is? | Only with corrections: 7 typo'd names, 1 missing articulation, 2 duplicate names in the secondary lists, plus the note-table off-by-one if ever fed a high map. |
| Is it useful at all? | **Yes, in one specific way:** it is the only place found where a GGD product's *internal articulation ordering* is written down, and it proves `.nka` is a viable per-user ingest path for GGD note numbers if KITWARP ever wants "read my own mapping". |
| Licence risk | Repo is **GPL-3.0** — do not copy tables verbatim into a proprietary plugin. GGD EULA **UNVERIFIED** (support site 403). |

---

# PART 2 — Rayzoon Jamstix 4

## 2.1 Why it is comparable to the KITWARP pivot

Jamstix composes drum parts abstractly and then renders them onto either its own samples or an
arbitrary third-party drum plugin, chosen at run time. It therefore *must* hold a
library-independent instrument vocabulary and a per-library projection of it — architecturally the
same source→pivot→target that KITWARP specifies. Rayzoon publishes both: the vocabulary as
**Appendix B — Kit Piece Reference IDs**, and the projection format as **Appendix C — Output
Mapping File Format**, in the Jamstix 4 user manual (release 4.5.0, 77 pp, © 2001-2021 Rayzoon
Technologies LLC).

## 2.2 The Jamstix pivot: complete enumeration

**Numeric, stable, with deliberately reserved holes.** Two disjoint namespaces sharing one ID
space: the DRUM KIT (used by the drum brain) and JAMCUSSION (a separately-sold percussion
expansion with its own brain).

### 2.2.1 Drum-kit reference IDs (Appendix B, table 1) — verbatim

| ID | Kit piece | Remark (verbatim from manual) |
|---|---|---|
| 0 | Kick | |
| 1 | Snare | At play time, this sound is resolved to center or offset hit by the A.I. |
| 2 | Snare Side/Crosstick | |
| 3 | Snare Bounced | |
| 4 | Snare Rimshot | |
| 5 | Snare Brushed Muted | This is a brush hit without lift in order to mute the head |
| 6 | Snare Brush Sweep | |
| 7 | *RESERVED* | |
| 8 | Hihat (Dynamic Open) | Pedal pressure controls open level |
| 9 | Hihat Foot Close | |
| 10 | Hihat Foot Splash | |
| 11 | *RESERVED* | |
| 12 | Ride | |
| 13 | Ride Bell | |
| 14 | *RESERVED* | |
| 15 | Crash 1 | |
| 16 | Crash 2 | |
| 17 | Crash 3 | |
| 18 | Crash 4 | |
| 19 | Splash 1 | |
| 20 | Splash 2 | |
| 21 | Splash 3 | |
| 22 | China 1 | |
| 23 | China 2 | |
| 24 | China 3 | |
| 25 | China 4 | |
| 26 | *RESERVED* | |
| 27 | Tom 1 | resolved to center or offset hit by the A.I. |
| 28 | Tom 2 | resolved to center or offset hit by the A.I. |
| 29 | Tom 3 | resolved to center or offset hit by the A.I. |
| 30 | Tom 4 | resolved to center or offset hit by the A.I. |
| 31 | Tom 5 | resolved to center or offset hit by the A.I. |
| 32 | Jam Block Hi | |
| 33 | Jam Block Lo | |
| 34 | Chimes | |
| 35 | Cowbell | |
| 36 | Tambourine | |
| 37 | Drumsticks | |
| 38 | Snare Center Hit | |
| 39 | Snare Offset Hit | The A.I. will use this sound for 16th L/R clusters |
| 40 | Tom 1 Center Hit | |
| 41 | Tom 1 Offset Hit | The A.I. will use this sound for 16th L/R clusters |
| 42 | Tom 2 Center Hit | |
| 43 | Tom 2 Offset Hit | The A.I. will use this sound for 16th L/R clusters |
| 44 | Tom 3 Center Hit | |
| 45 | Tom 3 Offset Hit | The A.I. will use this sound for 16th L/R clusters |
| 46 | Tom 4 Center Hit | |
| 47 | Tom 4 Offset Hit | The A.I. will use this sound for 16th L/R clusters |
| 48 | Tom 5 Center Hit | |
| 49 | Tom 5 Offset Hit | The A.I. will use this sound for 16th L/R clusters |
| 50 | Hihat Closed | Pedal pressure is not considered |
| 51 | Hihat 25% Open | |
| 52 | Hihat 50% Open | |
| 53 | Hihat 75% Open | |
| 54 | Hihat Open | |
| 55 | Cymbal Choke | Will choke the last cymbal played with the same hand |
| 56 | Egg Shaker | |
| 57 | Metal Shaker | |
| 90 | Kick (Left Drum) | This is the 2nd kick (left in drummer view) |
| 91 | Kick (Right Drum) | This is the main kick and only kick in a single kick drum setup |
| 92 | Hihat Shank Closed | |
| 93 | *RESERVED* | |
| 94 | Hihat Shank 50% Open | |
| 95 | *RESERVED* | |
| 96 | Hihat Shank Open | |
| 97 | 2nd Snare | |
| 98 | 2nd Snare Side/Crosstick | |
| 99 | 2nd Snare Bounced | |
| 100 | 2nd Snare Rimshot | |
| 101 | 2nd Snare Brushed Muted | |
| 102 | 2nd Snare Brush Sweep | |
| 103 | 2nd Snare Center Hit | |
| 104 | 2nd Snare Offset Hit | |

**67 defined drum-kit slots** (IDs 0-57 and 90-104, minus the six RESERVED holes 7, 11, 14, 26, 93, 95).

### 2.2.2 Jamcussion reference IDs (Appendix B, table 2) — verbatim

| ID | Kit piece | | ID | Kit piece |
|---|---|---|---|---|
| 58 | Drum 1 Center | | 74 | Percussion 1 Main |
| 59 | Drum 1 Medium/Open | | 75 | Percussion 1 Alternate |
| 60 | Drum 1 Rim/Slap | | 76 | Percussion 2 Main |
| 61 | Drum 1 Hit & Mute | | 77 | Percussion 2 Alternate |
| 62 | Drum 2 Center | | 78 | Percussion 3 Main |
| 63 | Drum 2 Medium/Open | | 79 | Percussion 3 Alternate |
| 64 | Drum 2 Rim/Slap | | 80 | Percussion 4 Main |
| 65 | Drum 2 Hit & Mute | | 81 | Percussion 4 Alternate |
| 66 | Drum 3 Center | | 82 | Percussion 5 Main |
| 67 | Drum 3 Medium/Open | | 83 | Percussion 5 Alternate |
| 68 | Drum 3 Rim/Slap | | 84 | Percussion 6 Main |
| 69 | Drum 3 Hit & Mute | | 85 | Percussion 6 Alternate |
| 70 | Drum 4 Center | | 86 | Percussion 7 Main |
| 71 | Drum 4 Medium/Open | | 87 | Percussion 7 Alternate |
| 72 | Drum 4 Rim/Slap | | 88 | Percussion 8 Main |
| 73 | Drum 4 Hit & Mute | | 89 | Percussion 8 Alternate |

**32 Jamcussion slots** (IDs 58-89, no holes).

### 2.2.3 Totals

| | Count |
|---|---|
| ID space | 0-104 = 105 |
| RESERVED holes | 6 (IDs 7, 11, 14, 26, 93, 95) |
| **Defined drum-kit slots** | **67** |
| **Defined Jamcussion slots** | **32** |
| **Total distinct Jamstix pivot slots** | **99** |

Every ID is *addressable by the pattern engine*, but not every ID is *independently composable*:
IDs 1, 27-31 and 97 are **abstract** — the manual says the A.I. resolves them at play time into
their Center/Offset concrete partners (38/39, 40-49, 103/104). That is a genuine two-level pivot:
an abstract instrument reference and a concrete rendering slot, resolved by performance logic.

## 2.3 How the pattern engine refers to them

- The **Bar Editor** lays events out on **limb rows labelled LH, RH, LF, RF** (§18.3 "Limb Menu":
  *"Clicking on a limb label to the left of the bar editor (LH,RH,LF etc.)"*). Limb is therefore a
  first-class property of an event, held separately from the kit-piece ID.
- Each bar carries three **aspects**: GROOVE, ACCENT, FILL (§18.8 `SHIFT-Z` cycles them). An event
  belongs to an aspect. This is closest to the `role` idea in `marty-615/drum-remap` — and note
  that in Jamstix it is a property of the *bar/event*, never of the instrument slot. That
  corroborates the earlier dossiers' conclusion that role is event metadata, not identity.
- Each tick carries a **groove weight**: `Heavy` / `Neutral` / `Syncopated`, plus per-tick modes
  `Beat Is A Hit`, `Keep Beat Silent` (§18.4).
- Events carry **time offset** (−24th … +24th, in 24th/32nd/48th units), velocity/power, and a
  `LOCKED` flag.
- `ENABLE LIMB CONTROL` (§29.1) computes real limb transit times and **suppresses physically
  unplayable events**. Suppressed events show a red cross in the editor. So the engine has a
  physical model over the pivot, not just a symbol table.
- Rudiments, flams, ruffs, rolls, ghost notes, double strokes, cymbal washes and crescendos are
  **generated as note clusters** by brain elements (`Rudiment Generator`, `Snare Ghosts`,
  `Double Strokes`, `ADD` cluster functions) — **not** as articulation slots. Jamstix has no
  "flam" or "roll" ID at all.

## 2.4 The per-library map files (Appendix C)

| Property | Value |
|---|---|
| Location (Windows) | `C:\ProgramData\Jamstix4\data\midimaps` |
| Location (macOS) | `~/Music/Jamstix4/data/midimaps` |
| Format | INI-style: `[Section]` headers with `Key=Value` lines. Plain text, editable in a text editor (Jamstix 3 manual §11: *"These files are editable text files so you can create your own in a text editor if you wish."*) |
| Extension | **UNVERIFIED.** Appendix C never names it. §28 refers to *"KMAP files"* — so `.kmap` is likely but not confirmed. |

### Sections, verbatim semantics

| Section | Keys | Meaning |
|---|---|---|
| `[Keys]` | `<ReferenceID>=<MIDI key>` | The core projection. One line per pivot slot. *"Only specify the keys that are actually supported by the 3rd party plugin."* Example: `0=36` → send MIDI key 36 for kick. |
| `[Hihat]` | `UseCC=` (0/1), `Controller=` | Whether the target supports continuous hi-hat pedal pressure and on which CC (*"usually #4"*). |
| `[Snare]` | `Controller=` | CC for **drum-head strike position** on the snare. `0` = unsupported. Default 14. |
| `[Tom]` | `Controller=` | CC for tom head position. `0` = unsupported. Default 15. |
| `[Chokes]` | `CH_<ReferenceID>=<MIDI key>`, `AfterTouchChoke=1` | Two alternative choke mechanisms: a **per-cymbal choke key** (`CH_15=13` → key 13 chokes Crash 1) or **aftertouch**. |
| `[Drum Kit]` | `ShortName=`, `LongName=` | Display names in the mapping list and selection dialog. |

Two structural points KITWARP should copy:

1. **The map is sparse and partial by design.** *"Only specify the keys that are actually supported
   by the 3rd party plugin."* A slot with no line is simply absent on that target. Jamstix then
   offers explicit, named policies for the mismatch: `Add Missing Pieces`, `Keep Percussion`,
   `Remove Unmapped Pieces`, `Force MIDI Output Only` (§22.1.1-22.1.4). That is exactly the
   fallback-policy layer KITWARP needs, and Jamstix exposes it as user-visible switches rather
   than a hidden chain.
2. **A target is described by more than keys.** Controller capability (`UseCC`, three
   `Controller=` numbers) and choke *mechanism* (key vs aftertouch) are part of the map, because
   the same musical intent must be expressed as a note on one target and a CC or aftertouch value
   on another. A pure note→note table cannot express this.

## 2.5 Distinctions the Jamstix pivot makes that a flat 40-tag model cannot

| Axis | Evidence in Jamstix | Why 40 flat instrument/articulation tags fail |
|---|---|---|
| **Instance (structured, not ordinal)** | Crash 1-4, Splash 1-3, China 1-4, Tom 1-5, Jam Block Hi/Lo, Percussion 1-8, Drum 1-4 — **and separately** `Kick (Left Drum)` / `Kick (Right Drum)` and `2nd Snare` with its own full 8-articulation sub-family | Two different kinds of instance coexist: an anonymous ordinal (Crash *n*) and a *named role* instance (main vs 2nd kick/snare). A flat tag set must either flatten these or explode combinatorially |
| **Articulation family replicated per instance** | The 2nd snare block (97-104) duplicates the entire primary snare block (1-6, 38-39) | Requires instance × articulation to be a product, not an enumerated list |
| **Ordered openness scalar with named anchors** | `Hihat Closed` (50) → `25% Open` (51) → `50% Open` (52) → `75% Open` (53) → `Open` (54); the manual adds *"depending on how many levels are available in the specific kit (3 to 5 levels)"* and `Closed Hat Variations` = three levels of openness fluctuation on closed hats | 5 discrete anchors on one instrument would burn 5 of 40 tags and still lose ordering |
| **Openness as a continuous controller, distinct from the discrete anchors** | `Hihat (Dynamic Open)` ID 8 — *"Pedal pressure controls open level"* — is a **separate slot** from the 5 discrete ones, plus `[Hihat] UseCC/Controller` (CC4) in the map | The same physical result is a note on one target and a note+CC on another. Needs a first-class controller axis |
| **Zone × openness cross product** | `Hihat Shank Closed` (92), `Hihat Shank 50% Open` (94), `Hihat Shank Open` (96) — a *shank* series parallel to the (implicit tip) series, with RESERVED holes at 93 and 95 for the missing 25 %/75 % shank levels | Proof that Rayzoon treats zone and openness as orthogonal and left room for the full grid. A flat list cannot |
| **Foot articulations on the hi-hat, separate from openness** | `Hihat Foot Close` (9), `Hihat Foot Splash` (10) | Limb-driven articulations of the same instrument |
| **Strike position on the head, as a distinct spatial axis** | `Snare Center Hit` / `Snare Offset Hit`, and Center/Offset for all five toms; plus `[Snare] Controller=` / `[Tom] Controller=` making the position **continuous** (CC14/CC15, MODODRUM); plus kit-menu options `Snare Position Variations` (5 levels), `Snare Position L/R Offset` (5 levels), and the tom equivalents | Position is *not* zone (rim/bell/bow) and *not* limb. It is a third spatial axis, and it is both discrete-sampled and CC-continuous depending on target |
| **Limb, as event property and as identity driver** | Bar editor rows LH/RH/LF/RF; `ENABLE LIMB CONTROL` physical model; *"The A.I. will use this sound for 16th L/R clusters"*; `Cymbal Choke` *"will choke the last cymbal played with the same hand"* | Limb determines which concrete slot an abstract slot resolves to. Cannot be metadata-only |
| **Implement / technique** | `Snare Brushed Muted` (*"a brush hit without lift in order to mute the head"*), `Snare Brush Sweep`, `Drumsticks` | Beater/implement is orthogonal to zone and instrument |
| **Damping as an articulation, not a level** | `Drum 1-4 Hit & Mute`, `Snare Brushed Muted`; plus a global `Position-Based Dampening` toggle | |
| **Choke modelled two ways at once** | ID 55 `Cymbal Choke` = one **generic, stateful** choke event bound to *the last cymbal played with the same hand*; **and** `[Chokes] CH_<id>=key` = per-cymbal choke notes; **and** `AfterTouchChoke=1` = choke as aftertouch | Choke is a *modifier on a prior event*, not an articulation of a cymbal. Every source model that lists "Crash 1 Choke" as a tag is flattening a relation. Jamstix is the first source found that models it both ways explicitly |
| **Abstract vs concrete slot** | IDs 1, 27-31, 97 resolve at play time to their Center/Offset partners | A two-level vocabulary: what the composer means vs what gets rendered |
| **Percussion as a parametric family, not named instruments** | `Drum 1-4 × {Center, Medium/Open, Rim/Slap, Hit & Mute}` and `Percussion 1-8 × {Main, Alternate}` | Deliberately abstract slots filled by whatever kit is loaded — the same trick KITWARP would need for "unclassifiable percussion" |
| **Reserved holes for future expansion** | 7, 11, 14, 26, 93, 95 | A design signal: even a numeric pivot needed extension room after ~20 years. Reinforces "symbolic and unbounded" |

## 2.6 Distinctions Jamstix does **not** make

These are the reasons it cannot be the pivot:

- **No ride zone vocabulary beyond the bell.** `Ride` (12) + `Ride Bell` (13) only. No bow, no
  edge, no crash-ride, no ride shank, no ride tip-vs-shoulder. (ID 14 is RESERVED next to them —
  very likely where ride edge was meant to go.) GGD's Halpern Original alone distinguishes
  `Ride Tip`, `Ride Crash`, `Ride Bell Tip`, `Ride Bell Shoulder`.
- **No crash zones.** Crashes 1-4 are single-slot. No crash bell, no crash edge/bow, no swell.
  GGD Halpern Original has `Left Crash Bell` and `Left Crash Swell`.
- **No tom rim articulations.** Toms have Center/Offset only — no rimshot, no rim-only, no
  rimclick. Studio Drummer, GGD Halpern Original and SD3 all have them.
- **No snare wires-off.** GGD has it in four of six libraries.
- **No flam / ruff / roll / buzz as identity** (`Snare Bounced` is the closest, and it is a
  double-stroke, not a buzz roll). Generated as clusters instead.
- **No stack, no X-hat, no auxiliary/mini hats.** GGD Invasion has `Xhat Closed`, `Xhat Open`,
  `Stack Hit`; P4 has `Mini Hats Hit`; Halpern Original has `Stack Tight Hit` / `Stack Loose Hit`.
- **No velocity/dynamic layer identity, no positional CC on cymbals, no cymbal bow-vs-edge.**

## 2.7 Sizing the Jamstix pivot against the established numbers

| Model | Slots | Note |
|---|---|---|
| GM percussion | 47 | |
| `marty-615/drum-remap` | 40 instrument/articulation pairs (12 instruments) | reference model |
| **Jamstix 4 — drum kit only** | **67** | what an acoustic-kit target must cover |
| **Jamstix 4 — total incl. Jamcussion** | **99** | Jamcussion is a paid expansion |
| Superior Drummer 3 | 80 (established) | **larger than the Jamstix drum kit** |
| `lotkey/Drum-MIDI-Converter` | 170 | current number to beat |

Jamstix sits between drum-remap and lotkey and **below SD3**. It is not a superset of the
libraries KITWARP must serve — which is consistent with its own design: `[Keys]` is explicitly
partial in the *other* direction too (Jamstix emits only what it can play, and simply never
addresses the SD3 articulations it has no concept of).

## 2.8 Terms Jamstix contributes that are missing from the models already surveyed

Recommended additions/renames for the KITWARP vocabulary, each attested:

| Term | Axis | Attestation |
|---|---|---|
| `offset` / `center` (head strike position) | **position** — new axis, distinct from zone | Jamstix 38-49, 103-104; NI Studio Drummer `Center` / `Halfway`; `[Snare]`/`[Tom] Controller=` |
| `shank` on the hi-hat, crossed with openness | zone × openness | Jamstix 92-96; NI Studio Drummer `Closed Shank …` |
| `foot_close`, `foot_splash` | limb + technique on hi-hat | Jamstix 9, 10 |
| `brush_sweep`, `brush_muted` | implement + damping | Jamstix 5, 6 |
| `bounced` (double stroke, not buzz) | technique | Jamstix 3 |
| `hit_and_mute` | damping applied at strike | Jamstix 61, 65, 69, 73 |
| `medium_open` (hand drum) | openness on non-hi-hat instruments | Jamstix 59, 63, 67, 71 |
| `rim_slap` | zone on hand drums | Jamstix 60, 64, 68, 72 |
| `choke` as a **relation to a prior event**, optionally carried by key or aftertouch | modifier, not identity | Jamstix 55 + `[Chokes]` |
| `kick_left` / `kick_right` as *named* instances | structured instance | Jamstix 90, 91 |
| `snare_2` as an instance carrying the whole snare articulation family | structured instance | Jamstix 97-104 |
| `drumsticks` (count-in / stick click) | instrument | Jamstix 37; GGD `Stick Click` |

## 2.9 What could not be verified without owning Jamstix

- **The map-file extension.** `.kmap` is strongly implied by §28 ("editable in KMAP files") but
  Appendix C never states it.
- **Which per-library maps actually ship.** The product page names *"BFD3™, Superior Drummer 3™,
  EZDrummer 2™ and Addictive Drums 2™"*, and the manual separately names IK Multimedia MODODRUM
  as the only bundled map using head-position CCs, plus Roland V-Drums TD-20 support on the
  *input* side. **The full contents of `data/midimaps` are UNVERIFIED.** The free download
  (`rayzoon2.com/dldemo4.php`) is a ZIP containing only `Jamstix4Manager.exe`, a Windows downloader
  — no product data is reachable without installing on Windows and activating.
- **The actual `[Keys]` values for any target.** No shipped map file was obtained. This is the
  single most valuable thing behind the paywall: ~99-slot → note-number tables for SD3, BFD3,
  EZD2, AD2 and MODODRUM, already curated by a third party.
- **The kit file format** (`.jkt` or similar) and whether kit files carry per-articulation MIDI
  key + channel in a readable form. The manual documents a `MIDI Key & Linkage Editor` and a
  `Show Key Map` command that *"will open a tabbed text file with all sounds used by the current
  kit and their MIDI key assignments"* — i.e. **there is a tab-separated dump of the live kit's
  key map, generated on demand.** Format UNVERIFIED; this would be the easiest ingest path for a
  Jamstix owner.
- **Whether the `[Keys]` ID set is exactly Appendix B** (i.e. whether undocumented IDs exist).
- **The `linked sounds` chaining mechanism** (one slot triggering another, e.g. snare + tambourine)
  — documented as existing but its file representation is unknown. Relevant because it is a 1→N
  expansion rule, the same construct as `drum-remap`'s `expand`.

## 2.10 Verdict on shortcut 2

| Question | Answer |
|---|---|
| Does Jamstix have a pivot? | **Yes** — 99 numbered slots, 67 of them acoustic-kit, published in full in Appendix B of a freely downloadable manual. |
| Can KITWARP adopt it as its pivot? | **No.** 67 acoustic slots < SD3's 80. It lacks ride zones, crash zones, tom rims, wires-off, stacks and aux hats. It is an *authoring* vocabulary sized to what the A.I. composes, not a *superset* of what libraries expose. |
| Does it settle any open design question? | **Yes, three.** (a) Head strike position (`center`/`offset`) is a real, independent axis — two sources now attest it. (b) Choke is a *modifier on a prior event*, not an articulation of a cymbal — Jamstix is the first source to model it that way explicitly, and it also shows the same intent must be emitted as a note *or* aftertouch depending on target, which forces a controller axis. (c) Aspect (groove/accent/fill) is a property of the *event*, not the instrument — corroborating that `role` does not belong in identity. |
| Does its map format help? | **Yes, directly.** Sparse INI, `<pivotID>=<note>`, plus target *capability* declarations (`UseCC`, three `Controller=` numbers, `AfterTouchChoke`) and four named unmapped-slot policies. That is a better-specified target-descriptor than anything else surveyed, and it is a workable model for KITWARP's per-layout files. |
| How much of the KITWARP inventory does it cover? | The *format and the axes* — fully useful. The *data* — none obtained; the shipped per-library `[Keys]` tables for SD3/BFD3/EZD2/AD2/MODODRUM are behind the paywall and remain **UNVERIFIED**. |

---

## 3. Implications for the KITWARP pivot vocabulary

1. **Neither shortcut removes the need to enumerate libraries by hand.** The GGD `.nka` carries no
   semantics; the Jamstix `[Keys]` tables were not obtainable. Plan for manual enumeration.
2. **Add a `position` axis** (head strike position: `center` / `offset` / `halfway` / `edge_of_head`),
   separate from `zone`. Attested independently by Jamstix (38-49, 103-104, CC14/CC15) and NI
   Studio Drummer (`Center` / `Halfway`). Neither `drum-remap` nor `lotkey` has it.
3. **`zone` and `openness` must be an orthogonal product, not an enumerated list.** Jamstix's
   `Hihat Shank {Closed, 50% Open, Open}` with RESERVED holes at the missing 25 %/75 % shank
   levels, and Studio Drummer's `Closed Tight Tip` / `Closed Tip` / `Closed Shank` grid, both
   prove the grid is real and both products left it partially filled.
4. **`limb` belongs in identity, not only in metadata.** Studio Drummer ships `Left Hand`,
   `Right Hand` and `R/L Alternating` as *separate samples*. Jamstix resolves abstract slots to
   concrete ones *by limb*. A pivot that treats limb as annotation cannot round-trip Studio Drummer.
5. **`choke` should be a modifier/relation, not an articulation tag.** Jamstix ID 55 chokes "the
   last cymbal played with the same hand"; the map may express it as a per-cymbal note
   (`CH_15=13`) or as aftertouch. Model it as an event modifier with a target-side emission
   strategy. Note this cuts against the GGD data, where every cymbal has a paired `X Choke`
   articulation — that pairing is the *target's* encoding, not the concept.
6. **The controller axis is not optional.** Three independent CC roles are already attested:
   CC4 hi-hat openness, CC14 snare position, CC15 tom position, plus channel aftertouch for choke.
   A target descriptor needs capability flags, not just a note table.
7. **Instance must be structured.** Jamstix carries both anonymous ordinals (Crash 1-4) and named
   role-instances (`Kick (Left Drum)` / `Kick (Right Drum)`, `2nd Snare` with a full duplicated
   articulation family). The GGD data shows the same split (`Main Crash L` vs `Wide Crash L`,
   `Splash L` vs `Splash C`, `China L` vs `China R`, `Bell L` vs `Bell R`) — position-in-kit is a
   *named* instance qualifier (`main`/`wide`/`left`/`centre`/`right`/`mini`), not an index.
8. **Ornaments are not articulations.** Jamstix generates flams, ruffs, rolls, ghosts, double
   strokes and washes as note clusters and has no ID for any of them; GGD ships them as
   articulations (`Flam`, `Ruff`, `Wires Off`). Both must be representable: the pivot needs an
   `ornament` qualifier that can be *either* an identity component (when a library samples it) or
   an unset default (when it does not). Do not force it into the instrument tag.
9. **Copy Jamstix's partial-mapping discipline.** A per-layout file should be sparse, and the
   unmapped-slot behaviour should be named policy (`add`, `keep`, `drop`, `passthrough`), visible
   to the user, not a hidden fallback chain.
10. **Do not copy MidiNoteNameGen's code or tables into KITWARP.** GPL-3.0.

---

## 4. Provenance

| Fact | Source | Licence / status |
|---|---|---|
| Converter code, name tables, bugs | `https://github.com/JPplayground/MidiNoteNameGen` → `src/ggd_data.py`, `src/logic.py`, `src/main.py`, `README.md` | **GPL-3.0** (`LICENSE.txt`) |
| `.nka` contents, slot counts, block layout | `presets/Default/*.nka`, `presets/Custom/*.nka` in the same repo (12 files), parsed with python3 | user exports; repo GPL-3.0 |
| `.nka` = KSP array dump, array name on line 1, one value per line, name must match on load | `https://docs.native-instruments.com/ni-tech-manuals/ksp-manual/en/load-save-commands` | NI documentation, © Native Instruments |
| GGD "Export Map" workflow, screenshot requirement | `README.md` of the same repo | GPL-3.0 |
| GGD preset map configs incl. Third-Party Hardware Configs (Roland/Alesis/Yamaha/Medeli/KAT), `Apply Config`; M&M2 `Manage Map Configs → Export Config` writing `.preset` | `https://support.ggd.co/hc/en-us/articles/31476793134743-Use-preset-MIDI-map-configurations`, `…/31476802898967-Save-import-and-export-mapping-configurations`, `https://support.ggd.co/hc/en-us/sections/31476527911703-Mapping` — **pages returned HTTP 403 (Cloudflare) to curl and WebFetch; recovered only from search-result snippets** | **UNVERIFIED** |
| GGD EULA | not obtained | **UNVERIFIED** |
| NI Studio Drummer articulation list; mapping PDFs only via Kontakt Info button | `https://docs.native-instruments.com/ni-tech-manuals/studio-drummer-manual/en/drum-articulations` | NI documentation |
| Jamstix Appendix B kit-piece IDs (99 slots, 6 RESERVED) | Rayzoon Jamstix 4 User Manual, rel. 4.5.0, **pp. 73-75** — `https://www.rayzoon2.com/docs/jamstix4_manual.pdf` | © 2001-2021 Rayzoon Technologies LLC |
| Jamstix Appendix C map file format, `data/midimaps` paths, `[Keys]/[Hihat]/[Snare]/[Tom]/[Chokes]/[Drum Kit]` | same manual, **pp. 76-77** | same |
| Unmapped-slot policies (Add Missing Pieces / Keep Percussion / Remove Unmapped Pieces / Force MIDI Output Only) | same manual, §22.1.1-22.1.4, p. 56 | same |
| CC4 hi-hat, CC14 snare position, CC15 tom position, aftertouch choke, 3-5 hi-hat levels | same manual, §11.4.1 p. 18-19, §11.6.3 p. 22, §22.3 pp. 56-57, §28 p. 61 | same |
| Limb rows LH/RH/LF/RF; groove weights Heavy/Neutral/Syncopated; groove/accent/fill aspects; ENABLE LIMB CONTROL | same manual, §18.3-18.4 p. 48, §18.8 p. 50, §29.1 p. 61 | same |
| TD-20 input extensions (hi-hat rim → tip/shank routing, splash, aftertouch choke, snare position sensing) | same manual, §13.4 p. 26 and §23.2 pp. 57-58 | same |
| Jamstix map files are plain editable text | Rayzoon Jamstix 3 User Manual §11, p. ~24 — `https://www.rayzoon2.com/docs/jamstix3_manual.pdf` | © 2001-2014 Rayzoon Technologies |
| Supported 3rd-party plugins "BFD3™, Superior Drummer 3™, EZDrummer 2™ and Addictive Drums 2™" | `https://www.rayzoon.com/jamstix4.html` | Rayzoon marketing page |
| Jamstix free download is a manager stub only | `https://www.rayzoon2.com/dldemo4.php` (HTTP 200, 5.5 MB ZIP containing `Jamstix4Manager.exe`) | observed |
