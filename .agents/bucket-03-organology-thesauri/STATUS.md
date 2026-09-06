status: done
updated: 2026-09-06T13:10:49Z
done:
  - Dossier written, committed and pushed at
    docs/research/round2/03-organology-thesauri.md, 1173 lines, structured as the
    brief requires: candidate register, extracted terminology, axis mapping with
    a separate no-axis section, conflicts and false friends, gaps against v0.1,
    self-critique, plus a section 0 that answers the bucket question directly
  - ANSWER TO THE BUCKET QUESTION. Yes for the instrument axis and only for its
    coarse half; no for every other axis. Six maintained authority files with
    stable dereferenceable ids exist and all six were reached and queried live,
    MIMO 2724 concepts, LCMPT 942, Getty AAT 348 plus 177, Wikidata 877 in the
    percussion subtree, MusicBrainz 288, GND 908. Best coverage of KITWARP's 27
    instrument values is Wikidata at 17. Not one of the six has a concept for
    ride, china, splash, stack, xhat, mini-china, mini-hihat, crash-ride,
    jam-block or aux-pad. AAT, LCMPT and MusicBrainz have no hi-hat at all.
    Across KITWARP's other eleven axes the total harvest from all six files is
    nine concepts, and there is no site, technique, openness, damping, ornament,
    position, contact, dynamic or voicing vocabulary anywhere.
  - RECOMMENDATION. Do not adopt a foreign namespace, it would force minting
    children under borrowed parents. Do add an optional outbound xref block,
    namespaces mimo lcmpt aat wikidata mb gnd, ids only and never label text.
    Do record Hornbostel-Sachs notations as a reference axis only, and pinned to
    a scheme version, because HS-15 means Metal sheets in MIMO and
    Stampf-Idiophon in the ACDH-CH implementation.
  - Cost and benefit are quantified in section 0.2 and 0.3. Cost is about 40
    xref-eligible terms of which 13 fill today, one schema field, one validator
    rule, plus the MIMO licence gap. Benefit is 13-language display names, an
    external anchor for ADR-0003, provenance for the unminted long tail, and a
    disambiguation test.
  - Round A recorded 36 candidates with locators, reached or not, and the five
    hosts that answered an error with their symptoms
  - Primary texts read: Hornbostel and Sachs 1914 German introduction, the MIMO
    2011 revision, its October 2017 Addenda and Corrigenda, the Knight Revision
  - Every page and count claim was re-verified against the source before commit;
    six wrong page numbers and two wrong counts were found and corrected
next:
  - Nothing. Bucket complete. Reconciliation should look at section 5.3, which
    argues sizzle-ride is a mechanism not an instrument, and at section 4.8, the
    collision between site bow and a future implement bow for bowed cymbals.
questions:
  - LICENCE. The MIMO thesaurus publishes no licence statement anywhere
    reachable, not in the Skosmos metadata, not on the concept scheme, not on
    the landing page. Is storing only a MIMO integer id, with no MIMO label
    copied, inside or outside the licence question under ADR-0004? The other
    five authorities are clean, AAT is ODC-By 1.0, LCMPT is public domain,
    Wikidata MusicBrainz and GND are CC0.
  - SEARCHES I COULD NOT RUN, worker WebSearch quota exhausted at 200 of 200.
    Please run these and send results, in priority order.
    1. CIMCIM "brasswind terminology" thesaurus - does a percussion equivalent
       exist? This is the last plausible home of a striking-site vocabulary.
    2. "Horniman Museum" OR "Musical Instrument Museum Brussels" collection
       catalogue drum parts terminology head shell rim hoop counterhoop
    3. museumsvokabular.de OR term.museum-digital.de Schlaginstrument
       Bestandteile Vokabular - a second German label set to check MIMO's
       Hi-hat defect against
    4. Kartomi 1990 "On Concepts and Classifications of Musical Instruments" -
       any open full text, does any of her 17 systems use playing technique as
       a primary axis?
    5. Grove Dictionary of Musical Instruments 2014 "Classification" v.1
       p.568-79 - any open preprint or mirror; this is the single most
       authoritative source not obtained, oxfordmusiconline returns 403
needs_owner: []
