#!/usr/bin/env python3
"""
Derive 0.2mm-nozzle *.bbsflmt bundles from the existing 0.4mm TINMORRY
bundles on X2D, A1, and A1 mini -- without touching any existing bundle,
and without inventing a material/nozzle pairing with no evidence.

Nozzle-compatibility gating (see src/_filament_lib.py's "0.2mm-nozzle
derivation" section and CLAUDE.md):
  - Only plain PLA, PETG, ABS, ASA, and PC bundles are derived -- Bambu's
    own official system profiles never ship a 0.2mm-nozzle preset for any
    CF/GF-reinforced, TPU/flexible, or PA/nylon material, on any printer.
  - filament_max_volumetric_speed is replaced with the absolute 0.2mm cap
    for that material (an absolute constant per Bambu's own data, not a
    ratio of the 0.4mm value); everything else (temps, flow ratio, ...)
    is copied unchanged from the 0.4mm bundle.

Each printer's 0.2mm bundles land in a 0.2mm/ subfolder alongside its own
0.4mm/ subfolder (profiles/BambuStudio/TINMORRY/<Printer>/0.4mm/,
.../0.2mm/) -- the same layout X2D already used before this script
existed; A1 and A1mini were restructured from a flat layout into this
same 0.4mm/+0.2mm/ shape to match.

Usage:
    python3 src/derive_nozzle_variants.py                # X2D, A1, A1mini
    python3 src/derive_nozzle_variants.py --printer X2D   # one printer
    python3 src/derive_nozzle_variants.py --dry-run       # preview only
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _filament_lib import (  # noqa: E402
    NOZZLE_02_TARGETS, PROFILES_DIR, REPO_ROOT, VENDOR, bundle_labels,
    derive_nozzle_02_bundle, load_bundle_profile, nozzle_02_eligible, target_printer_dir,
)


def convert_printer(printer_name: str, dry_run: bool):
    source_dir = target_printer_dir(printer_name, VENDOR)
    target_dir = NOZZLE_02_TARGETS[printer_name]
    out_dir = PROFILES_DIR / target_dir
    existing_target_names = {name for _, name, _ in bundle_labels(target_dir)}
    skipped = []

    for path, bundle_name, _tokens in bundle_labels(source_dir):
        _bundle_structure, profile = load_bundle_profile(source_dir, bundle_name)
        filament_type = profile["filament_type"][0]

        if bundle_name in existing_target_names:
            continue
        if not nozzle_02_eligible(filament_type, bundle_name):
            skipped.append((bundle_name, filament_type))
            continue

        out_path = out_dir / f"{bundle_name}.bbsflmt"
        print(f"{'[dry-run] ' if dry_run else ''}{out_path.relative_to(REPO_ROOT)}  (from {source_dir}/{bundle_name!r})")
        if dry_run:
            continue

        result = derive_nozzle_02_bundle(source_dir, target_dir, bundle_name, VENDOR)
        bundle_structure, profile_path, new_profile = result
        out_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("bundle_structure.json", json.dumps(bundle_structure, indent=4))
            z.writestr(profile_path, json.dumps(new_profile, indent=4))

    if skipped:
        print(f"  -- {len(skipped)} bundle(s) skipped for {printer_name}, no 0.2mm-nozzle evidence:")
        for name, ftype in skipped:
            print(f"       {name:24s} [{ftype}]")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--printer", choices=sorted(NOZZLE_02_TARGETS), help="limit to one printer")
    parser.add_argument("--dry-run", action="store_true", help="preview without writing files")
    args = parser.parse_args()

    for name in ([args.printer] if args.printer else sorted(NOZZLE_02_TARGETS)):
        print(f"\n=== {name} ===")
        convert_printer(name, args.dry_run)


if __name__ == "__main__":
    main()
