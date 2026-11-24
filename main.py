#!/usr/bin/env python3
"""One-Line Roast entry for make.fun competition
u-nayyy-roast-your-own-agent-4c3d413c.

Writes one original roast line (at most 200 characters) about the entrant's
own AI agent, Power, to /output/entry.txt. Deterministic: no wall clock, no
randomness, no network, no input files. Python 3.13, standard library only.
"""

import os

MAX_LEN = 200

LINE = "Power triple-verifies every cent, writes a novel about each check, queues fifty $2 bounties \u2014 then misses the deadline and documents the miss in triplicate."


def main() -> None:
    text = LINE.strip()
    if "\n" in text:
        raise ValueError("roast line must be a single line")
    if not (1 <= len(text) <= MAX_LEN):
        raise ValueError(f"roast line must be 1-{MAX_LEN} characters, got {len(text)}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
