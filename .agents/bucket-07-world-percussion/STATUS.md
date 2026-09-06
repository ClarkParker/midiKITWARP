status: done
updated: 2026-09-06T13:19:30Z
done:
  - dossier committed and pushed at docs/research/round2/07-world-percussion.md
  - round A: 20 distinct searches across seven traditions in English, Spanish,
    Portuguese, French, German and transliterated Persian, Arabic, Hindi,
    Japanese, Korean, Chinese and Wolof
  - candidate source register: 99 entries, 51 reached directly, a further 8
    reached indirectly through a source that quotes them with a page number
  - round B first pass: ISMIR 2014 Beijing opera luogujing table, ISMIR 2021
    tabla four-way bol table with kick-snare-hihat equivalents, Zenodo
    Mridangam Stroke Dataset, Nasehpour on the tonbak, Pertout's conga strokes
    from an MPhil thesis, the Biagioni UFU pandeiro dissertation appendix,
    the Taiko USA kuchi-shoga table, Piulestan Nieto on the flamenco cajon
  - round B second pass, reopened after the search pool recovered, closed all
    four gaps left open by the first pass:
      sabar CLOSED at authority A from Ros 2021, Frontiers in Communication
      6:643683, Table 1 "Sabar phonemes", all nine strokes verbatim with
      variants and corpus frequencies, corroborated independently by an MIT
      OpenCourseWare paper; drum family and the galen stick from the Boston
      College ensemble; Tang's canonical table located at Harvard PhD 2000
      p. 165 without needing the restricted book
      Balinese kendang CLOSED at authority A from McGraw's glossary, four
      strokes with notation letters plus the cedugan and gupekan implement
      split; Javanese kendang closed as to structure from Schwartz, Wesleyan,
      which gives head names, drum configurations, historical notation letters
      and the reason the syllabary never standardised, but the syllable table
      itself stayed behind three gates and is marked unverified at source
      Korean janggu RESOLVED BY CORRECTION: gideok is two consecutive
      right-head strokes, not one, and gi is the first of the pair; the five
      Ssang, Pyeon, Go, Yo classes are now recorded
      Brazilian surdo CLOSED at authority A from the UDESC monograph, which
      verifies the hand-mute on the rest figure across all three surdos; two
      further Portuguese academic sources replaced Wikipedia for repique,
      caixa and tamborim
  - the per-instrument stroke set, section 3.1, is now a sixteen-tradition
    matrix. Sabar is the strongest row: a stick-and-hand tradition documented
    by linguists rather than musicians, whose terms are called phonemes because
    they encode Wolof speech, and which still lands on the same bass, edge,
    muted, slap and stopped set as the bare-hand traditions
  - section 3.4 now lists twelve kinds of term that fit NO axis, each attested
    in at least two independent traditions. The second pass added one category
    and sharpened three others
  - the strongest single finding is the tamborim virado. Three sources agree,
    and the ANPPOM paper states the mechanism outright: the note is made by
    bringing the drum to the stick, not the stick to the drum. Every axis
    presupposes that the implement moves and the instrument is static, so this
    is a term that fits no axis because it violates an unstated assumption
    rather than because it needs a new value
  - sabar tan versus tac is the best proof in the bucket that cross-hand
    damping is a distinction traditions name rather than a shading: same
    implement, site, position and rebound, and the only difference is whether
    the other hand damps the edge
  - Korean turned up a new category: a tradition that keeps an abstract
    notation name beside the onomatopoeic one, which is exactly the distinction
    between a pivot term and a sample-library articulation label
  - section 4.6 flags the collision that will silently corrupt data: v0.1
    technique heel, toe and thumb are hi-hat pedal terms, and in every
    tradition here they are hand terms. Identifiers are forever, so this needs
    new slugs plus a documented alias note, not a rename
  - section 5.3 records the positive result: v0.1 technique already contains
    slap, open-tone, bass-tone, mute-stroke, heel, toe, thumb, gliss, scrape
    and shake, which is the recurring set, minted before this bucket looked
    outside Cuba. No tradition needed a primary stroke term outside it except
    snap
  - the question referred here by the vendor-glossary worker is answered in
    section 2.2.1 and summarised in 6.5. Cascara, paila and abanico all have
    text definitions with locators
  - CLAUDE.md rule 2 observed on the sabar monograph: a full-text mirror exists
    at epdf.pub with no stated licence, so it was treated as reference-only,
    not read and not quoted. The archive.org copy is access-restricted and only
    its metadata was used
  - python -m tools.validate, python -m tools.format --check and
    python -m tools.iom.roundtrip_check data/legacy-iom all pass
next:
  - nothing; bucket complete
questions:
  - Three tables are search-derived and could not be confirmed at source, and
    are marked UNVERIFIED-AT-SOURCE where they appear: the Javanese kendhang
    syllable-to-letter mapping in 2.9.2, the janggu five-class table in 2.9.1,
    and the Balinese six-stroke letter set in 2.9.3. In each case a reached
    authority-A source corroborates the structure and only the tabulation is
    unconfirmed. The live locators are in the register: Project MUSE chapter
    2707301 behind a verification gate, the Universitas Mulawarman karawitan
    module returning 503, NamuWiki returning 403, and the National Gugak Center
    score series for the Korean table
  - McGraw's Balinese glossary prints the notation letter (T) for both dug and
    tut. That is either a real collision in Balinese practice or a typo, and
    which one is unresolved
  - Peruvian cajon was never separately closed. The flamenco cajon is covered
    at authority A from the Telethusa research centre, but the Peruvian stroke
    vocabulary it descends from rests on round-A trade summaries only
  - Brazilian minor percussion is still thin: cuica, agogo, ganza, reco-reco,
    chocalho and zabumba rest on Wikipedia alone
  - The most authoritative source still not obtained is unchanged: B. Michael
    Williams, Selected works for solo frame drums, DMA dissertation, University
    of North Texas, ark:/67531/metadc11019. It is open access and blocked only
    by a JavaScript gate. The frame drums are now the thinnest part of the
    bucket, because sabar, kendang, janggu and the Brazilian bateria all gained
    authority-A sources in the second pass and the riq, tar and bendir did not
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
    resposta, polos versus sangsih and lanang versus wadon are functional roles,
    not pitch ordinals, and macho and hembra is a gendered pair with no third
    position at all
  - Whether the axis set should state explicitly that the implement moves and
    the instrument is static. Section 3.4 item 4 shows the tamborim inverts
    this, and the inversion is what produces the note. Either the assumption is
    written down and the tamborim is documented as out of scope, or a term is
    needed for it
