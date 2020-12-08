def run(lines):
    acc = 0
    i = 0
    linesVisited = set()
    while i < len(lines):
        linesVisited.add(i)
        cmd, arg = lines[i].split()

        if cmd == "acc":
            acc += int(arg)
            i += 1
        elif cmd =="jmp":
            i += int(arg)
        else:
            i += 1
        if i in linesVisited:
            return 0
    return acc


def main():
    with open("test.txt", "r") as fil:
        lines = fil.readlines()
    for val, x in enumerate(lines):
        k = 0
        if x[:3] == 'nop':
            lines[val] = x.replace("nop", "jmp")
            k = run(lines)
            lines[val] = x.replace("jmp", "nop")
        elif x[:3] == 'jmp':
            lines[val] = x.replace("jmp", "nop")
            k = run(lines)
            lines[val] = x.replace("nop", "jmp")
        if k > 0:
            print(k)
            break

main()
