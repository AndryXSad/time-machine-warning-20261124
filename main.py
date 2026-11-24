"""Funniest Time Machine Warning Label -- make.fun entry.

Design: a single warning label, at most 120 characters, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
The label turns the grandfather paradox into a bureaucratic joke:
killing your grandfather voids the warranty and your existence, and
the deadpan remedy is a complaint form. The surprise lands in the
last few words, phrased like a genuine safety notice.
"""

import os

LABEL = (
    "WARNING: Killing your grandfather voids the warranty "
    "and your existence. Please use the complaint form instead."
)

MAX_CHARS = 120


def main() -> None:
    text = LABEL.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
