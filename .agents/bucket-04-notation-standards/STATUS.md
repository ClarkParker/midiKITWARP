status: running
updated: 2026-09-06T12:58:00Z
done:
  - round A breadth complete: 15 distinct searches, candidate register built
  - SMuFL 1.4: all percussion ranges extracted verbatim from releases/1.4/tables in the
    w3c/smufl clone (128 beaters, 31 playing-technique pictograms, 21 drums, 11 cymbals,
    13 wooden, 9 shakers, 11 bells, 5 gongs, 9 chimes, 19 tuned mallet, 8 misc, 2 metallic,
    11 whistles, 18 handbells, 12 chop, 4 techniques noteheads)
  - MusicXML: every percussion enumeration dumped from the XSD and verified identical
    between tag v4.0 and master; 391 percussion ids from sounds.xml
  - MEI 5: data.ARTICULATION dumped (40 values, closed) - MEI has no percussion technique
    vocabulary at all, it defers to SMuFL glyph names through att.extSym
  - MNX (w3c/mnx master, 2026-08-25): kit / kitComponent / kitNote carry name + midiNumber
    only, no technique enumeration - the MusicXML pictogram vocabulary is not carried over
  - LilyPond drumpitch-init.ly: 65 drum pitch names + 7 drum styles including a
    weinberg-drums-style citing the PAS guidelines
  - Guitar Pro: full articulation list recovered from alphaTab GpifSoundMapper.ts, with GP's
    own implement.action.variant sound ids (stick.hit.rimshot, hand.hit.slap, ...)
  - MuseScore master: 107 percussion instruments with drum entries extracted from
    share/instruments/instruments.xml, including the marching sets
  - Sibelius SoundWorld: grammar from the Sound Set Editor guide, plus 4887 observed
    unpitched sound ids from 17 published sound sets
  - Weinberg, Guidelines for Drumset Notation, Percussive Notes June 1994 p.15-26: reached
    as a scanned PDF and read page by page; this is the PAS standard the task named
next:
  - write docs/research/round2/04-notation-standards.md
questions:
  - the session-wide WebSearch budget (200 calls) was exhausted after my 15th search; later
    breadth had to go through WebFetch and git clone. web.archive.org is blocked outright in
    this environment, so the Wayback fallback in the brief does not work.
needs_owner:
