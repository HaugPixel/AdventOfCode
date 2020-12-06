with open("input6.txt", "r") as fil:
    cases = fil.read().split("\n\n")


count= 0
for case in cases:
     liste = []
     num = 0
     for pers in cases:
         num +=1
         for ch in pers:
             liste.append(ch)
     for car in set(liste):
         if liste.count(car)==num:
             count+=1

print(sum[len(set(i.replace("\n", ""))) for i in cases])
#print([int(i in set(i.replace("\n", ""))) for k in cases[:2] for i in k])
