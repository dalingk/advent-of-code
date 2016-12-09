def main():
    (up, right) = (3,1)
    values = [
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,2,3,4,0,0],
            [0,5,6,7,8,9,0],
            [0,0,'A','B','C',0,0],
            [0,0,0,'D',0,0,0],
            [0,0,0,0,0,0,0]
            ]
    with open("resources/day2input.txt", "r") as file:
        for line in file:
            for char in line:
                if char == 'U':
                    if up > 0 and values[up - 1][right] != 0:
                        up -= 1
                elif char == 'D':
                    if up < 7 and values[up + 1][right] != 0:
                        up += 1
                elif char == 'L':
                    if right > 0 and values[up][right - 1] != 0:
                        right -= 1
                elif char == 'R':
                    if right < 7 and values[up][right + 1] != 0:
                        right += 1
            print(values[up][right], end="")
        print("")


if __name__ == "__main__":
    main()
