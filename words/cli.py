"""Main CLI app module."""
import click

from .constants import DEFAULT_LANGUAGE
from .words import solve


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
def main(letters: str, length: int, language: str, *, case_sensitive: bool) -> None:
    """Run the solver from CLI."""
    for word in solve(letters, length, language, case_sensitive=case_sensitive):
        click.echo(word)
