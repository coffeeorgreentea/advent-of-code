

# reads input from txt by line into list of int arrays split by 'x' and strips newline
def read_input():
    with open('day2.txt', 'r') as f:
        return [list(map(int, line.strip().split('x'))) for line in f.readlines()]


def calc_wrapping_paper(l, w, h):
    l, w, h = l*w, w*h, h*l
    slack = min(l, w, h)
    return 2*l+2*w+2*h+slack

# find the small and medium numbers
def smallest(a, b, c):
    if a < b:
        if a < c:
            return a, min(b, c)
        else:
            return c, min(a, b)
    else:
        if b < c:
            return b, min(a, c)
        else:
            return c, min(a, b)


def calc_ribbon(l, w, h):
    sm, md = smallest(l, w, h)
    wrap = 2*sm + 2*md
    bow = l*w*h
    return wrap + bow


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
part_two()
