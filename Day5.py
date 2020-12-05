def findbst(n, foo):
    top = n
    mid = 0
    bot = 0
    for i in range(len(foo)):
        cmd = foo[i]
        if cmd == 'B' or cmd == 'R':
            mid = (top-bot) // 2
            bot = bot  + mid
        elif cmd == 'F' or cmd == 'L':
            mid = (top-bot) // 2
            top = bot + mid

    return top


def main():
    seatcoord = set()
    with open("seat.txt", 'r') as f:
        mylist = f.readlines()
    seatlist = mylist
    for x in seatlist:
        row = x[:7]
        col = x[7:]

        rown = findbst(127, row)
        coln = findbst(7, col)

        cord = (rown, coln)
        seatcoord.add(cord)
        res = rown*8 + coln

    missingSeats = []
    for y in range(127):
        for x in range(7):
            if (y,x) not in seatcoord:
                missingSeats.append((y, x))
    print(missingSeats)
main()
