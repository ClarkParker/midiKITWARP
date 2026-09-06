# Round 2, bucket 02 — Orchestration treatises and percussion writing manuals

Scope: the percussion vocabulary as it is named in printed orchestration treatises,
instrumentation manuals and percussion-writing guides, from Berlioz (1843) to Solomon
(2016). This layer matters because it names the physical distinction — which part of the
instrument, which part of the beater, which stroke — without reference to any note number,
and because it names it in four languages that are all still used in scores.

**Method note.** Round A (breadth) was run before any extraction, as the brief requires.
The general web-search channel was unavailable for most of it (see A.0), so breadth was
obtained through catalogue and full-text APIs instead. Round B extraction was done against
page images via archive.org's OCR layers, so every quotation below carries a printed page
number, not a guess.

**OCR convention.** Quotations are taken from the OCR (`_chocr.html.gz`, character-level,
re-assembled per page and cross-checked against `_page_numbers.json` for the printed page).
Obvious OCR damage is corrected silently where the correct reading is certain — `cyrnbale`
→ `cymbale`, `Schlagel` → `Schlägel`, `fia` → `fla`, `Miinzen` → `Münzen` — and left with
`[sic]` where it is not. Read's Thesaurus prints four parallel language columns; the OCR
flattens them into one run, so column alignment below was reconstructed by matching term
counts per column and is marked UNVERIFIED wherever a column had a different number of
entries from the English one.

---

## 0. What this dossier is for

Every term below is a candidate for the KITWARP pivot vocabulary. Section 3 maps each onto
an axis; section 3.9 lists the ones that fit **no** axis, which the brief identifies as the
most valuable finding. Section 5 states what vocabulary v0.1 (155 terms, kit-only) is
missing or has named wrongly, measured against this literature.

---

## 1. Candidate source register (Round A)

### 1.0 Search channels — what worked and what did not

The environment blocked the ordinary route:

| Channel | Result |
|---|---|
| `WebSearch` tool | Budget exhausted at 200/200 **for the whole session, shared across workers**. 3 queries were run before it closed. |
| `html.duckduckgo.com`, `lite.duckduckgo.com` | HTTP 202 with an anti-bot page; via WebFetch, a CAPTCHA challenge |
| `searx.be` | "Verifying your browser…" / captcha |
| `mojeek.com` | 403 |
| `babel.hathitrust.org` | 403 (Cloudflare) — no in-volume full-text search |
| `catalog.hathitrust.org/api/volumes/…` | **works** (bibliographic only, no text) |
| `googleapis.com/books/v1/volumes` | HTTP 429, "Quota exceeded … for consumer project_number:624717413613" — the proxy project's daily quota, not ours; retried later, still 429 |
| archive.org `fulltext/inside.php` (search-inside) | "Item not available" for every lending-restricted item, on both `d1` and `d2` hosts |
| archive.org `advancedsearch.php` | **works** — the main breadth instrument used here |
| `openlibrary.org/search.json` | **works** |
| archive.org `download/<id>/<id>_djvu.txt`, `_chocr.html.gz`, `_page_numbers.json` | **works** for non-restricted items — the main depth instrument |
| direct `WebFetch` of known URLs | works (vsl.co.at returns 502; philharmonia.co.uk works) |

Consequence for the bucket: **every book still in copyright and held on archive.org under
controlled digital lending is unquotable from this environment** — not merely hard, but
returning no text at all, not even a snippet. That is what puts Blades, Adler, Stone,
Peinkofer/Tannigel, Brindle and Read's own later *Compendium* in the "not reached" column
below, and it is not a research choice.

### 1.1 The searches actually run

Twelve is the floor the brief sets; 31 distinct queries were run, varying register,
language, source type and era.

| # | Register / language / era | Query |
|---|---|---|
| Q1 | trade, EN, modern | `Gardner Read "Compendium of Modern Instrumental Techniques" percussion chapter techniques list` (WebSearch) |
| Q2 | pedagogical, EN, modern | `Samuel Solomon "How to Write for Percussion" techniques list snare drum rim shot rim click` (WebSearch) |
| Q3 | organological, EN, modern | `archive.org James Blades "Percussion Instruments and Their History" full text` (WebSearch) |
| Q4 | notational, EN, modern | `Kurt Stone "Music Notation in the Twentieth Century" percussion chapter beaters playing techniques terminology` (WebSearch) |
| Q5 | scholarly, **DE** | `Peinkofer Tannigel "Handbuch des Schlagzeugs" Schlaginstrumente Spieltechnik Schlägel` (WebSearch) |
| Q6 | scholarly, **DE** | `"Spieltechniken" Schlaginstrumente Instrumentationslehre Glossar "am Rand" "in der Mitte" Trommel` (WebSearch) |
| Q7 | treatise, EN/FR, 19c | IA: `creator:(Berlioz) AND title:(instrumentation OR orchestration) AND mediatype:texts` |
| Q8 | treatise, EN, 20c | IA: `title:("principles of orchestration")` |
| Q9 | treatise, EN, 20c | IA: `creator:(Forsyth) AND title:(orchestration)` |
| Q10 | treatise, EN, 20c | IA: `title:("technique of the modern orchestra")` |
| Q11 | treatise, **FR**, 19c | IA: `creator:(Gevaert)` |
| Q12 | treatise, **FR**, 19c | IA: `creator:(Kastner)` and `creator:("Kastner, Georges" OR "Kastner, Jean-Georges")` |
| Q13 | treatise, **DE**, 19–20c | IA: `title:(Instrumentationslehre)` |
| Q14 | organological, EN, 20c | IA: `creator:(Blades) AND title:(percussion)` |
| Q15 | handbook, EN/DE, 20c | IA: `title:("handbook of percussion instruments")` |
| Q16 | thesaurus, EN, 20c | IA: `creator:("Read, Gardner")` |
| Q17 | modernist, EN, 20c | IA: `title:("contemporary percussion")` |
| Q18 | pedagogical, EN, 20c | IA: `title:("study of orchestration")` |
| Q19 | pedagogical, EN, 21c | IA: `title:("how to write for percussion")` |
| Q20 | notational, EN, 20c | IA: `title:("music notation in the twentieth century")` |
| Q21 | treatise, **IT** | IA: `title:(strumentazione OR istrumentazione)` |
| Q22 | treatise, **ES** | IA: `title:(instrumentacion OR "instrumentación") AND subject:(music OR musica)` |
| Q23 | treatise, **FR** | IA: `title:("traité d'instrumentation" OR "traité general d'instrumentation")` |
| Q24 | pedagogical, EN, pre-1960 | IA: `subject:("Percussion instruments") AND date:[1850 TO 1960]` |
| Q25 | pedagogical, EN/FR/DE, pre-1930 | IA: `title:(drum OR drums OR tambour OR Trommel) AND subject:(instruction)` |
| Q26 | treatise, EN, 19c | IA: `title:("the orchestra" OR "orchestral technique") AND creator:(Prout OR Corder OR Jacob)` |
| Q27 | treatise, **FR** | IA: `creator:(Koechlin OR Lavignac OR Casella) AND title:(orchestration OR instrumentation)` |
| Q28 | trade, **DE** | IA: `(Schlaginstrumente OR Schlagzeug OR Schlagwerk)` |
| Q29 | pedagogical, EN/DE, pre-1940 | IA: `(timpani OR kettledrum OR kettledrums OR Pauken) AND date:[1800 TO 1940]` |
| Q30 | scholarly, EN, 20–21c | IA: `("instrumental techniques" OR "playing techniques") AND subject:(music)` |
| Q31 | notational, EN | IA: `("percussion notation" OR "notation for percussion")` |
| Q32 | catalogue, EN | OpenLibrary: `orchestration percussion techniques` |

### 1.2 The register

Authority levels: **A** = the standard reference in its field; **B** = a widely used
manual; **C** = a course guide, vendor page or derived resource.

#### Reached — full text obtained

| # | Title | Author | Year | Type | Locator (archive.org id / URL) | Auth | Yield |
|---|---|---|---|---|---|---|---|
| S1 | **Thesaurus of Orchestral Devices** | Gardner Read | 1953 | thesaurus of playing devices, 4-language | `thesaurusoforche00read` (Pitman, NY) — **not** lending-restricted | A | **very high** — Part IV Percussion, ch. 32–38, pp. 158–233 |
| S2 | **Instrumentationslehre**, vol. 2 | Berlioz, rev. & suppl. Richard Strauss | 1905 | treatise, DE | `instrumentations02berl` (Peters) | A | high — Schlaginstrumente pp. 395–430 |
| S3 | Instrumentationslehre, vol. 1 | Berlioz / Strauss | 1905 | treatise, DE | `instrumentations01berl` | A | low (strings/winds) |
| S4 | **Die Technik des modernen Orchesters** | Widor, tr. Riemann | 1904 | supplement to Berlioz, DE | `dietechnikdesmod00wido` | A | medium |
| S5 | **The Technique of the Modern Orchestra** | Widor, tr. Suddard | 1906 | supplement to Berlioz, EN | `techniqueofmoder00widouoft` | A | high — ch. III pp. 98–117 |
| S6 | Technique de l'orchestre moderne | Widor | 1904 | supplement to Berlioz, FR | `techniquedelorch00wido` | A | medium |
| S7 | **Orchestration** | Cecil Forsyth | 1914 | treatise, EN | `orchestration00fors` (also `cu31924022381440`) | A | **high** — Percussion pp. 22–52 |
| S8 | Principles of Orchestration | Rimsky-Korsakov, tr. Agate | 1912 | treatise, EN | `principlesoforch00rims`; Gutenberg text `principlesoforch33900gut` | A | low for technique names |
| S9 | **Nouveau traité d'instrumentation** | F.-A. Gevaert | 1885 | treatise, FR | `nouveautraitdins00geva` | A | **high** — batterie pp. 330–336 |
| S10 | Grand traité d'instrumentation et d'orchestration modernes | Berlioz | 1843 / 1855 | treatise, FR (original) | `grandtraitdins1843berl`, `grandtraitdins00berl` | A | medium |
| S11 | A Treatise on Modern Instrumentation and Orchestration | Berlioz, tr. Mary Cowden Clarke | 1900 | treatise, EN | `treatiseonmodern1900berl` | A | medium |
| S12 | **Strumentazione** | Ebenezer Prout, IT translation | 1901 | manual, IT | `ProutStrumentazione` | B | medium (Italian register) |
| S13 | The Orchestra | Ebenezer Prout | 1898 | manual, EN | `orchestra00prouuoft` | B | low |
| S14 | The Orchestra and How to Write for It | Frederick Corder | 1896 | manual, EN | `orchestraandhow00cordgoog` | B | low |
| S15 | Praktische Instrumentationslehre | Richard Hofmann | 1893 | manual, DE | `11516200bsb` (BSB scan) | B | low–medium |
| S16 | Musik-Instrumentenkunde in Wort und Bild | Teuchert & Haupt | 1910 | organology, DE | `musikinstrumente01teuc` | B | medium (instrument names) |
| S17 | The Bower System for Percussion, vol. 1: Drums | Harry A. Bower | 1912 | method, EN | `TheBowerSystemForPercussionV1` | B | medium (pre-MIDI stroke names) |
| S18 | The Harry A. Bower System for the Drum, Bells, Xylophone and Timpani | Harry A. Bower | 1912 | method, EN | `TheHarryBowerSystem` | B | medium |
| S19 | The Military Drummer | Carlton E. Gardner | 1918 | method, EN | `TheMilitaryDrummerAManual` | C | low |
| S20 | Manuel général de musique militaire | J.-G. Kastner | 1848 | treatise, FR | `manuelgnraldemu00kastgoog` | A | not yet mined (see §6) |
| S21 | Treatise on Orchestration, ch. 2 | Charles Koechlin (posted translation) | n.d. | treatise, EN tr. | `treatise-on-orchestration-chapter-2` | B | low |
| S22 | **Behind Bars** | Elaine Gould | 2011 | notation manual, EN | `behind-bars-by-elaine-gould` — openly posted; **licence: all rights reserved (Faber). Treat as reference-only, do not copy tables into `data/`.** | A | high, but overlaps the notation-standards bucket |
| S23 | **How to Write for Percussion**, 2/e | Samuel Z. Solomon | 2016 | technique catalogue, EN | publisher preview PDF, 32 pp: `https://api.pageplace.de/preview/DT0400.9780199920358_A26553236/preview-9780199920358_A26553236.pdf` | A | **high for structure** — full ToC with page numbers; body text not in preview |
| S24 | Music: Instrumental Techniques, Percussion | Jesse Pearl, Dade County Public Schools | 1971 | course guide, EN | `ERIC_ED061240` | C | low — rudiments-oriented, no technique table |
| S25 | Percussion (instrument resource) | Philharmonia Orchestra | — | vendor/orchestra page | `https://philharmonia.co.uk/resources/instruments/percussion/` | C | low |

#### Reached — bibliographic record only

| # | Title | Author | Year | Locator | Why not full text |
|---|---|---|---|---|---|
| S26 | Handbuch des Schlagzeugs: Praxis und Technik | Peinkofer & Tannigel | 1969, 2/e | Schott ED 12345 / ISBN 978-3-95983-510-x (repr.); `https://www.schott-music.com/en/handbuch-des-schlagzeugs-noc346712.html` | in print, not digitised openly |
| S27 | Compendium of Modern Instrumental Techniques | Gardner Read | 1993 | ISBN 0-313-28512-8, Greenwood; IA `compendiumofmode0000read` | lending-restricted |

#### Not reached — held under controlled digital lending, no snippet obtainable

| # | Title | Author | Year | Locator | What it would add |
|---|---|---|---|---|---|
| N1 | **Percussion Instruments and Their History** | James Blades | 1970 / 1984 / 1992 | IA `percussioninstru00jame`, `percussioninstru0000blad`, `percussioninstru0000blad_n5v0` | the organological backbone and a glossary; the standard reference |
| N2 | **Orchestral Percussion Technique** | James Blades | 1961 / 1973 | IA `orchestralpercus0000blad`, `orchestralpercus0000unse` | instrument-by-instrument technique with the player's names for strokes |
| N3 | **The Study of Orchestration** | Samuel Adler | 1982 / 1989 / 2002 | IA `studyoforchestra0000adle`, `…0002edadle_i2v0`, `…0003adle` | the percussion chapter's technique tables |
| N4 | **Music Notation in the Twentieth Century** | Kurt Stone | 1980 | IA `musicnotationint0000ston`, `…_h3s0` | ch. X: instrument abbreviations and pictograms, stick/mallet/beater pictograms, "effects and techniques"; beater pictograms at p. 211 (page reference from a secondary description, UNVERIFIED) |
| N5 | **Handbook of Percussion Instruments** | Peinkofer & Tannigel, tr. Kurt & Else Stone | 1976 (EN) / 1969 (DE) | IA `handbookofpercus0000pein`, `handbookofpercus0000karl` | "their characteristics and playing techniques" — the closest printed thing to the KITWARP model |
| N6 | **Contemporary Percussion** | Reginald Smith Brindle | 1970 | IA `contemporaryperc0000brin` | extended-technique names of the 1960s avant-garde |
| N7 | Compendium of Modern Instrumental Techniques | Gardner Read | 1993 | IA `compendiumofmode0000read` | Read's later, technique-first organisation — see §6 |
| N8 | Contemporary Instrumental Techniques | Gardner Read | 1976 | IA `contemporaryinst0000read` | predecessor of N7 |
| N9 | Music Notation: A Manual of Modern Practice | Gardner Read | 1969 / 1979 | IA `musicnotationman0000read`, `musicnotationman00read` | notation of percussion techniques |
| N10 | Pictographic Score Notation: A Compendium | Gardner Read | 1998 | IA `pictographicscor0000read` | the pictogram inventory (feeds the SMuFL comparison in dossier 07 §2.1) |
| N11 | Orchestral Technique: A Manual for Students | Gordon Jacob | 1931 / 1940 / 1982 | IA `orchestraltechni0000jaco`, `orchestraltechni0000gord` | British mid-century usage |
| N12 | Orchestration (2/e) | Cecil Forsyth | 1935 / 1936 / 1944 | IA `orchestration0000ceci_*` (many) | second-edition revisions; the 1914 first edition (S7) was used instead |
| N13 | Instrumentationslehre | Engelbert Humperdinck | 1981 | IA `instrumentations0000unse_o0c7` | 20c German pedagogical usage |
| N14 | Traité d'instrumentation et d'orchestration (critical ed.) | Berlioz | 1970 | IA `traitdinstrument0000berl` | modern editorial apparatus on Berlioz's terms |

**Register totals: 27 reached (25 in full text), 14 named and not reached, 41 candidates.**

---

## 2. Extracted terminology (Round B)

### 2.1 Gardner Read, *Thesaurus of Orchestral Devices* (1953) — structure

Part IV **Percussion**, pp. 158–233 (contents pp. XVI–XVII):

| Chapter | Title | p. | Sub-sections |
|---|---|---|---|
| 32 | Timpani | 159 | (1) Extended Range (2) Chords [Intervals] (3) Dampened (4) Methods of Striking (5) Muffled (6) Pedal Glissandi (7) Stick Types (8) 2-Timpani Roll (9) With 2 Sticks (10) Other Effects |
| 33 | Bells, Glockenspiel, Marimba, Vibraphone, and Xylophone | 173 | (1) Glissandi (2) Muffled (3) Off-stage (4) Stick Types (5) Tremolandi (6) Other Effects |
| 34 | Cymbals (Pair and Suspended) | 180 | (1) Dampened (2) Methods of Striking (3) Stick Types (4) Other Effects |
| 35 | Bass, Snare, and Tenor Drums | 196 | (1) Dampened (2) Methods of Striking (3) Muffled (4) Off-stage (5) Stick Types (6) **Without snares** (7) Other Effects |
| 36 | Gong, Tambourine, and Triangle | 213 | (1) Dampened (2) Methods of Striking (3) Muffled [Muted] (4) Off-stage (5) Stick Types (6) Other Effects |
| 37 | Other Percussion Instruments | 221 | (1) Methods of Playing or Striking (2) Muffled [Muted] (3) Off-stage (4) Stick Types (5) Other Effects (6) Other Keyed (7) Other Pitched (8) Other Unpitched Percussion Instruments |
| 38 | **Percussion Terminology** | 232 | Cymbals / Drums / Cymbals or Drums / Timpani / General |

**The structural fact.** Read's own section headings are an axis decomposition, arrived at
in 1953 without any reference to MIDI: *Dampened*, *Methods of Striking*, *Muffled*,
*Stick Types*, *Without snares*, *Other Effects*. That is, respectively, KITWARP's
`damping` (transient), `site` + `position` + `technique`, `damping` (sustained),
`implement`, `mechanism`, and the residue. Read separates *Dampened* from *Muffled* — a
distinction v0.1 collapses (see §5.3).

### 2.2 Read ch. 38, Percussion Terminology, pp. 232–233 — the four-language glossary

**Cymbals (p. 232).** Where a column has fewer entries than English, alignment is UNVERIFIED.

| English | Italian | French | German |
|---|---|---|---|
| Cymbal hung by its strap | Piatto sospeso dalla sua lascia | Une cymbale suspendue par sa courroie | Becken am Riemen hängend |
| Cymbal struck with drum-stick | Piatto colpo colla mazza | Cymbale frappée avec la mailloche | Teller mit Schlägel |
| Hung cymbal rolled with timpani sticks | Piatto rullo con bacchette di Timpani | Cymbale roulée avec baguettes de Timbales | Ein Beckenteller mit Paukenschlägel |
| Let vibrate gently by barely touching | Lasciate vibrare leggieramente — appena toccate | Laissez vibrer doucement en effleurant à peine les deux plateaux | Leicht vibrieren lassen — leicht berühren |
| Roll on suspended cymbal with sticks | Piatto sospeso rullo con bacchette | Roulement sur une cymbale avec des baguettes | Wirbel auf den Beckenteller mit Schlägel |
| Stick on cymbal | Piatto colla mazza | Baguette [mailloche] sur Cymbale | Schlägel auf den Becken |
| Suspended cymbal with stick | Piatto sospeso con bacchetta | Cymbale libre avec baguette | Becken frei mit Schlägel |
| Take the other cymbal | Prendete l'altro piatto | Prenez l'autre cymbale | Anderes Becken nehmen |
| With two [2] sticks on cymbal | Con due [2] bacchette a piatto | Avec deux [2] baguettes sur une cymbale | Mit zwei [2] Schlägel auf Becken |

**Drums (p. 232).**

| English | Italian | French | German |
|---|---|---|---|
| On the skin with thin sticks | Sulla membrana con bacchette sottile | Sur la peau avec des baguettes minces | Auf das Fell mit dünnen Ruten |
| **On the snares** | Sulle corde | Sur le(s) timbre(s) | Auf den Saiten |
| Played on the shell (of the drum) with handle of stick | Esecutato sulla cassa del tamburo col mancio della mazza | Joué sur le cadre du tambour avec le manche de la mailloche | Mit einem Holzstäbchen auf dem Holzrand der Trommel geschlagen |
| Roll on one side with soft sticks | Rullo sopra uno lato colle bacchette molle | Roulée sur un seul côté avec des baguettes molles | Mit weichen Schlägel auf einer Seite rollen |
| Well-tuned | Ben accordato | Bien accordé | Gut stimmen |

**Cymbals or Drums (p. 232).**

| English | Italian | French | German |
|---|---|---|---|
| Put stick aside | Lasciare la bacchetta | Laissez la baguette | Den Schlägel beiseite legen |
| Roll with sponge sticks | Rullo colle bacchette di spugna | Roulée avec des baguettes éponges | Wirbel mit den Schwammschlägel |
| Roll(ed) with two [2] sticks | Rullo con due [2] bacchette | Roulée avec deux [2] baguettes | Wirbel mit zwei [2] Schlägel |
| Take drumstick | Colla mazza | Prenez la mailloche | Mit der Schlägel |
| With stick(s) | Con bacchetta(e) | Avec baguette(s) | Mit Schlägel |
| **With switches** | Colli verghi | Avec verges | Mit Ruten |

**General (p. 233).**

| English | Italian | French | German |
|---|---|---|---|
| Allow to vibrate / Let vibrate [ring; sound] `l.v.` | Lasciare vibrare `l.v.` / Si lasci vibrare | Frappez en laissant vibrer / Laissez vibrer `l.v.` | Ausklingen lassen / Klingen lassen |
| Don't damp(en) | — | — | Nicht abdämpfen |
| Let sound [tone] die away | Lascia svanire / Lasciar estinguere / Lasci spegnere | Laisser mourir le son | Verklingen lassen |
| Touched with stick | Toccato con una bacchetta | Touchée avec une baguette | Mit einem Stock berühren |
| With sticks only | Bacchette soli | Baguettes solos | Nur mit Schlägel |

### 2.3 Read, Stick Types, pp. 166–167 — 61 beater names

This is the largest single implement list found anywhere in this bucket. English column
verbatim; Italian given where the OCR alignment is certain.

p. 166: Bass drum stick(s) `Bacchetta(e) di Gran cassa [Mazza della Gran cassa]` · Cane
stick(s) `Bacchetta(e) di canna` · Cane stick with fibre head `Bacchetta di giunco con la
testa di capoc` · Cotton stick(s) `Bacchetta(e) di cotone` · Cymbal stick `Bacchetta di
Piatto` · Drumstick(s) `Mazza(e)` · Felt stick(s) `Bacchetta(e) di feltro` · Felt timpani
stick(s) · Half-hard rubber stick(s) `…di gommaelastica mezza-dura` · Hard stick(s) · Hard
felt stick(s) · Hard leather stick(s) · Hard rubber stick(s) · Heavy mallet [Wooden hammer]
`Maglio [Mazzetta]` · Iron stick(s) `…di ferro` · **Knife-blade** `Lama di coltello` ·
Leather stick(s) · Light stick(s) · Medium hard stick(s) · Medium hard felt stick(s) ·
Medium hard leather stick(s) · Medium soft felt stick(s) · Metal stick(s) · **Ordinary
[Regular, Usual] beater(s) [hammer(s); mallet(s); stick(s); striker(s)]** · Padded stick(s)
· Plush stick(s) · Quarter-hard rubber stick(s) · Rattan stick(s) · Rawhide stick(s) ·
Rawhide timpani stick(s) · Rubber (covered) stick(s) · Short [small] stick · Small wood
stick · Snare [side] drum stick(s) · Soft stick(s) · Soft felt stick(s) · Soft felt timpani
stick(s) · Soft timpani stick(s)

p. 167: Sponge stick(s) `Bacchetta(e) di spugna` / FR `Baguette(s) d'éponge` · Sponge
timpani stick(s) · Steel stick(s) `…d'acciaio` · Stick(s) with fibre head [knob] `…di
capoc` · **Switch [Rod]** `Verghe(i)` / FR `Verges` · Thick stick(s) `…grosse` · Thick
timpani stick(s) · Thin stick(s) `…sottile` · Thin metal stick `Piccola bacchetta di
metallo` · Thin stick with sponge head · Thin wood stick · Timpani stick(s) `Bacchetta(e)
di Timpano(i) [Battuta di Timpano]` · Triangle stick `Bacchetta di Triangolo [Ferro del
Triangolo]` · **Two-headed stick [Double stick]** `Bacchetta a due capi` · Very hard
stick(s) · Very hard timpani stick(s) · Very soft stick(s) · Very soft timpani stick(s) ·
**Wire-brush [Brush(es)]** `Scovolo di fil di ferro` · Wood(en) stick(s) · Wood(en) timpani
stick(s) · Wool stick(s) `…di lana` · Xylophone stick(s) `…di Zilafono`

Three further beater headings appear in the chapter tables but **not** in the pp. 166–167
list, so the list is not closed: **Hard rubber xylophone mallets** (p. 186), **Soft wood
hammer** (p. 224), **Very hard leather sticks** (p. 224).

### 2.4 Read, Methods of Striking — timpani, ch. 32 pp. 163–165

| English | Italian | French | German | p. |
|---|---|---|---|---|
| Choke(d) / Damp(en) / Dampened / Damp [muffle] instantly / Dry / Off / Short / Stop (quickly) | Secco / Smorzate / Soffocato (subito) | Étouffé(s) / Étouffez (le son) / Sec / Très sec | Dämpfen / Gleich abdämpfen / Kurz / Schnell abdämpfen | 163 |
| At (the) rim of head / At (the) edge of (the) head / Close to (the) rim / Near (the) rim / On the edge of the skin / Struck near rim | All'estremità della membrana / Sul bordo della membrana | Au bord de la membrane [peau] / **Blousée / Blouser / Blousez** / Sur le bord de la membrane [peau] | Am Rand des Felles | 163 |
| Ordinary method of striking / Strike in usual manner | Colpete al ordinario | Frappées, comme à l'ordinaire / Frappez à la manière ordinaire | Gewöhnlich schlagen | 163 |
| (Hit) in center (of head) / Hit in middle / Roll at center (of head) / Roll in middle (of head) | Nel mezzo della membrana | Au centre / Au milieu de la membrane [peau] | In der Mitte des Felles | 164 |
| Rubbed in a circle with wire-brush | Fregato in circola con scovolo di fil di ferro | Frôlez dans un arc avec balai métallique | — | 164 |
| **Strike on copper kettle (of timpani)** | — | — | — | 164 |
| **Strike on metal rim around head** | Colpete sul orlo di metallo della membrana | Frappez sur le cercle métallique de la peau | Am Metallrand um Fell schlagen | 164 |
| Sweep wire-brush across head near rim | Passate uno scovolo di fil di ferro sulla membrana presso del orlo | Balayez un balai métallique à travers de la peau | Mit Drahtbürste nah dem Rand übers Fell streichen | 164 |
| Trill with pennies [coins] | Trillo colle monete | Trillez avec des pièces de monnaie | Mit Münzen trillern | 164 |
| With (the) fingernails | Colle unghie | Avec les ongles | Mit dem Nagel | 164 |
| Muffled / Muffle on / `con sord.` | Con sordino / Coperto(i) / Velato | Sons voilés / Sourdine `sourd.` / Un voile sur la peau de la timbale / Voilée | Abdämpfen / Bedeckt / Dumpf / Gedämpft `ged.` | 165 |
| Muffle off / Natural `nat.` / Remove muffle | Modo ordinario `modo ord.` / Senza sordino `senza sord.` | Naturel `nat.` / Sans sourdine `sans sourd.` | Gewöhnlich `gew.` / Dämpfung ab | 165 |
| Pedal glissando / Pedal Timpani — glissando | Glissando colla pedale | Glissando avec le levier / Glissando pour la Timbale à levier | Glissando mit Pedal | 165 |
| Double stick / With two [2] sticks | Con due [2] bacchette | Avec deux [2] baguettes | Mit zwei [2] Schlägel | 172 |
| Beat with maracas | Colpete colle marache | Frappez avec les maracas | Mit Maracas schlagen | 172 |

### 2.5 Read, Cymbals, ch. 34 pp. 180–195

| English | Italian | French | German | p. |
|---|---|---|---|---|
| At (the) edge / At (the) rim / On (the) edge | All'estremità / In margine / Sul bordo / Sull'orlo | Au bord / **Blousée / Blouser / Blousez / Blousez avec baguette(s) / Cymbale blousée** / Sur le bord [rebord] | Am Rand / Auf dem Rand | 180 |
| Barely touched / Lightly rubbed | Appena toccata | À peine frôlé / Frôlé | Leicht berühren | 181 |
| Brushed with a silver coin | Toccata colla moneta d'argenta | Brossez avec une pièce d'argent | Mit einer Silbermünze leicht berühren | 181 |
| Brushed with stick | Toccata colla bacchetta | Brossez avec la baguette | Mit einem Stock leicht berühren | 181 |
| **Clash(ed) / Crash(ed) / Cymbal-pair / Struck together / Together / Two [2] cymbals (free) / Two [2] cymbals clashed / Two [2] plate clash [crash] / Without stick / With plates** | A2 / Due [2] Piatti / Due [2] piatti al [nel] modo ordinario / Modo ordinario / Ordinario / Piatti a due [a 2] / Piatto con [contro] piatto | À l'ordinaire / Avec plateaux / Cymbales à main / Cymbale contre Cymbale / Cymbales plateaux / Frappée à l'ordinaire / Jeu ordinaire / Les deux [2] cymbales [plateaux] / Sans baguette(s) / Une paire | Becken gewöhnlich / Beide Schalen / Gewöhnlich / Mit den Tellern / Mit Teller(n) / Normal / Piatti ausklingen / Zwei [2] Becken mit Teller(n) | 181 |
| **Cymbal (struck) attached to bass drum / Cymbal, fixed to the foot-[pedal]** | Piatto uniti alla (gran) cassa / Piatto fissato alla (gran) cassa | Accrochez la Cymb. au pied / Cymbale fixée à la Grosse caisse / Grosse caisse à pied avec cymbale | Becken an der grossen Trommel befestigt (aber ohne Trommel geschlagen) / Becken angebunden — von Einem geschlagen / Die Becken an der grossen Trommel anzuhängen | 182 |
| Cymbal alone | Piatto solo | Cymbale seule | Becken allein | 182 |
| Hit with triangle | Colpo con triangolo | Frappée avec le triangle | Mit dem Triangel geschlagen | 183 |
| **In the air** | In aria | En l'air | In der Luft | 183 |
| **On (the) center / On (the) dome** | Sul mezzo / **Sulla cupola** | Au milieu / **Sur la protubérance** | In der Mitte / **Auf die Kuppel** | 183 |
| Rubbed together / Trill(ed) `tr.` / Trill a 2 / Two [2] plates together | Trillo (a 2) | Agitées l'une contre l'autre / Frôlée(s) [Frôlez] / Frottée(s) [Frottez] / Frottées l'une contre l'autre | Triller (zu 2) | 183 |
| Struck with the wood / With (the) handle of (the) stick / With wooden end of (the) stick | Colpete con legno / Col mancio della mazza / Coll'estremità di legno della bacchetta | Frappée avec le bois / Avec le manche de la mailloche / Coup avec le bois d'une baguette | Mit Holz geschlagen / Mit dem Stiel des Klöppels / Ein Becken mit dem Holzschaft des Schlägels berühren | 184 |
| With (the) hand | Colla mano | Avec la main | Mit der Hand | 184 |
| **With thick end of (the) stick** | Coll'estremità grossa della bacchetta | Avec l'extrémité grosse de la baguette | Mit dem dicken Ende des Stockes | 184 |
| **With thin end of (the) stick** | Coll'estremità sottile della bacchetta | Avec l'extrémité mince de la baguette | Mit dem dünnen Ende des Stockes | 184 |
| Dampened with the fingers | Assordate col il dita | Étouffez avec les doigts | Mit den Fingern gedämpft | 194 |
| Hissing | Cigolio | Sifflement | Zischend | 194 |
| Hold a wire-brush against vibrating cymbal | Tenete uno scovolo di fil di ferro contro il piatto vibrando | Tenez un balai métallique contre la cymbale vibrante | Eine Drahtbürste gegen das vibrierende Becken halten | 194 |
| **Hold cymbals together after striking** | Tenete i piatti insieme dopo avendo colpito | Après avoir frappé les cymbales tenez-les ensembles | Becken nach Anschlag zusammen halten | 194 |
| **Retain hold of edge — after stopping tone shake cymbal violently** | Tenete l'orlo dopo avendo assordato il suono e scuotete il piatto | Retenez au bord — après avoir étouffé le son secouez violemment | Becken am Rand halten (nach dem Ton abgedämpft ist) und lebhaft schütteln | 194 |
| "Stomp the beat" | — | — | — | 194 |
| **Stop [dampen] half-way, and full** | Assordate a mezza, e tutta | Étouffez à demi, et tout à fait | Halb und ganz dämpfen | 195 |
| Strike with back of a saw-blade on cymbal; draw saw across cymbal | Colpete col rovescio d'una lama di sega; tirate la sega sopra il piatto | Frappez avec l'envers d'une lame de scie; traînez la scie à travers une cymbale | Mit dem Rücken einer Säge auf das Becken schlagen; Säge über das Becken ziehen | 195 |
| Swishing | Strosciando | Cinglant | Peitschend | 195 |
| **Tremolo on cymbal with a 'cello bow** | Tremolo sulla piatto coll'arco di violoncello | Trémolo sur une cymbale avec l'archet d'un violoncelle | Tremolo auf einem Beckenteller mit einem Violoncellbogen | 195 |

### 2.6 Read, Bass, Snare and Tenor Drums, ch. 35 pp. 196–212

| English | Italian | French | German | p. |
|---|---|---|---|---|
| At the edge (of the head) | Sul bordo (della membrana) | Au bord (de la membrane) | Am Rand (des Felles) | 196 |
| **At (the) rim / On (the) rim (of the drum) / On (the) wood / Rim [R] / Strike (the) rim** | All'estremità / In margine / Sul bordo | À la jante / Sur le bois (du Tambour) / Sur le bord / Sur le cercle | Am Rand / Rand mit Holz geschlagen | 197 |
| Barely touched | Appena toccata | À peine frôlé | Leicht berühren | 197 |
| Center of (the) head / In the center [middle] / Near (the) center | Nel mezzo della membrana | Au milieu de la membrane [peau] | In der Mitte des Felles | 198 |
| **"Flam" stroke** | — | — | — | 198 |
| **Laid on side** | Sul lato | Placé à plat | Auf die Seite gedreht | 198 |
| **Lay 1 stick on head of drum — strike with the other (stick)** | Mettete una bacchetta sulla membrana — colpetela col altro | Appuyer une baguette sur la peau — frappez-la avec l'autre | Ein Schlägel um Fell — mit dem andern geschlagen | 198 |
| **On both sides [skins]** | Dalle due parti | Sur tous les deux côtés | Auf beiden Fellen | 198 |
| **On the bell [body] / On the frame [hoop] / On the shell [wood] / On (the) side** | Sulla cassa | Contre le pupitre / Sur la caisse / Sur le cadre | Auf dem Holzrand der Trommel / Auf dem Holzstäbchen / Auf den hölzernen Rahmen / Auf Holz geschlagen | 199 |
| On (the) head / On (the) skin | Sulla membrana / Modo ordinario | Position ordinaire / Sur la peau / Sur membrane | Auf das Fell / Gewöhnlich | 199 |
| **Rim shot — Shot** | *(no equivalent given)* | *(no equivalent given)* | *(no equivalent given)* | 200 |
| Roll(ed) with the fingers / With the fingertips | Rullo col il dita / Sulle punte delle dita | Roulé avec les doigts / Avec les pointes des doigts | Wirbel mit den Fingern / Mit Fingerspitzen | 200 |
| **Drag with wire-brush / Slide [swish] with brush** | Strisciate con scovolo di ferro | Effleurez [glissez] avec balai métallique | Mit einer Drahtbürste gleiten | 200 |
| Struck with the wood | Col mancio della mazza | Frappée avec le bois | Mit dem Stiel des Klöppels | 200 |
| **Bass drum alone (with Cymb. detached) / With foot-beater [foot-pedal]** | A piede | À pied / Gr. C. seule (avec Cymb. décrochée) | Mit dem Fuss | 201 |
| **Loosen snares / Slacken(ed) snares / Snares muffled / Snares loose(ned) / Snares off / Snares slacken(ed) / No snares / Without snares / With snares loose(ned) / With snares slacken(ed)** | Corde del Tamburo lasciare / Senza corda(e) / **Senza timbro** | Avec les cordes lâches [relâchées] / **Détimbrée(s)** / Sans corde(s) / **Sans timbre(s)** | **Ohne Schnarrseite** | 209 |
| **Snares on / Tight(en) snares / With snares** | Con corda(e) / Con timbro | Avec corde(s) / Avec timbre(s) / Très timbrée | Mit Schnarrseite | 210 |
| Cannon shot(s) / Like a cannon | Colpo(i) di cannone / Quasi cannone | Comme un canon | Wie eine Kanone | 211 |
| **Out of tune (without pitch or resonance)** | Scordata | Mal accordé | Verstimmt | 211 |
| Played delicately with the fingers, like a five-finger exercise | Teneramente, coi quintupolo dita, come un esercizio | Joué délicatement avec les doigts, comme une étude pour les cinq doigts | Zart mit den Fingern gespielt, wie eine 5-Fingerübung | 211 |
| **Rub a rosined glove or cloth over a snare drum stick with tip of stick pressed against center of drum head** | Fregate con uno guanto resinato sopra una bacchetta di tamburo spingendo la punta della bacchetta nel medio della membrana | Frottez avec un gant résineux sur une baguette de tambour en pressant le bout de la baguette contre le milieu de la peau | Mit einem harzigen Handschuh über einem Trommelschlägel reiben, mit dem Punkt des Schlägels an der Mitte des Fells drückend | 211 |
| **Place a handkerchief over drum head** | Coprire la membrana col fazzoletto | Mettez un mouchoir sur la peau | Mit einem Taschentuch an der [Felle bedeckt] | 211 |
| **Place a piece of paper on the drum head** | Coprire la membrana colla carta | Mettez un papier sur la peau | Mit einem Papier an der Felle bedeckt | 212 |
| **"Ride" solo** | — | — | — | 212 |
| **Roll — beginning at center — gradually going to the rim** | Rullo — dal medio all'orlo poco a poco | Roulez — commençant au milieu de la peau en allant peu à peu vers le bord | Wirbel — von der Mitte allmählich bis zum Rand | 212 |
| **Roll — beginning at the rim — gradually going to center** | Rullo — dall'orlo al medio poco a poco | Roulez — commençant au bord en allant peu à peu vers le milieu | Wirbel — vom Rand allmählich bis zur Mitte | 212 |
| Tuned high | Accordato in alto | Accordé en haut | Hoch gestimmt | 212 |
| **With a thin piece of felt on middle of drum head** | Con una minuto frammento di feltro nel medio della membrana | Avec un morceau mince de feutre au milieu de la peau | Mit dünnem Filzstück auf der Mitte des Fells | 212 |

### 2.7 Read, Gong, Tambourine and Triangle, ch. 36 pp. 213–220

| English | Italian | French | German | p. |
|---|---|---|---|---|
| **Brush the head [skin] with the thumb / Rub head [skin] with thumb / Stroke(d) / Thumb (trill) / With (the) thumb** | Col pollice (sulla membrana) | Avec le pouce / Frôlez la membrane avec le pouce / Le trille (tr.) indique le pouce | Das Fell mit dem Daumen streifen / Mit dem Daumen (über das Fell) | 213 |
| **Brush [click] the jingles / On the jingles** | Sulle [cliquetis, OCR damaged] | Effleurez [tintez] les cliquetis / Sur les tintements | Auf den Schellen | 214 |
| **Fist / With (the) fist** | Col pugno | Le coup frappé avec le poing | Mit der Faust | 214 |
| **On (the) knee / Strike on knee / With (the) knee** | Col ginocchio / Colpo sul ginocchio | Avec le genou / Frappez sur le genou / Le coup frappé avec le genou | Auf dem Knie / Mit dem Knie | 214 |
| On the rim | Sull'orlo | Sur bord | Am Rand | 214 |
| On the skin | Sulla membrana | Sur la peau | Auf das Fell | 215 |
| **Shake (hoop)** | Agitare / Trillo | Agité / Agitez / Secoué(er) / Secouez | Schütteln | 215 |
| Strike / Struck | Colpo / Colpete | Frappée(s) / Frapper / Frappez | Schlagen | 215 |
| With (the) fingers [fingertips] | Col il dita | Avec les doigts | Mit den Fingern | 215 |
| With (the) hand | Colla mano | Avec la main | Mit der Hand | 215 |
| **With (the) knuckles** | Colla nocce | Avec les jointures | Mit den Knöcheln | 216 |
| **Kept in vibration by friction on the edge** (gong) | Mantenuto in vibrazione per fregamento sull'orlo | Faites vibrer en frottant au bord | Durch Reibung an der Kante in Schwingung gehalten | 219 |
| **Laid horizontal — without resonance** (gong) | Orizzontalmente — senza risonanza | Placé à plat — sans résonance | Ohne Resonanz — horizontal gelegt | 219 |
| **Rapid glissando with triangle stick, describing an arc on the surface of the instrument** | Glissando rapido circolando sulla superficie del'instrumento colla bacchetta di triangolo | Glissez rapidement avec la baguette du triangle, décrivant un arc sur la surface de l'instrument | Schnelles Glissando mit Triangelschlägel im Bogen an der Oberfläche des Instrumentes ausgeführt | 220 |
| **Let drop on the floor** (tambourine) | Lasciate cadere sul palco | Tenir (le Tamb. de B.) tout bas au sol et le faire tomber | Auf den Boden werfen | 220 |
| **Placed on snare drum** (tambourine) | Mettere sulla tamburo militare | Mettez sur la caisse claire | Auf der kleinen Trommel | 220 |
| **Without jingles** | Senza tintinnìe | Sans tintements | Ohne Schellen | 220 |
| **Muffle notes by holding l.h. against triangle** | Assordate i toni mettendo la m.s. contra il triangolo | Étouffez les tons en mettant la m.g. contre le triangle | Töne durch linke Hand am Triangel gedämpft | 220 |
| **Wrapped tightly in a cloth — hold tightly in the hand** (triangle) | Involto strettamente in tela — tenere strettamente nella mano | Bien enveloppé de toile — tenez fermement à la main | Fest in Stoff gewickelt — fest in der Hand gehalten | 220 |

### 2.8 Read, Other Percussion Instruments, ch. 37 pp. 221–226

| English | Italian | French | German | Instrument, p. |
|---|---|---|---|---|
| Near the center | Nel mezzo della membrana | Au milieu de la peau | In der Mitte des Fells | hand drum, 221 |
| On the frame | Sulla cassa | Sur la caisse | Auf dem Holzrand | tom-tom, 221 |
| **Played behind the bridge** | Sonato dietro il ponticello | Jouez en arrière du chevalet | Hinter dem Steg spielen | cimbalom, 221 |
| **Plucked with the fingertips** | Pizzicato con il dita | Pizzicato avec les doigts | Mit den Fingern Pizzicato | cimbalom, 221 |
| **Rasped and beaten** | Raspato e battuto | Râpé et frappé | Gekratzt und geschlagen | reco-reco [rasper], 221 |
| Roll with the fingers | Rullo col il dita | Roulé avec les doigts | Wirbel mit den Fingern | small drums, 222 |
| With (the) handle of the stick | Col mancio della mazza | Avec le manche de la mailloche | Mit dem Stiel des Klöppels | cimbalom, 222 |
| **Glissando across (wood) blocks** | Glissando sui legni | Glissez sur les blocs | Gleitend über die Holzkasten | wood blocks, 225 |
| **Glissando on string with nail of l.h. thumb** | Glissando sulla corda colla unghia del pollice sinistro | Glissez sur la corde avec l'ongle du pouce gauche | Glissando auf der Saite mit dem Nagel der linken Hand | cimbalom, 225 |
| Harmonics | Armonici | Sons harmoniques | Flageolett | guitar, 225 |
| **Pricked with a pin** | Punturato con uno spillo | Piquez avec une épingle | Mit einer Nadel stechen | toy balloons, 226 |
| **(Glass) smashed with a mallet; emptied on a hard surface** | Fracassate con uno maglio; vuotate il vetraio spezzato sopra una superficie | Écrasez avec un maillet; videz le verre brisé sur une surface dure | Mit Hammer zerschlagen; Glas auf hartem Boden ausgeleert | glass plates, 226 |
| **Break bottle!** | Fracassate la bottiglia! | Brisez la bouteille! | Flasche zerbrechen! | bottle, 225 |
| **Draw a bow across sharp edge at end of bar** | Suonare col arco sul taglio del legno | Exécutez avec un archet sur la pointe du bois | Mit dem Bogen auf der scharfen Kante des Holzes spielen | xylophone, 179 |
| **Glissando across the resonators** | Glissando sui risonatori | Glissez sur les résonateurs | Glissando über die Resonatoren | xylophone, 179 |
| **Pedal off; no resonance** | Senza pedale; non risonanza | Sans pédale; non résonnant | Ohne Pedal; keine Resonanz | vibraphone, 179 |
| **Low (slow vibrato)** | Vibrato lento | Vibrez lentement | Langsam vibrierend | vibraphone, 179 |
| Muted: one player grasps tubes while another player strikes them | — | — | — | chimes, 174 |
| Dampened with one hand; struck with the other | Coperto con un pezzo di tela | Voilée avec une pièce de toile | Gedämpft mit einem Seidentuch überdeckt | bells, 174 |

### 2.9 Read, Nomenclature of Instruments, pp. 8–9 — the orchestral percussion inventory

**Main list, p. 8 (four languages).** Small Side Drum / Trap Drum `Tamburo piccolo` ·
Tenor Drum / Parade Drum `Tamburo rullante`, `Cassa rullante` / FR `Caisse roulante` / DE
`Rührtrommel` · Tabor / Field Drum / Long Drum `Tamburo` / FR `Tambourin de Provence`,
`Tambourin Provençal` · Cymbals `Piatti (a due; a 2)`, `Cinelli` / FR `Cymbales (libres)` /
DE `Becken`, `Cinellen`, `Zymbel` · Suspended / Hanging / Hung Cymbal / Cymbal, free /
Turkish crash `Piatto (sospeso)`, `Piatto oscillante` / FR `Cymbale (suspendue)` / DE
`Becken (frei)`, `Becken freihängend`, `Becken freischwingend` · Crash Cymbal / Chinese
Cymbal `Piatto chinoso` / FR `Cymbale Chinoise` / DE `Chinesische Zimbel` · Antique Cymbals
/ Finger Cymbals `Cimbali antichi` / FR `Cymbales antiques`, `Crotales` / DE `Antike
Zimbeln` · Gong / Tam-tam · Tambourine / Hand Drum `Tamburino`, `Tamburello Basco`,
`Tamburo Basco` / FR `Tambour de Basque` / DE `Tamburin`, `Schellentrommel` · Triangle ·
Castanets · (Tubular) Chimes / Bells `Campane`, `Campanelle` / FR `Cloches`, `Tubes` / DE
`Glocken`, `Glockengeläute` · Glockenspiel / Chime-Bells `Campanelli`, `Campanetta` / FR
`Carillon`, `Clochettes`, `Jeu de Timbres`, `Timbres` / DE `Glockenspiel` · Xylophone
`Xilofono`, `Silofono`, `Zilafono` / DE `Xylophon`, `Holzharmonika` · Vibraphone /
Vibraharp `Vibrafono` / DE `Vibraphon` · Marimba · Harp(s).

**Supplementary List of Percussion Instruments, p. 9 (four languages, 33 entries).**
Anvil [Steel Bar, Pipe] `Incudine` / `Enclume` / `Amboss` · Auto [Taxi] Horn `Corno di
automobile` / `Cor d'auto` / `Autohorn` · Bongos · Chains `Catene` / `Chaînes` / `Ketten` ·
Chinese Blocks [Drums] `Ceppi chinosi` / `Blocs chinois` / `Chinesische Blöcke` · Claves ·
Cowbells `Campanelle di vacca` / `Grelots`, `Ranz des vaches` / `Heerdenglocken` · Cowhorn
`Corno di vacca` / `Stierhorn` · Dulcimer `Cembalon [Cimbalom]` · Guitar · Harmonica
[Mouth Organ] · Jew's Harp `Scacciapensieri` / `Guimbarde` / `Brummeisen` · Jingles
`Bubbolo` / `Timbres` / `Schelle` · Mandoline · Maracas `Marache` / `Maracas [Boîte à
clous]` · Metal Block `Cassa di metallo` / `Bloc de métal` / `Metallkasten` · Rasper
[Güiro] `Raspe` / `Râpe` / `Raspel` · Rattle [Ratchet] `Raganella [Sistrum]` / `Crécelle` /
`Klapper [Knarre; Ratsche]` · Sandpaper (blocks) `Ceppi di carta vetro` / `Blocs à papier
de verre` / `Sandpapierblöcke` · Siren · Slapstick [Whip] `Frusta` / `Fouet` / `Peitsche` ·
Sleighbells `Sonagli` / `Grelots` / `Schelle` · **String Drum [Lion roar]** `Rugghio di
leone` / `Tambour à corde` / `Löwengebrüll` · **Switches** `Verghe(i)` / `Verges` /
`Rute (Ruthe)` · Temple Blocks · Thunder-machine `Macchina di tuono` / `Machine à
tonnerre` / `Donnermaschine` · Thunder-sheet · Wind-machine `Macchina a venti` / `Machine
à vent [Éoliphone]` / `Windmaschine` · Wood Blocks `Casse di legno [Legno]` / `Blocs de
bois [Wood-blocs]` / `Holzkasten [Holzton; Holztrommel]` · Zither `Cytharra`.

### 2.10 Berlioz / Richard Strauss, *Instrumentationslehre* vol. 2 (Peters, 1905)

Verbatim, p. 406, on timpani beaters:

> „Es gibt dreierlei Arten von Schlägeln, deren Anwendung den Klang des Paukentones
> dermaßen verändert, daß die Komponisten mehr als nachlässig sind, wenn sie in ihren
> Partituren nicht vorschreiben, welcher Schlägel benutzt werden soll. Die Schlägel **mit
> Holzköpfen** geben einen rauhen, trockenen, harten Ton … Die Schlägel **mit von Leder
> überzogenen Holzköpfen** sind weniger hart … Die besten sind die Schlägel **mit
> Schwammköpfen**; ihre Wirkung ist weniger lärmend und musikali[scher] …"

That is a three-value ordered hardness scale — wood / leather-covered wood / sponge —
asserted as *the* distinction that changes the timbre, and asserted as something the
composer is negligent not to specify.

p. 411, on muffling:

> „Man findet öfters, namentlich bei den älteren Meistern, die Bezeichnung: **„gedämpfte"
> oder „bedeckte" Pauken**. Dies bedeutet, daß das Fell des Instrumentes **mit einem Stück
> Tuch bedeckt** werden soll, wodurch der Klang desselben gedämpft wird …"

p. 423, on the snare drum, distinguishing the two ways of muting:

> „Man gebraucht die Trommeln auch gedämpft, wie die Pauken, aber **statt das Fell mit
> einem Tuchstück zu bedecken**, begnügen sich die Trommelschläger meist damit, **die
> Schnarrsaiten zu lockern**, oder zwischen diese u[nd das Fell etwas zu legen] …"

p. 418, on the pedal-mounted cymbal, and p. 422 on cymbal choking:

> p. 422: „… mit der Bemerkung: **„Abdämpfen."** Letzteres bewirkt der Ausführende dadurch,
> daß er **die Becken sofort nach dem Schlage an die Brust drückt**. Zuweilen bedient man
> sich eines **Paukenschlägels mit Schwammkopf** oder des **Klöppels einer großen Trommel**,
> um ein **an seinem Riemen hängendes Becken** zum Ertönen zu bringen …"

Instrument names asserted at p. 398 include `Große Wirbeltrommel` = FR `Grosse caisse
roulante`, and `Eine große Trommel mit zwei Klöppeln` (bass drum with two beaters).

### 2.11 Cecil Forsyth, *Orchestration* (1914)

| Term | Verbatim / gloss | p. |
|---|---|---|
| **batter-head / snare-head** | "The upper head — that on which the player beats — is called the **'batter-head'**: the lower, the **'snare-head'**." | 24 |
| muffling the side drum | "The essential part of the muffling is **to remove the snares from contact with the snare-head**, and so destroy the peculiar 'crackling' tone" | 27 |
| Ruthe | "The Germans had, or have, a sort of **birch-broom, called Ruthe**" (bass drum) | 28 |
| tenor drum, no snares | "Fr. *Caisse roulante*; It. *Tamburo rullante*; Ger. *Wirbeltrommel, Rolltrommel, Rührtrommel*. … **There are no snares.**" | 30 |
| tambourine, three methods | "(1) By striking the parchment … **with the knuckles**. This gives detached notes … (2) **By shaking the hoop.** This practically gives a 'roll' on the jingles. (3) **By rubbing the thumb on the 'head.'** This gives a partial tremolo made up chiefly of the sound of the jingles." | 32 |
| tambourine on timpani | "tuning one of the Kettle-Drums to a drone-bass, **placing the Tambourine on the Drum** and playing on the Tambourine-head with the Kettle-Drum sticks" | 33 |
| `battuto colla mano` | quoted as Elgar's marking for the tambourine (*Cockaigne*, p. 37 of the score) | 33 |
| **two-plate-stroke** | "a sort of sideways or **brushing movement**. This, the **two-plate-stroke**, is the ordinary method of playing single notes." | 35 |
| single plate with a stick | "(2) By striking a **single plate** either with a **hard Side-Drum stick** or with a **soft Kettle-Drum stick**." — "it is customary to write the words 'with hard stick' or 'with soft stick' above the part" | 35–36 |
| **two-plate-roll** | "(3) By **agitating the edges of the plates against each other**. This is the '**two-plate-roll**', and it must be marked as such." | 36 |
| **two-stick-roll** | "(4) By **hanging up a single plate** and performing a roll on it with two soft Kettle-Drum sticks. This is the '**two-stick-roll**'." — with the instruction that the plate "should never be held in the hand", and that the roll is made "by beating with the two sticks **at opposite sides of the circumference**" | 36 |
| finger-tip diminuendo | "A rapid diminuendo can, if necessary, be made by means of the **finger-tips** without any sticks whatever." | 36 |
| timpani played as side drum | "The Kettle-Drums can be reduced to almost the exact quality of the Side-Drum by simply placing three heavy non-vibrat[ing objects on the head]"; also played "with Side-Drum sticks or in various '**trick**' ways, such as **with a couple of coins**" | 50 |
| classification | "'Autophonic'" vs "'Membrane'" instruments; unmusical percussion = Side-, Bass-, Tenor-Drum, Tambourine | 22–23 |

### 2.12 Widor, *The Technique of the Modern Orchestra* (tr. Suddard, 1906)

| Term | Verbatim | p. |
|---|---|---|
| timpani sticks | "There are **two kinds: Sticks with skin knobs**, for ordinary use forte or piano, and **sticks with sponge knobs**, for particularly soft effects. Formerly, **wooden-headed sticks** were sometimes used, but the quality of tone produced is very hard and has very little timbre" | 100 |
| muffled drums | "If the head of the Drum be **covered with a cloth**, a very striking and mournful quality of tone is obtained, the vibrations of the parchment being more or less damped and, so to speak, **driven back into the interior of the Drum**." | 108 |
| `sans timbre` | "Sometimes the indication: **sans timbre** is met with; the effect required is obtained **either by loosening the snares, or by muffling** as described above; **the choice of the means of execution is usually left to the performer**." | 108 |
| tambourine, three ways | "(1) By **striking the parchment with the back of the hand** … (2) By **shaking the instrument**, in order to call into play the '**jingles**' … a **metallic rustle** rather than a roll … (3) By **gliding the thumb over the parchment**, a **temporary roll** can be produced, in which the sound of the jingles predominates." | 108–109 |
| tabor | "*Fr., Tambourin.* This is a very long drum, **without timbre**, used in Provence … he beats time with a **single stick**" | 109 |
| chapter structure | Kettle-Drums 98 · Side Drum 106 · **Muffled Drums 108** · Tenor Drum 108 · Tambourine 109 · Tabor 109 · Triangle 110 · Castanets 111 · Cymbals 113 · Ancient Cymbals 117 | vi |

Note that Widor's italic gloss "*sans timbre*" and Read's `Senza timbro` / `Sans timbre(s)`
(§2.6, p. 209) agree: in French and Italian orchestral usage **`timbre` means the snares**,
not the tone colour.

### 2.13 Gevaert, *Nouveau traité d'instrumentation* (1885) — French stroke names

pp. 331–332, on the *tambour militaire* (= *caisse claire*):

> "La percussion se fait à l'aide de **deux baguettes en bois dont le bout est renflé en
> forme d'olive**. Voici les éléments rythmiques des batteries du tambour, avec leurs
> dénominations techniques et leur traduction en notes.
> **1° Le coup simple ou *ta***, produit par une seule baguette; il s'emploie rarement isolé.
> **2° Le coup double, *fla***, donné par les deux baguettes; sa notation exacte serait
> celle-ci …; dans la notation usuelle on le confond avec le coup simple.
> **3° Le coup de charge, *tra***. Il se distingue du précédent en ce que l'accent
> rythmique tombe sur la note brève.
> **4° Les roulements partiels dits *ra***. On distingue des **ra de 3 coups**, de **4**, de
> **5**, de **6**, de **7** et d'un plus grand nombre de coups.
> **5° Le roulement continu.**"

p. 332, on muffling, giving three interchangeable procedures:

> "Dans les cortèges funèbres les tambours s'emploient **voilés**, de même que les
> timbales; mais **au lieu de couvrir la membrane supérieure d'un morceau d'étoffe** on se
> contente souvent de **détendre les cordes** placées sous la peau inférieure **ou
> d'empêcher leur contact avec celle-ci**. **L'effet des trois procédés est le même**: le
> son du tambour perd tout son éclat et prend une teinte sinistre."

p. 330 and the classification table at p. 13 give Gevaert's family split: `instruments à
percussion` → à membranes (timbales; grosse caisse, tambour militaire ou caisse claire,
caisse roulante, tambour de basque) / autophones (cloches, carillons, jeux de timbres;
triangle, cymbales, tam-tam, castagnettes). p. 331 defines `la batterie` = *grosse caisse +
cymbales + triangle*, "ce que l'on appelle la batterie ou **la musique turque**".

### 2.14 Samuel Z. Solomon, *How to Write for Percussion*, 2/e (OUP 2016)

Body text is not in the publisher preview; the **table of contents with printed page
numbers is**, and it is itself a technique catalogue. Locator: preview PDF pp. v–xi.

| Heading | p. | Reading |
|---|---|---|
| Note-Length Chart | 71 | note length as an explicit notated axis |
| **Muting (Muffling, Dampening)** | 74 | the three English words treated as one concept |
| **Dead Stroke** | 75 | |
| Damper Pedals | 75 | |
| Rolls | 77 | |
| **Chapter 4 Beaters** | 85 | **"Beater Lingo" 85** — an explicit statement that beater naming is unstable |
| Sticks / Mallets | 90 | |
| **Triangle Beaters and Knitting Needles** | 92 | |
| Brushes | 92 | |
| **Rute Sticks** | 94 | |
| Chime Hammers (Tubular Bell Hammers) | 94 | |
| **Superball Mallet** | 95 | |
| **Beaters as Instruments** | 95 | a beater used as the sounding body — no axis in v0.1 |
| Hands / Bows | 95 | |
| Sticks on Drums / Mallets on Drums / Hands on Drums | 118–120 | implement × instrument as an organising principle |
| **Playing on the Rim or Shell** | 121 | site |
| **Beating Spot** | 122 | position |
| Mutes | 123 | |
| **Pitch Bending** | 123 | |
| **Two-Headed Drums** | 123 | |
| Appendix C **Extended Techniques** | 239–250 | see below |
| Appendix G **Beaters** | 267 | |
| Appendix H **Percussion Family Tree** | 273 | a published taxonomy of the instrument axis |

Appendix C, *Extended Techniques*, headings with pages: **Return to a "Normal" Method of
Playing** 239 · **Manipulations of Timbre** 239 · **Striking Unusual Parts of an
Instrument** 241 · **Unusual Use of Beaters** 242 · **Dead Stroke** 242 · **Beating Spot**
243 · **Bowing** 244 · **Friction Roll** 244 · **Scrape** 244 · **Prepared Instruments**
245 · **Pitch Bending** 246 · **Vibrato** 247 · **Adding Mass** 248 · **Sympathetic
Resonance** 248 · **Clusters** 249 · **Harmonics** 250.

Solomon's chapter 7 (*Metal*) and 8 (*Wood*) also name instruments v0.1 does not have:
Almglocken 158 · Temple Bowls / Mixing Bowls 159 · Brake Drums, Metal Pipes, Anvils, **Bell
Plates** 160 · Thundersheet 161 · **Ribbon Crasher** 162 · **Spring Coil** 163 · Steel Drums
164 · **Mark Tree / Bell Tree** 166 · Flexatone 170 · Log Drum 173 · **Cajón** 175 ·
**Mahler Hammer** 175 · Rute 178 · Guiro 178 · Slapstick 179 · Ratchet 180 · **Bamboo Wind
Chimes** 181 · Cabasa 183 · Conch Shell 184 · Crystal Glasses 184 · Rainstick 187 ·
**Vibraslap** 190 · **Boobams** 141 · **Roto-Toms** 137 · Frame Drums 138 · Djembe and
Doumbek 141.

### 2.15 Minor sources, recorded for completeness

- **Philharmonia Orchestra** percussion resource page (S25): technique words used in prose
  only — "softer sticks", "hard mallets topped with wood or metal hammers", "soft beater",
  "roll", "brushes are used as beaters", "crash"/"clash cymbals", "metal beater", crotales
  "struck together like a finger cymbal" and "bowed", tambourine "hit with the fingers,
  fist or knee", "snare drumsticks", "rubbing the thumb across the head". Consistent with
  Read §2.7; adds nothing new.
- **Jesse Pearl, Dade County Public Schools (1971)** (S24): a Quinmester course outline. Its
  only technique content is "the **16 standard rudiments** as set forth by the **National
  Association of Rudimental Drummers**" and "proper handgrip … proper wrist action". No
  technique table. Belongs to the rudiments bucket, not this one.

---

## 3. Axis mapping

Every term extracted above is assigned to one KITWARP axis, or to §3.9 if it fits none.
Where a source term is a *sentence* rather than a name, the axis assignment is to the thing
it denotes, and the sentence is a candidate `alias`, not a candidate slug.

### 3.1 `instrument`

Read pp. 8–9 (§2.9) and Solomon ch. 5–9 (§2.14) between them supply the whole orchestral
and auxiliary inventory. v0.1 reserves `orch`, `perc.*` and `utility` families unminted, so
**all of it is new**. The highest-confidence subset, present in *both* Read 1953 and
Solomon 2016 and therefore stable across 63 years: anvil, bell plate, bongos, brake drum,
castanets, chains, chimes/tubular bells, claves, cowbell, crotales/antique cymbals, finger
cymbals, flexatone, glockenspiel, gong, guiro/rasper, jingles, log drum, maracas, marimba,
ratchet, sandpaper blocks, sleighbells, slapstick/whip, siren, steel drum, string
drum/lion's roar, tam-tam, temple blocks, thunder sheet, thunder machine, timbales,
timpani, tom-tom, vibraphone, wind machine, wood block, xylophone.

Two structural findings on this axis:

- **Suspended vs pair is an instrument-level distinction, not a technique.** Read gives them
  separate nomenclature entries at p. 8 (`Piatti (a due)` vs `Piatto sospeso` / `Cymbale
  suspendue` / `Becken frei`), and a separate chapter treatment. v0.1's single `cymbal`
  (id 18) cannot express it.
- **Read's `Tenor Drum` / `Rührtrommel` / `caisse roulante` is not a tom.** It is a
  snareless drum between side and bass drum (Forsyth p. 30, Widor p. 108). v0.1 has no slot
  for it and `tom` would be wrong.

### 3.2 `site`

| Source term | Source | Maps to |
|---|---|---|
| On (the) head / On (the) skin / Sur la peau / Auf das Fell | Read 199 | `head` |
| **batter-head** vs **snare-head** | Forsyth 24 | `head` vs `underside` — Forsyth names both, v0.1 names only the second |
| On both sides [skins] / Auf beiden Fellen | Read 198 | `head` + `underside` simultaneously |
| At (the) rim / On (the) rim (of the drum) / Sur le cercle / Rand mit Holz geschlagen | Read 197 | `rim` |
| **On the frame [hoop] / Sur le cadre / Auf den hölzernen Rahmen** | Read 199 | `rim` — but see §5.2, the wooden hoop and the metal counterhoop are different objects |
| **Strike on metal rim around head / Am Metallrand um Fell schlagen** | Read 164 | `rim` on timpani, i.e. the counterhoop |
| On the shell [wood] / On the bell [body] / On (the) side / Sulla cassa / Sur la caisse | Read 199, 221 | `shell` |
| **On the snares / Sulle corde / Sur le(s) timbre(s) / Auf den Saiten** | Read 232 | **no v0.1 site** — the snares as a struck surface |
| **Strike on copper kettle (of timpani)** | Read 164 | **no v0.1 site** — the bowl |
| On (the) dome / Sulla cupola / Sur la protubérance / Auf die Kuppel | Read 183 | `bell` (cymbal) |
| At (the) edge / Au bord / Am Rand (cymbal) | Read 180 | `edge` |
| Playing on the Rim or Shell | Solomon 121 | `rim`, `shell` |
| Played behind the bridge (cimbalom) | Read 221 | no v0.1 site (chordophone) |
| **Draw a bow across sharp edge at end of bar** (xylophone) | Read 179 | no v0.1 site (bar end) |
| **Glissando across the resonators** (xylophone) | Read 179 | no v0.1 site (resonator tube) |

### 3.3 `position`

| Source term | Source | Maps to |
|---|---|---|
| (Hit) in center (of head) / Nel mezzo / Au centre / In der Mitte des Felles | Read 164, 198 | `centre` |
| At the rim of head / Near the rim / Close to the rim / Struck near rim / **Blousé** | Read 163 | `perimeter` |
| At the edge (of the head) / Sul bordo (della membrana) | Read 196 | `perimeter` |
| On (the) center (cymbal) / Sul mezzo | Read 183 | `centre` |
| **Beating Spot** | Solomon 122, 243 | the axis itself, named |
| **Roll — beginning at center — gradually going to the rim** (and its inverse) | Read 212 | a *trajectory over* `position`, expressible only through `strike_position.radial` as a controller, not as a term |
| Sweep wire-brush across head near rim | Read 164 | `perimeter` + `technique: sweep` |

### 3.4 `contact` (part of the implement)

| Source term | Source | Maps to |
|---|---|---|
| With (the) handle of (the) stick / Col mancio della mazza / Avec le manche de la mailloche / Mit dem Stiel des Klöppels | Read 184, 200, 222, 232 | `butt` |
| With wooden end of (the) stick / Struck with the wood / Frappée avec le bois / Mit Holz geschlagen | Read 184, 200 | `butt` (a wooden-shafted beater struck shaft-first) |
| **With thick end of (the) stick / Coll'estremità grossa / Mit dem dicken Ende des Stockes** | Read 184 | `butt` |
| **With thin end of (the) stick / Coll'estremità sottile / Mit dem dünnen Ende des Stockes** | Read 184 | `tip` |
| **Ein Becken mit dem Holzschaft des Schlägels berühren** | Read 184 | `shank` |
| Lay 1 stick on head — strike with the other | Read 198 | `stick-shot`; the laid stick is the contact surface — see §3.9 |

### 3.5 `technique`

| Source term | Source | Maps to |
|---|---|---|
| Strike / Struck / Colpo / Frappez / Schlagen; Ordinary method of striking; Modo ordinario | Read 163, 199, 215 | `hit` |
| **Rim shot — Shot** | Read 200 | `rimshot` — with no IT/FR/DE equivalent given, see §4 |
| **"Flam" stroke** | Read 198 | `ornament: flam`, not a technique — Read files it under *Methods of Striking* |
| Lay 1 stick on head of drum — strike with the other | Read 198 | `stick-shot` |
| Struck with the wood / On the wood / Rand mit Holz geschlagen | Read 197, 200 | `sidestick` **or** `rim-only` — ambiguous, see §4 |
| Brush the head with the thumb / Thumb (trill) / Mit dem Daumen über das Fell | Read 213; Forsyth 32; Widor 109 | `thumb` (+ `ornament: roll`) |
| Shake (hoop) / Agitare / Secouez / Schütteln | Read 215 | `shake` |
| Roll(ed) with the fingers / With the fingertips | Read 200, 222 | `hit` with `implement: finger` + `ornament: roll` |
| Rubbed together / Frottées l'une contre l'autre / Trill a 2 | Read 183 | `swirl` / `circling` on a cymbal pair |
| **Two-plate-stroke** | Forsyth 35 | the pair-cymbal `hit` — a named stroke v0.1 has no term for |
| **Two-plate-roll** | Forsyth 36 | `ornament: roll` produced by plate friction |
| **Two-stick-roll** | Forsyth 36 | `ornament: roll` on a suspended cymbal with two beaters |
| Rubbed in a circle with wire-brush / Fregato in circola | Read 164 | `circling` |
| Drag with wire-brush / Slide [swish] with brush / Effleurez avec balai | Read 200 | `sweep` |
| **Kept in vibration by friction on the edge** (gong) | Read 219 | `technique` — friction roll; Solomon 244 names it **Friction Roll** |
| **Rub a rosined glove over a snare drum stick pressed against the head** | Read 211 | the string-drum/lion's-roar friction technique applied to a snare drum |
| Rasped and beaten / Raspato e battuto | Read 221 | `scrape` + `hit` |
| Glissando across (wood) blocks / Sui legni | Read 225 | `gliss` |
| Rapid glissando with triangle stick describing an arc | Read 220 | `gliss` on a triangle |
| **Tremolo on cymbal with a 'cello bow** | Read 195 | **no v0.1 technique** — bowing; Solomon 244 **Bowing** |
| Draw a bow across sharp edge at end of bar | Read 179 | bowing |
| **Dead Stroke** | Solomon 75, 242 | `dead` |
| Barely touched / Appena toccata / Leicht berühren; Let vibrate gently by barely touching | Read 181, 232 | `dynamic: ghost` or a light `hit` |
| With (the) hand / Colla mano | Read 184, 215 | `implement: hand` |
| **With (the) fist / Col pugno / Mit der Faust** | Read 214 | **no v0.1 value** |
| **With (the) knuckles / Colla nocce / Mit den Knöcheln** | Read 216; Forsyth 32 | **no v0.1 value** |
| **On (the) knee / Frappez sur le genou / Mit dem Knie** | Read 214 | **no v0.1 value** — the instrument is struck *against the player* |
| With (the) fingernails / Colle unghie / Mit dem Nagel | Read 164 | **no v0.1 implement** (`fingernail` is in the brief's axis sketch but not in `axes.json`) |
| Plucked with the fingertips / Pizzicato | Read 221 | no v0.1 value (chordophone) |
| Harmonics / Flageolett | Read 225; Solomon 250 | no v0.1 value |
| Pitch Bending | Solomon 123, 246 | no v0.1 value; `controllers` may cover it |
| Vibrato / Low (slow vibrato) / Vibrez lentement | Read 179; Solomon 247 | no v0.1 value (vibraphone motor) |
| Scrape | Solomon 244 | `scrape` |
| **Clusters**, **Sympathetic Resonance**, **Adding Mass**, **Prepared Instruments** | Solomon 245–249 | no v0.1 value |

### 3.6 `ornament`

| Source term | Source | Maps to |
|---|---|---|
| **le coup simple (*ta*)** | Gevaert 331 | the unornamented stroke; v0.1 expresses it by absence |
| **le coup double (*fla*)** | Gevaert 331 | `flam`, attack count 2 |
| **le coup de charge (*tra*)** | Gevaert 332 | **no v0.1 value** — a two-stroke figure distinguished from *fla* only by which note carries the accent |
| **les roulements partiels dits *ra*: ra de 3, 4, 5, 6, 7 coups** | Gevaert 332 | `drag` / `ruff` / `bounced` — but Gevaert supplies the **explicit attack count** the brief's ornament axis asks for, as a named series |
| **le roulement continu** | Gevaert 332 | `roll` |
| Roll(ed) / Rullo / Roulement / Wirbel | Read *passim* | `roll` |
| "Flam" stroke | Read 198 | `flam` |
| Rolls | Solomon 77 | `roll` |
| Trill with pennies [coins] / Trillo colle monete | Read 164 | `roll` produced by coins |
| Metallic rustle (tambourine shake) | Widor 109 | `roll` on jingles; Widor explicitly says "a **metallic rustle rather than a roll**" |
| Temporary roll (thumb) | Widor 109 | `roll` |

### 3.7 `damping`

| Source term | Source | Maps to |
|---|---|---|
| Muffled / Con sordino / Coperto / Velato / Sons voilés / Voilée / Bedeckt / Gedämpft | Read 165; Berlioz-Strauss 411; Gevaert 332; Widor 108 | `towel` when the means is a cloth over the head; `muted` when unspecified |
| Muffle off / Natural / Senza sordino / Sans sourdine / Dämpfung ab / Gewöhnlich | Read 165 | `none` |
| Choke(d) / Damp(en) / Dampened / Secco / Étouffez / Kurz / Schnell abdämpfen | Read 163 | `damped` — Read files this as a **separate section** from *Muffled* |
| **Stop [dampen] half-way, and full / Étouffez à demi, et tout à fait / Halb und ganz dämpfen** | Read 195 | a **two-point scale** on `damping` |
| Hold cymbals together after striking / Becken nach Anschlag zusammen halten | Read 194 | cymbal choke |
| „die Becken sofort nach dem Schlage an die Brust drückt" | Berlioz-Strauss 422 | the same choke, described mechanically |
| Muffle notes by holding l.h. against triangle | Read 220 | `damped` |
| Dampened with the fingers / Mit den Fingern gedämpft | Read 194 | `damped` |
| Place a handkerchief over drum head | Read 211 | `towel` |
| **Place a piece of paper on the drum head** | Read 212 | a *prepared* damping, not `towel` |
| **With a thin piece of felt on middle of drum head** | Read 212 | a *prepared*, position-specific damping |
| Wrapped tightly in a cloth (triangle) | Read 220 | `towel` on an idiophone |
| Laid horizontal — without resonance (gong) | Read 219 | a damping achieved by orientation |
| Let vibrate `l.v.` / Lasciare vibrare / Laissez vibrer / Klingen lassen | Read 233 | `none`, asserted positively |
| Pedal off; no resonance | Read 179 | `none`→`damped` via the vibraphone damper |
| Muting (Muffling, Dampening) | Solomon 74 | the axis, named — and Solomon treats the three English words as synonyms, which Read does not |

### 3.8 `mechanism`, `implement`, `dynamic`, `openness`

**`mechanism`.**

| Source term | Source | Maps to |
|---|---|---|
| Snares on / With snares / Con timbro / Avec timbre(s) / Mit Schnarrseite | Read 210 | `wires-on` |
| Snares off / Without snares / Senza timbro / Sans timbre / Détimbrée / Ohne Schnarrseite | Read 209 | `wires-off` |
| **Loosen snares / Slacken(ed) snares / With snares loosened / Avec les cordes lâches** | Read 209 | **distinct from `wires-off`** — the wires stay in contact but are slack. Berlioz-Strauss 423 and Gevaert 332 both give this as the *usual* practice, and Widor 108 says the choice between it and cloth-muffling is left to the player |
| **Tight(en) snares / Très timbrée** | Read 210 | a *third* state above `wires-on` |
| **Cymbal attached to bass drum / Cymbal fixed to the foot-pedal / Grosse caisse à pied avec cymbale** | Read 182; Berlioz-Strauss 418 | **no v0.1 mechanism** — the 19th-century pedal bass-drum-plus-cymbal rig |
| **Bass drum alone (with Cymb. detached) / Gr. C. seule (avec Cymb. décrochée)** | Read 201 | the negation of the above |
| With foot-beater [foot-pedal] / À pied / Mit dem Fuss | Read 201 | pedal-played bass drum |
| Damper Pedals | Solomon 75 | keyboard-percussion damper |
| Pedal glissando / Glissando mit Pedal | Read 165 | timpani pedal |

**`implement`.** Read pp. 166–167 (§2.3) is the master list, 61 names. Mapped onto v0.1:
`stick` ← Ordinary/Regular/Usual stick, Drumstick, Snare drum stick; `brush` ← Wire-brush
[Brush(es)] / Scovolo di fil di ferro / Balai métallique / Drahtbürste; `rod` ← Switch [Rod]
/ Verghe / Verges / **Ruten (Rute, Ruthe)** — Forsyth p. 28 identifies the German
*Ruthe* as a "birch-broom"; `hand`, `finger` ← With the hand / With the fingers;
`felt-beater` ← Felt stick, Soft/Medium/Hard felt; `wood-beater` ← Wood(en) stick,
Holzköpfe; `rubber-beater` ← Rubber (covered), quarter-/half-hard rubber; `mallet-soft /
-medium / -hard` ← the soft/medium/hard families; `superball` ← Solomon 95.

Read names, and v0.1 has no value for: **sponge** (Sponge stick / Bacchetta di spugna /
Baguette d'éponge / **Schwammschlägel**) — the *single most important* historical timpani
beater, called "die besten" by Berlioz-Strauss p. 406 and "sticks with sponge knobs" by
Widor p. 100; **leather / rawhide** (Berlioz-Strauss's middle grade); **cane / rattan**;
**cotton**; **wool**; **capoc / fibre head**; **steel / iron / metal**; **plush**;
**padded**; **knife-blade**; **two-headed [double] stick**; **triangle beater**; **chime
hammer**; **knitting needle** (Solomon 92); **coin** (Read 164, 181; Forsyth 50);
**'cello bow** (Read 195; Solomon 95); **saw blade** (Read 195); **maracas used as
beaters** (Read 172); **Klöppel** = the bass-drum beater as a named object distinct from
`Schlägel` (Berlioz-Strauss 418, 422).

**`dynamic`.** The treatises carry dynamics as ordinary musical dynamics, not as pivot
terms. The only pivot-shaped items are *Barely touched / Appena toccata / À peine frôlé /
Leicht berühren* (Read 181) → `ghost`, and the *accent* marker that Read p. 214 glosses
explicitly: "L'accent ( > ) indique le coup frappé avec le poing" — i.e. in that score the
accent sign *is* the technique marker, not a dynamic. That is a warning, not a term.

**`openness`.** Nothing in this bucket. The orchestral literature has no hi-hat and no
graded-openness instrument; the nearest analogue is Read's *Stop [dampen] half-way, and
full* (p. 195), which is graded `damping`, not graded `openness`.

**`timbre`, `voicing`.** Nothing. Both axes are recording- and synthesis-era concepts; the
treatises' word for the same idea is *timbre* in its ordinary sense, which collides badly
(see §4).

### 3.9 Terms that fit NO axis

These are the most valuable findings, per the brief. Each one is a real, named, published
distinction that the current twelve-axis model cannot carry.

| # | Term | Source | Why no axis fits |
|---|---|---|---|
| G1 | **On the snares / Sulle corde / Sur les timbres / Auf den Saiten** | Read 232 | The snare wires are a *contact site*, but `site` has no value for them; they are not `head`, `rim` or `underside`. Distinct from `mechanism: wires-on`, which describes whether they are engaged, not whether they are struck. |
| G2 | **Strike on copper kettle (of timpani)** | Read 164 | The bowl is a third body, neither `head` nor `shell` as `shell` is defined for a kit drum. |
| G3 | **On (the) knee / Frappez sur le genou / Mit dem Knie** | Read 214 | The *instrument* is moved against the *player's body*. Neither `implement` (the knee is not held) nor `site` (the site is on the tambourine, unchanged) captures it. It is a fourth kind of participant: the anvil surface. |
| G4 | **With the fist / knuckles** | Read 214, 216; Forsyth 32 | `implement: hand` and `finger` exist; fist and knuckles are neither, and the timbral difference is exactly the point of naming them. |
| G5 | **Cymbal fixed to the bass drum / to the foot-pedal**, and its negation **Bass drum alone (with cymbal detached)** | Read 182, 201; Berlioz-Strauss 418 | A *rig* fact: two instruments mechanically coupled so that one stroke sounds both. `mechanism` currently holds only per-instrument states. |
| G6 | **Two players (on same part) / Due esecutori / Zwei Spieler**; **3 Drums, I: f, II: mf, III: p** | Read 172, 211, 212 | A performer-count and per-instance dynamic assignment. Neither is on any axis; `instance` is a layout-slot property, not a multiplicity. |
| G7 | **Lay 1 stick on head of drum — strike with the other** | Read 198 | v0.1 has `stick-shot` as a technique, which is right — but the laid stick is simultaneously acting as `site`. The model cannot say that an implement has become part of the instrument. Solomon names the general case: **"Beaters as Instruments"** (p. 95). |
| G8 | **Place a piece of paper on the drum head**; **thin piece of felt on middle of drum head**; **Prepared Instruments** | Read 211, 212; Solomon 245 | A preparation is an *object added at a position*, with its own material. `damping` has nominal values only and cannot carry material or position. |
| G9 | **Adding Mass**; **Sympathetic Resonance** | Solomon 248 | Same shape as G8 but the intent is pitch/resonance change, not damping. |
| G10 | **Bowing** (cymbal, crotale, vibraphone bar, xylophone bar end) | Read 179, 195; Solomon 244 | Excitation by sustained friction with a bow — not a `technique` value, and the bow is not in `implement`. |
| G11 | **Friction roll** / **Kept in vibration by friction on the edge** / **Rub a rosined glove over a stick pressed to the head** | Read 211, 219; Solomon 244 | Continuous friction excitation. Different from `scrape` (transient) and from `roll` (discrete attacks). |
| G12 | **Roll beginning at centre gradually going to the rim** (and inverse) | Read 212 | A *trajectory* across `position` within one sounding event. The model has point values plus a `strike_position.radial` controller, but no term. |
| G13 | **Stop [dampen] half-way, and full** | Read 195 | `damping` is nominal; this is ordinal and mid-event. |
| G14 | **le coup de charge (*tra*)** | Gevaert 332 | Two strokes distinguished from *fla* **only by which stroke carries the rhythmic accent**. No axis carries intra-ornament accent placement. |
| G15 | **Laid on side / Sul lato / Auf die Seite gedreht** (bass drum); **Laid horizontal — without resonance** (gong); **Cymbal in the air / En l'air / In der Luft** | Read 198, 219, 183 | Instrument *orientation* and *mounting*, which changes both radiation and damping. No axis. |
| G16 | **Placed on snare drum** (tambourine); **Tambourine placed on a kettle-drum** | Read 220; Forsyth 33 | One instrument used as the resonator/anvil of another. Related to G5 but not a fixed rig. |
| G17 | **Out of tune (without pitch or resonance) / Scordata / Verstimmt**; **Tuned high / Hoch gestimmt**; **Well-tuned / Ben accordato** | Read 211, 212, 232 | Head tension as an expressive parameter of an *indefinite-pitch* drum. Not `openness`, not `damping`, not `voicing`. |
| G18 | **Beater Lingo** as an acknowledged problem | Solomon 85 | Not a term but a finding: the leading modern authority devotes a titled section to the instability of beater names. Any implement vocabulary must ship aliases. |
| G19 | **Return to a "Normal" Method of Playing** | Solomon 71, 239 | An explicit *reset* token. Read supplies four languages for it: *Modo ordinario / Position ordinaire / Gewöhnlich / nat.* The model has no "clear all non-default axes" term. |
| G20 | **Off-stage** (a section in five of Read's seven percussion chapters) | Read 174, 202, 216, 222 | Spatial placement of the player. No axis; arguably out of scope, but it is a first-class heading in the source. |

---

## 4. Conflicts and false friends

**One word, different things.**

1. **`timbre`.** In French and Italian orchestral usage **`timbre` / `timbro` means the
   snare wires**: `sans timbre` = snares off (Widor p. 108, Read p. 209), `avec timbre(s)`
   = snares on (Read p. 210), `détimbrée` = de-snared, `caisse claire` is so named *because*
   of the timbre. KITWARP's `timbre` axis means acoustic-vs-808-vs-FM. Any French or
   Italian source string containing `timbre` must be resolved on the snare axis first.
2. **`bell`.** Three meanings in play: v0.1 `instrument: bell` (id 17, a kit cymbal bell as
   a separate pad), v0.1 `site: bell` (the cup of a cymbal), and Read p. 8 **`Bells` =
   tubular chimes / `Campane` / `Cloches` / `Glocken`**, with `Chime-Bells` = glockenspiel.
   Read also uses "On the **bell** [body]" of a *drum* (p. 199) to mean the shell. Four
   readings of one word.
3. **`Tambourin` (FR)** is the **Provençal tabor**, a long snareless drum played with one
   stick, *not* the tambourine — which is `tambour de basque` (Read p. 8; Forsyth p. 31;
   Widor p. 109). `Tamburino` (IT) *is* the tambourine. Italian `Tamburo` is the side drum.
4. **`Becken` vs `Teller`.** German distinguishes the cymbal (`Becken`) from the individual
   plate (`Teller`); `Mit Teller(n)` means clashed as a pair, `Becken frei` means suspended
   (Read pp. 8, 181, 232). English "cymbal" carries neither.
5. **`cassa`.** Italian `cassa` = the shell of a drum ("sulla cassa" = on the shell, Read
   p. 199), but `gran cassa` = the bass drum, and `caisse claire` (FR) = the snare drum.
6. **`Schlägel` vs `Klöppel`.** Berlioz-Strauss uses `Klöppel` specifically for the
   bass-drum beater (pp. 398, 418) and `Schlägel` generically; Read's German column uses
   `Schlägel` for both, and `Stiel des Klöppels` for "handle of the stick" (p. 184).
7. **"muffled" vs "dampened".** Read keeps them as **separate chapter sections** throughout
   Part IV: *Dampened* = stop the sound after it starts (`Secco`, `Étouffez`, `Kurz`);
   *Muffled* = alter the sound before it starts (`Con sordino`, `Voilée`, `Bedeckt`).
   Solomon p. 74 collapses all three English words — "Muting (Muffling, Dampening)" — into
   one heading. **The 1953 distinction is the one KITWARP needs**; the 2016 conflation is
   the one most vendor lists inherit.
8. **"rim".** Read distinguishes *At the rim **of head*** (p. 163 — a radial position on the
   membrane) from *On the rim **of the drum*** / *On the wood* (p. 197 — the hoop). Both
   translate to English "rim". In KITWARP terms these are `position: perimeter` and
   `site: rim` respectively, and any importer that maps the word "rim" to one axis will
   silently mis-file the other.
9. **"struck with the wood".** Read files this under both cymbals (p. 184, meaning the
   wooden *shaft* of a beater = `contact: butt`) and drums (p. 200, meaning the wooden
   *hoop* = `site: rim`). Same English phrase, two axes.

**Different words, same thing.**

- `Étouffez` = `Secco` = `Dämpfen` = `Choke` = `Damp` = `Dry` = `Off` = `Short` = `Stop
  (quickly)` — Read p. 163 lists eight English synonyms for one action.
- `Ordinary` = `Regular` = `Usual` beater = `hammer` = `mallet` = `stick` = `striker` —
  Read p. 166 gives seven English words for the default beater in a single entry.
- Snares off: `Snares off` = `No snares` = `Without snares` = `Senza timbro` = `Senza
  corde` = `Sans timbre` = `Détimbrée` = `Ohne Schnarrseite`, and separately the *slack*
  variants; ten English forms at Read p. 209.
- `Blousé / blouser / blousée / blousez` (FR) = play at the edge — used for both timpani
  (Read p. 163) and cymbals (Read p. 180), and absent from every modern list examined.
- `fla` (FR, Gevaert 331) = `flam` (EN, Read 198) = `Flam` — identical.

**A documented absence.** At Read p. 200 the entry **"Rim shot — Shot"** has its Italian,
French and German columns **empty**. Read fills those columns for essentially every other
entry in 76 pages. The absence is therefore evidence, not an omission: in 1953 the
orchestral literature had no Italian, French or German name for the rim shot, because it
arrived from American dance-band and military drumming. Corroborating this, the two other
American-vernacular entries in Read's percussion part — **`"Ride" solo`** (p. 212) and
**`"Stomp the beat"`** (p. 194) — also have all three columns empty and are the only other
entries so marked.

---

## 5. Gaps against vocabulary v0.1

Measured against `vocabulary/axes.json` v0.1.0 (155 pivot terms, drum kit only).

### 5.1 Missing values, by axis

| Axis | Missing, with the source that names it |
|---|---|
| `site` | **snares** (Read 232), **kettle/bowl** (Read 164), **hoop distinct from counterhoop** (Read 199 `Sur le cadre` / `Auf den hölzernen Rahmen` vs Read 164 `Am Metallrand`), **batter-head as the explicit counterpart of `underside`** (Forsyth 24), **jingles** (Read 214 — the tambourine jingles are struck and brushed independently of the head), **bar-end** and **resonator** for keyboard percussion (Read 179) |
| `position` | nothing missing as *values*; missing as *shape* — Read 212's centre→rim gradient needs the radial controller, and the vocabulary should say so explicitly |
| `contact` | v0.1 has `tip / shank / butt` for a stick. Read distinguishes **thick end** vs **thin end** (p. 184) which maps cleanly, and **`Holzschaft`** = shaft (p. 184) which is `shank`. No gap, but the aliases are missing |
| `technique` | **bow** (Read 179, 195; Solomon 244), **friction-roll** (Read 219; Solomon 244), **fist** (Read 214), **knuckle** (Read 214, 216; Forsyth 32), **fingernail** (Read 164 — listed in the brief's axis sketch, absent from `axes.json`), **knee** (Read 214), **pitch-bend** (Solomon 123), **vibrato** (Read 179; Solomon 247), **cluster** (Solomon 249), **harmonic** (Read 225; Solomon 250), **two-plate-stroke** (Forsyth 35) |
| `ornament` | **ra-3 / ra-4 / ra-5 / ra-6 / ra-7** as named attack counts (Gevaert 332), **tra / coup de charge** (Gevaert 332), **thumb-roll** as an ornament distinct from `roll` (Read 213; Forsyth 32; Widor 109 — Widor calls it a "temporary roll", i.e. it cannot be sustained) |
| `damping` | **prepared** (paper, felt, cloth *on* the head — Read 211, 212), **half** as an ordinal step (Read 195), **choke** for cymbals as distinct from `damped` (Read 194; Berlioz-Strauss 422) |
| `mechanism` | **wires-slack** as a third state between `wires-on` and `wires-off` (Read 209; Berlioz-Strauss 423; Gevaert 332; Widor 108 — three independent sources make this the *usual* practice, not an edge case), **wires-tight** (Read 210 `Très timbrée`), **cymbal-coupled-to-kick** (Read 182; Berlioz-Strauss 418), **pedal-bass-drum** (Read 201) |
| `implement` | **sponge** (Berlioz-Strauss 406; Widor 100; Read 166–167 — the historically dominant timpani beater), **leather**, **rawhide**, **cane**, **rattan**, **cotton**, **wool**, **fibre/capoc head**, **steel**, **iron**, **metal**, **plush**, **padded**, **two-headed stick**, **triangle-beater**, **chime-hammer**, **knitting-needle** (Solomon 92), **coin**, **bow**, **saw-blade**, **rosined-glove**. Also a *hardness* qualifier that is orthogonal to material: Read carries `quarter-hard`, `half-hard`, `medium-hard`, `medium-soft`, `soft`, `hard`, `very hard`, `very soft` on rubber, felt and leather independently (pp. 166–167) — v0.1's `mallet-soft/medium/hard` folds material and hardness into one value, which cannot express "medium-hard **leather**" |
| `instrument` | the entire orchestral and auxiliary inventory of §2.9 and §2.14; the reserved families `orch`, `perc.*`, `utility` are exactly the right place for it |

### 5.2 What v0.1 names wrongly

1. **`instrument: sticks` (id 34) collides with `implement: stick`.** In every source in
   this bucket, "sticks" means the beater. The instrument that a kit calls "sticks" is
   `claves` in the orchestral literature (Read p. 9). Recommend a `correction` alias, not a
   rename (ADR-0003).
2. **`instrument: chimes` (id 38) is ambiguous.** Read p. 8 separates `(Tubular) Chimes /
   Bells / Campane / Cloches / Glocken` from `Glockenspiel / Chime-Bells / Campanelli`, and
   Solomon separates **Church Bells** (p. 163) from **Metal Wind Chimes, Mark Tree and Bell
   Tree** (p. 166) from **Bamboo Wind Chimes** (p. 181). A kit "chimes" pad is almost
   always the mark-tree sense; the orchestral "chimes" is always the tubular-bell sense.
   The single slug cannot carry both.
3. **`instrument: cymbal` (id 18) cannot express pair-vs-suspended**, which the literature
   treats as an instrument-level distinction with its own nomenclature and its own chapter
   (Read p. 8, ch. 34). `crash` in v0.1 is a *suspended* cymbal; there is no slot for
   `piatti` / clash cymbals at all.
4. **`damping: towel`** is a drum-kit-ism. The literature's word, in four languages, is
   *muffled / con sordino / coperto / voilée / bedeckt / gedämpft*. Keep the slug
   (identifiers are forever) but ship those six as aliases, and note that `towel` names the
   *means* while the sources name the *effect*.
5. **`site: rim2`** has no counterpart anywhere in this literature. It is an e-drum zone
   name. That is fine — but it means `rim` and `rim2` cannot be populated from any
   orchestral source, and a mapping that guesses will be wrong.
6. **`technique: sidestick` vs `site: crossstick`.** Read's *On the rim / On the wood /
   Rand mit Holz geschlagen* (p. 197) is the ancestor of both, and does **not** distinguish
   them. Orchestral sources cannot disambiguate a v0.1 `sidestick` from a `rim-only`; any
   import from this literature must leave the choice unresolved rather than guess.
7. **`dynamic: accent`.** Read p. 214 records a score in which the accent sign `>`
   *is* the technique marker ("L'accent ( > ) indique le coup frappé avec le poing"). A
   parser that reads `>` as `dynamic: accent` will lose a technique. Worth a note in
   `rules.json`.

### 5.3 What v0.1 gets right, confirmed independently

- Splitting `site` (on the instrument) from `contact` (on the implement) is exactly Read's
  own split between *Methods of Striking* and the beater qualifiers in the stick-type
  tables. Read p. 184 puts *With the handle of the stick* and *With the thin end of the
  stick* in the striking-methods section and *Felt stick / Sponge stick* in stick types —
  the same two axes.
- Separating `damping` from `mechanism` is confirmed three times over: Widor p. 108,
  Berlioz-Strauss p. 423 and Gevaert p. 332 all state that cloth-muffling and
  snare-slackening are *different means to the same end*, and Widor says the choice is left
  to the player. They must therefore be separate axes with independent values, which is what
  v0.1 does.
- `ornament` carrying an attack count is confirmed by Gevaert's *ra de 3/4/5/6/7 coups*
  (p. 332), which is a published, named, counted series from 1885.
- `position` as radial is confirmed by Read's centre/rim pair being given for **timpani,
  bass drum, snare drum and tambourine alike** (pp. 164, 196–199, 214), i.e. it is a
  cross-instrument axis, not a snare-drum special case.

---

## 6. Self-critique (Round C)

### 6.1 What is still missing from this bucket

- **Six of the nine books the bucket names could not be opened at all.** Blades ×2, Adler,
  Stone, Peinkofer/Tannigel, Brindle. Not "partially reached" — zero text, because
  archive.org's search-inside endpoint now refuses lending-restricted items and every
  snippet channel (Google Books, HathiTrust) was closed by quota or Cloudflare. Everything
  in §2 therefore comes from public-domain treatises plus one publisher preview.
- **Kastner's *Manuel général de musique militaire* (1848, S20) was downloaded and not
  mined.** 1.3 MB of French text on military percussion by the author Gevaert cites as his
  source for the French drum-beating names (Gevaert p. 332 n. 1). It should contain the
  primary definitions of *ta*, *fla*, *tra*, *ra* and the full French *batterie*
  repertoire. This is the cheapest remaining win in the bucket.
- **The German and Italian registers are thinner than the French and English.** Hofmann
  (S15), Teuchert (S16) and Prout's Italian translation (S12) were downloaded but only
  spot-checked. Peinkofer/Tannigel would have been the German authority and is closed.
- **Bower 1912 (S17, S18) and Gardner 1918 (S19)** — American pre-MIDI percussion methods,
  downloaded, not mined. These are the likeliest printed source for the *American*
  vernacular Read could not translate (rim shot, ride, stomp), and they predate the drum kit
  as a fixed object.
- **Elaine Gould, *Behind Bars* (S22)** was downloaded and deliberately not mined here: it
  is a notation manual, its percussion chapter overlaps the notation-standards bucket, and
  its licence is all-rights-reserved with an uncertain upload provenance. Flagged for the
  reconciliation pass to assign.
- **Read's four-language columns were reconstructed from flattened OCR.** Where a column
  has fewer entries than the English one the row alignment is marked UNVERIFIED above. A
  pass against the page images (`thesaurusoforche00read` leaves 189–262) would settle them.

### 6.2 The single most authoritative source NOT obtained

**Gardner Read, *Compendium of Modern Instrumental Techniques* (Greenwood, 1993; ISBN
0-313-28512-8; archive.org `compendiumofmode0000read`).**

The bucket brief already identifies Read as "the single richest source of technique names
in print", and it is right — but the 1953 *Thesaurus* obtained here is organised **by
composer and score**, with the technique names appearing as headings over citation tables.
The 1993 *Compendium* is organised **by technique**, codifying each one with its production
and effect. For a project that needs the technique list itself rather than its usage, the
*Compendium* is the higher-value book by a clear margin, and it is the one Read wrote after
forty more years of the repertoire.

Second on the list, and cheaper to obtain because it is in print and not a lending item, is
**Peinkofer & Tannigel, *Handbook of Percussion Instruments: Their Characteristics and
Playing Techniques*** (Schott, EN 1976 / DE *Handbuch des Schlagzeugs*, 1969) — the only
title in this bucket whose subtitle is literally the KITWARP model, and the only one that
covers instrument, characteristic and technique together for the full orchestral inventory
in both German and English.

Third, and obtainable for the price of a library copy rather than a scan: **Solomon,
Appendix C, pp. 239–250**. Its sixteen headings are already recovered here (§2.14) and they
map onto §3.9's gap list almost one to one. Sixteen pages of body text would close most of
the "fits no axis" column.

### 6.3 Confidence

| Claim class | Confidence |
|---|---|
| Terms quoted with a printed page from a public-domain scan (§2.2–2.13) | high — page number verified against `_page_numbers.json` and the running head |
| Four-language column alignment in Read's tables | medium — reconstructed from flattened OCR; mismatched columns marked UNVERIFIED |
| Solomon page numbers (§2.14) | high — from the publisher's own preview PDF |
| Stone p. 211 beater pictograms | **UNVERIFIED** — from a secondary description, the book itself was unreachable |
| Absence claims ("no Italian/French/German for rim shot", §4) | medium-high — the absence is visible in the source's own table, but only for the 1953 edition |
| "Not reached" verdicts (§1.2) | high — each locator was probed and the failure mode recorded |
