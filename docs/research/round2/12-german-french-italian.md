# Round 2, bucket 12 — Non-English score and pedagogical terminology

German, French, Italian and Spanish percussion terminology, taken from score practice,
pedagogical literature, organological thesauri, official examination standards and vendor
instrumentology.

Two deliverables, per `.agents/round2/12-german-french-italian.md`: a **synonym
concordance** across the languages, and — the more valuable one — **every technique that
only a non-English tradition names**, because those are the places where the English
vocabulary has collapsed a distinction.

Conventions:

- `DE` German, `FR` French, `IT` Italian, `ES` Spanish, `EN` English.
- Every row carries a locator. Anything not verified against a named source is marked
  `UNVERIFIED` and is not presented as a finding.
- Axis names are the KITWARP axes from `.agents/round2/BRIEF.md`: instrument, site,
  position, contact, technique, ornament, openness, damping, mechanism, implement,
  dynamic, timbre, voicing.
- Sources are cited by the `Sxx` id of the register in §1.

---

## 1. Candidate source register (round A)

Authority levels: **A** primary standard, treatise, official syllabus or museum thesaurus;
**B** professional vendor or institutional reference; **C** encyclopaedic or pedagogical
secondary; **D** aggregation.

| # | Title | Author / body | Year | Type | Locator | Lang | Auth | Reached |
|---|---|---|---|---|---|---|---|---|
| S01 | Instrumentology / Academy — Percussion, **German edition** | Vienna Symphonic Library | live | vendor instrumentology | https://www.vsl.co.at/de/academy/percussion (+ `/snare-drum`, `/timpani`, `/bass-drum`, `/cymbals`, `/suspended-cymbal`, `/tambourine`, `/tam-tam`, `/field-drum`) | DE | B | YES |
| S02 | Instrumentology / Academy — Percussion, **English edition** | Vienna Symphonic Library | live | vendor instrumentology | https://www.vsl.co.at/academy/percussion (same sub-paths) | EN with DE/FR/IT glosses | B | YES |
| S03 | *Le percussioni — storia e tecnica esecutiva nella musica classica, contemporanea, etnica e d'avanguardia*, 2 vols | Guido Facchin | Zecchini editore | treatise; extract PDF = complete table of contents (pp. I–XX), a four-language *Indice degli strumenti* from p. 1187, and sample chapters | https://www.zecchini.cloud/estratti/591.pdf | IT (index also EN/FR/DE) | A | YES (extract) |
| S04 | MIMO *Thesaurus of musical instrument names* (SKOS / Skosmos) | Musical Instrument Museums Online | live | museum thesaurus | https://vocabulary.mimo-international.com/InstrumentsKeywords/en/ ; REST: `https://vocabulary.mimo-international.com/rest/v1/InstrumentsKeywords/{search,data}` | 13 languages incl. DE/FR/IT/ES | A | YES |
| S05 | MIMO *Hornbostel-Sachs (classification)* (SKOS) | Musical Instrument Museums Online | live | museum thesaurus | https://vocabulary.mimo-international.com/HornbostelAndSachs/en/ | multi | A | partially (vocabulary listed, classes not walked) |
| S06 | *Systematik der Musikinstrumente. Ein Versuch* — German text and commentary | E. M. von Hornbostel, C. Sachs | 1914 | organological standard | https://www.musikwissenschaft.uni-wuerzburg.de/fileadmin/04070000/Instrumentensammlung/Materialien_Instrumente/Hornbostel_SysTex.pdf | DE | A | YES |
| S07 | *Bewertungskriterien und Literaturliste Perkussion* (Abiturprüfung Musik, G9) | Staatsinstitut für Schulqualität und Bildungsforschung (ISB), Bayern | n.d. | official examination standard | https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Faecher/Musik/Literaturlisten_G9/Perkussion.pdf | DE | A | YES |
| S08 | *Caisse claire — Modes de jeu* | Encyclopædia Universalis | live | encyclopaedia | https://www.universalis.fr/encyclopedie/caisse-claire-en-bref/4-modes-de-jeu/ | FR | C | YES |
| S09 | *Kleine Trommel* | Wikipedia DE | live | encyclopaedia | https://de.wikipedia.org/wiki/Kleine_Trommel | DE | C | YES |
| S10 | *Caisse claire* | Wikipedia FR | live | encyclopaedia | https://fr.wikipedia.org/wiki/Caisse_claire | FR | C | YES |
| S11 | *Wirbel (Spieltechnik)* | Wikipedia DE | live | encyclopaedia | https://de.wikipedia.org/wiki/Wirbel_(Spieltechnik) (via `de.wikipedia.org/w/api.php` extracts) | DE | C | YES |
| S12 | *Doppelschlag (Trommel)* | Wikipedia DE | live | encyclopaedia | https://de.wikipedia.org/wiki/Doppelschlag_(Trommel) | DE | C | YES |
| S13 | *Notation* (French drum-set notation conventions) | Percunivers | live | pedagogical | https://www.percunivers.com/notation.php | FR | C | YES |
| S14 | *Brahms* resource database — `modes de jeu` definition pages | IRCAM | live | research-institute database | https://brahms.ircam.fr/fr/definition/modes-de-jeu-de-la-trompette | FR | A | YES for trumpet only; **no percussion pages exist** — see §6 |
| S15 | *OrchideaSOL: a dataset of extended instrumental techniques for computer-aided orchestration* | Cella, Ghisi, Lostanlen, Lévy, Fineberg, Maresz | 2020 | dataset paper, direct descendant of IRCAM's SOL (1996–98) | arXiv:2007.00763 — https://arxiv.org/pdf/2007.00763 | EN | A | YES — 89 playing-technique classes, **none percussion** — see §6 |
| S16 | Dorico notation reference, *Techniques de jeu des instruments de percussions non chromatiques* | Steinberg | v3 archive | vendor documentation | https://archive.steinberg.help/dorico_pro/v3/fr/dorico/topics/notation_reference/notation_reference_unpitched_percussion/notation_reference_unpitched_percussion_playing_techniques_c.html | FR | B | YES — thin; only *ouverte* / *fermée* are named |
| S17 | *Programmi preaccademici — Strumenti a percussione* | Conservatorio di Musica "Jacopo Tomadini", Udine | n.d. | conservatory syllabus (official) | http://www.conservatorio.udine.it/pdf/preaccademici/percussioni.pdf | IT | A | YES |
| S18 | *Percusión para Dummies*, Spanish edition, publisher sample (front matter + full TOC) | Jeff Strong, ed. Planeta | n.d. | pedagogical | https://proassetspdlcom.cdnstatics2.com/usuaris/libros_contenido/arxius/38/37843_Percusion_para_dummies.pdf | ES | C | YES (TOC only; body pages 55–65 not in the sample) |
| S19 | *Pizzicato — L'écriture musicale de la batterie et des percussions*, incl. the **French General MIDI percussion map** | Arpège Musique | live | vendor documentation | http://www.arpegemusique.com/percussion.htm | FR | B | YES |
| S20 | *General MIDI* — Perkussionsklänge | Wikipedia DE | live | encyclopaedia | https://de.wikipedia.org/wiki/General_MIDI | DE | C | YES — significant negative, see §4 |
| S21 | *Handbuch des Schlagzeugs. Praxis und Technik* | Karl Peinkofer, Fritz Tannigel | Schott, 1981 | **the** German percussion reference work | ISBN 978-3-7957-2641-6; cited by S12 for the Einzelschlag/Doppelschlag/Pressschlag taxonomy at pp. 84–85 | DE | A | **NO** — see §6 |
| S22 | *Notazione percussioni* (handbook) | MuseScore | live | notation software documentation | https://musescore.org/it/manuale/notazione-percussioni | IT | B | NO — HTTP 403 |
| S23 | *Schlagwerk Notation* (Handbuch) | MuseScore | live | notation software documentation | https://musescore.org/de/handbuch/schlagwerk-notation | DE | B | NO — HTTP 403 |
| S24 | *Notazione comune per le percussioni* / *Rulli di tamburo* | LilyPond notation reference, Italian | v2.21 / v2.25 | notation software documentation | https://lilypond.org/doc/v2.25/Documentation/notation/drum-rolls.it.html | IT | B | NO — not attempted before time ran out |
| S25 | *Percussioni — L'arte della pratica e i rudimenti* | Marchingband.it | live | pedagogical | http://www.marchingband.it/content/percussioni-larte-della-pratica-e-i-rudimenti-i-parte | IT | C | NO |
| S26 | *Técnicas extendidas de percusión I* | Emusicarte | live | pedagogical | http://blog.emusicarte.es/tecnicas-extendidas-de-percusion-1/ | ES | C | NO — DNS timeout |
| S27 | *Music Notation in the Twentieth Century: A Practical Guidebook* | Kurt Stone | 1980 | notation standard | full PDF at https://hugoribeiro.com.br/biblioteca-digital/Stone-Music_Notation_20th_Century.pdf ; archive.org id `musicnotationint0000ston_h3s0` | EN, multilingual instrument tables | A | NO |
| S28 | *Music Notation: A Manual of Modern Practice* | Gardner Read | 1969 | notation standard | archive.org | EN | A | NO |
| S29 | *Spielanweisungen* (score-direction glossary) | Musiktreff.info | live | pedagogical glossary | https://www.musiktreff.info/spieltechniken/4956-spielanweisungen.html | DE | C | NO — HTTP 403 |
| S30 | *Musiklehre Online: Spielanweisungen* | musicademy.de | live | pedagogical glossary | http://www.musicademy.de/index.php?id=2591 | DE | C | NO |
| S31 | *Spielanweisungen* (engraving-house notes) | Vadon Music Preparation | live | engraving practice | http://www.vadonmusicpreparation.com/tag/spielanweisungen/ | DE | C | YES — strings only, no percussion content |
| S32 | *Klassifikation der Musikinstrumente nach Hornbostel/Sachs* | Universität Würzburg, Institut für Musikforschung | live | university course material | https://www.musikwissenschaft.uni-wuerzburg.de/musikinstrumente/organologie/systematiken/hornbostelsachs/ | DE | A | NO |
| S33 | *Grand traité d'instrumentation et d'orchestration modernes* | Hector Berlioz | 1843 | **treatise, pre-MIDI French primary** | archive.org id `grandtraitdins1843berl`; full text at https://archive.org/download/grandtraitdins1843berl/grandtraitdins1843berl_djvu.txt | FR | A | YES (poor OCR — see §2.13a) |
| S34 | *Batterie : les caisses* | marcdedouvan.com | live | pedagogical | http://www.marcdedouvan.com/instru.php?instru=caisses | FR | C | NO |
| S35 | Musique contemporaine — performer's own modes-de-jeu catalogue | Camille Émaille | live | performer catalogue | https://camilleemaille.com/projets/musique-contemporaine/ | FR | C | NO |
| S36 | *Schlagzeugbegriffe* | d-drums Schlagzeugschule Berlin | live | pedagogical glossary | https://schlagzeug-berlin.de/schlagzeugbegriffe-in-den-ring-geworfen/ | DE | C | NO |
| S37 | *Wirbel* | Stabführer.de (Spielmannszug tradition) | live | trade/tradition glossary | https://stabfuehrer.de/wiki/Wirbel | DE | C | NO |
| S38 | *L'arte della percussione*, vol. 2 (sezione tamburo) | A. e A. Buonomo | Suvini Zerboni | method, named as required text by S17 | ISBN not captured | IT | A | NO |
| S39 | *La tecnica completa del tamburo* | F. Campioni | Sonzogno | method, named as required text by S17 | ISBN not captured | IT | A | NO |
| S40 | *Etüden für Timpani*, Heft 1 | Richard Hochrainer | Doblinger | method, named as required text by S07 | — | DE | B | NO |
| S41 | *Schlaginstrumente 2: Pauken* | Eckehardt Keune | Breitkopf & Härtel | method, named as required text by S07 | — | DE | B | NO |
| S42 | *Musik-Instrumentenkunde in Wort und Bild* | Erhard Walter Haupt, Emil Teuchert | 1911 | **pre-MIDI German organology**, public domain | archive.org id `musikinstrument00haupgoog`; full text at https://archive.org/download/musikinstrument00haupgoog/musikinstrument00haupgoog_djvu.txt | DE | A | YES |
| S43 | *Große Trommel und Becken-Schule nebst Anleitung zum Triangel-, Tamburin- und Tam-tam-Schlagen* | A. Deutsch | pre-1911 | method, named as a standard text by S42 p. 201 | — | DE | A | NO |
| S44 | *Schule für alle Schlaginstrumente* | H. Kling | pre-1911 | method, named as a standard text by S42 p. 201 | — | DE | A | NO |
| S45 | Instrumentology / Academy — vibraphone and gong, German edition | Vienna Symphonic Library | live | vendor instrumentology | https://www.vsl.co.at/de/academy/percussion/vibraphone ; `/gong` | DE | B | YES |

Reached in whole or part: **22 of 45**.

### 1.1 Discovery method, and what did not work

The session-wide WebSearch budget (200 calls) was exhausted after 8 breadth queries, none
of them attributable to this worker alone. Every fallback search endpoint the environment
offers refuses it: DuckDuckGo (`html.` and `lite.`) serves a CAPTCHA, Mojeek and Ecosia
return 403, Brave returns 429, searx.be serves a browser check, Bing returns its own
interface pages instead of results. **`web.archive.org` is blocked for WebFetch and its
CDX API is blocked for curl**, so the Wayback fallback the brief recommends does not work
in this environment.

What does work, and should be reused by other buckets:

- the MIMO Skosmos REST API (§2.1) — structured, multilingual, stable URIs;
- `https://<lang>.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1` and
  `action=parse&prop=wikitext` — full article text without HTML scraping;
- `archive.org/advancedsearch.php?...&output=json`;
- arxiv.org PDF fetch;
- direct `curl` to institutional and vendor PDFs, then `pdftotext -layout`.

Google Books API returned HTTP 429 (daily project quota exhausted).

---

## 2. Extracted terminology (round B)

### 2.1 Instrument names — five-language concordance (MIMO, S04)

From the MIMO Skosmos REST API, `skos:prefLabel` per language. The last column is the MIMO
concept id under `http://www.mimo-db.eu/InstrumentsKeywords/`.

| EN | DE | FR | IT | ES | MIMO id |
|---|---|---|---|---|---|
| Drum | Trommel | Tambour | Tamburo | Tambor | 2585 |
| Drums | — | Tambours | Tamburi | — | 2493 |
| Side drum | kleine Trommel | Caisse claire | Tamburo piccolo / Cassa chiara | Tambor vertical | 2729 |
| Bass drum | Basstrommel | Grosse caisse | Grancassa | Tambor bajo | 2506 |
| Kettledrum | Pauke | Timbale | Timpano | Tímpano | 2887 |
| Drum set | Schlagzeug | Batterie | Batteria | Baterías | 5702 |
| Tom-tom | Tom Tom | Tom-tom | Tom-tom | Tom-tom | 6540 |
| Frame drum | Rahmentrommel | Tambour sur cadre | Tamburo a cornice | Pandero | 2598 |
| Tambourine | Tamburin | Tambourin (alt. *Tambour de basque*) | Tamburello | Pandereta | 2746 |
| Cymbals (small, paired) | Becken | Cymbales | **Cimbali** | Címbalos | 2451 |
| Cymbals (orchestral pair) | Becken | Cymbales | **Piatti** | Címbalos | 2471 |
| Gong | Gong | Gong | Gong | Gong | 2820 |
| Triangle | Triangel | Triangle | Triangolo | Triángulo | 3005 |
| Cowbell | Kuhglocke | Sonnaille | Campanaccio | Cencerro | 2390 |
| Bell | Glocke | Cloche | Campana | Campana | 2381 |
| Castanets | Kastagnetten | Castagnettes | Castagnette | Castañuelas | 2420, 2423 |
| Maracas | Maracas | Maracas | Maracas | Maracas | 3031 |
| Claves | Claves | Claves | Claves | Claves | 2989 |
| Rattle | Rassel | Hochet | Sonaglio | Sonaja | 3036 |
| Scraper | Schrapinstrument | Râcloir | Raspa | Rascador | 3058 |

### 2.2 Instrument names — four-language concordance (Facchin, S03)

Facchin's *Indice degli strumenti*, from p. 1187, is itself a published four-language
cross-reference index: every EN, FR and DE trade name is listed and redirected to the
Italian head-word. Extract, restricted to terms that touch the kit and the orchestral
battery:

| DE | FR | EN | IT head-word (S03) |
|---|---|---|---|
| Kleine Trommel; Kleine Trommel mit Saiten | Caisse claire; Tambour à timbre | Snare drum | cassa chiara |
| Rührtrommel (implied) | Caisse roulante; Caisse sourde | — | tamburo rullante |
| — | Caisse plate | — | tamburo tarole |
| Basler Trommel | Tambour de Bâle | Basel drum | tamburo di basilea |
| — | — | Field drum | tamburo militare |
| Einfellige grosse Trommel | Grand tambour; Grosse caisse | Bass drum; Big drum | grancassa (sinfonica) |
| — | Grosse caisse avec pédale; Grosse caisse jazz | — | grancassa jazz a pedale |
| — | — | Gong bass drum; Gong drum | grancassa gong |
| Becken an der grossen Trommel befestigt | — | Bass drum with cymbal (one player) | grancassa e piatti |
| 2 Beckenteller; HandBecken | Cymbales à main; Cymbales à 2; Cymbales choquées; Cymbales cossé | Hand cymbals; Clashed cymbals; **Crash cymbals** | piatti a mano (o in coppia / a due) turchi |
| Becken auf Ständer; Freihängende türkische Becken | Cymbales suspendues; Cymbales turques | — | piatti sospesi turchi |
| Hi-hat Becken | Charleston; Cymbales charleston; Cymbales à pédale | Hi-hat; Hi-hat cymbals charleston; Foot cymbals | piatti a pedale |
| — | Cymbales grésillantes; Cymbales cloutées; Cymbales sizzle | Sizzle cymbals | piatti chiodati |
| Chinesische Becken | — | Chinese cymbals | piatti a mano (e sospesi) cinesi |
| Antike Zimbeln | — | Antique cymbals | cimbali antichi |
| — | Cymbales tibétaines | Tibetan cymbals | tingsha |
| Chinesisches Tom-tom; Einfell-Tom-tom | — | — | tom tom; tom tom a una e due pelli |
| Pauken; Kesselpauken; Chromatische Pauken | Timbales | Timpani | timpani |
| Jazzschlagzeug | Batterie jazz | Drum set; Drums; Rhythm | batteria jazz |
| Donnerblech | — | Thunder sheet | lastra del tuono |
| Provenzalische Tambourin | Tambourin de Provence; Tambourin provençal | — | tamburo provenzale e galoubet |
| — | Tambour de basque; Tambourin | Tambourine | tamburello (o tamburo) basco |
| Chromatische gestimmte Kuhglocken | — | — | campanacci latino-americani cromatici |

### 2.3 Snare drum — techniques, four languages

Source S01/S02: the same VSL page in its German and English editions, read side by side.
Locators `vsl.co.at/de/academy/percussion/snare-drum` and
`vsl.co.at/academy/percussion/snare-drum`, section *Spieltechniken* / *Playing Techniques*.

| DE (S01) | EN (S02) | FR (S02) | IT (S02) | Axis |
|---|---|---|---|---|
| Einzelschläge | Single stroke | — | — | ornament, attack count 1 |
| Doppelschlag; **Papa-Mama-Streich**; **Mühle** | Double stroke ("mammy-daddy beats") | — | — | ornament |
| Repetitionen | Repetitions | — | — | ornament |
| Vorschläge | Grace notes | — | — | ornament |
| Einfacher Vorschlag | Flam | — | — | ornament, 1 grace |
| Zweifacher Vorschlag | Drag | — | — | ornament, 2 grace |
| Dreifacher Vorschlag | Three stroke ruff | — | — | ornament, 3 grace |
| Vierfacher Vorschlag | Four stroke ruff | — | — | ornament, 4 grace |
| Paradiddle | Paradiddle | — | — | none — sticking, see §3.2 |
| Pralltriller | Tied trills | — | — | ornament |
| Wirbel | Rolls | — | — | ornament |
| Druckwirbel / Presswirbel / geschlossener Wirbel | Press roll, closed roll | — | — | ornament = `buzz` |
| Offener Wirbel | Open roll, two-stroke roll, "legitimate roll" | — | — | ornament = `roll` / `bounced` |
| — | One-stroke roll | — | — | ornament |
| Rim shot; **Randschlag** | Rim shot | — | — | technique = `rimshot` |
| Stick on stick | Stick on stick | — | — | technique = `stick-shot` |
| Rimclick | Rim click | — | — | technique = `sidestick` |
| Mit Stahlbesen | Wire brushes | — | — | implement = `brush` |
| **Auf dem Holz** | On the wood | **sur le bois** | — | site = `shell` |
| Mit entspannten Schnarrsaiten | With released snares | **sans timbre** | **senza corde** | mechanism = `wires-off` |
| Coperto | Muffled | **voilé** | *coperto* | damping = `damped` |

Italian names for the same field, from the Facchin chapter *CASSA CHIARA, TAMBURO DA
CONCERTO, TAMBURO PICCOLO*, pp. 463–482 (S03):

| IT (S03) | p. | gloss | Axis |
|---|---|---|---|
| Corde del timbro | 463 | the snare wires | mechanism |
| Smorzamento, sordina | 464 | damping / mute | damping |
| Presa delle bacchette | 465 | stick grip | none, §3.2 |
| Tecnica del rullo; Tipi di rullo | 466–467 | roll technique, roll types | ornament |
| Rulli forte-piano | 469 | fp rolls | ornament + dynamic |
| Rulli crescendo-diminuendo | 469 | swell rolls | ornament = `crescendo`/`swell` |
| Abbellimenti | 469 | ornaments | ornament |
| Scelta delle mani per l'esecuzione di un passo | 471 | choice of hands = sticking | none, §3.2 |
| **Colpi a sparo (rim shots) tra il controcerchio di metallo e la pelle** | 471 | literally "shot strokes", between the metal **counterhoop** and the head | technique = `rimshot`; site = `rim` |
| **Colpi sul bordo di legno e di metallo e tra bacchette** | 473 | strokes on the *wooden* rim, on the *metal* rim, and stick against stick | site — rim distinguished by material |
| **Zone di percussione** e altre tecniche per effetti timbrici e ritmici | 474 | "percussion zones" | site + position |
| Metodi di percussione ed effetti vari | 477 | striking methods and effects | technique |
| Cambiamenti graduali di intonazione | 478 | gradual pitch change | technique = `gliss` |
| Bacchette e mazzuole | 478 | sticks and mallets | implement |
| Spazzole di filo metallico | 478 | wire brushes | implement = `brush` |
| Percussione con le dita | 479 | finger strokes | implement = `finger` |
| Percussione con le mani | 480 | hand strokes | implement = `hand` |
| Allenatori di gomma | 482 | rubber practice pads | none — equipment |

### 2.4 Snare-drum stroke and roll taxonomy, Italian conservatory (S17)

Conservatorio di Udine, *Programmi preaccademici*, section *Tamburo*. This is an official
syllabus, so the terms are normative in Italian conservatory practice.

| IT | year/§ | gloss | Axis |
|---|---|---|---|
| presa a bacchette parallele | 1.1 | matched grip | none, §3.2 |
| presa tradizionale | 1.1 | traditional grip | none, §3.2 |
| colpo libero | 1.1 b | free stroke | technique |
| colpo singolo (semplice, accentato) | 1.1 c, 1.2 | single stroke, plain / accented | ornament + dynamic |
| **colpo "accademico"** | 1.1 d | "academic" stroke | technique — no KITWARP value |
| **colpo "a pistone"** | 1.1 d, 1.1 (yr 5) | "piston" stroke | technique — no KITWARP value |
| **"Full"**, **"Tap"** | 1.1 d | full stroke, tap stroke | dynamic — no KITWARP values for stroke *height* |
| colpo doppio | 1.5 a | double stroke | ornament |
| colpo doppio rimbalzato (accentato) | 1.5 a | rebounded double stroke, accented | ornament = `bounced` |
| **colpo pressato** | 1.5 b, 1.6 a | pressed stroke | ornament = `buzz`, as a *single stroke* |
| **rullo militare** (legato e slegato) | 1.5 a, 1.6 a | military roll, slurred and unslurred | ornament — no KITWARP value |
| rullo a colpi singoli (legato e slegato) | 1.6 a | single-stroke roll | ornament |
| rullo pressato (legato e slegato) | 1.6 a | pressed roll | ornament = `buzz` |
| **"scomposizione del rullo"** | 1.1 (yr 3) | "decomposition of the roll" — resolving a roll into its written strokes | none — a notation-reading concept |
| attacco del rullo con due …; attacco simultaneo del rullo | 1.6 a, 3.c | roll attack, simultaneous roll attack | technique |
| acciaccature singole / doppie / triple / quadruple / quintuple, **singole e rimbalzate** | 1.6 c | 1- to 5-grace ornaments, each in a *single-stroke* and a *rebounded* form | ornament — the count and the rebound are two independent parameters |
| tipi di colpo: doppio verticale, singolo indipendente, singolo alternato, doppio laterale | 2.3 b | the four Burton-grip four-mallet stroke types | technique — no KITWARP values |
| presa "Burton"; tradizionale, Musser, Stevens | 2.3, 2.3 a | four-mallet grips by name | none, §3.2 |
| smorzamenti ausiliari ("Dampening") | 2.4 | auxiliary damping on the vibraphone, beside the pedal | damping |
| allenatore | 1.1 c, 1.2 | practice pad, treated as a distinct *instrument* from the tamburo | instrument |
| incroci, allontanamenti | 4.1 a | crossings and spreadings between two timpani | technique = DE *Kreuzschlag* |

### 2.5 Timpani / Pauken

S01, `vsl.co.at/de/academy/percussion/timpani`, section *Spieltechniken*, cross-read with
S07.

| DE | gloss given by the source | Axis |
|---|---|---|
| Einzelschläge | single strokes | ornament |
| Coperto | covered / muffled | damping |
| Secco | dry single stroke | damping |
| Anschlag mit der Hand | hand strike | implement = `hand` |
| Repetitionen | repetitions | ornament |
| **Einfacher Kreuzschlag** | simple cross-beat | technique — no value |
| **Doppelter Kreuzschlag** | double cross-beat | technique — no value |
| Vorschläge | grace notes | ornament |
| Mehrfachschläge | multiple strokes | ornament |
| Paradiddle | paradiddle | none, §3.2 |
| Wirbel | roll, tremolo | ornament |
| **Doppelwirbel** | double roll — one roll on two drums at once | ornament + two instruments |
| **Übergangswirbel** | transition roll — a roll that migrates from one drum to another | ornament — no value |
| **Abschlag** | cut-off stroke: the stroke that *terminates* a roll | technique — no value |
| **Resonanzglissando** | pedal change while the head is still ringing | technique = `gliss` |
| **Wirbelglissando** | pedal change under a sustained roll | ornament + `gliss` |

Striking positions on the same page (`Schlagstelle`):

| DE | definition given | Axis |
|---|---|---|
| **Schlagfleck** | the ideal striking spot, "one hand's width from the edge" | position — no exact value |
| Fellmitte | centre of the head | position = `centre` |
| Fellrand | edge of the head | position = `perimeter` |

Mallets: Weichfilz, Hartfilz, Flanell, Holz (S01). S07 §*Pauken* adds head **size** as an
independent parameter: "Groß-, Mittel-, Kleinkopf, Filz-, Flanell- oder Holzschlägel".

S07 also states a rule that English notation does not carry: for timpani, "Wirbel werden
weder gedrückt noch gepresst, die Ausführung erfolgt immer 'Hand zu Hand' =
rechts-links-rechts-links". The timpani roll is by definition single-stroke; press rolls
are excluded on this instrument. S11 corroborates: "der Einzelschlagwirbel (z. B. auf der
Kesselpauke, oft **Paukenwirbel** genannt)".

### 2.6 Bass drum / Große Trommel

S01, `vsl.co.at/de/academy/percussion/bass-drum`.

| DE | gloss | FR where given | Axis |
|---|---|---|---|
| Einzelschläge | single strokes | — | ornament |
| Fellrand | rim, as a striking place | — | position = `perimeter` |
| Secco | single stroke, immediately damped | — | damping |
| Coperto | damped strokes | — | damping |
| **Con la mano** | hand strokes (fingers) | — | implement = `hand` / `finger` |
| **Unisono-Schläge** | unison strokes, two beaters as one | — | technique — no value |
| Repetitionen | repetitions | — | ornament |
| Wirbel | rolls | — | ornament |
| **Schlägel auf Schlägel** | beater on beater | — | technique, cf. `stick-shot` |
| Stahlbesen | wire brushes | — | implement = `brush` |
| Fußmaschine | bass pedal | — | mechanism |
| Großer Trommelschlägel | bass drum mallet | **mailloche** | implement |
| Hartfilzschlägel | hard felt mallet | — | implement = `felt-beater` |
| **Lederkopfschlägel** | leather-headed mallet | mailloche | implement — **no KITWARP value** |
| Holzkopfschlägel | wood-headed mallet | — | implement = `wood-beater` |

### 2.7 Cymbals — Becken / piatti / cymbales

S01, `/cymbals` (the clashed pair) and `/suspended-cymbal` (hängendes Becken).

Clashed pair:

| DE | gloss | Axis |
|---|---|---|
| Einzelschläge | single strokes | ornament |
| **Breiter Schlag** | broad stroke — the two plates slide across each other | technique — no value |
| Secco | struck then damped at once, dry and metallic | damping |
| Wirbel | rolls | ornament |
| **An der großen Trommel befestigt** | cymbal mounted on the bass drum, one player | mechanism / layout |
| **Strisciato** (pl. *strisciati*) | one plate rubbed from centre to edge across the inner face of the other | technique, cf. `scrape` / `sweep` |
| Vibrato | circular waving of the plates after the strike | technique — no value |
| Repetitionen | repetitions | ornament |
| Rand | edge — the plates are struck edge to edge | site = `edge` |
| Mitte | centre — held there by the strap, not struck | position = `centre` |

Suspended cymbal:

| DE | gloss | Axis |
|---|---|---|
| Einzelschlag | single stroke | ornament |
| Secco | dry, immediately damped | damping |
| Wirbel | roll | ornament |
| **Gestrichen** | bowed, with a cello or double-bass bow | technique — **no value** |
| **Nieten / Kugelkette / Stahlnadel** | rivets / ball chain / steel needle — three distinct sizzle devices | mechanism — **no values** |
| Besen | wire brushes | implement = `brush` |
| Repetitionen | repetitions | ornament |
| **Beckenkuppe** | dome stroke | site = `bell` |
| **Beckenrand** | rim / edge stroke | site = `edge` |
| Hand / Fingernagel | hand, fingernail | implement = `hand`, `fingernail` |

Beater materials, verbatim: "Garn, Schnur, Stoff, umwickelt, Gummi, Paukenfilz, Holz".
Implements: Paukenschlägel, garnumwickelte Schlägel, Holzschlägel, Trommelstöcke,
Triangelschlägel, Cello- oder Kontrabassbogen, Besen.

Facchin, *PIATTI SOSPESI TURCHI*, pp. 108–115 (S03):

| IT | p. | gloss | Axis |
|---|---|---|---|
| **Zone di percussione** | 111 | percussion zones on the plate | site + position |
| Tecniche per suonare il piatto sospeso | 112 | suspended-cymbal techniques | technique |
| Smorzamento dei piatti sospesi | 113 | damping | damping |
| Il tremolo o rullo e la sua tecnica | 113 | tremolo / roll | ornament |
| Piatti sospesi suonati con le spazzole | 114 | played with brushes | implement |
| Piatti sospesi appoggiati su una membrana di timpano e suonati con l'arco di contrabbasso | 115 | cymbal laid on a timpano head and bowed | technique + mechanism |
| Piatti sospesi con **cupola** cilindrica e **bordo** all'insù | 77 | cymbals with a cylindrical bell and an upturned edge | site = `bell`, `edge` |

Hi-hat, Facchin *PIATTI A PEDALE, HI-HAT, CHARLESTON*, pp. 102–106: *lo hi-hat moderno*
103, ***l'air-lock*** 104, *regolazione dello hi-hat* 104, *tecniche di esecuzione* 105,
*altri tipi di hi-hat* 105, *notazione* 106.

### 2.8 Tambourine — three rolls named by mechanism

S01, `vsl.co.at/de/academy/percussion/tambourine`. German names **three distinct rolls by
how they are produced**, where English says "roll" and at best qualifies it:

| DE | gloss | Axis |
|---|---|---|
| **Schüttelwirbel** | shake roll — the instrument is shaken and the jingles sound | ornament + technique = `shake` |
| **Daumen(spitzen)-Wirbel** | thumb-tip roll — a wetted thumb dragged around the head | ornament + technique = `swirl` |
| **Schlägel-Wirbel** | stick roll — struck with sticks | ornament + implement |

Striking positions: **Schlagfleck** (3–4 cm from the rim), **Fellrand**, **Fellmitte**.
Implements: Mittelfinger, Daumen, Fingerknöchel, Handballen, **Ellenbogen**, **Knie**,
kleine Trommelstöcke, Hart-/Weichfilzschlägel, Becken-/Xylophonschlägel, Triangelstäbe,
Holzschlägel.

Facchin confirms the tripartition in Italian and adds more: *Il rullo con il pollice* 446,
*Rullo con le mani* 456, *Rullo breve e continuato (fingerrolls)* 786, ***Rullo o tremolo
ad altalena con le dita*** 787 ("see-saw" finger roll).

### 2.9 Tam-tam and gong

S01, `vsl.co.at/de/academy/percussion/tam-tam`.

| DE | gloss | Axis |
|---|---|---|
| Einzelschläge | single strokes | ornament |
| Secco | dry, damped | damping |
| Wirbel | roll | ornament |
| Repetitionen | repetitions | ornament |
| Triangelstab | triangle beater used on the tam-tam | implement |
| **Superball** | rubber ball dragged to excite a friction tone | implement = `superball` |
| **Kralle** | "claw" — a scraper drawn across the surface | implement — **no value** |
| **Watergong** | the gong is lowered into water while sounding, bending the pitch | technique — **no value** |
| Gestrichen | bowed | technique — **no value** |
| Gedämpft | damped | damping |

Beater anatomy is named as four independent parameters: **Kopf** (head; Hartfilz, Holz,
Metall; 6–15 cm), **Bezug** (cover; Filz, schwerer Stoff), **Stiel** (handle, 28–35 cm),
**Form** (scheibenförmig, rund, rechteckig).

### 2.10 German roll taxonomy (S11, S12)

Wikipedia DE *Doppelschlag (Trommel)*, citing Peinkofer/Tannigel (S21) pp. 84–85:

> "Man unterscheidet im Schlagzeugspiel zwischen **Einzelschlag, Doppelschlag und
> Pressschlag**."

Three named *stroke* types, from which the roll types follow. *Wirbel (Spieltechnik)*
(S11) then names five rolls:

| DE | EN given by the source | Axis |
|---|---|---|
| **Doppelschlagwirbel** | (double-stroke roll) — "militärisch klingend" | ornament = `roll` / `bounced` |
| **Einzelschlagwirbel**, on timpani also **Paukenwirbel** | Single Stroke Roll | ornament — **no value** |
| **Presswirbel** / **geschlossener Wirbel** | Closed Roll, Buzz Roll | ornament = `buzz` |
| **Offener Wirbel** | Open Stroke Roll | ornament = `roll` |
| **Einhändiger Wirbel** | One handed Roll, **Gravity Roll**; also *Freehand Technique* after Johnny Rabb | ornament + technique — **no value** |

Definitions verbatim: open roll = "mit kontrollierten Doppelschlägen … nach dem 'Rebound'
die Energie des ersten Schlages in den zweiten Schlag führt"; closed roll = "mit **nicht
kontrollierten** Pressschlägen … der Schlegel auf das Fell gepresst"; one-handed roll = "keine
Abfolge rechter und linker Mehrfachschläge … nur mit einer Hand … Push Pull Technik …
einfacher ist es, **den Rand der Trommel zu Hilfe zu nehmen**".

**Mühle** is given by S11/S12 as the *preparatory exercise* for the double-stroke roll, and
by S01 as a synonym for *Doppelschlag*. The two sources disagree; recorded as a conflict in
§4.

### 2.11 German striking-position and damping doctrine (S07, official standard)

ISB Bayern *Bewertungskriterien Perkussion*:

- §*Trommeln*: "die **Schlagposition** auf dem Fell [wird] der Lautstärke angepasst:
  **Forte in der Fellmitte, Piano eher am Fellrand**. Dies gilt nur für Solo-Werke, beim
  Drum-Set wird die Snare-Drum grundsätzlich in der Mitte angespielt." Striking position is
  a *function of dynamic* in German solo snare practice, not an independent choice.
- "**Klangverfremdungen** (Rand, **Korpus**, Stock auf Stock etc.) werden, wenn gewünscht,
  im Notentext angezeigt." A named superordinate class for timbre-alienating strokes.
  `Korpus` = shell. English has no single word for the class.
- "Die Unterscheidung zwischen **geschlossenem/gepresstem** (closed/press roll) und
  **offenem Wirbel** (open roll) hängt von der Literatur und deren Herkunft (hier v. a.
  Europa oder USA) ab. Nicht immer ist erkennbar, welche Art des Wirbels ausgeführt werden
  soll." An official standard stating that the closed/open roll distinction is
  **notationally underdetermined** and resolved by repertoire provenance.
- Mallets: "Die Klangstäbe werden immer **in der Mitte** angespielt … Hier werden die
  alterierten Töne **am Rand des Klangstabs** angeschlagen", with **Gabelgriff** named for
  the four-mallet interval grip.
- "**Pedal- und Schlägeldämpfung**" on the vibraphone — two named, distinct damping
  mechanisms.
- "**Handsätze** (z. B. r-l-l-r)", dependent on **Aufstellung**: European (lowest timpano to
  the player's right) versus American (to the left).

### 2.11a Pre-MIDI German, 1911 (S42)

Haupt & Teuchert, *Musik-Instrumentenkunde in Wort und Bild*, section D
*Schlaginstrumente*. This is the pre-MIDI layer the brief asks for: it names physical
distinctions with no reference to any note number, and it is public domain.

**Timpani beater coverings, p. 166, verbatim:** "Zum Schlagen der Pauken werden Schlägel,
die mit **Flanell, Filz, Schwamm oder Kork** überzogen sind, verwendet." Flannel, felt,
**sponge** and **cork**. Sponge- and cork-headed beaters are standard 19th-century
orchestral implements and have **no KITWARP `implement` value**; the axis has felt, wood,
plastic, rubber and superball only.

**Snare-drum damping, p. 202, verbatim:** "Das Dämpfen wird dadurch erzielt, daß man beim
Schlagen entweder ein **Tuch auf das oberste Fell legt**, oder **die angezogenen Saiten**
oder auch **das ganze, straff angezogene Fell nachläßt**." Three distinct damping
mechanisms, named as alternatives:

| mechanism | KITWARP |
|---|---|
| a cloth laid on the batter head | `damping.towel` |
| slackening the snare wires | `mechanism.wires-off` — but *slackened*, not thrown off, which is a third state between wires-on and wires-off |
| **slackening the head itself** | **no value on any axis** |

The third is a real, historically standard technique — detuning the head to kill it — and
KITWARP cannot express it. It is neither damping (nothing touches the head) nor a
mechanism value that exists.

**Cymbal damping, p. 204, verbatim:** the plates are damped by being "nach dem Schlagen
schnell **an die Brust gedrückt**" — pressed to the chest. A named damping gesture; the
nearest KITWARP relation is `choke`, which `vocabulary/rules.json` excludes.

**Two snare drums, not one, p. 202.** S42 records that Strauss (*Der Rosenkavalier*) and
Bittner (*Der Musikant*) call for two: "Die erste wird mit **Militärtrommel** oder **hohe
Trommel** bezeichnet, während die zweite die Bezeichnung **tiefe** oder **große
Rührtrommel** — auch **Tamburo vecchio** — trägt", the difference being head tension and
shell depth. KITWARP has a single `snare` slug; German score practice distinguishes at
least two instruments and Italian gives the deeper one its own direction.

**Instrument names given in four languages, verbatim:**

| DE (S42) | IT | FR | EN |
|---|---|---|---|
| große Trommel (p. 200) | gran-tamburo, gran-cassa | grand-caisse | bass-drum |
| kleine Trommel, auch Militärtrommel (p. 201) | tamburo | tambour militaire | — |
| Becken, auch türkische Becken (p. 204) | **piatti oder cinelli** | cymbales | — |
| Tamtam (p. 204) | — | **beffroi** | — |

*Cinelli* is a third Italian word for cymbals beside *piatti* and *cimbali* (cf. §4.1), and
*beffroi* for the tam-tam is not in any modern source reached here — both are recorded as
historical variants, not as current usage.

**Tam-tam beater, p. 204:** "ein mit **Leder überzogener Holzklöppel**" — a
leather-covered wooden beater, corroborating the *Lederkopfschlägel* of S01 from a source
a century earlier.

### 2.11b Vibraphone and gong (S45)

| DE | gloss | Axis |
|---|---|---|
| Anschlagen | striking | technique = `hit` |
| Vibrato / **Senza vibrato** | motor on / off | mechanism — **no value** |
| Tremolo / Wirbel | tremolo | ornament |
| Triller | trills | ornament |
| Glissando | glissando | technique = `gliss` |
| **Nachklangglissando** | resonance glissando — glissando over a still-ringing bar | technique |
| Akkordspiel / **Akkordtremolo** | chord playing, chord tremolo | ornament |
| Kontrabassbogen | double-bass bow | implement — **no value** |
| **Dead stroke** | dead stroke — German uses the English term untranslated | technique = `dead` |
| Legato / Staccatospielweise | legato, staccato manner | none — articulation |
| **Dämpferpedal** vs **Dämpfung** | damper pedal vs damping generally | damping / mechanism |
| Secco | dry, short | damping |

Vibraphone mallet materials, verbatim: "Garn, Schnur, Hartgummi, **Rosenholz**,
**Messing**, **Ebonitholz**" — yarn, cord, hard rubber, rosewood, brass, ebonite.

Gong (S45), where German names the striking geometry differently from the cymbal:

| DE | gloss | Axis |
|---|---|---|
| **Buckel** | the gong's boss / central dome | site = `bell`, but physically a different thing from a cymbal's *Beckenkuppe* |
| Rand | rim | site = `edge` |
| **Anschlagpunkt** | striking point | position |
| Gestrichen | bowed | technique — no value |
| Gedämpft | damped | damping |

### 2.12 Organological German (S06, Hornbostel–Sachs 1914)

Class terms verbatim from the German original: **Idiophone**, **Aufschlagidiophone**
(111.2), **Aufschlagstäbe** (111.21), **Aufschlagspiele** (1112.2), **Aufschlaggefäße**
(11124), **Membranophone**. The German scheme distinguishes *Gegenschlag-* (two like bodies
struck together) from *Aufschlag-* (a body struck by a non-sonorous beater); English
translations render both under "percussion"/"concussion" and the distinction is routinely
lost. **The *Aufschlag-* branch is verified in S06; the *Gegenschlag-* branch is
UNVERIFIED** — the Würzburg PDF is the commentary text, not the full class list. S05 (MIMO's
SKOS edition of Hornbostel-Sachs) would settle it and was not walked.

### 2.13 French terms (S08, S10, S13, S19)

| FR | source | definition given | Axis |
|---|---|---|---|
| **roulement** | S08 | roll, "utilise la possibilité de rebond multiple de la baguette sur la peau" | ornament |
| **roulé** | S08 | single bounce | ornament |
| **cross stick**, **click** | S08 | "un coup frappé sur le cercle, la paume de la main reposant sur la peau, donne un son sec" | technique = `sidestick` |
| **rimshot** | S08 | "frapper la peau et le rebord en même temps" | technique = `rimshot` |
| **baguettes** | S08 | sticks | implement = `stick` |
| **balais** | S08 | brushes | implement = `brush` |
| **fagots** | S08 | bundled rods | implement = `rod` |
| **mains nues** | S08 | bare hands | implement = `hand` |
| **cercle** | S08 | the hoop | site = `rim` |
| **rebord** | S08 | the rim edge | site = `rim` |
| **peau**, **peau de frappe** | S08, S10 | head, batter head | site = `head` |
| **peau de résonance**, **peau inférieure** | S10 | resonant / bottom head | site — **no value** |
| **fût** | S10 | shell | site = `shell` |
| **timbre** | S10 | the snare wires themselves | mechanism |
| **déclencheur** | S10 | snare throw-off / strainer | mechanism |
| **mis en tension** | S10 | snares engaged | mechanism = `wires-on` |
| **charleston** | S13, S19 | hi-hat | instrument |
| **jouer ouvert** | S13 | play open | openness = `open` |
| **joué avec le pied** | S13 | played with the foot | limb, a layout slot |
| **sans timbre** | S02 | snares off | mechanism = `wires-off` |
| **voilé** | S02 | muffled, veiled | damping |
| **sur le bois** | S02 | on the wood | site = `shell` / `rim` |
| **mailloche** | S01 | bass-drum beater | implement |
| **étouffé** | S19 | muted | damping |
| **ouverte / fermée** | S16 | open / closed — the only two techniques Dorico's French docs name for unpitched percussion | openness |

#### French General MIDI percussion map (S19)

The complete French rendering of the GM channel-10 map, from a French notation vendor.
Key numbers added here from the standard GM assignment; S19 gives French note names on a
C1 = 36 convention.

| GM | FR (S19) | EN (GM) |
|---|---|---|
| 35 | Grosse caisse acoustique | Acoustic Bass Drum |
| 36 | Grosse caisse | Bass Drum 1 |
| 37 | **Baguette sur bord de fût** | Side Stick |
| 38 | Caisse claire acoustique | Acoustic Snare |
| 39 | Claquement de mains | Hand Clap |
| 40 | Caisse claire électrique | Electric Snare |
| 41 | Tom basse 2 | Low Floor Tom |
| 42 | Charleston fermée | Closed Hi-Hat |
| 43 | Tom basse 1 | High Floor Tom |
| 44 | Charleston au pied | Pedal Hi-Hat |
| 45 | Tom médium 2 | Low Tom |
| 46 | Charleston ouverte | Open Hi-Hat |
| 47 | Tom médium 1 | Low-Mid Tom |
| 48 | Tom aigu 2 | Hi-Mid Tom |
| 49 | Cymbale crash 1 | Crash Cymbal 1 |
| 50 | Tom aigu 1 | High Tom |
| 51 | Cymbale ride 1 | Ride Cymbal 1 |
| 52 | Cymbale chinoise | Chinese Cymbal |
| 53 | Cloche de ride | Ride Bell |
| 54 | Tambourin | Tambourine |
| 55 | Cymbale splash | Splash Cymbal |
| 56 | Cowbell | Cowbell |
| 57 | Cymbale crash 2 | Crash Cymbal 2 |
| 58 | Vibra-slap | Vibraslap |
| 59 | Cymbale ride 2 | Ride Cymbal 2 |
| 60/61 | Bongo aigu / grave | High / Low Bongo |
| 62/63/64 | Conga aigu étouffé / Conga aigu / Conga grave | Mute Hi / Open Hi / Low Conga |
| 65/66 | **Timbale aigüe / grave** | High / Low Timbale |
| 67/68 | Agogo aigu / grave | High / Low Agogo |
| 69 | Cabasa | Cabasa |
| 70 | Maracas | Maracas |
| 71/72 | Sifflet aigu court / Sifflet grave long | Short / Long Whistle |
| 73/74 | Guiro court / long | Short / Long Guiro |
| 75 | Claves | Claves |
| 76/77 | Woodblock aigu / grave | Hi / Low Wood Block |
| 78/79 | Cuica étouffé / Cuica | Mute / Open Cuica |
| 80/81 | Triangle étouffé / Triangle | Mute / Open Triangle |

Two things follow. **`Baguette sur bord de fût`** is the French GM name for the side stick,
and it names the *implement plus site* rather than the stroke: "stick on the edge of the
shell". And French names the toms by **register plus ordinal** (basse/médium/aigu × 1–2),
where English GM names them by *mounting* (floor/rack) plus register — six English names
against three French registers. Here English is the more granular tradition, in the one
place where it usually is not.

### 2.13a Pre-MIDI French, 1843 (S33, Berlioz)

The archive.org scan's OCR is poor — accents are mangled and words are broken — so every
term below is given as the legible reading and the surrounding sense, and **the exact
orthography should be confirmed against a clean edition before any of it is minted**. The
terms themselves are unambiguous.

*Les Timbales*, from line 10187 of the plain text:

> "On trouve souvent dans les anciens maîtres surtout cette indication: **Timbales voilées
> ou couvertes**. Elle signifie que la peau de l'instrument doit être couverte d'un
> **morceau de drap** dont l'effet est d'étouffer sa sonorité … **Les baguettes à tête
> d'éponge** sont encore préférables aux autres en pareil cas."

This is the origin of the *voilé* that VSL still glosses in 2.3, from 1843, and it settles
two things:

| FR (S33, 1843) | what it names | Axis |
|---|---|---|
| **timbales voilées**, **timbales couvertes** | the head covered with a cloth — the French *coperto* | damping = `towel` |
| **morceau de drap** | the cloth itself | damping |
| **baguettes à tête d'éponge** | sponge-headed timpani sticks | implement — **no value**; confirms the *Schwamm* of S42 (1911) from the source that established the practice |
| "frapper **avec les deux baguettes à la fois** ou **avec une seule baguette**" | a notated distinction between striking with both sticks together and with one | technique — cf. DE *Unisono-Schläge* (S01); no KITWARP value |

Cymbals, from line 10455:

> "**laissez vibrer** … avec ces mots: **étouffez le son**, ce que l'exécutant obtient en
> **rapprochant de sa poitrine les cymbales** aussitôt après les avoir frappées. On se sert
> quelquefois d'une **baguette de timbales à tête d'éponge**, ou d'un **tampon de grosse
> caisse** pour faire vibrer une **cymbale suspendue par sa courroie**; cela produit un
> frémissement métallique d'une assez longue durée."

| FR (S33) | what it names | Axis |
|---|---|---|
| **laissez vibrer** | let ring | damping = `none` |
| **étouffez le son** | damp the sound | damping |
| "rapprochant de sa poitrine les cymbales" | the chest-damping gesture | **no value** — and see below |
| **tampon (de grosse caisse)** | the bass-drum beater, a second French name beside *mailloche* | implement |
| **cymbale suspendue par sa courroie** | the suspended cymbal, named by its strap | instrument |

**The chest-damping gesture is named independently in both pre-MIDI traditions**: Berlioz
1843, "rapprochant de sa poitrine les cymbales", and Haupt & Teuchert 1911, "nach dem
Schlagen schnell an die Brust gedrückt" (§2.11a). Two sources, two languages, sixty-eight
years apart, naming the same physical act that KITWARP has no way to express — its nearest
relative is `choke`, which `vocabulary/rules.json` deliberately excludes as a relation on a
previously sounded event. That two independent traditions bothered to name it is the
strongest evidence in this dossier that the exclusion of `choke` leaves a real hole.

### 2.14 Italian terms beyond the snare (S03)

| IT | p. | gloss | Axis |
|---|---|---|---|
| **Rullo rovesciato** | 41 | "reversed roll" | ornament — **no value** |
| **Rullo al galoppo** | 42 | "gallop roll" | ornament — **no value** |
| **Rullo lungo il braccio** | 45 | roll executed along the arm (frame drum) | ornament + technique |
| **Rullo riz**; *Riz (rullo) con le unghie* | 501, 787, 815 | the *riz* roll of the daf tradition; with the fingernails | ornament + implement = `fingernail` |
| **Rullo con colpo di chiusura** | 916 | roll with a closing stroke — identical to DE *Abschlag* | ornament + technique |
| **Rullo coronato** | 918 | fermata roll | ornament |
| **Rullo in crescendo e diminuendo** | 918 | swell roll | ornament = `crescendo`/`swell` |
| **Rullo glissando** | 919 | glissando roll | ornament + `gliss` |
| **Cambio di note durante un rullo** | 919 | note change under a roll — identical to DE *Übergangswirbel* | ornament |
| **Rullo aperto** / **Rullo chiuso** | 525 | open / closed roll, defined by finger stroke count | ornament |
| **Acciaccatura semplice** (Flam) | 524 | single grace | ornament = `flam` |
| **Doppia acciaccatura** | 524 | double grace = drag | ornament = `drag` |
| **Tripla acciaccatura** ("rullo breve") | 500, 779 | triple grace = three-stroke ruff | ornament = `ruff` |
| **Quadrupla acciaccatura** ("rullo breve a 5 colpi") | 779 | quadruple grace | ornament |
| **Colpi sui nodi, al centro e all'estremità** | 379 | strokes on the *nodes*, at the centre, at the end | position — **no value for "node"** |
| **Suoni con l'asta (manico) delle mazzuole** al centro / sul bordo delle barre | 262 | struck with the mallet *shaft*, at the bar centre / on the bar edge | contact = `shank`; position |
| **Controcerchio** | 471 | counterhoop | site = `rim` |
| **Cerchi e controcerchi** | 754 | hoops and counterhoops | site = `rim`, `rim2` |
| **Cupola** | 77 | the bell/dome of a cymbal | site = `bell` |
| **Bordo** | 77, 473 | edge or rim | site = `edge` / `rim` |
| **Colpo Doum / Tak / Ka / Pa (slap) / Snap** | 519–523 | the darbuka stroke set, given twice: *stile turco* and *stile arabo* | technique |
| **Colpi forti con suono smorzato, tono chiuso** | 548 | strong strokes, damped sound, closed tone | technique + damping |
| **Colpi aperti, posizione morbida** | 546 | open strokes, soft position | technique = `open-tone` |
| **Tecnica Split-Hand, mano divisa** | 523 | split-hand technique | none, §3.2 |
| **Fischio sul bordo della carta** | 995 | whistle on the edge of a sheet of paper | technique, extended |
| Piatti sospesi con cupola cilindrica e **bordo all'insù** | 77 | upturned edge | instrument morphology |

### 2.15 Spanish hand-drum stroke taxonomy (S18)

*Percusión para Dummies*, table of contents. This is the only complete **Spanish** stroke
taxonomy reached. The book organises hand strokes into three superordinate classes, which
is itself the finding — English pedagogy names the strokes but rarely the classes.

| ES | p. | class | gloss | Axis |
|---|---|---|---|---|
| **Tonos abiertos** | 55 | class | open tones | — |
| Golpe básico abierto | 56 | open | basic open tone | technique = `open-tone` |
| **Golpe de pulgar** | 56 | open | thumb stroke | technique = `thumb` |
| Golpe seco abierto | 58 | open | dry open stroke | technique + damping |
| **Tono bajo** | 59 | open | bass tone | technique = `bass-tone` |
| **Golpe de aro** | 59 | open | rim stroke | site = `rim` |
| **Tonos tapados** | 60 | class | muted / covered tones | damping |
| Golpe tapado básico | 60 | muted | basic muted stroke | technique = `mute-stroke` |
| Golpe seco cerrado | 61 | muted | dry closed stroke | technique + damping |
| **Golpe de palma** | 62 | muted | palm stroke | technique = `slap` |
| **Golpe talón-punta** | 62 | muted | heel-toe stroke, as **one** named motion | technique — see §3.2 |
| **Golpes alternativos** | 63 | class | alternative strokes | — |
| **Golpe arrastrado** | 63 | alt. | dragged stroke | technique = `sweep` |
| **Nota pedal** | 63 | alt. | pedal note — hand pressed into the head to bend the pitch | technique — **no value** |
| **Chasquido** | 64 | alt. | snap / pop | technique — **no value** |
| Trinos | 65 | alt. | trills | ornament |
| Redoble de golpe simple / de golpe doble | 50 | — | single- / double-stroke roll | ornament |
| Golpes de baqueta | 41 | — | stick strokes | implement = `stick` |
| **Talón arriba o talón abajo** | 75 | — | heel-up or heel-down, on the bass-drum pedal | technique — **no value** |
| parche | 664 (line ref in extract) | — | head | site = `head` |
| casco | 664 | — | shell | site = `shell` |
| aro | 669 | — | hoop | site = `rim` |
| borde | 673 | — | edge | site = `edge` |

Definitions for pp. 55–65 are **not in the publisher's sample**; only the term list and its
page numbers are verified. Marked UNVERIFIED for the glosses, which are given here from the
literal Spanish and should be confirmed against the printed book.

---

## 3. Axis mapping

### 3.1 Terms that map cleanly onto an existing axis value

| Term | Lang | Axis | KITWARP value |
|---|---|---|---|
| Beckenkuppe / cupola / coupole | DE/IT/FR | site | `bell` |
| Beckenrand / bordo / rebord | DE/IT/FR | site | `edge` |
| Spannreifen / controcerchio / cercle / aro | DE/IT/FR/ES | site | `rim` |
| cerchi e controcerchi | IT | site | `rim` + `rim2` |
| auf dem Holz / sur le bois / Korpus / fût / casco | DE/FR/DE/FR/ES | site | `shell` |
| Fell / peau / pelle / parche | DE/FR/IT/ES | site | `head` |
| Fellmitte / al centro / Mitte | DE/IT/DE | position | `centre` |
| Fellrand / sul bordo | DE/IT | position | `perimeter` |
| ohne Saiten / sans timbre / senza corde | DE/FR/IT | mechanism | `wires-off` |
| mis en tension / con corde | FR/IT | mechanism | `wires-on` |
| coperto / voilé / étouffé / gedämpft / tapado | IT/FR/FR/DE/ES | damping | `damped` |
| secco | IT (used in DE and EN sources) | damping | `damped`, at zero delay |
| Randschlag / colpi a sparo / rimshot | DE/IT/FR | technique | `rimshot` |
| Rimclick / cross stick / click | DE/EN/FR | technique | `sidestick` |
| Baguette sur bord de fût | FR | technique | `sidestick` |
| Stock auf Stock / Schlägel auf Schlägel / colpi tra bacchette | DE/IT | technique | `stick-shot` |
| Golpe básico abierto / Colpi aperti | ES/IT | technique | `open-tone` |
| Tono bajo | ES | technique | `bass-tone` |
| Golpe de palma / Colpo Pa (slap) | ES/IT | technique | `slap` |
| Golpe tapado / Colpi … tono chiuso | ES/IT | technique | `mute-stroke` |
| Golpe de pulgar / rullo con il pollice / Daumenwirbel | ES/IT/DE | technique | `thumb` |
| Golpe arrastrado | ES | technique | `sweep` |
| Strisciato | IT/DE | technique | `scrape` (approximately) |
| Schüttelwirbel | DE | technique | `shake` |
| Daumenspitzen-Wirbel | DE | technique | `swirl` |
| Resonanzglissando / cambiamenti graduali di intonazione | DE/IT | technique | `gliss` |
| Presswirbel / rullo chiuso / rullo pressato / colpo pressato | DE/IT | ornament | `buzz` |
| Offener Wirbel / rullo aperto | DE/IT | ornament | `roll` or `bounced` |
| colpo doppio rimbalzato | IT | ornament | `bounced` |
| Einfacher Vorschlag / acciaccatura semplice | DE/IT | ornament | `flam` |
| Zweifacher Vorschlag / doppia acciaccatura | DE/IT | ornament | `drag` |
| Dreifacher Vorschlag / tripla acciaccatura | DE/IT | ornament | `ruff` |
| Rulli crescendo-diminuendo / rullo in crescendo | IT | ornament | `crescendo`, `swell` |
| ouverte / jouer ouvert / Charleston ouverte | FR | openness | `open` |
| fermée / Charleston fermée | FR | openness | `closed` |
| fagots / Ruten | FR/DE | implement | `rod` |
| balais / Besen / Stahlbesen / spazzole | FR/DE/IT | implement | `brush` |
| baguettes / Trommelstöcke / bacchette / baquetas | FR/DE/IT/ES | implement | `stick` |
| mailloche / Hartfilzschlägel | FR/DE | implement | `felt-beater` |
| Holzkopfschlägel | DE | implement | `wood-beater` |
| Superball | DE | implement | `superball` |
| Fingernagel / unghie | DE/IT | implement | `fingernail` |
| Asta / manico delle mazzuole | IT | contact | `shank` |

### 3.2 Terms that fit NO axis

The most valuable part of this bucket. Grouped by what kind of thing they name.

**(a) Properties of a note *sequence*, not of a note**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Handsatz / Handsätze**; *scelta delle mani per l'esecuzione di un passo* | DE, IT | S07; S03 p. 471 | which hand plays which note (r-l-l-r). KITWARP carries `limb` on the layout slot but has no way to say *a sequence of limbs*. |
| **Paradiddle**; *Mühle*; **Tecnica Split-Hand / mano divisa** | DE, IT | S01, S11; S03 p. 523 | named sticking patterns spanning several attacks. `ornament` carries an attack count but no hand assignment. |
| **Aufstellung** (European vs American timpani layout) | DE | S07 | which drum stands where relative to the player; determines the notated Handsatz. |
| **"scomposizione del rullo"** | IT | S17 §1.1 | resolving a written roll into its constituent strokes — a reading operation over a figure. |

**(b) Grip and stroke *form*, which change timbre without changing implement or site**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Presa delle bacchette**; *Schlägelhaltung*; presa a bacchette parallele vs presa tradizionale; presa Burton / Musser / Stevens; **Gabelgriff** | IT, DE | S03 p. 465; S17 §1.1, §2.3; S07 | grip. Neither implement, nor contact, nor technique — but audibly different. |
| **colpo "accademico"**, **colpo "a pistone"**, **"Full"**, **"Tap"**, colpo libero | IT | S17 §1.1 d | stroke *height and trajectory*. Closest KITWARP axis is `dynamic`, but `normal/ghost/soft/hard/accent` names loudness, not stroke shape; a Tap and a ghost note are not the same thing. |
| **tipi di colpo: doppio verticale, singolo indipendente, singolo alternato, doppio laterale** | IT | S17 §2.3 b | the four four-mallet stroke types. |

**(c) Damping and sizzle *mechanisms*, where KITWARP names only the result**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Pedaldämpfung vs Schlägeldämpfung**; *smorzamenti ausiliari ("Dampening")* | DE, IT | S07; S17 §2.4 | pedal-damped vs mallet-damped. `damping` names the audible result; `mechanism` has only kit-drum values. |
| **Nieten / Kugelkette / Stahlnadel** | DE | S01 | rivets, ball chain, steel needle — three distinct sizzle attachments. KITWARP bakes one of them into `instrument.sizzle-ride` and has no `mechanism` value for the others. |
| **air-lock** | IT trade | S03 p. 104 | the hi-hat's air-release feature, which changes the closed sound. |

**(d) Implement structure, which KITWARP flattens to one slug**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Kopf / Bezug / Stiel / Form** of a beater | DE | S01 | head material, covering, shaft length, head shape — four independent parameters. `implement` cannot express "hard felt head, cloth-covered, 30 cm shaft, disc-shaped". |
| **Groß-, Mittel-, Kleinkopf** | DE | S07 | mallet head *size*, independent of material. |
| **Lederkopfschlägel** | DE | S01 | leather-headed beater. No `implement` value; not felt, not wood, not rubber. |
| **Kralle** | DE | S01 | a dedicated tam-tam scraper. `technique.scrape` names the act, nothing names the tool. |
| **Triangelstab / Triangelschlägel** used on the tam-tam | DE | S01 | a metal beater; `implement` has no metal-beater value. |

**(e) Rolls whose *internal shape* or *body part* is named**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Rullo rovesciato**, **Rullo al galoppo** | IT | S03 pp. 41, 42 | reversed and gallop rolls — a roll's internal rhythmic shape. |
| **Rullo lungo il braccio** | IT | S03 p. 45 | roll produced along the arm. |
| **Rullo o tremolo ad altalena con le dita**, **fingerrolls** | IT | S03 pp. 786, 787 | see-saw finger roll. |
| **Einhändiger Wirbel / Gravity Roll / Freehand** | DE | S11 | a roll produced by one hand against the rim. Not `roll`, not `buzz`, not `bounced`. |
| **Einzelschlagwirbel / Paukenwirbel / rullo a colpi singoli / Redoble de golpe simple** | DE, IT, ES | S11, S17, S18 | the single-stroke roll, named in all three languages. KITWARP has `roll`, `buzz`, `bounced` — none of which is specifically the single-stroke roll. |
| **rullo militare** (legato / slegato) | IT | S17 §1.5, §1.6 | a named roll kind distinct from both open and pressed, with a slurred and an unslurred form. |
| **acciaccature … singole e rimbalzate** | IT | S17 §1.6 c | a grace-note figure's count and its *rebounded or not* status as two independent parameters. `ornament` conflates them. |

**(f) Events that span two instrument slots or reference an earlier event**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Übergangswirbel**; *cambio di note durante un rullo* | DE, IT | S01; S03 p. 919 | a roll that migrates between drums. One event, two slots. |
| **Doppelwirbel** | DE | S01 | one roll sounding two timpani at once. |
| **Kreuzschlag** (einfach / doppelt); *incroci, allontanamenti* | DE, IT | S01; S17 §4.1 a | crossed-hands strokes between two drums — the *path between* slots. |
| **Abschlag**; *rullo con colpo di chiusura* | DE, IT | S01; S03 p. 916 | the stroke that terminates a roll. Defined by its position in a figure, not by its own physics. This is the same class of problem as `choke`, which `vocabulary/rules.json` deliberately excludes as "a relation on a previously sounded event". |
| **Watergong** | DE | S01 | a gong lowered into water while ringing — an after-attack pitch modulation. Same class as `choke`. |
| **Nota pedal** | ES | S18 p. 63 | the hand pressed into a hand-drum head to bend pitch after the attack. Same class. |
| **Rullo coronato** | IT | S03 p. 918 | a fermata roll — duration defined by the conductor, not the term. |

**(g) Excitation that is not a strike**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Gestrichen / con l'arco** | DE, IT | S01; S03 p. 115 | bowed. `technique` has no non-percussive excitation value; `scrape` is a different physical act. |
| **Breiter Schlag** | DE | S01 | the crash-pair stroke where the plates *shear* across each other rather than being struck. |
| **Strisciato** | IT, DE | S01, S03 | one plate rubbed across the other, centre → edge. Directional, and a pair action. |
| **Vibrato** (cymbal pair) | DE | S01 | the plates waved after the strike. |
| **Unisono-Schläge** | DE | S01 | two beaters striking as one — a multiplicity of implements, not an ornament. |
| **Chasquido** | ES | S18 p. 64 | finger snap / pop on a hand drum. |
| **Fischio sul bordo della carta** | IT | S03 p. 995 | whistling on the edge of a sheet of paper. |

**(h) Position and category terms with no home**

| Term | Lang | Source | What it names |
|---|---|---|---|
| **Schlagfleck** | DE | S01 | the *named* ideal striking spot, "one hand's width from the edge" (timpani) / "3–4 cm from the rim" (tambourine). `position` has `centre / halfway / offset / perimeter`; the Schlagfleck is a specific, instrument-dependent, named point and is the German default. |
| **Colpi sui nodi** | IT | S03 p. 379 | strokes on the *nodal points* of a bar or plate. `position` is radial; a node is acoustic. |
| **Zone di percussione** | IT | S03 pp. 111, 474 | "percussion zones" — the Italian superordinate term for what KITWARP splits into `site` + `position`. |
| **Klangverfremdung** | DE | S07 | a superordinate class over all timbre-alienating strokes (rim, shell, stick-on-stick). A category *over* techniques. |
| **peau de résonance / Resonanzfell** | FR, DE | S10, S09 | the bottom head as a named surface. `site` has `head` and `underside`, but FR and DE treat batter and resonant head as two *named heads*, not head vs underside. |
| **Golpe talón-punta**; **Talón arriba / talón abajo** | ES | S18 pp. 62, 75 | heel-toe as one named motion, and heel-up vs heel-down as a *pedal posture*. KITWARP has `heel` and `toe` as separate technique values and nothing for either the combined motion or the posture. |
| **allenatore / Allenatori di gomma** | IT | S17, S03 p. 482 | the practice pad, treated by an official syllabus as an instrument distinct from the tamburo. |

---

## 4. Conflicts and false friends

### 4.1 One word, different things

| Word | Lang | Meaning A | Meaning B | Locator |
|---|---|---|---|---|
| **timbre** | FR | the snare wires; *sans timbre* = snares off, *tambour à timbre* = snare drum | in EN, tone colour | S02, S10, S03 p. 2827 index |
| **timbale** | FR | the orchestral timpano (MIMO 2887) | *timbale aigüe/grave* = the Latin-American timbales (GM 65/66) | S04; S19 |
| **Tambourin** | FR | tambourine, *tambour de basque* | **tambourin de Provence**, a long two-headed drum with **no jingles** — a separate MIMO concept (2745) and a separate Facchin head-word | S03 index; S04 |
| **Crash cymbals** | EN in DE/FR/IT sources | in Facchin's index, *Crash cymbals*, *Cymbales choquées*, *HandBecken*, *2 Beckenteller* all redirect to **piatti a mano (in coppia)** — the clashed *pair* | in kit English, `crash` is a single suspended cymbal | S03 index |
| **Cimbali** vs **Piatti** | IT | *cimbali* = small paired cymbals (MIMO 2451) | *piatti* = orchestral cymbal pair (MIMO 2471). English says "cymbals" for both; German "Becken" and French "Cymbales" also collapse them | S04 |
| **Wirbel** | DE | a roll | the tuning peg of a string instrument | S11 |
| **Vorschlag** | DE | a grace-note figure, counted: *einfach / zweifach / dreifach / vierfach* | EN "grace note" is not systematically counted; it becomes flam/drag/ruff, three unrelated words | S01 |
| **Randschlag** vs **am Rand / Fellrand** | DE | *Randschlag* = the rim shot, a stroke | *Fellrand* = near the rim, a position | S01, S07 |
| **rullo / tremolo / trillo** | IT | Facchin's own index uses all three for the same act: "Tremolo o rullo" (p. 135), "Trillo (rullo)" (p. 719) | in EN notation, roll, tremolo and trill are three different things | S03 pp. 113, 135, 705, 719 |
| **coperto** | IT, used untranslated in DE and EN scores | "covered" = a cloth laid on the head, i.e. muffled | frequently misread as "the instrument is covered up / not used" | S01, S02 |
| **charleston** | FR, IT | the hi-hat | in EN, a dance and a rhythm | S03 p. 102; S13; S19 |
| **Mühle** | DE | S11/S12: the *preparatory exercise* for the double-stroke roll | S01: a *synonym* for Doppelschlag. The two sources disagree; S12 is the more authoritative (it cites Peinkofer/Tannigel) | S01 vs S11, S12 |
| **secco** | IT, used in DE and EN sources | struck and damped immediately | not the same as *coperto*, which damps before the stroke | S01 |

### 4.2 Different words, same thing

| Concept | DE | FR | IT | ES | EN |
|---|---|---|---|---|---|
| snares disengaged | mit entspannten Schnarrsaiten / Teppich ab | sans timbre | senza corde | — | snares off |
| muffled | Coperto / gedämpft | voilé / étouffé | coperto | tapado | muffled / muted |
| damped at once | Secco | — | secco | seco | choked, dry |
| roll terminated by a stroke | Abschlag | — | rullo con colpo di chiusura | — | (no single term) |
| roll moving between drums | Übergangswirbel | — | cambio di note durante un rullo | — | (no single term) |
| pressed / buzz roll | Presswirbel, Druckwirbel, geschlossener Wirbel | — | rullo pressato, rullo chiuso | — | press roll, closed roll, buzz roll |
| double-stroke roll | Doppelschlagwirbel, offener Wirbel | — | rullo militare (approx.) | redoble de golpe doble | open roll, two-stroke roll, legitimate roll |
| single-stroke roll | Einzelschlagwirbel, Paukenwirbel | — | rullo a colpi singoli | redoble de golpe simple | single-stroke roll |
| thumb roll | Daumen(spitzen)-Wirbel | — | rullo con il pollice | golpe de pulgar | thumb roll |
| shake roll | Schüttelwirbel | — | — | — | shake roll |
| stroke on the shell | auf dem Holz, Korpus | sur le bois | colpi sul bordo di legno | — | on the wood, on the shell |
| side stick | Rimclick | baguette sur bord de fût, cross stick, click | — | — | side stick, cross stick, rim click |
| bell / dome of a cymbal | Beckenkuppe | coupole | cupola | — | bell, dome, cup |
| the striking sweet spot | Schlagfleck | — | — | — | (no single term) |

### 4.3 A significant negative

**German-language MIDI practice does not translate the GM drum map.** The German Wikipedia
*General MIDI* article (S20) lists the channel-10 assignment with the **English** names
verbatim — "35 Bass Drum 2, 36 Bass Drum 1, 37 Side Stick, 38 Snare Drum 1 …". French
practice does translate it (S19). So a German-language KITWARP alias set would have two
disjoint registers: precise German score terminology for acoustic technique, and untranslated
English for anything MIDI-adjacent. Aliases must be sourced accordingly, not
machine-translated across the boundary.

---

## 5. Gaps against vocabulary v0.1

v0.1 = 155 terms, drum kit only, as summarised in `.agents/round2/BRIEF.md` and confirmed
against `vocabulary/axes.json` at the head of `claude/kitwarp-pivot-vocab-data-w56ld3`.

### 5.1 Missing axis values, ordered by how well evidenced they are

| Axis | Proposed value | Evidence | Note |
|---|---|---|---|
| implement | `metal-beater` | Triangelstab / Triangelschlägel used on tam-tam and cymbal (S01) | v0.1 has felt/wood/plastic/rubber but no metal. |
| implement | `leather-beater` | Lederkopfschlägel (S01) | Standard orchestral bass-drum beater. |
| implement | `fist` | listed in the BRIEF's axis sketch but **absent from `vocabulary/axes.json`** | The BRIEF lists `fist` under implement; the shipped axes.json does not. Discrepancy, not a finding — flagged for the reconciliation pass. |
| implement | `scraper` | Kralle (S01); Râcloir / Schrapinstrument / raspa / rascador (S04) | `technique.scrape` exists with no tool to do it. |
| implement | `sponge-beater`, `cork-beater` | Schwamm, Kork (S42 p. 166, 1911); **baguettes à tête d'éponge** (S33, 1843) | Standard 19th-century timpani beaters, named independently in French in 1843 and in German in 1911. |
| technique | `chest-damp` (or admit `choke` as a relation) | "rapprochant de sa poitrine les cymbales" (S33, 1843); "an die Brust gedrückt" (S42 p. 204, 1911) | Named in both pre-MIDI traditions. See §2.13a. |
| implement | `brass-beater`, `rosewood-beater`, `ebonite-beater` | Messing, Rosenholz, Ebonitholz (S45, vibraphone) | For the mallet-percussion family when it is minted. |
| mechanism | `head-slackened` | "das ganze, straff angezogene Fell nachläßt" (S42 p. 202) | Damping by detuning the head. Not `damping` — nothing touches the head. No axis has it. |
| mechanism | `wires-slack` | "die angezogenen Saiten … nachläßt" (S42 p. 202) | A third snare state between `wires-on` and `wires-off`. |
| mechanism | `motor-on` / `motor-off` | Vibrato / Senza vibrato (S45, vibraphone) | The vibraphone motor is a mechanism, and `senza vibrato` is a standard score direction. |
| implement | `bow` | Gestrichen (S01); arco di contrabbasso (S03 p. 115) | Collides with `site.bow`; a name must be chosen carefully. |
| technique | `bowed` | Gestrichen / con l'arco (S01, S03) | Not a strike; `scrape` is not a substitute. |
| technique | `shear` or `slide` | Breiter Schlag, Strisciato (S01, S03) | The clashed-pair stroke. |
| technique | `snap` | Chasquido (S18 p. 64); Colpo Snap (S03 pp. 521, 523) | Named in two independent traditions. |
| technique | `pedal-note` | Nota pedal (S18 p. 63) | Pitch bend by hand pressure. |
| technique | `heel-toe` | Golpe talón-punta (S18 p. 62) | v0.1 has `heel` and `toe` separately; the combined motion is a different event. |
| ornament | `single-stroke` | Einzelschlagwirbel / Paukenwirbel (S11); rullo a colpi singoli (S17); redoble de golpe simple (S18) | v0.1's `roll` is unqualified; three languages name the single-stroke roll explicitly. |
| ornament | `gravity` (one-handed roll) | Einhändiger Wirbel / Gravity Roll / Freehand (S11) | |
| ornament | `cut-off` | Abschlag (S01); rullo con colpo di chiusura (S03 p. 916) | Or handle as a relation, like `choke`. |
| ornament | `four-stroke-ruff` | Vierfacher Vorschlag (S01); quadrupla acciaccatura (S03 p. 779, S17 §1.6 c) | v0.1 stops at `ruff` (three strokes). Italian goes to *quintuple*. |
| position | `sweet-spot` | Schlagfleck (S01, twice, with two different measurements) | The German *default* striking place, distinct from centre and from perimeter. |
| position | `node` | Colpi sui nodi (S03 p. 379) | For bars and plates, when the percussion families are minted. |
| site | `resonant-head` | peau de résonance (S10); Resonanzfell (S09) | v0.1's `underside` is a geometric term; FR and DE name the head, not the side. |
| damping | (mechanism split) | Pedaldämpfung vs Schlägeldämpfung (S07); smorzamenti ausiliari (S17 §2.4) | Either new `mechanism` values or a second damping axis. |
| mechanism | `rivets` / `chain` / `needle` | Nieten / Kugelkette / Stahlnadel (S01) | v0.1 encodes one of these as `instrument.sizzle-ride`, which is an identity where a mechanism belongs. |
| dynamic | stroke-height values | colpo "a pistone", "Full", "Tap", colpo accademico (S17 §1.1 d) | `normal/ghost/soft/hard/accent` names loudness; these name trajectory. A `stroke-form` axis may be the honest answer. |

### 5.2 Things v0.1 names in a way the non-English sources contradict

- **`instrument.crash`.** In every non-English orchestral source reached, the crash *is* the
  clashed pair: Facchin's index sends *Crash cymbals*, *Cymbales choquées*, *HandBecken* and
  *2 Beckenteller* all to *piatti a mano in coppia* (S03). KITWARP's `crash` is the kit's
  single suspended cymbal, which those sources call *piatti sospesi* / *Becken auf Ständer* /
  *cymbales suspendues*. When the orchestral family is minted, `crash` will be ambiguous
  across traditions. Since identifiers are forever
  (`docs/adr/0003-identifiers-and-registry.md`), the orchestral pair needs its own slug from
  the start rather than an overload of `crash`.
- **`instrument.sizzle-ride`** bakes a removable mechanism (rivets) into an instrument
  identity, and German names three different such mechanisms (S01).
- **`ornament.roll`** is unqualified where German names five roll kinds (S11) and Italian at
  least eight (S03, S17). Any alias mapping "Wirbel" → `roll` loses which roll.
- **`position`** is purely radial. The German default position is a *named point*
  (Schlagfleck), and the German official standard makes position a function of dynamic
  (S07). A radial scalar cannot express "forte in der Fellmitte, piano am Fellrand" as a
  rule.
- **`site.rim` / `site.rim2`.** Italian distinguishes *cerchio* from *controcerchio* (S03
  p. 754) and, separately, the *wooden* rim from the *metal* rim (S03 p. 473). v0.1's `rim`
  and `rim2` are ordinals with no stated semantics; the Italian sources give them one.
- **`instrument.snare` is one slug where the German orchestral tradition has two.** S42
  p. 202 records the pair *Militärtrommel / hohe Trommel* against *tiefe (große)
  Rührtrommel / Tamburo vecchio*, distinguished by head tension and shell depth and scored
  separately by Strauss. VSL keeps them apart to this day as two instrument pages,
  `snare-drum` and `field-drum` (S01). KITWARP's `snare` covers both, and `voicing` cannot
  carry the difference because it is an instrument difference, not a production style.
- **Tom naming.** French GM names toms by register + ordinal (basse/médium/aigu × 1–2, S19),
  English GM by mounting + register (floor/rack). KITWARP's `instance` ordinal ("toms high
  to low in pitch") matches the French convention and not the English one — which is
  probably right, but it means English GM aliases will not map one-to-one.

### 5.3 What v0.1 gets confirmed

Confirmed independently by non-English sources: `sidestick` (FR *cross stick / click* with
the same palm-on-head definition, S08), `rimshot` (FR and IT both define it as head + rim
simultaneously, S08, S03 p. 471), `stick-shot` (DE *Stock auf Stock*, *Schlägel auf
Schlägel*, S01, S07), `buzz` (DE *Presswirbel* defined as *uncontrolled* pressed strokes,
S11), `open-tone` / `bass-tone` / `slap` / `mute-stroke` / `thumb` (the ES hand-drum
taxonomy, S18, maps onto them one for one), `wires-off` (three languages, S02),
`superball` (DE, S01), `crescendo` / `swell` (IT *rulli crescendo-diminuendo*, S03 p. 469).

---

## 6. Self-critique (round C)

### 6.1 The two catalogues the bucket named

- **Vienna Symphonic Library instrumentology: reached, and it is the single best source in
  this bucket.** The decisive discovery is that the same page exists at
  `vsl.co.at/de/academy/...` and `vsl.co.at/academy/...`, so the German and English editions
  gloss each other line by line, and the English edition additionally carries FR and IT
  score directions (*sur le bois*, *sans timbre*, *senza corde*, *voilé*). Ten instrument
  pages were mined (§2.3–2.9, §2.11b). **Not mined: tubular bells, plate bells, xylophone,
  marimba, glockenspiel, celesta** — six more pages of the same density. They bear on the
  orchestral and mallet families, which are reserved and unminted, so finishing the set is
  the right next step only once those families are being minted.
- **IRCAM: partly blocked, and where reachable the answer is negative.** Two separate
  facts. First, `instruments.ircam.fr` is **denied by this environment's egress policy** —
  it answers 502 on CONNECT, verified independently by the supervisor and by a status probe
  here (`000`). It cannot be reached from this environment at all and should not be retried.
  Second, and independent of the block: the IRCAM host that *is* reachable,
  `brahms.ircam.fr`, serves a
  single-page-application shell that returns HTTP 200 for *any* `/definition/<slug>` URL, so
  a status check proves nothing. Fetching the actual content shows that
  `modes-de-jeu-de-la-trompette` is real, while `modes-de-jeu-des-percussions`,
  `modes-de-jeu-de-la-caisse-claire` and `modes-de-jeu-du-vibraphone` are empty placeholders.
  IRCAM's *modes de jeu* pages cover wind and brass, not percussion. Its sample-database
  lineage confirms this from the other side: OrchideaSOL (S15), the direct descendant of the
  SOL corpus recorded at IRCAM in 1996–98, has 89 playing-technique classes and **no
  percussion instrument at all**. The reconciliation pass should treat "the IRCAM
  instrumental-technology database" as **blocked at one host and, at the reachable host,
  not existing for percussion** — not as merely unreached. Chasing it from a different
  network would still be worth one hour, because `instruments.ircam.fr` was never seen and
  its contents are therefore unknown; but the OrchideaSOL evidence says the percussion is
  unlikely to be there.

### 6.2 The single most authoritative source not obtained

**Karl Peinkofer and Fritz Tannigel, *Handbuch des Schlagzeugs. Praxis und Technik*, Schott
1981 (ISBN 978-3-7957-2641-6)** — S21. It is the reference work of German percussion
practice, it is what German Wikipedia cites for the Einzelschlag/Doppelschlag/Pressschlag
taxonomy (pp. 84–85), and it exists in an authorised English translation (*Handbook of
Percussion Instruments*), which makes it a **ready-made bilingual concordance for exactly
this bucket's purpose**. It is in copyright and no legitimate full text was reachable. If
the project can obtain one copy of each edition, a page-aligned German/English technique
concordance falls out of it directly, and it would settle every DE term this dossier marks
UNVERIFIED. This is the source the reconciliation pass should chase.

### 6.3 Other named gaps

- **Facchin (S03) was reached only as a publisher's extract.** What that extract contains is
  the complete table of contents and the four-language *Indice degli strumenti* — which is
  why this dossier can cite Italian terms with page numbers but can quote a verbatim Italian
  *definition* for almost none of them. The terms and their locators are solid; the glosses
  are mine unless quoted. The full two volumes would convert roughly forty Italian entries
  from "named at page N" to "defined as follows".
- **The Spanish taxonomy (S18) is TOC-only** for the same reason. Pages 55–65 of *Percusión
  para Dummies* would confirm or correct nine stroke glosses.
- **Berlioz 1843 (S33) was reached, but only through a bad scan.** The archive.org OCR of
  `grandtraitdins1843berl` mangles accents and breaks words, so §2.13a reports the terms
  with confidence but not the orthography. A clean edition — the 1855 reprint, the
  Berlioz–Strauss *Instrumentationslehre* (archive.org `instrumentations01berl`, 1905,
  which is the same text in German and therefore a ready-made FR/DE concordance), or the
  1970 Paris edition `traitdinstrument0000berl` — would fix that cheaply. The
  Berlioz–Strauss German edition is the more valuable of the three for this bucket's
  purpose and was identified but not opened.
- **Kurt Stone 1980 (S27)** has an accessible full PDF and was not opened. Its appendices
  carry multilingual instrument tables that would cross-check §2.1 and §2.2 independently.
- **MuseScore's German and Italian percussion handbooks (S22, S23) both return 403.** They
  are the obvious source for translated *note-map* names, and the same content is in the
  MuseScore source tree, reachable by `git clone --depth 1`. Note that MuseScore is GPL, so
  under `docs/adr/0004-provenance-and-licensing.md` its data is **rederive-only** — a reason
  to prefer it as a cross-check rather than a source of record.
- **The *Gegenschlag-* branch of Hornbostel–Sachs is UNVERIFIED** (§2.12). MIMO publishes
  Hornbostel-Sachs as SKOS (S05) with German labels and a REST API that is known to work;
  walking that vocabulary would settle it in a few calls.
- **No Austrian or Swiss source was reached**, and Basel drumming (*Basler Trommel*) has its
  own notation and its own vocabulary — Facchin gives it a dedicated chapter (p. 728) and
  S11 names it as a tradition with region-specific symbols. It is a distinct German-language
  tradition this bucket did not touch.

### 6.4 Method warning for the reconciliation pass

Eight of this bucket's terminology rows come from a small model's reading of a fetched page
rather than from a verbatim quotation (the VSL pages, which were read via WebFetch summaries
rather than parsed). They are consistent with each other and with the German page/English
page cross-check, but a row like "Mühle = double stroke" turned out to conflict with the two
Wikipedia sources on exactly that point (§4.1). Before any of these terms is minted as an
alias, the VSL pages should be fetched as raw HTML and the German strings taken verbatim.
