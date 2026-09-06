status: running
updated: 2026-09-06T13:25:00Z
done:
  - Round A breadth complete, 18 distinct searches across register, language, source type and era
  - MuseScore ground truth extracted: all four Marching_*.drm and the five marching-percussion
    instruments.xml entries, with pitch, staff line, notehead group and SMuFL glyph name
  - Provenance of MuseScore's names settled from git history in a deepened clone:
    instruments.xml marching group added 2013-07-01 f95f3e5459 by Michael Cowgill, remapped
    2017-06-23 5f8cac1369 by lasconic; the four .drm files added 2024-07-27 c7dc55ea2d by
    Peter Jonas, "Apply Muse Drumline drumset definitions to MDL1 instruments".
    "Ping Shot" and "Gok Shot" appear nowhere in MuseScore before that 2024 commit.
  - Tapspace Virtual Drumline 2.5 User Guide v.2.5.6 (112 pp) retrieved and mined: VDL has
    Ping Shot, RIM SHOTS, Backsticks, Cross stick Rim Knock, Stick Shot, Snare shell,
    FAT/DRY crush, Spock 1/2, Skank, Double-stop on lower shells, Vacuum Suck, Ding, Zing,
    Crunch Choke — and no "gock" or "gok" anywhere
  - Five marching cymbal technique packets and two technique manuals extracted verbatim
next:
  - Write docs/research/round2/08-marching-percussion.md
questions:
  - WebSearch budget for this session is exhausted (200/200); remaining work is WebFetch and
    curl against URLs already discovered
  - snarescience.com returns HTTP 500 and web.archive.org is blocked from this environment,
    so the drum-corps forum record of "gock/gawk" could not be read directly
needs_owner:
