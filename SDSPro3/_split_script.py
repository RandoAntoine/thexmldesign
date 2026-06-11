#!/usr/bin/env python3
import os, re, copy, sys, json
from lxml import etree

SRC = "/tmp/SDS_Pro3.xml"
OUT = "/tmp/SDS_Pro3"          # output root (becomes the repo subfolder)
NS  = "http://www.lotus.com/dxl"
DOCTYPE = "<!DOCTYPE database SYSTEM 'xmlschemas/domino_11_0_1.dtd'>"

# tag (local) -> category subfolder
CAT = {
    "form": "forms",
    "subform": "subforms",
    "view": "views",
    "folder": "folders",
    "agent": "agents",
    "scriptlibrary": "libraries",
    "sharedfield": "sharedfields",
    "page": "pages",
    "outline": "outlines",
    "frameset": "framesets",
    "imageresource": "resources",
    "fileresource": "resources",
    "stylesheetresource": "resources",
    "javaresource": "resources",
    "databasescript": "dbscript",
    "note": "rawnotes",
    # db-level metadata (not design notes)
    "databaseinfo": "_meta",
    "fulltextsettings": "_meta",
    "launchsettings": "_meta",
    "acl": "_meta",
}

ILLEGAL = re.compile(r'[<>:"/\\|?*\x00-\x1f]')

def sanitize(seg):
    seg = ILLEGAL.sub("_", seg).strip().strip(".")
    return seg or "_unnamed"

def local(tag):
    return tag.split("}")[-1] if "}" in tag else tag

def name_for(el):
    lt = local(el.tag)
    nm = el.get("name")
    if nm:
        # take primary name before alias separator '|'
        nm = nm.split("|")[0]
        return nm
    if lt == "note":
        cls = el.get("class", "note")
        # try to grab noteid for uniqueness
        ni = el.find("{%s}noteinfo" % NS)
        nid = ni.get("noteid") if ni is not None else "x"
        return "%s_%s" % (cls, nid)
    return lt

def rel_path(el):
    """Return (subdirs_list, filename_stem) honoring Notes '\\' cascade."""
    raw = name_for(el)
    parts = re.split(r"[\\]", raw)        # cascade hierarchy
    parts = [sanitize(p) for p in parts if p != ""]
    if not parts:
        parts = ["_unnamed"]
    return parts[:-1], parts[-1]

def main():
    print("Parsing %s ..." % SRC)
    tree = etree.parse(SRC)
    root = tree.getroot()
    root_attribs = dict(root.attrib)
    children = list(root)
    print("Top-level children: %d" % len(children))

    used = {}      # full path -> count (collision handling)
    manifest = []  # rows for README
    counts = {}
    bundle = {}    # local_tag -> list of elements to bundle into one file

    # tags that get bundled into a single file rather than one-per-element
    BUNDLE_TAGS = {"agentdata": "_data"}

    for el in children:
        lt = local(el.tag)
        if isinstance(el, etree._Comment) or isinstance(el, etree._ProcessingInstruction):
            continue

        if lt in BUNDLE_TAGS:
            bundle.setdefault(lt, []).append(el)
            continue

        cat = CAT.get(lt, "_other")
        counts[cat] = counts.get(cat, 0) + 1
        subdirs, stem = rel_path(el)

        dir_path = os.path.join(OUT, cat, *subdirs)
        os.makedirs(dir_path, exist_ok=True)
        base = os.path.join(dir_path, stem + ".dxl")

        # collision handling
        key = base.lower()
        if key in used:
            used[key] += 1
            base = os.path.join(dir_path, "%s__%d.dxl" % (stem, used[key]))
        else:
            used[key] = 1

        # build standalone DXL envelope
        new_root = etree.Element("{%s}database" % NS, nsmap={None: NS})
        for k, v in root_attribs.items():
            new_root.set(k, v)
        new_root.append(copy.deepcopy(el))
        xml_bytes = etree.tostring(
            new_root, xml_declaration=True, encoding="utf-8",
            doctype=DOCTYPE, pretty_print=False
        )
        with open(base, "wb") as f:
            f.write(xml_bytes)

        rel = os.path.relpath(base, OUT)
        manifest.append((cat, name_for(el), rel, len(xml_bytes)))

    # write bundled tags (e.g. agentdata) into a single wrapped DXL file each
    for lt, els in bundle.items():
        cat = BUNDLE_TAGS[lt]
        os.makedirs(os.path.join(OUT, cat), exist_ok=True)
        new_root = etree.Element("{%s}database" % NS, nsmap={None: NS})
        for k, v in root_attribs.items():
            new_root.set(k, v)
        for el in els:
            new_root.append(copy.deepcopy(el))
        xml_bytes = etree.tostring(new_root, xml_declaration=True,
                                   encoding="utf-8", doctype=DOCTYPE)
        bpath = os.path.join(OUT, cat, lt + ".dxl")
        with open(bpath, "wb") as f:
            f.write(xml_bytes)
        counts[cat] = counts.get(cat, 0) + 1
        manifest.append((cat, "%s (%d notes bundled)" % (lt, len(els)),
                         os.path.relpath(bpath, OUT), len(xml_bytes)))

    # write manifest / README
    manifest.sort(key=lambda r: (r[0], r[1].lower()))
    lines = []
    lines.append("# SDS_Pro3 — split DXL design elements\n")
    lines.append("Source: `SDS_Pro3.xml` (full-database DXL export, %d bytes).\n" % os.path.getsize(SRC))
    lines.append("Each file below is a **standalone, valid DXL fragment**: the original ")
    lines.append("`<database>` root attributes are preserved and a single design element ")
    lines.append("is wrapped inside, so any file can be re-imported into Domino Designer on its own.\n")
    lines.append("\n## Element counts by category\n")
    for c in sorted(counts):
        lines.append("- **%s/** — %d\n" % (c, counts[c]))
    lines.append("\n## Full manifest\n")
    lines.append("| Category | Element name | File | Bytes |\n")
    lines.append("|---|---|---|---|\n")
    for cat, nm, rel, sz in manifest:
        nm_esc = nm.replace("|", "\\|")
        rel_esc = rel.replace("\\", "/")
        lines.append("| %s | `%s` | `%s` | %d |\n" % (cat, nm_esc, rel_esc, sz))
    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as f:
        f.write("".join(lines))

    print("\n=== counts by category ===")
    for c in sorted(counts):
        print("  %-14s %d" % (c, counts[c]))
    print("Total files written: %d" % len(manifest))

if __name__ == "__main__":
    main()
