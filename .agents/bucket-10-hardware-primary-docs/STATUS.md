status: running
updated: 2026-09-06T12:44:00Z
done:
  - Setup complete, branch pushed
  - SOLVED the Roland "Data List PDF 403" problem. It is not an access control
    block. static.roland.com is an S3 bucket with ListBucket denied, so a key
    that does not exist answers 403 AccessDenied instead of 404. Every earlier
    403 was a guessed filename. The filename convention is not stable across
    products: TD-27_Data_List_eng04_W.pdf, TD-50X_DataList_eng01_W.pdf,
    TD-30_Datalist_e01.pdf, TD-15_11_Datalist.pdf all coexist.
  - Reproducible harvest method that returns HTTP 200 for every document:
    fetch https://www.roland.com/global/support/by_product/<slug>/owners_manuals/,
    read the per-document UUID pages it links, and take the
    static.roland.com/assets/media/pdf/... href out of each one.
  - Confirmed 200 for Data List and/or MIDI Implementation of TD-17, TD-27,
    TD-50, TD-50X, TD-07, TD-02, TD-30, TD-25, TD-15/TD-11, TM-6 PRO,
    SPD-SX PRO, TR-8S, TR-08, and the VAD kits which reuse the module documents
next:
  - Finish round A breadth (12+ distinct searches) across Yamaha, Alesis, 2Box,
    ATV, EFNOTE, GEWA, Pearl, Simmons, Millenium and the drum-machine corpus
  - Round B extraction of ZONE and VOICE terminology plus hi-hat controller
    behaviour from the reached documents
questions:
needs_owner:
