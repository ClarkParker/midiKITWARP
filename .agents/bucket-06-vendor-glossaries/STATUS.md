# bucket-06-vendor-glossaries

status: done
updated: 2026-09-06T12:52:00Z
done:
  - Round A breadth sweep: 20 distinct searches before any extraction, varying
    register (trade, pedagogical, retail, manufacturing), language (EN, DE, FR)
    and source type (vendor education, vendor FAQ, artist-relations material,
    retailer buying guide, trade press, vintage catalogue archive).
  - Candidate source register: 58 sources with locators and authority levels,
    26 of them actually reached. Every unreached row carries a live locator.
  - Round B extraction with verbatim definitions and per-row locators from
    Zildjian (FAQ cymbal anatomy, Marching Cymbals 101), Sabian (Guide to
    Cymbal Terminology - 30 defined terms, Cymbals 101, The Fine Art of
    Lathing), Paiste (Cymbal Anatomy, Sound Classification System, Usage and
    Care), Meinl Cymbals Wiki (types, effects, alloys, finishes), Remo,
    Evans/D'Addario, ProMark, Vic Firth (Percussion 101 crash cymbals and
    tambourine), Yamaha (snare and marching snare anatomy, hardware) and the
    Thomann Online Expert guides in English and German.
  - Axis mapping for every extracted term, plus five groups of terms that fit
    NO axis.
  - Conflicts and false friends, gaps against v0.1, and round C self-critique.
  - Dossier committed and pushed: docs/research/round2/06-vendor-glossaries.md
  - python -m tools.validate and python -m tools.format --check both pass.
next:
  - Nothing. Bucket complete. Handing the open items below to reconciliation.
questions:
  - Zildjian publishes its cymbal playing zones as "ride area" and "crash area"
    and uses "bow" only as a synonym for profile; Paiste uses "surface" for the
    zone and "bow" for the curvature. Only Meinl uses the bow/edge/bell triple
    the libraries ship. Does any library articulation list actually use
    "ride area"/"crash area"? Bucket 05 can answer from its articulation dumps.
  - The v0.1 ornament axis is defined as a grace or multi-stroke qualifier with
    an attack count, but "wash" carries no attack count and every vendor
    (Sabian, Thomann) defines it as a sustain property. Should wash move off
    ornament? A notation-standards bucket can say where wash lives there.
  - v0.1 mints mini-china and mini-hihat. No reached vendor source names either.
    Are they library-only coinages? Bucket 05 can confirm.
  - No vendor source reached uses "ping-shot", "gok-shot" or "stick-shot". These
    look like library words rather than trade words. Which library introduced
    each? Bucket 05 owns this.
  - Trade names for dampers (felt strip, pillow, Moongel, control ring, head
    overlay) are absent from the damping axis while "towel" is present. Which of
    these do libraries actually ship as separate articulations?
  - Timbale terms cascara, paila and abanico are recorded UNVERIFIED: LP
    publishes technique only as video and no primary text was reachable. A
    percussion-pedagogy bucket may already hold a citable source.
needs_owner:
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
