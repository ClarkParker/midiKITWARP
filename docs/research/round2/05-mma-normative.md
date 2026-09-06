# Round 2 · Bucket 05 — MMA and vendor normative MIDI documents

Scope: the MMA/AMEI Recommended Practices and the vendor specifications behind the GM1,
GM2, GS and XG percussion vocabularies; the MIDINameDocument DTD; DLS 1/2; SP-MIDI; MPE;
MIDI 2.0 per-note controllers; the MMA SysEx manufacturer-ID list as an identifier-
allocation precedent.

Purpose: dossier `docs/research/03-midi-standards.md` assembled a 184-sound union from
secondary transcriptions (Cakewalk `.ins` files in `jpcima/gm-xg-gs` and `pedrolcl/VMPK`)
and marked the result **UNVERIFIED against the paid primary specs**. This bucket went to
the normative documents, quotes them, and reports where the secondary tables are wrong.

**Headline finding about access.** Dossier 03 §5.2 says the GM1/GM2 specification PDFs
"require a MIDI Association membership" and that it is UNVERIFIED whether a free tier
grants download. That is true of `midi.org` and false of the standard as a whole.
**AMEI — the Association of Musical Electronics Industry, the Japanese body that co-issues
every MMA Recommended Practice — publishes the English-language RP PDFs free and
unauthenticated** at `https://amei.or.jp/midistandardcommittee/RP&CAj.html`. Every
document this bucket needed was obtained without payment or registration. Nothing in this
dossier rests on a paywalled restatement.

---

## 1. Candidate source register (round A)

Sixteen distinct searches were run before any extraction, varying register (standards-body,
vendor-service, notation-vendor, mobile-telephony, academic), language (English, German,
Japanese) and era (1991 GM1 → 2025 MIDI-CI profiles). The search budget for the session was
exhausted at 16; the remaining candidates were found by following links and by probing
vendor CDN URL patterns.

Authority levels: **N** = normative standard issued by MMA and/or AMEI; **V** = vendor's own
published documentation of its own format; **S** = secondary restatement; **X** = index or
metadata page.

### 1.1 MMA / AMEI standards

| # | Title | Body, year | Auth | Locator | Reached |
|---|---|---|---|---|---|
| 1 | The Complete MIDI 1.0 Detailed Specification, 3rd edition (contains **RP-003 / MMA0007 General MIDI System Level 1**, Table 3 GM Percussion Map, and the GM Level 1 Developer Guidelines) | MMA, doc v96.1, 3rd ed. 2014 | N | `https://freqsound.com/SIRA/MIDI%20Specification.pdf` (mirror of the MMA PDF; © 1995-2006, 2014 MMA) | **yes** |
| 2 | **General MIDI 2, Version 1.2a — RP-024** (incorporating RP-036, RP-037, RP-045) | MMA, 6 Feb 2007 | N | `https://amei.or.jp/midistandardcommittee/Recommended_Practice/e/GM2-v12a.pdf` | **yes** |
| 3 | General MIDI Level 2 — RP-024, original English release | MMA/AMEI, 1999 | N | `…/Recommended_Practice/e/rp24(e).pdf` | downloaded (2.2 MB) but **no extractable text layer**; superseded by #2 |
| 4 | GENERAL MIDI Level 2 Recommended Practice (RP024), Japanese | AMEI | N | `…/Recommended_Practice/GM2_japanese.pdf` | listed, not needed once #2 was in hand |
| 5 | **General MIDI Lite v1.0 — RP-033** | MMA/AMEI, 5 Oct 2001 | N | `…/Recommended_Practice/e/gml-v1.pdf` | **yes** |
| 6 | **Mobile Musical Interface Specification v1.0.2 — RP-048** (MMA version 197-102) | AMEI Active Ringtone WG, 10 Jul 2007 | N | `…/Recommended_Practice/e/rp48a(spec).pdf` | **yes** |
| 7 | Mobile Musical Interface v1.0.6 — RP-048/amd1 | AMEI, 30 Nov 2009 | N | `…/Recommended_Practice/e/rp48amd1.pdf` | **yes** (skimmed) |
| 8 | **Downloadable Sounds Level 1, v1.1a — RP-016** | MMA | N | `…/Recommended_Practice/e/dls1v11a.pdf` | **yes** |
| 9 | **Downloadable Sounds Level 2, v1.0a — RP-025** | MMA | N | `…/Recommended_Practice/e/dls2v10a.pdf` | **yes** |
| 10 | DLS 2.1 / 2.2 amendments — RP-025/amd1, amd2 | MMA | N | `…/e/rp25dls2amd1.pdf`, `…/e/dls2amd2(all)a(pub).pdf` | located, **not fetched** |
| 11 | **Scalable Polyphony MIDI, device profile v1.0a — RP-034 / RP-035** | MMA, Dec 2001 | N | `…/Recommended_Practice/e/sp-midi_all_v1a.pdf` | **yes** |
| 12 | **MIDI Polyphonic Expression v1.0 — RP-053** | MMA/AMEI, 12 Mar 2018 | N | `…/Recommended_Practice/e/rp053.pdf` (also `https://d30pueezughrda.cloudfront.net/campaigns/mpe/mpespec.pdf`) | **yes** |
| 13 | MPE Configuration RPN — CA-034 | MMA/AMEI | N | `…/Recommended_Practice/e/ca034.pdf` | located, not fetched |
| 14 | Specification for use of TRS Connectors with MIDI Devices — RP-054 | MMA/AMEI, 2018 | N | `…/Recommended_Practice/e/rp054.pdf` | **yes** — no percussion content, recorded so the next agent does not re-fetch it |
| 15 | **MIDI-CI Profile for Default Drum Note Map — M2-125-UM v1.0** | MMA + AMEI, published 2025-01-31 | N | page `https://midi.org/midi-ci-profile-for-default-drum-note-map`; PDF at `https://drive.google.com/uc?export=download&id=1Ee5OVXG7CAtv7mv6Va8c97rrWvllh0l0` | **yes** |
| 16 | **Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol v1.0 — M2-104-UM** | MMA/AMEI, 20 Feb 2020 | N | `https://amei.or.jp/midistandardcommittee/MIDI2.0/MIDI2.0-DOCS/M2-104-UM_v1-0_UMP_and_MIDI_2-0_Protocol_Specification.pdf` | **yes** |
| 17 | MIDI-CI and Common Rules for MIDI-CI Profiles | MMA/AMEI | N | AMEI MIDI2.0-DOCS directory | **not fetched** — needed only for negotiation mechanics |
| 18 | **MIDINameDocument DTD, version 1.0, 19 January 2003** | MMA | N | canonical URI `http://www.midi.org/dtds/MIDINameDocument10.dtd` **returns HTTP 404**; obtained from the mirror in `github.com/MichaelGJennings/midnamaker` → `dtd/MIDINameDocument10.dtd` (`git clone --depth 1`) | **yes** |
| 19 | MIDIEvents 1.0 DTD (`MIDIEvents10.dtd`), MIDIDeviceTypes DTD — referenced by #18 | MMA | N | same mirror | **yes** (present, not analysed) |
| 20 | **MMA SysEx ID Table** (assigned manufacturer SysEx IDs) | MMA | N | `https://midi.org/sysexidtable` | **yes** — 807 allocations parsed |
| 21 | AMEI MIDI Standards Committee RP/CA index | AMEI | X | `https://amei.or.jp/midistandardcommittee/RP&CAj.html` | **yes** — the key that unlocked #2, #5-#14 |
| 22 | midi.org `general-midi-2`, `general-midi-level-1` product pages | MMA | X | `https://midi.org/general-midi-2` etc. | reached in round 1; tables not public, PDFs gated |

### 1.2 Vendor documentation of the vendors' own formats

| # | Title | Vendor, year | Auth | Locator | Reached |
|---|---|---|---|---|---|
| 23 | **SC-8850 Owner's Manual** — contains "How to Use the Drum Set List" (p.44), Drum Set List (p.187 ff.), SC-88 Drum Set (1)-(3) (pp.208-210), SC-55 Drum Set (1)-(2) (pp.211-212), GM 2 Drum Set List (p.215) | Roland, 1999 | V | `https://cdn.roland.com/assets/media/pdf/SC-8850_OM.pdf` | **yes**, full text layer |
| 24 | **SC-88Pro Owner's Manual** — drum set list p.163 ff. | Roland, 1996 | V | `https://cdn.roland.com/assets/media/pdf/SC-88PRO_OM.pdf` | **yes**, full text layer |
| 25 | SC-88 Owner's Manual | Roland, 1994 | V | `https://cdn.roland.com/assets/media/pdf/SC-88_OM.pdf` | downloaded (8.4 MB) — **scanned images, no text layer**; unusable without OCR |
| 26 | SC-8820 Owner's Manual | Roland | V | `https://cdn.roland.com/assets/media/pdf/SC-8820_OM.pdf` | located, not fetched |
| 27 | SC-D70 Owner's Manual | Roland | V | `http://cdn.roland.com/assets/media/pdf/SC-D70_OM.pdf` | located, not fetched |
| 28 | SCB-55 Owner's Manual (SC-55 daughterboard; carries the GS drum map) | Roland | V | `https://cdn.roland.com/assets/media/pdf/SCB-55_OM.pdf` | located, not fetched |
| 29 | SC-55 / SC-55ST Owner's Manual | Roland, 1991 | V | ManualsLib `manualslib.com/manual/695759/…` | **not reached directly** — the SC-55 map was taken from #23 instead, where Roland reprints it |
| 30 | **MU100/MU100R TONE GENERATOR SOUND LIST & MIDI DATA** — XG Drum Map pp.101-105, TG300B Drum Map p.106, C/M Drum Map p.107 | Yamaha, 1997 | V | `https://usa.yamaha.com/files/download/other_assets/9/318079/MU100E2.pdf` | **yes**, full text layer |
| 31 | **PLG100-XG Data List** — XG Drum Map (Drum voice) pp.18-19; PLG100-XG is an XG-Level-1-only board, so its map *is* the XG Level 1 kit set | Yamaha | V | `https://data.yamaha.com/files/download/other_assets/8/318138/PLG100XGE.pdf` | **yes** |
| 32 | QY70 List Book (Japanese) — XGノーマルボイスリスト / XGドラムボイスリスト | Yamaha | V | `https://data.yamaha.com/files/download/other_assets/2/316562/QY70J3.PDF` | located, not fetched |
| 33 | B900 List Book (Japanese) — XG drum voice list | Yamaha | V | `https://data.yamaha.com/files/download/other_assets/8/316618/B900J2.pdf` | located, not fetched |
| 34 | Yamaha **XG Format Specification** (the developer document, as distinct from device data lists) | Yamaha | V | — | **NOT FOUND in public form.** See §6. |
| 35 | Roland **GS Format Specification** (the developer document) | Roland | V | — | **NOT FOUND in public form.** See §6. |

### 1.3 Secondary and contextual

| # | Title | Auth | Locator | Note |
|---|---|---|---|---|
| 36 | General MIDI PERCUSSION Key Map (PDF hosted by MuseScore) | S | `https://musescore.org/sites/musescore.org/files/General%20MIDI%20Standard%20Percussion%20Set%20Key%20Map.pdf` | not used; #1 supersedes it |
| 37 | General MIDI Level 2 Specification, third-party copy | S | `http://www.jososoft.dk/yamaha/pdf/gmlev2.pdf` | not used; #2 supersedes it |
| 38 | CMU `GMSpecs_PercMap.htm` — General MIDI Standards Table 2 Percussion Key Map | S | `https://www.cs.cmu.edu/~music/cmp/archives/cmsip/readings/GMSpecs_PercMap.htm` | not used |
| 39 | computermusicresource.com GM Percussion Key Map | S | `https://computermusicresource.com/GM.Percussion.KeyMap.html` | not used |
| 40 | Somascape — GM instrument and drum mapping | S | `http://www.somascape.org/midi/basic/gmins.html` | not used |
| 41 | Uni Hamburg TAMS, "GM — Der Standard" (German seminar page) | S | `https://tams.informatik.uni-hamburg.de/lehre/1999ws/proseminar/medien-audio/vortraege/generalmidi/p2.html` | German-register probe; adds nothing |
| 42 | IANA media type registration `audio/sp-midi` | N (registry) | `https://www.iana.org/assignments/media-types/audio/sp-midi` | context for #11 |
| 43 | `insolace/MIDI-Sysex-MFG-IDs` — tabularised MMA SysEx ID list | S | GitHub | not used; #20 is primary |
| 44 | digitalDrummer, "MIDI update promises smarter e-drum compatibility" (Aug 2026) | S | `https://digitaldrummermag.com/2026/08/04/…` | trade coverage of #15; confirms the profile's e-drum relevance |
| 45 | Wayback Machine (snapshots and CDX API) | X | `web.archive.org` | **UNREACHABLE.** Verified twice: `curl` on `http://web.archive.org/cdx/search/cdx?…` and on `http://web.archive.org/web/2015id_/…` both return `403` with the body `Blocked by egress policy`. A bare `HEAD` on `https://web.archive.org/web/2020/…` returns a `302` from the proxy with no body, which is easy to mistake for a working redirect — it is not. The brief's Wayback instructions cannot be followed in this environment. |
| 46 | archive.org itself (metadata API, full-text/advanced search) | X | `https://archive.org/advancedsearch.php?q=…&output=json` | **REACHABLE.** `https://archive.org/` returns 200 and `advancedsearch.php` returns well-formed JSON (`numFound: 371` for a `"general midi"` probe). This is the surviving archive route; Wayback is not. |

---

## 2. Extracted terminology (round B)

### 2.1 GM1 — the normative percussion key map, verbatim

Source: **The Complete MIDI 1.0 Detailed Specification, 3rd ed.**, section *General MIDI
System Level 1* (MMA0007 / RP003, © 1991, 1994 MMA), page 6, **Table 3**, headed
"General MIDI Percussion Map: (Channel 10)". Column heads are `MIDI Key` and `Drum Sound`.

| Key | Drum Sound | Key | Drum Sound | Key | Drum Sound |
|---|---|---|---|---|---|
| 35 | Acoustic Bass Drum | 51 | Ride Cymbal 1 | 67 | High Agogo |
| 36 | Bass Drum 1 | 52 | Chinese Cymbal | 68 | Low Agogo |
| 37 | Side Stick | 53 | Ride Bell | 69 | Cabasa |
| 38 | Acoustic Snare | 54 | Tambourine | 70 | Maracas |
| 39 | Hand Clap | 55 | Splash Cymbal | 71 | Short Whistle |
| 40 | Electric Snare | 56 | Cowbell | 72 | Long Whistle |
| 41 | Low Floor Tom | 57 | Crash Cymbal 2 | 73 | Short Guiro |
| 42 | **Closed Hi Hat** | 58 | **Vibraslap** | 74 | Long Guiro |
| 43 | High Floor Tom | 59 | Ride Cymbal 2 | 75 | Claves |
| 44 | **Pedal Hi-Hat** | 60 | **Hi Bongo** | 76 | Hi Wood Block |
| 45 | Low Tom | 61 | Low Bongo | 77 | Low Wood Block |
| 46 | **Open Hi-Hat** | 62 | Mute Hi Conga | 78 | Mute Cuica |
| 47 | Low-Mid Tom | 63 | Open Hi Conga | 79 | Open Cuica |
| 48 | **Hi Mid Tom** | 64 | Low Conga | 80 | Mute Triangle |
| 49 | Crash Cymbal 1 | 65 | High Timbale | 81 | Open Triangle |
| 50 | High Tom | 66 | Low Timbale | | |

Bold marks the six names where dossier 03 §2.1 differs. Supporting normative prose, same
document, page 2:

> A minimum of 47 preset percussion sounds conforming to the "GM Percussion Map" (see Table 3)

> Key-based Percussion is always on channel 10.

### 2.2 GM1 Developer Guidelines — note-off and mutual exclusion

Source: same document, *GM Level 1 Developer Guidelines – Second Revision*, pages 15-16.
These are the earliest MMA statements of two axes KITWARP models.

> **Response to Note-off on Channel 10 (Percussion)** — Only those two GM percussion
> sounds whose duration is most naturally under player control — long whistle and long
> Guiro — should respond to note-offs on Channel 10.

> **Mutually-Exclusive Percussion** — Two mutually-exclusive groups for drum sounds are
> recommended: open/pedal/closed hi-hat and open/mute triangle. Additional groups of
> mutually-exclusive drum sounds may be included as long as those groupings make sense
> musically.

> In order to support realism expectations, manufacturers set up certain groups of sounds
> in the percussion set to be mutually exclusive, so that playing a sound in the group
> cuts off any other previously-played sound in the group (as would naturally happen).

> GS, for example, mandates several mutually exclusive groups: high/low whistle,
> long/short Guiro, "open/mute" cuica, open/mute triangle, and open/pedal/closed hi-hat.
> (Another pair, open/mute surdo, uses sounds not included in the GM Percussion Map.)

And on vendor extension of the map, page 14:

> Extra drum sounds (additions or variations to the GM Percussion Map) should not be
> accessible while the device is in GM mode.

> Almost all devices use notes outside of the GM Percussion Map range to access additional
> sounds, but it is unclear if there is any consensus therein.

### 2.3 GM2 RP-024 v1.2a — Appendix B, the two columns dossier 03 does not have

Source: **General MIDI 2 v1.2a**, RP-024, MMA, 6 Feb 2007, **Appendix B: GM 2 Percussion
Sound Set**, pages 32-34. The table has *four* columns per set, not two: `NOTE#`,
`Inst.Name`, an `[EXC]` annotation, and `PAN`.

**The nine sets and their Program Changes** (spec's own one-based numbering; the footnote
says "the decimal value of PC #1 presented here (Standard Set) is equivalent to 00H"):

| Set | Spec PC# (1-based) | Wire value (0-based) |
|---|---|---|
| STANDARD | 1 | 0 |
| ROOM | 9 | 8 |
| POWER | 17 | 16 |
| ELECTRONIC | 25 | 24 |
| ANALOG | 26 | 25 |
| JAZZ | 33 | 32 |
| BRUSH | 41 | 40 |
| ORCHESTRA | 49 | 48 |
| SFX | 57 | 56 |

**Selection**, §3.3.1 and §2.4:

> A Rhythm Channel is a Channel that can select timbres from the GM2 Percussion Sound Set.
> These timbres are Programs in Bank 78H/xxH.

> Channel 10 defaults to a Rhythm Channel and Channel 11 defaults to a Melody Channel.

> Bank Select 78H/00H Program 1 (00H) corresponds to the GM1 Drum Set.

**The GM1 conformance clause**, §2.6 (this is the clause that makes GM2's Standard set an
authority for GM1's *notes* but not for GM1's *names*):

> Note numbers 35 – 81 (23H - 51H) in Program 1 of GM2 Rhythm Channel (Bank 78H/00H) shall
> conform to the GM1 Percussion Sound Set.

**Note-off**, §2.8.1:

> Note Off messages are ignored on Rhythm Channels, with the exception of the ORCHESTRA SET
> (specifically, Note number 88) and the SFX SET (Note numbers 47-84).

**The seven mutual-exclusion groups**, §2.8.1, reproduced exactly:

| Group | Standard Set | Analog Set | Orchestra Set | SFX Set |
|---|---|---|---|---|
| EXC1 | Closed HH (42) / Pedal HH (44) / Open HH (46) | Analog CHH 1 (42) / Analog CHH 2 (44) / Analog OHH (46) | Closed HH 2 (27) / Pedal HH (28) / Open HH 2 (29) | — |
| EXC2 | Short Whistle (71) / Long Whistle (72) | | | |
| EXC3 | Short Guiro (73) / Long Guiro (74) | | | |
| EXC4 | Mute Cuica (78) / Open Cuica (79) | | | |
| EXC5 | Mute Triangle (80) / Open Triangle (81) | | | |
| EXC6 | Mute Surdo (86) / Open Surdo (87) | | | |
| EXC7 | Scratch Push (29) / Scratch Pull (30) | | | Scratch Push (41) / Scratch Pull (42) |

**PAN, Standard Set, all 62 defined notes** (0-127, 64 = centre). This column does not
appear anywhere in dossier 03 and is normative recommended data:

| Note | Inst.Name | PAN | Note | Inst.Name | PAN |
|---|---|---:|---|---|---:|
| 27 | High Q | 49 | 58 | Vibra-slap | 29 |
| 28 | Slap | 49 | 59 | Ride Cymbal 2 | 44 |
| 29 | Scratch Push `[EXC7]` | 54 | 60 | High Bongo | 99 |
| 30 | Scratch Pull `[EXC7]` | 54 | 61 | Low Bongo | 99 |
| 31 | Sticks | 64 | 62 | Mute Hi Conga | 39 |
| 32 | Square Click | 54 | 63 | Open Hi Conga | 39 |
| 33 | Metronome Click | 64 | 64 | Low Conga | 44 |
| 34 | Metronome Bell | 64 | 65 | High Timbale | 84 |
| 35 | Acoustic Bass Drum | 64 | 66 | Low Timbale | 84 |
| 36 | Bass Drum 1 | 64 | 67 | High Agogo | 29 |
| 37 | Side Stick | 64 | 68 | Low Agogo | 29 |
| 38 | Acoustic Snare | 64 | 69 | Cabasa | 29 |
| 39 | Hand Clap | 54 | 70 | Maracas | 24 |
| 40 | Electric Snare | 64 | 71 | Short Whistle `[EXC2]` | 99 |
| 41 | Low Floor Tom | 34 | 72 | Long Whistle `[EXC2]` | 99 |
| 42 | Closed Hi-hat `[EXC1]` | 84 | 73 | Short Guiro `[EXC3]` | 94 |
| 43 | High Floor Tom | 46 | 74 | Long Guiro `[EXC3]` | 94 |
| 44 | Pedal Hi-hat `[EXC1]` | 84 | 75 | Claves | 84 |
| 45 | Low Tom | 58 | 76 | Hi Wood Block | 99 |
| 46 | Open Hi-hat `[EXC1]` | 84 | 77 | Low Wood Block | 99 |
| 47 | Low-Mid Tom | 70 | 78 | Mute Cuica `[EXC4]` | 44 |
| 48 | High Mid Tom | 82 | 79 | Open Cuica `[EXC4]` | 44 |
| 49 | Crash Cymbal 1 | 84 | 80 | Mute Triangle `[EXC5]` | 24 |
| 50 | High Tom | 94 | 81 | Open Triangle `[EXC5]` | 24 |
| 51 | Ride Cymbal 1 | 44 | 82 | Shaker | 94 |
| 52 | Chinese Cymbal | 44 | 83 | Jingle Bell | 99 |
| 53 | Ride Bell | 44 | 84 | Bell Tree | 104 |
| 54 | Tambourine | 74 | 85 | Castanets | 34 |
| 55 | Splash Cymbal | 54 | 86 | Mute Surdo `[EXC6]` | 44 |
| 56 | Cowbell | 84 | 87 | Open Surdo `[EXC6]` | 44 |
| 57 | Crash Cymbal 2 | 44 | 88 | `---` (all sets except ORCHESTRA) | — |

Table legend, verbatim: `---: Does not sound` · `@ : Use Standard Set Instrument` ·
`[EXC]: Instruments that have same EXC numbers do not sound simultaneously.`

### 2.4 MIDI-CI Profile for Default Drum Note Map, M2-125-UM v1.0 (2025)

The newest normative percussion document in the whole bucket, published 2025-01-31 by the
MIDI Association and AMEI. It is a MIDI 2.0 Profile, not a sound set: it fixes the
note→sound mapping and leaves timbre entirely open.

The note map (Table 5, pp.14-16) covers **27-88** and is GM2's Standard set with three
renamings (see §4.1). Its structural columns are `Mutually Exclusive Set`,
`Recommended Pan Position` (expressed as "Left 23%" / "Center" / "Right 32%" rather than
0-127) and a `Profile Details Discovery Bitmap` byte/bit per sound, so that a receiver can
report **which of the 62 sounds it actually has**.

Normative statements that bear directly on the KITWARP model:

> A Device is not required to be able to play all of the listed sounds and may include only
> a subset of the total list of sounds in the Drum Note Map.

> A Device may include extra sounds assigned to Note Numbers 0 through 26 and 89 through 127.

> **Sound Names: Undefined Tonal Quality** — The tonal qualities or properties of each sound
> is not defined. Each sound is defined in name only, although that name implies at least a
> musical role. A sound designer and/or device designer may freely decide what sound they
> will provide to best suit each of the named sounds. A Device may substitute a sound which
> is not identical to the name of the sound, if that sound is intended in context to fill a
> similar role to the named sound.

> Mutually Exclusive Sets (MES) … When any sound which belongs to any of the following
> Mutually Exclusive Sets (MES) starts to play, all other sounds in the same Mutually
> Exclusive Set shall be muted.
> • MES 1: Closed HH (42) / Pedal HH (44) / Open HH (46)
> • MES 2: Short Whistle (71) / Long Whistle (72)
> • MES 3: Short Guiro (73) / Long Guiro (74)
> • MES 4: Mute Cuica (78) / Open Cuica (79)
> • MES 5: Mute Triangle (80) / Open Triangle (81)
> • MES 6: Mute Surdo (86) / Open Surdo (87)
> • MES 7: Scratch Push (29) / Scratch Pull (30)

> In many Devices the Note Off message has no impact on the sound output for drum sounds.
> For most sounds, the Receiver should play the whole life cycle of the sound regardless of
> the timing of a Note Off message.

Per-note control the profile defines (§6.1, Table 8): **RPNC #7 Volume, #10 Pan, #71
Timbre/Harmonic Intensity, #72 Release Time, #73 Attack Time, #74 Brightness, #75 Decay
Time, #91 Reverb Send** — with MIDI 1.0 equivalents carried as *Key-Based Instrument
Controller* Universal SysEx `F0 7F <dev> 0A 01 0n kk [nn vv] … F7`. There is **no**
per-note controller for strike position, pedal position, damping or choke.

### 2.5 GM Lite RP-033 and RP-048 — two more MMA spellings of the same 47 sounds

**GM Lite v1.0** (RP-033, 5 Oct 2001), §3.4.2 *Rhythm Channel Sound Set*: notes 35-81 only,
with PAN and `[EXC1]`-`[EXC5]` — i.e. GM1's note range carrying GM2's names, PAN values and
exclusion groups. Its footnote defines EXC in the same words as GM2.

**RP-048 Mobile Musical Interface v1.0.2** (AMEI, 2007), §2.1.2, partitions the GM1 map
across four twelve-key phone-keypad sets:

> By defining four drum sets, each using the standard twelve keypad keys, all forty-seven
> instruments of the GM1 drum set are covered.

| Set | Members (RP-048's spellings) |
|---|---|
| **Drum Set 1** | Crash Cymbal 1, Splash Cymbal, Ride Cymbal 1, **Hi Tom**, **Low Mid Tom**, High Floor Tom, Acoustic Snare, Cowbell, Open Hi-Hat, Bass Drum 1, Side Stick, Closed Hi-Hat |
| **Drum Set 2** | Crash Cymbal 2, Chinese Cymbal, Ride Bell, **Hi Mid Tom**, Low Tom, Low Floor Tom, Electric Snare, Hand Clap, Ride Cymbal 2, Acoustic Bass Drum, (Reserved), Pedal Hi-Hat |
| **Percussion Set 1** | Claves, Cabasa, **VibraSlap**, Tambourine, Low Timbale, High Timbale, Maracas, **Hi Bongo**, Low Bongo, Mute Hi Conga, Open Hi Conga, Low Conga |
| **Percussion Set 2** | Short Guiro, Short Whistle, High Agogo, Long Guiro, Long Whistle, Low Agogo, Mute Cuica, Hi Wood Block, Mute Triangle, Open Cuica, Low Wood Block, Open Triangle |

This is the only MMA document that groups the GM1 vocabulary into *families* rather than by
note number. Its split is **kit vs hand-percussion**, and within hand-percussion it splits
**pitched-pair instruments** (bongo/conga/timbale, Percussion Set 1) from
**open/closed-pair and scraped instruments** (guiro/whistle/agogo/cuica/triangle/woodblock,
Percussion Set 2). That is a usable independent check on any family taxonomy KITWARP adopts.

### 2.6 Roland GS — from Roland's own manual, not a transcription

Source throughout: **Roland SC-8850 Owner's Manual** (`cdn.roland.com`), which reprints the
SC-55 and SC-88 maps for compatibility as well as the SC-8850's own.

Roland's own legend, "How to Use the Drum Set List", p.44 — the vocabulary of the notation:

| Token | Roland's definition, verbatim |
|---|---|
| `PC` | Drum Set number (Program number) |
| `Keys` | Note Number |
| `<-` | Same as the percussion sound of STANDARD 1 Set (PC1). |
| `---` | No sound |
| `[Pro]` | Same as the percussion sound of SC-88Pro |
| `[88]` | Same as the percussion sound of SC-88 |
| `[55]` | Same as the percussion sound of SC-55 |
| `[EXC]` | Percussion sound of the same number will not be heard at the same time. |
| `*` | Tones that are created using two voices |

**Drum-set Program Change numbers — the data dossier 03 §5.4 item 3 records as missing:**

| Map | Set | PC |
|---|---|---|
| SC-55 | STANDARD | 1 |
| SC-55 | ROOM | 9 |
| SC-55 | POWER | 17 |
| SC-55 | ELECTRONIC | 25 |
| SC-55 | TR-808 | 26 |
| SC-55 | JAZZ | 33 |
| SC-55 | BRUSH | 41 |
| SC-55 | ORCHESTRA | 49 |
| SC-55 | SFX | 57 |
| SC-55 | CM-64/32L | 128 |
| SC-88 | STANDARD 1 | 1 |
| SC-88 | STANDARD 2 | 2 |
| SC-88 | ROOM | 9 |
| SC-88 | POWER | 17 |
| SC-88 | ELECTRONIC | 25 |
| SC-88 | TR-808/909 | 26 |
| SC-88 | DANCE | 27 |
| SC-88 | JAZZ | 33 |
| SC-88 | BRUSH | 41 |
| SC-88 | ORCHESTRA | 49 |
| SC-88 | ETHNIC | 50 |
| SC-88 | KICK&SNARE | 51 |
| SC-88 | SFX | 57 |
| SC-88 | RHYTHM FX | 58 |

Roland's SC-55 table prints STANDARD and JAZZ as one column headed `PC 1 / PC 33`,
`STANDARD / JAZZ`, with slashed cells at notes 35-36 only (`Kick Drum2 / Jazz BD2`,
`Kick Drum1 / Jazz BD1`): JAZZ differs from STANDARD in exactly two notes.

Roland's own **GM 2 Drum Set List** (SC-8850 manual p.215) confirms the GM2 program numbers
independently of the MMA spec and states the vendor equivalences:

| GM2 PC | GM2 Name | SC-8850 Name |
|---|---|---|
| 1 | STANDARD | STANDARD 1 |
| 9 | ROOM | ROOM |
| 17 | POWER | POWER |
| 25 | ELECTRONIC | ELECTRONIC |
| 26 | **ANALOG** | **TR-808** |
| 33 | JAZZ | JAZZ |
| 41 | BRUSH | BRUSH |
| 49 | ORCHESTRA | ORCHESTRA |
| 57 | SFX | SFX |

**The GS articulation vocabulary that is axis-bearing** — all from the SC-8850 manual's own
set tables:

| Roland term | Physical meaning | Locator |
|---|---|---|
| `Ride Cymbal Inner` / `Ride Cymbal Edge` | radial contact site on the ride: bow-inner vs edge | SC-8850 Drum Set (6), PC 54 CYMBAL&CLAPS; also SC-8850 Drum Set tables at note 51/59 |
| `Ride Cymbal Low/Mid/High Inner`, `Ride Cymbal Low/Mid/High Edge` | six entries crossing Inner/Edge with a three-way Low/Mid/High. **UNVERIFIED** whether Low/Mid/High is pitch, size or dynamic — Roland does not say | PC 54 CYMBAL&CLAPS, notes 81-86 |
| `Ride Bell`, `Ride Cymbal Cup` (Yamaha's word) | the raised centre boss | SC-55 note 53; XG note 53 |
| `Half-Open Hi-Hat 1`, `Half-Open Hi-Hat 2` `[EXC1]` | the one genuine intermediate openness state Roland names | PC 54 CYMBAL&CLAPS, notes 48-50 |
| `Mute Crash Cymbal 1 [EXC3]`, `Mute Crash Cymbal 2 [EXC4]` | **the choke**, expressed as an exclusion group shared with `Crash Cymbal 1 [EXC3]` / `Crash Cymbal 2 [EXC4]` | PC 54 CYMBAL&CLAPS, notes 60/62 and 68/69 |
| `Concert BD 1 Mute [EXC1]` paired with `[55] Concert BD 1 [EXC1]` | mute/open pair on an orchestral bass drum | SC-8850 kick set |
| `Wadaiko` / `Wadaiko Rim`, `Djembe` / `Djembe Rim`, `Buk` / `Buk Rim`, `Jang-Gu Rim` | head vs rim as a named contrast on non-kit drums | SC-88 ETHNIC (PC 50); SC-8850 ASIA (PC 53) |
| `Kelontuk` / `Kelontuk Mute` / `Kelontuk Side` (all `[EXC1]`) | open / muted / side-struck, one instrument, one exclusion group | SC-8850 GAMELAN 1 (PC 55) |
| `Kopyak Open [EXC2]` / `Kopyak Mute [EXC2]`, `Sagat Open [EXC7]` / `Sagat Closed [EXC7]`, `Tang Gu [EXC4]` / `Tang Gu Mute [EXC4]`, `Jing p [EXC3]` / `Jing f [EXC3]` / `Jing Mute [EXC3]` | open/closed/mute pairs and triples bound by exclusion group | SC-8850 ASIA / GAMELAN sets |
| `Gengari p [EXC1]` / `Gengari Mute Low [EXC1]`, `Gengari f [EXC2]` / `Gengari Mute High [EXC2]`, `Jing p` / `Jing f` | **dynamic markings `p` and `f` inside the sound name** | SC-8850 ASIA (PC 53), notes 62-65, 70-72 |
| `Conga Slap`, `Conga Slide`, `Udo Slap`, `Timbales Paila`, `Cabasa Up` / `Cabasa Down` | stroke types and a directional scrape | SC-88 ETHNIC (PC 50) |
| `Bend Gong`, `Bend Talking Drum`, `Hu Yin Luo Low/Mid/Mid 2/High/High 2` (`[EXC5]`,`[EXC6]`) | pitch-bending struck idiophones and membranophones | SC-88 ETHNIC; SC-8850 ASIA |
| `Reverse …` (30+ entries) | time-reversed sample of another named sound | SC-88 RHYTHM FX (PC 58); SC-8850 CYMBAL&CLAPS |
| `[L]` / `[R]` prefixes and the `… L/R` set names (`STANDARD L/R`, `BRUSH 2 L/R`) | stereo-split kits addressing the left and right halves separately | SC-8850 Drum Set (1) and (5) |
| `[EXC8]` | an exclusion-group number **beyond the seven the MMA defines** | SC-8850 `STANDARD L/R`, note 102 `[L] Standard Closed Hi-Hat [EXC8]` |

**GS uses the whole 0-127 note range for drum sets.** SC-8850 drum-set pages carry the
footnote "About Notes 0-21, and 95-127, refer to p.199", and those pages place a full bank
of named kicks and snares (`[88] Standard 1 Kick 1`, `[55] Kick Drum 1`, `[Pro] TR-808 Kick 2`,
`[88] Power Kick 2`, …) on notes 0-21 and 95-127. Dossier 03 records the GS range as 25-108;
Roland's own document goes 0-127.

### 2.7 Yamaha XG — from Yamaha's own data lists

Sources: **Yamaha MU100/MU100R Sound List & MIDI Data** (`MU100E2.pdf`), *XG Drum Map*,
pp.101-105; and **Yamaha PLG100-XG Data List** (`PLG100XGE.pdf`), *XG Drum Map (Drum voice)*,
pp.18-19. The PLG100-XG is an XG-Level-1 board with no MU extensions, so its map is the
cleanest statement of XG Level 1 available.

Yamaha's table columns are `Note#`, `Note`, **`Rcv Note off`**, **`Alternate Group`**, then
one column per kit with an `E` (number of elements) sub-column.

**XG Level 1 drum kits, from the PLG100-XG Data List:**

| Bank MSB | Program# | Kit (PLG100-XG abbreviation) | MU100 full name |
|---|---|---|---|
| 127 | 1 | StandKit | Standard Kit |
| 127 | 2 | StndKit2 | Standard Kit 2 |
| 127 | 9 | Room Kit | Room Kit |
| 127 | 17 | Rock Kit | Rock Kit |
| 127 | 25 | ElctrKit | Electro Kit |
| 127 | 26 | AnalgKit | Analog Kit |
| 127 | **28** | **DanceKit** | **Dance Kit** |
| 127 | 33 | Jazz Kit | Jazz Kit |
| 127 | 41 | BrushKit | Brush Kit |
| 127 | 49 | **SymphKit** | **Symphony Kit** |
| 126 | 1 | SFXKit 1 | SFX Kit 1 |
| 126 | 2 | SFXKit 2 | SFX Kit 2 |

**Yamaha's Standard Kit, verbatim from the MU100 XG Drum Map** (bold = differs from dossier
03 §2.5; `KeyOff` = "O" in the *Rcv Note off* column; `AltGrp` = *Alternate Group*):

| Note | Name | KeyOff | AltGrp | Note | Name | KeyOff | AltGrp |
|---|---|:--:|:--:|---|---|:--:|:--:|
| 13 | Surdo Mute | | 3 | 49 | Crash Cymbal 1 | | |
| 14 | Surdo Open | | 3 | 50 | High Tom | | |
| 15 | Hi Q | | | 51 | Ride Cymbal 1 | | |
| 16 | Whip Slap | | | 52 | Chinese Cymbal | | |
| 17 | **Scratch H** | | 4 | 53 | Ride Cymbal Cup | | |
| 18 | **Scratch L** | | 4 | 54 | Tambourine | | |
| 19 | Finger Snap | | | 55 | Splash Cymbal | | |
| 20 | Click Noise | | | 56 | Cowbell | | |
| 21 | Metronome Click | | | 57 | Crash Cymbal 2 | | |
| 22 | Metronome Bell | | | 58 | Vibraslap | | |
| 23 | Seq Click L | | | 59 | Ride Cymbal 2 | | |
| 24 | Seq Click H | | | 60 | Bongo H | | |
| 25 | Brush Tap | | | 61 | Bongo L | | |
| 26 | **Brush Swirl** | O | | 62 | Conga H Mute | | |
| 27 | Brush Slap | | | 63 | Conga H Open | | |
| 28 | **Brush Tap Swirl** | O | | 64 | Conga L | | |
| 29 | Snare Roll | O | | 65 | Timbale H | | |
| 30 | Castanet | | | 66 | Timbale L | | |
| 31 | **Snare Soft** | | | 67 | Agogo H | | |
| 32 | Sticks | | | 68 | Agogo L | | |
| 33 | **Kick Soft** | | | 69 | Cabasa | | |
| 34 | Open Rim Shot | | | 70 | Maracas | | |
| 35 | **Kick Tight** | | | 71 | Samba Whistle H | O | |
| 36 | **Kick** | | | 72 | Samba Whistle L | O | |
| 37 | Side Stick | | | 73 | Guiro Short | | |
| 38 | **Snare** | | | 74 | Guiro Long | O | |
| 39 | Hand Clap | | | 75 | Claves | | |
| 40 | **Snare Tight** | | | 76 | Wood Block H | | |
| 41 | Floor Tom L | | | 77 | Wood Block L | | |
| 42 | Hi-Hat Closed | | 1 | 78 | Cuica Mute | | |
| 43 | Floor Tom H | | | 79 | Cuica Open | | |
| 44 | Hi-Hat Pedal | | 1 | 80 | Triangle Mute | | 2 |
| 45 | Low Tom | | | 81 | Triangle Open | | 2 |
| 46 | Hi-Hat Open | | 1 | 82 | Shaker | | |
| 47 | Mid Tom L | | | 83 | **Jingle Bells** | | |
| 48 | Mid Tom H | | | 84 | Bell Tree | | |

**Yamaha's four Alternate Groups** — narrower than Roland's seven and the MMA's seven:

| AltGrp | Members |
|---|---|
| 1 | Hi-Hat Closed (42) / Hi-Hat Pedal (44) / Hi-Hat Open (46) |
| 2 | Triangle Mute (80) / Triangle Open (81) |
| 3 | Surdo Mute (13) / Surdo Open (14) |
| 4 | Scratch H (17) / Scratch L (18) |

Yamaha does **not** group the whistles, guiros or cuicas, and instead marks Samba Whistle
H/L and Guiro Long as *Rcv Note off = O* — i.e. Yamaha models the long whistle and long
guiro as gated by note length rather than cut off by a sibling. **Six sounds receive note
off in XG: Brush Swirl (26), Brush Tap Swirl (28), Snare Roll (29), Samba Whistle H (71),
Samba Whistle L (72), Guiro Long (74).** All six are sustained, player-controlled-duration
articulations. That set is a normative statement of which percussion articulations are
*gestures with a duration* rather than one-shots.

Yamaha's Symphony Kit vocabulary (MU100 XG Drum Map): 35 `Gran Cassa`, 36 `Gran Cassa Mute`,
38 `Band Snare`, 40 `Band Snare 2`, 41-50 `Tom Jazz 1..6`, 49 `Hand Cymbal`,
51 `Hand Cymbal Short`, 57 `Hand Cymbal 2`, 59 `Hand Cymbal 2 Short`.

XG's per-note SysEx parameters (MU100 MIDI Data Format, NRPN table) — Yamaha exposes
per-drum-instrument edit of `Drum low pass filter cutoff`, `resonance`, `EG attack rate`,
`EG decay rate`, `pitch coarse`, `pitch fine`, `level`, `panpot`, each addressed by
`rr: drum instrument note number`. This is the 1990s ancestor of the MIDI 2.0 Registered
Per-Note Controllers in §2.4 — and, like them, it carries no strike-position parameter.

### 2.8 MIDINameDocument DTD — the interchange format's whole vocabulary

MMA DTD version 1.0, 19 January 2003. Formal Public Identifier
`-//MIDI Manufacturers Association//DTD MIDINameDocument 1.0//EN`; declared URI
`http://www.midi.org/dtds/MIDINameDocument10.dtd` — **which now returns HTTP 404**. Every
`.midnam` file in the wild carries a `DOCTYPE` pointing at a dead URL.

Complete element list, with the percussion-relevant declarations verbatim:

```
<!ENTITY % namelist "PatchNameList | NoteNameList | ControlNameList | ValueNameList">
<!ENTITY % noteorctl_listorref "(NoteNameList | UsesNoteNameList)?, (ControlNameList |
                                UsesControlNameList)?">

<!ELEMENT MIDINameDocument (Author, (MasterDeviceNames+ | ExtendingDeviceNames+ |
                            StandardDeviceMode+)) >
<!ELEMENT MasterDeviceNames (((Manufacturer, Model+) | Device),
                            (CustomDeviceMode | SupportsStandardDeviceMode)+,
                            ChannelNameSet*, (%namelist;)*) >
<!ELEMENT ChannelNameSet (AvailableForChannels, %noteorctl_listorref;, PatchBank+) >
<!ELEMENT PatchBank (MIDICommands?, (UsesPatchNameList | PatchNameList))>
<!ELEMENT Patch (PatchMIDICommands?, ChannelNameSetAssignments?, %noteorctl_listorref; ) >

<!ELEMENT NoteNameList (NoteGroup | Note)+>
<!ATTLIST NoteNameList  Name CDATA #IMPLIED>
<!ELEMENT NoteGroup (Note*)>
<!ATTLIST NoteGroup     Name CDATA #IMPLIED>
<!ELEMENT Note EMPTY>
<!ATTLIST Note
                Number  NMTOKEN #REQUIRED
                Name    CDATA   #REQUIRED>

<!ELEMENT Control (Values?)>
<!ATTLIST Control
                Type    (7bit | 14bit | RPN | NRPN) "7bit"
                Number  NMTOKEN                     #REQUIRED
                Name    CDATA                       #REQUIRED>
<!ELEMENT Values (ValueNameList | UsesValueNameList)?>
<!ATTLIST Values
                Min NMTOKEN #REQUIRED  Max NMTOKEN #REQUIRED
                Default NMTOKEN #IMPLIED  Units NMTOKEN #IMPLIED
                Mapping NMTOKEN #IMPLIED>
```

Full element inventory: `MIDINameDocument`, `Author`, `MasterDeviceNames`,
`ExtendingDeviceNames`, `Manufacturer`, `Model`, `Device`, `StandardDeviceMode`,
`CustomDeviceMode`, `DeviceModeEnable`, `DeviceModeDisable`, `SupportsStandardDeviceMode`,
`ChannelNameSetAssignments`, `ChannelNameSetAssign`, `ChannelNameSet`,
`AvailableForChannels`, `AvailableChannel`, `PatchBank`, `UsesPatchNameList`,
`PatchNameList`, `Patch`, `UsesNoteNameList`, `NoteNameList`, `NoteGroup`, `Note`,
`UsesControlNameList`, `ControlNameList`, `Control`, `Values`, `UsesValueNameList`,
`ValueNameList`, `Value`, `MIDICommands`, `PatchMIDICommands`, `MIDIDelay` — 35 elements,
plus the MIDI channel messages pulled in from `MIDIEvents10.dtd`.

**The decisive fact: a `<Note>` has exactly two attributes, `Number` and `Name`.** There is
no attribute for instrument, articulation, site, technique, exclusion group, pan, alternate
group, note-off behaviour, or anything else. `NoteGroup` provides exactly one optional level
of grouping, by free-text name. The industry's only cross-DAW percussion-naming interchange
format — read by Pro Tools, Logic, Digital Performer, Ardour — is a flat `int → string` map
with one grouping level and no schema for what the string means.

### 2.9 MPE, MIDI 2.0 and DLS — the controller-level vocabulary

**MPE RP-053 v1.0, §3.3.5 Timbre Control** — the only place in the whole MMA corpus where a
percussion *strike position* is normatively named:

> If a device offers a third dimension of control it will use Control Change #74 and
> typically control timbre. … **Initial-position.** The value of CC #74 at Note On encodes
> the initial position of a user's interaction with the instrument. An example of an
> Initial-position controller would be a digital hi-hat, in which CC #74 might encode the
> radius of the striking position, from bell to rim. **Initial-64.** The control pertains to
> a dimension that may be varied once a note has been struck. The initial position of CC #74
> under such circumstances must be 40h (64 decimal), such that movement can follow in either
> a positive or negative direction.

And, on hand drums, §3.3.4:

> Not all controllers can be expected to behave in this way. In the simulation of certain
> hand drums, for example, pressure applied to the drum skin is adjustable independently
> from the note creation mechanism.

**MIDI 2.0 M2-104-UM v1.0, Appendix A Table 11, Registered Per-Note Controllers** — the
complete defined list: 1 Modulation, 2 Breath, 3 Pitch 7.25, 4-6 Reserved, 7 Volume,
8 Balance, 9 Reserved, 10 Pan, 11 Expression, 12-69 Reserved, 70 Sound Controller 1
(Sound Variation), 71 Sound Controller 2 (Timbre/Harmonic Intensity), 72 Sound Controller 3
(Release Time), 73 Sound Controller 4 (Attack Time), **74 Sound Controller 5 (Brightness)**,
75 Sound Controller 6 (Decay Time), 76-78 Vibrato Rate/Depth/Delay, 79 Sound Controller 10
(Undefined), 80-90 Reserved. Note attribute type 0x03 is `Pitch 7.25`.

**DLS Level 2 v1.0a** — the file-format expression of mutual exclusion, `<rgnh-ck>` field
`usKeyGroup`:

> Specifies the key group for a drum instrument. Key group values allow multiple regions
> within a drum instrument to belong to the same "key group." If a synthesis engine is
> instructed to play a note with a key group setting and any other notes are currently
> playing with this same key group, the synthesis engine should turn off all notes with the
> same key group value as soon as possible. Valid values are: 0 No Key group; 1-15 Key
> groups 1 to 15.

> The second form of note exclusivity is useful for drums and sound effects. Each region can
> be assigned a Key Group. … As an example, this can be used to create mutually exclusive
> Open, Closed and Pedal High Hat sounds for a drum group.

DLS also carries `RangeVelocity` per region — velocity layering is in the format — and
`F_INSTRUMENT_DRUMS` (`ulBank` bit 31 / `0x80000000`) as the drum/melodic discriminator, with
drums "restricted to MIDI channel 10". Neither DLS level names a single percussion
articulation; they name the *mechanisms* (key group, velocity range, layer) and leave every
sound unnamed.

**SP-MIDI RP-034/035** — polyphony scaling and channel priority only; no percussion
vocabulary. Recorded so it is not re-fetched.

### 2.10 MMA SysEx manufacturer-ID list, as an identifier-allocation precedent

`https://midi.org/sysexidtable`, parsed: **807 allocations**. Structure:

- Single-byte IDs `01H`-`3FH`, allocated to North American and European manufacturers.
- `40H to 7FH` block: the table itself carries the row
  `40H to 5FH | [Assigned by AMEI for Japanese Manufacturers]` and
  `60H to 7FH | [Reserved for Other Uses]`.
- `00H` carries the row `[Used for ID Extensions]`; the three-byte extended space is then
  regionally partitioned by second byte: `00H 00H` / `00H 01H` (American), `00H 20H` /
  `00H 21H` / `00H 22H` (European & Asian), `00H 40H` / `00H 48H` (Japanese/AMEI).
- 86 single-byte rows, 721 three-byte rows.

Precedent that matters for ADR-0003 ("identifiers are forever"): the table contains **no**
row marked vacant, withdrawn, reassigned or reused. Companies that have not existed for
thirty years still hold their IDs — `01H Sequential Circuits`, `02H IDP`, `05H Passport
Designs`. Exactly **three** rows in the whole extended space read `Reserved`
(`00H 00H 2CH`, `00H 00H 36H`, `00H 00H 5DH`), which is consistent with slots pulled out of
service and never re-issued. **UNVERIFIED:** the page states no allocation or reclamation
policy in words, so "never reassigned" is an inference from the table's contents, not a
quoted rule.

---

## 3. Axis mapping

### 3.1 Terms that map cleanly onto an existing axis

| Source term | Source | KITWARP axis | Value |
|---|---|---|---|
| `Closed Hi-hat` / `Half-Open Hi-Hat 1`,`2` / `Open Hi-hat` | GM1/GM2/GS/XG; Roland SC-8850 PC54 | `openness` | `closed` / `half` / `open` |
| `Pedal Hi-hat` / `Hi-Hat Pedal` | GM1/GM2/GS/XG | `technique` | `chick` |
| `Side Stick` | GM1 Table 3 | `technique` | `sidestick` |
| `Open Rim Shot` (XG 34), `808 Rim Shot`, `Analog Rim Shot`, `CM Rim Shot`, `SD Rock Rim` | XG, GM2 ANALOG, GS | `technique` | `rimshot` |
| `Ride Bell` (GM1 53), `Ride Cymbal Cup` (XG 53) | GM1, XG | `site` | `bell` |
| `Ride Cymbal Inner` | Roland SC-8850 PC54 | `site` | `bow` |
| `Ride Cymbal Edge` | Roland SC-8850 PC54 | `site` | `edge` |
| `Mute Crash Cymbal 1/2` | Roland SC-8850 PC54 | `damping` = `muted` **plus** `relations.choke` — the `[EXC3]`/`[EXC4]` pairing with the ringing crash is exactly KITWARP's `choke` relation |
| `Mute Hi Conga` / `Open Hi Conga`; `Conga H Mute` / `Conga H Open` | GM1, XG | `technique` | `mute-stroke` / `open-tone` |
| `Conga Slap`, `Udo Slap`, `Req Tik` | GS SC-88 ETHNIC | `technique` | `slap` |
| `Conga Slide` | GS SC-88 ETHNIC | `technique` | `gliss` (closest; see §4.4) |
| `Cabasa Up` / `Cabasa Down` | GS SC-88 ETHNIC 95/96 | `technique` | `scrape`, with a direction KITWARP has no value for |
| `Short Guiro` / `Long Guiro` | GM1 73/74 | `technique` = `scrape`, duration carried by the MES-3 pairing |
| `Brush Tap` / `Brush Slap` / `Brush Swirl` / `Brush Tap Swirl` | GM2 BRUSH, XG 25-28 | `implement` = `brush` **plus** `technique` = `hit` / `slap` / `swirl` / (no value) |
| `Snare Roll` (GS 25, XG 29) | GS, XG | `ornament` | `roll` |
| `Gated SD`, `Gated Snare`, `Rim Gate 1-5`, `Kick Gate` | GS SC-88, XG Electro | `damping` | `gated` |
| `Room` / `Power` / `Jazz` / `Brush` / `Orchestra` set and voice prefixes | GM2, GS, XG | `voicing` | `room` / `power` / `jazz` / (`standard`) / `orchestra` |
| `LoFi Snare 1/2`, `Cowbell Lo-Fi`, `Crash Cymbal 2 Dark`, `Kick Soft Dark` | GS SC-8850, XG MU-extensions | `voicing` | `lo-fi` / `dark` |
| `TR-808 …`, `TR-909 …`, `TR-707 …`, `TR-606 …`, `CR-78 …` | GS SC-88/SC-8850 | `timbre` | `analog-808` / `-909` / `-707` / `-606` / `-cr78` |
| `Elec BD`, `Electric Snare 1`, `E Tom 1`, `Analog Bass Drum` | GM2 ELECTRONIC/ANALOG, GS, XG | `timbre` | `electronic` |
| `Snare Soft` / `Snare` / `Snare Tight`; `Kick Soft` / `Kick Tight` / `Kick` | XG 31/38/40 and 33/35/36 | `dynamic` — Yamaha's Soft/(default)/Tight triple on notes 31-40 is a **dynamic ladder addressed by note number**, not three snares | `soft` / `normal` / `hard` |
| `Gengari p` / `Gengari f`; `Jing p` / `Jing f` | Roland SC-8850 ASIA | `dynamic` | `soft` / `hard` |
| `Concert BD 1 Mute` / `Concert BD 1` | Roland SC-8850 | `damping` | `muted` / `none` |
| `Hand Cymbal` / `Hand Cymbal Short` | Yamaha Symphony Kit 49/51 | `damping` | `none` / `damped` |
| `Wadaiko` / `Wadaiko Rim`, `Djembe` / `Djembe Rim`, `Buk` / `Buk Rim` | GS ETHNIC, ASIA | `site` | `head` / `rim` |
| `Kelontuk` / `Kelontuk Side` | Roland SC-8850 GAMELAN 1 | `site` | `head` / `rim` (Roland's "Side") |
| CC #74 "radius of the striking position, from bell to rim" | MPE RP-053 §3.3.5 | `controllers.strike_position.radial` — **exact normative backing for the controller KITWARP already declares** |
| `usKeyGroup` 1-15 | DLS2 `<rgnh-ck>` | the file-format carrier for `relations.choke` and for the `openness`/`damping` exclusion semantics |

### 3.2 Terms that fit NO axis in vocabulary v0.1

These are the valuable ones. Each is a normatively named distinction that the current model
cannot express.

| Term | Source | Why no axis fits |
|---|---|---|
| **`[EXC]` / `MES` / `Alternate Group` / `usKeyGroup` as a first-class datum** | GM2 §2.8.1; M2-125-UM §4.1; Yamaha XG Drum Map; DLS2 | KITWARP has `relations.choke` and `relations.open-close`, which are *directed* relations between two terms. Every standard here instead declares an **undirected equivalence class**: "these N sounds are the same physical object and only one may ring". That class is what makes `openness` and `damping` mean anything, and it is also how Roland expresses the crash choke, the surdo, the whistle, the cuica and the guiro. There is no axis or relation for "these terms partition one resonator". |
| **`Rcv Note off` = O** (Brush Swirl, Brush Tap Swirl, Snare Roll, Samba Whistle H/L, Guiro Long) | Yamaha XG Drum Map; GM1 Developer Guidelines; GM2 §2.8.1 | A boolean *"this articulation has a player-controlled duration"*. It is not `technique`, not `ornament`, not `damping`. It is the property that decides whether a note length is meaningful. Three separate standards state it independently. |
| **`PAN` / `Recommended Pan Position`** | GM2 Appendix B (62 values); GM Lite §3.4.2; M2-125-UM Table 5 | A normative default stereo placement per sound. Related to `instance` but not derivable from it, and stated for hand percussion that has no `instance` at all (`Cabasa` 29, `Maracas` 24, `Bell Tree` 104). |
| **`Voices` / `E` (number of elements) and the `*` two-voice mark** | Roland SC-8850 legend; Yamaha XG Drum Map `E` column | How many synthesis voices one articulation costs. Not vocabulary, but it is normative per-sound data that any exporter targeting a polyphony-limited device needs. SP-MIDI exists entirely because of it. |
| **`[55]` / `[88]` / `[Pro]` compatibility-map prefixes** | Roland SC-8850 legend | "this is the sound the *older device generation* made". Not `voicing` (it is not a mic/room treatment), not `timbre` (it is not a different synthesis class). It is a **provenance-by-device-generation** tag. Roland puts four generations of the same closed hi-hat in one set. |
| **`[L]` / `[R]` and `… L/R` set names** | Roland SC-8850 `STANDARD L/R`, `BRUSH 2 L/R` | A stereo-split kit where the left and right halves of one instrument are separately addressable. Neither `instance` nor `limb`. |
| **`Reverse …`** (30+ GS entries; `Reverse Cymbal` is in GM2 ELECTRONIC note 52, so it is *in a standard*) | GM2 ELECTRONIC; GS RHYTHM FX | A transform of another sound. Not an instrument, technique, ornament or timbre. |
| **`Ride Cymbal Low/Mid/High Inner` and `… Edge`** | Roland SC-8850 PC54 | Inner/Edge is `site`. Low/Mid/High is a third quantity Roland does not define — plausibly three ride cymbals, plausibly three dynamic layers. Marked **UNVERIFIED**. If it is dynamic, KITWARP needs `dynamic` to be orthogonal to `site`, which it currently is; if it is three cymbals, it needs `instance` on a cymbal that is not in a left-to-right row. |
| **`Bend Gong`, `Bend Talking Drum`, `Hu Yin Luo Mid`/`Mid 2`/`High`/`High 2`** | GS ETHNIC, ASIA | Pitch that changes *during* the stroke, on an idiophone or membranophone. `technique.gliss` is a scrape-adjacent value; this is a bend of a struck sound. |
| **`Timpani F` … `Timpani f` (13 chromatic entries)** | GM2 ORCHESTRA notes 41-53 | Definite pitch on a percussion instrument, in a *standard*. No pitch axis exists. |
| **`Profile Details Discovery Bitmap` byte/bit per sound** | M2-125-UM Table 5 | Each of the 62 sounds has a permanently assigned bit position by which a device reports whether it has that sound. This is a **stable numeric identifier for a percussion sound issued by the MMA in 2025** — the closest thing to a KITWARP pivot id that any standards body has ever minted. |
| **"that name implies at least a musical role" / substitution by role** | M2-125-UM §4.1 | An explicit normative statement that a percussion sound name denotes a *role*, and that a device may substitute a different sound filling the same role. |
| **`Hi Q`, `Whip Slap`, `Click Noise`, `Seq Click L/H`, `Square Click`, `Metronome Click`/`Bell`, `High Q`, `Slap`, `Sticks`** | GM2 27-34; XG 15-24 | Utility and click sounds that are not instruments at all. `instrument.sticks` exists in v0.1 and covers one of them. |
| **`Scratch Push` / `Scratch Pull`, `Scratch H` / `Scratch L`** | GM2 29/30; XG 17/18 | Turntable gestures. Roland/MMA name them by direction, Yamaha by pitch. Neither is an axis value. |

### 3.3 Terms that fit an axis but need a value KITWARP does not have

| Term | Axis | Missing value |
|---|---|---|
| `Cabasa Up` / `Cabasa Down` | `technique` or a new modifier | scrape/shake **direction** |
| `Brush Tap Swirl` (XG 28) | `technique` | a tap-into-swirl compound; `swirl` alone loses the attack |
| `Timbales Paila` | `site` | the timbale **shell/side** stroke; `shell` exists, but `paila` is the trade name and must alias |
| `Kelontuk Side` | `site` | "side" as distinct from `rim` on a small drum — **UNVERIFIED** whether Roland means the shell or the rim |
| `Half-Open Hi-Hat 1` / `2` | `openness` | GS names exactly one intermediate state and then numbers *sample variants* of it; v0.1's eight-anchor ladder is finer than any standard supports (see §5.3) |
| `Snare Dry`, `Snare Dry Mute`, `Kick Dry Tight` | `damping` | Yamaha's `Dry` is a room/mic property; closest is `voicing`, but v0.1 has no `dry` |
| `Snare Snappy`, `SnrSnpyElctr` | `mechanism` | Yamaha's `Snappy` names the snare wires being present and tight; `wires-on` exists but not a tightness |

---

## 4. Conflicts and false friends

### 4.1 The MMA does not spell its own vocabulary consistently

Five MMA/AMEI *normative* documents publish the same 47 GM1 sounds under five different sets
of strings. Every one of these is a Recommended Practice or a MIDI-CI Profile, all still in
force.

| Note | GM1 (RP-003 Table 3) | GM2 (RP-024 App. B) | GM Lite (RP-033 §3.4.2) | RP-048 §2.1.2 | M2-125-UM Table 5 (2025) |
|---|---|---|---|---|---|
| 42 | **Closed Hi Hat** | Closed Hi-hat | Closed Hi-hat | **Closed Hi-Hat** | Closed Hi-hat |
| 44 | **Pedal Hi-Hat** | Pedal Hi-hat | Pedal Hi-hat | **Pedal Hi-Hat** | Pedal Hi-hat |
| 46 | **Open Hi-Hat** | Open Hi-hat | Open Hi-hat | **Open Hi-Hat** | Open Hi-hat |
| 47 | Low-Mid Tom | Low-Mid Tom | Low-Mid Tom | **Low Mid Tom** | Low-Mid Tom |
| 48 | **Hi Mid Tom** | High Mid Tom | High Mid Tom | **Hi Mid Tom** | High Mid Tom |
| 50 | High Tom | High Tom | High Tom | **Hi Tom** | High Tom |
| 58 | **Vibraslap** | Vibra-slap | Vibra-slap | **VibraSlap** | Vibra-slap |
| 60 | **Hi Bongo** | High Bongo | High Bongo | **Hi Bongo** | High Bongo |
| 62 | Mute Hi Conga | Mute Hi Conga | Mute Hi Conga | Mute Hi Conga | **Mute High Conga** |
| 63 | Open Hi Conga | Open Hi Conga | Open Hi Conga | Open Hi Conga | **Open High Conga** |
| 76 | Hi Wood Block | Hi Wood Block | Hi Wood Block | Hi Wood Block | **High Wood Block** |

Three separate drifts are visible: GM2 (1999) expanded `Hi` to `High` on the tom and the
bongo and hyphenated `Vibra-slap`; RP-048 (2007) reverted to `Hi` and closed up `VibraSlap`;
M2-125-UM (2025) expanded `Hi`→`High` on the conga and the wood block, which no earlier MMA
document had done, and adopted **Roland's** spelling for both (`Mute High Conga`,
`High Wood Block` are the SC-55 strings, §2.6). And note 58: Yamaha's XG map spells it
`Vibraslap`, siding with GM1 against GM2.

**This is the strongest available argument for ADR-0003.** The name string is not stable
even within one standards body's own corpus over 34 years. Only the note number was stable —
and §4.3 shows the note number is not stable either.

### 4.2 CC #74 means two incompatible things on a percussion channel

| Standard | CC/RPNC #74 on a drum sound |
|---|---|
| **MPE RP-053 §3.3.5** (2018) | "a digital hi-hat, in which CC #74 might encode the radius of the striking position, from bell to rim" — an **Initial-position** control, absolute, latched at Note On |
| **MIDI 2.0 M2-104-UM Table 11** (2020) | RPNC #74 = Sound Controller 5 = **Brightness** |
| **M2-125-UM §6.1.6** (2025) | RPNC #74 = Brightness = "the cut-off frequency of filter(s) for the specified Note Number… relative parameter whose center (null point) is 0x80000000" |
| **M2-125-UM Table 8** | MIDI 1.0 Key-Based Instrument Controller `nn = 74` = Brightness |

An MPE-conformant electronic hi-hat sending strike radius on CC #74 into a Drum Note Map
Profile receiver will have that value applied as a *relative filter cutoff offset*. The two
readings even disagree on the origin: MPE's Initial-position scheme is absolute over the
full range, MIDI 2.0's Brightness is bipolar around centre. MPE itself anticipates the
collision and offers a workaround (§3.3.5, option 2: "Fix CC #74 to Initial-64 behavior, and
designate another CC to convey the static initial position. One such implementation employs
**CC #75** for initial position") — but CC/RPNC #75 is Decay Time in the drum profile, so the
workaround collides too.

**There is no normatively defined MIDI controller for percussion strike position or for
hi-hat pedal position.** KITWARP's `controllers.hihat.pedal_position` and
`controllers.strike_position.*` have no standard behind them, only vendor practice.

### 4.3 The same sound sits on incompatible note numbers inside one vendor's own corpus

Roland, SC-8850 Owner's Manual, one document:

| Sound | SC-55/SC-88 STANDARD | SC-88 ETHNIC (PC 50) | SC-88 SFX (PC 57) |
|---|---|---|---|
| Castanets | 85 | **27** | — |
| Tambourine | 54 | **26** | — |
| Bell Tree | 84 | **34** | — |
| Crash Cymbal 1 | 49 | **28** | — |
| Snare Roll | 25 | **29** | — |
| Concert BD 1 | 36 (ORCHESTRA) | **32** | — |
| Scratch Push | 29 | — | **41** (and `Scratch Push2` at **31**) |
| Cabasa | 69 | **95/96** (Up/Down) | — |
| High Agogo | 67 | **84** | — |
| Claves | 75 | **97** | — |

And GM2 does the same inside one specification: `High Q` is note 27 in STANDARD and note 39
in SFX; `Sticks` is 31 in STANDARD and 43 in SFX; `Castanets` is 85 in STANDARD and 39 in
ORCHESTRA.

### 4.4 GM2's recommended pan is audience-perspective; KITWARP's `instance` is player-perspective

`vocabulary/axes.json` `reference_axes.instance` reads: *"ordered high to low in pitch for
toms and left to right from the player's seat for cymbals. The direction is fixed here and
must not be reinterpreted per device."*

GM2 Appendix B and M2-125-UM Table 5 place, from left to right:

- Low Floor Tom 34 → High Floor Tom 46 → Low Tom 58 → Low-Mid Tom 70 → High Mid Tom 82 →
  High Tom 94. Pitch **ascends** left to right.
- Hi-hat (42/44/46) at 84, "Right 32%".
- Ride Cymbal 1/2 and Ride Bell at 44, "Left 31%".

On a conventional right-handed kit the hi-hat is at the player's left, the ride at the
player's right, and the toms descend in pitch from left to right. GM2's image is the mirror
of that: **it is the audience's view, not the player's.** So an exporter that derives a pan
value from KITWARP's `instance` under the player's-seat rule produces a stereo image
mirrored against every MMA percussion table. This is a decision, not a defect — but it must
be a conscious one, and it is not currently written down anywhere.

### 4.5 Named false friends

| Word | Meaning A | Meaning B |
|---|---|---|
| `Slap` | GM2 note 28 / SFX note 40: an FX "slap" noise of no defined instrument | `Conga Slap`, `Udo Slap`, `Brush Slap`: a hand or brush stroke technique. Two unrelated senses in the same spec. |
| `Sticks` | GM1/GM2 note 31: two sticks struck together (a claves-like sound) | KITWARP `implement.stick`: the beater. The GM sound is an *instrument*, not an implement. |
| `Rim Shot` | Roland `CM Rim Shot` (SC-55 CM-64/32L note 37) sits where GM puts `Side Stick` — Roland means the cross-stick | XG `Open Rim Shot` (note 34) is a genuine rimshot, and XG *also* has `Side Stick` at 37. Same two words, opposite techniques. |
| `Closed` | Hi-hat: the two cymbals held together | `Hand Cym.Closed` (a Cakewalk `.ins` invention, §5.1) vs Yamaha's actual `Hand Cymbal Short` — a *damped* crash, not a closed one. Two plates struck and immediately choked is `damping.damped`, not `openness.closed`. |
| `Mute` | Conga/cuica/triangle/surdo: a stroke type producing a different sound | `Mute Crash Cymbal`: a choke, i.e. a *termination* of the previous sound |
| `Analog` | GM2 ANALOG set = TR-808 (Roland's own equivalence table, §2.6) | XG `Analog Kit` = Yamaha's own analog-modelled voices, not 808 samples. The set name does not identify the machine. |
| `Bell` | `Ride Bell` = the cup of a ride cymbal | `Jingle Bell`, `Bell Tree`, KITWARP `instrument.bell` = separate instruments |
| `Brush Swirl` | XG note 26, a sustained circular motion, `Rcv Note off = O` | Cakewalk `.ins` "Brush Swirl L"/"Brush Swirl H" — see §5.1, these are not Yamaha's names |
| `Hoo` (`High Hoo`/`Low Hoo`, SC-88 DANCE 78/79, `[EXC4]`) | A vocal sample occupying the cuica's note numbers *and its exclusion group* | The cuica it replaces. Roland reused the mute/open pair structure for a voice. |

---

## 5. Gaps against vocabulary v0.1, and where dossier 03's secondary tables are wrong

### 5.0 Gaps against vocabulary v0.1

Measured against `vocabulary/axes.json` v0.1.0 (serial 1). Ordered by how much of the
normative corpus each gap makes inexpressible.

| # | Gap | Evidence | Severity |
|---|---|---|---|
| 1 | **No axis or relation for an undirected exclusion class.** v0.1 has `relations.choke` (directed: "damps the last event on the referenced instrument") and `relations.open-close`. Every standard in this bucket instead declares an unordered set — "only one of these may ring" — and uses it for the hi-hat triple, the whistle/guiro/cuica/triangle/surdo/scratch pairs, the crash-choke pair, and 8+ world-percussion open/mute pairs | GM2 §2.8.1 (EXC1-7); M2-125-UM §4.1 (MES 1-7); Yamaha Alternate Group 1-4; Roland `[EXC1]`-`[EXC8]`; DLS2 `usKeyGroup` 1-15 | **highest.** Five independent standards encode it; KITWARP cannot round-trip it |
| 2 | **No "receives note off / has player-controlled duration" property.** Three standards state independently that a small, specific set of percussion articulations is gated by note length | GM1 Dev. Guidelines p.15 (long whistle, long guiro); GM2 §2.8.1 (ORCHESTRA 88, SFX 47-84); Yamaha `Rcv Note off` = O on notes 26, 28, 29, 71, 72, 74 | high — decides whether note length is meaningful on export |
| 3 | **No stable numeric identifier interop target.** M2-125-UM assigns each of its 62 sounds a permanent `Profile Details Discovery Bitmap` byte/bit. That is a standards-body-issued numeric id for a percussion sound, and KITWARP's registry has no field to record it | M2-125-UM Table 5 | high — this is the one external id worth pinning |
| 4 | **`openness` is over-specified.** v0.1 has eight ordered anchors; the corpus supports four (`closed`, `half`, `open`, plus pedal as a `technique`). See §5.3 | Roland SC-88 notes 42/46 across five sets; SC-8850 PC 54 | medium — not wrong, but unsupported from here |
| 5 | **No pan / default stereo placement, and `instance` runs the opposite way to every MMA table.** See §4.4 | GM2 App. B (62 values); GM Lite §3.4.2; M2-125-UM Table 5 | medium — an exporter decision that is currently undocumented |
| 6 | **No `pitch` field.** GM2's ORCHESTRA set puts a 13-note chromatic timpani run on notes 41-53, inside a standard | GM2 App. B, PC#49 | medium |
| 7 | **No modifier for `reverse`.** `Reverse Cymbal` is in GM2 ELECTRONIC note 52 — a standard, not an extension — and GS has 30+ | GM2 App. B; SC-88 RHYTHM FX | medium |
| 8 | **No device-generation provenance tag.** Roland's `[55]`/`[88]`/`[Pro]` puts four generations of the same closed hi-hat in one set; this is neither `voicing` nor `timbre` | SC-8850 legend p.44; PC 54 | medium |
| 9 | **`damping` mixes an implement (`towel`) into an outcome scale.** No standard names any physical damper; they name outcomes (`Mute`, `Short`, `Gate`). See §5A Q4 | zero hits for felt/pillow/Moongel/muffle across the corpus | low-medium — a factoring fault, cheap to fix now |
| 10 | **`instrument` lacks `surdo`, `agogo`, `bongo`, `conga`, `timbale`, `cuica`, `guiro`, `cabasa`, `maracas`, `claves`, `whistle`, `castanets`, `vibraslap`, `bell-tree`, `jingle-bell`, `wood-block` low/high** — all 47 GM1 sounds must be nameable or a GM1 layout cannot round-trip. v0.1's 27 instruments cover the kit and reserve the percussion families unminted | GM1 Table 3 | expected (families are deliberately reserved), recorded for completeness |
| 11 | **`mini-china`, `mini-hihat` have no source in the standards**, alongside `stack` and `xhat` which dossier 03 already flags | §5A Q2 | low — flags a provenance debt, not an error |
| 12 | **`technique.ping-shot`, `gok-shot`, `stick-shot` have no source in the standards** | §5A Q3 | low — same |
| 13 | **No direction on scrape/shake.** `Cabasa Up` / `Cabasa Down` are two named sounds in GS | SC-88 ETHNIC 95/96 | low |
| 14 | **No `[L]`/`[R]` stereo-half concept**, which is neither `instance` nor `limb` | SC-8850 `STANDARD L/R` | low |

Two things v0.1 gets **right** and that this bucket confirms rather than challenges:

- `controllers.strike_position.radial` has exact normative backing — MPE RP-053 §3.3.5 names
  a digital hi-hat's strike radius as the CC #74 use case. KITWARP is not inventing this.
- The decision to make `instrument` an open registry rather than a closed enum is forced by
  M2-125-UM's own clause that "a Device may include extra sounds assigned to Note Numbers 0
  through 26 and 89 through 127", and by Roland actually doing so across the whole 0-127
  range.

And one that this bucket says is **not** a KITWARP problem: there is no normatively defined
controller for hi-hat pedal position anywhere in the MMA corpus (§4.2), so
`controllers.hihat.pedal_position` cannot be aligned to a standard because no standard
exists. That is a gap in MIDI, not in the vocabulary.

### 5.1 GM1 — six names in `docs/research/03-midi-standards.md` §2.1 are not GM1's

Dossier 03 §2.1 is headed "GM Level 1 — percussion key map, all 47 sounds (notes 35–81)" and
sourced from `GM1_GM2.ins` section `[General MIDI Level 2 STANDARD Set]`, justified by
"GM2's Standard set is by definition GM1-compatible on 35–81". The justification is exact
about *notes* (GM2 §2.6 says so) and wrong about *names*: GM2 renamed six of them.

| Note | Dossier 03 §2.1 says | RP-003 Table 3 says | Verdict |
|---|---|---|---|
| 42 | Closed Hi-hat | **Closed Hi Hat** | GM2's string, mislabelled GM1 |
| 44 | Pedal Hi-hat | **Pedal Hi-Hat** | GM2's string |
| 46 | Open Hi-hat | **Open Hi-Hat** | GM2's string |
| 48 | High Mid Tom | **Hi Mid Tom** | GM2's string |
| 58 | Vibra-slap | **Vibraslap** | GM2's string |
| 60 | High Bongo | **Hi Bongo** | GM2's string |

The other 41 names are correct. The note numbers are all correct.

### 5.2 GM2 — the note map is right; two whole normative columns are missing

Checked note by note against RP-024 v1.2a Appendix B: **dossier 03 §2.2 is correct.** All
nine sets, all nine program numbers (both the 0-based wire values and the spec's 1-based
printing), and every per-set override list — ROOM 6, POWER 8, ELECTRONIC 10, ANALOG 19,
JAZZ 2, BRUSH 5, ORCHESTRA 25, SFX 46 — match the spec exactly. Its "set-dependence summary"
(23 set-dependent notes across the six kit-variant sets) is also correct.

What is missing rather than wrong:

1. **The PAN column** — 62 normative values, reproduced in §2.3 above. Dossier 03 does not
   mention that Appendix B has one.
2. **The `[EXC1]`-`[EXC7]` annotations and §2.8.1's group table** — reproduced in §2.3.
3. **§2.8.1's note-off rule** — "Note Off messages are ignored on Rhythm Channels, with the
   exception of the ORCHESTRA SET (specifically, Note number 88) and the SFX SET (Note
   numbers 47-84)."
4. Dossier 03 §5.4 open question 4 — *"Whether `Applause` at GM2 note 88 is formally part of
   the ORCHESTRA set or an out-of-range extension in the transcription"* — is **answered:
   it is formally part of the ORCHESTRA set.** Appendix B defines note 88 (E) in all nine
   set columns; it reads `---` ("Does not sound") in eight of them and `Applause`, PAN 64,
   in ORCHESTRA. It is in the map, not outside it.
5. Dossier 03 §5.4 open question 5 — whether the MIDI-CI Default Drum Note Map profile
   extends the GM vocabulary — is **answered: no.** M2-125-UM Table 5 is GM2's Standard set,
   notes 27-88, with three renamings (§4.1) and no added sounds. What it adds is the
   discovery bitmap, the MES naming and the per-note controller set.

### 5.3 Roland GS — six name errors, a systematic spacing error, and one interpretive error

Against the SC-8850 Owner's Manual, which is Roland's own document.

| Where | Dossier 03 §2.3/§2.4 says | Roland's manual says |
|---|---|---|
| SC-55 STANDARD, note 84 | `Belltree` | **`Bell Tree`** |
| SC-55 CM-64/32L, note 106 | `Waves` | **`SeaShore`** |
| SC-55 CM-64/32L, notes 44 / 46 | `CM Open High Hat 2` / `CM Open High Hat 1` | **`CM Open Hi-Hat2` / `CM Open Hi-Hat1`** |
| SC-55 SFX note 53, CM-64/32L note 77 | `Screaming` | **`Scream`** |
| SC-55 SFX, note 62 | `Windchimes` | **`Wind Chimes`** |
| SC-88 RHYTHM FX, note 64 | `Tekno Trip` | **`Tekno Thip`** — spelled this way in both the SC-8850 and the SC-88Pro manual. Almost certainly Roland's own typo for "Trip", but the normative string is `Thip`. |

**Systematic:** dossier 03 inserts a space before trailing ordinals throughout the SC-55 and
SC-88 maps where Roland closes them up — `Kick Drum 2`/`Kick Drum2`, `Snare Drum 1`/`Snare
Drum1`, `Low Tom 2`/`Low Tom2`, `Crash Cymbal 1`/`Crash Cymbal1`, `Ride Cymbal 1`/`Ride
Cymbal1`, `Closed Hi-hat 1`/`Closed Hi-hat1`, `Concert BD 1`/`Concert BD1`, `Footsteps 1`/
`Footsteps1`, `Telephone 1`/`Telephone1`, `Bird 2`/`Bird2`, `Applause 2`/`Applause2`,
`Tape Stop 1`/`Tape Stop1`, `Reverse Tom 1`/`Reverse Tom1`, `Reverse Cymbal 1`/`Reverse
Cymbal1`, `Brush Tap 1`/`Brush Tap1`, `Electric Snare 2`/`Electric Snare2`, `Scratch Push 2`/
`Scratch Push2`. Note that **Roland is not internally consistent**: in the SC-8850's *own*
sets (as opposed to the SC-55/SC-88 compatibility maps in the same manual) it does use the
space — `Crash Cymbal 1 [EXC3]`, `Brush Tap 1`, `Reverse Crash Cymbal 1`. So the space is
right for SC-8850-native names and wrong for SC-55/SC-88 names.

Also correct but worth recording: dossier 03 faithfully preserved three of Roland's own
errata — `Brash Swirl` (SC-55 BRUSH note 40 in the SC-8850 manual; dossier 03 normalises it
to `Brush Swirl`), `CM M.TomAcoustic Middle Tom` (SC-55 CM-64/32L note 47), and `Pandiero`
for *pandeiro* (SC-88 ETHNIC 79/80).

**Missing rather than wrong:** all 24 GS drum-set Program Change numbers (supplied in §2.6 —
dossier 03 §5.4 item 3 records this as out of scope); every `[EXC]` annotation; the `*`
two-voice marks; and the note range, which dossier 03 gives as 25-108 and which is actually
**0-127** on the SC-8850.

**Interpretive error.** Dossier 03 §2.6 asserts:

> Hi-hat openness is a **graded** axis, not 3 states … `Closed Hi-Hat`, `Closed Hi-Hat 2`,
> `Closed Hi-Hat 3`, `Closed Hi-Hat 4`, `Half-Open Hi-Hat 1`, `Half-Open Hi-Hat 2`,
> `Open Hi-Hat`, `Open Hi-Hat 2`, `Open Hi-Hat 3`, `Pedal Hi-Hat` — **10 openness steps on
> one instrument**

Roland's own tables show the numbers are **kit indices, not openness degrees**. In the SC-88
maps, note 42 carries `Closed Hi-hat1` in STANDARD 1, `Closed Hi-hat2` in STANDARD 2,
`Closed Hi-hat3` in ROOM, `Closed Hi-hat3` in POWER, `Closed Hi-hat2` in ELECTRONIC — and
note 46 carries `Open Hi-hat1/2/3/3/2` in the same five sets. The suffix indexes *which kit's
hi-hat sample*, exactly parallel to `Standard 1 Snare 1` vs `Room Snare 1`. In the SC-8850
`CYMBAL&CLAPS` set (PC 54), where Roland gathers every hi-hat it owns onto separate notes,
the same suffixes reappear alongside `[55]`/`[88]` generation prefixes and `TR-808`/`TR-707`/
`TR-606`/`CR-78` machine prefixes — all in `[EXC1]`.

The correct reading: **GS names exactly four openness states — closed, half-open, open,
pedal** — and everything else in that list is `voicing`, `timbre` or device-generation
provenance. Dossier 03's own §2.6 finding 4 ("kit-timbre is an independent axis from sound
identity") is the correct explanation of the data its finding 1 misreads.

This matters for v0.1 directly: the `openness` axis currently has eight ordered anchors
(`tight, closed, closed-loose, quarter, half, three-quarter, loose, open`). **No MIDI
standard or vendor drum map in this bucket supports more than four.** Anything finer must be
justified from e-drum modules or sample libraries (buckets 04/05 of round 1), not from here.

### 5.4 Yamaha XG — ten Standard Kit names are not Yamaha's, and the kit list is short by one

Dossier 03 §2.5 takes XG from `pedrolcl/VMPK` `data/gmgsxg.ins`. Against **two independent
Yamaha data lists** (MU100 Sound List; PLG100-XG Data List — the latter being XG-Level-1-only
hardware):

| Note | Dossier 03 §2.5 says | Yamaha MU100 says | Yamaha PLG100-XG says |
|---|---|---|---|
| 17 | Scratch Push | **Scratch H** | Scratch H |
| 18 | Scratch Pull | **Scratch L** | Scratch L |
| 26 | Brush Swirl L | **Brush Swirl** | Brush Swirl |
| 28 | Brush Swirl H | **Brush Tap Swirl** | BrushTapSwrl |
| 31 | Snare L | **Snare Soft** | Snare Soft |
| 33 | Bass Drum L | **Kick Soft** | Kick Soft |
| 35 | Bass Drum M | **Kick Tight** | Kick Tight |
| 36 | Bass Drum H | **Kick** | Kick |
| 38 | Snare M | **Snare** | Snare |
| 40 | Snare H | **Snare Tight** | Snare Tight |
| 83 | Jingle Bell | **Jingle Bells** | Jingle Bells |

The kit-variant diffs inherit the same problem. Dossier 03's `Standard2 Kit` reads
`34 = Open Rim Shot 2, 35 = Bass Drum M 2, 36 = Bass Drum H 2, 38 = Snare M 2, 40 = Snare H 2`;
Yamaha's Standard Kit 2 reads `34 = Open Rim Shot H Short, 35 = Kick Tight Short,
36 = Kick Short, 38 = Snare Short, 40 = Snare Tight H`.

Its `Classic Kit` reads `36 = Gran Casa, 41-50 = Jazz Tom 1..6, 49 = Hand Cym.Open L,
51 = Hand Cym.Closed L, 57 = Hand Cym.Open H, 59 = Hand Cym.Closed H`. Yamaha's Symphony Kit
reads `33 = Kick Soft 2, 35 = Gran Cassa, 36 = Gran Cassa Mute, 38 = Band Snare,
40 = Band Snare 2, 41-50 = Tom Jazz 1..6, 49 = Hand Cymbal, 51 = Hand Cymbal Short,
57 = Hand Cymbal 2, 59 = Hand Cymbal 2 Short`. Not one of the seven names matches, the kit is
not called Classic, `Gran Casa` is a misspelling of `Gran Cassa`, and the changes at notes
33, 35, 38 and 40 are missed entirely. The Open/Closed reading of the hand cymbals is a
semantic error, not just a string error (§4.5).

**Kit list.** Dossier 03 gives XG Level 1 as eleven kits. Yamaha's PLG100-XG Data List — an
XG-Level-1 board with no MU extensions, so its list is definitive for Level 1 — enumerates
**twelve**: ten on Bank MSB 127 (PC 1, 2, 9, 17, 25, 26, **28**, 33, 41, 49) plus two SFX
kits on Bank MSB 126 (PC 1, 2). The missing one is the **Dance Kit** (MSB 127, PC 28).
Dossier 03 also lists a `Classic Kit` where Yamaha has `Symphony Kit`.

**Missing rather than wrong:** Yamaha's `Rcv Note off` column (six sounds, §2.7), the
`Alternate Group` column (four groups, §2.7), the `E` element-count column, and the
Bank/Program numbers for the kits.

Dossier 03 §5.4 item 2 records XG Level 1's kit membership as UNVERIFIED. It is now
verified, and it was wrong.

### 5.5 One claim in dossier 03 §4.1 is now falsified by a 2025 standard

> drum-remap's `role` axis has **no analogue** in any standard. GM/GS/XG name timbres, never
> musical function.

M2-125-UM §4.1 (2025), *Sound Names: Undefined Tonal Quality*:

> The tonal qualities or properties of each sound is not defined. Each sound is defined in
> name only, although that name implies at least a musical role. … A Device may substitute a
> sound which is not identical to the name of the sound, if that sound is intended in context
> to fill a similar role to the named sound.

The current MMA position is the *opposite* of what dossier 03 states: the standard defines
role and explicitly refuses to define timbre. `role` therefore has a normative analogue, and
substitution-by-role is normatively sanctioned behaviour.

### 5.6 Summary of the error census

| Standard | Notes/structure | Names | Verdict |
|---|---|---|---|
| GM1 | correct | **6 of 47 wrong** (GM2 strings mislabelled) | usable after correction |
| GM2 | correct throughout, all 9 sets and PCs | correct | **sound**; PAN and EXC columns missing |
| GS SC-55/SC-88 | correct; PC numbers absent; note range understated (0-127, not 25-108) | 6 outright errors + systematic ordinal spacing | usable after correction |
| XG | Standard Kit note numbers correct; **kit list short by one (Dance Kit)** | **10 of ~72 Standard Kit names wrong**, kit-variant diffs worse | **not usable as-is** |

---

## 5A. Answers to the four questions referred by the vendor-glossary bucket

Scope limit stated up front: **this bucket holds no sample-library or e-drum-module
articulation lists.** Its corpus is the MMA/AMEI Recommended Practices and the Roland/Yamaha
*manufacturer* documentation for GS and XG. Three of the four questions ask which *library*
coined a term; I cannot answer that, and I say so rather than guess. What I can do is settle
the negative half of each question authoritatively — whether the term exists anywhere in the
MIDI standards or in Roland's and Yamaha's own tone-generator documentation — because that
is exactly the corpus that would have to contain a term for it *not* to be a library
coinage. Every "absent" below is a grep over the full extracted text of the SC-8850 and
SC-88Pro Owner's Manuals, the Yamaha MU100 Sound List, the PLG100-XG Data List, GM2 v1.2a,
the Complete MIDI 1.0 Detailed Specification, GM Lite and M2-125-UM.

**Q1 — Does any articulation list use Zildjian's "ride area" / "crash area" rather than the
bow/edge/bell triple?**

Not in this corpus, and the corpus is more relevant to the question than it looks.
The string `area` occurs in these documents only in EQ, memory-map and geographic senses
(`area of the center frequency`, `memory area`, `User Area`, `Warehouse Area`,
`Dominican Republic`); it never names a cymbal region. What the manufacturers use instead:

| Vendor | Terms for cymbal regions | Locator |
|---|---|---|
| Roland | `Inner` / `Edge`, plus `Ride Bell` | SC-8850, PC 54 `CYMBAL&CLAPS`, notes 51/59 and 81-86 |
| Yamaha | `Ride Cymbal Cup` (no bow or edge term at all) | XG Drum Map note 53 |
| MMA | `Ride Bell` only — no bow, no edge, no area | GM1 Table 3 note 53; GM2 App. B note 53; M2-125-UM Table 5 note 53 |

So the normative and vendor-normative vocabulary is **`bell`/`cup` + `inner`/`edge`**, i.e.
a two-or-three-zone radial scheme, and "area" is absent. One further datum that bears
directly on the question and that I would not have expected: **Zildjian sat on the working
group for the 2025 MIDI-CI Default Drum Note Map Profile** and the resulting standard
contains no zone vocabulary of any kind — its `Ride Bell` (53), `Ride Cymbal 1` (51) and
`Ride Cymbal 2` (59) are three separate *sounds*, not zones of one cymbal. **UNVERIFIED:**
the Zildjian/Medeli/BAC Audio working-group attribution comes from trade coverage
(digitalDrummer, Aug 2026, source #44), not from the M2-125-UM PDF, whose extracted text
carries no contributors section. Whether a *library* uses "ride area" is outside my corpus —
refer back to the library-articulation bucket.

**Q2 — `mini-china` and `mini-hihat`: library-only coinages?**

Absent from every document in this bucket. The nearest strings are Yamaha MU-extension
voices `Minimal Kick`, `Minimal Tom L`, `Minimal Tom H` (a texture adjective, not a size)
and the lead voice `Old Mini` — none of them cymbals. The standards' small-cymbal vocabulary
is exactly one word, `Splash Cymbal` (GM1 note 55, in every standard since), and their
china vocabulary is exactly one word, `Chinese Cymbal` (GM1 note 52); Roland adds
`Chinese Cymbal 2` in the SC-8850 `CYMBAL&CLAPS` set, which is a second sample, not a
smaller cymbal. So: **no MIDI standard and neither Roland's nor Yamaha's own tone-generator
documentation names a mini china or a mini hi-hat.** That is consistent with them being
library or e-drum coinages, but it does not prove it — proving it needs the library and
module buckets. What it does prove is that they cannot be justified from the standards, and
dossier 03 §4.1 already notes the parallel case: `stack` and `xhat` "appear nowhere in
GM1/GM2/GS/XG". `mini-china` and `mini-hihat` belong in that same list, which dossier 03
omits them from.

**Q3 — `ping-shot`, `gok-shot`, `stick-shot`: which library introduced each?**

I cannot say which library — no library material is in this bucket. I can report that all
three are **absent from the entire normative and vendor corpus**: `gok` returns zero hits
across all eight documents; `stick shot` and `stick-shot` return zero; `ping` occurs only as
the MU100 synth voice `Ping` in an E.Piano bank and inside the word `comping` in effect
descriptions — never as a cymbal or snare articulation. For contrast, the shot-family terms
the corpus *does* have are `Open Rim Shot` (XG note 34), `Rim Shot` / `808 Rim Shot` /
`Analog Rim Shot` / `CM Rim Shot` (GS, GM2 ANALOG), `Rim Gate 1-5` and `Snare Rim` variants
(SC-8850) — all rimshot-family, none of them a stick-on-stick or bell-ping term. So the
three v0.1 techniques have no standards provenance and their provenance must be established
from library documentation.

**Q4 — Which dampers do libraries ship as separate articulations (felt strip, pillow,
Moongel, control ring)?**

Cannot answer from this bucket, and the negative result is unusually clean: **`felt`,
`pillow`, `muffl`/`muffle`, `Moongel` and `control ring` each return exactly zero hits
across all eight documents.** The only `damp` occurrences are (a) GM2's `Damper` = CC#64
sustain pedal and `Half-Damper`, which is a *piano* control and which GM2 §3.3 explicitly
puts out of scope for percussion ("Rhythm Channels shall not respond to this message"), and
(b) Yamaha's `High Damp`, a reverb high-frequency parameter. **No MIDI standard and no
Roland or Yamaha tone-generator document in this corpus names a physical drum damper at
all.** What they name instead is the *result*: `Mute Crash Cymbal 1/2` (a choke, GS),
`Gran Cassa Mute` / `Hand Cymbal Short` (Yamaha Symphony Kit), `Concert BD 1 Mute` (GS),
`Gated SD` / `Gated Snare` / `Rim Gate 1-5` / `Kick Gate` (GS, XG). That is a real finding
for the axis model: **the standards model damping as an outcome on the `damping` axis and
never as an implement**, which is why v0.1's `damping` values (`none, muted, damped, towel,
gated`) mix an implement (`towel`) into an outcome scale. `towel` is the odd one out and has
no standards support; if libraries ship felt-strip/pillow/Moongel/control-ring as separate
articulations, those are implements and the model needs somewhere other than `damping` to
put them. That recommendation is safe to make from here; the library census is not.

---

## 6. Self-critique (round C)

**What this bucket got that dossier 03 did not have.** Every normative document, free. The
GM2 PAN column and the seven EXC groups. The GM1 Developer Guidelines' note-off and
mutual-exclusion rules. GS program-change numbers and Roland's own legend. Yamaha's
Alternate Group and Rcv-Note-off columns. The 2025 MIDI-CI drum profile, which nobody in
round 1 saw and which is the most directly relevant document in the corpus. The complete
`.midnam` DTD. MPE's hi-hat strike-radius clause.

**The single most authoritative source I did not get: the Yamaha XG Format Specification
itself** — the developer document, as distinct from device data lists. Everything in §2.7 is
inferred from two Yamaha *product* data lists. Those are Yamaha's own publications and they
agree with each other, which is strong, but they do not tell me what XG Level 1 *requires*
as opposed to what these two products *ship*. Specifically unresolved: whether "XG Level 1"
formally mandates exactly the twelve kits the PLG100-XG provides, and whether the Alternate
Group numbers are normative or per-product. If reconciliation wants one more document, it is
this one. Second in line is the **Roland GS Format Specification**, for the same reason —
§2.6 is entirely from owner's manuals.

**Other gaps, named:**

1. **The SC-88 Owner's Manual has no text layer** (8.4 MB of scans). The SC-88 map here is
   Roland's *reprint* in the SC-8850 manual. Roland reprints are marked `[88]` and are
   reliable, but a first-edition check would need OCR.
2. **The SC-55 Owner's Manual was not reached directly.** Same reasoning. In particular the
   `Brash Swirl` typo (§5.3) is present in the SC-8850 reprint and I could not check whether
   the SC-55's own manual says `Brush`.
3. **`rp24(e).pdf`, the 1999 original English GM2, has no extractable text.** I used v1.2a
   (2007) instead. The three changes between 1.0 and 1.2a are listed in v1.2a's preface and
   none touches Appendix B, so the percussion table is unchanged — but this is inference
   from a changelog, not a diff.
4. **Wayback is unreachable in this environment** (`403 Blocked by egress policy`, verified
   on both the CDX API and a snapshot URL). The brief lists it as a primary route; it is not
   available. `archive.org` proper — metadata API and `advancedsearch.php` — *does* answer,
   and is the route a later bucket should use. Losing Wayback cost me the archived
   `midi.org/dtds/` copy of the DTD (worked around via a GitHub mirror) and any archived
   midi.org GM1 Sound Set page.
5. **The web-search budget is one session-wide pool shared by all workers, and it ran out at
   my 16th search**, partway through round A. Later empty results are the budget, not the
   query. Everything after that was link-following and vendor-CDN URL-pattern probing. Sources 26-28,
   32, 33 (SC-8820, SC-D70, SCB-55, QY70, B900) were located but not fetched; sources 10, 13,
   17 (DLS amendments, CA-034, MIDI-CI Common Rules) likewise. None of them is likely to
   change a conclusion here, but the SCB-55 manual is the cheapest independent check on the
   SC-55 map.
6. **`Ride Cymbal Low/Mid/High Inner|Edge` is unresolved** (§3.2). Roland does not say what
   Low/Mid/High means. Resolving it needs the SC-8850's sound-design documentation or an
   instrument, not a manual.
7. **I did not systematically diff the SC-88Pro and SC-8850 native maps** against dossier
   03's §2.6 extension claims beyond spot checks (ride zones, mute crash, half-open,
   TR-prefixes, `Tekno Thip`). Every spot check confirmed dossier 03's *structural* findings
   while correcting its openness interpretation, so I judged a full diff lower value than
   the GM1/GM2/GS/XG normative work — but it is not done.
8. **No count of how many of dossier 03's 184 canonical sounds change identity** under these
   corrections. I believe the answer is small — the XG errors are name errors on sounds that
   are correctly *identified* (`Bass Drum H` and `Kick` are the same drum) — but the
   `Hand Cym.Open/Closed` → `Hand Cymbal / Hand Cymbal Short` correction does change one
   sound's identity from an openness pair to a damping pair, and the reconciliation pass
   should re-run the normalisation rather than take my word for it.

**What I would tell the reconciliation pass to do first:** re-key dossier 03's GM1 and XG
tables from §2.1 and §2.7 of this file before anything else uses them, and add
`M2-125-UM Table 5` as a fifth standard to the union — it is current, freely redistributable
in fact-content terms, and it is the map that MIDI 2.0 devices will actually negotiate.

---

## 7. Provenance

| Fact set | Source | Licence verdict |
|---|---|---|
| GM1 Table 3, GM Developer Guidelines (§2.1, §2.2) | The Complete MIDI 1.0 Detailed Specification 3rd ed., MMA0007/RP003 | © 1991, 1994, 1995-2006, 2014 MMA. "ALL RIGHTS RESERVED. NO PART … MAY BE REPRODUCED …". **Document not redistributable; the 47 note→name facts are not protectable.** Quote sparingly, re-key into KITWARP ids. |
| GM2 Appendix B, §2.6, §2.8.1 (§2.3) | GM2 v1.2a, RP-024, MMA | © 1999, 2003, 2007 MMA. Same reservation. Same verdict. |
| GM Lite §3.4.2, RP-048 §2.1.2 (§2.5) | RP-033, RP-048, MMA/AMEI | Same. |
| M2-125-UM Table 5, MES, §4.1 prose (§2.4) | MIDI-CI Profile for Default Drum Note Map v1.0 | © 2025 AMEI and MMA. Same reservation. |
| MIDI 2.0 RPNC list (§2.9) | M2-104-UM v1.0 | © MMA/AMEI. Same. |
| MPE §3.3.5 (§2.9) | RP-053 v1.0 | © 2017 MMA. Same. |
| DLS2 `usKeyGroup` (§2.9) | RP-025 v1.0a | © MMA. Same. |
| MIDINameDocument DTD (§2.8) | MMA DTD v1.0, 19 Jan 2003, obtained from `github.com/MichaelGJennings/midnamaker` `dtd/MIDINameDocument10.dtd` | The DTD is an MMA work; the mirror repository's licence was **not checked**. The canonical MMA URI is dead. **Do not vendor the file**; the element names are facts. |
| GS drum sets, PC numbers, EXC groups, legend (§2.6) | Roland SC-8850 and SC-88Pro Owner's Manuals, `cdn.roland.com` | © Roland. Manuals freely downloadable from Roland's own CDN, not redistributable. Note-name facts are not protectable. |
| XG drum map, Alternate Groups, Rcv Note off, kit list (§2.7) | Yamaha MU100 Sound List (`usa.yamaha.com`), PLG100-XG Data List (`data.yamaha.com`) | © Yamaha. Same verdict as Roland. |
| SysEx ID allocation structure (§2.10) | `https://midi.org/sysexidtable` | Public web page, © MMA. Counts and structure are facts. |

Working files for this bucket are under `/tmp/b05/` (PDFs and `pdftotext -layout` output);
nothing was written into the repository working tree except this dossier and the worker
status file.
