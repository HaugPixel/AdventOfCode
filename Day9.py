
def sol1(nums):
    i= 25
    while i < len(nums):
        toCheck = nums[i]
        sorted_sub = sorted(nums[i-25:i])
        k = 0
        j = 24
        found = False
        while k < j:
            res = sorted_sub[k]+sorted_sub[j]
            if res < toCheck:
                k += 1
            if res > toCheck:
                j -= 1
            if res == toCheck:
                found = True
                break
        if not found:
            return toCheck
        i+=1

    return -1

def sol2(tall, n):
    tall.remove(n)
    mySum = 0
    i= 0
    k= 0
    while i<len(tall):
        mySum += tall[k]
        if mySum < n:
            k+=1
        elif mySum > n:
            i+=1
            k=i
            mySum=0
        else:
            res_l = tall[i:k]
            return min(tall[i:k])+max(tall[i:k])

    return -1


def main():
    with open("input_9", "r") as fil:
        tall = [int(i) for i in fil.readlines()]

    answer1 = sol1(tall)
    answer2 = sol2(tall, answer1)
    print(answer1 ,answer2)


main()
