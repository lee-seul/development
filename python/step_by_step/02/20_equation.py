# coding: utf-8

a, b, c, d = map(int, input().split())

if a == c and b == d:
    print("many")
elif a == c:
    print("none")
elif a > c or c > a:
    a -= c
    b -= d
    print("{:.3f}".format(-(b/a)))

