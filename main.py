"""Describe Your Ex in One Word.

Writes exactly one word to /output/entry.txt: "Unsubscribe".

Why this word: an ex is someone you unsubscribe from. It is instantly
readable as a verdict on a former partner, lands as a joke at a glance
(the breakup as opting out of a mailing list), surprises instead of
reaching for the obvious insult, and anyone who has ever hit
"unsubscribe" recognises the feeling at once.
"""

import os

WORD = "Unsubscribe"


def main() -> None:
    # Validation guard: exactly one word, 1-111 chars, no whitespace.
    assert 1 <= len(WORD) <= 111, "word must be 1-111 characters"
    assert WORD.split() == [WORD], "entry must be exactly one word"
    assert WORD.strip() == WORD, "entry must not have surrounding whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
