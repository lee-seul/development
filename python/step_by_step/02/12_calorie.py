# coding: utf-8

a, b, c, d = map(int, input().split())

total = 0

if a == 1:
    total += 461
elif a == 2:
    total += 431
elif a == 3:
    total += 420

if b == 1:
    total += 130
elif b == 2:
    total += 160
elif b == 3:
    total += 118

if c == 1:
    total += 100
elif c == 2:
    total += 57
elif c == 3:
    total += 70

if d == 1:
    total += 167
elif d == 2:
    total += 266
elif d == 3:
    total += 75

print("Your total Calorie count is {}.".format(total))


