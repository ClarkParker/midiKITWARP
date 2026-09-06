# Dossier 04 — E-Drum Modules: semantic distinctions for the KITWARP pivot vocabulary

Research date: 2026-09-06. Author: research subagent.
Goal: NOT note-number collection. Goal: what semantic distinctions do hardware e-drum
modules make, so the pivot vocabulary can express them losslessly.

---

## 1. Scope and method

### 1.1 What was actually retrieved (primary sources, full text)

| # | Source | How obtained | Local extract |
|---|--------|--------------|---------------|
| S1 | Roland **TD-27 MIDI Implementation** v1.02 (Apr 13 2021), 5263 lines | `curl` https://static.roland.com/assets/media/pdf/TD-27_MIDI_Imple_eng03_W.pdf → `pdftotext -layout` | `scratchpad/td27_midi.txt` |
| S2 | Roland **TD-17 MIDI Implementation** v2.00 (Sep 1 2022) | `curl` https://static.roland.com/assets/media/pdf/TD-17_MIDI_Imple_eng04_W.pdf | `scratchpad/td17_midi.txt` |
| S3 | Roland **TD-17 Data List** eng01 | `curl` https://static.roland.com/assets/media/pdf/TD-17_DataList_eng01_W.pdf | `scratchpad/td17_dl.txt` |
| S4 | Roland KB **TD-17: Default MIDI Note Map** | web.archive.org snapshot 20250808010746 | `scratchpad/kb/td17.html` |
| S5 | Roland KB **TD-27: Default MIDI Note Map** | web.archive.org snapshot 20250629022847 | `scratchpad/kb/td27.html` |
| S6 | Roland KB **TD-50, TD-50X: Default MIDI Note Map** | web.archive.org snapshot 20250629022847 | `scratchpad/kb/td50.html` |
| S7 | Roland KB **TD-25: Default MIDI Note Number Map** | web.archive.org snapshot 20250629022850 | `scratchpad/kb/td25.html` |
| S8 | Roland KB **VAD103: Default MIDI Note Map** (= TD-07) | web.archive.org snapshot 20250808014959 | `scratchpad/kb/vad103.html` |
| S9 | Yamaha **DTX-PRO / DTX-PROX Reference Manual for Ver.2**, 7924 lines | `curl` https://data.yamaha.com/files/download/other_assets/3/2323553/DTX-PRO_DTX-PROX_reference_manual_En_v200_C0.pdf | `scratchpad/dtxpro.txt` |
| S10 | Yamaha **DTX502 Reference Manual** (has full note table + MIDI data format) | `curl` https://usa.yamaha.com/files/download/other_assets/9/329779/dtx502_en_rm_a0.pdf | `scratchpad/dtx502.txt` |
| S11 | **ATV aD5 Reference Guide** Ver 1.2 | `curl` http://www.atvcorporation.com/en/products/drums/ad5/file/602/aD5_rg_en05.pdf | `scratchpad/ad5.txt` |
| S12 | **2Box DrumIt Five User Manual OS 1.24** | `curl` https://2box-drums.com/wp-content/uploads/2023/05/DrumIt-Five-User-Manual-OS-1.24.pdf | `scratchpad/2box.txt` |
| S13 | **EFNOTE 3/5/7 Reference Guide** (Ver 1.1) en04 | `curl` https://www.ef-note.com/products/drums/common357/EFNOTE_3_5_7_RG_en04.pdf | `scratchpad/efnote.txt` |
| S14 | **GEWA G9 Owner's Manual** (EN), 7360 lines | `curl` https://gewadrums.com/manuals/gewadrums/01Digital%20Drums/01Module/g9/G9_OM_EN_Owners_Manual.pdf | `scratchpad/gewa.txt` |
| S15 | **Alesis Strike / Strike Pro Module User Guide** | `curl` https://www.fullcompass.com/common/files/38928-StrikeModuleUserGuide.pdf | `scratchpad/alesis.txt` |
| S16 | **Alesis Nitro Max Drum Module User Guide v1.1** | `curl` https://www.alesis.com/rscdn/2102/documents/Nitro%20Max%20Drum%20Module%20-%20User%20Guide%20-%20v1.1.pdf | `scratchpad/nitromax.txt` |
| S17 | **Pearl Mimic Pro User Manual v1.03** (MIMP24B) | `curl` https://images.thomann.de/pics/atg/atgdata/document/manual/pearl_mimic_pro_en.pdf | `scratchpad/mimic.txt` |
| S18 | Alesis support KB "Why does the Hi Hat send the same MIDI note open/closed?" | WebFetch | (quoted below) |

### 1.2 What could NOT be retrieved, and why

- **support.roland.com returns HTTP 403** to both WebFetch and `curl` (with browser UA). All
  Roland KB note maps were obtained via **web.archive.org** raw snapshots (`/web/<ts>id_/`)
  instead. The Wayback **CDX API is blocked by this environment's egress policy**; the
  `archive.org/wayback/available` JSON API works, so articles were enumerated by WebSearch
  and then resolved one at a time.
- **Roland VAD706, VAD716, V71, TD-07KV, TD-02K, TD-17KVX, TD-17KV2 note maps**: no Wayback
  snapshot exists (`archive.org/wayback/available` returned no `closest`). Not retrieved.
  Their content is expected to be a subset/superset of the TD-27/TD-50 pattern but this is
  **UNVERIFIED**.
- **`static.roland.com` served 403 for TD-50 MIDI Implementation and TD-27 Data List**
  (`TD-50_MIDI_Imple_eng03_W.pdf`, `TD-27_DataList_eng02_W.pdf`). TD-27 zone naming was
  instead confirmed from the TD-27 MIDI Implementation body text (S1) plus the KB map (S5).
- **Yamaha DTX-PROX "Data List"** (the document that holds the PROX default note numbers per
  trigger input source) was not located. Yamaha zone/source *names* come from S9; Yamaha
  default *note numbers* come from S10 (DTX502) and are explicitly a **different generation's**
  map (see §3.6 — Yamaha ships three mutually incompatible note maps).
- **Pearl Mimic Pro**: the shipped manual documents the *zone model* and hi-hat CC behaviour
  but contains **no default note-number table**; Mimic Pro is fully user-mapped. Recorded as
  such, not guessed.
- **Alesis Strike**: user guide contains no default note table either (fully user-mapped,
  "MIDI Note … 000 (C-2) – 127 (G8)" per trigger zone, S15 l.686). Alesis default map taken
  from Nitro Max (S16), which does publish one.

---

## 2. The extracted facts

### 2.1 Roland — exact zone terminology

Roland's own label vocabulary, verbatim, from the KB maps (S4–S8) and MIDI implementation (S1–S3):

- Instrument prefixes: `KICK`, `SNARE`, `TOM 1..4`, `HH` / `HI-HAT`, `CRASH 1..2`, `RIDE`,
  `AUX 1..4`
- Zone suffixes in angle/round brackets: `<HEAD>`, `<RIM>`, `<XSTICK>` (also written
  `X-Stick`), `<BRUSH>`, `<BOW>`, `<EDGE>`, `<BELL>`, `PEDAL`
- Hi-hat rows are **openness-qualified zone names**, not separate articulations:
  `HH OPEN (BOW)`, `HH OPEN (EDGE)`, `HH CLOSED (BOW)`, `HH CLOSED (EDGE)`, `HH PEDAL`
- The **SysEx kit-unit index** (S2, TD-17 MIDI Implementation, "The assignments to each head
  within the [Kit] are as follows", l.448-470) enumerates the 20 addressable zone slots of a
  TD-17 kit and uses **`HEAD`/`RIM` for cymbals too**:
  `1 KICK HEAD, 2 SNARE HEAD, 3 SNARE RIM, 4/5 TOM1 HEAD/RIM, 6/7 TOM2 HEAD/RIM,
   8/9 TOM3 HEAD/RIM, 10 HI-HAT HEAD, 11 HI-HAT RIM, 12/13 CRASH1 HEAD/RIM,
   14/15 CRASH2 HEAD/RIM, 16 RIDE HEAD, 17 RIDE RIM, 18 RIDE BELL, 19/20 AUX HEAD/RIM`.
  The parallel *trigger* index (`[TrigAnalog]`, l.523-534) is per-**jack**, not per-zone:
  `1 KICK, 2 SNARE, 3-5 TOM1-3, 6 HI-HAT, 7 CRASH1, 8 CRASH2, 9 RIDE, 10 AUX`.
  **⇒ Roland uses two parallel names for the same physical cymbal zone** (`BOW`≡`HEAD`,
  `EDGE`≡`RIM`), and separately distinguishes *jack* (10) from *zone slot* (20).
  A pivot must not treat `BOW`/`HEAD` as different, and must keep jack-identity out of
  zone-identity.

Zone counts per Roland pad type (from the maps):

| Pad | Zones | Roland labels |
|---|---|---|
| Kick | 1 | (no zone suffix) |
| Snare | 3 (+1 alt) | `<HEAD>`, `<RIM>`, `<XSTICK>`, plus `<BRUSH>` alternate head note (TD-25/TD-27) |
| Tom 1..4 | 2 | `<HEAD>`, `<RIM>` |
| Hi-hat | 2 zones × 2 openness + pedal = 5 notes | `OPEN <BOW>`, `OPEN <EDGE>`, `CLOSED <BOW>`, `CLOSED <EDGE>`, `PEDAL` |
| Crash 1..2 | 2 | `<BOW>`, `<EDGE>` |
| Ride | 3 | `<BOW>`, `<EDGE>`, `<BELL>` |
| Aux 1..4 | 2 | `<HEAD>`, `<RIM>` |

**Roland has no CUP/BELL zone on crash and no CUP on hi-hat.** Only the ride has `<BELL>`.

Default note numbers, exhaustive, per module (decimal):

| Roland label | TD-07/VAD103 | TD-17 | TD-25 | TD-27 | TD-50 / TD-50X |
|---|---|---|---|---|---|
| KICK | 36 | 36 | 36 | 36 | 36 |
| SNARE \<HEAD\> | 38 | 38 | 38 | 38 | 38 |
| SNARE \<RIM\> | 40 | 40 | 40 | 40 | 40 |
| SNARE X-Stick | 37 | 37 | 37 | 37 | 37 |
| SNARE \<BRUSH\> | – | – | 23 | (param exists, S1) | (param exists) |
| TOM 1 \<HEAD\> | 48 | 48 | 48 | 48 | 48 |
| TOM 1 \<RIM\> | – | 50 | 50 | 50 | 50 |
| TOM 2 \<HEAD\> | 45 | 45 | 45 | 45 | 45 |
| TOM 2 \<RIM\> | – | 47 | 47 | 47 | 47 |
| TOM 3 \<HEAD\> | 43 | 43 | 43 | 43 | 43 |
| TOM 3 \<RIM\> | – | 58 | 58 | 58 | 58 |
| TOM 4 \<HEAD\> | – | – | – | – | 41 |
| TOM 4 \<RIM\> | – | – | – | – | 39 |
| HH OPEN \<BOW\> | 46 | 46 | 46 | 46 | 46 |
| HH OPEN \<EDGE\> | 26 | 26 | 26 | 26 | 26 |
| HH CLOSED \<BOW\> | 42 | 42 | 42 | 42 | 42 |
| HH CLOSED \<EDGE\> | 22 | 22 | (not listed) | 22 | 22 |
| HH PEDAL | 44 | 44 | 44 | 44 | 44 |
| CRASH 1 \<BOW\> | 49 | 49 | 49 | 49 | 49 |
| CRASH 1 \<EDGE\> | 55 | 55 | 55 | 55 | 55 |
| CRASH 2 \<BOW\> | 57 | 57 | 57 | 57 | 57 |
| CRASH 2 \<EDGE\> | 52 | 52 | 52 | 52 | 52 |
| RIDE \<BOW\> | 51 | 51 | 51 | 51 | 51 |
| RIDE \<EDGE\> | 59 | 59 | 59 | 59 | 59 |
| RIDE \<BELL\> | 53 | 53 | 53 | 53 | 53 |
| AUX 1 \<HEAD\> | – | 27 | 27 | 27 | 27 |
| AUX 1 \<RIM\> | – | 28 | 28 | 28 | 28 |
| AUX 2 \<HEAD\>/\<RIM\> | – | – | – | 29 / 30 | 29 / 30 |
| AUX 3 \<HEAD\>/\<RIM\> | – | – | – | 31 / 32 | 31 / 32 |
| AUX 4 \<HEAD\>/\<RIM\> | – | – | – | – | 33 / 34 |

Roland's note map is **stable across its whole line** — the only differences are how many
toms/auxes exist. This makes Roland an excellent anchor layout but does not reduce the pivot's
job, because the *semantics* differ by module (see §3).

### 2.2 Yamaha — exact zone terminology ("trigger input source")

Yamaha's authoritative names are the **Trigger Input Source** identifiers (S9, p.9). Exhaustive
for DTX-PRO / DTX-PROX:

```
SnareHd  SnareOp  SnareCl          <- Head, Open rimshot, Closed rimshot (= cross-stick)
Tom1Hd   Tom1Rm    (…Tom2, Tom3)
RideBw   RideEg   RideCp           <- Bow, Edge, Cup
Crash1Bw Crash1Eg Crash1Cp
Crash2Bw Crash2Eg Crash2Cp
HhOpBw   HhOpEg   HhClBw  HhClEg  HhFtCl  HhFtSp
Kick     KickRm                    <- kick pad RIM is its own source
Pad3  Pad5  Pad7  Pad13
Pad14Hd  Pad14Rm1  Pad14Rm2        <- generic 3-zone pad: Head, Rim1, Rim2
```

DTX900-generation sources additionally include (S9, "Note Map" note):
`snrHdOff`, `snrOpOff`, `snrClOff` (**snares-off** variants of all three snare zones),
`tom1Rm2`…`tom4Rm2` (**second rim** on toms), `pad12Hd`–`pad15Rm2`.

Yamaha zone-suffix vocabulary: `Hd`(head) `Rm`/`Rm1`/`Rm2`(rim) `Op`(open rim shot)
`Cl`(closed rim shot / cross-stick) `Bw`(bow) `Eg`(edge) `Cp`(cup) `FtCl`(foot close)
`FtSp`(foot splash) `Op`/`Cl` prefixed onto Hh (open/closed state).

DTX502 default note numbers (S10, p.10) — exhaustive, including the GM-kit column which shows
Yamaha's own lossy GM fold-down:

| Yamaha input source | Preset kits 1–49 | GM kit (50) |
|---|---|---|
| snare Head | 38 | 38 |
| snare OpenRim | 40 | 40 |
| snare ClosedRim | 37 | 37 |
| snare(off) Head | 31 | 31 |
| snare(off) OpenRim | 34 | 34 |
| snare(off) ClosedRim | 27 | 27 |
| tom1 Head / tom2 Head / tom3 Head | 48 / 47 / 43 | same |
| ride Bow / Edge / Cup | 51 / **52** / 53 | 51 / **57** / 53 |
| crash Bow / Edge / Cup | **59** / **49** / 55 | same |
| hihat Open | 46 | 46 |
| hihat EdgeOpen | 78 | **46** (folded) |
| hihat CupOpen (*PCY100 only*) | 85 | **46** (folded) |
| hihat Close | 42 | 42 |
| hihat EdgeClose | 79 | **42** (folded) |
| hihat CupClose (*PCY100 only*) | 86 | **42** (folded) |
| hihat FootClose | 44 | 44 |
| hihat FootSplash | **83** | **46** (folded) |
| kick 1 | 36 | 36 |
| kick 2 (double-bass, pedal-derived) | 35 | 35 |
| pad 8 / 10 / 11 / 12 | 57 / 15 / 16 / 56 | 52 / 54 / 56 / 65 |

**Yamaha's crash Bow=59 / Edge=49 is the mirror image of Roland's crash Bow=49 / Edge=55.**
Any pivot that reasons on note numbers alone will silently swap bow and edge between these
two vendors.

### 2.3 ATV aD5 — abstract zone letters

S11 (p.11 and p.28). The aD5 does **not** name zones physically at the data level; it names
them `A`, `B`, `C` and then *maps* physical meanings per instrument group:

| aD5 zone | SNARE | HI-HAT | CRASH | RIDE (implied) |
|---|---|---|---|---|
| Zone A | Head | Bow | Bow | Bow |
| Zone B | Rim | Edge | Edge | Edge |
| Zone C | **Side Stick** | **Foot** | – | Cup |

Trigger-input → zone table (S11 p.28, verbatim):

| aD5 trigger input | Corresponding zone | Choke |
|---|---|---|
| KICK (K) | Head | – |
| SNARE (SN) | Head, Rim | YES |
| TOM 1/2/3 | Head | – |
| HIHAT (HH) | Bow, Edge | YES |
| CRASH (CR) | Bow, Edge | YES |
| RIDE (RD) | Bow, Edge, Cup | YES |
| AUX 1 | Head, Rim (Bow, Edge) | YES |
| AUX 2 | Head, Rim (Bow, Edge) | YES |
| CTL | hi-hat control pedal | – |

The aD5 documents interop failure explicitly (S11 p.16): *"When the aD5 is used to communicate
via MIDI with electronic drums from another manufacturer, your performance may not reproduce
correctly due to differences in velocity messages and **hi-hat control protocols**."*

### 2.4 EFNOTE — zone letters + physical mapping + per-zone open/closed notes

S13 p.11–12. Same A/B/C abstraction as ATV, different physical mapping:

| EFNOTE zone | Kick | Snare | Toms | Crashes / Ride | Hi-Hat |
|---|---|---|---|---|---|
| A | (kick) | Head | Head | Bow | Bow |
| B | – | Rim | Rim | Edge | Edge |
| C | – | **Side-Rim** | – | **Cup** | **Pedal** |

EFNOTE `ZONE EDIT > MIDI` parameters, per zone: `MIDI Note`, `Open` (note for hi-hat open
state on this zone), `Closed` (note for hi-hat closed state on this zone), `Pedal CC`
(control-change number for hi-hat pedal — **user-settable**).

EFNOTE default note numbers (S13 p.12), exhaustive:

| | Note# | | Note# | | Note# |
|---|---|---|---|---|---|
| Kick | 36 | HH Open Bow | 46 | Crash 1 Bow | 49 |
| Snare Head | 38 | HH Open Edge | 26 | Crash 1 Edge | 55 |
| Snare Rim | 40 | HH Open **Pedal Splash** | 44 (CC#4=0) | Crash 1 **Cup** | **54** |
| Snare **Side-rim** | 37 | HH Closed Bow | 42 | Crash 2 Bow | 57 |
| Tom 1 Head/Rim | 48 / 50 | HH Closed Edge | 22 | Crash 2 Edge | 52 |
| Tom 2 Head/Rim | 45 / 47 | HH Closed **Pedal Close** | 44 (CC#4=127) | Crash 2 **Cup** | **56** |
| Tom 3 Head/Rim | 43 / 58 | | | Crash 3 Bow/Edge | 27 / 28 |
| Tom 4 Head/Rim | 41 / 39 | | | Ride Bow/Edge/Cup | 51 / 59 / 53 |

**EFNOTE is Roland-note-compatible but adds crash Cup on notes 54/56, and disambiguates
pedal chick vs pedal splash using the CC#4 value, not the note number** — note 44 is used for
both, distinguished only by whether CC#4 was 0 or 127 immediately before.

### 2.5 GEWA G9 — "components"

S14. GEWA calls zones **components**: `Head|Bow`, `Rim|Edge`, `Bell`, `Choke` (S14 §12.2
Trigger Monitor colour table). Cymbal component sets by cymbal type (S14 §3.2.3):

| Cymbal type | Components | Trigger Type |
|---|---|---|
| Single-zone cymbal | **Edge** (only) | Single/Dual |
| 2-zone cymbal | Bow \| Edge | Dual |
| 3-zone cymbal, no separate bell output | Bow \| Edge \| Bell | Dual |
| 3-zone cymbal with separate bell output | Bow \| Edge + Bell (separate channel) | 3Way |

Hi-hat is explicitly a 3-zone cymbal (Bow/Edge/Bell), plus two pedal articulations with their
own volume controls: **Pedal Chick Volume** and **Pedal Splash Volume** (S14 §9.3.4), and
separate **Chick Sensitivity** and **Splash Sensitivity** trigger parameters (S14 §11).

Two GEWA constraints matter to KITWARP:
1. **"MIDI IN signals regarding trigger detection of connected pads are fixed and can't be
   modified"** (S14 §9.2.2). Only MIDI **OUT** is remappable. A GEWA G9 as *target* device
   therefore has a fixed input layout; KITWARP must own the whole translation.
2. GEWA velocity monitoring reserves **126–127 as a "Peak" band**, normal range 0–125
   (S14 §8, Trigger Monitor). Marked **UNVERIFIED** as to whether transmitted MIDI velocity is
   actually clamped at 125 — the manual describes the monitor display, not the wire format.

### 2.6 2Box DrumIt Five — numeric zones

S12. 2Box is the outlier: zones are **ordinal integers per channel**, not names.

- `ZONES` (per channel) = number of zones for that channel, derived from the trigger type
  (S12 §Unit-Interface).
- `NOTE` = **base** MIDI note. *"If the associated trigger type has more than one zone (like
  cup, bow, edge and choke), the additional zones are mapped onto consecutive higher notes."*
  Example given: NOTE=E4, ZONES=4 → E4, F4, F#4, G4.
- Cymbal zone ordering seen in the trigger-calibration text (S12 §Unit-Trig): zone **1 = cup**,
  zone **4 = bow** ("so only hard hits on the bow give full level on zone 4 … so only hard cup
  hits give full level on zone 1").
- Zone **8** is the "percussion" redirect target: if no sound is selected on the percussion
  channel, the rim trigger is *"redirected to zone 8 on the snare or tom channel"* (S12 §Sounds).
- **Choke is a zone** in 2Box's model, i.e. it consumes a note number, not aftertouch.
- Documented factory default: hi-hat channel base is such that *"the HIHAT drum channel uses
  MIDI notes A2-A#2-B2 to control the Bow, Edge and Foot zones"* (secondary source; the manual
  shows the factory NOTE picture but the extracted text does not carry the numbers) —
  **UNVERIFIED** at note-number level; the *contiguous-ascending-zones rule* IS verified.

### 2.7 Alesis

Two different models inside one brand:

**Alesis Strike / Strike Pro** (S15) — fully user-mapped, and the *whole* hi-hat protocol is a
global switch:

| Setting | Description (verbatim, S15 p.30) | Values |
|---|---|---|
| HiHat | "This determines whether the hi-hat MIDI note will be sent with or without a MIDI CC message (CC#4)." | `Note+CC#4`, `Note Only` |
| HiHat Splash | "…whether or not the hi-hat 'splash' note (generated by quickly pressing then releasing the pedal) will be sent." | Sent / Not Sent |
| Cymbal Choke | "…whether or not the cymbal 'choke' note (generated by grabbing the cymbal's choke strip) will be sent." | Sent / Not Sent |

**⇒ Alesis transmits choke as a NOTE**, where Roland/EFNOTE/Yamaha transmit choke as
polyphonic key pressure. This is a hard structural difference, not a naming difference.

Per-trigger MIDI parameters (S15 p.19): `MIDI Note` 000–127, `Gate Time`
(Off, 00–99 ms, 1/32, 1/16, …), `Note Off` (Not Sent / after gate / …). Alesis exposes
**note-off policy as a per-zone parameter**.

Alesis zone names used in the UI: `HiHat Bow`, `HiHat Edge` (S15 p.19, p.21).

**Alesis Nitro Max** (S16 §5.2) — publishes a default table, and it is *note-only* with a
three-level openness ladder:

| Trigger | Note | Trigger | Note |
|---|---|---|---|
| Kick | 36 | Ride | 51 |
| Snare | 38 | Crash 1 | 49 |
| Snare Rim | 40 | Crash 2 | 57 |
| Tom 1 / Tom 1 Rim | 48 / 50 | **Hi-Hat Open** | 46 |
| Tom 2 / Tom 2 Rim | 45 / 47 | **Hi-Hat Half-Open** | **23** |
| Tom 3 / Tom 3 Rim | 43 / 58 | **Hi-Hat Closed** | 42 |
| Tom 4 / Tom 4 Rim | 41 / 39 | **Hi-Hat Pedal** | 44 |
| | | **HH Splash** | **21** |

Alesis support (S18) states the design intent for the CC-based models:
*"the hi-hat regardless of position is still the hi-hat cymbal, and it's relative position is
indicated by a CC value as it opens and closes"* — described as a property of "Nitro and above",
as against entry kits that use separate note values. The article does **not** name the CC number
(the CC#4 figure for Alesis comes from S15, the Strike guide).

### 2.8 Pearl Mimic Pro

S17 (manual v1.03, the version actually read). **Verified from the retrieved text:**

- **Zones are per-piezo tabs**: the trigger UI has a `Center-Piezo` tab and a `Rim-Piezo` tab.
  Cymbal zones referenced are `Bow/Edge` and `bell` — *"Ride cymbals use two cables to send to
  Mimic Pro signals from Bow/Edge zone and from bell zone separately"* (S17 l.414-417), and
  cymbal zone volumes are described for *"Bow zone … Edge and Bell zones"* (S17 l.719-722).
- **`Rimshot` is NOT a separate zone — it is a threshold-derived articulation.** Every zone tab
  carries a `Rimshot Threshold` fader; on a dual-piezo pad *"both zone tabs have a Rimshot
  Threshold fader – Center and Rim … you can have full dynamic range of rim articulation (rim
  click, or sidestick) **with the ability to play rimshots**"* (S17 l.789-792). So the same Rim
  zone yields `sidestick | rim click | rimshot` purely by velocity threshold — the identical
  mechanism as Yamaha's `Xstick Adjust`.
- **MIDI Input and MIDI Output notes/channels are editable independently, per pad zone**
  (S17 "MIDI" tab, l.973-978): *"In this tab you can setup MIDI notes and channels for your pad
  zones. You can edit MIDI Input and MIDI Output notes and channels independently from each
  other, or together by pressing the Link Edit button."* The module is itself a remapper.
- **Hi-hat has a `Max Open` / `Max Close` calibration plus a third, separate
  `Close/Open Border Threshold`** — *"imagine you are closing an acoustic Hi-Hat and the top hat
  barely touches the bottom hat, but the sound of the Hi-Hat is not really closed yet"*
  (S17 l.601-612) — and a `Hi-Hat Control Curve` (S17 l.616-623). Same "note border" concept as
  Roland's `HH Note# Border` and Yamaha's `FootClosePos`.
- **Note-name root offset is user-selectable** (v1.0.3 feature, S17 l.2106-2112):
  `Show Middle C (60) Note As: C3 | C4 | C5`. Pure display, but it is exactly the reason
  third-party mapping tables disagree by an octave. KITWARP data must store **note numbers**,
  never note names, and should record which octave convention a scraped source used.
- **Ride Split**: two inputs for a 3-zone ride, or split into two single-input ride cymbals
  (S17 l.2101-2105).

**UNVERIFIED for Mimic Pro** (claimed by secondary sources, not found in the v1.03 text I read):
that the hi-hat pedal uses **CC4** and that the CC is sent *"on the Hi-Hat Bow Note MIDI
Channel"*. The manual documents hi-hat *calibration* thoroughly but never names a CC number.
No default note-number table is published; the module ships fully user-mapped.

### 2.9 THE HI-HAT CONTROLLER CC TABLE (the deliverable)

| Vendor / module | Pedal-position CC | Configurable? | Value polarity | Value range | Source |
|---|---|---|---|---|---|
| **Roland TD-17** | **CC4 (Foot Controller)** | no (fixed on TD-17) | **0 = open → max = closed** | **0–90** (`00H–5AH`) as transmitted | S2 l.320-328 |
| **Roland TD-27 / TD-50 / TD-50X** | **CC4 default** ("the foot controller is set to Pedal CC" in the factory example, S1 l.5137) | **yes** — `[SYSTEM]-[MIDI]-[CONTROL] HH Pedal CC` ∈ {1 Modulation, 2 Breath, **4 Foot**, 11 Expression, 16–19 General 1–4, 80–83 General 5–8} | 0 = open → max = closed | **0–90 or 0–127**, selected by SysEx param `HI-HAT CC MAX` (values literally "90, 127") | S1 §Control Change, S1 l.2099-2100 |
| **Yamaha DTX (DTX502, DTX-PRO/PROX, DTX900 line)** | **CC4 (Foot Controller)** — "transmitted and received" | no | 0 = open → 127 = closed | 0–127 | S10 §2.2.3 |
| **Alesis Strike / Strike Pro** | **CC4** | only on/off: `Note+CC#4` vs `Note Only` | (not stated) | (not stated) | S15 p.30 |
| **Alesis Nitro Max** | **none** — note-only, 3-level openness ladder + splash note | n/a | n/a | n/a | S16 §5.2 |
| **Pearl Mimic Pro** | **UNVERIFIED** — no CC number named anywhere in the v1.03 manual; secondary sources say CC4 on the Hi-Hat Bow zone's channel | (not stated) | (not stated) | (not stated) | S17 (absence), secondary |
| **2Box DrumIt Five** | **CC1 or CC4**, user-selected | **yes** | **user-selectable both ways**: 0=open→127=closed, *or* 0=closed→127=open | 0–127 | S12 §Unit-HiHat Pedal |
| **ATV aD5** | (CC number not stated in the Reference Guide) — manual warns explicitly about "differences in … hi-hat control protocols" between makers | (not stated) | (not stated) | (not stated) | S11 p.16, p.28 — **UNVERIFIED which CC** |
| **EFNOTE 3/5/7** | **CC4 default**, per-zone parameter `Pedal CC` | **yes** (per zone) | **0 = open → 127 = tight closed** | 0–127 | S13 p.11-12 |
| **GEWA G9** | **CC4 default** (`HHPedal CC`), selectable from {off, 1 Modulation, 2 Breath, **4 Foot**, 11 Expression, 16–19 General 1–4} | **yes** | (not stated) | (not stated) | S14 §12.3.1.1.4 |

**Answer to "CC4 vs CC1 vs CC2":** CC4 is the de-facto standard across every vendor examined.
CC1 appears only as (a) a *selectable alternative* on 2Box and (b) an option in Roland's and
GEWA's selectable list. CC2 (Breath) exists only as a Roland/GEWA menu option. **No vendor
ships CC1 or CC2 as its default.** The real interop hazards are not the CC number but:
1. **range** (Roland 0–90 vs everyone else 0–127),
2. **polarity** (2Box can invert it),
3. **whether it is sent at all** (Alesis `Note Only`; Nitro Max never),
4. **when it is sent** (see §2.10),
5. **which channel it is sent on** (Roland: "the channel to which HI-HAT\<BOW\> is assigned";
   Mimic Pro: "Hi-Hat Bow Note MIDI Channel" — *not* necessarily the global drum channel).

### 2.10 Timing / ordering semantics of the pedal CC (a note number cannot carry this)

Every vendor that sends CC4 states the **ordering rule**, and it is load-bearing:

- Roland: *"Striking the hi-hat pad causes the data to be transmitted as pedal position data
  **before the note-on message**"* (S1 transmit §; S2 l.328).
- EFNOTE: *"…sends MIDI control change #4 … **before the corresponding note message**"* (S13 p.12).
- 2Box: *"Normally MIDI pedal data is only sent **just before a note on**, selections with a `!`
  indicate that pedal changes are sent **continuously**."* (S12) — i.e. per-strike snapshot vs
  continuous stream is a user setting.

⇒ The pivot needs a notion of a **controller value attached to an event** (pre-note CC), distinct
from a free-running controller stream. Roland/EFNOTE default to the former; 2Box can do either.

### 2.11 Positional sensing (also not carriable by a note number)

Roland TD-27/TD-50X (S1) defines **four independent positional CC assignments**, each freely
mappable to CC 1/2/4/11/16–19/80–83, all sent **immediately before** the note-on on the same
channel:

| Roland setting name | Applies to | Semantic axis of the CC value |
|---|---|---|
| `Snare CC` | snare pad **head and rim** | head: **centre → perimeter**; rim: **deep → shallow** |
| `Ride CC` | ride pad **bow** | centre → perimeter |
| `Toms/AUXs CC` | heads **and rims** of TOM 1–3 and AUX 1–3 | as above |
| `Hi-Hat CC` | hi-hat pad **bow** | centre → perimeter |
| `Hi-Hat LR CC` | hi-hat pad **bow and edge** | **left → right** (a different geometry!) |

Preconditions (S1): a position-capable Trig Type or a digital pad, plus
`[SYSTEM]-[TRIGGER]-[PARAM] Position Detect Head/Rim = ON` (SysEx addresses `00 0A`,
`00 0B` — head and rim are **independently** switchable).

GEWA G9 ships the same four-CC architecture with **different factory defaults**
(S14 §12.3.1.1.4): `HHPedal CC` = 4, `Snare CC` = **16**, `Ride CC` = **17**,
`Toms/Aux CC` = **18**. GEWA's positional sensing is described sample-side as a
**Centre-Side blend** with three sample-set flavours: `CS` (centre-side blend, positional
active), `C` (centre only), `S` (side only) — the latter two "de facto deactivate positional
sensing" (S14 §9.2.x Sound Grouping).

Yamaha DTX-PRO/PROX has positional sensing as a **boolean per input**, not a transmitted CC:
`Snare Position off/on` ("tonal changes according to the location within a zone that is struck")
and `Ride Position off/on` ("position sensor for the **bow** of the ride cymbal") — S9 p.59.
**No evidence found that DTX-PRO transmits stick position over MIDI at all.** Marked
**UNVERIFIED**; the DTX MIDI data format section was not retrieved for the PRO generation.

Alesis, 2Box, EFNOTE, ATV, Mimic Pro: no positional-sensing MIDI transmission found in the
retrieved manuals.

### 2.12 Choke — three incompatible encodings

| Vendor | Choke encoding | Continuous? | Source |
|---|---|---|---|
| Roland TD-17 | Poly Key Pressure on the head/rim note; **7FH on grab, 00H on release** (binary) | no | S2 l.305-313 |
| Roland TD-27 (analog pads) | Poly Key Pressure, 7FH / 00H | no | S1 l.500-505 |
| Roland TD-27 (**digital** pads CY-18DR, VH-14D) | Poly Key Pressure, **continuous 7FH→00H "according to the strength of choking"**, and also transmitted "when you place your hand on the sensor" (i.e. *pre-strike damping*, not just cut-off) | **yes** | S1 l.504-509 |
| Roland (received) | Poly Key Pressure: "If the value is greater than 1, the **decay** of the note sounded by the received note number will be **shortened** based on the value" | yes | S1 l.42-43 |
| EFNOTE | *"The cymbal choke technique sends the polyphonic after touch (key after touch) message."* | (not stated) | S13 p.12 |
| **Alesis Strike** | a **choke NOTE** (on/off switch: Sent / Not Sent) | no | S15 p.30 |
| **2Box** | choke is **a zone** → its own note number in the ascending zone run | no | S12 |
| GEWA G9 | "Choke" is a first-class **component** alongside Head/Bow, Rim/Edge, Bell, detected by FSR with its own Threshold | (transmission form not stated) | S14 §11, §12.2 |
| ATV aD5 | choke supported on SN, HH, CR, RD, AUX1, AUX2 (transmission form not stated) | – | S11 p.28 |

### 2.13 Other module-level semantics with no drum-remap equivalent

| Semantic | Vendor evidence |
|---|---|
| **Openness threshold ("note border")** — the pedal CC value at which the module *switches* which note it emits for a hi-hat strike | Roland: `[SYSTEM]-[MIDI]-[CONTROL] **HH Note# Border**` (S1 l.493). Yamaha: `FootClosePos -32–0` (S9 p.59). Mimic Pro: "Close/Open Border Threshold Level". EFNOTE: implicit via per-zone Open/Closed notes. **The same physical stroke yields a different note number depending on a user-tunable threshold.** |
| **Foot splash vs foot chick are separate articulations** | Yamaha: distinct sources `HhFtCl` / `HhFtSp`, distinct notes 44 / 83 (S10). Alesis Nitro Max: 44 / 21 (S16). GEWA: separate Chick and Splash sensitivity + volume (S14). Roland/EFNOTE: **same note 44**, disambiguated only by CC context (EFNOTE) or by pedal motion (Roland). 2Box: *"A short time between down and up results in a foot splash, a longer time results in a foot chick"* — a **duration-derived** articulation, not encoded at all in the note. |
| **Snares-off as an orthogonal state, not one articulation** | Yamaha DTX900 sources `snrHdOff`, `snrOpOff`, `snrClOff` — snares-off ×{head, open rim, closed rim} = a **cross product**, not a single `snare/wires-off` tag (S9). |
| **Brush mode as an alternate note for the same zone** | Roland `Note No. (SNARE<BRUSH>)`, gated by `[KIT EDIT]-[OTHER]-[BRUSH SW]`, transmitted **on the SNARE\<HEAD\> channel** (S1 l.29-31). TD-25 default 23 (S7). |
| **Cross-stick as an alternate note for the RIM zone, gated by a switch or a pad capability** | Roland: `NOTE NO. (SNARE<XSTICK>)` received/transmitted **on the SNARE\<RIM\> channel**, only when XStick Switch is ON *or* a cross-stick-capable digital pad (PD-140DS) is fitted; the module also has an `Analog XStick Threshold` and `Xstick Adjust` (S1, S9). Yamaha models the same thing as `SnareOp`/`SnareCl` with an `Xstick Adjust 1–127` that trades open rimshot against cross-stick **by strike strength** (S9 p.59). |
| **Kick rim** | Yamaha `KickRm` is a first-class trigger input source (S9 p.9). No other vendor exposes it. |
| **Second kick / double bass derived from the hi-hat pedal** | Yamaha DTX502 `kick 2` = note 35, *"output only when DblBass is set to 'on' and the hi-hat controller is operated"* (S10). A pedal gesture producing a **kick** note. |
| **High-resolution velocity (CC88 prefix)** | Roland TD-27 transmits/receives `High Resolution Velocity Prefix (CC88)`, giving 0.5 steps over **317 levels (1 … 159)** for digitally-connected pads — velocities **above 127** are representable (S1 l.245-264, l.777-793). Gated by `HI-Reso Velocity` on/off. |
| **Gate time / note-off policy** | Roland: note-off after a per-kit `Gate Time`, note-off velocity fixed 40H (S1). Alesis: per-zone `Gate Time` and `Note Off` = {Not Sent, after gate, …} (S15 p.19). 2Box: pedal-down sends note-on, pedal-up sends the note-off. |
| **Note-number collision policy** | Roland: if a received note matches multiple pads, "the head instrument is heard" / topmost row wins (S3 p.11). ATV: "only one of the zones will produce sound" (S11 p.16). ⇒ vendor layouts are **not injective**, so an inverse mapping is not always well-defined. |
| **Per-zone MIDI channel** | Mimic Pro: per-zone note **and** channel, with MIDI-in and MIDI-out mappings editable independently (S17 MIDI tab). Roland: per-**pad** channel (`[KIT MIDI]-[MIDI CH]`), and the pedal CC and positional CCs are scoped to *that pad's* channel. 2Box: per-channel `CHAN`. ⇒ channel is part of the address, not a constant 10. |
| **Fixed-input devices** | GEWA G9: "MIDI IN signals regarding trigger detection of connected pads are **fixed and can't be modified**" (S14 §9.2.2). |

---

## 3. Implications for the KITWARP pivot vocabulary

### 3.1 The single most important structural finding

drum-remap's model is `instrument / articulation (/ instance)` — a **flat pair plus an index**.
Every module examined instead factorises the same information as roughly

```
instrument × instance × ZONE × STATE × MODIFIER  + continuous controllers
```

where **ZONE (striking position) is orthogonal to STATE (hi-hat openness, snares on/off, brush
on/off)**. Yamaha proves the orthogonality is real, not cosmetic, because it takes the *cross
product*: `{Hd, Op, Cl} × {snares-on, snares-off}` = 6 sources; `{Bw, Eg, Cp} × {open, closed}`
= 6 hi-hat cymbal sources. Encoding these as flat articulation strings (`snare/wires-off`,
`hihat/closed-edge`) works until a vendor adds a third dimension, and then the enumeration
explodes combinatorially instead of multiplying.

**Recommendation: make `zone` a first-class axis.**

### 3.2 Proposed normalised ZONE vocabulary (the striking-position axis)

Membrane / drum family:

| Pivot zone ID | Meaning | Vendor terms that map onto it |
|---|---|---|
| `head` | main playing surface of a membrane pad | Roland `<HEAD>`; Roland internal `HEAD`; Yamaha `Hd` / `Head`; ATV `Zone A` (snare/tom); EFNOTE `Zone A` / `Head`; GEWA component `Head`; Alesis (bare trigger name); Mimic Pro `Center`; 2Box zone-n (head) |
| `rim` | rim struck with the shoulder, sounding with the head | Roland `<RIM>`; Roland internal `RIM`; Yamaha `Rm`, `Rm1`, `OpenRim`/`Op`; ATV `Zone B` (snare); EFNOTE `Zone B` / `Rim`; GEWA `Rim`; Mimic Pro `Rim` (`Rim-Piezo` tab); Alesis `… Rim` |
| `rim2` | second, distinct rim zone on multi-rim pads | Yamaha `Rm2` (`Pad14Rm2`, `tom1Rm2`…`tom4Rm2`) |
| `crossstick` | stick laid across the head, tip/butt on the rim | Roland `<XSTICK>` / `X-Stick`; Yamaha `ClosedRim` / `Cl`; ATV `Zone C` = `Side Stick`; EFNOTE `Zone C` = `Side-Rim`; GEWA sample class `X-Stick` |
| `shell` | shell / hoop-side strike | (no module exposes it; reserved) |

Cymbal family:

| Pivot zone ID | Meaning | Vendor terms |
|---|---|---|
| `bow` | main body of the cymbal | Roland `<BOW>` (and internal `HEAD` on cymbal inputs); Yamaha `Bw`; ATV `Zone A` = `Bow`; EFNOTE `Zone A` = `Bow`; GEWA `Bow`; Alesis `HiHat Bow`; 2Box zone 4; Mimic Pro `Bow` |
| `edge` | outer rim / crash zone | Roland `<EDGE>` (and internal `RIM`); Yamaha `Eg`; ATV `Zone B`; EFNOTE `Zone B`; GEWA `Edge` (also the *only* component of a single-zone GEWA cymbal); Alesis `HiHat Edge`; Mimic Pro `Edge` |
| `bell` | cup / bell | Roland `<BELL>` (ride only); Yamaha `Cp` (`Cup`, on **ride, crash and hi-hat**); ATV `Cup`; EFNOTE `Zone C` = `Cup`; GEWA `Bell`; 2Box zone 1; Mimic Pro `Bell` |

**`bell` and `cup` are the same zone.** drum-remap's `ride/bell` + separate `megabell`
instrument conflates a *zone* with an *instrument*; `megabell` should be an instrument whose
`bell` zone is large, not a separate lexeme.

Pedal / foot family — these are **not striking positions** and must live on a separate axis
(see §3.3), but they are frequently named as "zones" by vendors, which is exactly the trap:

| Vendor term | What it actually is |
|---|---|
| ATV `Zone C` on HI-HAT = `Foot` | pedal articulation |
| EFNOTE `Zone C` on Hi-Hat = `Pedal` | pedal articulation |
| Roland `HH PEDAL` | pedal articulation |
| Yamaha `HhFtCl`, `HhFtSp` | pedal articulations |
| 2Box `Foot` zone | pedal articulation |

**Cross-vendor zone-count reality check** (this is the coverage the pivot must reach):

| | Roland | Yamaha | ATV aD5 | EFNOTE | GEWA G9 | 2Box | Alesis | Mimic Pro |
|---|---|---|---|---|---|---|---|---|
| snare zones | head, rim, crossstick | head, rim(open), crossstick(closed) ×{snares on/off} | head, rim, crossstick | head, rim, crossstick | head, rim (+choke) | numeric | head, rim | center, rim (rimshot/sidestick = velocity threshold on either) |
| tom zones | head, rim | head, rim (+rim2 on DTX900) | head only | head, rim | head, rim | numeric | head, rim | center, rim |
| crash zones | bow, edge | **bow, edge, cup** | bow, edge | **bow, edge, cup** | **bow, edge, bell** | numeric | bow, edge | bow, edge, bell |
| ride zones | bow, edge, bell | bow, edge, cup | bow, edge, cup | bow, edge, cup | bow, edge, bell | numeric | (bow) | bow, edge, bell |
| hi-hat cymbal zones | bow, edge | **bow, edge, cup** (PCY100) | bow, edge | bow, edge | **bow, edge, bell** | bow, edge | bow, edge | bow, edge |
| kick zones | 1 | **kick + kickRm** | 1 | 1 | 1 | numeric | 1 | 1 |

**Missing from drum-remap: `crash/cup`, `hihat/cup`, `tom/rim` (drum-remap has only `tom/hit`),
`tom/rim2`, `kick/rim`, and any generic `aux`/`pad` instrument.** Roland alone ships up to
**AUX 1–4 × {head, rim} = 8 note slots** with no fixed instrument identity; drum-remap has no
way to name them at all.

### 3.3 Axes the pivot needs (beyond drum-remap's instrument/articulation/role/instance)

1. **`zone`** — striking position, per §3.2. Closed enum.
2. **`state`** (orthogonal modal state), at minimum:
   - hi-hat openness: `closed | half | open` plus a continuous `openness` value; note that
     Roland/EFNOTE ship **2** discrete levels, Alesis Nitro Max ships **3**, and drum libraries
     want more. drum-remap's mixture of named (`tight`, `closed`, `open`) and ordinal
     (`open-0..3`) values is the right *content* but the wrong *shape* — it belongs on this axis
     as `{level: int, of: int}` or a normalised 0..1, not baked into the articulation string.
   - snare wires: `on | off` (Yamaha takes the cross product with all 3 snare zones).
   - brush mode: `on | off` (Roland: a whole alternate note for the head).
3. **`pedal`** — a separate articulation axis for foot events: `chick` (foot close),
   `splash`, and `sustain-position` (the continuous value). Yamaha, GEWA and Alesis Nitro Max
   distinguish chick from splash **by note**; Roland and EFNOTE distinguish them **only by
   controller context**; 2Box distinguishes them **by pedal-motion duration**. A pivot that has
   only drum-remap's `hihat/pedal` + `hihat/pedal-ching` cannot round-trip Yamaha→Roland
   without knowing this is the same axis.
4. **`controller`** — first-class continuous controllers with declared semantics, at minimum:
   - `hihat.pedal_position` (0 = open → 1 = closed, **normalised**, because Roland's wire range
     is 0–90 and 2Box's polarity is user-invertible)
   - `strike_position.radial` (centre → perimeter) for snare/tom heads, ride bow, hi-hat bow
   - `strike_position.rim_depth` (deep → shallow) for rims — **a different geometry from radial**
   - `strike_position.lateral` (left → right) for the Roland `Hi-Hat LR CC` case
   - `choke_amount` (0..1, continuous on Roland digital pads)
   Each pivot controller needs, per device layout: CC number, value range, polarity, channel
   scoping, and **emission timing** (pre-note snapshot vs continuous).
5. **`instance`** — keep, but fix drum-remap's inconsistency. Vendors are uniformly **ordinal
   and 1-based**: `TOM 1..4`, `CRASH 1..2` (EFNOTE: `Crash 1..3`), `AUX 1..4`, `Pad3/5/7/13/14`,
   `kick 1 / kick 2`. Use `{instrument, index:int}` and derive human labels ("left crash") from
   a per-layout presentation table. Never store `left`/`right`/`far-left` as the identity.
6. **`role`** — drum-remap's role enum has **no counterpart anywhere in module firmware**.
   No module has any concept of foundation/backbeat/ghost/timekeeping. Roles are a
   *library-side* / musical annotation. Keep it, but it must be **optional metadata that never
   participates in device-layout identity**, or hardware round-trips will be non-deterministic.

### 3.4 Distinctions that are REAL (must be representable)

- `bow` vs `edge` vs `bell` on cymbals — universal, and **note numbers reverse between vendors**
  (Roland crash bow 49 / edge 55 vs Yamaha crash bow 59 / edge 49). Provably lossy without a
  zone axis.
- `crash/cup` and `hihat/cup` — Yamaha, EFNOTE, GEWA ship them; Roland does not. Downward
  translation needs a declared fallback (`cup → bow` with a velocity delta, per drum-remap's
  existing chain mechanism).
- `tom/rim` — every mid-range and up module has it; drum-remap has no `tom/rimshot`.
- `crossstick` as a zone rather than an articulation — Yamaha's `Xstick Adjust` shows that
  cross-stick and open rimshot are **the same physical zone selected by strike strength**.
- Foot **chick** vs foot **splash** — separately notated by Yamaha/Alesis/GEWA.
- Snares-off × zone cross product — Yamaha.
- Hi-hat openness discretisation level count — 2 (Roland, EFNOTE), 3 (Alesis Nitro Max),
  continuous (any CC-driven library).
- Choke as **aftertouch** (Roland, EFNOTE) vs choke as a **note** (Alesis, 2Box) vs choke as a
  **component/zone** (GEWA). This is a message-*type* difference; a pivot that only maps notes
  loses choke entirely on Roland→Alesis and gains a phantom note on Alesis→Roland.
- Kick rim (Yamaha), second kick from the hi-hat pedal (Yamaha DblBass).
- High-resolution velocity >127 (Roland TD-27 CC88).
- Per-zone MIDI channel and per-zone note-off/gate policy (Mimic Pro, Alesis, Roland).

### 3.5 Distinctions that are COSMETIC (must be normalised away)

- Roland `<BOW>`/`<EDGE>` vs Roland's own `HEAD`/`RIM` for the *same* cymbal input.
- `cup` (Yamaha, ATV, EFNOTE) vs `bell` (Roland, GEWA, Mimic Pro).
- `Side Stick` (ATV) vs `Side-Rim` (EFNOTE) vs `X-Stick` (Roland) vs `ClosedRim` (Yamaha).
- `OpenRim` (Yamaha) vs `Rim`/`Rimshot` (Roland, Mimic Pro) vs `Rim` (everyone).
- `Zone A/B/C` (ATV, EFNOTE) — a *presentation* indirection over the same physical zones; the
  A/B/C letters are only meaningful together with the instrument family.
- `component` (GEWA) vs `zone` (everyone) vs `trigger input source` (Yamaha).
- Vendor pad/instance names: `Pad3`, `Pad13`, `AUX 1`, `Crash 3`, `T1` — all just
  `{family, index}`.
- 2Box's numeric zone indices — a *serialisation* of an ordered zone list, resolvable to named
  zones given the trigger type.

### 3.6 Consequences for the ID scheme and fallbacks

- **Stable numeric IDs are mandatory, and vendors prove it**: Yamaha ships **three mutually
  incompatible note maps for its own products** (`PRO/PROX`, `DTX900`, `DTX700`) and exposes
  them as a `Note Map` selector (S9). Roland ships a `HH Note# Border` that changes which note a
  given stroke produces. A layout is therefore `(vendor, model, **map revision**, user overrides)`
  — provenance and versioning must be in the data model from day one.
- **Note numbers cannot be the pivot key.** Modules are explicitly non-injective by design
  (Roland: "if the note number overlaps between head and rim, the head instrument is heard";
  ATV: "only one of the zones will produce sound"). The pivot must key on
  `(instrument, instance, zone, state, pedal)` and treat note numbers as a per-layout binding.
- **Fallback chains need a zone-aware dimension**, because the natural degradations are
  per-axis: `cup → bow`, `rim2 → rim`, `edge → bow`, `crossstick → rim`, `half-open → closed`,
  `snares-off → snares-on`. drum-remap's per-tag curated chains would need
  O(zones × states) hand-written entries; a per-axis degradation rule generates them.
- **1→N expand rules must extend to controllers.** drum-remap already expands
  `open-close hihat → open hit + pedal close`. The module data shows the mirror requirement:
  Roland/EFNOTE encode splash-vs-chick *in the CC value that precedes note 44*, so
  `pedal/splash → note 44 + CC4=0` and `pedal/chick → note 44 + CC4=127` are **N→1 collapses
  with a controller side-channel**, and Alesis Nitro Max needs `pedal/splash → note 21`.
  The rule engine needs to emit and consume controller values, not only notes.
- **Controller translation needs a normalisation contract.** Minimum per-layout controller
  descriptor: `{cc_number, min, max, polarity, channel_scope, emission: pre_note|continuous}`.
  Without `max`, a Roland TD-17 (0–90) driving a library expecting 0–127 never reaches
  fully-closed; without `polarity`, a 2Box user's inverted pedal is silently backwards.

---

## 4. Provenance

All licences: **manufacturer documentation, © the respective manufacturer**, retrieved for
reference/interoperability research only. No source text is reproduced in KITWARP's data files;
only factual note numbers and terminology (not copyrightable as such) are used.

| Ref | URL | Retrieved | Notes |
|---|---|---|---|
| S1 | https://static.roland.com/assets/media/pdf/TD-27_MIDI_Imple_eng03_W.pdf | 2026-09-06, HTTP 200 | © Roland Corporation |
| S2 | https://static.roland.com/assets/media/pdf/TD-17_MIDI_Imple_eng04_W.pdf | 200 | © Roland |
| S3 | https://static.roland.com/assets/media/pdf/TD-17_DataList_eng01_W.pdf | 200 | © Roland |
| S4 | https://support.roland.com/hc/en-us/articles/360005173411-TD-17-Default-MIDI-Note-Map | via web.archive.org/web/20250808010746 | live site 403s |
| S5 | https://support.roland.com/hc/en-us/articles/4407474950811-TD-27-Default-MIDI-Note-Map | via web.archive.org/web/20250629022847 | |
| S6 | https://support.roland.com/hc/en-us/articles/12190112095259-TD-50-TD-50X-Default-MIDI-Note-Map | via web.archive.org/web/20250629022847 | |
| S7 | https://support.roland.com/hc/en-us/articles/115000201706-TD-25-Default-MIDI-Note-Number-Map | via web.archive.org/web/20250629022850 | |
| S8 | https://support.roland.com/hc/en-us/articles/24553430488091-VAD103-Default-MIDI-Note-Map | via web.archive.org/web/20250808014959 | body says "Below is the Default MIDI Note Map for the **TD-07**" |
| S9 | https://data.yamaha.com/files/download/other_assets/3/2323553/DTX-PRO_DTX-PROX_reference_manual_En_v200_C0.pdf | 200 | © Yamaha; zone table p.9, trigger params p.59 |
| S10 | https://usa.yamaha.com/files/download/other_assets/9/329779/dtx502_en_rm_a0.pdf | 200 | © Yamaha; note table p.10, MIDI data format p.11 |
| S11 | http://www.atvcorporation.com/en/products/drums/ad5/file/602/aD5_rg_en05.pdf | 200 | © ATV Corporation; zones p.11, trigger table p.28 |
| S12 | https://2box-drums.com/wp-content/uploads/2023/05/DrumIt-Five-User-Manual-OS-1.24.pdf | 200 | © 2BOX |
| S13 | https://www.ef-note.com/products/drums/common357/EFNOTE_3_5_7_RG_en04.pdf | 200 | © EFNOTE; zones p.11, note map p.12 |
| S14 | https://gewadrums.com/manuals/gewadrums/01Digital%20Drums/01Module/g9/G9_OM_EN_Owners_Manual.pdf | 200 | © GEWA; CC table §12.3.1.1.4 |
| S15 | https://www.fullcompass.com/common/files/38928-StrikeModuleUserGuide.pdf | 200 | Alesis Strike User Guide, © inMusic |
| S16 | https://www.alesis.com/rscdn/2102/documents/Nitro%20Max%20Drum%20Module%20-%20User%20Guide%20-%20v1.1.pdf | 200 | © inMusic; §5.2 |
| S17 | https://images.thomann.de/pics/atg/atgdata/document/manual/pearl_mimic_pro_en.pdf | 200 | Pearl Mimic Pro v1.03, © Pearl |
| S18 | https://support.alesis.com/en/support/solutions/articles/69000851410-alesis-drums-why-does-the-hi-hat-send-the-same-midi-note-open-closed- | WebFetch 2026-09-06 | design-intent quote only; does not name the CC |

Additional URLs consulted but **not usable as primary evidence** (403 / no snapshot / secondary):
- https://support.roland.com/hc/en-us/articles/15607021831707-VAD706-Default-MIDI-Note-Map (403 live, no Wayback snapshot)
- https://support.roland.com/hc/en-us/articles/38488658966555-V71-Default-MIDI-Note-Map (same)
- https://support.roland.com/hc/en-us/articles/39323319201819-VAD716-Default-MIDI-Note-Map (same)
- https://support.roland.com/hc/en-us/articles/38775647024155-TD-07KV-Default-MIDI-Note-Map (same)
- https://support.roland.com/hc/en-us/articles/24553677957275-TD-02K-TD-02KV-Default-MIDI-Note-Map (same)
- https://support.roland.com/hc/en-us/articles/39437292857243-TD-17KVX-Default-MIDI-Note-Map (same)
- https://www.sweetwater.com/sweetcare/articles/control-change-data-transmitted-dtx-hi-hat-pedal-activated/ (403)
- https://pearldrum.com/sites/default/files/image_folder/SUPPORT/MANUAL/ELECTRONICS/2019-mimic-pro-user-manual.pdf (not fetched; Thomann mirror used instead)

## 5. Explicitly UNVERIFIED

1. Yamaha DTX-PRO/PROX **default note numbers** — the PRO-generation Data List was not located.
   The DTX502 table (S10) is a *different* Yamaha note map and must not be labelled "Yamaha".
2. Whether Yamaha DTX-PRO/PROX **transmits** stick position over MIDI (it has `Snare Position`
   and `Ride Position` on/off, but the retrieved manual does not describe a positional CC).
3. ATV aD5's hi-hat controller **CC number** — the Reference Guide describes calibration and the
   interop hazard but never names the CC.
4. Alesis CC4 **value range and polarity** — S15 names CC#4 but gives neither.
5. Pearl Mimic Pro's hi-hat pedal **CC number at all** (let alone range/polarity). The v1.03
   manual documents hi-hat calibration in detail but never names a controller number. The
   widely-repeated "CC4, sent on the Hi-Hat Bow Note MIDI Channel" claim comes from
   search-engine extraction of some Mimic Pro document, and I could not confirm it against the
   text I retrieved. No Mimic Pro default note table exists — the module ships user-mapped.
6. 2Box factory **note numbers** (the manual shows them as an image; only the
   base-note-plus-consecutive-zones *rule* was read as text).
7. Whether GEWA G9 actually clamps transmitted velocity to 0–125 with 126–127 reserved, or
   whether that band is a trigger-monitor display convention only.
8. Roland VAD706 / VAD716 / V71 / TD-07KV / TD-02K / TD-17KVX / TD-17KV2 note maps — not retrieved.
