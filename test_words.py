from typing import Sequence, TypedDict

from click.testing import CliRunner

import pytest

from words import main, solve


default_help_msg = ["Usage: main [OPTIONS]", "Try 'main --help' for help.", ""]


class HeterogeneousDictionary(TypedDict):
    """Solve function paramters typing definition."""
    letters: str
    length: int
    language: str
    case_sensitive: bool


@pytest.mark.parametrize(
    "test_data,expected",
    [
        ({"letters": "angular", "length": 5}, ["aural", "gnarl", "lunar", "ulnar"]),
        ({"letters": "angular", "length": 5, "language": "fr_FR"}, ["aluna", "argua", "gaula", "glana", "ragua"]),
        (
            {"letters": "Angular", "length": 5, "language": "en_US", "case_sensitive": True},
            ["Aural", "gnarl", "lunar", "ulnar"],
        ),
        ({"letters": "Angular", "length": 5, "language": "fr_FR", "case_sensitive": True}, ["Aluna", "Argua"]),
    ],
)
def test_solve(test_data: HeterogeneousDictionary, expected: list[str]) -> None:
    """Test solve function."""
    assert solve(**test_data) == expected


@pytest.mark.parametrize(
    "test_data,expected",
    [
        ((), default_help_msg + ["Error: Missing option '-L' / '--letters'."]),
        (("--letters", "angular"), default_help_msg + ["Error: Missing option '-l' / '--length'."]),
    ],
)
def test_required_args(test_data: Sequence[str], expected: list[str]) -> None:
    """Test CLI required arguments."""
    runner = CliRunner()
    result = runner.invoke(main, test_data)
    assert result.exit_code == 2
    assert result.stdout == "\n".join(expected) + "\n"


@pytest.mark.parametrize(
    "test_data,expected",
    [
        (("--letters", "angular", "--length", "5"), ["aural", "gnarl", "lunar", "ulnar"]),
        (
            ("--letters", "angular", "--length", "5", "--language", "fr_FR"),
            ["aluna", "argua", "gaula", "glana", "ragua"],
        ),
        (("--letters", "Angular", "--length", "5", "--case-sensitive"), ["Aural", "gnarl", "lunar", "ulnar"]),
        (("--letters", "Angular", "--length", "5", "--language", "fr_FR", "--case-sensitive"), ["Aluna", "Argua"]),
    ],
)
def test_main(test_data: Sequence[str], expected: list[str]):
    """Test main function."""
    runner = CliRunner()
    result = runner.invoke(main, test_data)
    assert result.stdout == "\n".join(expected) + "\n"
