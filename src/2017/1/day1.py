"""Day 1 solver for 2017 AOC"""

def load_input(filename):
    """Load file and return list of numbers"""
    rtrn = []
    infile = open(filename)
    for line in infile:
        rtrn += [int(x) for x in line]
    return rtrn

def main():
    """Main function"""
    input_list = load_input('../resources/day1.txt')
    total = 0
    for idx, digit in enumerate(input_list):
        next_idx = idx + 1
        if digit == input_list[next_idx % len(input_list)]:
            total += digit
    print(total)
    total_part_2 = 0
    for idx, digit in enumerate(input_list):
        next_idx = idx + (len(input_list) // 2)
        if digit == input_list[next_idx % len(input_list)]:
            total_part_2 += digit
    print(total_part_2)


if __name__ == '__main__':
    main()
