status: done
updated: 2026-09-06T13:14:17Z
done:
  - Dossier written and pushed: docs/research/round2/08-marching-percussion.md
  - Round A: 18 distinct searches (register, language, source type, era); 49-row candidate
    source register, 32 of them reached
  - The bucket's assigned question is answered. MuseScore's marching names come in two
    layers with different authorities. Layer 1, commit f95f3e5459 (2013-07-01, Michael
    Cowgill), brought Shell, Backstick (then named "Visual (BS,X-Over,Etc)"), Battery
    Snare, Buzz, Spock, Full/Half Crash, Bell Tap, Smash, Zing, Roll. Layer 2, commit
    c7dc55ea2d (2024-07-27, Peter Jonas, "Apply Muse Drumline drumset definitions to MDL1
    instruments"), brought Gok Shot, Ping Shot, Back Stick, Hit, Crunch (HH), Punch, Ting,
    Suc. "Ping Shot" and "Gok" appear nowhere in MuseScore before that 2024 commit.
  - The ultimate authority for most of the set is Tapspace Virtual Drumline; its 112-page
    2.5.6 user guide was retrieved and mined and ships Ping Shot, RIM SHOTS, Backsticks,
    Cross stick Rim Knock, Stick Shot HIGH/LOW, Snare shell, Double-stop on lower shells,
    Spock 1/2, Skank, Vacuum Suck, Ding, Zing, Crunch Choke, FAT/DRY crush
  - Section 0 rules on the three terms v0.1 has already minted. ping-shot: authority found
    (Tapspace ships it as a literal articulation name on five snare instruments; SUU 2025
    packet writes it above the stave; two further definitions). stick-shot: authority found
    (Modern Drummer, Steve Fidyk, July 2013, verbatim; SMuFL pictStickShot U+E7F0;
    Tapspace Stick shot HIGH/LOW). gok-shot: NO AUTHORITY FOR THE NAME. The spelling "Gok"
    exists only in Muse Drumline via that one MuseScore commit; Tapspace never uses the
    word in any spelling; the only definition of the concept is an uncited Wikipedia
    paragraph; and the sourced reference works that do write "gock" mean the small tenor
    accent drum, not a stroke.
  - Section 2.7.1 answers the supervisor's cymbal-corroboration request, and CORRECTS the
    negative result relayed to me. The marching cymbal set does not stand on Tapspace
    alone: zing has 6 independent non-Tapspace sources with definitions (GVSU, Rhythm
    Armada, Oregon State, PCHS, Missouri State, marchingcymbalstechnique), suck/succ has 4
    plus a mechanism corroboration from Ohio State ("offset to prevent suctioning"), crunch
    has 2. Only smash is thin: PCHS handbook p. 12 alone under that name. Oregon State's
    ten "crunches" are abdominal exercises, a false positive now recorded as such.
  - Both sources the supervisor named were fetched. Ohio State TBDBITL Marching
    Fundamentals names five cymbal positions (Traditional, Vertical A/V, Traditional
    hi-hat, Gumption, Punch) and no effect sounds; it independently corroborates Gumption
    and places Punch LOW on the body, supporting the finding that MuseScore's Punch at
    pitch 79 is mislabelled as a crash choke. coreypearce.com/marching-cymbals-101 is a
    video-course index that defines nothing. Both recorded as negative results.
  - Single-source names now sit in the gaps section beside gok-shot: smash (PCHS only),
    crunch-choke as a compound (Tapspace only), whale-call (Tapspace only), weedwacker
    (GVSU only), and Half Crash, which MuseScore has shipped since 2013 and which is
    attested in no source reached at all.
  - 14 terms recorded that fit NO axis, including "on cage" and the harness/stand strikes
    (site has no value for mount hardware), unison/split (a 1-to-N relation, not a tuple),
    solo-versus-section, "snenor" imitative voicing, and the marching-cymbal holding
    position dimension that all five packets organise themselves by
  - Two corrections to round 1: Marching_Tenors.drm has 20 entries and only two Shell
    entries (Drum 3, Drum 4), not 22 and six; and round 1 missed the fifth marching
    instrument, marching-show-tenors
  - Internal MuseScore contradictions documented: Spock 1 vs Spock 2 ordering differs
    between instruments.xml and Marching_Tenors.drm; pitch 79 is Punch in one file and
    Crash-Choke in the other; pitch 89 is Suc in one and Smash in the other
  - Verified before each commit: tools.validate 47 groups passed, tools.format canonical,
    iom roundtrip 11/11
next:
  - Nothing. Bucket complete.
questions:
  - For the notation bucket, via the supervisor: zing, suc/suck and ding/bell-tap can have
    their UNVERIFIED marks dropped, with the locators in section 2.7.1. crunch is thin but
    real. smash should stay marked, and "crunch choke" as a compound is Tapspace-only.
  - Is "guz" (Tapspace VDLite Finale map, notes 53 and 54, "Snare Guz Short" / "Snare Guz
    Long") a real marching snare term, and does it mean a crush? Found and recorded, not
    definable from any source reached. This is the one search I would spend supervisor
    budget on.
  - Does the PAS publication "Terms Used in Percussion" (Percussive Notes, Jan 1986) or
    "Notation for Percussion Instruments" define any marching stroke names? Both are behind
    the PAS member paywall. My conclusion that no PAS marching standard exists is an
    absence produced by a paywall, not evidence of absence.
  - Michael Udow, Percussion Pedagogy (OUP 2019) p. 363 is the only scholarly definition of
    the spock drum and could not be reached; Google Books shows no preview of that page and
    the Books API returns HTTP 429 project quota for the day.
  - Why does instruments.xml number Spock 2 above Spock 1 when both Tapspace maps and
    MuseScore's own .drm number Spock 1 higher? musescore.org issue #196321 and node 109826
    would settle it; both sit behind Cloudflare and refuse WebFetch and curl.
needs_owner:
  - technique.gok-shot has no authority for its name (full argument in section 0 of the
    dossier). Three options, and identifiers are forever so a worker must not choose.
    Recommendation: keep the slug, add a correction alias gock-shot plus an alias
    gawk-shot, and record its provenance as "Muse Drumline, single vendor, concept
    uncited". Alternative worth weighing: retire the name in favour of rimshot plus
    position=centre, which is what the only definition literally describes.
  - Should ping-shot, gok-shot and rimshot stay three sibling technique values? Every
    authority reached describes them as ONE technique at three striking positions
    (perimeter / offset / centre). Recommendation: keep all three slugs, and add a rule in
    rules.json that ping-shot and gok-shot imply technique=rimshot with the position set,
    so a converter can still tell that a ping shot is a rimshot.
  - Marching is a missing instrument family. The reserved families (perc.*, orch,
    electronic, utility, unknown) have nowhere for marching-snare, marching-tenor, spock,
    marching-bass and marching-cymbals, and marching is not a subset of orch: its
    instruments, its numbering and its technique names are all distinct.
    Recommendation: reserve a marching.* family.
