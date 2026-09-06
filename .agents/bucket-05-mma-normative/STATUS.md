status: done
updated: 2026-09-06T14:05:00Z
done:
  - Dossier written to docs/research/round2/05-mma-normative.md (1227 lines), committed
    and pushed. Structure follows BRIEF.md: source register, terminology, axis mapping,
    conflicts, gaps against v0.1, self-critique, plus provenance.
  - ACCESS: dossier 03 says the GM1/GM2 specs are paywalled. They are not. AMEI, the
    Japanese body that co-issues every MMA Recommended Practice, publishes the ENGLISH
    RP PDFs free at amei.or.jp/midistandardcommittee/RP&CAj.html. Every normative
    document this bucket needed was obtained without payment or registration.
  - Normative documents quoted: GM1 (RP-003 Table 3, via the Complete MIDI 1.0 Detailed
    Specification), GM2 RP-024 v1.2a Appendix B, GM Lite RP-033, RP-048, DLS 1 and 2,
    SP-MIDI, MPE RP-053, MIDI 2.0 UMP M2-104-UM, the MIDI-CI Default Drum Note Map
    Profile M2-125-UM v1.0 (2025), the MIDINameDocument DTD, the MMA SysEx ID table,
    Roland's own SC-8850/SC-88Pro manuals, Yamaha's own MU100 and PLG100-XG data lists.
  - ERRORS FOUND IN docs/research/03-midi-standards.md:
      GM1 - 6 of 47 names are GM2 strings mislabelled as GM1 (42,44,46,48,58,60)
      GM2 - note map and all 9 program numbers CORRECT; missing the normative PAN
            column (62 values) and the [EXC1]-[EXC7] mutual-exclusion groups
      GS  - 6 outright name errors (Belltree, Waves, CM Open High Hat 1/2, Screaming,
            Windchimes, Tekno Trip) plus a systematic ordinal-spacing error; all 24
            drum-set Program Change numbers were missing and are now supplied; the
            note range is 0-127, not 25-108
      XG  - 10 of the Standard Kit names are not Yamaha's names at all; the kit-variant
            diffs are worse; the XG Level 1 kit list omits the Dance Kit and calls the
            Symphony Kit "Classic Kit"
      The "10 hi-hat openness steps" claim is an overread: Roland's suffixes index the
      kit, not the degree of opening. The corpus supports four states, not eight.
      Dossier 03's claim that no standard has a "role" axis is falsified by
      M2-125-UM 4.1 (2025), which defines role and refuses to define timbre.
      Two of dossier 03's open questions (Applause at note 88; whether the MIDI-CI
      drum profile extends the GM vocabulary) are answered.
  - REFERRED QUESTIONS from the vendor-glossary worker: answered in dossier section 5A.
    Short form: "ride area"/"crash area" appear nowhere - Roland uses Inner/Edge, Yamaha
    uses Ride Cymbal Cup, the MMA uses Ride Bell only; mini-china and mini-hihat appear
    in no standard and no Roland/Yamaha document; ping-shot, gok-shot and stick-shot
    return zero hits across the whole corpus; felt, pillow, Moongel, muffle and control
    ring return zero hits - the standards name damping outcomes, never dampers, which
    is why v0.1's damping value "towel" is mis-factored. Questions 1, 3 and 4 also ask
    which LIBRARY coined a term, and no library material is in this bucket, so I settled
    the negative half only and said so.
  - ENVIRONMENT, verified: web.archive.org returns 403 "Blocked by egress policy" on
    both the CDX API and snapshot URLs (a bare HEAD returns a bodyless 302 from the
    proxy, which is easy to misread as working). archive.org itself answers 200 and
    advancedsearch.php returns valid JSON - that is the surviving archive route.
    WebSearch budget was exhausted session-wide at my 16th search.
next:
  - nothing; bucket complete
questions:
  - Does XG Level 1 formally mandate the twelve kits the PLG100-XG ships, or is that
    a product decision? Needs the Yamaha XG Format Specification, which I could not
    find in public form. Same question for Roland and the GS Format Specification.
  - Roland's "Ride Cymbal Low/Mid/High Inner/Edge": is Low/Mid/High pitch, size or
    dynamic? Roland's manuals do not say.
needs_owner:
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
