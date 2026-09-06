status: done
updated: 2026-09-06T13:18:10Z
done:
  - Dossier at docs/research/round2/03-organology-thesauri.md, 1280 lines,
    committed and pushed. Structure as the brief requires, plus section 0 that
    answers the bucket question directly with cost and benefit.
  - ANSWER TO THE BUCKET QUESTION. Yes for the instrument axis and only for its
    coarse half; no for every other axis. Six maintained authority files with
    stable dereferenceable ids exist and all six were reached and queried live:
    MIMO 2724 concepts, LCMPT 942, Getty AAT 348 plus 177, Wikidata 877 in the
    percussion subtree, MusicBrainz 288, GND 908. Best coverage of KITWARP's 27
    instrument values is Wikidata at 17. None of the six has ride, china,
    splash, stack, xhat, mini-china, mini-hihat, crash-ride, jam-block or
    aux-pad; AAT, LCMPT and MusicBrainz have no hi-hat at all. Across KITWARP's
    other eleven axes the total harvest from all six files is nine concepts.
  - RECOMMENDATION. Do not adopt a foreign namespace. Add an optional outbound
    xref block, namespaces mimo lcmpt aat wikidata mb gnd, ids only. Record
    Hornbostel-Sachs notations only as a version-pinned reference axis.
  - LICENCE QUESTION ANSWERED and written into the dossier as section 0.5, with
    the reasoning rather than as an assurance: a number is not a work under
    UrhG 2(2), an outbound id transfers no contents so it is neither extraction
    nor re-utilisation, and 40 of 2724 is about 1.5 percent. The three
    conditions are recorded as part of the recommendation, not as a caveat:
    ids only never labels, MIMO in data/sources.json with licence_applied
    none-stated, ids counted against the extraction budget.
  - SITE-VOCABULARY QUESTION CLOSED with a sourced negative, section 2.12 and
    2.13. CIMCIM built a brasswind terminology thesaurus by close inspection of
    instruments, the exact method that would produce a striking-site vocabulary,
    and never built the percussion counterpart. The Horniman catalogue was
    opened directly and verified here: its Hornbostel-Sachs numbers sit in a
    structured term layer with stable ids, but shell, hoop, head and membrane
    appear only in free prose, and its one structured component field carries
    materials. The catalogue layer is a corpus of part terms, not a vocabulary
    of them. Confidence that no percussion parts thesaurus exists is now high.
  - Supervisor's searches 1 to 4 folded in with locators; museumsvokabular and
    term.museum-digital recorded as confirmed live but not extracted; Kartomi
    recorded with her 17 systems and with the academia.edu excerpt marked
    reference-only and not quotable under ADR-0004.
next:
  - Nothing required. Bucket complete.
questions:
  - Search 5, Grove 2014 Classification article, is still worth running if the
    supervisor has budget, but it is not blocking: it would tell us whether the
    scholarship has drum-kit terms even though the thesauri do not. It is named
    in section 6.2 as the single most authoritative source not obtained.
needs_owner:
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
