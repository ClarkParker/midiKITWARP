# Dossier 06 — Electronic drum machines and grooveboxes

**Task:** the vocabulary needed for drum machines / grooveboxes that an acoustic-kit taxonomy
(marty-615/drum-remap) cannot express.
**Date:** 2026-09-06. **Author:** research subagent for KITWARP pivot vocabulary.

---

## 1. Scope and method

### 1.1 What was actually fetched

Primary manufacturer documents (downloaded as PDF, text-extracted with `pdftotext -layout`,
or fetched as Internet Archive OCR text):

| Source | Kind | Local extract |
|---|---|---|
| Roland *TR-808 Software Rhythm Composer* Owner's Manual (2018) | Roland, primary | `scratchpad/tr808sw.txt` |
| Roland *TR-909 Software Rhythm Composer* Owner's Manual (2018) | Roland, primary | `scratchpad/tr909sw.txt` |
| Roland *TR-707 Software Rhythm Composer* Owner's Manual (2021) | Roland, primary | `scratchpad/tr707sw.txt` |
| Roland *TR-606 Software Rhythm Composer* Owner's Manual (2020) | Roland, primary | `scratchpad/tr606sw.txt` |
| Roland *TR-8S MIDI Implementation Chart* v1.10 (2018-10-04) | Roland, primary | `scratchpad/tr8s_mic.pdf` |
| Roland *TR-8S Reference Manual* (2018) | Roland, primary | `scratchpad/tr8sref.txt` |
| Roland *TR-909 Owner's Manual* '83 DEC (hardware) | Roland, primary (OCR) | `scratchpad/909.txt` |
| Roland *TR-626 Owner's Manual* (hardware) | Roland, primary (OCR, partly garbled) | `scratchpad/626.txt` |
| Kenton *TR-808 MIDI retrofit* instructions (TR882150+) | 3rd-party retrofit, primary | tool-results PDF |
| Robin Whittle *TR-808 MIDI In* (2018) | 3rd-party retrofit, primary | tool-results PDF |
| Elektron *Machinedrum SPS-1 User's Manual* (2001-2002) | Elektron, primary | `scratchpad/md.txt` |
| Arturia *DrumBrute Impact User Manual* v1.0 EN | Arturia, primary | `scratchpad/dbi.txt` |
| Korg *volca beats MIDI Implementation Chart* v1.00 (2013-06-10) | Korg, primary | `scratchpad/volca.pdf` |
| Alesis *SR-16 Reference Manual* Rev C | Alesis, primary | `scratchpad/sr16.txt` |
| Sibelius *General MIDI 2.txt* device definition | GM2 drum-set map, secondary-but-authoritative | `scratchpad/gm2.txt` |

Repositories cloned (`scratchpad/repos/`):

| Repo | Licence | What it gave |
|---|---|---|
| `bsp2/libanalogrytm` | MIT (see `LICENSE`) | Analog Rytm's 12 track ids + all 34 "machine" ids/names + per-track machine compatibility lists — reverse-engineered but exact |
| `james7780/pxdrum2` | (unlicensed repo; file is a 1992 public mailing-list post) | GM Level 1 percussion key map + the statement that GM's percussion map "derives from the Roland/Sequential mapping used on early drum machines" |
| `EFHIII/midi-ch` | not checked | GS/GM2 per-set drum-name arrays (used only as corroboration; **contains at least one transcription error**, see §2.6) |
| `miclip/patchscore` | not checked | LLM-authored device manifests; used ONLY for the TR-1000 generator name list, flagged UNVERIFIED |
| `simonholliday/subsequence` | not checked | TR-8S note constants; superseded by the Roland chart |

### 1.2 What could not be obtained, and why

- **The GM2 specification PDF itself** (MMA, pages 32–34) is paywalled at midi.org. The GM2 drum
  sets in §2.6 come from the Sibelius GM2 device definition file, which is a faithful transcription
  but is not the MMA document. Marked accordingly.
- **The original TR-808 hardware Owner's Manual has no MIDI section** (the 808 has no MIDI). Its
  note map exists only in third-party retrofits and in Roland's own 2018 plugin. This is itself a
  finding (§2.4).
- **The TR-909 hardware manual states only** `Note Number 36-51 transmitted / 35-51 recognized,
  "assigns to each rhythm voice"` — it does not print the per-voice table. The per-voice table in
  §2.2 comes from Roland's own TR-909 plugin manual, which reproduces the hardware map.
- **TR-626 note numbers**: the Internet Archive OCR of the factory key-number diagram is garbled.
  The voice list and the exclusivity groups are clean; the note numbers are marked UNVERIFIED.
- **Alesis SR-16/SR-18 sound-name list**: the Reference Manual Rev C contains the architecture but
  not the 233-sound name table (it was a separate printed insert). Architecture captured; names not.
- **E-mu SP-1200, Oberheim DMX, LinnDrum, Sequential Drumtraks**: no primary manual obtained inside
  budget. Voice counts/lists are from encyclopaedic secondary sources and are marked UNVERIFIED.
- **Yamaha RX5/RY30, Boss DR-880, Korg Electribe, Akai MPC, Novation Circuit Rhythm**: only
  structural facts (how sounds are organised), from secondary sources; marked where relevant.
- `curl` to github.com is blocked by egress policy; all GitHub access was via `git clone --depth 1`
  or the GitHub MCP tools, per the environment notes.

---

## 2. Extracted facts

### 2.1 Roland TR-808 — 16 named voices, 11 trigger channels, hard exclusivity

The 808 panel names 16 instruments. It has **11 trigger channels**; several named instruments are
the *same circuit* selected by a switch, and therefore **cannot sound simultaneously**.

Kenton's retrofit exposes the trigger channels directly as program numbers 1–11
(*Kenton TR882000 instructions, p.3*):

| Kenton prog | Trigger channel | Named voices on it | Abbrev |
|---|---|---|---|
| 1 | Bass Drum | Bass Drum | BD |
| 2 | Snare Drum | Snare Drum | SD |
| 3 | Low Tom / Low Conga | Low Tom, Low Conga | LT, LC |
| 4 | Mid Tom / Mid Conga | Mid Tom, Mid Conga | MT, MC |
| 5 | Hi Tom / Hi Conga | Hi Tom, Hi Conga | HT, HC |
| 6 | Rim Shot / Claves | Rim Shot, Claves | RS, CL |
| 7 | hand ClaP / MAracas | Hand Clap, Maracas | CP, MA |
| 8 | Cow Bell | Cowbell | CB |
| 9 | CYmbal | Cymbal | CY |
| 10 | Open Hihat | Open Hi-Hat | OH |
| 11 | Closed Hihat | Closed Hi-Hat | CH |

Roland's own TR-808 plugin confirms the same grouping in its **sub-output list** — 11 sub outs, and
the pairs are named as pairs (*TR-808 Software Rhythm Composer manual, p.8*):

```
Sub out 1  Bass Drum          Sub out 7  Hand Clap / Maracas
Sub out 2  Snare Drum         Sub out 8  Closed Hihat
Sub out 3  Low Tom / Low Conga    Sub out 9  Open Hihat
Sub out 4  Mid Tom / Mid Conga    Sub out 10 Cymbal
Sub out 5  High Tom / High Conga  Sub out 11 Cowbell
Sub out 6  Rim Shot / Claves
```

Nuance from Robin Whittle's hardware analysis: *"the Hand Clap and Maracas circuits are
independent. They share a common volume circuit and output, and are triggered by the same channel
in the TR-808's internal sequencer. For the purposes of triggering from MIDI, they are separate
drum circuits."* So CP/MA is a **sequencer-track** exclusivity, not a voice exclusivity; LT/LC,
MT/MC, HT/HC, RS/CL are genuine single-circuit exclusivities.

Also from Whittle: the 808 hi-hat OH/CH share a circuit (CH cuts OH) — the classic hi-hat choke,
present here as a *hardware* fact rather than a performance articulation.

**Per-instrument continuous parameters** exposed as CC by Roland's plugin (p.8), i.e. the 808's own
per-voice parameter vocabulary: `TUNE, DECAY, LEVEL` on every voice, plus `SD TONE`, `SD SNAPPY`,
`SD COMP`, `BD ATTACK`, `CY TONE`, and a global `TOTAL ACCENT` (CC 71).

### 2.2 Roland TR-909 — 11 voices, one hi-hat circuit

Sound sources, from the hardware Owner's Manual specifications page (`909.txt`):

```
Bass Drum*  (Level, Tune, Decay, Attack)
Snare Drum* (Level, Tune, Tone, Snappy)
Low Tom*    (Level, Tune, Decay)
Mid Tom*    (Level, Tune, Decay)
Hi Tom*     (Level, Tune, Decay)
Rim Shot    (Level)
Hand Clap   (Level)
Closed*/Open Hi-Hat (Level, Decay)
Crash Cymbal (Level, Tune)
Ride Cymbal  (Level, Tune)
  * = the voice has a distinct "with accent" and "without accent" sound
```

Two facts of vocabulary weight:

1. **`Closed*/Open Hi-Hat` is one entry** — one circuit, two names, exactly like the 808.
2. **The asterisk**: on the 909 the accented and unaccented versions of BD/SD/LT/MT/HT/CH are
   *different sounds*, not merely louder. Accent is a **discrete two-state axis on the voice**,
   not a point on a velocity curve. (The 909 also has a global `TOTAL ACCENT`.)

Additional non-instrument outputs: the rear panel has a **Trigger Out** which fires "in the same
intervals as the Rim Shot written" (+14 V, 20 ms) — i.e. a drum-machine track whose "instrument"
is *a control voltage*, not a sound.

MIDI implementation chart (hardware manual, C-3): transmit ch 11 / receive ch 10; Note Number
transmitted 36–51, recognized 35–51, ": True voice — assigns to each rhythm voice";
**velocity `Note ON  o 9n v=64-96`, `Note OFF  X 9n v=0`, received velocity `X`** — i.e. the
hardware 909 transmits only two velocity values and *ignores* incoming velocity. Accent is carried
by note choice/`TOTAL ACCENT`, not velocity.

### 2.3 Roland TR-707 / TR-727 and TR-606

**TR-707** — 15 sounds on 11 channels. Sub-output list (*TR-707 Software Rhythm Composer, p.9*):

```
Sub out 1  BASS DRUM 1/2       Sub out 7  HAND CLAP / TAMBOURINE
Sub out 2  SNARE DRUM 1/2      Sub out 8  CLOSED HIHAT
Sub out 3  LOW TOM             Sub out 9  OPEN HIHAT
Sub out 4  MID TOM             Sub out 10 CRASH CYMBAL
Sub out 5  HI TOM              Sub out 11 RIDE CYMBAL
Sub out 6  RIM SHOT / COWBELL
```

Roland's own text: *"The 11 instruments are collectively called a 'kit.'"* — so on the 707 a "kit"
is 11 **slots**, and the 15 sounds are slot + variant. The panel sliders are labelled
`BD SD LT MT HT RIM/COW HCP/TAMB HH CRASH RIDE` + `AC (ACCENT)` — note that ACCENT gets its own
slider, i.e. is a first-class channel.

**TR-606 Drumatix** — 7 sounds, 7 sub outs: `BASS DRUM, SNARE DRUM, L.TOM, H.TOM, C.HIHAT,
O.HIHAT, CYMBAL`. The 606 has:
- **no rim shot, no hand clap, no cowbell, no ride** (one `CYMBAL`, which is a crash-ish noise),
- **two toms only**, named `L.TOM`/`H.TOM`,
- a shared `O.C.HIHAT TUNE / DECAY / LEVEL` CC set (again one hi-hat circuit).

### 2.4 The note-map divergence — four incompatible maps of the *same* 808 voice set

This is the single most load-bearing table in this dossier.

| 808 voice | Roland TR-808 plugin | GM2 "Analog Set" | Whittle MIDI-In retrofit | Behringer RD-8 |
|---|---|---|---|---|
| Bass Drum | **35, 36** | 36 | 36 | 36 |
| Snare Drum | **38, 40** | 38 | 38, 40 | **40** |
| Rim Shot / Claves | 37 | 37 (RS) + **75 (Claves)** | 37 + 75 | 37 |
| Hand Clap / Maracas | 39 | *(no analog clap)* + **70 (Maracas)** | 39 + 70 | 39 |
| Low Tom / Low Conga | 41, 43 | 41, 43 + **64 (Low Conga)** | 41, 43, 64 | **45** |
| Mid Tom / Mid Conga | 45, 47 | 45, 47 + **63 (Mid Conga)** | 45, 47, 63 | **47** |
| Hi Tom / Hi Conga | 48, 50 | 48, 50 + **62 (High Conga)** | 48, 50, 62 | **50** |
| Closed Hi-Hat | 42, 44 | 42 ("CHH 1"), 44 ("CHH 2") | 42 | 42 |
| Open Hi-Hat | 46 | 46 | 46 | 46 |
| Cymbal | **49** | **49** ("Analog Cymbal") | 49, **51, 52** | **51** |
| Cowbell | **51** | **56** | **56** | **56** |

Read the last two rows. Roland's own plugin puts the 808 **Cymbal on 49 (GM Crash Cymbal 1)** and
the 808 **Cowbell on 51 (GM Ride Cymbal 1)**. GM2's Analog Set puts the Cymbal on 49 and the
Cowbell on 56 (GM Cowbell). Behringer's 808 clone puts the **Cymbal on 51** and the Cowbell on 56.
Whittle's retrofit fires the Cymbal from 49, 51 *and* 52.

Consequences that matter for a pivot:

1. **A MIDI note number is not an identity.** The same physical circuit is note 49 on one 808, note
   51 on another 808, and both on a third. Any pivot keyed on GM note number is wrong before the
   first device is added.
2. **`808 CY` is not `crash` and is not `ride`.** It is a single cymbal voice. Every mapping above
   is a *lossy choice*, and the three vendors made three different choices. drum-remap's
   `crash/hit` and `ride/bow` are both wrong answers; `stack/hit` is also wrong.
3. **`808 RS` is not `snare/sidestick`.** It is a discrete oscillator+noise voice that shares a
   circuit with Claves. Filing it as a snare articulation asserts a shell relationship that does
   not exist, and it destroys the RS/CL exclusivity.
4. **The 808's congas are not GM's congas.** GM 62/63/64 are *Mute Hi / Open Hi / Low* conga —
   an articulation distinction. The 808's are *High / Mid / Low* — a pitch distinction on one
   circuit. GM2 papers over this by naming 63 "Analog Mid Conga" in the slot GM calls "Open Hi
   Conga". The axes are different kinds of axis.
5. **The 606's toms land on the 808's mid toms.** 606 `L.TOM` = 45/47, `H.TOM` = 48/50; 808/909
   `MT` = 45/47, `HT` = 48/50. A 2-tom machine is centred in the 6-slot GM tom range, so
   "606 low tom" and "808 mid tom" are the same note. Tom **instance index is not portable** —
   it must be expressed as a position within that machine's own tom set.

### 2.5 Roland TR-909 / TR-707 / TR-606 note maps (Roland-primary, exhaustive)

From the three Roland plugin manuals, section "How Note Numbers Select Sounds or Variations".
Common to all three: `24–31` = Variation Select A–H, `32` = Start sequencer, `33` = Stop sequencer
(the 808 manual omits 32/33). These are **non-instrument note assignments in the drum range** —
a pivot that assumes every note in 24–95 is a sound will mis-translate them.

| Note | TR-909 | TR-808 | TR-707 | TR-606 |
|---|---|---|---|---|
| 35 | Bass Drum | Bass Drum | BASS DRUM 1 | BASS DRUM |
| 36 | Bass Drum | Bass Drum | BASS DRUM 2 | BASS DRUM |
| 37 | Rim shot | Rim shot/Claves | RIM SHOT | — |
| 38 | Snare Drum | Snare Drum | SNARE DRUM 1 | SNARE DRUM |
| 39 | HandClap | HandClap/Maracas | HAND CLAP | — |
| 40 | Snare Drum | Snare Drum | SNARE DRUM 2 | SNARE DRUM |
| 41, 43 | LoTom | LoTom/LoConga | LO TOM | — |
| 42, 44 | Closed HiHat | Closed HiHat | CLOSED HIHAT | C.HIHAT |
| 45, 47 | MidTom | MidTom/MidConga | MID TOM | **L.TOM** |
| 46 | Open HiHat | Open HiHat | OPEN HIHAT | O.HIHAT |
| 48, 50 | HiTom | HiTom/HiConga | HI TOM | **H.TOM** |
| 49 | Crash Cymbal | **Cymbal** | CRASH CYMBAL | **CYMBAL** |
| 51 | Ride Cymbal | **Cowbell** | RIDE CYMBAL | — |
| 54 | — | — | TAMBOURINE | — |
| 56 | — | — | COWBELL | — |

Note that within *one vendor's own plugin family*, note 51 is "Ride Cymbal" on the 909 and 707 and
"Cowbell" on the 808, and note 49 is "Crash Cymbal", "Cymbal" and "Cymbal" respectively.

### 2.6 General MIDI and General MIDI 2

GM Level 1 percussion is 47 sounds, notes 35–81. The 1992 spec summary in `pxdrum2` states the
provenance explicitly: *"This mapping derives from the Roland/Sequential mapping used on early drum
machines."* That is why the TR-909's factory map is nearly GM and the TR-808's is not — GM
codified the 909/707 generation.

**GM2 drum sets** (Bank Select MSB 78H + Program Change; source: Sibelius `General MIDI 2.txt`
device definition, transcribing the MMA GM2 sound set):

| PC | Set name | Character of its overrides |
|---|---|---|
| 1 | Standard Set 1 | the GM1 map, notes 27–87 |
| 9 | Room Set | overrides only the 6 tom notes (`Room Low/Mid/Hi Tom 1/2`) |
| 17 | Power Set | overrides 36, 38 and the 6 toms |
| 25 | Electronic Set | `Electric Bass Drum`, `Electric Snare 1/2`, `Electric Low/Mid/Hi Tom 1/2` |
| 26 | **Analog Set** | the TR-808 (see below) |
| 33 | Jazz Set | overrides 35/36 only (`Jazz Kick 1/2`) |
| 41 | Brush Set | 35/36 + `Brush Tap` (38), `Brush Slap` (39), `Brush Swirl` (40) |
| 49 | Orchestra Set | remaps 41–53 to **chromatic timpani** (`Timpani F` … `Timpani f`), 27–30 to hats/ride, 38/40 to concert snares |
| 57 | SFX Set | not percussion at all |

GM2 **Analog Set** verbatim (notes not listed fall through to Standard):

```
36 Analog Bass Drum    45 Analog Mid Tom 2    62 Analog High Conga
37 Analog Rim Shot     46 Analog OHH          63 Analog Mid Conga
38 Analog Snare 1      47 Analog Mid Tom 1    64 Analog Low Conga
41 Analog Low Tom 2    48 Analog Hi Tom 2     70 Analog Maracas
42 Analog CHH 1        49 Analog Cymbal       75 Analog Claves
43 Analog Low Tom 1    50 Analog Hi Tom 1
44 Analog CHH 2        56 Analog Cowbell
```

What GM2 actually does here is the **timbre-family-as-program-change** model: the note grid is
fixed and the *set* selects a timbre family. It is close to what KITWARP needs — and it fails for
exactly three reasons:

- The families are a **closed enum of 9**, and 8 of them are acoustic. There is one electronic
  family ("Electronic") and one machine family ("Analog"/808). There is no 909, no 606, no 707,
  no LinnDrum, no DMX, no FM.
- **Set membership is not per-note.** GM2 cannot express "808 kick + 909 hats + acoustic ride",
  which is the single most common real-world electronic kit. GS/GM2 partially work around this
  with a second rhythm channel; two is not enough.
- **The overrides are name-only.** `49 Analog Cymbal` occupies GM's `Crash Cymbal 1` slot, so an
  inverse map has no way to learn that the 808 has no crash/ride distinction. GM2 is provably lossy
  on inversion in exactly the way the task brief describes.

Note on corroboration: `EFHIII/midi-ch`'s `drumNames["808"]` array lists notes 42, **44 and 46** all
as `"808 Closed Hi-Hat"`, which contradicts every primary source (46 is the open hat). Treated as a
transcription error and not used.

### 2.7 Roland TR-8S / TR-6S / TR-1000 — the modern "slot × tone" architecture

**TR-8S**: 11 fixed instrument slots — `BD SD LT MT HT RS HC CH OH CC RC`. Confirmed three ways:
the CC list in the MIDI Implementation Chart (`BD TUNE`…`RC LEVEL`, `BD CTRL`…`RC CTRL`), the
`UTILITY:MIDI:Inst Note` parameter list in the Reference Manual, and the pads `[1](BD)–[11](RC)`.

Factory note map, verbatim from *TR-8S MIDI Implementation Chart v1.10*, note `*1`:

| INST | Note Number | Note Number (ALT) |
|---|---|---|
| BD | 36 | 35 |
| SD | 38 | 40 |
| LT | 43 | 41 |
| MT | 47 | 45 |
| HT | 50 | 48 |
| RS | 37 | **56** |
| HC | 39 | **54** |
| CH | 42 | 44 |
| OH | 46 | **58** |
| CC | 49 | **61** |
| RC | 51 | **63** |
| TRIGGER OUT | OFF | — |

*"These note numbers are configurable on UTILITY:MIDI:Inst Note."*

Three structural facts:

1. **`ALT INST` is a second sound per slot with its own MIDI note.** Reference Manual, p.19:
   *"sounds (instrument's tones) whose name includes a '/' character, such as 707Bass1/2, are also
   assigned a second sound (alternate sound). You can switch between normal sounds and alternate
   sounds for performance."* So the 11 slots carry **22 addressable sounds**. Note that the ALT
   notes deliberately squat on GM's Cowbell (56), Tambourine (54) and other percussion notes —
   another way GM note semantics are destroyed by a real device.
2. **`TRIGGER OUT` is an assignable MIDI note** in the same list as the instruments. A note whose
   "instrument" is a CV pulse.
3. **Any tone can go in any slot.** The `INST` screen selects a tone from a categorised list;
   *"you can specify category lock for each instrument, and that setting is saved in the kit"* —
   i.e. category lock exists precisely because **the default is that a slot is not restricted to
   its own category**. A user sample or loop can be loaded into the BD slot
   (icons: `Preset / Sample / Loop / User`). The slot name is a **role/position label**, not a
   claim about the sound.

**Category-dependent parameter semantics** (Reference Manual p.30–31): the per-slot `[CTRL]`
parameter is `Attack` for ACB tones of the **BD** category, `Snappy` for the **SD** category, and
`Color` for the **TOM** category — where `Color` itself means different things per *family*:
ambience for `808 Low/Mid/High Tom`, **resonance** for `808 Noise Tom L/M/H`, ambience for
`909 Low/Mid/High Tom`, pitch movement for `707 Low/Mid/High Tom`. Timbre family is a real,
manufacturer-modelled axis with observable consequences.

**TR-6S**: the same architecture cut to **6 slots** — `BD SD LT HC CH OH` (per the TR-6S
Reference/Parameter Guide `Inst Note` row; corroborated in `miclip/patchscore`, UNVERIFIED
secondary). A 6-slot machine with no cymbal slot at all.

**TR-1000** (2025 flagship) — sound generators organised explicitly as `<family> <instrument>`
(source: `miclip/patchscore` `lib/devices/roland-tr-1000/index.ts`; **UNVERIFIED**, not
cross-checked against a Roland manual):

```
Kick:  808 / 909 / 8X / 9X / 707 (Bass 1-2) / 606 / CR78 Bass Drum, FM Kick Model1, FM Kick Model2
Snare: 808 / 909 / 8X / 9X / 707 (Snare 1-2) / 606 / CR78 Snare Drum, FM Snare Model
Tom:   808 Low Tom, 808 High Tom, 909 Low Tom, 909 High Tom, 8X Tom, 9X Tom, 707 Tom, 606 Tom, FM Tom Model
Clap:  808 / 909 / 8X / 9X Hand Clap, 707 Clap-Tamb, FM Clap Model
CH:    808 / 8X / 9X / 707 / 606 Closed HiHat, CR78 HiHat
OH:    808 / 8X / 9X / 707 / 606 Open HiHat
Cym:   808 Cymbal, 8X / 9X / 707 / 606 Crash Cymbal, CR78 Cymbal, FM Cymbal Model
```

If accurate this is Roland naming the axis for us: **instrument × timbre-family**, with the family
values being machine lineages (`808 909 707 606 CR78 8X 9X FM`) rather than acoustic adjectives.
Note `808 Cymbal` sits in the same list as `909 Crash Cymbal` — the family determines whether the
crash/ride distinction even exists.

### 2.8 Elektron — the strongest evidence for an orthogonal engine axis

**Machinedrum SPS-1**: sounds are named `<ENGINE>-<INST>`. Exhaustive machine list from the
manual's table of contents (Appendix A):

| Engine | Machines |
|---|---|
| `TRX` (analogue-modelled) | `TRX-BD` bass drum, `TRX-SD` snare, `TRX-XT` tom, `TRX-CP` clap, `TRX-RS` rim shot, `TRX-CB` cow bell, `TRX-CH` closed hihat, `TRX-OH` open hihat, `TRX-CY` cymbal, `TRX-MA` maracas, `TRX-CL` claves, `TRX-XC` congas |
| `EFM` (FM) | `EFM-BD`, `EFM-SD`, `EFM-XT` tom, `EFM-CP`, `EFM-RS`, `EFM-CB`, **`EFM-HH` hihat (one, not open/closed)**, `EFM-CY` |
| `E12` (sampled) | `E12-BD`, `E12-SD`, `E12-HT` high tom, `E12-LT` low tom, `E12-CP`, `E12-RS`, `E12-CB`, `E12-CH`, `E12-OH`, **`E12-RC` ride**, **`E12-CC` crash**, **`E12-BR` brushed snare**, `E12-TA` tambourine, `E12-TR` triangle, `E12-SH` shaker, `E12-BC` bongo/congo |
| `P-I` (physical modelling) | `PI-BD`, `PI-SD`, `PI-XT`, `PI-RS`, **`PI-ML` "Metallica"**, `PI-MA`, `PI-HH`, `PI-RC`, `PI-CC` |
| `GND` (generators) | **`GND-SN` sinus, `GND-NS` noise, `GND-IM` impulse** |
| `INP` (audio input) | `INP-GA/GB` input gate A/B, `INP-FA/FB` filter follower A/B, `INP-EA/EB` envelope A/B |
| `MID` | MIDI machines — a track that emits MIDI instead of audio |

Two things an acoustic taxonomy cannot say:
- `GND-SN`/`GND-NS`/`GND-IM` and `INP-*` are **not instruments**. They are raw generators and audio
  processors occupying drum tracks.
- The **engine changes which instruments exist**: `EFM` has one `HH`; `E12` has separate `CH`/`OH`
  *and* separate `RC`/`CC`; `TRX` has one `CY`. Whether the crash/ride and open/closed distinctions
  exist is a property of the engine, not of the music.

**Machinedrum default MIDI note map** (Appendix B), and this is important:

```
0x24 C2 track 1 | 0x26 D2 track 2 | 0x28 E2 track 3 | 0x29 F2 track 4
0x2b G2 track 5 | 0x2d A2 track 6 | 0x2f B2 track 7 | 0x30 C3 track 8
0x32 D3 track 9 | 0x34 E3 tr 10   | 0x35 F3 tr 11   | 0x37 G3 tr 12
0x39 A3 tr 13   | 0x3b B3 tr 14   | 0x3c C4 tr 15   | 0x3e D4 tr 16
0x40 E4 = pattern A01, 0x41 F4 = A02, ...
```

That is a **C-major scale over 16 slots**, carrying no instrument semantics at all, followed by
notes that select *patterns*. A note map can be purely positional.

**Analog Rytm** (from `bsp2/libanalogrytm`, MIT): **12 fixed tracks** —
`BD, SD, RS, CP, BT, LT, MT, HT, CH, OH, CY, CB` (`BT` = bass tom) — and **34 machines** that can
be assigned to tracks subject to a compatibility table:

```
bd hard, bd classic, bd fm, bd plastic, bd silky, bd sharp, bd acoustic,
sd hard, sd classic, sd fm, sd natural, sd acoustic,
rs hard, rs classic, cp classic, bt classic, xt classic,
ch classic, ch metallic, oh classic, oh metallic, hh basic, hh lab,
cy classic, cy metallic, cy ride, cb classic, cb metallic,
sy dual vco, sy chip, sy raw, ut noise, ut impulse, DISABLE
```

The compatibility lists in `sound.c` show that **track 1 (BD) accepts every `bd *`, every `sd *`,
`sy dual vco`, `sy chip`, `sy raw`, `ut noise`, `ut impulse` and `DISABLE`.** So on the Rytm:

- the **track** carries the identity (and the note, and the sequencer lane),
- the **machine** carries the timbre,
- and they are genuinely independent — the BD track can be a snare, a chip synth, or noise.
- `cy ride` is a *machine* on the CY track: **ride-vs-crash is a timbre variant of one cymbal
  voice**, not two instruments.
- `DISABLE` is a first-class machine value (a muted/absent voice).

**Digitakt**: 8 audio tracks with no instrument identity at all. Track triggering is by
`MIDI note numbers 0–7 (C0–G0)` = track 1–8; `12–84 (C1–C7)` play the **active track chromatically**
(secondary source: Digitakt user manual p.23 as quoted). Sample-slot machines, not drum voices.

### 2.9 Other machines — architecture and vocabulary

**Korg volca beats** (*MIDI Implementation Chart v1.00*, note `*2`, primary):
10 parts — `KICK, SNARE, LO TOM, HI TOM, CL HAT, OP HAT, CLAP, CLAVES, AGOGO, CRASH` (CC 40–49
= PART LEVEL for exactly those ten, in that order). Documented note numbers:
`36 KICK, 38 SNARE, 43 LO TOM, 50 HI TOM, 42 CL HAT, 46 OP HAT, 39 CLAP`.
**The four PCM parts (CLAP, CLAVES, AGOGO, CRASH) have `PCM SPEED` CCs 50–53** — the machine is
split into an analogue half and a PCM half, and *the manual documents a note only for CLAP*; notes
for CLAVES/AGOGO/CRASH are **UNVERIFIED**. Also `TOM DECAY` is one CC for both toms; `HAT GRAIN`
is one CC for both hats — again shared circuitry.

**Arturia DrumBrute Impact** (manual §3.1–3.4, primary): 10 instruments on 8 pads —
`Kick, Snare 1, Snare 2, Tom Hi, Tom Low, Cymbal, Cowbell, Closed Hat, Open Hat, FM Drum`.

- *"Each instrument actually has four different sounds: Normal, Normal with accent, Color without
  accent, and Color with accent. The Normal and Color versions of each sound have independent MIDI
  note numbers."* — so **accent** and **Color** are two orthogonal boolean axes on every voice, and
  Color is note-addressed.
- Color chart (what the variant *means*, per instrument): Kick→Drive (overdrive);
  Snare 1→Body (pitch+decay of components); **Snare 2→Clap** (*"Alters tone and attack
  characteristics to simulate a clap"*); Toms→Decay (shared across both toms);
  Cymbal→Cymbal Tone; Closed Hat→CH Decay; Open Hat→Harmonics (affects both hats);
  FM Drum→Pitch Envelope. **Cowbell has no Color.**
- *"The Closed Hat instrument and the Open Hat instrument are generated by the same analog
  circuitry, and so only one can be heard at a time… the Closed Hat will always cut off the Open
  Hat."*
- `FM Drum` is an instrument with **no acoustic referent**.

**Alesis SR-16** (Reference Manual, primary): >230 sounds; **12 velocity pads**; a "Drum Set" is a
per-pad assignment of *sound + tuning + volume + pan + output*; the **MIDI note is a property of
the pad**, user-assignable (`4.x Assign MIDI note numbers to drum pads`). Sound Stacking lets one
pad trigger several sounds. So: the addressable unit is a **kit slot**, and the same sound can
appear on several slots with different tunings — an identity that a "one note = one instrument"
model cannot represent.

**Yamaha RX5 / RY30** (secondary, UNVERIFIED): RX5 — 24 internal PCM voices + 28 on a ROM
"Waveform Data Cartridge"; a "drum set" is *"24 of the RX5's 64 voices"*. RY30 — waveforms are
grouped in **eight categories: Kicks (12), Snares (19), Hi-Hats (8), Cymbals (5), Toms (8), Latin
Percussion (20), Effects (12), Synthesised Waveforms (6)**. Note that `Effects` and `Synthesised
Waveforms` are categories with no acoustic instrument at all.

**Boss DR-880** (secondary): *"A kit is a collection of up to 60 drum sounds along with a bass sound
and an effect setup"*; sound-pool counts `64 Kicks, 102 Snares, 74 Percussion, 54 Hi-Hats, 67 Toms,
31 SFX`, plus **40 bass sounds with COSM bass-amp models on a dedicated bass part**. A drum machine
whose "kit" includes a pitched bass instrument.

**Behringer RD-8 / RD-9** (secondary, transcribed from the owner's manuals):
RD-8 (808 clone) — `36 BD, 37 RS/claves, 39 clap/maracas, 40 SD, 42 CH, 45 LT/low conga,
46 OH, 47 MT/mid conga, 50 HT/high conga, 51 cymbal, 56 cowbell`.
RD-9 (909 clone) — `36 BD, 37 RS, 38 SD, 39 clap, 42 CH, 45 LT, 46 OH, 47 MT, 49 crash, 50 HT,
51 ride`. Both differ from the corresponding Roland maps (§2.4/§2.5): the RD-9 puts LT on 45 where
the 909 puts it on 41/43.

**LinnDrum / Oberheim DMX / Sequential Drumtraks / E-mu SP-1200** (secondary, UNVERIFIED):
LinnDrum — 16 sampled sounds: bass, snare, **cross stick**, hi-hat, **two crash cymbals, two ride
cymbals**, four toms, cabasa, tambourine, cowbell, clap. DMX — 24 sounds from 11 samples, 8-voice;
bass drum at three volume levels, snare at three volume levels, tom at three pitches — i.e.
**velocity layers exposed as separate addressable sounds**. Drumtraks — 13 voices: bass, snare,
snare rim, toms 1–2, crash, ride, open/closed hi-hat, handclaps, tambourine, cowbell, cabasa.
SP-1200 — 8 pads over 4 banks of user samples; no fixed instrument identity.

**Akai MPC / Novation Circuit Rhythm / Korg Electribe** (secondary): pure slot machines.
MPC pads are `A01 = note 36` ascending chromatically, remappable; Circuit Rhythm has 8 sample
tracks × 8 pages × 16 samples. Nothing in the note number carries instrument meaning.

### 2.10 Cross-cutting mechanisms that no acoustic taxonomy has a slot for

| Mechanism | Where it is documented | Why an acoustic model can't hold it |
|---|---|---|
| **Voice-group exclusivity** (one circuit, several named voices) | 808 LT/LC, RS/CL, HT/HC; 707 RIM/COW, HCP/TAMB, BD1/BD2, SD1/SD2; 626's 13 groups; DrumBrute hats; Rytm CY/CB pairing in the compatibility table | drum-remap has choke only as `ride/choke`, `crash/choke` articulations — a *performance* gesture. Here it is a *device constraint* between two different instruments (a cowbell that silences a rim shot). |
| **TR-626 exclusivity groups**, verbatim | 626 manual specs page: `BD1/BD2` · `SD1/SD2` · `LOW TIMBALE/HI TIMBALE` · `LT1/LT2/MT1/MT2/HT1/HT2` · `OPEN HI CONGA/LOW CONGA` · `OHH/CHH` · `CCY/RCY` · `CHINA/CUP` · `RIM SHOT/SD3` · `HCP/CLAVES/MUTE HI CONGA` · `SHAKER` · `CB/TAMB/LAG` · `HAG` (30 voices total) | Six toms are mutually exclusive; `CRASH/RIDE` are mutually exclusive; `CHINA/CUP` are mutually exclusive. A kit where you cannot hit the crash and the ride together. |
| **Accent as a discrete second sound** | 909 spec page (`* = with and without accent`); 707 `AC` slider; 808 `TOTAL ACCENT` CC 71; DrumBrute "four sounds"; TR-8S `ACCENT [STEP]`; volca `ACCENT` | drum-remap has velocity only (`velocityDelta` in fallbacks). Accent is a *flag*, and on the 909 it selects a different waveform. |
| **Alternate sound per slot** | TR-8S `ALT INST` with its own note per slot; TR-1000 per-step `alt-inst` | Not an articulation of the same object; a second object sharing a lane. |
| **Timbre family / synthesis engine** | Machinedrum `TRX/EFM/E12/P-I`; Rytm `hard/classic/fm/plastic/silky/sharp/acoustic/natural/metallic/ride/basic/lab`; TR-1000 `808/909/707/606/CR78/8X/9X/FM`; TR-8S ACB tone categories; GM2 sets | drum-remap has none. |
| **Non-instrument voices** | `GND-SN/NS/IM`, `INP-*`, `MID` (Machinedrum); `ut noise`, `ut impulse`, `sy dual vco`, `sy chip`, `sy raw`, `DISABLE` (Rytm); `FM Drum` (DrumBrute); `Effects`/`Synthesised Waveforms` (RY30) | A raw sine, a noise burst, an input gate, a silent track. |
| **Non-sound notes inside the drum range** | Roland plugins: `24–31` variation select, `32/33` start/stop; Machinedrum: `E4+` pattern select; TR-8S/909: `TRIGGER OUT` as an assignable note | A pivot that assumes every incoming note is a hit will emit garbage. |
| **Slot-only machines** | Digitakt (notes 0–7 = tracks 1–8), MPC, SP-1200, Circuit Rhythm, Machinedrum's C-major slot map | There is no instrument to name. The pivot must be able to say "device slot n, unknown instrument". |
| **Trigger-only / no note-off, fixed velocity** | 909 chart: transmits `v=64-96`, **receives velocity `X`**; Kenton 808 "Receive Mode 0 — two level receive (normal/accent)"; 808 has no note-off at all | Velocity-based fallbacks are meaningless on such a target. |
| **Per-voice parameter set is family-dependent** | TR-8S: `[CTRL]` = Attack (BD) / Snappy (SD) / Color (TOM), and `Color` means ambience on 808 toms, resonance on 808 Noise toms, pitch movement on 707 toms | The same axis name carries different physics per family. |
| **Kit-slot identity vs sound identity** | SR-16 pads (sound + tune + pan + out, note assigned to the *pad*); TR-8S any tone in any slot with optional category lock; Rytm any compatible machine on any track | The thing a MIDI note addresses is a *slot in a kit*, not a sound. |

---

## 3. Implications for the KITWARP pivot vocabulary

### 3.1 The central question, answered

The brief asks whether machine voices are best modelled as (a) acoustic instrument + a
`synthetic/analog` modifier, (b) a separate namespace (`tr808-cowbell`), or (c) acoustic instrument
+ a timbre-family facet.

**The answer is (c), with two required additions, and (b) reduced to a fallback escape hatch.**

**(a) fails on evidence.** A single boolean `synthetic` cannot express that the 808's cymbal has no
crash/ride distinction while the 909's does, that the EFM engine has one hi-hat while E12 has two,
or that `808 Noise Tom` and `808 Tom` respond differently to the same knob. The distinctions are
per-family and structural, not a modifier on a shared object.

**(b) fails on scale and on transfer.** `tr808-cowbell` as a first-class instrument means the
vocabulary grows with every device ever added, and — worse — it destroys the only useful property
of a pivot: it gives the mapper no reason to believe `tr808-cowbell` should ever reach an
`ez-cowbell`. Every pair becomes a hand-written edge, which is the N×N problem the architecture
exists to avoid.

**(c) works, because the axes really are orthogonal in the devices themselves.** The Analog Rytm
proves it: the *track* (BD/SD/RS/CP/BT/LT/MT/HT/CH/OH/CY/CB) and the *machine*
(`bd classic`/`sd fm`/`sy chip`/`ut noise`) are separately selectable, and a BD track can legally
run an SD machine. Elektron names sounds `ENGINE-INST`. Roland's TR-1000 names them
`FAMILY INSTRUMENT`. GM2 names them `<family> <instrument>` (`Analog Bass Drum`,
`Electric Snare 1`). Three vendors independently arrived at two axes.

### 3.2 Axes the pivot needs (beyond drum-remap's instrument/articulation/role/instance)

| # | Axis | Values (initial) | Justification |
|---|---|---|---|
| 1 | **`family`** (timbre family / lineage) | `acoustic`, `analog-808`, `analog-909`, `analog-707`, `analog-606`, `analog-cr78`, `analog-linn`, `analog-dmx`, `analog-generic`, `fm`, `physical-model`, `sample`, `chip`, `unknown` | TR-1000 generator names; Rytm machines; Machinedrum engines; GM2 sets. Must be **open** (a string with a registry), not a closed enum. |
| 2 | **`engine`** (synthesis method, when known and distinct from lineage) | `analog`, `fm`, `pcm`, `physical`, `wavetable`, `acb`, `granular`, `unknown` | `EFM-BD` vs `E12-BD` vs `PI-BD` on one machine; Rytm `bd fm` vs `bd classic` vs `bd acoustic`. |
| 3 | **`variant`** (device-declared alternate sound / timbral toggle) | ordinal `0,1,…` plus a name when the device gives one (`alt`, `color`, `accent-sound`) | TR-8S `ALT INST` (11 slots → 22 notes); DrumBrute `Color`; 909 accented-vs-unaccented waveforms. This is **not** an articulation — it is a second sound on the same lane. |
| 4 | **`accent`** (discrete flag, separate from velocity) | `false` \| `true`, and optionally a level | 909 `*` spec footnote; 707 `AC` slider; 808 `TOTAL ACCENT`; Kenton's two-level receive mode; TR-8S `ACCENT [STEP]`. Must survive round-trip through targets that ignore velocity. |
| 5 | **`exclusion-group`** (device-side voice-group / choke group id) | opaque group id per device layout, resolved at map time | 808 LT/LC, RS/CL; 626's 13 groups; hi-hat circuits; 707 RIM/COW. Different from articulation-level choke. |
| 6 | **`slot`** (position in a fixed device kit, when the device has one) | integer + device-local label (`BD`, `T1`, `A05`) | TR-8S 11 slots, Rytm 12 tracks, Digitakt 8, MPC pad A01. For pure slot machines this is the *only* honest identity. |
| 7 | **`kind`** (what sort of thing occupies the lane) | `percussion`, `generator`, `processor`, `midi-out`, `trigger-out`, `control`, `silent` | `GND-SN/NS/IM`, `INP-GA`, `MID`, `ut noise`, `ut impulse`, `DISABLE`, TR-8S `TRIGGER OUT`, Roland's `32/33` start/stop notes. A hit with `kind != percussion` must never be mapped to a drum. |

### 3.3 Terms missing from drum-remap's 12 instruments / 40 pairs

**Instruments the machines have that drum-remap lacks entirely**
(present as a *voice*, not as a "percussion extra"):

`clap`, `rimshot-voice` (a voice, not `snare/rimshot`), `claves`, `maracas`, `shaker`, `cabasa`,
`tambourine`, `conga` (with `high/mid/low` instances *and* `mute/open` articulations — two different
axes, see §2.4 point 4), `bongo`, `timbale`, `agogo`, `woodblock`, `triangle`, `cuica`, `guiro`,
`whistle`, `vibraslap`, `surdo`, `castanets`, `jingle-bell`, `bell-tree`, `sticks`, `metronome-click`,
`metronome-bell`, `scratch-push`, `scratch-pull`, `slap`, `hi-q`, `square-click`, `timpani`
(chromatic, GM2 Orchestra Set), `applause`.

**Instruments with no acoustic referent at all:**

`fm-drum`, `sine`, `noise`, `impulse`, `chip`, `raw-synth`, `dual-vco`, `metallic` (Machinedrum
`PI-ML` "Metallica"), `input-gate`, `input-filter-follower`, `input-envelope`, `zap`,
`reverse-cymbal` (GS/GM2 Electronic set note 52), `disabled`.

**Articulations/variants that are machine-native:**

`accent` (discrete), `alt` (TR-8S alternate sound), `color` (DrumBrute), `noise-tom`
(808 Noise Tom L/M/H is a distinct tom family, not an articulation of 808 Tom), `brush-tap`,
`brush-slap`, `brush-swirl` (GM2 Brush Set — three *named* brush actions on one note each),
`gated` (`Gated SD`, GS Electronic set), `roll` (TR-8S/TR-1000 sub-step ratchets),
`flam` (TR-909/TR-626 have a *flam interval* parameter, and the 626 restricts flam to
SD1/2/3, LT1/2, MT1/2, HT1/2 only).

**Instance vocabulary that must change:**

drum-remap's tom instances (`rack-1/rack-2/floor-1/floor-2`) are drum-kit furniture. Machines have
`LT/MT/HT` (three, 808/909/707/8S), `L/H` (two, 606/DrumBrute), `LT1/LT2/MT1/MT2/HT1/HT2`
(six, 626), `BT/LT/MT/HT` (four, Rytm — where `BT` is a *bass tom*, a fourth register below low),
and `XT` (one generic tom, Machinedrum TRX/EFM/P-I). The correct model is **an ordinal position
within that device's tom set plus the set's cardinality**, resolved to a target's set at map time —
not a named piece of furniture. The 606-vs-808 collision in §2.4 point 5 is what happens when you
resolve by absolute name instead.

### 3.4 Real distinctions vs cosmetic ones

**Real (must be modelled):**

- **808 cymbal vs crash vs ride.** One voice; three vendors mapped it three ways. Needs to be
  `cymbal` with `family=analog-808` and *no* crash/ride commitment, plus a documented fallback
  ordering (→ crash, → ride) with the loss recorded.
- **Rim shot as a voice vs `snare/rimshot` as an articulation.** On the 808/909/Rytm/Machinedrum
  it is a separate circuit with its own level, tune and decay, and on the 808 it is interlocked
  with the claves. `snare/rimshot` asserts a shell it does not have.
- **Hand clap.** Never a snare articulation. On the 808 it is interlocked with the maracas.
- **Open/closed hi-hat sharing one circuit.** Affects both direction of translation: a source that
  can layer open+closed cannot be replayed on a machine that cannot.
- **Accent.** Discrete, and on the 909 a different sample/waveform.
- **Whether a device has an instrument at all** (606 has no clap, no cowbell, no ride; TR-6S has no
  cymbal slot; Rytm has no tambourine). Fallback chains must be able to say "absent", not "quiet".
- **Timbre family**, because the *set of available articulations depends on it* (§2.8).
- **Slot-only devices.** Digitakt/MPC/SP-1200 notes carry no instrument meaning; forcing them into
  an instrument vocabulary invents information.

**Cosmetic (should NOT get their own instrument term):**

- `TR-808 BD` vs `TR-808 Bass Drum` vs `BD` vs `Kick Drum 2` — pure spelling. One id, many aliases.
- `LT`/`Low Tom`/`LO TOM`/`L.TOM`/`Lo Tom`/`Low Tom 2` — same.
- The `35 vs 36` and `38 vs 40` and `41 vs 43` doublings in every Roland map: these are *the same
  voice on two notes*, not two voices. (Roland writes them as `35, 36  Bass Drum`.) The pivot must
  represent one voice with an alias set of source notes.
- GM2's `Room`/`Power` sets: these are the same instruments with a different sample — a `family`
  value, never new instrument ids.
- `CHH 1` / `CHH 2` in GM2's Analog set: the 808 has one closed hat on two notes.

### 3.5 Concrete ID-scheme recommendation

1. **The pivot id is `instrument/articulation` as in drum-remap, plus a facet bundle.** Keep the
   existing 40 pairs; extend the instrument list with the machine-native voices in §3.3; carry
   `family`, `engine`, `variant`, `accent`, `kind`, `instance{index,of}` and `exclusionGroup` as
   *facets on the mapping entry*, not as part of the id string.
2. **Give every pivot term a stable numeric id** in a namespaced range, so that adding
   `clap` or `fm-drum` never renumbers anything. Suggest: 1000-block per instrument family,
   with articulations as an offset — but the exact numbering is dossier 01/02's job; what this
   dossier requires is only that **the id is not the MIDI note number** (§2.4 point 1) and
   **not the device's name for it**.
3. **Provide a device-native escape hatch, and make it a first-class citizen rather than an
   error path.** Any voice that cannot be honestly named gets
   `kind=percussion|generator, instrument=unknown, deviceRef={vendor, model, slot, nativeName}`.
   Digitakt track 3, SP-1200 pad B4, and `PI-ML` all need this. A pivot that cannot say "I do not
   know what this is, but here is exactly where it came from" will lose data on the machines that
   matter most.
4. **Fallback chains must be family-aware and absence-aware.** `cymbal[family=analog-808]` →
   `crash` → `ride` is a different chain from `cymbal[family=acoustic]`. And "the target has no
   such instrument" must be a terminal state that a caller can surface, not a silent drop.
5. **Model `exclusionGroup` as device-layout metadata on both sides.** Source-side it explains why
   two events never coincide; target-side it warns that a 1→N expand (drum-remap's open+pedal-close
   trick) is physically impossible.
6. **Reserve a `nonSound` class for notes inside the percussion range** that select variations,
   start/stop transport, or fire trigger outs (Roland `24–33`, Machinedrum `0x40+`, TR-8S
   `TRIGGER OUT`). These must be passed through or dropped explicitly, never mapped.

### 3.6 What this means for data collection

Because a note number is not an identity (§2.4), **every device layout must be collected as
`slot → {pivot term, facets}` with the device's own note number as a *property of the slot*, and
with the slot's alternate notes listed as aliases.** Collecting `note → pivot term` will silently
merge the 808's cowbell with the 909's ride the first time both are added.

---

## 4. Provenance

| Fact | Source | Access | Licence / status |
|---|---|---|---|
| TR-808 11 trigger channels, program list, two-level receive mode, non-volatile note map | Kenton Electronics, *Instructions for MIDI interface Roland TR-808*, firmware TR882150+, p.2–3 | https://kentonuk.com/wp-content/uploads/2019/06/TR882000.pdf | © Kenton Electronics, quoted for research |
| TR-808 per-circuit MIDI note table, CP/MA circuit independence, hi-hat circuit sharing, AUX trigger note 84 | Robin Whittle, *TR-808 MIDI In*, 17 June 2018, p.2–4 | https://www.firstpr.com.au/rwi/tr-808/TR-808-MIDI-In.pdf | © Robin Whittle 2018 |
| TR-808 sub-out pairing, CC list, note map (`49 Cymbal`, `51 Cowbell`) | Roland, *TR-808 Software Rhythm Composer Owner's Manual*, 2018, p.8 | https://www.rolandcloud.com/getattachment/29827606-079c-4cf0-9777-e81ef9769868/TR-808-Manual-E.pdf | © Roland Corporation |
| TR-909 note map, sub-outs, CC list | Roland, *TR-909 Software Rhythm Composer Owner's Manual*, 2018, p.8 | https://www.rolandcloud.com/getmedia/38e821fb-17fd-4b17-95ca-04cd728fccde/TR-909-Manual-E.pdf | © Roland Corporation |
| TR-909 sound sources + accent asterisk, Trigger Out, MIDI implementation chart (v=64-96, receive velocity X) | Roland, *TR-909 Rhythm Composer Owner's Manual*, Dec 1983, specs page + chart C-3 | https://archive.org/stream/synthmanual-roland-tr-909-owners-manual/rolandtr-909ownersmanual_djvu.txt | © Roland; Internet Archive OCR |
| TR-707 note map, 11-instrument kit, sub-outs, CC list | Roland, *TR-707 Software Rhythm Composer Owner's Manual*, 2021, p.8–9 | https://www.rolandcloud.com/getmedia/a6fd7ea5-b0f2-47e9-9f68-e79e7e3d97c6/TR-707-Software-Rhythm-Composer-eng01-W.pdf | © Roland Corporation |
| TR-606 7 sounds, note map, shared O.C.HIHAT CCs | Roland, *TR-606 Software Rhythm Composer Owner's Manual*, 2020, p.8–9 | https://www.rolandcloud.com/getmedia/4d2759ec-25ee-4c04-86dc-69b741029581/TR-606-Software-Rhythm-Composer-Manual-eng01-W.pdf | © Roland Corporation |
| TR-626 30 voices, 13 exclusivity groups, flam restriction | Roland, *TR-626 Owner's Manual*, specs + "Drum Voice Group" pages | https://archive.org/stream/synthmanual-roland-tr-626-owners-manual/rolandtr-626ownersmanual_djvu.txt | © Roland; OCR, note numbers UNVERIFIED |
| TR-8S factory note map incl. ALT column and TRIGGER OUT; 11-instrument CC list | Roland, *TR-8S MIDI Implementation Chart* v1.10, 2018-10-04, note `*1` | https://static.roland.com/assets/media/pdf/TR-8S_MIDIImpleChart_eng02_W.pdf | © Roland Corporation |
| TR-8S ALT INST semantics, INST tone categories + category lock, Preset/Sample/Loop/User icons, per-category `[CTRL]`, family-dependent `Color`, `Inst Note` parameter | Roland, *TR-8S Reference Manual*, 2018, p.19, p.30–31, p.43 | https://static.roland.com/assets/media/pdf/TR-8S_Reference_eng01_W.pdf | © Roland Corporation |
| TR-1000 generator lists (`808/909/8X/9X/707/606/CR78/FM × BD/SD/Tom/Clap/CH/OH/Cym`); TR-6S 6-slot list | `miclip/patchscore`, `lib/devices/roland-tr-1000/index.ts`, `lib/devices/roland-tr-6s/index.ts` | `git clone https://github.com/miclip/patchscore` | **UNVERIFIED** — LLM-authored manifest, not cross-checked against a Roland manual |
| GM Level 1 percussion key map; "derives from the Roland/Sequential mapping used on early drum machines" | Jeff Mallory, *Brief Overview of Proposed General MIDI Level 1 Spec*, 14 Jan 1992, in `james7780/pxdrum2`, `MIDI - GM and GS mappings.txt` | `git clone https://github.com/james7780/pxdrum2` | public mailing-list post |
| GM2 drum sets 1/9/17/25/26/33/41/49/57 and per-set note overrides incl. the full Analog Set | Sibelius GM2 device definition `General MIDI 2.txt` | http://www.sibelius.com/helpcenter/resources/patchfiles/General%20MIDI%202.txt | transcription of the MMA GM2 sound set; the MMA spec itself was not obtainable |
| GM2 Bank Select 78H mechanism, 9 drum sets, spec pages 32–34 | Mike Kent, MIDI.org forum, *General MIDI Level 2 ch 11 percussion* | https://midi.org/community/midi-specifications/general-midi-level-2-ch-11-percussion | MMA forum |
| Machinedrum engine × instrument machine list; default MIDI note map (C-major over 16 tracks, then pattern-select notes); CC map | Elektron, *Machinedrum SPS-1 User's Manual*, 2001-2002, Appendix A ToC + Appendix B | https://www.polynominal.com/elektron-Machinedrum-sps1/machinedrum-sps1-manual.pdf | © Elektron ESI AB |
| Analog Rytm 12 track ids, 34 machine names, per-track machine compatibility, `DISABLE` machine, sample-recorder source enum (`BD, SD, RS/CP, BT, LT, …`) | `bsp2/libanalogrytm`, `sound.h`, `sound.c`, `settings.h` | `git clone https://github.com/bsp2/libanalogrytm` | MIT (repo `LICENSE`); reverse-engineered |
| volca beats 10 parts, PCM vs analogue split, documented note numbers | Korg, *volca beats MIDI Implementation Chart* v1.00, 2013-06-10, notes `*1`/`*2` | https://cdn.korg.com/us/support/download/files/456d19dc4cc9e6e73f7ed9ac34e38aec.pdf | © Korg Inc. |
| DrumBrute Impact 10 instruments, four sounds per instrument, Color chart, shared hat circuit, shared tom Color, cowbell has no Color, per-instrument drum map user-assignable | Arturia, *DrumBrute Impact User Manual* v1.0 EN, §3.1–3.6, §9.10.5 | http://downloads.arturia.com/products/drumbrute-impact/manual/drumbrute-impact_Manual_1_0_EN.pdf | © Arturia |
| SR-16 12 pads, Drum Set = per-pad sound/tune/level/pan/output, per-pad MIDI note assignment, sound stacking, >230 sounds | Alesis, *SR-16 Reference Manual* Rev C, §1.2D, §4.x, §8.3 | https://www.alesis.com/rscdn/920/documents/SR16%20Reference%20Rev%20C.pdf | © Alesis |
| Behringer RD-8 / RD-9 default note maps | Zoë Blade's notebook, *Behringer RD MIDI map*, citing the RD-8/RD-9 owner's manuals | https://notebook.zoeblade.com/Behringer_RD_MIDI_map.html | secondary; **UNVERIFIED** against the manuals directly |
| Digitakt track trigger notes 0–7, chromatic 12–84 | Elektron, *Digitakt User Manual* OS1.51, p.23 (quoted via search result) | https://www.elektron.se/wp-content/uploads/2024/09/Digitakt_User_Manual_ENG_OS1.51_231108.pdf | **UNVERIFIED** — manual not fetched directly |
| RX5 24+28 voices / 64-voice pool / 24-voice drum set; RY30 eight waveform categories with counts | Vintage Synth Explorer, Polynominal, Yamaha Black Boxes (search results) | see §1.1 | **UNVERIFIED** secondary |
| DR-880 kit = up to 60 drum sounds + a bass sound + effects; sound-pool counts | zZounds / Roland DR-880 Q&A (search results) | https://cdn.roland.com/assets/media/pdf/DR-880_Q&A.pdf | **UNVERIFIED** secondary |
| LinnDrum 16 sounds incl. two crashes + two rides + cross stick; DMX 24 sounds from 11 samples with 3 volume levels; Drumtraks 13 voices; SP-1200 8 pads × 4 banks | Wikipedia / Vintage Synth Explorer / Polynominal (search results) | see §1.1 | **UNVERIFIED** secondary |
| MPC pad A01 = note 36 ascending, remappable; Circuit Rhythm 8 sample tracks | Akai support articles; Novation user guides (search results) | see §1.1 | **UNVERIFIED** secondary |

### 4.1 Explicitly unverified claims

1. TR-626 per-voice factory key numbers (OCR garbled; the voice list and exclusivity groups are clean).
2. TR-1000 and TR-6S sound/slot lists — taken from an LLM-authored third-party repo.
3. volca beats note numbers for CLAVES, AGOGO and CRASH — Korg's chart documents only seven.
4. Behringer RD-8/RD-9 maps — one secondary transcription, not read from the manuals.
5. All of §2.9's LinnDrum / DMX / Drumtraks / SP-1200 / RX5 / RY30 / DR-880 / MPC / Circuit Rhythm
   figures.
6. `EFHIII/midi-ch`'s GS 808 set is *known wrong* on note 46 and was excluded.
