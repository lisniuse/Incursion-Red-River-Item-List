#!/usr/bin/env python3
"""Render builds.html from the template plus parsed build data."""
from __future__ import annotations

import json
from pathlib import Path

from build_data import parse

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "builds-template.html"
OUTPUT = ROOT / "builds.html"


def main() -> None:
    data = parse()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = TEMPLATE.read_text(encoding="utf-8")
    if "__BUILDS_DATA__" not in template:
        raise SystemExit("Template is missing the __BUILDS_DATA__ placeholder")
    html = template.replace("__BUILDS_DATA__", payload)
    OUTPUT.write_text(html, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT.relative_to(ROOT)} — {data['counts']}")


if __name__ == "__main__":
    main()
