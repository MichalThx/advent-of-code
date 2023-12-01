#!/usr/bin/env python3


input = open("2023/day1_1.txt", "r")
i = 0
total = 0
for line in input:
    #print(line)
    i += 1
    line = line.strip()
    l,r = 0, len(line) - 1
    #print(line[l] + " :: " + line[r])
    #print(line)
    while True:
       # print(line[l] + " - " + line[r])
        if not line[l].isdigit():
            l += 1
        if not line[r].isdigit():
            r -= 1
        if line[l].isdigit() and line[r].isdigit():
            break
        if l > r:
            break
    #print(line[l] + ":"+line[r])
    total += int(line[l]+ line[r])
    #print(total)
    #if i == 10:
    #    break
print(total)

# text manipulation with
# sed -i 's/seven/se7ven/' 2023/day1_1.txt
# this allows for endings to be part of another digit
# while keeping them in the right order
