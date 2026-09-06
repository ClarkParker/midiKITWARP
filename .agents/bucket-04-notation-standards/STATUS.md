status: done
updated: 2026-09-06T13:08:00Z
done:
  - dossier written, validated and pushed: docs/research/round2/04-notation-standards.md
    (1663 lines, six sections in the structure the brief prescribes)
  - round A: 15 distinct searches before any extraction; 41 candidates registered with
    locators and a reached/not-reached verdict each
  - round B, all enumerations complete and verbatim from the machine-readable form:
      SMuFL 1.4 - 306 percussion glyphs across 16 ranges, taken from releases/1.4/tables
        and diffed against data/ranges to prove the percussion vocabulary is unchanged
        since 1.4 (0 added, 0 removed; only articulation and tremolos have moved)
      MusicXML - 13 enumerations from the XSD, verified byte-identical between tag v4.0
        and the 4.1 draft, plus 391 percussion ids from sounds.xml
      MEI 6.0-dev - data.ARTICULATION (40, closed) and data.NOTEHEADMODIFIER (10, closed)
      MNX - the kit / kitComponent / kitNote model from the metaspec
      LilyPond - 65 drum pitch names, 65 abbreviations, 7 drum styles
      Guitar Pro - 90 articulations with GP's implement.action.variant sound ids
      MuseScore - 107 percussion instruments, incl. the four marching sets
      Sibelius - the SoundWorld id grammar plus 4887 observed unpitched ids
      Finale - the Note Type vocabulary, 572 distinct types across the map pages
      Weinberg / PAS 1994 - the primary standardisation article, read page by page
  - two findings the reconciliation pass should not have to rediscover:
      MEI has no percussion vocabulary at all and delegates to SMuFL glyph names, and MNX
      has replaced MusicXML's pictogram enumerations with {name, midiNumber} - the
      note-number pivot loss written into a draft W3C specification
      SMuFL encodes centre and rim three times each, once per notational authority
        (Weinberg, Ghent, Caltabiano), so a glyph list cannot be minted one-to-one
  - axis mapping done for every extracted term, with eleven kinds of term that fit no axis
next:
  - nothing; bucket complete
questions:
  - vocabulary/axes.json at serial 1 has 14 implement values and does NOT contain fist or
    fingernail, but the round 2 brief text lists both as if they were present. Which is
    authoritative? Both are in MusicXML beater-value and in SMuFL (pictBeaterFist U+E7E5,
    pictBeaterFingernails U+E7E6), so the gap analysis treats them as missing.
  - the shared WebSearch budget refused calls for this worker even after the supervisor
    reported it had recovered; three items were chased by direct HTTP instead and two of
    them succeeded (Finale, Weinberg).
needs_owner:
  - mint technique "choke"? Six independent sources name it (SMuFL pictChokeCymbal, Guitar
    Pro on five instruments, Sibelius, MuseScore, Finale, Weinberg 1994) and v0.1 cannot
    express a choked cymbal at all. Recommendation: mint it on the technique axis rather
    than as a damping value, because every source treats it as a named stroke.
  - site "crossstick" and technique "sidestick" are the same physical act carried on two
    axes; every source in this bucket encodes it once. Recommendation: keep both slugs
    (identifiers are forever) but document one as the canonical encoding before collection
    starts, or two encodings of one event will enter the data.
  - site "bow" collides with the standards' implement "bow" (a violin bow used as a beater,
    MusicXML beater-value bow, SMuFL pictBeaterBow). Recommendation: decide the
    disambiguation now, before an implement "bow" is ever minted.
