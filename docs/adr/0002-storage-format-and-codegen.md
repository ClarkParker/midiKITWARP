# ADR-0002 — Line-oriented JSON as the source of truth, compiled to a constexpr table

**Status:** Proposed
**Date:** 2026-09-06
**Depends on:** ADR-0001
**Evidence:** `docs/research/09-storage-and-codegen.md` — every number below was measured in
this environment, not quoted.

## Context

The format has to satisfy seven requirements at once: hand-curatable and reviewable as a
git diff; machine-generatable from parsers and scrapers; schema-validatable in CI;
compilable into a single C++ binary with no runtime parser and no allocation on the audio
thread; able to carry per-entry provenance; stable in key order; and survivable under
concurrent contribution.

Eight candidate families were benchmarked rather than argued about: JSON, YAML, TOML,
JSON5/JSONC, CSV/TSV, a TSV+TOML hybrid, SQLite, and the binary schema formats
(Protobuf/FlatBuffers/Cap'n Proto).

### The finding that decided it

**Merge safety is the deciding criterion, and it is a property of line-orientation, not of
format.** Two curators each insert one note at the same sorted position; resolve naively:

| Form | Result |
|---|---|
| Block JSON (`indent=2`) | two conflict regions; "take mine" **silently yields 9 records instead of 10**; "take both" also yields 9 (duplicate key, last wins). `json.loads` accepts it. `jsonschema.validate` **passes**. Only a duplicate-key `object_pairs_hook` catches it — which is exactly why QMK's `json_schema.py` uses one. |
| Block YAML | silent, same as JSON |
| Block TOML | **fails loudly** — `tomllib: Cannot overwrite a value`. Better, but still a manual redo of both curators' work |
| One record per line JSON | **correct: 10 records** |
| TSV | **correct: 10 records** |
| SQLite | `warning: Cannot merge binary files: kw.db` — unresolvable |

A format that can silently drop a contributor's work in a merge is disqualified for a
repository that expects concurrent per-device pull requests.

### Round-trip churn, measured on an 8-record file with no semantic change

| Writer | Lines changed | Comments |
|---|---|---|
| `json.dumps` stdlib default (`indent=4`) | 178 of 91 | n/a |
| canonical JSON (`indent=2, sort_keys`) on an already-canonical file | **0** | n/a |
| `tomlkit` | **0, byte-identical** — and uniquely stayed byte-identical on deliberately hand-formatted input (aligned `=`, literal strings, comment columns) | preserved |
| `ruamel.yaml`, tuned `indent(mapping=2, sequence=4, offset=2)` | 0, byte-identical | preserved, but normalises hand formatting |
| `ruamel.yaml`, default | 138 | one comment misplaced |
| `PyYAML`, `tomli_w`, `json5` | — | **all comments destroyed** |
| TSV | 0, byte-identical | n/a |

### Validation tooling, measured

- `check-jsonschema` 0.38.0 validates JSON, YAML, TOML **and** JSON5 against the same JSON
  Schema 2020-12 via `--force-filetype`. It cannot read `.jsonl`.
- `taplo` 0.9.0 gives the best diagnostics of anything tested — rustc-style
  `file:line:col` with a caret — **but was verified to silently ignore
  `dependentRequired` and `unevaluatedProperties`** while enforcing `type` and `enum` from
  the same schema file. It passed a file `check-jsonschema` correctly rejected. Those are
  precisely the constraints this schema needs (openness only meaningful on a hi-hat, site
  required for site-bearing techniques).
- `frictionless` 5.19.0 is the only tool that enforces `unique`, `primaryKey` and
  cross-file `foreignKey` — verified catching a device row whose pivot id was absent from
  the vocabulary. JSON Schema cannot express that at all; twenty lines of Python can.

### Codegen, measured at 13,500 rows × 11 columns (g++ 13.3.0, `-O2 -std=c++20`)

| Approach | `.rodata` | `.data.rel.ro` | relocations | binary | compile | startup |
|---|---:|---:|---:|---:|---:|---|
| **constexpr enum-id rows + offset string pool** | 344,402 B | **0** | **3** | 360,552 B | **0.39 s** | **none** |
| constexpr `std::array<std::string_view>` dictionaries | — | 127,488 B dirty | 7,970 | 622,736 B | — | none |
| no dictionary encoding (`{offset,len}` per field) | 1.25 MB | — | — | — | 2.77 s | none |
| FlatBuffers blob, genuinely zero-copy | 391,532 B | — | — | 405,208 B | 1.52 s | none |
| Cap'n Proto, unpacked / packed | 430,064 / 347,903 B | — | — | — | — | packed must be unpacked → allocates |
| `xxd -i` of the TSV + allocation-free parser | 1,035,563 B | — | — | — | — | **830 µs**, and no index built |

`sizeof(Row)` is 12 bytes hand-packed, 14 as a FlatBuffers struct, 16 in Cap'n Proto.
`.init_array` is 8 bytes and `nm` shows no `GLOBAL__sub_I` in every constexpr variant: no
dynamic initialisers, no allocation, the table in shared read-only pages. `std::string_view`
holds a pointer, which is why the dictionary variant costs 7,970 relocations and 127 KB of
per-process dirty pages in a PIE — a real cost in a plugin loaded into every DAW instance.

**Dictionary encoding, not the container, determines size.** CBOR dict-encoded is 344,089 B
against 2,277,456 B for a naive row-of-maps.

The domain's own precedent contains the anti-pattern: `lotkey/Drum-MIDI-Converter` generates
a `Keys.hpp` that declares 170 namespace-scope `const std::string` objects — 170 dynamic
initialisers and 170 heap allocations at plugin load, which is exactly what the no-allocation
requirement exists to prevent.

### What the comparable curated databases do

- **tzdata is the closest analogue and its lesson is architectural, not syntactic.** The 11
  hand-maintained files are 20,717 lines, **69.1 % of them comments** and 23.3 % data.
  Nothing parses `northamerica` at runtime — `zic.c` (4,334 lines) compiles it to TZif. A
  *separate* machine-canonical text form, `tzdata.zi`, is generated by `zishrink.awk`; **the
  hand file is never re-serialised.** Validation is 13 bespoke awk/make checks, not a schema
  language, because the interesting invariants are project-specific. And tzdb is itself a
  hybrid: `zone1970.tab` is TSV for the part of the data that really is a table.
- **SMuFL is the best template**, and it is the same shape as this project: a 2,940-term
  curated symbolic vocabulary, hand-edited YAML in `data/`, generated JSON in `metadata/`,
  and a CI pipeline of `check-jsonschema` per file, then `check_consistency.py` (*"checks
  that a JSON Schema alone can't express"*), then `check_immutability.py` (codepoints frozen
  against v1.4), then `generate.py --check`.
- **Provenance goes in fields, not comments — and the split is causal.** Projects whose hand
  file is never machine-rewritten go all-in on comments (tzdb 69 %, pci.ids free text).
  Projects whose files *are* machine-written moved provenance into fields: CLDR carries
  `draft=` on 169,650 elements while `common/main/de.xml` has exactly one XML comment;
  iso-codes' validator rewrites every file with `json.dump(sort_keys=True)`, so comments
  could never have survived.
- **pci.ids proves line-oriented text scales**: 43,047 lines, and 20 sampled consecutive
  commits changed 3–33 lines each, median ~7.

## Decision

**JSON, in two dialects, owned by one formatter; provenance in fields; the generator never
writes a hand-edited file; compiled to an enum-indexed constexpr table with an offset string
pool.**

1. **Format.** `tools/format.py` owns both dialects and is the only thing that writes them.
   - `vocabulary/pivot.json` — block-formatted, keyed by pivot slug, SMuFL
     `glyphnames.json` style. A few hundred terms at roughly 100 bytes each; block form
     suits the nested axis tuples and the fallback edges.
   - `data/devices/<vendor>/<model>.json` — **one note record per line** inside the `notes`
     array. This is what `marty-615/drum-remap` already does in its `maps/*.json`, and it is
     what buys the merge behaviour above.

   Chosen over the alternatives because it needs **no new dependency** (`tools/requirements.txt`
   already pins `jsonschema` and says additions must earn an ADR), has the strongest
   maintained validator with full 2020-12 semantics, makes sparse optional axes free where
   TSV's fixed columns turn ten axes into a wall of tabs in which a miscount silently shifts
   a value into the wrong column, and — measured — matches TSV **exactly** on merge safety
   and self-identifying diffs, the only two criteria on which TSV was ahead.

2. **Provenance as fields**, per ADR-0004. Every record carries `source` and a `confidence`
   enum. This reproduces CLDR's `draft=` decision and follows from decision 3.

3. **The generator never writes a hand file.** Scrapers write `build/proposals/*.json`; a
   human moves content into `data/`. Generated artefacts are committed and guarded by
   `--check` modes. This is the tzdata law and the SMuFL law, and it is what makes the
   comment question moot.

4. **CI, modelled on SMuFL's `pages.yml`:** `check-jsonschema` per file, then
   `tools.validate` for what a schema cannot express — a duplicate-key-rejecting loader,
   every device `pivot` slug resolving to an active vocabulary entry, ids unique, canonical
   sort order, and **immutability of published pivot ids against a frozen baseline**. That
   last check is the highest-value one in the whole pipeline, because changing the
   vocabulary invalidates everything already collected. Then `tools.format --check`,
   `tools.codegen --check`, `tools.export --check`.

5. **Codegen.** Python emits one header with per-axis dictionaries of `{uint32 offset,
   uint16 len}` into a single `constexpr char kPool[]`, a 12-byte `Row` of small integer
   axis ids, and `kRows` pre-sorted so lookup is `std::lower_bound`. Measured: 344 KB
   `.rodata`, 3 relocations, 0 bytes `.data.rel.ro`, `.init_array` = 8, no constructors, no
   allocation, 0.39 s compile, ~107 ns per lookup. Parallel `kSourceFile` / `kSourceLine`
   arrays are emitted under `#ifndef NDEBUG`, following systemd's hwdb, which carries
   `filename_off` and `line_number` into its compiled trie.

6. **Scheduled now, not later.** Measure the header's compile time on MSVC before the table
   shape is frozen. GCC scales linearly to 135,000 rows at 2.97 s; MSVC is **UNVERIFIED**
   and is a real risk for a Windows VST3. The fallback is splitting across translation units
   or switching the shipped artefact to the FlatBuffers blob, which costs 14 % size and 4×
   compile time for identical scan speed.

### Rejected, with the reason

| Option | Why not |
|---|---|
| YAML | new dependency; best-effort comment reattachment; block-form merge hazard; the YAML 1.1/1.2 bool-and-octal coercion trap in a file full of note numbers |
| JSON5 / JSONC | its only edge is comments, and the `json5` library destroys them on write — verified |
| CSV / TSV | fixed columns against ten sparse axes; `frictionless` is a heavy dependency for benefits that are twenty lines of Python in JSON |
| TSV + TOML hybrid | two schema languages, two validators, two parsers, two review idioms, to save ~2 MB of repository text that never reaches the binary |
| SQLite | `Cannot merge binary files` is disqualifying; no three-way merge driver exists |
| FlatBuffers / Cap'n Proto / textproto as **source** | 14–25 % larger output, 4× compile, a toolchain dependency, far weaker validation. All three are good *derived* formats and bad *source* formats |

## Consequences

The repository stays stdlib-only for reading its own data. Diffs are proportional to the
semantic change. A scraper can propose without ever touching a curated file. The compiled
artefact allocates nothing, initialises nothing and shares its pages across DAW instances.

The cost is that `tools/format.py` becomes load-bearing: if it and the hand files ever
disagree about canonical form, every diff turns to noise. That is why it has a `--check`
mode in CI from day one.

## Strongest counter-argument

**TOML with `tomlkit` is the only option under which a scraper and a human can edit the same
file, and that workflow may be worth more than everything JSON wins.**

`tomlkit` is not a serialiser but a concrete-syntax-tree round-tripper, and this was
verified: given a file a human actually typed — aligned `=`, single-quoted literal strings,
comments in their own columns — `tomlkit.dumps(tomlkit.parse(src))` returned it byte for
byte. Nothing else tested does that. That makes exactly one workflow possible, and it is the
one this project will actually want: a scraper proposes 90 notes from a Roland manual, a
curator writes `# manual p.142 shows 22 for HH Edge but the TD-30 factory kit sends 26 —
check on hardware` above three uncertain rows, and six weeks later the scraper runs again
with a better parser, updates 40 rows, and the curator's notes are still there, attached to
the right rows. Under this ADR that note has to be squeezed into a `source` string, which
means deciding in advance what kinds of note the schema permits — and free-form marginal
annotation, which is the actual substance of curation work, has nowhere to live. tzdb is
69 % comments for a reason: on a dataset like this the reasoning *is* the deliverable.

**Why it did not win.** The counter-argument's premise is that the generator writes the hand
file, and that premise is what every precedent rejects: tzdata never re-serialises
`northamerica`, SMuFL's generator writes `metadata/` and never `data/`, CLDR's tooling
writes locale XML and *therefore* CLDR moved per-datum confidence out of comments into a
`draft=` attribute used 169,650 times. Once the generator writes only to `build/`, TOML and
JSON preserve comments equally well and the advantage evaporates. Three further costs settle
it: TOML's block tables reproduce the multi-line-record merge hazard (loud rather than
silent, but still a manual redo); `taplo` silently ignores exactly the conditional
constraints this schema needs, so TOML means running `check-jsonschema` on the TOML anyway
and losing the caret diagnostics that were its second advantage; and `tomlkit` is a real
dependency added to a file whose own comment demands an ADR for additions.

**The honest residue:** this decision does give up free-form marginal annotation, and that
is a genuine loss. It is mitigated with a generous unconstrained `source` string plus an
optional `notes` array, and by putting narrative reasoning in `docs/` beside the ADRs. If
after six months curators are routinely fighting the schema to record what they know, that
is the signal to revisit — and the migration is a hundred-line script, because the axis
model, not the file format, is the expensive thing to change.
