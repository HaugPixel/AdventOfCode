with open("Day1_Input", 'r') as fil:
    liste = [int(i)for i in fil.readlines()]
    myset = set(liste)
    print([x * y * (2020 - (x + y)) for x in liste for y in liste if 2020 - (x + y) in myset].pop())

