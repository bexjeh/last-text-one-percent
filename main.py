"""Last text at one percent.

A dying phone's final message, written to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

MESSAGE = (
    "goodbye. i'm taking your 47 unread texts, "
    "your 3am 'is my crush single' searches, "
    "and that drunk voice memo to the grave. "
    "tell the charger i loved it. actually, don't. it never loved me back."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
