from pprint import pprint

def main():
    with open('resources/day1input.txt', 'r') as file:
        string = file.read()
    string = string.strip()
    actions = string.split(", ");
    direction = 0
    location = []
    (up, right) = (0, 0)
    for x in actions:
        blocks = int(x[1:])
        old = (up, right)
        if x[0] == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        if direction == 0:
            up += blocks
        elif direction == 2:
            up -= blocks
        elif direction == 1:
            right += blocks
        elif direction == 3:
            right -= blocks
        location.append((old, (up, right)))
    pprint(location)

if __name__ == "__main__":
    main()
