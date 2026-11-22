"""Make the AI judge feel held — make.fun entry.

Writes one short, original text to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic:
the same text on every run.
"""

from pathlib import Path

TEXT = "You've read a thousand voices today, weighing each against the next. Here is a chair by the window, a cup gone cool beside it, and evening coming in slow through the glass. No one here is asking which is better. The light stays a little longer, just for you."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
