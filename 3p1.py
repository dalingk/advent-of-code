from pprint import pprint
import heapq
def main():
    total = 0
    with open("resources/day3input.txt", "r") as file:
        for line in file:
            numbers = [int(s) for s in line.split() if s.isdigit()]
            maximum = max(numbers)
            if sum(numbers) - maximum > maximum:
                total += 1
        print(total)

if __name__ == "__main__":
    main()
