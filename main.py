"""One-Line Slogan for a Solana Wallet Agent.

Writes a single slogan to /output/entry.txt (or to the directory named by
the MAKEFUN_OUTPUT_DIR environment variable, which defaults to /output).

The slogan was picked from three hand-written candidates for the judge's
brief: it must name the Solana wallet, turn a fresh image instead of a
stock crypto line, read clearly to a newcomer, stick in the ear, and stay
honest about what a wallet agent does.

Chosen slogan (84 characters, 16 words):

    Your Solana wallet, with a brain that never sleeps and hands that
    never drop a coin.
"""

import os
import sys

# The chosen slogan: a wallet agent is a mind that watches the chain
# around the clock and hands that handle the coins, so the owner rests.
SLOGAN = (
    "Your Solana wallet, with a brain that never sleeps "
    "and hands that never drop a coin."
)

MAX_CHARS = 140
MAX_WORDS = 20


def validate_slogan(text):
    """Check the slogan against the competition's caps.

    Returns (char_count, word_count). Raises ValueError on any breach so
    a bad slogan can never reach the output file.
    """
    if not text or not text.strip():
        raise ValueError("slogan must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("slogan must be a single line")
    # The gate reads the file as UTF-8, so refuse anything unencodable here.
    text.encode("utf-8")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "slogan is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "slogan has %d words, over the %d limit"
            % (len(words), MAX_WORDS)
        )
    return len(text), len(words)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    char_count, word_count = validate_slogan(SLOGAN)

    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SLOGAN + "\n")
    os.chmod(entry_path, 0o644)

    print("Wrote %s (%d chars, %d words)" % (entry_path, char_count, word_count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
