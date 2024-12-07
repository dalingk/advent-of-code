import pytest
from pprint import pprint

from guard_path import get_starting_location
from guard_path import trace_guard_path

SAMPLE_MAP = [
    [y for y in x.strip()]
    for x in """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split()
]


def test_get_starting_location():
    room = [".....", "..^..", "......"]
    assert get_starting_location(room) == (1, 2)


def test_trace_guard_path():
    obstructions = trace_guard_path(SAMPLE_MAP)
    assert SAMPLE_MAP[9][7] == "|"
    assert obstructions == {(6,3), (7,6), (8,3), (9,7), (8,1), (7,7)}
