"""Make the AI Judge Laugh - one office joke, one line.

Writes the entry line to the output directory (MAKEFUN_OUTPUT_DIR
or /output/entry.txt) and verifies it against the gate: UTF-8 text,
1-200 characters, not only whitespace, single line.
"""

import os
import sys

LINE = "HR said bring my whole self to work, so I brought my pillow and my job applications."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate: 1-200 chars, not whitespace-only, single line.
    if not 1 <= len(LINE) <= 200:
        sys.exit("gate failed: line is %d characters" % len(LINE))
    if not LINE.strip():
        sys.exit("gate failed: line is whitespace only")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("gate failed: line is not a single line")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back verification: byte-identical, valid UTF-8, no newline.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if text != LINE:
        sys.exit("verification failed: read-back mismatch")
    if raw.endswith(b"\n"):
        sys.exit("verification failed: trailing newline")
    print("wrote %s (%d characters, verified on read-back)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
