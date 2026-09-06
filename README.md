# midiKITWARP — the data

The drum-layout dataset behind KITWARP, a VST3 MIDI plugin that translates drum MIDI
between the note layouts of different libraries and hardware modules.

**This repository is data, not plugin code.** Vocabulary, device layouts, schemas, parsers,
a validator, exporters and the reasoning behind all of it. The plugin is built elsewhere.

## The idea in one paragraph

A drum mapper that assigns library to library needs N² tables. A mapper with a pivot needs
N. The whole design therefore rests on what the pivot *is* — and the obvious answer, a MIDI
note number, is measurably wrong: across the eleven reference `.iom` files in
`data/legacy-iom/`, 1320 mapped source notes collapse onto 1038 slots, and Superior Drummer 3
loses 42 % of its distinctions on the way in. Regenerate that measurement yourself with
`python -m tools.iom.analyze data/legacy-iom`.

So the pivot here is a **symbolic vocabulary**: a closed, versioned registry of terms, each
with an opaque never-reused integer id and a sparse tuple of facets. No note number appears
anywhere in it. Note numbers live only in device layouts.

## Layout

```
vocabulary/axes.json          13 axis registries, 132 values — the irreversible part
vocabulary/pivot.json         the terms: id, slug, facets, parent, lifecycle
vocabulary/rules.json         per-axis degradation, curated edges, 1→N expansions, roots
schema/                       JSON Schema 2020-12 for every hand-maintained file
data/devices/                 device and library layouts — note numbers live here
data/legacy-iom/              eleven reference .iom files, kept as fixtures, not as data
docs/adr/                     the four decisions and why they went that way
docs/research/                ~800 KB of primary-source dossiers behind those decisions
docs/05-inventory.md          the ~190-entry work list
tools/                        parser, validator, formatter, exporters, codegen
```

## The four decisions

| ADR | Decision |
|---|---|
| [0001](docs/adr/0001-pivot-vocabulary.md) | The pivot is a symbolic, factored, versioned vocabulary — not a note number, not GM, not a flat tag |
| [0002](docs/adr/0002-storage-format-and-codegen.md) | Line-oriented JSON as the source of truth, compiled to a constexpr table with an offset string pool |
| [0003](docs/adr/0003-identifiers-and-registry.md) | Opaque never-reused integer ids, immutable slugs, four lifecycle states, SemVer plus a build serial |
| [0004](docs/adr/0004-provenance-and-licensing.md) | Provenance is mandatory and licence status is machine-checked |

All four are **Proposed**. Nothing is collected against them until they are signed off,
because changing the vocabulary afterwards invalidates everything collected.

## Working on it

```bash
python -m pip install -r tools/requirements.txt

python -m tools.validate                 # cross-file invariants
python -m tools.format --check           # canonical formatting
python -m tools.iom.roundtrip_check data/legacy-iom
check-jsonschema --schemafile schema/pivot.schema.json vocabulary/pivot.json
```

The validator checks the things a schema cannot: referential integrity across files,
identifier stability against a frozen baseline, that every term has a route out of the
fallback graph, and that every shipped assertion carries at least one provenance record
whose licence verdict permits shipping.

## Contributing a layout

1. Find a **primary** source: the manufacturer's own documentation, a file the product
   ships, or your own measurement of hardware you own. Curated third-party collections are
   worklists that tell you where to look, never the shipped source — see ADR-0004.
2. Add the source to `data/sources.json` once, with its licence.
3. Write `data/devices/<vendor>/<model>.json`, one note record per line, each with its own
   provenance record. A verbatim `quote` is required when the method is
   `manufacturer-doc`.
4. Run the validator and the formatter.

**No number without a source.** A documented gap beats a guessed note.

## Sources ruled out

Groove Monkee is `forbidden` — its licence bars use in a competing product, and after
*Ryanair* (C-30/14) that contractual restriction stands whether or not a database right
subsists. The REAPER Stash and two unlicensed converter repositories are `reference-only`.
The GPL-licensed collections are `rederive-only`. Details and per-source verdicts in
ADR-0004; the same table is repeated in the inventory.

## Legal

KITWARP is an independent project. It is not affiliated with, sponsored by, or endorsed by
Toontrack, XLN Audio, inMusic (BFD/Alesis), Steven Slate Drums, GetGood Drums, Roland,
Yamaha, Pearl, or any other manufacturer. All product names, company names and logos are
the trademarks or registered trademarks of their respective owners. They are used here
solely to identify the note layouts KITWARP can convert between, which is a descriptive use
permitted by Art. 14(1)(c) EUTMR and § 23 Abs. 1 Nr. 3 MarkenG.

This repository contains no software, samples, presets or documentation belonging to any of
these manufacturers. The layouts are factual tables of MIDI note assignments, compiled from
published documentation and from measurements of hardware and software the contributors own.
No manufacturer has reviewed or approved them. If you are a rights holder and believe an
entry is incorrect or should not be distributed, open an issue and it will be corrected or
removed.
