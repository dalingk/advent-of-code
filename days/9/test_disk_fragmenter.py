import pytest

from disk_fragmenter import expand_blocks
from disk_fragmenter import compact_blocks
from disk_fragmenter import compute_checksum
from disk_fragmenter import DiskBlocks


def str_to_disk_blocks(input_str: str) -> DiskBlocks:
    return [x if x == "." else int(x) for x in input_str]


TEST_STRINGS = ["12345", "2333133121414131402"]
TEST_BLOCKS = [
    str_to_disk_blocks("0..111....22222"),
    str_to_disk_blocks("00...111...2...333.44.5555.6666.777.888899"),
]
COMPACTED_BLOCKS = [
    str_to_disk_blocks("022111222......"),
    str_to_disk_blocks("0099811188827773336446555566.............."),
]


@pytest.mark.parametrize("disk_blocks,result", zip(TEST_BLOCKS, COMPACTED_BLOCKS))
def test_compact_blocks(disk_blocks: DiskBlocks, result: DiskBlocks):
    assert compact_blocks(disk_blocks) == result


@pytest.mark.parametrize("disk_blocks,result", zip(COMPACTED_BLOCKS, [60, 1928]))
def test_compute_checksum(disk_blocks: DiskBlocks, result: int):
    assert compute_checksum(disk_blocks) == result


@pytest.mark.parametrize(
    "disk_map,result",
    zip(
        TEST_STRINGS,
        TEST_BLOCKS,
    ),
)
def test_expand_blocks(disk_map: str, result: list[str]):
    assert expand_blocks(disk_map) == result
