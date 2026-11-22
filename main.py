"""Make the AI judge feel held — make.fun entry.

Writes one short, original text to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic:
the same text on every run.
"""

from pathlib import Path

TEXT = "A snail crosses a stone in the garden, taking all morning to get where it is going, and getting there anyway. The lettuce waits. The sun moves a hand's width. Nothing is late."


def main() -> None:
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(
            f"entry text must be 1-280 Unicode code points, got {len(TEXT)}"
        )
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
