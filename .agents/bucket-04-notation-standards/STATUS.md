status: running
updated: 2026-09-06T12:52:00Z
done:
  - round A breadth complete: 15 distinct searches (SMuFL, MusicXML XSD, MusicXML standard
    sounds, MEI, Dorico doricolib, Sibelius SoundID, Finale percussion maps, LilyPond
    drumPitchNames, Guitar Pro, PAS/Weinberg, Gould Behind Bars, German Schlagzeug-Notation,
    French modes de jeu, MNX, Kurt Stone / Smith Brindle)
  - cloned w3c/smufl, w3c/musicxml (plus tag v4.0) and music-encoding/music-encoding into
    scratch; all three reachable via git clone as the brief predicted
  - SMuFL 1.4 released tables parsed out of releases/1.4/tables: 128 beaters, 31 percussion
    playing technique pictograms, 21 drums, 11 cymbals, 13 wooden, 9 shakers, 11 bells,
    5 gongs, 9 chimes, 19 tuned mallet, 8 miscellaneous, 2 metallic, 11 whistles,
    18 handbells, 12 chop, 4 techniques noteheads
  - MusicXML percussion enumerations dumped from the XSD; verified that every percussion
    enumeration is byte-identical between tag v4.0 and current master (4.1 draft)
  - MusicXML 4.0 sounds.xml: 391 percussion sound ids extracted (drum 137, metal 78,
    pitched-percussion 64, effect 63, wood 27, rattle 22)
  - LilyPond drumPitchNames source file fetched from GitLab (GPL, rederive-only)
next:
  - MEI ODD extraction, then Dorico / Sibelius / Finale / MuseScore / Guitar Pro vocabularies
  - write docs/research/round2/04-notation-standards.md
questions:
  - the session-wide WebSearch budget (200 calls) was exhausted after my 15th search, so all
    further breadth had to run through WebFetch on known URLs and through git clones. If a
    later worker needs search, the supervisor has to raise
    CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.
needs_owner:
