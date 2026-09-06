# Resume here

Paused 2026-09-06. This file is the entry point for picking the work back up.

## Where the work stands

**Phase 1 (pivot vocabulary) and Phase 2 (storage format) are drafted and pushed.**
Four ADRs, all status **Proposed**, nothing signed off:

| ADR | Decision |
|---|---|
| 0001 | The pivot is a symbolic, factored, versioned vocabulary — not a note number, not GM |
| 0002 | Line-oriented JSON as source of truth, compiled to a constexpr table |
| 0003 | Opaque never-reused integer ids, immutable slugs, four lifecycle states |
| 0004 | Provenance mandatory, licence status machine-checked |

Vocabulary v0.1.0 is minted: 155 terms, 13 axes, 132 axis values, drum kit only.
Percussion, orchestral, electronic and utility families are reserved and unminted.
`tools/validate`, `tools/format` and `tools/iom` all pass.

**Round 2 (the terminology sweep) is complete.** Twelve workers, twelve dossiers,
14,129 lines from primary sources, all merged onto `work/round2-reconciliation`.

**The reconciliation is half done.** Three of four extracts are in this directory;
the fourth and the synthesis did not run.

## Branches

```
claude/kitwarp-pivot-vocab-data-w56ld3   the vocabulary, ADRs, tooling, round-1 research
work/round2-reconciliation               all twelve round-2 dossiers merged, plus this
work/bucket-01-rudiments-stroke-technique … work/bucket-12-german-french-italian
```

Nothing has been merged toward `main`. That is the owner's call.

## The first thing to do on resume

Finish the reconciliation. The workflow script is at
`kitwarp-round2-reconciliation-*.js` under the session's workflow scripts directory; if it
is gone, re-author it from the shape below. What remains:

1. **extract-D** — read `07-world-percussion.md`, `09-library-primary-manuals.md` and
   `11-acoustics-and-timbre.md` and produce `extract-D.md` in the same shape as A, B and C.
2. **Synthesis** — read all four extracts, then produce
   `docs/research/round2/00-RECONCILIATION.md` with five parts: the concordance sorted by
   attestation count, false friends and collisions, terms that fit no axis grouped by the
   missing thing, the diff against v0.1 (ADD / REMOVE / RE-AXIS / RENAME-by-alias, each
   marked MAJOR or MINOR under ADR-0003), and the deduplicated owner decisions.
3. Then update `docs/research/README.md` with a round-2 section. No worker touched it, by
   design — twelve workers editing one index would conflict on every push.

Count attestations by **independent tradition**, not by document. Two dossiers quoting one
manual is one attestation. Note in particular that Peinkofer/Tannigel was translated by
Kurt and Else Stone, so Stone 1980 and Peinkofer/Tannigel 1976 are one lineage and their
agreement is not corroboration.

`late-findings-to-verify.md` in this directory lists what two workers pushed *after* the
first reconciliation launch, including one bucket reversing another's finding. Every item
in it must appear in the final report.

## Then: the owner's decisions

`needs_owner.md` in this directory holds all 29 raw items as the workers wrote them. They
were bundled and put to the owner on 2026-09-06, deduplicated and ordered by how expensive
each is to reverse. **No answers have been received.** Until they are, CLAUDE.md rule 5
holds: nothing is collected against an unapproved vocabulary.

The four that block everything else are the undirected exclusion class, minting `choke` as
a technique, the `heel`/`toe`/`thumb` collision with hand percussion, and the
`site=bow` versus `implement=bow` collision.

## Environment facts worth not rediscovering

- `git clone --depth 1` works for public GitHub repositories; `curl` to github.com is 403.
- WebSearch has a **separate quota per worker**, exhausted at 200; the supervisor session
  has its own. Workers should put queries in `questions` and the supervisor runs them.
- `web.archive.org` is **intermittent, not blocked** — retry three to five times. A bare
  HEAD returns a misleading bodyless 302. The availability API is reliable.
- `static.roland.com` is an S3 bucket with `ListBucket` denied, so a non-existent key
  answers `403 AccessDenied` rather than `404`. Guessed filenames always look blocked.
  Read the real filename off the product's owners-manuals page.
- Vendor Zendesk help centres 403 a browser but serve the same PDFs from their public JSON
  API at `/articles/<id>/attachments.json`.
- AMEI publishes the English MMA Recommended Practice PDFs free; midi.org charges.
- Hosts denied by egress policy (502 on CONNECT): instruments.ircam.fr, lclsds.loc.gov,
  vocabs.dariah.eu, duckduckgo.com, howtowriteforpercussion.com, pearleurope.com,
  www.drummica.com.
- Wikipedia's API rate-limits at 429 on the third call within a minute.

## What has NOT been done, deliberately

No device data has been collected. Phase 3 does not start until the vocabulary is signed
off, because changing it afterwards invalidates everything collected against it.
