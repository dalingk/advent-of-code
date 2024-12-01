import argparse
import pathlib

LocationIdList = list[int]


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent / "resources" / "input.txt",
        nargs="?",
    )
    return parser


def load_file(filename: pathlib.Path) -> tuple[LocationIdList, LocationIdList]:
    """Open and parse a file containing 2 integers on each line."""
    list1 = []
    list2 = []
    with open(filename, "r") as read_file:
        for line in read_file:
            split_line = line.split()
            if not split_line:
                continue
            int1, int2 = [int(x) for x in line.split()]
            list1.append(int1)
            list2.append(int2)
    return list1, list2


def total_distance(list1: LocationIdList, list2: LocationIdList) -> int:
    """Given 2 lists, compute the minimum possible Hamming Distance between them"""
    distance = 0
    for i, j in zip(sorted(list1), sorted(list2)):
        distance += abs(i - j)
    return distance


def main():
    parser = get_parser()
    args = parser.parse_args()
    list1, list2 = load_file(args.filename)
    print(f"Total Distance: {total_distance(list1, list2)}")


if __name__ == "__main__":
    main()
