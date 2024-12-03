import pytest

from safety import is_pair_safe
from safety import is_safe_dampened
from safety import is_safe_report
from safety import load_file
from safety import minimize_distance_from_previous
from safety import minimize_distance_to_next

TEST_LEVELS = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
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
    zip(TEST_LEVELS, (True, False, False, False, False, True)),
)
def test_is_safe_report(the_list, result):
    assert is_safe_report(the_list) == result


@pytest.mark.parametrize(
    "the_list,result",
    list(zip(TEST_LEVELS, (True, False, False, True, True, True)))
    + [
        ([1, 2, 2, 2], False),
        ([1, 2, 2, 3, 4, 5], True),
        ([7, 10, 8, 10, 11], True),
        ([29, 28, 27, 25, 26, 25, 22, 20], True),
        ([1, 1, 2, 3, 4, 5], True),
    ],
)
def test_is_safe_dampened(the_list, result):
    assert is_safe_dampened(the_list) == result


@pytest.mark.parametrize(
    "levels,value", [((1, 10, 11), 10), ((2, 11, 3), 2), ((10, 9, 1), 9)]
)
def test_minimize_distance_to_next(levels, value):
    assert minimize_distance_to_next(levels) == value


@pytest.mark.parametrize("levels,value", [((27, 25, 26), 26)])
def test_minimize_distance_from_previous(levels, value):
    assert minimize_distance_from_previous(levels) == value


def test_load_file(tmp_path):
    content = tmp_path / "input.txt"
    content.write_text(TEST_FILE_CONTENT)
    assert load_file(content) == TEST_LEVELS
