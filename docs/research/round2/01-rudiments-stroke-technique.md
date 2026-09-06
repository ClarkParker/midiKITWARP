# Round 2, bucket 01 — Rudiments and stroke technique

Scope: the named vocabulary of snare-drum rudiments, stroke types, roll families, grace-note
ornaments, sticking systems, rimshot variants, brush strokes and foot techniques — as the
primary pedagogical and standards literature spells them, not as converters spell them.

Method: `.agents/round2/BRIEF.md`, three rounds. Round A (breadth) was run first: 20 distinct
searches varying register (scholarly / pedagogical / trade / notational / vendor), language
(English, German, French, Italian, Spanish) and era (1588 → 2019), followed by direct fetch
probing of every candidate URL. Extraction (round B) began only after the register was closed.

All fetches dated **2026-09-06** unless stated. Byte counts are the raw bodies as received.
Working files were written under
`scratch:bucket01/` (outside the repository) and are not committed.

---

## 1. Candidate source register (round A)

`Authority` is this dossier's judgement of how binding the source is for naming:
**normative** (a standards body or association defining the names), **primary** (the source
that first coined or codified them), **secondary** (a synthesis citing primaries),
**trade** (vendor or practitioner usage), **tertiary** (encyclopaedic).

`Licence` is the verdict for KITWARP use per ADR-0004: **cite-only** means the facts may be
recorded with a locator but no text or notation may be copied into `data/`.

### 1.1 Reached in full

| # | Source | Type / era | Authority | Locator | Licence | Result |
|---|---|---|---|---|---|---|
| R01 | **Percussive Arts Society International Drum Rudiments** (the sheet) | standard, 1984 | normative | `https://pas.org/wp-content/uploads/2024/04/pas-rudiments.pdf` | © 1984 PAS, all rights reserved → cite-only | **reached**, 309 898 B; all 40 names + the NARD-26 asterisks extracted verbatim |
| R02 | pas.org `/rudiments/` landing page | web, n.d. | normative | `https://pas.org/rudiments/` | cite-only | reached; prefatory text only, the list itself sits behind facet pages |
| R03 | **Strube, Gardiner A., _Strube's Drum and Fife Instructor_** | book, 1870 | primary (the direct ancestor of the NARD 26) | archive.org id `strubesdrumfifei00stru`, OCR `_djvu.txt` | public domain (pre-1929 US) → free | **reached**, 53 993 B OCR; lesson structure, grip, "centre of the head" and left/right-hand naming confirmed from the source itself |
| R04 | en.wikipedia **Drum rudiment** | tertiary, current | tertiary (but densely cited to primaries) | `action=raw`, 59 933 B | CC BY-SA 4.0 → reference-only | reached |
| R05 | en.wikipedia **Drum stroke** | tertiary | tertiary | 4 473 B | CC BY-SA 4.0 | reached |
| R06 | en.wikipedia **Drum roll** | tertiary | tertiary | 19 645 B | CC BY-SA 4.0 | reached |
| R07 | en.wikipedia **Rimshot** | tertiary | tertiary | 4 591 B | CC BY-SA 4.0 | reached |
| R08 | en.wikipedia **Moeller method** | tertiary | tertiary | 6 958 B | CC BY-SA 4.0 | reached |
| R09 | en.wikipedia **Heel-toe technique** | tertiary | tertiary, weakly sourced | 6 078 B | CC BY-SA 4.0 | reached |
| R10 | en.wikipedia **Marching percussion** | tertiary | tertiary | 36 096 B | CC BY-SA 4.0 | reached |
| R11 | en.wikipedia **Hi-hat** | tertiary | tertiary | 9 097 B | CC BY-SA 4.0 | reached |
| R12 | en.wikipedia **Snare drum** | tertiary | tertiary | 30 465 B | CC BY-SA 4.0 | reached |
| R13 | de.wikipedia **Rudiment (Schlagzeug)** | tertiary, German | tertiary | 6 030 B | CC BY-SA 4.0 | reached; Prussian 1777 system named |
| R14 | de.wikipedia **Doppelschlag (Trommel)** | tertiary, German | tertiary, cites Peinkofer/Tannigel 1981 | 1 982 B | CC BY-SA 4.0 | reached |
| R15 | de.wikipedia **Wirbel (Spieltechnik)** | tertiary, German | tertiary, cites Tobischek 1977 | 4 811 B | CC BY-SA 4.0 | reached; four German roll classes |
| R16 | de.wikipedia **Schlagzeugspiel** | tertiary, German | tertiary | 49 968 B | CC BY-SA 4.0 | reached; grip names, `halboffen`, `Chick` |
| R17 | de.wikipedia **Basler Trommel** | tertiary, German | tertiary, cites Berger 1928 | 6 884 B | CC BY-SA 4.0 | reached; instrument, **not** the rudiment list |
| R18 | it.wikipedia **Rudimento** | tertiary, Italian | tertiary | 6 105 B | CC BY-SA 4.0 | reached; Italian names for the 26 |
| R19 | es.wikipedia **Rudimento** | tertiary, Spanish | tertiary | 20 120 B | CC BY-SA 4.0 | reached; Spanish names for all 40 + `D`/`I` sticking |
| R20 | fr.wikipedia **Caisse claire** | tertiary, French | tertiary | 4 573 B | CC BY-SA 4.0 | reached; thin, no rudiment list |
| R21 | **Marc de Douvan, "Les rudiments de la batterie militaire française"** (2005, rev. 2011/2012/2014) | pedagogical web, derived from Tourte 1946 | secondary → primary-tracking | `http://www.marcdedouvan.com/lecon.php?id=5` | © Marc de Douvan → cite-only | **reached**, 30 964 B; 21 numbered French rudiment classes with stickings |
| R22 | **Percussive Notes brush anthology** (4 articles bound in one PDF) | journal, 1996–2004 | primary (practitioner codifications published by PAS) | `https://www.brad-meyer.com/wp-content/uploads/2012/01/Brushes.pdf` | PAS copyright, third-party host → cite-only | **reached**, 2 159 733 B → 53 KB text |
| R22a | ↳ O'Mahoney, Terry, "Alternate Brush Ideas" | Percussive Notes, June 1996, pp. 20–24 | primary | in R22 | cite-only | reached |
| R22b | ↳ Hazilla, Jon, "Brushistics" | Percussive Notes, Oct 2004, p. 32 | primary (ten concepts from _Mastering the Art of Brushes_, Berklee Press 2000) | in R22 | cite-only | reached |
| R22c | ↳ Soph, Ed, "Practicing Brushes" (Drum Set Forum) | Percussive Notes, p. 30 | primary | in R22 | cite-only | reached |
| R22d | ↳ Hamilton, Jeff, "You Got to be Pretty When You Play Brushes" | Percussive Notes, Feb 2004, pp. 18–20 | primary | in R22 | cite-only | reached |
| R23 | **nard.us.com, "History of N.A.R.D."** | association, current | normative-adjacent (the successor body) | `http://nard.us.com/History_of_N.A.R.D..html` | cite-only | reached, 14 055 B |
| R24 | nard.us.com, "N.A.R.D. Rudiments" | association | normative | `http://nard.us.com/N.A.R.D._Rudiments.html` | cite-only | reached, **but the 26 names are raster images**; no machine-readable list |
| R25 | historicdrumming.com, "Swiss Drum Manuals & Resources" | worklist | secondary | `https://www.historicdrumming.com/drum-resources/swiss-drum-manuals/` | cite-only | reached; 6 Swiss manuals + 15 Ordonnanz documents 1728–1964 enumerated |
| R26 | Bloom, Ryan Alexander, "Fake Swiss Rudiments – Hybrids in Disguise" | practitioner scholarship | secondary | `https://bloomdrums.com/fake-swiss-rudiments-hybrids-in-disguise/` | cite-only | reached via WebFetch |
| R27 | Bloom, Ryan Alexander, "Basel Drumming vs. Swiss Drumming" | practitioner scholarship | secondary | `https://bloomdrums.com/932-2/` | cite-only | reached via WebFetch |
| R28 | **Vic Firth, "40 Essential Rudiments"** (Dr. John Wooton four-tier ordering) | vendor education | trade | `https://ae.vicfirth.com/education/40-essential-rudiments/` | cite-only | reached via WebFetch |
| R29 | Ninja Drummist (Lewis Partridge), "507 Hybrid Rudiments" | practitioner glossary | trade | `http://www.ninjadrummist.com/drum-rudiments/hybrid-rudiments/` | cite-only | reached, 128 740 B; ≈500 names extracted |
| R30 | "Buddy and Louis on Billy Gladstone's Technique", Not So Modern Drummer, 2017-11-18 | magazine | secondary, quotes primaries | `https://www.notsomoderndrummer.com/not-so-modern-drummer/2017/11/18/billy-gladstone-technique` | cite-only | reached via WebFetch |
| R31 | Trommelschule Basel | school site, German | trade | `https://trommelschule-basel.ch/` | cite-only | reached; names `Grundstreiche`, `Ryslaifer`, `Arabi`, Hieroglyphenschrift vs Bergerschrift — **no enumerated list** |
| R32 | drummerforum.de thread 74875, "Technik-Fragen Basler Trommeln" | forum, German | trade | `https://www.drummerforum.de/forum/thread/74875-...` | cite-only | reached; exactly one term (`Doublé`) recovered |
| R33 | Studio Drum MTL, "Best Resources for Learning the Brushes" | bibliography | secondary | `https://www.studiodrummontreal.com/post/best-resources-for-learning-the-brushes-a-helpful-guide` | cite-only | reached via WebFetch; 7 books + 5 videos named |
| R34 | IMSLP, **Bruce & Emmett, _The Drummer's & Fifer's Guide_**, Wm. A. Pond & Co. | book, 1862 (this ed. 1865) | primary | `https://imslp.org/wiki/The_Drummer's_&_Fifer's_Guide_(Emmett,_Daniel_Decatur)`, file `PMLP1013283-b-e-guide.pdf`, 96 pp., 6.11 MB | public domain → free | **metadata reached, PDF not downloaded** |
| R38 | **Hart, Col. H. C., _Col. H.C. Hart's New and Improved Instructor for the Drum, with Original Notation_** | book, 1860 (the manual R04 dates 1862) | primary | archive.org id `colhchartsnewimp00hart`, OCR `_djvu.txt`, 44 457 B | public domain → free | **reached in full**; four-primitive alphabet, §2.3b |
| R39 | **Nevins, William (with A. J. Vaas), _Army Regulations for Drum, Fife and Bugle_** | book, 1864 | primary | archive.org id `armyregulationsf00nevi`, OCR `_djvu.txt`, 28 631 B | public domain → free | **reached in full**; the 30-item "Drum School" gamut, §2.3b |
| R40 | **Greissinger, F. Henri, _Instructions for the Trumpet and Drum_** | book, 1900 | primary | archive.org id `instructionsfor00smitgoog`, OCR `_djvu.txt`, 45 877 B | public domain → free | **reached in full**; the `t/f/d/r` + count encoding, §2.3c |
| R41 | **Straight, Edward B., _Straight's Modern Syncopated Rhythms for Drums_** | book, 1922 | primary | archive.org id `StraightsModernSyncopatedRhythms`, OCR `_djvu.txt`, 180 676 B | public domain → free | **reached in full**; drag-vs-press by attack count, 1922 implement list, §2.3c |
| R42 | Peinkofer, Karl / Tannigel, Fritz, _Handbook of Percussion Instruments_ (English translation of N17) | handbook, 1976 | normative-in-German, in translation | archive.org ids `handbookofpercus0000pein`, `handbookofpercus0000karl` | in-copyright, lending-restricted → cite-only | **located, not opened** — this is the reachable route to N17 |
| R43 | **Arsenault, Frank, _Wm. F. Ludwig Presents The 26 Standard American Drum Rudiments and Selected Solos_**, Ludwig Drum Company, 1958 | LP, 1958 | **normative** — NARD's own official recording, made by a NARD president | archive.org id `lp_wm-f-ludwig-presents-the-26-standard-ameri_frank-arsenault`; **item metadata carries the full 33-track list** | recording in copyright; the **track titles are the deliverable** → cite-only | **reached** via `archive.org/metadata/<id>`; §2.2b |
| R44 | _Corps Style Snare Drum Dictionary: A Complete Reference Guide … Through The Use Of American And Swiss Rudiments_, Alfred Publishing, 1981 | dictionary, 1981 | secondary, but a **dictionary** — the genre this bucket most needs | archive.org id `corpsstylesnared0000unse`, ISBN 9780739023228 | in-copyright, lending-restricted → cite-only | **located, not opened**; the likeliest place to find `back stick` and `gock` defined |
| R45 | Retzel, Frank / Adler, Henry / McKenzie, Ted, _Buddy Rich's Modern Interpretation of Snare Drum Rudiments_, Amsco | book | secondary | archive.org id `buddyrichsmodern0000fran`, ISBN 9780825634659 | in-copyright, lending-restricted → cite-only | located, not opened |

### 1.2 Reached only as an abstract (paywall)

| # | Source | Locator | What the abstract yields |
|---|---|---|---|
| R35 | PAS, "The Rudiments" (Marching Percussion Committee) | `https://pas.org/publication-articles/the-rudiments/` | verbatim: the committee "compiled an 'International Drum Rudiment' proposal, including the '26 Standard American Drum Rudiments,' a variety of international rudiments, and **certain changes in terminology**" |
| R36 | Spalding, Dan C., "Revising the Rudiments: A Conservative Approach" | `https://pas.org/publication-articles/revising-the-rudiments-a-conservative-approach/` | a rival model of **5 essential + 22 additional** rudiments exists inside PAS's own journal |
| R37 | Viña, Karlyn R., "An Analytical Approach To Rudiments", _Educators' Companion_ vol. 7, Fall 2019 | `https://pas.org/publication-articles/an-analytical-approach-to-rudiments/` | PAS names **four** basic stroke types: full, down, up, tap |

### 1.3 Named but NOT reached

| # | Source | Type / era | Why it matters | Outcome |
|---|---|---|---|---|
| N01 | Moeller, Sanford A., _The Art of Snare Drumming_ / _The Moeller Book_ (1925, reissued 1950) | book, primary | the codifying text for the whipping technique and for the two right-hand grips | not online; in print |
| N02 | Stone, George Lawrence, _Accents and Rebounds_ (1961) | book, primary | the stroke-type system (full/down/up/tap) is usually traced here | copies on academia.edu; not fetched, licence unclear |
| N03 | Stone, George Lawrence, _Stick Control_ (1935) | book, primary | the sticking-permutation vocabulary R22c builds on | in print |
| N04 | **Berger, Fritz R., _Das Basler Trommeln. Sein Werden und Wesen_**, Trommel-Verlag Basel 1928 | book, primary | **the** source for Basel nomenclature and the notation still used | in print (Musik Hug, Percussion Brandt); no digitisation found |
| N05 | Berger, Fritz R., _Instructor for Basle Drumming_ / _Méthode Baloise de Tambour_ (1964) | book, primary | the export-notation edition | in print |
| N06 | Benson, Allen C., _Details of the Swiss Basle Style of Drumming_ (1980) | book, secondary | the main English-language Basel description | only on pdfcoffee (403) |
| N07 | Hessler, Claus, _Camp Duty Update_, Alfred Music 2017 | book, primary | supplies the working definition of "rudiment" quoted by R04 | in print |
| N08 | **Percussion Creativ, _Rudimental Codex_ (42 rudiments)** | standard proposal, German/French/Basel | the only modern attempt at a trilingual normative list; submitted to UNESCO | **no reachable URL found**; `percussion-creativ.de/rudimental-codex/` → 404 |
| N09 | Bloom, Ryan Alexander, _Encyclopedia Rudimentia_, Hudson Music 2019 | book, secondary | the most complete cross-cultural rudiment concordance in print | in print |
| N10 | Weinberg, Norman, _Guide to Standardized Drumset Notation_, PAS (ISBN 9780966492811) | standard, current | PAS's own drumset notation legend, adopted by Finale, Sibelius and Dorico | in print; no open copy |
| N11 | Cameron, Clayton, _Brushworks: The New Language for Playing Brushes_ | book+CD, primary | the named brush-stroke rudiment system | in print |
| N12 | Thigpen, Ed, _The Sound of Brushes_ | book+CD, primary | the other named brush system | in print |
| N13 | Hazilla, Jon, _Mastering the Art of Brushes_, Berklee Press 2000 | book, primary | source of the ten concepts excerpted in R22b | in print |
| N14 | Jones, Philly Joe, _Brush Artistry_ | book, primary | source of the "Palm Up" stroke described in R22d | out of print 30+ years |
| N15 | Ashworth, Charles Stewart, _A New, Useful and Complete System of Drum Beating_, 1812 | book, primary | first use of the word "Rudiments" for drum patterns | not on archive.org; modern transcription by Bloom in print |
| N16 | Tourte, Robert, _Méthode de tambour et caisse claire d'orchestre_, 1946 (CNSM Paris) | book, primary | the official French conservatoire list R21 is derived from | in print |
| N17 | Peinkofer, Karl / Tannigel, Fritz, _Handbuch des Schlagzeugs. Praxis und Technik_, Schott 1981, pp. 84–85 | handbook, normative-in-German | the standard German percussion handbook, cited by R14 | in print |
| N18 | _Kurze Anweisung zum Trommel-Spiel_, Berlin 1777 (G. L. Winters Witwe) | manual, primary | the ~14-rudiment Prussian system (`Druckruf`, `Doppelwirbel`) | not digitised at a reachable URL |
| N19 | _Tambour-Ordonnanz für die eidgenössischen Truppen / Schweizerische Infanterie_, 1728…1964 (15 documents) | regulations, primary | the Swiss Ordonnanz system, ~32 rudiments | R25 links them only via Google Drive folders |
| N20 | Hessler, Claus, "Swiss Rudiments – Basel Drumming", Modern Drummer, parts 1–3 (2016–2017) | magazine, secondary | the best English exposition of Basel names | paywalled |
| N21 | _Scottish Drumming Rudiments_ sheet (46 rudiments) | standard | a third national list with its own names (`trizzlet`, stroked rolls to 25) | no reachable copy |
| N22 | Drumlines.org, _128 Hybrid Rudiments_ (arr. Ratamaswiss) | glossary PDF | the most-cited hybrid list | 403 direct, 403 via Wayback |
| N23 | snarescience.com "Percussion Dictionary" and "Drum Terminology" threads | forum glossary | source of `gock`/`sprock` synonymy | HTTP 500 on both |
| N24 | lebendige-traditionen.ch, "Basler Trommeln" dossier (DE and FR) | government heritage inventory | an official Swiss description of the tradition | HTTP 502 on both language versions |
| N25 | web.archive.org snapshot content | — | the fallback for every 403 above | **availability API works, content fetch returns proxy 403** |
| N26 | iatdrummers.com "History" | association | the IATD counter-position to the PAS 40 | proxy 502 |
| N27 | Wilcoxon, Charles, _All-American Drummer_ / _Modern Rudimental Swing Solos_ | books, primary | mid-century rudimental extension | in print |
| N28 | Dawson, Alan, "Rudimental Ritual" | curriculum, primary | the Berklee kit application of the rudiments | in print |
| N29 | Freytag, _Rudimental Cookbook_ (1993); Delucia, _Percussion Discussion_ (1995); Wooton, _Rudimental Remedies_ (2010); Bachman, _Rudimental Logic_ (2010) | books, primary | where hybrid naming actually happened | in print |

**Register totals:** 45 sources reached in full, as an abstract or as catalogue metadata, and
29 named and not reached — 74 distinct sources, 78 register rows (R22 carries four
sub-articles). Ids R35–R37 sit in §1.2 and R38–R45 in §1.1 because the latter were added after
the register was first closed; ids are never renumbered.

Two access facts worth carrying forward: `web.archive.org` **content** is unreachable from
this environment even though its availability API is not, and
`archive.org/download/<id>/<id>_djvu.txt` **is** reachable — that is how R03, R38, R39, R40
and R41 were obtained, and it is the cheapest route to any other pre-1929 drum manual.

---

## 2. Extracted terminology (round B)

### 2.1 The PAS 40, verbatim, with NARD membership

Locator: R01, single-sheet PDF, both pages. Headings and spellings are exactly as printed,
including the inconsistent `#` in the drag paradiddles and the hyphen in `Paradiddle-diddle`.
`*` reproduces the sheet's own mark, whose legend reads verbatim:
*"These rudiments are also included in the original Standard 26 American Drum Rudiments."*
The asterisk count on the sheet is 27, of which one is the legend — **26 marked rudiments**,
which is the arithmetic check that the sheet's own claim holds.

| # | Name as printed | Group | NARD 26 |
|---|---|---|---|
| 1 | Single Stroke Roll | I.A Single Stroke Roll Rudiments | * |
| 2 | Single Stroke Four | I.A | |
| 3 | Single Stroke Seven | I.A | |
| 4 | Multiple Bounce Roll | I.B Multiple Bounce Roll Rudiments | |
| 5 | Triple Stroke Roll | I.B | |
| 6 | Double Stroke Open Roll | I.C Double Stroke Open Roll Rudiments | * |
| 7 | Five Stroke Roll | I.C | * |
| 8 | Six Stroke Roll | I.C | |
| 9 | Seven Stroke Roll | I.C | * |
| 10 | Nine Stroke Roll | I.C | * |
| 11 | Ten Stroke Roll | I.C | * |
| 12 | Eleven Stroke Roll | I.C | * |
| 13 | Thirteen Stroke Roll | I.C | * |
| 14 | Fifteen Stroke Roll | I.C | * |
| 15 | Seventeen Stroke Roll | I.C | |
| 16 | Single Paradiddle | II. Diddle Rudiments | * |
| 17 | Double Paradiddle | II | * |
| 18 | Triple Paradiddle | II | |
| 19 | Single Paradiddle-diddle | II | |
| 20 | Flam | III. Flam Rudiments | * |
| 21 | Flam Accent | III | * |
| 22 | Flam Tap | III | * |
| 23 | Flamacue | III | * |
| 24 | Flam Paradiddle | III | * |
| 25 | Single Flammed Mill | III | |
| 26 | Flam Paradiddle-diddle | III | * |
| 27 | Pataflafla | III | |
| 28 | Swiss Army Triplet | III | |
| 29 | Inverted Flam Tap | III | |
| 30 | Flam Drag | III | |
| 31 | Drag | IV. Drag Rudiments | * |
| 32 | Single Drag Tap | IV | * |
| 33 | Double Drag Tap | IV | * |
| 34 | Lesson 25 | IV | * |
| 35 | Single Dragadiddle | IV | |
| 36 | Drag Paradiddle #1 | IV | * |
| 37 | Drag Paradiddle #2 | IV | * |
| 38 | Single Ratamacue | IV | * |
| 39 | Double Ratamacue | IV | * |
| 40 | Triple Ratamacue | IV | * |

Practice instruction printed on the sheet, verbatim: *"All rudiments should be practiced:
open (slow) to close (fast) to open (slow) and/or at an even moderate march tempo."*
Copyright line: *"Copyright © 1984 by the Percussive Arts Society™"*.

From R02, verbatim: *"This listing was an outgrowth of a five-year project compiled by the
PAS International Drum Rudiment Committee, a highly select group of percussionists,
organized and chaired by Jay Wanamaker."*

### 2.2 The NARD 26 (1933) and its two tiers

Locators: R23 (history and the reason for the split), R13 and R04 (the two lists).

**Thirteen "essential" rudiments** — the membership test: double stroke open roll, five
stroke roll, seven stroke roll, flam, flam accent, flam paradiddle, flamacue, drag (half drag
or ruff), single drag tap, double drag tap, double paradiddle, single ratamacue, triple
ratamacue.

**Second thirteen** — single stroke roll, nine stroke roll, ten stroke roll, eleven stroke
roll, thirteen stroke roll, fifteen stroke roll, flam tap, single paradiddle, drag paradiddle
No. 1, drag paradiddle No. 2, flam paradiddle-diddle, lesson 25, double ratamacue.

R23, verbatim: *"It should not be assumed that the purpose of this group was to originate or
invent any of the Standard American Drum Rudiments, but was to review the early rudiments
that first came from Switzerland 200 years previously, at a time when music notation was not
standardized."* Founded 20 June 1933 at the American Legion National Convention, Chicago; 13
named founders including William F. Ludwig and George Lawrence Stone.

**The fourteen added in 1984** (R04): single stroke four, single stroke seven, multiple
bounce roll, triple stroke roll, six stroke roll, seventeen stroke roll, triple paradiddle,
single paradiddle-diddle, single flammed mill, pataflafla, Swiss Army triplet, inverted flam
tap, flam drag, single dragadiddle.

### 2.2b The NARD 26 in NARD's own words, 1958

R24 (nard.us.com) prints the 26 names as raster images, so the association's own spelling could
not be read there. It was recovered instead from the item metadata of NARD's **official
recording**: Frank Arsenault — then NARD president — recorded the 26 for the Ludwig Drum
Company in 1958, one rudiment per track, in NARD's own order (R43). The track list *is* the
list, and the numbering confirms the 13 + 13 split: tracks 1–13 are the essentials, 14–26 the
second thirteen, 27–33 are solos.

| # | Track title as issued, 1958 | PAS 1984 name (R01) |
|---|---|---|
| 1 | **The Long Roll** | Double Stroke Open Roll |
| 2 | The Five Stroke Roll | Five Stroke Roll |
| 3 | The Seven Stroke Roll | Seven Stroke Roll |
| 4 | The Flam | Flam |
| 5 | The Flam Accent | Flam Accent |
| 6 | The Flam Paradiddle | Flam Paradiddle |
| 7 | The Flamacue | Flamacue |
| 8 | **The Ruff** | Drag |
| 9 | **The Single Drag** | Single Drag Tap |
| 10 | **The Double Drag** | Double Drag Tap |
| 11 | The Double Paradiddle | Double Paradiddle |
| 12 | The Single Ratamacue | Single Ratamacue |
| 13 | The Triple Ratamacue | Triple Ratamacue |
| 14 | The Single Stroke Roll | Single Stroke Roll |
| 15 | The Nine Stroke Roll | Nine Stroke Roll |
| 16 | The Ten Stroke Roll | Ten Stroke Roll |
| 17 | The Eleven Stroke Roll | Eleven Stroke Roll |
| 18 | The Thirteen Stroke Roll | Thirteen Stroke Roll |
| 19 | The Fifteen Stroke Roll | Fifteen Stroke Roll |
| 20 | The Flam Tap | Flam Tap |
| 21 | The Single Paradiddle | Single Paradiddle |
| 22 | The Drag Paradiddle No. 1 | Drag Paradiddle #1 |
| 23 | The Drag Paradiddle No. 2 | Drag Paradiddle #2 |
| 24 | The Flam Paradiddle-Diddle | Flam Paradiddle-diddle |
| 25 | **Lesson 25** | Lesson 25 |
| 26 | The Double Ratamacue | Double Ratamacue |

Solo tracks 27–33: Connecticut Halftime, Downfall Of Paris, The Three Camps, Hell On The
Wabash, Old Dan Tucker, Grandfather's Clock, The General.

**This settles what R35's abstract only hints at.** PAS's own committee said it made "certain
changes in terminology"; comparing 1958 with 1984 shows exactly four:

| 1958 (NARD) | 1984 (PAS) | Nature of the change |
|---|---|---|
| The Long Roll | Double Stroke Open Roll | descriptive-of-*sound* → descriptive-of-*sticking* |
| **The Ruff** | **Drag** | one name displaced another for the same figure (see §4.1, §5.1) |
| The Single Drag | Single Drag **Tap** | the terminal stroke added to the name |
| The Double Drag | Double Drag **Tap** | same |

`No. 1` / `No. 2` also became `#1` / `#2`, and `Paradiddle-Diddle` lost its second capital.
Note that `Lesson 25` survived both revisions unchanged, still carrying Strube's 1870 lesson
number (§2.3) — a rudiment named after its position in a book that almost nobody using the
name has read.

### 2.3 Strube 1870 — the pre-standard layer, from the source

Locator: R03, OCR text. Strube is the ancestor list: R04 states the NARD 26 is "largely based
on Strube's 25 rudiments from 1870, with a single addition, the single stroke roll".

Confirmed **in the primary text**:

| Locator (line in `_djvu.txt`) | Verbatim | Why it matters |
|---|---|---|
| 299 | "The first lesson of the Pupil will be the Long Roll or Double-Stroke Roll." | `long roll` = `double stroke roll` is an 1870 synonymy, not a modern one |
| 301–302 | "The Pupil will endeavor to beat in the **centre of the head, within a circle of about two inches**" | a 19th-century statement of the `position` axis, in inches |
| 288–290 | left stick "held in the hollow of the hand between the thumb and first two fingers"; right stick with "the little finger should press it harder than the rest" | traditional grip with the **little-finger fulcrum** — the same "vintage grip" R08 says Moeller documented |
| 306, 324, 348, 393, 470 | "LESSON, No. 1 … THE LONG ROLL", No. 2 "THE FIVE-STROKE ROLL", No. 3 "THE SEVEN-STROKE ROLL", No. 4 "THE NINE-STROKE ROLL", No. 5 "THE TEN-STROKE ROLL" | the "Lesson, No. X" framing is why PAS #34 is still called **Lesson 25** — it is the 25th lesson, which Strube left unnamed (R04 note) |
| 855–864 | "all left hand strokes … are indicated by notes written in the E, or upper space of the Staff, and … all right hand strokes … in the F, or lower space. All Rolls, commencing with the left and ending with the right hand, are indicated by notes written in the C" | **hand identity is encoded in staff position**, i.e. in the notation itself |
| 867–974 | "THE FIVE-STROKE ROLL … commencing and ending with the left hand, will be known as the **Left Hand Five-stroke Roll**"; likewise Right Hand Five-stroke, Left/Right Hand Nine-stroke | **lead hand is part of the rudiment's name** |
| 1028–1087 | "THE FLAM … The **Right Hand Flam** will be written thus … The **Left Hand Flam** …" | same for the flam |
| 1134 | "THE **OPEN FLAM**" as a separately named item | openness is applied to a grace ornament, not only to rolls or hi-hats |
| 1158–1189 | "THE RUFF … **Left Hand Ruff** … **Right Hand Ruff**" | ruff is a first-class 1870 name; PAS demoted it to a parenthetical of `Drag` |
| 1220–1306 | "THE SINGLE DRAG", "THE DOUBLE DRAG", each in Left Hand and Right Hand forms | |
| 1318–1443 | Single and Double Ratamacue, each Left Hand and Right Hand | |

The OCR of the engraved rudiment titles is partial (they are images in a lithographed score),
so the 25-item list is taken from R04's transcription and only the items above are confirmed
from the scan itself. Marked accordingly below.

### 2.3b The Civil War layer — two manuals that name the *sound*, not the pattern

This is the richest find of the bucket for KITWARP specifically, because both manuals below
were written before any standard list existed and both therefore had to name the elementary
sound events from scratch. Both were obtained in full from archive.org OCR.

#### Hart 1860 (R38) — a four-character alphabet

Hart states the design decision verbatim (lines 66–76):

> "all Blows, Taps, Flams, or Single Beats have but **one length of sound** on the Drum,
> therefore I would use but **four principal characters** in drumming, from which originate
> all the beats necessary to a perfect performance of any piece of music on the Drum, to wit,
> **a blow, a flam, a three roll closed, and a rest**"

That is a pivot vocabulary from 1860: one plain stroke, one 2-attack ornament, one
3-attack ornament, and silence. Every other figure in the book is said to *originate from*
these four.

Hart then grades each character on two independent scales (lines 133–166):

| Character | Weight / duration grade | Hart's own word |
|---|---|---|
| full flam / full blow / three roll closed / full rest | quarter-note weight | "beat **heavy**" |
| hard, quick flam / hard, quick blow / half rest | eighth-note weight | "hard, quick" |
| full **open** flam / full **open** blow / full **open** three roll | quarter-note duration | "executed **soft and light**" |
| small open flam / small open blow | eighth-note duration | soft and light |

**`open` in Hart means soft, not un-closed.** The notation carries it through: a soft roll is
written with an "**open figure**" numeral — an open 7, an open 5, an open 9, an open 11 — while
the same roll played normally uses a solid numeral. See §4.1.

Other Hart facts with locators:

| Fact | Locator |
|---|---|
| "beat square upon the head of the drum, and **as near the center of the head as possible**, make **no drawing strokes or sideway beats** in no case whatever, although it has been recommended by many professional teachers of drumming" | lines 116–121 — a striking-position rule *and* a documented disagreement about the lateral stroke |
| all motion "by turning or rolling the wrists, and not by motions of the arms or shoulders" | lines 124–128 |
| "The **Three Roll open** is performed by striking two hard, quick blows with the left, then one full blow with the right … until perfected in a **closed three Roll**", "the two first blows appearing to be nearly silent, as they in fact are when closed to the fine" | Lesson III — the drag/ruff as an **open↔closed continuum**, not two figures |
| "The **Flam** is performed by striking a **very soft, fine blow** with one hand, and a **full heavy blow** immediately following with the other" | Lesson IV — the flam defined purely as a dynamic relation between two attacks |
| "the **full and half Flam**, both heavy and light" | Lesson IV — a two-step size grade on the flam itself |
| "Those representing the **left hand flams are on the upper line**, and those for the **right hand on the lower line**" | Lesson IV — hand encoded in notation, as in Strube |
| "A **light accent** should be placed on the **last blow** of the Five Roll, as well as **all other Rolls** used" | Lesson VI |
| named rolls: two Stroke or Long Roll, Single Stroke (the "Single Blow Exercise"), Three Roll (open and closed), Seven Roll, Five Roll, Nine Roll, Eleven Roll, Fifteen Roll | Lessons I–VIII |
| named beats that did **not** survive into any modern list: "**Compound Double Drag Beat**", "**Triple Compound Drag Beat, or the Seven Quick Single Blows**", "**Paradiddle Drag Beat**", "**Reversed Flam Paradiddle**", "**Double Drag Beat, Three Roll**" | lines 909–1013 |

#### Nevins 1864 (R39) — the 30-item "Drum School" gamut

The full numbered gamut, verbatim spelling (the drum notation is printed on the lower of two
staves, ordinary notation on the upper):

1 LONG ROLL (written out) · 2 FIVE STROKE ROLL · 3 SEVEN STROKE ROLL · 4 SEVEN STROKE ROLL:
Faint, or Soft · 5 NINE STROKE ROLL · 6 TEN STROKE ROLL · 7 ELEVEN STROKE ROLL ·
**POING STROKES:** 8 Hard · 9 Middling Hard · 10 Faint or Soft · 11 FLAMS · 12 FAINT FLAMS ·
13 STROKE & FLAMS · 14 FLAMS & STROKE · 15 FLAMS PARADIDLE · 16 SINGLE PARADIDLE ·
17 DOUBLE PARADIDLE · **18 TRIPLE PARADIDLE** · 19 FLAMS PARADIDLE DIDLE · 20 HALF DRAG ·
21 FULL DRAG · 22 SINGLE DRAG · 23 DOUBLE DRAG · **24 SLOW SAG** · 25 RUFFS ·
26 SINGLE ROTAMACUE · 27 DOUBLE ROTAMACUE · 28 Quick · 29 Half as Quick · 30 TAPS.

Nevins's own definitions (lines 200–235), verbatim:

| Item | Definition |
|---|---|
| striking position | "Strike the Drum **about an inch above the center**." |
| No. 8 | "the **Poing Stroke**, means a sudden, **hard, short** beat." |
| No. 9 | "moderately hard." |
| No. 10 | "**soft, long, drawing stroke**." |
| No. 11 | "the **Flam** is produced by one hand following the other as quickly as possible. Saying, '**P'lum, p'lum, p'lum**,' gives some idea of the Flam." |
| No. 12 | "like No. 11, but with **soft strokes**." |
| No. 25 | "**RUFFS** … composed of **three Poing Strokes**, as follows: right, left, right — left, right, left" |
| No. 26 | "in beating these three beats, the hands change as quickly as possible." |
| No. 30 | TAPS: "a signal for the front to advance slow" |

Three findings from Nevins that bear directly on the pivot model:

1. **A named three-level dynamic scale, 1864: Hard / Middling Hard / Faint or Soft**, applied
   independently to the plain stroke (8, 9, 10) *and* to the flam (11 vs 12 "FAINT FLAMS")
   *and* to a roll (3 vs 4 "SEVEN STROKE ROLL: Faint, or Soft"). Dynamic is treated as an
   axis orthogonal to the figure — exactly as KITWARP treats it.
2. **`Poing Stroke` is a name for the stroke's envelope**, not for a pattern: "sudden, hard,
   short". Its opposite, No. 10, is "soft, long, **drawing**" — the very lateral gesture Hart
   forbade four years earlier. Two Civil War manuals in direct disagreement about whether a
   drawing stroke is legitimate technique.
3. **`TRIPLE PARADIDLE` is item 18 of an 1864 American army manual.** PAS lists it among the
   fourteen rudiments *added* in 1984 (§2.2), and R04 frames those additions as drum-corps,
   European or contemporary. At least this one is neither: it is older than the NARD 26 that
   omitted it.

`SLOW SAG` (No. 24) appears in no later list reached and no source defines it; recorded as an
unexplained 1864 name.

### 2.3c Greissinger 1900 and Straight 1922 — an encoding and a drum-set hinge

#### Greissinger 1900 (R40) — a four-letter event code with a numeric attack count

The most directly relevant single sentence found in this bucket. Verbatim, from the
Explanations page (line 5034):

> "**t** indicates tap; **f**, flam; **d**, drag; **r**, roll. The **figures under the rolls
> indicate the number of strokes in each roll**."

A US military manual of 1900 encodes drum events as a **one-letter event type plus a numeric
attack count** — which is precisely the `ornament` + count shape §5.3 finding 1 recommends,
arrived at independently 126 years earlier.

| Fact | Verbatim / locator |
|---|---|
| sticking letters | "The letter **L** under a note is for the left hand, **R** is for the right" (line 4110) — the earliest R/L attestation found here |
| lead-hand default | "**Every roll or beat should begin with the left hand**, except those which are termed from hand to hand, which commence with the left and follow in succession" (line 4100) |
| striking position | "Care should be taken that the sticks strike **near the middle of the drum-head**" (line 4089) |
| accent inside the double | "Slightly **accent the second stroke of each hand**" (line 4105) |
| onomatopoeia | the open roll is "called by drummers the '**Mammy-Daddy**'" (line 4099) — the American cognate of German `Mama-Papa` (R15) and French `papa-maman` (R21) |
| **Eight-stroke Roll** | "The Eight-stroke Roll is from hand to hand" (line 4221) — confirms R06's claim that the even-numbered rolls exist in published sources; it is on no modern list |
| named figures | The **Open Flam**, The **Flam and Stroke**, The **Open Drag**, The **Close Drag or Half Drag**, The Single Drag, The Double Drag, The **Drag Paradiddle**, The **Stroke and Drag Paradiddle**, The **Stroke and Single Drag** (lines 4289–4613) |

Note the pairing **Open Drag / Close Drag**: the drag is again a single figure with an
open↔closed axis, third independent attestation after Hart 1860 and R04.

#### Straight 1922 (R41) — where the rudimental vocabulary meets the kit

| Fact | Verbatim / locator |
|---|---|
| **drag vs press, by attack count** | "**Drags are not press rolls. A Drag is ended while a Press is made with one stick only. You must hear the two taps clear in a drag** and you must learn to play them with either hand." (line 1782) — the distinguishing feature is stated as *countability*, not as speed |
| lead hand in the name | "it is a **Left hand Drag**"; "All the taps before the regular large note is made with Left hand" (line 1787) |
| three-stroke roll as a live alternative | "instead of using the **three stroke roll** in a gallop, use the Left hand Drag" (line 1797) |
| implements, 1922 | "Sand-blocks, **Clog-mallets**, **Jazz-sticks** or **Leather straps**" (line 13078); "**Tympanie sticks**" (line 9951) — a 1922 attestation for v0.1's `jazz-stick` |
| damping | "Use **muffled drums** when you Jazz, not too loud" (line 4965); "both drums **muffled**" (line 6565) |
| the aux family, 1922 | "**traps**" as the collective noun; "two Tom-Toms and Cymbal, two Cow-Bells and Wood-Block" (line 119) |
| independence as the new problem | "We have to work on three different articles at once — Bass Drum, Snare Drum muffled and Tom-Tom at the same time and play three different beats" (line 117) |

### 2.4 Per-note ornaments, with attack counts

This is the table the pivot model actually needs: the rudiments are *patterns*, but a small
set of them are *single-note qualifiers* with a definite number of attacks.

| Term | Attacks | Physical description | Locator |
|---|---|---|---|
| **Flam** | 2 | one grace note on the opposite hand immediately before the primary; `rL` or `lR`; intended to sound as one broadened note | R04 §Terminology, §Flam rudiments |
| **Open flam** | 2 | flam with an audibly wider grace-to-primary gap; listed separately in older and some European systems | R03 line 1134; R04 §Flam |
| **Drag** (= half drag = PAS `ruff`) | 3 | two *diddled* (same-hand) grace notes before the primary; `llR` / `rrL` | R04 §Drag; R01 #31 "Two diddled grace notes before a tap" |
| **Ruff** (historic / American 3-stroke ruff) | 3 | two *single-stroked, alternating* grace notes before the primary; `rlR`. Confirmed in an 1864 primary: Nevins's No. 25 RUFFS is "composed of three Poing Strokes … right, left, right — left, right, left" | R04 §Ruff; **R39 line 231** |
| **4-stroke ruff** | 4 | three single grace notes before the primary; `lrlR` | R04 §Ruff |
| **Charge stroke** | 2 | an open flam in which the first note **precedes** the downbeat and the downbeat falls on the second; French form `Lr`/`Rl`, Swiss form `LR`/`RL` | R04 §Charge stroke |
| **Coup de charge** (French) | 2 | explicitly *"l'inverse du fla"* — the weak stroke **follows** the accented one | R21 item 7 |
| **Double stop** (= flat flam = unison = "both") | 2 simultaneous | both hands land at exactly the same instant, no space; "not considered an American rudiment on any common list, but is a staple of several European systems" | R04 §Double stop |
| **Diddle** | 2 | a double stroke at the prevailing subdivision | R04 §Diddle |
| **Cheese** | 3 | a diddle with a grace note, i.e. a flammed diddle | R04 §Hybrid rudiments |
| **Herta** | 3 | a drag played with alternating rather than diddled sticking | R04 §Hybrid rudiments |
| **Deadstick grace note** (Scottish "drag") | 2 | a flam whose grace note is played staccato, the stick not rebounding | R04 §Drag |
| **Ghost note** | 1 | a tap or up-stroke deliberately below the surrounding dynamic; the inverse of an accent | R05 §Other strokes |

R04 records the terminological demotion verbatim: *"the 3 Stroke Ruff and 4 Stroke Ruff are
not officially listed on the NARD or PAS rudiment sheets and the term Drag has eclipsed Ruff
(or Rough) for the double stroked rudiments, in both open or closed execution, according to
the current PAS standard terminology."*

### 2.5 The roll family, distinguished physically

| Term | Attacks per hand-motion | Distinguishing physical fact | Locator |
|---|---|---|---|
| Single stroke roll (`Einzelschlagwirbel`, `redoble de golpe único`) | 1 | alternating single strokes; indeterminate speed and length | R01 #1; R06; R15 |
| Double stroke open roll (`long roll`, `Doppelschlagwirbel`, `roulement`, `bâton rompu`) | 2 | first stroke wristed, second driven by rebound + finger pressure; each stroke individually audible | R06; R14; R21 item 3 |
| Triple stroke roll (`French roll`) | 3 | three strokes per hand; each may be bounced or wristed | R04 §Multiple bounce |
| Multiple bounce roll (`buzz`, `closed`, `press`, `Presswirbel`) | indeterminate | the stick is *pressed* into the head so it rebounds an uncounted number of times; the count cannot be specified | R04; R06; R15; R16 |
| Numbered rolls 5–17 | measured | a fixed **total** attack count with a terminal accent: odd numbers take one accent, even numbers two | R06 |
| 3-stroke roll | 3 | "the shortest possible open double stroke roll, but is commonly referred to by the specific name **Drag**, **Ruff**, or **Half Drag**" | R06, verbatim |
| Fulcrum / gravity / freehand roll | 2 per arm motion | the **rim** momentarily replaces the finger fulcrum: one arm stroke produces two head contacts | R06 §Fulcrum roll; R15 |
| One-handed roll (push-pull) | 2 per motion | wrist supplies one stroke, fingers the other, no rim contact | R15; R05 |

R06 also records which numbered rolls exist outside the PAS set: *"The 4 Stroke, 8 Stroke, 12
Stroke, 14 Stroke, and 16 Stroke are rare but all exist in official published sources. The
Scotch Pipe Band style has a rudimental roll up to 25 strokes."* The 8-stroke roll "is present
in the Moeller Book from 1925 but is lost in later publications".

Cross-cultural names for the *closed* roll specifically (R06, verbatim list):

| Tradition | Name |
|---|---|
| American | multiple bounce roll, triple stroke roll, crushed ruff |
| German | **Druckruf** |
| Scottish | buzz roll, stroked rolls 5 through 25, **trizzlet** |
| Dutch | **Ra stroke** |
| Mexican | **Rau Tau**, **Redoble** |
| Spanish | **Redoble de Zumbido** |
| Bajoaragonés | **Los Rufaos** |
| Eporedian (Ivrea, Italy) | **Rullo** |

R15 gives the German four-way classification directly: `Offener Wirbel` (open stroke roll),
`Geschlossener Wirbel` (closed roll / buzz roll / **Presswirbel**), `Einhändiger Wirbel`
(one-handed / gravity roll), `Einzelschlagwirbel` (single stroke roll) — and states that in
German and Austrian wind-band march music the closed roll is used *exclusively*, while in drum
corps and rudimental drumming the open roll is used almost exclusively.

R14 names the three German stroke primitives: **Einzelschlag**, **Doppelschlag**,
**Pressschlag**, citing Peinkofer/Tannigel 1981 pp. 84–85; and names **Mühle** as the
preparatory exercise for the double-stroke roll, with **Mama-Papa / Papa-Mama** as its
onomatopoeic alias (R15).

### 2.6 Stroke-type systems, and who codified each

| System | Named strokes | Codifier / locator |
|---|---|---|
| **Four basic strokes** | full, down, up, tap (low stroke) | PAS's own teaching text names exactly these four (R37); R05 adds a fifth, the **buzz stroke** |
| Positional definition | three wrist positions — **up position** (max height), **tap position** (min height), **rest position** (still) — every basic stroke is a combination of two of them | R05 §Basic strokes |
| **Moeller method** (= Moeller technique, whipping technique) | the same four strokes driven by a **dual-fulcrum whipping / wave motion**; grouped into doubles (up+down) and triples (down+tap+up) | Sanford A. Moeller, _The Art of Snare Drumming_ (N01); taught to Jim Chapin 1938–39 (R08) |
| Moeller's two right-hand grips | the **little-finger (vintage) grip** — fulcrum at the back of the hand, less vibration on loud strokes — and the **thumb fulcrum grip**, better for closed rolls and cymbal rhythms | R08, citing pp. 4 of the Moeller book |
| **Gladstone technique** | **free strokes** with completely uninhibited rebound in **full, half and low** varieties; finger control of the rebound | R05 §Other strokes; contested in R30 — Louis Bellson: *"Billy was the real master and the leading exponent of the finger system"*, Buddy Rich: *"I'm opposed to all that talk about finger control and all that nonsense"*, calling it wrist and forearm motion (Modern Drummer, Dec 1980) |
| **Push-pull** (dual fulcrum) | alternated wrist and finger motions producing two notes per motion | R05; R15 |
| **Freehand / gravity** | the rim is the second fulcrum; named "Freehand Technique" by **Johnny Rabb**, coined 1995, published as _The Official Freehand Technique_ | R06 §Fulcrum roll; R15 names Rabb explicitly |
| Marching **stick heights** | a graded height scale: "regularly used heights range from **3" to 12"**, with **1" and 15"** being used mostly for visual effect" | R10, verbatim |
| Grips | matched grip with three variants — **German grip** (palms down, wrist and arm, more power), **French grip** (palms inward, fingers, easier dynamics and very soft playing, less power), **American grip** (45°, the compromise) — versus **traditional / classic grip** | R16, verbatim German source |
| Marching cymbal grip | **Garfield grip**, named for the Garfield Cadets | R10 |

### 2.7 Rimshot and rim vocabulary as drummers actually use it

| Term | Physical definition | Who uses it | Locator |
|---|---|---|---|
| **Rimshot** ("normal") | tip/bead about **3 inches (8 cm)** from the rim; rim and head struck together by one stick | kit and marching | R07 |
| **Ping shot** | bead about **1 inch (2.5 cm)** from the rim; high-pitched | marching percussion | R07 |
| **Gock** (also spelled **gawk**) | bead struck at the **centre** of the head while the rim is struck by the **distal shaft near the hand**; lower sound | marching percussion | R07 |
| **Stick shot** (orchestral "rimshot") | one stick laid with its head near the middle of the head and its **shaft pressed against the rim**, struck by the *other* stick; less powerful, easier | orchestral | R07; R12 |
| **Cross-stick** = **rim click** = **side-stick** | tip held against the head near a bearing edge, the stick's **butt** struck against the rim, hand muting the head; dry claves-like click | kit, all genres | R12, verbatim: *"A commonly used alternative way to play the snare drum is known as 'cross-stick', 'rim click', or 'side-stick'"* |
| **Rim click** (marching bass) | strike a **metal bar attached to the rim** | marching bass line | R10 |
| Timbales rimshot | rimshots near the *edge* of the head; R07 states these "sound very different from gocks in marching percussion" | Latin percussion | R07 |
| **"gock" / "shot" / "spock" drums** | the 6″ or 8″ accent drums inside a multi-tenor arc — the *stroke name became an instrument name* | marching tenors | R10, verbatim |
| **Coup de douille** | French: turning the stick round and striking the head with the **butt/ferrule** end | French military drumming | R21, closing note |
| **Back stick / backsticking** | **NOT FOUND** in any source reached. No definition, no attestation. | — | see §6 |

### 2.8 Brush vocabulary

All from R22 unless marked. This is the only bucket area where a full primary journal source
was obtained, so these are quotable definitions rather than glossary paraphrase.

| Term | Physical definition | Locator |
|---|---|---|
| **Rim roll** | the *handle* of the brush rests on rim and head, palm laid on top of the handle, handle rolled back and forth "like rolling out a piece of dough"; the brush "flops" | R22a p. 20 |
| **Rim buzz** | the brush is slapped on the **rim** like a stick rimshot while the wire ends are kept ~1 inch clear of the head; the resulting "flutter" imitates a buzz stroke | R22a p. 20 |
| **Trill** | a **one-handed roll with brushes**: thumbs-up grip, the brush is "shaken" back and forth across the head; **unmetered**, speed set by the dynamic | R22a p. 21 |
| **Staccato/legato circles** | small circles "fill in" between accents in odd groupings (5s, 7s) | R22a p. 21 |
| **Brush double stroke** | the two strokes land at **different points** on the head (A then B) while the stroke is *pulled* toward the body; right hand French/thumbs-up grip rotating clockwise, left hand traditional grip counter-clockwise | R22a p. 23 |
| **Whipped cream roll** | the same pulled-double technique, "made famous by Buddy Rich" | R22a p. 23 |
| **Legato (push) stroke** | brushes **pushed** across the head perpendicular to the player for long legato notes | R22a p. 23 |
| **Palm Up** | Philly Joe Jones's stroke from his book _Brush Artistry_: the right brush is turned "like turning on the ignition", the wires flicked off the head with a quick wrist turn to the palm-up position, "resulting in a **snap**" | R22d p. 18 |
| **Half-note sweep** | Philly Joe's left-hand partner to Palm Up: 7 o'clock → 2 o'clock on beat 2, back to 7 for 3, to 2 for 4 | R22d p. 18 |
| **Clock-face position language** | brush position given as hours (12, 3, 6, 9 o'clock) — the standard way the literature states a *position on the head* | R22b p. 32; R22d |
| **Clockwise vs counter-clockwise circle** | Hamilton: "counter-clockwise circles push away the beat, while clockwise circles physically bring the beat to me" | R22d p. 20 |
| **Windshield wiper** | pejorative for relegating the left hand to a constant automatic sweep | R22d p. 20 |
| **Lateral stroke** | brushes are side-to-side where sticks are up-and-down: *"Brushes generate sound with lateral (or horizontal) strokes across the texture of the drumhead"* | R22a p. 20; R22d |
| **Feathering** | the bass drum played on all four beats at near-inaudible volume beneath brush time | R22b concept 5 |
| **Tips vs fan** | Soph: accents are made "by pressing more of the brush fan onto the head. This produces a darker, heavier sound. When not shading, or accenting, the brushes should be played on their **tips**." | R22c p. 30 |
| **Grip point** | Hazilla concept 3: "Grip the brush **two inches from the wires**" | R22b p. 32 |

Reported by search-result summary only, primary **not** reached — recorded as UNVERIFIED and
attributed so the reconciliation pass can chase them in N11/N12: `Sweep`, `Tight Sweep and
Taps`, `Strumming (Guitar Stroke)`, `Tap-Sweep-Tap (Time Stroke)`, `Silent Sweep` (brush moves
horizontally *off* the head, i.e. a deliberately silent repositioning), `Lift`. Cameron's book
is titled _Brushworks: **The New Language for Playing Brushes**_ (R33), which is itself the
claim that he minted names.

### 2.9 Foot technique

| Term | Physical definition | Locator |
|---|---|---|
| **Heel-down** | heel rests on the footboard; the ankle is the pivot | R09; general |
| **Heel-up** | heel raised off the board, leg mass drives the stroke | R09 |
| **Heel-toe** | **two attacks from one leg motion**: the foot lands flat in a "flam motion" (ball first, then heel) for stroke 1, then hip flexor and calf raise the leg while the foot snaps forward for stroke 2. R09 is explicit that despite the name "it's the ball of the foot (or toes) both times" | R09 |
| **Slide** | heel-up variant: after the first stroke the toes slide up the footboard and press again | search-result summary only, UNVERIFIED |
| **Swivel** | the heel moves laterally (inward with the right foot, outward with the left) without the ball leaving the board, alternating strokes | search-result summary only, UNVERIFIED |
| **Foot chick** (hi-hat) | the pedal closes the cymbals with no stick, producing a short muted "chick" / "chck" | R11, verbatim |
| **Pedal hi-hat** | R11's own standard term: "*pedal hi-hat* refers to parts or notes played solely with the pedal used to strike the two cymbals" | R11 |
| **Foot splash** (hi-hat) | like a chick but the pedal is **released immediately** after contact so the cymbals rebound apart and ring | search-result summary only; **not** attested in R11, see §6 |
| **Cooking** | shuffle figure: struck twice, held closed on the first, opened just before the second, allowed to ring, then closed with a chick | R11, verbatim |
| `halboffen` | German for the half-open hi-hat position, used alongside `offen` and `geschlossen` | R16 |
| Records | Tim Waterson set the WFD double-stroke feet record at **1 407 doubles in 60 seconds** using a hybrid heel-toe | R09 |

R09's attribution of the modern formalisation to James Davenport is single-sourced within a
weakly-cited article; treated as UNVERIFIED.

### 2.10 Sticking systems and how they are written

| Tradition | Symbols | Extra conventions | Locator |
|---|---|---|---|
| American / English | `R`, `L` | lower case = grace notes; `-` = rest | R06 table |
| French | `D` (droite), `G` (gauche) | `-` = silence; every exercise begins on beat 1 and loops *ad libitum* | R21 "Nomenclature" |
| Spanish | `D` (derecha), `I` (izquierda) | `DD`/`II` for doubles, `DIDD` for a paradiddle | R19 §Terminología |
| Italian | `R`, `L` borrowed from English | but "ogni rudimento viene eseguito solitamente **partendo con la mano sinistra**" — the default lead hand is the **left** | R18, verbatim |
| German | `R`, `L`; plus `Führungshand` / `Nichtführungshand` for lead and off hand | R16 |
| Strube 1870 | no letters at all — hand is encoded by **staff position** (left = E space, right = F space, rolls left-to-right = C) and by the **rudiment's name** | R03 lines 855–864 |
| Hart 1860 | left-hand flams on the **upper line**, right-hand on the **lower line** | R38 Lesson IV |
| Greissinger 1900 | "The letter **L** under a note is for the left hand, **R** is for the right" — the earliest letter sticking found here — plus a **default lead hand**: every roll or beat begins with the left | R40 lines 4100, 4110 |
| Greissinger 1900, event code | `t` = tap, `f` = flam, `d` = drag, `r` = roll, with **the number of strokes written under the roll** | R40 line 5034 |
| Pattern-level terms | `alternating` (single stroke), `diddle` (same-hand double at the prevailing rate), `paradiddle` = two singles + a diddle, whose function is explicitly "to switch the **lead hand**" | R04 §Paradiddle |
| `Mill stroke` | "essentially a reversed paradiddle with the sticking `RRLR` or `LLRL` with an accent on the first note" | R04 §Mill stroke |

### 2.11 The French system, named in French

Locator: R21, whose closing note states the list is taken from **Robert Tourte,
_Méthode de tambour et caisse claire d'orchestre_ (1946)**, the Conservatoire National
Supérieur de Musique de Paris method, and that these figures were called **"coups de
baguette"** in France. R21 further records that the elementary distinctions **bâton rond**
(one stroke per hand), **bâton rompu** (two strokes per hand) and **bâton mêlé** (mixed) are
already in Antoine Furetière's _Dictionnaire universel_ of **1690** — 122 years before
Ashworth first wrote "Rudiments".

| French term | Sticking (D=right, G=left) | Meaning / English equivalent |
|---|---|---|
| **coup simple**, **frisé**, old **bâton rond**, onomatopoeia "tapatapa" | `DGDG` | single stroke roll |
| **frisé de 3 / 4 / 5** | `DGD-`, `DGDG--`, `DGDGD---` | single-stroke grace groups; the *frisé de 4* is the single stroke four |
| **roulement**, old **bâton rompu**, "papa-maman", sung as a rolled "Rrrr" | `DDGGDDGG` | double stroke roll |
| **bâton mêlé** | e.g. `DGGDGG` | one hand single against the other's double, asymmetric; used in the *Rigodon d'honneur* |
| **fla** | `D--GD--G` | flam |
| **fla inversé / flafla** | `D--DG--G` | inverted flam |
| **coup de charge** | `DG--DG--` | the inverse of a flam: weak stroke *after* the accent |
| **coup anglais** ("Langlais") | `D--D-G` | flam preceded by a single stroke; the inverted form is what PAS calls *inverted flam tap* |
| **bâtard** | `D--G-G` | flam with a doubled stroke; the chained form is the NARD *flam tap* |
| **ra** (ra de 3 = "tra", 4, 5, 6, 7, 8, 9, 11, each with an inverted form) | e.g. ra de 3 `D-GGD-GG` | measured roll ending on an accent; *ra de 3* = **Drag** / older American **Ruff** |
| **frisé-sauté** | `DGDGD-G-` | |
| **flagada** | flam + two singles + rest | used in *La Marche des éclopés* |
| **patafla** | ternary | = **flam accent** |
| **coups coulés** | "papatala" / "tatatala" | two singles plus a coup de charge |
| **pataflafla** | `D--G-DG-DG--` | the PAS *pataflafla* keeps its French name |
| **moulin** | `DGDDGDGG` | = **single paradiddle** |
| **volant** | `DGDGDDGDGDGG` | = **double paradiddle** |
| **ra de 5 détaillé** | `DGGDD GDDGG` | in NARD but not in PAS |
| **raté-sauté** | `D-GGD-G-` | the 3-stroke form "is only called **Lesson 25** in the NARD rudiments" |
| **rigodon** | `D-GGD-G-DDG-` | = **single drag (tap)** |
| **coup de la Diane** | `D---GGD-G-DDG---DDG-D-GG` | = **double drag (tap)** |

R21 also records physical actions that appear in no rudiment list: rolls played
**stick-against-stick**, rolls **on the rim** (`sur le cercle`), the **coup de douille**
(butt-end stroke, stick reversed), and passing one stick under or around the other — described
as "gestes non décrits dans les rudiments".

### 2.12 The German and Prussian layer

| Term | Meaning | Locator |
|---|---|---|
| **Einzelschlag / Doppelschlag / Pressschlag** | single / double / pressed stroke — the three German primitives | R14 (Peinkofer/Tannigel 1981 pp. 84–85) |
| **Wirbel** | roll: "many strokes so fast that the ear no longer hears single strokes but a sustained, even noise" | R15, verbatim |
| **Offener / Geschlossener / Einhändiger Wirbel**, **Einzelschlagwirbel** | the four German roll classes | R15 |
| **Presswirbel** | pressed (buzz) roll | R15, R16 |
| **Mühle** | the preparatory double-stroke exercise; alias **Mama-Papa / Papa-Mama** | R14, R15 |
| **Vorschlag** | grace note; multiple Vorschläge (2, 3, 4) are what the Doppelschlag serves | R14 |
| **Druckruf**, **Doppelwirbel** | two of the ~14 rudiments of the Prussian system evidenced by the 1777 _Kurze Anweisung zum Trommel-Spiel_; the system "was dominated by the right hand" | R13, R04 §German |
| **Trommelstreiche** | the 19th-century Bavarian regulation word for drum strokes (title of the 1823 Royal Bavarian infantry instruction) | R13 §Literatur |
| **Chick**, **halboffen** | the German literature imports "Chick" untranslated and uses `halboffen` for half-open | R16 |
| **Rebound** | imported untranslated into German pedagogy | R16 |

### 2.13 Italian and Spanish

Italian (R18): `rullo a colpi singoli`, `rullo a colpi doppi`, `rullo a 5 / 7 / 9 / 10 / 11 /
13 / 15`, `paradiddle singolo`, `paradiddle doppio`, `flam`, `flam accentato`, `flam tap`,
`flamacue`, `flam paradiddle`, `flam paradiddle-didle` [sic], `ruff`, `drag singolo`,
`drag doppio`, `ratamacue singolo / doppio / triplo`, `drag paradiddle 1 / 2`, `lesson 25`.
Note that Italian keeps **`ruff`** as a first-class name in its 26 where PAS folded it into
`Drag`.

Spanish (R19) translates all 40: `redoble de golpe único`, `cuatro golpes sencillos`,
`siete golpes sencillos`, `redoble de rebote múltiple`, `redoble de golpe triple`,
`redoble abierto con golpe doble` (also `long roll`), `redoble de cinco/seis/siete/nueve/
diez/once/trece/quince/diecisiete golpes`, `paradiddle sencillo`, `doble paradiddle`,
`triple paradiddle`, `paradiddle-diddle`, `flam` (glossed as **`mordente`**), `flam acentuado`,
`flam tap`, `flamacue`, `flam paradiddle`, `single flammed mill`, `flam paradiddle-diddle`,
`pataflafla`, **`tresillo de la Armada Suiza`**, `flam tap invertido`, `flam drag`, `drag`
(also `half drag`, `ruff`), `drag sencillo`, `drag doble`, `lección 25`, `dragadiddle`,
`drag paradiddle n.º 1 / n.º 2`, `ratamacue sencillo / doble / triple`.

### 2.14 The Swiss/Basel layer — what could actually be verified

This bucket's brief asks specifically for Basel nomenclature. **The enumerated Basel
Grundstreiche list was not obtained.** What is verified:

| Fact | Locator |
|---|---|
| Switzerland has **two** distinct rudimental cultures: the wider **Swiss Ordonnanz Trommel** (Zurich, Valais, Geneva) and the **Basler Trommeln** | R04 §Swiss, verbatim |
| "Basel drumming uses up to **49** different rudiments while Swiss military drumming uses only about **32** over its entire history" | R27, verbatim |
| "There are about **8** rudiments in the military system that are commonly referred to as **Basel Grundlagen**" | R27, verbatim |
| Basel was notated in "hieroglyphic" symbol codes until the 20th century; **Fritz Berger** devised the legible export notation in _Das Basler Trommeln_ (1928); the STPV completely revised the Berger system in **1983** | R04 §Swiss; R17; R31 |
| The Basel school teaches from **Grundstreiche** ("basic strokes") and **Grundlagen**; named pieces include `Ryslaifer` and `Arabi`; notation is taught as `Hieroglyphenschrift` vs `Bergerschrift` | R31 |
| **Doublé** is a Basel stroke-figure name | R32 |
| Genuinely Swiss rudiments that entered American lists, with their Swiss names: **Swiss Army Triplet** = `Ordonnanz Triole`; **Single Flammed Mill** = `Schleppmühle`; **Flammed 5 Stroke** = `5er Ruf`; **Flammed 9 Stroke** = `9er Ruf`; **Pataflafla** = `Bataflafla` | R26 |
| Almost every other American rudiment with "Swiss" in its name is a misattributed hybrid: *"If the rudiment has the word 'Swiss' in the name, with the obvious exception of the Swiss Army Triplet, it probably isn't Swiss."* | R26, verbatim |
| Of the 14 rudiments PAS added in 1984, "only **eight** … are foreign or not found in American military manuals prior to Strube. Only **two** of those eight non-traditional rudiments can be traced to a Swiss origin." | R04 §Present day, verbatim |
| The Basel drum itself: two-headed cylinder drum, **40–41 cm** (occasionally 42–43) measured on the outside of the shell, shell height equal to the diameter, **eight** gut/synthetic snares plus metal on the *bottom* head, batter head damped by a `Dämpfer` to stop the drum "singing" | R17 |

The Basel/Swiss layer is the largest hole in this bucket; see §6.

### 2.15 Hybrid rudiments — a vocabulary that is not a vocabulary

R04: *"there are more than 850 rudiments worldwide"*, and hybrids number "an indeterminate
number, with more than **500** published and documented". R29 lists ≈500 hybrid names under
the page title "507 Hybrid Rudiments", extracted to `scratch:bucket01/hybrid_names.txt`.
Representative sample as spelled: `Cheese`, `Cheese Berger`, `Cheese Chatachichi`,
`Cheesed Deviled Eggs`, `Chewbacca-Diddle`, `Book Report (with Extra Credit)`,
`Brille Stroke`, `Buguda Chickens`, `Casey Claw`, `Blurz`, `Eggbeaters`, `Herta`,
`Swiss Army Triplet`, `Flam Dragon`, `Ninja`, `Diddle-Egg-Five`, `Cheese Invert`.
R29's own footer asks readers to send in more, "and help me to keep this educational resource
complete and up to date" — i.e. it is an **open, unowned, growing** list.

R04 also states the two structural constraints practitioners apply: a hybrid must not exceed
one bar, and it must be **symmetrical** (playable starting on either hand).

**Verdict for KITWARP: hybrid rudiment names are out of scope as pivot vocabulary.** They name
sequences, not sounds; there is no owning body; and the names are neither stable nor unique.

---

## 3. Axis mapping

### 3.1 Terms that map cleanly onto an existing axis

| Term (as the source spells it) | Axis | Existing v0.1 value | Note |
|---|---|---|---|
| centre of the head (Strube: "within a circle of about two inches"; Hart: "as near the center of the head as possible"; Nevins: "about an inch above the center") | position | `centre` | three independent 1860–1870 attestations |
| bead 3 in from rim (normal rimshot) | position | `offset` (approx.) | v0.1 has no distance unit |
| bead 1 in from rim (ping shot) | position | `perimeter`-ish | see §5 |
| rimshot | technique | `rimshot` | ✔ |
| ping shot | technique | `ping-shot` | ✔ spelling matches |
| gock / gawk | technique | `gok-shot` | **misspelt**, see §4 |
| stick shot | technique | `stick-shot` | ✔ |
| cross-stick / rim click / side-stick | technique + site | `sidestick` + `crossstick` | duplicated across two axes, see §5 |
| rim only (marching bass metal bar) | site | `rim` / `rim2` | |
| butt end (`coup de douille`) | contact | `butt` | 1946/2005 French attestation |
| distal shaft near the hand (gock) | contact | `shank` | |
| tip / bead | contact | `tip` | |
| flam | ornament | `flam` | 2 attacks |
| drag | ornament | `drag` | 3 attacks |
| ruff | ornament | `ruff` | 3 attacks, but see §4 |
| roll (open, double stroke) | ornament | `roll` | |
| buzz / press / closed roll | ornament | `buzz` | indeterminate attacks |
| bounced (triple stroke) | ornament | `bounced` | |
| chick | technique | `chick` | ✔ German literature imports the word untranslated |
| foot splash | technique | `foot-splash` | attestation weak, see §6 |
| heel / toe | technique | `heel` / `toe` | but "heel-toe" is one compound stroke, see §5 |
| sweep (brush) | technique | `sweep` | |
| swirl / circling (brush circles) | technique | `swirl`, `circling` | R22b/R22d use clock-face degrees, not these words |
| brush | implement | `brush` | |
| snares thrown off (strainer disengaged) | mechanism | `wires-off` | R12 |
| open / half-open / closed hi-hat (`offen`/`halboffen`/`geschlossen`) | openness | `open`, `half`, `closed` | R16 |
| ghost note | dynamic | `ghost` | R05: "the inverse of an accent" |
| accent | dynamic | `accent` | |
| left hand / right hand lead | limb (reference axis) | `left-hand`, `right-hand` | Strube encodes it in the *name* |
| alternating sticking | limb | `alternating` | |
| left foot (hi-hat), right foot (kick) | limb | `left-foot`, `right-foot` | |

### 3.2 Terms that need a NEW value on an existing axis

| Term | Axis | Proposed sense | Locator |
|---|---|---|---|
| **double stop / flat flam / unison / "both"** | ornament, or a limb value | two hands landing at exactly the same instant, zero offset — explicitly *not* a flam | R04 §Double stop |
| **charge stroke** (French `Lr`, Swiss `LR`; French `coup de charge`) | ornament | a grace attached **after** the primary, or an open flam whose accent sits on the second note | R04 §Charge stroke; R21 item 7 |
| **open flam** | ornament + openness | the flam with a wide grace gap, named separately in 1870 and in European systems | R03 line 1134; R04 |
| **deadstick grace note** | ornament | grace note played staccato with no rebound (Scottish "drag") | R04 §Drag |
| **rim roll** (brush) | technique | brush handle rolled on the rim | R22a |
| **rim buzz** (brush) | technique | brush slapped on the rim with wires held clear | R22a |
| **trill** (brush) | technique/ornament | one-handed unmetered brush roll | R22a |
| **pulled double / whipped cream** | technique | brush double landing at two different points, pulled toward the body | R22a |
| **legato push** | technique | brush pushed across the head perpendicular to the player | R22a |
| **palm-up snap** | technique | brush wires flicked off the head with a wrist turn | R22d |
| **feathered** | dynamic | bass drum played at near-inaudible level under brush time | R22b |
| **fan vs tips** | contact | brush accent by pressing more of the fan; unaccented on the tips | R22c |
| **stick-on-stick roll**, **stick under/around the other** | technique | attested French military actions absent from every rudiment list | R21 |
| **attack count** on ornaments (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 25) | ornament parameter | the numbered rolls *are* the attack-count vocabulary | R06; R01 |

### 3.3 Terms that fit NO axis — the most valuable finding

These are the largest and best-documented terminology families in this bucket, and **none of
them names a distinguishable sound event**. That is not a defect in the terms; it is evidence
about what layer of the model they belong to.

| Family | Terms | Why no axis fits |
|---|---|---|
| **Stroke type** | full stroke, down stroke, up stroke, tap/low stroke, buzz stroke; up/tap/rest positions | These name the **preparation and termination height** of the motion, not the sound. Two identical-sounding notes differ only in what the stick does afterwards. They are unrepresentable in a sampled note and must not become pivot values. |
| **Technique school** | Moeller / whipping, Gladstone free stroke, push-pull, Freehand / gravity, heel-toe, slide, swivel, single vs double bass pedal | These are **motor systems** that generate attacks. Their only audible trace is the attack count and spacing — already covered by `ornament` and by the note grid. |
| **Grip** | matched, German, French, American, traditional/classic, little-finger (vintage) fulcrum, thumb fulcrum, Garfield grip, thumbs-up | Affects timbre marginally and is never sampled separately. Fits neither `implement` nor `contact`. |
| **Rudiment name as a pattern** | all 40 PAS names, all 26 NARD names, all ~500 hybrids, all 21 French classes, the Basel Grundstreiche | These name **sequences of notes with a sticking**, i.e. objects one level above the pivot term. `paradiddle` is not a sound; it is four sounds and an assignment of limbs. |
| **Sticking pattern** | `RLRR`, `DGDD`, `DIDD`, lead hand, hand-to-hand, alternating | Per-note this collapses to `limb`; the *pattern* is above the pivot. |
| **Practice directive** | "open (slow) to close (fast) to open (slow)", "at an even moderate march tempo" | Performance instruction, not identity. |
| **Stick height as a number** | 1″, 3″ … 12″, 15″ | A continuous scalar; `dynamic` in v0.1 is a five-value unordered set. See §5. |
| **Notation-only conventions** | Strube's E-space/F-space hand encoding; Hart's upper-line/lower-line flams; single/double/triple stem slashes for diddles | Belong to the notation bucket, not the pivot. |
| **Stroke envelope** | Nevins's `Poing Stroke` ("sudden, hard, short") vs his No. 10 ("soft, long, drawing"); Hart's counter-claim that all strokes "have but **one length of sound** on the Drum" | Two 1860s primaries disagree about whether a drum stroke *has* a duration at all. v0.1 has no `duration` or `envelope` axis. See §5.3 finding 5. |

The one that should worry the model is **stroke type**, because it is the single most-taught
vocabulary in this entire bucket (PAS itself teaches it, R37) and it maps to nothing. That is
the correct answer — but any future contributor will try to add `full-stroke` to the
`technique` axis, so it is worth writing down that this was checked and rejected on purpose.

---

## 4. Conflicts and false friends

### 4.1 One word, different physical actions

| Word | Meaning A | Meaning B | Locator |
|---|---|---|---|
| **rimshot** | kit/marching: one stick strikes rim **and** head together | orchestral: one stick is **laid on the head**, its shaft pressed to the rim, and struck by the *other* stick (= stick shot) | R07 |
| **rimshot** | the technique | the comedy **sting** — "often called a rimshot, although some versions of it do not include a rimshot in the technical sense" | R07, verbatim |
| **drag** | PAS/NARD: two **diddled** grace notes before the primary | Scottish pipe band: "a flam where the grace note is played as a **deadstick** (staccato note)" | R04 §Drag, verbatim |
| **ruff** | historically: `llR` played **closed** (the open version was called *half drag*) | modern American: `rlR`, two **single** grace notes | R04 §Ruff |
| **roll** | orchestral/German band default: **closed** (buzz) | rudimental/drum corps default: **open** (double stroke) | R15, explicit for German and Austrian march music |
| **press roll** | drum-set usage: the multiple-bounce roll | German `Presswirbel`: the same, but `Pressschlag` is the *single* pressed stroke | R04; R14; R15 |
| **mill** | American `mill stroke`: reversed paradiddle `RRLR` | German `Mühle`: the **preparatory double-stroke exercise** for the roll | R04 §Mill stroke; R14 |
| **moulin** | French: the **single paradiddle** | — but cognate with both of the above | R21 item 16 |
| **French** | `French roll` = triple stroke roll | `French grip` = palms-inward matched grip | R04; R16 |
| **splash** | `splash cymbal`, an instrument | hi-hat `foot splash`, a technique | R11; v0.1 has both |
| **dead** | orchestral `dead stroke`: mallet held against the bar | rudimental `deadstick`: a grace note that does not rebound | R04 §Drag |
| **gock** | the stroke | the 6″/8″ **drum** in a multi-tenor arc named after it ("gock", "shot" or "spock" drums) | R07; R10 |
| **chick** | hi-hat foot close | R16 also uses `chick` loosely for a general background hiss/rustle texture | R16 |
| **open** | modern: un-closed — an open roll is double-stroked and audibly separated, an open hi-hat has the cymbals apart | **Hart 1860: soft and light.** "the full **open** flam … the full **open** blow … the full **open** three roll … will be executed **soft and light**", and a soft roll is written with an "**open figure**" numeral | R38 lines 158–170; R04 §Roll |
| **drawing stroke** | Nevins 1864 No. 10: a legitimate stroke type, "soft, long, drawing" | Hart 1860: forbidden — "make **no drawing strokes** or sideway beats in no case whatever" | R39 line 213; R38 lines 116–121 |
| **tap** | modern: the low stroke, one of the four stroke types | Nevins 1864 No. 30 **TAPS**: a bugle/drum *signal* ("a signal for the front to advance slow"); Hart lists "Blows, **Taps**, Flams" as interchangeable names for one plain stroke | R39; R38 line 68 |
| **blow** | 1860–1864: the standard word for a plain single stroke | absent from every modern list reached | R38, R39 |

### 4.2 Different words, same physical action

| Action | Names |
|---|---|
| tip on head, butt against rim, hand muting | **cross-stick** = **rim click** = **side-stick** (R12, all three in one sentence) |
| double-stroke roll of indeterminate length | **long roll** = **double stroke open roll** = `roulement` = `bâton rompu` = `Doppelschlagwirbel` = `redoble abierto` = `rullo a colpi doppi` |
| pressed multiple-bounce roll | **buzz roll** = **closed roll** = **press roll** = **multiple bounce roll** = `Presswirbel` = `Druckruf` = `trizzlet` (Scottish) = `Ra stroke` (Dutch) = `Redoble de Zumbido` (Spanish) = `Los Rufaos` (Bajoaragonés) = `Rullo` (Eporedian) = `Rau Tau` (Mexican) |
| 3-attack roll | **drag** = **half drag** = **ruff** = **3-stroke roll** = Hart's **three roll** (open and closed) = French **ra de 3** / **tra**. Nevins 1864 keeps **half drag**, **full drag**, **single drag**, **double drag** and **ruffs** as five separate gamut items where PAS has one `Drag` |
| plain single stroke | **blow** (Hart, Nevins) = **tap** (Hart) = **single beat** (Hart) = **Poing Stroke** (Nevins, when hard and short) = `Einzelschlag` = `coup simple` = `golpe único` = `colpo singolo` |
| ratamacue | **Rotamacue** (Nevins 1864 spelling) |
| paradiddle | **paradidle** (Nevins 1864 spelling), **paradiddle** (modern), `moulin` (French), `Mühle`-adjacent (German, different sense — see §4.1) |
| triple stroke roll | = **French roll** |
| flam with a diddle | **cheese** (hybrid) — a flammed diddle |
| drag with alternating sticking | **herta** |
| one-handed roll using the rim as fulcrum | **fulcrum roll** = **gravity roll** = **freehand roll** = **gravity blast** = `Einhändiger Wirbel` |
| single flammed mill | = `Schleppmühle` (Swiss) |
| Swiss Army Triplet | = `Ordonnanz Triole` (Swiss) |
| Pataflafla | = `Bataflafla` (Swiss) |
| flam paradiddle | = **flamadiddle** (R04) |
| inverted flam tap | = **tap flam** (R04) = French `coup anglais` inverted (R21 item 8) |
| gock | = **sprock** (UNVERIFIED — attributed to snarescience.com, which returned HTTP 500) |

### 4.3 The same list, respelled by its own vendors

Vic Firth's education page (R28), the largest single distributor of the PAS list, respells it:
`Patafla-Fla` (PAS: `Pataflafla`), `Flammed Mill` (PAS: `Single Flammed Mill`),
`5 Stroke Roll` / `9 Stroke Roll` / `13 Stroke Roll` in numerals (PAS spells them out),
`Drag Paradiddle #1` retained. It also reorders the 40 into **four difficulty tiers** (Dr.
John Wooton) that cut across the PAS I–IV grouping entirely. Italian (R18) prints
`flam paradiddle-didle` and `Single Dragadiggle`; Spanish (R19) glosses `flam` as `mordente`.

And the standards body respells its own list across revisions: §2.2b sets NARD's official 1958
recording against the 1984 sheet and finds four renamings (`Long Roll` → `Double Stroke Open
Roll`, `Ruff` → `Drag`, `Single Drag` → `Single Drag Tap`, `Double Drag` → `Double Drag Tap`).

**Consequence for KITWARP:** the rudiment names are *not* a controlled vocabulary even where a
standards body owns them. Any mapping table keyed on rudiment name must carry aliases, and the
alias set has to span revisions of the *same* list, not just rival lists.

### 4.4 Competing standards, all current

| List | Size | Owner | Locator |
|---|---|---|---|
| NARD Standard American | 26 (13 + 13) | National Association of Rudimental Drummers, 1933; revived by the IATD | R23, R13 |
| PAS International | 40 | Percussive Arts Society, 1984 | R01 |
| Scottish Drumming Rudiments | 46 | pipe band tradition | R04 §PAS rudiments |
| Rudimental Codex (French/Swiss) | 42 | Percussion Creativ / Claus Hessler; submitted to UNESCO | R04 §Present day |
| Spalding's proposal | 5 essential + 22 | published *inside* Percussive Notes | R36 |
| French conservatoire (Tourte) | 34, from a historical catalogue of 70+ | CNSM Paris | R04 §French |
| Hybrid corpus | 500+ and open | nobody | R29 |
| Worldwide | "more than 850" | — | R04 |

R04 records that the IATD's objection to the PAS 40 is its "Swiss influence" — and that the
objection is largely wrong on the facts (only two of the fourteen additions are traceably
Swiss). The disagreement is live, so **no single rudiment list can be treated as the
authority**.

---

## 5. Gaps against vocabulary v0.1

Checked against `vocabulary/axes.json` v0.1.0, serial 1.

### 5.1 Misnamed in v0.1

The renaming history in §2.2b is the strongest reason this section exists: a name that PAS
prints today is not the name the same figure carried in 1958, 1900, 1870 or 1860. Aliases are
not a nicety here, they are the only way a mapping survives contact with a source.

| v0.1 slug | Problem | Evidence | Recommendation |
|---|---|---|---|
| `technique: gok-shot` | The literature spells it **gock** (alt. **gawk**). "gok" appears in no source reached. Marching tenors even name a *drum* after it — "gock", "shot" or "spock" drums. | R07, R10 | ids are forever (ADR-0003): keep `gok-shot`, add a `correction` alias `gock-shot` and record `gock` / `gawk` as source spellings |
| `ornament: ruff` vs `ornament: drag` | v0.1 treats them as two ornaments. In the current PAS standard they are **the same figure**: PAS #31 is printed `Drag` and NARD calls it "drag (half drag or ruff)". NARD's own 1958 recording calls track 8 simply **The Ruff** — `Drag` displaced `Ruff` in 1984. The historical distinction was **open vs closed execution** (Hart's `Three Roll open`/`closed`, Greissinger's `Open Drag`/`Close Drag or Half Drag`), not two figures. The genuinely distinct item is the American **3-stroke ruff** `rlR` (single-stroked graces), which is on no official sheet but is defined in an 1864 army manual. | R01 #31; **R43 track 8**; R04 §Ruff, §Drag; R23; R38 Lesson III; R39 No. 25; R40 lines 4385–4406 | keep both ids; document that `ruff` means the *single-stroked* 3-attack grace and `drag` the *diddled* one, that most sources conflate them, and that `ruff` is the older name for what PAS now calls `drag` |
| `technique: heel` / `technique: toe` | These read as two separate contact points, but the literature's **heel-toe** is one compound motion producing **two** attacks, and R09 states that physically "it's the ball of the foot (or toes) both times". The real per-note distinction is heel-**down** vs heel-**up** posture, which is inaudible. | R09 | document the two values as *positions on a pedal or frame drum*, and record that "heel-toe" is a double-stroke ornament, not a technique value |
| `technique: sidestick` + `site: crossstick` | The same physical action is modelled on two axes at once. R12 gives cross-stick, rim click and side-stick as three names for one thing. | R12 | keep both ids; write the rule that a term uses one or the other, never both, and add `rim-click` as an alias |
| `technique: dead` | Ambiguous: orchestral *dead stroke* (implement held down on the bar) vs rudimental *deadstick* grace note. | R04 §Drag | disambiguate in the description |
| `technique: rim-only` | Not a term any reached source uses. The literature says rimshot, rim click, cross stick, side stick, or (marching bass) "rim click" on a metal bar. | R07, R10, R12 | keep the id; record that it is a KITWARP coinage with no literature attestation |
| `technique: back-stick` | **No attestation found in any source reached.** | §6 | mark UNVERIFIED in the vocabulary until a locator exists |

### 5.2 Missing values the literature demands

| Axis | Missing value | Evidence |
|---|---|---|
| ornament | **flat flam / double stop / unison** — both hands exactly together | R04 §Double stop: "a staple of several European systems … used in modern corps style snare drumming as well as drum kit and classical percussion" |
| ornament | **charge stroke** — grace *after* the primary | R04 §Charge stroke; R21 item 7 |
| ornament | **attack count** as an ordered parameter (3–17, 25) | R01 #7–#15; R06 on the 4/8/12/14/16 and Scottish 25 |
| ornament | **open flam** as distinct from flam | R03 line 1134; R04 §Flam |
| technique | **rim roll**, **rim buzz**, **trill**, **pulled double**, **legato push**, **palm-up snap** (brush) | R22a, R22d |
| technique | **stick shot on the rim / stick-against-stick roll**, **coup de douille** (butt-end stroke) | R21 |
| contact | **fan** (brush accent surface) as distinct from **tip** | R22c |
| implement | v0.1 lacks `fist` and `fingernail`, which `.agents/round2/BRIEF.md` lists in the model but `axes.json` does not carry | `vocabulary/axes.json` vs BRIEF |
| dynamic | v0.1's five values are an **unordered set**; marching practice uses an ordered height scale 1″–15″, PAS teaches accent/tap as a *height* relation, and Nevins 1864 already names an ordered three-step scale **Hard / Middling Hard / Faint or Soft** applied independently to strokes, flams and rolls | R10, R37, **R39** |
| dynamic | **faint / feathered** — a level below `ghost`: Nevins's "FAINT FLAMS" and "Faint, or Soft" seven-stroke roll; Hazilla's feathered bass drum | R39; R22b |
| position | v0.1's four values are radial and unitless; the sources give **distances in inches** (3″ from the rim for a normal rimshot, 1″ for a ping shot), Strube gives a 2-inch target circle at the centre, and Nevins says "about **an inch above the center**" | R03, R07, **R39** |

### 5.3 Structural findings, not value lists

0. **The recommended shape already existed in 1900.** Greissinger's legend — "t indicates
   tap; f, flam; d, drag; r, roll. The figures under the rolls indicate the number of strokes
   in each roll" (R40) — is an event-type letter plus an attack count, i.e. exactly finding 1
   below. This is the strongest single piece of evidence in the bucket that the ornament axis
   should carry a count, because it is a working encoding rather than a proposal.

1. **The ornament axis needs a count, and the numbered rolls are that count vocabulary.**
   `.agents/round2/BRIEF.md` already says ornament carries "an attack count", but
   `axes.json` v0.1 has no field for it. The rudiment literature is the canonical source of
   the count set: 3 (drag), 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 and the Scottish
   25. The odd/even accent rule (R06) means the count is not merely decorative: an even-count
   roll ends on **two** accented notes, an odd-count roll on one.

2. **Openness is not a hi-hat-only axis.** v0.1's `openness` anchors are all hi-hat words, but
   the primary literature applies open/closed to **rolls** (`open roll` / `closed roll`), to
   **flams** (Strube's `Open Flam`, Greissinger's `The Open Flam`) and to **drags**
   (Hart's `Three Roll open` / `closed three Roll`, Greissinger's `Open Drag` /
   `Close Drag or Half Drag`) — three independent attestations for the drag alone — plus the
   PAS practice directive "open to close to open". Either openness is generalised, or the
   roll's open/closed distinction has to be modelled elsewhere — it is currently split across
   `ornament: roll` and `ornament: buzz`, which is a workable answer but should be written
   down as a decision. Note the trap in §4.1: in Hart 1860 `open` means *soft*.

3. **Lead hand is identity-bearing in the primary literature, not decoration.** Strube 1870
   names half his rudiments "Left Hand …" / "Right Hand …" and encodes the hand in the staff
   position; Hart 1860 puts left-hand flams on the upper line and right-hand on the lower;
   Greissinger 1900 makes the left hand the default lead ("Every roll or beat should begin
   with the left hand"); Straight 1922 still writes "a **Left hand** Drag"; and Italian
   practice today still defaults to a left-hand start (R18). v0.1 carries `limb` as a
   *reference* axis on the layout slot rather than on the term. That is probably right for
   sampled drum kits, but a converter reading any rudimental source will find the hand baked
   into the name, and the default lead hand is **left**, not right.

4. **Rudiment names must not enter the pivot vocabulary.** They name patterns. The only
   rudiment-derived terms that belong on an axis are the per-note ornaments in §2.4.

5. **A stroke-envelope axis is arguable and currently absent.** Hart 1860 builds his whole
   notation on the claim that "all Blows, Taps, Flams, or Single Beats have but **one length
   of sound** on the Drum" (R38) — which is why he needs only four characters. Nevins 1864
   contradicts it four years later with a graded pair, `Poing Stroke` = "sudden, hard, short"
   against "soft, long, drawing" (R39). For a *sampled* pivot Hart is right and no envelope
   axis is needed, because the sample carries the envelope. It is worth recording that the
   question was asked and answered by the source material rather than by assumption.

6. **The 1984 "additions" were not all new.** `Triple Paradiddle` is item 18 of Nevins's 1864
   US Army gamut (R39) and `Flams Paradidle Didle` is item 19, yet both are counted among the
   fourteen rudiments PAS *added* in 1984 (§2.2), which R04 characterises as drum-corps,
   European or contemporary. Any provenance note that dates a rudiment by its list membership
   will be wrong; date it by the earliest manual instead.

### 5.4 Confirmations — v0.1 values this bucket independently validates

`rimshot`, `ping-shot`, `stick-shot`, `sidestick`, `crossstick`, `butt`, `shank`, `tip`,
`flam`, `drag`, `ruff`, `roll`, `buzz`, `bounced`, `ghost`, `accent`, `chick`, `wires-on`,
`wires-off`, `open`/`half`/`closed`, `brush`, `sweep`, `left-hand`/`right-hand`/`alternating`/
`left-foot`/`right-foot`, `centre`. Every one of these is attested in at least one source
reached, most in a pre-1930 or non-English one.

Two more that this bucket did not expect to confirm:

- **`implement: jazz-stick`** — attested by name in Straight 1922: "Sand-blocks, Clog-mallets,
  **Jazz-sticks** or Leather straps" (R41 line 13078). Not a modern marketing coinage.
- **`damping: muted` / `damped`** — Straight 1922 uses "**muffled** drums" as a standing
  instruction ("Use muffled drums when you Jazz, not too loud"), and the Basel drum's batter
  head carries a permanent `Dämpfer` to stop it singing (R17). Damping is a 19th- and early
  20th-century concept, not a sampling-era one.

---

## 6. Self-critique (round C)

### 6.1 The single most authoritative source not obtained

**Fritz R. Berger, _Das Basler Trommeln. Sein Werden und Wesen_ (Trommel-Verlag Basel, 1928),
with its companion complete method** (N04/N05). This is the source the bucket brief points at
directly, it is the reason Basel nomenclature exists outside Switzerland at all, and its
notation was revised into the current STPV standard in 1983. Without it the Basel section of
this dossier is five verified facts and one stroke name (`Doublé`). It is in print from Musik
Hug (Zurich) and Percussion Brandt (Germany) and is not digitised anywhere reachable.
**Recommendation to the reconciliation pass:** either buy it, or chase the
**Percussion Creativ _Rudimental Codex_** (N08), which is a modern trilingual list explicitly
built to reconcile the French and Basel systems with the American one and would deliver
German, French and English names side by side in one document. No URL for it was found; the
route is probably percussion-creativ.de's publications page or Claus Hessler directly.

### 6.2 Everything else this bucket could not reach, and what it would have added

| Not reached | What it would have added |
|---|---|
| Weinberg, _Guide to Standardized Drumset Notation_ (N10) | PAS's own **drumset** notation legend — the one document that would say authoritatively which technique names PAS blesses for the kit (as opposed to the snare), and it is the list Finale, Sibelius and Dorico implement |
| Moeller 1925 (N01), Stone _Accents and Rebounds_ (N02) | first-hand codification of the stroke types and of the two right-hand grips, instead of tertiary paraphrase |
| Cameron _Brushworks_ (N11), Thigpen _The Sound of Brushes_ (N12) | the named brush-stroke systems. §2.8 has real definitions only because a PAS journal anthology happened to be mirrored on a university page; the two canonical brush books remain unread, so `Tap-Sweep-Tap`, `Silent Sweep`, `Lift`, `Guitar Stroke` stay UNVERIFIED |
| Scottish Drumming Rudiments sheet (N21) | 46 names including the stroked rolls to 25 and `trizzlet` — the third national standard, entirely absent here |
| Swiss Ordonnanz manuals 1728–1964 (N19) | the ~32-rudiment military Swiss system; R25 lists them but only behind Google Drive folders |
| Bruce & Emmett 1862/1865 (R34) | the first printed **Flamacue** and the first advocacy of "open, closed, open" practice; the IMSLP PDF is public domain and downloadable — a later worker should simply take it |
| the *notation* of R03, R38, R39, R40 | all four are lithographed scores whose engraved figures did not OCR; every claim about them here rests on their **prose** only. Reading the plates would settle, for instance, exactly how many strokes Nevins's `SLOW SAG` has |
| Peinkofer/Tannigel English edition (R42) | the German normative handbook is on archive.org under lending restriction; worth one attempt with a borrowing account |
| snarescience dictionary (N23) | the marching slang layer where `gock`, `sprock` and very likely `back stick` are actually defined |
| **_Corps Style Snare Drum Dictionary_, Alfred 1981 (R44)** | the one *dictionary* of corps-style vocabulary located anywhere in this bucket. It is on archive.org under lending restriction (`corpsstylesnared0000unse`, ISBN 9780739023228). A borrowing account would very likely settle `back stick`, `gock`, `spock` and the American "Swiss" rudiment names in a single sitting. **This is the cheapest remaining win in the bucket.** |
| Percussive Notes archive (R35–R37) | PAS's own account of the "certain changes in terminology" made in 1984 — i.e. exactly which names were changed and from what |

### 6.3 Known weaknesses in what *is* reported

- **`back-stick` is unattested.** It is a v0.1 vocabulary value and this bucket, which owns
  rimshot and stick vocabulary, could not find a single definition for it in any source
  reached. It may be marching visual vocabulary (playing with the butt end during a flourish),
  but that is a guess and is recorded as one, not as a finding.
- **`foot-splash` is weakly attested.** Wikipedia's hi-hat article (R11) names `chick`,
  `pedal hi-hat`, open, closed and `cooking`, but not foot splash. The definition in §2.9 comes
  from a search-result summary whose underlying pages (drummagazine.com, rhythmnotes.net) both
  returned empty or 403 to a fetch. A drum-kit method book should confirm it.
- **`slide` and `swivel` are search-summary only** for the same reason.
- **Strube's full 25-item list is second-hand.** The scan's engraved titles OCR'd only in
  part; twelve of the twenty-five are confirmed from the primary text and the rest come from
  R04's transcription. Hart 1860 and Nevins 1864 OCR'd far better because their prose carries
  the definitions; their *notation* is still unreadable to this dossier, so every claim about
  what a Hart or Nevins figure looks like on the page rests on their prose alone.
- **The five archive.org primaries were mined for terminology, not exhaustively read.** Their
  camp-duty and exercise sections (the bulk of each book) were skimmed by grep for named
  figures, so a rudiment named only once in a tune heading could have been missed.
- **The heel-toe article (R09) is weakly sourced on Wikipedia** and its attribution of the
  modern formalisation to James Davenport should not be repeated without a second source.
- **No orchestral treatise was consulted** — Berlioz, Kastner, Blades, Peinkofer/Tannigel.
  That is bucket 02's job, but it means the orchestral half of the rimshot/roll conflict in
  §4.1 rests on encyclopaedic sources rather than on a treatise.
- **Round A's search leg was cut short by budget**, not by exhaustion: the session-wide
  WebSearch allowance (200 calls, shared across all twelve buckets) was consumed at search 20
  of this bucket, and the DuckDuckGo HTML endpoint is blocked by the egress proxy. Everything
  after search 20 was done by constructing URLs directly and by querying archive.org, which is
  where the five 1860–1922 primaries and the 1958 NARD track list came from. A later message
  said the pool had recovered; two retries from this worker were still refused with
  `200 of 200`. **Two searches were queued and never ran**: the Percussion Creativ
  _Rudimental Codex_ list (N08), and a German-language search for an enumerated Basel
  `Grundstreiche` table. Both are named in §6.1 as the chase-list for reconciliation.

### 6.4 Environment findings worth passing to other buckets

- `archive.org/download/<identifier>/<identifier>_djvu.txt` **works** and is the cheapest way
  to read any pre-1929 method book; `archive.org/advancedsearch.php?...&output=json` and
  `archive.org/metadata/<id>` work for finding identifiers and file names. This is how Strube
  1870, Hart 1860, Nevins 1864, Greissinger 1900 and Straight 1922 were all obtained, at a
  cost of two HTTP requests each. The productive query shapes were
  `title:(drum AND fife)`, `title:(drum beating)` and
  `subject:(drum) AND date:[1800-01-01 TO 1930-01-01]`. Identifiers ending `0000xxxx` are
  lending-restricted; plain identifiers are usually full public-domain text.
- `web.archive.org` **content** returns proxy 403 for both WebFetch and urllib, although
  `archive.org/wayback/available?url=` returns JSON normally. The Wayback fallback named in
  the brief is therefore **not available** in this environment.
- `archive.org/metadata/<id>` returns an item's **description field**, and for LPs that field
  routinely contains the full track list. For a bucket about *names*, a recording's track list
  is a primary artefact: the NARD 26 in §2.2b were recovered this way after the association's
  own web page turned out to publish them only as images. Worth trying for any list that a
  publisher issued as a record, a video or a poster.
- Several publisher sites (bloomdrums, elephantdrums, pdfcoffee, drumlines mirrors) return 403
  to urllib but **succeed via WebFetch**, and vice versa for PDFs. Trying both is worth it.
- Full-text mirrors of in-copyright method books surface on unlicensed aggregators
  (pdfcoffee, epdf and similar). Under CLAUDE.md rule 2 those are reference-only: this dossier
  registers such books with their locator and does **not** quote them. Every verbatim quotation
  above comes from a public-domain scan, an openly published PDF, or CC BY-SA text.
- pas.org's WordPress uploads directory serves PDFs at 200 while its article pages are
  paywalled — the sheet is reachable even though the journal is not.
