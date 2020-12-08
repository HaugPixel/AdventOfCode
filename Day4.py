with open("input4.txt", "r") as fil:
    file = fil.read().split("\n\n")
    file2 = [i.split() for i in file]

wordlist=["byr","iyr","eyr", "hgt","hcl","ecl","pid"]

count1 = 0
for passport in file2:
    vali = True
    for word in wordlist:
        if word not in passport:
            vali = False
    if vali:
        count1+=1

count = 0
for passport in file2:
    valid = [False for i in range(7)]
    for cred in passport:
        if cred[:3] == 'byr':
            if '1920' <= (cred[4:]) <= '2002':
                valid[0] = True
        elif cred[:3] == 'iyr':
            if '2010' <= (cred[4:]) <= '2020':
                valid[1] = True
        elif cred[:3] == 'eyr':
            if '2020' <= (cred[4:]) <= '2030':
                valid[2] = True
        elif cred[:3] == 'hgt':
            if cred[-2:] == "cm":
                if '150' <= (cred[4:-2]) <= '193':
                    valid[3] = True
            if cred[-2:] == "in":
                if '59' <= (cred[4:-2]) <= '76':
                    valid[3] = True
        elif cred[:3] == 'hcl':
            if cred[4]=="#" and len(cred[5:])==6 and cred[5:].isalnum():
                valid[4] = True
        elif cred[:3] == 'ecl':
            if cred[4:] in ['amb','blu','brn','gry','grn','hzl','oth']:
                valid[5] = True
        elif cred[:3] == 'pid':
            if len(cred[4:]) == 9 and cred[4:].isdigit():
                valid[6] = True

    if all(valid):
        count+=1

print(count1)
print(count)

