status: done
updated: 2026-09-06T14:32:00Z
done:
  - Dossier committed and pushed: docs/research/round2/02-orchestral-treatises.md
    (1160 lines, sections 1-6 exactly as BRIEF.md specifies)
  - Round A: 42 distinct queries (3 WebSearch before the pool closed, 39 through
    archive.org advancedsearch / openlibrary / HathiTrust catalogue API / direct
    URL probes). Register holds 45 candidates: 30 reached, 28 of them in full text,
    15 named-and-not-reached with a live locator each.
  - Round B: verbatim extraction with printed page numbers from
    * Gardner Read, Thesaurus of Orchestral Devices (1953) - NOT lending-restricted.
      Part IV Percussion ch. 32-38, pp. 158-233: four-language (EN/IT/FR/DE) technique
      tables, a 61-name beater list at pp. 166-167, the percussion terminology glossary
      at pp. 232-233, and the orchestral instrument nomenclature at pp. 8-9
    * Berlioz/Strauss, Instrumentationslehre vol. 2 (1905): three-grade timpani stick
      taxonomy p. 406, cloth muffling p. 411, snare slackening p. 423, cymbal choke p. 422
    * Forsyth, Orchestration (1914): batter-head/snare-head p. 24, two-plate-stroke p. 35,
      two-plate-roll and two-stick-roll p. 36, tambourine thumb method p. 32
    * Widor, Technique of the Modern Orchestra (1906): stick kinds p. 100, sans timbre
      p. 108, tambourine three ways pp. 108-109
    * Gevaert, Nouveau traite d'instrumentation (1885): ta / fla / tra / ra de 3-7 coups /
      roulement continu pp. 331-332, three muffling procedures p. 332
    * Gardner, The Military Drummer (1918): counted stroke-roll series pp. 20-23
    * Straight, Modern Syncopated Rhythms for Drums (1922): tip-to-butt on the kick rim
      (Lesson 53) and "Jazz sticks" (Lesson 41)
    * Solomon, How to Write for Percussion 2/e (2016): full ToC with page numbers from the
      publisher's own preview PDF, incl. Appendix C Extended Techniques pp. 239-250
  - Round C: 20 findings that fit NO current axis are listed separately (section 3.9);
    section 5 names 11 missing implement values, the wires-slack mechanism state, the
    pair-versus-suspended cymbal gap, and seven places where v0.1 names something wrongly
  - Access findings tested rather than assumed and written into section 1.0: archive.org
    search-inside answers with page-located JSON for unrestricted items and refuses
    restricted ones with HTTP 403; /stream/ returns the reader shell, not text;
    /download/ returns HTTP 401; ia-fts.archive.org, vsl.co.at and
    howtowriteforpercussion.com are 502 by egress policy; imslp.org search API returns
    empty for every query
next:
  - nothing outstanding in this bucket; the three follow-ups are in questions below
questions:
  - Please run these three searches for me - WebSearch still refuses from inside this
    worker with "200 of 200" even after the pool recovered:
    (1) `"rim shot" drum method 1930s "Gene Krupa" OR "Ray Bauduc" OR "Ben Duncan"
        site:archive.org` - the earliest printing of "rim shot" is the one loose end in
        section 6.1. Gardner 1918, Bower 1912 and Straight 1922 all lack the term, and
        Read 1953 records that Italian, French and German had no equivalent at all.
    (2) `Kastner "Methode complete et raisonnee" tambour OR timbales 1845 full text` -
        this is candidate N15, the primary source for the French stroke names ta / fla /
        tra / ra that Gevaert only cites second-hand. Gallica returns 403 here.
    (3) `Peinkofer Tannigel "Handbook of Percussion Instruments" contents OR index
        "playing techniques"` - candidate N5, the one book whose subtitle is literally
        the KITWARP model. Even a table of contents with page numbers would be worth
        having; the archive.org copy is lending-restricted and unquotable.
  - Should `docs/research/README.md` get a round-2 section, or does the reconciliation
    pass own that index? I have not touched it, since twelve workers editing one table
    would conflict on every push.
needs_owner:
  - Elaine Gould, Behind Bars (2011) is openly posted at archive.org
    `behind-bars-by-elaine-gould` with no stated licence, and it has a substantial
    percussion chapter. I registered it with its locator and deliberately did not quote
    from it, per CLAUDE.md rule 2 and the supervisor's instruction on unauthorised
    mirrors. If the owner has a bought copy, that chapter is worth a pass by someone who
    may quote it - and it would also settle whether it belongs to this bucket or to the
    notation-standards one.
