import itertools

import click

import enchant

DEFAULT_LANG = "en_US"


@click.command()
@click.option(
    "-L", "--letters", type=str, required=True, help="Letters used in the word."
)
@click.option(
    "-l", "--length", type=int, required=True, help="Length of the words to search."
)
@click.option(
    "-d",
    "--dictionary",
    type=str,
    default=DEFAULT_LANG,
    help=f"The language to search words (defaults to {DEFAULT_LANG})",
)
def main(letters: str, length: int, dictionary: str = DEFAULT_LANG) -> None:
    d = enchant.Dict(dictionary)

    for w in sorted(["".join(p) for p in set(itertools.permutations(letters, length))]):
        if d.check(w):
            click.echo(w)


if __name__ == "__main__":
    main()
