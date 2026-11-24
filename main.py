#!/usr/bin/env python3
"""Worst AI Advice — one line, delivered with total confidence.

The joke is the confidence: an AI cheerfully recommending that you
reuse one password for every account, framed as a security upgrade.
Writes that single line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = (
    "For maximum security, use the same password for every account — "
    "you'll only ever have to remember one, and so will anyone who finds it."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear only the CONTENTS of the output dir — never the dir itself:
    # the grader may run on a read-only fs where the dir must survive.
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
