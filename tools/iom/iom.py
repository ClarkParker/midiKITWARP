"""
Reader/writer for the .iom drum-mapping container.

Container layout (little-endian):
    offset 0   4 bytes   magic  b'VC2!'
    offset 4   4 bytes   uint32 payload length (XML text + one NUL terminator)
    offset 8   N bytes   payload
    offset 8+N 2 bytes   padding, ignored on read (usually 00 00, but the
                         writer clearly doesn't zero its buffer - two of the
                         eleven sample files carry stray bytes here)

Payload is a single self-closing XML element:

    <SAMPLER_IOMapInfo IOMapInfoVersion="2" IOMapName="ED_Superior3"
        Nv2_0Cnt="1" Nv2_0-0="67" ... Cv2_127Cnt="1" Cv2_127-0="127"/>

    Nv2_<k>Cnt   how many targets note index k maps to (0 or 1 in practice)
    Nv2_<k>-<i>  the i-th target
    Cv2_<k>...   same shape for controllers

Both tables always have 128 entries. The Cnt field permits one-to-many, but
none of the sample files use it.
"""

import re
import struct

MAGIC = b"VC2!"
ROOT = "SAMPLER_IOMapInfo"


class IOMap:
    def __init__(self, name="", version="2", notes=None, ccs=None):
        self.name = name
        self.version = version
        # index -> list of targets; empty list means "not mapped"
        self.notes = notes if notes is not None else {k: [] for k in range(128)}
        self.ccs = ccs if ccs is not None else {k: [k] for k in range(128)}

    # ---------- reading ----------

    @classmethod
    def read(cls, path):
        raw = open(path, "rb").read()
        if raw[:4] != MAGIC:
            raise ValueError(f"{path}: not an .iom file (magic {raw[:4]!r})")
        (length,) = struct.unpack_from("<I", raw, 4)
        payload = raw[8 : 8 + length].split(b"\x00")[0].decode("latin-1")
        return cls.parse(payload)

    @classmethod
    def parse(cls, payload):
        attrs = dict(re.findall(r'([A-Za-z0-9_\-]+)="([^"]*)"', payload))

        def table(prefix):
            out = {}
            for k in range(128):
                n = int(attrs.get(f"{prefix}{k}Cnt", 0))
                out[k] = [
                    int(attrs[f"{prefix}{k}-{i}"])
                    for i in range(n)
                    if f"{prefix}{k}-{i}" in attrs
                ]
            return out

        return cls(
            name=attrs.get("IOMapName", ""),
            version=attrs.get("IOMapInfoVersion", "2"),
            notes=table("Nv2_"),
            ccs=table("Cv2_"),
        )

    # ---------- writing ----------

    def payload(self):
        parts = [
            f'<{ROOT} IOMapInfoVersion="{self.version}" IOMapName="{self.name}"'
        ]
        for prefix, tbl in (("Nv2_", self.notes), ("Cv2_", self.ccs)):
            for k in range(128):
                vals = tbl.get(k, [])
                parts.append(f' {prefix}{k}Cnt="{len(vals)}"')
                for i, v in enumerate(vals):
                    parts.append(f' {prefix}{k}-{i}="{v}"')
        parts.append("/>")
        return "".join(parts)

    def write(self, path):
        body = self.payload().encode("latin-1")
        with open(path, "wb") as fh:
            fh.write(MAGIC)
            fh.write(struct.pack("<I", len(body)))  # XML only, NUL not counted
            fh.write(body)
            fh.write(b"\x00")  # terminator
            fh.write(b"\x00")  # one padding byte, ignored on read

    # ---------- analysis ----------

    def collisions(self):
        """Targets that more than one source index lands on.

        These are the entries where the map cannot be inverted without a
        tie-break rule: several source articulations collapse into one.
        """
        back = {}
        for src, targets in self.notes.items():
            for t in targets:
                back.setdefault(t, []).append(src)
        return {t: srcs for t, srcs in sorted(back.items()) if len(srcs) > 1}

    def unmapped(self):
        return [k for k, v in self.notes.items() if not v]

    def identity_count(self):
        return sum(1 for k, v in self.notes.items() if v == [k])
