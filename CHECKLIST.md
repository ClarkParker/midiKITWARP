# midiKITWARP — work list

Shared between the owner and every Claude session. Add tasks, tick them, never delete
history — a dropped task keeps its line with `[-]` and a reason.

`[ ]` open · `[~]` in progress · `[x]` done · `[-]` dropped · **H** = host test in Amorph
(owner's machine) · **P** = data pipeline (research branch `claude/kitwarp-pivot-vocab-data-w56ld3`)

## 0. Decisions

- [x] Pivot vocabulary instead of note-number pivot — `docs/adr/0001` (research branch), evidence in `docs/evidence/note-number-pivot-loss.md`
- [x] Data embedding in the two monoliths — `docs/adr/0002-data-embedding-in-the-monolith.md`
- [x] Flat arrays / zero-init encoding in the DSP — `docs/evidence/cmajor-embedding-probes.md` §2–3
- [ ] Revisit ADR-0002 after H1 (stored state vs parameters for module settings)
- [x] Parameter naming: strictly sequential `param1..paramN` (Amorph contract; descriptive IDs are invalid for the host)
- [ ] Parameter split within the **128-slot** budget: what restores headlessly (parameters) vs stored state — after H1
- [ ] Licence of the plugin itself (decides which reference code may be ported — `docs/research/midi-fx-prior-art.md` §4)

## 1. Host tests in Amorph (H — owner)

Five-minute patches each; H2 and H3 gate the core. Record results in
`docs/evidence/amorph-host-tests.md` (to be created with the first result). Paper answers
from the official contract are in `docs/research/amorph-host-contract-notes.md` §4.

- [ ] H0 Which Amorph build is installed — v0.99 (copy-paste only) or v1 beta (*Settings → Connections* present → MCP)? Decides whether a local Claude Code session can run H2–H9 over MCP.
- [ ] H1 view instantiated on project load with the window closed?
- [~] H2 MIDI channel preserved into `midiIn` and out of `midiOut` — UI hook exposes the channel nibble (`s & 0x0F`); `midiOut` side still unproven
- [ ] H3 struct event (`int32[128]` fields) from `sendEventOrValue` reaches a non-parameter `input event`
- [ ] H4 `DecompressionStream('deflate-raw')` available in the WebView (mac / win / linux)
- [ ] H5 `processor.latency` honoured (look-ahead bus)
- [ ] H6 CC and pitch-bend pass through `midiOut` to a downstream instrument
- [~] H7 `transportIn`: slot order documented (play, bpm, num, den, ppq, barStart, type `float`) — verify the buffer-size audit with our scheduler
- [ ] H8 runtime loads a ~200 KB UI file (the 8000-character rule is for LLM output)
- [ ] H9 Amorph lint accepts the generated DSP (big `const` tables, `int64` literals, chunked arrays, `% max(1, n)` guards)
- [ ] Amorph compile time for a DSP with the 130 KB table (expect < 1 s per probes)

## 2. Data pipeline (P — research branch)

- [ ] `tools.export` output format agreed with the plugin side: layouts with stable IDs, pivot IDs, vocabulary with parent links (fallback chain), names, provenance
- [ ] Stable, append-only layout ID policy written down in the data repo
- [ ] Vocabulary parent/fallback relation exported (needed by the DSP rebuild)
- [ ] First wave of layouts (inventory `docs/05-inventory.md`, "first wave")
- [ ] Fix CI on this branch: `tools.validate` / `tools.export` referenced in `.github/workflows/ci.yml` do not exist here yet (merge from the research branch or guard the steps)

## 3. DSP core (Cmajor)

- [x] Compiler probes: table sizes, initialiser limit, array shapes, functional mapping test — `tools/probes/cmajor_embed_probe.py`
- [ ] Scaffold with `Amorph_DEV_KIt/tools/new_plugin.py --type midi`, then split into `src/dsp/`
- [ ] Generated `namespace kwdata` (tables, `layoutOffset[id]`, vocabulary parents)
- [ ] Generator emits the Amorph lint shape: endpoints-first block, `float(processor.period)`, non-zero divisors, typed locals, no `let`, `transportIn` as `float` with barStart (`docs/research/amorph-host-contract-notes.md` §2)
- [ ] Rebuild: `src → pivot → tgt⁻¹` + fallback chain into the flat `outNote` table
- [ ] Routing matrix 16 × 16 with merge + refcounted note-off tracking
- [ ] Scheduler ring in `main()` (frame-stamped pending events), all-notes-off on stop/panic/rebuild
- [ ] Shared look-ahead + `processor.latency`
- [ ] Take ID + position-hash random (§3.6 of the prior-art doc)
- [ ] Input FX v1: Filter, Velocity (curve + comp/exp), Humanize (timing / velocity / length, distributions, colour ρ)
- [ ] Output FX v1: Target velocity, Choke groups, Transpose / channel
- [ ] Struct-event row push from the UI (`SlotRow`), chunked ≤ 64 KB
- [ ] `cmaj test` suite in `tests/cmajor/` for every rule above; CI compiles with the kit's `get_cmaj.sh`
- [ ] Investigate the `int8` state-array probe failure (or keep `int32`)

## 4. UI (Web Component)

- [ ] Kit recipe `07_SCALING.md` adopted 1:1 and diffed line by line (kit rule 8) — reconcile with the official `:host` 100 % rule and the no-`ResizeObserver` rule
- [ ] `data-param` wrappers per parameter (official contract), `// END_AMORPH_UI` marker, one `HTMLElement` subclass
- [ ] Primitives in `src/ui/`: knob, toggle, select, breakpoint curve, matrix cell, module card, meter
- [ ] Design tokens + accent gradient (concept §6); dark theme only
- [ ] Matrix view (Canvas) with activity lamps from `__amorphProcessMidi` / `__amorphProcessMidiOut`
- [ ] Input rail, output rail, module drawer
- [ ] Map view: source → pivot → target with names, unmapped list, MIDI learn, audition
- [ ] Monitor view: event list, dead-key meter, map coverage %
- [ ] Blob loader: base64 → `DecompressionStream` → JSON, with uncompressed fallback until H4 is known
- [ ] Stored state: slot config + deep module settings, echo-loop protection on every control
- [ ] Passes `ui_lint.py`, `check_sync.py`, `preflight.py` from the kit

## 5. Build & tooling

- [ ] `tools/build_monolith.py`: data export + `src/dsp` + `src/ui` → `dist/`; data blocks last and delimited
- [ ] `tools/pack_ui_data.py` (deflate-raw + base64) and the DSP table emitter (≤ 65,536 per list or int64-packed)
- [ ] CI: preflight + `cmaj test` + build
- [ ] Pre-commit hook from the kit (`tools/hooks/install.sh`)

## 6. Kit maintenance (Amorph_DEV_KIt — separate repo)

- [ ] Reconcile the kit with `amorph-for-agents` (2026-09): parameter naming, `transportIn` type + barStart slot, `data-param`, `ResizeObserver`, 128 parameter slots, endpoints-first block, lint rules, typed locals, struct-field initialisers, Assistant panel modes, snapshots — list in `docs/research/amorph-host-contract-notes.md` §6

## 7. Later (JUCE / VST3 phase)

- [ ] Re-evaluate manifest `externals` / resources once side-loading is allowed
- [ ] VST3 CC output reliability per DAW (`docs/02-host-formats.md`)
- [ ] VST-MA shell for Cubase MIDI insert slots (optional)
- [ ] Input FX v2/v3, Output FX v2/v3 (concept §3)

## Log

- 2026-09-06 — Kit read, embedding probes run, ADR-0002, concept, prior-art research, this list.
- 2026-09-06 — Owner handed over `artistsindsp.com/llms.txt` → `amorph-for-agents` repo read; host-contract notes, H0/H8/H9 added, H2/H7 partly answered, 128-slot budget adopted.
