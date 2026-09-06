status: running
updated: 2026-09-06T13:40:00Z
done:
  - ANSWER TO THE SUPERVISOR CORRECTION, already established before it arrived.
    The Roland 403 is not an access block and needs no Wayback. static.roland.com
    is an S3 bucket with ListBucket denied, so a key that does not exist answers
    403 AccessDenied (XML body, Code AccessDenied) instead of 404. Every earlier
    403 was a guessed filename. Naming is not stable across products:
    TD-27_Data_List_eng04_W.pdf, TD-50X_DataList_eng01_W.pdf,
    TD-30_Datalist_e01.pdf and TD-15_11_Datalist.pdf all coexist, so guessing
    cannot work and does not need to.
  - Working Roland route, HTTP 200 every time: GET
    https://www.roland.com/global/support/by_product/<slug>/owners_manuals/,
    follow each per-document UUID page it links, take the
    static.roland.com/assets/media/pdf/... href out of that page.
  - Second Roland host found: legacy and discontinued products are served from
    lib.roland.co.jp/support/en/manuals/res/<id>/<file>.pdf, listed on
    www.roland.com/global/support/archives/archive_manuals_<range>/. That host
    is HTTP-ONLY here: https returns 000, http returns 200.
  - Working Yamaha route: GET
    https://usa.yamaha.com/support/manuals/index.html?l=en&c=drums&k=<keyword>
    is server-rendered and returns direct
    usa.yamaha.com/files/download/other_assets/... PDF links. Suffix _dl_ is a
    Data List, _rm_ a Reference Manual, _om_ an Owner's Manual. The
    download.yamaha.com search UI is a JavaScript shell and is useless to curl.
  - 29 primary PDFs downloaded, all HTTP 200, all converted to text
  - Round A also reached 2Box, ATV, Simmons and Thomann/Millenium document
    indexes directly; Pearl answers 403 to everything (CDN block, not filename)
  - Confirmed unreachable here: web.archive.org (reset mid-tunnel, curl and
    WebFetch), efnote.com (connection refused), pearldrum.com (403)
next:
  - Build the per-document access table across every product the bucket names,
    with exact URL and live HTTP status for each
  - Round B extraction of ZONE and VOICE terminology and controller behaviour
questions:
  - Is the reconciliation pass allowed to cite a vendor PDF by URL plus SHA-256
    without redistributing it? Every document reached is free to download from
    the vendor but none carries a redistribution licence.
needs_owner:
