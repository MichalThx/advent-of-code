#!/usr/bin/env python3

from typing import List

input = open("2023/day3.txt", "r")

total = 0
lines = []
l = 0

def find_special(lines: List, y: int):
    valid = False
    if y < 0 or y >= len(lines[0]):
        return valid
    for x in range(3):
        #print("> " + lines[x][j])
        if not lines[x][y].isnumeric() and lines[x][y] != ".":
            valid = valid or True
    return valid

def check_line(lines: List) -> int:
    s = ""
    res = 0
    valid = False
    # print(lines)
    for i in range(len(line)):
        if lines[1][i].isnumeric():
            s += lines[1][i]
            if "48" in s:
                print(s)
            if valid == False:
                valid = valid or find_special(lines, i - 1)
                valid = valid or find_special(lines, i)
                valid = valid or find_special(lines, i + 1)
            if i == len(line) - 1:
                if s != "" and valid:
                    res += int(s)
                print(s + " valid ")
                if s!= "" and not valid:
                    print(s + " not ")
        else:
            if s != "" and valid:
                res += int(s)
                print(s + " valid ")
            if s!= "" and not valid:
                print(s + " not ")
            s = ""
            valid = False
    lines.pop(0)
    return res


#for line in input:
#    line = line.strip()
#
#    if len(lines) == 0:
#        l = len(line)
#        lines.append(l * ["."])
#    lines.append(line)
    #print(lines)
   # break
#    if len(lines) == 3:
#        total += check_line(lines)

#print(len(lines))
#lines.append(l * ".")
#total += check_line(lines)
#print(lines)
#lines.append(l * ".")
#total += check_line(lines)
#print(lines)
#print(total)


## PART TWO

input = open("2023/day3.txt")

d = {}
y = 0

lines = []
def find_star(lines, x, y):
    ds = [-1, 0, 1]
    r = []
    for i in ds:
        for j in ds:
            xp = x + i
            yp = y + j
            if xp >= 0 and xp < len(lines[0]) and yp >= 0 and yp < len(lines):
                if lines[yp][xp] == "*":
                    r.append((yp, xp))
    return r
for line in input:
    line = line.strip()
    lines.append(line)
print(d)
for y,line in enumerate(lines):
    s = ""
    r = []
    for x, c in enumerate(line):
        if c.isnumeric():
            s += c
            for pair in find_star(lines,x, y):
                #print(pair)
                if pair in d:
                    if "A" not in d[pair]:
                        d[pair].append("A")
                else:
                    d[pair] = ["A"]
            if x == len(line) - 1:
                if s != "":
                    for k in d:
                 #       print(k)
                        l = d[k]
                        if "A" in l:
                            l.remove("A")
                            l.append(s)
        else:
            if s != "":
               # print(d)
                for k in d:
                #    print(k)
                    l = d[k]
                    if "A" in l:
                        l.remove("A")
                        l.append(s)
            s = ""
            r = []
result = 0
for k in d:
    if len(d[k]) == 2:
        #print(d[k])
        result += int(d[k][0]) * int(d[k][1])
print(result)
