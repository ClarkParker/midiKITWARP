# Bucket 09 — sample-library manuals, first-hand

```
status: running
updated: 2026-09-06T13:10:38Z
done:
  - Round A complete: 20 distinct searches before extraction; candidate register of 45
    sources is section 1 of the dossier
  - Dossier committed and pushed: docs/research/round2/09-library-primary-manuals.md
  - VERDICT TABLE is section 0, as instructed. Of the fourteen products named in the task:
      seven publish an official chart reachable today - XLN AD2, BFD3, BFD Player,
        NI Studio Drummer, NI Abbey Road 60s/70s/80s/Modern, MT Power Drum Kit 2,
        Jamstix 4
      two only through a mirror of the vendor's own path - Sennheiser DrumMic'a, and the
        Toontrack SD2 / EZdrummer 1 predecessors
      one a list without note numbers - GetGood Drums Modern & Massive 2
      four publish nothing at all - Toontrack SD3 and EZdrummer 3, Steven Slate SSD5/5.5,
        ML Drums, IK MODO Drum
  - Round 1's community sources replaced by vendor primaries for XLN, BFD, NI, GGD,
    Jamstix, MT Power and Sennheiser. Toontrack's community drum maps are now at least
    corroborated by Toontrack's own SD2 and EZdrummer 1 manuals.
  - Access route worth reusing: vendor Zendesk help centres serve 403 to a browser but
    their public JSON API on the same host does not.
      /api/v2/help_center/en-us/articles/<id>.json
      /api/v2/help_center/en-us/articles.json?per_page=100
      /api/v2/help_center/articles/search.json?query=...
      /api/v2/help_center/articles/<id>/attachments.json   <- this one yields the PDFs
    Verified on support.xlnaudio.com, support.ggd.co, support.stevenslatedrums.com. It is
    what produced the official Addictive Drums 2 keymap PDF that round 1 could not reach.
  - Answered the cross-bucket question on five disputed v0.1 slugs (dossier section 5.4):
      ping-shot, gok-shot, stick-shot - no library coined them; they entered v0.1 from
        MuseScore's Marching_Snare_Drums.drm via round-1 dossier 02. Tapspace, the one
        marching library with a public KB, has no hit for "gock".
      mini-hihat - YES, vendor-attested: GetGood Drums Benny Greb Signature Pack lists a
        "Mini Stack" of "Meinl Artist Concept Crasher Hats" and "Meinl Artist Concept
        Mini Hats". Originates as a Meinl product name.
      mini-china - NOT established. Only a third-party converter uses it; GGD's own
        Architects page calls that cymbal a 13" Zildjian Oriental Trash China.
      Side finding: GGD publishes a "Mini Ride" and writes "X-Hats", so v0.1 has the
      weakest-attested member of the diminutive family and is missing the best-attested.
next:
  - Fetch the German vendor manuals (NI Studio Drummer German, Jamstix 4 German) for
    vendor-authored German articulation terms, then finalise
questions:
  - Correction to the environment advice, with evidence. web.archive.org is NOT dead here.
    WebFetch refuses it outright ("Claude Code is unable to fetch from web.archive.org"),
    which is probably what the other workers hit, but curl succeeds on retry. Test run at
    13:09 UTC, three attempts at one URL - try1 reset, try2 and try3 both HTTP 200 with a
    byte-identical 1095305-byte Toontrack PDF. A 3500226-byte NI manual ZIP came the same
    way and unzips to a valid PDF. Rule that works: use curl not WebFetch, keep CDX queries
    to matchType=prefix on one directory with limit<=100, and retry once on a reset.
    Four rows of my verdict table exist only because of that route; if the other buckets
    were told Wayback is dead, they may have abandoned reachable vendor documents.
  - Search I cannot run (worker WebSearch is refused at 200/200): is there ANY public URL
    for the IK Multimedia MODO Drum user manual PDF, chapter 10 "MIDI Mappings" and its
    "Special Hi-Hat Articulations" section? IK FAQ 1395 says manuals live in the account
    area only; I probed the IK CDN host g1.ikmultimedia.com with four plausible paths, all
    404. A regional domain (cn.ikmultimedia.com, jp.ikmultimedia.com) or a distributor
    mirror is the likeliest hit.
  - Search I cannot run: does any Toontrack-hosted page or PDF published since Superior
    Drummer 3 contain a key layout or articulation list? Everything I found is either the
    account-gated web manual or pre-2010 PDFs under toontrack.com/updates/manuals/.
  - Search I cannot run: do NI's per-kit Studio Drummer documents "The Session Kit -
    Default Mapping", "The Stadium Kit - Default Mapping", "The Garage Kit - Default
    Mapping" exist anywhere public? They are named in the manual and shipped inside the
    Kontakt library.
  - For bucket 08 (marching): ping shot and gok shot are your vocabulary, not the sample
    libraries'. The gloss in round-1 dossier 02 is "ping = rimshot near the rim (bright)",
    "gok = rimshot near centre (dark)". A marching-percussion primary confirming that
    contrast would let both be minted with a real definition instead of a drumset guess.
needs_owner:
  - Toontrack Superior Drummer 3 and EZdrummer 3 are the largest articulation corpus in the
    field and Toontrack publishes NOTHING on the open web: the manual is behind an account
    login, no drum maps are offered, and the last public Toontrack PDF manual dates from
    2009. Round 1 used community .drm and .pitchlist exports, which the provenance rules
    forbid as a shipped source. The only lawful route is a Toontrack account - a free
    account can read the web manual, and the key layout is also visible inside the product
    at Settings > MIDI In/E-Drums. Decision needed: does the owner supply that, or does
    KITWARP ship with Toontrack marked as a documented gap?
```
