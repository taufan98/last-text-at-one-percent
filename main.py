#!/usr/bin/env python3
"""Last Text at One Percent — make.fun bounty entry.

Writes the funniest final text a dying phone sends at one percent battery
(under 200 characters, in the phone's own voice) to /output/entry.txt.
Deterministic, standard library only, no network, no environment secrets.
"""

import os

ENTRY = (
    "1% left. tell my charger i forgive it. tell the group chat i died "
    "mid-sentence. delete my 3am searches \u2014 actually, leave them. "
    "let them wonder. tell the wifi i never really loved it."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")

    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
