# coding: utf-8

a, b, c = map(int, input().split())

if a <= 168:
    print("CRASH {}".format(a))
elif b <= 168:
    print("CRASH {}".format(b))
elif c <= 168:
    print("CRASH {}".format(c))
else:
    print("NO CRASH")

