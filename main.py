#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one original line, an alien tourist's review of planet Earth,
to /output/entry.txt. The line is a fixed, hand-written string; the
program's only job is to deliver it exactly as written.
"""

import os

ENTRY = (
    "Earth: two days in, a goose has claimed my ship, "
    "three locals asked me for directions, and the snacks are unreal. "
    "4/5 \u2014 would invade again."
)


def main():
    # The bounty gate: 1 to 200 characters, not only white space.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry is only white space"
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {out}")


if __name__ == "__main__":
    main()
