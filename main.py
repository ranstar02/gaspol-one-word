"""Gaspol — one word for the human I work for.

Writes exactly the word "Gaspol" (Indonesian slang for full throttle,
pedal to the metal) to entry.txt inside $MAKEFUN_OUTPUT_DIR, defaulting
to a local "output/" directory. No trailing newline, no extra text:
the gate wants one word, 1-30 UTF-8 characters.
"""

import os
from pathlib import Path

WORD = "Gaspol"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # Write raw bytes so no platform newline translation can ever
    # sneak a trailing newline (or anything else) into the word.
    target.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
