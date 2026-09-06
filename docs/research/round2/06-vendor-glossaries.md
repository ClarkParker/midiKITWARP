# Bucket 06 — Drum and cymbal manufacturer terminology

Round 2 vendor-glossary sweep. Scope: the published terminology of cymbal, drumhead,
stick, hardware and hand-percussion manufacturers, the trade press, and retailer
category taxonomies — the words that sample libraries inherited.

Observer: worker `bucket-06-vendor-glossaries`. Collection date: 2026-09-06 for every
retrieval below. Method: WebSearch breadth pass (round A), then WebFetch extraction of
the pages that answered (round B).

Environment constraints that shaped what is here, stated up front because they
determine the confidence of every "not reached" row:

- `web.archive.org` is unreachable from this environment, by `curl` (egress policy)
  and by WebFetch (host refused). The Wayback route named in the brief was therefore
  unavailable for the whole bucket. Every pre-2000 catalogue is consequently unreached.
- `curl` to arbitrary hosts is blocked by egress policy, not only to github.com.
- The session's WebSearch budget (200 calls, shared across all workers) was exhausted
  after this bucket's twentieth search. Planned Spanish and Italian register searches
  did not run. Round B continued on WebFetch against URLs already identified.

---

## 1. Candidate source register (round A)

Twenty distinct searches were run before any extraction, varying register (trade,
pedagogical, retail, manufacturing), language (English, German, French) and source type
(vendor education page, vendor FAQ, artist-relations material, retailer buying guide,
trade magazine, vintage catalogue archive).

Authority levels: `A` = the manufacturer's own published definition; `B` = manufacturer
product or catalogue copy, definition implied rather than formal; `C` = retailer or
trade-press glossary quoting or paraphrasing trade usage; `D` = third-party aggregation.

| # | Title | Publisher | Type | Locator | Auth. | Reached |
|---|---|---|---|---|---|---|
| 1 | Frequently Asked Questions (cymbal anatomy section) | Zildjian | vendor FAQ | https://zildjian.com/pages/frequently-asked-questions | A | yes |
| 2 | Marching Cymbals 101 (lesson index) | Zildjian Artists & Education | vendor education | https://ae.zildjian.com/education/marching-cymbals-101/ | A | yes |
| 3 | Marching Cymbals 101: Cymbal Selection | Zildjian A&E | vendor education | https://ae.zildjian.com/education/marching-cymbals-101/marching-cymbals-101-cymbal-selection/ | A | yes |
| 4 | Cymbal Shopping Tips from Paul Francis | Zildjian blog | vendor blog | https://blog.zildjian.com/tips-for-shopping-for-cymbals | A | no |
| 5 | SABIAN's Guide to Cymbal Terminology | Sabian | vendor glossary | https://sabian.com/sabians-guide-to-cymbal-terminology/ | A | yes |
| 6 | Cymbals 101 | Sabian | vendor education | https://sabian.com/cymbals-101/ | A | yes |
| 7 | The Fine Art of Lathing | Sabian | vendor education | https://sabian.com/the-fine-art-of-lathing/ | A | yes |
| 8 | The Hand Hammerer's Goal | Sabian | vendor education | https://sabian.com/the-hand-hammerers-goal/ | A | no |
| 9 | Cymbal Anatomy | Paiste | vendor education | https://www.paiste.com/en/about/everything-cymbals/cymbal-anatomy | A | yes |
| 10 | Cymbal Sound Classification System | Paiste | vendor classification scheme | https://www.paiste.com/en/about/everything-cymbals/cymbal-sound-classification-system | A | yes |
| 11 | Usage & Care | Paiste | vendor education | https://www.paiste.com/en/about/everything-cymbals/usage-and-care | A | yes |
| 12 | Production Process; Selection & Testing | Paiste | vendor education | /en/about/everything-cymbals/cymbals ; /selection-and-testing | A | no (enumerated only) |
| 13 | Meinl Cymbals Wiki | Meinl | vendor glossary | https://meinlcymbals.com/en/Wiki | A | yes |
| 14 | Understanding Drumhead types and differences | Remo | vendor FAQ | https://remo.com/support/faq/understanding-drumhead-types-and-differences | A | yes |
| 15 | same article, support-portal mirror | Remo | vendor FAQ | https://support.remo.com/hc/en-us/articles/360052028852 | A | no (HTTP 403) |
| 16 | Evans Drum Set — Snare Batter (technology copy) | D'Addario / Evans | vendor catalogue | https://www.daddario.com/products/percussion/evans-drumheads/drum-set/drumset-snare-batter/ | A/B | yes |
| 17 | Drumhead Finder | D'Addario / Evans | vendor selection tool | https://www.daddario.com/pages/drumhead-finder | A | partial (tool labels not in HTML) |
| 18 | Studio-X / muffle-ring description | Aquarian | vendor catalogue | https://shop.aquariandrumheads.com/collections/studio-x | B | no (search text only) |
| 19 | ProMark landing page + FAQ (tip shapes, taper, woods) | D'Addario / ProMark | vendor FAQ | https://www.daddario.com/collections/promark | A | yes |
| 20 | Artists & Education index | Vic Firth | vendor education index | https://ae.vicfirth.com/education/ | A | yes |
| 21 | Percussion 101 (index) | Vic Firth | vendor education | https://ae.vicfirth.com/education/percussion-101/ | A | yes |
| 22 | Percussion 101: Crash Cymbals | Vic Firth | vendor education | https://ae.vicfirth.com/education/percussion-101/percussion-101-crash-cymbals/ | A | yes |
| 23 | Percussion 101: Tambourine | Vic Firth | vendor education | https://ae.vicfirth.com/education/percussion-101/percussion-101-tambourine/ | A | yes |
| 24 | RUTE / Brushes / VicKick Beaters collections | Vic Firth | vendor catalogue | https://vicfirth.com/collections/vic-firth-category-alternative-implements-brushes-more | B | no (search text only) |
| 25 | Vater Percussion site | Vater | vendor site | https://www.vater.com/ ; /pages/faq | A | no (page shell only; /pages/faq HTTP 503) |
| 26 | Anatomy of a Snare Drum | Yamaha | vendor education | https://hub.yamaha.com/drums/anatomy-of-a-snare-drum/ | A | yes |
| 27 | Anatomy of a Marching Snare Drum | Yamaha | vendor education | https://hub.yamaha.com/drums/marching/anatomy-of-a-marching-snare-drum/ | A | yes |
| 28 | The Modern Drum Set, Part 5: Cymbals and Hardware | Yamaha | vendor education | https://hub.yamaha.com/drums/stage/cymbals-and-hardware/ | A | yes |
| 29 | The Making of a Drum Sound | Yamaha | vendor education | https://hub.yamaha.com/drums/how-a-drum-sound-is-produced/ | A | yes (no usable terms) |
| 30 | Anatomy of Timpani / Marimba / Vibraphone / Chimes | Yamaha | vendor education | https://hub.yamaha.com/drums/percussion/anatomy-of-timpani/ and siblings | A | no (enumerated only) |
| 31 | Classics Features: Hardware | DW | vendor catalogue | http://www2.dwdrums.com/drums/classics/featsopts/hardware.asp | B | no |
| 32 | Support / FAQ | Pearl | vendor FAQ | https://www.pearldrum.com/support/faq | A | no (HTTP 403) |
| 33 | Gretsch Drums site (category names) | Gretsch | vendor catalogue | https://www.gretschdrums.com/ | B | yes (publishes no glossary) |
| 34 | 1994 Ludwig Drum Catalog (PDF) | Ludwig, via drumarchive.com | vendor catalogue | https://www.drumarchive.com/ludwig/1994_ludwig.pdf | B | no |
| 35 | Slingerland catalogues 1928 / 1936 / 1950 / 1968 (PDF) | Slingerland, via drumarchive.com | vendor catalogue | https://www.drumarchive.com/slingerland/slingerland1950.pdf and siblings | B | no |
| 36 | Ludwig Timpani and Concert Drums Catalog | Ludwig, via manuals.plus mirror | vendor catalogue | https://manuals.plus/m/56e531df494abf49aca156edff184bf14… | B | no |
| 37 | LP Rhythmology (video series) | Latin Percussion | vendor education | https://www.lpmusic.com/stories/rhythmology/ | A | index only; content is video. `/pages/education` HTTP 404 |
| 38 | Slaptop Cajons / cajon blog | Meinl Percussion | vendor blog | https://meinlpercussion.com/en/blog/cajons/slaptop-cajons | B | no; `meinlpercussion.com/en/Wiki` HTTP 404 — no percussion wiki exists |
| 39 | Online Expert: Cajon — Playing techniques | Thomann | retailer guide | https://www.thomannmusic.com/onlineexpert_page_cajon_playing_techniques.html | C | yes |
| 40 | Online Expert: Congas — First Steps | Thomann | retailer guide | https://www.thomannmusic.com/onlineexpert_page_congas_first_steps.html | C | yes |
| 41 | Online Expert: Congas — Form; Arrangement of the Drums | Thomann | retailer guide | .../onlineexpert_page_congas_form.html ; .../onlineexpert_page_congas_arrangement_of_the_drums.html | C | yes (thin) |
| 42 | Online Expert: Cymbals — Drum Kit Cymbals | Thomann | retailer guide | https://www.thomannmusic.com/onlineexpert_page_cymbals_drum_kit_cymbals.html | C | yes |
| 43 | Online Expert: Cymbals — Concert cymbals | Thomann | retailer guide | https://www.thomannmusic.com/onlineexpert_page_cymbals_concert_cymbals.html | C | yes |
| 44 | Online Expert: Cymbals — Application | Thomann | retailer guide | https://www.thomannmusic.com/onlineexpert_page_cymbals_application.html | C | yes |
| 45 | Online Expert: Drumheads — Damping | Thomann | retailer guide | https://www.thomannmusic.com/onlineexpert_page_drumheads_damping.html | C | yes |
| 46 | Online-Ratgeber Becken — Arten; Anwendung (German) | Thomann | retailer guide, DE | https://www.thomann.de/de/onlineexpert_page_becken_arten.html ; .../becken_anwendung.html | C | yes |
| 47 | Drums & Percussion department taxonomy | Sweetwater | retailer taxonomy | https://www.sweetwater.com/shop/drums-percussion/ | C | no (HTTP 403); sub-category names only from search text |
| 48 | How To Choose The Right Drumsticks | DRUM! Magazine | trade press | https://drummagazine.com/how-to-choose-the-right-drumsticks/ | C | no (fetch returned empty body) |
| 49 | Modern Drummer drumming lexicon | Modern Drummer | trade press | no canonical URL located | C | no |
| 50 | Lexique du batteur | rimshotetghostnote.fr | trade glossary, FR | https://rimshotetghostnote.fr/lexique/ | D | no |
| 51 | Glossaire Batterie : 40 Termes Techniques | leguidedesbatteurs.com | trade glossary, FR | https://leguidedesbatteurs.com/glossaire-batterie/ | D | no |
| 52 | Glossaire de la Batterie et du Batteur | Redison | retailer glossary, FR | https://www.redison.com/pages/glossaire-de-la-batterie-et-du-batteur | D | no |
| 53 | Batterie & co — Lexique | drumsandco.com | trade glossary, FR | http://www.drumsandco.com/cours/lexique.htm | D | no |
| 54 | Fiche « batterie », Vitrine linguistique | Office québécois de la langue française | terminology authority, FR | https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26533038/batterie | B | no — **strong candidate for a later pass** |
| 55 | Cymbal Anatomy 101 | Sound Pure (retailer) | retailer guide | https://www.soundpure.com/a/expert-advice/drums/cymbal-anatomy-101/ | D | no |
| 56 | Drumstick Anatomy | Music Arts "The Vault" | retailer guide | https://thevault.musicarts.com/drumstick-anatomy/ | C | no (five-part anatomy from search text only — UNVERIFIED) |
| 57 | Drum Glossary: 250+ Drum Terms | drumming.com | trade glossary | https://www.drumming.com/drum-glossary | D | no |
| 58 | Wayback Machine / CDX API | Internet Archive | archive | http://web.archive.org/cdx/search/cdx | — | **blocked in this environment**, both curl and WebFetch |

Reached: 26 of 58. Every unreached row is a worklist item with a live locator, except
row 58, which is an environment limitation.

The twenty round-A searches, for the record: Zildjian cymbal anatomy; Sabian
glossary/profile/taper/lathing; Paiste sound character; Meinl cymbal anatomy zones;
Remo bearing edge/collar/batter/resonant; Evans drumhead anatomy; Vic Firth drumstick
anatomy; ProMark tip shapes; LP conga stroke names; LP timbales cascara/paila/abanico;
Meinl cajon technique; Thomann Becken Kuppe/Rand/Bogen (DE); Modern Drummer glossary;
Ludwig catalogue octoban/gong drum/piccolo/timbale; Vic Firth brushes/rute/beaters;
Sweetwater percussion taxonomy; anatomie d'une cymbale cloche/bord/corps (FR); Aquarian
muffling ring; DW hardware strainer/counterhoop/lug; drumarchive vintage catalogues.

---

## 2. Extracted terminology (round B)

### 2.1 Cymbal anatomy — the four majors disagree on the zone names

The most consequential table in the bucket: "bow / edge / bell" is the zone triple every
sample library ships, and only some of the four majors actually use it.

| Term as spelled | Vendor | Verbatim definition | Locator |
|---|---|---|---|
| Bell / cup | Zildjian | "the bell or cup size determines the amount of overtones or ring projected by a cymbal" | Zildjian FAQ, cymbal anatomy section |
| Profile / "bow" | Zildjian | "The profile or 'bow' of a cymbal affects its pitch and overtones. Higher profile cymbals will be higher in pitch and have fewer overtones." | Zildjian FAQ |
| Taper | Zildjian | "The degree to which the cymbal changes in thickness from the cup to the edge. The design of the taper will contribute to the amount of Crash-like or Ride-like qualities." | Zildjian FAQ |
| **Ride area** | Zildjian | "The center portion of the cymbal. This area doesn't open up immediately when struck, making it effective for pronounced stick tones and patterns." | Zildjian FAQ |
| **Crash area** | Zildjian | "The outer edge where a cymbal responds immediately and where most players strike to produce an instant Crash response." | Zildjian FAQ |
| Random hammering | Zildjian | "Random hammering applies the hammer strikes irregularly all over the cymbal surface. This lowers the profile and pitch, reduces and darkens overtones." | Zildjian FAQ |
| Symmetrical hammering | Zildjian | "Symmetrical hammering applies hammering strikes in organized patterns over the surface of the cymbal. This heightens the profile of the cymbal, raises its pitch." | Zildjian FAQ |
| Tonal grooves | Zildjian | "Applied during the final lathing stage. They facilitate the escape of sound energy from the cymbal." | Zildjian FAQ |
| Rivets | Zildjian | sold as "Stainless steel Sizzle Rivet 12-packs" for adding sizzle | Zildjian FAQ |
| Bell | Paiste | "The bell is at the center of the cymbal. Its shape and size affects the sound of the whole cymbal, and it is a useful playing area as it produces a separate type of sound, usually a clear tone, with a dominant higher pitch and sparse overtones." | Paiste, Cymbal Anatomy |
| **Surface** | Paiste | "The surface of the cymbal produces the majority of the cymbal's vibration, and therefore its sound." | Paiste, Cymbal Anatomy |
| Edge | Paiste | "Striking the edge of the cymbal produces the cymbal's fullest sound, commonly referred to as «crash»." | Paiste, Cymbal Anatomy |
| Taper | Paiste | "The taper is the gradual decrease in thickness from the bell to the edge." | Paiste, Cymbal Anatomy |
| **Curvature or Bow** | Paiste | "When cymbals are hammered, the alloy expands sideways at the point of the hammer mark. This expansion causes the cymbal to become curved downward from the bell." | Paiste, Cymbal Anatomy |
| Bell | Meinl | "The center part which transfers into the cymbal profile", producing "a cutting, high-pitched sound" | Meinl Cymbals Wiki |
| Bow | Meinl | the area approximately halfway from the bell to the edge; on a ride it gives the classic "ping" | Meinl Cymbals Wiki |
| Edge | Meinl | the outer perimeter; on a ride it gives crash swells | Meinl Cymbals Wiki |
| Profile | Sabian | "the shape and height of a cymbal as you look at it from the side. The higher a cymbal's profile is, the higher its pitch becomes and the brighter it is than a similar cymbal of the same size and lower profile." | Sabian, Cymbals 101 |
| Taper | Sabian | "the change in thickness from the bell to the edge of a cymbal … crucial for determining the degree of attack and wash" | Sabian, Cymbals 101 |
| Lathing | Sabian | "This technique involves shaving small amounts of metal from the surface of the cymbal, allowing for precise control over its sound and tone." | Sabian, The Fine Art of Lathing |
| Tonal grooves | Sabian | "lathing cuts tonal grooves into the surface, allowing the cymbal to flex and breathe while helping to both move vibrations around the metal and project the overall sound" | Sabian, The Fine Art of Lathing |
| Hammering | Sabian | "improves the complexity of a cymbal's sound" | Sabian, Cymbals 101 |
| Finish: natural / brilliant / raw | Sabian | "natural" (unpolished) or "brilliant" (polished); unlathed is "raw" | Sabian, Cymbals 101 |
| Kuppe | Thomann (DE) | German for bell/cup; a Bell cymbal "praktisch nur aus Beckenkuppe besteht" | thomann.de, Becken — Arten |
| Rand | Thomann (DE) | "Der Rand eines Beckens ist sein dünnstes und empfindlichstes Teil" | thomann.de, Becken — Anwendung |
| Bogen | Thomann (DE) | named as a cymbal part alongside Kuppe, Rand, Loch, Profil | thomann.de, Becken — Arten |
| Loch | Thomann (DE) | the centre hole | thomann.de, Becken — Arten |
| Bell | Thomann (EN) | "a raised and thicker area in their center" that "when struck produces a more defined, bright and often piercing sound" | thomannmusic.com, Cymbals — Drum Kit Cymbals |
| cloche / dôme / bord | French trade usage | the raised centre / the edge; the middle region is called "le bow" in French drum writing, i.e. the English word is borrowed untranslated | search-level evidence only, sources 50-53 — **UNVERIFIED** |

**Finding.** Zildjian, the largest cymbal maker, does not publish "bow" and "edge" as
playing zones at all. Its published zone names are **ride area** (centre portion) and
**crash area** (outer edge); it uses "bow" only as a synonym for *profile*, a shape
property. Paiste likewise uses **bow** for the curvature and **surface** for the playable
middle region. Only Meinl uses bow/edge/bell as the zone triple. The libraries'
`Bow / Edge / Bell` articulation naming therefore descends from Meinl-style usage, not
from a trade-wide standard, and it collides with the Zildjian and Paiste sense of "bow".

### 2.2 Paiste's Cymbal Sound Classification System — a vendor's own axis model

Paiste publishes a parameter scheme rather than a word list. It is the closest thing in
the trade to an axis model and is structurally comparable to the KITWARP axes.
Locator for every row: Paiste, Cymbal Sound Classification System.

| Group | Parameter | Scale as published | Definition |
|---|---|---|---|
| Physical | Size and Thickness | "Small to Large" / "Thin to Thick" | — |
| Physical | Weight | "Extra Thin to Extra Heavy" | thickness proportional to size |
| Physical | Volume | "Very Soft to Very Loud" | useful volume range |
| Sound character | Color | "Very Bright to Very Dark" | overall relative strength of higher to lower frequencies |
| Sound character | Frequency Range | "Very Narrow to Very Wide" | upper and lower frequency limits present |
| Sound character | Frequency Mix | "Very clean (delicate) to Very Complex (rough)" | density of cymbal sound |
| Function | Attack / Stick Sound | "Pronounced/Pingy to Spread/Washy" | initial sound following the drumstick stroke |
| Function | Response Intensity | "Dry to Lively" | frequencies developing from cymbal vibration |
| Function | Sustain | "Short to Long" | length of audible time after striking |
| Function | Bell Character (rides) | "Integrated to Separated" | whether the bell sound is distinct from the rest of the cymbal |
| Function | Hi-Hat Chick Sound | "Soft/Tight to Sharp/Pronounced" | "sound of two cymbals clashing" |
| Function | Feel | "Soft to Heavy" | physical sensation through the stick into the hands |

**Bell Character** and **Hi-Hat Chick Sound** are the vendor origin of the library
articulation names `Bell` and `Chick`. The rest are retrieval facets.

### 2.3 Sabian's sound-character glossary — thirty terms, verbatim

Sabian is the only major publishing a formal glossary with definitions. It defines **no**
anatomy terms and **no** cymbal type names; it is purely a sound-description vocabulary.
Locator for every row: SABIAN's Guide to Cymbal Terminology.

| Term | Sabian's definition (verbatim) |
|---|---|
| Sustain | "The duration a cymbal vibrates after being struck." |
| Wash | "The characteristics of sound following the attack" / "the sound during the sustain" |
| Dry | "Dry cymbals have shorter sustain, muted wash that emphasizes stick definition and precision." |
| Cut | "The ability of a cymbal to be clearly heard in a mix, even with loud instruments." |
| Attack | "How quickly a cymbal produces sound after being struck." |
| Warm | "A smooth, rich sound with mid to low frequency overtones." |
| Dark | "Dark cymbals emphasize lower frequency partials, resulting in a more subdued, complex tone." |
| Bright | "Bright cymbals emphasize higher frequencies, delivering sharp tones that stand out in loud environments." |
| Trashy | "A raw, distorted, biting sound that's perfect for explosive accents and unique textures." |
| Clean | "A harmonious sound profile with focused overtones." |
| Shimmering | "Light, sparkling, and lively overtones." |
| Explosive | "Immediate, loud burst of sound, typical of crash cymbals." |
| Mellow | "Smooth, warm tone with a soft attack." |
| Focused | "Controlled sound with a tight sonic range, not overly complex." |
| Rich | "Full-bodied sound with complex layers of overtones." |
| Raw | "Untamed, earthy sound with an organic feel." |
| Complex | "Multi-layered sound with shifting washy overtones." |
| Controlled | "Sound that stays tight and doesn't 'splash out' too much." |
| Glassy | "Very clear, smooth, high-end shimmer." |
| Buttery | "A soft, smooth response under the stick, especially used for hi-hats and rides." |
| Sizzle | "A slight buzzing or sustained shimmer (especially when rivets are used)." |
| Pangy | "Gong-like, metallic, exotic attack (think: China cymbals or Gongs)." |
| Responsive | "Cymbal reacts easily to light touch or stick." |
| Fast | "Quick attack and quick decay (sound disappears quickly)." |
| Slow | "Longer buildup of volume, slower decay." |
| Bouncy | "Good rebound off the stick, feels lively." |
| Dead | "Very short sustain, no lingering sound." |
| Sloshy | "Loose, messy hi-hat sound when open." |
| Tight | "Compact, clean and direct response." |
| Loose | "Open, airy feel, often for expressive or open hi-hat sounds." |

### 2.4 Cymbal type names

| Type | Vendor | Verbatim definition | Locator |
|---|---|---|---|
| Ride | Sabian | "Cymbals that are mostly used to maintain repetitive rhythmic patterns." 20-22" typical, 18-24" range | Sabian, Cymbals 101 |
| Ride | Thomann | "usually played in a repetetive rhythm to convey the basic feel and rhythmic subdivision of the music" | Thomann, Drum Kit Cymbals |
| Ride | Meinl | 20-22" typical; three sounds by strike location — bell (accented), bow ("ping"), edge (crash swells) | Meinl Wiki |
| Crash | Sabian | "Generally used to play accents"; thinner and smaller than rides (14-20"), "a burst of sound" | Sabian, Cymbals 101 |
| Crash | Meinl | "provide punch, flair, accents, energy, crescendos", 14-22"+, struck with glancing blows | Meinl Wiki |
| Hi-hats (Hats) | Sabian | "A pair of cymbals mounted on a stand that is operated/played by the foot." 14" common | Sabian, Cymbals 101 |
| Hihat | Meinl | "A pair of cymbals that include a top and bottom cymbal" on a pedal stand; 14" standard, 10-16" | Meinl Wiki |
| Splash | Sabian | "Small cymbals used to play short accents", 6-12", an "effect" cymbal | Sabian, Cymbals 101 |
| Splash | Meinl | "the smallest cymbal types in most kits, typically ranging from 6" to 12"", "lightning-fast response" | Meinl Wiki |
| Splash | Thomann | "smaller versions of crash cymbals with much shorter sustain" | Thomann, Drum Kit Cymbals |
| China | Sabian | "Cymbals that have an upturned edge", 16-18", "a sharp, cutting and dirty-sounding accent", "trashy" | Sabian, Cymbals 101 |
| China | Meinl | "an upward facing flanged edge that gives the cymbal an exotic, Chinese gong-like effect", 12-22" | Meinl Wiki |
| China | Thomann (DE) | "charakteristischem abgeflachten Rand" | thomann.de, Becken — Arten |
| Effect cymbals | Sabian | classification grouping splash and china | Sabian, Cymbals 101 |
| Crash-Ride | Meinl | "weight that falls in-between" ride and crash | Meinl Wiki |
| **China Ride** | Meinl | "combination between a china and ride cymbal" with a slightly upturned 1-2" edge | Meinl Wiki |
| **Flat Ride** | Meinl | ride cymbal without a bell, "highly articulate and defined with almost no wash", used in jazz | Meinl Wiki |
| Bell | Meinl | splash shape "but with extra heavy weight"; "higher pitch and longer sustaining ring" | Meinl Wiki |
| Bell-Becken | Thomann (DE) | "einen Klang erzeugen, der an den Glockensound eines Ride-Beckens erinnert" | thomann.de, Becken — Arten |
| **Trash Crash** | Meinl | crash with "hole cut-outs" that "dry the cymbal out — meaning they reduce the ring — while adding a host of complex tones" | Meinl Wiki |
| **Trash Splash** | Meinl | splash "with added hole cut-outs to boost trashiness and shorten the sustain" | Meinl Wiki |
| **Trash China** | Meinl | china with hole cut-outs, "earthy, gritty and dirty" | Meinl Wiki |
| Stack / Cymbal Stack | Meinl | "two or more cymbals of various types, sizes and shapes that are stacked on top of each other" | Meinl Wiki |
| Stacks | Thomann (DE) | "Zwei ineinander gelegte Becken" | thomann.de, Becken — Arten |
| **Drumbal** | Meinl | "cymbal which is used on a drum for completely unique sound effects", with a handle, 8" or 10" | Meinl Wiki |
| Suspended cymbal | Thomann | orchestral single cymbal, played with felt-covered mallets for rolls and crescendos | Thomann, Concert cymbals |
| Crash cymbals (pairs) | Thomann | "held by straps that pass through the hole in the centre of the cymbal", "struck together strongly … or lightly rubbed together", "usually struck together at a slight angle to avoid creating a brief vacuum" | Thomann, Concert cymbals |
| Ping | Thomann | "the bright sound of the sticks impact, which provides definition to your rhythms" | Thomann, Drum Kit Cymbals |
| Wash | Thomann | "the darker underlying roar that can build up when playing a ride cymbal" | Thomann, Drum Kit Cymbals |
| Chick sound | Thomann | produced by playing hi-hats "with just the pedal" | Thomann, Drum Kit Cymbals |
| Splash sound (hi-hat) | Thomann | also produced through hi-hat pedal manipulation | Thomann, Drum Kit Cymbals |

### 2.5 Alloys and finishes

Meinl publishes the fullest set. Locator for every row: Meinl Cymbals Wiki.

| Term | Definition (verbatim) |
|---|---|
| B8 Bronze | "92% copper and 8% tin", referred to as "sheet bronze" |
| B10 Bronze | "90% copper and 10% tin" |
| B12 Bronze | "88% copper and 12% tin" |
| B20 Bronze | "80% copper and 20% tin" |
| MS63 Brass | "63% copper and 37% zinc" |
| FX9 Alloy | "69% copper, 15% zinc, 15% manganese and 1% aluminum" |
| Brilliant Finish | polished, mirror-like; "slightly refined" sound, "smoother, lower frequency" |
| Dark Finish | unlathed or matte; darker tone, reduced sustain |
| Sandblasted / Sand Finish | "fine grain sand" surface creating a "dampened sound" |
| Raw / Unlathed | hand-hammer markings visible; minimally processed surface |
| Smoked Bronze | "dark finish" with "fully lathed and brilliant finish underside" |
| Hand Hammered / Machine Hammered | shaped by hand for individual character / mechanically for consistency |
| Laser Etch Technology | "modern laser etch technology to engrave serial numbers and certain logos" (2002+) |

### 2.6 Drumhead terminology

| Term | Vendor | Verbatim definition | Locator |
|---|---|---|---|
| Batter Head | Remo | "This is the top drumhead you hit with your sticks, brushes, mallets, or hands. It's what creates the sound when you strike it." | Remo FAQ, Understanding Drumhead types |
| Batter Head | Yamaha | "The top head that is struck with sticks or brushes." | Yamaha, Anatomy of a Snare Drum |
| Batter Head | Yamaha | "The top head of the drum that is played with drumsticks." | Yamaha, Anatomy of a Marching Snare Drum |
| Resonant Head | Remo | "This is the bottom drumhead, located on the opposite side of the drum. It's called 'resonant' because it helps create the tone and sustain by vibrating with the air inside the drum." | Remo FAQ |
| Snare Head | Yamaha | "The bottom head, also known as the resonant head" | Yamaha, Anatomy of a Snare Drum |
| Snare-Side Head | Remo | "Snare drum resonant heads (also called 'snare-side' heads) are much thinner than other resonant heads"; "should never be used as batter heads" | Remo FAQ |
| Mil | Remo | "Drumhead thickness is measured in 'mil,' which stands for thousandths of an inch. For example: 1 mil = 1/1000th of an inch." | Remo FAQ |
| Collar | Evans | "The drumhead collar is formed and the film is secured into a metal channel, which is then placed in between the drum's bearing edge and hoop." | daddario.com Evans copy, via search text — **partially UNVERIFIED** |
| Level 360 | Evans | "allows for ease of tuning and optimal quality of sound" | daddario.com, Evans Drum Set snare batter |
| Control Ring | Evans | "Eliminates excess overtones and controls sustain" | ibid. |
| Dry Vents | Evans | "Eliminate excess overtones by reducing transfer of energy to the reso head" | ibid. |
| Reverse Dot | Evans | "Provides extra durability, focus, and attack" | ibid. |
| Power Center | Evans | "Provides extra durability, focus, and attack" | ibid. |
| SST (Sound-Shaping Technology) | Evans | "overtone control … removing muddy mid-range overtones" | ibid. |
| Hydraulic | Evans | "Thin layer of oil between two plies of film to supress unwanted overtones" | ibid. |
| UV Coating | Evans | "UV-cured coating offers unmatched durability and consistency" | ibid. |
| Ply count | Evans | "1 ply" / "2 ply" film layers | ibid. |
| Coating types | Evans | Coated, Frosted, Calftone, Hybrid weave, Mesh | ibid. |
| Head-model names | Evans | Genera, HD, ST, G1, G2, G12, Onyx, UV1, UV2, Power Center, EC (Edge Control), Heavyweight, Hybrid, Calftone, dB Zero | ibid. |
| Sound descriptors | Evans | Attack "Balanced"→"Defined"; Tone "Dark"→"Bright"; Sustain "Short"→"Long"; Durability "Average"→"Extended" | ibid. |
| "X" muffle ring (Studio-X) | Aquarian | integrated overtone-control ring on the underside near the collar | search text only — **UNVERIFIED** |
| Bearing edge | Yamaha | "A 45-degree bearing edge is often utilized on the bottom side to ensure proper snare articulation" | Yamaha, Anatomy of a Marching Snare Drum |

### 2.7 Named damping accessories — the vendor vocabulary behind the `damping` axis

Trade product names that function as terminology; several appear verbatim in library
articulation lists. Locator for every row: Thomann Online Expert, Drumheads — Damping.

| Term | Definition (verbatim) | Applies to |
|---|---|---|
| Duct tape | "Applied in small pieces or folded at the edge of the drumhead, it quickly reduces annoying overtones" | snare, toms |
| Moongel (RTOM) | "a type of firm gel that sticks to the drumhead surface, is removable, and reusable" | snare, toms |
| Snareweight | leather affixed to the rim with a magnet, "can be lowered onto the drumhead as needed" | snare |
| Mini Muff (Rohema) | a furry damper operating similarly to Snareweight | snare |
| Head overlay (Big Fat Snare Drum) | "Just lay them on the drumhead, and you'll instantly get fat disco snare sounds or muffled '70s tom sounds" | snare, toms |
| Transparent damping ring | an economical overtone ring | snare, toms |
| Damping pillow | "offered in different versions by Pearl, DW, Evans, and others" | bass drum |
| Foam rails (Sonitus "Kicker") | shaped foam for internal damping | bass drum |
| Felt strip | "simply clamped between the drumhead and bearing edge"; vintage sound that lets "your bass drum sound to 'breathe' more" | bass drum |

### 2.8 Drumstick terminology

| Term | Vendor | Verbatim definition | Locator |
|---|---|---|---|
| Acorn (tip) | ProMark | "Increased responsiveness and articulation" | daddario.com/collections/promark FAQ |
| Barrel (tip) | ProMark | "Delivers a punch sound with pronounced attack" | ibid. |
| Oval (tip) | ProMark | "Full bodied and warm tone" | ibid. |
| Round, large (tip) | ProMark | "Produces a full and clear sound" | ibid. |
| Round, small (tip) | ProMark | "Bright tone that's articulate on drums & cymbals" | search text of the same FAQ — **partially UNVERIFIED** |
| Teardrop (tip) | ProMark | "Offers a darker, rich tone" | daddario.com/collections/promark FAQ |
| Taper | ProMark | "The taper (the shoulder of the stick going toward the bead) influences the stick's balance and rebound. A longer taper provides more rear-weight and a faster response, while a shorter taper offers more power and durability." | ibid. |
| Bead | ProMark | used interchangeably with "tip" in the taper definition above | ibid. |
| Hickory | ProMark | "the most common and offers a good balance of strength and flexibility" | ibid. |
| Maple | ProMark | "lighter and great for fast playing" | ibid. |
| Shira Kashi Oak | ProMark | "increased attack and durability" | ibid. |
| Wood vs nylon tip | ProMark | "Wood tips generally produce a warmer sound, while nylon tips have a brighter more articulate sound and added durability" | ibid. |
| tip, neck, shoulder, shaft, butt | retail trade | five-part stick anatomy: "The neck is where the stick begins to taper away from the tip to the apex of the shoulder. The shoulder is where the tapering ends and the uniform diameter of the shaft begins." | thevault.musicarts.com, via search text — **UNVERIFIED** |
| Rute | Vic Firth | "premium birch dowels secured in a birch drumstick handle"; the handle "can also be used for back beats, cross rim work and intricate patterns on the cymbal bell"; "a moveable band that adjusts the effect from crisp to splashy" | vicfirth.com Rute collection, via search text — **UNVERIFIED** |
| Brushes | Vic Firth | offered in "wire … rattan, grass, birch and synthetic" | ibid. — **UNVERIFIED** |
| VicKick Beaters | Vic Firth | available in "felt, wood and fleece"; "each model features a spherical head for a consistent striking surface and provides a distinct level of articulation" | ibid. — **UNVERIFIED** |

### 2.9 Shell, hardware and mechanism terminology

| Term | Vendor | Verbatim definition | Locator |
|---|---|---|---|
| Shell | Yamaha | "The body of the drum." / "Typically made from wood, the shell is the 'body' of a marching snare drum." | Anatomy of a Snare Drum / Marching Snare |
| Counter Hoop | Yamaha | "The rim or hoop that tightens the drumhead." | Anatomy of a Snare Drum |
| Lug Casing | Yamaha | "This part receives the tension rod." | ibid. |
| Tension Rod | Yamaha | "A threaded metal rod that is inserted into the lug casing." | ibid. |
| Snares | Yamaha | "Wire, cable, gut or synthetic materials stretched across the bottom head" | ibid. |
| Snares (marching) | Yamaha | "Synthetic strands or 'guts' that give a snare drum its characteristic buzzy sound." | Marching Snare |
| Snare Strainer | Yamaha | "The mechanism that includes the snare strainer release" | Anatomy of a Snare Drum |
| Snare Strainer Release | Yamaha | "The lever mechanism that engages or disengages the snares" | ibid. |
| Throw Off | Yamaha | "This allows the player to turn the buzzy sound on and off." | Marching Snare |
| Butt Plate | Yamaha | "This part secures the snares on the shell" | Anatomy of a Snare Drum |
| Air Hole / Air Vents | Yamaha | "Allows air to escape the cylinder when the batter head is struck." / "These allow air to escape from inside of the drum." | ibid. / Marching Snare |
| Badge | Yamaha | "The identification plate attached to the shell." | ibid. |
| Suspension Hoop; Top / Bottom Hoop; Tube Posts; Sound Posts; Removable Feet | Yamaha | marching-snare specific parts | Marching Snare |
| Straight / boom / convertible boom-straight stands; tom stands; drum racks; snare stands; thrones | Yamaha | hardware category names | Cymbals and Hardware |

### 2.10 Hand-percussion stroke names

Conga strokes, verbatim, with the published single-letter abbreviations — the notation
library articulation lists copy. Locator: Thomann Online Expert, Congas — First Steps.

| Stroke | Abbrev. | Definition (verbatim) |
|---|---|---|
| Bass | B | "the deepest note of the conga"; hit "the drum with your palm in the centre of the drumhead"; "a low, muffled sound" |
| Open tone | O | "The basic sound of each conga"; striking "the outside edge of the head quickly as if slapping a hot pan on a stove"; "a clear pitch with a resonant tone" |
| Closed slap | S | "slapping the fingers against the head and allowing it to rest there briefly" |
| Open slap | OS | "the loudest note of the conga"; using "only the fingertips"; "slap the drum very briefly to create a penetrating note" |
| Heel | H | "dropping the heel of the palm onto the drumhead creating a soft, muffled tone" |
| Tap | T | a "quiet technique" with "a higher pitch than the heel"; let "your fingers rise from the heel position and strike the drum from a low height" |
| Heel-toe roll | — | heel strokes and taps in rapid alternation |

Conga family names as published: **Conga** (medium, "placed directly in front of the
player"), **Tumba** ("placed to the right"), **Quinto** ("placed between the conga and
the tumba in a triangular formation"). Locator: Thomann, Congas — Arrangement of the
Drums. Requinto, segundo / tres golpes and super tumba are **not** named on the
reachable pages.

Cajon, verbatim. Locator: Thomann Online Expert, Cajon — Playing techniques, which
reproduces Meinl's published cajon method.

| Stroke | Definition (verbatim) |
|---|---|
| Bass tone | "slap the playing surface with your flat hand by simply letting the weight of your arm do what it wants"; struck with flat palm at the centre of the front playing surface (**tapa**) |
| Slap tone | "striking the upper part of the playing surface with the your palm at the top edge of the cajón and the relaxed extended fingers striking the playing surface" |
| High slap tone | "played with the finger tips at the top of the playing surface", "significantly less volume" |
| Playing zone | "the top third of the cajón's playing surface should actually be played" |

Timbale terms (**cascara**, **paila**, **abanico**) were recovered only at search-summary
level; no vendor page carrying LP's own definitions was reachable, because LP publishes
its instructional material as video. Recorded as **UNVERIFIED**: cascara = playing the
metal shell with the stick's shoulder; abanico = a flam-like sweep from rim to head used
as a section cue; paila = a name for the timbale itself. Locator: search summaries of
ipassio.com and rhythmnotes.net. These need a primary source before use.

### 2.11 Orchestral and marching cymbal vendor terminology

| Term | Vendor | Note | Locator |
|---|---|---|---|
| "Flams" | Vic Firth | a **fault** to be avoided: "All edges of the cymbals should touch at the same time, avoiding 'Flams'" | Percussion 101: Crash Cymbals |
| Muffling against the body | Vic Firth | "Touch the cymbals against the body after the crash" | ibid. |
| Torso damping | Thomann | players use "their torso to dampen the sound and control the cymbal decay" | Concert cymbals |
| Basic Crashes / Softer Crashes in the Flat Position | Zildjian | named lesson articulations | Marching Cymbals 101 |
| Chokes in the Flat Position | Zildjian | named articulation | ibid. |
| Hard Prep Crashes | Zildjian | named articulation | ibid. |
| Taps, Zings and Dings | Zildjian | three named articulations grouped in one lesson | ibid. |
| Sizzles; Sizz-Press; Sizz-Suck | Zildjian | three named articulations | ibid. |
| Hi-Hat (flat position) | Zildjian | a hand-cymbal technique, not the instrument | ibid. |
| Garfield Grip | Zildjian | named grip | ibid. |
| Set / Hip Rest / Gumption / Vertical positions; Flips; Lock Style | Zildjian | named carriage positions and transitions | ibid. |
| Thumb roll, shake roll, finger roll | Vic Firth | tambourine rolls: thumb friction on the head, shaking, finger friction | Percussion 101: Tambourine |
| Fist strike; palm strike ("pop"); single- and two-finger playing; knee-and-fist | Vic Firth | tambourine dynamic techniques | ibid. |
| "Wet" sound | Vic Firth | holding the tambourine perpendicular to the floor so jingles vibrate freely | ibid. |
| Head vs shell striking locations | Vic Firth | named tambourine strike sites | ibid. |
| Muffled playing | Vic Firth | "resting the hand on the head" | ibid. |
| Beeswax / spray rosin / silicone / moisture | Vic Firth | friction preparations for thumb rolls | ibid. |
| Glancing blow | Paiste | "When striking the edge of the cymbal use glancing blows or pull back the stick." "Do not hit directly at and 'through' the cymbal." | Usage & Care |
| Glancing blow | Thomann | "playing crash cymbals with a brief glancing blow in which the stick makes a brief angled contact with the cymbal, rather than playing straight through it" | Cymbals — Application |
| Tilt | Thomann | "Tilting a crash cymbal reduces the impact of the stick" | ibid. |
| x-shaped notehead | Thomann | "cymbal notes are usually notated with an x-shaped note head" | Concert cymbals |

---

## 3. Axis mapping

### 3.1 Terms that map cleanly

| Vendor term | Vendor | Axis | Value | Note |
|---|---|---|---|---|
| bell / cup / Kuppe / cloche | Zildjian, Paiste, Meinl, Thomann DE | site | `bell` | four-language concordance |
| bow (as playing zone) | Meinl | site | `bow` | Zildjian and Paiste use "bow" differently — see §4 |
| ride area | Zildjian | site | `bow` | Zildjian's own name for the same zone |
| surface | Paiste | site | `bow` | Paiste's own name for the same zone |
| edge / Rand / bord | Paiste, Meinl, Thomann | site | `edge` | |
| crash area | Zildjian | site | `edge` | Zildjian's own name for the same zone |
| batter head | Remo, Yamaha | site | `head` | |
| resonant head / snare head / snare-side head | Remo, Yamaha | site | `underside` | **`underside` is the KITWARP word for what every head maker calls the resonant head** |
| counter hoop / hoop / top hoop | Yamaha | site | `rim` | |
| shell | Yamaha | site | `shell` | |
| cascara (playing the timbale shell) | LP trade usage | site | `shell` | UNVERIFIED source; the mapping is exact |
| tapa | Meinl / Thomann | site | `head` | the cajon's front plate is its batter surface |
| top third of the playing surface | Meinl / Thomann | position | `perimeter` (approx.) | cajon slap zone |
| centre of the drumhead (bass stroke) | Thomann congas | position | `centre` | |
| outside edge of the head (open tone) | Thomann congas | position | `perimeter` | |
| bead / tip | ProMark | contact | `tip` | **"bead" is the trade word, "tip" the library word; same object** |
| shoulder | ProMark, retail trade | contact | `shank` | **the trade says shoulder; KITWARP and the libraries say shank** |
| butt | retail trade | contact | `butt` | |
| bass (B) | Thomann congas | technique | `bass-tone` | |
| open tone (O) | Thomann congas | technique | `open-tone` | |
| closed slap (S) | Thomann congas | technique + damping | `slap` + `muted` | fingers rest on the head |
| open slap (OS) | Thomann congas | technique + damping | `slap` + `none` | fingers leave the head |
| heel (H) | Thomann congas | technique | `heel` | |
| tap (T) | Thomann congas | technique | `toe` | **same stroke, different name — see §4** |
| bass tone (cajon) | Meinl / Thomann | technique | `bass-tone` | |
| slap tone (cajon) | Meinl / Thomann | technique | `slap` | |
| muffled playing (tambourine) | Vic Firth | damping | `muted` | hand rests on the head |
| torso damping / muffling against the body | Thomann, Vic Firth | damping | `damped` | hand-cymbal equivalent of a choke |
| felt strip; pillow; Moongel; damping ring; head overlay | Thomann | damping | *(no matching value)* | see §5.5 |
| snare strainer release / throw off | Yamaha | mechanism | `wires-on` / `wires-off` | the throw-off is the physical realisation of that axis |
| chick sound | Paiste, Thomann | technique | `chick` | |
| splash sound (hi-hat, pedal) | Thomann | technique | `foot-splash` | |
| tight | Sabian | openness | `tight` | Sabian defines a response quality, KITWARP a gap — see §4 |
| loose | Sabian | openness | `loose` | as above |
| sloshy | Sabian | openness | `open` | "Loose, messy hi-hat sound when open" |
| rute | Vic Firth | implement | `rod` | **"rute" is the German trade word; `rod` is the library word** |
| brushes | Vic Firth | implement | `brush` | |
| felt / wood beater | Vic Firth VicKick | implement | `felt-beater` / `wood-beater` | |
| felt-covered mallets | Thomann | implement | `mallet-soft`..`mallet-hard` | vendor gives no hardness grades on reachable pages |
| dark (product-line name) | Meinl, Sabian, Evans | voicing | `dark` | |
| thumb roll / shake roll / finger roll | Vic Firth | ornament | `roll` | three named production methods collapse to one value |
| crescendos / swells | Meinl, Thomann | ornament | `crescendo` / `swell` | |
| wash | Sabian, Thomann | ornament | `wash` | vendors define wash as a sustain property, not a stroke — see §4 |
| rivets / sizzle | Zildjian, Sabian | instrument | `sizzle-ride` | the instrument value encodes a fitted accessory |
| crash-ride | Meinl | instrument | `crash-ride` | |
| stack | Meinl, Thomann | instrument | `stack` | |
| china | Sabian, Meinl, Thomann | instrument | `china` | |
| splash | Sabian, Meinl, Thomann | instrument | `splash` | |
| bell (cymbal type) | Meinl, Thomann DE | instrument | `bell` | collides with site `bell`, correctly — see §4 |

### 3.2 Terms that fit NO axis

Per the brief, the most valuable rows. Five groups.

**Group 1 — cymbal build parameters that determine identity but are not performance.**
`profile`, `taper`, `weight`, `thickness`, `size`, `bow`/`curvature` (Paiste sense),
`lathing`, `tonal grooves`, `hammering` (random / symmetrical / hand / machine),
`sandblasting`, finishes (`brilliant`, `natural`, `raw`, `dark`, `smoked bronze`), alloys
(`B8`, `B10`, `B12`, `B20`, `MS63`, `FX9`).

These fit no KITWARP axis. They are neither instrument identity (a B20 crash and a B8
crash are both `crash`) nor `voicing` as currently defined, which is documented as "kit
or miking variant". Yet libraries ship them as distinct kit pieces and name the patch
after them. **This is the bucket's headline finding: either an axis is missing, or
`voicing` must be widened from "kit or miking variant" to "build or model variant of the
same instrument".**

**Group 2 — sound-character adjectives.** All thirty Sabian glossary terms, plus Paiste's
`color / range / mix / response intensity / feel` and Evans's `attack / tone / sustain /
durability` spectra. These are retrieval facets for choosing a product, not properties of
a struck event. Three have nevertheless leaked into pivot-shaped vocabulary: `dark` is a
KITWARP `voicing` value, `dry` is a common library kit-piece qualifier, and `tight` /
`loose` are KITWARP `openness` anchors. **The leak should be deliberate: either the
sound-character vocabulary is out of scope entirely, or it is a named axis. Half-adopting
three of thirty is the current state.**

**Group 3 — hardware parts that are never struck.** `lug casing`, `tension rod`, `badge`,
`air hole` / `air vent`, `butt plate`, `tube posts`, `sound posts`, `removable feet`,
`bearing edge`, `collar`, `snare bed`, stand and rack names. Correctly unmapped: they are
construction, not contact sites. `bearing edge` and `collar` deserve a note because they
sound like sites and are not — the bearing edge is where the shell meets the head, never a
strike location.

**Group 4 — player carriage and grip.** Zildjian's `Garfield Grip`, `Set`, `Hip Rest`,
`Gumption`, `Vertical`, `Flips`, `Lock Style`; Vic Firth's `knee-and-fist`. These describe
the performer's body, not the instrument or the stroke. KITWARP carries `limb` on the
layout slot; none of these fit there either. Out of scope for a pivot term, but recorded
because marching and orchestral libraries may use them as patch names (**UNVERIFIED** — no
library articulation list was inspected in this bucket; bucket 05 owns that check).

**Group 5 — a genuine orphan.** `Drumbal` (Meinl): "cymbal which is used on a drum for
completely unique sound effects", with a handle. It is an instrument, so in principle it
belongs on the `instrument` axis, but it is neither kit cymbal nor aux percussion — it is
a cymbal deliberately laid on a drumhead, an instrument whose identity depends on being
coupled to another instrument. **Nothing in the axis model expresses coupling.**

---

## 4. Conflicts and false friends

**`bow`.** Three incompatible senses. Meinl: the playing zone between bell and edge.
Paiste: "Curvature or Bow", the downward curve produced by hammering — a shape, not a
zone. Zildjian: "The profile or 'bow' of a cymbal", explicitly a synonym for profile.
KITWARP's `site.bow` follows Meinl. Locators: Meinl Wiki; Paiste Cymbal Anatomy;
Zildjian FAQ.

**The zone triple itself.** "Bow / edge / bell" is not the trade standard the libraries
imply. Zildjian's published zone names are **ride area** and **crash area**; Paiste's is
**surface**. A converter reading a Zildjian-derived source must know that "ride area" and
"bow" are the same site.

**`bell`.** Site (the raised centre of any cymbal) versus instrument (Meinl's and
Thomann's heavy small effect cymbal, "Bell-Becken") versus Paiste's classification
parameter "Bell Character". KITWARP already mints `bell` on both `site` and `instrument`;
the vendor evidence confirms this collision is real trade usage, not a modelling error.

**`cup`.** Zildjian says "bell or cup"; everyone else says bell. German `Kuppe` descends
from the same idea. A source spelling it "cup" is Zildjian-flavoured.

**`flam`.** In KITWARP and every rudiment tradition, a deliberate grace-note ornament. In
Vic Firth's hand-cymbal pedagogy it is a **defect**: "All edges of the cymbals should
touch at the same time, avoiding 'Flams'". Same word, opposite valence. Locator: Vic
Firth, Percussion 101: Crash Cymbals.

**`hi-hat`.** The instrument, versus Zildjian's marching hand-cymbal technique "Hi-Hat
(flat position)" — one cymbal struck against another held flat. Locator: Zildjian A&E,
Marching Cymbals 101.

**`sizzle`.** Three senses. Sabian sound descriptor: "A slight buzzing or sustained
shimmer (especially when rivets are used)". Zildjian product: rivets sold as "Sizzle
Rivets". Zildjian marching articulation: "Sizzles", "Sizz-Press", "Sizz-Suck" — a sliding
contact between two hand cymbals. KITWARP mints only `sizzle-ride` on `instrument`, which
covers the first two and not the third.

**`dead`.** Sabian sound descriptor: "Very short sustain, no lingering sound" — a property
of a cymbal. KITWARP `technique.dead` — a dead stroke, a property of a stroke. Unrelated
meanings sharing a spelling.

**`dry`.** Sabian: "shorter sustain, muted wash that emphasizes stick definition". Meinl:
hole cut-outs "dry the cymbal out — meaning they reduce the ring". Paiste and Evans: a
response-intensity pole. All three are instrument properties, none a playing state, yet
library naming routinely turns "Dry" into an articulation qualifier alongside real
techniques.

**`taper`.** Cymbal taper is the thickness change from bell to edge (Zildjian, Paiste,
Sabian). Stick taper is the narrowing from shaft to bead (ProMark). Same word, two
different objects, both in scope for this project.

**`profile`.** Sabian: "the shape and height of a cymbal as you look at it from the side".
Zildjian: a synonym for bow. No conflict of meaning, only of naming.

**`wash`.** Sabian: "the characteristics of sound following the attack … the sound during
the sustain". Thomann: "the darker underlying roar that can build up when playing a ride
cymbal". Both define it as a sustain property. KITWARP places `wash` on the `ornament`
axis, whose stated purpose is "grace or multi-stroke qualifier, with an attack count".
**A wash has no attack count.** Either `wash` is on the wrong axis, or the ornament axis
carries two different kinds of thing. Flagged for reconciliation.

**`ping`.** Thomann and Meinl use it for the bright stick sound on the ride bow; Paiste's
attack scale runs "Pronounced/Pingy to Spread/Washy". It is a sound quality. KITWARP's
`technique.ping-shot` is a stroke. No vendor source reached in this bucket uses
"ping-shot", and none uses "gok-shot" or "stick-shot" either. **These are library words,
not trade words** — a useful negative finding for a bucket whose job is to say where the
library spellings came from.

**`tight` / `loose`.** Sabian defines them as response and feel qualities ("Compact, clean
and direct response"; "Open, airy feel"). KITWARP uses them as named anchors on a 0.0-1.0
hi-hat aperture scale. The referents are adjacent but not identical: Sabian's "tight" can
describe a closed hi-hat *or* a focused crash.

**`tap` / `toe` / `touch`.** The same quiet conga stroke. Thomann and Meinl publish it as
**Tap (T)**; KITWARP mints it as `toe`; the wider conga literature calls it *touch* or
*toque de punta*. Locators: Thomann, Congas — First Steps; `vocabulary/axes.json`;
Spanish naming from search summaries only — **UNVERIFIED**.

**`bead` / `tip`, `shoulder` / `shank`.** Straight vendor-to-library concordance, worth
stating plainly because it explains a library spelling: the stick makers say **bead** and
**shoulder**; the sample libraries and KITWARP say **tip** and **shank**. Locator:
daddario.com ProMark FAQ, whose taper definition uses "shoulder" and "bead" in one
sentence.

**`resonant` / `underside`.** Head makers say **resonant head** or **snare-side head**;
KITWARP's `site` axis says `underside`. Same surface.

**`throw-off` / `strainer` / `wires-off`.** Yamaha names the part (`snare strainer
release`, `throw off`); KITWARP names the resulting state (`wires-off`). The vendor word
is the mechanism, the pivot word is its position.

**Closed slap is not an openness distinction.** The conga `closed slap` / `open slap` pair
looks like `openness` and is not: the difference is whether the fingers remain on the head
after contact, which is `damping`. Recorded so the reconciliation pass does not overload
the openness axis, which is documented as the hi-hat aperture scale.

---

## 5. Gaps against vocabulary v0.1

### 5.1 `instrument` — cymbal types the trade names and v0.1 does not

From Meinl's wiki and Thomann's German cymbal guide, both reached: `flat-ride` (a ride
with no bell — an identity, not a voicing), `china-ride`, `trash-crash`, `trash-splash`,
`trash-china`, `drumbal`. From Sabian: `effect cymbals` as a grouping term. Not found in
any reached vendor source but present in wider trade usage and worth another bucket's
check: `swish`, `pang`, `cup chime`.

v0.1 has `crash-ride` but not `china-ride`; has `stack` but no value for a holed or trash
cymbal, which is a different construction from a stack and a different sound. `mini-china`
and `mini-hihat` exist in v0.1 with no vendor source found in this bucket —
**UNVERIFIED against vendor literature**; they may be library-only coinages.

### 5.2 `instrument` — drums the catalogues name

`gong drum` / gong bass drum, `piccolo snare`, `concert tom` (single-headed), `timbale`,
`marching snare`, `conga` / `quinto` / `tumba`, `bongo`, `cajon`, `suspended cymbal`,
`hand cymbals` (pairs). v0.1 reserves the families (`perc.hand`, `orch`, …) but mints none
of these. `octoban` is minted and matches trade usage — deep, small-diameter,
single-headed toms, also sold as "tube toms".

Two are identity decisions rather than vocabulary gaps and belong to the owner: whether a
**piccolo snare** is its own instrument or a `voicing` of `snare`, and whether a **concert
tom** is its own instrument or a `tom` whose resonant head is absent — a state no current
axis can express.

### 5.3 `technique` — strokes the vendors publish that v0.1 lacks

`tap` (conga; distinct from `heel`, and not the same as a `ghost` dynamic — see §4);
`high tone` / `high slap tone` (cajon, a third named stroke beyond bass and slap);
`thumb roll`, `shake roll`, `finger roll` (Vic Firth tambourine — three production methods
a library ships as three patches, all collapsing to `ornament=roll` today); `zing`, `ding`,
`sizz-press`, `sizz-suck`, `hard prep crash` (Zildjian hand cymbals); `glancing blow`
(Paiste and Thomann both publish it as the correct way to strike a crash edge — arguably
the default rather than a named technique).

v0.1's `technique` has `thumb` but not a thumb roll; the tambourine thumb roll is a
friction roll, not a thumb strike.

### 5.4 `implement` — gaps

- **Tip material is carried nowhere.** ProMark distinguishes wood from nylon tips
  explicitly ("nylon tips have a brighter more articulate sound"), and every library ships
  them as separate sounds. `implement` has `stick` and `jazz-stick`; `contact` has `tip`.
  Neither carries the tip's material. A real hole.
- `fleece` beater (Vic Firth VicKick) has no value; v0.1 has felt, wood, plastic, rubber,
  superball.
- Brush material is undifferentiated: the trade sells wire, rattan, grass, birch and
  synthetic brushes as different sounds; v0.1 has one `brush`.
- The rute's "moveable band that adjusts the effect from crisp to splashy" is a
  continuously variable implement state with no home in the model.
- Mallet hardness: v0.1's three-step soft/medium/hard was not corroborated by any reached
  vendor source; Thomann says only "felt covered mallets". Vendor hardness scales exist but
  were not reached in this bucket.

### 5.5 `damping` — the named dampers

v0.1 has `none, muted, damped, towel, gated`. The trade names, all from one reached page:
`felt strip` (bass drum, clamped at the bearing edge), `damping pillow`, `foam rail`,
`Moongel` / gel pad, `damping ring` / `control ring` / `O-ring`, `head overlay`,
`duct tape`, `Snareweight`, `Mini Muff`. Libraries routinely ship "Kick w/ Pillow",
"Snare w/ Moongel" and "Tom Ringed" as separate articulations.

Note the asymmetry: v0.1's `towel` is one specific overlay damper elevated to a vocabulary
value, while `felt strip` and `pillow` — far more common in both real kits and libraries —
have none. Either the damper *device* is a modelled dimension or it is not; `towel` alone
is inconsistent.

Note also that `gated` is a production process, not a physical damper, and sits in the
same axis as `towel`. No manufacturer sells or names a gate. **UNVERIFIED** whether
`gated` belongs on this axis at all.

### 5.6 `voicing` and the missing build axis

See §3.2 Group 1. The cymbal build vocabulary — alloy, hammering pattern, lathing, finish,
weight, profile — is a large, well-documented, fully primary-sourced vendor terminology
with nowhere to go in the current model, while `voicing` already carries `dark`, a term
that in vendor use is simultaneously a finish (Meinl "Dark Finish"), a sound-character
pole (Sabian; Paiste "Color") and a product-line name.

### 5.7 `site` — a possible gap

Nothing reached in this bucket names a cymbal **underside** strike as a vendor term,
although v0.1 mints `underside`. Conversely, the timbale **shell** strike (cascara) and
the cajon **corner** are named in the trade and map to `shell` and to
`position=perimeter`. No vendor source reached names the hi-hat's **bottom cymbal** as a
separate strike site, which some libraries do ship.

---

## 6. Self-critique (round C)

**What this bucket did not reach, and what each would have added.**

1. **The Internet Archive, entirely.** Both `curl` and WebFetch are blocked from
   `web.archive.org` here. Every route the brief suggested for older catalogues therefore
   failed. This is the largest hole and it is environmental, not a research failure; it
   should be recorded as an environment fact for every future round-2 worker.

2. **The pre-1970 catalogues at drumarchive.com** (Slingerland 1928, 1936, 1950, 1968;
   Ludwig 1922 and 1994). This is the era the brief singles out as mattering most, because
   it names the physical distinctions with no reference to any note number — "sock cymbal",
   "Chinese crash", "tunable tom-tom", "traps". They were located but not fetched: the
   search budget ran out before the fetch phase reached them, and round-B time went to live
   vendor pages certain to answer. **Named single most authoritative source not obtained:**
   `https://www.drumarchive.com/slingerland/slingerland1950.pdf` and
   `https://www.drumarchive.com/ludwig/1994_ludwig.pdf`, both direct-linked and confirmed
   to exist.

3. **Latin Percussion's own instructional material.** LP publishes technique as video (LP
   Rhythmology) and its `/pages/education` path 404s. The English conga stroke names every
   library uses — open, bass, slap, muff, heel-toe — are LP printed-booklet vocabulary in
   origin, and no LP-published text was reachable. The conga stroke table in §2.10 therefore
   rests on Thomann, a retailer (authority C), not on the manufacturer. The LP booklet would
   raise that whole table one authority level and settle the `tap` / `toe` / `touch` naming
   question in §4.

4. **Vater** (site returned a bare shell; `/pages/faq` HTTP 503), **Aquarian** (search text
   only), **Toca** (not reached at all), **DW hardware pages**, **Pearl support** (403),
   **Sweetwater's category tree** (403). Vater and Aquarian would mainly corroborate ProMark
   and Evans. Toca is the real loss: it is the third hand-percussion vendor and would test
   whether LP's stroke names are trade-wide or house style.

5. **Trade press.** Neither the Modern Drummer lexicon nor the DRUM! drumstick article could
   be retrieved (no canonical URL found; empty response body). The bucket brief names both.
   Trade-press glossaries matter because they mediate between vendor copy and player speech,
   and they are where "rim click" versus "cross-stick" gets argued about.

6. **The non-English registers were cut short.** German is represented by Thomann's own
   guides (`Kuppe`, `Rand`, `Bogen`, `Loch`, `Profil`). French appears only as unverified
   search text: four French glossaries plus the **Office québécois de la langue française**
   terminology record — a state terminology authority and the highest-authority French source
   found — went unfetched when the search budget ended. Spanish and Italian searches never
   ran. For a bucket about why words are spelled the way they are, the missing Spanish is a
   real gap: conga and timbale vocabulary is Spanish in origin (`tono abierto`, `tono
   ahogado`, `toque de punta`, `cascara`, `paila`, `abanico`) and only anglicised forms are
   documented here.

7. **Methodological caveat.** Several rows in §2 are marked UNVERIFIED because they come
   from search-result summaries rather than a page fetched directly. They are kept and
   labelled rather than dropped, because they name real vendor pages a later pass can fetch.
   No unverified row should be promoted into `data/` as-is.

8. **What I would do differently.** The search budget was the binding constraint, not the
   fetch budget. A future worker should spend searches only to *discover URLs*, never to
   *read content*, and should switch to WebFetch as soon as a vendor's education-section
   index is in hand — Paiste, Thomann and Zildjian all publish machine-readable section
   indexes that yield ten or more sub-page URLs for a single call.

---

## Provenance summary

| Field | Value |
|---|---|
| Observer | worker `bucket-06-vendor-glossaries` |
| Method | WebSearch breadth pass (20 searches), then WebFetch extraction |
| Collection date | 2026-09-06 |
| Sources | 58 candidates registered, 26 reached; see §1 |
| Confidence | High for §2 rows carrying a fetched locator; explicitly marked UNVERIFIED otherwise |
| Licence verdict | All content is vendor marketing and education copy, all rights reserved. Quoted definitions here are short excerpts held for research. **None of this text may be shipped into `data/`**: vendor terminology must be re-derived as project-owned slugs citing the vendor page as source, never copied. |
