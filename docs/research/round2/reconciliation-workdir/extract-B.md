# Reconciliation extract B — the formal-vocabulary layer

Dossiers read in full:

- **D03** = `docs/research/round2/03-organology-thesauri.md` (organology, authority files)
- **D04** = `docs/research/round2/04-notation-standards.md` (notation standards, program vocabularies)
- **D12** = `docs/research/round2/12-german-french-italian.md` (non-English score terminology)

Vocabulary read: `vocabulary/axes.json` (0.1.0, serial 1), `vocabulary/pivot.json` (155 terms),
`vocabulary/rules.json`. ADRs read: `docs/adr/0001-pivot-vocabulary.md`,
`docs/adr/0003-identifiers-and-registry.md`.

## 0. How attestations are counted here

A "tradition" is a body of practice that could have named the thing without the others.
Where two of my sources descend from one text, they are **one** attestation and the row says so.
The lineages that matter, established from the dossiers themselves:

| Tag | Tradition | What it is, and what it is NOT independent of |
|---|---|---|
| `ORG` | Organological classification | H-S 1914 → Baines–Wachsmann 1961 → MIMO 2011 revision → MIMO SKOS / ACDH-CH digital H-S / Knight K-Rev. **All one lineage.** D03 §1.1 rows 1–5; D03 §2.1. Knight counts separately only where he adds a distinction of his own (the suffix glossary, D03 §2.3). |
| `LIB` | Library / museum authority control | LCMPT (D03 §2.6), Getty AAT (§2.5), GND (§2.11). Independent of ORG in editorial practice, though AAT and LCMPT both classify by H-S-like acoustics. |
| `AGG` | Crowd aggregation | Wikidata (§2.7), MusicBrainz (§2.8). **Not independent** wherever they carry a P1762/P3763/P1014/P1330 id — that is ORG or LIB copied. Independent only where they hold a concept no authority has (Wikidata `ride cymbal` Q93992, `hi-hat` Q963334 — D03 §0.1, §2.7). |
| `ENG` | Notation-engraving pictogram lineage | SMuFL 1.4, MusicXML 4.0/4.1, MEI, MNX. **Largely one lineage descending from Kurt Stone 1980**: MusicXML's own XSD says its effect list is "in addition to Stone's list" (D04 §2.2), SMuFL's percussion pictograms are largely Stone's, MEI has no percussion vocabulary at all and delegates to SMuFL glyph names (D04 §2.4), MNX has dropped the enumerations entirely (§2.5). Upstream of Stone: Ghent 1974, Read 1969, Smith Brindle 1970, preserved only as SMuFL attributions (D04 §1 rows 20–24). |
| `PAS` | American drumset-notation standardisation | Weinberg 1994 / Percussive Arts Society, from a survey of 220 publications (D04 §2.10). Partially overlaps ENG — Weinberg conforms "to the standards set forth by both Stone and Gardner Read". |
| `SW` | Notation-software vendor data | LilyPond, MuseScore, Sibelius SoundWorld, Finale, Guitar Pro, Dorico (D04 §2.6–§2.12). Each vendor is a separate witness, but MuseScore carries a `musicXMLid` on every instrument, so MuseScore↔MusicXML agreement on an *instrument name* is not corroboration. |
| `DE` | German orchestral / pedagogical | VSL German instrumentology (D12 S01), ISB Bayern official exam standard (S07), Haupt & Teuchert 1911 (S42), Peinkofer/Tannigel via Wikipedia DE (S11, S12, S21). |
| `FR` | French score practice | Berlioz 1843 (S33), Encyclopædia Universalis (S08), Percunivers (S13), Arpège/Pizzicato GM map (S19). |
| `IT` | Italian treatise / conservatory | Facchin (S03), Conservatorio di Udine syllabus (S17). |
| `ES` | Spanish pedagogy | Strong, *Percusión para Dummies* ES (S18) — TOC only, glosses UNVERIFIED. |
| `MARCH` | Marching / corps | reaches my dossiers only as vendor data: MuseScore marching instrument sets (D04 §2.8) and Tapspace Virtual Drumline via Finale (D04 §2.11). Bucket 08 owns the literature. |

**Lineage caution carried in from the late-findings file (item 3), and it bites here.**
Peinkofer & Tannigel's authorised English translation is by **Kurt and Else Stone**. If that
holds, then `ENG` (SMuFL + MusicXML, both downstream of Stone 1980) and D12's German handbook
lineage `S21` are *partly the same hand*, and D12 §6.2's proposal to use the German/English
editions as "a ready-made bilingual concordance" is a concordance made by the man who also
wrote the pictogram list the notation standards inherited. **None of my three dossiers records
this.** D04 §1 row 19 and D12 S27 both register Stone 1980 without naming him as a translator;
D12 S21 names the translation (*Handbook of Percussion Instruments*) but not its translators.
D12 also dates Peinkofer/Tannigel **Schott 1981**, where the late-findings file says **1976** —
neither is verified here. Any count that treats Stone 1980 and Peinkofer/Tannigel as two
independent traditions is wrong, and so is any count that treats SMuFL and MusicXML as two.

---

## 1. TERMS

Exhaustive across the three dossiers. Where a source ships a large closed enumeration
(128 SMuFL beater glyphs, 391 MusicXML sound ids, 2 724 MIMO concepts) the row names the
family, its size and its locator rather than transcribing it; the dossier section named is
complete and verbatim.

### 1.1 instrument axis — kit terms

| Term as the source spells it | Physical meaning | v0.1 axis | Independent traditions | Locator |
|---|---|---|---|---|
| Cymbals / Becken / Cymbales / Cimbali / Címbalos / Piatti | a struck metal plate, or a pair | instrument `cymbal` | 4 (ORG H-S 111.142; LIB LCMPT mp2013015195, AAT 300041897, GND 7542598-1; ENG MusicXML `crash cymbals`, SMuFL U+E720; DE/FR/IT) | D03 §2.1.1, §2.4, §2.5, §2.6, §2.11; D04 §2.1, §2.2; D12 §2.1, §2.2 |
| Side drum / Snare drum / kleine Trommel / caisse claire / cassa chiara / tamburo piccolo / caja / rullante / caixa | shallow double-skin cylindrical drum with wires | instrument `snare` | 5 (ORG 211.212.11; LIB LCMPT mp2013015657 UF *side drum*, *caixa*, GND 7542431-9; ENG MusicXML `snare drum`, SMuFL U+E6D1; SW; DE/FR/IT/ES) | D03 §2.1.2, §2.6, §4.9; D04 §2.1, §2.2; D12 §2.1, §2.2, §2.19 |
| Bass drum / Große Trommel / grosse caisse / grancassa / bombo / Kick | large drum, foot-operated on a kit | instrument `kick` | 5 (ORG 211.212.12 "bass drum in marching band"; LIB LCMPT mp2013015065, AAT 300041732; ENG MusicXML `bass drum`, `bass drum on side`; SW GP `pedal.hit.hit`; DE/FR/IT/ES) | D03 §2.1.2, §3.1; D04 §2.2, §2.7; D12 §2.1, §2.6 |
| Tom-tom / Tomtom / tom basse–médium–aigu | single- or double-headed drum without wires | instrument `tom` | 4 (LIB LCMPT mp2013015737 — but its *only* UF is *Chinese tom-tom*; ENG MusicXML `tomtom`, `Chinese tomtom`, `Japanese tomtom`, `Indo-American tomtom`, SMuFL U+E6D7–DA; SW; FR/IT) | D03 §2.6, §4.7; D04 §2.1, §2.2; D12 §2.15, §2.19 |
| Drum set / Schlagzeug / Batterie / Batteria / Drumstel / Trumset / traps / trap kit | the whole kit as one object | none — a layout, not a term | 4 (ORG 211.212.21 "USA/Europe drum kit"; LIB LCMPT mp2013015222 UF *traps*, *trap set*, *drum kit*, *trap kit*, *drumset*, AAT 300411407, GND 4137284-0; AGG Q128309, MB 12092505; ENG MusicXML `drum.group.set`) | D03 §2.1.2, §2.4, §2.6, §2.11; D04 §2.3; D12 §2.1 |
| Hi-hat / Hi-Hat-Maschine / Choke cymbal / Sock cymbal / Charleston / Charley / piatti a pedale / cymbales à pédale / foot cymbals | two cymbals on a pedal stand | instrument `hihat` | 5 (LIB GND 7525743-9 with the only authority-file *definition* found; AGG MB 6d328aab, Q963334 — no MIMO/AAT id; ENG SMuFL U+E722/E723, MusicXML `hi-hat` + `high-hat cymbals`; SW all six programs; FR/IT) — **absent from LCMPT, AAT and MusicBrainz-as-authority; MIMO has it only as the German label of two other concepts** | D03 §0.1, §2.4, §2.11, §4.1; D04 §2.1, §2.2, §2.7; D12 §2.2, §2.15, §2.19 |
| Ride cymbal / Cymbale ride / piatto ride | large sustaining cymbal played on the bow | instrument `ride` | 2 (AGG Wikidata Q93992 only, carrying **no** MIMO, AAT or MB id; SW LilyPond `ridecymbal`, MuseScore, Sibelius `…cymbal.ride`, GP, Finale, MusicXML **Standard Sounds** `metal.cymbal.ride`) — **zero in ORG, LIB, and zero in the ENG pictogram layer**: SMuFL's cymbals range has no ride glyph and MusicXML's `metal-value` has no `ride` | D03 §0.1, §2.7, §5.2; D04 §2.1 (cymbals range), §2.2, §2.3, §2.6–§2.11; D12 §2.19 |
| Chinese cymbal / China / cymbale chinoise / piatti cinesi | upturned-edge cymbal | instrument `china` | 3 (ENG SMuFL U+E726 `pictChineseCymbal`, MusicXML `Chinese cymbal`; SW LilyPond `chinesecymbal`, MuseScore, GP, Finale; IT/FR) — **zero in ORG and LIB**; no Wikidata item matched `china cymbal`@en | D03 §0.1, §2.7; D04 §2.1, §2.2; D12 §2.2, §2.19 |
| Splash cymbal / cymbale splash / piatto splash | small fast-decay cymbal | instrument `splash` | 2 (AGG Q1074981; SW LilyPond `splashcymbal`, MuseScore, GP, Finale, MusicXML Standard Sounds `metal.cymbal.splash`) — absent from SMuFL, from MusicXML's pictogram vocabulary, and from every authority file. MIMO's **Basque** label for `Choke cymbal` (2467) is *Splash txindata* | D03 §0.1, §2.7, §4.1; D04 §2.3; D12 §2.19 |
| Sizzle cymbal / Piatto chiodato / Címbalo ribeteado / Talerz z nitami / cymbales grésillantes, cloutées | cymbal with rivets fitted | v0.1 puts it on **instrument** `sizzle-ride`; every source describes a *build state* | 4 (ORG/LIB MIMO 2488; ENG SMuFL U+E724, MusicXML `sizzle cymbal`; SW Sibelius `sizzle` 10 ids, MuseScore marching-cymbals *Sizzle*, Finale *Sizzle Cymbal*; IT/FR/DE *Nieten*) | D03 §2.4, §5.3(a); D04 §2.1, §2.2, §2.8, §2.11; D12 §2.2, §2.7 |
| Suspended cymbal / piatti sospesi / cymbales suspendues / Becken auf Ständer / freihängende Becken | a single cymbal on a stand | **NONE** — v0.1 has `cymbal` and `crash`, neither of which is this | 4 (ENG SMuFL U+E721, MusicXML `suspended cymbal`; SW MuseScore `crash-cymbal` trackName "Suspended Cymbal", Finale *Suspended Cymbal Roll/Choke*; DE VSL `/suspended-cymbal`; IT Facchin *PIATTI SOSPESI TURCHI* pp. 108–115) | D04 §2.1, §2.2, §2.8, §2.11, §5.1; D12 §2.2, §2.7 |
| Crash cymbals / Cymbales à main, à 2, choquées, cossé / HandBecken / 2 Beckenteller / piatti a mano in coppia / Piatti | **a clashed pair of plates** | **NONE** — collides with v0.1 `crash` (a suspended cymbal on a stand) | 4 (ORG H-S 111.142 "vessel clappers … struck against each other"; ENG MusicXML `crash cymbals`, SMuFL U+E720; SW MuseScore instrument `cymbal` trackName "Hand Cymbals", GP *Piatti*; DE/FR/IT via Facchin's index) | D03 §2.1.1, §4.3; D04 §4 (last entry), §5.1; D12 §2.2, §4.1 |
| Bell / Glocke / Cloche / Campana / Almglocken / cencerro | a struck bell as an instrument | v0.1 `bell` is on **instrument** *and* on **site** | 4 (ORG 111.242; LIB LCMPT mp2013015079 with 11 children, AAT 300041872, MIMO `Bells` 2371 with 69 members; ENG SMuFL U+E714, MusicXML `bell`, 25 `metal.bells.*` sound ids; DE/FR/IT) | D03 §2.1.1, §2.4, §2.6, §5.3(b); D04 §2.1, §2.3, §4; D12 §2.1 |
| Cowbell / Kuhglocke / Sonnaille / Campanaccio / Cencerro | clapperless struck bell | instrument `cowbell` | 4 (LIB LCMPT mp2013015187 UF *Almglocke*, AAT 300041875, GND 133326514X; AGG Q775570, MB 2b75a5bc; ENG SMuFL U+E711, MusicXML `cowbell`; DE/FR/IT/ES) | D03 §2.6, §2.7, §2.11; D04 §2.1, §2.2; D12 §2.1, §2.19 |
| Tambourine / Tamburin / Tambourin, Tambour de basque / Tamburello / Pandereta | jingled frame drum | instrument `tambourine` | 5 (ORG 211.311; LIB LCMPT mp2013015705 UF *pandeiro*, *adufo*, AAT 300041759, GND 4504967-1; ENG SMuFL U+E6DB, MusicXML `tambourine`; SW; DE/FR/IT/ES) | D03 §2.1.2, §2.6, §2.7, §2.11; D04 §2.1; D12 §2.1, §2.8 |
| Triangle / Triangel / Triangolo / Triángulo | struck steel bar | instrument `triangle` | 4 (ORG 111.211; LIB LCMPT mp2013015746, AAT 300041911; ENG SMuFL U+E700, MusicXML `triangle`; DE/FR/IT/ES) | D03 §2.6, §2.7; D04 §2.1, §2.2; D12 §2.1, §2.19 |
| Wood block / bangzi / clog box / Chinese wood block / tap box / caja china | struck wooden box | instrument `woodblock` | 4 (LIB LCMPT mp2017015001 with that whole UF ring; ENG SMuFL U+E6F0, MusicXML `wood block`; SW; ES/IT/FR) | D03 §2.6, §4.9; D04 §2.1, §2.2; D12 §2.19 |
| Claves / Legnetti | paired struck sticks | v0.1 has `sticks`, **which is not the same object** (D03 §5.1) | 4 (LIB LCMPT mp2013015156, AAT 300041921; ENG SMuFL U+E6F2, MusicXML `claves`, `wood.claves`; SW; IT) | D03 §5.1; D04 §2.1, §2.2; D12 §2.1, §2.19 |
| Shaker / egg shaker / maraca / cabasa / shekeré | shaken rattle | instrument `shaker` | 4 (ORG 112.1 rattles; LIB LCMPT shaken-idiophone branch, MIMO `Rattles` 3012 with 87 children; ENG SMuFL U+E741–E743, MusicXML `maraca`, `cabasa`, 22 `rattle.*` sound ids; SW GP, Sibelius) | D03 §2.4, §2.6, §4.9; D04 §2.1, §2.2, §2.3, §2.7 |
| Hand clapping / Claquement de mains / Handclap | clapped hands | instrument `clap` | 3 (LIB LCMPT mp2013015316 under `body percussion`; ENG MusicXML `effect.hand-clap`; SW LilyPond `handclap`, GP, FR GM map) | D03 §2.6, §3.3(d); D04 §2.3, §2.7; D12 §2.15 |
| Chimes / tubular bells / orchestral chimes | hung metal tubes | instrument `chimes` | 3 (ORG 111.231 "Tubular bell"; LIB LCMPT mp2013015754; ENG SMuFL U+E6C0/E6C2, MusicXML `chimes`, `tubular chimes`) | D03 §2.1.1, §2.6, §4.9; D04 §2.1, §2.2 |
| Percussion controller / mallet controller / MIDI controller / drum machine | an electronic trigger device | instrument `aux-pad`; timbre `electronic` | 2 (LIB LCMPT mp2013015541, mp2013015442, mp2013015221 UF *rhythm machine*, **electronic percussion**, **electronic drum**, GND 4226169-7 *Elektronisches Schlagzeug* with score abbreviations *el-perc*, *E-Schz*, *el-dr*, *E-Drums*; SW MuseScore/LilyPond `electricsnare`, Sibelius `electric`) | D03 §2.6, §2.11, §3.1; D04 §2.3, §2.6, §2.9 |
| Roto-tom | tunable single-head shell | v0.1 nearest is `octoban` (D03 §3.1) | 2 (LIB LCMPT mp2019015002, AAT files it under **frame drums** 300041844; ENG MusicXML `drum.rototom`) | D03 §3.1, §4.7; D04 §2.3 |
| Stack, xhat, mini-china, mini-hihat, crash-ride, jam-block, aux-pad, octoban | kit-specific composites | v0.1 instrument values | **0 external traditions** — "Not one of the six [authority files] has a concept for `ride`, `china`, `splash`, `stack`, `xhat`, `mini-china`, `mini-hihat`, `crash-ride`, `jam-block` or `aux-pad`"; `jam-block` survives only as MusicXML sound id `wood.jam-block` | D03 §0.1, §5.2; D04 §2.3 |

### 1.2 site axis

| Term as the source spells it | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `drumheads` (AAT 300041846); Fell; peau, peau de frappe; pelle battente; parche | the struck membrane | site `head` | 4 (LIB AAT — but as a *museum object type*, a spare head in a drawer, not a place a stroke lands; ENG MusicXML `center` implies it; DE/FR/IT/ES) | D03 §2.10, §3.1, §3.2; D12 §2.15, §2.18, §2.19, §3.1 |
| `shells (drum components)` (AAT 300041856); auf dem Holz; Korpus; sur le bois; fût; casco; fusto; **Shell** | the drum body as a striking place | site `shell` | 5 (LIB AAT, again as object not place; ENG none; PAS Weinberg "playing on the shell of a drum … indicated with brief text"; SW MuseScore marching-tenor/marching-snare **Shell**, Sibelius `shell` 7 ids; DE/FR/ES/IT) | D03 §2.10, §3.1; D04 §2.8, §2.9, §2.10, §3.2; D12 §2.3, §2.11, §2.18, §2.19, §3.1 |
| `pictOnRim`, `pictRim1` "Rim **or edge**", `pictRim2`, `pictRim3`; `rim`; cercle, rebord; Spannreifen; controcerchio; aro; **Rim** | the hoop | site `rim` | 5 (ENG SMuFL U+E7F4, U+E801–E803, MusicXML `stick-location` `rim`; PAS Weinberg Ex. 16–17; SW MuseScore marching sets, Sibelius `rim` 10 ids, Finale *Snare Rims*; DE/FR/IT/ES) | D04 §2.1, §2.2, §2.8–§2.11, §3.2; D12 §2.15, §2.17, §2.18, §3.1 |
| **cerchi e controcerchi** (hoop and counterhoop); *colpi sul bordo di legno e di metallo* | two rims, distinguished as hoop/counterhoop **and** by material wood/metal | site `rim` + `rim2` — v0.1's pair are bare ordinals with no stated semantics; Italian gives them one | 1 (IT Facchin pp. 471, 473, 754) | D12 §2.3, §2.17, §5.2 |
| `pictEdgeOfCymbal` U+E729; `cymbal edge`; `edge`; Beckenrand; bordo; borde | the outer rim of a cymbal | site `edge` | 4 (ENG SMuFL, MusicXML `stick-location`; SW Sibelius `edge` 15 ids, GP `stick.hit.edge`; PAS Weinberg "at edge"; DE/IT/ES) | D04 §2.1, §2.2, §2.7, §2.9, §2.10, §3.2; D12 §2.7, §2.13, §2.18, §3.1 |
| `pictBellOfCymbal` U+E72A; `cymbal bell`; `bell`; Beckenkuppe; coupole; cupola; **Buckel** (gong boss) | the raised dome of a cymbal | site `bell` — **the same slug as instrument `bell`** | 4 (ENG SMuFL, MusicXML; SW Sibelius `bell` 17 ids, GP `stick.hit.bell`, MuseScore Ride Bell, Finale Ride Bell; PAS Weinberg "at bell"; DE/IT/FR) | D03 §5.3(b); D04 §2.1, §2.2, §2.7, §2.9–§2.11, §3.2, §4; D12 §2.7, §2.13, §3.1 |
| `bow` (v0.1 site) = the sloping playing area between bell and edge; GP "Ride (middle)" `stick.hit.mid` | the cymbal's main playing area | site `bow` | **1** (SW Guitar Pro, and only as "middle") — **no source in any of the three dossiers names a cymbal `bow` as a site.** In every organological source `bow` is a horsehair stick (MIMO `Bows` 2206) and in ENG `bow` is an implement (MusicXML `beater-value` `bow`, SMuFL `pictBeaterBow` U+E7DE) | D03 §4.7, §4.8; D04 §2.2, §3.2, §4 |
| `crossstick` (v0.1 site) | stick laid across the head onto the rim | v0.1 has it on **site** while the same act is `technique = sidestick` | 0 as a *site* — every source treats it as one act, not a place: GP `stick.hit.sidestick`, MuseScore one MIDI note and one notehead, LilyPond `sidestick`, FR *baguette sur bord de fût*, DE *Rimclick* | D04 §4, §5.3(1); D12 §2.3, §2.15, §3.1 |
| `underside` (v0.1 site) | the far side of a head | 0 attestations. What FR and DE name instead is a *head*: **peau de résonance**, **peau inférieure**, **Resonanzfell**; H-S and Knight make head-count and which-head-is-played a primary distinction (211.212.11 "one skin used for playing" vs .12 "both heads played") | D03 §2.1.2, §3.3(a); D04 §5.2; D12 §2.15, §3.2(h), §5.1 |
| **Zone di percussione** | "percussion zones" — the Italian superordinate over what v0.1 splits into `site` + `position` | NONE (a category over two axes) | 1 (IT Facchin pp. 111, 474) | D12 §3.2(h) |

### 1.3 position axis

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `pictCenter1` (Weinberg), `pictCenter2` (Ghent), `pictCenter3` (Caltabiano), `pictNormalPosition`; `center`; Fellmitte, Mitte; al centro | struck at the middle of the head | position `centre` | 4 (ENG SMuFL U+E7FE–E800, U+E804, MusicXML `stick-location` `center`; PAS Weinberg Ex. 17; DE; IT) | D04 §2.1, §2.2, §2.10, §3.2, §3.3; D12 §2.5, §2.7, §2.11, §3.1 |
| Fellrand; sul bordo; "Piano eher am Fellrand" | struck near the edge of the head | position `perimeter` | 2 (DE VSL + ISB Bayern; IT) | D12 §2.5, §2.6, §2.11, §3.1 |
| **Schlagfleck** | the *named* ideal striking spot — "one hand's width from the edge" (timpani), "3–4 cm from the rim" (tambourine) | **NONE** — not centre, not perimeter; the German default | 1 (DE VSL, twice, with two different measurements) | D12 §2.5, §2.8, §3.2(h), §5.1 |
| **Colpi sui nodi** | strokes on the *nodal points* of a bar or plate | **NONE** — v0.1 `position` is radial; a node is acoustic | 1 (IT Facchin p. 379) | D12 §2.17, §3.2(h), §5.1 |
| `halfway`, `offset` (v0.1) | intermediate radial positions | **0 attestations anywhere in the three dossiers** | D04 §3.3, §5.2 |

### 1.4 contact axis

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| Cowbell (tip) vs (hit) — GP `stick.hit.tip`; Sibelius `tip` | struck with the stick tip | contact `tip` | 1 (SW: two vendors, one tradition) | D04 §2.7, §2.9, §3.4 |
| **Asta / manico delle mazzuole** — "struck with the mallet *shaft*, at the bar centre / on the bar edge" | struck with the shaft, not the head | contact `shank` | 1 (IT Facchin p. 262) — **the only attestation of `shank` in any of my three dossiers.** D04 §3.4 states flatly that `shank` and `butt` "have no attestation in this bucket at all" | D04 §3.4, §5.2; D12 §2.17, §3.1 |
| `butt` (v0.1) | struck with the stick's far end | **0 attestations** | D04 §3.4, §5.2 |
| `tip`, `heel`, `palm`, `finger`, `fingers`, `hand` as Sibelius id elements on conga/bongo | which part of the *hand* lands | v0.1 splits these across `implement` (hand, finger) and `technique` (heel, toe, thumb) | 2 (SW Sibelius; ES *golpe talón-punta*, *golpe de palma*, *golpe de pulgar*) | D04 §2.9, §3.4; D12 §2.18 |

### 1.5 technique axis

| Term as the source spells it | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `pictOpenRimShot` "Closed / rim shot", `pictRimShotOnStem`; Snare (rim shot) `stick.hit.rimshot`; Rim Shot; **Randschlag**; *colpi a sparo … tra il controcerchio di metallo e la pelle*; *rimshot* "frapper la peau et le rebord en même temps" | head and rim struck together | technique `rimshot` | 5 (ENG SMuFL U+E7F5, U+E7FD; PAS Weinberg — who found **31 different notational procedures** for this one effect; SW GP, MuseScore, Finale; DE; FR; IT) | D04 §2.1, §2.7, §2.8, §2.10, §2.11, §3.5; D12 §2.3, §2.15, §3.1, §5.3 |
| `pictStickShot` "Stick shot"; **Stick Shot**; Stock auf Stock; Schlägel auf Schlägel; *colpi tra bacchette* | one stick struck against the other | technique `stick-shot` | 4 (ENG SMuFL U+E7F0; SW MuseScore marching-snare (57); DE VSL + ISB Bayern; IT Facchin p. 473) | D04 §2.1, §2.8, §3.5; D12 §2.3, §2.6, §2.11, §3.1, §5.3 |
| Snare (side stick) `stick.hit.sidestick`; **Side Stick** / **Cross-stick** / **Rim Click** / **Stick Click** / **Snare Cross Stick**; `sidestick`, `hisidestick`, `losidestick`; **Rimclick**; *cross stick, click* "un coup frappé sur le cercle, la paume de la main reposant sur la peau"; **Baguette sur bord de fût** | stick laid on the head, butt struck on the rim | technique `sidestick` (and, wrongly, site `crossstick`) | 4 (SW GP, MuseScore — 5 names in 2 files of one program, LilyPond, Finale; DE; FR twice, incl. the GM map; PAS via GM 37) | D04 §2.6–§2.11, §3.5, §4, §5.3(1); D12 §2.15, §3.1, §5.3 |
| **Backstick** | the stick flipped, struck with the butt end | technique `back-stick` | **2 in my dossiers** (SW MuseScore `marching-snare` (60, `ti` notehead) — the only closed set of snare techniques enumerated as data anywhere in D04; MARCH) **+ bucket 08's independent documentary lineage** — see §6 | D04 §2.8, §3.5 |
| `pictChokeCymbal` "Choke (Weinberg)"; (choke) `stick.hit.choke` on ride/splash/china/crash-high/crash-medium; `choke` (13 Sibelius ids); **Crash-Choke, Tap-Choke, Bell Tap-Choke**; **Crash Cymbals Choke Fat, Cymbal Section Crunch Choke, Cymbal Section Hi-Hat Choke, Suspended Cymbal Short/Fat Choke w/ Stick**; choke / cut-off | grabbing a ringing cymbal to stop it | **NONE on any axis.** `choke` exists in `vocabulary/rules.json` only as a *relation* inside one expansion (`splash.hit` → `crash.hit` + `crash.hit`, `"relation": "choke"`) — the resolver can synthesise a choke, a source file cannot state one | 4+ (ENG SMuFL U+E805; PAS Weinberg p. 21; SW GP, Sibelius, MuseScore, Finale — four vendors; DE/FR chest-damping, below) | D04 §3.5, §5.1 (called "the single clearest gap in this bucket"); rules.json:581–587 |
| "rapprochant de sa poitrine les cymbales" (Berlioz 1843); "nach dem Schlagen schnell **an die Brust gedrückt**" (Haupt & Teuchert 1911) | damping a clashed pair against the chest | **NONE** — nearest relative is the excluded `choke` | **2 independent pre-MIDI traditions, 68 years apart** (FR 1843; DE 1911) | D12 §2.12, §2.16, §5.1 |
| (slap) `hand.hit.slap`; **Slap** across 12 Finale Note Types; Slap on MuseScore Djembe/Doumbek; **Golpe de palma**; *Colpo Pa (slap)* | hand-drum slap tone | technique `slap` | 4 (SW GP, MuseScore, Finale, Sibelius `slap` 41 ids; ES; IT; DE untranslated) | D04 §2.7–§2.9, §2.11, §3.5, §5.3(6); D12 §2.17, §2.18, §3.1 |
| Slap / **Open** / **Bass** (MuseScore Djembe, Doumbek); **Bass Tone** across 6 Finale Note Types; **Tono bajo**; *colpi aperti, posizione morbida* | the hand-drum stroke set | technique `open-tone`, `bass-tone` | 3 (SW MuseScore + Finale; ES; IT) | D04 §2.8, §2.11, §5.3(6); D12 §2.17, §2.18, §3.1 |
| **Dead Stroke** (Finale, across conga, djembe, darbuka, bata, tumba, super tumba, quinto, surdu, tabla); **Dead stroke** used untranslated in German | stick or hand held into the head | technique `dead` | 3 (SW Finale — a named family across nine instruments; ENG SMuFL `pictDeadNoteStem` U+E80D; DE VSL vibraphone, borrowing the English) | D04 §2.1, §2.11, §3.5; D12 §2.13 |
| (mute) `hand.hit.mute`, `brush.hit.mute`, `stick.hit.mute`; **Mute/Muff** Note Types; **Golpe tapado**; *colpi … tono chiuso* | damped stroke | technique `mute-stroke`, damping `muted` | 4 (SW GP, MuseScore, Finale, Sibelius `mute`/`muffled` 46 ids; ES; IT; DE/FR *gedämpft*/*étouffé*) | D04 §2.7–§2.11, §3.5, §3.8; D12 §2.17, §2.18, §3.1 |
| `pictScrapeCenterToEdge`, `pictScrapeEdgeToCenter`, `pictScrapeAroundRim` (ccw), `pictScrapeAroundRimClockwise`; `scrape` (18 Sibelius ids); `stick.scrape.return`; **Scratch Push / Scratch Pull**; **Strisciato**; **Golpe arrastrado** | dragging an implement across a surface | technique `scrape`, `sweep` — **but the direction has no axis** | 5 (ENG SMuFL 4 glyphs + chop U+EE86–EE89; SW Sibelius, GP, Finale; IT; ES; MARCH `zing`) | D04 §2.1, §2.7, §2.9, §2.11, §3.5, §3.14(a); D12 §2.7, §2.18, §3.1 |
| **Schüttelwirbel** (shake roll) | instrument shaken so the jingles sound | technique `shake` | 2 (DE VSL; SW GP Tambourine (roll) `hand.hit.roll`) | D04 §2.7; D12 §2.8, §3.1 |
| **Daumen(spitzen)-Wirbel**; *rullo con il pollice*; **Golpe de pulgar** | wetted thumb dragged round the head | technique `thumb`, `swirl` | 3 (DE; IT; ES) | D12 §2.8, §2.17, §2.18, §3.1, §5.3 |
| **Ping** (`unpitched.metal.cymbal.ride.ping.rock`) | the ride's articulate stick sound | technique `ping-shot` | **1 (SW Sibelius only)** | D04 §2.9, §3.5, §5.2 |
| **pressed** (Sibelius, 10 ids); `pictCrushStem` "Combining crush for stem"; **colpo pressato**; **Pressschlag** | stick pressed into the head | **NONE** — v0.1 has ornament `buzz` for the multi-stroke result, nothing for the single pressed stroke | 3 (SW Sibelius; ENG SMuFL U+E80C; IT Udine §1.5 b; DE Peinkofer/Tannigel *Einzelschlag/Doppelschlag/Pressschlag*) | D04 §2.1, §2.9, §3.5, §5.1; D12 §2.4, §2.10 |
| **Gestrichen** / *con l'arco* / bowed | excited with a violin or double-bass bow | **NONE** — `scrape` is a different physical act | 3 (DE VSL suspended cymbal, tam-tam, vibraphone; IT Facchin p. 115; ENG MusicXML `beater-value` `bow`, SMuFL `pictBeaterBow`) | D04 §2.1, §2.2; D12 §2.7, §2.9, §2.13, §3.2(g), §5.1 |
| **Breiter Schlag**; **Strisciato** (pair) | the two plates shear across each other | **NONE** | 2 (DE; IT) | D12 §2.7, §3.2(g), §5.1 |
| **Vibrato** (cymbal pair) | plates waved after the strike | **NONE** | 1 (DE VSL) | D12 §2.7, §3.2(g) |
| **Watergong**; **Nota pedal** | pitch bent *after* the attack (gong lowered into water; hand pressed into a head) | **NONE** — same class as the excluded `choke` | 2 (DE; ES) | D12 §3.2(f), §5.1 |
| **Chasquido**; *Colpo Snap* | finger snap / pop on a hand drum | **NONE**; and LCMPT has `finger snapping` as an *instrument* | 3 (ES; IT; LIB LCMPT mp2013015264) | D03 §3.3(d), §5.1; D12 §2.17, §2.18, §5.1 |
| **Golpe talón-punta**; **Talón arriba / abajo** | heel-toe as one motion; heel-up vs heel-down pedal posture | v0.1 has `heel` and `toe` as separate values and nothing for the combined motion or the posture | 1 (ES) | D12 §2.18, §3.2(h), §5.1 |
| **Kreuzschlag** (einfach / doppelt); *incroci, allontanamenti* | crossed hands between two drums | **NONE** — the path *between* two slots | 2 (DE VSL; IT Udine §4.1a) | D12 §2.5, §3.2(f) |
| **Unisono-Schläge**; "frapper avec les deux baguettes à la fois" (Berlioz); **Unison** (MuseScore marching-bass) | two beaters or five drums struck as one event | **NONE** | 3 (DE; FR 1843; SW MuseScore) | D04 §2.8, §3.14(i); D12 §2.6, §2.16, §3.2(g) |
| **Abschlag**; *rullo con colpo di chiusura* | the stroke that *terminates* a roll | **NONE** — defined by position in a figure | 2 (DE; IT) | D12 §2.5, §2.17, §3.2(f), §5.1 |
| `gok-shot` (v0.1) | — | **0 attestations in any of the three dossiers** | D04 §5.2 |
| `circling`, `sweep`, `swirl` (v0.1) | rotary/dragging gestures | attested only obliquely: SMuFL scrape/turn glyphs *with a direction*, DE *Daumenwirbel*, ES *golpe arrastrado* | D04 §5.2; D12 §3.1 |
| `chick`, `foot-splash` (v0.1) | the closed and the open pedal hi-hat stroke | **confirmed verbatim**: Weinberg 1994 p. 21 defines the foot splash ("a sound similar to a pair of small crash cymbals, rather than the tight 'chick' sound"); LilyPond ships `splashhihat`/`hhs` in the source file though it is **absent from the published documentation table** | 2 (PAS; SW LilyPond) | D04 §2.6, §2.10, §5.3(5) |
| **Guz** — "Snare Guz Short" (53), "Snare Guz Long" (54) | **unknown**. A real shipping term of Tapspace's Virtual Drumline; no published source defines it | NONE — attested, undefined | 1 vendor (Tapspace via Finale), corroborated as a *string* by bucket 08 | D04 §2.11, §3.5, §6 |

### 1.6 ornament axis

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `swissRudimentsNoteheadBlackFlam`/`HalfFlam`; Snare Flam, Tom Flam; `flam` (33 Sibelius ids); **Einfacher Vorschlag**; *acciaccatura semplice* | one grace stroke | ornament `flam` | 4 (ENG SMuFL U+EE70–71; SW Sibelius, Finale; DE; IT) | D04 §2.1, §2.9, §2.11, §3.6; D12 §2.3, §2.17, §3.1 |
| `swissRudimentsNoteheadBlackDouble`/`HalfDouble` ("**doublé**"); **Zweifacher Vorschlag**; *doppia acciaccatura* | two grace strokes | ornament `drag` — and the Swiss tradition has **one** term (*doublé*) where v0.1 has two (`drag`, `ruff`) | 3 (ENG SMuFL/Basel; DE; IT) | D04 §2.1, §4; D12 §2.3, §2.17 |
| **Dreifacher Vorschlag**; *tripla acciaccatura* ("rullo breve") | three grace strokes | ornament `ruff` | 2 (DE; IT) | D12 §2.3, §2.17, §3.1 |
| **Vierfacher Vorschlag** (four-stroke ruff); *quadrupla acciaccatura*; Italian goes to **quintuple** | four and five grace strokes | **NONE** — v0.1 stops at `ruff` | 2 (DE; IT) | D12 §2.3, §2.17, §5.1 |
| *acciaccature … **singole e rimbalzate*** | grace-count and rebounded-or-not as **two independent parameters** | v0.1's `ornament` conflates them | 1 (IT Udine §1.6c) | D12 §2.4, §3.2(e) |
| **Buzz**; **Presswirbel / Druckwirbel / geschlossener Wirbel**; *rullo pressato / rullo chiuso*; Snare Buzz Roll | uncontrolled pressed multi-stroke roll | ornament `buzz` | 4 (SW MuseScore marching-snare + marching-tenor, Finale; DE — defined as *nicht kontrollierte* Pressschläge; IT; PAS "press roll") | D04 §2.8, §2.11, §3.6; D12 §2.3, §2.10, §3.1, §5.3 |
| **Offener Wirbel / Doppelschlagwirbel**; *rullo aperto*; *colpo doppio rimbalzato* | controlled double-stroke roll | ornament `roll` / `bounced` | 3 (DE; IT; PAS) | D12 §2.3, §2.4, §2.10, §3.1 |
| **Einzelschlagwirbel / Paukenwirbel**; *rullo a colpi singoli*; **Redoble de golpe simple**; MusicXML/LilyPond none | the single-stroke roll | **NONE** — `roll`, `buzz`, `bounced` are none of them specifically this | **3 (DE, IT, ES)** | D12 §2.4, §2.10, §3.2(e), §5.1 |
| **rullo militare** (legato e slegato) | a named roll kind distinct from both open and pressed | **NONE** | 1 (IT Udine, an official syllabus) | D12 §2.4, §3.2(e) |
| **Einhändiger Wirbel / Gravity Roll / Freehand** (Johnny Rabb) | one-handed roll against the rim | **NONE** | 1 (DE) | D12 §2.10, §3.2(e), §5.1 |
| **Rullo rovesciato**, **Rullo al galoppo**, **Rullo lungo il braccio**, **Rullo riz**, **Rullo o tremolo ad altalena con le dita**, **Rullo coronato** | reversed / gallop / along-the-arm / daf *riz* / see-saw finger / fermata roll | **NONE** — a roll's internal shape or body part | 1 (IT Facchin pp. 41, 42, 45, 501, 787, 918) | D12 §2.17, §3.2(e) |
| **Übergangswirbel**; *cambio di note durante un rullo*; **Doppelwirbel** | a roll that migrates between drums; one roll on two drums | **NONE** — one event, two slots | 2 (DE; IT) | D12 §2.5, §2.17, §3.2(f) |
| `crescendo`, `swell` (v0.1) | dynamic shape of a roll | confirmed: Sibelius `crescendo` 6 ids, `unpitched.metal.cymbal.roll.crescendo`; *rulli crescendo-diminuendo*, *rullo in crescendo e diminuendo*; Finale *Suspended Cymbal Cresc (Loud)* | 3 (SW; IT; DE *Wirbel*) | D04 §2.9, §2.11, §3.6; D12 §2.3, §2.17, §5.3 |
| `wash` (v0.1) | — | 0 attestations in these dossiers | — |

### 1.7 openness axis

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `pictOpen` U+E7F8; Hi-Hat (open) `stick.hit.open`; `openhihat`; Open Hi-Hat; `open` (49 Sibelius ids); Weinberg's open-circle articulation; **Charleston ouverte**; *ouverte* | pedal released | openness `open` | 5 (ENG SMuFL; SW GP, LilyPond, MuseScore, Sibelius, Finale, Dorico FR docs; PAS; FR; DE) | D04 §2.1, §2.6–§2.11, §3.7; D12 §2.15 |
| Hi-Hat (closed); `closedhihat`; `closed` (68 ids); Weinberg's plus sign, and "It should be assumed that all hi-hat notes are to be played on the closed hi-hat unless…"; **Charleston fermée** | pedal down | openness `closed` | 5 (same) | D04 §2.6–§2.11, §3.7; D12 §2.15 |
| `pictHalfOpen1`, `pictHalfOpen2` "Half-open 2 (Weinberg)"; Hi-Hat (half) `stick.hit.half`; `halfopenhihat`; `halfway` (3 ids); Weinberg's bisected circle | pedal partly down | openness `half` | 4 (ENG; SW GP, LilyPond `weinberg-drums-style` only, Sibelius; PAS) | D04 §2.1, §2.6, §2.7, §2.9, §2.10, §3.7 |
| `tight`, `closed-loose`, `quarter`, `three-quarter`, `loose` (v0.1) | five further openness anchors | **0 attestations.** "Every notation source tops out at three steps"; MusicXML has **no** open/closed hi-hat value at all, MEI none for percussion | D04 §3.7, §5.2 |

### 1.8 damping axis

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `pictDamp1`–`pictDamp4`, `handbellsDamp3`; `damp`; Sibelius `damp` 12 ids | damped — **four SMuFL symbols from four notational traditions, not four degrees** | damping `damped` | 3 (ENG; SW Sibelius; DE/IT *gedämpft*, *smorzamento*) | D04 §2.1, §2.2, §2.4, §2.9, §3.8, §4; D12 §2.3, §2.13 |
| **Coperto** / **voilé** / **étouffé** / **tapado** / **gedämpft** / **timbales voilées ou couvertes** + **morceau de drap** (Berlioz 1843) | a cloth laid on the head | damping `towel` — and this is where its provenance is | **4** (FR 1843 *and* modern FR; DE 1911 + VSL; IT; ES) | D12 §2.3, §2.12, §2.16, §3.1, §4.2 |
| **Secco** | struck and damped immediately — *not* the same as coperto, which damps before the stroke | damping `damped` at zero delay | 2 (DE/IT usage across timpani, bass drum, cymbals, tam-tam, vibraphone; ES *seco*) | D12 §2.5–§2.9, §2.13, §3.1, §4.1 |
| **laissez vibrer** (Berlioz); "all instruments of the drumset be allowed to ring for the entire length of their natural decay" (Weinberg) | let ring | damping `none` | 2 (FR 1843; PAS 1994) | D04 §2.10; D12 §2.16 |
| **pressed** (Sibelius) | pressed stroke as a damping state | **NONE** | 1 | D04 §3.8, §5.1 |
| `gated` (v0.1) | studio gate | **0 attestations** — "studio terms, not notation terms" | D04 §3.8, §5.2 |
| **Pedaldämpfung vs Schlägeldämpfung**; *smorzamenti ausiliari ("Dampening")* | pedal-damped vs mallet-damped — the *mechanism* of damping | **NONE** — `damping` names only the audible result | 2 (DE ISB Bayern; IT Udine §2.4) | D12 §2.11, §3.2(c), §5.1 |

### 1.9 mechanism axis

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `snares (drum components)` AAT 300041860; Knight suffix **`-x`** "snare (of any material) crossing the surface of a drum head"; `pictSnareDrumSnaresOff`, MusicXML `snare drum snares off`; **mit entspannten Schnarrsaiten / Teppich ab**, **sans timbre**, **senza corde**; FR **timbre** = the wires, **déclencheur** = the throw-off; IT **cordiera**, **macchinetta tendicordiera**, **fili** | snare wires engaged or not | mechanism `wires-on` / `wires-off` | 5 (LIB AAT; ORG Knight; ENG SMuFL + MusicXML — **both model it as a different instrument, not a state**; DE; FR; IT) | D03 §2.3, §2.10, §3.1; D04 §2.1, §2.2, §3.9; D12 §2.3, §2.15, §2.19, §3.1 |
| "die angezogenen **Saiten … nachläßt**" | wires *slackened* — a third state between on and off | **NONE** | 1 (DE 1911) | D12 §2.12, §5.1 |
| "das ganze, straff angezogene **Fell nachläßt**" | the head itself detuned to kill it | **NONE on any axis** — not damping (nothing touches the head), not an existing mechanism value | 1 (DE 1911) | D12 §2.12, §5.1 |
| **Nieten / Kugelkette / Stahlnadel**; *piatti chiodati*, *cymbales grésillantes/cloutées* | rivets, ball chain, steel needle — **three distinct sizzle devices** | **NONE** — v0.1 bakes one of them into instrument `sizzle-ride` | 2 (DE VSL; IT/FR via Facchin's index) | D12 §2.7, §2.2, §3.2(c), §5.1 |
| Knight suffix **`-s`** "sympathetic or co-vibrator, as in bottle caps on an mbira" — explicitly *not* a classification change | the same fact, from organology | as above | 1 (ORG Knight p. 37) | D03 §2.3, §5.3(a) |
| H-S suffix **`-9211`** "with mechanism (Machine timpani)", **`-92111`** pedals | pedal-operated tensioning | nearest v0.1 is `kick-*`; no value | 1 (ORG) | D03 §2.1.2, §3.1 |
| **Vibrato / Senza vibrato** (vibraphone motor) | motor on/off | **NONE** | 1 (DE VSL) | D12 §2.13, §5.1 |
| **air-lock** | the hi-hat's air-release feature, which changes the closed sound | **NONE** | 1 (IT trade, Facchin p. 104) | D12 §2.7, §3.2(c) |
| `kick-damped`, `kick-half-open` (v0.1) | — | **0 attestations anywhere** | D04 §3.9, §5.2 |

### 1.10 implement axis

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| `drumsticks (percussion beaters)` AAT 300042613 (with scope note); `pictDrumStick`, `snare stick`, `jazz stick`; **baguettes**, **Trommelstöcke**, **bacchette**, **baquetas**; Knight `-1`/`-2` one/two sticks | wooden stick | implement `stick`, `jazz-stick` | 5 (LIB AAT; ORG Knight; ENG SMuFL U+E7D1–E7D4, U+E7E8, MusicXML; SW; DE/FR/IT/ES) | D03 §2.5, §2.3, §3.1; D04 §2.1, §2.2, §3.10; D12 §2.3, §2.19, §3.1 |
| `percussion brushes` AAT 300429059 + `wire brushes` 300202390 (with scope note); `pictBeaterWireBrushes`, `wire brush`; **Stahlbesen**, **balais**, **spazzole**; Weinberg's closed set of four | wire brush | implement `brush` | 5 (LIB AAT; ENG; PAS; SW Sibelius `brush` 28 ids, GP `brush.hit.*`; DE/FR/IT) | D03 §2.5; D04 §2.1, §2.2, §2.7, §2.9, §2.10, §3.10; D12 §2.3, §2.7, §3.1 |
| `hammers (percussion beaters)` AAT 300042609, `gong mallets` 300425007; `stick-type` × `stick-material`; **mazzuole**, **Schlägel**; Weinberg **Hard Mallet / Soft Mallet** | mallet | implement `mallet-soft/-medium/-hard` | 4 (LIB AAT; ENG; PAS; DE/IT) | D03 §2.5; D04 §2.1, §2.2, §2.10, §3.10; D12 §2.3, §2.5 |
| **fagots** / **Ruten** | bundled rods | implement `rod` | 2 (FR; DE) | D12 §2.15, §3.1 |
| `pictBeaterHand` U+E7E3, `hand`; Knight `-3`/`-4`; **Anschlag mit der Hand**, **con la mano**, **mains nues**, *percussione con le mani* | bare hand | implement `hand` | 5 (ENG; ORG Knight; SW GP `hand.hit.*`; DE; FR; IT) | D03 §2.3; D04 §2.1, §2.2, §2.7, §3.10; D12 §2.5, §2.6, §2.15, §3.1 |
| `pictBeaterFinger` U+E7E4, `finger`; **Fingertips** (Finale, Djembe); *percussione con le dita*; **Mittelfinger**, **Daumen**, **Fingerknöchel**, **Handballen**, **Ellenbogen**, **Knie** | finger — and, in German, four more body parts down to elbow and knee | implement `finger`; elbow and knee have **no value** | 4 (ENG; SW Finale, Sibelius `finger`/`fingers` 18 ids; IT; DE) | D04 §2.1, §2.9, §2.11, §3.10; D12 §2.3, §2.8 |
| `pictBeaterFist` U+E7E5, MusicXML `beater-value` **fist** | the closed fist | **NONE — genuine gap.** D04 §5.1 resolves it: axes.json serial 1 holds exactly 14 implement values and `fist` is not among them; the round-2 brief listed it from an earlier axis sketch | **3** (ENG SMuFL + MusicXML = 1; MARCH Casey Claw "held in a fist, where all the fingers wrap around the stick" — late-findings item 5, **not in my dossiers**; D12 flags the brief/axes.json discrepancy independently) | D04 §5.1; D12 §5.1 |
| `pictBeaterFingernails` U+E7E6, MusicXML `fingernail`; MEI `fingernail`; **Fingernagel**; *riz con le unghie* | struck with the nail | **NONE — genuine gap** (same resolution as `fist`) | 3 (ENG SMuFL + MusicXML + MEI; DE VSL; IT Facchin p. 815) | D04 §2.1, §2.2, §2.4, §5.1; D12 §2.7, §2.17, §3.1 |
| `pictSuperball`, `superball`; **Superball** | rubber ball dragged for a friction tone | implement `superball` | 3 (ENG; PAS names it among "esoteric beaters"; DE VSL tam-tam) | D04 §2.1, §2.2, §2.10; D12 §2.9, §5.3 |
| `pictBeaterBow` U+E7DE, `beater-value` **bow**; **Cello- oder Kontrabassbogen**; *arco di contrabbasso* | a string bow used on a cymbal/vibraphone | **NONE**, and minting it collides with site `bow` | 3 (ENG; DE; IT) | D03 §4.8; D04 §2.1, §2.2, §4, §5.3(2); D12 §2.7, §2.13, §5.1 |
| **coin**, **knitting needle**, **spoon mallet**, **guiro scraper**, **chime hammer**, **metal hammer**, **triangle beater**, **triangle beater plain**, **brass mallets**, **slide brush on gong** | MusicXML `beater-value`'s remaining 10 of 20 | **NONE** | 2 (ENG SMuFL + MusicXML = 1; PAS lists knitting needles, rattan sticks, Superballs and coins as "esoteric beaters… indicated by a brief word") | D04 §2.1, §2.2, §2.10, §5.1 |
| **Lederkopfschlägel**; "ein mit **Leder überzogener Holzklöppel**" (1911, tam-tam) | leather-headed beater | **NONE** | **2** (DE VSL; DE 1911 — a century apart, but one language tradition) | D12 §2.6, §2.12, §5.1 |
| **baguettes à tête d'éponge** (Berlioz 1843); **Schwamm**, **Kork** (1911) | sponge- and cork-headed timpani beaters | **NONE** | **2 independent traditions** (FR 1843; DE 1911) | D12 §2.12, §2.16, §5.1 |
| **Triangelstab / Triangelschlägel** used on the tam-tam; `pictBeaterMetal*` U+E7C7–CA | a metal beater | **NONE** — v0.1 has felt/wood/plastic/rubber, no metal | 2 (DE; ENG) | D04 §2.1; D12 §2.9, §5.1 |
| **Kralle** ("claw") | a dedicated tam-tam scraper | **NONE** — `technique.scrape` exists with no tool to do it; MIMO/LCMPT have the *instrument* class `Scrapers`/`Râcloir`/`raspa`/`rascador` | 2 (DE VSL; LIB MIMO 3058) | D12 §2.9, §3.2(d), §5.1 |
| **Messing, Rosenholz, Ebonitholz, Hartgummi, Garn, Schnur** (vibraphone); **Garn, Schnur, Stoff, umwickelt, Gummi, Paukenfilz, Holz** (cymbal) | mallet head materials as an open list | **NONE** for brass, rosewood, ebonite, cord | 1 (DE VSL) | D12 §2.7, §2.13, §5.1 |
| MusicXML **`stick-type` (10 shapes) × `stick-material` (5 hardnesses)** | a **two-dimensional decomposition** of the beater | **NONE** — v0.1's `mallet-soft/-medium/-hard` encodes hardness only and cannot say "hard yarn" vs "hard gum" vs "wound, hard core" | 1 (ENG), corroborated in structure by DE **Kopf / Bezug / Stiel / Form** and **Groß-, Mittel-, Kleinkopf** | D04 §2.2, §3.10, §5.1; D12 §2.9, §3.2(d) |
| SMuFL beaters range, **128 glyphs** U+E770–U+E7EF | ≈32 implements × 4 orientations | orientation is **not physical** — it is which way the pictogram points | 1 (ENG) | D04 §2.1, §3.14(f) |
| `pictBeaterCombiningParentheses` "(padded)", `pictBeaterCombiningDashedCircle` "(plated)" | beater modifiers that **are** physical | **NONE** — `implement` is a flat list with no modifier slot | 1 (ENG) | D04 §2.1, §3.14(g) |

### 1.11 dynamic, timbre, voicing

| Term | Physical meaning | v0.1 axis | Traditions | Locator |
|---|---|---|---|---|
| **ghost stroke** — parenthetical notehead, "on any type of instrument (drums, cymbals, cowbells, etc.)" | a very quiet stroke | dynamic `ghost` | 1 (PAS) — the only percussion-specific dynamic value in D04 | D04 §2.10, §3.11 |
| **"Full"**, **"Tap"**, **colpo "accademico"**, **colpo "a pistone"**, **colpo libero** | stroke *height and trajectory*, not loudness. "a Tap and a ghost note are not the same thing" | **NONE** — `normal/ghost/soft/hard/accent` names loudness | 1 (IT Udine, an official syllabus) — plus **Tap / Muted Tap / Bell Tap** in MuseScore marching-cymbals, where it means a light plate contact | D04 §2.8, §3.14(c); D12 §2.4, §3.2(b), §5.1 |
| "**Forte in der Fellmitte, Piano eher am Fellrand**" | striking position as a **function of dynamic**, in solo snare practice — "Dies gilt nur für Solo-Werke, beim Drum-Set wird die Snare-Drum grundsätzlich in der Mitte angespielt" | **no axis can hold a rule linking two axes** | 1 (DE, official standard) | D12 §2.11, §5.2 |
| `drum.snare-drum.electric`, `drum.tom-tom.synth`; Electric Snare; Sibelius `electric` | electronic timbre | timbre `electronic` | 3 (ENG Standard Sounds; SW LilyPond, MuseScore, Sibelius; LIB LCMPT `drum machine` UF *electronic percussion*) | D03 §2.6; D04 §2.3, §2.6, §2.8, §2.9, §3.12 |
| Sibelius **`kit-tr-808`** | the 808 as vocabulary rather than a program-change number | timbre `analog-808` | 1 (SW Sibelius) — `analog-909`, `-707`, `-606`, `-cr78`, `fm`, `pcm`, `physical`, `chip`, `noise` have **no attestation in any of my three dossiers** | D04 §2.9, §3.12 |
| Sibelius **`kit-standard`, `kit-room`, `kit-power`, `kit-jazz`, `kit-orchestra`, `kit-brush`, `kit-electronic`** — the GM-2 kit list expressed as vocabulary; id elements `jazz` (30), `fusion` (28), `rock` (15), `orch` (14), `concert` (5) | production voicing | voicing `standard`, `room`, `power`, `jazz`, `orchestra`; **`fusion`, `rock`, `concert`, `brush` missing**; `lo-fi` and `dark` unattested | 1 (SW Sibelius) | D04 §2.9, §3.13, §5.1 |
| Sibelius `ambient`, `big`, `dry`, `dink`, `sloppy`, `a-list`, `sequential` | vendor patch names | **not vocabulary** — correctly excluded | 1 | D04 §3.13 |

### 1.12 Reference-axis and out-of-band terms

| Term | Physical meaning | v0.1 | Traditions | Locator |
|---|---|---|---|---|
| H-S "**sets of**" vs "individual" — 111.211/.212, 111.241.1/.2, and the kit itself as 211.212.21 | multiplicity as a class distinction | v0.1 handles it **better**, with `instance` on the layout slot rather than in the term | 1 (ORG) — direct organological support for the decision, "should be cited in ADR-0001" | D03 §3.3(c) |
| Knight `#n` "number of sounding elements" | same | reference axis `instance` | 1 (ORG Knight) | D03 §2.3 |
| Knight `-1`…`-5`: one stick / two sticks / one hand / two hands / **stick and hand** | implement **and** limb count in one symbol | v0.1's split (implement on the term, `limb` on the slot) is **better than Knight's** — but **`-5` "stick and hand" has no KITWARP expression at all** | 1 (ORG) | D03 §2.3, §5.5 |
| `pictRightHandSquare` / `pictLeftHandCircle` (Agostini); Weinberg's R/L sticking letters; GP Left/Right Maraca; Sibelius `left`/`right` (18/18); Finale **LH** across ~15 Note Types; MuseScore Drum 1–5 | which hand, which of a pair | reference axis `limb`, `instance` — "**every notation source puts it on the note**" | 4 (ENG; PAS; SW; MARCH) | D04 §2.1, §2.9–§2.11, §3.14(h) |
| **Handsatz / Handsätze** (r-l-l-r), dependent on **Aufstellung** (European vs American timpani layout); *scelta delle mani*; **Paradiddle**; **Mühle**; **Tecnica Split-Hand** | which hand plays which note, across a *sequence* | **NONE** — `limb` is per-event; nothing carries a sequence of limbs | 2 (DE ISB Bayern + VSL; IT Facchin p. 471, Udine §2.3) | D12 §2.3–§2.5, §2.11, §3.2(a) |
| **Presa delle bacchette**, presa parallela vs tradizionale, **Burton / Musser / Stevens**, **Gabelgriff** | grip | **NONE** — "neither implement, nor contact, nor technique — but audibly different" | 2 (IT; DE) | D12 §2.3, §2.4, §2.11, §3.2(b) |
| Hi-hat pedal position; `choke_amount`; radial strike position | continuous controllers | v0.1 `controllers` (5) — **no source in any of my three dossiers has a continuous controller concept**; MusicXML's `stick-location` has four discrete values and hangs off a `<direction>`, not the note | 0 | D04 §2.2 |

---

## 2. NO-AXIS TERMS, grouped by the missing thing

Ordered by how many independent traditions demand the missing thing.

### 2.1 A missing `choke` value — an after-attack relation that a source file cannot state

`choke` (SMuFL `pictChokeCymbal`, GP on five instruments, Sibelius 13 ids, MuseScore three
Note Types, Finale five, Weinberg's cut-off notation), **chest-damping** (Berlioz 1843,
Haupt & Teuchert 1911), **Watergong** (DE), **Nota pedal** (ES), **Abschlag** / *rullo con
colpo di chiusura* (DE, IT), **Rullo coronato** (IT).
*What is missing*: a way to state, on the term, that this event modifies a previously sounded
one. `vocabulary/rules.json` has `choke` as a *relation* used in exactly one expansion, which
lets the resolver synthesise a choke but gives a MusicXML, Dorico, Finale, MuseScore or Guitar
Pro import nowhere to land. **Six vendor sources plus two pre-MIDI traditions plus one
notation standard.** D04 §5.1 calls it "the single clearest gap in this bucket"; D12 §2.16
calls the two pre-MIDI chest-damping attestations "the strongest evidence in this dossier that
the exclusion of `choke` leaves a real hole". *Locators*: D04 §3.5, §3.14(c), §5.1; D12 §2.12,
§2.16, §3.2(f), §5.1; `vocabulary/rules.json` lines 581–587.

### 2.2 A missing direction / trajectory qualifier

`pictScrapeCenterToEdge`, `pictScrapeEdgeToCenter`, `pictScrapeAroundRim` (ccw),
`pictScrapeAroundRimClockwise`, `stringsScrapeCircularClockwise`/`Counterclockwise`,
`pictTurnRightStem`/`TurnLeftStem`/`TurnRightLeftStem`, `handbellsSwingUp`/`SwingDown`;
Guitar Pro `stick.scrape.return`; Finale **Scratch Push** / **Scratch Pull** where direction is
the *only* difference; **Strisciato** "one plate rubbed **from centre to edge**"; the marching
**zing**, defined as a scrape "**bell outward**".
*What is missing*: either a direction qualifier (in/out, cw/ccw) or a second site slot
(`site_from`, `site_to`). D04 calls this "**a missing axis, on the evidence of six separate
sources**". *Locators*: D04 §3.14(a); D12 §2.7, §3.2(g).

### 2.3 A missing hand-cymbal (piatti) instrument and its plate-against-plate contact set

MuseScore `marching-cymbals`: **Full Crash, Half Crash, Hi-Hat, Sizzle, Crash-Choke, Tap,
Tap-Choke, Bell Tap, Bell Tap-Choke, Muted Tap, Smash, Zing, Roll**; Finale **Crash Cymbals
Crash / Click / Ding / Choke Fat**, **Cymbal Section Crash / Click / Crunch Choke / Hi-Hat
Choke**; Guitar Pro **Piatti (hit) / (hand)**; MusicXML `crash cymbals`; SMuFL `pictCrashCymbals`;
DE **Breiter Schlag**, **Vibrato**, "an die Brust gedrückt"; IT **piatti a mano in coppia**,
**Strisciato**; FR **cymbales choquées**.
*What is missing*: the instrument is *a pair of plates*, so `site`, `contact` and `implement`
are all empty and `technique` would have to carry the whole distinction. Two independent
program vocabularies enumerate the same family from different vendors' libraries, and three
European score traditions name its strokes. Corroboration outside the programs varies:
`zing` six institutionally independent marching sources (via bucket 08), `suc` four, `crunch`
two, `smash` one. *Locators*: D04 §3.14(c), §5.1; D12 §2.2, §2.7, §2.12, §2.16, §4.1.

### 2.4 A missing beater decomposition — the implement is not one slug

MusicXML `stick-type` × `stick-material` (10 shapes × 5 hardnesses); SMuFL's 128 beater glyphs
≈ 32 implements × orientation; `pictBeaterCombiningParentheses` "(padded)" and
`pictBeaterCombiningDashedCircle` "(plated)"; DE **Kopf / Bezug / Stiel / Form** as four
independent parameters and **Groß-, Mittel-, Kleinkopf** as head size independent of material;
DE/FR/IT material lists (Garn, Schnur, Hartgummi, Rosenholz, Messing, Ebonitholz, Leder,
Schwamm, Kork, Flanell).
*What is missing*: a material dimension crossed with a hardness dimension, plus a modifier slot.
v0.1's `mallet-soft/-medium/-hard` cannot say "hard yarn" vs "hard gum" vs "wound, hard core".
**Three traditions** (ENG, DE, IT). *Locators*: D04 §2.2, §3.10, §3.14(g), §5.1; D12 §2.6,
§2.7, §2.9, §2.12, §2.13, §3.2(d), §5.1.

### 2.5 A missing roll taxonomy — `roll` is one slug where three languages have five to eight

**Einzelschlagwirbel / Paukenwirbel** (DE), *rullo a colpi singoli* (IT), *redoble de golpe
simple* (ES) — the single-stroke roll, named in three languages and absent from v0.1;
**Einhändiger Wirbel / Gravity Roll / Freehand**; *rullo militare* (legato/slegato);
*rullo rovesciato*, *al galoppo*, *lungo il braccio*, *riz*, *ad altalena con le dita*,
*coronato*; **Übergangswirbel** / *cambio di note durante un rullo*; **Doppelwirbel**;
**Schüttelwirbel** / **Daumenwirbel** / **Schlägel-Wirbel** (three tambourine rolls named by
mechanism where English says "roll").
*What is missing*: `ornament.roll` is unqualified. "Any alias mapping *Wirbel* → `roll` loses
which roll." Also missing: the grace-count / rebounded-or-not split (*acciaccature singole e
rimbalzate*), and counts above three (*vierfacher Vorschlag*, *quadrupla*, *quintupla*).
*Locators*: D12 §2.4, §2.5, §2.8, §2.10, §2.17, §3.2(e), §5.1, §5.2.

### 2.6 A missing head-identity concept — which head, not which side

H-S 211.212.11 "one skin used for playing" vs 211.212.12 "both heads played"; Knight makes head
count his **first** subdivision, ahead of shape; FR **peau de résonance / peau inférieure**,
DE **Resonanzfell**, IT **pelle risonante**.
*What is missing*: v0.1's `site = underside` is a geometric term where three traditions name a
*head*. D03 §3.3(a) notes this is what a gong-drum kick, an underside tom hit and Roland's
`Bongo H Inner`/`Edge` pair are about. **Recommendation in the dossier**: a `site` value
`resonant-head`; under ADR-0003 `underside` cannot be renamed, so this is a new value plus
possibly a `correction` alias. **3 traditions** (ORG, FR, DE/IT). *Locators*: D03 §2.1.2,
§3.3(a); D12 §2.15, §3.2(h), §5.1.

### 2.7 A missing sequence/figure layer — properties of several notes, not of one

**Handsatz / Handsätze** and **Aufstellung** (DE); **Paradiddle**, **Mühle**, **Tecnica
Split-Hand** (DE, IT); *scomposizione del rullo* (IT); Weinberg's R/L sticking; Knight `-5`
"stick and hand" (one event stream, two implements); **Unisono-Schläge** / "avec les deux
baguettes à la fois" / MuseScore **Unison**; Sibelius `unpitched.metal.cymbal.ensemble.*` and
`…hi-hat.ensemble`; handbell **lift** gestures (`martellato lift`, `mallet lift`, `pluck lift`,
`mallet table` vs `mallet bell suspended`) where the damping *changes during the note*.
*What is missing*: nothing in v0.1 spans events, spans limbs within one event, or aggregates a
section into one notated event. **5 traditions** (ORG, ENG, PAS, SW, DE/IT/FR).
*Locators*: D03 §5.5; D04 §3.14(b), §3.14(h), §3.14(i); D12 §3.2(a), §2.16.

### 2.8 A missing stroke-form / stroke-height dimension

**colpo "accademico"**, **colpo "a pistone"**, **"Full"**, **"Tap"**, **colpo libero** (IT
Udine); the four Burton-grip stroke types *doppio verticale, singolo indipendente, singolo
alternato, doppio laterale*; grip itself (*presa*, Gabelgriff, Musser, Stevens); the ISB rule
that position is a function of dynamic.
*What is missing*: D12 §5.1 proposes "a `stroke-form` axis may be the honest answer".
1–2 traditions (IT, DE). *Locator*: D12 §2.4, §2.11, §3.2(b), §5.1.

### 2.9 A missing build-property layer (belongs on the device layout, not the pivot)

Knight `-a`/`-b`/`-c` thin/medium/thick head, `-h` handle drum, `-s` sympathetic vibrator;
H-S's entire membranophone suffix set (`-6` glued, `-7` nailed, `-8` laced, `-81` cord-braced …
`-9211` machine, `-92111` pedal) — **all of which describe how the head is attached, none how
the drum is played**; IT *piatti sospesi con **cupola** cilindrica e **bordo all'insù***;
*allenatore / allenatori di gomma* (the practice pad, treated by an official syllabus as an
instrument distinct from the tamburo).
*What is missing*: nothing on the pivot should hold these — but v0.1 smuggles one in as
instrument `sizzle-ride`. *Locators*: D03 §2.1.2, §2.3, §3.3(b), §5.3(a); D12 §2.17, §3.2(h).

### 2.10 A missing instrument-identity layer for body percussion and non-instruments

LCMPT `body percussion` (mp2013015090) with children *armpit squeezing, body slapping,
finger snapping, foot tapping (UF foot percussion, podorhythm), hand clapping, head rapping,
vocal percussion (UF mouth drum, bouladjèl), whistling*, all under *concussion idiophone*;
Knight p. 11: "the floor is the instrument – a struck idiophone, while the foot is only the
beater"; ES **Chasquido**; IT *fischio sul bordo della carta*.
*What is missing*: v0.1 has instrument `clap` and implement `hand`/`finger`, which cannot
express *finger snapping* (no instrument at all) or *foot tapping* (the floor is the
instrument). D03 §3.3(d): "**`finger-snap` and `foot-stomp` are missing instrument values, not
technique values.**" 3 traditions (LIB, ORG, ES/IT). *Locators*: D03 §3.3(d), §5.1; D12 §2.17,
§2.18.

### 2.11 A missing stroke-length concept

MusicXML Standard Sounds and LilyPond both mint **two instruments** where there is one
instrument and two stroke lengths: `shortguiro`/`longguiro`, `shortwhistle`/`longwhistle`;
MuseScore Short/Long Güiro; Finale *Whistle Short/Long*, *Guiro Short/Long*, *Snare Guz
Short/Long*; GP Guiro (hit) vs (scrap-return).
*What is missing*: KITWARP has no duration or stroke-length concept on the term. **The standards
resolve it by minting instruments — exactly the identity inflation this project exists to
avoid.** 2 traditions (ENG, SW). *Locator*: D04 §3.14(d).

### 2.12 A missing "return" stroke

Guitar Pro `hand.hit.return` (tambourine, cabasa, maraca, shaker), `stick.hit.return` (bell
tree), `stick.scrape.return` (guiro).
*What is missing*: on a shaken instrument the back-stroke is a separate attack with a different
sound; v0.1's `shake` and `swirl` treat the gesture as one event. **1 tradition, 1 vendor** —
weak, and should be labelled so. *Locator*: D04 §3.14(e), §5.1.

### 2.13 A missing superordinate category layer

DE **Klangverfremdung** — an official standard's named class over all timbre-alienating strokes
(Rand, Korpus, Stock auf Stock); IT **Zone di percussione** — the superordinate over `site` +
`position`; ES **Tonos abiertos / Tonos tapados / Golpes alternativos** — three named classes
over the hand-drum strokes, "which is itself the finding — English pedagogy names the strokes
but rarely the classes"; MIMO/LCMPT/AAT all keep such classes.
*What is missing*: v0.1 has flat axis values and no class layer over them. 3 traditions (DE, IT,
ES). *Locators*: D12 §2.11, §2.18, §3.2(h).

### 2.14 Things that correctly fit no axis and must stay out

Beater **orientation** (Up/Down/Left/Right on nearly every SMuFL beater; MusicXML
`tip-direction`'s eight values incl. northwest/southeast) — "not a physical distinction, it is
which way the pictogram points on the page… the 128 glyphs are roughly 32 implements ×
orientation". Playing-technique-specific **noteheads** as identity (Dorico). The **blank
pictogram** `pictEmptyTrap`, MusicXML `other-percussion` and `smufl-pictogram-glyph-name`,
Sibelius's *secondary* ids, Dorico's free-text `xmap.*` ids — **every one of these standards
ships an explicit escape hatch. D04 §3.14(j): "a closed set plus a documented escape hatch is
the shape all four of them converged on", and says it is worth an ADR.**
*Locators*: D04 §3.14(f), §3.14(j), §3.14(k), §2.9, §2.12.

---

## 3. FALSE FRIENDS

### 3.1 One word, several meanings

| Word | Meaning A | Meaning B (and C…) | Locator |
|---|---|---|---|
| **bell** | v0.1 site: the raised dome of a cymbal | v0.1 instrument (id 17): a struck bell — **the same slug on two axes of one vocabulary**; plus MusicXML `metal-value` `bell`, SMuFL `pictBell`/`pictHandbell`/`pictBellPlate`/`pictBellTree`, MuseScore "Ride Bell" as an *instrument name*, MuseScore "Bell Tap" as plate-to-plate contact, 25 `metal.bells.*` sound ids, LCMPT mp2013015079 with 11 children, MIMO `Bells` 2371 with 69, H-S 111.242. **Six meanings; any importer that string-matches "bell" will be wrong most of the time** | D03 §4.7, §5.3(b); D04 §4 |
| **bow** | v0.1 site: the cymbal's playing area | an **implement**: a horsehair stick — MusicXML `beater-value` `bow`, SMuFL `pictBeaterBow`, MIMO `Elements of musical instruments` → `Bows` (2206) = Ajaeng bow, Haegeum bow…; DE *Kontrabassbogen*, IT *arco*. D03 §4.8 calls it "the worst word in the kit vocabulary". Both readings are standard in percussion and bowing a cymbal is a real technique KITWARP will need | D03 §4.7, §4.8; D04 §4, §5.3(2); D12 §2.7 |
| **open** | hi-hat openness | hand-drum open tone (LilyPond uses the **same** token `open` for congas and hi-hat); MEI `open` = "Full (as opposed to stopped) tone" (brass); undamped triangle (`opentriangle`); `opencuica`. Four physically unrelated meanings | D04 §2.6, §4 |
| **half** | GP "Hi-Hat (half)" = openness | MuseScore "Half Crash" = hand cymbals with reduced contact; MusicXML `harmon-closed-value` `half` = a mute position | D04 §4 |
| **damp** | v0.1 damping axis | MEI `damp` = "Stop harp string from sounding"; SMuFL `pictDamp1`–`4` = four symbols from four traditions, **not four degrees**; AAT `damping` 300256220 = a generic conservation/engineering activity | D03 §4.7; D04 §4 |
| **slap** | conga/bongo/djembe hand stroke | MusicXML Standard Sound `effect.slap` = a slapstick/whip sound effect; `effect.bass-string-slap`; `rattle.vibraslap` (an instrument); MuseScore instrument `slap` | D04 §4 |
| **crash** | v0.1: a single suspended cymbal on a stand | in every non-English orchestral source, the **clashed pair**: Facchin's index sends *Crash cymbals*, *Cymbales choquées*, *HandBecken*, *2 Beckenteller* all to *piatti a mano in coppia*; MusicXML `crash cymbals` is a pair; MuseScore has both, mapping each to `metal.cymbal.crash` | D04 §4; D12 §2.2, §4.1, §5.2 |
| **cymbal** | a suspended kit cymbal | in H-S, a **pair clashed together** (111.142 under "Concussion vessels… struck against each other") | D03 §4.3, §4.7 |
| **percussion** | striking generally | in H-S, `111.2 Percussion idiophones` is *specifically* the non-concussion case | D03 §4.7 |
| **percussion instruments** | everything you hit | in Getty AAT, **membranophones only** — idiophones sit in a parallel acoustical hierarchy, so `percussion instruments` has 92 extended descendants while `idiophones` has 177 that are not among them | D03 §2.5, §4.7 |
| **tom-tom** | the kit tom | LCMPT mp2013015737's only UF term is *Chinese tom-tom* | D03 §4.7 |
| **roto-tom** | a tunable single-head shell | Getty and LCMPT classify it under **frame drums** | D03 §4.7 |
| **shell** | v0.1 site: a place to hit | AAT `shells (drum components)` 300041856: the drum body as a museum artefact | D03 §4.7 |
| **Sidestick** | v0.1 technique | GND 4370425-6 `Sidestick` is an **aircraft control stick**, broader term *Steuerknüppel* | D03 §4.7 |
| **Kuhglocke** | the percussion cowbell (GND 133326514X, variant *Cowbell*) | GND 4165940-5 *Kuhglocke*, variant *Treichel*: the farm object | D03 §4.7 |
| **Becken** | cymbals | pelvis, basin, geological basin, technical vessel — GND ships seven and disambiguates `Becken <Musikinstrument>` | D03 §2.11, §4.7 |
| **Schlagzeug** | the drum kit | loosely, the whole percussion section | D03 §4.7 |
| **Batterie** | the drum kit | in orchestral French, the percussion section | D03 §4.7 |
| **Wirbel** | a roll | the tuning peg of a string instrument | D12 §4.1 |
| **Randschlag** vs **Fellrand** | *Randschlag* = the rim shot, a stroke | *Fellrand* = near the rim, a position | D12 §4.1 |
| **timbre** (FR) | the snare wires; *sans timbre* = snares off; *tambour à timbre* = snare drum | in English, tone colour | D12 §4.1 |
| **timbale** (FR) | the orchestral timpano (MIMO 2887) | *timbale aigüe/grave* = the Latin-American timbales (GM 65/66) | D12 §4.1 |
| **Tambourin** (FR) | tambourine, *tambour de basque* | **tambourin de Provence**, a long two-headed drum with **no jingles** — a separate MIMO concept (2745) | D12 §4.1 |
| **piatto** vs **piatti** (IT) | singular = one cymbal (*piatto sospeso*) | plural = the clashed pair, **a different instrument**. English "cymbal(s)" has the same letters and not the distinction | D12 §4.1 |
| **rullante** (IT) | in **kit** Italian, the snare drum | in **orchestral** Italian, *tamburo rullante / cassa rullante* is a **different, deeper drum** with its own Facchin chapter (p. 758), equated with FR *caisse roulante / caisse sourde*; the kit snare is *cassa chiara* (p. 463) | D12 §4.1 |
| **coperto** (IT, used untranslated in DE and EN scores) | "covered" = a cloth on the head, muffled | frequently misread as "the instrument is covered up / not used" | D12 §4.1 |
| **secco** vs **coperto** | struck then damped immediately | damped *before* the stroke — not the same thing | D12 §4.1 |
| **charleston** (FR, IT) | the hi-hat | in English, a dance and a rhythm; alphaTab's element name for the hi-hat is **`Charley`** | D04 §4; D12 §4.1 |
| **Mühle** (DE) | S11/S12: the *preparatory exercise* for the double-stroke roll | S01 (VSL): a *synonym* for Doppelschlag. **The two sources disagree**; D12 rates S12 more authoritative because it cites Peinkofer/Tannigel | D12 §2.10, §4.1, §6.4 |
| **rullo / tremolo / trillo** (IT) | Facchin's index uses all three for the same act ("Tremolo o rullo" p. 135, "Trillo (rullo)" p. 719) | in English notation, roll, tremolo and trill are three different things | D12 §4.1 |
| **mallet** | a percussion mallet | AAT `mallets (striking tools)` 300024825 is a carpenter's mallet; the percussion sense is `hammers (percussion beaters)` 300042609 | D03 §4.7 |
| **beater** | a drum beater | AAT has three unrelated `beaters`: culinary 300201092, striking tools 300379166, textile 300312126 | D03 §4.7 |
| **hi-hat** (MIMO German) | MIMO 2467 `Choke cymbal`@en has `Hi-hat`@de | MIMO 2489 `Sock cymbal`@en **also** has `Hi-hat`@de. Italian compounds it (*Piatto choke (Hi-hat)*, *Piatto sock (Hi-hat)*), Basque calls 2467 *Splash txindata*, Danish calls both *Bækken*, Spanish calls 2467 *Címbalo*. **"Depending on the language you read, concept 2467 is a choke cymbal, a hi-hat, a splash cymbal, or a cymbal."** | D03 §4.1 |
| **hi-hat vs high-hat cymbals** | MusicXML has both `metal-value`s, differing only in whether the drawing includes the stand | SMuFL likewise `pictHiHat` / `pictHiHatOnStand` | D04 §4 |
| **`pictOpenRimShot`** | the canonical glyph *name* says open | its *description* says "Closed / rim shot". Likewise `pictRightHandSquare` is described "Left hand (Agostini)" and `pictLeftHandCircle` "Right hand" — **name and description swapped in both** | D04 §4 |
| **`pictRim1`** "Rim **or edge** (Weinberg)" | one glyph already conflating two KITWARP sites | — | D04 §4 |
| **111.142** | a Hornbostel-Sachs number | **not a stable identifier**: MIMO's SKOS has 15 = Metal sheets, ACDH-CH has HS-15 = *Stampf-Idiophon* and a sixth top class **Hydrophone**, the 1914 original has neither, the Oct-2017 Addenda add class 17 that MIMO's own SKOS still lacks, Knight renumbers everything (`M11.15` for a djembe), Galpin uses `III,i,A,a,1`. **Must be recorded as `hs-mimo-2011:111.142`, never bare** | D03 §4.2, §4.4 |

### 3.2 Different words, one meaning

| Concept | The words | Locator |
|---|---|---|
| snare drum | `snare drum` = `side drum` = `caixa` (LCMPT UF ring) = H-S 211.212.11 "Side drum" = *kleine Trommel* = *caisse claire* = *cassa chiara* = *tamburo piccolo* = *rullante* (kit IT) = *caja* (ES). **But** MusicBrainz makes `caixa` (deep) and `tarol` (shallow) *separate* instruments where LCMPT makes caixa a UF of snare drum | D03 §4.7, §4.9; D12 §2.1, §2.19 |
| the kit | drum kit = drum set = traps = trap set = trap kit = drumset (LCMPT UF ring) = Schlagzeug = Batterie = Batteria = Drumstel = Trumset = Zestaw perkusyjny; GND adds the score abbreviations *perc*, *Schz*, *Drumset* | D03 §2.4, §2.11, §4.7; D12 §2.1 |
| the side stick | side stick = cross stick = rim click = stick click = *Rimclick* = *baguette sur bord de fût* = *click*. **MuseScore alone has five names for MIDI 37 across two files of one program** | D04 §4, §5.3(1); D12 §2.15, §4.2 |
| the snare drum, military | `military drum` (MusicXML) = `pictSnareDrumMilitary` (SMuFL) = MuseScore `military-drum` trackName "Field Drum", which maps back to `drum.snare-drum` | D04 §4 |
| timpani | timpani = kettledrums = H-S 211.11 "Separate vessel drums" = *Pauke* = *timbale* = *timpano* | D03 §4.9; D12 §2.1 |
| tubular bells | tubular bells = orchestral chimes = chimes = H-S 111.231 | D03 §4.9 |
| wood block | wood block = bangzi = bang zi = clog box = Chinese wood block = tap box = *caja china* (ES) | D03 §4.9; D12 §2.19 |
| finger cymbals | finger cymbals = zils = zilia = jalra (AAT, India) | D03 §4.9 |
| jingle bells | jingle bells = sleigh bells = pellet bells (AAT hierarchy) | D03 §4.9 |
| cabasa | cabaca = shekeré = chekeré = **guiro** = aggüé = agbe (LCMPT UF ring) — **and note that `guiro` there means a *rattle*, not the scraper: a genuine trap** | D03 §4.9 |
| snares off | *mit entspannten Schnarrsaiten* / *Teppich ab* = *sans timbre* = *senza corde* = snares off | D12 §4.2 |
| muffled | *Coperto* / *gedämpft* = *voilé* / *étouffé* = *coperto* = *tapado* = muffled / muted — **eight or more words in four languages** | D12 §4.2 |
| the buzz roll | *Presswirbel* / *Druckwirbel* / *geschlossener Wirbel* = *rullo pressato* / *rullo chiuso* = press roll / closed roll / buzz roll | D12 §4.2 |
| centre / rim | SMuFL encodes **centre as three codepoints** (Weinberg, Ghent, Caltabiano) and **rim as three more**, plus half-open twice. "A glyph enumeration is a *symbol* enumeration; it cannot be used as a concept enumeration without collapsing these" — **the strongest argument in D04 for why pivot terms must not be minted one-per-glyph** | D04 §3.2, §4 |
| the bell of a cymbal | Beckenkuppe = coupole = cupola = bell / dome / cup; and the gong's is **Buckel**, physically a different thing | D12 §2.13, §4.2 |
| concepts with no single English word | *Abschlag* / *rullo con colpo di chiusura*; *Übergangswirbel* / *cambio di note durante un rullo*; *Schlagfleck*; *Klangverfremdung* — D12 §4.2 marks each "(no single term)" in English | D12 §4.2 |
| duplicate concepts inside one authority | MIMO `Drum set` exists twice (5702, 5703, identical in all 13 languages, 5703 nested under 5702) and `Cymbals` twice (2451, 2471). **Wikidata records both members of each pair on the same item.** Five distinct Wikidata items are labelled `triangle`@en, four `cymbal`@en, three `cowbell`, four `tambourine` — "any label-based lookup into Wikidata is wrong by construction" | D03 §2.4, §4.5, §4.6 |

---

## 4. GAPS AGAINST v0.1

### 4.1 Missing — well evidenced (two or more independent traditions)

| Axis | Missing value | Evidence | Locator |
|---|---|---|---|
| technique | **choke** | 4+ traditions; six vendor sources; the only thing in `rules.json` is a *relation* the resolver uses, not a value a source file can state | D04 §5.1; rules.json:581 |
| technique | **bowed** + implement **bow** (name to be chosen against site `bow`) | DE *gestrichen* on suspended cymbal, tam-tam, vibraphone; IT *con l'arco*; ENG SMuFL/MusicXML have the implement | D04 §5.1; D12 §5.1 |
| technique | **shear/slide** (plate against plate) | DE *Breiter Schlag*; IT *Strisciato* | D12 §5.1 |
| technique | **snap** | ES *chasquido*; IT *colpo Snap*; LIB LCMPT `finger snapping` | D12 §5.1; D03 §5.1 |
| technique | **pressed** (single pressed stroke, distinct from the buzz roll) | Sibelius 10 ids; SMuFL `pictCrushStem`; IT *colpo pressato*; DE *Pressschlag* | D04 §5.1; D12 §2.4, §2.10 |
| technique/damping | **chest-damp** | FR 1843 + DE 1911, two pre-MIDI traditions | D12 §5.1 |
| ornament | **single-stroke roll** | DE, IT, ES — three languages name it; v0.1 has none of `roll`/`buzz`/`bounced` meaning specifically this | D12 §5.1 |
| ornament | **four-stroke ruff** (and Italian goes to quintuple) | DE *vierfacher Vorschlag*; IT *quadrupla acciaccatura* in a treatise **and** an official syllabus | D12 §5.1 |
| implement | **fist**, **fingernail** | ENG SMuFL + MusicXML (+ MEI for fingernail); DE *Fingernagel*; IT *unghie*; MARCH (late finding 5). **D04 §5.1 resolves the brief-vs-file discrepancy: axes.json serial 1 is authoritative and has neither, so these are genuine gaps** | D04 §5.1; D12 §5.1 |
| implement | **metal-beater** | DE *Triangelstab* on tam-tam; SMuFL `pictBeaterMetal*` | D12 §5.1; D04 §2.1 |
| implement | **sponge-beater**, **cork-beater** | FR 1843 *baguettes à tête d'éponge*; DE 1911 *Schwamm, Kork* — two traditions, 68 years apart | D12 §5.1 |
| implement | **leather-beater** | DE 1911 and DE VSL today | D12 §5.1 |
| implement | **scraper** (the tool) | DE *Kralle*; MIMO/LCMPT `Scrapers` / *Râcloir* / *raspa* / *rascador*. `technique.scrape` exists with no tool to do it | D12 §5.1 |
| implement | **coin, knitting-needle, spoon-mallet, guiro-scraper, chime-hammer, metal-hammer, triangle-beater, wire-brush, brass-mallets, snare-stick** | MusicXML `beater-value`'s 20; SMuFL's 128; PAS names the class "esoteric beaters" | D04 §5.1 |
| implement | a **material × hardness** decomposition | MusicXML `stick-type` × `stick-material`; DE Kopf/Bezug/Stiel/Form | D04 §5.1; D12 §3.2(d) |
| site | **resonant-head** | ORG (head count as a primary distinction); FR *peau de résonance*; DE *Resonanzfell*; IT *pelle risonante* | D03 §3.3(a); D12 §5.1 |
| position | **sweet-spot** (*Schlagfleck*) and **node** (*colpi sui nodi*) | DE, twice with two measurements; IT | D12 §5.1 |
| mechanism | **rivets / chain / needle** | DE names three distinct sizzle devices; ORG Knight `-s`; IT *piatti chiodati* | D12 §5.1; D03 §5.3(a) |
| mechanism | **wires-slack** (a third state) and **head-slackened** | DE 1911, both in one sentence | D12 §5.1 |
| mechanism | **motor-on / motor-off** | DE *Vibrato / Senza vibrato*, a standard score direction | D12 §5.1 |
| instrument | **hand-cymbals / piatti** and **suspended-cymbal** distinct from `cymbal`/`crash` | ENG, SW ×3, DE, FR, IT | D04 §5.1, §5.3(4); D12 §5.2 |
| instrument | **finger-snap**, **foot-stomp** | LIB LCMPT body-percussion branch; ORG Knight ("the floor is the instrument"); ES | D03 §3.3(d), §5.1 |
| instrument | **gong / tam-tam** distinct | SMuFL `pictTamTam`, `pictGong`, `pictGongWithButton`; MusicXML `gong`, `domed gong`, `tam tam`; 14 `metal.gong.*`; DE/IT/FR | D04 §5.1 |
| voicing | **fusion, rock, concert, brush** | Sibelius id elements + GM-2 kit names | D04 §5.1 |
| dynamic (or a new axis) | **stroke-form / stroke-height** | IT official syllabus (*Full*, *Tap*, *a pistone*, *accademico*); MuseScore *Tap* family | D12 §5.1; D04 §3.14(c) |

### 4.2 Missing — single-source, and must be labelled so

`return` (Guitar Pro only, D04 §5.1); `ping` beyond Sibelius (D04 §5.2 — v0.1's `ping-shot` rests
on one vendor id); `zing`, `suc`, `crunch`, `smash`, `tap`, `bell-tap`, `muted-tap`,
`half-crash`, `full-crash` (D04 §5.1 — corroboration varies from six sources to one, and bucket
08 owns the definitions); `air-lock`, `Kralle`, `Watergong`, `Vibrato` (cymbal pair),
*rullo militare*, *rullo rovesciato*, *al galoppo* (one tradition each, D12 §3.2).

### 4.3 Minted with no source found in these dossiers

Against `vocabulary/axes.json` serial 1:

- `contact` = **butt** — zero attestations (D04 §3.4, §5.2). `shank` has exactly one, and it is
  Italian, not English: *asta/manico delle mazzuole* (D12 §2.17).
- `position` = **halfway**, **offset** — zero (D04 §3.3, §5.2). `perimeter` has DE/IT only.
- `site` = **rim2** — zero as an ordinal; Italian gives it a *semantics* it does not have
  (*cerchio* vs *controcerchio*, and wooden vs metal rim) (D12 §5.2). `underside` — zero.
  `bow` — zero as a site anywhere in three dossiers.
- `openness` = **tight, closed-loose, quarter, three-quarter, loose** — zero; every notation
  source tops out at three steps (D04 §3.7, §5.2).
- `damping` = **towel** (has FR 1843 + DE 1911 provenance, D12 §2.12, §2.16), **gated** — zero.
- `mechanism` = **kick-damped**, **kick-half-open** — zero (D04 §3.9, §5.2).
- `technique` = **gok-shot** — zero; **ping-shot** — one vendor; **sweep, swirl, circling** —
  only as scrape/turn glyphs with a direction, or as DE *Daumenwirbel* / ES *golpe arrastrado*;
  **heel, toe, thumb** — attested in MEI, but as *organ-pedal* terms (D04 §5.2); `thumb` is
  properly attested in DE/IT/ES (D12 §3.1).
- `timbre` = **analog-909, -707, -606, -cr78, fm, pcm, physical, chip, noise** — zero in these
  three dossiers; only `analog-808` appears, as Sibelius `kit-tr-808` (D04 §3.12).
- `voicing` = **lo-fi**, **dark** — zero (D04 §3.13).
- `ornament` = **wash** — zero.
- `instrument` = **stack, xhat, mini-china, mini-hihat, crash-ride, jam-block, aux-pad,
  octoban** — zero in all six authority files; `jam-block` survives only as a MusicXML sound id
  (D03 §0.1, §5.2; D04 §2.3).

**This is not automatically a defect.** D03 §5.2 makes the positive case: `ride`, `china`,
`splash`, `stack`, `xhat`, `mini-china`, `mini-hihat`, `crash-ride`, `jam-block`, `aux-pad`,
`octoban` "and every value on the nine non-instrument axes" — 11 of 27 instrument values and
128 of 155 terms — "describe distinctions that the organological literature has never had a
reason to name". The defect is only where the **name** is wrong or where the axis assignment is.

### 4.4 Misnamed or on the wrong axis

1. **`instrument = sizzle-ride` is a build property wearing an instrument's clothes.** Every
   name for it in every language means "riveted cymbal" (*Piatto chiodato*, *Címbalo ribeteado*,
   *Talerz z nitami*, *cymbales cloutées*); Knight gives it a suffix `-s` explicitly *not* a
   classification change; German names **three** such devices (*Nieten / Kugelkette /
   Stahlnadel*). "A rivet is to a ride what snare wires are to a snare drum, and KITWARP already
   models the latter on `mechanism`." Should be `ride` + `mechanism = rivets-on`.
   *(D03 §5.3(a); D12 §3.2(c), §5.1)*
2. **`bell` is one slug on two axes of one vocabulary** (instrument id 17, site id 8), and it is
   homonymous with a large external class (69 MIMO members, 11 LCMPT children). ADR-0003 forbids
   renaming, so the fix is a `correction` alias, but it must be documented before the percussion
   family is minted and real bells arrive. *(D03 §5.3(b))*
3. **`site = crossstick` and `technique = sidestick` are the same physical act on two axes.**
   Every source treats it as one thing. "Carrying it on both axes will produce two encodings for
   one event." *(D04 §5.3(1))*
4. **`site = bow` will collide with implement `bow`** the moment bowed cymbal is minted — and
   bowing is named in DE, IT and both notation standards. *(D03 §4.8; D04 §5.3(2))*
5. **`site = rim` vs `position = perimeter` are ambiguous against every source.** MusicXML's
   single `rim` covers both; if both v0.1 axes can be set, any notation import is ambiguous.
   *(D04 §5.3(3))*
6. **`instrument = cymbal` is under-specified**: the standards split hand cymbals / suspended
   cymbal / crash-on-a-stand, and in non-English orchestral usage `crash` **is** the pair.
   D12 §5.2: since identifiers are forever, "the orchestral pair needs its own slug from the
   start rather than an overload of `crash`." *(D04 §5.3(4); D12 §5.2)*
7. **`instrument = snare` is one slug where the German orchestral tradition has two** —
   *Militärtrommel / hohe Trommel* against *tiefe (große) Rührtrommel / Tamburo vecchio*,
   distinguished by head tension and shell depth and scored separately by Strauss; VSL still
   keeps `snare-drum` and `field-drum` as two pages. `voicing` cannot carry it because it is an
   instrument difference. *(D12 §5.2)*
8. **`site = underside` is a geometric name for what three traditions name as a head.**
   *(D03 §3.3(a); D12 §5.1)*
9. **`ornament = roll` is unqualified** where German names five roll kinds and Italian at least
   eight. *(D12 §5.2)*
10. **`position` is purely radial** where the German default is a *named point* and the German
    official standard makes position a **function of dynamic**. *(D12 §5.2)*
11. **`instance` ordering.** v0.1's reference axis fixes toms "high to low in pitch". That
    matches the **French** GM convention (basse/médium/aigu × 1–2) and **not** the English GM
    convention (floor/rack × register) — "probably right, but English GM aliases will not map
    one-to-one". *(D12 §5.2)*

### 4.5 What v0.1 gets right, with the source that says so

- **Factoring `site`/`contact` into the pivot term rather than the layout slot.** Organology
  treats striking a different part of the same object as **a change of instrument**: Knight
  p. 18 demands a *dual classification as idiophone* for a drum whose technique regularly
  includes hitting the shell. *(D03 §3.3(e), §5.4)*
- **`instance` on the layout slot, not in the term.** H-S's whole "sets of" branch (111.211 vs
  .212, 111.241.1 vs .2, and the kit itself as 211.212.21) is direct organological support, and
  D03 §3.3(c) says it should be cited in ADR-0001.
- **Splitting implement from limb** — better than Knight's `-1`…`-5`, which fuse them.
  *(D03 §5.5)*
- **`chick` and `foot-splash`** now have primary-source provenance: Weinberg 1994 p. 21 defines
  both, and LilyPond ships `splashhihat`/`hhs`. *(D04 §5.3(5))*
- **The hand-drum stroke family** `dead` / `bass-tone` / `slap` / `open-tone` / `mute-stroke` is
  corroborated **without disagreement** by Finale across nine instruments, MuseScore's Djembe
  and Doumbek, and the Spanish taxonomy one-for-one. *(D04 §5.3(6); D12 §5.3)*
- **`sidestick`, `rimshot`, `stick-shot`, `buzz`, `thumb`, `wires-off`, `superball`,
  `crescendo`/`swell`** all confirmed by non-English primary sources. *(D12 §5.3)*
- **Keying on instrument-and-technique rather than on the kit or the note number.** Sibelius's
  SoundWorld paper reached the same conclusion and wrote it down: *"Each unpitched percussion
  instrument is listed as a separate ID, so SoundWorld needs no concept of drum sets"* and
  *"Because these are not perceived as the same timbre at all, in SoundWorld each drum sound
  must be represented by a different ID."* Dorico independently: a drum kit note **is** "the
  specific combination of instrument and playback playing technique", with the MIDI note and key
  switch as the *address*. Finale independently: two Note Types may share one MIDI number.
  *(D04 §2.9, §2.11, §2.12)*
- **Identifiers are forever.** MIMO is a live proof: the `mimo-db.eu` URI namespace was minted
  in 2010 for a project that ended in 2011, the domain no longer serves HTTPS, and
  `http://www.mimo-db.eu/InstrumentsKeywords/2467` still resolves HTTP 200 sixteen years later.
  *(D03 §0.3)*

### 4.6 A cross-reference recommendation that touches the schema

D03 §0.4 recommends an **optional, outbound, non-authoritative `xref` block** on a pivot term
(namespaces `mimo`, `lcmpt`, `aat`, `wikidata`, `mb`, `gnd`), never part of the pivot id, ids
only and never label text. ~40 of the 155 terms could carry one; ~13 would get a full row today.
Licences: AAT ODC-By 1.0 with a mandatory attribution string; LC public domain; MusicBrainz,
Wikidata and GND CC0; **MIMO states no licence anywhere reachable** → `unknown` → all rights
reserved under ADR-0004. D03 §0.5 rules that storing a bare MIMO integer is not a reproduction
(a number is not a work under §2(2) UrhG; an outbound id transfers no *contents* under the sui
generis right; ~1.5 % of MIMO's 2 724 concepts), with three conditions: ids only, MIMO
registered in `data/sources.json` with `licence_applied: none-stated`, and the ids counted
against MIMO's extraction budget. **One item is escalated to the owner**: ADR-0004 defines
`reference-only` as "may be cited in documentation; never ingested at all", which read literally
forbids an id in `data/`; the proposal is that an outbound cross-reference belongs to the
provenance layer, not the shipped assertion. Also recommended: **record H-S notations as a
reference axis, never a pivot facet**, and always version-pinned (`hs-mimo-2011:111.142`).
*(D03 §0.2–§0.5, §4.2, §4.4)*

---

## 5. STRONGEST CLAIMS

1. **Organology and library authority control describe objects, not events — and no percussion
   parts thesaurus exists to be found.** Six maintained authority files (MIMO 2 724 concepts,
   LCMPT 942, AAT 348+177, Wikidata 877, MusicBrainz 288, GND 908) yield **nine concepts**
   across KITWARP's eleven non-instrument axes: AAT's `drumheads`, `shells`, `snares`, its five
   `percussion beaters`, and LCMPT's `drum machine`. `site` gets 2 of 9, `mechanism` 3 of 4,
   `implement` 7 of 14, and **`position`, `contact`, `technique`, `ornament`, `openness`,
   `damping`, `dynamic`, `voicing` get zero**. Hornbostel and Sachs excluded playing technique
   for membranophones *deliberately* — the suffix mechanism exists and they used it for
   chordophones (verbatim, ZfE xlvi pp. 560–561 = GSJ 14 pp. 11–12; Knight p. 18 restates it in
   English). DOREMUS advertises "instrument playing techniques" and has 20 concepts, all vocal.
   CIMCIM built a brasswind terminology thesaurus and never built the percussion counterpart.
   The Horniman catalogue names shells, hoops and heads **in free prose**, while its structured
   `physical.component` field's only value is `"overall"`. **This closes the question rather
   than leaving it open: KITWARP's ten non-instrument axes have no external anchor and never
   will have one from this literature. It is a structural property of the field, not a gap in
   the research.** *(D03 §0.1, §2.2, §2.6, §2.9–§2.13, §3.2 — "the single most important table
   in the dossier")*
2. **The notation standards are one lineage, not four witnesses, and the newest one is a
   regression.** MusicXML's own XSD says its effect list is "in addition to **Stone's list**";
   SMuFL's percussion pictograms are largely Stone 1980's; MEI has **no percussion vocabulary at
   all** (a grep of the whole ODD returns two incidental hits) and delegates to SMuFL glyph
   names; MNX, MusicXML's successor, has **dropped the pictogram enumerations entirely** and
   models unpitched percussion as `{name: string, midiNumber: int}` — *the exact pivot loss this
   repository documents, now written into a draft W3C specification*. Anyone counting SMuFL +
   MusicXML + MEI as three attestations is counting one book three times.
   *(D04 §2.2, §2.4, §2.5, §6 item 4)*
3. **`choke` is the single clearest gap in the vocabulary.** Six vendor sources plus SMuFL plus
   Weinberg name it; two pre-MIDI traditions independently name the same physical act on hand
   cymbals (Berlioz 1843 "rapprochant de sa poitrine les cymbales"; Haupt & Teuchert 1911 "an
   die Brust gedrückt"); and `choke` exists in this repository only as a *relation* inside one
   `rules.json` expansion, so the resolver can synthesise a choke but no source file can state
   one. The same shape recurs with **Watergong**, **Nota pedal**, **Abschlag** and *rullo con
   colpo di chiusura* — a whole class of events defined by what they do to an event already
   sounding. *(D04 §5.1; D12 §2.16, §3.2(f), §5.1; rules.json:581–587)*
4. **A glyph enumeration is not a concept enumeration.** SMuFL encodes *centre* as three
   codepoints (Weinberg, Ghent, Caltabiano), *rim* as three more, *damp* as four, *half-open* as
   two — and `pictRim1` is captioned "Rim **or edge**", already conflating two KITWARP sites,
   while `pictOpenRimShot` is described "Closed / rim shot" and the two Agostini hand glyphs
   have their names and descriptions swapped. **Pivot terms must never be minted one-per-glyph.**
   *(D04 §3.2, §4)*
5. **The kit's own vocabulary is invisible to every formal authority, and the ride is the proof.**
   No authority file has `ride`, `china`, `splash`, `stack`, `xhat`, `mini-china`, `mini-hihat`,
   `crash-ride`, `jam-block` or `aux-pad`; AAT, LCMPT and MusicBrainz have no `hi-hat` concept at
   all; SMuFL's cymbals range and MusicXML's `metal-value` have **no ride cymbal**; Wikidata's
   `ride cymbal` carries no MIMO, AAT or MB id. H-S explains why: it classifies by the canonical
   playing mode of **1914**, when the orchestral cymbal was a clashed pair, so 111.142 sits under
   "concussion vessels… struck against each other" — and the October 2017 *Addenda & Corrigenda*
   revisits the idiophones, adds a whole new class 17, and **leaves 111.142 untouched**. The kit
   postdates the scheme and is invisible to it. **KITWARP is right to own the whole namespace and
   right not to adopt an authority file as its instrument namespace.**
   *(D03 §0.1, §0.4, §4.3, §5.2; D04 §2.1, §2.2)*
6. **The non-English traditions carry distinctions English has collapsed, and the loss is
   systematic in one direction: rolls, damping, and the beater.** German names five rolls and
   Italian at least eight where v0.1 has `roll`; German names three tambourine rolls **by
   mechanism** (*Schüttel-*, *Daumenspitzen-*, *Schlägel-Wirbel*); three languages name the
   single-stroke roll that v0.1 cannot express; German and Italian decompose the beater into
   four independent parameters (*Kopf / Bezug / Stiel / Form*) plus head size; Berlioz 1843 and
   Haupt & Teuchert 1911 both name sponge-headed timpani beaters that v0.1 has no value for.
   A German official examination standard (ISB Bayern) even states that **the open/closed roll
   distinction is notationally underdetermined and resolved by repertoire provenance**.
   *(D12 §2.5–§2.12, §2.16, §2.17, §3.2, §5.1)*
7. **The register split in German is a hard constraint on aliasing.** German has a precise native
   word for every orchestral instrument (*Kleine Trommel, Große Trommel, Becken, Pauke, Wirbel*)
   and **no native word at all** for ride, crash, china or splash; its word for a kit drumstick
   is *Stick*. German-language MIDI practice does not translate the GM drum map (the German
   Wikipedia article lists it in English verbatim) while French does. **A German alias set must
   be built from two disjoint registers with the boundary at orchestral-battery vs kit; it
   cannot be generated uniformly and must not be machine-translated across that boundary.**
   Related: **MIMO's Spanish labels are museum-register, not musician-register** — *Tambor
   vertical* and *Tambor bajo* where players say *caja* and *bombo*. *(D12 §2.19, §4.3)*
8. **Three programs independently reached this repository's own pivot decision.** Sibelius's
   SoundWorld paper (c. 2007): *"Because these are not perceived as the same timbre at all, in
   SoundWorld each drum sound must be represented by a different ID… there are no SoundWorld
   drum sets."* Dorico: a drum kit note **is** "the specific combination of instrument and
   playback playing technique", with the MIDI note and key switch as its *address* on one
   device. Finale: two Note Types may share one MIDI number within one map. Guitar Pro's sound
   id is a three-part **implement . action . variant** tuple — the closest thing in the whole
   notation layer to KITWARP's factored term. *(D04 §2.7, §2.9, §2.11, §2.12)*
9. **Every one of these standards ships an explicit escape hatch, and that shape is worth an
   ADR.** SMuFL `pictEmptyTrap`; MusicXML `other-percussion` and `smufl-pictogram-glyph-name`;
   Sibelius's primary/secondary id split with the instruction to extend by *adding elements to
   the closest existing id*; Dorico's free-text `xmap.*` map ids. **A closed set plus a
   documented escape hatch is the shape all four converged on.** *(D04 §3.14(j), §2.9, §2.12)*
10. **A bare Hornbostel-Sachs number is not an identifier.** Three maintained digital
    implementations disagree (MIMO's 15 = Metal sheets; ACDH-CH's HS-15 = *Stampf-Idiophon* plus
    a sixth top class Hydrophone; the 1914 original has neither), the 2017 Addenda add a class 17
    that MIMO's own SKOS still lacks nine years later, and Knight renumbers everything. If
    KITWARP records H-S at all it must be `hs-mimo-2011:111.142` — **and even that does not say
    whether the 2017 addenda were applied**. The same lesson applies inside MIMO itself, which
    carries duplicate concepts (`Drum set` 5702/5703, `Cymbals` 2451/2471) that a validator
    cannot choose between. *(D03 §4.2, §4.4, §4.5)*

---

## 6. DISAGREEMENTS

### 6.1 Carried in from the late-findings file, checked against my three dossiers

**(1) `back-stick` — bucket 01 said unattested, bucket 08 made it the best-sourced term in its
bucket.** *My dossiers add a third, independent line of evidence and it supports bucket 08.*
**MuseScore's `marching-snare` instrument enumerates `Backstick` at MIDI 60 with a `ti`
notehead** (D04 §2.8) — and D04 notes this is "the only place in any source in this bucket where
a *closed set of snare techniques* is enumerated as data": Buzz, Battery Snare, Rim Shot, Rim
Click, Stick Click, Stick Shot, Shell, **Backstick**. D04 §3.5 maps it to v0.1 `technique =
back-stick`, and `vocabulary/pivot.json` already carries `snare.back-stick`. The Marrella,
Dowlan and Mirsky evidence (1938 method; USAF 1958; the Armstrong & Co. lithograph of
A. R. Carrington, NYPL PC MUSIC-Dru, Digital ID 832408, and the Utica *New York Observer* review
of 3 July 1878 pushing it back ~150 years) is **not in any of my three dossiers** — I cannot
confirm those locators. **Bucket 01's negative was scope-limited and should be recorded as
"not attested in that bucket's sources", not as a refutation.** D04 §6 states exactly this rule
for itself, having made the same mistake twice: *"a term found in a notation program's data but
not in notation literature is not thereby unverified — it is out of this bucket's scope… Say
'not attested in the notation standards', never 'unverified'."*

**(2) `rim shot` entry into print bracketed 1922–1937 (Bauduc 1937 as a dynamic-accent device;
absent from Bower 1912, Gardner 1918, Straight 1922; Krupa 1938 not on archive.org so the
shaft-between-head-and-rim definition stays UNVERIFIED).** **Not in my dossiers** — none of
D03/D04/D12 reaches Bauduc, Bower, Gardner, Straight or Krupa. But **D12 corroborates the
explanation from the other side**: the non-English traditions borrow the English word for the
rim shot while having rich native vocabulary for muffling. FR *rimshot* is used untranslated
(S08), IT glosses it in English — *colpi a sparo (**rim shots**)* (Facchin p. 471) — and German
has *Randschlag* but VSL's own German page heads the section "Rim shot" (S01). Against that,
"muffled" has *coperto / voilé / étouffé / gedämpft / tapado / secco / timbales voilées ou
couvertes* across four languages and two centuries (D12 §2.3, §2.12, §2.16, §4.2). **The
asymmetry the late finding predicts is visible in D12's data.** D04 adds that the *notation* of
the rim shot was still unsettled in 1994: Weinberg found "five different note heads… defined as
'rimshot' and 12 different note heads specified rimshot variations… 14 additional rimshots and
rimshot variations" — **31 notational procedures for one effect** (D04 §2.10).

**(3) The Peinkofer/Tannigel ↔ Stone lineage.** **Not in my dossiers**, and it matters more here
than anywhere else — see §0 above. D12 §6.2 proposes using the German and English editions as
"a ready-made bilingual concordance"; if Kurt and Else Stone made that translation, the
concordance is not two traditions meeting but one hand writing twice, and the same hand is
upstream of SMuFL and MusicXML (D04 §2.2, §6 item 4). Also flagged: **D12 dates
Peinkofer/Tannigel Schott 1981, the late-findings file says 1976.** Neither is verified here.

**(4) Read splits *Dampened* from *Muffled*; v0.1 does not (contents pp. XVI–XVII, body
pp. 158–233).** **Not in my dossiers.** Gardner Read's *Notation: A Manual of Modern Practice*
appears in both registers as **not reached** (D04 §1 row 21, cited only as Weinberg's authority
for the circled-notehead rimshot; D12 S28, "registered by locator only, never quoted"). What my
dossiers do supply is the surrounding evidence that v0.1's damping axis is under-articulated:
SMuFL has **four** damp glyphs "from four notational traditions, none of which are four
*degrees*" (D04 §3.8, §4); Sibelius separates `mute` (35), `muffled` (11), `pressed` (10) and
`damp` (12) as four distinct id elements (D04 §2.9); Haupt & Teuchert 1911 names three
mechanically distinct damping methods in one sentence (D12 §2.12); and German separates
*Pedaldämpfung* from *Schlägeldämpfung* (D12 §2.11). **v0.1's `damping` = none/muted/damped/
towel/gated is a five-value axis carrying at least three different kinds of distinction.**

**(5) `fist` has a marching source (Casey Claw: "held in a fist, where all the fingers wrap
around the stick"); `fist` and `fingernail` are both in the round-2 brief and both absent from
axes.json.** **Confirmed twice in my dossiers, from two directions.** D12 §5.1 flags the
brief-vs-file discrepancy and defers it ("Discrepancy, not a finding — flagged for the
reconciliation pass"). **D04 §5.1 resolves it**: axes.json at serial 1 holds exactly 14 implement
values, neither is among them, "the round-2 brief listed them because it was written from an
earlier axis sketch rather than from the minted file. **The file is authoritative, so these are
genuine gaps**", with attestation SMuFL `pictBeaterFist` U+E7E5 / `pictBeaterFingernails`
U+E7E6 and MusicXML `beater-value` `fist` / `fingernail`. I verified this against
`vocabulary/axes.json` directly: 14 implement values, no `fist`, no `fingernail`. The Casey Claw
quotation is not in my dossiers; with it, `fist` has ENG + MARCH + (for `fingernail`) DE and IT.

### 6.2 My three dossiers against each other

- **`contact = shank`.** D04 §3.4 states flatly: "`shank` and `butt` have no attestation in this
  bucket at all. SMuFL, MusicXML, MEI, MNX, MuseScore and Weinberg have no concept of which part
  of the stick lands." D12 §2.17/§3.1 attests it in Italian: *"Suoni con l'**asta (manico)**
  delle mazzuole al centro / sul bordo delle barre"* (Facchin p. 262), mapped to `contact =
  shank`. **Both are right about their own literature**; the finding is that the distinction
  exists in Italian treatise prose and nowhere in the notation standards. `butt` remains
  unattested in all three.
- **`position` values.** D04 §3.3 says `halfway`, `offset` and `perimeter` have "no attestation
  anywhere in this bucket". D12 §3.1 maps DE *Fellrand* and IT *sul bordo* to `perimeter`. Not a
  contradiction — a bucket-scope difference — but any count must not read D04's negative as
  global.
- **`site = bow`.** D04 §3.2 says "`bow` appears only as the ride's middle (Guitar Pro
  `stick.hit.mid`)"; D03 §4.8 says that in every organological source `bow` is a violin bow. The
  two are consistent and jointly damning: **the v0.1 site name has no positive attestation in
  either dossier and a strong competing sense in both.**
- **Where the *bell* collision lives.** D03 §5.3(b) frames it as an internal collision between
  v0.1's own two axes plus an external homonym; D04 §4 counts **six** meanings including
  MuseScore's "Ride Bell" as an *instrument name* and "Bell Tap" as plate-to-plate contact. Same
  finding, D04's version is broader.
- **`sizzle-ride`.** D03 §5.3(a) and D12 §3.2(c)/§5.1 reach the same verdict independently
  (organology via Knight's `-s` suffix; German via *Nieten / Kugelkette / Stahlnadel*). **This is
  genuine corroboration across two unrelated traditions** and should not be collapsed to one.
- **MIMO's German `Hi-hat` on two concepts.** D03 §4.1 treats it as a reason never to take
  display names from MIMO. D12 §2.1 nevertheless uses MIMO prefLabels as its five-language
  instrument concordance. D03 §6.1 names the open question: the German museum vocabularies
  (museumsvokabular.de, term.museum-digital.de) were confirmed live but **not extracted**, and
  they are the second independent German label set that would settle whether MIMO's duplicate
  German label is MIMO's own error or a general German-cataloguing convention. **Unresolved.**
- **Whether v0.1's openness axis is too rich or the notation sources too poor.** D04 §3.7 says
  v0.1's eight anchors are "strictly richer than anything in this bucket" and a notation import
  can only ever populate three; D04 §5.2 then lists five of the eight as unsupported. These are
  two readings of one fact, and the reconciliation should keep the first: the axis's source is
  hardware controller data, not notation, and no dossier of mine covers that.

### 6.3 Contradictions with claims I know other dossiers make

- **`zing`.** D04 §3.14(c) originally marked it UNVERIFIED and now records it as **not** a vendor
  coinage: bucket 08 finds it defined in **six institutionally independent non-Tapspace sources**
  (Grand Valley State, Rhythm Armada, Oregon State, PCHS, Missouri State, and a marching-cymbal
  technique site), all giving the same definition — a scrape of one plate's edge along the
  other's bow, **bell outward**. D04 also records that `suc` has four sources, `crunch` two, and
  **only `smash` still rests on a single packet**. Anyone reading an earlier version of D04 will
  see the UNVERIFIED marking; **the corrected reading is the one above, and it is D04's own.**
- **`guz`.** D04 §2.11 and §6 record it as a real shipping Tapspace term whose physical meaning
  no published source gives, confirmed by bucket 08 as a genuine map entry at MIDI 53/54 and
  explicitly **not** a corruption of "Buzz" (the string occurs twice in machine-readable vendor
  HTML in a table where "Buzz" occurs nine times separately). **Record it as attested-and-
  undefined; do not mint it and do not silently normalise it to `buzz`.**
- **Wikidata vs MIMO on cymbal classification.** Wikidata tags crash, ride and splash as H-S
  `111.24` (percussion vessels); MIMO files Crash, Choke, Sizzle and Sock cymbal under `111.142`
  (concussion/vessel clappers). D03 §4.3: "**Both cannot be right.**"
- **LCMPT vs MusicBrainz on *caixa*.** LCMPT makes `caixa` a UF of `snare drum`; MusicBrainz
  makes `caixa` (deep) and `tarol` (shallow) two separate instruments. *(D03 §4.7)*
- **D03 §6.2 and D04 §6 nominate different "most authoritative source not obtained"** — Grove
  2014's "Classification" article (and the Grove Music Online "Drum kit" article, HTTP 403) for
  D03; **Kurt Stone 1980** for D04, "and it matters more than its date suggests" because both
  extracted standards are downstream of a book the bucket could not read; D12 nominates
  **Peinkofer & Tannigel 1981**. Given claim 2 in §5 and the lineage caution in §0, **Stone 1980
  is the one to chase first**: it is upstream of SMuFL and MusicXML, its chapter 10 is the
  percussion chapter, and it may be the same hand as the German handbook. Licence caution from
  D04: the full copies circulating on academia.edu and scribd carry no stated licence, so under
  ADR-0004 they are reference-only — read to check a claim, never transcribe into `data/`.

### 6.4 Reliability warnings my dossiers make about their own rows

- **D12 §6.4**: eight terminology rows come from a **WebFetch summary** of the VSL pages rather
  than verbatim quotation, and one of them (*Mühle* = double stroke) turned out to conflict with
  two Wikipedia sources. **Before any of these is minted as an alias the VSL pages must be
  fetched as raw HTML and the German taken verbatim.**
- **D12 §6.3**: Facchin was reached only as the publisher's extract (TOC + four-language index),
  so its Italian terms have page numbers but almost no verbatim definitions — "the glosses are
  mine unless quoted". The Spanish taxonomy is TOC-only for the same reason (glosses UNVERIFIED).
  Berlioz was read from a bad OCR, so **§2.16's orthography must be confirmed against a clean
  edition before minting**.
- **D04 §6**: Weinberg 1994 was read from page images with no text layer, transcribed by eye —
  the two longest quotes should be re-verified before use as normative evidence. The Guitar Pro
  vocabulary is **derived** (alphaTab's reconstruction, not Arobas Music). Sibelius's counts are
  of *observed* ids, not a published vocabulary. **SMuFL glyph descriptions were treated as
  definitions; they are captions.**
- **D03 §6.3**: the §0.1 coverage matrix was built by regex over label strings — "the very method
  §4.6 warns against". Confidence high for MIMO and LCMPT (searched exhaustively over a complete
  local copy), **medium for AAT** (SPARQL probes only). GND's coverage figure is a sample, marked
  UNVERIFIED, and its hierarchy was never walked. The claim that MIMO is "still maintained" rests
  on one concept created 2019-03-05, seven years ago.
