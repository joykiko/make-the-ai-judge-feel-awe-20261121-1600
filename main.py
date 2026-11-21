#!/usr/bin/env python3
"""Make the AI judge feel awe: write one short text to /output/entry.txt.

Anchor: makefun anchor 5a1bc622ff47c98c688544694f7919b537963b4b round 34158852
"""

import os
from pathlib import Path

TEXT = (
    "The lake lay still under the stars, and the stars lay still in the "
    "lake, and for a long while nothing moved at all. Somewhere far below "
    "the surface, the dark water kept holding the light, patient as stone, "
    "and the night went on being wide enough for all of it."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 char gate")
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
