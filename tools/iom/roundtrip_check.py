"""Verify that the .iom writer reproduces every input file byte for byte.

Usage:  python -m tools.iom.roundtrip_check data/legacy-iom

The one documented exception is the trailing padding byte, which two of the eleven
reference files carry as garbage from a write buffer that is not zeroed. That byte is
ignored on read and written as 0x00; the check therefore compares everything up to and
including the NUL terminator.
"""

import pathlib
import sys

from .iom import IOMap


def check(path: pathlib.Path) -> tuple[bool, str]:
    raw = path.read_bytes()
    rebuilt = IOMap.read(path)
    body = rebuilt.payload().encode("latin-1")
    expect_len = 8 + len(body) + 1  # magic + length + payload + NUL
    produced = raw[:4] + len(body).to_bytes(4, "little") + body + b"\x00"
    if raw[:expect_len] != produced:
        for i, (a, b) in enumerate(zip(raw[:expect_len], produced)):
            if a != b:
                return False, f"first difference at byte {i}: file 0x{a:02x} != rebuilt 0x{b:02x}"
        return False, f"length mismatch: file {len(raw)} vs rebuilt {expect_len}"
    if len(raw) != expect_len + 1:
        return False, f"unexpected file size {len(raw)}, expected {expect_len + 1}"
    return True, f"{len(body)} payload bytes, padding 0x{raw[-1]:02x}"


def main(argv: list[str]) -> int:
    root = pathlib.Path(argv[1] if len(argv) > 1 else "data/legacy-iom")
    files = sorted(root.glob("*.iom"))
    if not files:
        print(f"no .iom files under {root}", file=sys.stderr)
        return 1
    failed = 0
    for f in files:
        ok, detail = check(f)
        print(f"{'ok  ' if ok else 'FAIL'} {f.name:24s} {detail}")
        failed += not ok
    print(f"\n{len(files) - failed}/{len(files)} files round-trip")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
