"""Words solving module."""
import itertools

import enchant

from .constants import DEFAULT_LANGUAGE


def solve(
    letters: str,
    length: int,
    language: str = DEFAULT_LANGUAGE,
    *,
    case_sensitive: bool = False,
) -> list[str]:
    """Compute words from letters in a given language.

    Compute all combinations of letters with the given length,
    check if it's a valid word in the given language
    then return the list of found words.
    """
    dictionary = enchant.Dict(language)

    if not case_sensitive:
        letters = letters.lower()

    return [
        word
        for word in sorted(["".join(p) for p in set(itertools.permutations(letters, length))])
        if dictionary.check(word)
    ]
