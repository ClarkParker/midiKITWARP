status: running
updated: 2026-09-06T12:52:00Z
done:
  - Setup complete; branch pushed
  - Round A: 16 distinct searches run (English, German, Japanese; standards bodies,
    vendor manual libraries, notation vendors, mobile-audio registries)
  - MAJOR: AMEI (Japan MIDI Standards Committee) publishes the MMA Recommended
    Practice PDFs free at amei.or.jp/midistandardcommittee/RP&CAj.html - including
    the ENGLISH normative GM2 spec RP-024 v1.2a. midi.org paywalls the same document.
  - Obtained and text-extracted: GM2 RP-024 v1.2a (normative Appendix B percussion
    sound set, with PAN column and [EXC1]-[EXC7] mutual-exclusion groups that the
    round-1 secondary tables omit entirely)
  - Obtained: Roland SC-88, SC-88Pro, SC-8850 Owner's Manuals from cdn.roland.com
    (Roland's own PDFs); Yamaha MU100 Sound List (usa.yamaha.com) with the
    XG Drum Map including normative Key-Off and Alternate-Group columns
  - First confirmed errors in docs/research/03-midi-standards.md: XG Standard Kit
    note names 17,18,26,28,31,33,35,36,38,40 are wrong (VMPK-derived names differ
    from Yamaha's own XG Drum Map)
next:
  - Verify XG naming against an earlier Yamaha data list (MU50/MU80) to rule out an
    MU100-era rename
  - Extract Roland SC-55/SC-88 drum set tables from Roland's own manuals
  - Get the MIDINameDocument DTD (midi.org/dtds path now 404s; try Wayback / Ardour)
  - DLS1/DLS2, SP-MIDI, MPE, MIDI 2.0 UMP, SysEx ID list
questions:
needs_owner:
