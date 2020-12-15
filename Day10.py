
def solve1(nums):

    sortedNums = sorted(nums)
    i = 1
    ones = 0
    threes = 0
    while i < len(nums):
        res = sortedNums[i]-sortedNums[i-1]
        if res == 1:
            ones += 1
        if res == 3:
            threes += 1
        i+=1

    return ones * threes


def solve2(nums):

    sortedNums = sorted(nums)
    chain = False

    i = 0
    acc = 1

    while i < len(nums):
        if i+4<len(nums) and sortedNums[i+4]-sortedNums[i]==4:
            acc *=7
            chain=True

        elif i+3<len(nums) and sortedNums[i+3]-sortedNums[i]==3:
            if not chain:
                acc *=4
                chain = True

        elif i+2<len(nums) and sortedNums[i+2]-sortedNums[i]==2:
            if not chain:
                acc *=2

        else:
            chain= False

        i+=1

    return acc



def main():
    with open("test.txt", "r") as fil:
        tall = [int(i) for i in fil.readlines()]
    tall.append(max(tall)+3)
    tall.append(0)

    print("Part1: ", solve1(tall))
    print("Part2: ", solve2(tall))

main()

"""
12345

1 345
1  45
1 3 5
12 45
12  5
123 5

"""