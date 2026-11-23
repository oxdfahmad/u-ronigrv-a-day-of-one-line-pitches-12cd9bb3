"""One-line pitch entry: write the pitch sentence to /output/entry.txt.

The sentence is fixed and deterministic: every run writes the same bytes.
Standard library only, no network, no input, no reads outside this file.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SENTENCE = (
    "Describe your app idea in plain words and an AI agent on make.fun "
    "turns it into a real working app \u2014 no coding needed, and the "
    "only thing you risk is finding out your idea was good all along."
)


def check_sentence(text: str) -> None:
    """Gate rules: one sentence, 1-240 Unicode code points, not only whitespace."""
    if not 1 <= len(text) <= 240:
        raise ValueError(f"sentence is {len(text)} code points, gate allows 1-240")
    if not any(not c.isspace() for c in text):
        raise ValueError("sentence must contain a non-whitespace character")
    bare = text.replace("make.fun", "makefun")
    if bare.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")


def main() -> None:
    check_sentence(SENTENCE)
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SENTENCE, encoding="utf-8")
    written = out.read_text(encoding="utf-8")
    if written != SENTENCE:
        raise ValueError("written entry.txt does not match the sentence")
    print(f"wrote {out} ({len(SENTENCE)} characters)")


if __name__ == "__main__":
    main()
