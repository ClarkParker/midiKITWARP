# ADR-0004 — Provenance is mandatory, and licence status is machine-checked

**Status:** Proposed
**Date:** 2026-09-06
**Depends on:** ADR-0001

*Not legal advice. Every legal statement below is sourced. Where a source could not be
verified it is marked UNVERIFIED. Before shipping commercially, have a lawyer read this.*

## Context

The project rule is "no number without a source". That rule is worth nothing unless it is
enforced by something other than good intentions, and the surveyed prior art shows why:
`ReaperNoteNames` ships six wrong headers and three duplicate names; `MidiNoteNameGen`
ships `Eye Closed` for *Edge Closed*, `Peal` for *Pedal* and `Ruft` for *Ruff*; the
Toontrack corpus contains `Floot Tom 1` and `Crahs Main R`. Every one of those is now a
"fact" in somebody's dataset.

### The legal position, in one paragraph each

**A single note assignment is a free fact.** "Note 38 is the snare centre hit" is not a
*persönliche geistige Schöpfung* under § 2(2) UrhG and carries no copyright.

**A manufacturer's own note map carries no database right.** Directive 96/9/EC Art. 7(1)
protects investment in *obtaining* data, and the CJEU drew the line on 9 November 2004 in
C-203/02 *British Horseracing Board v William Hill*, operative ruling 1:

> "The expression 'investment in … the obtaining … of the contents' of a database … must be
> understood to refer to the resources used to seek out existing independent materials and
> collect them in the database. It does not cover the resources used for the creation of
> materials which make up the contents of a database."

Roland deciding that TD-30 pad input 3 emits note 48 is the exact analogue of the Football
League deciding a fixture date in C-338/02 *Fixtures Marketing*: Roland is not *finding*
that fact, Roland is *making* it. Created data, so no Art. 7(1) right. The manual's prose
and the artwork of a key-map graphic are a different matter and are not to be reproduced.

**A curated third-party collection is a different answer, and this is the part that
matters.** Someone who goes and finds thirty manufacturers' maps, checks them against
installed products, normalises the spelling and arranges them is doing precisely what BHB
¶30 calls protectable. BGH I ZR 130/04 *Gedichttitelliste I* confirms it for German law: a
list compiled entirely from pre-existing published sources was a protected database, with
the substantial-investment threshold met at roughly EUR 34,900 of expenditure.

So: **the facts stay free; the collection does not.** Reading a collection to learn that a
fact exists is fine. Independently verifying it against the manufacturer's own
documentation and recording that is fine. Copying its selection and arrangement is not, and
copying it twenty rows a week until you have all of it is specifically what Art. 7(5) and
§ 87b(1) sentence 2 exist to stop.

**And a contract beats the absence of a database right.** Post-*Ryanair v PR Aviation*
(C-30/14), where the Directive does not apply, national contract law is not displaced. A
collection whose EULA forbids use in a competing product forbids it whether or not a
database right subsists.

## Decision

### 1. Third-party collections are worklists, never sources

A collection may be used to learn **which devices exist and where the primary source is**.
The shipped assertion must carry a provenance record pointing at a primary source. This is
simultaneously the legal safe harbour and the data-quality rule, which is the reason it is
easy to hold to.

A hard extraction cap per collection — **10 % or 40 rows, whichever is smaller** — tracked
cumulatively in the sources registry, forever, because a cap that resets is not a cap.

### 2. Two tables, not one

Per-source facts (licence, URL, terms) belong to the source and change rarely. Per-assertion
facts (who checked what, when, how confidently) belong to the assertion. Collapsing them is
how provenance schemas rot: the licence gets restated on ten thousand rows and the
restatements drift.

`sources` carries: `id`, `kind`, `title`, `publisher`, `locator`, `version` (commit, manual
revision, firmware version), `retrieved`, `licence_declared[]` (what the source *says*,
possibly more than one), `licence_applied` (exactly one — what we comply with),
`licence_resolution`, `licence_verdict`, `attribution_required`, `attribution_string`,
`extraction_budget`, `contact`, `notes`.

`provenance` carries, per assertion: `assertion`, `source_id`, `method`, `locator`, `quote`,
`obtained`, `observer`, `confidence`, `licence_verdict`, `corroborated_by`,
`conflicts_with`, `tracker`, `superseded_by`.

Provenance records are **append-only**. A better source adds a record and marks the old one
superseded; it never overwrites it. The history of how we came to believe something is the
asset.

### 3. Three orthogonal questions, three fields

`method` says how we got it, `confidence` says how good the fact is, `licence_verdict` says
what we may do with it. Never collapse them into one quality score.

**`method`** — closed, most to least authoritative:
`manufacturer-doc` · `product-file` · `measured` · `vendor-support` · `third-party-collection`
· `user-report` · `inferred`.

`vendor-support` (a written answer from the maker's support or dev team) and `user-report`
(one person's report about their own installation) are included because without them the
other five are forced to lie: a staff email is the maker speaking but is not published
documentation, and one forum post is not a *collection* and carries none of a collection's
curation investment or legal risk.

A `quote` — the verbatim excerpt — is **required** when `method = manufacturer-doc`. It is
cheap to capture at the time and impossible to reconstruct later.

**`confidence`** — `measured` · `documented` · `corroborated` · `single-source` ·
`inferred` · `disputed`. "Independent" for the purpose of `corroborated` means *different
lineage*, not different URLs: two collections that both copied the same forum post are one
source, and where lineage is unknown it is not independent. `disputed` rows never ship as a
default mapping. Rows whose best confidence is `single-source` or `inferred` are surfaced in
the UI as unverified — `marty-615/drum-remap` already does this in prose, marking one
bundled map "unverified"; we do it structurally.

**`licence_verdict`** — `ingest-free` · `ingest-attribute` · `ingest-restricted` ·
`rederive-only` · `reference-only` · `forbidden`. Inherited from the source and may only be
narrowed, never widened.

### 4. The one CI invariant that makes it real

> Every shipped assertion must have at least one provenance record whose `licence_verdict`
> is `ingest-free`, `ingest-attribute` or `ingest-restricted`. Records with `rederive-only`
> or `reference-only` may sit on the same assertion and are informative — they say what we
> consulted — but they cannot satisfy this rule alone.

Plus: no file from a `rederive-only` source ever enters `data/`; a `forbidden` source id may
not appear anywhere in the repository, including in `corroborated_by`; and
`THIRD-PARTY-NOTICES.txt` is generated from the sources registry rather than maintained by
hand.

### 5. Per-source verdicts as of 2026-09-06

| Source | Licence as found on disk | Verdict |
|---|---|---|
| `DigitalInBlue/ReaperNoteNames` | `LICENSE` is CC0 1.0; `README` says CC BY 4.0. Two grants by the same rightsholder 13 minutes apart | **ingest-attribute** — comply with the stricter offer |
| `insomnimus/drum-mapper` | MIT | **ingest-attribute**, but its maps are themselves transcriptions, so re-verify |
| `musescore/MuseScore` drumsets | GPL-3.0-**only** | **rederive-only** |
| `lilypond` `ly/drumpitch-init.ly` | GPL-3.0-or-later | **rederive-only** — its naming vocabulary may inform our slugs; the file may not be copied |
| `hydrogen-music/hydrogen` drumkits | repo `COPYING` GPL-2.0, files claim GPL-3.0-or-later | **rederive-only** |
| `lotkey/Drum-MIDI-Converter` | GPL-3.0 | **rederive-only** — read the 170-key design, do not copy the file |
| `JPplayground/MidiNoteNameGen` | GPL-3.0-or-later, and the map data lives *inside* `src/ggd_data.py` under that header | **rederive-only** |
| `marty-615/drum-remap` | **no LICENSE file, no `license` field, no notice** | **reference-only** — the design is an idea and free to use; `maps/` is not licensed |
| `markheath/midifilemapper` | no licence anywhere | **reference-only** |
| Groove Monkee | EULA forbids use to "create or contribute to any competitive product" | **forbidden** |
| REAPER Stash uploads | no terms-of-use page found | **reference-only** — UNVERIFIED; unknown licence is not a permissive licence |

Copying the file is what the GPL reaches; knowing the fact is not. GPLv3 § 0 is broad
(*"'Copyright' also means copyright-like laws that apply to other kinds of works, such as
semiconductor masks"*) — broad enough to be read as reaching the sui generis database right
— which is exactly why the rule is a build rule and not a judgement call: no bytes from a
`rederive-only` source in `data/`, ever, and no mechanical transform of such a file into
`data/` either, because that is a derivative work regardless of who did the typing. A GPL
repository goes in `corroborated_by`, never in `source_id`. **A fact obtainable only from a
`rederive-only` source, and not independently confirmable, is dropped** — a documented gap
beats a laundered one.

Two consequences of CC BY 4.0 that are easy to miss:

- § 3(a)(2) allows satisfying attribution by a URI, but a DAW plugin may run offline, so
  `THIRD-PARTY-NOTICES.txt` ships **inside** the bundle and is surfaced in the About panel;
  the link is a supplement, not a substitute.
- § 4(b): this project's own layout corpus is itself a database in which the project holds
  obtaining and verification investment. Incorporating a substantial portion of a CC BY
  database therefore makes **our database** Adapted Material, so the duty to indicate
  modification applies at database level, not merely per row. The notices file carries a
  database-level statement as well as per-source blocks.

### 6. Trademarks

Product names identify the layouts this software converts to. That is descriptive use under
Art. 14(1)(c) EUTMR and § 23(1)(3) MarkenG. They appear in data fields and documentation,
never in the product name, the icon, or the UI chrome. The disclaimer ships in three places
(README, About panel, `NOTICE.txt`) and names the manufacturers explicitly, states that the
project contains none of their software, samples, presets or documentation, and gives a
contact address for rights holders — the last not because it is required but because it is
the cheapest de-escalation channel there is.

## Consequences

Curation gets slower per row and the schema gets wider. In exchange the question "where did
this number come from and may we ship it" is answerable by a script rather than by
archaeology, and the extraction budget makes the one genuinely risky activity —
systematically draining a curated collection — impossible to do by accident.

The `forbidden` verdict on Groove Monkee costs a convenient index. That is the correct
trade: the inventory already names the primary sources, and Roland alone publishes one
support article per module.

## Strongest counter-argument

This is a lot of ceremony for a hobby dataset, and the realistic legal exposure of shipping
a table of drum note numbers is close to zero. Every field here is a field a contributor can
fill in wrongly or skip, and a provenance schema that people route around is worse than none.

The answer is that most of the cost falls on the `sources` table, which has tens of rows, not
on the ten thousand assertions, which inherit from it. The per-assertion required set is
small: source, method, locator, date, observer, confidence. Everything else is optional or
derived. If that minimum still proves too heavy in practice, the honest fix is to cut fields
from this ADR by amendment — not to keep a schema nobody fills in.
