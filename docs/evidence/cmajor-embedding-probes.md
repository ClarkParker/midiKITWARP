# Evidence: embedding data in a Cmajor monolith — compiler probes

Measured on 2026-09-06 with `cmaj 1.0.3175` (Linux x64, fetched via
`Amorph_DEV_KIt/tools/get_cmaj.sh`), in a 4-thread container. Regenerate everything with

```
python3 tools/probes/cmajor_embed_probe.py --cmaj "$(../Amorph_DEV_KIt/tools/get_cmaj.sh)"
```

Two measurements per probe: `cmaj generate --target=cpp` (parse + type-check + codegen,
no JIT) and `cmaj test` with a `## testProcessor()` block (LLVM JIT, the engine Amorph
uses for its COMPILE button). Times are wall clock, single run, ±0.05 s.

## 1. Const tables in the source: size sweep

Table shape: `const int32[N] layoutTable = ( … );` in a namespace, index =
`layout * 128 + note`, read by a processor on every note-on.

| Layouts | Entries | Encoding | Source size | `generate` | Result |
|---:|---:|---|---:|---:|---|
| 200 | 25,600 | plain `int32` | 126 KB | 0.20 s | OK |
| 300 | 38,400 | plain `int32` | 187 KB | 0.25 s | OK |
| 500 | 64,000 | plain `int32` | 310 KB | 0.24 s | OK |
| 512 | **65,536** | plain `int32` | 317 KB | 0.23 s | OK |
| 520 | 66,560 | plain `int32` | 322 KB | — | **error: Initialiser list exceeds max length limit** |
| 200 | 25,600 | 4 × `int16` per `int64` | 134 KB | 0.11 s | OK |
| 1000 | 128,000 | 4 × `int16` per `int64` | 655 KB | 0.28 s | OK |
| 2000 | 256,000 | 4 × `int16` per `int64` | 1.3 MB | 0.50 s | OK |

The ceiling is **65,536 elements per initialiser list**, matching
`maxInitialiserListLength = 1024 * 64` in `modules/compiler/src/AST/cmaj_AST_Utilities.h`.
No source-file size limit was hit. Packing four 16-bit values per `int64` literal lifts
the ceiling to 262,144 entries per list at the cost of a shift-and-mask on read; chunking
into several arrays works too.

JIT cost of the table alone (processor with the 25,600-entry table and no other large
state): **0.13 s**. Data volume is not the problem.

## 2. State arrays: shape matters, size does not

Same trivial processor, one state array written and read on every note-on:

| Declaration | Entries | `cmaj test` (JIT) |
|---|---:|---:|
| `int32[4096] tbl;` | 4,096 | 0.1 s |
| `int32[12288] tbl;` | 12,288 | 0.1 s |
| `int32[32768] tbl;` | 32,768 | **0.2 s** |
| `int32[16,16,128] tbl;` | 32,768 | **7.5 s** |
| `int8[32768] tbl;` | 32,768 | 0.1 s, but the functional check **failed** — not investigated |

Multi-dimensional arrays are what the LLVM backend chokes on; a flat array with manual
index arithmetic is thirty times faster to compile at the same size.

## 3. The full mapping processor, four ways

Processor: 200-layout const table, 16 × 16 × 128 output table, 16 × 128 note-off
tracking, `rebuild()` on parameter change (source → pivot → inverse target → table),
channel-preserving `createMessage`. Same functional test in every case (§4).

| Variant | State layout | Init | JIT | Test |
|---|---|---|---:|---|
| V1 | `int32[16,16,128]` + `int32[16,128]` ×2 | nested init loops to −1 | **75 s** | pass |
| V2 | same, init loops with runtime-variable bounds | loops | 72 s | pass |
| V3 | same 3-D arrays | no init loops | 15.8 s | pass |
| V4 | **flat** `int32[32768]` + `int32[2048]` ×2, value stored as `note + 1` (0 = none) | none | **0.20 s** | pass |
| V4 + 256,000-entry packed table | flat | none | 0.25 s | pass |

Rules that fall out of this, now binding for the DSP:

1. **Flat arrays only** for anything large; index with `(a * B + b) * C + c`.
2. **No initialisation loops over large arrays.** Encode so that zero means "unmapped /
   nothing held" (store `note + 1`) and rely on Cmajor's zero-initialised state.
3. Const data tables may be as large as needed under the 65,536-per-list limit; they are
   free at JIT time.
4. `int32` for state arrays until the `int8` failure is understood.

## 4. Functional test (passes in V1–V4)

`## testProcessor()` graph: generator → mapper → checker. Source layout 0, target layout 1,
note 21 maps to 107; target layout 2 maps it to 19.

1. note-on ch 3 note 21 vel 100 → expect note-on ch 3 note **107** vel 100
2. switch target-layout parameter to 2 while the note is held
3. note-off ch 3 note 21 → expect note-off for **107** (the note actually sent, not the
   new mapping) — the note-off tracking rule from `docs/03-architecture.md`
4. note-on ch 3 note 21 vel 90 → expect **19** vel 90; note-off → **19**

All four events arrived in order with channel 3 preserved (`0x90 | ch` on emit,
`getChannel0to15()` on receive). Host-side channel preservation in Amorph is a separate
question (host test H2).

## 5. UI-side blob

Synthetic export: 200 layouts × 128 notes at ~55 % occupancy with a 320-entry
articulation vocabulary, names, vendor, kind, channel and a provenance record each.

| Form | Size |
|---|---:|
| JSON, minified | 161.7 KB |
| deflate-raw (zlib level 9) | 44.7 KB |
| base64 of the deflate stream | 59.7 KB (0.37 × JSON) |

Decoding in the UI needs no library: `atob` → `Uint8Array` →
`new DecompressionStream('deflate-raw')` → `Response.text()` → `JSON.parse`.
Availability of `DecompressionStream` inside Amorph's WebView is host test H4; the
fallback is either a ~1 KB inlined inflate or shipping the JSON uncompressed.

## What was not measured

- Amorph's own compile path (the IDE may use a different LLVM optimisation level).
- Whether Amorph forwards a struct-typed `input event` from `sendEventOrValue`
  unchanged (verified in the Cmajor source, not in the host) — host test H3.
- The `int8` state-array failure.
