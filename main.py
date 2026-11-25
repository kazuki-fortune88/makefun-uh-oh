#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word: Dunno.exe — the sound of an agent caught out mid-task,
confessing it has no idea what to do, in the voice of a machine:
a casual "dunno" wearing an executable's name tag.

Writes exactly one word (9 characters, no trailing newline) to
/output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when set.
"""

import os

WORD = "Dunno.exe"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
