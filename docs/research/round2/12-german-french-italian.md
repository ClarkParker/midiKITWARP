# Round 2, bucket 12 — Non-English score and pedagogical terminology

German, French, Italian, Spanish percussion terminology from score practice,
pedagogical literature, organological thesauri and vendor instrumentology.

Two deliverables, per the bucket brief: a **synonym concordance** across the languages,
and — more valuable — **every technique that only a non-English tradition names**, because
those are the places where the English vocabulary has collapsed a distinction.

Status: IN PROGRESS. Sections marked TODO are not yet filled.

Conventions used below:

- `DE` German, `FR` French, `IT` Italian, `ES` Spanish, `EN` English.
- Every row carries a locator. Anything not verified against a named source is marked
  `UNVERIFIED` and is not presented as a finding.
- Axis names are the KITWARP axes from `.agents/round2/BRIEF.md`: instrument, site,
  position, contact, technique, ornament, openness, damping, mechanism, implement,
  dynamic, timbre, voicing.

---

## 1. Candidate source register (round A)

Authority levels: **A** primary standard, treatise or museum thesaurus; **B** professional
vendor or institutional reference; **C** encyclopaedic or pedagogical secondary; **D**
aggregation.

| # | Title | Author / body | Year | Type | Locator | Lang | Auth | Reached |
|---|---|---|---|---|---|---|---|---|
| S01 | Instrumentology / Academy — Percussion, German edition | Vienna Symphonic Library | n.d. (live) | vendor instrumentology | https://www.vsl.co.at/de/academy/percussion | DE (+EN/FR/IT glosses) | B | YES |
| S02 | Instrumentology / Academy — Percussion, English edition | Vienna Symphonic Library | n.d. (live) | vendor instrumentology | https://www.vsl.co.at/academy/percussion | EN (+DE/FR/IT glosses) | B | YES |
| S03 | *Le percussioni — storia e tecnica esecutiva nella musica classica, contemporanea, etnica e d'avanguardia* | Guido Facchin | Zecchini ed. | treatise (extract PDF: full index + sample chapters, 2 vols) | https://www.zecchini.cloud/estratti/591.pdf | IT | A | YES (extract) |
| S04 | MIMO Thesaurus of musical instrument names (SKOS/Skosmos) | Musical Instrument Museums Online | live | museum thesaurus | https://vocabulary.mimo-international.com/InstrumentsKeywords/en/ ; REST at `/rest/v1/InstrumentsKeywords/` | 13 languages incl. DE/FR/IT/ES | A | YES |
| S05 | MIMO Hornbostel-Sachs classification (SKOS) | Musical Instrument Museums Online | live | museum thesaurus | https://vocabulary.mimo-international.com/HornbostelAndSachs/en/ | multi | A | partially |
| S06 | *Systematik der Musikinstrumente. Ein Versuch* (German original text + commentary) | E. M. von Hornbostel, C. Sachs | 1914 | organological standard | https://www.musikwissenschaft.uni-wuerzburg.de/fileadmin/04070000/Instrumentensammlung/Materialien_Instrumente/Hornbostel_SysTex.pdf | DE | A | YES |
| S07 | *Bewertungskriterien und Literaturliste Perkussion* (Abiturprüfung Musik, G9) | Staatsinstitut für Schulqualität und Bildungsforschung (ISB), Bayern | n.d. | official examination standard | https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Faecher/Musik/Literaturlisten_G9/Perkussion.pdf | DE | A | YES |
| S08 | *Caisse claire — Modes de jeu* | Encyclopædia Universalis | live | encyclopaedia | https://www.universalis.fr/encyclopedie/caisse-claire-en-bref/4-modes-de-jeu/ | FR | C | YES |
| S09 | *Kleine Trommel* | Wikipedia DE | live | encyclopaedia | https://de.wikipedia.org/wiki/Kleine_Trommel | DE | C | YES |
| S10 | *Caisse claire* | Wikipedia FR | live | encyclopaedia | https://fr.wikipedia.org/wiki/Caisse_claire | FR | C | YES |
| S11 | *Wirbel (Spieltechnik)* | Wikipedia DE | live | encyclopaedia | https://de.wikipedia.org/wiki/Wirbel_(Spieltechnik) | DE | C | partially (via search snippet) |
| S12 | *Doppelschlag (Trommel)* | Wikipedia DE | live | encyclopaedia | https://de.wikipedia.org/wiki/Doppelschlag_(Trommel) | DE | C | partially (via search snippet) |
| S13 | Notation (percussion, French drum-set conventions) | Percunivers | live | pedagogical | https://www.percunivers.com/notation.php | FR | C | YES |
| S14 | IRCAM *Brahms* resource database — `modes de jeu` definition pages | IRCAM | live | research institute database | https://brahms.ircam.fr/fr/definition/modes-de-jeu-de-la-trompette | FR | A | YES for trumpet; **NO percussion pages exist** (see §6) |
| S15 | *OrchideaSOL: a dataset of extended instrumental techniques for computer-aided orchestration* | Cella, Ghisi, Lostanlen, Lévy, Fineberg, Maresz | 2020 | dataset paper (IRCAM SOL lineage) | arXiv:2007.00763, https://arxiv.org/pdf/2007.00763 | EN | A | YES — **no percussion in the technique set** (see §6) |
| S16 | Dorico notation reference — *Techniques de jeu des instruments de percussions non chromatiques* | Steinberg | v3 archive | vendor documentation | https://archive.steinberg.help/dorico_pro/v3/fr/dorico/topics/notation_reference/notation_reference_unpitched_percussion/notation_reference_unpitched_percussion_playing_techniques_c.html | FR | B | YES — thin, only *ouverte* / *fermée* named |
| S17 | *Notazione percussioni* (handbook, Italian) | MuseScore | live | notation software documentation | https://musescore.org/it/manuale/notazione-percussioni | IT | B | TODO |
| S18 | *Schlagwerk Notation* (handbook, German) | MuseScore | live | notation software documentation | https://musescore.org/de/handbuch/schlagwerk-notation | DE | B | TODO |
| S19 | *Notazione comune per le percussioni* / *Rulli di tamburo* | LilyPond notation reference (IT) | v2.21/2.25 | notation software documentation | https://lilypond.org/doc/v2.25/Documentation/notation/drum-rolls.it.html | IT | B | TODO |
| S20 | Conservatorio di Musica "Jacopo Tomadini" Udine — programma preaccademico percussioni | Conservatorio di Udine | n.d. | conservatory syllabus | http://www.conservatorio.udine.it/pdf/preaccademici/percussioni.pdf | IT | A | TODO |
| S21 | *Percussioni — L'arte della pratica e i rudimenti* | Marchingband.it | live | pedagogical | http://www.marchingband.it/content/percussioni-larte-della-pratica-e-i-rudimenti-i-parte | IT | C | TODO |
| S22 | *Percusión para Dummies* (Spanish edition, sample PDF) | Planeta de Libros | n.d. | pedagogical | https://proassetspdlcom.cdnstatics2.com/usuaris/libros_contenido/arxius/38/37843_Percusion_para_dummies.pdf | ES | C | TODO |
| S23 | *Técnicas extendidas de percusión I* | Emusicarte (blog) | live | pedagogical | http://blog.emusicarte.es/tecnicas-extendidas-de-percusion-1/ | ES | C | TODO |
| S24 | *Music Notation in the Twentieth Century: A Practical Guidebook* | Kurt Stone | 1980 | notation standard | full PDF: https://hugoribeiro.com.br/biblioteca-digital/Stone-Music_Notation_20th_Century.pdf ; also archive.org `musicnotationint0000ston_h3s0` | EN with multilingual instrument tables | A | TODO |
| S25 | *Music Notation: A Manual of Modern Practice* | Gardner Read | 1969 | notation standard | archive.org / pdfcoffee mirror | EN | A | TODO |
| S26 | *Spielanweisungen* (score-direction glossary) | Musiktreff.info | live | pedagogical glossary | https://www.musiktreff.info/spieltechniken/4956-spielanweisungen.html | DE | C | TODO |
| S27 | *Musiklehre Online: Spielanweisungen* | musicademy.de | live | pedagogical glossary | http://www.musicademy.de/index.php?id=2591 | DE | C | TODO |
| S28 | *Spielanweisungen* (engraving-house notes) | Vadon Music Preparation | live | engraving practice | http://www.vadonmusicpreparation.com/tag/spielanweisungen/ | DE | C | YES — strings only, no percussion |
| S29 | *Klassifikation der Musikinstrumente nach Hornbostel/Sachs* | Universität Würzburg, Institut für Musikforschung | live | university course material | https://www.musikwissenschaft.uni-wuerzburg.de/musikinstrumente/organologie/systematiken/hornbostelsachs/ | DE | A | TODO |
| S30 | *Batterie : les caisses* | marcdedouvan.com | live | pedagogical | http://www.marcdedouvan.com/instru.php?instru=caisses | FR | C | TODO |
| S31 | *L'écriture musicale de la batterie et des percussions* | Arpège Musique (Pizzicato) | live | vendor documentation | http://www.arpegemusique.com/percussion.htm | FR | B | TODO |
| S32 | *Grand traité d'instrumentation et d'orchestration modernes* | Hector Berlioz | 1844 | treatise, pre-MIDI primary | IMSLP | FR | A | TODO |
| S33 | Musique contemporaine — modes de jeu (performer's own catalogue) | Camille Émaille | live | performer catalogue | https://camilleemaille.com/projets/musique-contemporaine/ | FR | C | TODO |
| S34 | *Schlagzeugbegriffe* | d-drums Schlagzeugschule Berlin | live | pedagogical glossary | https://schlagzeug-berlin.de/schlagzeugbegriffe-in-den-ring-geworfen/ | DE | C | TODO |
| S35 | *Wirbel* | Stabführer.de (Spielmannszug/marching tradition) | live | trade/tradition glossary | https://stabfuehrer.de/wiki/Wirbel | DE | C | TODO |

Reached at time of this commit: S01–S16 in whole or part.

---

## 2. Extracted terminology (round B)

### 2.1 Instrument names — multilingual concordance (MIMO thesaurus, S04)

Generated from the MIMO Skosmos REST API, `skos:prefLabel` per language. The final column
is the MIMO concept id under `http://www.mimo-db.eu/InstrumentsKeywords/`.

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
| Tambourine | Tamburin | Tambourin (alt: Tambour de basque) | Tamburello | Pandereta | 2746 |
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

Note on 2451 vs 2471: MIMO holds two distinct concepts whose English label is identical
("Cymbals") and whose German and French labels are identical ("Becken", "Cymbales"), but
whose **Italian labels differ**: *Cimbali* vs *Piatti*. See §4.

### 2.2 Snare drum / kleine Trommel — playing techniques

Source S01/S02, the same VSL page in its German and English editions, read side by side.
Locator: `vsl.co.at/de/academy/percussion/snare-drum` and `vsl.co.at/academy/percussion/snare-drum`,
section "Spieltechniken" / "Playing Techniques".

| DE (S01) | EN (S02) | FR (S02) | IT (S02) | Axis |
|---|---|---|---|---|
| Einzelschläge | Single stroke | — | — | ornament (attack count 1) |
| Doppelschlag; also **Papa-Mama-Streich**, **Mühle** | Double stroke ("mammy-daddy beats") | — | — | ornament |
| Repetitionen | Repetitions | — | — | ornament |
| Vorschläge | Grace notes | — | — | ornament |
| Einfacher Vorschlag | Flam | — | — | ornament (1 grace) |
| Zweifacher Vorschlag | Drag | — | — | ornament (2 grace) |
| Dreifacher Vorschlag | Three stroke ruff | — | — | ornament (3 grace) |
| Vierfacher Vorschlag | Four stroke ruff | — | — | ornament (4 grace) |
| Paradiddle | Paradiddle | — | — | (sticking — fits no axis, see §3.2) |
| Pralltriller | Tied trills | — | — | ornament |
| Wirbel | Rolls | — | — | ornament |
| Druckwirbel / Presswirbel / geschlossener Wirbel | Press roll / closed roll | — | — | ornament (buzz) |
| Offener Wirbel; Zweischlagwirbel | Open roll / two-stroke roll / "legitimate roll" | — | — | ornament (bounced/roll) |
| — | One-stroke roll | — | — | ornament |
| Rim shot / **Randschlag** | Rim shot | — | — | technique |
| Stick on stick | Stick on stick | — | — | technique (stick-shot) |
| Rimclick | Rim click | — | — | technique (sidestick) |
| Mit Stahlbesen | Wire brushes | — | — | implement |
| **Auf dem Holz** | On the wood | **sur le bois** | — | site (shell / wooden hoop) |
| Mit entspannten Schnarrsaiten | With released snares / snares off | **sans timbre** | **senza corde** | mechanism (wires-off) |
| Coperto | Muffled | **voilé** | *coperto* (the term is itself Italian) | damping |

Facchin (S03) index, snare drum chapter "CASSA CHIARA, TAMBURO DA CONCERTO, TAMBURO
PICCOLO", pp. 463–482, adds the Italian names for the same field:

| IT (S03) | page | gloss | Axis |
|---|---|---|---|
| Corde del timbro | 463 | the snare wires themselves | mechanism |
| Smorzamento, sordina | 464 | damping / mute | damping |
| Presa delle bacchette | 465 | stick grip | (grip — fits no axis, §3.2) |
| Tecnica del rullo / Tipi di rullo | 466–467 | roll technique / roll types | ornament |
| Rulli forte-piano | 469 | fp rolls | ornament + dynamic |
| Rulli crescendo-diminuendo | 469 | swell rolls | ornament (crescendo/swell) |
| Abbellimenti | 469 | ornaments (grace-note figures) | ornament |
| Scelta delle mani per l'esecuzione di un passo | 471 | choice of hands = sticking | (§3.2) |
| **Colpi a sparo (rim shots) tra il controcerchio di metallo e la pelle** | 471 | literally "shot strokes", between the metal **counterhoop** and the head | technique = rimshot; site = rim |
| **Colpi sul bordo di legno e di metallo e tra bacchette** | 473 | strokes on the *wooden* rim, on the *metal* rim, and stick against stick | site (rim distinguished by material) |
| **Zone di percussione** e altre tecniche per effetti timbrici e ritmici | 474 | "percussion zones" | site + position |
| Metodi di percussione ed effetti vari | 477 | striking methods and effects | technique |
| Cambiamenti graduali di intonazione | 478 | gradual pitch change | technique (gliss) |
| Bacchette e mazzuole | 478 | sticks and mallets | implement |
| Spazzole di filo metallico | 478 | wire brushes | implement |
| Percussione con le dita | 479 | finger strokes | implement (finger) |
| Percussione con le mani | 480 | hand strokes | implement (hand) |
| Allenatori di gomma | 482 | rubber practice pads | (equipment — no axis) |

### 2.3 Timpani / Pauken

Source S01, `vsl.co.at/de/academy/percussion/timpani`, section "Spieltechniken",
cross-read with S07 (ISB Bayern examination standard).

| DE | EN gloss given by the source | Axis |
|---|---|---|
| Einzelschläge | Single strokes | ornament |
| Coperto | Covered / muffled | damping |
| Secco | Dry single stroke | damping (immediately damped) |
| Anschlag mit der Hand | Hand strike | implement (hand) |
| Repetitionen | Repetitions | ornament |
| **Einfacher Kreuzschlag** | Simple cross-beat | technique (crossed hands between drums) |
| **Doppelter Kreuzschlag** | Double cross-beat | technique |
| Vorschläge | Grace notes | ornament |
| Mehrfachschläge | Multiple strokes | ornament |
| Paradiddle | Paradiddle | (§3.2) |
| Wirbel | Roll / tremolo | ornament |
| **Doppelwirbel** | Double roll (roll on two drums at once) | ornament + instrument multiplicity |
| **Übergangswirbel** | Transition roll (roll that moves from one drum to another) | ornament |
| **Abschlag** | Cut-off stroke (the stroke that *terminates* a roll) | technique |
| **Resonanzglissando** | Resonance glissando (pedal change while the head still rings) | technique (gliss) |
| **Wirbelglissando** | Glissando roll (pedal change under a sustained roll) | ornament + technique |

Striking positions named on the same page (`Schlagstelle`):

| DE | definition given | Axis |
|---|---|---|
| **Schlagfleck** | the ideal striking spot, "one hand's width from the edge" | position |
| Fellmitte | centre of the head | position = centre |
| Fellrand | edge of the head | position = perimeter |

Mallets: Weichfilz, Hartfilz, Flanell, Holz (S01); ISB Bayern (S07, §"Pauken") adds head
*size* as an independent parameter: "Groß-, Mittel-, Kleinkopf, Filz-, Flanell- oder
Holzschlägel" — i.e. head material and head size are two separate axes in German practice.

S07 also states a technique rule English notation does not carry: for timpani,
"Wirbel werden weder gedrückt noch gepresst, die Ausführung erfolgt immer 'Hand zu Hand' =
rechts-links-rechts-links" — the timpani roll is by definition single-stroke; press rolls
are excluded on this instrument.

### 2.4 Bass drum / Große Trommel

Source S01, `vsl.co.at/de/academy/percussion/bass-drum`.

| DE | EN gloss | FR gloss where given | Axis |
|---|---|---|---|
| Einzelschläge | Single strokes | — | ornament |
| Fellrand | Rim (as striking place) | — | position = perimeter |
| Secco | Single stroke, immediately damped | — | damping |
| Coperto | Damped strokes | — | damping |
| **Con la mano** | Hand strokes (fingers) | — | implement (hand/finger) |
| **Unisono-Schläge** | Unison strokes (two beaters together) | — | technique |
| Repetitionen | Repetitions | — | ornament |
| Wirbel | Rolls | — | ornament |
| **Schlägel auf Schlägel** | Beater on beater | — | technique (stick-shot analogue) |
| Stahlbesen | Wire brushes | — | implement |
| Fußmaschine | Bass pedal | — | mechanism |
| Großer Trommelschlägel | Bass drum mallet | **mailloche** | implement |
| Hartfilzschlägel | Hard felt mallet | — | implement = felt-beater |
| Lederkopfschlägel | Leather-headed mallet | mailloche | implement — **no KITWARP value** |
| Holzkopfschlägel | Wood-headed mallet | — | implement = wood-beater |

### 2.5 Cymbals — Becken / piatti / cymbales

Source S01, `vsl.co.at/de/academy/percussion/cymbals` (crash pair) and
`/suspended-cymbal` (hängendes Becken).

Crash pair (`cymbals`):

| DE | gloss | Axis |
|---|---|---|
| Einzelschläge | single strokes | ornament |
| **Breiter Schlag** | broad stroke (the two plates slide across each other) | technique |
| Secco | struck then damped at once, dry metallic | damping |
| Wirbel | rolls | ornament |
| **An der großen Trommel befestigt** | cymbal mounted on the bass drum, played by one player | mechanism/layout |
| **Strisciato** (also *strisciati*) | rubbing one plate from centre to edge across the inner face of the other | technique = scrape/sweep |
| Vibrato | circular waving of the plates after the strike | technique |
| Repetitionen | repetitions | ornament |
| Rand | edge (the plates are struck edge-to-edge) | site = edge |
| Mitte | centre (held there by the strap, not struck) | position = centre |

Suspended cymbal (`suspended-cymbal`):

| DE | gloss | Axis |
|---|---|---|
| Einzelschlag | single stroke | ornament |
| Secco | dry, immediately damped | damping |
| Wirbel | roll | ornament |
| **Gestrichen** | bowed (cello or double-bass bow) | technique — **no KITWARP value** |
| **Nieten / Kugelkette / Stahlnadel** | rivets / ball chain / steel needle — three distinct sizzle devices | mechanism/timbre — **no KITWARP value** |
| Besen | wire brushes | implement |
| Repetitionen | repetitions | ornament |
| **Beckenkuppe** | dome stroke | site = bell |
| **Beckenrand** | rim / edge stroke | site = edge |
| Hand / Fingernagel | hand, fingernail | implement (hand, fingernail) |

Beater material list for the suspended cymbal, verbatim: "Garn, Schnur, Stoff, umwickelt,
Gummi, Paukenfilz, Holz"; implements named: Paukenschlägel, garnumwickelte Schlägel,
Holzschlägel, Trommelstöcke, Triangelschlägel, Cello- oder Kontrabassbogen, Besen.

Facchin (S03), suspended-cymbal chapter "PIATTI SOSPESI TURCHI", pp. 108–115:

| IT | page | gloss | Axis |
|---|---|---|---|
| **Zone di percussione** | 111 | percussion zones on the plate | site + position |
| Tecniche per suonare il piatto sospeso | 112 | suspended-cymbal techniques | technique |
| Smorzamento dei piatti sospesi | 113 | damping of suspended cymbals | damping |
| Il tremolo o rullo e la sua tecnica | 113 | tremolo/roll | ornament |
| Piatti sospesi suonati con le spazzole | 114 | played with brushes | implement |
| Piatti sospesi appoggiati su una membrana di timpano e suonati con l'arco di contrabbasso | 115 | cymbal laid on a timpano head and bowed | technique + mechanism |
| Piatti sospesi con cupola cilindrica e bordo all'insù | 77 | cymbals with cylindrical **cupola** (bell) and upturned **bordo** (edge) | site = bell, edge |

Hi-hat, Facchin index "PIATTI A PEDALE, HI-HAT, CHARLESTON", pp. 102–106: *lo hi-hat
moderno* 103, *l'air-lock* 104, *regolazione dello hi-hat* 104, *tecniche di esecuzione*
105, *altri tipi di hi-hat* 105, *notazione* 106. Note the Italian and French trade name
for the hi-hat is **charleston** (S03 p. 102; S13 for FR).

### 2.6 Tambourine / Tamburin / tamburello / tambour de basque

Source S01, `vsl.co.at/de/academy/percussion/tambourine`. This page names **three distinct
rolls by their production mechanism**, which English collapses into "roll":

| DE | gloss | Axis |
|---|---|---|
| **Schüttelwirbel** | shake roll — the instrument is shaken, the jingles sound | ornament + technique = shake |
| **Daumen(spitzen)-Wirbel** | thumb-tip roll — wetted thumb dragged around the head | ornament + technique = swirl/friction |
| **Schlägel-Wirbel** | stick roll — struck with sticks | ornament + implement |

Striking positions on the same page: **Schlagfleck** (3–4 cm from the rim), **Fellrand**,
**Fellmitte**. Implements: Mittelfinger, Daumen, Fingerknöchel, Handballen, **Ellenbogen**,
**Knie**, kleine Trommelstöcke, Hart-/Weichfilzschlägel, Becken-/Xylophonschlägel,
Triangelstäbe, Holzschlägel.

Facchin (S03) confirms the same tripartition in Italian and adds a fourth: *Il rullo con il
pollice* 446 (thumb roll), *Rullo con le mani* 456, *Rullo breve e continuato (fingerrolls)*
786, *Rullo o tremolo ad altalena con le dita* 787 ("see-saw" finger roll).

### 2.7 Tam-tam and gong

Source S01, `vsl.co.at/de/academy/percussion/tam-tam`.

| DE | gloss | Axis |
|---|---|---|
| Einzelschläge | single strokes | ornament |
| Secco | dry, damped | damping |
| Wirbel | roll | ornament |
| Repetitionen | repetitions | ornament |
| Triangelstab | triangle beater used on the tam-tam | implement |
| **Superball** | rubber ball, dragged to excite friction tone | implement = superball |
| **Kralle** | "claw" — a scraper drawn across the surface | implement — **no KITWARP value** |
| **Watergong** | the gong is lowered into water while sounding, bending the pitch | technique — **no KITWARP value** |
| Gestrichen | bowed | technique — **no KITWARP value** |
| Gedämpft | damped | damping |

Beater anatomy named as three separate parts: **Kopf** (head; Hartfilz, Holz, Metall,
6–15 cm), **Bezug** (cover; Filz, schwerer Stoff), **Stiel** (handle, 28–35 cm), plus
**Form** (Scheibenförmig, rund, rechteckig). German therefore names beater *head material*,
*covering*, *shaft* and *head shape* as four independent parameters where the KITWARP
`implement` axis has a single flat slug.

### 2.8 Rührtrommel / field drum

Source S01, `vsl.co.at/de/academy/percussion/field-drum` (German page title
*Wirbeltrommel*). Same technique set as the snare drum, plus the confirmation that
**Papa-Mama-Streich** is the German trade name for the double-stroke, and **Randschlag**
for the rim shot.

### 2.9 German striking-position and roll doctrine (official standard, S07)

ISB Bayern *Bewertungskriterien Perkussion*, section "Trommeln":

- "die Schlagposition auf dem Fell [wird] der Lautstärke angepasst: **Forte in der
  Fellmitte, Piano eher am Fellrand**" — striking position is a *function of dynamic*, not
  an independent choice, in German solo snare practice; on the drum set the snare is struck
  in the centre by default.
- "**Klangverfremdungen** (Rand, **Korpus**, Stock auf Stock etc.)" — a named superordinate
  category for "timbral alienation" strokes. `Korpus` = shell. There is no English single
  word for this class.
- "Die Unterscheidung zwischen **geschlossenem/gepresstem** (closed/press roll) und
  **offenem Wirbel** (open roll) hängt von der Literatur und deren Herkunft (hier v. a.
  Europa oder USA) ab" — the source states explicitly that the closed/open roll distinction
  is *notationally underdetermined* and resolved by repertoire provenance.
- Mallet instruments: "Die Klangstäbe werden immer in der Mitte angespielt… Hier werden die
  alterierten Töne **am Rand des Klangstabs** angeschlagen" — bar centre vs bar edge is a
  named position distinction, with **Gabelgriff** ("fork grip") named for the four-mallet
  interval grip.
- "**Pedal- und Schlägeldämpfung**" for the vibraphone — pedal damping and mallet damping
  are two named, distinct damping mechanisms. English "damping" collapses them.
- "**Handsätze** (z. B. r-l-l-r)" — sticking, named as a first-class notated parameter,
  and dependent on **Aufstellung** (European: lowest timpano to the player's right;
  American: to the left).

### 2.10 Organological German (S06, Hornbostel–Sachs 1914)

German class terms verbatim from the 1914 systematics text: **Idiophone**,
**Aufschlagidiophone** (111.2), **Aufschlagstäbe** (111.21), **Aufschlagspiele** (1112.2),
**Aufschlaggefäße** (11124), **Membranophone**. The 1914 German scheme distinguishes
*Gegenschlag-* (two like bodies struck together) from *Aufschlag-* (a body struck by a
non-sonorous beater); English translations render both as "percussion" or "concussion" and
the distinction is routinely lost. Verified in S06 for the *Aufschlag-* branch;
the *Gegenschlag-* branch is **UNVERIFIED** in this extract — the Würzburg PDF is the
commentary text, not the complete class list.

### 2.11 French terms (S08, S13)

| FR | source | gloss / definition given | Axis |
|---|---|---|---|
| **roulement** | S08 | roll, "utilise la possibilité de rebond multiple de la baguette sur la peau" | ornament |
| **roulé** | S08 | single bounce | ornament |
| **cross stick** / **click** | S08 | "un coup frappé sur le cercle, la paume de la main reposant sur la peau, donne un son sec" | technique = sidestick |
| **rimshot** | S08 | "frapper la peau et le rebord en même temps" | technique = rimshot |
| **baguettes** | S08 | sticks | implement = stick |
| **balais** | S08 | brushes | implement = brush |
| **fagots** | S08 | bundled rods | implement = rod |
| **mains nues** | S08 | bare hands | implement = hand |
| **cercle** | S08 | the hoop | site = rim |
| **rebord** | S08 | the rim edge | site = rim |
| **peau** | S08/S10 | head | site = head |
| **peau de frappe** | S10 | batter head | site = head |
| **peau de résonance** / **peau inférieure** | S10 | resonant/bottom head | site — **no KITWARP value** (there is no bottom-head site) |
| **fût** | S10 | shell | site = shell |
| **timbre** | S10 | the snare wires | mechanism |
| **déclencheur** | S10 | snare throw-off / strainer | mechanism |
| **charleston** | S13 | hi-hat | instrument |
| **grosse caisse** | S13 | bass drum | instrument |
| **cymbale ride / crash** | S13 | ride / crash | instrument |
| **jouer ouvert** | S13 | play open (hi-hat) | openness = open |
| **joué avec le pied** | S13 | played with the foot | limb (layout slot, not an axis) |
| **sans timbre** | S02 | snares off | mechanism = wires-off |
| **voilé** | S02 | muffled / veiled | damping |
| **sur le bois** | S02 | on the wood | site = shell/rim |
| **mailloche** | S01 | bass-drum beater | implement |
| **ouverte / fermée** | S16 | open / closed (hi-hat), the only two techniques Dorico's French docs name | openness |

### 2.12 Italian terms beyond the snare (S03)

| IT | page | gloss | Axis |
|---|---|---|---|
| **Rullo rovesciato** | 41 | "reversed roll" | ornament — **no KITWARP value** |
| **Rullo al galoppo** | 42 | "gallop roll" | ornament — **no KITWARP value** |
| **Rullo lungo il braccio** | 45 | roll executed along the arm (frame drum) | ornament + technique |
| **Rullo riz** | 501, 787, 815 | the *riz* roll (Persian/daf tradition; *Riz con le unghie*, with the fingernails, 815) | ornament + implement = fingernail |
| **Rullo con colpo di chiusura** | 916 | roll with a closing stroke | ornament + technique (= DE *Abschlag*) |
| **Rullo coronato** | 918 | fermata roll | ornament |
| **Rullo in crescendo e diminuendo** | 918 | swell roll | ornament = crescendo/swell |
| **Rullo glissando** | 919 | glissando roll | ornament + technique |
| **Cambio di note durante un rullo** | 919 | note change under a roll (= DE *Übergangswirbel*) | ornament |
| **Rullo aperto** / **Rullo chiuso** | 525 | open / closed roll, defined by finger stroke count | ornament |
| **Acciaccatura semplice** (Flam) | 524 | single grace | ornament |
| **Doppia acciaccatura** | 524 | double grace (= drag) | ornament |
| **Tripla acciaccatura** ("rullo breve") | 500, 779 | triple grace (= three-stroke ruff) | ornament |
| **Quadrupla acciaccatura** ("rullo breve a 5 colpi") | 779 | quadruple grace | ornament |
| **Colpi sui nodi, al centro e all'estremità** | 379 | strokes on the *nodes*, at the centre and at the end (bars/plates) | position — **no KITWARP value for "node"** |
| **Suoni con l'asta (manico) delle mazzuole** al centro / sul bordo delle barre | 262 | struck with the *shaft* of the mallet, at the bar centre / on the bar edge | contact = shank; position |
| **Controcerchio** | 471 | counterhoop | site = rim |
| **Cerchio** | 754 | hoop | site = rim |
| **Cupola** | 77 | the bell/dome of a cymbal | site = bell |
| **Bordo** | 77, 473 | edge / rim | site = edge or rim |
| **Colpo Doum / Tak / Ka / Pa (slap) / Snap** | 519–523 | the darbuka stroke set, given separately for *stile turco* and *stile arabo* | technique |
| **Colpi forti con suono smorzato, tono chiuso** | 548 | strong strokes, damped sound, closed tone | technique + damping |
| **Colpi aperti, posizione morbida** | 546 | open strokes, soft position | technique = open-tone |
| **Tecnica Split-Hand, mano divisa** | 523 | split-hand technique | (§3.2) |
| **Fischio sul bordo della carta** | 995 | whistle on the edge of the paper | technique (extended) |

---

## 3. Axis mapping

### 3.1 Terms that map cleanly

Mapped inline in the tables of §2, in the "Axis" column. Summary of the non-obvious ones:

| Term | Language | Axis | KITWARP value |
|---|---|---|---|
| Beckenkuppe / cupola / coupole | DE/IT/FR | site | `bell` |
| Beckenrand / bordo / bord | DE/IT/FR | site | `edge` |
| Controcerchio / cercle / Spannreifen | IT/FR/DE | site | `rim` |
| auf dem Holz / sur le bois / Korpus | DE/FR/DE | site | `shell` |
| Fellmitte / al centro | DE/IT | position | `centre` |
| Fellrand / sul bordo | DE/IT | position | `perimeter` |
| Schlagfleck | DE | position | between `halfway` and `perimeter` — no exact value |
| ohne Saiten / sans timbre / senza corde | DE/FR/IT | mechanism | `wires-off` |
| coperto / voilé / gedämpft | IT/FR/DE | damping | `damped` |
| secco | IT (used in DE and EN sources) | damping | `damped` at zero delay |
| Randschlag / colpi a sparo / rimshot | DE/IT/FR | technique | `rimshot` |
| Rimclick / cross stick / click | DE/EN/FR | technique | `sidestick` |
| Stock auf Stock / Schlägel auf Schlägel | DE | technique | `stick-shot` |
| Presswirbel / rullo chiuso | DE/IT | ornament | `buzz` |
| Offener Wirbel / rullo aperto | DE/IT | ornament | `roll` or `bounced` |
| Einfacher/Zweifacher/Dreifacher Vorschlag; acciaccatura semplice/doppia/tripla | DE/IT | ornament | `flam` / `drag` / `ruff` |
| fagots / Ruten | FR/DE | implement | `rod` |
| mailloche | FR | implement | `felt-beater` (approximately) |
| Superball | DE | implement | `superball` |

### 3.2 Terms that fit NO axis

These are the most valuable findings, per the brief.

| Term | Language | Source | What it names | Why no axis fits |
|---|---|---|---|---|
| **Handsatz / Handsätze**, *scelta delle mani*, *sticking* | DE, IT | S07, S03 p.471 | which hand plays which note (r-l-l-r) | KITWARP carries `limb` on the layout slot, but not a *sequence* of limbs. Sticking is a property of a note *series*, not of a note. |
| **Paradiddle**, *Mühle*, *Split-Hand / mano divisa* | DE, IT | S01, S03 p.523 | named sticking patterns | Same: a pattern over several attacks. `ornament` carries an attack count but not a hand assignment. |
| **Presa delle bacchette**, *Schlägelhaltung*, *Gabelgriff* | IT, DE | S03 p.465, S07 | grip (matched, traditional, four-mallet fork grip) | Grip changes timbre and articulation but is neither implement nor contact nor technique. |
| **Aufstellung** (European vs American timpani layout) | DE | S07 | which drum is where relative to the player | Layout, not term. KITWARP puts `instance` on the layout slot but has no handedness/orientation convention. |
| **Klangverfremdung** | DE | S07 | superordinate class for all timbre-alienating strokes (rim, shell, stick-on-stick) | A *category over* techniques, not a technique. |
| **Gestrichen / bowed / con l'arco** | DE, IT | S01, S03 p.115 | the instrument is bowed, not struck | `technique` has no non-percussive excitation value. `scrape` is not the same physical act. |
| **Watergong** | DE | S01 | gong lowered into water while ringing | An after-the-attack pitch modulation. Closest relative in KITWARP is `choke`, which the vocabulary deliberately excludes as "a relation on a previously sounded event". Same class of problem. |
| **Kralle** (tam-tam claw/scraper) | DE | S01 | a dedicated scraping implement | `implement` has no scraper value; `technique.scrape` names the act but not the tool. |
| **Nieten / Kugelkette / Stahlnadel** | DE | S01 | three distinct sizzle attachments | `instrument.sizzle-ride` bakes one attachment into an instrument identity. There is no `mechanism` value for "rivets fitted" vs "chain laid on" vs "needle". |
| **Bezug / Kopf / Stiel / Form** of a beater | DE | S01 | covering, head material, shaft, head shape as four independent beater parameters | `implement` is one flat slug; it cannot express "hard felt head, cloth-covered, 30 cm shaft, disc-shaped". |
| **Groß-, Mittel-, Kleinkopf** | DE | S07 | mallet head *size* independent of material | Same. |
| **Pedaldämpfung vs Schlägeldämpfung** | DE | S07 | pedal-damped vs mallet-damped | `damping` names the result, not the mechanism; `mechanism` has only kit-drum values. |
| **Colpi sui nodi** | IT | S03 p.379 | strokes on the *nodal points* of a bar or plate | `position` is radial (centre/halfway/offset/perimeter). A node is an acoustic, not a radial, location. |
| **peau de résonance / Resonanzfell** | FR, DE | S10, S09 | the bottom head, as a striking surface | `site` has `head`, `underside`, but the FR/DE sources treat batter head and resonant head as two *named heads*, not as head vs underside of one drum. |
| **Rullo rovesciato**, **Rullo al galoppo**, **Rullo lungo il braccio** | IT | S03 pp.41, 42, 45 | reversed, gallop and along-the-arm rolls | `ornament` has `roll`, `buzz`, `bounced` — no way to name a roll's *internal rhythmic shape* or the body part that produces it. |
| **Übergangswirbel / cambio di note durante un rullo** | DE, IT | S01, S03 p.919 | a roll that migrates between instruments | A single event that spans two instrument slots. KITWARP terms are per-slot. |
| **Abschlag / rullo con colpo di chiusura** | DE, IT | S01, S03 p.916 | the terminating stroke of a roll | A stroke defined by its position in a figure, not by its own physics. |
| **Doppelwirbel** | DE | S01 | one roll sounding two timpani at once | Two instruments, one term. |
| **Kreuzschlag** (einfach/doppelt) | DE | S01 | crossed-hands stroke between two drums | Describes the *path between* two slots. |
| **Breiter Schlag** | DE | S01 | the crash-pair stroke where plates slide across each other | Not `hit`; the plates are not struck but sheared. |
| **Strisciato** | IT/DE | S01, S03 | one plate rubbed across the other, centre to edge | `technique.scrape` is the nearest, but the source treats it as a *cymbal-pair* action with a direction (centre → edge). |
| **Unisono-Schläge** | DE | S01 | two beaters striking as one | A multiplicity of implements, not an ornament. |
| **air-lock** (hi-hat) | IT trade | S03 p.104 | the hi-hat's air-release feature | Hardware, affects the closed sound; no axis. |
| **Allenatori di gomma** | IT | S03 p.482 | rubber practice pads | Equipment, no axis. |

---

## 4. Conflicts and false friends

TODO — partially drafted:

| Word | Language | Meaning A | Meaning B | Locator |
|---|---|---|---|---|
| **timbre** | FR | the snare wires (`sans timbre` = snares off) | in EN, tone colour | S02, S10 |
| **Cimbali** vs **Piatti** | IT | *cimbali*: small paired cymbals (MIMO 2451) | *piatti*: orchestral cymbal pair (MIMO 2471) — English says "cymbals" for both | S04 |
| **Tamburin** (DE) vs **tambourin** (FR) | DE/FR | DE *Tamburin* = tambourine (jingled frame drum) | FR *tambourin* also = *tambourin de Provence*, a long two-headed drum with **no jingles** (MIMO 2745 is a separate concept from 2746) | S04 |
| **Becken** | DE | cymbals | also, in other contexts, a basin | S04 |
| **Wirbel** | DE | a roll | also the tuning peg of a string instrument | S01, general |
| **Vorschlag** | DE | a grace note of any count; "zweifacher Vorschlag" = drag | EN "grace note" is not counted by number in the same systematic way | S01 |
| **Randschlag** | DE | rim shot (stick tip on head + shaft on hoop) | but "am Rand" / "Fellrand" = striking *near the rim*, a position, not a rim shot | S01, S07 |
| **coperto** | IT (used in DE and EN scores) | covered/muffled — a cloth on the head | often mistranslated as "covered" meaning the drum is put away | S01, S02 |
| **charleston** | FR/IT | hi-hat | in EN, a dance and a rhythm | S03 p.102, S13 |
| **rullo** vs **tremolo** vs **trillo** | IT | Facchin's index uses all three for the same act ("Tremolo o rullo", "Trillo (rullo)") | EN "roll", "tremolo" and "trill" are three different things in EN notation | S03 pp.113, 135, 705, 719 |

---

## 5. Gaps against vocabulary v0.1

TODO.

---

## 6. Self-critique (round C)

TODO.
