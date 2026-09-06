# Research dossiers

The evidence behind the ADRs. Each dossier was compiled by reading primary sources directly
— cloning repositories, fetching manufacturer documentation, parsing shipped data files —
and each ends with its own provenance table and a list of claims it could not verify.

These are working documents, not curated data. Nothing here is authoritative for the
dataset; the dataset's authority is the provenance record on each assertion (ADR-0004).
They are committed so that every claim in an ADR can be traced without repeating the work.

| # | Dossier | Feeds |
|---|---|---|
| 01 | Existing open-source drum remappers: data models, pivots, inversion loss | ADR-0001 |
| 02 | Notation and OSS percussion vocabularies (MuseScore, Hydrogen, LilyPond, SMuFL) | ADR-0001 |
| 03 | GM, GM2, Roland GS and Yamaha XG percussion vocabularies | ADR-0001 |
| 04 | E-drum modules: zone terminology and hi-hat controller behaviour | ADR-0001 |
| 05 | Sample-library articulation vocabularies, and Jamstix's rival pivot | ADR-0001 |
| 06 | Drum machines and grooveboxes: timbre lineage and slot-only devices | ADR-0001 |
| 07 | Hand, Latin and orchestral percussion naming | ADR-0001 |
| 08 | Export target formats and their field sets | ADR-0001, ADR-0002 |
| 09 | Storage format and C++ codegen, with measured benchmarks | ADR-0002 |
| 10 | Licensing, provenance schema, and stable-ID precedent | ADR-0003, ADR-0004 |
| 11 | Published drum-sound taxonomies from MIR datasets and the literature | ADR-0001 |
| 12 | GGD `.nka` structure and the Jamstix map format | ADR-0001, inventory |

`scratch:` in a path refers to a working directory outside the repository that no longer
exists. Where a dossier cites a cloned repository it also gives the upstream URL and the
commit.

## Reading order

`01` establishes what the existing converters do and where they lose information. `02`, `03`
and `11` are the three independent checks on the axis decomposition — open-source notation,
the MIDI standards, and the academic taxonomies. `04`, `05`, `06` and `07` supply the
vocabulary breadth from the devices themselves. `08` bounds the model from the export side.
`09` and `10` decide the engineering and legal mechanics.
