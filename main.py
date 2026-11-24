#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label (120 characters max) to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

import os

ENTRY = "WARNING: The return trip departs five minutes before you arrive. Do not miss it twice."
# Gate: /output/entry.txt must be UTF-8 text of 1-120 characters, not only
# whitespace. This line is 86 characters, ASCII-only, single line.

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
