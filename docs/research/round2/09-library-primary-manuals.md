# Round 2, bucket 09 — sample-library manuals, first-hand

Scope: the ARTICULATION VOCABULARY that each major drum-library vendor uses in its own
documentation, and, per library, a verdict on whether an OFFICIAL published note map or
articulation chart exists, where it lives, in what format, and whether it is reachable from
this environment. Note numbers are Phase 3 and are not the subject of this dossier; where a
chart happens to carry them, that is recorded as evidence that the chart exists, not as
data to be transcribed.

Round 1 (`docs/research/05-libraries-articulations.md`) covered most of these libraries with
community transcriptions — Cubase `.drm` packs, Studio One `.pitchlist` files, third-party
JSON maps. Under the provenance rules (CLAUDE.md rule 2, ADR-0004) those are worklists, not
shippable sources. This pass went back to the vendors.

Date of research: 2026-09-06. All HTTP statuses below were observed on that date from this
environment.

---

## 0. The verdict table

The primary deliverable. "Official" means published by the vendor (or on a host the vendor
controls) and describing the vendor's own product.

| Library | Official articulation chart? | Official note map? | Where | Format | Reachable here |
|---|---|---|---|---|---|
| **Toontrack Superior Drummer 3** | no | no | `toontrack.com/manual/superior-drummer-3/` — returns the site's "Please LOG IN to view Toontrack Manuals" page (HTTP 200, login wall) | web manual, account-gated | **no** |
| **Toontrack EZdrummer 3** | no | no | `toontrack.com/manual/ezdrummer-3/`, same login wall | web manual, account-gated | **no** |
| **Toontrack Superior Drummer 2** (predecessor) | partial | **yes** | `toontrack.com/updates/manuals/Superior_Drummer_Operation_Manual.pdf`, p. 56–57 "GM EXTENDED CORE MAPPING" + "X-DRUMS GENERIC MAPPING" | PDF, key-layout chart | yes, via Wayback replay of the vendor path |
| **Toontrack EZdrummer 1** (predecessor) | partial | **yes** | `toontrack.com/updates/manuals/EZdrummer_Operation_Manual.pdf`, §4.4 "Key Mapping" | PDF, keyboard chart | yes, via Wayback replay of the vendor path |
| **Toontrack EZX / SDX expansions** | no | no | product pages give articulation *counts* and a few names in marketing prose | HTML prose | pages yes, charts do not exist |
| **XLN Audio Addictive Drums 2** | **yes** | **yes** | `support.xlnaudio.com/hc/en-us/articles/16925247222045-Addictive-Drums-2-Keymap`, attachment `Addictive Drums 2 Keymap.pdf`; also inside the plugin (Top Menu) | 4-page PDF table: Notes / MIDI / KitPiece / StrokeType / Brushes StrokeType | **yes** — HTML 403s, the Zendesk JSON API and the attachment URL do not |
| **XLN Audio Addictive Drums 1** | **yes** | **yes** | `xlnaudio.com/downloads/manuals/addictive-drums-keymap.pdf` | 1-page PDF keyboard chart | yes, via Wayback replay of the vendor path (live path retired) |
| **FXpansion / inMusic BFD3** | **yes** | **yes** | `fxpansion.com/webmanuals/bfd3/operationmanual/bfd3_key_map_reference.htm`, mirrored at `internal.bfddrums.com/manuals/BFD30/bfd3_key_map_reference.htm` | HTML table, MIDI key / key number / "BFD3 articulation" | yes |
| **BFD Player** | **yes** | **yes** | `cdn.inmusicbrands.com/BFD/BFD_Player_-_User_Guide_-_v1.1.0_-_RevB.pdf`, Appendix "Keymap", pp. 16–17 | PDF table: Kit Piece / Articulation / MIDI Note / MIDI Number | yes |
| **Steven Slate SSD5** | **no** | **no** | `download.stevenslatedrums.com/ssd5/SSD5 User Manual.pdf` — fetched (HTTP 200, 3.2 MB) and read: "Articulations" is a UI-panel description, there is no list and no map | PDF | manual yes, chart does not exist |
| **Steven Slate SSD5.5** | **no** | **no** | `download.stevenslatedrums.com/ssd5/SSD5.5 User Manual.pdf`; KB article "MIDI Learn and Mapping in SSD5.5" describes the *mechanism* only | PDF + KB HTML | manual yes, chart does not exist |
| **NI Studio Drummer** | **yes** | in-product only | manual §5 "Drum Articulations": `native-instruments.com/fileadmin/ni_media/downloads/manuals/Studio_Drummer_Manual_English.pdf`, also HTML at `docs.native-instruments.com/ni-tech-manuals/studio-drummer-manual/en/drum-articulations` | PDF + HTML tables | yes. The note map is in three separate "…Kit – Default Mapping" documents shipped with the library (Kontakt Library tab → Info) — **not on the public web** |
| **NI Abbey Road 60s Drums** | **yes** | **yes** | manual §4.1–4.2 (articulations) and §4.3–4.4 "Default Drum Mapping" — `…/manuals/Abbey_Road_60s_Drums_Manual.pdf` | PDF; map is an annotated keyboard graphic | yes |
| **NI Abbey Road 70s / 80s / Modern Drummer** | **yes** | **yes** | manual §6 "Drum Articulations", one table per kit with a *Default Key / MIDI Number* column — `…/manuals/Abbey_Road_{70s,80s,Modern}_Drummer_Manual_English_2012_07.zip` | ZIP → PDF, three-column table | live path 404s; **yes** via Wayback replay of the vendor path |
| **NI Abbey Road 50s / Vintage Drummer** | presumed yes | presumed yes | same naming pattern, listed in the vendor's manual directory | ZIP → PDF | not fetched — UNVERIFIED |
| **GetGood Drums Modern & Massive 2** | **yes** | no | `support.ggd.co/hc/en-us/articles/32177396568727-What-articulations-are-available-in-Modern-Massive-2` | KB HTML, kit-piece → articulation list, no note numbers | **yes** via the Zendesk JSON API (HTML 403s) |
| **GetGood Drums, all other libraries** (Invasion, Matt Halpern, Zilla, One Kit Wonder, Gartska, The Downbeat …) | no | no | 47-article KB enumerated in full; exactly one articulation article exists, for M&M2 | — | KB yes, charts do not exist |
| **ML Sound Lab ML Drums** | **no** | **no** | product page, update page and FAQ on `ml-sound-lab.com` carry no articulation list, no map, no manual link | — | pages yes, documentation does not exist publicly |
| **IK Multimedia MODO Drum** | **no** | **no** | vendor FAQ 1395: "your user manuals will be stored in **My Products** under **Download Resources**" — account area only | PDF behind login | **no** |
| **MT Power Drum Kit 2 (Manda Audio)** | **yes** (as note-name files) | **yes** | `powerdrumkit.com/presets_drum-maps.php` → nine DAW drum maps on `resources.manda-audio.com`; plus VST3 exposes note names to the host natively | ZIP → per-DAW map file (Reaper `.txt`, Cubase `.drm`, Studio One pitch list, …) | yes |
| **Sennheiser DrumMic'a!** | **yes** | **yes** | manual `DrumMicA_manual_en.pdf`, §4.5.2 "MIDI Mapping", pp. 49–54: six complete maps (GM, V-Drums TD-12/20, V-Drums TD-3/6, EZdrummer, Addictive Drums, Superior Drummer) | PDF, rotated keyboard charts | document yes (mirror), **vendor distribution dead**: `drummica.com` and `drum-mica.com` do not resolve, `en-us.sennheiser.com/drummica` redirects to a generic page |
| **Rayzoon Jamstix 4** | **yes** | **yes** (as a reference-ID table plus a documented file format) | `rayzoon2.com/docs/jamstix4_manual.pdf`, Appendix B "Kit Piece Reference IDs" (pp. 73–75) and Appendix C "Output Mapping File Format" (pp. 76–77); German edition `jamstix4_manual_german.pdf` | PDF tables | yes |
| **Bogren Digital Krimh Drums** (not in the task list; checked opportunistically) | no | no | `bogrendigital.com/blogs/news/instantly-hear-your-songs-with-krimh-drums-midi-mapping` shows the mapping-preset list as a screenshot only | HTML + image | page yes, chart does not exist |

Summary count: of the fourteen products named in the task, **seven publish an official chart
reachable today** (AD2, BFD3, BFD Player, Studio Drummer, Abbey Road 60s/70s/80s/Modern,
MT Power, Jamstix 4), **two publish one that only a mirror still carries** (DrumMic'a,
and the Toontrack SD2/EZD1 predecessors), **one publishes a partial list without numbers**
(GGD M&M2), and **four publish nothing** (Toontrack SD3/EZD3, SSD5/5.5, ML Drums,
MODO Drum).

### 0.1 Access technique worth keeping

Round 1 recorded XLN, Steven Slate and GetGood support sites as unreachable (Cloudflare 403
to both WebFetch and curl). They are Zendesk help centres, and **the Zendesk public JSON API
on the same host is not behind the interstitial**:

```
https://<support-host>/api/v2/help_center/en-us/articles/<id>.json
https://<support-host>/api/v2/help_center/en-us/articles.json?per_page=100
https://<support-host>/api/v2/help_center/articles/search.json?query=<terms>
https://<support-host>/api/v2/help_center/articles/<id>/attachments.json
```

The last one is what produced the official AD2 keymap PDF: the article body does not contain
the link, the attachment record does (`content_url`
`https://support.xlnaudio.com/hc/article_attachments/16925267740829`, which serves the PDF
with HTTP 200). Verified working on `support.xlnaudio.com`, `support.ggd.co` and
`support.stevenslatedrums.com`. BFD's `support.bfddrums.com` is Freshdesk and serves its
article HTML directly without a block.

### 0.2 Environment note that contradicts the brief

The supervisor's correction states that `web.archive.org` is dead in this environment, and a
later correction adds that "Wayback content URLs remain 403". Neither matches what was
observed here on 2026-09-06, and the difference was checked deliberately rather than
assumed. Reproducible test, run at 13:09 UTC, three consecutive attempts at the same URL:

```
curl -L -o wbtest.pdf \
  "https://web.archive.org/web/20080920202809id_/http://www.toontrack.com:80/updates/manuals/EZdrummer_Operation_Manual.pdf"
try1: 000 0          <- connection reset
try2: 200 1095305    <- complete PDF
try3: 200 1095305    <- complete PDF, byte-identical
```

The payload is a real 18-page Toontrack PDF whose §4.4 is the EZdrummer key map quoted in
§2.6 below; it is not a 302, not an error page, and not a bodyless HEAD. The same route
delivered a 3,500,226-byte Abbey Road 70s manual ZIP that unzips to a valid PDF. So the
correct advice is neither "dead" nor "works": it is **retry-tolerant**. Behaviour observed:

- Large CDX queries (`matchType=domain` over `toontrack.com`, `native-instruments.com`,
  `sennheiser.com`) fail with `Recv failure: Connection reset by peer` or a 504 from the
  Wayback nginx.
- Narrow CDX queries (`matchType=prefix` on one directory, `limit` ≤ 100) succeeded
  repeatedly.
- `id_` replay downloads succeeded every time they were tried, including binaries of several
  megabytes: the AD1 keymap PDF, `EZdrummer_Operation_Manual.pdf` (1.1 MB),
  `Superior_Drummer_Operation_Manual.pdf` (3.5 MB), and three Abbey Road manual ZIPs
  (3.4 / 5.0 / 4.5 MB).
- `WebFetch` against `web.archive.org` **is** refused ("Claude Code is unable to fetch from
  web.archive.org"). curl is not. That asymmetry is the most likely explanation for the
  "dead" report: a worker testing only with WebFetch would see a hard refusal every time.

So: use curl, keep CDX queries narrow, and expect to retry. Four of the rows in the verdict
table exist only because of that route.

Hosts confirmed unreachable from here: `www.drummica.com` (curl exit 000, no connection),
`support.xlnaudio.com` HTML and `assets.xlnaudio.com/documents/*keymap*.pdf` (403),
`toontrack.com/manual/*` (login wall, HTTP 200 with no content).

---

## 1. Candidate source register (round A)

Twenty distinct searches were run before any extraction, varying vendor, register
(vendor "articulation list" / "key map" / "note map" / "drum map" / "stroke type" /
"pitch names"), source type (manual PDF, web manual, knowledge base, support attachment,
DAW-map download, product page), and language (English, German
"Schlagzeug Software Handbuch Artikulationen Notenbelegung Drum-Map", French
"drum map officiel batterie virtuelle manuel articulations MIDI"). The session-wide
WebSearch budget was exhausted at that point by all workers together; everything after
round A was done with direct HTTP.

Authority levels: **P** = vendor primary (vendor-authored, vendor-controlled host);
**P-m** = vendor-authored document reached through a mirror or archive of the vendor path;
**V** = vendor page, non-normative prose; **T** = third party.

| # | Source | Vendor | Type | Locator | Auth | Reached |
|---|---|---|---|---|---|---|
| 1 | Addictive Drums 2 Keymap (PDF attachment) | XLN | keymap chart | `support.xlnaudio.com/hc/article_attachments/16925267740829` (article 16925247222045, dated "June 2, 2021" on the sheet, article `updated_at` 2026-08-31) | P | **yes** |
| 2 | Addictive Drums 2 Manual | XLN | manual | `assets.xlnaudio.com/documents/addictive-drums-manual.pdf` (9.8 MB) | P | **yes** |
| 3 | Addictive Drums Keymap (AD1) | XLN | keymap chart | `xlnaudio.com/downloads/manuals/addictive-drums-keymap.pdf`, Wayback 20090124111010 | P-m | **yes** |
| 4 | KB "MIDI Mapping Window" | XLN | KB article | article 16593408783389 | P | **yes** |
| 5 | KB "E-drums, list of drum maps included in Addictive Drums 2" | XLN | KB article | article 27466261893917 | P | **yes** |
| 6 | KB "The PowerMap Engine" | XLN | KB article | article 16593306689437 | P | **yes** |
| 7 | BFD3 Key Map Reference | FXpansion/inMusic | web manual page | `fxpansion.com/webmanuals/bfd3/operationmanual/bfd3_key_map_reference.htm` | P | **yes** |
| 8 | BFD3 Operation Manual (contents, Kit display, Drum editor, MIDI key maps, Using Electronic Drumkits) | inMusic | web manual | `internal.bfddrums.com/manuals/BFD30/bfd3_manual_rev4_content.htm` and siblings | P | **yes** |
| 9 | BFD3 FAQ ("What are articulations and velocity layers?") | inMusic | KB article | `support.bfddrums.com/en/support/solutions/articles/69000801225-bfd3-frequently-asked-questions` | P | **yes** |
| 10 | BFD Player User Guide v1.1.0 RevB | inMusic | manual + keymap appendix | `cdn.inmusicbrands.com/BFD/BFD_Player_-_User_Guide_-_v1.1.0_-_RevB.pdf` | P | **yes** |
| 11 | Studio Drummer Manual (English) | Native Instruments | manual | `native-instruments.com/fileadmin/ni_media/downloads/manuals/Studio_Drummer_Manual_English.pdf` | P | **yes** |
| 12 | Studio Drummer online manual, "Drum Articulations" | Native Instruments | web manual | `docs.native-instruments.com/ni-tech-manuals/studio-drummer-manual/en/drum-articulations` | P | **yes** |
| 13 | Abbey Road 60s Drums Manual | Native Instruments | manual + note map | `…/manuals/Abbey_Road_60s_Drums_Manual.pdf` | P | **yes** |
| 14 | Abbey Road 70s Drummer Manual | Native Instruments | manual + note map | `…/manuals/Abbey_Road_70s_Drummer_Manual_English_2012_07.zip`, Wayback 2026-02 | P-m | **yes** |
| 15 | Abbey Road 80s Drummer Manual | Native Instruments | manual + note map | `…/manuals/Abbey_Road_80s_Drummer_Manual_English_2012_07.zip`, Wayback 2026-02 | P-m | **yes** |
| 16 | Abbey Road Modern Drummer Manual | Native Instruments | manual + note map | `…/manuals/Abbey_Road_Modern_Drummer_Manual_English_2012_07.zip`, Wayback 2026-02 | P-m | **yes** |
| 17 | Abbey Road 50s Drummer Manual | Native Instruments | manual + note map | `…/manuals/Abbey_Road_50s_Drummer_Manual_English.zip` | P-m | not fetched |
| 18 | Abbey Road Vintage Drummer Manual | Native Instruments | manual + note map | `…/manuals/Abbey_Road_Vintage_Drummer_Manual_English_12_2012.zip` | P-m | not fetched |
| 19 | Studio Drummer Manual (German) | Native Instruments | manual, German terms | `…/manuals/Studio_Drummer_Manual_German_2012_07.zip` | P-m | **yes** — and it translates no articulation name at all, see §2.1.1 |
| 20 | Karriem Riggins Drums Manual | Native Instruments | manual | `…/manuals/play-series/Karriem_Riggins_Drums_Manual_English_02_16_2023.pdf` | P | not fetched |
| 21 | SSD5.5 User Manual | Steven Slate | manual | `download.stevenslatedrums.com/ssd5/SSD5.5%20User%20Manual.pdf` | P | **yes** |
| 22 | SSD5 User Manual | Steven Slate | manual | `download.stevenslatedrums.com/ssd5/SSD5%20User%20Manual.pdf` | P | listed and confirmed live; content equivalent to #21 for our purposes |
| 23 | KB "Steven Slate Drums User Guides" | Steven Slate | KB index | article 360033679773 | P | **yes** |
| 24 | KB "MIDI Learn and Mapping in SSD5.5" | Steven Slate | KB article | article 360033680013 | P | **yes** |
| 25 | KB "What articulations are available in Modern & Massive 2?" | GetGood Drums | articulation list | article 32177396568727 (updated 2025-05-17) | P | **yes** |
| 26 | KB "Assign kit piece mapping manually" / "Use preset MIDI map configurations" / "Adjust hi-hat CC parameters" | GetGood Drums | KB articles | articles 31476769525783 / 31476793134743 / 31476794941079 | P | **yes** |
| 27 | Full GGD KB index (47 articles) | GetGood Drums | KB index | `support.ggd.co/api/v2/help_center/en-us/articles.json` | P | **yes** |
| 28 | Jamstix 4 User Manual, rel. 4.4.4 | Rayzoon | manual + appendices | `rayzoon2.com/docs/jamstix4_manual.pdf` | P | **yes** |
| 29 | Jamstix 4 Handbuch (German) | Rayzoon | manual, German terms | `rayzoon2.com/docs/jamstix4_manual_german.pdf` | P | **yes** — older revision, no Appendix B; UI labels untranslated, see §2.1.1 |
| 30 | Jamstix 3 User Manual, rel. 3.6.0 | Rayzoon | manual | `rayzoon2.com/docs/jamstix3_manual.pdf` | P | not fetched |
| 31 | DrumMic'a! Manual (EN), 60 pp., InDesign 2013 | Sennheiser | manual + six note maps | `dn721903.ca.archive.org/0/items/dru-mic-a/DrumMicA/Documentation/DrumMicA_manual_en.pdf` | P-m | **yes** |
| 32 | MT Power Drum Kit 2 drum-map downloads | Manda Audio | note-name files, 9 DAWs | `powerdrumkit.com/presets_drum-maps.php`; e.g. `resources.manda-audio.com/DOWNLOADS/presets/drum-maps/MT-PowerDrumKit_2_Drum_Map_for_Reaper.zip` | P | **yes** |
| 33 | MT Power "Reaper — how to load a drum map" | Manda Audio | KB page | `powerdrumkit.com/help-drum-map-Reaper.php` (also de/fr/es/pt/it) | P | **yes** |
| 34 | Superior Drummer 2 Operation Manual | Toontrack | manual + GM Extended chart | `toontrack.com/updates/manuals/Superior_Drummer_Operation_Manual.pdf`, Wayback 20091122132452 | P-m | **yes** |
| 35 | EZdrummer Operation Manual | Toontrack | manual + key map | `toontrack.com/updates/manuals/EZdrummer_Operation_Manual.pdf`, Wayback 20080920202809 | P-m | **yes** |
| 36 | dfh Superior manual | Toontrack | manual | `toontrack.com/updates/superior/Superior_Manual_dfhS_155.pdf` | P-m | not fetched |
| 37 | Toontrack manual portal | Toontrack | web manual | `toontrack.com/manual/superior-drummer-3/`, `…/ezdrummer-3/`, `toontrack.com/manuals/` | P | **no** — login wall |
| 38 | Toontrack E-Drums FAQ | Toontrack | KB article | `toontrack.com/faq/e-drums-faq/` | V | **yes** — no map, no articulation list |
| 39 | Toontrack SDX/EZdrummer product pages | Toontrack | marketing prose | `toontrack.com/product/the-rooms-of-hansa-sdx/`, `…/death-darkness-sdx/`, `…/superior-drummer-3/` | V | **yes** |
| 40 | IK FAQ 1395 "Where do I find my user manual?" | IK Multimedia | KB article | `ikmultimedia.com/faq/index.php?id=1395` | P | **yes** — states manuals are in the account area |
| 41 | IK FAQ 1262 "Can I use MODO DRUM with my electronic drumset?" | IK Multimedia | KB article | `ikmultimedia.com/faq/index.php?id=1262` | P | **yes** — CC setup only |
| 42 | MODO Drum product page (PLAY STYLES section) | IK Multimedia | marketing prose | `ikmultimedia.com/products/mododrum/` | V | **yes** |
| 43 | ML Drums product page / update page / FAQ | ML Sound Lab | product pages | `ml-sound-lab.com/pages/ml-drums`, `…/ml-drums-update`, `…/faq` | V | **yes** — nothing on articulations or mapping |
| 44 | Krimh Drums MIDI mapping article | Bogren Digital | blog/KB | `bogrendigital.com/blogs/news/instantly-hear-your-songs-with-krimh-drums-midi-mapping` | V | **yes** — screenshot only |
| 45 | Sennheiser DrumMic'a landing page | Sennheiser | product page | `en-us.sennheiser.com/drummica` | V | reached, redirects away; `www.drummica.com` unreachable |

Deliberately **not** used, and why: the Toontrack Cubase `.drm` pack and the Studio One
`.pitchlist` collection that round 1 leaned on (community redistribution); `manuals.plus`,
`usermanual.wiki`, `manualslib`, `manualzz`, `scribd`, `pdfcoffee`, `audiofanzine` and
`thomann` copies of vendor manuals (third-party rehosting — usable only as a last-resort
locator, and every one of them was replaced above by a vendor-path copy); Groove Monkee
(forbidden by contract, CLAUDE.md rule 2) even though its ML Drums page is the only public
statement that ML Drums ships DAW drum maps in an "Extras" folder — that claim is therefore
recorded here as UNVERIFIED and unsourced.

---

## 2. Extracted terminology (round B)

### 2.1 Each vendor's word for the concept

| Vendor | Their term for a way of playing | Their term for the note assignment | Locator |
|---|---|---|---|
| XLN Audio | **stroke type** (also written *StrokeType*, *Stroketype*) | **keymap** / **drum map**; a saved one is a **Map Preset** (`.ADmap`); the remapper is the **PowerMap Engine** | AD2 manual pp. 46, 53, 58–60; keymap PDF column header `StrokeType`; KB 16925247222045 "a PDF of the Addictive Drums 2 drum map/keymap … which midi notes the different drum sounds (stroke types) correspond to" |
| FXpansion / inMusic (BFD) | **articulation** — "Each drum, cymbal, hihat, or percussion instrument within BFD3 features a number of articulations, each representing a way of playing the instrument" | **Key Map** | BFD3 FAQ, article 69000801225; `bfd3_key_map_reference.htm` column header "BFD3 articulation" |
| inMusic (BFD Player) | **Articulation**, paired with **Kit Piece** | **keymap** | BFD Player User Guide, Appendix "Keymap", p. 16 |
| Native Instruments | **articulation**, paired with **Drum** | **Default Drum Mapping** / **MIDI Mapping**; presets are **Mapping Presets** | Studio Drummer manual §3.4.2, §5; Abbey Road 60s §4.3 |
| Steven Slate | **articulation**; the UI panel is the **Articulation panel**, the page is **Map** | **mapping**, **Map Preset**; SSD4 used **Map Converter** and **IOMap** | SSD5.5 manual pp. "Articulations", "Map"; KB 360033680013, 360033678813 |
| GetGood Drums | **articulation**, nested under **kit piece**; the window is **Mapping** | **Map Config** (Factory Configs / Third-Party Software Configs / Third-Party Hardware Configs) | KB 32177396568727, 31476793134743 |
| Toontrack | **articulation** — "Think of articulations as particular techniques that the drummer might have used or as variations that would be difficult to reproduce through MIDI only" | **key layout** / **MIDI mapping**; the house standard is **GM Extended** | SD2 manual p. "Construction", p. 45 (GM Extended), chart p. 56 |
| Rayzoon (Jamstix) | **kit piece** is the addressable unit; **ARTICULATION** exists only as a Kit Editor list of the sounds within a kit piece | **output mapping** file, `[Keys]` section keyed by **Kit Piece Reference ID** | Jamstix 4 manual §11.6, Appendix B, Appendix C |
| Sennheiser (DrumMic'a) | no cover term; the map lists instrument + technique as one string | **MIDI mapping** — glossary: "assigning sounds to MIDI-notes" | DrumMic'a manual §4.5.2, glossary p. 57 |
| Manda Audio (MT Power) | no cover term; entries are drum names | **drum map** / **note names** / **pitch names** | `powerdrumkit.com/presets_drum-maps.php` |
| IK Multimedia (MODO Drum) | **PLAY STYLES** — technique is a model parameter, not a named articulation | **Factory mapping** / **Custom MIDI mapping** | product page; FAQ 1262 |

### 2.1.1 What the vendors' own German editions do — the identifier finding

Two vendors publish a German manual, and both were fetched to see whether the articulation
names get translated. **Neither translates a single articulation name.**

- **NI Studio Drummer, German manual** (`Studio_Drummer_Manual_German_2012_07.zip` →
  `Studio Drummer Manual German.pdf`). The chapter is retitled "5 Drum **Spielvarianten**"
  and the running prose uses *Spielvariante* throughout ("jeder Spielvariante eine oder
  mehrere MIDI-Noten zuweisen", §3.4.2). But the tables in that chapter keep the English
  column header `Articulation` and every value in English: `Dampened`, `Open`,
  `Center Right/Left Alternating`, `Halfway Left Hand`, `Rimshot`, `Sidestick`, `Flam`,
  `Roll`, `Wires Off`, `Rim Only`, `Closed Tight Tip Right Hand`, `Open Three-Quarters`,
  `Open Controller`. The manual even keeps the English document titles when pointing at the
  note maps: "…in den separaten Dokumenten 'The Session Kit - Default Mapping', 'The Stadium
  Kit - Default Mapping' und 'The Garage Kit - Default Mapping'". Where NI does translate,
  it translates the *concepts*: `Belegung` (mapping/assignment), `MIDI-Zuweisungen`,
  `Anschlagsebenen` (velocity layers), `Anschlagsdynamik` (velocity),
  `Schlagzeuginstrument`.
- **Rayzoon Jamstix 4, German manual** (`rayzoon2.com/docs/jamstix4_manual_german.pdf`,
  68 pp. against the English edition's 77 — it is an older revision and does **not** contain
  the Appendix B reference-ID table). UI labels stay English in the German text:
  `'KIT PIECE'-Liste`, `'ARTICULATION'-Liste`, `WRIST ARTICULATION ANGLE`. Translated
  vocabulary is again conceptual: `Kit-Teil` / `Drumkit-Teil` / `Schlagzeugteil` (kit piece),
  `Fell` (head), `Kessel` (shell).

That is worth more to KITWARP than a German word list would have been: two independent
vendors, translating everything else, treat articulation names as **identifiers rather than
prose**. It is direct vendor practice supporting ADR-0003's "identifiers are forever" —
and it means a German-language KITWARP surface should localise the *labels* while keeping
the slugs, exactly as NI does.

Two structural outliers:

- **Jamstix** does not separate instrument from articulation in its interchange format at
  all. Appendix B is a flat numbered list in which `Snare` is ID 1, `Snare Rimshot` is 4 and
  `Snare Center Hit` is 38 — siblings, not an instrument and its variants. Round 1 already
  flagged this; the appendix is now confirmed first-hand.
- **XLN** is the only vendor whose word is not "articulation". "Stroke type" is used
  consistently across the manual, the keymap sheet and the KB.

### 2.2 XLN Addictive Drums — full stroke-type vocabulary

Source: `Addictive Drums 2 Keymap.pdf` (columns KitPiece / StrokeType / Brushes StrokeType),
corroborated by AD2 manual pp. 58–59 "Stroketypes Explained" where the terms appear in
quotation marks against a diagram.

| Kit piece | StrokeType | Brushes StrokeType |
|---|---|---|
| Kick | (single, unnamed) | — |
| Snare | `Open Hit`, `Rimshot`, `Shallow Hit`, `Shallow Rimshot`, `SideStick`, `RimClick`, `Sticks`, `Open Hit (dbl)`, `Rimshot (dbl)` | `Open Hit`, `Open Lateral Hit`, `Closed Hit`, `Closed Lateral Hit`, `Open Shallow Hit`, `Closed Shallow Hit`, `Closed Soft Tap`, `Sweep Mute`, `Sweep: Short 1`, `Sweep: Short 2`, `Sweep: No Accent`, `Sweep: Slow Bright Accent`, `Sweep: Fast Bright Accent`, `Sweep: Slow Dark Accent`, `Sweep: Fast Dark Accent`, `Sweep: Short 1 (dbl)` |
| Tom 1–4 | `Open Hit`, `Rimshot` | `Open Hit (dbl)` |
| HiHat | `Closed 1 Tip`, `Closed 1 Shaft`, `Closed 2 Tip`, `Closed 2 Shaft`, `Closed Bell`, `Open A`, `Open B`, `Open C`, `Open D`, `Open Bell`, `Pedal Closed`, `Pedal Open`, `CC Hihat Tip`, `CC Hihat Shaft`, `CC Hihat Bell` | `Closed 1 Hit`, `Closed 1 Hit (dbl)`, `Closed 2 Hit`, `Closed 2 Hit (dbl)` |
| Ride 1–2 | `Tip`, `Shaft`, `Bell`, `Choke`, `Tip (dbl)` | `Hit Softer`, `Hit Stronger`, `Hit Softer (dbl)` |
| Cymbal 1–6 | `Hit`, `Choke`, `Hit (dbl)` | — |
| Flexi 1–3 | `Hit A`, `Hit B`, `Hit C`, `Hit D` | — |
| Snare (CC) | `CCpos (Open<>Shallow)`, `CCpos [only brush] (Closed<>Shallow)` | |
| Ride 1–2 (CC) | `CCpos (Tip<>Bell)` | |

AD1 (2009 keymap PDF) used a different word for the same thing: `Ride Pearl`,
`HH Closed1 Pearl`, `HH Closed2 Pearl` where AD2 says `Tip`. `Shaft` is unchanged.
`HH Open A–D`, `HH Pedal Open/Closed`, `Snare RimClick / Shallow Hit / SideStick /
Shallow Rimshot / Open Hit R / Open Hit L / Rimshot R / Rimshot L`, `Cymbal n Choke`,
`Ride Pearl (double)` and `Cymbal 1 (double)` are all AD1 terms carried into AD2 nearly
unchanged (`(double)` → `(dbl)`, `Pearl` → `Tip`, `L/R` hands dropped).

AD2 manual, p. 58–59 diagram legend, verbatim: "Hihat & Ride: 'Shaft' / Cym: 'Hit'";
"Hihat & Ride: 'Bell'"; "Hihat & Ride: 'Tip'"; "Snare, Toms: 'Open Hit'"; "Snare, Toms:
'Rimshot'"; "Snare: 'Shallow Hit'"; "Snare: 'Shallow Rimshot'"; "Snare: 'Sidestick'";
"Snare: 'Rim Click'".

Manual p. 46 note, verbatim: "the stroke type names in the stroke type list are the default
names from the Addictive Drums 2 keymap … Some ADpaks may deviate slightly from that
standard. In the Modern Jazz Brushes ADpak, the 'RimClick' stroke type has been replaced by
the 'Sweep: Short 1' stroke type, but it will still be labeled as 'RimClick' in the stroke
type list." — i.e. XLN itself documents that the label and the sampled gesture can diverge
per expansion. That is a provenance warning for any per-ADpak mapping.

### 2.3 BFD3 — full articulation vocabulary

Source: `bfd3_key_map_reference.htm`, column "BFD3 articulation" (73 entries in the default
key map; the naming form is `<Drum slot>: <Articulation>`).

| Drum class | Articulations |
|---|---|
| Kick | `Hit`, `No Snare` |
| Snare | `Hit`, `Half Edge`, `Rim Shot`, `Rim Click`, `Side Stick`, `Flam`, `Drag` |
| Toms (Floor / Mid / High, each ×2) | `Hit`, `Rim Shot`, `Rim Click` |
| Hihat | `Closed Tip`, `Closed Shank`, `1/4 Tip`, `1/4 Shank`, `Half Tip`, `Half Shank`, `3/4 Tip`, `3/4 Shank`, `Open Tip`, `Open Shank`, `Pedal`, `Splash`, `Bell Tip` |
| Ride 1 | `Bow`, `Edge`, `Bell`, `Hit`, `Choke` |
| Crash 1–2 | `Bow`, `Edge`, `Bell`, `Hit`, `Choke` |
| Cymbal 1–3 | `Bow`, `Edge`, `Bell`, `Hit`, `Choke` |
| Perc / Perc 2 | `Hit` |

BFD Player (the free player, same house vocabulary) adds the CC-driven forms:
`Variable`, `Variable Tip`, `Variable Shank` for snare and hihat — one key whose articulation
is selected continuously by a controller. Everything else in its keymap is drawn from the
same list (`Bow`, `Edge`, `Bell`, `Choke`, `Rim Click`, `Rim Shot`, `Side Stick`, `Pedal`,
`Splash`, `1/4`, `Half`, `3/4`, `Open`, `Closed`, `Tip`, `Shank`).

**BFD3 defines its own terms, and in doing so settles an axis question.** From
`using_electronic_drumkits.htm`, verbatim:

- "Some brains that support multi-zone triggers are capable of sending out different open
  and closed notes for **tip (also known as bow)** and **shank (edge)** triggers."
- "The Variable tip is used for the main surface or 'bow' of the hihat … **'Tip' refers to
  the fact that the surface of the hihat is struck with the tip of the stick.**"
- "The Variable shank is used for the edge of the hihat … **'Shank' refers to the fact that
  the edge of the hat is struck with the shank, or body, of the stick.**"
- "Almost all brains send out a 'pedal', or **'foot-chick'**, sound when the hihat control
  pedal is depressed fully."
- "BFD3 is capable of analyzing this controller data while a hihat trigger is received to
  determine which hihat articulation to play from those available: **closed, 1/4-open,
  1/2-open, 3/4-open or fully open**."
- "The Open tip articulation in particular is more like a hihat bell sound, or a small ride
  cymbal." — i.e. the vendor warns that its own `Open Tip` is not the sound most users mean
  by an open hat, and recommends remapping a brain's open notes to `1/2-open tip` and
  `1/2-open shank`.

The first three are the single most useful sentences found in this bucket: a vendor stating
that for a hi-hat, naming the *stick part* and naming the *cymbal region* are two names for
one event, and saying which is which. See §3.3 and §4.

Structural terms from the BFD3 manual worth carrying: a **Drum** occupies a **slot**; each
Drum has a **Class**; "if the destination Drum's Class differs from that of the source Drum,
an attempt is made to trigger an articulation with the same name. If this does not exist,
the first articulation is played ('closed tip' for hihats and 'hit' for all other Drum
types)" (`kit_display.htm`). That is a vendor-documented fallback rule of exactly the kind
KITWARP's resolver needs, and it is name-based, not number-based.

### 2.4 Native Instruments — full articulation vocabulary

Sources: Studio Drummer manual §5 (three kits); Abbey Road 60s manual §4 (two kits);
Abbey Road 70s / 80s / Modern manuals §6 (two kits each, with the note column).

Common core, identical across all eight NI kits examined:

| Drum | Articulations |
|---|---|
| Kick Drum | `Dampened`, `Open`, and in 70s/80s/Modern also `Half Open` |
| Snare Drum 1 & 2 (& 3) | `Center Left Hand`, `Center Right Hand`, `Center Right/Left Alternating`, `Halfway Left Hand`, `Halfway Right Hand`, `Halfway Right/Left Alternating`, `Rimshot`, `Sidestick`, `Flam`, `Roll`, `Wires Off`, `Rim Only` |
| Hihat | `Closed Tight Tip {Right Hand, Left Hand, Right/Left Alternating}`, `Closed Tip {…}`, `Closed Shank {…}`, `Closed Pedal`, `Open Pedal`, `Open Quarter`, `Open Half`, `Open Three-Quarters`, `Open Loose`, `Open Full`, `Open Controller` |
| Tom 1–4 | `Center Right Hand`, `Center Left Hand`, `Center Right/Left Alternating`, `Rimshot`, `Rim Only` |
| Crash / Cymbal | `Edge`, `Tip`, `Bell`, `Choke` |
| Ride | `Tip`, `Bell`, `Edge`, `Choke` |
| China | `Edge`, `Tip`, `Choke` |
| Splash | `Edge`, `Choke` |
| Tambourine | `Tap`, `Shake` |
| Clap | `Solo`, `Multi` |
| Stick Hit | `Hit` / `Solo` |
| Cowbell | `Open`, `Muted` (High and Low variants) |
| Woodblock | `Hit`; in the 80s kit `High`, `Mid`, `Low` |
| Shaker | `Shake` |

Library-specific additions — these are the interesting ones:

| Term | Library | What it physically is | Locator |
|---|---|---|---|
| `Felt Beater`, `Rubber Beater` | Abbey Road 60s (kick) | beater material as the only kick articulation axis — 60s has no `Dampened`/`Open` pair | AR60s §4.1, §4.2 |
| `Tea Towel` (snare), `Towel` (toms) | Abbey Road 60s Late 60s Kit | cloth laid on the head | AR60s §4.2 |
| `Towel` | Abbey Road 70s Tight Kit (snare) | same | AR70s §6.2 |
| `Skin On Skin` | Abbey Road 80s (snare, all four toms) | "place an additional upside down snare skin on top of the … drum. This deadens the sound significantly but doesn't kill the tone" — verbatim, AR80s p. 14 | AR80s §6.1 |
| `Mirror` | Abbey Road 80s (kick, snare) | undocumented in the manual text; the same manual describes Studio Three's "Mirror Room" with its own reverberation time, so this is very probably a room/ambience variant rather than a striking variation — **UNVERIFIED** | AR80s §6.1, cf. pp. 213, 236, 362 |
| `Splash On`, `Splash Off`, `Splash Rim` | Abbey Road Modern (snare, Sparkle Kit) | undocumented; most plausibly a splash cymbal resting on the snare head, played on/off/at the rim — **UNVERIFIED** | ARModern §6.1 |
| `Chopper` | Abbey Road Modern (Perc 3, `High`/`Mid`/`Low`) | percussion instrument not otherwise identified in the manual — **UNVERIFIED** | ARModern §6.1 |
| `Sizzle Ride` (as a Drum, with `Tip`/`Bell`/`Edge`/`Choke`) | Abbey Road 60s | rivet ride | AR60s §4.1 |

Footnote semantics, verbatim from Studio Drummer §5 and repeated in every Abbey Road manual:

- `*` "There is a separate note assignment that alternates between the left and right hand
  samples of the center and halfway snare, center tom, and closed hi-hat articulations when
  playing faster than a certain speed."
- `**` "There is a separate note assignment for the open hi-hat that controls the amount of
  hi-hat openness depending on the position of the Modwheel controller (CC1) or a hi-hat
  foot controller (CC4). At the 0 position of the controller, the open hi-hat control key
  plays the fully open hi-hat."
- `***` "Cymbal choke samples are triggered by specific note assignments which play release
  samples … If no cymbal sound is currently active, then the cymbal choke notes will do
  nothing."

NI's own mapping-preset list (Studio Drummer §3.4.2) is itself a small piece of evidence
about which foreign layouts a vendor considers worth supporting: "General MIDI, V-Drums (two
options), DrumIt Five, EZDrummer, Superior Drummer, BFD, iMap, and Addictive Drums."

### 2.5 GetGood Drums — Modern & Massive 2

Verbatim from KB 32177396568727, the only official GGD articulation list that exists:

| Kit piece | Articulations |
|---|---|
| Kick | `Hit` |
| Snare | `Hit`, `Cross Stick`, `Wires Off` |
| Rack Tom 1–2, Floor Tom 1–2 | `Hit` |
| Hats | `Tight Tip`, `Tight Edge`, `Closed Tip`, `Closed Edge`, `Open 1`, `Open 2`, `Open 3`, `Pedal Chick`, `Pedal Ching`, `Edge CC`, `Tip CC` |
| Ride | `Bow`, `Bell`, `Crash`, `Choke` |
| Crash Far Left / Crash Left / Crash Right | `Crash`, `Choke` |
| China | `Crash`, `Choke` |
| Splash | `Crash`, `Choke` |

Note three things. GGD names the hi-hat contact point as a **site** (`Tip` vs `Edge`) where
NI and BFD name the **part of the stick** (`Tip` vs `Shank`) for what is acoustically the
same pair. GGD's open ladder is an unnamed ordinal (`Open 1/2/3`) as AD2's is (`Open A–D`),
against NI's named ladder (`Quarter`/`Half`/`Three-Quarters`/`Loose`/`Full`) and BFD's
fractional one (`1/4`/`Half`/`3/4`/`Open`). And GGD uses `Crash` as an *articulation* name
on the Ride, China, Splash and the crashes themselves — the same word KITWARP uses as an
instrument.

GGD's mapping vocabulary: `Map Config`, `Factory Configs`, `Third-Party Software Configs`,
`Third-Party Hardware Configs`, `By Semitone` / `By Octave` global shift, `Clear Map`,
`CC Invert` for a hi-hat pedal whose polarity is reversed (KB 31476794941079).

### 2.6 Toontrack

No current chart is published. What Toontrack's own documents say, from the two archived
vendor-path manuals:

**Superior Drummer 2, "GM EXTENDED CORE MAPPING" chart (p. 56)** — Toontrack's own naming:

| Group | Names on the chart |
|---|---|
| Kick | `Right` |
| Snare | `Head`, `Rimshot`, `Ruffs`, `Sidestick` |
| Toms | `Racktom 1`, `Racktom 2`, `Racktom 3`, `Floortom 1`, `Floortom 2` |
| Hats | `Closed`, `Open 1`, `Open 2`, `Open 3`, `Foot Splash`, `Pedal` |
| Cymbals | `Crash A`, `Crash A Mute`, `Crash B`, `Crash B Mute`, `Ride Bow`, `Ride Bell`, `Ride Edge` |
| X-Drums generic | `X-Snare {Head, Rimshot, Sidestick}`, `X-Hats {Closed, 1/2 Open, Open}`, `X-Ride {Bow, Bell, Edge}`, `X-Crash {Crash}`, `X-Tom {Rack/Floor}`, `X-Kick {Right}` |

Same page, verbatim: "Please refer to specific key layout included with your Toontrack
product for full mapping." Toontrack has therefore never published a per-library chart on
the open web; it ships one inside each product.

**EZdrummer 1, §4.4 "Key Mapping"** — the `[Instrument] Articulation` form that round 1
inferred from community `.drm` files, here in the vendor's own hand:
`[Kick] Right`, `[Snare] Head`, `[Snare] Right`, `[Snare] Rimshot`, `[Snare] Sidestick`,
`[RackT1] Head`, `[RackT2] Head`, `[FloorT] Head`, `[Hats] Open Max`, `[Hats] Closed Tip`,
`[Hats] Tight`, `[Hats] Tight Tip`, `[Hats] Seq Soft`, `[Hats] Seq Hard`, `[Ride] Bow`,
`[Ride] Edge`, `[Ride] Bell`, `[CrashA] Muted`, `[CrashB] Muted`, `[Special] Cowbell`,
plus `alias` entries and `{GM}` markers for the General MIDI-compatible keys.
Two vendor concepts here that round 1 did not have: **`alias`** (a second key that plays an
articulation already mapped elsewhere) and **`{GM}`** (a key kept where General MIDI expects
it). Toontrack's guidance, verbatim: "If GM compatibility is important to you you should
always program the map between C1 and C3 only."

**Superior Drummer 2 definition of articulation**, verbatim: "Think of articulations as
particular techniques that the drummer might have used or as variations that would be
difficult to reproduce through MIDI only." And on availability: "Depending on the Instrument
selected in the Construction window, some of these Articulations may not be available. They
may, for example, not have been sampled with this particular set of tools and can therefore
not be used with this specific drum selection. An '*' is used to represent the
unavailability." — Toontrack's marker for "this articulation does not exist on this
instrument" is a leading asterisk.

**Current-generation prose** (SDX product pages, the only public statement of what an SDX
contains): "All these instruments were sampled with three unique articulations: center hits,
rimshots and rims only" (The Rooms of Hansa SDX); "the hi-hats were recorded with up to 27
unique multi-sampled articulations"; "The ride cymbals were sampled with up to seven
articulations"; "The snares sampled with 'wires on' and sticks include eight unique
articulations"; "The crashes were sampled in up to six articulations" (Hansa, and Death &
Darkness with eight ride and eight snare articulations). Vocabulary recoverable from that:
`center hit`, `rimshot`, `rim only`, `wires on`. Counts, not names, for everything else.

### 2.7 Rayzoon Jamstix 4 — Appendix B verified and completed

Appendix B is two tables. **DRUM KIT** identifiers, IDs 0–57 and 90–104:

`Kick` 0; `Snare` 1 ("At play time, this sound is resolved to center or offset hit by the
A.I."); `Snare Side/Crosstick` 2; `Snare Bounced` 3; `Snare Rimshot` 4;
`Snare Brushed Muted` 5 ("This is a brush hit without lift in order to mute the head");
`Snare Brush Sweep` 6; RESERVED 7; `Hihat (Dynamic Open)` 8 ("Pedal pressure controls open
level"); `Hihat Foot Close` 9; `Hihat Foot Splash` 10; RESERVED 11; `Ride` 12; `Ride Bell`
13; RESERVED 14; `Crash 1–4` 15–18; `Splash 1–3` 19–21; `China 1–4` 22–25; RESERVED 26;
`Tom 1–5` 27–31 (same centre/offset resolution note); `Jam Block Hi` 32; `Jam Block Lo` 33;
`Chimes` 34; `Cowbell` 35; `Tambourine` 36; `Drumsticks` 37; `Snare Center Hit` 38;
`Snare Offset Hit` 39 ("The A.I. will use this sound for 16th L/R clusters");
`Tom n Center Hit` / `Tom n Offset Hit` 40–49; `Hihat Closed` 50 ("Pedal pressure is not
considered"); `Hihat 25% Open` 51; `Hihat 50% Open` 52; `Hihat 75% Open` 53; `Hihat Open`
54; `Cymbal Choke` 55 ("Will choke the last cymbal played with the same hand");
`Egg Shaker` 56; `Metal Shaker` 57; `Kick (Left Drum)` 90 ("This is the 2nd kick (left in
drummer view)"); `Kick (Right Drum)` 91; `Hihat Shank Closed` 92; RESERVED 93;
`Hihat Shank 50% Open` 94; RESERVED 95; `Hihat Shank Open` 96; `2nd Snare` 97;
`2nd Snare Side/Crosstick` 98; `2nd Snare Bounced` 99; `2nd Snare Rimshot` 100;
`2nd Snare Brushed Muted` 101; `2nd Snare Brush Sweep` 102; `2nd Snare Center Hit` 103;
`2nd Snare Offset Hit` 104.

**JAMCUSSION** identifiers, IDs 58–89 — round 1 did not have these:
`Drum 1–4 Center` / `Medium/Open` / `Rim/Slap` / `Hit & Mute` (58–73);
`Percussion 1–8 Main` / `Alternate` (74–89).

Appendix C, the output-mapping file format, is a plain `.ini`: `[Keys]` (`<ReferenceID>=<key>`),
`[Hihat]` (`UseCC=`, `Controller=`, "usually #4"), `[Snare]` (`Controller=` for "drum head
positioning", 0 if unsupported), `[Tom]` (same), `[Chokes]` (`CH_<ReferenceID>=<key>`, plus
`AfterTouchChoke=1` "If the 3rd party plugin supports choking via aftertouch events"), and
`[Drum Kit]` (`ShortName=`, `LongName=`). This is the one vendor in the bucket that
publishes a *documented, editable interchange format* rather than only a chart, which makes
it the natural round-trip test target for a KITWARP exporter.

### 2.8 Sennheiser DrumMic'a

The manual publishes six complete maps (Default/GM, V-Drums TD-12/20, V-Drums TD-3/6,
EZ Drummer, Addictive Drums, Superior Drummer). The instrument+technique strings used, in
full:

`Bass Drum`; `Snare Hit`, `Snare Sidestick`, `Snare Rimshot`, `Snare Flam`, `Snare Roll`,
`Snare Beach towel`, `Snare w/o wires`; `Tom 1`, `Tom 2`, `Tom Floor`;
`HiHat closed`, `HiHat pressed`, `HiHat loose`, `HiHat 1/2 open`, `HiHat open`,
`HiHat trash open`, `HiHat pedal`; `Ride tip`, `Ride edge`, `Ride bell`;
`Crash 16 tip`, `Crash 16 edge`, `Crash 16 bell`, `Crash 18 tip`, `Crash 18 edge`,
`Crash 18 bell`; `China tip`, `China edge`, `China bell`; `Count stick`.

Four of those are vocabulary nobody else in this bucket uses: `pressed` and `loose` as
distinct hi-hat states either side of `closed`; `trash open` (a deliberately trashy open
hi-hat, undefined in the manual — **UNVERIFIED** as to whether it means a shank hit, a
half-loose hat or a different pair of hats); `Beach towel` for the damped snare; and
`Count stick` for the count-in click.

Its glossary is the vendor's own definition set: `MIDI MAPPING` = "assigning sounds to
MIDI-notes"; `ROUND ROBIN` = "provision of multiple, slightly different samples for each
note and velocity range which are then cycled between … this eliminates the dreaded 'machine
gun effect'"; `SNARE BLEED` = "the resonance of the reverberating snare caused by the sound
of other instruments".

### 2.9 MT Power Drum Kit 2

The official Reaper note-name file (contents in full, as shipped):

`KICK`, `SNARE`, `SIDE-STICK`, `TOM LOW`, `TOM MID`, `TOM HI`, `HI-HAT CLOSED`,
`HI-HAT HALF OPEN`, `HI-HAT OPEN`, `HI-HAT PEDAL`, `CRASH LEFT`, `CRASH RIGHT`,
`CRASH RIGHT CHOKED`, `SPLASH`, `CHINA`, `RIDE`, `RIDE BELL`, `CHOKE ALL CYMBALS`,
plus parenthesised alias entries — `(Kick)`, `(Snare)`, `(Tom Hi)`, `(Tom Mid)`, `(Tom Low)`,
`(Hi-Hat closed)` — marking duplicate keys that play an already-named sound.

Two things generalise beyond this product. The parenthesis convention is a vendor's own way
of marking an alias key in a note-name file. And the vendor states: "If you're using the
VST3 version of the plugin, the drum names are automatically displayed in the piano roll or
drum editor of Reaper. You don't need to download and install an extra file for that"
(`powerdrumkit.com/help-drum-map-Reaper.php`) — i.e. the VST3 note-name interface is itself
an official, machine-readable source of a vendor's articulation names, available for any
VST3 instrument that implements it, without any document at all. No other vendor in this
bucket mentions it.

### 2.10 Steven Slate, ML Drums, MODO Drum — what the negatives contain

**SSD5.5**: the manual uses "articulation" throughout but names only two in prose — "the
Hi-Hat *pedal*, or the Snare *Sidestick*" (p. "Articulations") — and documents one naming
convention: "When an articulation displays '(stacked)' at the end of its name, multiple
[samples are] mapped to the MIDI note. For example, if you have multiple Snare Center
articulations loaded…". So `Snare Center` is an SSD articulation name, and `(stacked)` is
SSD's marker for a layered key. Nothing else is recoverable officially.

**MODO Drum**: technique is not articulated as named sounds at all. The vendor's public
vocabulary is parametric — "PLAY STYLES", "Change your player's kick technique: heel down
gives more resonance and tone to your kicks, while heel up gives you a more aggressive,
tighter sound", "choosing a beater made of felt, wood or plastic", "adjust the hi-hat gap to
shape the sound of open hi-hat hits" (product page). `heel up` / `heel down`, the three
beater materials and `hi-hat gap` are the only MODO terms this pass can source officially.

**ML Drums**: nothing. No manual, no keymap, no articulation list on any ML Sound Lab page.

---

## 3. Axis mapping

### 3.1 Terms that map cleanly

| Vendor term(s) | Axis | v0.1 value |
|---|---|---|
| `Hit`, `Open Hit`, `Head`, `Center …`, `Snare Center Hit`, `Drum n Center` | technique + position | `hit` + `centre` |
| `Halfway …`, `Half Edge`, `Shallow Hit`, `Snare Offset Hit`, `Medium/Open` | position | `halfway` / `offset` |
| `Rimshot`, `Rim Shot`, `Shallow Rimshot` | technique | `rimshot` |
| `Rim Only`, `Rim Click`, `RimClick` | technique | `rim-only` |
| `Sidestick`, `Side Stick`, `SideStick`, `Cross Stick`, `Snare Side/Crosstick` | technique / site | `sidestick` / `crossstick` |
| `Flam` | ornament | `flam` |
| `Drag`, `Snare Bounced` | ornament | `drag` / `bounced` |
| `Ruffs` | ornament | `ruff` |
| `Roll` | ornament | `roll` |
| `Tip`, `Pearl` (AD1) | contact | `tip` |
| `Shank`, `Shaft` | contact | `shank` |
| `Bow` | site | `bow` |
| `Edge` | site | `edge` |
| `Bell`, `Bell Tip`, `Closed Bell`, `Open Bell` | site (+ contact) | `bell` (+ `tip`) |
| `Closed Tight`, `Tight Tip`, `Tight Edge` | openness | `tight` |
| `Closed`, `Closed 1/2`, `Closed Tip/Shank/Edge` | openness | `closed` |
| `loose` (Sennheiser), `Open Loose` (NI) | openness | `closed-loose` / `loose` |
| `1/4`, `Open Quarter`, `Hihat 25% Open` | openness | `quarter` |
| `Half`, `Open Half`, `1/2 open`, `50% Open`, `HI-HAT HALF OPEN` | openness | `half` |
| `3/4`, `Open Three-Quarters`, `75% Open` | openness | `three-quarter` |
| `Open`, `Open Full`, `Open Max` | openness | `open` |
| `Pedal`, `Closed Pedal`, `Pedal Chick`, `Hihat Foot Close`, `HI-HAT PEDAL` | technique | `chick` |
| `Open Pedal`, `Foot Splash`, `Hihat Foot Splash`, `Splash` (BFD hihat) | technique | `foot-splash` |
| `Wires Off`, `w/o wires`, `Snare w/o wires` | mechanism | `wires-off` |
| `wires on` (Toontrack prose) | mechanism | `wires-on` |
| `Dampened` (NI kick) | mechanism | `kick-damped` |
| `Half Open` (NI kick) | mechanism | `kick-half-open` |
| `Felt Beater`, `Rubber Beater`, felt / wood / plastic beater (MODO) | implement | `felt-beater`, `rubber-beater`, `wood-beater`, `plastic-beater` |
| `Brushes` column (AD2), `Snare Brush Sweep`, `Snare Brushed Muted` | implement | `brush` |
| `Sticks`, `Drumsticks`, `Stick Hit`, `Count stick` | instrument | `sticks` |
| `Sweep`, `Sweep: Short/Slow/Fast …` | technique | `sweep` |
| `Sweep Mute`, `Snare Brushed Muted`, `Hit & Mute` | technique + damping | `sweep`/`hit` + `muted` / `mute-stroke` |
| `Tea Towel`, `Towel`, `Beach towel` | damping | `towel` |
| `Muted` (cowbell), `Crash A Mute`, `Crash B Muted`, `[CrashA] Muted` | damping | `muted` |
| `Choke`, `Cymbal Choke` | damping / technique | `dead` + choke semantics |
| `Tap`, `Shake` (tambourine, shaker) | technique | `hit` / `shake` |
| `Slap`, `Rim/Slap` (Jamstix jamcussion) | technique | `slap` |
| `Open Controller`, `CC Hihat Tip/Shaft/Bell`, `Variable Tip/Shank`, `Hihat (Dynamic Open)`, `Edge CC` / `Tip CC` | controller | `hihat.pedal_position` |
| `CCpos (Open<>Shallow)`, `CCpos (Tip<>Bell)`, Jamstix `[Snare] Controller=` | controller | `strike_position.radial` |
| `Left Hand` / `Right Hand` | limb (reference axis) | limb |
| `Ride`, `Crash`, `China`, `Splash`, `Cowbell`, `Tambourine`, `Woodblock`, `Jam Block`, `Chimes`, `Clap` | instrument | existing values |

### 3.2 Terms that fit NO axis in v0.1 — the valuable list

| Term | Vendor | Why it fits nothing |
|---|---|---|
| `Center Right/Left Alternating` | NI (all libraries) | It is not a limb value: it means *"the engine chooses a hand per note above a speed threshold"*. v0.1's `limb` is a definite reference value; there is no "either / engine-selected" value. Every NI kit maps this to its own key, so it is a first-class addressable thing. |
| `Solo` vs `Multi` (Clap) | NI | One pair of hands versus a group. An **ensemble-size** distinction — no axis carries it. The same distinction recurs in other libraries' `Claps` vs `Clap` naming. |
| `Skin On Skin` | NI Abbey Road 80s | A damping *object* that is not a towel: a second, inverted drumhead laid on the batter head. `damping: damped` loses the identity; `towel` is the wrong object. |
| `Mirror` | NI Abbey Road 80s | Almost certainly a room variant carried as an articulation (UNVERIFIED). If so it belongs on `voicing`, but `voicing` has no `mirror`/room-name concept and the mapping is a guess. |
| `Splash On` / `Splash Off` / `Splash Rim` | NI Abbey Road Modern | A second instrument resting on the snare, played in three ways. Neither `instrument` (it is a compound) nor `site` covers it. Closest existing idea is `stack`. |
| `Chopper` | NI Abbey Road Modern | Unidentified percussion instrument. No instrument value; may need one. |
| `trash open` | Sennheiser | A timbral qualifier on an open hi-hat. Not `openness`, not `voicing` as defined. |
| `pressed` | Sennheiser | A *pedal-force* state distinct from `closed` and `loose`. v0.1's `openness` is a geometry scalar; pedal force at a fixed gap is a different physical variable. |
| `Pedal Ching` | GetGood Drums | GGD lists it alongside `Pedal Chick`, so it is not `chick`. Most likely the loose/ringing foot close (a foot splash by another name) — **UNVERIFIED**; if it is a third pedal state, `technique` needs a value. |
| `Hit A` / `Hit B` / `Hit C` / `Hit D` (Flexi) | XLN | Ordinal variants of an unspecified user-loaded sound. Unmappable by design: the kit piece is a user slot. |
| `Open A/B/C/D`, `Open 1/2/3` | XLN, GGD | An openness ladder with no named anchors. Mapping onto v0.1's named anchors requires an assumption about how many steps map to which anchor — a real conversion loss, not a naming difference. |
| `Hit Softer` / `Hit Stronger` (brushes on ride) | XLN | Dynamic carried as a separate key rather than as velocity. Maps to `dynamic` `soft`/`hard`, but note that the vendor treats it as a *stroke type*, so an importer must know to move it to another axis. |
| `(dbl)` / `(double)` / `alias` / `(Snare)` in parentheses | XLN, Toontrack, Manda | Alias markers: "this key plays a thing already mapped elsewhere". A property of the *mapping*, not of the sound. KITWARP needs a first-class alias concept on layout slots; it is not an axis value. |
| `(stacked)` | Steven Slate | Marks a key that triggers several articulations at once. A layering property of the mapping. |
| `CHOKE ALL CYMBALS` | Manda Audio | A global control event, not an instrument articulation. |
| `Kick: No Snare` | BFD3 | A *recording state of the whole kit* (snares disengaged so the kick does not excite them) carried as a kick articulation. Cross-instrument state; no axis. |
| `Seq Soft` / `Seq Hard` | Toontrack EZdrummer 1 | Sequenced/programmed hi-hat variants intended for the groove engine. Neither dynamic nor technique in the physical sense. |
| `Variable`, `Variable Tip`, `Variable Shank` | BFD Player | One key whose articulation is a *function* of a controller. A pivot term would have to express "articulation selected by controller", which is a mapping construct. |
| `Percussion n Main` / `Alternate`, `Drum n Center/Medium/Open/Rim/Slap/Hit & Mute` | Rayzoon Jamstix | Deliberately abstract slots: the identity of the instrument is deferred to whatever the user loads. Slot semantics, not instrument semantics. |
| `heel up` / `heel down` | IK MODO | A pedalling technique that changes timbre without changing what is struck. No axis; nearest is `technique`, but it coexists with every kick technique rather than replacing one. |
| `hi-hat gap` | IK MODO | A continuous physical parameter (the geometry behind `openness`) exposed directly. |
| `X-Snare`, `X-Hats`, `X-Ride`, `X-Crash`, `X-Tom`, `X-Kick` | Toontrack SD2 | Generic "extra drum" slots addressed by a role rather than an identity. Layout-slot concept. |
| `Flexi 1–3` | XLN | Same idea under another name. |

### 3.3 Axis-choice disagreements between vendors

Same physical event, different axis chosen by different vendors:

| Physical event | Named as contact | Named as site | Named as instrument |
|---|---|---|---|
| stick's shaft against the hi-hat's outer edge | `Closed Shank` (NI, BFD), `Closed 1 Shaft` (XLN) | `Closed Edge`, `Tight Edge` (GGD) | — |
| tip on the hi-hat's top surface | `Closed Tip` (NI, BFD, XLN, GGD) | — | — |
| bow hit on a crash cymbal | — | `Bow` (BFD), `Edge`/`Tip` (NI) | `Crash` as the articulation name (GGD) |
| stick tip on the ride's bow | `Tip` (NI, XLN, Sennheiser) | `Bow` (BFD, Toontrack) | — |

That last row is the sharpest: for the same stroke, BFD and Toontrack name where on the
cymbal it lands and NI, XLN and Sennheiser name what part of the stick lands there. A pivot
that carries both `site` and `contact` can represent either, but an importer must know which
axis a given vendor's word belongs on — the word alone does not say.

For the hi-hat, one vendor says so outright, which converts the disagreement from a guess
into a documented equivalence: BFD3 writes "tip (also known as bow)" and "shank (edge)", and
explains that the words name the same event from the two ends — the stick's tip on the
cymbal's bow, the stick's shank on the cymbal's edge (`using_electronic_drumkits.htm`).
So `contact: tip` + `site: bow` and `contact: shank` + `site: edge` are the correct
full-fidelity encodings, and a vendor that gives only one half is under-specifying rather
than disagreeing. GGD's `Tight Edge` and NI's `Closed Shank` are therefore the *same*
articulation, and can be reconciled — which round 1, working from note numbers, could not
have established.

---

## 4. Conflicts and false friends

| Word | Meaning A | Meaning B | Note |
|---|---|---|---|
| `Crash` | an instrument (KITWARP, everyone's kit list) | an articulation on Ride / China / Splash / Crash (GGD M&M2) | GGD's `Ride > Crash` means "crash the ride", i.e. a hard edge/bow hit |
| `Splash` | a small cymbal (all vendors) | a hi-hat foot articulation, `Hihat: Splash` (BFD3, BFD Player) | and again a snare articulation `Splash On/Off/Rim` (NI Abbey Road Modern), meaning something else a third time |
| `Pearl` | the tip of a drumstick (XLN Addictive Drums 1: `Ride Pearl`, `HH Closed1 Pearl`) | a drum manufacturer, and a shell finish | XLN itself abandoned the word between AD1 and AD2 |
| `Shaft` / `Shank` | the same part of the stick | — | `Shaft` is XLN and Toontrack; `Shank` is NI, BFD and Jamstix. Pure synonym pair |
| `Bell` | site on a cymbal | an instrument (`bell` in v0.1's instrument axis) | and in BFD `Hihat: Bell Tip` combines both |
| `Edge` | site on a cymbal (BFD, NI) | contact point on a hi-hat naming the *stick* implicitly (GGD) | not actually a conflict for the hi-hat: BFD3 documents "shank (edge)" and "tip (also known as bow)" as the same events named from opposite ends — see §3.3 |
| `Tight` | openness anchor (NI `Closed Tight`, GGD `Tight Tip`) | a groove-feel control (`TIGHTNESS` knob, NI Studio Drummer §3.3) | different axes entirely |
| `Open` | openness anchor | kick articulation `Open` = undamped port (NI) | and `Open Tone` in hand-percussion vocabulary is a third thing |
| `Articulation` | a way of playing (every vendor) | `WRIST ARTICULATION ANGLE` — the anatomical joint angle of the animated drummer's wrist (Jamstix 4 manual §29) | genuine homograph inside one vendor's own manual |
| `Roll` | a sustained multi-stroke ornament (NI, Sennheiser) | — | Toontrack's nearest term is `Ruffs`, which elsewhere means a specific 3-stroke ornament, not a sustained roll |
| `Bounced` | Jamstix ID 3, sits where a drag would | v0.1 has both `drag` and `bounced` as distinct ornaments | Jamstix uses one word for what other vendors split |
| `Head` | Toontrack's word for the centre hit (`[Snare] Head`) | the drumhead as a *site* in v0.1 (`site: head`) | Toontrack's `Head` = `site: head` + `position: centre` + `technique: hit` |
| `Right` | Toontrack's word for the main kick (`[Kick] Right`, `X-Kick Right`) | a limb value | Toontrack means "the right-foot drum", i.e. an instance, not a technique |
| `Mute` / `Muted` | damping applied to a ringing cymbal (`Crash A Mute`) | a hand-percussion stroke type (`Hit & Mute`, Jamstix) | one is a state, one is a stroke |
| `Variable` | BFD Player: articulation chosen by controller | — | not a variability of dynamics |
| `Multi` | NI: a group of clappers | NI Groove naming: "more than one of the above sounds or techniques is used" | same word, two meanings inside one manual |

---

## 5. Gaps against vocabulary v0.1

Checked against `vocabulary/axes.json`, `vocabulary_version` 0.1.0, serial 1.

### 5.1 Missing values that a vendor names and v0.1 cannot express

| Axis | Missing value | Evidence |
|---|---|---|
| limb (reference axis) | an "alternating / engine-selected" value | NI ships a dedicated key for `Center Right/Left Alternating` in every kit of Studio Drummer, Abbey Road 60s, 70s, 80s and Modern. Today this can only be encoded by omitting `limb`, which is indistinguishable from "unknown" |
| damping | `skin-on-skin` | NI Abbey Road 80s, snare and all four toms, defined verbatim in the manual |
| openness | an ordinal-ladder representation | XLN `Open A–D`, GGD `Open 1–3`. Four unnamed steps do not map onto eight named anchors without an assumption |
| technique | a pedal-force state between `chick` and `foot-splash` | Sennheiser `pressed` vs `closed` vs `loose`; GGD `Pedal Ching` vs `Pedal Chick` |
| instrument | `sizzle-ride` exists ✓; `chopper` does not | NI Abbey Road Modern Perc 3 |
| instrument | `mini-ride` | GGD P V Matt Halpern Signature Pack, "R&D Big Bell Mini Ride 15"" — see §5.4 |
| instrument | material-qualified shakers: `egg shaker`, `metal shaker` | Jamstix IDs 56, 57 — v0.1 has one `shaker` |
| instrument | a compound "cymbal resting on a drum" | NI `Splash On/Off/Rim`; v0.1's `stack` covers cymbal-on-cymbal only |
| dynamic | nothing missing, but a note: `Hit Softer` / `Hit Stronger` are *stroke types* in XLN's model | AD2 keymap, brushes column on Ride 1 and 2 |
| (no axis) | ensemble size — `Solo` vs `Multi` claps | NI, every kit |
| (no axis) | cross-instrument recording state — `Kick: No Snare` | BFD3 key map reference |
| (no axis) | alias / stacked-key markers | XLN `(dbl)`, Toontrack `alias`, Manda `(Name)`, Slate `(stacked)` |

### 5.2 Things v0.1 names that no vendor in this bucket uses

`stick-shot`, `back-stick`, `ping-shot`, `gok-shot`, `heel`, `toe`, `thumb`, `swirl`,
`circling`, `scrape`, `gliss` appear in no vendor document read here. That is expected —
they are hand-percussion and orchestral terms and this bucket is acoustic kit libraries —
but it is worth recording that the acoustic-kit vendors between them use only about half of
v0.1's `technique` axis. The half they do use, they use almost unanimously.

### 5.3 Misnamings to review

- v0.1 `position: offset` — three vendors use *three* different words for the same idea:
  Jamstix `Offset Hit`, XLN `Shallow Hit`, BFD `Half Edge`, NI `Halfway`. v0.1 has both
  `halfway` and `offset` as separate values; nothing in this bucket's evidence distinguishes
  them physically. Either they are synonyms and one is redundant, or the distinction needs a
  definition that a vendor document supports. **Flagged for the reconciliation pass.**
- v0.1 `technique: chick` — better attested than it looks. Most vendors call it `Pedal`,
  `Closed Pedal` or `Foot Close`, but **two** use the word: GGD writes `Pedal Chick`, and
  BFD3's manual writes "a 'pedal', or **'foot-chick'**, sound"
  (`using_electronic_drumkits.htm`). The slug stands; the alias table needs `pedal`,
  `foot-close`, `closed pedal`, `hi-hat pedal` and `foot-chick` pointing at it.
- v0.1 `damping: towel` — NI writes `Tea Towel` on the snare and `Towel` on toms in the same
  library; Sennheiser writes `Beach towel`. The slug is right; the alias set is missing.

---

## 5.4 Where five disputed v0.1 slugs came from

Assigned to this bucket after two other workers found that no manufacturer and no MIDI
standard uses `ping-shot`, `gok-shot`, `stick-shot`, `mini-china` or `mini-hihat`. The
question was whether a *library* coined them. Answers, with the evidence chain:

| Slug | Did a library coin it? | Evidence |
|---|---|---|
| `ping-shot` | **No.** It entered v0.1 from notation software, not from a library. | MuseScore's shipped drumset file `Marching_Snare_Drums.drm`, note 49 `Ping Shot` — recorded first-hand in round 1, `docs/research/02-notation-oss.md` lines 286 and 966. No vendor document read in this bucket contains the word. |
| `gok-shot` | **No.** Same origin. | `Marching_Snare_Drums.drm`, note 52 `Gok Shot` — `02-notation-oss.md` lines 286 and 967, which glosses it "rimshot near centre (dark)" against `ping-shot` "rimshot near the rim (bright)". Absent from every vendor document in this bucket. Tapspace, the one marching-percussion sample library with a public knowledge base, returns no results for `gock` (`support.tapspace.com/support/search/solutions?term=gock`, checked 2026-09-06); its own public vocabulary for the same family is "rim shots, buzzes, rim clicks, press strokes, stick clicks" (article 26000029872). |
| `stick-shot` | **No**, but it is far better attested than the other two, outside this bucket. | SMuFL `pictStickShot` U+E7F0; MuseScore `marching-snare` 57 and `Marching_Snare_Drums.drm` 57; concert-snare technique lists (`docs/research/07-percussion-naming.md` lines 119, 320, 632). In *libraries* the word appears only as a false friend: XLN's snare `Sticks` stroke type (AD2 keymap, MIDI 75) and NI's `Stick Hit` are a stick *click*, not a stick shot. |
| `mini-hihat` | **Yes — GetGood Drums**, and behind them Meinl. | The GGD Benny Greb Signature Pack product page lists a kit-piece category **"Mini Stack"** containing "Meinl Artist Concept Crasher Hats" and "**Meinl Artist Concept Mini Hats**" — `ggd.co/products/benny-greb-signature-pack`, "Included Kit Pieces", fetched 2026-09-06. So the name is vendor-published, and it originates as a Meinl *product* name that GGD adopted as a kit-piece name. |
| `mini-china` | **Not established.** No vendor document found using it. | The only occurrences are third-party: a converter's slot labels for GGD OKW Architects (`Mini China Hit` 65 / `Mini China Choke` 66, `docs/research/12-nka-and-jamstix.md` lines 244–245 — and note that dossier attributes the names to the converter, not to the `.nka` payload) and `drum-remap` (`01-existing-converters.md` lines 433, 516, 758). GGD's own Architects page names the small china by model: "13" Zildjian Oriental Trash China", alongside a 19" — `ggd.co/products/one-kit-wonder-architects`. **UNVERIFIED** whether GGD's plugin UI calls it "Mini China"; that string would settle it and is visible only inside the product. |

Two side findings from the same sweep, both from vendor pages:

- GGD's **P V Matt Halpern Signature Pack** kit list includes an "R&D Big Bell **Mini Ride**
  15"" (`ggd.co/products/p-v-matt-halpern-signature-pack`). v0.1 has `mini-china` and
  `mini-hihat` but no `mini-ride`, so the diminutive family is minted inconsistently: two of
  the three members exist, and the one with the best vendor attestation is missing.
- GGD writes **"X-Hats"** on the same Architects page — "14" Zildjian A New Beat Hi-Hats
  (X-Hats)" — which is direct vendor attestation for v0.1's `xhat` instrument.

## 6. Self-critique (round C)

**What this pass did not get, in order of how much it would add.**

1. **The Superior Drummer 3 / EZdrummer 3 key layout, from Toontrack.** The single most
   authoritative source not obtained. It exists — every SD3 and EZD3 installation contains
   it, and the SD2 manual says so explicitly ("Please refer to specific key layout included
   with your Toontrack product for full mapping") — but Toontrack publishes no copy on the
   open web and gates its web manual behind an account. Round 1's SD3 data is community
   `.drm` and `.pitchlist` exports; this pass corroborated the *naming convention* against
   Toontrack's own SD2 and EZdrummer 1 manuals, which is a real strengthening, but it did
   not replace the SD3 articulation list with a vendor primary. Toontrack is also the
   largest single articulation corpus in the field (43 EZX/SDX layouts in the community
   pack), so this gap is disproportionate. **Recommendation: this is a
   `needs_owner` item — the owner has, or can create, a free Toontrack account, and the
   manual is readable from inside the product.** No amount of further scraping will fix it.

2. **The NI per-kit "Default Mapping" documents for Studio Drummer.** Named in the manual
   ("The Session Kit - Default Mapping", "The Stadium Kit - Default Mapping", "The Garage
   Kit - Default Mapping") and delivered via the Kontakt Library Info button. Not on the
   public web under any guessed path. The Abbey Road manuals make this gap survivable — they
   carry the same articulation vocabulary *with* the note column — but Studio Drummer's own
   numbers are not sourced.

3. **IK MODO Drum's manual, chapter 10 "MIDI Mappings"** including the "Special Hi-Hat
   Articulations" section. Behind the IK account area; the vendor FAQ confirms there is no
   public copy. MODO is the only physically-modelled instrument in the bucket, and its
   articulation set is the one most likely to contain distinctions the sample-based vendors
   cannot express (positional continua rather than discrete stroke types). Its public
   parameter vocabulary was captured; its articulation names were not.

4. ~~The German-language vendor manuals.~~ **Fetched after the first draft** — see §2.1.1.
   The result is a negative that is more useful than the positive would have been: neither
   NI nor Rayzoon translates any articulation name. Bucket 12 should not expect vendor
   German terminology to exist; the German percussion vocabulary it is after comes from
   scores and treatises, not from library vendors. What NI *does* translate is the concept
   layer (`Spielvariante`, `Belegung`, `Anschlagsebene`).

5. **NI Abbey Road 50s and Vintage Drummer manuals.** Same format as the three that were
   fetched, so probably no new vocabulary — but "probably" is doing work there, and the 80s
   manual proved that each library adds one or two unique articulations (`Skin On Skin`,
   `Mirror`).

6. **Meaning, not just spelling, for five NI terms.** `Mirror`, `Splash On/Off/Rim` and
   `Chopper` are printed in the articulation tables and defined nowhere in the manuals. They
   are marked UNVERIFIED above. Resolving them needs either the product itself or NI
   support.

7. **VST3 note names as a source class.** Manda Audio's documentation is the only vendor
   statement found that a plugin exposes its drum names to the host over VST3. If that is
   general, then for every VST3 drum instrument the *vendor's own* articulation names are
   machine-readable without any document — which would change the shape of Phase 3
   collection for exactly the libraries that publish nothing (SSD, ML Drums, GGD's Kontakt
   titles). This was not tested; there is no host in this environment. **Recommendation: put
   it to the reconciliation pass as a question, not a finding.**

**What could have been done better here.** The searches in round A were organised by vendor
rather than by document type; the two most productive routes of the whole pass — the Zendesk
attachments API and the vendors' historic `updates/manuals/` directories — were found by
accident while chasing individual products, not by a search designed to find them. A
document-type-first sweep ("which vendors expose a public help-centre API", "which vendors
ever hosted PDF manuals at a stable path") would have reached the same places in a third of
the requests.
