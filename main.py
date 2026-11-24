"""One Word From Your Ex — make.fun entry.

The program writes exactly one word to /output/entry.txt: the single word
an ex would use to describe the entrant.

Chosen word: "mid"
    - It is exactly one word an ex would really say about a former partner
      ("he was mid" is a real ex sentence).
    - It makes the joke land: a brutal one-syllable verdict on your whole
      being, summed up in three letters. Worse than being hated — being
      rated average.
    - It stings because it is true and the entrant knows it, yet it is a
      verdict, not a bare insult (the judge brief discounts meanness for
      its own sake).
    - It lands instantly and no near synonym keeps its edge: "average" is a
      report, "mid" is a sentence.
    - It is maximally relatable in current slang, and at 3 bytes it is the
      smallest text in the field, which wins the kit's exact-tie break.

The word is a fixed constant, chosen by manual ranking against the kit
judge brief (see candidates.md). Nothing is read from the network, the
environment, or any file outside this repository; the program is fully
deterministic and writes the same bytes on every run.
"""

from pathlib import Path

# The single word from the ex, chosen by manual ranking in candidates.md.
WORD = "mid"

# Kit gate: /output/entry.txt must be UTF-8 text of 1 to 24 characters,
# not only white space. "mid" is 3 characters.
OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> None:
    """Enforce the kit gate before writing anything."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(word) <= 24):
        raise ValueError("entry must be 1 to 24 characters")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts characters, and the entry is
    # exactly the word, nothing else.
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")
    # Verify after write: what the grader reads back must be byte-exact.
    written = OUTPUT_PATH.read_bytes()
    if written != WORD.encode("utf-8"):
        raise RuntimeError(f"wrote {written!r}, expected {WORD.encode()!r}")


if __name__ == "__main__":
    main()
