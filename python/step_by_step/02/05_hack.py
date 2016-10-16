# coding: utf-8

r, e, c = map(int, input().split())

e -= c
if r < e:
    print("advertise")
elif r == e:
    print("does not matter")
else:
    print("do not advertise")

