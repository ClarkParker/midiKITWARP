# Target environment: what to settle before starting (context)

Planned: VST3 with MIDI in and MIDI out, written in **Cmajor**, host **Amporph**. This is
plugin-side work and happens outside this repository; it is recorded here because it
bounds what the data has to deliver.

## What is settled

Cmajor exports a complete JUCE project in C++ via `cmaj generate --target=juce`, from which
VST/AU/AAX can be built; a CLAP export exists as well. There is a Cmajor JIT plugin that
loads patches in any DAW and recompiles on file change, so the fast iteration loop exists.
MIDI input in patches is standard.

## Risk 1 — MIDI output in Cmajor

**To be verified before anything else.** Whether a Cmajor patch can *emit* MIDI, and
whether that output survives the JUCE export all the way to the VST3 event bus, is not
confirmed. Without it the whole approach fails.

Minimal test, one hour: a patch with MIDI in and MIDI out that transposes incoming notes by
+12 and does nothing else. If that runs in the JIT plugin and in the JUCE export, the path
is clear.

If the test fails, the alternative is JUCE directly: `JucePlugin_IsSynth=1`,
`ProducesMidiOutput=1`, `WantsMidiInput=1`. The mapping core is unaffected as long as it
stays host-free.

## Risk 2 — VST3 and CC output

VST3 permits note output, but pitch-bend and CC output are unreliable and DAW-dependent.
Uncritical for note mapping. For the planned CC translation (hi-hat pedal) this has to be
tested in the target environment before it is planned in.

## Risk 3 — Cmajor and state

Cmajor patches are aimed at DSP. A mapper is mostly table logic and state management:
16 slots, 2048-entry lookups, note-off tracking, preset handling, `.iom` import. Plausible
split: Cmajor does event processing against a finished table, C++ does loading, inversion,
fallbacks and UI.

**Consequence for this repository:** the compiled artefact the data pipeline produces must
be consumable from plain C++ with no dependencies, because that is the side that owns the
table.

## Risk 4 — Amporph

No reliable information available on this host. To settle before it is fixed as the
prototype host: does it have real MIDI FX slots; does it pass a plugin's MIDI out to
downstream nodes; is channel information preserved; CC throughput?

If that drags on, Reaper's JSFX is the fastest comparison loop for the core: a real MIDI FX
slot, no build step, the script reloads on save.

## Order

1. MIDI-out minimal test in Cmajor.
2. Channel behaviour in Amporph.
3. Mapping core, host-free, against this repository's data as test input.
4. Note-off tracking with held notes and a mapping switch.
5. UI.
6. CC translation last, after the VST3 CC test.
