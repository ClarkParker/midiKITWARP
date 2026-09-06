status: running
updated: 2026-09-06T13:35:00Z
done:
  - Round A complete: 3 WebSearch queries plus 28 catalogue queries (archive.org
    advancedsearch, openlibrary, HathiTrust catalogue API, direct URL probes)
  - 22 public-domain or openly posted full texts located; 16 downloaded as text
  - Round B extraction under way and verified against page images:
    * Gardner Read, Thesaurus of Orchestral Devices (1953), Part IV Percussion,
      chapters 32-38, printed pp. 158-233 - four-language (EN/IT/FR/DE) technique
      and beater tables, extracted page by page
    * Berlioz/Strauss, Instrumentationslehre vol. 2 (1905) - timpani stick taxonomy
      p. 406, muffling p. 411, snare slackening p. 423
    * Forsyth, Orchestration (1914) - batter-head/snare-head, two-plate-stroke,
      two-stick-roll, tambourine thumb method
    * Gevaert, Nouveau traité d'instrumentation (1885) - ta / fla / tra / ra /
      roulement continu, tambours voilés, printed pp. 331-332
    * Solomon, How to Write for Percussion 2/e (2016) - publisher preview PDF,
      32 pp., full table of contents with page numbers incl. Appendix C
      Extended Techniques pp. 239-250
next:
  - Write docs/research/round2/02-orchestral-treatises.md, sections 1-6
questions:
  - WebSearch budget for this session is exhausted (200/200) and it is shared across
    all workers; duckduckgo, mojeek and searx return captcha/403 to both curl and
    WebFetch; HathiTrust is behind Cloudflare (403); the Google Books API returns
    HTTP 429 for the whole proxy project on every attempt. archive.org
    advancedsearch.php and openlibrary.org/search.json do work and were used
    instead. Should later rounds raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION?
  - archive.org "search inside" (fulltext/inside.php) now returns "Item not
    available" for lending-restricted items, so Blades, Adler, Stone, Peinkofer,
    Brindle and Read's later Compendium cannot be quoted at all from this
    environment. Is there an account with archive.org lending access, or a library
    proxy, that a later pass could use?
needs_owner:
