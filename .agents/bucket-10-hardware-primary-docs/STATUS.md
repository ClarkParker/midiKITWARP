status: done
updated: 2026-09-06T14:35:00Z
done:
  - Dossier committed and pushed at docs/research/round2/10-hardware-primary-docs.md
  - THE ACCESS PROBLEM IS SOLVED AND IT WAS NEVER ACCESS. static.roland.com is
    an S3 bucket with ListBucket denied, so a key that does not exist answers
    403 AccessDenied with an XML body instead of 404. Every earlier 403 was a
    guessed filename. Roland's own naming is inconsistent across products, so
    guessing cannot work: TD-27_Data_List_eng04_W.pdf, TD-50X_DataList_eng01_W.pdf,
    TD-30_Datalist_e01.pdf and TD-15_11_Datalist.pdf all coexist in one bucket.
  - Working Roland route, 200 every time: GET
    www.roland.com/global/support/by_product/<slug>/owners_manuals/, follow each
    per-document UUID page, take the static.roland.com href out of it.
  - Second Roland host: legacy products live on
    lib.roland.co.jp/support/en/manuals/res/<id>/<file>.pdf, indexed at
    /global/support/archives/archive_manuals_<range>/. HTTP-ONLY: https is 000,
    http is 200.
  - Working Yamaha route: usa.yamaha.com/support/manuals/index.html
    ?l=en&c=drums&k=<keyword> is server-rendered and hands over direct PDF links.
    download.yamaha.com is only a JavaScript redirect stub and is a dead end.
  - Regional Roland sites are a DEAD END for this bucket: roland.com/de and
    roland.com/uk carry only localised Quick Start and Reference Manuals. The
    Data List and MIDI Implementation are English-only, on /global.
  - 60+ documents enumerated with exact URL and live HTTP status, per document,
    in section 1 of the dossier. Every current Roland and Yamaha document the
    bucket named is officially downloadable and was reached 200.
  - EXCLUSION GROUPS CAPTURED, and the answer contradicts the premise. Four
    vendors implement four structurally different relations, only two undirected:
      Roland MUTE SEND / MUTE RECEIVE, 1-8, DIRECTED, per zone, configurable
      Yamaha AltGroup S1-32 / R1-32, DIRECTED, per layer, configurable
      Yamaha AltGroup S&R1-32, UNDIRECTED, per layer, configurable
      Yamaha Mono/Poly, SELF-exclusion, per layer
      Elektron Analog Rytm voice coupling, DIRECTED, per track, NOT configurable
        (CP mutes RS, HT mutes MT, OH mutes CH, CB mutes CY - hardware fixed)
      Roland TR-727 pair exclusion, UNDIRECTED, per voice, NOT configurable
    A single directed choke edge cannot represent any of these faithfully. The
    minimum shape needed is group id + role in {send, receive, both} +
    configurable flag + granularity in {zone, layer, track, voice}.
  - Round A: 17 distinct enumeration passes over vendor portals rather than a
    search engine, because the worker WebSearch quota stayed exhausted the whole
    time. The vendor indexes were the better instrument anyway.
  - Round B: zone and voice terminology extracted from Roland TD-50X/TD-27/
    TD-17/TM-6 PRO/HPD-20/TR-08/TR-8S, Yamaha DTX-PRO/DTX-PROX, ATV aD5,
    2Box DrumIt Five MkII in English, German and French, Alesis support
    articles, Elektron Analog Rytm, and the TR-808/TR-727/LinnDrum/Oberheim DMX
    manuals from archive.org.
  - 21 terms found that fit NO existing axis, including hi-hat pedal pressure
    past fully closed, choke as a technique, the Yamaha kick rim, Yamaha's
    four velocity layers per zone, ATV's zone index A/B/C, Roland's
    rubber-versus-mesh capability gate, and the harmonic stroke.
  - python -m tools.validate, tools.format --check and the IOM roundtrip check
    all pass on the committed tree.
next:
  - Nothing. Bucket complete.
questions:
  - Does the Roland SPD-30 Octapad documentation exist anywhere on roland.com?
    It is named in the bucket task and I could not find it: no by_product slug
    (spd-30 and spd-30_octapad both return an index with zero documents) and no
    entry in any of the five archive_manuals ranges. One search would settle it:
    SPD-30 Octapad owner's manual site:roland.com
  - Where are the Alesis Strike Pro and Strata Prime user guide PDFs served
    from? The Freshdesk articles link Salesforce knowledge articles rather than
    PDFs, and guessed cdn.inmusicbrands.com paths 404 exactly the way Roland's
    did, which suggests the same fix: find the real path in an article that
    actually links one. Suggested search: Alesis Strike Pro Kit user guide pdf
    cdn.inmusicbrands.com
  - Is there any officially downloadable Roland document for the TR-808 or
    TR-909? I found none on roland.com; the only copies are unlicensed
    third-party scans on archive.org. The TR-08 and TR-8S reissue documents are
    official but their voice sets differ from the originals, so they cannot
    stand in for them.
  - Licensing: is the reconciliation pass allowed to cite a vendor PDF by URL
    plus SHA-256 without redistributing it? Every document reached is free to
    download from the manufacturer but none carries a redistribution licence,
    and the archive.org scans carry no licence at all.
needs_owner:
  - Whether unlicensed third-party scans on archive.org (TR-808 and TR-727
    owner's manuals, TR-909 service notes, LinnDrum, Oberheim DMX, SP-1200) may
    be used as a WORKLIST to decide what to look for, given rule 2 says curated
    third-party collections are never the shipped source. I treated them as
    worklist-only and recorded every claim with its scan identifier, but the
    drum-machine voice names in the dossier have no licence-clean source and
    the manufacturers do not publish these documents at all.
