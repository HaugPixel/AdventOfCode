def solution(stepy, stepx, aMap):
    counter = 0
    x = 0
    for y in range(stepy, len(aMap), stepy):
        x = (x + stepx) % len(aMap[0])
        if aMap[y][k] == '#':
            counter+=1

    return counter


def main():
    myMap = filereader()
    print("Del 1: ", solution(1, 3, myMap))
    sol2 = solution(1, 1, myMap) * solution(1, 3, myMap) * solution(1, 5, myMap) * solution(1, 7, myMap) * solution(2, 1, myMap)
    print("Del 2: ", sol2)
