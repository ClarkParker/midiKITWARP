status: done
updated: 2026-09-06T15:18:00Z
done:
  - Dossier committed and pushed: docs/research/round2/02-orchestral-treatises.md
    (1262 lines, sections 1-6 exactly as BRIEF.md specifies)
  - Round A: 48 distinct queries. Register holds 51 candidates: 34 reached, 32 of them
    in full text, 17 named-and-not-reached with a live locator each.
  - Round B: verbatim extraction with printed page numbers from Read 1953 (Thesaurus of
    Orchestral Devices, NOT lending-restricted - four-language technique tables, 61-name
    beater list pp. 166-167, terminology glossary pp. 232-233, instrument nomenclature
    pp. 8-9), Berlioz/Strauss 1905, Forsyth 1914, Widor 1906, Gevaert 1885, Gardner 1918,
    Straight 1922, Bauduc 1937 (described, not quoted - no stated licence), Solomon 2016
    (publisher preview ToC).
  - Round C: 21 findings that fit NO current axis (section 3.9); section 5 names the
    missing implement values, the wires-slack mechanism state, the press-roll ornament,
    the pair-versus-suspended cymbal gap, and seven places where v0.1 names something
    wrongly.
  - ALL THREE supervisor searches acted on:
    * Search 1, rim shot. Ray Bauduc, Dixieland Drumming (1937) IS on archive.org
      unrestricted as `RayBauducDixielandDrumming`. It uses "rim shot" twice, without
      definition, as an established word - in Press Roll No. 3 and in a later snare
      exercise - and already as a dynamic-accent device, not a timbre. Combined with its
      absence from Bower 1912, Gardner 1918 and Straight 1922, that brackets the term's
      entry into print at 1922-1937 and closes the open question in section 4 and 6.1.
      Krupa's Drum Method 1938 is NOT on archive.org (Q44); the physical definition
      attributed to him (shaft of the stick between head and rim) stays UNVERIFIED,
      marked as such. Bauduc also yields: bass drum counter hoop struck with stick tips,
      six numbered press rolls, "sock cymbal pedal", a three-way Chinese/large
      Turkish/small Turkish cymbal distinction, four brush patterns.
    * Search 2, Kastner. The BnF ark btv1b10075080v is real - but Gallica returns HTTP
      200 with an identical 50 212-byte "Verification de securite" interstitial for every
      path including .texteBrut, so it is closed, not open. The PAS article is behind a
      member login; only its blurb is visible. Google Books id kdTS3H5ZVBwC recorded.
      Registered as N15 with all three locators. Emile Tavan's Methode pratique
      d'orchestration symphonique on fr.wikisource WAS reachable and read: notation,
      ranges and orchestral usage only, no beater, position, stroke or muffling terms.
      Registered as S20b, low yield.
    * Search 3, Peinkofer and Tannigel. Confirmed contents entered in full at N5 and the
      book PROMOTED to first place in section 6.2, ahead of Read's Compendium: it pairs
      beaters per instrument with playing techniques per instrument and ends in a
      four-language EN/DE/IT/FR dictionary, which is Read's ch. 38 at book length. One
      consequence worth the reconciliation pass's attention: the English translation is
      by Kurt and Else Stone, so candidates N4 (Stone) and N5 (Peinkofer/Tannigel) are
      ONE lineage and their agreement is not corroboration. Also added from the West
      Liberty reading list: Sam Denov, The Art of Playing Cymbals (1963) as N16 - a
      book-length treatment of the family where v0.1 is weakest - and Blades & Montagu
      as N17.
  - Both headline findings PROMOTED to a new section 0.1 at the head of the dossier, as
    instructed: (a) Read's own 1953 section headings - Dampened, Methods of Striking,
    Muffled, Stick Types, Without snares, Other Effects, contents pp. XVI-XVII, body
    pp. 158-233 - are the axis decomposition arrived at forty years before General MIDI;
    (b) `timbre` in French and Italian scores means the SNARE WIRES, so an importer
    resolving it on the `timbre` axis destroys a `mechanism` value. Flagged as needing a
    note in rules.json rather than a table row.
  - docs/research/README.md deliberately untouched: the reconciliation pass owns it.
  - python -m tools.validate and python -m tools.format --check both pass.
next:
  - nothing outstanding in this bucket
questions:
  - Two loose ends, both cheap, neither blocking. (1) Is Gene Krupa's Drum Method (1938)
    anywhere with a readable page? It is the only candidate for a PHYSICAL definition of
    the rim shot - shaft of the stick between head and rim - and that definition would
    let `technique: rimshot` be minted with `contact: shank` from a source rather than
    from a device manual. (2) `ride` is still untraced: Read p. 212 records `"Ride" solo`
    in 1953 with no translation, and Bauduc 1937 does not use the word at all.
needs_owner:
  - Two books would each close a large part of this bucket and both are in print or
    cheaply available second-hand, so this is a purchase decision rather than a research
    one. Recommendation: Peinkofer & Tannigel, Handbook of Percussion Instruments
    (Schott, EN tr. Stone 1976) FIRST - its four-language dictionary plus per-instrument
    beater and technique lists is the single closest published artefact to the KITWARP
    model. Gardner Read, Compendium of Modern Instrumental Techniques (Greenwood 1993)
    second. Both are lending-restricted on archive.org and unquotable from here.
  - Elaine Gould, Behind Bars (2011) is openly posted at archive.org
    `behind-bars-by-elaine-gould` with no stated licence, and has a substantial percussion
    chapter. Registered with its locator and deliberately not quoted, per CLAUDE.md rule 2.
    Same treatment applied to Bauduc 1937. If the owner has bought copies, both are worth
    a pass by someone who may quote them.
