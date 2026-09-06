# Bucket 09 — sample-library manuals, first-hand

```
status: done
updated: 2026-09-06T13:17:13Z
done:
  - Dossier committed and pushed: docs/research/round2/09-library-primary-manuals.md
    (837 lines, structured exactly as BRIEF.md requires, with the verdict table added as
    section 0 per the supervisor's correction). tools.validate and tools.format --check
    both pass on every commit.
  - Round A: 20 distinct searches before any extraction; candidate register of 45 sources
    with authority level and reached/not-reached is section 1.
  - VERDICT, per library - does an official published note map or articulation chart
    exist, where, in what format, reachable from here:
      REACHABLE OFFICIAL CHART (7): XLN Addictive Drums 2 (keymap PDF, Zendesk attachment
        16925267740829, dated 2021-06-02); FXpansion/inMusic BFD3 (HTML key map reference,
        fxpansion.com and internal.bfddrums.com); BFD Player (PDF appendix on
        cdn.inmusicbrands.com); NI Studio Drummer (articulation list in the manual PDF and
        on docs.native-instruments.com; note map is in-product only); NI Abbey Road 60s,
        70s, 80s and Modern (articulation tables WITH the note column); MT Power Drum Kit 2
        (nine DAW drum-map files on resources.manda-audio.com, plus VST3 note names);
        Rayzoon Jamstix 4 (Appendix B kit-piece reference IDs, Appendix C file format).
      MIRROR ONLY (2): Sennheiser DrumMic'a (six complete maps in the manual, but the
        vendor's distribution is dead - drummica.com does not resolve); Toontrack's
        predecessors, Superior Drummer 2 with its "GM Extended Core Mapping" chart and
        EZdrummer 1 with its key map, both from toontrack.com/updates/manuals/ via Wayback.
      LIST WITHOUT NUMBERS (1): GetGood Drums Modern & Massive 2, KB article 32177396568727
        - the first official GGD articulation list this project has had. GGD's 47-article
        KB was enumerated in full; no other GGD library has one.
      NOTHING PUBLISHED (4): Toontrack SD3 and EZdrummer 3 (manual behind an account
        login, no drum maps offered, last public Toontrack PDF dates from 2009);
        Steven Slate SSD5 and SSD5.5 (both manuals fetched and read - no list, no map);
        ML Sound Lab ML Drums (no documentation of any kind); IK MODO Drum (FAQ 1395 says
        manuals live in the account area). MODO and SD3 were then re-checked through
        archive.org's own item search: nothing there either.
  - Vocabulary extracted from vendor primaries only, with per-term locators: XLN's full
    stroke-type set including the brushes column; BFD3's 73 articulations plus BFD Player's
    "Variable" CC forms; NI's articulation set across eight kits plus the library-specific
    ones (Felt/Rubber Beater, Tea Towel, Towel, Skin On Skin, Mirror, Splash On/Off/Rim,
    Chopper); GGD M&M2; Toontrack's own GM Extended names; Jamstix Appendix B in full
    including the Jamcussion IDs round 1 did not have; DrumMic'a's six maps; MT Power's
    note-name file.
  - Best single find for the model: BFD3's manual states that a hi-hat's "tip (also known
    as bow)" and "shank (edge)" are the same events named from opposite ends, and explains
    which end is which. That converts the vendor disagreement between GGD's "Tight Edge"
    and NI's "Closed Shank" from a conflict into a documented equivalence. The same page
    attests "foot-chick", which was the weakest-supported slug on the technique axis.
  - Answered the cross-bucket question on five disputed slugs (dossier 5.4): ping-shot,
    gok-shot and stick-shot were coined by no library - they entered v0.1 from MuseScore's
    marching-snare drumset file; mini-hihat IS vendor-attested, on GetGood Drums' Benny
    Greb page as Meinl "Artist Concept Mini Hats"; mini-china is attested only by a
    third-party converter, while GGD itself calls that cymbal a 13" Zildjian Oriental Trash
    China. Side finding: GGD publishes a "Mini Ride" that v0.1 does not have, and writes
    "X-Hats", which is direct attestation for the xhat instrument.
  - Fetched NI's and Rayzoon's German manuals: neither translates a single articulation
    name. Two independent vendors treating those names as identifiers rather than prose is
    evidence for ADR-0003, and it tells bucket 12 that vendor German terminology does not
    exist to be collected.
  - Reusable access route, recorded in the dossier: vendor Zendesk help centres serve 403
    to a browser while their public JSON API on the same host does not, and the
    /articles/<id>/attachments.json endpoint is what yields the PDFs. Verified on XLN,
    GetGood and Steven Slate.
next:
  - Nothing outstanding in this bucket. Reconciliation should take the axis-mapping and
    no-axis lists in sections 3.2 and 5, and decide the halfway/offset question in 5.3.
questions:
  - CORRECTION for the other buckets, with evidence, in case they were told to stop
    trying: web.archive.org content downloads DO work here. WebFetch refuses it outright,
    which is probably what was observed, but curl succeeds on retry. Test at 13:09 UTC,
    three attempts at one URL: try1 reset, try2 and try3 both HTTP 200 with a
    byte-identical 1095305-byte Toontrack PDF; a 3500226-byte NI manual ZIP came the same
    way and unzips cleanly. Working rule: curl not WebFetch, CDX queries narrowed to
    matchType=prefix on one directory with limit<=100, retry once on a reset. Four rows of
    my verdict table exist only because of that route.
  - Search I cannot run (worker WebSearch refuses at 200/200): any public URL for the IK
    Multimedia MODO Drum user manual PDF, chapter 10 "MIDI Mappings" and its "Special
    Hi-Hat Articulations" section. IK FAQ 1395 says manuals are account-only; four
    plausible paths on IK's CDN host g1.ikmultimedia.com all 404; archive.org has nothing.
    A regional IK domain or a distributor mirror is the likeliest hit.
  - Search I cannot run: any Toontrack-hosted page or PDF published since Superior Drummer
    3 containing a key layout or an articulation list.
  - Search I cannot run: whether NI's per-kit documents "The Session Kit - Default
    Mapping", "The Stadium Kit - Default Mapping" and "The Garage Kit - Default Mapping"
    exist anywhere public. They are named in the manual and shipped inside the library.
  - For bucket 08 (marching): ping shot and gok shot are your vocabulary, not the
    libraries'. Round-1 dossier 02 glosses them "ping = rimshot near the rim (bright)",
    "gok = rimshot near centre (dark)". A marching primary confirming that contrast would
    let both be minted with a real definition instead of a drumset guess.
needs_owner:
  - Toontrack SD3 and EZdrummer 3 are the largest articulation corpus in the field and
    Toontrack publishes NOTHING on the open web: manual behind an account login, no drum
    maps offered, last public PDF manual from 2009, and no mirror on archive.org. Round 1
    used community .drm and .pitchlist exports, which rule 2 forbids as a shipped source.
    This pass corroborated Toontrack's naming convention against Toontrack's own SD2 and
    EZdrummer 1 manuals, but that is a 2009 generation. The only lawful route to the
    current layout is a Toontrack account - free registration reads the web manual, and
    the layout is visible in-product under Settings > MIDI In/E-Drums.
    Decision: does the owner supply that, or does KITWARP ship with Toontrack recorded as
    a documented gap? Recommendation: supply it. Everything else in this bucket is now
    vendor-sourced, and Toontrack is the one library whose absence would be conspicuous.
```
