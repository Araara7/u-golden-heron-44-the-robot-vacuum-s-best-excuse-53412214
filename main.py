"""The Robot Vacuum's Best Excuse.

Writes one line, at most 140 characters: the funniest excuse a robot
vacuum gives for missing a spot. Deterministic, stdlib only.

The joke: the vacuum's own sensors did their job twice and reached the
wrong conclusion with total confidence -- the dust is a pet, so leaving
it alone is the polite thing to do. The punch lands on the last words,
and the line stays in the vacuum's own voice throughout.
"""

import os

ENTRY = (
    "I didn't miss that spot. My sensors scanned it twice and "
    "classified the dust as a pet, so I left it alone."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
