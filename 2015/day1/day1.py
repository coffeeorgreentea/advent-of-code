

# reads input from .txt
def read_input():
    with open('day1.txt', 'r') as f:
        return f.read()

# counts occurence of a string in another string


def count_string(string, substring):
    return string.count(substring)

# returns floor value


def moveFloor(str):
    if str == '(':
        return 1
    elif str == ')':
        return -1


def part_one():
    input = read_input()
    up = count_string(input, '(')
    down = count_string(input, ')')
    print("Part One: " + str(up - down))


def part_two():
    floor = 0
    input = read_input()
    for i, c in enumerate(input):
        floor += moveFloor(c)
        if floor == -1:
            print("Part Two: " + str(i + 1))
            break


part_one()

part_two()
