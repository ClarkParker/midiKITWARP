# midiKITWARP — plugin concept (Amorph prototype)

**Status:** draft for owner review, 2026-09-06. Companion to `docs/03-architecture.md`
(mapping core) and `CHECKLIST.md` (work list). Decisions with measurements live in
`docs/adr/0002-data-embedding-in-the-monolith.md` and
`docs/evidence/cmajor-embedding-probes.md`; the module survey in
`docs/research/midi-fx-prior-art.md`.

The prototype is built with the Amorph kit (`../Amorph_DEV_KIt`): one Cmajor DSP file,
one JavaScript Web-Component UI file, a manifest, and the parameter bridge between them.
Later the same core moves to JUCE/VST3, where side-loading becomes available again.

---

## 1. What it is

A 16-channel MIDI hub. Every input channel is a **source** (a player, an e-drum module, a
DAW track in some library's layout); every output slot is a **target** (a sampler or
module expecting another layout). Between them: a routing matrix, the pivot mapping, and
two chains of MIDI effects. One drum track can feed several samplers in different layouts
at once — layering falls out of the pivot for free, because the source layout belongs to
the input and the target layout to the output.

```
midiIn (ch 1..16)
  └─ INPUT c  ─── filter ── input FX chain (performance level) ──┐
                                                                  │  route[c][o]  (16 × 16 matrix,
  … 16 inputs …                                                   ├─►  any input to any set of outputs,
                                                                  │   several inputs may merge into one output)
  ┌───────────────────────────────────────────────────────────────┘
  └─ OUTPUT o ── pivot map  src(c) → pivot → tgt(o)⁻¹ + fallback chain
                 ── output FX chain (target level) ── out channel ── scheduler ──► midiOut
MAIN: transport clock · Take ID (global random seed) · shared look-ahead / latency · panic ·
      monitor with unmapped-note list · presets / A-B
```

## 2. Layer one — routing and mapping

| Element | Per | State | Notes |
|---|---|---|---|
| source layout | input c | parameter | stable numeric layout ID (see §4) |
| input filter | input c | parameter | note range, velocity floor, pass/drop CC & PB |
| route mask | input c | parameter (16-bit mask) | which outputs this input feeds |
| target layout | output o | parameter | |
| out channel | output o | parameter | 0 = keep the input channel, 1–16 = force |
| pass unmapped | output o | parameter | pass a note the target doesn't know, or drop it |

Mapping is `src(c) → pivot → tgt(o)⁻¹` with the fallback chain of `03-architecture.md`
(exact articulation → related articulation → base articulation → drop). The DSP holds the
result as one flat table `outNote[(c·16 + o)·128 + n]` (32,768 × `int32`, value =
`note + 1`, 0 = drop), rebuilt outside the audio path whenever a layout or route changes.
That table shape is not cosmetic: the probes show a multi-dimensional `int32[16,16,128]`
costs 7.5 s of JIT time and 75 s once it gets init loops, the flat version 0.2 s.

**Merging.** Several inputs into one output are legal. Every emitted note is tracked by
its *input* identity `(c, n) → (outCh, outNote)`, so the note-off follows the note that
was actually sent even if the mapping changed meanwhile (functional test in the evidence
doc). Two inputs landing on the same output note are refcounted per `(outCh, outNote)`,
so the first note-off does not kill the second note.

## 3. Layer two — the MIDI effect chains

Two chains, because the same effect means different things in different places: an input
chain shapes a *performance* once, an output chain adapts the result to one *target*. Both
are fixed-order racks with per-module bypass; module order is decided per module type,
not by the user (v1). Every random module draws from the strip-wide **Take ID** hashed with
the musical position, so a take is reproducible across loops, locates and bounces
(`research/midi-fx-prior-art.md` §3.6).

### Input chain (performance level, per input channel)

| # | Module | Core controls | v |
|---|---|---|---|
| 1 | **Filter** | note range, velocity range, CC/PB/AT pass, channel | 1 |
| 2 | **Velocity** | curve (gamma / S / 3 breakpoints), compressor-expander (threshold, ratio incl. < 1, soft knee, make-up, auto ceiling), downward expansion below threshold, compand pivot | 1 |
| 3 | **Humanize** | targets: timing / velocity / length; amount per target; **distribution** (uniform, triangular, gauss, exp, reverse exp, user curve); **character** ρ (white → pink → brown, one-pole OU); weight, chance, hold (per note / per pitch / per bar); early-only / late-only | 1 |
| 4 | **Groove** | swing % (MPC semantics, timing only), grid, strength, safe zone, groove template (position / velocity / length %), per-instrument push-pull ("groove DNA") | 2 |
| 5 | **Length** | fixed gate / scale / min-max, overlap fix, legato via retrigger-close | 2 |
| 6 | **Substitute** | probability-based articulation swap on the pivot (snare centre → rimshot 10 %), round-robin bag with reset policy, alternation | 2 |
| 7 | **Ornament** | flam / drag / ruff (spacing, grace velocity, hand alternation → different RR index) | 2 |
| 8 | **Repeat** | tempo-synced echo with velocity decay, RR advance per repeat, beat align | 3 |
| 9 | **Ghosts** | ghost-note generator on free subdivisions (density, ceiling, backbeat mask) | 3 |
| 10 | **Texture** | urgency (velocity → timing), de-machine-gun, performance AGC, chance/drop, accent pattern | 3 |

### Output chain (target level, per output slot)

| # | Module | Core controls | v |
|---|---|---|---|
| 1 | **Target velocity** | curve / limits tuned to the library, minimum velocity | 1 |
| 2 | **Choke** | groups with SFZ `group` / `off_by` semantics, choke time 0–50 ms, self-choke flag, "auto from GM" preset | 1 |
| 3 | **Transpose / channel** | octave, semitone, channel force, CC filter | 1 |
| 4 | **Hi-hat bridge** | CC↔articulation zones with hysteresis, polarity, chick / splash detection, reverse bridge (CC before note) | 2 |
| 5 | **Articulation** | velocity → articulation with hysteresis + dwell; emit as keyswitch / CC / program / channel / note offset; re-arm on locate | 2 |
| 6 | **Voices** | per-group voice budget with stealing policy, mute-with-tail | 3 |

### Main

Transport receiver (`transportIn`, kit doc 14) · Take ID · shared look-ahead with reported
latency (one delay for everything that needs to be early: flams, negative groove offsets,
pre-delay) · panic / all-notes-off on stop · MIDI monitor with **unmapped-note list and
map coverage %** · preset / A-B.

Column `v` = the release the module is planned for. v1 is deliberately small: the
mapping core plus the modules that prove both chains and the scheduler.

## 4. Data: what lives where

Full reasoning in ADR-0002. Summary:

| Data | Lives in | Form | Size (200 layouts) |
|---|---|---|---|
| layout → pivot tables, layout IDs, vocabulary parents (fallback chain) | **DSP source**, generated trailing `namespace kwdata` | `const int32[]` / `int64[]` literals, ≤ 65,536 per list | ~50 KB binary, ~130 KB text |
| names, vendors, articulation semantics, provenance, UI metadata | **UI source**, generated trailing constant | deflate-raw + base64, inflated at start with `DecompressionStream` | ~60 KB |
| user-made maps, MIDI learn, custom layouts | **stored state** (`sendStoredStateValue`) | JSON; pushed to the DSP as chunked struct events (≤ 64 KB each) | small |
| slot configuration and module enable/amounts | **parameters** | `paramN` | — |
| deep module settings (curves, tables, choke graph) | **stored state**, pushed on UI load | JSON → struct events | small |

Rules:

- **Layout IDs are stable and append-only.** They are saved in DAW projects as parameter
  values. The generator emits `layoutOffset[id]`, so table order may change, IDs never.
- **One generator, one source of truth.** `tools/build_monolith.py` reads the curated
  export of the data pipeline and writes both embeddings; the DSP and the UI are never
  edited in `dist/`.
- **No decompression in the DSP** — Cmajor has none, and the numeric tables don't need it.
- **Host test H1 decides** whether deep module settings may stay in stored state or must
  become parameters (does Amorph instantiate the view on project load with the window
  closed?).

## 5. Realtime core (Cmajor) — binding rules

From the kit's golden rules plus the probes:

1. All MIDI work in `event midiIn`; `main()` runs the **scheduler**: a fixed ring of
   pending events (frame, status, note, velocity, channel), emitted when due. Time-based
   modules only ever enqueue.
2. **Flat arrays, `int32`, zero means "none".** No multi-dimensional state arrays, no
   init loops over large arrays (probes: 0.2 s vs 75 s JIT).
3. Tables are rebuilt in parameter/event handlers, never touched by the scheduler
   mid-flight; a rebuild writes a complete row and flips per-slot validity last.
4. Note-off tracking by input identity with refcounts (§2). All-notes-off on transport
   stop, on panic, and on any table rebuild that changes an output channel.
5. Anything "early" is implemented as "less delay" behind one shared look-ahead
   reported as `processor.latency` (host test H5).
6. Channel nibble preserved end to end: `getChannel0to15()` in, `0x90 | ch` out
   (verified in the compiler test; in the host it is H2).
7. Random: xorshift/splitmix on `(TakeID, bar, step, pitch, channel, moduleIdx)` — never
   `processor.session` for anything audible.
8. CC translation (hi-hat) waits for H6 (CC throughput in Amorph / VST3).

## 6. UI

The kit contract is fixed (`Amorph_DEV_KIt/docs/03_UI_WEBCOMPONENT.md`): one file, light
DOM, no imports, CSS `zoom` scaling on a fixed chassis, echo-loop protection, cleanup in
`disconnectedCallback`, `// WINDOW SIZE: WxH` on line 2. The scaling recipe in
`07_SCALING.md` is adopted 1:1 (kit rule 8).

**No framework.** The examples in the kit are vanilla and field-tested; a 16 × 16 matrix,
16 channel strips and a module rack are plain DOM plus Canvas. We build a small set of
primitives (knob, toggle, select, breakpoint curve, matrix cell, module card, meter) in
`src/ui/` and concatenate them into the monolith. An MIT micro-library (Preact, ~4 KB)
could be inlined later if module UIs outgrow this — deferred, not needed for v1.

**Structure (chassis 1280 × 800, zoom-scaled):**

- Top bar: name, preset strip, Take ID, latency readout, panic, A/B.
- Left rail: 16 input strips — activity lamp, source layout, route indicator.
- Centre: **the matrix** (Canvas) — cells light on activity, input side in orange, mapped
  output side in pink, unmapped hits in a cold grey-blue so they stand out.
- Right rail: 16 output slots — target layout, channel, activity, choke lamp.
- Bottom drawer: the selected slot's module rack (input chain / output chain tabs).
- Views: *Matrix* (above), *Map* (source note → pivot → target note with names, unmapped
  list, MIDI learn, audition), *Monitor*.

**Design language** — dark, minimal, one accent gradient:

```
--bg-0 #0A0A0D   --bg-1 #111116   --bg-2 #17171E   --line #22222B
--text #EDEDF2   --muted #8B8B98  --cold #5C6B8A (unmapped / inactive)
--accent-a #FF7A1A (neon orange) → --accent-b #FF4F5E (coral) → --accent-c #FF2E9A (pink)
glow: 0 0 24px rgba(255,79,94,.45)   fonts: system stack, monospace for numbers (no web fonts)
```

Techniques from `08_UI_RENDERING.md` that are known to work in Amorph: conic-gradient
knob rings, SVG-filter lighting for switches, Canvas for meters and the matrix. Not used:
`backdrop-filter`, `vw`/`vh`, WebGL, `transform: scale()`. Animations pause when hidden.

## 7. Build pipeline

```
data export (pipeline, research branch)  ─┐
src/dsp/*.cmajor  (modules, ordered)      ├─► tools/build_monolith.py ─► dist/midiKITWARP/
src/ui/*.js + *.css (primitives, views)   ┘        KitWarpDSP.cmajor · KitWarpUI.js · midiKITWARP.cmajorpatch
checks: Amorph_DEV_KIt/tools/preflight.py · cmaj test tests/cmajor/*.cmajtest · CI
```

Python, standard library only, like the kit's tools. The generated data blocks are the
last thing in each file and clearly delimited, so they can be stripped when the source is
pasted into an AI context.

## 8. What must be verified in Amorph before the design is final

| ID | Question | Why it matters |
|---|---|---|
| H1 | Is the view instantiated on project load with the window closed? | stored state vs parameters for module settings (ADR-0002) |
| H2 | Are MIDI channels delivered to `midiIn` and passed from `midiOut` unchanged? | the whole 16-slot idea |
| H3 | Does `sendEventOrValue` deliver a struct with `int32[128]` fields to a non-parameter `input event`? | UI → DSP table push |
| H4 | Does `DecompressionStream` exist in Amorph's WebView (mac / win / linux)? | UI blob format |
| H5 | Is `processor.latency` honoured by Amorph and the DAW? | look-ahead bus |
| H6 | Do CC and pitch-bend pass through `midiOut` to a downstream instrument? | hi-hat bridge |
| H7 | `transportIn` slot order and PPQ behaviour as documented in kit doc 14? | groove, repeat, per-bar hold |

Each is a five-minute patch; H2 and H3 come first because they gate the core.

## 9. Open points

- Cmajor `int8` state arrays failed a functional probe — `int32` until understood.
- The DSP source carries ~130 KB of numbers; acceptable for the compiler (0.2 s), but it
  is text the Amorph AI panel would read. Keep it stripped from prompts.
- Parameter budget: 16 inputs × (layout, mask, filter) + 16 outputs × (layout, channel,
  pass) ≈ 100, plus module enables/amounts. Field-tested fine (200+), but the automation
  list gets long — decide the parameter naming/grouping before the first preset exists.
