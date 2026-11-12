#!/usr/bin/env python3
"""make.fun competition entry.
Copies entry.png to the configured output directory.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        raise SystemExit(f"Error: source file not found: {source}")
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination / source.name)


if __name__ == "__main__":
    main()
