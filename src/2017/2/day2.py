
def main():
    infile = open('../resources/2.txt')
    int_lines = [[int(x) for x in y.split()] for y in infile]
    part1(int_lines)
    part2(int_lines)


def part1(lines):
    total = 0
    for line in lines:
        total += max(line) - min(line)
    print('Checksum is {}'.format(total))


def part2(lines):
    total = 0
    for line in lines:
        line = sorted(line)
        found = False
        for idx, val_1 in enumerate(line):
            for val_2 in line[idx + 1:]:
                if not found:
                    if (val_1 % val_2) == 0:
                        print("{} divides {}".format(val_1, val_2))
                        total += val_1 // val_2
                        found = True
                    elif (val_2 % val_1) == 0:
                        print("{} divides {}".format(val_1, val_2))
                        total += val_2 // val_1
                        found = True
    print('Checksum part 2 is {}'.format(total))


if __name__ == '__main__':
    main()
