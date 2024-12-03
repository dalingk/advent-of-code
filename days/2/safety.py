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
    """Returns true if the current difference between a and b is the same sign as
    the last difference and the differences is greater than 1 or less than 3."""
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


def minimize_distance_to_next(levels: Report) -> int:
    value, compare, next_compare = levels
    return value if abs(value - next_compare) < abs(compare - next_compare) else compare


def minimize_distance_from_previous(levels: Report) -> int:
    value, compare, next_compare = levels
    return compare if abs(compare - value) < abs(next_compare - value) else next_compare


def is_safe_dampened(levels: Report) -> bool:
    """If the report isn't safe, brute force removals to see if any are."""
    if is_safe_report(levels):
        return True
    for i in range(len(levels)):
        if is_safe_report(levels[0:i] + levels[i + 1 : len(levels)]):
            return True
    return False


def load_file(file_path: pathlib.Path) -> list[Report]:
    values = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            if strip_line := line.strip():
                values.append(list(int(x) for x in strip_line.split()))
    return values


def main():
    parser = get_parser()
    args = parser.parse_args()
    values = load_file(args.filename)

    for value in values:
        if not is_safe_report(value):
            print(f"{value} {is_safe_report(value)} {is_safe_dampened(value)}")

    count = sum(1 if is_safe_report(x) else 0 for x in values)
    print(f"{count} reports are safe")
    count_dampened = sum(1 if is_safe_dampened(x) else 0 for x in values)
    print(f"{count_dampened} reports are safe with dampening applied.")


if __name__ == "__main__":
    main()
