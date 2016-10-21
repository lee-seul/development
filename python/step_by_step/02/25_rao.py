# coding: utf-8

l = list(map(int, input().split()))
l.sort()

a = l[0] ** 2 + l[1] ** 2
b = l[2] ** 2
if a > b:
    print("acute")
elif a == b:
    print("right")
else:
    print("obtuse")

