import argparse
import pathlib
import re

MUL_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent / "resources" / "input.txt",
        nargs="?",
    )
    return parser


def load_file(file_path: pathlib.Path) -> str:
    with open(file_path, "r") as input_file:
        lines = "".join(x for x in input_file)
    return lines


def get_multiplication_groups(the_input: str) -> list[tuple[int, int]]:
    return [(int(x), int(y)) for x, y in MUL_RE.findall(the_input)]


def main():
    parser = get_parser()
    args = parser.parse_args()
    lines = load_file(args.filename)

    groups = get_multiplication_groups(lines)
    print(f"Sum of multiplications: {sum(x * y for x,y in groups)}")


if __name__ == "__main__":
    main()
