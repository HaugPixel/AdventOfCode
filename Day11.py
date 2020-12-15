def checkDeath(lines, y, x):
    return countBox(lines, "#", y, x) > 4


def checkDeath_V2(lines, y, x):
    return countDirections(lines, y, x) > 4


def checkBirth(lines, y, x):
    return countBox(lines, "#", y, x) == 0


def checkBirth_V2(lines, y, x):
    return countDirections(lines, y, x) == 0


def countDirections(lines, y, x):
    count = 0
    for direction in QueenLines(y, x, lines):
        for y1, x2 in direction:
            if lines[y1][x2] == "#":
                count += 1
                break
            if lines[y1][x2] == "L":
                break
    return count


def QueenLines(y, x, lines):
    size = len(lines[0])
    nw = [(y-k, x-i) for i, k in zip(range(1, x+1), range(1, y+1))]
    ne = [(y-k, x+i) for i, k in zip(range(1, size-x), range(1, y+1))]
    sw = [(y+k, x-i) for i, k in zip(range(1, x+1), range(1, size-y))]
    se = [(y+k, x+i) for i, k in zip(range(1, size-x), range(1, size-y))]

    n = [(y-i, x) for i in range(1, y+1)]
    w = [(y, x-i) for i in range(1, x+1)]
    s = [(y+i, x) for i in range(1, size-y)]
    e = [(y, x+i) for i in range(1, size-x)]

    #print("\n",y, x)
    #for j, k in zip(["nw", "ne", "sw", "se", "n", "w", "s", "e"], [nw, ne, sw, se, n, w, s, e]):
    #    print(j, k)
    return [nw, ne, sw, se, n, w, s, e]


def countBox(lines, ele, y, x):
    count = 0
    for y, x in box(y, x, lines):
        if lines[y][x] == ele:
            count += 1
    return count


def inbound(y, x, lines):
    return 0 <= y <= len(lines) and 0 <= x <= len(lines[0])


def box(y,x, lines):
    return [(y+i, x+k) for i in range(-1, 2) for k in range(-1, 2) if not (x==0 and y==0) and inbound(y+i,x+k, lines)]


def countSeated(lines):
    count = 0
    for y in lines:
        for x in y:
            if x == "#":
                count += 1
    return count

def game_status(lines):
    births = []
    deaths = []
    for y, line in enumerate(lines):
        for x, ele in enumerate(line):
            if ele == "L":
                if checkBirth_V2(lines, y, x):
                    births.append((y, x))
            elif ele == "#":
                if checkDeath_V2(lines, y, x):
                    deaths.append((y, x))

    return births, deaths


def makeNewGen(lines, b, d):
    for (y, x) in b:
        lines[y][x] = "#"
    for (y, x) in d:
        lines[y][x] = "L"


def game_of_seating(lines):
    b, d = game_status(lines)
    makeNewGen(lines, b, d)
    return b or d


def main():
    with open("test.txt", "r") as fil:
        lines = [list(i.strip()) for i in fil.readlines()]

    newGen = True
    while newGen:
       # print()
       # [print(*i) for i in lines]
        newGen = game_of_seating(lines)

    print(countSeated(lines))


main()

"""
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""