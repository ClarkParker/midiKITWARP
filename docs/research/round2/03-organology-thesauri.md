# Dossier 03 — Organology and controlled instrument vocabularies

Round 2, bucket 03. Written against `.agents/round2/BRIEF.md` and
`.agents/round2/03-organology-thesauri.md`.

**Scope line.** This dossier records what the organological literature and the maintained
instrument authority files call percussion instruments, striking sites and playing
techniques, so that ADR-0001 and ADR-0003 can be settled on evidence rather than on the
assumption that KITWARP must mint every name itself.

**All retrievals dated 2026-09-06** unless stated otherwise. Everything below carries a
locator. Anything not personally verified is marked UNVERIFIED.

---

## 0. The question this bucket was set

> Is there an existing maintained authority file with stable identifiers that KITWARP
> should cross-reference for instrument names, instead of inventing its own — the way
> SMuFL glyph names are already proposed as a cross-reference in
> `docs/research/07-percussion-naming.md` §2.1?

### 0.1 The short answer

**Yes for the instrument axis, and only for its coarse half. No for every other axis.**

There are six maintained authority files with stable, dereferenceable identifiers for
musical instruments. All six were reached and queried live. Measured against KITWARP's
27 `instrument` values:

| Authority | Concepts (whole file) | KITWARP `instrument` values matched | Values with no concept at all | Licence |
|---|---:|---:|---:|---|
| MIMO Thesaurus of musical instrument names | 2 724 | 13 / 27 | 14 | **none stated** |
| Library of Congress LCMPT | 942 | 13 / 27 | 14 | public domain |
| Getty AAT (musical instruments branch) | 348 under `aat:300041620`, plus 177 under `aat:300041646` | 11 / 27 | 16 | ODC-By 1.0 |
| Wikidata (percussion subtree) | 877 | 17 / 27 | 10 | CC0 |
| MusicBrainz instruments (percussion) | 288 | 12 / 27 | 15 | CC0 |
| GND, subject category 14.3 *Musikinstrumentenkunde* | 908 | ~12 / 27 (UNVERIFIED, sampled not enumerated) | — | CC0 |

Nothing that any of them offers reaches KITWARP's working granularity. **Not one of the
six has a concept for `ride`, `china`, `splash`, `stack`, `xhat`, `mini-china`,
`mini-hihat`, `crash-ride`, `jam-block` or `aux-pad`.** Getty AAT, LCMPT and MusicBrainz
have no `hi-hat` concept at all; MIMO has one but its English label is *Choke cymbal* and
its German label is *Hi-hat* (§4.1); GND has one, `Hi-Hat-Maschine` (§2.11), which is the
only authority-file *definition* of the instrument found anywhere in this bucket. Wikidata
is the only file with `ride cymbal`, and its `ride cymbal` item carries no MIMO id, no AAT
id and no MusicBrainz id — that is, the item exists but no authority file has adopted it.

**For everything that is not the instrument axis there is next to nothing.** The whole
harvest from all six files, across KITWARP's other eleven axes, is five concepts: Getty
AAT's `drumheads`, `shells (drum components)` and `snares (drum components)`, its five
`percussion beaters`, and LCMPT's `drum machine`. Getty AAT has no concept for rim shot,
side stick, flam, drag, buzz, choke, or open/closed hi-hat (query, §2.5), and no concept
for a drum rim or a cymbal bow, bell or edge (§2.10). LCMPT has none either, and by design — it is a *medium of
performance* thesaurus, not a technique thesaurus. Hornbostel-Sachs, in the authors' own
words, deliberately excludes playing technique for membranophones (§2.2). The one
linked-data vocabulary that promises "instrument playing techniques", DOREMUS
`vocabulary/technique/`, turns out to hold 20 concepts, all of them vocal — *blow,
breathing, cantillation, coloratura, cry, incantation, rapping, scat, throat singing,
ululation, ventriloquy, whistling* and eight more (§2.6). There is nothing for percussion.

### 0.2 What a cross-reference would cost

Cost is modest and one-directional. The recommended shape is a **non-authoritative,
optional, outbound `xref` block on a pivot term**, never a component of the pivot id and
never a source of truth:

```
"snare.hit": { "id": …, "xref": { "mimo": 2729, "lcmpt": "mp2013015657",
                                  "aat": 300041755, "wikidata": "Q208421",
                                  "mb": "947cca7d-74c6-4044-b6cc-71a1180d0b28" } }
```

- **Data cost.** About 40 of the 155 v0.1 terms are instrument-identity roots that could
  carry an xref at all; the rest are facet refinements below the level any authority
  describes. Roughly 13 of those 40 would get a full row today. Call it one afternoon of
  work plus a validator rule.
- **Maintenance cost.** Low but not zero. All five ids are stable by policy, but MIMO
  contains at least one duplicate pair (concepts 5702 and 5703, both `Drum set`,
  5703 nested under 5702, identical prefLabels in all 13 languages — §4.4) and Wikidata
  contains several same-label items (five distinct items labelled `triangle`@en, three
  labelled `cymbal`@en — §4.5). Choosing between duplicates is a human judgement that a
  validator cannot make, and a wrong choice is invisible.
- **Licence cost.** Mixed, and this is the sharp edge. Getty AAT is ODC-By 1.0 with a
  mandatory attribution string. LC data at `id.loc.gov` is declared a public domain data
  set. MusicBrainz core data is CC0. Wikidata is CC0. GND is CC0, stated per record. **MIMO publishes no licence
  statement anywhere reachable** — not in the Skosmos vocabulary metadata, not on the
  concept-scheme resource, not on the vocabulary landing page. Under ADR-0004 that is
  `unknown` and therefore all rights reserved. See the open question in §6.4: storing the
  bare integer `2729` and copying MIMO's label string `Side drum` are different acts, and
  only the second is plausibly a reproduction.
- **Complexity cost.** One new optional object in `pivot.json`, one schema addition, one
  validator rule (id must match a syntax pattern per namespace; no xref may be treated as
  identity). No effect on the compiled table if the exporter drops `xref`.

### 0.3 What a cross-reference would buy

- **Multilingual display names, free and checked.** MIMO carries a preferred label in
  **13 languages** for all 2 724 concepts — Basque, Catalan, Chinese, Danish, Dutch,
  English, French, German, Italian, Korean, Polish, Spanish, Swedish. LCMPT carries a
  dense variant-label ring in English (`snare drum` UF `side drum`, `caixa`;
  `drum set` UF `traps`, `trap set`, `drum kit`, `trap kit`, `drumset`). A parser that has
  to recognise `Caixa` in a Brazilian sample library, or `Schlagzeug` in a German device
  manual, gets those synonyms for free instead of guessing.
- **An external anchor for the identifier policy.** ADR-0003 asserts that ids are forever.
  MIMO is a live demonstration that the policy works: the `http://www.mimo-db.eu/…` URI
  namespace was minted in 2010 for an EU project that ended in 2011, the project's own
  domain no longer serves HTTPS, and yet
  `http://www.mimo-db.eu/InstrumentsKeywords/2467` still resolves — HTTP 200, redirected
  to `vocabulary.mimo-international.com` — sixteen years later. That is the behaviour
  KITWARP is promising, evidenced in a comparable project.
- **A defensible provenance answer for the long tail.** When percussion, orchestral and
  world families are eventually minted, "this term is MIMO 2746 / LCMPT mp2013015705" is a
  better provenance record than "we made this name up", and it is free to record.
- **A cheap disambiguation test.** Two device layouts that both say `Timbale` can be
  checked against LCMPT `timbales criollos` vs MIMO's `Timbales`, instead of against a
  maintainer's memory.

### 0.4 Recommendation

1. **Do not adopt any authority file as the instrument namespace.** None of them reaches
   the granularity KITWARP needs; adopting one would force the vocabulary to invent
   children under borrowed parents, which is worse than owning the whole namespace.
2. **Do add an optional outbound `xref` block** with namespaces `mimo`, `lcmpt`, `aat`,
   `wikidata`, `mb`, `gnd`. Populate it only where the match is exact and a human has checked it;
   leave it absent otherwise. A documented gap beats a guessed cross-reference, exactly as
   for note numbers.
3. **Do not copy any authority's label text into `pivot.json`.** Ids only. This keeps the
   MIMO licence gap out of the repository entirely, and it is also the honest position:
   KITWARP's display names describe drum-kit articulations, and MIMO's describe museum
   objects.
4. **Do record Hornbostel-Sachs notations where they are unambiguous** (`snare` 211.212.11,
   `kick` 211.212.12, drum kit 211.212.21, cymbal family 111.142) as a **reference axis**,
   not a pivot facet. They are a useful sanity check on family assignment and nothing more
   — see §4.2 for why they cannot carry more weight than that.

---

## 1. Candidate source register (round A)

Thirty-six candidates. "Authority level" is: **A** primary standard or maintained
authority file; **B** peer-reviewed scholarship or a national library product; **C**
secondary aggregation or index.

### 1.1 Classification schemes and primary organological texts

| # | Title | Author / body | Year | Type | Locator | Auth. | Reached |
|---|---|---|---|---|---|---|---|
| 1 | *Systematik der Musikinstrumente. Ein Versuch* | E. M. von Hornbostel, C. Sachs | 1914 | journal article | *Zeitschrift für Ethnologie* 46, Heft 4–5, pp. 553–590. Introductory essay reprinted as Univ. Würzburg, Institut für Musikforschung, *Materialhefte* n° 1, `https://www.musikwissenschaft.uni-wuerzburg.de/fileadmin/04070000/Instrumentensammlung/Materialien_Instrumente/Hornbostel_SysTex.pdf` (14 pp, HTTP 200) | A | **yes**, essay only, not the numbered table |
| 2 | "Classification of Musical Instruments" (English translation of #1) | A. Baines, K. P. Wachsmann (trans.) | 1961 | journal article | *Galpin Society Journal* 14, pp. 3–29. JSTOR. Cited by #3 p. 4 and #5 p. 1 | A | **no** — paywalled |
| 3 | *Revision of the Hornbostel-Sachs Classification of Musical Instruments by the MIMO Consortium* | MIMO working group for classification and thesauri, chaired by M. Birley (Horniman Museum), with A. Myers (Edinburgh), S. Willaert (MIM Brussels) | 8 July 2011 | standard document | 26 pp PDF, `https://archive.org/details/revisionofthehornbostelsachsclassificationofmusicalinstrumentsbythemimoconsortium`; also `http://www.mimo-international.com/documents/hornbostel%20sachs.pdf` (HTTP 200 over http) | A | **yes** |
| 4 | *Addenda & Corrigenda* to #3 | CIMCIM Working Group for Classification, chair M. Birley (Horniman) | **October 2017** | erratum | `https://archive.org/download/revisionofthehornbostelsachsclassificationofmusicalinstrumentsbythemimoconsortium/…%20-%20Addenda%20%26%20Corrigienda_djvu.txt` (follow the 302) | A | **yes** |
| 5 | *The Knight Revision of Hornbostel-Sachs: a new look at musical instrument classification* | R. C. Knight, Oberlin College | © 2015, rev. 2017 | classification scheme | 44 pp PDF, `https://www2.oberlin.edu/faculty/rknight/Organology/KnightRev2015.pdf` | B | **yes** |
| 6 | "A New Look at Classification and Terminology for Musical Instruments" | R. C. Knight | 2016 | journal article | *Galpin Society Journal* 69 | B | **no** — paywalled |
| 7 | Revision of H-S classes 1–4 | J. Montagu | n.d. | classification scheme | published in *Muzyka*; #3 p. 1 states its revision is "closely based" on it | B | **no** |
| 8 | *Catalogue descriptif et analytique du Musée instrumental … de Bruxelles* | V.-C. Mahillon | 1880, 2nd ed. 1893 | museum catalogue | cited #5 pp. 1, 4; origin of *aerophone / chordophone / membranophone / autophone* | B | **no** |
| 9 | *Old English Instruments of Music* (contains "Galpin 1", 1900 scheme) | F. W. Galpin | 1910, 4th ed. 1965 | book | cited #5 p. 4 | B | **no** |
| 10 | *A Textbook of European Musical Instruments* ("Galpin 2") | F. W. Galpin | 1937 | book | pp. 25–36, cited #5 p. 4 | B | **no** |
| 11 | "D'une nouvelle classification méthodique des instruments de musique" | A. Schaeffner | 1932 | journal article | *La Revue Musicale* 13/129, pp. 215–31 | B | **no** |
| 12 | "Adaptation française de la classification des professeurs E. M. von Hornbostel et C. Sachs" | A. Schaeffner | 1935 | encyclopaedia entry | *Encyclopédie Française* 16, pp. 15–16. The French-language H-S terminology | B | **no** |
| 13 | *Origine des instruments de musique* | A. Schaeffner | 1936 | book | cited #5 p. 4 | B | **no** |
| 14 | *The Ethnomusicologist* (Hood organogram) | M. Hood | 1971 | book | cited #5 p. 2 | B | **no** |
| 15 | *On Concepts and Classifications of Musical Instruments* | M. J. Kartomi | 1990 | book | Univ. of Chicago Press, ISBN 9780226425498; Internet Archive item `onconceptsclassi0000kart` (lending, not open) | B | **no** — borrow-only |
| 16 | "Classification", *Grove Dictionary of Musical Instruments*, 2nd ed. | K. Wachsmann, expanded by M. Kartomi and J. Montagu | 2014 | reference article | vol. 1, pp. 568–79, per #5 p. 3 | A | **no** — paywalled |
| 17 | "Drum kit", *Grove Music Online* | — | — | reference article | `https://www.oxfordmusiconline.com/grovemusic/display/10.1093/gmo/9781561592630.001.0001/omo-9781561592630-e-0000042868` returns **HTTP 403** | A | **no** |
| 18 | *Typologie et classification en organologie musicale* | C. Marcel-Dubois, ICOM CIMCIM | 1985 (Bern) | committee paper | `https://icom.museum/en/ressource/typologie-et-classification-en-organologie-musicale/` | B | **no** — record only |

### 1.2 Maintained controlled vocabularies with query APIs

| # | Vocabulary | Body | Concepts | Locator / API | Auth. | Reached |
|---|---|---|---:|---|---|---|
| 19 | Thesaurus of musical instrument names (`InstrumentsKeywords`) | MIMO / Musical Instrument Museums Online | **2 724** | Skosmos REST, `https://vocabulary.mimo-international.com/rest/v1/InstrumentsKeywords/…`; URIs `http://www.mimo-db.eu/InstrumentsKeywords/{n}` | A | **yes** |
| 20 | Hornbostel-Sachs classification, SKOS (`HornbostelAndSachs`) | MIMO | **643** | same host, `/rest/v1/HornbostelAndSachs/…` | A | **yes** |
| 21 | Art & Architecture Thesaurus | Getty Research Institute | 348 under `aat:300041620`; 177 under `aat:300041646` | SPARQL `https://vocab.getty.edu/sparql.json?query=…` | A | **yes** |
| 22 | Medium of Performance Thesaurus for Music (LCMPT) | Library of Congress | **942** | bulk N-Triples `https://id.loc.gov/download/authorities/performanceMediums.skosrdf.nt.gz`, file stamped **2026-09-02** | A | **yes** |
| 23 | LC Genre/Form Terms (LCGFT) | Library of Congress | — | `https://id.loc.gov/download/authorities/genreForms.skosrdf.nt.gz` | A | **no** — identified, not extracted; genre not instrument |
| 24 | LC Subject Headings (LCSH) | Library of Congress | — | `https://id.loc.gov/authorities/subjects.html` | A | **no** — superseded for this purpose by LCMPT |
| 25 | Wikidata | Wikimedia | 877 items under *percussion instrument* (Q133163) | SPARQL `https://query.wikidata.org/sparql` | B | **yes** |
| 26 | MusicBrainz instrument entity | MetaBrainz | 288 of type *Percussion instrument* | WS2 `https://musicbrainz.org/ws/2/instrument?query=…&fmt=json` | B | **yes** |
| 27 | Digital Hornbostel & Sachs Classification of Musical Instruments | ACDH-CH / OeAW, on DARIAH Skosmos | — | `https://vocabs.dariah.eu/rest/v1/hsinstruments_thesaurus/…`. **curl gets HTTP 502 from the egress proxy**; WebFetch on the same URLs succeeds | A | **partly** — via WebFetch only |
| 28 | Hornbostel-Sachs-Klassifikation (German museum vocabulary) | museumsvokabular.de / KOBV | — | `https://museumsvokabular.de/hornbostel-sachs/`, mirror `https://museumsvokabular.kobv.de/hornbostel-sachs/` | A | **no** |
| 29 | term.museum-digital.de instrument tags | museum-digital | — | `https://smb.museum-digital.de/tag/38141` (Hornbostel-Sachs-Systematik) | B | **no** |
| 30 | DOREMUS controlled vocabularies (33 vocabularies, 23 categories) | DOREMUS ANR project; described as IFLA de-facto standard | `technique` 20 concepts; `mop-mimo` 2 572 MIMO concepts | `git clone --depth 1 https://github.com/DOREMUS-ANR/knowledge-base.git`, HEAD 2024-03-29; portal `https://data.doremus.org/vocabularies/` | B | **yes** |
| 31 | Gemeinsame Normdatei (GND) | Deutsche Nationalbibliothek, via lobid (hbz) | **908** subject headings in category 14.3 *Musikinstrumentenkunde*; 8 M+ records overall | `https://lobid.org/gnd/search?q=…&format=json`, `https://lobid.org/gnd/{id}.json`. Licence CC0 1.0, stated per record | A | **yes** |
| 32 | Iconclass | Henri van de Waal foundation, on DARIAH Skosmos | — | `https://vocabs.dariah.eu/iconclass/` | A | **no** — iconography, not organology |
| 33 | CIMCIM resources (classification, brasswind terminology thesaurus) | ICOM CIMCIM | — | `https://cimcim.mini.icom.museum/resources/` | A | **no** |
| 34 | Collections du Musée de la musique / POP-Joconde | Philharmonie de Paris | 8 000+ objects | `https://collectionsdumusee.philharmoniedeparis.fr/` | B | **no** |
| 35 | "Controlled Vocabularies for Music Metadata" | P. Lisena, K. Todorov | 2018 | conference paper | ISMIR 2018, `https://ismir2018.ircam.fr/doc/pdfs/68_Paper.pdf`; Zenodo 1492441 | B | **no** — record only |
| 36 | *List of idiophones / membranophones by Hornbostel–Sachs number* | Wikipedia | — | `https://en.wikipedia.org/wiki/List_of_idiophones_by_Hornbostel%E2%80%93Sachs_number` | C | **no** — index only |

### 1.3 Hosts that answered an error, recorded as required

| Host | Symptom | Consequence |
|---|---|---|
| `lclsds.loc.gov` | `CONNECT tunnel failed, response 502` — egress policy | LC bulk downloads reached instead via `id.loc.gov/download/…`, which works |
| `vocabs.dariah.eu` | `502` to curl, `connection reset` | reached via WebFetch on constructed REST URLs |
| `www.oxfordmusiconline.com` | HTTP 403 | Grove not reached — see §6.2 |
| `https://www.mimo-international.com/` | TLS handshake failure | the same host over plain `http` serves the 2011 PDF (HTTP 200) |
| `web.archive.org` | unreachable in this environment (supervisor-verified) | Wayback not used anywhere in this dossier |

---

## 2. Extracted terminology (round B)

### 2.1 Hornbostel-Sachs, digit by digit — idiophones (1) and membranophones (2)

Source for every row: the MIMO 2011 revision (register #3), cross-checked against the live
SKOS at `https://vocabulary.mimo-international.com/rest/v1/HornbostelAndSachs/children?uri=…`.
Definitions are **verbatim** from the PDF where quoted. The tree as walked has 109 concepts
under Idiophones and 144 under Membranophones, of 643 in the whole scheme.

#### 2.1.1 Class 1, Idiophones — the top of the tree

| Notation | Term | Verbatim definition (MIMO 2011, register #3 p. 4) |
|---|---|---|
| 1 | Idiophones | "The substance of the instrument itself, owing to its solidity and elasticity, vibrates and may radiate sound without requiring stretched membranes or strings" |
| 11 | Struck idiophones | "The instrument is made to vibrate by being struck upon" |
| 111 | Idiophones struck directly | "The player himself executes the movement of striking; whether by mechanical intermediate devices, beaters, keyboards, or by pulling ropes, etc., is immaterial; it is definitive that the player can apply clearly defined individual strokes and that the instrument itself is equipped for this kind of percussion" |
| 111.1 | Concussion idiophones or clappers | "Two or more complementary sonorous parts are struck against each other" |
| 111.11 | Concussion sticks or stick clappers | — |
| 111.12 | Concussion plaques or plaque clappers | — |
| 111.13 | Concussion troughs or trough clappers | — |
| 111.14 | Concussion vessels or vessel clappers | "Even a slight hollow in the surface of a board counts as a vessel" |
| 111.141 | Castanets | "Vessel clappers, either natural, or artificially hollowed out" |
| **111.142** | **Cymbals** | **"Vessel clappers with everted rim"** |
| 111.143 | Concussion bells | "Nigeria" |
| 111.2 | Percussion idiophones | "The instrument is struck either with a non-sonorous object (hand, stick, striker) or against a non-sonorous object (human body, the ground)" |
| 111.21 / .211 / .212 | Percussion sticks / individual / sets | ".211 … also the triangle"; ".212 … All xylophones" |
| 111.22 / .221 / .222 | Percussion plaques / individual / sets | ".222 Lithophone (China), and most metallophones" |
| 111.23 / .231 / .232 | Percussion tubes / individual / sets | ".231 Tubular bell. NB Not slit drums, which are a sub-group of bells, 111.243" |
| 111.24 | Percussion vessels | — |
| 111.241 | Gongs | "The vibration is strongest near the vertex" |
| 111.241.11 | Bossed gongs, flat gongs (with flange) and intermediate types | — |
| 111.241.12 | Gongs with divided surface sounding different pitches | "Steel drum (Caribbean)" |
| 111.242 | Bells | "The vibration is weakest near the vertex" |
| 111.242.11 | Resting bells | "The cup is placed on the palm of the hand or on a …" |
| 111.242.12 | Suspended bells | — |
| 111.242.121 / .122 / .123 | struck from the outside / clapper bells / bells with attached external clapper(s) | — |
| 111.243 | Slit drums | — |
| 111.244 | Percussion troughs | — |
| 111.25 | Percussion boulders | — |
| 112 | Indirectly struck idiophones | — |
| 112.1 | Shaken idiophones or rattles | — |
| 112.11 / .111 / .112 | Suspension rattles / strung / stick | — |
| 112.12 / .121 / .122 | Frame rattles / pendant / sliding | — |
| 112.13 | Vessel rattles | — |
| 112.2 | Scraped idiophones | — |
| 112.21 / .211 / .212 | Scraped sticks / without resonator / with resonator | — |
| 112.22 / .23 / .24 / .25 | Scraped tubes / vessels / wheels or cog rattles / boards | — |
| 112.3 | Split idiophones | — |
| 12 | Lamellaphones (plucked idiophones) | — |
| 13 | Friction idiophones | "The instrument is made to vibrate by friction" |
| 131.1 | (Individual) friction sticks | "Sandpaper blocks" |
| 133.2 | Sets of friction vessels | "Verillon (glass armonica)" |
| 134 | Friction sheet | "Theatrical wind machine" |
| 14 | Blown idiophones | — |
| 15 | Metal sheets | — (MIMO/Montagu addition; sub-divided 151 friction, 152 directly struck, 153 played by shaking, 154 shaken and indirectly struck — "Flexatone") |
| 16 | Flexed diaphragms | "A diaphragm is flexed when a string passing through its centre is pulled, before returning to rest" |

Suffixes for any division of idiophones (register #3 p. 7):
`-1` transducer-coupled, `-11` non-integral microphones, `-12` non-integral pickups,
`-8` with keyboard, `-9` mechanically driven.

#### 2.1.2 Class 2, Membranophones — the part that carries the drum kit

| Notation | Term | Verbatim definition or example (register #3 pp. 7–9) |
|---|---|---|
| 2 | Membranophones | "The sound is excited by tightly stretched membranes" |
| 21 | Struck drums | "The membranes are struck" |
| 211 | Drums struck directly | "The player himself executes the movement of striking; this includes striking by any intermediate devices, such as beaters, keyboards, etc; drums that are shaken are excluded" |
| 211.1 | Vessel drums | "The single playing head encloses a body in the form of a vessel that is curvilinear or rectilinear in profile — Kettledrums" |
| 211.11 | Separate vessel drums | "European timpani" |
| 211.2 | Tubular drums | — |
| 211.21 | Cylindrical drums | "The diameter is essentially the same at the middle and the ends" |
| 211.211 | Single-skin cylindrical drums | — |
| 211.212 | Double-skin cylindrical drums | — |
| **211.212.11** | **Individual double-skin cylindrical drums, one skin used for playing** | **"Side drum, tenor drum, tambourin de Provence"** |
| **211.212.12** | **Individual double-skin cylindrical drums, both heads played** | **"Turkey (davul). Almost world-wide (bass drum in marching band)."** |
| **211.212.21** | **Sets of double-skin cylindrical drums with single playing heads** | **"USA/Europe drum kit"** |
| 211.212.22 | Sets of double-skin cylindrical drums, both heads played | — |
| 211.22 | Barrel-shaped drums | "The diameter is larger at the middle than at the ends; the body is curvilinear" |
| 211.23 | Double-conical drums | — |
| 211.24 | Hourglass-shaped drums | — |
| 211.25 | Conical drums | — |
| 211.26 | Goblet-shaped drums | — |
| 211.27 | Cylindro-conical drums | — |
| 211.28 | Vase-shaped drums | — |
| 211.3 | Frame drums | — |
| 211.31 / .311 / .312 | without handle / single-skin / double-skin | ".311 Tambourine" |
| 211.32 / .321 / .322 | with handle / single-skin / double-skin | — |
| 212 | Rattle drums | subdivided .1 vessel, .2 tubular, .3 frame |
| 23 | Friction drums | "The membrane is made to vibrate by friction" |
| 231 | Friction drums with stick | ".11 fixed stick, .12 semi-fixed, .13 free stick" |
| 232 | Friction drums with cord | ".2 Friction drum with whirling stick" |
| 233 | Hand friction drums | — |
| 24 | Singing membranes (kazoos) | ".241 free kazoos, .242 tube- or vessel-kazoos" |

Suffixes for any division of membranophones (register #3 pp. 11–12) — **all of them
describe how the head is attached, none describes how the drum is played**:
`-1/-11/-12` transducer, microphone, pickup; `-6` membrane glued; `-7` membrane nailed;
`-8` membrane laced; `-81` cord-(ribbon-)bracing; `-811` tension ligature; `-812` tension
loops; `-813` wedge-bracing; `-82` cord-and-hide; `-83` cord-and-board; `-84`
cord-and-flange; `-85` cord-and-belt; `-86` cord-and-peg; `-9` membrane lapped on;
`-91` lapped onto a ring of cord; `-92` lapped onto a hoop; `-921` with mechanism
("Machine timpani"); `-9211` with pedals ("Pedal timpani").

### 2.2 What Hornbostel and Sachs said about playing technique — the decisive passage

Register #1, Würzburg reprint p. 11. The MIMO *Addenda & Corrigenda* (register #4,
footnote 1) gives the locator in the original and in translation: **ZfE xlvi (1914)
pp. 560–561 = Galpin Society Journal 14 (1961) pp. 11–12.** Verbatim German:

> "Gemeinsame Merkmale, die für alle Instrumente einer Klasse in Frage kommen könnten,
> z. B. **für Membranophone die Art der Fellbefestigung** und **für Chordophone die
> Spielweise**, werden abermals durch Ziffern notiert, die durch einen Bindestrich an die
> eigentliche Systemzahl angehängt werden"

Translation of the load-bearing part: the suffix mechanism carries, per class, the feature
that class needs — *for membranophones the manner of head attachment, and for chordophones
the manner of playing*. The authors had the mechanism to record playing technique, used it
for strings, and deliberately did not use it for drums. Knight states the same conclusion
in English (register #5 p. 18): "**Details of playing technique for membranophones are not
included in H-S**".

The same page also documents the numbering philosophy, which is the closest historical
precedent for KITWARP's sparse tuple:

> "Es ist klar, daß jeder selbst entscheiden kann, wieweit er im Einzelfall gehen mag."

— each cataloguer decides how deep to go; a shorter number is less specific, not wrong.
The 1914 worked example is a bell chime: 1 → 11 (Schlagidiophone) → 111 → 1112
(Aufschlagidiophone) → 11124 (Aufschlaggefäße) → 111242 (Glocken) → 1112422
(Glockenspiele) → 11124222 (Hängeglockenspiele) → 111242222 (Klöppelglockenspiele),
written 111.242.222.

**German terms from the 1914 essay**, usable as a register check: *Schlagidiophone*,
*Aufschlagidiophone*, *Aufschlaggefäße*, *Aufschlagstäbe*, *Aufschlagspiele*,
*Zupftrommeln*, *Reibinstrument*, *Hängeglockenspiele*, *Klöppelglockenspiele*.

**German terms from the ACDH-CH digital H-S** (register #27, `children` of concepts 1 and 2,
via WebFetch): idiophone branch *Schlag-Idiophone*, *Zupf-Idiophone*, *Reib-Idiophone*,
*Blas-Idiophone*, *Stampf-Idiophon*; membranophone branch *Schlagtrommeln*,
*Zupftrommeln*, *Reibtrommeln*, *Ansingtrommeln (Mirlitons)*. Top classes: Idiophone,
Membranophone, Chordophone, Aerophone, Elektrophone, **Hydrophone** — the last is an
extension MIMO's revision does not have.

### 2.3 The Knight Revision suffix glossary — the only organological technique vocabulary found

Register #5, "Suffix Glossary", pp. 37–38. Knight's framing is verbatim and matters:

> "Suffixes are used to include supplementary information about an instrument that does not
> change its classification. A K-Rev number without a suffix where one might be applicable
> is not wrong, it is simply less complete than if the information were known."

| Suffix | Meaning | Nearest KITWARP axis |
|---|---|---|
| `-1` | played with one stick | implement + limb count |
| `-2` | played with two sticks | implement + limb count |
| `-3` | played with one hand | implement `hand` |
| `-4` | played with two hands | implement `hand` |
| `-5` | played with stick and hand | implement, mixed |
| `-a` / `-b` / `-c` | thin / medium / thick head | **no KITWARP axis** — a build property |
| `-x` | "snare (of any material) crossing the surface of a drum head" | mechanism `wires-on` |
| `-h` | handle drum | **no axis** — build property |
| `-s` | "sympathetic or co-vibrator, idiophonic in nature, as in bottle caps on an mbira" | closest to `sizzle` as a build property, cf. §5.3 |
| `-e` | "electrically-powered sound modification, as in a vibraphone" | timbre, loosely |
| `-k` | keyboard | none |
| `-m` | mechanical activation | none |
| `#n` | number of sounding elements | closest to layout `instance` |
| `-6 … -9222` | head attachment, adopted from H-S with "bracing" renamed "lacing" | none |

Worked example, register #5 p. 38: `M11.15 -85 -s -b -4` = West African djembe, cord-and-hoop
lacing, sympathetic vibrators, medium-thick head, played with both hands.

Knight also adds a rule directly relevant to KITWARP's `site` axis (p. 18):

> "If the technique regularly includes hitting the drum shell with a stick, as in the
> Ghanaian atsimewu or the Korean puk, a dual classification as idiophone should be given."

That is organology's answer to `site = shell`: it is not a facet of the drum, it is a
second instrument. See §3.3.

### 2.4 MIMO — Thesaurus of musical instrument names

Facts, all from the live REST API on 2026-09-06:

| Property | Value | Locator |
|---|---|---|
| Concepts | **2 724**, 0 deprecated | `/rest/v1/InstrumentsKeywords/vocabularyStatistics` |
| Languages | 13: `eu ca zh nl en fr de it ko pl es sv dk` | `/rest/v1/InstrumentsKeywords/?lang=en` |
| prefLabel coverage | 2 724 in ca, de, en, es, eu (full); 2 477 in dk | `/rest/v1/InstrumentsKeywords/labelStatistics` |
| altLabel counts | de 257, dk 1 202, eu 59, es 52, en 36, ca 28 | same |
| Scheme created | 2010-04-20 | `dc11:created` on `…/InstrumentsKeywords#` |
| Still maintained? | **yes** — concept 11347 `Dongbal` has `dc11:created` **2019-03-05**; concept 6681 `Penzhong` 2011-06-28 | `/data?uri=…/11347` |
| Top concepts | 9: Electronic instruments, Mirlitons, Other instruments, **Percussion instruments (2370)**, Mechanical instruments, Keyboard instruments, Elements of musical instruments, Stringed instruments, Wind instruments | `/topConcepts` |
| Licence | **none stated** anywhere in the REST metadata, the concept scheme resource, or the Skosmos landing page | — |
| URI persistence | `http://www.mimo-db.eu/InstrumentsKeywords/2467` → HTTP 200, redirects to `vocabulary.mimo-international.com/InstrumentsKeywords/en/page/2467` | curl, 2026-09-06 |

**Percussion instruments (2370) — the 19 direct children**: Bells, Castanets, Clappers,
Cymbals, **Drum set**, Drums, Gamelan, Gongs, Jingles, Kettledrums, Lamellaphones,
Lithophones, Metallophones, Others, Ratchets, Rattles, Scrapers, Trumps, Xylophones.

Direct child counts, every one verified by its own `children` call:

| Branch | MIMO id | Direct children |
|---|---|---:|
| Drums | 2493 | **406** |
| Rattles | 3012 | 87 |
| Bells | 2371 | 69 |
| Gongs | 2807 | 65 |
| Others | 2988 | 54 |
| Xylophones | 3062 | 40 |
| Cymbals | 2451 | **39** |
| Clappers | 2424 | 39 |
| Metallophones | 2965 | 32 |
| Kettledrums | 2879 | 30 |
| Lamellaphones | 2912 | 30 |
| Scrapers | 3047 | 22 |
| Trumps | 2861 | 21 |
| Jingles | 2870 | 8 |
| Lithophones | 2949 | 5 |
| Castanets | 2420 | 4 |
| Gamelan | 2805 | 1 |
| Ratchets | 3010 | 1 |
| **Drum set** | **5702** | **1** |

The single child of `Drum set` is concept **5703, also labelled `Drum set`**, identical in
all 13 languages, with **zero** children of its own.

**The whole MIMO account of the drum kit is therefore two identical nested concepts and
nothing below them.**

The 39 children of Cymbals (2451), with ids:
`5424 Bhusyah, 2452 Bo, 2460 Chap, 2462 Ching, 2467 Choke cymbal, 2468 Chum choe,
2469 Crash cymbal, 2470 Crotales, 2471 Cymbals, 4930 Dobachi, 2472 Dobatsu, 11347 Dongbal,
11348 Hyangbal, 2454 Jabara, 5242 Jhalica, 5243 Kangsi, 2475 Kartal, 2476 Kasat,
5506 Kecer, 4880 Mandira, 2478 Manjira, 6681 Penzhong, 5334 Rincik, 2479 Rol-mo,
2480 Sajat, 2482 Sanj, 2484 Sbub-chal, 5351 Sichyah, 2487 Sil-snyan, 5489 Silnen,
2488 Sizzle cymbal, 2489 Sock cymbal, 5365 Tah, 5366 Tahca, 5372 Talam, 5384 Than lvin,
2490 Ting-ting-shags, 5639 Zang, 2492 Zil`.

Of the 39, exactly four are drum-kit cymbals: **Choke cymbal (2467)**, **Crash cymbal
(2469)**, **Sizzle cymbal (2488)**, **Sock cymbal (2489)**. There is no ride, no china, no
splash, no stack. All four `exactMatch` the same H-S node, `HornbostelAndSachs/10` =
**111.142 Cymbals**, which is itself `exactMatch`ed by 23 different instrument-keyword
concepts.

Multilingual labels for those four (from `/data?uri=…`):

| MIMO id | en | de | fr | it | es | pl | nl |
|---|---|---|---|---|---|---|---|
| 2451 | Cymbals | Becken | Cymbales | Cimbali | Címbalos | Talerze | Cimbalen |
| 2467 | Choke cymbal | **Hi-hat** | Cymbale choke | Piatto choke (Hi-hat) | Címbalo | Talerz tłumiony | Chokecimbaal |
| 2469 | Crash cymbal | Crashbecken | Cymbale crash | Piatto crash | Címbalo | Talerz crash | Crashcimbaal |
| 2488 | Sizzle cymbal | Sizzle cymbal | Cymbale sizzle | Piatto chiodato | Címbalo ribeteado | Talerz z nitami | Sizzle cimbaal |
| 2489 | Sock cymbal | **Hi-hat** | Cymbale sock | Piatto sock (Hi-hat) | Címbalos de pinza | Niski hi-hat | Sock cymbal |

Drum set, all languages (5702 and 5703 are identical): en *Drum set*, de *Schlagzeug*,
fr *Batterie*, it *Batteria*, es *Baterías* / *Batería*, nl *Drumstel*, sv *Trumset*,
pl *Zestaw perkusyjny*.

### 2.5 Getty AAT

| Concept | AAT id | Direct parent |
|---|---|---|
| musical instruments | 300041620 | `<sound devices by function>` |
| percussion instruments | 300041726 | musical instruments |
| **idiophones** | 300041646 | **`<sound devices by acoustical characteristics>`** |
| **membranophones** | 300041661 | **`<sound devices by acoustical characteristics>`** |
| drums (membranophones) | 300041729 | membranophones |
| **drum kits** | **300411407** | drums (membranophones) |
| cymbals | 300041897 | concussion vessels |
| percussion instrument components | 300191003 | sound device components |
| percussion beaters | 300042611 | percussion instrument components |

AAT keeps **two parallel hierarchies**: functional (`musical instruments → percussion
instruments`) and acoustical (`idiophones` / `membranophones`). An instrument sits in one
or the other, so `percussion instruments` has only 92 extended descendants while
`idiophones` has 177 that are not among them.

`drum kits` (300411407) has **zero narrower terms**.
`cymbals` (300041897) has exactly three: `crotales` (300041899), `jalra` (300265926),
`zils` (300214184).
`percussion beaters` (300042611) has exactly five:

| AAT id | Term | Verbatim scope note |
|---|---|---|
| 300042613 | drumsticks (percussion beaters) | "Sticks, usually of wood, either padded with fabric or some other soft material on one end or plain, used to strike drums." |
| 300042609 | hammers (percussion beaters) | "Percussion beaters consisting of sticks with knobs or padded heads with which such instruments as xylophones, tubular bells, and certain types of dulcimers are struck." |
| 300429059 | percussion brushes | "Percussion beaters consisting of wires or other flexible material attached to a handle, used to strike or excite drums and cymbals for a softer sound." |
| 300425007 | gong mallets | "Percussion beaters specifically used to strike gongs." |
| 300191303 | clappers (bell components) | "Tongues of metal or wood in various types of open bells which produce the sound by striking the side of the instrument…" |

`percussion brushes` has one child, `wire brushes (percussion beaters)` 300202390.

**AAT has no drum-kit cymbal type and no percussion playing technique.** A Lucene search
for `hi-hat hihat ride crash splash china sizzle cymbals` over the whole AAT returns
`cymbals` and 40 irrelevant hits (`crash helmets`, `china caps`, `hat brushes`, `Hi-8`).
A prefLabel regex for `^(rim shot|rimshot|flam|drag|roll|ruff|sidestick|choke|muffl|damping|tremolo|glissando|playing technique)`
returns only `damping` (300256220, a generic activity) and unrelated words
(`Dragestil`, `Flamboyant`, `choke collars`, `dragnets`).

Licence: **ODC-By 1.0**, with a mandatory attribution string — "Contains information from
the J. Paul Getty Trust, Getty Research Institute, the Art & Architecture Thesaurus, which
is made available under the ODC Attribution License." Web interface refreshed monthly; LOD
refreshed periodically. Locator: `https://www.getty.edu/research/tools/vocabularies/obtain/index.html`.

### 2.6 Library of Congress LCMPT

942 concepts in the file stamped 2026-09-02. The `percussion instrument` subtree
(`mp2013015544`) has 231 nodes. Structure and selected leaves:

```
percussion instrument                      mp2013015544
├── drum                                   mp2013015218   (63 children)
│   ├── bass drum                          mp2013015065
│   ├── snare drum                         mp2013015657   UF side drum, caixa
│   │   ├── surdo, tabor, tamboril, tambourin
│   ├── tom-tom                            mp2013015737   UF Chinese tom-tom
│   ├── timpani                            mp2013015733   UF kettledrums
│   ├── roto-tom                           mp2019015002
│   ├── frame drum  mp2013015269  ├── tambourine mp2013015705 (UF pandeiro, adufo)
│   ├── goblet drum, hourglass drum, friction drum (cuíca, string drum "Löwengebrüll")
│   ├── conga, bongos, tabla, taiko, mridanga, …
├── drum set                               mp2013015222   UF traps, trap set, drum kit,
│                                                            trap kit, drumset  (0 children)
├── percussion controller                  mp2013015541
│   └── mallet controller                  mp2013015442   UF xylophone controller
├── struck idiophone                       mp2013015682
│   ├── concussion idiophone               mp2013015170
│   │   ├── body percussion                mp2013015090
│   │   │   ├── armpit squeezing, body slapping, finger snapping, foot tapping
│   │   │   │   (UF foot clapping, foot percussion, podorhythm),
│   │   │   │   hand clapping, head rapping, vocal percussion (UF mouth drum,
│   │   │   │   bouladjèl), whistling
│   │   ├── castanets, ching (cymbals), clapper (percussion) → bones, jin qian ban,
│   │   ├── clapsticks (UF bilma, clapping sticks), claves,
│   │   ├── cymbal                         mp2013015195   UF cymbals  → jao pa, jhāñjh
│   │   └── finger cymbals                 mp2013015263   UF zils, zilia
│   ├── indirectly struck idiophone        mp2013015353
│   │   ├── Talerschwingen (UF Talerrollen), jawbone (UF quijada de burro)
│   │   ├── scraped idiophone  mp2019015022 → guiro, notched rattle, reco-reco, washboard
│   │   ├── shaken idiophone   mp2019015021 → angklung, cabaca (UF shekeré, chekeré),
│   │   │       egg shaker, jingles (UF ankle bells) → jingle bells (UF sleigh bells),
│   │   │       maraca, rainstick, rattle → baby rattle, sistrum
│   │   └── vibraslap                      mp2019015024
│   ├── anvil, musical saw, amplified palette
│   └── percussion idiophone               mp2013015543
│       ├── bell → agogo, bian zhong, carillon, chimes → clock chimes / handchimes,
│       │       cowbell (UF Almglocke), ekón, handbell, singing bowl, sistro,
│       │       tap bell, tubular bells (UF orchestral chimes)
│       ├── brake drum (UF irons), cajón, catá, crotales, gong → ching, hsiao luo,
│       │       tam-tam, steel drum, triangle, lithophone, metallophone,
│       ├── slit drum → temple blocks (UF granite blocks, tone blocks),
│       │       teponaztli, wood block (UF bangzi, clog box, Chinese wood block, tap box)
│       ├── percussion tube (UF boomwhacker, stamping tube, pounding stick)
│       └── mallet instrument (UF keyboard percussion instrument) → glockenspiel,
│               marimba, vibraphone, xylophone, xylorimba, …
├── thunder sheet (UF thundersheet)        mp2019015001
├── balloon, flowerpot, glass, tin can, sound effects, spoils of war
└── struck string instrument (berimbau, clavichord, dulcimer, piano, …)
```

Also in LCMPT but outside the percussion-instrument subtree: `drum machine`
(mp2013015221, UF *rhythm machine*, *preset rhythm machine*, *sampling drum machine*,
**electronic percussion**, **electronic drum**), `percussion ensemble`, `MIDI controller`.

**LCMPT has no hi-hat, no ride cymbal, no crash cymbal, no china, no splash, no stack, no
kick as distinct from bass drum, and no playing technique of any kind.** Licence: "The
Library of Congress has prepared this linked data system and is making it available as a
public domain data set" (`https://id.loc.gov/about/`).

### 2.7 Wikidata

| Property | Statements site-wide |
|---|---:|
| P1762 Hornbostel-Sachs classification | 2 401 |
| P3763 MIMO instrument ID | 1 025 |
| P1330 MusicBrainz instrument ID | 972 |
| P1014 Art & Architecture Thesaurus ID | 25 242 (all subjects) |

Under *percussion instrument* (Q133163): **877** items, of which 350 carry P1762, 162
carry P3763, 155 carry P1330 and 115 carry P1014.

Kit-relevant items, with the authority ids they actually carry:

| Item | Label | P1762 (H-S) | P3763 (MIMO) | P1330 (MB) | P1014 (AAT) |
|---|---|---|---|---|---|
| Q128309 | drum kit | 211.212.21 | 5702 **and** 5703 | 12092505-6ee1-… | — |
| Q208421 | snare drum | 211.212.11 | 2729 | 947cca7d-74c6-… | 300041755 |
| Q211028 | bass drum | 211.212.1 | 2506 | e78b40c0-acc8-… | 300041732 |
| Q190172 | cymbal | 111.142 | 2451 **and** 2471 | 0fe1a768-45ba-… | 300041897 |
| Q963334 | **hi-hat** | — | — | 6d328aab-3bee-… | — |
| Q93985 | crash cymbal | 111.24 | 2469 | — | — |
| Q93992 | **ride cymbal** | 111.24 | — | — | — |
| Q1074981 | splash cymbal | 111.24 | — | — | — |
| Q193666 | tambourine | 112.1 **and** 211.311 | 2746 | 4431f7b0-69a4-… | 300041759 |
| Q775570 | cowbell | 111.242.11 | 2390 **and** 2389 | 2b75a5bc-f9ce-… | 300041875 |
| Q390110 | vibraslap | 112.1 | 4974 | 9c79b6a1-89bb-… | — |
| Q1024685 | cabasa | 112.13 | 6634 | 33b6ba89-8265-… | — |
| Q201735 | triangle | 111.211 | — | 63cfd648-2022-… | 300041911 |

No item matching `china cymbal`@en was returned by the label query.

### 2.8 MusicBrainz

288 instruments of type *Percussion instrument*. Kit-relevant entities:

| MBID | Name | Disambiguation |
|---|---|---|
| 12092505-6ee1-46af-a15a-b5b468b6b155 | drums (drum set) | "Set of drums in modern music" |
| 947cca7d-74c6-4044-b6cc-71a1180d0b28 | snare drum | — |
| 80eb5b78-b3eb-401a-b774-6a922cfee238 | tom-tom | — |
| 6d328aab-3bee-4d9d-b400-e1e71ff96f37 | **hi-hat** | — |
| 0fe1a768-45ba-49e4-8363-14db8e73ca85 | cymbal | — |
| 74e8088e-d5b0-44bc-853a-74aa8c8aa5aa | finger cymbals | — |
| 2b75a5bc-f9ce-49e8-ace8-35e5925fff4a | cowbell | "Tuned metal bell" |
| ec7a5fbf-f374-4bdb-8c1d-fabc7a8424c0 | wood block | — |
| 88dad742-e0b7-4ad4-811d-e32b6d2b847d | caixa | "Deep Brazilian samba snare-drum" |
| c9af11ea-cb3a-492c-90bb-f4b57637824a | tarol | "Shallow Brazilian samba snare-drum" |
| 2e899f30-ac87-4ea9-88bf-9b4b573bab63 | washboard | "American scraped idiophone" |

A search for `cymbal` over the whole instrument entity returns 5 hits, of which only
`cymbal` and `finger cymbals` are cymbals. **MusicBrainz has hi-hat but no ride, crash,
china or splash.** Core data is CC0.

### 2.9 DOREMUS — checked because it advertises playing techniques, and it does not have them

`git clone --depth 1 https://github.com/DOREMUS-ANR/knowledge-base.git`, HEAD 2024-03-29.

- `vocabularies/technique.ttl` — "Instrument playing or voice production techniques" /
  "Techniques vocales ou de jeu instrumental". `dct:license` CC BY 4.0, `dct:created` and
  `dct:modified` both 2018-07-19. **20 concepts, all vocal**: blow (fr *souffle*, it
  *soffio*), breathing, cantillation, coloratura, cry, incantation, rapping, scat, throat
  singing, ululation, ventriloquy, whistling, and eight more of the same kind. Nothing
  instrumental, nothing percussive.
- `vocabularies/performance_mode.ttl` — 5 concepts: improvisation, improvisation (in part),
  a cappella, a cappella (in part), four hands. CC BY 4.0.
- `vocabularies/mop-mimo.ttl` — a flat triple dump of MIMO, **2 572 distinct
  `InstrumentsKeywords/{n}` URIs**, carrying **no licence statement of its own**. Compare
  the live MIMO figure of 2 724: the DOREMUS snapshot is at least 152 concepts behind.
  (The exact snapshot date is UNVERIFIED — the shallow clone dates every file to HEAD.)
- Seventeen other DOREMUS vocabularies carry CC BY 4.0; one carries the French Licence
  Ouverte.

### 2.10 The two instrument-*parts* vocabularies, checked because they are where a `site` axis could hide

Both authority files that have a parts branch were walked to the leaf. Neither contains a
striking site.

**MIMO, `Elements of musical instruments` (concept 2205)** — a top concept of the
thesaurus, alongside `Percussion instruments`. Seven branches, 21 leaves in total:

| Branch | id | Children |
|---|---|---|
| Beaters | 6068 | Beater (6071), Gaktoe (11330), Galgo stick (11556), Janggu stick (11408), Ji (11331), Jin (11333) |
| Bows | 2206 | Ajaeng bow, Bow (2207), Haegeum bow, Sanjo ajaeng bow |
| Bridges | 11403 | Anjok, Wonsan |
| Frets | 11415 | Fret, Gwea |
| Mouthpieces | 6067 | Hyeo, Mouthpiece (6073) |
| Pegs | 11420 | Dolgwea, Jua, Peg |
| Plectra | 6070 | Plectrum (6074), Suldae |

Fifteen of the 21 are Korean-specific instances added late (ids in the 11xxx range). **The
branch contains no drumhead, no rim, no shell, no hoop, and no cymbal zone.** MIMO's
`Bows` here are violin bows, not cymbal bows — see §4.8.

**Getty AAT, `percussion instrument components` (300191003)** — 12 concepts in the whole
extended branch:

| AAT id | Term | Parent |
|---|---|---|
| 300041845 | drum components | percussion instrument components |
| **300041846** | **drumheads** | drum components |
| **300041856** | **shells (drum components)** | drum components |
| **300041860** | **snares (drum components)** | drum components |
| 300042611 | percussion beaters | percussion instrument components |
| 300042613 | drumsticks (percussion beaters) | percussion beaters |
| 300042609 | hammers (percussion beaters) | percussion beaters |
| 300433366 | xylophone hammers | hammers (percussion beaters) |
| 300425007 | gong mallets | percussion beaters |
| 300429059 | percussion brushes | percussion beaters |
| 300202390 | wire brushes (percussion beaters) | percussion brushes |
| 300191303 | clappers (bell components) | percussion beaters |

`drum components` has exactly three children, and they are the entire vocabulary of drum
anatomy available anywhere in this bucket: **head, shell, snares**. A prefLabel query for
`rims`, `hoops`, `counterhoops`, `lugs`, `tension rods`, `bell of…`, `bow of…` returns only
unrelated senses — `rims (container components)`, `rims (landforms)`, `hoops (toys)`,
`hoops (shaping garments)`, `lugs (knobs)`. **There is no drum rim and no cymbal bow, bell
or edge concept in the Getty AAT.**

### 2.11 GND — the German national authority file, checked last and worth the trip

Queried through lobid (`https://lobid.org/gnd/search?q=…&format=json` and
`https://lobid.org/gnd/{id}.json`). GND subject headings in category 14.3
*Musikinstrumentenkunde, Musikinstrumentenbau*: **908**. Licence, stated per record in
`describedBy.license`: **CC0 1.0**. Maintainer DE-101 (Deutsche Nationalbibliothek).

| GND id | preferredName | variantName | Broader | Note |
|---|---|---|---|---|
| **7525743-9** | **Hi-Hat-Maschine** | High-Hat, **Hi-Hat**, High-Hat-Maschine | Becken \<Musikinstrument\> | see the definition below |
| 7542598-1 | Becken \<Musikinstrument\> | Becken \<Musik\>, Cymbeln, Zimbeln, Kymbala \<Becken\> | — | — |
| 4137284-0 | Schlagzeug | **perc, Schz, Drumset** | — | the variants are score abbreviations |
| 4226169-7 | Elektronisches Schlagzeug | **el-perc, E-Schz, el-dr, E-Drums** | — | score abbreviations again |
| 7542431-9 | Kleine Trommel | — | — | snare drum |
| 4117255-3 | Trommel | — | — | — |
| 4504967-1 | Tamburin | Tambourin \<Musikinstrument\>, Schellentrommel | — | — |
| 133326514X | Kuhglocke \<Musikinstrument\> | Cowbell | — | distinct from 4165940-5 *Kuhglocke* (variant *Treichel*), the farm object |

**GND 7525743-9, verbatim definition** — the only definition of a hi-hat found in any
authority file in this bucket:

> "Zwei gegeneinander auf einen Ständer montierte Becken. Das obere bewegliche wird mittels
> eines Pedalmechanismus' gegen das fixierte untere Becken geschlagen. Das Instrument wird
> auch mit Trommelstock oder Besen angeschlagen."

That single sentence carries four of KITWARP's axes at once: the pedal `mechanism`, the
two-cymbal construction, and two `implement` values (*Trommelstock*, *Besen* — stick and
brush). It is also the only place in the bucket where an authority file acknowledges that
one instrument is played with more than one implement.

GND has **no** concept for ride, crash, china or splash cymbal.

Two things GND does that KITWARP should notice:

1. **Homonym qualifiers in angle brackets.** *Becken* alone is a pelvis, a basin, a
   geological basin and a technical vessel; GND ships seven of them and disambiguates with
   `Becken <Musikinstrument>`, `Becken <Anatomie>`, `Becken <Geologie>` and so on. This is
   the practice KITWARP needs for `bell` and `bow` (§4.8, §5.3), arrived at independently
   by a national library.
2. **Score abbreviations as variant names.** `Schlagzeug` carries `perc`, `Schz`,
   `Drumset`; `Elektronisches Schlagzeug` carries `el-perc`, `E-Schz`, `el-dr`, `E-Drums`.
   Those are exactly the tokens a parser meets in a German score or a device menu, and no
   other authority file records them.

---

## 3. Axis mapping

### 3.1 Terms that map cleanly onto a KITWARP axis

| Source term | Locator | KITWARP axis | KITWARP value |
|---|---|---|---|
| Cymbals (111.142) | MIMO 2011 p. 4 | instrument | `cymbal` |
| Crash cymbal | MIMO 2469 | instrument | `crash` |
| Sizzle cymbal | MIMO 2488 | instrument | `sizzle-ride` (approximate; see §5.3) |
| Sock cymbal | MIMO 2489 | instrument | `hihat` |
| Side drum (211.212.11) | MIMO 2011 p. 8 | instrument | `snare` |
| Bass drum in marching band (211.212.12) | MIMO 2011 p. 8 | instrument | `kick` |
| Drum set / Schlagzeug / Batterie | MIMO 5702 | — | the whole layout, not a term |
| tom-tom | LCMPT mp2013015737 | instrument | `tom` |
| roto-tom | LCMPT mp2019015002 | instrument | near `octoban` (§4.7) |
| cowbell / Almglocke | LCMPT mp2013015187 | instrument | `cowbell` |
| wood block, temple blocks | LCMPT mp2017015001 / mp2023015004 | instrument | `woodblock` |
| tambourine | LCMPT mp2013015705 | instrument | `tambourine` |
| triangle | LCMPT mp2013015746 | instrument | `triangle` |
| tubular bells / orchestral chimes | LCMPT mp2013015754 | instrument | `chimes` |
| claves, clapsticks | LCMPT mp2013015156 / mp2013015845 | instrument | `sticks` |
| hand clapping | LCMPT mp2013015316 | instrument | `clap` |
| egg shaker, maraca, cabaca | LCMPT mp2019015023 / …450 / …109 | instrument | `shaker` |
| percussion controller, mallet controller | LCMPT mp2013015541 / …442 | instrument | `aux-pad` |
| drumsticks (percussion beaters) | AAT 300042613 | implement | `stick` |
| percussion brushes, wire brushes | AAT 300429059 / 300202390 | implement | `brush` |
| hammers (percussion beaters) | AAT 300042609 | implement | `mallet-*` |
| gong mallets | AAT 300425007 | implement | `mallet-soft` (approximate) |
| Knight `-3` / `-4` played with one/two hands | K-Rev p. 37 | implement | `hand` |
| Knight `-1` / `-2` played with one/two sticks | K-Rev p. 37 | implement | `stick` |
| Knight `-5` stick and hand | K-Rev p. 37 | implement | mixed, see §5.5 |
| Knight `-x` snare crossing the head | K-Rev p. 37 | mechanism | `wires-on` |
| H-S `-9211` with pedals | MIMO 2011 p. 12 | mechanism | pedal-operated, cf. `kick-*` |
| drum machine, electronic percussion, electronic drum | LCMPT mp2013015221 | timbre | `electronic` |
| drumheads | AAT 300041846 | site | `head` |
| shells (drum components) | AAT 300041856 | site | `shell` |
| snares (drum components) | AAT 300041860 | mechanism | `wires-on` |

That is the entire list. **Thirty-two mappings from six authority files and two
classification schemes, and twenty-four of them land on the `instrument` axis.** GND adds
no new axis coverage — its contribution is German labels, score abbreviations and one
definition, not new distinctions.

### 3.2 Axes for which no authority-file term exists at all

| KITWARP axis | Values in v0.1 | Authority terms found |
|---|---:|---:|
| `site` | 9 | **2 of 9** — AAT `drumheads` 300041846 → `head`, AAT `shells (drum components)` 300041856 → `shell`. Nothing for `rim`, `rim2`, `crossstick`, `bow`, `edge`, `bell`, `underside`, in any authority file (§2.10) |
| `position` | 4 | **0** |
| `contact` | 3 | **0** |
| `technique` | 24 | **0** |
| `ornament` | 9 | **0** |
| `openness` | 8 | **0** |
| `damping` | 5 | **0** (AAT 300256220 `damping` is a generic conservation/engineering activity, not an articulation) |
| `mechanism` | 4 | **3** — AAT `snares (drum components)` 300041860, Knight `-x` snare, H-S `-9211` pedal |
| `implement` | 14 | **7** — AAT's five beaters plus Knight's `-1`…`-5` |
| `dynamic` | 5 | **0** |
| `timbre` | 13 | **1** — LCMPT `drum machine` UF *electronic percussion* |
| `voicing` | 7 | **0** |

Even the two `site` hits are only nominally hits: AAT's `drumheads` and `shells` are
*museum object types* — a spare head in a drawer, a shell without hardware — not places on
an instrument that a stroke can land. Nothing in any authority file names a place on an
instrument as a place.

This is the single most important table in the dossier. **Organology and library
authority control describe objects, not events.** They answer "what is this thing in the
vitrine" and are silent on "what did the player just do to it". KITWARP's ten
non-instrument axes have no external anchor and never will have one from this literature.
That is not a gap in KITWARP's research; it is a structural property of the field.

### 3.3 Terms that fit NO KITWARP axis — the valuable residue

Per the brief, a term that fits no axis is the most valuable finding, because it means an
axis may be missing. Six candidates, ordered by how seriously KITWARP should take them.

**(a) Number of heads, and which heads are played.** H-S 211.212.11 "one skin used for
playing" versus 211.212.12 "both heads played"; Knight makes head count his *first*
subdivision, ahead of shape (K-Rev p. 18, following Dournon 1992:272–3). KITWARP has no
way to say "the resonant head was struck". This is not hypothetical: it is exactly what a
gong-drum kick, an underside tom hit, and Roland's `Bongo H Inner`/`Edge` pair are about,
and `site = underside` is doing that job today with a name that means something else.
**Recommendation: consider a `site` value `resonant-head`, or rename `underside`.**

**(b) Head thickness / build properties.** Knight `-a` thin, `-b` medium, `-c` thick head;
also `-h` handle drum, `-s` sympathetic vibrator (bottle caps on an mbira; by extension
sizzle rivets). None of these is a per-note articulation, so none belongs on the pivot.
They belong, if anywhere, on the **device layout** as instrument build metadata. KITWARP
currently smuggles one of them into the instrument axis as `sizzle-ride` (§5.3).

**(c) "Sets of" as a class distinct from "individual".** H-S distinguishes 111.241.1
individual gongs from 111.241.2 sets of gongs, 111.211 individual percussion sticks from
111.212 sets, and the whole drum kit is nothing but the "sets of" branch, 211.212.21.
KITWARP handles this correctly and better, with `instance` on the layout slot rather than
in the term. **No change needed — but this is direct organological support for the
decision, and should be cited in ADR-0001.**

**(d) Body percussion as an instrument.** LCMPT `body percussion` (mp2013015090) with
children *armpit squeezing*, *body slapping*, *finger snapping*, *foot tapping*, *hand
clapping*, *head rapping*, *vocal percussion*, *whistling*, all classified under
*concussion idiophone*. KITWARP has `clap` on the instrument axis and `hand`/`finger` on
the implement axis, which cannot express *finger snapping* (no instrument at all) or
*foot tapping* (the floor is the instrument — Knight p. 11 says so explicitly: "the floor
is the instrument – a struck idiophone, while the foot is only the beater"). Sample
libraries ship finger snaps. **Recommendation: `finger-snap` and `foot-stomp` are missing
instrument values, not technique values.**

**(e) Dual classification.** Knight p. 18: a drum whose technique regularly includes
hitting the shell "should be given" a dual classification as idiophone. KITWARP models the
same fact as `site = shell` on one term. Both are defensible; the point for the dossier is
that organology treats *striking a different part of the same object* as **a change of
instrument**, not as a facet. This is evidence for keeping `site` in the pivot term rather
than on the layout slot — the distinction is identity-bearing, not annotation.

**(f) Hydrophone.** ACDH-CH digital H-S has a sixth top class, Hydrophone, that MIMO's
revision does not. Irrelevant to KITWARP; recorded because it shows the classification is
still being extended and is not one identifier space (§4.2).

---

## 4. Conflicts and false friends

### 4.1 "Hi-hat" is the preferred German label of two different MIMO concepts

MIMO 2467 `Choke cymbal`@en has `Hi-hat`@de. MIMO 2489 `Sock cymbal`@en also has
`Hi-hat`@de. Both are children of `Cymbals` 2451; both `exactMatch` H-S 111.142. The
Italian labels compound it: 2467 is *Piatto choke (Hi-hat)*, 2489 is *Piatto sock
(Hi-hat)*. Basque calls 2467 *Splash txindata* — splash cymbal. Danish calls both simply
*Bækken*, and Spanish calls 2467 *Címbalo*, both of which just mean "cymbal".

So in MIMO, depending on the language you read, concept 2467 is a choke cymbal, a hi-hat,
a splash cymbal, or a cymbal. **This is the concrete reason KITWARP must not take display
names from MIMO even if it takes ids.**

### 4.2 "Hornbostel-Sachs number" is not one identifier space

Three maintained digital implementations disagree:

- MIMO's SKOS gives notation **15 = Metal sheets** (a Montagu addition), 16 = Flexed
  diaphragms.
- ACDH-CH's digital H-S gives a concept with English altLabel **`HS-15` = *Stampf-Idiophon***
  (stamped idiophone), directly under Idiophone, and adds a top class **6 Hydrophone**.
- The 1914 original has neither.

Add Knight's K-Rev, which renumbers everything (`M11.15` for a djembe rather than
211.261), and Galpin's letter-and-numeral code (`III,i,A,a,1`), and the conclusion is
unavoidable: **a bare string like "111.142" is not a stable identifier unless the scheme
version is named alongside it.** If KITWARP records H-S notations at all, it must record
them as `hs-mimo-2011:111.142`, never as `111.142`.

### 4.3 A drum-kit cymbal is classified as a *concussion* idiophone

H-S 111.142 Cymbals sits under 111.14 "Concussion vessels or vessel clappers", defined as
"Two or more complementary sonorous parts are struck against each other" (111.1). That is
crash cymbals clashed in pairs. A suspended cymbal struck with a stick is by the scheme's
own logic a *percussion* idiophone (111.2, "struck either with a non-sonorous object (hand,
stick, striker)"), and there is no class for it — 111.24 Percussion vessels descends only
to gongs, bells, slit drums and troughs. MIMO nevertheless files `Crash cymbal`,
`Choke cymbal`, `Sizzle cymbal` and `Sock cymbal` under 111.142.

The October 2017 *Addenda & Corrigenda* (register #4) revisits the idiophones — it adds a
whole new class, **17 Shaken springs, Thunder tube**, and corrects 111.241.1 — and it
leaves 111.142 untouched. So this is not an oversight awaiting a fix; it is the settled
position of the classification.

The reason is historical and instructive: **H-S classifies by the canonical playing mode of
1914**, when the orchestral cymbal was a clashed pair. The whole of drum-kit practice —
suspended cymbal, stick, bow and bell zones, foot pedal — postdates the scheme and is
invisible to it. Wikidata partially corrects this by tagging crash, ride and splash
`111.24` instead of `111.142`, which contradicts MIMO. Both cannot be right.

### 4.4 MIMO's machine-readable Hornbostel-Sachs is six years behind MIMO's own published one

The October 2017 *Addenda & Corrigenda* (register #4) adds **class 17, "Shaken springs,
Thunder tube"**, as a new top-level subdivision of idiophones, citing Knight, GSJ 69 (2016)
p. 11. It also rewrites the definitions of 211.24 hourglass-shaped drums and 211.26
goblet-shaped drums, and fixes the cross-reference in the -81 suffix.

The live MIMO SKOS does not have any of it. A `children` call on the Idiophones node
returns exactly six: `11, 12, 13, 14, 15, 16`. **There is no 17.** The published standard
and its own machine-readable implementation, served by the same consortium, have been out
of step since 2017.

The consequence for KITWARP is narrow but real: if it records a Hornbostel-Sachs notation,
"which MIMO" is a second question after "which revision" (§4.2). The pinned form has to be
something like `hs-mimo-2011:111.142`, and even that does not say whether the 2017 addenda
were applied.

### 4.5 MIMO contains duplicate concepts for the same thing

`Drum set` exists twice, 5702 and 5703, with 5703 nested under 5702 and identical
prefLabels in all 13 languages. `Cymbals` exists twice, 2451 and 2471, with 2471 a child of
2451. Wikidata records **both** members of each pair on the same item (Q128309 carries
P3763 = 5702 and 5703; Q190172 carries 2451 and 2471). A KITWARP xref would have to pick
one, and there is no rule that says which.

### 4.6 Wikidata labels are not unique

The English label `triangle` is carried by five distinct Wikidata items (Q19821, Q201735,
Q2309718, Q11357200, Q89193228, Q107385829 — six, in fact); `cymbal` by four (Q190172,
Q3676836, Q4220665, Q136514071); `cowbell` by three; `tambourine` by four. Only Q201735
`triangle` and Q190172 `cymbal` carry AAT ids. Any label-based lookup into Wikidata is
therefore wrong by construction; only the Q-id is usable.

### 4.7 One-word false friends across the authority files

| Word | Meaning A | Meaning B | Locators |
|---|---|---|---|
| **tom-tom** | the kit tom | LCMPT's preferred sense is the *Chinese tom-tom* (that is its only UF term) | LCMPT mp2013015737 |
| **percussion instruments** | everything you hit | in Getty AAT, **membranophones only** — idiophones are in a separate hierarchy | AAT 300041726 vs 300041646 |
| **cymbal** | a suspended kit cymbal | in H-S, a *pair* clashed together (111.142, "vessel clappers") | MIMO 2011 p. 4 |
| **percussion** | striking | in Hornbostel-Sachs, `111.2 Percussion idiophones` is *specifically* the non-concussion case: struck with a non-sonorous object | MIMO 2011 p. 4 |
| **drum kit / drum set / traps** | the same object | LCMPT makes `drum set` preferred and `drum kit`, `traps`, `trap set`, `trap kit`, `drumset` variants | LCMPT mp2013015222 |
| **roto-tom** | a tunable single-head shell | Getty and LCMPT classify it under **frame drums** (AAT 300041844 parent `frame drums`) | AAT 300041844 |
| **bells** | a kit cymbal's bell zone | in every authority file, a bell is an *instrument* (LCMPT mp2013015079, AAT 300041872, H-S 111.242) | — |
| **Becken** (de) | cymbals, generic | KITWARP's `cymbal`; but MIMO's German for hi-hat is also a cymbal word | MIMO 2451 |
| **Schlagzeug** (de) | the drum kit | also, loosely, the whole percussion section | MIMO 5702 |
| **Batterie** (fr) | the drum kit | in orchestral French, the percussion section | MIMO 5702 |
| **caixa** | Brazilian samba snare, deep | LCMPT files it as a UF of `snare drum`; MusicBrainz makes it a *separate* instrument distinct from `tarol` (shallow) | LCMPT mp2013015657, MB 88dad742-…, c9af11ea-… |
| **damping** | KITWARP's `damping` axis | AAT 300256220 is a generic activity term unrelated to music | AAT |
| **mallet** | a percussion mallet | AAT's `mallets (striking tools)` 300024825 is a carpenter's mallet; the percussion sense is filed as `hammers (percussion beaters)` 300042609 | AAT |
| **beater** | a drum beater | AAT has three unrelated `beaters` — culinary tools 300201092, striking tools 300379166, textile-working equipment 300312126 — and the percussion sense only as `percussion beaters` 300042611 | AAT |
| **bow** | the playing area of a cymbal, between bell and edge | in MIMO's `Elements of musical instruments`, `Bows` (2206) are violin bows | MIMO 2206 |
| **shell** | KITWARP `site = shell`, a place to hit | in AAT, `shells (drum components)` 300041856 is the object, the drum body as an artefact | AAT |
| **Sidestick** | KITWARP `technique = sidestick` | GND 4370425-6 `Sidestick` is an **aircraft control stick**, broader term *Steuerknüppel*, subject category 31.7 *Fahrzeugbau, Fördertechnik, Raumfahrttechnik* | GND |
| **Kuhglocke** | the percussion cowbell, GND 133326514X, variant *Cowbell* | GND 4165940-5 *Kuhglocke*, variant *Treichel*, the farm object | GND |

### 4.8 A note on why `bow` is the worst word in the kit vocabulary

KITWARP `site = bow` means the sloping playing area of a cymbal. In every organological
source in this bucket, "bow" means a horsehair stick for exciting a string: MIMO's
`Elements of musical instruments` branch `Bows` (2206) contains `Bow`, `Ajaeng bow`,
`Haegeum bow`, `Sanjo ajaeng bow`. Hornbostel-Sachs uses it the same way. And bowing a
cymbal is a real, common extended technique that KITWARP will eventually need, at which
point `implement = bow` and `site = bow` will coexist and mean unrelated things in the same
term. This is the same species of collision as `bell` in §5.3, and it is worth catching
before the orchestral family is minted.

### 4.9 Different words, same thing

- `snare drum` = `side drum` = `caixa` (LCMPT UF ring) = H-S 211.212.11 "Side drum".
- `timpani` = `kettledrums` = H-S 211.11 "Separate vessel drums — European timpani".
- `tubular bells` = `orchestral chimes` = `chimes` (LCMPT UF) = H-S 111.231 "Tubular bell".
- `cabaca` = `shekeré` = `chekeré` = `guiro (rattle)` = `aggüé` = `agbe` (LCMPT UF ring —
  and note that `guiro` there means a *rattle*, not the scraper, which is a genuine trap).
- `finger cymbals` = `zils` = `zilia` (LCMPT) = `zils` (AAT 300214184) = `jalra` (AAT,
  India).
- `wood block` = `bangzi` = `bang zi` = `clog box` = `Chinese wood block` = `tap box`
  (LCMPT UF ring).
- `jingle bells` = `sleigh bells` (LCMPT), = `pellet bells` in AAT's hierarchy
  (AAT 300041886 `sleigh bells` under `pellet bells`).

---

## 5. Gaps against vocabulary v0.1

### 5.1 What the authority files say KITWARP is missing on the instrument axis

Terms that appear in **two or more** of {MIMO, LCMPT, AAT, Wikidata, MusicBrainz} and have
no KITWARP `instrument` value, restricted to things that plausibly appear in a drum
library or e-drum module:

| Missing term | MIMO | LCMPT | AAT | MB | Note |
|---|---|---|---|---|---|
| finger snapping | — | mp2013015264 | — | — | LCMPT only, but ships in most libraries |
| foot tapping / stomp | — | mp2013015840 | — | — | UF *foot percussion*, *podorhythm* |
| body slapping | — | mp2013015089 | — | — | — |
| vocal percussion / mouth drum | — | mp2013015836 | — | — | UF *bouladjèl* |
| castanets | ✓ (2370 child) | mp2013015114 | 300041917 | ✓ | reserved family, unminted |
| guiro (scraper) | ✓ Scrapers | mp2013015305 | ✓ | ✓ | `technique = scrape` exists, instrument does not |
| vibraslap | ✓ | mp2019015024 | — | ✓ | — |
| cajón | ✓ Cajon | mp2013015110 | — | ✓ | — |
| brake drum | — | mp2021015023 | — | ✓ | UF *irons* |
| thunder sheet | — | mp2019015001 | — | ✓ | H-S 15 Metal sheets |
| tam-tam / gong | ✓ Gongs (65) | mp2013015297 | 300041905 | ✓ | — |
| sleigh bells / jingles | ✓ Jingles | mp2021015001 | 300041886 | ✓ | — |
| agogo | ✓ | mp2014015007 | 300265898 | ✓ | — |
| claves | ✓ | mp2013015156 | 300041921 | ✓ | KITWARP has `sticks`, which is not the same object |
| timbales | ✓ | mp2013015732 | — | ✓ | — |
| conga / bongo | ✓ | mp2013015172 / …093 | 300041841 / 300041839 | ✓ | reserved family |
| tabla | ✓ | mp2013015694 | 300206829 | ✓ | reserved family |
| steel drum / steel pan | ✓ | mp2013015675 | — | ✓ | H-S 111.241.12 |
| ratchet | ✓ Ratchets | — | — | ✓ | H-S 112.24 cog rattle |
| washboard | — | mp2013015792 | — | ✓ | H-S 112.2 scraped |
| rainstick | — | mp2020015025 | — | ✓ | — |
| singing bowl | — | mp2013015647 | ✓ resting bells | ✓ | H-S 111.242.11 |
| flexatone | ✓ Others | — | — | ✓ | H-S 154, named in the MIMO PDF |
| lion's roar / string drum | — | mp2021015016 | — | — | UF *Löwengebrüll*, H-S 232 friction |
| cuíca | ✓ | mp2013015194 | — | ✓ | H-S 231 friction drum with stick |

These are all in the reserved-and-unminted percussion family, so none of them is a defect
in v0.1. The value of the table is that it is an **externally sourced work list** for when
that family is minted, with a provenance record already attached to each row.

### 5.2 What KITWARP has that no authority file has — and is therefore right to own

`ride`, `china`, `splash`, `stack`, `xhat`, `mini-china`, `mini-hihat`, `crash-ride`,
`jam-block`, `aux-pad`, `octoban`, and every value on the nine non-instrument axes.
Eleven of KITWARP's 27 instrument values, and 128 of its 155 terms, describe distinctions
that the organological literature has never had a reason to name.

### 5.3 Two v0.1 names that this bucket says are wrong

**(a) `sizzle-ride` is a build property wearing an instrument's clothes.** MIMO 2488
`Sizzle cymbal` / it *Piatto chiodato* / es *Címbalo ribeteado* / pl *Talerz z nitami* —
every one of those names means "riveted cymbal", a description of the object's
construction. Knight gives it a suffix, `-s` "sympathetic or co-vibrator", explicitly
*not* a classification change (K-Rev p. 37). The same physical ride is a sizzle ride with
rivets in and a plain ride with them out. **A rivet is to a ride what snare wires are to a
snare drum, and KITWARP already models the latter on the `mechanism` axis as
`wires-on`/`wires-off`.** `sizzle-ride` should be `ride` + a `mechanism` value
(`rivets-on`), for exactly the reason `kick.hit.wires-off` is not a separate instrument.

**(b) `bell` on the instrument axis collides with `bell` on the site axis.** KITWARP has
`instrument = bell` (id 17, family `kit.cymbal`) and `site = bell` (id 8). In every
authority file consulted, "bell" is an instrument in its own right — LCMPT mp2013015079
with 11 children, AAT 300041872, H-S 111.242 "Bells: the vibration is weakest near the
vertex", MIMO's `Bells` branch (2371) with **69** direct members. Two different things in KITWARP's own
vocabulary share one slug across two axes, and one of them is homonymous with a large
external class. ADR-0003 forbids renaming a slug, so the fix is a `correction` alias, but
the collision should at least be documented before the percussion family is minted and
real bells arrive.

### 5.4 One v0.1 name this bucket confirms is right

`crossstick` / `sidestick`. No authority file has the term, but every one of them treats
*striking a different part of the same object with a different part of the implement* as
identity-bearing rather than as annotation — Knight goes as far as demanding a dual
classification (§3.3e). KITWARP putting `site` and `contact` inside the pivot term, not on
the layout slot, is the organologically defensible choice.

### 5.5 An axis-shape observation KITWARP should take from Knight, not from MIMO

Knight's suffixes `-1` one stick, `-2` two sticks, `-3` one hand, `-4` two hands,
`-5` stick and hand encode **implement and hand-count in one symbol**. KITWARP splits
these correctly — `implement` on the term, `limb` on the layout slot — and that split is
better than Knight's. But `-5` "stick and hand" has no KITWARP expression at all: a
timbale played with a stick in one hand and the palm of the other is one event stream with
two implements. This is the same defect flagged in `07-percussion-naming.md` §2 about limb
versus hand-part, arriving from a different direction. **Recorded, not resolved.**

---

## 6. Self-critique (round C)

### 6.1 What is still missing from this bucket

- **The 1961 Baines–Wachsmann English translation** (register #2) was not read. Everything
  quoted here in English comes from the MIMO 2011 revision, which states it reproduces the
  1961 translation with revisions "not shown" in the version used. Where MIMO's English
  differs from Baines–Wachsmann, this dossier follows MIMO and does not know it.
- **Museum catalogue terminology** (the bucket brief asked for it) is only partly explored.
  The two *published* parts vocabularies were found and walked to the leaf — MIMO's
  `Elements of musical instruments` and Getty's `percussion instrument components`, §2.10 —
  and between them they yield two site terms, `head` and `shell`. What was **not** opened
  is the unpublished catalogue layer: CIMCIM's resources page and its brasswind
  terminology thesaurus, and the Horniman, MIM Brussels and Philharmonie de Paris
  catalogues. CIMCIM's brasswind thesaurus is the interesting one by analogy: if the
  committee produced a part-by-part terminology for one family, a percussion equivalent may
  exist or may be the obvious thing for KITWARP to look for. Confidence that no percussion
  parts thesaurus exists: **medium**, not high.
- **German museum vocabularies** — museumsvokabular.de and term.museum-digital.de — were
  identified but not fetched. They are the German-language equivalent of MIMO and would
  give a second, independent German label set to check MIMO's *Hi-hat* problem against.
- **GND** was queried after the search budget ran out, through the lobid JSON API, and is
  now the sixth column in §0.1 (§2.11). What was *not* done is an enumeration of its 908
  instrument headings; the coverage figure quoted for GND is a sample, marked UNVERIFIED.
  Its `broaderTermGeneral` graph was also not walked, so GND's hierarchy is undescribed.
- **LCGFT** was identified and not extracted. It is a genre/form vocabulary, so it would
  contribute nothing to the instrument axis; skipping it was a judgement, not an oversight,
  but it is untested.
- **The MIMO Addenda & Corrigenda** was read after the fact (register #4). It does not
  correct the cymbal misclassification; see §4.3, which is now a settled finding rather
  than a provisional one.
- **Nothing was extracted from Italian or Spanish scholarly sources.** The Italian and
  Spanish searches returned pedagogical material and Wikipedia-grade summaries, and the one
  peer-reviewed hit (Revista Musical Chilena 67/219, SciELO, "Clasificación
  Sachs-Hornbostel de instrumentos musicales") was not opened. Bucket 12 owns that ground.

- **The WebSearch budget for the session was exhausted twice**, the second time before the
  gap-closing searches in this section could be run. The two gaps that were closed after
  the first exhaustion (§2.10) were closed by querying APIs already known to work, not by
  searching. Anything that could only be found by search remains unfound.

### 6.2 The single most authoritative source not obtained

**The *Grove Dictionary of Musical Instruments*, 2nd edition, 2014 — specifically the
"Classification" article, vol. 1, pp. 568–79, by Klaus Wachsmann as expanded by Margaret
Kartomi and Jeremy Montagu, and the "Drum kit" article in Grove Music Online.**

`oxfordmusiconline.com` returns HTTP 403 to every request from this environment. Grove is
the only source that would have given a *scholarly, edited* account of drum-kit
terminology — hi-hat, ride, crash, bow, bell, rim shot, brush technique — with the
authority of a reference work rather than a vendor manual. Everything in §0.1 about the
absence of kit-level terms in the authority files is well evidenced; what Grove would add
is whether the *scholarship* has the terms even though the *thesauri* do not. If the
reconciliation pass can reach one paywalled source, this is the one.

Second choice: Kartomi 1990 (register #15), on Internet Archive as a lending item. It
would settle whether any of the seventeen classification systems she surveys uses playing
technique as a primary axis, which would be a direct precedent for KITWARP's design.

### 6.3 Where this dossier could be wrong

- The MIMO subtree walk under-returned children for at least one node (`Cymbals` came back
  with 8 of its 39 children on the recursive walk, correct on a direct query). **Every
  count in §2.4 quoted as a child count was re-verified by a direct `children` call; the
  aggregate figure of 973 concepts in the percussion subtree from the walk is therefore a
  lower bound and is not quoted anywhere as fact.** The authoritative total, 2 724, comes
  from `vocabularyStatistics`.
- The claim that MIMO is "still maintained" rests on one concept created 2019-03-05. That
  is seven years ago. A better test would be the MIMO service's own change log, which was
  not found.
- The coverage matrix in §0.1 was built by regex over label strings. Regex over labels is
  the very method §4.6 warns against. The eleven "no concept anywhere" verdicts were each
  re-checked by a targeted query per authority, but a concept hiding under an unexpected
  label (a `ride cymbal` recorded in AAT as, say, `suspended cymbals`) would have been
  missed. Confidence: high for MIMO and LCMPT, which were searched exhaustively over a
  complete local copy; **medium for AAT**, where only SPARQL probes were run.
- The four MIMO ids that Wikidata asserts for the core kit drums *were* checked back
  against the MIMO API and all four resolve correctly (`2729` = *Side drum* / de *kleine
  Trommel*, `2506` = *Bass drum* / de *Basstrommel*, `2746` = *Tambourine* / de
  *Tamburin*, `2390` = *Cowbell* / de *Kuhglocke*). The remaining Wikidata↔MIMO
  assertions in §2.7 were not spot-checked and are UNVERIFIED.

### 6.4 The one question this bucket cannot answer itself

MIMO publishes no licence. ADR-0004 says unknown licence means all rights reserved. But an
integer identifier minted by a third party, stored without any of that party's text, is
arguably a fact and not a reproduction — the same reasoning that lets this repository
publish note numbers. The distinction decides whether §0.4's recommendation is
implementable as written or whether the `mimo` namespace must be dropped from the xref
block, leaving AAT (ODC-By, attributable), LCMPT (public domain), Wikidata (CC0),
MusicBrainz (CC0) and GND (CC0). This is a licence-policy judgement, not a research question, and it is
recorded in the worker's `STATUS.md`.
