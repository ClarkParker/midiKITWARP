# Dossier 05 — Articulation vocabulary of the major acoustic drum libraries

Task: extract the ARTICULATION vocabulary (names and distinctions, not note numbers) that
the big acoustic drum libraries actually use, and identify what KITWARP's pivot vocabulary
must be able to express that `marty-615/drum-remap`'s 40 `instrument/articulation` tags
cannot.

Date of research: 2026-09-06.

---

## 1. Scope and method

### 1.1 What was obtained, and how

| Library | Source actually used | Kind | Exhaustive? |
|---|---|---|---|
| **BFD3** | `fxpansion.com/webmanuals/bfd3/operationmanual/bfd3_key_map_reference.htm` (HTML table, parsed cell-by-cell) | **Vendor primary** | Yes — full default key map, 73 named articulations |
| **BFD3 (e-drum / CC)** | `.../using_electronic_drumkits.htm` | **Vendor primary** | Yes for the CC/variable-articulation model |
| **Toontrack Superior Drummer 3** | `SD Superior Drummer 3.drm` (Cubase drum map) from the Toontrack Drum Maps pack posted on the Steinberg forum; **independently corroborated** by `chad-ramos/studio-one-drum-maps` → `Superior Drummer 3.pitchlist` | Community-distributed, vendor-derived naming | 96 named articulations; naming convention `[Instrument] Articulation` matches Toontrack's own manual style |
| **Toontrack EZdrummer + 42 EZX libraries** | Same Toontrack Drum Maps pack (43 `.drm` files, incl. "Alias & GM Versions" variants) | Community-distributed, vendor-derived naming | Yes across the pack — this is the single richest articulation corpus found |
| **Toontrack EZdrummer (GM Extended layout)** | Official **EZdrummer operation manual PDF**, §4.4 "Key Mapping" (`images.thomann.de/pics/prod/221685_ezdrummer_manual.pdf`) | **Vendor primary** | Yes for the EZdrummer core layout |
| **XLN Addictive Drums 2** | Official **AD2 manual PDF** (`medias.audiofanzine.com/files/ad2-manual-472076.pdf`), pp. 37–43 | **Vendor primary** for the terminology + CC model | Partial — the "Stroketypes Explained" page is an image; per-note names taken from `drum-remap/maps/addictive-drums-2.json` |
| **NI Studio Drummer** | Official **manual PDF** §5 "Drum Articulations" | **Vendor primary** | Yes — complete, all 3 kits |
| **NI Abbey Road 60s Drums** | Official **manual PDF** §4 "Drum Articulations" | **Vendor primary** | Yes — complete, both kits |
| **Rayzoon Jamstix 4** | Official **manual PDF**, Appendix B "Kit Piece Reference IDs" + Appendix C "Output Mapping File Format" | **Vendor primary** | Yes — complete numbered pivot vocabulary |
| **GetGood Drums (M&M, M&M2, Invasion, P4)** | `chad-ramos/studio-one-drum-maps` pitchlists; `drum-remap/maps/ggd-*.json` | Community | Partial |
| **Steven Slate SSD5** | Official **SSD5 User Manual PDF**; `drum-remap/maps/ssd5.json` | Manual is primary for the *concepts*, names are community | Partial |
| **IK MODO Drum** | IK FAQ #1262 (public), Sound On Sound review | Vendor (partial) + press | No — full key map is an image in an account-gated manual |
| **MT Power Drum Kit 2** | `powerdrumkit.com` preset/drum-map pages; `drum-remap/maps/mt-power-drum-kit.json` | Vendor page + community | Partial |
| **ML Drums** | — | — | **NOT OBTAINED** |

### 1.2 What could not be obtained, and why

- **Toontrack SD3 / EZdrummer 3 official web manual** (`toontrack.com/manual/superior-drummer-3/`) — behind a
  Toontrack account login ("Please LOG IN to view Toontrack Manuals"). Toontrack forum topic pages
  returned HTTP 402 to the fetcher. **Workaround:** two independent third-party exports of Toontrack's
  own layout (a Cubase `.drm` set and a Studio One `.pitchlist`) that agree with each other and with the
  official EZdrummer PDF's naming convention. Marked accordingly below.
- **XLN Audio support site** (`support.xlnaudio.com`) and **Steven Slate support site**
  (`support.stevenslatedrums.com`) — Cloudflare interstitial, HTTP 403 to both WebFetch and curl with a
  browser UA. The official AD2 *keymap PDF* was therefore not retrieved; the AD2 *manual* PDF was.
- **GetGood Drums support** (`support.ggd.co`) — HTTP 403 (Zendesk + Cloudflare). No official GGD keymap
  or articulation list obtained. GGD data below is community-sourced.
- **IK MODO Drum user manual** — distributed only through IK's "My Products" account area. The public FAQ
  key-map is a bitmap diagram. MODO articulation *names* are therefore **UNVERIFIED**.
- **ML Drums** — ML Sound Lab publishes no public manual or keymap; Groove Monkee's "ML Drums Support"
  page contains no note table. **No ML Drums data in this dossier.**
- **BFD3 Operation Manual PDF** on CloudFront — HTTP 403. The HTML web manual was used instead.
- **Abbey Road 70s / Modern Drummer manuals** — the guessed NI PDF URLs 404'd (the server returned an
  HTML error page). Abbey Road data below is from the **60s** manual only.

### 1.3 Working files

- `scratch:dl/` — downloaded manuals and maps
- `scratch:dl/ttmaps/` — 43 Toontrack Cubase `.drm` files
- `docs/research/toontrack_buckets.json` — aggregated Toontrack instrument→articulation sets
- `scratch:repos/drum-remap/`, `.../repos/s1maps/` — cloned repos

---

## 2. The extracted vocabulary

Throughout: **bold** = the term is verbatim from a vendor-primary source; *italic* = community-sourced,
naming style consistent with the vendor but not confirmed against vendor documentation.

### 2.0 Each vendor's word for "articulation"

| Vendor | Their term |
|---|---|
| Toontrack | **articulation** (instruments carry articulations; layout shown in "MIDI Mapping Layout") |
| FXpansion / BFD | **articulation** ("each drum … features a number of articulations, each representing a way of playing the instrument") |
| XLN Audio | **stroke type** / **stroketype** (AD2 manual, "Stroketypes Explained") |
| Native Instruments | **articulation** ("Drum Articulations", per Drum) |
| Steven Slate | **articulation** ("Articulation Name", "Articulation Volume") |
| Rayzoon Jamstix | **kit piece** (a numbered slot) + **articulation** (a sound within a kit piece) |
| GGD | *articulation* (community usage) |

Jamstix is the important outlier: it does **not** separate instrument from articulation. Its pivot is a
**flat numbered list of 105 "kit piece reference IDs"** in which `Snare Rimshot` (4) and `Snare` (1) are
sibling IDs. That is exactly the design KITWARP must *not* copy — see §3.7.

---

### 2.1 KICK

| Normalised | Toontrack SD3 | Toontrack EZdrummer | BFD3 | AD2 | NI Studio Drummer | NI Abbey Road 60s | Jamstix 4 | GGD | SSD5 | drum-remap tag |
|---|---|---|---|---|---|---|---|---|---|---|
| normal hit | *`[Kick] Hit`* | **`[Kick] Right`** | **`Kick: Hit`** | `Kick` | **`Open`** | — | `Kick (Right Drum)` id 91 | *`Kick`* | *`Kick`* | `kick/hit` |
| second/left kick | — | **`[Kick] Left`** | — | — | — | — | `Kick (Left Drum)` id 90 | *`Kick Left`* | *`Kick Double`* | `kick/hit` + instance |
| damped/muffled hit | *`[Kick] Open`* vs `Hit` (two distinct articulations) | — | — | — | **`Dampened`** | — | — | — | — | **not expressible** |
| recorded with snares off | — | — | **`Kick: No Snare`** | — | — | — | — | — | — | **not expressible** |
| felt beater | — | — | — | — | — | **`Felt Beater`** | — | — | — | **not expressible** |
| rubber/wood/plastic beater | — | — | — | — | — | **`Rubber Beater`** | — | — | — | **not expressible** |
| heel-up / heel-down pedal technique | — | — | — | — | — | — | — | — | — | **not expressible** (MODO models it) |

Notes:
- Toontrack has **two** kick articulations, `Hit` and `Open`, at notes 35 and 36 in SD3 — a real timbral
  distinction (damped vs. open port), not an alias. drum-remap collapses both to `kick/hit`.
- MODO Drum offers **three beater types (felt, wood, plastic)** and **heel-up / heel-down** pedalling
  (Sound On Sound review); in MODO these are model parameters rather than named articulations, but from a
  remapping point of view they are the same distinction as Abbey Road's `Felt Beater` / `Rubber Beater`.
- BFD3's `Kick: No Snare` is a *recording state* of the whole kit (snare wires disengaged so the kick does
  not excite them), not a striking variation.

### 2.2 SNARE

| Normalised | Toontrack SD3 | Toontrack EZdrummer | BFD3 | AD2 | NI Studio Drummer | NI Abbey Road 60s | Jamstix 4 | GGD | SSD5 | drum-remap |
|---|---|---|---|---|---|---|---|---|---|---|
| centre hit | *`[Snare] Center`* | **`[Snare] Head`** | **`Snare: Hit`** | **`Open Hit`** | **`Center …`** | **`Center …`** | `Snare Center Hit` 38 | *`Sn Hit`* | *`Snare Center`* | `snare/hit` |
| mid-position hit | *`[Snare] Mid Center`* | — | — | — | **`Halfway …`** | **`Halfway …`** | — | — | — | **missing** |
| edge / shallow hit | *`[Snare] Edge`* | — | **`Snare: Half Edge`** | **`Shallow Hit`** | — | — | `Snare Offset Hit` 39 | — | — | **missing** |
| rimshot | *`[Snare] Rimshot`* | **`[Snare] Rimshot`** | **`Snare: Rim Shot`** | `Snare Rimshot` | **`Rimshot`** | **`Rimshot`** | `Snare Rimshot` 4 | *`Snare Hit`*-family | *`Snare Rimshot`* | `snare/rimshot` |
| sidestick / cross-stick | *`[Snare] Sidestick`* | **`[Snare] Sidestick`** | **`Snare: Side Stick`** | `Snare SideStick` | **`Sidestick`** | **`Sidestick`** | `Snare Side/Crosstick` 2 | *`Sn Side Stick`* | *`Snare Sidestick`* | `snare/sidestick` |
| rim only (stick on rim, no head) | *`[Snare] Rim Only`* | — | **`Snare: Rim Click`** | — | **`Rim Only`** | **`Rim Only`** | — | — | — | **missing — collides with sidestick** |
| flam | *`[Snare] Flam`* | — | **`Snare: Flam`** | — | **`Flam`** | **`Flam`** | — | *`Sn Flam`* | — | `snare/flam` |
| drag | — | — | **`Snare: Drag`** | — | — | — | `Snare Bounced` 3 | — | — | **missing** |
| ruff | *`[Snare] Ruffs`* | — | — | — | — | — | — | *`Sn Ruff`* | — | `snare/ruff` |
| roll (sustained/buzz) | — | — | — | — | **`Roll`** | **`Roll`** | — | — | — | **missing** |
| muted (hand on head) | *`[Snare] Thump`* | — | — | — | — | — | — | — | — | **missing** |
| damped with cloth | — | — | — | — | — | **`Tea Towel`** (Late 60s kit) | — | — | — | **missing** |
| snares disengaged | — | — | — | — | **`Wires Off`** | **`Wires Off`** | — | *`Sn Off`* | — | `snare/wires-off` |
| brush forward sweep | *`[Brushes] Fwd Swirl`*, *`[Brushes] Forward`* | **`[Brush] Full Circle`**, **`Half Circle`** | — | — | — | — | `Snare Brush Sweep` 6 | — | — | **missing** |
| brush backward sweep | *`[Brushes] Back Swirl`*, *`[Brushes] Backward`* | — | — | — | — | — | — | — | — | **missing** |
| brush tap L / R | **`[Brush] Left Tap`**, **`[Brush] Right Tap`** | ditto | — | — | — | — | — | — | — | **missing** |
| brush short drag | **`[Brush] Short Drag`** | — | — | — | — | — | — | — | — | **missing** |
| brush muted (no lift, damps head) | *`[Brushes] Muted Hit`* | **`[Brush] Muted`** | — | — | — | — | `Snare Brushed Muted` 5 ("brush hit *without lift* in order to mute the head") | — | — | **missing** |
| brush handle / sticks-in-brush | **`[Brush] Sticks`** | — | — | — | — | — | — | — | — | **missing** |
| hand: closed slap / open slap / closed rim / open rim | **`[Hand] Closed Slap` / `Open Slap` / `Closed Rim` / `Open Rim`** (EZX Nashville Hand Selection) | ditto | — | — | — | — | — | — | — | **missing** |
| left-hand vs right-hand stroke | **`[Snare] Left Hit` / `Right Hit`** | **`[Snare] Left` / `Right`** | — | — | **`Center Left Hand` / `Center Right Hand`** | ditto | — | — | — | **missing** |
| L/R alternating (speed-switched) | — | — | — | — | **`Center Right/Left Alternating`** | ditto | `Snare Offset Hit` 39 ("A.I. will use this sound for 16th L/R clusters") | — | — | **missing** |
| CC-resolved position note | *`[Snare] {CC} Position Trig`* | — | (positional CC crossfades `Hit`↔`Half Edge`) | (`CC Positional Snare` crossfades `Open Hit`↔`Shallow Hit`) | — | — | `[Snare] Controller=` in map file | — | — | **missing** |

Notes:
- **`Rim Only` vs `Sidestick` is a real distinction and drum-remap cannot hold both.** BFD3 calls the
  cross-stick `Rim Click` and has no separate rim-only articulation; Toontrack and NI have BOTH
  `Sidestick` and `Rim Only`. A single `snare/sidestick` tag therefore forces a lossy choice.
- Toontrack's brush notes live under a separate bracket `[Brushes]`/`[Brush]` even though they are played
  on the snare — i.e. Toontrack itself models *implement* as a pseudo-instrument. See §3.4.
- Jamstix's remark on `Snare Offset Hit` (id 39) shows the "offset/edge" articulation is also used as a
  **hand-alternation** device, not only a strike-position device.

### 2.3 TOMS

| Normalised | Toontrack SD3 | BFD3 | NI Studio Drummer | NI Abbey Road 60s | Jamstix 4 | drum-remap |
|---|---|---|---|---|---|---|
| centre hit | *`[Racktom 1..3] Center`*, *`[Floortom 1..2] Center`* | **`High/Mid/Floor Tom[ 2]: Hit`** | **`Center …`** | **`Center …`** | `Tom 1..5 Center Hit` 40–48 | `tom/hit` |
| offset hit | — | — | — | — | `Tom n Offset Hit` 41–49 | **missing** |
| rimshot | *`[Racktom n] Rimshot`*, *`[Floortom n] Rimshot`* | **`…: Rim Shot`** | **`Rimshot`** | **`Rimshot`** | — | **missing** |
| rim only / rim click | *`[Racktom n] Rim Only`* | **`…: Rim Click`** | **`Rim Only`** | **`Rim Only`** | — | **missing** |
| flam | **`[Racktom n] Flam`**, **`[Floortom n] Flam`** (EZX) | — | — | — | — | **missing** |
| towel-damped | — | — | — | **`Tea Towel`** / **`Towel`** | — | **missing** |
| L / R / alternating | **`[CHTom1..4] Left` / `Right` / `Head`** (EZX) | — | **`Center Left Hand` / `Right Hand` / `Right/Left Alternating`** | ditto | (implicit in Center/Offset) | **missing** |
| CC positional | (SD3 e-drum tom position) | (`[Tom] Controller=` supported by Jamstix maps) | — | — | `[Tom] Controller=` | **missing** |
| octoban | **`[Octoban 1] Center`**, **`[Octoban 2] Center`** (EZX) | — | — | — | — | **missing** |

**drum-remap has exactly one tom articulation (`tom/hit`).** Every library above has at least three
(`hit`, `rimshot`, `rim only`). This is the single largest coverage hole after percussion.

### 2.4 HI-HAT

This is the axis with the most vendor disagreement. Three orthogonal sub-axes are in play:
**(a) openness**, **(b) strike zone (bow/edge vs bell)**, **(c) stick contact point (tip vs shank/shaft)**.

#### 2.4.1 Openness ladders, side by side

| Openness step | Toontrack SD3 | Toontrack EZdrummer | BFD3 | AD2 | NI Studio Drummer / Abbey Road | SSD5 | GGD M&M | Jamstix 4 |
|---|---|---|---|---|---|---|---|---|
| pedal fully down, foot chick | *`Closed Pedal`* | **`Pedal Chick`** | **`Pedal`** | `HiHat Pedal Closed` (**`Foot Close`**) | **`Closed Pedal`** | *`Hi-Hat Pedal`* | *`Hat Pedal Chick`* | `Hihat Foot Close` 9 |
| foot splash | *`Open Pedal`* | **`Foot Splash`** | **`Splash`** | (**`Foot Splash`**) | **`Open Pedal`** | *`Hi-Hat Footsplash`* | *`Hat Ching`* | `Hihat Foot Splash` 10 |
| very tight | *`Tight Tip` / `Tight Edge`* | **`Tight` / `Tight Tip`** | — | `HiHat Closed 1 Tip/Shaft` | **`Closed Tight Tip …`** | *`… Closed Tight`* | *`Hat Tight`* | — |
| closed | *`Closed Tip` / `Closed Edge`* | **`Closed Tip` / `Closed Edge`** | **`Closed Tip` / `Closed Shank`** | `HiHat Closed 2 Tip/Shaft` | **`Closed Tip …` / `Closed Shank …`** | *`… Closed`* | *`Hat Closed`* | `Hihat Closed` 50 |
| closed but loose | — | — | — | — | — | *`… Loosen`* | *`Hat Closed Loose`* | — |
| open level 0 | *`Open Tip 0`*, *`Open Edge 0`*, *`Open Min`* | **`Open Min`** | — | — | — | — | *`Hat Open0`* | — |
| open 1 (¼) | *`Open Tip 1`*, *`Open Edge 1`*, *`Open 1`* | **`Open 1`** | **`1/4 Tip` / `1/4 Shank`** | `HiHat Open A` | **`Open Quarter`** | *`… Open 1`* | *`Hat Open1`* | `Hihat 25% Open` 51 |
| open 2 (½) | *`Open Tip 2`*, *`Open Edge 2`*, *`Open 2`* | **`Open 2`** | **`Half Tip` / `Half Shank`** | `HiHat Open B` | **`Open Half`** | *`… Open 2`* | *`Hat Open2`* | `Hihat 50% Open` 52 |
| open 3 (¾) | *`Open Tip 3`*, *`Open Edge 3`*, *`Open 3`* | **`Open 3`** | **`3/4 Tip` / `3/4 Shank`** | `HiHat Open C` | **`Open Three-Quarters`** | *`… Open 3`* | *`Hat Open3`* | `Hihat 75% Open` 53 |
| open 4 | *`Open Tip 4`*, *`Open Edge 4`* | — | — | — | **`Open Loose`** | — | — | — |
| open 5 / max | *`Open Tip 5`*, *`Open Max`* | **`Open Max`** | **`Open Tip` / `Open Shank`** | `HiHat Open D` | **`Open Full`** | — | — | `Hihat Open` 54 |
| CC-driven variable | *`{CC} Tip Trig`, `{CC} Edge Trig`, `{CC} Bell Trig`, `{CC} Shaft Trig`*; **`[Hats] CC Variable`** | **`[Hats] CC Variable`** | **`Variable Tip` / `Variable Shank`** | **CC HiHat stroketypes** | **`Open Controller`** | (Hi-Hat Pedal Control CC) | *`Hats CC`* | `Hihat (Dynamic Open)` 8 |
| sequenced hits | *`Seq Hits`* | **`Seq Hard` / `Seq Soft`** | — | — | — | — | — | — |

**Findings:**
- The number of openness steps is **not 3, and not the same anywhere**: Toontrack SD3 exposes
  **6 tip levels (Open Tip 0–5)**, **5 edge levels (Open Edge 0–4)** and **5 bell levels
  (Open Bell 0–4)** plus `Open Min` / `Open Max`. drum-remap's `open-0 … open-3` + `open` tops out at 5
  steps and has no per-zone variant at all.
- BFD3 names steps as **fractions** (`1/4`, `Half`, `3/4`), NI as **words** (`Quarter`, `Half`,
  `Three-Quarters`, `Loose`, `Full`), Toontrack and SSD5 as **ordinals**, Jamstix as **percentages**
  (`25% / 50% / 75%`), AD2 as **letters** (`Open A/B/C/D`). All five are the same underlying axis.
- `Open Loose` (NI) and `Closed Loose`/`Loosen` (SSD5, GGD) are *different* things: NI's is between ¾ and
  full; SSD5/GGD's is between closed and ¼. drum-remap has one tag, `hihat/closed-loose`, and
  `ssd5.json` uses it for BOTH `Hi-Hat Tip Loosen` and `Hi-Hat Shank Loosen`, which is a collision.

#### 2.4.2 The hi-hat bell — a whole zone drum-remap has no room for

Toontrack SD3 has **6 hi-hat bell articulations**: *`Closed Bell`, `Open Bell 0`, `Open Bell 1`,
`Open Bell 2`, `Open Bell 3`, `Open Bell 4`*, plus a *`{CC} Bell Trig`*. BFD3 has **`Hihat: Bell Tip`**.
drum-remap has no hi-hat bell tag whatsoever. (drum-remap's `megabell` instrument is a *different*
physical thing — an oversized ride bell.)

#### 2.4.3 Tip vs shank on the hi-hat

BFD3 pairs **every** openness level with **Tip** and **Shank** (10 combinations + `Pedal`, `Splash`,
`Bell Tip`). SSD5 and AD2 do the same with `Tip`/`Shank` and `Tip`/`Shaft`. NI uses
`Closed Tip` vs `Closed Shank`. Toontrack SD3 uses `Tip` vs `Edge` for the strike zone, and separately
uses `Shaft` for the CC trigger note. Jamstix has a *partial* shank ladder
(`Hihat Shank Closed` 92, `Hihat Shank 50% Open` 94, `Hihat Shank Open` 96, with 93 and 95 RESERVED).

drum-remap encodes tip/edge inside the articulation string for a few levels
(`closed-tip`, `closed-edge`, `tight-tip`, `tight-edge`) but **not** for the open levels, and
`ssd5.json`/`addictive-drums-2.json` are forced to smuggle it into `instance: "shank"` — the
inconsistency the brief already flagged.

### 2.5 RIDE

| Normalised | Toontrack SD3 | Toontrack EZdrummer | BFD3 | AD2 | NI Studio Drummer | Jamstix 4 | SSD5 | GGD | drum-remap |
|---|---|---|---|---|---|---|---|---|---|
| bow, stick tip | *`[Ride] Bow Tip`* | **`[Ride] Bow`** / **`[Ride] Tip`** | **`Ride 1: Bow`** | `Ride 1 Tip` (**`Ride Tip`**) | **`Tip`** | `Ride` 12 | *`Ride Bow Tip`* | *`Ride Tip`* | `ride/bow` |
| bow, stick shank | *`[Ride] Bow Shank`* | **`[Ride] Shank`** / **`[Ride] Ride Shank`** | — | `Ride 1 Shaft` (**`Ride Shaft`**) | — | — | *`Ride Bow Shank`* | — | **collides — `instance:"shank"`** |
| bell, stick tip | *`[Ride] Bell Tip`* | — | — | — | — | — | — | — | **missing** |
| bell, stick shank | *`[Ride] Bell Shank`* | **`[Ride] Bell`** | **`Ride 1: Bell`** | `Ride 1 Bell` | **`Bell`** | `Ride Bell` 13 | *`Ride Bell`* | *`Ride Bell`* | `ride/bell` |
| edge / crash the ride | *`[Ride] Crashed`* | **`[Ride] Edge`** | **`Ride 1: Edge`** | — | **`Edge`** | — | *`Ride Edge`* | *`Ride Crash`* | `ride/crash` |
| muted | *`[Ride] Muted`* / **`[Ride] Mute`** | — | — | — | — | — | — | — | **missing** |
| crescendo / swell | **`[Ride] Crescendo`** | — | — | — | — | — | — | — | **missing** |
| choke | — | — | **`Ride 1: Choke`** | `Ride 1 Choke` | **`Choke`** | `Cymbal Choke` 55 | *`Ride Choke`* | — | `ride/choke` |
| rimshot (stick across the edge) | **`[Ride] Rimshot`** (EZX) | — | — | — | — | — | — | — | **missing** |
| sizzle ride (separate instrument) | — | — | — | — | — | — | — | — | **`Sizzle Ride`** (Abbey Road 60s) — **missing** |

**The 2×2 is the headline.** Toontrack SD3 exposes `Bow Tip`, `Bow Shank`, `Bell Tip`, `Bell Shank` as
four distinct articulations on the ride and on **every** cymbal slot 1–5. This proves that
**strike zone (bow / bell / edge) and stick contact point (tip / shank) are two independent axes**, not
one. drum-remap models the zone as `articulation` and is then forced to model the contact point as
`instance` — which is wrong (it is not a different piece of hardware) and cannot represent
`Bell Tip` at all.

AD2 also confirms zone-vs-contact independence from the other direction: its **`CC Positional Ride`**
crossfades between `Ride Tip` and `Ride Shaft` based on a positional CC — i.e. AD2 treats tip/shaft as a
*position on the cymbal*, whereas Toontrack treats it as *part of the stick*. Both readings must survive
a round-trip, so the pivot must keep the pair as one axis with a documented meaning.

### 2.6 CRASHES, CHINA, SPLASH, STACKS, OTHER CYMBALS

| Normalised | Toontrack SD3 (`[Cymbal 1..5]`) | Toontrack EZdrummer | BFD3 | NI Studio Drummer | AD2 | GGD | drum-remap |
|---|---|---|---|---|---|---|---|
| crash hit | *`Crashed`* | **`[Crash A] Crashed`**, **`[Crash B] Crashed`** | **`Crash n: Hit`** | **`Edge`** | `Cymbal n Hit` | *`Crash L/R Crash`* | `crash/hit` |
| bow | *`Bow Tip` / `Bow Shank`* | — | **`Crash n: Bow`** | **`Tip`** | — | — | **missing** |
| edge | (= `Crashed`) | — | **`Crash n: Edge`** | **`Edge`** | — | — | **`crash/hit` conflates edge and bow** |
| bell | *`Bell Tip` / `Bell Shank`* | — | **`Crash n: Bell`** | **`Bell`** | — | *`Bell L` / `Bell R`* | **missing (mapped to `megabell`)** |
| muted / mute hit | *`Muted`*, **`{Mute}`** | **`[Crash A] Muted`** | — | — | — | — | **missing — conflated with choke** |
| choke | (`Muted` used for this) | — | **`Crash n: Choke`** | **`Choke`** | `Cymbal n Choke` | *`Crash L/R Choke`* | `crash/choke` |
| crescendo / swell | **`[Cymbal 1/2] Crescendo`**, **`[Crash Rd 1] Crescendo`** | — | — | — | — | — | **missing** |
| circling (stick circling on the bow) | **`[CrashrB] Circling`** (EZX) | — | — | — | — | — | **missing** |
| china | *`[China] Crashed`*, **`[China 2] Bow` / `Edge` / `Crashed` / `Muted`** | **`[China] Crashed`** | (generic `Cymbal n`) | **`Edge` / `Tip` / `Choke`** | — | *`China Main Hit` / `China Choke`* | `china/hit`, `china/choke` |
| splash | **`[Splash 1..3] Crashed`**, **`[Splash] Muted`** | ditto | (generic) | **`Edge` / `Choke`** | — | *`Splash Main Hit` / `Splash Choke`* | `splash/hit`, `splash/choke` |
| crash-ride | **`[Crash Rd 1] Bell/Bow/Crashed/Crescendo/Edge`**, **`[Crash Ride] Bell/Bow/Crashed/Muted`** | ditto | — | — | — | — | **missing (a distinct instrument)** |
| stack / x-hat | **`[XHats] Closed`**, **`[DKHats] Closed`**, **`[HH Group] Closed/Open/Small`** | ditto | — | — | — | *`Stack`*, *`Mini Hats`*, *`X-Hats Closed/Open`* | `stack/hit`, `xhat/closed`, `xhat/open` |
| generic "cymbal" slot count | **5 numbered cymbal slots + ride** in SD3; BFD3 has **Crash 1–2 + Cymbal 1–3 + Ride 1** | | | | | | drum-remap has crash/china/splash/stack + instances |

**Muted ≠ Choked.** Toontrack has both `Muted` (a hit with the other hand damping) and, at the same
time, uses `Muted` where other libraries send a `Choke`. BFD3 keeps them separate (`Hit` vs `Choke`).
NI/GGD/AD2/SSD5 have only `Choke`. drum-remap has only `choke`. A pivot that cannot say "muted hit"
loses Toontrack's `[Cymbal n] Muted` on every crash.

**Slot naming is inconsistent across every source**: BFD3 has `Crash 1/2` *and* `Cymbal 1/2/3`;
Toontrack SD3 has `Cymbal 1..5` with no type in the name at all (the type is a property of the loaded
cymbal); GGD uses `Main Crash L/R` + `Wide Crash L/R`; SSD5 uses `Crash Left/Right`. drum-remap's
`instance` values (`left`, `right`, `far-left`, `far-right`, `1`, `2`, `3`) are an attempt to unify these
and are, as the brief says, inconsistent.

### 2.7 PERCUSSION — the total blind spot

drum-remap has exactly **one** percussion instrument: `cowbell`. The Toontrack `.drm` corpus alone
contains the following percussion instrument buckets, each with its own articulation set (verbatim
bracket names from the maps):

`Afuche` (Beat) · `Bells` (Crescendo, Gliss Fast, Gliss Slow, Hit, Single 1–5, Sleigh Large, Sleigh
Small) · `Body` (Chest Hit, Hand Breath, Hand Claps, Hands Body, Mth OffBeat, Mth OnBeat, Stairstep, Zip
OffBeat, Zip OnBeat) · `Body Sounds` (Big Claps, Crowd Snaps, Single Snaps, Stomps) ·
`Bongo 1/2` (Crescendo, Flam, Left Heel, Left Open, Right Heel, Right Open) · `Bowl` (Hit) ·
`Cabasa` (Beat, Long, On Beat, Short) · `Cajon` (Brush Hit L/R, Crescendo, Flam, Left Brush, Left Ghost,
Left Side, Right Bass, Right Brush, Right Ghost, Right Side) · `Cajon Slap` (Left Mid, Left Normal,
Right Mid, Right Normal) · `Caxixi` (Beat, FX, Off Beat, On Beat) · `Chimes` (Down, Stroke, Up) ·
`Clangers` (Hand, Muted, Open) · `Clappers` (Hit, Off Beat, On Beat) · `Claps` (Hit) ·
`Conga 1` (Closed Slap L/R, Crescendo, FX, Flam, Left Bass, Left Heel, Left Muted, Left Open, Open Slap
L/R, Right Bass, Right Heel, Right Muted, Right Open, Slap Cresc, Slap Flam) · `Conga 2` (subset) ·
`Crickets` (Crescendo, Stroke) · `Djembe` (Head, Left, Right) · `Fingers` (Index, Middle, Palm, Ring,
Thumb) · `FX Box` (Bell Tree, Castanet, Chimes, Dry FX 1/2, Flexatone, Lightning, Ocean Side, Ocean
Sound, Rain Stick, Ratchet, Thunder 1/2, Vibraslap, Whip Flam, Whip Single) · `FXBox` (Accordeon, Cow
Moo, Duck Quack, Ratchet, Siren Long/Short, Thunder Hit, Thunder SkR, Train Long/Short) ·
`Guiro` (Long, Short) · `Hand` (Closed Rim, Closed Slap, Open Rim, Open Slap) ·
`HandDrum` (Center, Edge/Rim) · `HndDrm` (Muted, Open) · `Maracas` (Beat, Off Beat, On Beat, Shake) ·
`Mouth` (Off Beat, On Beat) · `Octoban 1/2` (Center) · `Rattles` (Crescendo, Off Beat, On Beat) ·
`Shaker` (Crescendo, Hit, Off Beat, On Beat, Shake) · `Shaker 1/2` · `Shekere` (Beat, Off beat, On Beat,
Shake) · `Shells` (On Beat) · `Snaps` (Hit) · `Spikes` (On Beat) · `Sticks` (Count-ins) ·
`Tamb`/`Tambourine` (Bell, Crescendo, Hands, Hit, Muted Hit, Off Beat, On Beat, Open Hit, Sticks) ·
`Timbale 1/2` (Flam, Left Open, Right Open, Rimshot, Ruff, Sidestroke) · `Triangle` (Long, Muted, Open,
Short) · `Tribal` (Bass Drum, Boobam) · `Udu` (Flam, Left Ghost, Muted Slap, Open Cresc, Open High, Open
Low, Open Slap, Right Ghost, Slap Cresc) · `Vibraslap` (Hit, Stroke) · `Waterfall` (Crescendo, Stroke) ·
`Woodblock` (Block 1–5, Hit, Stick)

NI Studio Drummer adds: **`Tambourine` (Tap, Shake)**, **`Clap` (Solo, Multi)**, **`Stick Hit` (Hit)**,
**`Cowbell` (Open, Muted)**, **`High/Low Woodblock` (Hit)**, **`High/Low Cowbell` (Open, Muted)**.
Jamstix adds a generic percussion abstraction (see §2.9).

Note the recurring **`On Beat` / `Off Beat`** pair across ~10 shaker-family instruments: for hand
percussion the *phase of the shake* is a first-class articulation, and it has no analogue anywhere in a
drum-kit vocabulary.

### 2.8 CROSS-CUTTING MECHANISMS THE LIBRARIES IMPLEMENT

#### 2.8.1 Controller-resolved articulation ("variable" notes)

Every serious library has notes whose articulation is decided at play time by a controller value, not by
the note number. This is a **distinct kind of vocabulary entry** and drum-remap has no concept of it.

| Library | Note name(s) | Controller | Behaviour |
|---|---|---|---|
| Toontrack SD3 | *`[Hi-Hat] {CC} Tip Trig`, `{CC} Edge Trig`, `{CC} Bell Trig`, `{CC} Shaft Trig`*; **`[Hats] CC Variable`** | hi-hat pedal CC | note says *where* you hit; CC picks the openness level |
| Toontrack SD3 | *`[Snare] {CC} Position Trig`* | snare position CC | CC picks centre↔edge |
| BFD3 | **`Variable Tip`**, **`Variable Shank`** | default **CC #4**, 0 = open, 127 = fully down; 5 zones with adjustable transition points | picks one of the 5 openness articulations |
| BFD3 | (snare) | typically **CC #17** on Roland | crossfades `Hit` ↔ `Half Edge` at an adjustable threshold |
| AD2 | **`CC HiHat` stroketypes** | **CC #4** (+ optional secondary CC) | "AD cares only about where you hit the pad (bow or edge) and your current pedal position"; node graph sets transition values |
| AD2 | `CC Positional Snare` | **CC #16** default, reversible, with crossfade width and velocity compensation | crossfades `Snare Open Hit` ↔ `Snare Shallow Hit` |
| AD2 | `CC Positional Ride` | positional CC | crossfades `Ride Tip` ↔ `Ride Shaft` |
| NI Studio Drummer / Abbey Road | **`Open Controller`** | **CC #1 modwheel or CC #4** | "At the 0 position … plays the fully open hi-hat. As the controller sends higher values … gradually more closed" — **note the inverted polarity vs BFD3** |
| MODO Drum | **CC TIP / CC SHANK** | user-definable | continuously varies tip and shank hits from fully closed to fully open |
| MODO Drum | — | **CC4** pedal (invert ON), **CC16** snare position, **CC18** tom position (Roland TD-20 example) | |
| Jamstix 4 | `Hihat (Dynamic Open)` id 8 — "Pedal pressure controls open level"; vs `Hihat Closed` id 50 — "Pedal pressure is **not** considered" | `[Hihat] UseCC=`, `Controller=` (usually #4) in the map file | two *kinds* of hi-hat note in the same vocabulary |
| SSD5 | "Hi-Hat Pedal Control" (foot CC) vs "Hi-Hat MIDI Control" (mod wheel) | ch.4 typical | |
| GGD | *`Hats CC`* note | hi-hat CC | |

**Polarity is not agreed**: BFD3 says CC 0 = pedal up/open, rising = closing. NI says controller 0 = fully
open, rising = more closed (same direction). AD2 and MODO both ship an explicit **CC Reverse / Invert**
switch precisely because hardware disagrees. Any pivot that stores "hi-hat openness" as a controller
value must store the polarity convention with it.

#### 2.8.2 Choke by aftertouch, not by note

- AD2: "For certain edrum kits, the cymbals send out **aftertouch** midi messages when they are firmly
  grabbed … these aftertouch messages are set to trigger the cymbal choke stroketypes."
- Jamstix output map format: `AfterTouchChoke=1`, alongside `CH_[ReferenceID]=Key` for choke-by-note.
- NI: "Cymbal choke samples are triggered by specific note assignments which play **release samples** …
  If no cymbal sound is currently active, then the cymbal choke notes will do nothing."

So a choke is (a) sometimes a note, (b) sometimes channel aftertouch, and (c) semantically a *modifier on
a previous note*, not a sound of its own. Jamstix makes this explicit: `Cymbal Choke` id 55 — "Will choke
the **last cymbal played with the same hand**."

#### 2.8.3 Hand assignment (L / R / alternating)

NI Studio Drummer and Abbey Road expose `… Left Hand`, `… Right Hand`, and `… Right/Left Alternating` as
**separate articulations with separate note assignments** for snare centre, snare halfway, tom centre and
closed hi-hat. Toontrack EZX maps expose `[Snare] Left` / `[Snare] Right`, `[AltSnr] Left/Right`,
`[CHTom1..4] Left/Right`, `[Bongo 1] Left Open/Right Open`, `[Conga 1] Left Bass/Right Bass`, etc.
Jamstix resolves it internally (`Snare Center Hit` vs `Snare Offset Hit`, the latter "used for 16th L/R
clusters"). MODO models "playing position, diameter and stick tips … for left and right hands
individually."

drum-remap has no hand axis at all.

#### 2.8.4 Alias notes and GM-compatibility duplicates

Toontrack ships two versions of every map: a plain one and an **"Alias & GM Versions"** one in which
extra notes are labelled `[Kick] alias`, `[Snare] alias`, `[Cymbal 1] alias`, and GM anchor notes are
labelled `[Hats]{GM} Closed` (42), `[Hats]{GM} Pedal` (44), `[Hats]{GM} Open` (46). The official
EZdrummer manual documents the same: notes 34, 35, 41, 45, 50, 52, 55 are `alias` and
"all notes in this range are GM compliant with the following exceptions: 39, 54, 58, 60."

An alias is **a second note number producing the identical articulation**. A pivot must be able to mark a
layout entry as *non-canonical* so that a round-trip does not fan one source note out into several target
notes, and so that inversion picks the canonical one. drum-remap's `ssd5.json` hits this already — it
carries `Hi-Hat Tip Closed (GM)` and `Hi-Hat Pedal (GM)` with a made-up `instance: "gm"`.

#### 2.8.5 Implement (stick / brush / rod / hand / mallet)

Toontrack models the implement as a **pseudo-instrument bracket**: `[Brushes]`, `[Brush]`, `[Hand]`,
`[Fingers]`, `[Sticks]`, `[Special] Sticks`. EZX Nashville ships as three separate maps —
`EZX Nashville.drm`, `EZX Nashville (Hand Selection).drm`, `EZX Nashville (Brush-Snare Selection).drm` —
i.e. the *same kit* with a different implement produces a *different layout*. Vintage Rock likewise ships
`(Brushes)` and `(Snare)` variants. Jamstix carries `Snare Brushed Muted` (5) and `Snare Brush Sweep` (6)
as first-class kit-piece IDs. Abbey Road carries kick **beater type** (`Felt Beater` / `Rubber Beater`)
as an articulation.

### 2.9 Jamstix 4 — a rival pivot vocabulary, verbatim

Because Jamstix ships its own maps for many libraries, its internal IDs are directly comparable to what
KITWARP is building. Full drum-kit table (Appendix B, Jamstix 4 manual, pp. 73–74):

| ID | Kit Piece | Vendor remark |
|---|---|---|
| 0 | Kick | |
| 1 | Snare | "At play time, this sound is resolved to center or offset hit by the A.I." |
| 2 | Snare Side/Crosstick | |
| 3 | Snare Bounced | |
| 4 | Snare Rimshot | |
| 5 | Snare Brushed Muted | "brush hit without lift in order to mute the head" |
| 6 | Snare Brush Sweep | |
| 7 | RESERVED | |
| 8 | Hihat (Dynamic Open) | "Pedal pressure controls open level" |
| 9 | Hihat Foot Close | |
| 10 | Hihat Foot Splash | |
| 11 | RESERVED | |
| 12 | Ride | |
| 13 | Ride Bell | |
| 14 | RESERVED | |
| 15–18 | Crash 1–4 | |
| 19–21 | Splash 1–3 | |
| 22–25 | China 1–4 | |
| 26 | RESERVED | |
| 27–31 | Tom 1–5 | "resolved to center or offset hit by the A.I." |
| 32–33 | Jam Block Hi / Lo | |
| 34 | Chimes | |
| 35 | Cowbell | |
| 36 | Tambourine | |
| 37 | Drumsticks | |
| 38 | Snare Center Hit | |
| 39 | Snare Offset Hit | "used for 16th L/R clusters" |
| 40–49 | Tom 1–5 Center Hit / Offset Hit | |
| 50 | Hihat Closed | "Pedal pressure is not considered" |
| 51–53 | Hihat 25% / 50% / 75% Open | |
| 54 | Hihat Open | |
| 55 | Cymbal Choke | "Will choke the last cymbal played with the same hand" |
| 56–57 | Egg Shaker / Metal Shaker | |
| 58–89 | *(Jamcussion range — see below)* | |
| 90 | Kick (Left Drum) | "the 2nd kick (left in drummer view)" |
| 91 | Kick (Right Drum) | "the main kick and only kick in a single kick drum setup" |
| 92 | Hihat Shank Closed | |
| 93 | RESERVED | |
| 94 | Hihat Shank 50% Open | |
| 95 | RESERVED | |
| 96 | Hihat Shank Open | |
| 97 | 2nd Snare | |
| 98 | 2nd Snare Side/Crosstick | |
| 99 | 2nd Snare Bounced | |
| 100 | 2nd Snare Rimshot | |
| 101 | 2nd Snare Brushed Muted | |
| 102 | 2nd Snare Brush Sweep | |
| 103 | 2nd Snare Center Hit | |
| 104 | 2nd Snare Offset Hit | |

Jamcussion (generic percussion abstraction) — IDs 58–89:
`Drum 1..4 × {Center, Medium/Open, Rim/Slap, Hit & Mute}` (58–73) and
`Percussion 1..8 × {Main, Alternate}` (74–89).

Jamstix's output-map file format (Appendix C) is itself a mini schema worth copying the shape of:
```
[Keys]      0=36                      ; reference-ID → MIDI key
[Hihat]     UseCC=1  Controller=4     ; pedal-pressure CC
[Snare]     Controller=<n or 0>       ; head-position CC, 0 = unsupported
[Tom]       Controller=<n or 0>
[Chokes]    CH_15=13                  ; choke-by-key, per reference ID
            AfterTouchChoke=1         ; or choke-by-aftertouch
[Drum Kit]  ShortName= / LongName=
```

**Lessons from Jamstix, positive and negative:**
- Positive: stable numeric IDs; explicit RESERVED slots for forward compatibility; controller config is
  *part of the map*, not of the plugin; choke is modelled as a separate mechanism.
- Negative: the ID space is flat (instrument and articulation fused), so `Snare` (1), `Snare Rimshot` (4)
  and `Snare Center Hit` (38) are unrelated integers; new articulations had to be bolted on at 38–57 and
  90–104 in later versions, leaving the numbering non-monotonic; percussion is reduced to anonymous
  `Percussion n Main/Alternate` slots that carry no semantics at all, so nothing can be inferred when
  remapping between two libraries' congas.

---

## 3. Implications for the KITWARP pivot vocabulary

### 3.1 The evidence says the pivot needs at least these axes

| Axis | Evidence | drum-remap status |
|---|---|---|
| **instrument** (family) | all | present, 12 values — too few (no crash-ride, no sizzle ride, no octoban, essentially no percussion) |
| **instance** (which physical piece) | `Cymbal 1..5`, `Crash 1/2` + `Cymbal 1/3`, `Racktom 1..3`, `Floortom 1/2`, `2nd Snare`, `Kick Left/Right`, `Bongo 1/2`, `Conga 1/2`, `Timbale 1/2`, `Shaker 1/2` | present but ad-hoc and polluted with non-instance values (`shank`, `gm`) |
| **zone** (where on the piece) | `Center` / `Mid Center` / `Edge` / `Half Edge` / `Shallow` / `Rim` / `Bow` / `Bell` / `Cup`; hi-hat `Bell` | conflated into `articulation` |
| **contact** (part of the implement) | `Tip` / `Shank` / `Shaft` — orthogonal to zone (proved by SD3's `Bow Tip`/`Bow Shank`/`Bell Tip`/`Bell Shank`) | **absent**; smuggled into `instance` |
| **technique / stroke** | `Hit`, `Rimshot`, `Rim Only`/`Rim Click`, `Sidestick`, `Flam`, `Drag`/`Bounced`, `Ruff`, `Roll`, `Swirl`, `Sweep`, `Circling`, `Crescendo`, `Choke`, `Mute`, `Slap`, `Heel`, `Sidestroke`, `On Beat`/`Off Beat`, `Shake`, `Gliss` | partly present, most missing |
| **openness** (hi-hat, continuous) | 6 tip levels + 5 edge levels + 5 bell levels in SD3; 5 in BFD3; 5 in NI; 4 in AD2; 4 in Jamstix; percent/fraction/word/ordinal/letter naming | present but capped and un-crossed with zone |
| **implement** | stick / brush / rod / hand / fingers / mallet; kick beater felt/rubber/wood/plastic | **absent** |
| **hand** | `Left Hand` / `Right Hand` / `Right/Left Alternating` | **absent** |
| **damping / kit state** | `Wires Off`, `No Snare`, `Tea Towel`/`Towel`, `Dampened`, `Muted`, `Thump` | only `wires-off` |
| **dynamics tier** | `Seq Hard` / `Seq Soft`, `Ghost` (`Left Ghost`/`Right Ghost` in Cajon/Udu) | partially in `role` (`ghost`) — but `role` is a *musical function*, not a sample tier; these should not be the same field |
| **controller-resolved** flag + CC number + polarity | §2.8.1 | **absent** |
| **entry status** (canonical / alias / GM-anchor / trigger-only / reserved) | §2.8.4, Jamstix RESERVED | **absent** |
| **provenance** | — | **absent** (already flagged) |

### 3.2 Distinctions drum-remap's 40 tags provably cannot express

Ranked by how often they occur in real layouts:

1. **Tom rimshot and tom rim-only.** Every library has them; drum-remap has only `tom/hit`.
   (BFD3 alone has 12 tom articulations in its default map: 6 `Hit`, 6 `Rim Shot`… plus 6 `Rim Click`.)
2. **`Rim Only` as distinct from `Sidestick`.** Toontrack, NI and BFD3 all distinguish them.
3. **Cymbal bow vs edge vs bell on crashes.** BFD3 has `Crash n: Bow`, `Edge`, `Bell`, `Hit`;
   NI has `Edge`, `Tip`, `Bell`; drum-remap has `crash/hit`.
4. **Ride `Bell Tip` (and the whole zone × contact 2×2).**
5. **`Muted` cymbal hit vs `Choke`.**
6. **Hi-hat bell** (SD3: `Closed Bell` + `Open Bell 0–4`; BFD3: `Bell Tip`).
7. **Hi-hat openness beyond 3 open levels** and per-zone openness ladders.
8. **Brush articulations**: forward/backward sweep, swirl, half/full circle, short drag, left/right tap,
   muted (no-lift) hit, brush-handle sticks. Jamstix, Toontrack and NI all carry them.
9. **Snare buzz/roll** (`Roll` in NI/Abbey Road) and **drag** (`Drag` in BFD3, `Snare Bounced` in Jamstix).
10. **Snare mid/edge positions** (`Mid Center`, `Edge`, `Half Edge`, `Shallow Hit`, `Halfway`).
11. **Kick beater type** (`Felt Beater`/`Rubber Beater`; MODO felt/wood/plastic) and
    **kick damped vs open** (`Dampened`/`Open`, SD3 `Hit`/`Open`).
12. **Kick recorded with snares off** (`Kick: No Snare`).
13. **Hand assignment** L/R/alternating.
14. **Crescendo / swell** on ride, cymbals, congas, bongos, cajon, tambourine, shaker, bells, rattles,
    crickets, waterfall — a very widely used Toontrack articulation.
15. **Damping accessory state** (`Tea Towel`, `Towel`) on snare and toms.
16. **All percussion** beyond cowbell (§2.7) — ~45 instrument families, ~200 articulations in the
    Toontrack corpus alone.
17. **Controller-resolved trigger notes** (§2.8.1) — these are *notes in the layout* that have no fixed
    articulation, and there is currently no way to represent one.
18. **Alias / GM-anchor notes** (§2.8.4).
19. **Crash-ride and sizzle-ride as instruments**, `Octoban`, `Jam Block`, `Boobam`.
20. **Shaker phase (`On Beat` / `Off Beat`)** — a genuine articulation for hand percussion.

### 3.3 Distinctions that are cosmetic, and should be normalised away

- **Openness naming**: `1/4` (BFD3) = `Open Quarter` (NI) = `Open 1` (Toontrack) = `Open A` (AD2) =
  `Hihat 25% Open` (Jamstix) = `Open 1` (SSD5/GGD). One axis; store a **normalised fraction or ordinal**
  and keep the vendor string only as a display label.
- **`Shank` vs `Shaft`**: BFD3/NI/SSD5 say Shank, AD2 and SD3's CC note say Shaft. Same thing.
- **`Rim Click` (BFD3) vs `Sidestick` (everyone else)** — same thing *when the library has only one of
  them*; genuinely different when a library has both. The pivot needs both terms so that "BFD3 has no
  rim-only" is representable as a fallback, not as an identity.
- **`Crashed` (Toontrack) vs `Hit` (BFD3/GGD) vs `Edge` (NI)** for the ordinary crash stroke.
- **`Center` vs `Head` vs `Open Hit` vs `Hit`** for the ordinary snare stroke.
- **`Ruff` vs `Drag` vs `Bounced`** — musically these are *not* identical (a ruff is normally 3+ grace
  notes, a drag 2), but BFD3 has `Drag` and no `Ruff` while Toontrack/GGD have `Ruffs` and no `Drag`, so
  they must at minimum be fallback-linked. Keep both terms, chain them.
- **`Tight` vs `Closed Tight` vs `Closed 1`** for the tightest hi-hat.
- Case and punctuation variants inside one vendor's own data: the Toontrack corpus contains
  `Rim Only` **and** `Rim only`, `Seq Hard` **and** `Seq hard`, `Off Beat` **and** `Off beat`,
  `Crashed`/`Crashe`/`Crashed` typos, `Floot Tom 1`, `Crahs Main R`. **Vendor label strings are dirty;
  the pivot must never key on them.** This is the strongest argument in this dossier for stable numeric
  pivot IDs with vendor strings as a separate, non-load-bearing display field.

### 3.4 Recommended shape (what the sources push toward)

1. **A stable integer ID per pivot term**, never reused, with explicit reserved ranges — Jamstix proves
   both the value and the failure mode (do not make the integer space encode the taxonomy, or later
   additions land in the wrong place).
2. **A structured tuple as the term's definition**, not a string:
   `{ instrument, instance?, zone?, contact?, technique, openness?, implement?, hand?, state? }`.
   The ID is the primary key; the tuple is what fallback chains reason over; the vendor label is display
   only.
3. **A separate `controller` model** attached to layout entries, not to pivot terms:
   `{ resolvedBy: cc|aftertouch|none, ccNumber, polarity, zones: [...] }`. This covers BFD3
   `Variable Tip`, AD2 `CC HiHat`, NI `Open Controller`, SD3 `{CC} … Trig`, MODO `CC TIP/CC SHANK`,
   Jamstix `Hihat (Dynamic Open)`, GGD `Hats CC` with one mechanism.
4. **An `entryKind` on every layout note**: `canonical | alias | gm-anchor | controller-trigger |
   choke-modifier | reserved`. Without it, alias notes corrupt any inversion.
5. **Choke as a modifier**, not as an articulation of the cymbal. Jamstix's "chokes the last cymbal
   played with the same hand" and NI's "release samples … will do nothing if no cymbal is active" both
   say the same thing: a choke is an event that references a previous event.
6. **`role` must be separated from `dynamics tier`.** `ghost` is currently in drum-remap's `role` enum
   next to `backbeat` and `fill`, but `Left Ghost`/`Right Ghost` (Cajon, Udu) and `Seq Soft`/`Seq Hard`
   (Toontrack hats) are *sample selections*. Musical function and sample tier are independent.
7. **Percussion needs a real sub-taxonomy**, not Jamstix's anonymous `Percussion n Main/Alternate`.
   The Toontrack corpus (§2.7) is the best available enumeration to seed it, and the recurring
   articulation set is small and regular: `Open`, `Muted`, `Slap` (open/closed), `Bass`, `Heel`, `Rim`,
   `Ghost`, `Flam`, `Crescendo`, `Shake`, `On Beat`, `Off Beat`, `Long`, `Short` — plus a
   left/right hand axis that is already needed for the kit.

### 3.5 Sizing check

| Layout | named entries in its default map | drum-remap's map file |
|---|---|---|
| Toontrack SD3 | **96** | 20 |
| BFD3 | **73** | 25 |
| GGD Invasion | (≥45) | 45 |
| SSD5 | — | 38 |
| AD2 | — | 29 |
| GGD Modern & Massive | — | 29 |
| MT Power Drum Kit 2 | — | 17 |

drum-remap covers **20 of SD3's 96** and **25 of BFD3's 73**. A pivot sized for round-tripping the two
market-leading libraries needs on the order of **150–250 kit terms** before percussion, and the
Toontrack corpus suggests **another 200+** for percussion.

### 3.6 Things that must be decided before data collection

- **Is `tip`/`shank` a property of the stick or a position on the cymbal?** Toontrack says stick, AD2
  says position (it crossfades them with a *positional* CC). Pick one and document it; the pivot term
  must round-trip both readings.
- **Openness scale**: normalised 0.0–1.0, or an ordinal ladder with named anchors? SD3 needs 6 steps on
  tip, 5 on edge, 5 on bell; NI's `Open Loose` sits between ¾ and full; SSD5's `Loosen` sits between
  closed and ¼. A pure ordinal ladder cannot hold both without renumbering. A **normalised fraction plus
  a named anchor** holds both.
- **Does the pivot represent "the kit as recorded" (snares off, towel on, felt beater) as articulations
  or as a kit-state modifier?** Libraries do it both ways (`Wires Off` is an articulation in NI/GGD;
  `Kick: No Snare` is an articulation in BFD3; a beater is an articulation in Abbey Road but a model
  parameter in MODO).
- **Instance naming convention** for cymbals must be fixed now: SD3 numbers them 1–5 with no type;
  BFD3 splits `Crash 1/2` from `Cymbal 1/2/3`; GGD uses `Main`/`Wide` × `L`/`R`; SSD5 uses `Left`/`Right`.
  Recommend an ordinal + optional spatial hint (`ordinal: 1, position: left`) rather than either alone.

### 3.7 Explicit warning drawn from Jamstix

Jamstix's flat ID space is the closest existing thing to a pivot vocabulary and it has already failed in
the way KITWARP is trying to avoid: `Snare` (1) and `Snare Center Hit` (38) and `2nd Snare Center Hit`
(103) are three unrelated integers for what is structurally one term with two axis values, and the
percussion range is semantically empty. **Do not let the ID encode the taxonomy, and do not add
"2nd <X>" terms — put the piece index in an `instance` field.**

---

## 4. Provenance

| # | Fact set | Source | Licence / status |
|---|---|---|---|
| P1 | BFD3 default key map, 73 articulations (§2.1–2.6) | `https://www.fxpansion.com/webmanuals/bfd3/operationmanual/bfd3_key_map_reference.htm` — parsed table, saved at `scratchpad/dl/bfd3_key_map_reference.htm` | © FXpansion/inMusic. Vendor documentation, quoted as fact. |
| P2 | BFD3 e-drum model: `Variable Tip`/`Variable Shank`, CC#4 pedal, 5 zones, snare CC#17 `Hit`↔`Half Edge` | `https://www.fxpansion.com/webmanuals/bfd3/operationmanual/using_electronic_drumkits.htm` | ditto |
| P3 | BFD3 drum-editor terminology ("articulation", per-drum articulation control) | `https://www.fxpansion.com/webmanuals/bfd3/operationmanual/drum_editor.htm` | ditto |
| P4 | Superior Drummer 3 layout, 96 named articulations (§2.1–2.6, 2.8.1) | `SD Superior Drummer 3.drm` in `Toontrack Drum Maps.zip`, `https://forums.steinberg.net/uploads/short-url/iXKmYyLGMsoTzuUxMLnMcs4kxzD.zip` (thread `https://forums.steinberg.net/t/get-your-ezdrummer-and-sd3-drum-maps-here/99193`); local copy `scratchpad/dl/ttmaps/` | **Community-created**, forum-posted, no licence stated. Naming is Toontrack's. **Corroborated by P5.** |
| P5 | Independent SD3 articulation list (corroboration for P4) | `https://github.com/chad-ramos/studio-one-drum-maps` → `Superior Drummer 3.pitchlist`; cloned to `scratchpad/repos/s1maps/` | Community; repo has **no LICENSE file** — treat as all-rights-reserved, use as reference only, do not vendor the file. |
| P6 | Toontrack articulation corpus across 42 EZX libraries (§2.7, §2.8.3–2.8.5) | 42 further `.drm` files in the same zip as P4; aggregated to `scratchpad/research/toontrack_buckets.json` | as P4 |
| P7 | Official EZdrummer GM-Extended key map and alias/GM policy (§2.4.1, §2.8.4) | EZdrummer operation manual PDF §4.4 "Key Mapping", pp. 15; `https://images.thomann.de/pics/prod/221685_ezdrummer_manual.pdf` | © Toontrack Music AB. Vendor documentation. |
| P8 | Superior Drummer 2 manual (checked, superseded — retained only as evidence that the SD2 manual does not contain an articulation table) | `https://medias.audiofanzine.com/files/superior-drummer-operation-manual-472941.pdf` (©2008 Toontrack) | vendor, obsolete |
| P9 | AD2 terminology ("stroketype"), CC HiHat model, CC Positional Snare (CC#16) and Ride (`Ride Tip`/`Ride Shaft`), Foot Close/Foot Splash, Open Hit/Shallow Hit (§2.2, §2.5, §2.8.1) | Addictive Drums 2 manual PDF pp. 37–43; `https://medias.audiofanzine.com/files/ad2-manual-472076.pdf` | © XLN Audio. Vendor documentation. |
| P10 | AD2 per-note stroketype names (`HiHat Closed 1 Tip/Shaft`, `HiHat Open A–D`, `Ride 1 Tip/Shaft/Bell/Choke`, …) | `scratchpad/repos/drum-remap/maps/addictive-drums-2.json` | Community (drum-remap). **UNVERIFIED against XLN's own keymap PDF** — XLN support site is Cloudflare-blocked. |
| P11 | NI Studio Drummer complete articulation list, all 3 kits (§2.1–2.7, §2.8.1, §2.8.3) | `https://www.native-instruments.com/fileadmin/ni_media/downloads/manuals/Studio_Drummer_Manual_English.pdf` §5, pp. 35–46 | © Native Instruments. Vendor documentation. |
| P12 | NI Abbey Road 60s Drums complete articulation list, both kits; `Felt Beater`/`Rubber Beater`, `Tea Towel`/`Towel`, `Sizzle Ride` (§2.1–2.6) | `https://www.native-instruments.com/fileadmin/ni_media/downloads/manuals/Abbey_Road_60s_Drums_Manual.pdf` §4, pp. 19–23 | ditto |
| P13 | Abbey Road 70s Drummer ships mapping presets for GM, V-Drums ×2, DrumIt Five, EZdrummer, Superior Drummer, BFD, iMap, Addictive Drums | WebSearch result summarising the Abbey Road 70s Drummer owner's manual | **UNVERIFIED** — the 70s/Modern manual PDFs 404'd at the guessed NI URLs. |
| P14 | Jamstix 4 Kit Piece Reference IDs (Appendix B) and output-map file format (Appendix C) (§2.9) | `https://www.rayzoon2.com/docs/jamstix4_manual.pdf` pp. 72–77 | © Rayzoon Technologies. Vendor documentation. |
| P15 | SSD5 concepts: articulation naming/volume UI, Kit Mapping vs Input Converter, Hi-Hat Pedal Control (CC) vs Hi-Hat MIDI Control (mod wheel) | `https://slate-product-files.sfo2.cdn.digitaloceanspaces.com/ssd5/SSD5%20User%20Manual.pdf` pp. 11–18 | © Steven Slate Drums. Vendor documentation. **The manual contains no articulation-name table.** |
| P16 | SSD5 per-note articulation names (`Hi-Hat Tip Closed Tight`, `Hi-Hat Shank Loosen`, `Ride Bow Tip`/`Ride Bow Shank`, …) | `scratchpad/repos/drum-remap/maps/ssd5.json` | Community. **UNVERIFIED against Slate documentation.** |
| P17 | GGD Modern & Massive / P4 articulation names (`Hat Closed Loose`, `Hat Open0–3`, `Hats CC`, `Mini Hats`, `Stack`, `Crash Main/Wide L/R`, `Ride Crash`) | `scratchpad/repos/s1maps/GGD Modern and Massive.pitchlist`, `GGD P4.pitchlist`; `scratchpad/repos/drum-remap/maps/ggd-*.json` | Community. **UNVERIFIED** — `support.ggd.co` returns 403. |
| P18 | MODO Drum: CC4 pedal (invert), CC16 snare position, CC18 tom position | IK Multimedia FAQ #1262, `https://www.ikmultimedia.com/faq/index.php?id=1262` | © IK Multimedia. Vendor documentation. |
| P19 | MODO Drum: CC TIP / CC SHANK continuous hi-hat; felt/wood/plastic beaters; heel-up/heel-down; per-hand position/diameter/stick-tip | Sound On Sound review, `https://www.soundonsound.com/reviews/ik-multimedia-modo-drum` | Press. **Articulation names UNVERIFIED** (MODO manual is account-gated). |
| P20 | MT Power Drum Kit 2 ships cross-plugin MIDI-mapping presets for Abbey Road Modern Drummer, Addictive Drums, EZ Drummer, FXpansion BFD, GetGoodDrums, GM Standard, ML Drums, NI Studio Drummer, SSD4, SSD5, Superior Drummer | `https://www.powerdrumkit.com/presets_midi-mapping-for-other-drum-plugins.php`; the `.PDKmap` files themselves were downloaded and are **binary with no embedded names** | Vendor page. The preset list is itself evidence of which layouts matter in practice. |
| P21 | Superior Drummer 3 ride has "bow tip, bow shank, bell tip, bell shank, edge, mute hit and crescendo"; snares have 8 articulations (brushed snares 12); hi-hats have 27 articulations each; crash/ride up to 8 | MusicRadar review of SD3, via WebSearch, `https://www.musicradar.com/reviews/toontrack-superior-drummer-3` | Press. Independently consistent with P4/P5 — used only as corroboration. |
| P22 | drum-remap's own maps and the 40-tag set used for the gap analysis (§3.5) | `https://github.com/marty-615/drum-remap`, cloned to `scratchpad/repos/drum-remap/` | Community. |

### 4.1 Explicitly UNVERIFIED claims in this dossier

- All **SSD5**, **GGD**, and **AD2 per-note** articulation names (P10, P16, P17).
- All **MODO Drum** articulation names (P19).
- **Abbey Road 70s / Modern Drummer** articulation lists (P13) — not retrieved; the 60s list is assumed
  representative but this is an assumption.
- The claim that **SD3's `.drm`/`.pitchlist` naming is byte-identical to Toontrack's in-app naming** —
  two independent third-party exports agree with each other and with Toontrack's documented
  `[Instrument] Articulation` style, but no vendor page was reachable to confirm.
- **EZdrummer 3's** own extended layout — only EZdrummer 1/2-era EZX maps were obtained. EZD3 is
  documented (P7 + search) as using the same **Toontrack "GM Extended"** scheme, but its additional
  articulations were not enumerated.
- **ML Drums** — no data at all.
