# Research: the current Amorph host contract (amorph-for-agents)

Source: `github.com/Artists-in-DSP/amorph-for-agents`, commit `2835fee` (2026-09-05), whose
generated context comes from Amorph source commit `b5b1eb17` and targets **Cmajor 1.0.3175**.
Entry point handed over by the owner: `https://artistsindsp.com/llms.txt` (the site itself sits
behind a captcha; the GitHub repo is the readable copy). The kit (`../Amorph_DEV_KIt`) captured
the IDE prompts on 2026-06-16; this repo is three months newer and differs in places that matter
for us. Where the two disagree, this document lists both and says what midiKITWARP does.

## 1. Product facts that bound the design

| Fact | Source | Consequence |
|---|---|---|
| Three runtimes as **separate binaries**: `Amorph_Instrument`, `Amorph_FX`, `Amorph_MIDI`; "MIDI in → MIDI out (silent audio)". Code is not portable between variants. | PRODUCT_GUIDE | We build for `Amorph_MIDI` only. |
| **128 parameter slots** ("headroom; typical patches use 6–16"). The kit's "200+ field-tested" predates this wording. | PRODUCT_GUIDE | Parameter budget ≤ 128, with headroom: target ≤ 96. Deep module settings cannot be parameters. |
| Editor tabs DSP / UI / **Manifest** — the manifest is patch metadata; the kit reports it read-only. | PRODUCT_TIERS, kit doc 13 | No `externals`, `resources`, `worker` (ADR-0002 stands). |
| **v0.99 (Gumroad, today):** copy-paste only. **v1 beta (next):** MCP, in-plugin BYOK, share by link. v1.0 ~ end of summer 2026. Check *Settings → Connections* to tell the two apart. | BUILD_COMPAT | Which build the owner runs decides whether host tests can be driven by Claude Code over MCP (see §5). |
| DAW session embeds a copy of the patch; reopening a session restores that copy, not offline file edits. | AGENTS.md | Persistence of the *code* is the host's job; persistence of *settings* is still parameters / stored state (H1 open). |
| Play view has **snapshots** (knob states) and **knob presets** within a patch; MIDI CC actions for next/previous snapshot. | PRODUCT_GUIDE | Host-side preset handling exists; our A/B and presets can start as snapshots. |
| `run_qa_probe` renders a patch **headlessly** with real MIDI incl. **GM drums**, 32 × 512-sample blocks; `run_ui_probe` audits `[data-param]` controls against DSP endpoints; `audition_patch` does not support MIDI-only patches in v1. | TOOLS.md, ONTOLOGY | With MCP, a drum-note round trip through our mapper can be checked without a DAW. |

## 2. DSP contract — rules Amorph enforces or expects (binding for `src/dsp` and the generator)

From `context-src/v1/dsp/midi.md` and `shared/core-dsp-foundations.md`. Several are described as
**Amorph lint** (syntax-based, no data-flow inference), so they are hard requirements, not style:

1. **Parameter IDs are exactly `param1..paramN`, sequential.** "Descriptive IDs such as `paramSnap`
   are invalid for Amorph even if Cmajor accepts them." *(Kit says custom names work — follow the
   official rule.)* Every parameter carries `name`, `min`, `max`, `init` (and `step: 1` + integer
   bounds whenever `text:` labels are used). No trailing comma before `]]`.
2. **All endpoint declarations in one contiguous block at the start of the processor**, before any
   state, struct, handler or function. Never interleave endpoint / state / handler groups.
3. **`float(processor.period)`** around every occurrence of `processor.period`; bare or `float64(…)`
   forms fail the lint. Host-PPQ maths uses `processor.frequency` only (never cast to `float`,
   never divided by `processor.period`).
4. **Every `/` and `%` divisor must be visibly non-zero**: write `% max(1, count)`; `% heldCount`
   is rejected because it starts at zero. Guard float division with an epsilon.
5. **No `external`** for internal constants (host-supplied only) — consistent with ADR-0002.
6. **Struct fields are declarations only** — no `int note = -1;` inside a `struct`; initialise
   instances explicitly. (Our zero-is-none encoding avoids initialisation anyway.)
7. **Typed locals, no `let`** — stated as a generation policy ("required count is zero") and as a
   safeguard against redeclaration inside `loop`/`for`/`while` bodies. The kit's examples use `let`;
   our generated source will not, so it passes whatever the lint checks.
8. **`main()`**: `loop { advance(); }` for event-driven MIDI FX, **but** "host-synced arps / drums /
   sequencers may advance PPQ and schedule notes in `main()`" — the scheduler in the concept is
   explicitly allowed.
9. Forbidden identifiers `input`/`output`/`stream`; no `double`/`unsigned`/`size_t`/`auto`; ASCII
   only; `select()` is vector-only; `processor.currentTime` does not exist; float `%` is invalid
   (`fmod`).
10. **Transport** (`shared/host-transport.md`):
    ```
    input event float transportIn;   // reserved, hidden, no [[ ]], never a paramN
    slots: 0 play · 1 bpm · 2 numerator · 3 denominator · 4 ppq · 5 barStart   (repeats)
    ```
    *Kit doc 14 declares `float64` and calls slot 5 "unused/opaque" — the official contract is
    `float` and slot 5 is `barStart`.* Parse in the handler, never in `main()`. Advance
    `currentPpq += float64(hostBpm) / 60.0 / processor.frequency` once per frame while playing;
    a received PPQ only replaces `currentPpq`; never reset it on play/restart; trigger from
    `globalStep = floor(currentPpq / stepLength)` with `lastStepIndex`; **buffer-size audit**:
    identical output at 31, 64, 257 and 511-frame buffers. Transport stop clears generated notes
    and schedules, never held input notes.
11. Delay/state budget guidance: keep total fixed state "near or below 131072 floats"; copying
    65536 into every buffer "can cause a host compile stall" — matches our probe finding that
    shape and init loops, not size, stall the JIT.
12. Output contract for pasted code: one fenced block, `processor Name [[ main ]]` (name required),
    complete file, no placeholders. Relevant only for the copy-paste path.

## 3. UI contract — deltas vs the kit (binding for `src/ui`)

From `context-src/v1/shared/core-ui-contract.md` and `ui/midi.md`:

| Topic | Official (2026-09) | Kit (2026-06) | midiKITWARP |
|---|---|---|---|
| Control identity | `.control[data-param="paramN"]` with `data-min/max/init`, optional `data-mid/step`, `data-control`; exactly one wrapper per parameter | `data-endpoint-id="paramN"` | `data-param` (plus `data-endpoint-id` costs nothing) |
| File size | "New files must stay below 8000 visible characters" — a generation rule for LLM output | ~8 KB examples | Our monolith is far bigger → **H8**: confirm the runtime has no size limit |
| Listener | `addAllParameterListener(({ endpointID, value }) => …)` then `requestParameterValue` per param | same | same |
| Layout | `:host { display:block; width:100%; height:100% }`, no fixed px on `:host`, no scrolling containers, viewport-constrained grid/flex | fixed-size chassis scaled with CSS `zoom` (07_SCALING, battle-tested) | Kit recipe 1:1 (rule 8), chassis inside a 100 % host; verify with `run_ui_probe` if MCP is available |
| Canvas | size once in `connectedCallback`, never in rAF; **never `ResizeObserver`** (core contract) — the MIDI UI ref still allows one | "start resize observers" | No `ResizeObserver`; size once, resize via the zoom recipe |
| MIDI hooks | `window.__amorphProcessMidi` / `__amorphProcessMidiOut`, messages `{ s, d1, d2 }`, "use `s & 0xF0`" → the status byte **carries the channel nibble** | same hooks | Activity lamps per channel come straight from `s & 0x0F` — partial evidence for **H2** |
| Send MIDI | `sendMIDIInputEvent("midiIn", (status << 16) \| (d1 << 8) \| d2)`; `sendMIDI` does not exist | same | Audition button and MIDI-learn use it |
| Structure | factory `createPatchView` first, one plain control-helper class, exactly one `HTMLElement` subclass, state-only constructor, idempotent `_mounted` guard, light DOM, `// END_AMORPH_UI` last line | custom element + guarded define | Follow the official shape; more helper classes are fine outside the paste flow but keep one `HTMLElement` |
| Stored state | not mentioned anywhere | `sendStoredStateValue` field-tested, round-trips presets | **H1** stays open; nothing essential may depend on it |

## 4. Host tests — what the repo answers and what it changes

| ID | Status after reading | Note |
|---|---|---|
| H1 view instantiated on project load | open | not documented |
| H2 channel preserved in / out | **partial** — the UI hook exposes the channel nibble in `s`; DSP `getChannel0to15()` exists; whether `midiOut` keeps `0x9n` unchanged is still unproven | keep the test |
| H3 struct event from `sendEventOrValue` | open | not documented |
| H4 `DecompressionStream` | open | WebView engine not documented |
| H5 `processor.latency` | open | not documented |
| H6 CC / pitch-bend through `midiOut` | open | `isController`, `isPitchWheel` exist on input only |
| H7 transport | **answered on paper** — slot order and PPQ rules above; still verify the buffer-size audit with our scheduler | reduce to a check |
| **H8** UI file size | new — is the 8000-character rule an LLM-output rule only? | a 200 KB UI must load |
| **H9** Amorph lint on generated source | new — big `const` tables, `int64` literals with `L` suffix, chunked arrays, `% max(1,…)` guards | paste `dist/KitWarpDSP.cmajor` once and read the lint result |

## 5. Working with the host from an agent

With a **v1 beta** build, a local Claude Code (or Cursor / VS Code) session connects to the
running runtime through the auto-deployed `mcp_bridge.py` (macOS
`~/Library/Presets/Artists_in_DSP/AMORPH/`, Windows `%APPDATA%\Artists_in_DSP\AMORPH\`), ports
7331–7399. The loop is `get_host_status → read_code / edit_lines → task_complete → apply_draft →
get_error`; `run_qa_probe` renders headlessly with GM drum notes, `run_ui_probe` audits the UI. That
makes H2, H3, H7, H8 and H9 scriptable on the owner's machine. This remote session cannot reach a
local runtime; the owner (or a local session) runs them. On **v0.99** everything is copy-paste
through the Build tab.

## 6. Notes for the kit (Amorph_DEV_KIt)

Not applied here — the kit is its own project. Deltas worth reconciling: parameter naming rule,
`transportIn` type and slot 5, `data-param`, `ResizeObserver`, the 128-slot figure, the
endpoints-first block rule, the `float(processor.period)` and divisor lint rules, typed locals,
struct-field initialisers, the Assistant panel modes (Ask / Plan / Agent) and snapshots.
