from os import path

count = 0

with open(path.join('..', 'resources', '4.txt')) as infile:
    for line in infile:
        split = line.split()
        if len(split) == len(set(split)):
            count += 1


print(count)
