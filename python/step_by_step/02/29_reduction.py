# coding: utf-8

a, b, c, d = map(int, input().split())
tmp = 0
if a >= b:
    if d > c:
        tmp = a
        a = b
        b = tmp
else:
    if c > d:
        tmp = c
        c = d
        d = tmp

result = int(min(c/a, d/b) *100)
if result > 100:
    result = 100

print("{}%".format(result))

