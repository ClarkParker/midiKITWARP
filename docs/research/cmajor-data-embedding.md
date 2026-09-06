# Research: what Cmajor offers for embedding and moving data

Source-based answers, checked against the official repository
(`github.com/cmajor-lang/cmajor`, commit `4ba0924`, 2026-09-03). Paths are relative to
that checkout. Measured numbers live in `docs/evidence/cmajor-embedding-probes.md`.

## 1. `external` variables — VERIFIED, but not usable in Amorph

- Syntax `external <type> <name>;`, any state scope, implicitly const
  (`docs/Cmaj Language Guide.md:805-819`, `modules/compiler/src/passes/cmaj_ExternalResolver.h:69-84`).
- All types work: arrays, vectors, structs, nested structs, strings; an unsized
  `external int[] x;` takes its size from the JSON
  (`modules/compiler/src/AST/cmaj_AST_Classes_Constants.h:838-889, 491-498`).
- Supplied only through the manifest's `externals` object — **inline JSON literals are
  accepted**, no data file needed (`include/cmajor/helpers/cmaj_PatchManifest.h:438-453`;
  shipped proof: `tests/integration_tests/patches/External/`). Or in-source
  `[[ default: int[](1,2,3) ]]` (`cmaj_AST_Externals.h:92-102`).
- Frozen at link time: `cmaj_AST_Externals.h:105-125` turns the variable into a constant
  before `engine.link()`. **Not runtime-writable by any mechanism.**
- Amorph shows the manifest read-only → the route is closed for the prototype, open for
  the JUCE phase.

## 2. JS view → DSP arrays/structs at runtime — VERIFIED YES

- `sendEventOrValue(endpointID, value)` coerces objects/arrays to the endpoint type
  (`javascript/cmaj_api/cmaj-patch-connection.js:85-93`;
  `include/cmajor/helpers/cmaj_EndpointTypeCoercion.h:328-386` — arrays element-wise
  with zero-fill, structs by member name).
- Official example doing exactly this: `examples/patches/PatchWorker/PatchWorker.cmajor:13-33`
  declares `input event AudioDataChunk sampleData;` with `struct { float[512] frames; … }`
  and `worker.js:34-49` pushes chunks with a 1000 ms retry timeout.
- Constraints: **no slices on top-level endpoints** (`cmaj_Validator.h:1001-1033`) —
  use `int32[128]` or a struct of fixed arrays; **≈64 KB per event** hard limit
  (`cmaj_Patch.h:351-353` FIFO size, `choc_VariableSizeFIFO.h:171-206` single push must
  fit) → chunk anything larger.
- Native WebView path is JSON-serialised (`choc_WebView.h:1910/1949`); the exported
  WASM path packs directly and generates one JS statement per scalar element
  (`cmaj_JavascriptClassGenerator.h:1063-1097`) — another reason to keep events small.

## 3. Large const initialisers — VERIFIED

- `maxInitialiserListLength = 1024 * 64` = **65,536 elements per list**, nesting allowed;
  array size limit `int32` max (`modules/compiler/src/AST/cmaj_AST_Utilities.h:20-27`,
  enforced in `cmaj_Parser.h:1568, 1934`).
- No source-file size limit found (lexer only limits identifiers to 256 chars).
- Precedent in the repo: `examples/patches/GuitarLSTM/GuitarLSTM.cmajor` — 249 KB, 10,669
  float literals, lines up to 118 K chars; `examples/patches/Pro54/Pro54.cmajor` 145 KB.

## 4. Decompression / base64 / strings in the stdlib — NOT FOUND (none)

- Zero hits for base64/inflate/zlib/gzip/deflate in `standard_library/` and the compiler.
- Strings are read-only literal tokens, no concatenation or mutation
  (`docs/Cmaj Language Guide.md:465`).
- `std::` namespaces: `intrinsics, audio_data, convolution, envelopes, filters (tpt,
  dcblocker, butterworth, crossover, simper), frequency, smoothing, levels, pan_law,
  matrix, midi, mixers, noise, notes, oscillators (waveshape), random, timeline, voices`.
  Array helpers: `sum, product, read, readLinearInterpolated, anyTrue, allTrue, allEqual,
  swap`, plus `.size`, `.at()`.

## 5. Patch workers and source transformers — VERIFIED, not available in Amorph

- `"worker": "x.js"` in the manifest starts a QuickJS or hidden-WebView context with the
  full `PatchConnection` API plus `setTimeout`, `console`, `readResource`
  (`include/cmajor/helpers/cmaj_PatchWorker_QuickJS.h:33-207`, `cmaj_Patch.h:741-820`).
  It **cannot** set externals (no such client message, `cmaj_Patch.h:2771-2884`; started
  only after link, `cmaj_Patch.h:2624`) but **can** push endpoint events.
- `"sourceTransformer": "x.js"` rewrites source text before compilation
  (`cmaj_Patch.h:860-923`; example `examples/patches/FaustFM/`). JIT hosts only.
- Both are extra files → out for the Amorph prototype.

## 6. Manifest fields — VERIFIED (`cmaj_PatchManifest.h:296-327`)

Required: `CmajorVersion` (=1), `ID` (≥4 chars), `name` (1–128), `version` (1–24).
Optional: `description, category, manufacturer, mainProcessor, isInstrument, source
(string|array), view (object|array: src/width/height/resizable), worker,
sourceTransformer, resources, externals`; plus `icon, URL, plugin{pluginCode,
manufacturerCode, thumbnail}` read by exporters. `getStrippedManifest()` removes
`externals` before the manifest is sent to views.

## Bottom line

Three verified routes with one DSP file + one UI file: (1) generated `const` tables in
the `.cmajor`, (2) a compressed blob in the `.js` inflated by the WebView, (3) chunked
struct events from the view for runtime changes. Manifest `externals`, workers and
transformers are verified in Cmajor but unreachable in Amorph. In-DSP decompression does
not exist and is not needed. See ADR-0002 for the decision.
