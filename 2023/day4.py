#!/usr/bin/env python3


input = open("2023/day4.txt", "r")

twos = [0] * 40
twos[0] = 0
twos[1] = 1
for i in range(2, 27):
    twos[i] = twos[i-1] * 2
#print(twos)
sum = 0
for line in input:
    line = line.strip()
    colon = line.split(":")
    clean = colon[1].split("|")
    left = clean[0].strip()
    right = clean[1].strip()
    left = left.split()
    #print(right)
    right = right.split()
    #print(len(right))
    #print(sorted(left))
    #print(sorted(right))
    count = 0
    for l in left:
        if l in right:
            count += 1
   # print(str(twos[count]) + " :: " + str(count))
    sum += twos[count]
#print(sum)

## PART TWO ##
input = open("2023/day4.txt", "r")

sum = 0
i = 1
wins = [1] * 204
for line in input:
    line = line.strip()
    colon = line.split(":")
    clean = colon[1].split("|")
    left = clean[0].strip()
    right = clean[1].strip()
    left = left.split()
    right = right.split()
    count = 0
    for l in left:
        if l in right:
            count += 1
    #print("----- :: " + str(i))

    #print(count)
    while count > 0:
#        print(count)
        wins[i + count] += wins[i]
        #print(str(wins[i + count]) + " :: " + str(i+count))
        count -= 1
    #print(wins)
    i += 1
    #if i == 3:
    #    break
print(wins)
for q in wins:
    sum += q
print(sum-1)
