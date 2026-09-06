# Round 2, bucket 11 — Acoustics and timbre

Status: complete. Everything below is quoted or transcribed from the source named in the
row of the register in section 1. Every accuracy figure, mode label and measured quantity
carries the paper, table or section it came from. Anything I could not verify in a source
I actually read is marked **UNVERIFIED** and is never presented as a finding.

Collected: 2026-09-06. Observer: bucket-11 worker.
Licence posture throughout: metadata, abstracts and short quotations for research
purposes only. No source text is proposed for shipping into `data/`. Two sources that are
reachable but whose licence is unknown were deliberately **not** read — see 6.3.

---

## 0. The two decisions this bucket owns

The task set two questions. Both are answered here, up front, with the evidence and with
the boundary of what the literature actually settles.

### 0.1 How many named anchors does the openness scale need?

**Answer: at most five or six can be absolutely identified; three are physically distinct
regimes; the present eight are one to three too many, and their scalar spacing is
pathological. The literature settles the ceiling. It does not settle the exact number,
because no perceptual study of hi-hat openness exists.**

Three independent bounds, in decreasing strength:

**(a) The identification ceiling — Miller 1956, measured, strong.**
Miller reports channel capacity for absolute judgment of a single continuum:

> "The channel capacity for pitch seems to be about six and that is the best you can do."
> — Miller 1956, p. 85 (citing Pollack)

> "The channel capacity for absolute judgments of loudness is 2.3 bits, or about five
> perfectly discriminable alternatives." — Miller 1956, p. 85 (citing Garner)

> "the mean is 2.6 bits and the standard deviation is only 0.6 bit. In terms of
> distinguishable alternatives, this mean corresponds to about 6.5 categories, one standard
> deviation includes from 4 to 10 categories, and the total range is from 3 to 15
> categories." — Miller 1956, p. 86

Openness is presented in `axes.json` as exactly this kind of object: "labels for bands of
one normalised scalar, 0.0 fully closed to 1.0 fully open". For a single auditory continuum
the absolute-identification span is 4–10 categories, centred on 6.5, and for the two
auditory continua actually measured (pitch, loudness) it is 5–6. **Eight named anchors sits
at or above the top of that range.** Miller's caveat cuts the other way too and must be
stated: capacity rises when a stimulus varies on several dimensions at once, and hi-hat
openness varies decay, spectrum and rattle presence together, so 8 is not impossible —
it is simply unsupported, and no source measured it.

**(b) The physical-regime bound — Sekiguchi & Samejima 2023, modelled, medium.**
The only first-principles physical model of a hi-hat parameterises openness as `d`, "the
initial distance between the top and bottom cymbals which is controlled by the pedal"
(§3.2, eq. 25–26). It is *not* one continuum. The paper runs `d = 5.0e-6 m` (labelled
"Open hi-hat", Fig. 14) and `d = 0 m` ("Closed hi-hat", Fig. 15), and then says why a third
regime is out of reach:

> "with a real hi-hat, the situation is such that d is negative, because the force applied
> to the pedal causes the top and bottom cymbals to press against each other, resulting in
> static deformation. This would cause a faster decay in the real hi-hat. The calculation
> does not allow d to be negative because of the numerical divergence caused by the
> impossible placement of the cymbals." — §4.3

So there are three physically distinct regimes: `d < 0` pressed (the vocabulary's `tight`),
`d = 0` touching (`closed`), `d > 0` gap (everything from `closed-loose` to `open`). Below
`closed` the controlling variable is *normal force*, not gap; above it, gap. One scalar
running 0.0→1.0 silently splices two different physical quantities at the point where
`tight` meets `closed`. The paper also names a degree of freedom the model omits entirely:

> "the proposed model is preliminary and does not include the tilting motion that exists on
> a real hi-hat. Here, the term tilting refers to the rotational motion of a disk-shaped
> rigid body with a fixed center." — §4.3

Tilt is what makes a half-open hi-hat sound the way it does — contact is intermittent and
one-sided rather than annular. Nothing in the vocabulary carries it.

**(c) The decay-time discrimination bound — ISO 3382-1 / Seraphim, cited not read, weak.**
Openness acts on decay rate (Sekiguchi §4.3: "the overall decay is faster when d is 0 m").
The standard just-noticeable difference for reverberation time is 5% (ISO 3382-1:2009,
after Seraphim 1958); empirical estimates run 5–25%. **UNVERIFIED**: I did not reach the
standard or Seraphim, only secondary statements of the 5% figure, and no source in this
bucket measures the decay-time ratio between a closed and an open hi-hat, so the number of
JND steps across the openness range cannot be computed. What can be said is the shape of
the answer: *discrimination* of decay differences supports many more steps than
*identification* supports names. A fine scalar with few names is the physically honest
design; many names is not.

**Consequence for the vocabulary.** The present eight anchors have scalars
0.0 / 0.12 / 0.2 / 0.25 / 0.5 / 0.75 / 0.85 / 1.0. Three names (`closed`, `closed-loose`,
`quarter`) share the band 0.12–0.25, which is 13% of the axis, while the band 0.25–0.50 —
25% of the axis and the region where tilt and intermittent contact actually change the
sound — has no name at all. That distribution follows the vendor lists it was derived
from, not the physics. Recommended: keep five anchors carrying the three physical regimes
plus two subdivisions of the gap regime, and demote the rest. Under ADR-0003 the demoted
slugs are never deleted — they become `correction` aliases onto the retained anchors.

### 0.2 Does the radial strike-position axis resolve more than about three steps?

**Answer: no, not on the evidence that exists. Three radial steps are supported by the
physics, by every dataset design, by the only classification study that varied the count,
and by centuries-old drum nomenclature. Five degrade measurably, and they degrade
specifically by collapsing into their neighbours. No study measured what a human listener
can resolve, so the perceptual question is formally open.**

**(a) The one study that varied the number of positions — Tindale et al., ISMIR 2004.**
Design (§4.2, §5): three expert players, three snare drums, seven stroke types × 20
repetitions = 1260 samples; "The snare drums are marked so that the players would strike
the same place when performing the strokes." Five of the seven types are radial positions:
`center`, `near-center`, `halfway`, `near-edge`, `edge`. Two class groupings are directly
comparable: "Only 5" (all five positions) and "CHE" (`Center`, `Halfway`, `Edge`).

| Classifier / features | 5 positions ("Only 5") | 3 positions ("CHE") | chance |
|---|---|---|---|
| Neural net, all features (Table 1) | 88.3 / 86.1 / 86.6 / 85.6 % | 98.1 / 96.4 / 98.3 / 98.9 % | 20% / 33% |
| Neural net, time-domain only (Table 2) | 71.1 / 77.0 / 79.2 / 79.0 % | 91.3 / 95.9 / 97.2 / 98.1 % | |
| kNN, all features (Table 3) | 95.3 / 89.6 / 94.1 / 91.1 % | 99.3 / 96.1 / 98.7 / 96.9 % | |
| kNN, time-domain only (Table 4) | 90.9 / 88.8 / 87.6 / 90.0 % | 95.7 / 97.2 / 96.9 / 97.2 % | |
| SVM, all features (Table 5) | 86.8 / 79.7 / 82.3 / 82.6 % | 97.4 / 92.6 / 97.4 / 96.7 % | |
| SVM, time-domain only (Table 6) | 55.1 / 59.0 / 61.4 / 62.1 % | 85.4 / 89.1 / 91.1 / 91.9 % | |

(Four figures per cell are the four analysis windows: attack, 512, 1024, 2048 samples.)

Three positions are separable at 85–99% by every classifier and every feature set,
including time-domain features alone. Five positions cost 5–30 points, and the paper says
where the loss goes:

> "Many of the misclassifications in these tests were classified as the next nearest
> timbre." — §6

and what is needed to hold five up at all:

> "The spectral features were very useful for differentiating the different positions along
> the radius of the drum. Overall, the classifiers performed the 'Only 5' and the 'CHE'
> tests an average of 7.8% better with the spectral features than with the only the
> time-domain features." — §6

That is the definition of an axis being over-resolved: the extra anchors do not form their
own clusters, they bleed into the ones on either side.

**(b) What every dataset designer independently chose — three.**
- Prockup et al., ISMIR 2013 (Drexel MET-lab expressive percussion library), §3:
  "**strike positions: center, halfway, edge**", crossed with articulations
  (strike, rim shot, buzz stroke, cross stick), stick heights (8, 16, 24, 32 cm),
  intensities (light, medium, heavy) and snares on/off. 1804 examples for the subset used.
- Souza, Batista & Souza-Filho, IJCNN 2015, as summarised in Wu et al. 2018 §III-B: cymbal
  sounds "differentiated either by the position where the cymbal is struck (**bell, body,
  edge**), how a hi-hat is played (closed, open, chick), or other special effects such as
  choking a cymbal with the playing hand."
- Tabla nomenclature, developed over centuries and described in Patranabis et al. 2015 §1:
  the head (`puri`) has three named material zones — the central loaded patch (`syahi`),
  the intermediate ring (the "2nd circle", conventionally `maidan`), and the outer ring of
  thicker unattached skin (`chanti`). Three, again.

**(c) The measurement ceiling — Sokolovskis & McPherson, NIME 2014.**
State of the art in physically measuring where a snare was struck, using near-field optical
sensors under the head and time difference of arrival:

> "The average error for 100 drum strikes was 18mm with maximum error of 54mm." — §4

> "the distance from the centre of the drum is positively correlated with the error of the
> approximation of the strikes (p < 0.01, r = 0.52)" — §4

with the physical reason given: the TDOA equation "assumes that the velocity of a
wave-front propagating through the drumhead is uniform. This assumption is violated the
most when the strikes occur near the rim". On a 14" snare (radius ≈ 178 mm) an 18 mm mean
error gives roughly ten radial bins at best and a 54 mm worst case gives roughly three.
A capture rig cannot reliably label finer than about three to five bands near the rim —
which is exactly where a `near-edge` anchor would have to live.

**(d) Why three, physically.**
On a circular membrane the modes are labelled (m, n), m nodal diameters and n nodal circles
(Rossing 2001, Fig. 1). The centre is a node of every m > 0 mode, so a centre strike
excites only the axisymmetric family; the rim is a node of everything, so an edge strike
excites little and decays fastest; between them lies one privileged beating spot. This
gives three physically privileged radii and no fourth. Corroborated independently:

- Patranabis et al. 2015, conclusion (iv): "strokes made at the vicinity of centre circle
  pumped up energy at high frequency range and they are the brightest stokes while the
  strokes made at the edge of the membrane are weakest strokes having low energy."
- Madsen 2016 §4.3: at the edge "both samples have the steepest slope of decline across all
  3 regions of the drum. Suggesting that proximity to the shell of the drum is a main
  driver to dampening."
- Timpani: the normal beating point is chosen to suppress the concentric modes and favour
  the diametric ones. **UNVERIFIED** as to the exact radius — I could not reach Rossing's
  own text. The best secondary statement reached is *The Well-Tempered Timpani*
  (wtt.pauken.org, ch. 3, "Timpani Bowl", p. 3): "When a timpano is struck a quarter of the
  distance between the edge and the center, in many practical cases the inharmonic modes
  will radiate their energy much more efficiently and decay faster leaving the more
  harmonic preferred modes to dominate the sound spectrum." That is r ≈ 0.75R. The page
  attributes this sentence to no publication, though it cites Rossing 1982 (*Percussionist*)
  and Rossing 2000 elsewhere. The common trade phrasing "a quarter of the diameter in from
  the rim" gives r ≈ 0.5R instead. These are different radii. See §4.

**(e) Cymbals are different and the axis should not pretend otherwise.**
On a cymbal, radial strike position is a genuine continuum with no privileged steps.
Sekiguchi & Samejima §4.4 swept it in nineteen steps:

> "the position at which the point mass collides is varied in 0.05R increments from near
> the center of the top cymbal, namely r = 0.05R, to near the edge of the top cymbal,
> namely r = 0.95R … From this figure, it can be said that the closer to the edge of the
> strike point, the brighter the tone will be." — §4.4, Fig. 16

The measured quantity is the ratio of energy below 1 kHz to energy above 1 kHz, and it
moves monotonically. Monotone with no plateaux means no natural anchors: on cymbals the
named zones that matter are the *sites* (bell / bow / edge), which are geometric regions
with different curvature, not radial subdivisions of one site.

**What is NOT settled.** No study found in this sweep measures how many radial strike
positions a *human listener* can identify or discriminate on a membrane. Every number above
is either a machine classifier, a sensor accuracy or a modal argument. If the project needs
a perceptual number rather than a machine one, it does not exist yet in this literature.

---

## 1. Candidate source register (round A)

Method: 16 WebSearch sweeps varying register (scholarly / pedagogical / trade / notational
/ vendor), language (English, German, French) and era, until the session-wide WebSearch
budget was exhausted at 200/200; then 13 Crossref bibliographic queries and 3 DBLP queries
covering the registers the searches had not yet reached (Spanish, Italian, pre-MIDI,
positional sensing, choke, brush). Every candidate found is listed, reached or not.

Authority levels: **A** = primary measurement or first-principles model in a peer-reviewed
venue; **B** = peer-reviewed review, thesis or conference paper resting on A; **C** =
trade, pedagogical or student work; **D** = tertiary summary.

| # | Title | Author(s) | Year | Type | Locator | Auth | Reached |
|---|---|---|---|---|---|---|---|
| 1 | Science of Percussion Instruments | T. D. Rossing | 2000 | Book (World Scientific, Series in Popular Science v.3, 224 pp) | ISBN 981310564X; Google Books id `IIZIDQAAQBAJ` | A | **TOC only** |
| 2 | The Physics of Musical Instruments, 2nd ed. | N. H. Fletcher, T. D. Rossing | 1998 | Book (Springer) | DOI 10.1007/978-0-387-21603-4; ISBN 978-0-387-98374-5 | A | **No — see 6.3** |
| 3 | Acoustics of percussion instruments: Recent progress | T. D. Rossing | 2001 | Review, Acoust. Sci. Tech. 22(3) 177–188 | jstage `ast/22/3/22_3_177`, free access | A | **Yes, full text** |
| 4 | Acoustics of Drums | T. D. Rossing | 1992 | Feature, Physics Today 45(3) 40–47 | DOI 10.1063/1.881333 | A | No — paywall |
| 5 | Physical modeling and sound synthesis of the hi-hat | S. Sekiguchi, T. Samejima | 2023 | Paper, Acoust. Sci. Tech. 44(5) 352–360 | DOI 10.1250/ast.44.352, open PDF on J-Stage | A | **Yes, full text** |
| 6 | Auditory correlates of perceived mallet hardness for a set of recorded percussive sound events | D. J. Freed | 1990 | Paper, JASA 87(1) 311–322 | DOI 10.1121/1.399298 | A | **Abstract only** (Crossref JATS) |
| 7 | The magical number seven, plus or minus two | G. A. Miller | 1956 | Paper, Psychological Review 63(2) 81–97 | UT Austin mirror `MagicNumberSeven-Miller1956.pdf` | A | **Yes, full text** |
| 8 | Acoustics of snare drums: an experimental study of the modes of vibration, mode coupling, and sound radiation patterns | Huan Zhao | 1990 | M.S. thesis, Northern Illinois University | huskiecommons `allgraduate-thesesdissertations/974` | A | **Abstract only** — PDF 403 |
| 9 | Modes of vibration and sound radiation from a snare drum | Zhao Huan, T. D. Rossing | 1989 | Meeting abstract, JASA 85(S1) S33 | DOI 10.1121/1.2026918 | A | Metadata only |
| 10 | Vibration modes of the snare drum batter head | B. Larkin, A. Morrison | 2007 | Meeting abstract, JASA | DOI 10.1121/1.2942898 | A | Metadata only |
| 11 | Dampening vibration modes of the snare drum batter head | B. Larkin, A. Morrison | 2008 | Meeting abstract, JASA | DOI 10.1121/1.2935484 | A | Metadata only |
| 12 | Deep net classification of drum strike location with non-uniform membrane tension | Taylor et al. | 2023 | Paper, Proc. Meetings on Acoustics 51 | DOI 10.1121/2.0001828; also 10.1121/10.0023552 | A | No — 403 |
| 13 | Retrieval of percussion gestures using timbre classification techniques | A. Tindale, A. Kapur, G. Tzanetakis, I. Fujinaga | 2004 | Paper, ISMIR 2004, 541–544 | archives.ismir.net `ismir2004/paper/000235.pdf` | B | **Yes, full text** |
| 14 | Toward understanding expressive percussion through content based analysis | M. Prockup, E. Schmidt, J. Scott, Y. Kim | 2013 | Paper, ISMIR 2013 | archives.ismir.net `ismir2013/paper/000242.pdf` | B | **Yes, full text** |
| 15 | A review of automatic drum transcription | C.-W. Wu et al. | 2018 | Review, IEEE/ACM TASLP 26(9) | DOI 10.1109/TASLP.2018.2830113; OA at open-access.bcu.ac.uk/6180 | B | **Yes, full text** |
| 16 | Optical measurement of acoustic drum strike locations | J. Sokolovskis, A. McPherson | 2014 | Paper, NIME 2014, 70–73 | nime.org `proceedings/2014/nime2014_436.pdf` | A | **Yes, full text** |
| 17 | A scientific approach to microphone placement for cymbals in live sound | J. J. Harrison, A. J. Hill | 2013 | Paper, Proc. Institute of Acoustics 35(2) 219–227 | adamjhill.com `Harrison-Hill-RS2013.pdf` | B | **Yes, full text** |
| 18 | Harmonic and timbre analysis of tabla strokes | A. Patranabis et al. (Sir C. V. Raman Centre, Jadavpur Univ.) | 2015 | Preprint | arXiv:1510.04880 | B | **Yes, full text** |
| 19 | Bottom-head snare's effect on snare drum acoustics | R. Madsen | 2016 | Student report, UIUC Physics 406 | courses.physics.illinois.edu `phys406/sp2017/Student_Projects/Spring16/` | C | **Yes, full text** |
| 20 | Automatic classification of drum sounds with indefinite pitch | V. M. A. Souza, G. E. A. P. A. Batista, N. E. Souza-Filho | 2015 | Paper, IJCNN 2015, 1–8 | DOI 10.1109/IJCNN.2015.7280342 | B | No — metadata only, content via #15 |
| 21 | On drum playing technique detection in polyphonic mixtures | C.-W. Wu, A. Lerch | 2016 | Paper, ISMIR 2016, 218–224 | archives.ismir.net (index not resolved) | B | No — covered in round 1 dossier 11 |
| 22 | Modal approach for nonlinear vibrations of damped impacted plates: application to sound synthesis of gongs and cymbals | Ducceschi, Touzé et al. | 2015 | Paper, J. Sound Vib. | sciencedirect `S0022460X15000759` | A | No — paywall |
| 23 | Analyse et modélisation de vibrations non-linéaires de milieux minces élastiques — application aux instruments de percussion | C. Touzé | 2000 | PhD thesis (French register) | theses.hal.science `tel-00005656v2`; bibnum.ensta.fr/251 | A | No — not fetched |
| 24 | Vibrations non linéaires géométriques de structures minces (HDR) | C. Touzé | — | HDR (French register) | perso.ensta-paris.fr `~touze/PDF/hdrctVF.pdf` | A | No — host 503 |
| 25 | Transient wave propagation in a cymbal | Schedin | 2023 (repub.) | Paper, Int. Symp. Musical Acoustics | DOI 10.25144/15138 | A | No |
| 26 | Vibrational analysis of a splash cymbal by experimental measurements and parametric CAD-FEM simulations | — | 2024 | Paper, Vibration 7(1) | DOI 10.3390/vibration7010008 | A | No — metadata only |
| 27 | Amplitude and duration characteristics of snare drum tones | C. Henzie | 1960 | Ed.D. dissertation, Indiana University | cited as [7] in #13 | A | No — **pre-MIDI, origin of "stroke height"** |
| 28 | Measuring tonal characteristics of snare drum batter heads | R. Lewis, J. Beckford | 2000 | Article, Percussive Notes 38(3) 69–71 | cited as [11] in #13 | C | No |
| 29 | Some experiments concerning the effect of snares on the snare drum sound | D. Wheeler | 1989 | Article, Percussive Notes 27(4) 48–52 | cited as [20] in #13 | C | No — **the mechanism-axis source** |
| 30 | On the automatic transcription of percussive music — from acoustic signal to high-level analysis | A. Schloss | 1985 | PhD dissertation, CCRMA Stanford | cited as [15] in #13 | B | No — conga stroke classes |
| 31 | Modal analysis of a snare drum | M. Fischer | 2014 | Student report, UIUC Physics 406 | cited as [1] in #19 | C | No |
| 32 | Arm motion and striking force in drumming | S. Dahl | 2001 | Paper, ISMA 1, 293–296 | cited as [1] in #13 | A | No |
| 33 | Drum sound and drum tuning | R. Toulson (ed.) | 2021 | Book (Routledge) | DOI 10.4324/9781003104209; ch. 2 `-2`, ch. 8 Timbre `-8`, snare tuning `-10`, kick tuning `-11` | B | No — paywall |
| 34 | The Cymbal Book | H. Pinksterboer | 1992 | Book (Hal Leonard) | cited with p. 70 in #17 | C | No — **the trade source for cymbal anatomy** |
| 35 | Modern school for snare drum | M. Goldenberg | 1955 | Method book (Hal Leonard) | cited as [2] in #14 | C | No — pre-MIDI pedagogical |
| 36 | Classification of musical instruments (trans. Baines & Wachsmann) | E. M. von Hornbostel, C. Sachs | 1961 [1914] | Article, Galpin Soc. J. 14, 3–29 | cited as [1] in #5 | A | No — organological register |
| 37 | A common perceptual space for harmonic and percussive timbres | S. Lakatos | 2000 | Paper, Percept. Psychophys. 62(7) 1426–1439 | DOI 10.3758/BF03212144 | A | No — Springer auth redirect |
| 38 | Determining the just noticeable difference in timbre through spectral morphing: a trombone example | S. Carral | 2011 | Paper, Acta Acustica united w. Acustica | DOI 10.3813/AAA.918427 | A | Metadata only |
| 39 | Perceptual scaling of synthesized musical timbres: common dimensions, specificities, and latent subject classes | S. McAdams et al. | 1995 | Paper, Psychological Research | DOI 10.1007/BF00419633 | A | No |
| 40 | ISO 3382-1:2009, Acoustics — measurement of room acoustic parameters | ISO | 2009 | Standard | ISO 3382-1 | A | No — **the 5% RT JND is UNVERIFIED here** |
| 41 | Die Physik von Musikinstrumenten (Facharbeit) | H. Weich | — | German-register student work | holger-weich.de `Facharbeit.pdf` | C | No |
| 42 | Schlagzeug (Didaktik der Physik, Univ. Augsburg) | — | — | German-register course material | thomas-wilhelm.net `arbeiten/Schlagzeug.pdf` | C | No |
| 43 | Schlaginstrumente | Oesterreichisches Musiklexikon | — | German-register lexicon | musiklexikon.ac.at `ml/musik_S/Schlaginstrumente.xml` | D | Summary only |
| 44 | Analysing metallic percussion | G. Reid | 2002 | Trade article, Sound On Sound | soundonsound.com `techniques/analysing-metallic-percussion` | C | **Yes — contains no measurements** |
| 45 | Theory of the Indian musical drums, Part I | K. Nagabhushana Rao | — | Paper, Proc. Indian Acad. Sci. A 7(2) 75–84 | ias.ac.in `seca/007/02/0075-0084` | A | No — 403 |
| 46 | The eigenspectra of Indian musical drums | Sathej & Adhikari | 2009 | Paper, JASA 125(2) | arXiv:0809.1320 | A | No |
| 47 | Convolutional neural networks with batch normalization for classifying hi-hat, snare and bass percussion sound samples | Gajhede et al. | 2016 | Paper, Audio Mostly 2016 | DOI 10.1145/2986416.2986453 | B | No |
| 48 | Acoustic and modal analysis of an African djembe drum | — | 2000 | Meeting abstract, JASA 108(5 suppl.) 2591 | pubs.aip.org `jasa/article/108/5_Supplement/2591` | A | No — content via #3 |
| 49 | Banjo drum physics — sound experiments and simple acoustics demos | D. Politzer | 2018 | Preprint | arXiv:1806.08857 | B | No |
| 50 | Hi-hat / Choke cymbal / Sizzle cymbal / Crash cymbal (etc.) | Grove Music Online | 2001–2003 | Reference entries | DOIs `10.1093/gmo/9781561592630.article.52537`, `.j085200`, `.j412200`, `.j105300`, `.j424200`, `.j084600`, `.j452700`, `.j082400` | B | No — paywall; **worth chasing, these are the definitional entries** |
| 51 | Modes of vibration and directivity of percussion instruments | T. D. Rossing | 2018 | ASA outreach article, Explore Sound | exploresound.org `2018/03/modes-vibration-directivity-percussion-instruments/` | B | **Yes** |
| 52 | The Well-Tempered Timpani, ch. 3 "Timpani Bowl" | — | — | Pedagogical web book | wtt.pauken.org `chapter-3/timpani-bowl/3` | C | **Yes** — the only reachable statement of the timpani beating radius |

Reached in full: 12 of 52. Reached in part (abstract, TOC or metadata): 10. That ratio is
expected; the register itself is the deliverable, and it says clearly where the remaining
value sits — rows 1, 2, 4, 12, 27, 29 and 50.

---

## 2. Extracted terminology (round B)

### 2.1 Membrane and drum acoustics

| Term as the source spells it | Physical meaning | Source and locator |
|---|---|---|
| `(m, n)` mode | Membrane mode label, m = number of nodal diameters, n = number of nodal circles including the one at the edge | Rossing 2001, Fig. 1 and §2 |
| `(0,1)` mode | Axisymmetric fundamental. "A baffled membrane vibrating in its (0,1) mode acts as a monopole source. It radiates its energy and damps out very rapidly; hence this mode is not a factor in kettledrum sound." | Rossing 2001 §2 |
| `(1,1)` mode | "essentially a dipole source, radiates the note heard when a kettledrum is played" | Rossing 2001 §2 |
| `(2,1)`, `(3,1)` modes | Tuned a fifth and an octave above the (1,1); quadrupole and sextupole radiators | Rossing 2001 §2 |
| batter head | Upper head, the one usually struck | Tindale 2004 §2 |
| resonant head / snare head | Lower head; on a snare drum it bears the wires | Tindale 2004 §2; Rossing 2001 §3 |
| head–head coupling | "There is appreciable coupling between the two heads of a snare drum, especially at the lower frequencies. This coupling can take place acoustically, through the enclosed air, or mechanically, by way of the drum shell, and it leads to pairs of modes" | Rossing 2001 §3, Fig. 2 |
| — (finding) | "interactions between the two drum heads are mainly caused by acoustical coupling through the air enclosure rather than by mechanical coupling through the drum shell" | Zhao 1990, abstract |
| centre strike | Excites the m = 0 family only; every m > 0 mode has a node at the centre | Rossing 2001 Fig. 1 (inference from the mode diagrams, stated here as such) |
| edge / rim strike | Weakest and fastest-decaying: "strokes made at the edge of the membrane are weakest strokes having low energy" | Patranabis 2015, concl. (iv); Madsen 2016 §4.3 |
| sweet spot | Trade name for the halfway radius: "the 'sweet-spot' of the head (defined to be halfway between the center and the rim)" | Madsen 2016 §3 |
| normal beating spot (timpani) | Radius chosen to reinforce the diametric modes and suppress the concentric ones | **UNVERIFIED** — secondary only, wtt.pauken.org; exact radius disputed, see §4 |
| Helmholtz resonance (djembé) | "a bass note around 70 to 80 Hz, which appears to be due to the Helmholtz resonance of the shell" | Rossing 2001 §3 |
| stroke height | The height the stick starts from; established as "the major factor in the resulting amplitude of the strike" | Henzie 1960 via Tindale 2004 §3; measured levels 8/16/24/32 cm in Prockup 2013 §3 |
| radiation character of the first five drumhead modes | The first "radiates pretty much in all directions, at least in its own plane"; the rest "radiate most strongly in 2, 4, 6, or 8 directions" — monopole, dipole, quadrupole, hexapole, octupole | Rossing, ASA Explore Sound 2018 |
| two-head interaction | "the two membranes interact strongly as they vibrate", making "the modes or patterns of the drum quite different form what they are in a drum with a single membrane" | Rossing, ASA Explore Sound 2018 |

### 2.2 Snare mechanism and damping

| Term | Physical meaning | Source and locator |
|---|---|---|
| snares / snare wires | "usually made of metal and are strung across the bottom head of the drum. The snares vibrate in resonance when the drum is struck adding a noise component" | Tindale 2004 §2 |
| snares on / snares off | Recorded as an explicit binary condition in the reference expressive dataset: "samples with the snare wires both touching (snares on) and not touching (snares off) the bottom head" | Prockup 2013 §3 |
| snare damping (measured) | Snares on retained ≈23.5% of peak amplitude at 80 ms; snares off ≈66% (centre and halfway samples averaged) | Madsen 2016 §4.4 — **low confidence, n = 1 per condition** |
| snare-induced pitch shift | Fundamental shifted upward by ≈5 Hz (centre), ≈2 Hz (halfway), ≈9 Hz (edge) on a ≈211 Hz fundamental | Madsen 2016 §5.2 — **low confidence, n = 1** |
| dampening of a batter-head mode | Named as its own research object in the title of a JASA presentation | Larkin & Morrison 2008, DOI 10.1121/1.2935484 |
| O-ring | Damping ring on the head; "With the extra dampening from the O-ring, the samples could not be adequately studied." | Madsen 2016 §3 |

### 2.3 Cymbal acoustics

| Term | Physical meaning | Source and locator |
|---|---|---|
| bell (cup) / bow / edge | The three geometric regions of a Turkish cymbal, distinguished by curvature. "an actual cymbal has two surfaces with different radii of curvature: the cup and the bow" | Sekiguchi 2023 §2.1; anatomy figure in Harrison & Hill 2013 Fig. 2.1, after Pinksterboer 1992 p. 70 |
| China flange | "China cymbals have a similar anatomy, except they have an upturned flange instead of a continuous curved bow." | Harrison & Hill 2013 §2.1 |
| cymbal mode count | "Wilbur recorded over 100 modes of vibration in a 46-cm diameter medium crash cymbal, 23 of which are shown in Fig. 5." Elsewhere "some 300 modes have been observed in a 16-inch-diameter cymbal." | Rossing 2001 §6.1 |
| n = 0 modes | "In the n = 0 modes (top row), the center of the cymbal vibrates very little, and this nodal region expands as m increases." — the physical reason a bell strike and a bow strike are different sounds, not marketing | Rossing 2001 §6.1, Fig. 5 |
| strike sound | The first ≈1 ms: "the strike sound that results from rapid wave propagation during the first millisecond" | Rossing 2001 §6.1 |
| build-up | "the buildup of strong peaks around 700–1,000 Hz in the sound spectrum during the next 10 or 20 ms" | Rossing 2001 §6.1 |
| aftersound / shimmer | "the strong aftersound in the range of 3–5 kHz that dominates the sound a second or so after striking and gives the cymbal its 'shimmer'" | Rossing 2001 §6.1 |
| road to chaos | "first the generation of harmonics, then the generation of subharmonics, and finally chaotic behavior" | Rossing 2001 §6.2, Figs. 7–8 |
| active degrees of freedom | "there are between 3 and 7 active degrees of freedom and that physical modeling will require a like number of equations" | Rossing 2001 §6.2 |
| tip of stick / edge of stick | Two distinct excitation conditions recorded and plotted separately: "tip of stick on centre of bow", "edge of stick on edge of bow" | Harrison & Hill 2013, Figs. 4.7, 4.15, 4.16 |
| directivity, steady state | "By 500 ms all cymbals reach steady state vibratory patterns"; loudest zones "above and below the bow … below the centre and horizontal to the edge"; quietest "under the edge of the bell, above the transitional area between the bell and bow and above the centre" | Harrison & Hill 2013 §4, Fig. 4.11 |
| strike-position dependence | "The cymbal vibratory modes generated are partly dependant on the position of the strike" | Harrison & Hill 2013 §4 |

### 2.4 Hi-hat

| Term | Physical meaning | Source and locator |
|---|---|---|
| `d` | "the initial distance between the top and bottom cymbals which is controlled by the pedal" — the openness parameter, in metres | Sekiguchi 2023 §3.2, eqs. 25–26 |
| open hi-hat | Simulated at `d = 5.0e-6 m` | Sekiguchi 2023 §4.3, Fig. 14 |
| closed hi-hat | Simulated at `d = 0 m`; "the overall decay is faster when d is 0 m … the attenuation caused by setting d to zero becomes larger at lower frequencies" | Sekiguchi 2023 §4.3, Figs. 15–16 |
| pressed (d < 0) | The real tight state, outside the model: cymbals "press against each other, resulting in static deformation" | Sekiguchi 2023 §4.3 |
| rattling | "When in contact, a characteristic rattling sound is added to the sound of an ordinary cymbal. The duration in which the rattling sound is sustained depends on how much the pedal is loosened." | Sekiguchi 2023 §1 |
| tilting | "the rotational motion of a disk-shaped rigid body with a fixed center" — present on a real hi-hat, absent from the model | Sekiguchi 2023 §4.3 |
| closed / open / chick | The three hi-hat conditions in the cymbal-technique classification literature | Souza et al. 2015 via Wu et al. 2018 §III-B |

### 2.5 Playing technique and articulation

| Term | Physical meaning | Source and locator |
|---|---|---|
| rimshot | "A rimshot is when the player strikes the rim and head of the drum at the same time"; "Both the drumhead and rim are struck" | Tindale 2004 §4.2, Fig. 3; Prockup 2013 Table 1 |
| cross stick | "The butt of the stick strikes the rim while [the tip rests on the head]" | Prockup 2013 Table 1 |
| buzz stroke | A distinct articulation class alongside strike, rim shot and cross stick; "a buzz stroke evolves very differently than a rim shot" | Prockup 2013 §3, §4.1 |
| brush stroke | "when the player hits the drum with a brush instead of a stick" (Vic Firth standard brush, fully extended) | Tindale 2004 §4.2, §5 |
| choke | "choking a cymbal with the playing hand" — an effect distinct from strike position | Souza et al. 2015 via Wu et al. 2018 §III-B |
| basic rudiments | "roll, paradiddle, drag, and flam" — grouped as one kind of playing technique | Wu et al. 2018 §III-B |
| timbral variations | "ghost note, brush, cross stick, and rim shot" — grouped as the other kind | Wu et al. 2018 §III-B |
| kashira | Japanese tsuzumi: "a style of forcefully striking the membrane" | Rossing 2001 §3 |
| kan | Japanese tsuzumi: "a style where the membrane is struck normally" | Rossing 2001 §3 |
| otsu | Ko-tsuzumi: "the player loosens the shirabeo just after striking, causing a downward pitch glide; pitch changes of 16% have been noted." | Rossing 2001 §3 |

### 2.6 Tabla — the most finely differentiated stroke vocabulary reached

All from Patranabis et al. 2015 §1 (verbatim descriptions), for the nine bols analysed
across five instruments (45 signals total).

| Bol | Description as given | Head zone struck |
|---|---|---|
| Ta / Na | "lightly pressing the ring finger down in order to mute the sound while index finger strikes the edge" | chanti (edge) |
| Ti | "striking the dayan on the 2nd circle with the index finger and by keeping the finger on that position causes more damping" | maidan (2nd circle) |
| Teen | as Ti "but after striking if the index finger release quickly to give an open tone" | maidan |
| Ghe | "striking the bayan with middle and index finger keeping the wrist on the membrane" | bayan |
| (Ghin) | as Ghe "but after striking if released quickly" | bayan |
| Tu | "striking at the corner of centre circle of dayan with index finger only and immediately after striking finger will lift" | syahi boundary |
| Te | "striking the dayan with middle and ring finger at the centre of the circle" | syahi (centre) |
| Re | "striking the dayan with index finger at the centre of the circle and by keeping the finger on that position causes more damping" | syahi |

Structural terms: `puri` (head), `syahi`/`gub` ("a perfect circle, in the middle of the
puri … a semi-permanent paste made of coal dust, iron fillings, and rice paste"), `chanti`
("Around the outside of the puri, is a ring of thicker skin … this is not attached to the
lao"), `lao` (strap frame), `dayan` (right drum), `bayan` (left drum).

### 2.7 Perception and psychophysics

| Term / quantity | Value | Source |
|---|---|---|
| channel capacity, pitch | 2.5 bits ≈ 6 categories | Miller 1956 p. 85, after Pollack |
| channel capacity, loudness | 2.3 bits ≈ 5 categories | Miller 1956 p. 85, after Garner |
| channel capacity, taste (salt) | 1.9 bits ≈ 4 categories | Miller 1956 p. 85, after Beebe-Center et al. |
| channel capacity, visual position | 3.25–3.9 bits — "the largest channel capacity that has been measured" | Miller 1956 p. 86, after Hake & Garner |
| channel capacity, mean over continua | 2.6 bits ≈ 6.5 categories; ±1 SD = 4–10; range 3–15 | Miller 1956 p. 86 |
| perceived mallet hardness | A *unidimensional* perceptual scale, predicted from four attack-region parameters (mean and slope of spectral level, mean and time-weighted average of spectral centroid) over the first 325 ms; multiple R² = 0.725, F = 1135.8, p < 0.01 | Freed 1990, abstract |
| JND for reverberation time | 5% per ISO 3382-1:2009 after Seraphim 1958; empirical estimates 5–25% | **UNVERIFIED** — secondary statements only |

---

## 3. Axis mapping

### 3.1 Verdict per axis: physically real, or marketing?

This is the specific question this bucket was created to answer.

| Axis | Verdict | Evidence |
|---|---|---|
| `instrument` | **Real.** Different resonators. | trivial |
| `site` | **Real, and for cymbals the strongest distinction in the model.** Bell / bow / edge are regions of different curvature, and the n = 0 mode family has a near-nodal centre, so a bell strike cannot excite the modes an edge strike excites. `head` vs `rim` vs `shell` likewise: a rimshot drives head, rim and shell together. | Rossing 2001 §6.1 Fig. 5; Sekiguchi 2023 §2.1; Harrison & Hill 2013 §2.1, Fig. 4.11; Prockup 2013 Table 1 |
| `position` | **Real, but over-resolved at four values, and the fourth value is unnamed in the literature.** See §0.2. Three steps are supported everywhere; five are not; `offset` appears in no acoustics source. | Tindale 2004 Tables 1–6; Prockup 2013 §3; Sokolovskis 2014 §4; Patranabis 2015 §1 |
| `contact` (tip / shank / butt) | **Real.** Treated as a controlled experimental variable, and `cross stick` is *defined* by which part of the stick touches. | Harrison & Hill 2013 Figs. 4.7/4.15/4.16; Prockup 2013 Table 1 |
| `technique` | **Real.** Every value maps to a named, physically distinct excitation in at least one source. | §2.5 above |
| `ornament` | **Real but temporal, not timbral** — except `buzz`/`bounced`, which is also a timbre class. Flam, drag, ruff and roll are attack counts; `buzz stroke` is separately a class the classifier separates on spectral evolution. | Wu et al. 2018 §III-B; Prockup 2013 §3 |
| `openness` | **Real as a scalar. Over-named at eight anchors.** See §0.1. Also not one physical quantity: gap above `closed`, contact force below it. | Sekiguchi 2023 §3.2, §4.3; Miller 1956 pp. 85–86 |
| `damping` | **Real.** A named research object in its own right, and the tabla Ti/Teen pair shows finger-stays vs finger-lifts is a distinction traditions have encoded for centuries. | Larkin & Morrison 2008; Patranabis 2015 §1; Madsen 2016 §3 |
| `mechanism` | **Real.** Snares on/off changes decay by roughly a factor of three in retained amplitude at 80 ms and shifts the fundamental upward; head-to-head coupling is acoustic through the enclosed air, so disengaging the wires changes a resonator, not a mute. | Madsen 2016 §4.4, §5.2 (n = 1, low confidence); Rossing 2001 §3; Zhao 1990 abstract; Prockup 2013 §3 |
| `implement` | **Real, and perceptually a smooth unidimensional scale, so three hardness names are safe.** Mallet hardness is predicted at R² = 0.725 from attack spectral level and spectral centroid. One caution: a single student measurement found wood tip vs nylon tip "largely indistinguishable" — **UNVERIFIED, n = 1**, but worth a proper test before minting tip-material terms. | Freed 1990 abstract; Madsen 2016 §3 |
| `dynamic` | **Real, but the axis conflates gesture with result.** Stroke height (a gesture, 8/16/24/32 cm) and stroke intensity (a result, light/medium/heavy) are recorded as two separate dimensions in the reference dataset. Additionally, for cymbals dynamic is *not* orthogonal to timbre: above a threshold the plate enters subharmonic and then chaotic regimes, which is a change of sound kind, not of level. | Prockup 2013 §3; Henzie 1960 via Tindale 2004 §3; Rossing 2001 §6.2 |
| `timbre` (acoustic / 808 / fm / pcm …) | **Not an acoustic distinction at all.** These are synthesis-lineage and source-model labels. Nothing in the acoustics literature bears on them. Not marketing — they are real engineering categories — but they do not belong on the same footing as axes that name physical excitation. | absence of evidence across the whole register |
| `voicing` (standard / room / power / jazz / orchestra / lo-fi / dark) | **Marketing.** No acoustics source in this sweep names, measures or distinguishes any of these. They describe production choices and sample-library packaging, not properties of a struck instrument. This is the clearest "not physically real" answer the bucket can give. | absence of evidence across the whole register |

### 3.2 Terms found that fit NO existing axis

Per the brief, these are the most valuable findings, because each implies a missing axis.

1. **`otsu` — post-strike tension modulation.** "the player loosens the shirabeo just after
   striking, causing a downward pitch glide; pitch changes of 16% have been noted"
   (Rossing 2001 §3). The tension of the head is changed *after* the attack. This is not
   `technique: gliss` (a gesture across an instrument), not `damping`, and not
   `mechanism` (a state set before the strike). The same physical device appears on the
   talking drum and in bayan heel-of-hand pitch bending. **Missing: a post-attack
   continuous modulation axis, or a controller.**
2. **`syahi` / `maidan` / `chanti` — material zones of one head.** These are not radii on a
   uniform membrane; the syahi is a mass load of "coal dust, iron fillings, and rice paste"
   and the chanti is thicker skin that is *not attached* to the frame (Patranabis 2015 §1).
   The `position` axis presumes a homogeneous head where position is purely geometric.
   **Missing: a distinction between "radius on a uniform site" and "named material zone of
   a heterogeneous site".** Round 2's percussion buckets will hit this on every hand drum.
3. **Simultaneous second contact.** `Ghe` is struck "with middle and index finger keeping
   the wrist on the membrane" (Patranabis 2015 §1). The wrist is a second, load-bearing
   contact concurrent with the strike. `damping: muted` collapses this, but the wrist both
   damps *and* tunes. **Missing: more than one contact per term.**
4. **`strike sound` / `build-up` / `aftersound` (shimmer).** Rossing 2001 §6.1 decomposes a
   cymbal sound into three named temporal regions with different frequency content
   (first ms; 700–1000 Hz over 10–20 ms; 3–5 kHz after ≈1 s). Nothing in the vocabulary
   names a phase of one sound. Sizzle, wash and sustain terms all live in this region.
   **Missing: no decay-phase concept.** (May be out of scope for a pivot term; noted so
   reconciliation can decide.)
5. **Chaotic / wave-turbulence regime.** "between 3 and 7 active degrees of freedom"
   (Rossing 2001 §6.2). A cymbal driven hard is qualitatively a different oscillator, not
   a louder one. **Missing: an acknowledgement that `dynamic` and `timbre` are coupled for
   plate idiophones.**
6. **`tilting`.** The rotational motion of the top hi-hat cymbal about its centre
   (Sekiguchi 2023 §4.3). It is the mechanism by which a half-open hi-hat differs from a
   uniformly-gapped one, and it is unrepresented on any axis.

---

## 4. Conflicts and false friends

**One word, several meanings:**

| Word | Meaning A | Meaning B | Meaning C |
|---|---|---|---|
| `edge` | radial position on a drumhead (Tindale 2004 §4.2) | named region of a cymbal, a `site` (Harrison & Hill 2013 §2.1) | part of the *stick*: "edge of stick on edge of bow" (Harrison & Hill 2013 Fig. 4.7) — i.e. the shank, a `contact` |
| `bow` | region of a cymbal, a `site` (Rossing/Pinksterboer) | to excite with a violin bow, a `technique` — **absent from the vocabulary** | — |
| `open` | hi-hat openness state (Sekiguchi 2023 §4.3) | hand-drum "open tone" (Rossing 2001 §3, djembé) | tabla `Teen`, "release quickly to give an open tone" — a *damping release* (Patranabis 2015 §1) |
| `closed` | hi-hat `d = 0` (Sekiguchi 2023 §4.3) | conga/djembé "closed slap", a technique | — |
| `buzz` | `buzz stroke`, a multi-bounce ornament (Prockup 2013 §3) | snare-wire rattle, a mechanism (Tindale 2004 §2) | — |
| `damping` / `dampening` | the physical process (Larkin & Morrison 2008) | `damping` axis value distinct from `muted` — the split is **UNVERIFIED**, no acoustics source distinguishes the two words | — |
| `chick` | hi-hat foot close, in the vocabulary a `technique` | in the cymbal-classification literature one of three *openness-like* hi-hat conditions alongside closed and open (Souza 2015 via Wu 2018 §III-B) | — |
| `bell` | cymbal cup (Rossing 2001 §6.1) | cowbell, an instrument | church bell / handbell, in the same Rossing review §6 |

**Several words, one thing:**

- `sweet spot` (Madsen 2016 §3, "halfway between the center and the rim") = `halfway`
  (Tindale 2004, Prockup 2013) = the intermediate zone the tabla calls the *2nd circle* /
  `maidan`. Three registers, one radius.
- `cup` (Sekiguchi 2023 §2.1) = `bell` (Rossing 2001 §6.1, Harrison & Hill 2013 §2.1).
- `snares` = `snare wires` = `snappy` (trade). `wires-on`/`wires-off` in the vocabulary.
- `strike` (Prockup 2013 Table 1) = `hit` (vocabulary) = `kan`, "struck normally"
  (Rossing 2001 §3).

**A genuine numeric conflict, flagged for whoever owns the position axis:**
the privileged intermediate radius on a timpano is described as "a quarter of the distance
between the edge and the center" (*The Well-Tempered Timpani*, ch. 3 "Timpani Bowl" p. 3),
which is r ≈ 0.75R, while the common trade phrasing is "a quarter of the diameter in from
the rim", which is r ≈ 0.5R. Those are different places. Both are called "the normal
beating spot". The wtt page attributes its sentence to no publication. **UNVERIFIED** —
resolving it requires Rossing 1992 (Physics Today) or Fletcher & Rossing ch. 18. Until it
is resolved, `halfway` and any future `quarter` position value are ambiguous.

---

## 5. Gaps against vocabulary v0.1

Read against `vocabulary/axes.json` and `vocabulary/pivot.json` at
`origin/claude/kitwarp-pivot-vocab-data-w56ld3`.

### 5.1 Over-specified — more names than the physics or the perception supports

- **`openness`: 8 anchors.** `tight` 0.0, `closed` 0.12, `closed-loose` 0.2, `quarter` 0.25,
  `half` 0.5, `three-quarter` 0.75, `loose` 0.85, `open` 1.0. Two separate problems:
  (i) eight names is at or above the absolute-identification ceiling for a single
  continuum (Miller 1956 pp. 85–86); (ii) the spacing is inverted with respect to the
  physics — three names crowd into the 0.12–0.25 band (13% of the axis) while 0.25–0.50,
  the region where tilt and intermittent contact live, is unnamed. Recommend collapsing to
  five, with `closed-loose`, `quarter` and `three-quarter` retained as `correction`
  aliases per ADR-0003, never removed.
- **`position`: 4 values, one of which has no referent.** `centre`, `halfway`, `perimeter`
  are each attested. `offset` is attested in no acoustics source read here, and its
  position in the ordering (between `halfway` and `perimeter`) has no physical basis.
  Recommend either a locator for it from a vendor bucket, or a `correction` alias onto
  `halfway` or `perimeter`.

### 5.2 Mis-named or mis-classified

- **`timbre` and `voicing` are not the same kind of thing as the other axes.** Nothing in
  the acoustics literature bears on `voicing` at all (see §3.1). Keeping them alongside
  `site` and `technique` invites the reader to believe all twelve axes are equally
  grounded. Recommend at minimum a documented note in `axes.json` that these two are
  source-model and production labels rather than physical excitation properties.
- **`dynamic` conflates the gesture with the result.** Prockup 2013 §3 records stick
  height (8/16/24/32 cm) and stroke intensity (light/medium/heavy) as two dimensions
  because they are two dimensions. `ghost`/`soft`/`normal`/`hard`/`accent` is the result
  side only. Not necessarily wrong for a pivot term, but the omission should be recorded.
- **`ornament` mixes attack counts with a timbre class.** `flam`, `drag`, `ruff`, `roll`
  are counts; `buzz`/`bounced` is also a distinct spectral-evolution class in the
  classification literature. Worth noting so exporters do not treat them alike.

### 5.3 Missing

- **No `bowed` technique**, though bowed cymbal and bowed vibraphone are standard, and the
  word `bow` is already taken by a `site` value. This is a collision waiting to happen.
- **No post-attack tension modulation** (otsu, talking drum, bayan heel bend). See §3.2.1.
- **No material-zone concept** for heterogeneous heads (syahi / maidan / chanti). The
  `position` axis silently assumes a uniform membrane. See §3.2.2.
- **Only one `contact` per term**, so a strike with a simultaneous second contact (`Ghe`,
  wrist on the membrane) cannot be expressed. See §3.2.3.
- **`damping` has no `hand` value.** Souza et al. treat "choking a cymbal with the playing
  hand" as a named condition; the vocabulary's own axis description says hand damping
  while striking and while not striking are different sounds, but neither is a value.
- **`mechanism` has no snare-tension value.** Madsen 2016 §6 names it as the obvious next
  variable: "the impact of tightening or loosening the snares … very tight snares would
  greatly accelerate dampening and cause a higher shift in the harmonic frequency." Snare
  tension is continuous and audible; `wires-on`/`wires-off` is a two-state approximation
  of it.
- **No hi-hat `tilt`.** See §3.2.6.

### 5.4 Confirmed, keep as is

`site` (bell/bow/edge separation is the best-evidenced distinction in the whole model),
`contact` (tip/shank/butt), `technique`, `mechanism` as a concept, `implement` hardness at
three levels, and the decision to make `openness` a scalar with labels rather than a set of
unrelated terms — that framing is exactly right; only the label count is wrong.

---

## 6. Self-critique (round C)

### 6.1 The single most authoritative source I did NOT get

**Rossing, *Science of Percussion Instruments* (World Scientific, 2000)** — ch. 4 "Drums
with Indefinite Pitch" and ch. 9 "Cymbals, Gongs and Plates". I obtained only the table of
contents via Google Books. It is the one book that would settle, in one place: the exact
strike-position spectra for indefinite-pitch drums, the modal figures for cymbal bell vs
bow vs edge, and the timpani beating-point radius that section 4 flags as ambiguous. Every
other source in this dossier cites it. **Recommend the reconciliation pass chase this one
first** — a library copy or the World Scientific chapter DOIs would close three of the four
UNVERIFIED marks in this file.

Runner-up: **Rossing, "Acoustics of Drums", Physics Today 45(3) 40–47 (1992),
DOI 10.1063/1.881333** — paywalled, and it is the article that carries the strike-position
figures in accessible form.

### 6.2 What else I could not reach, and what it would have added

| Source | Would have added |
|---|---|
| Taylor et al., POMA 2023, deep-net drum strike location (403) | The most recent direct number on strike-location resolvability, on a *non-uniformly tensioned* head — i.e. the realistic case Sokolovskis's uniform-velocity assumption breaks on |
| Henzie 1960, Indiana Ed.D. dissertation | The pre-MIDI origin of `stroke height`, and the amplitude/duration data that would separate the gesture axis from the dynamic axis properly |
| Wheeler 1989, Percussive Notes 27(4) 48–52 | Measured spectra with snares engaged and disengaged — the proper source for the mechanism axis, replacing my n = 1 student report |
| Zhao 1990 NIU thesis full text (403 via the proxy) | The two-mass/three-spring coupling model and the radiation patterns; abstract only was reached |
| Grove Music Online entries for hi-hat, choke cymbal, sizzle cymbal, splash, China, top cymbal, Charleston cymbal (8 DOIs listed in the register) | The definitional register I am weakest in. These are the entries the whole trade vocabulary descends from |
| Souza et al., IJCNN 2015 | Per-class accuracies for the cymbal bell/body/edge and hi-hat closed/open/chick splits — the cymbal counterpart to Tindale's membrane numbers |
| Lakatos 2000, Percept. Psychophys. 62(7) | The MDS dimensionality of a *percussive* timbre space — the honest way to ask how many axes a listener uses at all |
| Touzé's thesis and HDR (French register, host 503) | The nonlinear-regime detail behind Rossing's "3 to 7 active degrees of freedom" |

### 6.3 A source I could reach and deliberately did not use

A full-text PDF of **Fletcher & Rossing, *The Physics of Musical Instruments*** is mirrored
at `csclub.uwaterloo.ca/~pbarfuss/The_Physics_of_Musical_Instruments.pdf`. Its licence is
unknown, and under CLAUDE.md rule 2 an unknown licence means all rights reserved. I did not
fetch or quote it. The book is registered as row 2 of section 1 so the project knows it is
the right source; it should be obtained legitimately. This is the largest single gap in the
dossier and it is a deliberate one.

### 6.4 The weakest evidence in this file, named

- **Madsen 2016 (UIUC Physics 406 student report)** carries the only quantitative
  snares-on/snares-off numbers here, and the author says himself: "the entirety of this
  report was based on only 1 of each type of sound sample being recorded … it is possible
  that different conclusions would have been drawn with slightly different sound samples."
  Every figure taken from it is marked low-confidence. It should be replaced by Wheeler
  1989 or by Larkin & Morrison's full papers.
- **The 5% JND for reverberation time** is quoted from secondary summaries of
  ISO 3382-1:2009 and Seraphim 1958. Neither was reached. Marked UNVERIFIED throughout.
- **The timpani beating radius** — see §4. Two mutually inconsistent conventions, neither
  verified against a primary source.

### 6.5 The structural hole in the literature itself

This is the finding the project most needs to hear, and it is a negative one.

**There is no perceptual study of hi-hat openness.** Crossref and DBLP queries for hi-hat
openness, degree of opening and aperture return exactly one acoustics paper (Sekiguchi &
Samejima 2023, a model, not a listening test) plus classification papers that treat
open/closed as labels. Nobody has asked a listener how many openness levels they can name.

**There is no perceptual study of radial strike position on a membrane either.** Every
number in §0.2 is a machine classifier or a sensor accuracy.

So both decisions this bucket owns rest on: a 1956 general psychophysical bound, a 2023
physical model, a 2004 classification study, and a 2014 measurement rig. That is enough to
say confidently that **eight openness anchors is too many and five radial positions is too
many**. It is not enough to say what the right numbers are to the nearest one. Anyone who
claims a precise answer from this literature is over-reading it, and the project should
record the two decisions as *bounded by evidence*, not as *determined by it*.
