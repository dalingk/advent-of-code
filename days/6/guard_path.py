import argparse
import pathlib

LabRoom = list[list[str]]
Point = tuple[int, int]
Obstructions = list[Point]

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=pathlib.Path,
        default=pathlib.Path(__file__).parent / "resources" / "input.txt",
        nargs="?",
    )
    return parser


def load_file(file_path: pathlib.Path) -> LabRoom:
    with open(file_path, "r") as input_file:
        return [[y for y in x.strip()] for x in input_file]


def get_starting_location(puzzle: LabRoom) -> Point:
    for i, line in enumerate(puzzle):
        try:
            column = line.index("^")
            return i, column
        except ValueError:
            pass
    raise ValueError("Could not find starting location")


def is_guard_in_map(x: int, y: int, map: LabRoom) -> bool:
    """From the indexes, determine if the guard is still in the map."""
    return x >= 0 and x < len(map) and y >= 0 and y < len(map[0])


def update_direction(x: int, y: int, direction: tuple[int, int]) -> tuple[int, int]:
    return x + direction[0], y + direction[1]


def print_map(map: LabRoom):
    print("\n".join("".join(x) for x in map))


def leads_to_obstruction(location: Point, direction: Point, map: LabRoom) -> bool:
    """If the guard walks in direction from location in the map, will the path lead to an obstruction?"""
    temp_x, temp_y = location
    update_x, update_y = direction
    while is_guard_in_map(temp_x, temp_y, map) and map[temp_x][temp_y] != "#":
        temp_x += update_x
        temp_y += update_y
    return map[temp_x][temp_y] == "+"


def returns_to_position(location: Point, direction_idx: int, map: LabRoom) -> bool:
    """If a turn is taken here, does it return to this point?"""
    original_direction = direction_idx
    current_direction = original_direction + 1
    print(location)

    p_x, p_y = update_direction(
        *location, DIRECTIONS[current_direction % len(DIRECTIONS)]
    )

    while (
        is_guard_in_map(p_x, p_y, map)
        and (current_direction % len(DIRECTIONS)) != original_direction
    ):
        print(current_direction)
        if (p_x, p_y) == location:
            return True

        next_x, next_y = update_direction(
            p_x, p_y, DIRECTIONS[current_direction % len(DIRECTIONS)]
        )
        if is_guard_in_map(next_x, next_y, map) and map[next_x][next_y] == "#":
            current_direction += 1
        p_x, p_y = update_direction(
            p_x, p_y, DIRECTIONS[current_direction % len(DIRECTIONS)]
        )
    return False


def trace_guard_path(map: LabRoom) -> Obstructions:
    """Update the map to indicate the guard's path."""
    position_x, position_y = get_starting_location(map)
    obstructions = set()
    position_markers = ["|", "-", "|", "-"]
    direction_idx = 0
    loop = 0

    while is_guard_in_map(position_x, position_y, map):
        next_x, next_y = update_direction(
            position_x, position_y, DIRECTIONS[direction_idx]
        )

        if map[position_x][position_y] in (".", "^"):
            map[position_x][position_y] = position_markers[direction_idx]
        else:
            map[position_x][position_y] = "+"

        if returns_to_position((position_x, position_y), direction_idx, map):
            obstructions.add((next_x, next_y))

        if is_guard_in_map(next_x, next_y, map):
            if map[next_x][next_y] == "#":
                map[position_x][position_y] = "+"
                direction_idx = (direction_idx + 1) % len(DIRECTIONS)
                next_x, next_y = update_direction(
                    position_x, position_y, DIRECTIONS[direction_idx]
                )
        position_x, position_y = next_x, next_y
        loop += 1
        if loop % 1000 == 0:
            print_map(map)

    return obstructions


def main():
    parser = get_parser()
    args = parser.parse_args()
    map = load_file(args.filename)

    obstructions = trace_guard_path(map)

    count = sum(x.count("X") for x in map)
    print(f"The guard visits {count} positions")

    print(
        f"Obstructions could be placed in {len(obstructions)} places to create infinite loops"
    )


if __name__ == "__main__":
    main()
