import re

def main():
    count = 0
    with open("resources/day7input.txt","r") as infile:
        for l in infile:
            line = re.split("\[|\]", l.strip())
            possible = False
            for i, item in enumerate(line):
                if isABBA(item):
                    if i % 2 == 0:
                        possible = True
                    else:
                        possible = False
                        break
            if possible:
                count += 1
    print("Total {}".format(count))

def isABBA(item):
    for i, char in enumerate(item):
        if i + 4 > len(item):
            return False
        if item.rindex(char) != i:
            if item[i] == item[i + 3] and item[i + 1] == item[i + 2] and item[i] != item[i + 1]:
                return True
    return False

if __name__ == "__main__":
    main()
