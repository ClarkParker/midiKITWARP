# The `.iom` container format (reverse engineered)

Basis: the eleven files in `data/legacy-iom/` (Ad2, Alesis DM10, Alesis Strike, BFD3,
EZdrummer 2, Pearl Mimic Pro, Roland TD-30, Studio Drummer, Superior 3, Yamaha DTX900,
Yamaha DTXplorer). Every statement below is verified against those eleven files.

## Container

| Offset | Size | Content |
|--------|------|---------|
| 0      | 4    | Magic `56 43 32 21` = `VC2!` |
| 4      | 4    | uint32 little-endian: length of the XML **excluding** the NUL |
| 8      | N    | XML payload (latin-1, no declaration, no whitespace) |
| 8+N    | 1    | `0x00` terminator |
| 9+N    | 1    | Padding byte, **ignore on read** |

File size is always exactly `10 + N`.

The padding byte is garbage from a write buffer that is not zeroed: nine of the eleven
files carry `0x00` there, `Ad2.iom` carries `0x77`, `Superior3.iom` carries `0xbd`. It is
not a checksum — sum and XOR over the payload were both tested and neither matches. Write
`0x00`.

## Payload

A single self-closing XML element; everything lives in attributes:

```xml
<SAMPLER_IOMapInfo IOMapInfoVersion="2" IOMapName="ED_Superior3"
    Nv2_0Cnt="1" Nv2_0-0="67"
    Nv2_1Cnt="1" Nv2_1-0="1"
    ...
    Cv2_127Cnt="1" Cv2_127-0="127"/>
```

- `IOMapInfoVersion` — `"2"` in all files, matching the `2` in `Nv2_` / `Cv2_`.
- `IOMapName` — display name, consistently prefixed `ED_` (E-Drum).
- `Nv2_<k>Cnt` — number of targets for note index k, followed by `Nv2_<k>-<i>`.
- `Cv2_<k>Cnt` / `Cv2_<k>-<i>` — the same shape for controllers.

Both tables always hold 128 entries (k = 0…127).

## Observed occupancy

**`Cnt` is always 0 or 1.** The format formally permits 1:n; none of the eleven files use
it. A reader should still treat the value as a list.

**Indices 120–127 are unassigned in all eleven files** (`Cnt="0"`).

**The CC table is pure identity in all eleven files** (`Cv2_k-0 == k` for every k). It
therefore carries no information. In particular the hi-hat pedal problem (CC4 vs CC1
depending on the library) is *not* addressed here.

## Direction of the note table

**Index = note in the foreign layout, value = note in the host's internal layout.**

The evidence is in the data itself:

| File | identity entries | targets with more than one source |
|---|---|---|
| Superior 3 | 21 | 33 |
| Pearl Mimic Pro | 30 | 30 |
| BFD3 | 36 | 20 |
| Studio Drummer | 43 | 20 |
| EZdrummer 2 | 44 | 19 |
| Ad2 | 52 | 27 |
| Yamaha DTX900 | 70 | 16 |
| Alesis DM10 | 82 | 12 |
| Roland TD-30 | 89 | 11 |
| Alesis Strike | 101 | 11 |
| Yamaha DTXplorer | 101 | 5 |

Superior 3 has the most articulations of all these layouts and at the same time the fewest
identity entries and the most collisions — a rich layout collapsing onto a smaller target
vocabulary. In the opposite direction the pattern would be reversed. Alesis Strike and
DTXplorer are simple modules close to GM and are therefore almost pure identity.

Consequence: the files supply the direction **source → pivot**. The reverse direction
**pivot → target** has to be built, and it is ambiguous exactly at the collisions. Example
Superior 3: source notes 33, 66 and 70 all land on pivot 33.

The host layout is GM-adjacent (kick 36, snare 38, closed hi-hat 42 map to themselves in
most files) but is not guaranteed to be identical to GM.

## Why this project does not adopt `.iom`'s pivot

`.iom`'s pivot is a MIDI note number, so it has at most 128 slots. Measured against the
eleven files, 1320 mapped source notes collapse onto 1038 distinct pivot slots — Superior 3
alone loses 42 % of its distinctions on the way in. See `docs/adr/0001-pivot-vocabulary.md`.
`.iom` remains an import source and an export target, not the internal model.

## Open points

- The exact origin of the files (root tag `SAMPLER_IOMapInfo` suggests SSD5) is not
  verified. Irrelevant for the parser.
- Whether `IOMapInfoVersion="1"` exists, and what it looks like: unknown.
- Whether a host accepts `Cnt > 1` on read: untested.
