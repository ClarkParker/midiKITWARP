# Reconciliation extract A — the Western stroke-and-ornament layer

Dossiers read in full:
- **D01** `docs/research/round2/01-rudiments-stroke-technique.md` (rudiment standards, stroke
  technique, brush and foot vocabulary, 1588–2019)
- **D02** `docs/research/round2/02-orchestral-treatises.md` (orchestration treatises and
  percussion-writing manuals, Berlioz 1843 → Solomon 2016)
- **D08** `docs/research/round2/08-marching-percussion.md` (marching snare, tenor, bass,
  cymbal line; MuseScore/Tapspace/Muse Drumline provenance)

Also read: `vocabulary/axes.json`, `vocabulary/pivot.json`, `vocabulary/rules.json`,
`docs/adr/0001-pivot-vocabulary.md`, `docs/adr/0003-identifiers-and-registry.md`, and the
late-findings file (all five items are carried; see §7).

## How attestations are counted here

An **independent tradition** is a body of practice with its own naming authority, not a
document. The traditions these three dossiers reach:

| Code | Tradition | Principal documents in these dossiers |
|---|---|---|
| T1 | American rudimental / military manual | Hart 1860, Nevins 1864, Strube 1870, Greissinger 1900, Gardner 1918, NARD 1933/1958, PAS 1984 |
| T2 | Swiss / Basel | Rudimental Codex (Hessler/Percussion Creativ) 2024 poster; Bloom; Trommelschule Basel |
| T3 | French military / conservatoire | Tourte 1946 via de Douvan; Gevaert 1885; Furetière 1690 |
| T4 | German percussion pedagogy | Peinkofer/Tannigel 1981 via de.wp; Berlioz–Strauss 1905; Tobischek 1977 via de.wp |
| T5 | Anglophone orchestral treatise | Read 1953, Forsyth 1914, Widor tr. 1906, Solomon 2016 |
| T6 | American dance-band / early kit | Straight 1922, Bauduc 1937, (Krupa 1938 unreached) |
| T7 | Jazz brush pedagogy | *Percussive Notes* brush anthology 1996–2004 (O'Mahoney, Hazilla, Soph, Hamilton) |
| T8 | American marching / drum corps practice | five university/corps technique packets, Blakley glossary, Udow via wp, Mirsky/Marrella |
| T9 | Marching **vendors** (not a tradition — a single commercial layer) | Tapspace VDL 2.5, Muse Drumline/MuseScore, MakeMusic/Finale |
| T10 | Scottish pipe band | only second-hand via en.wp *Drum roll* / *Drum rudiment* |
| T11 | Other national roll names (Dutch, Mexican, Spanish, Bajoaragonés, Eporedian) | one document only (en.wp *Drum roll*) |

Two cautions that change counts:

- **Stone 1980 and Peinkofer/Tannigel 1976 (EN) are ONE lineage.** The English *Handbook of
  Percussion Instruments* is translated by **Kurt and Else Stone**, the same Kurt Stone who
  wrote *Music Notation in the Twentieth Century*. D02 §6.2 and D02 §1.2 N5 state this
  explicitly. Their agreement is not corroboration.
- **Italian and Spanish rudiment lists are translations of the PAS 40, not independent
  witnesses** (D01 §2.13). They count as evidence of *spelling drift*, not of attestation.

---

# 1. TERMS

Every term the three dossiers establish. `v0.1` column gives the axis + value where one
exists, `NEW-VALUE` where the axis exists but the value does not, `NONE` where no axis fits
(cross-referenced to §2). Traditions counted per the table above; "1 vendor" is marked as
such and never merged into a tradition count.

## 1.1 `technique` — strokes on membranes

| Term as the source spells it | Physical meaning | v0.1 axis | Indep. traditions | Locator |
|---|---|---|---|---|
| Rim shot / rimshot | one stick strikes rim and head together; bead ~3 in (8 cm) from rim | `technique: rimshot` | 3 (T5 Read p. 200 "Rim shot — Shot"; T6 Bauduc 1937; T8 marching packets + Blakley) | D01 §2.7; D02 §2.6, §2.17; D08 §2.5 |
| Ping shot / Ping Rimshot | bead ~1 in (2.5 cm) from rim; high, metallic | `technique: ping-shot` | 2 (T8 SUU packet written above the stave, icanplaydrums; **plus 1 vendor** Tapspace VDL pp. 24–28 shipped articulation) | D08 §0, §2.5; D01 §2.7 |
| Gock / gawk (v0.1 `gok-shot`) | bead at **centre** of head while rim is struck by the distal shaft near the hand; lower sound | `technique: gok-shot` — **misspelt** | 0 traditions with a citation. Concept defined only in an **uncited** en.wp *Rimshot* paragraph; spelling `Gok` occurs in **one vendor**, Muse Drumline via MuseScore commit `c7dc55ea2d` | D08 §0, §2.5, §5.1.1; D01 §2.7, §5.1 |
| Full Shot | written contrast to Ping Shot on the same page of a corps packet; **UNVERIFIED** whether = normal rimshot | `technique` NEW-VALUE or alias | 1 (T8 SUU 2025 packet, fig. 25) | D08 §3.2 item 13 |
| Stick shot (orchestral "rimshot") | one stick laid on the head, shaft pressed against the rim, struck by the *other* stick | `technique: stick-shot` | 3 (T5 Read p. 198 "Lay 1 stick on head — strike with the other"; T8 marching + Blakley cross-stick sense 2; jazz/*Modern Drummer* Fidyk 2013) + SMuFL `pictStickShot` U+E7F0 + 1 vendor (VDL `Stick shot HIGH/LOW`) | D08 §0, §2.5; D02 §2.6; D01 §2.7 |
| Cross-stick = rim click = side-stick | tip held on head near a bearing edge, butt struck against the rim, hand muting | `technique: sidestick` + `site: crossstick` (**duplicated across two axes**) | 2 (T8 Blakley, marching; en.wp *Snare drum* naming all three in one sentence) + 1 vendor (VDL `Cross stick Rim Knock`) | D01 §2.7, §5.1; D08 §2.5, §3.1 |
| Rim knock | Tapspace's own word for the cross-stick-on-rim | `technique` NEW-VALUE (alias of sidestick/rim-only) | 0 traditions; 1 vendor (VDL) | D08 §5.2 |
| Rim click (marching bass) | strike on a **metal bar bolted to the rim** — not the rim | **NONE** — see §2 | 1 (T8, en.wp *Marching percussion* line 85) | D08 §2.6, §3.2 item 5, §5.1.3 |
| Rim-only | v0.1 coinage; **no reached source uses it** | `technique: rim-only` — unattested | 0 | D01 §5.1 |
| Back stick / backsticking | note played by swinging the **butt** of the stick over; a visual technique that sounds | `technique: back-stick` + `contact: butt` | 2 (T8 corps practice — Marrella *Drum Corps World* 36/15 Dec 2007, World Drum Corps Hall of Fame Dowlan bio, Mirsky's 1870s artefact; T1-adjacent iconography 1870s) + 1 vendor (VDL `RH/LH backstick`) | **D08 §2.5.1** (D01 §2.7 reports it NOT FOUND — see §6.1) |
| Skank (= muffled shot) | rimshot muffled immediately or after brief resonance; three fingers pressed hard into the centre of the head | `technique: rimshot` + `damping: muted` (composable) or NEW-VALUE | 1 (T8 Missouri State FA20) + 1 vendor (VDL `"Skank"`) | D08 §2.6, §5.2 |
| Spank | bottom drum rimshot followed by the opposite hand's fingers deadening it — actions **independent, not simultaneous** | `technique` NEW-VALUE | 1 (T8 Blakley) | D08 §2.6, §5.2 |
| Sweep (tenor) | double stroke split between two drums; sweeping/scraping motion | `technique: sweep` | 1 (T8 Rudimental University, Blakley, Missouri State "sweep playing zones") | D08 §2.6 |
| Scrape (tenor) | Rudimental University: interchangeable with sweep | `technique: scrape` | 1 (T8) — note collision with cymbal `scrape`, §3 | D08 §4 |
| Crossover — "stick cross" vs "arm cross" | one hand crosses the other; adjacent drums = sticks intersect at/in front of the fulcrum, non-adjacent = arm cross | **NONE** (motor system) | 1 (T8 Missouri State, Blakley) | D08 §2.6 |
| Helicopters / butterflies / figure eights | named crossover sweep patterns, named from the visual shape traced | **NONE** (pattern + choreography) | 1 (T8 Rudimental University) | D08 §2.6 |
| Stir (VDL `Drum n STIR w/dread`) | continuous stirring of a rod bundle on the head | `technique` NEW-VALUE (near `circling`) | 0 traditions; 1 vendor | D08 §5.2 |
| Friction slide (VDL `Friction Slide 1/2`) | stick dragged under friction across the head | `technique` NEW-VALUE | 0 traditions; 1 vendor | D08 §2.4, §5.2 |
| Stick snap | snap of the stick as a sound | **NONE** (equipment sound) | 0; 1 vendor | D08 §2.4, §3.2 item 4 |
| Coup de douille | French: stick reversed, head struck with the butt/ferrule | `contact: butt` + `technique: hit` | 1 (T3, de Douvan closing note ← Tourte) | D01 §2.7, §3.2 |
| Poing Stroke | 1864: "a sudden, **hard, short** beat" — a name for the stroke's **envelope**, not a pattern | **NONE** — no envelope/duration axis | 1 (T1 Nevins 1864 No. 8) | D01 §2.3b |
| Drawing stroke / "soft, long, drawing" | lateral, drawn stroke; Nevins's No. 10, **explicitly forbidden by Hart** four years earlier | **NONE** (envelope; and a documented conflict) | 1 tradition, 2 documents in disagreement (T1) | D01 §2.3b, §4.1 |
| Blow / Tap / Single Beat | 1860–1864 names for the plain single stroke | `technique: hit` | 1 (T1 Hart, Nevins) | D01 §2.3b, §4.2 |
| Lateral stroke (brush) | "Brushes generate sound with lateral (or horizontal) strokes across the texture of the drumhead" | `technique: sweep` | 1 (T7 O'Mahoney p. 20, Hamilton) | D01 §2.8 |
| Dead stroke | implement held down on the bar after contact | `technique: dead` | 2 (T5 Solomon pp. 75, 242; T8 body/dead tap) | D02 §2.14, §3.5; D08 §2.7 |
| Deadstick grace note (Scottish "drag") | grace note played staccato, stick not rebounding | `ornament` NEW-VALUE | 1 (T10, via en.wp) | D01 §2.4, §3.2 |
| Thumb / thumb roll | thumb rubbed across a tambourine or drum head | `technique: thumb` + `ornament: roll` | 3 (T5 Read p. 213, Forsyth p. 32, Widor p. 109 — three separate treatise authors) | D02 §2.7, §2.11, §2.12, §3.5 |
| Shake (hoop) | tambourine shaken, jingles sound | `technique: shake` | 2 (T5 Read p. 215, Forsyth p. 32, Widor p. 108) | D02 §2.7, §2.11 |
| Bowing / Tremolo with a 'cello bow | sustained friction excitation of a cymbal, crotale, bar or bar end | **NONE** — see §2 G10 | 2 (T5 Read pp. 179, 195; Solomon p. 244) | D02 §2.5, §2.8, §3.9 |
| Friction roll / "kept in vibration by friction on the edge" / rosined glove over a stick pressed to the head | continuous friction excitation, ≠ `scrape` (transient), ≠ `roll` (discrete attacks) | **NONE** — §2 G11 | 2 (T5 Read pp. 211, 219; Solomon p. 244) | D02 §2.5, §2.6, §3.9 |
| Rasped and beaten (`Raspato e battuto`) | scrape + strike on a reco-reco | `technique: scrape` + `hit` | 1 (T5 Read p. 221) | D02 §2.8 |
| Glissando across wood blocks / on the resonators / with a triangle stick describing an arc | `gliss` | `technique: gliss` | 1 (T5 Read pp. 179, 220, 225) | D02 §2.7, §2.8 |
| Pitch bending | | **NONE** (no v0.1 value; controllers may cover) | 1 (T5 Solomon pp. 123, 246) | D02 §2.14, §3.5 |
| Vibrato / slow vibrato | vibraphone motor rate | **NONE** | 1 (T5 Read p. 179; Solomon p. 247) | D02 §3.5 |
| Clusters / Sympathetic Resonance / Adding Mass / Prepared Instruments / Harmonics | | **NONE** — §2 G8, G9 | 1 (T5 Solomon pp. 245–250; Read p. 225) | D02 §2.14, §3.9 |

## 1.2 `technique` / `implement` — hand, body and the participants problem

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| With the hand / `colla mano` / `Mit der Hand` | | `implement: hand` | 2 (T5 Read pp. 184, 215; Forsyth) | D02 §2.5, §2.7 |
| With the fingers / fingertips; roll with the fingers | | `implement: finger` + `ornament: roll` | 2 (T5 Read pp. 200, 215, 222; Forsyth p. 36 finger-tip diminuendo) | D02 §2.5–2.8, §2.11 |
| **With the fist / `Col pugno` / `Mit der Faust`** | fist as the striking body | `implement` **MISSING** — §2 A4 | 2 (T5 Read p. 214; T8 Casey Claw grip "held in a fist, where all the fingers wrap around the stick") | D02 §2.7, §3.5, §5.1; **D08 §2.5.1, §5.2**; D01 §5.2 |
| **With the knuckles / `Colla nocce` / `Mit den Knöcheln`** | | `implement` **MISSING** | 2 (T5 Read p. 216; Forsyth p. 32) | D02 §2.7, §3.9 G4 |
| **With the fingernails / `Colle unghie` / `Mit dem Nagel`** | | `implement` **MISSING** (`fingernail` is in the round-2 brief, absent from `axes.json`) | 1 (T5 Read p. 164) | D02 §2.4, §5.1; D01 §5.2 |
| **On the knee / `Frappez sur le genou` / `Mit dem Knie`** | the *instrument* is struck **against the player's body** | **NONE** — §2 G3 | 1 (T5 Read p. 214; Philharmonia corroborates prose) | D02 §2.7, §3.9 |
| Palm Up (Philly Joe Jones) | right brush turned "like turning on the ignition", wires flicked off the head to palm-up, "resulting in a snap" | `technique` NEW-VALUE | 1 (T7 Hamilton p. 18 ← Jones *Brush Artistry*) | D01 §2.8 |
| Tips vs fan (brush) | accents made by pressing more of the brush **fan** onto the head; unaccented on the **tips** | `contact` **MISSING** value `fan` | 1 (T7 Soph p. 30) | D01 §2.8, §3.2, §5.2 |
| Grip point ("grip the brush two inches from the wires") | | **NONE** (grip) | 1 (T7 Hazilla p. 32) | D01 §2.8 |

## 1.3 `technique` — foot

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| Heel-down | heel on the footboard, ankle is the pivot | `technique: heel` (but see §4) | 1 (kit pedagogy via en.wp) | D01 §2.9 |
| Heel-up | heel raised, leg mass drives the stroke | `technique: toe`-adjacent | 1 | D01 §2.9 |
| **Heel-toe** | **two attacks from one leg motion**; despite the name "it's the ball of the foot (or toes) both times" | **NONE** as a technique value — it is a 2-attack ornament + a motor system | 1 (weakly sourced en.wp *Heel-toe technique*) | D01 §2.9, §5.1 |
| Slide | heel-up variant; after stroke 1 the toes slide up the footboard and press again | **UNVERIFIED** — search-summary only | 0 confirmed | D01 §2.9, §6.3 |
| Swivel | heel moves laterally without the ball leaving the board | **UNVERIFIED** — search-summary only | 0 confirmed | D01 §2.9, §6.3 |
| Foot chick / "chick" | pedal closes the cymbals with no stick; short muted "chick" | `technique: chick` | 2 (kit English via en.wp *Hi-hat*; T4 German literature imports "Chick" untranslated) | D01 §2.9, §2.12 |
| Pedal hi-hat | notes played solely with the pedal | `technique: chick` / `hihat.pedal.*` | 1 | D01 §2.9 |
| **Foot splash** | like a chick but the pedal is released immediately so the cymbals rebound apart and ring | `technique: foot-splash` — **weakly attested**; not in en.wp *Hi-hat*; underlying pages 403/empty | 0 confirmed | D01 §2.9, §6.3 |
| Cooking | shuffle figure: struck twice, held closed on the first, opened just before the second, rung, then chicked | **NONE** (a pattern) | 1 (en.wp *Hi-hat*, verbatim) | D01 §2.9 |
| `halboffen` / `offen` / `geschlossen` | German hi-hat openness triple | `openness: half`/`open`/`closed` | 1 (T4) | D01 §2.9, §2.12 |
| With foot-beater / `À pied` / `Mit dem Fuss`; Bass drum alone (with cymbal detached) | pedal-played bass drum, and the negation of the coupled rig | `mechanism` **MISSING** | 2 (T5 Read pp. 182, 201; T4 Berlioz–Strauss p. 418) | D02 §2.5, §2.6, §3.8 |

## 1.4 `ornament` — per-note qualifiers with attack counts

This is the table the pivot model actually needs (D01 §2.4 says so explicitly).

| Term | Attacks | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|---|
| Flam / `fla` / `Schlepp` / `Einfacher Vorschlag` / `coup double` / `mordente` (ES gloss) | 2 | grace on the opposite hand immediately before the primary; Hart 1860 defines it purely as a **dynamic relation**: "a very soft, fine blow … and a full heavy blow immediately following" | `ornament: flam` (attacks 2) | 5 (T1, T2, T3 Gevaert p. 331 `le coup double, fla`, T4, T5 Read p. 198 "'Flam' stroke") | D01 §2.4, §2.3b, §2.13b; D02 §2.6, §2.13 |
| **Open flam** | 2 | flam with an audibly wider grace-to-primary gap; a separately named item in 1870 and in European systems | `ornament` **MISSING** | 2 (T1 Strube line 1134, Greissinger "The Open Flam"; European systems via en.wp) | D01 §2.4, §3.2, §5.2 |
| Drag / half drag / `3er Ruf` / `ra de 3` / `tra` | 3 | two **diddled** (same-hand) grace notes before the primary | `ornament: drag` (attacks 3) | 4 (T1, T2 `3er Ruf`, T3 `ra de 3`, T4) | D01 §2.4, §2.13b; D02 §2.13 |
| Ruff (historic / American 3-stroke ruff) | 3 | two **single-stroked, alternating** grace notes; Nevins 1864 No. 25 "composed of three Poing Strokes … right, left, right" | `ornament: ruff` — but see §4, v0.1 treats ruff and drag as distinct ornaments where PAS treats them as one figure | 3 (T1 Nevins 1864 primary; Italian keeps `ruff` first-class in its 26; NARD 1958 track 8 "The Ruff") | D01 §2.4, §2.13, §5.1 |
| 4-stroke ruff / Four-Stroke Ruff | 4 | three single grace notes before the primary | `ornament: ruff` with count 4 — **count missing** | 2 (T1 Gardner 1918 p. 23; en.wp §Ruff) | D01 §2.4; **D02 §2.15** |
| **Charge stroke / `coup de charge` / `tra`** | 2 | grace attached **after** the primary; the rhythmic accent falls on the *first* of the pair, i.e. "l'inverse du fla". Codex ships **two** — Swiss and French forms — plus a *Flammed* Coup de Charge | `ornament` **MISSING** — §2 G14 | 3 (T2 Codex #14, #15; T3 de Douvan item 7 **and** Gevaert 1885 p. 332 `le coup de charge, tra`; T1 via en.wp §Charge stroke) | D01 §2.4, §2.13b, §5.2; **D02 §2.13, §3.6, §3.9 G14** |
| **Double stop / flat flam / unison / "both"** | 2 simultaneous | both hands land at exactly the same instant, zero offset; "a staple of several European systems" | `ornament` **MISSING** | 2 (European systems via en.wp; T9 vendor `Double-stop on lower shells`, VDL p. 30) | D01 §2.4, §3.2, §5.2; D08 §2.4 |
| Diddle | 2 | a double stroke at the prevailing subdivision | `ornament: bounced`-adjacent | 1 (T1) | D01 §2.4 |
| Cheese | 3 | a flammed diddle | hybrid — out of scope (§4.4 below) | 1 (T1 hybrid corpus) | D01 §2.4, §2.15 |
| Herta | 3 | a drag played with **alternating** rather than diddled sticking | hybrid — out of scope | 1 | D01 §2.4 |
| Ghost note | 1 | a tap deliberately below the surrounding dynamic; "the inverse of an accent" | `dynamic: ghost` | 2 (T1 via en.wp *Drum stroke*; T5 Read p. 181 "Barely touched") | D01 §2.4; D02 §3.8 |
| Roll (open, double stroke) / Long Roll / `roulement` / `bâton rompu` / `Doppelschlagwirbel` / `Offener Wirbel` | 2 per hand-motion | first stroke wristed, second driven by rebound + finger pressure; each stroke individually audible | `ornament: roll` | 4 (T1, T2, T3, T4) | D01 §2.5, §4.2 |
| Single stroke roll / `Einzelschlagwirbel` / `coup simple` / `frisé` / `bâton rond` / `redoble de golpe único` | 1 | alternating single strokes | `ornament: roll` with 1/hand | 4 (T1, T2, T3 — `bâton rond` in **Furetière 1690**, T4) | D01 §2.5, §2.11 |
| Multiple bounce / buzz / closed / press roll / `Presswirbel` / `Druckruf` / `trizzlet` / `Ra stroke` / `Redoble de Zumbido` / `Los Rufaos` / `Rullo` / `Rau Tau` | indeterminate | stick is *pressed* into the head; the count cannot be specified | `ornament: buzz` | 5+ (T1, T2, T4 `Druckruf`/`Presswirbel`, T10 Scottish `trizzlet`, T11 Dutch/Mexican/Spanish/Bajoaragonés/Eporedian names) | D01 §2.5, §4.2 |
| Triple stroke roll = **French roll** | 3 | three strokes per hand | `ornament: bounced` | 1 (T1) | D01 §2.5 |
| Numbered rolls 5, 6, 7, 9, 10, 11, 13, 15, 17 (+ 4, 8, 12, 14, 16 rare; Scottish to 25) | measured | a fixed **total** attack count with a terminal accent; **odd counts take one accent, even counts two** | `ornament` **count parameter MISSING** | 4 (T1 PAS/NARD + Gardner 1918; T2 `N er Ruf`; T3 `ra de N` + Gevaert 1885 `ra de 3/4/5/6/7 coups`; T10 Scottish stroked rolls to 25) | D01 §2.5, §2.13b, §5.3-1; **D02 §2.13, §2.15, §3.6, §5.3** |
| Eight-stroke Roll | 8 | "from hand to hand"; on no modern list | `ornament` count 8 | 1 (T1 Greissinger 1900 line 4221; Moeller 1925 via en.wp) | D01 §2.3c, §2.5 |
| 3-stroke roll | 3 | "the shortest possible open double stroke roll, but is commonly referred to by the specific name Drag, Ruff, or Half Drag" | `ornament: drag` | 1 (en.wp *Drum roll*, verbatim) | D01 §2.5 |
| Fulcrum / gravity / freehand roll / `Einhändiger Wirbel` / gravity blast | 2 per arm motion | **the rim momentarily replaces the finger fulcrum**: one arm stroke, two head contacts. Named "Freehand Technique" by Johnny Rabb, coined 1995 | **NONE** as a term (a motor system); its trace is attack count | 2 (T1 via en.wp; T4 `Einhändiger Wirbel`) | D01 §2.5, §2.6, §4.2 |
| One-handed roll (push-pull) | 2 per motion | wrist supplies one stroke, fingers the other, no rim contact | **NONE** (motor system) | 2 (T1, T4) | D01 §2.5, §2.6 |
| **Press roll** (Bauduc), six numbered varieties | indeterminate | distinguished by *where the press falls* and whether it is "a drag of the left hand stick"; the central device of the Dixieland style | `ornament` **MISSING** — `buzz` and `roll` exist, `press-roll` does not | 1 (T6 Bauduc 1937 *Dixieland Press Rolls*) — and T4 `Pressschlag` is the *single* pressed stroke, a different thing | **D02 §2.17, §3.6, §5.1** |
| Drag vs press, distinguished **by attack count** | | "Drags are not press rolls. A Drag is ended while a Press is made with one stick only. **You must hear the two taps clear in a drag**" — countability, not speed | supports `ornament` attacks field | 1 (T6 Straight 1922 line 1782) | D01 §2.3c |
| `Einzelschlag` / `Doppelschlag` / `Pressschlag` | 1 / 2 / indet. | the three German stroke primitives | `ornament` none / `bounced` / `buzz` | 1 (T4, Peinkofer/Tannigel 1981 pp. 84–85 via de.wp) | D01 §2.12 |
| `Vorschlag` | 1..4 | German for grace note; multiple Vorschläge are what the Doppelschlag serves | `ornament` grace | 1 (T4) | D01 §2.12 |
| `Mühle` / `Mama-Papa` / `Papa-Mama`; EN "Mammy-Daddy"; FR "papa-maman" | | onomatopoeic name for the double-stroke preparation | see §3 — `Mühle` has **three** senses | 3 (T1 Greissinger 1900 "Mammy-Daddy"; T3 "papa-maman"; T4 "Mama-Papa") | D01 §2.3c, §2.11, §2.12 |
| **Crush** (`FAT crush`, `DRY crush`, `WET crush`) | short, pressed | a short pressed multiple-bounce with a **named tone quality**; not `buzz`, not `roll`; "the single most frequently mapped articulation in the whole VDL library" | `ornament` **MISSING** | 0 traditions; 1 vendor (Tapspace VDL snare/tenor/bass keymaps) | D08 §3.1, §5.2 |
| Crescendo / decrescendo / diminuendo roll; `SHORT`/`MEDIUM`/`LONG`; `FP` (forte-piano) | sustained | roll **shape and length** as first-class articulation properties | `ornament: crescendo`/`swell` exist; **`diminuendo`, length and FP shape missing** | 0 traditions; 1 vendor (VDL) | D08 §3.1, §5.2 |
| Wash / Flat Roll / Circular Roll / Tremolo (cymbal pair) | sustained | plates rotated so edges touch continuously | `ornament: wash`/`roll` | 2 (T8 PCHS `Wash`, Missouri State "cymbal rolls") + 1 vendor (VDL three named roll types) | D08 §2.7 |
| Thumb roll ("temporary roll") | | Widor is explicit that it **cannot be sustained** — "a temporary roll" | `ornament` **MISSING** as distinct from `roll` | 3 (T5 Read p. 213, Forsyth p. 32, Widor p. 109) | D02 §2.11, §2.12, §5.1 |
| Trill (brush) | unmetered | a **one-handed roll with brushes**, thumbs-up grip, brush "shaken" across the head; speed set by the dynamic | `ornament`/`technique` NEW-VALUE | 1 (T7 O'Mahoney p. 21) | D01 §2.8, §3.2 |
| Trill with pennies / coins; `Trillo colle monete` | | roll produced by coins on a timpani head | `ornament: roll` + implement `coin` (missing) | 1 (T5 Read p. 164; Forsyth p. 50 "with a couple of coins") | D02 §2.4, §2.11 |
| **`loud-soft` and `soft-loud` as elementary pairs** | 2 | items **2 and 3** of the Rudimental Codex are nothing but these two pairs, ranked **above the flam**; the poster's whole sticking legend is `RIGHT HAND \| loud - soft`, `LEFT HAND \| loud - soft` | **NONE** — v0.1 cannot say "this attack is the soft half of a loud-soft pair" | 2 (T2 Codex #2, #3 + legend; T1 Hart 1860's definition of the flam as exactly this relation) | D01 §2.13b, §5.2 |

## 1.5 `site` — on the instrument

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| On the head / on the skin / `Sur la peau` / `Auf das Fell` | | `site: head` | 3 (T5 Read p. 199; T1; T8) | D02 §2.6, §3.2 |
| **batter-head vs snare-head** | Forsyth names both: "The upper head — that on which the player beats — is called the 'batter-head': the lower, the 'snare-head'" | `site: head` vs `underside` — v0.1 names **only the second** | 1 (T5 Forsyth p. 24) | D02 §2.11, §3.2, §5.1 |
| On both sides / skins / `Auf beiden Fellen` | both heads simultaneously | `site` head + underside at once — not expressible | 1 (T5 Read p. 198) | D02 §2.6, §3.2 |
| At/on the rim (of the drum) / on the wood / `Sur le cercle` / `Am Rand` | the hoop | `site: rim` | 3 (T5 Read p. 197; T1; T8) | D02 §2.6 |
| **On the frame / hoop / `Sur le cadre` / `Auf den hölzernen Rahmen`** vs **metal rim around head / `Am Metallrand`** | the **wooden hoop** and the **metal counterhoop are different objects** | `site: rim` conflates them | 2 (T5 Read pp. 164, 199; T6 Bauduc's "bass drum **counter hoop**" as a named playing surface struck with the tips of sticks) | D02 §2.6, §2.17, §5.1 |
| On the shell / on the bell [body] / on the side / `Sulla cassa` | | `site: shell` | 3 (T5 Read pp. 199, 221; T8 `Snare shell`, `Double-stop on lower shells`; T9 vendor) | D02 §2.6; D08 §2.8 |
| **On the snares / `Sulle corde` / `Sur le(s) timbre(s)` / `Auf den Saiten`** | the snare wires struck as a **surface** | **NONE** — §2 G1 | 1 (T5 Read p. 232) | D02 §2.2, §3.2, §3.9 |
| **Strike on copper kettle (of timpani)** | the bowl as a third body | **NONE** — §2 G2 | 1 (T5 Read p. 164) | D02 §2.4, §3.9 |
| On the dome / `Sulla cupola` / `Sur la protubérance` / `Auf die Kuppel` | cymbal cup | `site: bell` | 1 (T5 Read p. 183) | D02 §2.5 |
| At the edge / `Au bord` (cymbal); `Blousé/blouser/blousez` | | `site: edge` | 1 (T5 Read pp. 163, 180) | D02 §2.4, §2.5 |
| Bow / edge / bell of a **held** cymbal (cymbalist holds plates for a snare drummer) | the holder gives access to "the edge, bow, and bell" | `site: bow`/`edge`/`bell` | 2 (T8 Oregon State p. 154, PCHS p. 13, en.wp line 98) | D08 §2.7, §3.1 |
| **Jingles / `Sur les tintements` / `Auf den Schellen`; "without jingles"** | the tambourine jingles struck and brushed independently of the head | `site` **MISSING** | 2 (T5 Read pp. 214, 220; Forsyth p. 32; Widor p. 109) | D02 §2.7, §5.1 |
| **Cage / `RH on cage`, `LH on cage`** | the carrier frame of a marching snare, struck deliberately | **NONE** — §2 A2 | 0 traditions; 1 vendor | D08 §3.2 item 2, §5.2 |
| **`Dress center harness hit`** | strike on the player's **harness** | **NONE** | 0; 1 vendor | D08 §3.2 item 3 |
| **`Tenor Stand click`, `Aluminum mallet clicks`, `Sticks-in`** | sounds of the equipment and of the player's rest position | **NONE** | 0; 1 vendor | D08 §3.2 item 4 |
| **Bar-end** (bow drawn across the sharp edge at the end of a bar) and **resonator** (gliss across the resonators) | keyboard-percussion sites | `site` **MISSING** | 1 (T5 Read p. 179) | D02 §2.8, §5.1 |
| Played behind the bridge (cimbalom) | chordophone site | out of scope | 1 (T5 Read p. 221) | D02 §2.8 |
| `Rim of Bass drum` as a named playing surface | 1922 kit vernacular, listed beside the wood block | `site: rim` on `instrument: kick` | 2 (T6 Straight 1922 Lesson 41 & 53; Bauduc 1937 counter hoop) | D02 §2.16, §2.17 |

## 1.6 `position` — where on the site

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| "centre of the head, **within a circle of about two inches**" | | `position: centre` — v0.1 has no distance unit | T1 (Strube 1870 lines 301–302) | D01 §2.3, §3.1 |
| "beat square upon the head … **as near the center of the head as possible**" | plus a prohibition on drawing/sideway beats | `position: centre` | T1 (Hart 1860 lines 116–121) | D01 §2.3b |
| "Strike the Drum **about an inch above the center**" | | `position: centre`/`offset` | T1 (Nevins 1864) | D01 §2.3b |
| "sticks strike **near the middle of the drum-head**" | | `position: centre` | T1 (Greissinger 1900 line 4089) | D01 §2.3c |
| (Hit) in center / `Nel mezzo della membrana` / `Au centre` / `In der Mitte des Felles` | given for **timpani, bass drum, snare drum and tambourine alike** — a cross-instrument axis | `position: centre` | T5 (Read pp. 164, 198, 214) | D02 §2.4, §2.6, §5.3 |
| At the rim **of head** / near the rim / close to the rim / on the edge of the skin | a **radial position on the membrane**, distinct from the hoop | `position: perimeter` | T5 (Read p. 163) | D02 §2.4, §4 item 8 |
| **VDL mod-wheel legend: `00-43 = center of head`, `44-89 = halfway to edge`, `90-127 = edge of head`** | a striking-position scale in a vendor's own words | direct confirmation of `position: centre`/`halfway`/`perimeter` | 0 traditions; **1 vendor**, but it independently confirms three of four v0.1 anchors | D08 §2.4, §3.1, §5.2 |
| "**2 inches from the rim, or 1.5 inches from the bearing edge**"; "one concentric circle, like a timpanist" | the marching **default is `offset`, not `centre`** | `position: offset` | 1 (T8 Missouri State FA20 "Playing Zones") | D08 §2.6, §3.1, §5.2 |
| Sweep playing zones ("in the same concentric circle as the regular zones") | | `position` | 1 (T8 Missouri State) | D08 §2.6 |
| Ping/normal/gock as **one technique at three positions** | ping = bead ~1″ from rim; normal ~3″; gock = bead at centre with the rim contacted by the shaft | `position: perimeter`/`offset`/`centre` on `technique: rimshot` | 3 authorities (T8 packets, en.wp, T9 vendor) | D08 §2.5.2, §3.1, §5.1.2 |
| Clock-face position language (brush) | brush position given as hours: 12, 3, 6, 9 o'clock — "the standard way the literature states a position on the head" | `position` — v0.1 is radial only, no **angular** coordinate | 1 (T7 Hazilla p. 32; Hamilton) | D01 §2.8 |
| Half-note sweep: "7 o'clock → 2 o'clock on beat 2, back to 7 for 3, to 2 for 4" | an angular trajectory | **NONE** (angular + trajectory) | 1 (T7 Hamilton p. 18) | D01 §2.8 |
| Clockwise vs counter-clockwise circle | "counter-clockwise circles push away the beat, while clockwise circles physically bring the beat to me" | **NONE** (rotation direction) | 1 (T7 Hamilton p. 20) | D01 §2.8 |
| **Roll — beginning at centre — gradually going to the rim** (and its inverse) | a **trajectory across `position` within one sounding event** | **NONE** — §2 G12; expressible only via `strike_position.radial` as a controller | 1 (T5 Read p. 212) | D02 §2.6, §3.3, §3.9 |

## 1.7 `contact` — part of the implement

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| Tip / bead | | `contact: tip` | 4 (T1, T5, T6, T8) | D01 §3.1; D02 §3.4; D08 §2.5 |
| **With the thin end of the stick / `Coll'estremità sottile` / `Mit dem dünnen Ende des Stockes`** | | `contact: tip` (alias missing) | 1 (T5 Read p. 184) | D02 §2.5, §5.1 |
| **With the thick end / `Coll'estremità grossa` / `Mit dem dicken Ende`**; with the handle / `col mancio della mazza` / `Mit dem Stiel des Klöppels`; struck with the wood | | `contact: butt` | 2 (T5 Read pp. 184, 200, 222, 232; T4 Berlioz–Strauss) | D02 §2.5, §2.6, §3.4 |
| Shank / distal shaft near the hand; `Holzschaft des Schlägels` | | `contact: shank` | 3 (T5 Read p. 184; T8 gock definition; T9 VDL) | D01 §2.7; D02 §3.4 |
| Butt (vertical) — `RH/LH Butt (vertical)` | | `contact: butt` | 0; 1 vendor | D08 §2.4, §3.1 |
| Casey Claw | "the first note of every right hand double is played with the **'butt' end** of the drum stick and the very next note of the double is played with the **tip**" — created Mark Casey 1990, UK; DCI 1993; Cavaliers 1994/95/2023 | the sharpest statement that `contact: butt` must be first-class | 1 (T8) | D08 §2.5.1 |
| **"striking first at small end or tip and work up to Butt of sticks … keep moving up and down"** | a **continuum** on `contact`, not two values | **NONE** — §2 G12b; `contact` has three enum values and **no controller** | 1 (T6 Straight 1922, Lesson 53) | D02 §2.16, §3.4, §3.9 |
| Fan (brush) vs tips | accent surface | `contact` **MISSING** value | 1 (T7 Soph) | D01 §2.8, §5.2 |

## 1.8 `implement`

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| Read's 61 beater names, pp. 166–167 | the largest single implement list in these dossiers; the list is **not closed** — three further beater headings appear in the chapter tables but not in the list | see below | 1 document (T5), but four languages | D02 §2.3 |
| **Sponge stick / `Bacchetta di spugna` / `Baguette d'éponge` / `Schwammschlägel`** | the historically dominant timpani beater; "die besten" (Berlioz–Strauss p. 406), "sticks with sponge knobs" (Widor p. 100) | `implement` **MISSING** | 3 (T4 Berlioz–Strauss p. 406; T5 Read pp. 166–167 and Widor p. 100) | D02 §2.3, §2.10, §2.12, §5.1 |
| Leather / rawhide / skin-knob | the middle grade of the 19th-c. three-step hardness scale | `implement` **MISSING** | 2 (T4 Berlioz–Strauss p. 406 "mit von Leder überzogenen Holzköpfen"; T5 Widor p. 100, Read) | D02 §2.10, §2.12, §5.1 |
| Wood-headed stick / `Holzköpfe` | "rauh, trocken, hart"; Widor: "very hard and has very little timbre" | `implement: wood-beater` | 2 (T4, T5) | D02 §2.10, §2.12 |
| **A three-value ordered hardness scale: wood / leather-covered wood / sponge** | asserted as *the* distinction that changes the timbre, and as something the composer is negligent not to specify | supports an ordered hardness axis | 2 (T4 Berlioz–Strauss p. 406; T5 Widor p. 100) | D02 §2.10, §2.12 |
| **Hardness as a qualifier orthogonal to material** | Read carries `quarter-hard`, `half-hard`, `medium-hard`, `medium-soft`, `soft`, `hard`, `very hard`, `very soft` **on rubber, felt and leather independently** | v0.1's `mallet-soft/medium/hard` **folds material and hardness into one value** and cannot express "medium-hard **leather**" | 1 (T5 Read pp. 166–167) | D02 §5.1 |
| Cane / rattan / cotton / wool / capoc (fibre head) / plush / padded / steel / iron / metal / knife-blade / two-headed [double] stick / triangle beater / chime hammer | | `implement` **MISSING**, all | 1 (T5 Read pp. 166–167) | D02 §2.3, §5.1 |
| Switch [Rod] / `Verghe` / `Verges` / `Ruten (Rute, Ruthe)` | Forsyth p. 28 identifies the German *Ruthe* as a "birch-broom" | `implement: rod` | 3 (T5 Read pp. 166–167, Forsyth p. 28, Solomon p. 94 "Rute Sticks") | D02 §2.3, §2.11, §3.8 |
| Wire-brush / `Scovolo di fil di ferro` / `Balai métallique` / `Drahtbürste` | | `implement: brush` | 3 (T5 Read; T6 Bauduc 1937 four numbered brush patterns; T7 the whole brush anthology) | D02 §2.3, §2.17; D01 §2.8 |
| Knitting needle | | `implement` **MISSING** | 1 (T5 Solomon p. 92) | D02 §2.14, §5.1 |
| Superball mallet | | `implement: superball` | 1 (T5 Solomon p. 95) | D02 §2.14, §3.8 |
| Coin / silver coin / pennies | used as a beater on timpani and cymbals | `implement` **MISSING** | 2 (T5 Read pp. 164, 181; Forsyth p. 50 "trick ways, such as with a couple of coins") | D02 §2.4, §2.5, §2.11 |
| 'Cello bow; saw blade; rosined glove; maracas used as beaters | | `implement` **MISSING** | 1–2 (T5 Read pp. 172, 195, 211; Solomon p. 95) | D02 §2.4, §2.5, §5.1 |
| **`Klöppel` vs `Schlägel`** | Berlioz–Strauss uses `Klöppel` specifically for the **bass-drum beater** and `Schlägel` generically; Read's German column uses `Schlägel` for both | `implement` naming conflict, see §3 | 2 (T4 vs T5) | D02 §2.10, §4 item 6 |
| **Jazz-sticks** | "Sand-blocks, **Clog-mallets**, **Jazz-sticks** or **Leather straps**" — earliest attestation found for v0.1's `jazz-stick`, **1922, not a modern marketing coinage** | `implement: jazz-stick` — **confirmed with a primary locator** | 1 (T6 Straight 1922 Lesson 41 / line 13078) | **D01 §2.3c, §5.4; D02 §2.16, §3.8** |
| Sand blocks / clog mallets / leather straps | 1922 kit implements; the list is explicitly open-ended ("Play on anything") | `implement` **MISSING** | 1 (T6 Straight 1922) | D02 §2.16, §5.1 |
| **Dread** (Tapspace's multi-rod bundle) | a first-class VDL implement **distinct from `rod`** | `implement` **MISSING** | 0 traditions; 1 vendor | D08 §2.4, §5.2 |
| Felt (`RH felt` / `LH felt` on snare); puffy mallet; regular mallet; aluminium mallet | | `implement` `felt-beater` exists; **`puffy-mallet`, `aluminum-mallet` missing** | 0 traditions; 1 vendor | D08 §2.4, §5.2 |
| Bass mallet sizing by position: "Bass 1 – MB1H; Bass 2 & 3 – MB2H; Bass 4 – MB3H" | implement graded by instance | supports implement × instance | 1 (T8 EPCHS p. 3) | D08 §2.6 |
| **Plate / cymbal-on-cymbal** | for the entire marching cymbal line the implement **is another cymbal** | `implement` **MISSING** | 2 (T8 five packets; T5 Read's `Piatti a due` clash entries) | D08 §5.2; D02 §2.5 |
| Brush (fan, tips, grip point) | see §1.2 | `implement: brush` | 1 (T7) | D01 §2.8 |
| **Fist / fingernail** | see §1.2; listed in the round-2 brief's model, absent from `axes.json` | `implement` **MISSING**, both | 2 for `fist` (T5 Read p. 214; T8 Casey Claw) | D01 §5.2; D02 §5.1; **D08 §2.5.1, §5.2** |
| "**Beater Lingo**" | Solomon devotes a titled section to the instability of beater names | not a term — a **finding**: any implement vocabulary must ship aliases | 1 (T5 Solomon p. 85) | D02 §2.14, §3.9 G18 |
| "**Ordinary [Regular, Usual] beater(s) [hammer(s); mallet(s); stick(s); striker(s)]**" | Read gives **seven English words** for the default beater in one entry | `implement: stick` + six aliases | 1 (T5 Read p. 166) | D02 §2.3, §4 |

## 1.9 `damping` and `mechanism`

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| **Dampened** — Choke(d) / Damp(en) / Damp instantly / Dry / Off / Short / Stop (quickly) / `Secco` / `Smorzate` / `Soffocato` / `Étouffé` / `Sec` / `Dämpfen` / `Kurz` | **stop the sound after it starts** | `damping: damped` | 1 document but 4 languages (T5 Read p. 163) — **eight English synonyms for one action** | D02 §2.4, §3.7, §4 |
| **Muffled** — `Con sordino` / `Coperto` / `Velato` / `Sons voilés` / `Sourdine` / `Voilée` / `Abdämpfen` / `Bedeckt` / `Dumpf` / `Gedämpft` | **alter the sound before it starts** | `damping: muted`/`towel` | 4 (T5 Read p. 165; T4 Berlioz–Strauss p. 411 "gedämpfte oder bedeckte Pauken … mit einem Stück Tuch bedeckt"; T3 Gevaert p. 332 `voilés`; T5 Widor p. 108) | D02 §2.4, §2.10, §2.12, §2.13 |
| **Read splits `Dampened` from `Muffled`; v0.1 does not** | separate chapter sections throughout Part IV | see §4 | contents pp. XVI–XVII, body pp. 158–233 | **D02 §2.1, §4 item 7, §5.3** |
| Muting (Muffling, Dampening) as **one** heading | Solomon 2016 collapses the three English words; "the 2016 conflation is the one most vendor lists inherit" | the conflation v0.1 currently shares | 1 (T5 Solomon p. 74) | D02 §2.14, §4 item 7 |
| Muffle off / Natural `nat.` / `Modo ordinario` / `Senza sordino` / `Sans sourdine` / `Gewöhnlich` / `Dämpfung ab` | | `damping: none` | 1 (T5 Read p. 165) | D02 §2.4 |
| **Stop [dampen] half-way, and full / `Étouffez à demi, et tout à fait` / `Halb und ganz dämpfen`** | an **ordinal, mid-event** two-point damping scale | **NONE** — §2 G13; `damping` is nominal | 1 (T5 Read p. 195) | D02 §2.5, §3.7, §5.1 |
| Place a handkerchief / a piece of paper / a thin piece of felt **on the middle of** the head; wrapped tightly in a cloth (triangle); Prepared Instruments | a **preparation is an object added at a position, with its own material** | **NONE** — §2 G8; `damping` has nominal values only | 2 (T5 Read pp. 211, 212, 220; Solomon p. 245) | D02 §2.6, §2.7, §3.7, §3.9 |
| Muffled drums (as a **standing state**) | "Use **muffled drums** when you Jazz, not too loud"; "both drums muffled" | `damping: muted` — **a 1920s concept, not a sampling-era one** | 2 (T6 Straight 1922 lines 4965, 6565; T2 the Basel drum's permanent `Dämpfer` on the batter head) | D01 §5.4 |
| Hold cymbals together after striking / `Becken nach Anschlag zusammen halten`; "die Becken sofort nach dem Schlage an die Brust drückt" | the cymbal choke, described mechanically | `relations: choke` — **v0.1 is right to keep choke off the axes** | 2 (T5 Read p. 194; T4 Berlioz–Strauss p. 422) | D02 §2.5, §2.10, §3.7 |
| Every marching cymbal sound has a **choked twin** | Crash Choke, Tap Choke, Hi-Hat Choke, Crunch Choke, Slap Choke, Bell Tap-Choke | independent support for `choke` as a **relation, not an axis value** | 2 (T8 five packets; 1 vendor VDL) | D08 §3.1 |
| Snares on / `Con timbro` / `Avec timbre(s)` / `Mit Schnarrseite` | | `mechanism: wires-on` | 3 (T5 Read p. 210; T3; T4) | D02 §2.6, §3.8 |
| Snares off / no snares / without snares / `Senza timbro` / `Sans timbre` / `Détimbrée` / `Ohne Schnarrseite` | Read p. 209 gives **ten English forms** | `mechanism: wires-off` | 4 (T5 Read, Forsyth p. 27; T3 Gevaert; T4 Berlioz–Strauss; T9 VDL `Snares OFF`) | D02 §2.6, §2.11, §3.8, §4 |
| **Loosen / slacken snares; `Avec les cordes lâches`; "snares loosened"** | wires stay in contact but slack — **distinct from `wires-off`**, and given as the **usual** practice | `mechanism` **MISSING** | **3 independent** (T5 Read p. 209 + Widor p. 108; T4 Berlioz–Strauss p. 423; T3 Gevaert p. 332) | D02 §2.6, §2.10, §2.12, §2.13, §3.8, §5.1 |
| **Tighten snares / `Très timbrée`** | a **third** state above `wires-on` | `mechanism` **MISSING** | 1 (T5 Read p. 210) | D02 §2.6, §3.8, §5.1 |
| Throwoff ON / Throwoff OFF as keys **separate from** Snares ON/OFF | suggests the *sound of operating the throw-off* is distinct from the state — **UNVERIFIED** whether mechanism or equipment sound | `mechanism` open question | 0 traditions; 1 vendor | D08 §5.2 |
| **Cymbal attached to bass drum / fixed to the foot-pedal / `Grosse caisse à pied avec cymbale`**, and its negation | a **rig** fact: two instruments mechanically coupled so one stroke sounds both | **NONE** — §2 G5 | 2 (T5 Read pp. 182, 201; T4 Berlioz–Strauss p. 418) | D02 §2.5, §3.8, §3.9 |
| Damper Pedals (keyboard percussion); Pedal off, no resonance; Pedal glissando | | `mechanism` partly missing | 1 (T5 Read pp. 165, 179; Solomon p. 75) | D02 §2.4, §2.8, §3.8 |
| **Sock cymbal pedal** | the **pre-1940 name for the hi-hat** | `instrument: hihat` — **no historical alias in v0.1** | 1 (T6 Bauduc 1937) | D02 §2.17 |

## 1.10 `dynamic`

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| **Hard / Middling Hard / Faint or Soft** | a **named, ordered three-level dynamic scale of 1864**, applied independently to the plain stroke (items 8, 9, 10), to the flam (11 vs 12 "FAINT FLAMS") and to a roll (3 vs 4 "SEVEN STROKE ROLL: Faint, or Soft") | v0.1's five values are an **unordered set** | 1 (T1 Nevins 1864) — and it is the earliest evidence that dynamic is an axis orthogonal to the figure | D01 §2.3b, §5.2 |
| Full / half flam, "both heavy and light" | a two-step size grade on the flam itself | `dynamic` on an ornament — not expressible | 1 (T1 Hart 1860 Lesson IV) | D01 §2.3b |
| Hart's two independent scales: **weight** (heavy / hard-quick) and **duration** (`open` = soft and light) | four graded characters over four primitives | dynamic **and** an envelope dimension | 1 (T1 Hart 1860 lines 133–166) | D01 §2.3b |
| Accent / "a light accent should be placed on the last blow of the Five Roll, as well as all other Rolls" | | `dynamic: accent` | 3 (T1 Hart Lesson VI, Greissinger "accent the second stroke of each hand"; T5; T8) | D01 §2.3b, §2.3c |
| **Read p. 214: "L'accent ( > ) indique le coup frappé avec le poing"** | in that score the **accent sign *is* the technique marker** | a parser that reads `>` as `dynamic: accent` **loses a technique** | 1 (T5 Read p. 214) | D02 §3.8, §5.2 item 7 |
| Ghost note / barely touched / `Appena toccata` / `À peine frôlé` / `Leicht berühren` | | `dynamic: ghost` | 2 (T1; T5 Read p. 181) | D01 §2.4; D02 §3.8 |
| **Faint / feathered** — a level **below** `ghost` | Nevins's "FAINT FLAMS" and "Faint, or Soft" seven-stroke roll; Hazilla's bass drum "played on all four beats at near-inaudible volume beneath brush time" | `dynamic` **MISSING** | 2 (T1 Nevins 1864; T7 Hazilla concept 5) | D01 §2.8, §5.2 |
| Stick heights: "regularly used heights range from **3″ to 12″**, with **1″ and 15″** used mostly for visual effect" | an **ordered continuous scale** | **NONE** — §2 A6; `dynamic` is a five-value unordered set | 2 (T8 marching practice via en.wp; T1 PAS teaches accent/tap as a *height* relation) | D01 §2.6, §3.3, §5.2 |
| Per-instance dynamic assignment: "3 Drums, I: f, II: mf, III: p" | | **NONE** — §2 G6 | 1 (T5 Read pp. 211, 212) | D02 §3.9 |

## 1.11 `openness`

| Term | Physical meaning | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| `offen` / `halboffen` / `geschlossen`; open / half-open / closed hi-hat | | `openness: open`/`half`/`closed` | 2 (T4; kit English) | D01 §2.9, §3.1 |
| `Hi Hat LOOSE / MEDIUM / TIGHT` | lands exactly on existing anchors | `openness: loose`/`half`/`tight` — **no gap** | 0 traditions; 1 vendor | D08 §3.1, §5.2 |
| **Open roll vs closed roll** | | `ornament: roll` vs `buzz` — i.e. openness is currently expressed on `ornament`, not `openness` | 4 (T1, T2 `Offener`/`Geschlossener Wirbel`, T3, T4) | D01 §2.5, §5.3-2 |
| **Open Flam** (Strube 1870, Greissinger 1900) | openness applied to a **grace ornament** | `openness` is hi-hat-anchored; this is unrepresentable | 1 (T1, two documents) | D01 §2.3, §2.3c, §5.3-2 |
| **Open Drag / Close Drag or Half Drag**; Hart's "Three Roll open" / "closed three Roll" | the drag as a single figure with an **open↔closed axis** — **three independent attestations for the drag alone** | `openness` is not generalised to ornaments | 1 tradition, 3 documents (T1 Hart 1860, Greissinger 1900, and en.wp's summary) | D01 §2.3b, §2.3c, §5.3-2 |
| PAS practice directive: "open (slow) to close (fast) to open (slow)" | | **NONE** — a practice directive, not identity | 1 (T1 PAS 1984 sheet, verbatim) | D01 §2.1, §3.3 |
| **Hart 1860: `open` means SOFT** | "the full **open** flam … the full **open** blow … the full **open** three roll … will be executed **soft and light**"; a soft roll is written with an "**open figure**" numeral | a trap for any importer — see §3 | 1 (T1 Hart lines 158–170) | D01 §2.3b, §4.1 |
| The orchestral literature has **no** graded-openness instrument | the nearest analogue is Read's graded *damping*, not openness | confirms `openness` is a kit/e-drum axis | 1 (T5) | D02 §3.8 |

## 1.12 `instrument` — terms these dossiers add

| Term | Note | v0.1 | Indep. traditions | Locator |
|---|---|---|---|---|
| The whole orchestral + auxiliary inventory (Read pp. 8–9, 33 supplementary entries; Solomon chs. 5–9) | the highest-confidence subset is the ~37 instruments present in **both** Read 1953 and Solomon 2016 — anvil, bell plate, bongos, brake drum, castanets, chains, chimes, claves, cowbell, crotales, finger cymbals, flexatone, glockenspiel, gong, guiro, jingles, log drum, maracas, marimba, ratchet, sandpaper blocks, sleighbells, slapstick, siren, steel drum, string drum/lion's roar, tam-tam, temple blocks, thunder sheet, thunder machine, timbales, timpani, tom-tom, vibraphone, wind machine, wood block, xylophone | `orch`, `perc.*`, `utility` reserved and unminted — **all of it is new** | 2 (T5 Read 1953 and Solomon 2016, 63 years apart) | D02 §2.9, §2.14, §3.1 |
| **Suspended vs pair cymbal** | Read gives them **separate nomenclature entries** (`Piatti (a due)` vs `Piatto sospeso` / `Cymbale suspendue` / `Becken frei`) and a separate chapter | v0.1's single `cymbal` (id 18) **cannot express it**; `crash` is a suspended cymbal and there is **no slot for `piatti` / clash cymbals at all** | 2 (T5 Read p. 8, ch. 34; T8 the entire marching cymbal line is a clash pair) | D02 §3.1, §5.2 item 3; D08 §2.7 |
| **Tenor Drum / `Rührtrommel` / `caisse roulante`** | a **snareless** drum between side and bass drum — **not a tom** | v0.1 has no slot; `tom` would be wrong | 2 (T5 Forsyth p. 30, Widor p. 108, Read p. 8) | D02 §3.1 |
| Marching snare, marching tenor (multi-tom rack), **spock** (a.k.a. gock/shot drum), marching bass, marching cymbals | | **`marching.*` is a MISSING FAMILY** — not a member of `orch`; instruments, numbering and technique names are all distinct | 2 (T8 en.wp citing Udow p. 363, Blakley; T9 MuseScore/VDL) | D08 §5.2 |
| quads / quints / sextets / squints / hexes / sixpacks | 4 drums; +1 gock = quints; +2 = sextets | instrument configuration, not a term | 1 (T8 en.wp line 64) | D08 §2.6 |
| "gock", "shot" or "spock" **drums** | the 6″/8″ accent drums inside a multi-tenor arc — **the stroke name became an instrument name** | see §3 false friends | 2 (T8 en.wp line 64 citing Udow, Blakley) | D01 §2.7; D08 §2.6 |
| **Chinese Crash cymbal / large Turkish cymbal / small Turkish cymbal** | three distinct notation symbols in 1937 | a 1937 three-way cymbal distinction by **origin and size**, where v0.1 has `china`, `crash`, `cymbal` | 1 (T6 Bauduc 1937) | D02 §2.17 |
| `traps` | the collective noun for the auxiliary instruments; "two Tom-Toms and Cymbal, two Cow-Bells and Wood-Block" | | 1 (T6 Straight 1922 line 119) | D01 §2.3c; D02 §2.16 |
| `Große Wirbeltrommel` / `Grosse caisse roulante`; `Eine große Trommel mit zwei Klöppeln` | | | 1 (T4 Berlioz–Strauss p. 398) | D02 §2.10 |
| The Basel drum | two-headed cylinder, 40–41 cm shell measured outside, shell height = diameter, **eight** gut/synthetic snares plus metal on the **bottom** head, batter head damped by a `Dämpfer` | | 1 (T2) | D01 §2.14 |
| **`"snenor"`** (VDL `Drum n "snenor"`, `Spock "snenor"`) | a tenor drum voiced to **sound snare-like** | `voicing` **MISSING** — none of `standard/room/power/jazz/orchestra/lo-fi/dark` is about **imitating another instrument** | 0 traditions; 1 vendor | D08 §3.2 item 9, §5.2 |

## 1.13 Rudiment-list and cross-language name inventory (patterns, not pivot terms)

Recorded because they are the raw material for aliases, and because §4 shows the standards
bodies rename their own items.

| Set | Size / content | Locator |
|---|---|---|
| PAS International Drum Rudiments, 1984 | all 40 names verbatim, four groups (I.A/I.B/I.C single/multiple-bounce/double-stroke rolls, II Diddle, III Flam, IV Drag), with the sheet's own asterisk marking the **26** NARD items; arithmetic check holds (27 asterisks, one of which is the legend) | D01 §2.1 |
| NARD 26, 1933, in **NARD's own 1958 words** | recovered from the item metadata of Frank Arsenault's official Ludwig LP, one rudiment per track, in NARD's order; tracks 1–13 essentials, 14–26 second thirteen, 27–33 solos | D01 §2.2b |
| The 14 added in 1984 | single stroke four/seven, multiple bounce roll, triple stroke roll, six stroke roll, seventeen stroke roll, triple paradiddle, single paradiddle-diddle, single flammed mill, pataflafla, Swiss Army triplet, inverted flam tap, flam drag, single dragadiddle | D01 §2.2 |
| Hart 1860 four-character alphabet | "**a blow, a flam, a three roll closed, and a rest**" — one plain stroke, one 2-attack ornament, one 3-attack ornament, silence; every other figure "originates from" these four | D01 §2.3b |
| Nevins 1864 "Drum School" gamut | 30 numbered items verbatim, incl. **POING STROKES** (Hard / Middling Hard / Faint or Soft), FAINT FLAMS, HALF DRAG, FULL DRAG, **SLOW SAG** (defined nowhere), RUFFS, ROTAMACUE spelling, TRIPLE PARADIDLE at item 18 | D01 §2.3b |
| Greissinger 1900 event code | "**t** indicates tap; **f**, flam; **d**, drag; **r**, roll. The **figures under the rolls indicate the number of strokes in each roll**" — an event-type letter plus an attack count, 1900 | D01 §2.3c, §5.3-0 |
| Gardner 1918 contents | "All drum figures are based upon three fundamental beats technically called **roll, single stroke, and flam**"; then Five-/Six-/Seven-/Nine-/Ten-/Eleven-Stroke Roll and Four-Stroke Ruff | D02 §2.15 |
| Gevaert 1885 five French elements | `coup simple` (**ta**), `coup double` (**fla**), `coup de charge` (**tra**), `roulements partiels dits **ra**` (de 3/4/5/6/7 coups), `roulement continu` | D02 §2.13 |
| Rudimental Codex, 42 rudiments, trilingual | English + German/Swiss + French for all 42, from the compiler's own poster; items 2 and 3 are the bare pairs "loud-soft"/"soft-loud"; items 14 and 16 split the Coup de Charge by **nation** | D01 §2.13b |
| French system, 21+ classes | `frisé`, `frisé de 3/4/5`, `roulement`, `bâton mêlé`, `fla`, `fla inversé/flafla`, `coup de charge`, `coup anglais`, `bâtard`, `ra de N`, `frisé-sauté`, `flagada`, `patafla`, `coups coulés`, `pataflafla`, `moulin`, `volant`, `ra de 5 détaillé`, `raté-sauté`, `rigodon`, `coup de la Diane` | D01 §2.11 |
| German/Prussian layer | `Einzelschlag`/`Doppelschlag`/`Pressschlag`, `Wirbel`, `Offener`/`Geschlossener`/`Einhändiger Wirbel`, `Presswirbel`, `Mühle`, `Vorschlag`, `Druckruf`, `Doppelwirbel`, `Trommelstreiche`, `Schlepp`, `Schlepptriole`, `Schleppmühle`, `N er Ruf`, `Endstreich`, `Tagwachtstreich`, `Schweizer Ordonnanztriole`, prefixes `Umgekehrt-`/`Tripliert-` | D01 §2.12 |
| Competing current standards | NARD 26 · PAS 40 · Scottish 46 · **Rudimental Codex 42** (explicitly "to challenge the Percussive Arts Society interpretation … submitted to UNESCO") · Spalding's 5+22 · French conservatoire 34 (from a historical catalogue of 70+) · hybrid corpus 500+ and open · "more than 850" worldwide | D01 §4.4 |
| Sticking notations | EN/IT `R`/`L` (lower case = grace); FR `D`/`G`; ES `D`/`I`; DE `R`/`L` + `Führungshand`/`Nichtführungshand`; Strube 1870 encodes hand in **staff position** (left = E space, right = F space, rolls left-to-right = C); Hart 1860 upper/lower line; Greissinger 1900 `L`/`R` letters, the earliest found | D01 §2.10 |
| Basel verification table | `Schlepp`, `Doublé`, `5er/7er/11er/13er/15er Ruf`, `Bataflafla`, `Coup de Charge`, `Tagwacht` strokes, `Rigodon` all **verified**; `19er`, `Tupfen`, `Papamama`, `3er-Ruf-Tirole`, `Zündstoffschrift` **not found**; `Hieroglyphenschrift`/`Bergerschrift` verified as the two Basel notations | D01 §2.14 |
| Marching cymbal sound set, five packets | Port/Vertical Crash, Flat Crash, Orchestral Crash, Drop Crash, Crash Choke, Smash Crash, Hi-Hat, Press, Crunch, Sizzle/Sizz, Succ/Suck, Sizz-up/Sizzle-Suck, Tap, Ding, Tap Choke, Punch, Body Tap, Zing, Scrape, Tong, Wash, Weedwacker, Tap Sizz, Whale Call, "holding for snares", Garfield grip, Lock/West Coast vs Flow/East Coast | D08 §2.7 |
| MuseScore marching inventory | all 55 `.drm` entries and all 65 `instruments.xml` entries verbatim with pitches, staff lines and SMuFL glyphs | D08 §2.1, §2.2 |
| Tapspace VDL 2.5 articulation vocabulary | SnareLine, TenorLine, BassLine, CymbalLine keymaps in full | D08 §2.4 |
| **`guz`** (`Snare Guz Short` 53 / `Snare Guz Long` 54) | shipped by MakeMusic in **three** Finale editions; **absent from Tapspace's own 112-page manual**, from every packet, glossary and Wikipedia article; `guz ≈ crush` is **inference, UNVERIFIED, must not be minted** | D08 §2.4.1 |

**Term count for this section: 216 distinct terms/term-families tabulated.**

---

# 2. NO-AXIS TERMS — grouped by the missing thing

The brief says these are the most valuable finding. They are grouped by *what is missing*,
not by dossier. Nothing here has been forced onto an axis.

## A. A missing participant: the strike has more than instrument + implement

- **G3 On the knee / `Frappez sur le genou` / `Mit dem Knie`** (D02 §3.9). The *instrument*
  is moved against the *player's body*. Neither `implement` (the knee is not held) nor
  `site` (the site on the tambourine is unchanged) captures it. D02 calls it "a fourth kind
  of participant: the anvil surface". Read p. 214.
- **G16 One instrument used as the resonator/anvil of another**: tambourine *Placed on snare
  drum* (Read p. 220); Forsyth p. 33 tunes a kettle-drum to a drone, places the tambourine
  on it and plays the tambourine head with kettle-drum sticks. D02 §3.9.
- **G7 / "Beaters as Instruments"**: *Lay 1 stick on head of drum — strike with the other*
  (Read p. 198). v0.1 has `stick-shot` as a technique, which is right, **but the laid stick
  is simultaneously acting as `site`** — the model cannot say that an implement has become
  part of the instrument. Solomon names the general case at p. 95. D02 §3.9.
- **A2 The mount/hardware as a struck body**: `RH on cage` / `LH on cage` (the carrier frame
  of a marching snare), `Dress center harness hit`, `Tenor Stand click`, and the marching
  bass **metal click bar bolted to the rim**. None is head, rim, rim2, crossstick, shell,
  bow, edge, bell or underside. D08 §3.2 items 2, 3, 5; §5.1.3, §5.2.
- **G2 The bowl**: *Strike on copper kettle (of timpani)* — a third body, neither `head` nor
  `shell` as `shell` is defined for a kit drum. Read p. 164. D02 §3.9.
- **G1 The snares as a struck surface**: *On the snares / `Sulle corde` / `Sur le(s)
  timbre(s)` / `Auf den Saiten`* (Read p. 232). Distinct from `mechanism: wires-on`, which
  says whether they are *engaged*, not whether they are *struck*. D02 §3.9.

**What is missing:** `site` has no value for snares, bowl, jingles, bar-end, resonator or
hardware; and there is no way to express a participant that is neither the instrument nor a
held implement.

## B. A missing dimension: trajectory and continuum within one event

- **G12 Roll beginning at centre gradually going to the rim**, and its inverse (Read p. 212).
  A trajectory across `position` *within one sounding event*. v0.1 has point values plus a
  `strike_position.radial` controller but **no term**. D02 §3.9.
- **G12b "striking first at small end or tip and work up to Butt of sticks … keep moving up
  and down"** (Straight 1922, Lesson 53). The same trajectory shape on **`contact`**, which
  has three enum values and **no controller at all**, so it cannot be expressed even
  approximately. D02 §3.9, §2.16.
- **G13 Stop [dampen] half-way, and full** (Read p. 195). `damping` is nominal; this is
  ordinal *and* mid-event. D02 §3.9.
- **Angular position and rotation direction** (brush literature): clock-face position
  language (12/3/6/9 o'clock) is "the standard way the literature states a position on the
  head"; the half-note sweep is 7 o'clock → 2 o'clock and back; clockwise and
  counter-clockwise circles are described as musically opposite. v0.1's `position` is radial
  only and has no angular coordinate or rotation sense. D01 §2.8.

**What is missing:** every axis is a set of point values; several sources name a *path*.
`position` has a controller; `contact` and `damping` do not.

## C. A missing dimension: preparation and added mass

- **G8 Place a piece of paper on the drum head; a thin piece of felt on the middle of the
  head; a handkerchief over the head; triangle wrapped tightly in a cloth; Solomon's
  *Prepared Instruments*.** A preparation is **an object, of a material, added at a
  position**. `damping` has nominal values only and can carry neither material nor position.
  Read pp. 211, 212, 220; Solomon p. 245. D02 §3.9.
- **G9 Adding Mass; Sympathetic Resonance** — the same shape as G8 but the intent is
  pitch/resonance change, not damping. Solomon p. 248. D02 §3.9.
- **G17 Head tension as an expressive parameter of an indefinite-pitch drum**: *Out of tune
  (without pitch or resonance) / `Scordata` / `Verstimmt`*, *Tuned high / `Hoch gestimmt`*,
  *Well-tuned / `Ben accordato`*. Not `openness`, not `damping`, not `voicing`. Read
  pp. 211, 212, 232. D02 §3.9.

## D. A missing dimension: excitation type

- **G10 Bowing** (cymbal, crotale, vibraphone bar, xylophone bar end) — excitation by
  sustained friction with a bow; not a `technique` value, and the bow is not in `implement`.
  Read pp. 179, 195; Solomon p. 244.
- **G11 Friction roll / kept in vibration by friction on the edge / rub a rosined glove over
  a stick pressed to the head**. Continuous friction excitation: **different from `scrape`
  (transient) and from `roll` (discrete attacks)**. Read pp. 211, 219; Solomon p. 244.
- D02 §3.9. Related: VDL `Friction Slide 1/2` and `Drum n STIR w/dread` (D08 §5.2), which are
  the same excitation class in a vendor keymap.

## E. A missing dimension: orientation, mounting and holding position

- **G15 Laid on side / `Sul lato` / `Auf die Seite gedreht`** (bass drum); **Laid horizontal
  — without resonance** (gong); **Cymbal in the air / `En l'air` / `In der Luft`**. Read
  pp. 183, 198, 219. Orientation changes both radiation and damping. D02 §3.9.
- **G5 Cymbal fixed to the bass drum / to the foot-pedal**, and its negation *Bass drum alone
  (with cymbal detached)*. A **rig** fact: two instruments mechanically coupled so that one
  stroke sounds both. `mechanism` currently holds only per-instrument states. Read pp. 182,
  201; Berlioz–Strauss p. 418. D02 §3.9.
- **D08 §3.2 item 12: for marching cymbals the *holding position* is the primary organising
  dimension** — the packets are structured by position first and sound second (Garfield grip,
  Port, Flat, Orchestral, Choke, Vert, Tap; Ohio State adds Traditional, Vertical A/V,
  Traditional hi-hat, **Gumption**, **Punch** as *positions*). The pivot has no analogue of
  "instrument orientation" for a two-plate instrument.
- **G20 Off-stage** — a section heading in five of Read's seven percussion chapters
  (pp. 174, 202, 216, 222). Spatial placement of the *player*. D02 §3.9.

## F. A missing dimension: ensemble cardinality and performer count

- **G6 Two players (on same part) / `Due esecutori` / `Zwei Spieler`**, and *3 Drums, I: f,
  II: mf, III: p* (Read pp. 172, 211, 212). A performer count and a per-instance dynamic
  assignment; `instance` is a layout-slot property, not a multiplicity. D02 §3.9.
- **D08 §3.2 item 1: `unison` / `split part`.** MuseScore ships `Unison`, `Unison Hits`,
  `Unison Rims`, `Unison Rimshots` as ordinary drumset entries and VDL ships five `UNISON *`
  keys. Physically these are not a sound at a site — they are *"every instance in this
  section, together"*, with `split part` as the named counterpart (Bailey & Caneva ch. 8
  p. 132 via en.wp line 79). **This is a section-cardinality relation and needs a rule, not
  a term.**
- **D08 §3.2 item 6: Solo vs section** (`Solo HITS` vs `MAIN HITS`; VDL's cymbal keymap has
  an upper "unison cymbal section" range and a lower "solo cymbal player" range). Not
  `dynamic`, not `voicing` — an ensemble-size dimension.

## G. A missing dimension: the motion, not the sound

The single largest family in D01, and D01's own verdict is that **this is the correct
answer** — but it must be written down, because "any future contributor will try to add
`full-stroke` to the `technique` axis" (D01 §3.3).

- **Stroke type**: full stroke, down stroke, up stroke, tap/low stroke, buzz stroke; the
  three wrist positions (up position, tap position, rest position). These name the
  **preparation and termination height** of the motion, not the sound; two identical-sounding
  notes differ only in what the stick does afterwards. **PAS itself teaches exactly these
  four** (Viña, *Educators' Companion* vol. 7, Fall 2019), which makes this the most-taught
  vocabulary in the whole bucket, mapping to nothing.
- **Technique school / motor system**: Moeller (whipping/wave motion, dual fulcrum), Gladstone
  free stroke (full/half/low), push-pull, Freehand/gravity (Johnny Rabb, 1995), heel-toe,
  slide, swivel, single vs double bass pedal. Their only audible trace is attack count and
  spacing.
- **Grip**: matched, German, French, American, traditional/classic, little-finger (vintage)
  fulcrum, thumb fulcrum, thumbs-up, **Garfield grip**, Pistol grip, and the Casey Claw's
  **fist**. Fits neither `implement` nor `contact`. (Note: the *fist* as a **striking body**
  does belong on `implement` — see §1.2 — but the fist as a *grip on a stick* does not.)
- **Crossover, stick cross, arm cross; helicopters, butterflies, figure eights** (D08 §2.6).
- **`Visual`** — MuseScore's own 2013 name for pitch 60 was `Visual (BS,X-Over,Etc)`, and
  en.wp groups back-sticking and stick tosses as visual embellishments. **A whole class of
  marching notation exists to trigger a *movement* that may or may not sound.** No axis
  covers "this note is choreography". D08 §3.2 item 8.
- **Lock / West Coast vs Flow / East Coast** cymbal technique — a school-of-playing dimension
  that changes the attack envelope of *every* crash. D08 §3.2 item 11.

Locators: D01 §3.3; D08 §3.2 items 8, 11, 12.

## H. A missing dimension: stroke envelope / duration

Two 1860s primaries **disagree about whether a drum stroke has a duration at all**:

- Hart 1860 builds his entire four-character notation on the claim that "all Blows, Taps,
  Flams, or Single Beats have but **one length of sound** on the Drum".
- Nevins 1864 contradicts him four years later with a graded pair: `Poing Stroke` = "sudden,
  **hard, short**" against No. 10 = "**soft, long, drawing**".

D01 §5.3-5's verdict: for a *sampled* pivot Hart is right and no envelope axis is needed
because the sample carries the envelope — but the question was asked and answered **by the
source material**, not by assumption, and that is worth recording. D01 §2.3b, §3.3, §5.3-5.

Adjacent: roll **length and shape** as first-class properties (`SHORT`/`MEDIUM`/`LONG`, `FP`
forte-piano, crescendo/decrescendo) in VDL, and MuseScore modelling `buzz` as a **discrete
note** where every vendor and teaching source treats it as a **sustained** articulation with
length and dynamic shape (D08 §4 item 11, §5.2).

## I. A missing relation: intra-ornament accent placement

- **G14 `le coup de charge` (*tra*)** is distinguished from *fla* **only by which of the two
  strokes carries the rhythmic accent** (Gevaert p. 332: "l'accent rythmique tombe sur la
  note brève"). No axis carries intra-ornament accent placement. D02 §3.9.
- The Rudimental Codex makes exactly this relation **elementary**: its items **2 and 3** are
  the bare pairs "loud-soft" and "soft-loud", ranked **above the flam**, and its entire
  sticking legend is four glyph classes = hand × volume. v0.1 has no way to say "this attack
  is the soft half of a loud-soft pair". D01 §2.13b, §5.2.
- Hart 1860 defines the flam itself as nothing but this dynamic relation ("a very soft, fine
  blow … and a full heavy blow immediately following"). D01 §2.3b.

**Three independent traditions (T1, T2, T3) name a two-attack figure whose identity is a
dynamic/accent relation rather than a timing offset.** This is the strongest no-axis finding
in the ornament layer.

## J. A missing token: reset / "return to normal"

- **G19 Return to a "Normal" Method of Playing** (Solomon pp. 71, 239). Read supplies four
  languages for it — `Modo ordinario` / `Position ordinaire` / `Gewöhnlich` / `nat.` The
  model has **no "clear all non-default axes" term**. D02 §3.9.

## K. Named single-token effects with no decomposition

- **Whale Call, Weedwacker, Bizbop, Pea Soup** (D08 §3.2 item 10) — genuinely idiomatic
  single-token sounds that do not decompose into site/technique/implement.
- **`SLOW SAG`** (Nevins 1864 item 24) — appears in no later list reached and no source
  defines it. Recorded as an unexplained 1864 name. D01 §2.3b.
- **`guz`** (`Snare Guz Short`/`Long`, three Finale editions) — a real term in a shipping
  product map with **no published definition anywhere reachable**. D08 §2.4.1.
- **Imitative voicing (`"snenor"`)** — `voicing` exists but no value is about *imitating
  another instrument*. D08 §3.2 item 9.

## L. Above the pivot: patterns, lists and directives

Recorded so that no future contributor mints them (D01 §3.3, §5.3-4, §2.15):

- All 40 PAS names, all 26 NARD names, ~500 hybrids, all 21 French classes, the Basel
  `Grundstreiche` — these name **sequences of notes with a sticking**. "`paradiddle` is not a
  sound; it is four sounds and an assignment of limbs."
- Sticking patterns `RLRR`, `DGDD`, `DIDD`, lead hand, hand-to-hand: per-note this collapses
  to `limb`; the *pattern* is above the pivot.
- Practice directives: "open (slow) to close (fast) to open (slow)", "at an even moderate
  march tempo".
- Notation-only conventions: Strube's E-space/F-space hand encoding, Hart's upper/lower line
  flams, stem slashes for diddles.
- **Hybrid rudiment names are explicitly ruled out of scope**: they name sequences, there is
  no owning body, the list is open and growing ("507 Hybrid Rudiments", whose own footer asks
  readers to send in more), and the names are neither stable nor unique. D01 §2.15.
- **`Battery Snare`** is a **section label, not a stroke name** — do not mint it. D08 §5.1.4.

---

# 3. FALSE FRIENDS

## 3.1 One word, different meanings

| Word | Meaning A | Meaning B (and C, D) | Locator |
|---|---|---|---|
| **`timbre` / `timbro`** | KITWARP axis: acoustic vs 808 vs FM | **FR/IT orchestral: the snare wires.** `sans timbre` = snares off, `avec timbre(s)` = snares on, `détimbrée` = de-snared; `caisse claire` is named for it. **Any importer that sees `timbre` in a French or Italian source string and resolves it on the `timbre` axis silently destroys a `mechanism` value.** D02 says this needs flagging in `rules.json`, not burying in a table | **D02 §0.1(b), §2.6 p. 209–210, §2.12, §4 item 1** |
| **`open`** | modern: un-closed (open roll = double-stroked and audibly separated; open hi-hat = cymbals apart) | **Hart 1860: soft and light.** "the full **open** flam … the full **open** blow … the full **open** three roll … will be executed **soft and light**"; a soft roll is written with an "**open figure**" numeral | D01 §2.3b, §4.1 |
| **`rim`** | Read *At the rim **of head*** (p. 163) = a radial **position on the membrane** | Read *On the rim **of the drum*** / *On the wood* (p. 197) = the **hoop**. Both translate to English "rim"; in KITWARP terms `position: perimeter` vs `site: rim`. **Any importer that maps the word "rim" to one axis will silently mis-file the other** | D02 §4 item 8 |
| **"struck with the wood"** | cymbals (Read p. 184): the wooden **shaft** of a beater = `contact: butt` | drums (Read p. 200): the wooden **hoop** = `site: rim`. Same English phrase, two axes | D02 §4 item 9 |
| **rimshot** | kit/marching: one stick strikes rim **and** head together | orchestral: one stick is **laid on the head**, shaft pressed to the rim, struck by the *other* stick (= stick shot). Also: the comedy **sting**, "often called a rimshot, although some versions do not include a rimshot in the technical sense" | D01 §4.1; D08 §2.5 |
| **`gock`** | (a) a rimshot with the bead at the **centre** of the head | (b) the 6″/8″ **accent drum** on a multi-tenor rack (= spock = shot drum); (c) `gock block`, a plastic woodblock substitute. **A parser that maps "gock" to an instrument will collide with one that maps it to a stroke** | D08 §4 item 1; D01 §4.1 |
| **`shot`** | on a tenor = **rimshot** (`Drum 1 Shot`) | in `shot drum` = the small accent drum; in `stick shot` = neither | D08 §4 item 2 |
| **`cross stick`** | Blakley sense 1 = the laid-flat stick struck against the rim (kit sidestick) | Blakley sense 2 = one stick pressed to the head struck by the other — **which is the stick shot**. en.wp warns explicitly that "the rimshot is often confused with the cross stick technique" | D08 §4 item 6 |
| **`rim click`** | on a snare: the stick tapping the rim | on a marching bass: a strike on a **metal bar bolted to the rim** | D08 §4 item 7 |
| **`drag`** | PAS/NARD: two **diddled** grace notes before the primary | Scottish pipe band: "a flam where the grace note is played as a **deadstick** (staccato note)" | D01 §4.1 |
| **`ruff`** | historically: `llR` played **closed** (the open version was *half drag*) | modern American: `rlR`, two **single** grace notes | D01 §4.1 |
| **`roll`** | orchestral / German band default: **closed** (buzz) — in German and Austrian wind-band march music the closed roll is used *exclusively* | rudimental / drum corps default: **open** (double stroke), used almost exclusively | D01 §4.1 |
| **press roll / `Pressschlag`** | drum-set: the multiple-bounce roll; German `Presswirbel` is the same | but German **`Pressschlag` is the *single* pressed stroke** — and Bauduc's `press roll` is a third thing again, a six-variety Dixieland device distinguished by *where the press falls* | D01 §4.1; D02 §2.17 |
| **`mill` / `Mühle`** | American `mill stroke`: reversed paradiddle `RRLR` | German Wikipedia `Mühle`: the **preparatory double-stroke exercise**; the Rudimental Codex `Mühle`: the plain **single paradiddle**. **Three senses of one word inside German alone** | D01 §4.1 |
| **`French`** | `French roll` = triple stroke roll | `French grip` = palms-inward matched grip | D01 §4.1 |
| **`splash`** | `splash cymbal`, an instrument | hi-hat `foot splash`, a technique. v0.1 carries both | D01 §4.1 |
| **`dead`** | orchestral `dead stroke`: mallet held against the bar | rudimental `deadstick`: a grace note that does not rebound. v0.1's `technique: dead` is ambiguous between them | D01 §4.1, §5.1 |
| **`chick`** | hi-hat foot close | German literature also uses `chick` loosely for a general background hiss/rustle texture | D01 §4.1 |
| **`tap`** | modern: the low stroke, one of the four stroke types | Nevins 1864 **TAPS** = a bugle/drum **signal** ("a signal for the front to advance slow"); Hart lists "Blows, **Taps**, Flams" as interchangeable names for one plain stroke | D01 §4.1 |
| **`bell`** | v0.1 `instrument: bell` (id 17, a kit cymbal bell as a separate pad); v0.1 `site: bell` (the cup of a cymbal) | Read p. 8 **`Bells` = tubular chimes** / `Campane` / `Cloches` / `Glocken`, with `Chime-Bells` = glockenspiel; Read p. 199 "On the **bell** [body]" of a *drum* = the shell. **Four readings of one word** | D02 §4 item 2 |
| **`Tambourin` (FR)** | the **Provençal tabor**, a long snareless drum played with one stick | *not* the tambourine, which is `tambour de basque`. `Tamburino` (IT) **is** the tambourine; IT `Tamburo` is the side drum | D02 §4 item 3 |
| **`Becken` vs `Teller`** | German `Becken` = the cymbal | `Teller` = the individual plate; `Mit Teller(n)` = clashed as a pair, `Becken frei` = suspended. English "cymbal" carries neither | D02 §4 item 4 |
| **`cassa`** | IT `cassa` = the **shell** of a drum ("sulla cassa") | but `gran cassa` = the **bass drum**; and FR `caisse claire` = the **snare** drum | D02 §4 item 5 |
| **`Schlägel` vs `Klöppel`** | Berlioz–Strauss: `Klöppel` = specifically the bass-drum beater, `Schlägel` generic | Read's German column uses `Schlägel` for both, and `Stiel des Klöppels` for "handle of the stick" | D02 §4 item 6 |
| **"muffled" vs "dampened"** | Read 1953: *Dampened* = stop the sound **after** it starts; *Muffled* = alter it **before** it starts — kept as separate chapter sections throughout Part IV | Solomon 2016 collapses all three English words into one heading, "Muting (Muffling, Dampening)". **The 1953 distinction is the one KITWARP needs; the 2016 conflation is the one most vendor lists inherit** | **D02 §2.1, §4 item 7, §5.3** |
| **`slam`** (marching cymbal) | Oregon State: "quickly press the cymbals together to create an **air pocket** sound" — i.e. a suck | GVSU: a synonym of **Press/Crunch** — a damped closed sound. Rhythm Armada: press with force "**in a slightly offset position, so as to avoid an air pocket**" — the exact opposite of a suck. **Three programmes, three incompatible meanings** | D08 §4 item 4 |
| **`ding` / `ting`** | GVSU lists `Ting, Ding` as synonyms of a plain **Tap** | two pages later GVSU defines **Ding** as the strike into the **bell**, "also referred to as a Bell Tap, Dong, Gong". **Within one document "ding" names two different sounds** — and MuseScore ships `Ting` at the bell-tap pitch, i.e. spelled from the wrong side of a documented ambiguity | D08 §4 item 3, §2.8 |
| **`crunch`** | the blog: a forceful hi-hat slam | GVSU: a synonym of **Press**; VDL: `Crunch Choke` is a key **distinct from** `Hi Hat Choke`. MuseScore writes `Crunch (HH)`, hedging | D08 §4 item 8 |
| **`punch`** | GVSU: a **choked tap** from the choke position | MuseScore `.drm` puts `Punch` at pitch 79, which `instruments.xml` calls `Crash-Choke` — **a choked crash is not a choked tap**. Ohio State independently records `Punch` as a **low holding position** ("tops at the level of the armpits … an upside-down 'V'"), corroborating the mislabel | D08 §4 item 5, §2.7.1, §2.8 |
| **`tenor drum`** | marching: the multi-tom rack | orchestral: a single deep **snareless** drum between side and bass drum. MuseScore's `marching-tenor-drums` declares `musicXMLid` `drum.tenor-drum`, which collides with the orchestral instrument | D08 §4 item 9; D02 §3.1 |
| **`buzz`** | MuseScore: a **discrete note** | every vendor and teaching source: a **sustained** multiple-bounce roll with a length and a dynamic shape | D08 §4 item 11 |
| **`sweep` / `scrape`** | marching **tenor**: interchangeable names for one motion (a double split between two drums) | marching **cymbal** `scrape` is a cymbal-on-cymbal motion, unrelated. "Marching tenor `scrape` and marching cymbal `scrape` are unrelated" | D08 §4 |
| **drawing stroke** | Nevins 1864 No. 10: a legitimate stroke, "soft, long, drawing" | Hart 1860: **forbidden** — "make **no drawing strokes** or sideway beats in no case whatever, although it has been recommended by many professional teachers of drumming" | D01 §4.1 |
| **`blow`** | 1860–1864: the standard word for a plain single stroke | absent from every modern list reached | D01 §4.1 |
| **`Batafla` vs `Bataflafla`** | Codex `Batafla` = **flam accent** | Codex `Bataflafla` = **pataflafla**. One syllable apart, different figures | D01 §4.1 |
| **`Coup de Charge`** | Swiss form | French form — the Codex lists them as **two separate rudiments** (#14 and #16) | D01 §4.1, §2.13b |
| **`Doublé`** | claimed (from a forum) to be "a Schleppstreich doubled by a quiet preceding Tupfen" | **verified** in the Codex as the Swiss name for the **Inverted Flam Tap / Flam and Stroke / Coup Anglais** — i.e. the received description was wrong | D01 §2.14 |

## 3.2 Different words, one meaning

| The one thing | The names | Locator |
|---|---|---|
| tip on head, butt against rim, hand muting | **cross-stick = rim click = side-stick** (all three in one sentence) | D01 §4.2 |
| double-stroke roll of indeterminate length | **long roll = double stroke open roll** = `roulement` = `bâton rompu` = `Doppelschlagwirbel` = `Offener Wirbel` = `redoble abierto` = `rullo a colpi doppi` | D01 §4.2 |
| pressed multiple-bounce roll | **buzz roll = closed roll = press roll = multiple bounce roll** = `Presswirbel` = `Druckruf` = `trizzlet` (Scottish) = `Ra stroke` (Dutch) = `Redoble de Zumbido` (Spanish) = `Los Rufaos` (Bajoaragonés) = `Rullo` (Eporedian) = `Rau Tau` (Mexican) — **the widest synonym set in these dossiers** | D01 §4.2 |
| 3-attack roll | **drag = half drag = ruff = 3-stroke roll** = Hart's **three roll** = `ra de 3` = `tra` = `3er Ruf`. Nevins 1864 keeps **half drag, full drag, single drag, double drag and ruffs as five separate gamut items** where PAS has one `Drag` | D01 §4.2 |
| plain single stroke | **blow = tap = single beat = Poing Stroke** (when hard and short) = `Einzelschlag` = `coup simple` = `golpe único` = `colpo singolo` | D01 §4.2 |
| stop the sound after it starts | `Étouffez` = `Secco` = `Dämpfen` = **Choke = Damp = Dry = Off = Short = Stop (quickly)** — Read p. 163 lists **eight English synonyms for one action** | D02 §4 |
| the default beater | **Ordinary = Regular = Usual** beater = **hammer = mallet = stick = striker** — seven English words in one Read entry | D02 §4 |
| snares off | **Snares off = No snares = Without snares** = `Senza timbro` = `Senza corde` = `Sans timbre` = `Détimbrée` = `Ohne Schnarrseite`, plus the separate *slack* variants; **ten English forms at Read p. 209** | D02 §4 |
| play at the edge | `Blousé / blouser / blousée / blousez` (FR) — used for **both** timpani and cymbals, and **absent from every modern list examined** | D02 §4 |
| one-handed roll using the rim as fulcrum | **fulcrum roll = gravity roll = freehand roll = gravity blast** = `Einhändiger Wirbel` | D01 §4.2 |
| sizz-up (cymbal) | **sizz-up = sizz-succ = sizzle-suck = slide choke = fusion = bizbop = pea soup** — six names for one sound, "the worst case found in this bucket" | D08 §4 |
| the closed pressed cymbal sound | **press = crunch = crush = closed sizzle = slam** | D08 §4 |
| the bell strike | **ding = bell tap = dong = gong** | D08 §4 |
| the choked tap | **tap choke = vertical punch = vertical smack = vertical slap choke = skank = slap choke** | D08 §4 |
| the dead tap | **body tap = dead tap = click** | D08 §4 |
| the vacuum sound | **succ = suck = vacuum** = (MuseScore) `suc`; VDL `Vacuum Suck` | D08 §4 |
| the muffled rimshot | **skank = muffled shot = spank** (Blakley's spank has the muffle *independent* rather than simultaneous — a real physical difference inside the synonym set) | D08 §4 |
| the small tenor drum | **gock drum = shot drum = spock drum** | D08 §4 |
| a set of tenors | **quads = quints = sextets = squints = hexes = sixpacks = "tenors"** | D08 §4 |
| the vertical crash | **port = vertical = vert** | D08 §4 |
| the stick shot | **stick shot = cross stick (sense 2) = "stick on stick"** | D08 §4 |
| flam paradiddle | = **flamadiddle**; inverted flam tap = **tap flam** = FR `coup anglais` inverted | D01 §4.2 |
| the onomatopoeia of the double-stroke roll | **"Mammy-Daddy"** (US 1900) = `Mama-Papa` (DE) = `papa-maman` (FR) | D01 §2.3c, §4.2 |
| gock | = **sprock** (UNVERIFIED — attributed to snarescience.com, HTTP 500) | D01 §4.2 |

## 3.3 The same list, respelled by its own owners

- **The standards body respells its own list across revisions.** Comparing NARD's official
  1958 recording with the 1984 PAS sheet gives exactly four renamings: `The Long Roll` →
  `Double Stroke Open Roll` (descriptive-of-*sound* → descriptive-of-*sticking*); **`The Ruff`
  → `Drag`** (one name displaced another for the same figure); `The Single Drag` → `Single
  Drag **Tap**`; `The Double Drag` → `Double Drag **Tap**`. Plus `No. 1`/`No. 2` → `#1`/`#2`
  and `Paradiddle-Diddle` losing a capital. D01 §2.2b, §4.3.
- **Vic Firth**, the largest distributor of the PAS list, respells it (`Patafla-Fla`,
  `Flammed Mill`, numerals for spelled-out numbers) and reorders the 40 into four difficulty
  tiers that cut across the PAS I–IV grouping entirely. Italian prints `flam
  paradiddle-didle` and `Single Dragadiggle`; Spanish glosses `flam` as `mordente`. D01 §4.3.
- **MuseScore contradicts itself in two shipped files**: `.drm` vs `instruments.xml` disagree
  on pitch 53 (`Cross Stick` vs `Rim Click`), on pitch 79 (`Punch` vs `Crash-Choke`), on
  pitch 84 (`Ting` vs `Bell Tap`), on pitch 89 (`Suc` vs `Smash` — **two real but different
  sounds on one pitch**), and on **Spock ordering** (`.drm` puts Spock 1 above Spock 2;
  `instruments.xml` puts Spock 2 above). D08 §2.8, §4 item 10.
- **Consequence stated by D01 §4.3:** "the rudiment names are *not* a controlled vocabulary
  even where a standards body owns them. Any mapping table keyed on rudiment name must carry
  aliases, and the alias set has to span revisions of the *same* list, not just rival lists."

---

# 4. GAPS AGAINST v0.1

Measured against `vocabulary/axes.json` v0.1.0 serial 1 (13 axes, 132 values), `pivot.json`
(155 terms, kit only), `rules.json`. ADR-0003 §5 clause 2 governs every remedy: **a wrong
slug is fixed by a `correction` alias, never by a rename**; ADR-0001 makes adding an *axis*
a MAJOR bump and a re-curation, while adding axis *values* is cheap.

## 4.1 Minted with no source, or with a wrong source

| v0.1 item | Problem | Evidence | Remedy consistent with ADR-0003 |
|---|---|---|---|
| `technique: gok-shot` (axes.json id 8; `snare.gok-shot` id 1025) | The spelling `Gok` occurs in **exactly one place** outside KITWARP: MuseScore `Marching_Snare_Drums.drm` pitch 52, added 2024-07-27 by commit `c7dc55ea2d` from **Muse Drumline's** definitions. `git log -S "Gok"` over all of MuseScore returns that one commit. Tapspace's 112-page manual **never uses the word in any spelling**. The field spelling is **gock**, variant **gawk**, and the only definition of the *concept* anywhere is an **uncited** en.wp *Rimshot* paragraph. Where "gock" appears in sourced reference works it usually means **the tenor drum**, not the stroke | D08 §0, §2.5, §5.1.1; D01 §5.1 | keep the id and slug; add `correction` alias `gock-shot` and alias `gawk-shot`; provenance record must read "Muse Drumline, single vendor, concept uncited" |
| `technique: back-stick` (id 6; `snare.back-stick` id 1023) | D01 §5.1 recommends marking it **UNVERIFIED** because it found no attestation. **That recommendation is wrong and must not be carried forward** — see §6.1 | **D08 §2.5.1** | mint with the Marrella/Dowlan/Mirsky provenance chain, not UNVERIFIED |
| `technique: rim-only` (id 3; `snare.rim-only` id 1020, `tom.rim-only` id 1047) | "**Not a term any reached source uses.** The literature says rimshot, rim click, cross stick, side stick, or (marching bass) 'rim click' on a metal bar" | D01 §5.1 | keep the id; record that it is a **KITWARP coinage with no literature attestation** |
| `technique: foot-splash` (id 24; `hihat.pedal.splash` id 1093) | Weakly attested. en.wp *Hi-hat* names `chick`, `pedal hi-hat`, open, closed and `cooking` but **not** foot splash; the §2.9 definition comes from a search-result summary whose underlying pages returned empty or 403 | D01 §2.9, §6.3 | needs a kit method book before the provenance record can claim a source |
| `site: rim2` (id 3) | "has **no counterpart anywhere in this literature**. It is an e-drum zone name … `rim` and `rim2` cannot be populated from any orchestral source, and a mapping that guesses will be wrong" | D02 §5.2 item 5 | fine as an e-drum term; the rule must forbid populating it from treatise sources |
| `technique: slide` / `swivel` (not in v0.1 — correctly absent) | search-summary only in D01; do **not** mint | D01 §2.9, §6.3 | — |
| Anything minted from `guz`, `Half Crash`, `whale-call`, `weedwacker`, `crunch-choke` | `Half Crash` has shipped in MuseScore since 2013 and is attested in **no source reached at all**; `guz` is in three Finale editions with **no published definition anywhere**; `whale-call` and `crunch-choke` are Tapspace-only; `weedwacker` is GVSU-only | D08 §2.7.1, §5.1.5, §2.4.1 | do not mint, or mint with `confidence` recorded as single-source |

## 4.2 Misnamed / on the wrong axis

| v0.1 item | Problem | Locator |
|---|---|---|
| `technique: ping-shot` + `gok-shot` + `rimshot` as three sibling **techniques** | **Every authority reached describes them as ONE technique (rimshot) at THREE striking positions**: ping = bead ~1″ from rim, normal ~3″, gock = bead at centre with the rim contacted by the shaft near the hand. Modelling them as siblings means **a converter cannot tell that a ping shot is a rimshot** | **D08 §2.5.2, §3.1, §5.1.2**; D01 §2.7 |
| `technique: sidestick` (id 4) **and** `site: crossstick` (id 4) | The same physical action modelled on **two axes at once**; cross-stick, rim click and side-stick are three names for one thing. Orchestral sources cannot even disambiguate `sidestick` from `rim-only` — Read's *On the rim / On the wood / Rand mit Holz geschlagen* (p. 197) is the ancestor of both and does not distinguish them | D01 §5.1; **D02 §5.2 item 6** |
| `ornament: ruff` (id 3, attacks 4) vs `ornament: drag` (id 2, attacks 3) | v0.1 treats them as two ornaments. In the current PAS standard they are **the same figure** (#31 printed `Drag`; NARD calls it "drag (half drag or ruff)"; NARD's own 1958 track 8 is "The Ruff"). The historical distinction was **open vs closed execution**, not two figures. The genuinely distinct item is the American **3-stroke ruff** `rlR` (single-stroked graces), which is on no official sheet but is defined in Nevins 1864 | D01 §5.1 |
| `technique: heel` (13) / `technique: toe` (14) | These read as two contact points, but the literature's **heel-toe is one compound motion producing two attacks**, and the source is explicit that "it's the ball of the foot (or toes) both times". The real per-note distinction is heel-**down** vs heel-**up** posture, which is **inaudible** | D01 §5.1 |
| `technique: dead` (22) | Ambiguous between orchestral *dead stroke* (implement held on the bar) and rudimental *deadstick* grace note | D01 §5.1; D02 §3.5 |
| `instrument: sticks` (id 34) | **Collides with `implement: stick`.** In every source in D02, "sticks" means the beater; the instrument a kit calls "sticks" is **`claves`** in the orchestral literature | D02 §5.2 item 1 |
| `instrument: chimes` (id 38) | Ambiguous: Read separates tubular chimes/`Campane`/`Cloches`/`Glocken` from glockenspiel/`Chime-Bells`; Solomon separates Church Bells from Mark Tree/Bell Tree from Bamboo Wind Chimes. **A kit "chimes" pad is almost always the mark-tree sense; the orchestral "chimes" is always the tubular-bell sense. The single slug cannot carry both** | D02 §5.2 item 2 |
| `instrument: cymbal` (id 18) | **Cannot express pair-vs-suspended**, which the literature treats as an instrument-level distinction with its own nomenclature and its own chapter. `crash` in v0.1 is a *suspended* cymbal; **there is no slot for `piatti` / clash cymbals at all** — and the entire marching cymbal line is a clash pair | D02 §5.2 item 3; D08 §2.7 |
| `damping: towel` (id 3) | A drum-kit-ism. The literature's word, in four languages, is *muffled / con sordino / coperto / voilée / bedeckt / gedämpft*. `towel` names the **means**; the sources name the **effect** | D02 §5.2 item 4 |
| `dynamic: accent` (id 4) | Read p. 214 records a score in which the accent sign `>` **is the technique marker** ("L'accent ( > ) indique le coup frappé avec le poing"). A parser reading `>` as `dynamic: accent` **loses a technique**. Worth a note in `rules.json` | D02 §5.2 item 7 |
| `timbre` axis name | Collides with FR/IT `timbre` = snare wires. Needs a `rules.json` flag, not a table footnote | D02 §0.1(b), §4 item 1 |
| `mechanism` (4 values) misses the **usual** case | Three independent traditions give **snares slackened** as the *usual* muffling practice, not an edge case; v0.1 offers only `wires-on`/`wires-off` | D02 §5.1, §5.3 |
| `voicing` (7 values) | No value for **imitative** voicing (`"snenor"` = a tenor voiced to sound snare-like); `dark` is about tone, not imitation | D08 §3.2 item 9, §5.2 |
| `instance` direction rule | ADR-0001 fixes it once — "toms high to low in pitch, cymbals left to right from the player's seat". **That does not decide a marching bass line** (five separate players, largest to smallest left to right on the field, but numbered 1 = smallest) **or a tenor rack** (drums 1–4 high to low, spocks numbered separately and inconsistently). "MuseScore contradicts itself on spock ordering precisely because the rule was never written down." Ordering must be declared **per family** | D08 §5.3 |
| `limb` as specified | **UNVERIFIED** whether it can express "left hand of the pair on **this one** instrument" — a marching snare has two hands on one drum and the libraries sample them separately (`RH backstick`/`LH backstick`, `AutoRL`) | D08 §3.2 item 7 |

## 4.3 Missing values the literature demands

**`ornament`** (v0.1 has 9 values, none with a count field):
- **an attack count** — the single most-repeated structural finding across all three
  dossiers. `.agents/round2/BRIEF.md` already says ornament carries "an attack count";
  `axes.json` has **no field for it**. The count vocabulary is 3, 4, 5, 6, 7, 8, 9, 10, 11,
  12, 13, 14, 15, 16, 17 and the Scottish 25. The odd/even accent rule means the count is not
  decorative: an even-count roll ends on **two** accented notes, an odd-count roll on one.
  D01 §5.3-1; D02 §3.6, §5.1, §5.3.
- **flat flam / double stop / unison** (both hands exactly together). D01 §5.2.
- **charge stroke / `coup de charge` / `tra`**, with the Codex carrying **two** of them
  (Swiss and French) plus a *Flammed* form. D01 §5.2; D02 §3.6, §5.1.
- **open flam** as distinct from flam. D01 §5.2.
- **deadstick grace note**. D01 §3.2.
- **press-roll** (Bauduc's six varieties). D02 §5.1.
- **thumb-roll** as distinct from `roll` — Widor is explicit that it **cannot be sustained**.
  D02 §5.1.
- **crush**, with `fat-crush` / `dry-crush` / `wet-crush`. D08 §5.2.
- **diminuendo** to pair with `crescendo`; roll **length** (`SHORT`/`MEDIUM`/`LONG`) and `FP`
  shape. D08 §5.2.

**`technique`**: bow, friction-roll, fist, knuckle, fingernail, knee, pitch-bend, vibrato,
cluster, harmonic, two-plate-stroke (D02 §5.1); skank, spank, stir, friction-slide, rim-knock;
and for the cymbal line suck, sizzle-suck, crunch, smash, ding/bell-tap, tong, zing, tap,
body-tap, weedwacker (D08 §5.2); rim roll, rim buzz, trill, pulled double / whipped cream,
legato push, palm-up snap (brush, D01 §5.2); stick-on-stick roll, coup de douille (D01 §5.2).

**`site`**: snares, kettle/bowl, wooden hoop distinct from metal counterhoop, batter-head as
the explicit counterpart of `underside`, jingles, bar-end, resonator (D02 §5.1);
cage/mount/hardware, and the marching-bass **click bar** (D08 §5.1.3, §5.2).

**`contact`**: **fan** (brush accent surface) as distinct from tip (D01 §5.2). Aliases missing
for *thick end*/*thin end*/`Holzschaft` (D02 §5.1). **And `contact` has no controller**, which
makes Straight's tip→butt continuum inexpressible (D02 §3.9 G12b).

**`implement`**: sponge (the historically dominant timpani beater, "die besten"), leather,
rawhide, cane, rattan, cotton, wool, fibre/capoc head, steel, iron, metal, plush, padded,
two-headed stick, triangle-beater, chime-hammer, knitting-needle, coin, bow, saw-blade,
rosined-glove (D02 §5.1); clog mallets, sand blocks, leather straps (D02 §3.8); dread, felt,
puffy-mallet, aluminum-mallet, plate/cymbal-on-cymbal (D08 §5.2); **fist and fingernail**,
which the round-2 brief lists and `axes.json` does not carry (D01 §5.2; D02 §5.1; **D08
§5.2**). Plus a **hardness qualifier orthogonal to material** — v0.1's
`mallet-soft/medium/hard` folds the two together and cannot express "medium-hard **leather**"
where Read carries eight hardness grades on rubber, felt and leather independently (D02 §5.1).

**`damping`**: prepared (paper, felt, cloth *on* the head), **half** as an ordinal step, and
choke for cymbals as distinct from `damped` (D02 §5.1).

**`mechanism`**: **wires-slack** (three independent traditions call it the *usual* practice),
**wires-tight** (`Très timbrée`), cymbal-coupled-to-kick, pedal-bass-drum (D02 §5.1).

**`dynamic`**: an **ordered** scale — v0.1's five values are an unordered set, while marching
practice uses a 1″–15″ height scale, PAS teaches accent/tap as a *height* relation, and Nevins
1864 already names an ordered three-step scale Hard / Middling Hard / Faint or Soft applied
independently to strokes, flams **and** rolls. Plus **faint / feathered**, a level below
`ghost`. D01 §5.2.

**`position`**: no missing *values* — but v0.1's four are radial and unitless while the
sources give **distances in inches** (3″ from the rim for a normal rimshot, 1″ for a ping
shot, Strube's 2-inch target circle, Nevins's "about an inch above the center", Missouri
State's "2 inches from the rim, or 1.5 inches from the bearing edge"). D01 §5.2; D08 §2.6.
**No angular coordinate** for the brush literature's clock-face language (D01 §2.8).

**`instrument`**: the entire orchestral and auxiliary inventory (D02 §5.1); and **`marching.*`
is a missing reserved family** — not a member of `orch`, because its instruments, numbering
and technique names are all distinct (D08 §5.2).

**`openness`**: no marching or orchestral gap. But the axis is **hi-hat-anchored** while the
primary literature applies open/closed to **rolls, flams and drags** — three independent
attestations for the drag alone. Either openness generalises, or the decision to split
open/closed rolls across `ornament: roll` and `ornament: buzz` must be **written down as a
decision**. D01 §5.3-2.

## 4.4 Things v0.1 gets right, confirmed independently

Worth recording so a later pass does not "fix" them:

- **Splitting `site` from `contact` is exactly Read's own split** between *Methods of
  Striking* and the stick-type tables: p. 184 puts *With the handle of the stick* and *With
  the thin end of the stick* in striking-methods and *Felt stick / Sponge stick* in stick
  types. D02 §5.3.
- **Separating `damping` from `mechanism` is confirmed three times over**: Widor p. 108,
  Berlioz–Strauss p. 423 and Gevaert p. 332 all state that cloth-muffling and
  snare-slackening are *different means to the same end*, and Widor adds that the choice is
  left to the player. They must therefore be separate axes with independent values. D02 §5.3.
- **`position` as radial is cross-instrument, not a snare special case** — Read gives the
  centre/rim pair for timpani, bass drum, snare drum and tambourine alike. D02 §5.3. And a
  **vendor confirms three of the four anchors verbatim**: VDL's mod-wheel legend reads
  `center of head / halfway to edge / edge of head`. D08 §5.2.
- **`choke` as a relation rather than a technique value** is supported by the marching
  evidence, because *every* cymbal sound in the packets has a choked twin. D08 §3.1.
- **`implement: jazz-stick` has a 1922 primary source** and is not a modern marketing
  coinage: Straight 1922, "Sand-blocks, Clog-mallets, **Jazz-sticks** or Leather straps". The
  provenance record should carry that locator. D01 §5.4; D02 §2.16, §3.8.
- **`damping: muted` / `damped` is a 19th- and early-20th-century concept**, not a
  sampling-era one: Straight's standing "use muffled drums when you Jazz", and the Basel
  drum's permanent `Dämpfer`. D01 §5.4.
- **Rudiment names must not enter the pivot vocabulary** — the only rudiment-derived terms
  that belong on an axis are the per-note ornaments. D01 §5.3-4.
- Values independently validated by pre-1930 or non-English sources: `rimshot`, `ping-shot`,
  `stick-shot`, `sidestick`, `crossstick`, `butt`, `shank`, `tip`, `flam`, `drag`, `ruff`,
  `roll`, `buzz`, `bounced`, `ghost`, `accent`, `chick`, `wires-on`, `wires-off`,
  `open`/`half`/`closed`, `brush`, `sweep`, `left-hand`/`right-hand`/`alternating`/
  `left-foot`/`right-foot`, `centre`. D01 §5.4.
- **`position`'s four values are confirmed correct** by two marching sources, and `offset` —
  not `centre` — is the marching **default**. D08 §5.2.

---

# 5. STRONGEST CLAIMS

Ranked. These should survive even if everything else is cut.

**1. The axis decomposition was arrived at independently in 1953, without reference to MIDI.**
Gardner Read's *Thesaurus of Orchestral Devices* organises its percussion part (contents
pp. XVI–XVII, body pp. 158–233) under six recurring section headings applied to every
instrument family in turn: **Dampened · Methods of Striking · Muffled · Stick Types · Without
snares · Other Effects**. Those are, in order, KITWARP's `damping` (transient), `site` +
`position` + `technique`, `damping` (sustained), `implement`, `mechanism`, and the residue.
*Why it survives:* it is external validation that **the axes are in the subject matter rather
than in the tooling**, and it is worth more than any individual term. D02 §0.1(a), §2.1.

**2. Read splits `Dampened` from `Muffled` and v0.1 does not.** *Dampened* = stop the sound
**after** it starts (`Secco`, `Étouffez`, `Kurz`); *Muffled* = alter it **before** it starts
(`Con sordino`, `Voilée`, `Bedeckt`). Solomon 2016 collapses all three English words into one
heading, and **that 2016 conflation is the one most vendor lists inherit**. *Why it survives:*
it is a concrete, actionable split on a live axis, from the same source as claim 1, and it
tells you which of two conventions to follow. D02 §2.1, §4 item 7, §5.3.

**3. `timbre` is a false friend that collides with an existing axis name.** In French and
Italian scores `timbre`/`timbro` means the **snare wires**: `sans timbre` = snares off,
`avec timbre(s)` = snares on, `détimbrée` = de-snared, and `caisse claire` is named for it.
KITWARP's `timbre` axis means acoustic-vs-808-vs-FM. **Any importer that sees `timbre` in a
French or Italian source string and resolves it on the `timbre` axis silently destroys a
`mechanism` value.** *Why it survives:* it is a silent-corruption bug in the shipping design,
not a taxonomy quibble, and it belongs in `rules.json`. D02 §0.1(b), §2.6, §2.12, §4 item 1.

**4. The ornament axis needs an attack count, and three independent traditions supply the
count vocabulary — one of them as a working encoding in 1900.** Greissinger's legend reads
"**t** indicates tap; **f**, flam; **d**, drag; **r**, roll. The **figures under the rolls
indicate the number of strokes in each roll**" — an event-type letter plus a numeric attack
count, arrived at 126 years before this ADR. Gevaert 1885 counts `ra de 3/4/5/6/7 coups`;
Gardner 1918 counts `Five-/Six-/Seven-/Nine-/Ten-/Eleven-Stroke Roll` and `Four-Stroke Ruff`;
the Codex gives `N er Ruf` / `ra de N` across German/Swiss and French. The odd/even accent rule
makes the count load-bearing rather than decorative. The brief already says ornament carries a
count; **`axes.json` has no field for it**. *Why it survives:* it is the one change all three
dossiers demand, and it has a working 1900 encoding as precedent. D01 §2.3c, §5.3-0, §5.3-1;
D02 §2.13, §2.15, §3.6, §5.3.

**5. `back-stick` is not unattested — it is the best-sourced term in D08, and it reaches back
~150 years.** Named inventor (John Dowlan, Osmond Post Cadets 1935, technique dated 1938),
institutional debut (selected 1957 by M/Sgt Truman Crawford; taught to the USAF Drum Corps
snare section 1958), and an artefact that **overturns the 1938 date**: an Armstrong & Co.
lithograph, "A.R. Carrington, champion drum soloist, 1870s", NYPL call no. `PC MUSIC-Dru`,
Digital ID 832408, showing the flip mid-motion — corroborated by a *Utica New York Observer*
review of 3 July 1878 describing the flip and stick tosses **in one sentence**. D01 §2.7
reports it "NOT FOUND"; that negative is **scope-limited, not a refutation**. *Why it
survives:* it settles a v0.1 term that one dossier proposed to mark UNVERIFIED, and it
demonstrates that a bucket's negative is not evidence of absence. **D08 §2.5.1, §2.8**;
D01 §2.7, §5.1, §6.3.

**6. `gok-shot` is one vendor's spelling of a word whose only definition is uncited — and
ping/normal/gock are one technique at three positions, not three techniques.** `Gok` occurs in
exactly one place outside KITWARP (MuseScore commit `c7dc55ea2d`, from Muse Drumline);
Tapspace's 112-page manual never uses the word in any spelling; the field spelling is **gock**
(variant **gawk**); the only definition of the concept is an **uncited** Wikipedia paragraph;
and where "gock" appears in sourced reference works it usually means the **tenor drum**.
Meanwhile three separate authorities describe ping/normal/gock as **one technique (rimshot) at
three striking positions**. *Why it survives:* it is the clearest case in these dossiers of a
minted term with no source, it has a remedy that respects ADR-0003 (a `correction` alias, never
a rename), and the positional finding changes the model rather than just the spelling.
D08 §0, §2.5.2, §5.1.1–2.

**7. Two Rudimental-Codex items and two independent traditions say the elementary unit is a
*dynamic relation between adjacent attacks*, and v0.1 cannot express it.** The Codex's items
**2 and 3** are nothing but the pairs "loud-soft" and "soft-loud", ranked **above the flam**,
and its whole sticking legend is `RIGHT HAND | loud - soft`, `LEFT HAND | loud - soft` — four
glyph classes, hand × volume. Hart 1860 defines the flam itself as exactly this relation ("a
very soft, fine blow … and a full heavy blow immediately following"). Gevaert's `coup de
charge` (*tra*) differs from `fla` **only in which stroke carries the accent**. *Why it
survives:* it is a missing *relation*, not a missing value, and three traditions converge on
it. D01 §2.3b, §2.13b, §5.2; D02 §2.13, §3.9 G14.

**8. `rim shot` enters printed English between 1922 and 1937, in the dance-band literature,
and had not crossed into the orchestral languages sixteen years later.** Absent from Bower
1912, Gardner 1918 and Straight 1922 — two of which discuss playing on the rim at length
without ever using the word. **Present and already idiomatic in Bauduc, *Dixieland Drumming*,
1937** (archive.org `RayBauducDixielandDrumming`), used twice with no definition, and used as
a **dynamic-accent device rather than a timbre**. At Read p. 200 the entry "Rim shot — Shot"
has its Italian, French and German columns **empty** — as do the only two other
American-vernacular entries in 76 pages, `"Ride" solo` (p. 212) and `"Stomp the beat"`
(p. 194). *Why it survives:* it explains why `rimshot` has **no cross-language aliases to ship
while `muffled` has eight**, which is a directly actionable fact about the alias table. The
Krupa 1938 "shaft between head and rim" definition stays **UNVERIFIED** — Krupa is not on
archive.org. D02 §2.17, §4, §6.1, §6.3.

**9. Three independent traditions make *snares slackened* the usual muffling practice, and
v0.1 has no value for it.** Read p. 209 (`Avec les cordes lâches`, "snares loosened"),
Berlioz–Strauss p. 423 ("statt das Fell mit einem Tuchstück zu bedecken, begnügen sich die
Trommelschläger meist damit, die Schnarrsaiten zu lockern"), Gevaert p. 332 ("au lieu de
couvrir la membrane … on se contente souvent de détendre les cordes … **L'effet des trois
procédés est le même**"), with Widor p. 108 adding that the choice is left to the player.
v0.1 offers only `wires-on`/`wires-off`; Read also names a **third** state above `wires-on`,
`Très timbrée`. *Why it survives:* three independent traditions, the practice is the *usual*
one, and the same passages are what independently confirm that `damping` and `mechanism` must
be separate axes. D02 §2.6, §2.10, §2.12, §2.13, §3.8, §5.1, §5.3.

**10. The single most-taught vocabulary in the rudiment layer maps to no axis, and that is the
correct answer — but it must be written down.** Full / down / up / tap strokes are what PAS
itself teaches; they name the **preparation and termination height of the motion**, not the
sound, and two identical-sounding notes differ only in what the stick does afterwards. The
same holds for Moeller, Gladstone, push-pull, freehand, heel-toe, every grip, and MuseScore's
own `Visual (BS,X-Over,Etc)` class of notation that triggers a *movement* which may or may not
sound. *Why it survives:* "any future contributor will try to add `full-stroke` to the
`technique` axis, so it is worth writing down that this was checked and rejected on purpose."
D01 §3.3; D08 §3.2 item 8.

**11. Cymbal pair-vs-suspended is an instrument-level distinction v0.1 cannot express at all.**
Read gives them separate four-language nomenclature entries (`Piatti (a due)` vs `Piatto
sospeso` / `Cymbale suspendue` / `Becken frei`) and a separate chapter; the entire marching
cymbal line is a clash pair whose *implement is another cymbal*. v0.1's `crash` is a suspended
cymbal and **there is no slot for `piatti` at all**. *Why it survives:* it is the single
largest instrument-axis hole these dossiers find inside the already-minted kit family, not in
the reserved families. D02 §3.1, §5.2 item 3; D08 §2.7, §5.2.

---

# 6. DISAGREEMENTS

## 6.1 Between my own dossiers: `back-stick` — a direct contradiction

- **D01 §2.7** records: "**Back stick / backsticking** — **NOT FOUND** in any source reached.
  No definition, no attestation." **D01 §5.1** therefore recommends: "mark UNVERIFIED in the
  vocabulary until a locator exists," and **D01 §6.3** repeats it as a known weakness, guessing
  it "may be marching visual vocabulary … but that is a guess and is recorded as one".
- **D08 §2.5.1** overturns this and says so explicitly ("Raised because the rudiments bucket
  reports `back-stick` as unattested in any source it reached. **It is attested, and better
  than any other term here**"), with: Marrella, "The Baron of Backsticking", *Drum Corps
  World* Vol. 36 No. 15, Dec 2007 (developed 1938 as a left-hand training method; first taught
  to the USAF snare section in 1958 by John Dowlan); the World Drum Corps Hall of Fame's
  official Dowlan biography (Osmond Post Cadets 1935; selected 1957 by M/Sgt Truman Crawford);
  and Mirsky's overturning of the 1938 date with the Armstrong & Co. lithograph "A.R.
  Carrington, champion drum soloist, 1870s", NYPL `PC MUSIC-Dru`, Digital ID 832408, Record ID
  1062097, corroborated by the *Utica New York Observer* of 3 July 1878. **D08 §6** also
  records that an earlier draft of D08 itself claimed the bucket contributed nothing pre-1970
  and marks that "**That was wrong and is corrected in §2.5.1**".
- **Resolution:** D08 wins on evidence. D01's negative is **scope-limited** — it searched
  rudiment standards and stroke pedagogy, where the term does not live — and is **not a
  refutation**. D01 itself predicted the gap: §6.2 names the *Corps Style Snare Drum
  Dictionary* (Alfred 1981) and the snarescience dictionary as "the marching slang layer where
  `gock`, `sprock` and **very likely `back stick`** are actually defined". Both dossiers must
  be named in the final report; the vocabulary must **not** be marked UNVERIFIED on D01's
  recommendation.

## 6.2 Between my dossiers: what "no source uses gock" means

- **D01 §2.7** presents `gock`/`gawk` as ordinary marching vocabulary alongside ping shot and
  stick shot, and §5.1 treats the problem as purely orthographic ("the literature spells it
  **gock**").
- **D08 §0** goes much further: the *concept*'s only definition anywhere is an **uncited**
  Wikipedia paragraph; Tapspace's 112-page manual never uses the word; five technique packets,
  two manuals, two glossaries and the notated exercise packets do not use it; archive.org
  full-text search for `"gock" AND "rimshot"` returns **0 hits**; and D08 §6 names this "the
  bucket's central negative finding". D08 also records that the sharpest definition in the
  dossier "rests on an uncited tertiary paragraph, corroborated only by the fact that four
  independent paraphrases of it circulate" — i.e. **the four paraphrases are one source**.
- **Resolution:** D01 is not wrong about the spelling; it is under-stating the evidential
  position. D08's stronger reading should be carried, and the final report should record that
  `gock` has **no independent attestation at all**, only redistribution of one uncited
  paragraph.

## 6.3 Between my dossiers: is `stick-shot` orchestral or marching?

Not a contradiction, but the two dossiers assign it to different registers and both are right.
D01 §2.7 files "stick shot (orchestral 'rimshot')" as **orchestral**; D02 §2.6 finds Read's
*Lay 1 stick on head of drum — strike with the other* (p. 198) in the **orchestral** treatise;
D08 §0 finds it as a shipped **marching** articulation and notes "the register split: the stick
shot is a *jazz and orchestral* term that marching percussion also uses", with Blakley's
glossary recording the collision (his second sense of "cross stick" *is* the stick shot).
**Carry the register split, not one register.**

## 6.4 Inside a single tradition: two 1860s manuals contradict each other twice

- **Whether a drum stroke has a duration.** Hart 1860: "all Blows, Taps, Flams, or Single
  Beats have but **one length of sound** on the Drum" — the premise of his entire
  four-character notation. Nevins 1864, four years later: `Poing Stroke` = "sudden, **hard,
  short**" against No. 10 = "**soft, long, drawing**". D01 §3.3, §4.1, §5.3-5.
- **Whether the drawing stroke is legitimate technique.** Hart forbids it outright — "make
  **no drawing strokes or sideway beats** in no case whatever, although it has been recommended
  by many professional teachers of drumming" — which is itself a record that the disagreement
  was already live in 1860. Nevins lists it as gamut item 10. D01 §2.3b, §4.1.
- **Neither is resolved by these dossiers.** D01's judgement is that for a *sampled* pivot Hart
  is right and no envelope axis is needed, because the sample carries the envelope — but D01 is
  explicit that this was answered by the source material, not assumed.

## 6.5 Between the standards bodies (all live, none resolvable)

- **PAS 40 (1984) vs NARD 26 (1933/1958) vs Scottish 46 vs Rudimental Codex 42 vs Spalding's
  5+22 vs the French conservatoire 34 vs a 500+ open hybrid corpus.** The IATD objects to the
  PAS 40 on the grounds of "Swiss influence", and the objection is **largely wrong on the
  facts** (of the fourteen 1984 additions, only two are traceably Swiss). The Codex exists
  explicitly "to **challenge the Percussive Arts Society interpretation** of many rudiments of
  European origin" and has been submitted to UNESCO. **D01 §4.4's verdict: no single rudiment
  list can be treated as the authority.**
- **PAS renames its own items.** Four renamings between NARD's 1958 recording and the 1984
  sheet, including `Ruff` → `Drag`. D01 §2.2b.
- **The 1984 "additions" were not all new.** `Triple Paradiddle` is item 18 and `Flams
  Paradidle Didle` item 19 of Nevins's 1864 US Army gamut, yet both are counted among the
  fourteen rudiments PAS *added* in 1984 and characterised as drum-corps, European or
  contemporary. **Any provenance note that dates a rudiment by its list membership will be
  wrong; date it by the earliest manual instead.** D01 §5.3-6.

## 6.6 Inside the marching cymbal literature (five programmes, no authority)

`slam` has **three incompatible meanings** across Oregon State, GVSU and Rhythm Armada;
`ding`/`ting` names two different sounds **inside one document** (GVSU); `crunch` is a hi-hat
slam to one source and a synonym of `press` to another. **D08 §6 states the finding plainly:
"the disagreement between them … is real and is not resolvable from these sources — there is
no authority to appeal to."** D08 §4, §2.7, §2.7.1.

D08 also **reverses a negative reported to another bucket**: the notation-standards bucket was
told that no general marching-cymbal source names `zing`, `smash` or `crunch choke`. D08
§2.7.1: "**That negative is wrong for three of the four terms**" — `zing` has **six**
independent non-Tapspace sources and is the most uniformly defined marching cymbal term found;
`suck` has four plus a mechanism corroboration; `crunch` has two. What genuinely rests on one
source is narrower: `smash` under that name (PCHS only), `crunch choke` as a compound (Tapspace
only), `Half Crash` (**no source at all**), `whale-call` (Tapspace only), `weedwacker` (GVSU
only), `guz` (Tapspace/MakeMusic only, with **no published definition anywhere**).

## 6.7 MuseScore contradicting itself

Two shipped MuseScore files disagree on pitch 53 (`Cross Stick` vs `Rim Click`), pitch 79
(`Punch` vs `Crash-Choke` — **a genuine mislabel**, since a punch is a choked *tap*, not a
choked *crash*), pitch 84 (`Ting` vs `Bell Tap`), pitch 89 (`Suc` vs `Smash` — **two real but
different sounds on one pitch**), and **Spock ordering** (`.drm` Spock 1 above; `instruments.xml`
Spock 2 above). Tapspace's two independent maps both put Spock 1 higher, so **one of MuseScore's
two shipped files is wrong**. D08 §2.8, §4 item 10.

## 6.8 A lineage caution that changes attestation counting anywhere in the final report

**Peinkofer & Tannigel's English *Handbook of Percussion Instruments* (1976) is translated by
Kurt and Else Stone — the same Kurt Stone who wrote *Music Notation in the Twentieth Century*
(1980).** D02 §1.2 N5 and §6.2 both state it: "N4 and N5 are therefore **one lineage, not two
independent witnesses**, and the reconciliation pass should not count agreement between them as
corroboration." **Any attestation count in the final report that treats Stone 1980 and
Peinkofer/Tannigel 1976 as two independent traditions is wrong.** Note also that neither book
was actually opened — both are lending-restricted on archive.org, and Peinkofer/Tannigel's
contents are known only from publisher/catalogue copy supplied by the supervisor (**UNVERIFIED
against the book**).

## 6.9 Where these dossiers agree, notably

- **`ornament` needs an attack count**: D01 §5.3-1 and D02 §5.3 reach it from disjoint sources
  (American rudimental manuals vs Gevaert/Gardner), and D01 adds Greissinger 1900 as a working
  encoding. Independent convergence.
- **`fist` and `fingernail` are in the round-2 brief's model but absent from `axes.json`**:
  reported independently by D01 §5.2, D02 §5.1 and D08 §5.2 — with **Read p. 214 (`Col pugno` /
  `Mit der Faust`)** and the **Casey Claw** ("held in a fist, where all the fingers wrap around
  the stick") as two independent sources for `fist`, and Read p. 164 (`Colle unghie` / `Mit dem
  Nagel`) for `fingernail`. This is a real omission, not a drafting slip in the brief.
- **This marching vocabulary is monolingual American English.** D08 searched German
  *Spielmannszug*/*Marschtrommel* and French *batterie-fanfare* literature deliberately and
  found **nothing** — no equivalents for gock, ping, spock, backstick, zing or succ. D08 §6
  states this as a **positive finding**: "this vocabulary is … not translated in scores
  worldwide. Bucket 12 (German/French/Italian) should not expect overlap here." It is the exact
  counterpart of D02's finding that Read's four-language columns are **empty** for `Rim shot`,
  `"Ride" solo` and `"Stomp the beat"` and full for everything else.

---

# 7. Late-findings checklist

| # | Item | Present in my dossiers? | Where carried in this extract |
|---|---|---|---|
| 1 | `back-stick` — D01 says unattested, D08 makes it the best-sourced term; ~150 years; D01's negative was scope-limited | **Yes, both sides** | §1.1 row; §4.1; §5 claim 5; **§6.1** |
| 2 | `rim shot` bracketed 1922–1937 via Bauduc; dynamic-accent device not a timbre; explains why Read found no IT/FR/DE equivalent while `muffled` has eight; Krupa 1938 stays UNVERIFIED | **Yes (D02)** | §3.2; §5 claim 8; §1.9 |
| 3 | Peinkofer/Tannigel EN is translated by Kurt and Else Stone ⇒ Stone 1980 and P&T 1976 are **one lineage**, not two traditions | **Yes (D02 §1.2 N5, §6.2)** | "How attestations are counted", **§6.8** |
| 4 | Read splits `Dampened` from `Muffled`; v0.1 does not. Contents pp. XVI–XVII, body pp. 158–233 | **Yes (D02)** | §1.9; §3.1; §4.3; **§5 claim 2** |
| 5 | `fist` has a marching source (Casey Claw); `fist` and `fingernail` are both in the round-2 brief and both absent from `axes.json` | **Yes (D08 §2.5.1, §5.2; also D01 §5.2, D02 §5.1)** | §1.2; §1.8; §4.3; **§6.9** |
