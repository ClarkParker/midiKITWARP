# Research: MIDI-FX prior art, algorithms and reusable code

Web research, 2026-09-06. Feeds the module catalogue in `docs/06-plugin-concept.md`.
URLs are the sources consulted; licences of code are stated per row and must be
re-checked before anything is ported.

---

## 1. Frank's MIDI Plug-Ins (Frank Deinzer)

**Status:** effectively dead. `midi-plugins.de` still resolves but serves a zero-byte page
(`content-length: 0`, `last-modified: 2026-01-02`). Formats were **MFX** (Cakewalk) and
**VST-MA** (Steinberg Module Architecture — *not* VST/VST3), Windows only. Explicitly
not supported: Ableton, Digital Performer, FL, Pro Tools, Studio One. So the reference
point is a 2004–2012 Windows/Cakewalk-era suite; midiKITWARP is a modern re-do of that
idea, not a competitor to a living product.

**Confirmed module list:**

| Plug-in | Category | What it does |
|---|---|---|
| **Humanize** | Humaniser | Randomises note start, duration, velocity, pitch (via per-note pitch-wheel), plus CC/wheel/RPN/NRPN time & value. See below. |
| **Rhythmic Controller** | Modulator | Step sequencer **for controller events**. Trigger modes: Continuous, Measure Aligned, **Note On** (per-note "controller envelopes"). Interpolation between steps → smooth CC ramps. **User-defined per-step timing in ticks** (non-uniform step grids). |
| **Delete Doubles** | Filter | Removes doubled events (same time), *repeated* events (redundant CC), and **un-octaving** (delete octave doubles, keep top or bottom). Keep-policy selectable. **Temporary Quantization**: quantise → process → un-quantise, so near-doubles are caught without altering timing. |
| **Split Poly** | Splitter | Explodes chords into single lines on separate channels. "Overlap, free channel" guarantees one note per channel (lowest free channel). Track-split vs Live-split. Non-note handling: leave / duplicate / delete / force-to-channel. |
| **Split by Patches** | Splitter | Splits a track with several program-change-switched sounds onto separate channels. |
| **MIDI Statistics** | Monitor | Event statistics (note/wheel/patch/CC/RPN/NRPN). |
| **Virtual Band** | Auto-accompaniment | Chord symbols + style → arrangement. |
| **Track and Clip Notes** | Utility | Per-track / per-clip annotations. |

### Humanize — the randomness model

- **Targets, independently switchable:** Note On (start time) · Duration · Velocity ·
  Pitch (*inserts a randomised pitch-wheel event per note*) · CC/wheel/RPN/NRPN start
  time · CC/wheel/RPN/NRPN value.
- **Four random distributions ("curves"):** **Uniform**; **Gauss (bell)** — "very similar
  to the little inaccuracies produced by a human player… a lot of small and only very few
  large inaccuracies"; **Exponential** and **Reverse Exponential** — "for experimental
  humanization effects"; plus **"an unlimited number of user random curves"**
  (user-drawn PDFs).
- **Fix Note Overlaps** — repairs overlaps *between identical notes* created by jittering
  start/length; plus a **minimum note distance** parameter.
- **Relative vs Absolute units** — ticks / 0–127 / ±8192 vs % of a quarter note / % of 127.

**Takeaways:** (a) a selectable *distribution*, not just an amount, is the differentiator;
(b) user-drawable distribution curves; (c) overlap repair is a first-class part of any
timing/length randomiser; (d) relative (musical) vs absolute (tick) unit switching.

Sources: midiplugins.com/Plugin/12 (Humanize), /Plugin/10 (Rhythmic Controller),
/Plugin/11 (Delete Doubles), /Plugin/13 (Split Poly), /Plugin/15 (Split by Patches),
/Plugin/255 (Virtual Band); forums.steinberg.net/t/humanize-franks-midi-plugin/97715.

---

## 2. Survey of established MIDI-FX products

### 2.1 Cubase / Nuendo

**MIDI Modifiers** (per-track, real-time): Transpose · Velocity Shift · **Velocity
Compression** (ratio as numerator/denominator) · **Length Compression** · **Random 1 & 2**
(target Position / Pitch / Velocity / Length, min/max) · **Range 1 & 2** (pitch or
velocity range, *Limit* = force into range or *Filter* = exclude) · Scale Transpose.
→ steinberg.help, Cubase Artist 14, "MIDI Modifiers".

**MIDI Effects** (18): Arpache 5 · Arpache SX · Auto LFO · Beat Designer · Chorder ·
**Compressor** (velocity) · **Context Gate** (selective triggering/filtering by
polyphonic/monophonic context) · Density (probabilistic thinning) · MIDI Control ·
**MIDI Echo** (delay with pitch/velocity/length decay, §3.7) · MIDI Modifiers · MIDI
Monitor · Micro Tuner · Note to CC · **Quantizer** · StepDesigner · Track Control ·
**Transformer** (real-time Logical Editor: condition → action).
→ archive.steinberg.help, Cubase Pro plug-in reference v11, "MIDI effects".

### 2.2 Logic Pro — MIDI FX

Arpeggiator · Chord Trigger · **Modifier** (CC→CC) · **Modulator** (LFO/envelope →
parameter) · **Note Repeater** · **Randomizer** · Transposer · **Velocity Processor** ·
**Scripter** (JavaScript) · Velocity Limiter. → support.apple.com/guide/logicpro.

Parameter designs worth copying:

- **Randomizer** — *Event Type* · *Input Range* (only values inside are processed) ·
  **Amount** · **Weight** (biases how likely an event is randomised within the Amount
  range) · *Output Offset* (bipolar) · **Seed** (reproducibility).
- **Velocity Processor** — modes **Compress/Expand**, **Value/Range** (limiter),
  **Add/Scale**. Compress/Expand: *Threshold*, *Ratio* (**soft knee**; ratio < 1 =
  expansion), *Make-up* (bipolar), *Auto Gain* (Make-up becomes a **max-velocity
  ceiling**).
- **Note Repeater** — *Repeats*, *Delay* (ms or bars, *Delay Sync*), *Transpose* per
  repeat, **Velocity Ramp**, *Input Through*, *Note Range*.

### 2.3 Ableton Live 12

**MIDI effects:** Arpeggiator · CC Control · Chord · Note Length · Pitch · Random ·
Scale · Velocity (+ M4L devices). → ableton.com/en/manual/live-midi-effect-reference.

- **Velocity**: input window (*Range/Lowest*) + output window (*Out Hi/Lo*) +
  *Operation* (Note On/Off/Both) + *Mode* (Clip/Gate/Fixed) + **Random** + **Drive**
  (pushes toward extremes) + **Compand** (one bipolar knob: expand/compress around the
  midpoint).
- **Random**: *Chance* · *Choices* (1–24) · *Interval* · *Mode* (Random / **Alt** =
  cycling) · *Sign* (Add/Sub/Bi).
- **Chord**: 6 shifts with per-shift **Velocity** and **Chance**, **Strum** (≤400 ms),
  **Tension** (strum acceleration), **Crescendo**. Scale-aware.
- **Pitch**: out-of-range modes **Block / Fold / Limit**.
- **Scale**: 13×13 pitch-class remap matrix, Fold, Lowest/Range.
- **Note Length**: trigger on Note On or **Note Off**; Note-Off mode adds *Release
  Velocity*, *Decay Time*, *Key Scale*.

**Live 12 MIDI Tools** — Transformations: Arpeggiate, **Chop**, **Connect**, **Glissando**,
LFO, **Ornament** (flam / grace notes), Quantize, **Recombine**, **Span**
(legato/tenuto/staccato), **Strum**, **Time Warp**, **Velocity Shaper**. Generators:
Rhythm, Seed, Shape, Stacks, **Euclidean**. → ableton.com/en/live-manual/12/midi-tools.

### 2.4 Bitwig Studio — Note FX (the most complete modern set)

→ bitwig.com/userguide/latest/note_fx

| Device | What it does |
|---|---|
| Arpeggiator | 17 patterns, 3 octave modes |
| **Bend** | Per-note pitch expression from a relative start pitch to the true pitch, curve + pre-delay |
| **Dribble** | "Bouncing ball" repeats with decreasing velocity: first bounce time, damping, shortest bounce |
| Echo | Tempo-synced repeater: repetitions, feedback mode, time, gate, **velocity scaling**, **pitch scaling** |
| **Harmonize** | Transposes by the *live notes of another track* |
| **Humanize** | Randomises timing, velocity and **chance of playback**; early/late options |
| Key Filter | Corrects or removes notes outside a key/mode |
| Latch | Simple / Toggle / Velocity-threshold sustain |
| Micro-pitch | Per-pitch-class and per-octave tuning |
| Multi-note | Chord builder, up to 8 notes, **velocity spread** + **chance** per voice |
| Note Delay | Delay; option to pass note-offs immediately |
| Note Filter | Key range + velocity range, Keep or Remove |
| Note Length | Fixed length (optionally synced), trigger on Press or Release |
| Note Repeats | **Burst or Euclid** modes, accents, velocity decay |
| Note Transpose | Octaves + semitones + fine |
| **Quantize** | Toward the grid with *amount* and **forgiveness threshold**, optional **groove follow** |
| Randomize | Pitch, velocity, timbre, pressure, pan, gain at note start |
| **Ricochet** | Notes as balls in a room; collisions retrigger |
| Stepwise | 8-row step sequencer with per-row **timing** |
| Strum | Speed, direction, step sequencing, **stride**, grace period |
| **Transpose Map** | Remaps each note class individually — *the drum-remap device* |
| **Velocity Curve** | Piecewise shaper with **three breakpoints** |
| **Note Grid** | The Grid as a note processor/generator |

### 2.5 Reaper JSFX

ReaTeam/JSFX `/MIDI` (63 scripts, licence **per file**). Relevant: `talagan_MIDI Note
Remapper`, `talagan_MIDI Force Notes to Range`, `talagan_MIDI Delay X`, `talagan_MIDI Multi
Channel Pre-Delay`, `talagan_MIDI Channel Matrix Router`, `talagan_MIDI CC Mapper X`,
`mbncp_Legato Control`, `cfillion_MIDI note length control`, `cfillion_Sustain pedal to
note length`, `cfillion_MIDI Taps Repeater`, `cfillion_Note Duplicator`,
`albthealbatross_Multi-Channel MIDI Timing Randomizer`, `albthealbatross_MIDI Chord
Strummer`, **`XQ_Drum Converter` / `XQ_Drum Deviator` / `XQ_Drum Equalizer`** (drum-map
conversion + humanisation), `polgo_MIDI Envelocity` / `Varocity`, `mschnell_MIDI MPE to
single channel`, `mschnell_Note On under X velocity to Note Off`.
→ github.com/ReaTeam/JSFX/tree/master/MIDI

### 2.6 Blue Cat's Plug'n Script / PatchWork

AngelScript-scripted audio+MIDI plug-in with JIT, 48 bundled scripts; PatchWork chains
instances in series/parallel. A model for a *scriptable slot* in a channel strip.
→ github.com/bluecataudio/plugnscript

### 2.7 piz midi (Insert Piz Here)

The largest "one idea per plug-in" MIDI-FX collection; e.g. `midiVelocityScale`,
`midiSwing` (delay/velocity offset/**probability** on every other step of a note value).
**GPLv2**, JUCE. → thepiz.org/plugins, github.com/kzantow-audio/pizmidi

### 2.8 eaReckon MIDI Polysher (free)

Key range modes **Pass / Exclude / Free / Nearest** (*Nearest* re-routes a filtered key
to the closest allowed note instead of dropping it), velocity range, CC/AT/PB filtering,
channel filtering, per-channel activity monitor. → kvraudio.com, "MIDI Polysher".

### 2.9 VCV Rack / Cardinal, Max for Live, the MFX ecosystem

- **VCV/Cardinal**: quantisers in the CV domain (Fundamental *Quantizer*, ML *Quantum*,
  Impromptu *AdaptiveQuantizer*); Cardinal bundles 1382 GPLv3+ modules.
- **Max for Live**: *Expression Control* maps 10 sources (Velocity, Modwheel, Pitchbend,
  Pressure, Keytrack, Expression, **Random**, **Increment**, Slide, Sustain) to any
  parameter.
- **midiplugins.com** catalogues ~307 MFX plug-ins in 35 categories (Arpeggiator,
  Chorder, Delay, Filter, Groove/Swing/Shuffle, Harmoniser, Humaniser, Quantiser,
  Randomiser, Remapper/Converter, Scale/Key Adjuster, Splitter, Strummer, …). Worth
  mining: *TenCrazy* (`Kick Peddler`, `AutoLegato`, `SustainFix`, `Velocity to CC`,
  `CC Map`), *Ntonyx* kits, *Geniesys* (`Swinger`, `DrumScatter`), *Tobybear*
  (`Humanisator`, `Chordator`).

### 2.10 Deduplicated master list of distinct module types (76)

**A — Filter / route:** 1 note/key range filter · 2 velocity range filter · 3 channel
filter/channeliser · 4 event-type filter · 5 CC range filter + thinning · 6 duplicate /
redundant-event remover · **7 note remapper (midiKITWARP core)** · 8 converter (CC↔CC,
note→CC, velocity→CC, PB→CC) · 9 channel/port matrix router · 10 splitter (key, velocity,
polyphony, program) · 11 merger/layerer · 12 rule engine / transformer · 13 context gate.

**B — Pitch:** 14 transpose · 15 diatonic transpose · 16 scale/key quantiser (Block /
Fold / Limit / Nearest) · 17 pitch-class remap matrix · 18 harmoniser · 19 chorder
(per-voice velocity + chance + strum) · 20 chord identifier · 21 micro-tuner · 22 per-note
micro-pitch expression · 23 pitch-bend generator (glissando, per-note bend) · 24 keyboard
mirror/invert.

**C — Time:** 25 quantiser (grid, strength, safe-zone, randomise, iterative) · 26
groove/swing/shuffle templates · 27 humaniser (selectable distribution) · 28 delay /
pre-delay (negative via look-ahead) · 29 note echo (time/pitch/velocity/length decay) · 30
note repeat / ratchet / burst / Euclid · 31 arpeggiator · 32 strummer · 33 ornament
generator (flam / drag / ruff / grace) · 34 time-warp · 35 latch/hold · 36 mono/legato
controller · 37 note-length processor (gate, scale, min/max, **overlap removal**) · 38
sustain-pedal → note-length · 39 density/thinner.

**D — Velocity & dynamics:** 40 offset/scale · 41 curve shaper (gamma, S, breakpoints,
freehand) · 42 compressor/expander (threshold, ratio, knee, makeup, auto-gain) · 43
limiter / fixed velocity · 44 velocity randomiser · 45 crescendo/ramp · 46 accent pattern
· 47 velocity ↔ CC · 48 release-velocity processor.

**E — Generative / modulation:** 49 LFO → CC · 50 envelope → CC (per note) · 51 note step
sequencer · 52 CC step sequencer with interpolation · 53 random CC / chaos · 54 drum
pattern generator (Grids) · 55 Euclidean generator · 56 auto-accompaniment · 57 script
host.

**F — Drum / kit specific (thin coverage everywhere — the opening):** 58 drum-map /
layout converter · 59 round-robin / alternation · 60 choke / mute group · 61 hi-hat pedal
CC ↔ articulation · 62 positional-sensing mapping · 63 velocity → articulation +
keyswitch emitter · 64 kit-level voice budget with stealing.

**G — Utility / monitor:** 65 monitor / event list · 66 statistics · 67 panic · 68
stuck-note guard · 69 annotations · 70 program/bank mapper · 71 XY / controller surfaces
· 72 MPE ↔ single-channel · 73 audio→MIDI trigger · 74 sync/clock utility · 75 SysEx
librarian · 76 tracker/pattern editor.

---

## 3. Math & algorithms

### 3.1 Humanise — jitter distributions

`A` = amount (ticks or ms), `u, u₁, u₂ ~ U[0,1)`.

```
Uniform:        Δ = A·(2u − 1)
Triangular:     Δ = A·((u₁ + u₂) − 1)            // cheap gaussian-ish, bounded — good default
Irwin–Hall(n):  Δ = A·(2/n·Σuᵢ − 1)              // n = 4..12 → near-gaussian, still bounded
Gaussian:       z = √(−2·ln u₁)·cos(2π·u₂)       // Box–Muller
                Δ = σ·clamp(z, −3, +3),  σ = A/3  // 99.7 % inside ±A
Exponential:    Δ = −ln(1 − u)/λ,  λ = 3/A        // mostly tiny, rare large
Reverse exp.:   Δ = A − (−ln(1 − u)/λ)            // mostly large, rare tiny
User curve:     inverse CDF as a 256-entry LUT; Δ = A·(2·LUT[⌊256u⌋] − 1)
```
The LUT form is how "unlimited user random curves" are implemented: the user draws a
PDF, integrate → normalise → invert once, then sampling is one table lookup.

**Why pink/brown beats white for groove.** White jitter is uncorrelated — every note's
error is independent, which reads as *sloppy*; a human's error at note *n* is strongly
correlated with note *n−1* (you are behind the beat for a phrase). Brownian noise (random
walk) drifts away and never returns — reads as *rushing/dragging out of time*. Pink (1/f)
is correlated at all timescales but stationary: micro-wobble plus slow phrase-level lean,
no unbounded drift. Voss & Clarke showed pitch and loudness fluctuations in real music
have 1/f spectra.

**Voss–McCartney 1/f generator** (constant cost per step; firstpr.com.au/dsp/pink-noise):

```c
// state: uint32 dice[16] = {random}, counter = 0, total = Σdice, seed
uint32 k = ctz(counter) & 15;        // which octave-row updates
uint32 prev = dice[k];
seed = 1664525u*seed + 1013904223u;  uint32 nu = seed >> 13;
dice[k] = nu;
total += (nu - prev);                // O(1)
seed = 1664525u*seed + 1013904223u;  uint32 white = seed >> 13;
float out = normalise(total + white);
counter++;
```
Clock it **once per note event** (or grid step), not per sample. 8–10 rows suffice.

**Cheaper: a one-pole "colour" knob** — one state variable, continuous white→pink→brown:
```
x[n] = ρ·x[n−1] + √(1−ρ²)·N(0,1)      // ρ ∈ [0,1): 0 = white, 0.7–0.9 ≈ pink-ish, →1 = brown
Δ[n] = A·x[n]
```
Discrete Ornstein–Uhlenbeck; `√(1−ρ²)` keeps the variance constant, so *Amount* stays
honest while *Character* changes only the colour. **Shipping default**; Voss–McCartney as
the "true 1/f" option.

### 3.2 Velocity compression / expansion

Logic semantics (soft knee, ratio < 1 = expansion), knee width `W`:
```
// v, T in 1..127 ; R = ratio ; W = knee width ; M = makeup
d = v - T
if      2d < -W:            y = v
else if abs(2d) <= W:       y = v + (1/R - 1) * (d + W/2)^2 / (2W)     // quadratic soft knee
else:                       y = T + d / R
y = clamp(round(y + M), 1, 127)
```
- **Auto make-up** with ceiling `C`: `M = C − f(127)` so the loudest input maps exactly to `C`.
- **Downward expansion below threshold** (not in Logic, very useful for drums — deepens
  ghost notes): `if v < T: y = T − (T − v)·R_lo`.
- **Compand** (Ableton, one knob) with pivot `P`: `y = P + (v − P)·2^c`, `c ∈ [−1,+1]`.
- Discrete-domain trap: with 127 steps, ratios above ~4:1 quantise the output to a few
  values → machine-gun velocities. Dither ±0.5 before rounding, or clamp the ratio.

### 3.3 Velocity curves

```
Normalise:  x = (v − InLo)/(InHi − InLo), clamp 0..1
Gamma:      y = x^γ            // γ>1 softer, γ<1 harder;  one-knob: γ = 2^(−k), k ∈ [−1,+1]
S-curve:    x<0.5 → y = 0.5·(2x)^γ ;  x≥0.5 → y = 1 − 0.5·(2−2x)^γ
Tanh S:     y = 0.5·(1 + tanh(k(2x−1))/tanh(k))
Piecewise:  3 breakpoints with monotone cubic (PCHIP) → no overshoot (Bitwig Velocity Curve)
Denorm:     out = round(OutLo + (OutHi − OutLo)·y)
```

### 3.4 Quantise, groove templates, swing

**Quantise (Cubase controls):**
```
q  = round(t/G)·G
if |t − q| < Z:   t' = t               // Z = safe zone ("Non Quantize")
else:             t' = t + S·(q − t)   // S = strength 0..1 (iterative: err_n = err_0·(1−S)^n)
t' += uniform(−R, +R)                  // R = randomise
```

**Swing (MPC / Linn).** Roger Linn: *"I merely delay the second 16th note within each
8th note."* Swing % = the ratio of the two 16ths inside an 8th; 50 % even, 66.7 % =
triplet. Timing only — **never note duration**. Linn also insists random timing does
not help the groove once swing and dynamics are right → Humanize and Groove are
separate modules.
```
G = grid step (one 16th) ; p = swing percent (50..75)
δ = 2·G·(p/100 − 0.5)         // 54 → 0.08 G · 58 → 0.16 G · 62 → 0.24 G · 66.7 → G/3 · 75 → G/2
if (floor(t/G) is odd) t' = t + δ
```

**Groove templates:** `slot[i] = { dPos, velScale, lenScale }` over one or N bars with
independent strengths per dimension (Cubase Groove Quantize: Position / Velocity / Length
%). Extraction: snap each note of a reference part to the nearest slot (±G/2), store
residual offset, velocity ratio, length ratio; drop collisions.

### 3.5 Note-length processing

```
Fixed gate:   L' = Lgate               Scale:  L' = L·s
Staccato:     L' = min(L, k·G)         Legato: L' = (t_next_on − t_on) + O
Clamp:        L' = clamp(L', Lmin, Lmax)
Overlap fix (same pitch+channel): if t_off(n) > t_on(n+1) − ε:  t_off(n) = t_on(n+1) − ε
```
**Live-stream caveat:** legato and overlap-fix need the *next* note. Either (a) a global
**look-ahead delay** of `Lmax` reported as latency, or (b) **retrigger-driven close** —
a new note-on for the same pitch/group immediately emits the pending note-off. (b) is
zero-latency and structurally identical to a choke group (§3.11): implement once, reuse.

### 3.6 Constrained randomness

**Reproducibility — never seed from wall time.**
```
// 1. per-instance PRNG (xoshiro128** / PCG32) seeded from userSeed
// 2. better: stateless per-event hash — survives loop / locate / bounce
uint64 h = splitmix64(userSeed ^ mix(barIndex, stepIndex, pitch, channel, paramIdx))
splitmix64(x): z = x + 0x9E3779B97F4A7C15
               z = (z ^ (z>>30)) * 0xBF58476D1CE4E5B9
               z = (z ^ (z>>27)) * 0x94D049BB133111EB
               return z ^ (z>>31)
u = (h >> 11) * 2^-53
```
A walking PRNG desyncs the moment the host loops or scrubs; hashing the musical position
makes a take bit-identical every time.

**Amount + Character:** `Δ = A·shape(u)`; **Weight/Bias** `u' = u^(2^b)`; **Skew**
(asymmetric up/down amounts); **Chance** (apply only if `u < P`); **Drift** = the
one-pole ρ from §3.1; **Hold** granularity: per note · per pitch (each drum keeps its own
value) · per step · per bar · per phrase. Per-bar hold on velocity randomisation is what
makes hats sound like a performance rather than noise.

### 3.7 Note repeat / echo with feedback

Cubase MIDI Echo / Logic Note Repeater parameter set generalised:
```
t_r = t₀ + D·Σ_{i=1..r} k^i        // k=1 even; k<1 accelerando; k>1 ritardando
v_r = clamp(round(v₀·f^r + o·r), 1, 127)
p_r = p₀ + P·r                      // for drums: P = 0, advance round-robin per repeat instead
L_r = L₀·g^r ;  stop when r > N or v_r < v_floor ;  beat-align: snap t₁ to the grid
```
True feedback topologies need a hard repeat cap and a voice cap.

### 3.8 Round-robin / alternation

```
Cycle:       i = (i+1) mod N            // predictable
Random:      i = ⌊u·N⌋                  // repeats 2–3× in a row → machine-gun
Shuffle bag: pop from a shuffled bag; reshuffle when empty, reject if bag[0] == lastUsed
             ⇒ even distribution, never an immediate repeat   ← use this
History-N:   draw uniformly, reject if in the last N
Velocity-linked: choose layer by velocity band, RR within the layer
```
**Reset policy** must be exposed: on transport start (repeatable renders) / on bar /
never. **Emission** depends on the target: adjacent notes, keyswitch, CC, or channel —
channel-based RR is essentially free in a 16-slot design.

### 3.9 Flams, drags, ruffs

```
Flam (1 grace):   grace at t − Δ,   vel = m·v,  m ≈ 0.40..0.70
Drag (2 graces):  t − 2Δ', t − Δ',  vel ≈ 0.35·v, 0.45·v
4-stroke ruff:    3 graces
Δ  (flam):  tight 10–20 ms · normal 20–30 ms · open 30–45 ms
Δ' (drag):  closed ≈ 12–18 ms · open ≈ 30–40 ms, slightly accelerating (Δ'ᵢ = Δ'·0.85^i)
Humanise:   Δ ← Δ·(1 ± 0.2) ; m ← m·(1 ± 0.15)
Round-robin: force the grace onto a DIFFERENT RR index (other hand, other spot)
```
Grace spacing is a performance parameter, not a grid division. **Real-time constraint:**
graces precede the primary → look-ahead: (a) delay the whole stream by Δ_max and report
latency (recommended, one shared look-ahead bus), (b) "back-flam" after the primary,
(c) ornaments only with look-ahead from the arrangement.

### 3.10 Hi-hat pedal CC ↔ articulation

CC#4 is the de-facto pedal controller; Roland convention 0 = open, 127 = closed (some
invert → polarity parameter). GM notes: 42 closed, 44 pedal, 46 open.

```
zones = [(0,15,OPEN), (16,45,HALF_2), (46,80,HALF_1), (81,115,TIGHT), (116,127,CLOSED)]
// hysteresis h ≈ 4..6: leave the current zone only once cc passes its boundary by h
if cc > hi(cur)+h or cc < lo(cur)−h:  cur = zoneOf(cc)
noteOut = articulationNote[cur]
```
Without hysteresis a pedal resting on a boundary flips articulation on every hit.

**Chick / foot-splash detection:** `dCC/dt` over 20–40 ms; chick = cc crosses CLOSE_THR
upward faster than rateThr → emit note 44 with velocity from the rate; splash = open hat
ringing AND close-then-reopen within ~80 ms → foot-splash articulation.

**Reverse bridge** (articulation → CC for one-note-plus-CC libraries): send the CC at
`t − 1 tick` **before** the note — most samplers latch CC at note-on.

### 3.11 Choke / mute groups

SFZ `group=` / `off_by=` semantics are deliberately **asymmetric**: a region declares the
group it *belongs to* and the group it *is killed by* — a closed hat chokes an open hat
without the reverse. (sfzformat.com: `group`, `off_by`, cymbal muting tutorial.)
```
each mapped note n:  group(n), killedBy(n) ⊆ groups
on note_on(n) at t:  for each sounding m: if group(m) ∈ killedBy(n): emit note_off(m) at t − δ
                     mark n sounding
on note_off(n):      unmark
```
- δ = 1 tick before the note-on (buffer ordering); expose *choke time* 0–50 ms.
- **Self-choke** is a per-group flag (SF2/ARIA choke when `group == off_by`, rgc engines
  don't — don't inherit a convention by accident).
- Defaults: hats → one self-choking group; crashes not choked; "cymbal choke"
  articulation in its own group that kills the cymbal group.

### 3.12 Scale / chord quantisation & voicings

```
mask: uint16 bit i = degree i allowed ;  rel = (note%12 − root + 12) % 12
if mask & (1<<rel): out = note
else for d = 1..6: try down (rel−d) then up (rel+d); ties prefer down
```
Out-of-range policies: **Block** (drop), **Fold** (wrap by octaves), **Limit** (clamp),
**Nearest**. Scale masks: major (0,2,4,5,7,9,11), natural minor (0,2,3,5,7,8,10),
harmonic minor (0,2,3,5,7,8,11), dorian (0,2,3,5,7,9,10), mixolydian (0,2,4,5,7,9,10),
phrygian (0,1,3,5,7,8,10), lydian (0,2,4,6,7,9,11), locrian (0,1,3,5,6,8,10), pent. maj
(0,2,4,7,9), pent. min (0,3,5,7,10), blues (0,3,5,6,7,10), whole tone, dim H-W.

Chord tables: 5 [0,7] · maj [0,4,7] · min [0,3,7] · dim [0,3,6] · aug [0,4,8] · sus2
[0,2,7] · sus4 [0,5,7] · 6 [0,4,7,9] · m6 [0,3,7,9] · maj7 [0,4,7,11] · 7 [0,4,7,10] ·
m7 [0,3,7,10] · m7b5 [0,3,6,10] · dim7 [0,3,6,9] · mMaj7 [0,3,7,11] · 7sus4 [0,5,7,10] ·
add9 [0,4,7,14] · 9 [0,4,7,10,14] · m9 · maj9 · 7b9 · 11 · 13 · quartal [0,5,10].
Diatonic auto-quality: stack scale degrees {0,2,4(,6)} in the scale's own step pattern.
Voicings: drop-2, drop-3, drop-2+4, open, inversions, spread; voice-leading = the
inversion minimising Σ|Δpitch| from the previous chord.

### 3.13 Drum pattern generation (Mutable Instruments Grids)

Bilinear interpolation over a 5×5 map of pattern nodes, thresholded per instrument by a
density control; accent above 192; Euclidean mode via precomputed bit tables. ~50 lines
to port. Source: `pichenettes/eurorack` `grids/pattern_generator.cc` (GPL3 — read, don't copy).

### 3.14 Velocity → articulation & keyswitch emission

```
if v ≥ thr[k] + h  and  (now − lastSwitch) > dwell:  art = k       // hysteresis + dwell
emit via: keyswitch note at t − T_ks (velocity, momentary vs latched) | CC at t − 1 tick |
          program change | MIDI channel (free in a 16-slot design) | note offset
state: re-emit only on change; ALWAYS re-emit on transport locate / loop restart / play
```
"Re-emit on locate" is the classic keyswitch-desync bug.

---

## 4. Open-source code worth learning from / porting

**Licence warning:** GPL/AGPL code can be *read for algorithms* but **not copied** into
a closed or permissively licensed product. Only BSD/MIT rows are safely portable.

| Project | URL | Licence | Reusable |
|---|---|---|---|
| **libremidi** | github.com/celtera/libremidi | BSD-2 | C++20 MIDI 1/2 real-time + SMF I/O; standalone I/O outside a host |
| **midifile** | github.com/craigsapp/midifile | BSD-2 | SMF read/write — import groove templates and drum maps from `.mid`, offline fixtures |
| **sfizz** | github.com/sfztools/sfizz | BSD-2 (library) | Reference `group`/`off_by` choke, `seq_position`/`seq_length` round-robin, velocity layers |
| **Surge tuning-library** | github.com/surge-synthesizer/tuning-library | MIT | Scala/MTS if micro-tuning is ever needed |
| **pizmidi** | github.com/kzantow-audio/pizmidi | GPLv2 | ~80 single-purpose MIDI FX in JUCE — study only |
| **Bespoke Synth** | github.com/BespokeSynth/BespokeSynth | GPLv3 | Modular note-processing graph — architectural reference |
| **MI Grids** | github.com/pichenettes/eurorack | GPL3 | Topographic drum-map maths (§3.13) |
| **ReaTeam JSFX** | github.com/ReaTeam/JSFX | per file | Tiny readable MIDI scripts (`talagan_*`, `XQ_Drum *`, `mbncp_Legato Control`) |
| **Cardinal / VCV Fundamental / ML Modules** | github.com/DISTRHO/Cardinal, VCVRack/Fundamental, martin-lueders/ML_modules | GPLv3 | Quantiser variants |
| **Blue Cat plugnscript** | github.com/bluecataudio/plugnscript | permissive (per repo) | 48 AngelScript MIDI/audio scripts |
| **JUCE** | github.com/juce-framework/JUCE | AGPLv3 / commercial | `ArpeggiatorPluginDemo.h` — the canonical minimal MIDI-FX plug-in |
| **ShowMIDI** | github.com/pluginguru/ShowMIDI | GPLv3 | MIDI monitor UI reference |
| **firstpr pink-noise page** | firstpr.com.au/dsp/pink-noise | public write-up | Voss–McCartney code, Kellet filter |

---

## 5. Module ideas the incumbents don't offer

**Mapping & diagnostics**
1. **Dead-key meter / unmapped-note monitor** — live list of incoming notes that hit no
   destination, with hit counts, plus a "map coverage %" readout. The first question
   whenever a drum map is wrong; nobody offers it.
2. **Auto-map learner** — propose a mapping by fuzzy name match + GM fallback with a
   per-row confidence the user accepts/rejects.
3. **Nearest-articulation fallback** — instrument-aware: an unmapped Tom 4 falls back to
   the nearest mapped tom, not to silence. (This is the fallback chain of
   `docs/03-architecture.md`.)
4. **A/B map compare** — same input through two maps, alternate over N bars or split to
   two channels for double-tracking against two kits.

**Performance realism**
5. **Limb model** — assign each drum a limb (LH/RH/LF/RF); detect impossible
   simultaneities and resolve by displacement/drop/reassignment; drives flam
   hand-alternation and RR choice. The biggest "programmed vs played" tell after velocity.
6. **Per-instrument micro-timing ("groove DNA")** — push/pull in ms *per drum* (kick −4,
   snare +6, hats +2), independent of slot-based groove templates.
7. **Repetition detector / de-machine-gun** — N identical velocities on one pitch within
   a window → force minimum spread and an RR change.
8. **Ghost-note generator** — low-velocity snare/hat ghosts on free subdivisions with
   density, probability, ceiling, and a mask that protects the backbeat and played notes.
9. **Velocity→timing coupling ("urgency")** — `Δt = −U·(v − v̄)/127·A`: hard hits early,
   soft hits late (or the reverse). One knob, a genuine human trait.
10. **Performance-level dynamics AGC** — moving mean/σ of velocity → makeup toward a
    target; a *performance* normaliser, not a per-note compressor.
11. **Player-fatigue / arc envelope** — slow explicit drift of mean velocity and timing
    across a section.

**Kit mechanics**
12. **Choke-graph editor** — visible kills / killed-by matrix with per-pair choke time,
    "auto from GM" preset.
13. **Two-way hi-hat CC↔articulation bridge** (§3.10) incl. chick and splash synthesis.
14. **Kit-level voice budget with stealing** (oldest / quietest / lowest-priority).
15. **Round-robin bag with visible state + reset policy.**

**Workflow / determinism**
16. **Strip-wide Take ID** — one integer seeding every random module in all 16 slots
    (with the position hash of §3.6). Bump for a different-but-reproducible take; lock
    before bounce.
17. **Shared look-ahead bus with honest latency** — one global look-ahead serving flams,
    legato, negative groove offsets and pre-delay, reported once, all 16 channels
    phase-locked.
18. **Articulation state lamp + re-arm on locate.**
19. **Groove extraction from a live channel** — template from what the kick channel is
    actually doing, applied to the hats.
20. **CC de-stepper with chick preservation** — slew-limit steppy pedal CC but bypass the
    slew when |dCC/dt| exceeds a threshold.
21. **MIDI mute-with-tail** — mute a channel but let sustaining notes ring out.

### Orientation

Copy verbatim: **selectable distributions + user-drawn curves** (Frank), **Amount +
Weight + Seed** as the universal randomiser control set (Logic), **strength + safe-zone
+ randomise** as the universal quantiser control set (Cubase). The gaps — midiKITWARP's
opening — are **drum-map diagnostics**, **choke / round-robin / hi-hat mechanics as live
modules**, and **render-deterministic randomness**.
