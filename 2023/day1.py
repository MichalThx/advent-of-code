#!/usr/bin/env python3


input = open("2023/day1.txt", "r")
i = 0
total = 0
for line in input:
    #print(line)
    i += 1
    line = line.strip()
    l,r = 0, len(line) - 1
    #print(line[l] + " :: " + line[r])
    while True:
       # print(line[l] + " - " + line[r])
        if not line[l].isdigit():
            l += 1
        if not line[r].isdigit():
            r -= 1
        if line[l].isdigit() and line[r].isdigit():
            break
    total += int(line[l]+ line[r])
    #print(total)
    #if i == 5:
    #    break
print(total)