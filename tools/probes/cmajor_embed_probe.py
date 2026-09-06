#!/usr/bin/env python3
"""Regenerate the Cmajor embedding probes behind docs/evidence/cmajor-embedding-probes.md.

Pure standard library. Writes patches and .cmajtest files into an output directory and,
when --cmaj points at a cmaj binary, runs them and prints the timing table.

    python3 tools/probes/cmajor_embed_probe.py --out /tmp/probes --cmaj /path/to/cmaj
"""
import argparse, os, random, re, subprocess, sys, time

MANIFEST = '{"CmajorVersion":1,"ID":"com.kitwarp.probe.%s","version":"0.0.1","name":"%s","category":"instrument","isInstrument":true,"source":"%s.cmajor"}'


def table_namespace(n_layouts, packed):
    n = n_layouts * 128
    random.seed(n)
    vals = [random.randrange(-1, 320) for _ in range(n)]
    if packed:
        lits = []
        for i in range(0, n, 4):
            v = 0
            for j in range(4):
                v |= (vals[i + j] & 0xFFFF) << (16 * j)
            if v >= 2 ** 63:
                v -= 2 ** 64
            lits.append("%dL" % v)
        body = ",\n".join("        " + ", ".join(lits[i:i + 8]) for i in range(0, len(lits), 8))
        decl = "const int64[%d] layoutTable = (\n%s\n    );" % (n // 4, body)
        read = "int32 unpack (int idx) { let v = int32 ((layoutTable.at (idx / 4) >> (16 * (idx % 4))) & 0xFFFFL); return v == 0xFFFF ? -1 : v; }"
        lookup = "kw::unpack (%s)"
    else:
        body = ",\n".join("        " + ", ".join(map(str, vals[i:i + 32])) for i in range(0, n, 32))
        decl = "const int32[%d] layoutTable = (\n%s\n    );" % (n, body)
        read = "int32 unpack (int idx) { return layoutTable.at (idx); }"
        lookup = "kw::unpack (%s)"
    ns = "namespace kw\n{\n    // index = layout * 128 + note, value = pivot id (-1 = unmapped)\n    %s\n\n    %s\n\n    struct SlotRow { int32 slot; int32[128] outNote; int32[128] outChan; }\n}\n" % (decl, read)
    return ns, vals, lookup


def mapper(n_layouts, packed, flat):
    ns, vals, lookup = table_namespace(n_layouts, packed)
    if flat:
        state = "    int32[32768] outNote;   // [(inCh*16 + slot)*128 + note] = note + 1, 0 = drop\n    int32[2048]  heldNote;  // [inCh*128 + note] = emitted note + 1, 0 = none\n    int32[2048]  heldChan;\n"
        init = "    void init() { rebuild(); }\n"
        rebuild_write = "for (int c = 0; c < 16; c += 1) outNote.at (c * 2048 + n) = (p >= 0) ? inverse.at (p) + 1 : 0;"
        on = "            let target = outNote.at (ch * 2048 + n);\n            if (target == 0) return;\n            heldNote.at (ch * 128 + n) = target;\n            heldChan.at (ch * 128 + n) = ch;\n            midiOut <- std::midi::createMessage (0x90 | ch, target - 1, msg.getVelocity());"
        off = "            let target = heldNote.at (ch * 128 + n);\n            if (target == 0) return;\n            heldNote.at (ch * 128 + n) = 0;\n            midiOut <- std::midi::createMessage (0x80 | heldChan.at (ch * 128 + n), target - 1, 0);"
        row = "outNote.at (s * 128 + n) = row.outNote.at (n) + 1;"
    else:
        state = "    int32[16, 16, 128] outNote;\n    int32[16, 128] heldNote;\n    int32[16, 128] heldChan;\n"
        init = ("    void init()\n    {\n        for (int c = 0; c < 16; c += 1)\n            for (int n = 0; n < 128; n += 1)\n            {\n"
                "                heldNote.at (c).at (n) = -1;\n                heldChan.at (c).at (n) = 0;\n                for (int o = 0; o < 16; o += 1)\n                    outNote.at (c).at (o).at (n) = -1;\n            }\n        rebuild();\n    }\n")
        rebuild_write = "for (int c = 0; c < 16; c += 1) outNote.at (c).at (0).at (n) = (p >= 0) ? inverse.at (p) : -1;"
        on = "            let target = outNote.at (ch).at (0).at (n);\n            if (target < 0) return;\n            heldNote.at (ch).at (n) = target;\n            heldChan.at (ch).at (n) = ch;\n            midiOut <- std::midi::createMessage (0x90 | ch, target, msg.getVelocity());"
        off = "            let target = heldNote.at (ch).at (n);\n            if (target < 0) return;\n            heldNote.at (ch).at (n) = -1;\n            midiOut <- std::midi::createMessage (0x80 | heldChan.at (ch).at (n), target, 0);"
        row = "outNote.at (0).at (s).at (n) = row.outNote.at (n);"
    src = ns + """
processor KitWarpTest
{
    input  event std::midi::Message midiIn;
    output event std::midi::Message midiOut;
    input  event kw::SlotRow slotRowIn;                       // UI -> DSP row push (struct event)
    input  event float param1 [[ name: "Src Layout", min: 0, max: %(mx)d, init: 0, step: 1 ]];
    input  event float param2 [[ name: "Tgt Layout", min: 0, max: %(mx)d, init: 1, step: 1 ]];

    int srcLayout = 0;
    int tgtLayout = 1;
%(state)s
    event param1 (float v) { srcLayout = int (v); rebuild(); }
    event param2 (float v) { tgtLayout = int (v); rebuild(); }

    event slotRowIn (kw::SlotRow row)
    {
        let s = clamp (row.slot, 0, 15);
        for (int n = 0; n < 128; n += 1)
            %(row)s
    }

    void rebuild()
    {
        int32[512] inverse;
        for (int p = 0; p < 512; p += 1) inverse.at (p) = -1;
        for (int n = 0; n < 128; n += 1)
        {
            let p = %(tgt)s;
            if (p >= 0 && inverse.at (p) < 0) inverse.at (p) = n;
        }
        for (int n = 0; n < 128; n += 1)
        {
            let p = %(src)s;
            %(rebuild_write)s
        }
    }

%(init)s
    event midiIn (std::midi::Message msg)
    {
        let ch = msg.getChannel0to15();
        if (msg.isNoteOn())
        {
            let n = msg.getNoteNumber();
%(on)s
        }
        else if (msg.isNoteOff())
        {
            let n = msg.getNoteNumber();
%(off)s
        }
        else
            midiOut <- msg;
    }

    void main() { loop { advance(); } }
}
""" % dict(mx=n_layouts - 1, state=state, row=row, tgt=lookup % "tgtLayout * 128 + n", src=lookup % "srcLayout * 128 + n",
           rebuild_write=rebuild_write, init=init, on=on, off=off)
    return src, vals


def expected(vals):
    """First source note that maps under target layouts 1 and 2 to different notes."""
    def inv(t):
        d = {}
        for n in range(128):
            p = vals[t * 128 + n]
            if p >= 0 and p not in d:
                d[p] = n
        return d
    i1, i2 = inv(1), inv(2)
    for n in range(128):
        p = vals[n]
        if p >= 0 and p in i1 and p in i2 and i1[p] != i2[p]:
            return n, i1[p], i2[p]
    raise SystemExit("no suitable test note")


def mapping_test(src_file, note, e1, e2):
    return """## global ("%s")

## testProcessor()

processor Gen
{
    output event std::midi::Message midiOut;
    output event float p2;
    void main()
    {
        advance(); advance();
        midiOut <- std::midi::createMessage (0x93, %d, 100);
        advance();
        p2 <- 2.0f;
        advance();
        midiOut <- std::midi::createMessage (0x83, %d, 0);
        advance();
        midiOut <- std::midi::createMessage (0x93, %d, 90);
        advance();
        midiOut <- std::midi::createMessage (0x83, %d, 0);
        loop advance();
    }
}

processor Check
{
    input  event std::midi::Message midiIn;
    output event int out;
    int frames = 0; int count = 0; int ok = 1;
    event midiIn (std::midi::Message m)
    {
        let ch = m.getChannel0to15();
        let nn = m.getNoteNumber();
        count += 1;
        if (count == 1) ok = ok & ((m.isNoteOn()  && nn == %d && ch == 3 && m.getVelocity() == 100) ? 1 : 0);
        if (count == 2) ok = ok & ((m.isNoteOff() && nn == %d && ch == 3) ? 1 : 0);
        if (count == 3) ok = ok & ((m.isNoteOn()  && nn == %d && ch == 3 && m.getVelocity() == 90) ? 1 : 0);
        if (count == 4) ok = ok & ((m.isNoteOff() && nn == %d && ch == 3) ? 1 : 0);
    }
    void main()
    {
        loop
        {
            frames += 1;
            if (frames == 64) { console <- "count=" <- count <- " ok=" <- ok; out <- ((count == 4) ? 1 : 0); out <- ok; out <- -1; }
            advance();
        }
    }
}

graph P [[ main ]]
{
    output event int out;
    node gen = Gen; node warp = KitWarpTest; node chk = Check;
    connection { gen.midiOut -> warp.midiIn; gen.p2 -> warp.param2; warp.midiOut -> chk.midiIn; chk.out -> out; }
}
""" % (src_file, note, note, note, note, e1, e1, e2, e2)


def state_probe(decl, n, write, read):
    return """processor KitWarpTest
{
    input  event std::midi::Message midiIn;
    output event std::midi::Message midiOut;
    %s
    int idx = 0;
    event midiIn (std::midi::Message msg)
    {
        if (msg.isNoteOn())
        {
            idx = (idx + msg.getNoteNumber()) %% %d;
            %s
            midiOut <- std::midi::createMessage (0x90, %s & 127, msg.getVelocity());
        }
    }
    void main() { loop { advance(); } }
}
""" % (decl, n, write, read)


SMOKE = """## global ("%s")

## testProcessor()

processor Gen { output event std::midi::Message midiOut; void main() { advance(); midiOut <- std::midi::createMessage (0x90, 3, 100); loop advance(); } }
processor Check
{
    input event std::midi::Message midiIn; output event int out; int frames = 0;
    event midiIn (std::midi::Message m) {}
    void main() { loop { frames += 1; if (frames == 16) { out <- 1; out <- -1; } advance(); } }
}
graph P [[ main ]] { output event int out; node gen = Gen; node warp = KitWarpTest; node chk = Check;
    connection { gen.midiOut -> warp.midiIn; warp.midiOut -> chk.midiIn; chk.out -> out; } }
"""


def run(cmaj, args, cwd):
    t = time.time()
    r = subprocess.run([cmaj] + args, cwd=cwd, capture_output=True, text=True)
    out = r.stdout + r.stderr
    err = next((l.strip() for l in out.splitlines() if "error" in l), "")
    passed = "Passed:      1" in out
    return time.time() - t, err, passed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="probes_out")
    ap.add_argument("--cmaj", help="path to the cmaj binary; omit to only generate")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rows = []

    def write(name, src):
        open(os.path.join(a.out, name + ".cmajor"), "w").write(src)
        open(os.path.join(a.out, name + ".cmajorpatch"), "w").write(MANIFEST % (name.lower(), name, name))

    # 1. const-table size sweep (generate only)
    for n, packed in ((200, False), (512, False), (520, False), (200, True), (2000, True)):
        name = "Table%d%s" % (n, "p" if packed else "")
        write(name, mapper(n, packed, flat=True)[0])
        if a.cmaj:
            dt, err, _ = run(a.cmaj, ["generate", "--target=cpp", "--output=/dev/null", name + ".cmajorpatch"], a.out)
            rows.append((name, "generate", "%.2fs" % dt, err or "OK"))

    # 2. state-array shape sweep (JIT)
    for name, decl, n, wr, rd in (
        ("StateFlat32768", "int32[32768] tbl;", 32768, "tbl.at (idx) = idx;", "tbl.at (idx)"),
        ("State3D32768", "int32[16,16,128] tbl;", 32768, "tbl.at (idx / 2048).at ((idx / 128) % 16).at (idx % 128) = idx;", "tbl.at (idx / 2048).at ((idx / 128) % 16).at (idx % 128)"),
    ):
        write(name, state_probe(decl, n, wr, rd))
        open(os.path.join(a.out, name + ".cmajtest"), "w").write(SMOKE % (name + ".cmajor"))
        if a.cmaj:
            dt, err, ok = run(a.cmaj, ["test", name + ".cmajtest"], a.out)
            rows.append((name, "test (JIT)", "%.2fs" % dt, err or ("pass" if ok else "FAIL")))

    # 3. full mapper, 3-D vs flat, with the functional test
    for name, flat, n, packed in (("Mapper3D", False, 200, False), ("MapperFlat", True, 200, False), ("MapperFlatBig", True, 2000, True)):
        src, vals = mapper(n, packed, flat)
        write(name, src)
        note, e1, e2 = expected(vals)
        open(os.path.join(a.out, name + ".cmajtest"), "w").write(mapping_test(name + ".cmajor", note, e1, e2))
        if a.cmaj:
            dt, err, ok = run(a.cmaj, ["test", name + ".cmajtest"], a.out)
            rows.append((name, "test (JIT+functional)", "%.2fs" % dt, err or ("pass" if ok else "FAIL")))

    if rows:
        w = max(len(r[0]) for r in rows)
        for r in rows:
            print("%-*s  %-22s %8s  %s" % (w, r[0], r[1], r[2], r[3][:120]))
    else:
        print("generated into", a.out)


if __name__ == "__main__":
    main()
