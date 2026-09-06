status: done
updated: 2026-09-06T13:16:00Z
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
  - the bucket is deliverable as it stands; the queries below would ADD to it, not repair it
next:
  - nothing required. If the supervisor runs the searches under questions, I can fold the
    results in; otherwise the dossier stands and the unreached items are named in its
    self-critique with what each would add.
questions:
  - SEARCHES FOR THE SUPERVISOR TO RUN (worker WebSearch still refuses with 200 of 200).
    Listed in value order. Each line says what the result would resolve.
  - 1. Dorico "Playing Techniques.doricolib" percussion "Rim Shot" OR "Snares Off" technique
    ID - resolves the top unreached item in the dossier: Dorico's percussion playing-technique
    ids. Confirmed so far: the id namespace is pt.* (pt.natural, pt.legato found in public
    third-party expression maps); no percussion pt.* id found anywhere public. A forum post or
    a shared .doricolib containing percussion ids would settle it. Note steinberg.help is now a
    FluidTopics single-page app - its topic URLs return a JS shell to curl and its
    /api/khub/search endpoint 404s - so a search result pointing at a static mirror or a forum
    thread is more useful than a steinberg.help URL.
  - 2. Finale "Percussion Layout Designer" complete list of Note Types default percussion note
    type list - resolves the one Finale gap left: I have 572 Note Types from the shipped
    percussion-map pages, but not the master list the Layout Designer offers. Fetch note: the
    Finale manual pages are reachable by plain curl with a browser user-agent; WebFetch
    summarises them and refuses to reproduce the tables.
  - 3. Sibelius SoundWorld "S3W" primary sound ID list unpitched percussion download - resolves
    whether the 4887 ids I extracted from 17 published sound sets can be split into Sibelius's
    own primary vocabulary and vendor secondary ids. Without it the Sibelius section is
    "ids seen in the wild", not "Sibelius's vocabulary".
  - 4. Kurt Stone "Music Notation in the Twentieth Century" percussion pictogram beater table
    reproduced - the most authoritative source I could not get, and the upstream of BOTH
    MusicXML's and SMuFL's percussion pictograms (the MusicXML XSD says its effect list is
    "in addition to Stone's list"). Any reproduction of the pictogram plates would let the
    reconciliation pass separate Stone's original distinctions from later inventions.
    archive.org has it as a lending item (musicnotationint0000ston_h3s0) and archive.org
    proper answers from here, so an archive.org full-text search may work where Wayback does not.
  - 5. "guz" stroke marching snare drum definition Tapspace - the Finale Note Types "Snare Guz
    Short" and "Snare Guz Long" are marked UNVERIFIED in the dossier; no primary definition found.
  - 6. marching cymbal technique glossary "zing" "smash" "crunch choke" definitions - would
    confirm or refute the dossier's UNVERIFIED note on whether MuseScore's Zing and Smash are
    standard marching terms; Finale independently has Click, Ding and Crunch Choke, so the
    family is real even if the individual names are vendor coinages.
  - 7. vocabulary/axes.json at serial 1 has 14 implement values and does NOT contain fist or
    fingernail, but the round 2 brief text lists both as if present. Which is authoritative?
    No search needed - a repository question. Both are in MusicXML beater-value and SMuFL
    (pictBeaterFist U+E7E5, pictBeaterFingernails U+E7E6), so my gap analysis treats them as
    missing.
  - noted, no action: IRCAM is irrelevant to this bucket - it holds no notation standard, and
    nothing in my candidate register points at it. Wikipedia was not used as a source here.
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
