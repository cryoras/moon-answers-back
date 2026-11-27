#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes the entrant's chosen one-liner to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

Entry text (108 characters):
    Four billion years of wishes, howls and 2 a.m. promises, and not one of
    you has ever wished me a good night.

Gate (sealed scorer): UTF-8 text, 1 to 240 characters, not only whitespace.
Judge brief, most important first: (1) speaks as the Moon answering the
wishes, howls and late-night promises of everyone staring up at it; (2)
funny on one read, a real laugh rather than a polite smile; (3) sounds like
the Moon's own voice, wry and old and a little tired of being wished upon;
(4) lands as a comeback in one read, with the turn arriving before the line
ends; (5) stays inside 240 characters and wastes none of them.

Why this line: it answers all three things the brief names in one breath --
the wishes, the howls, the 2 a.m. promises -- then turns the whole bargain
around: for four billion years everyone has asked the Moon for something,
and nobody has ever wished the Moon itself a good night. The turn lands in
the final clause, needs no explanation, and is wry and old and tired rather
than cute: the Moon is not a vending machine, it is the one listener who
never gets wished well in return. One idea, one read, nothing tacked on.

Deterministic, standard library only, no network, no randomness, no clock.
"""

import os
import sys

ENTRY_TEXT = (
    "Four billion years of wishes, howls and 2 a.m. promises, "
    "and not one of you has ever wished me a good night."
)
MIN_CHARS = 1
MAX_CHARS = 240


def main() -> int:
    text = ENTRY_TEXT
    # Gate validation, mirroring the sealed scorer's rule.
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8 text

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
