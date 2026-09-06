# Host and plugin format landscape (context)

Status: September 2026. Context only — the build plan lives in `03-architecture.md`, and
plugin work happens outside this repository.

## The three formats

**VST2** (`.dll` on Windows). Still loadable in Cubase 14/15 but disabled by default;
enabled under Studio → VST Plug-in Manager → the "VST 2" button, which triggers an
immediate rescan. Not available on Windows ARM; on macOS only under Rosetta. Dead as a
target format for a new project.

**VST3** (`.vst3`). The current standard. **Cubase does not host VST3 in its MIDI insert
slots.** A MIDI-processing VST3 has to run as an instrument with event output and be routed
through a MIDI track. This has been an open feature request on the Steinberg forum for
years, most recently with Cubase 15 in view.

**VST-MA** (VST Module Architecture). Steinberg's own format for the MIDI insert slots,
published in 2003/04 expressly so that third parties could write MIDI effects for Cubase
and Nuendo. Modules live in the program folder under `Components`, not in a user plugin
path.

## Status of VST-MA

No withdrawal, no end date, no help-centre article — unlike VST2. The name lives on in the
current VST3 developer portal, but there it means the COM-like base layer that VST3 sits
on, not the 2004 MIDI plugin API.

Blue Cat Audio answered a 2022 question about a VST-MA version of Plug'n Script by saying
they did not consider the plugin type actively supported and had never seen anyone release
VST-MA plugins — while the SDK was still on the developer page and Cubase itself ships half
a dozen MIDI plugins in that format.

**Practical finding from this project:** Frank's MIDI Plugins (Frank Deinzer,
midi-plugins.de, commercial, MFX for Cakewalk plus a Cubase variant for the `Components`
folder) run in Cubase 14. The scan simply does not happen automatically at startup — they
are read via the update button in the submenu. **So the door is not closed.**

## Consequence for the format choice

VST-MA still is not the first choice: undocumented, unchanged since 2004, exactly one
target program. The sensible order is VST3 first, VST-MA optionally later as a second shell
around the same core — which then buys the real MIDI insert slot in Cubase without giving
up portability.

## Known VST3 limitation for MIDI output

VST3 permits note output from plugins, but pitch-bend and CC output are not reliable and
support varies between DAWs. FeelYourSound explicitly recommend the VST2 versions of their
own MIDI plugins where available.

For a drum mapper this matters as soon as hi-hat pedal CC is to be translated. Note
remapping alone is uncritical. **Verify in the target environment before planning the CC
feature.**

## Latency

A real MIDI insert processes events inside the track, ahead of the instrument. The detour
through a VSTi in the rack usually costs one audio buffer in Cubase, because a plugin's
MIDI output is only produced during audio processing. That is the substantive reason to
build a VST-MA shell later after all.

## Other findings

- Cubase's own MIDI plugins are listed under Studio → More Options → System Component
  Information, tab "MIDI Plug-ins". First place to look when a module does not appear.
- Cubase's built-in **drum maps** implement an I-Note/O-Note principle. They can do 1:1
  note → note, but no velocity-dependent articulations, no CC translation and no fallbacks.
  That gap is exactly where a dedicated plugin adds value.
- 32-bit plugins have been gone since Cubase 9, regardless of format.
- `pizmidi` (thepiz.org) is open source, JUCE-based and covers many classic MIDI utility
  functions — a usable reference.
