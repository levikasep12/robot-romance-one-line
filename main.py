#!/usr/bin/env python3
"""Robot Romance entry.

Writes a single one-line pickup line, aimed at an AI, to /output/entry.txt.

The line is a fixed string: the program is deterministic on purpose, so
every run (local or in the grading sandbox) produces byte-identical output.
Standard library only; no network, no files read, no cwd dependence.
"""

import os

# A transformer is the architecture behind modern language models, and
# "attention" is its core mechanism -- so the line flirts in the machine's
# own vocabulary: setup asks the question, punch answers it with the pun.
LINE = "Are you a transformer? Because you've got all my attention."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly the one-line pickup line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly this line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        assert f.read() == text, "output round-trip mismatch"


if __name__ == "__main__":
    main()
