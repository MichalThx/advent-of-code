#!/usr/bin/env python3

from typing import List

input = open("2023/day2.txt", "r")


# which games are possible with 12r, 13g, 14b

string = "Game 1: 1 blue; 4 green, 5 blue; 11 red, 3 blue, 11 green; 1 red, 10 green, 4 blue; 17 red, 12 green, 7 blue; 3 blue, 19 green, 15 red"


#print(string.split(":"))


def extract_id(day: str) -> int:
    arr = day.split(" ")
    return int(arr[1])

def extract_ball_numbers(line: str) -> List:
    arr = line.split(";")
    colours = { "red": 0, "green": 0, "blue": 0 }
    for a in arr:
        col = a.strip().split(",")
        for c in col:
            n = c.strip().split(" ")
           # print(str(n[0]) + " :: " + str(n[1]))
            colours[n[1]] = max(int(n[0]), colours[n[1]])
        #print("--")
    return colours


#print(extract_id(string.split(":")[0]))
#print(extract_ball_numbers(string.split(":")[1]))
total = 0
for line in input:
    clean = line.strip().split(":")
    id = extract_id(clean[0])
    col = extract_ball_numbers(clean[1])
    # PART ONE
    #if col["red"] <= 12 and col["green"] <= 13 and col["blue"] <= 14:
    #    total += id
    # PART TWO
    total += (col["red"] * col["green"] * col["blue"])
print(total)
