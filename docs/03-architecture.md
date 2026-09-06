# Architecture of the mapper (context for the data work)

The plugin itself is built elsewhere. This document is here because the data model in this
repository has to serve it, and because two of its properties — the pivot and the fallback
chain — *are* data decisions.

## Purpose

One MIDI drum track should hit the right instruments in different drum libraries and
modules. Pick a source on the left, a target on the right, translate in real time.

## Core principle: pivot instead of N×N

No library-to-library assignments. One fixed intermediate vocabulary:

```
source layout  ──[source map]──▶  pivot  ──[target map⁻¹]──▶  target layout
```

Every library gets exactly **one** definition. A new library costs one file instead of N.
All combinations fall out for free.

The `.iom` files supply the left half for eleven layouts already (see `01-format-iom.md`).
The right half is the inverse of the same tables.

### Ambiguity of the inverse

Source maps are not bijective: several source notes land on the same pivot. Inverting needs
a rule. In a note-number pivot this ambiguity is unavoidable and large — measured at 42 %
for Superior Drummer 3. That measurement is why this repository does **not** use a
note-number pivot; see `docs/adr/0001-pivot-vocabulary.md`.

With a symbolic pivot the remaining ambiguity is confined to genuine one-way collapses
(a target that really has fewer articulations than the source), and it is visible in the
data instead of hidden in the numbers.

### Fallbacks

If the target does not know a pivot entry, the note must not simply disappear. Chain:
exact articulation → related articulation of the same instrument → base articulation →
drop. Example: "snare rimshot" missing → "snare centre", optionally with a velocity lift.
Without this a mapper is unusable in practice, because hardly any two libraries have the
same articulation coverage.

The `.iom` data contains **no** names, only numbers. The pivot has to be labelled once —
once in total, not once per library. That labelling is the vocabulary in `vocabulary/`.

## Channels: 16 slots

One slot per MIDI input channel. Slot n holds:

| Field | Meaning |
|---|---|
| `enabled` | slot active |
| `sourceMap` | source layout |
| `targetMap` | target layout |
| `outChannel` | output channel (0 = unchanged) |
| `passUnmapped` | pass an unknown note through, or drop it |
| `velocityCurve` | optional, per slot |

## Realtime rules (constrains the data format)

**Precomputed lookup table.** The audio callback does not search, does not allocate and
does not lock.

```
int8_t  outNote[16][128];   // -1 = not mapped
uint8_t outCh  [16][128];
```

2048 entries, O(1). Rules, fallbacks and inversion are computed into that table **outside**
the callback, once.

This is the reason for the "no runtime parser" criterion on the storage format: the data
has to reach the binary as a compiled table, not as a file that is parsed while audio runs.

**Switching by pointer swap.** Build the new table fully in the background, then activate
it atomically. Never modify the live table in place.

**Note-off tracking.** The most critical detail. A note-off must go to the note that was
actually sent — not to the one the current mapping would produce.

```
int8_t  heldNote[16][128];  // emitted note, -1 = nothing open
uint8_t heldCh  [16][128];
```

Edge case: two different input notes can map to the same output note. If both are held, the
first note-off kills the second note. Solved cleanly with a refcount per `(outCh, outNote)`.

## Scope of v1

In: note mapping, channel assignment, 16 slots, velocity curve per slot, fallback chain,
`.iom` import, MIDI learn for the source column, audition button for the target column.

Out: round robin, keyswitches, position-dependent hi-hat, velocity-dependent articulation
selection. Those need a different data model.

**But:** the data model in this repository must not make them impossible later. Velocity
ranges and keyswitches are recorded in the device data where a primary source documents
them, and simply ignored by v1.

CC translation (hi-hat pedal CC4 vs CC1) is wanted but depends on whether the target
environment passes CC output through VST3 reliably. The vocabulary therefore carries a
separate controller namespace so the data is ready when the feature is.
