# ADR-0003 — Identifier rules and registry mechanics

**Status:** Proposed
**Date:** 2026-09-06
**Depends on:** ADR-0001

## Context

ADR-0001 decided that the pivot is a registry of symbolic terms with stable identifiers.
This ADR fixes the mechanics, because the failure modes are well documented elsewhere and
all of them are cheap to avoid up front and expensive to fix later.

Three concrete failures observed in the surveyed prior art:

- `lotkey/Drum-MIDI-Converter` derives keys from tree paths. Its README: *"If you
  reorganized the tree or removed some kit pieces, the other mappings will not compile."*
- Jamstix 4's flat integer IDs fused instrument and articulation, so later articulations had
  to be bolted on at 38–57 and 90–104; the numbering is non-monotonic and six IDs are
  permanently `RESERVED` holes.
- Hydrogen let instrument types be free-form strings and ended with 219 distinct strings for
  roughly 35 instruments across 54 shipped kits.

External practice was surveyed across Unicode, IANA (RFC 8126), RFC 5646, CLDR,
ISO 639/3166, LOINC, SNOMED CT, CVE, OBO Foundry and IEEE OUI.

The export targets add a hard external requirement: Logic articulation sets key on an
`ArticulationID` that is written into MIDI note events inside the user's project, and
Studio One `.keyswitch@id` and Dorico `baseSwitchID` do the same. An identifier that moves
between releases silently re-points MIDI in projects already saved.

## Decision

### 1. Two identifiers, different jobs

| Field | Mutable | Job |
|---|---|---|
| `id` | never | storage key, wire format, compiled table index |
| `slug` | never once published | what humans read and what layout files reference |
| `display_name` | freely | UI label; explicitly **not** an identifier |

### 2. IDs are meaning-free

An opaque, monotonically assigned positive integer. Never reused, never reassigned, never
derived from a note number, a slug or a tree path.

**No family ranges.** A range is an assertion and assertions get revised; the axes already
say what family a term is in, and duplicating that in the integer creates a second,
unversioned, unfixable copy of the classification. OBO Foundry, maintaining hundreds of
thousands of terms, states it outright: *"LOCALID should not be semantically meaningful,
therefore numeric IDs should be used."* Ranges also create reuse pressure when a family
fills up, and RFC 8126 §9.4 is the record of why reuse goes badly: *"Reclaiming previously
assigned values for reuse is tricky, because doing so can lead to interoperability problems
with deployed systems."*

The honest counter-argument is that IANA does allocate ranges and `pci.ids` is grouped by
vendor. But those ranges partition the **assigning authority**, not the meaning. Vendor
`0x8086` is not a claim about what a device does. That gives the one partition worth having:

```
1 … 999_999      core KITWARP vocabulary
1_000_000 …      private / third-party extension space, never assigned by the core
```

### 3. Integer on the wire, slug in the files

- Store, transmit and compile `id`. It forces every consumer through the vocabulary table,
  which is what makes deprecation actually work — a codebase that string-matches
  `"hihat.closed.tip"` silently ignores the day that slug is deprecated.
- Author in `slug`. Layout files under `data/devices/` are hand-edited and reference slugs;
  the build resolves slug → id and **fails** on an unknown, `draft` or `withdrawn` slug.
  This is the `pci.ids` arrangement: numbers are the truth, the names file is the human
  layer.
- Emitted artefacts carry `id` plus the `vocabulary_serial` they were written against.

### 4. Lifecycle states

| State | Resolvable by readers | Emitted by encoders | Offered in the UI |
|---|---|---|---|
| `draft` | pre-release builds only | no | no |
| `active` | yes | yes | yes |
| `deprecated` | yes | no | shown when reading old data, marked |
| `withdrawn` | yes | never | no |

`deprecated` versus `withdrawn` is LOINC's DISCOURAGED/DEPRECATED distinction: don't use it
for new work, versus this was wrong and must not be written even by a stubborn tool.
`draft` is LOINC's TRIAL, and it is what stops pre-release experimentation from silently
becoming a permanent commitment.

### 5. Stability policy (published in the repository, breaking it is a release blocker)

```
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
Stability policies transposed. Clause 4 is the one Unicode does not need and this project
does, because these entries are definitions rather than characters — and it is what makes
the split procedure mandatory rather than optional.

Slugs will contain mistakes. They are not edited. Unicode's own U+FE18 carries the
permanent typo `… LENTICULAR BRAKCET` and is addressed by a `correction` alias, not a
rename. Alias kinds are Unicode's `NameAliases.txt` set minus the two with no analogue here:
`correction`, `alternate`, `abbreviation`, `deprecated`.

### 6. Supersession

```yaml
- id: 1042
  slug: hihat.closed
  status: deprecated
  deprecated_in: "3.0.0"
  deprecation_reason: split          # closed set
  supersession_kind: split-into      # closed set
  superseded_by: [1310, 1311]        # ordered, most-preferred first
  migration_note: >
    Conflated tip and edge. Devices exposing both map note 22 -> 1310 and note 26 -> 1311;
    devices with a single closed-hat note map to 1310.
  tracker: "https://github.com/ClarkParker/midiKITWARP/issues/…"
```

A **split** — one slot turns out to be two sounds — is a MAJOR bump, because previously
valid data now resolves differently and a human has to decide which way each layout goes.
A **merge** is MINOR: the surviving id absorbs the other, which is deprecated with
`merged-into`.

The pattern is CVE's (`REJECTED` with a pointer, never deleted, ID never reassigned),
OBO's (`owl:deprecated`, label prefixed `obsolete`, `term replaced by` when unambiguous and
`consider` when not, plus a `term tracker item` pointing at where it was decided) and
LOINC's (*"LOINC codes are never removed from the database and meaning of a code is never
changed over time"*).

### 7. Versioning: both a SemVer contract and a monotonic serial

`vocabulary_version` — SemVer, the contract:

| Bump | Triggers |
|---|---|
| MAJOR | any `split` or `ambiguous` deprecation; any meaning change on an active entry; removal of an axis or axis value; anything under which previously valid data resolves differently |
| MINOR | new entries; new axis values; merges; new aliases; unambiguous `same-as` / `replaced-by` deprecations; new device layouts |
| PATCH | display names, descriptions, tracker links, documentation. Never a slug. |

`vocabulary_serial` — a monotonic integer, +1 on every published build, never reset. This
is the build identity. SemVer is not totally ordered in practice: hotfix branches and
parallel MINOR bumps produce version strings a human cannot rank at a glance, and a user
reporting a broken map has to be able to say which build they have. Unicode ships a version
*and* dated UCD snapshots; SNOMED CT puts an `effectiveTime` on every row.

Every entry carries `added_in`, and `deprecated_in` when not active. RFC 5646 §3.4 makes
exactly these fields part of its stability guarantee: *"Values in the fields 'Type',
'Subtag', 'Tag', and 'Added' MUST NOT be changed and are guaranteed to be stable over
time."*

## CI invariants

All cheap, each catching a real class of bug:

1. `id` unique across all entries including deprecated and withdrawn — forever.
2. No `id` disappears between releases; a missing one fails the build.
3. The union of every `slug` and every alias value, over all entries of all statuses, is
   globally unique.
4. No published slug or alias ever changes value — compared against the previous release.
5. `status != active` ⇒ `deprecated_in` and `deprecation_reason` present.
6. `supersession_kind ∈ {same-as, replaced-by, merged-into}` ⇒ exactly one `superseded_by`.
7. `deprecation_reason == split` ⇒ `supersession_kind == split-into`, at least two
   `superseded_by`, and the release bumps MAJOR.
8. Every `superseded_by` target exists and is not itself withdrawn.
9. No supersession cycles.
10. Every layout file resolves every slug it references to an `active` entry.
11. `id >= 1_000_000` may not appear in the core vocabulary file.

## Consequences

The registry file is append-mostly and never shrinks, so it grows monotonically and its
diff is always additive — which is exactly what makes review tractable. Every consumer must
go through a resolution step rather than string-matching, which is a small cost paid once.

Getting a term wrong is now cheap: deprecate, mint, migrate, note it. Getting an *axis*
wrong is still expensive, which is why ADR-0001 spends its budget there.

## Strongest counter-argument

Meaning-free integers make the vocabulary file unreadable without tooling, and the project
is small enough that family ranges would have been convenient for years before they hurt.

That is true, and it is why `slug` exists and why every file humans edit uses slugs rather
than integers. The integer is for the compiler and the wire, and nobody reads `2043`.
