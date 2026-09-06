# Bucket 10 — E-drum and drum-machine primary documentation

Round 2 dossier. Deliverable is ZONE and VOICE terminology plus controller
behaviour, and a per-document access report. Note numbers are Phase 3 and are
deliberately not extracted here.

Observer: worker `bucket-10-hardware-primary-docs`.
Collection date: 2026-09-06. All HTTP statuses below were observed on that date
from this environment.

---

## 0. The access problem, solved

The task said "direct Roland Data List PDF paths return 403 while the owner's
manuals return 200". That framing is wrong, and the wrongness is the finding.

`static.roland.com` is an S3 bucket served with `ListBucket` denied. S3 answers a
request for a **non-existent key** with `403 AccessDenied`, not `404`. Verified:

```
$ curl -s https://static.roland.com/assets/media/pdf/TD-50X_Data_List_eng01_W.pdf
<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>AccessDenied</Code><Message>Access Denied</Message>
<RequestId>ZF3461K2PSKGESYJ</RequestId>...</Error>
```

The real filename is `TD-50X_DataList_eng01_W.pdf` — no underscore between
"Data" and "List". Fetching that returns `200`, 2 732 524 bytes. Nothing is
blocked. Every earlier 403 was a guessed filename, and guessing cannot work
because Roland's own naming is inconsistent across products:

| Product | Data List filename |
|---|---|
| TD-27 | `TD-27_Data_List_eng04_W.pdf` |
| TD-50X | `TD-50X_DataList_eng01_W.pdf` |
| TD-30 | `TD-30_Datalist_e01.pdf` |
| TD-15/TD-11 | `TD-15_11_Datalist.pdf` |
| TM-6 PRO | `TM-6_PRO_DataList_eng01_W.pdf` |

Four spellings of the same words in one bucket.

### Route A — Roland, current products (verified, 200 every time)

1. `GET https://www.roland.com/global/support/by_product/<slug>/owners_manuals/`
2. That page links one UUID page per document:
   `/global/support/by_product/<slug>/owners_manuals/<uuid>/`
3. Each UUID page contains the literal
   `https://static.roland.com/assets/media/pdf/<file>.pdf` href.
4. Fetch it.

Harvester used: `roland_all.py` (breadth-first over the index, then per-document).
89 documents enumerated across 17 product slugs; 88 returned `200`, one UUID page
is a duplicate listing with no PDF link of its own (the SPD-SX PRO Reference
Manual, which is reachable from the sibling entry).

Slug gotchas found: `td-07` and `td-02` are not slugs — the kits are, `td-07kv`
and `td-02k`. The HandSonic is `handsonic_hpd-20`, not `hpd-20`. `spd-30` and
`r-8` do not exist as slugs at all.

### Route B — Roland, legacy and discontinued products

Listed at `https://www.roland.com/global/support/archives/archive_manuals_<range>/`
where `<range>` is one of `0-9`, `a-g`, `h-m`, `n-s`, `t-z`. These point at a
**different host**: `lib.roland.co.jp/support/en/manuals/res/<id>/<file>.pdf`.

That host is **HTTP-only from here**. `https://lib.roland.co.jp/...` returns
`000` (TLS failure); `http://lib.roland.co.jp/...` returns `200`. Verified with
`TD-20_r_e6.pdf`, 4 643 561 bytes.

### Route C — Yamaha

`https://usa.yamaha.com/support/manuals/index.html?l=en&c=drums&k=<keyword>` is
**server-rendered** and returns direct
`usa.yamaha.com/files/download/other_assets/<n>/<id>/<file>.pdf` links. No
JavaScript needed.

`download.yamaha.com` is a redirect stub — its `/common/common-redirect.js`
simply bounces to `https://<countrysite>/support/`. It is useless to a fetcher
and is the reason earlier passes concluded Yamaha was unreachable.

Yamaha filename suffix convention, verified across models:

| Suffix | Meaning |
|---|---|
| `_dl_` / `_Data_List_` | Data List |
| `_rm_` / `_reference_manual_` | Reference Manual |
| `_om_` / `_owners_manual_` | Owner's Manual |
| `_am_` | Assembly Manual |
| `_sm_` | Service/Setup Manual |

Keyword matching is literal substring on the model string: `DTX6` finds nothing,
`DTX6K` finds the kit. `DTX900` finds nothing, `DTX900M` does.

`jp.yamaha.com/support/manuals/index.html?l=ja&c=drums&k=...` serves from the
**same** `usa.yamaha.com/files/...` host and adds the Japanese-language editions
(`..._Ja_...`). No document is available there that is not available in English.

### Route D — regional Roland sites are a dead end for Data Lists

Checked on the supervisor's instruction. `roland.com/de/...` and
`roland.com/uk/...` for TD-50X return only the localised subset: Quick Start,
Reference Manual, Supplementary Manual, DWe pad note. **Neither the Data List nor
the MIDI Implementation appears on any regional site** — Roland publishes those
English-only, on `/global`. The regional sites are useful only for
German/French/Italian/Spanish *Reference Manuals*, which is a different value
(see section 2.7).

### Route E — archive.org, for the vintage drum machines

`archive.org` proper works: `advancedsearch.php`, `/metadata/<id>` and
`download/<id>/<id>_djvu.txt` all return `200`. `web.archive.org` does **not** —
every connection resets mid-tunnel by both curl and WebFetch. A bare request to
`web.archive.org` can return a bodyless 302 that looks like success; it is not.

Everything found on archive.org for this bucket is a **third-party upload of a
copyrighted vendor document with no declared licence** (`licenseurl` absent,
`rights` absent). Uploader for most of the drum-machine manuals is
`manuallibrary@textfiles.com`. Treat as `all rights reserved`, worklist only,
never a shipped source. See section 1.4.

---

## 1. Candidate source register (Round A)

Round A ran breadth-first over vendor portals rather than a general search
engine, because the worker's WebSearch quota was exhausted for the whole session
(confirmed twice by the supervisor: 200/200, separate from the supervisor's own
quota) and `web.archive.org` is unreachable. The vendor indexes turned out to be
the better instrument anyway — they are authoritative about what exists.

Distinct enumeration passes run (17, against different corpora and phrasings):

1. Roland `by_product` owner's-manual index, 24 product slugs probed
2. Roland `archives/archive_manuals_*`, all five ranges
3. Roland regional `de` and `uk` product manual indexes
4. Roland Japanese `roland.co.jp` and `roland.com/jp` manual indexes
5. Yamaha `usa.yamaha.com` manual library, English, category `drums`, 15 keywords
6. Yamaha `jp.yamaha.com` manual library, Japanese
7. Yamaha product `downloads.html` pages (dead end, JS)
8. Alesis Freshdesk support portal solution search
9. 2Box support page
10. ATV per-product `support.html` file listings
11. Simmons `simmonsdrums.net/manuals/` index
12. Thomann product page embedded manual links (Millenium)
13. GEWA `gewamusic.com` / `gewadrums.com`
14. Pearl `pearldrum.com`
15. Elektron `support-downloads/<product>`
16. Korg `support/download/product/` and `manual/` endpoints
17. archive.org `advancedsearch.php`, eight title queries

### 1.1 Roland — current products (all officially downloadable, all reached)

Access column: **Official** = served by the manufacturer from its own host, free
and unauthenticated. **Reached** = HTTP status observed here.

| Document | Official URL | Reached |
|---|---|---|
| TD-50X Data List | `https://static.roland.com/assets/media/pdf/TD-50X_DataList_eng01_W.pdf` | 200, 2 732 524 B |
| TD-50X MIDI Implementation | `.../TD-50X_MIDI_Imple_eng02_W.pdf` | 200, 173 305 B |
| TD-50X Reference Manual (EN) | `.../TD-50X_Reference_eng01_W.pdf` | 200, 6 956 730 B |
| TD-50X Reference Manual (DE) | `.../TD-50X_Reference_deu01_W.pdf` | 200, 6 906 152 B |
| TD-50X v1.30 Supplementary | `.../TD-50X_v130_SupplementaryManual_eng01_W.pdf` | 200 |
| TD-50X v1.20 Supplementary | `.../TD50X_v120_SupplementaryManual_eng01_W.pdf` | 200 |
| TD-50X DWe pad configuration | `.../TD-50X_DWePads_eng02_W.pdf` | 200 |
| TD-50 Data List | `.../TD-50_DataList_eng04_W.pdf` | 200, 2 115 695 B |
| TD-50 MIDI Implementation | `.../TD-50_MIDI_Imple_eng04_W.pdf` | 200, 162 568 B |
| TD-27 Data List | `.../TD-27_Data_List_eng04_W.pdf` | 200, 2 114 600 B |
| TD-27 MIDI Implementation | `.../TD-27_MIDI_Imple_eng04_W.pdf` | 200, 146 709 B |
| TD-17 Data List (v2.00) | `.../TD-17_DataList_eng03_W.pdf` | 200, 1 282 327 B |
| TD-17 MIDI Implementation (v2.00) | `.../TD-17_MIDI_Imple_eng04_W.pdf` | 200, 154 166 B |
| TD-07 Data List | `.../TD-07_Data_List_eng01_W.pdf` | 200, 280 496 B |
| TD-07 MIDI Implementation | `.../TD-07_MIDI_Implementation_eng01_W.pdf` | 200, 117 973 B |
| TD-02 MIDI Implementation | `.../TD-02_MIDI_Implementation_eng01_W.pdf` | 200, 83 917 B |
| TD-30 Data List | `.../TD-30_Datalist_e01.pdf` | 200, 899 000 B |
| TD-30 MIDI Implementation | `.../TD-30_MIDI_Imple_e01.pdf` | 200, 1 263 542 B |
| TD-25 Sound List | `.../TD-25_SoundList_e01_W.pdf` | 200 |
| TD-25 MIDI Implementation Chart | `.../TD-25_MIDI_Implementation_Chart_e01_W.pdf` | 200 |
| TD-15/TD-11 Data List | `.../TD-15_11_Datalist.pdf` | 200, 758 331 B |
| TM-6 PRO Data List | `.../TM-6_PRO_DataList_eng01_W.pdf` | 200, 2 630 581 B |
| TM-6 PRO MIDI Implementation | `.../TM-6PRO_MIDI_Imple_eng02_W.pdf` | 200, 112 252 B |
| TM-6 PRO Reference Manual | `.../TM-6_PRO_Reference_eng01_W.pdf` | 200 |
| TM-2 Sound List | `.../TM-2_SoundList_e01_W.pdf` | 200 |
| SPD-SX PRO MIDI Implementation | `.../SPD-SX_PRO_MIDI_Imple_eng01_W.pdf` | 200, 87 863 B |
| SPD-SX PRO Wave List | `.../SPD-SX_PRO_WaveList_multi01_W.pdf` | 200 |
| SPD-SX PRO Reference Manual (v2.00) | `.../SPD-SX_PRO_Reference_eng04_W.pdf` | 200 |
| SPD-SX Sound List | `.../SPD-SX_PA.pdf` | 200 |
| HandSonic HPD-20 MIDI Implementation | `.../HPD-20_MI.pdf` | 200, 828 615 B |
| HandSonic HPD-20 Patch List | `.../HPD-20_PA.pdf` | 200, 869 257 B |
| HandSonic HPD-20 Owner's Manual | `.../HPD-20_OM.pdf` | 200, 21 180 448 B |
| TR-8S MIDI Implementation Chart | `.../TR-8S_MIDIImpleChart_eng03_W.pdf` | 200, 49 847 B |
| TR-8S Preset INST Tone List (v3.00) | `.../TR-8S_PresetToneList_eng04_W.pdf` | 200 |
| TR-8S Reference Manual (v3.00) | `.../TR-8S_Reference_eng05_W.pdf` | 200 |
| TR-08 MIDI Implementation Chart | `.../TR-08_MIDI_Imple_Chart_eng01_W.pdf` | 200, 25 943 B |
| TR-08 Owner's Manual | `.../TR-08_eng04_W.pdf` | 200 |

**VAD series carries no documents of its own.** VAD706 lists the TD-50X set,
VAD506 the TD-27 set, VAD307 the TD-17 set, VAD103 the TD-07 set, plus
stand/shell hardware manuals (DTS-30S, DCS-30/DBS-30, PDS-20). Phase 3 should
treat VAD as a layout over an existing module, never as a separate note map.

**SPD-30 (Octapad) is not on roland.com at all.** No `by_product` slug, no
archive entry found. Its documentation is the single largest official gap in this
bucket — see section 6.

### 1.2 Yamaha (all officially downloadable, all reached)

| Document | Official URL | Reached |
|---|---|---|
| DTX-PROX Data List (Ver.2) | `https://usa.yamaha.com/files/download/other_assets/2/2325612/DTX-PROX_Data_List_En_v200_B0.pdf` | 200, 1 112 076 B |
| DTX-PRO Data List (Ver.2) | `.../1/2325611/DTX-PRO_Data_List_En_v200_C0.pdf` | 200, 1 051 585 B |
| DTX-PRO / DTX-PROX Reference Manual (Ver.2) | `.../3/2323553/DTX-PRO_DTX-PROX_reference_manual_En_v200_C0.pdf` | 200, 1 837 599 B |
| DTX-PROX Owner's Manual | `.../1/1354801/DTX-PROX_owners_manual_En_D0.pdf` | 200, 5 598 138 B |
| DTX-PROX Data List (v1, superseded) | `.../1/1464111/dtx-prox_en_dl.pdf` | 200 |
| DTX900 Data List | `.../1/314381/dtx900_en_dl_b0.pdf` | 200, 464 361 B |
| DTX700 Data List | `.../4/323584/dtx700_en_dl_a0.pdf` | 200, 555 742 B |
| DTX700 Reference Manual | `.../5/323575/dtx700_en_rm_a0.pdf` | 200 |
| DTX-MULTI 12 Data List | `.../0/314160/dtxm12_en_dl_a0.pdf` | 200, 1 421 985 B |
| DTX502 Reference Manual | `.../9/329779/dtx502_en_rm_a0.pdf` | 200, 477 807 B |
| RHH135 Owner's Manual | `.../8/1262778/RHH135_owners_manual_5MULTI_B0.pdf` | 200, 6 452 347 B |
| PCY65/65S/135/155 Owner's Manual (EN/DE/FR/ES) | `.../7/335047/pcy65_65s_135_155_en_de_fr_es_om_a0.pdf` | 200, 916 967 B |
| XP70/XP80 Owner's Manual | `.../6/323576/XP70_XP80_owners_manual_En_B0.pdf` | 200 |
| PCY175 Owner's Manual | `.../7/323577/PCY175_owners_manual_En_B0.pdf` | 200 |

**DTX6, DTX8, DTX10 have no Data List of their own.** The Yamaha library returns
only assembly manuals and rack/stand manuals for `DTX6K`, `DTX8K`, `DTX10K`. The
DTX6K and DTX8K carry the **DTX-PRO** module and the DTX10K the **DTX-PROX**, so
the DTX-PRO / DTX-PROX Data Lists are their Data Lists. UNVERIFIED that the kit
supplements nothing — no supplement document exists in the library to check.

DTX-PROX and DTX-PRO Data Lists are also offered as `.zip` (108–109 KB) alongside
the PDF; the zip is a machine-readable variant and may be worth Phase 3's
attention over the PDF.

### 1.3 Other e-drum vendors

| Vendor / document | Official URL | Reached |
|---|---|---|
| 2Box DrumIt Five MkII User Manual (EN) | `https://2box-drums.com/wp-content/uploads/2020/05/2BOX-DrumIt-Five-Mk2-User-Manual.pdf` | 200, 4 297 120 B |
| 2Box DrumIt Five MkII Bedienungsanleitung (DE) | `.../2020/10/2BOX-DrumIt-Five-MK2-Bedienungsanleitung.pdf` | 200, 2 354 102 B |
| 2Box DrumIt Five MkII Mode d'emploi (FR) | `.../2021/06/2BOX-DrumIt-Five-MKII-Mode-demploi.pdf` | 200, 2 936 813 B |
| 2Box DrumIt 3 & 5 sound list | `.../2019/01/soundsDrumIt3_and_5-1.pdf` | 200, 577 531 B |
| 2Box DrumIt Five User Manual OS 1.24 | `.../2023/05/DrumIt-Five-User-Manual-OS-1.24.pdf` | listed, 200 index |
| 2Box crosstalk manual OS 1.34.10 | `.../2020/01/Crosstalk-manual-for-OS-1.34.10.pdf` | listed, 200 index |
| ATV aD5 Reference Guide | `https://www.atvcorporation.com/en/products/drums/ad5/file/840/aD5_rg_en06.pdf` | 200, 1 002 859 B |
| ATV aD5 pad compatibility list | `.../ad5/file/1156/aD5_pad_compatibility_en07.pdf` | 200, 260 706 B |
| ATV aD5 Quick Start, 9 languages | `.../ad5/file/841..849/aD5_qs_<lang>04.pdf` | 200 index |
| ATV EXS series manual (KR) + QS in 9 languages | `.../exs-5_3/file/...` | 200 index |
| Millenium MPS-1000 manual (EN) | `https://fast-images.static-thomann.de/pics/atg/atgdata/document/manual/c_511732_528678_v2_r4_en_online.pdf` | 200, 2 816 427 B |
| Millenium MPS-1000 Handbuch (DE) | `.../c_511732_528678_v2_r4_de_online.pdf` | 200, 2 820 609 B |
| Simmons manual index (30+ legacy modules, SDS/SD series) | `https://simmonsdrums.net/manuals/` | 200 index; individual PDFs on `simmonsdrums.net/wp-content/uploads/2022/09/` |
| Alesis support portal (Freshdesk) | `https://support.alesis.com/support/solutions` | 200; article HTML only |
| Alesis Strike Pro hi-hat configuration article | `.../articles/69000823572-alesis-strike-pro-kit-hi-hat-configuration-and-troubleshooting` | 200 |
| Alesis Strike Pro FAQ article | `.../articles/69000801282-alesis-strike-pro-kit-frequently-asked-questions` | 200 |
| Elektron Analog Rytm MKII User Manual (OS 1.72) | `https://www.elektron.se/wp-content/uploads/2025/01/Analog-Rytm-MKII-User-Manual_ENG_OS1.72_250130.pdf` | 200, 13 216 102 B |
| Elektron Analog Rytm MKII Quick Guide | `.../2024/09/AnalogRytmMKIIQuickGuide_ENG_231122.pdf` | 200 index |
| Korg Volca Beats Owner's Manual | `https://cdn.korg.com/us/support/download/files/a8a87f14c9e3aef6f0e4429d15c92c36.pdf` | 200, 3 360 577 B |

**Not reached, with live locator:**

| Vendor | Locator | Status here | Note |
|---|---|---|---|
| Pearl (Mimic Pro) | `https://pearldrum.com/`, `https://www.pearldrum.com/support` | **403** on every path incl. root | CDN/WAF block, not a filename problem. Pearl documents exist and are official; a different network would reach them. |
| EFNOTE | `https://efnote.com`, `https://efnotedrums.com` | **000**, connection refused | Host does not answer at all from here. |
| GEWA | `https://gewadrums.com/en/downloads` | 200 but **zero bytes** to curl; WebFetch returns empty | JavaScript-rendered index; no server-rendered fallback found. |
| Alesis manual PDFs | `https://cdn.inmusicbrands.com/alesis/...` | 404 on every guessed path | Same class of problem Roland had; the correct paths are inside the Freshdesk articles, which cite `inmusicbrands.force.com` Salesforce article URLs rather than PDFs. |
| Roland SPD-30 Octapad | no slug on `roland.com`; no archive entry | **absent** | See section 6. |
| 2Box DrumIt Three/Five MIDI implementation chart | not present on the support page | **does not exist** as a separate document | Zone/note table is inside the user manual instead. |

### 1.4 Vintage drum machines — archive.org (third-party, NOT officially downloadable)

Every entry below is a scan uploaded by a third party. `licenseurl` and `rights`
are **absent** on all of them. Under `docs/adr/0004-provenance-and-licensing.md`
that means all rights reserved: **worklist only, never a shipped source**. The
manufacturers do not publish these documents themselves — Roland's site has no
TR-808, TR-909, TR-707, TR-727, TR-606, TR-626 or R-8 entry of any kind.

| Document | archive.org identifier | Uploader | Text reached |
|---|---|---|---|
| Roland TR-808 Owner's Manual | `synthmanual-roland-tr-808-owners-manual` | manuallibrary@textfiles.com | `_djvu.txt`, 72 027 B |
| Roland TR-808 service notes (1983-07-12) | `synthmanual-roland-tr-808-service-notes` | manuallibrary@textfiles.com | `_djvu.txt`, 51 714 B |
| Roland TR-808 service notes (alt scan) | `roland_TR-808_SERVICE_NOTES` | sketch@cow.net | `_djvu.txt`, 41 870 B |
| Roland TR-909 service notes | `roland_TR-909_SERVICE_NOTES` | sketch@cow.net | `_djvu.txt`, 40 353 B |
| Roland TR-909 Service Manual | `roland_Roland_TR-909_Service_Manual` | — | listed, not fetched |
| Roland TR-707/727 Service Notes | `Roland_TR-707_TR-727_Service_Notes` | — | listed, not fetched |
| Roland TR-727 Owner's Manual (1985) | `synthmanual-roland-tr-727-owners-manual` | manuallibrary@textfiles.com | `_djvu.txt`, 82 381 B |
| Roland TR-606 Service Notes (1982-01-06) | `roland-tr-606-service-notes-jan.-6-1982-600-dpi` | — | listed |
| Roland TR-606 Schematics | `Roland_TR-606_Schematics` | — | listed |
| Roland TR-626 Owner's Manual (1987) | `synthmanual-roland-tr-626-owners-manual` | manuallibrary@textfiles.com | listed; no OCR layer |
| Roland TR-626 Service Notes | `roland_TR-626_SERVICE_NOTES` | — | listed |
| Roland TR-626 Operation Chart (1988) | `roland-tr-626-operation-chart-1988` | — | listed |
| LinnDrum Owner's Manual | `synthmanual-linndrum-owners-manual` | manuallibrary@textfiles.com | `_djvu.txt`, 51 593 B |
| Oberheim DMX Owner's Manual | `synthmanual-oberheim-dmx-owners-manual` | manuallibrary@textfiles.com | `_djvu.txt`, 58 397 B |
| Oberheim DMX Schematics (1981-12-21) | `JL11363` | — | listed |
| Oberheim DX Owner's Manual, 1st ed. | `oberheim-dx-owners-manual` | — | listed |
| E-mu SP-1200 Owner's Manual | `synthmanual-emu-sp-1200-owners-manual` | manuallibrary@textfiles.com | `_djvu.txt`, 179 748 B |
| E-mu SP-1200 Service Manual (1987) | `emu-sp-1200-service-manual-1987` | — | listed |
| Alesis SR-16 Reference Manual | `manualslib-id-4005` | ManualsLib mirror | listed |

**Not found on archive.org:** Linn **LM-1** owner's manual (all `LM-1` title hits
are NASA Apollo documents and unrelated engineering memos — the drum machine's
manual is not there under that title), Yamaha **RX5** (21 `RX5` hits, none the
Yamaha drum machine), Elektron **Machinedrum** (Elektron's own site lists only
current products; the Machinedrum is discontinued and its manual was not located).

### 1.5 Roland patents and service notes for the 808/909 voice circuits

The task named these. **Not obtained.** The service notes above are the closest
primary artefact and they do carry the circuit-level voice names (section 2.6),
but they are third-party scans. No patent document was retrieved: patent search
requires a search engine, and this worker's WebSearch quota is exhausted
session-wide. This is the single most useful thing the reconciliation pass could
chase — see section 6.

---

## 2. Extracted terminology (Round B)

### 2.1 Roland — zone names, normative

Locator: **TD-50X Data List**, `TD-50X_DataList_eng01_W.pdf`, section
"MIDI note numbers transmitted and received by the hi-hat" and "...by the snare"
(p. 6–7 of the PDF; text lines 262–284 of the extracted layout text).

Verbatim, angle-bracket notation is Roland's own:

| Roland token | Verbatim gloss from the document |
|---|---|
| `HI-HAT OPEN <BOW>` | "MIDI note number transmitted and received by open hi-hat (bow, edge)" |
| `HI-HAT OPEN <EDGE>` | idem |
| `HI-HAT CLOSE <BOW>` | "MIDI note number transmitted and received by closed hi-hat (bow, edge)" |
| `HI-HAT CLOSE <EDGE>` | idem |
| `HI-HAT PEDAL` | "MIDI note number transmitted and received by pedal hi-hat" |
| `SNARE <HEAD>` | "MIDI note number transmitted and received by head shot and rim shot" |
| `SNARE <RIM>` | idem |
| `SNARE <BRUSH>` | "MIDI note number transmitted and received by brush sweep" |
| `SNARE <XSTICK>` | "MIDI note number transmitted and received by cross stick" |

TM-6 PRO uses `HH CLOSE <BOW>`, `HH CLOSE <EDGE>`, `HH PEDAL` — the same tokens
with `HI-HAT` abbreviated to `HH`
(`TM-6_PRO_DataList_eng01_W.pdf`, lines 706–711).

The TD-17 Data List has `SNARE <XSTICK>` but **no** `SNARE <BRUSH>`
(`TD-17_DataList_eng03_W.pdf`, lines 639–654) — brush sweep is a TD-50/TD-50X/
TD-27 capability only.

Zone names appearing in trigger settings but not in the note-number tables:
`BOW`, `EDGE`, `BELL` for cymbals; `HEAD`, `RIM` for drums.

### 2.2 Roland — playing methods, normative

Roland's own umbrella term is **"playing method"**. Locator: TD-27 Data List
p. 31, table headed "Trigger inputs and playing methods corresponding chart";
identical table in TD-50X Data List p. 38.

Named playing methods, with the trigger inputs that support them (TD-50X):

| Playing method | Supported on | Note |
|---|---|---|
| Rim Shot | SNARE, TOM 1–4, HI-HAT, CRASH 1–2, RIDE, AUX 1–4 | HI-HAT/CRASH/RIDE only with a **rubber** pad, not a mesh pad |
| Cross Stick | SNARE, AUX 1–4 | "Cross-stick is possible only for SNARE" (TD-27 memo) |
| Bell shot | RIDE only | "Bell shots are possible only for RIDE" (TD-27 memo) |
| Brush sweep | SNARE only | "Brush sweep can be used only SNARE" (TD-27 memo) |
| Positional Sensing (Head) | SNARE, TOM 1–4, RIDE, AUX 1–4 | hi-hat only with a VH-14D |
| Rim Shot Nuance | SNARE, TOM 1–4, AUX 1–4 | not RIDE |
| Choke play | all cymbal and hi-hat trigger types (see 2.3) |

The **rubber-vs-mesh distinction is normative and load-bearing**: the TD-50X and
TD-27 charts both split the Rim Shot column into "Rubber Pad" and "Mesh Pad", and
cross-stick is available on neither hi-hat nor cymbal at all. The vocabulary has
no way to say "this technique depends on the pad surface material".

`Trig Type list` (TD-50X Data List p. 38, TD-27 p. 31) is a per-pad-model
capability matrix with exactly these columns:

```
Trig Type | Rim shot | Bell shot | Positional sensing (Head | Rim) | Choke play
```

Rows cover every Roland pad model: KD-A22/222/220/200/180/180L/140/120/85/10/9/8/7
and KT-10/KT-9 (kick, no capabilities); PDA120/PDA120L/PDA100/PDA100L/PDA140F
(rim shot + rim positional); PD-128/125X/125/108/105X/105/85, PDX-100 (rim shot +
head **and** rim positional); PDX-12/8/6, PD-8 (rim shot only); VH-10/11/12/13
(rim shot + choke); CY-5/CY-8 (rim shot + choke); CY-12C/CY-14C and their `-T`
variants (rim shot + head positional + choke, no bell); CY-12R/C, CY-13R, CY-14R-T,
CY-15R, CY-16R-T (rim shot + **bell shot** + head positional + choke);
BT-1 (nothing); generic PAD1/PAD2/PAD3; acoustic triggers RT-30K/RT-30HR/RT-30H/
RT-10K/RT-10S/RT-10T.

### 2.3 Roland — controller behaviour, normative

Locator: **TD-50X MIDI Implementation**, `TD-50X_MIDI_Imple_eng02_W.pdf`,
"1. Receive Data / Channel Voice Messages / Control Change", pp. 1–2.

Roland defines **six named continuous quantities** carried over control change,
and every eligible CC number carries the same triple gloss verbatim:

```
vv = Control value: 00H–7FH (0–127)
     Pedal position:       open to closed
     Head strike position: center to perimeter
     Rim strike position:  deep to shallow
```

The five named CC roles are (`[SETUP]-[MIDI]-[CONTROL]` tab):

| Role | What it controls, verbatim |
|---|---|
| **Hi-Hat Pedal CC** | "the hi-hat control pedal position changes" |
| **Snare CC** | "used for the snare pad head and rim" |
| **Ride CC** | "used for the ride pad bow" |
| **Toms/AUXs CC** | "used for the heads and rims of TOM 1–4 and AUX 1–4" |
| **Hi-Hat CC** | "used for the hi-hat pad bow" |
| **Hi-Hat LR CC** | "used for the hi-hat pad bow and edge" |

Assignable CC numbers, from TM-6 PRO Data List line 769 (identical set on TD-50X):

```
HH Pedal CC:  OFF, 1, 2, 4, 11, 16, 17, 18, 19
```

That is Modulation (1), Breath (2), Foot (4), Expression (11), General Purpose
1–4 (16–19). **CC4 is the default but is not privileged** — any of the eight is
normative if configured. A converter that hard-codes CC4 is wrong on a
configured module.

Two behaviours that no other vendor documents:

- **Positional CC precedes its note.** "the strike position of the pad
  corresponding to the note number received **directly afterwards on the same
  note channel** changes." The CC is a prefix qualifier on the next note-on,
  not a free-running controller. Order matters.
- **Lateral position exists.** "If Hi-Hat LR CC has been set, the head and rim
  strike positions change **from left to right**." Confirmed in the TD-50X Data
  List trigger parameters: `Position Adjust LR 1–10`, "Adjusts how the tonal
  character is affected by the left-right strike position", and
  `Position Control ... Bow: Strike position, left-right detection (VH-14D only)`,
  `Edge: left-right detection (VH-14D only)`.

Choke is **continuous, not a switch**: "Polyphonic Key Pressure ... If the value
is greater than 1, the decay of the note sounded by the received note number will
be shortened based on the value (Used in choking)." Locator: TD-50X MIDI
Implementation p. 1, Polyphonic Key Pressure. Roland carries choke on
**poly aftertouch keyed to the note number**, not on a CC.

Hi-hat trigger parameters (TD-50X Data List, TRIGGER / HI-HAT tab, p. 37):

| Parameter | Range | Verbatim explanation |
|---|---|---|
| `Hi-Hat Type` | set automatically from Trig Type | "Type of hi-hat" |
| `Offset` | -100–+100 | "Extent of opening Hi-Hat. The bigger the value is, the wider the opening extent is." |
| `Foot Splash Sens` | -10–+10 | "Amount of how easy to make the foot splash" |
| `Noise Cancel` | 1–3 | "Amount of strength to cancel the bow and edge noise when you play foot close." |
| `Pressure Sens` | 1–5 | "Adjusts how the sound of the closed hi-hat changes according to how hard you press down on the pedal (the pressure used) **while the pedal is closed**." VH-14D only. |
| `CC MAX` | 90, 127 | "Amount of control change that is transmitted in stepping the hi-hat pedal down completely." |

`CC MAX = 90` is the reason the repository's controller note says "Roland
transmits 0-90". That is confirmed here and it is **a setting, not a constant** —
the alternative is 127.

`Pressure Sens` is a **second continuous dimension beyond fully closed**: pedal
pressure applied after the hi-hat is already shut. Nothing in the vocabulary can
express it; `openness` bottoms out at `tight`.

Digital-pad trigger parameters (TD-50X Data List, DIGITAL TRIGGER ADVANCED, p. 37):
`Position Adjust 1–10`, `Position Adjust LR 1–10`, `XStick Detect Sens OFF, 1–5`,
`Choke Sens OFF, 1–5`, `Bell Gain 0–3.2` ("balance between the force of a strike
on the bell (bell shot technique) and the loudness of the sound").

### 2.4 Roland — voice taxonomy, normative

Roland's word for a sound is **Instrument**, and each instrument carries an
**Instrument group**. Complete group list extracted from the TD-50X Instrument
List (`TD-50X_DataList_eng01_W.pdf` p. 65 onward), with occurrence counts:

```
KICK A (25)          KICK B (15)          KICK PROC (64)       KICK ELEC (31)
SNARE (37)           SNARE PROC (70)      SNARE ELEC (36)      SNARE BRUSH (2)
CROSS STICK (18)     CROSS STICK PROC (6)
TOM (74)             TOM PROC (16)        TOM ELEC (42)        TOM BRUSH (2)
HI-HAT (19)          HI-HAT PROC (9)      HI-HAT ELEC (4)      HI-HAT FIXED ELEC (10)
RIDE (36)            CRASH (32)           CHINA (12)           SPLASH (10)
STACKED CYMBAL (16)  CYMBAL PROC (20)     CYMBAL ELEC (14)     CYMBAL OTHERS (10)
BLOCK/COWBELL (20)   BELL/CHIME/GONG (11) PERCUSSION (104)     PERC ELEC (36)
CLAP (48)            SOUND FX (86)        ELEMENTS (28)        OFF (1)
```

The **suffix system is the finding**, not the individual names. Roland encodes
timbre as an orthogonal suffix on the instrument family:

- bare = acoustic sample
- `PROC` = processed/produced acoustic
- `ELEC` = electronic/analogue-modelled
- `BRUSH` = brush-played variant, its own group
- `FIXED ELEC` = electronic hi-hat whose openness does not track the pedal

`HI-HAT FIXED ELEC` is a group that exists **because** openness is not
controllable for those sounds. That is a timbre-openness interaction the
vocabulary treats as independent axes.

Per-instrument-group editable parameters (TD-50X Data List, KIT CUSTOMIZE /
INSTRUMENT, pp. 9–11) name physical properties directly:

| Group | Named parameters |
|---|---|
| KICK A/B | `Tuning`, `Muffling` (OFF, TAPE1–4, BLANKET1–3, WEIGHT1–2), `Shell Depth` 1.0–30.0, `Beater Type` (FELT1, FELT2, WOOD, PLASTIC1, PLASTIC2), `Kit Resonance`, `Snare Buzz`, `Mic Distance`, `Mic Size`, `Head Type` (CLEAR, COATED, PINSTRIPE) |
| SNARE / CROSS STICK / SNARE BRUSH | `Muffling` (OFF, TAPE1–7, DONUT1–2), `Overtone`, `Strainer Adj.` (OFF, LOOSE1–3, MEDIUM1–3, TIGHT1–3), `Wire Type` (TYPE1–3), `Wire Level`, `Head Type`, `XStick Inst` 1–5 |
| TOM / TOM BRUSH | `Muffling` (OFF, TAPE1–5, FELT1–4), `Shell Depth`, `Snare Buzz`, `Head Type` |
| HI-HAT / PROC / ELEC | `Size` 1.0–40.0, `Thickness` THIN-5–STANDARD–THICK+5, **`Fixed`: NORMAL, PRESS, CLOSE, HALF1, HALF2, OPEN**, `Pedal HH Volume` |
| CRASH / CHINA / SPLASH / STACKED CYMBAL | `Size`, `Thickness`, `Muffling` (OFF, TAPE1–19), `Sizzle Type` (OFF, RIVET, CHAIN, BEADS), `Sizzle Amount`, `Low Cut` (OFF, HALF, FULL) |
| RIDE | as crash, plus `Ping Color` (LIGHT2, LIGHT1, STANDARD, HEAVY1, HEAVY2), `Ping Level` |

`Fixed` is Roland's normative openness enumeration and its verbatim gloss is
"Openness of the hi-hat. If something other than NORMAL is selected, the openness
of the hi-hat does not change, regardless of how you press the hi-hat pedal."
Its anchors are **NORMAL, PRESS, CLOSE, HALF1, HALF2, OPEN** — six values, and
`PRESS` is the pedal-pressure state described in 2.3.

Also normative: `Pedal Bend Range -24–0–+24`, "Specifies the amount of pitch
change that occurs according to the depth to which you press the hi-hat pedal.
You can set this for each pad (head and rim separately) in semitone units."
The hi-hat pedal is a **global pitch controller for every pad**, not just the
hi-hat.

### 2.5 Yamaha — Inst, Voice, trigger input source

Locator: **DTX-PRO / DTX-PROX Reference Manual Ver.2**,
`DTX-PRO_DTX-PROX_reference_manual_En_v200_C0.txt`, "How the Triggers Generate
Sounds", pp. 9–11.

Two terms defined verbatim, and they are **not** synonyms:

> **Inst** — "'Inst' refers to each of the percussion instruments (snare, tom,
> cymbal, and kick) used in a drum set for the kit. With the PRO series modules,
> you can use a different inst on each trigger input."

> **Voice** — "'Voice' refers to a sound that makes up an Inst. With the PRO
> series modules, you can use a different voice on each trigger input source. For
> example, on an acoustic snare drum you can play a head shot sound, open rim
> shot sound, and a closed rim shot sound all from the same pad. Each one of
> these different sounds is called a voice."

So Yamaha: **Inst = instrument, Voice = per-zone sound**. One Inst spans several
Voices, one per zone. This is exactly the KITWARP instrument/site split, named.

> **Trigger input source** — "Trigger input source is a trigger signal
> transmitted from each zone of a pad."

Complete Yamaha trigger-input-source token set (Reference Manual p. 9 table):

| Trigger input | Sources | Token gloss |
|---|---|---|
| Snare | `SnareHd`, `SnareOp`, `SnareCl` | Head, **Open** rim shot, **Closed** rim shot |
| Tom1–3 | `Tom1Hd`, `Tom1Rm` … | Head, Rim |
| Ride | `RideBw`, `RideEg`, `RideCp` | Bow, Edge, **Cup** |
| Crash1, Crash2 | `Crash1Bw`, `Crash1Eg`, `Crash1Cp` | Bow, Edge, Cup |
| HiHat | `HhOpBw`, `HhOpEg`, `HhClBw`, `HhClEg`, `HhFtCl`, `HhFtSp` | Open bow, Open edge, Closed bow, Closed edge, **Foot Close**, **Foot Splash** |
| Kick | `Kick`, `KickRm` | Kick, Kick **rim** |
| Pad14 | `Pad14Hd`, `Pad14Rm1`, `Pad14Rm2` | Head, Rim 1, Rim 2 |

Three of these have no Roland equivalent:

- `HhFtSp` — foot splash is a **first-class trigger input source with its own
  note**, not a derived event. Roland has `Foot Splash Sens` but no separate
  foot-splash zone token.
- `KickRm` — a **rim zone on the kick drum**. Nothing in the vocabulary or in
  Roland's model has this.
- `Rm1` / `Rm2` — a numbered second rim on a single pad. The vocabulary has
  `rim2` on the site axis, which matches.

**Layers.** "Four layers (A to D) are provided for each trigger input source. You
can set a voice to each layer... You can set the velocity range to each layer so
that you can play a different voice in response to the strength of each strike."
(Reference Manual p. 11.) So Yamaha's full addressing is
`Inst → trigger input source (zone) → layer A–D → voice`, with velocity
switching between layers. Layer is a fifth level the pivot model has no name for.

Yamaha voice categories, from the DTX-PROX Data List "Voice" section, pp. 14–23:

```
Kick1  Kick2  Snare1  Snare2  Tom1  Tom2  Cymbal1  Cymbal2  HiHat1  HiHat2
Perc  Effect
```

The `1` / `2` split is acoustic-vs-electronic: `Kick1` is `22MplAHM1`,
`22x18Rock1`, `22Vintage1`, `20x16Jazz1`; `Kick2` is `RX5`, `RX11`, `T8-1..T8-8`,
`T9-1..T9-7`, `EDM 1–6`, `Gate 1–4`, `Electro 1–20`, `R&B 1–2`, `HipHop 1–11`,
`Break`, `DNB 1–2`. `T8` and `T9` are Yamaha's unbranded names for TR-808 and
TR-909 samples.

Position-sensing capability is a per-voice footnote in the Data List:

```
(*1) Supports RealAmbi.
(*2) Supports position sensing for head shots and open rim shots.
(*3) Supports position sensing for bow shots.
(*4) Selecting this will change the Inst EQ settings ... to the default one for each Inst.
```

So on Yamaha, positional sensing is a **property of the sampled voice**, not only
of the pad. Roland says the same thing informally ("You will also need to select
an Inst or a voice that supports position sensing", Reference Manual p. 59) but
only Yamaha marks it per voice in a machine-readable table.

### 2.6 Yamaha — controller behaviour

Locator: **DTX-PROX Data List**, MIDI Data Format and MIDI Implementation Chart,
pp. 25–28.

| CC | Yamaha's verbatim description |
|---|---|
| 0, 32 | Bank Select. MSB=125 LSB=0 Preset Kit, LSB=1 User Kit 1–100, LSB=2 User Kit 101–200 |
| **4** | "Foot Controller messages are transmitted and received. MIDI Ch 10 only." |
| **16** | "General Controller messages are transmitted and received. **Corresponds to the location of the strike on the Snare.** MIDI Ch 10 only." |
| **17** | "General Controller messages are transmitted and received. **Corresponds to the location of the strike on the Ride.** MIDI Ch 10 only." |
| 80 | received only. "Corresponds to the AMBIENCE knob value." |
| 81 | received only. "Corresponds to the COMP knob value." |
| 82 | received only. "Corresponds to the EFFECT knob value." |
| 1–95 | transmitted, "depend on Message Type or Pad Function setting" |

Yamaha **fixes** CC4 for the hi-hat pedal and CC16/CC17 for snare/ride strike
position, on channel 10 only. Roland makes all of these configurable. The two
vendors happen to agree on 4/16/17 by default, which is why converters get away
with hard-coding — but only Yamaha's is normative.

Hi-hat parameters (Reference Manual pp. 59–60):

| Parameter | Range | Verbatim |
|---|---|---|
| `FootClosePos` | -32 – 0 | "adjust the position at which the hi-hat switches from open to closed... The lower the value, the smaller the virtual opening between the top and bottom hi-hats." |
| `FootSplashSens` | off, 1–127 | "the degree of sensitivity for detecting hi-hat foot splashes... set this parameter to 'off' if you do not want to play foot splashes." |
| `HH Pitch Up` | off, on | "Specifies whether the pitch is raised (on) or not (off)" |
| `Snare Position` | off, on | "Turn the snare position on for creating tonal changes according to the location **within a zone** that is struck." |
| `Ride Position` | off, on | "Switches the position sensor for the bow of the ride cymbal on or off." |
| `Xstick Adjust` | 1–127 | "Sets the strength for switching the cross sticking to or from the open rim shots when hitting the rim... Turn the cross stick setting off to always play the open rim shot sound." |

`Xstick Adjust` is the important one: on Yamaha, **cross-stick and open rim shot
are the same physical gesture separated by a velocity threshold on the rim
zone**. Roland separates them into different note numbers via `XStick Detect
Sens`. Both vendors agree the discrimination is by strike strength, not by
position.

Yamaha's phrase "**the location within a zone**" is the cleanest normative
statement anywhere in this bucket that `position` is a sub-property of `site`,
not a peer of it. The KITWARP model already has that shape; this is the citation
for it.

### 2.7 Multi-language zone terminology

The vocabulary is English, but scores and vendor manuals worldwide are not, and
these are the vendors' own translations of their own zone names.

**German.** Locator: 2Box DrumIt Five MkII Bedienungsanleitung,
`2BOX-DrumIt-Five-MK2-Bedienungsanleitung.pdf`, p. 4 and the trigger table.
Verbatim: "Der Snare-Kanal hat 3 Zonen (Fell, Rim, Cross Stick), die Tom-Kanäle
... haben 2 Zonen (Fell, Rim), während die Becken-Kanäle wiederum 3
verschiedene Sound-Zonen bieten (Rand/Edge, Fläche/Bow und Kuppe/Bell)."

| English | 2Box German |
|---|---|
| head | **Fell** (literally "skin/hide") |
| rim | **Rim** (untranslated) |
| edge | **Rand** |
| bow | **Fläche** (literally "surface, area" — **not** "Bogen") |
| bell | **Kuppe** (literally "dome, cap") |
| foot | **Fuß** |
| cross stick | **Cross Stick** (untranslated) |

**French.** Locator: 2Box DrumIt Five MKII Mode d'emploi, same pages.

| English | 2Box French |
|---|---|
| head | **tête** |
| rim | **bord** |
| edge | **bord** / **bordure** |
| bow | **arc** in one place, **archet** in another |
| bell | **cloche** |
| foot | **pied** |
| hi-hat | **charleston** |

The French is internally inconsistent in the vendor's own document: `bord` is
used for both snare rim and cymbal edge on the same page, and `archet` (a violin
bow) is a mistranslation of the cymbal `bow`. Recorded as a false friend, not as
authority — see section 4.

A German-language **Roland** Reference Manual exists
(`TD-50X_Reference_deu01_W.pdf`, 200, 6 906 152 B) and would give a second
independent German rendering; it was downloaded but not extracted for lack of
time. Named here so the reconciliation pass can use it.

### 2.8 ATV — the abstract zone-index model

Locator: **ATV aD5 Reference Guide**, `aD5_rg_en06.pdf`, p. 30, section
"Zones corresponding to each trigger input".

Verbatim: "Three tones are assigned to each instrument. These three tones
correspond to zones A, B, and C of the pad; for example, zone A is heard when you
strike the head, and zone B is heard when you strike the rim."

| Trigger input | Zone A | Zone B | Zone C |
|---|---|---|---|
| KICK | Head | — | — |
| SNARE | Head | Rim | **Side Stick** |
| TOM 1–3 | Head | — | — |
| HI-HAT | Bow | Edge | **Foot** |
| CRASH | Bow | Edge | — |
| RIDE | Bow | Edge | **Cup** |
| AUX 1–2 | Head (Bow) | Rim (Edge) | — |

ATV is the only vendor in this bucket that separates the **zone index** (A/B/C,
a slot) from the **zone name** (head/rim/bow/edge/cup, a physical site) and
states the mapping in one table. The `AUX` row's "Head (Bow)" and "Rim (Edge)"
notation says explicitly that head↔bow and rim↔edge are the same slot under two
names depending on whether the pad is a drum or a cymbal.

ATV writes **Side Stick** as two words and **Cup** for the bell, agreeing with
Yamaha and disagreeing with Roland (`XSTICK`, `BELL`).

### 2.9 2Box — zone/channel model

Locator: 2Box DrumIt Five MkII User Manual, p. 4 and the "Drum channel / Trigger
channel / MIDI note / Zone / Choke" table.

Verbatim: "the snare channel, for instance, supports 3 zones (head, rim, cross
stick), the DrumIt Five MKII's tom channels provide 2 (head, rim) and the cymbal
channels 3 (edge, bow and bell). In addition, the cymbal channels feature a
'choke' function".

2Box's structural oddity: **rim zones are routed through separate `PERC` trigger
channels**. Snare rim is `PERC 5`, Tom 1 rim is `PERC 1`, Tom 2 rim is `PERC 2`,
Tom 3 rim is `PERC 3`. The zone is not an attribute of the drum channel; it is a
different channel that happens to be labelled as a zone in the table. That is a
model no other vendor uses and it means a 2Box layout cannot be read as
"instrument + site" without the channel table.

Hi-hat is `A2-A#2-B2` on one channel, three notes for bow/edge/foot.

### 2.10 Alesis — hi-hat controller vocabulary

Locator: Alesis support article 69000823572, "Alesis Strike Pro Kit | Hi-Hat
Configuration and Troubleshooting", HTML, reached 200.

Named zones: **Bow**, **Edge**, **Pedal**. Named articulations: **Open**,
**Closed/Chick**, **Splash**. Named parameters:

| Parameter | Meaning as stated |
|---|---|
| `Offset` | where the module recognises the hi-hat as "closed" |
| `Foot Sens` | chick sound dynamics |
| `Splash` | splash trigger sensitivity |
| `Velocity Curve` | Linear, Log, Exp |
| `Pedal Curve` | "Log favors closed; Exp favors open" |

`Pedal Curve` is a control Roland and Yamaha do not expose: a **transfer function
on the openness axis itself**, separate from the velocity curve. It means the
mapping from physical pedal travel to openness value is vendor-configurable, so
an openness scalar recorded from one module is not directly comparable with one
from another.

Alesis calls the third zone of a cymbal nothing at all — the FAQ says "triple-zone
pad" for the 16" ride and "dual-zone crash cymbals with choke" without naming the
zones. Recorded as a gap.

### 2.11 TR-808 — canonical voice names

Locator: **Roland TR-808 Owner's Manual**, archive.org
`synthmanual-roland-tr-808-owners-manual`, `_djvu.txt` lines 227–234. Verbatim,
Roland's own panel legend:

> "Clockwise from the lower left the choices include AC (ACCENT) BD (BASS DRUM),
> SD (SNARE DRUM), LT (LOW TOM or LOW CONGA), MT (MID TOM or MID CONGA), HT (HI
> TOM or HI CONGA), RS (RIM SHOT or CLAVES), CP (HANDCLAP or MARACAS), CB
> (COWBELL), CY (CYMBAL), OH (OPEN HIHAT), and CH (CLOSED HIHAT)."

Cross-checked against the **TR-08 MIDI Implementation Chart**
(`TR-08_MIDI_Imple_Chart_eng01_W.pdf`, Roland's own 2017 reissue, official
download), whose `Inst.` column reads: BASS DRUM, RIM SHOT, SNARE DRUM, HAND
CLAP, CLOSED HI-HAT, LOW TOM, OPEN HI-HAT, MID TOM, CYMBAL, HIGH TOM, COW BELL,
HIGH CONGA, MID CONGA, LOW CONGA, MARACAS, CLAVES.

**The reissue splits what the original merged.** The 1980 TR-808 has *one* LT
slot that is *either* Low Tom *or* Low Conga, selected by a panel switch. The
2017 TR-08 exposes LOW TOM and LOW CONGA as separate instruments with separate
note numbers. Same for RS/CLAVES and CP/MARACAS. Any layout derived from the
TR-08 chart is not a layout of a TR-808.

Owner's manual on the switch, verbatim (lines 333–337): "The RIM SHOT, HAND CLAP,
and COW BELL have variable LEVEL and RIM SHOT and HAND CLAP can be switched to
become, respectively, CLAVES and MARACAS."

Panel parameter names, from the TR-08 chart's control-change list (Roland's own
canonical abbreviations): `BD TUNE`, `BD TONE`, `BD COMP`, `BD DECAY`, `BD LEVEL`,
`SD TONE`, `SD SNAPPY`, `SD COMP`, `SD DECAY`, `SD LEVEL`, `LT/MT/HT TUNE|DECAY|LEVEL`,
`RS TUNE|DECAY|LEVEL`, `CP TUNE|DECAY|LEVEL`, `CH TUNE|DECAY|LEVEL`,
`OH TUNE|DECAY|LEVEL`, `CY TONE|DECAY|LEVEL`, `CB TUNE|DECAY|LEVEL`, `ACCENT`.

`SNAPPY` is the 808's name for snare-wire amount — the analogue counterpart of
the vocabulary's `mechanism: wires-on / wires-off`, and it is **continuous**, not
binary.

TR-808 service notes (`synthmanual-roland-tr-808-service-notes`, "TR-808 CIRCUIT
DESCRIPTION", ~line 377 onward) confirm the circuit-level grouping: the voices
are built as shared analogue blocks, and `RS/CL` is described as one section
("Output from multifeedback bridged T-network incorporated with IC20 is routed to
IC19. Output from IC21 (for RS), also routed via R320, can be ignored..."). The
manual notes for Low Tom that "Pink noise with a slightly longer decay time is
mixed for Low Tom to provide artificial reverberation". OCR quality is poor and
individual component references should not be trusted from this scan.

### 2.12 TR-8S / TR-909 lineage — the eleven-slot vocabulary

Locator: **TR-8S MIDI Implementation Chart**,
`TR-8S_MIDIImpleChart_eng03_W.pdf` (official Roland download), Notes `*1` table.

Roland's canonical eleven `INST` slot abbreviations:

```
BD  SD  LT  MT  HT  RS  HC  CH  OH  CC  RC
```

with per-slot CCs `<INST> TUNE | DECAY | LEVEL | CTRL`. Expanded:
BD bass drum, SD snare drum, LT low tom, MT mid tom, HT high tom, RS rim shot,
HC **hand clap**, CH closed hi-hat, OH open hi-hat, CC **crash cymbal**,
RC **ride cymbal**.

This is the TR-909 slot set. Note the deltas from the 808 set: the 808 has one
`CY` (cymbal) and no ride/crash split; the 909 splits it into `CC` and `RC`. The
808 uses `CP` for hand clap; the 909 lineage uses `HC`. **`CB` (cowbell) is
absent from the TR-8S set entirely.**

### 2.13 TR-727 — an explicitly symmetric exclusion relation

Locator: **Roland TR-727 Owner's Manual** (1985), archive.org
`synthmanual-roland-tr-727-owners-manual`, `_djvu.txt` "Summary of voices",
lines 735–800. Verbatim:

> "It is not possible to output the following pairs of voices at the same time.
> 1 and 2 (High Bongo and Low Bongo)
> 3 and 4 (Mute High Conga and Open High Conga)
> 8 and 9 (High Agogo and Low Agogo)
> 10 and 11 (Cabasa and Maracas)
> 12(13) and 14 (Short Whistle and Long Whistle)
> For instance, if you have entered the Maracas in the step where the Cabasa has
> already been written, the Cabasa will be automatically replaced with Maracas."

The sixteen TR-727 voices: 1 HI BONGO, 2 LOW BONGO, 3 MUTE HI CONGA, 4 OPEN HI
CONGA, 5 LOW CONGA, 6 HI TIMBALE, 7 LOW TIMBALE, 8 HI AGOGO, 9 LOW AGOGO,
10 CABASA, 11 MARACAS, 12 SHORT WHISTLE, 13 SHORT WHISTLE (duplicate; "The Short
Whistle 12 and 13 are exactly the same"), 14 LONG WHISTLE, 15 QUIJADA,
16 STAR CHIME.

**This is the undirected exclusion class, stated in a primary source.** It is
symmetric ("pairs of voices"), it is a hardware consequence of shared voice
circuits, and it is not a musical choke. `MUTE HI CONGA` / `OPEN HI CONGA` is the
same pair the GM `damping` axis would express as `muted` / `none` on one
instrument — so on this device, an axis value is what creates the exclusion.

### 2.14 Exclusion and mute groups across vendors — four different models

The supervisor asked whether the Data Lists carry exclusion-group assignments.
They do, and the finding is that **the four vendors implement four
structurally different relations**, only one of which is undirected.

**Roland — directed send/receive, 8 groups.** Locator: TD-50X Data List, KIT
MENU / MUTE GRP tab, p. 5; TD-27 Data List p. 22; TM-6 PRO Data List p. 13.
Verbatim:

> "MUTE SEND / MUTE RECEIVE — (OFF), 1–8. When you strike the pad of the number
> specified in MUTE SEND, the sound of the pad assigned to the same number in
> MUTE RECEIVE is muted. * Even if you specify the same number in MUTE SEND and
> MUTE RECEIVE for the same location (e.g., head or rim) of the same pad, muting
> does not occur."

Directed. A pad can be a sender, a receiver, or both; group membership alone does
not imply mutual exclusion. The self-mute exemption is explicit. Roland grants
mute groups **per zone**, not per pad — "the same location (e.g., head or rim)".

TD-17 Data List has **no** mute-group section at all. TD-30 Data List has none
either. This is a TD-27/TD-50/TD-50X/TM-6 PRO feature.

**Yamaha — directed with an explicit symmetric option, 32 groups.** Locator:
DTX-PRO/DTX-PROX Reference Manual, MENU / Kit Edit / Voice, `AltGroup`, p. 62.
Verbatim:

> "AltGroup — off, S&R1–32, S1–32, R1–32. By registering voices that cannot sound
> simultaneously, such as an open and closed hi-hat, to the same alternate group
> number (other than 'off'), you can prevent them from sounding simultaneously.
> Assign **S1–32 to the layer that transmits the mute command**, **R1–32 to the
> layer that receives the mute command**, and **S&R1–32 to the layer that you
> want to transmit and receive mute commands.**
> NOTE: If the specified trigger input source is a hi-hat, setting this parameter
> to anything other than 'off' will disable any effect."

Yamaha's `S&R` variant **is** the undirected exclusion class, and `S` / `R` are
the directed halves — in one field, at layer granularity. This is the richest
model found anywhere in this bucket. The hi-hat exemption is because hi-hat
open/close exclusion is already hardwired.

Yamaha also carries `Mono/Poly` per layer: "If you set this parameter to 'mono,'
when the same pad is struck repeatedly, each successive sound will mute each
previous sound." That is self-exclusion, a third distinct relation.

**Elektron Analog Rytm — directed priority from shared hardware voices.**
Locator: Analog Rytm MKII User Manual OS 1.72, section 8.1, p. 21. Verbatim:

> "8 individual track Sounds can be voiced simultaneously with the eight physical
> voices... The BD, SD, BT, and LT are independent tracks with their separate
> voices. Tracks RS-CP, MT-HT, CH-OH and CY-CB, each pair is shown with a coupling
> on the front panel... If you play or trigger both tracks of a coupled pair, the
> right-hand track has a higher priority. **Track CP mutes track RS, HT mutes MT,
> OH mutes CH and CB mutes CY.**"

Twelve tracks, eight voices, four fixed couplings, and the mute direction is
**fixed by the hardware and not configurable**. Asymmetric.

**Roland TR-727 — symmetric replacement.** Section 2.13. The later voice is
substituted for the earlier one in the same step, both directions.

Summary of the four relations, which the vocabulary needs to distinguish:

| Model | Direction | Granularity | Configurable | Source |
|---|---|---|---|---|
| Roland MUTE SEND/RECEIVE | directed | zone | yes, 8 groups | TD-50X/TD-27/TM-6 PRO Data List |
| Yamaha AltGroup `S`/`R` | directed | layer | yes, 32 groups | DTX Reference Manual p. 62 |
| Yamaha AltGroup `S&R` | **undirected** | layer | yes, 32 groups | idem |
| Yamaha Mono/Poly | self | layer | yes | idem |
| Elektron voice coupling | directed | track | **no** | Analog Rytm manual p. 21 |
| TR-727 pair exclusion | **undirected** | voice | **no** | TR-727 Owner's Manual |

### 2.15 Oberheim DMX — "voice" means a circuit card, not a sound

Locator: Oberheim DMX Owner's Manual, archive.org
`synthmanual-oberheim-dmx-owners-manual`, "THE SOUNDS", p. 16. Verbatim:

> "BASS — Bass drum, with three volume levels.
> SNARE — Snare drum, with three volume levels.
> HIHAT — A hihat, with a closed and an accented sound, plus a longer 'open' sound.
> TOM 1 — A tom-tom, with three individual pitches.
> TOM 2 — A tom-tom, lower in pitch than TOM 1, again with three pitches.
> CYMBAL — This voice contains two sounds, a ride cymbal which can be played
> accented or unaccented, as well as a crash cymbal.
> PERC 1 — This voice also contains two sounds, a tambourine with accent, as well
> as a rimshot.
> PERC 2 — two sounds, a shaker with accent, plus hand claps."

> "The pitch of each of the voices can be tuned up or down half an octave by
> adjusting the pitch controls located inside the DMX on the top rear of **each
> of the voice cards**."

Here `voice` = a swappable EPROM card that can hold **two unrelated instruments**
(`PERC 1` = tambourine + rimshot; `PERC 2` = shaker + hand claps). `CYMBAL`
holds ride and crash. So on the DMX, instrument identity is not recoverable from
the voice name at all, and the pitch control is per-card, i.e. shared by two
instruments.

### 2.16 LinnDrum

Locator: LinnDrum Owner's Manual, archive.org
`synthmanual-linndrum-owners-manual`, `_djvu.txt`. OCR is degraded; only claims
legible in more than one place are recorded.

Named instruments: BASS, SNARE, **SIDESTICK SNARE**, HIHAT (closed / open),
TOM(S), CONGA(S), CABASA, TAMBOURINE, RIDE CYMBAL, CRASH, COWBELL.

Two verbatim points:

> "In addition to the two levels of closed hihat, there is an 'open' hi-hat.
> Pressing the 'closed' hi-hat shortly after pressing the [open one]..."
> (line 114–115; the tail is OCR-damaged but the choke-by-retrigger behaviour is
> legible)

> "The snare, sidestick snare, toms, and congas may be tuned ... to simulate
> different pressures on the hihat pedal." (lines 130–134, OCR-damaged, two
> sentences run together)

`SIDESTICK SNARE` as a **separate named instrument** rather than a technique on
the snare is worth recording: it is the 1982 precedent for Roland treating
`CROSS STICK` as its own instrument *group* forty years later (section 2.4).

The LinnDrum manual is the weakest-quality source in this bucket. Everything
above beyond the instrument names is marked **UNVERIFIED** pending a better scan.

### 2.17 Korg Volca Beats, E-mu SP-1200, Alesis SR-16

Volca Beats manual reached (`cdn.korg.com`, 200, 3 360 577 B) but its text layer
is thin (624 lines for a multi-language leaflet) and its part names were not
extracted. SP-1200 owner's manual text reached (179 748 B) but not mined. Alesis
SR-16 Reference Manual located on archive.org (`manualslib-id-4005`) but not
fetched. All three are recorded as reachable-but-unmined so the reconciliation
pass knows the cost is small.

---

## 3. Axis mapping

### 3.1 Terms that map cleanly

| Source term | Source | Axis | Vocabulary value |
|---|---|---|---|
| `<HEAD>` / `SnareHd` / Head / Fell / tête | Roland, Yamaha, ATV, 2Box | site | `head` |
| `<RIM>` / `Rm` / Rim / Rand | Roland, Yamaha, ATV, 2Box | site | `rim` |
| `Rm1` / `Rm2` | Yamaha | site | `rim`, `rim2` |
| `<XSTICK>` / `SnareCl` / Side Stick / Cross Stick | Roland, Yamaha, ATV, 2Box | site | `crossstick` |
| `<BOW>` / `Bw` / Bow / Fläche / arc | all | site | `bow` |
| `<EDGE>` / `Eg` / Edge / Rand / bord | all | site | `edge` |
| `Cp` (Cup) / Bell / Kuppe / cloche | Yamaha+ATV vs Roland+2Box | site | `bell` |
| Rim Shot / open rim shot / `SnareOp` | Roland, Yamaha | technique | `rimshot` |
| Cross stick / side stick / closed rim shot | all | technique | `sidestick` |
| Bell shot | Roland | technique | `hit` on site `bell` |
| Brush sweep / `SNARE <BRUSH>` | Roland | technique | `sweep`; implement `brush` |
| Foot Close / `HhFtCl` / chick | Yamaha, Alesis | technique | `chick` |
| Foot Splash / `HhFtSp` / Splash | Yamaha, Alesis, Roland | technique | `foot-splash` |
| Choke play / choke | all | technique | (see 3.2 — no axis value) |
| `Fixed: OPEN / HALF1 / HALF2 / CLOSE` | Roland | openness | `open` / `half` / — / `closed` |
| `Muffling: OFF / TAPE / BLANKET / WEIGHT / DONUT / FELT` | Roland | damping | `none` / `muted`, `damped`, `towel` |
| `Strainer Adj.: OFF / LOOSE / MEDIUM / TIGHT` | Roland | mechanism | `wires-off` / — |
| `Beater Type: FELT / WOOD / PLASTIC` | Roland | implement | `felt-beater`, `wood-beater`, `plastic-beater` |
| `KICK ELEC` / `T8-` / `T9-` / TR-808 Kick | Roland, Yamaha | timbre | `analog-808`, `analog-909` |
| `CR-78 Kick`, `TR-606 Kick`, `TR-707 Kick`, `TR-626 Kick`, `DR-110 Kick`, `R-8 Kick` | Roland TD-50X Instrument List | timbre | `analog-cr78`, `analog-606`, `analog-707`, — , — , — |
| `SD FM` / `BD FM` | Elektron | timbre | `fm` |
| `SY CHIP` | Elektron | timbre | `chip` |
| `UT NOISE` | Elektron | timbre | `noise` |
| Pedal position 0–127 open→closed | Roland, Yamaha | controller | `hihat.pedal_position` |
| Head strike position center→perimeter | Roland | controller | `strike_position.radial` |
| Rim strike position deep→shallow | Roland | controller | `strike_position.rim_depth` |
| Head/rim strike position left→right | Roland | controller | `strike_position.lateral` |
| Poly key pressure decay shortening | Roland | controller | `choke_amount` |

### 3.2 Terms that fit NO axis

These are the valuable ones.

**1. `Pressure Sens` / pedal pressure while already closed.** Roland TD-50X Data
List p. 37, verbatim: "Adjusts how the sound of the closed hi-hat changes
according to how hard you press down on the pedal (the pressure used) while the
pedal is closed." Also Roland `Fixed: PRESS` as a named openness anchor.
`openness` is defined as 0.0 closed .. 1.0 open with `tight` as the low anchor.
There is no room below `tight` for a continuous pressure dimension. This is
either a **new axis** or an extension of `openness` below zero.

**2. Choke as a continuous amount with no axis home.** The `technique` axis has
no `choke` value at all, yet every vendor names choke, Roland transmits it as
continuous poly key pressure, and the controller axis has `choke_amount`. A
controller exists for a technique that cannot be named. Either `technique` needs
`choke` or the model needs a statement that choke is controller-only.

**3. Kick rim (`KickRm`).** Yamaha Reference Manual p. 9. A rim zone on a kick
drum, addressable as its own trigger input source. `site: rim` on
`instrument: kick` is expressible, but nothing says it exists, and no other
vendor has it.

**4. Layer (A–D) with velocity ranges.** Yamaha Reference Manual p. 11. A fifth
addressing level below the zone. `dynamic` has `ghost/soft/normal/hard/accent`
but those are qualitative labels, not a per-zone velocity-range partition with a
different sound in each band. The DMX's "three volume levels" and "three
individual pitches" per voice card are the same idea in 1981.

**5. Zone index vs zone name.** ATV's A/B/C. The model has `site` (a name) but no
notion of an ordinal slot that carries different names on different instrument
types. Needed to read an ATV or 2Box layout at all.

**6. Pad surface material as a capability gate.** Roland's rubber-vs-mesh split
in the playing-methods chart. Whether `rimshot` is available at all depends on
the pad's surface. Not an axis of the term; an axis of the *layout slot*.

**7. Exclusion relations.** Section 2.14. Four structurally different relations
(directed, undirected, self, hardware-fixed) and the vocabulary has only a
directed choke.

**8. `SNAPPY` as a continuous snare-wire amount.** TR-808. `mechanism` has
`wires-on` / `wires-off`, a binary. Roland's own analogue control is continuous
and Roland's own `Wire Level -6–NORMAL–+6` and `Strainer Adj. LOOSE1-3/MEDIUM1-3/
TIGHT1-3` on the TD-50X are graded, not binary.

**9. `Sizzle Type: RIVET / CHAIN / BEADS`.** Roland TD-50X. `sizzle-ride` exists
as an *instrument*, so a sizzle ride is a different instrument from a ride — but
Roland models sizzle as a **parameter of any cymbal** with three named
mechanisms. Neither `mechanism` nor `voicing` has room for it.

**10. `Ping Color: LIGHT / STANDARD / HEAVY`.** Roland RIDE parameter. The
vocabulary has `ping-shot` as a technique but no way to grade the ping character.

**11. `Position Area: INSIDE-5 – DEFAULT – OUTSIDE+5`.** Roland TD-50X Data List
p. 5. A calibration remap of the radial position axis, per pad. It means the
`position` values `centre/halfway/offset/perimeter` are relative to a
configurable window, not absolute geometry.

**12. `Pedal Bend Range -24..+24` semitones, per pad, head and rim separately.**
Roland TD-50X. The hi-hat pedal is a pitch controller for every other pad. There
is no axis and no controller for "pedal-driven pitch of an unrelated instrument".

**13. `HH Pitch Up: off/on`.** Yamaha. Same phenomenon, boolean.

**14. Instrument-group suffixes `PROC` / `ELEC` / `FIXED ELEC`.** Roland. `PROC`
("processed") is neither `acoustic` nor `electronic` on the `timbre` axis — it is
a produced acoustic sample. `timbre` has no value for it. 70 SNARE PROC and 64
KICK PROC instruments have nowhere to go.

**15. `RealAmbi` support flag.** Yamaha per-voice footnote `(*1)`. A voice-level
capability, not a term.

**16. Roland `ELEMENTS` group (28 instruments) and `CYMBAL OTHERS` (10).** Vendor
catch-all groups whose members are not instruments in any organological sense.
Named here because Phase 3 will meet them.

### 3.3 Terms that map but with a warning

- `Cup` (Yamaha, ATV) and `Bell` (Roland, 2Box) are the same site. Mapping to
  `bell` is right, but `bell` is **also an instrument slug** in the vocabulary
  (id 17, `kit.cymbal`). `site: bell` and `instrument: bell` are different
  things and a naive text match will conflate them.
- `SnareOp` / `SnareCl` (Yamaha) look like open/closed and map to
  `rimshot` / `sidestick`. A reader who assumes `Op`/`Cl` mean the hi-hat sense
  of open/closed will get it exactly wrong.
- Roland `HI-HAT OPEN <BOW>` vs `HI-HAT CLOSE <BOW>` are two note numbers for one
  `site: bow` differing only in `openness`. The site is not what varies.

---

## 4. Conflicts and false friends

**`bell` vs `cup`.** Roland and 2Box say **bell**; Yamaha and ATV say **cup**;
both mean the raised centre boss of a cymbal. The vocabulary uses `bell`. In
addition `bell` is a KITWARP instrument slug. Three meanings, one word.

**`bow` in German.** 2Box's own German is **Fläche** ("surface"), not the
literal `Bogen`. A German-language corpus search for `Bogen` will miss 2Box
entirely and will hit string-instrument arco instead.

**`bord` in French.** 2Box's French uses `bord` for the snare **rim** and
`bord`/`bordure` for the cymbal **edge** on the same page. The distinction the
English model depends on does not survive the vendor's own translation.

**`archet` in French.** 2Box writes `archet` for the cymbal bow in one place and
`arc` in another. `archet` is a violin bow. This is a vendor error, recorded so
nobody treats it as terminology.

**`open` / `closed`.** Three incompatible senses in this bucket:
1. hi-hat cymbal separation (Roland `HI-HAT OPEN/CLOSE`, everyone);
2. rim-shot type (Yamaha `SnareOp` open rim shot vs `SnareCl` closed rim shot =
   cross stick);
3. conga hand technique (TR-727 `MUTE HI CONGA` / `OPEN HI CONGA`).
Sense 2 is the trap: Yamaha's `Cl` is the vocabulary's `sidestick`, not
`openness: closed`.

**`voice`.** Four incompatible senses:
1. Yamaha: a per-zone sound within an Inst;
2. Oberheim DMX: a physical EPROM card holding up to two unrelated instruments;
3. Elektron Analog Rytm: a physical analogue sound-generation circuit, of which
   there are eight for twelve tracks;
4. TR-727: a numbered slot in a fixed list of sixteen.
The bucket task asked for "VOICE terminology"; the answer is that the word does
not denote one thing.

**`instrument`.** Roland `Instrument` = a sound (an entry in the Instrument
List). KITWARP `instrument` = the physical thing that makes the sound. Roland's
`Instrument group` is closer to the KITWARP sense, but it mixes family with
timbre (`KICK ELEC`).

**`machine`.** Elektron's word for a sound-generation model (`BD HARD`,
`CY RIDE`). Not related to `drum machine`. `CY RIDE` is a *machine* on the CY
track — i.e. a ride sound produced by the cymbal voice circuit, which is a
timbre/instrument conflation in one token.

**`rim shot`.** Roland's `Rim Shot` on a hi-hat or crash trigger input means
striking the pad's edge sensor, not an acoustic rim shot. Same words, different
gesture, and Roland's own playing-methods chart lists `Rim Shot` for `HI-HAT` and
`CRASH` where the physical rim does not exist.

**`RS`.** TR-808 `RS` = Rim Shot (a voice). Roland V-Drums `RS` does not occur,
but `RT-10S`/`RT-30HR` are acoustic triggers. Elektron `RS` = Rim Shot track.
Yamaha `Rm` = rim. Three abbreviations for overlapping concepts.

**`CP` vs `HC`.** Hand clap is `CP` on the TR-808 and `HC` on the TR-8S/TR-909
lineage. Both are Roland. A converter keyed on the abbreviation will fail across
the two families.

**`CY`.** TR-808 `CY` is a single cymbal voice that is neither crash nor ride.
TR-8S has `CC` and `RC` and no `CY`. Elektron `CY` is a cymbal track whose
machines include `CY RIDE`. Three different scopes.

**`LT` / `MT` / `HT`.** On the TR-808 these are *either* toms *or* congas by
panel switch. On the TR-8S and Analog Rytm they are toms only. Analog Rytm adds
`BT` (Bass Tom) as a fourth, which has no counterpart anywhere else and whose
machine is `BT CLASSIC` while LT/MT/HT all use `XT CLASSIC`.

**Tom instance ordering.** The vocabulary fixes tom `instance` high-to-low in
pitch. Roland's trigger inputs are `TOM 1–4` and the TD-50X Data List does not
state a pitch ordering for them; Yamaha's are `Tom1–Tom3`. Elektron's are
`BT, LT, MT, HT` — **low to high**, the opposite direction, and named rather than
numbered. Nothing in the vendor documents guarantees the vocabulary's direction.
UNVERIFIED that Roland's `TOM 1` is the highest tom; the Data Lists do not say.

---

## 5. Gaps against vocabulary v0.1

### 5.1 Missing values on existing axes

| Axis | Missing | Evidence |
|---|---|---|
| `site` | `cup` as an alias of `bell` (correction alias, not a new id) | Yamaha `RideCp`, ATV "Cup" |
| `site` | a name for the kick rim | Yamaha `KickRm` |
| `technique` | `choke` | every vendor; Roland transmits it continuously |
| `technique` | `bell-shot` or a statement that it is `hit`+`site:bell` | Roland playing-methods chart |
| `openness` | an anchor for pedal pressure past closed | Roland `Fixed: PRESS`, `Pressure Sens` |
| `timbre` | a value for "processed acoustic" | Roland `*PROC`, 140+ instruments |
| `timbre` | `analog-626`, `analog-dr110`, `analog-r8` | Roland TD-50X Instrument List: `TR-626 Kick`, `DR-110 Kick`, `R-8 Kick` |
| `damping` | `blanket`, `weight`, `donut` as muffling mechanisms | Roland `Muffling` value lists |
| `mechanism` | a graded snare-wire tension rather than a binary | Roland `Strainer Adj.`, TR-808 `SNAPPY` |
| `mechanism` | `sizzle-rivet`, `sizzle-chain`, `sizzle-beads` | Roland `Sizzle Type` |
| `implement` | nothing missing found; `fist`/`fingernail` unused by these vendors | — |
| `voicing` | `vintage`, `hybrid` appear as Roland instrument names but not as a voicing axis | TD-50X `Hybrid 2021 K`, `Vintage1 22" K` |

### 5.2 Misnamed

- **`crossstick`** (site) is spelled as one word with no hyphen while every other
  multi-word site is a single word too, so it is internally consistent — but the
  four vendors spell it `XSTICK` (Roland), `SnareCl`/closed rim shot (Yamaha),
  `Side Stick` (ATV), `Cross Stick` (2Box). No vendor writes `crossstick`. A
  `correction` alias set is needed, not a rename (identifiers are forever).
- **`bell`** used for both an instrument and a site is the single most likely
  source of future confusion. It cannot be renamed. It needs a documented
  disambiguation rule.
- **`sidestick`** (technique) and **`crossstick`** (site) name the same gesture
  from two axes. That is defensible, but no vendor separates them, so every
  vendor mapping will have to set both.

### 5.3 Structurally missing

1. **An exclusion/mute relation with a direction flag.** Four vendor models,
   section 2.14. Minimum viable shape: group id, plus role in
   `{send, receive, both}`, plus a `configurable` boolean, plus granularity in
   `{zone, layer, track, voice}`.
2. **A layer concept** with velocity ranges (Yamaha A–D, DMX volume levels).
3. **A zone-index concept** distinct from the zone name (ATV A/B/C).
4. **A capability matrix on the layout slot**: which playing methods this pad
   supports, gated on surface material. Roland publishes exactly this table for
   every pad model it sells.
5. **A statement that positional CC is a prefix qualifier on the next note**, not
   free-running. Roland states it; a converter that ignores it will attach the
   position to the wrong note.
6. **A note that `hihat.pedal_position` full-scale is a setting**, not a
   constant: Roland `CC MAX` is 90 **or** 127. The controllers note in
   `axes.json` says "Roland transmits 0-90", which is true only by default.
7. **A note that the openness transfer curve is vendor-configurable** (Alesis
   `Pedal Curve`), so openness scalars are not comparable across modules.

### 5.4 Instrument-axis gaps this bucket found

The vocabulary reserves `perc.*`, `orch.*` etc. as unminted. This bucket supplies
the primary-source names for a large part of that reservation:

TR-727: hi bongo, low bongo, mute hi conga, open hi conga, low conga, hi timbale,
low timbale, hi agogo, low agogo, cabasa, maracas, short whistle, long whistle,
quijada, star chime.
TR-808: claves, maracas, hi/mid/low conga.
Roland TD-50X groups: `BLOCK/COWBELL`, `BELL/CHIME/GONG`, `PERCUSSION` (104
instruments), `PERC ELEC` (36).
Roland HandSonic HPD-20 Patch List (reached, 869 257 B, not mined) is the single
densest source of hand-percussion instrument names in this bucket.

---

## 6. Self-critique (Round C)

### What is missing

**The SPD-30 Octapad has no documentation on roland.com at all.** No
`by_product` slug (`spd-30`, `spd-30_octapad` both return an index with zero
document entries), no entry in any of the five archive ranges. It is named in the
bucket task. It would add Roland's percussion-pad zone vocabulary, which differs
from the V-Drums vocabulary. **This is the largest official gap.**

**The Roland patents and the 808/909 service notes were not obtained as primary
documents.** archive.org has third-party scans of the service notes and I mined
them, but with poor OCR and no licence. No patent was retrieved at all — patent
search needs a search engine and the worker WebSearch quota is exhausted
session-wide. The bucket task named these explicitly and they are not delivered.

**Pearl Mimic Pro: zero documents.** `pearldrum.com` answers 403 on every path
including the root, from this network. This is a WAF/CDN block, not a filename
problem, and a different network would reach it. The Mimic Pro is the only
sample-playback module in the bucket with a fundamentally different architecture
(it plays multi-velocity sample libraries rather than modelled instruments) and
its zone vocabulary is unknown to this dossier.

**EFNOTE: zero documents.** Host does not answer. **GEWA: zero documents.** The
downloads index is JavaScript-only with no server-rendered fallback.

**Alesis: no PDF, only support articles.** I extracted real terminology from two
Freshdesk articles, but the actual Strike Pro / Strata Prime user guides were not
located — the articles link to Salesforce (`inmusicbrands.force.com`) knowledge
articles rather than to PDFs, and guessed `cdn.inmusicbrands.com` paths 404 the
same way Roland's did. **The fix is certainly the same fix**: find the real path
in the page source of an article that actually links a PDF. I did not exhaust
that.

**Linn LM-1 and Yamaha RX5 not found anywhere.** archive.org has neither under
its own name. The LinnDrum manual I did get is badly OCR'd.

**Elektron Machinedrum not found.** Discontinued; not on Elektron's support pages.

**Not mined, though reached:** HandSonic HPD-20 Patch List and MIDI
Implementation (the densest percussion-name source in the bucket), SPD-SX PRO
Reference Manual, TR-8S Reference Manual and Preset INST Tone List, TM-6 PRO
Reference Manual, TD-50X German Reference Manual, Millenium MPS-1000 manuals
(EN+DE), Simmons legacy manuals, Korg Volca Beats, SP-1200 owner's manual,
Yamaha DTX900/DTX700/DTX-MULTI 12 Data Lists, PCY65/135/155 four-language manual,
RHH135 manual, ATV pad compatibility list. All are on disk or one fetch away and
cost minutes each. The limiting factor was extraction time, not access.

### The single most authoritative source I did NOT get

**The Roland SPD-30 Octapad documentation**, because it is the one document in
the bucket that is named in the task, is unquestionably official, and appears to
be genuinely absent from every Roland route I found. Everything else I missed is
either a licensing problem (the vintage service manuals), a network problem
(Pearl, EFNOTE, GEWA) or a time problem (the reached-but-unmined list).

For the reconciliation pass to chase it, the specific unanswered question is
whether Roland retired the SPD-30 documents entirely or filed them under a slug I
did not guess. A search for `SPD-30 Octapad owner's manual site:roland.com` would
settle it in one query, and I could not run it.

### What I would tell the next worker

The access problem in this bucket was never access. It was that vendor filenames
are not derivable and vendor indexes are not uniform. Both Roland and Yamaha
publish a complete, server-rendered, unauthenticated index of everything they
have; neither is discoverable by guessing. Every one of the 60+ documents this
dossier cites came back `200` on the first try once the index was read. No
Wayback, no mirror, no third-party site was needed for anything a manufacturer
still publishes — and for everything a manufacturer *no longer* publishes (the
1980s drum machines), no route exists that is also licence-clean.
