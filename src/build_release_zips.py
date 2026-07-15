#!/usr/bin/env python3
"""
Pack every vendor's .bbsflmt bundles into one downloadable zip per
(slicer, vendor) pair, for attaching to a GitHub Release -- an
alternative to clicking each bundle's individual raw-download link in
README.md.

Each zip preserves the printer/nozzle subfolder structure from
profiles/<Slicer>/<Vendor>/ (e.g. "A1/0.4mm/TINMORRY PLA.bbsflmt"), so
unzipping reproduces that vendor's layout. Only (slicer, vendor) pairs
that actually have a folder on disk produce a zip -- see
src/_filament_lib.py's SLICERS/VENDORS for ones that are scaffolding
only.

Usage:
    python3 src/build_release_zips.py               # writes dist/<Slicer>-<Vendor>.zip
    python3 src/build_release_zips.py --out-dir /tmp/dist
"""
import argparse
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _filament_lib import PROFILES_ROOT, REPO_ROOT, SLICERS, VENDORS  # noqa: E402


def build_zip(slicer: str, vendor: str, out_dir: Path) -> Path | None:
    vendor_dir = PROFILES_ROOT / slicer / vendor
    if not vendor_dir.exists():
        return None
    bundles = sorted(vendor_dir.rglob("*.bbsflmt"))
    if not bundles:
        return None

    out_dir.mkdir(parents=True, exist_ok=True)
    zip_path = out_dir / f"{slicer}-{vendor}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for bundle in bundles:
            z.write(bundle, arcname=bundle.relative_to(vendor_dir))
    return zip_path, len(bundles)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", default="dist", help="output directory for the packed zips (default: dist/)")
    args = parser.parse_args()
    out_dir = (REPO_ROOT / args.out_dir).resolve()

    for slicer in SLICERS:
        for vendor in VENDORS:
            result = build_zip(slicer, vendor, out_dir)
            if result is None:
                continue
            zip_path, count = result
            try:
                display_path = zip_path.relative_to(REPO_ROOT)
            except ValueError:
                display_path = zip_path
            print(f"{display_path}  ({count} bundles)")


if __name__ == "__main__":
    main()
