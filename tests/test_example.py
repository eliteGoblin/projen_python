import pytest

from projen_python.example import hello


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("A. Musing", "Hello A. Musing!"),
        ("traveler", "Hello traveler!"),
        ("projen developer", "Hello projen developer!"),
    ],
)
def test_hello(name: str, expected: str) -> None:
    """Example test with parametrization."""
    assert hello(name) == expected
