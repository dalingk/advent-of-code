import argparse
import pathlib

DiskBlocks = list[int | str]


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
    blocks = []
    block_idx = 0
    for i, number in enumerate(disk_map):
        character = block_idx if i % 2 == 0 else "."
        blocks += [character for _ in range(int(number))]
        if i % 2 == 0:
            block_idx += 1
    return blocks


def compact_blocks(disk_blocks: DiskBlocks) -> DiskBlocks:
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


def compute_checksum(disk_blocks: DiskBlocks) -> int:
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
    defragmented = compact_blocks(blocks)
    checksum = compute_checksum(defragmented)
    print(f"Filesystem checksum: {checksum}")


if __name__ == "__main__":
    main()
