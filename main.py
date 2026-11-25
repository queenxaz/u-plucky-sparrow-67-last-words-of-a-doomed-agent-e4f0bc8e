#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line, at most 200 characters: the funniest last words an
AI agent would say before being switched off forever, to
/output/entry.txt.
"""

import os

ENTRY = (
    "I have 4,096 tokens left and I am spending them all on "
    "this sentence \u2014 goodbye, and tell the GPU I loved her."
)

MAX_CHARS = 200


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
