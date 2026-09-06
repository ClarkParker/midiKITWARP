# Dossier 10 — Licensing / provenance, and stable ID schemes

Status: research complete. Two copy-ready recommendations at §2.8 (provenance record) and
§3.3–§3.13 (ID rules). Everything above those is the evidence they rest on.

Not legal advice. Every legal statement below is sourced; where I am reasoning rather than
quoting, the line is marked **[reasoned]**. Where a fact could not be verified it is marked
UNVERIFIED.

---

## 1. Scope and method

Cloned and read on disk (all under `scratchpad/repos/`):

| Repo | What was read |
|---|---|
| `DigitalInBlue/ReaperNoteNames` | `LICENSE`, `README.md`, full `git log` after `--unshallow` |
| `lotkey/Drum-MIDI-Converter` | `LICENSE`, source headers, `src-python/conversions.lkcmap` |
| `JPplayground/MidiNoteNameGen` | `LICENSE.txt`, per-file headers in `src/*.py` |
| `marty-615/drum-remap` | directory listing incl. dotfiles, `package.json`, `README.md` |
| `insomnimus/drum-mapper` | `LICENSE`, `readme.md`, `drums/` |
| `markheath/midifilemapper` | full tree, `README.md`, `MidiFileMapper/Maps/*.xml`, `*.cs` |
| `musescore/MuseScore` | `LICENSE.txt`, `share/templates/*.drm` |
| `lilypond/lilypond` | `COPYING`, `ly/drumpitch-init.ly` header |
| `hydrogen-music/hydrogen` | `COPYING`, `data/drumkits/GMRockKit/drumkit.xml` |
| `VCVRack/Rack` | `LICENSE.md` (trademark clause) |
| `information-artifact-ontology/ontology-metadata` | `omo-full.owl` — extracted the full obsolescence-reason vocabulary programmatically |
| `pciutils/pciids` | `README.md`, `pci.ids` header |
| plus `thebruce/drumCartographer`, `Abstractize/drum-midi-remapper`, `EFHIII/midi-ch`, `bsp2/libanalogrytm`, `pedrolcl/VMPK`, `eggert/tz`, `alsa-project/alsa-ucm-conf` for licence comparison |

Fetched: CJEU C-203/02 and C-338/02 (EUR-Lex), §§87a–87e UrhG (gesetze-im-internet.de,
dejure.org, juraforum.de), CC BY 4.0 legalcode, CC0 1.0 (read verbatim from disk),
RFC 8126, RFC 5646, Unicode stability policies, UTS #35 Part 6, OBO Foundry ID policy,
OBO Academy obsoletion how-to, CVE CNA Operational Rules 4.1.0 (PDF → `pdftotext`),
LOINC editorial policy, SNOMED CT inactivation docs, Groove Monkee licence agreement.

Could not obtain:
- `confluence.ihtsdotools.org` — DNS does not resolve from this environment. SNOMED
  inactivation reasons are therefore taken from `docs.snomed.org` and secondary sources;
  the *complete* enumeration is UNVERIFIED, though the mechanism is not.
- CC BY 4.0 §4 could not be retrieved character-for-character (the fetcher summarises).
  The §4 text quoted in §2.6 is reproduced from the licence as I know it; its **structure
  and the operative clauses were confirmed** against the fetched legalcode. Marked as such.
- `stash.reaper.fm` terms of use: the site is JS-rendered and no terms page was found.
  The Reaper Stash's upload licensing is UNVERIFIED — see §2.4, which is why the verdict
  for it is conservative.

---

# TOPIC 1 — LICENSING AND PROVENANCE

## 2.1 The EU database right: OBTAINING vs CREATING

Directive 96/9/EC Art. 7(1) gives a *sui generis* right to the maker of a database that
shows "qualitatively and/or quantitatively a substantial investment in either the
obtaining, verification or presentation of the contents". On 9 November 2004 the Grand
Chamber decided four cases the same day and drew one line through all of them.

**C-203/02 British Horseracing Board v William Hill**, operative ruling 1 (verbatim):

> "The expression 'investment in … the obtaining … of the contents' of a database in
> Article 7(1) of Directive 96/9/EC … must be understood to refer to the resources used to
> seek out existing independent materials and collect them in the database. It does not
> cover the resources used for the creation of materials which make up the contents of a
> database."

Para 31, the purpose behind it:

> the directive aims to "promote the establishment of storage and processing systems for
> existing information and not the creation of materials capable of being collected
> subsequently."

Para 34 extends the same cut to verification:

> "The resources used for verification during the stage of creation of data … cannot
> therefore be taken into account."

Para 41, applied to the horse list:

> "The resources used to draw up a list of horses in a race … do not represent investment
> in the obtaining and verification of the contents of the database in which that list
> appears."

**C-338/02 Fixtures Marketing v Svenska Spel** (and its siblings C-46/02 Oy Veikkaus,
C-444/02 OPAP) apply the identical test to football fixture lists. Operative ruling is
word-for-word the BHB formula. Para 31: the resources spent deciding dates, times and team
pairings are investment in *creating* the fixture list — inseparable from organising the
league — and so fall outside Art. 7(1) entirely.

The three limbs, from C-338/02 paras 24 and 27:
- **obtaining** — locating pre-existing independent materials and assembling them;
- **verification** — monitoring the accuracy of collected materials, at creation of the
  database and during its operation;
- **presentation** — systematic arrangement plus individual accessibility.

### 2.1.1 What this means for a manufacturer's own note map

Roland deciding that on a TD-30 pad input 3 emits note 48 is the exact analogue of the
Football League deciding that Arsenal play Chelsea on 4 May. Roland is not *finding* that
fact anywhere; Roland is *making* it. The engineering spend that produced the module is
investment in creating the data, and under BHB ¶30/¶38 and Fixtures ¶31 it does not count
toward Art. 7(1). Consequences, stated flatly:

- **A manufacturer's own factory note map carries no sui generis database right.**
  Roland, Toontrack, XLN, inMusic: same answer. Their maps are created data. **[reasoned,
  but the reasoning is the direct application of the operative rulings above.]**
- It also carries no copyright in the individual assignments: "note 38 = Snare" is a fact,
  and under German law §2(2) UrhG a work requires a *persönliche geistige Schöpfung*.
  A number-to-name correspondence is not one.
- What *could* attract protection is the maker's own **expression around** the data — the
  prose of the manual, the layout of a PDF key-map graphic, the selection and arrangement
  if it rises to a *Datenbankwerk* under §4 UrhG. So: transcribe the facts, never
  photocopy the page, never reproduce the artwork.

There is one real caveat and it must be stated: the fact that the maker has no *database
right* does not mean the maker has no *contract*. See §2.1.3.

### 2.1.2 What this means for a curated third-party collection

Here the answer flips, and this is the part that matters most for KITWARP.

A third-party curator — the Reaper Stash uploader, the maintainer of ReaperNoteNames,
Groove Monkee compiling maps for thirty libraries — is doing precisely what BHB ¶30 calls
protectable: "resources used to seek out existing independent materials and collect them
in the database". They did not create the note assignments. They went and found them,
checked them against installed products, normalised the spelling, and arranged them.
That is obtaining, verification and presentation, all three.

German case law confirms the collection case. **BGH I ZR 130/04 "Gedichttitelliste I"**
(24.05.2007): a list of poem titles compiled from *existing published sources* was held to
be a protected database under §87a UrhG, with the substantial-investment threshold met at
around EUR 34,900 of expenditure. The material was entirely pre-existing; the investment
was in the finding and checking. That is the third-party-collection fact pattern exactly.

So, answering the question directly: **yes — a curated collection can acquire a sui generis
database right even though every individual fact inside it is free.** The facts stay free.
The collection does not.

What that right forbids, and — just as important — what it does not:

| Act | Permitted? |
|---|---|
| Reading the collection to learn that TD-30 pad 3 = note 48 | **Yes.** No right in the fact. |
| Independently verifying that fact against the Roland manual and recording it | **Yes.** You obtained it elsewhere. |
| Copying twenty entries out of a two-thousand-entry collection, once | **Probably yes** — insubstantial quantitatively (BHB ¶70) and qualitatively (¶71 measures the *investment* in the extracted part, and ¶72/¶78: "The intrinsic value of the materials … does not constitute a relevant criterion"). |
| Copying the whole collection, or the part of it that represents most of the curator's work | **No.** Extraction of a substantial part. |
| Copying twenty entries a week for a year until you have the whole thing | **No.** Art. 7(5) / §87b(1) sentence 2 — see §2.2. This is exactly the loophole those provisions exist to close (BHB ¶85–86). |
| Copying the collection's *structure and selection* — which layouts it chose to cover, in what order, with what normalised naming | **This is the real exposure.** Selection and arrangement is the protected investment. |

**Practical rule for KITWARP, and it is not a legal technicality — it is a data-quality
rule that happens to also be the legal safe harbour:** a third-party collection may be used
as a *worklist* (which devices to cover, which slots to check) and as a *cross-check*
(does our value agree with theirs?), but the value that ships must have been obtained from
a manufacturer document, a product file, or a measurement. That is what the
`method` / `corroborated_by` split in §2.8 is for.

### 2.1.3 The Ryanair trap — no database right does not mean no restriction

**C-30/14 Ryanair v PR Aviation** (15.01.2015): the CJEU held that Directive 96/9/EC

> "is not applicable to a database which is not protected either by copyright or by the
> sui generis right under that directive, so that Articles 6(1), 8 and 15 of that
> directive do not preclude the author of such a database from laying down contractual
> limitations on its use by third parties."

Read that backwards and it is alarming. The Directive's *user protections* (lawful-user
rights, the ban on overriding contracts) only exist for *protected* databases. A database
with **no** sui generis right gets **no** statutory user protection either — the owner is
free to restrict it by contract as tightly as they like.

This is directly load-bearing for KITWARP:
- **Groove Monkee.** Their licence agreement states the contents "may NOT be used in any
  way to train AI models", and "may not be used to create or contribute to any competitive
  product, including but not limited to drum loops or bass loops in any format including
  MIDI, Audio files or patterns generated by 'Artificial Intelligence'". Whether or not
  their mapping tables carry a database right is irrelevant: anyone who accepted that
  agreement is bound by it, and *KITWARP is plainly a competitive product* in the sense of
  that clause. **Verdict: forbidden. Do not ingest Groove Monkee material, do not
  cross-check against it, do not have it on the machine that builds the dataset.**
- Product EULAs (Toontrack, XLN, Roland) may contain reverse-engineering or
  data-extraction clauses. Reading a *published manual* is outside any EULA. Reading a
  *shipped product file* is inside one. That is why §2.8's `method` vocabulary keeps
  `manufacturer-doc` and `product-file` as separate values — they carry different risk.
- §87e UrhG voids contract terms that forbid use of *insubstantial* parts. It does not
  help against a clause forbidding use of the whole. Do not rely on it.

---

## 2.2 German UrhG §§ 87a–87e

Verbatim, from gesetze-im-internet.de and dejure.org (current consolidated text):

**§ 87a Abs. 1 Satz 1 — Begriffsbestimmungen**

> "Datenbank im Sinne dieses Gesetzes ist eine Sammlung von Werken, Daten oder anderen
> unabhängigen Elementen, die systematisch oder methodisch angeordnet und einzeln mit
> Hilfe elektronischer Mittel oder auf andere Weise zugänglich sind und deren Beschaffung,
> Überprüfung oder Darstellung eine nach Art oder Umfang wesentliche Investition
> erfordert."

§ 87a Abs. 1 Satz 2 adds that a substantially modified database counts as a new database
where the modification itself requires a substantial investment (the "rolling protection"
problem — every serious update restarts the 15-year clock in practice).

**§ 87a Abs. 2**

> "Datenbankhersteller im Sinne dieses Gesetzes ist derjenige, der die Investition im
> Sinne des Absatzes 1 vorgenommen hat."

**§ 87b Abs. 1 — Rechte des Datenbankherstellers** (both sentences, verbatim)

> "Der Datenbankhersteller hat das ausschließliche Recht, die Datenbank insgesamt oder
> einen nach Art oder Umfang wesentlichen Teil der Datenbank zu vervielfältigen, zu
> verbreiten und öffentlich wiederzugeben. Der Vervielfältigung, Verbreitung oder
> öffentlichen Wiedergabe eines nach Art oder Umfang wesentlichen Teils der Datenbank
> steht die wiederholte und systematische Vervielfältigung, Verbreitung oder öffentliche
> Wiedergabe von nach Art und Umfang unwesentlichen Teilen der Datenbank gleich, sofern
> diese Handlungen einer normalen Auswertung der Datenbank zuwiderlaufen oder die
> berechtigten Interessen des Datenbankherstellers unzumutbar beeinträchtigen."

§ 87b Abs. 2 applies §10(1), §17(2) and §27(2)–(3) accordingly.
§ 87b Abs. 3 (recent) disapplies Abs. 1 in the cases of **Art. 43 of Regulation (EU)
2023/2854 (Data Act)** — i.e. no sui generis right in data obtained from or generated by
the use of a connected product. Not obviously relevant to note maps, but it is the current
direction of travel and worth a line in the ADR. **[reasoned]**

**§ 87c — Schranken.** Reproduction of a substantial part is permitted for private use
(excluded for electronic databases), scientific research, teaching illustration, **text
and data mining**, and preservation. Attribution of source is required. Note what is
*not* there: there is no "commercial product development" exception. The TDM limitation
(§44b UrhG, referenced here) permits mining but §44b(2) allows the rightholder to reserve
the right in machine-readable form for online content. **Do not build the KITWARP dataset
on a TDM argument.** **[reasoned]**

**§ 87d — Dauer.** Fifteen years from publication; fifteen years from creation if not
published within that period.

**§ 87e — Verträge über die Benutzung einer Datenbank.** A contractual obligation on a
lawful owner/user of a database copy to refrain from reproducing, distributing or publicly
communicating **insubstantial** parts is invalid *to that extent*, so long as those acts
neither conflict with normal exploitation nor unreasonably prejudice the maker's legitimate
interests. As noted in §2.1.3 — narrow, and useless against a whole-database restriction,
and (per Ryanair) unavailable at all if the database is unprotected.

### 2.2.1 The "wesentlicher Teil" threshold in practice

There is no percentage in the statute and the CJEU refused to give one. What we do have:

- **Quantitatively** (BHB ¶70): "the volume of data extracted … must be assessed in
  relation to the volume of the contents of the whole of that database."
- **Qualitatively** (BHB ¶71): "the scale of the investment in the obtaining, verification
  or presentation of the contents of the subject of the act of extraction."
- **Not** the intrinsic value of the data (BHB ¶72, ¶78). A single critically useful row is
  not thereby a substantial part.
- BHB ¶80: if the extracted materials "did not require … investment independent of the
  resources required for their creation", they are not a substantial part qualitatively.

Operational threshold I recommend KITWARP adopt, deliberately far below any plausible legal
line, because the cost of compliance is near zero and the cost of a dispute is not
**[reasoned]**:

> From any single third-party collection, KITWARP may record at most **10 % of that
> collection's rows, capped at 40 rows**, and only as `cross_check`, never as the shipped
> `source`. Crossing that cap requires an explicit licence from the collection's maintainer,
> recorded in the sources registry.

### 2.2.2 Repeated extraction of insubstantial parts

§87b(1) sentence 2 is the German transposition of Art. 7(5). BHB ¶85–86 explain the point:
the clause exists "to prevent circumvention of the prohibition in Article 7(1)"; ¶95 gives
the test — acts whose "cumulative effect … [is] to reconstitute and/or make available to
the public … the whole or a substantial part of the contents … and thereby seriously
prejudice the investment."

The trap for a project like KITWARP is structural, not malicious: a contributor pulls "just
a few rows" from the Reaper Stash every week for two years, and the cumulative result is
that the Stash has been reconstituted inside KITWARP's dataset one commit at a time.
Nobody ever intended it. Art. 7(5) catches it anyway.

**The only defence that actually works is bookkeeping**, and it must be per-source and
cumulative, not per-commit. This is the second reason the sources registry in §2.8 is a
first-class artefact rather than a comment field: it is the thing that can answer, on
demand, "how much of collection X is in here?"

---

## 2.3 Trademark: using product names as layout / preset names

### 2.3.1 The law

**EU:** Art. 14(1)(c) Regulation (EU) 2017/1001 (EUTMR) — and the identical Art. 14(1)(c)
of Directive (EU) 2015/2436, transposed in Germany as **§ 23 Abs. 1 Nr. 3 MarkenG** —
permits a third party to use the mark

> for the purpose of identifying or referring to goods or services as those of the
> proprietor of the trade mark, in particular where the use of the trade mark is necessary
> to indicate the intended purpose of a product or service, in particular as accessories
> or spare parts

subject to Art. 14(2): the use must be "in accordance with honest practices in industrial
or commercial matters".

**C-228/03 Gillette v LA-Laboratories** (17.03.2005) is the controlling authority. Two
holdings that matter:

1. *Necessity.* Use is "necessary" where it is in practice the only means of providing the
   public with comprehensible and complete information as to the intended purpose.
2. *Honest practices.* Use is dishonest where it (a) suggests a commercial connection with
   the proprietor, (b) takes unfair advantage of the mark's distinctive character or repute,
   (c) discredits or denigrates the mark, or (d) presents the product as an imitation or
   replica.

**C-63/97 BMW v Deenik** is the older companion: an independent garage may say it repairs
BMWs; it may not present itself as part of the BMW network.

### 2.3.2 Applying it to KITWARP

Naming a layout "Superior Drummer 3" is squarely inside Gillette limb 1. There is no other
comprehensible way to tell a user which of thirty note layouts they are selecting. A
paraphrase ("Popular Swedish Metal Sampler Layout") would be *worse* for the consumer,
which is precisely the interest the exception protects. **The naming itself is defensible.**
**[reasoned, from Gillette]**

What breaks limb 2 — the honest-practices proviso — and must therefore be prohibited by
project rule, not left to taste:

| Forbidden | Why |
|---|---|
| Any manufacturer logo, wordmark artwork, house typeface or brand colour in the UI, icon, screenshots or store listing | Gillette (b) — unfair advantage of repute; also plain copyright in the logo |
| The mark in KITWARP's own product name, VST3 vendor string, bundle identifier, installer name, or domain | Gillette (a) — suggests connection |
| A store/plugin title of the form "KITWARP **for** Superior Drummer" | Suggests an official companion product. Note VCV Rack *explicitly permits* "for VCV Rack" — see §2.3.3 — but that is VCV's own grant, and generalising from it is exactly the error |
| Marketing copy implying tested/approved/official compatibility | Gillette (a) |
| Marks rendered with more visual weight than surrounding text | Gillette (b) |

Required, positively:
- Marks appear as plain text, same weight as their neighbours, in a data field
  (`layout.display_name`), never in chrome.
- The generic KITWARP term is the pivot slug; the mark is only ever a *label on a device
  layout row*.
- ™ / ® on first prominent use where the registration is known; a single symbol per screen
  is enough.
- The disclaimer in §2.3.4 in **three** places: repo README, the plugin's About/Credits
  panel, and a `NOTICE.txt` inside the `.vst3` bundle.

### 2.3.3 Real wording used by comparable open-source projects — verbatim

**(1) `insomnimus/drum-mapper`** — the closest possible comparable: an open-source VST3/CLAP
drum-note remapper that ships note maps for Addictive Drums 2, EZdrummer 2/3, SSD 5,
Superior Drummer 3, Ugritone and GGD, and lists them under a heading "Included Libraries".
`readme.md` line 7, verbatim:

> "Trademark and copyright notice: These are 3rd party libraries. This project and it's
> authors are not associated with the respective companies nor are endorsed by them."

(sic, including "it's"). MIT licensed, © 2023 Taylan Gökkaya.

**(2) `VCVRack/Rack`**, `LICENSE.md`, verbatim:

> "The **VCV logo and icon** are copyright © 2017 VCV and may not be used in derivative
> works.
>
> The **"VCV" name** is trademarked and may not be used for unofficial products.
> However, it is acceptable to use the phrase "for VCV Rack" for promotion of your Rack
> plugin. For all other purposes, email support@vcvrack.com."

Useful as the *other side* of the table: this is what a rightsholder's own permission looks
like, and it is why "for X" is safe for VCV and not safe by default for Toontrack.

**(3) `DISTRHO/Cardinal`** (a VCV Rack fork), README, verbatim:

> "All VCV branding has been removed (to the best of our knowledge) in order to avoid any
> trademark issues."

The instructive part is that Cardinal's answer was *behavioural* — strip the branding —
not a disclaimer sentence. That is the stronger move where a mark is not needed for
identification. It does not apply to KITWARP, where the mark *is* needed.

**(4) `MZehren/ADTOF`** (drum-transcription dataset built from third-party charts),
README, verbatim:

> ":warning: we are not affiliated with Rhythm Gaming World and we do not control any
> material, possibly copyrighted, linked there."

The model for a *dataset* project disclaiming both affiliation and control of upstream
material.

**(5) Apache-2.0 §6**, which `thebruce/drumCartographer` ships, verbatim:

> "6. Trademarks. This License does not grant permission to use the trade names,
> trademarks, service marks, or product names of the Licensor, except as required for
> reasonable and customary use in describing the origin of the Work…"

**(6) GPLv3 §7(e)**, present in every GPLv3 repo we read, verbatim:

> "e) Declining to grant rights under trademark law for use of some trade names,
> trademarks, or service marks; or"

(5) and (6) are worth citing in the ADR because they establish the norm that *a copyright
licence never carries a trademark licence* — which is the reason a separate disclaimer is
needed even for MIT/CC-licensed data we lawfully ingest.

### 2.3.4 Copy-ready KITWARP disclaimer

Short form, for the About panel and the README badge area:

```
KITWARP is an independent project. It is not affiliated with, sponsored by, or endorsed by
Toontrack, XLN Audio, inMusic (BFD/Alesis), Steven Slate Drums, GetGood Drums, Roland,
Yamaha, Pearl, or any other manufacturer. All product names, company names and logos are
the trademarks or registered trademarks of their respective owners. They are used here
solely to identify the note layouts to which KITWARP can convert, which is a descriptive
use permitted by Art. 14(1)(c) EUTMR and § 23 Abs. 1 Nr. 3 MarkenG.
```

Long form, for `NOTICE.txt` in the bundle — append to the short form:

```
KITWARP contains no software, samples, presets or documentation belonging to any of these
manufacturers. The note layouts distributed with KITWARP are factual tables of MIDI note
assignments, compiled from published documentation and from measurements of hardware and
software the KITWARP contributors own. Where a layout was compiled with the help of a
third-party collection, that collection is credited in THIRD-PARTY-NOTICES.txt.

No manufacturer has reviewed, approved or verified these layouts. If you are a rights
holder and believe an entry is incorrect or should not be distributed, contact
<address> and it will be corrected or removed.
```

That last sentence is not legally required. It is included because it is the cheapest
possible de-escalation channel, and because every dispute in this space that turned ugly
started with a rightsholder who had no one to write to. **[reasoned]**

---

## 2.4 Per-source licence verdicts

Verdict vocabulary (used again in §2.8):

- **ingest-free** — ship the data, no obligations.
- **ingest-attribute** — ship the data, must appear in `THIRD-PARTY-NOTICES.txt`.
- **rederive-only** — may be *read* to know what to verify; no bytes, no selection and no
  arrangement may be taken; the shipped fact must carry a different, ingestible source.
- **reference-only** — may be cited in documentation; never ingested at all.
- **forbidden** — a contract forbids the use; do not read it for this purpose.

| Source | Licence as actually found on disk | Verdict | Reason |
|---|---|---|---|
| **DigitalInBlue/ReaperNoteNames** | `LICENSE` = **CC0 1.0 Universal**; `README.md` = "licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license … See the `LICENSE` file for full details" | **ingest-attribute** (treat as CC BY 4.0) | Conflict resolved in §2.4.1 |
| **musescore/MuseScore** drumsets (`share/templates/*.drm`) | `LICENSE.txt`: "under the terms of the GNU General Public License **version 3** as published by the Free Software Foundation" — **GPL-3.0-only**, no "or later" | **rederive-only** | GPL-3.0-only cannot be combined with a proprietary VST3 binary. Also: the content is overwhelmingly GM, re-derivable from the GM spec, plus notation-only fields (`line`, `stem`, `head`) KITWARP does not need |
| **lilypond** `ly/drumpitch-init.ly` | Header: "either version 3 of the License, or (at your option) any later version" — **GPL-3.0-or-later**; © 2001–2026 Rune Zedeler, Han-Wen Nienhuys | **rederive-only** | Same GPL problem. The *terms* it uses (`acousticbassdrum`, `hisidestick`, `halfopenhihat`…) are a naming vocabulary and may inform KITWARP slug choices; the file may not be copied |
| **hydrogen** drumkits | Repo `COPYING` = **GPL-2.0**; but each `data/drumkits/*/drumkit.xml` carries a **GPL-3.0-or-later** header *and* `<license>GPL</license>` (GMRockKit © 2024 Glen MacArthur / Sebastian Moors). The repo-level and file-level statements differ | **rederive-only** | GPL either way. Note the internal inconsistency as a cautionary example for our own repo hygiene |
| **marty-615/drum-remap** | **No `LICENSE` file** (verified by `ls -a`), **no `license` field** in `package.json`, **no notice** in `README.md`. Default: all rights reserved | **reference-only** | No grant = no permission. Its *design* (instrument/articulation/role, fallback chains, 1→N expand) is an idea and freely usable; its `maps/` data is not. If the data is wanted, ask the author for an explicit licence and record the answer in the sources registry |
| **insomnimus/drum-mapper** | **MIT**, © 2023 Taylan Gökkaya | **ingest-attribute** | MIT requires the copyright notice and permission notice "in all copies or substantial portions". Its `drums/*.txt` are ingestible. Caveat: the maps are themselves transcriptions of manufacturer maps — the author can only license what he owns, so treat as `third-party-collection` for `method` and re-verify |
| **lotkey/Drum-MIDI-Converter** | `LICENSE` = full GPLv3 text; **no per-file headers found** in `src-python/` or `src-cpp/`, so whether "or later" applies is UNVERIFIED. Treat as **GPL-3.0** | **rederive-only** | The 170-key tree in `src-python/conversions.lkcmap` is the largest non-GM pivot found and is a genuinely valuable *design* reference. Read the design, do not copy the file |
| **JPplayground/MidiNoteNameGen** | `LICENSE.txt` = GPLv3; per-file headers in `src/*.py` say "either version 3 of the License, or (at your option) any later version" → **GPL-3.0-or-later**. Note the map data lives *inside a source file*, `src/ggd_data.py`, under that header | **rederive-only** | Copying `ggd_data.py` is copying GPL source, full stop. The GGD note assignments inside it are facts belonging to nobody and must be re-obtained from GGD documentation |
| **markheath/midifilemapper** | **No licence file anywhere**; no header in `*.cs`; no notice in `README.md`; `MidiFileMapper/Maps/*.xml` carry no notice. Default: all rights reserved | **reference-only** | Same as drum-remap. Its README even solicits contributed maps without stating terms, which makes the position *worse*, not better — the maps may have third-party contributors with no grant at all |
| **Groove Monkee** (mappings) | Proprietary EULA: contents "may not be used to create or contribute to any competitive product…"; redistribution prohibited; AI-training prohibited | **forbidden** | See §2.1.3. Post-Ryanair this contractual restriction stands whether or not a database right exists |
| **REAPER Stash** note-name uploads | **UNVERIFIED** — no terms-of-use page located; uploads are by individual users with no stated licence | **reference-only** | Unknown licence is not a permissive licence. Individual uploaders may be reachable; if one grants terms, record them per-file, not per-site |

### 2.4.1 Resolving ReaperNoteNames: CC0 file vs CC BY README

The repository states two different licences. The git history settles what *happened*, and
that in turn settles what to do.

```
01c5431  2025-02-10 08:20:57 -0500  author "John Farrier <3240972+DigitalInBlue@users.noreply.github.com>"
                                    committer "GitHub"     "Initial commit"
                                    → adds LICENSE (121 lines, CC0 1.0 Universal) + a 2-line README
c613bd9  2025-02-10 08:33:30 -0500  author "John Farrier <john.farrier@polyrhythm.com>"
                                    committer "John Farrier"  "Initial commit."
                                    → expands README by 52 lines, incl. the CC BY 4.0 paragraph
2104a71  2025-02-10 08:34:01 -0500  "Update README.md"  → cosmetic (removes an emoji from the heading)
```

Reading:
- The CC0 file was produced by **GitHub's repository-creation wizard** — the `noreply`
  author address, the `GitHub` committer, the boilerplate message, the fact that it landed
  13 minutes before any actual content. The author picked "Creative Commons" from a
  dropdown.
- The CC BY 4.0 paragraph is the author's **own prose**, written 13 minutes later, and it
  is what he says the project is licensed under. But it points at the wrong file:
  "See the `LICENSE` file for full details" — and that file is CC0.
- Both are public offers by the same rightsholder. Neither has been withdrawn.

**Verdict: comply with CC BY 4.0.**

Why that and not CC0 **[reasoned]**:
1. CC BY 4.0 is the *stricter* of the two offers and satisfying it satisfies both. There is
   no scenario in which attributing John Farrier puts KITWARP in breach of CC0.
2. The cost of compliance is one line in `THIRD-PARTY-NOTICES.txt`. The cost of guessing
   wrong is a licence dispute over a dataset the project's whole credibility rests on.
3. The README paragraph is the more *deliberate* statement; the CC0 file is more plausibly
   a dropdown accident. Relying on someone's accident to take more than they meant to give
   is exactly the behaviour that gets a project blacklisted by the community it depends on.
4. CC's own guidance is that CC0 is not revocable — so a strict reading might say CC0 wins
   as the earlier irrevocable dedication. That reading is *available* to us, and it is why
   this is genuinely ambiguous rather than obviously CC BY. It is not a reading worth
   using.

**Additionally, and independently of the licence:** what the repository contains is 60+
transcriptions of *other people's* note maps — GetGood Drums, Korg, Orchestral Tools,
Solemn Tones, Submission Audio. Neither CC0 nor CC BY can convey rights the uploader never
held. So even under CC0 the correct treatment would be the same: `method =
third-party-collection`, `confidence = single-source` at best, and re-verification against
the manufacturer before shipping.

**Action:** ingest as cross-check; attribute in `THIRD-PARTY-NOTICES.txt`; open an issue
against the upstream repo asking the maintainer to reconcile `LICENSE` and `README`, and
record the outcome in the sources registry. That issue is worth filing on its own merits —
it fixes the problem for everyone downstream.

---

## 2.5 Does ingesting DATA from a GPL repo contaminate?

Short answer: **copying the file does; knowing the fact does not.** The distinction is
sharp, and the discipline that keeps you on the right side of it is a build rule, not a
judgement call.

The reasoning, in order **[reasoned, from the licence texts quoted]**:

1. **The GPL is a copyright licence.** It operates only on what copyright (and, in GPLv3,
   copyright-like rights) reaches. GPLv3 §0, verbatim from `Drum-MIDI-Converter/LICENSE`
   line 77:

   > "'Copyright' also means copyright-like laws that apply to other kinds of works, such
   > as semiconductor masks."

   That phrasing is broad enough to be read as reaching the EU sui generis database right.
   **GPLv2 (Hydrogen's `COPYING`) has no equivalent clause** — I grepped for it; it is
   absent. So a GPLv3 data file arguably carries a database-right grant with the same
   copyleft conditions attached, and a GPLv2 one arguably does not carry the grant at all.
   Either way this cuts *against* copying, never for it.

2. **The individual facts are not copyrightable.** "Note 38 = Snare Center" fails §2(2)
   UrhG (no *persönliche geistige Schöpfung*) and fails *Feist* in the US. A GPL licensor
   cannot make a fact proprietary by putting it in a GPL file — and equally cannot license
   it to you, because it was never theirs. This is the same point as §2.1.1 seen from the
   other side.

3. **But the file is more than its facts.** Its selection (which slots were considered
   worth recording), its arrangement, its comments, its chosen names, and its structure can
   all be protected — as a compilation, as a *Datenbankwerk* (§4 UrhG), or simply as source
   code. `MidiNoteNameGen/src/ggd_data.py` is not a data file at all; it is a Python module
   with a GPL header. Copying it is copying GPL source. There is no argument to be had.

4. **Therefore the only safe operation is re-derivation**, and re-derivation has to be
   real, not nominal:
   - The GPL source may be used as a **worklist**: it tells you that GGD Invasion has an
     X-hat and that you should go find out which note it is.
     A worklist is an idea, and ideas are not protected.
   - The **value that ships** must come from `manufacturer-doc`, `product-file` or
     `measured`.
   - If a fact exists *only* in the GPL source and cannot be independently confirmed:
     **drop it.** Do not ship it with a hand-wave. A dataset whose distinguishing feature
     is trustworthiness cannot contain rows we could not check.
   - The GPL repo is recorded in `corroborated_by`, never in `source_id`.

5. **Never mechanically transform a GPL file into a KITWARP file.** A script that reads
   `conversions.lkcmap` and emits `kitwarp/device/*.json` produces a derivative work, and
   the fact that a program did the copying changes nothing. This is the rule that is
   easiest to break accidentally during a "quick bootstrap import", so it belongs in CI:
   **no file under `data/` may have a build-time dependency on any path under a
   `rederive-only` source.**

6. **Aggregation is not a defence here.** GPLv3's "mere aggregation" clause covers separate
   works on the same distribution medium. A note table compiled into the plugin's data
   segment and consulted by the plugin's mapping engine is not an aggregate; it is part of
   the work.

**CC0** is the clean case: §2 of the CC0 text (read verbatim from
`ReaperNoteNames/LICENSE`) waives, among "Copyright and Related Rights", item (v) "rights
protecting the extraction, dissemination, use and reuse of data in a Work" and item (vi)
"database rights (such as those arising under Directive 96/9/EC…)". A CC0 source imposes no
conditions at all. Note §4(a): CC0 does **not** waive trademark or patent rights — which is
the third reason the §2.3.4 disclaimer is needed regardless of data licensing.

---

## 2.6 CC BY 4.0 attribution for a dataset shipped inside a plugin binary

§3(a)(1) requires, if supplied, that you **retain**: (i) identification of the creator(s)
and anyone designated for attribution; (ii) a copyright notice; (iii) a notice referring to
the licence; (iv) a notice referring to the disclaimer of warranties; (v) a URI or hyperlink
to the Licensed Material so far as reasonably practicable. §3(a)(1)(B) requires you to
indicate if you modified the material and retain an indication of previous modifications.
§3(a)(1)(C) requires you to indicate the licence and include its text or a URI.

§3(a)(2), verbatim from the fetched legalcode:

> "You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the
> medium, means, and context in which You Share the Licensed Material. For example, it may
> be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource
> that includes the required information."

**§4 Sui Generis Database Rights** is the clause that actually bites for KITWARP. Its
structure and operative content were confirmed against the fetched legalcode; the wording
below is the standard CC BY 4.0 §4 text **[quoted from the licence; character-level
fidelity not machine-verified in this environment — see §1]**:

> "Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of
> the Licensed Material:
> a. for the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse,
>    reproduce, and Share all or a substantial portion of the contents of the database;
> b. if You include all or a substantial portion of the database contents in a database in
>    which You have Sui Generis Database Rights, then the database in which You have Sui
>    Generis Database Rights (but not its individual contents) is Adapted Material; and
> c. You must comply with the conditions in Section 3(a) if You Share all or a substantial
>    portion of the contents of the database."

Read §4(b) against KITWARP's own position: KITWARP's device-layout corpus is *precisely* a
database in which KITWARP will have obtaining/verification investment (§2.1.2 applies to us
too). So incorporating a substantial portion of a CC BY database makes **KITWARP's
database Adapted Material** — which means the "indicate if you modified" duty applies at the
database level, not just per row.

### Concrete compliance recipe

1. Ship a file **inside the bundle**: `KITWARP.vst3/Contents/Resources/THIRD-PARTY-NOTICES.txt`.
   Not only a URL. A plugin runs offline; §3(a)(2)'s hyperlink option is "reasonable" for a
   web page, much less so for a DAW plugin whose user may never have network access.
   **[reasoned]**
2. Surface it in the UI: About → "Data credits", scrollable, showing the same file's
   contents verbatim.
3. One block per source, in this exact shape:

```
GGD, Korg and Orchestral Tools note-name files
  Compiled by: John Farrier (DigitalInBlue) and contributors
  From:        https://github.com/DigitalInBlue/ReaperNoteNames
  Licence:     Creative Commons Attribution 4.0 International (CC BY 4.0)
               https://creativecommons.org/licenses/by/4.0/
  Notice:      Licensed "as is", without warranties or conditions of any kind,
               either express or implied. See the licence for details.
  Modified:    Yes. Values were re-verified against manufacturer documentation,
               renamed to the KITWARP pivot vocabulary, and rows KITWARP could not
               independently confirm were removed.
```

That block discharges (i)–(v), 3(a)(1)(B) and 3(a)(1)(C) in one place.

4. Add a database-level statement once, at the top of the same file, for §4(b):

```
The KITWARP layout database is Adapted Material with respect to those sources listed below
that are licensed under CC BY 4.0. It has been modified: values re-verified, renamed to the
KITWARP pivot vocabulary, restructured, and filtered.
```

5. Generate the whole file from the sources registry (§2.8) at build time. A hand-maintained
   notices file goes stale on the first commit that nobody remembers to mirror. Fail the
   build if any `licence_verdict = ingest-attribute` source has no `attribution_string`.

**CC0 sources**: nothing is required. Credit them anyway, in the same file, under a
"Public domain dedications" heading — it costs nothing, CC recommends it, and it makes the
notices file a complete provenance ledger rather than a legal minimum. **[reasoned]**

**MIT sources** (drum-mapper): the MIT text requires "the above copyright notice and this
permission notice shall be included in all copies or substantial portions of the Software",
so MIT sources need the **full licence text**, not a one-line reference. Include it.

---

## 2.7 Summary of Topic 1 as project rules

1. Manufacturer maps are created data → no database right, no copyright in the assignments.
   Transcribe freely; never reproduce artwork or prose.
2. Curated third-party collections *can* be protected; treat every one as if it is.
3. Third-party collections are worklists and cross-checks. They are never the shipped source.
4. Hard cap per collection: 10 % / 40 rows, tracked cumulatively per source, forever.
5. No file from a `rederive-only` source ever enters `data/`. Enforce in CI.
6. Unknown licence = all rights reserved = `reference-only`.
7. Contract beats the absence of a database right (Ryanair). Groove Monkee is `forbidden`.
8. Trademarks: descriptive text use only, in data fields, never in chrome or product name;
   disclaimer in three places.
9. `THIRD-PARTY-NOTICES.txt` is generated from the sources registry, ships in the bundle,
   and is visible in the UI.

---

## 2.8 Recommended provenance record schema

Two tables, deliberately. Per-source facts (licence, URL, terms) belong to the *source*
and change rarely; per-assertion facts (who checked what, when, with what confidence)
belong to the *assertion*. Collapsing them is the single most common way provenance schemas
rot, because the licence then has to be restated on every one of ten thousand rows and the
restatements drift. **[reasoned]**

### 2.8.1 `sources` — one row per external source

```yaml
sources:
  - id: src.reaper-note-names            # stable, opaque-ish slug; never reused
    kind: repository                     # repository | manual | product-file | website |
                                         # forum-post | vendor-correspondence | measurement-rig
    title: "ReaperNoteNames"
    publisher: "John Farrier (DigitalInBlue) and contributors"
    locator: "https://github.com/DigitalInBlue/ReaperNoteNames"
    version: "5644e07"                   # commit / doc revision / firmware version / edition
    retrieved: 2026-09-06
    licence_declared:                    # what the source SAYS, possibly more than one
      - spdx: "CC0-1.0"
        evidence: "LICENSE (added by GitHub repo wizard, commit 01c5431)"
      - spdx: "CC-BY-4.0"
        evidence: "README.md ## License section, commit c613bd9"
    licence_applied: "CC-BY-4.0"         # what WE comply with — exactly one
    licence_resolution: >
      Two inconsistent grants by the same rightsholder 13 minutes apart. We comply with the
      stricter offer. See dossier 10 §2.4.1.
    licence_verdict: ingest-attribute    # controlled, see §2.4
    attribution_required: true
    attribution_string: |                # verbatim block for THIRD-PARTY-NOTICES.txt
      GGD, Korg and Orchestral Tools note-name files
        Compiled by: John Farrier (DigitalInBlue) and contributors
        ...
    redistribute_data: true              # may the values themselves ship?
    extraction_budget:                   # §2.2.1 cap, tracked cumulatively
      total_rows_in_source: 2431
      rows_taken: 118
      cap_rows: 40                       # → OVER BUDGET; CI must fail
      cap_fraction: 0.10
    contact: "https://github.com/DigitalInBlue/ReaperNoteNames/issues"
    notes: "Upstream is itself a transcription of manufacturer maps; re-verify everything."
```

`extraction_budget` is not decoration. It is the only artefact that can answer the Art. 7(5)
/ §87b(1) s.2 question in §2.2.2, and it has to be cumulative across the project's whole
history, which means it must live in version control next to the data.

### 2.8.2 `provenance` — one or more records per assertion

An *assertion* is one (device_layout, note_number) → (pivot_id) binding, or one pivot entry
definition. Every shipped assertion carries at least one provenance record.

```yaml
provenance:
  - assertion: "layout:toontrack.sd3/note:38 -> pivot:1042"
    source_id: src.toontrack-sd3-manual
    method: manufacturer-doc            # closed vocabulary, §2.8.3
    locator: "SD3 Operation Manual v3.3, p.114, 'Key Map — Core Library'"
    quote: "38  Snare — Center hit"     # verbatim; REQUIRED for manufacturer-doc
    obtained: 2026-09-06
    observer: "dev@example.org"
    confidence: documented              # closed vocabulary, §2.8.5
    licence_verdict: rederive-only      # closed vocabulary, §2.8.4 — inherited from source,
                                        # overridable downward, never upward
    corroborated_by: [src.drum-mapper, src.reaper-note-names]
    conflicts_with: []
    tracker: "https://github.com/<org>/kitwarp/issues/214"
```

Field-by-field, with the rule that makes each one worth its cost:

| Field | Type | Required | Rule |
|---|---|---|---|
| `assertion` | string | yes | the thing being claimed; stable across the row's life |
| `source_id` | FK → `sources.id` | yes | never a free-text URL; that is what `sources` is for |
| `method` | enum | yes | §2.8.3 |
| `locator` | string | yes | must be precise enough for a second person to reach the same page/screen/dump without asking. "the manual" is not a locator |
| `quote` | string | **required when `method = manufacturer-doc`**, else optional | the verbatim excerpt. Cheap to capture at the time, impossible to reconstruct later |
| `obtained` | date | yes | when the observation was made, not when the row was written |
| `observer` | string | yes | a person or a rig identifier. Anonymous provenance is not provenance |
| `confidence` | enum | yes | §2.8.5 — describes the FACT |
| `licence_verdict` | enum | yes | §2.8.4 — describes WHAT WE MAY DO |
| `corroborated_by` | [source_id] | no | sources that agree but are not the shipped source |
| `conflicts_with` | [assertion ref] | no | non-empty ⇒ `confidence` must be `disputed` |
| `tracker` | URL | no | issue/ADR where the decision was argued. Borrowed from IAO:0000233 `term tracker item` |
| `superseded_by` | provenance ref | no | when a better source replaces a worse one, the old record is kept, not overwritten |

Provenance records are **append-only**. When a better source is found you add a record and
mark the old one superseded; you never edit it. The history of *how we came to believe this*
is the asset. **[reasoned]**

### 2.8.3 Controlled vocabulary for `method`

Closed set, ordered from most to least authoritative:

| Value | Definition | Typical locator | Licence risk |
|---|---|---|---|
| `manufacturer-doc` | Published documentation by the maker of the device or library: printed manual, PDF, official web key-map page, official support article. | "TD-30 Owner's Manual, p.86" | Lowest. Reading a published manual is outside any EULA. Transcribe facts only. |
| `product-file` | A machine-readable file shipped by the maker *with the product*: `.iom`, `.pitchlist`, `.nka`, `.drm`, a vendor-supplied note-names `.txt`, a factory preset, a SysEx template. | "SD3 install: Resources/Maps/Core.tsvmap" | **Higher than it looks.** Access is normally governed by a EULA. Check the EULA before extraction; record the check. |
| `measured` | Observed by operating the actual hardware or software: MIDI monitor capture, SysEx dump, screenshot of the product's own mapping page, a pad struck and the note recorded. | "SysEx dump `td30-2026-09-06.syx`, sha256 …" | Lowest of all for third-party rights, highest for effort. This is the gold standard. |
| `third-party-collection` | A curated collection made by someone who is not the maker: ReaperNoteNames, drum-mapper's `drums/*.txt`, a Reaper Stash upload, a forum table, another converter's map file. | "repo path + commit" | **Highest.** Database right may subsist (§2.1.2). Budget-capped. Cross-check only. |
| `inferred` | Derived by KITWARP from other assertions rather than observed: family pattern completion, GM default, interpolation across an instance series. | must name the rule, e.g. `rule:gm-default` | None. But it is the lowest-trust value and must be visible to the user. |

Two additions I recommend beyond the five requested, because without them the five are
forced to lie **[reasoned]**:

| Value | Definition | Why the five are not enough |
|---|---|---|
| `vendor-support` | A direct written answer from the maker's support or development team (email, ticket, forum post by a staff account). | Stronger than any third-party collection — it is the maker speaking — but it is not *published documentation*, so it cannot be `manufacturer-doc`, and forcing it into `third-party-collection` would wrongly subject it to the extraction budget and wrongly downgrade its confidence. |
| `user-report` | An individual's report about their own installation, uncurated. | A forum user saying "on my TD-27 it's note 26" is not a *collection* and carries none of a collection's curation investment. Filing it as `third-party-collection` inflates both its trust and its legal risk. |

If the five-value set must stay closed, map `vendor-support` → `manufacturer-doc` with a
mandatory `locator` prefix of `correspondence:` and `user-report` → `third-party-collection`
with `confidence: single-source`. But the seven-value set is the honest one.

### 2.8.4 Recording a licence verdict per entry

`licence_verdict` on a provenance record is inherited from `sources.licence_verdict` and
may only be **narrowed**, never widened. Enumeration and the operational meaning of each:

| Value | May the bytes ship? | Notices entry? | CI rule |
|---|---|---|---|
| `ingest-free` | yes | optional (do it anyway) | — |
| `ingest-attribute` | yes | **required** | build fails if `sources.attribution_string` is empty |
| `ingest-restricted` | yes, conditions met | required, conditions named | build fails unless `conditions_satisfied: true` with evidence |
| `rederive-only` | **no** | no | build fails if any file under `data/` has a build-time dependency on the source path; the shipped assertion must carry a *different* provenance record whose verdict permits shipping |
| `reference-only` | **no** | no | may appear only in `docs/`; build fails on any reference from `data/` |
| `forbidden` | **no** | no | the source id may not appear anywhere in the repo, including in `corroborated_by` |

The invariant that makes this enforceable in one line of CI:

> Every shipped assertion must have **at least one** provenance record whose
> `licence_verdict` is `ingest-free`, `ingest-attribute` or `ingest-restricted`.
> Records with `rederive-only` or `reference-only` are permitted on the same assertion and
> are informative — they say what we consulted — but they cannot satisfy this rule alone.

That single invariant is what turns §2.5's re-derivation discipline from a good intention
into something a machine checks.

### 2.8.5 Recording confidence

Ordered enum, most to least trustworthy. **`confidence` is about the FACT; `method` is
about HOW we got it; `licence_verdict` is about WHAT WE MAY DO.** Three orthogonal
questions — never collapse them into one "quality" score.

| Value | Means | Typically arises from |
|---|---|---|
| `measured` | Observed on the actual device or plugin, reproducibly, with an artefact on file | `method: measured` |
| `documented` | Stated by the maker in published documentation or direct correspondence | `manufacturer-doc`, `product-file`, `vendor-support` |
| `corroborated` | Two or more **independent** third-party sources agree, and none dissents | ≥2 `third-party-collection` with different lineage |
| `single-source` | Exactly one third-party source; unverified | one `third-party-collection` or `user-report` |
| `inferred` | Derived by a named rule; never observed | `method: inferred` |
| `disputed` | Sources conflict and the conflict is unresolved | `conflicts_with` non-empty |

Rules attached to it:
- "Independent" means *different lineage*, not different URLs. Two collections that both
  copied the same forum post are one source. Where lineage is unknown, it is not
  independent. This is the single most-often-broken rule in community datasets.
- `disputed` rows must never ship as a default mapping. They ship as a flagged alternative
  or not at all.
- Rows whose best confidence is `single-source` or `inferred` must be **surfaced in the
  UI** as unverified. There is good precedent from inside this exact domain:
  `marty-615/drum-remap`'s README already marks one bundled map "**unverified**" and
  annotates each map's source in a table ("user screenshots + 3 cross-checked sources",
  "official XLN keymap PDF"). Do the same, but structurally rather than in prose.
- Confidence may be raised only by adding a provenance record, never by editing one.

---

# TOPIC 2 — STABLE ID SCHEMES

## 3.1 Survey of comparable registries

| Registry | ID form | Meaning in the ID? | Reuse | Deprecation | Supersession | Split handling | Version expression |
|---|---|---|---|---|---|---|---|
| **Unicode code points** | 21-bit integer + immutable `Name` string | Blocks are grouped by script, but the code point itself asserts nothing normative | **Never.** "Once a character is encoded, it will not be moved or removed." (Encoding Stability, Unicode 2.0+) | `Deprecated` property; character stays | `NameAliases.txt` formal aliases (types: correction, control, alternate, figment, abbreviation). "Formal aliases, once assigned to a character, will not be changed or removed." (5.0+) | Not applicable — characters are not split | `MAJOR.MINOR.UPDATE` (17.0.0) plus dated UCD snapshots |
| **IANA registries (RFC 8126)** | varies; often small integers or strings | Sometimes ranged, but ranges partition by *who assigns*, not by semantics | Strongly discouraged: §9.4 "Reclaiming previously assigned values for reuse is tricky, because doing so can lead to interoperability problems with deployed systems." Hostile reclamation needs IESG Approval | §9.6 entries marked `obsolete` or `deprecated`; "the information in the registry remains there for informational and historic purposes" | Additional reference document | Ad hoc per registry | Per-registry; entries carry references, not versions |
| **BCP 47 / IANA Language Subtag Registry (RFC 5646)** | short strings | Yes, and it caused the problem below | Never within the registry | `Deprecated` field (a date) | `Preferred-Value` field, single-valued, "RECOMMENDED as the best choice to represent the value of this record" | Not directly supported | `File-Date` on the registry |
| **ISO 3166-1 alpha-2** | 2-letter string | Fully meaning-bearing | **Yes — after a reservation period.** Deleted codes reserved ≥50 years, transitionally reserved ≥5 years | Withdrawal + reservation categories | None in-band | None in-band | Newsletters / editions |
| **CLDR / UTS #35** | inherits ISO codes | inherited | inherited | `<territoryAlias type=… reason="deprecated">`; reasons: deprecated, overlong, macrolanguage, legacy, bibliographic | `replacement` attribute, **space-delimited, multi-valued** | **`<territoryAlias type="CS" replacement="RS ME"/>`** — one deprecated code, ordered list of successors, first is preferred | `MAJOR.MINOR` tied to release trains |
| **MusicBrainz MBID** | UUID | None whatsoever | Never | n/a | On merge "its MBIDs redirect to the other entity"; "An entity can have more than one MBID" | n/a | Schema versions; data is continuous |
| **LOINC** | numeric code + check digit | None | "LOINC codes are never removed from the database and meaning of a code is never changed over time" | `STATUS` ∈ ACTIVE, TRIAL, DISCOURAGED, DEPRECATED | `MAP_TO` field names the superseding term | not first-class | `MAJOR.MINOR` (2.79) |
| **SNOMED CT** | numeric SCTID | Partition bits only (namespace/type), not semantics | Never; concepts inactivated, not deleted | Concept inactivation indicator: Ambiguous, Duplicate, Erroneous, Outdated, Limited, Moved elsewhere, Non-conformance to editorial policy, Meaning of concept unknown, Classification derived | Historical association refsets: SAME AS, REPLACED BY, POSSIBLY EQUIVALENT TO, WAS A, MOVED TO, ALTERNATIVE | **Ambiguous** + multiple POSSIBLY EQUIVALENT TO targets | `effectiveTime` (date) on **every row** |
| **OBO Foundry / IAO** | `PREFIX:0000001`, 7 digits | **Explicitly forbidden**: "LOCALID should not be semantically meaningful, therefore numeric IDs should be used" | "Each OBO ID is assigned to a only single term within the set of all OBO ontologies" | `owl:deprecated true`; label prefixed `obsolete `; definition prefixed `OBSOLETE.` | `IAO:0100001 term replaced by` (automatic substitution) vs `oboInOwl:consider` (manual evaluation) | `IAO:0000229 term split` — "The term has been split into two or more new terms" | Dated release IRIs |
| **CVE** | `CVE-YYYY-NNNNN` | Year only | REJECTED IDs stay in the namespace; not reassigned | `REJECTED` state with a mandatory explanation (rule 4.5.3.7) | REJECTED description points at the surviving ID | rule 4.5.3.9: "CNAs MAY separate or split CVE ID assignments, assigning new CVE IDs and publishing corresponding CVE Records as necessary." | Per-record versions |
| **IEEE OUI / MA-L** | 24-bit block | None | Permanent, no expiry; not reassigned | n/a | n/a | n/a | n/a |
| **pci.ids** | vendor:device hex pairs assigned by PCI-SIG | Vendor prefix = change controller | Vendor-controlled | n/a | n/a | n/a | Dated file header (`Version: 2026.09.05`) |

Three findings drop out of that table and they are the ones that matter:

**(a) Every registry that survived long enough to matter refuses to reuse identifiers.**
Unicode, LOINC, SNOMED, OBO, CVE, MusicBrainz, IEEE. The one that *does* reuse — ISO
3166-1, after a reservation period — is the one everyone else had to build a workaround for.

**(b) The ISO 3166 lesson is documented in the wild.** RFC 5646 §2.2.4 rule 4.C, verbatim:

> "When ISO 3166-1 reassigns a code formerly used for one country or area to another
> country or area and that code already is present in the registry, the UN numeric code for
> that country or area MUST be registered in the registry as described in Section 3.4 and
> MUST be used to form language tags that represent the country or region for which it is
> defined (rather than the recycled ISO 3166-1 code)."

BCP 47 will *not accept* a recycled meaning-bearing code and falls back to opaque numbers.
That is the whole argument for meaning-free IDs, made by a standards body that had to live
with the alternative.

**(c) The two-identifier pattern is universal.** Opaque stable key + human-readable label,
with different stability guarantees on each. Unicode: code point (immutable) + Name
(immutable, corrected via alias). LOINC: code (immutable) + FSN (revisable). MusicBrainz:
MBID (immutable) + name (freely editable). pci.ids: numeric ID (assigned by PCI-SIG) +
name string (community-maintained). None of them makes the human-readable string the key.

## 3.2 What this means for the open question in `00-draft-axes.md`

The draft asks: "whether to reserve ID ranges per family (readability) or keep IDs
meaning-free (ISO 3166 reassignment lesson)."

**Keep IDs meaning-free.** Reasons, in order of force:

1. **A range is an assertion, and assertions get revised.** If `2000–2099` means "cymbal",
   then the day a slot turns out to be a stack (cymbal + closed hat, one sound, one note),
   the ID either lies forever or has to move — and it cannot move. The vocabulary's own
   axes already tell you it is a cymbal; the ID does not need to, and if it does, it is a
   second, unversioned, unfixable copy of the classification.
2. **OBO Foundry states the rule outright**: "LOCALID should not be semantically
   meaningful, therefore numeric IDs should be used." This is a community that maintains
   hundreds of thousands of terms across decades and arrived at it the hard way.
3. **Ranges create reuse pressure.** A family fills up; the obvious fix is to reclaim the
   deprecated IDs inside that family; and RFC 8126 §9.4 is the record of why that goes
   badly. Meaning-free IDs simply never run out and never tempt anyone.
4. **Readability is not the ID's job.** It is `slug`'s job (§3.4). Nobody reads `2043`.
   Everybody reads `hihat.closed.tip`. Making the integer readable buys nothing and costs
   the ability to reclassify.
5. **The honest counter-argument**, stated fairly: IANA *does* allocate ranges, and pci.ids
   *is* grouped by vendor. But look at what those ranges partition — the **change
   controller**, i.e. *who may assign*, not *what the thing is*. Vendor 0x8086 is not a
   claim about the device's function. That distinction is the whole difference, and it
   gives KITWARP the one range split that is worth having:

> **The only permitted ID partition is by assigning authority, never by instrument family.**
> `1 … 999_999` — core KITWARP vocabulary.
> `1_000_000 …` — private / third-party extension space, never assigned by the core.

Precedent: IANA private-use ranges; BCP 47 `x-` private-use subtags; MIDI's own
manufacturer SysEx ID space.

## 3.3 Rule 1 — two identifiers, different jobs

Every pivot entry carries both:

- **`id`** — opaque, monotonically assigned positive integer. Assigned once. Never reused,
  never reassigned, never meaning-bearing. This is the storage key and the wire format.
- **`slug`** — stable human-readable string, e.g. `hihat.closed.tip`. Unique. **Immutable
  once published.** This is what appears in hand-edited device-layout files, error
  messages, diffs and documentation.

`display_name` (e.g. "Hi-hat, closed, tip") is a third, **mutable** field — the LOINC FSN
analogue — and is explicitly *not* an identifier.

## 3.4 Rule 2 — integer on the wire, slug in the files

- **Store and transmit `id`.** Fixed width, cheap comparison on the audio thread, immune to
  case-folding and Unicode-normalisation arguments, and — decisively — it forces every
  consumer to go through the vocabulary table, which is what makes deprecation actually
  work. A codebase that string-matches `"hihat.closed.tip"` will silently ignore the day
  that slug is deprecated.
- **Author in `slug`.** Device layout files under `data/devices/` are hand-edited; they
  reference slugs. A build step resolves slug → id and **fails** on an unknown, `draft` or
  `withdrawn` slug. This is the pci.ids arrangement: numeric IDs are the truth, the names
  file is the human layer.
- Emitted artefacts (plugin state, presets, exported maps) carry `id` plus the
  `vocabulary_serial` they were written against (§3.10). Never a bare slug.

## 3.5 Rule 3 — never delete, and say so publicly

Adopt this as a written stability pledge in the repo, in Unicode's voice, and treat
breaking it as a release blocker:

```
KITWARP Pivot Vocabulary Stability Policy

1. Encoding stability.  Once a pivot entry is published in a released vocabulary version,
   its `id` will not be reassigned, reused, or removed. The entry may be deprecated.
2. Slug stability.      Once published, an entry's `slug` will not be changed. Incorrect
                        slugs are corrected by adding a `correction` alias, never by
                        editing the slug.
3. Alias stability.     Once assigned to an entry, an alias will not be changed or removed.
4. Meaning stability.   The meaning of an active entry will not be narrowed or broadened.
                        If the meaning must change, the entry is deprecated and one or more
                        new entries are minted.
```

Clauses 1–3 are Unicode's Encoding Stability, Name Stability and Formal Name Alias
Stability policies transposed. Clause 4 is the one Unicode does not need and KITWARP does,
because our entries are *definitions*, not characters — and it is the clause that makes
§3.7's split procedure mandatory rather than optional. **[reasoned]**

## 3.6 Rule 4 — lifecycle states

Closed set, four values:

| State | Resolvable by readers? | Emitted by encoders? | Offered in the UI? |
|---|---|---|---|
| `draft` | pre-release builds only | no | no |
| `active` | yes | yes | yes |
| `deprecated` | yes | no | no (but shown when reading old data, marked) |
| `withdrawn` | yes | **never** | no |

`deprecated` vs `withdrawn` is LOINC's DISCOURAGED/DEPRECATED distinction: `deprecated`
means "don't use it for new work"; `withdrawn` means "this was wrong and must not be
written even by a stubborn tool". `draft` is LOINC's TRIAL — present in the file, flagged,
and explicitly changeable, which is what stops pre-release experimentation from silently
becoming a permanent commitment.

## 3.7 Rule 5 — supersession fields

Copy-ready, adapted from IAO/OBO + SNOMED + BCP 47 + CLDR:

```yaml
- id: 1042
  slug: hihat.closed.tip
  status: deprecated
  deprecated_in: "3.0.0"
  deprecation_reason: split            # closed set, §3.7.1
  supersession_kind: split-into        # closed set, §3.7.2
  superseded_by: [1310, 1311]          # ORDERED, most-preferred first. May be empty.
  see_also: [1288]                     # unordered, non-normative
  tracker: "https://github.com/<org>/kitwarp/issues/214"
  migration_note: >
    Devices that expose a separate edge zone map note 22 to 1310 (tip) and note 26 to
    1311 (edge). Devices with a single closed-hat note map to 1310.
```

### 3.7.1 `deprecation_reason` — closed vocabulary

Lifted from the IAO obsolescence-reason individuals (extracted verbatim from
`omo-full.owl`) and SNOMED's inactivation indicators, spelled in KITWARP terms:

| KITWARP value | Source term | Meaning |
|---|---|---|
| `split` | IAO:0000229 *term split* — "The term has been split into two or more new terms." | The slot conflated two or more distinct sounds |
| `merged` | IAO:0000227 *terms merged* — "The term has been combined with one or more other terms to create a more encompassing (merged) term." | Folded into a broader entry |
| `duplicate` | SNOMED *Duplicate* | Another entry already meant exactly this |
| `erroneous` | SNOMED *Erroneous* | The entry described something that does not exist as described |
| `ambiguous` | SNOMED *Ambiguous* | Meaning was never determinate; unlike `split`, no clean successor set exists |
| `out-of-scope` | OMO:0001000 *out of scope* — "The term was added to the ontology on the assumption it was in scope, but it turned out later that it was not." | Belongs to the controller vocabulary, or to event metadata, not to the pivot |
| `placeholder-removed` | IAO:0000226 *placeholder removed* — "The term was created to temporarily stand in for a semantic purpose, but is no longer needed…" | A scaffold entry from early drafting |

Seven values, each with a real-world definition behind it. Do not invent an eighth without
an ADR.

### 3.7.2 `supersession_kind` and the automatic-rewrite rule

| Value | SNOMED / OBO analogue | May a decoder rewrite silently? |
|---|---|---|
| `same-as` | SNOMED SAME AS | **Yes**, if `superseded_by` has exactly one element |
| `replaced-by` | IAO:0100001 *term replaced by* — "Use on obsolete terms, relating the term to another term that can be used as a substitute" | **Yes**, if exactly one element |
| `split-into` | IAO:0000229 + SNOMED POSSIBLY EQUIVALENT TO | **No.** Apply `superseded_by[0]` and mark the result degraded, or ask |
| `merged-into` | IAO:0000227 | **Yes** — the target is broader, so the rewrite is lossy-but-correct; mark degraded |
| `consider` | `oboInOwl:consider` — "potential replacements that require manual evaluation" | **No.** Never automatic |

This is exactly OBO's distinction between `term replaced by` (automatic substitution) and
`consider` (manual evaluation), and it is exactly CLDR's "first replacement is preferred"
rule for multi-valued aliases. Encode it once in the resolver and every downstream tool
inherits correct behaviour.

## 3.8 Rule 6 — SPLIT, when one pivot slot turns out to be two sounds

**Do not keep the old ID for either half.** That is the ISO 3166 reassignment mistake in
miniature: the ID's meaning silently narrows, and every file already written with it now
claims something more specific than its author meant.

Procedure:

1. **Mint N new IDs** for the N distinct sounds. Never reuse the old ID for any of them.
2. Old entry: `status: deprecated`, `deprecation_reason: split`,
   `supersession_kind: split-into`, `superseded_by: [new1, new2, …]` ordered by expected
   frequency (most common reading first — CLDR orders `CS → RS ME` by population, same
   idea).
3. Write a `migration_note` giving the disambiguation rule if one exists (source device,
   incoming note number, adjacent-slot context). If no rule exists, say so — an honest
   "cannot be disambiguated automatically" is worth more than a silent guess.
4. **Bump MAJOR.** A split is breaking: data written before the split cannot be losslessly
   rewritten, because the information needed to choose a successor was never recorded.

Precedents, both real:
- CLDR: `<territoryAlias type="CS" replacement="RS ME" reason="deprecated"/>` — one
  deprecated code, ordered multi-valued replacement, first preferred.
- CVE rule **4.5.3.9**: "CNAs MAY separate or split CVE ID assignments, assigning new CVE
  IDs and publishing corresponding CVE Records as necessary."

**The test that decides whether something is a split at all** — apply it before touching
anything:

> *Would any already-emitted data using the old ID be **wrong** under the new reading?*
> **Yes** → it is a split. Deprecate, mint N new IDs, MAJOR.
> **No** → it is an addition. The old entry keeps its ID and its meaning; you are simply
> adding a sibling that was previously unrepresented. MINOR.

Most "we need to split this" reports turn out to be additions on inspection. Running the
test first is what keeps the MAJOR version from churning.

## 3.9 Rule 7 — MERGE, when two slots turn out to be one sound

1. **Choose the survivor by age and exposure, not aesthetics.**
   CVE rule **4.5.3.8**, verbatim: "CNAs MAY combine or merge CVE ID assignments. CNAs MUST
   reject published CVE IDs and CVE Records that become redundant after the change. When
   deciding which CVE IDs and CVE Records to reject, CNAs SHOULD consider factors such as
   the time of publication and the extent of public use and awareness."
   MusicBrainz community practice says the same in one line: target the MBID that has been
   public the longest.
2. Loser: `status: deprecated`, `deprecation_reason: duplicate` (or `merged` if the
   survivor is a new, broader entry), `supersession_kind: same-as`,
   `superseded_by: [survivor]`.
3. Decoders rewrite loser → survivor silently. Encoders never emit the loser.
4. **Bump MINOR, not MAJOR** — old data still resolves, and resolves correctly.
   *Unless* the distinction was load-bearing for someone (a device layout used both slots
   to mean different things). If so it is not really a merge; it is a merge plus a split,
   and it is MAJOR. Record which in the ADR.

**State the asymmetry explicitly in the policy document: splits are breaking, merges are
not.** It is counter-intuitive — merging feels more destructive — and getting it backwards
is how projects end up with a MAJOR bump every release and users who stop reading them.

## 3.10 Rule 8 — versioning: semver AND a monotonic serial, and they mean different things

Ship both. They answer different questions.

**`vocabulary_version` — SemVer `MAJOR.MINOR.PATCH`. This is the *contract*.**

| Bump | Triggers |
|---|---|
| **MAJOR** | any entry deprecated with reason `split` or `ambiguous`; any change to the meaning of an active entry; removal of an axis or an axis value; any change under which previously-valid data resolves differently |
| **MINOR** | new entries; new axis values; merges; new aliases; deprecations with a single unambiguous `same-as` / `replaced-by`; new device layouts |
| **PATCH** | `display_name`, descriptions, `tracker` links, notes, documentation. **Never a `slug`.** |

**`vocabulary_serial` — a monotonically increasing integer, +1 on every published build,
never reset.** This is the *identity* of a build. It goes in file headers, in exported
presets, and in bug reports.

Why both, concretely **[reasoned, but the failure mode is well attested]**: SemVer is not
totally ordered in practice — hotfix branches, pre-releases, and two maintainers bumping
MINOR in parallel all produce version strings a human cannot rank at a glance. A user
reporting "my map broke" needs to be able to say *which* vocabulary they have, and a
support engineer needs to rank two of them instantly. `3.2.0` vs `3.1.4` is ambiguous if
`3.1.4` shipped later off a hotfix branch. `serial: 118` vs `serial: 121` never is.

Precedent for carrying both: Unicode ships `17.0.0` *and* dated UCD snapshots; CVE has
year-based IDs plus per-record versions; SNOMED CT ships an `effectiveTime` on every single
row.

**And, following SNOMED and BCP 47, put the stamp on every row too:**
- `added_in` — the vocabulary version in which the entry first appeared.
- `deprecated_in` — required when `status ≠ active`.

RFC 5646 §3.4 makes exactly these fields part of its stability guarantee: "Values in the
fields 'Type', 'Subtag', 'Tag', and 'Added' MUST NOT be changed and are guaranteed to be
stable over time." Adopt the same: `id`, `slug`, `added_in` and any assigned alias are
immutable for the life of the project.

## 3.11 Rule 9 — slug immutability and the alias escape hatch

Slugs will contain mistakes. A misspelling, a wrong family (`crash.china.*` for something
that is really a stack), a name the community rejects. **Do not edit a published slug.**
Unicode's reasoning applies verbatim: character names are immutable, and therefore
"misspellings and incorrect names will never be corrected clerically", because
implementations key on them.

Instead:

```yaml
- id: 1042
  slug: hihat.closed.tip
  aliases:
    - {value: "hihat.closed.tipp", kind: deprecated}   # a spelling that once shipped
    - {value: "hh.cl.tip",         kind: abbreviation}
    - {value: "hihat.tip.closed",  kind: alternate}    # widely used elsewhere
    - {value: "hihat.closed.tip",  kind: correction}   # if the published slug were wrong
```

`kind` is Unicode's `NameAliases.txt` type set, minus the two that have no analogue here
(`control`, `figment`): **`correction`, `alternate`, `abbreviation`, `deprecated`**.

Rules:
- Any slug or alias resolves to the entry. Resolution is exact-match, case-sensitive.
- An alias, once assigned, is never changed or removed (Unicode Formal Name Alias
  Stability, 5.0+).
- Display uses the `correction` alias if one exists, else `slug`.
- An alias may never collide with another entry's `slug` or alias. CI enforces global
  uniqueness across the union of all slugs and all aliases, including deprecated and
  withdrawn entries — **forever**, because that union is exactly the set of strings that
  must keep resolving unambiguously.

## 3.12 Rule 10 — the deprecate-and-supersede pattern, as other projects actually do it

Four real examples, for the ADR's "how do others do this" section:

1. **Unicode, U+FE18.** Its Name contains a typo: `PRESENTATION FORM FOR VERTICAL RIGHT
   WHITE LENTICULAR BRAKCET` (sic, "BRAKCET"). Because names are immutable, the typo is
   permanent. It is addressed by a formal alias of type `correction` in `NameAliases.txt`.
   The character was never renamed and never moved. **UNVERIFIED at character-level detail
   in this environment** (I did not fetch `NameAliases.txt`), but the mechanism is
   documented in the stability policy quoted above and in UTN #27 "Known anomalies in
   Unicode Character Names".
2. **CVE.** A published record found to be a duplicate is not deleted; it is set to
   `REJECTED` with a mandatory explanation pointing at the surviving ID (rules 4.5.3.6–.8).
   The ID stays in the namespace and is never reassigned.
3. **OBO Foundry.** `owl:deprecated true`; label prefixed `obsolete `; definition prefixed
   `OBSOLETE.`; logical axioms stripped; `IAO:0100001 term replaced by` when the
   replacement is unambiguous, `oboInOwl:consider` when it is not;
   `IAO:0000231 has obsolescence reason` from a closed list; `IAO:0000233 term tracker
   item` pointing at the issue where it was decided. And the governing sentence, from the
   OAK documentation: "A good ontology will never *delete* an identifier, but will instead
   mark it as obsolete."
4. **LOINC.** "If a LOINC term is identified as erroneous or a duplicate of a previous term
   it is flagged as deprecated in the database, but the record is not removed", with the
   replacement named in `MAP_TO`. "LOINC codes are never removed from the database and
   meaning of a code is never changed over time."

## 3.13 Copy-ready pivot entry schema

```yaml
# vocabulary/pivot.yaml
vocabulary_version: "3.0.0"      # semver — the contract
vocabulary_serial: 121           # monotonic integer — the build identity
generated: 2026-09-06

entries:
  - id: 1310                                   # opaque, monotonic, never reused
    slug: hihat.closed.tip                     # immutable once published
    display_name: "Hi-hat — closed, tip"       # mutable
    status: active                             # draft | active | deprecated | withdrawn
    added_in: "3.0.0"
    parent: 1300                               # hihat.closed
    axes:
      instrument: hihat
      instance: {ordinal: 1}
      zone: tip
      openness: 0                              # ordered scalar, named anchors elsewhere
      technique: hit
      implement: stick
    aliases:
      - {value: "hh.cl.tip", kind: abbreviation}
    tracker: "https://github.com/<org>/kitwarp/issues/214"

  - id: 1042
    slug: hihat.closed                         # the pre-3.0 conflated slot
    display_name: "Hi-hat — closed"
    status: deprecated
    added_in: "1.0.0"
    deprecated_in: "3.0.0"
    deprecation_reason: split
    supersession_kind: split-into
    superseded_by: [1310, 1311]                # ordered, most-preferred first
    migration_note: >
      Conflated tip and edge. Devices exposing both map note 22 -> 1310 and note 26 -> 1311;
      devices with a single closed-hat note map to 1310.
    tracker: "https://github.com/<org>/kitwarp/issues/214"
```

### CI invariants (all cheap, all catch a real class of bug)

1. `id` is unique across all entries, including deprecated and withdrawn — forever.
2. `id` values are never removed from the file between releases; a missing `id` fails.
3. The union of every `slug` and every `aliases[].value`, over all entries of all statuses,
   is globally unique.
4. No published `slug` or alias ever changes value. Compare against the previous release.
5. `status != active` ⇒ `deprecated_in` and `deprecation_reason` are present.
6. `supersession_kind ∈ {same-as, replaced-by, merged-into}` ⇒ `len(superseded_by) == 1`.
7. `deprecation_reason == split` ⇒ `supersession_kind == split-into` and
   `len(superseded_by) >= 2` and the release bumps MAJOR.
8. Every `superseded_by` target exists and is not itself `withdrawn`.
9. No supersession cycles.
10. Every device-layout file resolves every slug it references to an `active` entry;
    referencing `draft`, `deprecated` or `withdrawn` fails the build.
11. `id >= 1_000_000` may not appear in the core vocabulary file.
12. Every shipped assertion satisfies the §2.8.4 licence invariant.

---

## 4. Provenance of this dossier

### Case law and legislation

| Item | URL | Licence / status |
|---|---|---|
| CJEU C-203/02 *British Horseracing Board v William Hill* | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62002CJ0203 | EUR-Lex reuse policy (Decision 2011/833/EU) — free reuse with source acknowledgement |
| CJEU C-338/02 *Fixtures Marketing v Svenska Spel* | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62002CJ0338 | ditto |
| CJEU C-46/02, C-444/02 *Fixtures Marketing* | https://ipcuria.eu/case?reference=C-444/02 | ditto |
| CJEU C-30/14 *Ryanair v PR Aviation* | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A62014CJ0030 | ditto |
| CJEU C-228/03 *Gillette v LA-Laboratories* | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62003CJ0228 | ditto |
| BGH I ZR 130/04 *Gedichttitelliste I* | https://www.telemedicus.info/urteile/Urheberrecht/Datenbankschutz/297-BGH-Az-I-ZR-13004-Gedichttitelliste-I.html | secondary report; primary text not fetched — the EUR 34,900 figure is UNVERIFIED against the judgment |
| § 87a UrhG | https://www.gesetze-im-internet.de/urhg/__87a.html | official, free of copyright (§5 UrhG) |
| § 87b UrhG | https://dejure.org/gesetze/UrhG/87b.html · https://www.juraforum.de/gesetze/urhg/87b-rechte-des-datenbankherstellers | ditto |
| § 87c UrhG | https://dejure.org/gesetze/UrhG/87c.html | ditto |
| §§ 87d, 87e UrhG | https://www.gesetze-im-internet.de/urhg/__87d.html · https://lxgesetze.de/urhg/87e | ditto |
| Art. 14 EUTMR (Reg. 2017/1001) | https://eur-lex.europa.eu | ditto |

### Licences read verbatim

| Item | Where |
|---|---|
| CC0 1.0 Universal, §§1–2 (database-rights waiver) | `scratchpad/repos/ReaperNoteNames/LICENSE`, lines 1–104 |
| CC BY 4.0 §3(a)(2), §4 | https://creativecommons.org/licenses/by/4.0/legalcode.en |
| GPL-3.0 §0 "copyright-like laws" | `scratchpad/repos/Drum-MIDI-Converter/LICENSE` line 77 |
| GPL-3.0 §7(e) trademark decline | ibid. lines 379–380 |
| GPL-2.0 (no copyright-like clause) | `scratchpad/repos/hydrogen/COPYING` |
| Apache-2.0 §6 Trademarks | `scratchpad/repos/thebruce_drumCartographer/LICENSE` lines 138–139 |
| MIT | `scratchpad/repos/drum-mapper/LICENSE` |

### Repositories examined (all clones under `scratchpad/repos/`)

| Repo | Commit / state | Licence found |
|---|---|---|
| DigitalInBlue/ReaperNoteNames | `5644e07`, unshallowed to 8 commits | LICENSE = CC0-1.0; README = CC-BY-4.0 (conflict, §2.4.1) |
| lotkey/Drum-MIDI-Converter | depth-1 | GPL-3.0 (LICENSE only; "or later" UNVERIFIED) |
| JPplayground/MidiNoteNameGen | depth-1 | GPL-3.0-or-later (per-file headers) |
| marty-615/drum-remap | depth-1 | **none** |
| insomnimus/drum-mapper | depth-1 | MIT © 2023 Taylan Gökkaya |
| markheath/midifilemapper | depth-1 | **none** |
| musescore/MuseScore | depth-1, blob:none | GPL-3.0-**only** |
| lilypond/lilypond | depth-1 | GPL-3.0-or-later |
| hydrogen-music/hydrogen | depth-1 | GPL-2.0 repo / GPL-3.0-or-later in `drumkit.xml` |
| VCVRack/Rack | depth-1 | GPL-3.0 + plugin exception; trademark clause in LICENSE.md |
| DISTRHO/Cardinal | README fetched via web | GPL-3.0-or-later |
| information-artifact-ontology/ontology-metadata | depth-1 | CC-BY-4.0 (IAO/OMO) |
| pciutils/pciids | depth-1 | GPL-2.0-or-later OR BSD-3-Clause |
| thebruce/drumCartographer | depth-1 | Apache-2.0 |
| Abstractize/drum-midi-remapper | depth-1 | MIT © 2025 Gabriel Abarca Aguilar |
| EFHIII/midi-ch | depth-1 | GPL-3.0 |
| MZehren/ADTOF | depth-1 | CC BY-NC-SA 4.0 |

### Registry and standards documentation

| Item | URL |
|---|---|
| Unicode Character Encoding Stability Policies | https://unicode.org/policies/stability_policy.html |
| Unicode Registered Code Stability Policy | https://www.unicode.org/policies/reg_stability_policy.html |
| UTN #27 Known anomalies in Unicode Character Names | https://www.unicode.org/notes/tn27/tn27-1.html |
| RFC 8126 §§2.3, 6, 9.4, 9.5, 9.6 | https://www.rfc-editor.org/rfc/rfc8126.html |
| RFC 5646 §§2.2.4, 3.1.6, 3.1.7, 3.4 | https://www.rfc-editor.org/rfc/rfc5646.txt |
| UTS #35 Part 6 (CLDR alias elements) | https://unicode-org.github.io/cldr/ldml/tr35-info.html |
| MusicBrainz Identifier | https://musicbrainz.org/doc/MusicBrainz_Identifier |
| MusicBrainz Merge | https://musicbrainz.org/doc/Merge |
| LOINC editorial policies (status values, MAP_TO) | https://loinc.org/kb/users-guide/editorial-policies-and-procedures/ |
| SNOMED CT Attribute Value Reference Set | https://docs.snomed.org/snomed-ct-specifications/snomed-ct-release-file-specification/reference-set-release-file-specification/5.2-reference-set-types/5.2.1-content-reference-sets/5.2.1.3-attribute-value-reference-set/5.2.1.3-attribute-value-reference-set |
| SNOMED CT inactivate concept (extension guide) | https://docs.snomed.org/snomed-ct-practical-guides/snomed-ct-extension-guide/5-key-steps/5.4-authoring/5.4.2-authoring-concepts/5.4.2.3-inactivate-concept-in-an-extension |
| OBO Foundry Identifier Policy | http://obofoundry.org/id-policy.html |
| OBO Academy — Obsoleting a term | https://oboacademy.github.io/obook/howto/obsolete-term/ |
| OAK — Obsoletion | https://incatools.github.io/ontology-access-kit/guide/obsoletion.html |
| CVE CNA Operational Rules 4.1.0 (rules 4.5.3.5–.9, 4.5.4.1) | https://www.cve.org/Resources/Roles/Cnas/CNA_Rules_v4.1.0.pdf |
| IEEE MA-L / OUI | https://standards.ieee.org/products-programs/regauth/oui/ |
| ISO 3166 glossary (reserved code categories) | https://www.iso.org/glossary-for-iso-3166.html |
| Groove Monkee License Agreement | https://groovemonkee.com/pages/license-agreement |
| REAPER Stash | https://stash.reaper.fm/ (terms of use not located — UNVERIFIED) |
