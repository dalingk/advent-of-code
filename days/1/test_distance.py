import pytest

from distance import count_list_items
from distance import load_file
from distance import similarity_score
from distance import total_distance

CONTENT = """3   4
4   3
2   5
1   3
3   9
3   3
"""

example_lists = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])

list_counts = ({3: 3, 4: 1, 2: 1, 1: 1}, {4: 1, 3: 3, 5: 1, 9: 1})


@pytest.mark.parametrize("list1,list2,distance", ((*example_lists, 11),))
def test_total_distance(list1, list2, distance):
    assert total_distance(list1, list2) == distance


@pytest.mark.parametrize("list1,list2,distance", ((*example_lists, 31),))
def test_similarity_score(list1, list2, distance):
    assert similarity_score(list1, list2) == distance


@pytest.mark.parametrize("the_list,counts", zip(example_lists, list_counts))
def test_count_items(the_list, counts):
    assert count_list_items(the_list) == counts


def test_load_file(tmp_path):
    content = tmp_path / "input.txt"
    content.write_text(CONTENT)
    assert load_file(content) == example_lists
