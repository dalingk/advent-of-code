from pprint import pprint

def main():
    with open('resources/day1input.txt', 'r') as file:
        string = file.read()
    string = string.strip()
    actions = string.split(", ");
    direction = 0
    (up, right) = (0, 0)
    for x in actions:
        blocks = int(x[1:])
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
        #print("Facing: {}, Moving: {}, Up: {}, Right: {}".format(direction, blocks, up, right))
    print("Up: {}, Right: {}".format(up, right))
    print("Total blocks: {}".format(abs(up) + abs(right)))

def isEven(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()
