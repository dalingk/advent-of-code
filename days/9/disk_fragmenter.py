import argparse
import pathlib
from typing import Generator

DiskBlocks = list[int | str]


class FileSpan:
    def __init__(self, span):
        self.span = span

    def __len__(self):
        return self.span


class File(FileSpan):
    """A span of file blocks with content."""

    def __init__(self, span, num):
        self.number = num
        super().__init__(span)


class Empty(FileSpan):
    """A span of non-allocated blocks"""


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent / "resources" / "input.txt",
        nargs="?",
    )
    return parser


def compute_compacted_checksum(disk_map: str) -> int:
    """1 iteration through disk_map to compute the checksum."""
    checksum = 0
    block_idx = 0

    disk_map_idx = 0

    defragmenting_idx = len(disk_map) - 1
    defragmenting = disk_map[-1]
    defragmenting_count = 0

    while disk_map_idx < defragmenting_idx:
        if block_idx % 2 == 0:
            pass
        else:
            pass

    return checksum


def expand_blocks(disk_map: str) -> DiskBlocks:
    """Expand the sparse disk representation to block representation"""
    blocks = []
    block_idx = 0
    for i, number in enumerate(disk_map):
        character = block_idx if i % 2 == 0 else "."
        blocks += [character for _ in range(int(number))]
        if i % 2 == 0:
            block_idx += 1
    return blocks


def compact_blocks(disk_blocks: DiskBlocks) -> DiskBlocks:
    """Compact blocks, placing them in any available free space"""
    updated_blocks = disk_blocks.copy()

    defragment_idx = len(disk_blocks) - 1
    for i, value in enumerate(disk_blocks):
        if value == "." and i < defragment_idx:
            updated_blocks[i], updated_blocks[defragment_idx] = (
                updated_blocks[defragment_idx],
                updated_blocks[i],
            )
            defragment_idx -= 1
            while disk_blocks[defragment_idx] == ".":
                defragment_idx -= 1

    return updated_blocks


def get_free_blocks(blocks: DiskBlocks) -> Generator[tuple[int, int], None, None]:
    free_idx = 0
    free_length = 0

    while free_idx + free_length < len(blocks):
        if blocks[free_idx + free_length] == ".":
            free_length += 1
        elif free_length == 0 and blocks[free_idx] != ".":
            free_idx += 1
        elif free_length > 0 and blocks[free_idx + free_length] != ".":
            yield (free_idx, free_length)
            free_idx += free_length
            free_length = 0


def compact_files(disk_blocks: DiskBlocks) -> DiskBlocks:
    updated_blocks = disk_blocks.copy()

    compact_idx = len(disk_blocks) - 1
    while disk_blocks[compact_idx] == ".":
        compact_idx -= 1

    while compact_idx >= 0:
        if updated_blocks[compact_idx] == ".":
            compact_idx -= 1
        else:
            test_idx = compact_idx
            while updated_blocks[test_idx] == updated_blocks[compact_idx]:
                test_idx -= 1
            for free_idx, free_length in get_free_blocks(updated_blocks):
                if free_length >= compact_idx - test_idx and free_idx < test_idx:
                    updated_blocks[free_idx : free_idx + compact_idx - test_idx] = (
                        updated_blocks[test_idx + 1 : compact_idx + 1]
                    )
                    updated_blocks[test_idx + 1 : compact_idx + 1] = [
                        "." for _ in range(test_idx, compact_idx)
                    ]
                    break
            compact_idx = test_idx
        if compact_idx % 100 == 0:
            print(compact_idx)

    return updated_blocks


def compute_checksum(disk_blocks: DiskBlocks) -> int:
    """Compute the checksum for a filesystem represented as blocks"""
    checksum = 0
    for i, block_value in enumerate(disk_blocks):
        if block_value != ".":
            checksum += i * block_value
    return checksum


def load_file(filename: pathlib.Path) -> str:
    with open(filename, "r") as input_file:
        return input_file.read().strip()


def main():
    parser = get_parser()
    args = parser.parse_args()
    puzzle_input = load_file(args.filename)

    blocks = expand_blocks(puzzle_input)
    compacted = compact_blocks(blocks)
    checksum = compute_checksum(compacted)
    print(f"Filesystem checksum: {checksum}")

    compacted_files = compact_files(blocks)
    checksum_files = compute_checksum(compacted_files)
    print(f"Filesystem checksum with file compaction: {checksum_files}")


if __name__ == "__main__":
    main()
