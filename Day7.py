def sol1(d):
    counter = 0
    for x in d.keys():
        bags = [i for i in d[x]]
        while bags:
            bag = bags.pop()
            if "no other bag" not in bag:
                n, c1, c2, _ = bag.split()
                col = " ".join([c1, c2])
                if col == "shiny gold":
                    counter += 1
                    break
                else:
                    bags = bags + d[col]

    return counter

def sol2(d):
    counter = 0
    bags = [i for i in d["shiny gold"]]
    while bags:
        bag = bags.pop()
        if "no other bag" not in bag:
            n, c1, c2, _ = bag.split()
            col = " ".join([c1, c2])
            counter += int(n)
            bags = bags + int(n) * d[col]

    return counter


def main():
    with open("seat.txt", "r") as file:
        lines = file.readlines()
        di = {i.split(" bags contain ")[0]: i.split(" bags contain ")[1].split(",") for i in lines}

    print("P1 =", sol1(di))
    print("P2 =", sol2(di))

main()