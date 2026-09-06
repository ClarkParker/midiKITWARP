status: done
updated: 2026-09-06T13:29:00Z
done:
  - dossier written, validated and pushed: docs/research/round2/04-notation-standards.md
    (1783 lines, six sections in the structure the brief prescribes)
  - round A: 15 distinct searches before any extraction; 42 candidates registered with
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
      Finale - the Note Type vocabulary, 572 distinct types, plus the verbatim definitions
      Dorico - the percussion map data model, from the archive.steinberg.help static mirror
      Weinberg / PAS 1994 - the primary standardisation article, read page by page
  - folded in all six supervisor search results (commit d76a29a):
      Dorico: archive.steinberg.help serves real HTML where steinberg.help serves a JS
        shell. Recovered the data model - a drum kit note is the combination of instrument
        and playback playing technique, addressed by a MIDI note plus key switch; both of
        its enumerations are confirmed closed and confirmed UNPUBLISHED. "Not published" is
        a finding, not a gap: every third-party Dorico percussion map was written by someone
        reading the list out of the application's own dialog.
      Sibelius: confirmed and quoted verbatim - "Each unpitched percussion instrument is
        listed as a separate ID, so SoundWorld needs no concept of drum sets", and "in
        SoundWorld each drum sound must be represented by a different ID ... because these
        are not perceived as the same timbre at all". Prior independent confirmation of this
        repository's pivot decision, reached from the playback side around 2007.
      Finale: the three glossary definitions verbatim, plus the cajon worked example - one
        instrument, three techniques, three Note Types, three MIDI notes, one staff line.
      Stone 1980: chapter 10 located as the percussion chapter with exactly the four
        enumerations this bucket extracted from SMuFL and MusicXML, in their original.
        Licence caution recorded: the academia.edu and scribd copies are reference-only.
      marching cymbal terms: negative result recorded as such, with the corps packets named
        and the resolution handed to bucket 08.
  - two corrections to my own earlier text, both now in the dossier:
      "Guz" is NOT an OCR artefact - it occurs twice in vendor HTML in a table where "Buzz"
      occurs nine times, so it is either a real Tapspace stroke or MakeMusic's typo; meaning
      stays UNVERIFIED, spelling is verified
      "choke" stated precisely: it exists in vocabulary/rules.json only as a relation inside
      the splash.hit decomposition, which lets the resolver SYNTHESISE a choke but gives a
      source file no way to STATE one
next:
  - nothing; bucket complete
questions:
  - answered and closed: fist and fingernail are genuinely absent from axes.json serial 1,
    the brief was written from an earlier sketch, the file is authoritative. The dossier now
    says so and treats both as gaps with their MusicXML and SMuFL evidence.
  - no open queries. If bucket 08 resolves "zing", "smash" and "crunch" from the Tapspace
    manual, §3.14(c) of my dossier should be updated with the result; I have flagged it
    there as theirs to resolve.
needs_owner:
  - mint technique "choke"? Six independent sources name it (SMuFL pictChokeCymbal, Guitar
    Pro on five instruments, Sibelius, MuseScore, Finale, Weinberg 1994). The existing
    "choke" relation in rules.json is not a substitute: it synthesises a splash out of a
    choked crash, it does not let an importer record that a crash WAS choked.
    Recommendation: mint it on the technique axis, because every source treats it as a
    named stroke rather than as a degree of damping.
  - site "crossstick" and technique "sidestick" are the same physical act carried on two
    axes; every source in this bucket encodes it once. Recommendation: keep both slugs
    (identifiers are forever) but document one as the canonical encoding before collection
    starts, or two encodings of one event will enter the data.
  - site "bow" collides with the standards' implement "bow" (a violin bow used as a beater,
    MusicXML beater-value bow, SMuFL pictBeaterBow). Recommendation: decide the
    disambiguation now, before an implement "bow" is ever minted.
