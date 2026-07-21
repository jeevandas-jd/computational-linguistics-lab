"""
eliza.py
--------
The ELIZA engine. This file contains NO domain knowledge - no mentions of
"exam", "stress", "teacher", etc. All of that lives in responses.py.
This file only knows HOW to:
    1. reflect pronouns in captured text          -> reflect()
    2. find the first matching rule and respond    -> respond()
    3. run the read-eval-print chat loop           -> main()

This mirrors classic ELIZA architecture (Weizenbaum, 1966): a small,
domain-agnostic pattern-matching engine driven by a swappable "script"
(here, responses.py) that defines the personality/topic.
"""

import random
import re

from response import (
    REFLECTIONS,
    PATTERNS,
    DEFAULT_RESPONSES,
    OPENING_LINE,
    FAREWELL_RESPONSES,
    EXIT_WORDS,
)


def reflect(fragment: str) -> str:
    """
    Swap pronouns/person in a captured text fragment so ELIZA doesn't just
    parrot the user back. e.g. "tired" stays "tired", but "my exam" ->
    "your exam", "i am" -> "you are".

    Uses a regex word-boundary substitution rather than naive str.split()
    so punctuation attached to a word (e.g. "tired.") doesn't stop the
    word from being matched.
    """
    def swap(match: re.Match) -> str:
        word = match.group(0)
        return REFLECTIONS.get(word.lower(), word)

    # \b\w+'?\w* matches words and simple contractions like "i'm", "you've"
    return re.sub(r"\b[\w']+\b", swap, fragment)


def respond(user_input: str) -> str:
    """
    Walk PATTERNS top-to-bottom and return the first matching response.
    Rules with a capturing group get their captured text reflected and
    substituted into the chosen template via str.format(). Rules without
    a capturing group just pick a template as-is.
    Falls back to a random DEFAULT_RESPONSES entry if nothing matches.
    """
    text = user_input.strip()

    for pattern, templates in PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            continue

        template = random.choice(templates)

        if "{0}" in template:
            # This template needs captured text (group 1) to fill in.
            # Some keyword patterns have incidental optional groups (e.g.
            # "teacher(s)?") that aren't meant for this, so we only treat
            # group(1) as real capture when the template actually asks for it.
            if not match.groups() or not match.group(1):
                continue
            fragment = match.group(1).strip().rstrip(".!?")
            reflected = reflect(fragment)
            return template.format(reflected)

        return template

    return random.choice(DEFAULT_RESPONSES)


def is_exit(user_input: str) -> bool:
    """Check the whole line (not a substring) against known exit words."""
    return user_input.strip().lower() in EXIT_WORDS


def main():
    print(OPENING_LINE)

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nELIZA:", random.choice(FAREWELL_RESPONSES))
            break

        if not user_input.strip():
            print("ELIZA: I'm listening. Go on.")
            continue

        if is_exit(user_input):
            print("ELIZA:", random.choice(FAREWELL_RESPONSES))
            break

        print("ELIZA:", respond(user_input))


if __name__ == "__main__":
    main()