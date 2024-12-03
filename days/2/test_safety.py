import pytest

from safety import is_pair_safe
from safety import is_safe_report
from safety import load_file

TEST_LEVELS = [
    (7, 6, 4, 2, 1),
    (1, 2, 7, 8, 9),
    (9, 7, 6, 2, 1),
    (1, 3, 2, 4, 5),
    (8, 6, 4, 4, 1),
    (1, 3, 6, 7, 9),
]

TEST_FILE_CONTENT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


@pytest.mark.parametrize(
    "a,b,last_difference,result",
    [(2, 7, None, False), (6, 2, None, False), (3, 6, -2, True)],
)
def test_is_pair_safe(a, b, last_difference, result):
    safe, _ = is_pair_safe(a, b, last_difference)
    assert safe == result


@pytest.mark.parametrize(
    "the_list,result",
    [
        ((7, 6, 4, 2, 1), True),
        ((1, 2, 7, 8, 9), False),
        ((9, 7, 6, 2, 1), False),
        ((1, 3, 2, 4, 5), False),
        ((8, 6, 4, 4, 1), False),
        ((1, 3, 6, 7, 9), True),
    ],
)
def test_is_safe_report(the_list, result):
    assert is_safe_report(the_list) == result


def test_load_file(tmp_path):
    content = tmp_path / "input.txt"
    content.write_text(TEST_FILE_CONTENT)
    assert load_file(content) == TEST_LEVELS
