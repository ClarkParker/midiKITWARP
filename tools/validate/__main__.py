"""Run every cross-file invariant. Exit non-zero on the first failing class.

    python -m tools.validate
"""

import json
import pathlib
import sys

from .loader import load

ROOT = pathlib.Path(__file__).resolve().parents[2]
VOCAB = ROOT / "vocabulary"
DEVICES = ROOT / "data" / "devices"
BASELINE = ROOT / "vocabulary" / "baseline.json"

SHIPPABLE = {"ingest-free", "ingest-attribute", "ingest-restricted"}
ORDERED_AXES = {"openness", "damping", "dynamic"}


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks = 0

    def check(self, name, ok, detail=""):
        self.checks += 1
        if not ok:
            self.errors.append(f"{name}: {detail}")
        return ok

    def error(self, name, detail):
        self.errors.append(f"{name}: {detail}")

    def warn(self, name, detail):
        self.warnings.append(f"{name}: {detail}")


def axis_values(axes):
    return {name: {v["slug"]: v for v in spec["values"]}
            for name, spec in axes["axes"].items()}


def check_axes(axes, rep):
    for name, spec in axes["axes"].items():
        ids = [v["id"] for v in spec["values"]]
        slugs = [v["slug"] for v in spec["values"]]
        rep.check(f"axis {name}: ids unique", len(ids) == len(set(ids)),
                  f"{len(ids) - len(set(ids))} duplicate id(s)")
        rep.check(f"axis {name}: slugs unique", len(slugs) == len(set(slugs)),
                  f"{len(slugs) - len(set(slugs))} duplicate slug(s)")
    scalars = [v["scalar"] for v in axes["axes"]["openness"]["values"]]
    rep.check("openness: ids follow scalar order",
              scalars == sorted(scalars),
              "ids must be assigned in increasing scalar order so 'nearest' is well defined")
    ctl = [c["slug"] for c in axes["controllers"]]
    rep.check("controllers: slugs unique", len(ctl) == len(set(ctl)), "duplicate controller slug")


def check_terms(pivot, values, rep):
    terms = pivot["terms"]
    ids = [t["id"] for t in terms.values()]
    rep.check("terms: ids unique", len(ids) == len(set(ids)),
              f"{len(ids) - len(set(ids))} duplicate id(s)")
    rep.check("terms: next_id is above every assigned id",
              pivot["next_id"] > max(ids), "next_id would re-issue an existing id")
    rep.check("terms: no id in private extension space",
              all(i < 1_000_000 for i in ids), "ids >= 1000000 are reserved for third parties")

    names = set()
    for slug, t in terms.items():
        for candidate in [slug] + [a["value"] for a in t.get("aliases", [])]:
            if candidate in names:
                rep.error("terms: slug/alias collision",
                          f"{candidate!r} is used more than once across slugs and aliases")
            names.add(candidate)

        for axis, value in t["axes"].items():
            if axis not in values:
                rep.error("terms: unknown axis", f"{slug}: {axis!r}")
            elif value not in values[axis]:
                rep.error("terms: unregistered axis value", f"{slug}: {axis}={value!r}")

        if t["status"] != "active":
            if "deprecated_in" not in t or "deprecation_reason" not in t:
                rep.error("terms: incomplete deprecation",
                          f"{slug} is {t['status']} without deprecated_in/deprecation_reason")
            kind = t.get("supersession_kind")
            targets = t.get("superseded_by", [])
            if kind in {"same-as", "replaced-by", "merged-into"} and len(targets) != 1:
                rep.error("terms: supersession arity",
                          f"{slug}: {kind} needs exactly one superseded_by, got {len(targets)}")
            if t.get("deprecation_reason") == "split":
                if kind != "split-into" or len(targets) < 2:
                    rep.error("terms: split shape",
                              f"{slug}: a split needs supersession_kind=split-into and >= 2 targets")

    by_id = {t["id"]: slug for slug, t in terms.items()}
    for slug, t in terms.items():
        for target in t.get("superseded_by", []):
            if target not in by_id:
                rep.error("terms: dangling supersession", f"{slug} -> id {target}")
            elif terms[by_id[target]]["status"] == "withdrawn":
                rep.error("terms: supersedes a withdrawn term", f"{slug} -> {by_id[target]}")

    # parent chains: exist, and terminate
    for slug, t in terms.items():
        seen, cur = set(), slug
        while cur is not None:
            if cur in seen:
                rep.error("terms: parent cycle", " -> ".join(list(seen) + [cur]))
                break
            seen.add(cur)
            parent = terms.get(cur, {}).get("parent")
            if parent is not None and parent not in terms:
                rep.error("terms: dangling parent", f"{cur} -> {parent!r}")
                break
            cur = parent
    rep.checks += 4


def check_rules(rules, pivot, values, rep):
    terms = pivot["terms"]
    for rule in rules["axis_degradation"]:
        axis = rule["axis"]
        if axis not in values and axis != "limb":
            rep.error("rules: unknown axis", axis)
            continue
        known = values.get(axis, {})
        if rule["from"] != "*" and known and rule["from"] not in known:
            rep.error("rules: unknown source value", f"{axis}={rule['from']!r}")
        to = rule["to"]
        if to not in (None, "nearest") and known and to not in known:
            rep.error("rules: unknown target value", f"{axis}={to!r}")
        if to == "nearest" and axis not in ORDERED_AXES:
            rep.error("rules: 'nearest' on an unordered axis",
                      f"{axis} has no defined order, so 'nearest' is meaningless")

    for src, edges in rules["curated"].items():
        if src not in terms:
            rep.error("rules: curated edge from unknown term", src)
        for edge in edges:
            if edge["to"] not in terms:
                rep.error("rules: curated edge to unknown term", f"{src} -> {edge['to']}")

    for src, alternatives in rules["expansions"].items():
        if src not in terms:
            rep.error("rules: expansion from unknown term", src)
        for alt in alternatives:
            for part in alt["parts"]:
                if part["to"] not in terms:
                    rep.error("rules: expansion to unknown term", f"{src} -> {part['to']}")

    # Mutual curated edges are legitimate and expected: "if the target has no ride bell use
    # the cowbell" and "if it has no cowbell use the ride bell" are both good rules, and only
    # one of them can ever fire for a given target. The resolver therefore walks with a
    # visited set, exactly as marty-615/drum-remap's resolveTag does. Cycles are reported so
    # they stay visible, but they are not an error.
    graph = {s: [e["to"] for e in edges] for s, edges in rules["curated"].items()}
    colour: dict[str, int] = {}

    def visit(node, path):
        if colour.get(node) == 2:
            return
        if colour.get(node) == 1:
            rep.warn("rules: mutual curated edges",
                     " -> ".join(path + [node]) + " (resolver walks with a visited set)")
            return
        colour[node] = 1
        for nxt in graph.get(node, []):
            visit(nxt, path + [node])
        colour[node] = 2

    for node in graph:
        visit(node, [])

    # Totality is the invariant that actually matters: a term with no route out cannot
    # degrade at all, so on a target that lacks it the note is simply dropped.
    degradable = {r["axis"] for r in rules["axis_degradation"]}
    roots = {r["term"] for r in rules.get("roots", [])}
    for r in rules.get("roots", []):
        if r["term"] not in terms:
            rep.error("rules: root names an unknown term", r["term"])
    for slug, term in terms.items():
        if slug in roots or term.get("parent") or slug in rules["curated"] or slug in rules["expansions"]:
            continue
        if any(axis in degradable for axis in term["axes"] if axis != "instrument"):
            continue
        rep.warn("rules: no fallback route",
                 f"{slug} has no parent, no curated edge and no degradable axis; on a target "
                 f"that lacks it the note is dropped")
    rep.checks += 5


def check_layouts(pivot, axes, rep, devices=DEVICES):
    terms = pivot["terms"]
    controllers = {c["slug"] for c in axes["controllers"]}
    sources_path = ROOT / "data" / "sources.json"
    sources = load(sources_path)["sources"] if sources_path.exists() else {}

    layouts = sorted(devices.rglob("*.json")) if devices.exists() else []
    for path in layouts:
        layout = load(path)
        rel = path.relative_to(ROOT) if ROOT in path.parents else path.name
        seen_canonical = {}
        for entry in layout["notes"]:
            if entry["entry_kind"] == "non-sound":
                continue
            slug = entry["pivot"]
            term = terms.get(slug)
            if term is None:
                rep.error("layout: unknown pivot term", f"{rel} note {entry['note']} -> {slug!r}")
                continue
            if term["status"] != "active":
                rep.error("layout: references a non-active term",
                          f"{rel} note {entry['note']} -> {slug} is {term['status']}")
            if entry["entry_kind"] == "canonical":
                key = (entry.get("channel", 10), entry["note"])
                if key in seen_canonical:
                    rep.error("layout: two canonical slots on one note",
                              f"{rel} note {entry['note']} claimed by {seen_canonical[key]} and {slug}")
                seen_canonical[key] = slug
            if not any(p["licence_verdict"] in SHIPPABLE for p in entry["provenance"]):
                rep.error("layout: nothing shippable",
                          f"{rel} note {entry['note']}: no provenance record permits shipping")
            for prov in entry["provenance"]:
                sid = prov["source_id"]
                if sources and sid not in sources:
                    rep.error("layout: unknown source_id", f"{rel} note {entry['note']} -> {sid}")
                elif sources and sources[sid]["licence_verdict"] == "forbidden":
                    rep.error("layout: forbidden source used", f"{rel} -> {sid}")
        for ctl in layout.get("controllers", []):
            if ctl["controller"] not in controllers:
                rep.error("layout: unknown controller", f"{rel} -> {ctl['controller']}")
            if ctl["carrier"] == "cc" and "number" not in ctl:
                rep.error("layout: cc controller without a number", f"{rel} -> {ctl['controller']}")
            if ctl["carrier"] in {"cc", "aftertouch"} and ("min" not in ctl or "max" not in ctl):
                rep.warn("layout: controller without a range",
                         f"{rel} -> {ctl['controller']}: without min/max a 0-90 device driving a "
                         f"0-127 target never reaches the end of its travel")
    rep.checks += 1
    return len(layouts)


def check_immutability(pivot, rep):
    """Published ids and slugs are frozen. This is the highest-value check here."""
    if not BASELINE.exists():
        rep.warn("immutability", "no vocabulary/baseline.json yet; nothing is frozen. "
                                 "Create it at the first release.")
        return
    base = load(BASELINE)["terms"]
    now = pivot["terms"]
    for slug, entry in base.items():
        if slug not in now:
            rep.error("immutability: term removed", f"{slug} (id {entry['id']}) is gone")
        elif now[slug]["id"] != entry["id"]:
            rep.error("immutability: id changed",
                      f"{slug}: {entry['id']} -> {now[slug]['id']}")
    by_id_base = {e["id"]: s for s, e in base.items()}
    for slug, entry in now.items():
        other = by_id_base.get(entry["id"])
        if other is not None and other != slug:
            rep.error("immutability: id reused",
                      f"id {entry['id']} was {other}, is now {slug}")
    rep.checks += 1


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--devices", type=pathlib.Path, default=DEVICES,
                    help="directory of device layouts to check (default data/devices)")
    args = ap.parse_args(argv)

    rep = Report()
    axes = load(VOCAB / "axes.json")
    pivot = load(VOCAB / "pivot.json")
    rules = load(VOCAB / "rules.json")

    for name, doc in (("axes", axes), ("pivot", pivot), ("rules", rules)):
        rep.check(f"{name}: version agrees with axes.json",
                  doc["vocabulary_version"] == axes["vocabulary_version"],
                  f"{doc['vocabulary_version']} != {axes['vocabulary_version']}")
        rep.check(f"{name}: serial agrees with axes.json",
                  doc["vocabulary_serial"] == axes["vocabulary_serial"], "serial mismatch")

    values = axis_values(axes)
    check_axes(axes, rep)
    check_terms(pivot, values, rep)
    check_rules(rules, pivot, values, rep)
    layouts = check_layouts(pivot, axes, rep, args.devices)
    check_immutability(pivot, rep)

    print(f"vocabulary {pivot['vocabulary_version']} serial {pivot['vocabulary_serial']}: "
          f"{len(pivot['terms'])} terms, "
          f"{sum(len(a['values']) for a in axes['axes'].values())} axis values across "
          f"{len(axes['axes'])} axes, {layouts} device layout(s)")
    for w in rep.warnings:
        print(f"  warning  {w}")
    for e in rep.errors:
        print(f"  ERROR    {e}", file=sys.stderr)
    if rep.errors:
        print(f"\n{len(rep.errors)} error(s)", file=sys.stderr)
        return 1
    print(f"  {rep.checks} check groups passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
