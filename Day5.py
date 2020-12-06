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
    seatcoord = []
    with open("seat.txt", 'r') as f:
        mylist = f.readlines()
    seatlist = mylist
    for x in seatlist:
        row = x[:7]
        col = x[7:]

        rown = findbst(127, row)
        coln = findbst(7, col)
        seatcoord.append(rown*8 + coln)

    print(seatcoord)



main()
