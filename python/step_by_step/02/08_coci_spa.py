# coding: utf-8

h, m = map(int, input().split())

m -= 45
if m < 0:
    h -= 1
    m += 15
    if h < 0:
        h += 24
    elif h >= 24:
        h -= 24

print(h, m)

