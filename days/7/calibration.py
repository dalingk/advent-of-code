import argparse
import pathlib
import re


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent / "resources" / "input.txt",
        nargs="?",
    )
    return parser


def load_file(file_path: pathlib.Path) -> list[tuple[int, list[int]]]:
    lines = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            strip = line.strip()
            if strip:
                calibration, rest = strip.split(":")
                lines.append((int(calibration), [int(x) for x in rest.split()]))
    return lines


def main():
    parser = get_parser()
    args = parser.parse_args()
    equations = load_file(args.filename)

    total_calibration = 0
    for calibration_result, equation in equations:
        if is_valid_equation(calibration_result, equation):
            total_calibration += calibration_result

    print(f"Total calibration result {total_calibration}")


def is_valid_equation(
    test_value: int, equation: list[int], accumulated: int | None = None
) -> bool:
    if not equation:
        return test_value == accumulated
    if accumulated is None:
        left, right = equation[:2]
        next = equation[2:]
    else:
        left = accumulated
        right = equation[0]
        next = equation[1:]
    if is_valid_equation(test_value, next, accumulated=left * right):
        return True
    elif is_valid_equation(test_value, next, accumulated=left + right):
        return True
    return False


if __name__ == "__main__":
    main()
