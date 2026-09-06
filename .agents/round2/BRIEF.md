# Bucket brief — KITWARP terminology sweep, round 2

## Why this exists

Round 1 searched by project and by device: GitHub repositories, converter source code,
manufacturer note maps. That was the wrong axis. The vocabulary of percussion instruments,
striking positions and playing techniques has existed for decades to centuries and is
documented in orchestration treatises, organological thesauri, rudiment standards,
pedagogical literature, notation standards and vendor glossaries. All of it is on the open
web. Round 1 found secondary aggregations of it; round 2 goes to the primary literature.

Your job is ONE bucket. Fill it exhaustively. A different agent owns each other bucket and
a reconciliation pass will cross-compare all of them at the end, so do not worry about
overlap — worry about depth and about naming your sources precisely.

## Method — three rounds, in this order. Do not skip round A.

**Round A — breadth. Enumerate candidate sources before extracting anything.**
Run at least 12 distinct searches with genuinely different phrasings. Vary:
- vocabulary register: scholarly ("organology", "idiophone", "membranophone",
  "Schlagidiophon"), pedagogical ("stroke types", "rudiments", "sticking"), trade
  ("cymbal zones", "bow edge bell"), notational ("playing technique", "articulation"),
  vendor ("articulation list", "key map", "note map")
- language: English, German, French, Italian, Spanish. German and French percussion
  terminology is often more precise and is used in scores worldwide
  (e.g. "Schlaginstrumente Spieltechniken", "Spielanweisungen Schlagzeug",
  "modes de jeu percussion", "coup de baguette", "colpo di bacchetta",
  "técnicas de percusión")
- source type: books and treatises, standards documents, university course material,
  museum and library thesauri, manufacturer glossaries, professional association standards
- era: pre-MIDI literature matters most, because it names the physical distinctions without
  reference to any note number

Record EVERY candidate in a table: title, author, year, type, locator (URL / ISBN / DOI /
archive.org id), authority level, and whether you could actually reach it. Aim for 25-40
candidates. Reaching only some of them is expected and fine; the list itself is a
deliverable, because it tells the project where to look next.

**Round B — depth. Extract terminology from the sources you can actually reach.**
Exhaustive tables. For every term: the term as the source spells it, what it means
physically, which axis of the KITWARP model it belongs to, and the exact locator (page,
section, glyph name, clause). Verbatim definitions where the source gives one.

**Round C — self-critique.** What is still missing from this bucket? Which named source
could not be reached and what would it add? Name the single most authoritative source you
did NOT get, so the reconciliation pass can decide whether to chase it.

## Access notes for this environment

- curl to github.com and raw.githubusercontent.com is BLOCKED (403). git clone --depth 1
  WORKS for public repositories.
- Load WebFetch and WebSearch via ToolSearch with query "select:WebFetch,WebSearch".
- **web.archive.org is INTERMITTENT, not blocked.** Corrected 2026-09-06 after a worker
  proved it: WebFetch refuses it, and curl fails on most attempts with a mid-tunnel reset,
  but a persistent retry does get through — one worker fetched the same 1,095,305-byte PDF
  twice, byte-identical, on attempts two and three. Retry three to five times before
  concluding a document is unreachable. The availability API
  (`https://archive.org/wayback/available?url=...`) is reliable and answers 200 with JSON
  even while snapshot fetches are failing, so use it to confirm a snapshot exists before
  spending retries on it. An earlier version of this brief called Wayback dead; any source
  registered as unreachable on that basis deserves one more attempt.
- **archive.org itself DOES answer** (HTTP 200). Its details pages, the metadata API
  (https://archive.org/metadata/<id>), full-text search
  (https://archive.org/advancedsearch.php?q=...&output=json) and the plain-text derivatives
  (https://archive.org/stream/<id>/<id>_djvu.txt) all work.
- **WebSearch draws on ONE session-wide budget shared by every worker.** Assume it is
  scarce or already spent. A search that returns nothing is the budget, not your query.
  Plan around WebFetch on URLs you construct directly, `git clone --depth 1` for anything
  on GitHub, and a site's own search endpoint fetched as a URL.
- Many vendor PDF paths return 403. Try, in order: the vendor's own knowledge-base HTML
  page; regional vendor domains; the vendor's separate documentation portal; Google Books;
  IMSLP for older treatises; HathiTrust; university library open pages.
- **The egress policy denies more hosts than github.com.** Confirmed 502 on CONNECT for
  instruments.ircam.fr, lclsds.loc.gov, vocabs.dariah.eu, duckduckgo.com,
  howtowriteforpercussion.com, pearleurope.com, www.drummica.com. A host answering 502 is
  denied, not slow: record it as unreachable with its locator and move on.
- A complete candidate register with live locators for sources you could NOT reach is worth
  as much as the extraction. Never stall retrying a dead host.
- Use python3 for parsing and aggregation. Save large intermediate downloads under
  scratch:buckets/<your bucket>/ and never into the project working directory
  /home/user/midiKITWARP.

## The model your findings feed

A pivot term is a sparse tuple over these axes. Map every term you find onto one of them,
or say plainly that it fits none — a term that fits no axis is the most valuable thing you
can find, because it means an axis is missing.

  instrument   what makes the sound
  site         contact site ON THE INSTRUMENT: head, rim, rim2, crossstick, shell,
               bow, edge, bell, underside
  position     where on that site, radially: centre, halfway, offset, perimeter
  contact      part of the IMPLEMENT that touches: tip, shank, butt
  technique    the stroke: hit, rimshot, rim-only, sidestick, stick-shot, back-stick,
               ping-shot, gok-shot, slap, open-tone, bass-tone, mute-stroke, heel, toe,
               thumb, sweep, swirl, circling, scrape, shake, gliss, dead, chick, foot-splash
  ornament     grace or multi-stroke qualifier, with an attack count: flam, drag, ruff,
               bounced, roll, buzz, crescendo, swell, wash
  openness     ordered scalar 0.0 closed .. 1.0 open, named anchors tight, closed,
               closed-loose, quarter, half, three-quarter, loose, open
  damping      none, muted, damped, towel, gated
  mechanism    wires-on, wires-off, kick-damped, kick-half-open
  implement    stick, jazz-stick, brush, rod, mallet-soft/medium/hard, hand, finger,
               fist, fingernail, felt/wood/plastic/rubber beater, superball
  dynamic      normal, ghost, soft, hard, accent
  timbre       acoustic, electronic, analog-808/909/707/606/cr78, fm, pcm, physical,
               chip, noise
  voicing      standard, room, power, jazz, orchestra, lo-fi, dark

Carried on a layout slot rather than on the term: instance (1-based ordinal; toms high to
low in pitch, cymbals left to right from the player's seat) and limb.

Current vocabulary v0.1 has 155 terms covering the drum kit only: kick 10, snare 32,
tom 14, hihat 38, ride 13, crash 7, china 4, stack 4, cowbell 4, tambourine 4, triangle 3,
plus singles for octoban, xhat, mini-hihat, mini-china, splash, bell, shaker, sizzle-ride,
crash-ride, cymbal, jam-block, woodblock, sticks, clap, chimes, aux-pad. Percussion,
orchestral, electronic and utility families are reserved and unminted. Round 2 exists to
find what that list is missing and what it names wrongly.

## Output

Write your bucket file to the path given in your task. Structure it exactly as:

  1. Candidate source register (round A) — the full table, reached or not
  2. Extracted terminology (round B) — exhaustive tables with locators
  3. Axis mapping — every term mapped to an axis, with a separate section for terms that
     fit NO axis
  4. Conflicts and false friends — one word meaning different things in different
     traditions, and different words meaning the same thing
  5. Gaps against vocabulary v0.1 — what is missing, what is misnamed
  6. Self-critique (round C) — what you could not reach and what it would have added

Facts over prose. Every claim carries a locator. Mark anything uncertain UNVERIFIED.
Never present a guess as a finding.
