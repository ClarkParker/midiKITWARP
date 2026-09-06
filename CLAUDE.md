# CLAUDE.md — house rules for this repository

Applies to the supervisor and to every worker.

## What this repository is

Data, not plugin code. Vocabulary, device layouts, schemas, parsers, validator, exporters,
and the reasoning behind them. Plugin code, VST3, Cmajor, GUI and host questions belong to
a different repository and are out of scope here — if a task drifts toward them, stop and
say so rather than building it.

## Scope check before starting anything

State in one line what you are about to change and why it belongs in this repository. If
the answer needs more than one line, the task is too big and should be split.

## The rules that are not negotiable

1. **No number without a source.** Every assertion carries a provenance record: source,
   method, locator, date, observer, confidence, licence verdict. A documented gap beats a
   guessed note. See `docs/adr/0004-provenance-and-licensing.md`.
2. **Primary sources only.** Curated third-party collections are worklists that say where
   to look; they are never the shipped source. Groove Monkee is `forbidden` by contract.
   GPL collections are `rederive-only`. Unknown licence means all rights reserved.
3. **Identifiers are forever.** Pivot ids and slugs are never reused, never renamed, never
   removed. Correct a slug with a `correction` alias. See
   `docs/adr/0003-identifiers-and-registry.md`.
4. **The generator never writes a hand-edited file.** Scrapers write to `build/proposals/`;
   a human moves content into `data/`. See `docs/adr/0002-storage-format-and-codegen.md`.
5. **Nothing is collected against an unapproved vocabulary.** Changing the vocabulary after
   collection invalidates everything collected.

## Before every commit

```bash
python -m tools.validate
python -m tools.format --check
python -m tools.iom.roundtrip_check data/legacy-iom
```

Commit only what passes. Commit verified intermediate states immediately rather than
batching — a worker that dies mid-task should leave usable work behind.

## Commit messages

Say what changed and why the alternative lost. No model identifiers, no tool names in the
message body. Body wrapped at 78 columns.

## Never merge to `main` without the owner's explicit go

Workers push their own branch and stop there.

## Writing

Repository content is English. Conversation with the owner is German. Facts over adjectives;
every claim carries a locator; anything uncertain is marked UNVERIFIED rather than smoothed
over.
