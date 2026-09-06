"""Canonical formatting for every JSON file the project hand-maintains.

    python -m tools.format            rewrite in place
    python -m tools.format --check    fail if anything is not canonical

Two dialects, per ADR-0002:

  vocabulary/*.json      block-formatted, two-space indent, terms in id order so related
                         entries stay adjacent for review
  data/devices/**.json   one note record per line inside the `notes` array, because that is
                         what makes a naive three-way merge produce ten records instead of
                         nine when two curators insert at the same position

This module is load-bearing: if it and the hand files ever disagree about canonical form,
every diff turns to noise. That is why --check runs in CI from the first commit.
"""

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDENT = 2

# Field order inside a note record. Anything not listed keeps its relative position after.
NOTE_ORDER = ["note", "channel", "pivot", "instance", "limb", "entry_kind", "vendor_label",
              "exclusion_group", "velocity_min", "velocity_max", "device_slot", "notes",
              "provenance"]


def _compact(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(", ", ": "))


def _ordered_note(entry: dict) -> dict:
    known = [k for k in NOTE_ORDER if k in entry]
    rest = [k for k in entry if k not in NOTE_ORDER]
    return {k: entry[k] for k in known + rest}


def format_vocabulary(doc: dict) -> str:
    if "terms" in doc:
        doc = dict(doc)
        doc["terms"] = dict(sorted(doc["terms"].items(), key=lambda kv: kv[1]["id"]))
    return json.dumps(doc, indent=INDENT, ensure_ascii=False) + "\n"


def format_layout(doc: dict) -> str:
    doc = dict(doc)
    notes = [_ordered_note(n) for n in doc.pop("notes", [])]
    notes.sort(key=lambda n: (n.get("channel", 10), n["note"], n.get("pivot", "")))
    head = json.dumps(doc, indent=INDENT, ensure_ascii=False)
    body = ",\n".join(f"{' ' * (INDENT * 2)}{_compact(n)}" for n in notes)
    closing = head.rfind("\n}")
    inner = head[:closing]
    return f'{inner},\n{" " * INDENT}"notes": [\n{body}\n{" " * INDENT}]\n}}\n'


def targets():
    for p in sorted((ROOT / "vocabulary").glob("*.json")):
        yield p, format_vocabulary
    for p in sorted((ROOT / "schema").glob("*.json")):
        yield p, format_vocabulary
    devices = ROOT / "data" / "devices"
    if devices.exists():
        for p in sorted(devices.rglob("*.json")):
            yield p, format_layout
    sources = ROOT / "data" / "sources.json"
    if sources.exists():
        yield sources, format_vocabulary


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report, do not rewrite")
    args = ap.parse_args()

    dirty = []
    for path, formatter in targets():
        current = path.read_text(encoding="utf-8")
        wanted = formatter(json.loads(current))
        if current == wanted:
            continue
        dirty.append(path.relative_to(ROOT))
        if not args.check:
            path.write_text(wanted, encoding="utf-8")

    if args.check and dirty:
        for p in dirty:
            print(f"not canonical: {p}", file=sys.stderr)
        print(f"\n{len(dirty)} file(s) need `python -m tools.format`", file=sys.stderr)
        return 1
    print(f"{'would rewrite' if args.check else 'rewrote'} {len(dirty)} file(s)"
          if dirty else "all files are canonical")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
