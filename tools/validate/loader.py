"""JSON loading that refuses duplicate keys.

A block-formatted JSON file merged naively after two curators inserted a record at the
same position can end up with a duplicate key. `json.loads` accepts it and keeps the last
one, and `jsonschema.validate` passes — so one curator's work vanishes with no error
anywhere. QMK's json_schema.py uses the same guard for the same reason.
"""

import json
import pathlib


def _no_duplicates(pairs):
    seen = {}
    for key, value in pairs:
        if key in seen:
            raise ValueError(f"duplicate key {key!r}")
        seen[key] = value
    return seen


def load(path: pathlib.Path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    try:
        return json.loads(text, object_pairs_hook=_no_duplicates)
    except ValueError as exc:
        raise ValueError(f"{path}: {exc}") from exc
