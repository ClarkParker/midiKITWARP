# Reconciliation extract C — the engineering layer

Dossiers read in full:

| Tag | File | Corpus |
|---|---|---|
| **D05** | `docs/research/round2/05-mma-normative.md` | MMA/AMEI Recommended Practices (GM1, GM2 RP-024, GM Lite RP-033, RP-048, MIDI-CI Drum Note Map M2-125-UM 2025, MPE RP-053, MIDI 2.0 M2-104-UM, DLS1/2, SP-MIDI, MIDINameDocument DTD, SysEx ID table) + Roland GS and Yamaha XG *tone-generator* documentation |
| **D10** | `docs/research/round2/10-hardware-primary-docs.md` | E-drum module and drum-machine primary documentation: Roland V-Drums/TM/SPD/HandSonic/TR, Yamaha DTX, ATV, 2Box, Alesis, Elektron, Korg, Oberheim, LinnDrum, E-mu |
| **D06** | `docs/research/round2/06-vendor-glossaries.md` | Cymbal, drumhead, stick, hardware and hand-percussion **manufacturer trade terminology**, plus retailer/trade-press glossaries |

Also read before judging: `vocabulary/axes.json`, `vocabulary/pivot.json`, `vocabulary/rules.json`,
`docs/adr/0001-pivot-vocabulary.md`, `docs/adr/0003-identifiers-and-registry.md`, and
`scratchpad/recon/late-findings-to-verify.md` (checklist answered in §7).

## How attestations are counted here

An **independent tradition** is an organisation that authored its terminology independently of
the others. Explicit lineage cautions that apply to *my* three dossiers, each of which would
inflate a naive count:

1. **The five MMA/AMEI spellings of the GM1 map are ONE tradition, not five.** GM1 RP-003,
   GM2 RP-024, GM Lite RP-033, RP-048 and M2-125-UM all restate the same 47 sounds; D05 §4.1
   shows they restate them in five *different* strings. Agreement between them is not
   corroboration; disagreement between them is the finding.
2. **The SC-88 and SC-55 maps in D05 are Roland's own reprints inside the SC-8850 manual**
   (D05 §6 gaps 1–2: the SC-88 manual has no text layer and the SC-55 manual was not reached).
   Three "sources" are one document.
3. **The TR-08 (2017) is not a witness to the TR-808 (1980).** D10 §2.11: "the reissue splits
   what the original merged" — LT is *either* Low Tom *or* Low Conga on the 808 and two
   separate instruments with separate notes on the TR-08. "Any layout derived from the TR-08
   chart is not a layout of a TR-808."
4. **Evans and ProMark are one publisher.** D06 rows 16 and 19 both resolve to `daddario.com`
   (D'Addario). Head-terminology and stick-terminology agreement between them is one house
   style. Similarly Zildjian's FAQ and `ae.zildjian.com` are one publisher, and Thomann DE and
   Thomann EN are one retailer translated.
5. **Vic Firth and Zildjian publish from the same `ae.<brand>.com/education/` platform**
   (D06 rows 2–3 vs 20–23). Whether they are corporately one house is **not stated in the
   dossier**; treat their agreement as *possibly* non-independent — UNVERIFIED.
6. Roland's tone-generator line (D05, SC series) and Roland's V-Drums/TR line (D10) use
   *different* vocabularies for the same objects, but they are **one manufacturer**. Counted as
   one tradition, with the internal split noted where it matters.

Counts below are of independent traditions **within these three dossiers only**. A term
attested by one vendor is marked so explicitly.

---

# 1. TERMS

Axis column: `axis=value` in v0.1, or **NONE** (no axis fits — see §2), or *alias* (same
referent as an existing value under a different spelling).

## 1.1 `site` — contact site on the instrument

| Term as the source spells it | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `SNARE <HEAD>`, `<HEAD>` | the struck membrane | `site=head` | 6: Roland, Yamaha, ATV, 2Box, Remo, Millenium/Thomann | D10 §2.1 (TD-50X Data List pp.6–7), §2.5, §2.8, §2.9; D06 §2.6 |
| `Batter Head` | trade word for the struck head, "the top drumhead you hit" | `site=head` (*trade alias*) | 2: Remo, Yamaha-education | D06 §2.6 (Remo FAQ; Yamaha *Anatomy of a Snare Drum*) |
| `Resonant Head` / `Snare Head` / `Snare-Side Head` | the bottom head | `site=underside` (*trade alias*) | 2: Remo, Yamaha-education | D06 §2.6, §4 ("head makers say resonant head; KITWARP says `underside`") |
| `tapa` | the cajon's front playing plate | `site=head` | 1: Meinl via Thomann | D06 §2.10, §3.1 |
| `Fell` | German for head, 2Box's own word | `site=head` | 1: 2Box | D10 §2.7 |
| `tête` | French for head | `site=head` | 1: 2Box | D10 §2.7 |
| `SNARE <RIM>`, `Rm`, `Rim`, `Rand` | the hoop | `site=rim` | 6: Roland, Yamaha, ATV, 2Box, Yamaha-edu (`Counter Hoop`), Thomann | D10 §2.1, §2.5, §2.8, §2.9, §2.7; D06 §2.9 |
| `Counter Hoop` / `Top Hoop` / `Bottom Hoop` | "the rim or hoop that tightens the drumhead" | `site=rim` (*trade alias*) | 1: Yamaha-education | D06 §2.9 |
| `Rm1` / `Rm2` | numbered second rim on one pad | `site=rim`, `site=rim2` | 1: Yamaha (DTX `Pad14Rm1/Rm2`) | D10 §2.5 |
| `KickRm` | a rim zone **on the kick drum**, its own trigger input source | `site=rim` on `instrument=kick` — expressible but unattested elsewhere | 1: Yamaha | D10 §2.5, §3.2 item 3 |
| `<XSTICK>` / `SnareCl` / `Side Stick` / `Cross Stick` | stick laid across the head, butt on the rim | `site=crossstick` | 6: Roland, Yamaha, ATV, 2Box, MMA (`Side Stick` GM1 37), LinnDrum (`SIDESTICK SNARE`) | D10 §2.1, §2.5, §2.8, §2.9, §2.16; D05 §2.1 |
| `<BOW>` / `Bw` / `Bow` / `Fläche` / `arc` | the playable middle region of a cymbal | `site=bow` | 5: Roland, Yamaha, ATV, 2Box, Meinl | D10 §2.1, §2.5, §2.8, §2.9, §2.7; D06 §2.1 (Meinl Wiki) |
| `Ride area` | Zildjian's name for the same region: "the center portion of the cymbal… effective for pronounced stick tones" | `site=bow` (*vendor alias*) | 1: Zildjian | D06 §2.1, §3.1 |
| `Surface` | Paiste's name for the same region: "produces the majority of the cymbal's vibration" | `site=bow` (*vendor alias*) | 1: Paiste | D06 §2.1, §3.1 |
| `<EDGE>` / `Eg` / `Edge` / `Rand` / `bord` | the outer perimeter of a cymbal | `site=edge` | 7: Roland, Yamaha, ATV, 2Box, Paiste, Meinl, Thomann | D10 §2.1, §2.5, §2.8, §2.9; D06 §2.1 |
| `Crash area` | Zildjian's name for the edge: "the outer edge where a cymbal responds immediately" | `site=edge` (*vendor alias*) | 1: Zildjian | D06 §2.1, §3.1 |
| `BELL` (Roland, 2Box) | the raised centre boss | `site=bell` | 4: Roland, 2Box, Paiste, Meinl | D10 §2.1, §2.9, §4; D06 §2.1 |
| `Cup` / `Cp` / `RideCp` / `Ride Cymbal Cup` | the same boss | `site=bell` (*needs alias*) | 4: Yamaha (module + XG), ATV, Zildjian ("bell **or cup**"), Thomann-DE (`Kuppe`) | D10 §2.5, §2.8, §4; D05 §2.6, §5A Q1; D06 §2.1 |
| `Kuppe` | German for the bell/cup | `site=bell` | 2: Thomann-DE, 2Box-DE | D06 §2.1; D10 §2.7 |
| `cloche` | French for the bell | `site=bell` | 1: 2Box-FR (+ unverified FR trade) | D10 §2.7; D06 §2.1 |
| `Ride Bell` | the ride's boss, as a *sound* on note 53 | `site=bell` | 1 tradition, 5 documents: MMA (GM1/GM2/GM Lite/RP-048/M2-125-UM) | D05 §2.1, §2.3, §5A Q1 |
| `Ride Cymbal Inner` | Roland's word for the bow of a ride | `site=bow` | 1: Roland (GS) | D05 §2.6, §3.1 |
| `Ride Cymbal Edge` | the ride's edge as a separate sound | `site=edge` | 1: Roland (GS) | D05 §2.6 |
| `Inner` (`Conga Inner`, `Bongo H Inner`) | a named radial band between centre and edge on a hand drum | `position=halfway`, **approximately** — "not obviously the same partition" | 1: Roland (HPD-20) | D10 §2.17 |
| `Shell` | "the body of the drum" | `site=shell` | 2: Yamaha-education, Roland (`Kelontuk Side`, `Timbales Paila`) | D06 §2.9; D05 §2.6, §3.3 |
| `Paila` | the metal shell side of a timbale, struck with the stick | **NONE** — `site=shell` is near but "a timbale's paila is a different surface from a drum shell" | 2: Roland (HPD-20 `Timbale H Paila`; GS `Timbales Paila`), LP trade (UNVERIFIED) | D10 §2.17, §3.2 item 18; D05 §2.6; D06 §2.10 (UNVERIFIED) |
| `cascara` | playing the timbale shell with the stick shoulder | `site=shell` (UNVERIFIED source) | 1: LP trade usage, search-summary only | D06 §2.10, §3.1 |
| `Ears` (`Djembe Ears`) | the metal rings on a djembe's tuning ropes | **NONE** — a site that is not part of the resonating body | 1: Roland (HPD-20) | D10 §2.17, §3.2 item 19 |
| `Hole` (`Pot Drum Hole S / Hole L`) | the drum's aperture as a strike site | **NONE** | 1: Roland (HPD-20) | D10 §2.17 |
| `Bottom` (`Pot Drum Bottom`) | the underside of a hand drum | `site=underside` | 1: Roland (HPD-20) | D10 §2.17 |
| `Gourd` (`Berimbau Gourd`) | the resonator gourd as a strike/contact site | **NONE** | 1: Roland (HPD-20) | D10 §2.17 |
| `Side` / `SideEdge` (`Cajon Side L`, `Kelontuk Side`) | the side panel of a box/small drum | **NONE / UNVERIFIED** — Roland does not say whether "Side" is shell or rim | 1: Roland (HPD-20 + GS) | D10 §2.17; D05 §3.3 |
| `Center` (HPD-20 name token) | centre of the head | `position=centre` | 1: Roland | D10 §2.17 |
| `Loch` | the centre hole of a cymbal | **NONE** (not a strike site) | 1: Thomann-DE | D06 §2.1 |
| `Bearing edge` | where the shell meets the head | **NONE** — construction, "never a strike location" | 2: Yamaha-education, Evans (`collar`) | D06 §2.6, §3.2 Group 3 |
| `Collar` | the formed lip of the drumhead | **NONE** — construction | 1: Evans (D'Addario) | D06 §2.6 |
| bottom hi-hat cymbal as a strike site | underside of the top / top of the bottom hat | **NONE found** — "no vendor source reached names the hi-hat's bottom cymbal as a separate strike site, which some libraries do ship" | 0 vendor traditions | D06 §5.7 |
| cymbal `underside` | v0.1 mints it; no vendor names it | `site=underside` — **unsourced for cymbals** | 0 | D06 §5.7 |

## 1.2 `position` — where on the site

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Head strike position: center to perimeter` | the radial continuum, verbatim in Roland's CC gloss | `position` / `controllers.strike_position.radial` | 2: Roland, Yamaha (CC16/17) | D10 §2.3, §2.6 |
| `Rim strike position: deep to shallow` | radial position **on the rim** | `controllers.strike_position.rim_depth` | 1: Roland | D10 §2.3 |
| `left to right` / `Position Adjust LR` / `Hi-Hat LR CC` | lateral strike position | `controllers.strike_position.lateral` | 1: Roland (VH-14D) | D10 §2.3 |
| "the location **within a zone** that is struck" (`Snare Position`) | position is a sub-property of site | confirms `position` ⊂ `site` | 1: Yamaha | D10 §2.6 — "the cleanest normative statement anywhere in this bucket" |
| `Position Area: INSIDE-5 – DEFAULT – OUTSIDE+5` | per-pad calibration window for the radial axis | **NONE** — makes `position` relative, not absolute geometry | 1: Roland | D10 §3.2 item 11 |
| "the top third of the cajón's playing surface" | the cajon slap zone | `position=perimeter` (approx.) | 1: Meinl via Thomann | D06 §2.10, §3.1 |
| "centre of the drumhead" (conga bass stroke) | | `position=centre` | 1: Thomann (retailer, authority C) | D06 §2.10 |
| "the outside edge of the head" (conga open tone) | | `position=perimeter` | 1: Thomann | D06 §2.10 |
| CC #74 = "the **radius** of the striking position, from bell to rim" | strike position on a digital hi-hat | `controllers.strike_position.radial` — **the only normative MMA backing for it** | 1: MMA (MPE RP-053 §3.3.5) | D05 §2.9, §3.1, §5.0 |

## 1.3 `contact` — part of the implement

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Tip` (`Cowbell 1 Tip`) | stick tip | `contact=tip` | 2: Roland (HPD-20), ProMark (as `bead`) | D10 §2.17; D06 §2.8 |
| `Bead` | the stick maker's word for the tip | `contact=tip` (*trade alias*) | 1: ProMark/D'Addario | D06 §2.8, §4 |
| `Shoulder` | the stick maker's word for the shank | `contact=shank` (*trade alias*) | 1: ProMark/D'Addario (+ retail trade, UNVERIFIED) | D06 §2.8, §3.1, §4 |
| `Butt` | the stick's back end | `contact=butt` | 1: retail trade, UNVERIFIED | D06 §2.8, §3.1 |
| `neck`, `shaft` | stick anatomy between tip and butt | **NONE** — no axis value, and none needed | 1: retail trade, UNVERIFIED | D06 §2.8 |
| Wood vs nylon tip | "nylon tips have a brighter more articulate sound" | **NONE** — tip *material* is carried nowhere; `implement` has no value, `contact` has no material | 1: ProMark/D'Addario | D06 §5.4 ("a real hole") |
| Tip shapes: `Acorn`, `Barrel`, `Oval`, `Round (large/small)`, `Teardrop` | five named tip geometries with published sound effects | **NONE** | 1: ProMark/D'Addario | D06 §2.8 |

## 1.4 `technique` — the stroke

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Rim Shot` / `Open Rim Shot` / `SnareOp` | stick strikes head and rim together | `technique=rimshot` | 4: Roland, Yamaha, MMA (GM2 ANALOG `Analog Rim Shot`), 2Box | D10 §2.1–2.2, §2.5; D05 §3.1 |
| `Rim Shot` **on a hi-hat / crash trigger** | striking the pad's *edge sensor* | `site=edge` + `technique=hit`, **not** `rimshot` | 1: Roland | D10 §4 — "same words, different gesture… where the physical rim does not exist" |
| `Cross Stick` / `Side Stick` / closed rim shot | | `technique=sidestick` | 6 (as §1.1 crossstick row) | D10 §2.1–2.2, §2.5, §2.8, §2.9; D05 §2.1 |
| `Xstick Adjust` | cross-stick and open rim shot are **one gesture separated by a velocity threshold on the rim zone** | affects how `sidestick`/`rimshot` are addressed | 2: Yamaha (`Xstick Adjust`), Roland (`XStick Detect Sens`) — "both vendors agree the discrimination is by strike strength, not by position" | D10 §2.6, §2.3 |
| `Bell shot` | striking the ride's cup | `technique=hit` + `site=bell` | 1: Roland (playing-methods chart, RIDE only) | D10 §2.2, §3.1 |
| `Bell Gain` | "balance between the force of a strike on the bell (bell shot technique) and the loudness" | supports bell-shot as a distinct playing method | 1: Roland | D10 §2.3 |
| `Brush sweep` / `SNARE <BRUSH>` | brush drawn across the head | `technique=sweep` + `implement=brush` | 2: Roland (TD-50/50X/27 only), MMA/Yamaha (`Brush Swirl`) | D10 §2.1, §2.2; D05 §2.7 |
| `Brush Tap` / `Brush Slap` / `Brush Swirl` / `Brush Tap Swirl` | four named brush articulations | `implement=brush` × `technique=hit/slap/swirl/(none)` | 2: Yamaha (XG 25–28), MMA (GM2 BRUSH) | D05 §2.7, §3.1 |
| `Choke play` / `choke` | damping a ringing cymbal by grabbing it | **NONE on `technique`** — exists only as `relations.choke` + `controllers.choke_amount` | 5: Roland, Yamaha, 2Box, Alesis, Elektron (+MMA as `Mute Crash` exclusion) | D10 §2.2, §2.3, §2.9, §3.2 item 2, §5.1; D05 §2.6 |
| Polyphonic Key Pressure choke | "the decay of the note… will be shortened based on the value" | `controllers.choke_amount` — **continuous, keyed to the note number, not a CC** | 1: Roland | D10 §2.3 |
| `Foot Close` / `HhFtCl` / `Chick` | pedal-closed hi-hat sound | `technique=chick` | 5: Yamaha, Alesis, MMA (`Pedal Hi-Hat`), Roland, Paiste (`Hi-Hat Chick Sound`) | D10 §2.5, §2.10, §3.1; D05 §2.1; D06 §2.2 |
| `Foot Splash` / `HhFtSp` / `Splash` | pedal opened-and-shut splash | `technique=foot-splash` | 4: Yamaha (**its own trigger input source with its own note**), Alesis, Roland (`Foot Splash Sens`), Thomann | D10 §2.5, §2.10, §2.3; D06 §2.4 |
| `Bass` (B) / `Bass tone` | flat palm at the centre, "a low, muffled sound" | `technique=bass-tone` | 2: Thomann-congas, Roland (HPD-20 `Conga Bass`, `Djembe Hi Bass`) | D06 §2.10; D10 §2.17 |
| `Open tone` (O) | "the basic sound… a clear pitch with a resonant tone" | `technique=open-tone` | 3: Thomann-congas, Roland (`Kelontuk`/`Kopyak Open`), MMA (`Open Hi Conga`) | D06 §2.10; D05 §2.6, §3.1 |
| `Closed slap` (S) | fingers rest on the head after contact | `technique=slap` + `damping=muted` | 1: Thomann-congas | D06 §2.10, §3.1, §4 |
| `Open slap` (OS) | fingertips leave the head | `technique=slap` + `damping=none` | 1: Thomann-congas | D06 §2.10 |
| `Slap` (`Conga Slap`, `Udo Slap`, `Slap tone`) | | `technique=slap` | 3: Roland (GS + HPD-20, 13 name tokens), Thomann, Meinl(cajon) | D05 §2.6, §3.1; D10 §2.17; D06 §2.10 |
| `Heel` (H) | "dropping the heel of the palm onto the drumhead" | `technique=heel` | 2: Thomann-congas, Roland (HPD-20 `Conga /Heel L`, 6 tokens) | D06 §2.10; D10 §2.17 |
| `Toe` | | `technique=toe` | 1: Roland (HPD-20 `Conga /Toe R`, 5 tokens) — **first vendor citation for this v0.1 value** | D10 §2.17 |
| `Tap` (T) | the quiet conga stroke v0.1 calls `toe` | `technique=toe` under a different name | 1: Thomann (+ *touch*, *toque de punta*, UNVERIFIED) | D06 §2.10, §4, §5.3 |
| `Thumb` | | `technique=thumb` | 2: Roland (HPD-20 `Cajon Thumb`, `Pandeiro Thumb`), Vic Firth (thumb roll) | D10 §2.17; D06 §2.11 |
| `Mute` / `Mute stroke` (`Conga H Mute`, `Kelontuk Mute`) | hand stays on the head | `technique=mute-stroke` | 3: MMA, Roland, Yamaha | D05 §2.1, §2.6, §3.1 |
| `Scrape` (`Cabasa Up`/`Cabasa Down`, `Bendir Scrape`) | | `technique=scrape`; **direction has no value** | 2: Roland (GS + HPD-20) | D05 §2.6, §3.3; D10 §2.17 |
| `Gliss` (`Conga Slide`, `Pot Drum Gliss`, `Berimbau Bend`) | pitch slide during the sound | `technique=gliss` — "closest; a bend of a struck sound is not a scrape" | 1: Roland | D05 §2.6, §3.2; D10 §2.17 |
| `Press` (`Berimbau Press`; Roland `Fixed: PRESS`) | pressing the string/pedal to alter the sound | **NONE** | 1: Roland | D10 §2.17, §2.4, §3.2 item 1 |
| `Harm` (`Bendir Harm`) | harmonic/overtone stroke — damping at a node to sound a partial | **NONE** — "not `mute-stroke`: a mute-stroke kills the sound, a harmonic selects a partial" | 1: Roland (HPD-20) | D10 §2.17, §3.2 item 17 |
| `Damp` (5 HPD-20 tokens) | | `damping=damped` | 1: Roland | D10 §2.17 |
| `Click`, `Roll`, `Buzz`, `Bend`, `Finger`, `Hand`, `Stick`, `Sweep`, `Choke`, `Splash` (HPD-20 name tokens, counts in D10) | compositional naming grammar `<instrument> [<site>] [<technique>] [<hand>]` | mixed | 1: Roland | D10 §2.17 |
| `Fist strike`, `palm strike ("pop")`, single-/two-finger playing, `knee-and-fist` | tambourine dynamic techniques | **`fist` has NO axis value** (see §4); palm/finger ≈ `implement=hand`/`finger` | 1: Vic Firth (2nd tradition for `fist` alongside marching's Casey Claw, per late-findings item 5) | D06 §2.11, §3.2 Group 4 |
| `Thumb roll`, `shake roll`, `finger roll` | three tambourine roll *production methods* | all collapse to `ornament=roll`; `technique=thumb` exists but a thumb roll is a **friction** roll | 1: Vic Firth | D06 §2.11, §3.1, §5.3 |
| `Glancing blow` | the correct way to strike a crash edge; "do not hit directly at and 'through' the cymbal" | **NONE** — arguably the default, not a named technique | 2: Paiste, Thomann | D06 §2.11, §5.3 |
| `Tilt` | tilting a crash reduces stick impact | **NONE** — mounting geometry | 1: Thomann | D06 §2.11 |
| `Zing`, `Ding`, `Tap`, `Sizzle`, `Sizz-Press`, `Sizz-Suck`, `Hard Prep Crash`, `Chokes in the Flat Position`, `Basic/Softer Crashes` | Zildjian's named **hand-cymbal** articulations | **NONE** — no piatti instrument in v0.1 | 1: Zildjian (bucket 08 supplies six more traditions for `zing` — see §6) | D06 §2.11 |
| `Muffling against the body` / torso damping | hand-cymbal choke against the chest | `damping=damped` | 2: Vic Firth, Thomann | D06 §2.11, §3.1 |
| `Muffled playing` (tambourine, hand on head) | | `damping=muted` | 1: Vic Firth | D06 §2.11 |
| `Snare Roll`, `Brush Swirl`, `Guiro Long` (Rcv Note off = O) | sustained, player-timed articulations | `ornament=roll` etc. **plus a missing duration property** | 2: Yamaha (XG), MMA (GM1 Dev. Guidelines; GM2 §2.8.1) | D05 §2.7, §3.2 |
| `Reverse …` (30+ GS entries; `Reverse Cymbal` GM2 ELECTRONIC 52) | a time-reversed sample of another sound | **NONE** — a transform, not an instrument/technique/ornament/timbre | 2: Roland (GS), MMA (it is *in* GM2) | D05 §2.6, §3.2, §5.0 gap 7 |
| `Scratch Push` / `Scratch Pull`; `Scratch H` / `Scratch L` | turntable gestures, named by direction (MMA/Roland) or pitch (Yamaha) | **NONE** | 2: MMA, Yamaha | D05 §2.3, §2.7, §3.2 |

## 1.5 `openness`, `damping`, `mechanism`

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Closed Hi Hat` / `Hi-Hat Closed` / `HI-HAT CLOSE <BOW>` / `HhClBw` | cymbals held together | `openness=closed` | 4: MMA, Roland, Yamaha, 2Box/ATV/Alesis (each) → effectively 6 | D05 §2.1, §2.6, §2.7; D10 §2.1, §2.5, §2.8–2.10 |
| `Open Hi-Hat` / `HI-HAT OPEN <BOW>` / `HhOpBw` | | `openness=open` | same | same |
| `Half-Open Hi-Hat 1`, `Half-Open Hi-Hat 2` | "the one genuine intermediate openness state Roland names" (GS) | `openness=half`; the 1/2 suffix indexes **samples**, not degrees | 1: Roland (GS) | D05 §2.6, §5.3 |
| `Fixed: NORMAL, PRESS, CLOSE, HALF1, HALF2, OPEN` | Roland V-Drums' normative openness enumeration; "if something other than NORMAL is selected, the openness… does not change" | `openness` — six anchors, one of them (`PRESS`) **below closed** | 1: Roland (V-Drums) | D10 §2.4 |
| `Pressure Sens` | "how the sound of the closed hi-hat changes according to how hard you press… **while the pedal is closed**" (VH-14D) | **NONE** — a second continuous dimension below `tight` | 1: Roland | D10 §2.3, §3.2 item 1 |
| `Offset` (Roland −100…+100; Alesis) | where the module decides the hat is "closed" | **NONE** — calibration of the openness axis | 2: Roland, Alesis | D10 §2.3, §2.10 |
| `FootClosePos` (−32…0) | "the position at which the hi-hat switches from open to closed… the smaller the virtual opening" | **NONE** — same calibration | 1: Yamaha | D10 §2.6 |
| `Pedal Curve` ("Log favors closed; Exp favors open") | a transfer function on the openness axis itself | **NONE** — "an openness scalar recorded from one module is not directly comparable with one from another" | 1: Alesis | D10 §2.10, §5.3 item 7 |
| `sloshy` | "loose, messy hi-hat sound when open" | `openness=open` (a *sound-character* word) | 1: Sabian | D06 §2.3, §3.1 |
| `tight` / `loose` | Sabian: "compact, clean and direct response" / "open, airy feel" — **response qualities, not apertures** | v0.1 uses both as `openness` anchors; "the referents are adjacent but not identical" | 1: Sabian | D06 §2.3, §4 |
| `Mute Crash Cymbal 1/2 [EXC3]/[EXC4]` | the choke, expressed as an exclusion pair with the ringing crash | `damping=muted` **plus** `relations.choke` | 1: Roland (GS) | D05 §2.6, §3.1 |
| `Muffling: OFF, TAPE1–7, BLANKET1–3, WEIGHT1–2, DONUT1–2, FELT1–4` | Roland's per-instrument damping enumeration, **by physical damper and by amount** | `damping` — `tape`/`blanket`/`weight`/`donut`/`felt` all missing | 1: Roland (V-Drums) | D10 §2.4, §5.1 |
| `Gated SD`, `Gated Snare`, `Rim Gate 1–5`, `Kick Gate` | gated-reverb production sounds as named articulations | `damping=gated` | 2: Roland (GS), Yamaha (XG Electro) | D05 §3.1 |
| `Gran Cassa Mute`, `Hand Cymbal Short`, `Concert BD 1 Mute` | orchestral mute/open pairs | `damping=muted` / `damped` | 2: Yamaha, Roland | D05 §2.6, §2.7, §3.1 |
| `Low Cut: OFF / HALF / FULL` | cymbal low-frequency removal | **NONE** (production, not damping) | 1: Roland | D10 §2.4 |
| `felt strip`, `damping pillow`, `foam rail`, `Moongel`, `damping ring` / `control ring` / `O-ring`, `head overlay`, `duct tape`, `Snareweight`, `Mini Muff`, transparent damping ring | the trade's named dampers | **NONE** — v0.1 has `towel` and none of these | 2: Thomann (retailer), Evans (`Control Ring`, `Dry Vents`) | D06 §2.7, §2.6, §5.5 |
| `towel` | v0.1 `damping` value | — | **0 traditions in all three dossiers.** D05 §5A Q4: `felt`, `pillow`, `muffl*`, `Moongel`, `control ring` return **exactly zero hits** across all eight normative/vendor documents; D06 lists nine trade dampers and `towel` is not among them; Roland's nearest value is `BLANKET` | D05 §5A Q4, §5.0 gap 9; D06 §5.5; D10 §2.4 |
| `Strainer Adj.: OFF, LOOSE1–3, MEDIUM1–3, TIGHT1–3`; `Wire Level −6…+6`; `Wire Type TYPE1–3` | snare-wire tension and character, **graded** | `mechanism` — v0.1 has only the binary `wires-on`/`wires-off` | 1: Roland | D10 §2.4, §3.2 item 8, §5.1 |
| `SNAPPY` (`SD SNAPPY`) | the 808's snare-wire amount, **continuous** | `mechanism` — same gap, from 1980 | 1: Roland (TR-808/TR-08) | D10 §2.11, §3.2 item 8 |
| `Snare Buzz` | sympathetic snare rattle from another drum | **NONE** — a coupling between two instruments | 1: Roland | D10 §2.4 |
| `Snare strainer release` / `Throw Off` | the part that engages/disengages the wires | `mechanism=wires-on/off` (*the vendor names the part, the pivot names the state*) | 1: Yamaha-education | D06 §2.9, §4 |
| `Snappy` (`Snare Snappy`, `SnrSnpyElctr`) | Yamaha's name for wires present and tight | `mechanism` — no tightness value | 1: Yamaha (XG) | D05 §3.3 |
| `Sizzle Type: OFF / RIVET / CHAIN / BEADS`, `Sizzle Amount` | sizzle as a **parameter of any cymbal**, three named mechanisms | **NONE** — v0.1 encodes sizzle as the *instrument* `sizzle-ride` | 2: Roland, Zildjian (`Sizzle Rivets` sold as an accessory) | D10 §2.4, §3.2 item 9; D06 §2.1, §4 |
| `[EXC1]`–`[EXC8]` / `MES 1–7` / `Alternate Group 1–4` / `usKeyGroup 1–15` | "these N sounds are one physical object and only one may ring" | **NONE** — an *undirected equivalence class*; v0.1 has only directed relations | 4: MMA (GM2+M2-125-UM+DLS2), Roland (GS `[EXC8]` **beyond the MMA's seven**), Yamaha (XG), + TR-727 below | D05 §2.2, §2.3, §2.4, §2.6, §2.9, §3.2, §5.0 gap 1 |
| TR-727 pair exclusion | "It is not possible to output the following pairs of voices at the same time… the Cabasa will be automatically replaced with Maracas" | **NONE** — undirected, hardware-fixed, in a 1985 primary source | 1: Roland (TR-727) | D10 §2.13 |
| `MUTE SEND` / `MUTE RECEIVE` (1–8) | Roland's **directed** mute groups, per zone, with an explicit self-mute exemption | **NONE** | 1: Roland (TD-27/TD-50/TD-50X/TM-6 PRO only; TD-17 and TD-30 have none) | D10 §2.14 |
| `AltGroup: off, S&R1–32, S1–32, R1–32` | Yamaha's **directed halves plus an explicit undirected option**, at *layer* granularity | **NONE** — "the richest model found anywhere in this bucket" | 1: Yamaha | D10 §2.14 |
| `Mono/Poly` per layer | self-exclusion: a pad mutes its own previous sound | **NONE** — a third distinct relation | 1: Yamaha | D10 §2.14 |
| Elektron voice coupling (`CP mutes RS, HT mutes MT, OH mutes CH, CB mutes CY`) | directed, hardware-fixed, **not configurable** | **NONE** | 1: Elektron | D10 §2.14 |
| `Rcv Note off = O` (XG notes 26, 28, 29, 71, 72, 74) | "this articulation has a player-controlled duration" | **NONE** | 2: Yamaha, MMA (GM1 Dev. Guidelines: long whistle + long guiro; GM2 §2.8.1: ORCHESTRA 88, SFX 47–84) | D05 §2.2, §2.3, §2.7, §3.2 |
| HPD-20 flags `*l` (sustains under GATE/ALT) and `*n` ("also sound at note-off") | duration-dependent realisation, **two attacks bracketing a held gate** | **NONE** | 1: Roland | D10 §2.17, §3.2 item 20 |
| HPD-20 flag `*h` | "instruments whose open/close state can be controlled by a hi-hat control pedal" — granted to **non-hi-hats** | **NONE** — openness as a per-instrument capability | 1: Roland | D10 §2.17, §3.2 item 21 |

## 1.6 `implement`

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Beater Type: FELT1, FELT2, WOOD, PLASTIC1, PLASTIC2` | kick beater material | `implement=felt-/wood-/plastic-beater` | 2: Roland, Vic Firth (`VicKick`: felt, wood, **fleece**) | D10 §2.4, §3.1; D06 §2.8 |
| `fleece` beater | | **NONE** — v0.1 has felt/wood/plastic/rubber/superball | 1: Vic Firth (UNVERIFIED, search text) | D06 §5.4 |
| `Brush` / `Brushes` | | `implement=brush` | 3: Roland (`SNARE <BRUSH>`, `SNARE BRUSH` group), MMA/Yamaha (BRUSH kits), Vic Firth | D10 §2.1, §2.4; D05 §2.7; D06 §2.8 |
| brush materials: wire, rattan, grass, birch, synthetic | five different sounds sold as different products | **NONE** — v0.1 has one `brush` | 1: Vic Firth (UNVERIFIED) | D06 §2.8, §5.4 |
| `Rute` | "premium birch dowels secured in a birch drumstick handle" | `implement=rod` (*the German trade word vs the library word*) | 1: Vic Firth (UNVERIFIED) | D06 §2.8, §3.1, §4 |
| rute's "moveable band that adjusts the effect from crisp to splashy" | a continuously variable implement state | **NONE** | 1: Vic Firth (UNVERIFIED) | D06 §5.4 |
| `felt-covered mallets` | orchestral suspended-cymbal mallets | `implement=mallet-soft…hard`, but **no vendor hardness grades were reached** | 1: Thomann | D06 §2.11, §5.4 |
| `Hand`, `Finger` (HPD-20 tokens; `Timbale H Hand`) | | `implement=hand` / `finger` | 1: Roland | D10 §2.17 |
| `fist` | "held in a fist, where all the fingers wrap around the stick" (marching, late-findings item 5); Vic Firth's tambourine `fist strike` and `knee-and-fist` | **NONE — absent from `axes.json`** | 2: Vic Firth (D06) + marching pedagogy (D08, via late-findings) | D06 §2.11; D10 §5.1 records `fist`/`fingernail` as "unused by these vendors" |
| `fingernail` | | **NONE — absent from `axes.json`**; **0 traditions in my three dossiers** | 0 here (Read p.164 `Colle unghie` is D02's) | D10 §5.1 |
| hickory / maple / Shira Kashi oak; taper | stick wood and profile | **NONE** — build properties of the implement | 1: ProMark/D'Addario | D06 §2.8 |
| rubber pad vs **mesh** pad | pad surface material, which **gates whether a technique exists at all** | **NONE** — a property of the layout slot | 1: Roland | D10 §2.2, §3.2 item 6 |

## 1.7 `instrument` — kit, and the vocabulary behind the reserved families

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Ride`, `Crash`, `Hi-hat`, `Splash`, `China`, `Stack`, `Crash-Ride` | kit cymbal types with published size ranges | `instrument=*` — all present in v0.1 | 4: Sabian, Meinl, Thomann, Roland (`STACKED CYMBAL` group) | D06 §2.4; D10 §2.4 |
| `China Ride` | "combination between a china and ride" with a 1–2" upturned edge | **NONE** — v0.1 has `crash-ride` but not `china-ride` | 1: Meinl | D06 §2.4, §5.1 |
| `Flat Ride` | a ride **without a bell** | **NONE** — an identity, not a voicing | 1: Meinl | D06 §2.4, §5.1 |
| `Trash Crash`, `Trash Splash`, `Trash China` | cymbals with hole cut-outs | **NONE** — "a different construction from a stack and a different sound" | 1: Meinl | D06 §2.4, §5.1 |
| `Drumbal` | "a cymbal which is used on a drum", with a handle | **NONE** — "an instrument whose identity depends on being coupled to another instrument. Nothing in the axis model expresses coupling" | 1: Meinl | D06 §2.4, §3.2 Group 5 |
| `Bell` / `Bell-Becken` (cymbal type) | heavy small cymbal, splash-shaped | `instrument=bell` | 2: Meinl, Thomann-DE | D06 §2.4 |
| `Effect cymbals` | grouping term for splash + china | **NONE** — a family label | 1: Sabian | D06 §2.4, §5.1 |
| `swish`, `pang`, `cup chime` | further cymbal types | **NONE**; not found in any reached vendor source — worklist | 0 | D06 §5.1 |
| `Suspended cymbal`, `Crash cymbals (pairs)` / hand cymbals | orchestral single vs clashed pair, "held by straps that pass through the hole" | **NONE** — v0.1's `crash` is a suspended cymbal; there is no pair instrument | 2: Thomann, Zildjian (marching line) | D06 §2.4, §2.11, §5.2 |
| `gong drum`, `piccolo snare`, `concert tom` (single-headed), `timbale`, `marching snare`, `conga`/`quinto`/`tumba`, `bongo`, `cajon` | catalogue instrument names | **reserved families, unminted** | 2: Thomann, Meinl (+ Yamaha-education for marching snare) | D06 §5.2 |
| `octoban` / "tube toms" | deep small-diameter single-headed toms | `instrument=octoban` — **matches trade usage** | 1: trade | D06 §5.2 |
| `mini-china`, `mini-hihat` | v0.1 instruments | — | **0 traditions.** Absent from every MMA document and from Roland's and Yamaha's own tone-generator documentation (D05 §5A Q2); no vendor source in D06 (§5.1); no e-drum module names them (D10) | D05 §5A Q2, §5.0 gap 11; D06 §5.1 |
| `xhat` | auxiliary hi-hat | — | **0 traditions in these three dossiers** (D05 records dossier 03's finding that `stack` and `xhat` "appear nowhere in GM1/GM2/GS/XG"; `stack` is rescued by Meinl/Thomann/Roland, `xhat` is not) | D05 §5A Q2 |
| `aux-pad`, `jam-block` | | **0 traditions here** (`BLOCK/COWBELL` is a Roland *group* name) | D10 §2.4 |
| TR-727 voices: HI/LOW BONGO, MUTE/OPEN HI CONGA, LOW CONGA, HI/LOW TIMBALE, HI/LOW AGOGO, CABASA, MARACAS, SHORT/LONG WHISTLE, QUIJADA, STAR CHIME | 16 named voices | reserved `perc.*` families | 1: Roland (1985 primary) | D10 §2.13, §5.4 |
| TR-808 voices: BD, SD, LT/LOW CONGA, MT/MID CONGA, HT/HI CONGA, RS/CLAVES, CP/MARACAS, CB, CY, OH, CH, AC | 12 panel slots, **three of them switchable between two instruments** | `instrument` + `timbre=analog-808` | 1: Roland | D10 §2.11 |
| TR-8S/TR-909 slots: `BD SD LT MT HT RS HC CH OH CC RC` | eleven-slot vocabulary; **no `CB`**; `CY` split into `CC`+`RC` | `instrument` + `timbre=analog-909` | 1: Roland | D10 §2.12 |
| HPD-20 Latin/African instrument names (~60): conga, tumba, bongo, timbale, cajon, pandeiro, tamborim, repinique, surdo, bombo, agogo, claves, guiro, maracas, caxixi, ganza, chafchas, cabasa, afuche, quijada, vibra-slap, cuica, berimbau, rain stick, djembe, kenkeni, sangban, doumdoumba, bougarabou, talking drum, bendir, pot drum, log drum, water drum, afro claves, metal castanets, apitua, grello, african bracelet, african jingle, ankle bells, moroccan castanet | primary-sourced percussion names ready to mint | reserved `perc.*` | 1: Roland (official download) | D10 §2.17, §5.4 |
| GM1's 47 sounds (surdo, agogo, bongo, conga, timbale, cuica, guiro, cabasa, maracas, claves, whistle, castanets, vibraslap, bell-tree, jingle-bell, wood block…) | | reserved families | 1: MMA | D05 §2.1, §5.0 gap 10 |
| `Hi Q`, `Slap`, `Square Click`, `Metronome Click`, `Metronome Bell`, `Seq Click L/H`, `Click Noise`, `Whip Slap`, `Sticks`, `Finger Snap`, `Applause` | utility/click/FX sounds that "are not instruments at all" | **reserved `utility` family, unminted**; only `sticks` exists | 2: MMA, Yamaha | D05 §2.3, §2.7, §3.2 |
| `SIDESTICK SNARE` (LinnDrum, 1982) | cross-stick as a **separate named instrument** | precedent for Roland's `CROSS STICK` instrument *group* 40 years later | 2: Linn, Roland | D10 §2.16, §2.4 |
| `PERC 1` / `PERC 2` / `CYMBAL` (Oberheim DMX voice cards) | one card holds **two unrelated instruments** (tambourine+rimshot; shaker+handclaps; ride+crash) | **NONE** — "instrument identity is not recoverable from the voice name" | 1: Oberheim | D10 §2.15 |
| Roland Instrument groups (34): `KICK A/B/PROC/ELEC`, `SNARE (PROC/ELEC/BRUSH)`, `CROSS STICK (PROC)`, `TOM (PROC/ELEC/BRUSH)`, `HI-HAT (PROC/ELEC/FIXED ELEC)`, `RIDE`, `CRASH`, `CHINA`, `SPLASH`, `STACKED CYMBAL`, `CYMBAL PROC/ELEC/OTHERS`, `BLOCK/COWBELL`, `BELL/CHIME/GONG`, `PERCUSSION`, `PERC ELEC`, `CLAP`, `SOUND FX`, `ELEMENTS`, `OFF` | family × timbre-suffix taxonomy with occurrence counts | family is documentation; the **suffix system** is the finding | 1: Roland | D10 §2.4 |
| `ELEMENTS` (28), `CYMBAL OTHERS` (10) | vendor catch-all groups "whose members are not instruments in any organological sense" | **NONE** | 1: Roland | D10 §3.2 item 16 |

## 1.8 `timbre` and `voicing`, and the build vocabulary behind them

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `TR-808/909/707/606`, `CR-78` prefixes; `T8-`/`T9-` | machine lineage in the sound name | `timbre=analog-808/-909/-707/-606/-cr78` | 2: Roland, Yamaha (`T8`/`T9` are "Yamaha's unbranded names for TR-808 and TR-909 samples") | D05 §2.6, §3.1; D10 §2.5, §3.1 |
| `TR-626 Kick`, `DR-110 Kick`, `R-8 Kick` | three further machine lineages | **NONE** — no `analog-626`, `analog-dr110`, `analog-r8` value | 1: Roland | D10 §3.1, §5.1 |
| `Elec BD`, `Electric Snare`, `E Tom`, `KICK ELEC` | electronic voices | `timbre=electronic` | 3: MMA, Roland, Yamaha | D05 §3.1; D10 §2.4 |
| `PROC` (processed/produced acoustic) | 70 `SNARE PROC` + 64 `KICK PROC` + 16 `TOM PROC` + 20 `CYMBAL PROC` + 6 `CROSS STICK PROC` + 9 `HI-HAT PROC` | **NONE** — "neither `acoustic` nor `electronic`… 140+ instruments have nowhere to go" | 1: Roland | D10 §2.4, §3.2 item 14, §5.1 |
| `FIXED ELEC` | electronic hi-hat "whose openness does not track the pedal" | **NONE** — a timbre×openness interaction v0.1 treats as independent axes | 1: Roland | D10 §2.4 |
| `SD FM` / `BD FM`, `SY CHIP`, `UT NOISE` | Elektron machine names | `timbre=fm` / `chip` / `noise` | 1: Elektron | D10 §3.1 |
| `machine` (`BD HARD`, `CY RIDE`) | Elektron's word for a sound-generation model | **NONE** — "a timbre/instrument conflation in one token" | 1: Elektron | D10 §4 |
| `Room` / `Power` / `Jazz` / `Brush` / `Orchestra` set names | GM2's nine sets, seven of which differ only in this | `voicing=room/power/jazz/orchestra` | 3: MMA, Roland, Yamaha | D05 §2.3, §2.6, §2.7, §3.1 |
| `LoFi Snare`, `Cowbell Lo-Fi`, `Crash Cymbal 2 Dark`, `Kick Soft Dark` | | `voicing=lo-fi` / `dark` | 2: Roland, Yamaha | D05 §3.1 |
| `Snare Dry`, `Kick Dry Tight` | Yamaha's room/mic property | `voicing` — **no `dry` value** | 1: Yamaha | D05 §3.3 |
| `Hybrid 2021 K`, `Vintage1 22" K` | Roland instrument names | `voicing` — no `vintage`/`hybrid` values | 1: Roland | D10 §5.1 |
| `[55]` / `[88]` / `[Pro]` | "this is the sound the *older device generation* made"; four generations of one closed hi-hat in one set | **NONE** — provenance-by-device-generation, neither `voicing` nor `timbre` | 1: Roland | D05 §2.6, §3.2, §5.0 gap 8 |
| `Analog` (GM2 ANALOG set) | = Roland TR-808, by Roland's own equivalence table | `timbre=analog-808` | 1: MMA/Roland | D05 §2.6 |
| `Analog Kit` (XG) | Yamaha's own analog-**modelled** voices, *not* 808 samples | `timbre=electronic`, **not** `analog-808` | 1: Yamaha | D05 §4.5 |
| `Size` 1.0–40.0, `Thickness` THIN-5…THICK+5, `Shell Depth` 1.0–30.0, `Head Type (CLEAR, COATED, PINSTRIPE)`, `Mic Distance`, `Mic Size`, `Kit Resonance`, `Overtone`, `Ping Color (LIGHT2…HEAVY2)`, `Ping Level` | Roland's per-instrument physical build parameters | **NONE** (`Mic Distance`/`Mic Size` are the only ones `voicing` half-covers) | 1: Roland | D10 §2.4, §3.2 item 10 |
| `profile`, `taper`, `weight`, `thickness`, `size`, `bow`/`curvature`, `lathing`, `tonal grooves`, `hammering` (random/symmetrical/hand/machine), `sandblasting`, finishes (`brilliant`, `natural`, `raw`, `dark`, `smoked bronze`), alloys (`B8`, `B10`, `B12`, `B20`, `MS63`, `FX9`) | the cymbal industry's build vocabulary | **NONE** — "neither instrument identity… nor `voicing` as currently defined" | 4: Zildjian, Paiste, Sabian, Meinl | D06 §2.1, §2.5, §3.2 Group 1, §5.6 — **the bucket's headline finding** |
| Evans head technology: `Level 360`, `Control Ring`, `Dry Vents`, `Reverse Dot`, `Power Center`, `SST`, `Hydraulic`, `UV Coating`, ply count, coatings (Coated/Frosted/Calftone/Hybrid/Mesh), model names (Genera, HD, ST, G1, G2, G12, Onyx, UV1, UV2, EC, Heavyweight, Calftone, dB Zero) | drumhead build vocabulary | **NONE** | 1: Evans/D'Addario | D06 §2.6 |
| `Mil` (thousandths of an inch) | drumhead thickness unit | **NONE** | 1: Remo | D06 §2.6 |

## 1.9 `dynamic`

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Snare Soft` / `Snare` / `Snare Tight`; `Kick Soft` / `Kick` / `Kick Tight` | a **dynamic ladder addressed by note number**, not three snares | `dynamic=soft/normal/hard` | 1: Yamaha (XG) | D05 §2.7, §3.1 |
| `Gengari p` / `Gengari f`; `Jing p` / `Jing f` | dynamic markings **inside the sound name** | `dynamic=soft/hard` | 1: Roland (GS ASIA) | D05 §2.6, §3.1 |
| Layers **A–D** with velocity ranges, per trigger input source | "you can set the velocity range to each layer so that you can play a different voice in response to the strength of each strike" | **NONE** — a fifth addressing level; `dynamic`'s labels are qualitative, not a velocity-range partition | 1: Yamaha (+ Oberheim DMX "three volume levels", 1981; DLS `RangeVelocity`) | D10 §2.5, §3.2 item 4; D05 §2.9 |
| `ACCENT` (TR-808 `AC`) | a global accent track | `dynamic=accent` | 1: Roland | D10 §2.11 |
| `Velocity Curve` (Linear, Log, Exp) | | **NONE** — a per-device transfer function | 1: Alesis | D10 §2.10 |

## 1.10 Controllers, structural data and identifier practice

| Term | Meaning | Axis | Traditions | Locator |
|---|---|---|---|---|
| `Hi-Hat Pedal CC` — assignable to `OFF, 1, 2, 4, 11, 16, 17, 18, 19` | pedal position; **"CC4 is the default but is not privileged"** | `controllers.hihat.pedal_position` | 1: Roland | D10 §2.3 |
| CC4 fixed, "MIDI Ch 10 only" | Yamaha **fixes** it | same controller, incompatible normativity | 1: Yamaha | D10 §2.6 |
| CC16 = "location of the strike on the Snare", CC17 = "…on the Ride" | fixed positional CCs | `controllers.strike_position.radial` | 1: Yamaha | D10 §2.6 |
| `CC MAX: 90, 127` | "amount of control change transmitted in stepping the pedal down completely" — **a setting, not a constant** | qualifies `hihat.pedal_position` | 1: Roland | D10 §2.3, §5.3 item 6 |
| positional CC "**directly afterwards on the same note channel**" | the CC is a **prefix qualifier on the next note-on**, not free-running | schema requirement, no axis | 1: Roland | D10 §2.3, §5.3 item 5 |
| `Pedal Bend Range −24…+24` semitones, per pad, head and rim separately | the hi-hat pedal is a **pitch controller for every other pad** | **NONE** | 1: Roland | D10 §2.4, §3.2 item 12 |
| `HH Pitch Up: off/on` | the same phenomenon as a boolean | **NONE** | 1: Yamaha | D10 §2.6, §3.2 item 13 |
| `PAN` (GM2 App. B, 62 values) / `Recommended Pan Position` ("Left 23%", "Center") | normative default stereo placement per sound | **NONE** — related to `instance` but stated for percussion that has no instance | 1: MMA (3 documents) | D05 §2.3, §2.4, §3.2, §5.0 gap 5 |
| `[L]` / `[R]` prefixes, `STANDARD L/R`, `BRUSH 2 L/R` | stereo-split kits addressing the halves of one instrument separately | **NONE** — "neither `instance` nor `limb`" | 1: Roland | D05 §2.6, §3.2, §5.0 gap 14 |
| `E` (number of elements) column; `*` "tones created using two voices" | polyphony cost per articulation | **NONE** — normative per-sound data | 2: Yamaha, Roland | D05 §3.2 |
| `Profile Details Discovery Bitmap` byte/bit per sound | a permanently assigned bit by which a device reports **which of the 62 sounds it has** | **NONE** — "a stable numeric identifier for a percussion sound issued by the MMA in 2025 — the closest thing to a KITWARP pivot id that any standards body has ever minted" | 1: MMA | D05 §2.4, §3.2, §5.0 gap 3 |
| MMA SysEx ID table (807 allocations) | no row is vacant, withdrawn, reassigned or reused; three `Reserved` holes; dead companies still hold IDs | **precedent for ADR-0003**; "never reassigned" is an inference from contents, **UNVERIFIED** as a quoted rule | 1: MMA | D05 §2.10 |
| `<Note Number="" Name="">` (MIDINameDocument DTD) | the industry's only cross-DAW percussion-naming interchange format is **a flat int→string map with one grouping level and no schema for what the string means**; canonical DTD URI returns **HTTP 404** | **NONE** — the anti-model | 1: MMA | D05 §2.8 |
| `Trig Type` capability matrix (`Rim shot | Bell shot | Positional sensing (Head|Rim) | Choke play`) per pad model | which playing methods a given pad supports | **NONE** — a capability matrix on the layout slot | 1: Roland | D10 §2.2, §5.3 item 4 |
| Per-voice flags `(*1) RealAmbi`, `(*2) position sensing for head shots and open rim shots`, `(*3) position sensing for bow shots` | positional sensing is a **property of the sampled voice**, not only of the pad | **NONE** | 2: Yamaha (machine-readable), Roland (informal) | D10 §2.5 |
| HPD-20 flag `*p` | "instruments whose sound varies depending on the location of your strike (M1 and M2 pads only)" | **NONE** — same capability shape | 1: Roland | D10 §2.17 |
| Zones **A / B / C** | ATV's abstract zone *index*, mapped to physical names per instrument type ("Head (Bow)", "Rim (Edge)") | **NONE** — an ordinal slot distinct from the site name | 1: ATV | D10 §2.8, §3.2 item 5 |
| 2Box `PERC 1–5` channels carrying rim zones | "the zone is not an attribute of the drum channel; it is a different channel" | **NONE** — "a 2Box layout cannot be read as instrument + site without the channel table" | 1: 2Box | D10 §2.9 |
| "A Device is not required to be able to play all of the listed sounds"; "may include extra sounds assigned to Note Numbers 0–26 and 89–127" | open-namespace mandate | **confirms** `instrument` must be an open registry | 1: MMA (+ Roland actually using 0–127) | D05 §2.4, §5.0 |
| "that name implies at least a **musical role**… a Device may substitute a sound… intended in context to fill a similar role" | the 2025 MMA position: **define role, refuse to define timbre** | `role` — v0.1 carries it as an optional non-identity annotation only | 1: MMA (M2-125-UM §4.1) | D05 §2.4, §5.5 |

## 1.11 Sound-character vocabulary (a whole layer with no axis)

| Term set | Count | Axis | Traditions | Locator |
|---|---|---|---|---|
| Sabian's glossary: `sustain, wash, dry, cut, attack, warm, dark, bright, trashy, clean, shimmering, explosive, mellow, focused, rich, raw, complex, controlled, glassy, buttery, sizzle, pangy, responsive, fast, slow, bouncy, dead, sloshy, tight, loose` | 30 defined terms | **NONE** — "retrieval facets for choosing a product, not properties of a struck event". Three have leaked into v0.1: `dark` (voicing), `tight`/`loose` (openness) | 1: Sabian ("the only major publishing a formal glossary with definitions") | D06 §2.3, §3.2 Group 2 |
| Paiste's Cymbal Sound Classification System: `Size and Thickness, Weight, Volume, Color, Frequency Range, Frequency Mix, Attack/Stick Sound, Response Intensity, Sustain, Bell Character, Hi-Hat Chick Sound, Feel` | 12 published parameters with scales | **NONE** — but `Bell Character` and `Hi-Hat Chick Sound` are "the vendor origin of the library articulation names `Bell` and `Chick`" | 1: Paiste | D06 §2.2 |
| Evans's four spectra: Attack (Balanced→Defined), Tone (Dark→Bright), Sustain (Short→Long), Durability | 4 | **NONE** | 1: Evans/D'Addario | D06 §2.6 |
| `Ping` | "the bright sound of the stick's impact"; Paiste's attack scale "Pronounced/Pingy to Spread/Washy" | **a sound quality** — v0.1 mints `technique=ping-shot` | 3: Thomann, Meinl, Paiste | D06 §2.4, §4 |
| `Wash` | Sabian: "the characteristics of sound following the attack… the sound during the sustain"; Thomann: "the darker underlying roar" | **a sustain property** — v0.1 puts `wash` on `ornament`, whose stated purpose is "grace or multi-stroke qualifier, with an attack count". **"A wash has no attack count."** | 2: Sabian, Thomann | D06 §2.3, §2.4, §4 |
| Player carriage and grip: `Garfield Grip`, `Set`, `Hip Rest`, `Gumption`, `Vertical`, `Flips`, `Lock Style`, `knee-and-fist` | 8 | **NONE** — "these describe the performer's body"; `limb` does not fit them either | 2: Zildjian, Vic Firth | D06 §3.2 Group 4 |
| Hardware parts never struck: `lug casing`, `tension rod`, `badge`, `air hole`/`air vent`, `butt plate`, `tube posts`, `sound posts`, `removable feet`, stand/rack names | 9+ | **NONE** — correctly unmapped, construction not contact | 1: Yamaha-education | D06 §2.9, §3.2 Group 3 |

## 1.12 Multi-language zone terminology (vendors' own translations)

| English | German (2Box) | French (2Box) | Note | Locator |
|---|---|---|---|---|
| head | `Fell` | `tête` | | D10 §2.7 |
| rim | `Rim` (untranslated) | `bord` | | D10 §2.7 |
| edge | `Rand` | `bord` / `bordure` | **`bord` is used for both rim and edge on the same page** | D10 §2.7, §4 |
| bow | `Fläche` ("surface") — **not** `Bogen` | `arc` in one place, `archet` in another | "`archet` is a violin bow… a vendor error"; "a German corpus search for `Bogen` will miss 2Box entirely" | D10 §2.7, §4 |
| bell | `Kuppe` ("dome, cap") | `cloche` | | D10 §2.7 |
| foot | `Fuß` | `pied` | | D10 §2.7 |
| hi-hat | — | `charleston` | | D10 §2.7 |
| cymbal parts (Thomann DE) | `Kuppe`, `Rand`, `Bogen`, `Loch`, `Profil` | — | Thomann-DE **does** use `Bogen` where 2Box uses `Fläche` — two German renderings, one language | D06 §2.1 |

---

# 2. NO-AXIS TERMS, grouped by the missing thing

## A. A missing **undirected exclusion class** — the single largest structural gap

`[EXC1]`–`[EXC8]`, `MES 1–7`, `Alternate Group 1–4`, `usKeyGroup 1–15`, TR-727 pair
exclusion, `MUTE SEND`/`MUTE RECEIVE`, `AltGroup S / R / S&R`, `Mono/Poly`, Elektron voice
coupling, `Hoo`-for-cuica reuse of an exclusion pair.

What is missing: v0.1 has `relations.choke` (directed: "damps the last event on the referenced
instrument") and `relations.open-close`. Every source here instead declares **an equivalence
class over terms** — "these N sounds are one physical object and only one may ring" — and it is
the class that makes `openness` and `damping` mean anything. Five standards encode it
(D05 §5.0 gap 1) and four vendors implement **four structurally different relations**
(D10 §2.14): directed with a self-mute exemption (Roland, per zone, 8 groups), directed-with-
explicit-symmetric-option (Yamaha `S`/`R`/`S&R`, per layer, 32 groups), self (Yamaha
`Mono/Poly`), and hardware-fixed directed (Elektron). D10 §5.3 states the minimum viable shape:
group id + role in `{send, receive, both}` + a `configurable` boolean + granularity in
`{zone, layer, track, voice}`. The TR-727 (D10 §2.13) is the undirected case in a 1985 primary
source, and there the exclusion is created **by an axis value**: `MUTE HI CONGA` / `OPEN HI
CONGA` is a `damping` pair that shares a voice circuit.

## B. A missing **duration / gate** property

`Rcv Note off = O` (XG: Brush Swirl, Brush Tap Swirl, Snare Roll, Samba Whistle H/L, Guiro
Long); GM1 Developer Guidelines' long whistle and long guiro; GM2 §2.8.1's ORCHESTRA 88 and
SFX 47–84; M2-125-UM's "for most sounds, the Receiver should play the whole life cycle…
regardless of the timing of a Note Off"; HPD-20 flags `*l` and `*n`; `Trigger Mode: GATE/ALT`.

What is missing: a boolean (or small enum) saying **whether note length is meaningful for this
articulation**. Three MMA documents state it independently of Yamaha, and Yamaha's six gated
sounds "are all sustained, player-controlled-duration articulations" — a normative statement of
which percussion articulations are *gestures with a duration* rather than one-shots. `*n`
("also sounds at note-off") is worse: a term whose realisation has two attacks bracketing a
held gate, which no axis expresses. (D05 §2.2, §2.3, §2.4, §2.7, §3.2, §5.0 gap 2; D10 §2.17,
§3.2 item 20.)

## C. A missing **spatial placement** concept, and a conflict with `instance`

GM2 `PAN` (62 normative values), GM Lite's PAN, M2-125-UM `Recommended Pan Position`,
Roland `[L]`/`[R]` stereo-split kits, `STANDARD L/R`.

What is missing: default stereo placement per sound — "related to `instance` but not derivable
from it, and stated for hand percussion that has no `instance` at all". Worse, D05 §4.4 shows
the MMA tables are laid out in the **audience's** view (pitch ascends left to right; hi-hat
Right 32%, ride Left 31%) while `reference_axes.instance` fixes "left to right **from the
player's seat**". An exporter deriving pan from `instance` produces a stereo image mirrored
against every MMA percussion table. `[L]`/`[R]` is a third thing again: the two halves of one
instrument, neither `instance` nor `limb`.

## D. A missing **build / construction** layer

Cymbals: profile, taper, weight, thickness, size, curvature, lathing, tonal grooves, hammering
(random/symmetrical/hand/machine), sandblasting, finishes, six alloys. Drumheads: ply count,
coating type, mil, collar, all Evans technology names. Sticks: wood, taper, tip shape, tip
material. Roland's module parameters: `Size`, `Thickness`, `Shell Depth`, `Head Type`,
`Sizzle Type`, `Ping Color`, `Mic Distance`, `Mic Size`.

What is missing: D06 §3.2 Group 1 states the choice — "either an axis is missing, or `voicing`
must be widened from 'kit or miking variant' to 'build or model variant of the same
instrument'." Four independent cymbal makers publish this vocabulary and libraries ship the
results as distinct kit pieces. Roland proves the same shape is needed on the module side.
D10 §3.2 item 9 adds the specific case: v0.1 encodes sizzle as an **instrument**
(`sizzle-ride`) while Roland models it as a parameter of *any* cymbal with three named
mechanisms.

## E. A missing **sound-character / retrieval** layer

Sabian's 30 terms, Paiste's 12 parameters, Evans's 4 spectra, `ping`, `wash`, `dry`, `dead`.

What is missing: a decision. D06 §3.2 Group 2: "three have nevertheless leaked into
pivot-shaped vocabulary… The leak should be deliberate: either the sound-character vocabulary
is out of scope entirely, or it is a named axis. **Half-adopting three of thirty is the current
state.**" `dark` sits on `voicing`; `tight` and `loose` are `openness` anchors; `dead` is a
`technique`; `wash` is an `ornament`. All four are Sabian/Paiste product-description words.

## F. A missing **capability / gating** layer on the layout slot

Roland's `Trig Type` matrix per pad model; the **rubber-vs-mesh** split that decides whether
`Rim Shot` exists at all; "cross-stick is possible only for SNARE"; "bell shots are possible
only for RIDE"; "brush sweep can be used only SNARE"; Yamaha's per-voice `(*2)`/`(*3)`
position-sensing flags; HPD-20 `*p` and `*h`; Yamaha's `RealAmbi` `(*1)`.

What is missing: "an axis of the *layout slot*", not of the term (D10 §3.2 item 6, §5.3 item 4).
Roland publishes exactly this table for every pad it sells. The `*h` flag is the sharpest case:
**openness is a per-instrument capability granted to instruments that are not hi-hats**, while
v0.1's `openness` is implicitly a hi-hat property.

## G. A missing **layer / velocity-range** level, and a missing zone *index*

Yamaha layers A–D with per-layer velocity ranges and per-layer `AltGroup`; Oberheim DMX's
"three volume levels" and "three individual pitches" per voice card (1981); DLS
`RangeVelocity`; ATV zones A/B/C; 2Box's rim zones routed through `PERC` channels.

What is missing: two distinct things. (1) A fifth addressing level below the zone —
`Inst → trigger input source → layer A–D → voice` — where `dynamic`'s five qualitative labels
are not a velocity-range partition. (2) An **ordinal zone slot** distinct from the zone name;
ATV states the mapping in one table and says explicitly that head↔bow and rim↔edge are the same
slot under two names. Without it an ATV or 2Box layout cannot be read at all.

## H. Missing **continuity** where v0.1 has a boolean or an enum

`SNAPPY` (continuous snare wires, 1980); `Strainer Adj. LOOSE1-3/MEDIUM1-3/TIGHT1-3` and
`Wire Level −6…+6`; `Pressure Sens` and `Fixed: PRESS` (pedal pressure **below** fully closed);
`choke_amount` on poly aftertouch with **no `technique=choke` to attach it to**; `Ping Color`;
the rute's adjustable band; `Position Area` (a calibration window that makes `position` relative);
`Pedal Curve`, `Offset`, `FootClosePos`, `CC MAX` (openness is not comparable across modules).

## I. A missing **pitch** dimension

GM2 ORCHESTRA's 13-note chromatic timpani run on notes 41–53 — "definite pitch on a percussion
instrument, **in a standard**"; `Bend Gong`, `Bend Talking Drum`, `Hu Yin Luo Low/Mid/High`;
`Berimbau Bend`; `Pedal Bend Range ±24` semitones on every pad; `HH Pitch Up`; DMX per-card
pitch shared by two instruments; LinnDrum tuning. (D05 §3.2, §5.0 gap 6; D10 §2.4, §2.15, §3.2
items 12–13.)

## J. A missing **transform-of-another-sound** modifier

`Reverse Cymbal` (GM2 ELECTRONIC note 52 — inside a standard) and 30+ `Reverse …` entries in GS
RHYTHM FX. "Not an instrument, technique, ornament or timbre." (D05 §3.2, §5.0 gap 7.)

## K. A missing **device-generation provenance** tag

Roland `[55]` / `[88]` / `[Pro]` — four generations of the same closed hi-hat in one set.
Not `voicing` (not a mic/room treatment), not `timbre` (not a different synthesis class).
(D05 §2.6, §3.2, §5.0 gap 8.)

## L. Missing **sites that are not the resonating body**, and missing **coupling**

`Ears` (djembe tuning rings), `Gourd` (berimbau), `Hole` (pot drum), `Paila`, `SideEdge`;
`Drumbal` ("a cymbal used **on a drum**", identity depends on being coupled to another
instrument); `Snare Buzz` (one drum's wires rattling from another drum); the hi-hat pedal as a
pitch controller for unrelated pads. Nothing in the axis model expresses **coupling between two
instruments**. (D10 §2.17, §2.4; D06 §3.2 Group 5.)

## M. A missing **harmonic** stroke, and a missing **direction**

`Harm` (Bendir) — "a mute-stroke kills the sound, a harmonic selects a partial".
`Cabasa Up` / `Cabasa Down` — two named sounds in GS; `technique=scrape` has no direction.
(D10 §3.2 item 17; D05 §3.3, §5.0 gap 13.)

## N. A missing **external-identifier** field, and missing **cost** data

M2-125-UM's `Profile Details Discovery Bitmap` (a standards-body-issued permanent numeric id per
percussion sound, 2025); Yamaha's `E` element count and Roland's `*` two-voice mark (what an
articulation costs a polyphony-limited device — SP-MIDI exists entirely because of it).
(D05 §2.4, §3.2, §5.0 gap 3.)

## O. Utility and non-instrument sounds

`Hi Q`, `Slap`, `Square Click`, `Metronome Click`/`Bell`, `Seq Click L/H`, `Click Noise`,
`Whip Slap`, `Finger Snap`, `Applause`, `Scratch Push`/`Pull`, `Scratch H`/`L`, Roland's
`ELEMENTS` and `CYMBAL OTHERS` groups. The `utility` family is reserved and unminted; only
`sticks` exists, and `sticks` is a false friend (§3). (D05 §2.3, §2.7, §3.2; D10 §3.2 item 16.)

## P. Correctly no axis, and must stay out

Player carriage and grip (Zildjian's `Garfield Grip`, `Set`, `Hip Rest`, `Gumption`,
`Vertical`, `Flips`, `Lock Style`; Vic Firth's `knee-and-fist`); hardware parts never struck
(`lug casing`, `tension rod`, `badge`, `air vent`, `butt plate`, `bearing edge`, `collar`).
D06 §3.2 Group 3 warns that `bearing edge` and `collar` "sound like sites and are not".

---

# 3. FALSE FRIENDS

## 3.1 One word, several meanings

| Word | Meanings | Locator |
|---|---|---|
| **`bow`** | (a) the playable middle **zone** of a cymbal — Meinl, and all four e-drum vendors; (b) the **curvature** produced by hammering — Paiste ("Curvature or Bow"); (c) a synonym for **profile** — Zildjian ("The profile or 'bow' of a cymbal"); (d) German `Bogen` is a *string-instrument bow*, and 2Box's own German avoids it with `Fläche` | D06 §2.1, §4; D10 §2.7, §4 |
| **`bell`** | (a) `site` — the raised centre boss of any cymbal; (b) `instrument` — Meinl's/Thomann's heavy small effect cymbal (`Bell-Becken`); (c) Paiste's classification parameter `Bell Character`; (d) separate instruments `Jingle Bell`, `Bell Tree`. **Both (a) and (b) are minted in v0.1 and "the vendor evidence confirms this collision is real trade usage, not a modelling error"** | D06 §2.4, §4; D10 §3.3, §4, §5.2; D05 §4.5 |
| **`rim shot`** | (a) a genuine acoustic rimshot — XG `Open Rim Shot` (34); (b) **the cross-stick** — Roland `CM Rim Shot` sits where GM puts `Side Stick`; (c) **striking a cymbal's edge sensor** — Roland lists `Rim Shot` as a playing method for HI-HAT and CRASH, "where the physical rim does not exist"; (d) TR-808 `RS`, a voice slot switchable to CLAVES | D05 §4.5; D10 §4, §2.2, §2.11 |
| **`open` / `closed`** | (a) hi-hat cymbal separation; (b) **rim-shot type** — Yamaha `SnareOp` = open rim shot, `SnareCl` = closed rim shot = **cross stick**; (c) conga hand technique (`MUTE`/`OPEN HI CONGA`); (d) Cakewalk's invented `Hand Cym.Closed` where Yamaha actually has `Hand Cymbal Short`, **a damped crash, not a closed one**. "Sense 2 is the trap." | D10 §4, §3.3; D05 §4.5, §5.4 |
| **`voice`** | (a) Yamaha: a per-zone sound within an Inst; (b) Oberheim DMX: a physical EPROM **card** holding up to two unrelated instruments; (c) Elektron: a physical analogue circuit, eight of them for twelve tracks; (d) TR-727: a numbered slot in a fixed list of sixteen; (e) Roland/Yamaha tone generators: a synthesis element counted in the `E` column. "The bucket task asked for 'VOICE terminology'; the answer is that the word does not denote one thing." | D10 §4, §2.15, §2.14, §2.13 |
| **`instrument`** | (a) Roland: **a sound**, an entry in the Instrument List; (b) Roland `Instrument group`: closer to KITWARP's sense but "mixes family with timbre (`KICK ELEC`)"; (c) Yamaha `Inst`: the percussion instrument on a trigger input, spanning several Voices; (d) KITWARP: the physical thing that makes the sound | D10 §4, §2.4, §2.5 |
| **`mute`** | (a) a **stroke type** producing a different sound (conga/cuica/triangle/surdo); (b) a **choke**, i.e. termination of a previous sound (`Mute Crash Cymbal`); (c) a mute *group* membership (`MUTE SEND`/`RECEIVE`) | D05 §4.5; D10 §2.14 |
| **`slap`** | (a) GM2 note 28 / SFX 40: an FX "slap" noise of no defined instrument; (b) `Conga Slap`, `Udo Slap`, `Brush Slap`: a hand or brush stroke. "Two unrelated senses in the same spec." | D05 §4.5 |
| **`sticks`** | (a) GM1/GM2 note 31: **two sticks struck together**, an instrument; (b) `implement=stick`: the beater. v0.1 mints `instrument=sticks` *and* `implement=stick` | D05 §4.5 |
| **`analog`** | (a) GM2 ANALOG = Roland TR-808, by Roland's own equivalence table; (b) XG `Analog Kit` = Yamaha's own analog-**modelled** voices. "The set name does not identify the machine." | D05 §4.5 |
| **`sizzle`** | (a) Sabian sound descriptor ("a slight buzzing or sustained shimmer"); (b) Zildjian product (rivets); (c) Zildjian marching **articulation** (`Sizzles`, `Sizz-Press`, `Sizz-Suck`, a sliding contact between two hand cymbals); (d) Roland `Sizzle Type` = a cymbal build parameter. v0.1 mints only `instrument=sizzle-ride` | D06 §4; D10 §2.4 |
| **`dead`** | (a) Sabian: "very short sustain, no lingering sound" — a **property of a cymbal**; (b) `technique=dead` — a dead stroke, a property of a **stroke** | D06 §4 |
| **`dry`** | (a) Sabian: shorter sustain; (b) Meinl: what hole cut-outs do to a cymbal; (c) Paiste/Evans: a response pole; (d) Yamaha `Snare Dry`: a room/mic property. All instrument properties, "yet library naming routinely turns 'Dry' into an articulation qualifier" | D06 §4; D05 §3.3 |
| **`tight` / `loose`** | (a) Sabian response qualities ("Sabian's 'tight' can describe a closed hi-hat *or* a focused crash"); (b) v0.1 `openness` anchors; (c) Roland `Strainer Adj. TIGHT/LOOSE` = **snare-wire tension**; (d) `Kick Tight` = a **dynamic** ladder step in XG; (e) v0.1 `stack.tight`/`stack.loose`, which set no `openness` at all | D06 §2.3, §4; D10 §2.4; D05 §2.7; `pivot.json` 1132/1133 |
| **`taper`** | (a) cymbal: thickness change from bell to edge; (b) stick: narrowing from shaft to bead. "Same word, two different objects, both in scope" | D06 §4 |
| **`flam`** | (a) the ornament; (b) Vic Firth hand-cymbal pedagogy: **a defect** — "all edges of the cymbals should touch at the same time, avoiding 'Flams'". Same word, opposite valence | D06 §4 |
| **`hi-hat`** | (a) the instrument; (b) Zildjian's marching **hand-cymbal technique** "Hi-Hat (flat position)" | D06 §4 |
| **`CY`** | (a) TR-808: one cymbal voice that is neither crash nor ride; (b) TR-8S: absent, replaced by `CC`+`RC`; (c) Elektron: a cymbal track whose machines include `CY RIDE` | D10 §4 |
| **`RS`** | (a) TR-808/Elektron: Rim Shot voice/track; (b) Roland `RT-30HR`/`RT-10S`: acoustic triggers; (c) Yamaha `Rm`: rim | D10 §4 |
| **`LT`/`MT`/`HT`** | (a) TR-808: **either** toms **or** congas, by panel switch; (b) TR-8S/Analog Rytm: toms only (+ Elektron's `BT`, with no counterpart anywhere) | D10 §4 |
| **`Half-Open Hi-Hat 1`/`2`, `Closed Hi-hat1/2/3`** | not openness degrees — "the suffix indexes **which kit's hi-hat sample**", parallel to `Standard 1 Snare 1` vs `Room Snare 1`. Dossier 03 read them as 10 openness steps; they are 4 states × kit index | D05 §5.3 |
| **`Hoo`** (`High Hoo`/`Low Hoo`, SC-88 DANCE, `[EXC4]`) | a **vocal sample** occupying the cuica's note numbers *and its exclusion group* | D05 §4.5 |
| **`bord`** (FR) | 2Box uses it for the snare **rim** and for the cymbal **edge** on the same page — "the distinction the English model depends on does not survive the vendor's own translation" | D10 §4 |
| **`archet`** (FR) | 2Box writes it for the cymbal bow; it is a **violin bow**. Vendor error, recorded so nobody treats it as terminology | D10 §4 |
| **`Ride Cymbal Low/Mid/High Inner|Edge`** | Inner/Edge is `site`; **Low/Mid/High is undefined** — "plausibly three ride cymbals, plausibly three dynamic layers". UNVERIFIED | D05 §3.2, §6 gap 6 |

## 3.2 Different words, one meaning

| Meaning | Spellings, by tradition | Locator |
|---|---|---|
| the cymbal's raised centre | `bell` (Roland, 2Box, Paiste, Meinl, MMA `Ride Bell`) · `cup` (Yamaha `Cp`/`RideCp`/`Ride Cymbal Cup`, ATV, Zildjian "bell or cup") · `Kuppe` (DE) · `cloche` (FR) | D10 §2.5, §2.8, §4; D05 §5A Q1; D06 §2.1 |
| the cymbal's playable middle | `bow` (Meinl + all e-drum vendors) · `ride area` (Zildjian) · `surface` (Paiste) · `Inner` (Roland GS) · `Fläche` (DE) | D06 §2.1, §3.1; D05 §2.6; D10 §2.7 |
| the cymbal's outer perimeter | `edge` · `crash area` (Zildjian) · `Rand` (DE) · `bord`/`bordure` (FR) | D06 §2.1; D10 §2.7 |
| stick laid across head to rim | `XSTICK` (Roland) · `SnareCl` / "closed rim shot" (Yamaha) · `Side Stick` (ATV, MMA) · `Cross Stick` (2Box, Roland's instrument group) · `CM Rim Shot` (Roland GS) · `SIDESTICK SNARE` (Linn). **No vendor writes `crossstick`** | D10 §2.1, §2.5, §2.8, §2.9, §5.2; D05 §4.5 |
| the bottom head | `resonant head` · `snare head` · `snare-side head` (Remo, Yamaha) vs v0.1 `underside` | D06 §2.6, §4 |
| the stick's striking end | `bead` (ProMark) vs `tip` (libraries, v0.1) | D06 §2.8, §4 |
| the stick's thicker mid-section | `shoulder` (ProMark) vs `shank` (libraries, v0.1) | D06 §2.8, §4 |
| bundled dowels | `rute` (Vic Firth, German trade word) vs `rod` (v0.1) | D06 §3.1, §4 |
| the quiet conga stroke | `Tap (T)` (Thomann, Meinl) vs `toe` (v0.1) vs `touch` / `toque de punta` (UNVERIFIED) | D06 §2.10, §4, §5.3 |
| snare wires disengaged | `snare strainer release` / `throw off` (the **part**, Yamaha) vs `wires-off` (the **state**, v0.1) vs `Strainer Adj. OFF` (Roland) | D06 §2.9, §4; D10 §2.4 |
| hand clap | `CP` (TR-808) vs `HC` (TR-8S/TR-909 lineage) — **both Roland**. "A converter keyed on the abbreviation will fail across the two families" | D10 §4 |
| pedal-closed hi-hat | `Pedal Hi-Hat` (MMA) · `HI-HAT PEDAL` (Roland) · `HhFtCl` / "Foot Close" (Yamaha) · `Foot` (ATV zone C) · `Closed/Chick` (Alesis) · `chick sound` (Paiste, Thomann) | D05 §2.1; D10 §2.1, §2.5, §2.8, §2.10; D06 §2.2 |
| the same 47 GM1 sounds | five MMA spellings across 34 years: `Closed Hi Hat`/`Closed Hi-hat`/`Closed Hi-Hat`; `Hi Mid Tom`/`High Mid Tom`; `Vibraslap`/`Vibra-slap`/`VibraSlap`; `Hi Bongo`/`High Bongo`; `Mute Hi Conga`/`Mute High Conga` | D05 §4.1 |
| a processed/produced acoustic sample | Roland `PROC` — no other vendor has a word for it at all | D10 §2.4 |

---

# 4. GAPS AGAINST v0.1

## 4.1 Minted with no source found in these three dossiers

| v0.1 item | File | Evidence of absence |
|---|---|---|
| `damping=towel`; terms `snare.towel` (1034), `tom.hit.towel` (1052) | `axes.json`, `pivot.json` | **Zero** hits for `felt`, `pillow`, `muffl*`, `Moongel`, `control ring` across all eight MMA/Roland/Yamaha documents (D05 §5A Q4); nine trade dampers listed by Thomann and `towel` is not one (D06 §2.7, §5.5); Roland's own enumeration is `TAPE/BLANKET/WEIGHT/DONUT/FELT` (D10 §2.4). "**`towel` is the odd one out and has no standards support**" (D05 §5A Q4); "v0.1's `towel` is one specific overlay damper elevated to a vocabulary value while `felt strip` and `pillow` have none" (D06 §5.5) |
| `technique=ping-shot` (term 1024), `gok-shot` (1025), `stick-shot` (1022) | both | `gok` = zero hits; `stick shot`/`stick-shot` = zero; `ping` only as an E.Piano voice and inside "comping" (D05 §5A Q3). "No vendor source reached in this bucket uses 'ping-shot', and none uses 'gok-shot' or 'stick-shot' either. **These are library words, not trade words**" (D06 §4). **But see §6: bucket 02/08 attest `stick-shot` in the orchestral and marching literature — these negatives are scope-limited.** |
| `technique=back-stick` (term 1023) | both | **Absent from all three of my dossiers.** Carried from late-findings item 1 — see §7 |
| `instrument=mini-china` (1123/1124), `mini-hihat` (1098/1099) | both | Absent from every MMA document and from Roland's and Yamaha's own tone-generator documentation; the standards' small-cymbal vocabulary is exactly `Splash Cymbal` and their china vocabulary exactly `Chinese Cymbal` (D05 §5A Q2). No vendor source in D06 §5.1. No e-drum module names them (D10 §2.4 lists `SPLASH`, `CHINA`, `STACKED CYMBAL` and no mini anything) |
| `instrument=xhat` | `axes.json` | No source in any of the three. (`stack` **is** sourced — Meinl, Thomann, Roland `STACKED CYMBAL`; D06 §2.4, D10 §2.4) |
| `site=underside` for cymbals | `axes.json` | "Nothing reached in this bucket names a cymbal **underside** strike as a vendor term" (D06 §5.7). It **is** sourced for drums (`resonant head`, and Roland `Pot Drum Bottom`) |
| `openness` anchors `closed-loose`, `quarter`, `three-quarter` | `axes.json` | "**No MIDI standard or vendor drum map in this bucket supports more than four** [openness states]" (D05 §5.3). Roland's V-Drums enumeration has six (`NORMAL, PRESS, CLOSE, HALF1, HALF2, OPEN`) and one of those is *below* closed (D10 §2.4) |
| `dynamic` five-value ladder | `axes.json` | Supported: XG's `Soft/normal/Tight` note-addressed ladder and GS's `p`/`f` naming give three; `ghost` and `accent` are not attested in these three dossiers (`ACCENT` on the TR-808 is a global track, D10 §2.11) |
| `mallet-soft/medium/hard` | `axes.json` | "v0.1's three-step soft/medium/hard was not corroborated by any reached vendor source; Thomann says only 'felt covered mallets'" (D06 §5.4) |

## 4.2 Misnamed, or on the wrong axis

1. **`ornament=wash` is on the wrong axis.** The `ornament` axis is documented as "grace or
   multi-stroke qualifier, with an attack count"; `wash` carries `attacks: 0`. Two vendors
   define `wash` as a **sustain property** ("the characteristics of sound following the
   attack"; "the darker underlying roar"). D06 §4: "**A wash has no attack count.** Either
   `wash` is on the wrong axis, or the ornament axis carries two different kinds of thing."
   Note it is doing a *third* job in `pivot.json`: `hihat.open-close.tip/edge` (1094/1095) use
   `ornament=wash` to mean **an open-close pedal gesture**, and `rules.json` degrades
   `wash → null` with the reason "no open-close gesture". One slug, three referents.
2. **`site=crossstick` is spelled the way no vendor spells it.** Roland `XSTICK`, Yamaha
   `SnareCl`, ATV `Side Stick`, 2Box `Cross Stick`, MMA `Side Stick`. Under ADR-0003 §5 clause 2
   this is fixed by a `correction`-kind alias set, never a rename (D10 §5.2 says exactly this).
3. **`site=bell` vs `instrument=bell`** — "the single most likely source of future confusion.
   It cannot be renamed. It needs a documented disambiguation rule" (D10 §5.2, §3.3). D06 §4
   independently confirms the collision is genuine trade usage.
4. **`technique=sidestick` and `site=crossstick` name the same gesture from two axes.**
   "Defensible, but no vendor separates them, so every vendor mapping will have to set both"
   (D10 §5.2).
5. **`damping` mixes an implement into an outcome scale.** "The standards model damping as an
   outcome on the `damping` axis and **never as an implement**" (D05 §5A Q4) — they name
   `Mute`, `Short`, `Gate`. Roland is the counter-case and names the *damper* (`TAPE`,
   `BLANKET`, `WEIGHT`, `DONUT`, `FELT`) with an amount. Either way `towel` alone is
   inconsistent. **Note also that ADR-0001's own facet table gives `damping` as
   `none, beater-strike, hand-strike, hand-after, body` (the PAL factoring: *what damps and
   when*) while `axes.json` ships `none, muted, damped, towel, gated` (an outcome scale).
   The ADR and the shipped axis disagree, and no dossier authorises the shipped version.**
6. **ADR-0001 vs `axes.json` on `mechanism`:** the ADR lists `wires-on, wires-off,
   kick-dampened, gated`; `axes.json` ships `wires-on, wires-off, kick-damped,
   kick-half-open` and has moved `gated` to `damping`. `gated` is a production process, not a
   damper (D06 §5.5) — but it **is** attested as a named sound class by two vendors
   (`Gated SD`, `Rim Gate 1-5`, `Kick Gate`, XG Electro; D05 §3.1). See §6.
7. **`instrument=sizzle-ride` puts a fitted accessory in the identity.** Roland models sizzle
   as a parameter of any cymbal with three named mechanisms (`RIVET`, `CHAIN`, `BEADS`);
   Zildjian sells rivets as an add-on (D10 §2.4, §3.2 item 9; D06 §2.1).
8. **`stack.tight` (1132) and `stack.loose` (1133) are minted from Sabian's sound-character
   vocabulary and carry no distinguishing facet.** Mechanically verified against
   `pivot.json`: `stack.loose` has **exactly the same facet tuple** as `stack.hit` (1121)
   `{instrument: stack, site: bow, technique: hit}`, and `stack.tight` has exactly the same
   tuple as `stack.mute` (1122) `{… damping: muted}`. Two id pairs whose identity is not
   determined by their facets — an ADR-0001 invariant violation ("a term is defined by a
   sparse tuple") and a validator target. The words themselves come from D06 §2.3.
9. **`reference_axes.instance` direction is contradicted twice.** GM2/M2-125-UM pan tables are
   audience-perspective, the mirror of the "player's seat" rule (D05 §4.4); Elektron names its
   toms `BT, LT, MT, HT` — **low to high**, the opposite direction (D10 §4). "UNVERIFIED that
   Roland's `TOM 1` is the highest tom; the Data Lists do not say."
10. **`controllers.hihat.pedal_position`'s note "Roland transmits 0-90" is true only by
    default.** Roland's `CC MAX` is `90` **or** `127`, a user setting; and the CC number itself
    is assignable to any of `1, 2, 4, 11, 16, 17, 18, 19` (D10 §2.3, §5.3 item 6). Yamaha fixes
    CC4/16/17 on channel 10 only. "A converter that hard-codes CC4 is wrong on a configured
    module."

## 4.3 Missing values and terms the sources demand

**`site`:** `cup` as a *correction/alternate* alias of `bell` (Yamaha, ATV, Zildjian);
a kick rim (`KickRm`, Yamaha); `paila`; `ears`; `hole`; `gourd`; `side`/`sideedge`;
`inner` if Roland's three-way hand-drum split is not v0.1's four-way one.

**`position`:** nothing missing in the four anchors, but a statement that they are
*relative to a configurable window* (`Position Area`), and Yamaha's "the location within a
zone" is the citation that `position ⊂ site` (D10 §2.6).

**`contact`:** tip **material** (wood vs nylon) has no home at all; `bead`/`shoulder` aliases.

**`technique`:** `choke` (five vendors name it; a controller exists for a technique that cannot
be named — D10 §3.2 item 2, §5.1); `harm`; a decision on `bell-shot` (`hit`+`site=bell`);
scrape/shake direction; `tap` as an alias of `toe`; `high slap tone` (cajon);
`glancing blow`; the tambourine friction rolls.

**`openness`:** an anchor **below** `tight` for pedal pressure (`PRESS`, `Pressure Sens`), and
a note that the transfer curve is vendor-configurable so scalars are not comparable across
modules (Alesis `Pedal Curve`).

**`damping`:** `blanket`, `weight`, `donut`, `felt`, `tape` (Roland's own value list);
`pillow`, `Moongel`, `damping ring`, `head overlay`, `duct tape`, `Snareweight` (the trade).

**`mechanism`:** graded snare-wire tension (`Strainer Adj.`, `Wire Level`, `SNAPPY` — all
continuous or 9-step, v0.1 is binary); `sizzle-rivet` / `sizzle-chain` / `sizzle-beads`;
a state for a **missing resonant head** (a concert tom — "a state no current axis can express",
D06 §5.2).

**`implement`:** `fist` (two traditions: Vic Firth + marching); `fingernail` (none here, but
absent from `axes.json` and named in the round-2 brief); `fleece` beater; brush materials;
tip material; the rute's adjustable band.

**`timbre`:** a value for **processed acoustic** (`PROC`, 140+ Roland instruments);
`analog-626`, `analog-dr110`, `analog-r8`.

**`voicing`:** `dry`, `vintage`, `hybrid`; and the §2D decision about widening it to build
variants.

**`instrument`:** `china-ride`, `flat-ride`, `trash-crash`/`-splash`/`-china`, `drumbal`,
hand-cymbal pairs (piatti), suspended cymbal; ~60 primary-sourced percussion names from the
HPD-20 Sound List and the TR-727 voice list, all from officially downloadable manufacturer
documents (D10 §5.4).

**Structural (not a value — a schema change):** the exclusion relation (§2A), the duration
property (§2B), pan (§2C), the capability matrix (§2F), layer and zone-index (§2G), the
external-id field (§2N).

## 4.4 What v0.1 gets right, with the source that says so

- **`controllers.strike_position.radial` has exact normative backing** — MPE RP-053 §3.3.5
  names a digital hi-hat's strike radius as the CC #74 use case. "KITWARP is not inventing
  this" (D05 §5.0).
- **`position` as a sub-property of `site`** — Yamaha's `Snare Position`: "tonal changes
  according to the location **within a zone** that is struck" (D10 §2.6).
- **`instrument` as an open registry rather than a closed enum** — forced by M2-125-UM's own
  clause allowing extra sounds on notes 0–26 and 89–127, and by Roland using the whole 0–127
  range (D05 §5.0).
- **The instrument/site split is named by a vendor** — Yamaha defines `Inst` ("each of the
  percussion instruments… used in a drum set") and `Voice` ("a sound that makes up an Inst…
  head shot, open rim shot, closed rim shot all from the same pad") as **not synonyms**.
  "This is exactly the KITWARP instrument/site split, named" (D10 §2.5).
- **`site=rim2`** matches Yamaha's `Pad14Rm1`/`Rm2` (D10 §2.5).
- **`technique=heel`, `toe`, `thumb`** now have a vendor citation for the first time
  (HPD-20 Sound List) (D10 §2.17).
- **Separating identity from note number** — GM2 puts `High Q` at 27 in STANDARD and 39 in SFX,
  `Castanets` at 85 in STANDARD and 39 in ORCHESTRA; Roland moves Castanets 85→27, Tambourine
  54→26, Crash 1 49→28 **inside one manual** (D05 §4.3).
- **`timbre` as an axis** — without it "every GM2 Analog, GS TR-808 and XG Electro source
  becomes indistinguishable from the acoustic set after a round trip"; Roland's `PROC`/`ELEC`
  suffix system is the same decomposition applied by a vendor (D10 §2.4).
- **Not aligning `hihat.pedal_position` to a standard** — "there is **no normatively defined
  MIDI controller for percussion strike position or for hi-hat pedal position**… That is a gap
  in MIDI, not in the vocabulary" (D05 §4.2, §5.0).

---

# 5. STRONGEST CLAIMS

**1. Five independent standards encode an *undirected exclusion class* and four vendors
implement four structurally different mute relations; v0.1 has only a directed `choke`.**
`[EXC1-8]` (GM2, GS), `MES 1-7` (M2-125-UM 2025), `Alternate Group` (XG), `usKeyGroup 1-15`
(DLS2), TR-727 pair exclusion (1985 primary source), Roland `MUTE SEND`/`MUTE RECEIVE`
(directed, per zone, with an explicit self-mute exemption), Yamaha `AltGroup S / R / S&R`
(directed **and** undirected in one field, per layer, 32 groups), Yamaha `Mono/Poly` (self),
Elektron voice coupling (hardware-fixed). *Why it survives:* it is the highest-severity gap in
both my normative and my hardware dossier, arrived at from disjoint corpora; it is what makes
`openness` and `damping` mean anything; and D10 §5.3 already states the minimum viable schema.
**D05 §3.2, §5.0 gap 1; D10 §2.13, §2.14, §5.3 item 1.**

**2. The bow/edge/bell zone triple is an e-drum-module and Meinl usage, not a cymbal-industry
standard, and it appears in no MIDI standard at all.** Zildjian — the largest cymbal maker —
publishes **`ride area`** and **`crash area`** as its zone names and uses "bow" only as a
synonym for *profile*; Paiste uses **`surface`** for the zone and "bow" for the hammered
curvature. Only Meinl uses the triple. Meanwhile the string `area` never names a cymbal region
anywhere in the MMA/Roland/Yamaha corpus, whose entire zone vocabulary is `Ride Bell` /
`Ride Cymbal Cup` / `Inner` / `Edge`. **Zildjian sat on the working group for the 2025 MIDI-CI
Default Drum Note Map Profile and the resulting standard contains no zone vocabulary of any
kind** (UNVERIFIED attribution: trade coverage, not the PDF). *Why it survives:* it tells an
importer that "ride area" and "bow" are the same `site`, and it shows the library convention
descends from one manufacturer, not from the trade. **D06 §2.1, §4; D05 §5A Q1.**

**3. The MMA cannot spell its own vocabulary consistently across 34 years — and the note number
is not stable either.** Five in-force MMA/AMEI documents publish the same 47 GM1 sounds under
five different sets of strings (`Hi Mid Tom`/`High Mid Tom`, `Vibraslap`/`Vibra-slap`/
`VibraSlap`, `Mute Hi Conga`/`Mute High Conga`); the 2025 profile adopted **Roland's**
spellings. Meanwhile `High Q` is note 27 in GM2 STANDARD and 39 in SFX, and Roland relocates
Castanets, Tambourine, Bell Tree, Crash 1, Snare Roll and Cabasa between sets **inside one
manual**. *Why it survives:* D05 calls it "the strongest available argument for ADR-0003", and
it is external evidence for the immutable-slug/opaque-id policy from the body whose names the
industry uses. **D05 §4.1, §4.3.**

**4. The industry's only cross-DAW percussion-naming interchange format is a flat int→string
map, and its canonical DTD URI is dead.** MIDINameDocument 1.0: `<Note>` has exactly two
attributes, `Number` and `Name`; `NoteGroup` adds one optional level of free-text grouping;
there is no attribute for instrument, articulation, site, technique, exclusion group, pan,
alternate group or note-off behaviour. `http://www.midi.org/dtds/MIDINameDocument10.dtd`
returns **HTTP 404**, so every `.midnam` in the wild has a DOCTYPE pointing at a dead URL.
*Why it survives:* it is the sharpest available statement of what KITWARP exists to replace,
in a format Pro Tools, Logic, Digital Performer and Ardour all read. **D05 §2.8.**

**5. `openness` is simultaneously over-specified above and under-specified below.** No MIDI
standard or tone-generator map supports more than **four** states (closed / half / open /
pedal), and D05 §5.3 shows the apparent "10 openness steps" in dossier 03 are four states
crossed with a kit-sample index. But Roland's V-Drums firmware names **six** (`NORMAL, PRESS,
CLOSE, HALF1, HALF2, OPEN`) and adds a continuous `Pressure Sens` dimension **below fully
closed** — "there is no room below `tight`". Add Alesis's `Pedal Curve` ("Log favors closed;
Exp favors open") and openness scalars are **not comparable across modules**. *Why it survives:*
it converts a vague "residual risk" into three concrete actions: justify or drop three anchors,
add a below-closed state, and record that the scalar is device-relative.
**D05 §5.3, §5.0 gap 4; D10 §2.3, §2.4, §2.10, §3.2 item 1, §5.3 item 7.**

**6. `choke` is named by every e-drum vendor, transmitted continuously by Roland, and has a
controller in v0.1 — but no `technique` value to attach it to.** Roland carries it as
**polyphonic key pressure keyed to the note number** ("the decay of the note sounded by the
received note number will be shortened based on the value"), not as a CC; 2Box, Alesis, Yamaha
and Elektron all name it; Roland's `Trig Type` matrix lists `Choke play` as a per-pad
capability. *Why it survives:* "a controller exists for a technique that cannot be named"
(D10 §3.2 item 2) — and this converges with extract B's independent claim 3 from the notation
side. **D10 §2.2, §2.3, §3.2 item 2, §5.1.**

**7. The vendor-normative controller behaviour breaks two assumptions the repository has
written down.** (a) **Order matters:** Roland's positional CC applies to "the note number
received **directly afterwards on the same note channel**" — it is a prefix qualifier on the
next note-on, not a free-running controller, and a converter that ignores this attaches the
position to the wrong note. (b) **CC4 is not privileged and 0–90 is not a constant:** Roland
lets the hi-hat pedal CC be any of `1, 2, 4, 11, 16, 17, 18, 19` and lets `CC MAX` be 90 **or**
127, while Yamaha *fixes* CC4/CC16/CC17 on channel 10 — so only Yamaha's is normative and the
two vendors agree by coincidence of default. *Why it survives:* both are one-line schema
consequences with a named primary locator. **D10 §2.3, §2.6, §5.3 items 5–6.**

**8. Roland's `PROC` suffix names a timbre class the model cannot express, on 140+
instruments.** `KICK PROC` (64), `SNARE PROC` (70), `TOM PROC` (16), `CYMBAL PROC` (20),
`HI-HAT PROC` (9), `CROSS STICK PROC` (6) — a *produced acoustic* sample that is neither
`acoustic` nor `electronic`. The same suffix system also yields `FIXED ELEC`, "a group that
exists **because** openness is not controllable for those sounds" — a timbre×openness
interaction v0.1 treats as independent axes. *Why it survives:* it is a single vendor, but it
is 185 instruments in one shipping product's Instrument List, and the fix is one axis value.
**D10 §2.4, §3.2 item 14, §5.1.**

**9. The MMA's 2025 position is that a percussion sound name denotes a *role* and its timbre is
deliberately undefined — which falsifies the claim that `role` has no analogue in any
standard.** M2-125-UM §4.1: "The tonal qualities or properties of each sound is not defined.
Each sound is defined in name only, although that name implies at least a musical role… A
Device may substitute a sound which is not identical to the name of the sound, if that sound is
intended in context to fill a similar role." *Why it survives:* ADR-0001's finding 4 ("`role` is
not identity", "four dossiers independently found no analogue… in any MIDI standard") now has a
documented counter-example, and **substitution-by-role is normatively sanctioned behaviour** —
which is exactly what `rules.json`'s curated edges do. The ADR's decision may still be right;
its stated justification is now partly wrong. **D05 §5.5, §2.4.**

**10. The manufacturer trade has a large, fully primary-sourced build vocabulary with nowhere
to go, and v0.1 has half-adopted three words from the *sound-character* vocabulary instead.**
Four cymbal makers publish alloy (B8/B10/B12/B20/MS63/FX9), hammering pattern, lathing, tonal
grooves, taper, profile, weight, thickness and finish; Roland ships `Size`, `Thickness`,
`Shell Depth`, `Head Type`, `Sizzle Type` and `Ping Color` as editable parameters. None fits
`instrument` or `voicing` as documented. Meanwhile `dark`, `tight` and `loose` — three of
Sabian's thirty *product-description* adjectives — are already axis values, and
`stack.tight`/`stack.loose` are minted with no distinguishing facet at all. *Why it survives:*
D06 states the choice cleanly ("either an axis is missing, or `voicing` must be widened…"), and
the half-adoption is a concrete, mechanically detectable defect. **D06 §2.1, §2.3, §3.2 Groups
1–2, §5.6; D10 §2.4; `pivot.json` 1121/1132/1133.**

**11. The TR-08 is not a witness to the TR-808, and other same-vendor lineage traps.** "The
1980 TR-808 has *one* LT slot that is *either* Low Tom *or* Low Conga, selected by a panel
switch. The 2017 TR-08 exposes LOW TOM and LOW CONGA as separate instruments with separate note
numbers… **Any layout derived from the TR-08 chart is not a layout of a TR-808.**" Same for
RS/CLAVES and CP/MARACAS. The Oberheim DMX is the extreme case: `voice` = an EPROM card holding
two unrelated instruments (`PERC 1` = tambourine + rimshot), so instrument identity is not
recoverable from the voice name. *Why it survives:* it is a rule for Phase 3 collection — the
reissue and the original are different devices — and it generalises to the SC-8850's reprinted
SC-55/SC-88 maps and to Evans/ProMark being one publisher. **D10 §2.11, §2.15; D05 §6.**

---

# 6. DISAGREEMENTS

## 6.1 Between my own three dossiers

**(a) Is `gated` a legitimate `damping` value?**
- **D06 §5.5:** "`gated` is a production process, not a physical damper, and sits in the same
  axis as `towel`. **No manufacturer sells or names a gate.** UNVERIFIED whether `gated`
  belongs on this axis at all."
- **D05 §3.1** maps `Gated SD`, `Gated Snare`, `Rim Gate 1-5` and `Kick Gate` (Roland GS,
  Yamaha XG Electro) straight onto `damping=gated`.
- **Both are right in their own scope and the recommendations differ.** No *accessory maker*
  sells a gate (D06's corpus is the accessory trade); two *tone-generator makers* ship named
  `Gated`/`Gate` sounds (D05's corpus). The open question is whether a named sound class is
  evidence for a *damping* value or for a `voicing`/production value. Name both dossiers; do
  not silently keep or drop the value.

**(b) How many openness states does Roland name?**
- **D05 §5.3** (Roland tone generators): "**GS names exactly four openness states — closed,
  half-open, open, pedal** — and everything else in that list is `voicing`, `timbre` or
  device-generation provenance."
- **D10 §2.4** (Roland V-Drums): `Fixed: NORMAL, PRESS, CLOSE, HALF1, HALF2, OPEN` — six
  anchors, one of them below closed.
- **Not a contradiction — a product-line split inside one manufacturer.** But an attestation
  count that says "Roland supports N openness states" is wrong without saying which line.

**(c) Are `ping-shot` / `stick-shot` unattested, or just not in the engineering layer?**
- **D05 §5A Q3** and **D06 §4** both return clean negatives, and D06 concludes "**these are
  library words, not trade words**".
- That conclusion over-reaches its corpus. See §6.2 — bucket 02 finds the stick shot in Read's
  orchestral treatise and bucket 08 finds it shipped in marching articulation lists. **Carry
  the negative as "absent from the MIDI standards and from manufacturer trade literature",
  never as "unattested".**

**(d) Is `fist` used by anyone?**
- **D10 §5.1** records under `implement`: "nothing missing found; `fist`/`fingernail` unused by
  these vendors".
- **D06 §2.11** publishes Vic Firth's tambourine `Fist strike` and `knee-and-fist`.
- Both true (e-drum vendors vs orchestral pedagogy), but D10's row would, read alone, suppress
  a term that has at least two independent traditions once bucket 08's Casey Claw is added.

## 6.2 Against claims I know other dossiers make

- **`back-stick` (late-findings item 1).** Bucket 01 reported it unattested; bucket 08 makes it
  the best-sourced term in its bucket, reaching back ~150 years. **My three dossiers contain no
  occurrence of the string at all** — it is absent from the MMA corpus, from every e-drum and
  drum-machine document, and from all manufacturer trade literature reached. That is a *fourth*
  scope-limited negative and it must be reported as such: **the engineering layer is not where
  this term lives.** It does not weaken bucket 08's evidence (Marrella, *Drum Corps World*
  Vol. 36 No. 15, Dec 2007; World Drum Corps Hall of Fame Dowlan bio; the Armstrong & Co.
  lithograph, NYPL `PC MUSIC-Dru`, Digital ID 832408; *Utica New York Observer*, 3 July 1878).
- **`stick-shot` / `ping` / `gock`.** D06 §4's "library words, not trade words" is contradicted
  for `stick-shot` by D02 (Read p. 198, "*Lay 1 stick on head of drum — strike with the
  other*") and by D08 (a shipped marching articulation), per extract A §6.3. For `ping` my
  dossiers add something the others do not have: **`ping` is a vendor *sound-quality* word**
  (Thomann, Meinl, Paiste's "Pronounced/Pingy" attack scale) and Roland ships `Ping Color` as a
  ride *parameter* — so `technique=ping-shot` mints a sound quality as a stroke. That supports
  bucket 08's finding that ping/normal/gock are one technique at three positions.
- **`zing`.** D06 §2.11 lists `Taps, Zings and Dings` and `Sizzles / Sizz-Press / Sizz-Suck` as
  Zildjian's own named marching hand-cymbal articulations. This is a **manufacturer** source and
  it is independent of the six institutional sources bucket 08 gives (extract B §6.3). It
  strengthens the correction of D04's earlier UNVERIFIED marking rather than contradicting it.
- **"`role` has no analogue in any standard"** (ADR-0001 finding 4, attributed to four
  dossiers). Falsified by M2-125-UM §4.1 (2025). D05 §5.5 states it explicitly: "the current
  MMA position is the *opposite* of what dossier 03 states".
- **Notation standards are one lineage** (extract B claim 2). My corpus supplies the exact
  parallel and it should be stated once for both: the five MMA spellings of the GM1 map are one
  lineage drifting, not five witnesses (D05 §4.1); and the SC-55/SC-88 maps used here are
  Roland's reprints inside the SC-8850 manual, not three documents (D05 §6).
- **Alias-building across languages** (extract B claim 7, on German register splits). D10 §2.7
  adds a harder constraint from the vendors' *own* translations: 2Box's German renders `bow` as
  **`Fläche`** while Thomann's German uses **`Bogen`**; 2Box's French uses `bord` for both rim
  and edge on one page and `archet` (a violin bow) for the cymbal bow. **A vendor's own
  translation is not a reliable alias source, and two German vendor renderings already
  disagree.**
- **`choke`** (extract B claim 3, from notation and orchestral sources). My hardware dossier
  independently reaches the same conclusion from five vendors plus a continuous controller —
  convergence from disjoint corpora, worth saying so.

## 6.3 Reliability warnings my dossiers make about their own rows

- **D05 §6:** the Yamaha **XG Format Specification** and the Roland **GS Format Specification**
  were never found in public form; everything in D05 §2.6–§2.7 is inferred from *product* data
  lists, so "whether the Alternate Group numbers are normative or per-product" is unresolved.
  The SC-88 manual has no text layer; the SC-55 manual was not reached; the 1999 GM2 original
  has no extractable text (v1.2a used instead, with the no-change claim resting on a changelog,
  not a diff). `Ride Cymbal Low/Mid/High` is unresolved. Wayback is unreachable; `archive.org`
  proper is not.
- **D10 §6:** the **Roland SPD-30 Octapad** has no documentation on roland.com at all (named in
  the task, the largest official gap); Roland's 808/909 **patents** were not obtained;
  **Pearl Mimic Pro** (403), **EFNOTE** (no answer) and **GEWA** (JS-only index) returned zero
  documents; Alesis yielded support articles but no PDFs. Every vintage drum-machine manual is a
  **third-party archive.org scan with no declared licence — worklist only, never a shipped
  source** (ADR-0004). The LinnDrum OCR is degraded and everything beyond its instrument names
  is UNVERIFIED; the TR-808 service-notes OCR is poor and component references should not be
  trusted.
- **D06 §6:** only **26 of 58** candidate sources were reached. Wayback was blocked, so every
  pre-2000 catalogue (Slingerland 1928/1936/1950/1968, Ludwig 1994) is unread — named as the
  single most authoritative source not obtained. **Latin Percussion published nothing textual**
  that was reachable, so the whole conga stroke table rests on **Thomann, a retailer (authority
  C)**, not on the manufacturer; the timbale terms `cascara`/`paila`/`abanico` are
  search-summary only. Vic Firth's rute/brush/beater rows and the five-part stick anatomy are
  **UNVERIFIED** (search text, not fetched pages). Spanish and Italian registers were never
  searched. **Licence verdict for the whole bucket: vendor marketing and education copy, all
  rights reserved — "none of this text may be shipped into `data/`".**

---

# 7. Late-findings checklist

| # | Item | In my three dossiers? | How carried |
|---|---|---|---|
| 1 | `back-stick` — bucket 01 said unattested, bucket 08 made it the best-sourced term (~150 years; Marrella 2007; Dowlan bio; Armstrong lithograph NYPL `PC MUSIC-Dru` / Digital ID 832408; *Utica NY Observer* 3 Jul 1878); bucket 01's negative was scope-limited | **No — the string does not occur in D05, D10 or D06** | Carried verbatim and reported as a **fourth scope-limited negative**: §4.1 row, §6.2 first bullet. The engineering layer is not where this term lives; this does not weaken bucket 08 |
| 2 | `rim shot` enters print between 1922 and 1937 (Bauduc, *Dixieland Drumming*, archive.org `RayBauducDixielandDrumming`, unrestricted), as a **dynamic accent device not a timbre**; explains Read's empty IT/FR/DE columns while `muffled` has eight synonyms; Krupa 1938 not on archive.org, so the shaft-between-head-and-rim definition stays **UNVERIFIED** | **No** — no dossier of mine reaches the 1912–1938 print record | Carried as stated. My dossiers add the *later* history of the same word: by the MIDI era it carries **four** incompatible senses (§3.1 `rim shot`), including Roland's `CM Rim Shot` = cross-stick and Roland's `Rim Shot` playing method on pads with no rim — consistent with a word that entered print undefined |
| 3 | Peinkofer & Tannigel's English translation is by Kurt and Else Stone ⇒ **Stone 1980 and P&T 1976 are one lineage**; any count treating them as two traditions is wrong | **No** — neither book is in my corpus | Carried. My corpus supplies four further lineage traps of the same shape, stated in "How attestations are counted": five MMA documents = one tradition; SC-55/SC-88 maps = one reprint; TR-08 ≠ TR-808; **Evans and ProMark are both D'Addario**; and a possible Vic Firth/Zildjian shared publisher (UNVERIFIED) |
| 4 | Read splits `Dampened` (stop after it starts) from `Muffled` (alter before it starts); v0.1 does not. Contents pp. XVI–XVII, body pp. 158–233 | **No** — Read is bucket 02 | Carried. My dossiers corroborate the *shape* of the problem from the engineering side: the MMA models damping **only as an outcome** and never names a physical damper (D05 §5A Q4 — zero hits for felt/pillow/muffle/Moongel/control ring), while Roland names the **damper and its amount** (`TAPE/BLANKET/WEIGHT/DONUT/FELT`) and D06 lists nine trade dampers. So the axis must carry *when it damps* (Read) **and** *what damps* (Roland) — and v0.1's five values do neither cleanly. §4.2 item 5 |
| 5 | `fist` has a marching source (Casey Claw: "held in a fist, where all the fingers wrap around the stick"); `fist` and `fingernail` are both in the round-2 brief and both absent from `axes.json` | **`fist` yes, `fingernail` no** | `fist`: **a second independent tradition** — Vic Firth's tambourine `Fist strike` and `knee-and-fist` (D06 §2.11). Also recorded: D10 §5.1 says `fist`/`fingernail` are "unused by these vendors", which read alone would suppress the term — flagged in §6.1(d). `fingernail`: zero attestation in my three dossiers; confirmed absent from `axes.json`. §1.6, §4.3 |
