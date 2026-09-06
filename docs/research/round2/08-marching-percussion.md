# Round 2, bucket 08 — Marching and drum corps percussion

Scope: the vocabulary of marching snare, multi-tenor, marching bass line and marching
cymbal technique, and the authority behind the names MuseScore ships in its four
`Marching_*.drm` drumsets and its `marching-*` instruments.

Observer: worker `bucket-08-marching-percussion`. Dates of access: 2026-09-06 (all web
sources), commit-dated for repository sources. Everything below carries a locator.
Anything not confirmed against a locator is marked **UNVERIFIED**.

**Headline answer to the question this bucket was set.** The names `Gok Shot`,
`Ping Shot`, `Back Stick`, `Suc`, `Ting`, `Crunch (HH)` and `Punch` did not exist anywhere
in MuseScore before commit `c7dc55ea2d` (2024-07-27, Peter Jonas), whose message is
*"Apply Muse Drumline drumset definitions to MDL1 instruments"*. Their proximate authority
is therefore **Muse Drumline**, the Muse Group MuseSounds marching library — not the older
MuseScore Drumline (MDL) extension, and not Tapspace. The older names `Shell`,
`Backstick`, `Battery Snare`, `Buzz`, `Rim Click`, `Stick Click`, `Stick Shot`, `Spock`,
`Full Crash`, `Half Crash`, `Bell Tap`, `Smash`, `Zing`, `Roll` entered in a different
event: commit `f95f3e5459` (2013-07-01, Michael Cowgill), *"instruments.xml update … the
marching percussion group has been added"*. The ultimate authority for both layers is the
Tapspace Virtual Drumline articulation vocabulary plus American drum corps studio slang;
per-name verdicts are in §2.8.

---

## 0. Ruling on `ping-shot`, `gok-shot` and `stick-shot`

v0.1 has minted all three on the `technique` axis with no source recorded, and the
vendor-glossary bucket reports that no cymbal, head or stick manufacturer it reached uses
any of them. Marching pedagogy is where they live. Verdicts:

**`stick-shot` — authority found, keep.** Four independent sources, three of them
citable:

- *Modern Drummer*, "Jazz Drummer's Workshop: The Stick Shot", Steve Fidyk, July 2013:
  "Press one drumstick tip against the head at approximately 30 degrees, while striking
  that stick at the shoulder with the opposite stick."
- SMuFL glyph `pictStickShot`, U+E7F0 — a named notation standard symbol.
- Tapspace *Virtual Drumline 2.5 User Guide* v.2.5.6, keymaps pp. 24–28: `Stick Shot` on
  every SnareLine instrument, and `Stick shot HIGH` / `Stick shot LOW` on the two solo snare
  instruments.
- Wikipedia *Rimshot*, wikitext line 20, §orchestral: the orchestral rimshot "is also known
  as a 'stick shot'".

Note the register split: the stick shot is a *jazz and orchestral* term that marching
percussion also uses. Blakley's glossary records the collision — his second sense of
"cross stick" is the stick shot.

**`ping-shot` — authority found, keep.** Four sources, one of them a vendor's own
articulation name:

- Tapspace *VDL 2.5 User Guide*, pp. 24, 25, 26, 27, 28: `Ping Shot` is a literal, shipped
  articulation name on five separate marching snare instruments. This is the strongest
  evidence in the bucket for any snare stroke name.
- Southern Utah University Drumline 2025 Exercise Packet: "Ping Shot" written as a
  performance direction above the snare stave (rehearsal figure 23), contrasted with
  "Full Shot" two figures later.
- Wikipedia *Rimshot*, line 15: "the 'ping shot', where the bead is struck about one inch
  (2.5 cm) from the rim. This produces a high-pitched sound."
- icanplaydrums.com, Jack Bennett, 2025-01-13: "Ping Rimshot: achieved by hitting closer to
  the rim, producing a higher-pitched, metallic sound."

**`gok-shot` — no authority for the name. Reconsider it.** Stated plainly, because that is
the finding:

- The spelling **`Gok`** occurs in exactly one place: MuseScore's
  `share/templates/Marching_Snare_Drums.drm`, pitch 52, added 2024-07-27 in commit
  `c7dc55ea2d` from Muse Drumline's definitions. `git log -S "Gok"` over the whole MuseScore
  repository returns that one commit.
- Tapspace's 112-page *Virtual Drumline 2.5 User Guide* — the industry-standard marching
  library, and the vendor behind the earlier MuseScore Drumline extension — **never uses
  the word, in any spelling**. It ships `Ping Shot` but no gock.
- None of the five marching technique packets, two technique manuals or the notated
  exercise packets reached uses it.
- No association standard reached uses it (PAS is paywalled; see §6).
- The only definition of the *concept* found anywhere is Wikipedia *Rimshot* line 16 — "a
  'gock' (also spelled *gawk*), which is produced by hitting the bead of the drum stick at
  the center of the drum while the rim is percussed with the distal shaft of the stick
  (near the hand). This makes a lower sound." **That paragraph carries no citation.** Every
  other statement of the three rimshot types reached in this bucket is a paraphrase of it.
- Where "gock" *does* appear in sourced reference works, it means something else entirely:
  the small 6″ or 8″ accent drum on a multi-tenor rack (Wikipedia *Marching percussion*
  line 64, citing Udow; Blakley's glossary, s.v. Gock, "also called a spock or shot drum").

The *physical distinction* is real and worth a term — a rimshot with the bead at the centre
of the head is audibly lower than one an inch from the rim, and MuseScore, Muse Drumline
and the model all need to express it. What has no authority is the **name**. Three options,
none of which a worker may take unilaterally under ADR 0003:

1. Keep `gok-shot` as the immutable slug and add a `correction` alias `gock-shot`, with
   `gawk-shot` as a second alias. Cheapest, preserves the id, and matches the way the term
   is actually spelled in the one tertiary source that defines it.
2. Retire the name and express the sound compositionally as `rimshot` + `position=centre`,
   which is what the definition literally says and what §5.1 recommends anyway for all
   three rimshot variants.
3. Leave it and record the provenance as "Muse Drumline, single vendor, uncorroborated".

Recommendation to the owner: option 1 plus the §5.1 rule, so the slug survives, the field
spelling resolves, and the ping/normal/gock family is recorded as one technique at three
positions rather than three techniques. **Do not present `gok-shot` as an established
marching term; it is one vendor's spelling of a word whose only definition is uncited.**

---

## 1. Candidate source register (round A)

Authority levels used: **P** primary (the body that owns the term, or the artefact itself),
**V** vendor primary (the manufacturer's or publisher's own document), **T** teaching
primary (a program's own technique packet — written by the people who use the words),
**S** secondary/aggregation, **X** tertiary.

| # | Title | Author / body | Year | Type | Locator | Auth | Reached |
|---|---|---|---|---|---|---|---|
| 1 | `share/templates/Marching_Snare_Drums.drm` | MuseScore Ltd | 2024 | shipped data file | musescore/MuseScore, blob at `6a454cd835` | P | yes |
| 2 | `share/templates/Marching_Tenors.drm` | MuseScore Ltd | 2024 | shipped data file | same repo | P | yes |
| 3 | `share/templates/Marching_Bass_Drums.drm` | MuseScore Ltd | 2024 | shipped data file | same repo | P | yes |
| 4 | `share/templates/Marching_Cymbals.drm` | MuseScore Ltd | 2024 | shipped data file | same repo | P | yes |
| 5 | `share/instruments/instruments.xml`, `<InstrumentGroup id="marching-percussion">` | MuseScore | 2013→ | shipped data file | lines 11292–11976 of the file at `6a454cd835` | P | yes |
| 6 | Commit `f95f3e5459` "instruments.xml update" | Michael Cowgill | 2013-07-01 | VCS record | musescore/MuseScore | P | yes |
| 7 | Commit `5f8cac1369` "add new tenor and bass marching drum mapping. See #196321" | lasconic (Nicolas Froment) | 2017-06-23 | VCS record | same | P | yes |
| 8 | Commit `c7dc55ea2d` "Apply Muse Drumline drumset definitions to MDL1 instruments" | Peter Jonas (shoogle) | 2024-07-27 | VCS record | same | P | yes |
| 9 | Commit `0ce0df221b` "Use General MIDI Percussion as the standard drumset" | Peter Jonas | 2025-01-28 | VCS record | same | P | yes |
| 10 | `src/project/internal/mdlmigrator.cpp` | MuseScore Ltd | 2024 | source code | same repo | P | yes |
| 11 | `share/sound/MS Basic_Readme.md`, "MuseScore Marching Percussion" section | MuseScore Ltd | — | vendor doc | same repo | V | yes |
| 12 | **Virtual Drumline 2.5 User Guide v.2.5.6**, 112 pp | Tapspace Technologies | 2026 rev | vendor manual | `https://tapspace.com/wp-content/uploads/2026/06/VDL-2.5-User-Guide-v.2.5.6.pdf` | V | yes |
| 13 | "Percussion MIDI Maps: Tapspace Virtual Drumline" (VDLite maps) | MakeMusic / Finale | ~2012 | vendor manual | `https://usermanuals.finalemusic.com/Finale2012Win/Content/Finale/PercussionMaps3.htm` and the FinaleMac twin | V | yes |
| 14 | "TapSpace Instruments & Percussion Maps" (VDL-for-Garritan maps) | MakeMusic, mirrored by Portland State Univ. | ~2009 | vendor manual | `https://web.pdx.edu/~jnewton/assignments/043ft_finale_tutorials/finale_tutorials/Finale/TapSpace_Instruments.htm` | V | yes |
| 15 | Tapspace VDL 2.5 product page | Tapspace | 2026 | vendor page | `https://tapspace.com/product/virtual-drumline-2-5/` | V | yes |
| 16 | Wikipedia, **Rimshot**, §"In marching percussion" | — | rev. 2026 | tertiary | `https://en.wikipedia.org/wiki/Rimshot` (raw wikitext lines 13–18) | X | yes |
| 17 | Wikipedia, **Marching percussion** | — | rev. 2026 | tertiary | `https://en.wikipedia.org/wiki/Marching_percussion` (raw wikitext lines 52, 64, 79, 85, 92, 96) | X | yes |
| 18 | Wikipedia, **Backsticking** | — | rev. 2026 | tertiary | `https://en.wikipedia.org/wiki/Backsticking` | X | yes |
| 19 | **Cymbal Technique Packet 2020** | Rhythm Armada (WGI independent) | 2020 | teaching packet | `https://armadacorps.org/wp-content/uploads/2020/10/Rhtyhm-Armada-Cymbal-Packet.pdf`, "Glossary of Sounds" p. 9, "Sound Effects" pp. 14–16 | T | yes |
| 20 | **Cymbal Technique** | Linden Waling, Grand Valley State University | n.d. | teaching packet | `https://www.gvsu.edu/cms5/asset/24356562-…/gvsu_cymbal_packet.pdf`, pp. 5–13 | T | yes |
| 21 | **Marching Cymbals Technique Packet** | Oregon State University Drumline | 2020 | teaching packet | `https://static1.squarespace.com/static/5f16620b3658156511e40b2f/t/5f1b487855b1856053673f07/1595623568034/Oregon-State-Drumline-Cymbal-Technique-Packet.pdf` | T | yes |
| 22 | **Marching Percussion Information and Technique Manual** FA20 | Missouri State University ("Pride of MSU") | 2020 | teaching manual | `https://www.missouristate.edu/Band/_Files/FA20TechManual.pdf`, "Playing Zones", "Cross Overs", "Skanks (Muffled Shots)", "Bass Line Technique" | T | yes |
| 23 | **Marching Percussion Handbook** | PCHS "Sound of Silver" Drumline | n.d. | teaching packet | `https://www.soundofsilver.net/uploads/1/6/9/9/16997372/pchs_drum_line_handbook.pdf`, cymbal glossary pp. 12–13 | T | yes |
| 24 | **SUU Drumline 2025 Exercise Packet** | Kevin Johnson / Southern Utah University | 2025 | teaching packet + notated exercises | `https://www.suu.edu/pva/music/marching-band/pdf/drumline-packet.pdf`; "Ping Shot" and "Full Shot" as written performance directions; "Unisons"/"splits" p. 8 | T | yes |
| 25 | **Marching Tenor Technique Guide and Exercise Packet** | EPCHS Bands | 2011 | teaching packet | `http://www.epchsbands.org/wp-content/audio/2011/03/Marching-Tenor-Guide.pdf` | T | yes |
| 26 | **Marching Bass Drum Technique Guide and Exercise Packet** | EPCHS Bands | 2011 | teaching packet | `http://www.epchsbands.org/wp-content/audio/2011/03/Marching-Bass-Drum-Guide.pdf` | T | yes |
| 27 | **Marching Cymbals** blog | (anonymous cymbal instructor) | n.d. | teaching notes | `https://marchingcymbalstechnique.blogspot.com/` | T | yes |
| 28 | **Percussion Glossary** | Patrick Blakley | 2026 (living doc) | glossary | `https://www.patrickblakley.com/percussion-glossary/` | S | yes |
| 29 | "How to Play Marching Tenor Drums, part 5 of 7: Sweeps & Scrapes" | Rudimental University Press | 2018-03-29 | pedagogy article | `https://www.rudimentaluniversity.com/2018/03/29/how-to-play-marching-tenor-drums-part-5-of-7/` | T | yes |
| 30 | MuseScore Studio Handbook, "Other percussion notation" | MuseScore | 2026 | vendor doc | `https://handbook.musescore.org/idiomatic-notation/percussion/other-percussion-notation` | V | yes — **negative result**, documents no marching names |
| 31 | "Terms Used in Percussion", *Percussive Notes* Jan 1986 | Percussive Arts Society | 1986 | association publication | `https://pas.org/publication-articles/terms-used-in-percussion-january-1986/` | P | **no — member paywall** |
| 32 | "Notation for Percussion Instruments" | Percussive Arts Society | n.d. | association standard | `https://pas.org/publication-articles/notation-for-percussion-instruments/` | P | **no — member paywall** |
| 33 | *Percussion Pedagogy*, p. 363 | Michael Udow, Oxford Univ. Press | 2019 | scholarly book | ISBN 9780190902971; Google Books id `t5ugDwAAQBAJ` | P | **no — no preview of p. 363** |
| 34 | *The Complete Marching Band Resource Manual*, ch. 8, p. 132 | Wayne Bailey & Thomas Caneva, Univ. of Pennsylvania Press | 2003 | scholarly book | ISBN 9780812218565; Google Books id `H_v81GgtO1QC` | P | **no** |
| 35 | snarescience.com forum, threads `t=589` ("gock") and `f=6&t=62` ("Drum Terminology") | drum corps community | 2000s | forum | `http://www.snarescience.com/forums/viewtopic.php?t=589` | S | **no — server returns HTTP 500; web.archive.org blocked from this environment** |
| 36 | WGI Percussion Score Sheets / Adjudication Manual 2026 | Winter Guard International | 2026 | association rulebook | `https://www.wgi.org/percussion/percussion-score-sheets/` | P | **no — not fetched, and adjudication captions do not name strokes (see §6)** |
| 37 | PAS International Drum Rudiments (PAS 40) | Percussive Arts Society | 1984 | association standard | `https://pas.org/rudiments/` | P | not needed here — owned by bucket 01 |
| 38 | *The Drummers' and Fifers' Guide* | George B. Bruce & Dan D. Emmett | 1862 | pre-MIDI treatise | IMSLP, "The Drummer's & Fifer's Guide (Emmett, Daniel Decatur)" | P | **no — not fetched; see §6** |
| 39 | German-language marching drum literature | — | — | — | searched (`Marschtrommel Spieltechnik`, `Spielanweisungen Trommelkorps`); de.wikipedia `Kleine Trommel`, `Schlagzeugspiel`; bandsnap.org | S | **negative result: no German equivalents for gock/ping/backstick exist** |
| 40 | French-language *batterie-fanfare* literature | — | — | — | searched (`caisse claire technique de jeu`, `coup de baguette`); batteriefanfare.com, marcdedouvan.com | S | **negative result, same** |
| 41 | musescore.org node 109826, "Add 2nd spock drum to Marching Percussion Tenor instrument" | MuseScore community | 2017 | issue thread | `https://musescore.org/en/node/109826` | P | **no — Cloudflare 403 to both WebFetch and curl** |
| 42 | musescore.org/en/mdl, MuseScore Drumline landing | MuseScore | 2018 | vendor page | `https://musescore.org/en/mdl` | V | **no — same Cloudflare block** |
| 43 | "Jazz Drummer's Workshop: The Stick Shot" | Steve Fidyk, *Modern Drummer*, July 2013 | 2013 | trade periodical | `https://www.moderndrummer.com/2013/06/jazz-drummers-workshop-the-stick-shot/` | P | yes |
| 44 | "The Art of Mastering a Snare Drum Rimshot" | Jack Bennett, icanplaydrums.com | 2025-01-13 | pedagogy article | `https://www.icanplaydrums.com/blog/the-art-of-mastering-a-rimshot` | S | yes — names Full / Side / **Ping** rimshot |
| 45 | Drum Glossary, 250+ terms | drumming.com | 2026 | glossary | `https://www.drumming.com/drum-glossary` | S | yes — **negative result**: no entry for gock, gawk, ping shot, stick shot or backstick |
| 46 | archive.org full-text/metadata search for `"gock" AND "rimshot"` | Internet Archive | — | search API | `https://archive.org/advancedsearch.php?q=%22gock%22+AND+%22rimshot%22&output=json` | — | yes — **0 hits** |
| 47 | Google Books API, `q="gock shot"` and `q="gock" marching snare` | Google | — | search API | `https://www.googleapis.com/books/v1/volumes` | — | **no — HTTP 429, daily project quota exhausted** |
| 48 | **Marching Fundamentals**, percussion section | The Ohio State University Marching Band (TBDBITL) | 2019 rev. | teaching manual | `https://tbdbitl.osu.edu/sites/tbdbitl.osu.edu/files/fundamentals-percussion.pdf`, §D "Instrument Playing Position" | T | yes — names five cymbal **positions** (Traditional, Vertical A/V, Traditional hi-hat, **Gumption**, **Punch**) and no effect sounds |
| 49 | Marching Cymbals 101 | Corey Pearce | n.d. | course outline | `https://coreypearce.com/marching-cymbals-101` | T | yes — **negative result**: a lesson index naming grips, positions and flips (Garfield Grip, Pistol Grip, Port, Set, Carry, Wrist Rolls, Sones Flips) with no sound definitions at all |
| 50 | *Basic Snare Drum Technique*, 13 pp | Thom Hannum, published free by Pearl | 2019 | pedagogy primer | `https://pearldrum.com/sites/default/files/2019-10/basic-snare-drum-technique.pdf` | P | yes — **negative result**, see §2.5.1 |
| 51 | "Backsticking — A Drumming Technique Institutionalized by John Dowlan" | Ellis Mirsky, *Field Drums* | 2008-12-28 | research blog quoting two primary sources | `http://www.fielddrums.com/2008/12/backsticking-drumming-technique.html` | S→P | yes |
| 52 | "Was Carrington Backsticking in the 1870s? YES!" | Ellis Mirsky, *Field Drums* | 2009-01-03 | ditto | `http://www.fielddrums.com/2009/01/was-carrington-back-sticking-in-1870.html` | S→P | yes |
| 53 | "The Baron of Backsticking" | Joe Marrella, *Drum Corps World* Vol. 36 No. 15 | 2007-12 | trade periodical | quoted verbatim in sources 51 and 52 | P | via quotation |
| 54 | Official biography of John Dowlan | World Drum Corps Hall of Fame | n.d. | association record | quoted verbatim in source 51 | P | via quotation |
| 55 | Lithograph, "A.R. Carrington, champion drum soloist, 1870s" | Armstrong & Co., Boston | 187‑ | image, primary artefact | New York Public Library, Mid-Manhattan Picture Collection, call no. `PC MUSIC-Dru`, Digital ID 832408, Record ID 1062097 | P | described in source 52, image not viewed |
| 56 | *Utica New York Observer*, 1878-07-03, review of A.R. Carrington | — | 1878 | newspaper | quoted verbatim in source 52 | P | via quotation |
| 57 | *New York Clipper*, 1879-07-19, p. 185 col. 5, Carrington advertisement | — | 1879 | newspaper | cited in source 52 | P | not viewed |
| 58 | Wikipedia, **Casey Claw** | — | rev. 2026 | tertiary | `https://en.wikipedia.org/wiki/Casey_Claw` | X | yes |
| 59 | "Percussion MIDI Maps: Tapspace Virtual Drumline", Finale 2014 Mac edition | MakeMusic / Finale | ~2014 | vendor manual | `https://usermanuals.finalemusic.com/Finale2014Mac/Content/Finale/PercussionMaps3.htm` | V | yes — third Finale edition carrying `Snare Guz Short` (53) / `Snare Guz Long` (54) |

Searches run in round A (18, all distinct): `"gock" marching snare rimshot`; `PAS marching
percussion terminology standard glossary`; `MuseScore Drumline MDL Tapspace`; `"spock
drums" tenor quad origin`; `Tapspace VDL articulation list ping gock backstick`; `DCI WGI
adjudication technique vocabulary`; `marching cymbal crash hi-hat choke zing sizzle suc
glossary`; `marching bass drum numbering 1 to 5 split unison packet`; `"back stick"
backsticking marching snare`; `marching tenor sweep crossover scrape shot`; `"stick shot"
snare definition stick-on-stick`; German `Marschtrommel Spieltechnik Rimshot Stockschlag`;
French `batterie-fanfare caisse claire coup de baguette`; `Percussive Notes marching snare
rimshot types ping gock`; `snarescience glossary rim click cross stick shell`; `Bruce
Emmett Drummers' and Fifers' Guide 1862`; `PAS standardized marching notation 1980s`;
`MuseScore Drumline handbook Gock Ping Backstick Shell`.

---

## 2. Extracted terminology (round B)

### 2.1 MuseScore `Marching_*.drm` — verbatim, all 55 entries

Extracted by parsing the four files at commit `6a454cd835`. Columns: MIDI pitch, `<name>`
verbatim, `<line>` (staff line, negative = above the top line), `<head>`, and the SMuFL
glyph from `<noteheads><quarter>` where present.

`Marching_Snare_Drums.drm` — 9 entries:

| pitch | name | line | head | SMuFL quarter glyph |
|---|---|---|---|---|
| 49 | `Ping Shot` | 1 | normal | `noteheadRoundWhiteWithDot` |
| 50 | `Hit` | 1 | normal | — |
| 51 | `Rim Shot` | 1 | normal | `noteheadXOrnate` |
| 52 | `Gok Shot` | 1 | normal | `noteheadCircleX` |
| 53 | `Rim` | 0 | cross | — |
| 55 | `Stick click` | −1 | plus | — |
| 56 | `Cross Stick` | 1 | slashed1 | — |
| 57 | `Stick Shot` | 1 | slashed2 | — |
| 60 | `Back Stick` | 1 | normal | `noteheadTriangleRoundDownBlack` |

`Marching_Tenors.drm` — **20** entries (round 1 recorded 22; that is wrong):
`Drum 1..4` and `Spock 1..2` each × {plain, `Rim`, `Shot`}, **plus `Drum 3 Shell` (52) and
`Drum 4 Shell` (40) only**. Pitches: Drum 4 36/37/41, Drum 3 48/49/53, Drum 2 60/61/65,
Drum 1 72/73/77, Spock 2 84/85/89, Spock 1 96/97/101. `Shot` carries `noteheadXOrnate`;
`Rim` uses head `cross`; `Shell` uses head `xcircle`. **`Spock 1` sits above `Spock 2`
(line −2 vs −1).**

`Marching_Bass_Drums.drm` — 18 entries: `Drum 1..5` × {`Hits`, `Rims`, `Rimshots`} plus
`Unison Hits` (90, head `slash`), `Unison Rimshots` (91, `noteheadXOrnate`),
`Unison Rims` (92, `noteheadSlashX`). Drum 1 is the highest staff line (line 1), Drum 5 the
lowest (line 9).

`Marching_Cymbals.drm` — 8 entries: 72 `Crash`, 76 `Crunch (HH)` (head `cross`),
77 `Sizzle` (head `diamond`), 79 `Punch` (`noteheadXOrnate`), 81 `Tap` (head
`triangle-up`), 84 `Ting` (`noteheadTriangleRoundDownBlack`), 89 `Suc` (head `plus`),
91 `Zing` (head `slashed1`).

### 2.2 MuseScore `instruments.xml` marching group — verbatim, all 65 entries

Five instruments, not four. Round 1 missed `marching-show-tenors`.

- `marching-snare` (11, bank 128 / program 56 "Marching Snare"): 48 `Buzz`, 50 `Battery
  Snare`, 52 `Rim Shot`, 53 `Rim Click`, 55 `Stick Click`, 57 `Stick Shot`, 59 `Shell`,
  60 `Backstick`, 72 `Ride Cymbal 1`, 74 `Open Hi-Hat`, 76 `Closed Hi-Hat`.
- `marching-tenor-drums` (25, program 96 "Marching Tenor"): Drum 4 36/37/38/39/40
  (plain/`Rim`/`Buzz`/`Muted`/`Shell`), Drum 3 48–52 likewise, Drum 2 60/61/62/63,
  Drum 1 72/73/74/75, `Spock 1` 84/85/86, `Spock 2` 96/97/98, 43 `Stick Click`.
  **`Spock 2` is the higher drum here (line −2) — the opposite of the `.drm`.**
- `marching-show-tenors` (1, program 0): 50 `Hit`. Track name "Show-Style Tenors".
- `marching-bass-drums` (11, program 59 "Marching Bass"): `Drum 1..5` × {plain, `Rim`}
  at 85/87, 73/75, 61/63, 49/51, 37/39, plus 90 `Unison`.
- `marching-cymbals` (13, program 58 "Marching Cymbals"): 72 `Full Crash`, 74 `Half
  Crash`, 76 `Hi-Hat`, 77 `Sizzle`, 79 `Crash-Choke`, 81 `Tap`, 83 `Tap-Choke`, 84 `Bell
  Tap`, 86 `Bell Tap-Choke`, 88 `Muted Tap`, 89 `Smash`, 91 `Zing`, 93 `Roll`.

Preset numbers are documented in `share/sound/MS Basic_Readme.md`, §"MuseScore Marching
Percussion": bank 128 presets 56 Marching Snare, 57 OldMarchingBass, 58 Marching Cymbals,
59 Marching Bass, 95 OldMarchingTenor, 96 Marching Tenor, with the note *"These presets are
used for marching percussion support in MuseScore and do not conform to GM layout."*

### 2.3 Provenance chain inside MuseScore

| event | commit | date | author | what it introduced |
|---|---|---|---|---|
| marching group created | `f95f3e5459` | 2013-07-01 | Michael Cowgill | `Battery Snare`, `Buzz`, `Rim Shot`, `Rim Click`, `Stick Click`, `Stick Shot`, `Shell`, **`Visual (BS,X-Over,Etc)`** at pitch 60, `Spock`, `Drum3/4 Shell`, `Bass Drum n Rim Knock`, `Full Crash`, `Half Crash`, `High Hat`, `Sizzle`, `Crash-Choke`, `Normal Tap`, `Normal Tap-Choke`, `Bell Tap`, `Bell Tap-Choke`, `Muted Tap`, `Smash`, `Zing`, `Roll` |
| tenor/bass remap | `5f8cac1369` | 2017-06-23 | lasconic | splits `Spock` into `Spock 1` (84) and `Spock 2` (96); renumbers tenors to 36/48/60/72/84/96 and basses to 37/49/61/73/85; adds `sticks` at 43 |
| MDL1 migration | `c7dc55ea2d` | 2024-07-27 | Peter Jonas | adds the four `.drm` files carrying `Ping Shot`, `Gok Shot`, `Back Stick`, `Hit`, `Crunch (HH)`, `Punch`, `Ting`, `Suc`, `Unison Rims/Rimshots`, `Drum n Shot` |
| GM standardisation | `0ce0df221b` | 2025-01-28 | Peter Jonas | renames pitch 60 from `Visual (BS,X-Over,Etc)` to `Backstick` |

`git log -S "Ping Shot"` over the whole repository returns exactly one commit,
`c7dc55ea2d`. Same for `Gok`. Both strings are absent from MuseScore before 2024-07-27.

`src/project/internal/mdlmigrator.cpp` shows what the `.drm` files replace: MDL1 instrument
ids `mdl-snareline`, `mdl-snareline-a`, `mdl-snaresolo`, `mdl-snaresolo-a`,
`mdl-tenorline`, `mdl-tenorsolo`, `mdl-bassline-5`, `mdl-bassline-10`, `mdl-cymballine`,
each with a hard-coded `repitch` table. MDL1's own drumset definitions are **not** in the
repository (they shipped with the non-GPL MDL extension), so the MDL1 *names* remain
unrecoverable from this source; only the pitch mapping survives. Note the naming trap:
**MuseScore Drumline (MDL, 2018 extension, Tapspace-built)** and **Muse Drumline
(MuseSounds library, 2024, Muse Group)** are two different products.

### 2.4 Tapspace Virtual Drumline 2.5 — vendor articulation vocabulary

Locator throughout: *Virtual Drumline 2.5 User Guide v.2.5.6*, "Keymaps" chapter.

**SnareLine (AutoRL), p. 24; SnareLine Manual / Manual LITE, p. 25; SnareLine VDL1, p. 26**

`MAIN HITS` · `RIM SHOTS` · `Ping Shot` · `RIMS` · `Over the head double shots` ·
`Cross stick Rim Knock` · `Stick Shot` (and, on the solo instruments, `Stick shot HIGH` /
`Stick shot LOW`) · `Backsticks` (`RH backstick`, `LH backstick`) · `Dreads` · `Rods` ·
`FAT crush` / `DRY crush` · `FP buzz roll` · `Buzz Roll SUSTAINED` ·
`Crescendo SHORT/MEDIUM/LONG` · `Decrescendo SHORT/MEDIUM/LONG` · `Throwoff OFF` /
`Throwoff ON` · `Snares OFF` / `Snares ON` · `Solo SHOTS` / `Solo HITS` ·
`Hi Hat LOOSE` / `Hi Hat MEDIUM` / `Hi Hat TIGHT` · `Ride cym` · `Bell of ride cym` ·
`Crash` · `HH press roll` · `Ride cym roll` · `Dress center harness hit` · `Stick click` ·
**`Snare shell`** · `Sticks-in` · `Vocal "dut" 1/2` · `Metronome accent` / `Metronome click`.

**Solo Kevlar Snare, p. 27** adds: `Twisting motion rim roll` · `Rim buzz roll` ·
`Stick on stick rebound doubles` · `RH/LH edge rebound` (p. 28) · `RH felt` / `LH felt` ·
`RH Butt (vertical)` / `LH Butt (vertical)` · `Friction Slide 1` / `Friction Slide 2` ·
**`RH on cage` / `LH on cage`** · `Stick snap` · `FP sustained rolls`.

The same page carries a mod-wheel legend that is a striking-position scale in vendor words:

> `***STICK PLACEMENT` — `• 00-43 = center of head` `• 44-89 = halfway to edge`
> `• 90-127 = edge of head`

**TenorLine (AutoRL), p. 30; TenorLine Manual/LITE, p. 31; Tenor Solo Manual, p. 29**

`Drum 1..4 hits` · `Spock 1 hits` / `Spock 2 hits` · `Drum n shots/rims` ·
`Spock n shots/rims` · `dreads/rods` · `Rods on rim` / `ROD on RIM` · `WET crush` /
`DRY crush` · `Roll … crescendo` / `diminuendo` / `sustained buzz` · **`"Skank"`** ·
`Hand muffle on drum 4` · `Muffled drum 4 taps` · `Drum n STIR w/dread` ·
**`Double-stop on lower shells`** · `Aluminum mallet clicks` · `Tenor Stand click` ·
`High/Low Jam Block` · `Cowbell` · `Hand claps` · `Vocal "duts"` ·
`Drum n "snenor"` / `Spock "snenor"` · keyswitches `reg mallets` / `puffy mallets`.

**BassLine (AutoRL), p. 33; BassLine 10-Drums, pp. 34–35; BassLine Manual, p. 36**

`Drum 1..6 hits` · `Drum n rims/rods/dreads` · `Drum n CRUSH` · `Drum n sustained roll` ·
`UNISON HITS` · `UNISON RIMS` · `UNISON CRUSH` · `UNISON sustained roll` ·
`Unison stick click` · `Unison sticks-in` · mallet keyswitch `reg` / `puffy`.
The 10-drum variant exists because a bass line can exceed five players.

**CymbalLine 16in/18in/20in/All, p. 38**

`Port Crash` · `Orchestral Crash` · `Flat Crash` · `Crash Choke Fat` · `Crash Choke Secco` ·
`Vacuum Suck` · `Sizzle` · `Sizz/Suck` (A and B) · `Tap Choke` · `Tap Halfway` ·
`Tap Edge` · `Ding` · `Click` · `Crunch Choke` · `Hi Hat Choke` · `Slow Zing` /
`Fast Zing` · `Scratch In` / `Scratch Out` · `Flat Roll` · `Circular Roll` · `Tremolo` ·
`Whale Call`. Mod-wheel selects `20"` / `18"` / `16"` plates; the keymap has an upper
"unison cymbal section" octave range and a lower "solo cymbal player" range.

**Critical negative result: the strings `gock`, `gok` and `gawk` do not occur anywhere in
the 112-page VDL 2.5 user guide.** VDL has `Ping Shot`; it has no gock.

Older Tapspace maps corroborate the drum-numbering direction. In "VDL for Garritan
Tenorline" (source 14), `Spock 2 hits` sit at MIDI 73/74 and `Spock 1 hits` at 75/76 —
**Spock 1 is the higher drum**. `Drum 1` sits at 71/72 and `Drum 4` at 65/66 — **Drum 1 is
the highest of the four**. In "VDL for Garritan Bassline", `Drum 1` is at 75/76 and
`Drum 6` at 65/66 — **bass drum 1 is the highest/smallest**. The Finale "VDLite Finale
Marching Percussion" combined map (source 13) also contains `Snare Guz Short` (53) and
`Snare Guz Long` (54) — see §2.4.1.

### 2.4.1 `guz` — a shipping term with no published definition anywhere reachable

Recorded as a bounded negative rather than a guess, because that is a citable state.

**Where it exists.** `Snare Guz Short` at MIDI 53 and `Snare Guz Long` at MIDI 54, in the
"VDLite Finale Marching Percussion" combination map. Confirmed in **three** editions of the
Finale user manual, all carrying the identical pair at the identical pitches: Finale 2012
Windows, Finale Mac, and Finale 2014 Mac (sources 13 and 59). So it has been shipped by
MakeMusic in a released product across at least three editions.

**Where it does not exist.** Not in Tapspace's own 112-page *VDL 2.5 User Guide* — the
SnareLine keymaps carry `FAT crush` and `DRY crush` in the region where the combination map
puts guz, but never the word. Not in the VDL-for-Garritan maps. Not in any of the five
technique packets, the two technique manuals, Blakley's glossary, drumming.com's 250-term
glossary, or the Wikipedia snare articles. The supervisor ran two further searches across
VDL documentation, drumline glossaries, technique manuals and snare pedagogy and found
nothing that defines it.

**Status.** A real term in a shipping product map with **no published definition anywhere
reachable**. Its map position, adjacent to where the Manual instruments place `FAT crush` /
`DRY crush`, and its Short/Long pairing, which every other VDL sustained articulation uses
for length, together suggest `guz ≈ crush`. That is inference and is recorded as
**UNVERIFIED**; it is not a finding and must not be minted as one. Tapspace is the sole
source, which puts `guz` in the same bracket as `gok-shot`, `smash`, `crunch-choke` and
`Half Crash` (§5.1 item 5).

### 2.5 Marching snare stroke names in the pedagogical and reference literature

| Term (source spelling) | Verbatim or close definition | Locator |
|---|---|---|
| **rimshot** (normal) | "played with the tip (bead) of the stick held about three inches (about 8 cm) from the rim. This produces a prominent, accented tone." | Wikipedia *Rimshot*, wikitext line 14 |
| **ping shot** | "the bead is struck about one inch (2.5 cm) from the rim. This produces a high-pitched sound." | ibid. line 15 |
| **gock** (also **gawk**) | "produced by hitting the bead of the drum stick at the center of the drum while the rim is percussed with the distal shaft of the stick (near the hand). This makes a lower sound." | ibid. line 16 |
| — | "In Latin percussion, timbales players use rimshots near the edge of the head, but these sound very different from gocks in marching percussion." | ibid. line 18 |
| **ping rimshot** | "achieved by hitting closer to the rim, producing a higher-pitched, metallic sound" | Jack Bennett, icanplaydrums.com, 2025-01-13 |
| **stick shot** | "a rimshot is performed by placing one drum stick with the stick head near the middle of the drumhead, and the shaft pressed against the rim, and striking with the other stick. This produces a less powerful sound … This variation is also known as a 'stick shot'." | ibid. line 20, §orchestral |
| **stick shot** | "Press one drumstick tip against the head at approximately 30 degrees, while striking that stick at the shoulder with the opposite stick." | Steve Fidyk, "Jazz Drummer's Workshop: The Stick Shot", *Modern Drummer*, July 2013 |
| **cross stick** | "the tip of a drum stick is placed on the head near one of the bearing edges and the shaft of the stick is struck against the rim opposite the tip, thus creating a dry, high-pitched 'click' similar to a set of claves" | ibid. line 22 |
| **backsticking** | "a snare drum technique characterized by swinging the butt of the drumstick to play the drum … typically only practiced among marching drum corps or drumlines" | Wikipedia *Backsticking* |
| **backstick** | "when a note is played with the butt of the drumstick, most often found in marching snarelines … Backsticks are closely related to visuals" | Blakley, *Percussion Glossary*, s.v. Backstick |
| **cross stick** (2nd sense) | "can also refer to when a stick is pressed against the drum head and the other stick then hits it to create a wooden click that is supported by the lower frequency of the drum underneath" | ibid., s.v. Cross Stick — this second sense **is** the stick shot |
| **rim click** | "simply tapping the rim of the drum with the implement rather than the drum head itself. This is most often notated using an 'X'" | ibid., s.v. Rim Click |
| **rimshot** | "played by simultaneously hitting the drum head and drum rim together with the implement" | ibid., s.v. Rimshot |
| **Ping Shot**, **Full Shot** | used as written performance directions above the snare stave in a college warm-up | SUU Drumline 2025 Exercise Packet, exercise at rehearsal figures 23 and 25 |
| **backsticking, crossovers, stick tosses** | grouped together as "embellishments" that "were developed in and originated in the North American drum & bugle corps activity" | Wikipedia *Marching percussion*, wikitext line 24 |

### 2.5.1 `back-stick` — a dated provenance chain, and the oldest evidence in this bucket

Raised because the rudiments bucket reports `back-stick` as unattested in any source it
reached. It is attested, and better than any other term here: it has a named inventor, a
date, an institution, and a nineteenth-century artefact.

**The received account.** Joe Marrella, "The Baron of Backsticking", *Drum Corps World*
Vol. 36 No. 15, December 2007, quoted verbatim by Mirsky:

> "Believe it or not, BackSticking was developed in 1938 by its creator as a method to
> improve a drummer's left hand. The first BackSticking exercise was accenting triplets.
> The technique was first taught to the Air Force snare drum section in 1958 by my dear
> friend, my mentor, my instructor … His name is John Dowlan. To me, he is the 'Baron of
> BackSticking'."

**The institutional record.** World Drum Corps Hall of Fame, official biography of John
Dowlan, quoted verbatim by Mirsky:

> "In 1935, John joined the Osmond Post Cadets Junior Corps in Philadelphia as a rookie
> drummer … It was during this time John also developed and refined his practice techniques
> commonly known today as BackSticking." … "In 1957, John was selected by M/Sgt Truman
> Crawford to teach and arrange percussion for the drum line of the USAF Drum Corps,
> Washington, DC. While there the Air Force drummers introduced the World to John's
> BackSticking Techniques."

Mirsky adds his own dating of the technique's spread: "I first saw backsticking during a
visit to a rehearsal of the New York Skyliners at the 369th Regiment Armory … sometime in
the early 1960s … At the time it was revolutionary."

**The pre-1938 evidence.** Mirsky's follow-up article overturns the 1938 date using an
artefact: an Armstrong & Co. (Boston) lithograph, *"A.R. Carrington, champion drum soloist,
1870s"*, NYPL Mid-Manhattan Picture Collection, call number `PC MUSIC-Dru`, Digital ID
832408, Record ID 1062097. He writes:

> "it is now clear that some form of the technique was practiced by A.R. Carrington some 60
> years earlier than 1938, in the 1870s, as evidenced by the drawing illustrating
> Carrington's right hand in the middle of a backsticking flip."

Corroborated by a contemporary review, *Utica New York Observer*, 3 July 1878:

> "The manner in which he handles the drum-sticks is something marvelous … During his most
> rapid performance a drum stick would be seen whirling in the air, or would be thrown from
> behind up under one leg, and caught, the most exact time being kept the while."

**What this fixes.** `back-stick` is not a vendor coinage. It is a named technique with a
1930s inventor, a 1958 institutional debut through the USAF Drum Corps, and iconographic
evidence from the 1870s. It also confirms the classification MuseScore's own 2013 name
implied: the 1878 review describes *stick tosses in the same breath*, and MuseScore called
pitch 60 `Visual (BS,X-Over,Etc)` until 2025. Backsticking is a visual technique that
happens to sound.

**Casey Claw** (Wikipedia, *Casey Claw*) is the sharpest statement of why `contact` needs
`butt` as a first-class value: "the first note of every right hand double is played with the
'butt' end of the drum stick and the very next note of the double is played with the tip".
Created by Mark Casey in 1990 at the University of Kentucky, first performed at DCI in 1993,
performed by the Cavaliers 1994, 1995 and 2023. The article also records a grip the model
cannot express: "The stick is held with the right hand in the middle of the stick … held in
a fist, where all the fingers wrap around the stick". The round 2 brief lists `fist` among
the `implement` values; `axes.json` v0.1 does not contain it (see §5.2).

### 2.5.2 Negative result: Thom Hannum, *Basic Snare Drum Technique*

Hannum is among the most cited marching pedagogues in the United States (University of
Massachusetts; Star of Indiana), and Pearl publishes this 13-page primer free. Its sections
are: Stand Assembly and Instrument Position · Tuning and Stick Selection · Grip Guidelines
and Posture · Stroke Motion, Rebounds, and Stick Heights · Multiple Bounce · Flams ·
Single-double-triple beats · Music Reading · Practice Tips.

It names **none** of `backstick`, `rimshot`, `ping`, `gock`, `stick shot`, `cross stick`,
`rim click`, `shell` or `crush`. Its only relevant vocabulary is "striking area (center of
the drum head)" and "multiple bounce, or buzz roll". This is a genuine finding, not a failed
fetch: **the standard free primer by a leading marching authority is about grip, stroke and
rudiment, and does not name striking positions or stroke variants at all.** The
position-and-variant vocabulary this bucket documents lives in sample-library keymaps and in
individual programmes' packets, not in general snare pedagogy.

Three separate authorities therefore describe the *ping / normal / gock* triple as a
**striking-position family within the single technique "rimshot"**: the variable is how far
from the rim the bead lands, which simultaneously fixes where on the stick the rim is
struck. Ping = bead ~1″ from rim; normal = bead ~3″ from rim; gock = bead at centre, rim
contacted by the shaft near the hand.

### 2.6 Marching tenor and bass line

| Term | Verbatim or close definition | Locator |
|---|---|---|
| **spocks** | "Modern tenor configurations usually have four drums and one to two special effect drums known as spocks … The spocks are tuned relatively high and are used to play a unique, high pitched sound that cuts through the ensemble" | Wikipedia *Marching percussion*, line 52, citing Udow, *Percussion Pedagogy*, p. 363 |
| **gock / shot / spock drums** | "A full-size set of tenors consists of 10, 12, 13, and 14 in toms arranged in an arc, often with an additional one or two smaller (6 or 8-inch) toms called 'gock,' 'shot,' or 'spock' drums inside of the arc." | ibid., line 64 |
| **quads / quints / sextets** | "All multi-tenors based on the four-drum configuration are called *quads* … Sets with one gock drum are called *quints*, and sets with two gock drums are called *sextets*, 'squints', *hexes*, or *sixpacks*." | ibid. |
| **gock drum** | "A gock drum is the smallest drum or drums on a set of marching tenors. This drum is also called a spock or shot drum." | Blakley, s.v. Gock (also `Shot Drum → see Gock`) |
| **sweep** | "Sweeps get their name from the sweeping motion — or scraping motion — that is created when you play a double, and you split it between two drums." | Rudimental University, part 5 of 7 |
| **sweep** (2nd) | "most common in marching tenor drumming where a double-stroke roll is moved all around the set of drums" | Blakley, s.v. Sweep |
| **sweep playing zones** | "When playing sweep or scrape patterns, the sweep playing zones are as follows … These zones are in the same concentric circle as the regular zones." | Missouri State FA20 manual, "Playing Zones" |
| **regular playing zone** | "We want to impact the head on one concentric circle, like a timpanist. We want to be off center, approximately 2 inches from the rim, or 1.5 inches from the bearing edge." | ibid. |
| **crossover** | "if you are crossing between two drums that are adjacent … you will do a 'stick cross'. That is, the sticks will intersect each other at or in front of the fulcrum. If you need to cross over to two drums that are not next to each other, you will perform an 'arm cross'." | ibid., "Cross Overs" |
| **crossover** (2nd) | "where one hand physically crosses over the other to play a drum" | Blakley, s.v. Crossover |
| **helicopters, butterflies, figure eights** | named crossover sweep patterns, taken from the visual shape traced | Rudimental University, crossovers tag |
| **skank** (= muffled shot) | "This is a rim shot that is muffled immediately or after a brief period of resonance … Use three fingers to press hard into the CENTER of the head" | Missouri State FA20 manual, "Skanks (Muffled Shots)" |
| **spank** | "the bottom drum is played with a rimshot quickly followed by the opposite hand's fingers deadening the sound. This is similar to a muffle, but the actions are independent, not simultaneous." | Blakley, s.v. Spank |
| **split part** | "each bass drummer only plays one segment of the entire bass drum part, unlike the snares and tenors. This is known as a *split part*." | Wikipedia *Marching percussion*, line 79, citing Bailey & Caneva, ch. 8, p. 132 |
| **unison** | "A *unison* refers to when all or some bass drummers play together at the same time." | ibid. |
| **rim click** (bass) | "sometimes the basses will play a rim click, in which they will hit a metal bar attached to the rim of the drum. This is mainly used for subdividing rhythms, and are mainly used when the snares play one or more rim shots and the basses have a unison note on the offbeat." | ibid., line 85 |
| **splits, groupings** | "Most splits will be in groupings of 2 (16th notes), 3 (24th notes / sextuplets), and 4 (32nd notes and above)." | SUU packet p. 8 |
| **unison balance** | "Bassline should balance in ascending order (4 listens to 3, 3 listens to 2 and so on)." | SUU packet, "Unisons" |
| **line size** | "A line of 5 (with individual drum sizes ranging from 18 to 32-inches) is the most common in a drum corps." | Wikipedia *Marching percussion*, line 79 |
| **bass mallet sizing by position** | "Bass 1 – MB1H; Bass 2 & 3 – MB2H; Bass 4 – MB3H" | EPCHS Marching Bass Drum Guide, p. 3 |

The bass numbering direction (1 = smallest and highest, N = largest and lowest) is
corroborated three ways: MuseScore places `Drum 1` on the top staff line and `Drum 5` on
the bottom; Tapspace places `Drum 1` at the highest MIDI pitch of the group; EPCHS assigns
progressively larger mallets from Bass 1 to Bass 4. No source reached states the rule in
one sentence, so it is recorded as **corroborated by three independent artefacts** rather
than as a quoted rule.

### 2.7 Marching cymbal line

Five programmes' packets agree on the sound set and disagree on the names. Locators:
**[RA]** Rhythm Armada 2020, **[GV]** GVSU/Waling, **[OS]** Oregon State, **[PC]** PCHS,
**[MB]** marchingcymbalstechnique.blogspot, **[MS]** Missouri State FA20, **[VDL]**
Tapspace VDL 2.5 p. 38.

| Sound | Definition (source) | Synonyms the sources themselves list |
|---|---|---|
| **Port Crash** / **Vertical Crash** | plates vertical, "A"/"V" prep, flam contact [RA p. 11], [OS] | Vert Crash [GV] |
| **Flat Crash** | plates at a 45° "seat-belt" angle, primary hand attacks the stationary hand [RA p. 12], [GV p. 14] | — |
| **Orchestral Crash** | "the purest technique as it relates in comparison to the technique one would use off the field" [RA p. 13] | Full Orchestral, Concert/Ballet technique [RA] |
| **Drop Crash** | attacking hand fully extended overhead, dropped into the stationary plate [RA p. 13] | — |
| **Crash Choke** | "instead of following through the rebound, the cymbals are pulled into the stomach or the shoulders" [PC p. 12] | Flat/Port Crash Choke [RA], [GV] |
| **Smash Crash** | "All of the edges must come in contact at the same time … leave the cymbals together. The objective is to produce a very short accented sound. There should be no vibrating" [PC p. 12] | Slam [OS], Slams [RA] |
| **Hi-Hat** | "press the right plate firmly to the left … mimics the drumset Hi-Hat, but creates a darker 'thoop' sound" [GV p. 5]; "press front of cymbals together to create a nice 'chick' sound" [MB] | Hi-Hat Choke [PC], Hinge choke [MS] |
| **Press** | "pressing and holding the cymbals together while still maintaining the Flat position … slightly heavier but brighter version of a Hi-Hat" [GV p. 7] | **Crunch, Crush, Closed Sizzle, Slam** [GV, explicit synonym list] |
| **Crunch** | "slamming the cymbals together from a distance for a forceful hi-hat sound" [MB] | Crunch Choke [VDL] |
| **Sizzle / Sizz** | "bringing the cymbals together and then leaving little pressure … let the plate rattle against each other" [GV p. 7] | **Sizzle, Slide, Rattle** [GV] |
| **Succ / Suck** | "bringing the right cymbal backwards, towards the player, and pressing the bottoms of the palms of both hands together. This should create a vacuum like 'thoop' or a Succ of air." [GV p. 8] | **Vacuum, Suck** [GV]; `Vacuum Suck` [VDL] |
| **Sizz-up / Sizzle Suck** | a sizz that resolves into a succ with no gap [GV p. 8], [RA p. 16] | **Sizz-Succ, Slide Choke, Fusion, Bizbop, Pea Soup** [GV]; Fusion Crash, "also referred to as a slide" [PC p. 12]; Slides, or sizzle-sucks [Wikipedia *Marching percussion* line 96] |
| **Tap** | "rotating the right forearm and wrist so that the plate travels in the current horizontal plane … contact 1–2 inches inside the edge" [GV p. 10]; "tapping the edge of one cymbal with the other" [MB] | **Ting, Ding** [GV, explicit] ; `Tap Edge`, `Tap Halfway` [VDL] |
| **Ding** | "hitting the right to the left 1 inch outside the inner bell of the left" [GV p. 12]; "similar to the sound of the Bell being struck with the shoulder of a stick … striking the edge of the Attacking Hand cymbal into the Bell of the Secondary Hand" [RA p. 14]; "a tap, but this time against the inside bell" [MB] | **Bell Tap, Dong, Gong** [GV, explicit] |
| **Tap Choke** | tap immediately muted into the choke position, "an eighth note after the sound" [GV p. 10] | **Vertical Punch, Vertical Smack, Vertical Slap Choke** [GV, explicit] |
| **Punch** | "played from choke positions and starts with a prep … After the contact is made, the plates are brought into choke position to mute the sound." [GV p. 11] | **Tap Choke, Skank, Slap Choke** [GV, explicit] |
| **Body Tap** | "rotating the right plate … then contacting the left plate … After playing a Body Tap, the cymbals reset to Choke position" [GV p. 11] | **Dead Tap, Clicks** [GV]; Dead taps [OS]; `Click` [VDL] |
| **Zing** | "putting pressure on the plates and scraping the right cymbal upwards against the left plate, stopping 1–2 inches past the outer edge" [GV p. 12]; "scrape the edge of the right cymbal along the inside bow of the left cymbal from the bell to the edge. This is the softest sound produced on cymbals" [PC p. 13]; "scraping outward along the inside of the bow of one cymbal with the edge of the other" [MB] | Slow Zing / Fast Zing [VDL]; scrapes/zings [MS] |
| **Scrape** | "The edge of the right plate is brought inside the left cymbal, and then scraped back and forth" [GV p. 13] | **Scratch** [GV]; `Scratch In`/`Scratch Out` [VDL] |
| **Tong** | "The right cymbal bells come in contact with the left cymbal edge" — the mirror image of a Tap [PC p. 13] | — |
| **Wash** | "By rotating both wrists the edges of the cymbals should touch in a circular motion … to sustain the cymbal sound for long periods" [PC p. 13] | `Circular Roll`, `Flat Roll`, `Tremolo` [VDL]; cymbal rolls [MS] |
| **Weedwacker** | left plate rises to port while the right rotates thumb-down, contacting perpendicular 1–2″ off the inner bell [GV p. 13] | — |
| **Tap Sizz** | "playing a Tap and then continuing to add slight pressure to let the edges of the plates rattle" [GV p. 13] | — |
| **Whale Call** | (unnamed elsewhere) | [VDL] only |
| **Holding for snares** | the cymbalist holds plates so a snare drummer can play them "as ride cymbals or like hi-hats"; the holder gives access to "the edge, bow, and bell" [OS p. 154], [PC p. 13], [Wikipedia line 98] | — |
| **Garfield grip** | "the hand goes through the leather strap and twists, causing the hand to be flat against the bell of the cymbal", named after the Garfield Cadets | [Wikipedia line 92], [RA p. 7] |
| **Lock / West Coast vs Flow / East Coast** | two named schools of marching cymbal technique, rigid-aggressive vs fluid-relaxed | [RA p. 3] |

### 2.7.1 Corroboration status of the cymbal terms — is Tapspace the only authority?

Raised by the supervisor on behalf of the notation-standards bucket, which carries `zing`,
`smash` and `crunch choke` as UNVERIFIED and was told that no general marching-cymbal source
names them. **That negative is wrong for three of the four terms.** Counts below are
word-bounded occurrences in the extracted text of each source, all of them non-Tapspace and
institutionally independent of each other.

| Term | Independent non-Tapspace sources naming it | Verdict |
|---|---|---|
| **zing** | 6 — GVSU/Waling (2, with a full definition), Rhythm Armada (2, definition), Oregon State (5, definition), PCHS (2, definition), Missouri State ("scrapes/zings", p. 541), marchingcymbalstechnique blog (definition) | **Well corroborated.** The most uniformly defined marching cymbal term in the bucket: every source describes a scrape of one plate's edge along the other's bow, bell outward. Notation bucket may drop the UNVERIFIED mark. |
| **suc / succ / suck** | 4 naming it — GVSU (8, "also referred to as Vacuum, Suck"), Rhythm Armada ("Sucks (suck)" in its Glossary of Sounds, plus a definition), Oregon State ("sizz-suck", 3), marchingcymbalstechnique blog (definition) — plus Ohio State corroborating the *mechanism* without the name: cymbals are held "slightly offset to prevent suctioning" | **Well corroborated as a sound.** MuseScore's spelling `Suc` remains single-vendor; the field spellings are succ and suck. |
| **crunch** | 2 — GVSU, which lists **Crunch** as an explicit synonym of its `Press` sound ("also referred to as Crunch, Crush, Closed Sizzle, Slam"); marchingcymbalstechnique blog, which defines it outright: "slamming the cymbals together from a distance for a forceful hi-hat sound". Oregon State's ten "crunches" are abdominal exercises, not a cymbal sound — a false positive worth recording | **Thinly corroborated but real.** Two sources, one of them only as a synonym. MuseScore's `Crunch (HH)` gloss is vindicated by the blog's definition, which literally says "hi-hat sound". |
| **smash** | 1 — PCHS Marching Percussion Handbook, "**Smash Crash**", p. 12, with a full definition ("All of the edges must come in contact at the same time … The objective is to produce a very short accented sound. There should be no vibrating"). Its documented synonym **slam** adds 3 more: GVSU, Rhythm Armada ("Slams (slam)"), Oregon State | **Weakest of the four.** Under the name *smash* it rests on one packet; under the name *slam* it is well attested — but see §4, where three programmes give *slam* three incompatible meanings. |
| **crunch choke** (the Tapspace key name specifically) | 0 | **Tapspace-only as a compound.** `Crunch` and `choke` are each attested; their combination is a VDL key name (p. 38) and nothing else reached uses it. |

So the marching cymbal vocabulary does **not** stand on Tapspace alone — it is the one part
of this bucket with the *most* independent corroboration, from five programmes' own
technique packets. What does stand on a single source is narrower and should be marked as
such: `smash` under that name (PCHS only), `crunch choke` as a compound (Tapspace only),
`Half Crash` (no source at all — see §2.8), and `Whale Call` / `Weedwacker` (one source each).

Two named sources fetched at the supervisor's suggestion returned **negative results worth
recording**, because they show where this vocabulary is *not* written down:

- **Ohio State (TBDBITL) Marching Fundamentals**, §D, names five cymbal *positions* —
  Traditional, Vertical A/V, Traditional hi-hat, **Gumption**, **Punch** — and no effect
  sounds whatever. It is a drill-and-carriage document. Two incidental corroborations fall
  out of it: `Gumption` as a position name, which GVSU also lists (as a synonym of Flat,
  alongside "Mid Port"); and `Punch` as a **low** position, "tops at the level of the
  armpits … an upside-down 'V'", which independently supports §2.8's finding that
  MuseScore's `Punch` at pitch 79 is mislabelled, since a punch is played low and choked,
  not as a crash.
- **Corey Pearce, "Marching Cymbals 101"** is a video-course index. It names grips,
  positions and flips (Garfield Grip, Pistol Grip, Port, Set, Carry, Wrist Rolls, Basic
  Flips, Holster, Sones Flips) and defines nothing. Useful only as further evidence that
  marching cymbal pedagogy is organised by *holding position* first — the dimension §3.2
  item 12 records as fitting no axis.

The four sources the supervisor named as places where corroboration for the Garfield grip,
lock technique, V crashes and choke technique would live: all four are now cited in this
dossier — GVSU and Rhythm Armada in §2.7 (fetched before the suggestion arrived), Ohio State
and Corey Pearce here.

### 2.8 Verdict per MuseScore name — does its use match the authority?

| MuseScore name (file) | Authority found | Does MuseScore's use match? |
|---|---|---|
| `Gok Shot` (snare .drm 52) | Muse Drumline via `c7dc55ea2d`; field term is **gock / gawk**, defined by Wikipedia *Rimshot* line 16 as a rimshot with the bead at the drum's centre; **also** a name for the small tenor drum ([Wikipedia *Marching percussion*] line 64, Blakley) | **Meaning yes, spelling no.** It is placed in the snare set as a rimshot variant, which is the correct sense; but "Gok" is a single-vendor spelling attested nowhere outside MuseScore/Muse Drumline. Tapspace's 112-page manual never uses the word at all. |
| `Ping Shot` (snare .drm 49) | Wikipedia *Rimshot* line 15; used as a written performance direction in the SUU 2025 packet; **`Ping Shot` is a literal Tapspace VDL articulation name** (VDL guide pp. 24–28) | **Yes.** Name, spelling and meaning all match the vendor and the literature. |
| `Rim Shot` (snare .drm 51, instruments.xml 52) | VDL `RIM SHOTS`; Wikipedia line 14; Blakley | **Yes**, but the model loses the ping/normal/gock distinction being *positional*: all three are rimshots. |
| `Back Stick` / `Backstick` (60) | VDL `Backsticks`, `RH/LH backstick`; Wikipedia *Backsticking*; Blakley; and the full dated chain in **§2.5.1** — Marrella in *Drum Corps World* 2007, the World Drum Corps Hall of Fame bio of John Dowlan, and an 1870s NYPL lithograph | **Yes, and it is the best-sourced term in the bucket.** Note the archaeology: MuseScore called pitch 60 `Visual (BS,X-Over,Etc)` from 2013 until `0ce0df221b` (2025-01-28). The 2013 name was the more honest one — an 1878 newspaper review of A.R. Carrington describes backsticking and stick tosses in the same sentence. |
| `Stick Shot` (57) | VDL `Stick Shot`, `Stick shot HIGH` / `Stick shot LOW`; Wikipedia *Rimshot* line 20; SMuFL `pictStickShot` U+E7F0 | **Yes.** MuseScore has one stick shot; VDL distinguishes two heights. |
| `Cross Stick` (snare .drm 56) | VDL calls it `Cross stick Rim Knock`; Wikipedia line 22; Blakley gives **two** senses | **Partly.** MuseScore ships `Cross Stick` (56) and `Rim` (53) in the `.drm` but `Rim Click` (53) and no cross stick in `instruments.xml`. The two files disagree about pitch 53. |
| `Rim` / `Rim Click` (53) | Blakley s.v. Rim Click; VDL `RIMS` and `Rim Knock` | **Yes** for meaning; the two MuseScore files name the same pitch differently. |
| `Buzz` (instruments.xml snare 48; tenors `Drum n Buzz`) | VDL `FP buzz roll`, `Buzz Roll SUSTAINED`, `Rim buzz roll`, `sustained buzz` | **Yes**, but MuseScore models buzz as a single discrete note; every vendor source treats it as a *sustained* articulation with length and dynamic shape (`FP`, `crescendo`, `SHORT/MEDIUM/LONG`). |
| `Shell` (instruments.xml snare 59; tenors `Drum 3/4 Shell`) | VDL `Snare shell` (p. 24) and **`Double-stop on lower shells`** (p. 30) | **Yes, and precisely.** MuseScore gives Shell only to tenor drums 3 and 4 — exactly the "lower shells" Tapspace records. That is not a coincidence; it is the vendor constraint showing through. |
| `Spock 1` / `Spock 2` (tenors) | Wikipedia *Marching percussion* line 52 (citing Udow p. 363) and line 64; VDL `Spock 1` / `Spock 2` | **Meaning yes, ordering contradictory.** `Marching_Tenors.drm` puts Spock 1 above Spock 2, agreeing with Tapspace; `instruments.xml` (from `5f8cac1369`, 2017) puts Spock 2 above Spock 1. One of MuseScore's two shipped files is wrong. Tapspace's ordering (Spock 1 high) is the one with vendor backing. |
| `Drum n Shot` (tenors .drm) | VDL `Drum n shots/rims` | **Yes** — "shot" on a tenor is a rimshot. |
| `Unison` / `Unison Hits/Rims/Rimshots` (bass) | Wikipedia line 79 citing Bailey & Caneva p. 132; VDL `UNISON HITS`/`UNISON RIMS`/`UNISON CRUSH`; SUU packet | **Yes.** A 1→N expand target, exactly as round 1 suspected. |
| `Drum 1..5` (bass) | VDL `Drum 1..6`; EPCHS mallet table; MuseScore's own staff lines | **Yes** for direction (1 = highest). But 5 is not a limit: VDL ships a 10-drum bass line and Wikipedia records lines of 2 to 9. |
| `Rim` (bass, was `Rim Knock` in 2013) | Wikipedia line 85: the bass "rim click" is a strike on **a metal bar attached to the rim**, not on the rim itself; VDL `Cross stick Rim Knock` | **Name yes, physics no.** A marching bass "rim" is a dedicated metal click bar. This is a distinct contact site the model has no value for. |
| `Crash` / `Full Crash` / `Half Crash` (cymbals) | VDL has `Port Crash`, `Orchestral Crash`, `Flat Crash`; the packets add `Drop Crash` | **Weak.** "Full" and "Half" describe dynamic/depth; every marching authority classifies crashes by *plate geometry* (port/vertical, flat, orchestral, drop), not by depth. `Half Crash` is attested in **no** source reached — **UNVERIFIED**. |
| `Crunch (HH)` (cymbals .drm 76) / `Hi-Hat` (instruments.xml 76) | [MB]: crunch = "slamming the cymbals together from a distance for a forceful hi-hat sound"; [GV]: Press "also referred to as Crunch, Crush, Closed Sizzle, Slam"; VDL `Crunch Choke` and `Hi Hat Choke` are separate keys | **Yes for crunch; the "(HH)" gloss is defensible but the two are separate sounds in every packet.** MuseScore collapses hi-hat and crunch onto one pitch, and its two files disagree on which name that pitch carries. |
| `Sizzle` (77) | [GV] Sizz; [PC]; VDL `Sizzle` | **Yes.** |
| `Punch` (cymbals .drm 79) / `Crash-Choke` (instruments.xml 79) | [GV p. 11] defines Punch as a **choked tap from the choke position**, synonyms "Tap Choke, Skank, Slap Choke" | **No.** Pitch 79 is `Crash-Choke` in one MuseScore file and `Punch` in the other, and those are different sounds in the literature: a punch is a choked *tap*, not a choked *crash*. This is a genuine mislabel. |
| `Tap` (81) | [GV p. 10]; VDL `Tap Edge` / `Tap Halfway` | **Yes**, though the sources split tap by contact point and MuseScore does not. |
| `Ting` (cymbals .drm 84) / `Bell Tap` (instruments.xml 84) | [GV p. 12] "Ding … also referred to as a **Bell Tap**, Dong, Gong"; [RA p. 14] Ding = edge into the bell; VDL `Ding` | **Meaning yes, spelling no.** Both MuseScore names sit on the same pitch and denote the same physical stroke, and the literature confirms Ding = Bell Tap. "Ting" as a spelling appears only as one of GVSU's synonyms *for a plain Tap*, so MuseScore's `Ting` at the bell-tap pitch is spelled from the wrong side of a documented ambiguity. |
| `Suc` (cymbals .drm 89) / `Smash` (instruments.xml 89) | Succ/Suck [GV p. 8], VDL `Vacuum Suck`; Smash Crash [PC p. 12], Slam [OS], Slams [RA] | **Both are real terms — but they are different sounds sharing one pitch.** A succ traps air for a vacuum "thoop"; a smash crash is an all-edges-flat dead attack. MuseScore's two files put them on the same note. `Suc` is also a non-standard spelling (field spellings: succ, suck). |
| `Zing` (91) | [GV p. 12], [PC p. 13], [MB], VDL `Slow Zing`/`Fast Zing` | **Yes.** The most uniformly defined marching cymbal term found. |
| `Tap-Choke` (83), `Bell Tap-Choke` (86) | [GV p. 10] Tap Choke; VDL `Tap Choke` | **Yes.** MuseScore's `Bell Tap-Choke` is a compositional combination no single source names, but it is a coherent one. |
| `Muted Tap` (88) | [GV p. 11] Body Tap, "also referred to as a Dead Tap, Clicks"; [OS] Dead taps; VDL `Click` | **Yes** in meaning; the field name is Body Tap or Dead Tap. |
| `Roll` (93) | [PC p. 13] Wash; VDL `Flat Roll`, `Circular Roll`, `Tremolo`; [MS] "cymbal rolls" | **Yes**, but flattened: three named roll types collapse to one. |
| `Battery Snare` (instruments.xml 50) / `Hit` (.drm 50) | VDL `MAIN HITS`; "battery" = the marching drums as a section (Blakley: `Battery → see Drumline`) | **`Hit` yes; `Battery Snare` is a section label, not a stroke name.** |
| `Stick Click` / `Stick click` (55, tenors 43) | VDL `Stick click`, `Unison stick click`, `Tenor Stand click`, `Aluminum mallet clicks` | **Yes.** |
| `Show-Style Tenors` (`marching-show-tenors`) | VDL `Showstyle Single Tenors` (guide p. 21 index) | **Yes** — and round 1 missed this instrument entirely. |

---

## 3. Axis mapping

### 3.1 Terms that map cleanly

| Term | Axis | Value (existing or proposed) |
|---|---|---|
| ping shot, gock shot, rim shot (normal) | `technique` = `rimshot` **plus** `position` | the three differ only in `position`: perimeter / offset / centre |
| stick shot, stick shot HIGH / LOW | `technique` | `stick-shot` (exists) |
| back stick, backsticking | `technique` `back-stick` + `contact` `butt` | exists |
| cross stick, rim knock | `technique` `sidestick` + `site` `crossstick` | exists |
| rim click, rim only | `technique` `rim-only` + `site` `rim` | exists |
| shell, snare shell, double-stop on lower shells | `site` | `shell` (exists) |
| bow, edge, bell (cymbal held for snares) | `site` | `bow`, `edge`, `bell` (exist) |
| tap edge / tap halfway | `position` | `perimeter` / `halfway` (exist) |
| VDL "STICK PLACEMENT: center of head / halfway to edge / edge of head" | `position` | `centre` / `halfway` / `perimeter` — **direct vendor confirmation of the axis and of three of its four anchors** |
| Missouri State "2 inches from the rim … 1.5 inches from the bearing edge" | `position` | `offset` — the marching default is *not* `centre` |
| buzz, buzz roll, FP buzz roll | `ornament` | `buzz`, `roll` (exist) |
| crush, fat crush, dry crush, wet crush | `ornament` | **missing** — see §5 |
| crescendo / decrescendo / diminuendo roll | `ornament` | `crescendo`, `swell` (exist); diminuendo missing |
| wash, flat roll, circular roll, tremolo | `ornament` | `wash`, `roll` (exist) |
| flam (cymbal crash contact), drag, ruff | `ornament` | exist |
| muted, hand muffle, muffled taps, dead tap, body tap | `damping` | `muted`, `damped` (exist); `dead` also exists on `technique` |
| skank, spank (muffled rimshot) | `technique` `rimshot` + `damping` `muted` | composable from existing values |
| snares off / snares on, throwoff off / on | `mechanism` | `wires-off` / `wires-on` (exist) |
| hi hat LOOSE / MEDIUM / TIGHT (VDL snare's held hi-hat) | `openness` | `loose` / `half` / `tight` (exist) |
| rods, dreads, felt, puffy mallets, regular mallets, aluminum mallet | `implement` | `rod` exists; the rest missing — see §5 |
| butt (vertical) | `contact` | `butt` (exists) |
| sweep, scrape, scratch | `technique` | `sweep`, `scrape` (exist) |
| circling / stir with dread / weedwacker | `technique` | `circling` (exists) |
| choke, crash choke, tap choke, hi-hat choke, crunch choke, slap choke | not an axis value by design (`axes.json` records that `choke` "is deliberately absent: it is a relation on a previously …") | correct call — the marching evidence supports it, because *every* cymbal sound in the packets has a choked twin |
| accent, tap (dynamic sense) | `dynamic` | `accent`, `soft` (exist) |
| Drum 1..5 (bass), Drum 1..4 + Spock 1..2 (tenors) | layout slot `instance` | exists — but see the ordering conflict in §4 |
| unison, split | neither a term nor a slot — a **1→N expansion rule** | see §3.2 |

### 3.2 Terms that fit NO axis — the valuable ones

1. **`unison` / `split part`.** MuseScore ships `Unison` (bass 90) and `Unison Hits/Rims/
   Rimshots` (90/91/92) as ordinary drumset entries. Physically they are not a sound at a
   site: they are *"every instance in this section, together"*. VDL ships them the same way
   (`UNISON HITS`, `UNISON RIMS`, `UNISON CRUSH`, `UNISON sustained roll`, `Unison stick
   click`, `Unison sticks-in`). The complementary term `split` is what a normal note means
   in a bass line. **This is a section-cardinality relation, not a pivot tuple.** It fits no
   axis and should not be forced onto one.
2. **`cage` (VDL `RH on cage` / `LH on cage`).** The carrier frame of a marching snare,
   struck deliberately. Not head, rim, rim2, crossstick, shell, bow, edge, bell or
   underside. **`site` is missing a value for the mount/hardware.**
3. **`Dress center harness hit` (VDL SnareLine).** Same class as `cage`: a strike on the
   player's harness, not on the drum.
4. **`Tenor Stand click`, `Aluminum mallet clicks`, `Stick snap`, `Sticks-in`.** Sounds of
   the equipment and of the player's rest position. `sticks` exists as an *instrument*;
   `sticks-in` is a *position*, and the click of a stand is neither.
5. **Bass drum `rim`, which is a metal bar bolted to the rim** (Wikipedia line 85). The
   thing struck is neither the rim nor the shell. Either `site` needs a `click-bar` value
   or bass rim needs to be understood as a distinct instrument.
6. **`Solo` vs section (`Solo HITS` vs `MAIN HITS`; `unison cymbal section` vs `solo
   cymbal player` in the VDL cymbal keymap).** One player or many playing the same stroke.
   Not `dynamic`, not `voicing` — it is an ensemble-size dimension the model has nowhere to
   put. Hydrogen and MuseScore both duck it too.
7. **`RH` / `LH` and Tapspace's `AutoRL`.** Handedness is carried on a *sample*, not on a
   term. The model puts `limb` on a layout slot, which handles kit limbs; a marching snare
   has two hands on one drum and the sample libraries distinguish them. **UNVERIFIED**
   whether `limb` as currently specified can express "left hand of the pair on this one
   instrument".
8. **`Visual`** — MuseScore's own 2013 name for pitch 60 was `Visual (BS,X-Over,Etc)`, and
   Wikipedia groups "back-sticking and stick tosses" as visual embellishments. A whole
   class of marching notation exists to trigger a *movement* that may or may not sound.
   No axis covers "this note is choreography".
9. **`"snenor"`** (VDL: `Drum 1 "snenor"`, `Spock "snenor"`). A tenor drum voiced to sound
   snare-like. Closest axis is `voicing`, but none of the existing values (`standard`,
   `room`, `power`, `jazz`, `orchestra`, `lo-fi`, `dark`) is about *imitating another
   instrument*.
10. **`Whale Call`, `Weedwacker`, `Bizbop`, `Pea Soup`.** Named effects with no
    decomposition into site/technique/implement. Genuinely idiomatic single-token sounds.
11. **`Lock` / `West Coast` vs `Flow` / `East Coast` cymbal technique** [RA p. 3]. A
    school-of-playing dimension that changes the attack envelope of every crash. No axis.
12. **`Garfield grip`, `Port`, `Flat`, `Orchestral`, `Choke`, `Vert`, `Tap` positions.** For
    marching cymbals, the *holding position* is the primary organising dimension — the
    packets are structured by position first and sound second. The pivot model has no
    analogue of "instrument orientation" for a two-plate instrument.
13. **`Full Shot` (SUU packet).** Written above a marching snare stave. Contrasts with
    `Ping Shot` on the same page. **UNVERIFIED** whether "full shot" is the same as the
    normal rimshot or a further variant.

---

## 4. Conflicts and false friends

**One word, different things**

1. **`gock`.** (a) a rimshot with the bead at the centre of the head, rim struck by the
   shaft near the hand [Wikipedia *Rimshot* line 16]; (b) the 6″ or 8″ accent drum on a
   multi-tenor rack, synonymous with *spock* and *shot* drum [Wikipedia *Marching
   percussion* line 64; Blakley s.v. Gock]; (c) `gock block`, a plastic woodblock
   substitute [Blakley]. MuseScore uses sense (a). Any parser that maps "gock" to an
   instrument will collide with a parser that maps it to a stroke.
2. **`shot`.** On a tenor it means *rimshot* (`Drum 1 Shot`); as a noun in `shot drum` it
   means the small accent drum; in `stick shot` it means neither.
3. **`ding` / `ting`.** [GV] lists `Ting, Ding` as synonyms of a plain **Tap**, and two
   pages later defines **Ding** as the strike into the bell, "also referred to as a Bell
   Tap, Dong, Gong". So within one document "ding" names two different sounds. MuseScore
   ships `Ting` at the bell-tap pitch.
4. **`slam`.** [OS] "quickly press the cymbals together to create an air pocket sound" —
   i.e. a suck. [GV] lists `Slam` as a synonym of **Press/Crunch** — i.e. a damped closed
   sound. [RA] "simply press, or 'slam', the cymbals together with a significant amount of
   force … in a slightly offset position, so as to avoid an air pocket" — i.e. the opposite
   of a suck. Three programmes, three meanings.
5. **`punch`.** [GV] a choked tap from choke position. MuseScore's `.drm` puts `Punch` at
   pitch 79, which `instruments.xml` calls `Crash-Choke`.
6. **`cross stick`.** [Blakley] sense 1 = the laid-flat stick struck against the rim
   (drum-kit sidestick); sense 2 = one stick pressed to the head struck by the other —
   which is the **stick shot**. Wikipedia's *Rimshot* article warns explicitly that "the
   rimshot is often confused with the cross stick technique".
7. **`rim click`.** On a snare it is the stick tapping the rim. On a marching bass it is a
   strike on a metal bar bolted to the rim [Wikipedia line 85].
8. **`crunch`.** [MB] a forceful hi-hat slam. [GV] a synonym of Press. [VDL] `Crunch Choke`,
   a distinct key from `Hi Hat Choke`. MuseScore writes `Crunch (HH)`, hedging.
9. **`tenor drum`.** In marching it is the multi-tom rack; in orchestral usage it is a
   single deep snareless drum. MuseScore's `marching-tenor-drums` correctly declares
   `musicXMLid` `drum.tenor-drum`, which collides with the orchestral instrument.
10. **`Spock 1` vs `Spock 2`.** MuseScore contradicts itself: `Marching_Tenors.drm` has
    Spock 1 higher (line −2, pitch 96); `instruments.xml` has Spock 2 higher (line −2,
    pitch 96). Tapspace's two independent maps both put Spock 1 higher.
11. **`buzz`.** In MuseScore a discrete note. In every vendor and teaching source, a
    sustained multiple-bounce roll with a length and a dynamic shape.

**Different words, one thing**

- ping shot ≈ (no synonym found; a distinctly drum-corps coinage)
- gock = gawk = (MuseScore) gok
- succ = suck = vacuum = (MuseScore) suc; and `Vacuum Suck` [VDL]
- sizz = sizzle = slide = rattle [GV]
- sizz-up = sizz-succ = sizzle-suck = slide choke = fusion = bizbop = pea soup [GV, PC,
  Wikipedia] — six names for one sound, the worst case found in this bucket
- ding = bell tap = dong = gong [GV]
- body tap = dead tap = click [GV, OS, VDL]
- tap choke = vertical punch = vertical smack = vertical slap choke = skank = slap
  choke [GV]
- press = crunch = crush = closed sizzle = slam [GV]
- smash crash = slam [PC, OS]
- port = vertical = vert
- quads = quints = sextets = squints = hexes = sixpacks = "tenors" [Wikipedia line 64]
- gock drum = shot drum = spock drum [Wikipedia line 64, Blakley]
- sweep = scrape (of the same motion) [Rudimental University: "these terms are
  interchangeable"] — but [GV] and [MS] use `scrape` for a *different*, cymbal-on-cymbal or
  head-crossing motion. Marching tenor `scrape` and marching cymbal `scrape` are unrelated.
- skank = muffled shot [MS] = spank [Blakley, with the muffle independent rather than
  simultaneous]
- stick shot = cross stick (sense 2) = "stick on stick"

---

## 5. Gaps against vocabulary v0.1

v0.1 has 155 terms, drum kit only. Percussion, orchestral, electronic and utility families
are reserved and unminted. Against that baseline:

### 5.1 What is misnamed

1. **`technique.gok-shot`.** Full ruling in **§0**. The identifier carries MuseScore's
   single-vendor spelling; the field spelling is **gock**, with **gawk** as a documented
   variant (Wikipedia *Rimshot* line 16). Tapspace's 112-page manual, the five technique
   packets, the notated exercise packets and the marching glossaries never write "gok" —
   and the reference works that do write "gock" mostly mean the tenor drum, not the stroke.
   Per ADR 0003 the slug cannot be renamed; the recommended remedy is a `correction` alias
   `gock-shot → gok-shot`, plus an alias `gawk-shot`, and a provenance record that says
   "Muse Drumline, single vendor, concept uncited".
2. **`technique.ping-shot` / `gok-shot` / `rimshot` are not three techniques.** Every
   authority reached describes them as **one technique (rimshot) at three striking
   positions**. Modelling them as sibling `technique` values means a converter cannot tell
   that a ping shot is a rimshot. Recommendation: keep the three slugs (identifiers are
   forever) but record in `rules.json` that `ping-shot` and `gok-shot` imply
   `technique=rimshot` with `position=perimeter` and `position=centre` respectively.
3. **`site.shell` is right, but `site` is missing the mount.** VDL's `RH on cage`,
   `Dress center harness hit`, `Tenor Stand click` and the marching-bass metal click bar
   are all strikes on hardware, not on the drum.
4. **`Battery Snare`** (MuseScore's name for a plain hit) is a section label, not a stroke.
   Do not mint it.
5. **Single-source names, to be minted only with the provenance recorded as such.** Beside
   `gok-shot` (§0), the corroboration audit in §2.7.1 leaves four cymbal names resting on
   one source each. Any term minted from them must carry `confidence` accordingly:
   `smash` — PCHS handbook p. 12 only, under that name; `crunch-choke` as a compound —
   Tapspace VDL p. 38 only; `whale-call` — Tapspace only; `weedwacker` — GVSU only;
   `guz` — Tapspace only, and with **no published definition at all** (§2.4.1), so it must
   not be minted on the crush inference. And
   `Half Crash`, which MuseScore has shipped since 2013, is attested in **no source
   reached at all** and should not be minted without one. By contrast `zing` (6 independent
   sources), `suck` (4 plus a mechanism corroboration) and `ding`/`bell-tap` (3 with
   explicit synonym lists) are the best-evidenced terms in the whole bucket and can be
   minted with confidence.

### 5.2 Missing values, by axis

`instrument` — `marching-snare`, `marching-tenor` (multi-tom rack), `spock` (a.k.a. gock/
shot drum), `marching-bass`, `marching-cymbals` (clash pair). All belong to a
`marching.*` family that does not yet exist among the reserved families
(`perc.hand`, `perc.shaken`, `perc.scraped`, `perc.struck-idiophone`, `perc.wind`, `orch`,
`electronic`, `utility`, `unknown`). **Marching is a missing family**, not a member of
`orch`: its instruments, its numbering and its technique names are all distinct.

`site` — missing `cage` / `mount` / `hardware` (VDL `on cage`, `Tenor Stand click`,
`Dress center harness hit`, marching-bass click bar).

`position` — the four values `centre` / `halfway` / `offset` / `perimeter` are **confirmed
correct** by Tapspace's own `center of head / halfway to edge / edge of head` legend and by
Missouri State's "2 inches from the rim". No gap. Note that `offset` — not `centre` — is the
marching *default*.

`contact` — `tip`, `shank`, `butt` cover the snare strokes found. No gap.

`technique` — missing **`skank`** (muffled rimshot, the standard tenor effect, in VDL as a
literal key name), **`spank`**, **`stir`** (VDL `STIR w/dread`), **`friction-slide`**,
**`rim-knock`** (VDL's own word for the bass/snare cross-stick-on-rim). For the cymbal
line, missing **`suck`** (vacuum), **`sizzle-suck`**, **`crunch`**, **`smash`**, **`ding` /
`bell-tap`**, **`tong`**, **`zing`**, **`tap`**, **`body-tap`**, **`weedwacker`**. `sweep`,
`scrape`, `circling`, `dead`, `rim-only`, `sidestick`, `stick-shot`, `back-stick` already
exist and cover the rest.

`ornament` — missing **`crush`** with its two documented flavours **`fat-crush`** and
**`dry-crush`** (and `wet-crush` on tenors). Crush is not `buzz` and not `roll`: it is a
short pressed multiple-bounce with a named tone quality, and it is the single most
frequently mapped articulation in the whole VDL library. Also missing **`diminuendo`** to
pair with the existing `crescendo`, and roll *length* (`SHORT` / `MEDIUM` / `LONG`) and
`FP` (forte-piano) shape.

`openness` — no gap; VDL's `Hi Hat LOOSE / MEDIUM / TIGHT` lands on existing anchors.

`damping` — `none`, `muted`, `damped`, `towel`, `gated` cover hand-muffle and dead-stroke.
No gap found, though "choke" as a *relation* is correctly kept off this axis.

`mechanism` — `wires-on` / `wires-off` cover VDL's `Snares ON/OFF`. VDL also has
`Throwoff ON` / `Throwoff OFF` as separate keys from `Snares ON/OFF`, which suggests the
*sound of operating the throw-off* is distinct from the state. **UNVERIFIED** whether that
is a mechanism value or an equipment sound.

`implement` — missing **`dread`** (Tapspace's multi-rod bundle, a first-class VDL implement
distinct from `rod`), **`felt`** (VDL `RH felt` on snare), **`puffy-mallet`** (VDL's
keyswitched alternative bass/tenor mallet), **`aluminum-mallet`**, and **`plate`** /
**`cymbal-on-cymbal`** for the entire marching cymbal line — where the implement *is*
another cymbal. The brief lists `fist` and `fingernail` in the model description but
`axes.json` v0.1 contains neither. The Casey Claw is direct marching evidence that `fist`
is needed — "held in a fist, where all the fingers wrap around the stick" (§2.5.1) — so
this is a real omission, not just a drafting slip in the brief.

`dynamic` — no gap.

`voicing` — missing a value for **imitative voicing** (VDL `"snenor"`); the closest
existing value, `dark`, is about tone not imitation.

### 5.3 Missing *mechanism* outside the axis system

- **Section unison as a 1→N expansion.** `Unison` (MuseScore bass 90) and VDL's four
  `UNISON *` keys are one note meaning "every instance". Round 1 already flagged this from
  MuseScore alone; Tapspace confirms it independently, and the marching literature gives it
  a name and a counterpart (`split part`). It needs a rule, not a term.
- **Instance ordering must be declared per family.** The layout slot rule as stated — toms
  high to low, cymbals left to right from the player's seat — does not decide a marching
  bass line (five separate players, largest to smallest left to right on the field, but
  numbered 1 = smallest) or a tenor rack (drums 1–4 numbered high to low, spocks numbered
  separately and inconsistently). MuseScore contradicts itself on spock ordering precisely
  because the rule was never written down.
- **Solo vs section.** See §3.2 item 6.

---

## 6. Self-critique (round C)

**The single most authoritative source not reached: Michael Udow, *Percussion Pedagogy*
(Oxford University Press, 2019), p. 363** — the only scholarly, peer-reviewed, citable
definition of the spock drum found anywhere in this bucket, and the citation Wikipedia
itself leans on. Google Books returns no preview of that page and no full text was
reachable. Getting it would replace a tertiary citation with a primary one for the one
piece of marching *instrument* vocabulary the model most needs. Second most valuable:
**Bailey & Caneva, *The Complete Marching Band Resource Manual*, ch. 8, p. 132**, the cited
authority for `split part`.

**What could not be reached and what it would have added**

- **Percussive Arts Society publications.** Both "Terms Used in Percussion" (*Percussive
  Notes*, Jan 1986) and "Notation for Percussion Instruments" are behind a member paywall.
  These are the closest thing to a *standard* in this space. My working conclusion — that
  no published PAS standard covers marching snare stroke names — is **UNVERIFIED**; it is
  an absence of evidence produced by a paywall, not evidence of absence. The bucket brief
  asked for "PAS marching percussion terminology and any published standard"; I can say
  only that no such standard is discoverable from outside the membership.
- **WGI and DCI.** Both bodies publish adjudication manuals and score sheets, not
  terminology standards. Their captions grade *achievement* (content, excellence, effect),
  not named strokes. I did not fetch the 2026 WGI manual because the search evidence
  indicates it would not contain stroke vocabulary. This is a judgement call and could be
  wrong; a reconciliation pass that wants certainty should fetch
  `wgi.org/percussion/percussion-score-sheets/` directly.
- **snarescience.com** returns HTTP 500 and `web.archive.org` is unreachable from this
  environment — the CDX API answers `403 Blocked by egress policy` and the supervisor
  reports connections reset mid-tunnel for both curl and WebFetch. `archive.org` itself
  answers HTTP 200, and its search API was used (source 46, zero hits). That forum is the
  main community record of "gock/gawk" and of the spelling debate around it, and it is the
  likely upstream of the Wikipedia *Rimshot* passage — which is itself **unsourced**. That
  is a real weakness: the sharpest definition of gock in this dossier rests on an
  uncited tertiary paragraph, corroborated only by the fact that four independent
  paraphrases of it circulate.
- **musescore.org** is behind Cloudflare and refused both WebFetch and curl. Issue
  `#196321` (the 2017 tenor/bass remap) and node 109826 ("Add 2nd spock drum") would settle
  *why* `instruments.xml` numbers Spock 2 above Spock 1, which is the one MuseScore
  self-contradiction I could not explain, only document.
- **MDL1's own drumset definitions.** They shipped with the non-GPL MuseScore Drumline
  extension and are not in the repository. `mdlmigrator.cpp` preserves the pitch mapping but
  not the names, so the intermediate naming layer between 2013 and 2024 is lost.
- **Muse Drumline itself.** The `.drm` names come from it, but its own documentation was
  not located; `musehub.com/muse-sounds/muse-drumline` was identified but not fetched. Its
  articulation list would show whether `Gok`, `Suc`, `Ting` and `Punch` are Muse Drumline's
  spellings or MuseScore's transcriptions of them.
- **Pre-MIDI literature.** Bruce & Emmett 1862 is on IMSLP and was not fetched. An earlier
  draft of this dossier claimed the bucket contributes nothing to the era axis because
  nothing here predates about 1970. **That was wrong and is corrected in §2.5.1.**
  Backsticking has a documented 1930s invention (John Dowlan, Osmond Post Cadets, from
  1935), a dated institutional debut (USAF Drum Corps, 1957–58), and iconographic evidence
  from the 1870s in an Armstrong & Co. lithograph of A.R. Carrington held by the New York
  Public Library, corroborated by a *Utica New York Observer* review of 3 July 1878. So one
  term in this bucket reaches back 150 years. The rest — gock, ping, spock, skank, and the
  marching cymbal effect vocabulary — do still look like post-1960 American drum corps
  coinages, but that is now an observation about those terms rather than about the bucket.
  Bruce & Emmett would still be worth fetching: 19th-century rudimental manuals name
  *beats*, and confirming that they name no striking positions would firm up §2.5.2's
  finding that position vocabulary is a sample-library phenomenon.
- **German, French, Italian and Spanish.** Searched, deliberately, and found **nothing**.
  German *Spielmannszug* / *Marschtrommel* literature and French *batterie-fanfare*
  literature describe grip, roll and rudiment but have no equivalents for gock, ping, spock,
  backstick, zing or succ. This is a positive finding, not a failure: **this vocabulary is
  monolingual American English and is not translated in scores worldwide.** Bucket 12
  (German/French/Italian) should not expect overlap here.

**Environment limits that shaped what could be checked**

- `web.archive.org` is unreachable (see above). The Wayback fallback the round 2 brief
  prescribes does not work in this environment; `archive.org`'s own search API does.
- WebSearch draws on one session-wide budget shared by all twelve round 2 workers and was
  exhausted (200/200) partway through this bucket. Round A's eighteen searches were all
  completed before that; everything after it was WebFetch and curl against constructed or
  already-discovered URLs.
- The Google Books API returns HTTP 429 "daily quota exhausted" for the whole project, so
  the two book sources (Udow; Bailey & Caneva) could not be checked by a second route.
- `musescore.org` and `tapspace.com/product/...` sit behind Cloudflare and refuse WebFetch;
  `tapspace.com/wp-content/...` does not, which is how the VDL user guide was retrieved.

**Where this dossier is weakest**

1. The gock definition rests on an unsourced Wikipedia paragraph (§2.5, §0). Everything else
   in the snare table has vendor or teaching-packet backing; gock does not. This is the
   bucket's central negative finding and it is stated plainly in §0 rather than smoothed
   over: `ping-shot` and `stick-shot` have authorities, `gok-shot` does not.
2. "guz" (Finale's VDLite map, notes 53–54) is recorded but not explained — now bounded in
   §2.4.1 rather than merely noted: confirmed in three Finale editions, absent from
   Tapspace's own manual and from every glossary and packet reached, and absent from two
   further supervisor searches. A shipping term with no published definition anywhere.
3. The bass-line numbering rule is triangulated from three artefacts rather than quoted.
4. Marching cymbal terminology is drawn from five teaching packets, which are primary for
   the programmes that wrote them but are not standards. The disagreement between them
   documented in §4 is real and is not resolvable from these sources — there is no
   authority to appeal to. That is the finding.
5. I did not test MuseScore's playback: whether `Suc` at pitch 89 actually sounds like a
   vacuum suck in the MS Basic soundfont, or whether it sounds like the `Smash` that
   `instruments.xml` names at the same pitch, is **UNVERIFIED**. Answering it would need
   the soundfont rendered, which is out of scope for a data repository.
