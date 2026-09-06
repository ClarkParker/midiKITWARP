status: done
updated: 2026-09-06T12:57:29Z
done:
  - dossier committed and pushed at docs/research/round2/07-world-percussion.md
  - round A: 20 distinct searches across seven traditions in English, Spanish,
    Portuguese, French, German and transliterated Persian, Arabic, Hindi,
    Japanese, Korean and Chinese; candidate register of 70 sources, 34 reached
  - round B: verbatim stroke tables extracted from primary and peer-reviewed
    sources, not from sample-library marketing. The load-bearing ones are the
    ISMIR 2014 Beijing opera paper (luogujing syllable to instrument-combination
    table, Table 1), the ISMIR 2021 tabla paper (bol to damped / resonant-treble
    / resonant-bass / resonant-both, Table 1, with explicit kick-snare-hihat
    equivalents), the Zenodo Mridangam Stroke Dataset (ten labels under a DOI),
    Nasehpour on the tonbak (eleven strokes with Persian script), Pertout's
    conga strokes from an MPhil thesis, the Biagioni UFU pandeiro dissertation
    (appendix B, twelve articulations each decomposed into contact, region and
    damping), the Taiko USA kuchi-shoga table, and Piulestan Nieto on the
    flamenco cajon
  - the per-instrument stroke set is section 3.1: a fourteen-tradition matrix
    showing bass, open, muted, slap, heel, tip and rim recurring across
    unrelated families. Every bass cell is centre-of-head with the palm and
    every open cell is near the edge with the fingers, in the sources' own
    words. The strokes are defined physically by site, position, contact and
    damping, not as atomic techniques, which is the axis decomposition
  - section 3.4 lists the eleven kinds of term that fit NO axis, with at least
    two independent traditions each: ensemble-combination names, pitch bend by
    pressure, friction as distinct from scrape, instrument re-orientation,
    ensemble role as distinct from instance ordinal, playing posture, named
    patterns, the finger snap, cross-hand damping, school lineage, and notated
    rests. Two candidate missing axes follow from these: role, and a pitch-bend
    scalar analogous to openness
  - section 4.6 flags the collision that will silently corrupt data: v0.1
    technique heel, toe and thumb are hi-hat pedal terms, and in every tradition
    in this bucket they are hand terms. Identifiers are forever, so this needs
    new slugs plus a documented alias note, not a rename
  - section 5.3 records the positive result: v0.1 technique already contains
    slap, open-tone, bass-tone, mute-stroke, heel, toe, thumb, gliss, scrape and
    shake, which is exactly the recurring set, minted before this bucket looked
    outside Cuba. No tradition needed a primary stroke term outside it except
    snap
  - the question referred here by the vendor-glossary worker is answered in
    section 2.2.1 and summarised in 6.5. Cascara, paila and abanico all have
    text definitions with locators. Dicciani 2009 defines cascara verbatim and
    records that the word has migrated from naming a site to naming a pattern;
    paila carries two incompatible senses, the instrument and the shell; abanico
    is a rimshot then a 7- or 9-stroke roll then a rimshot on the macho, which
    contradicts the round A guess of a rim-to-head sweep, so that guess is
    dropped rather than carried as unverified
  - python -m tools.validate, python -m tools.format --check and
    python -m tools.iom.roundtrip_check data/legacy-iom all pass
next:
  - nothing; bucket complete
questions:
  - Sabar stroke names are the largest hole. Utrecht's Drum Languages Project
    states there are at least nine named strokes and that every stroke has a
    name, but neither reached source lists one. Patricia Tang, Masters of the
    Sabar, Temple University Press 2007, is the standard monograph and is the
    place to look. Reaching it needs a search, and the session WebSearch pool
    was spent before round B
  - The Javanese and Balinese kendang stroke syllabary was not obtained;
    ragakusuma.org returned 503 and the ScienceDirect gamelan notation dataset
    is paywalled. Indonesia is the one major tradition in this bucket left with
    essentially no stroke vocabulary
  - Korean janggu gi, gideok and gigideok remain UNVERIFIED; the Graz
    ethnomusicology page confirms the syllable system exists but lists no
    syllables
  - The Brazilian material outside pandeiro rests on Wikipedia alone. The surdo
    open versus abafado pair, one of the most-used articulations in the bucket,
    is explicitly marked UNVERIFIED
needs_owner:
  - Whether world percussion terms should reuse the v0.1 slugs heel, toe and
    thumb, which currently mean hi-hat pedal actions, or mint distinct hand
    slugs such as palm-heel and finger-tip. Section 4.6 recommends distinct
    slugs, because a conga toque de talon mapped onto technique.heel reads in
    the kit sense as heel-down on a pedal. Identifiers are forever, so this
    cannot be corrected later by renaming
  - Whether to add a pitch-bend or pressure-modulation axis. Section 3.4 item 2
    finds it independently in mridangam gumiki, tabla bayan modulation, kanjira,
    cuica and the conga moose call. It behaves exactly as openness does for the
    hi-hat, an ordered scalar with named anchors driven by a continuous physical
    control, so the model already has the shape for it
  - Whether ensemble role, section 3.4 item 5, belongs on the layout slot beside
    instance. Quinto versus salidor, sangban versus dununba, marcacao versus
    resposta and polos versus sangsih are functional roles, not pitch ordinals,
    and macho and hembra is a gendered pair with no third position at all
