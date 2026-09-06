# ADR-0001 — The pivot is a symbolic, factored, versioned vocabulary

**Status:** Proposed — awaiting sign-off before any device data is collected
**Date:** 2026-09-06
**Supersedes:** —
**Superseded by:** —

## Context

KITWARP translates drum MIDI between layouts through a pivot rather than N×N assignments.
Everything downstream depends on what the pivot *is*. Changing it later invalidates every
layout collected against it, so it is settled first.

### What the existing options actually cost

**A MIDI note number is not a viable pivot.** Measured on the eleven `.iom` reference files
in this repository (`docs/evidence/note-number-pivot-loss.md`, regenerate with
`python -m tools.iom.analyze data/legacy-iom`):

| Layout | source notes mapped | distinct pivot slots hit | loss |
|---|---:|---:|---:|
| Superior Drummer 3 | 120 | 70 | 42 % |
| Pearl Mimic Pro | 120 | 80 | 33 % |
| EZdrummer 2 | 120 | 83 | 31 % |
| … | | | |
| Yamaha DTXplorer | 120 | 115 | 4 % |

1320 mapped source notes collapse onto 1038 slots. One Superior 3 pivot slot absorbs eight
distinct articulations. The ceiling is structural: a note number has 128 values, and
Superior Drummer 3's default map alone names 96 entries while BFD3 names 73.

**Every surveyed converter that used General MIDI as its intermediate is provably lossy,
and its author says so.** `insomnimus/drum-mapper`, `readme.md` line 95:

> Currently mappings other than General MIDI -> X are lossy; the plugin reverses the mapping
> while converting between libraries.

`markheath/midifilemapper`'s own map comments say the same thing in passing — *"we will
allow electric snare through to play a rim shot"*, *"filter out 54 – tambourine"*.

### What the prior art offers

| Project | Pivot | Distinct slots | GM-based |
|---|---|---:|---|
| `insomnimus/drum-mapper` | GM note numbers | 25 used | yes |
| `Abstractize/drum-midi-remapper` | named string keys | 9 | no, but degenerate |
| `markheath/midifilemapper` | none — direct N×N rule files | — | GM by convention |
| `marty-615/drum-remap` | flat `instrument/articulation` tags | 40 pairs, 12 instruments | no |
| Rayzoon Jamstix 4 | flat integer kit-piece IDs | 99 (67 acoustic) | no |
| `lotkey/Drum-MIDI-Converter` | hierarchical key tree | **170** | no |

`marty-615/drum-remap` was the nominated starting point and it contributes three ideas worth
keeping outright: semantic tags rather than note numbers, curated fallback chains with
velocity compensation, and 1→N expansion rules (open-close hi-hat → open hit plus a pedal
close a 32nd later). No other surveyed project has expansion at all.

It is nevertheless too small and mis-factored for this inventory:

- 40 tags is smaller than a single library's own vocabulary. It covers 20 of Superior
  Drummer 3's 96 entries and 25 of BFD3's 73.
- `articulation` conflates independent facts. `hihat/closed-tip` packs a state (closed) and
  a contact part (tip) into one opaque token. Yamaha's modules take the literal cross
  product — `{head, open rim, closed rim} × {snares on, snares off}` — and Superior Drummer
  crosses `{bow, bell} × {tip, shank}`. As flat strings that is 18 hand-written tags and 18
  hand-written fallback chains; as axes it is 6 + 3 values and the chains derive themselves.
- `instance` is polluted: `hihat/shank` is filed as an instance, but shank is a contact
  part. Crash instances appear variously as `left`/`right`, `1`/`2`/`3` and
  `far-left`/`far-right`, so exact matching across maps silently fails.
- There is no controller model, and hi-hat pedal CC is a first-class kit piece in six GGD
  libraries, in Jamstix's map format, and in every e-drum module examined.
- There is no percussion beyond a rock kit, no implement axis (brushes, rods, mallets), and
  no provenance.

### What the sources demand

Twelve research dossiers were compiled (`docs/research/`). The load-bearing findings:

1. **Separate identity from rendering from note number.** LilyPond's symbol layer contains
   no MIDI pitch at all — `tamtam` has a symbol and no pitch; `splashhihat` and `pedalhihat`
   are distinct symbols that happen to share pitch 44. That property is what keeps GM's
   ceiling from leaking back in. Hydrogen is the control group: free-form instrument-type
   strings produced 219 distinct strings for roughly 35 instruments across 54 kits.
2. **The axes are real, and three independent bodies of work factor them the same way.**
   PAL (Bell, *Percussive Audio Lexicon*, PhD 2015) separates instrument, beater/exciter,
   articulation, placement, damping and dynamic level. Prockup et al. (ISMIR 2013) built a
   full factorial over instrument × stick height × stroke intensity × strike position ×
   articulation × snares-on/off, expressly to classify articulation *independent of
   instrument*. Yamaha, ATV, EFNOTE, GEWA and Roland firmware all expose zone as an axis
   crossed with state.
3. **`zone` is two axes, not one.** PAL splits *placement on the instrument* (bow, edge,
   bell, head, rim, shell) from *which part of the implement contacts* (tip, shank, butt).
   Real layouts contain both: `HH Closed (Bow)` is placement, Abbey Road's `Hihat Closed
   Tip` / `Shank` is implement-part, and Superior Drummer crosses them.
4. **`role` is not identity.** Four dossiers independently found no analogue of
   foundation/backbeat/ghost/timekeeping in any MIDI standard, any module firmware, any
   notation program, any dataset taxonomy or any other converter. The same sound has
   different roles in different bars, so putting role in the identity makes the identity
   unstable.
5. **Controllers are mandatory.** CC4 is the de-facto standard for hi-hat pedal position
   across every vendor examined, but Roland transmits 0–90 while everyone else transmits
   0–127, 2Box lets the user invert the polarity, Alesis can be told not to send it at all,
   and every vendor that does send it sends it *before* the note-on. Jamstix's map format
   additionally carries CC14 for snare head position and CC15 for tom head position, and
   models choke as channel aftertouch.
6. **Two shipping DAWs have already arrived at this design.** Cubase 12+ `.drm` files
   carry, per drum-map slot, an `InstrumentEntityID` **and** a `TechniqueEntityID`,
   resolved against Steinberg's own `instruments.xml` and
   `playingTechniqueDefinitions.xml`. Dorico goes further: a playing-technique combination
   is keyed on `techniqueIDs`, a comma-separated **set** of orthogonal `pt.*` identifiers
   (171 distinct combinations over 496 slots), with mutually exclusive dimensions declared
   explicitly as named `mutualExclusionGroups`. That is a factored-facet identity with an
   unbounded symbolic vocabulary, shipping in a product. Sibelius's SoundWorld does the
   same with dotted sound IDs, relative modifiers (`+pizzicato`, `-mute`) and a documented
   fallback by prefix truncation — and its editor guide explicitly recommends separate
   facets over compound tokens.
7. **Identifier stability is a hard requirement of the export targets, not only of this
   repository.** Logic articulation sets key on an `ArticulationID` that "is the value
   assigned to MIDI note events" in the user's project; Studio One `.keyswitch@id` and
   Dorico `baseSwitchID` play the same role. If an exported identifier moves between
   versions, MIDI in existing user projects silently re-points to a different sound.
8. **Size is a consequence, not a goal.** The largest genuinely *taxonomic* drum
   vocabularies are small (ENST-Drums 20 labels plus an instance suffix, MDB Drums 21).
   lotkey's 170 and Superior Drummer's 96 are flattened products of a few axes. The right
   target is therefore "express every distinction the sources make, with the fewest
   orthogonal axes", not "beat 170".

## Decision

**The pivot is a closed, versioned registry of symbolic terms. A term carries a stable
opaque integer ID and a sparse tuple of facets. No MIDI note number appears anywhere in the
vocabulary.**

Three layers, strictly separated:

```
vocabulary/   closed registry of pivot TERMS   id + slug + facet tuple + parent
data/devices/ per-device LAYOUTS               slot -> term, plus notes, CCs, provenance
vocabulary/rules/  FALLBACKS                   per-axis degradation + curated overrides
```

Note numbers exist only in layer 2. Layer 1 never refers to them.

### Identity facets

A term is defined by a sparse tuple. Most terms set two or three facets; the registry mints
only combinations that some primary source attests, so the space never expands
combinatorially.

| facet | meaning | example values |
|---|---|---|
| `instrument` | what makes the sound | kick, snare, tom, hihat, ride, crash, conga, … |
| `site` | contact site **on the instrument** | head, rim, rim2, crossstick, shell, bow, edge, bell |
| `position` | where on that site, radially | centre, halfway, offset, perimeter |
| `contact` | contact part **of the implement** | tip, shank, butt |
| `technique` | the stroke | hit, rimshot, rim-only, sidestick, slap, open-tone, heel, sweep, … |
| `ornament` | grace / multi-stroke qualifier, with an attack count | flam, drag, ruff, bounced, roll, buzz, swell |
| `openness` | ordered state, normalised 0.0 closed … 1.0 open, with named anchors | tight, closed, quarter, half, three-quarter, loose, open |
| `damping` | what damps and when | none, beater-strike, hand-strike, hand-after, body |
| `mechanism` | device state that is not damping | wires-on, wires-off, kick-dampened, gated |
| `implement` | what strikes it, with tip hardness | stick, brush, rod, mallet-soft/medium/hard, hand, felt-beater |
| `dynamic` | sample tier, not musical role | normal, ghost, soft, hard, accent |
| `timbre` | sound-generating lineage | acoustic, electronic, analog-808, fm, pcm, noise |
| `voicing` | kit or miking variant of the same instrument | standard, room, power, jazz, orchestra |

**Two facets deliberately live on the reference, not on the term.** A layout slot names a
term *plus* an optional `instance` and `limb`:

- `instance` is an unbounded ordinal — a kit may have six toms and six crashes — so minting
  a term per instance would multiply the registry by the largest kit anyone owns, for no
  gain: the fallback rule for instances is positional pairing, which needs the number, not a
  name. The ordinal is 1-based and its direction is fixed once, here: **toms high to low in
  pitch, cymbals left to right from the player's seat.** Getting that direction wrong
  silently swaps every tom and every conga in every conversion, and the sources genuinely
  conflict — GM puts High Bongo on note 60 and Low Bongo on 61, MuseScore's `tom-toms` has
  `Tom 6` as the *lowest* drum while its `temple-blocks` runs low to high.
- `limb` is dropped at zero fallback cost by a target that does not sample hands separately,
  which is a property no other facet has. It is identity-bearing where a layout ships
  separate Left Hand / Right Hand samples, and invisible everywhere else.

`choke` is deliberately **not** a technique. It is a relation on a previously sounded event,
which is why Jamstix models it as one generic stateful action that a target emits either as a
per-cymbal note or as channel aftertouch, while GGD ships a paired "X Choke" articulation per
cymbal. The per-cymbal pairing is the target's encoding, not the concept. Relations live on
rules and layout slots.

### Non-identity facets (properties of a layout slot)

`entryKind` (canonical | alias | gm-anchor | controller-trigger | choke-modifier | reserved |
non-sound), `exclusionGroup`, device `slot` and native name, `deviceRef` escape hatch,
`role` as optional annotation, and a mandatory `provenance` record.

### Controllers

A parallel namespace under the same ID discipline: `hihat.pedal_position`,
`strike_position.radial`, `strike_position.rim_depth`, `strike_position.lateral`,
`choke_amount`. Each layout declares, per controller: number or aftertouch, min, max,
polarity, channel scope, and emission timing (pre-note snapshot or continuous). Without
min/max a TD-17 driving a library that expects 0–127 never reaches fully closed.

### Identifiers

Two identifiers, with different jobs:

- `id` — an opaque, monotonically assigned integer. **Never reused, never reassigned, never
  meaning-bearing**, and never derived from a note number, a slug, or a position in a tree.
  `lotkey/Drum-MIDI-Converter` derives its keys from tree paths and its README states the
  consequence: *"If you reorganized the tree or removed some kit pieces, the other mappings
  will not compile."* The id is what is stored, transmitted and compiled.
- `slug` — a stable, human-readable, dotted string (`hihat.closed.tip`), unique and
  **immutable once published**. This is what hand-edited layout files reference and what
  appears in diffs and error messages. `display_name` is a third field and is mutable; it
  is explicitly not an identifier.

**IDs are not partitioned by instrument family.** A range is an assertion, and assertions
get revised; the axes already say what family a term belongs to, and encoding it a second
time in the integer makes that copy unversioned and unfixable. OBO Foundry, which maintains
hundreds of thousands of terms, states the rule outright: *"LOCALID should not be
semantically meaningful, therefore numeric IDs should be used."* The one partition that is
worth having is by **assigning authority**, which is what IANA's and pci.ids' ranges
actually partition:

```
1 … 999_999          core KITWARP vocabulary
1_000_000 …          private / third-party extension space, never assigned by the core
```

Terms are never deleted. Four lifecycle states — `draft`, `active`, `deprecated`,
`withdrawn` — with `deprecated_in`, a closed `deprecation_reason` vocabulary, an ordered
`superseded_by`, and a `migration_note`. A term that turns out to be two sounds is split,
which is a MAJOR bump. Corrections to a published slug are made by adding a `correction`
alias, never by editing the slug — Unicode's rule, for Unicode's reason.

Versioning ships **both** a SemVer `vocabulary_version` (the contract: MAJOR on a split or
a meaning change, MINOR on additions, PATCH on documentation) and a monotonic
`vocabulary_serial` (the build identity), because SemVer is not totally ordered in practice
and a user reporting a broken map has to be able to say which build they have.

*(The full registry mechanics, the CI invariants that enforce them, and the surveyed
precedent from IANA, Unicode, CLDR, ISO 3166, LOINC, SNOMED, CVE and OBO are in ADR-0003.)*

### Fallbacks

Resolution order, in the mapping compiler, never in the audio thread:

1. exact term
2. instance peer — same term, different instance, paired by relative position
3. per-axis degradation, derived: `bell → bow`, `rim2 → rim`, `edge → bow`,
   `crossstick → rim`, `shank → tip`, `half-open → closed`, `wires-off → wires-on`,
   `mallet → stick`, and `limb → unspecified` at zero cost
4. curated override edges, with velocity compensation
5. curated 1→N expansions and N→1 collapses, including ones with a controller side channel
   (`pedal/splash → note 44 + CC4 = 0`)
6. explicit, named failure — the note is dropped, passed through, or reported

Steps 1–3 are mechanical, which is what makes several hundred terms tractable where 40
hand-written chains were already at their limit. Steps 4–5 are the curated part and carry a
human-readable reason, as `drum-remap` does.

## Criteria and how the options score

| Criterion | GM note pivot | `drum-remap` 40 tags | lotkey 170-key tree | **this ADR** |
|---|---|---|---|---|
| Round-trips Superior Drummer 3 | no (42 % loss) | no (20 of 96) | partly (80 keys) | yes |
| Round-trips a GS/XG source | no | no (7.6 % coverage) | no | yes |
| Expresses zone × state cross products | no | combinatorially | partly | yes, by construction |
| Fallbacks derivable | n/a | hand-written | walk-up-tree, but randomised | per-axis + curated |
| Stable IDs | note number | none | path-derived, breaks on reorg | opaque, never reused |
| Controller model | none | none | key exists, resolves to a note | first-class namespace |
| Provenance | none | none | none | mandatory per entry |
| Extensible without invalidating data | no | no | no | yes, MINOR bump |

## Consequences

**Easier.** New layouts are a sparse list of slots; fallbacks come from the axes; export to
`.iom`, `.drm`, Reaper note names, `.ins` and Studio One pitch lists becomes a projection of
layer 2; collisions and missing fallbacks become computable properties that a validator can
report.

**Harder.** The vocabulary must be minted before collection, and minting is judgement work.
Every device layout now needs facet-level curation rather than a note list, which is slower
per device and is the reason the inventory says twenty good maps beat two hundred raw ones.

**Now required.** A validator (`tools/validate`) that checks: every layout slot references an
*active* minted term; no two canonical slots claim one note on one channel; every axis value
is registered; every entry carries provenance and at least one record whose licence verdict
permits shipping; identifiers are stable against a frozen baseline; and **every term has a
route out** — a parent, a curated edge, an expansion, a degradable axis, or an explicit
entry in the `roots` list saying that nothing to fall back to is the correct answer.

Totality, not acyclicity, is the invariant. Mutual curated edges are legitimate and
expected — "if the target has no ride bell use the cowbell" and "if it has no cowbell use
the ride bell" are both good rules, and only one can ever fire for a given target — so the
resolver walks with a visited set, exactly as `marty-615/drum-remap`'s `resolveTag` does.
The validator reports cycles so they stay visible and fails on terms with no route at all.

**Irreversible once collection starts.** Adding an axis after data exists is a MAJOR bump and
a re-curation of everything. Adding axis *values* and terms is cheap. That asymmetry is why
the axis list above is deliberately generous.

## Strongest counter-argument

Fifteen facets is a lot of model for a plugin whose v1 ships note-to-note mapping, and every
axis that turns out to be unused is dead weight in the schema, the validator, the codegen and
every curator's head. `drum-remap` ships and works with four fields.

Two things answer it. First, the asymmetry above: an unused axis costs a column, while a
missing axis costs a re-curation of the entire corpus, and the sources say plainly which axes
exist — `zone` alone is attested by six independent vendors' firmware. Second, the facets are
sparse and mostly unset; a plain kick is `{instrument: kick, technique: hit}` and nothing
else. The cost is carried by the terms that need it.

The honest residual risk is `position`, `voicing` and `dynamic`. Each rests on fewer sources
than the rest, and each could reasonably have been left to a later MAJOR bump. They are in
because Jamstix exposes head position as a continuous controller, GM2 builds seven of its
nine sets on voicing alone, and three independent sources treat ghost as a named band rather
than a velocity.
