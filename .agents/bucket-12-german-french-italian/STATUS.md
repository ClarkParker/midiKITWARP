status: done
updated: 2026-09-06T13:06:39Z
done:
  - Dossier committed and pushed to docs/research/round2/12-german-french-italian.md,
    ~14700 words, all six sections of the BRIEF output structure filled, no TODOs
  - Round A: 46 candidate sources registered, 25 reached, each with a live locator
  - Round B: German, French, Italian and Spanish extraction with per-term locators
  - Round C: self-critique naming what could not be reached and what it would add
  - DELIVERABLE 1, synonym concordance: instrument names in five languages from the
    MIMO SKOS thesaurus with stable URIs; a four-language concordance from Facchin's
    own Indice degli strumenti; the full French General MIDI percussion map; and a
    mechanical cross-check via Wikipedia cross-language links
  - DELIVERABLE 2, techniques only the non-English tradition names: 40+ terms in
    section 3.2, grouped into six classes, each class being an axis KITWARP lacks -
    note-sequence properties (Handsatz, sticking), grip and stroke form (presa,
    colpo a pistone, Full/Tap, Gabelgriff), damping mechanism (Pedal- vs
    Schlaegeldaempfung), beater structure (Kopf/Bezug/Stiel/Form as four parameters),
    roll internals (five named German rolls, eight Italian), and events spanning two
    slots (Uebergangswirbel, Kreuzschlag, Abschlag)
  - The two catalogues the bucket named are both settled. VSL instrumentology reached
    in DE and EN editions that gloss each other line by line - ten instrument pages
    mined - and it is the best source in the bucket. IRCAM is two separate facts:
    instruments.ircam.fr is egress-denied here, and the reachable host brahms.ircam.fr
    has NO percussion modes-de-jeu pages at all (its SPA returns 200 for any URL, so
    only fetching content proves it), while OrchideaSOL, the SOL successor, has 89
    technique classes and no percussion. Treat it as answered, not as unreached.
  - Pre-MIDI layer reached in both languages after the Wayback route failed, via the
    archive.org search API: Berlioz 1843 and Haupt/Teuchert 1911. Both independently
    name the cymbal chest-damping gesture, 68 years apart, which is the strongest
    evidence in the dossier that excluding choke leaves a real hole.
  - Structural finding: German has precise native words for the whole orchestral
    battery and none for ride, crash, china or splash. A German alias set must be
    built from two registers; the boundary is orchestral battery versus drum kit.
  - Licence position stated per source: what may be quoted, what is registered by
    locator only (Kurt Stone, Gardner Read - copyright, unlicensed mirrors), what is
    rederive-only (MuseScore, GPL)
next:
  - Nothing. Bucket complete.
questions:
  - WebSearch is still refused for this worker at 200/200 after the supervisor
    reported the pool had recovered - both retries came back with the same budget
    message. The supervisor's successful call may have been on a different quota.
    Worth checking before telling other workers the pool is back.
  - Wikipedia's API rate-limits aggressively from this environment (HTTP 429 on the
    third call in a minute). Sleep 0.4s between calls and retry with backoff.
needs_owner:
  - Section 5.2 argues instrument.crash will be ambiguous once the orchestral family
    is minted: every non-English orchestral source reached uses crash for the CLASHED
    PAIR, while KITWARP's crash is the kit's single suspended cymbal. Since ids are
    forever under ADR 0003, the orchestral pair needs its own slug decided before the
    orchestral family is minted, not after. Recommendation: mint a distinct slug for
    the clashed pair now and leave crash as the kit cymbal.
  - The BRIEF's axis sketch lists 'fist' under implement but vocabulary/axes.json does
    not contain it. One of the two is wrong. Recommendation: treat axes.json as
    authoritative and correct the brief.
