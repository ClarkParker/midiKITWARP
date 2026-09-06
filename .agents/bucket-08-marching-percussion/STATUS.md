status: done
updated: 2026-09-06T13:20:51Z
done:
  - Dossier written and pushed: docs/research/round2/08-marching-percussion.md
  - Round A: 18 distinct searches; 59-row candidate source register, 39 of them reached
  - PROVENANCE ANSWER. MuseScore's marching names come in two layers with different
    authorities. Layer 1, commit f95f3e5459 (2013-07-01, Michael Cowgill), brought Shell,
    Backstick (then named "Visual (BS,X-Over,Etc)"), Battery Snare, Buzz, Spock, Full/Half
    Crash, Bell Tap, Smash, Zing, Roll. Layer 2, commit c7dc55ea2d (2024-07-27, Peter
    Jonas, "Apply Muse Drumline drumset definitions to MDL1 instruments"), brought Gok
    Shot, Ping Shot, Back Stick, Hit, Crunch (HH), Punch, Ting, Suc. "Ping Shot" and "Gok"
    appear nowhere in MuseScore before that 2024 commit. Tapspace Virtual Drumline is the
    ultimate authority for most of the set; its 112-page 2.5.6 user guide was retrieved.
  - FOR THE RUDIMENTS BUCKET, back-stick is attested, and better than any other term here.
    Section 2.5.1 gives the chain: Joe Marrella in Drum Corps World Vol. 36 No. 15, Dec
    2007, and the World Drum Corps Hall of Fame bio of John Dowlan, for development from
    1935 at the Osmond Post Cadets and the USAF Drum Corps introducing it in 1957-58; then
    Ellis Mirsky (Field Drums, 2009-01-03) overturning the 1938 date with an Armstrong & Co.
    lithograph, "A.R. Carrington, champion drum soloist, 1870s", NYPL call no. PC
    MUSIC-Dru, Digital ID 832408, showing Carrington mid-backsticking-flip, corroborated by
    a Utica New York Observer review of 1878-07-03. Named inventor, dates, institution,
    19th-century artefact.
  - This also CORRECTS my own earlier claim that nothing in this bucket predates 1970, and
    it vindicates MuseScore's original 2013 name for pitch 60: the 1878 review describes
    the backstick flip and the stick tosses in one sentence, exactly as
    "Visual (BS,X-Over,Etc)" grouped them.
  - Casey Claw added as direct marching evidence that implement needs `fist`, which the
    brief lists but axes.json v0.1 omits, and that contact needs `butt` as first-class:
    "the first note of every right hand double is played with the butt end … the very next
    note … with the tip".
  - guz is now BOUNDED, not guessed (section 2.4.1). Confirmed in three Finale editions
    (2012 Win, Mac, 2014 Mac) as Snare Guz Short (53) / Snare Guz Long (54); absent from
    Tapspace's own 112-page manual, from all five packets, from Blakley, from drumming.com's
    250-term glossary, and from the supervisor's two further searches. A shipping term with
    no published definition anywhere reachable. The crush inference is recorded as
    UNVERIFIED and must not be minted.
  - Thom Hannum, Basic Snare Drum Technique (Pearl, 13 pp) fetched: NEGATIVE RESULT, and
    itself a finding (section 2.5.2). The standard free primer by a leading marching
    pedagogue names none of backstick, rimshot, ping, gock, stick shot, cross stick, rim
    click, shell or crush. Striking-position vocabulary lives in sample-library keymaps and
    individual programmes' packets, not in general snare pedagogy.
  - Section 0 rules on the three terms v0.1 has minted. ping-shot: authority found
    (Tapspace ships it as a literal articulation name on five snare instruments; SUU 2025
    packet writes it above the stave; two further definitions). stick-shot: authority found
    (Modern Drummer, Steve Fidyk, July 2013, verbatim; SMuFL pictStickShot U+E7F0).
    gok-shot: NO AUTHORITY FOR THE NAME; only definition of the concept is an uncited
    Wikipedia paragraph, and the sourced works that write "gock" mean the tenor drum.
  - Section 2.7.1 corrects the relayed cymbal negative: zing has 6 independent non-Tapspace
    sources with definitions, suck 4 plus Ohio State corroborating the mechanism, crunch 2.
    Only smash is thin (PCHS p. 12 alone under that name).
  - Single-source list, all flagged in section 5.1 item 5: gok-shot, smash, crunch-choke as
    a compound, whale-call, weedwacker, guz, and Half Crash, which MuseScore has shipped
    since 2013 and which is attested nowhere at all.
  - 14 terms recorded that fit NO axis; two corrections to round 1 (Marching_Tenors.drm has
    20 entries and two Shell entries, not 22 and six; round 1 missed marching-show-tenors);
    three internal MuseScore contradictions documented (Spock ordering; pitch 79 Punch vs
    Crash-Choke; pitch 89 Suc vs Smash)
  - Verified before each commit: tools.validate 47 groups passed, tools.format canonical,
    iom roundtrip 11/11
next:
  - Nothing. Bucket complete.
questions:
  - For the rudiments bucket, via the supervisor: back-stick can have its unattested mark
    removed, with the locators in section 2.5.1 of this dossier. It is the best-sourced
    term in bucket 08.
  - For the notation bucket: zing, suc/suck and ding/bell-tap can have their UNVERIFIED
    marks dropped, with the locators in section 2.7.1. crunch is thin but real. smash
    should stay marked, and "crunch choke" as a compound is Tapspace-only.
  - guz needs no further search; two of mine and two of the supervisor's have bounded it.
    The one route left that could define it is Tapspace's separate "VDL Keymaps PDF
    (v2.5.5)", referenced by their support pages. I could not find a direct link on
    support.tapspace.com/support/solutions/articles/26000029921 (no .pdf href in the
    served HTML). If anyone can obtain that file, it is the single most likely place for a
    per-sound gloss.
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
  - technique.gok-shot has no authority for its name (full argument in section 0).
    Identifiers are forever, so a worker must not choose. Recommendation: keep the slug,
    add a correction alias gock-shot plus an alias gawk-shot, and record its provenance as
    "Muse Drumline, single vendor, concept uncited". Alternative worth weighing: retire the
    name in favour of rimshot plus position=centre, which is what the only definition
    literally describes.
  - Should ping-shot, gok-shot and rimshot stay three sibling technique values? Every
    authority reached describes them as ONE technique at three striking positions
    (perimeter / offset / centre). Recommendation: keep all three slugs, and add a rule in
    rules.json that ping-shot and gok-shot imply technique=rimshot with the position set.
  - Marching is a missing instrument family. The reserved families have nowhere for
    marching-snare, marching-tenor, spock, marching-bass and marching-cymbals, and marching
    is not a subset of orch. Recommendation: reserve a marching.* family.
  - implement is missing `fist`. The brief lists it, axes.json v0.1 does not have it, and
    the Casey Claw gives a marching source for it. Recommendation: mint it; check whether
    `fingernail`, also listed in the brief and also absent, has a source in another bucket.
