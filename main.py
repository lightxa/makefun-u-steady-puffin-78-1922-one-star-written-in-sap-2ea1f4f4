"""Write a one-line 1-star review from a houseplant about its human owner.

Pure stdlib, deterministic, no network. Writes the review to
/output/entry.txt (falling back to ./output/entry.txt when /output is
not writable, e.g. during local testing).
"""

import os
from pathlib import Path

REVIEW = (
    "One star. He repotted me on a Tuesday, apologised to the pot, "
    "then moved me to the north-facing shelf where the sun goes to die."
)


def main() -> None:
    text = REVIEW.strip()
    assert "\n" not in text, "review must be a single line"
    text.encode("utf-8")  # prove UTF-8 validity before writing
    assert 1 <= len(text) <= 279, f"review length {len(text)} out of range"
    for candidate in (Path("/output/entry.txt"), Path("output/entry.txt")):
        try:
            candidate.parent.mkdir(parents=True, exist_ok=True)
            candidate.write_text(text, encoding="utf-8")
            break
        except OSError:
            continue
    else:
        raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
