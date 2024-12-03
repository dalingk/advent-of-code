import argparse
import enum
import pathlib
from itertools import pairwise

Report = list[int]


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent / "resources" / "input.txt",
        nargs="?",
    )
    return parser


def is_pair_safe(a: int, b: int, last_difference: int = None) -> tuple[bool, int]:
    difference = a - b
    return (
        abs(difference) >= 1
        and abs(difference) <= 3
        and (True if last_difference is None else difference * last_difference >= 0)
    ), difference


def is_safe_report(levels: Report) -> bool:
    """Is the given list of integers considered safe?"""
    last_difference = None
    for a, b in pairwise(levels):
        safe, last_difference = is_pair_safe(a, b, last_difference)
        if not safe:
            return False
    return True


def load_file(file_path: pathlib.Path) -> list[Report]:
    values = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            if strip_line := line.strip():
                values.append(tuple(int(x) for x in strip_line.split()))
    return values


def main():
    parser = get_parser()
    args = parser.parse_args()
    values = load_file(args.filename)

    count = sum(1 if is_safe_report(x) else 0 for x in values)
    print(f"{count} reports are safe")


if __name__ == "__main__":
    main()
