## bucket-01-rudiments-stroke-technique  (done, 1 items)
  - Fritz Berger, "Das Basler Trommeln. Sein Werden und Wesen" (Trommel-Verlag
    Basel 1928) remains the one source only the owner can get: in print from Musik
    Hug (Zurich) and Percussion Brandt (Germany), digitised nowhere reachable.
    NOTE: the earlier alternative recommendation is now DISCHARGED - the Rudimental
    Codex was obtained and delivered the trilingual names. What Berger would still
    add is narrower than before: the Codex maps Basel figures that have an American
    counterpart, so it cannot give the figures that have none, it is not the Basel
    school's own Grundstreiche curriculum, and it does not explain either Basel
    notation system. Recommendation: buy it only if the Basel-specific figures and
    the Hieroglyphenschrift matter to the vocabulary; the pan-European layer is now
    covered without it

## bucket-02-orchestral-treatises  (done, 1 items)
  - Elaine Gould, Behind Bars (2011) is openly posted at archive.org
    `behind-bars-by-elaine-gould` with no stated licence, and it has a substantial
    percussion chapter. I registered it with its locator and deliberately did not quote
    from it, per CLAUDE.md rule 2 and the supervisor's instruction on unauthorised
    mirrors. If the owner has a bought copy, that chapter is worth a pass by someone who
    may quote it - and it would also settle whether it belongs to this bucket or to the
    notation-standards one.

## bucket-03-organology-thesauri  (done, 3 items)
  - ADR-0004 defines reference-only as "may be cited in documentation; never
    ingested at all", which read literally forbids putting a third-party
    identifier into data/. Recommendation: amend ADR-0004 to say that an
    outbound cross-reference belongs to the provenance layer rather than to the
    shipped assertion. Without that amendment the xref block recommended in
    section 0.4 cannot be implemented as written.
  - Cheap and permanent: write to MIMO and ask for a licence statement. The
    thesaurus publishes none anywhere reachable, and an answer removes the only
    licence uncertainty in this bucket.
  - Three structural findings for reconciliation. Section 5.3, sizzle-ride names
    a riveted ride and is a mechanism value, not an instrument, exactly as
    wires-on is for the snare. Section 4.8, site bow collides with the
    implement bow that bowed cymbals will need; reported by three buckets
    independently. Section 4.2, a bare Hornbostel-Sachs notation is not a stable
    identifier, HS-15 means Metal sheets in MIMO and Stampf-Idiophon in the
    ACDH-CH implementation, so any notation must be version-pinned.

## bucket-04-notation-standards  (done, 3 items)
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

## bucket-05-mma-normative  (done, 2 items)
  - vocabulary/axes.json needs a way to express an UNDIRECTED exclusion class ("only
    one of these may ring"). Five independent standards encode it (GM2 EXC1-7,
    M2-125-UM MES 1-7, Yamaha Alternate Group, Roland [EXC1]-[EXC8], DLS2 usKeyGroup);
    v0.1 has only the directed relations.choke. Recommendation: add it before any
    device data is collected, since it changes what openness and damping mean.
  - reference_axes.instance fixes cymbal order "left to right from the player's seat".
    GM2 Appendix B and M2-125-UM Table 5 recommend pan from the AUDIENCE's side
    (hi-hat right, ride left, toms ascending in pitch left to right). Either convention
    is defensible; the owner should pick one and have it written down, because an
    exporter deriving pan from instance will otherwise mirror every MMA table.

## bucket-06-vendor-glossaries  (done, 5 items)
  - Cymbal build vocabulary (alloy B8/B10/B12/B20, hammering pattern, lathing,
    finish brilliant/raw/sandblasted, profile, weight) is fully primary-sourced
    and maps to NO axis. It is not miking, so it is not `voicing` as currently
    documented, yet libraries ship these as distinct kit pieces.
    Recommendation: widen `voicing` from "kit or miking variant" to "build or
    model variant of the same instrument" rather than mint a new axis, because a
    new axis would multiply the sparse tuple for a distinction that is almost
    always carried in the kit-piece name anyway.
  - Sound-character adjectives: v0.1 has adopted exactly three of them (`dark`
    on voicing, `tight`/`loose` on openness) out of the thirty Sabian defines.
    Recommendation: rule the sound-character vocabulary out of scope explicitly
    and document `dark` as a voicing label that happens to share a vendor word,
    so no future worker is tempted to import the other twenty-seven.
  - Is a piccolo snare its own `instrument` or a `voicing` of `snare`?
    Recommendation: `voicing`, because the trade sells it as a size variant of a
    snare drum and not as a different instrument.
  - Is a concert tom its own `instrument` or a `tom` with no resonant head? No
    current axis expresses head-absence. Recommendation: mint it as its own
    instrument value rather than add a head-count axis for one case.
  - `gated` currently sits on the `damping` axis next to `towel`. It is a
    production process, not a physical damper, and no manufacturer names it.
    Recommendation: keep it, but document the axis as "what shortens the sound,
    physically or in production", so the mixed membership is deliberate.

## bucket-07-world-percussion  (done, 4 items)
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
    resposta, polos versus sangsih and lanang versus wadon are functional roles,
    not pitch ordinals, and macho and hembra is a gendered pair with no third
    position at all
  - Whether the axis set should state explicitly that the implement moves and
    the instrument is static. Section 3.4 item 4 shows the tamborim inverts
    this, and the inversion is what produces the note. Either the assumption is
    written down and the tamborim is documented as out of scope, or a term is
    needed for it

## bucket-08-marching-percussion  (done, 3 items)
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

## bucket-09-library-primary-manuals  (done, 1 items)
  - Toontrack SD3 and EZdrummer 3 are the largest articulation corpus in the field and
    Toontrack publishes NOTHING on the open web: manual behind an account login, no drum
    maps offered, last public PDF manual from 2009, and no mirror on archive.org. Round 1
    used community .drm and .pitchlist exports, which rule 2 forbids as a shipped source.
    This pass corroborated Toontrack's naming convention against Toontrack's own SD2 and
    EZdrummer 1 manuals, but that is a 2009 generation. The only lawful route to the
    current layout is a Toontrack account - free registration reads the web manual, and
    the layout is visible in-product under Settings > MIDI In/E-Drums.
    Decision: does the owner supply that, or does KITWARP ship with Toontrack recorded as
    a documented gap? Recommendation: supply it. Everything else in this bucket is now
    vendor-sourced, and Toontrack is the one library whose absence would be conspicuous.
```

## bucket-10-hardware-primary-docs  (done, 1 items)
  - Whether unlicensed third-party scans on archive.org (TR-808 and TR-727
    owner's manuals, TR-909 service notes, LinnDrum, Oberheim DMX, SP-1200) may
    be used as a WORKLIST to decide what to look for, given rule 2 says curated
    third-party collections are never the shipped source. I treated them as
    worklist-only and recorded every claim with its scan identifier, but the
    drum-machine voice names in the dossier have no licence-clean source and
    the manufacturers do not publish these documents at all.

## bucket-11-acoustics-and-timbre  (done, 3 items)
  - Whether to reduce the openness anchors from eight to five, aliasing closed-loose,
    quarter and three-quarter onto the retained anchors. Recommendation: yes. This
    changes the vocabulary, and CLAUDE.md rule 5 says nothing is collected against an
    unapproved vocabulary, so it has to be decided before collection starts.
  - Whether the position value `offset` keeps its slug. No acoustics source names it and
    its place in the ordering has no physical basis. Recommendation: keep the id, get a
    locator for it from a vendor bucket, or alias it onto halfway or perimeter.
  - Whether to buy or borrow Rossing, Science of Percussion Instruments (World Scientific
    2000). It is the single most authoritative source not obtained and would close three
    of the four UNVERIFIED marks in the dossier. A full-text mirror of the companion
    Fletcher and Rossing volume exists but its licence is unknown, so under CLAUDE.md
    rule 2 it was deliberately left unread rather than quoted.

## bucket-12-german-french-italian  (done, 2 items)
  - Section 5.2 argues instrument.crash will be ambiguous once the orchestral family
    is minted: every non-English orchestral source reached uses crash for the CLASHED
    PAIR, while KITWARP's crash is the kit's single suspended cymbal. Since ids are
    forever under ADR 0003, the orchestral pair needs its own slug decided before the
    orchestral family is minted, not after. Recommendation: mint a distinct slug for
    the clashed pair now and leave crash as the kit cymbal.
  - The BRIEF's axis sketch lists 'fist' under implement but vocabulary/axes.json does
    not contain it. One of the two is wrong. Recommendation: treat axes.json as
    authoritative and correct the brief.

