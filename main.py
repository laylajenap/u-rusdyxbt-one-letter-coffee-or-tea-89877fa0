#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry "A" (coffee).

Writes exactly one byte, "A", to /output/entry.txt, with no trailing
newline. Deterministic: every run produces the same single byte.

Why "A": coffee is the bolder, more vivid of the two drinks -- a full,
alive answer in a single letter -- so it is the entry's pick.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(b"A")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
