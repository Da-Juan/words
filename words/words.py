import itertools

import click

import enchant

from .constants import DEFAULT_LANGUAGE


def solve(
    letters: str,
    length: int,
    language: str = DEFAULT_LANGUAGE,
    case_sensitive: bool = False,
) -> list[str]:
    """
    Compute words from letters in a given language.

    Compute all combinations of letters with the given length,
    check if it's a valid word in the given language
    then return the list of found words.
    """

    dictionary = enchant.Dict(language)
    words = []

    if not case_sensitive:
        letters = letters.lower()

    for word in sorted(["".join(p) for p in set(itertools.permutations(letters, length))]):
        if dictionary.check(word):
            words.append(word)
    return words


@click.command()
@click.option("-L", "--letters", type=str, required=True, help="Letters used in the word.")
@click.option("-l", "--length", type=int, required=True, help="Length of the words to search.")
@click.option(
    "-d",
    "--language",
    type=str,
    default=DEFAULT_LANGUAGE,
    help=f"The language to search words (defaults to {DEFAULT_LANGUAGE})",
)
@click.option(
    "-c/ ",
    "--case-sensitive/--case-insensitive",
    default=False,
    help="Should search be case sensitive (defaults to insensitive).",
)
def main(letters: str, length: int, language: str, case_sensitive: bool) -> None:
    """Run the solver from CLI."""
    for word in solve(letters, length, language, case_sensitive):
        click.echo(word)


if __name__ == "__main__":
    main()  # pylint: disable=E1120
