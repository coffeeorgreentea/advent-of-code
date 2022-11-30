

# reads input from txt by line into list of int arrays split by 'x' and strips newline
def read_input():
    with open('day2.txt', 'r') as f:
        return [list(map(int, line.strip().split('x'))) for line in f.readlines()]


def calc_wrapping_paper(l, w, h):
    l, w, h = l*w, w*h, h*l
    slack = min(l, w, h)
    return 2*l+2*w+2*h+slack


def calc_ribbon(l, w, h):
    l, w, h = l+w, w+h, h+l
    bow = l*w*h
    ribbon = 2*min(l, w, h)
    return ribbon+bow


def part_one():
    total = 0
    input = read_input()
    for i in input:
        total += calc_wrapping_paper(i[0], i[1], i[2])
    print("Part One: " + str(total))


def part_two():
    total = 0
    input = read_input()
    for i in input:
        total += calc_ribbon(i[0], i[1], i[2])
    print("Part Two: " + str(total))


part_one()
