def main():
    counts = []
    sortedcounts = []
    strlen = 8
    for x in range(strlen):
        counts.append({})
    with open("resources/day6input.txt", "r") as infile:
        for l in infile:
            line = l.strip()
            for i, char in enumerate(line):
                if char not in counts[i]:
                    counts[i][char] = 0
                counts[i][char] += 1
    for i, elm in enumerate(counts):
        sortedcounts.append(sorted(counts[i], key=counts[i].get))
    print("".join(x[0] for x in sortedcounts))

if __name__ == "__main__":
    main()
