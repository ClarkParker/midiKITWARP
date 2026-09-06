# Legacy `.iom` reference files

Eleven `.iom` files carried over from the preparatory work, kept here as **reference and
test material**, not as curated data.

## What they are

Each file maps a foreign drum layout onto one host's internal layout. The direction is
`foreign note → host note`; see `docs/01-format-iom.md` for the container and for the
evidence establishing that direction.

| File | Layout it describes |
|---|---|
| `Ad2.iom` | XLN Addictive Drums 2 |
| `Alesis_DM10.iom` | Alesis DM10 |
| `Alesis_Strike.iom` | Alesis Strike |
| `Bfd3.iom` | FXpansion BFD3 |
| `EZDrummer2.iom` | Toontrack EZdrummer 2 |
| `Pearl_Mimic_Pro.iom` | Pearl Mimic Pro |
| `Roland_TD30.iom` | Roland TD-30 |
| `Studio_Drummer.iom` | Native Instruments Studio Drummer |
| `Superior3.iom` | Toontrack Superior Drummer 3 |
| `Yamaha_DTX900.iom` | Yamaha DTX900 |
| `Yamaha_DTXplorer.iom` | Yamaha DTXplorer |

`legacy-iom-analysis.json` is the earlier JSON dump of the same tables together with a
per-file collision analysis. It is superseded by `tools/iom/analyze.py` and kept only so the
earlier numbers stay reproducible.

## Provenance — deliberately incomplete

**These files do not meet this repository's provenance standard and are not promoted into
`data/devices/`.**

- Source: unknown. The root element is `SAMPLER_IOMapInfo` and the display names carry an
  `ED_` prefix, which points at a Steven Slate Drums host, but that is inference, not a
  verified origin.
- Date obtained: unknown.
- Method: product file (`P`), assumed.
- Licence status: unknown.

They are useful for three things and nothing else:

1. verifying the `.iom` reader and writer round-trip (`tools/iom/roundtrip_check.py`),
2. measuring what a note-number pivot costs (`tools/iom/analyze.py`),
3. cross-checking a layout that has been derived independently from a primary source —
   a disagreement is a signal to look again, never a reason to overwrite the primary source.

Every layout these files touch is still an open row in `docs/05-inventory.md` and has to be
re-derived from a primary source before it becomes curated data.
