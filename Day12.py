import math

def move(y, x, f, cmd):
    if cmd == "N":
        return [y -f, x]
    if cmd == "W":
        return [y, x - f]
    if cmd == "S":
        return [y + f, x]
    if cmd == "E":
        return [y, x + f]


def boating(commands):
    y,x = (0,0)
    dirs = ["E","S","W","N"]
    current = 0

    for cmd in commands:
        if cmd[0] == "R":
            current = (current + int(cmd[1:])//90) % 4
        elif cmd[0] == "L":
            current = (4 + current - int(cmd[1:])//90) % 4
        elif cmd[0] == "F":
            y, x = move(y, x, int(cmd[1:]), dirs[current])
        else:
            y, x = move(y, x, int(cmd[1:]), cmd[0])

    return abs(y)+abs(x)

def way_pointing(commands):
    by, bx = (0,0)
    wy, wx = (-1,10)
    dirs = ["E","S","W","N"]

    for cmd in commands:
        n = int(cmd[1:])
        if cmd[0] == "R" or cmd[0] == "L":
            nd = n//90
            while nd:
                if cmd[0] == "R":
                    wy, wx = (wx, -wy)
                if cmd[0] == "L":
                    wy, wx = (-wx, wy)
                nd -=1

        elif cmd[0] == "F":
            by, bx = by+(n*wy), bx+(n*wx)

        else:
            wy, wx = move(wy, wx, int(cmd[1:]), cmd[0])

        print(cmd)
        print("Boat", by,bx)
        print("Wp", wy,wx)
        print()

    return abs(by)+abs(bx)


def main():
    with open("test.txt", "r") as fil:
        commands = [i.strip() for i in fil.readlines()]

    print(way_pointing(commands))

main()