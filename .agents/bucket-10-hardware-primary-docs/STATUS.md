status: running
updated: 2026-09-06T13:05:00Z
done:
  - Setup complete, branch pushed
  - SOLVED the Roland "Data List PDF 403" problem. It is not an access control
    block. static.roland.com is an S3 bucket with ListBucket denied, so a key
    that does not exist answers 403 AccessDenied instead of 404. Every earlier
    403 was a guessed filename. Naming is not stable across products:
    TD-27_Data_List_eng04_W.pdf, TD-50X_DataList_eng01_W.pdf,
    TD-30_Datalist_e01.pdf, TD-15_11_Datalist.pdf all coexist.
  - Reproducible Roland harvest, HTTP 200 every time: fetch
    https://www.roland.com/global/support/by_product/<slug>/owners_manuals/,
    follow each per-document UUID page, take the static.roland.com href.
  - SOLVED Yamaha too: https://usa.yamaha.com/support/manuals/index.html
    ?l=en&c=drums&k=<keyword> is server-rendered and returns direct
    usa.yamaha.com/files/download/other_assets/... PDF links. The suffix _dl_
    marks a Data List, _rm_ a Reference Manual, _om_ an Owner's Manual.
  - Downloaded 29 primary PDFs, all HTTP 200, all converted to text:
    Roland TD-50X, TD-50, TD-30, TD-27, TD-17, TD-15/11, TD-07, TD-02,
    TM-6 PRO, SPD-SX PRO, TR-8S, TR-08; Yamaha DTX-PROX, DTX-PRO, DTX900,
    DTX-MULTI 12, DTX700, DTX502, RHH135, PCY65/135/155
  - NEGATIVE FINDING worth recording: web.archive.org is unreachable from this
    environment by both curl and WebFetch, and the WebSearch budget for the
    whole session was already spent before this worker started. The Wayback
    fallback the brief suggests is therefore unavailable; the vendor portals
    had to be solved directly, which turned out to be the better answer anyway.
next:
  - Round A completion for Alesis, 2Box, ATV, EFNOTE, GEWA, Pearl, Simmons,
    Millenium and the drum-machine corpus
  - Round B extraction of ZONE and VOICE terminology and hi-hat controller
    behaviour from the 29 reached documents
questions:
  - Is the reconciliation pass allowed to cite a vendor PDF by URL plus SHA-256
    without redistributing it? Every document here is free to download from the
    vendor but none carries a redistribution licence.
needs_owner:
