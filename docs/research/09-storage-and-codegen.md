# 09 — On-disk storage format and C++ codegen

Evidence for an ADR choosing how KITWARP's hand-curated, machine-generated,
schema-validated pivot vocabulary and device layouts are stored on disk and compiled into
the plugin binary.

---

## 1. Scope and method

Everything below that is stated as a number was **measured in this environment**, not
recalled. Three kinds of work were done:

**(a) Format experiments.** A realistic 8-record KITWARP fragment (a Roland TD-30 hi-hat /
snare / ride group carrying the axes argued for in `00-draft-axes.md`: instrument,
instance, zone, articulation, openness, damping, implement, limb, plus a per-note
provenance note) was rendered into every candidate format. Then, per format: a one-line
semantic change was applied and the git diff measured; a generator round-trip
(parse → re-serialise) was run and the churn measured; two branches were made to insert a
record at the same sorted position and the merge conflict was resolved naively and the
result re-parsed. Scratch tree:
`scratch:fmt/`

**(b) Codegen experiments.** A synthetic dataset at realistic KITWARP scale (150 devices ×
90 notes = 13,500 rows × 11 columns) was compiled six different ways with
`g++ (Ubuntu 13.3.0) -O2 -std=c++20` and the resulting ELF sections, relocation counts,
compile wall-times and access times measured. Scratch tree:
`/tmp/claude-0/.../scratchpad/cg/`

**(c) Precedent inspection.** Real repositories cloned and read, not summarised from
memory. Clones in `/tmp/claude-0/.../scratchpad/repos/`.

| Cloned | What it is | Read |
|---|---|---|
| `eggert/tz` | tzdata + `zic` | data files, `Makefile`, `checktab.awk`, `zic.c`, `zone1970.tab` |
| `pciutils/pciids` | `pci.ids` (43,047 lines) | file, header, 60 commits of history |
| `pciutils/pciutils` | `lspci`/`libpci` | `lib/names-parse.c`, `lib/names-cache.c`, `update-pciids.sh` |
| `vcrhonek/hwdata` | `pci.ids` + `usb.ids` + `pnp.ids` packaging | `Makefile` check target, `check-pci-ids.py`, `AUTOMATION.md` |
| `systemd/systemd` (sparse) | udev `hwdb` | `hwdb.d/*.hwdb` (383,927 lines), `sd-hwdb/hwdb-internal.h` |
| `unicode-org/cldr` (sparse) | CLDR | `common/main/*.xml` (1,148 files, 94 MB), `common/dtd/ldml.dtd` |
| `iso-codes-team/iso-codes` (salsa) | ISO 639/3166/4217/15924 | `data/*.json`, `data/schema-*.json`, `scripts/validate_json_data.py`, `meson.build` |
| `w3c/smufl` | 2,940-term music-symbol vocabulary | `metadata/`, `data/ranges/*.yaml`, `.github/workflows/pages.yml`, `metadata/schema/check_consistency.py` |
| `qmk/qmk_firmware` (sparse) | keyboard/keymap DB | `data/schemas/*.jsonschema`, `data/mappings/*.hjson`, `lib/python/qmk/{json_schema,cli/generate}` |
| `alsa-project/alsa-ucm-conf` | ALSA UCM per-device configs | `ucm2/**/*.conf` |
| `Ardour/ardour` (sparse) | 475 MIDNAM device files (23 MB) | `share/patchfiles/*.midnam`, `share/patchfiles/README` |
| `lotkey/Drum-MIDI-Converter` | **the domain-specific precedent** | `src-cpp/mappings/tree/*.txt`, `SampleTree/Keys.hpp`, generated `Mappings/**/*.cpp`, `update-mappings/update.cpp`, `src-python/conversions.lkcmap` |
| `marty-615/drum-remap` | reference pivot model | `maps/*.json` |

**Could not obtain:** ZSA's `zsa/oryx-keymaps` (repo not public — `git clone` returned an
authentication prompt). The GitHub MCP tools are scoped to `clarkparker/midikitwarp` only,
so release metadata was obtained by cloning each tool repo and reading `git log -1` instead.
`sqlite3` CLI is not installed here, so the SQLite dump was produced with Python's
`sqlite3.Connection.iterdump()`, which emits the same statements as `.dump`.

---

## 2. The format experiments

### 2.1 The corpus

The same 8 records, with per-note provenance, in each candidate:

| File | Bytes | Lines | B/record | Lines/record | Provenance carried as |
|---|---:|---:|---:|---:|---|
| `a.json` — JSON, `indent=2`, `sort_keys` | 2,005 | 91 | 251 | 11.4 | *nothing — dropped* |
| `a_prov.json` — same + `note_comment` field | 2,408 | 97 | 301 | 12.1 | field |
| `f.json` — **JSON, one record per line** | 1,910 | 14 | 239 | 1.75 | field |
| `g.jsonl` — JSON Lines | 2,101 | 8 | 263 | 1.0 | field |
| `b.yaml` — YAML block | 1,828 | 78 | 229 | 9.8 | `#` comment |
| `c.toml` — TOML `[[notes]]` | 1,682 | 93 | 210 | 11.6 | `#` comment |
| `d.json5` — JSON5, one record per line | 1,712 | 20 | 214 | 2.5 | `//` comment |
| `e.tsv` — TSV + `#` comment lines | 884 | 17 | 111 | 2.1 | `#` comment |
| `e_col.tsv` — TSV + `source` column | 838 | 9 | 105 | 1.1 | column |

Size is the least interesting axis and is listed only to kill the argument from it: at full
scale (13,500 rows) the whole corpus is 1.0 MB as TSV and 4.2 MB as pretty JSON, and
**neither ships in the plugin** — the generated `.rodata` is 344 KB either way (§4).

### 2.2 Criterion 1a — what a ONE-LINE change looks like

Changing `snare.rimshot` from note 40 to 41 (resolving the `UNVERIFIED` note):

```
 a.json    | 2 +-      b.yaml    | 2 +-      c.toml    | 2 +-
 d.json5   | 2 +-      e.tsv     | 2 +-      e_col.tsv | 2 +-
```

Every format gives a one-line diff. **That is not the discriminator.** The discriminator is
whether the changed line *identifies itself*. At `git diff -U0`:

```
--- a.json ---                --- c.toml ---              --- e_col.tsv ---
-      "note": 40,            -note = 40                  -snare.rimshot 40 snare snare1 rim rimshot  none stick right_hand UNVERIFIED:…
+      "note": 41,            +note = 41                  +snare.rimshot 41 snare snare1 rim rimshot  none stick right_hand UNVERIFIED:…
```

In block-structured JSON, YAML and TOML, the changed line says only `note: 40 → 41`; the
record it belongs to is 8 lines away and invisible in a review-mail diff, a GitHub
"changed lines only" view, or `git log -p --stat`. In TSV, JSON5 and **one-record-per-line
JSON**, the changed line carries its own identity and its whole context. TOML is a partial
exception: git's hunk-header heuristic put `id = "snare.rimshot"` in the `@@` header,
because `id` is the first key in the table — so a TOML file whose first key is always the
id recovers most of the benefit for free.

### 2.3 Criterion 1b — does re-serialisation churn the whole file

A generator that reads and writes the hand file, making **no semantic change**:

| Format + library | Lines changed (of 91–97) | Comments surviving (of 6) | Byte-identical? |
|---|---:|---:|---|
| JSON, `json.dumps` **stdlib default** (`indent=4`) | **178** (whole file) | n/a | no |
| JSON, canonical (`indent=2, sort_keys=True, ensure_ascii=False`) on an already-canonical file | 0 | n/a | **yes** |
| YAML, `PyYAML safe_dump` | whole file | **0** | no |
| YAML, `ruamel.yaml` default indent | 138 | 6 (but reattached to the wrong record) | no |
| YAML, `ruamel.yaml` with `indent(mapping=2, sequence=4, offset=2)` | 0 | 6 | **yes** |
| TOML, `tomllib` + `tomli_w` | whole file | **0** | no |
| TOML, `tomlkit` | 0 | 6 | **yes** |
| JSON5, `json5` lib | whole file | **0** | no |
| TSV, `csv`/split-join | 0 | 6 | **yes** |

Two findings that only fall out of running it:

**(i) `tomlkit` is a true concrete-syntax-tree round-tripper and the only one that survives
non-canonical hand formatting.** Fed a file a human actually typed —

```toml
[[notes]]
id     = "kick.hard"      # aligned =
note   = 36
[[notes]]
id = 'snare.hit'          # literal string
note = 38
```

`tomlkit.dumps(tomlkit.parse(src))` returned it **byte for byte**, alignment, literal-string
quoting and comment columns intact. `ruamel.yaml` given the analogous YAML normalised
`note:   38` → `note: 38` and shifted the trailing comment's column. That difference is the
entire practical case for TOML.

**(ii) `ruamel.yaml` misplaces comments.** In the default-indent round-trip, the comment
that belonged *after* the last key of record 1 was re-emitted at the old (deeper)
indentation while the record around it was re-indented shallower — a silently
wrong-looking file that still parses. Comment reattachment in a YAML round-tripper is
best-effort, not a guarantee.

### 2.4 Criterion 2 — machine-generatable from parsers and scrapers

Not a discriminator between text formats; all are one function call from a Python or Node
scraper. The differences are in dependencies and in what the emitter has to be careful about:

| | Writer | Extra dependency for KITWARP | Emitter must be careful about |
|---|---|---|---|
| JSON | `json` | **none** (stdlib) | nothing; must own the layout to get one-record-per-line |
| YAML | `ruamel.yaml` (to keep comments) | ruamel.yaml (C ext optional) | indent config, comment reattachment, `1.1` vs `1.2` bool/octal coercion |
| TOML | `tomlkit` (to keep comments) | tomlkit; `tomli` on py<3.11 (already in `tools/requirements.txt`) | nothing; tomlkit is exact |
| JSON5 | `json5` | json5 | **comments are lost on any write** |
| TSV | `csv`/`str.join` | **none** | quoting/escaping of embedded tabs and newlines; column count |
| SQLite | `sqlite3` | none (stdlib) | see §2.8 |
| FlatBuffers/Cap'n Proto text | `flatc`/`capnp` | a compiler toolchain | schema evolution rules |

The KITWARP repo's `tools/requirements.txt` already says "Kept deliberately small: the data
pipeline must be runnable from a clean checkout with a stock Python. Anything added here
has to earn its place in an ADR." — and already lists `jsonschema>=4.21` and
`tomli>=2.0 ; python_version < "3.11"`. JSON and TSV need nothing new; TOML needs `tomlkit`
added; YAML needs `ruamel.yaml` added.

### 2.5 Criterion 3 — schema validation in CI, with which concrete tool

Three tools were installed and run against the corpus.

**`check-jsonschema` 0.38.0** (`python-jsonschema/check-jsonschema`, last commit
2026-08-17). One tool, one schema, four formats:

```
$ check-jsonschema --schemafile schema.json a.json                  → ok
$ check-jsonschema --schemafile schema.json b.yaml                  → ok
$ check-jsonschema --schemafile schema.json c.toml                  → ok
$ check-jsonschema --schemafile schema.json --force-filetype json5 d.json5 → ok
$ check-jsonschema --schemafile schema.json c_bad.toml
  Schema validation errors were encountered.
    c_bad.toml::$.notes[2].openness: 'open5' is not one of ['closed','open1','open2','open3','open4']
```

`--default-filetype`/`--force-filetype` accept `json|toml|yaml|json5`. It runs the Python
`jsonschema` library, so the full 2020-12 dialect is honoured. **It cannot read `.jsonl`**
(`JSONDecodeError: Extra data: line 2 column 1`); a 7-line
`jsonschema.Draft202012Validator` loop replaces it and gives better locality
(`g_bad.jsonl:3: note: 460 is greater than the maximum of 127`).

**`taplo` 0.9.0** (npm `@taplo/cli`; repo `tamasfe/taplo`, last commit 2026-07-28). Best
error locality of anything tested — rustc-style caret diagnostics with file:line:col:

```
error: "open5" is not one of ["closed","open1","open2","open3","open4"]
   ┌─ …/c_bad.toml:36:12
36 │ openness = "open5"
   │            ^^^^^^^
```

**But taplo silently ignores post-Draft-4 keywords.** Verified: a schema containing
`"dependentRequired": {"openness": ["zone"]}` and `"unevaluatedProperties": false` was
loaded by taplo without complaint, taplo reported the file clean, and `check-jsonschema`
run on the same file with the same schema correctly reported
`$.notes[3]: 'zone' is a dependency of 'openness'`. taplo *does* enforce `type` and `enum`
from that same schema (a `note = "forty-two"` was caught with a caret), so it is not
failing to load the schema — it is no-opping on keywords it doesn't implement. That is a
**silent false negative**, which is worse than an error. `taplo fmt` on the hand-written
TOML produced no changes, i.e. it is a usable canonical formatter.
(`tombi-toml/tombi` v1.5.2, last commit 2026-09-06, is an actively developed alternative
TOML toolkit with claimed newer-draft support — **UNVERIFIED**, not tested here.)

**`frictionless` 5.19.0** (`frictionlessdata/frictionless-py`, last commit 2026-08-27).
Table Schema over the TSV. Best *semantic* coverage of the three:

```
$ frictionless validate dp_bad.json
 Row Field Type              Message
 3   2     constraint-error  The cell "400" … field "note" … does not conform: "maximum" is "127"
 7   1     unique-error      Row at position "7" has unique constraint violation in field "id"…
 7   —     primary-key       Row at position "7" violates the primary key…
```

and — the feature nothing else has — **cross-file referential integrity**:

```
$ frictionless validate dp_fk.json        # notes.id must exist in pivot.tsv
 7   —     foreign-key   Row at position "7" violates the foreign key:
                         for "id": values "snare.rimshot" not found in the lookup table "pivot" as "pivot_id"
```

That is exactly the check KITWARP needs most (every device row's pivot id must exist in the
vocabulary), and **JSON Schema cannot express it**: `uniqueItems` compares whole items, not
a key within them, and there is no cross-document reference keyword. In JSON/YAML/TOML this
check is bespoke Python — which is what every serious precedent in §3 also does.

Maintenance status of every candidate validator/round-tripper, from `git log -1` on
2026-09-06:

| Tool | Latest tag | Last commit | Verdict |
|---|---|---|---|
| `check-jsonschema` | 0.38.0 | 2026-08-17 | actively maintained |
| `frictionless-py` | 5.19.0 (5.20.0rc1) | 2026-08-27 | actively maintained |
| `taplo` | taplo-cli 0.10.0 | 2026-07-28 | maintained, but Draft-4-era semantics |
| `tombi` | v1.5.2 | 2026-09-06 | very active (young) |
| `ajv` | v8.20.0 | 2026-04-24 | maintained |
| `tomlkit` | 0.15.1 | 2026-08-18 | maintained |
| `pyjson5` | — | 2026-06-24 | maintained |
| `hjson-py` | — | 2025-11-02 (docs only) | **~10 months idle** |
| `flatbuffers` | v25.12.19 | 2026-08-11 | maintained |
| `capnproto` | v1.5.0 | 2026-09-03 | maintained |

### 2.6 Criterion 5 — comments for per-entry provenance

| Format | Native comments | Survives a generator write? |
|---|---|---|
| JSON | **no** | n/a |
| JSON5 / JSONC | yes (`//`, `/* */`) | **no** — `json5` lib dropped all 6 |
| YAML | yes (`#`) | only with `ruamel.yaml`, and reattachment is best-effort |
| TOML | yes (`#`) | **yes, exactly** — `tomlkit` kept all 6 byte-identically |
| CSV/TSV | not standardised; `#`-prefixed lines are a convention every reader must be told about (`csv` module does **not** skip them; `frictionless` needs `dialect.commentChar`) | yes (they are just lines) |
| SQLite | no | a `source` column, or SQL `--` comments in the `.dump` only |
| textproto / FlatBuffers JSON | `#` / `//` | no |

**The precedents split cleanly on this, and the split is causal.** Projects whose hand file
is *never* machine-rewritten put provenance in comments and go all-in on it: tzdb's main
data files are **69.1 % comment lines** (14,310 of 20,717; `asia` 74 %, `northamerica`
71 %), and `pci.ids`/`usb.ids` carry free-text notes above entries. Projects whose files
*are* machine-generated or machine-normalised put provenance in **fields**:

- CLDR carries a `draft=` attribute on **169,650** data elements across `common/main`
  (`contributed` 82,908, `unconfirmed` 74,154, `provisional` 12,588) — a per-datum
  confidence axis in the schema, not in a comment; `common/main/de.xml` contains exactly
  **one** XML comment in 100 kB.
- SMuFL's 2,940 vocabulary entries each carry a `description` string; across all 132
  hand-edited `data/ranges/*.yaml` files, only `manifest.yaml` has any `#` comments at all
  (2 lines).
- iso-codes' `validate_json_data.py` **re-writes** every data file
  (`json.dump(..., indent=2, sort_keys=True)`) as part of validation — comments could not
  survive even if JSON had them, so provenance lives in `official_name`/`common_name`
  fields.
- systemd's hwdb goes further: the compiled trie's `trie_value_entry2_f` record carries
  `filename_off` and `line_number`, so the *binary* knows which source file and line each
  property came from.

**Implication for KITWARP:** the comment-support question is downstream of a workflow
decision. If the generator writes the hand file, provenance must be a field regardless of
format, and JSON's lack of comments costs nothing. If the generator never writes the hand
file, comments work everywhere except JSON.

### 2.7 Criterion 6 — key-order stability

No text format guarantees order by itself; every precedent enforces it with a check:

- **tzdb**: `make check` includes a `sorted.ck` target among `character-set.ck`,
  `white-space.ck`, `name-lengths.ck`, `links.ck`, `tables.ck`, `slashed-abbrs.ck`,
  `ziguard.ck`.
- **pci.ids / usb.ids**: the file header literally says `# Vendors, devices and subsystems.
  Please keep sorted.`, and hwdata's `make check` runs a 39-line `check-pci-ids.py` that
  fails with `"%d: Vendor ID (0x%04x) is less that previous ID (0x%04x)"`.
- **iso-codes**: sorts and rewrites in the validator, so the check *is* the fixer.
- **SMuFL**: `tools/generate.py --check` asserts the committed metadata equals what the
  generator would emit.

Python `json.dumps(sort_keys=True)` and `tomlkit`'s CST both give deterministic output.
The practical rule that emerges: **have one canonical formatter and a CI mode that fails if
the committed file differs from its output.** Format choice is secondary.

### 2.8 Criterion 7 — merge-conflict behaviour (the decisive experiment)

Two curators branch from the same commit; each inserts one new snare record at the same
sorted position (`snare.crossstick` note 37 / `snare.flam` note 39). `git merge`, then
resolve naively.

Correct answer in every case: **10 records.**

| Format | Conflict regions | "take mine" | "take both" | Parses after "take both"? |
|---|---:|---:|---:|---|
| JSON, block (`indent=2`) | **2** | 9 records | **9 records — one insert silently lost** | **yes** |
| TOML, `[[notes]]` blocks | 1 | 9 | 9 (duplicate `id` key in one table) | **no** — `tomllib.TOMLDecodeError: Cannot overwrite a value` |
| YAML, block | 1 | 9 | 9 | yes |
| **JSON, one record per line** | 1 | 9 | **10 records** | **yes** |
| **TSV** | 1 | 9 | **10 rows** | yes |
| SQLite `.db` | — | — | — | `warning: Cannot merge binary files: kw.db` |

The JSON result is the one to put in the ADR. Git's line-based merge saw that both branches
inserted blocks sharing the lines `"articulation": "hit",`, `"damping": "none",`,
`"instrument": "snare",` … and merged those silently, conflicting only on the two lines that
differed:

```
<<<<<<< HEAD              <<<<<<< HEAD
      "id": "snare.crossstick",       "note": 37,
=======                   =======
      "id": "snare.flam",             "note": 39,
>>>>>>> brB               >>>>>>> brB
```

Taking `HEAD` in both regions yields **one** record (`snare.crossstick`, 37) where there
should be two, and `snare.flam` is gone with no trace. Taking both sides yields a record
with duplicate `"id"` and `"note"` keys — which `json.loads` accepts (last wins) and
returns **9 notes**. And:

```
plain json.loads          : OK, 9 notes
JSON Schema validate      : PASSES (does not see the loss)
duplicate-key hook        : CAUGHT -> duplicate key 'id'
```

**A JSON Schema will not catch this.** The document is structurally valid; it is just
missing a record. Only a duplicate-key rejecting loader catches it — which is precisely why
QMK's `lib/python/qmk/json_schema.py` passes
`object_pairs_hook=_dict_raise_on_duplicates` to every load. TOML at least fails loudly
(`Cannot overwrite a value`); block YAML is as silent as JSON.

**The property that matters is line-orientation, not the format.** One record per line makes
"keep both" the obvious and correct resolution, and it makes it impossible for git to
interleave two records. `f.json` (one-record-per-line JSON) and `e_col.tsv` behave
identically and correctly.

The one cost of line-oriented JSON over TSV: appending a record at the end also touches the
previous line to add a trailing comma —

```
 e_col.tsv | 1 +
 f.json    | 3 ++-
```

— so two branches appending at the end conflict where TSV would not. JSON Lines (`.jsonl`,
no wrapper array, no commas) removes even that, at the cost of `check-jsonschema` not being
able to read it.

**SQLite**: a single-cell `UPDATE` changed exactly 3 bytes of the 12,288-byte file; git
reported `kw.db | Bin 12288 -> 12288 bytes / 1 file changed, 0 insertions(+), 0
deletions(-)` and `Binary files differ`, and stored a whole new 12 KB blob. A
`.dump`/`textconv` gitattribute recovers a perfect one-line diff for *review*
(`-INSERT INTO "note" VALUES('snare.rimshot',40,…)` / `+…41,…`), and the dump proved
insert-order-stable across an insert/delete/insert cycle. It does **not** recover merging:
`git merge` on two branches that each inserted a row printed
`warning: Cannot merge binary files: kw.db` and left an unresolvable conflict. There is no
three-way merge driver for SQLite in general use.

---

## 3. How comparable curated device databases are actually stored

### 3.1 tzdata / `zic` — the closest analogue, and what it specifically implies

| Fact | Measured |
|---|---|
| Hand-maintained data files | 11 (`africa`, `asia`, `europe`, `northamerica`, …) |
| Total lines | 20,717 |
| Comment lines | **14,310 (69.1 %)** |
| Data lines | 4,817 (23.3 %) |
| The compiler | `zic.c`, **4,334 lines** of C |
| Compiled output | `TZif` binary; nothing parses `northamerica` at runtime |
| A second, machine-canonical text form | `tzdata.zi`, generated by `zishrink.awk` (388 lines) |
| A tabular companion file | `zone1970.tab` — **tab-separated**, one row per zone |
| Validation | `make check` → `character-set.ck white-space.ck links.ck mainguard.ck name-lengths.ck news.ck slashed-abbrs.ck sorted.ck tables.ck ziguard.ck tzs.ck back.ck now.ck`, implemented in `checktab.awk` (228 lines), `checklinks.awk` (70), `checknow.awk`, `leapseconds.awk` |
| Dialect variants from one source | `vanguard.zi` / `rearguard.zi` via `ziguard.awk` (382 lines) |

The data syntax is line-oriented, tab-separated, with a first-column keyword:

```
# Rule  NAME  FROM  TO   -  IN   ON       AT    SAVE  LETTER
Rule    NYC   1921  1966 -  Apr  lastSun  2:00  1:00  D
# Zone  NAME              STDOFF   RULES  FORMAT  [UNTIL]
Zone America/New_York     -4:56:02 -      LMT     1883 Nov 18 17:00u
                          -5:00    US     E%sT    1920
```

Seven things this specifically implies for KITWARP:

1. **Two artifacts, never one.** The hand file is text; the thing programs read is a
   compiled binary. Nothing ever re-serialises `northamerica`. That is exactly KITWARP's
   requirement ("compiles into a C++ monolith, no runtime parser") and it is the single
   most important structural lesson.
2. **Because nothing rewrites the hand file, comments can be 69 % of it.** tzdb's comments
   are not decoration — they are the evidence (`# From Paul Eggert (2024-11-18): Dowd's
   proposal left many details unresolved…`, citations to Howse 1997). KITWARP's `.iom`
   provenance and manual-page citations are the same kind of content. If KITWARP adopts a
   never-rewrite rule, it can have this. If it lets a scraper write the file, it cannot.
3. **A separate, generator-owned canonical text export is normal.** `tzdata.zi` is
   diff-stable, machine-readable, and not hand-edited. KITWARP's analogue is the export
   that `tools/export --check` already guards in `.github/workflows/ci.yml`.
4. **No general-purpose schema language is used, and it would not have been enough.** All
   thirteen checks are project-specific invariants — sortedness, name-length limits,
   cross-table link integrity, character-set restrictions. Plan for a `tools/validate` that
   is mostly bespoke Python; the schema handles field types, not the interesting rules.
5. **The compiler is a permanent cost.** 4,334 lines of C, maintained for four decades.
   KITWARP's equivalent (a Python emitter of `.h`) is far smaller, but it is a component
   with a test suite, not a script.
6. **One source, several output dialects.** vanguard/rearguard exist because consumers have
   different capabilities. KITWARP's analogue is a full-fidelity pivot export versus a
   GM-degraded one — worth designing the generator for from the start.
7. **tzdb is itself a hybrid.** `zone1970.tab` is TSV, one row per entity, because that
   part of the data *is* a table. The custom multi-line format is used only for the part
   that genuinely is not (a Zone's history is a variable-length continuation list).
   The multi-line block form is tolerable there because tzdb is edited by essentially one
   maintainer through a mailing list, not by concurrent pull requests. KITWARP will have
   concurrent pull requests; §2.8 says what that costs.

### 3.2 `pci.ids` / `usb.ids` / hwdata — the hand-curated text DB with a compiler that isn't one

- `pci.ids`: 43,047 lines, 1,591,819 bytes. `usb.ids`: 25,705 lines. `pnp.ids`: 2,557.
- Format: tab-depth-significant, `id␠␠name`, two levels of nesting plus `C`/`S`-prefixed
  section blocks. Free comments anywhere.
- Licence stated in the file: *"can be distributed under either the GNU General Public
  License (version 2 or higher) or the 3-clause BSD License… The database is a compilation
  of factual data, and as such the copyright only covers the aggregation and formatting."*
  — a useful precedent for KITWARP's own licensing of collected device data.
- **Real churn**: 20 consecutive snapshot commits sampled from history changed
  3–33 lines each in a 43,047-line file (median ~7). A line-oriented text DB keeps diffs
  proportional to the semantic change at 43 k lines and daily update traffic.
- **But the git file is an export, not the curation surface.** Commits are titled
  `New snapshot generated`, and `update-pciids.sh` downloads from
  `https://pci-ids.ucw.cz/v2.2/pci.ids`. The humans curate in a **web database**; git gets
  a generated snapshot. At sufficient scale the hand-editing story stops being "edit the
  text file".
- **The "compiler" is a runtime parser.** `lib/names-parse.c` parses all 1.5 MB on every
  `lspci` invocation into a hash table (`id_parse_list`, hand-rolled `sscanf`-free scanner).
  There is no compiled form; `lib/names-cache.c` is a DNS-lookup cache, not an ids cache.
  For a CLI that is fine; **for an audio plugin it is exactly the anti-pattern** — 1.5 MB of
  text parsed and hashed on every instantiation, with allocation.
- Validation in hwdata's `make check`: `check-pci-ids.py` (sort order), `iconv -f UTF-8`
  (encoding), and — notably — **running the real consumer over the file**
  (`lspci -A dump -i pci.ids`). That "the consumer must parse it" acceptance test is
  already mirrored in KITWARP's `tools/iom/roundtrip_check.py`.

### 3.3 systemd `hwdb` — text source, compiled trie, provenance carried into the binary

- 383,927 lines across 39 `hwdb.d/*.hwdb` files (`60-keyboard.hwdb`, `70-mouse.hwdb`,
  `20-pci-vendor-model.hwdb`, …).
- Syntax: a match pattern line, then indented ` KEY=value` property lines; `#` comments.
- `hwdb.d/README`: *"Files in this directory are not read by udev directly. Instead,
  systemd-hwdb compiles them into a binary database."* — the tzdata model, restated.
- The binary is an **mmap-able trie** with signature `KSLPHHRH`
  (`src/libsystemd/sd-hwdb/hwdb-internal.h`): `trie_header_f`, `trie_node_f`,
  `trie_child_entry_f`, `trie_value_entry_f`. Lookup is pointer arithmetic over a mapped
  file — no parse, no allocation.
- **`trie_value_entry2_f` carries `filename_off`, `line_number` and `file_priority`.**
  The compiler pushes source provenance *through* into the binary. If KITWARP wants
  "which source row produced this mapping?" available in a debug build, this is the
  precedent for doing it in the generated table rather than in a side file.

### 3.4 CLDR — XML + DTD, generated code, per-datum confidence

- `common/main`: 1,148 locale XML files, 94 MB. `common/dtd`: `ldml.dtd`,
  `ldmlSupplemental.dtd`, plus `.xsd` equivalents.
- The DTD is a real content model, not decoration:
  `<!ELEMENT ldml ( identity, ( alias | ( fallback*, localeDisplayNames?, layout?, … ) ) ) >`
  and enumerated attributes:
  `<!ATTLIST ldml draft (approved|contributed|provisional|unconfirmed|true|false) #IMPLIED >`.
- **`draft=` appears on 169,650 elements.** A first-class per-datum confidence axis.
  KITWARP's `UNVERIFIED` marking should be this: a schema-constrained field with a closed
  vocabulary (`verified` / `contributed` / `provisional` / `unverified`), not a comment
  convention.
- `alt=` gives alternate forms of the same datum (`narrow` 17,161, `variant` 3,650,
  `short` 1,803, `menu` 554, …) — the precedent for KITWARP carrying a device's *display
  name* variants (module UI label vs manual label vs DAW drum-map label) as one record with
  alternates, rather than as separate records.
- Data is not primarily hand-edited in the files: it comes from the Survey Tool and is
  written back by CLDR tooling; ICU then compiles it to a binary resource bundle. Same
  three-stage shape: curation surface → canonical text in git → binary for the consumer.

### 3.5 iso-codes — JSON + JSON Schema as source of truth, XML as the *generated* artifact

- `data/`: `iso_639-3.json` (876 KB), `iso_3166-2.json` (498 KB), `iso_3166-1.json`,
  `iso_4217.json`, `iso_15924.json`, … each with a sibling `schema-*.json`.
- `meson.build` custom targets generate the now-deprecated `.xml` **from** the JSON via
  `scripts/xml_from_json.py`. The direction of travel is XML → JSON, not the reverse.
- The schemas are ordinary JSON Schema with `pattern`, `required` and
  `"additionalProperties": false` — e.g. `alpha_2: {"pattern": "^[A-Z]{2}$"}`,
  `flag: {"pattern": "^[🇦-🇿]{2}$"}`.
- `scripts/validate_json_data.py` does three things in one pass and is worth copying
  wholesale as a model:
  1. `jsonschema.validate(data, schema)` per standard;
  2. **sort the records by their key and re-write the file**
     (`json.dump(iso, f, ensure_ascii=False, indent=2, sort_keys=True)` + final newline) —
     the canonical formatter *is* the validator;
  3. a hand-written duplicate-key detection loop over `alpha_2`, `alpha_3`, `alpha_4`,
     `numeric`, `code`, because JSON Schema cannot express it.

### 3.6 SMuFL — the closest analogue to a *pivot vocabulary*, and the best CI in the sample

`w3c/smufl` is a curated symbolic vocabulary of 2,940 music-notation glyph names. Its shape
is what KITWARP's pivot vocabulary wants to be:

```json
{
  "4stringTabClef":            { "codepoint": "U+E06E", "description": "4-string tab clef" },
  "accSagittal11LargeDiesisUp":{ "codepoint": "U+E30C", "description": "11 large diesis up, (11L), … [46 EDO]" }
}
```

302,519 bytes, **103 bytes per term** — the same order as KITWARP's 105 B/note TSV, so a
few-hundred-term pivot vocabulary is a ~30 KB file. Plus `ranges.json` (132 ranges, each
listing its member glyph names) and `classes.json` — i.e. the vocabulary and its groupings
are separate files with cross-references, not one nested tree.

**The architecture is a hybrid, and the split is source-vs-derived, not tabular-vs-nested:**

- `data/ranges/*.yaml` (132 files) + `data/*.yaml` — **hand-edited source**, YAML, one file
  per range, essentially comment-free (provenance is the `description` field).
- `metadata/*.json` — **generated and committed**, the published artifact consumers read.
- `metadata/schema/*.json` (Draft-07) and `data/schema/*.json` — the schemas.

Its CI (`.github/workflows/pages.yml`) is the single best template found:

```yaml
- run: pip install check-jsonschema
- run: check-jsonschema --schemafile metadata/schema/glyphnames.schema.json metadata/glyphnames.json
- run: check-jsonschema --schemafile metadata/schema/ranges.schema.json     metadata/ranges.json
- run: check-jsonschema --schemafile metadata/schema/classes.schema.json    metadata/classes.json
- run: python3 metadata/schema/check_consistency.py
- run: python3 metadata/schema/check_immutability.py       # codepoints frozen against v1.4
- run: find data/ranges -name '*.yaml' ! -name 'manifest.yaml' -print0 | xargs -0 check-jsonschema --schemafile data/schema/range.schema.json
- run: python3 tools/generate.py --check                   # generated output == committed metadata
- run: python3 tools/sync_ufo_glyphs.py --check
```

`check_consistency.py`'s own docstring states the general law: *"These are checks that a
JSON Schema alone can't express: relationships between glyphnames.json, ranges.json and
classes.json. Run after schema validation has already passed."* And `check_immutability.py`
is the one KITWARP most needs and would not have thought of: **once a pivot term is
published, its identity must never change**, and that is a CI check against a frozen
baseline, not a schema.

### 3.7 QMK / ZSA — JSON + JSON Schema + Python generators emitting C

- Schemas: `data/schemas/{keyboard,keymap,keycodes,definitions,community_module}.jsonschema`,
  `$schema: https://json-schema.org/draft/2020-12/schema#`, with `$ref` across files
  (`{"$ref": "./definitions.jsonschema#/text_identifier"}`).
- Constants: `data/constants/keycodes/keycodes_0.0.*.hjson` — **versioned** vocabulary
  files, so a keycode set is frozen per spec version and new versions are additive. Each
  entry: `{"group": "quantum", "key": "QK_LAYER_LOCK", "label": "Layer Lock", "aliases":
  ["QK_LLCK"]}`, and `"!delete!"` as an explicit tombstone for retired codes. That
  versioning + tombstone pattern is directly applicable to a pivot vocabulary that must
  never silently re-mean a term.
- Mappings: `data/mappings/*.hjson` (Hjson — JSON with `//` comments and unquoted keys).
  **Caution:** `hjson-py` is the least maintained tool surveyed (last commit 2025-11-02,
  documentation only).
- Loading: `lib/python/qmk/json_schema.py` loads *everything* through `hjson.load` with
  `object_pairs_hook=_dict_raise_on_duplicates` — duplicate keys are a hard error. Given
  §2.8, this is not paranoia.
- Codegen: `lib/python/qmk/cli/generate/{keycodes,keyboard_c,keyboard_h,keymap_h,config_h,rules_mk,dfu_header,autocorrect_data,rgb_breathe_table}.py` — Python
  string-building, emitting `enum qk_keycode_ranges { … }`, `#define IS_…(code)` helpers,
  and aliases. Plain `lines.append(f'    {value.get("key")} = {key},')`. No template engine,
  no C++ metaprogramming. This is the low-tech approach and it is what a 30 k-file project
  actually uses.
- ZSA `oryx-keymaps` could not be inspected (repository not publicly clonable).

### 3.8 ALSA UCM — one directory per device, runtime-parsed

`ucm2/<Vendor>/<Model>/{<model>.conf, HiFi.conf, init.conf, …}` in alsa-lib's config
syntax (a JSON superset with `Section…{}` blocks, `[]` sequences and `${Var}` substitution).
Parsed at runtime by alsa-lib. The relevant lesson is only structural: **one directory per
device, with a small entry-point file that `Include`s the rest**, scales to hundreds of
devices without a monolithic file. No schema, no CI validation found.

### 3.9 MIDNAM — the MMA's own per-device MIDI name format

475 `.midnam` files in Ardour, 23 MB — **48 KB per device**. XML validated against
`MIDINameDocument10.dtd`. `share/patchfiles/README` states the whole discipline in eight
lines:

```
All documents validate against MIDINameDocument10.dtd.
To validate a document, run:
    xmllint --dtdvalid MIDINameDocument10.dtd Acme_Synthomatic.midnam > /dev/null
The same tool can be used to format the file nicely:
    xmllint --format My_Device.ugly.midnam > Acme_Synthomatic.midnam
```

i.e. **one validator + one canonical formatter, both the same off-the-shelf binary.** The
warning is the size: `Alesis_DM5.midnam` spends its first 40 lines on 16
`<ChannelNameSetAssign>` and 16 `<AvailableChannel>` boilerplate elements before reaching
any of its 1,281 `<Note>` entries. Ardour parses these at runtime
(`libs/midi++2/midnam_patch.cc`). MIDNAM is the incumbent interchange format in this exact
domain, and it is 460× more verbose per device than a TSV row set.

### 3.10 `lotkey/Drum-MIDI-Converter` — the domain-specific precedent, and a warning

This is KITWARP's problem solved once already, and its storage decisions are instructive in
both directions.

- **The vocabulary is a directory of indentation-trees.** `src-cpp/mappings/tree/{cymbal,
  hat,kick,perc,snare,tom}.txt`, 235 lines total, `*`-prefix marking a valid leaf:

  ```
  hit
      closed
          *edge
              *_1
              tight
                  *_1
          *tip
              *_1
  ```

  Hand-curatable, tiny, and with **no schema, no validation and no comment convention**
  (indentation is significant and `*` is unexplained in-file).

- **A generator compiles that tree into C++.** `update-mappings/update.cpp --keys` emits
  `SampleTree/Keys.hpp` (330 lines, 170 terms) as nested namespaces:

  ```cpp
  namespace Cymbal { namespace Bell { namespace Crash { namespace Tip {
      const string _1 = "cymbal_bell_crash_tip__1";
  ```

- **Device layouts are hand-written C++, and the compiler is the validator.**
  37 files, 1,668 lines, e.g. `Mappings/Toontrack/SuperiorDrummer3.cpp`:

  ```cpp
  {Cymbal::Bell::China::_1,        {{Note::C_SHARP, 7}}},
  {Cymbal::Hit::China::_1,         {{Note::E, 2}, {Note::D, 7}}},
  ```

  One line per note, self-identifying in a diff, merge-safe, and a typo in a pivot term is
  a **compile error** — free referential integrity, no `foreignKeys` needed. This is a
  genuinely strong property that no data format gives you.

- **The interchange export is an opaque blob.** `src-python/conversions.lkcmap` is 3,954
  lines of packed ASCII (`$$%%&&(())++,,--..2233445566778899<<==>>??AABBCCDDEEFFHCIDJEKF…`)
  — machine-written, unreviewable, unmergeable. Derived artifact, and it shows.

- **The warning.** `const std::string _1 = "…"` at namespace scope, **170 times**. That is
  170 dynamic initialisers and 170 heap allocations executed when the library loads,
  with static-initialisation-order fragility. For a VST3 that a host may instantiate dozens
  of times, this is the failure mode KITWARP's "no allocation" requirement exists to avoid.
  §4 measures exactly what it costs and how to avoid it.

### 3.11 Linux kernel device tables

*Stated from knowledge; the kernel tree was not cloned (a blobless clone was judged too slow
for the value). Treat as **UNVERIFIED** in detail, though the shape is well established.*
Drivers declare `static const struct pci_device_id foo_tbl[] = { … };` in C, annotated with
`MODULE_DEVICE_TABLE(pci, foo_tbl)`; `scripts/mod/file2alias.c` reads those structures out
of the compiled object's ELF section **at build time** and emits `MODULE_ALIAS("pci:v…d…")`
strings into the generated `.mod.c`. Source of truth is C source; the "database" is
extracted from it rather than compiled into it. Same conclusion as Drum-MIDI-Converter:
when the data lives next to the code and only the code reads it, C source is a legitimate
storage format and the compiler is the schema.

### 3.12 Summary of precedent

| Project | Source of truth | Schema / validator | Consumer artifact | Provenance in |
|---|---|---|---|---|
| tzdata | custom line-oriented text | 13 bespoke awk/make checks | `TZif` binary via `zic` (4,334 LOC C) | comments (69 % of file) |
| pci.ids / usb.ids | tab-indented text (generated from a web DB) | sort check + UTF-8 + consumer round-trip | none — **parsed at runtime** | comments |
| systemd hwdb | `.hwdb` text | none formal | mmap'd binary trie | comments + `line_number` in the binary |
| CLDR | XML | DTD + XSD + CLDR tooling | ICU binary resource bundles | `draft=` attribute (169,650×) |
| iso-codes | **JSON** | `jsonschema` + sort-rewrite + dup check | JSON (XML generated, deprecated) | fields |
| SMuFL | **YAML** (`data/`) | `check-jsonschema` + 2 bespoke Python checks + `generate.py --check` | **JSON** (`metadata/`) | `description` field |
| QMK | **JSON / hjson** | `jsonschema` 2020-12 + dup-key hook | generated `.c` / `.h` | fields, versioned files, `!delete!` tombstones |
| ALSA UCM | alsa-conf text, one dir/device | none | none — runtime parse | comments |
| MIDNAM | XML, one file/device | `xmllint --dtdvalid` | none — runtime parse | `<Author>` element |
| Drum-MIDI-Converter | indentation tree + **hand-written C++** | **the C++ compiler** | compiled into the binary | none |
| Linux device tables | **C source** | the C compiler | extracted at build time | comments |

Two patterns repeat with no exceptions:

1. **Nothing that must be fast reads the curated text at runtime.** Every project that cares
   about load time compiles to a binary or to C. The two that parse text at runtime
   (`lspci`, Ardour MIDNAM) are tools where a few milliseconds do not matter.
2. **The hand file and the machine file are different files.** Where a single file is both
   (iso-codes), the machine's write is a *canonicalisation* and comments were never an option.

---

## 4. Criterion 4 — compiling into a single C++ binary, measured

13,500 rows × 11 columns. `g++ 13.3.0 -O2 -std=c++20`, x86-64 PIE. Sections from
`size -A`, relocations from `readelf -r … | grep -c RELATIV`.

| # | Approach | `.rodata` | `.data.rel.ro` | Relocs | Binary | Compile | Startup cost | Audio-thread safe |
|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | **constexpr enum-id rows + offset string pool** | 344,402 | **0** | **3** | 360,552 | **0.39 s** | **none** | yes |
| 2 | constexpr enum-id rows + `array<string_view>` dicts | 288,486 | **127,488** | **7,970** | 622,736 | 0.75 s | RELRO relocation of 8 k pointers, pages dirtied | yes |
| 3 | constexpr `{offset,len}` per field, no enum ids | 1,252,592 | 0 | — | 1,269,456 | 2.77 s | none | yes |
| 4 | `xxd -i` / CMake `bin2c` of the TSV + hand parser | 1,035,563 | 0 | 3 | 1,052,488 | 2.77 s | **830 µs** parse | only if the parser allocates nothing |
| 5 | **FlatBuffers** blob via `bin2c`, zero-copy | 391,532 | 0 | 3 | 405,208 | 1.52 s | none | yes |
| 6 | Cap'n Proto unpacked blob | 430,064 (blob) | 0 | — | — | — | none | yes |
| 7 | Cap'n Proto **packed** blob | 347,903 (blob) | — | — | — | — | unpack pass + buffer | **no** (allocates) |
| 8 | CBOR blob, dictionary-encoded | 344,089 | — | — | — | — | decode + build index | **no** |
| 9 | MessagePack blob, dictionary-encoded | 316,906 | — | — | — | — | decode + build index | **no** |
| 10 | CBOR blob, naive (row = map of strings) | 2,277,456 | — | — | — | — | decode | **no** |
| 11 | gzip'd TSV embedded | 169,971 | — | — | — | — | inflate + parse + index | **no** |
| — | raw JSON, for reference | 4,207,863 | — | — | — | — | — | — |

Row widths: hand-packed struct **12 bytes**; FlatBuffers `struct` **14**; Cap'n Proto
struct **16** (8-byte word rounding).

### 4.1 The findings that only show up when you measure

**(a) Dictionary-encode the axes, and it is not close.** Approach 3 stores an
`{offset,len}` pair per field per row (10 × 8 bytes after padding + note) → 1.25 MB.
Approach 1 stores a small integer id per axis (`uint8_t` where cardinality ≤ 256,
`uint16_t` otherwise) → `sizeof(Row) == 12`, rows = 162 KB. **7.7× smaller and 7× faster to
compile, from the same data.** Measured axis cardinalities in the synthetic set: device 150,
instrument 12, instance 48, zone 10, articulation 10, openness 6, damping 4, implement 6,
limb 5 — every KITWARP axis except the pivot id itself fits in a `uint8_t`. This also makes
comparisons integer compares instead of string compares in the hot path.

**(b) `constexpr std::array<std::string_view, N>` is not free — it costs relocations.**
Approach 2 vs approach 1 is the *same data*, differing only in whether the dictionaries hold
`string_view` (pointer + size) or `{uint32 offset, uint16 len}` into one `constexpr char
kPool[]`:

```
approach 2:  7,970 R_X86_64_RELATIVE relocations, 127,488 bytes of .data.rel.ro
approach 1:      3 R_X86_64_RELATIVE relocations,       0 bytes of .data.rel.ro
```

Every `string_view` holds a pointer, so in a PIE (which a VST3 bundle is) the dynamic
loader must rewrite all 8 k of them at load and the pages become private-dirty instead of
shared-clean. The offset-pool form is pure integers: the whole table lands in `.rodata`,
demand-paged straight from the plugin binary and shared across every instance the host
loads. `readelf -S` confirms `.rodata` is `A` (alloc, read-only, not writable).

**(c) There are no dynamic initialisers either way.** `size -A` shows `.init_array = 8`
bytes (the single standard entry) for approaches 1, 2 and 4, `.data = 16`, `.bss = 8`, and
`nm -C | grep GLOBAL__sub_I` is empty. This is the property Drum-MIDI-Converter's 170
namespace-scope `const std::string` objects throw away.

**(d) Do the sorting in the generator, not in `constexpr`.** An attempt to build a
`std::lower_bound` index with a `constexpr` insertion sort over 13,500 rows did not finish
in 120 s of `cc1plus` (O(n²) in the constant evaluator). Emitting rows already sorted from
Python and doing a plain `std::lower_bound` at runtime: 128 lookups in **13.6 µs cold**
(~107 ns each, including first-touch page faults), zero allocation. General rule: the
generator computes, the header only declares.

**(e) The embedded-blob-plus-parser approach costs 830 µs at startup and 3× the size.**
Approach 4's parser is a `std::string_view` scanner that allocates nothing, and it still
takes 830 µs (measured over three runs: 831 / 808 / 834 µs) to walk 13,500 rows — and that
is *without* building any lookup index, which is what you would actually need and which
would allocate. Meanwhile it costs 1.04 MB of `.rodata` versus 344 KB. `xxd -i` and CMake's
`file(READ … HEX)` are the mechanisms here; in a JUCE plugin the same thing is
`juce_add_binary_data()`. It is the easiest thing to build and the worst result of the
serious options.

**(f) FlatBuffers works and is genuinely zero-copy, but loses on every axis to codegen.**
`flatc --cpp kw.fbs` produced a 347-line header; `flatc -b kw.fbs kw.json` compiled the JSON
to a 391,460-byte binary; embedding that with `bin2c` and calling `kwfb::GetDb(fb::kBin)` is
a pointer cast and one offset read. Scanning all rows: 16–39 µs, statistically the same as
the constexpr table's 17–23 µs (both are dominated by page faults). But: 391 KB vs 344 KB
`.rodata`, 405 KB vs 360 KB binary, 1.52 s vs 0.39 s compile, plus a schema language, a code
generator, and the FlatBuffers runtime headers as build dependencies. It buys nothing that
codegen does not already give.

There is one thing `flatc` *does* buy, worth noting for completeness: **`flatc -b
schema.fbs data.json` is a validator.** The `.fbs` schema rejects unknown fields and
out-of-range enums when compiling the JSON text form. That is option H's text-format story
and it is real — but it validates far less than JSON Schema (no `pattern`, no `minimum`, no
`dependentRequired`) and it requires `flatc` in CI.

**Cap'n Proto**: `capnp compile -oc++` produced `kw.capnp.h` (17,294 bytes) +
`kw.capnp.c++` (12,952). `capnp convert json:binary` → 430,064 bytes;
`capnp convert json:packed` → 347,903. The unpacked form is mmap-able zero-copy like
FlatBuffers, at 16 bytes/row because struct data sections round to 8-byte words. **The
packed form must be unpacked into a buffer before use** — an allocation and a decode pass —
so it is disqualified by the no-allocation requirement despite being the smaller number.

**(g) Compile time scales roughly linearly on GCC.** 135,000 rows (10×) → 2.97 s and
1.62 MB `.rodata`, from 0.39 s and 344 KB. No superlinear blow-up. **UNVERIFIED for MSVC**,
which historically handles very large brace-initialised `constexpr` arrays much worse than
GCC/Clang; since KITWARP must build a Windows VST3, this needs a one-off measurement on the
real toolchain before the table size is locked in. Mitigation if MSVC is a problem: split
the table across several translation units (one per device family), or fall back to
approach 5 (FlatBuffers blob), which is a `bin2c` array of bytes and compiles uniformly.

### 4.2 The recommended generated-header shape

```cpp
// GENERATED FILE - do not edit. Source: data/devices/*.json @ <git sha>
#pragma once
#include <array>
#include <cstdint>
#include <string_view>
namespace kw {

inline constexpr char kPool[] = "kickhihatsnare…";                 // one string arena
struct Str { std::uint32_t off; std::uint16_t len; };
constexpr std::string_view sv(Str s) { return {kPool + s.off, s.len}; }

inline constexpr std::array<Str, 12> k_instrument = {{ {0,4}, {4,5}, … }};   // per-axis dict
// … one array per axis …

struct Row {                     // 12 bytes, no pointers
  std::uint8_t  note;
  std::uint16_t device, pivot_id;
  std::uint8_t  instrument, instance, zone, articulation,
                openness, damping, implement, limb;
};
inline constexpr std::array<Row, 13500> kRows = {{ {42,0,17,2,1,5,0,1,0,0,0}, … }};
// emitted PRE-SORTED by (device, note) so lookup is std::lower_bound over .rodata
}
```

Properties, all measured above: 3 relocations, `.init_array` = 8 bytes, no constructor, no
allocation, entire table in shared read-only pages, integer comparisons in the hot path,
0.39 s of compile time, and string text reachable only when a UI actually needs it.

---

## 5. Decision matrix

Scores: **++** strong, **+** adequate, **o** neutral/workable-with-effort, **−** weak,
**−−** disqualifying. "JSON (line-oriented)" means option A serialised one record per line,
as `marty-615/drum-remap` already does in `maps/*.json`.

| | A. JSON (block) | A′. **JSON (line-oriented)** | B. YAML | C. TOML | D. JSON5/JSONC | E. CSV/TSV | F. Hybrid TSV+TOML | G. SQLite | H. FlatBuffers/capnp/textproto |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1a One-line change is a one-line diff | + | ++ | + | + | ++ | ++ | ++ | −− (binary) |  − |
| 1b Changed line self-identifying | − | ++ | − | + (id-first + hunk header) | ++ | ++ | ++ | − (only via textconv) | − |
| 1c Generator round-trip is byte-exact | ++ (own the layout) | ++ | + (ruamel, tuned, canonical input only) | ++ (**tomlkit, even non-canonical**) | − (comments lost) | ++ | + | o (dump is stable; file is not) | ++ |
| 2 Machine-generatable | ++ (stdlib) | ++ (stdlib) | + (new dep) | + (new dep) | + | ++ (stdlib) | + | ++ | o (needs a compiler) |
| 3 Schema-validated in CI, maintained tool | ++ `check-jsonschema` 2020-12 | ++ (7-line shim for `.jsonl`) | ++ same tool | + same tool; `taplo` is prettier but **silently ignores 2020-12 keywords** | + same tool w/ `--force-filetype` | ++ `frictionless` (**unique + primaryKey + cross-file foreignKey**) | ++ both | o (CHECK constraints only) | o (`.fbs`/`.capnp` types only; no pattern/range) |
| 4 Compiles to constexpr, no runtime parser | ++ | ++ | ++ | ++ | ++ | ++ | ++ | + (generator reads it fine) | + (blob is 14 % bigger, 4× compile) |
| 5 Per-entry provenance comments | −− (none) | −− (use a field) | + (ruamel; reattachment fragile) | ++ (**tomlkit exact**) | + hand-only, destroyed on write | o (`#` convention, reader must opt in) / ++ as a column | ++ | − (column only) | + (textproto `#`), destroyed on write |
| 6 Key-order stability | ++ `sort_keys` | ++ | + | ++ | + | ++ | ++ | + | ++ |
| 7 Merge safety (measured) | **−− silent record loss** | ++ **10/10 correct** | − silent | + loud parse failure | + | ++ **10/10 correct** | ++ | −− `Cannot merge binary files` | −− |
| 8 New dependencies for this repo | **0** | **0** | ruamel.yaml | tomlkit | json5 | 0 (+frictionless for the good checks) | 2 | 0 | flatc/capnp toolchain |
| 9 Sparse optional axes (9–10 axes, 3–5 used) | ++ | ++ | ++ | ++ | ++ | **− fixed columns; empty-tab miscount is a silent axis shift** | + | ++ | ++ |
| 10 Precedent in this exact problem class | iso-codes, QMK, SMuFL output | drum-remap `maps/*.json` | SMuFL sources | — | QMK (hjson, least-maintained tool) | tzdb `zone1970.tab`, pci.ids | **tzdb, SMuFL, CLDR** | none found | Cap'n Proto/FB used for *derived* data only |

---

## 6. Recommendation

**Store the data as JSON, emitted one record per line, with provenance and confidence as
schema-constrained fields; validate with `check-jsonschema` plus bespoke Python; never let
a generator rewrite a hand file in place; compile to an enum-indexed `constexpr` table with
an offset string pool.**

Concretely, six decisions:

1. **Format: JSON**, in two serialisation dialects that a single `tools/format.py` owns.
   - `vocabulary/pivot.json` — block-formatted, an object keyed by symbolic pivot id,
     SMuFL-style. A few hundred entries at ~100 B each ≈ 30 KB. Nested structure (axis
     domains, fallback chains, `expand` rules) lives here and block form is right for it.
   - `data/devices/<vendor>/<model>.json` — **one note record per line** inside the `notes`
     array. This is the §2.8 merge-safety property and the §2.2 self-identifying-diff
     property, and `marty-615/drum-remap` already writes its `maps/*.json` this way with
     hand column alignment and blank-line grouping.
   - Rationale for JSON over TOML/YAML/TSV: zero new dependencies (the repo's
     `requirements.txt` explicitly asks for this); the strongest maintained validator with
     full 2020-12 semantics; sparse optional axes are free, where TSV's fixed columns turn
     9–10 axes into a wall of tabs in which a miscount silently shifts a value into the
     wrong axis; and — measured — line-oriented JSON matches TSV exactly on both merge
     safety and diff readability, which were the only two criteria TSV was winning.

2. **Provenance and confidence are fields, not comments.** Every record carries
   `source` (free text: manual page, `.iom` path, URL) and `confidence` with a closed
   enum — CLDR's `draft=` reproduced: `verified | contributed | provisional | unverified`.
   This is what SMuFL, CLDR, iso-codes and QMK all do, and §2.6 shows why: any format whose
   comments survive a generator write (only TOML+tomlkit, reliably) is buying an advantage
   that decision 3 makes irrelevant.

3. **The generator never writes a hand-curated file.** Scrapers write to
   `build/proposals/*.json`; a human moves content into `data/`. Generated artifacts
   (`build/kitwarp_tables.h`, the interchange export) are committed and guarded by a
   `--check` mode. This is the tzdata law (`northamerica` is never re-serialised;
   `tzdata.zi` is), and the SMuFL law (`tools/generate.py --check`), and the KITWARP CI
   already has the slot for it (`python -m tools.export --check`).

4. **CI, modelled on SMuFL's `pages.yml`:**
   ```
   check-jsonschema --schemafile schema/pivot.schema.json  vocabulary/pivot.json
   check-jsonschema --schemafile schema/device.schema.json data/devices/**/*.json
   python -m tools.validate            # the checks a schema cannot express:
                                       #  - duplicate-key rejecting loader (QMK's hook)
                                       #  - every device row's pivot_id exists in the vocabulary
                                       #  - pivot ids unique; sort order canonical
                                       #  - IMMUTABILITY: no published pivot id changed meaning
                                       #    (SMuFL check_immutability.py) — the highest-value check,
                                       #    given the brief's warning that changing the vocabulary
                                       #    invalidates everything already collected
   python -m tools.format --check      # committed files == canonical formatter output
   python -m tools.codegen --check     # committed .h == generated .h
   python -m tools.export --check      # already in ci.yml
   ```
   `check-jsonschema` needs no new dependency: it is a thin CLI over `jsonschema>=4.21`,
   which `tools/requirements.txt` already pins; `python -m tools.validate` can call
   `jsonschema.Draft202012Validator` directly and skip the CLI entirely.

5. **Codegen: approach 1 of §4.** Python emits a single `.h` with per-axis dictionaries of
   `{uint32 offset, uint16 len}` into one `constexpr char kPool[]`, a 12-byte `Row` of
   small integer axis ids, and `kRows` **pre-sorted** so lookup is `std::lower_bound`.
   Measured: 344 KB `.rodata`, 3 relocations, 0 bytes of `.data.rel.ro`, `.init_array` = 8,
   no constructors, no allocation, 0.39 s compile, ~107 ns per binary-search lookup. Also
   emit `kSourceFile`/`kSourceLine` parallel arrays under `#ifndef NDEBUG` — systemd hwdb's
   `trie_value_entry2_f` shows the value of carrying provenance into the binary.

6. **Two things to schedule now, not later.** (a) Measure the header's compile time on MSVC
   before the table shape is frozen — GCC scales linearly to 135 k rows but MSVC is
   UNVERIFIED here and is a real risk for a Windows VST3. (b) Version the vocabulary file
   the way QMK versions `keycodes_0.0.*.hjson`, with `"!delete!"`-style tombstones for
   retired terms, so that "the vocabulary must be settled before device data is collected"
   becomes "the vocabulary is append-only and CI proves it" rather than a hope.

**Rejected, with reasons:** YAML (a new dependency, comment reattachment is best-effort,
block form has JSON's silent-merge hazard, and the `1.1`/`1.2` bool-and-octal coercion trap
is a real hazard for a file full of note numbers); JSON5/JSONC (its only advantage over JSON
is comments, and the `json5` library destroys them on any write — verified); pure CSV/TSV
(fixed columns versus 9–10 sparse axes; frictionless is a heavy dependency for benefits
that are 20 lines of Python in JSON); the TSV+TOML hybrid (two schema languages, two
validators, two parsers, two review idioms, to save ~2 MB of repository text that never
reaches the binary); SQLite (`Cannot merge binary files` is disqualifying for a
multi-contributor curated dataset, and no three-way merge driver exists); FlatBuffers /
Cap'n Proto / textproto as the *source* (14–25 % larger output, 4× the compile time, a
toolchain dependency, and far weaker validation than JSON Schema — all three are good
*derived* formats and bad *source* formats).

---

## 7. Strongest counter-argument

**TOML with `tomlkit` is the only option under which a scraper and a human can edit the same
file, and that workflow is worth more than everything JSON wins.**

The case, stated fairly:

`tomlkit` is not a serialiser, it is a concrete-syntax-tree round-tripper, and §2.3 proves
it: given a file a human actually typed — aligned `=` signs, single-quoted literal strings,
comments in their own columns — `tomlkit.dumps(tomlkit.parse(src))` returned it **byte for
byte**. Nothing else tested does that. `ruamel.yaml` was byte-exact only when the input
already matched its canonical style, and it misplaced a comment when it was not.
`json5`, `tomli_w` and `PyYAML` destroyed every comment.

That makes exactly one workflow possible, and it is the workflow this project will actually
want. A scraper reads a Roland manual and proposes 90 notes. A curator opens the file, and
above the three rows they are unsure about writes `# manual p.142 shows 22 for HH Edge but
the TD-30 factory kit sends 26 — check on hardware`. Six weeks later the scraper runs again
with an improved parser, updates 40 rows, and **the curator's notes are still there, still
attached to the right rows, in the same columns**. Under the recommendation, that note has
to be squeezed into a `source` string field, which means it must be decided in advance what
kinds of note the schema permits, and the free-text marginal annotation that is the actual
substance of curation work has nowhere to live. tzdb is 69 % comments for a reason: on a
dataset like this the reasoning *is* the deliverable, and it does not fit in a field.

`taplo` sharpens the case: its diagnostics are `file:line:col` with a caret under the
offending value, where `check-jsonschema` gives `$.notes[3].openness` and leaves the curator
to count array elements. For a hand-curated corpus, error locality is a daily cost. And
TOML's `[[notes]]` table arrays put the id first, so git's hunk-header heuristic recovers
most of the self-identifying-diff benefit for free (verified in §2.2). Precedent is not
against it either: the repo's own `tools/requirements.txt` already ships `tomli`, meaning
somebody has already thought TOML.

**Why it did not win.**

The counter-argument's premise is decision 3 — that the generator writes the hand file —
and that premise is what every precedent in §3 rejects. tzdata never re-serialises
`northamerica`; `zishrink.awk` writes `tzdata.zi` instead. SMuFL's generator writes
`metadata/`, never `data/`. CLDR's tooling writes locale XML and therefore CLDR moved
per-datum confidence out of comments and into a `draft=` attribute used 169,650 times.
iso-codes' validator rewrites its JSON and therefore its provenance is in
`official_name`/`common_name` fields. **The comment-preservation advantage is only
purchasable by adopting a workflow that four independent, decades-old curated databases
each decided against.** Once the generator writes only to `build/`, TOML and JSON preserve
comments equally well — which is to say, the question stops mattering.

Three further costs settle it:

- **Merge.** TOML's `[[notes]]` blocks reproduce the multi-line-record hazard. In the
  measured merge, resolving "take both" produced `tomllib.TOMLDecodeError: Cannot overwrite
  a value` — loud, and therefore much better than JSON's silent loss of a whole record, but
  still a manual redo of both curators' work. Line-oriented JSON and TSV both produced the
  correct 10 records from the naive resolution. On a repository expecting concurrent
  contributions per device, that is a recurring tax TOML cannot avoid without abandoning
  block form, at which point its comment advantage goes too.
- **Validation.** `taplo` 0.9.0 **silently ignores** `dependentRequired` and passes a file
  that `check-jsonschema` correctly rejects, while enforcing `type` and `enum` from the same
  schema — a false negative, not an error. The axes in `00-draft-axes.md` are exactly the
  kind that need conditional constraints (`openness` only meaningful with a hi-hat
  instrument; `zone` required when `articulation` is a zone-bearing technique), and those
  are `dependentRequired`/`if-then`/`allOf` keywords. Using TOML means either accepting
  taplo's silence or running `check-jsonschema` on the TOML anyway — in which case the
  pretty caret diagnostics are gone and TOML has lost its second advantage too.
- **Dependency.** `tomlkit` is a real addition to a file whose own comment says anything
  added must earn its place in an ADR. JSON is stdlib.

The honest residue: **the recommendation does give up free-form marginal annotation, and
that is a genuine loss.** The mitigation is to make the `source` field generous — a free
string with no length or content constraint, plus an optional `notes` array of strings — and
to accept that the *narrative* reasoning (why an axis exists, why a device is weird) belongs
in `docs/` next to the ADRs, where tzdb's comments would also live if tzdb had a docs
directory. If, after six months, curators are routinely fighting the schema to record what
they know, that is the signal to revisit this decision — and the migration is a
100-line `json → tomlkit` script, because the axis model, not the file format, is the thing
that is expensive to change.

---

## 8. Provenance

Everything below was cloned and read on 2026-09-06 unless noted. Clone root:
`scratch:repos/`

| Source | URL | Paths read | Licence |
|---|---|---|---|
| tzdata / tzcode | `https://github.com/eggert/tz` | `africa antarctica asia australasia europe northamerica southamerica etcetera backward backzone factory`, `Makefile`, `checktab.awk`, `checklinks.awk`, `ziguard.awk`, `zishrink.awk`, `zic.c`, `zone1970.tab` | data files: **public domain** (stated in each file); code: BSD-style (`LICENSE`) |
| pci.ids | `https://github.com/pciutils/pciids` | `pci.ids`, 60 commits of history | **GPL-2.0-or-later OR BSD-3-Clause** (stated in the file header, lines 13–14) |
| pciutils | `https://github.com/pciutils/pciutils` | `lib/names-parse.c`, `lib/names-cache.c`, `Makefile`, `update-pciids.sh` | GPL-2.0-or-later (`COPYING`) |
| hwdata | `https://github.com/vcrhonek/hwdata` | `usb.ids`, `pci.ids`, `pnp.ids`, `Makefile`, `check-pci-ids.py`, `check-usb-ids.sh`, `AUTOMATION.md` | `LICENSE`: "licenced under 2 different licenses — 1) GNU GPL v2 or later …" |
| systemd hwdb | `https://github.com/systemd/systemd` | `hwdb.d/*.hwdb`, `hwdb.d/README`, `src/libsystemd/sd-hwdb/hwdb-internal.h` | LGPL-2.1-or-later (SPDX headers) |
| CLDR | `https://github.com/unicode-org/cldr` | `common/main/*.xml` (1,148 files), `common/dtd/ldml.dtd` | **Unicode-3.0** (SPDX headers) |
| iso-codes | `https://salsa.debian.org/iso-codes-team/iso-codes` | `data/*.json`, `data/schema-*.json`, `scripts/validate_json_data.py`, `meson.build`, `CHANGELOG.md` | LGPL-2.1-or-later (`LICENSES/`, SPDX headers) |
| SMuFL | `https://github.com/w3c/smufl` | `metadata/glyphnames.json`, `metadata/ranges.json`, `metadata/schema/*.json`, `metadata/schema/check_consistency.py`, `data/ranges/*.yaml`, `data/ranges/manifest.yaml`, `.github/workflows/pages.yml`, `w3c.json` | **no `LICENSE` file in the repo**; `w3c.json` declares `"repo-type": "cg-report"` (W3C Community Group report) — **UNVERIFIED**, check before reusing text |
| QMK | `https://github.com/qmk/qmk_firmware` | `data/schemas/*.jsonschema`, `data/mappings/*.hjson`, `data/constants/keycodes/*.hjson`, `lib/python/qmk/json_schema.py`, `lib/python/qmk/cli/generate/keycodes.py` | GPL-2.0 (`LICENSE`) |
| ALSA UCM | `https://github.com/alsa-project/alsa-ucm-conf` | `ucm2/**/*.conf` | BSD-3-Clause (`LICENSE`) |
| Ardour MIDNAM | `https://github.com/Ardour/ardour` | `share/patchfiles/README`, `share/patchfiles/Alesis_DM5.midnam` (475 files, 23 MB) | Ardour: GPL-2.0-or-later. Individual `.midnam` files carry their own provenance, e.g. `<Author>Mark of the Unicorn - converted from FreeMIDI</Author>` — **licence of the data unclear, verify per file before reuse** |
| Drum-MIDI-Converter | `https://github.com/lotkey/Drum-MIDI-Converter` | `src-cpp/mappings/tree/*.txt`, `src-cpp/mappings/SampleTree/Keys.hpp`, `src-cpp/mappings/Mapping/Mappings/**/*.cpp`, `update-mappings/update.cpp`, `src-python/conversions.lkcmap` | **GPL-3.0** (`LICENSE`) |
| drum-remap | `https://github.com/marty-615/drum-remap` | `maps/*.json` (10 files) | no `LICENSE` file found — **UNVERIFIED** |
| ZSA oryx-keymaps | `https://github.com/zsa/oryx-keymaps` | — | **not obtainable**: clone returned `could not read Username for 'https://github.com'` |
| Linux device tables | — | not cloned | **UNVERIFIED** — §3.11 stated from knowledge |

Tool versions and maintenance dates, from `git log -1` on each upstream repository,
2026-09-06: `tamasfe/taplo` 2026-07-28 (CLI 0.10.0; the 0.9.0 binary tested here came from
npm `@taplo/cli`); `python-jsonschema/check-jsonschema` 2026-08-17 (0.38.0);
`ajv-validator/ajv` 2026-04-24 (v8.20.0); `frictionlessdata/frictionless-py` 2026-08-27
(5.19.0 installed); `google/flatbuffers` 2026-08-11 (system `flatc` 2.0.8 used here);
`capnproto/capnproto` 2026-09-03 (system `capnp` 1.0.1 used here);
`python-poetry/tomlkit` 2026-08-18 (0.15.1); `dpranke/pyjson5` 2026-06-24;
`hjson/hjson-py` 2025-11-02 (documentation-only commit); `tombi-toml/tombi` 2026-09-06
(v1.5.2, not tested).

Measurement environment: Linux 6.18.44, x86-64; `g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1)`;
Python 3.11.15; Node v22.22.2. All C++ figures are `-O2 -std=c++20`, default PIE. Compile
wall-times are single runs on a shared container and should be read as ratios, not
absolutes; the section sizes, relocation counts and record counts are exact.
