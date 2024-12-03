import argparse
import pathlib
import re

MUL_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
ENABLE_MUL_RE = re.compile(r"((?:do|don't)\(\))|(mul)\((\d{1,3}),(\d{1,3})\)")


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


def get_mult_enable_groups(the_input: str) -> list[tuple[int, int]]:
    commands = []
    enabled = True
    for match in ENABLE_MUL_RE.finditer(the_input):
        if match.group(1) == "do()":
            enabled = True
        elif match.group(1) == "don't()":
            enabled = False
        if enabled and match.group(2) == "mul":
            commands.append((int(match.group(3)), int(match.group(4))))
    return commands


def main():
    parser = get_parser()
    args = parser.parse_args()
    lines = load_file(args.filename)

    groups = get_multiplication_groups(lines)
    print(f"Sum of multiplications: {sum(x * y for x,y in groups)}")

    enabled_groups = get_mult_enable_groups(lines)
    print(f"Sum of enabled multiplications: {sum(x * y for x,y in enabled_groups)}")


if __name__ == "__main__":
    main()
