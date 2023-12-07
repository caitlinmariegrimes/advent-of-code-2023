def part1():
    with open('aoc2.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    valid = 0
    j = 0
    for line in lines:
        line = line.split()
        for i in line:
            print(line[i].rstrip())
            i += 1
        j += 1
        if j < 2:
            break
        '''min, max = line[0].split("-")
        min = int(min)
        max = int(max)
        letter = line[1][0]
        password = line[2]
        if min <= password.count(letter) <= max:
            valid += 1
    return valid'''


def main():
    print("temp")
    part1()
    #print("Day 2, Part 1 Solution:", part1())
    #print("Day 2, Part 2 Solution:", part2())

if __name__ == "__main__":
    main()