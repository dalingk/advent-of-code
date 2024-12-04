import pytest

from word_search import count_xmas_matches
from word_search import DIRECTIONS
from word_search import LETTERS


@pytest.fixture
def generate_grid(request: pytest.FixtureRequest) -> list[list[int]]:
    direction_x, direction_y = request.param
    grid = [["." for y in range(7)] for x in range(7)]
    grid[3][3] = "X"
    for i in range(1, 4):
        grid[3 + direction_x * i][3 + direction_y * i] = LETTERS[i]
    return grid


@pytest.mark.parametrize("generate_grid", DIRECTIONS, indirect=["generate_grid"])
def test_count_matches(generate_grid):
    assert count_xmas_matches(generate_grid) == 1
    generate_grid[3][3] = "."
    assert count_xmas_matches(generate_grid) == 0
