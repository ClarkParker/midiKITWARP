# ADR-0002 — Data embedding in the two monoliths

**Status:** Accepted (prototype), revisit after host test H1 (see `CHECKLIST.md`)
**Date:** 2026-09-06
**Supersedes:** —
**Superseded by:** —

## Context

The Amorph prototype consists of exactly **one Cmajor DSP file, one JavaScript UI file
and a manifest that the Amorph IDE shows read-only** (`Amorph_DEV_KIt/docs/13_AMORPH_IDE.md`,
"Manifest (read-only)"). No side-loaded data: no `resources`, no `externals` block, no
`worker` or `sourceTransformer` script — all of those are manifest features
(`docs/research/cmajor-data-embedding.md`, §5–6).

The data the plugin needs, measured on a synthetic set of 200 layouts × 128 notes at
~55 % occupancy, a 320-entry articulation vocabulary, names and provenance
(`docs/evidence/cmajor-embedding-probes.md`):

| Payload | Size |
|---|---:|
| Numeric layout tables only (200 × 128 × int16) | 50 KB binary, ~126 KB as source literals |
| Full JSON (tables + vocabulary + names + provenance) | 162 KB |
| Same JSON, deflate-raw | 45 KB |
| Same, base64-encoded for embedding in `.js` | 60 KB |

Cmajor facts, verified against the compiler source and against `cmaj 1.0.3175`:

- An initialiser list holds at most **65,536 elements** (`maxInitialiserListLength`;
  probe: 65,536 compiles, 66,560 fails). Array size itself is limited only by `int32`.
- Cmajor has **no strings beyond literals, no base64, no decompression** — nothing in
  `std::` handles bytes or text. Data must arrive already decoded.
- Const tables are cheap to compile: 25,600 `int32` entries JIT in 0.13 s; 256,000
  entries packed four-per-`int64` JIT in well under a second.
- The **JS view can push arrays/structs** into a DSP `input event` of a fixed-size
  struct type; one event must stay under ~64 KB (event FIFO size), slices are not
  allowed on top-level endpoints. This is the officially demonstrated `PatchWorker`
  pattern.
- `external` variables can only be supplied by the manifest and are frozen at link
  time — not writable from JS at runtime. Not available in Amorph anyway.

WebView facts: `DecompressionStream('deflate-raw')` is a native browser API in
Chromium ≥ 80 (WebView2) and WebKit ≥ 16.4 (WKWebView on macOS 13.3+, WebKitGTK 2.40+).
No library is needed to inflate a blob in the UI. **[unverified in Amorph — host test H4]**

The plugin must behave correctly when the host restores a project **without opening
the UI**. Whether Amorph instantiates the view at load regardless of window state is
unknown **[host test H1]**.

## Decision

We embed the **numeric layout tables as generated `const` arrays in the DSP source**
(chunked below 65,536 entries per list, or packed four `int16` per `int64`), and the
**full metadata (vocabulary, names, provenance, articulation semantics) as one
deflate+base64 blob at the end of the UI source**, inflated at startup with the
native `DecompressionStream`. Both embeddings are emitted by **one generator from the
same curated export**, so the DSP can build every routing table headlessly from
parameters, and the UI only adds names and editing. Maps created at runtime (MIDI
learn, user layouts) travel UI → DSP as chunked struct events and persist in stored
state.

## Criteria and how the options score

| Criterion | A · DSP const tables + UI blob (chosen) | B · manifest `externals` JSON | C · data only in UI, push at load | D · worker / sourceTransformer | E · uncompressed JSON in UI |
|---|---|---|---|---|---|
| No extra files in Amorph | ✅ | ❌ manifest read-only | ✅ | ❌ extra script file | ✅ |
| Works when the UI is never opened | ✅ | ✅ | ❌ (unless H1 says the view always exists) | ✅ | ❌ |
| Compile / load cost | 0.1–0.5 s | 0 s | 0 s + 64 events per open | 0 s | 0 s |
| Runtime decode in DSP needed | no | no | no | no | no |
| Size of code the Amorph AI panel sees | +126 KB DSP, +60 KB UI | +0 | +60 KB UI | +0 | +162 KB UI |
| One copy of the data | ❌ two generated views of one source | ✅ | ✅ | ✅ | ✅ |
| Portable to the later JUCE build | ✅ (tables become C++ arrays) | ✅ | ⚠️ needs a headless path | ❌ Cmajor-JIT-only | ⚠️ |
| Verified today | ✅ compiler probes | ✅ source, ❌ Amorph | ✅ source, ❌ Amorph bridge | ✅ source | ✅ |

B and D are technically the cleanest and are ruled out purely by the Amorph
single-file constraint — they come back on the table in the JUCE phase. C is the
strongest live competitor (see below).

## Consequences

- A generator (`tools/build_monolith.py`) becomes a first-class build step; the
  hand-written DSP and UI live in `src/` and are never edited in `dist/`.
- Layout IDs must be **stable and append-only** (the parameter values that select a
  layout are numbers saved in DAW projects). The generator emits an `layoutOffset[id]`
  indirection so table order can change without breaking presets.
- The DSP owns the mapping maths (pivot → inverse → fallback chain). The UI reproduces
  it only for display. Both are tested against the same fixtures.
- The DSP source carries ~125 KB of numbers. This is well inside the compiler's comfort
  zone but inflates whatever the Amorph AI panel reads — keep the table in a clearly
  delimited trailing namespace so it can be stripped for prompts.
- Revisit after H1: if Amorph always instantiates the view, option C becomes viable
  and would remove the duplicate; the generator would then emit only the UI blob.

## Strongest counter-argument

"Keep the data in one place — the UI — and push the finished 16×16×128 table into the
DSP whenever the view starts. The DSP stays dumb, the data exists once, and the push
is only 64 events of 512 bytes." This is simpler and fully verified at the Cmajor
level. It lost because a plugin that produces wrong notes until its window is opened
is a correctness bug in every DAW project reload, and Amorph's behaviour there is not
known. If H1 shows the view is instantiated unconditionally, this ADR is superseded.
