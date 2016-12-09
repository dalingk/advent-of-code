from pprint import pprint
import heapq
def main():
    total = 0
    heap = [[],[],[]]
    with open("resources/day3input.txt", "r") as file:
        for line in file:
            numbers = [int(s) for s in line.split() if s.isdigit()]
            for i,n in enumerate(numbers):
                heap[i].append(n)
        for li in heap:
            s = sorted(li)
            (first, second, third) = (0,1,2)
            while third < len(li):
                subset = (s[first], s[second], s[third])
                if triangle(subset):
                    total += 1
                    first = third + 1
                    second = first + 1
                    third = second + 1
                else:
                    third += 1
        print(total)


def triangle(elmList):
    maximum = max(elmList)
    if sum(elmList) - maximum > maximum:
        return True
    else:
        return False



if __name__ == "__main__":
    main()
