"""One-shot bootstrap that minted vocabulary v0.1.0.

Kept in the repository for audit, NOT for re-running. From v0.1.0 onward the vocabulary
files are hand-maintained and machine-validated; per ADR-0002 no generator writes them.
Re-running this would re-assign ids, which ADR-0003 forbids.

    python -m tools.bootstrap.mint_v0_1 --emit    # what produced the committed files
"""

import argparse
import json
import pathlib

VERSION = "0.1.0"
SERIAL = 1

# --------------------------------------------------------------------------------------
# Axis registries. Closed enums. Adding a value is a MINOR bump; adding an AXIS is MAJOR.
# The small integer ids are what codegen packs into a row; they are stable and never reused.
# --------------------------------------------------------------------------------------

AXES = {
    "instrument": {
        "description": "What makes the sound. Grouped by family; the family is documentation "
                       "and fallback scope, not part of the identity.",
        "values": [
            # kit.membrane
            (1, "kick", "kit.membrane"),
            (2, "snare", "kit.membrane"),
            (3, "tom", "kit.membrane"),
            (4, "octoban", "kit.membrane"),
            # kit.cymbal
            (10, "hihat", "kit.cymbal"),
            (11, "xhat", "kit.cymbal"),
            (12, "ride", "kit.cymbal"),
            (13, "crash", "kit.cymbal"),
            (14, "china", "kit.cymbal"),
            (15, "splash", "kit.cymbal"),
            (16, "stack", "kit.cymbal"),
            (17, "bell", "kit.cymbal"),
            (18, "cymbal", "kit.cymbal"),
            (19, "mini-china", "kit.cymbal"),
            (20, "mini-hihat", "kit.cymbal"),
            (21, "crash-ride", "kit.cymbal"),
            (22, "sizzle-ride", "kit.cymbal"),
            # kit.aux
            (30, "cowbell", "kit.aux"),
            (31, "jam-block", "kit.aux"),
            (32, "woodblock", "kit.aux"),
            (33, "tambourine", "kit.aux"),
            (34, "sticks", "kit.aux"),
            (35, "clap", "kit.aux"),
            (36, "shaker", "kit.aux"),
            (37, "triangle", "kit.aux"),
            (38, "chimes", "kit.aux"),
            (39, "aux-pad", "kit.aux"),
        ],
        "reserved_families": [
            "perc.hand", "perc.shaken", "perc.scraped", "perc.struck-idiophone",
            "perc.wind", "orch", "electronic", "utility", "unknown",
        ],
    },
    "site": {
        "description": "Contact site ON THE INSTRUMENT. Distinct from `contact`, which is the "
                       "part of the implement. PAL splits these and real layouts contain both.",
        "values": [
            (1, "head", None), (2, "rim", None), (3, "rim2", None), (4, "crossstick", None),
            (5, "shell", None), (6, "bow", None), (7, "edge", None), (8, "bell", None),
            (9, "underside", None),
        ],
    },
    "position": {
        "description": "Where on the site, radially. Also expressible continuously through the "
                       "strike_position controllers.",
        "values": [(1, "centre", None), (2, "halfway", None), (3, "offset", None),
                   (4, "perimeter", None)],
    },
    "contact": {
        "description": "Part of the implement that touches. Orthogonal to `site`: Superior "
                       "Drummer ships Bow Tip, Bow Shank, Bell Tip and Bell Shank.",
        "values": [(1, "tip", None), (2, "shank", None), (3, "butt", None)],
    },
    "technique": {
        "description": "The stroke itself. `choke` is deliberately absent: it is a relation on "
                       "a previously sounded event, not a stroke. See vocabulary/rules.json.",
        "values": [
            (1, "hit", None), (2, "rimshot", None), (3, "rim-only", None), (4, "sidestick", None),
            (5, "stick-shot", None), (6, "back-stick", None), (7, "ping-shot", None),
            (8, "gok-shot", None), (9, "slap", None), (10, "open-tone", None),
            (11, "bass-tone", None), (12, "mute-stroke", None), (13, "heel", None),
            (14, "toe", None), (15, "thumb", None), (16, "sweep", None), (17, "swirl", None),
            (18, "circling", None), (19, "scrape", None), (20, "shake", None), (21, "gliss", None),
            (22, "dead", None), (23, "chick", None), (24, "foot-splash", None),
        ],
    },
    "ornament": {
        "description": "Grace or multi-stroke qualifier. `attacks` lets the expansion rules "
                       "find compound strokes mechanically: a flam is one note in a library and "
                       "two notes in a performance.",
        "values": [
            (1, "flam", 2), (2, "drag", 3), (3, "ruff", 4), (4, "bounced", 2),
            (5, "roll", 0), (6, "buzz", 0), (7, "crescendo", 0), (8, "swell", 0), (9, "wash", 0),
        ],
        "value_meaning": "attacks: number of contacts, 0 = sustained/indeterminate",
    },
    "openness": {
        "description": "Ordered state. The named anchors are labels for bands of one normalised "
                       "scalar, 0.0 fully closed to 1.0 fully open, so a four-level device and a "
                       "six-level device project onto the same axis without inventing terms. "
                       "This is the same axis the hi-hat pedal CC measures.",
        "values": [
            (0, "tight", 0.0), (1, "closed", 0.12), (2, "closed-loose", 0.20),
            (3, "quarter", 0.25), (4, "half", 0.50), (5, "three-quarter", 0.75),
            (6, "loose", 0.85), (7, "open", 1.0),
        ],
        "value_meaning": "scalar: position on the normalised openness axis",
    },
    "damping": {
        "description": "What damps and when, applied AT the strike. PAL shows this is not a bare "
                       "scalar: hand damping while striking and while not striking are different "
                       "sounds. Distinct from the choke relation, which is applied after.",
        "values": [(0, "none", None), (1, "muted", None), (2, "damped", None),
                   (3, "towel", None), (4, "gated", None)],
    },
    "mechanism": {
        "description": "Device state that is not damping. Snares off is a resonating mechanism "
                       "being disengaged, not a mute.",
        "values": [(0, "wires-on", None), (1, "wires-off", None), (2, "kick-damped", None),
                   (3, "kick-half-open", None)],
    },
    "implement": {
        "description": "What strikes it. MusicXML factors this as stick-type x stick-material; "
                       "VSL ships a seven-step hardness scale. Tip hardness is carried in the "
                       "value name where a source distinguishes it.",
        "values": [
            (1, "stick", None), (2, "jazz-stick", None), (3, "brush", None), (4, "rod", None),
            (5, "mallet-soft", None), (6, "mallet-medium", None), (7, "mallet-hard", None),
            (8, "hand", None), (9, "finger", None), (10, "felt-beater", None),
            (11, "wood-beater", None), (12, "plastic-beater", None), (13, "rubber-beater", None),
            (14, "superball", None),
        ],
    },
    "dynamic": {
        "description": "Sample tier, not musical role. Some layouts give a dynamic band its own "
                       "note (Snare Ghost, Seq Soft / Seq Hard); without this axis such a note "
                       "cannot map onto a target's plain hit at low velocity, or back.",
        "values": [(0, "normal", None), (1, "ghost", None), (2, "soft", None),
                   (3, "hard", None), (4, "accent", None)],
    },
    "timbre": {
        "description": "Sound-generating lineage. Without it every GM2 Analog, GS TR-808 and XG "
                       "Electro source becomes indistinguishable from the acoustic set after a "
                       "round trip.",
        "values": [
            (1, "acoustic", None), (2, "electronic", None), (3, "analog-808", None),
            (4, "analog-909", None), (5, "analog-707", None), (6, "analog-606", None),
            (7, "analog-cr78", None), (8, "fm", None), (9, "pcm", None), (10, "physical", None),
            (11, "chip", None), (12, "noise", None), (99, "unknown", None),
        ],
    },
    "voicing": {
        "description": "Kit or miking variant of the same instrument. GM2 builds seven of its "
                       "nine sets on this alone.",
        "values": [(1, "standard", None), (2, "room", None), (3, "power", None), (4, "jazz", None),
                   (5, "orchestra", None), (6, "lo-fi", None), (7, "dark", None)],
    },
}

# Carried on a LAYOUT SLOT's reference to a term, not on the term itself, because they are
# unbounded-ordinal (instance) or droppable at zero cost (limb). See ADR-0001.
REFERENCE_AXES = {
    "instance": {
        "description": "Which one of several identical instruments on the device, 1-based, "
                       "ordered high to low in pitch for toms and left to right from the "
                       "player's seat for cymbals. The direction is fixed here and must not be "
                       "reinterpreted per device: getting it backwards silently swaps every tom.",
    },
    "limb": {
        "description": "Which limb, where a layout samples them separately. Identity-bearing "
                       "when present, but a target that lacks it drops it at zero fallback cost.",
        "values": [(1, "left-hand", None), (2, "right-hand", None), (3, "alternating", None),
                   (4, "left-foot", None), (5, "right-foot", None)],
    },
}

CONTROLLERS = [
    (1, "hihat.pedal_position", "0.0 fully open .. 1.0 fully closed, normalised. Roland "
     "transmits 0-90 and everyone else 0-127, 2Box can invert polarity, and every vendor "
     "sends it before the note-on."),
    (2, "strike_position.radial", "centre .. perimeter, for snare and tom heads, ride bow, "
     "hi-hat bow. Jamstix carries it as CC14 for snare and CC15 for tom."),
    (3, "strike_position.rim_depth", "deep .. shallow on a rim. A different geometry from radial."),
    (4, "strike_position.lateral", "left .. right."),
    (5, "choke_amount", "0.0 .. 1.0, continuous on Roland digital pads."),
]

# --------------------------------------------------------------------------------------
# Terms. v0.1.0 mints the drum-kit core only. Percussion, orchestral, electronic and
# utility families are reserved above and are a MINOR bump: adding terms is cheap, adding
# an axis is not, which is the asymmetry ADR-0001 spends its budget on.
#
# `instance` and `limb` are NOT here. They live on a layout slot's reference to a term,
# because instance is an unbounded ordinal and limb is droppable at zero fallback cost.
# --------------------------------------------------------------------------------------

TERMS = []


def T(slug, display, parent=None, role=None, **axes):
    TERMS.append({"slug": slug, "display_name": display, "parent": parent,
                  "role_hint": role, "axes": axes})


HH_LEVELS = ["tight", "closed", "closed-loose", "quarter", "half", "three-quarter",
             "loose", "open"]

# ---- kick ----
T("kick.hit", "Kick", role="foundation", instrument="kick", technique="hit")
T("kick.hit.damped", "Kick, damped", "kick.hit", "foundation",
  instrument="kick", technique="hit", mechanism="kick-damped")
T("kick.hit.half-open", "Kick, half open", "kick.hit", "foundation",
  instrument="kick", technique="hit", mechanism="kick-half-open")
T("kick.hit.wires-off", "Kick, snares off", "kick.hit", "foundation",
  instrument="kick", technique="hit", mechanism="wires-off")
T("kick.hit.felt", "Kick, felt beater", "kick.hit", "foundation",
  instrument="kick", technique="hit", implement="felt-beater")
T("kick.hit.wood", "Kick, wood beater", "kick.hit", "foundation",
  instrument="kick", technique="hit", implement="wood-beater")
T("kick.hit.plastic", "Kick, plastic beater", "kick.hit", "foundation",
  instrument="kick", technique="hit", implement="plastic-beater")
T("kick.hit.double", "Kick, auto double", "kick.hit", "foundation",
  instrument="kick", technique="hit", ornament="bounced")
T("kick.rim", "Kick rim", "kick.hit", "effect", instrument="kick", site="rim", technique="hit")
T("kick.electric", "Kick, electronic", "kick.hit", "foundation",
  instrument="kick", technique="hit", timbre="electronic")

# ---- snare ----
T("snare.hit", "Snare", role="backbeat",
  instrument="snare", site="head", position="centre", technique="hit")
T("snare.hit.halfway", "Snare, halfway", "snare.hit", "backbeat",
  instrument="snare", site="head", position="halfway", technique="hit")
T("snare.hit.offset", "Snare, off centre", "snare.hit", "backbeat",
  instrument="snare", site="head", position="offset", technique="hit")
T("snare.hit.edge", "Snare, edge", "snare.hit", "backbeat",
  instrument="snare", site="head", position="perimeter", technique="hit")
T("snare.hit.ghost", "Snare, ghost", "snare.hit", "ghost",
  instrument="snare", site="head", technique="hit", dynamic="ghost")
T("snare.hit.soft", "Snare, soft layer", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", dynamic="soft")
T("snare.hit.hard", "Snare, hard layer", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", dynamic="hard")
T("snare.rimshot", "Snare rimshot", "snare.hit", "backbeat",
  instrument="snare", site="rim", technique="rimshot")
T("snare.rimshot.shallow", "Snare rimshot, shallow", "snare.rimshot", "backbeat",
  instrument="snare", site="rim", position="perimeter", technique="rimshot")
T("snare.rim-only", "Snare rim only", "snare.hit", "ghost",
  instrument="snare", site="rim", technique="rim-only")
T("snare.sidestick", "Snare cross stick", "snare.hit", "ghost",
  instrument="snare", site="crossstick", technique="sidestick")
T("snare.stick-shot", "Snare stick shot", "snare.hit", "accent",
  instrument="snare", site="head", technique="stick-shot")
T("snare.back-stick", "Snare back stick", "snare.hit", "accent",
  instrument="snare", site="head", technique="back-stick")
T("snare.ping-shot", "Snare ping shot", "snare.rimshot", "accent",
  instrument="snare", site="rim", technique="ping-shot")
T("snare.gok-shot", "Snare gok shot", "snare.rimshot", "accent",
  instrument="snare", site="rim", technique="gok-shot")
T("snare.shell", "Snare shell", "snare.hit", "effect",
  instrument="snare", site="shell", technique="hit")
T("snare.flam", "Snare flam", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", ornament="flam")
T("snare.drag", "Snare drag", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", ornament="drag")
T("snare.ruff", "Snare ruff", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", ornament="ruff")
T("snare.roll", "Snare roll", "snare.hit", "fill",
  instrument="snare", site="head", technique="hit", ornament="roll")
T("snare.buzz", "Snare buzz roll", "snare.roll", "fill",
  instrument="snare", site="head", technique="hit", ornament="buzz")
T("snare.wires-off", "Snare, wires off", "snare.hit", "effect",
  instrument="snare", site="head", technique="hit", mechanism="wires-off")
T("snare.wires-off.rimshot", "Snare rimshot, wires off", "snare.wires-off", "effect",
  instrument="snare", site="rim", technique="rimshot", mechanism="wires-off")
T("snare.towel", "Snare, towel", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", damping="towel")
T("snare.brush.hit", "Snare, brush", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", implement="brush")
T("snare.brush.sweep", "Snare, brush sweep", "snare.brush.hit", "timekeeping",
  instrument="snare", site="head", technique="sweep", implement="brush")
T("snare.brush.swirl", "Snare, brush swirl", "snare.brush.hit", "timekeeping",
  instrument="snare", site="head", technique="swirl", implement="brush")
T("snare.brush.circling", "Snare, brush circling", "snare.brush.sweep", "timekeeping",
  instrument="snare", site="head", technique="circling", implement="brush")
T("snare.brush.muted", "Snare, brush muted", "snare.brush.hit", "ghost",
  instrument="snare", site="head", technique="hit", implement="brush", damping="muted")
T("snare.rod.hit", "Snare, rods", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", implement="rod")
T("snare.mallet.hit", "Snare, mallet", "snare.hit", "fill",
  instrument="snare", site="head", technique="hit", implement="mallet-medium")
T("snare.electric", "Snare, electronic", "snare.hit", "backbeat",
  instrument="snare", site="head", technique="hit", timbre="electronic")

# ---- toms ----
T("tom.hit", "Tom", role="fill", instrument="tom", site="head", position="centre", technique="hit")
T("tom.hit.edge", "Tom, edge", "tom.hit", "fill",
  instrument="tom", site="head", position="perimeter", technique="hit")
T("tom.hit.ghost", "Tom, ghost", "tom.hit", "ghost",
  instrument="tom", site="head", technique="hit", dynamic="ghost")
T("tom.rimshot", "Tom rimshot", "tom.hit", "fill",
  instrument="tom", site="rim", technique="rimshot")
T("tom.rim-only", "Tom rim only", "tom.hit", "ghost",
  instrument="tom", site="rim", technique="rim-only")
T("tom.shell", "Tom shell", "tom.hit", "effect", instrument="tom", site="shell", technique="hit")
T("tom.flam", "Tom flam", "tom.hit", "fill",
  instrument="tom", site="head", technique="hit", ornament="flam")
T("tom.roll", "Tom roll", "tom.hit", "fill",
  instrument="tom", site="head", technique="hit", ornament="roll")
T("tom.hit.damped", "Tom, damped", "tom.hit", "fill",
  instrument="tom", site="head", technique="hit", damping="damped")
T("tom.hit.towel", "Tom, towel", "tom.hit", "fill",
  instrument="tom", site="head", technique="hit", damping="towel")
T("tom.brush.hit", "Tom, brush", "tom.hit", "fill",
  instrument="tom", site="head", technique="hit", implement="brush")
T("tom.brush.sweep", "Tom, brush sweep", "tom.brush.hit", "timekeeping",
  instrument="tom", site="head", technique="sweep", implement="brush")
T("tom.mallet.hit", "Tom, mallet", "tom.hit", "fill",
  instrument="tom", site="head", technique="hit", implement="mallet-medium")
T("tom.electric", "Tom, electronic", "tom.hit", "fill",
  instrument="tom", site="head", technique="hit", timbre="electronic")
T("octoban.hit", "Octoban", role="fill", instrument="octoban", site="head", technique="hit")

# ---- hi-hat: openness x (site | contact) ----
# The ladder is generated rather than typed out because it IS a product, and writing it as
# a product is the point of the axis decomposition. Eight anchors x four readings.
_HH_DISPLAY = {
    "tight": "tight", "closed": "closed", "closed-loose": "loose closed", "quarter": "quarter open",
    "half": "half open", "three-quarter": "three-quarter open", "loose": "loose", "open": "open",
}
for _lvl in HH_LEVELS:
    _d = _HH_DISPLAY[_lvl]
    T(f"hihat.{_lvl}", f"Hi-hat, {_d}", None, "timekeeping",
      instrument="hihat", site="bow", technique="hit", openness=_lvl)
    T(f"hihat.{_lvl}.tip", f"Hi-hat, {_d}, tip", f"hihat.{_lvl}", "timekeeping",
      instrument="hihat", site="bow", contact="tip", technique="hit", openness=_lvl)
    T(f"hihat.{_lvl}.shank", f"Hi-hat, {_d}, shank", f"hihat.{_lvl}", "timekeeping",
      instrument="hihat", site="bow", contact="shank", technique="hit", openness=_lvl)
    T(f"hihat.{_lvl}.edge", f"Hi-hat, {_d}, edge", f"hihat.{_lvl}", "timekeeping",
      instrument="hihat", site="edge", technique="hit", openness=_lvl)

T("hihat.closed.bell", "Hi-hat bell, closed", "hihat.closed", "accent",
  instrument="hihat", site="bell", technique="hit", openness="closed")
T("hihat.open.bell", "Hi-hat bell, open", "hihat.open", "accent",
  instrument="hihat", site="bell", technique="hit", openness="open")
T("hihat.pedal.chick", "Hi-hat pedal chick", None, "timekeeping",
  instrument="hihat", technique="chick", openness="closed")
T("hihat.pedal.splash", "Hi-hat foot splash", "hihat.pedal.chick", "accent",
  instrument="hihat", technique="foot-splash", openness="half")
T("hihat.open-close.tip", "Hi-hat open-close, tip", "hihat.open.tip", "timekeeping",
  instrument="hihat", site="bow", contact="tip", technique="hit", openness="open", ornament="wash")
T("hihat.open-close.edge", "Hi-hat open-close, edge", "hihat.open.edge", "timekeeping",
  instrument="hihat", site="edge", technique="hit", openness="open", ornament="wash")

T("xhat.closed", "X-hat, closed", None, "timekeeping",
  instrument="xhat", site="bow", technique="hit", openness="closed")
T("xhat.open", "X-hat, open", None, "timekeeping",
  instrument="xhat", site="bow", technique="hit", openness="open")
T("mini-hihat.closed", "Mini hi-hat, closed", None, "timekeeping",
  instrument="mini-hihat", site="bow", technique="hit", openness="closed")
T("mini-hihat.open", "Mini hi-hat, open", None, "timekeeping",
  instrument="mini-hihat", site="bow", technique="hit", openness="open")

# ---- ride ----
T("ride.bow", "Ride bow", None, "timekeeping", instrument="ride", site="bow", technique="hit")
T("ride.bow.tip", "Ride bow, tip", "ride.bow", "timekeeping",
  instrument="ride", site="bow", contact="tip", technique="hit")
T("ride.bow.shank", "Ride bow, shank", "ride.bow", "timekeeping",
  instrument="ride", site="bow", contact="shank", technique="hit")
T("ride.bell", "Ride bell", None, "accent", instrument="ride", site="bell", technique="hit")
T("ride.bell.tip", "Ride bell, tip", "ride.bell", "accent",
  instrument="ride", site="bell", contact="tip", technique="hit")
T("ride.bell.shank", "Ride bell, shank", "ride.bell", "accent",
  instrument="ride", site="bell", contact="shank", technique="hit")
T("ride.edge", "Ride edge", "ride.bow", "timekeeping",
  instrument="ride", site="edge", technique="hit")
T("ride.crash", "Ride, crashed", "ride.edge", "accent",
  instrument="ride", site="edge", technique="hit", dynamic="accent")
T("ride.roll", "Ride roll", "ride.bow", "fill",
  instrument="ride", site="bow", technique="hit", ornament="roll")
T("ride.swell", "Ride swell", "ride.bow", "effect",
  instrument="ride", site="bow", technique="hit", ornament="swell")
T("ride.mute", "Ride, muted", "ride.bow", "timekeeping",
  instrument="ride", site="bow", technique="hit", damping="muted")
T("ride.brush", "Ride, brush", "ride.bow", "timekeeping",
  instrument="ride", site="bow", technique="hit", implement="brush")
T("ride.mallet", "Ride, mallet", "ride.bow", "effect",
  instrument="ride", site="bow", technique="hit", implement="mallet-medium")
T("sizzle-ride.bow", "Sizzle ride", None, "timekeeping",
  instrument="sizzle-ride", site="bow", technique="hit")
T("crash-ride.bow", "Crash ride", None, "timekeeping",
  instrument="crash-ride", site="bow", technique="hit")

# ---- crashes and effect cymbals ----
for _inst, _label in (("crash", "Crash"), ("china", "China"), ("splash", "Splash"),
                      ("stack", "Stack"), ("mini-china", "Mini china")):
    T(f"{_inst}.hit", _label, None, "accent", instrument=_inst, site="bow", technique="hit")
    T(f"{_inst}.mute", f"{_label}, muted", f"{_inst}.hit", "accent",
      instrument=_inst, site="bow", technique="hit", damping="muted")
T("crash.edge", "Crash edge", "crash.hit", "accent",
  instrument="crash", site="edge", technique="hit")
T("crash.bell", "Crash bell", "crash.hit", "accent",
  instrument="crash", site="bell", technique="hit")
T("crash.swell", "Crash swell", "crash.hit", "effect",
  instrument="crash", site="bow", technique="hit", ornament="swell")
T("crash.roll", "Crash roll", "crash.hit", "fill",
  instrument="crash", site="bow", technique="hit", ornament="roll")
T("crash.mallet", "Crash, mallet", "crash.hit", "effect",
  instrument="crash", site="bow", technique="hit", implement="mallet-medium")
T("china.edge", "China edge", "china.hit", "accent",
  instrument="china", site="edge", technique="hit")
T("china.bell", "China bell", "china.hit", "accent",
  instrument="china", site="bell", technique="hit")
T("stack.tight", "Stack, tight", "stack.hit", "accent",
  instrument="stack", site="bow", technique="hit", damping="muted")
T("stack.loose", "Stack, loose", "stack.hit", "accent",
  instrument="stack", site="bow", technique="hit")
T("bell.bow", "Kit bell, bow", None, "accent", instrument="bell", site="bow", technique="hit")
T("bell.bell", "Kit bell", None, "accent", instrument="bell", site="bell", technique="hit")
T("cymbal.hit", "Cymbal, unclassified", None, "accent",
  instrument="cymbal", site="bow", technique="hit")

# ---- auxiliary kit pieces ----
T("cowbell.hit", "Cowbell", None, "timekeeping", instrument="cowbell", technique="hit")
T("cowbell.tip", "Cowbell, tip", "cowbell.hit", "timekeeping",
  instrument="cowbell", contact="tip", technique="hit")
T("cowbell.shank", "Cowbell, shank", "cowbell.hit", "accent",
  instrument="cowbell", contact="shank", technique="hit")
T("cowbell.mute", "Cowbell, muted", "cowbell.hit", "timekeeping",
  instrument="cowbell", technique="hit", damping="muted")
T("jam-block.hit", "Jam block", None, "timekeeping", instrument="jam-block", technique="hit")
T("woodblock.hit", "Woodblock", None, "timekeeping", instrument="woodblock", technique="hit")
T("tambourine.hit", "Tambourine", None, "accent", instrument="tambourine", technique="hit")
T("tambourine.shake", "Tambourine, shake", "tambourine.hit", "timekeeping",
  instrument="tambourine", technique="shake")
T("tambourine.roll", "Tambourine roll", "tambourine.hit", "fill",
  instrument="tambourine", technique="hit", ornament="roll")
T("tambourine.thumb-roll", "Tambourine thumb roll", "tambourine.roll", "fill",
  instrument="tambourine", technique="thumb", ornament="roll")
T("sticks.hit", "Sticks", None, "effect", instrument="sticks", technique="hit")
T("clap.hit", "Hand clap", None, "backbeat", instrument="clap", technique="hit")
T("shaker.hit", "Shaker", None, "timekeeping", instrument="shaker", technique="hit")
T("shaker.shake", "Shaker, shake", "shaker.hit", "timekeeping",
  instrument="shaker", technique="shake")
T("triangle.open", "Triangle, open", None, "accent", instrument="triangle", technique="hit")
T("triangle.mute", "Triangle, muted", "triangle.open", "accent",
  instrument="triangle", technique="hit", damping="muted")
T("triangle.roll", "Triangle roll", "triangle.open", "effect",
  instrument="triangle", technique="hit", ornament="roll")
T("chimes.gliss", "Chimes, glissando", None, "effect", instrument="chimes", technique="gliss")
T("aux-pad.hit", "Auxiliary pad", None, "effect", instrument="aux-pad", technique="hit")

# --------------------------------------------------------------------------------------
# Fallback rules. Steps 1 to 3 of ADR-0001's resolution order are mechanical and derive
# from the axes; only the curated edges and the expansions are hand-written, and each
# carries a human-readable reason the way marty-615/drum-remap does.
# --------------------------------------------------------------------------------------

AXIS_DEGRADATION = [
    # axis, from, to, velocity_delta, reason
    ("site", "bell", "bow", -6, "no bell on this piece; the bow is the nearest body"),
    ("site", "edge", "bow", -4, "no edge zone; the bow is the nearest body"),
    ("site", "rim2", "rim", 0, "second rim zone absent; use the rim"),
    ("site", "crossstick", "rim", -8, "no cross-stick zone; a quiet rim is the nearest gesture"),
    ("site", "shell", "rim", -6, "no shell zone; the rim is the nearest wooden sound"),
    ("contact", "shank", "tip", 6, "no shank sample; the tip with more velocity keeps the accent"),
    ("contact", "butt", "shank", 0, "no butt sample; the shank is nearest"),
    ("openness", "*", "nearest", 0, "no such openness level; move to the nearest available level"),
    ("mechanism", "wires-off", "wires-on", 0, "target cannot disengage the snares"),
    ("mechanism", "kick-damped", "kick-half-open", 0, "no damped kick; half open is nearer than open"),
    ("damping", "towel", "damped", 0, "no towel state; plain damping is nearest"),
    ("damping", "damped", "muted", 0, "no damped state; muted is nearest"),
    ("damping", "muted", "none", -8, "no muted sample; play it open and quieter"),
    ("implement", "jazz-stick", "stick", 0, "no jazz stick; the standard stick is nearest"),
    ("implement", "rod", "brush", 0, "no rods; brushes are nearer than sticks"),
    ("implement", "brush", "stick", -12, "no brushes; a quiet stick is the least wrong"),
    ("implement", "mallet-hard", "mallet-medium", 0, "hardness step down"),
    ("implement", "mallet-medium", "mallet-soft", 0, "hardness step down"),
    ("implement", "mallet-soft", "stick", -6, "no mallets at all"),
    ("implement", "wood-beater", "plastic-beater", 0, "beater hardness step"),
    ("implement", "plastic-beater", "felt-beater", 0, "beater hardness step"),
    ("dynamic", "ghost", "normal", -25, "no ghost sample; a very quiet normal hit"),
    ("dynamic", "soft", "normal", -12, "no soft layer"),
    ("dynamic", "hard", "normal", 12, "no hard layer"),
    ("dynamic", "accent", "normal", 15, "no accent sample"),
    ("ornament", "buzz", "roll", 0, "no buzz roll; a roll is nearest"),
    ("ornament", "ruff", "drag", 0, "ornament with fewer grace notes"),
    ("ornament", "drag", "flam", 0, "ornament with fewer grace notes"),
    ("ornament", "flam", None, 8, "no ornament; a single hit with more velocity for the doubled attack"),
    ("ornament", "bounced", "flam", 0, "double stroke as a flam"),
    ("ornament", "swell", "roll", 0, "no swell; a roll is nearest"),
    ("ornament", "wash", None, 0, "no open-close gesture; the plain stroke"),
    ("position", "halfway", "centre", 0, "no positional sampling"),
    ("position", "offset", "centre", 0, "no positional sampling"),
    ("position", "perimeter", "halfway", 0, "no edge position; move inward"),
    ("timbre", "electronic", "acoustic", 0, "target has no electronic voice for this piece"),
    ("limb", "*", None, 0, "target does not sample hands separately; drop at no cost"),
]

# Curated cross-instrument edges. These may not be derived, because they cross an axis the
# distance metric cannot see. Ordered; the first that resolves wins.
CURATED = {
    "snare.sidestick": [("snare.hit", -20, "cross stick to a quiet centre hit; same function, lower dynamics"),
                        ("snare.rimshot", -25, "cross stick to a very quiet rimshot")],
    "snare.wires-off": [("tom.hit", 0, "wires off sounds like a timbale; the highest rack tom"),
                        ("snare.hit", 0, "last resort: an ordinary snare hit")],
    "ride.bow": [("crash-ride.bow", 0, "the only other riding metal"),
                 ("hihat.closed.tip", 0, "timekeeping stays timekeeping: closed hi-hat")],
    "ride.bell": [("bell.bell", 0, "bell character preserved"),
                  ("cowbell.hit", 0, "metallic ping, timekeeping kept")],
    "cowbell.hit": [("ride.bell", 0, "metallic ping, timekeeping kept")],
    "xhat.closed": [("hihat.closed", 0, "no auxiliary hat; the main hi-hat")],
    "xhat.open": [("hihat.open", 0, "no auxiliary hat; the main hi-hat")],
    "mini-hihat.closed": [("hihat.closed", 0, "no mini hat; the main hi-hat")],
    "mini-china.hit": [("china.hit", -8, "no mini china; the full china, quieter")],
    "china.hit": [("crash.hit", 0, "same role, nearest wash"),
                  ("ride.crash", 0, "crash on the ride")],
    "crash.hit": [("china.hit", 0, "the only other accent cymbal"),
                  ("ride.crash", 0, "crash on the ride")],
    "splash.hit": [("crash.hit", -10, "smaller cymbal, less velocity"),
                   ("china.hit", -10, "china, less velocity")],
    "stack.hit": [("splash.hit", 0, "short trashy accent"),
                  ("china.hit", -10, "china, shorter accent")],
    "cymbal.hit": [("crash.hit", 0, "unclassified cymbal defaults to a crash"),
                   ("ride.crash", 0, "then to a crashed ride")],
    "octoban.hit": [("tom.hit", 0, "no octoban; the highest tom")],
    "jam-block.hit": [("woodblock.hit", 0, "same wooden click"),
                      ("cowbell.hit", -6, "no wood; the cowbell is the nearest click")],
    "sizzle-ride.bow": [("ride.bow", 0, "no sizzle; the plain ride bow")],
    "aux-pad.hit": [("tom.hit", 0, "an unassigned pad defaults to a tom rather than vanishing")],
    "woodblock.hit": [("jam-block.hit", 0, "same wooden click"),
                      ("cowbell.mute", -4, "no wood at all; a muted cowbell is the nearest click")],
    "tambourine.hit": [("shaker.hit", 0, "no tambourine; a shaker keeps the same pulse"),
                       ("sticks.hit", -6, "last resort: a dry click")],
    "tambourine.shake": [("shaker.shake", 0, "no tambourine; the shaker is the nearest sustained rattle")],
    "shaker.hit": [("tambourine.shake", -6, "no shaker; a quiet tambourine shake")],
    "triangle.open": [("bell.bell", -8, "no triangle; a small bell is the nearest ringing metal"),
                      ("ride.bell", -12, "last resort: the ride bell, well down in level")],
    "chimes.gliss": [("triangle.roll", 0, "no chimes; a triangle roll is the nearest shimmer")],
    "clap.hit": [("snare.rimshot", 0, "no clap; a rimshot is the nearest sharp backbeat"),
                 ("snare.hit", 6, "then an ordinary snare, lifted")],
    "sticks.hit": [("snare.sidestick", 0, "no sticks; a cross stick is the nearest dry click"),
                   ("woodblock.hit", 0, "then a woodblock")],
}

# Terms that are intentionally terminal: every kit has one, so there is nothing to fall back
# to and nothing is lost by saying so explicitly.
ROOTS = {
    "kick.hit": "every kit has a kick; if a target lacks one there is nothing to substitute",
}

# 1 -> N expansions. offset is in quarter notes.
EXPANSIONS = {
    "hihat.open-close.tip": [
        {"parts": [{"to": "hihat.open.tip"},
                   {"to": "hihat.pedal.chick", "offset_quarters": 0.125,
                    "velocity_scale": 0.7, "duration_quarters": 0.125}],
         "reason": "open-close gesture: the open hit plus the foot closing a 32nd later"},
        {"parts": [{"to": "hihat.open.tip"}], "reason": "open-close without the close"},
    ],
    "hihat.open-close.edge": [
        {"parts": [{"to": "hihat.open.edge"},
                   {"to": "hihat.pedal.chick", "offset_quarters": 0.125,
                    "velocity_scale": 0.7, "duration_quarters": 0.125}],
         "reason": "open-close gesture on the edge"},
        {"parts": [{"to": "hihat.open.edge"}], "reason": "open-close without the close"},
    ],
    "splash.hit": [
        {"parts": [{"to": "crash.hit"},
                   {"to": "crash.hit", "relation": "choke", "offset_quarters": 0.5,
                    "velocity_scale": 0.9, "duration_quarters": 0.125}],
         "reason": "a splash is close to a choked crash: hit, then choke an eighth later"},
    ],
}

# Relations reference a previously sounded event rather than describing a stroke. A target
# emits them as a dedicated note, as channel aftertouch, or not at all.
RELATIONS = [
    (1, "choke", "damps the last event on the referenced instrument"),
    (2, "open-close", "an open stroke followed by the pedal closing"),
]


# --------------------------------------------------------------------------------------
# Emit
# --------------------------------------------------------------------------------------

ROOT = pathlib.Path(__file__).resolve().parents[2]
FIRST_ID = 1001


def build_axes():
    out = {"vocabulary_version": VERSION, "vocabulary_serial": SERIAL, "axes": {}}
    for name, spec in AXES.items():
        vals = []
        for vid, slug, extra in spec["values"]:
            v = {"id": vid, "slug": slug}
            if name == "instrument":
                v["family"] = extra
            elif name == "openness":
                v["scalar"] = extra
            elif name == "ornament":
                v["attacks"] = extra
            vals.append(v)
        entry = {"description": spec["description"], "values": vals}
        for k in ("reserved_families", "value_meaning"):
            if k in spec:
                entry[k] = spec[k]
        out["axes"][name] = entry
    out["reference_axes"] = {
        name: ({"description": s["description"]} if "values" not in s else
               {"description": s["description"],
                "values": [{"id": i, "slug": sl} for i, sl, _ in s["values"]]})
        for name, s in REFERENCE_AXES.items()
    }
    out["controllers"] = [{"id": i, "slug": s, "description": d} for i, s, d in CONTROLLERS]
    out["relations"] = [{"id": i, "slug": s, "description": d} for i, s, d in RELATIONS]
    return out


def build_pivot():
    seen = set()
    terms = {}
    next_id = FIRST_ID
    for t in TERMS:
        if t["slug"] in seen:
            raise SystemExit(f"duplicate slug in mint list: {t['slug']}")
        seen.add(t["slug"])
        entry = {
            "id": next_id,
            "display_name": t["display_name"],
            "status": "active",
            "added_in": VERSION,
            "axes": t["axes"],
        }
        if t["parent"]:
            entry["parent"] = t["parent"]
        if t["role_hint"]:
            entry["role_hint"] = t["role_hint"]
        terms[t["slug"]] = entry
        next_id += 1
    return {"vocabulary_version": VERSION, "vocabulary_serial": SERIAL,
            "next_id": next_id, "terms": terms}


def build_rules():
    return {
        "vocabulary_version": VERSION,
        "vocabulary_serial": SERIAL,
        "axis_degradation": [
            {"axis": a, "from": f, "to": t, "velocity_delta": d, "reason": r}
            for a, f, t, d, r in AXIS_DEGRADATION
        ],
        "curated": {
            src: [{"to": to, "velocity_delta": d, "reason": r} for to, d, r in edges]
            for src, edges in CURATED.items()
        },
        "expansions": EXPANSIONS,
        "roots": [{"term": t, "reason": r} for t, r in sorted(ROOTS.items())],
    }


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--emit", action="store_true",
                    help="write vocabulary/*.json (this is what produced the committed files)")
    args = ap.parse_args()

    axes, pivot, rules = build_axes(), build_pivot(), build_rules()

    known = {name: {v["slug"] for v in spec["values"]} for name, spec in axes["axes"].items()}
    for slug, t in pivot["terms"].items():
        for axis, value in t["axes"].items():
            if axis not in known:
                raise SystemExit(f"{slug}: unknown axis {axis!r}")
            if value not in known[axis]:
                raise SystemExit(f"{slug}: {axis}={value!r} is not a registered value")
        if "parent" in t and t["parent"] not in pivot["terms"]:
            raise SystemExit(f"{slug}: parent {t['parent']!r} does not exist")

    if args.emit:
        for p in (dump(ROOT / "vocabulary/axes.json", axes),
                  dump(ROOT / "vocabulary/pivot.json", pivot),
                  dump(ROOT / "vocabulary/rules.json", rules)):
            print("wrote", p.relative_to(ROOT))
    print(f"{len(pivot['terms'])} terms, ids {FIRST_ID}..{pivot['next_id'] - 1}")
    print(f"{sum(len(a['values']) for a in axes['axes'].values())} axis values "
          f"across {len(axes['axes'])} axes")


if __name__ == "__main__":
    main()
