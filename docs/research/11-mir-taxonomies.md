# Dossier 11 — MIR / ADT drum taxonomies as an external check on the KITWARP axes

Status: complete. Everything below is quoted or transcribed from the source named in
section 4. Anything not directly verified in a primary source is marked UNVERIFIED.

---

## 1. Scope and method

### 1.1 What was obtained

| Source | How obtained | Result |
|---|---|---|
| Magenta Groove MIDI Dataset (GMD) — TD-11 map + reduction table | `WebFetch` of `magenta.tensorflow.org/datasets/groove` | Full 22-row table, verbatim |
| GMD paper (Gillick et al., ICML 2019) | `curl` arXiv 1905.06118 + `pdftotext` | Rationale text + Appendix B counts |
| Magenta 9-class code table | `git clone magenta/magenta` -> `magenta/models/music_vae/data.py` | `ROLAND_DRUM_PITCH_CLASSES`, `FULL_DRUM_PITCH_CLASSES` |
| note-seq GM 9-class table | `git clone magenta/note-seq` -> `note_seq/drums_encoder_decoder.py` | `DEFAULT_DRUM_TYPE_PITCHES` |
| E-GMD pitch names + 3/8-hit maps | `magenta/models/onsets_frames_transcription/drum_mappings.py` | `GROOVE_PITCH_NAMES`, `HIT_MAPS` |
| E-GMD paper (Callender et al., 2020) | `curl` arXiv 2004.00188 + `pdftotext` | Table 1, Table 2 verbatim |
| ENST-Drums (Gillet & Richard, ISMIR 2006) | `WebFetch` archives.ismir.net PDF -> `pdftotext` | Table 2 (all 20 labels) verbatim |
| MDB Drums | `git clone CarlSouthall/MDBDrums` + paper PDF -> `pdftotext` | Table 1 verbatim + counted from annotation files |
| IDMT-SMT-Drums | `WebFetch` Fraunhofer IDMT dataset page | 3 classes, licence |
| ADTOF / A2MD / reduced-N maps | `git clone MZehren/ADTOF` -> `adtof/ressources/instrumentsMapping.py`, `adtof/config.py` | `MIDI_REDUCED_3..9`, `LABELS_5`, `ENST_MIDI`, `MDBS_MIDI`, `RBMA_MIDI_*` |
| Vogl et al. DAFx-18 3/8/18-class table | `curl` arXiv 1806.06676 + `pdftotext` | Table 1 verbatim + rationale |
| STAR Drums (Weber et al., TISMIR 2025) | `WebFetch` -> googleapis PDF -> `pdftotext` | Table 1 (dataset survey) and Table 4 (18/8/5/3) verbatim |
| AudioSet ontology | `git clone audioset/ontology` -> `ontology.json` | Full percussion sub-tree + descriptions |
| FSD50K vocabulary (200 classes) | mirrored `vocabulary.csv` via GitHub code search (`JinhuaLiang/LaD-ProtoNet`) | Percussion subset |
| Wu & Lerch, ISMIR 2016, drum playing technique | `curl` archives.ismir.net PDF | Table 1 + technique definitions |
| Prockup et al., ISMIR 2013 (MDLib) | `curl` archives.ismir.net/ismir2013/paper/000242.pdf | Table 1 + full factorial dataset design |
| PAL — Percussive Audio Lexicon v1.0 (Bell, 2015) | `curl` of the published PDF lexicon -> `pdftotext` | Full attribute tree + leaf descriptors for the axis-relevant branches |

### 1.2 What could NOT be obtained, and why

- **MIREX wiki task definitions** (`music-ir.org/mirex/wiki/2017:Drum_Transcription`,
  `.../2018:Drum_Transcription`, and `music-ir.org/mirex/abstracts/2018/RV1.pdf`) returned
  **HTTP 503** on every attempt. The MIREX class vocabulary is therefore reconstructed
  indirectly from (a) the MDB Drums repo's own `MIREX2017.md` (which documents only the
  track splits, not the classes) and (b) Vogl's DAFx-18 paper, whose 3/8/18 sets are the
  sets his MIREX submissions used. **Marked UNVERIFIED where it depends on this.**
- **RBMA13's 23-class label list**: the dataset repo is not publicly clonable
  (`git clone https://github.com/CPJKU/RBMA13` -> auth required). Only the 18-class
  *reduction* of RBMA is recoverable, from ADTOF's `RBMA_MIDI_18` and `RBMA_FULL_MIDI`.
  The count "23" is quoted from Vogl et al. 2018 §4.3. **The 23 raw labels are UNVERIFIED.**
- **RWC "up to 29 drum classes"**: count quoted from STAR Drums Table 1 only; the RWC
  drum annotation label list was not obtained. **UNVERIFIED.**
- **Herrera et al. (2002/2003) percussion taxonomy**: academia.edu returns 403. The
  9-class structure (5 membrane + 4 cymbal) is from a search-result summary only.
  **UNVERIFIED.**

---

## 2. The extracted label sets, exhaustively

### 2.1 Magenta Groove MIDI Dataset (GMD) — the worked example of lossy collapse

The GMD is recorded on a **Roland TD-11**. The published dataset page carries a 22-row
table. Columns are exactly as published: `Pitch | Roland Mapping | GM Mapping | Paper
Mapping | Frequency`. "Paper Mapping" is the reduction; "Frequency" is the count of that
pitch in the corpus.

| Pitch | Roland mapping | GM mapping | Paper mapping (reduced) | Frequency |
|---|---|---|---|---|
| 36 | Kick | Bass Drum 1 | Bass (36) | 88,067 |
| 38 | Snare (Head) | Acoustic Snare | Snare (38) | 102,787 |
| 40 | Snare (Rim) | Electric Snare | Snare (38) | 22,262 |
| 37 | Snare X-Stick | Side Stick | Snare (38) | 9,696 |
| 48 | Tom 1 | Hi-Mid Tom | High Tom (50) | 13,145 |
| 50 | Tom 1 (Rim) | High Tom | High Tom (50) | 1,561 |
| 45 | Tom 2 | Low Tom | Low-Mid Tom (47) | 3,935 |
| 47 | Tom 2 (Rim) | Low-Mid Tom | Low-Mid Tom (47) | 1,322 |
| 43 | Tom 3 (Head) | High Floor Tom | High Floor Tom (43) | 11,260 |
| 58 | Tom 3 (Rim) | Vibraslap | High Floor Tom (43) | 1,003 |
| 46 | HH Open (Bow) | Open Hi-Hat | Open Hi-Hat (46) | 3,905 |
| 26 | HH Open (Edge) | N/A | Open Hi-Hat (46) | 10,243 |
| 42 | HH Closed (Bow) | Closed Hi-Hat | Closed Hi-Hat (42) | 31,691 |
| 22 | HH Closed (Edge) | N/A | Closed Hi-Hat (42) | 34,764 |
| 44 | HH Pedal | Pedal Hi-Hat | Closed Hi-Hat (42) | 52,343 |
| 49 | Crash 1 (Bow) | Crash Cymbal 1 | Crash Cymbal (49) | 720 |
| 55 | Crash 1 (Edge) | Splash Cymbal | Crash Cymbal (49) | 5,567 |
| 57 | Crash 2 (Bow) | Crash Cymbal 2 | Crash Cymbal (49) | 1,832 |
| 52 | Crash 2 (Edge) | Chinese Cymbal | Crash Cymbal (49) | 1,046 |
| 51 | Ride (Bow) | Ride Cymbal 1 | Ride Cymbal (51) | 43,847 |
| 59 | Ride (Edge) | Ride Cymbal 2 | Ride Cymbal (51) | 2,220 |
| 53 | Ride (Bell) | Ride Bell | Ride Cymbal (51) | 5,567 |

**22 source distinctions -> 9 classes.** The code form of the reduction, verbatim from
`magenta/models/music_vae/data.py`:

```python
ROLAND_DRUM_PITCH_CLASSES = [
    [36],              # kick drum
    [38, 37, 40],      # snare drum
    [42, 22, 44],      # closed hi-hat
    [46, 26],          # open hi-hat
    [43, 58],          # low tom
    [47, 45],          # mid tom
    [50, 48],          # high tom
    [49, 52, 55, 57],  # crash cymbal
    [51, 53, 59]       # ride cymbal
]
```

**What the reduction destroys, by axis:**

| Distinction destroyed | KITWARP axis it belongs to | Count of merges |
|---|---|---|
| Snare head vs. rim(shot) vs. X-stick | zone + articulation | 3 -> 1 |
| Tom head vs. tom rim (x3 toms) | zone | 6 -> 3 |
| HH closed bow vs. closed edge | zone | 2 -> 1 (then folded further) |
| HH open bow vs. open edge | zone | 2 -> 1 |
| HH pedal vs. closed | articulation / limb / openness | folded into "closed" |
| Crash bow vs. edge (x2 crashes) | zone | 4 -> 1 |
| Crash 1 vs. Crash 2 | **instance** | 2 -> 1 |
| Ride bow vs. edge vs. bell | zone | 3 -> 1 |
| Tom 1 vs Tom 2 vs Tom 3 preserved | instance (as pitch ordinal) | kept |

Notably **the axis that survives intact is instrument + instance-for-toms**. Every zone
distinction and every articulation distinction is destroyed, and cymbal *instance* is
destroyed while tom *instance* is kept. That asymmetry is not principled — it is an
artefact of GM having three tom slots and only two crash slots.

**Authors' own words** (Gillick et al. 2019 §3.1):

> "While some nonpercussive instrument... captured by the electronic drum kit, including
> multiple sensors to detect hits on different parts of each drum, we make several
> preprocessing choices to simplify our models for this work. First, we map all drum hits
> to a smaller set of 9 canonical drum categories, following Roberts et al. (2018). These
> categories represent the most common instruments in standard drum kits: bass drum, snare
> drum, hi-hats, toms, and cymbals"

and, on the further loss from time quantisation:

> "Although this preprocessing step forces us to discard some of the subtle details of drum
> rolls that can be played on a single drum faster than 16th notes, we found that
> perceptually, much of the expressiveness in drumming can be conveyed at this resolution...
> One potential path forward in future work might be to supplement our data representation
> with an explicit token for a drum roll."

The rationale is explicitly **modelling convenience**, not a claim that the distinctions
are inaudible. The last sentence is an author-acknowledged regret: they want a
**roll/articulation token** back.

There is also a 61-class "full GM" list in the same file, which is simply one class per
GM pitch — a note-number pivot, i.e. exactly the thing dossier-0 already ruled out:

```python
FULL_DRUM_PITCH_CLASSES = [[p] for p in
 [36,35,38,27,28,31,32,33,34,37,39,40,56,65,66,75,85,42,44,54,68,69,70,71,73,78,80,
  46,67,72,74,79,81,45,29,41,61,64,84,48,47,60,63,77,86,87,50,30,43,62,76,83,49,55,
  57,58,51,52,53,59,82]]
```

And a separate 9-class table for *General MIDI* input (note-seq `DEFAULT_DRUM_TYPE_PITCHES`),
which merges e.g. side stick (37), hand clap (39), tambourine-ish, cowbell (56), timbales
(65,66), claves (75) and castanets (85) all into **snare**:

| Class | GM pitches merged |
|---|---|
| kick | 36, 35 |
| snare | 38, 27, 28, 31, 32, 33, 34, 37, 39, 40, 56, 65, 66, 75, 85 |
| closed hi-hat | 42, 44, 54, 68, 69, 70, 71, 73, 78, 80, 22 |
| open hi-hat | 46, 67, 72, 74, 79, 81, 26 |
| low tom | 45, 29, 41, 43, 61, 64, 84 |
| mid tom | 48, 47, 60, 63, 77, 86, 87 |
| high tom | 50, 30, 62, 76, 83 |
| crash | 49, 52, 55, 57, 58 |
| ride | 51, 53, 59, 82 |

Header comment, verbatim: *"This default list attempts to map all GM1 and GM2 drums onto
a much smaller standard drum kit based on drum sound and function."* — "sound and function"
is the merge criterion; note that cowbell -> snare and vibraslap -> crash are function-free.

### 2.2 Expanded Groove MIDI Dataset (E-GMD)

E-GMD extends GMD with 6 more pitches. The **28-entry** name table, verbatim from
`magenta/models/onsets_frames_transcription/drum_mappings.py` (`GROOVE_PITCH_NAMES`):

| Pitch | Name | | Pitch | Name |
|---|---|---|---|---|
| 36 | Kick | | 44 | HHPedal |
| 38 | Snare_Head | | 49 | Crash1_Bow |
| 40 | Snare_Rim | | 55 | Crash1_Edge |
| 37 | Snare_X-Stick | | 57 | Crash2_Bow |
| 48 | Tom1 | | 52 | Crash2_Edge |
| 50 | Tom1_Rim | | 51 | Ride_Bow |
| 45 | Tom2 | | 59 | Ride_Edge |
| 47 | Tom2_Rim | | 53 | Ride_Bell |
| 43 | Tom3_Head | | 39 | Clap |
| 58 | Tom3_Rim | | 54 | Tambourine |
| 46 | HHOpen_Bow | | 56 | Cowbell |
| 26 | HHOpen_Edge | | 70 | Maracas |
| 42 | HHClosed_Bow | | 64 | Low_Conga |
| 22 | HHClosed_Edge | | 75 | Claves |

The naming convention here is worth noting: every name is **`Instrument` + `_` + `Zone`**
(`Snare_Head`, `Snare_Rim`, `Ride_Bell`, `HHOpen_Bow`), or **`Instrument` + `Openness`**
(`HHOpen`, `HHClosed`, `HHPedal`), with instance carried as a numeral (`Tom1`, `Crash2`).
Google's own flat label set is a **string-concatenation of exactly the axes KITWARP
proposes**. It is a flattened product, not a genuinely flat vocabulary.

**E-GMD paper Table 2 (verbatim)** — the 7-hit and 3-hit maps:

| E-GMD hits | 7 hit | 3 hit |
|---|---|---|
| Kick drum | KD | KD |
| Snare drum, Snare rim, Cross-stick, Clap | SD | SD |
| Tom 1, Tom 1 Rim, Tom 2, Tom 2 Rim, Tom 3, Tom 3 Rim | TT | SD |
| Open Hi-Hat, Open Hi-Hat Bow, Closed Hi-Hat Bow, Pedal Hi-Hat | HH | HH |
| Tambourine, Crash 1 Bow, Crash 1 Edge, Crash 2 Bow, Crash 2 Edge | CY | HH |
| Ride Bow, Ride Edge, Ride Bell | RD | HH |
| Cow Bell | BE | HH |

**Discrepancy worth recording:** the *paper* defines a 7-hit map; the *shipped code*
(`HIT_MAPS` in `drum_mappings.py`) defines an **8-hit** map that adds an eighth class
`[75]  # Clave / Sticks` and moves Maracas(70) into HH and Low_Conga(64) into TT. The
released code also has a `3-hit` map that puts **all** cymbals, hats, tambourine and
maracas into one "hi-hats" class and all toms into "snare". So even within one project the
reduced vocabulary is unstable between publication and implementation — evidence that
these reduced sets are evaluation conveniences, not taxonomies.

Authors' own words (E-GMD §2/§3):

> "the set of drum hits is not standardized, with each dataset containing a varied
> collection of drum hits"

> "For evaluation and listening tests, we group the annotated hits down to a 7 and 3 hit
> classification task, as shown in Table 2."

The paper's own headline result is that F-measure over a reduced class set is a **poor
proxy for perceived quality**: a model scoring similarly on classification metrics produced
outputs judged better in listening tests once velocity was predicted. That is direct
published evidence that a coarse class vocabulary understates what listeners hear.

### 2.3 ENST-Drums (Gillet & Richard, ISMIR 2006) — 20 labels

Table 2 of the paper, verbatim and complete:

| Label | Description | | Label | Description |
|---|---|---|---|---|
| `bd` | Bass drum | | `lmt` | Low-mid tom |
| `sweep` | Brush sweep | | `mt` | Mid tom |
| `sticks` | Sticks hit together | | `mtr` | Mid tom, hit on the rim |
| `sd` | Snare drum | | `lt` | Low tom |
| `rs` | Rim shot | | `ltr` | Low tom, hit on the rim |
| `cs` | Cross stick | | `lft` | Lowest tom |
| `chh` | Hi-hat (closed) | | `rc` | Ride cymbal |
| `ohh` | Hi-hat (open) | | `ch` | Chinese ride cymbal |
| `cb` | Cowbell | | `cr` | Crash cymbal |
| `c` | Other cymbals | | `spl` | Splash cymbal |

**20 labels.** Structure of this label set, decomposed:

- instrument: bd, sd, lt/lmt/mt/lft, rc/ch/cr/spl/c, chh/ohh, cb
- **zone folded into label**: `mtr`, `ltr` (= tom, rim) — but only for two of the four toms
- **articulation folded into label**: `rs` (rim shot), `cs` (cross stick), `sweep` (brush sweep)
- **implement folded into label**: `sweep` (brushes), `sticks` (stick-on-stick)
- **openness folded into label**: `chh` vs `ohh` — a two-value collapse of a continuum
- **catch-all**: `c` ("Other cymbals") — an admission the instrument axis is under-specified

**The single most important structural fact about ENST-Drums for KITWARP:**
the cymbal labels carry a **separate instance number**, appended, not baked in. §2.4:

> "For events associated to cymbals, the number of the cymbal (cymbals are numbered from
> left to right, from the drummer's point of view, see figure 1) is also added. For example,
> `rc3` indicates a ride cymbal hit, the 3rd cymbal for this particular drummer."

This is an **independent, peer-reviewed precedent for a first-class `instance` axis**,
carried orthogonally to the instrument label, and defined **spatially** (left-to-right from
the player's seat) rather than as an arbitrary ordinal. It also means the same drummer's
`cr1` and `cr5` are different physical cymbals — exactly the "structured, not a bare
ordinal" requirement in the brief.

ENST also states that per sequence a drummer "used either **sticks, rods, brushes or
mallets**" — the **implement axis is a recording-session variable held constant per
sequence**, not encoded per event. So implement exists but sits at a different scope.

Concrete label variants actually seen in the corpus (from ADTOF's `ENST_MIDI`, which maps
the corpus's raw strings): `bd, cs, rs, sd, sd-, lft, chh, lt, ohh, lmt, mt, cr, c1, cr1,
cr5, rc, rc1, rc3, ch, ch1, ch5, spl, spl2, cb, cr2, c, c4, rc2, rc4, sticks` (plus `mtr`,
`ltr`, `sweep` which that map comments out). Note `sd-` — an unlisted variant, and the
instance suffixes going up to 5.

### 2.4 IDMT-SMT-Drums — 3 classes

Fraunhofer IDMT dataset page: **kick drum, snare drum, hi-hat**. 104 polyphonic drum
loops; 608 WAV files; ~2h10m; onsets manually annotated, delivered as XML and SVL.
Licence: **CC BY-NC-ND 4.0**.

The page gives **no rationale** for the restriction — the recordings simply contain only
those three instruments. This dataset is the reason the 3-class vocabulary became the field
default; it is a **property of one recording session**, not a taxonomic claim. E-GMD's
description confirms: *"IDMT-SMT contains only the 3 standard drum hits (KD, SN, HH)"*.

### 2.5 MDB Drums — the two-level taxonomy (this is the important one)

23 tracks from MedleyDB's MusicDelta subset; **7994 onsets**; **6 classes** / **21
subclasses**. Table 1 of Southall, Wu, Lerch & Hockman (ISMIR 2017 LBD), verbatim,
cross-checked against a count over the repo's `annotations/class/*.txt` and
`annotations/subclass/*.txt` (counts match exactly):

| Class | Subclass | Description | Onsets |
|---|---|---|---|
| KD | KD | kick drum | 1539 |
| SD | SD | snare drum | 1510 |
| SD | SDB | snare drum: brush | 332 |
| SD | SDD | snare drum: drag | 2 |
| SD | SDF | snare drum: flam | 11 |
| SD | SDG | snare drum: ghost note | 790 |
| SD | SDNS | snare drum: no snare | 9 |
| HH | CHH | closed hi-hat | 1847 |
| HH | OHH | open hi-hat | 269 |
| HH | PHH | pedal hi-hat | 523 |
| TT | HIT | high tom | 4 |
| TT | MHT | high-mid tom | 26 |
| TT | HFT | high floor tom | 14 |
| TT | LFT | low floor tom | 46 |
| CY | RDC | ride cymbal | 835 |
| CY | RDB | ride cymbal bell | 16 |
| CY | CRC | crash cymbal | 126 |
| CY | CHC | china cymbal | 15 |
| CY | SPC | splash cymbal | 10 |
| OT | SST | side stick | 38 |
| OT | TMB | tambourine | 32 |

Class-level totals (counted from the repo): SD 2654, HH 2639, KD 1539, CY 1002, TT 90, OT 70.

Authors' own words:

> "These onsets are divided into 6 classes based on drum instruments or 21 subclasses based
> on playing techniques."

> "this dataset includes the most commonly used drum classes (e.g., kick drum, snare drum
> and hi-hat) as well as additional drum classes (e.g., toms and cymbals) in conjunction
> with detailed categorisation for each class (e.g., flam, drag, and roll for snare drum),
> encouraging further ADT studies such as the detection of playing technique."

And on why they built it (§1):

> "as discussed in [4], most of the existing datasets only contain annotations of basic
> techniques (e.g., strikes, cross sticks, rim shots), and more detailed annotations on
> techniques such as flam, drag, and buzz rolls are missing."

**Analysis — MDB Drums does NOT cleanly separate the axes it claims to.** The paper says
subclass = "playing technique", but the actual subclass column is a mixture:

| Subclass | What it actually varies |
|---|---|
| SDB (brush) | **implement** |
| SDD (drag), SDF (flam) | **rudiment / multi-stroke articulation** |
| SDG (ghost note) | **dynamic level**, not technique |
| SDNS (no snare) | **instrument state / mechanism** (snares off) |
| CHH / OHH / PHH | **openness** (2 values) + **limb/pedal** (1 value), conflated |
| HIT / MHT / HFT / LFT | **instance** (which tom), not technique at all |
| RDC / RDB | **zone** (bow vs bell) |
| CRC / CHC / SPC | **instrument** (different cymbal types), not technique |
| SST | **articulation** (side stick) but placed in class "OT", not "SD" |
| TMB | **instrument** (auxiliary percussion) |

So the one published dataset that explicitly advertises a "drum type / stroke type" split
in fact has a level-2 that mixes **five** different axes: implement, rudiment, dynamic,
mechanism state, instance, zone, and plain instrument. And it commits a taxonomic error
KITWARP must avoid: `SST` (side stick) is a *snare* articulation but is filed under `OT`
(other percussion) because at class level it did not sound like the other SD onsets.

**Conclusion for KITWARP: MDB Drums is evidence FOR the axis decomposition — it is what
happens when you try to be two-level without naming your axes.** A single "subclass" slot
cannot hold implement, rudiment, dynamic, zone and instance simultaneously without exactly
this kind of incoherence.

Licence: **CC BY-NC-SA 4.0** (audio and annotations).

### 2.6 The standard 3 / 5 / 8 / 18-class ADT evaluation vocabularies, and where they come from

#### 2.6.1 Vogl, Widmer & Knees, DAFx-18 — the canonical source of 3/8/18

Table 1 of "Towards multi-instrument drum transcription" (arXiv 1806.06676), verbatim.
Caption: *"Classes used in the different drum instrument classification systems. Labels map
to General MIDI drum instruments: e.g. bass drum: 35, 36; side stick: 37; etc."*

| 3 | 8 | 18 | instrument name |
|---|---|---|---|
| BD | BD | BD | bass drum |
| SD | SD | SD | snare drum |
| | | SS | side stick |
| | | CLP | hand clap |
| | | HT | high tom |
| | TT | MT | mid tom |
| | | LT | low tom |
| | | CHH | closed hi-hat |
| HH | HH | PHH | pedal hi-hat |
| | | OHH | open hi-hat |
| | | TB | tambourine |
| | RD | RD | ride cymbal |
| | BE | RB | ride bell |
| | BE | CB | cowbell |
| | CY | CRC | crash cymbal |
| | CY | SPC | splash cymbal |
| | CY | CHC | Chinese cymbal |
| | CL | CL | clave/sticks |

Authors' own words:

> "The majority of works on ADT, especially the more recent ones, focus solely on
> transcribing three drum instrument (SD, BD, HH)"

> "...grouping different play styles like closed, opened, and pedal hi-hat strokes. In
> order to investigate ways of generating a model which is capable to transcribe more than
> these three instruments, two classification systems, i.e., a medium and a large one, for
> drum instruments of a standard drum kit are defined."

**The reason given for the small sets is data sparsity, explicitly, not perception:**

> "Given the nature of drum rhythms found in western popular music, another issue of ADT
> datasets is the uneven distribution of onsets between instrument classes... this often
> results in the trained models to never predict onsets for sparse classes. This is due to
> the number of potential false negatives being negligible, compared to the amount of false
> positives produced in the early stages of training... a loss function weighting cannot
> compensate for the problem in the case of very sparse classes."

And the errors the 18-class models actually make:

> "similar sounding instruments may get confused (BD/LT, CHH/PHH), instruments with energy
> over a wide frequency range mask more delicate instruments"

BD/LT and CHH/PHH confusions are *acoustic* confusions of a transcriber, not evidence that
the distinctions are unreal.

#### 2.6.2 STAR Drums (Weber et al., TISMIR 2025) — the current consolidation

Table 4, verbatim — the 18/8/5/3 nesting, cited by the authors to "Vogl et al. (2018) and
Zehren et al. (2023)":

| Class name | 18 | 8 | 5 | 3 |
|---|---|---|---|---|
| Bass drum | BD | BD | BD | BD |
| Snare drum | SD | SD | SD | SD |
| Side stick | SS | — | — | — |
| Hand clap | CLP | — | — | — |
| Closed hi-hat | CHH | HH | HH | HH |
| Pedal hi-hat | PHH | HH | HH | HH |
| Open hi-hat | OHH | HH | HH | HH |
| Tambourine | TB | — | — | — |
| Low tom | LT | TT | TT | — |
| Mid tom | MT | TT | TT | — |
| High tom | HT | TT | TT | — |
| Splash cymbal | SPC | CY | CY | — |
| Chinese cymbal | CHC | CY | CY | — |
| Crash cymbal | CRC | CY | CY | — |
| Ride cymbal | RD | RD | CY | — |
| Ride bell | RB | BE | CY | — |
| Cowbell | CB | BE | CY | — |
| Clave/sticks | CL | CL | — | — |

Table 1 of the same paper, the field's own census of dataset granularity:

| Dataset | Drums | # drum classes | Length (h) |
|---|---|---|---|
| RWC Music Database (Goto et al., 2002) | Rec. | 29 | 18.1 |
| ENST Drums (Gillet & Richard, 2006) | Rec. & Synth. | 20 | 1.0 |
| MDB Drums (Southall et al., 2017) | Rec. | 20 | 0.4 |
| RBMA13 (Vogl et al., 2017) | Rec. | 23 | 1.9 |
| TMIDT (Vogl et al., 2018) | Synth. | 18 | 257.1 |
| Slakh (Manilow et al., 2019) | Synth. | — (user-defined) | 118.3 |
| A2MD (Wei et al., 2021) | Rec. | 3 | 34.5 |
| ADTOF-RGW (Zehren et al., 2021) | Rec. | 5 | 89.2 |
| ADTOF-YT (Zehren et al., 2023) | Rec. | 5 | 202.2 |
| STAR Drums (proposed) | Synth. | 18 | 124.5 |

(STAR lists MDB Drums as 20, not the paper's own 21 — a transcription slip in the survey.
Use 21 from the primary source.)

Note the inverse relation: **the biggest datasets have the fewest classes.** ADTOF-YT is
202 hours at 5 classes; MDB Drums is 0.4 hours at 21. Granularity is being traded for scale.
Also note on the Slakh row, the authors' own remark:

> "In Slakh, no mapping from MIDI notes to drum classes is provided. Therefore, the number
> of supported classes depends on the mapping created by the user."

> "the MIDI notes associated with specific drum classes are inconsistent across the virtual
> drum kits used. Therefore, to use Slakh for ADT, users must create individual mapping
> tables from MIDI notes to drum classes for each drum kit."

That last sentence is a third-party, peer-reviewed statement of **the exact problem KITWARP
exists to solve**: virtual drum kits use inconsistent note layouts, so a per-kit mapping
table is mandatory. STAR Drums says it built 20 such tables by hand (one per kit).

STAR also states the mapping is not always 1:1 in either direction:

> "If the number of drum instruments of the virtual instrument does not match the class
> vocabulary described in Section 3.6, we summarize multiple instruments into one class or
> assign a single instrument to several classes."

A published acknowledgement that both **N->1 collapse** and **1->N expansion** are needed —
which is precisely the `expand` rule in `marty-615/drum-remap` that the brief mentions.

#### 2.6.3 ADTOF (Zehren et al.) — the 5-class set and the 3..9 ladder

From `adtof/config.py`:

```python
LABELS_5    = [35, 38, 47, 42, 49]
LABELS_5TXT = ["BD", "SD", "TT", "HH", "CY+RD"]
LABELS_3    = [35, 38, 42]
```

From `adtof/ressources/instrumentsMapping.py`, the full ladder with the authors' own
comments — this is the clearest published statement of *what gets split off at each step*:

| Set | Comment in source | What is added relative to the previous set |
|---|---|---|
| `MIDI_REDUCED_3` | "Std 3 classes ADT, we ignore the rest" | BD(35), SD(38), HH(42). Merges in: 36->35; 37,39,40->38; 44,46->42 |
| `MIDI_REDUCED_5` | "Adding TT and CY + RD" | TT(47) <- 41,43,45,47,48,50; CY(49) <- 49,51,52,53,55,57,59 |
| `MIDI_REDUCED_6` | "Splitting CY and RD" | RD(51) <- 51,53,59 |
| `MIDI_REDUCED_7` | "Splitting OH and CH" | OHH(46) split out of HH |
| `MIDI_REDUCED_8` | "Splitting floor tom and rack tom" | floor tom(41) <- 41,43 split out of TT |
| `MIDI_REDUCED_9` | "Adding percussion" | High Bongo(60); ~30 further GM percussion pitches listed but **commented out** |

The order in which distinctions are re-introduced as the budget grows is a **ranked
importance ordering** produced independently of KITWARP:

1. kick / snare / hi-hat (instrument)
2. toms, cymbals (instrument)
3. ride vs crash (instrument)
4. **open vs closed hi-hat (openness)**
5. **floor vs rack tom (instance)**
6. auxiliary percussion (instrument)

Zone (bow/edge/bell) and articulation (rimshot/cross-stick) **never appear at any level** —
in ADTOF they are merged into the parent from step 1 and never recovered.

ADTOF also carries mapping tables that are *themselves* evidence for the axes. The
`ar_modern_white_kit_full.nkm` table (Native Instruments Abbey Road Modern Drummer) is
mapped down to GM, and the comments preserve the original library's naming:

```
48: 57,  # Cymbal 1 (High Crash) Tip
49: 57,  # Cymbal 1 (High Crash) Edge
50: 57,  # Cymbal 1 (High Crash) Bell
51: 51,  # Cymbal 3 (Ride) Tip
52: 51,  # Cymbal 3 (Ride) Edge
53: 53,  # Cymbal 3 (Ride) Bell
76: 46,  # Hihat Open Quarter
77: 46,  # Hihat Open Half
78: 46,  # Hihat Open Three
79: 46,  # Hihat Open Loose
80: 46,  # Hihat Open Full
81: 38,  # Snare Drum 1, 2 & 3 Center Left Hand
83: 38,  # Snare Drum 1, 2 & 3 Center Right Hand
84: 38,  # Snare Drum 1, 2 & 3 Halfway Left Hand
64: 38,  # Snare Drum 1, 2 & 3 Wires Off
62: 38,  # Snare Drum 1, 2 & 3 Flam
63: 38,  # Snare Drum 1, 2 & 3 Roll
72: 37,  # Tom 4 (Floor Tom) Rim Only
```

Every one of KITWARP's proposed axes is present in that source layout and destroyed by the
GM mapping: **zone** (Tip/Edge/Bell, Center/Halfway, Rim Only), **openness as a 5-value
ordered scalar** (Quarter/Half/Three/Loose/Full), **limb** (Left Hand/Right Hand),
**mechanism state** (Wires Off), **articulation** (Flam, Roll, Choke), **instance**
(Cymbal 1/2/3/4/5, Snare 1,2&3, Tom 1-4). Five distinct openness levels collapse to one
pitch (46). Left/right hand collapses. This is a second, independent instance of the same
1320->1038 loss the KITWARP `.iom` measurement already found.

Licence: ADTOF repo **CC BY-NC-SA 4.0**.

#### 2.6.4 Other vocabularies carried in the same file

`RBMA_MIDI_18` (Vogl's RBMA13 reduction; 18 slots, index -> GM pitch, comments verbatim):
`0 BD(35), 1 SD(38), 2 side stick(37), 3 clap(39), 4 TT/lft(41), 5 lt(45), 6 hmt(48),
7 HH(42), 8 pedal hh(44), 9 open hh(46), 10 tamborine(54), 11 RD(51), 12 ride bell(53),
13 crash(49), 14 splash(55), 15 chinese(52), 16 cowbell(56), 17 click/sticks(75)`

`RBMA_MIDI_8` ("drums_m"): `BD(35), SD(38), TT(47), HH(42), CY(49), RD(51),
"ride bell/bells/etc"(53), "claves/sticks"(75)`.
`RBMA_MIDI_3` ("drums_3"): `35, 38, 42`.
`RBMA_FULL_MIDI` ("drums_f"): 47 entries, one per GM pitch 35-81 — again a note-number pivot.

`MDBS_MIDI` — MDB Drums' 21 subclass labels forced onto GM pitches, showing the collapse:
`KD->35; SD,SDB,SDD,SDF,SDG,SDNS ->38 (all six snare subclasses collapse to one pitch);
CHH->42; OHH->46; PHH->44; HIT->50; MHT->48; HFT->43; LFT->41; RDC->51; RDB->53; CRC->49;
CHC->52; SPC->55; SST->37; TMB->54`. Six technique subclasses -> one number. GM has no slot
for brush / drag / flam / ghost / snares-off.

**A2MD** (Wei et al., 2021): **3 classes** — kick drum, snare drum, hi-hat. Per STAR Drums:
*"This dataset supports three drum classes: kick drum, snare drum, [hi-hat]"*.

#### 2.6.5 MIREX drum transcription — UNVERIFIED

The MIREX wiki was unreachable (503) on every attempt. What is verified:

- MDB Drums was the MIREX 2017 drum transcription evaluation dataset; the repo's
  `MIREX2017.md` publishes only the 12/11-track train/test split (drum-only and full-mix
  versions of each, "resulting in 46 tracks in total"), **not** a class list.
- Vogl's MIREX 2017 and 2018 submission abstracts exist at
  `music-ir.org/mirex/abstracts/2017/RV1.pdf` and `.../2018/RV1.pdf` (503 at fetch time).
- A search-result summary (UNVERIFIED) reports MIREX subtasks **DTD** (drum transcription
  of drum-only recordings), **DTP** (percussion), **DTM** (in the presence of melodic
  instruments), a 50 ms onset tolerance, and that the 2018 task used three-fold CV on
  MIDI/RBMA/MEDLEY for an **eight-instrument-class** task.

**Conclusion (with the above caveat): MIREX did not invent a vocabulary. It evaluated on
Vogl's 3/8-class sets over MDB Drums and RBMA13.** There is no independent MIREX taxonomy
to check KITWARP against.

### 2.7 AudioSet ontology — the percussion branch, exhaustively

`git clone audioset/ontology`; 632 nodes total; licence **CC BY-SA 4.0** (Google/Dan Ellis).
Complete percussion sub-tree, with FSD50K membership and AudioSet's own restrictions field:

```
Percussion                     /m/0l14md    [in FSD50K]
├── Drum kit                   /m/02hnl     [in FSD50K]
│   └── Drum machine           /m/0cfdd
├── Drum                       /m/026t6     [in FSD50K]
│   ├── Snare drum             /m/06rvn     [in FSD50K]
│   │   ├── Rimshot            /m/03t3fj
│   │   └── Drum roll          /m/02k_mr
│   ├── Bass drum              /m/0bm02     [in FSD50K]
│   ├── Timpani                /m/011k_j
│   └── Tabla                  /m/01p970    [in FSD50K]
├── Cymbal                     /m/01qbl     [in FSD50K]
│   ├── Hi-hat                 /m/03qtq     [in FSD50K]
│   └── Crash cymbal           /m/0bm0k     [in FSD50K]  restrictions: blacklist
├── Cowbell                    /m/0239kh    [in FSD50K]
├── Wood block                 /m/01sm1g
├── Tambourine                 /m/07brj     [in FSD50K]
├── Rattle (instrument)        /m/05r5wn    [in FSD50K]
│   └── Maraca                 /m/0xzly
├── Gong                       /m/0mbct     [in FSD50K]
├── Tubular bells              /m/016622
└── Mallet percussion          /m/0j45pbj   [in FSD50K]
    ├── Marimba, xylophone     /m/0dwsp     [in FSD50K]
    ├── Glockenspiel           /m/0dwtp     [in FSD50K]
    ├── Vibraphone             /m/0dwt5
    └── Steelpan               /m/0l156b
```

**25 nodes for all of percussion.** Only 8 of them are drum-kit relevant
(Drum kit, Drum, Snare drum, Bass drum, Cymbal, Hi-hat, Crash cymbal, Cowbell), plus 2
technique nodes.

Three findings that matter to KITWARP:

1. **AudioSet does NOT separate the axes.** The only two non-instrument nodes in the whole
   percussion branch — `Rimshot` and `Drum roll` — are modelled as **children of Snare
   drum**, i.e. technique is expressed as a *subclass of an instrument*, not as a separate
   dimension. AudioSet's own descriptions confirm they are techniques, not instruments:
   - Rimshot: *"The sound of an accented snare drum beat produced by simultaneously hitting
     the rim and head of a drum with a drum stick."*
   - Drum roll: *"A sustained sound produced by multiple, rapid strikes between drum sticks
     and drum, made possible by bouncing alternating sticks off the head..."*
   Note "hitting the rim **and head**" — the rimshot definition is a *zone* statement, and
   the drum roll definition is a *rudiment* statement. Two different axes, both filed as
   children of one instrument node. In a hierarchy this immediately breaks: a rimshot on a
   *tom* has no node, and a drum roll on a *floor tom* has no node, because both are
   defined only under Snare drum.

2. **There is no zone axis at all.** No bow/edge/bell nodes; no hi-hat openness. `Hi-hat` is
   one leaf. `Crash cymbal` is the only cymbal sub-type and it is **blacklisted**
   (`"restrictions": ["blacklist"]`) — AudioSet's own quality process removed it.

3. **FSD50K dropped both technique nodes.** FSD50K's 200-class vocabulary
   (144 leaves + 56 intermediate nodes, drawn from the AudioSet ontology) contains
   16 percussion labels: `Percussion, Drum_kit, Drum, Snare_drum, Bass_drum, Tabla,
   Cymbal, Hi-hat, Crash_cymbal, Cowbell, Tambourine, Rattle_(instrument), Gong,
   Mallet_percussion, Marimba_and_xylophone, Glockenspiel`. **`Rimshot` and `Drum_roll` are
   absent**, as are `Timpani, Wood_block, Maraca, Tubular_bells, Vibraphone, Steelpan,
   Drum_machine`. So the only two technique-level nodes that any general audio ontology has
   ever defined were dropped the moment someone tried to collect enough labelled examples.

**Verdict: AudioSet/FSD50K is a negative control.** It shows what a drum taxonomy looks like
when it is built as a single is-a hierarchy by non-drummers for general audio tagging: 8
usable kit classes, zero zones, and two orphaned technique nodes that do not survive
contact with data. It is not a counter-model to KITWARP; it is a demonstration of why a
single hierarchy is the wrong shape.

### 2.8 Published work that DOES separate the axes

These are the sources that answer the brief's central question. All three are peer-reviewed
and were designed independently of each other and of KITWARP.

#### 2.8.1 Prockup, Schmidt, Scott & Kim, ISMIR 2013 — MDLib (the strongest confirmation)

"Toward Understanding Expressive Percussion Through Content Based Analysis". Abstract:

> "we present a system that seeks to classify different expressive articulation techniques
> **independent of percussion instrument**."

Method statement (§2, final paragraph):

> "we train classifiers to distinguish excitation techniques **independent of drum, stick
> height, intensity of stroke, and head strike position**."

Their dataset (§3) is a **full factorial over five named axes**:

| Axis | Values |
|---|---|
| instrument | snare drum, rack tom, floor tom (full set also bass drum, hi-hat, cymbals) |
| **stick heights** | 8 cm, 16 cm, 24 cm, 32 cm |
| **stroke intensities** | light, medium, heavy |
| **strike positions** | centre, halfway, edge |
| **articulations** | strike, rim shot, buzz stroke, cross stick |
| mechanism state | snares on / snares off ("snare wires both touching and not touching") |
| mic perspective | direct (attached) / indirect (room), mono and stereo |

1804 examples over 3 drums x 4 articulations, "at least 4 examples of each expressive
combination".

Their Table 1, "Excitation Techniques: There are four basic drum excitation techniques" —
note that each definition is **stated in terms of implement-part x contact-zone**:

| Articulation | Description (verbatim) |
|---|---|
| Strike | "The drumhead is struck with the tip of the stick." |
| Rim Shot | "Both the drumhead and rim are struck with the tip and shaft of the stick simultaneously." |
| Cross Stick | "The butt of the stick strikes the rim while the tip rests on the head." |
| Buzz Stroke | "The stick is pressed into the drum to create multiple, rapid strokes." |

This is a **direct, published decomposition into instrument x zone x implement-part x
gesture x dynamic**, with a stated design goal of making them independent, and a working
classifier that recognises articulation across instruments.

Their conceptual model (Figure 1) is: **Expression = f(Timing, Dynamics, Timbre)**, with
Articulation sitting inside Timbre. Timing and Dynamics are *performance* attributes;
Articulation/Timbre is an *identity* attribute. That maps cleanly onto KITWARP's split
between the pivot identity and per-event metadata.

#### 2.8.2 Wu & Lerch, ISMIR 2016 — technique detection, and the field's own dataset census

"On Drum Playing Technique Detection in Polyphonic Mixtures". Framing (§1):

> "the main focus of AMT systems for percussive instruments has been put on **recognizing
> the instrument types** (e.g., HiHat (HH), Snare Drum (SD), Bass Drum (BD)) and their
> corresponding onset times. Studies on retrieving the **playing techniques and
> expressions** are relatively sparse."

Rudiment taxonomy (§2), four families:

1. **Roll Rudiments**: drum rolls created by single or multiple bounce strokes (Buzz Roll).
2. **Paradiddle Rudiments**: a mixture of alternative single and double strokes.
3. **Flam Rudiments**: drum hits with one preceding grace note.
4. **Drag Rudiments**: drum hits with two preceding grace notes created by double stroke.

Plus, verbatim: *"There are also other playing techniques that are commonly used to create
timbral variations in a drum set, such as **Brush, Cross Stick, Rim Shot**, etc. Most drum
transcription systems, however, focus on single strikes instead of these playing techniques."*

Their Table 1 — the field's census of what technique annotation actually exists, verbatim:

| Dataset | Annotated techniques | Description | Total |
|---|---|---|---|
| Tindale et al. [15] | Strike, Rim Shot, Brush | 1 drum (snare), **5 strike positions (from centre to edge)** | 1264 clips |
| MDLib2.2 [16] | Strike, Rim Shot, Buzz Roll, Cross Stick | 9 drums, **4 stick heights, 3 stroke intensities, 3 strike positions** | 10624 clips |
| IDMT-Drum | Strike | 3 drums (snare, bass, hihat), 3 drum kits (real, waveDrum, technoDrum) | 560 clips |
| ENST Drums Minus One | Strike, Rim Shot, Brush, Cross Stick | 13 drums, 3 drum kits played by 3 drummers | 64 tracks |

Two of the four datasets are **explicit multi-axis cross-products**, and the paper's
"Description" column names the axes: *drums x stick heights x stroke intensities x strike
positions*, with technique as a separate column. This is the published field consensus on
how a drum sound is parameterised, and it is a 4-to-5-axis model.

Their own conclusion about the gap:

> "most of the datasets only contain annotations of playing techniques that are easily
> distinguishable from the normal strike (e.g., Cross Stick, Brush, Rim Shot). For playing
> techniques such as Flam, Drag and Buzz Roll, there are no datasets and annotations
> available."

I.e. the technique axis is under-annotated because it is *hard to detect from audio*, not
because it is unreal or unused.

#### 2.8.3 PAL — the Percussive Audio Lexicon (Bell, PhD, Swinburne/Victoria Univ., 2015)

The only published artefact found that is explicitly designed as a **percussion sound
ontology** rather than a note layout or an ADT evaluation set. PAL v1.0 is a released
document: ~2500 descriptors organised into three trees (Source, Sound, Subject) with an
alphanumeric ID scheme.

**Tree 1 (SOURCE) is a direct, independent statement of the KITWARP axes.** Full non-leaf
structure, extracted verbatim from the PDF:

```
T1  TREE 1: SOURCE
 T1.OB   OBJECT
  T1.OB.IN   INSTRUMENT NAME
   T1.OB.IN.AI  ACOUSTIC INSTRUMENT NAME
     .DM Drums, Membranes, Vessel Drums   .CP Cymbals, Plates, Gongs
     .BR Bars, Rods, Tubes, Tines, Slats  .BB Bells, Bowls
     .RS Rattles, Shakers                 .CL Clappers
     .SF Scrapers, Friction               .BL Blocks
     .FO Found Objects                    .HB Human Body
   T1.OB.IN.ED  ELECTRONIC DEVICE NAME    (.HW Hardware, .SW Software)
  T1.OB.MO   MORPHOLOGY  (SHAPE, SIZE, RANGE, MATERIALS)
 T1.EX   EXCITATION
  T1.EX.BE   BEATER/EXCITER
   T1.EX.BE.BT  BEATER TYPE
   T1.EX.BE.SP  SHAFT PROPERTIES  (Drumstick Size, Length, Shape, Thickness, Material)
   T1.EX.BE.TP  TIP PROPERTIES    (Number of Tips, Size, Hardness, Shape, Material, Mallet Core Material)
  T1.EX.EM   EXCITATION MODE
   T1.EX.EM.AR  ARTICULATION   (Stroke, Other Action, Damping, Modulation, Electronic Articulation)
   T1.EX.EM.PM  PLACEMENT      (per instrument family)
   T1.EX.EM.NO  NOTE/OCTAVE
   T1.EX.EM.DL  DYNAMIC LEVEL  (English, Italian, Expressive, Peak dBFS)
```

Mapped onto the brief's axis list:

| KITWARP axis (from brief) | PAL branch | Match |
|---|---|---|
| instrument | `T1.OB.IN` INSTRUMENT NAME | exact |
| instance | — | **absent from PAL** (PAL describes one sound, not a kit) |
| zone (tip/edge/bow/bell/rim/shell/head/centre) | `T1.EX.EM.PM` PLACEMENT | exact, and finer |
| articulation / technique | `T1.EX.EM.AR.ST` Stroke + `.OA` Other Action | exact |
| openness scalar | — | **absent as a named scalar**; expressed via `.DP` Damping |
| damping scalar | `T1.EX.EM.AR.DP` DAMPING | exact, 7 named values |
| beater / implement | `T1.EX.BE` BEATER/EXCITER (3 sub-axes) | exact, much finer |
| limb | partly `T1.EX.BE.BT.BC` (Human Body, Clothes) | partial |
| controller | `T1.EX.EM.AR.EA` Electronic Articulation | partial |
| (not in brief) dynamic level | `T1.EX.EM.DL` | **PAL treats dynamic as a first-class axis** |
| (not in brief) morphology (size/material/shape) | `T1.OB.MO` | **PAL treats these as identity, not metadata** |

**PAL's exhaustive leaf lists for the axis-relevant branches** (verbatim):

`T1.EX.EM.AR.ST` **STROKE** (23): Clap; Drag; Finger roll; Flam; Press roll; Rattle;
Rim click; Rim shot; Rub; Ruff; Scrape; Shake – body; Shake – handle; Single/double roll;
Slap; Stamp; Strike – beater shaft; Strike – beater tip; Strike + rub/scrape;
Strike - other; Sweep; Swish; Twist/rotate

`T1.EX.EM.AR.OA` **OTHER ACTION** (13): Break; Click; Drop; Flick; Kick; Press; Pull;
Punch; Push; Shoot; Smash; Snap; Stretch

`T1.EX.EM.AR.DP` **DAMPING** (7): No damping - open/rebound; Beater damping (non-striking);
Beater damping (striking); Body damping; Hand damping (non-striking); Hand damping
(striking); Choke/hold

`T1.EX.EM.AR.ML` **MODULATION** (5): Glissando; Portamento; Tremolo; Vibrato; Wah-wah

`T1.EX.EM.AR.EA` **ELECTRONIC ARTICULATION** (5): Strike - single attack;
Flam - double attack; Drag – triple attack; Ruff - quadruple attack; Roll

`T1.EX.EM.PM.DM` **PLACEMENT — Drums, Membranes** (verbatim tree):
```
1  Drum head/membrane:
   1.1 Batter/strike side:   1.1.1 Centre  1.1.2 Edge  1.1.3 Between centre/edge
   1.2 Bottom side:          1.2.1 Centre  1.2.2 Edge  1.2.3 Between centre/edge
2  Drum frame/shell:
   2.1 Rim   2.2 Rim + head   2.3 Shell (side)   2.4 Mounts/brackets   2.5 Air cavity
```

`T1.EX.EM.PM.CP` **PLACEMENT — Cymbals, Plates, Gongs** (verbatim tree):
```
1  Cymbal, Gong
   1.1 Beater-tip - top/front side:   1.1.1 Centre (bell, boss, dome)  1.1.2 Edge (rim)  1.1.3 Between centre/edge
   1.2 Beater-tip - bottom/rear side: 1.2.1 Centre (bell, boss, dome)  1.2.2 Edge (rim)  1.2.3 Between centre/edge
   1.3 Side-stick/shaft: 1.3.1 Centre (bell, boss, dome)  1.3.2 Between centre and edge
                         1.3.3 Edge: side-on, perpendicular
                         1.3.4 Edge: crash/glance, oblique
                         1.3.5 Edge: crash/glance, vertical
   1.4 Pair of cymbals struck together      1.5 Pair of gongs struck together
2  Plate  (same 3-way radial split, for beater-tip and side-stick/shaft)
```

`T1.EX.EM.PM.BB` **PLACEMENT — Bells** (relevant to cowbell/ride-bell modelling):
Crown (head); Shoulder; Waist (outer side); Sound bow (inner side); Rim (tip)

`T1.EX.BE.BT` **BEATER TYPE**, by family, exhaustive:
- `.IP` Idiophonic – Self-Sounding (1): Idiophonic
- `.SM` Sticks, Mallets, Rods (36): Bachi; Cipin/Tipper; Conga stick; Cowbell beater;
  Dagga; **Drumstick**; Hudak beaters; **Kick drum pedal beater**; Mallet – Bass Drum;
  Mallet – Cymbal; Mallet – Glockenspiel; Mallet – Gong; Mallet - Marimba;
  Mallet – Orchestral Chimes; Mallet - Steel Drum – alto/bass/tenor; Mallet - Surdo;
  Mallet - Tenor drum; Mallet – Timpani; Mallet – Vibraphone; Mallet – Xylophone;
  Mallet, generic; Metal bar, oblong; Metal pipe, hollow; Metal rod, cylindrical;
  Microphone beaters; Repenique stick; Singing Bowl beater; Tamborim beater; Tihli;
  Timbale stick; Triangle beater; Tubz™; Tupan beaters; Wooden stick
- `.BU` Bundled Rods (13): Acoustick™; Blasticks™; Broomstick™; **Brush**; Cajon brush;
  Dreadlocks™; Poly brush; Rods™; **Rute**; Smax™; Tala Wand™; Tam Brush™;
  Thai Bamboo cluster sticks
- `.FR` Friction (4): Bow; Cord/strap/thong; Scraper; Slider
- `.TI` Tools, Implements (16): Broom; Brush; Coin; Chain; Hammer; Knife; Knitting
  needle(s); Paddle; Pen, pencil; Ruler; Screwdriver; Spanner; Spoon; Switch; Thimble; Whip
- `.BC` Human Body, Clothes (14): Finger; Fingernail; Fingertip; Foot; Glove; **Hand**;
  Hand - fist; Hand - knuckle; Hand - palm - flat; Hand - palm - heel; Leg;
  Sandal/flip-flop; Shoe/boot; Steel tipped shoe/boot

`T1.EX.BE.TP.HN` **TIP HARDNESS** (3, ordered): Soft; Medium; Hard
`T1.EX.BE.TP.MA` **TIP MATERIAL** (17): Aluminium; Bamboo; Bone; Brass; Ceramic; Chamois;
Cotton; Felt; Foam/sponge; Leather; Plastic/nylon; Rubber/latex; Steel; Stone; Wood;
Wool - lambswool; Wool - yarn

`T1.EX.EM.DL.EN` **DYNAMIC LEVEL — English** (13, ordered): Very very quiet; Very quiet;
Quiet; Medium-quiet; Medium; Medium-loud; Loud; Very loud; Very very loud; With force;
Cannon-like; Increasing loudness; Decreasing loudness
`T1.EX.EM.DL.EX` **DYNAMIC LEVEL — Expressive** (10): Barely touching; Soft; Gentle; Light;
Muted; Hard; Heavy; Explosive; Thunderous; Varying

Licence: PAL v1.0 is `© Dr. Robert Bell, 2015`, published as a free PDF for use in tagging
sound libraries. **No open licence is stated** — treat as all-rights-reserved reference
material, cite but do not copy wholesale into a shipped product without permission.

---

## 3. Implications for the KITWARP pivot vocabulary

### 3.1 The headline answer to the brief's question

**Do any of these independently-designed taxonomies separate instrument from
stroke/technique from striking position? Yes — but only the ones that were designed by
percussionists to describe sounds, not the ones designed by MIR researchers to score
transcribers.**

| Source | Separates instrument from technique? | Separates striking position (zone)? | Separates implement? |
|---|---|---|---|
| PAL (Bell 2015) | **Yes, explicitly** (`T1.OB.IN` vs `T1.EX.EM.AR`) | **Yes**, `T1.EX.EM.PM`, per family, 3-way radial + side | **Yes**, 3 sub-axes (type/shaft/tip) |
| Prockup et al. 2013 (MDLib) | **Yes, explicitly** ("independent of percussion instrument") | **Yes**, centre/halfway/edge as a separate factor | implicit (sticks only) |
| Wu & Lerch 2016 census | **Yes** (technique column vs instrument column) | **Yes** ("3 strike positions", "5 strike positions") | **Yes** (brush vs stick) |
| Tindale et al. 2004 | Yes | **Yes**, 5 positions centre->edge | Yes (brush) |
| MDB Drums | claims to; in practice conflates 5 axes into one level | no (bow/edge absent; only RDC/RDB) | partly (SDB = brush) |
| ENST-Drums | no — flat labels, but **instance is separate** | no (baked into `mtr`/`ltr`) | no (session-level) |
| GMD / E-GMD | no — but names are literally `Instrument_Zone` strings | no (merged away) | no |
| Vogl 3/8/18, ADTOF 3-9, STAR, A2MD, IDMT | **no** | **no** | **no** |
| AudioSet / FSD50K | no — technique modelled as *child of* instrument | **no** | no |

**The MIR ADT evaluation vocabularies (3/5/8/18) are not taxonomies and should not be used
as one.** Vogl's own words give the reason: the sets exist because of *"the uneven
distribution of onsets between instrument classes"* causing models to *"never predict onsets
for sparse classes"*. They are class-imbalance mitigations. STAR Drums' 2025 census shows the
tradeoff undisguised: 202 h at 5 classes vs 0.4 h at 21.

### 3.2 Axis-by-axis verdict against the brief's list

| Axis in brief | Verdict from this dossier |
|---|---|
| **instrument** | **Confirmed universally.** Every source has it; it is the only axis all 12 sources agree on. |
| **instance (structured, not bare ordinal)** | **Confirmed, and refined.** ENST-Drums is a peer-reviewed precedent: cymbal instance is a *separate suffix* and is defined **spatially** ("numbered from left to right, from the drummer's point of view"). Prockup/MDLib has "9 drums" as a factor. GMD keeps tom instance but destroys cymbal instance — an incoherence KITWARP must not copy. Recommendation: treat instance as a structured record with an optional spatial/positional key, not `crash2`. |
| **zone** | **Confirmed, and the brief's list is subtly wrong.** PAL splits what KITWARP calls "zone" into **two independent things**: (a) *placement on the instrument* — batter side vs bottom side x {centre, between, edge}, plus rim / rim+head / shell / mounts / air cavity; and (b) *which part of the beater contacts* — `Strike – beater tip` vs `Strike – beater shaft`, and separately `Side-stick/shaft` placements for cymbals. In library layouts these appear fused ("tip"/"shank" for hi-hat, "bow"/"edge" for cymbal), but tip/shank is a **beater-part** fact and bow/edge is a **placement** fact. **Recommendation: split the brief's single `zone` axis into `contact_site` (on the instrument) and `contact_part` (of the implement).** Evidence: `HH Closed (Bow)` vs `HH Closed (Edge)` is placement, while Abbey Road's `Hihat Closed Tip` vs `Hihat Closed Shank` is beater-part, and both appear in real layouts. |
| **openness (ordered scalar with named anchors)** | **Confirmed as necessary, but NOT confirmed as universal in MIR.** No MIR taxonomy models it as a scalar; all use 2-3 discrete values (closed/open/pedal). But the Abbey Road layout in ADTOF's own tables has **five** ordered levels — `Hihat Open Quarter / Half / Three / Loose / Full` — plus `Hihat Closed Tight` as a sixth below `Closed`. ADTOF maps all five to 46. That is a 6-value ordered scalar in a shipping library, collapsed to 1 by the MIR vocabulary. The MIR sources therefore *refute nothing*; they simply never had the data. |
| **damping (ordered scalar)** | **Confirmed by PAL, with better values than the brief implies.** PAL's damping axis is **not a single scalar** — it is a 7-value enum crossing *what damps* (beater / hand / body / none) with *when* (striking vs non-striking) plus `Choke/hold`. "Hand damping (striking)" and "hand damping (non-striking)" are different sounds. **Recommendation: model damping as `{agent, phase}` or as an enum with those 7 anchors, not as a bare 0-1 scalar.** MDB Drums' `SDNS` (snares off) is a *different* thing again — mechanism state, not damping. |
| **beater / implement** | **Strongly confirmed, and the brief under-specifies it.** PAL gives implement three independent sub-axes: **beater type** (~84 named beaters across 6 families), **shaft properties** (size/length/shape/thickness/material), **tip properties** (number of tips, size, **hardness {soft, medium, hard}**, shape, material, mallet core material). ENST varies sticks/rods/brushes/mallets at session scope. MDB Drums has `SDB` = brush. Drum libraries expose exactly the PAL top level: sticks / rods / brushes / mallets / hands. **Recommendation: `implement` should carry at minimum `{family, tip_hardness}`; a bare enum of 5 will not round-trip libraries that expose felt vs wood beaters on kick, or nylon vs wood tips.** |
| **limb** | **Weakly confirmed.** Present in Abbey Road (`Left Hand` / `Right Hand` on snare, hats, toms) and in Rock Band/PhaseShift animation data (ADTOF `ANIMATIONS_MIDI`: `Floor Tom hit w/RH`, `Snare hit w/LH`, `Kick hit w/RF`). Present in PAL only obliquely via `T1.EX.BE.BT.BC` (Finger/Hand/Foot as beater). **Never present in any MIR class vocabulary** — Vogl's 18 classes have no limb, MDB has none. The evidence for limb is entirely from *layouts*, not from *taxonomies*: it is a round-robin/sample-selection device, and often not perceptually distinct. **Recommendation: keep limb, but rank it below zone/articulation; a target that lacks it should be able to drop it with no fallback penalty.** |
| **controller (first-class)** | **Confirmed only weakly and only for electronic sources.** PAL has `T1.EX.EM.AR.EA` Electronic Articulation, but its five values (single/double/triple/quadruple attack, roll) are *rudiments*, not CC data. The genuine evidence for a controller axis is the hi-hat pedal-position CC in TD/DTX modules, which no MIR taxonomy models at all (they all collapse pedal-HH into "closed"). **This dossier neither confirms nor refutes the controller axis. Marked UNVERIFIED from MIR sources.** |
| **role** | **Refuted again.** Zero of the twelve sources has anything resembling a `role` field. Prockup's Figure 1 places *timing* and *dynamics* outside timbre/articulation, i.e. as performance attributes of an event. Consistent with the brief's existing conclusion that `role` is event metadata, not identity. |

### 3.3 Axes these sources say KITWARP is MISSING

Three axes appear repeatedly in the external sources and are not in the brief's list:

1. **Dynamic level as an identity axis, not just a velocity number.**
   PAL makes `DYNAMIC LEVEL` a first-class attribute with 13 ordered English anchors and 10
   expressive ones. MDB Drums has `SDG` = **ghost note** as a *subclass*, i.e. a named
   dynamic band that changes the label. Prockup's MDLib has *stroke intensity*
   {light, medium, heavy} and *stick height* {8,16,24,32 cm} as **two separate** factors —
   height and intensity are not the same thing. Drum libraries expose the same split:
   articulations named "ghost", "soft", "accent", "rimshot hard".
   **Implication: some target layouts have a dedicated note for a dynamic band (a "ghost"
   articulation). If dynamic is only carried as velocity, KITWARP cannot map a source's
   `Snare Ghost` note onto a target's `Snare` + low velocity, nor the reverse. This needs at
   minimum a `dynamic_band` field with an ordered enum and a documented interaction with
   velocity.** This is the same shape as the `velocityDelta` in `marty-615/drum-remap`, but
   it should be an axis, not only a fallback annotation.

2. **Mechanism / device state, distinct from damping.**
   `snares off` appears in Prockup (snare wires touching / not touching), MDB Drums (`SDNS`),
   and the Abbey Road layout (`Snare Drum 1,2&3 Wires Off`). It is not damping (the snares
   are a resonating mechanism, not a mute), not zone, not articulation, and not implement.
   Similarly "muffled kick" / "dampened kick" appears in Abbey Road (`Kick Drum Dampened`,
   `Kick Half Open`). **Recommendation: a small `mechanism_state` axis, or explicitly fold
   `snares_off` into `damping` and document the decision.** Do not leave it to `articulation`,
   which is where MDB Drums put it and got an incoherent level-2.

3. **Multi-stroke / rudiment articulation as a distinct kind from single-stroke articulation.**
   Every technique-aware source separates these two groups. PAL splits `Stroke` into
   single-contact items (Slap, Rim shot, Rim click, Strike) and multi-contact items (Flam,
   Drag, Ruff, Press roll, Single/double roll, Finger roll), and gives Electronic
   Articulation its own 5-value ladder that is *purely* a count of attacks
   (single/double/triple/quadruple/roll). Wu & Lerch organise the whole field into four
   rudiment families. MDB Drums has SDD/SDF. Layouts have `Snare Flam`, `Snare Roll`.
   **Implication: a flam is a single MIDI note in a library and two notes in a performance.
   A pivot that treats `flam` as just another value of `articulation` will map a target's
   `Snare Flam` note to a source's two-note flam incorrectly, and vice versa. This is a
   1->N / N->1 case, and it is exactly what STAR Drums describes needing
   ("summarize multiple instruments into one class or assign a single instrument to several
   classes"). Recommend marking multi-stroke articulations with an explicit `attack_count`
   or `is_compound` flag so the expand/collapse rules can find them.**

### 3.4 Where these sources DISAGREE with the brief

Stated plainly, as the task asks:

1. **The MIR sources do not support an `instance` axis for anything except toms and cymbals,
   and they do not support it at all in the reduced vocabularies.** Only ENST-Drums has a
   real instance mechanism. If instance is going to be first-class in KITWARP, the
   justification comes from *layouts* (Superior Drummer's multiple snares/kicks), not from
   this dossier. This dossier gives it one supporting precedent, not consensus.

2. **No MIR taxonomy treats openness as ordered.** Every one uses closed/open/pedal as three
   unrelated labels. The ordered-scalar-with-anchors design is supported by *library layouts*
   (Abbey Road's 5-step ladder) and by physical reality, not by these taxonomies. Fine — but
   do not claim MIR consensus for it.

3. **`limb` has no support in any taxonomy here.** It is layout-only. Rank it accordingly.

4. **The brief's `zone` is one axis; PAL says it is two** (contact site on instrument vs
   contact part of implement). This is a genuine disagreement and PAL is the more careful
   source. See 3.2.

5. **The brief has no dynamic axis; three independent sources say it needs one.** See 3.3.1.

6. **Nothing here supports 170+ pivot keys as a *taxonomy* size.** The largest genuinely
   taxonomic drum-kit vocabularies found are: PAL Tree 1 SOURCE (unbounded, but factored),
   ENST 20 labels (+instance suffix), MDB 21, RBMA 23, RWC 29 (UNVERIFIED). The 80-key
   Superior Drummer requirement and the 170-key `lotkey` tree are *flattened products*, and
   this dossier explains why they are so much larger: they are enumerating
   `instrument x instance x zone x articulation x openness` as separate keys. **The right
   conclusion is not "beat 170 flat keys"; it is "a factored vocabulary of ~6-8 axes with
   10-40 values each generates far more than 170 combinations, and the flat count is an
   output, not a target."** PAL demonstrates exactly this: 39 attributes generating ~2500
   descriptors and an effectively unbounded combination space.

### 3.5 What the published evidence says listeners and transcribers actually distinguish

The brief asks for this specifically. Ranked by strength of evidence:

| Distinction | Evidence | Strength |
|---|---|---|
| kick / snare / hi-hat | universal in every source; the 3-class set | overwhelming (but circular — it is what everyone trains on) |
| toms vs snare vs cymbals | ADTOF step 3->5; Vogl 8-class; MDB 6-class | strong |
| ride vs crash | ADTOF `MIDI_REDUCED_6` "Splitting CY and RD"; Vogl 8-class | strong |
| open vs closed hi-hat | ADTOF `MIDI_REDUCED_7`; MDB CHH/OHH; Vogl 18-class | strong |
| floor tom vs rack tom | ADTOF `MIDI_REDUCED_8`; Vogl HT/MT/LT | strong |
| ride bell vs ride bow | MDB `RDB` vs `RDC`; Vogl `RB` vs `RD`; E-GMD `Ride_Bell` | strong (present in 3 independent annotations) |
| china / splash / crash as distinct cymbals | Vogl 18 (CHC/SPC/CRC); MDB (CHC/SPC/CRC); ENST (`ch`,`spl`,`cr`) | strong |
| side stick / cross stick vs normal snare | ENST `cs`; MDB `SST`; Vogl `SS`; E-GMD `Snare_X-Stick`; Prockup Table 1 | **very strong — 5 independent sources** |
| rim shot vs normal snare | ENST `rs`; PAL; Prockup; AudioSet `Rimshot`; Tindale; Wu&Lerch | **very strong — 6 independent sources** |
| brush vs stick | ENST `sweep`; MDB `SDB`; Tindale; Wu&Lerch; PAL `.BU` family | strong |
| strike position centre / halfway / edge on a drum head | Tindale (5 positions); Prockup (3); PAL (3 + sides) | strong, and **exclusively from the technique literature** |
| flam / drag / roll (multi-stroke) | MDB SDF/SDD; Wu&Lerch; PAL; Vic Firth rudiments | strong as a *musical* distinction; **explicitly noted as un-annotated in ADT datasets** |
| ghost note as a class | MDB `SDG` (790 onsets, 10 % of the corpus) | moderate; one source, but a large count |
| snares on / off | Prockup; MDB `SDNS`; layouts | moderate |
| bow vs edge on hi-hat / cymbal | E-GMD names; TD-11 hardware; **destroyed by every MIR reduction** | present in hardware and layouts; **no MIR taxonomy tests it** |
| pedal hi-hat vs closed hi-hat | MDB `PHH` (523 onsets); Vogl `PHH`; GMD 44 (52,343 hits — the 3rd most common pitch in GMD) | strong by count, but Vogl reports CHH/PHH as a top confusion for classifiers |
| left hand vs right hand | layouts only; zero taxonomies | weak |

Two things to draw from this table:

- **Rim shot, cross stick and strike position are the three best-attested non-instrument
  distinctions in the entire literature.** All three are exactly what the reduced ADT
  vocabularies delete first, and all three are *zone x implement-part x articulation*
  facts. This is direct support for KITWARP's decomposition.
- **The distinctions that hardware exposes and MIR deletes (bow/edge, openness gradations,
  bell) are deleted because the audio is hard, not because the MIDI is ambiguous.** KITWARP
  works on MIDI, where these arrive as unambiguous distinct notes. The MIR merge rationale
  therefore **does not transfer** to KITWARP, and should not be cited as precedent for
  merging.

### 3.6 One concrete anti-pattern to copy from, inverted

The GMD reduction table in §2.1 is the cleanest available worked example of the collapse
KITWARP must avoid. It is worth keeping the table itself as a **regression fixture**: any
KITWARP pivot must be able to represent all 22 TD-11 rows as 22 distinct pivot identities.
If a candidate pivot vocabulary collapses any two of those 22 rows, it has reproduced
Google's loss. The 22 rows exercise: instrument (7), instance (Tom1/2/3, Crash1/2),
zone (Head/Rim, Bow/Edge, Bell), articulation (X-Stick), openness (Open/Closed), and
limb-adjacent mechanism (Pedal). That is 6 of the brief's axes in one 22-row test case.

Similarly, the `ar_modern_white_kit_full.nkm` table in ADTOF (§2.6.3) is a 100-note layout
exercising 5-step openness, tip/shank, centre/halfway, left/right hand, wires-off, flam,
roll, choke and rim-only. It is a second fixture, and it is already in the cloned repo at
`repos/ADTOF/adtof/ressources/instrumentsMapping.py`.

---

## 4. Provenance

### 4.1 Cloned repositories (local paths)

Base: `scratch:repos/`

| Repo | Local path | Key files read | Licence |
|---|---|---|---|
| `magenta/magenta` | `repos/magenta/` | `magenta/models/music_vae/data.py` (L46-74); `magenta/models/onsets_frames_transcription/drum_mappings.py` | Apache-2.0 |
| `magenta/note-seq` | `repos/note-seq/` | `note_seq/drums_encoder_decoder.py` (L18-50) | Apache-2.0 |
| `MZehren/ADTOF` | `repos/ADTOF/` | `adtof/ressources/instrumentsMapping.py` (911 lines); `adtof/config.py` (L201-210) | CC BY-NC-SA 4.0 |
| `CarlSouthall/MDBDrums` | `repos/MDBDrums/` | `README.md`; `MIREX2017.md`; `MDB Drums/annotations/class/*.txt`; `.../subclass/*.txt` | CC BY-NC-SA 4.0 |
| `audioset/ontology` | `repos/audioset-ontology/` | `ontology.json` (632 nodes); `README.md` L49 | CC BY-SA 4.0 |
| `JinhuaLiang/LaD-ProtoNet` (FSD50K vocabulary mirror) | `repos/ladproto/` | `src/taxonomy/ground_truth/vocabulary.csv` (200 rows) | repo unlicensed; the vocabulary itself is FSD50K's, CC BY 4.0 |

Repos that could NOT be cloned: `CPJKU/RBMA13`, `edufonseca/FSD50K_baseline` — both required
GitHub auth (`fatal: could not read Username for 'https://github.com'`).

### 4.2 Documents fetched

| Document | URL | Local copy | Licence |
|---|---|---|---|
| Groove MIDI Dataset page (TD-11 table) | `https://magenta.tensorflow.org/datasets/groove` | — (WebFetch) | CC BY 4.0, Google LLC |
| Gillick et al., "Learning to Groove", ICML 2019 | `https://arxiv.org/pdf/1905.06118` | `scratchpad/groove.pdf`, `groove.txt` | arXiv, author-retained |
| Callender et al., E-GMD, 2020 | `https://arxiv.org/pdf/2004.00188` | `.../tool-results/webfetch-1788694408477-bpyjv9.pdf`, `scratchpad/egmd.txt` | arXiv; dataset CC BY 4.0 |
| Gillet & Richard, ENST-Drums, ISMIR 2006 | `https://archives.ismir.net/ismir2006/paper/000027.pdf` | `.../tool-results/webfetch-1788694200776-ug415w.pdf` | ISMIR archive, open |
| ENST-Drums project page | `https://perso.telecom-paristech.fr/grichard/ENST-drums/` (referenced, not fetched) | — | research-use-only, signed letter of engagement per §4 of paper |
| Southall, Wu, Lerch, Hockman, MDB Drums, ISMIR 2017 LBD | `https://musicinformatics.gatech.edu/wp-content_nondefault/uploads/2017/10/Wu-et-al_2017_MDB-Drums-An-Annotated-Subset-of-MedleyDB-for-Automatic-Drum-Transcription.pdf` | `.../tool-results/webfetch-1788694202819-zzgp4c.pdf` | paper CC BY 4.0 |
| Vogl, Widmer & Knees, "Towards multi-instrument drum transcription", DAFx-18 | `https://arxiv.org/pdf/1806.06676` | `.../tool-results/webfetch-1788694283481-nga82z.pdf` | arXiv |
| Weber et al., STAR Drums, TISMIR 2025 | `https://transactions.ismir.net/articles/10.5334/tismir.244` -> PDF `https://storage.googleapis.com/jnl-up-j-tismir-files/journals/1/articles/244/6888ab991b2f2.pdf` | `.../tool-results/webfetch-1788694361455-agwza8.pdf`, `scratchpad/star.txt` | TISMIR, CC BY 4.0 |
| Wu & Lerch, "On drum playing technique detection in polyphonic mixtures", ISMIR 2016 | `https://archives.ismir.net/ismir2016/paper/000268.pdf` | `scratchpad/wu2016.pdf` | CC BY 4.0 (stated on p.1) |
| Prockup, Schmidt, Scott & Kim, ISMIR 2013 | `https://archives.ismir.net/ismir2013/paper/000242.pdf` | `scratchpad/prockup2013.pdf`, `prockup.txt` | ISMIR 2013, © ISMIR |
| IDMT-SMT-Drums dataset page | `https://www.idmt.fraunhofer.de/en/publications/datasets/drums.html` | — (WebFetch) | dataset CC BY-NC-ND 4.0 |
| Bell, PAL v1.0 (Percussive Audio Lexicon) | `https://vucollaborate.vu.edu.au/d2l/common/viewFile.d2lfile/Database/ODI0ODEy/PERCUSSIVE%20AUDIO%20LEXICON.pdf?ou=6606&contextId=298536,27364` | `scratchpad/pal.pdf`, `pal.txt` | © Dr. Robert Bell, 2015 — **no open licence** |
| Bell, PAL PhD thesis (not fetched, referenced) | `https://researchbank.swinburne.edu.au/file/2738a422-a1a6-4d40-9f93-0ec799744a2c/1/Robert%20Bell%20Thesis.pdf` | — | Swinburne research bank |

### 4.3 Sources that returned errors

| URL | Error |
|---|---|
| `https://www.music-ir.org/mirex/wiki/2018:Drum_Transcription` | HTTP 503 |
| `https://www.music-ir.org/mirex/wiki/2017:Drum_Transcription` | HTTP 503 |
| `https://www.music-ir.org/mirex/abstracts/2018/RV1.pdf` | HTTP 503 |
| `https://www.academia.edu/1835692/Automatic_labeling_of_unpitched_percussion_sounds` | HTTP 403 |
| `https://github.com/CPJKU/RBMA13.git` (clone) | auth required |
| `https://github.com/edufonseca/FSD50K_baseline.git` (clone) | auth required |
| `https://archives.ismir.net/ismir2013/paper/000201.pdf`, `000107.pdf` | empty body (wrong paper IDs) |

### 4.4 Facts marked UNVERIFIED in this dossier

1. MIREX drum-transcription subtask names (DTD/DTP/DTM), the 50 ms tolerance, and the claim
   that MIREX 2018 ran an eight-class task — from search-result summaries only; the MIREX
   wiki was 503.
2. The RBMA13 raw 23-label list — only the 18-class reduction is verified.
3. RWC's "up to 29 drum classes" — from STAR Drums Table 1 only.
4. Herrera et al. (2002) "5 membrane + 4 cymbal" 9-class taxonomy — search summary only,
   academia.edu returned 403. Not used in any conclusion above.
5. PAL's total attribute count: sources give both "35 Attributes" and "39 Attributes" and
   both "~600 descriptors" and "over 2500 descriptors" — the discrepancy is between the
   thesis and the released lexicon. The **structure** quoted in §2.8.3 is verified directly
   from the PAL v1.0 PDF and is not affected.
