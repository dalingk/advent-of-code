import pytest
from total_distance import total_distance, load_file

CONTENT = """3   4
4   3
2   5
1   3
3   9
3   3
"""

example_lists = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


@pytest.mark.parametrize("list1,list2,distance", ((*example_lists, 11),))
def test_total_distance(list1, list2, distance):
    assert total_distance(list1, list2) == distance


def test_load_file(tmp_path):
    content = tmp_path / "input.txt"
    content.write_text(CONTENT)
    assert load_file(content) == example_lists
