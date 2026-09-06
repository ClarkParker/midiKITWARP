status: done
updated: 2026-09-06T12:53:16Z
done:
  - Dossier written, validated and pushed at docs/research/round2/11-acoustics-and-timbre.md
  - Round A: 16 WebSearch sweeps across scholarly, pedagogical, trade, notational and
    vendor registers in English, German and French, then 13 Crossref and 3 DBLP queries
    once the session WebSearch budget ran out; 52-row candidate register, 12 reached in
    full and 10 in part
  - Round B: full text extracted from Tindale et al. ISMIR 2004, Prockup et al. ISMIR
    2013, Sekiguchi and Samejima AST 2023, Rossing AST 2001, Sokolovskis and McPherson
    NIME 2014, Harrison and Hill IoA 2013, Wu et al. TASLP 2018, Patranabis et al.
    arXiv 2015, Madsen UIUC 2016, Miller 1956, Rossing ASA Explore Sound 2018 and the
    Freed 1990 JASA abstract
  - DECISION 1, openness anchors. Eight is too many. Absolute identification of a single
    auditory continuum tops out at 2.3 bits or about five categories for loudness and
    2.5 bits or about six for pitch, mean 2.6 bits or 6.5 categories over all continua
    Miller measured (Miller 1956 pp. 85-86). Separately, openness is not one physical
    quantity - Sekiguchi and Samejima 2023 sec. 4.3 shows d < 0 pressed, d = 0 touching
    and d > 0 gap are three regimes, the pressed one so different that their model
    diverges on it - and the model omits the tilting motion that makes half-open sound
    the way it does. The current scalars are also mis-spaced: closed, closed-loose and
    quarter crowd into 0.12 to 0.25 while 0.25 to 0.50 is unnamed. Recommendation is
    five anchors, with the demoted slugs kept as correction aliases per ADR-0003.
  - DECISION 2, radial strike position. Three steps, not five. Tindale et al. 2004 is the
    only study that varied the count: centre/halfway/edge scores 85 to 99 per cent with
    every classifier and every feature set, five positions cost 5 to 30 points, and the
    paper says the misclassifications go to the next nearest timbre - the extra anchors
    bleed into their neighbours rather than forming clusters. Prockup et al. 2013, Souza
    et al. 2015 and tabla nomenclature all independently chose three. The best optical
    measurement rig achieves 18 mm mean and 54 mm maximum error on a snare with error
    rising toward the rim, so a capture rig cannot reliably label a near-edge band.
    On cymbals radial position is a smooth monotone continuum with no anchors at all,
    so the named cymbal distinctions belong to the site axis, not the position axis.
  - Both decisions are bounded by the evidence, not determined by it: no perceptual study
    of hi-hat openness or of radial strike position on a membrane exists. That negative
    result is recorded in section 6.5 of the dossier.
  - Marketing verdict the bucket owed: voicing (standard, room, power, jazz, orchestra,
    lo-fi, dark) has no acoustic basis anywhere in the register - it names production
    choices. timbre (acoustic, 808, fm, pcm) is a real engineering category but not a
    physical excitation property. Every other axis is physically real, with site the
    best-evidenced of all.
  - Six terms found that fit no axis, each implying a gap: otsu post-strike tension
    modulation, the syahi/maidan/chanti material zones of a loaded head, a simultaneous
    second contact, the strike-sound/build-up/aftersound temporal decomposition, the
    chaotic regime that couples dynamic to timbre on plates, and hi-hat tilt.
next:
questions:
  - Session-wide WebSearch budget was exhausted at 200/200 partway through round A.
    Crossref, DBLP, archive.org and WebFetch still work and covered the remainder.
  - Does the project want the timpani beating radius resolved? The two conventions in
    circulation, a quarter of the distance edge-to-centre and a quarter of the diameter
    in from the rim, name different radii, and both are called the normal beating spot.
    Rossing 1992 in Physics Today would settle it.
needs_owner:
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
