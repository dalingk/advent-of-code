from pprint import pprint
def main():
    with open('resources/day4tests.txt', 'r') as testFile:
        for line in testFile:
            sline = line.strip().replace('-','').split('[')
            print(sline)

if __name__ == "__main__":
    main()
