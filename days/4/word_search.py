import argparse
import pathlib

Puzzle = list[list[int]]


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent / "resources" / "input.txt",
        nargs="?",
    )
    return parser


# Matches can be found in any of these directions
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
LETTERS = "XMAS"


def count_xmas_matches(puzzle: Puzzle) -> int:
    """Could the number of times XMAS appears in the puzzle"""
    match_count = 0
    for i, puzzle_row in enumerate(puzzle):
        for j, puzzle_entry in enumerate(puzzle_row):
            for offset_i, offset_j in DIRECTIONS:
                i_extent = i + offset_i * 3
                j_extent = j + offset_j * 3
                if (
                    puzzle_entry != "X"
                    or i_extent < 0
                    or i_extent >= len(puzzle)
                    or j_extent < 0
                    or j_extent >= len(puzzle_row)
                ):
                    continue
                if all(
                    puzzle[i + offset_i * x][j + offset_j * x] == LETTERS[x]
                    for x in range(1, 4)
                ):
                    match_count += 1
    return match_count


def load_file(file_path: pathlib.Path) -> Puzzle:
    lines = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            lines.append([x for x in line.strip()])
    return lines


def main():
    parser = get_parser()
    args = parser.parse_args()
    puzzle = load_file(args.filename)

    print(f"{count_xmas_matches(puzzle)} matches for XMAS")


if __name__ == "__main__":
    main()
